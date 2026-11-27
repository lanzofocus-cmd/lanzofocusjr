"""THE SHIP THAT NEVER LEFT — a great ship rusting in harbor while its dreamer studies maps.

World: a teal-and-amber harbor at dusk with a lighthouse, cranes and gulls. Seasons pass and the harbor decays.
THE DREAMER (sand coat) sits at a chart table; FEAR is a hooded storm-grey shade; THE CAPTAIN (navy coat, cap)
blows the horn and takes the ship out through a storm into sunlight.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, shade, sun,
                   stars, moon, rain, snow, flash, bolt, top_caption, final_card, stage_end, shake, darkness, beam, cloud)
from kit import s_follow

TITLE = ("THE SHIP THAT", "NEVER LEFT")
OUTPUT = "102_The_Ship_That_Never_Left_16x9.mp4"
LINES = [
    "",
    "You can spend your entire life preparing to sail.",
    "",
    "Or you can finally leave the harbor.",
    "",
    "",
]
SILENT = {0: 3.0, 2: 2.8, 4: 3.6}
GAPS = {1: 3.4, 3: 5.2}

SEA = (12, 50, 64, 255)
HULL = (30, 30, 36, 255)
KEEL = (150, 40, 40, 255)
DREAM = (225, 200, 160, 255)
CAPT = (60, 90, 160, 255)
FEAR = (130, 140, 160, 255)
LAMP = (255, 200, 120, 255)
CH = 230
SHIP_X = 400


def harbor_sky(d, t, dusk=1.0, storm=0.0, sunny=0.0):
    top = mix(mix((20, 30, 60, 255), (40, 44, 56, 255), storm), (90, 160, 230, 255), sunny)
    bot = mix(mix((250, 150, 100, 255), (70, 76, 90, 255), storm), (255, 230, 190, 255), sunny)
    draw_sky(d, top, bot)


def sea(d, cam, t, rough=0.0, a=1.0, sunny=0.0):
    hy = cam.p(0, 0)[1]
    c = mix(mix(SEA, (20, 30, 40, 255), rough), (40, 120, 160, 255), sunny)
    d.rectangle([0, hy, W, H], fill=col(c, a))
    for k in range(7):  # wave rows
        y0 = hy + k * cam.s(40) * (1 + k * 0.4)
        amp = cam.s(8 + 60 * rough) * (1 + k * 0.3)
        pts = []
        for i in range(0, W + 40, 40):
            pts.append((i, y0 + math.sin(i * 0.012 + t * (1.5 + rough * 2) + k) * amp))
        polyline(d, pts, 1, col(mix((80, 160, 170, 255), WHITE, rough * 0.5 + sunny * 0.3), 0.35 * a), max(1, int(cam.s(4))))


def ship(d, cam, x, t, rust=0.0, smoke=0.0, roll=0.0, bob=0.0, lights=1.0):
    """Side view of a steamship; x = stern, waterline y=0. roll in radians tilts it about its centre."""
    L = 1600
    cx, cy = x + L / 2, 0
    def P(px, py):
        dx, dy = px - cx, py - cy - bob
        return cam.p(cx + dx * math.cos(roll) - dy * math.sin(roll), cy + bob + dx * math.sin(roll) + dy * math.cos(roll))
    hull = [P(x, -260), P(x + L, -300), P(x + L - 150, 60), P(x + 80, 60)]
    d.polygon(hull, fill=col(mix(HULL, (90, 50, 30, 255), rust), 1))
    d.polygon([P(x + 70, 0), P(x + L - 110, 0), P(x + L - 150, 60), P(x + 80, 60)], fill=col(mix(KEEL, (110, 60, 40, 255), rust), 1))
    for i in range(14):  # portholes
        px = x + 140 + i * 95
        q = P(px, -150)
        r = cam.s(14)
        d.ellipse([q[0] - r, q[1] - r, q[0] + r, q[1] + r], fill=col(LAMP if lights > 0.5 else (40, 40, 50, 255), 0.4 + 0.6 * lights))
    sup = [P(x + 380, -260), P(x + 1100, -260), P(x + 1060, -480), P(x + 420, -480)]
    d.polygon(sup, fill=col(mix((230, 230, 225, 255), (160, 130, 110, 255), rust), 1))
    br = [P(x + 950, -480), P(x + 1150, -480), P(x + 1130, -600), P(x + 970, -600)]
    d.polygon(br, fill=col(mix((240, 240, 235, 255), (160, 130, 110, 255), rust), 1))
    for i in range(6):
        q0, q1 = P(x + 450 + i * 100, -400), P(x + 500 + i * 100, -440)
        d.rectangle([min(q0[0], q1[0]), min(q0[1], q1[1]), max(q0[0], q1[0]), max(q0[1], q1[1])], fill=col(LAMP, 0.3 + 0.6 * lights))
    fun = [P(x + 640, -480), P(x + 800, -480), P(x + 780, -820), P(x + 660, -820)]
    d.polygon(fun, fill=col(mix((200, 60, 50, 255), (120, 70, 50, 255), rust), 1))
    d.polygon([P(x + 655, -760), P(x + 785, -760), P(x + 780, -820), P(x + 660, -820)], fill=(20, 20, 24, 255))
    for mx in (x + 200, x + 1400):
        a, b = P(mx, -260), P(mx, -1000)
        d.line([a, b], fill=col((60, 50, 44, 255), 1), width=max(2, int(cam.s(10))))
    polyline(d, [P(x + 200, -1000), P(x + 720, -820), P(x + 1400, -1000)], 1, col((60, 50, 44, 255), 1), max(1, int(cam.s(3))))
    if rust > 0:  # rust streaks
        r = random.Random(3)
        for i in range(18):
            px = x + r.uniform(100, L - 200)
            a, b = P(px, -240), P(px + 10, -240 + r.uniform(60, 200))
            d.line([a, b], fill=col((150, 80, 40, 255), 0.6 * rust), width=max(1, int(cam.s(6))))
    if smoke > 0:
        top = P(x + 720, -820)
        for i in range(8):
            u = (t * 0.4 + i / 8) % 1
            sx, sy = top[0] - u * cam.s(500), top[1] - u * cam.s(400)
            rr = cam.s(40 + 140 * u)
            tpoly(d, [(sx - rr, sy - rr), (sx + rr, sy + rr)], col((200, 200, 205, 255), 0.4 * smoke * (1 - u)), kind="ellipse")
    return P


def dock(d, cam, t, decay=0.0):
    d.rectangle(cam.box(-1400, -10, 380, 260), fill=col(mix((80, 60, 44, 255), (50, 44, 40, 255), decay), 1))
    for k in range(-14, 4):
        x = k * 100
        d.line([cam.p(x, -10), cam.p(x, 260)], fill=(40, 30, 24, 255), width=max(1, int(cam.s(3))))
    for x in (-1200, -700, -200, 300):  # pilings
        d.rectangle(cam.box(x - 22, 0, x + 22, 500), fill=(46, 36, 28, 255))
    # lamp posts (going out as the harbor decays)
    for i, x in enumerate((-1100, -400)):
        on = 1 - clamp(decay * 3 - i)
        d.line([cam.p(x, -10), cam.p(x, -420)], fill=(40, 40, 48, 255), width=max(2, int(cam.s(8))))
        lp = cam.p(x, -430)
        d.ellipse([lp[0] - cam.s(16), lp[1] - cam.s(16), lp[0] + cam.s(16), lp[1] + cam.s(16)], fill=col(mix((60, 60, 60, 255), LAMP, on), 1))
        if on > 0.1:
            glow(d, lp[0], lp[1], cam.s(220), LAMP, 0.6 * on)
    # a crane leaning further over the years
    lean = decay * 0.25
    base = cam.p(-900, -10)
    top = (base[0] + math.sin(lean) * cam.s(900), base[1] - math.cos(lean) * cam.s(900))
    d.line([base, top], fill=(70, 60, 50, 255), width=max(2, int(cam.s(14))))
    d.line([top, (top[0] + cam.s(400), top[1] + cam.s(40))], fill=(70, 60, 50, 255), width=max(2, int(cam.s(10))))


def lighthouse(d, cam, t, a=1.0):
    bx = -1900
    d.polygon([cam.p(bx - 70, -10), cam.p(bx - 45, -800), cam.p(bx + 45, -800), cam.p(bx + 70, -10)], fill=col((220, 210, 200, 255), a))
    for k in range(4):
        y = -150 - k * 170
        d.polygon([cam.p(bx - 66 + k * 6, y), cam.p(bx - 60 + k * 6, y - 60), cam.p(bx + 60 - k * 6, y - 60), cam.p(bx + 66 - k * 6, y)], fill=col((190, 50, 50, 255), a))
    lp = cam.p(bx, -850)
    d.rectangle([lp[0] - cam.s(50), lp[1] - cam.s(50), lp[0] + cam.s(50), lp[1] + cam.s(50)], fill=col((255, 240, 200, 255), a))
    glow(d, lp[0], lp[1], cam.s(260), (255, 230, 170), 0.8 * a)
    ang = t * 1.1
    L = cam.s(5000)
    ex, ey = lp[0] + math.cos(ang) * L, lp[1] + math.sin(ang) * L * 0.08
    tpoly(d, [lp, (ex, ey - cam.s(200)), (ex, ey + cam.s(200))], col((255, 240, 200, 255), 0.12 * a))


def dreamer(d, cam, t, x=-520, maps=1.0, recoil=0.0):
    fx, fy = cam.p(x, -10)
    d.rectangle(cam.box(x + 40, -130, x + 300, -115), fill=(110, 80, 55, 255))
    for sx in (x + 60, x + 280):
        d.rectangle(cam.box(sx - 6, -115, sx + 6, -10), fill=(90, 64, 44, 255))
    # a growing pile of maps on the table
    for i in range(int(3 + 9 * maps)):
        d.rectangle(cam.box(x + 70 + (i % 3) * 6, -150 - i * 10, x + 270 - (i % 2) * 8, -140 - i * 10), fill=col((235, 220, 180, 255), 1), outline=(150, 130, 100, 255))
    d.rectangle(cam.box(x - 60, -90, x + 20, -80), fill=(90, 64, 44, 255))
    figure(d, fx + cam.s(-20) - recoil * cam.s(40), fy - cam.s(80), cam.s(CH), DREAM, mode="sit", face=1, acc=("hair",), head_down=0.4 * (1 - recoil),
           look=-0.3 + recoil * 0.8, hands=((fx + cam.s(110), fy - cam.s(150)), (fx + cam.s(170), fy - cam.s(150))) if recoil < 0.5 else None,
           name="THE DREAMER")


def s0_hook(d, t, dur):
    p = t / dur
    # night harbor: a lighthouse beam sweeps the black water and reveals a giant hull
    cam = cam_lerp((-1200, -500, 0.5), (200, -420, 0.42), sstep(p))
    harbor_sky(d, t, storm=0.4)
    stars(d, 0.6, seed=2, n=60, ymax=0.45)
    sea(d, cam, t)
    lighthouse(d, cam, t)
    ship(d, cam, SHIP_X, t, lights=ramp(t, 1.2, 0.6))
    dock(d, cam, t)
    darkness(d, W / 2, H / 2, 0.55)


def s1_preparing(d, t, dur):
    p = t / dur
    # seasons pass on the dock: maps pile up, lamps die, the crane leans, rust spreads over the hull
    cam = cam_lerp((250, -420, 0.5), (400, -440, 0.46), p)
    season = int(p * 4) % 4
    harbor_sky(d, t, storm=0.3 + 0.2 * p)
    sea(d, cam, t)
    lighthouse(d, cam, t, a=1 - 0.5 * p)
    ship(d, cam, SHIP_X, t, rust=p, lights=1 - p)
    dock(d, cam, t, decay=p)
    dreamer(d, cam, t, maps=p)
    if season == 1:
        snow(d, t, 0.9, n=140)
    elif season == 3:
        rain(d, t, 0.7, n=140)
    d.text((W - 120, H - 120), ["SPRING", "WINTER", "SUMMER", "AUTUMN"][season] + f"  ·  YEAR {1 + int(p * 9)}", font=font(30), fill=col(WHITE, 0.7), anchor="rm")
    top_caption(d, ["YOU CAN SPEND YOUR ENTIRE LIFE", "PREPARING TO SAIL."], t, dur, accent={"ENTIRE", "PREPARING"})


def s2_fear(d, t, dur):
    p = t / dur
    # Fear rises beside the table and points at the storm on the horizon
    cam = cam_lerp((-150, -360, 0.7), (100, -420, 0.55), sstep(p))
    harbor_sky(d, t, storm=0.6)
    sea(d, cam, t, rough=0.2)
    hx = cam.p(2600, -10)
    for i in range(4):
        cloud(d, hx[0] - 300 + i * 200 - 600, hx[1] - 150 - 40 * (i % 2), cam.s(300), col((60, 64, 80, 255), 0.9), w=max(2, int(cam.s(30))))
    fl = pulse(t, 1.0, 0.1) + pulse(t, 1.25, 0.08)
    if fl > 0:
        bolt(d, W * 0.86, H * 0.25, fl, 0.8)
    ship(d, cam, SHIP_X, t, rust=1.0, lights=0)
    dock(d, cam, t, decay=1.0)
    fx, fy = cam.p(-760, 0)
    shade(d, fx, fy, cam.s(380), FEAR, ramp(t, 0.1, 0.6), t, point=(fx + cam.s(380), fy - cam.s(330)), jag=0.8, name="FEAR")
    dreamer(d, cam, t, maps=1.0, recoil=sstep(ramp(t, 0.8, 0.6)))
    flash(d, fl)


def s3_leave(d, t, dur):
    p = t / dur
    # The Captain strides up the gangplank, blows the horn; ropes fall; the ship pulls out into the storm,
    # rides the waves, and breaks through into sunlight.
    a1, a2, a3 = 0.22, 0.4, 0.82
    if p < a2:
        u = p / a2
        cam = cam_lerp((100, -420, 0.55), (500, -500, 0.45), sstep(u))
        harbor_sky(d, t, storm=0.6)
        sea(d, cam, t, rough=0.2)
        ship(d, cam, SHIP_X, t, rust=1.0, lights=ramp(u, 0.5, 0.2), smoke=ramp(u, 0.55, 0.3))
        dock(d, cam, t, decay=1.0)
        dreamer(d, cam, t, maps=1.0, recoil=0.0)
        k = sstep(ramp(u, 0.0, 0.55))
        cx = lerp(-1300, 350, k)
        fx, fy = cam.p(cx, -10 - max(0, cx - 0) * 0.6)
        figure(d, fx, fy, cam.s(CH * 1.05), CAPT, mode="walk" if k < 1 else "pull", phase=t * 5, face=1, acc=("cap",), name="THE CAPTAIN")
        d.line([cam.p(0, -10), cam.p(SHIP_X + 60, -230)], fill=(110, 90, 70, 255), width=max(2, int(cam.s(10))))  # gangplank
    else:
        u = (p - a2) / (1 - a2)
        storm = 1 - sstep(ramp(u, 0.65, 0.3))
        sunny = sstep(ramp(u, 0.7, 0.3))
        sx = SHIP_X + 4000 * u
        cam = Cam(sx + 900, -500 + 60 * math.sin(t * 2) * storm, lerp(0.5, 0.42, u))
        shake(cam, t, 6 * storm)
        harbor_sky(d, t, storm=storm, sunny=sunny)
        if sunny > 0:
            sun(d, W * 0.75, cam.p(0, 0)[1] - 160, 90, sunny, (255, 230, 170, 255))
        sea(d, cam, t, rough=storm, sunny=sunny)
        roll = 0.08 * math.sin(t * 2.3) * storm
        ship(d, cam, sx, t, rust=1.0, lights=1, smoke=1.0, roll=roll, bob=40 * math.sin(t * 2.3) * storm)
        # big crest in front of the bow
        bow = cam.p(sx + 1700, 0)
        if storm > 0.2:
            r = cam.s(260) * storm
            tpoly(d, [(bow[0] - r, bow[1]), (bow[0] + r * 0.4, bow[1] - r * (0.8 + 0.3 * math.sin(t * 3))), (bow[0] + r, bow[1])], col(WHITE, 0.5 * storm))
        fl = pulse(u, 0.25, 0.03) + pulse(u, 0.45, 0.03)
        if fl > 0:
            bolt(d, W * 0.3, H * 0.15, fl, 0.9)
        rain(d, t, storm, n=220, slant=0.5)
        flash(d, fl)
    top_caption(d, ["OR YOU CAN FINALLY", "LEAVE THE HARBOR."], t, dur, accent={"FINALLY", "HARBOR."})


def s4_end(d, t, dur):
    sx = SHIP_X + 4400 + 200 * t
    cam = Cam(sx + 900, -500, 0.42)
    harbor_sky(d, t, sunny=1.0)
    sun(d, W * 0.75, cam.p(0, 0)[1] - 160, 90, 1.0, (255, 230, 170, 255))
    sea(d, cam, t, sunny=1.0)
    ship(d, cam, sx, t, rust=1.0, smoke=1.0)
    stage_end(d, t, dur, ["LEAVE THE HARBOR."], [WHITE], size=120, dim=0.35, y=H * 0.3)


SCENES = [s0_hook, s1_preparing, s2_fear, s3_leave, s4_end, s_follow]
