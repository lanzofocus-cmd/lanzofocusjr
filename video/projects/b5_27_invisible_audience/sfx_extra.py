"""A studio click and hum, ON AIR buzz, light banks clunking on, canned applause swelling and cutting off,
silence, then rain on a skylight, the soft whirr of a potter's wheel, wet clay, and a warm chime."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.34


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    st, en = w[0]
    m.add(X.tick(0.4, 0.8), st + 0.4)
    m.add(X.hum(w[1][1] - st, 0.05, 120), st + 0.4)
    for j in range(3):
        m.add(X.clank(0.4, 0.4, 0.5), st + 0.8 + j * 0.33)
    a = st + 1.8
    b = w[1][0] + (w[1][1] - w[1][0]) * 0.45
    m.bed(X.applause(b - a, 0.45), a)
    st, en = w[2]
    m.bed(X.rain(w[4][1] - st, 0.07), st)
    m.add(X.hum(w[4][1] - st, 0.04, 70), st)
    m.add(X.lp(X.noise(w[3][1] - st), 8) * X.fade_env(int((w[3][1] - st) * SR), 0.5, 0.5) * 0.06, st)
    m.add(X.chime(0.35, 392.0, 4.5), w[3][0] + (w[3][1] - w[3][0]) * 0.3)
