#!/bin/bash
# usage: batch.sh PAR reel1 reel2 ...   (names without .js) -> /opt/bfyp/out/final/<name>/
cd /opt/bfyp
PAR=$1; shift
for n in "$@"; do echo "$n"; done | xargs -P $PAR -I{} sh -c '
  mkdir -p out/final/{}
  start=$(date +%s)
  timeout 2400 python3 engine/render_v2.py reels/{}.js --out out/final/{}/{}.mp4 --preview out/final/{}/prev --cover out/final/{}/{}_cover.png > out/final/{}/render.log 2>&1
  rc=$?
  echo "$(date +%H:%M:%S) {} rc=$rc $(( $(date +%s) - start ))s $(tail -c 300 out/final/{}/render.log | tr -d "\n")" >> out/final/batch.log
'
