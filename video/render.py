#!/usr/bin/env python3
"""Render "THE VERSION YOU'RE BECOMING" in the LanzoFocus minimalist style.

Black background, soft centre glow, glowing white line-art icons and bold
uppercase captions revealed word by word. 1920x1080 (16:9), 30 fps.

Usage: python3 render.py timings.json out_silent.mp4 [projects/<name>/scenes.py]
timings.json: {"intro": seconds, "segments": [[start, end], ...]} (17 segments, seconds on the final timeline)
"""
import json, math, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

W, H, FPS = 1920, 1080, 30
WHITE = (255, 255, 255, 255)
GREY = (120, 120, 120, 255)
DIM = (70, 70, 70, 255)
FONT_B = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
FONT_SB = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"
import os
if not os.path.exists(FONT_B):
    FONT_B = FONT_SB
_fonts = {}


def font(size, bold=True):
    k = (size, bold)
    if k not in _fonts:
        _fonts[k] = ImageFont.truetype(FONT_B if bold else FONT_SB, size)
    return _fonts[k]


def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))


def ease(x):
    x = clamp(x)
    return 1 - (1 - x) ** 3


def ramp(t, start, dur=0.5):
    return ease((t - start) / dur)


def lerp(a, b, p):
    return a + (b - a) * p


def col(c, a):
    return (c[0], c[1], c[2], int(c[3] * clamp(a)))


# ---------------------------------------------------------------- primitives
def polyline(d, pts, p=1.0, fill=WHITE, width=6):
    """Draw a polyline revealed up to fraction p of its length."""
    if p <= 0 or len(pts) < 2:
        return
    segs = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    total = sum(segs) * clamp(p)
    out = [pts[0]]
    for i, s in enumerate(segs):
        if total >= s:
            out.append(pts[i + 1]); total -= s
        else:
            f = total / s if s else 0
            out.append((lerp(pts[i][0], pts[i + 1][0], f), lerp(pts[i][1], pts[i + 1][1], f)))
            break
    d.line(out, fill=fill, width=width, joint="curve")
    r = width / 2 - 0.5
    for q in (out[0], out[-1]):
        d.ellipse([q[0] - r, q[1] - r, q[0] + r, q[1] + r], fill=fill)


def rect_pts(x0, y0, x1, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)]


def rrect(d, box, r, p=1.0, fill=WHITE, width=6):
    if p >= 1:
        d.rounded_rectangle(box, r, outline=fill, width=width)
    else:
        polyline(d, rect_pts(*box), p, fill, width)


def arc_pts(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(math.radians(lerp(a0, a1, i / n))),
             cy + r * math.sin(math.radians(lerp(a0, a1, i / n)))) for i in range(n + 1)]


def circle(d, cx, cy, r, p=1.0, fill=WHITE, width=6):
    polyline(d, arc_pts(cx, cy, r, -90, 270, 90), p, fill, width)


def person(d, cx, base, s=1.0, a=1.0, fill=WHITE):
    """Filled figure (head + rounded torso) standing on y=base."""
    c = col(fill, a)
    hr = 26 * s
    bw, bh = 46 * s, 64 * s
    d.rounded_rectangle([cx - bw, base - bh, cx + bw, base], int(30 * s), fill=c)
    d.rectangle([cx - bw, base - bh * 0.4, cx + bw, base], fill=c)
    hy = base - bh - hr - 10 * s
    d.ellipse([cx - hr, hy - hr, cx + hr, hy + hr], fill=c)


def dashed_person(d, cx, base, s=1.0, a=1.0, fill=WHITE):
    c = col(fill, a)
    hr = 26 * s
    bw, bh = 46 * s, 64 * s
    hy = base - bh - hr - 10 * s
    for i in range(0, 360, 30):
        d.arc([cx - hr, hy - hr, cx + hr, hy + hr], i, i + 16, fill=c, width=max(2, int(4 * s)))
    pts = [(cx - bw, base)] + arc_pts(cx, base - bh + 30 * s, bw, 180, 360, 30) + [(cx + bw, base), (cx - bw, base)]
    dashed(d, pts, c, max(2, int(4 * s)), 14 * s, 10 * s)


def dashed(d, pts, fill, width, dash, gap):
    for i in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        L = math.dist(pts[i], pts[i + 1])
        if L == 0:
            continue
        pos = 0.0
        while pos < L:
            e = min(L, pos + dash)
            d.line([(lerp(x0, x1, pos / L), lerp(y0, y1, pos / L)), (lerp(x0, x1, e / L), lerp(y0, y1, e / L))], fill=fill, width=width)
            pos += dash + gap


def pill(d, cx, cy, text, a=1.0, size=26, inverted=True):
    f = font(size)
    tw = d.textlength(text, font=f)
    pw, ph = tw / 2 + 26, size * 0.95
    if inverted:
        d.rounded_rectangle([cx - pw, cy - ph, cx + pw, cy + ph], int(ph), fill=col(WHITE, a))
        d.text((cx, cy), text, font=f, fill=(0, 0, 0, int(255 * clamp(a))), anchor="mm")
    else:
        d.rounded_rectangle([cx - pw, cy - ph, cx + pw, cy + ph], int(ph), outline=col(WHITE, a), width=3)
        d.text((cx, cy), text, font=f, fill=col(WHITE, a), anchor="mm")


def label(d, cx, cy, text, a=1.0, size=24, c=WHITE):
    d.text((cx, cy), text, font=font(size, False), fill=col(c, a), anchor="mm")


def check(d, cx, cy, s, p, width=8, fill=WHITE):
    polyline(d, [(cx - 22 * s, cy), (cx - 6 * s, cy + 16 * s), (cx + 24 * s, cy - 18 * s)], p, fill, width)


# ---------------------------------------------------------------- captions
def caption(d, lines, t, dur, y=170, size=64, accent=None, start=0.0, speak=0.6):
    """Word-by-word reveal. lines: list of strings. accent: set of words drawn larger/brighter."""
    words = [(li, w) for li, ln in enumerate(lines) for w in ln.split()]
    n = len(words)
    window = max(0.4, dur * speak)
    lh = size * 1.18
    y0 = y - (len(lines) - 1) * lh / 2
    f = font(size)
    idx = 0
    for li, ln in enumerate(lines):
        ws = ln.split()
        widths = [d.textlength(w, font=f) for w in ws]
        space = d.textlength(" ", font=f)
        total = sum(widths) + space * (len(ws) - 1)
        x = W / 2 - total / 2
        for w, wd in zip(ws, widths):
            appear = start + window * idx / max(1, n)
            a = ramp(t, appear, 0.35)
            dy = (1 - a) * 18
            fill = WHITE if not accent or w.strip(".,…?") in accent else (200, 200, 200, 255)
            d.text((x, y0 + li * lh + dy), w, font=f, fill=col(fill, a), anchor="lm")
            x += wd + space
            idx += 1


# ---------------------------------------------------------------- scenes
CY = 600  # icon centre line


TITLE = ("THE VERSION", "YOU'RE BECOMING")
CAMERA_PUSH = 0.04  # each scene slowly zooms in by this fraction
FOLLOW_SUB = ("FOR IDEAS, LESSONS, AND PERSPECTIVES THAT HELP YOU", "BECOME A BETTER VERSION OF YOURSELF.")


def s_title(d, t, dur):
    a = ramp(t, 0.1, 0.8) * (1 - ramp(t, dur - 0.5, 0.5))
    pill(d, W / 2, 380, "LANZOFOCUS", a, 24)
    l1, l2 = TITLE
    size = 120 if max(len(l1), len(l2)) <= 16 else 100
    d.text((W / 2, 520), l1, font=font(size), fill=col(WHITE, a), anchor="mm")
    d.text((W / 2, 660), l2, font=font(size), fill=col(WHITE, ramp(t, 0.5, 0.8) * (1 - ramp(t, dur - 0.5, 0.5))), anchor="mm")
    polyline(d, [(W / 2 - 260, 770), (W / 2 + 260, 770)], ramp(t, 0.9, 1.0), col(WHITE, a), 4)


def s_vote(d, t, dur):
    caption(d, ["EVERY CHOICE YOU MAKE", "IS A VOTE."], t, dur, accent={"VOTE"})
    # ballot box
    p = ramp(t, 0.2, 0.9)
    rrect(d, [W / 2 - 170, CY - 10, W / 2 + 170, CY + 230], 18, p)
    polyline(d, [(W / 2 - 80, CY + 40), (W / 2 + 80, CY + 40)], ramp(t, 0.8, 0.4), WHITE, 10)
    # card dropping in
    k = ramp(t, 1.0, 1.0)
    cy = lerp(CY - 260, CY - 30, k)
    a = ramp(t, 0.9, 0.3)
    sub = Image.new("RGBA", (W, H))
    sd = ImageDraw.Draw(sub)
    sd.rounded_rectangle([W / 2 - 70, cy - 90, W / 2 + 70, cy + 70], 10, fill=(0, 0, 0, 255), outline=col(WHITE, a), width=6)
    check(sd, W / 2, cy - 10, 1.4, ramp(t, 1.9, 0.5))
    # clip card into slot
    mask = Image.new("L", (W, H), 255)
    ImageDraw.Draw(mask).rectangle([0, CY + 40, W, H], fill=0)
    d._image.paste(sub, (0, 0), ImageChops.multiply(sub.getchannel("A"), mask))
    label(d, W / 2, CY + 280, "YOUR FUTURE", ramp(t, 1.5))


def s_today(d, t, dur):
    caption(d, ["NOT FOR WHAT", "YOU WANT TODAY…"], t, dur, accent={"TODAY"})
    a = ramp(t, 0.2)
    x0, y0 = W / 2 - 150, CY - 40
    d.rounded_rectangle([x0, y0, x0 + 300, y0 + 300], 26, outline=col(WHITE, a), width=7)
    d.rounded_rectangle([x0, y0, x0 + 300, y0 + 80], 26, fill=col(WHITE, a))
    d.rectangle([x0, y0 + 50, x0 + 300, y0 + 80], fill=col(WHITE, a))
    d.text((x0 + 150, y0 + 42), "TODAY", font=font(34), fill=(0, 0, 0, int(255 * a)), anchor="mm")
    fade = 1 - 0.6 * ramp(t, dur * 0.55, 0.8)
    d.text((x0 + 150, y0 + 190), "NOW", font=font(96), fill=col(WHITE, a * fade), anchor="mm")
    polyline(d, [(x0 - 40, y0 + 330), (x0 + 340, y0 - 30)], ramp(t, dur * 0.55, 0.6), (150, 150, 150, 255), 8)


def s_tomorrow(d, t, dur):
    caption(d, ["BUT FOR WHO YOU", "BECOME TOMORROW."], t, dur, accent={"TOMORROW", "BECOME"})
    base = CY + 200
    polyline(d, [(W / 2 - 500, base), (W / 2 + 500, base)], ramp(t, 0.1, 0.8), WHITE, 4)
    person(d, W / 2 - 280, base, 1.3, ramp(t, 0.3))
    label(d, W / 2 - 280, base + 40, "YOU", ramp(t, 0.5))
    polyline(d, [(W / 2 - 130, base - 90), (W / 2 + 130, base - 90)], ramp(t, 0.9, 0.8), WHITE, 4)
    polyline(d, [(W / 2 + 105, base - 110), (W / 2 + 130, base - 90), (W / 2 + 105, base - 70)], ramp(t, 1.6, 0.3), WHITE, 4)
    g = ramp(t, 1.4, 1.0)
    rrect(d, [W / 2 + 180, base - 340, W / 2 + 380, base], 100, ramp(t, 1.2, 0.8), WHITE, 5)
    dashed_person(d, W / 2 + 280, base - 20, 1.3, g)
    label(d, W / 2 + 280, base + 40, "FUTURE YOU", g)


def s_moment(d, t, dur):
    caption(d, ["YOU DON'T BECOME DISCIPLINED", "IN ONE MOMENT."], t, dur, accent={"DISCIPLINED"})
    # one big burst that fizzles
    cx, cy = W / 2, CY + 60
    a = ramp(t, 0.3, 0.4) * (1 - 0.75 * ramp(t, dur * 0.6, 0.8))
    for i in range(24):
        ang = math.radians(i * 15)
        r0 = 70 + 10 * ramp(t, 0.3, 0.6)
        r1 = r0 + lerp(10, 90, ramp(t, 0.3, 0.7))
        d.line([(cx + r0 * math.cos(ang), cy + r0 * math.sin(ang)), (cx + r1 * math.cos(ang), cy + r1 * math.sin(ang))], fill=col(WHITE, a), width=6)
    pill(d, cx, cy + 260, "ONE MOMENT", ramp(t, 0.6) * (1 - 0.6 * ramp(t, dur * 0.6, 0.8)), 24)


def s_choosing(d, t, dur):
    caption(d, ["YOU BECOME DISCIPLINED BY", "CHOOSING TO DO SOMETHING…"], t, dur, accent={"CHOOSING"})
    items = ["WAKE UP EARLY", "TRAIN", "READ 10 PAGES", "SAY NO"]
    x0, y0 = W / 2 - 230, CY - 60
    for i, it in enumerate(items):
        st = 0.3 + i * dur * 0.18
        a = ramp(t, st, 0.35)
        y = y0 + i * 80
        d.rounded_rectangle([x0, y, x0 + 50, y + 50], 8, outline=col(WHITE, a), width=5)
        if t > st + 0.3:
            d.rounded_rectangle([x0, y, x0 + 50, y + 50], 8, fill=col(WHITE, ramp(t, st + 0.3, 0.2)))
            check(d, x0 + 25, y + 26, 0.9, ramp(t, st + 0.35, 0.3), 7, (0, 0, 0, 255))
        d.text((x0 + 80, y + 25), it, font=font(40), fill=col(WHITE, a), anchor="lm")


def s_rather(d, t, dur):
    caption(d, ["WHEN YOU'D RATHER NOT."], t, dur, y=190, size=76)
    cx, cy = W / 2, CY + 40
    a = ramp(t, 0.2)
    shake = math.sin(t * 60) * 6 * (ramp(t, 0.6, 0.2) * (1 - ramp(t, 2.0, 0.3)))
    cx2 = cx + shake
    circle(d, cx2, cy, 150, ramp(t, 0.1, 0.8))
    for side in (-1, 1):
        d.arc([cx2 + side * 120 - 50, cy - 200, cx2 + side * 120 + 50, cy - 100], 180 if side < 0 else 270, 270 if side < 0 else 360, fill=col(WHITE, a), width=8)
        polyline(d, [(cx2 + side * 90, cy + 130), (cx2 + side * 130, cy + 190)], a, WHITE, 8)
    d.text((cx2, cy), "5:00", font=font(92), fill=col(WHITE, a), anchor="mm")
    label(d, cx2, cy + 75, "AM", a, 28)
    pill(d, cx, cy + 270, "SNOOZE?", ramp(t, 1.0) * 0.6, 24, inverted=False)


def s_waiting(d, t, dur):
    caption(d, ["YOU DON'T BECOME CONFIDENT", "BY WAITING UNTIL YOU'RE READY."], t, dur, accent={"CONFIDENT", "READY."})
    a = ramp(t, 0.2)
    x0, x1, y = W / 2 - 360, W / 2 + 360, CY + 80
    d.rounded_rectangle([x0, y - 34, x1, y + 34], 34, outline=col(WHITE, a), width=6)
    prog = 0.12 + 0.06 * math.sin(t * 2.5) * 0 + 0.07 * ramp(t, 0.4, 1.5)
    d.rounded_rectangle([x0 + 12, y - 22, x0 + 12 + (x1 - x0 - 24) * prog, y + 22], 22, fill=col(WHITE, a))
    label(d, W / 2, y - 90, "READY", a, 30)
    dots = "." * (1 + int(t * 2) % 3)
    label(d, W / 2, y + 90, f"LOADING{dots}", a * 0.8, 26, GREY)
    label(d, x1 - 40, y - 90, f"{int(prog * 100)}%", a, 30)


def gauge(d, cx, cy, r, val, a):
    d.arc([cx - r, cy - r, cx + r, cy + r], 180, 360, fill=col(WHITE, a), width=7)
    for i in range(11):
        ang = math.radians(180 + i * 18)
        r0 = r - (30 if i % 5 == 0 else 18)
        d.line([(cx + r0 * math.cos(ang), cy + r0 * math.sin(ang)), (cx + (r - 6) * math.cos(ang), cy + (r - 6) * math.sin(ang))], fill=col(WHITE, a), width=4)
    ang = math.radians(180 + 180 * val)
    d.line([(cx, cy), (cx + (r - 50) * math.cos(ang), cy + (r - 50) * math.sin(ang))], fill=col(WHITE, a), width=8)
    d.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], fill=col(WHITE, a))
    label(d, cx - r + 10, cy + 34, "LOW", a, 22, GREY)
    label(d, cx + r - 10, cy + 34, "HIGH", a, 22, GREY)
    label(d, cx, cy - r * 0.45, "CONFIDENCE", a, 24)


def s_scare(d, t, dur):
    caption(d, ["YOU BECOME CONFIDENT BY", "DOING THINGS THAT SCARE YOU…"], t, dur, accent={"SCARE"})
    base = CY + 180
    a = ramp(t, 0.2)
    polyline(d, [(W / 2 - 560, base), (W / 2 - 120, base), (W / 2 - 120, base + 200)], ramp(t, 0.1, 0.8), WHITE, 5)
    polyline(d, [(W / 2 + 560, base), (W / 2 + 120, base), (W / 2 + 120, base + 200)], ramp(t, 0.3, 0.8), WHITE, 5)
    k = ramp(t, 0.6, dur * 0.6)
    person(d, lerp(W / 2 - 420, W / 2 - 180, k), base, 1.2, a)
    pill(d, W / 2, base - 260, "FEAR", ramp(t, 1.0) * 0.9, 24, inverted=False)
    for i in range(3):  # gap shimmer
        y = base + 40 + i * 50
        dashed(d, [(W / 2 - 90, y), (W / 2 + 90, y)], col(DIM, a), 3, 14, 12)


def s_survived(d, t, dur):
    caption(d, ["AND REALIZING", "YOU SURVIVED."], t, dur, accent={"SURVIVED."})
    base = CY + 180
    polyline(d, [(W / 2 - 560, base), (W / 2 - 120, base), (W / 2 - 120, base + 200)], 1, WHITE, 5)
    polyline(d, [(W / 2 + 560, base), (W / 2 + 120, base), (W / 2 + 120, base + 200)], 1, WHITE, 5)
    k = ramp(t, 0.0, 0.9)
    x = lerp(W / 2 - 180, W / 2 + 260, k)
    hop = -math.sin(math.pi * k) * 170
    # dotted trail
    for i in range(14):
        f = i / 13
        if f > k:
            break
        px = lerp(W / 2 - 180, W / 2 + 260, f)
        py = base - 70 - math.sin(math.pi * f) * 170
        d.ellipse([px - 4, py - 4, px + 4, py + 4], fill=col(GREY, 1))
    person(d, x, base + hop, 1.2)
    pill(d, W / 2 + 260, base + 60, "YOU SURVIVED", ramp(t, 1.0), 24)


def s_wishing(d, t, dur):
    caption(d, ["AND YOU DON'T BECOME SUCCESSFUL", "BY WISHING YOUR LIFE WAS DIFFERENT."], t, dur, accent={"SUCCESSFUL", "WISHING"})
    base = CY + 220
    person(d, W / 2 - 220, base, 1.2, ramp(t, 0.2))
    polyline(d, [(W / 2 - 700, base), (W / 2 + 700, base)], ramp(t, 0.1, 0.8), WHITE, 4)
    # thought bubbles
    for i, (bx, by, r) in enumerate([(W / 2 - 160, CY + 30, 10), (W / 2 - 120, CY - 10, 16)]):
        a = ramp(t, 0.6 + i * 0.2, 0.3)
        d.ellipse([bx - r, by - r, bx + r, by + r], outline=col(WHITE, a), width=4)
    a = ramp(t, 1.0, 0.5)
    bx, by = W / 2 + 120, CY - 60
    d.rounded_rectangle([bx - 190, by - 110, bx + 190, by + 110], 60, outline=col(WHITE, a), width=5)
    # house + car icon inside (the dream)
    polyline(d, [(bx - 90, by + 50), (bx - 90, by - 10), (bx - 40, by - 60), (bx + 10, by - 10), (bx + 10, by + 50), (bx - 90, by + 50)], ramp(t, 1.2, 0.8), WHITE, 5)
    d.text((bx + 95, by), "$", font=font(90), fill=col(WHITE, ramp(t, 1.5, 0.5)), anchor="mm")
    # shooting star
    k = ramp(t, 1.8, 0.8)
    if 0 < k < 1:
        sx, sy = lerp(W / 2 + 700, W / 2 + 350, k), lerp(CY - 260, CY - 120, k)
        d.line([(sx, sy), (sx + 90, sy - 36)], fill=col(WHITE, 1 - k), width=4)


def s_choices(d, t, dur):
    caption(d, ["YOU BECOME SUCCESSFUL BY", "MAKING DIFFERENT CHOICES…"], t, dur, accent={"DIFFERENT"})
    sx, sy = W / 2 - 500, CY + 160
    jx = W / 2 - 100
    polyline(d, [(sx, sy), (jx, sy)], ramp(t, 0.1, 0.6), WHITE, 5)
    up = [(jx, sy), (jx + 160, sy - 150), (W / 2 + 500, sy - 150)]
    dn = [(jx, sy), (jx + 160, sy + 100), (W / 2 + 500, sy + 100)]
    polyline(d, dn, ramp(t, 0.6, 0.7), (110, 110, 110, 255), 5)
    polyline(d, up, ramp(t, 0.8, 0.7), WHITE, 5)
    label(d, W / 2 + 560, sy + 100, "EASY", ramp(t, 1.0), 24, GREY)
    label(d, W / 2 + 580, sy - 150, "HARD", ramp(t, 1.2), 24)
    k = ramp(t, 1.4, dur * 0.5)
    pts = [(sx + 80, sy), (jx, sy)] + up[1:]
    # position along path
    segs = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    L = sum(segs) * k
    px, py = pts[0]
    for i, s in enumerate(segs):
        if L <= s:
            f = L / s; px, py = lerp(pts[i][0], pts[i + 1][0], f), lerp(pts[i][1], pts[i + 1][1], f); break
        L -= s
        px, py = pts[i + 1]
    person(d, px, py - 6, 0.9, ramp(t, 0.3))


def s_watching(d, t, dur):
    caption(d, ["EVEN WHEN", "NOBODY'S WATCHING."], t, dur, accent={"NOBODY'S"})
    base = CY + 230
    a = ramp(t, 0.2)
    # spotlight cone
    cone = Image.new("RGBA", (W, H))
    ImageDraw.Draw(cone).polygon([(W / 2 - 60, CY - 160), (W / 2 + 60, CY - 160), (W / 2 + 230, base), (W / 2 - 230, base)], fill=(255, 255, 255, int(38 * a)))
    d._image.alpha_composite(cone.filter(ImageFilter.GaussianBlur(18)))
    d.rounded_rectangle([W / 2 - 70, CY - 190, W / 2 + 70, CY - 150], 10, fill=col(WHITE, a))
    polyline(d, [(W / 2 - 400, base), (W / 2 + 400, base)], a, WHITE, 4)
    person(d, W / 2, base, 1.3, a)
    # closed eye
    ex, ey = W / 2 - 520, CY - 40
    ea = ramp(t, 0.6)
    d.arc([ex - 70, ey - 50, ex + 70, ey + 50], 20, 160, fill=col(WHITE, ea), width=6)
    for i in (-1, 0, 1):
        d.line([(ex + i * 40, ey + 50), (ex + i * 48, ey + 75)], fill=col(WHITE, ea), width=5)
    d.text((W / 2 + 520, CY - 40), "5:06 AM", font=font(52), fill=col(WHITE, ramp(t, 0.8)), anchor="mm")


def s_eventually(d, t, dur):
    caption(d, ["BECAUSE EVENTUALLY…"], t, dur, y=190, size=76)
    cx, cy = W / 2, CY + 60
    a = ramp(t, 0.2)
    rot = 0
    hw, hh = 120, 170
    d.line([(cx - hw - 20, cy - hh), (cx + hw + 20, cy - hh)], fill=col(WHITE, a), width=8)
    d.line([(cx - hw - 20, cy + hh), (cx + hw + 20, cy + hh)], fill=col(WHITE, a), width=8)
    left = [(cx - hw, cy - hh), (cx - hw, cy - hh + 50), (cx - 12, cy - 10), (cx - 12, cy + 10), (cx - hw, cy + hh - 50), (cx - hw, cy + hh)]
    right = [(2 * cx - x, y) for x, y in left]
    polyline(d, left, a, WHITE, 6)
    polyline(d, right, a, WHITE, 6)
    k = clamp(t / max(dur, 0.1))
    top = lerp(cy - 40, cy - 10, k)
    d.polygon([(cx - lerp(80, 8, k), top - 40 * (1 - k)), (cx + lerp(80, 8, k), top - 40 * (1 - k)), (cx, cy - 8)], fill=col(WHITE, a))
    h = 100 * k
    d.polygon([(cx - hw + 15, cy + hh - 6), (cx + hw - 15, cy + hh - 6), (cx, cy + hh - 6 - h)], fill=col(WHITE, a))
    d.line([(cx, cy), (cx, cy + hh - 10)], fill=col(WHITE, a * 0.6), width=3)


def s_building(d, t, dur):
    caption(d, ["YOUR HABITS WILL INTRODUCE YOU TO", "THE PERSON YOU'VE BEEN BUILDING."], t, dur, accent={"HABITS", "BUILDING."})
    base = CY + 250
    bw, bh = 110, 46
    rows = 6
    n = 0
    total = sum(5 - (r % 2) for r in range(rows))
    for r in range(rows):
        cnt = 5 - (r % 2)
        y = base - (r + 1) * (bh + 8)
        x0 = W / 2 - 420 - (cnt * (bw + 8)) / 2
        for c in range(cnt):
            st = 0.2 + (dur * 0.65) * n / total
            k = ramp(t, st, 0.3)
            if k > 0:
                yy = y - (1 - k) * 60
                d.rounded_rectangle([x0 + c * (bw + 8), yy, x0 + c * (bw + 8) + bw, yy + bh], 6, outline=col(WHITE, k), width=4)
            n += 1
    polyline(d, [(W / 2 - 760, base), (W / 2 + 700, base)], ramp(t, 0.1), WHITE, 4)
    # the person emerging
    g = ramp(t, dur * 0.55, 1.0)
    person(d, W / 2 + 380, base, 1.7, g)
    dashed_person(d, W / 2 + 380, base, 1.7, 1 - g)
    label(d, W / 2 + 380, base + 44, "WHO YOU BUILT", ramp(t, 0.6))
    polyline(d, [(W / 2 - 120, base - 160), (W / 2 + 200, base - 160)], ramp(t, 0.8, 0.6), WHITE, 4)
    polyline(d, [(W / 2 + 175, base - 180), (W / 2 + 200, base - 160), (W / 2 + 175, base - 140)], ramp(t, 1.3, 0.3), WHITE, 4)


def mirror(d, t, a, faded):
    cx, base = W / 2 + 260, CY + 250
    d.rounded_rectangle([cx - 150, base - 400, cx + 150, base], 150, outline=col(WHITE, a), width=6)
    return cx, base


def s_recognize(d, t, dur):
    caption(d, ["AND YOU'LL EITHER", "RECOGNIZE THEM…"], t, dur, accent={"RECOGNIZE"})
    base = CY + 250
    a = ramp(t, 0.2)
    polyline(d, [(W / 2 - 600, base), (W / 2 + 600, base)], a, WHITE, 4)
    person(d, W / 2 - 260, base, 1.5, a)
    cx, _ = mirror(d, t, a, False)
    g = ramp(t, 0.6, 1.0)
    glow = 1 + 0.15 * math.sin(t * 3)
    person(d, cx, base - 40, 1.5, g)
    pill(d, cx, base - 450, "IT'S YOU", ramp(t, 1.2), 24)
    if g > 0.5:
        check(d, W / 2, CY - 20, 1.6 * glow, ramp(t, 1.4, 0.4), 8)


def s_chosen(d, t, dur):
    caption(d, ["OR WISH YOU HAD", "CHOSEN DIFFERENTLY."], t, dur, accent={"DIFFERENTLY."})
    base = CY + 250
    polyline(d, [(W / 2 - 600, base), (W / 2 + 600, base)], 1, WHITE, 4)
    person(d, W / 2 - 260, base, 1.5)
    cx, _ = mirror(d, t, 1, True)
    g = 1 - ramp(t, 0.3, 1.2)
    person(d, cx, base - 40, 1.5, g)
    dashed_person(d, cx, base - 40, 1.5, 1 - g, GREY)
    pill(d, cx, base - 450, "A STRANGER", ramp(t, 1.0) * 0.9, 24, inverted=False)
    d.text((W / 2, CY - 20), "?", font=font(110), fill=col(GREY, ramp(t, 1.2)), anchor="mm")


def s_follow(d, t, dur):
    a = ramp(t, 0.1, 0.6)
    d.text((W / 2, 330), "FOLLOW", font=font(70), fill=col((200, 200, 200, 255), a), anchor="mm")
    d.text((W / 2, 440), "LANZOFOCUS", font=font(150), fill=col(WHITE, ramp(t, 0.4, 0.6)), anchor="mm")
    sub = list(FOLLOW_SUB)
    caption(d, sub, t, dur, y=600, size=40, start=0.9, speak=min(0.7, 2.0 / max(dur, 0.1)))
    # follow button
    k = ramp(t, dur * 0.55, 0.5)
    bx, by = W / 2, 790
    d.rounded_rectangle([bx - 190, by - 46, bx + 190, by + 46], 46, fill=col(WHITE, k))
    d.text((bx, by), "+ FOLLOW", font=font(40), fill=(0, 0, 0, int(255 * k)), anchor="mm")
    # sprout
    s = ramp(t, 1.2, 1.2)
    polyline(d, [(W / 2 - 80, 910), (W / 2 + 80, 910)], s, WHITE, 4)


SCENES = [s_vote, s_today, s_tomorrow, s_moment, s_choosing, s_rather, s_waiting,
          s_scare, s_survived, s_wishing, s_choices, s_watching, s_eventually,
          s_building, s_recognize, s_chosen, s_follow]


# ---------------------------------------------------------------- compositing
def make_background():
    bg = Image.new("RGB", (W, H), (0, 0, 0))
    glow = Image.new("L", (W, H), 0)
    gd = ImageDraw.Draw(glow)
    gd.ellipse([W / 2 - 700, H / 2 - 480, W / 2 + 700, H / 2 + 480], fill=28)
    glow = glow.filter(ImageFilter.GaussianBlur(220))
    return Image.merge("RGB", (glow, glow, glow))


def main():
    global TITLE, SCENES
    timing = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    if len(sys.argv) > 3:  # project scenes module, e.g. projects/foo/scenes.py
        import importlib.util
        spec = importlib.util.spec_from_file_location("scenes", sys.argv[3])
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        SCENES = mod.SCENES
        TITLE = getattr(mod, "TITLE", TITLE)
        globals()["TITLE"] = TITLE
        globals()["FOLLOW_SUB"] = getattr(mod, "FOLLOW_SUB", FOLLOW_SUB)
        # scenes imported via `from render import ...` live in a second copy of this module
        if "render" in sys.modules:
            sys.modules["render"].TITLE = TITLE
            sys.modules["render"].FOLLOW_SUB = globals()["FOLLOW_SUB"]
    intro = timing["intro"]
    segs = timing["segments"]
    end = timing["end"]
    # scene windows: each scene runs from its segment start to the next segment start
    windows = [("title", 0.0, intro, s_title)]
    for i, fn in enumerate(SCENES):
        st = segs[i][0] - 0.15 if i else intro
        en = (segs[i + 1][0] - 0.15) if i + 1 < len(SCENES) else end
        windows.append((fn.__name__, st, en, fn))
    bg = make_background()
    wm_layer = Image.new("RGBA", (W, H))
    ImageDraw.Draw(wm_layer).text((W - 60, H - 50), "@lanzofocusjr", font=font(26, False), fill=(255, 255, 255, 150), anchor="rm")
    nframes = int(math.ceil(end * FPS))
    proc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                             "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for fi in range(nframes):
        T = fi / FPS
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        zoom = 1.0
        for name, st, en, fn in windows:
            if st <= T < en:
                fn(d, T - st, en - st)
                fade = min(ramp(T - st, 0, 0.25), 1 - ramp(T, en - 0.25, 0.25))
                zoom = 1.0 + CAMERA_PUSH * clamp((T - st) / max(0.1, en - st))
                break
        else:
            fade = 0
        if zoom > 1.0005:  # slow camera push-in towards the frame centre
            inv = 1 / zoom
            layer = layer.transform((W, H), Image.AFFINE, (inv, 0, W / 2 * (1 - inv), 0, inv, H / 2 * (1 - inv)), Image.BILINEAR)
        if fade < 1:
            layer.putalpha(layer.getchannel("A").point(lambda v, f=fade: int(v * f)))
        # glow: blurred copy of the white content added underneath
        small = layer.resize((W // 4, H // 4), Image.BILINEAR).filter(ImageFilter.GaussianBlur(6))
        glow = small.resize((W, H), Image.BILINEAR)
        frame = bg.copy().convert("RGBA")
        ga = glow.getchannel("A").point(lambda v: int(v * 0.9))
        glow.putalpha(ga)
        frame.alpha_composite(glow)
        frame.alpha_composite(layer)
        frame.alpha_composite(wm_layer)
        proc.stdin.write(frame.convert("RGB").tobytes())
        if fi % 150 == 0:
            print(f"frame {fi}/{nframes}", flush=True)
    proc.stdin.close()
    proc.wait()


if __name__ == "__main__":
    main()
