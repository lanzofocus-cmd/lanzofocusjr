"""THE CLOCK THAT HATES YOU — Time as a giant walking clock in a noir city.

World: cold blue-grey night city. TIME is a towering figure in a long coat with a clock face for a head; its red
second hand jumps on every tick, and on every tick something in the street dissolves. THE WASTER lives on a
couch lit by a phone; THE BUILDER works under a desk lamp while finished work piles up. Ends on a split screen
of the same clock over two different lives.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline, pill
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, stars, moon, figure,
                   top_caption, low_caption, final_card, shake, dust, darkness, word_reveal, beam, rain)
from kit import s_follow

TITLE = ("THE CLOCK", "THAT HATES YOU")
OUTPUT = "98_The_Clock_That_Hates_You_16x9.mp4"
FOLLOW_SUB = ("FOR IDEAS, LESSONS, AND PERSPECTIVES", "THAT CHALLENGE THE WAY YOU THINK.")

LINES = [
    "Time doesn't wait.",
    "While you wait for the perfect moment…",
    "Time is the only opponent…",
    "…that never gets tired.",
    "You cannot stop time.",
    "But you can decide what it carries.",
    "Same twenty-four hours.",
    "Different decisions.",
    "Use your time.",
    "",
]
SPOKEN = [l.lstrip("…") for l in LINES]
GAPS = {0: 1.4, 1: 3.0, 2: 0.4, 3: 1.4, 4: 1.6, 5: 1.6, 6: 0.8, 7: 1.4, 8: 1.4}

NAVY = (16, 22, 38, 255)
COAT = (24, 30, 50, 255)
FACE = (236, 236, 228, 255)
RED = (230, 50, 50, 255)
COLD = (150, 175, 220, 255)
WASTE = (160, 150, 175, 255)
BUILD = (255, 200, 110, 255)
LAMP = (255, 214, 150, 255)
TICK = 0.5   # seconds per tick


def clock_face(d, cx, cy, r, t, speed=1.0, a=1.0, ticks=True, face=FACE, glowk=0.3):
    glow(d, cx, cy, r * 1.8, COLD, glowk * a)
    d.ellipse([cx - r * 1.08, cy - r * 1.08, cx + r * 1.08, cy + r * 1.08], fill=col((40, 46, 66, 255), a))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col(face, a))
    for i in range(60):
        ang = math.radians(i * 6 - 90)
        big = i % 5 == 0
        r0 = r * (0.82 if big else 0.9)
        d.line([(cx + math.cos(ang) * r0, cy + math.sin(ang) * r0), (cx + math.cos(ang) * r * 0.96, cy + math.sin(ang) * r * 0.96)],
               fill=col((30, 30, 40, 255), a), width=max(1, int(r * (0.035 if big else 0.012))))
    sec = math.floor(t / TICK) * speed if ticks else t * speed / TICK
    # a tiny overshoot on each jump
    frac = (t / TICK) % 1
    sec += 0.12 * math.exp(-frac * 12) * math.sin(frac * 30) if ticks else 0
    for val, ln, wd, c in ((sec / 3600 * 6 + 3, 0.5, 0.06, (30, 30, 40, 255)), (sec / 60 * 6 + 1.5, 0.75, 0.04, (30, 30, 40, 255)), (sec, 0.85, 0.018, RED)):
        ang = math.radians(val * 6 - 90)
        d.line([(cx - math.cos(ang) * r * 0.12, cy - math.sin(ang) * r * 0.12), (cx + math.cos(ang) * r * ln, cy + math.sin(ang) * r * ln)],
               fill=col(c, a), width=max(2, int(r * wd)))
    d.ellipse([cx - r * 0.05, cy - r * 0.05, cx + r * 0.05, cy + r * 0.05], fill=col(RED, a))


def time_figure(d, cx, base, h, t, walk=0.0, a=1.0, speed=1.0, carry=None):
    """Towering clock-headed figure. base = feet y, h = height in px, walk = phase."""
    glow(d, cx, base - h * 0.5, h * 0.55, COLD, 0.22 * a)
    hip = (cx, base - h * 0.45)
    L = h * 0.24
    for i, c in ((1, (34, 42, 68, 255)), (0, (52, 62, 96, 255))):
        ph = walk + i * math.pi
        fx = cx + math.cos(ph) * h * 0.16
        fy = base - max(0.0, math.sin(ph)) * h * 0.06
        dx, dy = fx - hip[0], fy - hip[1]
        dist = min(L * 2 - 1, math.hypot(dx, dy))
        ang = math.atan2(dy, dx)
        k = math.acos(clamp(dist / (2 * L), -1, 1))
        knee = (hip[0] + L * math.cos(ang - k), hip[1] + L * math.sin(ang - k))
        d.line([hip, knee, (fx, fy)], fill=col(c, a), width=max(2, int(h * 0.045)), joint="curve")
        d.polygon([(fx - h * 0.02, fy), (fx + h * 0.07, fy), (fx + h * 0.06, fy - h * 0.025), (fx - h * 0.02, fy - h * 0.03)], fill=col(c, a))
    # long coat
    sh_y = base - h * 0.80
    coat = [(cx - h * 0.11, sh_y), (cx + h * 0.11, sh_y), (cx + h * 0.16 + math.sin(walk) * h * 0.02, base - h * 0.32), (cx - h * 0.17 + math.sin(walk) * h * 0.02, base - h * 0.30)]
    d.polygon(coat, fill=col(COAT, a))
    polyline(d, coat + [coat[0]], 1, col(COLD, 0.5 * a), max(1, int(h * 0.006)))
    d.line([(cx, sh_y + h * 0.02), (cx + h * 0.01, base - h * 0.32)], fill=col((10, 14, 24, 255), a), width=max(1, int(h * 0.006)))
    for side in (-1, 1):  # arms
        sw = math.sin(walk + (0 if side > 0 else math.pi)) * 0.4
        sx, sy = cx + side * h * 0.1, sh_y + h * 0.03
        ex, ey = sx + math.sin(sw) * h * 0.14, sy + math.cos(sw) * h * 0.14
        hx, hy = ex + math.sin(sw + 0.4) * h * 0.13, ey + math.cos(sw + 0.4) * h * 0.13
        d.line([(sx, sy), (ex, ey), (hx, hy)], fill=col((20, 26, 44, 255), a), width=max(2, int(h * 0.035)), joint="curve")
    # collar and the clock head
    d.polygon([(cx - h * 0.09, sh_y), (cx, sh_y + h * 0.06), (cx + h * 0.09, sh_y)], fill=col((40, 50, 80, 255), a))
    r = h * 0.12
    clock_face(d, cx, sh_y - r * 1.05, r, t, speed, a)
    if carry:
        carry(d, cx, sh_y - r * 1.05, r)


def city(d, cam, t, light=1.0, gone=None, change=0.0):
    draw_sky(d, (4, 6, 14, 255), (26, 34, 56, 255))
    stars(d, 0.6 * light, seed=13, n=60, ymax=0.4)
    moon(d, *cam.p(1600, -1300), cam.s(70), 0.8, bg=(4, 6, 14))
    rng = random.Random(3)
    # far towers (parallax)
    for k in range(-14, 22):
        x = k * 230
        hgt = rng.uniform(500, 1300)
        sx = (x - cam.cx * 0.5) * cam.z * 0.75 + W / 2
        top = (-hgt - cam.cy * 0.5) * cam.z * 0.75 + H / 2 + cam.oy
        bot = cam.p(0, 0)[1]
        if -300 < sx < W + 300:
            d.rectangle([sx, top, sx + 200 * cam.z * 0.75, bot], fill=(14, 18, 32, 255))
    # near buildings that can change over the years
    rng = random.Random(7)
    for k in range(-8, 12):
        x = k * 420
        hgt = rng.uniform(380, 820)
        swap = rng.random() < change * 0.8
        if swap:
            hgt = rng.uniform(600, 1100)
        a0, b0 = cam.p(x, -hgt), cam.p(x + 360, 0)
        if b0[0] < -50 or a0[0] > W + 50:
            continue
        d.rectangle([a0[0], a0[1], b0[0], b0[1]], fill=col((22, 28, 46, 255) if not swap else (30, 36, 58, 255), 1))
        wr = random.Random(k * 13 + int(change * 5))
        for row in range(int(hgt / 90)):
            for c in range(4):
                if wr.random() < 0.4 * light:
                    wx, wy = x + 30 + c * 85, -60 - row * 90
                    d.rectangle(cam.box(wx, wy - 40, wx + 40, wy), fill=col(LAMP, 0.55))
    fy = cam.p(0, 0)[1]
    if fy < H:
        d.rectangle([0, fy, W, H], fill=(10, 12, 20, 255))
    d.line([(0, fy), (W, fy)], fill=col(COLD, 0.3), width=max(1, int(cam.s(3))))
    props(d, cam, t, gone or {})
    fog(d, *cam.p(0, -60), cam.s(6000), 0.15, (150, 170, 220))


PROPS = [("lamp", -1500), ("bench", -1100), ("tree", -700), ("sign", -250), ("lamp", 200), ("car", 650), ("tree", 1150), ("lamp", 1600), ("bench", 2000), ("sign", 2400)]


def props(d, cam, t, gone):
    """Street furniture. gone: {index: 0..1} dissolve amount."""
    for i, (kind, x) in enumerate(PROPS):
        g = gone.get(i, 0.0)
        a = 1 - g
        if a <= 0.01:
            continue
        c = col((70, 80, 110, 255), a)
        if kind == "lamp":
            d.line([cam.p(x, 0), cam.p(x, -420)], fill=c, width=max(2, int(cam.s(10))))
            d.line([cam.p(x, -420), cam.p(x + 70, -420)], fill=c, width=max(2, int(cam.s(8))))
            lx, ly = cam.p(x + 70, -405)
            d.ellipse([lx - cam.s(16), ly - cam.s(10), lx + cam.s(16), ly + cam.s(14)], fill=col(LAMP, a))
            glow(d, lx, ly, cam.s(220), LAMP, 0.5 * a)
            beam(d, lx, ly, lx - cam.s(160), lx + cam.s(160), cam.p(0, 0)[1], LAMP, 0.06 * a, cam.s(10))
        elif kind == "bench":
            d.rectangle(cam.box(x - 110, -70, x + 110, -55), fill=c)
            d.rectangle(cam.box(x - 110, -130, x + 110, -115), fill=c)
            for s in (-1, 1):
                d.rectangle(cam.box(x + s * 90 - 6, -70, x + s * 90 + 6, 0), fill=c)
        elif kind == "tree":
            d.rectangle(cam.box(x - 14, -220, x + 14, 0), fill=col((60, 50, 60, 255), a))
            d.ellipse(cam.box(x - 140, -460, x + 140, -180), fill=col((40, 70, 80, 255), a))
        elif kind == "sign":
            d.line([cam.p(x, 0), cam.p(x, -300)], fill=c, width=max(2, int(cam.s(8))))
            d.rectangle(cam.box(x - 120, -380, x + 120, -280), fill=col((200, 60, 70, 255), a))
            d.text(cam.p(x, -330), "OPEN", font=font(max(10, int(cam.s(40)))), fill=col(WHITE, a), anchor="mm")
        elif kind == "car":
            d.rounded_rectangle(cam.box(x - 180, -110, x + 180, -30), int(cam.s(30)), fill=col((60, 70, 100, 255), a))
            d.rounded_rectangle(cam.box(x - 100, -170, x + 90, -100), int(cam.s(30)), fill=col((50, 60, 90, 255), a))
            for s in (-1, 1):
                d.ellipse(cam.box(x + s * 110 - 40, -70, x + s * 110 + 40, 10), fill=col((20, 20, 26, 255), a))
        if 0 < g < 1:  # dissolving into rising particles
            r = random.Random(i)
            for k in range(26):
                px = x + r.uniform(-150, 150)
                py = -r.uniform(0, 400) - g * r.uniform(100, 500)
                sx, sy = cam.p(px, py)
                rr = max(1.5, cam.s(6))
                d.ellipse([sx - rr, sy - rr, sx + rr, sy + rr], fill=col(COLD, (1 - g) * 0.9))


def tick_gone(t, order, start=0.0):
    """Every tick from `start` dissolves the next prop in `order`."""
    out = {}
    for j, idx in enumerate(order):
        at = start + (j + 1) * TICK
        out[idx] = clamp((t - at) / 0.4)
    return out


# ---------------------------------------------------------------- interiors
def room(d, t, kind, x0=0, x1=W, years=0.0, work=0.0, a=1.0, clock_speed=1.0):
    """kind: waste | build. A side-on room: window with the city and Time passing, furniture, a shelf."""
    w = x1 - x0
    cx = (x0 + x1) / 2
    wall = (26, 26, 36, 255) if kind == "waste" else (40, 32, 28, 255)
    d.rectangle([x0, 0, x1, H], fill=col(wall, a))
    floor_y = H * 0.8
    d.rectangle([x0, floor_y, x1, H], fill=col(dimc(wall, 0.6), a))
    # window
    wx0, wx1, wy0, wy1 = x0 + w * 0.08, x0 + w * 0.42, H * 0.22, H * 0.58
    night = 0.5 + 0.5 * math.sin(t * (1.8 if years > 0 else 0.3) * clock_speed)
    d.rectangle([wx0, wy0, wx1, wy1], fill=col(mix((120, 150, 200, 255), (10, 14, 30, 255), night), a))
    for k in range(5):  # little skyline in the window
        bx = wx0 + (wx1 - wx0) * k / 5
        d.rectangle([bx + 4, wy1 - (wy1 - wy0) * (0.3 + 0.12 * (k % 3)), bx + (wx1 - wx0) / 5 - 4, wy1], fill=col((20, 24, 40, 255), a))
    # Time walking past outside
    tp = ((t * 0.12 * clock_speed) % 1.4) - 0.2
    tx = lerp(wx0 - 80, wx1 + 80, tp)
    d._image.alpha_composite(_clip_time(int(wx1 - wx0), int(wy1 - wy0), t, tx - wx0, clock_speed), (int(wx0), int(wy0)))
    d.rectangle([wx0, wy0, wx1, wy1], outline=col((70, 64, 70, 255), a), width=8)
    d.line([((wx0 + wx1) / 2, wy0), ((wx0 + wx1) / 2, wy1)], fill=col((70, 64, 70, 255), a), width=6)
    # wall calendar
    calx, caly = x0 + w * 0.52, H * 0.3
    d.rectangle([calx, caly, calx + w * 0.09, caly + w * 0.1], fill=col((235, 230, 220, 255), a))
    d.rectangle([calx, caly, calx + w * 0.09, caly + w * 0.025], fill=col(RED, a))
    yr = 2026 + int(years * 12)
    d.text((calx + w * 0.045, caly + w * 0.06), str(yr), font=font(max(12, int(w * 0.022))), fill=(40, 30, 30, int(255 * a)), anchor="mm")
    # shelf
    sx0, sx1, sy = x0 + w * 0.62, x0 + w * 0.94, H * 0.36
    for k in range(2):
        yy = sy + k * H * 0.16
        d.rectangle([sx0, yy, sx1, yy + 10], fill=col((90, 70, 50, 255), a))
    items = int(work * 12)
    r = random.Random(4)
    for k in range(items):
        row = k // 6
        bx = sx0 + 12 + (k % 6) * (sx1 - sx0 - 24) / 6
        hgt = r.uniform(40, 80)
        yy = sy + row * H * 0.16
        c = r.choice([(255, 200, 110, 255), (120, 200, 255, 255), (240, 120, 100, 255), (160, 230, 150, 255)])
        d.rectangle([bx, yy - hgt, bx + (sx1 - sx0) / 6 - 10, yy], fill=col(c, a))
    if kind == "waste" and years > 0:
        for k in range(3):  # dust and an unfinished canvas
            d.text((sx0 + 40 + k * 90, sy - 20), "~", font=font(30), fill=col(GREY, 0.5 * years * a), anchor="mm")
    return floor_y


_tcache = {}


def _clip_time(w, h, t, tx, speed):
    from PIL import Image, ImageDraw
    im = Image.new("RGBA", (w, h))
    dd = ImageDraw.Draw(im)
    time_figure(dd, tx, h + h * 0.15, h * 1.25, t, walk=t * 2.2 * speed, a=0.95, speed=speed)
    return im


def couch_waster(d, cx, floor_y, s, t, years=0.0, look=0.0, a=1.0):
    d.rounded_rectangle([cx - 230 * s, floor_y - 190 * s, cx + 230 * s, floor_y - 60 * s], int(40 * s), fill=col((80, 60, 90, 255), a))
    d.rounded_rectangle([cx - 260 * s, floor_y - 110 * s, cx + 260 * s, floor_y - 20 * s], int(40 * s), fill=col((100, 76, 110, 255), a))
    c = mix(WASTE, (200, 200, 200, 255), years)
    figure(d, cx - 20 * s, floor_y - 95 * s, 230 * s, c, mode="sit", face=1, acc=("hair",), look=look, head_down=0.3 * (1 - look),
           hands=None, a=a, prop=phone, tired=0.0)


def phone(d, fh, bh, h, a):
    if fh:
        x, y = fh
        d.rounded_rectangle([x - h * 0.03, y - h * 0.06, x + h * 0.03, y + h * 0.02], int(h * 0.01), fill=col((180, 210, 255, 255), a))
        glow(d, x, y, h * 0.5, (140, 180, 255), 0.6 * a)


def desk_builder(d, cx, floor_y, s, t, a=1.0, act=0):
    d.rectangle([cx - 40 * s, floor_y - 170 * s, cx + 300 * s, floor_y - 150 * s], fill=col((110, 80, 55, 255), a))
    for sx in (cx - 20 * s, cx + 280 * s):
        d.rectangle([sx - 8 * s, floor_y - 150 * s, sx + 8 * s, floor_y], fill=col((90, 64, 44, 255), a))
    lx, ly = cx + 240 * s, floor_y - 170 * s
    d.line([(lx, ly), (lx - 40 * s, ly - 120 * s), (lx - 110 * s, ly - 150 * s)], fill=col((60, 60, 70, 255), a), width=max(2, int(8 * s)))
    d.polygon([(lx - 150 * s, ly - 140 * s), (lx - 80 * s, ly - 175 * s), (lx - 70 * s, ly - 130 * s)], fill=col((70, 70, 80, 255), a))
    glow(d, lx - 110 * s, ly - 100 * s, 300 * s, LAMP, 0.7 * a)
    # what the builder is working on: a book, an instrument, a canvas
    if act == 0:
        d.rectangle([cx + 60 * s, ly - 20 * s, cx + 180 * s, ly], fill=col((240, 235, 220, 255), a))
        d.line([(cx + 120 * s, ly - 20 * s), (cx + 120 * s, ly)], fill=col((120, 110, 100, 255), a), width=2)
    elif act == 1:
        d.rectangle([cx + 40 * s, ly - 70 * s, cx + 200 * s, ly - 5 * s], fill=col((30, 34, 44, 255), a), outline=col((120, 200, 255, 255), a), width=3)
        glow(d, cx + 120 * s, ly - 40 * s, 120 * s, (120, 200, 255), 0.4 * a)
    else:
        d.polygon([(cx + 80 * s, ly), (cx + 140 * s, ly - 200 * s), (cx + 200 * s, ly)], outline=col((200, 160, 110, 255), a), width=3)
        d.rectangle([cx + 70 * s, ly - 190 * s, cx + 210 * s, ly - 80 * s], fill=col((240, 230, 210, 255), a))
        d.arc([cx + 90 * s, ly - 180 * s, cx + 190 * s, ly - 90 * s], 200, 340, fill=col(BUILD, a), width=4)
    # chair and the builder
    d.rectangle([cx - 120 * s, floor_y - 120 * s, cx - 20 * s, floor_y - 105 * s], fill=col((80, 60, 45, 255), a))
    d.rectangle([cx - 120 * s, floor_y - 260 * s, cx - 105 * s, floor_y - 105 * s], fill=col((80, 60, 45, 255), a))
    k = math.sin(t * 6)
    hands = ((cx + 70 * s + 10 * s * k, ly - 10 * s), (cx + 120 * s - 10 * s * k, ly - 8 * s))
    figure(d, cx - 70 * s, floor_y - 120 * s + 4, 230 * s, BUILD, mode="sit", face=1, acc=("hair",), hands=hands, a=a,
           head_down=0.35, look=-0.2)


# ---------------------------------------------------------------- scenes
def s0_wait(d, t, dur):
    p = t / dur
    # hook: the face fills the screen, ticking hard; pull back to a giant in the street, the city vanishing tick by tick
    pull = sstep(ramp(t, 0.5, dur * 0.8))
    z = lerp(3.2, 0.42, pull)
    cam = Cam(0, lerp(-1640, -800, pull), z)
    city(d, cam, t, gone=tick_gone(t, [3, 4, 2, 5, 1], start=dur * 0.45))
    fx, fy = cam.p(0, 0)
    time_figure(d, fx, fy, cam.s(2000), t, walk=t * 0.8)
    top_caption(d, ["TIME DOESN'T WAIT."], t, dur, accent={"WAIT."})


def s1_perfect(d, t, dur):
    p = t / dur
    # the waster scrolls; years pass in the window, the calendar, the hair
    yrs = sstep(ramp(t, dur * 0.35, dur * 0.6))
    fl = room(d, t, "waste", years=yrs, clock_speed=1 + 8 * yrs)
    couch_waster(d, W * 0.42, fl, 1.25, t, years=yrs, look=0.8 if yrs > 0.05 else 0.0)
    if 0.02 < yrs < 0.98:  # calendar pages flying off
        r = random.Random(int(t * 10))
        for k in range(4):
            px, py = W * 0.56 + r.uniform(-40, 160), H * 0.3 - r.uniform(0, 300)
            d.rectangle([px, py, px + 50, py + 56], fill=col((235, 230, 220, 255), 0.7))
    darkness(d, W / 2, H / 2, 0.35)
    top_caption(d, ["WHILE YOU WAIT FOR", "THE PERFECT MOMENT…"], t, dur, accent={"PERFECT"})


def _walker(d, t, dur, part):
    p = t / dur
    k = (part + p) / 2
    x = lerp(-2000, 2200, k)
    cam = Cam(x + 200, -950, 0.42)
    city(d, cam, t, change=k, gone=tick_gone(t + part * 3, [0, 6, 7, 8, 9], start=0.3) if part else tick_gone(t, [0, 6], start=0.3))
    # people on the pavement grow older as it passes
    for j, px in enumerate((-1200, -300, 700, 1500)):
        age = clamp(k * 1.8 - j * 0.2)
        fx, fy = cam.p(px, 0)
        figure(d, fx, fy, cam.s(170), mix((150, 160, 190, 255), (120, 120, 130, 255), age), mode="walk" if age < 0.6 else "slump",
               phase=t * (4 - 2 * age), face=-1, acc=("hair",), lean=0.3 * age, eyes=True)
    fx, fy = cam.p(x, 0)
    time_figure(d, fx, fy, cam.s(1700), t, walk=x / 160)
    if part == 0:
        low_caption(d, ["TIME IS THE ONLY OPPONENT…"], t, dur, accent={"OPPONENT…"}, size=64)
    else:
        low_caption(d, ["…THAT NEVER GETS TIRED."], t, dur, accent={"NEVER", "TIRED."}, size=64)


def s2(d, t, dur):
    _walker(d, t, dur, 0)


def s3(d, t, dur):
    _walker(d, t, dur, 1)
s3.seamless = True


def s4_cannot(d, t, dur):
    p = t / dur
    work = p * 0.6
    fl = room(d, t, "build", work=work, clock_speed=3)
    act = min(2, int(p * 3))
    desk_builder(d, W * 0.38, fl, 1.25, t, act=act)
    lbl = ["STUDYING", "PRACTICING", "CREATING"][act]
    pill(d, 220, H - 120, lbl, 0.9, 28, inverted=True)
    top_caption(d, ["YOU CANNOT STOP TIME."], t, dur, accent={"CANNOT"})


def s5_carries(d, t, dur):
    p = t / dur
    # Time walks on, and this time it carries the builder's finished work on its hands
    cam = Cam(lerp(-600, 600, p) + 200, -980, 0.45)
    city(d, cam, t, change=1.0)
    fx, fy = cam.p(lerp(-600, 600, p), 0)

    def carry(dd, cx, cy, r):
        n = 6
        for i in range(n):
            ang = t * 1.2 + i * math.tau / n
            k = ramp(t, 0.3 + i * 0.25, 0.4)
            px, py = cx + math.cos(ang) * r * 2.1, cy + math.sin(ang) * r * 2.1
            c = [(255, 200, 110, 255), (120, 200, 255, 255), (240, 120, 100, 255), (160, 230, 150, 255)][i % 4]
            glow(dd, px, py, r * 0.8, c, 0.6 * k)
            dd.regular_polygon((px, py, r * 0.32), 4, rotation=t * 50 + i * 20, fill=col(c, k))
    time_figure(d, fx, fy, cam.s(1650), t, walk=lerp(-600, 600, p) / 160, carry=carry)
    low_caption(d, ["BUT YOU CAN DECIDE WHAT IT CARRIES."], t, dur, accent={"DECIDE", "CARRIES."}, size=60)


def split(d, t, dur, part):
    p = t / dur
    fl = room(d, t, "waste", 0, W // 2, years=1.0, work=0.0, clock_speed=2)
    couch_waster(d, W * 0.24, fl, 0.75, t, years=1.0)
    room(d, t, "build", W // 2, W, work=1.0, clock_speed=2)
    desk_builder(d, W * 0.66, fl, 0.75, t, act=2)
    d.line([(W / 2, 0), (W / 2, H)], fill=(0, 0, 0, 255), width=10)
    overlay(d, (0, 0, 0), 0.25)
    # the same clock over both lives
    clock_face(d, W / 2, H * 0.47, 120, t * 4, a=1.0, glowk=0.5)
    d.text((W * 0.25, H - 70), "THE WASTER", font=font(34), fill=col(WASTE, 0.9), anchor="mm")
    d.text((W * 0.75, H - 70), "THE BUILDER", font=font(34), fill=col(BUILD, 0.9), anchor="mm")
    if part == 0:
        top_caption(d, ["SAME TWENTY-FOUR HOURS."], t, dur, accent={"SAME"})
    else:
        top_caption(d, ["DIFFERENT DECISIONS."], t, dur, accent={"DIFFERENT"})


def s6(d, t, dur):
    split(d, t, dur, 0)


def s7(d, t, dur):
    split(d, t + 3, dur, 1)
s7.seamless = True


def s8_use(d, t, dur):
    draw_sky(d, (4, 6, 14, 255), (20, 26, 44, 255))
    clock_face(d, W / 2, 420, 250, t, a=ramp(t, 0.0, 0.4), glowk=0.6)
    final_card(d, t, dur, ["USE YOUR TIME."], [WHITE], size=130, y=860)


SCENES = [s0_wait, s1_perfect, s2, s3, s4_cannot, s5_carries, s6, s7, s8_use, s_follow]
