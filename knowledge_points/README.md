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
- **Round 3 (11 Oct 2026):** the KS3 question-shaped instruments,
  `<slug>#<activity>-<n>` (269 units), read off the BUILT pages by the same
  rules as the answer tap (`tools/kp_ks3_units.py`), placed onto the points
  as round 2 left them (own cache; earlier rounds undisturbed).
- **Round 4 (13 Oct 2026):** the practice-set items Design authors INSIDE a
  rebuilt lesson (batch 4 on, the lesson's `bankSrc`), which are not in the
  subtopic's quiz — e.g. "What do antitoxins do?" on
  communicable-diseases-defence. The practice set sends question_id null and
  the server derives the CLASSIC id `ks4q:<slug>:<h>` from the prompt, so
  these are classic-shaped ids no earlier round could see (176 of them, on 56
  lessons). Read by evaluating each lesson's `Ks4QuizBank` per route (the
  first 5 items — all the answer tap sends), `ks4_lessonbank_items()`. Also
  round 4: the 929 block ids of the 16 batch-7 lessons merged after round 3.
  All placed by the top-up (below); its new points carry `"added": "round-4"`.
- **Answer keys:** each scope's `keys` map gives, for every lesson-page
  question with exactly ONE right option, that option's text exactly as the
  page renders and sends it (trimmed only). It comes from the page markup
  where the page carries it (`data-correct`, `data-<p>-want-…`, `-is`,
  `data-answer`, the "Good guess" reply), else from the authored data by one
  named rule per instrument kind (`AUTHORED_RULES`). Predictions, written
  items, explorations and instruments whose one id covers several questions
  have no key. `--check` recomputes every key and refuses one that is not a
  rendered option. Exported into the backend's `knowledge-points.json`
  (see below); also loaded into TEST's `question_knowledge_points.answer_key`.
- Round-2 ids were placed onto the EXISTING points (one model call per
  scope). Where nothing fitted, a new point was appended to the end of that
  scope, never renumbering the others; those points carry `"added": "round-2"` (or `"round-3"`)
  in the JSON and are listed by `--coverage`.

## Editing and re-running

- **To fix a label or move a question by hand**, edit the JSON directly. Keep
  the point ids as they are, then run
  `python3 tools/export_knowledge_points.py --check`.
- **After new lessons or questions arrive (a merge, a new batch): top up.**

      MRB_BACKEND_DIR=<backend checkout> python3 tools/kp_classify.py --top-up --cache <dir>

  It reads the COMMITTED `ks3.json`/`ks4.json`, finds every id the loaders
  know that they do not tag, and places only those onto their scope's
  EXISTING points (the round-2 prompt, one call per scope, `"added":
  "round-4"` on any new point). Nothing already tagged moves and no point is
  renumbered, and it needs no cache — use it rather than the full run below,
  whose round-1-3 cache lives outside the repo and is gone after a reboot
  (the full run with no cache would re-draft and renumber every scope). A
  brand-new scope with no points is drafted by round 1 first. `--scope`
  narrows it. Then `--check`, `--backend`, and commit both repos.
  `MRB_BACKEND_DIR` also says whose `.env` the model key is read from.
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
- **Coverage:** `python3 tools/export_knowledge_points.py --coverage`. Ends
  with a per-bank section: for `ks3_assignment_bank` and `ks4_assignment_bank`
  (their Python sources) and for every other source together, the questions
  tagged and untagged, and every knowledge point with fewer than 3 questions
  from that source, listed by id.

## The backend's copy — `knowledge-points.json` (13 Oct 2026)

**The backend does not read the `knowledge_points` tables any more.**
Production will not get them (42k rows), so the backend ships its own copy:
`knowledge-points.json` in the backend repo root, read once (lazily) by
`consumer/knowledge-index.js`. It is how a consumer child's answer gets its
knowledge point, how a revealed lesson block is marked by its answer key, and
how the parent's activity view labels each point. Shape: `points` (point id →
`{label, key_stage, scope}`) and `questions` (question id → `[point id,
answer key or null]`), one entry per line.

**After ANY edit to ks3.json or ks4.json, re-export it:**

    python3 tools/export_knowledge_points.py --backend <backend checkout>

and commit the file in the backend repo. The `knowledge_points_mirror` gate
(`--check-backend`, the backend dir from `MRB_BACKEND_DIR` or the sibling
checkout) turns red until the two agree. The TEST tables can still be loaded
with `--load test` for SQL work, but nothing the backend does depends on them.
