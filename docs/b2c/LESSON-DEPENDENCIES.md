# What family (B2C) children depend on in lesson pages

For the people rebuilding lessons to the lean standard (`docs/lessons/LEAN-STANDARD.md`).
Everything below is read off the lesson pages by code that sits outside the
lesson. Change one of these and a parent's child loses saved work, their
progress on a second device, or their knowledge-point tags, and **nothing on
the page looks wrong**. Line numbers are from commit 883a94eeb; search for the
function name if they have moved.

"Family child" means a session with an address ending `@children.mrbadmus.internal`.
School pupils at Rainford are not affected by any of this capture code.

---

## 1. Question ids

Every answer is saved against an id. Change the id and the answer no longer
comes back, the parent view counts a brand-new question, and it loses its
knowledge point. The server refuses any id outside `^[a-z0-9:#._-]{1,200}$`
(`QUESTION_ID_SHAPE`, backend `consumer/answers.js:1275`).

The ids below are built from the page, so **renaming a block, moving a rung or
rewording some questions changes the id**. The full list is in
`knowledge_points/README.md` ("How the ids work").

| id | where it comes from | what changes it |
|---|---|---|
| KS3 rung `<slug>#recall\|apply\|explain\|produce` | `.ks3-ladder[data-lesson]` + `.ks3-rung[data-rung]`, `shared/ks3.js:493,553,1231` | changing `data-rung`, `data-lesson` |
| KS3 start `<slug>#start` | `[data-activity="hook"][data-keyedblock]`, `shared/mrbadmus.v2.js:2991` | renaming the hook activity |
| KS3 keyed commit `<slug>#<activity>` | `[data-keyedblock]`, `mrbadmus.v2.js:2996` | changing `data-activity` |
| KS3 prediction `<slug>#<activity>` | `[data-activity]` not an instrument, `mrbadmus.v2.js:3006,3014` | changing `data-activity` |
| KS3 "Your turn" `<slug>#<activity>-<q>` | `[data-p<N>cfa-q]`, `mrbadmus.v2.js:3057` | changing the activity or question position |
| KS3 instruments `<slug>#<activity>-<n>` | adapters and `<ks3-specs>`: `KIND_A` :2084, `KIND_B5C` :2085, `<ks3-specs>` :2327, read by `tools/kp_ks3_units.py` | changing the activity, block class, or the ORDER of units (n counts them) |
| KS4 blocks `ks4:<slug>:<route>#start\|choice-n\|sort-n-i\|cfifa-n-q\|steps-n\|r1..r4\|r<r>-<i>\|chain-n\|write-n` | `pilotId`, `mrbadmus.v2.js:3843`; `shared/ks4-runtime.js:683` hands each block to the capture | adding, removing or reordering a block (n counts blocks of that type); changing the ladder's `r1..r4` keys |
| KS4 lesson's own activity `ks4:<slug>:<route>#<state key>[-<entry>]` | `<ks4-root-acts>` :4223 | renaming the lesson's state key or option list |
| KS4 forms (`ROOT_FORMS` stems) `ks4:<slug>:<route>#<form id>[-<row>]` | `ROOT_FORMS` :4699 | renaming the form's state or handlers; the table names them per lesson |
| KS4 practice set `ks4q:<slug>:<hash>` | server hashes the question text, `ks4QuizId`, backend `consumer/answers.js:122` | **rewording the question at all** |
| KS4 classic quiz card `ks4q:<slug>:<hash>` | `.q-text` on the page | **rewording the question at all** |
| KS4 classic matching `ks4c:<slug>:match-<n>` | `.match-def[data-index]`, `mrbadmus.v2.js:3643` | reordering the pairs |

⚠️ `ks4q:` ids are hashes of the wording. A plain-voice rewrite of a practice
question is a new id. Tighten the wording, then list old and new in the id map.

KS3 ids are by slug, so the eight slugs shared with KS4 (`aerobic-respiration`
and friends) stay apart only because the page path carries the key stage.

The id derivation in `tools/kp_classify.py` and `tools/kp_ks3_units.py` is the
single source. `tools/lesson_contract_check.py` reuses it.

## 2. Knowledge-point tags

Each question id has one knowledge point, the thing a parent sees as "secured"
or not. Tags live in `knowledge_points/ks3.json` and `ks4.json` and ship to the
backend as `knowledge-points.json` (`consumer/knowledge-index.js`), read by
`kpOf`, `consumer/answers.js:1536`. An untagged id is recorded with no point,
so it counts for nothing in a parent's view.

**New questions must be tagged before they ship:**

```
MRB_BACKEND_DIR=<backend checkout> python3 tools/kp_classify.py --top-up --cache <dir>
python3 tools/export_knowledge_points.py --check            # gate: knowledge_points_check
python3 tools/export_knowledge_points.py --backend <dir>    # writes knowledge-points.json
python3 tools/export_knowledge_points.py --check-backend <dir>   # gate: knowledge_points_mirror
```

Commit `knowledge_points/*.json` in the site repo and `knowledge-points.json` in
the backend repo. The backend pushes first (the deployment order in `CLAUDE.md`).
Each saved row keeps the point it had when it was written, so a tag can change
later without rewriting history. A point left with no questions fails the
`knowledge_points_check` gate and needs a person.

## 3. Answer keys the server trusts

| what | where | what breaks |
|---|---|---|
| `keys` map: the one right option per question, as the page sends it | `knowledge_points/*.json` → `knowledge-points.json`, read at `consumer/answers.js:1843` | change the option text or the right option and the child is marked by the old key. A top-up re-places the tag and key together. |
| KS3 ladder MCQ `<slug>#recall\|apply` | DB table `ks3_ladder_questions`, read at `consumer/answers.js:1863` | if options change, the server cannot match the child's answer (it falls back to the page's own verdict). Reload when the unit ships with `python3 export_ks3_questions.py --load prod --pools ladder` (rehearse with `--load test` first); `--verify --project prod` is the gate. |
| KS3 written rung twin `ks3-<unit>-<slug>-explain\|produce` | DB table `exam_questions` (`export_ks3_extended.py`), read at `consumer/answers.js:1907` | used only when its text and scheme match the page exactly (`twinMatchesPage`); otherwise the page's own question and criteria are marked. Rewording the rung is safe, but the twin goes unused until reloaded. |

## 4. Page selectors the saving and restoring code reads

The capture and restore code (`shared/mrbadmus.v2.js:1464-6741`, `shared/ks3.js`)
reads these exact selectors. If one disappears the block silently stops saving.

**KS3 lesson**
`/shared/config.js`, `/shared/mrbadmus.v2.js` and `/shared/ks3.js` scripts ·
`body[data-ks3-lesson]` (`ks3.js:38098`) · `.ks3-lesson` ·
`.ks3-ladder[data-lesson]` · `#s-ladder` (`ks3.js:18528`) · `.ks3-rung[data-rung]` and
`[data-mode]` · `.ks3-rung-q` (the question text sent, `ks3.js:1229`) ·
`[data-score]` · `[data-activity]` · `.ks3-option` with `[data-correct]` ·
`.ks3-opt-label` and `[data-full]` · `[data-keyedblock]`, `[data-keyed]`,
`.ks3-keyed-reply[data-reply]` · `[data-reveal]`, `.ks3-commit`,
`[data-instrument]`, and each instrument kind's own class and `data-*` attributes
listed in `KIND_A`, `KIND_B5C` and `<ks3-specs>`.

**KS4 rebuilt lesson**
`/shared/config.js`, `/shared/mrbadmus.v2.js`, `/shared/ks4-runtime.js`,
`/shared/ks4-lib.js` scripts · `#ks4-mount` (`__mrbKs4` on it, restored
through the block state) · `MrBadmusKS4Runtime.mount` · `.ks3-ladder-score .ks3-score`
(see section 6). `ROOT_FORMS`, `ROOT_SPECS` and `ROOT_DRAFT` in `mrbadmus.v2.js` name
each lesson's own state keys and handlers: a rebuilt lesson's state keys must
keep their names, or those tables must be updated in the same change.

**KS4 classic page**
`.q-text`, `.quiz-opt`, `#quizEndMsg`, `.match-check-btn`, `.match-drop[data-accepts]`,
`.match-def[data-index]`, `.match-term`.

## 5. Embedded sims and instruments that save

The standard removes embedded sims. Some save answers: a KS3 instrument whose
kind is in `KIND_A`, `KIND_B5C` or `<ks3-specs>`, or a KS4 lesson's own activity
(`ROOT_FORMS`). What happens to a child's rows for a removed activity:

- The rows stay in `child_answers`. It is append-only and we keep it. The parent
  still sees those answers with their question text and point.
- Restoring has nothing to put them back into, and quietly skips them.
- **The rule:** list every removed activity's ids in the id map with value `null`
  (retired). Do not delete rows, do not reuse a retired id for a different question.
- If you delete a KS4 sim's state, also delete its entries in `ROOT_FORMS`,
  `ROOT_DRAFT` and `tools/ks4_root_explorations.json`, or
  `python3 activity_save_drive.py --commits` flags a draft key the lesson has lost.

## 6. Lesson-done signals

A family child's lesson ticks itself done on their Today screen from these
signals (`markLessonDoneFromActivity`, `consumer/work.js:2685`). Lose one and the
lesson never completes, and their streak breaks.

| page | signal | what must stay |
|---|---|---|
| KS3 | the ladder's `/api/quiz-score` post, `shared/ks3.js:198`; matched at `server.js:613` | `.ks3-ladder`, the URL path (subject, unit, slug are read from it) |
| KS4 rebuilt | `POST /api/consumer/child/lesson-done`, `mrbadmus.v2.js:1291`, sent once `.ks3-ladder-score .ks3-score` reads "Score N of 4" | the four-rung ladder and that exact line |
| KS4 classic | the same post, sent once `#quizEndMsg` is shown | `#quizEndMsg` |

## 7. Lesson URLs

Family work is set by page. `work_items.ref` stores
`/ks3/<subject>/<unit-slug>/<slug>.html` (or the KS4 path)
`hrefFor`, `consumer/work.js:636`, and answers find their work by that path
(`lessonItemMatch`, `consumer/answers.js:163`). `pathInfo`
(`consumer/answers.js:135`) reads subject, unit and slug from the URL.

**A lesson URL may not move.** There is no redirect map, and a moved page leaves
every set lesson link broken and every answer unattached. The check fails if a
page in the baseline has gone from its URL.

---

## THE RULE

**Question ids stay the same.** If an id must change, the rebuilt unit ships an
old-to-new map in the same commit.

File: `docs/b2c/id-maps/<unit>.json` — KS3 `P4.json`, KS4 `physics-energy.json`.
Shape, one key per id that moved or went:

```json
{
  "friction#old-activity-1": "friction#new-activity-1",
  "friction#removed-sim-2": null
}
```

`null` means the question has been retired. Any id that vanishes and is not in
the map fails the check.

**New questions carry a knowledge-point tag.** No map entry excuses a missing tag.

**How the map is applied**, in this order, when the unit ships:

1. **Tags:** run the top-up and export (section 2). It prunes retired ids and
   re-places renamed ones. Backend pushes first.
2. **The ledger:** `python3 tools/lesson_contract_check.py --unit <unit> --ledger-sql`
   prints the `update public.child_answers set question_id …` statements for the
   renamed ids. Mide runs it in the Supabase SQL editor after the code ships.
   Retired ids are left alone.
3. If a rung's options changed, reload `ks3_ladder_questions` (section 3).

---

## How to prove a rebuilt unit is safe

Run from the rebuilt worktree, after building. Static needs no browser and no
network; `--drive` opens headless Chrome, one at a time per machine.

```bash
# 1. The contract check. Pick the lessons by unit, slugs or path.
python3 tools/lesson_contract_check.py --unit P4
python3 tools/lesson_contract_check.py --unit physics/energy
python3 tools/lesson_contract_check.py --slugs efficiency,power
python3 tools/lesson_contract_check.py --pages 'ks3/physics/forces/*.html'

# 2. The live part: press the page as a family child, then a fresh browser.
#    MRB_BACKEND_DIR is the backend checkout (for the server's real id validator).
MRB_BACKEND_DIR=<backend checkout> python3 tools/lesson_contract_check.py --unit P4 --drive

# 3. The tag and answer-key gates.
python3 tools/export_knowledge_points.py --check
python3 tools/export_knowledge_points.py --check-backend <backend checkout>

# 4. Selector-independent checks of KS4 lesson state against the capture tables.
python3 activity_save_drive.py --commits
```

Exit 0 and "SAFE" means every id is there or mapped, every new id is tagged, no
selector the saving code reads has gone, and (with `--drive`) the answers come back
on a second device and the second device posts nothing.

`--drive` runs against this checkout with a pretend backend inside the script and
reaches nothing beyond 127.0.0.1, so it cannot touch TEST data or production, and
refuses to start if the configured backend is production. It uses
`activity_save_drive.py`'s press routine on just the chosen pages (a KS3 lesson
takes about 20 seconds, a KS4 page about two minutes; use `--pages` to pick
routes). On a rebuilt KS4 page it compares the shared answer blocks on the second
device; a lesson's OWN activities are proven by the named cases in
`activity_save_drive.py` itself, which do not take a page list.

The baseline (`tools/lesson_contract_baseline.json`) records what main looked
like before the rebuild. Regenerate it with `--write-baseline` **only from a clean
main before a rebuild starts**. Never regenerate it to make a failing check pass:
a red check is telling you a child's work would be lost.
