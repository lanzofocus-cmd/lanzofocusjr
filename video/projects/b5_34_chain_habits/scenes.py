"""THE CHAIN OF HABITS — a chain of glowing links that either drags you back or carries you across.

World: a dark slate cliff-top at dusk at the edge of a chasm. THE PERSON is tethered to a long chain; each LINK
glows and is named for a habit. Red links (SNOOZE, SCROLLING, LATER, JUNK FOOD) drag back toward a heavy anchor.
One by one the person swaps them for green links (READING, TRAINING, SLEEP EARLY, PRACTICE); the chain lifts, swings
out over the chasm and straightens into a bridge they walk across into the sunrise.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, sun, dust)
from kit import s_follow

TITLE = ("THE CHAIN", "OF HABITS")
OUTPUT = "134_The_Chain_Of_Habits_16x9.mp4"
LINES = [
    "",
    "Your habits are either holding you…",
    "Or carrying you.",
    "",
    "",
    "",
]
SILENT = {0: 3.0, 3: 4.8, 4: 3.4}
GAPS = {1: 1.4, 2: 4.2}

RED = (255, 70, 70, 255)
GREEN = (110, 255, 150, 255)
YOU = (236, 228, 214, 255)
BAD = ["SNOOZE", "SCROLLING", "LATER", "JUNK FOOD", "EXCUSES", "SKIPPING"]
GOOD = ["READING", "TRAINING", "SLEEP EARLY", "PRACTICE", "SHOWING UP", "FOCUS"]
EDGE = 600       # cliff edge x
FAR = 2600       # far side x
CH = 220


def cliffs(d, cam, t, dawn=0.0):
    draw_sky(d, mix((30, 32, 50, 255), (120, 150, 210, 255), dawn), mix((90, 70, 90, 255), (255, 190, 140, 255), dawn))
    if dawn > 0.05:
        sun(d, cam.p(FAR + 800, -300)[0], cam.p(0, -260)[1], 80, dawn, (255, 220, 160, 255))
    for (x0, x1) in ((-3000, EDGE), (FAR, FAR + 3000)):
        pts = [cam.p(x0, 0), cam.p(x1, 0), cam.p(x1 + (-120 if x1 == EDGE else 0), 2000), cam.p(x0, 2000)]
        d.polygon(pts, fill=mix((40, 40, 52, 255), (90, 80, 90, 255), dawn * 0.5))
        d.line([cam.p(x0, 0), cam.p(x1, 0)], fill=col((120, 120, 140, 255), 0.6), width=max(1, int(cam.s(5))))
    fog(d, *cam.p((EDGE + FAR) / 2, 600), cam.s(3000), 0.4, (150, 150, 200))


def link(d, cam, x, y, ang, label, c, a=1.0, s=1.0):
    sx, sy = cam.p(x, y)
    w, h = cam.s(90 * s), cam.s(46 * s)
    ca, sa = math.cos(ang), math.sin(ang)
    pts = []
    for k in range(24):
        q = k * math.tau / 24
        px, py = math.cos(q) * w, math.sin(q) * h
        pts.append((sx + px * ca - py * sa, sy + px * sa + py * ca))
    glow(d, sx, sy, w * 1.6, c, 0.35 * a)
    polyline(d, pts + [pts[0]], 1, col(c, a), max(2, int(cam.s(14 * s))))
    if label and abs(ang) < 0.6:
        d.text((sx, sy - h - cam.s(26)), label, font=font(max(10, int(cam.s(24)))), fill=col(c, a), anchor="mm")


def chain(d, cam, t, px, swapped=0.0, bridge=0.0, n=14):
    """Links from the person's waist back to an anchor; swapped = fraction turned green; bridge = 0..1 straightening
    into a span from EDGE to FAR."""
    anchor = (-1500, -10)
    out = []
    for i in range(n):
        u = (i + 0.5) / n
        # slack chain dragging back on the ground
        x0 = lerp(px - 60, anchor[0], u)
        y0 = -10 - math.sin(math.pi * u) * 20
        # bridge span
        x1 = lerp(EDGE - 40, FAR + 40, u)
        y1 = -10 + math.sin(math.pi * u) * 60
        x, y = lerp(x0, x1, sstep(bridge)), lerp(y0, y1, sstep(bridge))
        ang = 0.0 if bridge > 0.5 else (0.2 * math.sin(t * 2 + i) if i % 2 else 1.4)
        green = swapped * n > (n - 1 - i) if False else swapped * n > i
        c = GREEN if green else RED
        lbl = (GOOD if green else BAD)[(i // 2) % 6] if i % 2 == 0 else None
        out.append((x, y, ang, lbl, c))
    if bridge < 0.5:  # the anchor block
        ax, ay = cam.p(*anchor)
        d.rounded_rectangle([ax - cam.s(120), ay - cam.s(140), ax + cam.s(120), ay], int(cam.s(16)), fill=col((70, 30, 34, 255), 1 - bridge * 2), outline=col(RED, 1 - bridge * 2), width=3)
    for (x, y, ang, lbl, c) in out:
        link(d, cam, x, y, ang, lbl, c)


def person(d, cam, x, t, mode="walk", **kw):
    fx, fy = cam.p(x, 0)
    figure(d, fx, fy, cam.s(CH), YOU, mode=mode, phase=kw.pop("phase", t * 3), face=kw.pop("face", 1), acc=("hair",), **kw)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # macro: a red link snaps taut and glows; pull back to the tether at someone's waist
    cam = cam_lerp((-300, -60, 3.0), (-200, -200, 0.8), sstep(p))
    jolt = pulse(t, 0.6, 0.1)
    shake(cam, t, 14 * jolt)
    cliffs(d, cam, t)
    chain(d, cam, t, 200)
    person(d, cam, 200, t, mode="walk", lean=0.4, swing=0.5, stride=0.4, tired=0.6)


def s1_holding(d, t, dur):
    p = t / dur
    # straining forward toward the edge while the red chain drags back
    x = 200 + 120 * math.sin(p * 2) * 0.5
    cam = cam_lerp((-200, -200, 0.8), (-300, -250, 0.7), p)
    cliffs(d, cam, t)
    chain(d, cam, t, x)
    person(d, cam, x, t, mode="walk", lean=0.45, swing=0.5, stride=0.4, tired=0.8)
    top_caption(d, ["YOUR HABITS ARE EITHER", "HOLDING YOU…"], t, dur, accent={"HOLDING"})


def s2_carrying(d, t, dur):
    p = t / dur
    # one by one, red links are lifted out and green ones locked in
    sw = sstep(ramp(p, 0.1, 0.8))
    cam = cam_lerp((-300, -250, 0.7), (100, -300, 0.62), sstep(p))
    cliffs(d, cam, t)
    chain(d, cam, t, 300, swapped=sw)
    person(d, cam, 300 + 200 * sw, t, mode="carry" if p < 0.85 else "stand", face=-1, lean=0.0, mouth=0.5 * sw)
    i = int(sw * 14)
    if 0 < sw < 1:
        x = lerp(240, -1500, (i + 0.5) / 14)
        particles(d, *cam.p(x, -10), cam.s(160), (sw * 14) % 1, GREEN, n=14, seed=i, rise=0.4)
    top_caption(d, ["OR CARRYING YOU."], t, dur, accent={"CARRYING"})


def s3_bridge(d, t, dur):
    p = t / dur
    # the green chain rises, swings out over the chasm and locks into a bridge; the person crosses into sunrise
    b = sstep(ramp(p, 0.0, 0.4))
    walk = sstep(ramp(p, 0.45, 0.55))
    dawn = sstep(ramp(p, 0.3, 0.6))
    x = lerp(500, FAR + 200, walk)
    cam = cam_lerp((100, -300, 0.62), (1600, -400, 0.42), sstep(ramp(p, 0.0, 0.6)))
    cliffs(d, cam, t, dawn=dawn)
    chain(d, cam, t, 500, swapped=1.0, bridge=b)
    yb = -10 + math.sin(math.pi * clamp((x - EDGE) / (FAR - EDGE))) * 60 - 30 if EDGE < x < FAR else 0
    fx, fy = cam.p(x, yb)
    figure(d, fx, fy, cam.s(CH), YOU, mode="walk" if 0 < walk < 1 else "stand", phase=x / 55, face=1, acc=("hair",), mouth=0.6)
    dust(d, t, 0.5 * dawn, n=40, color=(255, 230, 170))


def s4_end(d, t, dur):
    cam = Cam(1600, -400, 0.42)
    cliffs(d, cam, t, dawn=1.0)
    chain(d, cam, t, 500, swapped=1.0, bridge=1.0)
    person(d, cam, FAR + 200, t, mode="stand", mouth=0.6)
    stage_end(d, t, dur, ["CHOOSE YOUR LINKS."], [GREEN], size=120, dim=0.4, glow_col=GREEN, y=H * 0.28)


SCENES = [s0_hook, s1_holding, s2_carrying, s3_bridge, s4_end, s_follow]
