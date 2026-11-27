"""Street murmur and footsteps far above, muffled earth tone, a heartbeat-like pulse in the seed, roots creaking
and rocks cracking, rain and thunder above, then the breakthrough, birdsong-like chimes and a warm swell."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.murmur(w[1][1], 0.05), 0.0)
    m.steps(0.2, w[1][1], 1.6, 0.25, 1.0, soft=True)
    m.bed(X.lp(X.noise(w[3][1]), 200) * X.fade_env(int(w[3][1] * SR), 1, 1) * 0.3, 0.0)   # earth
    k = w[0][0] + 1.5
    while k < w[3][1]:
        m.add(X.heartbeat(0.35), k)
        k += 1.6
    st, en = w[2]
    for j in range(5):
        m.add(X.thud(0.3, 2.4, 0.2), st + (en - st) * (0.3 + 0.12 * j))
        m.add(X.hp(X.noise(0.2), 2) * X.env_ad(int(0.2 * SR), 0.002, 20) * 0.2, st + (en - st) * (0.3 + 0.12 * j))
    st, en = w[3]
    m.bed(X.rain(en - st + 1.0, 0.1), st)
    m.add(X.thunder(0.7), st + (en - st) * 0.6)
    st, en = w[4]
    m.add(X.low_hit(0.7), st + 0.2)
    m.add(X.swell(en - st, 0.25, bright=True), st)
    for j in range(8):
        m.add(X.chime(0.05, 2000 + 300 * (j % 3), 0.3, (1, 1.2)), st + 1.5 + j * 0.4, pan=rng.uniform(-0.7, 0.7))
    m.add(X.chime(0.35, 392.0, 4.5), w[5][0] + 0.2)
