#!/usr/bin/env bash
# Render frames from timings.json, then mix voiceover + ducked music into output/.
# Needs assets/voiceover.mp3 and assets/music.wav (extract music with: ffmpeg -i <music.mov> -vn -ac 2 -ar 44100 assets/music.wav)
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p output
TMP=$(mktemp -d)
python3 render.py timings.json "$TMP/silent.mp4"
END=$(python3 -c "import json;print(json.load(open('timings.json'))['end'])")
INTRO_MS=$(python3 -c "import json;print(int(json.load(open('timings.json'))['intro']*1000))")
FADE=$(python3 -c "print($END-2.5)")
ffmpeg -v error -y -i "$TMP/silent.mp4" -i assets/voiceover.mp3 -i assets/music.wav -filter_complex "\
[1:a]adelay=$INTRO_MS|$INTRO_MS,aresample=44100,aformat=channel_layouts=stereo,apad,atrim=0:$END,asplit=2[vo][sc];\
[2:a]atrim=0:$END,volume=0.45,afade=t=in:d=1.5,afade=t=out:st=$FADE:d=2.5[mu];\
[mu][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[duck];\
[vo][duck]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -t "$END" -movflags +faststart \
  output/The_Version_Youre_Becoming_16x9.mp4
rm -rf "$TMP"
