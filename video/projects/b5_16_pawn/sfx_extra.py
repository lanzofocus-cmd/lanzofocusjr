"""A vast hollow void, heavy stone pieces grinding on marble, low mocking rumbles, the small clack of each pawn
step, a rising choir-like swell, and a radiant chime at the crowning."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.34


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.add(X.hum(w[4][1], 0.05, 41), 0.0)
    m.bed(X.wind(w[4][1], 0.08), 0.0)
    st, en = w[0]
    for j in range(3):
        m.add(X.lp(X.noise(1.0), 6) * X.fade_env(int(SR), 0.1, 0.5) * 0.25, st + 0.3 + j * 0.9, pan=-0.6 + j * 0.6)
    st, en = w[1]
    for j in range(3):
        m.add(X.low_hit(0.4, 1.5), st + 0.3 + j * 0.8)
    st, en = w[2]
    for j in range(7):
        m.add(X.clank(0.35, 2.2, 0.25), st + (en - st) * (j + 1) / 7.5)
    st, en = w[3]
    m.add(X.clank(0.4, 2.2, 0.25), st + (en - st) * 0.18)
    m.add(X.swell(en - st, 0.3, bright=True), st)
    m.add(X.low_hit(0.9, 3.0), st + (en - st) * 0.5)
    m.add(X.chime(0.4, 261.6, 5.0, (1, 1.26, 1.5, 2.0)), st + (en - st) * 0.5)
    m.add(X.chime(0.3, 392.0, 4.5), w[4][0] + 0.2)
