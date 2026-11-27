"""Elevator ding and doors, a flickering hum, button clicks with nothing happening, elevator muzak-free silence,
footsteps, the START button, a heavy motor engaging, and the wind of a fast climb."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.34


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.hum(w[3][1], 0.05, 60), 0.0)
    m.add(X.chime(0.35, 880.0, 1.6, (1, 1.26)), w[0][0] + 0.2)            # ding
    m.add(X.lp(X.noise(1.0), 8) * X.fade_env(int(SR), 0.2, 0.3) * 0.2, w[0][0] + 0.4)   # doors
    st, en = w[1]
    for i in range(3):
        m.add(X.tick(0.5, 1.4), st + (en - st) * (i + 0.55) / 3)
        m.add(X.thud(0.15, 2.0, 0.15), st + (en - st) * (i + 0.6) / 3)
    st, en = w[2]
    k = st
    while k < en:
        m.add(X.tick(0.3, 1.4), k)
        k += 0.4
    st, en = w[3]
    m.add(X.lp(X.noise(1.0), 8) * X.fade_env(int(SR), 0.2, 0.3) * 0.2, st + 0.1)
    m.steps(st + (en - st) * 0.15, st + (en - st) * 0.55, 2.4, 0.5)
    m.add(X.tick(0.7, 0.9), st + (en - st) * 0.82)
    m.add(X.power_up(1.6, 0.5), st + (en - st) * 0.85)
    st, en = w[4]
    m.add(X.low_hit(0.8), st)
    m.bed(X.wind(en - st, 0.25), st)
    m.add(X.swell(en - st, 0.25, bright=True), st)
    m.add(X.chime(0.35, 523.25, 4.0), st + (en - st) * 0.55)
