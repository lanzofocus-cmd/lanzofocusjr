"""THE CITY OF COMPARISON — a city where everyone measures their building against the next one.

World: a canyon of glass skyscrapers in cold steel blue, seen from a dizzying worm's-eye view, towers leaning in
toward a single point in the sky, each one tagged with its height. THE OBSERVER stands craning upward beside their
own small, unfinished frame of a building. When they finally look down and start building, their building grows
in its own warm shape and colour, and the cold towers blur into the background.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, dust, sun)
from kit import s_follow

TITLE = ("THE CITY OF", "COMPARISON")
OUTPUT = "129_The_City_Of_Comparison_16x9.mp4"
LINES = [
    "",
    "You keep measuring your life…",
    "Against someone else's building.",
    "Build your own.",
    "",
    "",
]
SILENT = {0: 3.2, 4: 3.4}
GAPS = {1: 0.8, 2: 2.4, 3: 5.6}

GLASS = (60, 90, 130, 255)
GLASS_L = (140, 180, 220, 255)
OBS = (230, 225, 215, 255)
WARM = (255, 170, 90, 255)
CH = 190
LABELS = ["300 FLOORS", "THEIRS", "BIGGER", "FASTER", "BETTER", "MORE", "HIGHER", "AHEAD"]


def worms_eye(d, t, spin=0.0, dim=0.0):
    """Looking straight up between converging skyscrapers."""
    draw_sky(d, (110, 150, 200, 255), (200, 220, 240, 255))
    cx, cy = W / 2, H / 2
    vp = (cx + 40 * math.sin(spin * 0.7), cy)
    n = 8
    for i in range(n):
        a0 = spin + i * math.tau / n
        a1 = a0 + math.tau / n * 0.62
        R = 1500
        base = [(cx + math.cos(a0) * R, cy + math.sin(a0) * R), (cx + math.cos(a1) * R, cy + math.sin(a1) * R)]
        k = 0.12
        top = [(lerp(vp[0], base[1][0], k), lerp(vp[1], base[1][1], k)), (lerp(vp[0], base[0][0], k), lerp(vp[1], base[0][1], k))]
        c = mix(mix(GLASS, (30, 40, 60, 255), (i % 3) * 0.2), (90, 100, 110, 255), dim)
        d.polygon(base + top, fill=c)
        for j in range(1, 14):  # floor lines converging
            u = j / 14
            p0 = (lerp(base[0][0], top[1][0], u), lerp(base[0][1], top[1][1], u))
            p1 = (lerp(base[1][0], top[0][0], u), lerp(base[1][1], top[0][1], u))
            d.line([p0, p1], fill=col(GLASS_L, 0.35 * (1 - dim)), width=2)
        mx, my = (base[0][0] + base[1][0] + top[0][0] + top[1][0]) / 4, (base[0][1] + base[1][1] + top[0][1] + top[1][1]) / 4
        d.text((mx, my), LABELS[i], font=font(40), fill=col(WHITE, 0.8 * (1 - dim)), anchor="mm")


def street(d, cam, t, own=0.0, dim=0.0, warm=0.0):
    """Side view of the street: giant glass towers, and the observer's own small lot."""
    draw_sky(d, mix((110, 150, 200, 255), (255, 180, 130, 255), warm), mix((200, 220, 240, 255), (255, 225, 190, 255), warm))
    if warm > 0:
        sun(d, W * 0.8, H * 0.3, 70, warm, (255, 225, 170, 255))
    r = random.Random(7)
    for i in range(12):
        x = -3000 + i * 520
        if -350 < x < 450:
            continue
        hgt = r.uniform(1800, 3400)
        a, b = cam.p(x, -hgt), cam.p(x + 440, 0)
        c = mix(GLASS, (130, 140, 150, 255), dim)
        d.rectangle([a[0], a[1], b[0], b[1]], fill=col(c, 1))
        for k in range(int(hgt / 120)):
            yy = cam.p(0, -hgt + k * 120)[1]
            d.line([(a[0], yy), (b[0], yy)], fill=col(GLASS_L, 0.25 * (1 - dim)), width=1)
        lx, ly = cam.p(x + 220, -hgt - 120)
        d.text((lx, ly), LABELS[i % len(LABELS)], font=font(max(10, int(cam.s(60)))), fill=col(WHITE, 0.75 * (1 - dim)), anchor="mm")
        # measuring ticks running up the tower
        for k in range(0, int(hgt / 300)):
            ty = cam.p(0, -k * 300)[1]
            d.line([(b[0], ty), (b[0] + cam.s(40), ty)], fill=col((255, 255, 255, 255), 0.4 * (1 - dim)), width=2)
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=(80, 84, 92, 255))
    own_building(d, cam, t, own)


def own_building(d, cam, t, k):
    """The observer's own building: an empty frame at k=0, a tall warm unique tower at k=1."""
    x0, x1 = -300, 400
    hgt = lerp(260, 2800, k)
    # scaffold frame
    if k < 0.15:
        for xx in (x0, x1):
            d.line([cam.p(xx, 0), cam.p(xx, -260)], fill=(150, 130, 100, 255), width=max(2, int(cam.s(10))))
        d.line([cam.p(x0, -260), cam.p(x1, -260)], fill=(150, 130, 100, 255), width=max(2, int(cam.s(10))))
        d.rectangle(cam.box(x0, -40, x1, 0), fill=(150, 130, 110, 255))
        return
    # stepped, rounded, warm — its own shape
    tiers = 5
    for i in range(tiers):
        u0, u1 = i / tiers, (i + 1) / tiers
        if u0 * 2800 > hgt:
            break
        top = -min(hgt, u1 * 2800)
        shrink = i * 40
        a, b = cam.p(x0 + shrink, top), cam.p(x1 - shrink, -u0 * 2800)
        d.rounded_rectangle([a[0], a[1], b[0], b[1]], int(cam.s(40)), fill=col(mix((220, 130, 80, 255), (255, 190, 120, 255), i / tiers), 1))
        for wy in range(int((b[1] - a[1]) / cam.s(80))):
            for wx in range(3):
                q = (lerp(a[0], b[0], (wx + 0.5) / 3), a[1] + cam.s(40) + wy * cam.s(80))
                d.ellipse([q[0] - cam.s(16), q[1] - cam.s(20), q[0] + cam.s(16), q[1] + cam.s(20)], fill=(255, 235, 180, 255))
    if hgt > 2600:  # a little garden on the roof
        rx, ry = cam.p((x0 + x1) / 2, -hgt)
        d.ellipse([rx - cam.s(80), ry - cam.s(120), rx + cam.s(80), ry], fill=(90, 160, 90, 255))
    glow(d, *cam.p((x0 + x1) / 2, -hgt * 0.5), cam.s(1200), WARM, 0.3 * k)


def observer(d, cam, t, look_up=1.0, mode="stand", x=-500):
    fx, fy = cam.p(x, 0)
    figure(d, fx, fy, cam.s(CH), OBS, mode=mode, phase=t * 5, face=1, acc=("hair",), look=look_up, lean=-0.25 * look_up,
           head_down=0.0 if look_up > 0 else 0.4, name="THE OBSERVER",
           prop=(lambda dd, fh, bh, h, a: fh and dd.rectangle([fh[0] - h * 0.05, fh[1] - h * 0.22, fh[0] + h * 0.05, fh[1] - h * 0.16], fill=col((200, 200, 210, 255), a))) if mode == "hammer" else None)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    worms_eye(d, t, spin=t * 0.25)
    overlay(d, (0, 0, 0), 0.6 * (1 - ramp(t, 0.0, 0.8)))


def s1_measuring(d, t, dur):
    p = t / dur
    # crane down from the tower tops to the street: one small figure, head tilted all the way back
    cam = cam_lerp((-1200, -2600, 0.3), (-300, -600, 0.5), sstep(p))
    street(d, cam, t)
    observer(d, cam, t, look_up=1.0)
    top_caption(d, ["YOU KEEP MEASURING", "YOUR LIFE…"], t, dur, accent={"MEASURING"})


def s2_someone(d, t, dur):
    p = t / dur
    # beside the observer: their own empty lot, a bare frame, waiting
    cam = cam_lerp((-300, -600, 0.5), (-150, -300, 1.2), sstep(p))
    street(d, cam, t)
    observer(d, cam, t, look_up=1.0)
    if p > 0.4:
        fx, fy = cam.p(50, -300)
        d.text((fx, fy), "YOURS", font=font(int(cam.s(60))), fill=col(WARM, ramp(p, 0.4, 0.2)), anchor="mm")
    top_caption(d, ["AGAINST SOMEONE", "ELSE'S BUILDING."], t, dur, accent={"SOMEONE", "ELSE'S"})


def s3_own(d, t, dur):
    p = t / dur
    # the observer lowers their eyes to their own plot, picks up a hammer; it rises in its own shape;
    # the glass towers grey out behind it
    k = sstep(ramp(p, 0.2, 0.7))
    cam = cam_lerp((-150, -300, 1.2), (0, -1500, 0.28), sstep(ramp(p, 0.15, 0.8)))
    street(d, cam, t, own=k, dim=sstep(ramp(p, 0.3, 0.5)), warm=sstep(ramp(p, 0.4, 0.5)))
    observer(d, cam, t, look_up=lerp(1.0, -0.4, sstep(ramp(p, 0.0, 0.15))), mode="hammer" if 0.15 < p < 0.9 else "stand")
    dust(d, t, 0.5 * k, n=50, color=(255, 210, 160))
    top_caption(d, ["BUILD YOUR OWN."], t, dur, accent={"OWN."})


def s4_end(d, t, dur):
    cam = Cam(0, -1500, 0.28)
    street(d, cam, t, own=1.0, dim=1.0, warm=1.0)
    observer(d, cam, t, look_up=0.4)
    stage_end(d, t, dur, ["BUILD YOUR OWN."], [WARM], size=120, dim=0.35, glow_col=WARM, y=H * 0.22)


SCENES = [s0_hook, s1_measuring, s2_someone, s3_own, s4_end, s_follow]
