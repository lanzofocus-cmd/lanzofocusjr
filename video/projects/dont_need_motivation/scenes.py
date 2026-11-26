"""YOU DON'T NEED TO FEEL MOTIVATED."""
from render import *  # noqa: F401,F403
from render import (W, H, CY, WHITE, GREY, DIM, font, clamp, ease, ramp, lerp, col, polyline, rrect,
                    arc_pts, circle, person, dashed_person, dashed, pill, label, check, caption, s_follow)
import math

TITLE = ("YOU DON'T NEED", "TO FEEL MOTIVATED")
OUTPUT = "You_Dont_Need_To_Feel_Motivated_16x9.mp4"
LINES = [
    "You keep waiting for motivation.", "For the perfect mood.", "The perfect time.", "The perfect circumstances.",
    "But motivation is unreliable.", "Some days you'll feel unstoppable.",
    "Other days, getting out of bed will feel like a challenge.",
    "And if your progress depends on how you feel", "You'll only move when life feels easy.",
    "That's why discipline matters.", "Not because you always want to do the work",
    "But because you decided it matters.", "You don't need to feel motivated to take one step.",
    "You just need to take it.", "And sometimes",
    "That one step is enough to remind you that you're still moving.",
    "Follow LanzoFocus for ideas, lessons, and perspectives that help you become a better version of yourself.",
]


# ---------------------------------------------------------------- helpers
def battery(d, cx, cy, level, a=1.0, w=260, h=120, bolt=False):
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], 22, outline=col(WHITE, a), width=7)
    d.rounded_rectangle([cx + w / 2 + 6, cy - 24, cx + w / 2 + 22, cy + 24], 6, fill=col(WHITE, a))
    inner = (w - 36) * clamp(level)
    if inner > 4:
        d.rounded_rectangle([cx - w / 2 + 18, cy - h / 2 + 18, cx - w / 2 + 18 + inner, cy + h / 2 - 18], 10, fill=col(WHITE, a))
    if bolt:
        pts = [(cx + 10, cy - 44), (cx - 26, cy + 6), (cx, cy + 6), (cx - 10, cy + 44), (cx + 26, cy - 6), (cx, cy - 6)]
        d.polygon(pts, fill=(0, 0, 0, int(255 * a)), outline=None)


def face(d, cx, cy, r, mood, a=1.0, width=7):
    """mood in [-1, 1]: -1 frown, 0 flat, 1 smile."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col(WHITE, a), width=width)
    er = r * 0.09
    for sx in (-1, 1):
        ex, ey = cx + sx * r * 0.35, cy - r * 0.22
        d.ellipse([ex - er, ey - er, ex + er, ey + er], fill=col(WHITE, a))
    pts = []
    for i in range(21):
        f = i / 20
        x = cx + lerp(-r * 0.42, r * 0.42, f)
        y = cy + r * 0.32 + mood * r * 0.22 * (1 - (2 * f - 1) ** 2) - mood * r * 0.05
        pts.append((x, y))
    polyline(d, pts, a, col(WHITE, a), width)


def wave(x, amp, phase=0.0):
    return amp * (0.6 * math.sin(x * 0.011 + phase) + 0.4 * math.sin(x * 0.027 + 1.7 + phase))


# ---------------------------------------------------------------- scenes
def m_waiting(d, t, dur):
    caption(d, ["YOU KEEP WAITING", "FOR MOTIVATION."], t, dur, accent={"MOTIVATION."})
    base = CY + 220
    polyline(d, [(W / 2 - 520, base), (W / 2 + 520, base)], ramp(t, 0.1, 0.8), WHITE, 4)
    person(d, W / 2 - 230, base, 1.4, ramp(t, 0.2))
    blink = 0.35 + 0.65 * (0.5 + 0.5 * math.sin(t * 5))
    battery(d, W / 2 + 200, CY + 40, 0.08, ramp(t, 0.4) * blink)
    label(d, W / 2 + 200, CY + 140, "MOTIVATION", ramp(t, 0.6))
    dots = "." * (1 + int(t * 2) % 3)
    pill(d, W / 2 - 230, base - 230, "WAITING" + dots, ramp(t, 0.9) * 0.9, 24, inverted=False)


def m_mood(d, t, dur):
    caption(d, ["FOR THE PERFECT MOOD."], t, dur, y=190, size=76, accent={"MOOD."})
    a = ramp(t, 0.2)
    mood = lerp(-0.6, 1.0, ramp(t, 0.5, 1.2))
    face(d, W / 2, CY + 20, 150, mood, a)
    x0, x1, y = W / 2 - 300, W / 2 + 300, CY + 260
    polyline(d, [(x0, y), (x1, y)], a, WHITE, 5)
    k = lerp(0.2, 1.0, ramp(t, 0.5, 1.2))
    kx = lerp(x0, x1, k)
    d.ellipse([kx - 18, y - 18, kx + 18, y + 18], fill=col(WHITE, a))
    label(d, x0, y + 40, "BAD", a, 22, GREY)
    label(d, x1, y + 40, "PERFECT", a, 22)


def m_time(d, t, dur):
    caption(d, ["THE PERFECT TIME."], t, dur, y=190, size=76, accent={"TIME."})
    cx, cy, r = W / 2, CY + 60, 170
    a = ramp(t, 0.1)
    circle(d, cx, cy, r, ramp(t, 0.1, 0.8))
    for i in range(12):
        ang = math.radians(i * 30)
        r0 = r - (30 if i % 3 == 0 else 18)
        d.line([(cx + r0 * math.cos(ang), cy + r0 * math.sin(ang)), (cx + (r - 12) * math.cos(ang), cy + (r - 12) * math.sin(ang))], fill=col(WHITE, a), width=5)
    spin = t * 2.2
    for length, speed, wdt in ((r * 0.5, 1, 9), (r * 0.78, 12, 6)):
        ang = -math.pi / 2 + spin * speed
        d.line([(cx, cy), (cx + length * math.cos(ang), cy + length * math.sin(ang))], fill=col(WHITE, a), width=wdt)
    d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=col(WHITE, a))


def m_circumstances(d, t, dur):
    caption(d, ["THE PERFECT CIRCUMSTANCES."], t, dur, y=190, size=76, accent={"CIRCUMSTANCES."})
    items = ["PERFECT MOOD", "PERFECT TIME", "PERFECT CIRCUMSTANCES"]
    x0, y0 = W / 2 - 300, CY - 40
    for i, it in enumerate(items):
        st = 0.2 + i * 0.35
        a = ramp(t, st, 0.35)
        y = y0 + i * 100
        d.rounded_rectangle([x0, y, x0 + 56, y + 56], 10, outline=col(WHITE, a), width=5)
        d.text((x0 + 90, y + 28), it, font=font(42), fill=col(WHITE, a), anchor="lm")
    q = ramp(t, 1.4, 0.4)
    pill(d, W / 2, y0 + 360, "STILL WAITING...", q * 0.9, 24, inverted=False)


def m_unreliable(d, t, dur):
    caption(d, ["BUT MOTIVATION", "IS UNRELIABLE."], t, dur, accent={"UNRELIABLE."})
    x0, x1, base = W / 2 - 620, W / 2 + 620, CY + 120
    a = ramp(t, 0.1)
    polyline(d, [(x0, base + 200), (x1, base + 200)], a, DIM, 3)
    polyline(d, [(x0, base - 220), (x0, base + 200)], a, DIM, 3)
    pts = [(x, base + wave(x - x0, 150)) for x in range(int(x0), int(x1) + 1, 8)]
    polyline(d, pts, ramp(t, 0.3, max(0.6, dur * 0.7)), WHITE, 6)
    label(d, x0 + 10, base - 250, "MOTIVATION", a, 24)
    label(d, x1 - 40, base + 235, "TIME", a, 22, GREY)


def m_unstoppable(d, t, dur):
    caption(d, ["SOME DAYS YOU'LL", "FEEL UNSTOPPABLE."], t, dur, accent={"UNSTOPPABLE."})
    a = ramp(t, 0.2)
    lvl = ramp(t, 0.3, 1.0)
    cx, cy = W / 2, CY + 60
    battery(d, cx, cy, lvl, a, w=360, h=170, bolt=lvl > 0.95)
    burst = ramp(t, 1.2, 0.5)
    for i in range(16):
        ang = math.radians(i * 22.5)
        r0, r1 = 240, 240 + 50 * burst
        d.line([(cx + r0 * math.cos(ang) * 1.2, cy + r0 * math.sin(ang) * 0.8), (cx + r1 * math.cos(ang) * 1.2, cy + r1 * math.sin(ang) * 0.8)], fill=col(WHITE, burst), width=5)
    label(d, cx, cy + 150, f"{int(lvl * 100)}%", a, 30)


def m_bed(d, t, dur):
    caption(d, ["OTHER DAYS, GETTING OUT OF BED", "WILL FEEL LIKE A CHALLENGE."], t, dur, accent={"BED", "CHALLENGE."})
    a = ramp(t, 0.2)
    cx, base = W / 2 - 80, CY + 230
    # bed frame
    polyline(d, [(cx - 330, base - 260), (cx - 330, base + 20)], ramp(t, 0.1, 0.5), WHITE, 7)
    polyline(d, [(cx + 330, base - 120), (cx + 330, base + 20)], ramp(t, 0.1, 0.5), WHITE, 7)
    polyline(d, [(cx - 330, base - 60), (cx + 330, base - 60)], ramp(t, 0.2, 0.6), WHITE, 7)
    # pillow + head
    d.rounded_rectangle([cx - 300, base - 130, cx - 180, base - 70], 24, outline=col(WHITE, a), width=5)
    d.ellipse([cx - 270, base - 175, cx - 200, base - 105], fill=col(WHITE, a))
    # blanket
    sway = math.sin(t * 1.5) * 4
    d.rounded_rectangle([cx - 190, base - 140 + sway, cx + 320, base - 66], 30, fill=col(WHITE, a))
    # zzz
    for i in range(3):
        za = ramp(t, 0.8 + i * 0.3, 0.3) * (0.5 + 0.5 * math.sin(t * 3 - i))
        d.text((cx - 150 + i * 50, base - 220 - i * 50), "Z", font=font(34 + i * 10), fill=col(WHITE, za), anchor="mm")
    battery(d, W / 2 + 470, CY - 20, 0.1, ramp(t, 0.9), w=200, h=90)
    d.text((W / 2 + 470, CY + 70), "7:42 AM", font=font(40), fill=col(WHITE, ramp(t, 1.0)), anchor="mm")


def m_depends(d, t, dur):
    caption(d, ["AND IF YOUR PROGRESS", "DEPENDS ON HOW YOU FEEL…"], t, dur, accent={"PROGRESS", "FEEL…"})
    a = ramp(t, 0.2)
    mood = math.sin(t * 2.2)
    fx, fy = W / 2 - 360, CY + 60
    face(d, fx, fy, 110, mood, a)
    label(d, fx, fy + 150, "HOW YOU FEEL", a, 24)
    dashed(d, [(fx + 130, fy), (W / 2 - 60, fy)], col(WHITE, ramp(t, 0.6)), 4, 16, 12)
    x0, x1 = W / 2 - 20, W / 2 + 520
    d.rounded_rectangle([x0, fy - 36, x1, fy + 36], 36, outline=col(WHITE, a), width=6)
    prog = 0.25 + 0.2 * (mood + 1) / 2
    d.rounded_rectangle([x0 + 12, fy - 24, x0 + 12 + (x1 - x0 - 24) * prog, fy + 24], 24, fill=col(WHITE, a))
    label(d, (x0 + x1) / 2, fy + 90, "YOUR PROGRESS", a, 24)


def m_easy(d, t, dur):
    caption(d, ["YOU'LL ONLY MOVE", "WHEN LIFE FEELS EASY."], t, dur, accent={"EASY."})
    base = CY + 230
    xa, xb = W / 2 - 600, W / 2 - 20
    hill = [(xa, base), (xb, base), (W / 2 + 380, base - 300), (W / 2 + 620, base - 300)]
    polyline(d, hill, ramp(t, 0.1, 0.9), WHITE, 5)
    label(d, (xa + xb) / 2, base + 40, "EASY", ramp(t, 0.5), 24, GREY)
    label(d, W / 2 + 230, base - 110, "HARD", ramp(t, 0.7), 24)
    k = ramp(t, 0.4, max(0.8, dur * 0.5))
    person(d, lerp(xa + 60, xb - 50, k), base, 1.1, ramp(t, 0.2))
    pill(d, xb - 50, base - 210, "STOPPED", ramp(t, 0.4 + max(0.8, dur * 0.5)) * 0.9, 24, inverted=False)


def m_discipline(d, t, dur):
    caption(d, ["THAT'S WHY", "DISCIPLINE MATTERS."], t, dur, accent={"DISCIPLINE"})
    x0, x1, mid = W / 2 - 620, W / 2 + 620, CY + 120
    pts = [(x, mid + wave(x - x0, 120)) for x in range(int(x0), int(x1) + 1, 8)]
    polyline(d, pts, ramp(t, 0.1, 0.8), (90, 90, 90, 255), 5)
    label(d, x1 - 60, mid - 170, "MOTIVATION", ramp(t, 0.5), 22, GREY)
    line = [(x0, mid + 170), (x1, mid - 120)]
    polyline(d, line, ramp(t, 0.6, 1.0), WHITE, 8)
    label(d, x1 - 80, mid - 70, "DISCIPLINE", ramp(t, 1.2), 26)


def m_want(d, t, dur):
    caption(d, ["NOT BECAUSE YOU ALWAYS", "WANT TO DO THE WORK…"], t, dur, accent={"WANT"})
    a = ramp(t, 0.2)
    cx, cy = W / 2, CY + 80
    d.rounded_rectangle([cx - 300, cy - 170, cx + 300, cy + 170], 26, outline=col(WHITE, a), width=6)
    d.text((cx, cy - 100), "THE WORK", font=font(48), fill=col(WHITE, a), anchor="mm")
    label(d, cx - 120, cy + 40, "WANT TO?", ramp(t, 0.6), 30)
    # toggle switched off
    tx, ty = cx + 120, cy + 40
    d.rounded_rectangle([tx - 70, ty - 36, tx + 70, ty + 36], 36, outline=col(GREY, ramp(t, 0.6)), width=5)
    d.ellipse([tx - 60, ty - 26, tx - 8, ty + 26], fill=col(GREY, ramp(t, 0.6)))
    label(d, cx + 220, cy + 40, "NO", ramp(t, 0.9), 26, GREY)


def m_decided(d, t, dur):
    caption(d, ["BUT BECAUSE YOU", "DECIDED IT MATTERS."], t, dur, accent={"DECIDED"})
    a = 1.0
    cx, cy = W / 2, CY + 80
    d.rounded_rectangle([cx - 300, cy - 170, cx + 300, cy + 170], 26, outline=col(WHITE, a), width=6)
    d.text((cx, cy - 100), "THE WORK", font=font(48), fill=col(WHITE, a), anchor="mm")
    k = ramp(t, 0.3, 0.6)
    tx, ty = cx, cy + 40
    d.rounded_rectangle([tx - 70, ty - 36, tx + 70, ty + 36], 36, outline=col(WHITE, a), width=5,
                        fill=col(WHITE, k))
    kx = lerp(tx - 34, tx + 34, k)
    d.ellipse([kx - 26, ty - 26, kx + 26, ty + 26], fill=(0, 0, 0, 255) if k > 0.5 else col(GREY, 1))
    pill(d, cx, cy + 112, "I DECIDED", ramp(t, 0.9), 26)


def stairs(d, x0, base, n=5, sw=150, sh=70, p=1.0, fill=WHITE):
    pts = [(x0 - 200, base)]
    for i in range(n):
        x = x0 + i * sw
        pts += [(x, base - i * sh), (x, base - (i + 1) * sh)]
    pts.append((x0 + n * sw, base - n * sh))
    polyline(d, pts, p, fill, 6)


def m_one_step(d, t, dur):
    caption(d, ["YOU DON'T NEED TO FEEL MOTIVATED", "TO TAKE ONE STEP."], t, dur, accent={"ONE", "STEP."})
    base = CY + 260
    x0 = W / 2 - 250
    stairs(d, x0, base, p=ramp(t, 0.1, 1.0))
    person(d, x0 - 90, base, 1.1, ramp(t, 0.3))
    battery(d, W / 2 - 560, CY - 40, 0.12, ramp(t, 0.8), w=180, h=80)
    label(d, W / 2 - 560, CY + 30, "MOTIVATION", ramp(t, 0.8), 20, GREY)


def m_take_it(d, t, dur):
    caption(d, ["YOU JUST NEED", "TO TAKE IT."], t, dur, accent={"TAKE"})
    base = CY + 260
    x0 = W / 2 - 250
    stairs(d, x0, base)
    k = ramp(t, 0.5, 0.7)
    x = lerp(x0 - 90, x0 + 75, k)
    y = base - 70 * k - math.sin(math.pi * k) * 60
    person(d, x, y, 1.1)
    pill(d, x0 + 75, base - 300, "STEP 1", ramp(t, 1.1), 24)
    battery(d, W / 2 - 560, CY - 40, 0.12, 1, w=180, h=80)
    label(d, W / 2 - 560, CY + 30, "MOTIVATION", 1, 20, GREY)


def m_sometimes(d, t, dur):
    caption(d, ["AND SOMETIMES…"], t, dur, y=190, size=76)
    cx, cy = W / 2, CY + 80
    pulse = 0.5 + 0.5 * math.sin(t * 4)
    r = 22 + 6 * pulse
    a = ramp(t, 0.2)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col(WHITE, a))
    for k in range(2):
        rr = 60 + ((t * 70 + k * 60) % 120)
        ra = a * (1 - (rr - 60) / 120)
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=col(WHITE, ra), width=3)


def m_still_moving(d, t, dur):
    caption(d, ["THAT ONE STEP IS ENOUGH TO REMIND YOU", "THAT YOU'RE STILL MOVING."], t, dur, accent={"STILL", "MOVING."})
    y = CY + 180
    x0, x1 = W / 2 - 640, W / 2 + 640
    a = ramp(t, 0.1)
    polyline(d, [(x0, y), (x1, y)], ramp(t, 0.1, 0.8), WHITE, 4)
    polyline(d, [(x1 - 30, y - 22), (x1, y), (x1 - 30, y + 22)], ramp(t, 0.8, 0.3), WHITE, 4)
    k = ramp(t, 0.4, max(1.0, dur * 0.8))
    for i in range(9):
        px = lerp(x0 + 80, x1 - 120, i / 8)
        fill = WHITE if lerp(x0 + 80, x1 - 120, k) >= px else DIM
        d.ellipse([px - 10, y - 10, px + 10, y + 10], fill=col(fill, a))
    px = lerp(x0 + 80, x1 - 120, k)
    person(d, px, y - 18, 1.0, a)
    pill(d, px, y + 70, "STILL MOVING", ramp(t, 1.2), 22)


SCENES = [m_waiting, m_mood, m_time, m_circumstances, m_unreliable, m_unstoppable, m_bed, m_depends,
          m_easy, m_discipline, m_want, m_decided, m_one_step, m_take_it, m_sometimes, m_still_moving, s_follow]
