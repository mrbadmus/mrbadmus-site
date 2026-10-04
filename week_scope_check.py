#!/usr/bin/env python3
"""week_scope_check.py — x-week-truth (MRB-353 redone), 4 Oct 2026.

`weekScope` (shared/teacher-live.js) is plain browser JavaScript, so its
test is a Node file; this is the .py the gate registry names (every gate
needs one — `gate_watches_check` requires it) and all it does is run that
file and pass its exit code through, exactly as `flashcard_engine_test.py`
does for `flashcard_engine_test.js`. See `week_scope_check.js` for what is
actually proved.
"""
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    node = shutil.which("node")
    if not node:
        print("week_scope_check: node is not installed, so weekScope cannot be run")
        sys.exit(1)
    sys.exit(subprocess.call([node, os.path.join(ROOT, "week_scope_check.js")] + sys.argv[1:]))
