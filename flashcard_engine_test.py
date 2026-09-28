#!/usr/bin/env python3
"""MRB-351 pupil flow — the gate's own script for flashcard_engine_test.js.

The engine is plain browser JavaScript, so its test is a Node file; this is
the .py the gate registry names (gate_watches_check needs one) and all it
does is run that file and pass its exit code through. See
flashcard_engine_test.js for what is proved.
"""
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    node = shutil.which("node")
    if not node:
        print("flashcard_engine_test: node is not installed, so the engine cannot be run")
        sys.exit(1)
    sys.exit(subprocess.call([node, os.path.join(ROOT, "flashcard_engine_test.js")] + sys.argv[1:]))
