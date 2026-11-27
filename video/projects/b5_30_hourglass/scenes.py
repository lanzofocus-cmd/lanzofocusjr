"""THE FINAL HOURGLASS — a person tries to stop the sand, and learns to plant a garden instead.

World: a dusk desert of rose and violet dunes, a monumental hourglass taller than a house, its sand a glittering
gold stream. THE PERSON pushes against the glass, wraps their arms round it, shakes it. THE KEEPER, an old robed
figure in grey-teal with a staff, lays a hand on their shoulder. The person turns away from the glass and plants;
around the hourglass, a garden grows in time-lapse while the last of the sand falls.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, dust, sun, stars)
from kit import s_follow

TITLE = ("THE FINAL", "HOURGLASS")
OUTPUT = "130_The_Final_Hourglass_16x9.mp4"
LINES = [
    "",
    "",
    "You cannot stop the sand.",
    "But you can decide what you do before it falls.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.6, 4: 3.4}
GAPS = {2: 1.8, 3: 6.0}

SAND = (255, 200, 110, 255)
GLASS = (200, 220, 240, 255)
WOOD = (110, 70, 40, 255)
YOU = (236, 228, 214, 255)
KEEPER = (130, 170, 170, 255)
CH = 230
HG_H = 1300


def desert(d, cam, t, green=0.0):
    draw_sky(d, (70, 50, 110, 255), (255, 160, 130, 255))
    stars(d, 0.3, seed=4, n=40, ymax=0.3)
    sun(d, W * 0.2, cam.p(0, 0)[1] - cam.s(150), 70, 0.9, (255, 210, 160, 255))
    for f, c, base in ((0.3, (190, 120, 120), -200), (0.6, (210, 140, 110), -80)):
        pts = []
        for i in range(30):
            x = -6000 + i * 420
            y = base - 140 * (0.5 + 0.5 * math.sin(i * 0.8 + f * 4))
            zz = cam.z * (0.5 + 0.5 * f)
            pts.append(((x - cam.cx * f) * zz + W / 2, (y - cam.cy * f) * zz + H / 2))
        pts += [(W + 10, H + 10), (-10, H + 10)]
        d.polygon(pts, fill=c + (255,))
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=mix((220, 160, 110, 255), (120, 160, 90, 255), green * 0.7))


def hourglass(d, cam, t, sand=0.0, shake_a=0.0):
    """sand: 0 full top .. 1 all fallen."""
    sx = math.sin(t * 40) * shake_a * cam.s(8)
    cx, base = cam.p(0, 0)
    cx += sx
    top = cam.p(0, -HG_H)[1]
    w = cam.s(420)
    neck = cam.s(30)
    mid = (top + base) / 2
    # frame
    for yy in (top, base - cam.s(50)):
        d.rounded_rectangle([cx - w - cam.s(60), yy, cx + w + cam.s(60), yy + cam.s(50)], int(cam.s(14)), fill=col(WOOD, 1))
    for s in (-1, 1):
        d.rectangle([cx + s * (w + cam.s(30)) - cam.s(20), top, cx + s * (w + cam.s(30)) + cam.s(20), base], fill=col(WOOD, 1))
    t0, b0 = top + cam.s(50), base - cam.s(50)
    upper = [(cx - w, t0), (cx + w, t0), (cx + neck, mid), (cx - neck, mid)]
    lower = [(cx - neck, mid), (cx + neck, mid), (cx + w, b0), (cx - w, b0)]
    # sand in the top bulb (a shrinking triangle) and the bottom (a growing mound)
    level = lerp(t0 + cam.s(60), mid, sand)
    if sand < 1:
        k = (mid - level) / (mid - t0)
        d.polygon([(cx - w * k, level), (cx + w * k, level), (cx + neck, mid), (cx - neck, mid)], fill=col(SAND, 1))
    mound = (b0 - mid) * 0.75 * sand
    d.polygon([(cx - w * 0.95, b0), (cx - w * 0.95 * min(1, sand * 1.5), b0 - mound * 0.3), (cx, b0 - mound), (cx + w * 0.95 * min(1, sand * 1.5), b0 - mound * 0.3), (cx + w * 0.95, b0)],
              fill=col(SAND, 1))
    if sand < 1:  # the falling stream, glittering
        d.line([(cx, mid), (cx, b0 - mound)], fill=col(SAND, 1), width=max(2, int(cam.s(10))))
        r = random.Random(int(t * 20))
        for i in range(12):
            yy = lerp(mid, b0 - mound, r.random())
            ox = r.uniform(-6, 6)
            d.ellipse([cx - 3 + ox, yy - 3, cx + 3 + ox, yy + 3], fill=(255, 245, 210, 255))
    for pts in (upper, lower):
        tpoly(d, pts, col(GLASS, 0.12))
        polyline(d, pts + [pts[0]], 1, col(GLASS, 0.8), max(2, int(cam.s(6))))
    glow(d, cx, mid, cam.s(500), SAND, 0.25)


def garden(d, cam, t, k):
    """Plants grown around the hourglass, k 0..1."""
    if k <= 0:
        return
    r = random.Random(6)
    for i in range(26):
        x = r.choice([-1, 1]) * r.uniform(550, 2200)
        kk = clamp(k * 1.5 - r.random() * 0.5)
        if kk <= 0:
            continue
        hgt = r.uniform(120, 520) * kk
        bx, by = cam.p(x, 0)
        if r.random() < 0.4:  # tree
            d.line([(bx, by), (bx, by - cam.s(hgt))], fill=(110, 80, 50, 255), width=max(2, int(cam.s(20))))
            rr = cam.s(hgt * 0.4)
            d.ellipse([bx - rr, by - cam.s(hgt) - rr, bx + rr, by - cam.s(hgt) + rr], fill=mix((80, 150, 80, 255), (120, 190, 100, 255), r.random()))
        else:  # flowers
            d.line([(bx, by), (bx, by - cam.s(hgt * 0.4))], fill=(80, 140, 70, 255), width=max(1, int(cam.s(6))))
            fr = cam.s(26 * kk)
            d.ellipse([bx - fr, by - cam.s(hgt * 0.4) - fr, bx + fr, by - cam.s(hgt * 0.4) + fr], fill=r.choice([(255, 120, 150, 255), (255, 220, 90, 255), (200, 140, 255, 255)]))


def person(d, cam, t, x, mode="stand", **kw):
    fx, fy = cam.p(x, 0)
    figure(d, fx, fy, cam.s(CH), YOU, mode=mode, phase=kw.pop("phase", t * 4), face=kw.pop("face", 1), acc=("hair",), **kw)


def keeper(d, cam, t, x, a=1.0):
    fx, fy = cam.p(x, 0)
    h = cam.s(CH * 1.15)
    figure(d, fx, fy, h, KEEPER, mode="reach", face=-1, a=a, acc=("hood",), bodyw=1.5, name="THE KEEPER", name_a=a, look=-0.2)
    d.line([(fx - h * 0.25, fy), (fx - h * 0.3, fy - h * 1.1)], fill=col((150, 120, 90, 255), a), width=max(2, int(h * 0.03)))


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # macro on the neck of the glass: grains of gold falling, glittering
    cam = cam_lerp((0, -HG_H / 2, 3.2), (0, -HG_H / 2, 1.6), sstep(p))
    desert(d, cam, t)
    hourglass(d, cam, t, sand=0.25)


def s1_stop(d, t, dur):
    p = t / dur
    # pushing against the glass; arms around it; shaking it; the sand doesn't care
    cam = cam_lerp((0, -500, 0.75), (-150, -450, 0.85), p)
    i = min(2, int(p * 3))
    shake_a = 1.0 if i == 2 else 0.0
    shake(cam, t, 6 * shake_a)
    desert(d, cam, t)
    hourglass(d, cam, t, sand=lerp(0.25, 0.4, p), shake_a=shake_a)
    if i == 0:
        person(d, cam, t, -520, mode="reach", lean=0.4, tired=0.6)
    elif i == 1:
        person(d, cam, t, -470, mode="reach", lean=0.1, look=0.6, mouth=-0.5)
    else:
        person(d, cam, t, -500, mode="pull", phase=t * 14, lean=0.2)


def s2_cannot(d, t, dur):
    p = t / dur
    cam = cam_lerp((-150, -450, 0.85), (-300, -420, 0.9), sstep(p))
    desert(d, cam, t)
    hourglass(d, cam, t, sand=lerp(0.4, 0.5, p))
    person(d, cam, t, -500, mode="slump", head_down=0.5)
    keeper(d, cam, t, -780, a=ramp(t, 0.2, 0.6))
    top_caption(d, ["YOU CANNOT", "STOP THE SAND."], t, dur, accent={"CANNOT", "SAND."})


def s3_decide(d, t, dur):
    p = t / dur
    # the person turns away from the glass and starts planting; a garden grows in time-lapse as the sand runs out
    k = sstep(ramp(p, 0.1, 0.85))
    cam = cam_lerp((-300, -420, 0.9), (0, -650, 0.38), sstep(ramp(p, 0.1, 0.8)))
    desert(d, cam, t, green=k)
    garden(d, cam, t, k)
    hourglass(d, cam, t, sand=lerp(0.5, 0.96, p))
    keeper(d, cam, t, -780, a=1 - sstep(ramp(p, 0.1, 0.3)))
    x = lerp(-500, -1400, k) + 300 * math.sin(p * 6)
    person(d, cam, t, x, mode="kneel" if math.sin(t * 2) > 0 else "walk", phase=t * 5, face=-1 if math.cos(p * 6) > 0 else 1, mouth=0.5)
    dust(d, t, 0.5 * k, n=50, color=(255, 230, 170))
    top_caption(d, ["BUT YOU CAN DECIDE WHAT YOU", "DO BEFORE IT FALLS."], t, dur, accent={"DECIDE"})


def s4_end(d, t, dur):
    cam = Cam(0, -650, 0.38)
    desert(d, cam, t, green=1.0)
    garden(d, cam, t, 1.0)
    hourglass(d, cam, t, sand=0.97)
    person(d, cam, t, -1100, mode="stand", mouth=0.6)
    stage_end(d, t, dur, ["DECIDE WHAT", "YOU DO."], [WHITE, SAND], size=110, dim=0.4, glow_col=SAND, y=H * 0.3)


SCENES = [s0_hook, s1_stop, s2_cannot, s3_decide, s4_end, s_follow]
