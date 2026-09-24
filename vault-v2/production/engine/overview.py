#!/usr/bin/env python3
"""Build vault-v2/covers_overview.jpg: 6x5 grid of all 30 covers with IDs."""
import cv2, numpy as np, os, sys, importlib.util
spec = importlib.util.spec_from_file_location("plan", "/opt/bfyp/plan/plan.py"); P = importlib.util.module_from_spec(spec); spec.loader.exec_module(P)
OUT = "/opt/bfyp/out/final"
tiles = []
for r in P.REELS:
    n = f"v2_{r['id'][3:]}_{r['slug']}"
    im = cv2.resize(cv2.imread(f"{OUT}/{n}/{n}_cover.png"), (270, 480), interpolation=cv2.INTER_AREA)
    bar = np.full((40, 270, 3), (13, 14, 8), np.uint8)
    cv2.putText(bar, r["id"], (10, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (138, 181, 23), 2, cv2.LINE_AA)
    tiles.append(cv2.copyMakeBorder(np.vstack([im, bar]), 6, 6, 6, 6, cv2.BORDER_CONSTANT, value=(13, 14, 8)))
rows = [np.hstack(tiles[i:i + 6]) for i in range(0, 30, 6)]
sheet = np.vstack(rows)
dst = sys.argv[1] if len(sys.argv) > 1 else "/opt/bfyp/test/covers_overview.jpg"
cv2.imwrite(dst, sheet, [cv2.IMWRITE_JPEG_QUALITY, 86])
print(dst, sheet.shape, round(os.path.getsize(dst) / 1e6, 2), "MB")
