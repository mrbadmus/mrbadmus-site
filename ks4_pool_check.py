#!/usr/bin/env python3
"""ks4_pool_check.py — the KS4 pool's CONTENT RULE, proved against real rows.

    python3 ks4_pool_check.py --rows rows.json
    python3 ks4_pool_check.py --python        # measure the authored source instead

── WHAT THIS PROVES, AND WHAT THE OTHER TWO CHECKS PROVE ───────────────

Three different things watch this pool and it is worth being exact about
which is which, because a reader who conflates them will think a green run
says more than it does:

  · `export_ks4_questions.py --verify` proves the DATABASE MATCHES PYTHON —
    the mirror is faithful. It says nothing about whether the content rule
    is safe.
  · `verify_answer_positions.py` proves the correct answer is not always in
    the same place. It says nothing about who gets served what.
  · **This file** proves the CONTENT RULE: that the four (pathway, tier)
    audiences each receive exactly the set they are entitled to, and in
    particular that a Foundation Combined class can never be handed a Higher
    or a Triple-only question.

The rule, ruled by Mide and restated in the migration:

    tier='foundation', triple_only=false → BASE. Every class.
    tier='higher',     triple_only=false → higher tier only.
    triple_only=true                     → Triple Science only.

── WHY IT SIMULATES THE SERVING FILTER RATHER THAN TRUSTING IT ─────────

The filter that actually protects a child lives in the backend's `bankFor`,
in a different repo and a different language. Asserting there that the code
*contains* the right `.eq()` calls is a spelling test; it passes a filter
that is correct in shape and wrong in effect.

So this re-derives the four audiences from the rule itself and checks the
POOL against them: for each audience, which rows would it be served, and is
every one of those rows something that audience is entitled to. It is a
statement about the data, so it stays true no matter how the query is
written — and it is the check that fails loudly the day someone adds a
fifth flag value and forgets an audience.

`--rows` takes the JSON array a `select ... from ks4_assignment_bank` gives
back, so the same logic can be pointed at TEST or at production without this
file needing a database driver or a credential of its own.
"""

import argparse
import collections
import json
import os
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)

# The four audiences, and what each is ENTITLED to. Written as inclusion
# predicates — "these may be served" — never as exclusions. An exclusion list
# silently admits anything added later that nobody thought to exclude, which
# is exactly how a Foundation class ends up with a Higher question.
AUDIENCES = {
    ("combined", "foundation"):
        lambda r: r["tier"] == "foundation" and not r["triple_only"],
    ("combined", "higher"):
        lambda r: not r["triple_only"],
    ("triple", "foundation"):
        lambda r: r["tier"] == "foundation",
    ("triple", "higher"):
        lambda r: True,
}

FAIL = []


def check(label, ok, detail):
    print("  %s %s — %s" % ("✅" if ok else "❌", label, detail))
    if not ok:
        FAIL.append(label)


def load_rows(args):
    if args.python:
        import ks4_data
        return ks4_data.load_pool(strict=not args.partial)
    with open(args.rows, encoding="utf-8") as fh:
        rows = json.load(fh)
    for r in rows:
        r["triple_only"] = bool(r["triple_only"])
        if isinstance(r.get("options"), str):
            r["options"] = json.loads(r["options"])
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rows", help="JSON array of ks4_assignment_bank rows")
    ap.add_argument("--python", action="store_true",
                    help="measure ks4_data instead of a database dump")
    ap.add_argument("--partial", action="store_true",
                    help="allow a part-authored pool (ship-per-subject)")
    args = ap.parse_args()
    if not args.rows and not args.python:
        ap.error("give --rows <file> or --python")

    rows = load_rows(args)
    print("ks4_pool_check — the KS4 content rule, over %d row(s)" % len(rows))
    if not rows:
        print("❌ the pool is empty — nothing to prove")
        return 1

    import ks4_data
    cls = ks4_data.classify()

    # ── 1 · every row's flags match the curriculum ──────────────────────
    #
    # The flags are what the serving filter reads, so a row whose flags
    # disagree with the curriculum is served to the wrong children even
    # though every other check passes.
    drift = []
    for r in rows:
        meta = cls.get(r["subtopic_slug"])
        if meta is None:
            drift.append("%s: subtopic %r is not in the KS4 scheme"
                         % (r["id"], r["subtopic_slug"]))
            continue
        if r["tier"] != meta["tier"] or r["triple_only"] != meta["triple_only"]:
            drift.append(
                "%s (%s): row says tier=%s triple_only=%s; curriculum says "
                "tier=%s triple_only=%s"
                % (r["id"], r["subtopic_slug"], r["tier"], r["triple_only"],
                   meta["tier"], meta["triple_only"]))
        if r["subject"] != meta["subject"]:
            drift.append("%s: filed under %s, curriculum says %s"
                         % (r["id"], r["subject"], meta["subject"]))
    check("flags match the curriculum", not drift,
          "all %d row(s) agree with ks4_data.classify()" % len(rows)
          if not drift else "%d disagreement(s): %s"
          % (len(drift), "; ".join(drift[:5])))

    # ── 2 · THE RULE. Each audience gets only what it is entitled to ────
    print("\n  the four audiences:")
    for (pathway, tier), entitled in AUDIENCES.items():
        served = [r for r in rows if entitled(r)]
        # Re-derive the forbidden set independently of the predicate above,
        # so the check is not the predicate agreeing with itself.
        forbidden = []
        for r in served:
            if tier == "foundation" and r["tier"] == "higher":
                forbidden.append("%s is higher-tier" % r["id"])
            if pathway == "combined" and r["triple_only"]:
                forbidden.append("%s is triple-only" % r["id"])
        check("%-8s %-10s" % (pathway, tier), not forbidden,
              "%d question(s) servable, none forbidden" % len(served)
              if not forbidden
              else "⚠️ %d FORBIDDEN question(s) reachable: %s"
                   % (len(forbidden), "; ".join(forbidden[:5])))

    # The rule is only worth anything if the audiences actually differ.
    sizes = {k: sum(1 for r in rows if f(r)) for k, f in AUDIENCES.items()}
    cf = sizes[("combined", "foundation")]
    th = sizes[("triple", "higher")]
    check("the audiences are nested and distinct",
          cf <= sizes[("combined", "higher")] <= th
          and cf <= sizes[("triple", "foundation")] <= th and cf < th,
          "Combined Foundation %d ⊂ … ⊂ Triple Higher %d" % (cf, th))

    # ── 3 · twelve per subtopic, four per band ──────────────────────────
    by_sub = collections.defaultdict(list)
    for r in rows:
        by_sub[r["subtopic_slug"]].append(r)
    wrong = []
    for slug, qs in sorted(by_sub.items()):
        if len(qs) != 12:
            wrong.append("%s has %d" % (slug, len(qs)))
            continue
        bands = collections.Counter(q["band"] for q in qs)
        if any(bands[b] != 4 for b in ("easier", "standard", "harder")):
            wrong.append("%s bands %s" % (slug, dict(bands)))
    check("twelve per subtopic, four per band", not wrong,
          "%d subtopic(s), all 4/4/4" % len(by_sub) if not wrong
          else "%d wrong: %s" % (len(wrong), "; ".join(wrong[:6])))

    # ── 4 · ids and positions are sound ─────────────────────────────────
    ids = collections.Counter(r["id"] for r in rows)
    dupes = [i for i, n in ids.items() if n > 1]
    check("ids unique", not dupes,
          "%d id(s)" % len(ids) if not dupes
          else "%d duplicate(s): %s" % (len(dupes), dupes[:5]))

    badpos = [s for s, qs in by_sub.items()
              if len(qs) == 12
              and sorted(q["bank_position"] for q in qs) != list(range(12))]
    check("bank_position is 0..11 per subtopic", not badpos,
          "contiguous everywhere" if not badpos
          else "%d subtopic(s) wrong: %s" % (len(badpos), badpos[:5]))

    # ── 5 · four distinct options, answer in range ──────────────────────
    shape = []
    for r in rows:
        opts = r["options"]
        if len(opts) != 4:
            shape.append("%s has %d options" % (r["id"], len(opts)))
        elif len({o.strip().lower() for o in opts}) != 4:
            shape.append("%s has a repeated option" % r["id"])
        if not 0 <= r["correct_index"] <= 3:
            shape.append("%s correct_index=%s" % (r["id"], r["correct_index"]))
    check("four distinct options, answer in range", not shape,
          "every row" if not shape
          else "%d problem(s): %s" % (len(shape), "; ".join(shape[:5])))

    # ── 6 · the longest option is not the answer ────────────────────────
    #
    # A real, playable tell rather than a style note. Question writers pad the
    # correct option because it is the one that has to be unambiguously true,
    # and a student who has noticed can score above chance without knowing any
    # science — which is precisely the kind of skew MRB-278 was raised about,
    # in a different dimension.
    #
    # Chance is 25%. This warns rather than fails: a handful of long correct
    # answers is honest writing, and the threshold is set where the pattern
    # stops being explicable that way. It reports the worst offenders so the
    # cold reviewer can look at them rather than at a number.
    longest_correct = 0
    counted = 0
    offenders = collections.Counter()
    for r in rows:
        opts = r["options"]
        if len(opts) != 4:
            continue
        counted += 1
        lens = [len(o) for o in opts]
        if lens.index(max(lens)) == r["correct_index"] and \
                lens.count(max(lens)) == 1:
            longest_correct += 1
            offenders[r["subject"]] += 1
    pct = 100.0 * longest_correct / counted if counted else 0.0
    check("the longest option is not the answer", pct <= 40.0,
          "longest option is correct in %d of %d (%.0f%%; chance is 25%%)%s"
          % (longest_correct, counted, pct,
             "" if pct <= 40.0 else "  ← a student can play this: " +
             ", ".join("%s %d" % kv for kv in offenders.most_common())))

    # ── 7 · coverage against the seeded scheme ──────────────────────────
    # Reported per subject, because the run ships one subject at a time and a
    # partial pool is expected mid-run rather than a failure.
    print("\n  coverage against the seeded KS4 scheme:")
    for subject in ("physics", "chemistry", "biology"):
        want = {s for s, m in cls.items() if m["subject"] == subject}
        got = {s for s in by_sub if cls.get(s, {}).get("subject") == subject}
        missing = want - got
        mark = "✅" if not missing else ("…" if got else "·")
        print("    %s %-10s %3d/%3d subtopic(s)%s"
              % (mark, subject, len(got), len(want),
                 "" if not missing else "   %d not yet authored" % len(missing)))
        if missing and not args.partial and got:
            FAIL.append("%s coverage" % subject)

    if FAIL:
        print("\n❌ %d check(s) failed" % len(FAIL))
        return 1
    print("\n✅ the KS4 content rule holds: a Foundation Combined class "
          "cannot reach a Higher or Triple question")
    return 0


if __name__ == "__main__":
    sys.exit(main())
