"""Harbor water and gulls, a lighthouse hum, years of wind, distant thunder for Fear, boots on the gangplank,
the ship's horn, an engine coming alive, a storm crossing, and calm open sea."""
import numpy as np
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def horn(length=2.2, gain=0.5):
    t = np.arange(int(length * X.SR)) / X.SR
    s = sum(np.sin(2 * np.pi * f * t) * a for f, a in ((110, 1), (220, 0.5), (330, 0.3), (138.6, 0.6)))
    return (s * X.fade_env(len(t), 0.15, 0.5) * gain / 2.4).astype(np.float32)


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    end = w[4][1]
    m.bed(X.lp(X.noise(end), 60) * X.fade_env(int(end * SR), 1, 1) * 0.12, 0.0)   # water
    for j in range(5):
        m.add(X.chime(0.04, 1800 + 200 * j, 0.4, (1, 1.12)), 0.8 + j * 2.3, pan=rng.uniform(-0.8, 0.8))  # gulls
    m.bed(X.wind(w[2][1], 0.12), 0.0)
    st, en = w[2]
    m.add(X.thunder(0.8, 3.0), st + 1.0)
    st, en = w[3]
    p2 = st + (en - st) * 0.4
    m.steps(st, st + (en - st) * 0.22, 2.4, 0.6, 0.9)
    m.add(horn(2.4, 0.6), st + (en - st) * 0.24)
    m.add(X.machine(en - p2 + (w[4][1] - w[4][0]), 0.15, 2.0), p2 - 0.6)
    m.bed(X.rain((en - st) * 0.45, 0.14), p2)
    for k in (0.25, 0.45):
        m.add(X.thunder(0.7, 2.5), p2 + (en - p2) * k)
    m.add(X.swell(en - p2, 0.25, bright=True), p2)
    m.add(X.chime(0.3, 392.0, 4.5), w[4][0] + 0.2)
