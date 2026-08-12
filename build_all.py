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
now fixed at source — ``build_site()`` lifts foreign output trees out before
the wipe and puts them back after, so the two generators are safe in either
order. This script exists so nobody has to know that: run one command, get a
complete site, every time.

The KS4 generator still runs first here, because that is the order the deploy
notes and the commit history describe, and there is no reason to diverge from
it now that either order is safe.
"""

import subprocess
import sys

STEPS = [
    ("KS4 site — combined/, triple/, root pages, shared/", "generate_site_v5.py"),
    ("KS3 site — ks3/ (33 units, 183 lesson slots)",       "build_ks3.py"),
]


def main():
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
    print("   Next: check `git status`, then Mide pushes via GitHub Desktop.")
    print("─" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
