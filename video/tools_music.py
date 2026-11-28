#!/usr/bin/env python3
"""Build a music bed that starts on a track's best part and keeps looping that part.

Usage: python3 tools_music.py <source audio> <best_start_s> <best_end_s> <out.m4a> [minutes]

The section [best_start, best_end] is repeated with 1.5 s crossfades so a video of any length
stays inside the strongest part of the song, and the very first frame lands on the drop.
The bed is loudness-normalised so different tracks sit at the same level under the voice.
"""
import subprocess, sys, tempfile, os

src, s0, s1, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
minutes = float(sys.argv[5]) if len(sys.argv) > 5 else 3.0
seg_len = s1 - s0
xf = 1.5
copies = max(2, int(minutes * 60 / (seg_len - xf)) + 1)
with tempfile.TemporaryDirectory() as tmp:
    seg = os.path.join(tmp, "seg.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(s0), "-t", str(seg_len), "-i", src,
                    "-ar", "44100", "-ac", "2", seg], check=True)
    args = ["ffmpeg", "-v", "error", "-y"]
    for _ in range(copies):
        args += ["-i", seg]
    chain, last = [], "[0:a]"
    for i in range(1, copies):
        lbl = f"[x{i}]"
        chain.append(f"{last}[{i}:a]acrossfade=d={xf}:c1=tri:c2=tri{lbl}")
        last = lbl
    chain.append(f"{last}loudnorm=I=-16:TP=-1.5:LRA=11,aresample=44100[out]")
    args += ["-filter_complex", ";".join(chain), "-map", "[out]", "-c:a", "aac", "-b:a", "192k", out]
    subprocess.run(args, check=True)
print(out)
