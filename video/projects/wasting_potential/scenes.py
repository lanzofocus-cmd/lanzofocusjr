"""YOU'RE WASTING YOUR POTENTIAL."""
from render import (W, H, CY, WHITE, GREY, DIM, font, clamp, ramp, lerp, col, polyline, circle, person,
                    dashed_person, dashed, pill, label, check, caption, s_follow)
import math

TITLE = ("YOU'RE WASTING", "YOUR POTENTIAL")
OUTPUT = "Youre_Wasting_Your_Potential_16x9.mp4"
FOLLOW_SUB = ("FOR IDEAS, LESSONS, AND PERSPECTIVES", "THAT CHALLENGE THE WAY YOU THINK.")
LINES = [
    "You're not failing because you're incapable.",
    "You're failing to see how much you're capable of.",
    "You have ideas you never acted on.",
    "Goals you abandoned before giving them a real chance.",
    "And abilities you've never developed because you kept telling yourself…",
    "\"Maybe later.\"",
    "But potential means nothing if you never use it.",
    "The world doesn't reward the person you could have become.",
    "It rewards what you actually do.",
    "So stop measuring yourself by your dreams.",
    "Start measuring yourself by your actions.",
    "Because one day…",
    "You'll either look back at the life you built…",
    "Or the life you kept telling yourself you would build.",
    "Follow LanzoFocus for ideas, lessons, and perspectives that challenge the way you think.",
]


# ---------------------------------------------------------------- helpers
def bulb(d, cx, cy, s, a, lit=0.0):
    r = 60 * s
    fill = col(WHITE, a * lit) if lit > 0 else None
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col(WHITE, a), width=max(3, int(6 * s)), fill=fill)
    d.rounded_rectangle([cx - 28 * s, cy + r - 4, cx + 28 * s, cy + r + 40 * s], int(8 * s), outline=col(WHITE, a), width=max(3, int(5 * s)))
    d.line([(cx - 22 * s, cy + r + 14 * s), (cx + 22 * s, cy + r + 14 * s)], fill=col(WHITE, a), width=max(2, int(4 * s)))
    if lit > 0.5:
        for i in range(8):
            ang = math.radians(-90 + (i - 3.5) * 25)
            r0, r1 = r + 20 * s, r + 50 * s
            d.line([(cx + r0 * math.cos(ang), cy + r0 * math.sin(ang)), (cx + r1 * math.cos(ang), cy + r1 * math.sin(ang))], fill=col(WHITE, a * lit), width=max(2, int(5 * s)))


def house(d, cx, base, s, a, dashed_line=False, c=WHITE):
    w, h, roof = 170 * s, 170 * s, 110 * s
    pts = [(cx - w, base), (cx - w, base - h), (cx, base - h - roof), (cx + w, base - h), (cx + w, base), (cx - w, base)]
    if dashed_line:
        dashed(d, pts, col(c, a), max(3, int(5 * s)), 18 * s, 12 * s)
        dashed(d, [(cx - 35 * s, base), (cx - 35 * s, base - 90 * s), (cx + 35 * s, base - 90 * s), (cx + 35 * s, base)], col(c, a), max(3, int(4 * s)), 12 * s, 9 * s)
    else:
        polyline(d, pts, a, c, max(3, int(6 * s)))
        d.rectangle([cx - 35 * s, base - 90 * s, cx + 35 * s, base], fill=col(c, a))
        for sx in (-1, 1):
            x = cx + sx * 100 * s
            d.rectangle([x - 32 * s, base - 140 * s, x + 32 * s, base - 85 * s], fill=col(c, a))


def cloud(d, cx, cy, s, a, c=WHITE):
    for dx, dy, r in ((-110, 20, 70), (-30, -30, 95), (70, -10, 80), (140, 30, 55)):
        d.ellipse([cx + (dx - r) * s, cy + (dy - r) * s, cx + (dx + r) * s, cy + (dy + r) * s], outline=col(c, a), width=6)
    # flatten bottom: cover inner outlines
    d.rounded_rectangle([cx - 175 * s, cy + 20 * s, cx + 190 * s, cy + 85 * s], int(30 * s), fill=(0, 0, 0, int(255 * a)), outline=col(c, a), width=6)
    d.rectangle([cx - 150 * s, cy - 10 * s, cx + 160 * s, cy + 30 * s], fill=(0, 0, 0, int(255 * a)))


def ruler(d, x, y0, y1, a):
    d.rounded_rectangle([x - 26, y0, x + 26, y1], 6, outline=col(WHITE, a), width=4)
    n = int((y1 - y0) / 30)
    for i in range(1, n):
        yy = y0 + i * 30
        d.line([(x - 26, yy), (x - 26 + (22 if i % 5 == 0 else 12), yy)], fill=col(WHITE, a), width=3)


# ---------------------------------------------------------------- scenes
def p_incapable(d, t, dur):
    caption(d, ["YOU'RE NOT FAILING BECAUSE", "YOU'RE INCAPABLE."], t, dur, accent={"NOT", "INCAPABLE."})
    base = CY + 230
    polyline(d, [(W / 2 - 400, base), (W / 2 + 400, base)], ramp(t, 0.1, 0.7), WHITE, 4)
    person(d, W / 2, base, 1.5, ramp(t, 0.2))
    a = ramp(t, 0.5)
    pill(d, W / 2, base - 290, "INCAPABLE", a, 30, inverted=False)
    polyline(d, [(W / 2 - 150, base - 290), (W / 2 + 150, base - 290)], ramp(t, dur * 0.55, 0.4), WHITE, 7)


def p_capable(d, t, dur):
    caption(d, ["YOU'RE FAILING TO SEE HOW MUCH", "YOU'RE CAPABLE OF."], t, dur, accent={"SEE", "CAPABLE"})
    wl = CY + 20
    a = ramp(t, 0.1)
    dashed(d, [(W / 2 - 640, wl), (W / 2 + 640, wl)], col(GREY, a), 3, 22, 14)
    tip = [(W / 2 - 110, wl), (W / 2 - 30, wl - 120), (W / 2 + 40, wl - 70), (W / 2 + 120, wl)]
    polyline(d, tip, ramp(t, 0.2, 0.6), WHITE, 6)
    under = [(W / 2 - 110, wl), (W / 2 - 330, wl + 140), (W / 2 - 220, wl + 330), (W / 2 + 60, wl + 380),
             (W / 2 + 320, wl + 260), (W / 2 + 280, wl + 90), (W / 2 + 120, wl)]
    polyline(d, under, ramp(t, 0.8, 1.2), WHITE, 6)
    label(d, W / 2 + 350, wl - 60, "WHAT YOU SEE", ramp(t, 0.6), 24, GREY)
    label(d, W / 2 - 10, wl + 210, "WHAT YOU'RE", ramp(t, 1.6), 28)
    label(d, W / 2 - 10, wl + 250, "CAPABLE OF", ramp(t, 1.6), 28)


def p_ideas(d, t, dur):
    caption(d, ["YOU HAVE IDEAS", "YOU NEVER ACTED ON."], t, dur, accent={"IDEAS", "NEVER"})
    for i in range(5):
        cx = W / 2 + (i - 2) * 220
        a = ramp(t, 0.2 + i * 0.15)
        lit = 0
        if i == 2:
            lit = max(0, math.sin(t * 9)) * (1 - ramp(t, 1.4, 0.5))
        bulb(d, cx, CY + 40, 0.9, a * (1 if i == 2 else 0.75), lit)
    pill(d, W / 2, CY + 260, "NEVER ACTED ON", ramp(t, 1.0) * 0.9, 24, inverted=False)


def p_goals(d, t, dur):
    caption(d, ["GOALS YOU ABANDONED BEFORE", "GIVING THEM A REAL CHANCE."], t, dur, accent={"ABANDONED"})
    base = CY + 260
    x0, x1 = W / 2 - 560, W / 2 + 460
    peak = (x1, base - 360)
    path = [(x0, base), (W / 2 - 200, base - 100), (W / 2 + 60, base - 170), peak]
    polyline(d, path[:2], ramp(t, 0.1, 0.6), WHITE, 6)
    dashed(d, path[1:], col(DIM, ramp(t, 0.5)), 5, 20, 14)
    # flag on the peak
    fa = ramp(t, 0.4)
    d.line([peak, (peak[0], peak[1] - 120)], fill=col(GREY, fa), width=5)
    d.polygon([(peak[0], peak[1] - 120), (peak[0] + 90, peak[1] - 95), (peak[0], peak[1] - 70)], fill=col(GREY, fa))
    label(d, peak[0], peak[1] + 40, "GOAL", fa, 22, GREY)
    # figure walks a little, then turns back
    k = ramp(t, 0.5, 0.8) - 0.5 * ramp(t, 1.6, 0.8)
    px = lerp(x0 + 60, W / 2 - 230, clamp(k))
    py = lerp(base, base - 90, clamp(k))
    person(d, px, py, 1.0, ramp(t, 0.2))
    pill(d, px, py - 200, "GAVE UP", ramp(t, 1.8) * 0.9, 22, inverted=False)


def p_abilities(d, t, dur):
    caption(d, ["AND ABILITIES YOU'VE NEVER DEVELOPED", "BECAUSE YOU KEPT TELLING YOURSELF…"], t, dur, accent={"ABILITIES", "NEVER"})
    skills = [("CREATIVITY", 0.18), ("DISCIPLINE", 0.12), ("LEADERSHIP", 0.22), ("CONFIDENCE", 0.15)]
    x0, x1 = W / 2 - 160, W / 2 + 460
    for i, (name, lvl) in enumerate(skills):
        y = CY - 40 + i * 95
        a = ramp(t, 0.2 + i * 0.2)
        d.text((x0 - 40, y), name, font=font(36), fill=col(WHITE, a), anchor="rm")
        dashed(d, [(x0, y - 22), (x1, y - 22), (x1, y + 22), (x0, y + 22), (x0, y - 22)], col(DIM, a), 3, 14, 10)
        fill = (x1 - x0) * lvl * ramp(t, 0.4 + i * 0.2, 0.6)
        if fill > 4:
            d.rounded_rectangle([x0, y - 22, x0 + fill, y + 22], 10, fill=col(WHITE, a))
        label(d, x1 + 60, y, f"{int(lvl * 100)}%", a, 26, GREY)


def p_later(d, t, dur):
    caption(d, ["“MAYBE LATER.”"], t, dur, y=190, size=84, accent={"“MAYBE", "LATER.”"})
    items = ["START THE BUSINESS", "LEARN THE SKILL", "WRITE THE BOOK", "GET IN SHAPE"]
    x0, y0 = W / 2 - 330, CY - 60
    for i, it in enumerate(items):
        a = ramp(t, 0.15 + i * 0.15, 0.3)
        y = y0 + i * 90
        d.rounded_rectangle([x0, y, x0 + 50, y + 50], 8, outline=col(WHITE, a), width=5)
        d.text((x0 + 80, y + 25), it, font=font(38), fill=col(WHITE, a), anchor="lm")
        pill(d, x0 + 600, y + 25, "LATER", ramp(t, 0.5 + i * 0.15, 0.3) * 0.8, 22, inverted=False)


def p_unused(d, t, dur):
    caption(d, ["BUT POTENTIAL MEANS NOTHING", "IF YOU NEVER USE IT."], t, dur, accent={"NOTHING", "USE"})
    a = ramp(t, 0.2)
    cx, cy = W / 2 - 250, CY + 80
    w, h = 300, 140
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], 24, outline=col(WHITE, a), width=7)
    d.rounded_rectangle([cx + w / 2 + 6, cy - 26, cx + w / 2 + 22, cy + 26], 6, fill=col(WHITE, a))
    d.rounded_rectangle([cx - w / 2 + 18, cy - h / 2 + 18, cx + w / 2 - 18, cy + h / 2 - 18], 10, fill=col(WHITE, a))
    label(d, cx, cy + 120, "POTENTIAL 100%", a, 26)
    # usage meter at 0
    gx, gy = W / 2 + 300, CY + 120
    r = 150
    d.arc([gx - r, gy - r, gx + r, gy + r], 180, 360, fill=col(WHITE, ramp(t, 0.5)), width=7)
    ang = math.radians(180 + 4)
    d.line([(gx, gy), (gx + (r - 30) * math.cos(ang), gy + (r - 30) * math.sin(ang))], fill=col(WHITE, ramp(t, 0.5)), width=8)
    d.ellipse([gx - 14, gy - 14, gx + 14, gy + 14], fill=col(WHITE, ramp(t, 0.5)))
    label(d, gx, gy + 60, "USED 0%", ramp(t, 0.8), 26, GREY)


def podium(d, cx, base, a, c=WHITE):
    d.rectangle([cx - 110, base - 110, cx + 110, base], outline=col(c, a), width=5)
    d.text((cx, base - 55), "1", font=font(60), fill=col(c, a), anchor="mm")


def p_could_have(d, t, dur):
    caption(d, ["THE WORLD DOESN'T REWARD THE PERSON", "YOU COULD HAVE BECOME."], t, dur, accent={"DOESN'T", "COULD"})
    base = CY + 260
    a = ramp(t, 0.2)
    polyline(d, [(W / 2 - 500, base), (W / 2 + 500, base)], a, WHITE, 4)
    podium(d, W / 2, base, a, GREY)
    dashed_person(d, W / 2, base - 110, 1.3, ramp(t, 0.5), GREY)
    label(d, W / 2, base + 40, "WHO YOU COULD BE", ramp(t, 0.7), 24, GREY)
    # trophy crossed out
    tx, ty = W / 2 + 360, CY + 20
    ta = ramp(t, 0.9)
    d.arc([tx - 60, ty - 60, tx + 60, ty + 60], 0, 180, fill=col(GREY, ta), width=6)
    d.line([(tx - 60, ty), (tx + 60, ty)], fill=col(GREY, ta), width=6)
    d.line([(tx, ty + 60), (tx, ty + 100)], fill=col(GREY, ta), width=6)
    d.line([(tx - 40, ty + 100), (tx + 40, ty + 100)], fill=col(GREY, ta), width=6)
    polyline(d, [(tx - 90, ty - 80), (tx + 90, ty + 130)], ramp(t, 1.4, 0.4), WHITE, 6)


def p_actually_do(d, t, dur):
    caption(d, ["IT REWARDS WHAT", "YOU ACTUALLY DO."], t, dur, accent={"ACTUALLY", "DO."})
    base = CY + 260
    polyline(d, [(W / 2 - 500, base), (W / 2 + 500, base)], 1, WHITE, 4)
    podium(d, W / 2, base, 1)
    person(d, W / 2, base - 110, 1.3, ramp(t, 0.1, 0.4))
    for i, txt in enumerate(["SHOWED UP", "DID THE WORK", "KEPT GOING"]):
        a = ramp(t, 0.5 + i * 0.3, 0.3)
        pill(d, W / 2 - 420, CY - 20 + i * 80, txt, a, 22)
    tx, ty = W / 2 + 360, CY + 20
    ta = ramp(t, 1.0)
    d.arc([tx - 60, ty - 60, tx + 60, ty + 60], 0, 180, fill=col(WHITE, ta), width=6)
    d.line([(tx - 60, ty), (tx + 60, ty)], fill=col(WHITE, ta), width=6)
    d.line([(tx, ty + 60), (tx, ty + 100)], fill=col(WHITE, ta), width=6)
    d.line([(tx - 40, ty + 100), (tx + 40, ty + 100)], fill=col(WHITE, ta), width=6)
    for i in range(6):
        ang = math.radians(-160 + i * 28)
        d.line([(tx + 90 * math.cos(ang), ty + 10 + 90 * math.sin(ang)), (tx + 120 * math.cos(ang), ty + 10 + 120 * math.sin(ang))], fill=col(WHITE, ramp(t, 1.3)), width=4)


def p_dreams(d, t, dur):
    caption(d, ["SO STOP MEASURING YOURSELF", "BY YOUR DREAMS."], t, dur, accent={"STOP", "DREAMS."})
    a = ramp(t, 0.2) * (1 - 0.6 * ramp(t, dur * 0.6, 0.6))
    cloud(d, W / 2 + 60, CY + 20, 1.2, a)
    label(d, W / 2 + 60, CY + 40, "DREAMS", a, 30)
    ruler(d, W / 2 - 330, CY - 150, CY + 250, ramp(t, 0.5))
    polyline(d, [(W / 2 - 420, CY + 290), (W / 2 + 330, CY - 190)], ramp(t, dur * 0.6, 0.4), (160, 160, 160, 255), 7)


def p_actions(d, t, dur):
    caption(d, ["START MEASURING YOURSELF", "BY YOUR ACTIONS."], t, dur, accent={"START", "ACTIONS."})
    base = CY + 260
    ruler(d, W / 2 - 420, CY - 180, base, ramp(t, 0.1))
    for i in range(6):
        h = 50 + i * 60
        k = ramp(t, 0.3 + i * 0.18, 0.4)
        x = W / 2 - 300 + i * 120
        if k > 0:
            d.rounded_rectangle([x, base - h * k, x + 80, base], 8, fill=col(WHITE, 1))
    polyline(d, [(W / 2 - 340, base), (W / 2 + 460, base)], ramp(t, 0.1), WHITE, 4)
    label(d, W / 2 + 80, base + 40, "ACTIONS", ramp(t, 0.4), 24)


def p_one_day(d, t, dur):
    caption(d, ["BECAUSE ONE DAY…"], t, dur, y=190, size=76, accent={"ONE", "DAY…"})
    hz = CY + 220
    a = ramp(t, 0.1)
    polyline(d, [(W / 2 - 600, hz), (W / 2 + 600, hz)], a, WHITE, 4)
    rise = ramp(t, 0.2, max(0.8, dur * 0.9))
    r = 130
    cy = hz + r - rise * 1.4 * r
    d.pieslice([W / 2 - r, cy - r, W / 2 + r, cy + r], 180, 360, outline=col(WHITE, a), width=7)
    d.rectangle([W / 2 - r - 10, hz + 3, W / 2 + r + 10, hz + r + 10], fill=(0, 0, 0, 0))


def scene_life(d, t, dur, built):
    base = CY + 260
    a = ramp(t, 0.1)
    polyline(d, [(W / 2 - 640, base), (W / 2 + 560, base)], a, WHITE, 4)
    if built:
        house(d, W / 2 - 300, base, 1.1, ramp(t, 0.3))
        label(d, W / 2 - 300, base + 44, "THE LIFE YOU BUILT", ramp(t, 0.6), 24)
    else:
        house(d, W / 2 - 300, base, 1.1, ramp(t, 0.3), dashed_line=True, c=GREY)
        label(d, W / 2 - 300, base + 44, "THE LIFE YOU WOULD BUILD", ramp(t, 0.6), 24, GREY)
    # older figure looking back (left), with a cane
    px = W / 2 + 330
    person(d, px, base, 1.3, 1)
    d.line([(px - 70, base - 60), (px - 85, base)], fill=col(WHITE, 1), width=6)
    dashed(d, [(px - 120, base - 150), (W / 2 - 60, base - 200)], col(WHITE, ramp(t, 0.8)), 4, 16, 12)


def p_built(d, t, dur):
    caption(d, ["YOU'LL EITHER LOOK BACK", "AT THE LIFE YOU BUILT…"], t, dur, accent={"BUILT…"})
    scene_life(d, t, dur, True)


def p_would_build(d, t, dur):
    caption(d, ["OR THE LIFE YOU KEPT TELLING", "YOURSELF YOU WOULD BUILD."], t, dur, accent={"WOULD", "BUILD."})
    scene_life(d, t, dur, False)


SCENES = [p_incapable, p_capable, p_ideas, p_goals, p_abilities, p_later, p_unused, p_could_have,
          p_actually_do, p_dreams, p_actions, p_one_day, p_built, p_would_build, s_follow]
