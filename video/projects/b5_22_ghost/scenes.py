"""THE GHOST OF YESTERDAY — a pale figure that follows you down a foggy street, showing you your mistakes.

World: a cobbled old-town street at night, iron lamps, thick blue fog. YESTERDAY is a tall, pale, translucent
ghost in the shape of the person, and in the fog around it float faded memory-frames of past mistakes.
THE PRESENT runs; the ghost only grows. The present stops, turns and looks at it; the ghost shrinks, and as the
person walks on toward a pale dawn it thins away into the sunlight.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, sun)
from kit import s_follow

TITLE = ("THE GHOST", "OF YESTERDAY")
OUTPUT = "122_The_Ghost_Of_Yesterday_16x9.mp4"
LINES = [
    "",
    "Your past can follow you.",
    "",
    "But it doesn't have to lead you.",
    "",
    "",
]
SILENT = {0: 3.0, 2: 3.6, 4: 3.4}
GAPS = {1: 2.6, 3: 6.0}

YOU = (236, 228, 214, 255)
GHOST = (170, 200, 255, 255)
LAMP = (255, 210, 140, 255)
MEMORIES = ["THE TEST I FAILED", "WHAT I SAID", "THE DAY I QUIT", "THE CHANCE I MISSED", "WHO I LET DOWN"]
CH = 230


def street(d, cam, t, dawn=0.0):
    draw_sky(d, mix((6, 10, 22, 255), (120, 150, 200, 255), dawn), mix((24, 34, 56, 255), (255, 200, 160, 255), dawn))
    if dawn > 0.05:
        sun(d, W * 0.8, cam.p(0, 0)[1] - cam.s(200), 70, dawn, (255, 220, 170, 255))
    # rows of old houses
    r = random.Random(3)
    x = -3000
    while x < 9000:
        w = r.uniform(260, 420)
        hgt = r.uniform(500, 900)
        a, b = cam.p(x, -hgt), cam.p(x + w, 0)
        if b[0] > -50 and a[0] < W + 50:
            c = mix((18, 22, 36, 255), (90, 90, 110, 255), dawn * 0.6)
            d.rectangle([a[0], a[1], b[0], b[1]], fill=c)
            d.polygon([(a[0] - cam.s(10), a[1]), ((a[0] + b[0]) / 2, a[1] - cam.s(w * 0.35)), (b[0] + cam.s(10), a[1])], fill=c)
            for k in range(2):
                wx = x + w * (0.3 + 0.4 * k)
                if r.random() < 0.5:
                    d.rectangle(cam.box(wx - 25, -hgt * 0.6, wx + 25, -hgt * 0.6 + 70), fill=mix(c, LAMP, 0.7 * (1 - dawn)))
        x += w + 10
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=mix((20, 22, 30, 255), (110, 100, 100, 255), dawn * 0.5))
        for k in range(-40, 120):  # cobbles
            cx = cam.p(k * 90, 30)[0]
            if -40 < cx < W + 40:
                d.ellipse([cx - cam.s(40), gy + cam.s(12), cx + cam.s(40), gy + cam.s(40)], fill=mix((30, 32, 42, 255), (130, 120, 115, 255), dawn * 0.5))
    for x in range(-2000, 9000, 900):  # lamps
        b, tp = cam.p(x, 0), cam.p(x, -520)
        if -100 < b[0] < W + 100:
            d.line([b, tp], fill=(30, 30, 36, 255), width=max(2, int(cam.s(12))))
            d.rectangle([tp[0] - cam.s(22), tp[1] - cam.s(50), tp[0] + cam.s(22), tp[1]], fill=mix((60, 60, 70, 255), LAMP, 1 - dawn))
            glow(d, tp[0], tp[1] - cam.s(25), cam.s(300), LAMP, 0.6 * (1 - dawn))
    fog(d, *cam.p(cam.cx, -150), cam.s(5000), 0.45 * (1 - dawn * 0.7), (150, 180, 230))
    fog(d, *cam.p(cam.cx - 800, -300), cam.s(3000), 0.3 * (1 - dawn), (150, 180, 230))


def ghost(d, cam, x, t, size=1.0, a=0.6, reach=0.0):
    fx, fy = cam.p(x, 0)
    h = cam.s(CH) * size
    glow(d, fx, fy - h * 0.5, h * 0.7, GHOST, 0.4 * a)
    hands = None
    if reach > 0:
        hands = ((fx + h * 0.1, fy - h * 0.4), (fx + h * lerp(0.15, 0.55, reach), fy - h * lerp(0.4, 0.65, reach)))
    figure(d, fx, fy, h, GHOST, mode="walk", phase=t * 2.5, face=1, a=a, acc=("hair",), hands=hands, eye_col=(255, 255, 255, 255),
           name="YESTERDAY", name_a=a, swing=0.2)


def memories(d, cam, t, cx, a=1.0, n=5):
    r = random.Random(9)
    for i in range(n):
        ph = (t * 0.25 + i / n) % 1
        x = cx + r.uniform(-900, 300) - ph * 200
        y = -r.uniform(350, 900)
        k = math.sin(math.pi * ph) * a
        if k <= 0.02:
            continue
        sx, sy = cam.p(x, y)
        w, h = cam.s(260), cam.s(170)
        tpoly(d, [(sx - w / 2, sy - h / 2), (sx + w / 2, sy - h / 2), (sx + w / 2, sy + h / 2), (sx - w / 2, sy + h / 2)], col((160, 190, 240, 255), 0.25 * k))
        polyline(d, [(sx - w / 2, sy - h / 2), (sx + w / 2, sy - h / 2), (sx + w / 2, sy + h / 2), (sx - w / 2, sy + h / 2), (sx - w / 2, sy - h / 2)], 1, col(GHOST, 0.7 * k), 2)
        figure(d, sx, sy + h * 0.38, h * 0.65, GHOST, mode="slump", a=0.6 * k, eyes=False, acc=("hair",))
        d.text((sx, sy + h / 2 + cam.s(24)), MEMORIES[i % len(MEMORIES)], font=font(max(10, int(cam.s(22)))), fill=col(GHOST, 0.85 * k), anchor="mm")


def you(d, cam, x, t, mode="walk", speed=1.0, **kw):
    fx, fy = cam.p(x, 0)
    figure(d, fx, fy, cam.s(CH), YOU, mode=mode, phase=x / (45 if mode == "run" else 55), face=kw.pop("face", 1), acc=("hair", "scarf"), **kw)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # fog and footsteps; a pale hand slides into frame behind the person's shoulder
    x = 200 * p
    cam = Cam(x + 80, -160, 1.6)
    street(d, cam, t)
    ghost(d, cam, x - 140, t, a=0.55 * ramp(t, 1.0, 1.2), reach=sstep(ramp(t, 1.3, 1.2)))
    you(d, cam, x, t, look=0.0, head_down=0.2)
    darkness(d, W / 2, H / 2, 0.5)


def s1_follow(d, t, dur):
    p = t / dur
    x = 200 + 800 * p
    cam = Cam(x + 100, -330, 0.75)
    street(d, cam, t)
    memories(d, cam, t, x, a=ramp(t, 0.3, 0.8))
    ghost(d, cam, x - 330, t, size=1.3, a=0.55)
    you(d, cam, x, t, look=-0.2, head_down=0.3, swing=0.3)
    top_caption(d, ["YOUR PAST CAN", "FOLLOW YOU."], t, dur, accent={"PAST", "FOLLOW"})


def s2_run(d, t, dur):
    p = t / dur
    # the person breaks into a run; the faster they go, the bigger the ghost gets
    x = 1000 + 1800 * sstep(p)
    cam = Cam(x + 50, -420 - 200 * p, lerp(0.75, 0.5, p))
    shake(cam, t, 4)
    street(d, cam, t)
    memories(d, cam, t, x, a=1.0, n=6)
    ghost(d, cam, x - lerp(330, 600, p), t, size=lerp(1.3, 3.6, sstep(p)), a=0.5)
    you(d, cam, x, t, mode="run", lean=0.35, swing=1.0, stride=1.4, tired=0.5, look=0.0)


def s3_lead(d, t, dur):
    p = t / dur
    # stop. turn. look at it. The ghost shrinks to the size of a memory; the person turns forward and
    # walks on into the dawn while the ghost thins away
    x = 2800 + 900 * sstep(ramp(p, 0.5, 0.5))
    turn = 0.12 < p < 0.5
    shrink = sstep(ramp(p, 0.18, 0.3))
    dawn = sstep(ramp(p, 0.45, 0.5))
    cam = Cam(lerp(2700, x + 150, sstep(ramp(p, 0.45, 0.5))), lerp(-620, -330, sstep(p)), lerp(0.5, 0.75, sstep(p)))
    street(d, cam, t, dawn=dawn)
    memories(d, cam, t, x, a=1 - shrink)
    ghost(d, cam, 2200 + 300 * shrink, t, size=lerp(3.6, 0.6, shrink), a=0.5 * (1 - dawn))
    if p < 0.5:
        you(d, cam, 2800, t, mode="stand", face=-1 if turn else 1, look=0.5 * (1 - shrink), lean=-0.1 if turn else 0.0)
    else:
        you(d, cam, x, t, look=0.2, mouth=0.4)
    top_caption(d, ["BUT IT DOESN'T HAVE", "TO LEAD YOU."], t, dur, accent={"LEAD"})


def s4_end(d, t, dur):
    x = 3700 + 120 * t
    cam = Cam(x + 150, -330, 0.75)
    street(d, cam, t, dawn=1.0)
    you(d, cam, x, t, look=0.2, mouth=0.4)
    stage_end(d, t, dur, ["MOVE FORWARD."], [(255, 220, 170, 255)], size=130, dim=0.4, glow_col=(255, 210, 160), y=H * 0.3)


SCENES = [s0_hook, s1_follow, s2_run, s3_lead, s4_end, s_follow]
