#!/usr/bin/env python3
"""Can a pupil pick the key from the SHAPE of the options alone?

⚠️ Pattern-free by design. Ruled 12 Sep 2026 after the `atmosphere` examiner
found 187 distractors across 95 of 174 rows carrying a rotation of 17
boilerplate clauses that announced their own wrongness ("…, although this has
been shown not to be the case"). On **30 rows every distractor carried one and
the key carried none** — 17% of the leaf where a pupil scores by elimination
on formatting, knowing no science at all.

A clause list cannot generalise: those 17 strings are topic-neutral, so another
lane inventing its own rotation would phrase it differently and a literal sweep
would return clean. The examiner's own advice, and it is right:

    "What generalises is the SHAPE: a trailing comma-clause that comments on
     the option's truth status instead of stating science. A cheap independent
     check that needs no pattern at all: flag any row where every distractor
     ends in a subordinate clause and the key does not."

That is what this measures, and it catches the shape regardless of wording.

⚠️ It REPORTS, it does not fail. A leaf where distractors genuinely carry
their own reasons — which brief §9.2 explicitly ASKS FOR — will show hits, and
that is correct authoring, not a defect. What is damning is the ASYMMETRY:
every distractor dressed one way and the key dressed another, row after row.
Read the flagged rows; the number alone proves nothing.
"""
import argparse, collections, importlib.util, os, re, sys

# A trailing subordinate clause: a comma, then a clause of real substance.
SUBORD = re.compile(
    r",\s+(although|which|because|since|even though|rather than|while|"
    r"whereas|despite|so that|as this|a claim|a detail|a mechanism|a step|"
    r"something that|and this|but this|though)\b", re.I)

def trailing_clause(s):
    if not s or "," not in s:
        return False
    if SUBORD.search(s):
        return True
    tail = s.rsplit(",", 1)[-1].strip()
    return len(tail.split()) >= 5          # a substantial trailing clause

# ⊕ 12 Sep 2026 — THE OPENING-FRAME TEST, asked for by the B8 examiner after
# it found the worst tell of the night in its own unit. A lane had discarded
# six boilerplate filler phrases (good) and hand-redone the pass, which left
# every distractor in 43 rows opening "The claim is…" / "The argument is…"
# while the key never did: "the claim is correct" appeared 48 times in
# distractors and ZERO times in a key. A child who noticed that the option NOT
# phrased as a verdict is always right scored 43/43 knowing no science.
#
# That is the same defect as the disclaimer rotation, one level up: grammatical
# rather than lexical, so a clause list cannot see it. What it shares is the
# ASYMMETRY, and an opening frame is as visible to a pupil as a trailing one.
# ⊕ 12 Sep 2026 — THE ABSOLUTE-TAIL TEST. This file's trailing-clause check
# UNDER-REPORTED the `organisation` lane at 7.9%, because it looks for a
# subordinate CLAUSE and that lane's padding was bare adverbial tails:
# ", without any exception at all", ", in almost every situation like this",
# ", at every single stage involved". 16 phrases, 762 uses, 386 distractor
# options across 192 of 468 rows — and ZERO in any key.
#
# ⚠️ Worse than a neutral hedge: an absolute quantifier ("always", "never",
# "without exception") is the oldest test-wiseness heuristic there is, and a
# pupil taught to distrust absolutes picks the key by avoiding them. Stripping
# that padding revealed a 77.8% pick-the-longest exploit underneath, against
# 25% by chance — while the padded file's rank distribution read a textbook
# 23.9/27.4/23.5/25.2, which is why no gate saw it.
ABSOLUTE_TAIL = re.compile(
    r"(without (?:any )?exception|in every (?:single )?case|at every single|"
    r"\balways\b|\bnever\b|in all circumstances|no matter what|"
    r"under any circumstances|every single time|in almost every situation|"
    r"as would (?:generally )?be expected|quite possibly|most likely|"
    r"\bapparently\b|or so\b)", re.I)

# ⊕ 12 Sep 2026 — THE MIRROR LENGTH TELL, and the OVER-ASSERTION sweep. Both
# asked for by the C3 examiner, and both are invisible to every gate in the
# estate.
#
# ⚠️ `verify_answer_lengths` and mrb338_leafcheck §4 measure key-LONGEST ONLY.
# C3's `filtration` leaf had the key as the SHORTEST option in 51.6% of visible
# sets — more than double chance — while its key-longest read a healthy 22.9%.
# `evaporation` was 37.5% shortest against 19.8% longest. **Both leaves passed
# every gate in the estate while a pupil tapping the shortest option scored far
# above chance.** The cause is the mirror of the usual defect: distractors
# written with a trailing justification, keys left bare.
#
# The over-assertion sweep is the same story one level down. An option carrying
# "at all" / "genuinely" / "somehow" / "truly" was wrong 101 times out of 110
# across 444 new rows, and in two leaves 15/15 and 9/9 — no key EVER carried
# one. Four lanes converged on the habit independently; each lane's own share
# looked like noise, and only the unit-wide count shows it is a rule.
OVER_ASSERT = re.compile(
    r"\b(at all|genuinely|somehow|whatever|truly|secretly|after all|"
    r"actually|in fact|really)\b", re.I)

FRAME_WORDS = 3   # how many leading words count as "the same frame"

def opening_frame(s, n=FRAME_WORDS):
    w = re.findall(r"[A-Za-z']+", (s or "").lower())
    return " ".join(w[:n]) if len(w) >= n else None

# ⚠️ ⊕ 12 Sep 2026 — a file-path import is NOT enough. `ks3_data/p1/
# questions_04_heating_and_thermal_equilibrium.py` does `from ..quantities
# import …` (core quantities are defined once and imported, never retyped), and
# a standalone `spec_from_file_location` cannot resolve a relative import. The
# first version CRASHED on it and printed NOTHING — a whole-estate sweep that
# produces no output at all is worse than one that skips a file, because the
# operator sees an error rather than a silent gap and may still not know how
# many files went unmeasured. So: import via the package when the path form
# fails, and REPORT anything still unreadable rather than dropping it.
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIPPED = []

def load(p):
    try:
        spec = importlib.util.spec_from_file_location("_m", p)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        return getattr(m, "QUESTIONS", [])
    except ImportError:
        pass
    try:
        rel = os.path.relpath(os.path.abspath(p), REPO)
        dotted = rel[:-3].replace(os.sep, ".")
        if REPO not in sys.path:
            sys.path.insert(0, REPO)
        return getattr(importlib.import_module(dotted), "QUESTIONS", [])
    except Exception as exc:
        SKIPPED.append((p, "%s: %s" % (type(exc).__name__, exc)))
        return []

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--show", type=int, default=6, help="example rows to print")
    a = ap.parse_args()

    missing = [p for p in a.paths if not os.path.exists(p)]
    if missing:
        print("⚠️  %d path(s) do not exist and were NOT checked" % len(missing))
        if len(missing) == len(a.paths):
            print("❌ NOTHING was checked. In zsh use \"${(@f)FILES}\" or xargs.")
            return 2

    per = collections.Counter(); tot = collections.Counter(); shown = 0
    examples = []
    frame_hits = collections.Counter(); frame_ex = []
    abs_hits = collections.Counter(); abs_ex = []
    short_vis = collections.Counter(); short_key = collections.Counter()
    oa_wrong = collections.Counter(); oa_key = collections.Counter()
    for p in a.paths:
        if p in missing:
            continue
        for q in load(p):
            opts = q.get("options") or []
            if len(opts) != 4:
                continue
            if isinstance(opts[0], dict):
                ds = [o.get("text", "") for o in opts if not o.get("correct")]
                ks = [o.get("text", "") for o in opts if o.get("correct")]
            else:
                ci = q.get("correct_index")
                if not isinstance(ci, int) or not (0 <= ci < 4):
                    continue
                ds = [o for i, o in enumerate(opts) if i != ci]
                ks = [opts[ci]]
            if len(ds) != 3 or not ks:
                continue
            tot[p] += 1
            # mirror tell — key SHORTEST by a visible margin
            lens = sorted((len(o) for o in (ds + [ks[0]])))
            if lens[1] - lens[0] >= 6:
                short_vis[p] += 1
                if len(ks[0]) == lens[0]:
                    short_key[p] += 1
            # over-assertion — does the phrase mark a WRONG option?
            for o in ds:
                if OVER_ASSERT.search(o):
                    oa_wrong[p] += 1
            if OVER_ASSERT.search(ks[0]):
                oa_key[p] += 1
            da = [bool(ABSOLUTE_TAIL.search(d)) for d in ds]
            if all(da) and not ABSOLUTE_TAIL.search(ks[0]):
                abs_hits[p] += 1
                if len(abs_ex) < a.show:
                    abs_ex.append((q.get("id", "?"), ks[0], ds))
            frames = [opening_frame(d) for d in ds]
            kf = opening_frame(ks[0])
            framed = (frames[0] is not None and len(set(frames)) == 1
                      and frames[0] != kf)
            if framed:
                frame_hits[p] += 1
                if len(frame_ex) < a.show:
                    frame_ex.append((q.get("id", "?"), frames[0], ks[0], ds))
            if all(trailing_clause(d) for d in ds) and not trailing_clause(ks[0]):
                per[p] += 1
                if len(examples) < a.show:
                    examples.append((q.get("id", "?"), ks[0], ds))
    grand = sum(per.values()); rows = sum(tot.values())
    print("shape tell — every distractor dressed in a trailing clause, the key "
          "bare\n")
    for p in sorted(tot, key=lambda x: -per[x]):
        if per[p]:
            print("  %4d / %-4d  %5.1f%%  %s"
                  % (per[p], tot[p], 100.0 * per[p] / tot[p], p))
    print("\n  TOTAL %d / %d rows = %.1f%%" % (grand, rows,
          100.0 * grand / rows if rows else 0))
    if examples:
        print("\n  examples to READ:")
        for qid, k, ds in examples:
            print("    %s\n       key : %s" % (qid, k[:96]))
            for d in ds:
                print("       dist: %s" % d[:96])
    sv, sk = sum(short_vis.values()), sum(short_key.values())
    print("\n\nMIRROR TELL — key is the SHORTEST option (margin 6). Chance is "
          "25%; above ~35% a pupil\n              tapping the shortest option "
          "beats guessing. NO GATE WATCHES THIS.\n")
    for p in sorted(tot, key=lambda x: -(short_key[x] / short_vis[x] if short_vis[x] else 0)):
        if short_vis[p] >= 8:
            r = 100.0 * short_key[p] / short_vis[p]
            print("  %4d / %-4d  %5.1f%%  %s%s" % (short_key[p], short_vis[p], r, p,
                  "   ← ABOVE 35%" if r > 35 else ""))
    print("\n  TOTAL %d / %d = %.1f%%" % (sk, sv, 100.0 * sk / sv if sv else 0))

    ow, ok = sum(oa_wrong.values()), sum(oa_key.values())
    print("\n\nOVER-ASSERTION SWEEP — 'at all / genuinely / truly / actually' "
          "marking a WRONG option\n")
    print("  in distractors: %d   ·   in keys: %d" % (ow, ok))
    if ow + ok:
        print("  wrong %.1f%% of the time (chance is 75%% — three of four "
              "options are wrong)" % (100.0 * ow / (ow + ok)))
        print("  ⚠️  Well above 75% means the phrase MARKS the wrong options.")

    ag = sum(abs_hits.values())
    print("\n\nABSOLUTE-TAIL TELL — every distractor hedged or absolute, the "
          "key not\n")
    for p in sorted(tot, key=lambda x: -abs_hits[x]):
        if abs_hits[p]:
            print("  %4d / %-4d  %5.1f%%  %s"
                  % (abs_hits[p], tot[p], 100.0 * abs_hits[p] / tot[p], p))
    print("\n  TOTAL %d / %d rows = %.1f%%" % (ag, rows,
          100.0 * ag / rows if rows else 0))
    for qid, k, ds in abs_ex:
        print("\n    %s" % qid)
        print("       key : %s" % k[:90])
        for d in ds:
            print("       dist: %s" % d[:90])

    fg = sum(frame_hits.values())
    print("\n\nOPENING-FRAME TELL — all three distractors share their first %d "
          "words, the key does not\n" % FRAME_WORDS)
    for p in sorted(tot, key=lambda x: -frame_hits[x]):
        if frame_hits[p]:
            print("  %4d / %-4d  %5.1f%%  %s"
                  % (frame_hits[p], tot[p], 100.0 * frame_hits[p] / tot[p], p))
    print("\n  TOTAL %d / %d rows = %.1f%%" % (fg, rows,
          100.0 * fg / rows if rows else 0))
    for qid, fr, k, ds in frame_ex:
        print("\n    %s  — all three distractors open %r, the key does not"
              % (qid, fr))
        print("       key : %s" % k[:90])
        for d in ds:
            print("       dist: %s" % d[:90])

    if SKIPPED:
        print("\n⚠️  %d FILE(S) COULD NOT BE READ AND WERE NOT MEASURED:"
              % len(SKIPPED))
        for f, why in SKIPPED[:10]:
            print("      %s — %s" % (f, why[:90]))
        print("   A sweep that silently omits files is a sweep that proves "
              "nothing about them.")

    print("\n⚠️  Reported, never failed. Distractors carrying their own reasons "
          "is what brief §9.2 asks for;\n   the defect is the ASYMMETRY. Read "
          "the rows.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
