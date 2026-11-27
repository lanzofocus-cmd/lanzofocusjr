"""THE ANVIL OF FAILURE — told from the point of view of the metal being struck.

World: a black smithy lit only by molten orange. THE METAL is a glowing ingot with two eyes, squeezing them shut
at every blow; THE HAMMER comes down in slow motion; THE SMITH is a huge backlit silhouette. Strike by strike the
ingot curves and opens; a hiss of steam in the quench; and what comes out is a golden bell that rings out from a
tower at dawn.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, dust, sun)
from kit import s_follow

TITLE = ("THE ANVIL", "OF FAILURE")
OUTPUT = "131_The_Anvil_Of_Failure_16x9.mp4"
LINES = [
    "",
    "",
    "Some things aren't being destroyed.",
    "They're being shaped.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.4, 4: 3.6}
GAPS = {2: 2.0, 3: 6.2}

MOLTEN = (255, 140, 40, 255)
HOT = (255, 200, 110, 255)
GOLD = (240, 190, 90, 255)
SMITH = (24, 16, 14, 255)


def smithy(d, cam, t, heat=1.0):
    d.rectangle([0, 0, W, H], fill=(8, 5, 4, 255))
    fx, fy = cam.p(-900, -300)
    glow(d, fx, fy, cam.s(1400), MOLTEN, 0.5 * heat)   # the forge glow off to the side
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=(16, 10, 8, 255))
    # anvil
    d.polygon([cam.p(-360, -260), cam.p(420, -260), cam.p(300, -190), cam.p(-240, -190)], fill=(50, 50, 58, 255))
    d.rectangle(cam.box(-120, -190, 120, -40), fill=(42, 42, 50, 255))
    d.rectangle(cam.box(-240, -40, 240, 0), fill=(36, 36, 44, 255))
    d.line([cam.p(-360, -260), cam.p(420, -260)], fill=col(MOLTEN, 0.4 * heat), width=max(1, int(cam.s(6))))


def metal(d, cam, t, shape=0.0, wince=0.0, glowk=1.0, cool=0.0):
    """The ingot, morphing toward a bell as shape goes 0 -> 1; it has eyes until it cools."""
    cx, cy = cam.p(0, -262)
    c = mix(mix(MOLTEN, HOT, 0.5 * glowk), GOLD, cool)
    w0, h0 = cam.s(220), cam.s(70)
    # interpolate an ingot outline into a bell silhouette
    ingot = [(-1, 0), (-1, -1), (1, -1), (1, 0)]
    bell = [(-1.25, 0), (-0.55, -2.4), (0.55, -2.4), (1.25, 0)]
    pts = []
    for (ax, ay), (bx, by) in zip(ingot, bell):
        x, y = lerp(ax, bx, shape), lerp(ay, by, shape)
        pts.append((cx + x * w0, cy + y * h0))
    if shape > 0.3:  # rounded crown and a flared lip
        crown = (cx, cy - h0 * lerp(1, 2.9, shape))
        pts = [pts[0], pts[1], crown, pts[2], pts[3]]
    if glowk > 0:
        glow(d, cx, cy - h0, w0 * 2.5, MOLTEN, 0.7 * glowk * (1 - cool))
    d.polygon(pts, fill=col(c, 1))
    if cool > 0.5:
        tpoly(d, [(cx - w0 * 0.5, cy - h0 * 2), (cx - w0 * 0.3, cy - h0 * 2.2), (cx - w0 * 0.7, cy - h0 * 0.3)], col(WHITE, 0.3))
    if cool < 0.9:  # eyes
        ey = cy - h0 * lerp(0.55, 1.4, shape)
        er = max(2, cam.s(10))
        for o in (-1, 1):
            ex = cx + o * w0 * 0.3
            if wince > 0.5:
                d.line([(ex - er * 1.4, ey - er * 0.4 * o * 0), (ex + er * 1.4, ey)], fill=(80, 30, 10, int(255 * (1 - cool))), width=max(2, int(er * 0.7)))
            else:
                d.ellipse([ex - er, ey - er * 1.3, ex + er, ey + er * 1.3], fill=(80, 30, 10, int(255 * (1 - cool))))


def hammer(d, cam, k):
    """k: 0 raised .. 1 on the metal."""
    hx, hy = cam.p(60, lerp(-900, -330, k ** 2))
    d.rectangle([hx - cam.s(110), hy - cam.s(90), hx + cam.s(110), hy], fill=(80, 80, 90, 255))
    d.line([(hx + cam.s(40), hy - cam.s(45)), (hx + cam.s(500), hy - cam.s(380))], fill=(90, 60, 40, 255), width=max(2, int(cam.s(30))))


def smith(d, cam, t, swing):
    fx, fy = cam.p(700, 0)
    h = cam.s(1100)
    figure(d, fx, fy, h, SMITH, mode="stand", face=-1, acc=("hair",), bodyw=1.6, eyes=False,
           hands=((fx - h * 0.32, fy - h * lerp(0.95, 0.42, swing)), (fx - h * 0.28, fy - h * lerp(0.9, 0.4, swing))))


def strike_cycle(t, period=1.1, phase=0.0):
    u = ((t + phase) / period) % 1
    down = clamp((u - 0.6) / 0.15)
    hit = pulse(u, 0.75, 0.05)
    return down if u < 0.75 else 1 - clamp((u - 0.75) / 0.25), hit


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # extreme slow motion: the hammer descends on the glowing metal; sparks bloom; the metal screws its eyes shut
    cam = Cam(0, -300, 2.4)
    k = sstep(clamp(t / 1.6))
    hit = pulse(t, 1.6, 0.08)
    shake(cam, t, 20 * hit)
    smithy(d, cam, t)
    metal(d, cam, t, wince=1.0 if t > 1.2 else 0.0)
    hammer(d, cam, k if t < 1.6 else 1 - ramp(t, 1.8, 1.0))
    particles(d, *cam.p(0, -330), cam.s(700), ramp(t, 1.6, 1.4), HOT, n=80, seed=2, rise=0.5, size=5)
    darkness(d, W / 2, H / 2, 0.4)


def s1_strikes(d, t, dur):
    p = t / dur
    # blow after blow; each time the metal flinches, sure it's being destroyed
    cam = cam_lerp((150, -500, 0.9), (200, -520, 0.8), p)
    down, hit = strike_cycle(t)
    shake(cam, t, 10 * hit)
    smithy(d, cam, t)
    smith(d, cam, t, down)
    metal(d, cam, t, shape=0.25 * p, wince=1.0 if down > 0.6 else 0.0)
    hammer(d, cam, down)
    if hit > 0:
        particles(d, *cam.p(0, -330), cam.s(500), 0.4, HOT, n=40, seed=int(t), rise=0.5, size=4)


def s2_destroyed(d, t, dur):
    p = t / dur
    # close: the metal opens one eye between blows... and sees its own shape changing
    cam = cam_lerp((0, -380, 1.6), (0, -400, 1.4), p)
    down, hit = strike_cycle(t, period=1.4)
    shake(cam, t, 8 * hit)
    smithy(d, cam, t)
    metal(d, cam, t, shape=lerp(0.25, 0.7, p), wince=1.0 if down > 0.6 else 0.0)
    hammer(d, cam, down)
    if hit > 0:
        particles(d, *cam.p(0, -330), cam.s(400), 0.4, HOT, n=30, seed=int(t), rise=0.5, size=4)
    top_caption(d, ["SOME THINGS AREN'T", "BEING DESTROYED."], t, dur, accent={"DESTROYED."})


def s3_shaped(d, t, dur):
    p = t / dur
    # final blows; a plunge into the quench (steam); then it hangs in a tower at dawn — a bell — and rings
    if p < 0.4:
        u = p / 0.4
        cam = Cam(0, -420, 1.2)
        smithy(d, cam, t, heat=1 - 0.5 * u)
        metal(d, cam, t, shape=lerp(0.7, 1.0, u), cool=sstep(ramp(u, 0.6, 0.4)), glowk=1 - u)
        if u > 0.55:
            for j in range(10):  # steam
                v = ((t * 0.8 + j / 10) % 1)
                sx, sy = cam.p(-200 + j * 45, -400 - v * 700)
                rr = cam.s(60 + 120 * v)
                tpoly(d, [(sx - rr, sy - rr), (sx + rr, sy + rr)], col((220, 220, 230, 255), 0.35 * (1 - v)), kind="ellipse")
    else:
        u = (p - 0.4) / 0.6
        cam = Cam(0, -900, lerp(1.0, 0.6, sstep(u)))
        draw_sky(d, (90, 120, 190, 255), (255, 190, 140, 255))
        sun(d, W * 0.75, H * 0.65, 90, 1.0, (255, 220, 160, 255))
        # bell tower arch
        d.rectangle(cam.box(-600, -1600, -450, 600), fill=(70, 56, 60, 255))
        d.rectangle(cam.box(450, -1600, 600, 600), fill=(70, 56, 60, 255))
        d.chord(cam.box(-600, -2000, 600, -1200), 180, 360, fill=(70, 56, 60, 255))
        d.line([cam.p(-450, -1300), cam.p(450, -1300)], fill=(60, 44, 40, 255), width=max(2, int(cam.s(40))))
        swing = math.sin(t * 3) * 0.25
        bx, by = cam.p(0, -1300)
        L = cam.s(500)
        cx, cy = bx + math.sin(swing) * L, by + math.cos(swing) * L
        d.line([(bx, by), (bx + math.sin(swing) * cam.s(80), by + math.cos(swing) * cam.s(80))], fill=(60, 44, 40, 255), width=max(2, int(cam.s(20))))
        w0, h0 = cam.s(260), cam.s(380)
        pts = [(cx - w0, cy), (cx - w0 * 0.45, cy - h0 * 0.85), (cx, cy - h0), (cx + w0 * 0.45, cy - h0 * 0.85), (cx + w0, cy)]
        d.polygon(pts, fill=col(GOLD, 1))
        tpoly(d, [(cx - w0 * 0.5, cy - h0 * 0.8), (cx - w0 * 0.3, cy - h0 * 0.85), (cx - w0 * 0.7, cy - h0 * 0.1)], col(WHITE, 0.35))
        for k in range(3):  # sound rings
            v = ((t * 0.9 + k / 3) % 1)
            rr = cam.s(300 + 900 * v)
            d.ellipse([cx - rr, cy - h0 / 2 - rr * 0.6, cx + rr, cy - h0 / 2 + rr * 0.6], outline=col(GOLD, 0.5 * (1 - v)), width=max(2, int(cam.s(8))))
        glow(d, cx, cy - h0 / 2, cam.s(700), GOLD, 0.4)
    top_caption(d, ["THEY'RE BEING SHAPED."], t, dur, accent={"SHAPED."})


def s4_end(d, t, dur):
    cam = Cam(0, -900, 0.6)
    draw_sky(d, (90, 120, 190, 255), (255, 190, 140, 255))
    sun(d, W * 0.75, H * 0.65, 90, 1.0, (255, 220, 160, 255))
    cx, cy = cam.p(0, -800)
    w0, h0 = cam.s(260), cam.s(380)
    d.polygon([(cx - w0, cy), (cx - w0 * 0.45, cy - h0 * 0.85), (cx, cy - h0), (cx + w0 * 0.45, cy - h0 * 0.85), (cx + w0, cy)], fill=col(GOLD, 1))
    glow(d, cx, cy - h0 / 2, cam.s(800), GOLD, 0.5)
    stage_end(d, t, dur, ["YOU'RE BEING SHAPED."], [GOLD], size=110, dim=0.4, glow_col=GOLD, y=H * 0.78)


SCENES = [s0_hook, s1_strikes, s2_destroyed, s3_shaped, s4_end, s_follow]
