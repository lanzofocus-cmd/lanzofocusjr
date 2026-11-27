"""THE WATCHTOWER — a guard who keeps looking away, and the shadows that move while they do.

World: a black marsh drowned in green-grey fog, one colossal stone watchtower with a lantern at the top. THE GUARD
keeps turning toward drifting glowing lights, pretty distractions that float by. Out in the fog, THE ENEMY is a
crowd of shadow shapes with pale eyes, creeping closer whenever the guard's back is turned. The guard finally
turns, raises the lantern and focuses its beam: the shadows dissolve, and the tower stands at dawn.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, flash, bolt, sun)
from kit import s_follow

TITLE = ("THE", "WATCHTOWER")
OUTPUT = "135_The_Watchtower_16x9.mp4"
LINES = [
    "",
    "",
    "Your attention…",
    "Is your responsibility.",
    "",
    "",
]
SILENT = {0: 3.2, 1: 3.6, 4: 3.4}
GAPS = {2: 1.2, 3: 6.2}

STONE = (50, 56, 58, 255)
LAMP = (255, 220, 140, 255)
LURE = (255, 120, 220, 255)
GUARD = (200, 190, 170, 255)
TOWER_TOP = -1600
CH = 160


def marsh(d, cam, t, dawn=0.0):
    draw_sky(d, mix((6, 10, 10, 255), (110, 140, 170, 255), dawn), mix((24, 34, 30, 255), (255, 200, 160, 255), dawn))
    if dawn > 0.05:
        sun(d, W * 0.8, cam.p(0, 0)[1] - cam.s(200), 70, dawn, (255, 225, 170, 255))
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=mix((10, 16, 14, 255), (70, 80, 70, 255), dawn))
        for k in range(12):  # reeds and pools
            x = cam.p(-3000 + k * 520, 0)[0]
            d.ellipse([x - cam.s(160), gy + cam.s(30), x + cam.s(160), gy + cam.s(60)], fill=mix((20, 30, 34, 255), (120, 150, 170, 255), dawn))


def tower(d, cam, t):
    b0, b1 = cam.p(-260, 0), cam.p(260, 0)
    t0, t1 = cam.p(-170, TOWER_TOP), cam.p(170, TOWER_TOP)
    d.polygon([b0, b1, t1, t0], fill=col(STONE, 1))
    for k in range(1, 14):  # stone courses
        y = k * TOWER_TOP / 14
        w = lerp(260, 170, k / 14)
        d.line([cam.p(-w, y), cam.p(w, y)], fill=(40, 44, 46, 255), width=max(1, int(cam.s(4))))
    # crenellated top platform
    d.rectangle(cam.box(-230, TOWER_TOP - 80, 230, TOWER_TOP), fill=col(STONE, 1))
    for k in range(5):
        x = -230 + k * 110
        d.rectangle(cam.box(x, TOWER_TOP - 150, x + 60, TOWER_TOP - 80), fill=col(STONE, 1))


def guard(d, cam, t, face=1, lift=0.0, look=0.0):
    fx, fy = cam.p(0, TOWER_TOP - 80)
    h = cam.s(CH)
    lx = fx + face * h * lerp(0.25, 0.35, lift)
    ly = fy - h * lerp(0.55, 1.0, lift)
    figure(d, fx, fy, h, GUARD, mode="stand", face=face, acc=("hood",), hands=((fx - face * h * 0.05, fy - h * 0.35), (lx, ly)), look=look,
           name="THE GUARD")
    glow(d, lx, ly, h * 1.2, LAMP, 0.8)
    d.rectangle([lx - h * 0.05, ly - h * 0.06, lx + h * 0.05, ly + h * 0.06], fill=col(LAMP, 1))
    return lx, ly


def lures(d, cam, t, a=1.0):
    """Glowing distractions drifting past the top of the tower (on the side away from the fog)."""
    for i in range(6):
        u = ((t * 0.15 + i / 6) % 1)
        x = lerp(-300, -1400, u)
        y = TOWER_TOP - 60 + 90 * math.sin(t * 1.5 + i)
        sx, sy = cam.p(x, y)
        r = cam.s(24)
        glow(d, sx, sy, r * 4, LURE, 0.6 * a)
        for s in (-1, 1):  # little wings
            d.ellipse([sx + s * r * 0.2 - r * 0.6 + s * r * 0.4, sy - r * (0.4 + 0.4 * abs(math.sin(t * 9 + i))), sx + s * r * 0.2 + r * 0.6 + s * r * 0.4, sy + r * 0.3], fill=col(LURE, a))


def shadows(d, cam, t, near=0.0, dissolve=0.0):
    """Shadow shapes creeping across the marsh toward the tower (from the right)."""
    r = random.Random(4)
    for i in range(14):
        x0 = r.uniform(1200, 3600)
        x = lerp(x0, 400 + r.uniform(0, 400), near)
        h = r.uniform(260, 520)
        k = 1 - clamp(dissolve * 1.5 - r.random() * 0.5)
        if k <= 0:
            continue
        sx, sy = cam.p(x, 0)
        hh = cam.s(h)
        sway = math.sin(t * 1.3 + i) * hh * 0.05
        pts = [(sx - hh * 0.25, sy), (sx - hh * 0.18 + sway, sy - hh * 0.75), (sx + sway, sy - hh), (sx + hh * 0.18 + sway, sy - hh * 0.75), (sx + hh * 0.25, sy)]
        tpoly(d, pts, col((4, 6, 8, 255), 0.85 * k))
        for o in (-1, 1):
            ex, ey = sx + sway + o * hh * 0.06, sy - hh * 0.82
            d.ellipse([ex - hh * 0.025, ey - hh * 0.012, ex + hh * 0.025, ey + hh * 0.012], fill=col((200, 220, 200, 255), k))
        if dissolve > 0 and k < 1:
            particles(d, sx, sy - hh * 0.5, hh * 0.6, 1 - k, (180, 200, 190), n=10, seed=i, rise=0.6)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # pitch dark fog; lightning; the silhouette of a colossal tower; a tiny lantern at the very top
    cam = cam_lerp((0, -700, 0.38), (0, -1000, 0.5), sstep(p))
    fl = pulse(t, 0.8, 0.12) + 0.7 * pulse(t, 1.1, 0.1)
    marsh(d, cam, t)
    tower(d, cam, t)
    guard(d, cam, t)
    fog(d, *cam.p(0, -200), cam.s(6000), 0.5, (140, 170, 150))
    darkness(d, W / 2, H / 2, 0.6 * (1 - fl))
    if fl > 0:
        bolt(d, W * 0.2, 40, fl, 1.0)
    flash(d, fl)


def s1_away(d, t, dur):
    p = t / dur
    # the guard turns to watch the floating lights; out in the fog, the shadows edge closer
    cam = cam_lerp((0, -1100, 0.55), (400, -800, 0.42), sstep(p))
    marsh(d, cam, t)
    shadows(d, cam, t, near=0.45 * p)
    tower(d, cam, t)
    lures(d, cam, t)
    guard(d, cam, t, face=-1, look=0.3)
    fog(d, *cam.p(1500, -150), cam.s(6000), 0.45, (140, 170, 150))


def s2_attention(d, t, dur):
    p = t / dur
    # close on the guard: the eyes leave the lights and go to the fog
    cam = cam_lerp((-100, TOWER_TOP - 200, 1.6), (0, TOWER_TOP - 220, 1.8), p)
    marsh(d, cam, t)
    tower(d, cam, t)
    lures(d, cam, t, a=1 - 0.5 * p)
    guard(d, cam, t, face=-1 if p < 0.5 else 1, look=0.0)
    top_caption(d, ["YOUR ATTENTION…"], t, dur, accent={"ATTENTION…"})


def s3_responsibility(d, t, dur):
    p = t / dur
    # the lantern goes up; a focused beam sweeps the marsh; shadows dissolve; dawn
    lift = sstep(ramp(p, 0.0, 0.2))
    sweep = sstep(ramp(p, 0.2, 0.5))
    dawn = sstep(ramp(p, 0.55, 0.45))
    cam = cam_lerp((0, TOWER_TOP - 220, 1.8), (500, -800, 0.42), sstep(ramp(p, 0.1, 0.5)))
    marsh(d, cam, t, dawn=dawn)
    shadows(d, cam, t, near=0.5, dissolve=sweep)
    tower(d, cam, t)
    lx, ly = guard(d, cam, t, face=1, lift=lift)
    if lift > 0.5:
        ang = lerp(0.15, 0.55, sweep)
        L = cam.s(6000)
        ex, ey = lx + math.cos(ang) * L, ly + math.sin(ang) * L
        tpoly(d, [(lx, ly), (ex, ey - cam.s(500)), (ex, ey + cam.s(500))], col(LAMP, 0.22 * (1 - dawn * 0.6)))
    fog(d, *cam.p(1500, -150), cam.s(6000), 0.4 * (1 - dawn), (140, 170, 150))
    top_caption(d, ["IS YOUR", "RESPONSIBILITY."], t, dur, accent={"RESPONSIBILITY."})


def s4_end(d, t, dur):
    cam = Cam(500, -800, 0.42)
    marsh(d, cam, t, dawn=1.0)
    tower(d, cam, t)
    guard(d, cam, t, face=1, lift=1.0)
    stage_end(d, t, dur, ["GUARD YOUR", "ATTENTION."], [WHITE, LAMP], size=110, dim=0.4, glow_col=LAMP, y=H * 0.3)


SCENES = [s0_hook, s1_away, s2_attention, s3_responsibility, s4_end, s_follow]
