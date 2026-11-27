"""THE BRICKS OF A FUTURE — one brick a day, against a storm that knocks them down, until a tower meets the clouds.

World: a lone tower rising from an open plain, shot as one long upward crane move through days and nights,
rain and snow. THE ARCHITECT (white helmet, orange vest) sets one brick at a time with a trowel. THE DESTROYER
is a dark whirling storm with two pale eyes that tears the top courses off. The architect rebuilds every time;
the tower climbs through the cloud layer into gold light.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, rain, snow, stars, sun, cloud, dust)
from kit import s_follow

TITLE = ("THE BRICKS", "OF A FUTURE")
OUTPUT = "126_The_Bricks_Of_A_Future_16x9.mp4"
LINES = [
    "",
    "One brick doesn't look like progress.",
    "",
    "Until you see the building.",
    "",
    "",
]
SILENT = {0: 3.0, 2: 4.2, 4: 3.4}
GAPS = {1: 3.4, 3: 5.0}

BRICK = (190, 90, 60, 255)
ARCH = (255, 140, 50, 255)
TW = 420          # tower width
BH = 60           # course height
CH = 170


def sky_at(d, cam, t, hour, alt=0.0):
    """hour: 0..1 day cycle (0.5 noon); alt raises us toward the gold above the clouds."""
    day = clamp(math.sin(hour * math.pi) * 1.6)
    top = mix(mix((6, 8, 24, 255), (80, 140, 220, 255), day), (40, 30, 80, 255), alt)
    bot = mix(mix((20, 24, 50, 255), (255, 190, 140, 255), day), (255, 200, 130, 255), alt)
    draw_sky(d, top, bot)
    stars(d, (1 - day) * 0.8 * (1 - alt), seed=3, n=80)
    if day > 0.05:
        sun(d, lerp(W * 0.1, W * 0.9, hour), H * (0.7 - 0.5 * math.sin(hour * math.pi)), 60, day, (255, 220, 160, 255))


def tower(d, cam, rows, t, top_damage=0.0):
    """rows: number of courses (float); the top course is being laid. top_damage knocks bricks off the top."""
    n = int(rows)
    r = random.Random(1)
    for row in range(n + 1):
        y = -row * BH
        a, b = cam.p(-TW / 2, y - BH), cam.p(TW / 2, y)
        if b[1] < -20 or a[1] > H + 20:
            continue
        cnt = 4
        frac = 1.0 if row < n else rows - n
        for c in range(cnt):
            if c / cnt >= frac:
                break
            off = (TW / cnt / 2) if row % 2 else 0
            x0 = -TW / 2 + c * TW / cnt + off * 0
            p0, p1 = cam.p(x0 + 3, y - BH + 3), cam.p(x0 + TW / cnt - 3, y - 3)
            d.rectangle([p0[0], p0[1], p1[0], p1[1]], fill=col(mix(BRICK, (150, 70, 50, 255), r.random() * 0.5), 1))
        # windows every few courses once the tower is tall
        if row % 3 == 1 and row > 6:
            for c in range(2):
                wx = -TW / 4 + c * TW / 2
                q0, q1 = cam.p(wx - 30, y - BH + 12), cam.p(wx + 30, y - 12)
                d.rectangle([q0[0], q0[1], q1[0], q1[1]], fill=(255, 210, 130, 255))


def architect(d, cam, rows, t, mode="hammer"):
    y = -int(rows) * BH
    fx, fy = cam.p(TW / 2 - 60, y)
    figure(d, fx, fy, cam.s(CH), ARCH, mode=mode, phase=t * 5, face=-1, acc=("cap",), name="THE ARCHITECT")


def destroyer(d, cam, x, y, t, a=1.0, size=1.0):
    sx, sy = cam.p(x, y)
    R = cam.s(300) * size
    for k in range(7):
        rr = R * (1 - k * 0.12)
        ang = t * (3 + k)
        tpoly(d, [(sx - rr, sy - rr * 0.5), (sx + rr, sy + rr * 0.5)], col((20, 16, 30, 255), 0.25 * a), kind="ellipse")
        polyline(d, [(sx + math.cos(ang + j * 0.35) * rr, sy + math.sin(ang + j * 0.35) * rr * 0.45) for j in range(10)], 1, col((140, 130, 170, 255), 0.5 * a), 3)
    for o in (-1, 1):
        d.ellipse([sx + o * R * 0.2 - R * 0.06, sy - R * 0.05, sx + o * R * 0.2 + R * 0.06, sy + R * 0.05], fill=col((230, 230, 255, 255), a))
    d.text((sx, sy - R * 0.7), "THE DESTROYER", font=font(int(clamp(R * 0.12, 14, 36))), fill=col((200, 190, 230, 255), a), anchor="mm")


def cloud_bank(d, cam, t):
    r = random.Random(5)
    for j in range(16):
        x = -3200 + j * 420 + (t * 30) % 420
        y = -55 * BH + r.uniform(-120, 120)
        rx, ry = r.uniform(300, 520), r.uniform(120, 200)
        a, b = cam.p(x - rx, y - ry), cam.p(x + rx, y + ry)
        tpoly(d, [a, b], col((255, 245, 235, 255), 0.85), kind="ellipse")


def ground(d, cam):
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=(90, 80, 70, 255))


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # macro at dawn: a trowel of mortar, one brick pressed down onto it
    cam = Cam(0, -30, 4.0)
    sky_at(d, cam, t, 0.15)
    ground(d, cam)
    press = sstep(ramp(t, 0.8, 0.8))
    p0, p1 = cam.p(-60, -6), cam.p(60, 0)
    d.rectangle([p0[0], p0[1], p1[0], p1[1]], fill=(200, 190, 180, 255))  # mortar
    by = lerp(-160, 0, press)
    b0, b1 = cam.p(-55, by - BH + 3), cam.p(55, by - 3)
    d.rectangle([b0[0], b0[1], b1[0], b1[1]], fill=col(BRICK, 1))
    if press > 0.95:
        particles(d, *cam.p(0, -3), cam.s(90), ramp(t, 1.6, 0.6), (200, 190, 180), n=14, seed=1, rise=0.2)
    hx, hy = cam.p(80, by - BH - 10)
    d.line([(hx, hy), (hx + cam.s(80), hy - cam.s(50))], fill=(150, 110, 70, 255), width=int(cam.s(10)))


def s1_progress(d, t, dur):
    p = t / dur
    # days flash by; the tower creeps up; the Destroyer tears the top off; the architect rebuilds
    hour = (t * 0.6) % 1
    rows = lerp(1, 14, p)
    hit = pulse(p, 0.55, 0.12)
    if 0.5 < p < 0.62:
        rows -= 5 * sstep((p - 0.5) / 0.06) if p < 0.56 else 5 * (1 - sstep((p - 0.56) / 0.06)) + 0.0
    cam = Cam(0, -rows * BH * 0.6 - 150, 0.9)
    shake(cam, t, 10 * hit)
    sky_at(d, cam, t, hour)
    ground(d, cam)
    tower(d, cam, rows, t)
    if 0.4 < p < 0.75:
        k = math.sin(math.pi * (p - 0.4) / 0.35)
        destroyer(d, cam, lerp(-800, 300, (p - 0.4) / 0.35), -rows * BH - 150, t, a=k)
        if hit > 0:
            particles(d, *cam.p(0, -rows * BH), cam.s(400), ramp(p, 0.55, 0.15), BRICK, n=20, seed=2, rise=-0.5, size=8)
    architect(d, cam, rows, t)
    d.text((W - 120, H - 100), f"DAY {int(1 + 120 * p)}", font=font(32), fill=col(WHITE, 0.8), anchor="rm")
    top_caption(d, ["ONE BRICK DOESN'T", "LOOK LIKE PROGRESS."], t, dur, accent={"ONE", "BRICK"})


def s2_rebuild(d, t, dur):
    p = t / dur
    # the long climb: weather changes, the Destroyer strikes again, the camera keeps rising with the top
    rows = lerp(14, 60, p)
    hour = (t * 0.7 + 0.3) % 1
    cam = Cam(0, -rows * BH + 200, 0.75)
    sky_at(d, cam, t, hour, alt=0.3 * p)
    tower(d, cam, rows, t)
    architect(d, cam, rows, t)
    seg = int(p * 3)
    if seg == 0:
        rain(d, t, 0.8, n=150)
    elif seg == 1:
        snow(d, t, 1.0, n=120)
    if 0.6 < p < 0.85:
        destroyer(d, cam, lerp(700, -300, (p - 0.6) / 0.25), -rows * BH - 200, t, a=math.sin(math.pi * (p - 0.6) / 0.25), size=0.8)
    d.text((W - 120, H - 100), f"DAY {int(120 + 900 * p)}", font=font(32), fill=col(WHITE, 0.8), anchor="rm")


def s3_building(d, t, dur):
    p = t / dur
    # through the cloud layer, then a long pull-back: a tower that reaches above the clouds
    rows = lerp(60, 90, sstep(ramp(p, 0.0, 0.4)))
    cam = cam_lerp((0, -60 * BH + 200, 0.75), (0, -45 * BH, 0.16), sstep(ramp(p, 0.25, 0.75)))
    sky_at(d, cam, t, 0.55, alt=lerp(0.3, 1.0, sstep(p)))
    ground(d, cam)
    tower(d, cam, rows, t)
    # cloud layer around the tower's middle
    cloud_bank(d, cam, t)
    architect(d, cam, rows, t, mode="cheer" if p > 0.4 else "hammer")
    glow(d, *cam.p(0, -rows * BH), cam.s(900), (255, 210, 140), 0.5 * p)
    top_caption(d, ["UNTIL YOU SEE", "THE BUILDING."], t, dur, accent={"BUILDING."})


def s4_end(d, t, dur):
    cam = Cam(0, -45 * BH, 0.16)
    sky_at(d, cam, t, 0.55, alt=1.0)
    ground(d, cam)
    tower(d, cam, 90, t)
    cloud_bank(d, cam, t)
    glow(d, *cam.p(0, -90 * BH), cam.s(900), (255, 210, 140), 0.5)
    stage_end(d, t, dur, ["ONE BRICK A DAY."], [(255, 210, 150, 255)], size=120, dim=0.4, glow_col=(255, 200, 130), y=H * 0.62)


SCENES = [s0_hook, s1_progress, s2_rebuild, s3_building, s4_end, s_follow]
