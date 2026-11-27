"""THE RACE AGAINST YOUR OLD SELF — a night stadium, two versions of the same runner.

World: an empty stadium under floodlights, steel-blue night, a red track with white lane lines. Side-on tracking
camera with parallax stands and light towers. OLD YOU is muted grey-brown in a hood; FUTURE YOU is the same
silhouette in glowing cyan. By the end the old self turns cyan and crosses the line alone.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline, pill
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, rain, figure,
                   top_caption, low_caption, final_card, shake, beam, darkness, label_tag)
from kit import s_follow

TITLE = ("THE RACE AGAINST", "YOUR OLD SELF")
OUTPUT = "93_The_Race_Against_Your_Old_Self_16x9.mp4"
FOLLOW_SUB = ("FOR IDEAS, LESSONS, AND PERSPECTIVES", "THAT CHALLENGE THE WAY YOU THINK.")

LINES = [
    "The most important race you'll ever run…",
    "…is against the person you were yesterday.",
    "Your old self knows every excuse.",
    "Your future self doesn't care about your excuses.",
    "Every day you delay…",
    "…is another day they get further ahead.",
    "Stop wishing you were them.",
    "Start becoming them.",
    "Your only competition is who you were.",
    "",
]
SPOKEN = [l.lstrip("…") for l in LINES]
GAPS = {0: 0.4, 1: 1.0, 2: 2.0, 3: 1.4, 4: 0.3, 5: 1.4, 6: 1.3, 7: 3.0, 8: 1.6}

OLD = (150, 135, 120, 255)
FUT = (110, 220, 255, 255)
TRACK = (120, 40, 40, 255)
SKY_T = (2, 6, 14, 255)
SKY_B = (14, 30, 52, 255)
CH = 225
FIN = 4600
LANE_Y = {"FUT": -75, "OLD": 70}


def stadium(d, cam, t, light=1.0, wet=0.0, lights_on=1.0):
    draw_sky(d, SKY_T, SKY_B)
    # stands (parallax 0.4): tiers of empty seats
    f = 0.4
    z2 = cam.z * (0.55 + 0.45 * f)
    base_y = (-420 - cam.cy * f) * z2 + H / 2 + cam.oy
    off = (-cam.cx * f) * z2
    for tier in range(6):
        y = base_y - tier * 60 * z2
        d.rectangle([0, y - 52 * z2, W, y], fill=(10 + tier * 2, 16 + tier * 2, 28 + tier * 3, 255))
        sp = 46 * z2
        x0 = off % sp
        for i in range(int(W / sp) + 2):
            x = x0 + i * sp - sp
            d.rectangle([x, y - 30 * z2, x + sp * 0.6, y - 12 * z2], fill=(24, 36, 58, 255))
    # light towers (parallax 0.6)
    f = 0.6
    z3 = cam.z * (0.55 + 0.45 * f)
    for i in range(-6, 30):
        wx = i * 1500
        sx = (wx - cam.cx * f) * z3 + W / 2
        if sx < -400 or sx > W + 400:
            continue
        top = (-1300 - cam.cy * f) * z3 + H / 2 + cam.oy
        bot = (-200 - cam.cy * f) * z3 + H / 2 + cam.oy
        d.line([(sx, top), (sx, bot)], fill=(30, 40, 60, 255), width=max(2, int(10 * z3)))
        on = clamp(lights_on * 6 - (i % 6))
        d.rectangle([sx - 70 * z3, top - 40 * z3, sx + 70 * z3, top], fill=col((230, 240, 255, 255), 0.25 + 0.75 * on))
        if on > 0:
            glow(d, sx, top - 20 * z3, 260 * z3, (200, 225, 255), 0.8 * on)
            beam(d, sx, top, sx - 600 * z3, sx + 300 * z3, H, (200, 225, 255), 0.07 * on, 60 * z3)
    # track
    y0 = cam.p(0, -180)[1]
    y1 = cam.p(0, 260)[1]
    d.rectangle([0, y0, W, y1], fill=col(mix(TRACK, (60, 30, 40, 255), wet * 0.5), light))
    if y1 < H:
        d.rectangle([0, y1, W, H], fill=(16, 40, 30, 255))
    d.rectangle([0, y0 - cam.s(40), W, y0], fill=(18, 50, 34, 255))
    for ly in (-180, 0, 150, 260):
        polyline(d, [(0, cam.p(0, ly)[1]), (W, cam.p(0, ly)[1])], 1, col(WHITE, 0.75 * light), max(2, int(cam.s(6))))
    # distance markers and dashes
    step = 200
    xa = int((cam.cx - W / cam.z) / step) - 1
    xb = int((cam.cx + W / cam.z) / step) + 2
    for k in range(xa, xb):
        x = k * step
        sx, sy = cam.p(x, 205)
        d.line([(sx, sy - cam.s(12)), (sx, sy + cam.s(12))], fill=col(WHITE, 0.5 * light), width=max(1, int(cam.s(4))))
        if k % 5 == 0 and k >= 0:
            d.text((sx, cam.p(0, 232)[1]), f"{k * 2}M", font=font(max(12, int(cam.s(26)))), fill=col(WHITE, 0.5 * light), anchor="mm")
    # start line
    sx = cam.p(0, 0)[0]
    d.line([(sx, y0), (sx, y1)], fill=col(WHITE, light), width=max(3, int(cam.s(12))))
    # finish line
    fx = cam.p(FIN, 0)[0]
    if -100 < fx < W + 100:
        sq = cam.s(26)
        for r in range(int((y1 - y0) / sq) + 1):
            for c2 in range(2):
                if (r + c2) % 2 == 0:
                    d.rectangle([fx + c2 * sq, y0 + r * sq, fx + (c2 + 1) * sq, min(y1, y0 + (r + 1) * sq)], fill=col(WHITE, light))
    # wet sheen: reflections of the lights on the track
    if wet > 0:
        rng = random.Random(int(cam.cx / 50))
        for i in range(30):
            x = rng.uniform(0, W)
            y = rng.uniform(y0, y1)
            tpoly(d, [(x - 80, y), (x + 80, y)], col((200, 225, 255, 255), 0.18 * wet), kind="line", width=3)


def runner(d, cam, who, x, t, mode="run", color=None, a=1.0, name_a=1.0, **kw):
    y = LANE_Y[who]
    fx, fy = cam.p(x, y)
    s = 1.0 if who == "OLD" else 0.94
    c = color or (OLD if who == "OLD" else FUT)
    gk = kw.pop("glow_k", 1.0 if who == "FUT" else 0.0)
    if gk > 0:
        glow(d, fx, fy - cam.s(90), cam.s(240), c, 0.45 * a * gk)
    kw.setdefault("phase", x / 55)
    kw.setdefault("acc", ("hair", "hood") if who == "OLD" else ("hair",))
    nm = "OLD YOU" if who == "OLD" else "FUTURE YOU"
    figure(d, fx, fy, cam.s(CH * s), c, mode=mode, a=a, name=nm, name_a=name_a, name_col=c,
           lean=kw.pop("lean", 0.25 if mode == "run" else 0.0), swing=kw.pop("swing", 0.9 if mode == "run" else 0.4), **kw)
    return fx, fy


def phone_prop(d, fh, bh, h, a):
    if fh:
        x, y = fh
        d.rounded_rectangle([x - h * 0.03, y - h * 0.06, x + h * 0.03, y + h * 0.03], int(h * 0.01), fill=col((180, 220, 255, 255), a))
        glow(d, x, y, h * 0.4, (150, 200, 255), 0.6 * a)


def bubble(d, x, y, text, a, size=34):
    if a <= 0.01:
        return
    f = font(size)
    tw = d.textlength(text, font=f)
    d.rounded_rectangle([x - tw / 2 - 24, y - size, x + tw / 2 + 24, y + size * 0.8], int(size * 0.9), fill=col((30, 28, 26, 255), a), outline=col(OLD, a), width=3)
    d.text((x, y - size * 0.1), text, font=f, fill=col((230, 220, 210, 255), a), anchor="mm")


# ---------------------------------------------------------------- scenes
def s0_race(d, t, dur):
    p = t / dur
    # hook: black, then the floodlights slam on tower by tower, low on the start line
    cam = cam_lerp((0, -110, 1.9), (0, -110, 1.5), sstep(p))
    stadium(d, cam, t, lights_on=ramp(t, 0.2, 1.6))
    runner(d, cam, "FUT", 110, t, mode="stand", lean=0.12, phase=0, name_a=0, look=0.3)
    runner(d, cam, "OLD", -110, t, mode="stand", name_a=0, look=0.0)
    overlay(d, (0, 0, 0), 0.8 * (1 - ramp(t, 0.15, 0.25)))
    top_caption(d, ["THE MOST IMPORTANT RACE", "YOU'LL EVER RUN…"], t, dur, accent={"RACE"})


def s1_yesterday(d, t, dur):
    p = t / dur
    cam = cam_lerp((0, -110, 1.5), (150, -80, 0.95), sstep(p))
    stadium(d, cam, t)
    runner(d, cam, "FUT", 110, t, mode="stand", lean=0.12, phase=0, name_a=ramp(t, dur * 0.4, 0.5), look=0.3)
    runner(d, cam, "OLD", -110, t, mode="stand", name_a=ramp(t, dur * 0.55, 0.5), phase=0, head_down=0.3, tired=0.6)
    top_caption(d, ["…IS AGAINST THE PERSON", "YOU WERE YESTERDAY."], t, dur, accent={"YESTERDAY."})
s1_yesterday.seamless = True


def s2_excuses(d, t, dur):
    p = t / dur
    # Old You: runs, stops, phone, sits, watches the other runner
    if p < 0.25:
        x, mode, kw = lerp(-110, 260, sstep(p / 0.25)), "run", dict(swing=0.6, lean=0.15)
    elif p < 0.55:
        x, mode, kw = 260, "phone", dict(prop=phone_prop, look=-0.3)
    else:
        x, mode, kw = 260, "sit", dict(look=0.2, head_down=0.0)
    xf = lerp(110, 1400, p)
    cam = cam_lerp((150, -80, 0.95), (330, -110, 1.05), sstep(p))
    stadium(d, cam, t)
    runner(d, cam, "FUT", xf, t)
    if mode == "sit":  # a little bench appears under the old self
        bx, by = cam.p(260 - 30, LANE_Y["OLD"] - CH * 0.3)
        d.rounded_rectangle([bx - cam.s(70), by, bx + cam.s(90), by + cam.s(20)], int(cam.s(6)), fill=col((80, 70, 60, 255), 0.9))
    hx, hy = runner(d, cam, "OLD", x, t, mode=mode, **kw)
    for i, txt in enumerate(["TOO TIRED", "NOT TODAY", "I'M BUSY", "TOMORROW"]):
        k = ramp(t, dur * (0.3 + 0.15 * i), 0.25)
        bubble(d, hx + cam.s(-260 + 170 * (i % 2) * 2), hy - cam.s(300 + 80 * i), txt, k * (1 - ramp(t, dur - 0.3, 0.3)))
    top_caption(d, ["YOUR OLD SELF KNOWS", "EVERY EXCUSE."], t, dur, accent={"EVERY", "EXCUSE."})


def s3_future(d, t, dur):
    p = t / dur
    xf = lerp(1400, 2600, p)
    cam = Cam(xf + 160, -100, lerp(1.15, 1.0, p))
    shake(cam, t, 2)
    wet = ramp(t, dur * 0.2, 0.8)
    stadium(d, cam, t, wet=wet)
    runner(d, cam, "FUT", xf, t)
    # splashes at each footfall
    ph = (xf / 55) % math.pi
    if wet > 0.3 and ph < 0.6:
        fx, fy = cam.p(xf, LANE_Y["FUT"])
        r = cam.s(30) * (0.5 + ph)
        d.arc([fx - r * 2, fy - r * 0.5, fx + r * 2, fy + r * 0.5], 190, 350, fill=col((200, 225, 255, 255), 0.6 * (1 - ph / 0.6)), width=3)
    rain(d, t, wet, n=200, slant=0.35)
    top_caption(d, ["YOUR FUTURE SELF DOESN'T", "CARE ABOUT YOUR EXCUSES."], t, dur, accent={"FUTURE", "EXCUSES."})


def gap_meter(d, days, a):
    if a <= 0.01:
        return
    pill(d, W / 2, H - 120, f"THE GAP:  {days} DAYS", a, 34, inverted=False)


def _gap(d, t, dur, part):
    p = t / dur
    k = (part + p) / 2
    xf = lerp(2600, 4100, k)
    xo = 260
    # wide: the old self small in the foreground, the future self pulling away
    cam = cam_lerp((700, -60, 0.55), (1100, -60, 0.5), sstep(k))
    stadium(d, cam, t, wet=0.6)
    runner(d, cam, "FUT", xf, t, name_a=0.8)
    up = sstep(ramp(k, 0.1, 0.2))
    if up < 0.5:
        runner(d, cam, "OLD", xo, t, mode="sit", look=0.6)
    else:
        runner(d, cam, "OLD", xo, t, mode="flail" if 0.3 < k < 0.55 else "stand", phase=t * 1.5, look=0.4, mouth=-0.6)
    # a stretching line between them
    ax, ay = cam.p(xo + 40, LANE_Y["OLD"] - 220)
    bx, by = cam.p(xf - 40, LANE_Y["FUT"] - 220)
    polyline(d, [(ax, ay), (min(bx, W - 30), by)], 1, col(WHITE, 0.4), 3)
    for (x, y) in ((ax, ay), (bx, by)):
        d.ellipse([x - 6, y - 6, x + 6, y + 6], fill=col(WHITE, 0.6))
    if bx > W - 40:
        d.polygon([(W - 30, by), (W - 70, by - 26), (W - 70, by + 26)], fill=col(FUT, 0.9))
        d.text((W - 90, by), "FUTURE YOU", font=font(26), fill=col(FUT, 0.9), anchor="rm")
    gap_meter(d, int(lerp(1, 365, k ** 1.3)), ramp(t, 0.2, 0.4) if part == 0 else 1.0)
    rain(d, t, 0.6, n=120)
    if part == 0:
        top_caption(d, ["EVERY DAY YOU DELAY…"], t, dur, accent={"DELAY…"})
    else:
        top_caption(d, ["…IS ANOTHER DAY THEY", "GET FURTHER AHEAD."], t, dur, accent={"FURTHER", "AHEAD."})


def s4(d, t, dur):
    _gap(d, t, dur, 0)


def s5(d, t, dur):
    _gap(d, t, dur, 1)
s5.seamless = True


def s6_stop(d, t, dur):
    p = t / dur
    # close and low on the old self: eyes leave the other runner and drop to its own feet
    cam = cam_lerp((300, -120, 1.6), (275, -80, 2.1), sstep(p))
    stadium(d, cam, t, wet=0.4)
    down = sstep(ramp(t, dur * 0.25, 0.8))
    drop = ramp(t, dur * 0.45, 0.5)
    runner(d, cam, "OLD", 260, t, mode="stand", head_down=down * 1.4, look=-down, phase=0, name_a=0,
           prop=phone_prop if drop <= 0 else None)
    if drop > 0:  # the phone falls to the track, face down, its light going out
        fx, fy = cam.p(260 + 60, LANE_Y["OLD"])
        y = lerp(fy - cam.s(110), fy - cam.s(6), min(1, drop * 1.3))
        d.rounded_rectangle([fx - cam.s(14), y - cam.s(5), fx + cam.s(14), y + cam.s(5)], 3, fill=col((40, 50, 70, 255), 1))
        glow(d, fx, y, cam.s(40), (150, 200, 255), 0.5 * (1 - drop))
    top_caption(d, ["STOP WISHING", "YOU WERE THEM."], t, dur, accent={"WISHING"})


def s7_become(d, t, dur):
    p = t / dur
    acc = p ** 1.4
    xo = lerp(260, 3900, acc)
    xf = lerp(4100, 4380, p)
    c = mix(OLD, FUT, sstep(ramp(p, 0.25, 0.6)))
    cam = Cam(lerp(xo + 250, (xo + xf) / 2, sstep(ramp(p, 0.5, 0.5))), -80, lerp(1.05, 0.7, sstep(p)))
    shake(cam, t, 3 * p)
    stadium(d, cam, t, wet=0.3 * (1 - p), lights_on=1)
    runner(d, cam, "FUT", xf, t, a=0.85)
    runner(d, cam, "OLD", xo, t, color=c, streak=0.6 * p, glow_k=sstep(ramp(p, 0.25, 0.6)), name_a=0.9)
    top_caption(d, ["START BECOMING THEM."], t, dur, accent={"BECOMING"})


def s8_competition(d, t, dur):
    p = t / dur
    # they run side by side to the line; the future self dissolves into the runner, who finishes alone
    xo = lerp(4250, 4900, p)
    xf = lerp(4420, 4950, p)
    merge = sstep(ramp(p, 0.1, 0.4))
    cam = cam_lerp((4450, -90, 0.85), (4750, -90, 0.7), sstep(p))
    stadium(d, cam, t)
    if merge < 1:
        fx, fy = cam.p(lerp(xf, xo, merge), LANE_Y["FUT"])
        runner(d, cam, "FUT", lerp(xf, xo, merge), t, a=1 - merge, name_a=1 - merge)
        rng = random.Random(3)
        for i in range(40):  # particles drifting into the runner
            u = clamp(merge * 1.3 - rng.random() * 0.3)
            sx = lerp(fx + rng.uniform(-60, 60), cam.p(xo, 0)[0], u)
            sy = lerp(fy - rng.uniform(0, cam.s(CH)), cam.p(0, LANE_Y["OLD"])[1] - rng.uniform(0, cam.s(CH)), u)
            d.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=col(FUT, 0.8 * (1 - u) + 0.2))
    tape = ramp(p, 0.42, 0.2)
    ox, oy = runner(d, cam, "OLD", xo, t, color=FUT, glow_k=1.0, name_a=0)
    tx = cam.p(FIN, 0)[0]
    if tape < 1:
        polyline(d, [(tx, cam.p(0, -150)[1]), (tx, cam.p(0, 220)[1])], 1, col(WHITE, 0.9), 4)
    else:  # broken tape streaming behind
        for s in (-1, 1):
            polyline(d, [(tx, cam.p(0, -150 if s < 0 else 220)[1]), (tx - cam.s(120), cam.p(0, 40 + s * 40)[1])], 1, col(WHITE, 0.8), 4)
    if tape >= 1:
        glow(d, ox, oy - cam.s(100), cam.s(500), FUT, 0.5)
    overlay(d, (0, 0, 0), 0.6 * ramp(p, 0.55, 0.3))
    if p > 0.5:
        final_card(d, t - dur * 0.5, dur, ["YOUR ONLY COMPETITION", "IS WHO YOU WERE."], [WHITE, FUT], size=96, y=H / 2 - 80)
    else:
        top_caption(d, ["YOUR ONLY COMPETITION", "IS WHO YOU WERE."], t, dur, accent={"WHO", "WERE."})


SCENES = [s0_race, s1_yesterday, s2_excuses, s3_future, s4, s5, s6_stop, s7_become, s8_competition, s_follow]
