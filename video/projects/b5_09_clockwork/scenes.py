"""THE CLOCKWORK HUMAN — a person inside a great machine of gears that are their time.

World: a brass-and-copper clockwork chamber in amber light, interlocking gears of every size turning around a
person at the centre. DISTRACTIONS are small glowing magenta drones with screens that pluck gears out and fly
away; the machine slows, groans and stops. The person turns to real work and every completed task brings a
gear flying back; the whole machine restarts, faster and brighter.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, dust)
from kit import s_follow

TITLE = ("THE CLOCKWORK", "HUMAN")
OUTPUT = "109_The_Clockwork_Human_16x9.mp4"
LINES = [
    "",
    "Every distraction takes something.",
    "Not always money.",
    "Not always opportunity.",
    "Sometimes it takes your time.",
    "",
    "",
]
SILENT = {0: 3.0, 5: 4.6}
GAPS = {1: 1.2, 2: 0.6, 3: 0.6, 4: 2.4}

BRASS = (210, 160, 80, 255)
COPPER = (190, 110, 70, 255)
DIS = (255, 70, 190, 255)
YOU = (236, 232, 226, 255)
CH = 380

r0 = random.Random(9)
GEARS = []   # x, y, radius, teeth, direction
for (x, y, rr) in [(0, -800, 300), (-520, -700, 190), (480, -760, 220), (-300, -1150, 150), (320, -1180, 170), (-760, -300, 160),
                   (760, -330, 180), (0, -1000, 120), (-980, -760, 130), (1000, -800, 140), (-560, -1350, 110), (600, -1400, 120)]:
    GEARS.append((x, y, rr, int(rr / 14), 1 if len(GEARS) % 2 == 0 else -1))
STOLEN = [1, 4, 6, 8, 10, 3, 9]   # order in which distractions take gears


def chamber(d, cam, t, light=1.0):
    draw_sky(d, (14, 8, 4, 255), (40, 24, 12, 255))
    for k in range(-6, 7):  # riveted wall panels
        x = k * 400
        d.rectangle(cam.box(x + 10, -1700, x + 390, 0), outline=col((70, 44, 22, 255), light), width=max(1, int(cam.s(6))))
        for j in range(8):
            rx, ry = cam.p(x + 30, -1650 + j * 220)
            d.ellipse([rx - 3, ry - 3, rx + 3, ry + 3], fill=col((110, 70, 36, 255), light))
    fy = cam.p(0, 0)[1]
    if fy < H:
        d.rectangle([0, fy, W, H], fill=(24, 14, 8, 255))
    fog(d, *cam.p(0, -600), cam.s(4000), 0.12, (255, 200, 140))


def gear(d, cam, x, y, rr, teeth, rot, c, a=1.0):
    cx, cy = cam.p(x, y)
    R = cam.s(rr)
    pts = []
    for i in range(teeth * 2):
        ang = rot + i * math.pi / teeth
        rad = R if i % 2 == 0 else R * 0.86
        pts.append((cx + math.cos(ang) * rad, cy + math.sin(ang) * rad))
    d.polygon(pts, fill=col(dimc(c, 0.7), a))
    polyline(d, pts + [pts[0]], 1, col(c, a), max(1, int(cam.s(4))))
    d.ellipse([cx - R * 0.62, cy - R * 0.62, cx + R * 0.62, cy + R * 0.62], outline=col(c, a), width=max(1, int(cam.s(8))))
    for k in range(5):
        ang = rot + k * math.tau / 5
        d.line([(cx, cy), (cx + math.cos(ang) * R * 0.62, cy + math.sin(ang) * R * 0.62)], fill=col(c, a), width=max(1, int(cam.s(10))))
    d.ellipse([cx - R * 0.14, cy - R * 0.14, cx + R * 0.14, cy + R * 0.14], fill=col(c, a))


def machine(d, cam, t, speed=1.0, missing=(), returning=None, bright=0.0, gone_pos=None):
    """All gears; `missing` are absent; returning = {index: progress} flying back in."""
    ang = t * 0.6 * speed
    for i, (x, y, rr, teeth, sgn) in enumerate(GEARS):
        c = mix(BRASS if i % 3 else COPPER, (255, 230, 160, 255), bright)
        if i in missing and not (returning and i in returning):
            # empty axle where the gear was
            cx, cy = cam.p(x, y)
            d.ellipse([cx - cam.s(18), cy - cam.s(18), cx + cam.s(18), cy + cam.s(18)], fill=col((80, 50, 30, 255), 1))
            continue
        gx, gy = x, y
        if returning and i in returning:
            k = sstep(returning[i])
            sx, sy = gone_pos(i) if gone_pos else (x + 1500, y - 800)
            gx, gy = lerp(sx, x, k), lerp(sy, y, k)
            if 0 < k < 1:
                glow(d, *cam.p(gx, gy), cam.s(rr * 1.3), (255, 220, 150), 0.6)
        gear(d, cam, gx, gy, rr, teeth, sgn * ang * (300 / rr), c)
    if bright > 0:
        glow(d, *cam.p(0, -700), cam.s(1600), (255, 210, 140), 0.35 * bright)


def drone(d, sx, sy, s, t, a=1.0, carrying=None):
    glow(d, sx, sy, s * 2, DIS, 0.5 * a)
    d.rounded_rectangle([sx - s * 0.7, sy - s * 0.5, sx + s * 0.7, sy + s * 0.5], int(s * 0.2), fill=col((40, 10, 40, 255), a), outline=col(DIS, a), width=max(1, int(s * 0.08)))
    d.rectangle([sx - s * 0.55, sy - s * 0.38, sx + s * 0.55, sy + s * 0.38], fill=col((255, 140, 220, 255), a * (0.6 + 0.4 * math.sin(t * 9))))
    for k in (-1, 1):  # little rotors
        d.line([(sx + k * s * 0.4 - s * 0.35 * math.cos(t * 30), sy - s * 0.75), (sx + k * s * 0.4 + s * 0.35 * math.cos(t * 30), sy - s * 0.75)], fill=col(DIS, a), width=max(1, int(s * 0.08)))
    if carrying is not None:
        carrying(sx, sy + s * 1.4)


def person(d, cam, t, mode="stand", phase=0.0, **kw):
    fx, fy = cam.p(0, 0)
    figure(d, fx, fy, cam.s(CH), YOU, mode=mode, phase=phase, face=kw.pop("face", 1), acc=("hair",), **kw)
    return fx, fy


def steal_state(t, dur, upto):
    """Which gears have been taken by time t (each taken in sequence across the scene)."""
    out = []
    for j, i in enumerate(STOLEN[:upto]):
        out.append((i, clamp((t - j * dur / max(1, upto)) / (dur / max(1, upto)))))
    return out


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # a huge gear turns past the lens; the camera pulls back through the machinery to the person at its heart
    cam = cam_lerp((0, -520, 2.4), (0, -700, 0.55), sstep(p))
    chamber(d, cam, t)
    machine(d, cam, t)
    person(d, cam, t, look=0.6)


def thieves(d, cam, t, dur, start_missing, steals):
    missing = list(start_missing)
    for i, k in steals:
        x, y, rr, teeth, sgn = GEARS[i]
        if k <= 0:
            continue
        # drone flies in (k<0.4), grabs (0.4-0.5), flies off with the gear (k>0.5)
        if k < 0.4:
            u = k / 0.4
            sx, sy = cam.p(lerp(x + 1600, x, sstep(u)), lerp(y - 600, y - rr - 80, sstep(u)))
            drone(d, sx, sy, cam.s(130), t)
        else:
            missing.append(i)
            u = clamp((k - 0.5) / 0.5)
            gx, gy = lerp(x, x - 1800 if x < 0 else x + 1800, sstep(u)), lerp(y, y - 1200, sstep(u))
            def carry(cx, cy, rr=rr, teeth=teeth):
                gear(d, Cam(0, 0, 1), cx - W / 2, cy - H / 2, rr * cam.z * 0.7, teeth, t * 4, BRASS)
            sx, sy = cam.p(gx, gy - rr - 80)
            drone(d, sx, sy, cam.s(130), t, carrying=lambda cx, cy, rr=rr, teeth=teeth: gear(d, Cam(W / 2, H / 2, 1), cx, cy + cam.s(rr * 0.5), cam.s(rr) * 0.8, teeth, t * 4, BRASS))
    return missing


def s1_takes(d, t, dur):
    p = t / dur
    cam = cam_lerp((0, -700, 0.55), (0, -700, 0.6), p)
    chamber(d, cam, t)
    steals = steal_state(t, dur, 2)
    missing = [i for i, k in steals if k >= 0.4]
    machine(d, cam, t, speed=1 - 0.15 * len(missing), missing=missing)
    thieves(d, cam, t, dur, [], steals)
    person(d, cam, t, mode="phone", look=-0.2, prop=lambda dd, fh, bh, h, a: fh and dd.rectangle([fh[0] - h * 0.03, fh[1] - h * 0.06, fh[0] + h * 0.03, fh[1] + h * 0.02], fill=col((255, 160, 230, 255), a)))
    top_caption(d, ["EVERY DISTRACTION", "TAKES SOMETHING."], t, dur, accent={"DISTRACTION", "TAKES"})


def _more(d, t, dur, base, n, caption, accent):
    p = t / dur
    cam = cam_lerp((0, -700, 0.6), (0, -680, 0.66), p)
    chamber(d, cam, t)
    taken = STOLEN[:base]
    cur = [(STOLEN[base + j], clamp((t - j * dur / n) / (dur / n))) for j in range(n)]
    missing = taken + [i for i, k in cur if k >= 0.4]
    machine(d, cam, t, speed=max(0.05, 1 - 0.13 * len(missing)), missing=missing)
    thieves(d, cam, t, dur, taken, cur)
    person(d, cam, t, mode="phone", look=-0.2, prop=lambda dd, fh, bh, h, a: fh and dd.rectangle([fh[0] - h * 0.03, fh[1] - h * 0.06, fh[0] + h * 0.03, fh[1] + h * 0.02], fill=col((255, 160, 230, 255), a)))
    top_caption(d, caption, t, dur, accent=accent)


def s2(d, t, dur):
    _more(d, t, dur, 2, 1, ["NOT ALWAYS MONEY."], {"MONEY."})


def s3(d, t, dur):
    _more(d, t, dur, 3, 1, ["NOT ALWAYS OPPORTUNITY."], {"OPPORTUNITY."})


def s4_time(d, t, dur):
    p = t / dur
    # the last gears go; the machine grinds to a halt; the person finally looks up
    cam = cam_lerp((0, -680, 0.66), (0, -420, 0.9), sstep(p))
    chamber(d, cam, t, light=1 - 0.5 * p)
    taken = STOLEN[:4]
    cur = [(STOLEN[4 + j], clamp((t - j * dur * 0.2) / (dur * 0.25))) for j in range(3)]
    missing = taken + [i for i, k in cur if k >= 0.4]
    stop = sstep(ramp(p, 0.5, 0.4))
    machine(d, cam, t * (1 - stop * 0.9), speed=max(0.0, 0.4 * (1 - stop)), missing=missing)
    thieves(d, cam, t, dur, taken, cur)
    person(d, cam, t, mode="stand", look=0.6 * stop, head_down=0.3 * (1 - stop))
    darkness(d, W / 2, H / 2, 0.5 * stop)
    top_caption(d, ["SOMETIMES IT", "TAKES YOUR TIME."], t, dur, accent={"TIME."})


def s5_reclaim(d, t, dur):
    p = t / dur
    # the person turns to real work: each finished task calls a gear home; the machine restarts brighter
    cam = cam_lerp((0, -420, 0.9), (0, -760, 0.5), sstep(p))
    chamber(d, cam, t)
    ret = {i: ramp(p, 0.1 + j * 0.1, 0.18) for j, i in enumerate(STOLEN)}
    allback = min(ret.values())
    machine(d, cam, t, speed=lerp(0.05, 1.6, allback), missing=STOLEN, returning=ret, bright=allback,
            gone_pos=lambda i: (GEARS[i][0] + (1800 if GEARS[i][0] > 0 else -1800), GEARS[i][1] - 1200))
    acts = ["hammer", "carry", "hammer"]
    person(d, cam, t, mode=acts[int(t * 1.2) % 3], phase=t * 6, look=0.0, mouth=0.4)
    dust(d, t, 0.6 * allback, n=60, color=(255, 220, 160))


def s6_end(d, t, dur):
    cam = Cam(0, -760, 0.5)
    chamber(d, cam, t)
    machine(d, cam, t + 5, speed=1.6, bright=1.0)
    person(d, cam, t, mode="stand", mouth=0.4)
    stage_end(d, t, dur, ["PROTECT YOUR TIME."], [(255, 220, 150, 255)], size=120, dim=0.5, glow_col=BRASS)


SCENES = [s0_hook, s1_takes, s2, s3, s4_time, s5_reclaim, s6_end, s_follow]
LINES.insert(6, "")
SILENT[6] = 3.4
