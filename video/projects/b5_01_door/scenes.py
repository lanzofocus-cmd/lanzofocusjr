"""THE DOOR THAT NEVER OPENED — a vast dark hallway of doors that appear, wait, and turn to dust.

World: an endless corridor of black stone, cold blue haze, doors outlined in warm light. OPPORTUNITY is a gold
figure who holds a door ajar; REGRET is a grey hooded shade that grows after every missed door. The last door
opens onto a bright world of green hills and morning light.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, PCam, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, shade,
                   back_figure, particles, top_caption, final_card, shake, darkness, sun, cloud, word_reveal)
from kit import s_follow

TITLE = ("THE DOOR THAT", "NEVER OPENED")
OUTPUT = "101_The_Door_That_Never_Opened_16x9.mp4"
LINES = [
    "",
    "Some opportunities don't wait forever.",
    "",
    "Eventually, the door stops appearing.",
    "Stop waiting for permission.",
    "Knock. Push. Move.",
    "",
]
SILENT = {0: 3.2, 2: 2.6}
GAPS = {1: 1.0, 3: 1.4, 4: 0.8, 5: 3.8}

STONE = (14, 16, 24, 255)
HAZE = (110, 130, 200)
WARM = (255, 200, 130, 255)
OPP = (255, 205, 110, 255)
REG = (120, 120, 140, 255)
YOU = (232, 228, 222, 255)
CH = 220


def hall_side(d, cam, t, light=1.0):
    """Side view: the long wall with door frames, floor and the cold haze."""
    draw_sky(d, (4, 4, 8, 255), (16, 18, 30, 255))
    for k in range(-10, 14):
        x = k * 360
        a, b = cam.p(x, -1300), cam.p(x + 40, 0)
        d.rectangle([a[0], a[1], b[0], b[1]], fill=col((22, 24, 36, 255), light))  # pillars
    fy = cam.p(0, 0)[1]
    if fy < H:
        d.rectangle([0, fy, W, H], fill=(10, 10, 16, 255))
    d.line([(0, fy), (W, fy)], fill=col(HAZE + (255,), 0.25), width=2)
    fog(d, *cam.p(0, -100), cam.s(5000), 0.15, HAZE)


def door(d, cam, x, t, open_=0.0, a=1.0, dust=0.0, w=300, h=620, glowk=1.0, light_col=WARM):
    """A door standing on the floor at x (left edge). open_: 0..1 swing. dust: 0..1 crumbling."""
    if a <= 0.01 and dust <= 0:
        return
    x0, x1, y0 = x, x + w, -h
    aa = a * (1 - dust)
    # frame and the light leaking around it
    glow(d, *cam.p(x + w / 2, -h / 2), cam.s(500), light_col, 0.45 * aa * glowk)
    d.rectangle(cam.box(x0 - 30, y0 - 30, x1 + 30, 0), fill=col((40, 34, 30, 255), aa))
    d.rectangle(cam.box(x0, y0, x1, 0), fill=col((255, 236, 200, 255), aa * (0.3 + 0.7 * open_)))
    # the leaf, swinging inward (narrows as it opens)
    lw = w * (1 - open_ * 0.85)
    d.rectangle(cam.box(x0, y0, x0 + lw, 0), fill=col((60, 44, 34, 255), aa))
    for py in (-h * 0.8, -h * 0.4):
        d.rectangle(cam.box(x0 + lw * 0.12, py, x0 + lw * 0.88, py + h * 0.3), outline=col((90, 70, 54, 255), aa), width=max(1, int(cam.s(4))))
    kx, ky = cam.p(x0 + lw * 0.85, -h * 0.47)
    d.ellipse([kx - cam.s(10), ky - cam.s(10), kx + cam.s(10), ky + cam.s(10)], fill=col(OPP, aa))
    # light under the door
    d.rectangle(cam.box(x0, -8, x1, 0), fill=col(WARM, aa * 0.9))
    if dust > 0:
        particles(d, *cam.p(x + w / 2, -h / 2), cam.s(500), dust, (200, 190, 170), n=80, seed=int(x), rise=0.6)


def s0_hook(d, t, dur):
    p = t / dur
    # black; a door slams into existence; a lone figure waits in front of it
    cam = cam_lerp((250, -360, 1.05), (220, -340, 0.9), sstep(p))
    hit = pulse(t, 0.6, 0.12)
    shake(cam, t, 14 * hit)
    hall_side(d, cam, t)
    door(d, cam, 380, t, a=ramp(t, 0.5, 0.1))
    fx, fy = cam.p(150, 0)
    figure(d, fx, fy, cam.s(CH), YOU, mode="stand", face=1, acc=("hair",), look=0.2, phase=0)
    darkness(d, W / 2, H / 2, 0.55)
    overlay(d, (0, 0, 0), 1 - ramp(t, 0.5, 0.1))
    if t > 1.2:  # waiting: a slow tap of the foot, the clock of patience
        d.text((W - 160, H - 120), "WAITING…", font=font(30), fill=col(GREY, 0.6 * ramp(t, 1.2, 0.4)), anchor="rm")


def s1_opportunity(d, t, dur):
    p = t / dur
    # Opportunity opens the door from inside and beckons. The person steps back instead of forward.
    cam = cam_lerp((260, -360, 0.95), (300, -360, 1.1), sstep(p))
    hall_side(d, cam, t)
    op = sstep(ramp(t, 0.2, 0.8))
    door(d, cam, 380, t, open_=op * 0.7)
    ox, oy = cam.p(520, 0)
    glow(d, ox, oy - cam.s(110), cam.s(300), OPP, 0.6 * op)
    figure(d, ox, oy, cam.s(CH), OPP, mode="reach" if p > 0.35 else "stand", face=-1, a=op, name="OPPORTUNITY", name_a=op,
           eye_col=(90, 60, 10, 255), mouth=0.6)
    back = sstep(ramp(t, dur * 0.5, 0.6))
    fx, fy = cam.p(150 - 90 * back, 0)
    figure(d, fx, fy, cam.s(CH), YOU, mode="stand", face=1, acc=("hair",), lean=-0.15 * back, look=0.1, mouth=-0.3)
    darkness(d, W / 2, H / 2, 0.45)
    top_caption(d, ["SOME OPPORTUNITIES", "DON'T WAIT FOREVER."], t, dur, accent={"OPPORTUNITIES", "FOREVER."})


def s2_dust(d, t, dur):
    p = t / dur
    # the door closes, then crumbles to dust; Regret rises out of it
    cam = cam_lerp((300, -360, 1.1), (200, -360, 0.85), sstep(p))
    hall_side(d, cam, t)
    close = sstep(ramp(t, 0.0, 0.5))
    dust = ramp(t, 0.7, 1.4)
    door(d, cam, 380, t, open_=0.7 * (1 - close), dust=dust, a=1.0)
    ox, oy = cam.p(520, 0)
    figure(d, ox, oy, cam.s(CH), OPP, mode="stand", face=-1, a=1 - close)
    rg = ramp(t, 1.2, 0.8)
    shade(d, *cam.p(-60, 20), cam.s(300), REG, rg, t, name="REGRET", name_a=rg)
    fx, fy = cam.p(60, 0)
    figure(d, fx, fy, cam.s(CH), YOU, mode="stand" if p < 0.5 else "slump", face=1, acc=("hair",), head_down=0.5 * p)
    darkness(d, W / 2, H / 2, 0.5)


def corridor(d, cam, t, doors, regret=0.0, walker_z=0.0, walker_phase=0.0, walk_speed=0.7, end_door=0.0, end_open=0.0, run=False):
    """One-point perspective down the endless hall. doors: list of (z, side, state 0..1 visible, dust)."""
    draw_sky(d, (2, 2, 6, 255), (10, 12, 22, 255))
    W2, HH = 700, 1300
    far = cam.z + 9000
    # floor, walls, ceiling as receding quads
    for pts, c in (([(-W2, cam.z + 60, 0), (W2, cam.z + 60, 0), (W2, far, 0), (-W2, far, 0)], (12, 12, 18)),
                   ([(-W2, cam.z + 60, 0), (-W2, far, 0), (-W2, far, HH), (-W2, cam.z + 60, HH)], (18, 20, 30)),
                   ([(W2, cam.z + 60, 0), (W2, far, 0), (W2, far, HH), (W2, cam.z + 60, HH)], (18, 20, 30)),
                   ([(-W2, cam.z + 60, HH), (W2, cam.z + 60, HH), (W2, far, HH), (-W2, far, HH)], (8, 8, 12))):
        q = cam.quad(pts)
        if q:
            d.polygon(q, fill=c + (255,))
    # ribs every 600 units
    z0 = math.floor(cam.z / 600) * 600
    for k in range(1, 16):
        z = z0 + k * 600
        q = cam.quad([(-W2, z, 0), (-W2, z, HH), (W2, z, HH), (W2, z, 0)])
        if q:
            polyline(d, q, 1, col(HAZE + (255,), 0.12), 2)
    # far end: darkness, or the last door glowing
    fe = cam.p(0, far)
    if end_door > 0:
        zd = cam.z + 4200 - 2600 * end_door
        q = cam.quad([(-180, zd, 0), (-180, zd, 560), (180, zd, 560), (180, zd, 0)])
        if q:
            glow(d, (q[0][0] + q[2][0]) / 2, (q[0][1] + q[1][1]) / 2, abs(q[2][0] - q[0][0]) * 2.2, WARM, 0.7)
            d.polygon(q, fill=col((255, 236, 200, 255), 0.4 + 0.6 * end_open))
            lw = 1 - end_open * 0.9
            leaf = cam.quad([(-180, zd, 0), (-180, zd, 560), (-180 + 360 * lw, zd, 560), (-180 + 360 * lw, zd, 0)])
            if leaf and lw > 0.05:
                d.polygon(leaf, fill=(60, 44, 34, 255))
    # side doors
    for z, side, vis, dust in sorted(doors, key=lambda q: -q[0]):
        x = side * W2
        q = cam.quad([(x, z, 0), (x, z, 560), (x, z + 330, 560), (x, z + 330, 0)])
        if not q:
            continue
        aa = vis * (1 - dust)
        if aa > 0.01:
            cx, cy = sum(v[0] for v in q) / 4, sum(v[1] for v in q) / 4
            glow(d, cx, cy, abs(q[2][0] - q[0][0]) * 3 + 40, WARM, 0.5 * aa)
            tpoly(d, q, col((90, 66, 50, 255), aa))
            polyline(d, q + [q[0]], 1, col(WARM, aa), 3)
        if dust > 0:
            cx, cy = sum(v[0] for v in q) / 4, sum(v[1] for v in q) / 4
            particles(d, cx, cy, abs(q[2][0] - q[0][0]) * 2 + 60, dust, (200, 190, 170), n=50, seed=int(z), rise=0.4)
    # the person (from behind), and Regret behind them
    p = cam.p(0, walker_z)
    if p:
        sx, sy, s = p
        back_figure(d, sx, sy, CH * s, YOU, t, walker_phase, walk_speed * (1.6 if run else 1), acc=("scarf",))
    if regret > 0:
        rp = cam.p(-260, walker_z - 300)
        if rp:
            shade(d, rp[0], rp[1], 300 * rp[2] * (0.6 + regret), REG, 0.7 * regret, t, eyes=True, name="REGRET", name_a=0.6 * regret)
    fog(d, W / 2, cam.horizon, 2600, 0.12, HAZE)


def s3_stops(d, t, dur):
    p = t / dur
    # walking the endless hall: door after door lights up ahead and crumbles before it is reached
    wz = 600 + 2800 * p
    cam = PCam(80, wz - 700, 420, horizon=H * 0.45)
    doors = []
    for i in range(8):
        z = 900 + i * 520
        side = -1 if i % 2 else 1
        appear = ramp(wz, z - 1600, 300)
        dust = ramp(wz, z - 700, 400)
        doors.append((z, side, appear, dust))
    corridor(d, cam, t, doors, regret=0.4 + 0.6 * p, walker_z=wz, walker_phase=t * 4.5, walk_speed=0.6)
    top_caption(d, ["EVENTUALLY, THE DOOR", "STOPS APPEARING."], t, dur, accent={"STOPS"})


def s4_permission(d, t, dur):
    p = t / dur
    # one last door, far away. The person breaks into a run.
    wz = 3400 + 1400 * sstep(p)
    cam = PCam(0, wz - 700, 380, horizon=H * 0.45)
    corridor(d, cam, t, [], regret=1 - p, walker_z=wz, walker_phase=t * 8, walk_speed=1.0, end_door=ramp(t, 0.0, 0.6) * 0.5 + 0.5 * p, run=True)
    top_caption(d, ["STOP WAITING", "FOR PERMISSION."], t, dur, accent={"PERMISSION."})


def world_beyond(d, t, k):
    """The bright world through the door."""
    draw_sky(d, (110, 170, 240, 255), (255, 225, 190, 255))
    sun(d, W * 0.7, H * 0.38, 90, 1.0, (255, 235, 180, 255))
    for i, (yy, c) in enumerate(((0.62, (120, 180, 120)), (0.7, (90, 160, 100)), (0.8, (70, 140, 80)))):
        pts = [(0, H)]
        for j in range(25):
            x = j * W / 24
            pts.append((x, H * yy - 40 * math.sin(j * 0.7 + i * 2 + t * 0.1) - 20 * i))
        pts.append((W, H))
        d.polygon(pts, fill=c + (255,))
    for j in range(5):
        cloud(d, (j * 470 + t * 20) % (W + 400) - 200, 160 + 40 * (j % 2), 60, col(WHITE, 0.8))


def s5_knock(d, t, dur):
    p = t / dur
    # knock, knock, knock — push — and the camera flies through the open door into the light
    knocks = [0.25, 0.55, 0.85]
    hit = max(pulse(t, k, 0.08) for k in knocks)
    openk = sstep(ramp(t, 1.3, 0.8))
    fly = sstep(ramp(t, 1.9, 1.4))
    if fly < 1:
        cam = PCam(0, 4800 - 700 + 1400 * fly, 380 - 100 * fly, horizon=H * 0.45)
        shake_off = 10 * hit
        cam.x += math.sin(t * 60) * shake_off
        corridor(d, cam, t, [], walker_z=4800 + 900 * fly, walker_phase=0 if openk < 1 else t * 5, walk_speed=0 if openk < 1 else 0.7,
                 end_door=1.0, end_open=openk)
        overlay(d, (255, 240, 210), clamp(fly * 1.4 - 0.4))
    else:
        world_beyond(d, t, 1)
        fx = lerp(W * 0.4, W * 0.55, ramp(t, 1.9 + 1.4, dur))
        figure(d, fx, H * 0.78, 200, YOU, mode="walk", phase=t * 5, face=1, acc=("hair", "scarf"), look=0.3)
        overlay(d, (255, 240, 210), 1 - ramp(t, 3.3, 0.6))
    words = ["KNOCK.", "PUSH.", "MOVE."]
    times = [0.25, 1.3, 2.0]
    f = font(120)
    x = W / 2 - sum(d.textlength(w + " ", font=f) for w in words) / 2
    for w, tt in zip(words, times):
        k = ramp(t, tt, 0.25)
        tc = mix(WHITE, (40, 40, 60, 255), clamp(fly * 2 - 0.3))
        d.text((x, 170 + (1 - k) * 14), w, font=f, fill=col(tc, k), anchor="lm")
        x += d.textlength(w + " ", font=f)


SCENES = [s0_hook, s1_opportunity, s2_dust, s3_stops, s4_permission, s5_knock, s_follow]
