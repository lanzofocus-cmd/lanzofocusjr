"""THE KINGDOM OF EXCUSES — a storybook kingdom of unfinished towers that one builder brings back to life.

World: a stone kingdom at dusk in dusty violet, half-built towers wrapped in scaffolding, idle cranes, broken
roads and citizens sitting around. EXCUSES (lilac, scroll), LAZINESS (sage, crown, lying on a throne),
PROCRASTINATION (rust, giant calendar) and ACTION (warm gold, hard hat, hammer). As Action works, the city
completes itself and lights up for the night.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline, pill
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, stars, moon, sun,
                   figure, top_caption, final_card, shake, dust, word_reveal)
from kit import s_follow

TITLE = ("THE KINGDOM", "OF EXCUSES")
OUTPUT = "94_The_Kingdom_Of_Excuses_16x9.mp4"
FOLLOW_SUB = ("FOR IDEAS, LESSONS, AND PERSPECTIVES", "THAT CHALLENGE THE WAY YOU THINK.")

LINES = [
    "Once upon a time, there was a kingdom full of potential.",
    "But nothing was ever finished.",
    "Every problem had a reason.",
    "Every effort was avoided.",
    "Tomorrow became the favorite day of a kingdom that never moved.",
    "Then one person stopped waiting.",
    "Progress doesn't begin when everything is perfect.",
    "It begins when someone finally starts.",
    "Stop waiting.",
    "Start building.",
    "",
]
GAPS = {0: 0.7, 1: 1.0, 2: 2.0, 3: 1.2, 4: 1.6, 5: 2.6, 6: 1.6, 7: 1.8, 8: 0.5, 9: 1.4}

EXC = (190, 160, 240, 255)
LAZ = (140, 190, 150, 255)
PRO = (230, 120, 80, 255)
ACT = (255, 215, 130, 255)
CIT = (120, 112, 130, 255)
STONE = (52, 44, 66, 255)
STONE_LIT = (96, 78, 92, 255)
LINE = (200, 180, 220, 255)
WARM = (255, 190, 110, 255)
CH = 150

rng = random.Random(12)
BUILD = []   # x, width, height, kind, start completion, crane
x = -3000
while x < 3000:
    kind = rng.choice(["tower", "house", "house", "hall", "tower"])
    wdt = {"tower": rng.uniform(140, 200), "house": rng.uniform(220, 320), "hall": rng.uniform(300, 420)}[kind]
    hgt = {"tower": rng.uniform(700, 1100), "house": rng.uniform(260, 420), "hall": rng.uniform(420, 600)}[kind]
    if abs(x) < 380:  # the keep, centre stage
        kind, wdt, hgt = "keep", 640, 900
        x = -320
    BUILD.append((x, wdt, hgt, kind, rng.uniform(0.25, 0.65), rng.random() < 0.25))
    x += wdt + rng.uniform(40, 140)
CITIZENS = [(-2300, 1), (-1750, -1), (-1400, 1), (-600, -1), (-480, 1), (520, -1), (1250, 1), (1600, -1), (2100, 1), (2500, -1)]
HOLES = [(-2100, 120), (-1500, 160), (-1050, 90), (-200, 140), (700, 120), (1350, 170), (2000, 110)]


def bwin(d, cam, bx, bw, top, lit, seed):
    r = random.Random(seed)
    for row in range(int((-top - 120) / 110)):
        for c in range(max(1, int((bw - 60) / 70))):
            wx = bx + 40 + c * 70
            wy = -120 - row * 110
            on = lit > r.random()
            fill = col(WARM, 0.95) if on else (22, 18, 30, 255)
            d.rectangle(cam.box(wx, wy - 50, wx + 30, wy), fill=fill)
            if on and cam.z > 0.4 and r.random() < 0.3:
                glow(d, *cam.p(wx + 15, wy - 25), cam.s(70), WARM, 0.35)


def city(d, cam, t, prog=0.0, lit=0.0, night=0.0, light=1.0):
    """prog: 0 = abandoned .. 1 = finished. lit: share of lit windows."""
    draw_sky(d, mix((40, 26, 62, 255), (6, 6, 22, 255), night), mix((210, 130, 120, 255), (40, 30, 70, 255), night))
    stars(d, night, seed=4, n=100, ymax=0.5)
    if night < 0.95:
        sun(d, *cam.p(1400, -900 + 500 * night), cam.s(110), (1 - night) * 0.8, (255, 170, 120, 255))
    if night > 0.2:
        moon(d, *cam.p(-1800, -1500), cam.s(80), night, bg=(6, 6, 22))
    # distant hills
    hp = [(0, cam.p(0, -260)[1] + 30 * math.sin(i)) for i in range(1)]
    pts = []
    for i in range(0, 25):
        sx = i * W / 24
        sy = cam.p(0, -230)[1] * 0.6 + H * 0.4 * 0.6 - 60 * abs(math.sin(i * 0.9)) * cam.z
        pts.append((sx, sy))
    d.polygon(pts + [(W, H), (0, H)], fill=col(mix((40, 30, 60, 255), (14, 12, 30, 255), night), 1))
    for i, (bx, bw, bh, kind, c0, crane) in enumerate(BUILD):
        comp = clamp(lerp(c0, 1.0, clamp(prog * 1.3 - (i % 7) * 0.05)))
        top = -bh * comp
        stone = mix(STONE, STONE_LIT, lit * 0.6)
        x0, x1 = bx, bx + bw
        s0, s1 = cam.p(x0, 0), cam.p(x1, top)
        if s1[0] < -50 or s0[0] > W + 50:
            continue
        d.rectangle([s0[0], s1[1], s1[0], s0[1]], fill=col(stone, light))
        polyline(d, [cam.p(x0, 0), cam.p(x0, top), cam.p(x1, top), cam.p(x1, 0)], 1, col(LINE, 0.55 * light), max(2, int(cam.s(5))))
        if comp >= 0.999:  # roofs once finished
            if kind == "tower":
                d.polygon([cam.p(x0 - 15, top), cam.p((x0 + x1) / 2, top - bw * 1.1), cam.p(x1 + 15, top)], fill=col((130, 60, 70, 255), light))
                fl = cam.p((x0 + x1) / 2, top - bw * 1.1)
                d.line([fl, (fl[0], fl[1] - cam.s(60))], fill=col(LINE, light), width=max(1, int(cam.s(4))))
                d.polygon([(fl[0], fl[1] - cam.s(60)), (fl[0] + cam.s(50 + 6 * math.sin(t * 5)), fl[1] - cam.s(48)), (fl[0], fl[1] - cam.s(36))], fill=col(ACT, light))
            elif kind == "house":
                d.polygon([cam.p(x0 - 20, top), cam.p((x0 + x1) / 2, top - 120), cam.p(x1 + 20, top)], fill=col((110, 56, 60, 255), light))
            else:
                for k in range(int(bw / 50)):
                    if k % 2 == 0:
                        d.rectangle(cam.box(x0 + k * 50, top - 40, x0 + k * 50 + 50, top), fill=col(stone, light))
        else:  # scaffolding up to the planned height
            sc = col((150, 120, 90, 255), 0.7 * light)
            for k in range(0, int(bw / 60) + 2):
                xx = min(x1, x0 + k * 60)
                d.line([cam.p(xx, top), cam.p(xx, -bh)], fill=sc, width=max(1, int(cam.s(3))))
            yy = top
            while yy > -bh:
                d.line([cam.p(x0, yy), cam.p(x1, yy)], fill=sc, width=max(1, int(cam.s(3))))
                d.line([cam.p(x0, yy), cam.p(x1, yy - 90)], fill=col((150, 120, 90, 255), 0.35 * light), width=1)
                yy -= 90
            # jagged broken top
            jag = [cam.p(x0 + u * bw, top + (25 if j % 2 else 0)) for j, u in enumerate([0, 0.2, 0.35, 0.5, 0.7, 0.85, 1])]
            d.line(jag, fill=col(LINE, 0.4 * light), width=max(1, int(cam.s(3))))
        if kind == "keep" and comp > 0.5:  # gate
            gx = (x0 + x1) / 2
            d.rounded_rectangle(cam.box(gx - 90, -240, gx + 90, 0), int(cam.s(80)), fill=(14, 10, 20, 255))
        bwin(d, cam, bx, bw, top, lit, i)
        if crane and comp < 0.999:  # idle crane with a swinging hook
            cx = x1 - 30
            ct = -bh - 120
            d.line([cam.p(cx, 0), cam.p(cx, ct)], fill=col((180, 140, 90, 255), light), width=max(2, int(cam.s(8))))
            d.line([cam.p(cx - 260, ct), cam.p(cx + 120, ct)], fill=col((180, 140, 90, 255), light), width=max(2, int(cam.s(8))))
            sw = math.sin(t * 0.9 + i) * 0.12
            hx, hy = cx - 220 + math.sin(sw) * 300, ct + math.cos(sw) * 300
            d.line([cam.p(cx - 220, ct), cam.p(hx, hy)], fill=col(LINE, 0.6 * light), width=1)
            d.arc(cam.box(hx - 14, hy, hx + 14, hy + 28), 0, 200, fill=col(LINE, light), width=max(1, int(cam.s(4))))
    # street and road
    d.rectangle([0, cam.p(0, 0)[1], W, H], fill=col((26, 20, 34, 255), light))
    road_y = 0
    for k in range(-80, 80):
        rx = k * 48
        sx, sy = cam.p(rx, road_y + 22)
        if sx < -60 or sx > W + 60:
            continue
        broken = False
        for hx, hw in HOLES:
            if hx < rx < hx + hw:
                fixed = prog > 0.02 and (hx < -1700 + 5000 * prog)
                broken = not fixed
        if broken:
            continue
        d.rounded_rectangle(cam.box(rx + 3, 6, rx + 44, 38), int(cam.s(8)), fill=col((70, 58, 72, 255), light))
    fog(d, *cam.p(0, -100), cam.s(6000), 0.18 * light * (1 - night * 0.5), (230, 180, 200))


def citizens(d, cam, t, work=0.0, turn=0.0):
    for i, (cx, face) in enumerate(CITIZENS):
        fx, fy = cam.p(cx, 0)
        if fx < -100 or fx > W + 100:
            continue
        joined = work * 1.4 - (i * 0.11) > 0
        if joined:
            figure(d, fx, fy, cam.s(CH * 0.95), mix(CIT, (210, 190, 170, 255), work), mode="hammer", phase=t * 5 + i, face=face,
                   prop=hammer_prop, acc=("hair",))
        else:
            figure(d, fx, fy, cam.s(CH * 0.95), CIT, mode="sit", face=-face if turn * 2 - i * 0.1 > 0 else face,
                   head_down=0.6 * (1 - turn), acc=("hair",))


def hammer_prop(d, fh, bh, h, a):
    if not fh:
        return
    x, y = fh
    d.line([(x, y), (x, y - h * 0.18)], fill=col((150, 110, 70, 255), a), width=max(2, int(h * 0.03)))
    d.rectangle([x - h * 0.06, y - h * 0.24, x + h * 0.06, y - h * 0.17], fill=col((200, 200, 210, 255), a))


def scroll_prop(d, fh, bh, h, a):
    if not fh:
        return
    x, y = fh
    d.rectangle([x - h * 0.03, y - h * 0.2, x + h * 0.03, y + h * 0.12], fill=col((240, 225, 190, 255), a))
    d.ellipse([x - h * 0.05, y - h * 0.24, x + h * 0.05, y - h * 0.16], fill=col((210, 190, 150, 255), a))


def plaque(d, x, y, text, a, c=EXC, size=36):
    if a <= 0.01:
        return
    f = font(size)
    tw = d.textlength(text, font=f)
    d.rounded_rectangle([x - tw / 2 - 26, y - size * 0.9, x + tw / 2 + 26, y + size * 0.9], 14, fill=col((24, 18, 34, 255), 0.9 * a), outline=col(c, a), width=3)
    d.text((x, y), text, font=f, fill=col(WHITE, a), anchor="mm")


# ---------------------------------------------------------------- scenes
def s0_once(d, t, dur):
    p = t / dur
    # storybook opening: a slow lateral glide across the skyline, the crane hook swinging in the foreground
    cam = cam_lerp((-2200, -680, 0.42), (-300, -660, 0.42), sstep(p))
    city(d, cam, t)
    citizens(d, cam, t)
    dust(d, t, 0.6, n=50, color=(255, 210, 180))
    top_caption(d, ["ONCE UPON A TIME, THERE WAS", "A KINGDOM FULL OF POTENTIAL."], t, dur, accent={"POTENTIAL."})


def s1_never(d, t, dur):
    p = t / dur
    cam = cam_lerp((-300, -660, 0.42), (-1500, -250, 0.95), sstep(p))
    city(d, cam, t)
    citizens(d, cam, t)
    top_caption(d, ["BUT NOTHING WAS", "EVER FINISHED."], t, dur, accent={"NOTHING", "FINISHED."})


def s2_reason(d, t, dur):
    p = t / dur
    cam = cam_lerp((-1050, -330, 0.85), (-980, -360, 0.8), p)
    city(d, cam, t)
    citizens(d, cam, t)
    ex = -1150
    fx, fy = cam.p(ex, 0)
    figure(d, fx, fy, cam.s(CH * 1.1), EXC, mode="point", look=1.0, face=1, prop=None, name="EXCUSES", acc=("glasses",))
    for i, txt in enumerate(["NOT ENOUGH MONEY.", "NOT ENOUGH TIME.", "NOT THE RIGHT CONDITIONS."]):
        k = ramp(t, dur * (0.05 + 0.2 * i), 0.3)
        plaque(d, fx + cam.s(380), fy - cam.s(560 - i * 110), txt, k)
    # two workers put down their tools and walk away
    for j in range(2):
        lv = ramp(t, dur * (0.45 + 0.15 * j), 0.1)
        wx = -900 + 120 * j + 700 * sstep(ramp(t, dur * (0.45 + 0.15 * j), dur * 0.5))
        wfx, wfy = cam.p(wx, 0)
        figure(d, wfx, wfy, cam.s(CH * 0.95), CIT, mode="walk" if lv > 0 else "hammer", phase=t * 5 + j, face=1,
               prop=None if lv > 0 else hammer_prop, acc=("hair",))
    top_caption(d, ["EVERY PROBLEM", "HAD A REASON."], t, dur, accent={"REASON."})


def throne(d, cam, x, a=1.0):
    d.rounded_rectangle(cam.box(x - 140, -420, x + 140, -120), int(cam.s(30)), fill=col((110, 40, 60, 255), a), outline=col(ACT, a * 0.7), width=max(2, int(cam.s(6))))
    d.rectangle(cam.box(x - 190, -130, x + 190, -40), fill=col((140, 60, 70, 255), a))
    d.rectangle(cam.box(x - 230, -40, x + 230, 0), fill=col((80, 60, 70, 255), a))
    for s in (-1, 1):
        d.ellipse(cam.box(x + s * 150 - 18, -460, x + s * 150 + 18, -424), fill=col(ACT, a))


def s3_avoided(d, t, dur):
    p = t / dur
    cam = cam_lerp((60, -300, 1.05), (0, -260, 0.9), sstep(p))
    city(d, cam, t)
    glow(d, *cam.p(0, -260), cam.s(500), (255, 160, 120), 0.4)
    throne(d, cam, 0)
    fx, fy = cam.p(-40, -130)
    figure(d, fx, fy, cam.s(CH * 1.15), LAZ, mode="lie", face=1, acc=("crown",))
    d.text((fx + cam.s(10), fy - cam.s(150)), "LAZINESS", font=font(int(clamp(cam.s(30), 16, 34))), fill=col(LAZ, 1), anchor="mm")
    # z z z
    for i in range(3):
        u = (t * 0.6 + i / 3) % 1
        zx, zy = fx - cam.s(60) - u * cam.s(80), fy - cam.s(140) - u * cam.s(160)
        d.text((zx, zy), "z", font=font(int(cam.s(26 + 18 * u))), fill=col(WHITE, 0.7 * (1 - u)), anchor="mm")
    citizens(d, cam, t)
    for cx in (-420, 380):
        f2 = cam.p(cx, 0)
        figure(d, f2[0], f2[1], cam.s(CH * 0.95), CIT, mode="sit", face=1 if cx < 0 else -1, head_down=0.7, acc=("hair",))
    top_caption(d, ["EVERY EFFORT", "WAS AVOIDED."], t, dur, accent={"AVOIDED."})


def calendar(d, x, y, s, text, flip, a=1.0):
    w, h = 300 * s, 330 * s
    d.rounded_rectangle([x - w / 2, y - h, x + w / 2, y], int(20 * s), fill=col((245, 238, 225, 255), a))
    d.rounded_rectangle([x - w / 2, y - h, x + w / 2, y - h + 70 * s], int(20 * s), fill=col(PRO, a))
    d.rectangle([x - w / 2, y - h + 40 * s, x + w / 2, y - h + 70 * s], fill=col(PRO, a))
    for k in (-1, 1):
        d.rounded_rectangle([x + k * 80 * s - 10 * s, y - h - 25 * s, x + k * 80 * s + 10 * s, y - h + 25 * s], int(8 * s), fill=col((60, 50, 60, 255), a))
    size = int(54 * s if len(text) < 9 else 44 * s)
    d.text((x, y - h / 2 + 20 * s), text, font=font(size), fill=(40, 30, 40, int(255 * a)), anchor="mm")
    if 0 < flip < 1:  # page flying up
        fy = y - h + 70 * s - flip * 260 * s
        tpoly(d, [(x - w / 2, fy), (x + w / 2, fy), (x + w / 2 - 30 * s, fy + (h - 70 * s) * (1 - flip)), (x - w / 2 + 30 * s, fy + (h - 70 * s) * (1 - flip))],
              col((255, 250, 240, 255), 0.9 * (1 - flip)))


def s4_tomorrow(d, t, dur):
    p = t / dur
    cam = cam_lerp((900, -330, 0.95), (880, -340, 0.85), p)
    city(d, cam, t)
    citizens(d, cam, t)
    fx, fy = cam.p(760, 0)
    figure(d, fx, fy, cam.s(CH * 1.1), PRO, mode="point", look=0.6, face=1, name="PROCRASTINATION", acc=("hair",))
    words = ["TOMORROW", "NEXT WEEK", "NEXT MONTH", "NEXT YEAR"]
    seg = dur / len(words)
    i = min(len(words) - 1, int(t / seg))
    u = (t - i * seg) / seg
    calendar(d, *cam.p(1080, -40), cam.s(1.1), words[i], u * 4 if u < 0.25 and i > 0 else 0)
    top_caption(d, ["TOMORROW BECAME THE FAVORITE DAY", "OF A KINGDOM THAT NEVER MOVED."], t, dur, accent={"TOMORROW", "NEVER"})


def action(d, cam, x, t, mode, name_a=1.0, **kw):
    fx, fy = cam.p(x, 0)
    glow(d, fx, fy - cam.s(80), cam.s(260), ACT, 0.4)
    figure(d, fx, fy, cam.s(CH * 1.05), ACT, mode=mode, phase=kw.pop("phase", t * 5), name="ACTION", name_a=name_a,
           acc=("cap",), prop=hammer_prop if mode == "hammer" else (toolbox_prop if mode == "carry" else None), **kw)


def toolbox_prop(d, fh, bh, h, a):
    if fh:
        x, y = fh
        d.rounded_rectangle([x - h * 0.12, y - h * 0.02, x + h * 0.12, y + h * 0.12], int(h * 0.02), fill=col((200, 70, 60, 255), a))
        d.arc([x - h * 0.06, y - h * 0.08, x + h * 0.06, y + h * 0.02], 180, 360, fill=col((80, 80, 90, 255), a), width=max(2, int(h * 0.02)))


def s5_one(d, t, dur):
    p = t / dur
    # Action walks in with tools and starts on the smallest job: a gap in the road. Nobody looks up.
    cam = cam_lerp((-2400, -200, 0.9), (-2050, -220, 1.05), sstep(p))
    walk = sstep(ramp(t, 0.0, dur * 0.35))
    x = lerp(-2900, -2130, walk)
    prog = 0.012 * ramp(t, dur * 0.55, dur * 0.3)
    city(d, cam, t, prog=prog * 0)
    # the hole being filled stone by stone
    hx, hw = HOLES[0]
    n = int(ramp(t, dur * 0.42, dur * 0.5) * 4)
    for k in range(n):
        rx = hx + k * 48 - (hx % 48)
        d.rounded_rectangle(cam.box(rx + 3, 6, rx + 44, 38), int(cam.s(8)), fill=col((150, 120, 90, 255), 1))
    citizens(d, cam, t, turn=ramp(t, dur * 0.85, 0.5) * 0.4)
    if walk < 1:
        action(d, cam, x, t, "carry", phase=walk * 18)
    else:
        action(d, cam, x, t, "hammer", phase=t * 6)
        if math.sin(t * 6) > 0.95:
            sx, sy = cam.p(x + 60, 10)
            for j in range(5):
                d.line([(sx, sy), (sx + math.cos(j) * cam.s(40), sy - abs(math.sin(j)) * cam.s(40))], fill=col(ACT, 0.8), width=2)
    top_caption(d, ["THEN ONE PERSON", "STOPPED WAITING."], t, dur, accent={"ONE", "WAITING."})


def s6_progress(d, t, dur):
    p = t / dur
    # time-lapse: the camera glides back across the kingdom as it builds itself
    prog = sstep(p) * 0.9
    cam = cam_lerp((-2000, -420, 0.7), (200, -620, 0.5), sstep(p))
    city(d, cam, t, prog=prog, lit=0.4 * prog, night=0.3 * p)
    citizens(d, cam, t, work=p, turn=1)
    action(d, cam, lerp(-1900, 300, sstep(p)), t, "walk", phase=lerp(-1900, 300, sstep(p)) / 40, name_a=0.8)
    dust(d, t, 0.7, n=60, color=(255, 220, 160), rise=40)
    top_caption(d, ["PROGRESS DOESN'T BEGIN WHEN", "EVERYTHING IS PERFECT."], t, dur, accent={"PERFECT."})


def s7_starts(d, t, dur):
    p = t / dur
    cam = cam_lerp((200, -620, 0.5), (0, -1000, 0.3), sstep(p))
    night = lerp(0.3, 1.0, sstep(p))
    city(d, cam, t, prog=lerp(0.9, 1.0, p), lit=lerp(0.4, 0.95, sstep(p)), night=night)
    citizens(d, cam, t, work=1, turn=1)
    action(d, cam, 300, t, "cheer" if p > 0.5 else "stand", name_a=0.9)
    # lanterns rising over the finished kingdom
    r = random.Random(8)
    for i in range(24):
        u = clamp(p * 1.5 - r.random() * 0.5)
        if u <= 0:
            continue
        lx = r.uniform(-2600, 2600) + 60 * math.sin(t + i)
        ly = lerp(-200, -1800, u)
        sx, sy = cam.p(lx, ly)
        glow(d, sx, sy, cam.s(110), WARM, 0.5)
        d.ellipse([sx - cam.s(12), sy - cam.s(16), sx + cam.s(12), sy + cam.s(16)], fill=col(WARM, 0.9))
    top_caption(d, ["IT BEGINS WHEN SOMEONE", "FINALLY STARTS."], t, dur, accent={"STARTS."})


def ending(d, t, dur, part):
    cam = Cam(0, -1000, 0.3)
    city(d, cam, t + 10, prog=1.0, lit=0.95, night=1.0)
    citizens(d, cam, t, work=1, turn=1)
    overlay(d, (0, 0, 0), 0.5)
    if part == 0:
        final_card(d, t, dur, ["STOP WAITING."], [WHITE], size=130)
    else:
        d.text((W / 2, H / 2 - 90), "STOP WAITING.", font=font(110), fill=col(GREY, 0.7), anchor="mm")
        word_reveal(d, W / 2, H / 2 + 60, "START BUILDING.", t, 1.0, 130, ACT, anchor="mm")
        glow(d, W / 2, H / 2 + 60, 500, ACT, 0.3 * ramp(t, 0.3, 0.8))


def s8(d, t, dur):
    ending(d, t, dur, 0)


def s9(d, t, dur):
    ending(d, t, dur, 1)
s9.seamless = True


SCENES = [s0_once, s1_never, s2_reason, s3_avoided, s4_tomorrow, s5_one, s6_progress, s7_starts, s8, s9, s_follow]
