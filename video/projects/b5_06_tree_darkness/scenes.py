"""THE TREE THAT GREW IN DARKNESS — a seed's long, unseen journey under the ground.

World: a cross-section of the earth in warm browns and charcoal: soil layers, buried rocks, roots that glow
faintly green as they grow. Above ground, a grey street where people walk past unaware; a STORM rolls in, the
shoot breaks the surface, and a great tree grows in time-lapse as THE SUN comes out.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, rain, flash, bolt, sun, cloud, dust)
from kit import s_follow

TITLE = ("THE TREE THAT", "GREW IN DARKNESS")
OUTPUT = "106_The_Tree_That_Grew_In_Darkness_16x9.mp4"
LINES = [
    "",
    "Nobody sees the beginning.",
    "Nobody applauds underground.",
    "But that's where the roots are built.",
    "",
    "",
    "",
]
SILENT = {0: 3.0, 4: 4.8, 5: 3.4}
GAPS = {1: 1.4, 2: 1.8, 3: 2.2}

SEED = (150, 255, 160, 255)
ROOT = (120, 200, 120, 255)
SOIL = [(60, 40, 28), (48, 32, 24), (38, 26, 22), (28, 20, 18)]
CH = 150
SEED_Y = 700  # depth of the seed below the surface (y=0)

# ---------------------------------------------------------------- the root system, generated once
_r = random.Random(11)
ROOTS = []  # (x0, y0, x1, y1, birth 0..1, width)


def _grow(x, y, ang, length, depth, birth, width):
    if depth > 6 or length < 30:
        return
    n = 4
    for k in range(n):
        ang += _r.uniform(-0.25, 0.25)
        nx, ny = x + math.cos(ang) * length / n, y + math.sin(ang) * length / n
        b = birth + (k + 1) / n * 0.09
        ROOTS.append((x, y, nx, ny, min(1.0, b), width))
        x, y = nx, ny
        birth = b
    for s in (-1, 1):
        if _r.random() < 0.85:
            _grow(x, y, ang + s * _r.uniform(0.4, 0.9), length * 0.72, depth + 1, birth, width * 0.7)


_grow(0, SEED_Y, math.pi / 2, 760, 0, 0.0, 22)
for a in (math.pi * 0.25, math.pi * 0.75):
    _grow(0, SEED_Y, a, 680, 1, 0.08, 16)
ROCKS = [(-380, 1150, 160), (320, 1000, 130), (-120, 1500, 190), (520, 1450, 150), (-600, 820, 110)]


def underground(d, cam, t, g=0.0, glowk=1.0, light=1.0):
    # soil layers
    gy = cam.p(0, 0)[1]
    for i, c in enumerate(SOIL):
        y0 = cam.p(0, i * 600)[1]
        y1 = cam.p(0, (i + 1) * 600)[1] if i < 3 else H
        if y1 > 0 and y0 < H:
            d.rectangle([0, max(0, y0), W, min(H, y1)], fill=c + (255,))
    r = random.Random(3)
    for i in range(160):  # pebbles
        x, y = r.uniform(-2000, 2000), r.uniform(40, 2400)
        sx, sy = cam.p(x, y)
        if 0 < sx < W and 0 < sy < H:
            rr = cam.s(r.uniform(4, 12))
            d.ellipse([sx - rr, sy - rr * 0.7, sx + rr, sy + rr * 0.7], fill=col((90, 70, 56, 255), 0.7 * light))
    # rocks (cracking when roots reach them)
    for i, (x, y, rr) in enumerate(ROCKS):
        pts = [cam.p(x + math.cos(a) * rr * (1 + 0.2 * math.sin(a * 3 + i)), y + math.sin(a) * rr * 0.7) for a in [k * math.tau / 9 for k in range(9)]]
        d.polygon(pts, fill=col((80, 74, 70, 255), light))
        polyline(d, pts + [pts[0]], 1, col((120, 110, 100, 255), light), max(1, int(cam.s(4))))
        crack = clamp((g - 0.35 - i * 0.07) * 4)
        if crack > 0:
            cx, cy = cam.p(x, y)
            polyline(d, [(cx - cam.s(rr * 0.6), cy - cam.s(10)), (cx - cam.s(10), cy + cam.s(15)), (cx + cam.s(20), cy - cam.s(20)), (cx + cam.s(rr * 0.6), cy + cam.s(10))],
                     crack, col((20, 16, 14, 255), 1), max(2, int(cam.s(6))))
    # roots
    for (x0, y0, x1, y1, b, w) in ROOTS:
        b = b * 0.85
        if b > g + 0.12:
            continue
        k = clamp((g - (b - 0.12)) / 0.12)
        ex, ey = lerp(x0, x1, k), lerp(y0, y1, k)
        p0, p1 = cam.p(x0, y0), cam.p(ex, ey)
        d.line([p0, p1], fill=col(mix((90, 70, 50, 255), ROOT, glowk * 0.7), 1), width=max(1, int(cam.s(w))))
        if k < 1 and glowk > 0:
            glow(d, p1[0], p1[1], cam.s(60), SEED, 0.6 * glowk)
    # the seed
    sx, sy = cam.p(0, SEED_Y)
    pulse_k = 0.7 + 0.3 * math.sin(t * 4)
    glow(d, sx, sy, cam.s(220), SEED, 0.6 * pulse_k * glowk)
    d.ellipse([sx - cam.s(30), sy - cam.s(20), sx + cam.s(30), sy + cam.s(20)], fill=col((180, 140, 80, 255), 1))
    if g > 0.02:  # split shell
        d.line([(sx - cam.s(26), sy), (sx + cam.s(26), sy)], fill=col(SEED, 1), width=max(1, int(cam.s(4))))


def shoot(d, cam, k, t):
    """The stem climbing from the seed to the surface (k 0..1) and beyond."""
    if k <= 0:
        return
    top = lerp(SEED_Y, -40, clamp(k))
    pts = [cam.p(math.sin(y * 0.01) * 30, y) for y in [lerp(SEED_Y, top, i / 12) for i in range(13)]]
    polyline(d, pts, 1, col((140, 220, 110, 255), 1), max(2, int(cam.s(14))))
    glow(d, pts[-1][0], pts[-1][1], cam.s(80), SEED, 0.7)


def surface(d, cam, t, storm=0.0, sunny=0.0, walkers=True):
    gy = cam.p(0, 0)[1]
    if gy <= 0:
        return
    draw_sky(d, mix(mix((60, 64, 80, 255), (30, 32, 44, 255), storm), (100, 170, 230, 255), sunny),
             mix(mix((150, 150, 160, 255), (70, 72, 84, 255), storm), (255, 225, 180, 255), sunny), h=int(min(H, max(2, gy))))
    if sunny > 0.05:
        sun(d, W * 0.78, gy * 0.4, 70, sunny, (255, 230, 170, 255))
    if storm > 0:
        for j in range(5):
            cloud(d, j * 420 + 80, gy * 0.25 + 30 * (j % 2), 110, col((120, 122, 136, 255), storm), w=8)
    # street and passers-by
    d.rectangle([0, gy - cam.s(14), W, gy], fill=(90, 90, 96, 255))
    if walkers:
        for j, (x0, v) in enumerate(((-1500, 260), (900, -220), (-300, 180))):
            x = x0 + v * t
            fx, fy = cam.p(x, -14)
            figure(d, fx, fy, cam.s(CH), (120, 120, 130, 255), mode="walk", phase=t * 5 + j, face=1 if v > 0 else -1, acc=("hair",), look=0.0)


def tree(d, cam, k, t):
    """Time-lapse tree from sapling (k=0) to giant (k=1), standing at x=0 on the surface."""
    if k <= 0:
        return
    hgt = lerp(60, 1300, k)
    trunk_w = lerp(10, 120, k)
    base = cam.p(0, 0)
    topp = cam.p(0, -hgt * 0.55)
    d.polygon([(base[0] - cam.s(trunk_w), base[1]), (base[0] + cam.s(trunk_w), base[1]), (topp[0] + cam.s(trunk_w * 0.4), topp[1]), (topp[0] - cam.s(trunk_w * 0.4), topp[1])],
              fill=(90, 62, 44, 255))
    r = random.Random(5)
    for i in range(7):  # branches
        bk = clamp(k * 1.5 - i * 0.08)
        if bk <= 0:
            continue
        y = -hgt * (0.35 + 0.08 * i)
        s = -1 if i % 2 else 1
        p0 = cam.p(0, y)
        p1 = cam.p(s * hgt * 0.35 * bk, y - hgt * 0.15 * bk)
        d.line([p0, p1], fill=(90, 62, 44, 255), width=max(2, int(cam.s(trunk_w * 0.3))))
    for i in range(16):  # canopy
        ck = clamp(k * 1.4 - 0.15 - i * 0.02)
        if ck <= 0:
            continue
        a = r.uniform(0, math.tau)
        dist = r.uniform(0, hgt * 0.32)
        cx, cy = math.cos(a) * dist, -hgt * 0.72 + math.sin(a) * dist * 0.6
        rr = hgt * r.uniform(0.14, 0.22) * ck
        sx, sy = cam.p(cx, cy)
        c = mix((60, 130, 70, 255), (120, 200, 110, 255), r.random())
        d.ellipse([sx - cam.s(rr), sy - cam.s(rr * 0.85), sx + cam.s(rr), sy + cam.s(rr * 0.85)], fill=c)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # dive from the grey street straight down through the soil to one glowing seed
    cam = cam_lerp((0, -300, 0.6), (0, SEED_Y, 1.4), sstep(p))
    underground(d, cam, t, g=0.0)
    surface(d, cam, t)
    darkness(d, W / 2, H / 2, 0.5 * p)


def s1_beginning(d, t, dur):
    p = t / dur
    # split screen in one shot: people walking above, the seed cracking open below
    cam = cam_lerp((0, SEED_Y - 300, 0.85), (0, SEED_Y - 200, 0.7), sstep(p))
    underground(d, cam, t, g=0.12 * p)
    surface(d, cam, t)
    top_caption(d, ["NOBODY SEES", "THE BEGINNING."], t, dur, accent={"NOBODY", "BEGINNING."})


def s2_underground(d, t, dur):
    p = t / dur
    # roots push down and around the rocks, cracking them
    cam = cam_lerp((0, SEED_Y + 300, 0.6), (100, SEED_Y + 500, 0.45), sstep(p))
    underground(d, cam, t, g=lerp(0.12, 0.7, p))
    for i, (x, y, rr) in enumerate(ROCKS):
        if 0 < (lerp(0.12, 0.7, p) - 0.35 - i * 0.07) * 4 < 1:
            particles(d, *cam.p(x, y), cam.s(rr), clamp((lerp(0.12, 0.7, p) - 0.35 - i * 0.07) * 4), (140, 120, 100), n=18, seed=i, rise=0.0)
    top_caption(d, ["NOBODY APPLAUDS", "UNDERGROUND."], t, dur, accent={"APPLAUDS", "UNDERGROUND."})


def s3_roots(d, t, dur):
    p = t / dur
    # the whole network lights up; a stem starts climbing toward a stormy surface
    cam = cam_lerp((100, SEED_Y + 500, 0.45), (0, SEED_Y - 250, 0.42), sstep(p))
    fl = pulse(t, dur * 0.6, 0.1)
    underground(d, cam, t, g=lerp(0.7, 1.0, p), glowk=1 + p)
    shoot(d, cam, sstep(ramp(p, 0.3, 0.7)) * 0.95, t)
    surface(d, cam, t, storm=1.0, walkers=False)
    gy = cam.p(0, 0)[1]
    if gy > 0:
        if fl > 0:
            bolt(d, W * 0.7, gy * 0.15, fl, 0.6)
    flash(d, fl)
    top_caption(d, ["BUT THAT'S WHERE", "THE ROOTS ARE BUILT."], t, dur, accent={"ROOTS"})


def s4_grow(d, t, dur):
    p = t / dur
    # breakthrough; the storm clears; a great tree grows in time-lapse; the camera rises and pulls back,
    # keeping the roots visible underneath like the tree's real foundation
    k = sstep(ramp(p, 0.1, 0.8))
    cam = cam_lerp((0, -100, 0.75), (0, -300, 0.32), sstep(p))
    underground(d, cam, t, g=1.0, glowk=1.2)
    surface(d, cam, t, storm=1 - k, sunny=k, walkers=False)
    shoot(d, cam, 1.0, t)
    tree(d, cam, k, t)
    if p < 0.12:
        particles(d, *cam.p(0, -10), cam.s(200), p / 0.12, (120, 90, 60), n=30, seed=2, rise=1.0)
    dust(d, t, 0.6 * k, n=50, color=(255, 240, 180))


def s5_end(d, t, dur):
    cam = Cam(0, -300, 0.32)
    underground(d, cam, t, g=1.0, glowk=1.2)
    surface(d, cam, t, sunny=1.0, walkers=False)
    tree(d, cam, 1.0, t)
    stage_end(d, t, dur, ["BUILD YOUR ROOTS."], [(180, 255, 170, 255)], size=120, dim=0.45, glow_col=SEED, y=H * 0.5)


SCENES = [s0_hook, s1_beginning, s2_underground, s3_roots, s4_grow, s5_end, s_follow]
