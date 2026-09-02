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

⚠️ MARKS ARE DERIVED, AND THAT IS A CODE DECISION AWAITING MIDE'S RULING.
`marks = min(6, max(2, len(success)))`. A success criterion is not a mark
point: an author wrote them to help a thirteen-year-old check their own
answer, not to tariff it, and four criteria does not reliably mean four
marks. It is the only signal in the record that scales with the demand of
the question, so it is what the tariff is taken from tonight. If Mide rules
differently — a flat 4, a per-rung tariff, or hand-tariffed per lesson —
the change is one line here and a re-run of the seeder.
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
                # ⚠️ DERIVED. See the module docstring — awaiting Mide.
                "marks": min(6, max(2, len(success))),
                "command": COMMAND[rung],
                "text": q,
                "stem": None,
                # A success criterion is authored as something the student
                # can tick, so nothing here is `essential`: an answer that
                # misses one is a lower mark, not a zero.
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
