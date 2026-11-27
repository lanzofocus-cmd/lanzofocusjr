"""THE CANDLE AND THE SUN — a tiny flame that tries to be the sun, then finds its own room to light.

World: macro scale. A small white candle on a windowsill, its flame a living character with two calm eyes.
Outside, a colossal sun rises and floods the sky; the candle strains to match it, flares, sputters and smokes.
Night falls. The candle burns steady again, and its small circle of light turns out to hold a whole world:
a person reading beside it, a cat asleep, a cup of tea.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, light_hole, stars, sun, dust)
from kit import s_follow

TITLE = ("THE CANDLE", "AND THE SUN")
OUTPUT = "120_The_Candle_And_The_Sun_16x9.mp4"
LINES = [
    "",
    "",
    "Don't compare your light…",
    "To someone else's sky.",
    "",
    "",
]
SILENT = {0: 3.2, 1: 4.0, 4: 3.6}
GAPS = {2: 1.6, 3: 5.6}

FLAME = (255, 190, 90, 255)
WAX = (245, 238, 225, 255)
YOU = (230, 220, 205, 255)


def window_scene(d, cam, t, day=0.0, night=0.0, sun_y=None):
    """Interior wall with a big window; outside is the sky."""
    sky_t = mix(mix((4, 6, 16, 255), (90, 150, 230, 255), day), (4, 6, 16, 255), night)
    sky_b = mix(mix((14, 16, 34, 255), (255, 210, 150, 255), day), (14, 16, 34, 255), night)
    d.rectangle([0, 0, W, H], fill=(16, 12, 12, 255))
    wx0, wy0 = cam.p(-900, -1100)
    wx1, wy1 = cam.p(900, -60)
    lay_h = int(max(2, wy1 - wy0))
    from story import sky as _sky
    from PIL import Image
    im = _sky(sky_t, sky_b, h=lay_h).crop((0, 0, int(max(2, wx1 - wx0)), lay_h)) if wx1 - wx0 < W else _sky(sky_t, sky_b, h=lay_h)
    d._image.alpha_composite(im, (int(max(0, wx0)), int(max(0, wy0))), (int(max(0, -wx0)), 0))
    stars(d, (1 - day) * 0.8, seed=4, n=60, ymax=0.5)
    if sun_y is not None:
        sun(d, (wx0 + wx1) / 2 + cam.s(200), sun_y, cam.s(420), 1.0, (255, 220, 140, 255))
    # wall around the window (keeps the sun inside the glass)
    wc = (16, 12, 12, 255)
    for box in ([0, 0, W, wy0], [0, wy1, W, H], [0, 0, wx0, H], [wx1, 0, W, H]):
        x0, y0, x1, y1 = max(0, box[0]), max(0, box[1]), min(W, box[2]), min(H, box[3])
        if x1 > x0 and y1 > y0:
            d.rectangle([x0, y0, x1, y1], fill=wc)
    # window frame
    d.rectangle([wx0, wy0, wx1, wy1], outline=(50, 36, 30, 255), width=max(3, int(cam.s(30))))
    d.line([((wx0 + wx1) / 2, wy0), ((wx0 + wx1) / 2, wy1)], fill=(50, 36, 30, 255), width=max(3, int(cam.s(20))))
    # sill
    d.rectangle(cam.box(-1100, -60, 1100, 20), fill=(80, 56, 40, 255))
    sy = cam.p(0, 20)[1]
    if sy < H:
        d.rectangle([0, sy, W, H], fill=(30, 22, 18, 255))
    return wx0, wy0, wx1, wy1


def candle(d, cam, t, x=0, power=1.0, strain=0.0, sad=0.0, sputter=0.0):
    bx, by = cam.p(x, -60)
    w, h = cam.s(70), cam.s(260)
    d.rounded_rectangle([bx - w, by - h, bx + w, by], int(cam.s(12)), fill=col(WAX, 1))
    d.chord([bx - w, by - h - cam.s(20), bx + w, by - h + cam.s(20)], 0, 180, fill=col(dimc(WAX, 0.92), 1))
    for k in range(3):  # wax drips
        dx = bx - w * 0.6 + k * w * 0.6
        d.rounded_rectangle([dx - cam.s(10), by - h, dx + cam.s(10), by - h + cam.s(40 + 30 * k)], int(cam.s(10)), fill=col(WAX, 1))
    wick = (bx, by - h - cam.s(10))
    d.line([wick, (wick[0], wick[1] - cam.s(20))], fill=(40, 30, 26, 255), width=max(1, int(cam.s(6))))
    flick = 1 + 0.05 * math.sin(t * 13) + 0.04 * math.sin(t * 7.3) + strain * 0.25 * math.sin(t * 31)
    fh = cam.s(120) * power * flick * (1 + strain * 1.2) * (1 - 0.6 * sputter)
    fw = fh * 0.38
    fx, fy = wick[0] + math.sin(t * 5) * cam.s(4), wick[1] - cam.s(16)
    glow(d, fx, fy - fh * 0.5, fh * (3 + strain * 2), FLAME, 0.7 * power)
    pts = [(fx, fy - fh)] + [(fx + math.sin(a) * fw, fy - fh * 0.35 + math.cos(a) * fw * 0.9) for a in [math.pi * 0.5 + k * math.pi / 10 for k in range(11)]]
    pts = [(fx, fy - fh), (fx + fw, fy - fh * 0.35), (fx + fw * 0.7, fy - fh * 0.1), (fx, fy), (fx - fw * 0.7, fy - fh * 0.1), (fx - fw, fy - fh * 0.35)]
    d.polygon(pts, fill=col(mix(FLAME, (255, 240, 200, 255), 0.3), 1))
    inner = [(fx, fy - fh * 0.6), (fx + fw * 0.45, fy - fh * 0.25), (fx, fy - fh * 0.05), (fx - fw * 0.45, fy - fh * 0.25)]
    d.polygon(inner, fill=(255, 250, 230, 255))
    # the flame's face
    ey = fy - fh * 0.32 + sad * fh * 0.04
    er = max(1.5, fw * 0.1)
    for o in (-1, 1):
        if strain > 0.5:
            d.line([(fx + o * fw * 0.3 - er, ey), (fx + o * fw * 0.3 + er, ey)], fill=(80, 40, 10, 255), width=max(1, int(er)))
        else:
            d.ellipse([fx + o * fw * 0.3 - er, ey - er * 1.3, fx + o * fw * 0.3 + er, ey + er * 1.3], fill=(80, 40, 10, 255))
    if sputter > 0:  # smoke curls
        for k in range(5):
            u = ((t * 0.6 + k / 5) % 1)
            sx = fx + math.sin(u * 8 + k) * cam.s(30)
            sy = fy - fh - u * cam.s(400)
            r = cam.s(20 + 50 * u)
            tpoly(d, [(sx - r, sy - r), (sx + r, sy + r)], col((180, 180, 190, 255), 0.35 * sputter * (1 - u)), kind="ellipse")
    return fx, fy - fh * 0.5, fh


def reader(d, cam, t, a=1.0):
    """The small world inside the candle's light: someone reading, a cat, a cup of tea."""
    fx, fy = cam.p(-420, -60)
    h = cam.s(520)
    figure(d, fx, fy, h, YOU, mode="sit", face=1, acc=("hair",), head_down=0.45, a=a,
           hands=((fx + h * 0.2, fy - h * 0.42), (fx + h * 0.28, fy - h * 0.42)))
    bx, by = fx + h * 0.24, fy - h * 0.45
    d.polygon([(bx - h * 0.1, by), (bx, by - h * 0.03), (bx + h * 0.1, by), (bx, by + h * 0.02)], fill=col((240, 232, 210, 255), a))
    # cat
    cx, cy = cam.p(350, -60)
    d.ellipse([cx - cam.s(110), cy - cam.s(70), cx + cam.s(110), cy], fill=col((70, 60, 60, 255), a))
    d.ellipse([cx + cam.s(60), cy - cam.s(100), cx + cam.s(140), cy - cam.s(30)], fill=col((70, 60, 60, 255), a))
    for o in (0, 1):
        ex = cx + cam.s(80 + 40 * o)
        d.polygon([(ex - cam.s(14), cy - cam.s(90)), (ex, cy - cam.s(124)), (ex + cam.s(14), cy - cam.s(90))], fill=col((70, 60, 60, 255), a))
    # tea
    tx, ty = cam.p(200, -60)
    d.rounded_rectangle([tx - cam.s(40), ty - cam.s(80), tx + cam.s(40), ty], int(cam.s(10)), fill=col((220, 210, 200, 255), a))
    for k in range(3):
        u = ((t * 0.4 + k / 3) % 1)
        sx = tx + math.sin(u * 6 + k) * cam.s(14)
        sy = ty - cam.s(90) - u * cam.s(120)
        d.ellipse([sx - cam.s(6), sy - cam.s(6), sx + cam.s(6), sy + cam.s(6)], fill=col((255, 240, 220, 255), 0.4 * (1 - u) * a))


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # pure black; a spark; a tiny flame — which opens its eyes
    cam = cam_lerp((0, -420, 3.0), (0, -380, 1.8), sstep(p))
    window_scene(d, cam, t)
    power = ramp(t, 0.6, 0.6)
    lx, ly, fh = candle(d, cam, t, power=max(0.05, power))
    light_hole(d, lx, ly, cam.s(260) * (0.3 + power), a=1.0)


def s1_sun(d, t, dur):
    p = t / dur
    # the sun rises, colossal, and fills the window; the candle strains to match it and starts to sputter
    cam = cam_lerp((0, -380, 1.2), (0, -550, 0.55), sstep(p))
    day = sstep(ramp(p, 0.0, 0.6))
    wy0, wy1 = cam.p(0, -1100)[1], cam.p(0, -60)[1]
    window_scene(d, cam, t, day=day, sun_y=lerp(wy1 + cam.s(400), wy0 + cam.s(450), day))
    strain = sstep(ramp(p, 0.35, 0.4))
    sput = ramp(p, 0.75, 0.25)
    candle(d, cam, t, power=1.0, strain=strain * (1 - sput), sputter=sput)


def s2_compare(d, t, dur):
    p = t / dur
    # tiny beside the huge bright window, the flame shrinks and droops
    cam = cam_lerp((0, -550, 0.55), (0, -380, 1.1), sstep(p))
    window_scene(d, cam, t, day=1.0, sun_y=cam.p(0, -1100)[1] + cam.s(450))
    candle(d, cam, t, power=0.55, sad=1.0, sputter=0.6 * (1 - p))
    top_caption(d, ["DON'T COMPARE", "YOUR LIGHT…"], t, dur, accent={"COMPARE"})


def s3_sky(d, t, dur):
    p = t / dur
    # night returns; the flame burns steady; the camera pulls back and its circle of light holds a whole small world
    night = sstep(ramp(p, 0.0, 0.35))
    cam = cam_lerp((0, -380, 1.1), (-80, -420, 0.55), sstep(ramp(p, 0.2, 0.7)))
    window_scene(d, cam, t, day=1 - night)
    reveal = sstep(ramp(p, 0.4, 0.4))
    reader(d, cam, t, a=1.0)
    lx, ly, fh = candle(d, cam, t, power=lerp(0.6, 1.1, night))
    light_hole(d, lx, ly, cam.s(lerp(300, 1100, reveal)) + fh, a=night)
    dust(d, t, 0.4 * reveal, n=40, color=(255, 210, 150))
    top_caption(d, ["TO SOMEONE", "ELSE'S SKY."], t, dur, accent={"SKY."})


def s4_end(d, t, dur):
    cam = Cam(-80, -420, 0.55)
    window_scene(d, cam, t, night=1.0)
    reader(d, cam, t)
    lx, ly, fh = candle(d, cam, t, power=1.1)
    light_hole(d, lx, ly, cam.s(1100) + fh, a=1.0)
    final_card(d, t, dur, ["SHINE WHERE", "YOU ARE."], [WHITE, FLAME], size=110, y=H * 0.22)


SCENES = [s0_hook, s1_sun, s2_compare, s3_sky, s4_end, s_follow]
