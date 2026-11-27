"""Marsh wind and frogs, thunder, a tinkling shimmer from the floating lights, low creeping breaths and
footfalls in the fog, then a lantern flaring, a bright beam sweep, shadows hissing away and dawn birdsong."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[4][1], 0.14), 0.0)
    for j in range(12):
        m.add(X.tick(0.08, 0.5), 0.5 + j * 1.3, pan=rng.uniform(-0.8, 0.8))   # frogs
    m.add(X.thunder(0.8, 3.0), w[0][0] + 0.8)
    st, en = w[1]
    for j in range(10):
        m.add(X.chime(0.05, 1500 + 200 * (j % 4), 0.6, (1, 1.5)), st + j * 0.35, pan=-0.6)
    m.add(X.faded(X.lp(X.noise(en - st + (w[2][1] - w[2][0])), 40), 1.0, 1.0, 0.2), st, pan=0.6)
    m.add(X.heartbeat(0.5), w[2][0] + 0.3)
    st, en = w[3]
    m.add(X.power_up(0.8, 0.3), st + 0.1)
    m.add(X.whoosh(1.6, 0.35), st + (en - st) * 0.25)
    for j in range(10):
        m.add(X.faded(X.hp(X.noise(0.3), 2), 0.02, 0.2, 0.12), st + (en - st) * (0.25 + 0.04 * j), pan=0.5)
    for j in range(8):
        m.add(X.chime(0.04, 2200 + 250 * (j % 3), 0.25, (1, 1.2)), st + (en - st) * 0.65 + j * 0.3, pan=rng.uniform(-0.7, 0.7))
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
