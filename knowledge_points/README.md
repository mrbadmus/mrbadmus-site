# Knowledge points

A **knowledge point** is one fact, idea or skill a pupil must know or be able
to do, written as a short plain-English statement a parent can read — for
example "Enzymes stop working when heat changes the shape of the active site".
Every question on the site is tagged with exactly one: the main thing it
tests. That is what lets a parent see which points their child has and has
not secured, and lets the site find "a different question testing the same
point".

**Status: machine-drafted on 11 Oct 2026 from the authored lesson content,
awaiting Mide's examiner review.** `tools/kp_classify.py` made one model call
(`claude-sonnet-4-6`) per KS3 lesson and per KS4 subtopic, giving it that
scope's own teaching content and every question in it, and asking for 4–10
points and one point per question. Nothing outside the supplied material was
allowed in. Treat every label and every tag as a draft.

## The files

| file | holds |
|---|---|
| `ks3.json` | one entry per KS3 lesson slug |
| `ks4.json` | one entry per KS4 subtopic slug |
| `untagged.json` | questions with no point, each with a reason; scopes whose classification failed |

Each entry: `{scope_ref, key_stage, subject, title, points: [{id, label}],
questions: {question_id: point_id}}`.

## How the ids work

- **Point ids** are `ks3.<lesson-slug>.<n>` and `ks4.<subtopic>.<n>`, with
  `n` counting from 1 in the order the points are listed.
- **Question ids** are the stable ids the parent-truth ledger stores:
  bank row ids (`b1-04-s01`, `ks4-enzymes-e01`), KS3 ladder rungs
  (`<slug>#recall|apply|explain|produce`), their exam twins
  (`ks3-<unit>-<slug>-explain|produce`, always the same point as the rung),
  KS4 rebuilt-lesson rungs (`ks4:<slug>#r1`..`#r4`), KS4 classic quiz cards
  (`ks4q:<subtopic>:<h>`, `h` = first 10 hex of sha1 of the normalised card
  text — `ks4_quiz_id()` in `tools/kp_classify.py`, the same function as the
  backend's `ks4QuizId`), and exam_questions ids (`bv2-…`, `cs-…`).
- **Round 2 (11 Oct 2026), every other id a lesson page sends:** KS3
  `<slug>#start`, predictions and keyed commits `<slug>#<activity id>`, and
  "your turn" questions `<slug>#<activity id>-<q>`; KS4 classic matching
  cards `ks4c:<subtopic>:match-<n>` (n = the pair's place in
  `matching.pairs`, from 1); and every block on a rebuilt KS4 lesson, PER
  ROUTE, `ks4:<slug>:<cf|ch|tf|th>#start|choice-n|sort-n-i|cfifa-n-q|steps-n|
  r1..r4|r<r>-<i>|chain-n|write-n`. Those last ids are read by running each
  lesson's logic for each route in Node (`tools/kp_ks4_eval.js`), because the
  content differs by route on about 128 of the 308 pages. Round 1's
  route-less `ks4:<slug>#rN` ids are retired.
- Round-2 ids were placed onto the EXISTING points (one model call per
  scope). Where nothing fitted, a new point was appended to the end of that
  scope, never renumbering the others; those points carry `"added": "round-2"`
  in the JSON and are listed by `--coverage`.

## Editing and re-running

- **To fix a label or move a question by hand**, edit the JSON directly. Keep
  the point ids as they are, then run
  `python3 tools/export_knowledge_points.py --check`.
- **To re-draft one scope** without touching any other:

      python3 tools/kp_classify.py --cache <cache dir> --scope <slug> --force

  Only that scope is sent to the model (its round-1 points, then its round-2
  ids onto them); every other scope is rebuilt from the cache unchanged (and the KS4 exam rows are re-placed from cache unless their
  candidate points changed). ⚠️ A re-drafted scope's points are renumbered
  from 1, so its point ids may now mean something different. Answers already
  recorded in `child_answers` copied the point id at the time, so re-draft a
  scope that has live answers only deliberately.
- A new or changed question turns the `knowledge_points_check` gate red until
  its scope is re-drafted (or the question is tagged by hand).
- **Load into TEST:** `python3 tools/export_knowledge_points.py --load test`
  (upsert, prune rows the JSON no longer names, then verify row for row).
  There is no production load yet: production does not have the tables.
- **Coverage:** `python3 tools/export_knowledge_points.py --coverage`.
