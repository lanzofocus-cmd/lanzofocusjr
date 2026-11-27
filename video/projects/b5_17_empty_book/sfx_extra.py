"""A heavy book thudding open, fluttering pages in a draught, candle crackle, a clock-like silence of waiting,
the scratch of a quill, ink strokes, and a watercolour bloom swell with birdsong."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.add(X.fire(w[3][1], 0.06), 0.0)
    st, en = w[0]
    m.add(X.thud(0.9, 0.8), st + 0.3)
    k = st + 0.4
    while k < en:
        m.add(X.page_flip(0.35), k)
        k += 0.4
    st, en = w[1]
    for j in range(6):
        m.add(X.tick(0.1, 0.8), st + 0.3 + j * 0.5)
    for i in (2, 3):
        st, en = w[i]
        k = st + (en - st) * (0.55 if i == 2 else 0.0)
        stop = en if i == 2 else st + (en - st) * 0.6
        while k < stop:
            m.add(X.hp(X.noise(0.35), 2) * X.fade_env(int(0.35 * SR), 0.03, 0.15) * 0.14, k)
            k += 0.4
    st, en = w[3]
    m.add(X.swell(en - st, 0.25, bright=True), st + (en - st) * 0.4)
    for j in range(8):
        m.add(X.chime(0.05, 2200 + 250 * (j % 3), 0.25, (1, 1.2)), st + (en - st) * 0.6 + j * 0.3, pan=rng.uniform(-0.6, 0.6))
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
