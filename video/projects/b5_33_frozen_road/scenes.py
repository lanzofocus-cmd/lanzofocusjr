"""THE FROZEN ROAD — a road sealed under ice that only opens once you walk on it.

World: a blue-white frozen valley in a blizzard; the road ahead is buried under a thick sheet of ice. THE TRAVELER
(red coat) tests it with a boot. The first step cracks the ice and warm gold light leaks out of the cracks; every
step melts a footprint, and behind the traveler the road thaws into stone, grass and flowers while the snow thins
and a low sun comes out.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, snow, sun)
from kit import s_follow

TITLE = ("THE FROZEN", "ROAD")
OUTPUT = "133_The_Frozen_Road_16x9.mp4"
LINES = [
    "",
    "",
    "Sometimes the road doesn't open…",
    "Until you start walking.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.0, 4: 3.4}
GAPS = {2: 2.2, 3: 6.2}

ICE = (190, 220, 245, 255)
ICE_D = (120, 160, 200, 255)
WARM = (255, 200, 120, 255)
COAT = (220, 60, 60, 255)
CH = 220


def valley(d, cam, t, thaw_x=-9999, spring=0.0):
    draw_sky(d, mix((150, 170, 200, 255), (110, 160, 230, 255), spring), mix((230, 236, 245, 255), (255, 220, 180, 255), spring))
    if spring > 0.05:
        sun(d, W * 0.8, cam.p(0, 0)[1] - cam.s(400), 70, spring, (255, 230, 170, 255))
    for f, c in ((0.3, (200, 210, 225)), (0.55, (170, 185, 205))):
        pts = []
        for i in range(30):
            x = -6000 + i * 450
            y = -120 - 260 * abs(math.sin(i * 0.9 + f * 3)) - 120 * abs(math.sin(i * 0.37))
            zz = cam.z * (0.5 + 0.5 * f)
            pts.append(((x - cam.cx * f) * zz + W / 2, (y - cam.cy * f) * zz + H / 2))
        pts += [(W + 10, H + 10), (-10, H + 10)]
        d.polygon(pts, fill=mix(c + (255,), (120, 160, 120, 255), spring * 0.6))
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=mix((235, 240, 248, 255), (150, 190, 120, 255), spring * 0.6))
    # the road: ice ahead, thawed stone behind the traveler
    for x in range(-4000, 8000, 100):
        p0, p1 = cam.p(x, 0), cam.p(x + 100, 60)
        if p1[0] < 0 or p0[0] > W:
            continue
        thawed = x < thaw_x
        c = (150, 130, 110, 255) if thawed else ICE
        d.rectangle([p0[0], p0[1], p1[0], p1[1]], fill=c)
        if not thawed:
            d.line([(p0[0], p0[1] + cam.s(10)), (p1[0], p0[1] + cam.s(14))], fill=col(WHITE, 0.6), width=max(1, int(cam.s(4))))
        else:
            r = random.Random(x)
            if r.random() < 0.5 * spring:  # grass and flowers along the thawed road
                fx, fy = cam.p(x + 50, -2)
                d.line([(fx, fy), (fx, fy - cam.s(30))], fill=(80, 150, 70, 255), width=max(1, int(cam.s(4))))
                d.ellipse([fx - cam.s(8), fy - cam.s(38), fx + cam.s(8), fy - cam.s(22)], fill=r.choice([(255, 120, 150, 255), (255, 220, 90, 255)]))
    # thick ice slab edge ahead
    if thaw_x < 8000:
        a, b = cam.p(max(thaw_x, -4000), -40), cam.p(8000, 0)
        tpoly(d, [a, (b[0], a[1]), b, (a[0], b[1])], col(ICE, 0.6))


def cracks(d, cam, x, k, t, seed=1):
    """Cracks spreading from a footfall at x, with warm light leaking through."""
    if k <= 0:
        return
    r = random.Random(seed)
    cx, cy = cam.p(x, 10)
    glow(d, cx, cy, cam.s(260) * k, WARM, 0.6 * k)
    for i in range(8):
        ang = r.uniform(-math.pi, 0) if r.random() < 0.5 else r.uniform(0, math.pi)
        L = cam.s(r.uniform(120, 420)) * k
        pts = [(cx, cy)]
        x0, y0 = cx, cy
        for j in range(4):
            ang += r.uniform(-0.4, 0.4)
            x0 += math.cos(ang) * L / 4
            y0 += math.sin(ang) * L / 4 * 0.3
            pts.append((x0, y0))
        polyline(d, pts, 1, col(WARM, 0.9), max(2, int(cam.s(5))))


def traveler(d, cam, x, t, mode="walk", **kw):
    fx, fy = cam.p(x, 0)
    figure(d, fx, fy, cam.s(CH), COAT, mode=mode, phase=kw.pop("phase", x / 55), face=1, acc=("hair", "backpack"), name="THE TRAVELER", **kw)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # a whiteout; it thins to show a lone figure before a road buried in ice
    cam = cam_lerp((300, -300, 0.9), (200, -300, 0.75), p)
    valley(d, cam, t)
    traveler(d, cam, -100, t, mode="stand", look=0.2)
    snow(d, t, 1.0, n=260)
    overlay(d, (240, 244, 250), 0.9 * (1 - ramp(t, 0.2, 1.6)))


def s1_test(d, t, dur):
    p = t / dur
    # close on a boot at the ice's edge: a tap... a step back
    cam = Cam(0, -120, 2.0)
    valley(d, cam, t)
    tap = pulse(p, 0.35, 0.08) + pulse(p, 0.6, 0.08)
    traveler(d, cam, -120 + 30 * tap, t, mode="stand", look=-0.6, lean=0.1 * tap)
    snow(d, t, 0.8, n=160)


def s2_open(d, t, dur):
    p = t / dur
    # the first real step: a crack, a flare of warm light from under the ice
    step = sstep(ramp(p, 0.1, 0.25))
    x = lerp(-120, 60, step)
    cam = cam_lerp((0, -120, 2.0), (100, -250, 1.0), sstep(p))
    hit = pulse(p, 0.35, 0.06)
    shake(cam, t, 10 * hit)
    valley(d, cam, t, thaw_x=lerp(-9999, 0, ramp(p, 0.35, 0.6)) if p > 0.35 else -9999)
    cracks(d, cam, 60, ramp(p, 0.33, 0.5), t)
    traveler(d, cam, x, t, mode="walk" if 0 < step < 1 else "stand", look=-0.4)
    snow(d, t, 0.8, n=160)
    top_caption(d, ["SOMETIMES THE ROAD", "DOESN'T OPEN…"], t, dur, accent={"DOESN'T"})


def s3_walking(d, t, dur):
    p = t / dur
    # walking: each step cracks and melts the ice; behind, the road becomes spring
    x = lerp(60, 3600, sstep(ramp(p, 0.0, 0.9)))
    spring = sstep(ramp(p, 0.2, 0.7))
    cam = Cam(x + 150, -320, lerp(1.0, 0.6, sstep(p)))
    valley(d, cam, t, thaw_x=x - 40, spring=spring)
    stepn = int(x / 110)
    cracks(d, cam, stepn * 110 + 60, 0.6, t, seed=stepn)
    traveler(d, cam, x, t, mode="walk", mouth=0.6 * spring)
    snow(d, t, 0.8 * (1 - spring), n=160)
    top_caption(d, ["UNTIL YOU START", "WALKING."], t, dur, accent={"WALKING."})


def s4_end(d, t, dur):
    x = 3600 + 120 * t
    cam = Cam(x + 150, -320, 0.6)
    valley(d, cam, t, thaw_x=x - 40, spring=1.0)
    traveler(d, cam, x, t, mode="walk", mouth=0.6)
    stage_end(d, t, dur, ["START WALKING."], [WARM], size=130, dim=0.35, glow_col=WARM, y=H * 0.28)


SCENES = [s0_hook, s1_test, s2_open, s3_walking, s4_end, s_follow]
