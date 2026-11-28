"""THE HUNGRY WOLF — a wolf grown soft in a warm cave, and the day the food stops coming.

World: a cave mouth in a snowbound pine wilderness. Inside: firelight, and bowls of food that slide in on their own
out of a warm glow, COMFORT. THE WOLF, slate-grey with pale eyes, lies by the fire and grows slow. Then the bowls
stop, the fire dies, the cave turns cold blue. The wolf steps out into the snow, stumbles, finds its stride,
runs, and howls from a ridge as the dawn comes up: THE HUNT.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, snow, stars, moon, sun, limb)
from kit import s_follow

TITLE = ("THE HUNGRY", "WOLF")
OUTPUT = "139_The_Hungry_Wolf_16x9.mp4"
LINES = [
    "",
    "Comfort can feed you.",
    "",
    "But it can also weaken your ability to survive without it.",
    "",
    "",
]
SILENT = {0: 3.0, 2: 3.4, 4: 3.4}
GAPS = {1: 3.6, 3: 6.0}

WOLF = (120, 130, 150, 255)
WOLF_D = (80, 88, 104, 255)
FIRE = (255, 150, 60, 255)
COMFORT = (255, 200, 130, 255)


def wolf(d, cam, x, y, t, mode="walk", face=1, plump=0.0, s=1.0, speed=1.0, head_up=0.0):
    """A stylised wolf, side-on, standing at (x, y). mode: walk | run | lie | howl | stand."""
    def P(px, py):
        return cam.p(x + px * face * s, y + py * s)
    L = 120
    body_h = 70 + 30 * plump
    if mode == "lie":
        d.ellipse(cam.box(x - 170 * s, y - 80 * s - 20 * plump * s, x + 170 * s, y), fill=col(WOLF, 1))
        hx, hy = P(170, -70)
        d.ellipse([hx - cam.s(55 * s), hy - cam.s(45 * s), hx + cam.s(55 * s), hy + cam.s(40 * s)], fill=col(WOLF, 1))
        d.polygon([P(205, -80), P(285, -55), P(205, -40)], fill=col(WOLF, 1))
        for ex in (160, 190):
            d.polygon([P(ex - 15, -105), P(ex, -145), P(ex + 15, -105)], fill=col(WOLF_D, 1))
        ex, ey = P(210, -75)
        d.line([(ex - cam.s(10), ey), (ex + cam.s(10), ey)], fill=(20, 20, 30, 255), width=max(1, int(cam.s(5))))
        d.polygon([P(-170, -40), P(-280, -20), P(-170, -10)], fill=col(WOLF_D, 1))
        return
    ph = t * (6 if mode == "walk" else 11) * speed
    bounce = abs(math.sin(ph)) * (6 if mode == "walk" else 18) if mode in ("walk", "run") else 0
    by = -L - body_h / 2 - bounce
    # legs (back pair darker)
    for k, (lx, off, c) in enumerate(((-110, 0, WOLF_D), (110, math.pi, WOLF_D), (-90, math.pi, WOLF), (130, 0, WOLF))):
        if mode in ("walk", "run"):
            sw = math.sin(ph + off) * (35 if mode == "walk" else 70)
            lift = max(0.0, math.sin(ph + off)) * (25 if mode == "walk" else 50)
        else:
            sw, lift = 0, 0
        hip = P(lx, by + 20)
        knee = P(lx + sw * 0.5, -L * 0.5 - lift * 0.5)
        foot = P(lx + sw, -lift)
        limb(d, hip, knee, col(c, 1), cam.s(22 * s))
        limb(d, knee, foot, col(c, 1), cam.s(18 * s))
    # body
    d.ellipse(cam.box(x - 170 * s * 1, y + (by - body_h / 2) * s, x + 170 * s, y + (by + body_h / 2) * s), fill=col(WOLF, 1))
    # tail
    tl = 0.3 * math.sin(ph * 0.5) if mode != "howl" else -0.4
    d.polygon([P(-150, by - 10), P(-290, by + 30 + 40 * tl), P(-150, by + 20)], fill=col(WOLF_D, 1))
    # head: lifts for the howl
    hu = head_up if mode != "howl" else 1.0
    hx, hy = P(190, by - 40 - 60 * hu)
    d.polygon([P(140, by - 20), P(200, by - 70 - 60 * hu), P(230, by - 10 - 40 * hu), P(150, by + 25)], fill=col(WOLF, 1))
    d.ellipse([hx - cam.s(55 * s), hy - cam.s(45 * s), hx + cam.s(55 * s), hy + cam.s(40 * s)], fill=col(WOLF, 1))
    snout = [P(220, by - 50 - 70 * hu), P(300 - 40 * hu, by - 30 - 140 * hu), P(220, by - 15 - 50 * hu)]
    d.polygon(snout, fill=col(WOLF, 1))
    for ex in (170, 200):
        d.polygon([P(ex - 15, by - 75 - 60 * hu), P(ex - 10 * hu, by - 125 - 70 * hu), P(ex + 15, by - 75 - 60 * hu)], fill=col(WOLF_D, 1))
    ex, ey = P(212, by - 55 - 62 * hu)
    d.ellipse([ex - cam.s(8 * s), ey - cam.s(6 * s), ex + cam.s(8 * s), ey + cam.s(6 * s)], fill=(230, 240, 255, 255))
    return hx, hy


def cave(d, cam, t, warm=1.0, food=0):
    d.rectangle([0, 0, W, H], fill=mix((10, 14, 24, 255), (40, 24, 18, 255), warm))
    # rock walls arching over
    d.chord(cam.box(-2200, -1500, 1400, 600), 180, 360, fill=mix((20, 24, 34, 255), (60, 40, 30, 255), warm))
    d.chord(cam.box(-1900, -1250, 1100, 500), 180, 360, fill=mix((14, 18, 28, 255), (46, 30, 24, 255), warm))
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=mix((26, 30, 40, 255), (70, 50, 36, 255), warm))
    # fire
    fx, fy = cam.p(-500, 0)
    if warm > 0.05:
        glow(d, fx, fy - cam.s(100), cam.s(800), FIRE, 0.7 * warm)
        for k in range(3):
            hh = cam.s(140 * warm * (1 - k * 0.25)) * (0.85 + 0.15 * math.sin(t * 9 + k))
            d.polygon([(fx - hh * 0.45, fy), (fx + math.sin(t * 7 + k) * hh * 0.1, fy - hh), (fx + hh * 0.45, fy)], fill=col(((220, 70, 30), (255, 150, 40), (255, 220, 120))[k] + (255,), 1))
    d.line([(fx - cam.s(80), fy), (fx + cam.s(80), fy - cam.s(10))], fill=(80, 50, 30, 255), width=max(2, int(cam.s(16))))
    # bowls of food
    for i in range(food):
        bx, by = cam.p(-150 + i * 150, 0)
        d.chord([bx - cam.s(55), by - cam.s(50), bx + cam.s(55), by + cam.s(10)], 0, 180, fill=(150, 100, 60, 255))
        d.ellipse([bx - cam.s(45), by - cam.s(30), bx + cam.s(45), by - cam.s(10)], fill=(200, 120, 90, 255))


def wild(d, cam, t, dawn=0.0):
    draw_sky(d, mix((6, 10, 26, 255), (100, 130, 190, 255), dawn), mix((30, 40, 70, 255), (255, 190, 160, 255), dawn))
    stars(d, 0.8 * (1 - dawn), seed=39, n=90, ymax=0.5)
    moon(d, W * 0.78, H * 0.2, 60, 1 - dawn * 0.7, bg=mix((6, 10, 26, 255), (100, 130, 190, 255), dawn))
    if dawn > 0.05:
        sun(d, W * 0.2, cam.p(0, 0)[1] - cam.s(100), 70, dawn, (255, 220, 170, 255))
    r = random.Random(3)
    for f in (0.35, 0.65):
        for i in range(30):
            x = -4000 + i * 360 + r.uniform(-50, 50)
            sx = (x - cam.cx * f) * cam.z * (0.5 + 0.5 * f) + W / 2
            base = (0 - cam.cy * f) * cam.z * (0.5 + 0.5 * f) + H / 2
            hgt = r.uniform(200, 420) * cam.z * f
            d.polygon([(sx - hgt * 0.3, base), (sx, base - hgt), (sx + hgt * 0.3, base)], fill=mix((14, 24, 30, 255), (60, 80, 80, 255), dawn * f))
            d.polygon([(sx - hgt * 0.12, base - hgt * 0.6), (sx, base - hgt), (sx + hgt * 0.12, base - hgt * 0.6)], fill=(230, 236, 245, 255))
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=mix((210, 220, 236, 255), (250, 230, 220, 255), dawn))


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # total darkness; two pale eyes open; the camera eases back to show the cave and the fire
    cam = cam_lerp((300, -220, 2.4), (-100, -350, 0.8), sstep(ramp(t, 1.0, dur - 1.0)))
    cave(d, cam, t, warm=ramp(t, 1.2, 1.2), food=0)
    wolf(d, cam, 200, 0, t, mode="lie", face=-1)
    if t < 1.4:
        overlay(d, (0, 0, 0), 0.92)
        ex, ey = cam.p(200 - 210, -75)
        k = ramp(t, 0.4, 0.3)
        for o in (-1, 1):
            d.ellipse([ex + o * cam.s(30) - cam.s(12), ey - cam.s(6) * k, ex + o * cam.s(30) + cam.s(12), ey + cam.s(6) * k], fill=(230, 240, 255, 255))


def s1_feed(d, t, dur):
    p = t / dur
    # bowls slide in out of a warm glow; the wolf eats, sprawls, grows round and slow
    cam = Cam(0, -250, 1.1)
    cave(d, cam, t, warm=1.0, food=1 + int(p * 4))
    gx, gy = cam.p(700, -200)
    glow(d, gx, gy, cam.s(500), COMFORT, 0.6)
    d.text((gx, gy - cam.s(280)), "COMFORT", font=font(int(cam.s(40))), fill=col(COMFORT, 0.8), anchor="mm")
    wolf(d, cam, 200, 0, t, mode="lie", face=-1, plump=p)
    top_caption(d, ["COMFORT CAN", "FEED YOU."], t, dur, accent={"COMFORT", "FEED"})


def s2_stops(d, t, dur):
    p = t / dur
    # the bowls stop; the fire dies; the cave turns cold; the wolf lifts its head toward the cave mouth
    cam = cam_lerp((0, -250, 1.1), (300, -300, 1.0), p)
    cave(d, cam, t, warm=1 - sstep(p), food=5)
    wolf(d, cam, 200, 0, t, mode="lie" if p < 0.6 else "stand", face=1 if p > 0.6 else -1, plump=1.0, head_up=0.3)
    snow(d, t, 0.4 * p, n=60)


def s3_survive(d, t, dur):
    p = t / dur
    # out into the snow: a stagger, then a walk, then a run along the ridge; a howl as the dawn comes up
    dawn = sstep(ramp(p, 0.5, 0.5))
    x = lerp(0, 4200, sstep(ramp(p, 0.05, 0.8)) ** 1.2)
    mode = "walk" if p < 0.3 else ("run" if p < 0.82 else "howl")
    cam = Cam(x + 200, -320, lerp(0.75, 0.55, p))
    wild(d, cam, t, dawn=dawn)
    for k in range(int(x / 120)):  # paw prints behind
        px, py = cam.p(k * 120, 6)
        d.ellipse([px - cam.s(12), py - cam.s(6), px + cam.s(12), py + cam.s(6)], fill=(170, 180, 200, 255))
    wolf(d, cam, x, 0, t, mode=mode, face=1, plump=lerp(1.0, 0.0, sstep(ramp(p, 0.1, 0.5))), speed=lerp(0.6, 1.0, p))
    if mode == "howl":
        hx, hy = cam.p(x + 260, -360)
        for k in range(3):
            v = ((t * 0.8 + k / 3) % 1)
            rr = cam.s(80 + 300 * v)
            d.arc([hx - rr, hy - rr, hx + rr, hy + rr], 220, 320, fill=col(WHITE, 0.5 * (1 - v)), width=max(2, int(cam.s(6))))
    snow(d, t, 0.7 * (1 - dawn), n=140)
    top_caption(d, ["BUT IT CAN ALSO WEAKEN YOUR", "ABILITY TO SURVIVE WITHOUT IT."], t, dur, accent={"WEAKEN", "SURVIVE"})


def s4_end(d, t, dur):
    cam = Cam(4400, -320, 0.55)
    wild(d, cam, t, dawn=1.0)
    wolf(d, cam, 4200, 0, t, mode="howl", face=1)
    stage_end(d, t, dur, ["LEAVE THE CAVE."], [(255, 225, 190, 255)], size=120, dim=0.35, glow_col=(255, 210, 170), y=H * 0.25)


SCENES = [s0_hook, s1_feed, s2_stops, s3_survive, s4_end, s_follow]
