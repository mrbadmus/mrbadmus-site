#!/usr/bin/env python3
"""tools/ks4_assemble_pack.py — assemble a batch's Design input pack.

    python3 tools/ks4_assemble_pack.py batch-4

Mide's ruling, 2 Oct 2026: Design authors every KS4 lesson from batch 4 on;
Code builds her input packs. The examiners write one fragment per lesson
(`_brief/<slug>.md`, `_flags/<slug>.md`); this script joins them, in
BATCH-PLAN order, into the three files Design reads first:

    docs/ks4/packs/batch-N/00-BRIEF.md
    docs/ks4/packs/batch-N/FLAGS.md
    docs/ks4/packs/batch-N/DESIGN-BRIEF.txt

and refuses if any lesson in the plan has no fragment, or a fragment names
a lesson the plan does not. Fragments are deleted once assembled (they are
the same text twice otherwise) unless --keep.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAN = os.path.join(ROOT, "docs", "ks4", "BATCH-PLAN.md")


def plan_rows(batch):
    """[(n, slug, title, subject, topic, routes, family, rainford)] for batch."""
    n = batch.split("-")[1]
    rows, on = [], False
    for line in open(PLAN, encoding="utf-8"):
        if line.startswith("## "):
            on = line.strip() == "## Batch %s" % n
            continue
        if on and re.match(r"^\| \d+ \|", line):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            rows.append(dict(n=c[0], slug=c[1].strip("`"), title=c[2],
                             subject=c[3], topic=c[4], routes=c[6],
                             family=c[7], rainford=c[11] if len(c) > 11 else ""))
    if not rows:
        sys.exit("no rows for %s in BATCH-PLAN.md" % batch)
    return rows


def frag(d, slug):
    p = os.path.join(d, slug + ".md")
    return open(p, encoding="utf-8").read().strip() if os.path.exists(p) else None


SUPERSEDED = ("> **Raw extraction notes, written before the examination.** Where they "
              "disagree with `examination/`, `FLAGS.md` or `00-BRIEF.md` (spec "
              "references, required-practical numbers, quiz-key alignment), those "
              "win.\n\n")


def stamp_extract_notes(pack):
    """The extractor's notes repeat the frozen data's own labels (wrong RP
    numbers, the site's internal spec numbering) and its key-alignment check
    missed shifted wrong_explanations the examiners caught. Say so at the top."""
    p = os.path.join(pack, "_extract-notes.md")
    if os.path.exists(p):
        s = open(p, encoding="utf-8").read()
        if not s.startswith(SUPERSEDED[:40]):
            open(p, "w", encoding="utf-8").write(SUPERSEDED + s)


def main():
    if sys.argv[1:2] == ["--stamp-notes"]:
        for b in sys.argv[2:]:
            stamp_extract_notes(os.path.join(ROOT, "docs", "ks4", "packs", b))
        return
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    keep = "--keep" in sys.argv
    if len(args) != 1 or not re.match(r"^batch-\d+$", args[0]):
        sys.exit(__doc__)
    batch = args[0]
    pack = os.path.join(ROOT, "docs", "ks4", "packs", batch)
    rows = plan_rows(batch)
    bdir, fdir = os.path.join(pack, "_brief"), os.path.join(pack, "_flags")
    slugs = [r["slug"] for r in rows]

    missing = [s for s in slugs if frag(bdir, s) is None or frag(fdir, s) is None]
    if missing:
        sys.exit("missing fragments for: " + ", ".join(missing))
    extra = sorted(set(f[:-3] for d in (bdir, fdir) for f in os.listdir(d)
                       if f.endswith(".md")) - set(slugs))
    if extra:
        sys.exit("fragments for lessons not in the plan: " + ", ".join(extra))

    sources = sorted(os.listdir(os.path.join(pack, "04-checked-science-source")))
    src_of = {}
    for s in slugs:
        # <subject>-<spec>-<slug>.md; the spec part may be "8463-4.6.3" or
        # carry a "(physics only)" note, but never letters of a longer slug.
        hit = [f for f in sources if f.endswith("-" + s + ".md") and re.fullmatch(
            r"(biology|chemistry|physics)-[0-9.]+(-[0-9.]+)?( \([a-z ]+\))?-",
            f[:-len(s) - 3])]
        if len(hit) != 1:
            sys.exit("expected one source file for %s, found %r" % (s, hit))
        src_of[s] = hit[0]

    title = "KS4 %s — Design input pack" % batch.replace("-", " ").title()
    out = ["# " + title, "",
           "Mide's ruling, 2 Oct 2026: **Design authors and draws every KS4 "
           "lesson from batch 4 on.** Code built this pack, will port your "
           "pages, check the science and ship them, exactly as for the pilot.",
           "",
           "## Read first", "",
           "- `docs/ks4/architecture.md` — the ten laws, the families, the "
           "CFIFA amendment, and **the two amendments of 2 Oct 2026** "
           "(Design writes the lessons; the four lesson rules).",
           "- The pilot, as the bar and the template: "
           "`docs/ks4/design-reference/pilot/` (your delivery, unmodified) "
           "and the live pages it became.",
           "- This file, then `FLAGS.md` (science you must not repeat), then "
           "each lesson's `04-checked-science-source/` file, then "
           "`05-diagram-library/README.md`.",
           "",
           "## The four lesson rules (Mide, 2 Oct 2026) — apply to every "
           "lesson here", "",
           "1. **Start here is a two-option guess**, framed as a guess, "
           "answerable from everyday experience on every route; the reveal "
           "is encouraging either way and leads straight into the teaching.",
           "2. **Equations are formula triangles you can cover** — in the "
           "equation block, the equation-sheet panel and CFIFA's Formula "
           "step. A square or a ½ gets its own extra line (square-root, ×2).",
           "3. **Teach every step before you test it.** A calculation that "
           "chains two equations gets its own \"Step 1 … Step 2 …\" worked "
           "example before any pupil does one; CFIFA on each step.",
           "4. **Practice is the same size in every lesson** — same number of "
           "questions at each rung of the end practice and the exam ladder. "
           "Set the number once (at least the content-standards floor) and "
           "keep it across the batch.",
           "",
           "Each lesson below says which calculations chain, which equations "
           "need triangles, and how many verbatim quiz items are usable; the "
           "rest of each bank is yours to write to the fixed size.",
           "",
           "## Lessons", "",
           "| # | lesson | slug | subject · topic | source file |",
           "|---|---|---|---|---|"]
    for r in rows:
        out.append("| %s | %s | `%s` | %s · %s | `04-checked-science-source/%s` |"
                   % (r["n"], r["title"], r["slug"], r["subject"], r["topic"],
                      src_of[r["slug"]]))
    out += ["", "True routes, layers and families are in each lesson's entry "
            "below; they come from the AQA specification's own labels, "
            "checked by an examiner, and where they differ from what the site "
            "ships today the entry says so.", "", "## Per lesson", ""]
    for r in rows:
        out += [frag(bdir, r["slug"]), "", "---", ""]
    open(os.path.join(pack, "00-BRIEF.md"), "w", encoding="utf-8").write(
        "\n".join(out).rstrip("-\n ") + "\n")

    fl = ["# %s — science flags" % batch.replace("-", " ").title(), "",
          "Numbered per lesson. **WRONG** items are frozen text kept verbatim in "
          "the source files that must not be used as written. Each flag says "
          "what to do instead.", ""]
    for r in rows:
        fl += ["## %s. %s (`%s`)" % (r["n"], r["title"], r["slug"]), "",
               frag(fdir, r["slug"]), ""]
    open(os.path.join(pack, "FLAGS.md"), "w", encoding="utf-8").write(
        "\n".join(fl).rstrip() + "\n")

    n = batch.split("-")[1]
    db = ["KS4 batch %s — %d lessons." % (n, len(rows)), "",
          "Pack: docs/ks4/packs/%s/ in the mrbadmus-site repo (main branch)." % batch,
          "Read 00-BRIEF.md first, then FLAGS.md, then each lesson's file in "
          "04-checked-science-source/, then 05-diagram-library/README.md.", "",
          "Lessons:"]
    for r in rows:
        db.append("  %s. %s (%s)" % (r["n"], r["title"], r["slug"]))
    db += ["", "Deliver one runnable .dc.html per lesson, as for the pilot, "
           "with NOTES (numbered science flags), README, _ds and support.js."]
    open(os.path.join(pack, "DESIGN-BRIEF.txt"), "w", encoding="utf-8").write(
        "\n".join(db) + "\n")

    stamp_extract_notes(pack)

    if not keep:
        for d in (bdir, fdir):
            for f in os.listdir(d):
                os.remove(os.path.join(d, f))
            os.rmdir(d)
    print("assembled %s: %d lessons -> 00-BRIEF.md, FLAGS.md, DESIGN-BRIEF.txt"
          % (batch, len(rows)))


if __name__ == "__main__":
    main()
