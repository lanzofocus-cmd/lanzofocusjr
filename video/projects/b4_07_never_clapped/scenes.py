"""THE PEOPLE WHO NEVER CLAPPED — a performer, a huge stage and an audience that never came.

World: a grand theatre in deep crimson and black. Two camera positions alternate: from the house looking at
the stage, and the reverse, from behind the performer out into rows of empty seats. The imagined crowd is
ghostly blue-grey; years later the real crowd is warm and gold. The performer plays guitar and, at the end,
keeps playing after the room goes quiet.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline, pill
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, beam,
                   top_caption, low_caption, final_card, shake, dust, darkness, word_reveal)
from kit import s_follow

TITLE = ("THE PEOPLE WHO", "NEVER CLAPPED")
OUTPUT = "97_The_People_Who_Never_Clapped_16x9.mp4"
FOLLOW_SUB = ("FOR IDEAS, LESSONS, AND PERSPECTIVES", "THAT CHALLENGE THE WAY YOU THINK.")

LINES = [
    "Not everyone will believe in you.",
    "Some will laugh.",
    "Some will doubt you.",
    "Some won't even care.",
    "And sometimes…",
    "…you'll have absolutely no one cheering.",
    "That's when you find out…",
    "…whether you're doing it for them.",
    "Because if you need applause to continue…",
    "…you'll stop when the room goes quiet.",
    "Work even when nobody watches.",
    "",
]
SPOKEN = [l.lstrip("…") for l in LINES]
GAPS = {0: 1.0, 1: 0.9, 2: 0.9, 3: 1.2, 4: 0.4, 5: 1.4, 6: 0.4, 7: 3.0, 8: 0.5, 9: 2.2, 10: 1.6}

CRIMSON = (120, 16, 30, 255)
CRIMSON_L = (180, 40, 50, 255)
GOLD = (255, 200, 110, 255)
SPOT = (235, 240, 255, 255)
GHOST = (120, 140, 190, 255)
YOU = (236, 232, 226, 255)
SEAT = (60, 14, 22, 255)
CH = 230


# ---------------------------------------------------------------- the house view (stage from the seats)
def stage_view(d, cam, t, spot=1.0, lights=0.0, warm=0.0, crowd=None, curtains=1.0):
    draw_sky(d, (4, 2, 4, 255), mix((14, 6, 8, 255), (40, 22, 12, 255), warm))
    # back wall / cyclorama
    a, b = cam.p(-900, -1100), cam.p(900, 0)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=col(mix((16, 10, 14, 255), (70, 40, 24, 255), warm), 1))
    # stage floor
    f0, f1 = cam.p(-1100, 0), cam.p(1100, 70)
    d.rectangle([f0[0], f0[1], f1[0], f1[1]], fill=col(mix((40, 26, 22, 255), (110, 70, 40, 255), warm * 0.8 + spot * 0.1), 1))
    d.line([cam.p(-1100, 0), cam.p(1100, 0)], fill=col(GOLD, 0.35), width=max(1, int(cam.s(4))))
    for k in range(-10, 11):  # floor boards
        d.line([cam.p(k * 110, 0), cam.p(k * 130, 70)], fill=(30, 18, 16, 255), width=1)
    # lighting bank
    for i in range(9):
        lx = -800 + i * 200
        on = clamp(lights * 9 - abs(i - 4) * 2) if lights < 1 else 1.0
        lp = cam.p(lx, -1060)
        d.rectangle([lp[0] - cam.s(30), lp[1] - cam.s(24), lp[0] + cam.s(30), lp[1] + cam.s(24)], fill=(30, 30, 34, 255))
        if on > 0:
            c = mix(SPOT, GOLD, warm)
            glow(d, lp[0], lp[1] + cam.s(20), cam.s(120), c, 0.8 * on)
            beam(d, lp[0], lp[1] + cam.s(20), cam.p(lx * 0.5 - 300, 0)[0], cam.p(lx * 0.5 + 300, 0)[0], cam.p(0, 0)[1], c, 0.05 * on, cam.s(20))
    # the single hard spotlight on the performer
    if spot > 0:
        sp = cam.p(0, -1100)
        beam(d, sp[0], 0, cam.p(-260, 0)[0], cam.p(260, 0)[0], cam.p(0, 0)[1], SPOT, 0.12 * spot, cam.s(70))
        tpoly(d, [cam.p(-300, -24), cam.p(300, 24)], col(SPOT, 0.2 * spot), kind="ellipse")
    # curtains and proscenium
    for s in (-1, 1):
        x0 = s * 900
        open_w = 330 * curtains + 40
        pts = [cam.p(x0, -1250), cam.p(x0 - s * open_w, -1250), cam.p(x0 - s * (open_w - 60), -500), cam.p(x0 - s * open_w * 0.7, 0), cam.p(x0 + s * 400, 0), cam.p(x0 + s * 400, -1250)]
        d.polygon(pts, fill=col(CRIMSON, 1))
        for k in range(7):  # folds
            fx = x0 - s * (open_w * k / 7)
            d.line([cam.p(fx, -1250), cam.p(fx + s * 30, 0)], fill=col(CRIMSON_L, 0.35), width=max(1, int(cam.s(6))))
    valance = [cam.p(-1300, -1300), cam.p(1300, -1300), cam.p(1300, -1120), cam.p(-1300, -1120)]
    d.polygon(valance, fill=col(CRIMSON, 1))
    for k in range(14):
        cx = -1250 + k * 190
        d.chord(cam.box(cx - 95, -1190, cx + 95, -1080), 0, 180, fill=col(CRIMSON, 1))
    d.line([cam.p(-1300, -1120), cam.p(1300, -1120)], fill=col(GOLD, 0.6), width=max(2, int(cam.s(6))))


def front_rows(d, cam, t, crowd=None, warm=0.0):
    """Seat backs in the foreground (and heads when someone is sitting there)."""
    for row in range(2):
        y = 260 + row * 170
        n = 12
        for i in range(n):
            x = -1500 + i * 270 + (135 if row else 0)
            sx, sy = cam.p(x, y)
            r = cam.s(115 + row * 20)
            if crowd:
                kind = crowd(i + row * 20)
                if kind:
                    head(d, sx, sy - r * 0.8, r * 0.55, kind, t, i)
            d.rounded_rectangle([sx - r, sy - r * 0.55, sx + r, sy + r * 1.6], int(r * 0.4), fill=col(mix(SEAT, (90, 30, 30, 255), warm), 1))
            d.line([(sx - r * 0.8, sy - r * 0.4), (sx + r * 0.8, sy - r * 0.4)], fill=col(CRIMSON_L, 0.4), width=max(1, int(cam.s(4))))


def head(d, x, y, r, kind, t, i):
    """An audience member's head and shoulders. kind: (state, alpha) with state laugh|doubt|leave|clap|still|phone."""
    state, a = kind
    ghost = state in ("laugh", "doubt", "leave", "phone", "ghost")
    c = GHOST if ghost else GOLD
    c = col(dimc(c, 0.95 if ghost else 0.9), a * (0.8 if ghost else 1.0))
    dx = 0
    dy = 0
    if state == "laugh":
        dy = -abs(math.sin(t * 9 + i)) * r * 0.25
    elif state == "doubt":
        dx = math.sin(t * 6 + i) * r * 0.25
    elif state == "clap":
        dy = -abs(math.sin(t * 7 + i * 1.3)) * r * 0.1
    elif state == "leave":
        dy = 0
    d.chord([x - r * 1.5, y + r * 0.7 + dy, x + r * 1.5, y + r * 3.2 + dy], 180, 360, fill=c)
    d.ellipse([x - r * 0.75 + dx, y - r * 0.75 + dy, x + r * 0.75 + dx, y + r * 0.75 + dy], fill=c)
    if state == "laugh" and math.sin(t * 3 + i) > 0.3:
        d.text((x + r * 1.2, y - r * 1.4 + dy), "HA", font=font(int(r * 0.9)), fill=col(GHOST, a * 0.8), anchor="mm")
    if state == "clap":
        k = abs(math.sin(t * 9 + i))
        for s in (-1, 1):
            hx = x + s * r * (0.3 + 0.35 * k)
            d.ellipse([hx - r * 0.28, y + r * 0.5 - r * 0.28 + dy, hx + r * 0.28, y + r * 0.5 + r * 0.28 + dy], fill=col(mix(GOLD, WHITE, 0.4), a))
    if state == "phone":
        d.rectangle([x - r * 0.25, y + r * 0.9, x + r * 0.25, y + r * 1.4], fill=col((170, 210, 255, 255), a))
        glow(d, x, y + r, r * 2, (150, 200, 255), 0.4 * a)


def performer(d, cam, x, t, strum=1.0, look=0.0, face=1, a=1.0, mode="stand", guitar=True, head_down=0.0):
    fx, fy = cam.p(x, 0)
    h = cam.s(CH)
    body = (fx + 0.04 * h * face, fy - 0.43 * h)
    neck_end = (fx + 0.47 * h * face, fy - 0.66 * h)
    st = math.sin(t * 10) * strum
    hands = ((neck_end[0] - 0.06 * h * face, neck_end[1] + 0.02 * h), (body[0] + 0.02 * h * face, body[1] - 0.05 * h + st * 0.04 * h)) if guitar else None
    figure(d, fx, fy, h, YOU, mode=mode, phase=0, face=face, look=look, acc=("hair",), hands=hands, a=a, head_down=head_down)
    if guitar:
        gc = col((190, 110, 60, 255), a)
        d.line([body, neck_end], fill=col((90, 50, 30, 255), a), width=max(2, int(h * 0.035)))
        d.ellipse([body[0] - 0.11 * h, body[1] - 0.09 * h, body[0] + 0.11 * h, body[1] + 0.09 * h], fill=gc)
        d.ellipse([body[0] - 0.08 * h + 0.06 * h * face, body[1] - 0.12 * h, body[0] + 0.08 * h + 0.06 * h * face, body[1] + 0.03 * h], fill=gc)
        d.ellipse([body[0] - 0.025 * h, body[1] - 0.025 * h, body[0] + 0.025 * h, body[1] + 0.025 * h], fill=col((30, 16, 10, 255), a))
        # the hands drawn again on top of the guitar
        for hp in hands:
            d.ellipse([hp[0] - 0.035 * h, hp[1] - 0.035 * h, hp[0] + 0.035 * h, hp[1] + 0.035 * h], fill=col(YOU, a))


# ---------------------------------------------------------------- the reverse view (from the stage into the seats)
ROWS = 8


def seats_view(d, t, z=1.0, crowd=None, warm=0.0, light=1.0, perf_a=1.0, strum=0.0, perf_look=0.0):
    draw_sky(d, (2, 1, 3, 255), mix((10, 4, 6, 255), (36, 20, 10, 255), warm))
    cx = W / 2
    horizon = 300
    # balcony line and exit signs
    d.line([(0, horizon - 30 * z), (W, horizon - 30 * z)], fill=col(CRIMSON_L, 0.3), width=3)
    for ex in (220, W - 220):
        d.rectangle([ex - 50, horizon - 120, ex + 50, horizon - 80], fill=col((60, 200, 120, 255), 0.7))
        glow(d, ex, horizon - 100, 90, (60, 200, 120), 0.3)
    for r in range(ROWS - 1, -1, -1):
        k = r / (ROWS - 1)
        y = lerp(H - 120, horizon + 20, k ** 0.8)
        y = H / 2 + (y - H / 2) * z
        s = lerp(1.0, 0.38, k) * z
        n = int(lerp(9, 17, k))
        span = lerp(W * 1.25, W * 0.95, k) * z
        for i in range(n):
            x = cx - span / 2 + span * (i + 0.5) / n
            r0 = 62 * s
            if crowd:
                kind = crowd(r * 30 + i)
                if kind:
                    head(d, x, y - r0 * 1.25, r0 * 0.8, kind, t, r * 30 + i)
            d.rounded_rectangle([x - r0, y - r0 * 0.7, x + r0, y + r0 * 0.9], int(r0 * 0.4), fill=col(mix(SEAT, (110, 40, 34, 255), warm), light))
            d.line([(x - r0 * 0.75, y - r0 * 0.5), (x + r0 * 0.75, y - r0 * 0.5)], fill=col(CRIMSON_L, 0.35 * light), width=max(1, int(3 * s)))
    # stage edge and the performer's back in the foreground
    d.rectangle([0, H - 90, W, H], fill=(24, 16, 14, 255))
    d.line([(0, H - 90), (W, H - 90)], fill=col(GOLD, 0.4), width=3)
    if perf_a > 0:
        px, py = W * 0.32, H + 30
        hh = 720 * z
        c = col(dimc(YOU, 0.25), perf_a)
        d.rounded_rectangle([px - hh * 0.16, py - hh * 0.55, px + hh * 0.16, py], int(hh * 0.12), fill=c)
        hx = px + perf_look * hh * 0.03
        d.ellipse([hx - hh * 0.1, py - hh * 0.78, hx + hh * 0.1, py - hh * 0.58], fill=c)
        d.chord([hx - hh * 0.105, py - hh * 0.79, hx + hh * 0.105, py - hh * 0.63], 180, 360, fill=col(dimc(YOU, 0.15), perf_a))
        # guitar neck sticking out past the shoulder
        d.line([(px + hh * 0.1, py - hh * 0.3), (px + hh * 0.42, py - hh * 0.52)], fill=col((90, 50, 30, 255), perf_a), width=int(hh * 0.025))
        glow(d, px, py - hh * 0.6, hh * 0.5, SPOT, 0.25 * perf_a)


def crowd_fn(t, dur, mode, seed=1):
    r = random.Random(seed)
    table = {}

    def f(idx):
        if idx not in table:
            table[idx] = r.random()
        u = table[idx]
        if mode == "laugh":
            return ("laugh", ramp(t, u * dur * 0.4, 0.3)) if u < 0.7 else None
        if mode == "doubt":
            return ("doubt" if u < 0.5 else "laugh", 1.0) if u < 0.7 else None
        if mode == "leave":
            if u < 0.7:
                leave = ramp(t, u * dur * 0.9, 0.3)
                return ("phone" if u < 0.25 else "ghost", 1 - leave) if leave < 1 else None
            return None
        if mode == "full":
            return ("clap", ramp(t, u * 0.6, 0.4)) if u < 0.92 else None
        if mode == "quiet":
            return ("still", 1 - ramp(t, u * dur * 0.5, 0.6)) if u < 0.92 and ramp(t, u * dur * 0.5, 0.6) < 1 else None
        return None
    return f


# ---------------------------------------------------------------- scenes
def s0_believe(d, t, dur):
    p = t / dur
    on = ramp(t, 0.15, 0.06)
    cam = cam_lerp((0, -420, 0.62), (0, -360, 0.75), sstep(p))
    stage_view(d, cam, t, spot=on)
    performer(d, cam, 0, t, strum=0, a=on, look=0.2)
    front_rows(d, cam, t)
    darkness(d, W / 2, H / 2 - 100, 0.4)
    overlay(d, (0, 0, 0), 1 - on)
    top_caption(d, ["NOT EVERYONE WILL", "BELIEVE IN YOU."], t, dur, accent={"BELIEVE"})


def s1_laugh(d, t, dur):
    p = t / dur
    seats_view(d, t, z=lerp(1.0, 1.06, p), crowd=crowd_fn(t, dur, "laugh", 3))
    top_caption(d, ["SOME WILL LAUGH."], t, dur, accent={"LAUGH."})


def s2_doubt(d, t, dur):
    p = t / dur
    seats_view(d, t, z=lerp(1.06, 1.12, p), crowd=crowd_fn(t, dur, "doubt", 3))
    top_caption(d, ["SOME WILL DOUBT YOU."], t, dur, accent={"DOUBT"})
s2_doubt.seamless = True


def s3_care(d, t, dur):
    p = t / dur
    seats_view(d, t, z=lerp(1.12, 1.18, p), crowd=crowd_fn(t, dur, "leave", 3))
    top_caption(d, ["SOME WON'T EVEN CARE."], t, dur, accent={"CARE."})
s3_care.seamless = True


def s4_sometimes(d, t, dur):
    p = t / dur
    cam = cam_lerp((0, -300, 0.9), (0, -280, 1.0), p)
    stage_view(d, cam, t, spot=1)
    look = math.sin(t * 2.0)
    performer(d, cam, 0, t, strum=0, look=0.1, face=1 if look > 0 else -1)
    front_rows(d, cam, t)
    top_caption(d, ["AND SOMETIMES…"], t, dur, accent={"SOMETIMES…"})


def s5_no_one(d, t, dur):
    p = t / dur
    # the lights go out bank by bank until only a cold work light is left
    cam = cam_lerp((0, -520, 0.55), (0, -480, 0.5), p)
    spot = 1 - ramp(t, dur * 0.55, 0.4)
    stage_view(d, cam, t, spot=spot, lights=1 - ramp(t, 0.1, dur * 0.5))
    if spot < 1:  # a bare work lamp on a stand
        wx, wy = cam.p(-500, -380)
        d.line([cam.p(-500, 0), (wx, wy)], fill=(80, 80, 90, 255), width=max(2, int(cam.s(6))))
        d.ellipse([wx - cam.s(16), wy - cam.s(16), wx + cam.s(16), wy + cam.s(16)], fill=col((255, 240, 210, 255), 1 - spot))
        glow(d, wx, wy, cam.s(500), (255, 230, 190), 0.5 * (1 - spot))
    performer(d, cam, 0, t, strum=0, head_down=0.6 * p, look=-0.4 * p)
    front_rows(d, cam, t)
    darkness(d, W / 2, H / 2, 0.3 + 0.4 * p)
    top_caption(d, ["…YOU'LL HAVE ABSOLUTELY", "NO ONE CHEERING."], t, dur, accent={"NO", "ONE"})


def worklight_stage(d, cam, t, warm=0.0):
    stage_view(d, cam, t, spot=0, lights=0, warm=warm)
    wx, wy = cam.p(-500, -380)
    d.line([cam.p(-500, 0), (wx, wy)], fill=(80, 80, 90, 255), width=max(2, int(cam.s(6))))
    d.ellipse([wx - cam.s(16), wy - cam.s(16), wx + cam.s(16), wy + cam.s(16)], fill=(255, 240, 210, 255))
    glow(d, wx, wy, cam.s(600), (255, 230, 190), 0.55)


def s6_find_out(d, t, dur):
    p = t / dur
    # looks at the empty seats... then turns back to the instrument
    cam = cam_lerp((0, -300, 0.95), (60, -280, 1.1), sstep(p))
    worklight_stage(d, cam, t)
    turn = p > 0.55
    performer(d, cam, 0, t, strum=0, face=-1 if not turn else 1, look=0.0 if not turn else -0.2, head_down=0 if not turn else 0.3)
    front_rows(d, cam, t)
    darkness(d, W / 2, H / 2, 0.35)
    top_caption(d, ["THAT'S WHEN YOU FIND OUT…"], t, dur, accent={"FIND", "OUT…"})


def s7_for_them(d, t, dur):
    p = t / dur
    # practice montage under the work light: again, again, again
    shots = [("AGAIN.", "DAY 1", (0, -300, 1.15), 0), ("AGAIN.", "DAY 86", (-200, -260, 0.8), 1), ("AGAIN.", "DAY 340", (150, -250, 1.35), 2),
             ("AGAIN.", "DAY 912", (0, -400, 0.6), 3)]
    n = len(shots)
    i = min(n - 1, int(p * n))
    u = p * n - i
    tag, day, c, k = shots[i]
    cam = Cam(c[0] + lerp(-20, 20, u), c[1], c[2] * lerp(1.0, 1.04, u))
    worklight_stage(d, cam, t, warm=0.1 * i)
    performer(d, cam, 0, t, strum=1.0, look=-0.1, head_down=0.3)
    front_rows(d, cam, t)
    darkness(d, W / 2, H / 2, 0.3)
    a = ramp(u, 0.05, 0.15) * (1 - ramp(u, 0.85, 0.15))
    d.text((W - 160, H - 140), tag, font=font(64), fill=col(WHITE, a), anchor="rm")
    pill(d, 220, H - 140, day, a, 30, inverted=False)
    dip = max(0.0, 1 - min(u, 1 - u) / 0.06) if (i > 0 or u > 0.5) and not (i == n - 1 and u > 0.5) else 0
    overlay(d, (0, 0, 0), 0.85 * dip)
    top_caption(d, ["…WHETHER YOU'RE", "DOING IT FOR THEM."], t, dur, accent={"FOR", "THEM."})


def s8_applause(d, t, dur):
    p = t / dur
    # years later: a full, warm house on its feet. The performer barely looks up.
    if p < 0.5:
        u = p / 0.5
        seats_view(d, t, z=lerp(1.0, 1.08, u), crowd=crowd_fn(t, dur, "full", 9), warm=1.0, strum=1)
        dust(d, t, 0.6, n=60, color=(255, 220, 150))
    else:
        u = (p - 0.5) / 0.5
        cam = cam_lerp((0, -420, 0.7), (0, -340, 0.85), u)
        stage_view(d, cam, t, spot=0.5, lights=1, warm=1.0)
        performer(d, cam, 0, t, strum=1.0, head_down=0.3)
        front_rows(d, cam, t, crowd=crowd_fn(t, dur, "full", 9), warm=1.0)
        dust(d, t, 0.6, n=60, color=(255, 220, 150))
    if p < 0.12:
        pill(d, W / 2, H - 140, "YEARS LATER", 1 - ramp(p, 0.09, 0.03), 30, inverted=True)
    top_caption(d, ["BECAUSE IF YOU NEED", "APPLAUSE TO CONTINUE…"], t, dur, accent={"APPLAUSE"})


def s9_quiet(d, t, dur):
    p = t / dur
    # the room goes quiet and dark, seat by seat. The one on stage keeps playing.
    cam = cam_lerp((0, -340, 0.85), (0, -300, 1.0), sstep(p))
    warm = 1 - sstep(ramp(t, dur * 0.2, dur * 0.6))
    stage_view(d, cam, t, spot=1 - warm * 0.5, lights=warm, warm=warm)
    performer(d, cam, 0, t, strum=1.0, head_down=0.3)
    front_rows(d, cam, t, crowd=crowd_fn(t, dur, "quiet", 9), warm=warm)
    darkness(d, W / 2, H / 2 - 100, 0.5 * (1 - warm))
    top_caption(d, ["…YOU'LL STOP WHEN", "THE ROOM GOES QUIET."], t, dur, accent={"STOP", "QUIET."})
s9_quiet.seamless = True


def s10_final(d, t, dur):
    cam = Cam(0, -300, 1.0)
    stage_view(d, cam, t, spot=1, lights=0)
    performer(d, cam, 0, t, strum=1.0, head_down=0.3)
    front_rows(d, cam, t)
    overlay(d, (0, 0, 0), 0.6)
    final_card(d, t, dur, ["WORK EVEN WHEN", "NOBODY WATCHES."], [WHITE, GOLD], size=110, glow_col=GOLD)


SCENES = [s0_believe, s1_laugh, s2_doubt, s3_care, s4_sometimes, s5_no_one, s6_find_out, s7_for_them, s8_applause,
          s9_quiet, s10_final, s_follow]
