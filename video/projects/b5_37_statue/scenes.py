"""THE STATUE THAT NEVER MOVED — a block of marble waiting to become perfect on its own.

World: a moonlit stone courtyard with arches. A raw marble block on a plinth. THE FIRST SCULPTOR sits and stares at
it, waiting for perfection to appear; seasons pass, DUST and moss settle, the sculptor leaves. THE SECOND SCULPTOR
arrives and starts striking. Chips fly cell by cell, and out of the stone emerges a figure reaching upward, glowing
in the first light.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, stars, moon, sun, dust, snow)
from kit import s_follow

TITLE = ("THE STATUE THAT", "NEVER MOVED")
OUTPUT = "137_The_Statue_That_Never_Moved_16x9.mp4"
LINES = [
    "",
    "Perfection doesn't appear.",
    "",
    "It's created.",
    "",
    "",
]
SILENT = {0: 3.2, 2: 3.2, 4: 3.6}
GAPS = {1: 4.2, 3: 6.2}

MARBLE = (236, 232, 226, 255)
DUSTY = (150, 146, 140, 255)
S1 = (150, 160, 190, 255)
S2 = (255, 170, 90, 255)
BW, BH = 520, 900    # block size
CELL = 52
CELLS = [(cx, cy) for cx in range(int(BW / CELL)) for cy in range(int(BH / CELL))]
_r = random.Random(37)
ORDER = sorted(CELLS, key=lambda c: (abs(c[0] - BW / CELL / 2) * -1 + _r.uniform(-2, 2), -c[1]))
ORDER = sorted(CELLS, key=lambda c: -(c[1] * 0.4) + _r.uniform(0, 6))


def courtyard(d, cam, t, dawn=0.0):
    draw_sky(d, mix((8, 10, 26, 255), (120, 150, 210, 255), dawn), mix((30, 34, 60, 255), (255, 200, 160, 255), dawn))
    stars(d, 0.7 * (1 - dawn), seed=37, n=60, ymax=0.4)
    if dawn < 0.9:
        moon(d, W * 0.82, H * 0.16, 50, 1 - dawn, bg=(8, 10, 26))
    if dawn > 0.05:
        sun(d, W * 0.15, H * 0.55, 80, dawn, (255, 220, 160, 255))
    for k in range(-3, 4):  # arches
        x = k * 700
        a, b = cam.p(x - 260, -1300), cam.p(x + 260, 0)
        d.rectangle([a[0] - cam.s(60), a[1], a[0], b[1]], fill=(40, 38, 50, 255))
        d.rectangle([b[0], a[1], b[0] + cam.s(60), b[1]], fill=(40, 38, 50, 255))
        d.chord([a[0] - cam.s(60), a[1] - cam.s(260), b[0] + cam.s(60), a[1] + cam.s(260)], 180, 360, fill=(40, 38, 50, 255))
        d.chord([a[0], a[1] - cam.s(200), b[0], a[1] + cam.s(200)], 180, 360, fill=mix((8, 10, 26, 255), (120, 150, 210, 255), dawn))
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=(46, 42, 46, 255))
    # plinth
    d.rectangle(cam.box(-360, -120, 360, 0), fill=(80, 76, 80, 255))


def statue(d, cam, t, carve=0.0, dirt=0.0, polish=0.0):
    """carve: fraction of block cells removed. The figure inside is drawn first; remaining cells cover it."""
    x0, y0 = -BW / 2, -120 - BH
    c = mix(MARBLE, DUSTY, dirt)
    if carve > 0:
        fx, fy = cam.p(0, -120)
        h = cam.s(BH * 0.98)
        if polish > 0:
            glow(d, fx, fy - h * 0.5, h * 0.8, (255, 230, 190), 0.5 * polish)
        figure(d, fx, fy, h, mix(c, (255, 250, 240, 255), polish), mode="cheer", face=1, acc=("hair",), eyes=False)
    n = len(ORDER)
    removed = int(carve * n)
    for i, (cx, cy) in enumerate(ORDER):
        if i < removed:
            continue
        a, b = cam.p(x0 + cx * CELL, y0 + cy * CELL), cam.p(x0 + (cx + 1) * CELL, y0 + (cy + 1) * CELL)
        shade = 0.92 + 0.08 * ((cx * 7 + cy * 3) % 5) / 5
        d.rectangle([a[0], a[1], b[0] + 1, b[1] + 1], fill=col(dimc(c, shade), 1))
    if carve <= 0 and dirt > 0.4:  # moss and a cobweb
        mx, my = cam.p(x0, -120)
        d.chord([mx - cam.s(40), my - cam.s(120), mx + cam.s(140), my + cam.s(40)], 180, 360, fill=(70, 110, 60, 255))
        wx, wy = cam.p(x0 + BW, y0)
        for k in range(5):
            ang = math.radians(90 + k * 20)
            d.line([(wx, wy), (wx - math.cos(ang) * cam.s(140), wy + math.sin(ang) * cam.s(140))], fill=col(WHITE, 0.4 * dirt), width=1)


def sculptor(d, cam, x, color, mode, t, name, a=1.0, face=1, **kw):
    fx, fy = cam.p(x, 0)
    tool = lambda dd, fh, bh, h, aa: fh and mode == "hammer" and dd.line([fh, (fh[0] + face * h * 0.12, fh[1] - h * 0.04)], fill=col((180, 180, 190, 255), aa), width=max(2, int(h * 0.025)))
    figure(d, fx, fy, cam.s(260), color, mode=mode, phase=t * 7, face=face, acc=("hair",), a=a, name=name, name_a=a, prop=tool, **kw)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # moonlight on a raw block of marble; someone sitting in front of it, chin in hand, waiting
    cam = cam_lerp((0, -800, 0.95), (-250, -560, 0.68), sstep(p))
    courtyard(d, cam, t)
    statue(d, cam, t)
    sculptor(d, cam, -620, S1, "sit", t, "THE FIRST SCULPTOR", head_down=0.1, look=0.5)
    dust(d, t, 0.4, n=40, color=(220, 220, 240), rise=-10)


def s1_appear(d, t, dur):
    p = t / dur
    # seasons pass; dust and moss settle; the first sculptor gives up and walks away
    cam = Cam(-250, -560, 0.68)
    courtyard(d, cam, t)
    statue(d, cam, t, dirt=sstep(p))
    leave = sstep(ramp(p, 0.55, 0.4))
    sculptor(d, cam, lerp(-620, -1500, leave), S1, "sit" if leave <= 0 else "walk", t, "THE FIRST SCULPTOR", a=1 - leave, face=-1 if leave > 0 else 1)
    dust(d, t, 0.9, n=80, color=(220, 210, 190), rise=-15)
    if 0.25 < p < 0.5:
        snow(d, t, 0.8, n=120)
    d.text((W - 120, H - 100), f"YEAR {1 + int(p * 9)}", font=font(30), fill=col(WHITE, 0.7), anchor="rm")
    top_caption(d, ["PERFECTION", "DOESN'T APPEAR."], t, dur, accent={"PERFECTION"})


def s2_strike(d, t, dur):
    p = t / dur
    # a second sculptor walks in, climbs the plinth step and strikes. First chips fly.
    cam = cam_lerp((-250, -560, 0.68), (100, -700, 1.0), sstep(p))
    hit = pulse(p, 0.7, 0.05)
    shake(cam, t, 8 * hit)
    courtyard(d, cam, t)
    statue(d, cam, t, carve=0.03 * ramp(p, 0.7, 0.2), dirt=1.0)
    walk = sstep(ramp(p, 0.0, 0.55))
    sculptor(d, cam, lerp(1400, 420, walk), S2, "walk" if walk < 1 else "hammer", t, "THE SECOND SCULPTOR", face=-1)
    if p > 0.7:
        particles(d, *cam.p(260, -700), cam.s(300), ramp(p, 0.7, 0.3), MARBLE, n=30, seed=1, rise=0.2, size=6)


def s3_created(d, t, dur):
    p = t / dur
    # carving time-lapse: chips flying, the figure emerging, then polished and glowing in the dawn
    carve = sstep(ramp(p, 0.0, 0.75))
    dawn = sstep(ramp(p, 0.5, 0.5))
    cam = cam_lerp((100, -700, 1.0), (0, -650, 0.62), sstep(p))
    courtyard(d, cam, t, dawn=dawn)
    statue(d, cam, t, carve=carve, dirt=lerp(1.0, 0.0, carve), polish=sstep(ramp(p, 0.7, 0.3)))
    side = 1 if math.sin(t * 0.8) > 0 else -1
    sculptor(d, cam, side * 420, S2, "hammer" if carve < 1 else "stand", t, "THE SECOND SCULPTOR", face=-side)
    if carve < 1:
        particles(d, *cam.p(side * 200, -120 - BH * (1 - carve * 0.8)), cam.s(400), (t * 2) % 1, MARBLE, n=24, seed=int(t * 2), rise=0.1, size=6)
    dust(d, t, 0.5, n=50, color=(255, 230, 190))
    top_caption(d, ["IT'S CREATED."], t, dur, accent={"CREATED."})


def s4_end(d, t, dur):
    cam = Cam(0, -650, 0.62)
    courtyard(d, cam, t, dawn=1.0)
    statue(d, cam, t, carve=1.0, polish=1.0)
    sculptor(d, cam, 420, S2, "stand", t, "", face=-1, mouth=0.5)
    stage_end(d, t, dur, ["CREATE IT."], [(255, 230, 190, 255)], size=140, dim=0.35, glow_col=(255, 220, 170), y=H * 0.2)


SCENES = [s0_hook, s1_appear, s2_strike, s3_created, s4_end, s_follow]
