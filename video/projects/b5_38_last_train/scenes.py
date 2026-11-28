"""THE LAST TRAIN — a passenger waiting for the perfect train while every train leaves.

World: a vast iron-and-glass railway station at night in teal and amber, a huge platform clock and a
split-flap departures board. THE PASSENGER (mustard coat, suitcase) waits. Trains roar in and out in streaks of
light; the board flips and flips; the clock hands race. The last train starts to roll; the passenger runs the
length of the platform and leaps aboard as it pulls out into the dawn.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, sun, dust)
from kit import s_follow

TITLE = ("THE LAST", "TRAIN")
OUTPUT = "138_The_Last_Train_16x9.mp4"
LINES = [
    "",
    "Some people miss their lives…",
    "Waiting for the perfect moment.",
    "",
    "",
]
SILENT = {0: 3.2, 3: 3.6}
GAPS = {1: 4.6, 2: 6.2}

PASS = (240, 190, 70, 255)
TRAIN = (40, 70, 80, 255)
AMBER = (255, 200, 120, 255)
CH = 230
PLAT_Y = 0       # platform surface
RAIL_Y = 160     # track bed (in front of the platform edge, lower)


def station(d, cam, t, dawn=0.0, board_text="NOT YET", clock_speed=1.0):
    draw_sky(d, mix((6, 14, 20, 255), (110, 140, 190, 255), dawn), mix((20, 40, 50, 255), (255, 190, 140, 255), dawn))
    if dawn > 0.05:
        sun(d, W * 0.85, H * 0.55, 80, dawn, (255, 220, 160, 255))
    # glass roof arches
    for k in range(-6, 7):
        x = k * 600
        a = cam.p(x, -1500)
        b = cam.p(x + 600, -1500)
        d.arc([a[0], a[1] - cam.s(300), b[0], a[1] + cam.s(300)], 180, 360, fill=col((90, 120, 120, 255), 0.7), width=max(2, int(cam.s(8))))
        d.line([cam.p(x, -1500), cam.p(x, PLAT_Y)], fill=(40, 56, 60, 255), width=max(2, int(cam.s(16))))
    # platform and tracks
    p0 = cam.p(0, PLAT_Y)[1]
    d.rectangle([0, p0, W, cam.p(0, RAIL_Y - 60)[1]], fill=(70, 70, 76, 255))
    d.rectangle([0, cam.p(0, RAIL_Y - 60)[1], W, H], fill=(24, 24, 28, 255))
    d.line([(0, p0 + cam.s(10)), (W, p0 + cam.s(10))], fill=col((230, 200, 60, 255), 0.8), width=max(2, int(cam.s(10))))
    for k in range(-40, 60):
        x = cam.p(k * 120, 0)[0]
        d.line([(x, cam.p(0, RAIL_Y)[1]), (x + cam.s(40), cam.p(0, RAIL_Y + 60)[1])], fill=(50, 40, 34, 255), width=max(2, int(cam.s(14))))
    for yy in (RAIL_Y + 10, RAIL_Y + 50):
        d.line([(0, cam.p(0, yy)[1]), (W, cam.p(0, yy)[1])], fill=(130, 130, 140, 255), width=max(1, int(cam.s(5))))
    # the big clock
    cx, cy = cam.p(-700, -1050)
    r = cam.s(170)
    d.ellipse([cx - r * 1.1, cy - r * 1.1, cx + r * 1.1, cy + r * 1.1], fill=(40, 50, 54, 255))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(240, 232, 210, 255))
    for k in range(12):
        a = k * math.pi / 6
        d.line([(cx + math.cos(a) * r * 0.82, cy + math.sin(a) * r * 0.82), (cx + math.cos(a) * r * 0.95, cy + math.sin(a) * r * 0.95)], fill=(40, 40, 40, 255), width=3)
    ma = t * clock_speed * 2 - math.pi / 2
    ha = t * clock_speed * 2 / 12 - math.pi / 2 + 2
    d.line([(cx, cy), (cx + math.cos(ha) * r * 0.5, cy + math.sin(ha) * r * 0.5)], fill=(30, 30, 30, 255), width=max(2, int(r * 0.06)))
    d.line([(cx, cy), (cx + math.cos(ma) * r * 0.8, cy + math.sin(ma) * r * 0.8)], fill=(30, 30, 30, 255), width=max(2, int(r * 0.035)))
    glow(d, cx, cy, r * 2, AMBER, 0.25)
    # departures board
    bx, by = cam.p(400, -1050)
    bw, bh = cam.s(700), cam.s(160)
    d.rectangle([bx - bw / 2, by - bh / 2, bx + bw / 2, by + bh / 2], fill=(14, 16, 18, 255), outline=(60, 60, 60, 255), width=3)
    d.text((bx, by - bh * 0.22), "DEPARTURES", font=font(max(10, int(cam.s(30)))), fill=col(AMBER, 0.8), anchor="mm")
    d.text((bx, by + bh * 0.18), board_text, font=font(max(10, int(cam.s(52)))), fill=col(AMBER, 1), anchor="mm")
    fog(d, *cam.p(0, -200), cam.s(5000), 0.15, (160, 200, 200))


def train(d, cam, x, t, cars=6, blur=0.0, lit=1.0, doors=0.0):
    """A train whose front is at world x (moving right), on the track in front of the platform."""
    L = 900
    for c in range(cars):
        x1 = x - c * (L + 30)
        x0 = x1 - L
        a, b = cam.p(x0, -470), cam.p(x1, -40)
        if b[0] < -50 or a[0] > W + 50:
            continue
        d.rounded_rectangle([a[0], a[1], b[0], b[1]], int(cam.s(40 if c == 0 else 16)), fill=col(TRAIN, 1))
        d.rectangle([a[0], a[1] + cam.s(60), b[0], a[1] + cam.s(80)], fill=col((230, 200, 60, 255), 1))
        for k in range(6):
            wx0 = x0 + 60 + k * 140
            q0, q1 = cam.p(wx0, -340 + -40), cam.p(wx0 + 100, -220 + -40)
            d.rectangle([q0[0], q0[1], q1[0], q1[1]], fill=col(AMBER, 0.4 + 0.6 * lit))
        if doors > 0 and c == cars - 1:  # an open door in the last car
            q0, q1 = cam.p(x0 + 380, -360 + -40), cam.p(x0 + 380 + 140 * doors, -50)
            d.rectangle([q0[0], q0[1], q1[0], q1[1]], fill=col((255, 230, 180, 255), 1))
            glow(d, (q0[0] + q1[0]) / 2, (q0[1] + q1[1]) / 2, cam.s(260), AMBER, 0.6 * doors)
    if blur > 0:  # speed streaks
        r = random.Random(int(t * 30))
        for i in range(int(30 * blur)):
            y = cam.p(0, r.uniform(-420, 0) + -40)[1]
            x0 = r.uniform(0, W)
            d.line([(x0, y), (x0 - r.uniform(100, 400) * blur, y)], fill=col(AMBER, 0.5 * blur), width=2)


def passenger(d, cam, x, t, mode="stand", **kw):
    fx, fy = cam.p(x, PLAT_Y)
    h = cam.s(CH)

    def case(dd, fh, bh, hh, a):
        if bh and mode in ("stand", "walk", "run"):
            dd.rounded_rectangle([bh[0] - hh * 0.09, bh[1], bh[0] + hh * 0.09, bh[1] + hh * 0.16], int(hh * 0.02), fill=col((120, 70, 40, 255), a))
    figure(d, fx, fy, h, PASS, mode=mode, phase=kw.pop("phase", t * 5), face=kw.pop("face", 1), acc=("hair",), prop=case, name="THE PASSENGER", **kw)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # a train roars through, right past the lens, in a blur of light; behind it, the passenger under the clock
    cam = Cam(-200, -500, 0.62)
    station(d, cam, t)
    passenger(d, cam, -400, t, look=0.3)
    x = lerp(-1500, 9000, sstep(clamp(t / (dur * 0.8))))
    if t < dur * 0.85:
        train(d, cam, x, t, cars=7, blur=1.0)
    shake(cam, t, 6 * (1 - ramp(t, dur * 0.7, 0.4)))


def s1_miss(d, t, dur):
    p = t / dur
    # train after train arrives, waits and leaves; the passenger checks, hesitates, steps back; the clock races
    cam = Cam(-200, -500, 0.62)
    texts = ["NOT YET", "TOO EARLY", "NOT READY", "MAYBE NEXT", "NOT PERFECT"]
    station(d, cam, t, board_text=texts[int(p * 5) % 5], clock_speed=8)
    cycle = (p * 3) % 1
    if cycle < 0.3:
        x = lerp(-3000, 1400, sstep(cycle / 0.3))
    elif cycle < 0.6:
        x = 1400
    else:
        x = lerp(1400, 8000, sstep((cycle - 0.6) / 0.4))
    train(d, cam, x, t, cars=5, doors=1.0 if 0.3 < cycle < 0.6 else 0.0)
    passenger(d, cam, -400 + 60 * math.sin(cycle * math.pi) * (0.3 < cycle < 0.6), t, mode="stand", look=0.2,
              lean=0.15 if 0.3 < cycle < 0.45 else (-0.1 if 0.45 < cycle < 0.6 else 0))
    top_caption(d, ["SOME PEOPLE MISS", "THEIR LIVES…"], t, dur, accent={"MISS"})


def s2_perfect(d, t, dur):
    p = t / dur
    # the last train: LAST TRAIN on the board, a bell; it starts rolling; the passenger runs and leaps aboard;
    # the camera tracks alongside and the train pulls out into the dawn
    start = 0.15
    tx = 1400 + (0 if p < start else 4500 * ((p - start) / (1 - start)) ** 1.6)
    run = sstep(ramp(p, 0.15, 0.4))
    aboard = p > 0.55
    px = lerp(-400, tx - 5 * 930 + 450, run) if not aboard else tx - 5 * 930 + 450
    dawn = sstep(ramp(p, 0.55, 0.45))
    cam = Cam(lerp(-200, px + 200, sstep(ramp(p, 0.15, 0.4))), -500, lerp(0.62, 0.5, p))
    station(d, cam, t, dawn=dawn, board_text="LAST TRAIN", clock_speed=1)
    train(d, cam, tx, t, cars=6, doors=1.0 - ramp(p, 0.58, 0.1), blur=clamp((p - 0.6) * 2))
    if not aboard:
        passenger(d, cam, px, t, mode="run" if run > 0 else "stand", phase=px / 40, lean=0.35, swing=1.0, stride=1.4, look=0.3)
    else:
        fx, fy = cam.p(px, -60)
        figure(d, fx, fy, cam.s(CH), PASS, mode="cheer", face=1, acc=("hair",), mouth=0.8)
    dust(d, t, 0.4 * dawn, n=40, color=(255, 220, 170))
    top_caption(d, ["WAITING FOR THE", "PERFECT MOMENT."], t, dur, accent={"PERFECT"})


def s3_end(d, t, dur):
    cam = Cam(4500, -500, 0.5)
    station(d, cam, t, dawn=1.0, board_text="DEPARTED")
    train(d, cam, 6000 + 900 * t, t, cars=6, blur=0.6)
    stage_end(d, t, dur, ["GET ON", "THE TRAIN."], [WHITE, PASS], size=120, dim=0.4, glow_col=AMBER, y=H * 0.3)


SCENES = [s0_hook, s1_miss, s2_perfect, s3_end, s_follow]
