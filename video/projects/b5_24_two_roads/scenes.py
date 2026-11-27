"""THE TWO ROADS — one smooth, one hard; told in a diagonal split screen.

World: a fork in the road seen from above, then a split screen that follows both travelers at once. Left: THE
COMFORTABLE TRAVELER (pastel pink) on a smooth, sunny, flower-lined road gently downhill, which narrows and ends
at a blank wall. Right: THE DIFFICULT TRAVELER (deep blue) climbing a rocky, windy, uphill track in grey weather,
which crests over an enormous shining city. At the end the split closes on the city.
"""
import math
import random
from PIL import Image, ImageDraw
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, sun, cloud, rain, dust)
from kit import s_follow

TITLE = ("THE TWO", "ROADS")
OUTPUT = "124_The_Two_Roads_16x9.mp4"
LINES = [
    "",
    "",
    "Easy isn't always better.",
    "Difficult isn't always wrong.",
    "Choose the road that takes you somewhere.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.0, 5: 3.4}
GAPS = {2: 1.8, 3: 2.0, 4: 3.6}

COMF = (255, 170, 190, 255)
DIFF = (80, 130, 255, 255)
GOLD = (255, 205, 110, 255)
CH = 200
WALL_X = 3000
CREST_X = 3000


def easy_world(d, cam, t, prog):
    draw_sky(d, (140, 200, 250, 255), (255, 235, 220, 255))
    sun(d, W * 0.3, H * 0.2, 70, 1.0, (255, 240, 190, 255))
    for j in range(4):
        cloud(d, (j * 500 + t * 15) % (W + 400) - 200, 140 + 40 * (j % 2), 60, col(WHITE, 0.9))
    def road_y(x):
        return 0.08 * x
    pts = [cam.p(x, road_y(x)) for x in range(-3000, WALL_X + 1, 100)]
    gy_pts = pts + [(pts[-1][0], H + 10), (pts[0][0], H + 10)]
    d.polygon(gy_pts, fill=(150, 210, 130, 255))
    narrow = lambda x: lerp(1.0, 0.2, clamp((x - 1800) / 1200))
    top = [cam.p(x, road_y(x) - 40 * narrow(x)) for x in range(-1000, WALL_X + 1, 100)]
    bot = [cam.p(x, road_y(x) + 40 * narrow(x)) for x in range(WALL_X, -1001, -100)]
    d.polygon(top + bot, fill=(235, 225, 210, 255))
    r = random.Random(2)
    for i in range(40):  # flowers
        x = r.uniform(-1000, WALL_X - 200)
        fx, fy = cam.p(x, road_y(x) + r.uniform(60, 160))
        c = r.choice([(255, 120, 150), (255, 220, 90), (200, 140, 255)])
        d.ellipse([fx - cam.s(10), fy - cam.s(10), fx + cam.s(10), fy + cam.s(10)], fill=c + (255,))
    # the dead end
    wx0, wy = cam.p(WALL_X, road_y(WALL_X) - 600)
    wx1, wy1 = cam.p(WALL_X + 400, road_y(WALL_X) + 300)
    d.rectangle([wx0, wy, wx1, wy1], fill=(170, 160, 160, 255))
    for k in range(6):
        yy = lerp(wy, wy1, k / 6)
        d.line([(wx0, yy), (wx1, yy)], fill=(140, 130, 130, 255), width=2)
    sx, sy = cam.p(WALL_X - 120, road_y(WALL_X) - 160)
    d.line([(sx, sy), (sx, cam.p(0, road_y(WALL_X))[1])], fill=(90, 80, 70, 255), width=max(2, int(cam.s(8))))
    d.rectangle([sx - cam.s(90), sy - cam.s(60), sx + cam.s(90), sy], fill=(230, 60, 60, 255))
    d.text((sx, sy - cam.s(30)), "DEAD END", font=font(max(10, int(cam.s(30)))), fill=WHITE, anchor="mm")
    x = lerp(-600, WALL_X - 220, prog)
    fx, fy = cam.p(x, road_y(x))
    stopped = prog >= 0.999
    figure(d, fx, fy, cam.s(CH), COMF, mode="sit" if stopped else "walk", phase=x / 70, face=1, acc=("hair",), mouth=0.7 if not stopped else -0.5,
           swing=0.3, name="COMFORTABLE", head_down=0.5 if stopped else 0.0)
    return x, road_y(x)


def hard_world(d, cam, t, prog, reveal=0.0):
    draw_sky(d, mix((60, 70, 90, 255), (40, 60, 120, 255), reveal), mix((130, 140, 150, 255), (255, 190, 130, 255), reveal))
    if reveal > 0:
        sun(d, W * 0.75, H * 0.45, 80, reveal, (255, 220, 160, 255))
    def road_y(x):
        return -0.32 * x + 40 * math.sin(x * 0.01)
    # the city beyond the crest
    if reveal > 0:
        r = random.Random(4)
        for i in range(40):
            bx = CREST_X + 300 + i * 90
            hgt = r.uniform(300, 1500) * reveal
            base_y = road_y(CREST_X) + 900
            a, b = cam.p(bx, base_y - hgt), cam.p(bx + 80, base_y)
            d.rectangle([a[0], a[1], b[0], b[1]], fill=(50, 44, 70, 255))
            if r.random() < 0.3:
                d.polygon([(a[0], a[1]), ((a[0] + b[0]) / 2, a[1] - cam.s(120)), (b[0], a[1])], fill=(50, 44, 70, 255))
            for wy in range(int(hgt / 60)):
                for wx in range(2):
                    if r.random() < 0.7:
                        q = cam.p(bx + 15 + wx * 35, base_y - hgt + 30 + wy * 60)
                        d.rectangle([q[0], q[1], q[0] + cam.s(20), q[1] + cam.s(28)], fill=col(GOLD, 0.95))
        glow(d, *cam.p(CREST_X + 2000, road_y(CREST_X) + 200), cam.s(2500), GOLD, 0.6 * reveal)
    pts = [cam.p(x, road_y(x)) for x in range(-1000, CREST_X + 1, 60)]
    pts += [cam.p(CREST_X + 200, road_y(CREST_X) + 300), cam.p(CREST_X + 200, 3000), cam.p(-1000, 3000)]
    d.polygon(pts, fill=(80, 74, 80, 255))
    r = random.Random(6)
    for i in range(50):  # rocks on the track
        x = r.uniform(-1000, CREST_X)
        rx, ry = cam.p(x, road_y(x) + r.uniform(-10, 40))
        s = cam.s(r.uniform(20, 60))
        d.polygon([(rx - s, ry), (rx - s * 0.4, ry - s * 0.8), (rx + s * 0.5, ry - s * 0.6), (rx + s, ry)], fill=(120, 112, 116, 255))
    x = lerp(-600, CREST_X - 60, prog)
    fx, fy = cam.p(x, road_y(x))
    top = prog >= 0.999
    figure(d, fx, fy, cam.s(CH), DIFF, mode="cheer" if top and reveal > 0.5 else "walk", phase=x / 50, face=1, acc=("hair", "backpack"), lean=0.4 if not top else 0.0,
           swing=0.5, tired=0.6 if not top else 0.0, mouth=0.7 * reveal, name="DIFFICULT")
    if reveal < 0.5:
        rain(d, t, 0.6, n=120, slant=0.6)
    return x, road_y(x)


def split(d, t, draw_left, draw_right, k=0.5):
    """Diagonal split screen: left world above-left of the line, right world below-right. k shifts the divide."""
    lay_l = Image.new("RGBA", (W, H))
    draw_left(ImageDraw.Draw(lay_l))
    lay_r = Image.new("RGBA", (W, H))
    draw_right(ImageDraw.Draw(lay_r))
    cx = W * k
    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).polygon([(0, 0), (cx + 200, 0), (cx - 200, H), (0, H)], fill=255)
    d._image.alpha_composite(lay_r)
    lay_l.putalpha(mask)
    d._image.alpha_composite(lay_l)
    d.line([(cx + 200, 0), (cx - 200, H)], fill=(255, 255, 255, 255), width=6)


def fork(d, cam, t, go=0.0):
    """Top-down view of the fork: a sunny paved road left, a dark rocky track right."""
    d.rectangle([0, 0, W, H], fill=(120, 150, 100, 255))
    tpoly(d, [(W / 2, 0), (W, 0), (W, H), (W / 2 + 200, H)], col((70, 70, 80, 255), 0.6))
    c = cam.p(0, 300)
    base = cam.p(0, 1600)
    d.polygon([(base[0] - cam.s(120), H), (base[0] + cam.s(120), H), (c[0] + cam.s(90), c[1]), (c[0] - cam.s(90), c[1])], fill=(220, 210, 190, 255))
    left = cam.p(-1600, -1400)
    right = cam.p(1600, -1400)
    d.polygon([(c[0] - cam.s(90), c[1]), (c[0] + cam.s(60), c[1] - cam.s(80)), (left[0] + cam.s(120), left[1]), (left[0] - cam.s(120), left[1])], fill=(235, 225, 210, 255))
    d.polygon([(c[0] - cam.s(60), c[1] - cam.s(80)), (c[0] + cam.s(90), c[1]), (right[0] + cam.s(100), right[1]), (right[0] - cam.s(100), right[1])], fill=(110, 104, 110, 255))
    r = random.Random(3)
    for i in range(60):
        x, y = r.uniform(300, 1700), r.uniform(-1400, 200)
        sx, sy = cam.p(x, y)
        d.ellipse([sx - cam.s(30), sy - cam.s(20), sx + cam.s(30), sy + cam.s(20)], fill=(90, 86, 92, 255))
    for i in range(60):
        x, y = r.uniform(-1700, -300), r.uniform(-1400, 200)
        sx, sy = cam.p(x, y)
        d.ellipse([sx - cam.s(12), sy - cam.s(12), sx + cam.s(12), sy + cam.s(12)], fill=r.choice([(255, 120, 150, 255), (255, 220, 90, 255)]))
    # two travelers from above (dots with heads)
    for s, c2 in ((-1, COMF), (1, DIFF)):
        u = sstep(go)
        px, py = cam.p(lerp(s * 60, s * 700, u), lerp(500, -600, u))
        d.ellipse([px - cam.s(34), py - cam.s(34), px + cam.s(34), py + cam.s(34)], fill=col(c2, 1))
        d.ellipse([px - cam.s(18), py - cam.s(18), px + cam.s(18), py + cam.s(18)], fill=col(dimc(c2, 0.7), 1))


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    cam = Cam(0, lerp(800, 100, sstep(p)), lerp(0.9, 0.5, sstep(p)))
    fork(d, cam, t)
    cloud(d, W * 0.2, H * 0.2 + 30 * p, 120, col(WHITE, 0.7 * (1 - p)))


def s1_choose(d, t, dur):
    p = t / dur
    cam = Cam(0, 100, 0.5)
    fork(d, cam, t, go=ramp(p, 0.2, 0.8))
    for i, (txt, x) in enumerate((("EASY", W * 0.25), ("HARD", W * 0.75))):
        d.text((x, H * 0.2), txt, font=font(80), fill=col(WHITE, 0.85 * ramp(t, 0.3 + 0.3 * i, 0.4)), anchor="mm")


def s2_easy(d, t, dur):
    p = t / dur
    pe, ph = lerp(0, 0.5, p), lerp(0, 0.3, p)
    split(d, t, lambda dd: _easy(dd, t, pe), lambda dd: _hard(dd, t, ph))
    top_caption(d, ["EASY ISN'T", "ALWAYS BETTER."], t, dur, accent={"EASY"})


def _easy(dd, t, prog):
    x = lerp(-600, WALL_X - 220, prog)
    cam = Cam(x + 200, 0.08 * x - 200, 0.65)
    easy_world(dd, cam, t, prog)


def _hard(dd, t, prog, reveal=0.0):
    x = lerp(-600, CREST_X - 60, prog)
    cam = Cam(x - 420 + reveal * 1500, -0.32 * x - 250 + reveal * 300, 0.65 - 0.3 * reveal)
    hard_world(dd, cam, t, prog, reveal)


def s3_wrong(d, t, dur):
    p = t / dur
    pe, ph = lerp(0.5, 1.0, sstep(p)), lerp(0.3, 0.85, p)
    split(d, t, lambda dd: _easy(dd, t, pe), lambda dd: _hard(dd, t, ph))
    top_caption(d, ["DIFFICULT ISN'T", "ALWAYS WRONG."], t, dur, accent={"DIFFICULT"})


def s4_somewhere(d, t, dur):
    p = t / dur
    ph = lerp(0.85, 1.0, sstep(ramp(p, 0.0, 0.3)))
    reveal = sstep(ramp(p, 0.25, 0.5))
    k = lerp(0.5, -0.2, sstep(ramp(p, 0.5, 0.4)))   # the split slides away, leaving the city
    split(d, t, lambda dd: _easy(dd, t, 1.0), lambda dd: _hard(dd, t, ph, reveal), k=k)
    dust(d, t, 0.5 * reveal, n=50, color=(255, 220, 160))
    top_caption(d, ["CHOOSE THE ROAD THAT", "TAKES YOU SOMEWHERE."], t, dur, accent={"SOMEWHERE."})


def s5_end(d, t, dur):
    _hard(d, t, 1.0, 1.0)
    stage_end(d, t, dur, ["CHOOSE YOUR ROAD."], [GOLD], size=120, dim=0.4, glow_col=GOLD, y=H * 0.25)


SCENES = [s0_hook, s1_choose, s2_easy, s3_wrong, s4_somewhere, s5_end, s_follow]
