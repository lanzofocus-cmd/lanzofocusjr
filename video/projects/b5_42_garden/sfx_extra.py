"""Birdsong and a breeze, a seed pressed into soil, shovel scrapes and clods thudding again and again, a
watering can's trickle, a rain storm on an umbrella, then a bright time-lapse swell of growth and bees."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.25
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[4][1], 0.08), 0.0)
    for j in range(12):
        m.add(X.chime(0.04, 2200 + 250 * (j % 3), 0.25, (1, 1.2)), 0.3 + j * 0.8, pan=rng.uniform(-0.8, 0.8))
    m.add(X.faded(X.lp(X.noise(0.4), 6), 0.05, 0.2, 0.2), w[0][0] + 1.4)
    st, en = w[1]
    for j in range(3):
        tt = st + (en - st) * (j + 0.6) / 3
        m.add(X.faded(X.lp(X.noise(0.4), 3), 0.02, 0.2, 0.3), tt, pan=-0.5)
        m.add(X.thud(0.3, 1.5, 0.25), tt + 0.3, pan=-0.5)
    m.add(X.faded(X.hp(X.noise(en - st), 4), 0.3, 0.3, 0.05), st, pan=0.5)
    st, en = w[2]
    m.bed(X.rain(en - st + 1.0, 0.14), st)
    st, en = w[3]
    m.add(X.swell(en - st, 0.28, bright=True), st)
    m.add(X.faded(X.hum(en - st, 1.0, 240), 1.0, 1.0, 0.03), st + (en - st) * 0.4, pan=0.4)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
