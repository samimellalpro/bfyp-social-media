#!/bin/bash
# Mix + QC every reel whose VO build passes and whose final is missing or stale, one at a time, until all 30 are final
cd /opt/bfyp
for i in $(seq 1 400); do
  busy=$(ps -eo args | grep -E "vo2.py (mix|qc) " | grep -v grep | awk '{print $4}' | sort -u | tr '\n' ' ')
  todo=$(python3 engine/vo2_status.py --to-mix)
  [ "$1" = "rev" ] && todo=$(echo $todo | tr " " "\n" | tac | tr "\n" " ")
  next=""
  for r in $todo; do case " $busy " in *" $r "*) ;; *) next=$r; break;; esac; done
  if [ -n "$next" ]; then
    echo "$(date +%T) mix $next"; engine/vo2_mixqc.sh 1 $next; tail -1 vo2/logs/$next.mixqc.txt
  else
    done=$(python3 engine/vo2_status.py | tail -1)
    case "$done" in 30/30*) echo "$(date +%T) all final: $done"; exit 0;; esac
    sleep 20
  fi
done
