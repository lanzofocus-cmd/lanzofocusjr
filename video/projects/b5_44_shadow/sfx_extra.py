"""A buzzing streetlamp, lone footsteps (and an echo a beat late), running steps with a rising low drone as the
shadow grows, a heavy hit at the dead end, then a warm lantern swell that dissolves the drone into morning birds."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.25
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.hum(w[3][0] + (w[3][1] - w[3][0]) * 0.6, 0.04, 120), 0.0)
    st, en = w[0]
    tt = st + 0.2
    while tt < en:
        m.add(X.step(0.35), tt, pan=0.2)
        m.add(X.step(0.18, 0.8, soft=True), tt + 0.28, pan=-0.4)
        tt += 0.5
    m.add(X.low_hit(0.3, 2.0), st + en * 0.0 + (en - st) * 0.75)
    st, en = w[1]
    tt = st
    while tt < en:
        m.add(X.step(0.4, 1.1), tt, pan=0.3)
        tt += 0.3
    m.add(X.faded(X.hum(en - st + (w[2][1] - w[2][0]), 1.0, 45), 1.0, 0.4, 0.14), st)
    m.add(X.low_hit(0.7, 3.0), w[2][0] + 0.1)
    st, en = w[3]
    m.add(X.power_up(1.4, 0.25), st + (en - st) * 0.08)
    for j in range(6):
        m.add(X.step(0.25, 0.9, soft=True), st + (en - st) * (0.18 + j * 0.1))
    m.add(X.swell(en - st, 0.28, bright=True), st + (en - st) * 0.3)
    for j in range(8):
        m.add(X.chime(0.04, 2000 + 250 * (j % 3), 0.25, (1, 1.2)), st + (en - st) * 0.6 + j * 0.5, pan=rng.uniform(-0.8, 0.8))
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
