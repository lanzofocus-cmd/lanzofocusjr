"""Door slam, a waiting room tone, the creak of a door held open, it closing and crumbling, a long walk with doors
dying in the dark, a run, three knocks, a push, and the rush of open air."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.hum(w[4][1], 0.04, 48), 0.0)
    m.add(X.thud(1.0, 0.7), w[0][0] + 0.6)
    m.add(X.low_hit(0.6), w[0][0] + 0.6)
    st, en = w[1]
    m.add(X.lp(X.noise(1.0), 3) * X.fade_env(int(1.0 * SR), 0.3, 0.3) * 0.15, st + 0.2)        # creak
    m.add(X.chime(0.15, 523.25, 2.5), st + 0.4)
    st, en = w[2]
    m.add(X.thud(0.8, 0.9), st + 0.5)
    m.add(X.lp(X.noise(1.5), 2) * X.fade_env(int(1.5 * SR), 0.1, 1.0) * 0.25, st + 0.75)       # crumbling
    st, en = w[3]
    m.steps(st, en, 2.2, 0.45, 0.9)
    for j in range(8):
        m.add(X.whoosh(0.6, 0.18), st + j * (en - st) / 8, pan=0.5 if j % 2 == 0 else -0.5)
    st, en = w[4]
    m.steps(st, en, 4.0, 0.6, 1.0)
    st, en = w[5]
    for k in (0.25, 0.55, 0.85):
        m.add(X.thud(0.9, 1.3, 0.35), st + k)
    m.add(X.lp(X.noise(0.9), 3) * X.fade_env(int(0.9 * SR), 0.05, 0.5) * 0.2, st + 1.3)
    m.add(X.swell(1.6, 0.35, bright=True), st + 1.5)
    m.add(X.chime(0.35, 392.0, 4.5), st + 2.0)
    m.bed(X.wind(3.0, 0.12), st + 2.6)
