#!/usr/bin/env python3
"""List reels whose VO build failed or is older than its spec (for one more build pass)."""
import sys
sys.path.insert(0, "/opt/bfyp/engine")
from vo2_status import REELS, status  # noqa: E402
print(" ".join(s["reel"] for s in map(status, REELS) if s["build"] in (False, "stale")))
