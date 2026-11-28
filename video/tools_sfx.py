"""Atmospheric sound-design track: a soft filtered-noise whoosh at every scene change.

Usage: python3 tools_sfx.py projects/<name>/timings.json out.wav
"""
import json, sys
import numpy as np
import soundfile as sf

SR = 44100
tim = json.load(open(sys.argv[1]))
end = tim["end"]
starts = [0.0] + [s for s, _ in tim["segments"]]
if len(sys.argv) > 3:  # actual (beat-snapped) scene cut times written by render.py
    starts = [0.0] + json.load(open(sys.argv[3]))
out = np.zeros((int(end * SR) + SR, 2), dtype=np.float32)
rng = np.random.default_rng(1)


def whoosh(length=0.9, peak=0.6):
    n = int(length * SR)
    noise = rng.standard_normal(n).astype(np.float32)
    # band-limit with a moving average whose width sweeps (a crude sweeping low-pass)
    env_t = np.linspace(0, 1, n)
    env = np.sin(np.pi * env_t ** peak) ** 2
    lo = np.convolve(noise, np.ones(60) / 60, mode="same")
    hi = np.convolve(noise, np.ones(8) / 8, mode="same")
    mix = lo * (1 - env_t) + hi * env_t * 0.35
    sig = mix * env
    pan = np.linspace(-0.4, 0.4, n)
    return np.stack([sig * (1 - pan) * 0.5, sig * (1 + pan) * 0.5], axis=1)


for i, st in enumerate(starts):
    w = whoosh(0.8 if i else 1.4)
    a = int(max(0, st - 0.45) * SR)
    seg = out[a:a + len(w)]
    seg += w[:len(seg)]
out /= max(1e-6, np.abs(out).max())
sf.write(sys.argv[2], out * 0.5, SR)
