"""THE LABYRINTH OF DISTRACTION — a neon maze that grows every time you chase a sound.

World: a top-down neon labyrinth on black: cyan walls, a small white RUNNER seen from above. THE ECHOES are
magenta pulses that ping from side corridors; each time the runner turns to chase one, new walls draw
themselves and the maze grows. The runner stops, ignores the pings and heads one way; the walls in that
direction slide apart and THE EXIT opens as a column of gold light.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, particles,
                   top_caption, final_card, stage_end, shake)
from kit import s_follow

TITLE = ("THE LABYRINTH", "OF DISTRACTION")
OUTPUT = "121_The_Labyrinth_Of_Distraction_16x9.mp4"
LINES = [
    "",
    "Every distraction…",
    "Creates another direction.",
    "",
    "",
    "",
]
SILENT = {0: 3.0, 3: 4.6, 4: 3.4}
GAPS = {1: 1.2, 2: 3.4}

CYAN = (60, 220, 255, 255)
MAG = (255, 60, 200, 255)
GOLD = (255, 205, 110, 255)
CELL = 160
N = 31          # grid cells per side (odd)
C0 = N // 2     # runner starts in the centre cell
EXIT_ROW = -1   # the exit is past the top edge

# ---------------------------------------------------------------- maze (DFS), generated once
_r = random.Random(21)
WALLS = set()   # walls as (x0, y0, x1, y1) in cell units
for i in range(N + 1):
    for j in range(N):
        WALLS.add((i, j, i, j + 1))   # vertical
        WALLS.add((j, i, j + 1, i))   # horizontal
seen = {(C0, C0)}
stack = [(C0, C0)]
while stack:
    cx, cy = stack[-1]
    nb = [(cx + dx, cy + dy, dx, dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)) if 0 <= cx + dx < N and 0 <= cy + dy < N and (cx + dx, cy + dy) not in seen]
    if not nb:
        stack.pop()
        continue
    nx, ny, dx, dy = _r.choice(nb)
    if dx == 1:
        WALLS.discard((cx + 1, cy, cx + 1, cy + 1))
    elif dx == -1:
        WALLS.discard((cx, cy, cx, cy + 1))
    elif dy == 1:
        WALLS.discard((cx, cy + 1, cx + 1, cy + 1))
    else:
        WALLS.discard((cx, cy, cx + 1, cy))
    seen.add((nx, ny))
    stack.append((nx, ny))
WALLS = sorted(WALLS)

# the runner's wandering path (chasing pings): a random walk through open cells
def _open(a, b):
    (x0, y0), (x1, y1) = a, b
    if x1 == x0 + 1:
        return (x1, y0, x1, y0 + 1) not in WSET
    if x1 == x0 - 1:
        return (x0, y0, x0, y0 + 1) not in WSET
    if y1 == y0 + 1:
        return (x0, y1, x0 + 1, y1) not in WSET
    return (x0, y0, x0 + 1, y0) not in WSET


WSET = set(WALLS)
WANDER = [(C0, C0)]
_r2 = random.Random(5)
prev = None
for _ in range(26):
    cx, cy = WANDER[-1]
    opts = [(cx + dx, cy + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)) if 0 <= cx + dx < N and 0 <= cy + dy < N and _open((cx, cy), (cx + dx, cy + dy))]
    nxt = [o for o in opts if o != prev] or opts
    prev = (cx, cy)
    WANDER.append(_r2.choice(nxt))


def cell_pos(c):
    return ((c[0] - C0) * CELL + CELL / 2 - CELL / 2, (c[1] - C0) * CELL)


def wander_pos(u):
    """Position along the wander path, u in 0..1 (moves cell to cell)."""
    f = u * (len(WANDER) - 1)
    i = min(len(WANDER) - 2, int(f))
    k = sstep(f - i)
    a, b = cell_pos(WANDER[i]), cell_pos(WANDER[i + 1])
    return lerp(a[0], b[0], k), lerp(a[1], b[1], k), (b[0] - a[0], b[1] - a[1])


def maze(d, cam, t, reveal, centre, part=None, open_k=0.0):
    """Draw walls within `reveal` cells of `centre`; open_k slides apart the walls on the straight path north."""
    d.rectangle([0, 0, W, H], fill=(4, 6, 12, 255))
    cx, cy = centre
    lw = max(2, int(cam.s(12)))
    for (x0, y0, x1, y1) in WALLS:
        mx, my = (x0 + x1) / 2 - C0, (y0 + y1) / 2 - C0
        dist = math.hypot(mx * CELL - cx, my * CELL - cy) / CELL
        if dist > reveal:
            continue
        a = clamp(reveal - dist)
        wx0, wy0 = (x0 - C0) * CELL - CELL / 2, (y0 - C0) * CELL - CELL / 2
        wx1, wy1 = (x1 - C0) * CELL - CELL / 2, (y1 - C0) * CELL - CELL / 2
        if open_k > 0 and y0 == y1 and x0 == C0 and y0 <= C0:  # walls straight north of the centre slide away
            shift = open_k * CELL * 0.9
            for s in (-1, 1):
                p0 = cam.p(lerp(wx0, wx1, 0.5 if s > 0 else 0) + s * shift * 0.5, wy0)
                p1 = cam.p(lerp(wx0, wx1, 1 if s > 0 else 0.5) + s * shift, wy1)
                d.line([p0, p1], fill=col(CYAN, a), width=lw)
            continue
        d.line([cam.p(wx0, wy0), cam.p(wx1, wy1)], fill=col(CYAN, a), width=lw)
    glow(d, *cam.p(cx, cy), cam.s(CELL * reveal * 0.8), (60, 200, 255), 0.18)


def runner(d, cam, x, y, heading, t, still=False):
    sx, sy = cam.p(x, y)
    r = cam.s(32)
    glow(d, sx, sy, r * 4, WHITE, 0.4)
    d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(245, 245, 250, 255))
    ang = math.atan2(heading[1], heading[0]) if heading != (0, 0) else -math.pi / 2
    d.polygon([(sx + math.cos(ang) * r * 1.7, sy + math.sin(ang) * r * 1.7), (sx + math.cos(ang + 2.4) * r, sy + math.sin(ang + 2.4) * r),
               (sx + math.cos(ang - 2.4) * r, sy + math.sin(ang - 2.4) * r)], fill=(245, 245, 250, 255))
    if not still:  # footstep trail dots
        for k in range(1, 4):
            d.ellipse([sx - math.cos(ang) * r * 1.4 * k - 3, sy - math.sin(ang) * r * 1.4 * k - 3, sx - math.cos(ang) * r * 1.4 * k + 3, sy - math.sin(ang) * r * 1.4 * k + 3],
                      fill=col(WHITE, 0.5 / k))


def ping(d, cam, x, y, t, k, a=1.0):
    """An echo pulse at (x, y): expanding rings."""
    sx, sy = cam.p(x, y)
    d.ellipse([sx - cam.s(18), sy - cam.s(18), sx + cam.s(18), sy + cam.s(18)], fill=col(MAG, a))
    glow(d, sx, sy, cam.s(120), MAG, 0.6 * a)
    for j in range(3):
        u = (k + j / 3) % 1
        rr = cam.s(40 + 260 * u)
        d.ellipse([sx - rr, sy - rr, sx + rr, sy + rr], outline=col(MAG, a * (1 - u)), width=max(1, int(cam.s(5))))


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # black; the maze draws itself outward in neon from a single point
    cam = Cam(0, 0, lerp(1.6, 1.0, sstep(p)))
    maze(d, cam, t, reveal=lerp(0, 4, sstep(p)), centre=(0, 0))
    runner(d, cam, 0, 0, (0, -1), t, still=True)


def s1_every(d, t, dur):
    p = t / dur
    # a ping from a side corridor; the runner turns and chases; new walls draw themselves
    u = 0.35 * sstep(p)
    x, y, hd = wander_pos(u)
    cam = Cam(x * 0.6, y * 0.6, lerp(1.0, 0.8, p))
    maze(d, cam, t, reveal=4 + 4 * p, centre=(x, y))
    tgt = cell_pos(WANDER[min(len(WANDER) - 1, int(u * (len(WANDER) - 1)) + 3)])
    ping(d, cam, *tgt, t, t * 1.2)
    runner(d, cam, x, y, hd, t)
    top_caption(d, ["EVERY DISTRACTION…"], t, dur, accent={"DISTRACTION…"})


def s2_direction(d, t, dur):
    p = t / dur
    # ping after ping, left, right, back; the maze keeps growing; the camera pulls out to show how lost
    u = lerp(0.35, 1.0, p)
    x, y, hd = wander_pos(u)
    cam = Cam(x * 0.4, y * 0.4, lerp(0.8, 0.32, sstep(p)))
    maze(d, cam, t, reveal=8 + 9 * p, centre=(x, y))
    r = random.Random(3)
    for j in range(6):
        c = (r.randint(2, N - 3), r.randint(2, N - 3))
        k = ramp(t, j * dur / 7, 0.2)
        if k > 0:
            ping(d, cam, *cell_pos(c), t, t * 1.3 + j * 0.2, a=k)
    runner(d, cam, x, y, hd, t)
    top_caption(d, ["CREATES ANOTHER", "DIRECTION."], t, dur, accent={"ANOTHER", "DIRECTION."})


def s3_focus(d, t, dur):
    p = t / dur
    # the runner stops. The pings keep going, unanswered. One direction: north. The walls part. The exit.
    stop = 0.25
    if p < stop:
        x, y, hd = wander_pos(1.0)
        x, y = lerp(x, 0, sstep(p / stop)), lerp(y, 0, sstep(p / stop))
    else:
        u = sstep((p - stop) / (1 - stop))
        x, y, hd = 0, lerp(0, -(C0 + 1.5) * CELL, u), (0, -1)
    cam = Cam(x * 0.5, lerp(0, -1900, sstep(ramp(p, 0.3, 0.7))), lerp(0.32, 0.42, sstep(p)))
    open_k = sstep(ramp(p, 0.2, 0.3))
    maze(d, cam, t, reveal=17, centre=(0, 0), open_k=open_k)
    r = random.Random(3)
    for j in range(6):
        c = (r.randint(2, N - 3), r.randint(2, N - 3))
        ping(d, cam, *cell_pos(c), t, t * 1.3 + j * 0.2, a=0.6 * (1 - sstep(ramp(p, 0.4, 0.5))))
    # the line north and the exit light beyond the top edge
    ex, ey = cam.p(0, -(C0 + 1.5) * CELL)
    sx, sy = cam.p(0, 0)
    d.line([(sx, sy), (ex, ey)], fill=col(GOLD, 0.6 * open_k), width=max(2, int(cam.s(10))))
    glow(d, ex, ey, cam.s(600), GOLD, 0.8 * open_k)
    d.ellipse([ex - cam.s(120), ey - cam.s(120), ex + cam.s(120), ey + cam.s(120)], fill=col((255, 240, 200, 255), open_k))
    runner(d, cam, x, y, hd, t, still=p < stop)


def s4_end(d, t, dur):
    cam = Cam(0, -1900, 0.42)
    maze(d, cam, t, reveal=17, centre=(0, 0), open_k=1.0)
    ex, ey = cam.p(0, -(C0 + 1.5) * CELL)
    glow(d, ex, ey, cam.s(900), GOLD, 0.9)
    d.ellipse([ex - cam.s(140), ey - cam.s(140), ex + cam.s(140), ey + cam.s(140)], fill=(255, 240, 200, 255))
    stage_end(d, t, dur, ["CHOOSE ONE", "DIRECTION."], [WHITE, GOLD], size=110, dim=0.5, glow_col=GOLD, y=H * 0.6)


SCENES = [s0_hook, s1_every, s2_direction, s3_focus, s4_end, s_follow]
