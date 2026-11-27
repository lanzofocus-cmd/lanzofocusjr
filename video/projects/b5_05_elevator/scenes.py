"""THE ELEVATOR OF EXCUSES — an elevator to SUCCESS that never moves.

World: an art-deco brass elevator in deep green and gold, a semicircular floor dial stuck on G, a panel of
glowing buttons: WAIT, NOT READY, PERFECT TIMING, MAYBE LATER... and one green START nobody presses.
EXCUSES is a slick grey-violet figure; THE PASSENGER waits in white; ACTION arrives in bright green.
Ends outside: a glass elevator shooting up a tower into the clouds.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, cloud, stars, dust)
from kit import s_follow

TITLE = ("THE ELEVATOR", "OF EXCUSES")
OUTPUT = "105_The_Elevator_Of_Excuses_16x9.mp4"
LINES = [
    "",
    "",
    "You've been pressing every button…",
    "Except the one that moves you.",
    "",
    "",
]
SILENT = {0: 2.8, 1: 3.4, 4: 4.4}
GAPS = {2: 1.6, 3: 2.4}

BRASS = (200, 160, 80, 255)
GREEN = (20, 50, 44, 255)
EXC = (150, 130, 180, 255)
PASS = (230, 228, 222, 255)
ACT = (90, 240, 140, 255)
CH = 600
BUTTONS = ["WAIT", "NOT READY", "PERFECT TIMING", "MAYBE LATER", "ONE DAY", "START"]


def car(d, cam, t, doors=0.0, light=1.0, flicker=False, dial=0.0):
    """Front view into the elevator car. doors: 0 closed .. 1 open."""
    draw_sky(d, (10, 12, 12, 255), (24, 26, 24, 255))
    # lobby wall around the doors
    d.rectangle([0, 0, W, H], fill=(30, 28, 24, 255))
    x0, x1 = cam.p(-520, 0)[0], cam.p(520, 0)[0]
    top, bot = cam.p(0, -1200)[1], cam.p(0, 0)[1]
    lit = light * (0.4 + 0.6 * (0.5 + 0.5 * math.sin(t * 31)) if flicker else 1)
    # inside of the car
    d.rectangle([x0, top, x1, bot], fill=col(mix((10, 20, 18, 255), GREEN, lit), 1))
    for k in range(1, 6):
        xx = lerp(x0, x1, k / 6)
        d.line([(xx, top), (xx, bot)], fill=col(BRASS, 0.25 * lit), width=max(1, int(cam.s(4))))
    glow(d, (x0 + x1) / 2, top + cam.s(80), cam.s(500), (255, 220, 160), 0.6 * lit)
    d.rectangle([x0, top, x1, top + cam.s(30)], fill=col((255, 230, 180, 255), lit))
    # frame and SUCCESS sign
    d.rectangle([x0 - cam.s(60), top - cam.s(60), x1 + cam.s(60), bot], outline=col(BRASS, 1), width=max(3, int(cam.s(24))))
    cx = (x0 + x1) / 2
    d.text((cx, top - cam.s(180)), "SUCCESS", font=font(max(12, int(cam.s(90)))), fill=col(BRASS, 1), anchor="mm")
    # floor dial
    dc = (cx, top - cam.s(330))
    r = cam.s(120)
    d.pieslice([dc[0] - r, dc[1] - r, dc[0] + r, dc[1] + r], 180, 360, fill=col((40, 34, 24, 255), 1), outline=col(BRASS, 1), width=max(2, int(cam.s(8))))
    for i, lbl in enumerate(["G", "1", "5", "20", "50", "∞"]):
        ang = math.radians(180 + 10 + i * 32)
        d.text((dc[0] + math.cos(ang) * r * 0.78, dc[1] + math.sin(ang) * r * 0.78), lbl, font=font(max(8, int(cam.s(24)))), fill=col(BRASS, 1), anchor="mm")
    ang = math.radians(180 + 10 + dial * 160 + 4 * math.sin(t * 25) * (dial < 0.05))
    d.line([dc, (dc[0] + math.cos(ang) * r * 0.9, dc[1] + math.sin(ang) * r * 0.9)], fill=col((240, 60, 50, 255), 1), width=max(2, int(cam.s(6))))
    return x0, x1, top, bot


def doors_draw(d, cam, x0, x1, top, bot, open_):
    half = (x1 - x0) / 2
    w = half * (1 - open_)
    for side in (-1, 1):
        if side < 0:
            d.rectangle([x0, top, x0 + w, bot], fill=col((160, 128, 64, 255), 1))
            d.line([(x0 + w, top), (x0 + w, bot)], fill=col((90, 70, 30, 255), 1), width=3)
        else:
            d.rectangle([x1 - w, top, x1, bot], fill=col((160, 128, 64, 255), 1))
            d.line([(x1 - w, top), (x1 - w, bot)], fill=col((90, 70, 30, 255), 1), width=3)


def panel(d, t, pressed=None, press_k=0.0, start_glow=1.0, hand=None, hand_col=EXC):
    """Full-screen close-up of the button panel."""
    d.rectangle([0, 0, W, H], fill=(28, 22, 14, 255))
    px0, px1, py0, py1 = W * 0.3, W * 0.7, H * 0.12, H * 0.95
    d.rounded_rectangle([px0, py0, px1, py1], 30, fill=(150, 116, 56, 255), outline=(220, 180, 100, 255), width=6)
    for i, lbl in enumerate(BUTTONS):
        y = py0 + 90 + i * 135
        bx = px0 + 120
        start = lbl == "START"
        on = (pressed == i) * press_k
        base = (40, 160, 90, 255) if start else (60, 50, 40, 255)
        fill = mix(base, (255, 230, 170, 255) if not start else (140, 255, 170, 255), on if not start else max(on, 0.3 * start_glow * (0.6 + 0.4 * math.sin(t * 3))))
        r = 46 - 6 * on
        d.ellipse([bx - r, y - r, bx + r, y + r], fill=col(fill, 1), outline=(230, 190, 110, 255), width=4)
        if start or on > 0:
            glow(d, bx, y, 140, (140, 255, 170) if start else (255, 220, 150), 0.6 * (start_glow if start else on))
        d.text((bx + 90, y), lbl, font=font(44), fill=(250, 235, 200, 255) if not start else (180, 255, 200, 255), anchor="lm")
    if hand:  # a finger coming in to press
        hx, hy = hand
        c = col(hand_col, 1)
        d.line([(W + 40, hy + 200), (hx + 60, hy + 20)], fill=c, width=70)
        d.ellipse([hx - 10, hy - 30, hx + 110, hy + 70], fill=c)
        d.line([(hx + 40, hy + 10), (hx - 6, hy)], fill=c, width=34)


def btn_pos(i):
    return (W * 0.3 + 120, H * 0.12 + 90 + i * 135)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # ding — the doors slide open on someone already waiting inside
    cam = cam_lerp((0, -600, 0.55), (0, -620, 0.62), p)
    x0, x1, top, bot = car(d, cam, t, flicker=t < 0.8)
    fx, fy = cam.p(-200, 0)
    figure(d, fx, fy, cam.s(CH), PASS, mode="stand", face=1, acc=("hair",), look=0.3, name="THE PASSENGER", name_a=ramp(t, 1.5, 0.4))
    ex, ey = cam.p(240, 0)
    figure(d, ex, ey, cam.s(CH), EXC, mode="stand", face=-1, acc=("hair", "glasses"), name="EXCUSES", name_a=ramp(t, 1.8, 0.4), mouth=0.6)
    doors_draw(d, cam, x0, x1, top, bot, sstep(ramp(t, 0.4, 1.2)))


def s1_buttons(d, t, dur):
    p = t / dur
    # close-ups: Excuses presses WAIT, NOT READY, PERFECT TIMING
    i = min(2, int(p * 3))
    u = p * 3 - i
    press = pulse(u, 0.55, 0.25)
    bx, by = btn_pos(i)
    hx = lerp(W + 100, bx + 10, sstep(ramp(u, 0.0, 0.45)))
    panel(d, t, pressed=i, press_k=press, hand=(hx, by - 10))
    if press > 0.5:
        d.text((W * 0.85, H * 0.5), "*CLICK*", font=font(48), fill=col(WHITE, press), anchor="mm")


def s2_every(d, t, dur):
    p = t / dur
    # inside: press after press; the dial twitches but never leaves G; the passenger waits, then sits
    cam = cam_lerp((0, -620, 0.62), (0, -560, 0.75), p)
    x0, x1, top, bot = car(d, cam, t, dial=0.02 * pulse((t * 2) % 1, 0.5, 0.2))
    fx, fy = cam.p(-200, 0)
    figure(d, fx, fy, cam.s(CH), PASS, mode="stand" if p < 0.5 else "sit", face=1, acc=("hair",), head_down=0.4 * p, look=-0.2)
    ex, ey = cam.p(240, 0)
    figure(d, ex, ey, cam.s(CH), EXC, mode="reach", face=1, acc=("hair", "glasses"), phase=t * 4, mouth=0.6)
    lbl = BUTTONS[int(t * 2.5) % 5]
    d.text((cam.p(450, -900)[0], cam.p(0, -900)[1]), lbl, font=font(int(cam.s(50))), fill=col((255, 220, 150, 255), 0.6 + 0.4 * math.sin(t * 8)), anchor="mm")
    top_caption(d, ["YOU'VE BEEN PRESSING", "EVERY BUTTON…"], t, dur, accent={"EVERY"})


def s3_except(d, t, dur):
    p = t / dur
    # the doors open: Action steps in, past Excuses, and presses START
    if p < 0.6:
        u = p / 0.6
        cam = cam_lerp((0, -560, 0.75), (60, -600, 0.62), u)
        x0, x1, top, bot = car(d, cam, t)
        fx, fy = cam.p(-200, 0)
        figure(d, fx, fy, cam.s(CH), PASS, mode="sit" if u < 0.6 else "stand", face=1, acc=("hair",), look=0.4)
        ex, ey = cam.p(220 + 180 * sstep(ramp(u, 0.4, 0.4)), 0)
        figure(d, ex, ey, cam.s(CH), EXC, mode="stand", face=-1, acc=("hair", "glasses"), lean=-0.2 * sstep(ramp(u, 0.4, 0.4)))
        walk = sstep(ramp(u, 0.2, 0.6))
        ax, ay = cam.p(lerp(-900, 120, walk), 0)
        glow(d, ax, ay - cam.s(150), cam.s(400), ACT, 0.5 * walk)
        figure(d, ax, ay, cam.s(CH), ACT, mode="walk" if walk < 1 else "reach", phase=t * 5, face=1, acc=("hair",), name="ACTION",
               eye_col=(10, 60, 30, 255), mouth=0.4)
    else:
        u = (p - 0.6) / 0.4
        press = sstep(ramp(u, 0.3, 0.3))
        bx, by = btn_pos(5)
        hx = lerp(W + 100, bx + 10, sstep(ramp(u, 0.0, 0.35)))
        panel(d, t, pressed=5, press_k=press, start_glow=1 + press, hand=(hx, by - 10), hand_col=ACT)
        if press > 0.5:
            overlay(d, (140, 255, 170), 0.25 * pulse(u, 0.7, 0.2))
    top_caption(d, ["EXCEPT THE ONE", "THAT MOVES YOU."], t, dur, accent={"MOVES"})


def s4_rise(d, t, dur):
    p = t / dur
    # outside: a glass elevator shooting up the face of a tower, through the clouds, into the light
    rise = sstep(ramp(t, 0.0, dur * 0.7)) * 4200
    cam = Cam(0, -600 - rise, lerp(0.6, 0.45, p))
    draw_sky(d, mix((30, 40, 80, 255), (80, 150, 230, 255), p), mix((255, 170, 120, 255), (255, 230, 200, 255), p))
    stars(d, 0.5 * (1 - p), seed=3, n=50)
    # the tower
    d.rectangle(cam.box(-260, -6000, 260, 400), fill=(40, 46, 60, 255))
    for k in range(-60, 4):
        y = k * 100
        for c in range(4):
            x = -220 + c * 120
            d.rectangle(cam.box(x, y, x + 70, y + 60), fill=col((255, 210, 140, 255), 0.5))
    # the glass car
    ey = -600 - rise
    d.rectangle(cam.box(-200, ey - 420, 200, ey), fill=col((140, 255, 190, 255), 0.25), outline=col(BRASS, 1), width=max(2, int(cam.s(10))))
    glow(d, *cam.p(0, ey - 200), cam.s(500), (140, 255, 170), 0.5)
    fx, fy = cam.p(-60, ey)
    figure(d, fx, fy, cam.s(260), PASS, mode="cheer", face=1, acc=("hair",), mouth=0.8)
    ax, ay = cam.p(80, ey)
    figure(d, ax, ay, cam.s(260), ACT, mode="stand", face=-1, acc=("hair",), eye_col=(10, 60, 30, 255))
    for j in range(6):  # clouds rushing past
        cy = cam.p(0, -2400 - j * 500)[1]
        cloud(d, (j * 380) % W, cy, cam.s(260), col(WHITE, 0.8), w=max(2, int(cam.s(40))))
    # speed lines
    for j in range(14):
        x = (j * 151) % W
        y = (j * 97 + t * 1500) % H
        d.line([(x, y), (x, y + 120)], fill=col(WHITE, 0.25 * (1 - p)), width=2)
    if p > 0.55:
        stage_end(d, t - dur * 0.55, dur, ["PRESS START."], [ACT], size=130, dim=0.25, glow_col=ACT)


SCENES = [s0_hook, s1_buttons, s2_every, s3_except, s4_rise, s_follow]
