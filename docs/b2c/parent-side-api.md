# Parent side: API contract, final shapes (25 Oct 2026)

Backend: `mrbadmus---backend`, branch `feat/parent-side` (worktree
`mrbadmus-backend-worktrees/parent-side`), commits `324c3d3`, `c56e72d`, `60b7d64`, plus the fixture-text fix.
The calculations are pure functions in `consumer/answers.js`, next to `outcomeOf` and `tally`. The rules
are tested in `test_parent_side.js` (133 checks) and the routes are in the same file.

Every route is under `/api/consumer`, sits behind `consumerGate`, and is **read-only**: no insert, update or
delete anywhere on these paths. The one exception is `requireChild`'s existing five-minutely `last_active`
stamp on the child route, which every child route already makes. Each route is scoped like this:

| route | guard | whose data |
|---|---|---|
| `GET /children/:id/activity` (extended) | `requireGuardian` | `:id`, only once `guardian_of_child()` has said yes. Any other id gets **404** and nothing is confirmed. |
| `GET /children/:id/past-work` (new) | `requireGuardian` | same as above |
| `GET /family/past-work` (new) | `requireParent` | the students of the parent's own family org (the same read as `GET /family`). `?child=` with any other id gets **404**. |
| `GET /family/home` (new) | `requireParent` | same as above |
| `GET /child/activity` (new) | `requireChild` | always `req.child.profile.id`. It has no id parameter, and any `child_id` or `id` in the query is ignored. |

Production schema only, with **no migrations**. Every column read already exists on production
(`child_answers.subject/key_stage/lesson_slug/unmarked_reason`, `work_items.ref`).

---

## The rules (what the backend calculates)

### Secure / Shaky / Not yet: `topicStatus()`
Topic = **knowledge point**. The rule runs over **marked** attempts only, in answer order (`answered_at`, then
`attempt_no`).
- **right** = outcome `correct`. A written answer is right only at full marks. `partial` is **not** right.
- **secure** = the two most recent marked attempts are both right, on **different** `question_id`s, and **≥ 7
  London calendar days apart**. Calendar days, not hours: Mon 18:00 to the next Mon 09:00 counts as 7.
- **not_yet** = the most recent marked attempt is not right, or the topic has never been right. That includes a
  topic with **no marked attempt at all**: `basis.marked === 0`, so the page should say "not marked yet"
  rather than imply the child got it wrong.
- **shaky** = everything else: the most recent attempt was right, but the topic is not yet secure.
- Unmarked and self-checked answers are never right and never in the basis. They are counted beside it in
  `basis.unmarked` and `basis.self_checked`.

### Keeps getting wrong: `buildKeepsWrong()`
Only answers with outcome `wrong` count. `partial` and unmarked answers never count.
- **question** entry: the same `question_id` wrong ≥ 2 times.
- **topic** entry: the same knowledge point wrong ≥ 2 times across **≥ 2 different questions**. A topic
  whose wrong answers are all on one question is already that question's entry, and listing it twice would
  repeat itself (the "no redundant text" rule).
- `weeks_span` = the number of distinct Mon–Sun London calendar weeks the wrong answers fall in. Sunday 18 Oct
  then Monday 19 Oct counts as 2.
- `answers[]` = every wrong answer: what the child wrote, the correct answer, when, and its `work_item_id`.
- Sorted by `wrong_count` (highest first), then by the most recent wrong answer.

### Tracked: `trackedOf()`. How we know an activity saved no answers
- An item with ≥ 1 ledger row is `tracked: true`.
- An item that is **not done** is `tracked: true`, because it is "not done", never "untracked".
- A **done** item with **zero** ledger rows is `tracked: false`, with an `untracked_reason`:
  - `kind_not_saved`: a `flashcards` item. Flashcards keep their own record (`flashcard_reviews`) and never
    write to the answer ledger.
  - `before_saving`: `done_at` is before the ledger existed. Production's `child_answers` went live on
    14 Oct 2026 10:59:42 UTC (migration `20261014105942`). A database that had it earlier can say so with
    the `LEDGER_STARTED_AT` env variable.
  - `no_answers_saved`: done after the ledger began, of a kind that writes answers, yet no answers are
    there. For a **lesson** this means a page that saves nothing: a custom layout such as a simulation (no
    `mrbadmus.v2.js` on the page), or a lesson read and ticked without answering. For practice, exam or unit
    check (whose hooks always write) it means a ledger write that did not land.
  - The page words every untracked case as "This activity isn't tracked yet", never as missing, blank or
    zero. An untracked item's score is `null`, not 0.
- Known limit: in `/activity`, `tracked` looks at the item's answers **within the requested range**.

### Marking states
Each answer carries `marking_state`:
- `scored`: a key, the AI or the stub marker gave it a verdict.
- `self_checked`: the child checked it themselves. It is stored, but is never right or wrong.
- `unmarked`: nobody could mark it. `unmarked_reason` gives the reason: `marker_error`, `daily_limit`,
  `no_key` or `no_scheme`.

Every summary carries `marked` and `self_checked` beside the existing counts (marked + unmarked =
answered), so the page can write "7/11 marked · 1 answer not marked". Scores use marked answers only.
6-mark answers keep `mark_level` (0–3) and `mark_next_step`.

### Weeks
- **The parent's week is Mon–Sun** (`week.js stripOf`), London time, and is labelled by its Monday:
  `"19 October"`, with the year added when it is not the current year.
- ⚠️ This is **not** `work_items.week_start`, which is the *teaching* week (it rolls on Sunday). A Sunday item
  has `week_start` = the next Monday. Past work groups by the **London day the item was done**, so an item
  done early sits in the week it was done, never in a future week.
- `/activity` (all routes) now reads `week_start ≤ to + 1`. Before this, on a Sunday, today's own item
  (`week_start` = tomorrow) was missing from "this week".

### Time
`time_spent_seconds` is `null` when it was not measured. `summary.time_seconds` is `null` when nothing in
the item was measured, and `time_complete` is false when some answers were untimed. The backend never makes
up a time estimate.

---

## 1. `GET /children/:id/activity`: additions
All existing fields are unchanged, and the new ones are appended. Top-level keys, in order:
`child, range, work_items, other_answers, own_work, knowledge_points, tutor_questions,` **`topics, topics_unplaced,
keeps_wrong`**.

⊕ 9 Nov 2026, additive. `own_work` holds the answers in no work item (a child's free choice), as pieces in the
shape of a done item, with `own_work: true`, `done_day` and `answers`: one per child + lesson (or exam or session)
+ UK day. A page shows these or `other_answers`, never both, and every answer row is in exactly one work item or
own-work entry. "N of M done" and the week strip stay about set work. On an answer, `self_ticks` and `self_level`
are the child's own self-marking, never a mark. A piece's `marks_scored` and `marks_available` count each
question's latest marked attempt; `answers` still lists every attempt. See API-CONTRACT.md.

```json
{
  "child": { "id": "ecc8…", "first_name": "Amara", "year_group": "9", "key_stage": "KS3",
             "username": "CrimsonPrism79", "last_active_at": "2026-10-22T19:00:00.000Z" },
  "work_items": [{
    "id": "8bf4…", "kind": "exam", "title": "Exam question: a flat phone battery", "sub": "6 marks",
    "week_start": "2026-10-12", "scheduled_for": "2026-10-17", "status": "done",
    "done_at": "2026-10-17T11:30:00+00:00", "removed": false,
    "summary": { "answered": 1, "questions": 1, "correct": 0, "partial": 1, "wrong": 0, "unmarked": 0,
                 "marks_scored": 4, "marks_available": 6, "time_seconds": 410, "time_complete": true,
                 "answers_timed": 1, "answers_untimed": 0, "sessions_timed": 0,
                 "marked": 1, "self_checked": 0 },
    "answers": [{
      "id": "4807…", "surface": "exam", "question_id": "ks3-p1-energy-stores-produce",
      "knowledge_point": { "id": "ks3.energy-stores.3", "label": "Light, sound, heating and electric current are pathways…" },
      "question_text": "A student says: “A phone battery holds electrical energy…” Correct both.",
      "answer": "The battery does not hold electrical energy, it holds a chemical store. …",
      "correct_answer": "Says the battery holds a chemical store, not an electrical one.\n…",
      "kind": "written", "outcome": "partial", "is_correct": null, "marks_scored": 4, "marks_available": 6,
      "points_hit": [1, 2, 3], "points_total": 5, "feedback": "…", "mark_level": 2,
      "mark_next_step": "Say where the energy has gone — …", "marked_by": "stub", "attempt_no": 1,
      "time_spent_seconds": 410, "answered_at": "2026-10-17T11:24:00+00:00",
      "work_item_id": "8bf4…", "marking_state": "scored", "unmarked_reason": null, "subject": "Physics"
    }],
    "subject": "Physics", "tracked": true, "untracked_reason": null
  }, {
    "id": "…", "kind": "lesson", "title": "Animal and plant cells", "status": "done", "answers": [],
    "summary": { "answered": 0, "marked": 0, "…": "…" },
    "subject": "Biology", "tracked": false, "untracked_reason": "no_answers_saved"
  }],
  "topics": [{
    "id": "ks3.energy-stores.2",
    "label": "Energy sits in stores: kinetic, gravitational, elastic, thermal, chemical, magnetic, electrostatic or nuclear",
    "subject": "Physics", "key_stage": "KS3",
    "lesson": { "slug": "energy-stores", "name": "Energy stores" },
    "status": "secure",
    "basis": { "answers": 2, "marked": 2, "unmarked": 0, "self_checked": 0, "right": 2, "wrong": 0, "partial": 0, "questions": 2 },
    "last_seen": "2026-10-15T18:03:00+00:00"
  }, {
    "id": "ks3.animal-and-plant-cells.1", "label": "Name and describe the four parts found in both animal and plant cells",
    "subject": "Biology", "key_stage": "KS3", "lesson": { "slug": "animal-and-plant-cells", "name": "Animal and plant cells" },
    "status": "shaky",
    "basis": { "answers": 3, "marked": 2, "unmarked": 1, "self_checked": 1, "right": 2, "wrong": 0, "partial": 0, "questions": 3 },
    "last_seen": "2026-10-09T16:40:00+00:00"
  }],
  "topics_unplaced": { "answers": 0 },
  "keeps_wrong": [{
    "kind": "topic", "id": "ks3.changes-of-state.3",
    "label": "Temperature stays constant during a change of state while energy breaks particles apart",
    "subject": "Chemistry", "wrong_count": 3, "weeks_span": 2,
    "first_at": "2026-10-07T17:31:00+00:00", "last_at": "2026-10-15T18:02:00+00:00",
    "answers": [{ "question_id": "c1-03-e03", "question_text": "…At which two temperatures does it stop?",
                  "answer": "−20 °C and 0 °C", "correct_answer": "0 °C and 100 °C", "outcome": "wrong",
                  "answered_at": "2026-10-07T17:31:00+00:00", "work_item_id": "c1d3…", "…": "the full answer shape" }]
  }]
}
```
- `topics[]` is one entry per knowledge point (sorted by key stage, lesson, then point). `lesson` lets the page
  group or name them. `topics_unplaced.answers` counts answers with no knowledge point, so none are dropped
  silently.
- A question entry in `keeps_wrong` has `kind: "question"`, `id` = the question id, and `label` = its newest
  question text.

## 2. `GET /family/home`
```json
{
  "today": "2026-10-25",
  "ledger_ready": true,
  "parent": { "first_name": "Funmi" },
  "children": [{
    "id": "ecc8…", "first_name": "Amara", "year_group": "9", "key_stage": "KS3", "username": "CrimsonPrism79",
    "last_active_at": "2026-10-22T19:00:00.000Z", "days_inactive": 3, "never_logged_in": false,
    "week": { "week_start": "2026-10-19", "label": "19 October", "done": 4, "total": 6,
      "days": [ { "date": "2026-10-19", "weekday": "Mon", "state": "done", "set": 1, "done": 1 },
                { "date": "2026-10-23", "weekday": "Fri", "state": "missed", "set": 1, "done": 0 },
                { "date": "2026-10-24", "weekday": "Sat", "state": "none", "set": 0, "done": 0 },
                { "date": "2026-10-25", "weekday": "Sun", "state": "due_today", "set": 1, "done": 0 } ] },
    "most_recent": { "work_item_id": "46d2…", "title": "Flashcards: changes of state", "kind": "flashcards",
      "subject": null, "done_at": "2026-10-22T19:00:00+00:00", "score": null,
      "tracked": false, "untracked_reason": "kind_not_saved" },
    "attention": [ { "kind": "overdue", "due_count": 1 },
      { "kind": "keeps_wrong", "topic": "Temperature stays constant during a change of state…", "topic_kind": "topic",
        "topic_id": "ks3.changes-of-state.3", "wrong_count": 3, "weeks": 2, "more": 1 } ]
  }, {
    "first_name": "Tobi", "key_stage": "KS4", "days_inactive": 6, "never_logged_in": false,
    "most_recent": { "title": "Distance, Speed and Velocity", "kind": "lesson", "subject": "Physics",
      "score": { "marked_scored": 0, "marked_available": 2, "marked": 2, "unmarked": 0 }, "tracked": true, "untracked_reason": null },
    "attention": [ { "kind": "inactive", "days": 6, "due_count": 2 },
      { "kind": "keeps_wrong", "topic": "A runner covers 240 m in 40 s. Calculate the average speed.",
        "topic_kind": "question", "topic_id": "ks4-distance-speed-velocity-e02", "wrong_count": 2, "weeks": 2, "more": 0 } ]
  }],
  "attention_all": [ { "child": { "id": "ecc8…", "first_name": "Amara" }, "kind": "overdue", "due_count": 1 }, "…" ],
  "plan": { "state": "active", "interval": "month", "children": 2, "monthly_pence": 1598, "annual_pence": 12800,
            "next_payment": "2026-11-06T18:05:29.823+00:00", "payment_failed_at": null,
            "cancel_at_period_end": false, "access_end": null }
}
```
- `week.days[].state` is one of:
  - `done`: every item that day is done (done early counts)
  - `missed`: a past day with an item not done
  - `due_today`: today, with an item not done
  - `set`: a later day with items set (**added**: the contract had no word for it, and `none` would have said
    "nothing set", which is false)
  - `none`: nothing set that day
- `attention` holds **at most one** of `never_logged_in` (`set_count`, `first_due`), `inactive` (≥ 5 days:
  `days`, `due_count` = not-done items up to today) or `overdue` (`due_count` = not-done items before today).
  After that comes the child's **top** `keeps_wrong` entry, with `more` = how many other entries there are.
  `days_inactive` is always sent, because "several days" means 4+ and the flag only shows at 5.
- `never_logged_in` = no sign of life at all: no visit, no finished item, no own action. This is
  `work.js lastActiveOf()`, the same rule as the existing dashboard. ⚠️ A visit stamp within 60 s of the
  profile's creation is read as the column default and ignored, so a fixture child driven straight after
  creation still looks "never".
- `plan` comes from `stripe.billingFor()`. It never carries a trial countdown (`days_left` and `trial_end` are
  not passed on). If billing cannot be read, it is `null`.
- `ledger_ready: false` means the database has no answer ledger. Cards still render, with `score: null`,
  `tracked: null` and no keeps-wrong entries.

## 3. `GET /children/:id/past-work?sort=&subject=&week=`
- `sort`: `newest` (default), `oldest`, `highest` or `lowest`.
  - `highest` and `lowest` order **weeks** by the week's marked fraction (Σ marks scored / Σ available
    across its items) and order **items** within a week by their own fraction.
  - A week or item with nothing marked sorts **last** either way.
  - Any other value gets 400 `past_work_invalid` `{field:'sort'}`.
- `subject`: `Biology`, `Chemistry` or `Physics` (case-insensitive). `all` or empty means no filter. Anything
  else gets 400.
- `week`: any date, normalised to its Monday.
- Only **done** items are listed (Design: "Completed work appears here week by week").

```json
{
  "child": { "id": "ecc8…", "first_name": "Amara" },
  "sort": "newest", "subject": null, "week": null,
  "subjects": ["Biology", "Chemistry", "Physics"],
  "total_items": 11,
  "weeks": [{
    "week_start": "2026-10-19", "label": "19 October", "done": 4, "untracked": 2,
    "score": { "marked_scored": 3, "marked_available": 4, "marked": 4, "unmarked": 0, "fraction": 0.75 },
    "items": [{
      "id": "46d2…", "kind": "flashcards", "title": "Flashcards: changes of state", "sub": null, "subject": null,
      "scheduled_for": "2026-10-22", "done_at": "2026-10-22T19:00:00+00:00", "done_day": "2026-10-22",
      "summary": { "answered": 0, "marked": 0, "self_checked": 0, "marks_scored": 0, "marks_available": 0, "time_seconds": null, "…": "…" },
      "score": { "marked_scored": 0, "marked_available": 0, "marked": 0, "unmarked": 0, "fraction": null },
      "tracked": false, "untracked_reason": "kind_not_saved"
    }]
  }]
}
```
- `subjects` lists every subject present, so the filter chips stay put while a filter is on.
- `title` and `sub` are the display names (`work-display.js`, the same names Today shows).
- To open an item, use the `answers[]` of that `work_items[]` entry from `/children/:id/activity`, or from
  `/child/activity` for the child.

⊕ 9 Nov 2026, additive. A row may be `own_work: true` (see section 1), or `started: true` with its `status`: set
work holding answers but not finished, in the week of its last answer. A week's `done` stays set work, with
`own_work` and `started` counted beside it. Every answer row of the child is in exactly one row here.

## 4. `GET /family/past-work?sort=&subject=&week=&child=`
This has the same shape as route 3, across every child in the family. It starts with
`children: [{id, first_name}]` in place of `child`, and every item carries `child: {id, first_name}`.

## 5. `GET /child/activity?from=&to=`
This has the same shape as `/children/:id/activity`, for the signed-in child only. `child` has no
`last_active_at` (a field only the parent sees). The child sees their own tutor questions with replies.
The response is sent with `Cache-Control: no-store`.

---

## TEST fixture and local server (for the drivers)

Both scripts are **TEST only**. They read the credentials at run time and prove the target from each key's own
`ref` claim. Production (`urklkrwevjtlfbwnipjn`) is refused. Nothing secret is written to disk.

```bash
cd mrbadmus-backend-worktrees/parent-side
node scripts/parent-side-fixture.js create --out /path/fixture.json   # prints + writes the manifest
node scripts/parent-side-server.js --port 41877 [--origin http://localhost:8123]
node scripts/parent-side-fixture.js teardown /path/fixture.json       # snapshot-by-owner, delete by id
```

- The service key and URL come from `mrbadmus---backend/.env`. The TEST **anon** key, which child sign-in
  needs, comes from `mrbadmus-worktrees/b2c/backend/.env`. Override either path with `PARENT_SIDE_ENV` or
  `PARENT_SIDE_ANON_ENV`.
- The server runs with:
  - `CONSUMER_SIGNUP_ENABLED=true`
  - `ANTHROPIC_API_KEY=''`: no model, stub marking, and the tutor answers "unavailable"
  - `STRIPE_SECRET_KEY=''` and `RESEND_API_KEY=''`
  - `EXTRA_CORS_ORIGINS=--origin`
  - `localhost:3000` and `localhost:5500` are already allowed
- When it is listening it prints one JSON line: `{"ready":true,"base":…}`.
- The manifest contains:
  - `org_id`
  - `parent{id,email,password}`
  - `children[{id,first_name,username,password,email,key_stage,year_group,work_items[{id,kind,title,
    scheduled_for,week_start,status,done_at,why,expect}],answers[{id,work_item_id,question_id,
    knowledge_point_id,outcome,answered_at,why}],tutor_questions[]}]`
  - `ids{work_items,child_answers,child_tutor_questions}`
  - `expect{…}`: the intended Secure/Shaky/Not-yet topics, keeps-wrong entries and untracked items
  - `logins_checked`: each login proven against real Auth
- Children sign in through the real `POST /api/consumer/child/login` with `{username, password}`. The
  usernames are the database's generated ones (the username guard replaces any it rejects).
- ⚠️ Wait more than a minute after `create` before driving a child. Otherwise their first visit stamp is
  read as the profile default (see above).
