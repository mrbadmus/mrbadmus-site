#!/usr/bin/env python3
"""export_ks3_extended.py — the KS3 ladder's EXTENDED rungs, as JSON rows.

    python3 export_ks3_extended.py            # JSON array on stdout
    python3 export_ks3_extended.py --check    # counts only

── Why this exists, and why it is a separate script ─────────────────────

`export_ks3_questions.py` mirrors the three KS3 pools that a machine can
MARK: the bank, and the `recall`/`apply` rungs. It says so in its own
docstring, and it is right to:

    "Only `recall` and `apply` are exported: they are multiple choice and
     have a right answer. `explain` and `produce` are marked BY THE STUDENT
     against success criteria — nothing can score them."

MRB-313 is the thing that changed. `exam_questions` is a pool of
EXTENDED-RESPONSE items, and an extended-response item is exactly what
cannot be marked by comparing an option index. The `explain` and `produce`
rungs are the only KS3 content in the estate that is already written as a
written-answer question WITH criteria attached, so they are the KS3 half of
that pool.

⚠️ THIS IS NOT A SECOND MIRROR AND IT MUST NOT BECOME ONE. It writes
nothing to `ks3_ladder_questions`, and it does not touch the pools MRB-288
governs. It prints rows for the backend's `scripts/seed-exam-questions.js`
to upsert into `exam_questions`, whose `source` column records that they
came from here. The lesson page still renders its own ladder from the
authored file, unchanged, and still marks these two rungs the way it always
has — against the criteria, by the student.

⊕ MARKS ARE A PER-RUNG TARIFF — RULED BY MIDE, 2 Sep 2026 (MRB-313, Night 3).
An `explain` rung is **4 marks** and a `produce` rung is **6 marks**. The
success criteria are the marking points, and the marker applies best-fit
against them: an answer is placed by how much of the criteria it meets,
not by counting ticks one-to-one.

This REPLACES the Night 2 derivation `marks = min(6, max(2, len(success)))`,
which was a code decision awaiting this ruling. Why it was wrong: a success
criterion is written to help a thirteen-year-old check their own answer,
not to tariff the question, so four criteria never reliably meant four
marks — and it left the KS3 pool with no 6-markers at all, so Design's
"6 marks" filter on the child's exam-questions screen returned nothing at
KS3. The tariff now lives in `MARKS` below; changing it is one line and a
re-run of `scripts/seed-exam-questions.js` (idempotent upsert on `id`).
"""

import argparse
import importlib
import json
import os
import pkgutil
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)

# The rungs that are WRITTEN answers. `recall` and `apply` are multiple
# choice and belong to the other exporter; taking them here would put the
# same question in two pools, which is the thing MRB-288 exists to stop.
EXTENDED_RUNGS = ("explain", "produce")

COMMAND = {"explain": "Explain", "produce": "Produce"}

# The tariff. Ruled by Mide 2 Sep 2026 — see the module docstring. The
# `exam_questions.marks` CHECK is `between 2 and 6`; both values sit inside it.
MARKS = {"explain": 4, "produce": 6}

# A KS3 unit code's first letter is its science. There are exactly three.
SUBJECT = {"B": "Biology", "C": "Chemistry", "P": "Physics"}


def lesson_modules():
    """Every authored lesson module, as (unit_code, module).

    Same walk as `export_ks3_questions.lesson_modules()`, deliberately —
    if the two ever disagree about what a lesson is, the pools drift.
    """
    import ks3_data

    found = []
    for unit in sorted(m.name for m in pkgutil.iter_modules(ks3_data.__path__)
                       if m.ispkg):
        pkg_dir = os.path.join(REPO, "ks3_data", unit)
        for fname in sorted(os.listdir(pkg_dir)):
            if not (fname.startswith("lesson_") and fname.endswith(".py")):
                continue
            mod = importlib.import_module("ks3_data.%s.%s" % (unit, fname[:-3]))
            if getattr(mod, "LESSON", None) is not None:
                found.append((unit.upper(), mod))
    return found


def unit_titles():
    from ks3_data.structure import unit_index
    return {code: u["title"] for code, u in unit_index().items()}


def rows():
    titles = unit_titles()
    out = []
    for unit_code, mod in lesson_modules():
        lesson = mod.LESSON
        slug = lesson.get("slug")
        ladder = lesson.get("ladder") or {}
        if not slug:
            raise SystemExit(
                "export_ks3_extended: %s has a ladder but no slug" % mod.__name__)

        subject = SUBJECT.get(unit_code[0])
        if subject is None:
            raise SystemExit(
                "export_ks3_extended: unit %s does not start B, C or P, so "
                "its science cannot be read off the code" % unit_code)

        for rung in EXTENDED_RUNGS:
            r = ladder.get(rung)
            if r is None:
                continue
            q = (r.get("q") or "").strip()
            success = [s for s in (r.get("success") or []) if s and s.strip()]
            if not q:
                raise SystemExit(
                    "export_ks3_extended: %s#%s has no question text"
                    % (slug, rung))
            if not success:
                # A rung with no criteria cannot be marked by anything —
                # not by the student on the page, and not by the marker.
                # Skipping it silently would hide an authoring gap, so say so.
                raise SystemExit(
                    "export_ks3_extended: %s#%s has no success criteria, so "
                    "there is nothing to mark it against" % (slug, rung))

            out.append({
                "id": "ks3-%s-%s-%s" % (unit_code.lower(), slug, rung),
                "key_stage": "KS3",
                "subject": subject,
                "topic": titles.get(unit_code, unit_code),
                "unit_code": unit_code,
                # Per-rung tariff, ruled. See MARKS and the module docstring.
                "marks": MARKS[rung],
                "command": COMMAND[rung],
                "text": q,
                "stem": None,
                # The success criteria ARE the marking points (Mide, 2 Sep
                # 2026). Nothing here is `essential`: the marker places the
                # answer by best fit against the set, so missing one point is
                # a lower mark, never a zero.
                "scheme": [{"text": s, "essential": False} for s in success],
                "levels": None,
                "indicative": None,
                "source": "ks3_ladder",
                "tier": None,
                "pathway": None,
            })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="print counts only, emit no JSON")
    args = ap.parse_args()

    data = rows()
    if args.check:
        by_subject = {}
        by_rung = {}
        for r in data:
            by_subject[r["subject"]] = by_subject.get(r["subject"], 0) + 1
            by_rung[r["command"]] = by_rung.get(r["command"], 0) + 1
        print("rows:      %d" % len(data))
        print("by subject: %s" % by_subject)
        print("by command: %s" % by_rung)
        print("marks:      %s" % sorted({r["marks"] for r in data}))
        return

    json.dump(data, sys.stdout, ensure_ascii=False, indent=None)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
