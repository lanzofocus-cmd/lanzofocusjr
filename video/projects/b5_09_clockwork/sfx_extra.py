"""A ticking machine room, drone buzzes for each distraction, gears wrenched out with metallic clanks, the machine
groaning to a halt, then work sounds, gears snapping home one by one, and the machine roaring back to life."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.34


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    k, n = 0.0, 0
    end4 = w[4][1]
    while k < end4:  # the machine's tick, slowing as gears go
        u = k / end4
        m.add(X.tick(0.25, 0.8 if n % 2 else 1.1), k)
        k += 0.35 + 0.9 * u ** 2
        n += 1
    m.add(X.machine(end4 * 0.6, 0.12, 2.5), 0.2)
    for i, (a, b, cnt) in enumerate(((1, 1, 2), (2, 2, 1), (3, 3, 1))):
        st, en = w[a]
        for j in range(cnt):
            tt = st + j * (en - st) / cnt
            m.add(X.hum(0.8, 0.08, 330), tt, pan=0.6)
            m.add(X.clank(0.5, 1.2, 0.6), tt + (en - st) / cnt * 0.45)
    st, en = w[4]
    m.add(X.power_down(2.0, 0.4), st + (en - st) * 0.5)
    st, en = w[5]
    for j in range(7):
        m.add(X.clank(0.5, 0.9 + 0.05 * j, 0.6), st + (en - st) * (0.28 + j * 0.1))
    m.add(X.power_up(2.2, 0.45), st + (en - st) * 0.75)
    m.add(X.machine(w[6][1] - st - (en - st) * 0.8, 0.2, 5.0), st + (en - st) * 0.8)
    m.add(X.chime(0.35, 392.0, 4.5), w[6][0] + 0.2)
