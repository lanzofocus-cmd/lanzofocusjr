"""THE FOUR VOICES IN YOUR HEAD — a lone climber at the foot of a vast mountain at night.

World: cold violet night, layered ridges and ground fog, one huge mountain. The person is a warm white figure
with a red scarf. FEAR, COMFORT and DOUBT are hooded shadow-voices that float; COURAGE is the only voice made
of light, and the only one with legs: it walks.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, beam, darkness, shade_all, draw_sky, fog, stars,
                   moon, cloud, figure, shade, top_caption, low_caption, final_card, flash, shake, word_reveal)
from kit import s_follow

TITLE = ("THE FOUR VOICES", "IN YOUR HEAD")
OUTPUT = "92_The_Four_Voices_In_Your_Head_16x9.mp4"
FOLLOW_SUB = ("FOR IDEAS, LESSONS, AND PERSPECTIVES", "THAT CHALLENGE THE WAY YOU THINK.")

LINES = [
    "Every time you try to become something greater…",
    "…four voices appear.",
    "Fear tells you what could go wrong.",
    "Comfort tells you that you don't have to try.",
    "Doubt tells you that you're not enough.",
    "Courage doesn't silence the voices.",
    "It walks anyway.",
    "You don't need to feel fearless.",
    "You just need to move.",
    "",
]
SPOKEN = [l.replace("…", "") if i == 1 else l for i, l in enumerate(LINES)]
GAPS = {0: 0.5, 1: 1.2, 2: 1.2, 3: 1.4, 4: 1.4, 5: 0.9, 6: 2.0, 7: 0.5, 8: 1.4}

# ---------------------------------------------------------------- palette
SKY_TOP = (6, 4, 18, 255)
SKY_BOT = (34, 22, 64, 255)
YOU = (240, 236, 230, 255)
FEAR = (150, 90, 255, 255)
COMFORT = (255, 168, 90, 255)
DOUBT = (140, 185, 170, 255)
COURAGE = (130, 245, 225, 255)
MOUNT = (16, 12, 30, 255)
RIM = (170, 150, 255, 255)
DANGER = (255, 80, 90, 255)

# ---------------------------------------------------------------- world (x right, y up is negative)
PEAK = (3300, -3300)
MPTS = [(900, 0), (1500, -500), (1750, -700), (2050, -1150), (2300, -1300), (2600, -1900), (2850, -2150),
        (3050, -2700), PEAK, (3500, -2950), (3750, -2500), (4100, -2200), (4500, -1500), (4900, -900),
        (5400, -400), (6000, 0)]
PATH = [(260, 0), (900, -30), (1350, -260), (1600, -420), (1900, -700), (2150, -1000), (2450, -1300),
        (2700, -1700), (2950, -2100), (3150, -2600), (3300, -3260)]
CLIFFS = [[(1750, -700), (2050, -1150), (1980, -1010), (1860, -860)],
          [(2600, -1900), (2850, -2150), (2760, -2020)],
          [(3050, -2700), (3300, -3300), (3180, -3000)]]
YOU_X = 0
CH = 175


def far_ridges(d, cam, a=1.0):
    """Two distant ridge lines with parallax."""
    for f, base, amp, c in ((0.25, -150, 700, (22, 16, 44)), (0.45, -60, 420, (14, 10, 30))):
        pts = []
        for i in range(0, 41):
            x = -6000 + i * 400
            y = base - amp * (0.5 + 0.5 * math.sin(i * 1.7 + f * 9)) * (0.6 + 0.4 * math.sin(i * 0.53))
            sx = (x - cam.cx * f) * cam.z * (0.4 + 0.6 * f) + W / 2
            sy = (y - cam.cy * f) * cam.z * (0.4 + 0.6 * f) + H / 2 + cam.oy
            pts.append((sx, sy))
        pts += [(pts[-1][0], H + 10), (pts[0][0], H + 10)]
        d.polygon(pts, fill=c + (int(255 * a),))


def world(d, cam, t, light=1.0, dawn=0.0, path_glow=0.0):
    draw_sky(d, mix(SKY_TOP, (40, 30, 60, 255), dawn), mix(SKY_BOT, (230, 140, 110, 255), dawn * 0.8))
    stars(d, 0.9 * (1 - dawn), seed=21, n=110, ymax=0.7)
    mx, my = cam.p(4300, -3700)
    moon(d, mx, my, max(18, cam.s(140)), 0.9 * (1 - dawn), bg=SKY_TOP)
    far_ridges(d, cam, light)
    # the mountain
    pts = [cam.p(x, y) for x, y in MPTS]
    d.polygon(pts + [cam.p(6000, 600), cam.p(900, 600)], fill=col(MOUNT, light))
    rim = mix(RIM, (255, 200, 150, 255), dawn)
    polyline(d, pts[2:-2], 1, col(rim, 0.55 * light), max(2, int(cam.s(9))))
    # snow cap
    cap = [cam.p(3050, -2700), cam.p(*PEAK), cam.p(3500, -2950), cam.p(3380, -2900), cam.p(3260, -3000), cam.p(3150, -2800)]
    d.polygon(cap, fill=col(mix((120, 110, 170, 255), (255, 220, 190, 255), dawn), light * 0.9))
    if dawn > 0:
        glow(d, *cam.p(*PEAK), cam.s(900), (255, 190, 140), dawn * 0.7)
    # path up the mountain
    pp = [cam.p(x, y) for x, y in PATH]
    for i in range(len(pp) - 1):
        a, b = pp[i], pp[i + 1]
        for k in range(6):
            u = k / 6
            x, y = lerp(a[0], b[0], u), lerp(a[1], b[1], u)
            r = max(1.5, cam.s(8))
            d.ellipse([x - r, y - r * 0.6, x + r, y + r * 0.6], fill=col((200, 190, 255, 255), light * (0.35 + 0.5 * path_glow)))
    # ground
    g = [cam.p(-8000, 0), cam.p(9000, 0), cam.p(9000, 900), cam.p(-8000, 900)]
    d.polygon(g, fill=col((10, 8, 20, 255), light))
    polyline(d, [cam.p(-8000, 0), cam.p(1000, 0)], 1, col(RIM, 0.35 * light), max(2, int(cam.s(4))))
    # rocks on the plain
    rng = random.Random(4)
    for i in range(26):
        x = rng.uniform(-3000, 900)
        s = rng.uniform(20, 70)
        rp = [cam.p(x - s, 0), cam.p(x - s * 0.6, -s * 0.7), cam.p(x + s * 0.3, -s), cam.p(x + s, 0)]
        d.polygon(rp, fill=col((24, 18, 44, 255), light))
    fog(d, *cam.p(0, -40), cam.s(5000), 0.25 * light, (170, 150, 255))
    fog(d, *cam.p(1800, -500), cam.s(4000), 0.18 * light, (170, 150, 255))


def you(d, cam, x=YOU_X, **kw):
    fx, fy = cam.p(x, 0)
    kw.setdefault("acc", ("hair", "scarf"))
    kw.setdefault("mode", "stand")
    return figure(d, fx, fy, cam.s(CH), YOU, **kw), (fx, fy)


VOICES = {  # world x, floating height, colour, name
    "FEAR": (-330, FEAR, 0.0),
    "COMFORT": (-560, COMFORT, 0.0),
    "DOUBT": (330, DOUBT, 0.0),
}


def voices(d, cam, t, rise=1.0, a=1.0, only=None, focus=None, point=None, arms=None, names=1.0, dim_others=0.35, xs=None):
    out = {}
    for i, (nm, (x, c, _)) in enumerate(VOICES.items()):
        if only and nm not in only:
            continue
        if xs and nm in xs:
            x = xs[nm]
        r = clamp(rise * 3 - i * 0.6) if rise < 1 else 1.0
        if r <= 0:
            continue
        aa = a * r * (1.0 if (focus is None or focus == nm) else dim_others)
        cx, cy = cam.p(x, 30 - 60 * r + 12 * math.sin(t * 1.3 + i))
        hh = cam.s(330) * (0.6 + 0.4 * r)
        out[nm] = shade(d, cx, cy, hh, c, aa, t + i, point=(point if focus == nm else None),
                        arms=(arms if focus == nm and arms else 0.0), jag=1.0 if nm == "FEAR" else 0.0,
                        name=nm, name_a=names * r, face=1 if x < 0 else -1)
    return out


# ---------------------------------------------------------------- scenes
def s0_greater(d, t, dur):
    p = t / dur
    # hook: open on the moonlit peak, then tilt all the way down to one tiny person at its foot
    c0 = (3300, -3000, 0.42)
    c1 = (900, -700, 0.24)
    cam = cam_lerp(c0, c1, sstep(p * 0.95))
    fl = pulse(t, 0.35, 0.15) + 0.6 * pulse(t, 0.6, 0.1)
    world(d, cam, t, light=0.7 + 0.3 * ramp(t, 0.0, 0.6))
    you(d, cam, look=1.0)
    flash(d, fl, (190, 170, 255))
    top_caption(d, ["EVERY TIME YOU TRY TO BECOME", "SOMETHING GREATER…"], t, dur, accent={"GREATER…"})


def s1_appear(d, t, dur):
    p = t / dur
    cam = cam_lerp((900, -700, 0.24), (60, -260, 0.95), sstep(p))
    world(d, cam, t)
    rise = ramp(t, dur * 0.12, dur * 0.7)
    voices(d, cam, t, rise=rise)
    you(d, cam, look=lerp(1.0, 0.0, p), face=1 if p < 0.6 else -1)
    darkness(d, W / 2, H / 2 + 80, 0.35)
    top_caption(d, ["…FOUR VOICES APPEAR."], t, dur, accent={"FOUR", "VOICES"})
s1_appear.seamless = True


def s2_fear(d, t, dur):
    p = t / dur
    # over-the-shoulder: Fear beside the person, pointing up at the cliffs
    cam = cam_lerp((820, -620, 0.5), (900, -660, 0.56), p)
    world(d, cam, t, light=0.9)
    # the dangers light up red, one after another
    for i, cl in enumerate(CLIFFS):
        k = ramp(t, dur * (0.15 + 0.15 * i), 0.4)
        pts = [cam.p(x, y) for x, y in cl]
        if k > 0:
            polyline(d, pts + [pts[0]], k, col(DANGER, 0.9), max(3, int(cam.s(10))))
            glow(d, *pts[0], cam.s(500), DANGER, 0.35 * k)
    # loose rocks tumble down the flank
    for j in range(5):
        u = ((t * 0.55 + j * 0.21) % 1)
        x = lerp(2050, 1500, u) + 60 * j
        y = lerp(-1150, -300, u) - abs(math.sin(u * 18 + j)) * 60
        sx, sy = cam.p(x, y)
        r = cam.s(22)
        d.regular_polygon((sx, sy, r), 5, rotation=u * 900, fill=col((200, 170, 255, 255), 0.7 * ramp(t, dur * 0.3, 0.3)))
    fx, fy = cam.p(-330, -40)
    tgt = cam.p(1950, -1000)
    voices(d, cam, t, focus="FEAR", point=(lerp(fx, tgt[0], 0.18 * ramp(t, 0.2, 0.6)), lerp(fy - cam.s(260), tgt[1], 0.18 * ramp(t, 0.2, 0.6))))
    # the person flinches backward
    back = sstep(ramp(t, dur * 0.45, 0.6))
    you(d, cam, x=YOU_X - 60 * back, look=0.9, mode="stand", lean=-0.12 * back, mouth=-0.5)
    top_caption(d, ["FEAR TELLS YOU", "WHAT COULD GO WRONG."], t, dur, accent={"FEAR", "WRONG."})


def room(d, cam, k, t):
    """Comfort's warm room materialising behind the person."""
    if k <= 0:
        return
    x0, x1, y0 = -1150, -620, -520
    glow(d, *cam.p((x0 + x1) / 2, -260), cam.s(900), COMFORT, 0.55 * k)
    d.rectangle(cam.box(x0, y0, x1, 0), fill=col((70, 38, 22, 255), 0.85 * k))
    d.rectangle(cam.box(x0, y0, x1, 0), outline=col(COMFORT, k), width=max(2, int(cam.s(10))))
    # fireplace
    fx0, fx1 = -1100, -900
    d.rectangle(cam.box(fx0, -220, fx1, 0), fill=col((40, 20, 14, 255), k), outline=col(COMFORT, k * 0.8), width=max(2, int(cam.s(6))))
    for i in range(4):
        hgt = 90 + 40 * math.sin(t * 9 + i * 1.7)
        cx = fx0 + 40 + i * 40
        fp = [cam.p(cx - 25, -10), cam.p(cx + math.sin(t * 7 + i) * 8, -10 - hgt), cam.p(cx + 25, -10)]
        d.polygon(fp, fill=col((255, 200 - i * 20, 90, 255), k))
    glow(d, *cam.p(-1000, -80), cam.s(260), (255, 150, 60), 0.8 * k)
    # armchair
    ax = -780
    d.rounded_rectangle(cam.box(ax - 110, -260, ax + 60, -60), int(cam.s(30)), fill=col((150, 70, 50, 255), k))
    d.rounded_rectangle(cam.box(ax - 140, -150, ax + 90, -40), int(cam.s(30)), fill=col((190, 90, 60, 255), k))
    d.rectangle(cam.box(ax - 120, -40, ax - 100, 0), fill=col((90, 50, 30, 255), k))
    d.rectangle(cam.box(ax + 50, -40, ax + 70, 0), fill=col((90, 50, 30, 255), k))
    # floor lamp
    polyline(d, [cam.p(-660, 0), cam.p(-660, -360)], k, col(COMFORT, k), max(2, int(cam.s(6))))
    d.polygon([cam.p(-700, -360), cam.p(-620, -360), cam.p(-640, -420), cam.p(-680, -420)], fill=col((255, 210, 140, 255), k))


def s3_comfort(d, t, dur):
    p = t / dur
    cam = cam_lerp((-120, -300, 0.78), (-420, -300, 0.72), sstep(p))
    world(d, cam, t, light=0.85)
    k = sstep(ramp(t, dur * 0.1, dur * 0.4))
    room(d, cam, k, t)
    voices(d, cam, t, focus="COMFORT", arms=0.9 * k, xs={"COMFORT": -480})
    turn = p > 0.4
    drift = sstep(ramp(t, dur * 0.55, dur * 0.4))
    you(d, cam, x=YOU_X - 120 * drift, face=-1 if turn else 1, mode="walk" if 0.02 < drift < 0.98 else "stand",
        phase=drift * 6, swing=0.2, stride=0.5, look=0.2)
    top_caption(d, ["COMFORT TELLS YOU THAT", "YOU DON'T HAVE TO TRY."], t, dur, accent={"COMFORT", "DON'T"})


SHARDS = ["FAILED", "QUIT", "NOT READY", "TOO LATE", "WHO ARE YOU?", "AGAIN?"]


def s4_doubt(d, t, dur):
    p = t / dur
    cam = cam_lerp((0, -260, 0.8), (0, -230, 1.05), sstep(p))
    world(d, cam, t, light=0.6)
    darkness(d, W / 2, H / 2 + 60, 0.6)
    voices(d, cam, t, focus="DOUBT", arms=0.5, dim_others=0.2)
    cx, cy = cam.p(YOU_X, -120)
    R = cam.s(390)
    rot = t * 0.25
    for i, lbl in enumerate(SHARDS):
        k = ramp(t, dur * 0.08 + i * 0.18, 0.4)
        if k <= 0:
            continue
        ang = rot + i * math.tau / len(SHARDS)
        sx, sy = cx + R * math.cos(ang), cy + R * 0.42 * math.sin(ang) - cam.s(20)
        front = math.sin(ang) > 0
        s = cam.s(1.0) * (1.0 if front else 0.75)
        w, hgt = 70 * s, 190 * s
        pts = [(sx - w, sy - hgt * 0.7), (sx - w * 0.2, sy - hgt), (sx + w, sy - hgt * 0.8), (sx + w * 0.8, sy + hgt * 0.3), (sx - w * 0.6, sy + hgt * 0.35)]
        d.polygon(pts, fill=col((40, 60, 60, 255), 0.75 * k))
        polyline(d, pts + [pts[0]], 1, col(mix(DOUBT, WHITE, 0.4), k), max(2, int(3 * s)))
        figure(d, sx, sy + hgt * 0.18, hgt * 0.62, dimc(YOU, 0.55), mode="slump", acc=("hair",), a=0.8 * k, eyes=False)
        d.text((sx, sy - hgt * 0.78), lbl, font=font(max(12, int(20 * s))), fill=col(WHITE, 0.85 * k), anchor="mm")
    low = sstep(ramp(t, dur * 0.4, 0.8))
    you(d, cam, mode="slump" if low > 0.5 else "stand", head_down=low, look=-low)
    top_caption(d, ["DOUBT TELLS YOU", "THAT YOU'RE NOT ENOUGH."], t, dur, accent={"DOUBT", "ENOUGH."})


def courage(d, cam, x, t, a=1.0, walking=True, name_a=1.0):
    fx, fy = cam.p(x, 0)
    glow(d, fx, fy - cam.s(100), cam.s(300), COURAGE, 0.55 * a)
    figure(d, fx, fy, cam.s(CH * 1.05), COURAGE, mode="walk" if walking else "stand", phase=t * 5.5, swing=0.45,
           a=a, name="COURAGE", name_a=name_a, eye_col=(10, 60, 60, 255))
    # light it leaves on the ground
    d.ellipse([fx - cam.s(70), fy - cam.s(10), fx + cam.s(70), fy + cam.s(10)], fill=col(COURAGE, 0.35 * a))


def s5_courage(d, t, dur):
    p = t / dur
    cam = cam_lerp((-250, -300, 0.95), (200, -300, 0.85), sstep(p))
    world(d, cam, t, light=0.7 + 0.2 * p)
    voices(d, cam, t, a=0.8, names=0.8)
    # the voices keep talking: their words drift around
    for i, (w, vx) in enumerate((("WHAT IF YOU FALL?", -330), ("STAY HERE.", -560), ("YOU CAN'T.", 330))):
        k = 0.5 + 0.5 * math.sin(t * 2 + i * 2)
        sx, sy = cam.p(vx, -470 - 30 * math.sin(t + i))
        d.text((sx, sy), w, font=font(int(cam.s(30))), fill=col(GREY, 0.5 * k), anchor="mm")
    cx = lerp(-900, 700, sstep(ramp(t, 0.1, dur * 0.95)))
    you(d, cam, mode="slump", head_down=lerp(1, 0.4, ramp(t, dur * 0.4, 0.8)), look=lerp(-1, 0.3, ramp(t, dur * 0.4, 0.8)),
        face=1)
    courage(d, cam, cx, t, a=ramp(t, 0.0, 0.5))
    top_caption(d, ["COURAGE DOESN'T", "SILENCE THE VOICES."], t, dur, accent={"COURAGE", "SILENCE"})


def s6_anyway(d, t, dur):
    p = t / dur
    # low angle at ground level: the first step
    cam = cam_lerp((150, -160, 1.15), (500, -380, 0.6), sstep(ramp(t, dur * 0.35, dur * 0.65)))
    world(d, cam, t, light=0.85, path_glow=ramp(t, dur * 0.3, 1.0))
    voices(d, cam, t, a=lerp(0.8, 0.45, p), names=0.6)
    stepk = sstep(ramp(t, dur * 0.18, dur * 0.8))
    x = YOU_X + 420 * stepk
    you(d, cam, x=x, mode="walk" if 0.01 < stepk < 0.99 else "stand", phase=stepk * 7, swing=0.45, look=0.4)
    fx, fy = cam.p(x, 0)
    if stepk > 0.05:  # each footfall leaves a little light
        for j in range(int(stepk * 6)):
            gx, gy = cam.p(YOU_X + 70 * (j + 1), 0)
            d.ellipse([gx - cam.s(30), gy - cam.s(6), gx + cam.s(30), gy + cam.s(6)], fill=col(COURAGE, 0.4))
    courage(d, cam, 900 + 300 * p, t, a=0.9, name_a=0.6)
    top_caption(d, ["IT WALKS ANYWAY."], t, dur, accent={"ANYWAY."})


def ending(d, t, dur, part):
    p = t / dur
    k = (part + p) / 2
    cam = cam_lerp((1500, -1300, 0.3), (2100, -1700, 0.26), k)
    dawn = sstep(k * 1.2)
    world(d, cam, t, light=0.9, dawn=dawn, path_glow=1.0)
    x = lerp(900, 1500, k)
    ty = lerp(-30, -330, clamp((x - 900) / 600))
    fx, fy = cam.p(x, ty)
    glow(d, fx, fy - 20, 60, COURAGE, 0.6)
    figure(d, fx, fy, cam.s(CH), YOU, mode="walk", phase=t * 6, acc=("hair", "scarf"), eyes=False)
    shade_all(d, 0.35)
    lines = ["YOU DON'T NEED", "TO FEEL FEARLESS."] if part == 0 else ["YOU JUST", "NEED TO MOVE."]
    colors = [WHITE, WHITE] if part == 0 else [WHITE, COURAGE]
    final_card(d, t, dur, lines, colors, size=104, y=H / 2 - 40)


def s7(d, t, dur):
    ending(d, t, dur, 0)


def s8(d, t, dur):
    ending(d, t, dur, 1)
s8.seamless = True


SCENES = [s0_greater, s1_appear, s2_fear, s3_comfort, s4_doubt, s5_courage, s6_anyway, s7, s8, s_follow]
