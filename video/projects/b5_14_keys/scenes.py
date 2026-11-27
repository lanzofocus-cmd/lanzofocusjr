"""THE HUNDRED FAILED KEYS — a giant lock, a mountain of keys that didn't fit, and one that did.

World: a vaulted stone chamber in teal shadow and brass light, with a colossal round vault door and lock.
THE LOCKSMITH (teal coat, glasses) tries key after key; each one flashes red and drops onto a growing pile.
Then the locksmith sits down among the failures, reads them like notes, and forges a new key out of what they
taught. The tumblers turn, the bolts slide back and light floods out.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, dust, flash)
from kit import s_follow

TITLE = ("THE HUNDRED", "FAILED KEYS")
OUTPUT = "114_The_Hundred_Failed_Keys_16x9.mp4"
LINES = [
    "",
    "",
    "Failure isn't always a dead end.",
    "Sometimes it's information.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.4, 4: 3.4}
GAPS = {2: 3.0, 3: 6.0}

BRASS = (220, 175, 90, 255)
TEAL = (60, 150, 150, 255)
SMITH = (90, 190, 180, 255)
RED = (255, 70, 60, 255)
CH = 200
DOOR = (600, -620, 560)  # centre x, centre y, radius


def chamber(d, cam, t):
    draw_sky(d, (6, 14, 16, 255), (14, 30, 32, 255))
    for k in range(-8, 10):
        x = k * 300
        d.rectangle(cam.box(x, -1500, x + 290, 0), outline=(20, 40, 42, 255), width=max(1, int(cam.s(6))))
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=(16, 26, 26, 255))
    fog(d, *cam.p(300, -300), cam.s(4000), 0.15, (150, 220, 220))


def vault(d, cam, t, turn=0.0, bolts=0.0, open_=0.0, reject=0.0):
    cx, cy, R = DOOR
    sx, sy = cam.p(cx, cy)
    r = cam.s(R)
    if open_ > 0:  # light behind the opening door
        glow(d, sx, sy, r * 2.5, (255, 230, 170), 0.8 * open_)
        d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=col((255, 225, 180, 255), 1))
        d.ellipse([sx - r * 0.25, sy - r * 0.15, sx + r * 0.25, sy + r * 0.35], fill=col((255, 245, 220, 255), 1))
        d.chord([sx - r, sy - r, sx + r, sy + r], 20, 160, fill=col((120, 170, 110, 255), 1))
        d.chord([sx - r, sy - r * 0.9, sx + r, sy + r], 40, 140, fill=col((90, 150, 90, 255), 1))
    # the door swings toward the camera (narrows horizontally and slides left)
    k = 1 - 0.85 * open_
    dx = -open_ * r * 1.1
    d.ellipse([sx - r * 1.08 + dx, sy - r * 1.08, sx - r * 1.08 + dx + 2 * r * 1.08 * k, sy + r * 1.08], fill=(70, 60, 44, 255))
    d.ellipse([sx - r + dx, sy - r, sx - r + dx + 2 * r * k, sy + r], fill=col(BRASS, 1), outline=(120, 90, 40, 255), width=max(2, int(cam.s(10))))
    ccx = sx - r + dx + r * k
    for i in range(12):  # rivets
        a = i * math.tau / 12
        rx, ry = ccx + math.cos(a) * r * 0.85 * k, sy + math.sin(a) * r * 0.85
        d.ellipse([rx - cam.s(10), ry - cam.s(10), rx + cam.s(10), ry + cam.s(10)], fill=(150, 110, 50, 255))
    # rotating dial ring with tumblers
    rr = r * 0.5
    d.ellipse([ccx - rr * k, sy - rr, ccx + rr * k, sy + rr], fill=(160, 120, 60, 255), outline=(110, 80, 36, 255), width=max(2, int(cam.s(8))))
    for i in range(8):
        a = turn * math.pi * 1.5 + i * math.tau / 8
        d.line([(ccx, sy), (ccx + math.cos(a) * rr * 0.9 * k, sy + math.sin(a) * rr * 0.9)], fill=(110, 80, 36, 255), width=max(2, int(cam.s(14))))
    d.ellipse([ccx - cam.s(40) * k, sy - cam.s(40), ccx + cam.s(40) * k, sy + cam.s(40)], fill=(30, 22, 14, 255))  # keyhole
    d.rectangle([ccx - cam.s(10) * k, sy, ccx + cam.s(10) * k, sy + cam.s(70)], fill=(30, 22, 14, 255))
    # bolts at the rim
    for side in (-1, 1):
        for j in (-1, 0, 1):
            bx = sx + side * (r * 1.02 + cam.s(60) * (1 - bolts)) + dx * (side < 0)
            by = sy + j * r * 0.45
            if open_ <= 0:
                d.rectangle([bx - cam.s(50), by - cam.s(22), bx + cam.s(50), by + cam.s(22)], fill=(170, 170, 180, 255))
    if reject > 0:
        glow(d, ccx, sy, r * 0.7, RED, 0.8 * reject)


def key_shape(d, x, y, s, ang, c, teeth=(1, 0, 1, 1, 0)):
    """A key with its bow at (x, y), shaft pointing along ang."""
    ca, sa = math.cos(ang), math.sin(ang)
    def P(u, v):
        return (x + ca * u - sa * v, y + sa * u + ca * v)
    d.ellipse([x - s * 0.35, y - s * 0.35, x + s * 0.35, y + s * 0.35], outline=c, width=max(2, int(s * 0.12)))
    d.line([P(s * 0.35, 0), P(s * 1.6, 0)], fill=c, width=max(2, int(s * 0.12)))
    for i, tt in enumerate(teeth):
        if tt:
            u = s * (1.1 + i * 0.1)
            d.line([P(u, 0), P(u, s * (0.12 + 0.12 * tt))], fill=c, width=max(1, int(s * 0.08)))


def key_pile(d, cam, n, t):
    r = random.Random(4)
    for i in range(int(n)):
        x = r.uniform(-500, 300) * (1 - i / max(n, 1) * 0.4)
        y = -r.uniform(0, 160 * (n / 100) ** 0.7) * (1 - abs(x) / 600)
        sx, sy = cam.p(x, y)
        c = mix((150, 120, 70, 255), (90, 80, 70, 255), r.random())
        key_shape(d, sx, sy, cam.s(40), r.uniform(0, 6.28), col(c, 1), tuple(r.randint(0, 2) for _ in range(5)))


def smith(d, cam, x, t, mode="reach", **kw):
    fx, fy = cam.p(x, 0)
    figure(d, fx, fy, cam.s(CH), SMITH, mode=mode, face=kw.pop("face", 1), acc=("hair", "glasses"), phase=kw.pop("phase", t * 4),
           name=kw.pop("name", "THE LOCKSMITH"), **kw)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # macro on the giant keyhole: a key slides in, turns, sparks — and the lock flashes red
    cam = Cam(DOOR[0], DOOR[1], 2.6)
    chamber(d, cam, t)
    rej = pulse(t, 1.8, 0.3)
    vault(d, cam, t, turn=0.03 * math.sin(t * 30) * rej, reject=rej)
    ins = sstep(ramp(t, 0.3, 1.0))
    kx, ky = cam.p(DOOR[0] - lerp(600, 230, ins), DOOR[1])
    key_shape(d, kx, ky, cam.s(180), 0.0 + 0.3 * pulse(t, 1.5, 0.2), col(mix(BRASS, RED, rej), 1))
    particles(d, *cam.p(DOOR[0], DOOR[1]), cam.s(300), ramp(t, 1.8, 0.8), (255, 140, 100), n=30, seed=2, rise=0.3)
    flash(d, rej * 0.6, (255, 80, 60))


def s1_montage(d, t, dur):
    p = t / dur
    # key after key, faster and faster; the pile grows; the counter runs to 99
    cam = cam_lerp((300, -400, 0.62), (250, -380, 0.7), p)
    chamber(d, cam, t)
    rate = lerp(2, 14, p)
    phase = (t * rate) % 1
    vault(d, cam, t, reject=pulse(phase, 0.6, 0.25))
    key_pile(d, cam, 99 * sstep(p), t)
    smith(d, cam, 120, t, mode="reach", look=0.5)
    n = int(1 + 98 * sstep(p))
    d.text((W - 120, H - 110), f"KEY {n}", font=font(44), fill=col(RED, 0.9), anchor="rm")
    if phase > 0.6:
        kx, ky = cam.p(DOOR[0] - 300, DOOR[1] + (phase - 0.6) * 1200)
        key_shape(d, kx, ky, cam.s(60), phase * 6, col(RED, 1))


def s2_dead_end(d, t, dur):
    p = t / dur
    # sitting among the failures; picking them up; laying them out in rows; chalk lines linking them
    cam = cam_lerp((0, -260, 0.95), (-80, -240, 1.05), sstep(p))
    chamber(d, cam, t)
    vault(d, cam, t)
    key_pile(d, cam, 99 * (1 - 0.5 * p), t)
    smith(d, cam, -250, t, mode="sit", head_down=0.5, look=-0.4, hands=None)
    # the laid-out keys and notes on the wall
    notes = ["TOO LONG", "WRONG TEETH", "TOO THIN", "ALMOST"]
    for i in range(int(4 * sstep(ramp(p, 0.1, 0.7))) + 1):
        if i >= 4:
            break
        x, y = -800 + i * 300, -520
        sx, sy = cam.p(x, y)
        key_shape(d, sx - cam.s(70), sy, cam.s(70), 0.0, col(BRASS, 1), ((1, 0, 1, 1, 0), (2, 2, 0, 1, 1), (1, 0, 0, 0, 1), (1, 1, 2, 0, 1))[i])
        d.text((sx + cam.s(20), sy + cam.s(70)), notes[i], font=font(int(cam.s(38))), fill=col((230, 240, 230, 255), 0.85), anchor="mm")
        if i > 0:
            polyline(d, [cam.p(x - 260 + 120, y + 30), cam.p(x - 60, y + 30)], ramp(p, 0.2 + i * 0.15, 0.2), col(WHITE, 0.5), 2)
    top_caption(d, ["FAILURE ISN'T ALWAYS", "A DEAD END."], t, dur, accent={"DEAD", "END."})


def s3_information(d, t, dur):
    p = t / dur
    # forge the new key from the lessons, insert it — the tumblers turn, bolts slide, the door swings open
    forge = sstep(ramp(p, 0.0, 0.25))
    ins = sstep(ramp(p, 0.25, 0.15))
    turn = sstep(ramp(p, 0.4, 0.2))
    bolts = sstep(ramp(p, 0.55, 0.15))
    open_ = sstep(ramp(p, 0.7, 0.3))
    cam = cam_lerp((200, -400, 0.7), (DOOR[0], DOOR[1], 0.75 + 0.6 * open_), sstep(ramp(p, 0.2, 0.8)))
    chamber(d, cam, t)
    vault(d, cam, t, turn=turn, bolts=bolts, open_=open_)
    key_pile(d, cam, 50, t)
    if p < 0.25:
        smith(d, cam, 100, t, mode="hammer", phase=t * 7)
        sx, sy = cam.p(220, -160)
        glow(d, sx, sy, cam.s(160), (255, 220, 150), 0.8)
        key_shape(d, sx, sy, cam.s(70), 0.0, col((255, 240, 200, 255), 1), (2, 1, 1, 2, 1))
        particles(d, sx, sy, cam.s(160), (t * 3) % 1, (255, 220, 150), n=12, seed=int(t * 3), rise=0.4)
    else:
        smith(d, cam, 250, t, mode="reach" if open_ < 0.5 else "cheer", mouth=0.6 * open_)
        if open_ < 0.3:
            ccx, cy = cam.p(DOOR[0], DOOR[1])
            kx = ccx - cam.s(lerp(500, 170, ins))
            key_shape(d, kx, cy, cam.s(110), turn * math.pi / 2, col((255, 240, 200, 255), 1), (2, 1, 1, 2, 1))
            glow(d, kx, cy, cam.s(120), (255, 230, 170), 0.6)
    if open_ > 0.3:
        dust(d, t, 0.7, n=60, color=(255, 230, 180))
    top_caption(d, ["SOMETIMES IT'S", "INFORMATION."], t, dur, accent={"INFORMATION."})


def s4_end(d, t, dur):
    cam = Cam(DOOR[0], DOOR[1], 1.35)
    chamber(d, cam, t)
    vault(d, cam, t, turn=1, bolts=1, open_=1)
    stage_end(d, t, dur, ["FAILURE IS", "INFORMATION."], [WHITE, BRASS], size=110, dim=0.45, glow_col=BRASS)


SCENES = [s0_hook, s1_montage, s2_dead_end, s3_information, s4_end, s_follow]
