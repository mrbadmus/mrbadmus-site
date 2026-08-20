"""build_all.py — build the whole site, both generators, correct order.

Run it:

    python3 build_all.py

**This is the entrypoint to use.** The site is produced by two deliberately
separate generators:

* ``generate_site_v5.py`` → the KS4 site (982 pages: combined/, triple/, the
  hand-written root pages, shared/).
* ``build_ks3.py``        → the KS3 site (221 pages under ks3/).

They are separate on purpose — see the module docstring in ``build_ks3.py``.
Wiring KS3 into ``build_site()`` would rebuild 300+ KS4 pages on every KS3
content change and make architecture.md §9's "zero KS4 pages changed" gate
impossible to demonstrate.

Separate generators used to mean an order that mattered: ``build_site()``
wipes ``mrbadmus_site/`` and rebuilt it, which silently deleted
``mrbadmus_site/ks3/`` whenever the KS4 generator ran second. That hazard is
now fixed at source — ``build_site()`` SKIPS the foreign output trees named in
its ``FOREIGN_OUTPUT_DIRS`` where they stand, so the two generators are safe in
either order. (This paragraph used to say the trees were lifted out and put
back afterwards. That was an earlier fix, and it was replaced precisely because
it stranded the KS3 output in a temp directory if the build raised in between;
nothing is moved now.) This script exists so nobody has to know any of that:
run one command, get a complete site, every time.

``mrbadmus_site/3d/`` is on the same list as of MRB-194, but it is NOT built
here: 3D Studio is a Vite app, and ``npm run build`` inside ``3d-studio/`` is a
manual pre-step (see CLAUDE.md). A Node failure must not be able to fail a KS3
or KS4 build. The generator publishes whatever build exists and shouts, loudly
and twice, when that build is stale or missing.

The KS4 generator still runs first here, because that is the order the deploy
notes and the commit history describe, and there is no reason to diverge from
it now that either order is safe.
"""

import os
import subprocess
import sys

STEPS = [
    ("KS4 site — combined/, triple/, root pages, shared/", "generate_site_v5.py"),
    ("KS3 site — ks3/ (33 units, 183 lesson slots)",       "build_ks3.py"),
    # ⊕ MRB-270 phase 8a. LAST, and that ordering is load-bearing.
    # generate_site_v5.py rmtree's mrbadmus_site/ on the way in, so anything
    # emitted before it is deleted by it. build_student.py writes straight into
    # mrbadmus_site/student/ and mirrors to student/, exactly as build_ks3.py
    # does for ks3/, so it has to run after the tree exists.
    ("student preview pages — student/*-preview.html",     "build_student.py"),
]


def main():
    # ⊕ MRB-271 — the steps below are BARE SCRIPT NAMES, and a bare name
    # resolves against the current directory. Without this, running
    # `python3 /elsewhere/build_all.py` from inside a worktree ran the
    # WORKTREE's generators while reporting /elsewhere's name, and running it
    # from a directory with no generators at all failed three times over with
    # "can't open file". Anchor to this file's own directory: build_all always
    # builds the checkout it belongs to, whatever the invocation path.
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("\n🏗️  build_all — %d generators, in order\n" % len(STEPS))

    for i, (label, script) in enumerate(STEPS, 1):
        print("─" * 72)
        print("  [%d/%d] %s" % (i, len(STEPS), label))
        print("         python3 %s" % script)
        print("─" * 72)

        result = subprocess.run([sys.executable, script])
        if result.returncode != 0:
            print("\n❌ build_all FAILED at step %d/%d (%s), exit code %d."
                  % (i, len(STEPS), script, result.returncode))
            print("   Later steps were NOT run — the output tree is incomplete.")
            return result.returncode
        print()

    print("─" * 72)
    print("✅ build_all complete — both generators ran, in order.")
    # ⊕ MRB-228 — this used to say "then Mide pushes via GitHub Desktop".
    # Push authorisation is standing and permanent; see CLAUDE.md's Autonomy
    # Contract. The shipping discipline is one unit, one commit, one push.
    print("   Next: check `git status`, run the unit's gates, commit and push,")
    print("         then verify live with ./check_ks3_live.sh <UNIT>.")
    print("─" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
