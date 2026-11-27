"""A vast silent hall, a creaking crank going round and round with no response, a sigh, then one tiny click,
gurgling light in the tubes, gears catching one after another, a rising power-up and a huge luminous burst."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.34


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.add(X.hum(w[5][1], 0.04, 40), 0.0)
    st, en = w[1]
    k = st
    while k < en:
        m.add(X.lp(X.noise(0.5), 3) * X.fade_env(int(0.5 * SR), 0.1, 0.2) * 0.15, k)
        k += 1.57
    st, en = w[2]
    m.add(X.lp(X.noise(1.0), 30) * X.fade_env(int(SR), 0.3, 0.5) * 0.15, st + 0.3)
    m.add(X.tick(0.5, 1.5), st + (en - st) * 0.6)
    st, en = w[3]
    for j in range(8):
        m.add(X.tick(0.3, 1.2 + 0.1 * j), st + j * (en - st) / 8)
    m.add(X.lp(X.noise(en - st), 20) * X.fade_env(int((en - st) * SR), 0.3, 0.3) * 0.15, st)
    st, en = w[4]
    for j in range(20):
        m.add(X.clank(0.2, 0.8 + j * 0.05, 0.3), st + (en - st) * 0.6 * (j / 20))
    m.add(X.power_up(2.0, 0.45), st + (en - st) * 0.3)
    m.add(X.low_hit(1.0, 3.0), st + (en - st) * 0.62)
    m.add(X.chime(0.4, 261.6, 5.0, (1, 1.26, 1.5, 2.0)), st + (en - st) * 0.62)
    m.add(X.hum(w[5][1] - st, 0.08, 110), st + (en - st) * 0.62)
    m.add(X.chime(0.3, 392.0, 4.5), w[5][0] + 0.2)
