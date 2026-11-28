"""THE SHADOW THAT GREW — the thing you run from gets bigger; the thing you face shrinks.

World: a long night street seen side-on, one endless violet concrete wall with posters peeling, a single amber
streetlamp. THE PERSON (white jacket) notices their shadow on the wall is a little too big, with two pale eyes.
They run; with every stride the SHADOW stretches taller until it towers over the whole wall and they are cornered
at a dead end. They turn around, lift a small lantern, and step toward it: each step the shadow shrinks, until it
is just an ordinary shadow at their feet, and the wall warms to morning.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, dust)
from kit import s_follow

TITLE = ("THE SHADOW", "THAT GREW")
OUTPUT = "144_The_Shadow_That_Grew_16x9.mp4"
LINES = [
    "",
    "",
    "Some things become bigger…",
    "Because you refuse to face them.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.6, 4: 3.4}
GAPS = {2: 2.4, 3: 6.6}

PERSON = (235, 235, 245, 255)
SHADOW = (8, 6, 18, 255)
LAMP = (255, 190, 110)
CH = 220


def street(d, cam, t, warm=0.0, lamp_x=-600):
    wall = mix((60, 50, 90, 255), (200, 150, 120, 255), warm)
    d.rectangle([0, 0, W, H], fill=wall)
    # panel seams and posters along the wall
    for k in range(-20, 40):
        x = k * 400
        a = cam.p(x, -2000)
        b = cam.p(x, 0)
        if -50 < a[0] < W + 50:
            d.line([a, b], fill=mix((45, 38, 72, 255), (170, 125, 100, 255), warm), width=max(1, int(cam.s(4))))
        r = random.Random(k)
        if r.random() < 0.45:
            px, py = x + r.uniform(60, 200), -r.uniform(500, 800)
            q0, q1 = cam.p(px, py), cam.p(px + 140, py + 190)
            if -300 < q0[0] < W + 300:
                d.rectangle([q0[0], q0[1], q1[0], q1[1]], fill=mix(r.choice([(90, 60, 110, 255), (70, 80, 120, 255), (110, 70, 80, 255)]), (230, 190, 150, 255), warm * 0.6))
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=mix((30, 26, 44, 255), (110, 90, 80, 255), warm))
        d.line([(0, gy), (W, gy)], fill=mix((80, 70, 110, 255), (220, 180, 140, 255), warm), width=max(2, int(cam.s(8))))
    # the streetlamp
    lx, ly = cam.p(lamp_x, -620)
    bx, by = cam.p(lamp_x, 0)
    d.line([(bx, by), (lx, ly)], fill=(30, 28, 40, 255), width=max(2, int(cam.s(16))))
    d.line([(lx, ly), (lx + cam.s(80), ly)], fill=(30, 28, 40, 255), width=max(2, int(cam.s(12))))
    flick = 1.0 if (t * 7) % 5 > 0.3 else 0.6
    glow(d, lx + cam.s(80), ly + cam.s(20), cam.s(700), LAMP, 0.35 * flick * (1 - warm))
    d.ellipse([lx + cam.s(60), ly, lx + cam.s(100), ly + cam.s(34)], fill=(255, 220, 160, 255))


def shadow(d, cam, x, t, size, mode="walk", phase=0.0, face=1, eyes=1.0, a=0.9, lean=0.0):
    """The shadow on the wall: a dark copy of the person, feet at x, `size` times their height."""
    fx, fy = cam.p(x, 0)
    h = cam.s(CH * size)
    if h < 4:
        return
    figure(d, fx, fy, h, SHADOW, mode=mode, phase=phase, face=face, a=a, eyes=False, mouth=0, lean=lean)
    if eyes > 0.02 and size > 1.2:
        ex = fx + face * h * 0.03
        ey = fy - h * 0.9
        for o in (-1, 1):
            r = h * 0.012
            glow(d, ex + o * h * 0.025, ey, r * 6, (200, 190, 255), 0.4 * eyes)
            d.ellipse([ex + o * h * 0.025 - r, ey - r * 0.6, ex + o * h * 0.025 + r, ey + r * 0.6], fill=(220, 215, 255, int(230 * eyes)))


def person(d, cam, x, t, mode="walk", lantern=0.0, **kw):
    fx, fy = cam.p(x, 0)
    face = kw.pop("face", 1)

    def lamp(dd, fh, bh, hh, a):
        if fh and lantern > 0:
            cx, cy = fh[0] + face * hh * 0.02, fh[1] + hh * 0.06
            dd.rectangle([cx - hh * 0.03, cy - hh * 0.04, cx + hh * 0.03, cy + hh * 0.04], fill=(255, 220, 150, int(255 * lantern)))
    figure(d, fx, fy, cam.s(CH), PERSON, mode=mode, phase=kw.pop("phase", t * 6), face=face, acc=("hood",), name=kw.pop("name", "THE PERSON"),
           prop=lamp, **kw)
    if lantern > 0:
        glow(d, fx + face * cam.s(CH * 0.1), fy - cam.s(CH * 0.45), cam.s(500 * lantern), (255, 210, 140), 0.55 * lantern)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # close on a walking person; on the wall behind, their shadow... a beat late, a little too big, then two eyes open
    cam = Cam(lerp(-200, 100, p), -260, 1.3)
    street(d, cam, t)
    x = lerp(-300, 0, p)
    shadow(d, cam, x - 120, t, lerp(1.0, 1.35, sstep(p)), phase=(t - 0.25) * 6, eyes=sstep(ramp(p, 0.65, 0.2)))
    person(d, cam, x, t, mode="walk", phase=t * 6, name="", look=-0.4 * sstep(ramp(p, 0.75, 0.2)))


def s1_run(d, t, dur):
    p = t / dur
    # they run; every stride the shadow stretches taller along the wall
    x = lerp(0, 2400, p)
    cam = cam_lerp((x + 200, -300, 0.9), (x + 300, -700, 0.55), sstep(p))
    street(d, cam, t, lamp_x=-600)
    size = lerp(1.4, 4.2, sstep(p)) + 0.15 * math.sin(t * 9)
    shadow(d, cam, x - lerp(200, 500, p), t, size, mode="run", phase=t * 9, eyes=1.0, lean=0.15)
    person(d, cam, x, t, mode="run", phase=t * 10, look=-0.5, lean=0.2)
    shake(cam, t, 2 * p)


def s2_bigger(d, t, dur):
    p = t / dur
    # a dead end; the shadow fills the wall from floor to sky, leaning over them
    cam = cam_lerp((2600, -700, 0.55), (2500, -900, 0.42), sstep(p))
    street(d, cam, t, lamp_x=1500)
    # dead-end wall
    d.rectangle(cam.box(3000, -2400, 3600, 0), fill=(40, 32, 60, 255))
    size = lerp(4.2, 7.0, sstep(p)) + 0.1 * math.sin(t * 2)
    shadow(d, cam, 2100, t, size, mode="stand", face=1, eyes=1.0, lean=0.25 * sstep(p))
    person(d, cam, 2850, t, mode="crouch", face=-1, name="", head_down=True)
    top_caption(d, ["SOME THINGS", "BECOME BIGGER…"], t, dur, accent={"BIGGER…"})


def s3_face(d, t, dur):
    p = t / dur
    # they turn, lift a little lantern, and step toward it; with each step it shrinks, and morning comes
    turn = sstep(ramp(p, 0.05, 0.12))
    steps = sstep(ramp(p, 0.15, 0.6))
    warm = sstep(ramp(p, 0.55, 0.4))
    cam = cam_lerp((2500, -900, 0.42), (2300, -380, 1.0), sstep(ramp(p, 0.1, 0.7)))
    street(d, cam, t, warm=warm, lamp_x=1500)
    d.rectangle(cam.box(3000, -2400, 3600, 0), fill=mix((40, 32, 60, 255), (180, 130, 110, 255), warm))
    px = lerp(2850, 2300, steps)
    size = lerp(7.0, 1.0, steps ** 0.8)
    sx = lerp(2100, px - 90, steps)
    shadow(d, cam, sx, t, size, mode="stand", face=1, eyes=1 - steps, a=lerp(0.9, 0.45, steps))
    mode = "stand" if p < 0.15 else ("walk" if steps < 0.98 else "stand")
    person(d, cam, px, t, mode=mode, face=-1 if turn > 0.5 else -1, lantern=sstep(ramp(p, 0.08, 0.1)), phase=px / 40,
           mouth=0.5 * warm, name="")
    if 0.2 < p < 0.8:
        particles(d, *cam.p(px - 60, -100), cam.s(260), (p - 0.2) / 0.6, (255, 210, 140), n=16, seed=3, rise=0.4)
    dust(d, t, 0.5 * warm, n=40, color=(255, 220, 170))
    top_caption(d, ["BECAUSE YOU REFUSE", "TO FACE THEM."], t, dur, accent={"REFUSE", "FACE"})


def s4_end(d, t, dur):
    cam = Cam(2300, -380, 1.0)
    street(d, cam, t, warm=1.0, lamp_x=1500)
    d.rectangle(cam.box(3000, -2400, 3600, 0), fill=(180, 130, 110, 255))
    shadow(d, cam, 2210, t, 1.0, mode="stand", face=-1, eyes=0, a=0.45)
    person(d, cam, 2300, t, mode="stand", face=-1, lantern=1.0, mouth=0.6, name="")
    stage_end(d, t, dur, ["FACE IT."], [(255, 210, 150, 255)], size=150, dim=0.4, glow_col=LAMP, y=H * 0.3)


SCENES = [s0_hook, s1_run, s2_bigger, s3_face, s4_end, s_follow]
