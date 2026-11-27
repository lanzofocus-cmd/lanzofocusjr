"""Sound design: dusk wind and a creaking crane, Excuses' plaques, workers' tools dropping, Laziness snoring,
calendar pages flipping, the first hammer blows, a growing chorus of work, lanterns and a warm swell."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.4
SFX_VOLUME = 0.3


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[5][1], 0.12), 0.0)
    for k in range(3):
        m.add(X.clank(0.15, 0.3, 1.2), w[0][0] + 0.8 + k * 1.3, pan=0.4)   # crane creak
    st, en = w[2]
    for i in range(3):
        m.add(X.thud(0.35, 1.6, 0.3), st + (en - st) * (0.05 + 0.2 * i))
    m.add(X.clank(0.3, 1.2, 0.4), st + (en - st) * 0.45)
    m.add(X.clank(0.3, 1.1, 0.4), st + (en - st) * 0.6)
    st, en = w[3]
    k = st + 0.3
    while k < en:  # snoring
        m.add(X.lp(X.noise(0.9), 40) * X.fade_env(int(0.9 * SR), 0.4, 0.4) * 0.25, k)
        k += 1.6
    st, en = w[4]
    for i in range(1, 4):
        m.add(X.page_flip(0.5), st + (en - st) * i / 4)
    st, en = w[5]
    m.steps(st, st + (en - st) * 0.35, 2.2, 0.6)
    k = st + (en - st) * 0.4
    while k < en:
        m.add(X.clank(0.35, 0.9, 0.35), k)
        k += 1.05
    st, en = w[6]
    for j in range(40):  # more and more hammers join in
        tt = st + (en - st) * (j / 40) ** 0.8
        m.add(X.clank(0.2, rng.uniform(0.7, 1.3), 0.3), tt, pan=rng.uniform(-0.7, 0.7))
    m.bed(X.murmur(w[7][1] - st, 0.06), st)
    m.add(X.swell(w[7][1] - st, 0.25), st)
    m.add(X.chime(0.3, 392.0, 4.5), w[7][0] + 0.5)
    m.add(X.low_hit(0.7), w[9][0])
