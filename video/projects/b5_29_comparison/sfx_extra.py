"""A dizzy city roar overhead, traffic and murmuring crowds, a hollow wind in the empty lot, then hammering
and building sounds rising with a warm swell as the city noise fades away."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.add(X.swell(w[0][1] - w[0][0], 0.25), w[0][0])
    city_end = w[3][0] + (w[3][1] - w[3][0]) * 0.4
    m.bed(X.murmur(city_end, 0.12), 0.0)
    m.bed(X.lp(X.noise(city_end), 60) * X.fade_env(int(city_end * SR), 0.5, 1.0) * 0.15, 0.0)
    m.bed(X.wind(w[2][1] - w[2][0], 0.12), w[2][0])
    st, en = w[3]
    k = st + (en - st) * 0.15
    while k < en - 0.5:
        m.add(X.clank(0.25, rng.uniform(0.9, 1.3), 0.25), k)
        k += 0.35
    m.add(X.swell(en - st, 0.25, bright=True), st + (en - st) * 0.2)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
