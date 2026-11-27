"""THE OCEAN OF OPPORTUNITIES — a small sailboat in a safe harbor, watching the others leave.

World: shot from water level, unlike the steamship film. A stone harbor at night full of reflected lights; tall
ships glide past toward the open sea. THE SAILOR (yellow oilskin) sits in a little moored sailboat. When they cast
off, the camera rolls with the swell: the horizon tilts, huge waves rise, spray flies, and then it all opens onto a
calm, gold sunrise ocean where a whale breaches.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, stars, sun, rain)
from kit import s_follow

TITLE = ("THE OCEAN OF", "OPPORTUNITIES")
OUTPUT = "136_The_Ocean_Of_Opportunities_16x9.mp4"
LINES = [
    "",
    "Safety can protect you.",
    "But it can also keep you…",
    "From everything waiting beyond it.",
    "",
    "",
]
SILENT = {0: 3.2, 4: 3.6}
GAPS = {1: 1.4, 2: 0.8, 3: 6.8}

SAILOR = (255, 210, 60, 255)
HULL = (200, 80, 60, 255)
SAIL = (245, 240, 230, 255)


def sea_frame(d, t, roll=0.0, horizon=0.5, storm=0.0, dawn=0.0, night=1.0):
    """Sky and sea split by a horizon line that tilts with the boat's roll."""
    top = mix(mix((8, 10, 30, 255), (40, 44, 60, 255), storm), (90, 140, 210, 255), dawn)
    bot = mix(mix((30, 40, 80, 255), (90, 96, 110, 255), storm), (255, 190, 130, 255), dawn)
    draw_sky(d, top, bot)
    stars(d, night * (1 - dawn) * (1 - storm), seed=6, n=80, ymax=horizon * 0.9)
    hy = H * horizon
    dy = math.tan(roll) * W / 2
    if dawn > 0.05:
        sun(d, W * 0.62, hy - 30 + dy * 0.24, 110, dawn, (255, 220, 150, 255))
        tpoly(d, [(W * 0.62 - 120, hy + dy * 0.24), (W * 0.62 + 120, hy + dy * 0.24), (W * 0.7, H), (W * 0.54, H)], col((255, 220, 150, 255), 0.3 * dawn))
    sea_c = mix(mix((10, 20, 46, 255), (40, 50, 60, 255), storm), (60, 110, 160, 255), dawn)
    d.polygon([(0, hy + dy), (W, hy - dy), (W, H), (0, H)], fill=sea_c)
    for k in range(10):  # wave bands receding to the horizon
        u = (k / 10) ** 1.6
        y = hy + (H - hy) * u
        amp = (6 + 70 * storm) * (0.3 + u)
        pts = [(x, y + dy * (1 - 2 * x / W) + math.sin(x * 0.01 / (0.3 + u) + t * (1.5 + storm) + k) * amp) for x in range(0, W + 40, 40)]
        polyline(d, pts, 1, col(mix((90, 120, 170, 255), WHITE, storm * 0.6 + dawn * 0.3), 0.3 + 0.3 * u), max(1, int(2 + 3 * u)))
    return hy, dy


def boat(d, cx, cy, s, t, roll=0.0, sail=0.0, a=1.0, sailor=True):
    """A small sailboat at (cx, cy) scale s; sail 0 furled .. 1 full."""
    ca, sa = math.cos(roll), math.sin(roll)
    def R(x, y):
        return (cx + x * ca - y * sa, cy + x * sa + y * ca)
    hull = [R(-180 * s, -40 * s), R(200 * s, -40 * s), R(130 * s, 30 * s), R(-140 * s, 30 * s)]
    d.polygon(hull, fill=col(HULL, a))
    d.line([R(0, -40 * s), R(0, -420 * s)], fill=col((90, 70, 50, 255), a), width=max(2, int(10 * s)))
    if sail > 0:
        d.polygon([R(8 * s, -400 * s), R(8 * s, -60 * s), R(8 * s + 200 * s * sail, -60 * s)], fill=col(SAIL, a))
        d.polygon([R(-8 * s, -380 * s), R(-8 * s, -80 * s), R(-8 * s - 120 * s * sail, -80 * s)], fill=col(dimc(SAIL, 0.9), a))
    if sailor:
        fx, fy = R(-90 * s, -40 * s)
        figure(d, fx, fy, 170 * s, SAILOR, mode="sit_edge" if sail <= 0 else "stand", face=1, acc=("hood",), a=a, look=0.3)


def harbor(d, t, hy, glow_a=1.0):
    # stone quay and lamps on the left; their reflections in the water
    d.polygon([(0, hy - 140), (W * 0.42, hy - 120), (W * 0.42, hy + 40), (0, hy + 40)], fill=(30, 28, 34, 255))
    for i in range(5):
        x = 80 + i * 170
        d.line([(x, hy - 120), (x, hy - 260)], fill=(40, 40, 46, 255), width=6)
        glow(d, x, hy - 270, 70, (255, 200, 120), 0.7 * glow_a)
        d.ellipse([x - 10, hy - 280, x + 10, hy - 260], fill=(255, 220, 150, 255))
        for k in range(5):
            yy = hy + 60 + k * 26 + math.sin(t * 2 + k + i) * 4
            d.line([(x - 18 + math.sin(t * 3 + k) * 6, yy), (x + 18 + math.sin(t * 3 + k) * 6, yy)], fill=col((255, 200, 120, 255), 0.5 * glow_a * (1 - k / 5)), width=4)


def tall_ship(d, x, y, s, t, a=1.0):
    d.polygon([(x - 260 * s, y - 40 * s), (x + 300 * s, y - 40 * s), (x + 220 * s, y + 40 * s), (x - 200 * s, y + 40 * s)], fill=col((24, 22, 30, 255), a))
    for k, mx in enumerate((-120, 40, 180)):
        d.line([(x + mx * s, y - 40 * s), (x + mx * s, y - (500 - 60 * k) * s)], fill=col((24, 22, 30, 255), a), width=max(2, int(8 * s)))
        for j in range(3):
            sy = y - (460 - 60 * k - j * 120) * s
            d.rectangle([x + mx * s - 80 * s, sy, x + mx * s + 80 * s, sy + 90 * s], fill=col((50, 46, 56, 255), a))
    for k in range(5):
        lx = x - 180 * s + k * 90 * s
        d.ellipse([lx - 6 * s, y - 20 * s, lx + 6 * s, y - 8 * s], fill=col((255, 210, 140, 255), a))


def whale(d, x, y, s, k):
    """A whale breaching: rises and falls with k 0..1."""
    if k <= 0 or k >= 1:
        return
    lift = math.sin(math.pi * k)
    bx, by = x, y - lift * 260 * s
    ang = lerp(-0.9, 0.9, k)
    pts = []
    for j in range(16):
        u = j / 15
        px = lerp(-300, 300, u) * s
        py = -math.sin(math.pi * u) * 90 * s
        pts.append((bx + px * math.cos(ang) - py * math.sin(ang), by + px * math.sin(ang) + py * math.cos(ang)))
    for j in range(15, -1, -1):
        u = j / 15
        px = lerp(-300, 300, u) * s
        py = math.sin(math.pi * u) * 30 * s
        pts.append((bx + px * math.cos(ang) - py * math.sin(ang), by + px * math.sin(ang) + py * math.cos(ang)))
    d.polygon(pts, fill=(40, 60, 90, 255))
    particles(d, x, y, 300 * s, k, WHITE, n=40, seed=3, rise=0.8, size=5)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # water level at night: harbor lights shimmer; a tall ship slides across the frame, out to sea
    hy, dy = sea_frame(d, t, roll=0.02 * math.sin(t), horizon=0.55)
    harbor(d, t, hy)
    tall_ship(d, lerp(W * 0.1, W * 1.25, p), hy + 10, 1.0, t)
    boat(d, W * 0.3, hy + 160, 0.8, t, roll=0.04 * math.sin(t * 1.3))


def s1_safety(d, t, dur):
    p = t / dur
    hy, dy = sea_frame(d, t, roll=0.02 * math.sin(t), horizon=0.55)
    harbor(d, t, hy)
    for i in range(2):
        tall_ship(d, lerp(W * 0.55, W * 1.1, ((p + i * 0.5) % 1)), hy + 5, 0.6, t, a=1.0)
    boat(d, W * 0.32, hy + 200, 1.1, t, roll=0.04 * math.sin(t * 1.3))
    top_caption(d, ["SAFETY CAN", "PROTECT YOU."], t, dur, accent={"SAFETY", "PROTECT"})


def s2_keep(d, t, dur):
    p = t / dur
    # close on the sailor, looking out past the harbor mouth at a faint glow on the horizon
    hy, dy = sea_frame(d, t, roll=0.02 * math.sin(t), horizon=0.6)
    glow(d, W * 0.8, hy, 400, (255, 190, 130), 0.4 + 0.2 * math.sin(t * 2))
    harbor(d, t, hy, glow_a=0.6)
    boat(d, W * 0.42, hy + 330, 2.0, t, roll=0.03 * math.sin(t * 1.3))
    top_caption(d, ["BUT IT CAN ALSO", "KEEP YOU…"], t, dur, accent={"KEEP"})


def s3_beyond(d, t, dur):
    p = t / dur
    # cast off; sails fill; the camera rolls with a heavy swell, waves rise, spray; then calm gold sunrise and a whale
    storm = sstep(ramp(p, 0.08, 0.15)) * (1 - sstep(ramp(p, 0.55, 0.15)))
    dawn = sstep(ramp(p, 0.55, 0.25))
    roll = 0.22 * math.sin(t * 1.6) * storm + 0.02 * math.sin(t)
    hy, dy = sea_frame(d, t, roll=roll, horizon=0.55 - 0.05 * storm, storm=storm, dawn=dawn)
    if p < 0.1:
        harbor(d, t, hy, glow_a=1 - p * 10)
    by = hy + 220 + 60 * math.sin(t * 1.6) * storm
    if storm > 0.2:  # a wall of water rising in front
        crest = H * 0.62 - 200 * storm * (0.5 + 0.5 * math.sin(t * 1.6))
        d.polygon([(0, H), (0, crest + 80), (W * 0.3, crest), (W * 0.6, crest + 60), (W, crest - 20), (W, H)], fill=col((50, 70, 90, 255), 0.9 * storm))
        particles(d, W * 0.5, crest, 700, (t * 0.8) % 1, WHITE, n=40, seed=int(t * 0.8), rise=0.5, size=4)
    boat(d, W * 0.45, by, 1.2, t, roll=roll * 1.2, sail=sstep(ramp(p, 0.02, 0.1)))
    rain(d, t, storm * 0.8, n=180, slant=0.6)
    whale(d, W * 0.75, hy + 60, 0.7, ramp(p, 0.72, 0.22))
    top_caption(d, ["FROM EVERYTHING", "WAITING BEYOND IT."], t, dur, accent={"BEYOND"})


def s4_end(d, t, dur):
    hy, dy = sea_frame(d, t, roll=0.02 * math.sin(t), horizon=0.55, dawn=1.0)
    boat(d, W * 0.45, hy + 220, 1.2, t, roll=0.03 * math.sin(t), sail=1.0)
    stage_end(d, t, dur, ["SAIL BEYOND IT."], [(255, 225, 160, 255)], size=120, dim=0.35, glow_col=(255, 210, 150), y=H * 0.22)


SCENES = [s0_hook, s1_safety, s2_keep, s3_beyond, s4_end, s_follow]
