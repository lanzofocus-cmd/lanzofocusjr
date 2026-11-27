"""Desert wind, the endless hiss of falling sand, straining and a shaken frame creaking, a calm low tone with
the Keeper, then digging and planting, birds arriving, and a warm close as the last grains fall."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    end = w[4][1]
    m.bed(X.wind(end, 0.12), 0.0)
    m.bed(X.hp(X.noise(end), 3) * X.fade_env(int(end * SR), 0.5, 1.0) * 0.06, 0.0)
    st, en = w[1]
    for j in range(8):
        m.add(X.lp(X.noise(0.3), 4) * X.fade_env(int(0.3 * SR), 0.05, 0.1) * 0.25, st + (en - st) * (0.67 + 0.04 * j))
    m.add(X.chime(0.2, 196.0, 4.0, (1, 1.5, 2.0)), w[2][0] + 0.4)
    st, en = w[3]
    for j in range(10):
        m.add(X.lp(X.noise(0.25), 6) * X.env_ad(int(0.25 * SR), 0.01, 12) * 0.3, st + 0.5 + j * 0.5)
    for j in range(10):
        m.add(X.chime(0.05, 2200 + 250 * (j % 3), 0.25, (1, 1.2)), st + (en - st) * 0.5 + j * 0.3, pan=rng.uniform(-0.7, 0.7))
    m.add(X.swell(en - st, 0.22, bright=True), st)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
