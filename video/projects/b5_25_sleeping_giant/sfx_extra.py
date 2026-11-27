"""Night air over the city, a deep slow breathing from inside the mountain, murmured doubt, footsteps up a tower,
a bronze bell ringing again and again with rumbles in the rock, then a colossal awakening rumble and a rising
golden swell."""
import numpy as np
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.34


def bell(gain=0.5):
    t = np.arange(int(3.0 * X.SR)) / X.SR
    s = sum(np.sin(2 * np.pi * f * t) * a * np.exp(-t * d) for f, a, d in ((220, 1, 1.0), (440 * 1.19, 0.5, 1.5), (660 * 1.27, 0.35, 2.0), (110, 0.6, 0.8)))
    return (s * np.minimum(1, t / 0.005) * gain / 2.0).astype(np.float32)


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[4][1], 0.1), 0.0)
    k = 0.5
    while k < w[3][0]:
        m.add(X.lp(X.noise(2.5), 120) * X.fade_env(int(2.5 * SR), 1.0, 1.2) * 0.6, k)
        k += 3.5
    m.bed(X.murmur(w[1][1] - w[1][0], 0.08), w[1][0])
    m.steps(w[1][0] + 1.0, w[1][1], 2.4, 0.35, 1.1)
    k = w[2][0] + 0.1
    while k < w[3][0] + (w[3][1] - w[3][0]) * 0.4:
        m.add(bell(0.45), k)
        m.add(X.low_hit(0.2, 1.0), k + 0.3)
        k += 1.25
    st, en = w[3]
    m.add(X.low_hit(1.0, 4.0), st + (en - st) * 0.35)
    m.add(X.thunder(0.8, 4.0), st + (en - st) * 0.38)
    m.add(X.swell(en - st, 0.3, bright=True), st + (en - st) * 0.3)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
