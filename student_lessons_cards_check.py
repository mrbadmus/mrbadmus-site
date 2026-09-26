#!/usr/bin/env python3
"""student_lessons_cards_check.py — MRB-336 N2. "Lessons in this topic" cards
resolve a KS4 slug's href, not just a KS3 one.

    python3 student_lessons_cards_check.py

⚠️ THIS IS A TEXT ASSERTION, NOT A BEHAVIOUR DRIVE. The defect it guards
lives inside `lessonDefs`' build in `buildClass()` (`shared/student-live.js`),
which runs only against a REAL Supabase-backed class — `student_behaviour.py`
drives `student/class-fixture.html`, whose data is Design's own static
`window.__MRB_DATA__` (`shared/student-fixture-class.js`); its `lessonDefs`
entries carry no `href` field at all, KS3 or KS4, so the fixture cannot tell
a working KS4 link from a broken one and never has. Standing up a real,
DB-backed KS4 class fixture (a second `classes` row with `science_pathway`/
`tier`, a `ks4_assignment_bank`-shaped `source_ref`, real `assignment_questions`
rows) is the shape `mrb348_student_equiv.py` uses for exactly this reason —
a real sign-in against TEST — and is a materially bigger, riskier change than
this one wiring fix earns on its own; see the file's own docstring for the
precedent. So this checks the one thing a text read CAN prove: the resolution
this fix depends on is actually in the shipped file, and the defect it
replaces is not still there under another name.

WHAT IT CHECKS, all against `shared/student-live.js`:

  1. The old unconditional `href: lessonHref(slug)` line inside the
     `lessonDefs` build is GONE — `lessonHref` only ever reads
     `window.MRB_KS3_LESSONS`, so that line was the whole defect
     (student_rulings.py's 8 Sep 2026 note: "EVERY KS4 CLASS TAKES THAT
     BRANCH... on a KS4 pupil's page all four lesson cards have no href").
  2. `href: resolvedHref(slug)` (or equivalent) IS the line that replaced it,
     inside the same `lessonDefs.push({...})` call.
  3. The resolver reads `lessonsFor[currentId]` — the SAME per-assignment
     list the `assignmentQuestions` loop already builds with
     `ks4TopicHref(ks4Slug, subjectForAssignment[...], klass.science_pathway,
     klass.tier)` — so a KS4 card's href is the class's own pathway/tier, not
     a guess.
  4. The resolver still falls back to `lessonHref(slug)` for a slug with no
     entry in that list — the auto-composed KS3 path, whose
     `current.questions[].lesson_slug` never goes through `lessonsFor`.
  5. `ks4TopicHref` and `lessonHref` are both still defined (the fix reuses
     them, it does not reimplement either).

A change that keeps all five true cannot have reintroduced the bare
`lessonHref(slug)` regression; a change that breaks one of them has moved the
wiring in a way this check cannot vouch for, and needs a human read (or the
real drive above) before it ships.
"""

import re
import sys

PATH = "shared/student-live.js"


def check():
    problems = []
    with open(PATH, "r", encoding="utf-8") as f:
        src = f.read()

    # 1 & 2 — find the lessonDefs.push({...}) block and inspect its own
    # `href:` line, not just search the whole file (an unrelated `lessonHref`
    # call elsewhere, e.g. the auto-composed fallback inside the resolver
    # itself, must not satisfy or fail this by accident).
    m = re.search(r"lessonDefs\.push\(\{(.*?)\}\);", src, re.DOTALL)
    if not m:
        problems.append("could not find the `lessonDefs.push({...})` block "
                         "at all — has it been renamed or restructured?")
        return problems
    block = m.group(1)

    href_lines = [ln.strip() for ln in block.splitlines()
                  if re.match(r"^\s*href\s*:", ln)]
    if len(href_lines) != 1:
        problems.append("expected exactly one `href:` line inside "
                         "`lessonDefs.push({...})`, found %d: %r"
                         % (len(href_lines), href_lines))
    else:
        href_line = href_lines[0]
        if re.match(r"^href\s*:\s*lessonHref\(slug\)\s*,?$", href_line):
            problems.append("`lessonDefs.push({...})` still reads "
                             "`href: lessonHref(slug)` directly — this is "
                             "the MRB-336 N2 regression: `lessonHref` only "
                             "ever resolves KS3, so every KS4 card's href "
                             "is empty and the card stays inert.")
        elif "resolvedHref(slug)" not in href_line and \
                "lessonHref(slug)" not in href_line:
            problems.append("`lessonDefs.push({...})`'s `href:` line is "
                             "%r — neither the fixed form "
                             "(`resolvedHref(slug)`) nor the old bare form "
                             "was recognised; read it by hand." % href_line)

    # 3 — the resolver (whatever it is named) reads `lessonsFor[currentId]`.
    if "lessonsFor[currentId]" not in src:
        problems.append("no read of `lessonsFor[currentId]` found — the fix "
                         "is supposed to reuse the per-assignment list the "
                         "`assignmentQuestions` loop already resolved with "
                         "`ks4TopicHref`, not re-derive it.")

    # 4 — the fallback to lessonHref(slug) still exists somewhere (the
    # resolver's own body, for slugs `lessonsFor` has no entry for).
    if src.count("lessonHref(slug)") < 1:
        problems.append("no remaining call to `lessonHref(slug)` at all — "
                         "the KS3 auto-composed fallback path (whose "
                         "`current.questions[].lesson_slug` never goes "
                         "through `lessonsFor`) needs one.")

    # 5 — both functions this fix depends on are still defined.
    if "function ks4TopicHref(" not in src:
        problems.append("`ks4TopicHref` is no longer defined in "
                         "shared/student-live.js.")
    if "function lessonHref(" not in src:
        problems.append("`lessonHref` is no longer defined in "
                         "shared/student-live.js.")

    return problems


def main():
    problems = check()
    if problems:
        print("❌ student_lessons_cards_check: %d problem(s)\n"
              % len(problems))
        for p in problems:
            print("   · %s" % p)
        print()
        return 1
    print("✅ student_lessons_cards_check: \"Lessons in this topic\" "
          "resolves a KS4 card's href from the class's own pathway/tier "
          "(via lessonsFor[currentId]/ks4TopicHref), falls back to "
          "lessonHref(slug) for KS3, and the bare lessonHref(slug)-only "
          "regression is not back. TEXT ASSERTION ONLY — see this "
          "file's docstring for why a real drive is not run here.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
