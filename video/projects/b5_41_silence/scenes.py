"""THE TOWER OF SILENCE — noise drawn as something you can see, and a quiet room that lets a tower grow.

World: a plain at dusk filled with visible noise: jagged magenta and orange sound waves, shouting speech bubbles,
a swarm of loudspeaker-shaped NOISE creatures that bump into everything. THE BUILDER (teal) can't lay two bricks
without being knocked over. So they build a small domed room of SILENCE and step inside: the waves flatten into
one calm line, they work, and outside a tower rises while the noise bounces off the dome.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, sun, dust)
from kit import s_follow

TITLE = ("THE TOWER", "OF SILENCE")
OUTPUT = "141_The_Tower_Of_Silence_16x9.mp4"
LINES = [
    "",
    "",
    "",
    "Not every voice deserves your attention.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.4, 2: 3.4, 4: 3.4}
GAPS = {3: 6.4}

NOISE = (255, 80, 180, 255)
NOISE2 = (255, 150, 60, 255)
CALM = (120, 200, 255, 255)
BUILD = (80, 210, 190, 255)
WORDS = ["HEY!", "LOOK!", "PING", "LISTEN!", "NOW!", "BREAKING", "WOW", "??!", "SALE!", "SCROLL"]
CH = 200


def plain(d, cam, t, dusk=0.0):
    draw_sky(d, mix((60, 40, 80, 255), (30, 50, 90, 255), dusk), mix((255, 160, 130, 255), (180, 140, 200, 255), dusk))
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=(70, 60, 74, 255))


def waves(d, t, amp=1.0, calm=0.0, region=None, seed=1):
    """Jagged sound waves across the frame (or a region), flattening as calm -> 1."""
    x0, y0, x1, y1 = region or (0, 0, W, H)
    r = random.Random(seed)
    for k in range(7):
        yb = lerp(y0, y1, (k + 0.5) / 7)
        pts = []
        for i in range(0, int(x1 - x0) + 30, 30):
            x = x0 + i
            j = (math.sin(i * 0.05 + t * (6 + k) + k) + 0.6 * math.sin(i * 0.13 - t * 9 + k * 2)) * amp * (1 - calm)
            pts.append((x, yb + j * 50 * r.uniform(0.6, 1.4)))
        c = mix(NOISE if k % 2 else NOISE2, CALM, calm)
        polyline(d, pts, 1, col(c, 0.5), 3)


def bubbles(d, t, a=1.0, region=None, n=10):
    x0, y0, x1, y1 = region or (0, 0, W, H)
    r = random.Random(4)
    for i in range(n):
        ph = (t * r.uniform(0.3, 0.7) + r.random()) % 1
        x = lerp(x0, x1, r.random())
        y = lerp(y0, y1, r.random()) - ph * 80
        k = math.sin(math.pi * ph) * a
        if k <= 0.05:
            continue
        txt = WORDS[i % len(WORDS)]
        f = font(36)
        tw = d.textlength(txt, font=f)
        d.rounded_rectangle([x - tw / 2 - 18, y - 30, x + tw / 2 + 18, y + 30], 24, fill=col((40, 20, 40, 255), 0.9 * k), outline=col(NOISE, k), width=3)
        d.text((x, y), txt, font=f, fill=col(WHITE, k), anchor="mm")


def speaker(d, cam, x, y, t, s=1.0, a=1.0):
    sx, sy = cam.p(x, y)
    w = cam.s(70 * s)
    d.polygon([(sx - w * 0.6, sy - w * 0.35), (sx, sy - w * 0.35), (sx + w, sy - w), (sx + w, sy + w), (sx, sy + w * 0.35), (sx - w * 0.6, sy + w * 0.35)], fill=col(NOISE, a))
    for k in range(3):
        rr = w * (1.3 + 0.5 * k + 0.3 * ((t * 3) % 1))
        d.arc([sx + w - rr, sy - rr, sx + w + rr, sy + rr], -40, 40, fill=col(NOISE2, a * (0.8 - 0.2 * k)), width=max(2, int(w * 0.08)))
    for o in (-1, 1):
        d.ellipse([sx - w * 0.35 + o * w * 0.12 - w * 0.06, sy - w * 0.12, sx - w * 0.35 + o * w * 0.12 + w * 0.06, sy], fill=(30, 10, 30, int(255 * a)))


def swarm(d, cam, t, cx, cy, radius, n=7, a=1.0, bounce=None):
    r = random.Random(9)
    for i in range(n):
        ph = r.uniform(0, 6.28)
        ang = t * r.uniform(0.6, 1.4) + ph
        rr = radius * (0.8 + 0.4 * math.sin(t * 2 + i))
        if bounce is not None:
            rr = max(rr, bounce + 80)
        speaker(d, cam, cx + math.cos(ang) * rr, cy + math.sin(ang) * rr * 0.5, t, s=r.uniform(0.8, 1.3), a=a)


def tower(d, cam, rows):
    for i in range(int(rows)):
        y = -i * 70
        a, b = cam.p(600, y - 66), cam.p(860, y)
        d.rectangle([a[0], a[1], b[0], b[1]], fill=(200, 110, 80, 255), outline=(150, 80, 60, 255))
        if i % 3 == 1:
            q0, q1 = cam.p(700, y - 50), cam.p(760, y - 16)
            d.rectangle([q0[0], q0[1], q1[0], q1[1]], fill=(255, 220, 150, 255))


def dome(d, cam, k, inside=False):
    """The room of silence: a dome built up to k (0..1)."""
    if k <= 0:
        return
    cx, base = cam.p(-300, 0)
    R = cam.s(420)
    d.pieslice([cx - R, base - R, cx + R, base + R], 180, 180 + 180 * k, fill=col((30, 40, 70, 255), 1), outline=col(CALM, 1), width=max(2, int(cam.s(10))))
    glow(d, cx, base - R * 0.4, R * 1.2, CALM, 0.3 * k)


def builder(d, cam, x, t, mode="hammer", **kw):
    fx, fy = cam.p(x, 0)
    figure(d, fx, fy, cam.s(CH), BUILD, mode=mode, phase=t * 6, face=kw.pop("face", 1), acc=("cap",), name=kw.pop("name", "THE BUILDER"), eye_col=(10, 50, 50, 255), **kw)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # the whole screen is noise: jagged waves, shouting bubbles, speakers swooping
    d.rectangle([0, 0, W, H], fill=(20, 10, 24, 255))
    waves(d, t, amp=1.0 + 0.5 * math.sin(t * 3))
    bubbles(d, t, n=14)
    cam = Cam(0, -300, 0.8)
    swarm(d, cam, t, 0, -300, 700, n=8)
    shake(cam, t, 6)


def s1_interrupted(d, t, dur):
    p = t / dur
    # trying to build: brick, brick, BUMP — the stack falls; hands over ears
    cam = Cam(300, -300, 0.75)
    plain(d, cam, t)
    rows = (2 + int(p * 6)) % 4
    tower(d, cam, rows)
    waves(d, t, amp=0.7, region=(0, 0, W, H * 0.6))
    swarm(d, cam, t, 600, -400, 500, n=6)
    builder(d, cam, 460, t, mode="hammer" if p < 0.6 else "reach", face=1, hands=None if p < 0.6 else None)
    bubbles(d, t, a=0.8, region=(W * 0.4, H * 0.15, W, H * 0.6), n=8)
    if (p * 6) % 4 > 3.6:
        particles(d, *cam.p(730, -100), cam.s(300), ((p * 6) % 4 - 3.6) / 0.4, (200, 110, 80), n=10, seed=int(p * 6), rise=-0.5, size=10)


def s2_room(d, t, dur):
    p = t / dur
    # the builder builds a small dome, steps inside; the door closes; inside, the waves fall flat
    cam = cam_lerp((300, -300, 0.75), (-300, -300, 0.8), sstep(p))
    plain(d, cam, t)
    k = sstep(ramp(p, 0.0, 0.6))
    waves(d, t, amp=0.7, region=(0, 0, W, H * 0.6))
    swarm(d, cam, t, -300, -300, 650, n=6, bounce=420)
    dome(d, cam, k)
    inside = p > 0.7
    builder(d, cam, lerp(200, -300, sstep(ramp(p, 0.55, 0.15))), t, mode="hammer" if p < 0.55 else "walk", face=-1, a=1.0 if not inside else 0.0)
    if inside:  # inside view: a flat calm line
        cx, base = cam.p(-300, 0)
        polyline(d, [(cx - cam.s(300), base - cam.s(200)), (cx + cam.s(300), base - cam.s(200))], 1, col(CALM, 0.9), 3)


def s3_voice(d, t, dur):
    p = t / dur
    # cutaway of the dome: inside, calm and work; outside, the noise bounces off and the tower rises
    rows = lerp(2, 26, sstep(ramp(p, 0.05, 0.85)))
    cam = cam_lerp((-100, -400, 0.7), (200, -900, 0.42), sstep(p))
    plain(d, cam, t, dusk=p)
    waves(d, t, amp=0.5 * (1 - p), region=(0, 0, W, H * 0.5))
    tower(d, cam, rows)
    dome(d, cam, 1.0)
    swarm(d, cam, t, -300, -300, 650, n=6, bounce=430, a=1 - 0.6 * p)
    cx, base = cam.p(-300, 0)
    R = cam.s(420)
    waves(d, t, amp=0.0, calm=1.0, region=(cx - R * 0.8, base - R * 0.9, cx + R * 0.8, base - R * 0.5))
    d.rectangle(cam.box(-420, -180, -200, -160), fill=(110, 80, 60, 255))  # drafting table
    builder(d, cam, -420, t, mode="carry", face=1, name="", mouth=0.4)
    dust(d, t, 0.4 * p, n=40, color=(200, 230, 255))
    top_caption(d, ["NOT EVERY VOICE DESERVES", "YOUR ATTENTION."], t, dur, accent={"EVERY", "ATTENTION."})


def s4_end(d, t, dur):
    cam = Cam(200, -900, 0.42)
    plain(d, cam, t, dusk=1.0)
    tower(d, cam, 26)
    dome(d, cam, 1.0)
    stage_end(d, t, dur, ["CHOOSE WHAT", "YOU HEAR."], [WHITE, CALM], size=110, dim=0.4, glow_col=CALM, y=H * 0.3)


SCENES = [s0_hook, s1_interrupted, s2_room, s3_voice, s4_end, s_follow]
