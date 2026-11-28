"""A wall of chattering noise, pings, horns and buzzing speakers, bricks clattering down, then a heavy door
shutting and sudden near-silence: a soft room tone, pencil scratches, and muffled noise outside as the tower rises."""
import numpy as np
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.25
SFX_VOLUME = 0.34


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    shut = w[2][0] + (w[2][1] - w[2][0]) * 0.7
    m.bed(X.faded(X.murmur(shut, 1.0), 0.3, 0.2, 0.25), 0.0)
    k = 0.2
    while k < shut:
        m.add(X.chime(0.1, rng.choice([660, 880, 990, 1320, 1760]), 0.3, (1, 2.0)), k, pan=rng.uniform(-0.9, 0.9))
        m.add(X.faded(X.hum(0.3, 1.0, rng.choice([220, 330, 440])), 0.02, 0.1, 0.05), k + 0.1, pan=rng.uniform(-0.9, 0.9))
        k += rng.uniform(0.15, 0.4)
    st, en = w[1]
    for j in range(2):
        m.add(X.thud(0.4, 1.6, 0.3), st + (en - st) * (0.5 + 0.3 * j))
    m.add(X.thud(0.9, 0.7, 0.6), shut)
    m.add(X.hum(w[4][1] - shut, 0.03, 60), shut)
    m.add(X.faded(X.lp(X.murmur(w[3][1] - shut, 1.0), 60), 0.5, 0.5, 0.08), shut)
    st, en = w[3]
    for j in range(10):
        m.add(X.faded(X.hp(X.noise(0.25), 2), 0.03, 0.1, 0.06), st + 0.4 + j * 0.5)
    m.add(X.swell(en - st, 0.2, bright=True), st)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
