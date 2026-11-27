"""Sound design: a dead hall with a buzzing bulb, dripping, switches clicking off, a TV glow hum, the generator
powering down, then the lever thrown, power-up, machines joining one by one, and the hum of a working complex."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.35
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[7][1], 0.07), 0.0)
    k = 0.4
    while k < w[1][1]:  # buzzing, flickering bulb
        m.add(X.hum(0.25, 0.08, 120), k, pan=-0.3)
        k += rng.uniform(0.3, 0.9)
    for j in range(8):
        m.add(X.tick(0.15, 0.5), w[0][0] + 0.6 + j * 1.1, pan=0.5)  # drips
    st, en = w[5]
    for j in range(6):
        m.add(X.clank(0.3, 1.8, 0.2), st + (en - st) * (0.1 + 0.13 * j))  # switches off
    m.add(X.hum(w[6][1] - st, 0.05, 220), st)
    st, en = w[7]
    m.add(X.clank(0.7, 0.6, 0.8), st + (en - st) * 0.35)
    m.add(X.power_down(1.6, 0.4), st + (en - st) * 0.4)
    m.add(X.page_flip(0.5), st + (en - st) * 0.55)
    st, en = w[8]
    m.steps(st, st + (en - st) * 0.3, 2.2, 0.6)
    m.add(X.clank(0.9, 0.5, 1.0), st + (en - st) * 0.3)
    m.add(X.power_up(1.8, 0.45), st + (en - st) * 0.32)
    m.add(X.machine(w[11][1] - (st + (en - st) * 0.45), 0.25, 3.0), st + (en - st) * 0.45)
    for j in range(5):
        m.add(X.spark(0.3), st + (en - st) * (0.6 + 0.08 * j), pan=0.4)
    m.add(X.hum(w[11][1] - (st + (en - st) * 0.4), 0.06, 55), st + (en - st) * 0.4)
    m.add(X.swell(w[9][1] - st, 0.25), st)
    m.add(X.low_hit(0.8), w[9][0] + (w[9][1] - w[9][0]) * 0.45)
    m.add(X.chime(0.3, 392.0, 4.5), w[11][0] + 0.2)
