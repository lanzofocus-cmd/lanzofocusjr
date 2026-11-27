"""Moorland night silence, a flint strike, a tiny ember's hiss, a howling gust, hands closing around the
flame, twigs snapping, the fire catching and roaring, then distant beacons whooshing alight one by one."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.34


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    st, en = w[0]
    m.add(X.clank(0.4, 2.8, 0.3), st + 0.6)
    m.add(X.fire(en - st, 0.03), st + 0.7)
    st, en = w[1]
    m.bed(X.wind(en - st, 0.4), st)
    m.add(X.thud(0.3, 1.2, 0.3), st + (en - st) * 0.6)
    st, en = w[2]
    for j in range(5):
        m.add(X.hp(X.noise(0.08), 2) * X.env_ad(int(0.08 * SR), 0.001, 40) * 0.4, st + 0.3 + j * 0.45)
    m.add(X.fire(w[4][1] - st, 0.25), st)
    st, en = w[3]
    for j in range(10):
        m.add(X.whoosh(0.7, 0.25), st + (en - st) * (0.25 + 0.06 * j), pan=-0.8 + j * 0.16)
    m.add(X.swell(en - st, 0.25, bright=True), st)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
