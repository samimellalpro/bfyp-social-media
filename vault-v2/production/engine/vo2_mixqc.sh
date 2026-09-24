#!/bin/bash
# vo2_mixqc.sh <parallel> <reel>... : mix the built VO into the validated reel (video copied bit for bit), then final-file QC.
# Output: vo2/final/<reel>/<reel>_VO.mp4 (+ .log.json, .qc.json); one line per reel in vo2/logs/<reel>.mixqc.txt
cd /opt/bfyp
P=$1; shift
printf '%s\n' "$@" | xargs -P "$P" -I{} sh -c '
  mkdir -p vo2/final/{}
  python3 engine/vo2.py mix {} vo2/final/{}/{}_VO.mp4 > vo2/logs/{}.mixqc.txt 2>&1 &&
  python3 engine/vo2.py qc {} vo2/final/{}/{}_VO.mp4 2>&1 | grep -v "Warning\|WeightNorm" >> vo2/logs/{}.mixqc.txt'
