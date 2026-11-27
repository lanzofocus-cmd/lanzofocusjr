"""THE WALL OF NAMES — every stone the critics throw becomes a step.

World: a dusty grey plain under a cold sky. THE BUILDER (teal) works on something small. On a ridge, THE CRITICS,
a row of grey figures, hurl stones with words carved into them: NOBODY CARES, YOU'LL FAIL, WHO ARE YOU?...
The stones land and stack into a wall that boxes the builder in. The builder pulls the same stones out and
sets them as a staircase, climbing out above the wall into a warm sunrise.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, dust, sun)
from kit import s_follow

TITLE = ("THE WALL", "OF NAMES")
OUTPUT = "119_The_Wall_Of_Names_16x9.mp4"
LINES = [
    "",
    "",
    "They tried to build a wall around you.",
    "Use the bricks…",
    "To build your way up.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.6, 5: 3.4}
GAPS = {2: 1.6, 3: 2.4, 4: 3.6}

BUILD = (90, 210, 200, 255)
CRIT = (120, 118, 124, 255)
STONE = (150, 145, 140, 255)
WORDS = ["YOU'LL FAIL", "NOBODY CARES", "WHO ARE YOU?", "TOO LATE", "GIVE UP", "NOT GOOD ENOUGH", "STAY SMALL", "WHY BOTHER"]
CH = 210
BW, BH = 150, 70
COLS = 6          # wall: 3 courses each side... built as a ring seen side-on: left and right columns
WALL_ROWS = 8


def plain(d, cam, t, warm=0.0):
    draw_sky(d, mix((80, 90, 110, 255), (255, 170, 120, 255), warm), mix((170, 170, 175, 255), (255, 220, 170, 255), warm))
    if warm > 0:
        sun(d, W * 0.72, cam.p(0, 0)[1] - cam.s(300), 80, warm, (255, 220, 150, 255))
    # the critics' ridge
    rp = [cam.p(-3000, -420), cam.p(-1400, -520), cam.p(-900, -380), cam.p(-600, 0), cam.p(-3000, 0)]
    d.polygon(rp, fill=(100, 96, 96, 255))
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=mix((130, 124, 116, 255), (170, 140, 110, 255), warm))
    fog(d, *cam.p(0, -100), cam.s(4000), 0.2, (220, 220, 225))


def critics(d, cam, t, throwing=True, a=1.0):
    for i in range(6):
        x = -2400 + i * 220
        y = -420 - 80 * math.sin(i * 0.9) if x < -1400 else -500 + (x + 1400) * 0.2
        y = lerp(-420, -520, clamp((x + 2400) / 1000))
        fx, fy = cam.p(x, y)
        ph = t * 2.2 + i * 1.3
        figure(d, fx, fy, cam.s(CH), CRIT, mode="hammer" if throwing else "stand", phase=ph, face=1, a=a, acc=("hair",), mouth=0.5,
               name="THE CRITICS" if i == 2 else None)


def stone(d, cam, x, y, word, a=1.0, rot=0.0, s=1.0):
    sx, sy = cam.p(x, y)
    w, h = cam.s(BW / 2 * s), cam.s(BH / 2 * s)
    ca, sa = math.cos(rot), math.sin(rot)
    pts = [(sx + ca * px - sa * py, sy + sa * px + ca * py) for px, py in ((-w, -h), (w, -h), (w, h), (-w, h))]
    d.polygon(pts, fill=col(STONE, a), outline=col((100, 96, 92, 255), a))
    if abs(rot) < 0.3:
        d.text((sx, sy), word, font=font(max(8, int(cam.s(16 * s)))), fill=col((60, 56, 54, 255), a), anchor="mm")


def wall_slots():
    """Stone positions: two columns either side of the builder, bottom-up, alternating."""
    out = []
    for r in range(WALL_ROWS):
        for side in (-1, 1):
            for c in range(2):
                x = side * (230 + c * (BW + 4)) + (BW / 2 if r % 2 else 0) * side * 0.3
                out.append((x, -BH / 2 - r * (BH + 3)))
    return out


SLOTS = wall_slots()
STEPS = [(-80 + i * 40, -BH / 2 - i * (BH + 3)) for i in range(WALL_ROWS + 1)]


def flying(d, cam, t, i, k, target):
    """Stone i flying from the ridge to target, k 0..1."""
    x0, y0 = -2000 + (i % 6) * 220, -650
    x1, y1 = target
    x = lerp(x0, x1, k)
    y = lerp(y0, y1, k) - math.sin(math.pi * k) * 700
    stone(d, cam, x, y, WORDS[i % len(WORDS)], rot=k * 8 * (1 - k))


def builder(d, cam, x, y, t, mode="hammer", **kw):
    fx, fy = cam.p(x, y)
    figure(d, fx, fy, cam.s(CH), BUILD, mode=mode, phase=kw.pop("phase", t * 5), face=kw.pop("face", 1), acc=("cap",),
           name=kw.pop("name", "THE BUILDER"), eye_col=(10, 50, 50, 255), **kw)


def wall(d, cam, t, n, removed=0):
    """First n slots filled; the first `removed` stones have been taken to become steps."""
    for i in range(int(n)):
        if i < removed:
            continue
        x, y = SLOTS[i]
        stone(d, cam, x, y, WORDS[i % len(WORDS)])


def steps(d, cam, n):
    for i in range(int(n)):
        x, y = STEPS[i]
        stone(d, cam, x, y, WORDS[i % len(WORDS)], s=1.0)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # a stone carved with YOU'LL FAIL tumbles at the lens in slow motion and whips past; behind it, the builder
    cam = Cam(-300, -260, 1.0)
    plain(d, cam, t)
    builder(d, cam, 0, 0, t, mode="hammer")
    u = sstep(ramp(t, 0.0, dur * 0.8))
    sx, sy = lerp(W * 0.2, W * 0.75, u), lerp(H * 0.35, H * 0.5, u)
    sc = lerp(2.5, 9, u)
    w, h = BW / 2 * sc, BH / 2 * sc
    rot = u * 2
    ca, sa = math.cos(rot), math.sin(rot)
    pts = [(sx + ca * px - sa * py, sy + sa * px + ca * py) for px, py in ((-w, -h), (w, -h), (w, h), (-w, h))]
    d.polygon(pts, fill=col(STONE, 1), outline=(100, 96, 92, 255))
    d.text((sx, sy), "YOU'LL FAIL", font=font(int(16 * sc)), fill=(60, 56, 54, 255), anchor="mm")
    darkness(d, W / 2, H / 2, 0.3)


def s1_throwing(d, t, dur):
    p = t / dur
    # stone after stone arcs in from the ridge and stacks up around the builder
    cam = cam_lerp((-900, -400, 0.45), (-500, -350, 0.55), sstep(p))
    plain(d, cam, t)
    critics(d, cam, t)
    n_target = len(SLOTS) * 0.7
    rate = n_target / dur
    landed = int(t * rate)
    wall(d, cam, t, landed)
    for j in range(3):
        i = landed + j
        if i < len(SLOTS):
            k = (t * rate - landed) - j * 0.33 + 1 if False else clamp(((t * rate) - i + 1.0) / 1.0)
            if 0 < k < 1:
                flying(d, cam, t, i, k, SLOTS[i])
    builder(d, cam, 0, 0, t, mode="hammer" if p < 0.6 else "stand", look=0.4 if p > 0.6 else 0.0)


def s2_wall(d, t, dur):
    p = t / dur
    # the wall closes over the builder's head; the light goes cold
    cam = cam_lerp((-300, -400, 0.6), (0, -450, 0.7), sstep(p))
    plain(d, cam, t)
    critics(d, cam, t, throwing=p < 0.7)
    n0 = len(SLOTS) * 0.7
    n = lerp(n0, len(SLOTS), sstep(ramp(p, 0.0, 0.6)))
    wall(d, cam, t, n)
    builder(d, cam, 0, 0, t, mode="slump", head_down=0.3, look=0.6)
    darkness(d, *cam.p(0, -200), 0.4 * p)
    top_caption(d, ["THEY TRIED TO BUILD", "A WALL AROUND YOU."], t, dur, accent={"WALL"})


def s3_bricks(d, t, dur):
    p = t / dur
    # the builder pulls the stones from the wall and sets them as steps
    cam = cam_lerp((0, -450, 0.7), (0, -500, 0.72), p)
    plain(d, cam, t)
    critics(d, cam, t, throwing=False)
    moved = int(4 * sstep(p))
    wall(d, cam, t, len(SLOTS), removed=moved)
    steps(d, cam, moved)
    builder(d, cam, -200 + 40 * moved, 0, t, mode="carry", phase=t * 4)
    top_caption(d, ["USE THE BRICKS…"], t, dur, accent={"BRICKS…"})


def s4_up(d, t, dur):
    p = t / dur
    # step by step, up and out over the top of the wall, into a warm sunrise
    n = lerp(4, WALL_ROWS + 1, sstep(ramp(p, 0.0, 0.6)))
    climb = lerp(1, WALL_ROWS + 1, sstep(ramp(p, 0.15, 0.7)))
    i = min(len(STEPS) - 1, int(climb) - 1)
    bx, by = STEPS[i][0], STEPS[i][1] - BH / 2
    warm = sstep(ramp(p, 0.4, 0.5))
    cam = cam_lerp((0, -500, 0.72), (0, -700, 0.6), sstep(p))
    plain(d, cam, t, warm=warm)
    critics(d, cam, t, throwing=False, a=1 - 0.5 * warm)
    wall(d, cam, t, len(SLOTS), removed=int(n))
    steps(d, cam, n)
    builder(d, cam, bx, by, t, mode="walk" if p < 0.85 else "cheer", phase=climb * math.pi, mouth=0.6 * warm, name_a=1 - warm)
    if warm > 0:
        glow(d, *cam.p(bx, by - 150), cam.s(400), (255, 210, 150), 0.5 * warm)
    top_caption(d, ["TO BUILD YOUR WAY UP."], t, dur, accent={"UP."})


def s5_end(d, t, dur):
    cam = Cam(0, -700, 0.6)
    plain(d, cam, t, warm=1.0)
    critics(d, cam, t, throwing=False, a=0.5)
    wall(d, cam, t, len(SLOTS), removed=WALL_ROWS + 1)
    steps(d, cam, WALL_ROWS + 1)
    bx, by = STEPS[-1][0], STEPS[-1][1] - BH / 2
    glow(d, *cam.p(bx, by - 150), cam.s(400), (255, 210, 150), 0.5)
    builder(d, cam, bx, by, t, mode="stand", name_a=0, mouth=0.6)
    stage_end(d, t, dur, ["BUILD YOUR WAY UP."], [BUILD], size=120, dim=0.4, glow_col=(255, 210, 150), y=H * 0.26)


SCENES = [s0_hook, s1_throwing, s2_wall, s3_bricks, s4_up, s5_end, s_follow]
