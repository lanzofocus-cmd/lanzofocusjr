"""THE FIRE THAT DIDN'T BURN OUT — a spark, a wind that wants it gone, and the hands that protect it.

World: a dark moorland at night under heavy blue cloud. THE SPARK is a single ember. THE WIND arrives as grey-blue
ribbons of air with a cold face that tear at it until it's nearly gone. THE FIREKEEPER, a figure in a deep red
hooded cloak, kneels and cups it; it becomes a flame, a bonfire, and then beacon after beacon lights along the
hills to the horizon, embers rising into the night.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, stars, dust)
from kit import s_follow

TITLE = ("THE FIRE THAT", "DIDN'T BURN OUT")
OUTPUT = "128_The_Fire_That_Didnt_Burn_Out_16x9.mp4"
LINES = [
    "",
    "",
    "Every great fire…",
    "Started small.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.6, 4: 3.6}
GAPS = {2: 2.4, 3: 6.0}

FIRE = (255, 140, 40, 255)
EMBER = (255, 200, 90, 255)
KEEPER = (170, 40, 40, 255)
WIND = (150, 170, 210, 255)
CH = 260
BEACONS = [(-2600 + i * 700, -200 - 420 * abs(math.sin(i * 0.75 + 0.4))) for i in range(12)]


def moor(d, cam, t, glowk=0.0):
    draw_sky(d, mix((4, 6, 14, 255), (40, 20, 20, 255), glowk * 0.5), mix((14, 18, 34, 255), (90, 40, 30, 255), glowk * 0.6))
    stars(d, 0.5, seed=8, n=50, ymax=0.4)
    for f, c, base in ((0.4, (16, 18, 28), -260), (0.7, (12, 14, 22), -140)):
        pts = []
        for i in range(40):
            x = -8000 + i * 420
            y = base - 120 * abs(math.sin(i * 0.7 + f * 5))
            zz = cam.z * (0.5 + 0.5 * f)
            pts.append(((x - cam.cx * f) * zz + W / 2, (y - cam.cy * f) * zz + H / 2))
        pts += [(W + 10, H + 10), (-10, H + 10)]
        d.polygon(pts, fill=c + (255,))
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=(18, 16, 20, 255))
    r = random.Random(3)
    for i in range(80):  # grass tufts
        x = r.uniform(-1500, 1500)
        gx, gyy = cam.p(x, 0)
        if -20 < gx < W + 20:
            for k in (-1, 0, 1):
                d.line([(gx, gyy), (gx + k * cam.s(10) + math.sin(t * 2 + i) * cam.s(6), gyy - cam.s(40 + 20 * abs(k)))], fill=(40, 46, 40, 255), width=max(1, int(cam.s(3))))


def ridge(d, cam):
    pts = [cam.p(-3400, 0)] + [cam.p(x, y) for x, y in BEACONS] + [cam.p(5200, 0)]
    d.polygon(pts + [cam.p(5200, 400), cam.p(-3400, 400)], fill=(14, 13, 18, 255))
    polyline(d, pts, 1, col((90, 50, 40, 255), 0.6), 2)


def flame(d, cam, x, y, size, t, a=1.0):
    """A layered flame of height `size` (world units) at (x, y)."""
    if size <= 0:
        return
    sx, sy = cam.p(x, y)
    h = cam.s(size)
    glow(d, sx, sy - h * 0.4, h * 2.5, FIRE, 0.7 * a)
    for k, c in enumerate(((220, 70, 30), (255, 140, 40), (255, 210, 110))):
        hh = h * (1 - k * 0.28)
        w = hh * 0.42
        pts = [(sx - w, sy)]
        for j in range(1, 8):
            u = j / 8
            pts.append((sx - w * (1 - u) + math.sin(t * 9 + j + k) * w * 0.15, sy - hh * u * (0.8 + 0.2 * math.sin(t * 7 + j))))
        pts.append((sx + math.sin(t * 11 + k) * w * 0.2, sy - hh))
        for j in range(7, 0, -1):
            u = j / 8
            pts.append((sx + w * (1 - u) + math.sin(t * 8 + j * 1.3 + k) * w * 0.15, sy - hh * u * (0.8 + 0.2 * math.sin(t * 6 + j))))
        pts.append((sx + w, sy))
        d.polygon(pts, fill=col(c + (255,), a))


def ember(d, cam, x, y, k, t):
    sx, sy = cam.p(x, y)
    r = cam.s(8 + 6 * k)
    glow(d, sx, sy, cam.s(120) * (0.3 + k), EMBER, 0.8 * k)
    d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=col(mix((120, 40, 20, 255), EMBER, k), 1))


def wind(d, cam, t, a=1.0, face=True):
    if a <= 0.01:
        return
    for j in range(9):
        y = -120 - j * 70
        pts = []
        for i in range(30):
            x = -1600 + i * 110 + (t * 900) % 110
            pts.append(cam.p(x, y + math.sin(i * 0.4 + t * 3 + j) * 40))
        polyline(d, pts, 1, col(WIND, 0.35 * a), max(2, int(cam.s(8))))
    if face:
        fx, fy = cam.p(-650, -560)
        R = cam.s(170)
        tpoly(d, [(fx - R, fy - R * 0.8), (fx + R, fy + R * 0.8)], col(WIND, 0.25 * a), kind="ellipse")
        for o in (-1, 1):
            d.ellipse([fx + o * R * 0.35 - R * 0.08, fy - R * 0.15, fx + o * R * 0.35 + R * 0.08, fy], fill=col((230, 240, 255, 255), a))
        d.ellipse([fx + R * 0.1, fy + R * 0.2, fx + R * 0.4, fy + R * 0.45], outline=col((230, 240, 255, 255), a), width=max(2, int(cam.s(8))))
        d.text((fx, fy - R * 1.1), "THE WIND", font=font(int(clamp(cam.s(40), 14, 40))), fill=col(WIND, a), anchor="mm")


def keeper(d, cam, t, cup=1.0, a=1.0):
    fx, fy = cam.p(-120, 0)
    h = cam.s(CH)
    hands = ((fx + h * 0.32, fy - h * 0.1), (fx + h * 0.46, fy - h * 0.12)) if cup > 0 else None
    figure(d, fx, fy, h, KEEPER, mode="kneel", face=1, acc=("hood",), hands=hands, a=a, head_down=0.4, name="THE FIREKEEPER")


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # black; a flint strikes; one ember floats down and settles in the grass
    cam = Cam(60, -60, 2.6)
    moor(d, cam, t)
    strike = pulse(t, 0.6, 0.1)
    k = ramp(t, 0.6, 0.3)
    y = lerp(-220, -10, sstep(ramp(t, 0.7, 1.6)))
    if k > 0:
        ember(d, cam, 60 + 20 * math.sin(t * 2), y, k, t)
    if strike > 0:
        particles(d, *cam.p(60, -220), cam.s(140), strike, EMBER, n=20, seed=1, rise=0.3)
    darkness(d, *cam.p(60, y), 0.95)


def s1_wind(d, t, dur):
    p = t / dur
    # the wind arrives; the ember fades almost to nothing; then two red sleeves cup around it
    cam = cam_lerp((60, -60, 2.6), (0, -160, 1.2), sstep(p))
    shake(cam, t, 4 * (1 - ramp(p, 0.6, 0.3)))
    moor(d, cam, t)
    wind(d, cam, t, a=ramp(t, 0.2, 0.6) * (1 - sstep(ramp(p, 0.65, 0.3))))
    k = lerp(1.0, 0.15, sstep(ramp(p, 0.1, 0.45))) + 0.4 * sstep(ramp(p, 0.75, 0.25))
    ember(d, cam, 60 + 30 * math.sin(t * 6) * (1 - p), -10, k, t)
    keeper(d, cam, t, cup=1.0, a=sstep(ramp(p, 0.5, 0.3)))
    darkness(d, *cam.p(60, -10), 0.7)


def s2_great(d, t, dur):
    p = t / dur
    # in the shelter of the hands, a flame; twigs; it climbs
    cam = cam_lerp((0, -160, 1.2), (0, -260, 0.9), sstep(p))
    moor(d, cam, t, glowk=0.3 * p)
    keeper(d, cam, t, cup=1.0 - ramp(p, 0.7, 0.2))
    for i in range(int(6 * sstep(p))):  # twigs
        a = i * 0.5 - 1.2
        x0, y0 = cam.p(60 + math.cos(a) * 60, -4)
        d.line([(x0, y0), cam.p(60 - math.cos(a) * 60, -20)], fill=(90, 60, 40, 255), width=max(2, int(cam.s(10))))
    flame(d, cam, 60, -10, lerp(40, 220, sstep(p)), t)
    dust(d, t, 0.4 * p, n=30, color=(255, 170, 90), rise=60)
    top_caption(d, ["EVERY GREAT FIRE…"], t, dur, accent={"GREAT", "FIRE…"})


def s3_small(d, t, dur):
    p = t / dur
    # a roaring bonfire, then beacon after beacon lighting along the hills to the horizon
    cam = cam_lerp((0, -260, 0.9), (-200, -500, 0.28), sstep(ramp(p, 0.15, 0.6)))
    lit = ramp(p, 0.25, 0.65)
    moor(d, cam, t, glowk=0.4 + 0.6 * lit)
    ridge(d, cam)
    keeper(d, cam, t, cup=0)
    flame(d, cam, 60, -10, lerp(220, 520, sstep(ramp(p, 0.0, 0.3))), t)
    for i, (bx, by) in enumerate(BEACONS):
        k = clamp(lit * len(BEACONS) - abs(i - 4) * 0.9)
        if k > 0:
            flame(d, cam, bx, by, 300 * k, t + i)
    particles(d, *cam.p(60, -400), cam.s(1400), (t * 0.3) % 1, EMBER, n=60, seed=int(t * 0.3), rise=1.2, size=4)
    dust(d, t, 0.7, n=60, color=(255, 170, 90), rise=80)
    top_caption(d, ["STARTED SMALL."], t, dur, accent={"SMALL."})


def s4_end(d, t, dur):
    cam = Cam(-200, -500, 0.28)
    moor(d, cam, t, glowk=1.0)
    ridge(d, cam)
    keeper(d, cam, t, cup=0)
    flame(d, cam, 60, -10, 520, t)
    for i, (bx, by) in enumerate(BEACONS):
        flame(d, cam, bx, by, 300, t + i)
    dust(d, t, 0.7, n=60, color=(255, 170, 90), rise=80)
    stage_end(d, t, dur, ["PROTECT YOUR SPARK."], [EMBER], size=120, dim=0.4, glow_col=FIRE, y=H * 0.3)


SCENES = [s0_hook, s1_wind, s2_great, s3_small, s4_end, s_follow]
