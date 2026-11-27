"""THE INVISIBLE AUDIENCE — a performer who only moves while the APPLAUSE sign is lit.

World: two rooms. A glossy TV studio in black and hot pink: an ON AIR light, camera rigs, an APPLAUSE sign and
rows of empty seats where ghostly audience outlines flicker in only when imagined. THE PERFORMER dances, eyes on
the sign; when it goes dark, they stop. Then a quiet attic studio at night in warm wood and lamplight, rain on the
skylight: THE CREATOR at a potter's wheel, shaping clay with nobody watching, a shelf slowly filling with work.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (Cam, cam_lerp, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, figure, particles,
                   top_caption, final_card, stage_end, shake, darkness, beam, dust, rain)
from kit import s_follow

TITLE = ("THE INVISIBLE", "AUDIENCE")
OUTPUT = "127_The_Invisible_Audience_16x9.mp4"
LINES = [
    "",
    "Stop performing for people.",
    "",
    "Start creating for yourself.",
    "",
    "",
]
SILENT = {0: 3.0, 2: 4.4, 4: 3.4}
GAPS = {1: 4.0, 3: 4.4}

PINK = (255, 60, 150, 255)
PERF = (230, 220, 240, 255)
CREA = (255, 180, 110, 255)
CLAY = (190, 120, 80, 255)
CH = 300


def studio(d, cam, t, lights=1.0, applause=1.0, onair=1.0):
    d.rectangle([0, 0, W, H], fill=mix((8, 6, 12, 255), (40, 16, 36, 255), lights))
    gy = cam.p(0, 0)[1]
    # glossy floor with reflection streaks
    if gy < H:
        d.rectangle([0, gy, W, H], fill=mix((10, 8, 14, 255), (50, 30, 50, 255), lights))
        for k in range(6):
            x = cam.p(-900 + k * 360, 0)[0]
            tpoly(d, [(x, gy), (x + 40, gy), (x + 120, H), (x + 60, H)], col(PINK, 0.08 * lights))
    # back wall LED strips
    for k in range(8):
        y = cam.p(0, -1100 + k * 110)[1]
        d.line([(0, y), (W, y)], fill=col(PINK, (0.1 + 0.15 * (k % 2)) * lights), width=max(1, int(cam.s(6))))
    # spotlight rig
    for i, x in enumerate((-500, 0, 500)):
        lp = cam.p(x, -1200)
        d.rectangle([lp[0] - cam.s(40), lp[1] - cam.s(30), lp[0] + cam.s(40), lp[1] + cam.s(30)], fill=(40, 40, 50, 255))
        on = clamp(lights * 3 - i)
        if on > 0:
            beam(d, lp[0], lp[1], cam.p(x * 0.4 - 250, 0)[0], cam.p(x * 0.4 + 250, 0)[0], gy, (255, 200, 230), 0.1 * on, cam.s(40))
    # ON AIR and APPLAUSE signs
    ox, oy = cam.p(-650, -950)
    d.rounded_rectangle([ox - cam.s(140), oy - cam.s(50), ox + cam.s(140), oy + cam.s(50)], int(cam.s(14)), fill=col(mix((50, 20, 20, 255), (255, 40, 40, 255), onair), 1))
    d.text((ox, oy), "ON AIR", font=font(int(cam.s(46))), fill=col(WHITE, 0.4 + 0.6 * onair), anchor="mm")
    if onair > 0.5:
        glow(d, ox, oy, cam.s(260), (255, 40, 40), 0.5)
    ax, ay = cam.p(650, -950)
    d.rounded_rectangle([ax - cam.s(200), ay - cam.s(50), ax + cam.s(200), ay + cam.s(50)], int(cam.s(14)), fill=col(mix((40, 30, 20, 255), (255, 190, 60, 255), applause), 1))
    d.text((ax, ay), "APPLAUSE", font=font(int(cam.s(46))), fill=col((40, 20, 10, 255), 0.4 + 0.6 * applause), anchor="mm")
    if applause > 0.5:
        glow(d, ax, ay, cam.s(300), (255, 190, 60), 0.5)
    # camera rig on a tripod
    cx, cy = cam.p(-1000, -450)
    d.rectangle([cx - cam.s(110), cy - cam.s(70), cx + cam.s(90), cy + cam.s(70)], fill=(30, 30, 40, 255))
    d.rectangle([cx + cam.s(90), cy - cam.s(40), cx + cam.s(170), cy + cam.s(40)], fill=(20, 20, 30, 255))
    for s in (-1, 1):
        d.line([(cx, cy + cam.s(70)), (cx + s * cam.s(120), gy)], fill=(40, 40, 50, 255), width=max(2, int(cam.s(10))))


def ghosts(d, cam, t, a):
    """Imagined audience in the empty seats: dashed outlines that clap."""
    if a <= 0.01:
        return
    for row in range(2):
        for i in range(9):
            x = -1100 + i * 270 + row * 135
            fx, fy = cam.p(x, 520 + row * 160)
            hh = cam.s(220)
            k = abs(math.sin(t * 8 + i + row))
            d.ellipse([fx - hh * 0.18, fy - hh, fx + hh * 0.18, fy - hh * 0.64], outline=col((255, 180, 220, 255), a * 0.7), width=2)
            d.chord([fx - hh * 0.35, fy - hh * 0.62, fx + hh * 0.35, fy - hh * 0.1], 180, 360, outline=col((255, 180, 220, 255), a * 0.7), width=2)
            for s in (-1, 1):
                d.ellipse([fx + s * hh * (0.06 + 0.12 * k) - 5, fy - hh * 0.55 - 5, fx + s * hh * (0.06 + 0.12 * k) + 5, fy - hh * 0.55 + 5], fill=col((255, 200, 230, 255), a))


def seats(d, cam):
    for row in range(2):
        for i in range(9):
            x = -1100 + i * 270 + row * 135
            fx, fy = cam.p(x, 520 + row * 160)
            d.rounded_rectangle([fx - cam.s(100), fy - cam.s(60), fx + cam.s(100), fy + cam.s(120)], int(cam.s(20)), fill=(30, 20, 34, 255))


def performer(d, cam, t, dancing=1.0, look=0.0, slump=0.0):
    fx, fy = cam.p(0, 0)
    if slump > 0.5:
        figure(d, fx, fy, cam.s(CH), PERF, mode="slump", face=1, acc=("hair",), head_down=0.6, name="THE PERFORMER")
    else:
        mode = "cheer" if math.sin(t * 4) > 0.3 else ("run" if math.sin(t * 4) > -0.4 else "point")
        figure(d, fx, fy, cam.s(CH), PERF, mode=mode if dancing > 0.5 else "stand", phase=t * 8, face=1 if math.sin(t * 2) > 0 else -1,
               acc=("hair",), look=look, lean=0.15 * math.sin(t * 6), mouth=0.8, name="THE PERFORMER")


def attic(d, cam, t, pots=0, lamp=1.0):
    d.rectangle([0, 0, W, H], fill=(46, 30, 22, 255))
    for k in range(-8, 10):  # wooden planks
        x = cam.p(k * 220, 0)[0]
        d.line([(x, 0), (x, cam.p(0, 0)[1])], fill=(56, 38, 28, 255), width=max(1, int(cam.s(6))))
    # sloped roof with a rainy skylight
    d.polygon([(0, 0), (W, 0), (W, cam.p(0, -1100)[1]), (0, cam.p(0, -700)[1])], fill=(34, 22, 18, 255))
    sx0, sy0 = cam.p(-300, -1000)
    sx1, sy1 = cam.p(200, -760)
    d.polygon([(sx0, sy0), (sx1, sy0 - cam.s(60)), (sx1, sy1 - cam.s(60)), (sx0, sy1)], fill=(30, 40, 60, 255))
    r = random.Random(int(t * 12))
    for i in range(14):
        x = r.uniform(sx0, sx1)
        y = r.uniform(sy0, sy1)
        d.line([(x, y), (x - 4, y + 14)], fill=(140, 160, 200, 255), width=2)
    gy = cam.p(0, 0)[1]
    if gy < H:
        d.rectangle([0, gy, W, H], fill=(60, 40, 30, 255))
    # lamp
    lx, ly = cam.p(250, -700)
    d.line([(lx, 0), (lx, ly)], fill=(30, 30, 30, 255), width=2)
    d.polygon([(lx - cam.s(80), ly + cam.s(60)), (lx + cam.s(80), ly + cam.s(60)), (lx + cam.s(40), ly), (lx - cam.s(40), ly)], fill=(200, 160, 90, 255))
    glow(d, lx, ly + cam.s(200), cam.s(700), (255, 200, 120), 0.6 * lamp)
    # shelf with finished pots
    d.rectangle(cam.box(600, -620, 1300, -600), fill=(90, 60, 40, 255))
    d.rectangle(cam.box(600, -320, 1300, -300), fill=(90, 60, 40, 255))
    rr = random.Random(2)
    for i in range(int(pots)):
        row, c = divmod(i, 6)
        if row > 1:
            break
        x = 650 + c * 110
        y = -620 + row * 300
        hgt = rr.uniform(90, 170)
        cc = rr.choice([(200, 120, 80), (110, 140, 160), (220, 190, 140), (150, 90, 70)])
        d.polygon([cam.p(x, y), cam.p(x - 35, y - hgt * 0.3), cam.p(x - 20, y - hgt), cam.p(x + 20, y - hgt), cam.p(x + 35, y - hgt * 0.3), cam.p(x + 70 - 70, y)],
                  fill=cc + (255,))


def creator(d, cam, t, clay=0.5, lift=0.0):
    wx, wy = cam.p(0, -260)
    # wheel
    d.ellipse([wx - cam.s(200), wy - cam.s(30), wx + cam.s(200), wy + cam.s(30)], fill=(80, 70, 70, 255))
    d.rectangle(cam.box(-60, -260, 60, 0), fill=(70, 60, 60, 255))
    # the pot growing on the wheel (spinning highlight)
    hgt = cam.s(60 + 160 * clay)
    py = wy - cam.s(20) - lift * cam.s(110)
    d.polygon([(wx - cam.s(70), py), (wx - cam.s(90), py - hgt * 0.4), (wx - cam.s(40), py - hgt), (wx + cam.s(40), py - hgt), (wx + cam.s(90), py - hgt * 0.4), (wx + cam.s(70), py)],
              fill=col(CLAY, 1))
    hx = wx + math.sin(t * 9) * cam.s(60)
    d.line([(hx, py - hgt * 0.9), (hx, py - cam.s(10))], fill=col((230, 170, 130, 255), 0.7), width=max(1, int(cam.s(6))))
    fx, fy = cam.p(-260, 0)
    d.rectangle(cam.box(-330, -80, -200, -60), fill=(90, 60, 40, 255))
    d.rectangle(cam.box(-280, -60, -250, 0), fill=(90, 60, 40, 255))
    hands = ((wx - cam.s(80), py - hgt * 0.5), (wx - cam.s(50), py - hgt * 0.7)) if lift <= 0 else ((wx - cam.s(70), py - hgt * 0.2), (wx + cam.s(70), py - hgt * 0.2))
    figure(d, fx, fy - cam.s(70), cam.s(CH), CREA, mode="sit", face=1, acc=("hair",), hands=hands, head_down=0.3 if lift <= 0 else -0.1, mouth=0.4 + 0.4 * lift,
           name="THE CREATOR")


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # darkness; ON AIR flicks on; the lights slam on one by one; the performer hits a pose
    cam = Cam(0, -380, 0.75)
    onair = 1.0 if t > 0.4 else 0.0
    studio(d, cam, t, lights=ramp(t, 0.8, 1.0), applause=ramp(t, 1.8, 0.1), onair=onair)
    seats(d, cam)
    ghosts(d, cam, t, ramp(t, 1.9, 0.4))
    performer(d, cam, t, dancing=1.0 if t > 1.8 else 0.0)
    overlay(d, (0, 0, 0), 0.9 * (1 - ramp(t, 0.8, 1.0)))


def s1_people(d, t, dur):
    p = t / dur
    # dancing for the sign... the sign goes out, the imagined crowd vanishes, the performer stops dead
    off = sstep(ramp(p, 0.45, 0.1))
    cam = cam_lerp((0, -380, 0.75), (0, -260, 1.0), sstep(p))
    studio(d, cam, t, lights=1 - 0.8 * sstep(ramp(p, 0.55, 0.3)), applause=1 - off, onair=1 - sstep(ramp(p, 0.7, 0.1)))
    seats(d, cam)
    ghosts(d, cam, t, 1 - off)
    performer(d, cam, t, dancing=1 - off, look=0.6, slump=sstep(ramp(p, 0.6, 0.2)))
    darkness(d, W / 2, H / 2, 0.5 * off)
    top_caption(d, ["STOP PERFORMING", "FOR PEOPLE."], t, dur, accent={"PERFORMING"})


def s2_attic(d, t, dur):
    p = t / dur
    # a quiet attic at night: the creator at the wheel; time passes; the shelf fills
    cam = cam_lerp((0, -300, 1.1), (300, -380, 0.75), sstep(p))
    attic(d, cam, t, pots=11 * sstep(p))
    creator(d, cam, t, clay=(p * 3) % 1)
    dust(d, t, 0.4, n=40, color=(255, 210, 160))
    d.text((W - 120, H - 100), f"NIGHT {1 + int(p * 40)}", font=font(30), fill=col((255, 220, 180, 255), 0.7), anchor="rm")


def s3_yourself(d, t, dur):
    p = t / dur
    cam = cam_lerp((300, -380, 0.75), (250, -360, 0.62), sstep(p))
    attic(d, cam, t, pots=11)
    creator(d, cam, t, clay=1.0, lift=sstep(ramp(p, 0.2, 0.4)))
    dust(d, t, 0.5, n=40, color=(255, 210, 160))
    top_caption(d, ["START CREATING", "FOR YOURSELF."], t, dur, accent={"CREATING", "YOURSELF."})


def s4_end(d, t, dur):
    cam = Cam(250, -360, 0.62)
    attic(d, cam, t, pots=12)
    creator(d, cam, t, clay=1.0, lift=1.0)
    stage_end(d, t, dur, ["CREATE FOR", "YOURSELF."], [WHITE, CREA], size=110, dim=0.45, glow_col=CREA, y=H * 0.3)


SCENES = [s0_hook, s1_people, s2_attic, s3_yourself, s4_end, s_follow]
