#!/usr/bin/env python3
"""Flashcards round 3 (teacher) — the gate's own script for
flashcard_truth_test.js (shared/flashcard-truth.js, pure, in Node). It runs
that file and passes its exit code through."""
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    node = shutil.which("node")
    if not node:
        print("flashcard_truth_test: node is not installed")
        sys.exit(1)
    sys.exit(subprocess.call([node, os.path.join(ROOT, "flashcard_truth_test.js")] + sys.argv[1:]))
