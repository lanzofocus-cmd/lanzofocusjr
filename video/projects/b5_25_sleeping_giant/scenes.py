"""THE SLEEPING GIANT — a city built on top of a giant nobody believes can wake.

World: a night city of small lit windows perched on a mountain; the mountainside below is a colossal sleeping
stone face, its closed eye glowing faintly with each slow breath. Townspeople shrug: IT WILL NEVER WAKE.
THE AWAKENER, one small figure in red, climbs a bell tower and rings THE ALARM again and again; rings ripple
through the rock until the giant's eye cracks open, blazing gold.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, stars, moon, dust)
from kit import s_follow

TITLE = ("THE SLEEPING", "GIANT")
OUTPUT = "125_The_Sleeping_Giant_16x9.mp4"
LINES = [
    "",
    "",
    "Your potential isn't gone.",
    "It's asleep.",
    "",
    "",
]
SILENT = {0: 3.4, 1: 3.0, 4: 3.4}
GAPS = {2: 3.4, 3: 5.4}

ROCK = (54, 50, 70, 255)
ROCK_L = (90, 84, 110, 255)
GOLD = (255, 200, 90, 255)
AWAKE = (230, 60, 60, 255)
TOWN = (140, 140, 160, 255)
CH = 120
EYE = (120, 900)
TOWER_X = 650


def scene(d, cam, t, eye=0.0, quake=0.0, lights=0.5):
    draw_sky(d, (4, 6, 20, 255), (30, 36, 70, 255))
    stars(d, 0.9, seed=11, n=100, ymax=0.6)
    moon(d, W * 0.85, H * 0.15, 50, 0.9, bg=(4, 6, 20))
    # the mountain / the giant's face (profile facing left, lying on its back along the mountainside)
    face = [(-2600, 3000), (-2600, 0), (-1600, -80), (-900, 0), (-300, 120), (100, 380), (60, 520), (260, 640), (120, 760), (330, 1000),
            (180, 1200), (420, 1400), (300, 1700), (700, 2100), (2600, 2200), (2600, 3000)]
    pts = [cam.p(x, y) for x, y in face]
    d.polygon(pts, fill=col(ROCK, 1))
    polyline(d, pts[1:-2], 1, col(ROCK_L, 1), max(2, int(cam.s(8))))
    # brow, nose, lips carved into the rock
    for seg in ([(-200, 760), (200, 690), (420, 700)], [(330, 1000), (520, 1060), (440, 1180)], [(420, 1400), (600, 1440)], [(300, 1560), (560, 1580)]):
        polyline(d, [cam.p(*q) for q in seg], 1, col(ROCK_L, 1), max(2, int(cam.s(14))))
    # the eye
    ex, ey = cam.p(*EYE)
    w = cam.s(200)
    breath = 0.5 + 0.5 * math.sin(t * 0.9)
    if eye <= 0.02:
        d.arc([ex - w, ey - w * 0.5, ex + w, ey + w * 0.5], 10, 170, fill=col(mix(ROCK_L, GOLD, 0.25 * breath), 1), width=max(2, int(cam.s(16))))
        glow(d, ex, ey + w * 0.2, w * 0.8, GOLD, 0.15 * breath)
    else:
        oh = w * 0.5 * eye
        d.ellipse([ex - w, ey - oh, ex + w, ey + oh], fill=col((255, 230, 160, 255), 1))
        d.ellipse([ex - w * 0.3, ey - min(oh, w * 0.3), ex + w * 0.3, ey + min(oh, w * 0.3)], fill=col(GOLD, 1))
        glow(d, ex, ey, w * (3 + 4 * eye), GOLD, 0.8 * eye)
        tpoly(d, [(ex, ey), (ex + cam.s(2600), ey - cam.s(600)), (ex + cam.s(2600), ey + cam.s(500))], col(GOLD, 0.18 * eye))
    # the city on top of the mountain
    r = random.Random(4)
    for i in range(34):
        x = -2400 + i * 75 + r.uniform(-10, 10)
        top_y = -80 * (1 - abs(x + 1600) / 1600) if x < -900 else 0
        hgt = r.uniform(80, 260)
        a, b = cam.p(x, top_y - hgt), cam.p(x + 60, top_y + 20)
        d.rectangle([a[0], a[1], b[0], b[1]], fill=(26, 26, 40, 255))
        for k in range(int(hgt / 50)):
            if r.random() < lights:
                q = cam.p(x + 20, top_y - hgt + 20 + k * 50)
                d.rectangle([q[0], q[1], q[0] + cam.s(18), q[1] + cam.s(24)], fill=col((255, 210, 130, 255), 0.9))
    # bell tower
    bx = TOWER_X - 1600
    base = cam.p(bx, -40)
    tp = cam.p(bx, -620)
    d.rectangle([base[0] - cam.s(70), tp[1], base[0] + cam.s(70), base[1]], fill=(40, 38, 54, 255))
    d.polygon([(tp[0] - cam.s(90), tp[1]), (tp[0], tp[1] - cam.s(160)), (tp[0] + cam.s(90), tp[1])], fill=(60, 40, 50, 255))
    fog(d, *cam.p(0, 300), cam.s(6000), 0.2, (150, 160, 220))
    if quake > 0:
        particles(d, *cam.p(0, 600), cam.s(2000), (t * 0.8) % 1, (120, 110, 130), n=50, seed=int(t * 0.8), rise=-0.8, size=4)


def bell(d, cam, t, ring=0.0, rings=()):
    bx = TOWER_X - 1600
    bp = cam.p(bx, -520)
    sw = math.sin(t * 8) * 0.5 * ring
    r = cam.s(50)
    cx, cy = bp[0] + math.sin(sw) * r * 0.6, bp[1]
    d.polygon([(cx - r, cy + r), (cx - r * 0.6, cy - r * 0.8), (cx + r * 0.6, cy - r * 0.8), (cx + r, cy + r)], fill=col(GOLD, 1))
    for k in rings:  # shock rings travelling outward through rock
        rr = cam.s(100 + 2500 * k)
        d.ellipse([bp[0] - rr, bp[1] - rr * 0.6, bp[0] + rr, bp[1] + rr * 0.6], outline=col(GOLD, 0.6 * (1 - k)), width=max(1, int(cam.s(8))))


def awakener(d, cam, t, mode="pull", y=-400, x=None):
    x = TOWER_X - 1600 + 110 if x is None else x
    fx, fy = cam.p(x, y)
    figure(d, fx, fy, cam.s(CH), AWAKE, mode=mode, phase=t * 8, face=-1, acc=("hair",), name="THE AWAKENER")


def townsfolk(d, cam, t, a=1.0):
    for i, x in enumerate((-2200, -2000, -1850, -1300, -1150)):
        fx, fy = cam.p(x, -40 if x < -900 else 0)
        figure(d, fx, fy, cam.s(CH), TOWN, mode="stand", face=1 if i % 2 else -1, a=a, acc=("hair",), hands=((fx - cam.s(30), fy - cam.s(CH * 0.75)), (fx + cam.s(30), fy - cam.s(CH * 0.75))))


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # over the night city, then a slow tilt down the cliff: the cliff is a face, and it's breathing
    cam = cam_lerp((-1600, -300, 0.6), (0, 700, 0.42), sstep(p))
    scene(d, cam, t)


def s1_doubt(d, t, dur):
    p = t / dur
    cam = cam_lerp((-1500, -250, 0.85), (-1100, -350, 0.75), p)
    scene(d, cam, t)
    townsfolk(d, cam, t)
    d.text((W * 0.35, H * 0.3), "IT WILL NEVER WAKE.", font=font(60), fill=col((200, 200, 220, 255), ramp(t, 0.3, 0.5)), anchor="mm")
    climb = sstep(ramp(p, 0.3, 0.7))
    awakener(d, cam, t, mode="walk", y=lerp(-40, -400, climb), x=TOWER_X - 1600 + lerp(-200, 110, climb))


def s2_gone(d, t, dur):
    p = t / dur
    # ring after ring; the rings pass through the rock; the giant sleeps on
    cam = cam_lerp((-1100, -350, 0.75), (-600, 200, 0.45), sstep(p))
    scene(d, cam, t)
    bell(d, cam, t, ring=1.0, rings=[((t * 0.8 + k / 3) % 1) for k in range(3)])
    awakener(d, cam, t, mode="pull")
    top_caption(d, ["YOUR POTENTIAL", "ISN'T GONE."], t, dur, accent={"POTENTIAL", "GONE."})


def s3_asleep(d, t, dur):
    p = t / dur
    # the eyelid flickers... and opens; the mountain shakes; the whole city lights up
    eye = sstep(ramp(p, 0.3, 0.4)) if p > 0.3 else 0.08 * pulse(p, 0.15, 0.05) + 0.06 * pulse(p, 0.24, 0.04)
    cam = cam_lerp((-600, 200, 0.45), (100, 800, 0.7), sstep(ramp(p, 0.0, 0.5)))
    if p > 0.6:
        cam = cam_lerp((100, 800, 0.7), (-600, 300, 0.32), sstep((p - 0.6) / 0.4))
    quake = sstep(ramp(p, 0.35, 0.3))
    shake(cam, t, 14 * quake * (1 - ramp(p, 0.85, 0.15)))
    scene(d, cam, t, eye=eye, quake=quake, lights=0.5 + 0.5 * quake)
    bell(d, cam, t, ring=1.0 - quake, rings=[((t * 0.8 + k / 3) % 1) for k in range(3)] if quake < 0.5 else ())
    awakener(d, cam, t, mode="pull" if quake < 0.5 else "cheer")
    top_caption(d, ["IT'S ASLEEP."], t, dur, accent={"ASLEEP."})


def s4_end(d, t, dur):
    cam = Cam(-600, 300, 0.32)
    scene(d, cam, t, eye=1.0, lights=1.0)
    awakener(d, cam, t, mode="cheer")
    stage_end(d, t, dur, ["WAKE IT UP."], [GOLD], size=140, dim=0.4, glow_col=GOLD, y=H * 0.3)


SCENES = [s0_hook, s1_doubt, s2_gone, s3_asleep, s4_end, s_follow]
