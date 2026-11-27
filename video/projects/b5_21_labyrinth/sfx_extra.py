"""An electric hum as the neon maze draws itself, synthetic pings from every corridor, quick footsteps chasing,
a disorienting swirl, then silence, steady steps, walls grinding apart, and a bright chime at the exit."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.add(X.hum(w[4][1], 0.05, 110), 0.0)
    st, en = w[0]
    for j in range(14):
        m.add(X.tick(0.12, 1.5 + j * 0.1), st + j * (en - st) / 14)
    for i in (1, 2):
        st, en = w[i]
        k = st + 0.1
        while k < en:
            m.add(X.chime(0.08, rng.choice([880, 990, 1170, 1320]), 0.6, (1, 2.0)), k, pan=rng.uniform(-0.9, 0.9))
            k += rng.uniform(0.3, 0.6)
        m.steps(st, en, 4.5, 0.35, 1.2)
    m.add(X.swell(w[2][1] - w[2][0], 0.2), w[2][0])
    st, en = w[3]
    m.steps(st + (en - st) * 0.25, en, 2.2, 0.5, 1.0)
    m.add(X.lp(X.noise(1.5), 4) * X.fade_env(int(1.5 * SR), 0.2, 0.6) * 0.25, st + (en - st) * 0.2)
    m.add(X.chime(0.35, 523.25, 4.0), st + (en - st) * 0.5)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
