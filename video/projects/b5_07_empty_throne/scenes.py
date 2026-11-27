"""THE EMPTY THRONE — a kingdom falling apart beside a throne nobody will take.

World: a vast symmetrical throne hall in one-point perspective: a long crimson carpet, stone columns, banners
and a tall stained-glass window behind a golden throne. POTENTIAL is a silver-blue figure who stands beside the
throne but never sits; LAZINESS lounges on cushions on the steps. The hall cracks and darkens until Potential
finally climbs the steps and sits, and the light comes back.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, PCam, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, back_figure,
                   particles, top_caption, final_card, stage_end, shake, darkness, dust)
from kit import s_follow

TITLE = ("THE EMPTY", "THRONE")
OUTPUT = "107_The_Empty_Throne_16x9.mp4"
LINES = [
    "",
    "You keep waiting to become the person in charge.",
    "",
    "But your life is already yours to lead.",
    "",
    "",
]
SILENT = {0: 3.2, 2: 3.8, 4: 3.4}
GAPS = {1: 2.6, 3: 4.2}

GOLD = (255, 200, 100, 255)
POT = (150, 190, 255, 255)
LAZ = (130, 170, 110, 255)
CARPET = (130, 20, 30, 255)
STONE = (60, 56, 66, 255)
HW, HH, BACK = 900, 1800, 5200
THRONE_Z = 4500
COLS = [600 + i * 650 for i in range(7)]


def hall(d, cam, t, ruin=0.0, light=1.0):
    draw_sky(d, (6, 5, 8, 255), (20, 16, 22, 255))
    near = cam.z + 60
    for pts, c in (([(-HW, near, 0), (HW, near, 0), (HW, BACK, 0), (-HW, BACK, 0)], (40, 34, 40)),
                   ([(-HW, near, 0), (-HW, BACK, 0), (-HW, BACK, HH), (-HW, near, HH)], (34, 30, 38)),
                   ([(HW, near, 0), (HW, BACK, 0), (HW, BACK, HH), (HW, near, HH)], (34, 30, 38)),
                   ([(-HW, near, HH), (HW, near, HH), (HW, BACK, HH), (-HW, BACK, HH)], (16, 14, 18)),
                   ([(-HW, BACK, 0), (HW, BACK, 0), (HW, BACK, HH), (-HW, BACK, HH)], (28, 24, 30))):
        q = cam.quad(pts)
        if q:
            d.polygon(q, fill=tuple(int(v * (0.5 + 0.5 * light)) for v in c) + (255,))
    # stained-glass window
    wl = mix((60, 60, 90, 255), (255, 210, 140, 255), light * (1 - ruin * 0.8))
    q = cam.quad([(-260, BACK - 1, 500), (260, BACK - 1, 500), (260, BACK - 1, 1500), (-260, BACK - 1, 1500)])
    if q:
        cx, cy = (q[0][0] + q[1][0]) / 2, (q[0][1] + q[2][1]) / 2
        glow(d, cx, cy, abs(q[1][0] - q[0][0]) * 2.4, wl, 0.6 * light)
        d.polygon(q, fill=col(wl, 1))
        for k in range(1, 4):
            d.line([(lerp(q[0][0], q[1][0], k / 4), q[2][1]), (lerp(q[0][0], q[1][0], k / 4), q[0][1])], fill=(30, 24, 30, 255), width=3)
        d.line([(q[0][0], cy), (q[1][0], cy)], fill=(30, 24, 30, 255), width=3)
        # god rays down onto the throne
        tb = cam.p(0, THRONE_Z, 0)
        if tb:
            tpoly(d, [q[3], q[2], (tb[0] + abs(q[1][0] - q[0][0]) * 1.2, tb[1]), (tb[0] - abs(q[1][0] - q[0][0]) * 1.2, tb[1])], col(wl, 0.12 * light))
    # carpet
    q = cam.quad([(-240, near, 1), (240, near, 1), (240, THRONE_Z - 300, 1), (-240, THRONE_Z - 300, 1)])
    if q:
        d.polygon(q, fill=col(dimc(CARPET, 0.6 + 0.4 * light), 1))
    # columns (with cracks), banners
    r = random.Random(4)
    for z in sorted(COLS, reverse=True):
        for s in (-1, 1):
            x = s * (HW - 140)
            base, top = cam.p(x, z, 0), cam.p(x, z, HH)
            if not base:
                continue
            w = 90 * base[2]
            d.rectangle([base[0] - w, top[1], base[0] + w, base[1]], fill=col(tuple(int(v * (0.6 + 0.4 * light)) for v in STONE[:3]) + (255,), 1))
            if ruin > 0:
                for k in range(3):
                    yy = lerp(base[1], top[1], r.uniform(0.2, 0.8))
                    polyline(d, [(base[0] - w, yy), (base[0] - w * 0.2, yy + w * 0.4), (base[0] + w * 0.3, yy - w * 0.2), (base[0] + w, yy + w * 0.3)],
                             ruin, (14, 12, 16, 255), max(1, int(w * 0.12)))
            # banner hanging inside the column; falls with ruin
            fall = clamp(ruin * 2 - (z - 600) / 4000)
            bt = cam.p(x - s * 160, z, HH * 0.85 - fall * 900)
            bb = cam.p(x - s * 160, z, HH * 0.85 - 600 - fall * 900)
            if bt and bb and fall < 1:
                bw = 70 * bt[2]
                d.polygon([(bt[0] - bw, bt[1]), (bt[0] + bw, bt[1]), (bb[0] + bw, bb[1]), (bb[0], bb[1] + bw * 0.6), (bb[0] - bw, bb[1])],
                          fill=col(mix((150, 30, 40, 255), (80, 20, 26, 255), ruin), 1 - fall * 0.5))
                d.ellipse([bt[0] - bw * 0.4, (bt[1] + bb[1]) / 2 - bw * 0.4, bt[0] + bw * 0.4, (bt[1] + bb[1]) / 2 + bw * 0.4], fill=col(GOLD, 1 - fall))
    throne(d, cam, t, light)
    fog(d, W / 2, cam.horizon + 80, 2600, 0.1 + 0.15 * ruin, (200, 180, 200))


def throne(d, cam, t, light=1.0):
    z = THRONE_Z
    for k in range(3):  # steps
        q = cam.quad([(-500 + k * 80, z - 300 + k * 100, k * 70), (500 - k * 80, z - 300 + k * 100, k * 70),
                      (500 - k * 80, z - 300 + k * 100, (k + 1) * 70), (-500 + k * 80, z - 300 + k * 100, (k + 1) * 70)])
        if q:
            d.polygon(q, fill=col((70 + k * 8, 64 + k * 8, 74 + k * 8, 255), 1))
    back = cam.quad([(-170, z, 210), (170, z, 210), (170, z, 900), (-170, z, 900)])
    seat = cam.quad([(-210, z - 60, 210), (210, z - 60, 210), (210, z - 60, 400), (-210, z - 60, 400)])
    gl = mix((140, 110, 60, 255), GOLD, light)
    if back:
        d.polygon(back, fill=col(gl, 1))
        cx = (back[0][0] + back[1][0]) / 2
        topy = back[2][1]
        w = abs(back[1][0] - back[0][0])
        d.polygon([(cx - w * 0.5, topy), (cx - w * 0.3, topy - w * 0.35), (cx, topy - w * 0.15), (cx + w * 0.3, topy - w * 0.35), (cx + w * 0.5, topy)], fill=col(gl, 1))
        d.rectangle([cx - w * 0.3, topy + w * 0.2, cx + w * 0.3, back[0][1] - w * 0.1], fill=col((120, 20, 30, 255), 1))
    return seat


def throne_seat_front(d, cam, light=1.0):
    z = THRONE_Z
    q = cam.quad([(-210, z - 70, 210), (210, z - 70, 210), (210, z - 70, 390), (-210, z - 70, 390)])
    if q:
        d.polygon(q, fill=col(mix((140, 110, 60, 255), GOLD, light), 1))
        d.polygon([q[3], q[2], (q[2][0], q[2][1] + (q[0][1] - q[3][1]) * 0.3), (q[3][0], q[3][1] + (q[0][1] - q[3][1]) * 0.3)], fill=col((150, 25, 35, 255), 1))


def potential(d, cam, z, x, t, walking=False, phase=0.0, a=1.0, y=0.0, facing="toward"):
    p = cam.p(x, z, y)
    if not p:
        return
    glow(d, p[0], p[1] - 230 * p[2], 300 * p[2], POT, 0.4 * a)
    back_figure(d, p[0], p[1], 380 * p[2], POT, t, phase, 0.7 if walking else 0.0, facing=facing, a=a, name="POTENTIAL", name_a=a)


def laziness(d, cam, t, a=1.0):
    p = cam.p(-380, THRONE_Z - 380, 0)
    if not p:
        return
    h = 380 * p[2]
    d.ellipse([p[0] - h * 0.5, p[1] - h * 0.18, p[0] + h * 0.6, p[1] + h * 0.04], fill=col((120, 40, 60, 255), a))
    figure(d, p[0], p[1] - h * 0.06, h, LAZ, mode="lie", face=1, a=a)
    d.text((p[0], p[1] - h * 0.45), "LAZINESS", font=font(int(clamp(h * 0.12, 14, 30))), fill=col(LAZ, a), anchor="mm")
    return p, h


def whisper(d, x, y, text, a, size=30):
    if a <= 0.01:
        return
    f = font(size)
    tw = d.textlength(text, font=f)
    d.rounded_rectangle([x - tw / 2 - 20, y - size * 0.9, x + tw / 2 + 20, y + size * 0.9], int(size), fill=col((30, 40, 26, 255), 0.85 * a), outline=col(LAZ, a), width=2)
    d.text((x, y), text, font=f, fill=col(WHITE, a), anchor="mm")


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # great doors part, and the camera glides down the carpet toward an empty throne in a shaft of light
    cam = PCam(0, lerp(-400, 1600, sstep(p)), 700, horizon=H * 0.42)
    hall(d, cam, t)
    door = sstep(ramp(t, 0.2, 1.3))
    for s in (-1, 1):  # the doors swinging away to the sides
        w = W / 2 * (1 - door)
        x0 = 0 if s < 0 else W - w
        d.rectangle([x0, 0, x0 + w, H], fill=(50, 34, 24, 255))
        d.line([(x0 + (w if s < 0 else 0), 0), (x0 + (w if s < 0 else 0), H)], fill=(90, 66, 40, 255), width=8)


def s1_waiting(d, t, dur):
    p = t / dur
    cam = PCam(250, lerp(2300, 2700, p), 650, horizon=H * 0.42)
    hall(d, cam, t, ruin=0.15 * p)
    potential(d, cam, THRONE_Z - 250, 360, t)
    lp = laziness(d, cam, t)
    if lp:
        (lx, ly, _s), h = lp
        for i, w in enumerate(["NOT YET.", "SOMEONE ELSE WILL.", "WHY YOU?"]):
            whisper(d, lx + (i - 1) * h * 0.9, ly - h * (0.8 + 0.25 * i), w, ramp(t, dur * (0.15 + 0.25 * i), 0.3), int(clamp(h * 0.09, 18, 34)))
    dust(d, t, 0.4, n=40, color=(255, 220, 170))
    top_caption(d, ["YOU KEEP WAITING TO BECOME", "THE PERSON IN CHARGE."], t, dur, accent={"WAITING", "CHARGE."})


def s2_collapse(d, t, dur):
    p = t / dur
    # the kingdom falls apart around the empty seat: cracks, falling banners, a chandelier crashing down
    cam = PCam(0, lerp(2000, 1400, p), 800, horizon=H * 0.42)
    hits = [0.5, 1.5, 2.4]
    hit = max(pulse(t, k, 0.15) for k in hits)
    cam.x += math.sin(t * 50) * 30 * hit
    ruin = sstep(ramp(t, 0.2, dur * 0.8))
    hall(d, cam, t, ruin=ruin, light=1 - 0.6 * ruin)
    potential(d, cam, THRONE_Z - 250, 360, t, a=1.0)
    laziness(d, cam, t)
    # chandelier
    fall = sstep(ramp(t, 1.3, 0.35))
    cy = lerp(HH - 150, 30, fall)
    c = cam.p(0, 2900, cy)
    if c:
        r = 160 * c[2]
        rope = cam.p(0, 2900, HH)
        if fall < 0.05:
            d.line([rope[:2], c[:2]], fill=(60, 56, 50, 255), width=2)
        d.ellipse([c[0] - r, c[1] - r * 0.3, c[0] + r, c[1] + r * 0.3], outline=col(GOLD, 1), width=max(2, int(r * 0.08)))
        for k in range(6):
            fx = c[0] + math.cos(k) * r
            d.ellipse([fx - r * 0.06, c[1] - r * 0.35, fx + r * 0.06, c[1] - r * 0.15], fill=col((255, 220, 150, 255), 1 - fall))
        if fall >= 1:
            particles(d, c[0], c[1], r * 3, ramp(t, 1.65, 1.0), (180, 170, 160), n=50, seed=4, rise=0.5)
    particles(d, W * 0.5, H * 0.2, 600, ((t * 0.7) % 1), (150, 140, 130), n=40, seed=int(t * 0.7), rise=-0.8)
    darkness(d, W / 2, H / 2, 0.4 * ruin)


def s3_lead(d, t, dur):
    p = t / dur
    # Potential climbs the steps and sits. The light comes back; cracks fade; banners return.
    cam = PCam(0, lerp(1600, 3500, sstep(p)), lerp(800, 520, p), horizon=H * 0.42)
    sit = sstep(ramp(p, 0.15, 0.4))
    restore = sstep(ramp(p, 0.5, 0.45))
    hall(d, cam, t, ruin=1 - restore, light=0.4 + 0.6 * restore)
    laziness(d, cam, t, a=1 - restore)
    if sit < 1:
        z = lerp(THRONE_Z - 250, THRONE_Z - 60, sit)
        x = lerp(360, 0, sit)
        potential(d, cam, z, x, t, walking=True, phase=t * 5, y=sit * 210, facing="away" if sit < 0.6 else "toward")
    else:
        potential(d, cam, THRONE_Z - 60, 0, t, y=150)
        throne_seat_front(d, cam, 0.4 + 0.6 * restore)
    glow(d, W / 2, H * 0.35, 700, GOLD, 0.35 * restore)
    dust(d, t, 0.7 * restore, n=60, color=(255, 220, 160))
    top_caption(d, ["BUT YOUR LIFE IS", "ALREADY YOURS TO LEAD."], t, dur, accent={"YOURS", "LEAD."})


def s4_end(d, t, dur):
    cam = PCam(0, 3500 - 250 * (t / dur), 520, horizon=H * 0.42)
    hall(d, cam, t, ruin=0, light=1.0)
    potential(d, cam, THRONE_Z - 60, 0, t, y=150)
    throne_seat_front(d, cam, 1.0)
    stage_end(d, t, dur, ["TAKE THE THRONE."], [GOLD], size=120, dim=0.45, glow_col=GOLD, y=H * 0.78)


SCENES = [s0_hook, s1_waiting, s2_collapse, s3_lead, s4_end, s_follow]
