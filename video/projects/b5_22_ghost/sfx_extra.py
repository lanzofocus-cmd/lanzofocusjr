"""Footsteps on wet cobbles, a cold breath of wind, a ghostly whispering drone and memory shimmers, running feet
and a heartbeat, a sudden stop and silence, then calm steps into birdsong at dawn."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[4][1], 0.12), 0.0)
    m.steps(w[0][0], w[1][1], 1.8, 0.45, 0.9)
    m.add(X.hum(w[3][0] + 2.0, 0.05, 165), w[0][0] + 1.0)
    m.bed(X.murmur(w[2][1] - w[1][0], 0.06), w[1][0])
    for j in range(8):
        m.add(X.chime(0.05, 700 + 90 * j, 1.0, (1, 1.5)), w[1][0] + 0.4 + j * 0.6, pan=-0.5)
    st, en = w[2]
    m.steps(st, en, 4.2, 0.6, 1.1)
    m.add(X.heartbeat(0.6), st + 0.6)
    m.add(X.heartbeat(0.65), st + 1.5)
    m.add(X.heartbeat(0.7), st + 2.4)
    st, en = w[3]
    m.add(X.low_hit(0.6), st + (en - st) * 0.12)
    m.steps(st + (en - st) * 0.5, en, 1.8, 0.45, 0.95)
    m.add(X.swell(en - st, 0.2, bright=True), st + (en - st) * 0.3)
    for j in range(8):
        m.add(X.chime(0.05, 2200 + 250 * (j % 3), 0.25, (1, 1.2)), st + (en - st) * 0.6 + j * 0.3, pan=0.5)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
