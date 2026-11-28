#!/usr/bin/env python3
"""Build a per-video music track that is cut to the song's beat grid.

Usage: python3 tools_track.py <song name> <timings.json> <drop_time_s|-1> <out.wav> <beats.json>

Layout on the video timeline:
  0 .. K-B      the song's strongest section, starting on its drop (the hook lands on the drop)
  K-B .. K      the song's own build-up (or, for songs without one, a one-beat dropout)
  K ..          the drop again, exactly on the key line of the voiceover (K = drop_time)
Every join is on a beat, so the loop never drifts off the grid. beats.json lists every beat time
on the video timeline plus the drop time, for beat-synced cuts and visual pulses in render.py.
"""
import json, subprocess, sys, tempfile, os
import numpy as np
import soundfile as sf

SONGS = {
    # src, drop (s), beats per minute, loop length in beats, build-up length in beats (0 = dropout)
    "twofaced": dict(src="assets/music_twofaced.m4a", drop=27.67, bpm=73.7, loop_beats=38, build_beats=6),
    "vyzee": dict(src="assets/music.m4a", drop=4.41, bpm=102.6, loop_beats=94, build_beats=0),
}
SR = 44100

name, timings, K, out, beats_out = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4], sys.argv[5]
S = SONGS[name]
end = json.load(open(timings))["end"]
P = 60.0 / S["bpm"]
with tempfile.TemporaryDirectory() as tmp:
    wav = os.path.join(tmp, "s.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", S["src"], "-ar", str(SR), "-ac", "2", wav], check=True)
    song, _ = sf.read(wav, dtype="float32")


def at(t):
    return int(round(t * SR))


D = S["drop"]
loop = song[at(D):at(D + S["loop_beats"] * P)]
gain = 0.1 / max(1e-6, float(np.sqrt(np.mean(loop ** 2))))  # same loudness for every song
song = song * gain
loop = loop * gain


def strong(n):
    """n samples of the strong section, looping on the beat with tiny crossfades."""
    xf = at(0.06)
    outa = np.zeros((0, 2), np.float32)
    while len(outa) < n:
        piece = loop.copy()
        if len(outa):
            ramp = np.linspace(0, 1, xf)[:, None]
            outa[-xf:] = outa[-xf:] * (1 - ramp) + piece[:xf] * ramp
            piece = piece[xf:]
        outa = np.concatenate([outa, piece])
    return outa[:n]


total = at(end + 1)
beats = []
if K <= 0 or K > end - 2:  # no drop line: strong section from frame 0
    track = strong(total)
    beats = list(np.arange(0, end, P))
    K = -1
else:
    B = S["build_beats"] * P
    a_len = max(0.0, K - (B if B else P) + 0.2)  # +0.2 s overlap for the crossfade into the build
    track = strong(at(a_len))
    beats += list(np.arange(0, a_len, P))
    if B:
        build = song[at(D - B):at(D)]
        beats += list(K - B + np.arange(0, S["build_beats"]) * P)
    else:  # dropout: one beat of the song fading to silence
        build = song[at(D):at(D + P)] * np.linspace(1, 0, at(P))[:, None] ** 3
    xf = at(0.2)
    if len(track) > xf and len(build) > xf:
        r = np.linspace(0, 1, xf)[:, None]
        track[-xf:] = track[-xf:] * (1 - r) + build[:xf] * r
        build = build[xf:]
    track = np.concatenate([track, build])
    track = track[:at(K)] if len(track) > at(K) else np.concatenate([track, np.zeros((at(K) - len(track), 2), np.float32)])
    track = np.concatenate([track, strong(total - len(track))])
    beats += list(np.arange(K, end, P))
sf.write(out, np.clip(track[:total], -0.98, 0.98), SR)
json.dump({"beats": [round(float(b), 3) for b in sorted(beats) if b < end], "drop": K, "period": P}, open(beats_out, "w"))
print(out)
