"""Wind through clouds, a flowing river bed, a boulder crashing into the water, pressure building, seasons of
wind and snow, a trickle, then the river rushing again and waves on the shore."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[0][1], 0.25), 0.0)
    flow = X.lp(X.noise(w[4][1]), 12) * 0.5 + X.hp(X.noise(w[4][1]), 3) * 0.2
    env = X.fade_env(len(flow), 1.0, 1.0)
    st1, en1 = w[1]
    a, b = int((st1 + 0.7) * SR), int(w[3][0] * SR)
    env[a:b] *= 0.3
    m.bed(X.norm(flow) * env * 0.12, 0.0)
    m.add(X.low_hit(1.0, 3.0), st1 + 0.7)
    m.add(X.thud(0.9, 0.6, 1.0), st1 + 0.7)
    m.add(X.hum(en1 - st1, 0.06, 50), st1 + 1.0)
    st, en = w[2]
    m.bed(X.wind(en - st, 0.18), st)
    m.add(X.chime(0.1, 1300, 2.0, (1, 1.5)), st + (en - st) * 0.5)
    st, en = w[3]
    m.add(X.swell(2.0, 0.3), st)
    m.add(X.swell(en - st, 0.2, bright=True), st)
    st, en = w[4]
    for j in range(3):
        m.add(X.lp(X.noise(2.5), 20) * X.fade_env(int(2.5 * SR), 1.0, 1.2) * 0.3, st - 2 + j * 1.6)
    m.add(X.chime(0.35, 392.0, 4.5), st + 0.2)
