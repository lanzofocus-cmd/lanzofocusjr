"""Sound design: high mountain wind, boots on rock and snow, a slip and a slide, heavy breathing, the flag
snapping on the summit, a deep rumble as the next mountain rises, a low drone for the shadow, and a warm
resolution as the trail lights up."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[9][1], 0.2), 0.0)
    st, en = w[2]
    f0, f1, u1 = 0.38, 0.5, 0.62
    m.steps(st, st + (en - st) * f0, 2.6, 0.6, 0.9, soft=True)
    m.add(X.lp(X.noise(0.6), 6) * X.fade_env(int(0.6 * SR), 0.02, 0.3) * 0.5, st + (en - st) * f0)  # slide
    m.add(X.thud(0.8, 0.8), st + (en - st) * (f0 + 0.05))
    for j in range(3):  # breathing
        b = X.lp(X.noise(0.7), 18) * X.fade_env(int(0.7 * SR), 0.3, 0.3) * 0.25
        m.add(b, st + (en - st) * f1 + j * 0.8)
    m.steps(st + (en - st) * u1, en, 2.2, 0.6, 0.85, soft=True)
    m.bed(X.wind(en - st, 0.1), st + (en - st) * u1)
    st, en = w[3]
    m.add(X.thud(0.5, 1.5, 0.3), st + 0.1)                                    # flag planted
    m.add(X.chime(0.25, 523.25, 3.0), st + 0.2)
    st, en = w[4]
    m.add(X.low_hit(0.9, 4.0), st + 0.2)                                      # the next mountain rises
    m.add(X.thunder(0.5, 3.5), st + 0.4)
    m.add(X.hum(w[6][1] - w[5][0], 0.08, 40), w[5][0])                       # the shadow's drone
    m.add(X.heartbeat(0.5), w[5][0] + 1.0)
    m.add(X.heartbeat(0.5), w[6][0] + 0.5)
    st, en = w[8]
    for j in range(12):  # trail lights coming on, top to bottom
        m.add(X.chime(0.06, 880 - 30 * j, 1.0, (1, 1.5)), st + 0.4 + j * (en - st - 1) / 12)
    m.add(X.swell(w[9][1] - st, 0.2, bright=True), st)
    m.add(X.chime(0.3, 392.0, 4.5), w[9][0] + 0.2)
