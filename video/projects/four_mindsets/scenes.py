"""FOUR MINDSETS — WHO REACHES THE TOP?

A short story told on one enormous glowing staircase. Four simple flat figures (no realism, no injuries):
MOTIVATION (orange, flame tuft), DISCIPLINE (blue, headband), OBSESSION (red, leaning, speed streaks)
and CONSISTENCY (plain white, quiet, back lane). Every staircase scene shares one world, so the camera
can track, push in and pull back across the same stairs.
"""
import math
import random
from PIL import Image, ImageDraw, ImageFilter
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, caption, polyline, pill
from kit import s_follow

TITLE = ("FOUR MINDSETS", "WHO REACHES THE TOP?")
OUTPUT = "Four_Mindsets_Who_Reaches_The_Top_16x9.mp4"
FOLLOW_SUB = ("FOR IDEAS, LESSONS, AND PERSPECTIVES", "THAT CHALLENGE THE WAY YOU THINK.")

LINES = [
    "Four mindsets. One goal. But not everyone reaches the top.",
    "Motivation starts fast.",
    "But feelings don't last forever.",
    "Discipline doesn't care how you feel.",
    "It moves anyway.",
    "Obsession makes you relentless.",
    "But intensity without control can destroy progress.",
    "Consistency doesn't need to be impressive.",
    "It just needs to happen again.",
    "Because the people who win aren't always the fastest.",
    "They're the ones who keep showing up.",
    "Motivation starts you.",
    "Discipline keeps you moving.",
    "Obsession pushes you.",
    "Consistency gets you there.",
    "Show up again tomorrow.",
    "",
]
# pauses after lines (seconds): room for the action to play out
GAPS = {0: 0.9, 1: 1.6, 2: 1.3, 3: 0.6, 4: 1.8, 5: 1.0, 6: 1.2, 7: 2.4, 8: 2.4, 9: 1.1, 10: 2.4,
        11: 0.45, 12: 0.45, 13: 0.45, 14: 1.0, 15: 1.2}

# ---------------------------------------------------------------- palette
MOT = (255, 150, 50, 255)
DIS = (90, 165, 255, 255)
OBS = (255, 62, 72, 255)
CON = (238, 238, 238, 255)
GOLD = (255, 205, 110, 255)
BLACK = (0, 0, 0, 255)

# ---------------------------------------------------------------- staircase geometry (world units)
RUN = 100
N = 40                       # summit tread
OFF = (-175, -105)           # depth vector (oblique view): z=0 front edge, z=1 back wall
LANE = {"MOT": 0.16, "OBS": 0.38, "DIS": 0.60, "CON": 0.84}
NAMES = {"MOT": "MOTIVATION", "OBS": "OBSESSION", "DIS": "DISCIPLINE", "CON": "CONSISTENCY"}
COLS = {"MOT": MOT, "OBS": OBS, "DIS": DIS, "CON": CON}
YS = [0.0]
for i in range(1, N + 1):
    YS.append(YS[-1] - (48 + 1.35 * i))   # risers grow: the staircase gets steeper
CH_H = 150                   # figure height


def sstep(x):
    x = clamp(x)
    return x * x * (3 - 2 * x)


def Y(s):
    return YS[max(0, min(N, s))]


def foot(q, z):
    """World foot point for continuous step position q on depth lane z."""
    n = math.floor(q)
    f = q - n
    if q <= 0:
        x, y = q * RUN + 50, 0.0
    elif n >= N:
        x, y = q * RUN + 50, Y(N)
    else:
        e = sstep(f * 1.25)
        x = (n + f) * RUN + 50
        y = lerp(Y(n), Y(n + 1), e) - math.sin(math.pi * clamp(f * 1.25)) * 14
    return x + OFF[0] * z, y + OFF[1] * z


class Cam:
    def __init__(self, cx, cy, z):
        self.cx, self.cy, self.z = cx, cy, z

    def p(self, x, y):
        return ((x - self.cx) * self.z + W / 2, (y - self.cy) * self.z + H / 2 + 60)


def cam_lerp(a, b, k):
    return Cam(lerp(a[0], b[0], k), lerp(a[1], b[1], k), math.exp(lerp(math.log(a[2]), math.log(b[2]), k)))


def cam_on(q, z=0.5, zoom=1.0, dx=0, dy=-60):
    x, y = foot(q, z)
    return (x + dx, y + dy, zoom)


# ---------------------------------------------------------------- pre-rendered atmosphere
def _soft(size, color, blur, alpha):
    w, h = size
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(im).ellipse([blur * 2, blur * 2, w - blur * 2, h - blur * 2], fill=color[:3] + (alpha,))
    return im.filter(ImageFilter.GaussianBlur(blur))


GLOW_GOLD = _soft((900, 900), GOLD, 120, 120)
GLOW_RED = _soft((500, 500), OBS, 70, 70)
FOG = _soft((1400, 500), (255, 255, 255), 90, 26)
_vig = Image.new("L", (W * 2, H * 2), 255)
ImageDraw.Draw(_vig).ellipse([W - 520, H - 420, W + 520, H + 420], fill=0)
_vig = _vig.filter(ImageFilter.GaussianBlur(160))
DARK = Image.merge("RGBA", (Image.new("L", _vig.size, 0),) * 3 + (_vig,))
TOPBAND = Image.new("RGBA", (W, 360))
for yy in range(360):
    ImageDraw.Draw(TOPBAND).line([(0, yy), (W, yy)], fill=(0, 0, 0, int(235 * (1 - yy / 360) ** 1.4)))


def paste(d, im, cx, cy, a=1.0, scale=1.0):
    if a <= 0.01:
        return
    if scale != 1.0:
        im = im.resize((max(2, int(im.width * scale)), max(2, int(im.height * scale))), Image.BILINEAR)
    if a < 0.99:
        im = im.copy()
        im.putalpha(im.getchannel("A").point(lambda v: int(v * a)))
    x, y = int(cx - im.width / 2), int(cy - im.height / 2)
    if x > W or y > H or x + im.width < 0 or y + im.height < 0:
        return
    d._image.alpha_composite(im, (max(0, x), max(0, y)), (max(0, -x), max(0, -y)))


def darkness(d, cx, cy, a):
    if a > 0.01:
        paste(d, DARK, cx, cy, a)


# ---------------------------------------------------------------- staircase
def stairs(d, cam, light=1.0, trail=0.0, trail_q=0.0, lit_to=None):
    z = cam.z
    if z * RUN < 3:
        return
    # visible step range
    s0, s1 = 0, N
    for s in range(N + 1):
        x, _ = cam.p(s * RUN + RUN, Y(s))
        if x < -300:
            s0 = s
    for s in range(N, -1, -1):
        x, _ = cam.p(s * RUN + OFF[0], Y(s))
        if x > W + 300:
            s1 = s
    a = light
    # ground
    g0 = cam.p(-3000, 0)
    g1 = cam.p(50, 0)
    gb = cam.p(-3000 + OFF[0], OFF[1])
    d.polygon([g0, cam.p(0, 0), cam.p(OFF[0], OFF[1]), gb], fill=(14, 14, 16, int(255 * a)))
    polyline(d, [g0, g1], 1, col((150, 150, 150, 255), a * 0.6), max(2, int(4 * z)))
    for s in range(max(1, s0), min(N, s1) + 1):
        x0, x1 = s * RUN, (s + 1) * RUN if s < N else s * RUN + 900
        y0, y = Y(s - 1), Y(s)
        # riser (faces left, toward the climber)
        rq = [cam.p(x0, y0), cam.p(x0, y), cam.p(x0 + OFF[0], y + OFF[1]), cam.p(x0 + OFF[0], y0 + OFF[1])]
        d.polygon(rq, fill=(20, 20, 24, int(255 * a)))
        # tread
        tq = [cam.p(x0, y), cam.p(x1, y), cam.p(x1 + OFF[0], y + OFF[1]), cam.p(x0 + OFF[0], y + OFF[1])]
        warm = 0
        if lit_to is not None and s <= lit_to:
            warm = 1
        tc = (int(lerp(38, 70, warm)), int(lerp(38, 58, warm)), int(lerp(44, 40, warm)), int(255 * a))
        d.polygon(tq, fill=tc)
        # glowing nosing on the front edge + faint back edge
        nose = (255, 236, 200, 255) if warm else WHITE
        polyline(d, [cam.p(x0 + OFF[0], y + OFF[1]), cam.p(x0, y)], 1, col(nose, a * 0.9), max(2, int(5 * z)))
        polyline(d, [cam.p(x0 + OFF[0], y + OFF[1]), cam.p(x1 + OFF[0], y + OFF[1])], 1, col(WHITE, a * 0.18), max(1, int(3 * z)))
    # front side face (solid zigzag silhouette) with glowing outline
    prof = [cam.p(0, 0)]
    for s in range(max(1, s0), min(N, s1) + 1):
        prof += [cam.p(s * RUN, Y(s - 1)), cam.p(s * RUN, Y(s))]
    last = min(N, s1)
    xend = (last + 1) * RUN if last < N else N * RUN + 900
    prof.append(cam.p(xend, Y(last)))
    bottom = [cam.p(xend, 400), cam.p(max(0, s0) * RUN - 10, 400)]
    d.polygon(prof + bottom, fill=(8, 8, 10, int(255 * a)))
    polyline(d, prof, 1, col(WHITE, a * 0.85), max(2, int(5 * z)))
    if last == N:  # summit cliff
        polyline(d, [cam.p(xend, Y(N)), cam.p(xend, 400)], 1, col(WHITE, a * 0.5), max(2, int(4 * z)))
    # step numbers on the side face
    if z > 0.42:
        f = font(max(14, int(30 * z)), False)
        for s in range(max(1, s0), min(N - 1, s1) + 1):
            x, yv = cam.p(s * RUN + RUN * 0.5, Y(s) + 34)
            if -50 < x < W + 50 and -50 < yv < H + 50:
                d.text((x, yv), str(s), font=f, fill=col((110, 110, 115, 255), a), anchor="mm")
    # Consistency's quiet trail: one soft mark on every step it took
    if trail > 0:
        for s in range(1, min(N, int(trail_q)) + 1):
            x, yv = cam.p(*foot(s + 0.5, LANE["CON"]))
            r = max(2, 7 * z)
            if -20 < x < W + 20 and -20 < yv < H + 20:
                d.ellipse([x - r * 1.6, yv - r * 0.7, x + r * 1.6, yv + r * 0.7], fill=col(GOLD, trail * 0.75))


def summit(d, cam, a=1.0, boost=0.0):
    x, y = cam.p(N * RUN + 400 + OFF[0] * 0.5, Y(N) + OFF[1] * 0.5)
    sc = max(0.5, cam.z * (2.2 + 1.2 * boost))
    paste(d, GLOW_GOLD, x, y - 120 * cam.z, min(1.0, a * (0.9 + 0.3 * boost)), sc)
    # light beam from above
    bw = 260 * cam.z
    beam = [(x - bw * 0.35, y - 2400 * cam.z), (x + bw * 0.35, y - 2400 * cam.z), (x + bw, y), (x - bw, y)]
    d.polygon(beam, fill=col(GOLD, a * (0.10 + 0.10 * boost)))
    # line-art clouds around the summit
    for i, (ox, oy, s) in enumerate([(-700, -260, 1.0), (520, -420, 1.25), (-150, -620, 0.8), (900, -120, 0.9)]):
        cx, cy = cam.p(N * RUN + 400 + ox, Y(N) + oy)
        cloud(d, cx, cy, s * 150 * cam.z, col(WHITE, a * 0.35))
    paste(d, FOG, *cam.p(N * RUN, Y(N) - 60), a * 0.9, cam.z * 2.4)


def cloud(d, cx, cy, r, c):
    w = max(2, int(r * 0.05))
    pts = []
    for k, (dx, rr) in enumerate([(-1.1, 0.55), (-0.45, 0.8), (0.35, 0.95), (1.1, 0.6)]):
        d.arc([cx + dx * r - rr * r, cy - rr * r * 1.1, cx + dx * r + rr * r, cy + rr * r * 0.9], 180, 360, fill=c, width=w)
    d.line([(cx - 1.65 * r, cy), (cx + 1.7 * r, cy)], fill=c, width=w)


def summit_hint(d, cam, a=0.8):
    """When the summit is off screen, a warm glow on the frame edge points to it."""
    x, y = cam.p(N * RUN + 300, Y(N) - 150)
    if 0 < x < W and 0 < y < H:
        return
    ex, ey = clamp(x, 40, W - 40), clamp(y, 40, H - 40)
    paste(d, GLOW_GOLD, ex, ey, a * 0.8, 1.0)


# ---------------------------------------------------------------- characters
def limb(d, a, b, c, w):
    d.line([a, b], fill=c, width=max(2, int(w)))
    r = w / 2
    for p in (a, b):
        d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=c)


def leg(d, hip, footp, L1, L2, c, w, fwd=1):
    dx, dy = footp[0] - hip[0], footp[1] - hip[1]
    dist = max(1e-3, min(L1 + L2 - 0.01, math.hypot(dx, dy)))
    ang = math.atan2(dy, dx)
    k = math.acos(clamp((L1 * L1 + dist * dist - L2 * L2) / (2 * L1 * dist), -1, 1))
    knee = (hip[0] + L1 * math.cos(ang - k * fwd), hip[1] + L1 * math.sin(ang - k * fwd))
    end = (hip[0] + dist * math.cos(ang), hip[1] + dist * math.sin(ang))
    limb(d, hip, knee, c, w)
    limb(d, knee, end, c, w)
    return end


def figure(d, fx, fy, h, who, phase=0.0, mode="walk", lean=0.0, energy=1.0, swing=0.5, stride=1.0,
           lift=1.0, a=1.0, face=1, look=0.0, streak=0.0, label=True, label_a=1.0, tired=0.0):
    c = col(COLS[who], a)
    back = col(tuple(int(v * 0.62) for v in COLS[who][:3]) + (255,), a)
    lw = 0.085 * h
    if mode == "sit":
        fx -= 0.28 * h  # sits right on the front edge of the tread
        face = -1
        hip = (fx + 0.10 * h, fy - 0.05 * h)
        neck = (hip[0] - 0.10 * h, hip[1] - 0.29 * h)
        head = (neck[0] - 0.08 * h, neck[1] - 0.06 * h + 0.07 * h * (1 - look))
        for side, cc in ((1, back), (0, c)):
            kx = hip[0] - 0.24 * h - side * 0.03 * h
            limb(d, hip, (kx, hip[1] - 0.02 * h), cc, lw)
            limb(d, (kx, hip[1] - 0.02 * h), (kx - 0.02 * h, hip[1] + 0.24 * h), cc, lw)
    else:
        hip = (fx, fy - 0.47 * h)
        if mode == "crouch":
            hip = (fx, fy - 0.36 * h)
        L = 0.255 * h
        for i, cc in ((1, back), (0, c)):
            ph = phase + i * math.pi
            fxp = fx + 0.15 * h * stride * math.cos(ph)
            fyp = fy - lift * 0.17 * h * max(0.0, math.sin(ph))
            if mode == "stand":
                fxp, fyp = fx + (0.06 if i else -0.06) * h, fy
            if mode == "crouch":
                fxp, fyp = fx + (0.14 if i else -0.12) * h, fy
            leg(d, hip, (fxp, fyp), L, L, cc, lw, fwd=face)
        tl = 0.32 * h
        neck = (hip[0] + math.sin(lean) * tl * face, hip[1] - math.cos(lean) * tl)
        head = (neck[0] + math.sin(lean) * 0.13 * h * face, neck[1] - math.cos(lean) * 0.13 * h)
    # arms (back arm behind the torso)
    sh = (lerp(hip[0], neck[0], 0.88), lerp(hip[1], neck[1], 0.88))
    al = 0.17 * h

    def arm(sign, cc):
        if mode == "sit":
            e = (sh[0] - 0.12 * h, sh[1] + 0.12 * h)
            hnd = (e[0] - 0.08 * h, e[1] - 0.10 * h)
        elif mode == "flail":
            ang = -math.pi / 2 + sign * 0.9 + 0.6 * math.sin(phase * 3 + sign)
            e = (sh[0] + al * math.cos(ang), sh[1] + al * math.sin(ang))
            hnd = (e[0] + al * math.cos(ang + 0.5 * sign), e[1] + al * math.sin(ang + 0.5 * sign))
        elif mode == "cheer":
            ang = -math.pi / 2 + sign * 0.35
            e = (sh[0] + al * math.cos(ang), sh[1] + al * math.sin(ang))
            hnd = (e[0] + al * math.cos(ang), e[1] + al * math.sin(ang))
        else:
            sw = swing * math.sin(phase + (0 if sign > 0 else math.pi)) * (1 if mode == "walk" else 0.2)
            ang = math.pi / 2 - sw * face + lean * face * 0.6
            e = (sh[0] + al * math.cos(ang), sh[1] + al * math.sin(ang))
            ang2 = ang - 0.7 * face * (0.5 + abs(sw))
            hnd = (e[0] + al * math.cos(ang2), e[1] + al * math.sin(ang2))
        limb(d, sh, e, cc, lw * 0.8)
        limb(d, e, hnd, cc, lw * 0.8)

    arm(-1, back)
    # torso
    limb(d, hip, neck, c, 0.19 * h)
    arm(1, c)
    r = 0.12 * h
    hx, hy = head
    # accessories behind the head
    if who == "MOT":
        fl = col((255, 205, 90, 255), a)
        for k, (ang, ln) in enumerate([(-130, 1.0), (-100, 1.45), (-70, 1.15), (-160, 0.7)]):
            ln *= 0.25 + 0.75 * energy
            wob = 6 * math.sin(phase * 2 + k) * energy
            ra = math.radians(ang + wob - 15 * face * 0)
            tip = (hx + math.cos(ra) * r * (1 + ln), hy + math.sin(ra) * r * (1 + ln))
            b1 = (hx + math.cos(ra - 0.5) * r * 0.8, hy + math.sin(ra - 0.5) * r * 0.8)
            b2 = (hx + math.cos(ra + 0.5) * r * 0.8, hy + math.sin(ra + 0.5) * r * 0.8)
            d.polygon([b1, tip, b2], fill=fl)
    if who == "OBS":
        for k in range(3):
            ra = math.radians(200 + k * 22) if face > 0 else math.radians(-20 - k * 22)
            tip = (hx + math.cos(ra) * r * 1.9, hy + math.sin(ra) * r * 1.5 - r * 0.3)
            d.polygon([(hx, hy - r * 0.9 + k * r * 0.45), tip, (hx, hy - r * 0.4 + k * r * 0.45)], fill=c)
    d.ellipse([hx - r, hy - r, hx + r, hy + r], fill=c)
    if who == "DIS":
        d.line([(hx - r * 0.98, hy - r * 0.25), (hx + r * 0.98, hy - r * 0.25)], fill=col((20, 40, 80, 255), a), width=max(2, int(r * 0.28)))
    # face: eyes looking the way it faces (+ up when `look`)
    ex = hx + face * r * 0.45
    ey = hy - r * 0.05 - look * r * 0.25
    er = max(1.5, r * 0.13)
    eye_c = (10, 10, 14, int(255 * a))
    blink = (math.sin(phase * 0.37 + fx * 0.01) > 0.985)
    for o in (-0.22, 0.22):
        exx = ex + o * r * face * 0.9 - face * r * 0.12
        if who == "CON" and tired > 0.5 or blink:
            d.line([(exx - er, ey), (exx + er, ey)], fill=eye_c, width=max(1, int(er * 0.8)))
        else:
            d.ellipse([exx - er, ey - er * 1.25, exx + er, ey + er * 1.25], fill=eye_c)
    if who == "OBS":  # focused brows
        d.line([(ex - r * 0.45 * face, ey - r * 0.42), (ex + r * 0.30 * face, ey - r * 0.22)], fill=eye_c, width=max(1, int(er)))
    if who == "MOT":  # smile that flattens as energy fades
        mx, my = ex - face * r * 0.05, hy + r * 0.42
        bend = lerp(-0.5, 0.6, energy)
        d.line([(mx - r * 0.25, my - bend * r * 0.18), (mx, my + bend * r * 0.12), (mx + r * 0.25, my - bend * r * 0.18)],
               fill=eye_c, width=max(1, int(er * 0.8)), joint="curve")
    if tired > 0:  # sweat drop
        sx, sy = hx - face * r * 1.1, hy - r * 0.2 + (phase * 8 % 1) * r * 0.6
        d.ellipse([sx - er, sy - er * 1.4, sx + er, sy + er], fill=col((170, 210, 255, 255), a * tired))
    if streak > 0:
        for k in range(5):
            yy = lerp(hy, fy - 0.15 * h, k / 4)
            ln = h * (0.5 + 0.35 * math.sin(k * 2.3 + phase)) * streak
            x0 = fx - face * h * 0.28
            d.line([(x0, yy), (x0 - face * ln, yy)], fill=col(COLS[who], a * 0.55 * streak), width=max(2, int(h * 0.02)))
    if label and label_a > 0.01:
        size = int(clamp(h * 0.17, 16, 34))
        d.text((hx, hy - r - h * 0.2), NAMES[who], font=font(size), fill=col(COLS[who], a * label_a), anchor="mm")


def draw_char(d, cam, who, q, a=1.0, **kw):
    fx, fy = cam.p(*foot(q, LANE[who]))
    h = CH_H * cam.z * (0.88 if who == "CON" else 1.0) * (1 - 0.06 * LANE[who])
    if fx < -h * 2 or fx > W + h * 2 or fy < -h * 2 or fy > H + h * 2:
        return fx, fy, h
    kw.setdefault("phase", q * math.pi)
    figure(d, fx, fy, h, who, a=a, **kw)
    return fx, fy, h


def scene_world(d, cam, chars, light=1.0, trail=0.0, summit_boost=0.0, lit_to=None):
    summit(d, cam, light, summit_boost)
    stairs(d, cam, light, trail, chars.get("CON", (0, {}))[0], lit_to)
    summit_hint(d, cam, light)
    pos = {}
    for who in sorted(chars, key=lambda w: -LANE[w]):
        q, kw = chars[who]
        pos[who] = draw_char(d, cam, who, q, **kw)
    return pos


def top_caption(d, lines, t, dur, accent=None, size=64):
    d._image.alpha_composite(TOPBAND, (0, 0))
    caption(d, lines, t, dur, y=150 if len(lines) == 2 else 130, size=size, accent=accent)


# ---------------------------------------------------------------- weather / time of day
def rain(d, t, a, seed=3):
    rng = random.Random(seed)
    for i in range(160):
        x0 = rng.uniform(-200, W + 200)
        sp = rng.uniform(1400, 2000)
        y0 = (rng.uniform(0, H) + t * sp) % (H + 200) - 100
        ln = rng.uniform(30, 60)
        d.line([(x0, y0), (x0 - ln * 0.25, y0 + ln)], fill=col((180, 200, 230, 255), a * rng.uniform(0.25, 0.6)), width=2)


def snow(d, t, a, seed=5):
    rng = random.Random(seed)
    for i in range(130):
        x0 = rng.uniform(0, W)
        sp = rng.uniform(60, 140)
        y0 = (rng.uniform(0, H) + t * sp) % (H + 40) - 20
        x = x0 + 30 * math.sin(t * 1.3 + i)
        r = rng.uniform(2, 5)
        d.ellipse([x - r, y0 - r, x + r, y0 + r], fill=col(WHITE, a * rng.uniform(0.4, 0.9)))


def stars(d, a, seed=9):
    rng = random.Random(seed)
    for i in range(70):
        x, y = rng.uniform(0, W), rng.uniform(0, H * 0.55)
        r = rng.uniform(1, 2.6)
        d.ellipse([x - r, y - r, x + r, y + r], fill=col(WHITE, a * rng.uniform(0.3, 0.8)))


def moon(d, x, y, r, a):
    d.ellipse([x - r, y - r, x + r, y + r], fill=col((235, 235, 245, 255), a))
    d.ellipse([x - r + r * 0.45, y - r - r * 0.15, x + r + r * 0.45, y + r - r * 0.15], fill=(0, 0, 0, int(255 * a)))


def sun(d, x, y, r, a):
    paste(d, GLOW_GOLD, x, y, a * 0.9, r / 160)
    d.ellipse([x - r, y - r, x + r, y + r], fill=col(GOLD, a))
    for i in range(12):
        ang = math.radians(i * 30)
        d.line([(x + math.cos(ang) * r * 1.35, y + math.sin(ang) * r * 1.35), (x + math.cos(ang) * r * 1.75, y + math.sin(ang) * r * 1.75)],
               fill=col(GOLD, a * 0.8), width=4)


def bolt(d, x, y, a):
    pts = [(x, y), (x - 40, y + 120), (x + 10, y + 120), (x - 50, y + 280), (x + 70, y + 90), (x + 15, y + 90), (x + 50, y)]
    d.polygon(pts, fill=col((220, 230, 255, 255), a))


def flash(d, a):
    if a > 0.01:
        d.rectangle([0, 0, W, H], fill=(200, 210, 255, int(70 * a)))


def tag(d, text, a, x=W - 120, y=H - 130):
    f = font(30)
    tw = d.textlength(text, font=f)
    d.rounded_rectangle([x - tw - 36, y - 30, x, y + 30], 30, outline=col(WHITE, a * 0.8), width=3)
    d.text((x - tw / 2 - 18, y), text, font=f, fill=col(WHITE, a), anchor="mm")


# ---------------------------------------------------------------- story positions
# (start, end) of each character's step position q in every staircase scene
START = -0.7
ST = dict(MOT=-0.5, OBS=-1.7, DIS=-2.9, CON=-4.1)
POS = {
    1: dict(MOT=(ST["MOT"],) * 2, OBS=(ST["OBS"],) * 2, DIS=(ST["DIS"],) * 2, CON=(ST["CON"],) * 2),
    2: dict(MOT=(ST["MOT"], 12.0), OBS=(ST["OBS"], ST["OBS"]), DIS=(ST["DIS"], 0.6), CON=(ST["CON"], 0.0)),
    3: dict(MOT=(12.0, 13.0), OBS=(ST["OBS"], ST["OBS"]), DIS=(0.6, 1.8), CON=(0.0, 1.0)),
    4: dict(MOT=(13.0, 13.0), OBS=(ST["OBS"], -0.2), DIS=(1.8, 6.5), CON=(1.0, 3.6)),
    5: dict(MOT=(13.0, 13.0), OBS=(-0.2, 0.2), DIS=(6.5, 15.0), CON=(3.6, 9.5)),
    6: dict(MOT=(13.0, 13.0), OBS=(0.2, 21.0), DIS=(15.0, 17.0), CON=(9.5, 12.0)),
    7: dict(MOT=(13.0, 13.0), OBS=(21.0, 23.0), DIS=(17.0, 19.0), CON=(12.0, 14.5)),
    8: dict(MOT=(13.0, 13.0), OBS=(23.0, 27.0), DIS=(19.0, 24.0), CON=(14.5, 24.0)),
    9: dict(MOT=(13.0, 13.4), OBS=(27.0, 32.0), DIS=(24.0, 29.0), CON=(24.0, 33.0)),
    10: dict(MOT=(13.4, 14.6), OBS=(32.0, 34.4), DIS=(29.0, 32.0), CON=(33.0, 37.0)),
    11: dict(MOT=(14.6, 16.0), OBS=(34.4, 35.6), DIS=(32.0, 34.0), CON=(37.0, 41.6)),
}


def q_of(scene, who, p):
    a, b = POS[scene][who]
    return lerp(a, b, clamp(p))


# ---------------------------------------------------------------- scenes
def s1_beginning(d, t, dur):
    p = t / dur
    k = sstep(p)
    wide = (2300, -1900, 0.215)
    close = cam_on(-2.3, 0.5, 0.95, dx=120, dy=-120)
    cam = cam_lerp(wide, close, k)
    chars = {w: (ST[w], dict(mode="stand", phase=0, label_a=ramp(t, dur * 0.45 + 0.25 * i, 0.5),
                             look=0.6 + 0.4 * math.sin(t * 0.8 + i), face=1))
             for i, w in enumerate(["MOT", "OBS", "DIS", "CON"])}
    chars["MOT"][1]["mode"] = "walk"
    chars["MOT"][1]["phase"] = t * 9  # bouncing on the spot, can't wait
    chars["MOT"][1]["stride"] = 0.15
    chars["CON"][1]["label_a"] *= 0.6
    scene_world(d, cam, chars)
    paste(d, FOG, W / 2, H - 80, 0.8, 1.6)
    top_caption(d, ["FOUR MINDSETS. ONE GOAL.", "BUT NOT EVERYONE REACHES THE TOP."], t, dur, accent={"FOUR", "TOP."})


def _bg_climbers(scene, p, extra=None):
    """Default state of every climber in a scene; override entries with `extra`."""
    ch = {}
    for w in ("MOT", "OBS", "DIS", "CON"):
        q = q_of(scene, w, p)
        kw = dict(swing=0.5)
        if w == "CON":
            kw.update(label_a=0.55, swing=0.3, stride=0.8)
        a, b = POS[scene][w]
        if a == b:
            kw.update(mode="stand", phase=0)
        ch[w] = (q, kw)
    if extra:
        for w, (q, kw) in extra.items():
            ch[w] = (q, kw)
    return ch


def s2_motivation(d, t, dur):
    p = t / dur
    # bursts forward in hops of two steps, fastest at the start
    pm = 1 - (1 - clamp(p * 1.05)) ** 1.6
    q = lerp(ST["MOT"], 12.0, pm)
    hop = (q - ST["MOT"]) / 2
    qq = ST["MOT"] + 2 * (math.floor(hop) + sstep((hop % 1) * 1.3))
    lift = math.sin(math.pi * clamp((hop % 1) * 1.3)) * 50
    ch = _bg_climbers(2, p, {"MOT": (qq, dict(mode="walk", phase=hop * math.pi * 2, lean=0.32, swing=1.2, stride=1.5,
                                               lift=1.6, energy=1.0, streak=0.4 * (1 - pm)))})
    ch["OBS"] = (ST["OBS"], dict(mode="stand", phase=0, look=0.3))
    cam = cam_lerp(cam_on(-1.5, 0.4, 0.9, dx=200, dy=-120), cam_on(12, 0.4, 0.62, dx=-120, dy=-160), sstep(p * 1.1))
    cam.cy -= lift * 0.3
    scene_world(d, cam, ch)
    # dust puffs at each landing
    fx, fy = cam.p(*foot(qq, LANE["MOT"]))
    ph = hop % 1
    if ph < 0.35 and p < 0.9:
        r = 40 * cam.z * (0.3 + ph * 3)
        d.arc([fx - r * 1.8, fy - r * 0.6, fx + r * 0.2, fy + r * 0.5], 180, 330, fill=col(WHITE, 0.5 * (1 - ph / 0.35)), width=3)
    top_caption(d, ["MOTIVATION STARTS FAST."], t, dur, accent={"FAST."}, size=76)


def s3_feelings(d, t, dur):
    p = t / dur
    sit = ramp(t, dur * 0.45, 0.6)
    e = 1 - ramp(t, 0.2, dur * 0.5)
    qm = lerp(12.0, 13.0, sstep(p / 0.45))
    if sit < 0.5:
        mkw = dict(mode="walk", lean=lerp(0.1, -0.05, p), swing=0.3 * e, stride=0.6, energy=e, look=1.0 if p > 0.25 else 0.4,
                   phase=qm * math.pi * 1.0)
    else:
        mkw = dict(mode="sit", energy=0.0, look=lerp(1, -0.6, ramp(t, dur * 0.6, 0.8)))
    ch = _bg_climbers(3, p, {"MOT": (qm, mkw)})
    # close, low framing on Motivation with the endless stairs rising behind
    cam = cam_lerp(cam_on(12.0, 0.2, 1.05, dx=260, dy=-260), cam_on(13.0, 0.2, 1.35, dx=320, dy=-300), sstep(p))
    scene_world(d, cam, ch)
    # a little rain cloud forms over the sitting figure
    fx, fy = cam.p(*foot(qm, LANE["MOT"]))
    h = CH_H * cam.z
    ca = ramp(t, dur * 0.55, 0.8)
    cloud(d, fx + 20, fy - h * 1.55, h * 0.32, col(GREY, ca))
    for i in range(5):
        yy = fy - h * 1.45 + ((t * 2 + i * 0.37) % 1) * h * 0.45
        xx = fx - h * 0.25 + i * h * 0.12
        d.line([(xx, yy), (xx - 3, yy + h * 0.06)], fill=col((150, 170, 210, 255), ca * 0.8), width=3)
    top_caption(d, ["BUT FEELINGS DON'T", "LAST FOREVER."], t, dur, accent={"FEELINGS", "FOREVER."})


def s4_discipline(d, t, dur):
    p = t / dur
    qd = q_of(4, "DIS", p)
    ch = _bg_climbers(4, p, {"DIS": (qd, dict(mode="walk", lean=0.06, swing=0.45, stride=1.0))})
    ch["MOT"] = (13.0, dict(mode="sit", energy=0, look=-0.5))
    ch["OBS"] = (q_of(4, "OBS", p), dict(mode="stand", phase=0, look=0.8))
    cam = cam_lerp(cam_on(1.8, 0.6, 0.95, dx=120, dy=-150), cam_on(6.5, 0.6, 0.8, dx=160, dy=-160), p)
    scene_world(d, cam, ch, light=1 - 0.25 * p)
    # steady metronome ticks above Discipline: the same beat, every step
    fx, fy, h = cam.p(*foot(qd, LANE["DIS"])) + (CH_H * cam.z,)
    beat = (qd * 1.0) % 1
    for i in range(3):
        a = 0.7 * (1 - abs(beat - 0.5) * 2) if i == int(qd) % 3 else 0.18
        d.ellipse([fx - 40 + i * 40 - 7, fy - h * 1.62 - 7, fx - 40 + i * 40 + 7, fy - h * 1.62 + 7], fill=col(DIS, a))
    top_caption(d, ["DISCIPLINE DOESN'T CARE", "HOW YOU FEEL."], t, dur, accent={"DISCIPLINE", "FEEL."})


def s5_anyway(d, t, dur):
    p = t / dur
    qd = q_of(5, "DIS", p)
    ch = _bg_climbers(5, p, {"DIS": (qd, dict(mode="walk", lean=0.08, swing=0.45))})
    ch["MOT"] = (13.0, dict(mode="sit", energy=0, look=lerp(-0.5, 0.6, ramp(t, dur * 0.7, 0.5))))
    ch["OBS"] = (q_of(5, "OBS", p), dict(mode="stand", phase=0, look=1.0))
    cam = cam_lerp(cam_on(6.5, 0.6, 0.72, dx=60, dy=-140), cam_on(15, 0.6, 0.72, dx=-80, dy=-160), p)
    dark = ramp(t, 0.0, 0.8) * (1 - 0.4 * ramp(t, dur * 0.8, 0.6))
    scene_world(d, cam, ch, light=0.75 - 0.25 * dark)
    fx, fy = cam.p(*foot(qd, LANE["DIS"]))
    # thunder in the distance
    fl = max(0.0, 1 - abs(t - dur * 0.32) * 8) + 0.6 * max(0.0, 1 - abs(t - dur * 0.36) * 10)
    if fl > 0:
        bolt(d, W * 0.78, 140, fl)
    darkness(d, fx, fy - 60, 0.8 * dark)
    rain(d, t, 0.9 * ramp(t, 0.1, 0.6))
    flash(d, fl)
    pill(d, 210, H - 120, "RAIN", ramp(t, 0.4) * (1 - ramp(t, dur * 0.45, 0.3)) * 0.9, 24, inverted=False)
    pill(d, 210, H - 120, "DARKNESS", ramp(t, dur * 0.5) * 0.9, 24, inverted=False)
    top_caption(d, ["IT MOVES ANYWAY."], t, dur, accent={"ANYWAY."}, size=76)


def s6_obsession(d, t, dur):
    p = t / dur
    pk = p ** 1.6  # accelerating
    qo = lerp(0.2, 21.0, pk)
    spd = 1.6 * p ** 0.6
    ch = _bg_climbers(6, p, {"OBS": (qo, dict(mode="walk", lean=0.5, swing=1.0, stride=1.4, lift=1.4, streak=clamp(spd),
                                               phase=qo * math.pi * 0.9))})
    ch["MOT"] = (13.0, dict(mode="sit", energy=0, look=lerp(0.6, 1.0, p)))
    ch["DIS"] = (q_of(6, "DIS", p), dict(mode="walk", lean=0.08, swing=0.45))
    c0 = cam_on(0.2, 0.38, 0.9, dx=260, dy=-140)
    c1 = cam_on(21.0, 0.38, 0.62, dx=220, dy=-180)
    cam = cam_lerp(c0, c1, pk)
    shake = 6 * clamp(spd)
    cam.cx += math.sin(t * 47) * shake / cam.z
    cam.cy += math.cos(t * 39) * shake / cam.z
    fx, fy = cam.p(*foot(qo, LANE["OBS"]))
    paste(d, GLOW_RED, fx, fy - 80, 0.0)
    scene_world(d, cam, ch)
    paste(d, GLOW_RED, fx, fy - 90 * cam.z, 0.9, cam.z * 1.4)
    # speed lines across the frame
    rng = random.Random(int(t * 30))
    for i in range(int(18 * clamp(spd))):
        y = rng.uniform(220, H - 60)
        x = rng.uniform(0, W)
        ln = rng.uniform(120, 380)
        d.line([(x, y), (x - ln, y + ln * 0.62)], fill=col(WHITE, 0.15 + 0.15 * rng.random()), width=2)
    top_caption(d, ["OBSESSION MAKES YOU", "RELENTLESS."], t, dur, accent={"OBSESSION", "RELENTLESS."})


def s7_control(d, t, dur):
    p = t / dur
    # race on, slip at 30%, slide back a step, catch, then continue carefully
    t1, t2, t3 = 0.22, 0.48, 0.62
    if p < t1:
        qo, mode, lean = lerp(21.0, 22.6, p / t1), "walk", 0.5
    elif p < t2:
        u = (p - t1) / (t2 - t1)
        qo, mode, lean = lerp(22.6, 21.6, sstep(u)), "flail", lerp(0.2, -0.45, sstep(u * 2)) + 0.12 * math.sin(u * 20)
    elif p < t3:
        qo, mode, lean = 21.6, "crouch", 0.25
    else:
        qo, mode, lean = lerp(21.6, 23.0, (p - t3) / (1 - t3)), "walk", 0.12
    okw = dict(mode=mode, lean=lean, swing=1.0 if p < t1 else 0.35, stride=1.4 if p < t1 else 0.7,
               streak=0.8 if p < t1 else 0.0, phase=qo * math.pi * 0.9 if mode == "walk" else t * 6, tired=ramp(t, dur * t3, 0.4) * 0.7)
    ch = _bg_climbers(7, p, {"OBS": (qo, okw)})
    ch["MOT"] = (13.0, dict(mode="sit", energy=0))
    cam = cam_lerp(cam_on(21.0, 0.38, 0.95, dx=160, dy=-150), cam_on(22.5, 0.38, 1.2, dx=120, dy=-140), sstep(p))
    jolt = max(0.0, 1 - abs(p - t1 - 0.04) * 12)
    cam.cx += math.sin(t * 60) * 18 * jolt / cam.z
    cam.cy += math.cos(t * 53) * 14 * jolt / cam.z
    scene_world(d, cam, ch)
    fx, fy = cam.p(*foot(qo, LANE["OBS"]))
    if t1 < p < t3:  # little warning marks and a dust kick, nothing graphic
        a = ramp(t, dur * t1, 0.15) * (1 - ramp(t, dur * (t3 - 0.05), 0.3))
        h = CH_H * cam.z
        d.text((fx + h * 0.55, fy - h * 1.35), "!", font=font(int(h * 0.5)), fill=col(GOLD, a), anchor="mm")
        for i in range(4):
            r = h * (0.1 + 0.12 * i) * ramp(t, dur * t1, 0.5)
            d.arc([fx - r * 2, fy - r * 0.5, fx + r, fy + r * 0.4], 200, 340, fill=col(WHITE, a * (0.5 - i * 0.1)), width=3)
    top_caption(d, ["BUT INTENSITY WITHOUT CONTROL", "CAN DESTROY PROGRESS."], t, dur, accent={"CONTROL", "DESTROY"})


MONTAGE = [
    # tag, weather, camera zoom, camera dx, dy, day number
    ("MORNING", "morning", 0.95, 140, -170, 1),
    ("NIGHT", "night", 0.75, -60, -200, 38),
    ("RAIN", "rain", 1.15, 120, -140, 91),
    ("SNOW", "snow", 0.85, 200, -170, 140),
    ("DARKNESS", "dark", 1.0, 80, -150, 203),
    ("EXHAUSTION", "tired", 1.3, 60, -120, 266),
    ("ANOTHER DAY", "morning", 0.8, -120, -200, 312),
    ("ANOTHER STEP", "plain", 1.05, 140, -150, 365),
]


def montage(d, t, dur, scene, shots, caption_lines, accent):
    p = t / dur
    n = len(shots)
    i = min(n - 1, int(p * n))
    u = p * n - i
    name, wx, zoom, dx, dy, day = shots[i]
    qc = q_of(scene, "CON", p)
    tired = 1.0 if wx == "tired" else 0.0
    ch = _bg_climbers(scene, p, {"CON": (qc, dict(mode="walk", swing=0.3, stride=0.8 if not tired else 0.55, lean=0.05 + 0.2 * tired,
                                                  label_a=1.0, tired=tired, phase=qc * math.pi))})
    ch["MOT"] = (q_of(scene, "MOT", p), dict(mode="sit", energy=0))
    drift = lerp(-30, 30, u)
    cam = Cam(*cam_on(qc, 0.84, zoom, dx=dx + drift, dy=dy))
    light = {"night": 0.6, "dark": 0.55, "tired": 0.8}.get(wx, 1.0)
    if wx == "night":
        stars(d, 1.0)
        moon(d, W - 300, 330, 60, 1.0)
    if wx == "morning":
        sun(d, W - 360, 420, 70, 1.0)
    scene_world(d, cam, ch, light=light, trail=0.6)
    fx, fy = cam.p(*foot(qc, LANE["CON"]))
    if wx == "rain":
        rain(d, t, 0.9, seed=i)
    if wx == "snow":
        snow(d, t, 1.0, seed=i)
    if wx == "dark":
        darkness(d, fx, fy - 60, 0.95)
    if wx in ("night", "dark"):
        darkness(d, fx, fy - 60, 0.4)
    ta = ramp(u, 0.0, 0.15) * (1 - ramp(u, 0.85, 0.15))
    pill(d, 230, H - 120, name, ta, 26, inverted=True)
    tag(d, f"DAY {day}", ta * 0.9)
    # dip to black between shots
    dip = max(0.0, 1 - min(u, 1 - u) / 0.07) if 0 < i or u > 0.5 else 0.0
    if i == n - 1 and u > 0.5:
        dip = 0
    if dip > 0:
        d.rectangle([0, 0, W, H], fill=(0, 0, 0, int(200 * dip)))
    top_caption(d, caption_lines, t, dur, accent=accent)


def s8_consistency(d, t, dur):
    montage(d, t, dur, 8, MONTAGE[:4], ["CONSISTENCY DOESN'T NEED", "TO BE IMPRESSIVE."], {"CONSISTENCY", "IMPRESSIVE."})


def s9_again(d, t, dur):
    montage(d, t, dur, 9, MONTAGE[4:], ["IT JUST NEEDS TO", "HAPPEN AGAIN."], {"AGAIN."})


def s10_fastest(d, t, dur):
    p = t / dur
    qo = q_of(10, "OBS", sstep(p) * 0.6 + p * 0.4)
    ch = _bg_climbers(10, p, {
        "OBS": (qo, dict(mode="walk", lean=0.15, swing=0.35, stride=0.6, tired=0.8)),
        "DIS": (q_of(10, "DIS", p), dict(mode="walk", lean=0.08, swing=0.45)),
        "CON": (q_of(10, "CON", p), dict(mode="walk", swing=0.3, stride=0.8, label_a=1.0)),
        "MOT": (q_of(10, "MOT", p), dict(mode="walk", swing=0.2, stride=0.5, energy=0.25, lean=0.1)),
    })
    # start on the two "leaders", then pan up the stairs to find who is really ahead
    c0 = cam_on(32.5, 0.5, 0.85, dx=0, dy=-150)
    c1 = cam_on(35.0, 0.6, 0.5, dx=120, dy=-180)
    cam = cam_lerp(c0, c1, sstep(ramp(t, dur * 0.25, dur * 0.7)))
    scene_world(d, cam, ch, trail=0.8, summit_boost=0.3 * p)
    top_caption(d, ["BECAUSE THE PEOPLE WHO WIN", "AREN'T ALWAYS THE FASTEST."], t, dur, accent={"WIN", "FASTEST."})


def s11_showing_up(d, t, dur):
    p = t / dur
    arrive = 0.45
    qc = lerp(37.0, 41.6, sstep(p / arrive))
    at_top = p > arrive
    ckw = dict(mode="walk", swing=0.3, stride=0.8, label_a=1.0, phase=qc * math.pi)
    if at_top:
        ckw = dict(mode="stand", phase=0, label_a=1.0, face=-1 if p > arrive + 0.12 else 1, look=-0.3)
    ch = _bg_climbers(11, p, {
        "CON": (qc, ckw),
        "OBS": (q_of(11, "OBS", p), dict(mode="walk", lean=0.12, swing=0.3, stride=0.6, tired=0.6)),
        "DIS": (q_of(11, "DIS", p), dict(mode="walk", lean=0.08, swing=0.45)),
        "MOT": (q_of(11, "MOT", p), dict(mode="walk", swing=0.25, stride=0.5, energy=0.4, lean=0.1)),
    })
    # pull back slowly into the widest shot of the film
    c0 = cam_on(38.0, 0.8, 0.75, dx=100, dy=-170)
    c1 = (2300, -1850, 0.24)
    cam = cam_lerp(c0, c1, sstep(ramp(t, dur * 0.35, dur * 0.65)))
    boost = ramp(t, dur * arrive, 0.8)
    lit = int(N * ramp(t, dur * arrive, dur * 0.5))
    scene_world(d, cam, ch, trail=0.8 + 0.2 * boost, summit_boost=boost, lit_to=None)
    fx, fy = cam.p(*foot(qc, LANE["CON"]))
    if boost > 0:  # soft rings of light around the figure at the top
        for i in range(3):
            r = (60 + 90 * i + 40 * ((t * 0.8) % 1)) * cam.z * 2.2
            d.ellipse([fx - r, fy - r * 0.4 - 60 * cam.z, fx + r, fy + r * 0.4 - 60 * cam.z], outline=col(GOLD, boost * (0.35 - i * 0.1)), width=3)
    top_caption(d, ["THEY'RE THE ONES WHO", "KEEP SHOWING UP."], t, dur, accent={"SHOWING", "UP."})


# ---------------------------------------------------------------- final text
FINAL = [("MOT", "MOTIVATION", "STARTS YOU."), ("DIS", "DISCIPLINE", "KEEPS YOU MOVING."),
         ("OBS", "OBSESSION", "PUSHES YOU."), ("CON", "CONSISTENCY", "GETS YOU THERE.")]


def final_rows(d, t, dur, upto):
    if upto == 0:  # fade the summit shot to black behind the first line
        cam = Cam(2300, -1850, 0.24)
        a = 0.55 * (1 - ramp(t, 0.0, 1.4))
        if a > 0.01:
            ch = {w: (q, dict(mode="walk" if w != "CON" else "stand", phase=t * 3, label=False, a=a))
                  for w, q in (("CON", 41.6), ("OBS", 35.6), ("DIS", 34.0), ("MOT", 16.0))}
            scene_world(d, cam, ch, light=a, summit_boost=1.0)
    y0 = 300
    gap = 150
    f = font(66)
    bw = max(d.textlength(n + " " + r, font=f) for _, n, r in FINAL)
    X0 = W / 2 - (bw + 110) / 2
    for i in range(upto + 1):
        who, name, rest = FINAL[i]
        a = 1.0 if i < upto else ramp(t, 0.05, 0.4)
        dim = 0.45 if i < upto else 1.0
        if upto == 3 and i < 3:
            dim = 0.35
        y = y0 + i * gap + (1 - a) * 20
        h = 120
        figure(d, X0 + 30, y + h * 0.42, h, who, phase=t * 4 if who != "CON" else 0, mode="stand" if who == "CON" else "walk",
               swing=0.4, stride=0.6, label=False, a=a * (dim if who != "CON" else max(dim, 0.9)),
               energy=1.0)
        f = font(66)
        nw = d.textlength(name + " ", font=f)
        d.text((X0 + 110, y), name, font=f, fill=col(COLS[who] if who != "CON" else GOLD, a * dim), anchor="lm")
        caption_word(d, X0 + 110 + nw, y, rest, t if i == upto else 99, a * dim)


def caption_word(d, x, y, text, t, a):
    f = font(66)
    for j, w in enumerate(text.split()):
        k = ramp(t, 0.25 + 0.18 * j, 0.3)
        d.text((x, y + (1 - k) * 14), w, font=f, fill=col(WHITE, a * k), anchor="lm")
        x += d.textlength(w + " ", font=f)


def s12(d, t, dur):
    final_rows(d, t, dur, 0)


def s13(d, t, dur):
    final_rows(d, t, dur, 1)


def s14(d, t, dur):
    final_rows(d, t, dur, 2)


def s15(d, t, dur):
    final_rows(d, t, dur, 3)
    if t > dur * 0.4:  # Consistency's line glows
        paste(d, GLOW_GOLD, W / 2 - 470, 300 + 3 * 150 + 30, 0.6 * ramp(t, dur * 0.4, 0.6), 0.5)


def s16_tomorrow(d, t, dur):
    # one lit step, and the quiet white figure taking it
    cam = Cam(*cam_on(3.5, 0.5, 1.25, dx=60, dy=-80))
    k = sstep(ramp(t, 0.6, 1.4))
    q = lerp(2.6, 3.6, k)
    paste(d, GLOW_GOLD, *cam.p(*foot(3.5, 0.5)), 0.6 * ramp(t, 0.3, 1.0), 0.9)
    stairs(d, cam, 0.5, lit_to=None)
    x0, x1, y = 3 * RUN, 4 * RUN, Y(3)
    tq = [cam.p(x0, y), cam.p(x1, y), cam.p(x1 + OFF[0], y + OFF[1]), cam.p(x0 + OFF[0], y + OFF[1])]
    d.polygon(tq, fill=col((255, 214, 140, 255), 0.75 * ramp(t, 0.3, 0.8)))
    draw_char(d, cam, "CON", q, a=1.0, mode="walk" if 0 < k < 1 else "stand", phase=q * math.pi, swing=0.3, stride=0.8, label=False)
    d._image.alpha_composite(TOPBAND, (0, 0))
    a = ramp(t, 0.1, 0.5)
    d.text((W / 2, 170), "SHOW UP AGAIN", font=font(104), fill=col(WHITE, a), anchor="mm")
    d.text((W / 2, 290), "TOMORROW.", font=font(104), fill=col(GOLD, ramp(t, 0.6, 0.5)), anchor="mm")


SCENES = [s1_beginning, s2_motivation, s3_feelings, s4_discipline, s5_anyway, s6_obsession, s7_control,
          s8_consistency, s9_again, s10_fastest, s11_showing_up, s12, s13, s14, s15, s16_tomorrow, s_follow]
