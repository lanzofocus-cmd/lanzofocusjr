"""Shared toolkit for the cinematic story videos (projects/b4_*).

Each story video builds its own world in its scenes.py; this module only holds the pieces they share:
camera, soft light, weather, the articulated figure, shadowy "voice" figures, captions and title cards.
Scenes are still plain f(d, t, dur) functions rendered by render.py.
"""
import math
import random
from PIL import Image, ImageDraw, ImageFilter
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, caption, polyline, pill

BLACK = (0, 0, 0, 255)


def sstep(x):
    x = clamp(x)
    return x * x * (3 - 2 * x)


def pulse(t, at, width=0.25):
    """1 at time `at`, falling to 0 within `width` seconds on either side."""
    return max(0.0, 1 - abs(t - at) / width)


def mix(c1, c2, k):
    return tuple(int(lerp(a, b, clamp(k))) for a, b in zip(c1, c2))


def dimc(c, k):
    return tuple(int(v * k) for v in c[:3]) + (c[3] if len(c) > 3 else 255,)


# ---------------------------------------------------------------- camera
class Cam:
    """World -> screen: x right, y down, zoom z, centred on (cx, cy)."""

    def __init__(self, cx, cy, z=1.0, oy=0):
        self.cx, self.cy, self.z, self.oy = cx, cy, z, oy

    def p(self, x, y):
        return ((x - self.cx) * self.z + W / 2, (y - self.cy) * self.z + H / 2 + self.oy)

    def s(self, v):
        return v * self.z

    def box(self, x0, y0, x1, y1):
        a, b = self.p(x0, y0), self.p(x1, y1)
        return [a[0], a[1], b[0], b[1]]


def cam_lerp(a, b, k, oy=0):
    return Cam(lerp(a[0], b[0], k), lerp(a[1], b[1], k), math.exp(lerp(math.log(a[2]), math.log(b[2]), k)), oy)


def shake(cam, t, amt):
    if amt > 0:
        cam.cx += math.sin(t * 53) * amt / cam.z
        cam.cy += math.cos(t * 47) * amt / cam.z
    return cam


# ---------------------------------------------------------------- light and atmosphere
_cache = {}


def soft(w, h, color, blur, alpha):
    key = ("soft", w, h, color[:3], blur, alpha)
    if key not in _cache:
        im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        ImageDraw.Draw(im).ellipse([blur * 2, blur * 2, w - blur * 2, h - blur * 2], fill=tuple(color[:3]) + (alpha,))
        _cache[key] = im.filter(ImageFilter.GaussianBlur(blur))
    return _cache[key]


def paste(d, im, cx, cy, a=1.0, scale=1.0):
    if a <= 0.01 or scale <= 0.01:
        return
    if abs(scale - 1.0) > 0.01:
        im = im.resize((max(2, int(im.width * scale)), max(2, int(im.height * scale))), Image.BILINEAR)
    if a < 0.99:
        im = im.copy()
        im.putalpha(im.getchannel("A").point(lambda v: int(v * a)))
    x, y = int(cx - im.width / 2), int(cy - im.height / 2)
    if x > W or y > H or x + im.width < 0 or y + im.height < 0:
        return
    d._image.alpha_composite(im, (max(0, x), max(0, y)), (max(0, -x), max(0, -y)))


def glow(d, cx, cy, r, color, a=1.0, squash=1.0):
    """Soft coloured light pool of radius ~r pixels."""
    base = soft(400, int(400 * squash) if squash != 1 else 400, color, 60, 140)
    paste(d, base, cx, cy, a, r / 140)


def tpoly(d, pts, fill, kind="polygon", **kw):
    """Draw a translucent shape that blends over what is already drawn (ImageDraw alone would overwrite)."""
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    x0, y0 = max(0, int(min(xs)) - 2), max(0, int(min(ys)) - 2)
    x1, y1 = min(W, int(max(xs)) + 3), min(H, int(max(ys)) + 3)
    if x1 <= x0 or y1 <= y0:
        return
    lay = Image.new("RGBA", (x1 - x0, y1 - y0))
    ld = ImageDraw.Draw(lay)
    q = [(p[0] - x0, p[1] - y0) for p in pts]
    if kind == "polygon":
        ld.polygon(q, fill=fill)
    elif kind == "ellipse":
        ld.ellipse([q[0], q[1]], fill=fill)
    elif kind == "line":
        ld.line(q, fill=fill, **kw)
    d._image.alpha_composite(lay, (x0, y0))


def overlay(d, color, a):
    """Blend a flat colour over the whole frame."""
    if a > 0.01:
        d._image.alpha_composite(Image.new("RGBA", (W, H), tuple(color[:3]) + (int(255 * clamp(a)),)))


def beam(d, x_top, y_top, x0, x1, y_bot, color, a=0.15, wtop=40):
    tpoly(d, [(x_top - wtop, y_top), (x_top + wtop, y_top), (x1, y_bot), (x0, y_bot)], col(tuple(color[:3]) + (255,), a))


def vignette_img():
    if "vig" not in _cache:
        v = Image.new("L", (W * 2, H * 2), 255)
        ImageDraw.Draw(v).ellipse([W - 520, H - 420, W + 520, H + 420], fill=0)
        v = v.filter(ImageFilter.GaussianBlur(160))
        _cache["vig"] = Image.merge("RGBA", (Image.new("L", v.size, 0),) * 3 + (v,))
    return _cache["vig"]


def darkness(d, cx, cy, a, scale=1.0):
    if a > 0.01:
        paste(d, vignette_img(), cx, cy, a, scale)


def shade_all(d, a, color=(0, 0, 0)):
    overlay(d, color, a)


def sky(top, bottom, a=1.0, h=H):
    """Vertical gradient image (cached), pasted full-frame by the caller."""
    key = ("sky", top[:3], bottom[:3], h)
    if key not in _cache:
        im = Image.new("RGBA", (W, h))
        dd = ImageDraw.Draw(im)
        for y in range(h):
            k = y / max(1, h - 1)
            dd.line([(0, y), (W, y)], fill=mix(top[:3], bottom[:3], k) + (int(lerp(top[3] if len(top) > 3 else 255, bottom[3] if len(bottom) > 3 else 255, k)),))
        _cache[key] = im
    im = _cache[key]
    return im


def draw_sky(d, top, bottom, a=1.0, y=0, h=H):
    im = sky(top, bottom, h=h)
    if a < 0.99:
        im = im.copy()
        im.putalpha(im.getchannel("A").point(lambda v: int(v * a)))
    d._image.alpha_composite(im, (0, int(y)))


def fog(d, cx, cy, w, a=0.3, color=(255, 255, 255)):
    paste(d, soft(1400, 420, color, 90, 40), cx, cy, a, w / 1400)


def topband(d, a=1.0):
    if "band" not in _cache:
        im = Image.new("RGBA", (W, 340))
        dd = ImageDraw.Draw(im)
        for yy in range(340):
            dd.line([(0, yy), (W, yy)], fill=(0, 0, 0, int(230 * (1 - yy / 340) ** 1.4)))
        _cache["band"] = im
    d._image.alpha_composite(_cache["band"], (0, 0))


def top_caption(d, lines, t, dur, accent=None, size=None, y=None):
    topband(d)
    if size is None:
        size = 76 if len(lines) == 1 else 62
    caption(d, lines, t, dur, y=y or (150 if len(lines) == 2 else 135), size=size, accent=accent)


def low_caption(d, lines, t, dur, accent=None, size=58):
    """Caption near the bottom, for shots whose action fills the top of the frame."""
    if "lband" not in _cache:
        im = Image.new("RGBA", (W, 300))
        dd = ImageDraw.Draw(im)
        for yy in range(300):
            dd.line([(0, yy), (W, yy)], fill=(0, 0, 0, int(220 * (yy / 300) ** 1.4)))
        _cache["lband"] = im
    d._image.alpha_composite(_cache["lband"], (0, H - 300))
    caption(d, lines, t, dur, y=H - 150 if len(lines) == 1 else H - 180, size=size, accent=accent)


# ---------------------------------------------------------------- weather
def rain(d, t, a, seed=3, n=160, color=(180, 200, 230), slant=0.25, speed=1.0):
    if a <= 0.01:
        return
    rng = random.Random(seed)
    for i in range(n):
        x0 = rng.uniform(-200, W + 200)
        sp = rng.uniform(1400, 2000) * speed
        y0 = (rng.uniform(0, H) + t * sp) % (H + 200) - 100
        ln = rng.uniform(30, 60)
        d.line([(x0 - slant * (y0 / 2), y0), (x0 - slant * (y0 / 2) - ln * slant, y0 + ln)], fill=col(tuple(color) + (255,), a * rng.uniform(0.25, 0.6)), width=2)


def snow(d, t, a, seed=5, n=130):
    if a <= 0.01:
        return
    rng = random.Random(seed)
    for i in range(n):
        x0 = rng.uniform(0, W)
        y0 = (rng.uniform(0, H) + t * rng.uniform(60, 140)) % (H + 40) - 20
        x = x0 + 30 * math.sin(t * 1.3 + i)
        r = rng.uniform(2, 5)
        d.ellipse([x - r, y0 - r, x + r, y0 + r], fill=col(WHITE, a * rng.uniform(0.4, 0.9)))


def dust(d, t, a, seed=7, n=60, color=(255, 220, 170), rise=20):
    """Floating motes in a light beam."""
    if a <= 0.01:
        return
    rng = random.Random(seed)
    for i in range(n):
        x = (rng.uniform(0, W) + t * rng.uniform(-15, 15)) % W
        y = (rng.uniform(0, H) - t * rng.uniform(5, rise)) % H
        r = rng.uniform(1, 3)
        d.ellipse([x - r, y - r, x + r, y + r], fill=col(tuple(color) + (255,), a * rng.uniform(0.2, 0.7)))


def stars(d, a, seed=9, n=80, ymax=0.55):
    if a <= 0.01:
        return
    rng = random.Random(seed)
    for i in range(n):
        x, y = rng.uniform(0, W), rng.uniform(0, H * ymax)
        r = rng.uniform(1, 2.6)
        d.ellipse([x - r, y - r, x + r, y + r], fill=col(WHITE, a * rng.uniform(0.3, 0.8)))


def moon(d, x, y, r, a, bg=(0, 0, 0)):
    glow(d, x, y, r * 3, (200, 210, 255), a * 0.4)
    d.ellipse([x - r, y - r, x + r, y + r], fill=col((235, 235, 245, 255), a))
    d.ellipse([x - r + r * 0.45, y - r - r * 0.15, x + r + r * 0.45, y + r - r * 0.15], fill=tuple(bg[:3]) + (int(255 * a),))


def sun(d, x, y, r, a, color=(255, 205, 110, 255)):
    glow(d, x, y, r * 3.5, color, a * 0.8)
    d.ellipse([x - r, y - r, x + r, y + r], fill=col(color, a))


def bolt(d, x, y, a, s=1.0):
    pts = [(x, y), (x - 40 * s, y + 120 * s), (x + 10 * s, y + 120 * s), (x - 50 * s, y + 280 * s), (x + 70 * s, y + 90 * s), (x + 15 * s, y + 90 * s), (x + 50 * s, y)]
    d.polygon(pts, fill=col((220, 230, 255, 255), a))


def flash(d, a, color=(200, 210, 255)):
    overlay(d, color, 0.3 * clamp(a))


def cloud(d, cx, cy, r, c, w=None):
    w = w or max(2, int(r * 0.05))
    for dx, rr in [(-1.1, 0.55), (-0.45, 0.8), (0.35, 0.95), (1.1, 0.6)]:
        d.arc([cx + dx * r - rr * r, cy - rr * r * 1.1, cx + dx * r + rr * r, cy + rr * r * 0.9], 180, 360, fill=c, width=w)
    d.line([(cx - 1.65 * r, cy), (cx + 1.7 * r, cy)], fill=c, width=w)


# ---------------------------------------------------------------- the figure
def limb(d, a, b, c, w):
    w = max(2, int(w))
    d.line([a, b], fill=c, width=w)
    r = w / 2
    for p in (a, b):
        d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=c)


def two_bone(d, root, target, L1, L2, c, w, bend=1):
    dx, dy = target[0] - root[0], target[1] - root[1]
    dist = max(1e-3, min(L1 + L2 - 0.01, math.hypot(dx, dy)))
    ang = math.atan2(dy, dx)
    k = math.acos(clamp((L1 * L1 + dist * dist - L2 * L2) / (2 * L1 * dist), -1, 1))
    mid = (root[0] + L1 * math.cos(ang - k * bend), root[1] + L1 * math.sin(ang - k * bend))
    end = (root[0] + dist * math.cos(ang), root[1] + dist * math.sin(ang))
    limb(d, root, mid, c, w)
    limb(d, mid, end, c, w)
    return end


def figure(d, fx, fy, h, color, mode="walk", phase=0.0, face=1, lean=0.0, swing=0.5, stride=1.0, lift=1.0,
           a=1.0, look=0.0, acc=None, name=None, name_a=1.0, name_col=None, eyes=True, mouth=None, tired=0.0,
           streak=0.0, energy=1.0, hands=None, prop=None, head_down=0.0, bodyw=1.0, eye_col=None):
    """Articulated flat figure standing with its feet at (fx, fy), h pixels tall.

    mode: walk | run | stand | slump | sit (on a chair/ledge) | sit_edge | crouch | flail | cheer | kneel |
          point | phone | pull | carry | hammer | clap | lie | reach
    hands: optional ((x, y), (x, y)) targets for back/front hand, overriding the mode's arms.
    acc:   accessory name(s): flame headband spikes cap crown backpack hair hood scarf glasses
    prop:  callback prop(d, front_hand, back_hand, h, a) drawn last.
    """
    c = col(color, a)
    back = col(dimc(color, 0.62), a)
    lw = 0.085 * h
    accs = acc if isinstance(acc, (tuple, list)) else ((acc,) if acc else ())
    L = 0.255 * h
    hip_y = {"crouch": 0.36, "kneel": 0.30, "sit": 0.30, "sit_edge": 0.05}.get(mode, 0.47)
    if mode == "lie":
        _lie(d, fx, fy, h, c, back, lw, face, accs, a)
        return
    hip = (fx, fy - hip_y * h)
    # legs
    for i, cc in ((1, back), (0, c)):
        ph = phase + i * math.pi
        if mode in ("walk", "run"):
            k = 1.35 if mode == "run" else 1.0
            tgt = (fx + 0.15 * h * stride * k * math.cos(ph) * face, fy - lift * 0.17 * h * k * max(0.0, math.sin(ph)))
        elif mode == "crouch":
            tgt = (fx + (0.14 if i else -0.12) * h * face, fy)
        elif mode == "kneel":
            tgt = (fx + (0.25 if i else -0.20) * h * face, fy)
        elif mode == "sit":
            kx = fx + (0.24 + 0.03 * i) * h * face
            limb(d, hip, (kx, hip[1] - 0.01 * h), cc, lw)
            limb(d, (kx, hip[1] - 0.01 * h), (kx + 0.02 * h * face, fy), cc, lw)
            continue
        elif mode == "sit_edge":
            kx = fx + (0.24 + 0.03 * i) * h * face
            limb(d, hip, (kx, hip[1] - 0.02 * h), cc, lw)
            limb(d, (kx, hip[1] - 0.02 * h), (kx + 0.02 * h * face, hip[1] + 0.24 * h), cc, lw)
            continue
        else:
            tgt = (fx + (0.07 if i else -0.06) * h * face, fy)
        two_bone(d, hip, tgt, L, L, cc, lw, bend=face)
    # torso
    if mode in ("slump", "sit_edge"):
        lean = lean + 0.25
    tl = 0.32 * h
    neck = (hip[0] + math.sin(lean) * tl * face, hip[1] - math.cos(lean) * tl)
    hd = head_down + (0.6 if mode == "slump" else 0) + (0.5 if mode == "sit_edge" else 0)
    hang = lean + hd * 0.6
    head = (neck[0] + math.sin(hang) * 0.13 * h * face, neck[1] - math.cos(hang) * 0.13 * h)
    sh = (lerp(hip[0], neck[0], 0.88), lerp(hip[1], neck[1], 0.88))
    al = 0.17 * h

    def arm_pts(sign):
        """returns elbow, hand for the back (sign=-1) or front (sign=1) arm"""
        if hands is not None:
            tgt = hands[0 if sign < 0 else 1]
            return None, tgt
        if mode in ("walk", "run", "stand"):
            sw = swing * math.sin(phase + (0 if sign > 0 else math.pi)) * (1 if mode != "stand" else 0.15)
            ang = math.pi / 2 - sw + lean * 0.6
            ang2 = ang - 0.7 * (0.5 + abs(sw)) * (1.6 if mode == "run" else 1)
            e = (sh[0] + al * math.cos(ang) * face, sh[1] + al * math.sin(ang))
            return e, (e[0] + al * math.cos(ang2) * face, e[1] + al * math.sin(ang2))
        if mode in ("slump",):
            return None, (sh[0] + 0.06 * h * face * sign, sh[1] + 0.33 * h)
        if mode in ("sit_edge",):
            return None, (sh[0] + 0.24 * h * face, sh[1] + 0.12 * h)
        if mode == "sit":
            return None, (sh[0] + 0.2 * h * face, sh[1] + 0.22 * h)
        if mode in ("crouch", "kneel"):
            return None, (sh[0] + 0.22 * h * face, sh[1] + 0.25 * h)
        if mode == "flail":
            ang = -math.pi / 2 + sign * 0.9 + 0.6 * math.sin(phase * 3 + sign)
            e = (sh[0] + al * math.cos(ang), sh[1] + al * math.sin(ang))
            return e, (e[0] + al * math.cos(ang + 0.5 * sign), e[1] + al * math.sin(ang + 0.5 * sign))
        if mode == "cheer":
            return None, (sh[0] + sign * 0.12 * h, sh[1] - 0.32 * h)
        if mode == "point":
            if sign > 0:
                ang = -look * 0.6
                return None, (sh[0] + 0.34 * h * face * math.cos(ang), sh[1] + 0.34 * h * math.sin(ang))
            return None, (sh[0] - 0.02 * h * face, sh[1] + 0.32 * h)
        if mode == "reach":
            return None, (sh[0] + 0.30 * h * face, sh[1] - 0.14 * h + sign * 0.04 * h)
        if mode == "phone":
            if sign > 0:
                return None, (head[0] + 0.12 * h * face, head[1] + 0.12 * h)
            return None, (sh[0] + 0.02 * h * face, sh[1] + 0.32 * h)
        if mode == "pull":
            k = 0.5 + 0.5 * math.sin(phase)
            return None, (sh[0] + 0.18 * h * face, sh[1] - lerp(0.30, 0.05, k) * h)
        if mode == "carry":
            return None, (sh[0] + 0.24 * h * face, sh[1] + 0.06 * h + sign * 0.02 * h)
        if mode == "hammer":
            if sign > 0:
                k = abs(math.sin(phase))
                ang = lerp(-1.6, 0.5, k)
                return None, (sh[0] + 0.30 * h * face * math.cos(ang), sh[1] + 0.30 * h * math.sin(ang))
            return None, (sh[0] + 0.22 * h * face, sh[1] + 0.20 * h)
        if mode == "clap":
            k = abs(math.sin(phase * 2))
            return None, (sh[0] + 0.22 * h * face + sign * 0.06 * h * k, sh[1] + 0.02 * h)
        return None, (sh[0] + 0.03 * h * face * sign, sh[1] + 0.32 * h)

    hands_out = {}

    def arm(sign, cc):
        e, hnd = arm_pts(sign)
        if e is None:
            hnd = two_bone(d, sh, hnd, al, al, cc, lw * 0.8, bend=-face)
        else:
            limb(d, sh, e, cc, lw * 0.8)
            limb(d, e, hnd, cc, lw * 0.8)
        hands_out[sign] = hnd

    if "backpack" in accs:
        bx, by = lerp(hip[0], neck[0], 0.55) - face * 0.12 * h, lerp(hip[1], neck[1], 0.55)
        d.rounded_rectangle([bx - 0.08 * h, by - 0.14 * h, bx + 0.08 * h, by + 0.12 * h], int(0.04 * h), fill=col(dimc(color, 0.5), a))
    arm(-1, back)
    limb(d, hip, neck, c, 0.19 * h * bodyw)
    if "scarf" in accs:
        sc = col((230, 80, 70, 255), a)
        limb(d, (neck[0] - 0.06 * h, neck[1] + 0.02 * h), (neck[0] + 0.06 * h, neck[1] + 0.02 * h), sc, 0.06 * h)
        tail = (neck[0] - face * 0.2 * h, neck[1] + 0.04 * h + 0.03 * h * math.sin(phase * 2))
        limb(d, neck, tail, sc, 0.045 * h)
    arm(1, c)
    r = 0.12 * h
    hx, hy = head
    if "flame" in accs:
        fl = col((255, 205, 90, 255), a)
        for k, (ang, ln) in enumerate([(-130, 1.0), (-100, 1.45), (-70, 1.15), (-160, 0.7)]):
            ln *= 0.25 + 0.75 * energy
            ra = math.radians(ang + 6 * math.sin(phase * 2 + k) * energy)
            tip = (hx + math.cos(ra) * r * (1 + ln), hy + math.sin(ra) * r * (1 + ln))
            d.polygon([(hx + math.cos(ra - 0.5) * r * 0.8, hy + math.sin(ra - 0.5) * r * 0.8), tip,
                       (hx + math.cos(ra + 0.5) * r * 0.8, hy + math.sin(ra + 0.5) * r * 0.8)], fill=fl)
    if "spikes" in accs:
        for k in range(3):
            ra = math.radians(200 + k * 22) if face > 0 else math.radians(-20 - k * 22)
            tip = (hx + math.cos(ra) * r * 1.9, hy + math.sin(ra) * r * 1.5 - r * 0.3)
            d.polygon([(hx, hy - r * 0.9 + k * r * 0.45), tip, (hx, hy - r * 0.4 + k * r * 0.45)], fill=c)
    if "hair" in accs:
        d.chord([hx - r * 1.05, hy - r * 1.15, hx + r * 1.05, hy + r * 0.6], 180, 360, fill=col(dimc(color, 0.55), a))
    d.ellipse([hx - r, hy - r, hx + r, hy + r], fill=c)
    if "hair" in accs:
        d.chord([hx - r * 1.02, hy - r * 1.08, hx + r * 1.02, hy + r * 0.3], 190, 350, fill=col(dimc(color, 0.55), a))
    if "headband" in accs:
        d.line([(hx - r * 0.98, hy - r * 0.25), (hx + r * 0.98, hy - r * 0.25)], fill=col((20, 40, 80, 255), a), width=max(2, int(r * 0.28)))
    if "cap" in accs:  # hard hat
        hc = col((255, 190, 40, 255), a)
        d.chord([hx - r * 1.1, hy - r * 1.25, hx + r * 1.1, hy + r * 0.5], 180, 360, fill=hc)
        d.line([(hx - r * 1.1 + face * r * 0.2, hy - r * 0.37), (hx + r * 1.1 + face * r * 0.5, hy - r * 0.37)], fill=hc, width=max(2, int(r * 0.25)))
    if "crown" in accs:
        cc2 = col((255, 205, 90, 255), a)
        y0 = hy - r * 0.8
        d.polygon([(hx - r * 0.7, y0), (hx - r * 0.75, y0 - r * 0.7), (hx - r * 0.35, y0 - r * 0.35), (hx, y0 - r * 0.85),
                   (hx + r * 0.35, y0 - r * 0.35), (hx + r * 0.75, y0 - r * 0.7), (hx + r * 0.7, y0)], fill=cc2)
    if "hood" in accs:
        d.arc([hx - r * 1.25, hy - r * 1.3, hx + r * 1.25, hy + r * 1.2], 150, 30, fill=col(dimc(color, 0.45), a), width=max(2, int(r * 0.35)))
    if eyes:
        ex = hx + face * r * 0.45
        ey = hy - r * 0.05 - look * r * 0.25 + hd * r * 0.2
        er = max(1.5, r * 0.13)
        ec = eye_col or (10, 10, 14, 255)
        ec = col(ec, a)
        for o in (-0.22, 0.22):
            exx = ex + o * r * face * 0.9 - face * r * 0.12
            if tired > 0.5:
                d.line([(exx - er, ey), (exx + er, ey)], fill=ec, width=max(1, int(er * 0.8)))
            else:
                d.ellipse([exx - er, ey - er * 1.25, exx + er, ey + er * 1.25], fill=ec)
        if mouth is not None:  # -1 frown .. +1 smile
            mx, my = ex - face * r * 0.05, hy + r * 0.42
            d.line([(mx - r * 0.25, my - mouth * r * 0.18), (mx, my + mouth * r * 0.12), (mx + r * 0.25, my - mouth * r * 0.18)],
                   fill=ec, width=max(1, int(er * 0.8)), joint="curve")
        if "glasses" in accs:
            for o in (-0.22, 0.22):
                exx = ex + o * r * face * 0.9 - face * r * 0.12
                d.ellipse([exx - er * 2.2, ey - er * 2.2, exx + er * 2.2, ey + er * 2.2], outline=ec, width=max(1, int(er * 0.6)))
    if tired > 0:
        sx, sy = hx - face * r * 1.1, hy - r * 0.2 + (phase * 8 % 1) * r * 0.6
        er = max(1.5, r * 0.13)
        d.ellipse([sx - er, sy - er * 1.4, sx + er, sy + er], fill=col((170, 210, 255, 255), a * tired))
    if streak > 0:
        for k in range(5):
            yy = lerp(hy, fy - 0.15 * h, k / 4)
            ln = h * (0.5 + 0.35 * math.sin(k * 2.3 + phase)) * streak
            x0 = fx - face * h * 0.28
            d.line([(x0, yy), (x0 - face * ln, yy)], fill=col(color, a * 0.55 * streak), width=max(2, int(h * 0.02)))
    if prop:
        prop(d, hands_out.get(1), hands_out.get(-1), h, a)
    if name and name_a > 0.01:
        size = int(clamp(h * 0.16, 16, 36))
        d.text((hx, hy - r - h * 0.2), name, font=font(size), fill=col(name_col or color, a * name_a), anchor="mm")
    return head


def _lie(d, fx, fy, h, c, back, lw, face, accs, a):
    """Reclining, propped on one elbow (lazy)."""
    hip = (fx, fy - 0.08 * h)
    neck = (fx - face * 0.30 * h, fy - 0.22 * h)
    for i, cc in ((1, back), (0, c)):
        knee = (fx + face * 0.24 * h, fy - (0.18 if i else 0.10) * h)
        limb(d, hip, knee, cc, lw)
        limb(d, knee, (fx + face * 0.48 * h, fy - 0.04 * h), cc, lw)
    limb(d, neck, (neck[0] + face * 0.02 * h, fy - 0.02 * h), back, lw * 0.8)
    limb(d, hip, neck, c, 0.19 * h)
    hx, hy = neck[0] - face * 0.10 * h, neck[1] - 0.08 * h
    r = 0.12 * h
    hand = (neck[0] + face * 0.20 * h, fy - 0.16 * h)
    limb(d, neck, hand, c, lw * 0.8)
    d.ellipse([hx - r, hy - r, hx + r, hy + r], fill=c)
    if "crown" in accs:
        cc2 = col((255, 205, 90, 255), a)
        y0 = hy - r * 0.8
        d.polygon([(hx - r * 0.7, y0), (hx - r * 0.75, y0 - r * 0.7), (hx - r * 0.35, y0 - r * 0.35), (hx, y0 - r * 0.85),
                   (hx + r * 0.35, y0 - r * 0.35), (hx + r * 0.75, y0 - r * 0.7), (hx + r * 0.7, y0)], fill=cc2)
    er = max(1.5, r * 0.13)
    for o in (-0.2, 0.2):  # sleepy closed eyes
        ex = hx + face * r * 0.35 + o * r
        d.line([(ex - er, hy), (ex + er, hy)], fill=(10, 10, 14, int(255 * a)), width=max(1, int(er * 0.8)))


def shade(d, cx, cy, h, color, a=1.0, t=0.0, eyes=True, point=None, arms=0.0, jag=0.0, name=None, name_a=1.0, solid=0.55, face=1):
    """Shadowy hooded voice-figure, floating (no legs). cy = bottom of the cloak.
    point: optional (x, y) screen point an arm reaches toward. jag: jagged cloak hem. arms: 0..1 raised."""
    sway = math.sin(t * 1.6 + cx * 0.01) * h * 0.02
    top = (cx + sway, cy - h)
    hw = h * 0.28
    pts = [(cx - hw * 0.45 + sway, cy - h * 0.78)]
    n = 9
    for i in range(n + 1):
        u = i / n
        x = lerp(cx - hw, cx + hw, u)
        y = cy - (abs(math.sin(u * math.pi * 4 + t * 3)) * h * 0.08 * (1 + jag * 2))
        pts.append((x + math.sin(t * 2 + i) * h * 0.01, y))
    pts.append((cx + hw * 0.45 + sway, cy - h * 0.78))
    body = col(color, a * solid)
    edge = col(color, a * 0.9)
    d.polygon(pts, fill=body)
    polyline(d, pts + [pts[0]], 1, edge, max(2, int(h * 0.012)))
    # hood
    r = h * 0.15
    hx, hy = top[0], top[1] + r * 1.1
    d.ellipse([hx - r * 1.15, hy - r * 1.2, hx + r * 1.15, hy + r * 1.1], fill=col(color, a * (solid + 0.15)))
    d.ellipse([hx - r * 0.75, hy - r * 0.6, hx + r * 0.75, hy + r * 0.8], fill=(0, 0, 0, int(255 * a * 0.85)))
    if eyes:
        er = r * 0.16
        for o in (-0.3, 0.3):
            ex = hx + o * r + face * r * 0.12
            d.ellipse([ex - er * 1.4, hy - er, ex + er * 1.4, hy + er], fill=col(mix(color, WHITE, 0.6), a))
            glow(d, ex, hy, r * 0.5, color, a * 0.5)
    sh = (hx, hy + r * 1.4)
    if point is not None:
        limb(d, sh, point, col(color, a * 0.85), h * 0.045)
    elif arms > 0:
        for s in (-1, 1):
            limb(d, sh, (sh[0] + s * h * 0.3, sh[1] - h * 0.18 * arms + h * 0.1), col(color, a * 0.7), h * 0.04)
    if name and name_a > 0.01:
        size = int(clamp(h * 0.09, 18, 40))
        d.text((hx, hy - r * 1.9), name, font=font(size), fill=col(mix(color, WHITE, 0.3), a * name_a), anchor="mm")
    return hx, hy


# ---------------------------------------------------------------- title cards
def word_reveal(d, x, y, text, t, a, size, c=WHITE, anchor="lm", step=0.16, start=0.1):
    f = font(size)
    words = text.split()
    widths = [d.textlength(w, font=f) for w in words]
    space = d.textlength(" ", font=f)
    total = sum(widths) + space * (len(words) - 1)
    if anchor == "mm":
        x -= total / 2
    for j, (w, wd) in enumerate(zip(words, widths)):
        k = ramp(t, start + step * j, 0.3)
        d.text((x, y + (1 - k) * 14), w, font=f, fill=col(c, a * k), anchor="lm")
        x += wd + space
    return total


def final_card(d, t, dur, lines, colors=None, size=110, y=None, glow_col=None, sub=None):
    """Big centred end text, each line revealed word by word."""
    n = len(lines)
    lh = size * 1.2
    y0 = (y or H / 2) - (n - 1) * lh / 2
    if glow_col:
        glow(d, W / 2, y0 + (n - 1) * lh / 2, 600, glow_col, 0.5 * ramp(t, 0.2, 1.0))
    for i, ln in enumerate(lines):
        c = (colors[i] if colors else WHITE)
        word_reveal(d, W / 2, y0 + i * lh, ln, t - i * 0.45, 1.0, size, c, anchor="mm")
    if sub:
        d.text((W / 2, y0 + n * lh + 10), sub, font=font(34, False), fill=col(GREY, ramp(t, 1.2, 0.6)), anchor="mm")


def label_tag(d, text, a, x, y, size=28, inverted=False, c=WHITE):
    pill(d, x, y, text, a, size, inverted=inverted)


def windows(tim, n_scenes):
    """Scene windows on the final timeline, exactly as render.py computes them."""
    segs, intro, end = tim["segments"], tim["intro"], tim["end"]
    out = []
    for i in range(n_scenes):
        st = segs[i][0] - 0.15 if i else intro
        en = segs[i + 1][0] - 0.15 if i + 1 < n_scenes else end
        out.append((st, en))
    return out
