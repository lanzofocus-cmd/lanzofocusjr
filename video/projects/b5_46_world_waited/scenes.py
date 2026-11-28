"""THE WORLD THAT WAITED — a locked-off time-lapse of a city that never pauses, and one person on a bench.

World: a city plaza seen straight on, a clock tower, a tree, a bench. The camera never moves while time does: suns
whip across the sky, nights flicker, seasons cycle (blossom, green, amber, snow), crowds become streaks of light,
cranes raise new towers. THE PERSON (lilac) sits motionless on the bench, snow piling on their shoulders. Then they
stand, shake it off, and run: the camera finally moves with them and the world slows to real time as they join it.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, dust, snow)
from kit import s_follow

TITLE = ("THE WORLD", "THAT WAITED")
OUTPUT = "146_The_World_That_Waited_16x9.mp4"
LINES = [
    "",
    "",
    "The world isn't waiting for you.",
    "But you can still catch up.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.6, 4: 3.4}
GAPS = {2: 3.0, 3: 6.6}

PERSON = (200, 160, 255, 255)
CH = 240
SEASON_LEAF = [(255, 170, 200), (70, 170, 80), (230, 140, 50), (235, 240, 250)]
SEASON_GROUND = [(90, 100, 90), (80, 100, 80), (100, 90, 70), (210, 215, 225)]
CROWD = [(255, 120, 120), (120, 200, 255), (255, 210, 100), (150, 255, 170), (255, 160, 220), (200, 200, 220)]


def sky_at(day):
    ph = day % 1.0                       # 0 = midnight, 0.5 = noon
    light = clamp(0.5 - 0.5 * math.cos(ph * math.tau) * 1.25 + 0.1)
    dusk = math.exp(-((min(abs(ph - 0.27), abs(ph - 0.75))) / 0.05) ** 2)
    top = mix(mix((8, 12, 30, 255), (80, 140, 220, 255), light), (120, 70, 130, 255), dusk * 0.5)
    bot = mix(mix((20, 25, 55, 255), (180, 215, 245, 255), light), (255, 150, 90, 255), dusk * 0.8)
    return top, bot, light, ph


def season_mix(day, table):
    s = (day / 3.0) % 4.0
    i = int(s)
    return mix(table[i] + (255,), table[(i + 1) % 4] + (255,), sstep(clamp((s - i - 0.7) / 0.3)))


def city(d, cam, t, day, rise=0.0, crowd_speed=1.0, streak=1.0):
    top, bot, light, ph = sky_at(day)
    draw_sky(d, top, bot)
    # sun or moon racing along an arc
    ang = ph * math.tau - math.pi / 2
    bx, by = cam.p(math.cos(ang) * 1700, -300 + math.sin(ang) * 1100)
    if by < cam.p(0, -250)[1]:
        c = (255, 230, 160) if 0.25 < ph < 0.75 else (230, 235, 255)
        glow(d, bx, by, cam.s(260), c, 0.5)
        d.ellipse([bx - cam.s(50), by - cam.s(50), bx + cam.s(50), by + cam.s(50)], fill=c + (255,))
    # skyline: some towers are cranes-and-frames that rise over the years
    for i in range(int((cam.cx - 2600) // 260), int((cam.cx + 2600) // 260) + 1):
        r = random.Random(i * 13 + 3)
        x = i * 260 + r.uniform(-30, 30)
        h = r.uniform(500, 1100)
        grows = i % 4 == 1 and abs(i * 260 - 660) > 300
        if grows:
            h = lerp(150, h + 500, rise)
        bcol = mix((40, 45, 70, 255), (120, 130, 160, 255), light * 0.6)
        d.rectangle(cam.box(x, -h, x + 220, 0), fill=bcol)
        if grows and rise < 0.98:  # crane on top
            cx, cy = cam.p(x + 110, -h)
            d.line([(cx, cy), (cx, cy - cam.s(220))], fill=(255, 190, 80, 255), width=max(2, int(cam.s(8))))
            d.line([(cx - cam.s(160), cy - cam.s(200)), (cx + cam.s(200), cy - cam.s(200))], fill=(255, 190, 80, 255), width=max(2, int(cam.s(8))))
        rr = random.Random(i * 7 + int(day))
        for wy in range(int(h // 90)):
            for wx in range(3):
                if rr.random() < (1 - light) * 0.7:
                    a, b = cam.p(x + 30 + wx * 65, -h + 40 + wy * 90), cam.p(x + 65 + wx * 65, -h + 75 + wy * 90)
                    d.rectangle([a[0], a[1], b[0], b[1]], fill=(255, 220, 140, 255))
    # clock tower
    d.rectangle(cam.box(560, -1050, 760, 0), fill=mix((60, 55, 70, 255), (150, 140, 150, 255), light * 0.6))
    d.polygon([cam.p(540, -1050), cam.p(780, -1050), cam.p(660, -1250)], fill=(70, 60, 80, 255))
    cx, cy = cam.p(660, -900)
    R = cam.s(80)
    d.ellipse([cx - R, cy - R, cx + R, cy + R], fill=(240, 235, 220, 255), outline=(40, 40, 50, 255), width=max(2, int(cam.s(8))))
    hr = day * math.tau * 2
    mn = day * math.tau * 24
    d.line([(cx, cy), (cx + math.sin(hr) * R * 0.55, cy - math.cos(hr) * R * 0.55)], fill=(30, 30, 40, 255), width=max(2, int(cam.s(10))))
    d.line([(cx, cy), (cx + math.sin(mn) * R * 0.85, cy - math.cos(mn) * R * 0.85)], fill=(30, 30, 40, 255), width=max(2, int(cam.s(6))))
    # ground
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=dimc(season_mix(day, SEASON_GROUND), 0.5 + 0.5 * light))
    # crowd: streaks when time is fast, walkers when it is slow
    if streak > 0.02:
        rr = random.Random(11)
        for i in range(18):
            y = rr.uniform(20, 160)
            spd = rr.uniform(0.6, 1.4) * (1 if i % 2 else -1)
            x = ((t * 2.3 * spd + rr.random()) % 1) * 5000 - 2500
            a, b = cam.p(x, y - 26), cam.p(x + spd * 700, y)
            tpoly(d, [(min(a[0], b[0]), a[1]), (max(a[0], b[0]), a[1]), (max(a[0], b[0]), b[1]), (min(a[0], b[0]), b[1])], rr.choice(CROWD) + (int(140 * streak),))
    if streak < 0.98:
        rr = random.Random(12)
        for i in range(22):
            spd = rr.uniform(100, 200) * crowd_speed
            x0 = rr.uniform(-2500, 2500)
            x = cam.cx + ((x0 + t * spd + 2500) % 5000) - 2500
            y = rr.uniform(40, 150)
            fx, fy = cam.p(x, y)
            figure(d, fx, fy, cam.s(CH * 0.95), rr.choice(CROWD) + (255,), mode="walk", phase=x / 30, face=1, a=1 - streak, eyes=False, mouth=0)


def tree(d, cam, day):
    bx, by = cam.p(-500, 0)
    d.rectangle(cam.box(-520, -420, -480, 0), fill=(70, 50, 40, 255))
    leaf = season_mix(day, SEASON_LEAF)
    for (ox, oy, rr) in ((-500, -520, 200), (-620, -430, 140), (-380, -440, 150), (-500, -650, 140)):
        sx, sy = cam.p(ox, oy)
        d.ellipse([sx - cam.s(rr), sy - cam.s(rr * 0.8), sx + cam.s(rr), sy + cam.s(rr * 0.8)], fill=leaf)


def bench(d, cam):
    d.rectangle(cam.box(-150, -70, 150, -50), fill=(110, 80, 60, 255))
    d.rectangle(cam.box(-150, -150, 150, -130), fill=(110, 80, 60, 255))
    for x in (-130, 120):
        d.rectangle(cam.box(x, -70, x + 12, 0), fill=(40, 40, 50, 255))


def person(d, cam, x, t, mode="sit", snow_k=0.0, **kw):
    fx, fy = cam.p(x, 0 if mode != "sit" else -60)
    if mode != "sit":
        glow(d, fx, fy - cam.s(CH * 0.5), cam.s(CH * 1.2), PERSON[:3], 0.45)
    figure(d, fx, fy, cam.s(CH), PERSON, mode=mode, phase=kw.pop("phase", t * 6), face=kw.pop("face", 1), acc=("scarf",),
           name=kw.pop("name", "THE PERSON"), **kw)
    if snow_k > 0.02:  # snow piled on head and shoulders
        hx, hy = cam.p(x, -60 - CH * 0.92) if mode == "sit" else cam.p(x, -CH * 0.98)
        d.ellipse([hx - cam.s(30) * snow_k, hy - cam.s(16) * snow_k, hx + cam.s(30) * snow_k, hy + cam.s(6)], fill=(245, 248, 255, 255))


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # tight on the tower clock: the minute hand starts creeping, then whirls; pull back to the plaza
    day = 0.3 + (sstep(p) ** 2) * 0.6
    cam = cam_lerp((660, -900, 3.2), (0, -450, 0.5), sstep(ramp(p, 0.45, 0.55)))
    city(d, cam, t, day, streak=sstep(ramp(p, 0.5, 0.5)))
    tree(d, cam, day)
    bench(d, cam)
    person(d, cam, 0, t, mode="sit", name="")


def s1_timelapse(d, t, dur):
    p = t / dur
    # locked-off camera: days flash by, seasons turn, crowds become rivers of light; the person never moves
    day = 0.9 + p * 6
    cam = Cam(0, -450, 0.5)
    city(d, cam, t, day, rise=0.3 * p)
    tree(d, cam, day)
    bench(d, cam)
    person(d, cam, 0, t, mode="sit", head_down=True)


def s2_world(d, t, dur):
    p = t / dur
    # more years: cranes raise new towers, winter comes, snow piles on the person's shoulders
    day = 6.9 + p * 5.5
    cam = cam_lerp((0, -450, 0.5), (0, -300, 0.62), sstep(p))
    city(d, cam, t, day, rise=0.3 + 0.7 * sstep(p))
    tree(d, cam, day)
    bench(d, cam)
    winter = 1 - abs(((day / 3.0) % 4.0) - 3.5) / 0.5 if ((day / 3.0) % 4.0) > 3 else 0
    if winter > 0:
        snow(d, t, 0.6 * winter)
    person(d, cam, 0, t, mode="sit", head_down=True, snow_k=clamp(p * 1.5))
    top_caption(d, ["THE WORLD ISN'T", "WAITING FOR YOU."], t, dur, accent={"ISN'T", "WAITING"})


def s3_catchup(d, t, dur):
    p = t / dur
    # they stand, shake off the snow, and run; the camera finally moves; time slows to real; they join the stream
    stand = sstep(ramp(p, 0.05, 0.12))
    run = sstep(ramp(p, 0.18, 0.82))
    slow = sstep(ramp(p, 0.15, 0.4))
    day = 12.4 + (1 - slow) * p * 2 + 0.25 * p   # time-lapse decelerates into one sunrise
    x = lerp(0, 3200, run ** 1.2)
    cam = cam_lerp((0, -300, 0.62), (x + 250, -380, 0.6), sstep(ramp(p, 0.18, 0.3)))
    city(d, cam, t, day, rise=1.0, crowd_speed=1.0, streak=1 - slow)
    tree(d, cam, day)
    bench(d, cam)
    if p < 0.15:
        person(d, cam, 0, t, mode="sit", head_down=p < 0.07, snow_k=1 - stand * 3, name="")
        if p > 0.08:
            particles(d, *cam.p(0, -200), cam.s(200), (p - 0.08) / 0.07, (245, 248, 255), n=14, seed=2, rise=-0.2)
    else:
        person(d, cam, x, t, mode="run" if run < 0.98 else "walk", phase=x / 35, mouth=0.5, lean=0.15 * (1 - slow * 0.5), name="")
    top_caption(d, ["BUT YOU CAN STILL", "CATCH UP."], t, dur, accent={"STILL", "CATCH"})


def s4_end(d, t, dur):
    cam = Cam(3450, -380, 0.6)
    city(d, cam, t + 8, 12.65, rise=1.0, streak=0.0)
    person(d, cam, 3200 + t * 120, t, mode="walk", phase=t * 5, mouth=0.6, name="")
    stage_end(d, t, dur, ["DON'T WAIT.", "MOVE."], [WHITE, PERSON], size=120, dim=0.4, glow_col=PERSON[:3], y=H * 0.3)


SCENES = [s0_hook, s1_timelapse, s2_world, s3_catchup, s4_end, s_follow]
