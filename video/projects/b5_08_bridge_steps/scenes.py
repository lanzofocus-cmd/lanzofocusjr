"""THE BRIDGE OF SMALL STEPS — a canyon with no giant leap, only stones that appear under each step.

World: a red-rock canyon at dusk, violet sky, a drop into blue haze. THE TRAVELER (white, red scarf) dreams of
THE GIANT STEP: a huge ghostly leaping figure that never lands. Instead THE SMALL STEP: a glowing gold stone
rises out of the abyss each time a foot reaches forward, until a whole bridge spans the gap.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, stars, dust)
from render import dashed
from kit import s_follow

TITLE = ("THE BRIDGE OF", "SMALL STEPS")
OUTPUT = "108_The_Bridge_Of_Small_Steps_16x9.mp4"
LINES = [
    "",
    "You keep searching for one giant leap.",
    "But sometimes…",
    "The entire bridge is made of small steps.",
    "",
    "",
]
SILENT = {0: 3.2, 4: 3.6}
GAPS = {1: 3.0, 2: 2.0, 3: 5.0}

ROCK = (150, 70, 50, 255)
ROCK_D = (90, 40, 34, 255)
GOLD = (255, 205, 110, 255)
YOU = (236, 232, 226, 255)
GAP0, GAP1 = 0, 2400       # canyon edges (x)
STEP = 160
NSTONES = int((GAP1 - GAP0) / STEP)
CH = 170


def canyon(d, cam, t, light=1.0):
    draw_sky(d, (40, 26, 70, 255), (255, 150, 110, 255))
    stars(d, 0.4, seed=8, n=40, ymax=0.3)
    # far mesas (parallax)
    for f, c, base in ((0.3, (120, 70, 90), -300), (0.55, (100, 50, 60), -120)):
        pts = []
        r = random.Random(int(f * 10))
        for i in range(30):
            x = -6000 + i * 500
            hgt = base - r.choice([0, 0, 300, 420])
            pts.append(((x - cam.cx * f) * cam.z * (0.5 + 0.5 * f) + W / 2, (hgt - cam.cy * f) * cam.z * (0.5 + 0.5 * f) + H / 2))
            pts.append(((x + 480 - cam.cx * f) * cam.z * (0.5 + 0.5 * f) + W / 2, (hgt - cam.cy * f) * cam.z * (0.5 + 0.5 * f) + H / 2))
        pts += [(W + 10, H + 10), (-10, H + 10)]
        d.polygon(pts, fill=c + (255,))
    # the abyss haze
    gy = cam.p(0, 0)[1]
    xa, xb = cam.p(GAP0, 0)[0], cam.p(GAP1, 0)[0]
    for k in range(40):
        y0 = gy + (H - gy) * k / 40 if gy < H else H
        y1 = gy + (H - gy) * (k + 1) / 40 if gy < H else H
        d.rectangle([xa, max(0, y0), xb, max(0, y1) + 1], fill=mix((150, 120, 170, 255), (20, 20, 50, 255), k / 40))
    fog(d, *cam.p((GAP0 + GAP1) / 2, 900), cam.s(5000), 0.5, (160, 150, 220))
    # cliffs left and right
    for sgn, x in ((-1, GAP0), (1, GAP1)):
        pts = [cam.p(x, 0)]
        r = random.Random(x)
        for k in range(1, 12):
            pts.append(cam.p(x + sgn * r.uniform(-40, 120) * (k / 6), k * 300))
        pts += [cam.p(x + sgn * 4000, 3600), cam.p(x + sgn * 4000, 0)]
        d.polygon(pts, fill=col(ROCK, light))
        for k in range(1, 8):  # strata lines
            y = k * 220
            a, b = cam.p(x + sgn * 30 * k, y), cam.p(x + sgn * 3000, y + 40)
            d.line([a, b], fill=col(ROCK_D, 0.6 * light), width=max(1, int(cam.s(8))))
        d.line([cam.p(x, 0), cam.p(x + sgn * 4000, 0)], fill=col((220, 140, 100, 255), light), width=max(2, int(cam.s(6))))


def stones(d, cam, t, n, rising=0.0):
    """n stones already in place; the next one rising with `rising`."""
    for i in range(int(n) + (1 if rising > 0 else 0)):
        x = GAP0 + STEP * (i + 0.5)
        if x > GAP1:
            break
        k = 1.0 if i < int(n) else sstep(rising)
        y = lerp(900, 0, k) + 4 * math.sin(t * 2 + i)
        sx, sy = cam.p(x, y)
        w, h = cam.s(70), cam.s(30)
        glow(d, sx, sy, cam.s(130), GOLD, 0.55)
        d.polygon([(sx - w, sy), (sx + w, sy), (sx + w * 0.7, sy + h), (sx - w * 0.6, sy + h * 1.2)], fill=col((220, 170, 90, 255), 1))
        d.ellipse([sx - w, sy - h * 0.4, sx + w, sy + h * 0.4], fill=col(GOLD, 1))


def traveler(d, cam, x, y, t, mode="stand", **kw):
    fx, fy = cam.p(x, y)
    kw.setdefault("acc", ("hair", "scarf"))
    figure(d, fx, fy, cam.s(CH), YOU, mode=mode, face=kw.pop("face", 1), **kw)
    return fx, fy


def giant_leap(d, cam, k, t):
    """A huge ghost of the traveler leaping across in one arc — and fading before it lands."""
    if k <= 0 or k >= 1:
        return
    x = lerp(GAP0 - 100, GAP1 + 100, k)
    y = -math.sin(math.pi * k) * 900
    pts = [cam.p(lerp(GAP0 - 100, GAP1 + 100, u / 30), -math.sin(math.pi * u / 30) * 900) for u in range(31)]
    dashed(d, pts, col(WHITE, 0.9 * (1 - k * 0.5)), max(3, int(cam.s(10))), cam.s(30), cam.s(20))
    fx, fy = cam.p(x, y)
    figure(d, fx, fy, cam.s(CH * 3), (200, 210, 255, 255), mode="run", phase=1.2, lean=0.5, a=0.75 * (1 - k ** 3), acc=("hair",), eyes=False,
           name="THE GIANT LEAP" if k < 0.5 else None, name_a=0.8)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # crane up out of the abyss, past the cliff face, to the small figure standing at the edge
    cam = cam_lerp((300, 1500, 0.55), (-100, -150, 0.85), sstep(p))
    canyon(d, cam, t)
    traveler(d, cam, -90, 0, t, look=-0.3)
    for j in range(4):  # pebbles falling past the camera
        u = ((t * 0.6 + j * 0.27) % 1)
        sx, sy = cam.p(-30 + j * 20, u * 1500)
        d.ellipse([sx - 5, sy - 5, sx + 5, sy + 5], fill=col((200, 140, 110, 255), 1 - u))


def s1_leap(d, t, dur):
    p = t / dur
    # backs up, takes a run-up... the dream of a giant leap flies across and fades. They skid to a halt.
    cam = cam_lerp((100, -260, 0.75), (700, -400, 0.48), sstep(p))
    canyon(d, cam, t)
    if p < 0.25:
        x, mode, kw = lerp(-90, -500, sstep(p / 0.25)), "walk", dict(face=-1, phase=t * 4)
    elif p < 0.55:
        u = (p - 0.25) / 0.3
        x, mode, kw = lerp(-500, -60, u ** 1.5), "run", dict(phase=t * 9, lean=0.4)
    else:
        x, mode, kw = -60, "flail" if p < 0.65 else "stand", dict(phase=t * 3, lean=-0.3 if p < 0.65 else 0.0, look=-0.5)
    giant_leap(d, cam, ramp(p, 0.45, 0.45), t)
    traveler(d, cam, x, 0, t, mode=mode, **kw)
    if 0.55 < p < 0.75:
        particles(d, *cam.p(-20, 0), cam.s(120), (p - 0.55) / 0.2, (200, 140, 110), n=16, seed=3, rise=-0.6)
    top_caption(d, ["YOU KEEP SEARCHING FOR", "ONE GIANT LEAP."], t, dur, accent={"GIANT", "LEAP."})


def s2_sometimes(d, t, dur):
    p = t / dur
    # close at the edge: a foot reaches out over nothing... and a small stone rises to meet it
    cam = cam_lerp((40, -100, 1.6), (80, -60, 1.9), sstep(p))
    canyon(d, cam, t)
    stones(d, cam, t, 0, rising=ramp(t, dur * 0.35, dur * 0.5))
    fx, fy = cam.p(-60, 0)
    figure(d, fx, fy, cam.s(CH), YOU, mode="stand", face=1, acc=("hair", "scarf"), look=-0.7, head_down=0.4)
    top_caption(d, ["BUT SOMETIMES…"], t, dur, accent={"SOMETIMES…"})


def s3_bridge(d, t, dur):
    p = t / dur
    # step, stone, step, stone: tracking alongside, then pulling back to see the whole bridge appear
    n = NSTONES * sstep(ramp(p, 0.0, 0.85))
    pos = GAP0 + STEP * (n - 0.5)
    cam = cam_lerp((pos + 150, -150, 1.1), ((GAP0 + GAP1) / 2, -300, 0.36), sstep(ramp(p, 0.3, 0.7)))
    cam.cx = lerp(pos + 150, (GAP0 + GAP1) / 2, sstep(ramp(p, 0.3, 0.7)))
    canyon(d, cam, t)
    stones(d, cam, t, n, rising=n % 1)
    if n < NSTONES:
        traveler(d, cam, max(-60, pos), 0, t, mode="walk", phase=n * math.pi, swing=0.4, stride=0.7, look=-0.2)
    else:
        traveler(d, cam, GAP1 + 120, 0, t, mode="cheer", mouth=0.8)
    top_caption(d, ["THE ENTIRE BRIDGE IS MADE", "OF SMALL STEPS."], t, dur, accent={"SMALL", "STEPS."})


def s4_end(d, t, dur):
    cam = Cam((GAP0 + GAP1) / 2, -300, 0.36)
    canyon(d, cam, t)
    stones(d, cam, t, NSTONES)
    traveler(d, cam, GAP1 + 120, 0, t, mode="stand", face=-1, look=-0.2)
    stage_end(d, t, dur, ["ONE SMALL STEP", "AT A TIME."], [WHITE, GOLD], size=110, dim=0.45, glow_col=GOLD, y=H * 0.4)


SCENES = [s0_hook, s1_leap, s2_sometimes, s3_bridge, s4_end, s_follow]
