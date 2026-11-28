"""A single drip and splash in silence, a quiet studio with a ticking clock, a brush's soft first stroke,
more strokes, and then a joyful rush of splashes and a bright swell as the colour floods the room."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.25
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    st, en = w[0]
    m.add(X.faded(X.lp(X.noise(0.5), 5), 0.005, 0.3, 0.5), st + 1.8)
    m.add(X.chime(0.15, 880, 1.5, (1, 1.5)), st + 1.8)
    st, en = w[1]
    k = st
    while k < en:
        m.add(X.tick(0.12, 1.0), k)
        k += 0.5
    for i, frac in ((2, [0.55]), (3, [0.1, 0.3, 0.5, 0.7, 0.9])):
        st, en = w[i]
        for f in frac:
            m.add(X.faded(X.hp(X.noise(0.35), 3), 0.05, 0.2, 0.15), st + (en - st) * f)
    st, en = w[4]
    for j in range(24):
        m.add(X.faded(X.lp(X.noise(0.3), 5), 0.005, 0.2, 0.25), st + (en - st) * (0.3 + 0.025 * j), pan=rng.uniform(-0.8, 0.8))
    m.add(X.swell(en - st, 0.3, bright=True), st)
    m.add(X.chime(0.35, 523.25, 4.5), st + (en - st) * 0.4)
    m.add(X.chime(0.35, 392.0, 4.5), w[5][0] + 0.2)
