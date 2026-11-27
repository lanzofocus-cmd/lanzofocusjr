"""THE ARMOR OF DISCIPLINE — a warrior with no armor, and a blacksmith who forges it out of habits.

World: two places. A storm-lit arena where swarms of glowing DISTRACTIONS (notification orbs) batter an
unarmoured WARRIOR until the shield drops; and a cavernous red-orange forge where THE BLACKSMITH hammers glowing
habit symbols — ROUTINE, FOCUS, PATIENCE, CONSISTENCY — into plates of armor. Clad in them, the warrior walks
back through the swarm while the orbs spark off the steel.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, dust, flash)
from kit import s_follow

TITLE = ("THE ARMOR", "OF DISCIPLINE")
OUTPUT = "112_The_Armor_Of_Discipline_16x9.mp4"
LINES = [
    "",
    "",
    "Discipline isn't a weapon.",
    "It's armor.",
    "",
    "",
]
SILENT = {0: 2.8, 1: 3.6, 4: 3.4}
GAPS = {2: 3.4, 3: 5.6}

WAR = (220, 210, 200, 255)
SMITH = (170, 90, 60, 255)
STEEL = (190, 200, 215, 255)
FIRE = (255, 140, 50, 255)
DIS = (255, 80, 200, 255)
CH = 260
HABITS = ["ROUTINE", "FOCUS", "PATIENCE", "CONSISTENCY"]
PIECES = ["helmet", "chest", "gauntlets", "shield"]


def arena(d, cam, t, light=1.0):
    draw_sky(d, (10, 8, 20, 255), (50, 30, 60, 255))
    gy = cam.p(0, 0)[1]
    # colosseum arches
    for k in range(-10, 11):
        x = k * 260
        a, b = cam.p(x - 90, -700), cam.p(x + 90, -200)
        d.rectangle([a[0], a[1] + (b[0] - a[0]) * 0.5, b[0], b[1]], fill=(30, 22, 40, 255))
        d.chord([a[0], a[1], b[0], a[1] + (b[0] - a[0])], 180, 360, fill=(30, 22, 40, 255))
    d.rectangle([0, cam.p(0, -200)[1], W, gy], fill=(40, 30, 46, 255))
    if gy < H:
        d.rectangle([0, gy, W, H], fill=(60, 48, 52, 255))
    fog(d, *cam.p(0, -100), cam.s(4000), 0.2, (200, 160, 220))


def orbs(d, cam, t, n=18, target=(0, -150), bounce=0.0, hit_rate=1.0):
    """Swirling notification orbs. With bounce>0 they spark off the target instead of hitting."""
    r = random.Random(5)
    for i in range(n):
        ph = r.uniform(0, 6.28)
        sp = r.uniform(0.6, 1.4)
        rad = r.uniform(250, 900)
        u = (t * sp * 0.4 + ph) % 1
        ang = ph + t * sp
        # spiral inward toward the target
        rr = rad * (1 - u)
        x, y = target[0] + math.cos(ang) * rr, target[1] + math.sin(ang) * rr * 0.6
        if bounce > 0 and u > 0.75:
            k = (u - 0.75) / 0.25
            x = target[0] + math.cos(ang) * (rad * 0.25 + k * 500)
            y = target[1] + math.sin(ang) * (rad * 0.15) - k * 200
        sx, sy = cam.p(x, y)
        s = cam.s(18)
        glow(d, sx, sy, s * 3, DIS, 0.6)
        d.rounded_rectangle([sx - s, sy - s, sx + s, sy + s], int(s * 0.4), fill=col((255, 160, 225, 255), 1))
        d.ellipse([sx + s * 0.4, sy - s * 1.3, sx + s * 1.3, sy - s * 0.4], fill=col((255, 50, 60, 255), 1))
        if bounce > 0 and 0.74 < u < 0.8:
            particles(d, sx, sy, cam.s(80), (u - 0.74) / 0.06, (255, 230, 150), n=10, seed=i, rise=0.2)


def armor(d, fx, fy, h, pieces, a=1.0, shine=0.0, face=1):
    """Armor plates drawn over a standing figure. pieces: {name: 0..1 attached}."""
    c = col(mix(STEEL, WHITE, shine), a)
    edge = col((90, 100, 120, 255), a)
    hx, hy = fx + face * 0.0 * h, fy - 0.84 * h
    def off(k):
        return (1 - k) * h * 1.5
    k = pieces.get("helmet", 0)
    if k > 0:
        oy = -off(k)
        d.chord([hx - 0.14 * h, hy - 0.15 * h + oy, hx + 0.14 * h, hy + 0.12 * h + oy], 180, 360, fill=c)
        d.rectangle([hx - 0.14 * h, hy - 0.02 * h + oy, hx + 0.14 * h, hy + 0.06 * h + oy], fill=c)
        d.rectangle([hx + face * 0.02 * h, hy - 0.01 * h + oy, hx + face * 0.13 * h, hy + 0.02 * h + oy], fill=(20, 20, 30, int(255 * a)))
        d.polygon([(hx - 0.02 * h, hy - 0.15 * h + oy), (hx, hy - 0.26 * h + oy), (hx + 0.02 * h, hy - 0.15 * h + oy)], fill=col((200, 40, 40, 255), a))
    k = pieces.get("chest", 0)
    if k > 0:
        ox = -face * off(k)
        pts = [(fx - 0.13 * h + ox, fy - 0.78 * h), (fx + 0.13 * h + ox, fy - 0.78 * h), (fx + 0.11 * h + ox, fy - 0.5 * h), (fx + ox, fy - 0.44 * h), (fx - 0.11 * h + ox, fy - 0.5 * h)]
        d.polygon(pts, fill=c, outline=edge)
        d.line([(fx + ox, fy - 0.76 * h), (fx + ox, fy - 0.47 * h)], fill=edge, width=max(1, int(h * 0.01)))
    k = pieces.get("gauntlets", 0)
    if k > 0:
        oy = off(k)
        for sx in (fx - 0.16 * h, fx + 0.16 * h):
            d.rounded_rectangle([sx - 0.04 * h, fy - 0.52 * h + oy, sx + 0.04 * h, fy - 0.42 * h + oy], int(h * 0.02), fill=c)
    k = pieces.get("shield", 0)
    if k > 0:
        ox = face * off(k)
        sx, sy = fx + face * 0.22 * h + ox, fy - 0.55 * h
        r = 0.2 * h
        d.ellipse([sx - r * 0.8, sy - r, sx + r * 0.8, sy + r], fill=c, outline=edge, width=max(2, int(h * 0.015)))
        d.ellipse([sx - r * 0.3, sy - r * 0.35, sx + r * 0.3, sy + r * 0.35], fill=col(FIRE, a))


def warrior(d, cam, x, t, mode="stand", pieces=None, shine=0.0, **kw):
    fx, fy = cam.p(x, 0)
    h = cam.s(CH)
    figure(d, fx, fy, h, WAR, mode=mode, face=kw.pop("face", 1), acc=("hair",), name=kw.pop("name", None), **kw)
    if pieces:
        armor(d, fx, fy, h, pieces, shine=shine)
    return fx, fy


def forge(d, cam, t, heat=1.0):
    draw_sky(d, (14, 6, 4, 255), (60, 24, 10, 255))
    gy = cam.p(0, 0)[1]
    # furnace mouth
    fx0, fx1 = cam.p(-900, 0)[0], cam.p(-400, 0)[0]
    top = cam.p(0, -500)[1]
    d.rectangle([fx0 - cam.s(60), top - cam.s(80), fx1 + cam.s(60), gy], fill=(50, 30, 24, 255))
    d.chord([fx0, top, fx1, top + (fx1 - fx0)], 180, 360, fill=col(mix((80, 30, 10, 255), (255, 170, 60, 255), heat * (0.85 + 0.15 * math.sin(t * 9))), 1))
    d.rectangle([fx0, top + (fx1 - fx0) / 2, fx1, gy], fill=col(mix((80, 30, 10, 255), (255, 150, 50, 255), heat * (0.85 + 0.15 * math.sin(t * 7))), 1))
    glow(d, (fx0 + fx1) / 2, (top + gy) / 2, cam.s(900), FIRE, 0.7 * heat)
    if gy < H:
        d.rectangle([0, gy, W, H], fill=(30, 18, 14, 255))
    # anvil
    ax = 250
    d.polygon([cam.p(ax - 220, -230), cam.p(ax + 260, -230), cam.p(ax + 180, -170), cam.p(ax - 140, -170)], fill=(60, 60, 70, 255))
    d.rectangle(cam.box(ax - 80, -170, ax + 80, -40), fill=(50, 50, 60, 255))
    d.rectangle(cam.box(ax - 150, -40, ax + 150, 0), fill=(44, 44, 54, 255))
    dust(d, t, 0.8 * heat, n=60, color=(255, 170, 80), rise=60)


def smith(d, cam, t, phase):
    fx, fy = cam.p(20, 0)
    h = cam.s(CH * 1.15)
    figure(d, fx, fy, h, SMITH, mode="hammer", phase=phase, face=1, acc=("hair",), bodyw=1.4, name="THE BLACKSMITH",
           prop=lambda dd, fh, bh, hh, a: fh and dd.rectangle([fh[0] - hh * 0.07, fh[1] - hh * 0.26, fh[0] + hh * 0.07, fh[1] - hh * 0.17], fill=col((120, 120, 130, 255), a)))
    d.rectangle([fx - h * 0.1, fy - h * 0.72, fx + h * 0.12, fy - h * 0.35], fill=col((70, 40, 30, 255), 1))  # apron


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # slow-motion: a hammer comes down on glowing metal; sparks bloom in the dark
    cam = Cam(250, -230, 3.2)
    forge(d, cam, t)
    hit = pulse(t, 1.2, 0.08)
    shake(cam, t, 18 * hit)
    ax, ay = cam.p(250, -232)
    d.rounded_rectangle([ax - cam.s(70), ay - cam.s(18), ax + cam.s(70), ay], int(cam.s(6)), fill=col((255, 200, 120, 255), 1))
    glow(d, ax, ay, cam.s(200), FIRE, 0.9)
    hy = lerp(ay - cam.s(400), ay - cam.s(20), sstep(clamp(t / 1.2)) if t < 1.2 else 1 - 0.6 * ramp(t, 1.3, 0.8))
    d.rectangle([ax - cam.s(50), hy - cam.s(70), ax + cam.s(50), hy], fill=(110, 110, 120, 255))
    d.line([(ax, hy - cam.s(35)), (ax + cam.s(260), hy - cam.s(200))], fill=(110, 80, 50, 255), width=int(cam.s(16)))
    particles(d, ax, ay, cam.s(500), ramp(t, 1.2, 1.4), (255, 210, 120), n=70, seed=2, rise=0.6, size=5)
    darkness(d, ax, ay, 0.6)


def s1_battle(d, t, dur):
    p = t / dur
    # the arena: a swarm of glowing distractions hits the unarmoured warrior; the shield falls
    cam = cam_lerp((0, -180, 1.2), (0, -170, 1.4), p)
    hit = max(pulse(t, k, 0.12) for k in (0.9, 1.7, 2.4))
    shake(cam, t, 12 * hit)
    arena(d, cam, t)
    knock = sstep(ramp(t, 1.7, 0.4))
    drop = ramp(t, 1.7, 0.6)
    warrior(d, cam, -60 * knock, t, mode="flail" if 0.8 < t < 2.6 else "stand", phase=t * 3, look=0.6, name="THE WARRIOR",
            pieces={"shield": 1.0} if drop <= 0 else None, lean=-0.2 * knock)
    if drop > 0:
        sx, sy = cam.p(150 + 120 * drop, -140 * (1 - drop))
        d.ellipse([sx - cam.s(40), sy - cam.s(50), sx + cam.s(40), sy + cam.s(50)], fill=col(STEEL, 1))
    orbs(d, cam, t)
    flash(d, hit * 0.6, (255, 120, 200))


def s2_weapon(d, t, dur):
    p = t / dur
    # the forge: each blow drives a glowing habit word into a plate of steel
    cam = cam_lerp((200, -260, 1.05), (240, -270, 1.15), p)
    forge(d, cam, t)
    smith(d, cam, t, t * 5)
    i = min(3, int(p * 4))
    ax, ay = cam.p(250, -232)
    word = HABITS[i]
    glow(d, ax, ay - cam.s(40), cam.s(260), FIRE, 0.8)
    d.rounded_rectangle([ax - cam.s(150), ay - cam.s(40), ax + cam.s(150), ay], int(cam.s(8)), fill=col((255, 190, 110, 255), 1))
    d.text((ax, ay - cam.s(20)), word, font=font(int(cam.s(34))), fill=(120, 40, 10, 255), anchor="mm")
    if abs(math.sin(t * 5)) < 0.15:
        particles(d, ax, ay - cam.s(20), cam.s(260), 0.5, (255, 210, 120), n=20, seed=int(t * 5), rise=0.6)
    # finished plates stacking on the right
    for j in range(i):
        px, py = cam.p(700, -60 - j * 70)
        d.rounded_rectangle([px - cam.s(120), py - cam.s(26), px + cam.s(120), py + cam.s(26)], int(cam.s(6)), fill=col(STEEL, 1))
        d.text((px, py), HABITS[j], font=font(int(cam.s(28))), fill=(50, 60, 80, 255), anchor="mm")
    top_caption(d, ["DISCIPLINE ISN'T", "A WEAPON."], t, dur, accent={"WEAPON."})


def s3_armor(d, t, dur):
    p = t / dur
    # piece by piece the armor flies on — then the warrior walks back into the swarm, untouched
    if p < 0.45:
        u = p / 0.45
        cam = cam_lerp((0, -170, 1.6), (0, -170, 1.8), u)
        arena(d, cam, t)
        pieces = {pc: sstep(ramp(u, 0.1 + j * 0.2, 0.2)) for j, pc in enumerate(PIECES)}
        warrior(d, cam, 0, t, mode="stand", pieces=pieces, shine=0.3)
        for j, pc in enumerate(PIECES):
            k = ramp(u, 0.1 + j * 0.2 + 0.18, 0.1)
            if 0 < k < 1:
                fx, fy = cam.p(0, -150)
                particles(d, fx, fy, cam.s(200), k, (255, 230, 160), n=20, seed=j, rise=0.2)
                d.text((fx + cam.s(240), fy - cam.s(120) - j * cam.s(40)), HABITS[j], font=font(int(cam.s(30))), fill=col((255, 220, 150, 255), 1 - k), anchor="lm")
    else:
        u = (p - 0.45) / 0.55
        x = lerp(-400, 500, u)
        cam = Cam(x + 100, -180, lerp(1.4, 1.2, u))
        arena(d, cam, t)
        warrior(d, cam, x, t, mode="walk", phase=x / 50, pieces={pc: 1 for pc in PIECES}, shine=0.4 + 0.2 * math.sin(t * 6), swing=0.3)
        orbs(d, cam, t, target=(x, -150), bounce=1.0)
    top_caption(d, ["IT'S ARMOR."], t, dur, accent={"ARMOR."})


def s4_end(d, t, dur):
    x = 500 + 60 * t
    cam = Cam(x + 100, -180, 1.2)
    arena(d, cam, t)
    warrior(d, cam, x, t, mode="stand", pieces={pc: 1 for pc in PIECES}, shine=0.5)
    orbs(d, cam, t, target=(x, -150), bounce=1.0, n=14)
    stage_end(d, t, dur, ["BUILD YOUR ARMOR."], [STEEL], size=120, dim=0.45, glow_col=FIRE, y=H * 0.32)


SCENES = [s0_hook, s1_battle, s2_weapon, s3_armor, s4_end, s_follow]
