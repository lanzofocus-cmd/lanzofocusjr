"""THE CITY BUILT ON TOMORROW — a dream city of unfinished floating towers, and one real brick.

World: a pale pink-and-blue haze where half-built towers float, drawn only in dashed outlines and turning
slowly. TOMORROW is a tall lavender figure holding plans and a TOMORROW sign. TODAY is a small warm-orange
builder. Today's bricks are the only solid things; as they stack up, the floating pieces sink down and lock into
a real city.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, dust, cloud)
from kit import s_follow
from render import dashed

TITLE = ("THE CITY BUILT", "ON TOMORROW")
OUTPUT = "104_The_City_Built_On_Tomorrow_16x9.mp4"
LINES = [
    "",
    "Tomorrow built an entire city.",
    "But never finished a single building.",
    "Today built one brick.",
    "Then another.",
    "",
    "",
]
SILENT = {0: 3.0, 5: 3.4}
GAPS = {1: 1.2, 2: 1.4, 3: 1.6, 4: 5.0}

TOM = (180, 160, 230, 255)
TODAY = (255, 150, 70, 255)
BRICK = (220, 110, 70, 255)
LINEC = (100, 80, 170, 255)
CH = 180

r0 = random.Random(4)
FLOAT = []  # x, y (float height), w, h, rot speed, phase, slot (target in the final city)
for i in range(22):
    w, h = r0.uniform(160, 300), r0.uniform(260, 900)
    FLOAT.append((r0.uniform(-2600, 2600), r0.uniform(-2200, -400), w, h, r0.uniform(-0.15, 0.15), r0.uniform(0, 6.28), i))
SLOTS = []
x = -1700
for i in range(22):
    w = FLOAT[i][2]
    SLOTS.append(x)
    x += w + 20


def sky(d, t, real=0.0):
    draw_sky(d, mix((200, 190, 240, 255), (60, 90, 160, 255), real), mix((255, 210, 220, 255), (255, 190, 140, 255), real))


def tower(d, cam, x, y, w, h, rot, a, solid=0.0, t=0.0, i=0):
    """A tower of w x h whose base centre is at (x, y), rotated by rot; dashed outline or solid stone."""
    cx, cy = x, y - h / 2
    pts = []
    for px, py in ((-w / 2, h / 2), (w / 2, h / 2), (w / 2, -h / 2), (0, -h / 2 - w * 0.5), (-w / 2, -h / 2)):
        rx = px * math.cos(rot) - py * math.sin(rot)
        ry = px * math.sin(rot) + py * math.cos(rot)
        pts.append(cam.p(cx + rx, cy + ry))
    if solid > 0:
        d.polygon(pts, fill=col(mix((230, 220, 240, 255), (200, 170, 150, 255), solid), a * solid))
        # windows
        r = random.Random(i)
        for k in range(int(h / 120)):
            for c in range(max(1, int(w / 80))):
                wx = -w / 2 + 30 + c * 80
                wy = h / 2 - 80 - k * 120
                q = cam.p(cx + wx * math.cos(rot) - wy * math.sin(rot), cy + wx * math.sin(rot) + wy * math.cos(rot))
                if r.random() < 0.7:
                    d.rectangle([q[0], q[1], q[0] + cam.s(26), q[1] + cam.s(40)], fill=col((255, 210, 140, 255), a * solid))
    if solid < 1:
        tpoly(d, pts, col((255, 255, 255, 255), 0.18 * a * (1 - solid)))
        dashed(d, pts + [pts[0]], col(LINEC, a * (1 - solid)), max(2, int(cam.s(8))), cam.s(26), cam.s(14))


def floating(d, cam, t, settle=0.0, a=1.0):
    """The dream towers; settle 0..1 brings each one down into its slot in the real city."""
    for (fx, fy, w, h, rs, ph, i) in FLOAT:
        k = sstep(clamp(settle * 1.6 - i * 0.03))
        bob = math.sin(t * 0.6 + ph) * 40 * (1 - k)
        x = lerp(fx, SLOTS[i] + w / 2, k)
        y = lerp(fy + bob, 0, k)
        rot = (math.sin(t * 0.3 + ph) * 0.25 + rs * t) * (1 - k)
        tower(d, cam, x, y, w, h * lerp(0.7, 1.0, k), rot, a, solid=k, t=t, i=i)


def ground(d, cam, real=0.0):
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=col(mix((210, 200, 230, 255), (90, 80, 90, 255), real), 1))
    fog(d, *cam.p(0, -50), cam.s(6000), 0.35 * (1 - real), (255, 255, 255))


def tomorrow(d, cam, x, t, a=1.0):
    fx, fy = cam.p(x, 0)
    h = cam.s(CH * 1.4)
    figure(d, fx, fy, h, TOM, mode="point" if math.sin(t * 1.5) > 0 else "cheer", look=0.9, face=1, a=a, name="TOMORROW",
           acc=("hair",), mouth=0.7)
    # sign
    sx, sy = fx - h * 0.45, fy - h * 0.2
    d.line([(sx, fy), (sx, sy - h * 0.25)], fill=col((120, 100, 160, 255), a), width=max(2, int(h * 0.02)))
    d.rounded_rectangle([sx - h * 0.3, sy - h * 0.45, sx + h * 0.3, sy - h * 0.25], int(h * 0.04), fill=col((250, 245, 255, 255), a))
    d.text((sx, sy - h * 0.35), "TOMORROW", font=font(max(10, int(h * 0.075))), fill=col((90, 70, 140, 255), a), anchor="mm")


def bricks(d, cam, n, x0=-200, t=0.0, new=1.0):
    """n bricks laid in courses from x0; the last brick drops in with `new`."""
    bw, bh = 90, 44
    per = 6
    for i in range(int(n)):
        row, c = divmod(i, per)
        bx = x0 + c * (bw + 6) + (bw / 2 if row % 2 else 0)
        by = -row * (bh + 4)
        drop = 1.0 if i < int(n) - 1 else new
        yy = by - (1 - drop) * 140
        d.rounded_rectangle(cam.box(bx, yy - bh, bx + bw, yy), int(cam.s(6)), fill=col(BRICK, 1), outline=col((120, 50, 30, 255), 1))
    return int(n)


def today(d, cam, x, t, mode="carry", a=1.0, name_a=1.0):
    fx, fy = cam.p(x, 0)
    glow(d, fx, fy - cam.s(90), cam.s(220), TODAY, 0.4 * a)

    def brick_prop(dd, fh, bh, h, aa):
        if fh and mode == "carry":
            dd.rounded_rectangle([fh[0] - h * 0.12, fh[1] - h * 0.06, fh[0] + h * 0.12, fh[1] + h * 0.05], int(h * 0.02), fill=col(BRICK, aa))
    figure(d, fx, fy, cam.s(CH), TODAY, mode=mode, phase=t * 5, face=1, a=a, name="TODAY", name_a=name_a, acc=("cap",), prop=brick_prop, mouth=0.5)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # gliding up through a haze of floating, half-drawn towers
    cam = cam_lerp((-1800, -1600, 0.5), (-300, -900, 0.42), sstep(p))
    sky(d, t)
    floating(d, cam, t)
    ground(d, cam)
    for j in range(4):
        cloud(d, (j * 560 + t * 25) % (W + 400) - 200, 220 + 70 * (j % 2), 70, col(WHITE, 0.6))


def s1_city(d, t, dur):
    p = t / dur
    cam = cam_lerp((-300, -900, 0.42), (0, -520, 0.68), sstep(p))
    sky(d, t)
    floating(d, cam, t)
    ground(d, cam)
    tomorrow(d, cam, -100, t, a=ramp(t, 0.1, 0.5))
    top_caption(d, ["TOMORROW BUILT", "AN ENTIRE CITY."], t, dur, accent={"TOMORROW", "CITY."})


def s2_never(d, t, dur):
    p = t / dur
    # close on a tower: the dashed lines flicker, nothing fills in
    cam = cam_lerp((0, -520, 0.68), (150, -600, 0.8), p)
    sky(d, t)
    flick = 0.5 + 0.5 * math.sin(t * 9)
    floating(d, cam, t, a=0.6 + 0.4 * flick)
    ground(d, cam)
    tomorrow(d, cam, -100, t)
    top_caption(d, ["BUT NEVER FINISHED", "A SINGLE BUILDING."], t, dur, accent={"NEVER", "SINGLE"})


def s3_one(d, t, dur):
    p = t / dur
    # low and close on the ground: Today walks in and sets down one solid, real brick
    cam = cam_lerp((-300, -120, 1.5), (-180, -120, 1.7), sstep(p))
    sky(d, t, real=0.1)
    floating(d, cam, t, a=0.4)
    ground(d, cam, real=0.2)
    walk = sstep(ramp(t, 0.0, dur * 0.4))
    x = lerp(-700, -330, walk)
    lay = ramp(t, dur * 0.45, 0.4)
    if lay > 0:
        bricks(d, cam, 1, x0=-200, new=lay)
        particles(d, *cam.p(-155, 0), cam.s(80), ramp(t, dur * 0.45 + 0.35, 0.5), (230, 200, 170), n=16, seed=2, rise=0.3)
    today(d, cam, x, t, mode="walk" if walk < 1 and lay <= 0 else ("crouch" if lay < 1 else "stand"))
    top_caption(d, ["TODAY BUILT ONE BRICK."], t, dur, accent={"ONE", "BRICK."})


def s4_another(d, t, dur):
    p = t / dur
    # brick after brick; a house; then the dream towers sink down and lock into place as a real city
    n = 1 + 47 * sstep(ramp(p, 0.0, 0.5))
    settle = sstep(ramp(p, 0.35, 0.65))
    cam = cam_lerp((-180, -120, 1.7), (100, -900, 0.36), sstep(ramp(p, 0.15, 0.85)))
    sky(d, t, real=settle)
    floating(d, cam, t, settle=settle)
    ground(d, cam, real=0.2 + 0.8 * settle)
    k = bricks(d, cam, n, x0=-200, new=(n % 1))
    today(d, cam, -330, t, mode="carry" if p < 0.5 else "cheer", name_a=1 - settle)
    if settle > 0.95:
        dust(d, t, 0.5, n=50, color=(255, 230, 190))
    top_caption(d, ["THEN ANOTHER."], t, dur, accent={"ANOTHER."})


def s5_end(d, t, dur):
    cam = Cam(100, -900, 0.36)
    sky(d, t, real=1.0)
    floating(d, cam, t, settle=1.0)
    ground(d, cam, real=1.0)
    bricks(d, cam, 48, x0=-200)
    today(d, cam, -330, t, mode="stand", name_a=0)
    stage_end(d, t, dur, ["BUILD TODAY."], [TODAY], size=130, dim=0.45, glow_col=TODAY)


SCENES = [s0_hook, s1_city, s2_never, s3_one, s4_another, s5_end, s_follow]
