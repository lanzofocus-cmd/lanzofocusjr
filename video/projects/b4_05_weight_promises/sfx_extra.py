"""Sound design: the spotlight clunk, each weight slamming down with a chain rattle, dragging and straining,
a heartbeat at the light, an unhooked chain, chains snapping one by one, and a warm chime at the threshold."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.hum(w[5][1], 0.05, 50), 0.0)                       # cold room tone
    st, en = w[0]
    m.add(X.clank(0.5, 0.4, 0.6), st + 0.1)                      # spotlight on
    m.add(X.thud(1.0, 0.8), st + 0.75 + 0.2)
    m.add(X.chain_rattle(0.5), st + 0.95)
    st, en = w[1]
    for h in (0.15, 0.45):
        m.add(X.thud(1.0, 0.8), st + (en - st) * h + 0.2)
        m.add(X.chain_rattle(0.5), st + (en - st) * h + 0.25)
    st, en = w[2]
    for i in range(4):
        tt = st + (en - st) * (0.1 + 0.14 * i) + 0.2
        m.add(X.thud(0.9, 0.75 + 0.05 * i), tt, pan=-0.3)
        m.add(X.chain_rattle(0.4), tt + 0.05)
    m.add(X.lp(X.noise(en - st - 1), 8) * X.fade_env(int((en - st - 1) * SR), 0.5, 0.5) * 0.15, st + 1)  # dragging scrape
    m.add(X.heartbeat(0.6), w[4][0] + 0.3)
    m.add(X.heartbeat(0.55), w[4][0] + 1.25)
    st, en = w[5]
    m.add(X.chain_rattle(0.6, 1.2), st + (en - st) * 0.45)
    m.add(X.clank(0.6, 0.6, 1.0), st + (en - st) * 0.8)
    st, en = w[6]
    for i in range(1, 7):
        m.add(X.snap(0.7), st + (en - st) * (0.08 + 0.13 * i))
    m.steps(st + 0.2, en, 2.4, 0.5)
    m.add(X.swell(w[7][1] - st, 0.25, bright=True), st)
    st, en = w[7]
    m.add(X.chime(0.35, 523.25, 4.5), st + (en - st) * 0.5)
    m.add(X.low_hit(0.7), w[8][0])
