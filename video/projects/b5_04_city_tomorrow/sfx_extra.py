"""Airy drones in the dream city, a hollow flicker, footsteps, one solid brick set down, then brick after brick
and the deep locking thuds of towers settling into a real city."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[2][1], 0.1), 0.0)
    m.add(X.hum(w[2][1], 0.05, 220), 0.0)
    st, en = w[2]
    for j in range(6):
        m.add(X.tick(0.1, 3.0), st + 0.2 + j * 0.3)
    st, en = w[3]
    m.steps(st, st + (en - st) * 0.4, 2.2, 0.5)
    m.add(X.thud(0.9, 1.6, 0.35), st + (en - st) * 0.45 + 0.35)
    st, en = w[4]
    for j in range(24):
        m.add(X.thud(0.35, 1.7, 0.25), st + (en - st) * 0.5 * j / 24)
    for j in range(10):
        m.add(X.low_hit(0.25, 1.2), st + (en - st) * (0.4 + 0.05 * j))
    m.add(X.swell(en - st, 0.25), st)
    m.add(X.chime(0.35, 392.0, 4.5), w[5][0] + 0.2)
