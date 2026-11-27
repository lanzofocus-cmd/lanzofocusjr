"""A wet trowel scrape and a brick set down, days ticking by in soft taps, a roaring storm that tears bricks
loose, rebuilding taps, rain and wind, then air and height and a long warm swell above the clouds."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    st, en = w[0]
    m.add(X.lp(X.noise(0.5), 5) * X.fade_env(int(0.5 * SR), 0.05, 0.2) * 0.25, st + 0.3)
    m.add(X.thud(0.7, 1.4, 0.35), st + 1.6)
    for i in (1, 2):
        a, b = w[i]
        k = a
        while k < b:
            m.add(X.clank(0.15, 1.6, 0.2), k)
            k += 0.5
    st, en = w[1]
    m.bed(X.wind((en - st) * 0.35, 0.3), st + (en - st) * 0.4)
    for j in range(6):
        m.add(X.thud(0.4, 1.6, 0.3), st + (en - st) * (0.55 + 0.03 * j))
    st, en = w[2]
    m.bed(X.rain((en - st) / 3, 0.12), st)
    m.bed(X.wind(en - st, 0.15), st)
    st, en = w[3]
    m.add(X.swell(en - st, 0.3, bright=True), st)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
