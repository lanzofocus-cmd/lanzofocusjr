"""THE PAWN THAT BECAME A KING — a giant chessboard, and the smallest piece that never stopped moving.

World: an enormous marble chessboard in a black void with hard red rim light, seen in deep perspective from
ground level. The characters are the pieces themselves: towering obsidian knights, rooks and bishops with
glowing eyes who look down on THE PAWN, a small ivory piece. The pawn advances square by square to the far edge,
and in a column of light becomes a KING.
"""
import math
import random
from render import W, H, WHITE, GREY, font, clamp, ramp, lerp, col, polyline
from story import (PCam, sstep, pulse, mix, dimc, glow, tpoly, overlay, draw_sky, fog, particles,
                   top_caption, final_card, stage_end, shake, darkness, dust)
from kit import s_follow

TITLE = ("THE PAWN THAT", "BECAME A KING")
OUTPUT = "116_The_Pawn_That_Became_A_King_16x9.mp4"
LINES = [
    "",
    "",
    "Never underestimate the piece that's still moving.",
    "",
    "",
    "",
]
SILENT = {0: 3.0, 1: 3.4, 3: 4.8, 4: 3.4}
GAPS = {2: 5.0}

IVORY = (240, 232, 214, 255)
OBS = (30, 26, 34, 255)
RIM = (255, 70, 60, 255)
GOLD = (255, 205, 110, 255)
SQ = 300

ENEMIES = [("rook", 1, 6), ("knight", 6, 5), ("bishop", 2, 4), ("queen", 5, 7), ("knight", 3, 6), ("rook", 7, 7), ("bishop", 0, 5), ("king", 4, 9)]
FILE = 4


def board_pos(f, r):
    return (f - 3.5) * SQ, r * SQ + SQ / 2


def board(d, cam, t, glow_rank=None):
    draw_sky(d, (4, 2, 6, 255), (20, 8, 14, 255))
    for r in range(0, 9):
        for f in range(8):
            x0, z0 = (f - 4) * SQ, r * SQ
            q = cam.quad([(x0, z0, 0), (x0 + SQ, z0, 0), (x0 + SQ, z0 + SQ, 0), (x0, z0 + SQ, 0)])
            if not q:
                continue
            light = (f + r) % 2 == 0
            c = (200, 192, 180) if light else (50, 44, 52)
            if glow_rank is not None and r == 8 and f == FILE:
                c = mix(c + (255,), GOLD, glow_rank)[:3]
            d.polygon(q, fill=c + (255,))
    # board edge
    q = cam.quad([(-4 * SQ, 0, 0), (4 * SQ, 0, 0), (4 * SQ, 0, -60), (-4 * SQ, 0, -60)])
    if q:
        d.polygon(q, fill=(20, 16, 20, 255))
    fog(d, W / 2, cam.horizon + 40, 2800, 0.25, (120, 40, 50))


def piece(d, cam, kind, f, r, color, t, scale=1.0, eyes=False, rim=True, tilt=0.0, y=0.0):
    x, z = board_pos(f, r)
    p = cam.p(x, z, y)
    if not p:
        return None
    sx, sy, s = p
    h = {"pawn": 280, "rook": 520, "knight": 600, "bishop": 640, "queen": 760, "king": 820}[kind] * s * scale
    w = h * 0.32
    c = col(color, 1)
    def R(px, py):
        return (sx + px + math.sin(tilt) * (sy - py - sy) * 0, py)
    base = [(sx - w, sy), (sx + w, sy), (sx + w * 0.85, sy - h * 0.08), (sx - w * 0.85, sy - h * 0.08)]
    d.polygon(base, fill=c)
    if kind == "pawn":
        d.polygon([(sx - w * 0.6, sy - h * 0.08), (sx + w * 0.6, sy - h * 0.08), (sx + w * 0.25, sy - h * 0.62), (sx - w * 0.25, sy - h * 0.62)], fill=c)
        d.ellipse([sx - w * 0.5, sy - h * 1.0, sx + w * 0.5, sy - h * 0.58], fill=c)
        top = sy - h
    else:
        body = [(sx - w * 0.6, sy - h * 0.08), (sx + w * 0.6, sy - h * 0.08), (sx + w * 0.35, sy - h * 0.7), (sx - w * 0.35, sy - h * 0.7)]
        d.polygon(body, fill=c)
        if kind == "rook":
            d.rectangle([sx - w * 0.55, sy - h, sx + w * 0.55, sy - h * 0.7], fill=c)
            for k in (-1, 0, 1):
                d.rectangle([sx + k * w * 0.36 - w * 0.12, sy - h * 1.08, sx + k * w * 0.36 + w * 0.12, sy - h * 0.98], fill=c)
        elif kind == "knight":
            d.polygon([(sx - w * 0.4, sy - h * 0.7), (sx + w * 0.4, sy - h * 0.7), (sx + w * 0.5, sy - h * 0.9), (sx - w * 0.1, sy - h * 1.05),
                       (sx - w * 0.75, sy - h * 0.88), (sx - w * 0.65, sy - h * 0.8)], fill=c)
        elif kind == "bishop":
            d.ellipse([sx - w * 0.45, sy - h * 1.0, sx + w * 0.45, sy - h * 0.66], fill=c)
            d.ellipse([sx - w * 0.1, sy - h * 1.08, sx + w * 0.1, sy - h * 0.98], fill=c)
        elif kind == "queen":
            pts = [(sx - w * 0.55, sy - h * 0.7)]
            for k in range(5):
                pts += [(sx - w * 0.55 + k * w * 0.275, sy - h * 1.0), (sx - w * 0.41 + k * w * 0.275, sy - h * 0.85)]
            pts += [(sx + w * 0.55, sy - h * 1.0), (sx + w * 0.55, sy - h * 0.7)]
            d.polygon(pts, fill=c)
        elif kind == "king":
            d.rectangle([sx - w * 0.5, sy - h * 0.92, sx + w * 0.5, sy - h * 0.7], fill=c)
            d.rectangle([sx - w * 0.06, sy - h * 1.12, sx + w * 0.06, sy - h * 0.92], fill=c)
            d.rectangle([sx - w * 0.2, sy - h * 1.06, sx + w * 0.2, sy - h * 1.0], fill=c)
        top = sy - h
    if rim:
        d.line([(sx + w * 0.35, sy - h * 0.7), (sx + w * 0.6, sy - h * 0.08)], fill=col(RIM, 0.8), width=max(1, int(s * 8)))
    if eyes:
        ey = sy - h * 0.82
        for o in (-1, 1):
            ex = sx + o * w * 0.18
            d.polygon([(ex - w * 0.1, ey - w * 0.02 * o), (ex + w * 0.1, ey + w * 0.02 * o), (ex, ey + w * 0.06)], fill=col((255, 90, 70, 255), 1))
            glow(d, ex, ey, w * 0.3, RIM, 0.5)
    return sx, top, s, h


def pawn_face(d, info, look=0.0, happy=0.0):
    if not info:
        return
    sx, top, s, h = info
    w = h * 0.32
    ey = top + h * 0.2
    for o in (-1, 1):
        d.ellipse([sx + o * w * 0.16 - w * 0.05, ey - w * 0.07, sx + o * w * 0.16 + w * 0.05, ey + w * 0.07], fill=(30, 26, 30, 255))


def enemies(d, cam, t, eyes=True, bow=0.0, shift=0.0, behind=None):
    """behind: only draw pieces farther (True) or nearer (False) than rank `behind[1]`."""
    for kind, f, r in sorted(ENEMIES, key=lambda e: -e[2]):
        if behind is not None and ((r > behind[1]) != behind[0]):
            continue
        piece(d, cam, kind, f, r, OBS, t, eyes=eyes)


# ---------------------------------------------------------------- scenes
def s0_hook(d, t, dur):
    p = t / dur
    # ground-level, low and close: obsidian giants loom over the board; the camera slides past to find a tiny pawn
    cam = PCam(lerp(-700, 0, sstep(p)), lerp(-200, -500, p), lerp(60, 120, p), horizon=H * 0.62)
    board(d, cam, t)
    enemies(d, cam, t)
    info = piece(d, cam, "pawn", FILE, 1, IVORY, t, rim=False)
    pawn_face(d, info)
    darkness(d, W / 2, H / 2, 0.5)


def s1_laugh(d, t, dur):
    p = t / dur
    # the pieces look down; their verdict hangs in the air
    cam = PCam(0, -500 + 100 * p, 140, horizon=H * 0.6)
    board(d, cam, t)
    enemies(d, cam, t)
    info = piece(d, cam, "pawn", FILE, 1, IVORY, t, rim=False)
    pawn_face(d, info)
    for i, (txt, f, r) in enumerate((("JUST A PAWN.", 2, 4), ("TOO SMALL.", 6, 5), ("ONE STEP AT A TIME? HA.", 5, 7))):
        x, z = board_pos(f, r)
        q = cam.p(x, z, 900)
        if q:
            a = ramp(t, 0.3 + i * 0.8, 0.3)
            d.text((q[0], q[1]), txt, font=font(int(clamp(q[2] * 120, 20, 50))), fill=col((255, 120, 100, 255), a), anchor="mm")
    darkness(d, W / 2, H / 2, 0.45)


def s2_moving(d, t, dur):
    p = t / dur
    # square by square: each hop a small arc; the camera tracks low behind, passing under the giants
    hop = 1 + 6 * sstep(p)
    r = math.floor(hop)
    u = hop - r
    rr = r + sstep(u)
    y = math.sin(math.pi * u) * 120
    x, z = board_pos(FILE, rr)
    cam = PCam(80 * math.sin(t * 0.7), z - 900, 220, horizon=H * 0.55)
    board(d, cam, t)
    enemies(d, cam, t, behind=(True, rr))
    info = piece(d, cam, "pawn", FILE, rr, IVORY, t, rim=False, y=y)
    pawn_face(d, info)
    enemies(d, cam, t, behind=(False, rr))
    top_caption(d, ["NEVER UNDERESTIMATE THE PIECE", "THAT'S STILL MOVING."], t, dur, accent={"STILL", "MOVING."})


def s3_crown(d, t, dur):
    p = t / dur
    # the last square: a column of light, and the pawn rises into a king; the dark pieces lean away
    rr = lerp(7, 8, sstep(ramp(p, 0.0, 0.2)))
    x, z = board_pos(FILE, rr)
    cam = PCam(lerp(0, 600, sstep(p)), lerp(z - 900, z - 1400, sstep(p)), lerp(220, 120, p), horizon=H * 0.58)
    k = sstep(ramp(p, 0.25, 0.45))
    board(d, cam, t, glow_rank=k)
    enemies(d, cam, t, eyes=p < 0.6)
    q = cam.p(x, z, 0)
    if q and k > 0:
        tpoly(d, [(q[0] - 160 * q[2] * 1.5, 0), (q[0] + 160 * q[2] * 1.5, 0), (q[0] + 300 * q[2], q[1]), (q[0] - 300 * q[2], q[1])], col(GOLD, 0.25 * k))
        glow(d, q[0], q[1] - 400 * q[2], 900 * q[2], GOLD, 0.8 * k)
    if k < 0.5:
        info = piece(d, cam, "pawn", FILE, rr, IVORY, t, rim=False, scale=lerp(1.0, 1.4, k * 2))
        pawn_face(d, info)
    else:
        piece(d, cam, "king", FILE, rr, mix(IVORY, GOLD, 0.4), t, rim=False, scale=lerp(0.6, 1.2, (k - 0.5) * 2))
    if 0.4 < p < 0.9 and q:
        particles(d, q[0], q[1] - 300 * q[2], 900 * q[2], (p - 0.4) / 0.5, GOLD, n=60, seed=3, rise=0.8, size=5)


def s4_end(d, t, dur):
    x, z = board_pos(FILE, 8)
    cam = PCam(600, z - 1400, 120, horizon=H * 0.58)
    board(d, cam, t, glow_rank=1.0)
    enemies(d, cam, t, eyes=False)
    q = cam.p(x, z, 0)
    glow(d, q[0], q[1] - 400 * q[2], 900 * q[2], GOLD, 0.7)
    piece(d, cam, "king", FILE, 8, mix(IVORY, GOLD, 0.4), t, rim=False, scale=1.2)
    stage_end(d, t, dur, ["KEEP MOVING."], [GOLD], size=130, dim=0.45, glow_col=GOLD, y=H * 0.25)


SCENES = [s0_hook, s1_laugh, s2_moving, s3_crown, s4_end, s_follow]
