"""Cavernous room tone, a key sliding in and grinding, the lock's harsh reject buzz, keys clattering onto a
growing pile faster and faster, chalk scratches, forging taps, then tumblers clicking, bolts sliding and a vast
door groaning open onto light."""
import numpy as np
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.34


def buzz(length=0.4, gain=0.3):
    t = np.arange(int(length * X.SR)) / X.SR
    s = np.sign(np.sin(2 * np.pi * 110 * t)) * 0.5 + np.sin(2 * np.pi * 220 * t) * 0.3
    return (X.lp(s.astype(np.float32), 6) * X.fade_env(len(t), 0.01, 0.1) * gain).astype(np.float32)


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.add(X.hum(w[4][1], 0.04, 50), 0.0)
    st, en = w[0]
    m.add(X.lp(X.noise(0.8), 3) * X.fade_env(int(0.8 * SR), 0.05, 0.3) * 0.2, st + 0.4)
    m.add(buzz(0.5, 0.35), st + 1.8)
    m.add(X.clank(0.5, 1.1, 0.8), st + 1.8)
    st, en = w[1]
    k = st
    while k < en:
        u = (k - st) / (en - st)
        m.add(buzz(0.15, 0.15), k)
        m.add(X.clank(0.2, rng.uniform(1.8, 2.6), 0.25), k + 0.08, pan=rng.uniform(-0.5, 0.5))
        k += 1 / (2 + 12 * u)
    st, en = w[2]
    for j in range(4):
        m.add(X.hp(X.noise(0.5), 3) * X.fade_env(int(0.5 * SR), 0.05, 0.2) * 0.1, st + 0.6 + j * 0.6)
    st, en = w[3]
    for j in range(5):
        m.add(X.clank(0.35, 1.3, 0.4), st + (en - st) * 0.05 * j)
    for j in range(6):
        m.add(X.tick(0.4, 0.8), st + (en - st) * (0.4 + 0.03 * j))
    m.add(X.clank(0.6, 0.5, 1.2), st + (en - st) * 0.6)
    m.add(X.lp(X.noise(2.0), 4) * X.fade_env(int(2.0 * SR), 0.3, 0.8) * 0.3, st + (en - st) * 0.7)
    m.add(X.swell(en - st, 0.22, bright=True), st)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
