#!/bin/bash
# usage: fastbatch.sh reel1.js reel2.js ...  (3 in parallel)
cd /opt/bfyp
for f in "$@"; do
  n=$(basename $f .js)
  echo "$n"
done | xargs -P 3 -I{} sh -c 'timeout 300 python3 engine/render_v2.py reels/{}.js --out out/fast/{}.mp4 --fast out/fast/{} > out/fast/{}.log 2>&1; echo "{} $(tail -c 200 out/fast/{}.log | tr -d "\n")"'
