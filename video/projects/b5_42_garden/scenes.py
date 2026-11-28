"""THE GARDEN OF RESULTS — two gardeners, one who keeps digging up the seeds to check, and one who waits.

World: two neighbouring garden plots split by a low picket fence, drawn as a cutaway so we can see under the soil.
THE IMPATIENT GARDENER (rust) plants, then digs the seeds up again and again to look; underground, the roots tear
and nothing survives. THE PATIENT GARDENER (sage) waters, shields the seedlings from the storm and waits; under
the soil the roots spread. Time-lapse: one side bursts into an enormous garden; the other is bare earth.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, rain, sun, dust, cloud)
from kit import s_follow

TITLE = ("THE GARDEN", "OF RESULTS")
OUTPUT = "142_The_Garden_Of_Results_16x9.mp4"
LINES = [
    "",
    "",
    "Stop digging up your progress…",
    "Just to check whether it's growing.",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.6, 4: 3.4}
GAPS = {2: 1.8, 3: 6.0}

IMP = (210, 110, 70, 255)
PAT = (130, 180, 120, 255)
SOIL = (90, 60, 40, 255)
SOIL_D = (60, 40, 28, 255)
FENCE_X = 0
SEEDS_L = [-1000 + i * 180 for i in range(5)]
SEEDS_R = [200 + i * 180 for i in range(5)]
CH = 210


def garden(d, cam, t, rainy=0.0, season=0.0):
    sky_t = mix((110, 170, 230, 255), (70, 80, 100, 255), rainy)
    draw_sky(d, sky_t, mix((230, 240, 220, 255), (130, 140, 150, 255), rainy))
    if rainy < 0.5:
        sun(d, W * 0.82, H * 0.18, 60, 1 - rainy, (255, 230, 170, 255))
    for j in range(4):
        cloud(d, (j * 500 + t * 20) % (W + 400) - 200, 130 + 40 * (j % 2), 60, col(mix(WHITE, (100, 100, 110, 255), rainy), 0.9))
    gy = cam.p(0, 0)[1]
    # soil cross-section
    d.rectangle([0, gy, W, H], fill=col(SOIL, 1))
    for k in range(1, 4):
        y = cam.p(0, k * 140)[1]
        d.line([(0, y), (W, y)], fill=col(SOIL_D, 1), width=max(1, int(cam.s(6))))
    d.rectangle([0, gy - cam.s(14), W, gy], fill=col(mix((90, 140, 70, 255), (120, 170, 80, 255), season), 1))
    # fence
    for k in range(-2, 3):
        x = FENCE_X + k * 50
        a, b = cam.p(x - 12, -160), cam.p(x + 12, 0)
        d.rectangle([a[0], a[1], b[0], b[1]], fill=(240, 236, 228, 255))
    d.rectangle(cam.box(FENCE_X - 130, -120, FENCE_X + 130, -100), fill=(240, 236, 228, 255))


def roots(d, cam, x, growth, torn=False, t=0.0):
    """Roots under a seed at x."""
    if growth <= 0:
        return
    r = random.Random(int(x))
    for k in range(5):
        ang = math.pi / 2 + r.uniform(-0.9, 0.9)
        L = 260 * growth * r.uniform(0.6, 1.1)
        pts = [cam.p(x, 10)]
        px, py = x, 10
        for j in range(5):
            ang += r.uniform(-0.3, 0.3)
            px += math.cos(ang) * L / 5
            py += math.sin(ang) * L / 5
            pts.append(cam.p(px, py))
        if torn:
            pts = pts[:2]
        d.line(pts, fill=col((220, 200, 150, 255), 0.9), width=max(1, int(cam.s(6))), joint="curve")


def plant(d, cam, x, size, t, color=(255, 120, 150), wilt=0.0):
    if size <= 0:
        return
    bx, by = cam.p(x, -10)
    h = cam.s(60 + 520 * size)
    sway = math.sin(t * 1.5 + x) * cam.s(8)
    top = (bx + sway + wilt * h * 0.5, by - h * (1 - wilt * 0.6))
    d.line([(bx, by), top], fill=col(mix((70, 150, 60, 255), (130, 110, 60, 255), wilt), 1), width=max(2, int(cam.s(8 + 10 * size))))
    for k in range(int(2 + 4 * size)):
        u = (k + 1) / (2 + 4 * size + 1)
        lx, ly = lerp(bx, top[0], u), lerp(by, top[1], u)
        s = 1 if k % 2 else -1
        d.ellipse([lx + s * cam.s(10) - cam.s(30 * (0.4 + size)), ly - cam.s(12), lx + s * cam.s(10) + cam.s(30 * (0.4 + size)), ly + cam.s(12)],
                  fill=col(mix((80, 170, 70, 255), (140, 120, 60, 255), wilt), 1))
    if size > 0.5 and wilt < 0.3:
        fr = cam.s(40 + 70 * size)
        for k in range(6):
            a = k * math.pi / 3 + t * 0.2
            d.ellipse([top[0] + math.cos(a) * fr * 0.6 - fr * 0.45, top[1] + math.sin(a) * fr * 0.6 - fr * 0.45,
                       top[0] + math.cos(a) * fr * 0.6 + fr * 0.45, top[1] + math.sin(a) * fr * 0.6 + fr * 0.45], fill=color + (255,))
        d.ellipse([top[0] - fr * 0.35, top[1] - fr * 0.35, top[0] + fr * 0.35, top[1] + fr * 0.35], fill=(255, 220, 80, 255))


def gardener(d, cam, x, color, t, mode, name, face=1, **kw):
    fx, fy = cam.p(x, -14)
    tool = kw.pop("tool", None)

    def prop(dd, fh, bh, h, a):
        if not fh:
            return
        if tool == "shovel":
            dd.line([fh, (fh[0] + face * h * 0.1, fh[1] + h * 0.35)], fill=(120, 90, 60, 255), width=max(2, int(h * 0.025)))
            dd.polygon([(fh[0] + face * h * 0.06, fh[1] + h * 0.33), (fh[0] + face * h * 0.16, fh[1] + h * 0.33), (fh[0] + face * h * 0.12, fh[1] + h * 0.45)], fill=(160, 160, 170, 255))
        elif tool == "can":
            dd.rounded_rectangle([fh[0], fh[1] - h * 0.04, fh[0] + face * h * 0.14, fh[1] + h * 0.06], int(h * 0.02), fill=(80, 140, 200, 255))
        elif tool == "umbrella":
            dd.line([fh, (fh[0], fh[1] - h * 0.45)], fill=(60, 60, 60, 255), width=max(2, int(h * 0.02)))
            dd.chord([fh[0] - h * 0.4, fh[1] - h * 0.65, fh[0] + h * 0.4, fh[1] - h * 0.25], 180, 360, fill=(200, 80, 90, 255))
    figure(d, fx, fy, cam.s(CH), color, mode=mode, phase=t * 6, face=face, acc=("hair",), prop=prop, name=name, **kw)


def meadow(d, cam, t, g):
    """Extra flowers filling the patient side as it blooms."""
    if g <= 0:
        return
    r = random.Random(42)
    for i in range(22):
        x = r.uniform(120, 1500)
        k = clamp(g * 1.4 - r.random() * 0.4)
        plant(d, cam, x, 0.25 + 0.45 * k * r.random(), t, color=r.choice([(255, 120, 150), (255, 200, 60), (190, 120, 255), (255, 150, 80), (120, 180, 255)])) if k > 0 else None


def water_drops(d, cam, x, t):
    sx, sy = cam.p(x + 140, -150)
    for k in range(6):
        u = ((t * 2 + k / 6) % 1)
        d.line([(sx + k * cam.s(8), sy + u * cam.s(120)), (sx + k * cam.s(8), sy + u * cam.s(120) + cam.s(14))], fill=(120, 180, 240, 255), width=2)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # macro: a fingertip presses one seed into dark soil; the soil falls back over it
    cam = Cam(SEEDS_R[0], 40, 3.0)
    garden(d, cam, t)
    push = sstep(ramp(t, 0.4, 1.0))
    sx, sy = cam.p(SEEDS_R[0], lerp(-60, 20, push))
    d.ellipse([sx - cam.s(12), sy - cam.s(8), sx + cam.s(12), sy + cam.s(8)], fill=(200, 160, 90, 255))
    fx, fy = cam.p(SEEDS_R[0] + 10, lerp(-200, 0, push) - 20)
    d.rounded_rectangle([fx - cam.s(26), fy - cam.s(160), fx + cam.s(26), fy], int(cam.s(24)), fill=col(PAT, 1))
    if t > 1.6:
        particles(d, sx, sy, cam.s(60), ramp(t, 1.6, 0.6), (90, 60, 40), n=12, seed=1, rise=-0.2, size=6)


def s1_dig(d, t, dur):
    p = t / dur
    # left: dig, look, replant, dig again — roots torn each time. right: water and wait.
    cam = Cam(-100, -200, 0.62)
    garden(d, cam, t)
    cycle = (p * 3) % 1
    for i, x in enumerate(SEEDS_L):
        roots(d, cam, x, 0.25 * cycle, torn=cycle > 0.6)
        plant(d, cam, x, 0.08 * cycle, t, wilt=sstep(ramp(cycle, 0.6, 0.3)))
    if cycle > 0.6:
        particles(d, *cam.p(SEEDS_L[2], 0), cam.s(300), (cycle - 0.6) / 0.4, (90, 60, 40), n=20, seed=int(p * 3), rise=0.4, size=7)
    gardener(d, cam, SEEDS_L[2] - 160, IMP, t, "hammer" if cycle > 0.5 else "stand", "THE IMPATIENT GARDENER", tool="shovel", look=-0.4)
    for x in SEEDS_R:
        roots(d, cam, x, 0.3 * p)
        plant(d, cam, x, 0.1 * p, t)
    gardener(d, cam, SEEDS_R[-1] + 200, PAT, t, "stand", "THE PATIENT GARDENER", face=-1, tool="can")
    water_drops(d, cam, SEEDS_R[-1] - 60, t)


def s2_progress(d, t, dur):
    p = t / dur
    # a storm: the patient gardener shields the seedlings; underground their roots spread deep
    cam = cam_lerp((-100, -200, 0.62), (400, -100, 0.8), sstep(p))
    garden(d, cam, t, rainy=1.0)
    for x in SEEDS_L:
        roots(d, cam, x, 0.15, torn=True)
    for x in SEEDS_R:
        roots(d, cam, x, lerp(0.3, 0.8, p))
        plant(d, cam, x, lerp(0.1, 0.25, p), t)
    gardener(d, cam, SEEDS_R[2], PAT, t, "stand", "THE PATIENT GARDENER", face=-1, tool="umbrella", hands=None)
    gardener(d, cam, SEEDS_L[2] - 160, IMP, t, "hammer", "THE IMPATIENT GARDENER", tool="shovel")
    rain(d, t, 0.9, n=180)
    top_caption(d, ["STOP DIGGING UP", "YOUR PROGRESS…"], t, dur, accent={"DIGGING"})


def s3_growing(d, t, dur):
    p = t / dur
    # time-lapse: the patient side explodes into an enormous garden; the other side stays bare;
    # the impatient gardener looks over the fence and puts the shovel down
    g = sstep(ramp(p, 0.05, 0.75))
    cam = cam_lerp((400, -100, 0.8), (0, -500, 0.5), sstep(ramp(p, 0.1, 0.8)))
    garden(d, cam, t, rainy=1 - sstep(ramp(p, 0.0, 0.3)), season=g)
    for x in SEEDS_L:
        roots(d, cam, x, 0.15, torn=True)
    cols = [(255, 120, 150), (255, 200, 60), (190, 120, 255), (255, 150, 80), (120, 180, 255)]
    meadow(d, cam, t, g)
    for i, x in enumerate(SEEDS_R):
        roots(d, cam, x, lerp(0.8, 1.2, g))
        plant(d, cam, x, lerp(0.25, 1.0, g), t, color=cols[i])
    gardener(d, cam, SEEDS_R[-1] + 200, PAT, t, "stand", "", face=-1, mouth=0.6)
    gardener(d, cam, FENCE_X - 140, IMP, t, "stand" if p > 0.6 else "hammer", "", face=1, tool=None if p > 0.75 else "shovel", look=0.4)
    dust(d, t, 0.5 * g, n=50, color=(255, 240, 180))
    top_caption(d, ["JUST TO CHECK WHETHER", "IT'S GROWING."], t, dur, accent={"GROWING."})


def s4_end(d, t, dur):
    cam = Cam(0, -500, 0.5)
    garden(d, cam, t, season=1.0)
    cols = [(255, 120, 150), (255, 200, 60), (190, 120, 255), (255, 150, 80), (120, 180, 255)]
    meadow(d, cam, t, 1.0)
    for i, x in enumerate(SEEDS_R):
        roots(d, cam, x, 1.2)
        plant(d, cam, x, 1.0, t, color=cols[i])
    stage_end(d, t, dur, ["LET IT GROW."], [(255, 230, 160, 255)], size=130, dim=0.35, glow_col=(255, 220, 150), y=H * 0.25)


SCENES = [s0_hook, s1_dig, s2_progress, s3_growing, s4_end, s_follow]
