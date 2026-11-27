"""THE STORM INSIDE THE ROOM — the weather is not outside. It's in here.

World: an ordinary warm living room, side-on: sofa, lamp, bookshelf, a window full of calm blue sky. A storm forms
under the ceiling: indoor rain, lightning, books and chairs lifting into a whirlwind. CHAOS is a dark swirling
vortex with lightning eyes that grows every time THE PERSON panics. CALM is a soft pale-blue glowing figure who
simply sits down; the person breathes with it, and the storm folds itself away into sunlight.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, rain, flash, bolt, cloud, dust)
from kit import s_follow

TITLE = ("THE STORM INSIDE", "THE ROOM")
OUTPUT = "115_The_Storm_Inside_The_Room_16x9.mp4"
LINES = [
    "",
    "",
    "You can't always control what happens.",
    "But you can control what happens next.",
    "",
    "",
]
SILENT = {0: 3.2, 1: 3.4, 4: 4.2}
GAPS = {2: 1.6, 3: 5.0}

WALL = (200, 170, 140, 255)
YOU = (236, 230, 222, 255)
CALM = (170, 210, 255, 255)
CHAOS = (40, 30, 60, 255)
CH = 400

OBJECTS = [("book", -700, -500), ("chair", -300, 0), ("lamp", 640, 0), ("book", 500, -520), ("frame", -150, -760), ("cup", 300, -260),
           ("book", -560, -500), ("plant", 820, 0), ("book", 600, -520), ("pillow", -480, -170)]


def room(d, cam, t, storm=0.0, sun=0.0):
    wall = mix(mix(WALL, (60, 60, 80, 255), storm), (230, 200, 160, 255), sun)
    d.rectangle([0, 0, W, H], fill=wall)
    # wallpaper stripes
    for k in range(-12, 14):
        x = cam.p(k * 140, 0)[0]
        d.line([(x, 0), (x, cam.p(0, 0)[1])], fill=col(dimc(wall, 0.92), 1), width=max(1, int(cam.s(30))))
    # window
    wx0, wy0 = cam.p(-150, -900)
    wx1, wy1 = cam.p(250, -350)
    d.rectangle([wx0, wy0, wx1, wy1], fill=col(mix((140, 190, 240, 255), (255, 230, 170, 255), sun), 1))
    if sun > 0:
        glow(d, (wx0 + wx1) / 2, (wy0 + wy1) / 2, cam.s(800), (255, 220, 150), 0.6 * sun)
        fy = cam.p(0, 0)[1]
        tpoly(d, [(wx0, wy0), (wx1, wy0), (wx1 + cam.s(500), fy), (wx0 + cam.s(200), fy)], col((255, 230, 170, 255), 0.18 * sun))
    d.rectangle([wx0, wy0, wx1, wy1], outline=(110, 80, 60, 255), width=max(2, int(cam.s(14))))
    d.line([((wx0 + wx1) / 2, wy0), ((wx0 + wx1) / 2, wy1)], fill=(110, 80, 60, 255), width=max(2, int(cam.s(10))))
    # floor
    fy = cam.p(0, 0)[1]
    if fy < H:
        d.rectangle([0, fy, W, H], fill=mix((120, 80, 56, 255), (60, 50, 50, 255), storm))
    # puddles left by the storm
    if sun > 0 or storm > 0.5:
        for x in (-500, 120, 600):
            px, py = cam.p(x, 6)
            d.ellipse([px - cam.s(140), py - cam.s(14), px + cam.s(140), py + cam.s(14)], fill=col((150, 190, 230, 255), 0.7))
    # sofa
    d.rounded_rectangle(cam.box(-760, -260, -260, -80), int(cam.s(40)), fill=(110, 60, 70, 255))
    d.rounded_rectangle(cam.box(-800, -150, -220, -20), int(cam.s(40)), fill=(140, 76, 86, 255))
    # bookshelf
    d.rectangle(cam.box(420, -900, 760, 0), fill=(100, 70, 50, 255))
    for k in range(4):
        d.rectangle(cam.box(430, -860 + k * 220, 750, -845 + k * 220), fill=(70, 48, 34, 255))


def thing(d, cam, kind, x, y, rot, a=1.0):
    sx, sy = cam.p(x, y)
    s = cam.s(1)
    def R(px, py):
        return (sx + px * math.cos(rot) - py * math.sin(rot), sy + px * math.sin(rot) + py * math.cos(rot))
    if kind == "book":
        d.polygon([R(-40 * s, -55 * s), R(40 * s, -55 * s), R(40 * s, 55 * s), R(-40 * s, 55 * s)], fill=col((180, 60, 60, 255), a))
    elif kind == "chair":
        d.polygon([R(-60 * s, -60 * s), R(60 * s, -60 * s), R(60 * s, -40 * s), R(-60 * s, -40 * s)], fill=col((120, 80, 50, 255), a))
        d.polygon([R(-60 * s, -200 * s), R(-40 * s, -200 * s), R(-40 * s, 0), R(-60 * s, 0)], fill=col((120, 80, 50, 255), a))
        d.polygon([R(40 * s, -60 * s), R(60 * s, -60 * s), R(60 * s, 0), R(40 * s, 0)], fill=col((120, 80, 50, 255), a))
    elif kind == "lamp":
        d.polygon([R(-8 * s, -300 * s), R(8 * s, -300 * s), R(8 * s, 0), R(-8 * s, 0)], fill=col((60, 60, 60, 255), a))
        d.polygon([R(-70 * s, -300 * s), R(70 * s, -300 * s), R(40 * s, -400 * s), R(-40 * s, -400 * s)], fill=col((240, 210, 150, 255), a))
    elif kind == "frame":
        d.polygon([R(-90 * s, -70 * s), R(90 * s, -70 * s), R(90 * s, 70 * s), R(-90 * s, 70 * s)], fill=col((150, 110, 60, 255), a))
        d.polygon([R(-70 * s, -50 * s), R(70 * s, -50 * s), R(70 * s, 50 * s), R(-70 * s, 50 * s)], fill=col((120, 170, 200, 255), a))
    elif kind == "cup":
        d.polygon([R(-25 * s, -40 * s), R(25 * s, -40 * s), R(20 * s, 0), R(-20 * s, 0)], fill=col((240, 240, 240, 255), a))
    elif kind == "plant":
        d.polygon([R(-40 * s, -80 * s), R(40 * s, -80 * s), R(30 * s, 0), R(-30 * s, 0)], fill=col((170, 90, 60, 255), a))
        d.ellipse([sx - 80 * s, sy - 220 * s, sx + 80 * s, sy - 70 * s], fill=col((80, 140, 80, 255), a))
    elif kind == "pillow":
        d.polygon([R(-70 * s, -40 * s), R(70 * s, -40 * s), R(70 * s, 40 * s), R(-70 * s, 40 * s)], fill=col((230, 190, 90, 255), a))


def objects(d, cam, t, lift=0.0):
    """Furniture lifts into a slow whirlwind around the centre of the room as `lift` rises."""
    for i, (kind, x, y) in enumerate(OBJECTS):
        k = sstep(clamp(lift * 1.4 - i * 0.04))
        ang = t * 1.2 + i * 0.63
        ox = math.cos(ang) * (380 + 60 * (i % 3))
        oy = -620 + math.sin(ang) * 220
        px, py = lerp(x, ox, k), lerp(y, oy, k)
        rot = k * (t * 2 + i)
        thing(d, cam, kind, px, py, rot)


def chaos(d, cam, t, size, a=1.0):
    if size <= 0.01:
        return
    cx, cy = cam.p(0, -700)
    R = cam.s(420) * size
    for k in range(8):
        rr = R * (1 - k * 0.1)
        ang = t * (2 + k * 0.3)
        tpoly(d, [(cx - rr * 1.3, cy - rr * 0.5), (cx + rr * 1.3, cy + rr * 0.5)], col((30 + k * 6, 26 + k * 4, 50 + k * 8, 255), 0.18 * a), kind="ellipse")
        polyline(d, [(cx + math.cos(ang + j * 0.3) * rr * 1.2, cy + math.sin(ang + j * 0.3) * rr * 0.45) for j in range(12)], 1,
                 col((150, 140, 200, 255), 0.35 * a), max(1, int(cam.s(5))))
    for o in (-1, 1):
        ex = cx + o * R * 0.25
        d.polygon([(ex - R * 0.1, cy - R * 0.05), (ex + R * 0.1, cy - R * 0.08), (ex, cy + R * 0.05)], fill=col((220, 230, 255, 255), a))
        glow(d, ex, cy, R * 0.25, (180, 200, 255), 0.6 * a)
    d.text((cx, cy - R * 0.6), "CHAOS", font=font(int(clamp(R * 0.12, 16, 40))), fill=col((200, 190, 240, 255), a), anchor="mm")


def person(d, cam, t, x=0, mode="stand", **kw):
    fx, fy = cam.p(x, 0)
    return figure(d, fx, fy, cam.s(CH), YOU, mode=mode, face=kw.pop("face", 1), acc=("hair",), **kw)


def calm(d, cam, x, t, a=1.0, sit=0.0):
    fx, fy = cam.p(x, 0)
    glow(d, fx, fy - cam.s(150), cam.s(380), CALM, 0.5 * a)
    figure(d, fx, fy, cam.s(CH), CALM, mode="sit" if sit > 0.5 else "stand", face=-1, a=a, acc=("hair",), name="CALM", name_a=a,
           eye_col=(40, 70, 110, 255), mouth=0.3)


def breath(d, cam, x, t, a):
    """A slow expanding ring: breathe in, breathe out."""
    if a <= 0:
        return
    k = 0.5 + 0.5 * math.sin(t * 1.4)
    fx, fy = cam.p(x, -180)
    r = cam.s(120 + 120 * k)
    d.ellipse([fx - r, fy - r, fx + r, fy + r], outline=col(CALM, 0.6 * a), width=max(2, int(cam.s(6))))
    d.text((fx, fy + r + cam.s(40)), "BREATHE IN" if math.cos(t * 1.4) > 0 else "BREATHE OUT", font=font(int(cam.s(30))), fill=col(CALM, 0.8 * a), anchor="mm")


def indoor_rain(d, cam, t, a):
    if a <= 0:
        return
    top = cam.p(0, -980)[1]
    r = random.Random(3)
    for i in range(int(140 * a)):
        x = r.uniform(0, W)
        y = top + ((r.uniform(0, H) + t * r.uniform(900, 1300)) % (cam.p(0, 0)[1] - top))
        d.line([(x, y), (x - 6, y + 34)], fill=col((180, 200, 240, 255), 0.6), width=2)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # a quiet room. A single drop falls from the ceiling and lands on the person's head. Thunder. Indoors.
    cam = cam_lerp((0, -420, 0.62), (-60, -360, 0.78), sstep(p))
    fl = pulse(t, 2.1, 0.12)
    room(d, cam, t, storm=0.3 * ramp(t, 2.0, 1.0))
    objects(d, cam, t)
    person(d, cam, t, x=-60, mode="sit" if t < 2.0 else "stand", look=0.6 if t > 1.4 else 0.0)
    dy = lerp(-980, -CH, clamp((t - 0.6) / 0.9))
    if t < 1.55:
        dx, ddy = cam.p(-60, dy)
        d.ellipse([dx - cam.s(10), ddy - cam.s(16), dx + cam.s(10), ddy + cam.s(10)], fill=col((150, 190, 240, 255), 1))
    else:
        particles(d, *cam.p(-60, -CH), cam.s(60), ramp(t, 1.55, 0.4), (150, 190, 240), n=10, seed=1, rise=0.5)
    if t > 2.0:
        cx, cy = cam.p(0, -980)
        for j in range(4):
            cloud(d, cx - cam.s(500) + j * cam.s(330), cy + cam.s(60), cam.s(140), col((80, 80, 100, 255), ramp(t, 2.0, 0.8)), w=max(2, int(cam.s(60))))
        indoor_rain(d, cam, t, ramp(t, 2.3, 0.6) * 0.6)
    flash(d, fl)


def s1_panic(d, t, dur):
    p = t / dur
    # the furniture lifts into a whirlwind; the person panics, and Chaos grows with every flail
    cam = cam_lerp((-60, -360, 0.78), (0, -480, 0.6), sstep(p))
    fl = pulse(t, 1.2, 0.1) + pulse(t, 2.6, 0.1)
    shake(cam, t, 8 * p)
    room(d, cam, t, storm=0.5 + 0.5 * p)
    chaos(d, cam, t, 0.3 + 0.7 * p)
    objects(d, cam, t, lift=sstep(p))
    person(d, cam, t, x=-60, mode="flail", phase=t * 3, look=0.6, mouth=-0.6)
    indoor_rain(d, cam, t, 0.8)
    if fl > 0:
        bolt(d, W * 0.55, cam.p(0, -900)[1], fl, 0.7)
    flash(d, fl)


def s2_control(d, t, dur):
    p = t / dur
    cam = cam_lerp((0, -480, 0.6), (0, -500, 0.55), p)
    fl = pulse(t, 1.0, 0.1)
    shake(cam, t, 10)
    room(d, cam, t, storm=1.0)
    chaos(d, cam, t, 1.0 + 0.1 * math.sin(t * 5))
    objects(d, cam, t, lift=1.0)
    person(d, cam, t, x=-60, mode="flail", phase=t * 3, look=0.6, mouth=-0.6)
    indoor_rain(d, cam, t, 1.0)
    if fl > 0:
        bolt(d, W * 0.4, cam.p(0, -900)[1], fl, 0.8)
    flash(d, fl)
    top_caption(d, ["YOU CAN'T ALWAYS CONTROL", "WHAT HAPPENS."], t, dur, accent={"CAN'T"})


def s3_next(d, t, dur):
    p = t / dur
    # Calm walks in and sits. The person stops, breathes with it, and sits too. The storm slowly lets go.
    cam = cam_lerp((0, -500, 0.55), (-100, -380, 0.75), sstep(p))
    settle = sstep(ramp(p, 0.35, 0.6))
    room(d, cam, t, storm=1 - settle)
    chaos(d, cam, t, 1.0 - settle, a=1 - settle)
    objects(d, cam, t, lift=1 - settle)
    walk = sstep(ramp(p, 0.0, 0.25))
    calm(d, cam, lerp(600, 200, walk), t, a=ramp(p, 0.0, 0.15), sit=ramp(p, 0.28, 0.05))
    sitting = p > 0.45
    person(d, cam, t, x=-60, mode="sit" if sitting else "stand", look=0.2 * (1 - settle), mouth=-0.3 + 0.6 * settle, head_down=0.1)
    breath(d, cam, -60, t, ramp(p, 0.3, 0.2) * (1 - ramp(p, 0.9, 0.1)))
    indoor_rain(d, cam, t, 1 - settle)
    top_caption(d, ["BUT YOU CAN CONTROL", "WHAT HAPPENS NEXT."], t, dur, accent={"CAN", "NEXT."})


def s4_sun(d, t, dur):
    p = t / dur
    cam = cam_lerp((-100, -380, 0.75), (0, -420, 0.62), p)
    room(d, cam, t, storm=0.0, sun=sstep(ramp(p, 0.0, 0.5)))
    objects(d, cam, t)
    calm(d, cam, 200, t, a=1 - p * 0.6, sit=1.0)
    person(d, cam, t, x=-60, mode="sit", mouth=0.5)
    dust(d, t, 0.7, n=50, color=(255, 230, 180))
    if p > 0.3:
        final_card(d, t - dur * 0.3, dur, ["CONTROL WHAT'S NEXT."], [(60, 80, 120, 255)], size=104, y=H * 0.18)


SCENES = [s0_hook, s1_panic, s2_control, s3_next, s4_sun, s_follow]
