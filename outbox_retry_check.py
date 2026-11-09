#!/usr/bin/env python3
"""outbox_retry_check.py — runs outbox_retry_check.js under Node (see there)."""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.exit(subprocess.call(["node", os.path.join(HERE, "outbox_retry_check.js")]))
