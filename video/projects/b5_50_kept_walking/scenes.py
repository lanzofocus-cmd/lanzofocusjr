"""THE ONE WHO KEPT WALKING — the finale: a thousand dreamers at the start line, one at the end of the road.

World: one long road through five lands, a single journey. Overhead, a sea of heads crowds a painted start line.
Behind them, everyone walks toward a star on the horizon with a little dream glowing over each head. Then a long
side-on tracking shot: green meadow, amber desert, a white blizzard, night mountains, a sunrise plateau. Along the
way people sprint ahead and collapse, sit down, stop, turn around and walk home. THE WALKER (gold) never runs and
never stops. Alone in the snow; climbing in the dark; and at sunrise the gate at the end of the road, the long way
back lit with tiny figures. KEEP GOING.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, PCam, back_figure, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure,
                   particles, top_caption, final_card, stage_end, shake, dust, snow, stars, sun)
from kit import s_follow

TITLE = ("THE ONE WHO", "KEPT WALKING")
OUTPUT = "150_The_One_Who_Kept_Walking_16x9.mp4"
LINES = [
    "",
    "Everyone starts with a dream.",
    "Not everyone stays.",
    "",
    "The difference…",
    "…is who keeps walking.",
    "",
    "",
]
SPOKEN = ["", "Everyone starts with a dream.", "Not everyone stays.", "", "The difference…", "is who keeps walking.", "", ""]
SILENT = {0: 3.4, 3: 3.4, 6: 3.6}
GAPS = {1: 3.4, 2: 5.6, 4: 3.6, 5: 7.0}

GOLD = (255, 200, 80, 255)
CROWD = [(120, 200, 255), (255, 130, 130), (150, 230, 150), (220, 160, 255), (255, 170, 90), (200, 200, 210), (120, 230, 220),
         (255, 150, 210)]
CH = 200
BIOMES = [  # x start, sky top, sky bottom, ground
    (0, (90, 150, 230), (200, 230, 255), (90, 150, 80)),
    (3000, (230, 140, 80), (255, 215, 150), (215, 170, 110)),
    (6000, (110, 120, 150), (200, 210, 230), (232, 236, 246)),
    (9000, (25, 25, 70), (90, 70, 120), (80, 70, 100)),
    (12000, (255, 160, 110), (255, 230, 180), (170, 130, 110)),
]
GATE = 12700


def ground_y(x):
    if x < 9000:
        return 0.0
    if x < 12000:
        u = (x - 9000) / 3000
        return -1100 * (u - math.sin(u * math.tau * 3) / (math.tau * 3))   # switchback-ish rising slope
    return -1100.0


def biome_at(x):
    for i in range(len(BIOMES) - 1, -1, -1):
        if x >= BIOMES[i][0]:
            j = min(i + 1, len(BIOMES) - 1)
            u = sstep(clamp((x - BIOMES[j][0] + 700) / 700)) if j != i else 0
            a, b = BIOMES[i], BIOMES[j]
            return tuple(mix(a[k] + (255,), b[k] + (255,), u) for k in (1, 2, 3))
    return tuple(c + (255,) for c in BIOMES[0][1:])


def land(d, cam, t, sky_x=None):
    top, bot, gnd = biome_at(sky_x if sky_x is not None else cam.cx)
    draw_sky(d, top, bot)
    bx = sky_x if sky_x is not None else cam.cx
    if 9000 <= bx < 12300:
        stars(d, clamp(1 - (bx - 10800) / 1200))
    if bx > 11000:
        sun(d, W * 0.72, cam.p(0, -1150)[1] + 40 - 120 * clamp((bx - 11000) / 1600), 90, clamp((bx - 11000) / 1200), (255, 220, 160, 255))
    # far mountains, parallax
    r = random.Random(4)
    pts = []
    for i in range(-2, 24):
        x = i * 120 - (cam.cx * 0.08) % 120
        pts.append((x, H * 0.55 - r.uniform(40, 200) * (1.5 if bx > 8000 else 0.8) - cam.cy * 0.08 * cam.z))
    d.polygon(pts + [(W, H), (0, H)], fill=dimc(mix(bot, (80, 80, 110, 255), 0.5), 0.8))
    # ground following the road
    xs = range(int(cam.cx - W / cam.z) // 100 * 100 - 200, int(cam.cx + W / cam.z) + 300, 100)
    top_pts = [cam.p(x, ground_y(x)) for x in xs]
    d.polygon(top_pts + [(top_pts[-1][0], H + 50), (top_pts[0][0], H + 50)], fill=gnd)
    for x in xs:
        g = biome_at(x + 50)[2] if cam.z < 0.3 else gnd
        a0, a1 = cam.p(x, ground_y(x)), cam.p(x + 101, ground_y(x + 101))
        if cam.z < 0.3:
            d.polygon([a0, a1, cam.p(x + 101, ground_y(x + 101) + 260), cam.p(x, ground_y(x) + 260)], fill=g)
        r0, r1 = cam.p(x, ground_y(x) + 30), cam.p(x + 101, ground_y(x + 101) + 30)
        q0, q1 = cam.p(x + 101, ground_y(x + 101) + 90), cam.p(x, ground_y(x) + 90)
        d.polygon([r0, r1, q0, q1], fill=dimc(g, 0.82))
    # props per biome
    for x in xs:
        if x % 300:
            continue
        rr = random.Random(x)
        px = x + rr.uniform(-80, 80)
        gy = ground_y(px)
        sx, sy = cam.p(px, gy)
        s = cam.s(1)
        if px < 3000:
            d.rectangle([sx - 8 * s, sy - 160 * s, sx + 8 * s, sy], fill=(90, 70, 50, 255))
            d.ellipse([sx - 70 * s, sy - 260 * s, sx + 70 * s, sy - 130 * s], fill=(70, 140, 70, 255))
        elif px < 6000:
            if rr.random() < 0.6:
                c = (90, 140, 80, 255)
                d.rounded_rectangle([sx - 14 * s, sy - 150 * s, sx + 14 * s, sy], int(12 * s) + 1, fill=c)
                d.rounded_rectangle([sx - 50 * s, sy - 110 * s, sx - 36 * s, sy - 60 * s], int(6 * s) + 1, fill=c)
                d.line([(sx - 43 * s, sy - 62 * s), (sx - 10 * s, sy - 62 * s)], fill=c, width=max(2, int(12 * s)))
        elif px < 9000:
            d.polygon([(sx, sy - 220 * s), (sx - 70 * s, sy), (sx + 70 * s, sy)], fill=(50, 80, 70, 255))
            d.polygon([(sx, sy - 220 * s), (sx - 30 * s, sy - 130 * s), (sx + 30 * s, sy - 130 * s)], fill=(240, 245, 255, 255))
        elif px < 12000:
            d.polygon([(sx - 60 * s, sy), (sx - 20 * s, sy - 90 * s), (sx + 50 * s, sy - 60 * s), (sx + 70 * s, sy)], fill=(60, 55, 80, 255))


def gate(d, cam, t, glow_a=1.0):
    gy = ground_y(GATE)
    for o in (-160, 160):
        d.rectangle(cam.box(GATE + o - 30, gy - 600, GATE + o + 30, gy + 40), fill=(240, 220, 190, 255))
    a, b = cam.p(GATE - 200, gy - 700), cam.p(GATE + 200, gy - 500)
    d.arc([a[0], a[1], b[0], b[1] + (b[1] - a[1])], 180, 360, fill=(240, 220, 190, 255), width=max(3, int(cam.s(40))))
    cx, cy = cam.p(GATE, gy - 300)
    glow(d, cx, cy, cam.s(900), (255, 220, 150), 0.6 * glow_a)
    tpoly(d, [cam.p(GATE - 130, gy - 600), cam.p(GATE + 130, gy - 600), cam.p(GATE + 130, gy + 30), cam.p(GATE - 130, gy + 30)],
          (255, 240, 200, int(200 * glow_a)))


def walker(d, cam, x, t, mode="walk", depth=50, **kw):
    fx, fy = cam.p(x, ground_y(x) + depth)
    figure(d, fx, fy, cam.s(CH), GOLD, mode=mode, phase=kw.pop("phase", x / 38), face=kw.pop("face", 1), acc=("scarf",),
           name=kw.pop("name", "THE WALKER"), eye_col=(60, 40, 10, 255), **kw)
    return fx, fy


# the crowd's fates for the long tracking shot (fate, stop progress, offset, depth)
FATES = []
_r = random.Random(21)
for i in range(18):
    fate = ["sprint", "sit", "turn", "stop", "sit", "sprint", "turn", "stop", "sit"][i % 9]
    FATES.append((fate, _r.uniform(0.12, 0.85), _r.uniform(-700, 500), _r.uniform(10, 85), CROWD[i % len(CROWD)] + (255,)))


def crowd(d, cam, t, p, xw, x_of):
    """Draw the crowd during the long tracking shot; xw = the walker's x at progress p, x_of(p) gives it at any p."""
    order = sorted(range(len(FATES)), key=lambda i: FATES[i][3])
    for i in order:
        fate, ps, off, dep, c = FATES[i]
        boost = 1800 if fate == "sprint" else 0
        if p < ps:
            x = x_of(p) + off + boost * p / ps * ps
            mode, face, extra = ("run" if fate == "sprint" else "walk"), 1, {}
        else:
            x = x_of(ps) + off + boost * ps
            q = p - ps
            if fate == "sprint":
                mode, face, extra = "slump", 1, dict(tired=1.0)
            elif fate == "sit":
                mode, face, extra = "sit", 1, dict(head_down=True)
            elif fate == "turn":
                x -= q * 2500
                mode, face, extra = "walk", -1, dict(head_down=True)
            else:
                mode, face, extra = "stand", 1, dict(look=-0.3)
        fx, fy = cam.p(x, ground_y(x) + dep)
        if -200 < fx < W + 200:
            figure(d, fx, fy, cam.s(CH * 0.95), c, mode=mode, phase=x / 36, face=face, eyes=False, mouth=0, **extra)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # overhead: a sea of heads packed at a painted start line; a star appears at the top; every head turns to it
    z = lerp(1.0, 1.25, p)
    d.rectangle([0, 0, W, H], fill=(70, 120, 70, 255))
    d.rectangle([W / 2 - 520 * z, 0, W / 2 + 520 * z, H], fill=(90, 90, 100, 255))
    d.rectangle([W / 2 - 520 * z, H * 0.3 - 10 * z, W / 2 + 520 * z, H * 0.3 + 10 * z], fill=(245, 245, 245, 255))
    d.text((W / 2, H * 0.3 - 50 * z), "START", font=font(int(46 * z)), fill=(245, 245, 245, 255), anchor="mm")
    look = sstep(ramp(p, 0.45, 0.25))
    r = random.Random(1)
    for i in range(260):
        x = W / 2 + r.uniform(-500, 500) * z
        y = H * 0.3 + 30 * z + r.uniform(0, 900) * z
        if y > H + 40:
            continue
        gold = i == 37
        c = GOLD if gold else CROWD[i % len(CROWD)] + (255,)
        jx = math.sin(t * 2 + i) * 3
        rr = (26 if gold else 22) * z
        d.ellipse([x - rr * 1.5 + jx, y - rr * 0.7, x + rr * 1.5 + jx, y + rr * 0.9], fill=dimc(c, 0.7))   # shoulders
        d.ellipse([x - rr + jx, y - rr - 6 * z, x + rr + jx, y + rr - 6 * z], fill=c)
        d.ellipse([x - rr * 0.5 + jx, y - rr * 0.5 - 6 * z - rr * 0.6 * look, x + rr * 0.5 + jx, y + rr * 0.5 - 6 * z - rr * 0.6 * look],
                  fill=dimc(c, 0.6))   # the face tilting up
        if gold:
            glow(d, x, y, 120 * z, GOLD[:3], 0.4)
    sy = lerp(-60, 70, look)
    glow(d, W / 2, sy, 260, (255, 230, 150), 0.7 * look)
    d.ellipse([W / 2 - 22, sy - 22, W / 2 + 22, sy + 22], fill=(255, 240, 190, int(255 * look)))


def s1_dream(d, t, dur):
    p = t / dur
    # from behind: the crowd walks toward the star on the horizon, a little dream glowing over every head
    wz = p * 900
    cam = PCam(0, wz - 700, 360, horizon=H * 0.5)
    draw_sky(d, (90, 150, 230, 255), (220, 235, 255, 255))
    glow(d, W / 2, H * 0.36, 300, (255, 230, 150), 0.7)
    d.ellipse([W / 2 - 18, H * 0.36 - 18, W / 2 + 18, H * 0.36 + 18], fill=(255, 245, 200, 255))
    d.rectangle([0, H * 0.5, W, H], fill=(90, 150, 80, 255))
    q = cam.quad([(-500, wz - 650, 0), (500, wz - 650, 0), (500, wz + 9000, 0), (-500, wz + 9000, 0)])
    if q:
        d.polygon(q, fill=(110, 110, 120, 255))
    r = random.Random(3)
    people = []
    for i in range(70):
        x = r.uniform(-460, 460)
        z = r.uniform(-300, 2600) + wz * 0.95
        people.append((z, x, i))
    for z, x, i in sorted(people, reverse=True):
        v = cam.p(x, z)
        if not v:
            continue
        sx, sy, s = v
        c = GOLD if i == 5 else CROWD[i % len(CROWD)] + (255,)
        back_figure(d, sx, sy, CH * s, c, t, phase=t * 6 + i, speed=1.0, acc=("scarf",) if i == 5 else ())
        k = sstep(ramp(p, 0.15 + (i % 7) * 0.05, 0.2))
        if k > 0 and CH * s > 12:
            gy = sy - CH * s * 1.25 - math.sin(t * 2 + i) * 4
            glow(d, sx, gy, CH * s * 0.25, (255, 230, 150), 0.5 * k)
            d.ellipse([sx - CH * s * 0.05, gy - CH * s * 0.05, sx + CH * s * 0.05, gy + CH * s * 0.05], fill=(255, 245, 200, int(255 * k)))
    top_caption(d, ["EVERYONE STARTS", "WITH A DREAM."], t, dur, accent={"DREAM."})


def x_s2(p):
    return lerp(400, 5800, p)


def s2_stays(d, t, dur):
    p = t / dur
    # the long tracking shot: meadow to desert; people sprint and collapse, sit, stop, turn back for home
    xw = x_s2(p)
    cam = Cam(xw + 250, -330, 0.62)
    land(d, cam, t)
    crowd(d, cam, t, p, xw, x_s2)
    walker(d, cam, xw, t, mode="walk", name="THE WALKER" if p < 0.5 else "")
    dust(d, t, 0.3 * clamp((xw - 3000) / 1000), n=30, color=(255, 220, 170))
    top_caption(d, ["NOT EVERYONE", "STAYS."], t, dur, accent={"STAYS."})


def s3_alone(d, t, dur):
    p = t / dur
    # the pause: alone in a white blizzard; one last companion sits down in the snow; the walker keeps on
    xw = lerp(6300, 8600, p)
    cam = Cam(xw + 150, -300, 0.75)
    land(d, cam, t)
    shake(cam, t, 1.5)
    cx = min(xw, 7000) - 130
    fx, fy = cam.p(cx, 70)
    figure(d, fx, fy, cam.s(CH * 0.95), CROWD[0] + (255,), mode="sit" if xw > 7000 else "walk", phase=t * 5, face=1, eyes=False, mouth=0,
           head_down=True)
    walker(d, cam, xw, t, mode="walk", lean=0.2, name="", head_down=False)
    snow(d, t, 1.0, n=220)
    fog(d, W / 2, H * 0.5, W * 1.5, 0.3, (230, 235, 250))


def s4_difference(d, t, dur):
    p = t / dur
    # night mountains: the climb; slow, steady, step after step up the switchbacks; the sky starts to pale
    xw = lerp(9100, 11600, p)
    cam = Cam(xw + 100, ground_y(xw) - 280, 0.7)
    land(d, cam, t)
    walker(d, cam, xw, t, mode="walk", lean=0.25, name="", tired=0.4)
    top_caption(d, ["THE DIFFERENCE…"], t, dur, accent={"DIFFERENCE…"})


def s5_keeps(d, t, dur):
    p = t / dur
    # sunrise plateau: the gate at the end of the road; the walker arrives, turns, and the camera pulls back
    # over the whole long road behind, dotted with the tiny figures who stopped
    arrive = sstep(ramp(p, 0.0, 0.45))
    xw = lerp(11700, GATE - 40, arrive)
    pull = sstep(ramp(p, 0.5, 0.5))
    cam = cam_lerp((xw, -1350, 0.75), (9800, -750, 0.15), pull)
    land(d, cam, t, sky_x=lerp(xw, 12400, pull))
    if pull > 0.05:
        crowd(d, cam, t, 1.0, x_s2(1.0), x_s2)
    gate(d, cam, t, glow_a=0.5 + 0.5 * arrive)
    walker(d, cam, xw, t, mode="walk" if arrive < 0.98 else ("stand" if p < 0.55 else "cheer"), face=1 if p < 0.55 else -1,
           mouth=0.7 * arrive, name="")
    top_caption(d, ["IS WHO KEEPS", "WALKING."], t, dur, accent={"KEEPS", "WALKING."})


def s6_end(d, t, dur):
    cam = Cam(9800, -750, 0.15)
    land(d, cam, t, sky_x=12400)
    crowd(d, cam, t, 1.0, x_s2(1.0), x_s2)
    gate(d, cam, t)
    walker(d, cam, GATE - 40, t, mode="cheer", face=-1, name="")
    stage_end(d, t, dur, ["KEEP GOING."], [GOLD], size=170, dim=0.45, glow_col=GOLD[:3], y=H * 0.3)


SCENES = [s0_hook, s1_dream, s2_stays, s3_alone, s4_difference, s5_keeps, s6_end, s_follow]
