"""THE WEIGHTLESS GOAL — the dream was never the heavy part.

World: a surreal pastel desert, peach sand and a mint sky, enormous half-buried objects (a clock, a chair, a door)
casting long violet shadows. THE WORKER (teal) trudges, sinking ankle-deep, under an absurd tower of baggage strapped
to their back: labelled crates and junk (SCROLLING, DRAMA, WHAT IFS, OLD GRUDGES, OTHERS' OPINIONS, PERFECTION...).
On a pedestal floats THE DREAM, a small glowing orb. They can't lift it. They look back at what they carry, and
let the straps go: crate after crate thuds into the sand. The orb lifts easily, and lifts them, floating, into the sky.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, dust, sun)
from kit import s_follow

TITLE = ("THE WEIGHTLESS", "GOAL")
OUTPUT = "147_The_Weightless_Goal_16x9.mp4"
LINES = [
    "",
    "",
    "Your goal isn't always too heavy.",
    "Sometimes…",
    "You're carrying too much else.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.4, 5: 3.4}
GAPS = {2: 2.4, 3: 2.2, 4: 6.4}

WORKER = (70, 210, 200, 255)
DREAM = (255, 230, 140)
SAND = (245, 200, 170, 255)
CH = 210
PACK = [  # label, width, height, colour (bottom to top)
    ("OLD GRUDGES", 230, 110, (150, 90, 110)),
    ("WHAT IFS", 190, 100, (110, 110, 170)),
    ("SCROLLING", 210, 120, (90, 140, 200)),
    ("DRAMA", 170, 90, (210, 90, 110)),
    ("OTHERS' OPINIONS", 260, 110, (160, 120, 90)),
    ("PERFECTION", 200, 100, (180, 180, 190)),
    ("REGRETS", 160, 90, (120, 100, 140)),
    ("NOISE", 150, 80, (200, 140, 80)),
]
PED = 1500


def desert(d, cam, t, dusk=0.0):
    draw_sky(d, mix((150, 225, 210, 255), (120, 110, 180, 255), dusk), mix((255, 225, 200, 255), (255, 170, 150, 255), dusk))
    sun(d, cam.p(cam.cx * 0.6 + 900, 0)[0], cam.p(0, -900)[1], cam.s(110) + 40, 1.0, (255, 240, 210, 255))
    gy = cam.p(0, 0)[1]
    # far dunes
    for k, (yy, c) in enumerate(((-30, (240, 190, 165)), (0, SAND[:3]))):
        pts = [(x, cam.p(0, yy)[1] - math.sin(x * 0.004 + k * 2 + cam.cx * 0.0004 * (k + 1)) * 30 * (2 - k)) for x in range(0, W + 41, 40)]
        d.polygon(pts + [(W, H), (0, H)], fill=c + (255,))
    # giant half-buried objects with long shadows
    for (ox, kind) in ((-1400, "clock"), (700, "chair"), (2600, "door"), (-3200, "chair"), (4200, "clock")):
        sx, sy = cam.p(ox, 0)
        s = cam.s(1)
        if not (-900 < sx < W + 900):
            continue
        tpoly(d, [(sx - 50 * s, sy), (sx + 50 * s, sy), (sx + 700 * s, sy + 90 * s), (sx + 500 * s, sy + 110 * s)], (150, 110, 170, 90))
        if kind == "clock":
            d.ellipse([sx - 220 * s, sy - 380 * s, sx + 220 * s, sy + 60 * s], fill=(240, 230, 210, 255), outline=(120, 100, 120, 255), width=max(2, int(10 * s)))
            d.line([(sx, sy - 160 * s), (sx + 30 * s, sy - 300 * s)], fill=(80, 70, 90, 255), width=max(2, int(10 * s)))
            d.line([(sx, sy - 160 * s), (sx + 140 * s, sy - 130 * s)], fill=(80, 70, 90, 255), width=max(2, int(8 * s)))
        elif kind == "chair":
            c = (190, 120, 150, 255)
            d.rectangle([sx - 160 * s, sy - 260 * s, sx + 160 * s, sy - 220 * s], fill=c)
            d.rectangle([sx + 120 * s, sy - 620 * s, sx + 160 * s, sy - 220 * s], fill=c)
            for lx in (-150, 110):
                d.rectangle([sx + lx * s, sy - 220 * s, sx + (lx + 40) * s, sy + 20 * s], fill=c)
        else:
            d.rectangle([sx - 140 * s, sy - 560 * s, sx + 140 * s, sy + 20 * s], fill=(110, 150, 190, 255), outline=(70, 90, 120, 255), width=max(2, int(10 * s)))
            d.ellipse([sx + 80 * s, sy - 280 * s, sx + 110 * s, sy - 250 * s], fill=(255, 220, 120, 255))


def pedestal(d, cam, t, lift=0.0, held=None):
    a, b = cam.p(PED - 90, -260), cam.p(PED + 90, 0)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(250, 245, 240, 255), outline=(200, 190, 200, 255), width=3)
    if held is None:
        ox, oy = cam.p(PED, -340 - math.sin(t * 2) * 12 - lift)
    else:
        ox, oy = held
    r = cam.s(46)
    glow(d, ox, oy, r * 5, DREAM, 0.6)
    d.ellipse([ox - r, oy - r, ox + r, oy + r], fill=DREAM + (255,))
    d.ellipse([ox - r * 0.4, oy - r * 0.55, ox - r * 0.05, oy - r * 0.2], fill=(255, 255, 240, 255))
    return ox, oy


LAND_X = PED - 220


def land(i):
    """World landing spot of crate i once dropped (a scattered pile behind the worker)."""
    r = random.Random(i)
    return LAND_X - 260 - (i % 4) * 190 + r.uniform(-40, 40), -(i // 4) * 105 * 0.75


def crate(d, cam, x0, y0, w, hh, lbl, c, s):
    d.rounded_rectangle([x0, y0, x0 + w, y0 + hh], max(2, int(8 * s)), fill=c + (255,), outline=dimc(c + (255,), 0.6), width=max(1, int(4 * s)))
    if s * 22 > 6:
        fz = max(8, int(min(26 * s, w / max(1, len(lbl)) * 1.6)))
        d.text((x0 + w / 2, y0 + hh / 2), lbl, font=font(fz), fill=(255, 255, 255, 255), anchor="mm")


def pack(d, cam, fx, fy, h, face, t, dropped=0.0, sway=0.0):
    """The baggage tower on the worker's back. Items from the top fall away (to world landing spots) as dropped
    goes 0..len(PACK); fully dropped items are drawn by pile()."""
    s = h / CH * 0.8
    y = fy - h * 0.5
    for i, (lbl, w, hh, c) in enumerate(PACK):
        w, hh = w * s, hh * s
        k = clamp(dropped - (len(PACK) - 1 - i))
        lean = math.sin(t * 2.2 + i * 0.5) * sway * (i + 1) * 3 * s
        x0 = fx - face * (w / 2 + h * 0.1) - w / 2 + lean
        y0 = y - hh
        if k <= 0:
            crate(d, cam, x0, y0, w, hh, lbl, c, s)
            y = y0
        elif k < 1:
            lx, ly = land(i)
            tx, ty = cam.p(lx, ly)
            crate(d, cam, lerp(x0, tx - w / 2, k), lerp(y0, ty - hh, k * k), w, hh, lbl, c, s)
    if dropped < len(PACK) - 0.5:
        d.line([(fx, fy - h * 0.78), (fx - face * h * 0.12, fy - h * 0.5)], fill=(80, 60, 50, 255), width=max(2, int(h * 0.03)))


def pile(d, cam, t, dropped):
    s = cam.s(1) * 0.8
    for i, (lbl, w, hh, c) in enumerate(PACK):
        k = clamp(dropped - (len(PACK) - 1 - i))
        if k >= 1:
            lx, ly = land(i)
            tx, ty = cam.p(lx, ly)
            crate(d, cam, tx - w * s / 2, ty - hh * s, w * s, hh * s, lbl, c, s)


def worker(d, cam, x, t, mode="walk", dropped=0.0, sink=1.0, sway=0.6, y=0.0, **kw):
    fx, fy = cam.p(x, y + 30 * sink)
    h = cam.s(CH)
    face = kw.pop("face", 1)
    pile(d, cam, t, dropped)
    pack(d, cam, fx, fy, h, face, t, dropped=dropped, sway=sway)
    figure(d, fx, fy, h, WORKER, mode=mode, phase=kw.pop("phase", t * 3), face=face, acc=("cap",), name=kw.pop("name", "THE WORKER"),
           eye_col=(10, 50, 50, 255), **kw)
    if sink > 0.05:  # feet sunk in sand
        d.ellipse([fx - h * 0.18, fy - h * 0.04, fx + h * 0.18, fy + h * 0.05], fill=SAND)
    return fx, fy, h


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # tight on feet sinking with each step into the sand; tilt up the impossible tower of baggage
    cam = cam_lerp((-200, -40, 2.6), (-200, -700, 0.95), sstep(ramp(p, 0.3, 0.7)))
    desert(d, cam, t)
    worker(d, cam, -300 + t * 30, t, mode="walk", phase=t * 2.4, tired=1.0, lean=0.25, name="", head_down=True)


def s1_trudge(d, t, dur):
    p = t / dur
    # wide: the tiny worker under a towering pack trudges toward a pedestal where the small dream glows
    x = lerp(-200, 900, p)
    cam = cam_lerp((300, -600, 0.45), (900, -500, 0.5), sstep(p))
    desert(d, cam, t)
    pedestal(d, cam, t)
    worker(d, cam, x, t, mode="walk", phase=t * 2.4, tired=1.0, lean=0.25)
    ox, oy = cam.p(PED, -340)
    d.text((ox, oy - cam.s(110)), "THE DREAM", font=font(26), fill=(255, 245, 210, 255), anchor="mm")


def s2_heavy(d, t, dur):
    p = t / dur
    # they reach for the orb, strain; it won't rise; their knees buckle under the tower
    cam = cam_lerp((1100, -560, 0.6), (1300, -500, 0.75), sstep(p))
    shake(cam, t, 3 * ramp(p, 0.3, 0.3))
    desert(d, cam, t)
    pedestal(d, cam, t, lift=8 * math.sin(t * 20) * ramp(p, 0.2, 0.3))
    mode = "reach" if p < 0.6 else "kneel"
    worker(d, cam, PED - 220, t, mode=mode, tired=1.0, sway=1.2, look=-0.3, name="")
    top_caption(d, ["YOUR GOAL ISN'T ALWAYS", "TOO HEAVY."], t, dur, accent={"HEAVY."})


def s3_sometimes(d, t, dur):
    p = t / dur
    # they look back over their shoulder; the camera climbs the tower, reading the labels
    cam = cam_lerp((1250, -300, 1.1), (1150, -900, 1.1), sstep(p))
    desert(d, cam, t)
    pedestal(d, cam, t)
    worker(d, cam, PED - 220, t, mode="kneel", tired=1.0, sway=0.5, face=1, look=-1.0, name="")
    top_caption(d, ["SOMETIMES…"], t, dur, accent={"SOMETIMES…"})


def s4_else(d, t, dur):
    p = t / dur
    # straps loosen: crate after crate thuds into the sand; they stand tall, lift the orb, and it lifts them
    dropped = len(PACK) * sstep(ramp(p, 0.05, 0.45))
    up = sstep(ramp(p, 0.55, 0.45))
    cam = cam_lerp((1250, -500, 0.7), (1350, -800, 0.55), sstep(ramp(p, 0.4, 0.6)))
    desert(d, cam, t, dusk=0.4 * up)
    x = PED - 220 + 130 * sstep(ramp(p, 0.45, 0.1))
    fy_world = -up * 700
    mode = "kneel" if dropped < 5 else ("reach" if up < 0.05 else "cheer")
    fx, fy, h = worker(d, cam, x, t, mode=mode, dropped=dropped, sink=1 - sstep(ramp(p, 0.4, 0.15)), sway=0.3, y=fy_world, face=1,
                       mouth=0.6 * up, name="", lean=0.0)
    held = (fx + h * 0.05, fy - h * 1.15) if up > 0 else None
    pedestal(d, cam, t, held=held, lift=0)
    dust(d, t, 0.4 * up, n=40, color=(255, 240, 200))
    top_caption(d, ["YOU'RE CARRYING", "TOO MUCH ELSE."], t, dur, accent={"TOO", "MUCH", "ELSE."})


def s5_end(d, t, dur):
    cam = Cam(1350, -800, 0.55)
    desert(d, cam, t, dusk=0.4)
    fx, fy, h = worker(d, cam, 1410, t, mode="cheer", dropped=len(PACK), sink=0, y=-700 - t * 30, face=1, mouth=0.7, name="")
    pedestal(d, cam, t, held=(fx + h * 0.05, fy - h * 1.15))
    stage_end(d, t, dur, ["DROP WHAT", "DOESN'T MATTER."], [WHITE, DREAM + (255,)], size=104, dim=0.4, glow_col=DREAM, y=H * 0.2)


SCENES = [s0_hook, s1_trudge, s2_heavy, s3_sometimes, s4_else, s5_end, s_follow]
