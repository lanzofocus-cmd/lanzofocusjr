#!/usr/bin/env bash
# Usage: ./build.sh projects/<name>
# Renders <project>/scenes.py with <project>/timings.json, mixes <project>/voiceover.mp3 over the
# shared ducked music (assets/music.m4a) and writes output/<OUTPUT from scenes.py>.
set -euo pipefail
cd "$(dirname "$0")"
PROJ=${1:?usage: ./build.sh projects/<name>}
OUTNAME=$(python3 -c "import ast,sys;t=ast.parse(open('$PROJ/scenes.py').read());print([n.value.value for n in t.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='OUTPUT'][0])")
# optional MUSIC = "twofaced" | "vyzee" in scenes.py picks a best-part bed (assets/bed_<name>.m4a)
MUSIC=$(python3 -c "import ast;t=ast.parse(open('$PROJ/scenes.py').read());print(([n.value.value for n in t.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='MUSIC']+[''])[0])")
if [ -n "$MUSIC" ] && [ -f "assets/bed_$MUSIC.m4a" ]; then TRACK="assets/bed_$MUSIC.m4a"; FADEIN=0.05; else TRACK=assets/music.m4a; FADEIN=1.5; fi
mkdir -p output
TMP=$(mktemp -d)
python3 render.py "$PROJ/timings.json" "$TMP/silent.mp4" "$PROJ/scenes.py"
python3 tools_sfx.py "$PROJ/timings.json" "$TMP/sfx.wav"
J="$PROJ/timings.json"
END=$(python3 -c "import json;print(json.load(open('$J'))['end'])")
INTRO_MS=$(python3 -c "import json;print(int(json.load(open('$J'))['intro']*1000))")
FADE=$(python3 -c "print($END-2.5)")
ffmpeg -v error -y -i "$TMP/silent.mp4" -i "$PROJ/voiceover.mp3" -stream_loop -1 -i "$TRACK" -i "$TMP/sfx.wav" -filter_complex "\
[1:a]adelay=$INTRO_MS|$INTRO_MS,aresample=44100,aformat=channel_layouts=stereo,apad,atrim=0:$END,asplit=2[vo][sc];\
[2:a]aresample=44100,aformat=channel_layouts=stereo,atrim=0:$END,volume=0.45,afade=t=in:d=$FADEIN,afade=t=out:st=$FADE:d=2.5[mu];\
[mu][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[duck];\
[3:a]aresample=44100,aformat=channel_layouts=stereo,volume=0.16,atrim=0:$END[fx];\
[vo][duck][fx]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -t "$END" -movflags +faststart "output/$OUTNAME"
rm -rf "$TMP"
echo "output/$OUTNAME"
