"""THE FACTORY THAT NEVER SLEEPS — potential as a silent factory that only runs when someone runs it.

World: a cavernous factory hall in dark teal steel with amber work lights: trusses, a generator with a huge lever,
a tool wall, gears, a press, a furnace and a long conveyor. POTENTIAL is a towering translucent blue presence,
DISTRACTION a magenta figure with a glowing screen, PROCRASTINATION a rust figure with a calendar, WORK an amber
worker in a hard hat. The film ends outside, on the whole complex lit up at night.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline, pill
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, stars, figure, beam,
                   top_caption, final_card, shake, dust, darkness, word_reveal)
from kit import s_follow

TITLE = ("THE FACTORY", "THAT NEVER SLEEPS")
OUTPUT = "96_The_Factory_That_Never_Sleeps_16x9.mp4"
FOLLOW_SUB = ("FOR IDEAS, LESSONS, AND PERSPECTIVES", "THAT CHALLENGE THE WAY YOU THINK.")

LINES = [
    "Some people spend their entire lives…",
    "…inside a factory that never produces anything.",
    "You have the tools.",
    "You have the ability to learn.",
    "You have the opportunity to begin.",
    "But potential without action…",
    "…is just unused equipment.",
    "",
    "Your future doesn't build itself.",
    "Stop admiring what you could become.",
    "Start producing it.",
    "Your potential is useless without execution.",
    "",
]
SPOKEN = [l.lstrip("…") for l in LINES]
GAPS = {0: 0.4, 1: 1.0, 2: 0.7, 3: 0.7, 4: 1.0, 5: 0.4, 6: 1.0, 7: 0.3, 8: 2.4, 9: 1.2, 10: 1.6, 11: 1.6}

STEEL = (30, 52, 60, 255)
STEEL_L = (70, 110, 120, 255)
AMBER = (255, 180, 80, 255)
POT = (90, 140, 255, 255)
DIS = (255, 70, 200, 255)
PRO = (230, 120, 80, 255)
WORK = (255, 190, 90, 255)
YOU = (225, 228, 232, 255)
CH = 170

LAMPS = [-1500 + i * 420 for i in range(11)]
GEN_X = -1250
LEVER = (GEN_X + 230, -260)


def hall(d, cam, t, power=0.0, lamps_on=0.0, flicker=False, belt=0.0, gears=0.0, press=0.0, furnace=0.0, products=0.0, light=1.0):
    """power 0..1 overall; the others 0..1 per machine (running speed / on)."""
    draw_sky(d, mix((4, 8, 10, 255), (14, 18, 20, 255), power), mix((10, 18, 22, 255), (40, 34, 28, 255), power))
    # back wall panels and tall windows
    for k in range(-6, 9):
        x0 = k * 420 - 200
        a, b = cam.p(x0, -1250), cam.p(x0 + 400, 0)
        d.rectangle([a[0], a[1], b[0], b[1]], outline=(18, 32, 38, 255), width=max(1, int(cam.s(4))))
        wa, wb = cam.p(x0 + 120, -1150), cam.p(x0 + 280, -700)
        d.rectangle([wa[0], wa[1], wb[0], wb[1]], fill=col(mix((20, 40, 60, 255), (60, 50, 40, 255), power), 1))
        for j in range(1, 3):
            yy = lerp(wa[1], wb[1], j / 3)
            d.line([(wa[0], yy), (wb[0], yy)], fill=(10, 20, 26, 255), width=max(1, int(cam.s(4))))
    # roof trusses
    y_t, y_b = -1350, -1220
    polyline(d, [cam.p(-2400, y_t), cam.p(3200, y_t)], 1, col(STEEL_L, light), max(2, int(cam.s(10))))
    polyline(d, [cam.p(-2400, y_b), cam.p(3200, y_b)], 1, col(STEEL_L, light), max(2, int(cam.s(8))))
    for k in range(-24, 32):
        x = k * 100
        polyline(d, [cam.p(x, y_t), cam.p(x + 100, y_b)], 1, col(STEEL_L, 0.7 * light), max(1, int(cam.s(5))))
    # catwalk
    cy = -700
    d.rectangle(cam.box(-300, cy - 20, 2400, cy), fill=col(STEEL, light))
    for k in range(0, 28):
        x = -300 + k * 100
        d.line([cam.p(x, cy - 20), cam.p(x, cy - 110)], fill=col(STEEL_L, 0.6 * light), width=max(1, int(cam.s(4))))
    d.line([cam.p(-300, cy - 110), cam.p(2400, cy - 110)], fill=col(STEEL_L, 0.8 * light), width=max(1, int(cam.s(5))))
    # floor
    fy = cam.p(0, 0)[1]
    if fy < H: d.rectangle([0, fy, W, H], fill=col(mix((12, 20, 24, 255), (36, 32, 28, 255), power), 1))
    d.line([(0, fy), (W, fy)], fill=col(STEEL_L, 0.6), width=max(1, int(cam.s(4))))
    for k in range(-30, 40):  # hazard stripes at the floor edge of the machine zone
        x = k * 80
        if k % 2 == 0:
            d.polygon([cam.p(x, 6), cam.p(x + 40, 6), cam.p(x + 60, 26), cam.p(x + 20, 26)], fill=col((200, 160, 40, 255), 0.35 + 0.4 * power))
    generator(d, cam, t, power)
    toolwall(d, cam, t, power)
    conveyor(d, cam, t, belt, products)
    gear(d, cam, 380, -420, 170, t * 1.6 * gears, gears)
    gear(d, cam, 600, -560, 110, -t * 2.5 * gears + 0.3, gears)
    gear(d, cam, 980, -430, 140, t * 1.9 * gears, gears)
    presser(d, cam, t, press)
    furnace_(d, cam, t, furnace)
    # hanging lamps
    for i, lx in enumerate(LAMPS):
        on = clamp(lamps_on * len(LAMPS) - i)
        if flicker and i == 3:
            on = max(on, 0.9 if math.sin(t * 23) + math.sin(t * 7.3) > 0.6 else 0.08)
        top, bulb = cam.p(lx, -1220), cam.p(lx, -980)
        d.line([top, bulb], fill=col(STEEL_L, 0.8), width=max(1, int(cam.s(3))))
        d.polygon([cam.p(lx - 60, -960), cam.p(lx - 25, -1000), cam.p(lx + 25, -1000), cam.p(lx + 60, -960)], fill=col(STEEL_L, 1))
        d.ellipse(cam.box(lx - 18, -975, lx + 18, -945), fill=col(mix((40, 40, 40, 255), (255, 230, 170, 255), on), 1))
        if on > 0.05:
            glow(d, *cam.p(lx, -950), cam.s(260), AMBER, 0.7 * on)
            beam(d, *cam.p(lx, -960), cam.p(lx - 380, 0)[0], cam.p(lx + 380, 0)[0], fy, AMBER, 0.06 * on, cam.s(50))
    fog(d, *cam.p(500, -200), cam.s(5000), 0.10 + 0.08 * power, (150, 200, 210))


def generator(d, cam, t, power):
    x0, x1 = GEN_X - 200, GEN_X + 200
    d.rounded_rectangle(cam.box(x0, -600, x1, 0), int(cam.s(30)), fill=col(STEEL, 1), outline=col(STEEL_L, 1), width=max(2, int(cam.s(6))))
    for k in range(5):  # cooling fins
        yy = -520 + k * 70
        d.line([cam.p(x0 + 40, yy), cam.p(x1 - 40, yy)], fill=col(STEEL_L, 0.5), width=max(1, int(cam.s(6))))
    # dial
    cx, cy = cam.p(GEN_X, -470)
    r = cam.s(60)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(10, 16, 18, 255), outline=col(STEEL_L, 1), width=max(2, int(cam.s(5))))
    ang = math.radians(200 + 140 * power + 3 * math.sin(t * 20) * power)
    d.line([(cx, cy), (cx + math.cos(ang) * r * 0.8, cy + math.sin(ang) * r * 0.8)], fill=col(AMBER if power > 0.5 else (200, 80, 80, 255), 1), width=max(2, int(cam.s(6))))
    # status light
    sx, sy = cam.p(GEN_X, -320)
    c = (80, 255, 140, 255) if power > 0.5 else (255, 60, 60, 255)
    d.ellipse([sx - cam.s(18), sy - cam.s(18), sx + cam.s(18), sy + cam.s(18)], fill=col(c, 0.4 + 0.6 * (0.5 + 0.5 * math.sin(t * 6))))
    glow(d, sx, sy, cam.s(80), c, 0.5)
    d.text(cam.p(GEN_X, -160), "MAIN POWER", font=font(max(10, int(cam.s(30)))), fill=col(STEEL_L, 1), anchor="mm")


def lever(d, cam, up):
    """up: 0 = down (off) .. 1 = up (on). returns handle point."""
    px, py = cam.p(*LEVER)
    d.rounded_rectangle([px - cam.s(30), py - cam.s(40), px + cam.s(30), py + cam.s(40)], int(cam.s(10)), fill=col(STEEL_L, 1))
    ang = math.radians(lerp(60, -60, up)) - math.pi / 2
    L = cam.s(220)
    hx, hy = px + math.cos(ang) * L, py + math.sin(ang) * L
    d.line([(px, py), (hx, hy)], fill=col((180, 190, 200, 255), 1), width=max(2, int(cam.s(14))))
    d.ellipse([hx - cam.s(28), hy - cam.s(28), hx + cam.s(28), hy + cam.s(28)], fill=col((220, 50, 50, 255), 1))
    return hx, hy


def toolwall(d, cam, t, power):
    x0, x1 = -820, -470
    d.rectangle(cam.box(x0, -620, x1, -180), fill=(16, 28, 32, 255), outline=col(STEEL_L, 0.8), width=max(1, int(cam.s(4))))
    for i in range(6):
        for j in range(4):
            x, y = x0 + 40 + i * 52, -580 + j * 100
            d.ellipse(cam.box(x - 3, y - 3, x + 3, y + 3), fill=col(STEEL_L, 0.6))
    tc = col(mix((150, 160, 170, 255), (255, 230, 190, 255), power), 1)
    w = max(2, int(cam.s(8)))
    # wrench, hammer, screwdriver, saw, pliers silhouettes
    polyline(d, [cam.p(-780, -560), cam.p(-780, -380)], 1, tc, w)
    d.arc(cam.box(-805, -600, -755, -550), 200, 340, fill=tc, width=w)
    polyline(d, [cam.p(-700, -570), cam.p(-700, -380)], 1, tc, w)
    d.rectangle(cam.box(-735, -590, -665, -555), fill=tc)
    polyline(d, [cam.p(-620, -580), cam.p(-620, -430)], 1, tc, max(1, w // 2))
    d.rectangle(cam.box(-632, -430, -608, -370), fill=tc)
    d.polygon([cam.p(-570, -590), cam.p(-510, -590), cam.p(-510, -380), cam.p(-540, -360)], outline=tc, width=max(1, w // 2))


def conveyor(d, cam, t, belt, products):
    x0, x1, y = -350, 2500, -150
    d.rounded_rectangle(cam.box(x0, y - 40, x1, y + 20), int(cam.s(30)), fill=col(STEEL, 1), outline=col(STEEL_L, 1), width=max(2, int(cam.s(5))))
    off = (t * 160 * belt) % 80
    for k in range(int((x1 - x0) / 80)):
        x = x0 + 30 + k * 80 + off
        if x < x1 - 30:
            d.line([cam.p(x, y - 38), cam.p(x, y + 18)], fill=col(STEEL_L, 0.6), width=max(1, int(cam.s(3))))
    for k in range(0, int((x1 - x0) / 300) + 1):
        lx = x0 + 100 + k * 300
        d.line([cam.p(lx, y + 20), cam.p(lx, 0)], fill=col(STEEL_L, 0.8), width=max(1, int(cam.s(8))))
    # boxes / products riding the belt
    for k in range(14):
        px = x0 + 80 + ((k * 210 + t * 160 * belt) % (x1 - x0 - 160))
        made = px > 1500  # out of the press: glowing finished products
        if products <= 0 and k % 3:
            continue
        if made and products > 0:
            sx, sy = cam.p(px, y - 90)
            glow(d, sx, sy, cam.s(90), AMBER, 0.5 * products)
            d.regular_polygon((sx, sy, cam.s(40)), 6, rotation=t * 60 * belt, fill=col((255, 215, 140, 255), products))
        else:
            d.rectangle(cam.box(px - 45, y - 130, px + 45, y - 40), fill=col((110, 84, 60, 255), 0.9), outline=col((150, 120, 90, 255), 1), width=max(1, int(cam.s(3))))


def gear(d, cam, x, y, r, rot, on):
    cx, cy = cam.p(x, y)
    rr = cam.s(r)
    n = 12
    pts = []
    for i in range(n * 2):
        a = rot + i * math.pi / n
        R = rr if i % 2 == 0 else rr * 0.82
        pts.append((cx + math.cos(a) * R, cy + math.sin(a) * R))
    c = mix(STEEL_L, AMBER, on * 0.7)
    d.polygon(pts, fill=col(STEEL, 1), outline=col(c, 1))
    polyline(d, pts + [pts[0]], 1, col(c, 1), max(1, int(cam.s(5))))
    d.ellipse([cx - rr * 0.3, cy - rr * 0.3, cx + rr * 0.3, cy + rr * 0.3], outline=col(c, 1), width=max(1, int(cam.s(6))))
    for k in range(4):
        a = rot + k * math.pi / 2
        d.line([(cx + math.cos(a) * rr * 0.3, cy + math.sin(a) * rr * 0.3), (cx + math.cos(a) * rr * 0.7, cy + math.sin(a) * rr * 0.7)], fill=col(c, 1), width=max(1, int(cam.s(6))))


def presser(d, cam, t, on):
    x = 1450
    d.rectangle(cam.box(x - 170, -760, x + 170, -620), fill=col(STEEL, 1), outline=col(STEEL_L, 1), width=max(2, int(cam.s(5))))
    for s in (-1, 1):
        d.rectangle(cam.box(x + s * 150 - 15, -620, x + s * 150 + 15, -150), fill=col(STEEL_L, 1))
    k = abs(math.sin(t * 3)) if on > 0 else 0.0
    yb = lerp(-600, -230, k ** 3 * on)
    d.rectangle(cam.box(x - 30, -620, x + 30, yb - 40), fill=col((150, 160, 170, 255), 1))
    d.rectangle(cam.box(x - 120, yb - 40, x + 120, yb), fill=col(mix(STEEL_L, AMBER, on), 1))
    if on > 0 and k > 0.97:
        for j in range(10):
            a = j * 0.6
            sx, sy = cam.p(x + math.cos(a) * 140, -190)
            d.line([(sx, sy), (sx + math.cos(a) * cam.s(60), sy - abs(math.sin(a)) * cam.s(60))], fill=col(AMBER, 0.9), width=2)


def furnace_(d, cam, t, on):
    x = 2050
    d.rounded_rectangle(cam.box(x - 220, -560, x + 220, -160), int(cam.s(40)), fill=col(STEEL, 1), outline=col(STEEL_L, 1), width=max(2, int(cam.s(5))))
    m0, m1 = cam.p(x - 120, -440), cam.p(x + 120, -240)
    d.rounded_rectangle([m0[0], m0[1], m1[0], m1[1]], int(cam.s(30)), fill=col(mix((20, 14, 12, 255), (255, 140, 60, 255), on * (0.85 + 0.15 * math.sin(t * 9))), 1))
    if on > 0:
        glow(d, (m0[0] + m1[0]) / 2, (m0[1] + m1[1]) / 2, cam.s(380), (255, 120, 50), 0.6 * on)
    d.rectangle(cam.box(x - 60, -1250, x + 60, -560), fill=col(STEEL, 1), outline=col(STEEL_L, 0.7), width=max(1, int(cam.s(4))))


def potential(d, cam, x, t, a=1.0, name_a=1.0):
    fx, fy = cam.p(x, 0)
    glow(d, fx, fy - cam.s(300), cam.s(500), POT, 0.4 * a)
    figure(d, fx, fy, cam.s(560), POT, mode="stand", phase=0, a=0.55 * a, name="POTENTIAL", name_a=name_a, look=0.3,
           eye_col=(200, 230, 255, 255), bodyw=1.1)


def screen_prop(d, fh, bh, h, a):
    if fh:
        x, y = fh
        d.rounded_rectangle([x - h * 0.05, y - h * 0.09, x + h * 0.05, y + h * 0.05], int(h * 0.015), fill=col((255, 160, 230, 255), a))
        glow(d, x, y, h * 0.6, DIS, 0.7 * a)


def cal_prop(d, fh, bh, h, a):
    if fh:
        x, y = fh
        w, hh = h * 0.32, h * 0.34
        d.rounded_rectangle([x, y - hh, x + w, y], int(h * 0.02), fill=col((245, 238, 225, 255), a))
        d.rectangle([x, y - hh, x + w, y - hh + h * 0.07], fill=col(PRO, a))
        d.text((x + w / 2, y - hh / 2 + h * 0.03), "TOMORROW", font=font(max(8, int(h * 0.045))), fill=(40, 30, 40, int(255 * a)), anchor="mm")


# ---------------------------------------------------------------- scenes
def s0_lives(d, t, dur):
    p = t / dur
    # hook: one flickering bulb in a dead factory; a slow dolly along the silent line
    cam = cam_lerp((-300, -500, 0.75), (300, -520, 0.6), p)
    hall(d, cam, t, flicker=True)
    dust(d, t, 0.5, n=50, color=(200, 220, 230))
    darkness(d, W / 2, H / 2, 0.55)
    top_caption(d, ["SOME PEOPLE SPEND", "THEIR ENTIRE LIVES…"], t, dur, accent={"ENTIRE", "LIVES…"})


def s1_never(d, t, dur):
    p = t / dur
    cam = cam_lerp((300, -520, 0.6), (700, -620, 0.42), sstep(p))
    hall(d, cam, t, flicker=True)
    dust(d, t, 0.5, n=50, color=(200, 220, 230))
    darkness(d, W / 2, H / 2, 0.45)
    top_caption(d, ["…INSIDE A FACTORY THAT", "NEVER PRODUCES ANYTHING."], t, dur, accent={"NEVER", "ANYTHING."})
s1_never.seamless = True


def s2_tools(d, t, dur):
    p = t / dur
    cam = cam_lerp((-650, -400, 1.3), (-640, -410, 1.45), p)
    hall(d, cam, t, flicker=True, power=0.15)
    sx, sy = cam.p(-650, -420)
    glow(d, sx, sy, cam.s(420), (200, 230, 255), 0.5 * ramp(t, 0.1, 0.5))
    darkness(d, sx, sy, 0.5)
    top_caption(d, ["YOU HAVE THE TOOLS."], t, dur, accent={"TOOLS."})


def s3_learn(d, t, dur):
    p = t / dur
    # Potential: a towering, idle presence beside the machines; a blueprint draws itself
    cam = cam_lerp((150, -450, 0.62), (230, -470, 0.58), p)
    hall(d, cam, t, flicker=True, power=0.15)
    potential(d, cam, -120, t, a=ramp(t, 0.0, 0.6))
    bx0, by0 = cam.p(560, -1000)
    bx1, by1 = cam.p(1100, -750)
    k = ramp(t, 0.2, dur * 0.7)
    d.rectangle([bx0, by0, bx1, by1], fill=col((20, 50, 110, 255), 0.85 * ramp(t, 0.1, 0.3)), outline=col(POT, ramp(t, 0.1, 0.3)), width=3)
    lines = [[(0.1, 0.8), (0.1, 0.3), (0.35, 0.3), (0.35, 0.8)], [(0.45, 0.8), (0.55, 0.25), (0.65, 0.8)], [(0.72, 0.5), (0.9, 0.5), (0.9, 0.8), (0.72, 0.8), (0.72, 0.5)]]
    for i, ln in enumerate(lines):
        pts = [(lerp(bx0, bx1, u), lerp(by0, by1, v)) for u, v in ln]
        polyline(d, pts, clamp(k * 3 - i), col((200, 225, 255, 255), 0.9), 3)
    top_caption(d, ["YOU HAVE THE", "ABILITY TO LEARN."], t, dur, accent={"LEARN."})


def s4_begin(d, t, dur):
    p = t / dur
    cam = cam_lerp((-1150, -330, 0.95), (-1080, -330, 1.1), sstep(p))
    hall(d, cam, t, power=0.15)
    lever(d, cam, 0.0)
    hx, hy = cam.p(*LEVER)
    glow(d, hx, hy - cam.s(150), cam.s(380), (255, 230, 200), 0.45 * ramp(t, 0.1, 0.5))
    darkness(d, hx - cam.s(100), hy, 0.5)
    pill(d, hx, hy - cam.s(320), "START", ramp(t, dur * 0.4, 0.4), int(clamp(cam.s(30), 18, 40)), inverted=False)
    top_caption(d, ["YOU HAVE THE", "OPPORTUNITY TO BEGIN."], t, dur, accent={"BEGIN."})


def s5_without(d, t, dur):
    p = t / dur
    # Distraction walks the line switching things off, and leads the person away toward a glowing screen
    cam = cam_lerp((150, -280, 0.95), (-450, -260, 1.0), sstep(p))
    lamps = 0.6 * (1 - ramp(t, 0.1, dur * 0.8))
    hall(d, cam, t, power=0.3 * (1 - p), lamps_on=lamps, belt=0.0)
    dx = lerp(400, -700, sstep(p))
    fx, fy = cam.p(dx, 0)
    figure(d, fx, fy, cam.s(CH), DIS, mode="phone", face=-1, prop=screen_prop, name="DISTRACTION", acc=("hair",), mouth=0.6)
    px = dx + 220
    gx, gy = cam.p(px, 0)
    figure(d, gx, gy, cam.s(CH), YOU, mode="walk", phase=t * 4, face=-1, acc=("hair",), look=-0.2, hands=None)
    top_caption(d, ["BUT POTENTIAL", "WITHOUT ACTION…"], t, dur, accent={"WITHOUT", "ACTION…"})


def s6_unused(d, t, dur):
    p = t / dur
    cam = cam_lerp((-560, -300, 0.95), (-600, -290, 1.05), sstep(p))
    hall(d, cam, t, power=0.0, lamps_on=0.0)
    # the person, slumped on a crate in front of a glowing screen; cobwebs form on the tools
    sx, sy = cam.p(-900, -250)
    d.rounded_rectangle([sx - cam.s(150), sy - cam.s(100), sx + cam.s(150), sy + cam.s(80)], int(cam.s(14)), fill=col((60, 20, 60, 255), 1), outline=col(DIS, 1), width=3)
    glow(d, sx, sy, cam.s(500), DIS, 0.6 + 0.1 * math.sin(t * 9))
    cx, cy = cam.p(-560, 0)
    d.rectangle([cx - cam.s(70), cy - cam.s(60), cx + cam.s(70), cy], fill=col((90, 70, 50, 255), 1))
    figure(d, cx, cy - cam.s(18), cam.s(CH), YOU, mode="sit", face=-1, acc=("hair",), head_down=0.2)
    fx, fy = cam.p(-300, 0)
    figure(d, fx, fy, cam.s(CH), DIS, mode="stand", face=-1, prop=None, name="DISTRACTION", name_a=0.7, acc=("hair",), mouth=0.6)
    web = ramp(t, 0.2, dur * 0.7)
    wx, wy = cam.p(-470, -620)
    for k in range(5):
        a = math.radians(90 + k * 20)
        polyline(d, [(wx, wy), (wx - math.cos(a) * cam.s(120), wy + math.sin(a) * cam.s(120))], web, col(WHITE, 0.4), 1)
    darkness(d, W / 2, H / 2, 0.5)
    top_caption(d, ["…IS JUST", "UNUSED EQUIPMENT."], t, dur, accent={"UNUSED"})
s6_unused.seamless = True


def s7_procrastination(d, t, dur):
    p = t / dur
    # silent beat: Procrastination pulls the main lever down. Everything dies.
    cam = cam_lerp((-1150, -330, 0.9), (-1150, -330, 1.0), p)
    off = sstep(ramp(t, dur * 0.35, 0.5))
    hall(d, cam, t, power=0.12 * (1 - off), lamps_on=0.15 * (1 - off))
    up = 0.6 * (1 - off)
    hall_lever = lever(d, cam, up)
    fx, fy = cam.p(LEVER[0] + 140, 0)
    figure(d, fx, fy, cam.s(CH * 1.05), PRO, mode="stand", face=-1, name="PROCRASTINATION", acc=("hair",),
           hands=(hall_lever, (fx - cam.s(30), fy - cam.s(CH * 0.35))), prop=None)
    cx, cy = cam.p(LEVER[0] + 380, -360)
    k = ramp(t, dur * 0.55, 0.4)
    d.rounded_rectangle([cx - cam.s(130), cy - cam.s(150), cx + cam.s(130), cy + cam.s(110)], int(cam.s(14)), fill=col((245, 238, 225, 255), k))
    d.rectangle([cx - cam.s(130), cy - cam.s(150), cx + cam.s(130), cy - cam.s(100)], fill=col(PRO, k))
    d.text((cx, cy), "TOMORROW", font=font(int(cam.s(40))), fill=(40, 30, 40, int(255 * k)), anchor="mm")
    darkness(d, W / 2, H / 2, 0.4 + 0.5 * off)


def s8_future(d, t, dur):
    p = t / dur
    # Work arrives and throws the lever: machine after machine wakes up
    on = sstep(ramp(t, dur * 0.3, 0.5))
    cam = cam_lerp((-1150, -330, 0.9), (-200, -560, 0.5), sstep(ramp(t, dur * 0.45, dur * 0.55)))
    seq = ramp(t, dur * 0.4, dur * 0.6)
    hall(d, cam, t, power=0.12 + 0.88 * seq, lamps_on=seq, belt=clamp(seq * 4 - 1), gears=clamp(seq * 4 - 1.5),
         press=clamp(seq * 4 - 2), furnace=clamp(seq * 4 - 2.5), products=clamp(seq * 4 - 3))
    hl = lever(d, cam, on)
    walk = sstep(ramp(t, 0, dur * 0.3))
    fx, fy = cam.p(lerp(LEVER[0] + 500, LEVER[0] + 130, walk), 0)
    hands = (hl, hl) if walk >= 1 else None
    figure(d, fx, fy, cam.s(CH * 1.05), WORK, mode="walk" if walk < 1 else "stand", phase=walk * 8, face=-1, name="WORK",
           acc=("cap",), hands=hands)
    glow(d, fx, fy - cam.s(90), cam.s(240), WORK, 0.4)
    top_caption(d, ["YOUR FUTURE DOESN'T", "BUILD ITSELF."], t, dur, accent={"BUILD", "ITSELF."})


def exterior(d, t, k, glowk=1.0):
    """The whole complex at night, seen from outside. k: pull-back progress."""
    cam = Cam(0, -500, lerp(0.75, 0.42, k))
    draw_sky(d, (4, 8, 18, 255), (30, 34, 50, 255))
    stars(d, 0.8, seed=31, n=90, ymax=0.5)
    fy = cam.p(0, 0)[1]
    if fy < H: d.rectangle([0, fy, W, H], fill=(10, 12, 16, 255))
    r = random.Random(5)
    blocks = [(-2600, 600, 500), (-1950, 900, 700), (-1000, 1400, 900), (450, 1000, 650), (1500, 800, 550), (2350, 700, 450)]
    for i, (x, w, hgt) in enumerate(blocks):
        a, b = cam.p(x, -hgt), cam.p(x + w, 0)
        d.rectangle([a[0], a[1], b[0], b[1]], fill=(20, 30, 36, 255))
        teeth = int(w / 150)
        for j in range(teeth):  # sawtooth roof
            p0 = cam.p(x + j * 150, -hgt)
            p1 = cam.p(x + j * 150, -hgt - 90)
            p2 = cam.p(x + (j + 1) * 150, -hgt)
            d.polygon([p0, p1, p2], fill=(20, 30, 36, 255))
            tpoly(d, [p1, p2, p0], col(AMBER, 0.35 * glowk))
        for row in range(int(hgt / 120)):
            for c in range(int(w / 90)):
                if r.random() < 0.85:
                    wx, wy = x + 30 + c * 90, -80 - row * 120
                    d.rectangle(cam.box(wx, wy - 50, wx + 45, wy), fill=col(AMBER, glowk * (0.75 + 0.25 * r.random())))
        glow(d, (a[0] + b[0]) / 2, (a[1] + b[1]) / 2, cam.s(w * 0.9), AMBER, 0.35 * glowk)
    for i, x in enumerate((-1700, -400, 900, 2000)):  # chimneys and steam
        a, b = cam.p(x, -1500), cam.p(x + 90, 0)
        d.rectangle([a[0], a[1], b[0], b[1]], fill=(26, 34, 40, 255))
        d.rectangle([a[0], a[1], b[0], a[1] + cam.s(30)], fill=col((200, 70, 60, 255), 1))
        for j in range(6):
            u = (t * 0.25 + j / 6 + i * 0.13) % 1
            sx, sy = cam.p(x + 45 + u * 300, -1520 - u * 700)
            rr = cam.s(60 + 160 * u)
            tpoly(d, [(sx - rr, sy - rr), (sx + rr, sy + rr)], col((200, 210, 220, 255), 0.25 * (1 - u)), kind="ellipse")
    return cam


def s9_admiring(d, t, dur):
    p = t / dur
    if p < 0.45:  # inside, full production
        u = p / 0.45
        cam = cam_lerp((600, -560, 0.55), (900, -620, 0.45), u)
        hall(d, cam, t, power=1, lamps_on=1, belt=1, gears=1, press=1, furnace=1, products=1)
        dust(d, t, 0.8, n=70, color=(255, 210, 150), rise=40)
        overlay(d, (0, 0, 0), sstep(ramp(u, 0.85, 0.15)))
    else:
        exterior(d, t, sstep((p - 0.45) / 0.55))
        overlay(d, (0, 0, 0), 1 - ramp(p, 0.45, 0.08))
    top_caption(d, ["STOP ADMIRING WHAT", "YOU COULD BECOME."], t, dur, accent={"ADMIRING", "BECOME."})


def s10_producing(d, t, dur):
    p = t / dur
    exterior(d, t + 5, 1.0 + 0.0 * p)
    top_caption(d, ["START PRODUCING IT."], t, dur, accent={"PRODUCING"})


def s11_final(d, t, dur):
    exterior(d, t + 8, 1.0)
    overlay(d, (0, 0, 0), 0.6)
    final_card(d, t, dur, ["YOUR POTENTIAL IS USELESS", "WITHOUT EXECUTION."], [WHITE, AMBER], size=96, glow_col=AMBER)


SCENES = [s0_lives, s1_never, s2_tools, s3_learn, s4_begin, s5_without, s6_unused, s7_procrastination, s8_future,
          s9_admiring, s10_producing, s11_final, s_follow]
