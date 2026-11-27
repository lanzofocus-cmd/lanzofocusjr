"""THE LAST LIGHT IN THE FOREST — a lantern that only ever shows the next few steps.

World: an enormous dark forest of black-blue trunks and drifting fog; the only colour is the lantern's warm
circle. DARKNESS lives at the edge of that circle as watching shapes with pale eyes that slide back as the light
comes near. The path appears stone by stone only inside the light. At the end the trees thin and the forest
opens onto a sunrise valley.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, light_hole, sun, dust)
from kit import s_follow

TITLE = ("THE LAST LIGHT", "IN THE FOREST")
OUTPUT = "110_The_Last_Light_In_The_Forest_16x9.mp4"
LINES = [
    "",
    "You don't need to see the entire path.",
    "You just need enough light…",
    "To take the next step.",
    "",
    "",
    "",
]
SILENT = {0: 3.0, 4: 4.8, 5: 3.4}
GAPS = {1: 1.8, 2: 0.8, 3: 3.0}

LAMP = (255, 190, 100, 255)
YOU = (230, 222, 210, 255)
TRUNK = (44, 38, 34, 255)
CH = 210

r0 = random.Random(2)
TREES = [(x + r0.uniform(-60, 60), r0.uniform(16, 34), r0.random()) for x in range(-1500, 9000, 260)]
EYES = [(r0.uniform(-1200, 8000), r0.uniform(-500, -150)) for _ in range(40)]


def forest(d, cam, t, dawn=0.0, thin=0.0):
    draw_sky(d, mix((12, 16, 26, 255), (90, 120, 180, 255), dawn), mix((22, 28, 40, 255), (255, 190, 140, 255), dawn))
    if dawn > 0.05:
        sun(d, W * 0.72, cam.p(0, 0)[1] - 120, 80, dawn, (255, 220, 160, 255))
    # back layers of trunks (parallax), fading with dawn
    for f, c, step in ((0.4, (26, 34, 50), 130), (0.7, (36, 44, 60), 160)):
        r = random.Random(int(f * 100))
        x = -2000
        while x < 12000:
            sx = (x - cam.cx * f) * cam.z * (0.5 + 0.5 * f) + W / 2
            wv = r.uniform(30, 70) * cam.z * f
            keep = r.random() > thin * 1.15
            if -100 < sx < W + 100 and keep:
                d.rectangle([sx - wv, 0, sx + wv, H], fill=tuple(mix(c + (255,), (120, 120, 150, 255), dawn * 0.6))[:3] + (255,))
            x += step + r.uniform(-40, 40)
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=mix((10, 12, 16, 255), (70, 60, 50, 255), dawn))
    fog(d, *cam.p(cam.cx, -120), cam.s(6000), 0.25 + 0.1 * dawn, (150, 170, 200))


def near_trees(d, cam, t, thin=0.0, dawn=0.0):
    for x, w, u in TREES:
        if u < thin:
            continue
        sx, gy = cam.p(x, 0)
        if -200 < sx < W + 200:
            wv = cam.s(w)
            d.rectangle([sx - wv, 0, sx + wv, gy + cam.s(10)], fill=mix(TRUNK, (60, 60, 70, 255), dawn * 0.5))
            # roots
            d.polygon([(sx - wv * 2, gy + cam.s(8)), (sx - wv, gy - cam.s(60)), (sx + wv, gy - cam.s(60)), (sx + wv * 2, gy + cam.s(8))], fill=mix(TRUNK, (60, 60, 70, 255), dawn * 0.5))


def path_stones(d, cam, lx, radius):
    """Stones visible only near the lantern."""
    for k in range(-20, 80):
        x = k * 120
        dist = abs(x - lx)
        a = clamp(1 - dist / radius)
        if a <= 0:
            continue
        sx, sy = cam.p(x, 8)
        d.ellipse([sx - cam.s(45), sy - cam.s(10), sx + cam.s(45), sy + cam.s(10)], fill=col((120, 110, 95, 255), a))


def eyes(d, cam, t, lx, radius, a=1.0):
    for i, (x, y) in enumerate(EYES):
        dist = abs(x - lx)
        if dist < radius * 0.9 or dist > radius * 2.6:
            continue
        k = clamp((dist - radius * 0.9) / (radius * 0.5)) * clamp((radius * 2.6 - dist) / radius) * a
        blink = math.sin(t * 2 + i * 3) > 0.92
        if blink:
            continue
        sx, sy = cam.p(x, y)
        for o in (-1, 1):
            d.ellipse([sx + o * cam.s(14) - cam.s(6), sy - cam.s(3), sx + o * cam.s(14) + cam.s(6), sy + cam.s(3)], fill=col((200, 220, 255, 255), k))


def traveler(d, cam, x, t, walking=True, lift=0.0, a=1.0):
    fx, fy = cam.p(x, 0)
    h = cam.s(CH)
    hand = (fx + h * 0.3, fy - h * lerp(0.55, 0.95, lift))
    figure(d, fx, fy, h, YOU, mode="walk" if walking else "stand", phase=x / 50, face=1, acc=("hair", "backpack"), swing=0.35,
           hands=((fx - h * 0.05, fy - h * 0.3), hand), look=0.3 + 0.5 * lift, a=a)
    # the lantern
    lx, ly = hand[0], hand[1] + h * 0.1
    d.line([hand, (lx, ly - h * 0.03)], fill=col((80, 70, 60, 255), a), width=2)
    d.rounded_rectangle([lx - h * 0.05, ly - h * 0.03, lx + h * 0.05, ly + h * 0.1], int(h * 0.02), fill=col((255, 230, 170, 255), a), outline=col((90, 70, 50, 255), a), width=2)
    return lx, ly + h * 0.03


def scene_core(d, cam, t, x, radius, walking=True, lift=0.0, dawn=0.0, thin=0.0, dark=1.0):
    forest(d, cam, t, dawn, thin)
    near_trees(d, cam, t, thin, dawn)
    path_stones(d, cam, x + 80, radius)
    lx, ly = traveler(d, cam, x, t, walking, lift)
    eyes(d, cam, t, x, radius)
    rr = cam.s(radius) * (1 + 0.03 * math.sin(t * 13) + 0.02 * math.sin(t * 7))
    light_hole(d, lx, ly, rr, a=dark * (1 - dawn))
    glow(d, lx, ly, cam.s(radius * 0.7), LAMP, 0.6)
    eyes(d, cam, t, x, radius, a=dark)  # eyes stay visible in the dark
    dust(d, t, 0.3, n=30, color=(255, 210, 160))
    return lx, ly


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # total darkness: a match flares, the lantern catches, a face and three trees appear
    cam = Cam(120, -160, 1.4)
    strike = pulse(t, 0.8, 0.15)
    lit = ramp(t, 1.0, 0.6)
    radius = lerp(40, 380, lit) + 60 * strike
    if t < 0.75:
        overlay(d, (0, 0, 0), 1.0)
        return
    scene_core(d, cam, t, 0, radius, walking=False, lift=0.3)
    if strike > 0:
        lx, ly = cam.p(80, -150)
        particles(d, lx, ly, 80, strike, (255, 210, 120), n=16, seed=1, rise=0.6)


def s1_entire(d, t, dur):
    p = t / dur
    # holding the lantern high to see far ahead: the light still only reaches a few steps
    cam = cam_lerp((120, -160, 1.4), (300, -300, 0.8), sstep(p))
    lift = sstep(ramp(t, 0.2, 0.8))
    scene_core(d, cam, t, 0, 420 + 60 * lift, walking=False, lift=lift)
    top_caption(d, ["YOU DON'T NEED TO SEE", "THE ENTIRE PATH."], t, dur, accent={"ENTIRE"})


def s2_enough(d, t, dur):
    p = t / dur
    x = 600 * sstep(p)
    cam = Cam(x + 250, -260, 0.9)
    scene_core(d, cam, t, x, 450)
    top_caption(d, ["YOU JUST NEED", "ENOUGH LIGHT…"], t, dur, accent={"LIGHT…"})


def s3_next(d, t, dur):
    p = t / dur
    # a long tracking walk: stones appear one by one at the edge of the light, the eyes slide away
    x = lerp(600, 3600, p)
    cam = Cam(x + 200, -260 + 30 * math.sin(t * 0.6), lerp(0.9, 0.75, p))
    scene_core(d, cam, t, x, 450)
    top_caption(d, ["TO TAKE THE", "NEXT STEP."], t, dur, accent={"NEXT", "STEP."})


def s4_dawn(d, t, dur):
    p = t / dur
    # the trees thin, the darkness lifts, and the forest opens onto a sunrise valley
    x = lerp(3600, 6000, sstep(p))
    dawn = sstep(ramp(p, 0.25, 0.65))
    cam = Cam(x + lerp(200, 600, p), -300, lerp(0.75, 0.45, sstep(p)))
    scene_core(d, cam, t, x, 450 + 900 * dawn, dawn=dawn, thin=dawn * 0.95)
    if dawn > 0.4:  # the valley beyond
        gy = cam.p(0, 0)[1]
        for i, c in enumerate(((120, 140, 110), (90, 120, 90))):
            pts = [(0, gy)] + [(j * W / 20, gy - 40 - 50 * math.sin(j * 0.8 + i) - i * 20) for j in range(21)] + [(W, gy)]
            tpoly(d, pts, col(c + (255,), (dawn - 0.4) / 0.6))


def s5_end(d, t, dur):
    x = 6000
    cam = Cam(x + 600, -300, 0.45)
    scene_core(d, cam, t, x, 1400, walking=False, dawn=1.0, thin=0.95)
    stage_end(d, t, dur, ["TAKE THE NEXT STEP."], [LAMP], size=120, dim=0.4, glow_col=LAMP)


SCENES = [s0_hook, s1_entire, s2_enough, s3_next, s4_dawn, s5_end, s_follow]
