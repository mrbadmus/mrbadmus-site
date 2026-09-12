#!/usr/bin/env python3
"""Does the KEY agree with the arithmetic its own `why` sets out?

⚠️ NOTHING ELSE IN THE ESTATE ASKS THIS. `ks4_pool_check` checks that
`correct_index` is IN RANGE; `question_bank` checks that exactly one option
carries `correct: True` and that the key has no `why`. Neither asks whether
the key is TRUE — REPORT §6 says so in as many words, and night 1's near-miss
was exactly this shape.

It became urgent on 12 Sep 2026: one lane, asked to resolve a placeholder
`correct_index`, found that EIGHT further rows in its own batch carried a
`correct_index` pointing at an option the row's own `why` contradicted. A
shipped row of that shape is the worst defect this programme can produce — a
question whose marked answer is wrong — and it passes every gate.

THE RULE, and it is deliberately narrow so it can be trusted:
  If the key option carries a number, the number the `why` works out to
  should BE that number. So every numeric token in the key must appear
  somewhere in the `why`. If it does not, the key and its own working
  disagree, and a human must read the row.

  ⚠️ It REPORTS, it does not fail the build. A key of "0.50 kg" whose `why`
  says "half a kilogram" is fine and would be flagged; only a human can tell
  those apart. Precision over recall would be the wrong trade here — a missed
  wrong key reaches a child.
"""
import argparse, importlib.util, os, re, subprocess, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 18 000 → 18000 ; 1,200 → 1200 ; strips a trailing unit, keeps the number.
_NUM = re.compile(r"\d[\d\s,]*\.?\d*")

def nums(s):
    out = set()
    for m in _NUM.finditer(s or ""):
        t = m.group(0).replace(" ", "").replace(",", "").rstrip(".")
        if not t:
            continue
        try:
            v = float(t)
        except ValueError:
            continue
        out.add(v)
        if v == int(v):
            out.add(float(int(v)))
    return out

def load(path):
    spec = importlib.util.spec_from_file_location("_m", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)          # exec, not ast.parse — see __doc__
    return getattr(mod, "QUESTIONS", [])

def new_ids(paths, base):
    """Ids that do NOT exist in `base` — tonight's rows only."""
    seen = set()
    for p in paths:
        try:
            old = subprocess.run(["git", "show", "%s:%s" % (base, p)],
                                 cwd=REPO, capture_output=True, text=True)
            if old.returncode == 0:
                seen |= set(re.findall(r'"id":\s*"([^"]+)"', old.stdout))
        except Exception:
            pass
    return seen

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+", help="question files to check")
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--all", action="store_true",
                    help="check every row, not only rows new since --base")
    a = ap.parse_args()

    rel = [os.path.relpath(os.path.abspath(p), REPO) for p in a.paths]
    old_ids = set() if a.all else new_ids(rel, a.base)

    checked = flagged = skipped = 0
    # ⚠️ A PATH THAT DOES NOT EXIST IS REPORTED, NEVER SKIPPED IN SILENCE.
    # 12 Sep 2026: this file's first multi-file run printed "0 rows checked"
    # and exited 0. The shell was zsh, where an unquoted $FILES does NOT
    # word-split, so all 31 paths arrived as ONE argument naming no file —
    # and the loop's `continue` turned that into a clean bill of health.
    # A gate that measures nothing must never look like a gate that found
    # nothing. Pass files with `"${(@f)FILES}"` in zsh, or via xargs.
    missing = [p for p in rel if not os.path.exists(os.path.join(REPO, p))]
    if missing:
        print("⚠️  %d path(s) do not exist and were NOT checked:" % len(missing))
        for p in missing[:5]:
            print("      %s" % p[:120])
        if len(rel) == len(missing):
            print("\n❌ key-arithmetic: NOTHING was checked — every path given "
                  "is missing.\n   In zsh use \"${(@f)FILES}\" or xargs; an "
                  "unquoted $FILES is a single word.")
            return 2
    for p in rel:
        full = os.path.join(REPO, p)
        if not os.path.exists(full):
            continue
        for q in load(full):
            qid = q.get("id", "?")
            if qid in old_ids:
                continue
            # KS4 shape (plain strings + correct_index) and KS3 shape (dicts).
            opts, why = q.get("options") or [], q.get("why")
            if opts and isinstance(opts[0], dict):
                keys = [o for o in opts if o.get("correct")]
                if len(keys) != 1:
                    continue
                key_text = keys[0].get("text", "")
                why = " ".join(o.get("why", "") for o in opts
                               if not o.get("correct"))
            else:
                ci = q.get("correct_index")
                if not isinstance(ci, int) or not (0 <= ci < len(opts)):
                    continue
                key_text = opts[ci]
            kn, wn = nums(key_text), nums(why or "")
            if not kn or not wn:
                skipped += 1
                continue
            checked += 1
            missing = kn - wn
            if missing:
                flagged += 1
                print("  ⚠️  %s" % qid)
                print("      key : %s" % key_text[:100])
                print("      why : %s" % (why or "")[:160])
                print("      the key's %s appears nowhere in the working"
                      % ", ".join(("%g" % m) for m in sorted(missing)))
    print("\nkey-arithmetic: %d numeric row(s) checked, %d to READ, "
          "%d skipped (no number in key or working)" % (checked, flagged, skipped))
    print("⚠️  Reported, never failed — a human decides. See the module docstring.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
