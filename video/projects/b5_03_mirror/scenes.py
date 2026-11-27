"""THE MIRROR OF POTENTIAL — a reflection that is everything you could be, and that cannot come out.

World: a dark violet room, one tall arched mirror in a silver frame. THE PRESENT SELF is a muted grey figure;
THE POTENTIAL SELF in the glass is the same silhouette in warm gold light, upright, practising, building.
The glass cracks under a touch; the reflection fades; the person turns and starts doing the work, and the gold
light moves onto them.
"""
import math
import random
from PIL import Image, ImageDraw
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, dust)
from kit import s_follow

TITLE = ("THE MIRROR", "OF POTENTIAL")
OUTPUT = "103_The_Mirror_Of_Potential_16x9.mp4"
LINES = [
    "",
    "You keep looking at who you could become.",
    "",
    "At some point…",
    "You have to become them.",
    "",
    "",
]
SILENT = {0: 3.0, 2: 3.0, 5: 3.4}
GAPS = {1: 2.6, 3: 0.8, 4: 3.6}

ROOM = (16, 10, 26, 255)
SILVER = (200, 205, 225, 255)
PRESENT = (150, 150, 160, 255)
GOLD = (255, 205, 120, 255)
CH = 300
MX, MW, MH = 300, 520, 1000   # mirror: left edge x, width, height (bottom at floor)


def room(d, cam, t, light=1.0):
    draw_sky(d, (6, 4, 10, 255), (22, 14, 34, 255))
    fy = cam.p(0, 0)[1]
    if fy < H:
        d.rectangle([0, fy, W, H], fill=(14, 10, 20, 255))
    for k in range(-8, 10):  # wall panels
        x = k * 320
        d.rectangle(cam.box(x + 20, -1300, x + 300, -40), outline=col((40, 26, 56, 255), light), width=max(1, int(cam.s(4))))
    fog(d, *cam.p(MX + MW / 2, -200), cam.s(3000), 0.12, (180, 150, 220))


def mirror_shape(cx, top, bot, w):
    """Arched mirror outline in screen coordinates."""
    pts = [(cx - w / 2, bot), (cx - w / 2, top + w / 2)]
    for i in range(21):
        a = math.pi + i * math.pi / 20
        pts.append((cx + math.cos(a) * w / 2, top + w / 2 + math.sin(a) * w / 2))
    pts += [(cx + w / 2, bot)]
    return pts


def mirror(d, cam, t, draw_inside, crack=0.0, gone=0.0, glowk=1.0):
    """Frame + glass. draw_inside(dd, cam) draws the reflection (clipped to the glass)."""
    cx = cam.p(MX + MW / 2, 0)[0]
    top, bot = cam.p(0, -MH)[1], cam.p(0, -30)[1]
    w = cam.s(MW)
    shape = mirror_shape(cx, top, bot, w)
    glow(d, cx, (top + bot) / 2, w * 1.1, SILVER, 0.25 * glowk)
    outer = mirror_shape(cx, top - cam.s(40), bot, w + cam.s(80))
    d.polygon(outer, fill=col((120, 110, 140, 255), 1))
    polyline(d, outer + [outer[0]], 1, col(SILVER, 1), max(2, int(cam.s(8))))
    d.polygon(shape, fill=col((34, 24, 50, 255), 1))
    if gone < 1:  # reflection, clipped to the glass
        x0, y0 = int(cx - w / 2), int(top)
        lay = Image.new("RGBA", (int(w) + 2, int(bot - top) + 2))
        ld = ImageDraw.Draw(lay)
        ld._image = lay
        draw_inside(ld, x0, y0)
        mask = Image.new("L", lay.size, 0)
        ImageDraw.Draw(mask).polygon([(p[0] - x0, p[1] - y0) for p in shape], fill=int(255 * (1 - gone)))
        lay.putalpha(Image.composite(lay.getchannel("A"), Image.new("L", lay.size, 0), mask))
        d._image.alpha_composite(lay, (max(0, x0), max(0, y0)), (max(0, -x0), max(0, -y0)))
    # glass sheen
    tpoly(d, [(cx - w * 0.35, top + w * 0.3), (cx - w * 0.2, top + w * 0.25), (cx - w * 0.45, bot - w * 0.2), (cx - w * 0.5, bot - w * 0.3)], col(WHITE, 0.06))
    if crack > 0:  # cracks spreading from the touch point
        r = random.Random(7)
        ox, oy = cx - w * 0.05, (top + bot) * 0.5
        for i in range(14):
            ang = r.uniform(0, math.tau)
            L = w * r.uniform(0.3, 0.9) * clamp(crack * 1.4 - i * 0.04)
            pts = [(ox, oy)]
            x, y = ox, oy
            for k in range(5):
                ang += r.uniform(-0.5, 0.5)
                x += math.cos(ang) * L / 5
                y += math.sin(ang) * L / 5
                pts.append((x, y))
            polyline(d, pts, 1, col(WHITE, 0.85), 2)
        glow(d, ox, oy, w * 0.3, WHITE, 0.4 * pulse(crack, 0.1, 0.2))


def reflection_fig(dd, x0, y0, cam, t, act, a=1.0):
    """The Potential Self inside the glass."""
    fx = cam.p(MX + MW / 2, 0)[0] - x0
    fy = cam.p(0, -30)[1] - y0
    h = cam.s(CH)
    glow(dd, fx, fy - h * 0.5, h * 0.8, GOLD, 0.45 * a)
    hands = None
    mode = "stand"
    phase = 0
    prop = None
    if act == "stand":
        mode = "stand"
    elif act == "read":
        mode = "stand"
        hands = ((fx - h * 0.18, fy - h * 0.55), (fx - h * 0.1, fy - h * 0.55))
        def prop(d2, fh, bh, hh, aa):
            d2.rectangle([fx - h * 0.24, fy - h * 0.62, fx - h * 0.04, fy - h * 0.5], fill=col((250, 240, 220, 255), aa))
    elif act == "run":
        mode, phase = "run", t * 8
    elif act == "lift":
        mode = "cheer"
    elif act == "build":
        mode, phase = "hammer", t * 6
    figure(dd, fx, fy, h, GOLD, mode=mode, phase=phase, face=-1, acc=("hair",), hands=hands, prop=prop, a=a, eye_col=(90, 60, 10, 255),
           lean=0.2 if act == "run" else 0.0, mouth=0.5)


def present(d, cam, t, x, mode="stand", face=1, color=PRESENT, **kw):
    fx, fy = cam.p(x, -30)
    figure(d, fx, fy, cam.s(CH), color, mode=mode, face=face, acc=("hair",), **kw)
    return fx, fy


def s0_hook(d, t, dur):
    p = t / dur
    # darkness; the mirror's frame lights up; the reflection appears before the person steps into frame
    cam = cam_lerp((MX + MW / 2, -470, 0.95), (MX + 200, -450, 0.8), sstep(p))
    room(d, cam, t)
    lit = ramp(t, 0.3, 1.2)
    mirror(d, cam, t, lambda dd, x0, y0: reflection_fig(dd, x0, y0, cam, t, "stand", ramp(t, 1.2, 0.6)), glowk=lit)
    walk = sstep(ramp(t, 1.6, 1.2))
    present(d, cam, t, lerp(-600, -60, walk), mode="walk" if 0 < walk < 1 else "stand", phase=t * 5, head_down=0.3, swing=0.3)
    darkness(d, W / 2, H / 2, 0.6)
    overlay(d, (0, 0, 0), 1 - lit)


def s1_looking(d, t, dur):
    p = t / dur
    # the reflection starts moving on its own: reading, running, lifting, building
    cam = cam_lerp((MX + 200, -450, 0.8), (MX + 150, -430, 0.88), p)
    room(d, cam, t)
    acts = ["stand", "read", "run", "lift", "build"]
    act = acts[min(4, int(p * 5))]
    mirror(d, cam, t, lambda dd, x0, y0: reflection_fig(dd, x0, y0, cam, t, act))
    present(d, cam, t, -60, look=0.2, head_down=0.1)
    darkness(d, W / 2, H / 2, 0.45)
    top_caption(d, ["YOU KEEP LOOKING AT", "WHO YOU COULD BECOME."], t, dur, accent={"COULD", "BECOME."})


def s2_crack(d, t, dur):
    p = t / dur
    # close: the hand reaches the glass — and the glass cracks
    cam = cam_lerp((MX + 100, -430, 1.0), (MX + 60, -450, 1.25), sstep(p))
    hit = pulse(t, 1.4, 0.1)
    shake(cam, t, 12 * hit)
    room(d, cam, t)
    crack = ramp(t, 1.4, 1.0)
    mirror(d, cam, t, lambda dd, x0, y0: reflection_fig(dd, x0, y0, cam, t, "stand"), crack=crack)
    reach = sstep(ramp(t, 0.2, 1.2))
    fx, fy = cam.p(80, -30)
    hx = lerp(fx + cam.s(60), cam.p(MX + MW * 0.45, 0)[0], reach)
    hy = fy - cam.s(CH * 0.62)
    present(d, cam, t, 80, mode="stand", hands=((fx + cam.s(20), fy - cam.s(CH * 0.35)), (hx, hy)), look=0.0)
    if crack > 0:
        particles(d, hx, hy, cam.s(200), clamp(crack * 1.5), WHITE, n=24, seed=3, rise=0.2)


def s3_point(d, t, dur):
    p = t / dur
    # behind the cracks, the reflection gives one small nod and fades
    cam = cam_lerp((MX + 60, -450, 1.25), (MX + 150, -430, 1.0), sstep(p))
    room(d, cam, t)
    mirror(d, cam, t, lambda dd, x0, y0: reflection_fig(dd, x0, y0, cam, t, "stand", 1.0), crack=1.0, gone=sstep(ramp(t, 0.3, dur * 0.9)))
    present(d, cam, t, 80, look=0.0, head_down=0.2)
    darkness(d, W / 2, H / 2, 0.5)
    top_caption(d, ["AT SOME POINT…"], t, dur, accent={"POINT…"})


def s4_become(d, t, dur):
    p = t / dur
    # the person turns away from the glass and starts: reading, running, building. The gold moves onto them.
    k = sstep(ramp(t, 0.6, dur * 0.8))
    cam = cam_lerp((MX + 150, -430, 1.0), (-200, -470, 0.7), sstep(p))
    room(d, cam, t)
    mirror(d, cam, t, lambda dd, x0, y0: None, crack=1.0, gone=1.0, glowk=0.3)
    acts = ["stand", "read", "run", "build"]
    act = acts[min(3, int(p * 4))]
    c = mix(PRESENT, GOLD, k)
    fx, fy = cam.p(lerp(80, -350, p), -30)
    glow(d, fx, fy - cam.s(CH * 0.5), cam.s(CH) * 0.9, GOLD, 0.5 * k)
    mode = {"stand": "stand", "read": "stand", "run": "run", "build": "hammer"}[act]
    figure(d, fx, fy, cam.s(CH), c, mode=mode, phase=t * 7, face=-1, acc=("hair",), lean=0.2 if act == "run" else 0.0, mouth=0.4 * k,
           hands=((fx - cam.s(50), fy - cam.s(CH * 0.55)), (fx - cam.s(30), fy - cam.s(CH * 0.55))) if act == "read" else None)
    dust(d, t, 0.6 * k, n=60, color=(255, 220, 160))
    top_caption(d, ["YOU HAVE TO", "BECOME THEM."], t, dur, accent={"BECOME", "THEM."})


def s5_end(d, t, dur):
    cam = Cam(-200, -470, 0.7)
    room(d, cam, t)
    mirror(d, cam, t, lambda dd, x0, y0: None, crack=1.0, gone=1.0, glowk=0.3)
    fx, fy = cam.p(-350, -30)
    glow(d, fx, fy - cam.s(CH * 0.5), cam.s(CH) * 0.9, GOLD, 0.6)
    figure(d, fx, fy, cam.s(CH), GOLD, mode="stand", face=1, acc=("hair",), mouth=0.5)
    stage_end(d, t, dur, ["BECOME THEM."], [GOLD], size=130, glow_col=GOLD)


SCENES = [s0_hook, s1_looking, s2_crack, s3_point, s4_become, s5_end, s_follow]
