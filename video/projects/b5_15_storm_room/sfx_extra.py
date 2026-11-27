"""A ticking quiet room, one drip, thunder indoors, rain on the floor, wind and objects thudding in the
whirlwind, a slow breathing pulse, the storm dying away, and birds outside a sunlit window."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.34


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    st, en = w[0]
    for j in range(5):
        m.add(X.tick(0.12, 1.0), st + 0.2 + j * 0.5)
    m.add(X.tick(0.4, 2.2), st + 1.55)
    m.add(X.thunder(0.9, 3.0), st + 2.1)
    storm_end = w[3][0] + (w[3][1] - w[3][0]) * 0.9
    m.bed(X.rain(storm_end - st - 2.3, 0.14), st + 2.3)
    m.bed(X.wind(storm_end - w[1][0], 0.25), w[1][0])
    for j in range(10):
        m.add(X.thud(0.25, rng.uniform(1.2, 2.0), 0.3), w[1][0] + rng.uniform(0, w[2][1] - w[1][0]), pan=rng.uniform(-0.8, 0.8))
    m.add(X.thunder(0.7), w[1][0] + 1.2)
    m.add(X.thunder(0.8), w[2][0] + 1.0)
    st, en = w[3]
    k = st + (en - st) * 0.3
    while k < en:
        m.add(X.lp(X.noise(1.2), 30) * X.fade_env(int(1.2 * SR), 0.5, 0.6) * 0.25, k)  # breath
        k += 4.5 / 1.4 * 0.7
    m.add(X.swell(en - st, 0.2, bright=True), st + (en - st) * 0.4)
    st, en = w[4]
    for j in range(10):
        m.add(X.chime(0.05, 2200 + 300 * (j % 3), 0.25, (1, 1.2)), st + 0.5 + j * 0.35, pan=0.5)
    m.add(X.chime(0.35, 392.0, 4.5), st + (en - st) * 0.3)
