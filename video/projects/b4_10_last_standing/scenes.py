"""THE LAST PERSON STANDING — a long road and the people who stop walking it.

World: a perspective road that runs to the horizon, first through desert at golden hour, then rain, snow and
night, toward a city of light. Unlike the other films, the camera lives on the road: behind the walkers,
ahead of them looking back, at ground level and high above. THE SPRINTER (red), THE PERFECTIONIST (blue,
glasses), THE DOUBTER (violet-grey) and THE CONSISTENT ONE (warm white, backpack), plus a few others who
quietly drop out along the way.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline, pill
from story import (Cam, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, sun, stars, moon,
                   top_caption, low_caption, final_card, shake, rain, snow, limb)
from kit import s_follow

TITLE = ("THE LAST", "PERSON STANDING")
OUTPUT = "100_The_Last_Person_Standing_16x9.mp4"
FOLLOW_SUB = ("FOR IDEAS, LESSONS, AND PERSPECTIVES", "THAT CHALLENGE THE WAY YOU THINK.")

LINES = [
    "Everyone starts.",
    "Some start too fast.",
    "Some never begin.",
    "Some convince themselves it's not worth it.",
    "And some…",
    "…simply keep going.",
    "Talent gets attention.",
    "Speed creates excitement.",
    "But persistence…",
    "…changes everything.",
    "Be the last person to quit.",
    "",
]
SPOKEN = [l.lstrip("…") for l in LINES]
GAPS = {0: 1.6, 1: 2.0, 2: 1.4, 3: 2.0, 4: 0.4, 5: 4.2, 6: 0.5, 7: 0.5, 8: 0.4, 9: 2.4, 10: 1.6}

SPR = (240, 70, 70, 255)
PER = (90, 150, 255, 255)
DOU = (160, 145, 190, 255)
CON = (245, 235, 215, 255)
EXTRA = (130, 120, 115, 255)
GOLD = (255, 200, 110, 255)
CH = 170
FIG = 210  # walker height in world units
ROAD_W = 300
FAR = 26000
CITY_Z = 24000


class PCam:
    """Perspective road camera. z runs along the road, x across it, y is height above the ground."""

    def __init__(self, x, z, h, dir=1, f=900, horizon=None, tilt=0):
        self.x, self.z, self.h, self.dir, self.f = x, z, h, dir, f
        self.horizon = horizon if horizon is not None else H * 0.48

    def p(self, x, z, y=0.0):
        dz = (z - self.z) * self.dir
        if dz < 5:
            return None
        s = self.f / dz
        return (W / 2 + (x - self.x) * s * self.dir, self.horizon + (self.h - y) * s, s)


ENV = {  # sky top, sky bottom, ground, road, sun?
    "dawn": ((40, 30, 70), (255, 170, 110), (120, 80, 60), (60, 50, 56)),
    "desert": ((60, 90, 160), (255, 200, 140), (200, 140, 90), (70, 60, 64)),
    "rain": ((30, 36, 50), (90, 100, 120), (60, 66, 70), (36, 40, 46)),
    "snow": ((120, 140, 170), (220, 225, 235), (230, 232, 240), (90, 92, 100)),
    "night": ((4, 6, 18), (30, 34, 70), (20, 22, 34), (24, 26, 34)),
    "gold": ((70, 40, 90), (255, 190, 120), (150, 100, 80), (66, 52, 58)),
}


def world(d, cam, t, env="desert", city=0.0, env2=None, k2=0.0):
    sky_t, sky_b, ground, road = ENV[env]
    if env2:
        o = ENV[env2]
        sky_t, sky_b, ground, road = (mix(sky_t, o[0], k2), mix(sky_b, o[1], k2), mix(ground, o[2], k2), mix(road, o[3], k2))
    hy = cam.horizon
    draw_sky(d, tuple(sky_t) + (255,), tuple(sky_b) + (255,), h=int(max(2, hy)) if hy > 2 else 2)
    if env in ("night",) or env2 == "night" and k2 > 0.5:
        stars(d, 1.0, seed=2, n=120, ymax=hy / H * 0.9)
    if env in ("dawn", "desert", "gold"):
        sun(d, W / 2 + 260 * cam.dir, hy - 40, 70, 0.9, (255, 220, 160, 255))
    # distant mountains on the horizon
    r = random.Random(5)
    pts = [(0, hy)]
    for i in range(25):
        pts.append((i * W / 24, hy - r.uniform(10, 70)))
    pts.append((W, hy))
    d.polygon(pts, fill=tuple(mix(sky_b, (60, 50, 80), 0.6)) + (255,))
    if city > 0 and cam.dir > 0:  # the destination: a city of light on the horizon
        c = cam.p(0, CITY_Z)
        if c:
            cx = c[0]
            glow(d, cx, hy - 20, 260 + 400 * city, GOLD, 0.5 + 0.4 * city)
            rr = random.Random(9)
            for i in range(22):
                bx = cx - 200 + i * 19
                bh = rr.uniform(20, 90) * (0.6 + city)
                d.rectangle([bx, hy - bh, bx + 14, hy], fill=col((255, 220, 160, 255), 0.6 + 0.4 * city))
    d.rectangle([0, hy, W, H], fill=tuple(ground) + (255,))
    # road
    near = cam.z + cam.dir * 40
    far = cam.z + cam.dir * FAR
    a, b = cam.p(-ROAD_W, near), cam.p(ROAD_W, near)
    c2, d2 = cam.p(ROAD_W, far), cam.p(-ROAD_W, far)
    if a and c2:
        d.polygon([(a[0], a[1]), (b[0], b[1]), (c2[0], c2[1]), (d2[0], d2[1])], fill=tuple(road) + (255,))
        for s in (-1, 1):  # edge lines
            q = [cam.p(s * (ROAD_W - 34), near), cam.p(s * (ROAD_W - 16), near), cam.p(s * (ROAD_W - 16), far), cam.p(s * (ROAD_W - 34), far)]
            d.polygon([(v[0], v[1]) for v in q], fill=(225, 215, 195, 255))
    # centre dashes
    z0 = math.floor(cam.z / 500) * 500
    for k in range(-2, 60):
        z = z0 + cam.dir * k * 500
        p0, p1 = cam.p(-8, z), cam.p(8, z + cam.dir * 220)
        if p0 and p1:
            q0, q1 = cam.p(8, z), cam.p(-8, z + cam.dir * 220)
            d.polygon([(p0[0], p0[1]), (q0[0], q0[1]), (p1[0], p1[1]), (q1[0], q1[1])], fill=(240, 220, 120, 230))


def roadside(d, cam, t, kind, density=1.0, seed=1):
    """Props on both sides of the road; drawn far to near."""
    r = random.Random(seed)
    items = []
    z0 = math.floor(cam.z / 700) * 700
    for k in range(-1, 40):
        z = z0 + cam.dir * k * 700
        for s in (-1, 1):
            rr = random.Random(int(z) * 3 + s)
            if rr.random() > density:
                continue
            x = s * rr.uniform(ROAD_W + 150, ROAD_W + 900)
            items.append((z, x, rr.random()))
    items.sort(key=lambda it: -(it[0] - cam.z) * cam.dir)
    for z, x, u in items:
        p = cam.p(x, z)
        if not p:
            continue
        sx, sy, s = p
        if kind == "desert":  # cactus
            hh = (180 + 120 * u) * s
            c = (60, 110, 70, 255)
            limb(d, (sx, sy), (sx, sy - hh), c, max(2, 40 * s))
            limb(d, (sx, sy - hh * 0.55), (sx + 50 * s, sy - hh * 0.55), c, max(2, 26 * s))
            limb(d, (sx + 50 * s, sy - hh * 0.55), (sx + 50 * s, sy - hh * 0.8), c, max(2, 26 * s))
        elif kind == "rain":  # telegraph pole
            hh = 520 * s
            d.line([(sx, sy), (sx, sy - hh)], fill=(40, 36, 34, 255), width=max(1, int(18 * s)))
            d.line([(sx - 70 * s, sy - hh * 0.9), (sx + 70 * s, sy - hh * 0.9)], fill=(40, 36, 34, 255), width=max(1, int(12 * s)))
        elif kind == "snow":  # pines with snow
            hh = (300 + 200 * u) * s
            d.polygon([(sx - 110 * s, sy), (sx, sy - hh), (sx + 110 * s, sy)], fill=(40, 70, 70, 255))
            d.polygon([(sx - 50 * s, sy - hh * 0.55), (sx, sy - hh), (sx + 50 * s, sy - hh * 0.55)], fill=(245, 245, 250, 255))
        elif kind == "night":  # street lamps
            hh = 480 * s
            d.line([(sx, sy), (sx, sy - hh)], fill=(60, 60, 70, 255), width=max(1, int(12 * s)))
            lx = sx - (60 * s if x > 0 else -60 * s)
            d.line([(sx, sy - hh), (lx, sy - hh)], fill=(60, 60, 70, 255), width=max(1, int(10 * s)))
            glow(d, lx, sy - hh + 10 * s, 260 * s, (255, 210, 150), 0.6)
            d.ellipse([lx - 14 * s, sy - hh - 4 * s, lx + 14 * s, sy - hh + 18 * s], fill=(255, 230, 180, 255))


def walker(d, cam, x, z, color, t, phase=0.0, mode="walk", facing=None, name=None, name_a=1.0, acc=(), a=1.0, speed=1.0,
           look_back=0.0, tired=0.0, lean=0.0):
    """Back or front view walker on the road (facing = 'away' / 'toward'), or side-view poses via `mode`."""
    p = cam.p(x, z)
    if not p:
        return None
    sx, sy, s = p
    h = FIG * s
    if h < 3:
        return p
    if facing is None:
        facing = "away" if cam.dir > 0 else "toward"
    if mode in ("sit", "kneel", "crouch", "slump", "stand_side"):
        figure(d, sx, sy, h, color, mode="stand" if mode == "stand_side" else mode, face=1 if x > 0 else -1, acc=acc, a=a,
               tired=tired, head_down=0.4 if mode in ("sit", "slump") else 0.0, name=name, name_a=name_a)
        return p
    c = col(color, a)
    back = col(dimc(color, 0.65), a)
    bob = abs(math.sin(phase)) * h * 0.03 * speed
    hip = (sx, sy - h * 0.46 - bob)
    for i, cc in ((0, back), (1, c)):
        side = -1 if i == 0 else 1
        lift = max(0.0, math.sin(phase + i * math.pi)) * speed
        foot = (sx + side * h * 0.07, sy - lift * h * 0.12)
        knee = (sx + side * h * 0.075, lerp(hip[1], foot[1], 0.5) - lift * h * 0.06)
        limb(d, (sx + side * h * 0.05, hip[1]), knee, cc, h * 0.08)
        limb(d, knee, foot, cc, h * 0.08)
    sh_y = hip[1] - h * 0.3
    if "backpack" in acc and facing == "away":
        d.rounded_rectangle([sx - h * 0.1, sh_y + h * 0.02, sx + h * 0.1, hip[1] - h * 0.02], int(h * 0.04), fill=col(dimc(color, 0.5), a))
    for i, cc in ((0, back), (1, back)):
        side = -1 if i == 0 else 1
        sw = math.sin(phase + i * math.pi) * speed
        hand = (sx + side * h * 0.16, sh_y + h * 0.28 - sw * h * 0.06)
        limb(d, (sx + side * h * 0.11, sh_y + h * 0.04), hand, cc, h * 0.065)
    d.rounded_rectangle([sx - h * 0.11, sh_y, sx + h * 0.11, hip[1] + h * 0.02], int(h * 0.08), fill=c)
    if "backpack" in acc and facing == "away":
        d.rounded_rectangle([sx - h * 0.09, sh_y + h * 0.04, sx + h * 0.09, hip[1] - h * 0.04], int(h * 0.04), fill=col(dimc(color, 0.5), a))
    hx = sx + look_back * h * 0.02
    hy = sh_y - h * 0.13
    r = h * 0.12
    if "headband" in acc:
        pass
    d.ellipse([hx - r, hy - r, hx + r, hy + r], fill=c)
    if facing == "away":
        d.chord([hx - r * 1.02, hy - r * 1.05, hx + r * 1.02, hy + r * 0.5], 180, 360, fill=col(dimc(color, 0.55), a))
        if look_back > 0:  # turning the head: one eye and a cheek visible
            er = r * 0.13
            d.ellipse([hx + r * 0.55 - er, hy - er, hx + r * 0.55 + er, hy + er], fill=(10, 10, 14, int(255 * a * look_back)))
    else:
        d.chord([hx - r * 1.02, hy - r * 1.1, hx + r * 1.02, hy + r * 0.1], 180, 360, fill=col(dimc(color, 0.55), a))
        er = r * 0.13
        for o in (-0.35, 0.35):
            d.ellipse([hx + o * r - er, hy - er * 1.2, hx + o * r + er, hy + er * 1.2], fill=(10, 10, 14, int(255 * a)))
        if "glasses" in acc:
            for o in (-0.35, 0.35):
                d.ellipse([hx + o * r - er * 2.4, hy - er * 2.4, hx + o * r + er * 2.4, hy + er * 2.4], outline=(10, 10, 14, int(255 * a)), width=max(1, int(er * 0.6)))
    if "headband" in acc:
        d.line([(hx - r, hy - r * 0.35), (hx + r, hy - r * 0.35)], fill=col((250, 250, 250, 255), a), width=max(1, int(r * 0.3)))
    if tired > 0:
        d.ellipse([hx + r * 1.1, hy - r * 0.2 + (t * 3 % 1) * r, hx + r * 1.3, hy + r * 0.1 + (t * 3 % 1) * r], fill=col((170, 210, 255, 255), tired * a))
    if name and name_a > 0.01:
        d.text((hx, hy - r - h * 0.12), name, font=font(int(clamp(h * 0.14, 14, 34))), fill=col(color, a * name_a), anchor="mm")
    return p


def draw_people(d, cam, t, people):
    """people: list of (x, z, color, kwargs); drawn far to near."""
    for x, z, c, kw in sorted(people, key=lambda q: -(q[1] - cam.z) * cam.dir):
        walker(d, cam, x, z, c, t, **kw)


START_X = {"SPR": -180, "PER": -60, "DOU": 60, "CON": 180, "E1": -240, "E2": 0, "E3": 240}


# ---------------------------------------------------------------- scenes
def _one_at_a_time(t, dur, k):
    order = ["SPR", "PER", "DOU", "CON"]
    if k not in order:
        return 0.0
    i = order.index(k)
    st = dur * 0.08 + i * dur * 0.12
    return ramp(t, st, 0.15) * (1 - ramp(t, st + dur * 0.12, 0.15)) if i < 3 else ramp(t, st, 0.15)


def s0_everyone(d, t, dur):
    p = t / dur
    # hook: low behind the start line at dawn, the group in silhouette; then everybody sets off
    cam = PCam(0, lerp(-650, -500, p), lerp(90, 180, sstep(p)), 1, horizon=H * lerp(0.62, 0.5, sstep(p)))
    world(d, cam, t, "dawn")
    sl = [cam.p(-ROAD_W, 0), cam.p(ROAD_W, 0), cam.p(ROAD_W, 60), cam.p(-ROAD_W, 60)]
    if all(sl):
        d.polygon([(q[0], q[1]) for q in sl], fill=(240, 240, 240, 255))
    go = ramp(t, dur * 0.55, 0.4)
    people = []
    for k, c, acc in (("SPR", SPR, ("headband",)), ("PER", PER, ("glasses",)), ("DOU", DOU, ()), ("CON", CON, ("backpack",)),
                      ("E1", EXTRA, ()), ("E2", EXTRA, ()), ("E3", EXTRA, ())):
        z = -40 + (k.startswith("E")) * -120 + go * 200 * (1 if k != "PER" else 0) + (go * 300 if k == "SPR" else 0)
        people.append((START_X[k], z, c, dict(phase=t * 6 if go > 0 and k != "PER" else 0, speed=go if k != "PER" else 0, acc=acc,
                                              name={"SPR": "THE SPRINTER", "PER": "THE PERFECTIONIST", "DOU": "THE DOUBTER", "CON": "THE CONSISTENT ONE"}.get(k),
                                              name_a=_one_at_a_time(t, dur, k) * (1 - go))))
    draw_people(d, cam, t, people)
    top_caption(d, ["EVERYONE STARTS."], t, dur, accent={"EVERYONE"})


def s1_fast(d, t, dur):
    p = t / dur
    # front view, camera far down the road looking back: the sprinter flies toward us... and stalls
    zs = lerp(300, 2600, 1 - (1 - min(1, p / 0.6)) ** 2)
    stop = p > 0.6
    cam = PCam(0, 3600, 160, -1, horizon=H * 0.5)
    world(d, cam, t, "desert")
    roadside(d, cam, t, "desert", 0.5)
    people = [(-60, 200, PER, dict(speed=0, acc=("glasses",))), (60, 280 + 120 * p, DOU, dict(phase=t * 5, speed=0.7)),
              (180, 300 + 150 * p, CON, dict(phase=t * 5, speed=0.7, acc=("backpack",))),
              (-240, 200 + 120 * p, EXTRA, dict(phase=t * 5, speed=0.7)), (0, 180 + 100 * p, EXTRA, dict(phase=t * 5, speed=0.7)),
              (240, 220 + 130 * p, EXTRA, dict(phase=t * 5, speed=0.7))]
    if stop:
        people.append((-200, zs, SPR, dict(mode="sit", tired=1.0, acc=("headband",))))
    else:
        people.append((-180, zs, SPR, dict(phase=t * 14, speed=1.6 * (1 - p / 0.6) + 0.4, acc=("headband",), name="THE SPRINTER", tired=p)))
    draw_people(d, cam, t, people)
    top_caption(d, ["SOME START TOO FAST."], t, dur, accent={"FAST."})


def s2_never(d, t, dur):
    p = t / dur
    # side view at the start line: the perfectionist checks laces, gear, watch, sky — and never leaves
    cam = Cam(0, -150, 1.6)
    draw_sky(d, (60, 90, 160, 255), (255, 200, 140, 255))
    sun(d, W * 0.8, H * 0.4, 60, 0.9)
    gy = cam.p(0, 0)[1]
    d.rectangle([0, gy, W, H], fill=(200, 140, 90, 255))
    d.rectangle([0, gy, W, gy + 90], fill=(70, 60, 64, 255))
    d.rectangle([cam.p(-60, 0)[0], gy, cam.p(-20, 0)[0], gy + 90], fill=(240, 240, 240, 255))
    d.text((cam.p(-200, 0)[0], gy + 45), "START", font=font(48), fill=(240, 240, 240, 255), anchor="mm")
    acts = ["kneel", "point", "stand", "reach"]
    i = min(3, int(p * 4))
    fx, fy = cam.p(-140, 0)
    figure(d, fx, fy, cam.s(CH), PER, mode=acts[i], face=1, look=[-0.6, 0.0, 1.0, 0.6][i], acc=("glasses", "hair"), name="THE PERFECTIONIST",
           head_down=0.6 if i == 0 else 0.0)
    lbl = ["CHECKING SHOES…", "WAITING FOR THE RIGHT TIME…", "NOT YET…", "ALMOST READY…"][i]
    pill(d, W / 2, H - 120, lbl, 0.9, 30, inverted=False)
    top_caption(d, ["SOME NEVER BEGIN."], t, dur, accent={"NEVER"})


def s3_doubt(d, t, dur):
    p = t / dur
    # behind the doubter: it slows, looks back over its shoulder, and turns around toward us
    turn = sstep(ramp(t, dur * 0.45, 0.4))
    zd = 1100 + 500 * sstep(min(1, p / 0.45)) - 600 * sstep(ramp(t, dur * 0.6, dur * 0.4))
    cam = PCam(80, 400 + 200 * p, 200, 1, horizon=H * 0.5)
    world(d, cam, t, "desert")
    roadside(d, cam, t, "desert", 0.5)
    people = [(180, 1500 + 900 * p, CON, dict(phase=t * 5, speed=0.7, acc=("backpack",))),
              (-200, 2900, SPR, dict(mode="sit", tired=0.6)),
              (60, zd, DOU, dict(phase=t * 4, speed=0.6 if p < 0.4 or p > 0.6 else 0.1, look_back=ramp(t, dur * 0.25, 0.3),
                                 facing="away" if turn < 0.5 else "toward", name="THE DOUBTER"))]
    draw_people(d, cam, t, people)
    q = cam.p(60, zd)
    if q and 0.2 < p < 0.75:
        for j in range(3):
            d.text((q[0] + (j - 1) * 50 * q[2], q[1] - FIG * q[2] * 1.3 - j * 20), "?", font=font(int(clamp(60 * q[2], 20, 80))),
                   fill=col(WHITE, 0.8 * ramp(t, dur * (0.2 + 0.1 * j), 0.2)), anchor="mm")
    top_caption(d, ["SOME CONVINCE THEMSELVES", "IT'S NOT WORTH IT."], t, dur, accent={"CONVINCE", "WORTH"})


def s4_some(d, t, dur):
    p = t / dur
    cam = PCam(180, 2000 + 300 * p, 120, 1, horizon=H * 0.55)
    world(d, cam, t, "desert", env2="gold", k2=p)
    roadside(d, cam, t, "desert", 0.5)
    draw_people(d, cam, t, [(180, 2450 + 300 * p, CON, dict(phase=t * 5, speed=0.7, acc=("backpack",), name="THE CONSISTENT ONE"))])
    top_caption(d, ["AND SOME…"], t, dur, accent={"SOME…"})


MONTAGE = [("rain", "rain", "RAIN"), ("snow", "snow", "SNOW"), ("night", "night", "NIGHT"), ("desert", "desert", "HEAT"), ("night", "night", "ALONE")]


def s5_keep_going(d, t, dur):
    p = t / dur
    n = len(MONTAGE)
    i = min(n - 1, int(p * n))
    u = p * n - i
    env, props, lbl = MONTAGE[i]
    zc = 4000 + 3500 * p
    views = [PCam(180, zc - 450, 130, 1), PCam(-300, zc - 900, 420, 1), PCam(180, zc + 900, 150, -1), PCam(500, zc - 300, 60, 1), PCam(0, zc - 2400, 1100, 1)]
    cam = views[i]
    world(d, cam, t, env)
    roadside(d, cam, t, props, 0.6, seed=i)
    people = [(180, zc, CON, dict(phase=t * 5, speed=0.7, acc=("backpack",), tired=0.6 if i == 3 else 0.0))]
    if i in (1, 3):  # others who quit, sitting at the roadside as it passes
        people.append((-420, zc + 600 - 400 * u, EXTRA, dict(mode="sit")))
    draw_people(d, cam, t, people)
    if env == "rain":
        rain(d, t, 0.9, n=200)
    if env == "snow":
        snow(d, t, 1.0, n=160)
    a = ramp(u, 0.05, 0.15) * (1 - ramp(u, 0.85, 0.15))
    pill(d, 220, H - 120, lbl, a, 30, inverted=True)
    pill(d, W - 220, H - 120, f"KM {int(4 + 3.5 * p * 100)}", a * 0.9, 28, inverted=False)
    dip = max(0.0, 1 - min(u, 1 - u) / 0.06) if (i > 0 or u > 0.5) and not (i == n - 1 and u > 0.5) else 0
    overlay(d, (0, 0, 0), 0.85 * dip)
    top_caption(d, ["…SIMPLY KEEP GOING."], t, dur, accent={"KEEP", "GOING."})


def high(d, t, dur, part):
    """Crane shot rising over the nearly empty road."""
    p = t / dur
    k = (part + p) / 4
    zc = 7600 + 9000 * k
    cam = PCam(0, zc - lerp(1200, 4000, k), lerp(500, 2600, k), 1, f=900, horizon=H * lerp(0.42, 0.28, k))
    env = "night" if k < 0.5 else "gold"
    world(d, cam, t, env if k < 0.45 else "gold", city=ramp(k, 0.3, 0.6), env2="gold" if k < 0.5 else None, k2=sstep(ramp(k, 0.3, 0.2)))
    people = [(180, zc, CON, dict(phase=t * 5, speed=0.7, acc=("backpack",)))]
    # the others, far behind, where they stopped
    people += [(-200, 2900, SPR, dict(mode="sit")), (-60, 0, PER, dict(mode="stand_side")), (60, 200, DOU, dict(facing="toward", speed=0.4, phase=t * 4))]
    draw_people(d, cam, t, people)
    q = cam.p(180, zc)
    if q:  # a soft light following the one who kept going
        glow(d, q[0], q[1] - FIG * q[2] * 0.5, max(60, FIG * q[2] * 2.5), GOLD, 0.5)
    return cam


def s6(d, t, dur):
    high(d, t, dur, 0)
    # talent gets attention: camera flashes around the sprinter, far behind
    top_caption(d, ["TALENT GETS ATTENTION."], t, dur, accent={"TALENT"})


def s7(d, t, dur):
    high(d, t, dur, 1)
    top_caption(d, ["SPEED CREATES EXCITEMENT."], t, dur, accent={"SPEED"})
s7.seamless = True


def s8(d, t, dur):
    high(d, t, dur, 2)
    top_caption(d, ["BUT PERSISTENCE…"], t, dur, accent={"PERSISTENCE…"})
s8.seamless = True


def s9_everything(d, t, dur):
    p = t / dur
    # back on the ground behind the walker as the city of light opens up ahead
    zc = lerp(20500, 23400, sstep(p))
    cam = PCam(180, zc - 600, 140, 1, horizon=H * 0.55)
    world(d, cam, t, "gold", city=1.0)
    c = cam.p(0, CITY_Z)
    if c:
        glow(d, c[0], cam.horizon - 30, 500 + 700 * p, GOLD, 0.6 + 0.4 * p)
    draw_people(d, cam, t, [(180, zc, CON, dict(phase=t * 5, speed=0.7, acc=("backpack",)))])
    overlay(d, (255, 220, 170), 0.25 * ramp(p, 0.75, 0.25))
    top_caption(d, ["…CHANGES EVERYTHING."], t, dur, accent={"EVERYTHING."})


def s10_final(d, t, dur):
    cam = PCam(180, 22800, 140, 1, horizon=H * 0.55)
    world(d, cam, t, "gold", city=1.0)
    draw_people(d, cam, t, [(180, 23400, CON, dict(phase=0, speed=0, acc=("backpack",)))])
    overlay(d, (0, 0, 0), 0.55)
    final_card(d, t, dur, ["BE THE LAST", "PERSON TO QUIT."], [WHITE, GOLD], size=110, glow_col=GOLD)


SCENES = [s0_everyone, s1_fast, s2_never, s3_doubt, s4_some, s5_keep_going, s6, s7, s8, s9_everything, s10_final, s_follow]
