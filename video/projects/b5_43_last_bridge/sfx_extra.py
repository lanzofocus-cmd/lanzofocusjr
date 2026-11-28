"""Jungle wind and birds in the gorge, a pebble clicking down into silence, hammer taps on planks (slow, then a
rapid time-lapse rhythm), creaking rope, then a warm evening swell as the traveler crosses."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.25
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[4][1], 0.1), 0.0)
    for j in range(10):
        m.add(X.chime(0.03, 1800 + 300 * (j % 4), 0.3, (1, 1.3)), 0.5 + j * 2.1, pan=rng.uniform(-0.9, 0.9))
    for j in range(4):  # pebble bouncing away, fading
        m.add(X.tick(0.4 * (0.6 ** j), 1.6), w[0][0] + 0.6 + j * 0.35 + j * j * 0.05)
    st, en = w[2]
    for j in range(3):
        m.add(X.clank(0.25, 2.2, 0.3), st + (en - st) * (0.25 + j * 0.15))
    st, en = w[3]
    k = 0.0
    tt = st
    while tt < st + (en - st) * 0.5:
        m.add(X.clank(0.18, 2.0 + rng.uniform(-0.2, 0.2), 0.25), tt, pan=rng.uniform(-0.3, 0.3))
        tt += max(0.12, 0.45 - k)
        k += 0.03
    for j in range(5):  # rope creaks during the crossing
        m.add(X.faded(X.lp(X.noise(0.5), 12), 0.2, 0.25, 0.12), st + (en - st) * (0.55 + j * 0.08), pan=0.2)
    m.add(X.swell(en - st, 0.26, bright=True), st + (en - st) * 0.3)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
