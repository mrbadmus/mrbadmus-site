"""gate_watches_check.py — MRB-346. Every gate's `watches` list is honest.

    python3 gate_watches_check.py

`prepush_gate.py` binds a slow gate's receipt to the content of the files
its `watches` names, and selects which gates a branch even needs to run by
the same list. Both of those depend entirely on `watches` being TRUE — a
list that's too narrow lets a real change go undetected (the receipt stays
valid, or the gate never gets selected, even though the gate's actual
behaviour would have changed), which is the exact defect `gate_registry.py`
exists to prevent, one level further down.

This can't prove a `watches` list is COMPLETE — that still needs a human
who has read the gate's script. What it can prove, for every gate,
mechanically, on every push:

  1. `watches` is not empty. An empty list can never be selected and its
     receipt, once written, would never invalidate — a permanently green
     gate that has stopped watching anything.
  2. The gate's own script IS inside its `watches`. A gate that doesn't
     watch its own code is a gate a change to itself can't select.
  3. NOTHING any gate watches matches `docs/**`, `**/*.md`, or `README*` —
     checked both by pattern text (so a pattern that's obviously docs-shaped
     is refused outright) and empirically, against this repo's own
     `README.md`, which must never match any gate's `watches`.

⚠️ A gate whose real source-of-truth genuinely lives under `docs/` (Design's
`.dc.html` deliveries, a hand-maintained register) cannot close rule 3 and
still be honest about rule 1 in the strongest sense — its `watches` will be
narrower than its true dependency. That is a NAMED, ACCEPTED gap (see
`docs/mrb346/REPORT.md`), not something this script tries to paper over by
bending the rule. It still enforces rule 1 (non-empty) and rule 2 (own
script) for those gates, because both are always achievable.
"""

import os
import sys

import gate_registry as g

SENTINEL_NON_TRIGGER = "README.md"


def _looks_docs_shaped(pattern):
    """A crude, deliberately generous text check — catches a pattern that is
    obviously docs/md/README-shaped even before it's matched against any
    real file. The empirical check below (matching `README.md` itself)
    catches the sneakier cases this text scan would miss (e.g. a bare `**`).
    """
    p = pattern.lower()
    if p == "docs" or p.startswith("docs/") or p.startswith("docs**"):
        return True
    if p.endswith(".md") or p.endswith(".markdown"):
        return True
    base = os.path.basename(p.rstrip("*"))
    if "readme" in base:
        return True
    return False


def check():
    problems = []
    for gate in g.GATES:
        watches = gate.get("watches")
        if not watches:
            problems.append(
                "%s has no (or an empty) `watches` — it could never be "
                "selected and its receipt would never invalidate."
                % gate["name"])
            continue

        for pat in watches:
            if _looks_docs_shaped(pat):
                problems.append(
                    "%s watches %r, which is docs/md/README-shaped — "
                    "rule 3 (MRB-346) bans this unconditionally."
                    % (gate["name"], pat))

        if g.matches_any(SENTINEL_NON_TRIGGER, watches):
            problems.append(
                "%s's `watches` matches %r — no gate may ever be selected "
                "by a change to a docs/README file."
                % (gate["name"], SENTINEL_NON_TRIGGER))

        script = g.own_script(gate)
        if script is None:
            problems.append(
                "%s's `cmd` names no .py file to check as its own script."
                % gate["name"])
            continue
        if not os.path.isfile(script):
            problems.append(
                "%s's own script %r does not exist." % (gate["name"], script))
            continue
        if not g.matches_any(script, watches):
            problems.append(
                "%s does not watch its own script (%r) — a change to the "
                "gate's own code would not select it."
                % (gate["name"], script))

    return problems


def main():
    problems = check()
    if problems:
        print("❌ gate_watches_check: %d problem(s)\n" % len(problems))
        for p in problems:
            print("   · %s" % p)
        print()
        return 1
    print("✅ gate_watches_check: %d gate(s) — each watches its own "
          "script, and none watch anything under docs/**, *.md, or README*."
          % len(g.GATES))
    return 0


if __name__ == "__main__":
    sys.exit(main())
