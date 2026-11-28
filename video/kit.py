"""Reusable LanzoFocus scene kit.

Describe a video as a list of (spoken line, motif name, options) and build() turns it into
LINES + SCENES for render.py. Captions are wrapped automatically; pass acc="WORD WORD" to highlight words.

    SPEC = [
        ("Every choice has a price.", "price_tag", dict(text="$ ?")),
        ...
    ]
    LINES, SCENES = build(SPEC)
"""
import math
from render import (W, H, CY, WHITE, GREY, DIM, font, clamp, ease, ramp, lerp, col, polyline, arc_pts, circle,
                    person, dashed_person, dashed, pill, label, check, caption, s_follow)

BLACK = (0, 0, 0, 255)
SOFT = (200, 200, 200, 255)


# ================================================================ caption helpers
def wrap(text, width=30):
    text = text.replace("**", "").upper().replace("’", "'").replace("...", "…")
    words = text.split()
    if len(text) <= 24:
        return [text]
    # split into two balanced lines (three if very long)
    n = 3 if len(text) > 66 else 2
    target = len(text) / n
    lines, cur = [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > target + 6 and len(lines) < n - 1:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    lines.append(cur)
    return lines


def make_caption(text, acc):
    lines = wrap(text)
    accent = None
    if acc:
        want = {w.upper() for w in acc.split()}
        # render.caption compares w.strip(".,…?"), so collect those stripped forms
        accent = {w.strip(".,…?") for ln in lines for w in ln.split()
                  if w.strip(".,…?!\"“”") in want}
    one = len(lines) == 1
    return lines, accent, one


# ================================================================ small drawing helpers
def base_line(d, t, y=CY + 240, half=560, a_start=0.0):
    polyline(d, [(W / 2 - half, y), (W / 2 + half, y)], ramp(t, a_start, 0.7), WHITE, 4)


def ftext(d, x, y, s, size=40, a=1.0, c=WHITE, anchor="mm", bold=True):
    d.text((x, y), s, font=font(size, bold), fill=col(c, a), anchor=anchor)


def bubble(d, cx, cy, text, a, size=30, inverted=False, tail=-1):
    f = font(size)
    tw = d.textlength(text, font=f)
    w, h = tw / 2 + 34, size * 1.2
    if inverted:
        d.rounded_rectangle([cx - w, cy - h, cx + w, cy + h], 22, fill=col(WHITE, a))
    else:
        d.rounded_rectangle([cx - w, cy - h, cx + w, cy + h], 22, outline=col(WHITE, a), width=5, fill=col(BLACK, a))
    tx = cx + tail * w * 0.5
    d.polygon([(tx - 14, cy + h - 3), (tx + 14, cy + h - 3), (tx - tail * 4, cy + h + 26)],
              fill=col(WHITE if inverted else WHITE, a))
    d.text((cx, cy), text, font=f, fill=(0, 0, 0, int(255 * a)) if inverted else col(WHITE, a), anchor="mm")


def trophy(d, tx, ty, a, c=WHITE):
    d.arc([tx - 60, ty - 60, tx + 60, ty + 60], 0, 180, fill=col(c, a), width=6)
    d.line([(tx - 60, ty), (tx + 60, ty)], fill=col(c, a), width=6)
    d.line([(tx, ty + 60), (tx, ty + 100)], fill=col(c, a), width=6)
    d.line([(tx - 40, ty + 100), (tx + 40, ty + 100)], fill=col(c, a), width=6)


def lock_icon(d, cx, cy, s, a, open_=0.0):
    d.rounded_rectangle([cx - 70 * s, cy - 10 * s, cx + 70 * s, cy + 100 * s], int(14 * s), outline=col(WHITE, a), width=6)
    lift = 40 * s * open_
    d.arc([cx - 45 * s, cy - 80 * s - lift, cx + 45 * s, cy + 10 * s - lift], 180, 360, fill=col(WHITE, a), width=6)
    d.line([(cx - 45 * s, cy - 35 * s - lift), (cx - 45 * s, cy - 10 * s - (lift if open_ else 0))], fill=col(WHITE, a), width=6)
    d.line([(cx + 45 * s, cy - 35 * s - lift), (cx + 45 * s, cy - 10 * s)], fill=col(WHITE, a), width=6)
    d.ellipse([cx - 10 * s, cy + 30 * s, cx + 10 * s, cy + 50 * s], fill=col(WHITE, a))


def brain_shape(d, cx, cy, s, a):
    for dx, dy, r in ((-60, -30, 70), (10, -60, 75), (80, -20, 65), (-40, 40, 60), (50, 45, 60)):
        d.ellipse([cx + (dx - r) * s, cy + (dy - r) * s, cx + (dx + r) * s, cy + (dy + r) * s], fill=col(BLACK, a), outline=col(WHITE, a), width=6)
    for dx, dy, r in ((-60, -30, 64), (10, -60, 69), (80, -20, 59), (-40, 40, 54), (50, 45, 54)):
        d.ellipse([cx + (dx - r) * s, cy + (dy - r) * s, cx + (dx + r) * s, cy + (dy + r) * s], fill=col(BLACK, a))
    d.line([(cx + 10 * s, cy - 120 * s), (cx + 10 * s, cy + 90 * s)], fill=col(WHITE, a * 0.6), width=4)
    for dx, dy in ((-60, -20), (60, 0), (-30, 50), (40, -70)):
        d.arc([cx + (dx - 25) * s, cy + (dy - 15) * s, cx + (dx + 25) * s, cy + (dy + 15) * s], 200, 340, fill=col(WHITE, a * 0.8), width=4)


def house_icon(d, cx, base, s, a, dashed_line=False, c=WHITE):
    w, h, roof = 150 * s, 150 * s, 100 * s
    pts = [(cx - w, base), (cx - w, base - h), (cx, base - h - roof), (cx + w, base - h), (cx + w, base), (cx - w, base)]
    if dashed_line:
        dashed(d, pts, col(c, a), 5, 18, 12)
    else:
        polyline(d, pts, a, c, 6)
        d.rectangle([cx - 30 * s, base - 80 * s, cx + 30 * s, base], fill=col(c, a))


def door_icon(d, cx, base, a, open_=0.0, lbl=None, c=WHITE):
    w, h = 130, 300
    d.rectangle([cx - w / 2, base - h, cx + w / 2, base], outline=col(c, a), width=6)
    # door leaf swings: drawn as a quadrilateral narrowing to the hinge side
    leaf = w * (1 - 0.8 * open_)
    skew = 30 * open_
    d.polygon([(cx - w / 2, base - h), (cx - w / 2 + leaf, base - h + skew), (cx - w / 2 + leaf, base - skew), (cx - w / 2, base)],
              outline=col(c, a), fill=col(c if open_ < 0.5 else BLACK, a * (0.9 if open_ < 0.5 else 1)))
    if open_ >= 0.5:
        d.polygon([(cx - w / 2, base - h), (cx - w / 2 + leaf, base - h + skew), (cx - w / 2 + leaf, base - skew), (cx - w / 2, base)], outline=col(c, a), width=5)
    if lbl:
        label(d, cx, base + 40, lbl, a, 24, c)


# ================================================================ motifs
# every motif: f(d, t, dur, **kw)

def m_big(d, t, dur, text="", sub=None, **k):
    """A big centred word or phrase as the visual."""
    a = ramp(t, 0.3, 0.6)
    size = 140 if len(text) <= 10 else 100
    ftext(d, W / 2, CY + 60, text, size, a)
    polyline(d, [(W / 2 - 220, CY + 160), (W / 2 + 220, CY + 160)], ramp(t, 0.7, 0.6), WHITE, 4)
    if sub:
        label(d, W / 2, CY + 210, sub, ramp(t, 0.9), 28, GREY)


def m_quote(d, t, dur, text="", **k):
    """Speech bubble from a figure."""
    base = CY + 250
    person(d, W / 2 - 260, base, 1.4, ramp(t, 0.1))
    base_line(d, t, base, 480)
    bubble(d, W / 2 + 60, CY - 20, text, ramp(t, 0.4), 40, tail=-1)


def m_bubbles(d, t, dur, texts=(), center="person", inverted=False, **k):
    base = CY + 250
    if center == "person":
        person(d, W / 2, base, 1.4, ramp(t, 0.1))
        base_line(d, t, base, 420)
    elif center == "brain":
        brain_shape(d, W / 2, CY + 120, 1.0, ramp(t, 0.1))
    pos = [(W / 2 - 430, CY - 10), (W / 2 + 430, CY - 10), (W / 2 - 470, CY + 150), (W / 2 + 470, CY + 150), (W / 2, CY - 60)]
    for i, tx in enumerate(texts):
        x, y = pos[i % len(pos)]
        bubble(d, x, y, tx, ramp(t, 0.3 + i * 0.3, 0.35), 30, inverted, tail=1 if x < W / 2 else -1)


def m_crowd(d, t, dur, n=9, highlight=None, highlight_label=None, dim=False, faces=None, **k):
    base = CY + 250
    base_line(d, t, base, 640)
    for i in range(n):
        x = W / 2 + (i - (n - 1) / 2) * 120
        a = ramp(t, 0.1 + i * 0.05)
        c = GREY if (highlight is not None and i != highlight) or dim else WHITE
        person(d, x, base, 0.9, a, c)
    if highlight is not None:
        x = W / 2 + (highlight - (n - 1) / 2) * 120
        if highlight_label:
            pill(d, x, base - 220, highlight_label, ramp(t, 0.8), 22)


def m_alone(d, t, dur, tag=None, others=0, **k):
    """A single figure; optional label pill; faded others far away."""
    base = CY + 250
    base_line(d, t, base, 620)
    person(d, W / 2, base, 1.5, ramp(t, 0.2))
    for i in range(others):
        side = -1 if i % 2 == 0 else 1
        person(d, W / 2 + side * (420 + 80 * (i // 2)), base, 0.8, ramp(t, 0.4) * 0.5, GREY)
    if tag:
        pill(d, W / 2, base - 300, tag, ramp(t, 0.7), 26)


def m_sticker(d, t, dur, tags=(), strike=False, **k):
    """Figure with labels stuck onto it (identity)."""
    base = CY + 250
    base_line(d, t, base, 520)
    person(d, W / 2, base, 1.6, ramp(t, 0.1))
    pos = [(W / 2 - 300, CY + 20), (W / 2 + 300, CY + 20), (W / 2 - 330, CY + 150), (W / 2 + 330, CY + 150), (W / 2, CY - 110)]
    for i, tg in enumerate(tags):
        x, y = pos[i % len(pos)]
        a = ramp(t, 0.4 + i * 0.3, 0.3)
        pill(d, x, y, tg, a, 26, inverted=True)
        dashed(d, [(x + (60 if x < W / 2 else -60), y + 10), (W / 2 + (-40 if x < W / 2 else 40), base - 90)], col(GREY, a), 3, 10, 8)
        if strike:
            sa = ramp(t, dur * 0.5 + i * 0.15, 0.3)
            polyline(d, [(x - 110, y), (x + 110, y)], sa, (90, 90, 90, 255), 6)


def m_list(d, t, dur, items=(), mode="check", tag=None, **k):
    """Vertical list; mode: check | empty | tag | strike."""
    n = len(items)
    x0 = W / 2 - 330
    y0 = CY + 70 - (n - 1) * 45
    step = min(0.4, max(0.15, dur * 0.5 / max(1, n)))
    for i, it in enumerate(items):
        st = 0.2 + i * step
        a = ramp(t, st, 0.3)
        y = y0 + i * 90
        d.rounded_rectangle([x0, y - 25, x0 + 50, y + 25], 8, outline=col(WHITE, a), width=5)
        if mode == "check" and t > st + 0.25:
            d.rounded_rectangle([x0, y - 25, x0 + 50, y + 25], 8, fill=col(WHITE, a))
            check(d, x0 + 25, y + 1, 0.9, ramp(t, st + 0.3, 0.3), 7, BLACK)
        ftext(d, x0 + 80, y, it, 40, a, anchor="lm")
        if mode == "strike":
            polyline(d, [(x0 + 70, y), (x0 + 90 + d.textlength(it, font=font(40)), y)], ramp(t, st + 0.4, 0.3), (150, 150, 150, 255), 6)
        if mode == "tag" and tag:
            pill(d, x0 + 640, y, tag, ramp(t, st + 0.3, 0.3) * 0.85, 22, inverted=False)


def m_price(d, t, dur, text="$ ?", sub=None, **k):
    """Price tag swinging on a string."""
    a = ramp(t, 0.2)
    sway = math.sin(t * 2) * 6
    size = 70 if len(text) < 8 else 46
    tw = d.textlength(text, font=font(size))
    half = max(150, tw / 2 + 50)
    cx, cy = W / 2 + sway, CY + 80
    left, right = cx - half - 30, cx + half + 50
    d.line([(W / 2, CY - 160), (left + 40, cy - 60)], fill=col(GREY, a), width=3)
    pts = [(left, cy), (left + 60, cy - 80), (right, cy - 80), (right, cy + 80), (left + 60, cy + 80)]
    d.polygon(pts, outline=col(WHITE, a), fill=col(BLACK, a))
    polyline(d, pts + [pts[0]], a, WHITE, 6)
    d.ellipse([left + 35, cy - 15, left + 65, cy + 15], outline=col(WHITE, a), width=5)
    ftext(d, (left + 80 + right) / 2, cy, text, size, ramp(t, 0.5))
    if sub:
        label(d, W / 2, cy + 150, sub, ramp(t, 0.8), 26, GREY)


def m_receipt(d, t, dur, items=(), total="", **k):
    a = ramp(t, 0.1)
    x0, x1 = W / 2 - 230, W / 2 + 230
    y0 = CY - 120
    h = 130 + 70 * len(items) + 90
    reveal = ramp(t, 0.1, 0.8)
    y1 = y0 + h * reveal
    zig = [(x0, y1)]
    for i in range(12):
        zig.append((lerp(x0, x1, (i + 0.5) / 12), y1 + 14))
        zig.append((lerp(x0, x1, (i + 1) / 12), y1))
    polyline(d, [(x0, y1), (x0, y0), (x1, y0), (x1, y1)], a, WHITE, 5)
    polyline(d, zig, a, WHITE, 5)
    ftext(d, W / 2, y0 + 50, "RECEIPT", 34, a * reveal)
    for i, (name, price) in enumerate(items):
        y = y0 + 130 + i * 70
        if y < y1 - 20:
            ia = ramp(t, 0.5 + i * 0.3, 0.3)
            ftext(d, x0 + 30, y, name, 30, ia, anchor="lm")
            ftext(d, x1 - 30, y, price, 30, ia, GREY, anchor="rm")
    if total:
        y = y0 + 130 + len(items) * 70 + 20
        if y < y1:
            dashed(d, [(x0 + 30, y - 30), (x1 - 30, y - 30)], col(GREY, a), 3, 10, 8)
            ta = ramp(t, 0.6 + len(items) * 0.3, 0.3)
            ftext(d, x0 + 30, y + 10, "TOTAL", 34, ta, anchor="lm")
            ftext(d, x1 - 30, y + 10, total, 34, ta, anchor="rm")


def m_chart(d, t, dur, kind="up", lbl=None, lbl2=None, **k):
    """Line chart: up | flat | wave | down | invest (dip then up)."""
    x0, x1, base = W / 2 - 600, W / 2 + 600, CY + 270
    a = ramp(t, 0.1)
    polyline(d, [(x0, base), (x1, base)], a, DIM, 3)
    polyline(d, [(x0, base), (x0, CY - 120)], a, DIM, 3)
    pts = []
    for i in range(0, 121):
        f = i / 120
        if kind == "up":
            y = base - 40 - 330 * f ** 1.8
        elif kind == "flat":
            y = base - 120 + 6 * math.sin(f * 30)
        elif kind == "down":
            y = CY - 60 + 300 * f ** 1.2
        elif kind == "invest":
            y = base - 120 + 60 * math.sin(f * math.pi * 1.2) * (1 - f) - 300 * max(0, f - 0.45) ** 1.6 * 2.2
        else:
            y = base - 180 + 120 * (0.6 * math.sin(f * 11) + 0.4 * math.sin(f * 27 + 1.7))
        pts.append((lerp(x0, x1, f), y))
    polyline(d, pts, ramp(t, 0.3, max(0.8, dur * 0.7)), WHITE, 6)
    if lbl:
        label(d, x0 + 20, CY - 150, lbl, a, 24, GREY if kind == "flat" else WHITE)
    if lbl2:
        label(d, x1 - 60, base + 36, lbl2, a, 22, GREY)


def m_coins(d, t, dur, stacks=5, lbl="FUTURE", **k):
    base = CY + 260
    base_line(d, t, base, 520)
    for i in range(stacks):
        x = W / 2 - 360 + i * 180
        n = 2 + i * 2
        for j in range(n):
            st = 0.2 + (i * 0.25) + j * 0.05
            if t > st:
                y = base - 10 - j * 26
                d.ellipse([x - 60, y - 16, x + 60, y + 16], fill=col(BLACK, 1), outline=col(WHITE, ramp(t, st, 0.2)), width=5)
    pill(d, W / 2 + 360, base - 380, lbl, ramp(t, 1.4), 24)


def m_scale(d, t, dur, left="COMFORT", right="GROWTH", tip=-1, **k):
    """Balance scale; tip = -1 left heavier, 1 right heavier, 0 level."""
    cx, top = W / 2, CY - 60
    a = ramp(t, 0.1)
    ang = tip * 0.18 * ramp(t, 0.6, 0.8)
    d.line([(cx, top), (cx, CY + 250)], fill=col(WHITE, a), width=7)
    d.line([(cx - 120, CY + 250), (cx + 120, CY + 250)], fill=col(WHITE, a), width=7)
    L = 380
    lx, ly = cx - L * math.cos(ang), top - L * math.sin(ang) * -1
    rx, ry = cx + L * math.cos(ang), top + L * math.sin(ang) * -1
    ly, ry = top + L * math.sin(-ang) * -1, top - L * math.sin(-ang) * -1
    d.line([(lx, ly), (rx, ry)], fill=col(WHITE, a), width=7)
    for x, y, txt in ((lx, ly, left), (rx, ry, right)):
        d.line([(x, y), (x - 90, y + 140)], fill=col(WHITE, a), width=3)
        d.line([(x, y), (x + 90, y + 140)], fill=col(WHITE, a), width=3)
        d.arc([x - 110, y + 90, x + 110, y + 190], 0, 180, fill=col(WHITE, a), width=6)
        label(d, x, y + 230, txt, ramp(t, 0.4), 26)
    d.ellipse([cx - 16, top - 16, cx + 16, top + 16], fill=col(WHITE, a))


def m_door(d, t, dur, open_=False, closing=False, lbl=None, figure=True, **k):
    base = CY + 250
    base_line(d, t, base, 560)
    if closing:
        o = 1 - ramp(t, 0.6, 1.0)
    elif open_:
        o = ramp(t, 0.6, 1.0)
    else:
        o = 0
    door_icon(d, W / 2 + 180, base, ramp(t, 0.2), o, lbl)
    if o > 0.3:
        glow = ramp(t, 0.8)
        d.polygon([(W / 2 + 115, base - 300), (W / 2 + 115, base), (W / 2 - 150, base + 0)], fill=(255, 255, 255, int(25 * glow * o)))
    if figure:
        person(d, W / 2 - 220, base, 1.3, ramp(t, 0.1))


def m_brain(d, t, dur, says=None, says2=None, **k):
    brain_shape(d, W / 2 - 220, CY + 110, 1.15, ramp(t, 0.1))
    if says:
        bubble(d, W / 2 + 260, CY - 20, says, ramp(t, 0.6), 34, tail=-1)
    if says2:
        bubble(d, W / 2 + 300, CY + 170, says2, ramp(t, 1.1), 30, tail=-1)


def m_gauge(d, t, dur, lbl="CONFIDENCE", start=0.1, end=0.1, **k):
    cx, cy, r = W / 2, CY + 200, 260
    a = ramp(t, 0.1)
    d.arc([cx - r, cy - r, cx + r, cy + r], 180, 360, fill=col(WHITE, a), width=8)
    for i in range(11):
        ang = math.radians(180 + i * 18)
        r0 = r - (34 if i % 5 == 0 else 20)
        d.line([(cx + r0 * math.cos(ang), cy + r0 * math.sin(ang)), (cx + (r - 8) * math.cos(ang), cy + (r - 8) * math.sin(ang))], fill=col(WHITE, a), width=4)
    v = lerp(start, end, ramp(t, 0.6, 1.2))
    ang = math.radians(180 + 180 * v)
    d.line([(cx, cy), (cx + (r - 60) * math.cos(ang), cy + (r - 60) * math.sin(ang))], fill=col(WHITE, a), width=9)
    d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=col(WHITE, a))
    label(d, cx, cy - r * 0.42, lbl, a, 28)
    label(d, cx - r + 10, cy + 36, "LOW", a, 22, GREY)
    label(d, cx + r - 10, cy + 36, "HIGH", a, 22, GREY)


def m_lock(d, t, dur, lbl="CERTAINTY", opening=False, **k):
    o = ramp(t, 0.8, 0.6) if opening else 0
    lock_icon(d, W / 2, CY + 40, 1.6, ramp(t, 0.1), o)
    label(d, W / 2, CY + 260, lbl, ramp(t, 0.4), 28)


def m_doc(d, t, dur, title="PROOF", empty=True, stamp=None, **k):
    a = ramp(t, 0.1)
    x0, y0, x1, y1 = W / 2 - 190, CY - 140, W / 2 + 190, CY + 290
    d.polygon([(x0, y0), (x1 - 70, y0), (x1, y0 + 70), (x1, y1), (x0, y1)], outline=col(WHITE, a), fill=col(BLACK, a))
    polyline(d, [(x0, y0), (x1 - 70, y0), (x1, y0 + 70), (x1, y1), (x0, y1), (x0, y0)], a, WHITE, 6)
    polyline(d, [(x1 - 70, y0), (x1 - 70, y0 + 70), (x1, y0 + 70)], a, WHITE, 5)
    ftext(d, W / 2 - 30, y0 + 70, title, 40 if len(title) <= 8 else 28, a)
    for i in range(5):
        y = y0 + 150 + i * 46
        if empty:
            dashed(d, [(x0 + 40, y), (x1 - 40, y)], col(DIM, a), 4, 14, 12)
        else:
            polyline(d, [(x0 + 40, y), (x1 - 40 - (i % 2) * 80, y)], ramp(t, 0.4 + i * 0.1, 0.3), WHITE, 5)
    if stamp:
        sa = ramp(t, 1.2, 0.3)
        pill(d, W / 2, y1 - 70, stamp, sa, 30, inverted=False)


def m_path(d, t, dur, kind="fork", walker=True, labels=("EASY", "HARD"), fog=False, **k):
    """Paths: fork | straight | winding | dashed (unknown ahead)."""
    base = CY + 200
    x0 = W / 2 - 600
    if kind == "fork":
        jx = W / 2 - 120
        polyline(d, [(x0, base), (jx, base)], ramp(t, 0.1, 0.6), WHITE, 5)
        polyline(d, [(jx, base), (jx + 160, base + 100), (W / 2 + 600, base + 100)], ramp(t, 0.5, 0.6), GREY, 5)
        polyline(d, [(jx, base), (jx + 160, base - 150), (W / 2 + 600, base - 150)], ramp(t, 0.7, 0.6), WHITE, 5)
        label(d, W / 2 + 540, base + 140, labels[0], ramp(t, 0.9), 24, GREY)
        label(d, W / 2 + 540, base - 190, labels[1], ramp(t, 1.0), 24)
        if walker:
            person(d, lerp(x0 + 60, jx - 40, ramp(t, 0.3, 1.2)), base, 0.9, ramp(t, 0.2))
    elif kind == "winding":
        pts = [(lerp(x0, W / 2 + 600, i / 80), base + 90 * math.sin(i / 80 * 4 * math.pi) * (1 - i / 80)) for i in range(81)]
        polyline(d, pts, ramp(t, 0.1, 1.0), WHITE, 5)
        if walker:
            i = int(80 * ramp(t, 0.4, max(1.0, dur * 0.8)))
            person(d, pts[i][0], pts[i][1], 0.8, ramp(t, 0.2))
    else:
        mid = W / 2 - 80
        polyline(d, [(x0, base), (mid, base)], ramp(t, 0.1, 0.6), WHITE, 5)
        dashed(d, [(mid, base), (W / 2 + 600, base)], col(GREY if kind == "dashed" else WHITE, ramp(t, 0.5)), 5, 20, 14)
        if fog:
            for i in range(5):
                fx = mid + 140 + i * 80
                dashed(d, [(fx, base - 200), (fx, base - 20)], col(DIM, ramp(t, 0.6)), 3, 10, 14)
        if walker:
            k2 = ramp(t, 0.3, max(1.0, dur * 0.7))
            person(d, lerp(x0 + 80, mid + (120 if kind == "dashed" else 400), k2), base, 1.0, ramp(t, 0.2))


def m_stairs(d, t, dur, n=6, climb=0, highlight=None, **k):
    base = CY + 270
    x0 = W / 2 - 360
    sw, sh = 140, 70
    pts = [(x0 - 200, base)]
    for i in range(n):
        x = x0 + i * sw
        pts += [(x, base - i * sh), (x, base - (i + 1) * sh)]
    pts.append((x0 + n * sw, base - n * sh))
    polyline(d, pts, ramp(t, 0.1, 0.9), WHITE, 6)
    if highlight is not None:
        x = x0 + highlight * sw
        d.rectangle([x, base - (highlight + 1) * sh, x + sw, base - highlight * sh], fill=col(WHITE, 0.25 * ramp(t, 0.6)))
        pill(d, x + sw / 2, base - (highlight + 1) * sh - 250, "NEXT STEP", ramp(t, 0.8), 22)
    kk = ramp(t, 0.5, max(0.8, dur * 0.6)) * climb
    step = int(kk)
    frac = kk - step
    x = x0 - 90 + (step + frac) * sw + (sw / 2 if step + frac > 0 else 0)
    y = base - min(n, step + frac) * sh - math.sin(math.pi * frac) * 40
    person(d, min(x, x0 + n * sw - 60), y, 1.0, ramp(t, 0.2))


def m_timeline(d, t, dur, n=8, progress=0.5, tag=None, slow=False, compare=False, **k):
    y = CY + 160
    x0, x1 = W / 2 - 620, W / 2 + 620
    a = ramp(t, 0.1)
    if compare:
        for row, (ty, pr, lb, c) in enumerate(((y - 120, 0.85, "THEM", GREY), (y + 80, 0.35, "YOU", WHITE))):
            polyline(d, [(x0, ty), (x1, ty)], a, c, 4)
            label(d, x0 - 10, ty - 40, lb, a, 24, c)
            px = lerp(x0 + 60, x1 - 60, pr * ramp(t, 0.3, 1.0))
            person(d, px, ty - 10, 0.75, a, c)
        return
    polyline(d, [(x0, y), (x1, y)], ramp(t, 0.1, 0.8), WHITE, 4)
    polyline(d, [(x1 - 30, y - 22), (x1, y), (x1 - 30, y + 22)], ramp(t, 0.8, 0.3), WHITE, 4)
    sp = (0.15 if slow else 1.0)
    k2 = clamp(progress * ramp(t, 0.3, max(1.0, dur * 0.8)) * (1 if not slow else 1))
    for i in range(n):
        px = lerp(x0 + 80, x1 - 120, i / (n - 1))
        fill = WHITE if lerp(x0 + 80, x1 - 120, k2) >= px else DIM
        d.ellipse([px - 10, y - 10, px + 10, y + 10], fill=col(fill, a))
    px = lerp(x0 + 80, x1 - 120, k2)
    person(d, px, y - 18, 1.0, a)
    if tag:
        pill(d, px, y + 70, tag, ramp(t, 1.0), 22)


def m_phone(d, t, dur, content="highlight", lbl=None, **k):
    a = ramp(t, 0.1)
    cx, cy = W / 2 + (180 if lbl else 0), CY + 70
    d.rounded_rectangle([cx - 150, cy - 270, cx + 150, cy + 270], 40, outline=col(WHITE, a), width=7)
    d.rounded_rectangle([cx - 40, cy - 250, cx + 40, cy - 236], 7, fill=col(WHITE, a))
    if content == "highlight":
        d.rounded_rectangle([cx - 115, cy - 200, cx + 115, cy + 40], 16, outline=col(WHITE, a), width=4)
        trophy(d, cx, cy - 110, ramp(t, 0.4))
        for i in range(5):
            sx = cx - 80 + i * 40
            st = ramp(t, 0.6 + i * 0.1, 0.2)
            pts = [(sx + 14 * math.cos(math.radians(-90 + j * 36)) * (1 if j % 2 == 0 else 0.45),
                    cy + 90 + 14 * math.sin(math.radians(-90 + j * 36)) * (1 if j % 2 == 0 else 0.45)) for j in range(10)]
            d.polygon(pts, fill=col(WHITE, st))
        ftext(d, cx, cy + 160, "♥ 98.4K", 30, ramp(t, 0.9))
    if lbl:
        person(d, W / 2 - 300, CY + 280, 1.3, ramp(t, 0.2), GREY)
        label(d, W / 2 - 300, CY + 320, lbl, ramp(t, 0.5), 24, GREY)


def m_iceberg(d, t, dur, top="WHAT YOU SEE", bottom="WHAT YOU DON'T", **k):
    wl = CY + 30
    a = ramp(t, 0.1)
    dashed(d, [(W / 2 - 640, wl), (W / 2 + 640, wl)], col(GREY, a), 3, 22, 14)
    polyline(d, [(W / 2 - 110, wl), (W / 2 - 30, wl - 120), (W / 2 + 40, wl - 70), (W / 2 + 120, wl)], ramp(t, 0.2, 0.6), WHITE, 6)
    polyline(d, [(W / 2 - 110, wl), (W / 2 - 330, wl + 140), (W / 2 - 220, wl + 320), (W / 2 + 60, wl + 370),
                 (W / 2 + 320, wl + 250), (W / 2 + 280, wl + 90), (W / 2 + 120, wl)], ramp(t, 0.8, 1.2), WHITE, 6)
    label(d, W / 2 + 360, wl - 60, top, ramp(t, 0.6), 24, GREY)
    label(d, W / 2 - 10, wl + 210, bottom, ramp(t, 1.6), 28)


def m_network(d, t, dur, nodes=(), focus=None, tangled=True, **k):
    cx, cy = W / 2, CY + 110
    n = len(nodes)
    pos = []
    for i in range(n):
        ang = math.radians(-90 + i * 360 / n)
        pos.append((cx + 470 * math.cos(ang), cy + 210 * math.sin(ang)))
    a = ramp(t, 0.1)
    if tangled:
        for i in range(n):
            for j in range(i + 1, n):
                la = ramp(t, 0.3 + 0.05 * (i + j), 0.3) * (0.25 if focus is not None else 0.7)
                d.line([pos[i], pos[j]], fill=col(WHITE, la), width=2)
    person(d, cx, cy + 70, 1.0, a)
    for i, (nm, (x, y)) in enumerate(zip(nodes, pos)):
        na = ramp(t, 0.2 + i * 0.1, 0.3)
        if focus is not None and i != focus:
            na *= 0.35
        pill(d, x, y, nm, na, 24, inverted=(focus == i))
    if focus is not None:
        polyline(d, [(cx, cy - 30), pos[focus]], ramp(t, 0.6, 0.5), WHITE, 5)


def m_plant(d, t, dur, roots=True, height=0.3, lbl=None, **k):
    gy = CY + 120
    a = ramp(t, 0.1)
    polyline(d, [(W / 2 - 600, gy), (W / 2 + 600, gy)], a, WHITE, 4)
    h = 60 + 240 * height * ramp(t, 0.3, 1.0)
    d.line([(W / 2, gy), (W / 2, gy - h)], fill=col(WHITE, a), width=6)
    d.ellipse([W / 2 - 60, gy - h - 10, W / 2, gy - h + 30], outline=col(WHITE, a), width=5)
    d.ellipse([W / 2, gy - h - 30, W / 2 + 60, gy - h + 10], outline=col(WHITE, a), width=5)
    if roots:
        rr = ramp(t, 0.5, max(1.0, dur * 0.7))
        for ang, ln in ((-60, 260), (-100, 300), (-130, 220), (-30, 200), (-80, 180)):
            pts = [(W / 2, gy)]
            for j in range(1, 8):
                f = j / 7
                pts.append((W / 2 + math.cos(math.radians(ang + 90 + 10 * math.sin(j))) * ln * f * 0.9,
                            gy + abs(math.sin(math.radians(ang))) * ln * f * 0.8))
            polyline(d, pts, rr, (170, 170, 170, 255), 4)
        label(d, W / 2 + 420, gy + 160, lbl or "WHAT NOBODY SEES", ramp(t, 1.0), 24, GREY)


def m_book(d, t, dur, chapter="CHAPTER 3", text=None, **k):
    a = ramp(t, 0.1)
    cx, cy = W / 2, CY + 100
    for side in (-1, 1):
        pts = [(cx, cy - 150), (cx + side * 300, cy - 180), (cx + side * 300, cy + 140), (cx, cy + 170), (cx, cy - 150)]
        polyline(d, pts, ramp(t, 0.1, 0.8), WHITE, 6)
        for i in range(5):
            y = cy - 100 + i * 50
            polyline(d, [(cx + side * 40, y), (cx + side * (260 - (i % 2) * 60), y - 20 * 0)], ramp(t, 0.5 + i * 0.1, 0.3), DIM, 4)
    ftext(d, cx, cy - 250, chapter, 36, ramp(t, 0.4))
    if text:
        pill(d, cx, cy + 240, text, ramp(t, 0.9), 24)


def m_chairs(d, t, dur, n=7, lbl="NOBODY WATCHING", **k):
    base = CY + 260
    for r in range(2):
        for i in range(n):
            x = W / 2 + (i - (n - 1) / 2) * 140 + r * 70
            y = base - r * 120
            a = ramp(t, 0.1 + (i + r) * 0.05) * (0.6 if r else 1)
            d.line([(x - 40, y), (x - 40, y - 60), (x + 30, y - 60)], fill=col(WHITE, a), width=5)
            d.line([(x - 40, y - 60), (x - 40, y - 130)], fill=col(WHITE, a), width=5)
            d.line([(x + 30, y - 60), (x + 30, y)], fill=col(WHITE, a), width=5)
    pill(d, W / 2, CY - 60, lbl, ramp(t, 0.8) * 0.9, 24, inverted=False)


def m_frame(d, t, dur, who="OLD YOU", dashed_fig=False, fade=False, **k):
    a = ramp(t, 0.1)
    cx, cy = W / 2 - (260 if k.get("new") else 0), CY + 90
    d.rectangle([cx - 200, cy - 230, cx + 200, cy + 210], outline=col(WHITE, a), width=8)
    d.rectangle([cx - 170, cy - 200, cx + 170, cy + 180], outline=col(GREY, a), width=3)
    f = 1 - (0.7 * ramp(t, dur * 0.4, 1.0) if fade else 0)
    if dashed_fig:
        dashed_person(d, cx, cy + 150, 1.6, a * f, GREY)
    else:
        person(d, cx, cy + 150, 1.6, a * f, GREY)
    label(d, cx, cy + 250, who, a, 24, GREY)
    if k.get("new"):
        base = cy + 210
        person(d, W / 2 + 330, base, 1.7, ramp(t, 0.6))
        label(d, W / 2 + 330, base + 40, k["new"], ramp(t, 0.8), 24)


def m_shed(d, t, dur, old="OLD YOU", new="YOU NOW", **k):
    """Old dashed self left behind, new self stepping forward."""
    base = CY + 250
    base_line(d, t, base, 600)
    k2 = ramp(t, 0.4, 1.4)
    dashed_person(d, W / 2 - 200, base, 1.5, 1 - 0.5 * k2, GREY)
    label(d, W / 2 - 200, base + 40, old, ramp(t, 0.3), 24, GREY)
    person(d, lerp(W / 2 - 200, W / 2 + 250, k2), base, 1.5, ramp(t, 0.2))
    label(d, W / 2 + 250, base + 40, new, ramp(t, 1.4), 24)


def m_arrows(d, t, dur, items=(), **k):
    """Labels with arrows turning from one direction to a new one."""
    x0 = W / 2 - 380
    n = len(items)
    y0 = CY + 70 - (n - 1) * 50
    for i, it in enumerate(items):
        y = y0 + i * 100
        a = ramp(t, 0.2 + i * 0.25, 0.3)
        ftext(d, x0, y, it, 40, a, anchor="lm")
        turn = ramp(t, 0.5 + i * 0.25, 0.5)
        ang = math.radians(lerp(180, -25, turn))
        ax = W / 2 + 280
        L = 110
        ex, ey = ax + L * math.cos(ang), y + L * math.sin(ang)
        d.line([(ax, y), (ex, ey)], fill=col(WHITE, a), width=6)
        for s in (-1, 1):
            hb = ang + math.pi + s * 0.5
            d.line([(ex, ey), (ex + 26 * math.cos(hb), ey + 26 * math.sin(hb))], fill=col(WHITE, a), width=6)


def m_startline(d, t, dur, behind=True, **k):
    base = CY + 250
    base_line(d, t, base, 640)
    d.line([(W / 2 - 300, base - 160), (W / 2 - 300, base + 20)], fill=col(WHITE, ramp(t, 0.2)), width=5)
    label(d, W / 2 - 300, base + 50, "START", ramp(t, 0.3), 22, GREY)
    for i in range(4):
        person(d, W / 2 + 60 + i * 150, base, 0.9, ramp(t, 0.3 + i * 0.1) * 0.6, GREY)
    person(d, W / 2 - 480 if behind else W / 2 - 300, base, 1.1, ramp(t, 0.2))
    if behind:
        pill(d, W / 2 - 480, base - 200, "YOU", ramp(t, 0.6), 22)


def m_bricks(d, t, dur, rows=4, lbl="WHAT YOU HAVE", uneven=True, **k):
    base = CY + 270
    bw, bh = 120, 50
    total = sum(5 - (r % 2) for r in range(rows))
    n = 0
    for r in range(rows):
        cnt = 5 - (r % 2)
        y = base - (r + 1) * (bh + 8)
        x0 = W / 2 - (cnt * (bw + 8)) / 2
        for c in range(cnt):
            st = 0.2 + (max(0.8, dur * 0.6)) * n / total
            kk = ramp(t, st, 0.3)
            if kk > 0:
                yy = y - (1 - kk) * 60
                c2 = GREY if uneven and (r + c) % 3 == 0 else WHITE
                d.rounded_rectangle([x0 + c * (bw + 8), yy, x0 + c * (bw + 8) + bw, yy + bh], 6, outline=col(c2, kk), width=4)
            n += 1
    polyline(d, [(W / 2 - 520, base), (W / 2 + 520, base)], ramp(t, 0.1), WHITE, 4)
    label(d, W / 2, base + 40, lbl, ramp(t, 0.5), 24)


def m_map(d, t, dur, a_lbl="WHERE YOU START", b_lbl="WHERE YOU GO", **k):
    a = ramp(t, 0.1)
    ax, ay = W / 2 - 450, CY + 230
    bx, by = W / 2 + 450, CY - 40
    for x, y, lb, c, st in ((ax, ay, a_lbl, GREY, 0.1), (bx, by, b_lbl, WHITE, 1.2)):
        pa = ramp(t, st, 0.4)
        d.ellipse([x - 30, y - 90, x + 30, y - 30], outline=col(c, pa), width=6)
        d.polygon([(x - 26, y - 52), (x + 26, y - 52), (x, y)], fill=col(c, pa))
        label(d, x, y + 40, lb, pa, 24, c)
    pts = [(lerp(ax, bx, f), lerp(ay, by, f) + 120 * math.sin(f * math.pi * 2)) for f in [i / 60 for i in range(61)]]
    dashed(d, pts[:int(60 * ramp(t, 0.4, 1.0)) + 1], col(WHITE, a), 5, 16, 12)


def m_dots(d, t, dur, connect=False, n=9, **k):
    """Scattered dots; optionally connected into a path looking back."""
    import random
    rnd = random.Random(7)
    pts = [(W / 2 - 600 + i * 150, CY + 120 + rnd.randint(-170, 170)) for i in range(n)]
    for i, (x, y) in enumerate(pts):
        a = ramp(t, 0.1 + i * 0.08, 0.3)
        d.ellipse([x - 14, y - 14, x + 14, y + 14], fill=col(WHITE, a))
    if connect:
        polyline(d, pts, ramp(t, 0.6, max(0.8, dur * 0.6)), WHITE, 5)


def m_fog(d, t, dur, lbl=None, **k):
    """Figure with a small lantern on a path into fog."""
    base = CY + 230
    base_line(d, t, base, 620)
    person(d, W / 2 - 300, base, 1.2, ramp(t, 0.2))
    lx, ly = W / 2 - 220, base - 110
    d.rounded_rectangle([lx - 18, ly - 26, lx + 18, ly + 26], 6, outline=col(WHITE, ramp(t, 0.4)), width=4)
    glow = 0.6 + 0.4 * math.sin(t * 3)
    circle(d, lx, ly, 60 + 10 * glow, ramp(t, 0.4), col(WHITE, 0.35), 3)
    for i in range(7):
        fx = W / 2 - 60 + i * 100
        dashed(d, [(fx, base - 260), (fx, base - 20)], col(DIM, ramp(t, 0.3)), 3, 10, 14)
    if lbl:
        pill(d, W / 2 + 260, base - 330, lbl, ramp(t, 0.8) * 0.9, 22, inverted=False)


def m_mirror(d, t, dur, reflect="solid", lbl=None, **k):
    base = CY + 250
    base_line(d, t, base, 560)
    person(d, W / 2 - 260, base, 1.5, ramp(t, 0.2))
    cx = W / 2 + 260
    d.rounded_rectangle([cx - 150, base - 400, cx + 150, base], 150, outline=col(WHITE, ramp(t, 0.1)), width=6)
    if reflect == "solid":
        person(d, cx, base - 40, 1.5, ramp(t, 0.6, 1.0))
    else:
        dashed_person(d, cx, base - 40, 1.5, ramp(t, 0.6, 1.0), GREY)
    if lbl:
        pill(d, cx, base - 450, lbl, ramp(t, 1.0), 24)


def m_cage(d, t, dur, words=(), **k):
    """Figure boxed in by walls made of words."""
    base = CY + 260
    person(d, W / 2, base, 1.3, ramp(t, 0.1))
    x0, x1, y0 = W / 2 - 260, W / 2 + 260, CY - 120
    k2 = ramp(t, 0.4, 1.2)
    polyline(d, [(x0, base), (x0, y0), (x1, y0), (x1, base)], k2, WHITE, 6)
    pos = [(W / 2, y0 - 40), (x0 - 150, CY + 80), (x1 + 150, CY + 80), (x0 - 150, CY + 200), (x1 + 150, CY + 200)]
    for i, w in enumerate(words):
        x, y = pos[i % len(pos)]
        pill(d, x, y, w, ramp(t, 0.6 + i * 0.25), 24, inverted=True)
    for i in range(7):
        x = lerp(x0, x1, i / 6)
        d.line([(x, y0), (x, base)], fill=col(WHITE, 0.5 * ramp(t, 1.0)), width=3)


def m_shield(d, t, dur, front="PROTECTING", back="PREVENTING", **k):
    """Figure behind a shield that is also a wall blocking a path."""
    base = CY + 250
    base_line(d, t, base, 620)
    person(d, W / 2 - 330, base, 1.3, ramp(t, 0.1))
    sx = W / 2 - 120
    pts = [(sx - 80, CY - 60), (sx + 80, CY - 60), (sx + 80, CY + 110), (sx, CY + 200), (sx - 80, CY + 110), (sx - 80, CY - 60)]
    polyline(d, pts, ramp(t, 0.3, 0.6), WHITE, 6)
    label(d, sx, CY - 100, front, ramp(t, 0.5), 24)
    trophy(d, W / 2 + 380, CY + 60, ramp(t, 0.8), GREY)
    dashed(d, [(sx + 100, base - 80), (W / 2 + 300, base - 80)], col(GREY, ramp(t, 0.9)), 4, 16, 12)
    label(d, W / 2 + 380, CY + 210, back, ramp(t, 1.1), 24, GREY)


def m_hourglass(d, t, dur, **k):
    cx, cy = W / 2, CY + 80
    a = ramp(t, 0.2)
    hw, hh = 120, 170
    d.line([(cx - hw - 20, cy - hh), (cx + hw + 20, cy - hh)], fill=col(WHITE, a), width=8)
    d.line([(cx - hw - 20, cy + hh), (cx + hw + 20, cy + hh)], fill=col(WHITE, a), width=8)
    left = [(cx - hw, cy - hh), (cx - hw, cy - hh + 50), (cx - 12, cy - 10), (cx - 12, cy + 10), (cx - hw, cy + hh - 50), (cx - hw, cy + hh)]
    polyline(d, left, a, WHITE, 6)
    polyline(d, [(2 * cx - x, y) for x, y in left], a, WHITE, 6)
    kk = clamp(t / max(dur, 0.1))
    d.polygon([(cx - lerp(80, 8, kk), cy - 40 - 40 * (1 - kk)), (cx + lerp(80, 8, kk), cy - 40 - 40 * (1 - kk)), (cx, cy - 8)], fill=col(WHITE, a))
    d.polygon([(cx - hw + 15, cy + hh - 6), (cx + hw - 15, cy + hh - 6), (cx, cy + hh - 6 - 100 * kk)], fill=col(WHITE, a))


def m_sunrise(d, t, dur, **k):
    hz = CY + 230
    a = ramp(t, 0.1)
    polyline(d, [(W / 2 - 600, hz), (W / 2 + 600, hz)], a, WHITE, 4)
    rise = ramp(t, 0.2, max(0.8, dur * 0.9))
    r = 130
    cy = hz + r - rise * 1.4 * r
    d.pieslice([W / 2 - r, cy - r, W / 2 + r, cy + r], 180, 360, outline=col(WHITE, a), width=7)
    for i in range(7):
        ang = math.radians(-180 + 15 + i * 25)
        r0, r1 = r + 30, r + 30 + 40 * rise
        d.line([(W / 2 + r0 * math.cos(ang), cy + r0 * math.sin(ang)), (W / 2 + r1 * math.cos(ang), cy + r1 * math.sin(ang))], fill=col(WHITE, a * rise), width=4)


def m_puzzle(d, t, dur, missing=True, lbl=None, **k):
    """3x2 grid of pieces; one missing then (optionally) dropped in."""
    s = 150
    x0, y0 = W / 2 - 1.5 * s, CY - 40
    for r in range(2):
        for c in range(3):
            i = r * 3 + c
            a = ramp(t, 0.1 + i * 0.08, 0.3)
            off = 0
            if i == 4:
                if missing:
                    dashed(d, [(x0 + c * s, y0 + r * s), (x0 + (c + 1) * s, y0 + r * s), (x0 + (c + 1) * s, y0 + (r + 1) * s), (x0 + c * s, y0 + (r + 1) * s), (x0 + c * s, y0 + r * s)], col(GREY, a), 4, 12, 10)
                    continue
                off = (1 - ramp(t, 0.6, 0.6)) * -220
            d.rounded_rectangle([x0 + c * s + 6, y0 + r * s + 6 + off, x0 + (c + 1) * s - 6, y0 + (r + 1) * s - 6 + off], 12, outline=col(WHITE, a), width=5)
            cx_, cy_ = x0 + c * s + s / 2, y0 + r * s + 6 + off
            d.ellipse([cx_ - 18, cy_ - 18, cx_ + 18, cy_ + 18], fill=col(BLACK, a), outline=col(WHITE, a), width=5)
    if lbl:
        label(d, W / 2, y0 + 2 * s + 50, lbl, ramp(t, 0.9), 26)


def m_compass(d, t, dur, lbl="DIRECTION", settle=True, **k):
    cx, cy, r = W / 2, CY + 90, 180
    a = ramp(t, 0.1)
    circle(d, cx, cy, r, ramp(t, 0.1, 0.8))
    for i, nm in enumerate("NESW"):
        ang = math.radians(-90 + i * 90)
        ftext(d, cx + (r - 40) * math.cos(ang), cy + (r - 40) * math.sin(ang), nm, 28, a, GREY)
    wob = math.sin(t * 7) * 60 * (1 - ramp(t, 0.6, 1.4)) if settle else math.sin(t * 5) * 90
    ang = math.radians(-60 + wob)
    tip = (cx + (r - 70) * math.cos(ang), cy + (r - 70) * math.sin(ang))
    tail = (cx - (r - 70) * math.cos(ang), cy - (r - 70) * math.sin(ang))
    perp = (math.cos(ang + math.pi / 2) * 18, math.sin(ang + math.pi / 2) * 18)
    d.polygon([tip, (cx + perp[0], cy + perp[1]), tail, (cx - perp[0], cy - perp[1])], outline=col(WHITE, a), fill=None)
    d.polygon([tip, (cx + perp[0], cy + perp[1]), (cx - perp[0], cy - perp[1])], fill=col(WHITE, a))
    label(d, cx, cy + r + 50, lbl, ramp(t, 0.6), 26)


def m_key(d, t, dur, lbl="YOURS", **k):
    a = ramp(t, 0.2)
    cx, cy = W / 2 - 160, CY + 90
    circle(d, cx, cy, 90, ramp(t, 0.1, 0.6))
    circle(d, cx, cy, 36, ramp(t, 0.3, 0.4))
    polyline(d, [(cx + 90, cy), (cx + 420, cy)], ramp(t, 0.4, 0.6), WHITE, 10)
    polyline(d, [(cx + 340, cy), (cx + 340, cy + 60)], ramp(t, 0.8, 0.3), WHITE, 10)
    polyline(d, [(cx + 400, cy), (cx + 400, cy + 80)], ramp(t, 0.9, 0.3), WHITE, 10)
    pill(d, cx + 250, cy - 110, lbl, ramp(t, 1.0), 26)


def m_crown(d, t, dur, lbl="CHOOSE YOURSELF", **k):
    base = CY + 250
    base_line(d, t, base, 520)
    person(d, W / 2, base, 1.6, ramp(t, 0.1))
    y = base - 270 - (1 - ramp(t, 0.5, 0.6)) * 120
    pts = [(W / 2 - 70, y), (W / 2 - 70, y - 60), (W / 2 - 35, y - 25), (W / 2, y - 75), (W / 2 + 35, y - 25), (W / 2 + 70, y - 60), (W / 2 + 70, y), (W / 2 - 70, y)]
    polyline(d, pts, ramp(t, 0.5, 0.6), WHITE, 6)
    pill(d, W / 2, base + 60, lbl, ramp(t, 1.0), 24)


def m_tangle(d, t, dur, lbl="EVERYTHING AT ONCE", **k):
    import random
    rnd = random.Random(3)
    cx, cy = W / 2, CY + 100
    pts = [(cx + rnd.randint(-330, 330), cy + rnd.randint(-170, 170)) for _ in range(26)]
    polyline(d, pts, ramp(t, 0.1, max(0.8, dur * 0.7)), WHITE, 4)
    label(d, cx, cy + 250, lbl, ramp(t, 0.8), 24, GREY)


def m_question(d, t, dur, a_lbl=None, b_lbl=None, **k):
    """Two options with a big question mark between."""
    a = ramp(t, 0.2)
    ftext(d, W / 2, CY + 80, "?", 220, a)
    if a_lbl:
        pill(d, W / 2 - 420, CY + 80, a_lbl, ramp(t, 0.6), 28, inverted=False)
    if b_lbl:
        pill(d, W / 2 + 420, CY + 80, b_lbl, ramp(t, 0.9), 28)


def m_pulse(d, t, dur, **k):
    cx, cy = W / 2, CY + 90
    pulse = 0.5 + 0.5 * math.sin(t * 4)
    r = 22 + 6 * pulse
    a = ramp(t, 0.2)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col(WHITE, a))
    for kk in range(2):
        rr = 60 + ((t * 70 + kk * 60) % 120)
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=col(WHITE, a * (1 - (rr - 60) / 120)), width=3)


def m_progress(d, t, dur, lbl="PROGRESS", value=0.08, invisible=False, **k):
    a = ramp(t, 0.2)
    x0, x1, y = W / 2 - 400, W / 2 + 400, CY + 100
    d.rounded_rectangle([x0, y - 40, x1, y + 40], 40, outline=col(WHITE, a), width=6)
    v = value * ramp(t, 0.5, 1.5)
    fill_c = DIM if invisible else WHITE
    d.rounded_rectangle([x0 + 14, y - 26, x0 + 14 + max(30, (x1 - x0 - 28) * v), y + 26], 26, fill=col(fill_c, a))
    label(d, W / 2, y - 100, lbl, a, 30)
    label(d, x1 - 40, y + 90, f"{max(1, int(v * 100))}%", a, 28, GREY)


def m_notifs(d, t, dur, items=("NEW MESSAGE", "3 NEW VIDEOS", "@YOU WAS MENTIONED", "BREAKING NEWS"), **k):
    """Phone with notification cards popping in one after another."""
    a = ramp(t, 0.1)
    cx, cy = W / 2, CY + 70
    d.rounded_rectangle([cx - 170, cy - 280, cx + 170, cy + 280], 40, outline=col(WHITE, a), width=7)
    d.rounded_rectangle([cx - 40, cy - 260, cx + 40, cy - 246], 7, fill=col(WHITE, a))
    every = max(0.25, min(0.6, dur * 0.6 / max(1, len(items))))
    for i, it in enumerate(items):
        st = 0.3 + i * every
        k2 = ramp(t, st, 0.25)
        if k2 <= 0:
            continue
        y = cy - 190 + i * 100 - (1 - k2) * 30
        x0 = cx - 260 if i % 2 else cx - 140
        d.rounded_rectangle([x0, y - 38, x0 + 400, y + 38], 16, fill=col(BLACK, k2), outline=col(WHITE, k2), width=4)
        d.ellipse([x0 + 16, y - 16, x0 + 48, y + 16], fill=col(WHITE, k2))
        ftext(d, x0 + 64, y, it, 24, k2, anchor="lm")


def m_stage(d, t, dur, lbl=None, empty=False, performing=True, **k):
    """Figure on a stage under a spotlight, audience heads in front."""
    base = CY + 140
    a = ramp(t, 0.1)
    d.rectangle([W / 2 - 360, base, W / 2 + 360, base + 40], outline=col(WHITE, a), width=5)
    bob = math.sin(t * 6) * 8 if performing else 0
    person(d, W / 2, base + bob, 1.3, ramp(t, 0.2))
    for i in range(9 if not empty else 0):
        x = W / 2 + (i - 4) * 130
        d.ellipse([x - 32, base + 120, x + 32, base + 184], fill=col(GREY, ramp(t, 0.2 + i * 0.04) * 0.7))
        d.rounded_rectangle([x - 50, base + 190, x + 50, base + 260], 30, fill=col(GREY, ramp(t, 0.2 + i * 0.04) * 0.7))
    if lbl:
        pill(d, W / 2, base - 290, lbl, ramp(t, 0.7), 24, inverted=False)


def m_ring(d, t, dur, tags=(), center_tag=None, **k):
    """Figure surrounded by a ring of people, each with an optional label."""
    cx, cy = W / 2, CY + 140
    n = max(6, len(tags))
    for i in range(n):
        ang = math.radians(i * 360 / n)
        x, y = cx + 520 * math.cos(ang), cy + 190 * math.sin(ang) + 60
        a = ramp(t, 0.15 + i * 0.07)
        person(d, x, y + 60, 0.75, a * 0.75, GREY)
        if i < len(tags):
            pill(d, x, y - 80, tags[i], ramp(t, 0.5 + i * 0.12), 20, inverted=False)
    person(d, cx, cy + 120, 1.2, ramp(t, 0.1))
    if center_tag:
        pill(d, cx, cy - 110, center_tag, ramp(t, 1.2), 22)


def m_cta(d, t, dur, kind="comment", lbl=None, **k):
    """Call-to-action icon: comment | save | share."""
    cx, cy = W / 2, CY + 60
    a = ramp(t, 0.2)
    pop = 1 + 0.08 * math.sin(math.pi * clamp((t - 0.2) / 0.5))
    s = 1.3 * pop
    if kind == "comment":
        d.rounded_rectangle([cx - 150 * s, cy - 100 * s, cx + 150 * s, cy + 70 * s], int(40 * s), outline=col(WHITE, a), width=8)
        d.polygon([(cx - 70 * s, cy + 66 * s), (cx - 20 * s, cy + 66 * s), (cx - 90 * s, cy + 130 * s)], fill=col(WHITE, a))
        for i in range(3):
            da = ramp(t, 0.5 + i * 0.15, 0.2) * (0.6 + 0.4 * math.sin(t * 5 - i))
            d.ellipse([cx + (i - 1) * 70 * s - 16 * s, cy - 31 * s, cx + (i - 1) * 70 * s + 16 * s, cy + 1 * s], fill=col(WHITE, da))
        lbl = lbl or "COMMENT BELOW"
    elif kind == "save":
        fill = ramp(t, 0.8, 0.4)
        pts = [(cx - 90 * s, cy - 140 * s), (cx + 90 * s, cy - 140 * s), (cx + 90 * s, cy + 130 * s), (cx, cy + 60 * s), (cx - 90 * s, cy + 130 * s)]
        d.polygon(pts, fill=col(WHITE, a * fill))
        polyline(d, pts + [pts[0]], a, WHITE, 8)
        lbl = lbl or "SAVE THIS"
    else:
        k2 = ramp(t, 0.6, 0.6)
        ox, oy = 60 * k2, -40 * k2
        pts = [(cx - 160 * s + ox, cy + oy), (cx + 160 * s + ox, cy - 120 * s + oy), (cx + 40 * s + ox, cy + 130 * s + oy), (cx - 10 * s + ox, cy + 30 * s + oy)]
        polyline(d, pts + [pts[0]], a, WHITE, 8)
        polyline(d, [(cx - 10 * s + ox, cy + 30 * s + oy), (cx + 160 * s + ox, cy - 120 * s + oy)], a, WHITE, 6)
        for i in range(3):
            dashed(d, [(cx - 260 * s, cy + (i * 40 - 20) * s), (cx - 180 * s, cy + (i * 40 - 20) * s)], col(GREY, a * k2), 4, 14, 10)
        lbl = lbl or "SEND IT TO SOMEONE"
    pill(d, cx, cy + 230, lbl, ramp(t, 0.6), 28)


def m_blank(d, t, dur, **k):
    pass


# ================================================================ HUD motifs (stat-panel style)
def _icon(d, x, y, kind, a, s=1.6):
    c = col(WHITE, a)
    if kind in ("thumb", "thumbdown"):
        f = 1 if kind == "thumb" else -1
        P = lambda px, py: (x + px * s, y + f * py * s)
        d.rectangle([*P(-13, -1), *P(-9, 14)] if f > 0 else [*P(-13, -14), *P(-9, 1)], fill=c)  # cuff
        d.rounded_rectangle([x - 7 * s, y - (2 if f > 0 else 14) * s, x + 11 * s, y + (14 if f > 0 else 2) * s], int(4 * s), fill=c)
        d.polygon([P(-7, 0), P(-4, -17), P(0, -19), P(3, -15), P(3, 0)], fill=c)  # thumb
        for i in range(3):  # finger creases
            yy = y + f * (3 + i * 4) * s
            d.line([(x + 2 * s, yy), (x + 11 * s, yy)], fill=(0, 0, 0, int(255 * a)), width=2)
    elif kind == "heart":
        pts = [(x + 16 * s * math.sin(q) ** 3 * 0.75,
                y - (13 * math.cos(q) - 5 * math.cos(2 * q) - 2 * math.cos(3 * q) - math.cos(4 * q)) * s * 0.75)
               for q in [i * math.pi / 30 for i in range(61)]]
        polyline(d, pts, 1, c, 3)
    elif kind == "q":
        ftext(d, x, y, "?", 34, a)


def _panel(d, cx, top, rows, t, a, w=560):
    """rows: list of (label, value 0..100). Draws a bordered stat panel; returns its bottom y."""
    h = 34 + 62 * len(rows)
    d.rounded_rectangle([cx - w / 2, top, cx + w / 2, top + h], 14, outline=col(WHITE, a), width=3, fill=col(BLACK, a * 0.85))
    for i, (lb, v) in enumerate(rows):
        y = top + 34 + i * 62
        ftext(d, cx - w / 2 + 28, y, lb, 24, a * 0.8, SOFT, anchor="lm")
        ftext(d, cx + w / 2 - 28, y, f"{int(round(v))}%", 40, a, anchor="rm")
        bx0, bx1, by = cx - w / 2 + 28, cx + w / 2 - 28, y + 30
        d.rounded_rectangle([bx0, by - 4, bx1, by + 4], 4, outline=col(GREY, a), width=2)
        if v > 0.5:
            d.rounded_rectangle([bx0, by - 4, bx0 + (bx1 - bx0) * v / 100, by + 4], 4, fill=col(WHITE, a))
    return top + h


def _crowd_xs(n, gap=125, hole=170):
    xs = []
    for i in range(n):
        side = -1 if i % 2 == 0 else 1
        k = i // 2
        xs.append(W / 2 + side * (hole + k * gap))
    return sorted(xs)


def m_hud(d, t, dur, lbl="PUBLIC APPROVAL", start=0, end=93, lbl2=None, start2=0, end2=0,
          cross=False, crowd=6, icons="thumb", tag=None, tag_dim=False, hero=True, count=1.4, **k):
    """Stat panel counting start->end, wired to a glowing figure in a grey crowd."""
    a = ramp(t, 0.05, 0.3)
    base = CY + 250
    p = ease((t - 0.2) / count)
    rows = [(lbl, lerp(start, end, p))]
    if lbl2:
        rows.append((lbl2, lerp(start2, end2, p)))
    top = 345
    bottom = _panel(d, W / 2, top, rows, t, a)
    if hero:
        polyline(d, [(W / 2, bottom), (W / 2, base - 175)], ramp(t, 0.3, 0.4), col(WHITE, a * 0.7), 3)
        person(d, W / 2, base, 1.15, a)
    for i, x in enumerate(_crowd_xs(crowd)):
        ia = ramp(t, 0.15 + 0.05 * i, 0.3)
        person(d, x, base, 0.8, ia * 0.8, GREY)
        if icons:
            _icon(d, x, base - 165, icons, ramp(t, 0.5 + 0.08 * i, 0.25) * 0.9)
    polyline(d, [(W / 2 - 700, base + 2), (W / 2 + 700, base + 2)], a, col(WHITE, 0.35), 2)
    if tag:
        pill(d, W / 2, bottom + 70, tag, ramp(t, 0.9, 0.3) * (0.45 if tag_dim else 1), 24, inverted=not tag_dim)
    if cross:
        c0 = 0.9
        pad = 40
        polyline(d, [(W / 2 - 280 + pad, top - 10), (W / 2 + 280 - pad, bottom + 10)], ramp(t, c0, 0.2), WHITE, 9)
        polyline(d, [(W / 2 + 280 - pad, top - 10), (W / 2 - 280 + pad, bottom + 10)], ramp(t, c0 + 0.15, 0.2), WHITE, 9)


def m_battery(d, t, dur, lbl="YOUR ENERGY", start=1.0, end=0.15, drains=5, **k):
    """Your battery drains into the people around you."""
    a = ramp(t, 0.05, 0.3)
    base = CY + 250
    lv = lerp(start, end, ease((t - 0.3) / max(0.8, dur * 0.6)))
    bx, by, bw, bh = W / 2 + 230, 430, 270, 100
    ftext(d, bx + bw / 2, by - 40, lbl, 24, a * 0.8, SOFT)
    d.rounded_rectangle([bx, by, bx + bw, by + bh], 12, outline=col(WHITE, a), width=5)
    d.rectangle([bx + bw, by + 32, bx + bw + 14, by + bh - 32], fill=col(WHITE, a))
    cells = 5
    on = math.ceil(lv * cells - 0.01)
    for i in range(cells):
        x0 = bx + 12 + i * (bw - 24) / cells
        d.rounded_rectangle([x0 + 3, by + 12, x0 + (bw - 24) / cells - 3, by + bh - 12], 5,
                            fill=col(WHITE, a * (1 if i < on else 0.08)))
    ftext(d, bx + bw + 40, by + bh / 2, f"{int(lv * 100)}%", 44, a, anchor="lm")
    person(d, bx + bw / 2, base, 1.15, a)
    for i in range(drains):
        x = W / 2 - 650 + i * 150
        person(d, x, base, 0.8, ramp(t, 0.1 + 0.05 * i, 0.3) * 0.8, GREY)
        fill = 1 - lv
        ix, iy = x, base - 175
        d.rounded_rectangle([ix - 26, iy - 12, ix + 26, iy + 12], 4, outline=col(WHITE, a * 0.8), width=3)
        d.rectangle([ix - 22, iy - 8, ix - 22 + 44 * fill, iy + 8], fill=col(WHITE, a * 0.8))
        dashed(d, [(bx - 10, by + bh / 2), (ix + 30, iy)], col(GREY, a * 0.8), 2, 10, 8)
    polyline(d, [(W / 2 - 750, base + 2), (W / 2 + 700, base + 2)], a, col(WHITE, 0.35), 2)


def m_beam(d, t, dur, lbl="YOUR FUTURE", crowd=5, tags=(), **k):
    """A wall of light between the crowd and you; you walk on toward what's next."""
    a = ramp(t, 0.05, 0.3)
    base = CY + 250
    for i in range(crowd):
        x = W / 2 - 700 + i * 120
        person(d, x, base, 0.8, ramp(t, 0.1 + 0.05 * i, 0.3) * 0.75, GREY)
    bx = W / 2 - 60
    h = ramp(t, 0.3, 0.5)
    for wdt, al in ((26, 0.12), (14, 0.3), (5, 1.0)):
        d.rectangle([bx - wdt / 2, CY - 330 + 330 * (1 - h), bx + wdt / 2, base + 60 - 30 * (1 - h)], fill=col(WHITE, al * h))
    hx = W / 2 + 120 + 90 * ease((t - 0.6) / max(1, dur - 0.6))
    person(d, hx, base, 1.15, a)
    ax0, ax1 = hx + 90, W / 2 + 720
    polyline(d, [(ax0, base - 60), (ax1, base - 60)], ramp(t, 0.8, 0.5), WHITE, 4)
    polyline(d, [(ax1 - 22, base - 78), (ax1, base - 60), (ax1 - 22, base - 42)], ramp(t, 1.2, 0.2), WHITE, 4)
    if lbl:
        pill(d, (ax0 + ax1) / 2 + 40, base - 110, lbl, ramp(t, 1.0, 0.3), 24)
    spots = [(W / 2 - 480, CY - 140), (W / 2 - 230, CY - 60), (W / 2 - 560, CY - 10), (W / 2 - 300, CY + 60)]
    for i, tg in enumerate(tags):
        x, y = spots[i % len(spots)]
        pill(d, x, y, tg, ramp(t, 0.6 + 0.2 * i, 0.3) * 0.7, 22, inverted=False)
    polyline(d, [(W / 2 - 760, base + 2), (W / 2 + 760, base + 2)], a, col(WHITE, 0.35), 2)


# ================================================================ batch 6 motifs
def m_water(d, t, dur, inside=False, lbl=None, ripples=False, **k):
    """Waves across the lower frame; a figure on the edge, or already in the water."""
    a = ramp(t, 0.05, 0.4)
    wy = CY + 170
    for i in range(4):
        y = wy + i * 46
        ph = t * (1.6 - i * 0.2) + i
        pts = [(x, y + 12 * math.sin(x / 70 + ph)) for x in range(int(W / 2 - 800), int(W / 2 + 820), 20)]
        polyline(d, pts, a, col(WHITE, 0.9 - i * 0.2), 4 - i // 2)
    if inside:
        cx = W / 2 + 40 * math.sin(t * 1.2)
        bob = 6 * math.sin(t * 2.4)
        d.rounded_rectangle([cx - 60, wy - 40 + bob, cx + 60, wy + 6], 30, fill=col(WHITE, a))
        d.ellipse([cx - 34, wy - 124 + bob, cx + 34, wy - 56 + bob], fill=col(WHITE, a))
        pts = [(x, wy + 12 * math.sin(x / 70 + t * 1.6)) for x in range(int(cx - 100), int(cx + 110), 10)]
        polyline(d, pts, a, WHITE, 4)
        if ripples:
            for j in range(2):
                r = 60 + 90 * ((t * 0.6 + j * 0.5) % 1)
                d.ellipse([cx - r * 1.6, wy - r * 0.3, cx + r * 1.6, wy + r * 0.3], outline=col(WHITE, a * (1 - ((t * 0.6 + j * 0.5) % 1)) * 0.6), width=3)
    else:
        polyline(d, [(W / 2 - 800, wy - 40), (W / 2 - 300, wy - 40), (W / 2 - 300, wy + 160)], a, WHITE, 6)
        person(d, W / 2 - 380, wy - 40, 1.3, a)
    if lbl:
        pill(d, W / 2 + 330, CY - 120, lbl, ramp(t, 0.6, 0.3), 26)


def m_loop(d, t, dur, items=("TASK", "OVERWHELM", "AVOID", "RELIEF"), lbl=None, broken=False, **k):
    """A habit loop: nodes on a ring with a dot circling them."""
    cx, cy, rx, ry = W / 2, CY + 80, 430, 200
    n = len(items)
    angs = [-90 + i * 360 / n for i in range(n)]
    pos = [(cx + rx * math.cos(math.radians(g)), cy + ry * math.sin(math.radians(g))) for g in angs]
    a = ramp(t, 0.1, 0.4)
    ring = [(cx + rx * math.cos(math.radians(g)), cy + ry * math.sin(math.radians(g))) for g in range(-90, 271, 4)]
    if broken:
        dashed(d, ring, col(GREY, a), 3, 16, 12)
    else:
        polyline(d, ring, ramp(t, 0.1, 0.9), col(WHITE, 0.55), 3)
    for i, (x, y) in enumerate(pos):
        pill(d, x, y, items[i], ramp(t, 0.3 + 0.25 * i, 0.3), 26, inverted=(i == 0))
    if not broken:
        g = -90 + ((t * 70) % 360)
        dx, dy = cx + rx * math.cos(math.radians(g)), cy + ry * math.sin(math.radians(g))
        d.ellipse([dx - 11, dy - 11, dx + 11, dy + 11], fill=col(WHITE, a))
    if lbl:
        ftext(d, cx, cy, lbl, 30, ramp(t, 0.9, 0.4), SOFT)


def m_ticket(d, t, dur, lbl="ADMIT ONE", sub="NON-REFUNDABLE", tear=False, walk=False, **k):
    """A cinema ticket; optionally torn, with the figure walking toward the exit."""
    a = ramp(t, 0.1, 0.4)
    cx, cy = W / 2 - (200 if walk else 0), CY + 60
    w, h = 560, 240
    sx = cx + 150
    off = 40 * ramp(t, dur * 0.4, 0.6) if tear else 0
    def body(x0, x1, dx):
        pts = [(x0 + dx, cy - h / 2), (x1 + dx, cy - h / 2), (x1 + dx, cy + h / 2), (x0 + dx, cy + h / 2), (x0 + dx, cy - h / 2)]
        polyline(d, pts, a, WHITE, 6)
    body(cx - w / 2, sx, 0)
    body(sx, cx + w / 2, off)
    for x in (cx - w / 2, cx + w / 2 + off):
        d.ellipse([x - 22, cy - 22, x + 22, cy + 22], fill=col(BLACK, 1), outline=col(WHITE, a), width=6)
    dashed(d, [(sx + off * 0.5, cy - h / 2 + 10), (sx + off * 0.5, cy + h / 2 - 10)], col(GREY, a), 4, 12, 10)
    ftext(d, cx - 70, cy - 30, lbl, 52, a)
    label(d, cx - 70, cy + 45, sub, a, 24, GREY)
    ftext(d, sx + off + 70, cy, "01", 44, a)
    if walk:
        base = CY + 300
        door_icon(d, W / 2 + 560, base, ramp(t, 0.3), 0.8, "EXIT")
        px = W / 2 + 260 + 160 * ease((t - 0.6) / max(1, dur - 0.6))
        person(d, px, base, 1.1, ramp(t, 0.4))


def m_house(d, t, dur, progress=0.6, lbl=None, watchers=True, **k):
    """A house going up line by line, its builder beside it; far-off figures doubting."""
    a = ramp(t, 0.1, 0.4)
    base = CY + 270
    cx = W / 2 + 120
    p = lerp(progress * 0.6, progress, ease((t - 0.2) / max(0.6, dur * 0.7)))
    w, hh, roof = 260, 230, 150
    pts = [(cx - w, base), (cx - w, base - hh), (cx, base - hh - roof), (cx + w, base - hh), (cx + w, base), (cx - w, base)]
    dashed(d, pts, col(GREY, a * 0.5), 3, 14, 12)
    polyline(d, pts, p * a, WHITE, 7)
    for i in range(1, 5):
        yy = base - i * hh / 5
        if p > 0.15 * i:
            polyline(d, [(cx - w, yy), (cx + w, yy)], ramp(t, 0.3 + 0.15 * i, 0.4), col(WHITE, 0.35), 2)
    person(d, cx + w + 110, base, 1.15, a)
    polyline(d, [(cx + w + 160, base - 120), (cx + w + 200, base - 170)], a, WHITE, 6)
    if watchers:
        for i in range(3):
            x = W / 2 - 720 + i * 110
            person(d, x, base, 0.7, ramp(t, 0.5 + 0.1 * i, 0.3) * 0.6, GREY)
            _icon(d, x, base - 150, "q", ramp(t, 0.8 + 0.1 * i, 0.3) * 0.7)
    polyline(d, [(W / 2 - 780, base + 2), (W / 2 + 780, base + 2)], a, col(WHITE, 0.35), 2)
    if lbl:
        pill(d, cx, base - hh - roof - 60, lbl, ramp(t, 0.8, 0.3), 26)


MOTIFS = {k[2:]: v for k, v in globals().items() if k.startswith("m_") and callable(v)}


# ================================================================ builder
def build(spec):
    lines, scenes = [], []
    for item in spec:
        text, motif, kw = (item + ({},))[:3] if len(item) == 2 else item
        lines.append(text)
        if motif == "follow":
            scenes.append(s_follow)
            continue
        kw = dict(kw)
        acc = kw.pop("acc", None)
        if not text.strip():
            scenes.append(lambda d, t, dur, fn=MOTIFS[motif], kw=kw: fn(d, t, dur, **kw))
            continue
        fn = MOTIFS[motif]
        cap_lines, accent, one = make_caption(text, acc)

        def scene(d, t, dur, fn=fn, kw=kw, cap_lines=cap_lines, accent=accent, one=one):
            if one:
                caption(d, cap_lines, t, dur, y=190, size=76, accent=accent)
            else:
                caption(d, cap_lines, t, dur, y=170 if len(cap_lines) == 2 else 150,
                        size=64 if len(cap_lines) == 2 else 54, accent=accent)
            fn(d, t, dur, **kw)
        scene.__name__ = f"k_{motif}"
        scenes.append(scene)
    return lines, scenes


def follow_sub(text):
    """Split the follow line's tail into the two-line subtitle."""
    if "LanzoFocus" not in text:
        return ("FOR IDEAS, LESSONS, AND PERSPECTIVES", "THAT CHALLENGE THE WAY YOU THINK.")
    tail = text.split("LanzoFocus", 1)[1].strip().upper().replace("’", "'")
    words = tail.split()
    if len(tail) < 40:
        return (tail,)
    half = len(tail) / 2
    acc, out = "", []
    for w in words:
        if not out and len(acc) + len(w) > half:
            out.append(acc.strip()); acc = ""
        acc += " " + w
    out.append(acc.strip())
    return tuple(out)


# ================================================================ hook (visual cold open)
def headline(d, lines, t, start=0.12, y=180, size=72):
    """Bold title in a glowing bordered box, slammed in word by word."""
    lines = [ln.upper() for ln in lines]
    f = font(size)
    lh = size * 1.15
    widths = [d.textlength(ln, font=f) for ln in lines]
    bw, bh = max(widths) + 100, lh * len(lines) + 46
    x0, y0, x1, y1 = W / 2 - bw / 2, y - bh / 2, W / 2 + bw / 2, y + bh / 2
    pb = ramp(t, 0, 0.3)
    d.rounded_rectangle([x0, y0, x1, y1], 16, fill=col(BLACK, 0.85 * pb))
    polyline(d, [(W / 2, y0), (x1 - 16, y0), (x1, y0 + 16), (x1, y1 - 16), (x1 - 16, y1), (x0 + 16, y1), (x0, y1 - 16),
                 (x0, y0 + 16), (x0 + 16, y0), (W / 2, y0)], pb, WHITE, 4)
    words = [(li, w) for li, ln in enumerate(lines) for w in ln.split()]
    n = len(words)
    idx = 0
    done = start + 0.85
    for li, ln in enumerate(lines):
        ws = ln.split()
        space = d.textlength(" ", font=f)
        x = W / 2 - widths[li] / 2
        ty = y - (len(lines) - 1) * lh / 2 + li * lh
        for w in ws:
            ap = start + 0.85 * idx / max(1, n)
            a = ramp(t, ap, 0.12)
            d.text((x, ty + (1 - a) * 16), w, font=f, fill=col(WHITE, a), anchor="lm")
            x += d.textlength(w, font=f) + space
            idx += 1
    flash = clamp(1 - (t - done) / 0.5) if t >= done else 0
    if flash > 0:
        d.rounded_rectangle([x0 - 8, y0 - 8, x1 + 8, y1 + 8], 22, outline=col(WHITE, flash * 0.8), width=3)


def hook(title, motif=None, kw=None):
    """Cold-open scene: a moving visual from frame 0 with the title slammed in as a headline."""
    kw = dict(kw or {})
    kw.pop("acc", None)
    fn = MOTIFS[motif] if motif else None

    def s_hook(d, t, dur):
        if fn:
            fn(d, t + 0.3, dur + 0.3, **kw)
        headline(d, title, t)
    return s_hook
