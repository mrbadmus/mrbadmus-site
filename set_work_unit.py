#!/usr/bin/env python3
"""set_work_unit.py — Set work v2's two pure suites, run as one gate.

    python3 set_work_unit.py
    MRB_BACKEND=/path/to/backend python3 set_work_unit.py
    python3 set_work_unit.py /path/to/backend

── WHY A PYTHON WRAPPER ROUND TWO `node` COMMANDS ─────────────────────

Because they live in two repos and one of them is not this one.

`test_set_work_v2.js` is in the BACKEND checkout and tests `set-work-scope.js`
— the pure half of Set work: the class-name rule, the cohort, the tree filter,
the pool spec, the paper map, `pickRoundRobin`. `tools/set_work_time_test.js`
is in THIS repo and tests the sheet's London↔UTC helpers, which are the other
half of the same feature and the one that cannot be tested from Python at all
(`Intl` is the authority and the browser is where it lives).

Neither had a row in `gate_registry.py`. Both existed, both worked, and both
could only run if a human remembered them by name — which is the exact defect
the registry was built after (`verify_questions`, MRB-277). A gate that
straddles two repos is still a gate; it just needs somewhere to stand.

⚠️ THE BACKEND CHECKOUT IS NAMED, NOT GUESSED, and the precedence is
`pool_ownership.py`'s, deliberately, so the two cannot come to disagree about
which backend a run is measuring. The main checkout is a SHARED working copy
that any session can leave on any branch: on 7 September it was sitting on a
colleague's branch, and a gate pointed at it would have reported green about
code nobody was shipping. An argument, then `MRB_BACKEND`, then the sibling
repo — the last because that is what an ordinary machine has.

⚠️ FAST, AND IT HAS TO STAY FAST. Neither suite touches a database, a network
or a clock — that is what makes them the PURE half. `test_set_work_v2.js` does
open a Supabase connection for its bank-shape probes and cleans up after
itself; if that ever grows into something slow, this row moves to `slow` and
earns a receipt rather than being quietly tolerated inside a push hook.
"""

import os
import subprocess
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO)

BACKEND = (
    (sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else None)
    or os.environ.get("MRB_BACKEND")
    or "/Users/midebadmus/Documents/GitHub/mrbadmus---backend"
)

SUITES = [
    ("set-work-scope.js — the class-name rule, the cohort, the tree filter, "
     "the pool spec, the paper map, pickRoundRobin",
     BACKEND, ["node", "test_set_work_v2.js"]),
    ("the sheet's London↔UTC helpers — the BST boundary, in the only place "
     "`Intl` is the authority",
     REPO, ["node", "tools/set_work_time_test.js"]),
]


def main():
    print("\n🧪  set_work_unit — Set work v2's two pure suites")
    print("    backend: %s\n" % BACKEND)

    if not os.path.isfile(os.path.join(BACKEND, "server.js")):
        print("❌ %s is not a backend checkout (no server.js).\n"
              "   Name one with MRB_BACKEND, or pass it as an argument. This "
              "gate is\n   about the code being shipped, and a guess is not "
              "that." % BACKEND)
        return 1

    bad = []
    for label, cwd, cmd in SUITES:
        script = os.path.join(cwd, cmd[-1])
        if not os.path.isfile(script):
            print("❌ %s\n   missing: %s" % (label, script))
            bad.append(label)
            continue
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
        out = (r.stdout or "") + (r.stderr or "")
        tail = [l for l in out.strip().split("\n") if l.strip()][-1:]
        print("   %s  %s" % ("✅" if r.returncode == 0 else "❌", label))
        print("        %s" % (tail[0].strip() if tail else "(no output)"))
        if r.returncode != 0:
            bad.append(label)
            # The failures, not the whole log: a suite that prints every
            # passing check buries the two lines a reader needs.
            for line in out.split("\n"):
                if "❌" in line or "not ok" in line.lower():
                    print("        · %s" % line.strip()[:160])

    if bad:
        print("\n❌ set_work_unit: %d of %d suite(s) failed" % (len(bad), len(SUITES)))
        return 1
    print("\n✅ set_work_unit: both pure suites pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
