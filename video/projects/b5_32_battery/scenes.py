"""THE EMPTY BATTERY — a person whose energy drains into things that give nothing back.

World: a dark charcoal room drawn like a heads-up display: thin cyan UI lines, percentages, graphs. THE PERSON
carries a glowing battery in their chest. Cables run from it to a phone, an endless feed, notifications and an
argument; energy drains along them as glowing liquid until the battery blinks red. The person unplugs them,
and plugs into THE CHARGERS: meaningful work, rest and focused effort; each refills it in its own colour.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, dust)
from kit import s_follow

TITLE = ("THE EMPTY", "BATTERY")
OUTPUT = "132_The_Empty_Battery_16x9.mp4"
LINES = [
    "",
    "",
    "You're not always tired of working.",
    "Sometimes…",
    "You're tired of working on the wrong things.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.4, 5: 3.4}
GAPS = {2: 1.6, 3: 1.6, 4: 4.8}

CYAN = (80, 220, 255, 255)
RED = (255, 70, 70, 255)
GREEN = (110, 255, 140, 255)
YOU = (220, 220, 230, 255)
DRAINS = [("PHONE", (680, -700)), ("ENDLESS FEED", (720, -380)), ("NOTIFICATIONS", (680, -60)), ("ARGUMENTS", (-700, -560))]
CHARGERS = [("MEANINGFUL WORK", (700, -650), (255, 200, 110, 255)), ("REST", (-700, -550), (150, 160, 255, 255)), ("FOCUSED EFFORT", (700, -200), GREEN)]
CH = 420


def hud_room(d, t):
    d.rectangle([0, 0, W, H], fill=(12, 14, 18, 255))
    for k in range(0, W, 80):  # faint grid
        d.line([(k, 0), (k, H)], fill=(20, 26, 32, 255), width=1)
    for k in range(0, H, 80):
        d.line([(0, k), (W, k)], fill=(20, 26, 32, 255), width=1)
    # corner brackets
    for (x, y, sx, sy) in ((40, 40, 1, 1), (W - 40, 40, -1, 1), (40, H - 40, 1, -1), (W - 40, H - 40, -1, -1)):
        d.line([(x, y), (x + sx * 80, y)], fill=col(CYAN, 0.6), width=3)
        d.line([(x, y), (x, y + sy * 80)], fill=col(CYAN, 0.6), width=3)


def battery_icon(d, cx, cy, s, level, color=None):
    color = color or (GREEN if level > 0.5 else (CYAN if level > 0.2 else RED))
    w, h = 160 * s, 300 * s
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], int(20 * s), outline=col(WHITE, 0.9), width=max(2, int(8 * s)))
    d.rectangle([cx - w * 0.2, cy - h / 2 - 22 * s, cx + w * 0.2, cy - h / 2], fill=col(WHITE, 0.9))
    fill_h = (h - 24 * s) * clamp(level)
    if fill_h > 1:
        d.rounded_rectangle([cx - w / 2 + 12 * s, cy + h / 2 - 12 * s - fill_h, cx + w / 2 - 12 * s, cy + h / 2 - 12 * s], int(10 * s), fill=col(color, 1))
        glow(d, cx, cy, h, color, 0.35)
    return color


def person(d, cam, t, level, mode="stand", **kw):
    fx, fy = cam.p(0, 0)
    h = cam.s(CH)
    figure(d, fx, fy, h, mix((120, 120, 130, 255), YOU, clamp(level * 1.5)), mode=mode, face=1, acc=("hair",), phase=t * 4,
           head_down=kw.pop("head_down", 0.6 * (1 - level)), tired=1 - level if level < 0.4 else 0, **kw)
    bx, by = fx + h * 0.02, fy - h * (0.62 if mode != "sit" else 0.46)
    c = battery_icon(d, bx, by, h / 900, level)
    d.text((bx + h * 0.18, by), f"{int(level * 100)}%", font=font(max(12, int(h * 0.07))), fill=col(c, 1), anchor="lm")
    return bx, by


def cable(d, a, b, t, flow_dir=1, color=CYAN, a_=1.0, flow=1.0):
    """A sagging cable from a to b with glowing pulses travelling along it."""
    pts = []
    for i in range(21):
        u = i / 20
        pts.append((lerp(a[0], b[0], u), lerp(a[1], b[1], u) + math.sin(math.pi * u) * 80))
    polyline(d, pts, 1, col((70, 80, 90, 255), a_), 6)
    for k in range(6):
        u = ((t * 0.7 * flow_dir * flow + k / 6) % 1)
        i = int(u * 20)
        x, y = pts[i]
        d.ellipse([x - 7, y - 7, x + 7, y + 7], fill=col(color, a_))
        glow(d, x, y, 30, color, 0.4 * a_)


def node(d, x, y, label, color=CYAN, a=1.0, icon="box"):
    if a <= 0.01:
        return
    d.rounded_rectangle([x - 160, y - 60, x + 160, y + 60], 16, outline=col(color, a), width=3, fill=(16, 22, 28, 255) if a > 0.99 else None)
    d.text((x, y), label, font=font(30), fill=col(color, a), anchor="mm")


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # a huge battery HUD drains from 100% to 3% in seconds, warning blinks
    hud_room(d, t)
    level = lerp(1.0, 0.03, sstep(ramp(t, 0.3, dur * 0.8)))
    c = battery_icon(d, W / 2, H / 2, 2.0, level)
    blink = level < 0.2 and math.sin(t * 12) > 0
    d.text((W / 2 + 230, H / 2), f"{int(level * 100)}%", font=font(110), fill=col(RED if blink else c, 1), anchor="lm")
    if level < 0.2:
        d.text((W / 2, H - 160), "LOW ENERGY", font=font(50), fill=col(RED, 0.9 if blink else 0.4), anchor="mm")


def s1_drain(d, t, dur):
    p = t / dur
    # the person on the couch, phone in hand; cables carry their energy out to the things that drain it
    cam = Cam(0, -280, 0.85)
    hud_room(d, t)
    level = lerp(0.6, 0.05, sstep(p))
    d.rounded_rectangle(cam.box(-300, -230, 300, -60), int(cam.s(40)), fill=(50, 50, 70, 255))
    bx, by = person(d, cam, t, level, mode="sit")
    for i, (lbl, (x, y)) in enumerate(DRAINS):
        nx, ny = cam.p(x, y)
        a = ramp(t, 0.2 + i * 0.3, 0.4)
        cable(d, (bx, by), (nx, ny), t, 1, CYAN, a)
        node(d, nx, ny, lbl, RED, a)


def s2_tired(d, t, dur):
    p = t / dur
    cam = cam_lerp((0, -280, 0.85), (0, -260, 1.0), p)
    hud_room(d, t)
    d.rounded_rectangle(cam.box(-300, -230, 300, -60), int(cam.s(40)), fill=(50, 50, 70, 255))
    bx, by = person(d, cam, t, 0.05, mode="sit")
    for i, (lbl, (x, y)) in enumerate(DRAINS):
        nx, ny = cam.p(x, y)
        cable(d, (bx, by), (nx, ny), t, 1, CYAN, 0.8)
        node(d, nx, ny, lbl, RED)
    # HUD readout
    d.text((80, H - 160), f"SCREEN TIME: {int(6 + 4 * p)}H {int(t * 20) % 60:02d}M", font=font(34), fill=col(RED, 0.8), anchor="lm")
    d.text((80, H - 110), "THINGS FINISHED: 0", font=font(34), fill=col(RED, 0.8), anchor="lm")
    top_caption(d, ["YOU'RE NOT ALWAYS", "TIRED OF WORKING."], t, dur, accent={"TIRED"})


def s3_sometimes(d, t, dur):
    p = t / dur
    # one by one, the cables are pulled out
    cam = Cam(0, -280, 1.0)
    hud_room(d, t)
    d.rounded_rectangle(cam.box(-300, -230, 300, -60), int(cam.s(40)), fill=(50, 50, 70, 255))
    bx, by = person(d, cam, t, 0.05, mode="sit", head_down=0.0)
    for i, (lbl, (x, y)) in enumerate(DRAINS):
        nx, ny = cam.p(x, y)
        cut = ramp(p, 0.1 + i * 0.2, 0.15)
        if cut < 1:
            cable(d, (lerp(bx, nx, cut * 0.5), lerp(by, ny, cut * 0.5) + cut * 200), (nx, ny), t, 1, CYAN, 1 - cut)
        node(d, nx, ny, lbl, RED, 1 - 0.7 * cut)
        if 0 < cut < 0.4:
            particles(d, bx, by, 120, cut / 0.4, CYAN, n=10, seed=i, rise=0.3)
    top_caption(d, ["SOMETIMES…"], t, dur, accent={"SOMETIMES…"})


def s4_wrong(d, t, dur):
    p = t / dur
    # plug into what matters: meaningful work, rest, focused effort — the battery refills in their colours
    cam = cam_lerp((0, -280, 1.0), (0, -320, 0.8), sstep(p))
    hud_room(d, t)
    level = lerp(0.05, 1.0, sstep(ramp(p, 0.15, 0.75)))
    bx, by = person(d, cam, t, level, mode="stand" if p > 0.35 else "sit", head_down=0.0, mouth=0.6 * level)
    for i, (lbl, (x, y), c) in enumerate(CHARGERS):
        nx, ny = cam.p(x, y)
        a = ramp(p, 0.1 + i * 0.15, 0.2)
        cable(d, (nx, ny), (bx, by), t, 1, c, a)
        node(d, nx, ny, lbl, c, a)
    top_caption(d, ["YOU'RE TIRED OF WORKING", "ON THE WRONG THINGS."], t, dur, accent={"WRONG"})


def s5_end(d, t, dur):
    cam = Cam(0, -320, 0.8)
    hud_room(d, t)
    bx, by = person(d, cam, t, 1.0, mode="stand", head_down=0.0, mouth=0.6)
    for i, (lbl, (x, y), c) in enumerate(CHARGERS):
        nx, ny = cam.p(x, y)
        cable(d, (nx, ny), (bx, by), t, 1, c, 0.6)
        node(d, nx, ny, lbl, c, 0.6)
    stage_end(d, t, dur, ["CHARGE ON", "WHAT MATTERS."], [WHITE, GREEN], size=110, dim=0.5, glow_col=GREEN)


SCENES = [s0_hook, s1_drain, s2_tired, s3_sometimes, s4_wrong, s5_end, s_follow]
