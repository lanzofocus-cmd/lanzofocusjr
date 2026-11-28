"""THE DOORWAY OF YEARS — on the other side of a door stands who you'll be, looking back at today.

World: a misty violet meadow at dusk with fireflies, and in the middle of nothing, a single tall door in a carved
frame, ajar, warm gold light spilling out. THE YOUNG TRAVELER (coral) approaches. Inside the light stands THE OLD
TRAVELER (silver hair, a cane), the same person decades on, mirroring every move, turning to look back. As the young
one goes, glowing MEMORY FRAMES rise from their footsteps (a climb, a hug, a finished painting, a finish line) and
drift through the doorway. At the threshold the two reach for each other; the young one steps through into light.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, dust, stars, flash)
from kit import s_follow

TITLE = ("THE DOORWAY", "OF YEARS")
OUTPUT = "149_The_Doorway_Of_Years_16x9.mp4"
LINES = [
    "",
    "One day…",
    "Your future self will look back at today.",
    "Make sure there's something worth remembering.",
    "",
    "",
]
SILENT = {0: 3.0, 4: 3.4}
GAPS = {1: 2.6, 2: 3.4, 3: 7.0}

YOUNG = (255, 130, 110, 255)
OLD = (205, 205, 220, 255)
GOLD = (255, 205, 120)
CH = 220
DW, DH = 300, 620
MEMS = [("climb", (120, 200, 255)), ("hug", (255, 150, 180)), ("paint", (150, 230, 150)), ("finish", (255, 210, 90))]


def meadow(d, cam, t, light=0.0):
    draw_sky(d, mix((30, 20, 60, 255), (90, 60, 110, 255), light), mix((150, 90, 140, 255), (255, 190, 150, 255), light))
    stars(d, 0.6 * (1 - light))
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=mix((40, 30, 60, 255), (110, 80, 90, 255), light))
    r = random.Random(3)
    for i in range(70):  # grass tufts
        x = r.uniform(-2500, 2500)
        y = r.uniform(0, 400)
        sx, sy = cam.p(x, y)
        hh = cam.s(r.uniform(20, 50))
        sw = math.sin(t * 1.5 + x * 0.01) * hh * 0.3
        d.line([(sx, sy), (sx + sw, sy - hh)], fill=(70, 60, 100, 255), width=max(1, int(cam.s(4))))
    fog(d, *cam.p(0, -60), cam.s(5000), 0.35, (200, 170, 220))
    for i in range(24):  # fireflies
        ph = r.random() * 6.28
        x = r.uniform(-1800, 1800) + math.sin(t * 0.7 + ph) * 60
        y = r.uniform(-700, -50) + math.cos(t * 0.9 + ph) * 40
        sx, sy = cam.p(x, y)
        a = 0.5 + 0.5 * math.sin(t * 3 + ph)
        glow(d, sx, sy, cam.s(30), (255, 230, 140), 0.5 * a)
        d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 240, 180, int(255 * a)))


def door(d, cam, t, open_=0.6, inner=None):
    """Door frame at x=0; open_ swings the leaf; inner(d, cam) draws the world beyond (clipped to the opening)."""
    x0, x1 = -DW / 2, DW / 2
    a, b = cam.p(x0, -DH), cam.p(x1, 0)
    glow(d, (a[0] + b[0]) / 2, (a[1] + b[1]) / 2, cam.s(700) * (0.6 + open_), GOLD, 0.25 + 0.35 * open_)
    # light inside the opening
    d.rectangle([a[0], a[1], b[0], b[1]], fill=mix((60, 40, 50, 255), (255, 235, 190, 255), open_))
    if inner:
        inner(d, cam, a, b)
    # light spilling onto the ground
    tpoly(d, [(a[0], b[1]), (b[0], b[1]), (b[0] + cam.s(600) * open_, b[1] + cam.s(260)), (a[0] - cam.s(600) * open_, b[1] + cam.s(260))],
          GOLD + (int(120 * open_),))
    # carved frame
    fw = cam.s(30)
    for box in ((a[0] - fw, a[1] - fw, a[0], b[1]), (b[0], a[1] - fw, b[0] + fw, b[1]), (a[0] - fw, a[1] - fw, b[0] + fw, a[1])):
        d.rectangle(box, fill=(80, 55, 50, 255), outline=(180, 140, 90, 255), width=max(1, int(cam.s(4))))
    # the leaf swung toward the viewer on its left hinge
    w = (b[0] - a[0]) * (1 - open_)
    lx = a[0] - (b[0] - a[0]) * open_ * 0.25
    d.polygon([(a[0], a[1]), (a[0] + w + lx - a[0], a[1] + cam.s(20) * open_), (a[0] + w + lx - a[0], b[1] - cam.s(20) * open_), (a[0], b[1])],
              fill=(100, 70, 60, 255), outline=(180, 140, 90, 255))


def young(d, cam, x, t, mode="walk", **kw):
    fx, fy = cam.p(x, 0)
    figure(d, fx, fy, cam.s(CH), YOUNG, mode=mode, phase=kw.pop("phase", t * 6), face=kw.pop("face", 1), acc=("hair", "backpack"),
           name=kw.pop("name", "THE YOUNG TRAVELER"), **kw)


def old(d, cam, a, b, t, age=1.0, mode="stand", face=-1, reach=0.0, **kw):
    """The old traveler seen inside the doorway light (a, b = the opening on screen)."""
    fx = (a[0] + b[0]) / 2 + (b[0] - a[0]) * 0.1
    fy = b[1] - (b[1] - a[1]) * 0.02
    h = (b[1] - a[1]) * 0.56
    c = mix(YOUNG, OLD, age)

    def cane(dd, fh, bh, hh, aa):
        if bh and age > 0.5:
            dd.line([bh, (bh[0] + face * hh * 0.04, fy)], fill=(120, 90, 70, int(255 * aa * age)), width=max(2, int(hh * 0.025)))
    figure(d, fx, fy, h, c, mode="reach" if reach > 0.5 else mode, phase=t * 3, face=face, acc=("hair",), tired=0.6 * age,
           lean=0.12 * age, prop=cane, name=kw.pop("name", "") and "", **kw)


def memory(d, cx, cy, s, kind, c, t, a=1.0):
    """A glowing memory frame with a little scene inside."""
    if a <= 0.02 or s < 6:
        return
    w, h = s * 1.4, s
    glow(d, cx, cy, s * 1.4, c, 0.35 * a)
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], max(2, int(s * 0.08)), fill=(30, 20, 40, int(230 * a)),
                        outline=c + (int(255 * a),), width=max(2, int(s * 0.05)))
    fy = cy + h * 0.38
    fc = c + (255,)
    if kind == "climb":
        d.polygon([(cx - w * 0.45, fy), (cx + w * 0.05, cy - h * 0.35), (cx + w * 0.45, fy)], fill=dimc(fc, 0.5))
        figure(d, cx + w * 0.02, cy - h * 0.3, h * 0.35, WHITE, mode="cheer", phase=0, face=1, a=a, eyes=False, mouth=0)
    elif kind == "hug":
        figure(d, cx - w * 0.06, fy, h * 0.6, fc, mode="stand", face=1, a=a, eyes=False, mouth=0)
        figure(d, cx + w * 0.06, fy, h * 0.55, WHITE, mode="stand", face=-1, a=a, eyes=False, mouth=0)
    elif kind == "paint":
        d.rectangle([cx + w * 0.02, cy - h * 0.3, cx + w * 0.38, cy + h * 0.15], fill=(255, 255, 255, int(255 * a)))
        d.ellipse([cx + w * 0.12, cy - h * 0.2, cx + w * 0.26, cy - h * 0.06], fill=(255, 200, 60, int(255 * a)))
        d.polygon([(cx + w * 0.02, cy + h * 0.15), (cx + w * 0.2, cy - h * 0.02), (cx + w * 0.38, cy + h * 0.15)], fill=fc)
        figure(d, cx - w * 0.2, fy, h * 0.6, WHITE, mode="reach", face=1, a=a, eyes=False, mouth=0)
    else:
        d.line([(cx + w * 0.25, cy - h * 0.4), (cx + w * 0.25, fy)], fill=fc, width=max(2, int(s * 0.04)))
        d.rectangle([cx + w * 0.25, cy - h * 0.4, cx + w * 0.42, cy - h * 0.25], fill=fc)
        figure(d, cx - w * 0.05, fy, h * 0.6, WHITE, mode="cheer", face=1, a=a, eyes=False, mouth=0)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # total dark; a hairline of gold light opens vertically, widening; dust drifts in it
    d.rectangle([0, 0, W, H], fill=(6, 4, 12, 255))
    k = sstep(ramp(p, 0.15, 0.85))
    w = 3 + 160 * k
    glow(d, W / 2, H / 2, 200 + 700 * k, GOLD, 0.4 + 0.3 * k)
    d.rectangle([W / 2 - w / 2, H * 0.1, W / 2 + w / 2, H * 0.9], fill=(255, 235, 190, 255))
    tpoly(d, [(W / 2 - w / 2, H * 0.9), (W / 2 + w / 2, H * 0.9), (W / 2 + w * 3, H), (W / 2 - w * 3, H)], GOLD + (120,))
    dust(d, t, 0.6 * k, n=40, color=(255, 230, 170))


def s1_oneday(d, t, dur):
    p = t / dur
    # wide: a lone door ajar in a misty dusk meadow; the young traveler stops at a distance
    cam = cam_lerp((0, -380, 0.9), (-350, -350, 0.55), sstep(p))
    meadow(d, cam, t)
    door(d, cam, t, open_=0.35)
    young(d, cam, lerp(-1400, -1000, sstep(p)), t, mode="walk" if p < 0.8 else "stand", phase=p * 30, look=0.2)
    top_caption(d, ["ONE DAY…"], t, dur, accent={"ONE", "DAY…"})


def s2_lookback(d, t, dur):
    p = t / dur
    # the door swings wider; inside the light stands the same traveler, decades older, who turns and looks back
    op = lerp(0.35, 0.8, sstep(ramp(p, 0.0, 0.4)))
    age = sstep(ramp(p, 0.1, 0.6))
    cam = cam_lerp((-350, -350, 0.55), (-250, -330, 0.9), sstep(p))
    meadow(d, cam, t, light=0.2 * p)
    x = lerp(-1000, -620, sstep(p))
    face_old = 1 if p < 0.35 else -1
    door(d, cam, t, open_=op, inner=lambda dd, cc, a, b: old(dd, cc, a, b, t, age=age, face=face_old, mouth=0.4 * age,
                                                              name="THE OLD TRAVELER" if p > 0.4 else ""))
    young(d, cam, x, t, mode="walk" if p < 0.9 else "stand", phase=x / 40, name="")
    top_caption(d, ["YOUR FUTURE SELF WILL", "LOOK BACK AT TODAY."], t, dur, accent={"FUTURE", "TODAY."})


def s3_memories(d, t, dur):
    p = t / dur
    # the young one walks on; with each stride a memory frame rises and drifts through the door;
    # at the threshold the two reach for each other, and the young one steps into the light
    walk = sstep(ramp(p, 0.0, 0.65))
    x = lerp(-620, -40, walk)
    reach = sstep(ramp(p, 0.62, 0.12))
    enter = sstep(ramp(p, 0.78, 0.14))
    cam = cam_lerp((-250, -330, 0.9), (-60, -330, 1.15), sstep(ramp(p, 0.3, 0.6)))
    meadow(d, cam, t, light=0.2 + 0.5 * enter)
    door(d, cam, t, open_=lerp(0.8, 1.0, enter),
         inner=lambda dd, cc, a, b: old(dd, cc, a, b, t, age=1.0, face=-1, reach=reach, mouth=0.7, name=""))
    for i, (kind, c) in enumerate(MEMS):
        t0 = 0.04 + i * 0.12
        k = ramp(p, t0, 0.42)
        if 0 < k < 1:
            sx0, sy0 = cam.p(lerp(-620, -40, clamp((t0 - 0.0) / 0.65)), -100)
            dx, dy = cam.p(0, -300)
            cx = lerp(sx0, dx, sstep(k))
            cy = lerp(sy0, dy, sstep(k)) - math.sin(math.pi * k) * cam.s(150)
            memory(d, cx, cy, cam.s(lerp(80, 260, math.sin(math.pi * min(1, k * 1.3)))), kind, c, t, a=1 - ramp(k, 0.85, 0.15))
    if enter < 0.95:
        young(d, cam, x + enter * 120, t, mode="walk" if walk < 0.98 and reach < 0.5 else ("reach" if enter < 0.2 else "walk"),
              phase=x / 40, a=1 - enter, mouth=0.5, name="")
    if enter > 0.6:
        flash(d, (enter - 0.6) * 1.5, (255, 240, 210))
    top_caption(d, ["MAKE SURE THERE'S SOMETHING", "WORTH REMEMBERING."], t, dur, accent={"WORTH", "REMEMBERING."})


def s4_end(d, t, dur):
    cam = Cam(-60, -330, 1.15)
    meadow(d, cam, t, light=0.7)
    door(d, cam, t, open_=1.0)
    overlay(d, (255, 240, 210), 0.35)
    for i, (kind, c) in enumerate(MEMS):
        ang = math.pi * (0.15 + 0.7 * i / 3)
        cx, cy = cam.p(-math.cos(ang) * 620, -200 - math.sin(ang) * 120 + math.sin(t * 1.5 + i) * 15)
        memory(d, cx, cy, cam.s(150), kind, c, t, a=ramp(t, 0.2 + i * 0.15, 0.4))
    stage_end(d, t, dur, ["MAKE TODAY", "WORTH REMEMBERING."], [WHITE, GOLD + (255,)], size=100, dim=0.5, glow_col=GOLD, y=H * 0.16)


SCENES = [s0_hook, s1_oneday, s2_lookback, s3_memories, s4_end, s_follow]
