"""THE RIVER THAT NEVER STOPPED — seen from above: a river, a boulder, and the patience of water.

World: a top-down aerial view of a valley, unlike any other film in the set. A silver river winds across green
land dotted with tree crowns. THE ROCK, a huge boulder, crashes into its path; the water pools, the seasons turn
(green, gold, white, green), a thin channel creeps around the stone, and the river runs again, carrying a small
leaf boat, THE TRAVELER, all the way to the ocean.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, particles,
                   top_caption, final_card, stage_end, shake, snow, cloud)
from kit import s_follow

TITLE = ("THE RIVER THAT", "NEVER STOPPED")
OUTPUT = "113_The_River_That_Never_Stopped_16x9.mp4"
LINES = [
    "",
    "You don't always need to force your way through.",
    "Sometimes…",
    "You just need to keep moving.",
    "",
    "",
]
SILENT = {0: 3.2, 4: 3.4}
GAPS = {1: 2.6, 2: 3.4, 3: 5.4}

WATER = (90, 170, 230, 255)
WATER_D = (40, 100, 170, 255)
SEASONS = [(110, 160, 80), (200, 150, 60), (235, 238, 245), (120, 175, 90)]
ROCK = (0, 0)
OCEAN_X = 5200


def river_y(x):
    return 260 * math.sin(x * 0.0016) + 90 * math.sin(x * 0.0047 + 1.0)


def land(d, cam, t, season=0.0):
    i = int(season) % 4
    c = mix(SEASONS[i] + (255,), SEASONS[(i + 1) % 4] + (255,), season % 1)
    d.rectangle([0, 0, W, H], fill=c)
    r = random.Random(4)
    for k in range(260):  # tree crowns from above
        x, y = r.uniform(-3000, 6000), r.uniform(-1800, 1800)
        if abs(y - river_y(x)) < 260 or x > OCEAN_X - 200:
            continue
        sx, sy = cam.p(x, y)
        if -60 < sx < W + 60 and -60 < sy < H + 60:
            rr = cam.s(r.uniform(30, 70))
            tc = mix(dimc(c, 0.7), (250, 250, 255, 255), 0.8 if i == 2 and season % 1 < 0.7 else 0.0)
            d.ellipse([sx - rr + cam.s(10), sy - rr + cam.s(14), sx + rr + cam.s(10), sy + rr + cam.s(14)], fill=col(dimc(c, 0.5), 0.6))  # shadow
            d.ellipse([sx - rr, sy - rr, sx + rr, sy + rr], fill=tc)
    # the ocean at the far end
    ox = cam.p(OCEAN_X, 0)[0]
    if ox < W:
        d.rectangle([ox, 0, W, H], fill=(40, 110, 170, 255))
        for k in range(14):
            y = (k * 80 + t * 20) % H
            d.line([(ox + 20, y), (W, y + 10)], fill=col((150, 210, 240, 255), 0.35), width=3)
        d.rectangle([ox - cam.s(60), 0, ox, H], fill=(230, 210, 160, 255))


def path_pts(cam, x0, x1, step=40, detour=0.0):
    """Screen points along the river from x0 to x1; detour bends the channel around the rock."""
    pts = []
    x = x0
    while x <= x1:
        y = river_y(x)
        if detour > 0 and -500 < x < 500:
            y += math.cos((x / 500) * math.pi / 2) ** 2 * 420 * detour
        pts.append(cam.p(x, y))
        x += step
    return pts


def water(d, cam, t, x0, x1, width=150, detour=0.0, flow=1.0, a=1.0):
    dry = 1 - a
    a = 1.0
    pts = path_pts(cam, x0, x1, detour=detour)
    if len(pts) < 2:
        return
    w = max(2, int(cam.s(width)))
    d.line(pts, fill=mix(WATER_D, (110, 90, 60, 255), dry), width=w + max(2, int(cam.s(20))), joint="curve")
    d.line(pts, fill=mix(WATER, (150, 125, 90, 255), dry), width=w, joint="curve")
    # flow highlights travelling downstream
    n = len(pts)
    for k in range(0, n - 1, 3):
        u = ((k / n) * 8 - t * 0.9 * flow) % 1
        if u < 0.3:
            p0, p1 = pts[k], pts[min(n - 1, k + 1)]
            if dry < 0.5:
                d.line([p0, p1], fill=col((220, 240, 255, 255), 0.7), width=max(1, int(cam.s(8))))


def rock(d, cam, t, drop=1.0):
    sx, sy = cam.p(*ROCK)
    if drop < 1:  # falling: shadow grows, rock shrinks from above
        sh = cam.s(260) * (0.3 + 0.7 * drop)
        tpoly(d, [(sx - sh, sy - sh * 0.8), (sx + sh, sy + sh * 0.8)], col((0, 0, 0, 255), 0.35 * drop), kind="ellipse")
        s = cam.s(260) * lerp(2.2, 1.0, drop)
        oy = -(1 - drop) * cam.s(500)
    else:
        s = cam.s(260)
        oy = 0
    r = random.Random(1)
    pts = [(sx + math.cos(a) * s * r.uniform(0.85, 1.1), sy + oy + math.sin(a) * s * 0.85 * r.uniform(0.85, 1.1)) for a in [k * math.tau / 11 for k in range(11)]]
    d.polygon(pts, fill=(120, 116, 112, 255))
    d.polygon([(p[0] * 0.6 + sx * 0.4 - s * 0.15, p[1] * 0.6 + (sy + oy) * 0.4 - s * 0.2) for p in pts], fill=(160, 156, 150, 255))
    d.text((sx, sy + oy + s * 1.15), "THE ROCK", font=font(int(clamp(cam.s(40), 14, 40))), fill=col(WHITE, 0.85), anchor="mm")


def pool(d, cam, k):
    """Water backing up behind the rock."""
    if k <= 0:
        return
    sx, sy = cam.p(-320, river_y(-320))
    rx, ry = cam.s(200 + 340 * k), cam.s(150 + 220 * k)
    d.ellipse([sx - rx, sy - ry, sx + rx * 0.7, sy + ry], fill=WATER_D)
    d.ellipse([sx - rx + cam.s(12), sy - ry + cam.s(12), sx + rx * 0.7 - cam.s(12), sy + ry - cam.s(12)], fill=WATER)


def leaf_boat(d, cam, x, t, detour=1.0):
    y = river_y(x)
    if -500 < x < 500:
        y += math.cos((x / 500) * math.pi / 2) ** 2 * 420 * detour
    sx, sy = cam.p(x, y)
    ang = math.atan2(river_y(x + 10) - river_y(x), 10)
    s = cam.s(60)
    pts = [(sx + math.cos(ang) * s, sy + math.sin(ang) * s), (sx - math.sin(ang) * s * 0.35, sy + math.cos(ang) * s * 0.35),
           (sx - math.cos(ang) * s, sy - math.sin(ang) * s), (sx + math.sin(ang) * s * 0.35, sy - math.cos(ang) * s * 0.35)]
    d.polygon(pts, fill=(240, 160, 60, 255))
    d.line([pts[0], pts[2]], fill=(170, 100, 30, 255), width=max(1, int(s * 0.08)))
    d.ellipse([sx - s * 0.18, sy - s * 0.18, sx + s * 0.18, sy + s * 0.18], fill=(250, 245, 235, 255))  # the traveler, from above
    d.text((sx, sy - s * 1.1), "THE TRAVELER", font=font(int(clamp(s * 0.4, 12, 30))), fill=col(WHITE, 0.85), anchor="mm")


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # falling through clouds onto a silver river winding through the valley
    cam = cam_lerp((-1600, 0, 0.18), (-700, 0, 0.42), sstep(p))
    land(d, cam, t)
    water(d, cam, t, -4000, OCEAN_X)
    for j in range(6):
        k = clamp(1 - p * 1.6 + j * 0.05)
        if k > 0:
            fog(d, W * (0.15 + 0.15 * j), H * (0.3 + 0.1 * (j % 3)), 1800 * (1 + (1 - k)), 0.8 * k)


def s1_force(d, t, dur):
    p = t / dur
    # a boulder crashes into the river; the water stops, piles up and pushes, but cannot move it
    cam = cam_lerp((-500, 0, 0.6), (-300, 50, 0.7), sstep(p))
    drop = sstep(ramp(t, 0.2, 0.5))
    hit = pulse(t, 0.7, 0.15)
    shake(cam, t, 20 * hit)
    land(d, cam, t)
    blocked = drop >= 1
    water(d, cam, t, -4000, -150 if blocked else OCEAN_X)
    if blocked:
        water(d, cam, t, 250, OCEAN_X, width=150, a=1 - sstep(ramp(t, 0.8, 1.2)))  # downstream drains away
    pool(d, cam, sstep(ramp(t, 0.8, dur * 0.7)))
    rock(d, cam, t, drop)
    if hit > 0:
        particles(d, *cam.p(*ROCK), cam.s(500), ramp(t, 0.7, 0.8), (230, 245, 255), n=60, seed=2, rise=0.0, size=6)
    top_caption(d, ["YOU DON'T ALWAYS NEED TO", "FORCE YOUR WAY THROUGH."], t, dur, accent={"FORCE"})


def s2_sometimes(d, t, dur):
    p = t / dur
    # the seasons turn over the stand-off; a thin new channel creeps around the stone
    cam = cam_lerp((-300, 50, 0.7), (0, 150, 0.6), p)
    season = 4 * sstep(p) * 0.99
    land(d, cam, t, season)
    water(d, cam, t, -4000, -150)
    pool(d, cam, 1.0)
    # the trickle: drawn along the detour, growing in length
    pts = path_pts(cam, -500, lerp(-500, 520, sstep(ramp(p, 0.4, 0.6))), detour=1.0)
    if len(pts) > 1:
        d.line(pts, fill=WATER, width=max(2, int(cam.s(30))), joint="curve")
    rock(d, cam, t)
    if 2 <= season < 3:
        snow(d, t, 0.9, n=120)
    names = ["SPRING", "AUTUMN", "WINTER", "SPRING"]
    d.text((W - 120, H - 100), names[int(season) % 4], font=font(30), fill=col(WHITE, 0.8), anchor="rm")
    top_caption(d, ["SOMETIMES…"], t, dur, accent={"SOMETIMES…"})


def s3_moving(d, t, dur):
    p = t / dur
    # the channel widens, the river runs again; follow the leaf boat around the rock and down to the sea
    widen = sstep(ramp(p, 0.0, 0.3))
    bx = lerp(-1400, OCEAN_X - 300, sstep(ramp(p, 0.15, 0.85)))
    cam = Cam(bx + 300, river_y(bx) * 0.7, lerp(0.6, 0.5, p))
    land(d, cam, t, 3.99)
    water(d, cam, t, -4000, -400)
    pool(d, cam, 1 - widen)
    water(d, cam, t, -520, 520, width=lerp(30, 150, widen), detour=1.0)
    water(d, cam, t, 400, OCEAN_X, a=widen)
    rock(d, cam, t)
    leaf_boat(d, cam, bx, t)
    top_caption(d, ["YOU JUST NEED TO", "KEEP MOVING."], t, dur, accent={"KEEP", "MOVING."})


def s4_end(d, t, dur):
    cam = Cam(OCEAN_X - 200, 0, 0.5)
    land(d, cam, t, 3.99)
    water(d, cam, t, 400, OCEAN_X)
    leaf_boat(d, cam, OCEAN_X - 150 + 60 * t, t)
    stage_end(d, t, dur, ["KEEP MOVING."], [WATER], size=130, dim=0.45, glow_col=WATER)


SCENES = [s0_hook, s1_force, s2_sometimes, s3_moving, s4_end, s_follow]
