"""Lapping harbor water and creaking ropes, a distant ship's bell and horn as tall ships leave, a rope cast off,
sails snapping full, crashing waves, wind and rain, then calm water, a whale's spout and gulls at sunrise."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    end = w[4][1]
    m.bed(X.faded(X.lp(X.noise(end), 40), 1.0, 1.0, 0.12), 0.0)
    for j in range(8):
        m.add(X.faded(X.lp(X.noise(0.6), 3), 0.2, 0.3, 0.1), 0.6 + j * 1.6, pan=-0.5)
    m.add(X.chime(0.15, 660, 3.0, (1, 1.19, 1.5)), w[0][0] + 1.0, pan=0.5)
    st, en = w[3]
    m.add(X.clank(0.3, 1.5, 0.3), st + 0.1)
    m.add(X.whoosh(0.5, 0.4), st + (en - st) * 0.05)
    a, b = st + (en - st) * 0.08, st + (en - st) * 0.6
    m.bed(X.faded(X.wind(b - a, 1.0), 0.5, 0.8, 0.3), a)
    m.bed(X.rain(b - a, 0.12), a)
    k = a
    while k < b:
        m.add(X.faded(X.lp(X.noise(1.2), 15), 0.1, 0.8, 0.35), k)
        k += 1.0
    m.add(X.swell(en - b, 0.25, bright=True), b)
    m.add(X.faded(X.hp(X.noise(0.8), 4), 0.05, 0.6, 0.3), st + (en - st) * 0.8)
    for j in range(5):
        m.add(X.chime(0.04, 1800 + 200 * j, 0.4, (1, 1.12)), st + (en - st) * 0.75 + j * 0.5, pan=rng.uniform(-0.8, 0.8))
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
