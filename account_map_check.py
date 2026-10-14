#!/usr/bin/env python3
"""account_map_check.py — the one map of who goes where (front door, Part 1).

`shared/account.js` is plain browser JavaScript, so its test is a Node file;
this is the .py the gate registry names (every gate needs one —
`gate_watches_check` requires it) and all it does is run that file and pass
its exit code through, exactly as `week_scope_check.py` does for
`week_scope_check.js`. See `account_map_check.js` for what is proved.
"""
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    node = shutil.which("node")
    if not node:
        print("account_map_check: node is not installed, so shared/account.js cannot be run")
        sys.exit(1)
    sys.exit(subprocess.call([node, os.path.join(ROOT, "account_map_check.js")] + sys.argv[1:]))
