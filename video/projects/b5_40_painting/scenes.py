"""THE PAINTING OF YOUR LIFE — a blank canvas, waiting for inspiration that only comes after the first mark.

World: a pure white minimal studio, unlike the dark worlds elsewhere: one easel, one huge blank canvas, one ARTIST
in charcoal grey with a brush. A drop of paint falls in slow motion. The artist waits; nothing happens. One small
blue dab. Then another. Then colour floods the canvas into a living landscape and spills off it, over the floor
and walls, until the whole white room has become the painting.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   final_card, stage_end, shake, dust, word_reveal)
from kit import s_follow

TITLE = ("THE PAINTING", "OF YOUR LIFE")
OUTPUT = "140_The_Painting_Of_Your_Life_16x9.mp4"
LINES = [
    "",
    "",
    "You don't need inspiration to begin.",
    "Sometimes…",
    "Beginning creates inspiration.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.0, 5: 3.4}
GAPS = {2: 1.8, 3: 1.6, 4: 5.6}

ARTIST = (60, 60, 70, 255)
PALETTE = [(40, 120, 255), (255, 80, 90), (255, 200, 40), (60, 200, 120), (180, 90, 255), (255, 140, 50)]
CANVAS = (-420, -1100, 420, -300)


def studio(d, cam, t, paint=0.0):
    d.rectangle([0, 0, W, H], fill=(246, 244, 240, 255))
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=(232, 228, 222, 255))
    d.line([(0, gy), (W, gy)], fill=(210, 205, 198, 255), width=3)
    if paint > 0:  # colour spilling over floor and walls
        r = random.Random(4)
        for i in range(60):
            k = clamp(paint * 1.6 - r.random() * 0.6)
            if k <= 0:
                continue
            x, y = r.uniform(-1800, 1800), r.uniform(-1400, 300)
            rr = r.uniform(80, 320) * k
            c = r.choice(PALETTE)
            sx, sy = cam.p(x, y)
            tpoly(d, [(sx - cam.s(rr), sy - cam.s(rr * 0.7)), (sx + cam.s(rr), sy + cam.s(rr * 0.7))], c + (int(200 * k),), kind="ellipse")


def easel(d, cam):
    x0, y0, x1, y1 = CANVAS
    for a, b in (((-350, 0), (-150, -1200)), ((350, 0), (150, -1200)), ((0, 0), (0, -1250))):
        d.line([cam.p(*a), cam.p(*b)], fill=(150, 110, 70, 255), width=max(2, int(cam.s(14))))
    d.rectangle(cam.box(x0 - 20, y1, x1 + 20, y1 + 30), fill=(150, 110, 70, 255))


def canvas(d, cam, t, marks=0, bloom=0.0):
    x0, y0, x1, y1 = CANVAS
    a, b = cam.p(x0, y0), cam.p(x1, y1)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(255, 255, 255, 255), outline=(220, 215, 205, 255), width=3)
    w, h = b[0] - a[0], b[1] - a[1]
    def P(u, v):
        return (a[0] + u * w, a[1] + v * h)
    # a few loose strokes, one by one
    r = random.Random(2)
    for i in range(int(marks)):
        u, v = r.uniform(0.15, 0.85), r.uniform(0.2, 0.8)
        c = PALETTE[i % len(PALETTE)]
        pts = [P(u + j * 0.03, v + math.sin(j + i) * 0.02) for j in range(5)]
        d.line(pts, fill=c + (255,), width=max(3, int(w * 0.03)), joint="curve")
    if bloom > 0:  # the landscape blooming across the canvas
        tpoly(d, [P(0, 0), P(1, 0), P(1, 0.6), P(0, 0.6)], (120, 180, 255, int(255 * bloom)))
        sx, sy = P(0.7, 0.25)
        d.ellipse([sx - w * 0.08 * bloom, sy - w * 0.08 * bloom, sx + w * 0.08 * bloom, sy + w * 0.08 * bloom], fill=(255, 210, 60, 255))
        hills = [P(0, 0.6), P(0.2, 0.42), P(0.45, 0.58), P(0.7, 0.38), P(1, 0.55), P(1, 1), P(0, 1)]
        tpoly(d, hills, (70, 190, 110, int(255 * bloom)))
        tpoly(d, [P(0, 0.75), P(0.3, 0.68), P(0.6, 0.8), P(1, 0.7), P(1, 1), P(0, 1)], (40, 150, 90, int(255 * bloom)))
        river = [P(0.45, 1), P(0.5, 0.85), P(0.42, 0.72), P(0.48, 0.62), P(0.52, 0.62), P(0.48, 0.72), P(0.56, 0.85), P(0.55, 1)]
        tpoly(d, river, (60, 140, 255, int(255 * bloom)))
        for k in range(6):
            fx, fy = P(0.1 + k * 0.15, 0.9)
            d.ellipse([fx - w * 0.015, fy - w * 0.015, fx + w * 0.015, fy + w * 0.015], fill=PALETTE[k % 6] + (int(255 * bloom),))


def artist(d, cam, t, mode="stand", x=-700, face=1, hands=None, **kw):
    fx, fy = cam.p(x, 0)
    h = cam.s(400)

    def brush(dd, fh, bh, hh, a):
        if fh:
            dd.line([fh, (fh[0] + face * hh * 0.12, fh[1] - hh * 0.1)], fill=(150, 110, 70, int(255 * a)), width=max(2, int(hh * 0.02)))
            dd.ellipse([fh[0] + face * hh * 0.12 - hh * 0.02, fh[1] - hh * 0.12, fh[0] + face * hh * 0.12 + hh * 0.02, fh[1] - hh * 0.08],
                       fill=PALETTE[int(t * 2) % 6] + (255,))
    figure(d, fx, fy, h, ARTIST, mode=mode, phase=t * 6, face=face, acc=("hair",), prop=brush, hands=hands, name="THE ARTIST", **kw)


def top_caption(d, lines, t, dur, accent=None):
    """Dark ink captions for the white studio (no black band)."""
    n = len(lines)
    size = 64 if n == 2 else 76
    for i, ln in enumerate(lines):
        word_reveal(d, W / 2, 110 + i * size * 1.15, ln, t - i * 0.5, 1.0, size, (40, 40, 60, 255), anchor="mm", step=0.12)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # pure white; one drop of blue paint falls in slow motion and blooms into a splash
    d.rectangle([0, 0, W, H], fill=(246, 244, 240, 255))
    y = lerp(-80, H * 0.62, sstep(clamp(t / 1.8)))
    if t < 1.8:
        d.ellipse([W / 2 - 22, y - 34, W / 2 + 22, y + 22], fill=(40, 120, 255, 255))
    else:
        k = ramp(t, 1.8, 0.8)
        d.ellipse([W / 2 - 200 * k, H * 0.62 - 30 * k, W / 2 + 200 * k, H * 0.62 + 30 * k], fill=(40, 120, 255, 255))
        r = random.Random(1)
        for i in range(14):
            ang = r.uniform(math.pi, math.tau)
            dist = 260 * k * r.uniform(0.5, 1.2)
            sx, sy = W / 2 + math.cos(ang) * dist, H * 0.62 + math.sin(ang) * dist * 0.6 + 120 * k * k
            rr = r.uniform(8, 22) * (1 - k * 0.3)
            d.ellipse([sx - rr, sy - rr, sx + rr, sy + rr], fill=(40, 120, 255, 255))


def s1_wait(d, t, dur):
    p = t / dur
    # the artist before an enormous blank canvas, brush raised... waiting; a clock ticks on the wall
    cam = Cam(-150, -620, 0.7)
    studio(d, cam, t)
    easel(d, cam)
    canvas(d, cam, t)
    artist(d, cam, t, mode="reach", look=0.4)
    cx, cy = cam.p(-1300, -1100)
    d.ellipse([cx - cam.s(70), cy - cam.s(70), cx + cam.s(70), cy + cam.s(70)], outline=(120, 120, 120, 255), width=4)
    a = t * 3
    d.line([(cx, cy), (cx + math.cos(a) * cam.s(55), cy + math.sin(a) * cam.s(55))], fill=(120, 120, 120, 255), width=3)


def s2_inspiration(d, t, dur):
    p = t / dur
    # one small mark of blue
    cam = cam_lerp((-150, -620, 0.7), (-100, -700, 0.95), sstep(p))
    studio(d, cam, t)
    easel(d, cam)
    canvas(d, cam, t, marks=1 if p > 0.5 else 0)
    artist(d, cam, t, mode="reach", x=-560, look=0.2)
    if 0.45 < p < 0.75:
        particles(d, *cam.p(-150, -600), cam.s(120), (p - 0.45) / 0.3, PALETTE[0], n=12, seed=1, rise=0.2)
    top_caption(d, ["YOU DON'T NEED INSPIRATION", "TO BEGIN."], t, dur, accent={"INSPIRATION"})


def s3_sometimes(d, t, dur):
    p = t / dur
    cam = Cam(-100, -700, 0.95)
    studio(d, cam, t)
    easel(d, cam)
    canvas(d, cam, t, marks=1 + 5 * sstep(p))
    artist(d, cam, t, mode="hammer", x=-560, look=0.2, mouth=0.4 * p)
    top_caption(d, ["SOMETIMES…"], t, dur, accent={"SOMETIMES…"})


def s4_creates(d, t, dur):
    p = t / dur
    # the canvas blooms into a landscape; colour spills off it across the whole white room
    bloom = sstep(ramp(p, 0.05, 0.35))
    spill = sstep(ramp(p, 0.35, 0.6))
    cam = cam_lerp((-100, -700, 0.95), (0, -600, 0.5), sstep(ramp(p, 0.2, 0.7)))
    studio(d, cam, t, paint=spill)
    easel(d, cam)
    canvas(d, cam, t, marks=6, bloom=bloom)
    artist(d, cam, t, mode="cheer" if p > 0.5 else "hammer", x=-620, mouth=0.8)
    if 0.3 < p < 0.9:
        particles(d, *cam.p(0, -700), cam.s(1600), (p - 0.3) / 0.6, PALETTE[int(t * 3) % 6], n=50, seed=int(t * 3), rise=0.2, size=8)
    top_caption(d, ["BEGINNING CREATES", "INSPIRATION."], t, dur, accent={"BEGINNING", "INSPIRATION."})


def s5_end(d, t, dur):
    cam = Cam(0, -600, 0.5)
    studio(d, cam, t, paint=1.0)
    easel(d, cam)
    canvas(d, cam, t, marks=6, bloom=1.0)
    artist(d, cam, t, mode="stand", x=-620, mouth=0.6)
    overlay(d, (255, 255, 255), 0.35)
    final_card(d, t, dur, ["JUST BEGIN."], [(40, 60, 120, 255)], size=150, y=H * 0.2)


SCENES = [s0_hook, s1_wait, s2_inspiration, s3_sometimes, s4_creates, s5_end, s_follow]
