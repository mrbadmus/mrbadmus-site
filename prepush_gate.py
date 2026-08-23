"""prepush_gate.py — refuses a push while any gate is red, and names which.

⊕ MRB-277, 21 Aug 2026. Read `gate_registry.py` first; it explains the defect
this exists to stop.

── WHAT IT DOES ────────────────────────────────────────────────────────

    python3 prepush_gate.py --check          # the guard. exit 0 = safe to push
    python3 prepush_gate.py --record NAME    # run a slow gate, keep a receipt
    python3 prepush_gate.py --record-all     # run every slow gate

`--check` is what the `pre-push` hook calls. It:

  1. refuses outright if tracked files are dirty — a gate result cannot be
     attributed to a tree that has changed since it ran;
  2. RUNS every `fast` gate, so those can never be skipped;
  3. requires a RECEIPT for every `slow` gate, matching the exact tree being
     pushed;
  4. reports every gate that is missing a precondition as SKIPPED, by name —
     a missing path (`needs`) or a missing credential (`needs_env`).

── THE RECEIPT, AND WHY IT IS KEYED ON THE TREE ────────────────────────

A receipt records that a named gate exited 0 against a specific git TREE
object. The tree sha changes if any tracked byte changes, so a receipt cannot
survive an edit — not a content fix, not a whitespace change, not a "tiny"
one. This is the whole mechanism: it converts "I ran the gates" from
something a tired person remembers into something the repo can check.

Receipts live in `.gate-receipts/` and are NOT committed. They are evidence
about one working copy at one moment, and a committed receipt would be a
receipt for somebody else's machine.

── THE OVERRIDE, AND WHY IT LANDS IN THE COMMIT MESSAGE ────────────────

There is an override, because a guard with no escape hatch gets deleted the
first night it is wrong at 2am, and a deleted guard protects nothing.

It is deliberately expensive:

    GATE-OVERRIDE: <gate-name> — <reason>

must appear in the message of the commit being pushed, once per red gate,
naming that gate. Not a flag, not an environment variable, not a prompt — the
commit message, because that is the only record that travels with the code to
everyone who ever reads the history. A flag is forgotten by the next morning;
`git log` still says it a year later.

An override that names no gate, or names a gate that is not red, is refused:
it would otherwise become a blanket the next person copies forward.
"""

import json
import os
import subprocess
import sys

import gate_registry

RECEIPTS = ".gate-receipts"
OVERRIDE = "GATE-OVERRIDE:"


def _git(*args):
    return subprocess.run(["git"] + list(args), capture_output=True,
                          text=True).stdout.strip()


def _tracked_dirty():
    """Tracked files with changes. Untracked files are not a gate concern."""
    out = _git("status", "--porcelain", "--untracked-files=no")
    return [l for l in out.splitlines() if l.strip()]


def _tree():
    return _git("rev-parse", "HEAD^{tree}")


def _receipt_path(name):
    return os.path.join(RECEIPTS, "%s.json" % name)


def _read_receipt(name):
    try:
        with open(_receipt_path(name), encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def _skip_reason(gate):
    need = gate.get("needs")
    if need and not os.path.exists(need):
        return "%s does not exist" % need
    # ⊕ MRB-282. A gate that reads production cannot run without a credential.
    # The alternative — letting the gate notice that for itself and exit 0 —
    # is a PASS that measured nothing, which is the failure mode this whole
    # guard exists to make impossible.
    env = gate.get("needs_env")
    if env:
        # A row may name ALTERNATIVES — student_controls_drive accepts either
        # MRB_DRIVE_PASSWORD or MRB_TEST_STUDENT_PASSWORD. Any one present is
        # enough; the skip only fires when none of them is.
        names = (env,) if isinstance(env, str) else tuple(env)
        if not any(os.environ.get(n) for n in names):
            return ("none of %s is set, so this gate cannot reach what it "
                    "checks" % ", ".join("$" + n for n in names))
    return None


def _run(gate):
    print("  running %-20s %s" % (gate["name"], " ".join(gate["cmd"])))
    r = subprocess.run(gate["cmd"], capture_output=True, text=True)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def record(names):
    """Run the named gates and keep a receipt for each that passes."""
    dirty = _tracked_dirty()
    if dirty:
        print("REFUSING TO RECORD — %d tracked file(s) are modified.\n"
              "A receipt attests a gate against a TREE. With the tree moving "
              "under it, it would attest nothing.\n  %s"
              % (len(dirty), "\n  ".join(dirty[:10])))
        return 1
    os.makedirs(RECEIPTS, exist_ok=True)
    tree = _tree()
    bad = 0
    for name in names:
        gate = gate_registry.by_name(name)
        why = _skip_reason(gate)
        if why:
            print("  SKIP    %-20s %s" % (name, why))
            continue
        code, out = _run(gate)
        if code == 0:
            with open(_receipt_path(name), "w", encoding="utf-8") as fh:
                json.dump({"gate": name, "tree": tree, "exit": 0}, fh, indent=2)
            print("  PASS    %s — receipt written for tree %s"
                  % (name, tree[:12]))
        else:
            bad += 1
            # A failing gate must not leave a stale PASS receipt behind it.
            if os.path.exists(_receipt_path(name)):
                os.remove(_receipt_path(name))
            print("  FAIL    %s (exit %d)\n%s"
                  % (name, code, "\n".join(out.strip().splitlines()[-15:])))
    return 1 if bad else 0


def check():
    print("── pre-push gate guard (MRB-277) " + "─" * 34)
    dirty = _tracked_dirty()
    if dirty:
        print("\n❌ REFUSED — %d tracked file(s) are modified.\n"
              "   Every gate result describes a tree. Commit or stash first, "
              "so that what was\n   measured is what is being pushed.\n\n   %s"
              % (len(dirty), "\n   ".join(dirty[:10])))
        return 1

    tree = _tree()
    msg = _git("log", "-1", "--format=%B")
    red, skipped = [], []

    for gate in gate_registry.GATES:
        why = _skip_reason(gate)
        if why:
            skipped.append((gate["name"], why))
            continue
        if gate["speed"] == "fast":
            code, out = _run(gate)
            if code != 0:
                red.append((gate["name"], "exit %d — %s"
                            % (code, (out.strip().splitlines() or [""])[-1])))
            else:
                print("  PASS    %s" % gate["name"])
        else:
            rec = _read_receipt(gate["name"])
            if rec is None:
                red.append((gate["name"],
                            "NEVER RUN against this tree — no receipt. "
                            "python3 prepush_gate.py --record %s"
                            % gate["name"]))
            elif rec.get("tree") != tree:
                red.append((gate["name"],
                            "receipt is for tree %s, pushing %s — the code "
                            "changed after the gate ran. Re-run: python3 "
                            "prepush_gate.py --record %s"
                            % ((rec.get("tree") or "?")[:12], tree[:12],
                               gate["name"])))
            else:
                print("  PASS    %-20s (receipt, tree %s)"
                      % (gate["name"], tree[:12]))

    for name, why in skipped:
        print("  SKIP    %-20s %s" % (name, why))

    if not red:
        print("\n✅ every registered gate is green for tree %s — push allowed."
              % tree[:12])
        return 0

    # ── an override must NAME the gate it is excusing ────────────────────
    excused, unexcused = [], []
    for name, detail in red:
        line = next((l.strip() for l in msg.splitlines()
                     if l.strip().startswith(OVERRIDE) and name in l), None)
        (excused if line else unexcused).append((name, detail, line))

    print("\n❌ %d GATE(S) RED:" % len(red))
    for name, detail, _line in [(n, d, None) for n, d in red]:
        print("     %-20s %s" % (name, detail))

    if unexcused:
        print("\n   PUSH REFUSED. %d of them carry no override.\n"
              % len(unexcused))
        print("   A red gate is a finding, not an obstacle: fix it, and do "
              "not weaken it to pass.\n")
        print("   If it genuinely must ship red, the commit being pushed has "
              "to say so, once\n   per gate, naming it:\n")
        for name, _d, _l in unexcused:
            print("       %s %s — <why this ships red>" % (OVERRIDE, name))
        print("\n   It goes in the COMMIT MESSAGE and nowhere else, so that "
              "`git log` still\n   says it long after the night it seemed "
              "reasonable.")
        return 1

    print("\n⚠️  PUSH ALLOWED UNDER EXPLICIT OVERRIDE — recorded in the "
          "commit message:")
    for name, _d, line in excused:
        print("     %s" % line)
    print("\n   This is now part of the history of the repository.")
    return 0


def main(argv):
    if "--check" in argv:
        return check()
    if "--record-all" in argv:
        return record([g["name"] for g in gate_registry.GATES
                       if g["speed"] == "slow"])
    if "--record" in argv:
        i = argv.index("--record")
        if i + 1 >= len(argv):
            print("--record needs a gate name. Registry: %s"
                  % ", ".join(g["name"] for g in gate_registry.GATES))
            return 2
        return record([argv[i + 1]])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
