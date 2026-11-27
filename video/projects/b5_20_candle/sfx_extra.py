"""Silence and a tiny ignition, a soft candle crackle, a huge bright swell as the sun rises, the flame
straining and sputtering with hiss and smoke, then night crickets, a page turning, a purring cat and warmth."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.25
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    st, en = w[0]
    m.add(X.hp(X.noise(0.25), 2) * X.env_ad(int(0.25 * SR), 0.003, 12) * 0.4, st + 0.6)
    m.add(X.fire(w[4][1] - st, 0.07), st + 0.7)
    st, en = w[1]
    m.add(X.swell(en - st, 0.35, bright=True), st)
    m.add(X.low_hit(0.6, 3.0), st + (en - st) * 0.5)
    m.add(X.hp(X.noise(1.5), 2) * X.fade_env(int(1.5 * SR), 0.2, 0.6) * 0.15, st + (en - st) * 0.75)
    st, en = w[3]
    for j in range(16):
        m.add(X.tick(0.06, 3.5), st + (en - st) * 0.4 + j * 0.25, pan=0.6)
    m.add(X.page_flip(0.3), st + (en - st) * 0.6)
    m.add(X.lp(X.noise(2.0), 30) * X.fade_env(int(2.0 * SR), 0.5, 0.5) * 0.12, st + (en - st) * 0.7, pan=0.5)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
