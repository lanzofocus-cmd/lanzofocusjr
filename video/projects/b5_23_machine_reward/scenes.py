"""THE MACHINE THAT REWARDED NOTHING — effort that seems to do nothing, until it does everything.

World: a colossal, mysterious machine tower in deep indigo with glass tubes, wheels, pistons and a dark crystal
orb at the top. THE WORKER (orange overalls) cranks and pulls at its base; nothing happens. Unseen, one tiny cog
deep inside moves. Then another. Light creeps up the tubes, wheel turns wheel, and finally THE REWARD, the orb,
blazes on and the whole machine erupts in lime-green light.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, dust)
from kit import s_follow

TITLE = ("THE MACHINE THAT", "REWARDED NOTHING")
OUTPUT = "123_The_Machine_That_Rewarded_Nothing_16x9.mp4"
LINES = [
    "",
    "",
    "Not every effort gives you an immediate reward.",
    "Some efforts…",
    "Are building the reward.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.4, 5: 3.4}
GAPS = {2: 2.0, 3: 1.6, 4: 4.6}

INDIGO = (24, 22, 50, 255)
METAL = (60, 60, 96, 255)
LIME = (160, 255, 110, 255)
WORK = (255, 150, 60, 255)
CH = 200

r0 = random.Random(23)
PARTS = []   # (kind, x, y, size, threshold)
for i in range(26):
    y = -150 - i * 90
    kind = r0.choice(["wheel", "wheel", "tube", "piston", "lamp"])
    PARTS.append((kind, r0.uniform(-380, 380), y, r0.uniform(50, 120), i / 26))
ORB_Y = -2600


def hall(d, cam, t, lit=0.0):
    draw_sky(d, mix((6, 6, 16, 255), (20, 40, 30, 255), lit), mix((18, 16, 38, 255), (40, 70, 50, 255), lit))
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=mix((14, 12, 26, 255), (30, 50, 36, 255), lit))
    fog(d, *cam.p(0, -300), cam.s(5000), 0.15 + 0.15 * lit, (150, 140, 255) if lit < 0.5 else (170, 255, 150))


def machine(d, cam, t, charge=0.0, burst=0.0):
    # tower body
    d.polygon([cam.p(-560, 0), cam.p(560, 0), cam.p(420, ORB_Y + 200), cam.p(-420, ORB_Y + 200)], fill=col(INDIGO, 1))
    for k in range(1, 12):
        y = -k * 220
        d.line([cam.p(-560 + k * 12, y), cam.p(560 - k * 12, y)], fill=col(METAL, 1), width=max(1, int(cam.s(6))))
    # pipes running up the sides (filling with light as charge rises)
    for s in (-1, 1):
        x = s * 470
        d.line([cam.p(x, 0), cam.p(x * 0.8, ORB_Y + 250)], fill=col(METAL, 1), width=max(2, int(cam.s(40))))
        fill_y = lerp(0, ORB_Y + 250, charge)
        if charge > 0:
            d.line([cam.p(x, 0), cam.p(lerp(x, x * 0.8, charge), fill_y)], fill=col(LIME, 0.9), width=max(2, int(cam.s(22))))
            glow(d, *cam.p(lerp(x, x * 0.8, charge), fill_y), cam.s(160), LIME, 0.7)
    for kind, x, y, s, th in PARTS:
        on = clamp((charge - th) * 8)
        c = mix(METAL, LIME, on)
        sx, sy = cam.p(x, y)
        R = cam.s(s)
        if kind == "wheel":
            rot = t * 3 * on * (1 if int(x) % 2 else -1)
            d.ellipse([sx - R, sy - R, sx + R, sy + R], outline=col(c, 1), width=max(2, int(cam.s(10))))
            for k in range(6):
                a = rot + k * math.pi / 3
                d.line([(sx, sy), (sx + math.cos(a) * R, sy + math.sin(a) * R)], fill=col(c, 1), width=max(1, int(cam.s(6))))
        elif kind == "tube":
            d.rounded_rectangle([sx - R * 0.3, sy - R, sx + R * 0.3, sy + R], int(R * 0.3), outline=col((140, 140, 190, 255), 1), width=max(1, int(cam.s(5))))
            if on > 0:
                d.rounded_rectangle([sx - R * 0.22, min(sy + R * 0.9, sy + R - 2 * R * on * 0.9), sx + R * 0.22, sy + R * 0.92], int(R * 0.2), fill=col(LIME, 0.9))
        elif kind == "piston":
            k = abs(math.sin(t * 4 + x)) * on
            d.rectangle([sx - R * 0.5, sy - R * 0.3, sx + R * 0.5, sy + R * 0.3], fill=col(METAL, 1))
            d.rectangle([sx + R * 0.5, sy - R * 0.12, sx + R * (0.5 + 0.8 * k), sy + R * 0.12], fill=col(c, 1))
        else:
            d.ellipse([sx - R * 0.3, sy - R * 0.3, sx + R * 0.3, sy + R * 0.3], fill=col(mix((40, 40, 60, 255), LIME, on), 1))
            if on > 0:
                glow(d, sx, sy, R * 1.5, LIME, 0.5 * on)
    # the orb
    ox, oy = cam.p(0, ORB_Y)
    R = cam.s(240)
    orb_on = clamp((charge - 0.95) * 20)
    d.ellipse([ox - R, oy - R, ox + R, oy + R], fill=col(mix((30, 30, 60, 255), (220, 255, 200, 255), orb_on), 1), outline=col(METAL, 1), width=max(2, int(cam.s(14))))
    if orb_on > 0:
        glow(d, ox, oy, R * (3 + 3 * burst), LIME, 0.9 * orb_on)
        for k in range(16):  # beams
            a = k * math.tau / 16 + t * 0.3
            L = R * (2 + 6 * burst)
            tpoly(d, [(ox, oy), (ox + math.cos(a - 0.04) * L, oy + math.sin(a - 0.04) * L), (ox + math.cos(a + 0.04) * L, oy + math.sin(a + 0.04) * L)], col(LIME, 0.3 * orb_on))
    d.text((ox, oy + R + cam.s(70)), "THE REWARD", font=font(int(clamp(cam.s(50), 14, 44))), fill=col(LIME if orb_on else (120, 120, 170, 255), 0.9), anchor="mm")
    # the crank at the base
    cx, cy = cam.p(-700, -160)
    d.ellipse([cx - cam.s(60), cy - cam.s(60), cx + cam.s(60), cy + cam.s(60)], fill=col(METAL, 1))


def worker(d, cam, t, mode="pull", **kw):
    fx, fy = cam.p(-860, 0)
    figure(d, fx, fy, cam.s(CH), WORK, mode=mode, phase=kw.pop("phase", t * 4), face=1, acc=("cap",), name="THE WORKER", **kw)


def crank_arm(d, cam, t, speed=1.0):
    cx, cy = cam.p(-700, -160)
    a = t * 4 * speed
    hx, hy = cx + math.cos(a) * cam.s(110), cy + math.sin(a) * cam.s(110)
    d.line([(cx, cy), (hx, hy)], fill=(150, 150, 190, 255), width=max(2, int(cam.s(16))))
    d.ellipse([hx - cam.s(20), hy - cam.s(20), hx + cam.s(20), hy + cam.s(20)], fill=col(WORK, 1))
    return hx, hy


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # tilt up a silent colossal machine to a dark orb, then drop back down to a tiny worker at its foot
    y = lerp(-200, ORB_Y, sstep(clamp(p * 1.6))) if p < 0.62 else lerp(ORB_Y, -500, sstep((p - 0.62) / 0.38))
    cam = Cam(0, y, 0.55 if p < 0.62 else lerp(0.55, 0.42, (p - 0.62) / 0.38))
    hall(d, cam, t)
    machine(d, cam, t)
    worker(d, cam, t, mode="stand", look=1.0)
    darkness(d, W / 2, H / 2, 0.5)


def s1_crank(d, t, dur):
    p = t / dur
    # crank and crank; nothing happens
    cam = Cam(-500, -380, 0.8)
    hall(d, cam, t)
    machine(d, cam, t)
    hx, hy = crank_arm(d, cam, t)
    worker(d, cam, t, mode="stand", hands=((hx, hy), (hx, hy)), lean=0.2, tired=p)
    d.text((W - 120, H - 110), "NOTHING.", font=font(36), fill=col(GREY, 0.6 * ramp(t, 1.5, 0.4)), anchor="rm")


def s2_reward(d, t, dur):
    p = t / dur
    # the worker sits down, beaten. Behind their back, deep in the machine, one tiny cog turns.
    cam = cam_lerp((-500, -380, 0.8), (-150, -320, 1.0), sstep(p))
    hall(d, cam, t)
    machine(d, cam, t, charge=0.04 * ramp(p, 0.55, 0.2))
    worker(d, cam, t, mode="sit_edge", head_down=0.6)
    if p > 0.55:  # a small spotlight on the first moving part
        kind, x, y, s, th = PARTS[0]
        glow(d, *cam.p(x, y), cam.s(220), LIME, 0.5 * ramp(p, 0.55, 0.2))
    top_caption(d, ["NOT EVERY EFFORT GIVES YOU", "AN IMMEDIATE REWARD."], t, dur, accent={"IMMEDIATE"})


def s3_some(d, t, dur):
    p = t / dur
    cam = cam_lerp((-150, -320, 1.0), (0, -800, 0.55), sstep(p))
    hall(d, cam, t, lit=0.1 * p)
    machine(d, cam, t, charge=lerp(0.04, 0.3, p))
    worker(d, cam, t, mode="stand", look=0.8)
    top_caption(d, ["SOME EFFORTS…"], t, dur, accent={"EFFORTS…"})


def s4_building(d, t, dur):
    p = t / dur
    # the chain reaction races up the tower; the orb blazes on; the whole machine erupts in light
    charge = lerp(0.3, 1.0, sstep(ramp(p, 0.0, 0.6)))
    burst = sstep(ramp(p, 0.6, 0.3))
    cy = lerp(-800, ORB_Y * 0.55, sstep(ramp(p, 0.0, 0.6)))
    cam = Cam(0, cy, lerp(0.55, 0.32, sstep(p)))
    shake(cam, t, 10 * pulse(p, 0.62, 0.05))
    hall(d, cam, t, lit=burst)
    machine(d, cam, t, charge=charge, burst=burst)
    worker(d, cam, t, mode="cheer" if burst > 0.3 else "stand", look=1.0, mouth=0.8 * burst)
    if burst > 0:
        particles(d, *cam.p(0, ORB_Y), cam.s(1500), clamp(burst * 1.2), LIME, n=80, seed=4, rise=0.3, size=6)
    dust(d, t, 0.7 * burst, n=60, color=(200, 255, 170))
    top_caption(d, ["ARE BUILDING", "THE REWARD."], t, dur, accent={"BUILDING"})


def s5_end(d, t, dur):
    cam = Cam(0, ORB_Y * 0.55, 0.32)
    hall(d, cam, t, lit=1.0)
    machine(d, cam, t, charge=1.0, burst=1.0)
    worker(d, cam, t, mode="stand", look=1.0, mouth=0.6)
    stage_end(d, t, dur, ["KEEP BUILDING."], [LIME], size=130, dim=0.45, glow_col=LIME)


SCENES = [s0_hook, s1_crank, s2_reward, s3_some, s4_building, s5_end, s_follow]
