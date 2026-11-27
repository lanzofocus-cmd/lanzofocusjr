"""Procedural sound-design helpers for the story videos (used by projects/*/sfx_extra.py).

Every function returns a mono float32 array at SR; Mixer.add places it on the timeline.
"""
import numpy as np

SR = 44100
_rng = np.random.default_rng(11)


def noise(sec):
    return _rng.standard_normal(max(1, int(sec * SR))).astype(np.float32)


def lp(x, k):
    k = max(1, int(k))
    return np.convolve(x, np.ones(k) / k, mode="same").astype(np.float32)


def hp(x, k):
    return (x - lp(x, k)).astype(np.float32)


def norm(x, peak=1.0):
    return (x / (np.abs(x).max() + 1e-6) * peak).astype(np.float32)


def env_ad(n, attack=0.01, decay=5.0):
    t = np.arange(n) / SR
    return (np.minimum(1, t / max(attack, 1e-4)) * np.exp(-t * decay)).astype(np.float32)


def fade_env(n, fin=0.3, fout=0.3):
    t = np.arange(n) / SR
    return np.minimum(1, np.minimum(t / max(fin, 1e-3), (n / SR - t) / max(fout, 1e-3))).clip(0, 1).astype(np.float32)


def step(gain=1.0, pitch=1.0, soft=False):
    n = int(0.10 * SR)
    t = np.arange(n) / SR
    thump = np.sin(2 * np.pi * 85 * pitch * t) * np.exp(-t * 45)
    tick = lp(noise(0.10), 6 if not soft else 14) * np.exp(-t * 90) * 0.5
    return ((thump + tick) * gain).astype(np.float32)


def thud(gain=1.0, pitch=1.0, length=0.6):
    n = int(length * SR)
    t = np.arange(n) / SR
    s = np.sin(2 * np.pi * 55 * pitch * t * (1 - 0.3 * t)) * np.exp(-t * 7) + lp(noise(length), 30) * np.exp(-t * 18) * 0.6
    return norm(s, gain)


def clank(gain=1.0, pitch=1.0, length=1.2):
    """Metallic hit: inharmonic partials with a noisy attack."""
    n = int(length * SR)
    t = np.arange(n) / SR
    s = np.zeros(n, dtype=np.float32)
    for f, a, dk in ((320, 1, 4), (857, 0.6, 6), (1430, 0.4, 8), (2210, 0.25, 11), (157, 0.7, 3)):
        s += a * np.sin(2 * np.pi * f * pitch * t) * np.exp(-t * dk)
    s += hp(noise(length), 3) * np.exp(-t * 60) * 0.8
    return norm(s, gain)


def chain_rattle(gain=0.6, length=0.8):
    n = int(length * SR)
    s = np.zeros(n, dtype=np.float32)
    for k in range(10):
        a = int(_rng.uniform(0, length * 0.8) * SR)
        c = clank(_rng.uniform(0.2, 0.5), _rng.uniform(2.0, 3.5), 0.15)
        s[a:a + len(c)] += c[:n - a]
    return norm(s, gain)


def snap(gain=1.0):
    """Breaking chain: sharp crack + bright ring."""
    c = clank(1.0, 1.8, 0.9)
    c[: int(0.02 * SR)] += hp(noise(0.02), 2) * 2
    return norm(c, gain)


def chime(gain=0.4, base=523.25, length=3.5, chord=(1, 1.26, 1.5, 2.0)):
    n = int(length * SR)
    t = np.arange(n) / SR
    s = sum(np.sin(2 * np.pi * base * r * t) * (1 / (1 + i * 0.7)) for i, r in enumerate(chord))
    return (s * np.exp(-t * 1.2) * np.minimum(1, t / 0.01) * gain).astype(np.float32)


def low_hit(gain=0.9, length=2.5):
    """Cinematic boom for reveals."""
    n = int(length * SR)
    t = np.arange(n) / SR
    s = np.sin(2 * np.pi * 42 * t * (1 - 0.15 * t)) * np.exp(-t * 2.2) + lp(noise(length), 120) * np.exp(-t * 3) * 0.8
    return norm(s, gain)


def swell(length, gain=0.3, bright=False):
    s = lp(noise(length), 12 if bright else 40)
    r = np.linspace(0, 1, len(s)) ** 2
    return norm(s, 1) * r * gain


def wind(length, gain=0.12):
    w = lp(lp(noise(length), 180), 60)
    w = norm(w, 1) * fade_env(len(w), 2.0, 1.5)
    lfo = 0.7 + 0.3 * np.sin(np.arange(len(w)) / SR * 0.7)
    return (w * lfo * gain).astype(np.float32)


def rain(length, gain=0.1):
    r = hp(noise(length), 4)
    return (norm(r, 1) * fade_env(len(r), 0.4, 0.4) * gain).astype(np.float32)


def thunder(gain=0.9, length=2.8):
    th = lp(lp(noise(length), 400), 200)
    t = np.arange(len(th)) / SR
    return norm(th, 1) * (np.minimum(1, t / 0.05) * np.exp(-t * 1.4)) * gain


def tick(gain=0.5, pitch=1.0):
    n = int(0.06 * SR)
    t = np.arange(n) / SR
    s = np.sin(2 * np.pi * 2400 * pitch * t) * np.exp(-t * 120) + hp(noise(0.06), 2) * np.exp(-t * 200) * 0.6
    return norm(s, gain)


def hum(length, gain=0.08, f=55):
    t = np.arange(int(length * SR)) / SR
    s = np.sin(2 * np.pi * f * t) + 0.5 * np.sin(2 * np.pi * f * 2 * t) + 0.25 * np.sin(2 * np.pi * f * 3 * t)
    return (s * fade_env(len(t), 0.6, 0.6) * gain / 1.75).astype(np.float32)


def machine(length, gain=0.1, rate=3.0):
    """Rhythmic clunk-hiss of a running machine."""
    n = int(length * SR)
    s = np.zeros(n, dtype=np.float32)
    k = 0.0
    while k < length - 0.3:
        c = clank(0.5, 0.5, 0.25) * 0.6 + lp(noise(0.25), 3) * env_ad(int(0.25 * SR), 0.01, 18) * 0.3
        a = int(k * SR)
        s[a:a + len(c)] += c[:n - a]
        k += 1 / rate
    return norm(s, gain)


def applause(length, gain=0.3):
    n = int(length * SR)
    s = np.zeros(n, dtype=np.float32)
    for _ in range(int(length * 120)):
        a = int(_rng.uniform(0, length - 0.05) * SR)
        c = hp(noise(0.03), 3) * env_ad(int(0.03 * SR), 0.001, 120) * _rng.uniform(0.3, 1)
        s[a:a + len(c)] += c[:n - a]
    return norm(s, 1) * fade_env(n, 0.5, 0.8) * gain


def murmur(length, gain=0.12):
    s = lp(noise(length), 25) * (0.6 + 0.4 * np.sin(np.arange(int(length * SR)) / SR * 5.3))
    return norm(s, 1) * fade_env(len(s), 0.4, 0.6) * gain


def fire(length, gain=0.08):
    s = lp(noise(length), 6) * 0.3
    n = len(s)
    for _ in range(int(length * 12)):
        a = int(_rng.uniform(0, length - 0.02) * SR)
        c = hp(noise(0.015), 2) * _rng.uniform(0.5, 1.5)
        s[a:a + len(c)] += c[:n - a]
    return norm(s, 1) * fade_env(n, 0.4, 0.4) * gain


def heartbeat(gain=0.6):
    a = thud(1.0, 1.1, 0.25)
    b = thud(0.7, 1.0, 0.3)
    s = np.zeros(int(0.9 * SR), dtype=np.float32)
    s[:len(a)] += a
    s[int(0.22 * SR):int(0.22 * SR) + len(b)] += b
    return norm(s, gain)


def spark(gain=0.3):
    return norm(hp(noise(0.25), 2) * env_ad(int(0.25 * SR), 0.001, 25), gain)


def power_up(length=1.6, gain=0.4):
    t = np.arange(int(length * SR)) / SR
    f = 40 + 120 * (t / length) ** 2
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) + 0.4 * np.sin(4 * np.pi * np.cumsum(f) / SR)
    return (s * np.minimum(1, t / 0.2) * fade_env(len(t), 0.05, 0.3) * gain).astype(np.float32)


def power_down(length=1.4, gain=0.4):
    return power_up(length, gain)[::-1].copy()


def page_flip(gain=0.4):
    s = hp(noise(0.18), 3) * env_ad(int(0.18 * SR), 0.02, 14)
    return norm(s, gain)


def whoosh(length=0.6, gain=0.4):
    n = int(length * SR)
    t = np.linspace(0, 1, n)
    s = lp(noise(length), 10) * np.sin(np.pi * t) ** 2
    return norm(s, gain)


class Mixer:
    """Adds sounds to the stereo buffer `out` that tools_sfx.py hands to sfx_extra.extra()."""

    def __init__(self, out):
        self.out = out

    def add(self, sig, t, gain=1.0, pan=0.0):
        a = int(t * SR)
        if sig is None or a >= len(self.out) or t < 0:
            return
        if sig.ndim == 1:
            sig = np.stack([sig * (1 - pan) * 0.7, sig * (1 + pan) * 0.7], axis=1)
        seg = self.out[a:a + len(sig)]
        seg += sig[:len(seg)] * gain

    def bed(self, sig, t, gain=1.0, width=700):
        """Wide stereo bed (decorrelated by a small delay)."""
        st = np.stack([sig, np.roll(sig, width)], axis=1) * 0.7
        self.add(st, t, gain)

    def steps(self, t0, t1, rate, gain=0.7, pitch=1.0, pan=0.0, soft=False):
        k = t0
        while k < t1:
            self.add(step(gain * _rng.uniform(0.8, 1.1), pitch * _rng.uniform(0.95, 1.05), soft), k, pan=pan)
            k += 1 / rate


def faded(sig, fin=0.3, fout=0.3, gain=1.0):
    """Apply a fade-in/out envelope matching the signal's own length."""
    return (sig * fade_env(len(sig), fin, fout) * gain).astype(np.float32)
