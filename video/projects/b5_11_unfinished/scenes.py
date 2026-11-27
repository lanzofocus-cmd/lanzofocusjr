"""THE MOUNTAIN OF UNFINISHED PROJECTS — a mountain of plans, and one finished house.

World: split by a valley. On the left, THE COLLECTOR sits on a towering mountain of blueprint paper in cold
blueprint blue, ghostly plan-outlines of grand buildings floating above. On the right, on warm open ground at
golden hour, THE BUILDER finishes one terracotta house, then another, until a lit city stands there and the
wind starts carrying the paper mountain away.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, dust, stars, sun)
from render import dashed
from kit import s_follow

TITLE = ("THE MOUNTAIN OF", "UNFINISHED PROJECTS")
OUTPUT = "111_The_Mountain_Of_Unfinished_Projects_16x9.mp4"
LINES = [
    "",
    "Plans look impressive.",
    "",
    "Finished work changes everything.",
    "",
    "",
]
SILENT = {0: 3.2, 2: 4.2, 4: 3.4}
GAPS = {1: 2.4, 3: 5.4}

BLUE = (40, 90, 170, 255)
PAPER = (220, 232, 250, 255)
COL = (120, 170, 255, 255)
BUILD = (255, 170, 90, 255)
TERRA = (200, 110, 70, 255)
CH = 170
MTN_X = -1500
HOUSES = [(300 + i * 330, r) for i, r in enumerate([0.8, 1.0, 0.9, 1.2, 0.85, 1.1, 0.95, 1.3])]


def sky(d, night=0.0):
    draw_sky(d, mix((60, 90, 150, 255), (6, 10, 30, 255), night), mix((255, 190, 140, 255), (40, 40, 80, 255), night))


def paper_mountain(d, cam, t, h=1.0, blow=0.0):
    r = random.Random(3)
    top = -1200 * h
    pts = [cam.p(MTN_X - 1100, 0), cam.p(MTN_X - 300, top * 0.7), cam.p(MTN_X, top), cam.p(MTN_X + 350, top * 0.75), cam.p(MTN_X + 1000, 0)]
    d.polygon(pts, fill=col(BLUE, 1))
    for i in range(int(160 * h)):  # sheets and rolls making up the mountain
        u = r.random()
        side = r.uniform(-1, 1)
        y = -r.uniform(0, -top) * (1 - abs(side) * 0.7)
        x = MTN_X + side * (1000 * (1 + y / 1300))
        drift = blow * r.uniform(0.0, 1.0)
        if drift > 0.3 and r.random() < blow:
            continue
        sx, sy = cam.p(x, y)
        w = cam.s(r.uniform(50, 110))
        if u < 0.5:
            ang = r.uniform(-0.6, 0.6)
            pts2 = [(sx + math.cos(ang) * w - math.sin(ang) * w * 0.6, sy + math.sin(ang) * w + math.cos(ang) * w * 0.6) for _ in range(1)]
            d.polygon([(sx - w, sy - w * 0.4), (sx + w, sy - w * 0.6), (sx + w * 0.9, sy + w * 0.4), (sx - w * 1.1, sy + w * 0.5)], fill=col(mix(BLUE, PAPER, 0.25), 1), outline=col(COL, 1))
        else:
            d.rounded_rectangle([sx - w, sy - w * 0.2, sx + w, sy + w * 0.2], int(w * 0.2), fill=col(PAPER, 1))
            d.ellipse([sx + w - w * 0.2, sy - w * 0.2, sx + w + w * 0.2, sy + w * 0.2], fill=col(mix(PAPER, BLUE, 0.4), 1))
    return cam.p(MTN_X, top)


def ghost_plans(d, cam, t, a=1.0):
    """Grand plan outlines floating over the mountain."""
    r = random.Random(7)
    for i in range(6):
        x = MTN_X + (i - 2.5) * 380
        y = -1600 - 200 * (i % 2) + 30 * math.sin(t + i)
        w, h = r.uniform(140, 220), r.uniform(400, 800)
        pts = [cam.p(x - w / 2, y), cam.p(x + w / 2, y), cam.p(x + w / 2, y - h), cam.p(x, y - h - w * 0.6), cam.p(x - w / 2, y - h)]
        tpoly(d, pts, col(COL, 0.15 * a))
        dashed(d, pts + [pts[0]], col((200, 225, 255, 255), a), max(3, int(cam.s(10))), cam.s(24), cam.s(14))
        for k in range(int(h / 120)):
            yy = y - 60 - k * 120
            dashed(d, [cam.p(x - w / 2 + 20, yy), cam.p(x + w / 2 - 20, yy)], col(COL, 0.4 * a), 1, cam.s(10), cam.s(10))


def house(d, cam, x, s, k, t, night=0.0):
    """A house at x scaled by s, built to k (0 foundation .. 1 finished, lit)."""
    if k <= 0:
        return
    w, h = 220 * s, 200 * s
    d.rectangle(cam.box(x - w / 2 - 10, -16, x + w / 2 + 10, 0), fill=(120, 110, 100, 255))
    wall = clamp(k / 0.6)
    d.rectangle(cam.box(x - w / 2, -h * wall, x + w / 2, -16), fill=col(TERRA, 1))
    if k > 0.6:
        rk = clamp((k - 0.6) / 0.25)
        roof = [cam.p(x - w / 2 - 20, -h), cam.p(x, -h - h * 0.7 * rk), cam.p(x + w / 2 + 20, -h)]
        d.polygon(roof, fill=(140, 60, 50, 255))
    if k > 0.85:
        lit = clamp((k - 0.85) / 0.15)
        for wx in (x - w * 0.25, x + w * 0.25):
            d.rectangle(cam.box(wx - 22 * s, -h * 0.75, wx + 22 * s, -h * 0.45), fill=col(mix((60, 50, 40, 255), (255, 210, 130, 255), lit), 1))
            if night > 0.3:
                glow(d, *cam.p(wx, -h * 0.6), cam.s(80 * s), (255, 200, 120), 0.5 * lit)
        d.rectangle(cam.box(x - 20 * s, -h * 0.4, x + 20 * s, -16), fill=(90, 50, 40, 255))


def ground(d, cam, night=0.0):
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=mix((150, 110, 70, 255), (30, 26, 30, 255), night))
    # the valley gap between the two worlds
    d.polygon([cam.p(-350, 0), cam.p(150, 0), cam.p(0, 600), cam.p(-200, 600)], fill=mix((90, 70, 50, 255), (14, 12, 18, 255), night))


def collector(d, cam, t, top, lift=1.0):
    figure(d, top[0], top[1], cam.s(CH), (180, 200, 240, 255), mode="cheer" if lift > 0.5 else "sit", face=1, acc=("hair", "glasses"),
           name="THE COLLECTOR", mouth=0.6)
    if lift > 0.5:  # holding a plan aloft
        hx, hy = top[0], top[1] - cam.s(CH * 1.05)
        d.rectangle([hx - cam.s(60), hy - cam.s(40), hx + cam.s(60), hy + cam.s(10)], fill=col(PAPER, 1), outline=col(COL, 1))


def builder(d, cam, x, t, mode="hammer", name_a=1.0):
    fx, fy = cam.p(x, 0)
    figure(d, fx, fy, cam.s(CH), BUILD, mode=mode, phase=t * 6, face=1, acc=("cap",), name="THE BUILDER", name_a=name_a,
           prop=lambda dd, fh, bh, h, a: fh and mode == "hammer" and dd.rectangle([fh[0] - h * 0.05, fh[1] - h * 0.22, fh[0] + h * 0.05, fh[1] - h * 0.16], fill=col((200, 200, 210, 255), a)))


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # blueprints rain out of the dark and pile up into a mountain
    cam = cam_lerp((MTN_X, -600, 0.55), (MTN_X + 200, -900, 0.42), sstep(p))
    sky(d, night=0.8 - 0.4 * p)
    ground(d, cam, night=0.6)
    top = paper_mountain(d, cam, t, h=lerp(0.15, 1.0, sstep(p)))
    r = random.Random(int(t * 4))
    for i in range(30):  # sheets fluttering down
        x = MTN_X + r.uniform(-900, 900)
        y = -2200 + ((t * 600 + i * 120) % 2200)
        sx, sy = cam.p(x, y)
        ang = t * 3 + i
        w = cam.s(50)
        d.polygon([(sx - w * math.cos(ang), sy - w * 0.4), (sx + w * math.cos(ang), sy - w * 0.4), (sx + w * math.cos(ang), sy + w * 0.4), (sx - w * math.cos(ang), sy + w * 0.4)],
                  fill=col(PAPER, 0.9), outline=col(COL, 1))
    if p > 0.5:
        collector(d, cam, t, top, lift=0)


def s1_impressive(d, t, dur):
    p = t / dur
    cam = cam_lerp((MTN_X + 200, -900, 0.42), (MTN_X + 100, -1500, 0.55), sstep(p))
    sky(d, night=0.4)
    ground(d, cam, night=0.4)
    top = paper_mountain(d, cam, t)
    ghost_plans(d, cam, t, a=ramp(t, 0.2, 0.8))
    collector(d, cam, t, top, lift=1)
    top_caption(d, ["PLANS LOOK IMPRESSIVE."], t, dur, accent={"IMPRESSIVE."})


def s2_build(d, t, dur):
    p = t / dur
    # across the valley, on bare ground: one small house, start to finish
    cam = cam_lerp((300, -250, 1.0), (330, -230, 1.15), p)
    sky(d, night=0.1)
    ground(d, cam)
    house(d, cam, HOUSES[0][0], HOUSES[0][1], sstep(ramp(p, 0.05, 0.85)), t)
    builder(d, cam, 60, t, mode="hammer" if p < 0.9 else "cheer")
    dust(d, t, 0.5, n=40, color=(255, 210, 160))


def s3_changes(d, t, dur):
    p = t / dur
    # house after house, the city lights up at nightfall; the camera pulls back to see both worlds;
    # the wind starts carrying the paper mountain away
    night = sstep(ramp(p, 0.3, 0.6))
    cam = cam_lerp((330, -230, 1.15), (0, -800, 0.3), sstep(ramp(p, 0.05, 0.75)))
    sky(d, night=night)
    stars(d, night * 0.8, seed=5, n=80)
    ground(d, cam, night=night)
    top = paper_mountain(d, cam, t, blow=sstep(ramp(p, 0.5, 0.5)))
    collector(d, cam, t, top, lift=0)
    r = random.Random(1)
    n = 1 + 30 * sstep(ramp(p, 0.0, 0.8))
    for i in range(int(n) + 1):
        if i < len(HOUSES):
            x, s = HOUSES[i]
        else:
            x, s = 300 + (i % 10) * 300 + r.uniform(-50, 50), r.uniform(0.7, 1.6) * (1 + (i // 10) * 0.6)
        k = 1.0 if i < int(n) else n % 1
        house(d, cam, x, s, k, t, night)
    builder(d, cam, 60, t, mode="hammer", name_a=1 - night)
    if p > 0.5:  # sheets blowing off the mountain
        rr = random.Random(int(t * 5))
        for i in range(20):
            x = MTN_X + rr.uniform(-600, 600) + (t * 400) % 2000
            y = -rr.uniform(200, 1500)
            sx, sy = cam.p(x, y)
            d.rectangle([sx - cam.s(40), sy - cam.s(20), sx + cam.s(40), sy + cam.s(20)], fill=col(PAPER, 0.8))
    top_caption(d, ["FINISHED WORK", "CHANGES EVERYTHING."], t, dur, accent={"FINISHED", "EVERYTHING."})


def s4_end(d, t, dur):
    cam = Cam(0, -800, 0.3)
    sky(d, night=1.0)
    stars(d, 0.8, seed=5, n=80)
    ground(d, cam, night=1.0)
    top = paper_mountain(d, cam, t, blow=1.0)
    r = random.Random(1)
    for i in range(31):
        if i < len(HOUSES):
            x, s = HOUSES[i]
        else:
            x, s = 300 + (i % 10) * 300 + r.uniform(-50, 50), r.uniform(0.7, 1.6) * (1 + (i // 10) * 0.6)
        house(d, cam, x, s, 1.0, t, 1.0)
    stage_end(d, t, dur, ["FINISH SOMETHING."], [BUILD], size=120, dim=0.45, glow_col=BUILD, y=H * 0.3)


SCENES = [s0_hook, s1_impressive, s2_build, s3_changes, s4_end, s_follow]
