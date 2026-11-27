"""THE WEIGHT OF YOUR PROMISES — a person chained to every promise they broke.

World: a cold concrete void under one hard spotlight, steel-grey palette; far away, a warm doorway of light.
Heavy labelled blocks slam down and chain themselves to the person. They break free one chain at a time and
finally choose to carry one small golden weight: SHOW UP TOMORROW.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline, pill
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, beam,
                   top_caption, final_card, shake, dust, darkness, figure)
from kit import s_follow

TITLE = ("THE WEIGHT OF", "YOUR PROMISES")
OUTPUT = "95_The_Weight_Of_Your_Promises_16x9.mp4"
FOLLOW_SUB = ("FOR IDEAS, LESSONS, AND PERSPECTIVES", "THAT CHALLENGE THE WAY YOU THINK.")

LINES = [
    "Every promise you break…",
    "…becomes something you carry.",
    "Eventually, your excuses become heavier than the work itself.",
    "And the worst part?",
    "You already know what you could have done.",
    "You don't fix your life in one moment.",
    "You fix it by keeping one promise.",
    "Make promises you can keep.",
    "Then keep them.",
    "",
]
SPOKEN = [l.lstrip("…") for l in LINES]
GAPS = {0: 0.4, 1: 1.2, 2: 1.4, 3: 0.9, 4: 1.4, 5: 1.0, 6: 2.6, 7: 2.2, 8: 1.4}

YOU = (232, 230, 226, 255)
STEEL = (120, 128, 140, 255)
STEEL_D = (52, 56, 64, 255)
WARM = (255, 200, 140, 255)
GOLD = (255, 205, 110, 255)
CH = 230
DOOR_X = 2300

BLOCKS = [  # label, x offset behind the person, size
    ("START TOMORROW", -420, 1.0),
    ("GET SERIOUS NEXT WEEK", -790, 1.15),
    ("I'LL TRY AGAIN", -1150, 0.95),
    ("EXCUSES", -1480, 1.05),
    ("PROCRASTINATION", -1850, 1.2),
    ("FEAR", -2180, 0.9),
    ("UNFINISHED GOALS", -2520, 1.1),
]


def room(d, cam, t, warmth=0.0, spot_x=0, spot_a=1.0, door=1.0):
    draw_sky(d, mix((4, 5, 8, 255), (30, 20, 16, 255), warmth), mix((14, 16, 20, 255), (60, 40, 30, 255), warmth))
    # back wall seams
    for k in range(-20, 30):
        x = k * 400
        sx = cam.p(x, 0)[0]
        if -10 < sx < W + 10:
            d.line([(sx, 0), (sx, cam.p(0, 0)[1])], fill=(22, 24, 30, 255), width=max(1, int(cam.s(3))))
    fy = cam.p(0, 0)[1]
    d.rectangle([0, fy, W, H], fill=mix((18, 19, 23, 255), (40, 30, 26, 255), warmth))
    d.line([(0, fy), (W, fy)], fill=col(STEEL, 0.4), width=max(1, int(cam.s(3))))
    # the doorway of light far to the right
    if door > 0:
        dx0, dx1 = cam.p(DOOR_X, 0)[0], cam.p(DOOR_X + 260, 0)[0]
        top = cam.p(0, -560)[1]
        glow(d, (dx0 + dx1) / 2, (top + fy) / 2, cam.s(900), WARM, 0.55 * door)
        d.rectangle([dx0, top, dx1, fy], fill=col((255, 235, 200, 255), door))
        tpoly(d, [(dx0, fy), (dx1, fy), (dx1 - cam.s(900), H), (dx0 - cam.s(1400), H)], col(WARM, 0.18 * door))
    # the hard spotlight from above
    if spot_a > 0:
        sx = cam.p(spot_x, 0)[0]
        beam(d, sx, -40, sx - cam.s(360), sx + cam.s(360), fy, (220, 230, 255), 0.10 * spot_a, cam.s(60))
        tpoly(d, [(sx - cam.s(380), fy - cam.s(18)), (sx + cam.s(380), fy + cam.s(18))], col((220, 230, 255, 255), 0.12 * spot_a), kind="ellipse")


def block(d, cam, x, s, label, a=1.0, drop=1.0, gold=False):
    w, h = 300 * s, 190 * s
    y = -(1 - drop) * 900
    x0, y0, x1, y1 = cam.box(x - w / 2, y - h, x + w / 2, y)
    c = GOLD if gold else STEEL
    d.rounded_rectangle([x0, y0, x1, y1], int(cam.s(10)), fill=col(dimc(c, 0.45), a), outline=col(c, a), width=max(2, int(cam.s(5))))
    d.rounded_rectangle([x0 + cam.s(12), y0 + cam.s(12), x1 - cam.s(12), y0 + cam.s(30)], int(cam.s(6)), fill=col(dimc(c, 0.7), a))
    ring = cam.p(x, y - h - 18)
    d.ellipse([ring[0] - cam.s(16), ring[1] - cam.s(16), ring[0] + cam.s(16), ring[1] + cam.s(16)], outline=col(c, a), width=max(2, int(cam.s(5))))
    size = int(clamp(cam.s(34 * s) * (1 if len(label) < 14 else 0.72), 10, 70))
    d.text(((x0 + x1) / 2, (y0 + y1) / 2 + cam.s(10)), label, font=font(size), fill=col(WHITE if not gold else (60, 40, 10, 255), a), anchor="mm")
    return ring


def chain(d, cam, a_pt, b_pt, a=1.0, sag=0.25, broken=0.0, t=0.0, c=STEEL):
    """Links along a sagging curve from screen point a to b. broken: 0..1 how far the chain has fallen away."""
    (ax, ay), (bx, by) = a_pt, b_pt
    L = math.hypot(bx - ax, by - ay)
    n = max(3, int(L / max(6, cam.s(26))))
    r = max(3, cam.s(13))
    floor_y = cam.p(0, 0)[1] - r * 0.6
    for i in range(n + 1):
        u = i / n
        x = lerp(ax, bx, u)
        y = lerp(ay, by, u) + math.sin(math.pi * u) * min(L * sag, cam.s(70)) + broken * (1 - u) * cam.s(300) * u * 2
        y = min(y, floor_y)
        if broken > 0 and u < broken * 0.3:
            continue
        horiz = i % 2 == 0
        if horiz:
            d.ellipse([x - r, y - r * 0.55, x + r, y + r * 0.55], outline=col(c, a), width=max(2, int(r * 0.35)))
        else:
            d.line([(x - r * 0.8, y), (x + r * 0.8, y)], fill=col(c, a), width=max(2, int(r * 0.45)))


def person(d, cam, x, t, mode="stand", **kw):
    fx, fy = cam.p(x, 0)
    kw.setdefault("acc", ("hair",))
    head = figure(d, fx, fy, cam.s(CH), YOU, mode=mode, **kw)
    return (fx - cam.s(30), fy - cam.s(CH * 0.62)), head


def chained(d, cam, px, t, n, broken=None, drops=None, strain=0.0, **kw):
    """Draw the blocks, chains and the person; returns the person's back point."""
    broken = broken or {}
    drops = drops or {}
    back_pt = (cam.p(px, 0)[0] - cam.s(30), cam.p(px, 0)[1] - cam.s(CH * 0.62))
    rings = []
    for i in range(n):
        lbl, off, s = BLOCKS[i]
        bx = px + off + strain * 40 * math.sin(t * 3 + i)
        rings.append(block(d, cam, bx, s, lbl, drop=drops.get(i, 1.0)))
    for i in range(n):
        if drops.get(i, 1.0) >= 1:
            chain(d, cam, back_pt, rings[i], sag=0.08 + 0.03 * i, broken=broken.get(i, 0.0))
    return person(d, cam, px, t, **kw)


def slam(t, at):
    """Drop progress for a block falling at time `at` (fast, with a tiny bounce)."""
    u = clamp((t - at) / 0.22)
    return u * u if u < 1 else 1.0


# ---------------------------------------------------------------- scenes
def s0_break(d, t, dur):
    on = ramp(t, 0.1, 0.08)
    cam = Cam(-250, -230, 1.1)
    hit = pulse(t, 0.95, 0.15)
    shake(cam, t, 14 * hit)
    room(d, cam, t, spot_a=on, door=0)
    drop0 = slam(t, 0.75)
    ring = block(d, cam, BLOCKS[0][1], BLOCKS[0][2], BLOCKS[0][0], a=on, drop=drop0)
    back, _ = person(d, cam, 0, t, look=-0.2 if t < 0.9 else 0.4, head_down=0.3)
    if drop0 >= 1:
        chain(d, cam, back, ring, a=1.0, sag=0.08)
    darkness(d, W / 2, H / 2, 0.7)
    overlay(d, (0, 0, 0), 1 - on)
    top_caption(d, ["EVERY PROMISE YOU BREAK…"], t, dur, accent={"BREAK…"})


def s1_carry(d, t, dur):
    p = t / dur
    cam = cam_lerp((-250, -230, 1.1), (-650, -260, 0.82), sstep(p))
    hits = [dur * 0.15, dur * 0.45]
    hit = max(pulse(t, h + 0.2, 0.15) for h in hits)
    shake(cam, t, 12 * hit)
    room(d, cam, t, door=0)
    drops = {1: slam(t, hits[0]), 2: slam(t, hits[1])}
    chained(d, cam, 0, t, 3, drops=drops, look=0.0, head_down=0.4)
    darkness(d, W / 2, H / 2, 0.6)
    top_caption(d, ["…BECOMES SOMETHING", "YOU CARRY."], t, dur, accent={"CARRY."})
s1_carry.seamless = True


def s2_heavier(d, t, dur):
    p = t / dur
    # low side angle; four more weights land as the person tries to walk
    cam = cam_lerp((-1050, -260, 0.66), (-1150, -270, 0.6), p)
    hits = [dur * (0.1 + 0.14 * i) for i in range(4)]
    hit = max(pulse(t, h + 0.2, 0.15) for h in hits)
    shake(cam, t, 10 * hit)
    room(d, cam, t, spot_x=0)
    drops = {3 + i: slam(t, hits[i]) for i in range(4)}
    strain = ramp(t, dur * 0.2, 0.6)
    px = 60 * sstep(p) - 15 * math.sin(t * 4) * strain
    chained(d, cam, px, t, 7, drops=drops, strain=strain, mode="walk", phase=t * 2.2, lean=0.45 * strain, swing=0.25, stride=0.4,
            tired=strain, look=-0.2)
    darkness(d, W / 2, H / 2, 0.45)
    top_caption(d, ["EVENTUALLY, YOUR EXCUSES BECOME", "HEAVIER THAN THE WORK ITSELF."], t, dur, accent={"EXCUSES", "HEAVIER"})


def s3_worst(d, t, dur):
    p = t / dur
    # the camera swings round to find the light far away
    cam = cam_lerp((-900, -270, 0.6), (950, -300, 0.42), sstep(p))
    room(d, cam, t, spot_x=60, door=ramp(t, 0.1, 0.8))
    chained(d, cam, 60, t, 7, mode="reach", look=0.3, lean=0.3, face=1)
    top_caption(d, ["AND THE WORST PART?"], t, dur, accent={"WORST"})


def s4_know(d, t, dur):
    p = t / dur
    cam = cam_lerp((950, -300, 0.42), (1300, -300, 0.5), sstep(p))
    room(d, cam, t, spot_x=60, door=1)
    # in the light: the person they could have been, walking tall
    g = ramp(t, dur * 0.15, 0.8)
    gx = DOOR_X + 130 + 80 * math.sin(t * 0.6)
    fx, fy = cam.p(gx, 0)
    figure(d, fx, fy, cam.s(CH), (70, 45, 30, 255), mode="walk", phase=t * 4.5, face=1, a=0.85 * g, acc=("hair",), eyes=False)
    d.text((fx, fy - cam.s(CH * 1.25)), "WHO YOU COULD BE", font=font(int(cam.s(30))), fill=col(WARM, g * 0.9), anchor="mm")
    pull = 0.5 + 0.5 * math.sin(t * 3)
    chained(d, cam, 60 + 20 * pull, t, 7, strain=1.0, mode="reach", look=0.3, lean=0.35 + 0.1 * pull, face=1, tired=0.8)
    top_caption(d, ["YOU ALREADY KNOW WHAT", "YOU COULD HAVE DONE."], t, dur, accent={"KNOW"})


def s5_one_moment(d, t, dur):
    p = t / dur
    # close: the person reaches back and unhooks one chain
    cam = cam_lerp((-250, -200, 1.0), (-300, -210, 1.1), sstep(p))
    room(d, cam, t, spot_x=60, door=1, warmth=0.1 * p)
    unhook = ramp(t, dur * 0.45, 0.5)
    hands = None
    fx, fy = cam.p(60, 0)
    if t < dur * 0.8:
        reach = sstep(ramp(t, dur * 0.1, dur * 0.35))
        hands = ((fx - cam.s(30 + 30 * reach), fy - cam.s(CH * 0.6)), (fx - cam.s(40 + 40 * reach), fy - cam.s(CH * 0.62)))
    chained(d, cam, 60, t, 7, broken={0: unhook}, face=-1 if t < dur * 0.8 else 1, look=-0.4, hands=hands)
    if 0 < unhook < 1:
        glow(d, fx - cam.s(40), fy - cam.s(CH * 0.62), cam.s(120), WARM, 0.6 * (1 - unhook))
    top_caption(d, ["YOU DON'T FIX YOUR LIFE", "IN ONE MOMENT."], t, dur, accent={"ONE", "MOMENT."})


def s6_keep_one(d, t, dur):
    p = t / dur
    # walking toward the light; chain after chain snaps and falls away; the room warms up
    px = lerp(60, 1500, sstep(p))
    cam = Cam(px + 250, -260, lerp(0.7, 0.55, p))
    breaks = {0: 1.0}
    for i in range(1, 7):
        breaks[i] = ramp(t, dur * (0.08 + 0.13 * i), 0.5)
    room(d, cam, t, spot_a=1 - p, spot_x=60, door=1, warmth=p)
    back = (cam.p(px, 0)[0] - cam.s(30), cam.p(px, 0)[1] - cam.s(CH * 0.62))
    for i, (lbl, off, s) in enumerate(BLOCKS):
        bx = 60 + off  # the weights stay where they were dropped
        ring = block(d, cam, bx, s, lbl, a=lerp(1, 0.45, breaks[i]))
        if breaks[i] < 1:
            chain(d, cam, back, ring, sag=0.05, broken=breaks[i])
        if 0.0 < breaks[i] < 0.3:  # sparks where the chain snaps
            r = random.Random(i)
            for k in range(8):
                ang = r.uniform(0, math.tau)
                ln = cam.s(r.uniform(30, 90)) * breaks[i] * 3
                d.line([back, (back[0] + math.cos(ang) * ln, back[1] + math.sin(ang) * ln)], fill=col(GOLD, 0.9), width=2)
    left = sum(1 for v in breaks.values() if v < 1)
    person(d, cam, px, t, mode="walk", phase=px / 60, lean=lerp(0.35, 0.08, p), swing=lerp(0.2, 0.5, p), stride=lerp(0.5, 1.0, p),
           look=0.2)
    dust(d, t, 0.6 * p, n=50, color=(255, 220, 180))
    top_caption(d, ["YOU FIX IT BY KEEPING", "ONE PROMISE."], t, dur, accent={"ONE", "PROMISE."})


def s7_keep(d, t, dur):
    p = t / dur
    # at the threshold, one small golden weight is waiting; the person picks it up willingly
    px = lerp(1900, 2230, sstep(ramp(t, 0, dur * 0.35)))
    cam = cam_lerp((2100, -250, 0.95), (2180, -230, 1.2), sstep(p))
    room(d, cam, t, spot_a=0, door=1, warmth=1.0)
    lift = sstep(ramp(t, dur * 0.5, 0.7))
    gx = 2330
    if lift <= 0:
        block(d, cam, gx, 0.55, "SHOW UP TOMORROW", gold=True)
        person(d, cam, px, t, mode="walk" if px < 2229 else "kneel", phase=px / 60, look=-0.3)
    else:
        fx, fy = cam.p(2230, 0)
        bx, by = fx + cam.s(70), lerp(fy, fy - cam.s(CH * 0.45), lift)
        figure(d, fx, fy, cam.s(CH), YOU, mode="carry", acc=("hair",), look=0.2, mouth=0.5)
        w, h = cam.s(115), cam.s(77)
        d.rounded_rectangle([bx - w / 2, by - h, bx + w / 2, by], int(cam.s(8)), fill=col(dimc(GOLD, 0.45), 1), outline=col(GOLD, 1), width=max(2, int(cam.s(4))))
        d.text((bx, by - h / 2), "SHOW UP", font=font(int(cam.s(18))), fill=col((60, 40, 10, 255), 1), anchor="mm")
        d.text((bx, by - h / 2 + cam.s(18)), "TOMORROW", font=font(int(cam.s(14))), fill=col((60, 40, 10, 255), 1), anchor="mm")
        glow(d, bx, by - h / 2, cam.s(240), GOLD, 0.6 * lift)
    top_caption(d, ["MAKE PROMISES", "YOU CAN KEEP."], t, dur, accent={"KEEP."})


def s8_then(d, t, dur):
    cam = Cam(1700, -250, 0.9)
    room(d, cam, t, spot_a=0, door=1, warmth=1.0)
    overlay(d, (0, 0, 0), 0.55)
    final_card(d, t, dur, ["THEN KEEP THEM."], [GOLD], size=140, glow_col=GOLD)


SCENES = [s0_break, s1_carry, s2_heavier, s3_worst, s4_know, s5_one_moment, s6_keep_one, s7_keep, s8_then, s_follow]
