"""A stone whooshing past in slow motion, distant jeering, stones landing and stacking with heavy knocks, the
wall closing in, then stones scraped loose and set as steps, footsteps climbing, and wind and warmth on top."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[5][1], 0.12), 0.0)
    m.add(X.whoosh(1.6, 0.5), w[0][0] + 0.8)
    a, b = w[1][0], w[2][1]
    m.bed(X.murmur(b - a, 0.08), a)
    k = a + 0.4
    while k < b - (w[2][1] - w[2][0]) * 0.3:
        m.add(X.thud(0.4, rng.uniform(1.2, 1.6), 0.3), k, pan=rng.uniform(-0.4, 0.4))
        k += 0.28
    st, en = w[3]
    for j in range(4):
        m.add(X.lp(X.noise(0.4), 3) * X.fade_env(int(0.4 * SR), 0.05, 0.2) * 0.2, st + j * (en - st) / 4)
        m.add(X.thud(0.4, 1.3, 0.3), st + j * (en - st) / 4 + 0.4)
    st, en = w[4]
    m.steps(st + (en - st) * 0.15, st + (en - st) * 0.85, 2.0, 0.6)
    m.add(X.swell(en - st, 0.25, bright=True), st)
    m.add(X.chime(0.35, 392.0, 4.5), w[5][0] + 0.2)
