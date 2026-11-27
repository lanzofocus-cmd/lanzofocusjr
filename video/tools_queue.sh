#!/usr/bin/env bash
# Render worker: builds every projects/<glob> that has a .ready marker and no output yet.
# Usage: nohup ./tools_queue.sh 'b5_*' > logs/queue_1.log 2>&1 &   (run up to 3 workers)
cd "$(dirname "$0")"
GLOB=${1:-b5_*}
while true; do
  found=0
  for p in projects/$GLOB; do
    [ -f "$p/.ready" ] || continue
    out=$(python3 -c "import ast;t=ast.parse(open('$p/scenes.py').read());print([n.value.value for n in t.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='OUTPUT'][0])")
    [ -f "output/$out" ] && continue
    mkdir "$p/.lock" 2>/dev/null || continue   # another worker has it
    found=1
    echo "$(date +%T) building $p"
    ./build.sh "$p" > "logs/$(basename $p).log" 2>&1 || echo "$(date +%T) FAILED $p"
    rmdir "$p/.lock"
  done
  [ $found = 0 ] && sleep 20
done
