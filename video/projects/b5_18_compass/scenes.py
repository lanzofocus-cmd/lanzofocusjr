"""THE BROKEN COMPASS — a crossroads of eight roads, a crowd of pointing voices, and one quiet needle.

World: a windswept grey-gold plain at dusk seen from a high crane angle, eight roads radiating from one junction.
THE NOISE is a ring of grey figures who each point a different way, arrows flying from their hands. THE
TRAVELER's brass compass spins helplessly. When the traveler closes their eyes and stops listening, the noise
fades, the needle settles, and one road lights up gold.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, PCam, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, back_figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, dust, sun)
from kit import s_follow

TITLE = ("THE BROKEN", "COMPASS")
OUTPUT = "118_The_Broken_Compass_16x9.mp4"
LINES = [
    "",
    "",
    "Too many directions…",
    "Can make you forget your own.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.2, 4: 3.6}
GAPS = {2: 1.4, 3: 6.0}

GOLD = (255, 200, 100, 255)
BRASS = (210, 165, 80, 255)
NOISE = (130, 130, 140, 255)
YOU = (236, 230, 222, 255)
ROADS = [i * math.tau / 8 + 0.2 for i in range(8)]
TRUE_ROAD = 2


def plain(d, cam, t, lit=0.0):
    draw_sky(d, (40, 40, 60, 255), (230, 170, 120, 255), h=int(max(2, cam.horizon)))
    sun(d, W * 0.7, cam.horizon - 30, 60, 0.8, (255, 210, 150, 255))
    d.rectangle([0, cam.horizon, W, H], fill=(120, 110, 80, 255))
    for i, a in enumerate(ROADS):
        L = 9000
        ca, sa = math.cos(a), math.sin(a)
        w = 130
        q = cam.quad([(-sa * w, ca * w, 0), (sa * w, -ca * w, 0), (ca * L + sa * w, sa * L - ca * w, 0), (ca * L - sa * w, sa * L + ca * w, 0)]) if False else None
        pts = []
        for (u, v) in ((0, -w), (0, w), (L, w), (L, -w)):
            x, z = ca * u - sa * v, sa * u + ca * v
            pts.append((x, z + 1500, 0))
        q = cam.quad(pts)
        if q:
            c = mix((160, 150, 120, 255), GOLD, lit if i == TRUE_ROAD else 0)
            d.polygon(q, fill=c)
            if i == TRUE_ROAD and lit > 0:
                glow(d, (q[0][0] + q[1][0]) / 2, (q[0][1] + q[1][1]) / 2, 400, GOLD, 0.4 * lit)
    # signpost
    p = cam.p(0, 1500, 0)
    if p:
        sx, sy, s = p
        d.line([(sx, sy), (sx, sy - 700 * s)], fill=(90, 70, 50, 255), width=max(2, int(30 * s)))
        r = random.Random(2)
        for j in range(6):
            ang = r.uniform(-0.6, 0.6)
            yy = sy - (380 + j * 50) * s
            d.polygon([(sx, yy), (sx + math.cos(ang) * 260 * s * (1 if j % 2 else -1), yy + math.sin(ang) * 60 * s), (sx + math.cos(ang) * 260 * s * (1 if j % 2 else -1), yy + math.sin(ang) * 60 * s + 30 * s), (sx, yy + 30 * s)],
                      fill=(150, 120, 80, 255))
    fog(d, W / 2, cam.horizon + 40, 2600, 0.25, (255, 220, 190))


def noise_ring(d, cam, t, a=1.0, shout=True):
    r = random.Random(7)
    for i in range(10):
        ang = i * math.tau / 10 + 0.3
        x, z = math.cos(ang) * 900, 1500 + math.sin(ang) * 700
        p = cam.p(x, z, 0)
        if not p:
            continue
        sx, sy, s = p
        h = 340 * s
        point_ang = r.uniform(0, math.tau)
        tx, ty = sx + math.cos(point_ang) * h * 0.6, sy - h * 0.7 + math.sin(point_ang) * h * 0.3
        figure(d, sx, sy, h, NOISE, mode="stand", face=1 if math.cos(point_ang) > 0 else -1, a=a, acc=("hair",),
               hands=((sx, sy - h * 0.35), (tx, ty)), mouth=0.0)
        if shout and a > 0.05:
            # arrows flying out of the pointing hand
            for k in range(2):
                u = ((t * 0.9 + k * 0.5 + i * 0.13) % 1)
                ax, ay = tx + math.cos(point_ang) * u * 500 * s * 3, ty + math.sin(point_ang) * u * 200 * s * 3
                bx, by = ax - math.cos(point_ang) * 60 * s * 3, ay - math.sin(point_ang) * 20 * s * 3
                d.line([(bx, by), (ax, ay)], fill=col((240, 90, 70, 255), a * (1 - u)), width=max(2, int(8 * s)))
                d.polygon([(ax, ay), (ax - math.cos(point_ang - 0.5) * 30 * s * 3, ay - math.sin(point_ang - 0.5) * 30 * s), (ax - math.cos(point_ang + 0.5) * 30 * s * 3, ay - math.sin(point_ang + 0.5) * 30 * s)],
                          fill=col((240, 90, 70, 255), a * (1 - u)))
            words = ["THIS WAY!", "GO BACK!", "TRUST ME!", "NOT THAT ONE!", "FOLLOW US!"]
            if math.sin(t * 2 + i) > 0.4:
                d.text((sx, sy - h * 1.25), words[i % 5], font=font(int(clamp(h * 0.12, 14, 30))), fill=col(WHITE, 0.8 * a), anchor="mm")


def traveler(d, cam, t, spin=0.0, still=False, walk=0.0):
    x, z = 0, 1500 - 250 + walk * 3000
    if walk > 0:
        a = ROADS[TRUE_ROAD]
        x, z = math.cos(a) * walk * 3000, 1500 + math.sin(a) * walk * 3000
    p = cam.p(x, z, 0)
    if not p:
        return
    sx, sy, s = p
    h = 340 * s
    if walk > 0:
        back_figure(d, sx, sy, h, YOU, t, t * 5, 0.7, acc=("scarf",))
    else:
        face = 1 if math.sin(spin) > 0 else -1
        figure(d, sx, sy, h, YOU, mode="stand" if not still else "slump", face=face, acc=("hair", "scarf"), look=0.3, head_down=0.0 if not still else -0.2,
               hands=((sx + face * h * 0.18, sy - h * 0.5), (sx + face * h * 0.22, sy - h * 0.48)), name="THE TRAVELER")
        # compass held in the hands
        cx, cy = sx + face * h * 0.2, sy - h * 0.5
        d.ellipse([cx - h * 0.06, cy - h * 0.06, cx + h * 0.06, cy + h * 0.06], fill=col(BRASS, 1))


def compass_close(d, t, spin_speed=1.0, settle=0.0, crack=True):
    """Full-frame macro of the compass face."""
    cx, cy, R = W / 2, H / 2 + 40, 380
    d.rectangle([0, 0, W, H], fill=(30, 22, 16, 255))
    glow(d, cx, cy, R * 1.6, (255, 200, 120), 0.4)
    d.ellipse([cx - R * 1.1, cy - R * 1.1, cx + R * 1.1, cy + R * 1.1], fill=col((150, 110, 50, 255), 1))
    d.ellipse([cx - R, cy - R, cx + R, cy + R], fill=col((240, 228, 200, 255), 1))
    for i, lbl in enumerate("NESW"):
        a = -math.pi / 2 + i * math.pi / 2
        d.text((cx + math.cos(a) * R * 0.8, cy + math.sin(a) * R * 0.8), lbl, font=font(60), fill=(60, 40, 30, 255), anchor="mm")
    for i in range(32):
        a = i * math.tau / 32
        d.line([(cx + math.cos(a) * R * 0.88, cy + math.sin(a) * R * 0.88), (cx + math.cos(a) * R * 0.96, cy + math.sin(a) * R * 0.96)], fill=(80, 60, 40, 255), width=3)
    wild = t * 9 * spin_speed + 2 * math.sin(t * 13)
    target = -math.pi / 2 + 0.6
    ang = lerp(wild, target + 0.05 * math.sin(t * 6) * (1 - settle), sstep(settle))
    tip = (cx + math.cos(ang) * R * 0.75, cy + math.sin(ang) * R * 0.75)
    tail = (cx - math.cos(ang) * R * 0.75, cy - math.sin(ang) * R * 0.75)
    side = (math.cos(ang + math.pi / 2) * 30, math.sin(ang + math.pi / 2) * 30)
    d.polygon([tip, (cx + side[0], cy + side[1]), tail, (cx - side[0], cy - side[1])], fill=(60, 60, 70, 255))
    d.polygon([tip, (cx + side[0], cy + side[1]), (cx - side[0], cy - side[1])], fill=col(mix((200, 50, 40, 255), GOLD, settle), 1))
    if settle > 0.5:
        glow(d, tip[0], tip[1], 120, GOLD, settle)
    d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=col(BRASS, 1))
    tpoly(d, [(cx - R * 0.6, cy - R * 0.7), (cx - R * 0.2, cy - R * 0.85), (cx - R * 0.75, cy - R * 0.1)], col(WHITE, 0.15))


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # macro: the needle spinning wildly — then a sharp pull up to the crossroads far below
    if p < 0.55:
        compass_close(d, t)
    else:
        u = (p - 0.55) / 0.45
        cam = PCam(0, lerp(900, -600, sstep(u)), lerp(500, 1500, sstep(u)), f=900, horizon=H * lerp(0.2, 0.32, u))
        plain(d, cam, t)
        traveler(d, cam, t, spin=t * 2)
        overlay(d, (255, 230, 200), 1 - ramp(u, 0, 0.3))


def s1_noise(d, t, dur):
    p = t / dur
    cam = PCam(200 * math.sin(t * 0.4), -600 + 200 * p, 1500, horizon=H * 0.32)
    plain(d, cam, t)
    noise_ring(d, cam, t, a=ramp(t, 0.2, 0.8))
    traveler(d, cam, t, spin=t * 3)


def s2_directions(d, t, dur):
    p = t / dur
    # the camera orbits low; the traveler turns and turns; cut-ins of the spinning needle
    if (p * 3) % 1 < 0.35:
        compass_close(d, t, spin_speed=1.6)
    else:
        ang = t * 0.6
        cam = PCam(math.sin(ang) * 500, -300, 900, horizon=H * 0.36)
        plain(d, cam, t)
        noise_ring(d, cam, t)
        traveler(d, cam, t, spin=t * 5)
    top_caption(d, ["TOO MANY DIRECTIONS…"], t, dur, accent={"DIRECTIONS…"})


def s3_own(d, t, dur):
    p = t / dur
    # eyes closed, still. The noise fades; the needle settles; one road lights; the traveler walks it
    fade = sstep(ramp(p, 0.1, 0.35))
    settle = sstep(ramp(p, 0.3, 0.2))
    lit = sstep(ramp(p, 0.45, 0.2))
    walk = sstep(ramp(p, 0.6, 0.4)) * 0.9
    if 0.28 < p < 0.48:
        compass_close(d, t, settle=settle)
    else:
        cam = PCam(0, lerp(-500, -100, p) + walk * 1500 * math.sin(ROADS[TRUE_ROAD]), lerp(1500, 900, sstep(p)), horizon=H * 0.32)
        cam.x = walk * 3000 * math.cos(ROADS[TRUE_ROAD]) * 0.6
        plain(d, cam, t, lit=lit)
        noise_ring(d, cam, t, a=1 - fade, shout=fade < 0.5)
        traveler(d, cam, t, still=walk <= 0, walk=walk)
    top_caption(d, ["CAN MAKE YOU", "FORGET YOUR OWN."], t, dur, accent={"FORGET", "OWN."})


def s4_end(d, t, dur):
    a = ROADS[TRUE_ROAD]
    walk = 0.9 + 0.02 * t
    cam = PCam(walk * 3000 * math.cos(a) * 0.6, -100 + walk * 1500 * math.sin(a), 900, horizon=H * 0.32)
    plain(d, cam, t, lit=1.0)
    traveler(d, cam, t, walk=walk)
    stage_end(d, t, dur, ["FIND YOUR OWN", "DIRECTION."], [WHITE, GOLD], size=110, dim=0.45, glow_col=GOLD, y=H * 0.62)


SCENES = [s0_hook, s1_noise, s2_directions, s3_own, s4_end, s_follow]
