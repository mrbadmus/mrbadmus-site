#!/usr/bin/env python3
"""studio_build.py — the 3D Studio gates build the studio themselves.

The three 3D gates (3d_parity, 3d_render_check, 3d_isolation) all measure
`3d-studio/dist/`, which is gitignored. They used to be SKIPPED by the push
guard on any checkout with no dist/ (registry `needs="3d-studio/dist"`), so a
red studio gate could sit unnoticed for weeks and every push on a clean
machine passed without measuring the studio at all.

`ensure_built()` is called first thing in each gate's main(). When dist/ is
missing or older than its sources it runs `npm ci` (only if node_modules is
missing) and `npm run build` in 3d-studio/, then lets the gate proceed. It
returns None on success and a one-paragraph FAILURE message otherwise
(no node/npm, install failed, build failed). The gate prints it and exits
non-zero: a studio that cannot be built is a red gate, never a skip.

This does NOT change the site generator, which still never builds the studio
(CLAUDE.md, "3D Studio has a manual build step"): a Node problem must not be
able to fail a KS3/KS4 site build. Only the GATES build it.
"""
from __future__ import annotations

import os
import shutil
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(HERE, "3d-studio")
DIST = os.path.join(APP, "dist")

# What Vite reads. Same set the generator's staleness banner compares
# (src, content, public) plus the files that change a build without touching
# them. node_modules is never walked.
_SOURCE_DIRS = ("src", "content", "public")
_SOURCE_FILES = ("index.html", "vite.config.ts", "tsconfig.json",
                 "package.json", "package-lock.json")


def _newest_source_mtime():
    newest = 0.0
    for d in _SOURCE_DIRS:
        for dirpath, dirs, files in os.walk(os.path.join(APP, d)):
            dirs[:] = [x for x in dirs if x != "node_modules"]
            for f in files:
                if f == ".DS_Store":
                    continue
                try:
                    newest = max(newest, os.path.getmtime(os.path.join(dirpath, f)))
                except OSError:
                    pass
    for f in _SOURCE_FILES:
        try:
            newest = max(newest, os.path.getmtime(os.path.join(APP, f)))
        except OSError:
            pass
    return newest


def needs_build():
    """Why dist/ must be (re)built, or None when it is present and fresh."""
    index = os.path.join(DIST, "index.html")
    if not os.path.exists(index):
        return "3d-studio/dist/ is missing"
    if _newest_source_mtime() > os.path.getmtime(index):
        return "3d-studio/dist/ is older than its sources"
    return None


def _run(cmd, label):
    print("  [studio_build] %s ..." % label, flush=True)
    r = subprocess.run(cmd, cwd=APP, capture_output=True, text=True)
    if r.returncode != 0:
        tail = "\n".join(((r.stdout or "") + (r.stderr or "")).strip().splitlines()[-25:])
        return "`%s` failed (exit %d):\n%s" % (" ".join(cmd), r.returncode, tail)
    return None


def ensure_built():
    """Build the studio if dist/ is missing or stale. None on success, else a
    failure message. Never skips: no node/npm is a FAILURE."""
    why = needs_build()
    if why is None:
        return None
    print("  [studio_build] %s - building the studio first" % why)
    node, npm = shutil.which("node"), shutil.which("npm")
    if not node or not npm:
        return ("cannot build the 3D Studio: %s not found on PATH. These gates "
                "no longer skip when dist/ is missing - install Node (see "
                "3d-studio/package.json) or run the gate on a machine that has it."
                % ("node and npm" if not (node or npm) else ("node" if not node else "npm")))
    if not os.path.isdir(os.path.join(APP, "node_modules")):
        err = _run([npm, "ci"], "npm ci")
        if err:
            return err
    err = _run([npm, "run", "build"], "npm run build")
    if err:
        return err
    if needs_build() is not None:
        return ("`npm run build` exited 0 but 3d-studio/dist/ is still missing "
                "or stale - refusing to measure it.")
    return None
