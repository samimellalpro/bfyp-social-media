#!/usr/bin/env python3
"""Regenerate assets/screens/<id>@2x.png from the 1x crops (Lanczos x2 + light unsharp), as used by the renders."""
import glob, os, sys
import cv2
d = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "screens")
for f in sorted(glob.glob(os.path.join(d, "*.png"))):
    if f.endswith("@2x.png"):
        continue
    im = cv2.imread(f)
    up = cv2.resize(im, (im.shape[1] * 2, im.shape[0] * 2), interpolation=cv2.INTER_LANCZOS4)
    up = cv2.addWeighted(up, 1.35, cv2.GaussianBlur(up, (0, 0), 1.2), -0.35, 0)
    cv2.imwrite(f[:-4] + "@2x.png", up)
    print("wrote", os.path.basename(f)[:-4] + "@2x.png")
