"""THE MOUNTAIN THAT MOVES — every summit reveals a bigger one.

World: snow mountains at sunrise in rose, apricot and lavender, layered ranges and drifting cloud banks.
THE CLIMBER wears an orange jacket and a backpack and plants a small flag at each summit. THE SHADOW is a long
dark copy of the climber that grows behind it whenever it looks past the peak it is standing on.
The film ends with the climber sitting down and the camera tracing the whole route below, lit like a trail.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline, pill
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, sun,
                   top_caption, low_caption, final_card, shake, snow, cloud)
from kit import s_follow

TITLE = ("THE MOUNTAIN", "THAT MOVES")
OUTPUT = "99_The_Mountain_That_Moves_16x9.mp4"
FOLLOW_SUB = ("FOR IDEAS, LESSONS, AND PERSPECTIVES", "THAT CHALLENGE THE WAY YOU THINK.")

LINES = [
    "You think everything will change…",
    "…when you reach the top.",
    "So you climb.",
    "Then you realize…",
    "…there's always another mountain.",
    "If your happiness depends on reaching the next peak…",
    "…you'll never enjoy the one you're standing on.",
    "Don't just chase the destination.",
    "Learn to respect the climb.",
    "The journey is part of the victory.",
    "",
]
SPOKEN = [l.lstrip("…") for l in LINES]
GAPS = {0: 0.4, 1: 1.0, 2: 3.2, 3: 0.4, 4: 1.6, 5: 0.4, 6: 1.6, 7: 0.8, 8: 2.4, 9: 1.6}

ROSE = (255, 150, 160, 255)
APRICOT = (255, 190, 130, 255)
LAV = (120, 100, 170, 255)
SNOW = (250, 240, 245, 255)
ROCK = (70, 56, 96, 255)
JACKET = (255, 120, 60, 255)
SHADOW = (24, 14, 40, 255)
CH = 150

# the climbed mountain: route as polyline from base to summit
ROUTE = [(-1400, 0), (-1000, -120), (-760, -330), (-500, -420), (-300, -650), (-60, -760), (120, -1000),
         (330, -1140), (480, -1400), (620, -1560), (760, -1820)]
SUMMIT = ROUTE[-1]
M1 = [(-2600, 300), (-1400, 0)] + ROUTE + [(1100, -1500), (1500, -1100), (2000, -700), (2600, -200), (3200, 300)]


def route_pt(u):
    """Point and slope along the route, u in 0..1."""
    segs = [math.dist(ROUTE[i], ROUTE[i + 1]) for i in range(len(ROUTE) - 1)]
    L = sum(segs) * clamp(u)
    for i, s in enumerate(segs):
        if L <= s or i == len(segs) - 1:
            f = clamp(L / s)
            a, b = ROUTE[i], ROUTE[i + 1]
            return (lerp(a[0], b[0], f), lerp(a[1], b[1], f)), math.atan2(b[1] - a[1], b[0] - a[0])
        L -= s


def ranges(d, cam, t, light=1.0, warm=1.0):
    draw_sky(d, mix((40, 30, 80, 255), (90, 70, 140, 255), warm), mix((150, 110, 160, 255), (255, 170, 140, 255), warm))
    sx, sy = cam.p(2600, -900)
    sun(d, sx * 0.3 + W * 0.55, sy * 0.3 + H * 0.15, 70, 0.9 * warm, (255, 220, 170, 255))
    for f, base, amp, c, seed in ((0.15, -500, 900, (150, 120, 180), 1), (0.3, -250, 700, (120, 96, 160), 2), (0.5, -80, 500, (96, 76, 138), 3)):
        pts = []
        r = random.Random(seed)
        hs = [r.uniform(0.3, 1.0) for _ in range(40)]
        for i in range(40):
            x = -8000 + i * 420
            y = base - amp * hs[i] * (i % 2 == 0)
            zz = cam.z * (0.45 + 0.55 * f)
            pts.append(((x - cam.cx * f) * zz + W / 2, (y - cam.cy * f) * zz + H / 2 + cam.oy))
        pts += [(pts[-1][0], H + 10), (pts[0][0], H + 10)]
        d.polygon(pts, fill=c + (int(255 * light),))
        # snow on the peaks
        for i in range(0, len(pts) - 3, 2):
            p0, p1, p2 = pts[i], pts[i + 1], pts[i + 2]
            if p1[1] < p0[1]:
                d.polygon([p1, (lerp(p1[0], p0[0], 0.25), lerp(p1[1], p0[1], 0.25)), (lerp(p1[0], p2[0], 0.25), lerp(p1[1], p2[1], 0.25))],
                          fill=col(mix(SNOW, ROSE, 0.3), 0.8 * light))


def big_mountain(d, cam, t, rise=0.0, x0=2500, scale=1.7):
    """The next, bigger mountain rising out of the clouds behind."""
    if rise <= 0:
        return
    pk = (x0, -1820 * scale * rise - 400 * (1 - rise))
    pts = [cam.p(x0 - 2600 * scale * 0.6, 400), cam.p(x0 - 900 * scale * 0.6, -900 * scale * rise), cam.p(*pk),
           cam.p(x0 + 700 * scale * 0.6, -1100 * scale * rise), cam.p(x0 + 2400 * scale * 0.6, 400)]
    d.polygon(pts, fill=col((90, 66, 128, 255), 0.95))
    cap = [pts[2], (lerp(pts[2][0], pts[1][0], 0.3), lerp(pts[2][1], pts[1][1], 0.3)), (lerp(pts[2][0], pts[3][0], 0.3), lerp(pts[2][1], pts[3][1], 0.3))]
    d.polygon(cap, fill=col(SNOW, 0.95))
    glow(d, *pts[2], cam.s(600), APRICOT, 0.4 * rise)


def mountain(d, cam, t, trail=0.0, light=1.0):
    pts = [cam.p(x, y) for x, y in M1]
    d.polygon(pts + [cam.p(3200, 900), cam.p(-2600, 900)], fill=col(ROCK, light))
    # sunlit face and snow
    d.polygon([cam.p(*SUMMIT), cam.p(1100, -1500), cam.p(1500, -1100), cam.p(900, -1200), cam.p(600, -1400)], fill=col((150, 110, 150, 255), light))
    cap = [cam.p(480, -1400), cam.p(620, -1560), cam.p(*SUMMIT), cam.p(1100, -1500), cam.p(900, -1380), cam.p(700, -1450)]
    d.polygon(cap, fill=col(SNOW, light))
    polyline(d, pts[1:-4], 1, col(mix(ROSE, WHITE, 0.4), 0.7 * light), max(2, int(cam.s(6))))
    # rocks and ledges on the route
    r = random.Random(2)
    for i in range(30):
        u = i / 30
        (x, y), ang = route_pt(u)
        s = r.uniform(30, 70)
        sx, sy = cam.p(x + r.uniform(-60, 60), y + r.uniform(10, 80))
        d.polygon([(sx - cam.s(s), sy), (sx - cam.s(s * 0.4), sy - cam.s(s * 0.7)), (sx + cam.s(s * 0.5), sy - cam.s(s * 0.5)), (sx + cam.s(s), sy)],
                  fill=col((90, 72, 118, 255), light))
    if trail > 0:  # the route, lit like a trail of lanterns
        n = 40
        for i in range(int(n * trail) + 1):
            (x, y), _ = route_pt(i / n)
            sx, sy = cam.p(x, y - 8)
            glow(d, sx, sy, cam.s(60), APRICOT, 0.6)
            d.ellipse([sx - cam.s(7), sy - cam.s(7), sx + cam.s(7), sy + cam.s(7)], fill=col((255, 230, 190, 255), 1))


def clouds(d, cam, t, a=0.8, y=-300):
    for i in range(8):
        x = -3000 + i * 900 + (t * 30) % 900
        fog(d, *cam.p(x, y + 80 * math.sin(i)), cam.s(1800), 0.45 * a, (255, 230, 235))


def climber(d, cam, u, t, mode="walk", flag=False, **kw):
    (x, y), ang = route_pt(u)
    fx, fy = cam.p(x, y)
    kw.setdefault("lean", 0.35 if mode == "walk" else 0.0)
    head = figure(d, fx, fy, cam.s(CH), JACKET, mode=mode, phase=kw.pop("phase", u * 120), acc=("backpack", "hair"),
                  swing=kw.pop("swing", 0.5), **kw)
    return fx, fy


def flag(d, cam, x, y, t, a=1.0, c=APRICOT):
    bx, by = cam.p(x, y)
    tx, ty = cam.p(x, y - 170)
    d.line([(bx, by), (tx, ty)], fill=col((60, 50, 60, 255), a), width=max(2, int(cam.s(6))))
    wv = math.sin(t * 6) * cam.s(10)
    d.polygon([(tx, ty), (tx + cam.s(110), ty + cam.s(25) + wv), (tx, ty + cam.s(55))], fill=col(c, a))


def shadow_fig(d, cam, x, y, t, k, face=1):
    """The climber's long shadow, standing up behind it."""
    if k <= 0:
        return
    fx, fy = cam.p(x, y)
    h = cam.s(CH) * lerp(1.0, 3.4, k)
    glow(d, fx - face * h * 0.3, fy - h * 0.5, h * 0.6, (10, 0, 30), 0.6 * k)
    figure(d, fx - face * cam.s(110) * k, fy, h, SHADOW, mode="stand", phase=0, face=face, a=0.85 * k, acc=("backpack",),
           eye_col=(255, 120, 140, 255), look=0.4)


# ---------------------------------------------------------------- scenes
def s0_think(d, t, dur):
    p = t / dur
    # hook: the climber's boots at the bottom, then a vertical tilt up the whole face to the summit
    cam = cam_lerp((-1400, -80, 1.3), (-300, -900, 0.48), sstep(p))
    ranges(d, cam, t)
    clouds(d, cam, t, y=-200)
    mountain(d, cam, t)
    climber(d, cam, 0.0, t, mode="stand", look=1.0, lean=0.0)
    top_caption(d, ["YOU THINK EVERYTHING", "WILL CHANGE…"], t, dur, accent={"EVERYTHING"})


def s1_top(d, t, dur):
    p = t / dur
    cam = cam_lerp((-300, -900, 0.48), (500, -1500, 0.62), sstep(p))
    ranges(d, cam, t)
    clouds(d, cam, t, y=-200)
    mountain(d, cam, t)
    glow(d, *cam.p(*SUMMIT), cam.s(500), APRICOT, 0.6)
    climber(d, cam, 0.0, t, mode="stand", look=1.0, lean=0.0)
    top_caption(d, ["…WHEN YOU REACH", "THE TOP."], t, dur, accent={"TOP."})
s1_top.seamless = True


def s2_climb(d, t, dur):
    p = t / dur
    # the climb: tracking shots, a slip and a slide back, getting up, the last push in snow
    fall0, fall1, up1 = 0.38, 0.5, 0.62
    if p < fall0:
        u = lerp(0.0, 0.48, p / fall0)
        mode, kw = "walk", {}
    elif p < fall1:
        f = (p - fall0) / (fall1 - fall0)
        u = lerp(0.48, 0.42, sstep(f))
        mode, kw = ("flail", dict(lean=-0.4)) if f < 0.4 else ("crouch", dict(lean=0.2))
    elif p < up1:
        u = 0.42
        mode, kw = "kneel", dict(lean=0.1, tired=0.8)
    else:
        u = lerp(0.42, 0.97, (p - up1) / (1 - up1))
        mode, kw = "walk", dict(tired=0.5)
    (x, y), _ = route_pt(u)
    zoom = 0.95 if p < up1 else lerp(0.95, 0.7, (p - up1) / (1 - up1))
    cam = Cam(x + 180, y - 220, zoom)
    jolt = pulse(p, fall0 + 0.03, 0.04)
    shake(cam, t, 16 * jolt)
    ranges(d, cam, t)
    clouds(d, cam, t, y=lerp(-200, -900, p))
    mountain(d, cam, t)
    climber(d, cam, u, t, mode=mode, phase=u * 140 if mode == "walk" else t * 5, **kw)
    if fall0 < p < fall1:  # snow kicked up by the slide
        fx, fy = cam.p(x, y)
        for i in range(10):
            a = i * 0.7
            d.ellipse([fx + math.cos(a) * cam.s(60) - 4, fy - abs(math.sin(a)) * cam.s(50) - 4, fx + math.cos(a) * cam.s(60) + 4, fy - abs(math.sin(a)) * cam.s(50) + 4],
                      fill=col(SNOW, 0.8))
    snow(d, t, 0.7 * ramp(p, up1, 0.1), n=110)
    top_caption(d, ["SO YOU CLIMB."], t, dur, accent={"CLIMB."})


def s3_realize(d, t, dur):
    p = t / dur
    # the summit: flag planted, arms up... then the clouds part
    cam = cam_lerp((SUMMIT[0] + 100, SUMMIT[1] - 200, 0.9), (SUMMIT[0] + 600, SUMMIT[1] - 300, 0.6), sstep(p))
    ranges(d, cam, t)
    clouds(d, cam, t, a=1.0, y=-1300)
    mountain(d, cam, t)
    flag(d, cam, SUMMIT[0] + 40, SUMMIT[1], t, a=ramp(t, 0.0, 0.3))
    climber(d, cam, 1.0, t, mode="cheer", lean=0.0, mouth=0.8)
    top_caption(d, ["THEN YOU REALIZE…"], t, dur, accent={"REALIZE…"})


def s4_another(d, t, dur):
    p = t / dur
    cam = cam_lerp((SUMMIT[0] + 600, SUMMIT[1] - 300, 0.6), (SUMMIT[0] + 900, SUMMIT[1] - 500, 0.4), sstep(p))
    ranges(d, cam, t)
    big_mountain(d, cam, t, rise=sstep(ramp(t, 0.1, dur * 0.7)))
    clouds(d, cam, t, a=1.0, y=-900)
    mountain(d, cam, t)
    flag(d, cam, SUMMIT[0] + 40, SUMMIT[1], t)
    climber(d, cam, 1.0, t, mode="stand", lean=0.0, look=0.8, mouth=lerp(0.8, -0.4, p))
    top_caption(d, ["…THERE'S ALWAYS", "ANOTHER MOUNTAIN."], t, dur, accent={"ANOTHER"})
s4_another.seamless = True


def _shadow(d, t, dur, part):
    p = t / dur
    k = (part + p) / 2
    cam = cam_lerp((SUMMIT[0] + 700, SUMMIT[1] - 350, 0.6), (SUMMIT[0] + 600, SUMMIT[1] - 350, 0.68), sstep(k))
    ranges(d, cam, t, warm=lerp(1.0, 0.45, k))
    big_mountain(d, cam, t, rise=1.0)
    clouds(d, cam, t, a=1.0, y=-1100)
    mountain(d, cam, t, light=lerp(1.0, 0.8, k))
    flag(d, cam, SUMMIT[0] + 40, SUMMIT[1], t)
    shadow_fig(d, cam, SUMMIT[0], SUMMIT[1], t, sstep(ramp(k, 0.05, 0.6)), face=1)
    climber(d, cam, 1.0, t, mode="slump" if k > 0.3 else "stand", lean=0.0, look=0.6, head_down=0.3 * k)
    overlay(d, (20, 0, 40), 0.25 * k)
    if part == 0:
        top_caption(d, ["IF YOUR HAPPINESS DEPENDS ON", "REACHING THE NEXT PEAK…"], t, dur, accent={"HAPPINESS", "NEXT"})
    else:
        top_caption(d, ["…YOU'LL NEVER ENJOY THE", "ONE YOU'RE STANDING ON."], t, dur, accent={"NEVER", "STANDING"})


def s5(d, t, dur):
    _shadow(d, t, dur, 0)


def s6(d, t, dur):
    _shadow(d, t, dur, 1)
s6.seamless = True


def s7_chase(d, t, dur):
    p = t / dur
    # the climber turns away from the next peak and sits down; the shadow shrinks back into the ground
    cam = cam_lerp((SUMMIT[0] + 600, SUMMIT[1] - 350, 0.68), (SUMMIT[0] - 50, SUMMIT[1] - 200, 1.15), sstep(p))
    ranges(d, cam, t, warm=lerp(0.45, 0.9, p))
    big_mountain(d, cam, t, rise=1.0)
    clouds(d, cam, t, a=1.0, y=-1100)
    mountain(d, cam, t)
    flag(d, cam, SUMMIT[0] + 40, SUMMIT[1], t)
    shadow_fig(d, cam, SUMMIT[0], SUMMIT[1], t, 1 - sstep(ramp(t, 0.2, dur * 0.6)), face=1)
    sit = p > 0.5
    climber(d, cam, 1.0, t, mode="sit_edge" if sit else "stand", face=-1, lean=0.0, look=-0.3, head_down=0.0 if not sit else -0.3)
    top_caption(d, ["DON'T JUST CHASE", "THE DESTINATION."], t, dur, accent={"CHASE"})


def s8_respect(d, t, dur):
    p = t / dur
    # the camera follows the climber's gaze back down the whole route; every hard step lights up
    cam = cam_lerp((SUMMIT[0] - 50, SUMMIT[1] - 200, 1.15), (-300, -820, 0.42), sstep(ramp(t, 0.1, dur * 0.8)))
    ranges(d, cam, t, warm=1.0)
    big_mountain(d, cam, t, rise=1.0)
    clouds(d, cam, t, a=0.8, y=-300)
    mountain(d, cam, t, trail=1 - sstep(ramp(t, 0.2, dur * 0.7)) * 0 + 0)
    # light the trail from the top down as the camera passes
    k = sstep(ramp(t, 0.2, dur * 0.7))
    n = 40
    for i in range(n, int(n * (1 - k)) - 1, -1):
        (x, y), _ = route_pt(i / n)
        sx, sy = cam.p(x, y - 8)
        glow(d, sx, sy, cam.s(70), APRICOT, 0.6)
        d.ellipse([sx - cam.s(8), sy - cam.s(8), sx + cam.s(8), sy + cam.s(8)], fill=col((255, 230, 190, 255), 1))
    for u, lbl in ((0.12, "THE FIRST STEP"), (0.45, "THE FALL"), (0.47, ""), (0.75, "THE STORM")):
        if lbl and k > 1 - u:
            (x, y), _ = route_pt(u)
            sx, sy = cam.p(x, y - 120)
            d.text((sx, sy), lbl, font=font(int(clamp(cam.s(44), 16, 40))), fill=col(WHITE, 0.9 * ramp(k, 1 - u, 0.15)), anchor="mm")
    flag(d, cam, SUMMIT[0] + 40, SUMMIT[1], t)
    climber(d, cam, 1.0, t, mode="sit_edge", face=-1, lean=0.0, look=-0.3)
    top_caption(d, ["LEARN TO RESPECT", "THE CLIMB."], t, dur, accent={"RESPECT", "CLIMB."})


def s9_final(d, t, dur):
    cam = Cam(-300, -820, 0.42)
    ranges(d, cam, t, warm=1.0)
    big_mountain(d, cam, t, rise=1.0)
    mountain(d, cam, t, trail=1.0)
    flag(d, cam, SUMMIT[0] + 40, SUMMIT[1], t)
    climber(d, cam, 1.0, t, mode="sit_edge", face=-1, lean=0.0)
    overlay(d, (20, 10, 30), 0.5)
    final_card(d, t, dur, ["THE JOURNEY IS PART", "OF THE VICTORY."], [WHITE, APRICOT], size=104, glow_col=APRICOT)


SCENES = [s0_think, s1_top, s2_climb, s3_realize, s4_another, s5, s6, s7_chase, s8_respect, s9_final, s_follow]
