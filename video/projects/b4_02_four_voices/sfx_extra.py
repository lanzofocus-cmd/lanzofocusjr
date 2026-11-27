"""Sound design: night wind, a lightning crack on the peak, voices rising, falling rocks, the fire of the warm room,
a glassy shimmer for Doubt's mirrors, a heartbeat, and Courage's footsteps."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.4
SFX_VOLUME = 0.3


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[8][1], 0.16), 0.0)
    m.add(X.thunder(0.8, 3.0), w[0][0] + 0.3)
    m.add(X.low_hit(0.7), w[1][0] + 0.2)                       # the voices rise
    m.bed(X.murmur(w[5][1] - w[1][0], 0.07), w[1][0])            # whispering under scenes 1-5
    st, en = w[2]
    for k in range(5):                                           # rocks tumbling down the flank
        m.add(X.thud(0.25, 2.2, 0.25), st + (en - st) * (0.3 + k * 0.12), pan=0.5)
    m.add(X.fire(w[3][1] - w[3][0], 0.25), w[3][0] + 0.3, pan=-0.4)
    st, en = w[4]
    for k in range(6):                                           # mirror shards appearing
        m.add(X.chime(0.08, 1300 + 140 * k, 1.5, (1, 1.5)), st + (en - st) * 0.08 + k * 0.18)
    m.add(X.heartbeat(0.6), st + (en - st) * 0.45)
    m.add(X.heartbeat(0.5), st + (en - st) * 0.45 + 0.95)
    st, en = w[5]
    m.steps(st + 0.3, en, 2.6, 0.45, 1.1, pan=0.2)
    st, en = w[6]
    m.steps(st + (en - st) * 0.2, en, 2.4, 0.7, 0.95)
    m.add(X.chime(0.25, 392.0, 4.0), st + (en - st) * 0.2)       # the first step
    m.add(X.swell(w[8][1] - w[7][0], 0.18, bright=True), w[7][0])
