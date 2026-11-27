#!/usr/bin/env bash
# Restartable render queue. Usage: ./tools_queue.sh queue.txt
# Each line of the queue file is a project dir (projects/<name>); a line "END" stops the runner once
# everything above it is done. Finished projects are appended to <queue>.done, so re-running resumes.
# Voices a project first if it has no voiceover yet. Renders 3 at a time.
set -u
cd "$(dirname "$0")"
Q=$1; D=$Q.done; touch "$D"; mkdir -p logs
one() {
  p=$1
  [ -f "$p/voiceover.mp3" ] || nice python3 tts/speak.py "$p" af_heart 0.92 > "logs/$(basename "$p").voice.log" 2>&1
  if ./build.sh "$p" > "logs/$(basename "$p").log" 2>&1; then echo "OK $p"; echo "$p" >> "$D"; else echo "FAIL $p"; fi
}
export -f one; export D
while true; do
  pending=$(grep -v '^END$' "$Q" | grep -vxF -f "$D" || true)
  if [ -z "$pending" ]; then grep -qx END "$Q" && exit 0; sleep 20; continue; fi
  echo "$pending" | xargs -P 3 -I{} bash -c 'one {}'
done
