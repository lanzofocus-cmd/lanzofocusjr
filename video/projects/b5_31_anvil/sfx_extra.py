"""A forge roar, one enormous slowed-down strike, rhythmic hammer blows on hot metal, a hiss of steam in the
quench, and a big golden bell ringing out over a dawn town."""
import numpy as np
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.25
SFX_VOLUME = 0.34


def bell(gain=0.5):
    t = np.arange(int(4.0 * X.SR)) / X.SR
    s = sum(np.sin(2 * np.pi * f * t) * a * np.exp(-t * d) for f, a, d in ((196, 1, 0.7), (392 * 1.19, 0.5, 1.1), (588 * 1.27, 0.35, 1.6), (98, 0.6, 0.5)))
    return (s * np.minimum(1, t / 0.005) * gain / 2.0).astype(np.float32)


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.add(X.fire(w[3][0] + 3, 0.12), 0.0)
    m.add(X.clank(1.0, 0.5, 2.5), w[0][0] + 1.6)
    m.add(X.low_hit(0.8), w[0][0] + 1.6)
    for i, period in ((1, 1.1), (2, 1.4)):
        st, en = w[i]
        k = st + period * 0.75
        while k < en:
            m.add(X.clank(0.7, 0.8, 1.0), k)
            k += period
    st, en = w[3]
    m.add(X.hp(X.noise(1.5), 2) * X.fade_env(int(1.5 * SR), 0.02, 1.0) * 0.4, st + (en - st) * 0.22)
    k = st + (en - st) * 0.4
    while k < en:
        m.add(bell(0.5), k)
        k += 2.1
    m.add(bell(0.45), w[4][0] + 0.3)
