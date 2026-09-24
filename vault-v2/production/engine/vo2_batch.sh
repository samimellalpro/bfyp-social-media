#!/bin/bash
# vo2_batch.sh <parallel> <reel>... : build the directed VO of several reels, logs in vo2/logs/<reel>.build.txt
cd /opt/bfyp
P=$1; shift
printf '%s\n' "$@" | xargs -P "$P" -I{} sh -c 'python3 engine/vo2.py build {} 2>&1 | grep -v "Warning\|WeightNorm" > vo2/logs/{}.build.txt'
