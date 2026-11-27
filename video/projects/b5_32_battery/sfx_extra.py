"""Electronic UI blips, a falling-pitch drain tone and low-battery warning beeps, the pulse of energy leaving
through cables, plugs pulled out one by one, then three rising charge tones layering into full power."""
import numpy as np
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.25
SFX_VOLUME = 0.32


def tone(f0, f1, length, gain=0.2):
    t = np.arange(int(length * X.SR)) / X.SR
    f = np.linspace(f0, f1, len(t))
    return (np.sin(2 * np.pi * np.cumsum(f) / X.SR) * X.fade_env(len(t), 0.05, 0.2) * gain).astype(np.float32)


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.add(X.hum(w[5][1], 0.03, 60), 0.0)
    st, en = w[0]
    m.add(tone(900, 120, en - st - 0.3, 0.18), st + 0.3)
    for j in range(4):
        m.add(X.chime(0.15, 1760, 0.2, (1,)), st + (en - st) * 0.7 + j * 0.25)
    st, en = w[1]
    for j in range(4):
        m.add(X.tick(0.3, 1.8), st + 0.2 + j * 0.3)
    m.add(tone(500, 150, en - st, 0.08), st)
    st, en = w[3]
    for j in range(4):
        m.add(X.clank(0.3, 2.0, 0.2), st + (en - st) * (0.1 + 0.2 * j))
    st, en = w[4]
    for j, f in enumerate((262, 330, 392)):
        m.add(tone(f * 0.5, f, 2.5, 0.12), st + (en - st) * (0.1 + 0.15 * j))
    m.add(X.chime(0.35, 523.25, 4.0), st + (en - st) * 0.8)
    m.add(X.chime(0.35, 392.0, 4.5), w[5][0] + 0.2)
