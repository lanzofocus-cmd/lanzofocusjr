"""A crackling fire in a cave, contented breathing, bowls scraping in, then the fire dying, a cold draught,
a hungry growl, snow crunching under paws, running, and a long howl at dawn."""
import numpy as np
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def howl(length=2.6, gain=0.35):
    t = np.arange(int(length * X.SR)) / X.SR
    f = 330 + 160 * np.sin(np.pi * t / length) + 8 * np.sin(2 * np.pi * 5 * t)
    s = np.sin(2 * np.pi * np.cumsum(f) / X.SR) + 0.3 * np.sin(4 * np.pi * np.cumsum(f) / X.SR)
    return (s * X.fade_env(len(t), 0.3, 0.8) * gain).astype(np.float32)


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.add(X.fire(w[2][0] + 2.0, 0.18), w[0][0] + 1.0)
    st, en = w[1]
    for j in range(4):
        m.add(X.faded(X.lp(X.noise(0.4), 4), 0.05, 0.2, 0.2), st + j * (en - st) / 4)
    st, en = w[2]
    m.bed(X.wind(en - st + (w[3][1] - w[3][0]), 0.2), st + 1.0)
    m.add(X.faded(X.lp(X.noise(1.0), 60), 0.2, 0.5, 0.4), st + (en - st) * 0.6)
    st, en = w[3]
    k = st + (en - st) * 0.05
    while k < st + (en - st) * 0.82:
        u = (k - st) / (en - st)
        m.add(X.step(0.35, 1.2, soft=True), k)
        k += 0.35 if u < 0.3 else 0.18
    m.add(howl(2.8, 0.35), st + (en - st) * 0.82)
    m.add(howl(2.4, 0.3), w[4][0] + 0.3)
