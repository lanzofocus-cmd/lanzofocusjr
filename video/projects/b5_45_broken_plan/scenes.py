"""THE BROKEN PLAN — the plan was a staircase; the storm took it; the pencil drew a new way.

World: the whole film lives on a blueprint. Deep blue paper, a faint grid, everything drawn in chalky white line.
A pencil draws PLAN A: a perfect staircase up to a gold star. THE PLANNER (white, glasses) climbs it confidently.
A paper storm blows in: sheets fly, lightning, the staircase lines snap and the steps tumble away, the planner falls.
On the ground, they pick up the pencil and draw a new, winding route, imperfect but real, and walk it to the star.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, dust, flash)
from kit import s_follow

TITLE = ("THE BROKEN", "PLAN")
OUTPUT = "145_The_Broken_Plan_16x9.mp4"
LINES = [
    "",
    "",
    "Your plan can break.",
    "Your progress doesn't have to.",
    "",
    "",
]
SILENT = {0: 3.2, 1: 3.4, 4: 3.4}
GAPS = {2: 3.0, 3: 6.6}

PAPER = (16, 52, 112, 255)
INK = (225, 240, 255, 255)
GOLD = (255, 205, 80, 255)
PLAN = (150, 200, 255, 255)
CH = 190
STEPS = 16
S0, S1 = (500, 0), (2200, -720)        # staircase from ground to the goal platform
GOAL = (2200, 2800, -720)
NEW = [(500, 0), (900, -60), (1250, -30), (1450, -200), (1250, -380), (1600, -470), (1950, -430), (2200, -720)]
BROKEN = range(6, 12)


def sheet(d, cam, t, storm=0.0):
    d.rectangle([0, 0, W, H], fill=mix(PAPER, (10, 30, 70, 255), storm))
    step = 100
    x0 = int((cam.cx - W / 2 / cam.z) // step) * step
    y0 = int((cam.cy - H / 2 / cam.z) // step) * step
    gc = col(mix((60, 100, 170, 255), (40, 70, 130, 255), storm), 1)
    for k in range(int(W / cam.z / step) + 3):
        x = x0 + k * step
        sx = cam.p(x, 0)[0]
        d.line([(sx, 0), (sx, H)], fill=gc, width=1 if x % 500 else 2)
    for k in range(int(H / cam.z / step) + 3):
        y = y0 + k * step
        sy = cam.p(0, y)[1]
        d.line([(0, sy), (W, sy)], fill=gc, width=1 if y % 500 else 2)
    # title block in the corner of the sheet
    a, b = cam.p(-900, 120), cam.p(-300, 330)
    d.rectangle([a[0], a[1], b[0], b[1]], outline=col(INK, 0.6), width=2)
    if cam.s(30) > 8:
        d.text((a[0] + cam.s(20), a[1] + cam.s(20)), "PROJECT: MY GOAL", font=font(max(8, int(cam.s(34)))), fill=col(INK, 0.7))


def partial(pts, k):
    """First fraction k of a polyline (by length)."""
    if k >= 1:
        return pts
    L = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    want = sum(L) * max(0, k)
    out = [pts[0]]
    for i, l in enumerate(L):
        if want >= l:
            out.append(pts[i + 1])
            want -= l
        else:
            u = want / l if l else 0
            out.append((lerp(pts[i][0], pts[i + 1][0], u), lerp(pts[i][1], pts[i + 1][1], u)))
            break
    return out


def at(pts, k):
    return partial(pts, k)[-1]


def ground(d, cam, k=1.0):
    polyline(d, [cam.p(*q) for q in partial([(-1200, 0), (S0[0], 0)], k)], 1, col(INK, 1), max(2, int(cam.s(6))))
    gx0, gx1, gy = GOAL
    if k > 0.6:
        a = ramp(k, 0.6, 0.4)
        polyline(d, [cam.p(gx0, gy), cam.p(gx1, gy), cam.p(gx1, 0)], 1, col(INK, a), max(2, int(cam.s(6))))
        # hatching under the platform
        for i in range(8):
            x = lerp(gx0, gx1, i / 8)
            d.line([cam.p(x, gy), cam.p(x + 120, gy + 160)], fill=col(INK, 0.3 * a), width=1)


def star(d, cam, t, k=1.0, burst=0.0):
    if k <= 0:
        return
    cx, cy = cam.p(2550, -900)
    r = cam.s(70) * k * (1 + 0.06 * math.sin(t * 3))
    glow(d, cx, cy, r * 4 * (1 + burst), GOLD, 0.35 + 0.4 * burst)
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + math.cos(a) * rr, cy + math.sin(a) * rr))
    d.polygon(pts, fill=GOLD)


def stairs(d, cam, t, k=1.0, fall=0.0, a=1.0):
    """The planned staircase, drawn to fraction k; the BROKEN steps tumble with fall in 0..1."""
    w = (S1[0] - S0[0]) / STEPS
    h = (S1[1] - S0[1]) / STEPS
    for i in range(int(STEPS * k + 0.999)):
        x, y = S0[0] + i * w, S0[1] + i * h
        seg = [(x, y), (x, y + h), (x + w, y + h)]
        if i in BROKEN and fall > 0:
            r = random.Random(i)
            ff = clamp(fall * 1.4 - (i - 6) * 0.05)
            dy = ff * ff * 1600
            dx = r.uniform(-120, 120) * ff
            rot = r.uniform(-2, 2) * ff
            cx, cy = x + w / 2, y + h / 2
            seg = [(cx + (px - cx) * math.cos(rot) - (py - cy) * math.sin(rot) + dx,
                    cy + (px - cx) * math.sin(rot) + (py - cy) * math.cos(rot) + dy) for px, py in seg]
            aa = a * (1 - ff * 0.6)
        else:
            aa = a
        polyline(d, [cam.p(*q) for q in seg], 1, col(PLAN, aa), max(2, int(cam.s(6))))
        if i in BROKEN and 0 < fall < 0.4:  # crack sparks
            particles(d, *cam.p(x + w / 2, y), cam.s(80), fall / 0.4, INK[:3], n=6, seed=i, rise=-0.3, size=4)


def papers(d, cam, t, k=1.0, seed=2, n=26):
    if k <= 0:
        return
    r = random.Random(seed)
    for i in range(n):
        sp = r.uniform(500, 1100)
        ph = r.random()
        x = cam.cx - W / cam.z + ((t * sp / 1600 + ph) % 1) * (2 * W / cam.z) * 1.1
        y = cam.cy + r.uniform(-0.5, 0.5) * H / cam.z + math.sin(t * 2 + i) * 80
        rot = t * r.uniform(2, 5) + i
        sw, sh = cam.s(70), cam.s(90)
        cx, cy = cam.p(x, y)
        q = [(-sw, -sh), (sw, -sh), (sw, sh), (-sw, sh)]
        sq = abs(math.cos(rot * 0.7))
        pts = [(cx + px * sq * math.cos(rot) - py * math.sin(rot) * 0.6, cy + px * sq * math.sin(rot) + py * math.cos(rot) * 0.6) for px, py in q]
        tpoly(d, pts, (235, 245, 255, int(220 * k)))
        d.line([pts[0], pts[1]], fill=(120, 160, 220, int(255 * k)), width=1)


def planner(d, cam, x, y, t, mode="walk", pencil=False, **kw):
    fx, fy = cam.p(x, y)
    face = kw.pop("face", 1)

    def pen(dd, fh, bh, hh, a):
        if fh and pencil:
            dd.line([fh, (fh[0] + face * hh * 0.08, fh[1] + hh * 0.08)], fill=GOLD, width=max(2, int(hh * 0.025)))
    figure(d, fx, fy, cam.s(CH), INK, mode=mode, phase=kw.pop("phase", t * 6), face=face, acc=("glasses",), name=kw.pop("name", "THE PLANNER"),
           prop=pen, eye_col=PAPER, **kw)


def storm_clouds(d, cam, t, k):
    if k <= 0:
        return
    r = random.Random(5)
    for i in range(9):
        x = cam.cx + (i - 4) * 500 + math.sin(t * 0.5 + i) * 60
        y = cam.cy - H / 2 / cam.z + 40 + r.uniform(0, 160)
        sx, sy = cam.p(x, y)
        rr = cam.s(r.uniform(260, 380))
        # sketchy spiral clouds, like scribbles on the sheet
        pts = [(sx + math.cos(a) * rr * (0.4 + a / 18), sy + math.sin(a) * rr * 0.5 * (0.4 + a / 18)) for a in [j * 0.3 + t for j in range(40)]]
        polyline(d, pts, 1, col(INK, 0.5 * k), 2)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # a pencil draws PLAN A on an empty blueprint: ground, staircase, platform, gold star; stamp
    cam = Cam(1500, -420, 0.55)
    sheet(d, cam, t)
    k = sstep(ramp(p, 0.0, 0.8))
    ground(d, cam, k)
    stairs(d, cam, t, k)
    star(d, cam, t, sstep(ramp(p, 0.75, 0.15)))
    tip = cam.p(*at([S0, S1], k))
    d.line([tip, (tip[0] + 60, tip[1] - 160)], fill=GOLD, width=10)
    if p > 0.85:
        s = 1 + 2 * (1 - sstep(ramp(p, 0.85, 0.1)))
        f = font(int(80 * s))
        d.text((W * 0.2, H * 0.22), "PLAN A", font=f, fill=col((255, 120, 110, 255), ramp(p, 0.85, 0.05)), anchor="mm")


def s1_climb(d, t, dur):
    p = t / dur
    # the planner climbs confidently; scribbled storm clouds gather; the first sheets blow past
    k = lerp(0.05, 0.45, sstep(p))
    x, y = at([S0, S1], k)
    cam = cam_lerp((900, -250, 0.85), (x + 200, y - 150, 0.85), sstep(p))
    sheet(d, cam, t, storm=0.4 * p)
    ground(d, cam)
    stairs(d, cam, t)
    star(d, cam, t)
    storm_clouds(d, cam, t, sstep(ramp(p, 0.3, 0.6)))
    papers(d, cam, t, sstep(ramp(p, 0.6, 0.4)), n=8)
    planner(d, cam, x, y, t, mode="walk", phase=t * 7, mouth=0.4)
    d.text((W * 0.12, H * 0.2), "PLAN A", font=font(50), fill=col((255, 120, 110, 255), 0.6))


def s2_break(d, t, dur):
    p = t / dur
    # lightning; the middle steps snap and tumble; the planner falls back down to the ground in a paper blizzard
    fall = sstep(ramp(p, 0.15, 0.5))
    k = 0.45
    x0, y0 = at([S0, S1], k)
    if p < 0.18:
        x, y, mode = x0, y0, "stand"
    else:
        u = sstep(ramp(p, 0.18, 0.35))
        x, y, mode = lerp(x0, 760, u), lerp(y0, 0, u) - math.sin(math.pi * u) * 120, ("flail" if u < 1 else "kneel")
    cam = cam_lerp((x0 + 200, y0 - 150, 0.85), (1300, -300, 0.55), sstep(ramp(p, 0.15, 0.5)))
    shake(cam, t, 10 * (1 - ramp(p, 0.2, 0.4)) * (p > 0.15))
    sheet(d, cam, t, storm=0.4 + 0.5 * fall)
    storm_clouds(d, cam, t, 1.0)
    ground(d, cam)
    stairs(d, cam, t, fall=fall)
    star(d, cam, t, 1.0)
    papers(d, cam, t, 1.0, n=30)
    planner(d, cam, x, y, t, mode=mode, head_down=mode == "kneel")
    if 0.14 < p < 0.2:
        flash(d, 0.6)
    top_caption(d, ["YOUR PLAN", "CAN BREAK."], t, dur, accent={"BREAK."})


def s3_progress(d, t, dur):
    p = t / dur
    # they pick up the pencil and draw a new, winding route around the gap, then walk it to the star
    draw = sstep(ramp(p, 0.08, 0.35))
    walk = sstep(ramp(p, 0.45, 0.45))
    clear = sstep(ramp(p, 0.3, 0.5))
    cam = cam_lerp((1300, -300, 0.55), (1550, -280, 0.58), sstep(p))
    sheet(d, cam, t, storm=0.9 * (1 - clear))
    storm_clouds(d, cam, t, 1 - clear)
    ground(d, cam)
    stairs(d, cam, t, fall=1.0, a=0.4)
    newp = partial(NEW, draw)
    polyline(d, [cam.p(*q) for q in newp], 1, col(GOLD, 1), max(3, int(cam.s(8))))
    for q in newp[1:-1]:
        sx, sy = cam.p(*q)
        d.ellipse([sx - 5, sy - 5, sx + 5, sy + 5], fill=GOLD)
    star(d, cam, t, 1.0, burst=sstep(ramp(p, 0.9, 0.1)))
    papers(d, cam, t, 1 - clear, n=20)
    if p < 0.45:
        tip = cam.p(*at(NEW, draw))
        planner(d, cam, 760 if p < 0.08 else 560, 0, t, mode="kneel" if p < 0.08 else "point", pencil=True, face=1)
        if 0.08 < p < 0.43:
            d.line([tip, (tip[0] + 40, tip[1] - 110)], fill=GOLD, width=8)
            glow(d, tip[0], tip[1], 40, GOLD, 0.5)
    else:
        x, y = at(NEW, walk) if walk < 1 else (2450, -720)
        planner(d, cam, x, y, t, mode="walk" if walk < 1 else "cheer", phase=walk * 60, mouth=0.6)
    d.text((W * 0.12, H * 0.2), "PLAN B" if p > 0.1 else "PLAN A", font=font(50), fill=col(GOLD if p > 0.1 else (255, 120, 110, 255), 0.7))
    top_caption(d, ["YOUR PROGRESS", "DOESN'T HAVE TO."], t, dur, accent={"PROGRESS", "DOESN'T"})


def s4_end(d, t, dur):
    cam = Cam(1500, -620, 0.5)
    sheet(d, cam, t)
    ground(d, cam)
    stairs(d, cam, t, fall=1.0, a=0.4)
    polyline(d, [cam.p(*q) for q in NEW], 1, col(GOLD, 1), max(3, int(cam.s(8))))
    star(d, cam, t, 1.0, burst=0.3)
    planner(d, cam, 2450, -720, t, mode="cheer", mouth=0.7)
    stage_end(d, t, dur, ["CHANGE THE PLAN.", "KEEP THE GOAL."], [WHITE, GOLD], size=100, dim=0.45, glow_col=GOLD[:3], y=H * 0.17)


SCENES = [s0_hook, s1_climb, s2_break, s3_progress, s4_end, s_follow]
