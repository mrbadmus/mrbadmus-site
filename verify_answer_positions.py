#!/usr/bin/env python3
"""MRB-278, made permanent and cross-key-stage: the correct answer is not
always in the same place, anywhere a student meets a fixed-position MCQ.

Why this gate exists. KS3's bank once had a skew where the correct answer
NEVER landed on one position — a student who noticed could answer a
four-option question as a three-option one. verify_ks3 gained the check for
KS3's authored corpora (MRB-278), but nothing watched KS4. This gate watches
BOTH key stages, permanently, as a fast registered gate.

⚖️ WHAT IS MEASURED IS WHAT IS SERVED, and the two key stages differ:

  · KS3 serves AUTHORED order — build_ks3.py emits ladder rungs and the
    bank exactly as written (options render in authored order, MRB-278
    ruling), so this gate measures the authored .py data.
  · KS4 serves BUILD-SHUFFLED order — the authored all_subtopics_*.py
    corpora are 100% index-0 by convention (the correct option is the
    first tuple, `wrong_explanations` keyed {1,2,3}), and
    generate_site_v5.make_new_quiz deterministically reshuffles at build
    time. Measuring the authored files would be RED at 100% forever and
    would demand pointless churn of a deliberate authoring convention; a
    student never sees that order. So for KS4 this gate measures the
    BUILT tree's `data-answer` attributes — the thing a student's
    browser actually receives.
  · KS4's ASSIGNMENT POOL (ks4_data → ks4_assignment_bank, MRB-332) is
    measured AUTHORED, like KS3 and unlike the KS4 lesson pages two
    bullets up. ⚠️ That is not a contradiction — it is the same rule
    reaching a different answer, because the rule is "measure what is
    served". Nothing shuffles this pool. `bankFor` reads it ordered by
    `bank_position` and composition takes the rows in that order, so the
    `correct_index` an author types is the position the child meets. The
    KS4 lesson pages are measured built ONLY because
    generate_site_v5.make_new_quiz reshuffles them after authoring; there
    is no such step here, and measuring the exported table instead would
    measure the same numbers a day later.
  · The 46 KS4 bonding "rd" pages shuffle at RUNTIME (shared/quiz.js,
    per-option data-correct, no data-answer at all) and are
    position-immune by construction. The gate asserts that property
    STAYS true rather than measuring them: a data-answer appearing on a
    quiz.js page means someone rebuilt them positional, which is the
    regression this line exists to catch.

Thresholds match verify_ks3's MRB-278 check exactly: within a corpus no
index may hold more than half the answers, and no index may be the answer
zero times (once the corpus is at least as big as its option count).
"""

import collections
import os
import re
import sys

FAIL = []


def check(label, ok, detail):
    print("  %s %s — %s" % ("✅" if ok else "❌", label, detail))
    if not ok:
        FAIL.append(label)


def pos_report(label, sets):
    """One corpus. `sets` is (scope, where, n_options, correct_idx)."""
    probs = []
    glob = collections.Counter()
    per = collections.defaultdict(collections.Counter)
    sizes = collections.defaultdict(set)
    for scope, _where, n, idx in sets:
        glob[idx] += 1
        per[scope][idx] += 1
        sizes[scope].add(n)
    if not sets:
        return ["%s: nothing to measure — the corpus is missing" % label], ""
    alln = sorted({n for _s, _w, n, _i in sets})
    for scope, c in ([("whole corpus", glob)]
                     + [(u, per[u]) for u in sorted(per)]):
        tot = sum(c.values())
        nopt = max(alln) if scope == "whole corpus" else max(sizes[scope])
        row = [c.get(i, 0) for i in range(nopt)]
        top = max(row)
        if top * 2 > tot:
            probs.append(
                "%s · %s: index %d holds %d of %d (%.0f%%) — more than half"
                % (label, scope, row.index(top), top, tot, 100.0 * top / tot))
        if tot >= nopt:
            zero = [i for i, v in enumerate(row) if v == 0]
            if zero:
                probs.append(
                    "%s · %s: index %s is NEVER the answer across %d set(s)"
                    % (label, scope, zero, tot))
    tot = sum(glob.values())
    row = [glob.get(i, 0) for i in range(max(alln))]
    return probs, ("%s: %d question(s), distribution %s, worst index %.0f%%"
                   % (label, tot, row, 100.0 * max(row) / tot))


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("verify_answer_positions — MRB-278 across both key stages")

    # ── KS3, authored (what build_ks3 serves verbatim) ──────────────────
    import ks3_data
    lad, bank = [], []
    for u in ks3_data.build_units():
        for l in u.get("lessons", []):
            if not l.get("authored"):
                continue
            for rung, r in (l.get("ladder") or {}).items():
                if isinstance(r, dict) and r.get("options"):
                    a = r.get("answer")
                    if isinstance(a, int) and 0 <= a < len(r["options"]):
                        lad.append((u.get("code"),
                                    "%s %s" % (l["slug"], rung),
                                    len(r["options"]), a))
    import ks3_data.question_bank as qb
    for rec in qb.load_bank():
        for q in rec["questions"]:
            ci = [i for i, o in enumerate(q["options"]) if o.get("correct")]
            if len(ci) == 1:
                bank.append((rec["unit"], q.get("id"),
                             len(q["options"]), ci[0]))
    # Per-unit scoping stays verify_ks3's job (it reports unit by unit for
    # KS3); here each KS3 corpus is measured whole, so a unit-local skew
    # that balances globally is verify_ks3's finding, not a double report.
    for label, sets in (("KS3 ladder", [("KS3", w, n, i) for _u, w, n, i in lad]),
                        ("KS3 bank", [("KS3", w, n, i) for _u, w, n, i in bank])):
        probs, line = pos_report(label, sets)
        check(label, not probs, line if not probs else "; ".join(probs))

    # ── KS4, built (what generate_site_v5's shuffle actually shipped) ───
    card = re.compile(r'class="quiz-card"[^>]*\bdata-answer="(\d+)"')
    oi = re.compile(r'\bdata-oi="\d"')
    ks4 = []
    immune_bad = []
    counted_pages = 0
    for tree in ("mrbadmus_site/combined", "mrbadmus_site/triple"):
        for root, _dirs, files in os.walk(tree):
            for fn in files:
                if not fn.endswith(".html"):
                    continue
                fp = os.path.join(root, fn)
                with open(fp, encoding="utf-8") as fh:
                    html = fh.read()
                answers = [int(m) for m in card.findall(html)]
                if "/shared/quiz.js" in html:
                    # Runtime-shuffled rd pages: position-immune, and they
                    # must stay that way.
                    if answers:
                        immune_bad.append(fp)
                    continue
                if not answers:
                    continue
                counted_pages += 1
                nopts = len(oi.findall(html))
                if nopts != 4 * len(answers):
                    check("KS4 card shape", False,
                          "%s has %d cards but %d options — the 4-option "
                          "assumption this gate makes no longer holds"
                          % (fp, len(answers), nopts))
                    continue
                scope = tree.rsplit("/", 1)[-1]
                for a in answers:
                    ks4.append((scope, fp, 4, a))
    probs, line = pos_report("KS4 built quiz cards", ks4)
    check("KS4 built quiz cards", not probs,
          ("%s, over %d page(s)" % (line, counted_pages)) if not probs
          else "; ".join(probs))
    check("KS4 rd pages stay position-immune", not immune_bad,
          "no data-answer on any quiz.js page" if not immune_bad
          else "positional cards appeared on: %s" % ", ".join(immune_bad))

    # ── KS4 assignment pool, AUTHORED (MRB-332) ─────────────────────────
    #
    # ⚠️ AUTHORED, not built — and the header explains at length why the KS4
    # lesson pages above are the other way round. Both follow the one rule:
    # measure what is SERVED. This pool has no shuffle anywhere between the
    # .py file and the child — `export_ks4_questions.py` copies
    # `correct_index` across, `bankFor` orders by `bank_position`, and
    # composition takes the rows in that order — so the index an author types
    # is the position a student meets, and the authored file is the honest
    # place to measure it.
    #
    # Scoped per SUBJECT and again per SUBTOPIC. The subtopic pass is the one
    # that matters for a student: a subtopic is twelve questions and it is the
    # unit of homework, so a skew inside one is a skew a class actually sits,
    # even when the subject as a whole averages out.
    try:
        import ks4_data
        # strict=False: the pool is authored by many hands over many days and
        # a part-written subject must still be measurable. Completeness is
        # export_ks4_questions.py's gate, not this one's.
        pool = ks4_data.load_pool(strict=False)
    except SystemExit as exc:
        # A pool that will not load is a finding, not a skip. If an author is
        # mid-save the message says so and the re-run is free.
        check("KS4 assignment pool", False,
              "ks4_data.load_pool() failed, so the pool could not be "
              "measured: %s" % str(exc).replace("\n", " "))
        pool = None
    except Exception as exc:                       # noqa: BLE001 — reported
        check("KS4 assignment pool", False,
              "ks4_data could not be loaded (%s: %s)"
              % (type(exc).__name__, exc))
        pool = None

    if pool is not None and not pool:
        # The ONLY clean skip, and it is announced. An empty corpus has no
        # distribution to measure; anything else is measured.
        print("  ⏭️  KS4 assignment pool — SKIP: no questions authored yet. "
              "One question and this measures.")
    elif pool:
        for label, key in (("KS4 assignment pool · by subject", "subject"),
                           ("KS4 assignment pool · by subtopic",
                            "subtopic_slug")):
            sets = [(r[key], r["id"], len(r["options"]), r["correct_index"])
                    for r in pool]
            probs, line = pos_report(label, sets)
            check(label, not probs, line if not probs else "; ".join(probs))

    if FAIL:
        print("❌ %d check(s) failed" % len(FAIL))
        sys.exit(1)
    print("✅ answer positions healthy in both key stages")


if __name__ == "__main__":
    main()
