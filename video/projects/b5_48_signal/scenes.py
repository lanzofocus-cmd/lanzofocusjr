"""THE SIGNAL — every action is a transmission; the future is the receiver.

World: a neon night far in the future. On a rooftop antenna in a dense cyan city, THE SENDER (cyan) works: every
push-up, every hammer swing, every page sends a ring of signal into the sky. Across a dark valley of red STATIC (the
NOISE: glitchy jagged interference, scrolling, excuses) a lonely relay tower on a far ridge waits, with a gold
silhouette at its console: THE RECEIVER. Single pulses scatter in the static. Kept up, they fuse into one solid beam
that cuts through the noise; the console lights MESSAGE RECEIVED and the gold figure, the sender years later, smiles.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, dust, stars)
from kit import s_follow

TITLE = ("THE", "SIGNAL")
OUTPUT = "148_The_Signal_16x9.mp4"
LINES = [
    "",
    "",
    "Your actions are sending a message.",
    "Make sure your future receives it.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.6, 4: 3.4}
GAPS = {2: 3.6, 3: 6.6}

CYAN = (80, 220, 255, 255)
NOISE = (255, 60, 100, 255)
GOLD = (255, 200, 90, 255)
CH = 200
SEND = (80, -1020)     # antenna tip
RECV = (5200, -1180)   # relay dish
NOISE_X = (1500, 3700)


def path(u):
    x = lerp(SEND[0], RECV[0], u)
    y = lerp(SEND[1], RECV[1], u) - math.sin(math.pi * u) * 500
    return x, y


def world(d, cam, t, noise=1.0, lit=0.0):
    draw_sky(d, (8, 6, 30, 255), mix((40, 20, 80, 255), (90, 60, 60, 255), lit))
    stars(d, 0.8)
    # far ridge with the relay tower
    ridge = [cam.p(x, -700 + math.sin(x * 0.0012) * 120 - max(0, x - 4200) * 0.25) for x in range(-2000, 7001, 200)]
    d.polygon(ridge + [cam.p(7000, 2000), cam.p(-2000, 2000)], fill=(18, 14, 40, 255))
    tx, ty = cam.p(RECV[0], -900)
    bx, by = cam.p(RECV[0], RECV[1] + 60)
    lw = max(2, int(cam.s(14)))
    d.line([cam.p(RECV[0] - 120, -930), (bx, by), cam.p(RECV[0] + 120, -930)], fill=(60, 50, 90, 255), width=lw)
    d.line([cam.p(RECV[0], -930), (bx, by)], fill=(60, 50, 90, 255), width=lw)
    r = cam.s(90)
    dx, dy = cam.p(*RECV)
    d.chord([dx - r, dy - r, dx + r, dy + r], 120, 300, fill=mix((70, 60, 100, 255), GOLD, lit))
    glow(d, dx, dy, r * 3, GOLD[:3], 0.15 + 0.6 * lit)
    # cabin with console window and the receiver in it
    a, b = cam.p(RECV[0] - 260, -1050), cam.p(RECV[0] - 40, -900)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(30, 26, 50, 255))
    d.rectangle([a[0] + cam.s(20), a[1] + cam.s(20), b[0] - cam.s(20), a[1] + cam.s(90)], fill=mix((40, 40, 70, 255), GOLD, lit * 0.8))
    # the city in front, left, with neon rooftops
    rr = random.Random(2)
    for i in range(-14, 8):
        x = i * 170
        h = rr.uniform(350, 900) if i != 0 else 520
        q0, q1 = cam.p(x - 80, -h), cam.p(x + 80, 400)
        d.rectangle([q0[0], q0[1], q1[0], q1[1]], fill=(14, 20, 40, 255))
        d.line([q0, (q1[0], q0[1])], fill=col(CYAN if i % 3 else (255, 90, 200, 255), 0.8), width=max(1, int(cam.s(4))))
        for k in range(int(h // 70)):
            if rr.random() < 0.3:
                w0, w1 = cam.p(x - 50 + rr.choice((0, 50)), -h + 40 + k * 70), cam.p(x - 20 + rr.choice((0, 50)), -h + 60 + k * 70)
                d.rectangle([w0[0], w0[1], w1[0], w1[1]], fill=(60, 200, 255, 255) if rr.random() < 0.6 else (255, 120, 220, 255))
    # sender's rooftop + antenna
    d.rectangle(cam.box(-150, -520, 260, 400), fill=(20, 26, 50, 255))
    d.line([cam.p(80, -520), cam.p(*SEND)], fill=(150, 170, 200, 255), width=max(2, int(cam.s(10))))
    for k in range(4):
        y = -620 - k * 100
        d.line([cam.p(80 - 60 + k * 10, y), cam.p(80 + 60 - k * 10, y)], fill=(150, 170, 200, 255), width=max(1, int(cam.s(6))))
    sx, sy = cam.p(*SEND)
    glow(d, sx, sy, cam.s(80), CYAN[:3], 0.6 + 0.3 * math.sin(t * 6))
    d.ellipse([sx - cam.s(12), sy - cam.s(12), sx + cam.s(12), sy + cam.s(12)], fill=CYAN)
    if noise > 0:
        static(d, cam, t, noise)


def static(d, cam, t, a):
    """The valley of noise: flickering jagged red interference and glitch blocks."""
    r = random.Random(int(t * 12))
    x0, x1 = NOISE_X
    for i in range(int(60 * a)):
        x = r.uniform(x0, x1)
        y = r.uniform(-1700, -600)
        pts = [cam.p(x + j * 40, y + r.uniform(-40, 40)) for j in range(r.randint(3, 7))]
        polyline(d, pts, 1, col(NOISE, r.uniform(0.3, 0.8) * a), max(1, int(cam.s(5))))
    for i in range(int(14 * a)):
        x, y = r.uniform(x0, x1), r.uniform(-1700, -600)
        q0, q1 = cam.p(x, y), cam.p(x + r.uniform(60, 220), y + r.uniform(10, 40))
        tpoly(d, [q0, (q1[0], q0[1]), q1, (q0[0], q1[1])], (255, 80, 120, int(110 * a)))
    cx, cy = cam.p((x0 + x1) / 2, -1150)
    glow(d, cx, cy, cam.s(1300), NOISE[:3], 0.18 * a)
    if cam.s(40) > 10:
        for wd, (fx_, fy_) in zip(("SCROLL", "LATER", "EXCUSE", "TOMORROW", "SKIP", "MEH"),
                                  ((0.45, 0.75), (0.85, 0.3), (0.3, 0.2), (0.15, 0.55), (0.7, 0.62), (0.6, 0.15))):
            x, y = lerp(x0 + 200, x1 - 200, fx_), lerp(-1600, -750, fy_)
            jx = r.uniform(-6, 6)
            sx, sy = cam.p(x, y)
            d.text((sx + jx, sy), wd, font=font(max(10, int(cam.s(120)))), fill=col(NOISE, 0.55 * a), anchor="mm")


def ring(d, cam, u, t, strength=1.0, a=1.0):
    """One pulse travelling along the path at u; inside the noise a weak pulse jitters and dissolves."""
    if not 0 <= u <= 1:
        return
    x, y = path(u)
    inside = NOISE_X[0] < x < NOISE_X[1]
    dissolve = 0.0
    if inside and strength < 1:
        dissolve = clamp((x - NOISE_X[0]) / 700) * (1 - strength)
    aa = a * (1 - dissolve)
    if aa <= 0.03:
        return
    sx, sy = cam.p(x, y)
    for k in range(3):
        R = cam.s(130 + k * 80)
        j = random.Random(int(t * 30) + k).uniform(-1, 1) * cam.s(30) * dissolve
        d.arc([sx - R + j, sy - R, sx + R + j, sy + R], -55, 55, fill=col(CYAN, aa * (1 - 0.25 * k)), width=max(2, int(cam.s(10))))
    glow(d, sx, sy, cam.s(160), CYAN[:3], 0.35 * aa)


def beam(d, cam, k, t):
    """The fused beam from antenna to dish, drawn to fraction k of the path."""
    if k <= 0:
        return
    pts = [cam.p(*path(u / 60 * k)) for u in range(61)]
    for w, a in ((40, 0.15), (18, 0.4), (6, 1.0)):
        polyline(d, pts, 1, col(CYAN, a), max(1, int(cam.s(w))))
    hx, hy = pts[-1]
    glow(d, hx, hy, cam.s(260), CYAN[:3], 0.6)


def hud(d, t, bars, label, col_=CYAN, wave=1.0):
    """Bottom-left signal readout: strength bars and a little waveform."""
    x0, y0 = 70, H - 170
    d.rounded_rectangle([x0 - 20, y0 - 30, x0 + 420, y0 + 110], 14, fill=(5, 10, 25, 200), outline=col(col_, 0.6), width=2)
    for i in range(6):
        on = i < bars
        h = 20 + i * 12
        d.rectangle([x0 + i * 26, y0 + 70 - h, x0 + i * 26 + 18, y0 + 70], fill=col(col_, 1 if on else 0.18))
    pts = [(x0 + 180 + i * 4, y0 + 30 + math.sin(i * 0.4 + t * 8) * 22 * wave * (0.4 + 0.6 * random.Random(int(t * 10) + i).random())) for i in range(55)]
    polyline(d, pts, 1, col(col_, 0.9), 2)
    d.text((x0, y0 + 92), label, font=font(24), fill=col(col_, 0.9), anchor="lm")


def sender(d, cam, t, mode="hammer", **kw):
    fx, fy = cam.p(-20, -520)
    figure(d, fx, fy, cam.s(CH), CYAN, mode=mode, phase=kw.pop("phase", t * 6), face=kw.pop("face", 1), acc=("headband",),
           name=kw.pop("name", "THE SENDER"), eye_col=(10, 30, 60, 255), **kw)


def receiver(d, cam, t, lit=0.0, **kw):
    fx, fy = cam.p(RECV[0] - 150, -900)
    figure(d, fx, fy, cam.s(CH * 0.9), mix((120, 110, 90, 255), GOLD, lit), mode=kw.pop("mode", "stand"), phase=t * 4, face=-1,
           acc=("headband",), name=kw.pop("name", "THE RECEIVER"), eye_col=(60, 40, 10, 255), **kw)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # black screen, a flat oscilloscope line; one blip; a second; HUD: SEARCHING
    d.rectangle([0, 0, W, H], fill=(3, 6, 14, 255))
    for k in range(0, H, 6):
        d.line([(0, k), (W, k)], fill=(10, 18, 30, 255))
    pts = []
    for i in range(0, W + 1, 8):
        u = i / W
        blip = 0.0
        for c in (0.35 + (t * 0.25) % 1, 0.75 + (t * 0.25) % 1):
            blip += math.exp(-((u - (c % 1)) / 0.01) ** 2) * (1 if t > 1.0 else 0)
        pts.append((i, H / 2 - blip * 180 * math.sin(i * 0.3)))
    polyline(d, pts, 1, CYAN, 4)
    glow(d, W / 2, H / 2, 600, CYAN[:3], 0.1)
    d.text((W / 2, H * 0.68), "SIGNAL: SEARCHING" + "." * (int(t * 3) % 4), font=font(34), fill=col(CYAN, 0.8), anchor="mm")


def s1_noise(d, t, dur):
    p = t / dur
    # wide: the city antenna on the left, a far gold tower on the right, the red static valley between;
    # a single pulse goes out and scatters in the noise
    cam = cam_lerp((300, -800, 0.85), (2650, -950, 0.36), sstep(ramp(p, 0.0, 0.6)))
    world(d, cam, t)
    sender(d, cam, t, mode="hammer")
    receiver(d, cam, t)
    for k, t0 in enumerate((0.15, 0.55)):
        ring(d, cam, (p - t0) * 1.2, t, strength=0.2)
    hud(d, t, 1, "SIGNAL  WEAK", NOISE, wave=1.4)


def s2_actions(d, t, dur):
    p = t / dur
    # a montage on the rooftop: push-ups, hammer, reading; each action sends a ring; more get further; bars climb
    phase = int(p * 3)
    mode = ("crouch", "hammer", "carry")[min(2, phase)]
    if p < 0.55:
        cam = Cam(120, -720, 1.05)
    else:
        cam = cam_lerp((120, -720, 1.05), (2650, -950, 0.36), sstep(ramp(p, 0.55, 0.4)))
    world(d, cam, t, noise=1 - 0.3 * p)
    sender(d, cam, t, mode=mode, mouth=0.4)
    receiver(d, cam, t)
    for k in range(10):
        t0 = k * 0.09
        ring(d, cam, (p - t0) * 1.3, t, strength=clamp(k / 9) * 0.9)
    hud(d, t, 1 + int(4 * p), "SIGNAL  " + ("WEAK" if p < 0.5 else "RISING"), mix(NOISE, CYAN, p), wave=1.4 - p)
    top_caption(d, ["YOUR ACTIONS ARE", "SENDING A MESSAGE."], t, dur, accent={"ACTIONS", "MESSAGE."})


def s3_receive(d, t, dur):
    p = t / dur
    # pulses fuse into one beam that burns through the static; the dish lights; close on the receiver's console
    k = sstep(ramp(p, 0.0, 0.4))
    lit = sstep(ramp(p, 0.35, 0.15))
    if p < 0.45:
        cam = Cam(2650, -950, 0.36)
    else:
        cam = cam_lerp((2650, -950, 0.36), (RECV[0] - 250, -1050, 1.1), sstep(ramp(p, 0.45, 0.35)))
    world(d, cam, t, noise=1 - 0.85 * k, lit=lit)
    sender(d, cam, t, mode="hammer", name="")
    beam(d, cam, k, t)
    receiver(d, cam, t, lit=lit, mode="cheer" if p > 0.75 else "stand", mouth=0.7 * lit, name="THE RECEIVER" if p > 0.6 else "")
    if p > 0.6:
        a, b = cam.p(RECV[0] - 240, -1030), cam.p(RECV[0] - 60, -960)
        if b[0] - a[0] > 60:
            d.text(((a[0] + b[0]) / 2, (a[1] + b[1]) / 2), "MESSAGE RECEIVED", font=font(max(10, int((b[0] - a[0]) / 10))), fill=(40, 25, 0, 255), anchor="mm")
    hud(d, t, 6 if k > 0.9 else 4, "CONNECTED" if lit > 0.5 else "LOCKING...", CYAN if lit < 0.5 else GOLD, wave=0.4)
    top_caption(d, ["MAKE SURE YOUR FUTURE", "RECEIVES IT."], t, dur, accent={"FUTURE", "RECEIVES"})


def s4_end(d, t, dur):
    cam = Cam(2650, -950, 0.36)
    world(d, cam, t, noise=0.15, lit=1.0)
    sender(d, cam, t, mode="stand", name="")
    beam(d, cam, 1.0, t)
    receiver(d, cam, t, lit=1.0, mode="cheer", name="")
    stage_end(d, t, dur, ["SEND THE", "RIGHT SIGNAL."], [WHITE, CYAN], size=110, dim=0.45, glow_col=CYAN[:3], y=H * 0.3)


SCENES = [s0_hook, s1_noise, s2_actions, s3_receive, s4_end, s_follow]
