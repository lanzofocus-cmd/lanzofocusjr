"""THE EMPTY BOOK — a huge blank book that stays blank until you write in it.

World: a candlelit library at night in sepia and ink black. A giant open book on a lectern; wind flips page after
blank page. THE AUTHOR waits beside it, then picks up the quill. Ink lines pour across the page and draw a world:
horizon, mountains, a sun, a river, trees. The lines bloom into watercolour colour and the little drawn figure
of the author steps into the picture.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, dust)
from kit import s_follow

TITLE = ("THE EMPTY", "BOOK")
OUTPUT = "117_The_Empty_Book_16x9.mp4"
LINES = [
    "",
    "",
    "Your life isn't waiting to be discovered.",
    "It's waiting to be written.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.0, 4: 3.6}
GAPS = {2: 2.0, 3: 6.4}

PAGE = (245, 234, 208, 255)
INK = (30, 24, 26, 255)
CANDLE = (255, 190, 110, 255)
YOU = (230, 220, 200, 255)
CH = 260
BOOK = (0, -520, 1100, 720)   # centre x, centre y, width, height of the open spread


def library(d, cam, t):
    draw_sky(d, (10, 6, 4, 255), (34, 22, 14, 255))
    for k in range(-6, 7):  # shelves of books
        x = k * 420
        a, b = cam.p(x, -1500), cam.p(x + 400, -40)
        d.rectangle([a[0], a[1], b[0], b[1]], fill=(40, 26, 18, 255))
        r = random.Random(k)
        for row in range(5):
            yy = -1450 + row * 280
            bx = x + 10
            while bx < x + 390:
                bw = r.uniform(20, 40)
                c = r.choice([(90, 40, 30), (40, 60, 50), (70, 50, 30), (50, 40, 70)])
                d.rectangle(cam.box(bx, yy, bx + bw - 3, yy + r.uniform(180, 240)), fill=c + (255,))
                bx += bw
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=(24, 16, 12, 255))
    # candles
    for x in (-760, 760):
        b, tp = cam.p(x, -160), cam.p(x, -330)
        d.rectangle([b[0] - cam.s(22), tp[1], b[0] + cam.s(22), b[1]], fill=(240, 230, 210, 255))
        fl = cam.p(x, -360 - 8 * math.sin(t * 9 + x))
        d.ellipse([fl[0] - cam.s(12), fl[1] - cam.s(30), fl[0] + cam.s(12), fl[1] + cam.s(6)], fill=col(CANDLE, 1))
        glow(d, fl[0], fl[1], cam.s(400), CANDLE, 0.6)


def lectern(d, cam):
    cx, cy, bw, bh = BOOK
    d.polygon([cam.p(cx - 200, cy + bh / 2), cam.p(cx + 200, cy + bh / 2), cam.p(cx + 120, 0), cam.p(cx - 120, 0)], fill=(70, 46, 30, 255))


def book(d, cam, t, flip=0.0):
    """The open spread; returns its screen rectangle. flip: page-flutter phase (0 = still)."""
    cx, cy, bw, bh = BOOK
    x0, y0 = cam.p(cx - bw / 2, cy - bh / 2)
    x1, y1 = cam.p(cx + bw / 2, cy + bh / 2)
    d.rounded_rectangle([x0 - cam.s(30), y0 - cam.s(20), x1 + cam.s(30), y1 + cam.s(30)], int(cam.s(20)), fill=(90, 30, 30, 255))
    d.rectangle([x0, y0, x1, y1], fill=col(PAGE, 1))
    mx = (x0 + x1) / 2
    d.line([(mx, y0), (mx, y1)], fill=col((200, 185, 150, 255), 1), width=max(1, int(cam.s(6))))
    if flip > 0:  # a page mid-turn, arcing over the spine
        ang = (flip % 1) * math.pi
        px = mx + math.cos(ang) * (x1 - mx)
        lift = math.sin(ang) * cam.s(120)
        pts = [(mx, y0), (px, y0 - lift), (px, y1 - lift * 0.6), (mx, y1)]
        d.polygon(pts, fill=col(dimc(PAGE, 0.94), 1), outline=col((200, 185, 150, 255), 1))
    return x0, y0, x1, y1


def ink_world(d, rect, k, color_k, t):
    """The world drawn on the spread: k = ink progress 0..1, color_k = watercolour bloom 0..1."""
    x0, y0, x1, y1 = rect
    w, h = x1 - x0, y1 - y0
    def P(u, v):
        return (x0 + u * w, y0 + v * h)
    hz = 0.62
    strokes = [
        [P(0.04, hz), P(0.96, hz)],                                                                                # horizon
        [P(0.05, hz), P(0.18, 0.35), P(0.28, 0.5), P(0.4, 0.26), P(0.55, hz)],                                      # mountains
        [P(0.5, hz), P(0.66, 0.4), P(0.78, 0.52), P(0.9, 0.36), P(0.96, hz)],
        [P(0.62, 0.95), P(0.58, 0.82), P(0.66, 0.74), P(0.6, 0.66), P(0.64, hz)],                                    # river
        [P(0.7, 0.95), P(0.68, 0.82), P(0.75, 0.74), P(0.68, 0.66), P(0.665, hz)],
    ]
    n = len(strokes) + 3
    # watercolour washes first, under the ink
    if color_k > 0:
        tpoly(d, [P(0, 0), P(1, 0), P(1, hz), P(0, hz)], col((150, 200, 240, 255), 0.6 * color_k))
        tpoly(d, [P(0, hz), P(1, hz), P(1, 1), P(0, 1)], col((140, 200, 120, 255), 0.65 * color_k))
        tpoly(d, strokes[1] + [P(0.55, hz)], col((140, 120, 170, 255), 0.7 * color_k))
        tpoly(d, strokes[2], col((120, 110, 160, 255), 0.7 * color_k))
        tpoly(d, strokes[3] + strokes[4][::-1], col((90, 160, 230, 255), 0.8 * color_k))
        sx, sy = P(0.3, 0.22)
        glow(d, sx, sy, w * 0.12, (255, 210, 120), 0.7 * color_k)
    lw = max(3, int(w * 0.006))
    for i, s in enumerate(strokes):
        polyline(d, s, clamp(k * n - i), col(INK, 1), lw)
    # sun
    sk = clamp(k * n - 5)
    if sk > 0:
        sx, sy = P(0.3, 0.22)
        r = w * 0.05
        polyline(d, [(sx + math.cos(a) * r, sy + math.sin(a) * r) for a in [j * math.tau / 30 for j in range(31)]], sk, col(INK, 1), lw)
        if color_k > 0:
            d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=col((255, 200, 90, 255), color_k))
    # trees
    tk = clamp(k * n - 6)
    r = random.Random(3)
    for j in range(7):
        if tk * 7 <= j:
            break
        u = r.uniform(0.08, 0.5) if j % 2 else r.uniform(0.75, 0.95)
        v = r.uniform(0.7, 0.9)
        tx, ty = P(u, v)
        th = h * 0.1
        d.line([(tx, ty), (tx, ty - th * 0.4)], fill=col(INK, 1), width=lw)
        d.ellipse([tx - th * 0.25, ty - th, tx + th * 0.25, ty - th * 0.35], outline=col(INK, 1), width=lw,
                  fill=col((80, 150, 80, 255), color_k) if color_k > 0 else None)
    return P


def quill(d, x, y, s, a=1.0):
    d.polygon([(x, y), (x + s * 0.3, y - s * 1.6), (x + s * 0.8, y - s * 1.9), (x + s * 0.2, y - s * 0.4)], fill=col((240, 240, 235, 255), a))
    d.line([(x, y), (x + s * 0.6, y - s * 1.7)], fill=col((150, 140, 130, 255), a), width=2)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # the book slams open; a wind flips blank page after blank page in the candlelight
    cam = cam_lerp((0, -520, 1.4), (0, -480, 0.95), sstep(p))
    hit = pulse(t, 0.3, 0.12)
    shake(cam, t, 12 * hit)
    library(d, cam, t)
    lectern(d, cam)
    book(d, cam, t, flip=t * 2.5 if t > 0.4 else 0)
    dust(d, t, 0.6, n=50, color=(255, 210, 160))


def s1_wait(d, t, dur):
    p = t / dur
    # the author sits beside the empty book and waits; candles burn down; nothing appears
    cam = cam_lerp((-420, -360, 1.0), (-380, -350, 1.08), p)
    library(d, cam, t)
    lectern(d, cam)
    book(d, cam, t)
    fx, fy = cam.p(-760 + 120, 0)
    figure(d, fx, fy, cam.s(CH), YOU, mode="sit", face=1, acc=("hair",), head_down=0.4 + 0.2 * math.sin(t), look=0.2, name="THE AUTHOR")
    d.text((W - 140, H - 110), "WAITING…", font=font(30), fill=col(GREY, 0.7), anchor="rm")


def s2_discovered(d, t, dur):
    p = t / dur
    # standing, quill in hand; a hesitation... and the first line of ink
    cam = cam_lerp((-100, -440, 0.85), (0, -430, 1.0), sstep(p))
    library(d, cam, t)
    lectern(d, cam)
    rect = book(d, cam, t)
    P = ink_world(d, rect, 0.12 * sstep(ramp(p, 0.55, 0.45)), 0.0, t)
    hx, hy = P(lerp(0.04, 0.4, sstep(ramp(p, 0.55, 0.45))), 0.62)
    quill(d, hx, hy, cam.s(90))
    top_caption(d, ["YOUR LIFE ISN'T WAITING", "TO BE DISCOVERED."], t, dur, accent={"DISCOVERED."})


def s3_written(d, t, dur):
    p = t / dur
    # ink pours across the pages, then blooms into colour; a tiny drawn author steps into the picture
    cam = cam_lerp((0, -430, 1.0), (0, -420, 1.2), sstep(p))
    library(d, cam, t)
    lectern(d, cam)
    rect = book(d, cam, t)
    k = lerp(0.12, 1.0, sstep(ramp(p, 0.0, 0.6)))
    ck = sstep(ramp(p, 0.55, 0.3))
    P = ink_world(d, rect, k, ck, t)
    if p < 0.6:
        n = 8
        seg = min(7, int(k * n))
        hx, hy = P(0.1 + 0.1 * seg + 0.05 * math.sin(t * 6), 0.4 + 0.15 * math.sin(t * 3))
        quill(d, hx, hy, cam.s(90))
    if ck > 0.3:
        u = lerp(0.15, 0.45, sstep(ramp(p, 0.75, 0.25)))
        fx, fy = P(u, 0.84)
        figure(d, fx, fy, cam.s(110), INK, mode="walk", phase=t * 5, face=1, acc=("hair",), a=ramp(p, 0.65, 0.1), eyes=False)
    top_caption(d, ["IT'S WAITING", "TO BE WRITTEN."], t, dur, accent={"WRITTEN."})


def s4_end(d, t, dur):
    cam = Cam(0, -420, 1.2 + 0.5 * sstep(t / dur))
    library(d, cam, t)
    rect = book(d, cam, t)
    P = ink_world(d, rect, 1.0, 1.0, t)
    fx, fy = P(0.45 + 0.03 * t, 0.84)
    figure(d, fx, fy, cam.s(110), INK, mode="walk", phase=t * 5, face=1, acc=("hair",), eyes=False)
    stage_end(d, t, dur, ["WRITE IT."], [INK], size=150, dim=0.0, y=H * 0.3)


SCENES = [s0_hook, s1_wait, s2_discovered, s3_written, s4_end, s_follow]
