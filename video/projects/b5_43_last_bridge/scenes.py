"""THE LAST BRIDGE — a gap too wide to jump, so you build the way across, plank by plank.

World: a jungle gorge in deep teal-green, mist pouring through the bottom, vines hanging from cliff faces.
THE TRAVELER (orange shirt) stands at the edge with a pile of planks and rope. The first plank nailed out over the
void looks absurd and wobbles. Time-lapse: plank after plank, ropes strung, a hanging bridge reaches the far side;
the traveler walks it in golden evening light while the mist glows below.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, sun, dust)
from kit import s_follow

TITLE = ("THE LAST", "BRIDGE")
OUTPUT = "143_The_Last_Bridge_16x9.mp4"
LINES = [
    "",
    "",
    "Your goal may feel impossible.",
    "Until you start building the way across.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.0, 4: 3.4}
GAPS = {2: 2.2, 3: 6.4}

TRAV = (255, 140, 60, 255)
WOOD = (150, 100, 60, 255)
ROPE = (200, 170, 120, 255)
A, B = 0, 2600     # cliff edges
CH = 200
PLANK = 70


def gorge(d, cam, t, gold=0.0):
    draw_sky(d, mix((40, 80, 80, 255), (90, 130, 170, 255), gold), mix((120, 170, 150, 255), (255, 190, 130, 255), gold))
    if gold > 0.05:
        sun(d, cam.p((A + B) / 2, 0)[0], cam.p(0, -500)[1], 80, gold, (255, 220, 150, 255))
    for (x0, x1, s) in ((A - 4000, A, -1), (B, B + 4000, 1)):
        r = random.Random(x1)
        edge, outer = (x1, x0) if s < 0 else (x0, x1)
        pts = [cam.p(outer, 0), cam.p(edge, 0)]
        for k in range(1, 10):
            pts.append(cam.p(edge - s * r.uniform(-40, 140) * min(1, k / 4), k * 260))
        pts += [cam.p(edge, 3000), cam.p(outer, 3000)]
        d.polygon(pts, fill=mix((30, 60, 50, 255), (70, 70, 60, 255), gold * 0.5))
        # foliage along the top
        for k in range(14):
            fx = lerp(x0, x1, k / 13)
            sx, sy = cam.p(fx, 0)
            rr = cam.s(r.uniform(60, 130))
            d.ellipse([sx - rr, sy - rr * 1.2, sx + rr, sy + rr * 0.3], fill=mix((40, 110, 60, 255), (90, 120, 60, 255), gold))
        for k in range(5):  # hanging vines
            vx = (x1 - 40 - k * 60) if s < 0 else (x0 + 40 + k * 60)
            polyline(d, [cam.p(vx + math.sin(t + k + j * 0.3) * 10, j * 120) for j in range(7)], 1, (50, 120, 60, 255), max(1, int(cam.s(6))))
    fog(d, *cam.p((A + B) / 2, 900), cam.s(5000), 0.7, mix((200, 230, 220, 255), (255, 210, 170, 255), gold)[:3])
    fog(d, *cam.p((A + B) / 2, 600), cam.s(4000), 0.4, (220, 240, 230))


def bridge(d, cam, t, n, sway=0.0):
    """n planks laid out from edge A (float)."""
    total = int((B - A) / PLANK)
    full = n >= total
    def y_at(x):
        if full:
            u = (x - A) / (B - A)
            return math.sin(math.pi * u) * 140 + math.sin(t * 1.5) * sway * math.sin(math.pi * u) * 40
        k = (x - A) / max(1, n * PLANK)
        return (x - A) * 0.02 + math.sin(t * 3) * 6 * k   # a stiff, wobbly cantilever before it's joined
    for i in range(int(min(n, total))):
        x = A + i * PLANK
        y = y_at(x + PLANK / 2)
        a, b = cam.p(x + 4, y - 10), cam.p(x + PLANK - 4, y + 14)
        d.rectangle([a[0], a[1], b[0], b[1]], fill=col(mix(WOOD, (120, 80, 50, 255), (i % 3) * 0.2), 1))
    reach = A + min(n, total) * PLANK
    for off in (-150, -60):  # hand ropes
        pts = [cam.p(x, y_at(x) + off) for x in range(A, int(reach) + 1, 40)]
        if len(pts) > 1:
            polyline(d, pts, 1, col(ROPE, 1), max(1, int(cam.s(6))))
    for x in (A, B):  # posts
        if x == B and not full:
            continue
        d.rectangle(cam.box(x - 14, -200, x + 14, 10), fill=col(WOOD, 1))
    return y_at


def traveler(d, cam, x, y, t, mode="stand", **kw):
    fx, fy = cam.p(x, y)
    tool = kw.pop("tool", False)
    figure(d, fx, fy, cam.s(CH), TRAV, mode=mode, phase=kw.pop("phase", t * 6), face=kw.pop("face", 1), acc=("hair", "backpack"), name="THE TRAVELER",
           prop=(lambda dd, fh, bh, h, a: fh and dd.rectangle([fh[0] - h * 0.05, fh[1] - h * 0.22, fh[0] + h * 0.05, fh[1] - h * 0.16], fill=(170, 170, 180, 255))) if tool else None, **kw)


def pile(d, cam, k=1.0):
    for i in range(int(8 * k)):
        a, b = cam.p(-500 + i * 6, -14 - i * 18), cam.p(-260 + i * 6, -i * 18)
        d.rectangle([a[0], a[1], b[0], b[1]], fill=col(WOOD, 1))
    cx, cy = cam.p(-150, -30)
    d.ellipse([cx - cam.s(50), cy - cam.s(30), cx + cam.s(50), cy + cam.s(30)], outline=col(ROPE, 1), width=max(2, int(cam.s(10))))


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # a pebble tips off the edge and falls, and falls, into the mist; no bottom
    y = 0 if t < 0.6 else 0.5 * 2000 * (t - 0.6) ** 2
    cam = Cam(A + 80, lerp(-100, 900, sstep(clamp((t - 0.6) / 2.2))), 1.0)
    gorge(d, cam, t)
    sx, sy = cam.p(A + 40 + (t > 0.6) * 60, y - 12)
    d.ellipse([sx - cam.s(14), sy - cam.s(12), sx + cam.s(14), sy + cam.s(12)], fill=(120, 110, 100, 255))


def s1_edge(d, t, dur):
    p = t / dur
    # standing at the edge: the far side is impossibly far; a pile of planks and rope behind
    cam = cam_lerp((A - 200, -250, 0.9), (1200, -400, 0.38), sstep(p))
    gorge(d, cam, t)
    pile(d, cam)
    traveler(d, cam, A - 80, 0, t, mode="stand", look=0.3)


def s2_impossible(d, t, dur):
    p = t / dur
    # the first plank goes out over the void... absurd, wobbling
    cam = cam_lerp((A + 100, -250, 0.9), (A + 200, -260, 1.05), p)
    gorge(d, cam, t)
    pile(d, cam, 0.85)
    bridge(d, cam, t, 3 * sstep(ramp(p, 0.2, 0.6)))
    traveler(d, cam, A - 60, 0, t, mode="hammer" if p < 0.8 else "stand", tool=True, look=-0.3)
    top_caption(d, ["YOUR GOAL MAY", "FEEL IMPOSSIBLE."], t, dur, accent={"IMPOSSIBLE."})


def s3_across(d, t, dur):
    p = t / dur
    # plank after plank, ropes strung, reaching the far side; then a slow walk across in golden light
    total = int((B - A) / PLANK)
    n = lerp(3, total, sstep(ramp(p, 0.0, 0.5)))
    gold = sstep(ramp(p, 0.4, 0.5))
    walk = sstep(ramp(p, 0.55, 0.45))
    cam = cam_lerp((A + 200, -260, 1.05), ((A + B) / 2, -400, 0.42), sstep(ramp(p, 0.05, 0.5)))
    gorge(d, cam, t, gold=gold)
    pile(d, cam, 1 - p)
    y_at = bridge(d, cam, t, n, sway=walk)
    if p < 0.5:
        bx = A + n * PLANK - 60
        traveler(d, cam, bx, y_at(bx), t, mode="hammer", tool=True, look=-0.2)
    else:
        x = lerp(A + 40, B + 120, walk)
        traveler(d, cam, x, y_at(x) if A < x < B else 0, t, mode="walk", phase=x / 50, mouth=0.5 * gold)
    dust(d, t, 0.4 * gold, n=40, color=(255, 220, 170))
    top_caption(d, ["UNTIL YOU START BUILDING", "THE WAY ACROSS."], t, dur, accent={"BUILDING", "ACROSS."})


def s4_end(d, t, dur):
    cam = Cam((A + B) / 2, -400, 0.42)
    gorge(d, cam, t, gold=1.0)
    bridge(d, cam, t, 999)
    traveler(d, cam, B + 160, 0, t, mode="cheer", mouth=0.7)
    stage_end(d, t, dur, ["BUILD THE WAY", "ACROSS."], [WHITE, (255, 210, 150, 255)], size=110, dim=0.35, glow_col=(255, 200, 140), y=H * 0.28)


SCENES = [s0_hook, s1_edge, s2_impossible, s3_across, s4_end, s_follow]
