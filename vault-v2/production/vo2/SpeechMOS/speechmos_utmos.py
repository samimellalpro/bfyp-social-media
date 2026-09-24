"""Shim: load tarepan/SpeechMOS UTMOS22 strong (MIT) from local code + release weights (no torch.hub, no network)."""
import os
import sys

import torch

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from utmos_pkg.utmos22.strong.model import UTMOS22Strong  # noqa: E402


def load_utmos():
    m = UTMOS22Strong()
    m.load_state_dict(torch.load(os.path.join(HERE, "utmos22_strong_step7459_v1.pt"), map_location="cpu"))
    m.eval()
    return m
