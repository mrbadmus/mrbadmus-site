# Parent side rebuild — plan and API contract (25 Oct 2026)

Built from Design's delivery: `/Users/midebadmus/Desktop/MrBadmus AI/B2C/UI-UX/Parent Side Rebuild /`
(prototype `prototype/MrBadmus parent side - bundle.html`, readable source `source/Parent Side.dc.html`,
tokens `tokens/parent-side-tokens.css`, notes `HANDOFF-NOTES.md`, `README.md`). Use `?screen=home|child|past|today|question|kidpast`
`&child=amara&theme=light|dark&w=1440` on the bundle to see every state.

Worktrees (never push from them; the commander pushes):
- site    `/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/parent-side`  branch feat/parent-side (origin/main 1448d9033)
- backend `/Users/midebadmus/Documents/GitHub/mrbadmus-backend-worktrees/parent-side` branch feat/parent-side (origin/main 8fb1112)

## Scope tonight
Parent Home · Child detail (this week, Topic picture, Keeps getting wrong, Tutor questions, work panel showing every question) ·
Past work (parent: all children, and child: "Everything you've done") grouped by week, newest first, sort newest/oldest/highest/lowest,
filter by subject, open an item = every question as in the child view · desktop child Today + question page · theme switch in the header
(Light / Dark / System, persists per device) · light default, softened dark at WCAG AA · brand = chevron + "MrBadmus" via `brand.py` only.
NOT tonight (list in the report as not built): Messages, Account sub-pages (plan, receipts, card, auto-renew, end plan, privacy…), Add child
/ Child settings redesign. Existing pages that already do these keep working and must stay linked from the new nav (no dead ends, no "coming soon").
School (Rainford) pages and behaviour must not change.

## Hard rules (from Mide)
- Every number on screen comes from real data. No invented fields. No placeholders on production.
- Secure / Shaky / Not yet are CALCULATED BY THE BACKEND. Per topic (knowledge point), over MARKED attempts only (an unmarked answer is never
  right and never in the basis, but is counted separately):
  - right = outcome `correct` (a written answer is right only at full marks; `partial` is NOT right).
  - **Secure** = the two most recent marked attempts are both right, on DIFFERENT questions, and at least 7 days apart.
  - **Not yet** = the most recent marked attempt is not right, or it has never been right.
  - **Shaky** = everything else (a mix recently: most recent right but not yet secure).
  - Always send the basis: how many answers (marked / unmarked / right / wrong / partial) the status is based on.
- **Keeps getting wrong** = same topic OR same question with `wrong` outcome two or more times; each wrong answer shown (answer text, correct answer, when).
- Never show an estimate as a measurement: time only where measured (`time_spent_seconds`/session times), else say nothing or "not timed".
- Never show an unmarked answer as correct. Three states: unmarked / self-checked / scored. 6-mark answers show the AQA LEVEL (`mark_level`), not just a score.
- Scores count marked answers only: "7/11 marked · 1 answer not marked".
- A gap in what is saved (an activity that saves no answers: custom-layout activities, anything done before saving existed) is shown honestly:
  "This activity isn't tracked yet" — never as missing, blank or zero. Backend flags it; the page words it.
- Week = Mon–Sun, British dates ("Week of 13 October"). "Nothing done for several days" = 4+ days; flag shows at 5.
- No claims about Mide's experience anywhere. No trial countdowns or "cancel before…". No green for marking states in new UI where Design says none
  (Design's own screens use a green tint for Secure/done — see conflicts file; follow Mide's WCAG + shape-and-word rule, not colour alone).
- Where Design's screens conflict with these rules or the data available: FOLLOW THE RULES and append a line to `docs/b2c/parent-side-conflicts.md`
  (screen · what Design drew · what the rule/data says · what you built). Do not guess silently.

## API contract (backend builds, site consumes)
All under `/api/consumer`, guardian-checked, READ-ONLY, same gates as `/children/:id/activity`. Additive only: existing fields unchanged.

1. `GET /children/:id/activity` (exists) — ADD:
   - `topics[]`: `{ id, label, subject, key_stage, status: 'secure'|'shaky'|'not_yet', basis:{answers, marked, unmarked, right, wrong, partial, questions}, last_seen }`
     (topic = knowledge point; if labels are unusable as topic names, group by lesson and say so in the conflicts file).
   - `keeps_wrong[]`: `{ kind:'topic'|'question', id, label, wrong_count, weeks_span, answers:[answerOut + work_item_id] }`.
   - on each `work_items[]`: `subject`, `tracked: boolean`, `untracked_reason: string|null`, `status_word` inputs (marked/unmarked/self-checked counts via `summary`),
     and each answer keeps `mark_level`, `outcome`, `time_spent_seconds` (null when not measured).
   - `child.username`, `child.last_active_at`.
2. `GET /family/home` (new) — one call for the parent home: `{ today, parent:{first_name}, children:[{ id, first_name, year_group, key_stage, username, last_active_at, days_inactive,
   never_logged_in, week:{week_start, done, total, days:[{date, weekday, state:'done'|'missed'|'due_today'|'none'}]}, most_recent:{work_item_id,title,kind,subject,done_at,score:{marked_scored,marked_available,unmarked}|null},
   attention:[{kind:'keeps_wrong'|'inactive'|'never_logged_in'|'overdue', topic?, wrong_count?, weeks?, days?, due_count?}] }], attention_all:[…same items with child ref…], plan:{children, monthly_pence, annual_pence, next_payment, … from billing, nullable} }`.
3. `GET /children/:id/past-work?sort=newest|oldest|highest|lowest&subject=&week=` (new) — work items grouped by week (`week_start`, label), each with summary and `tracked`,
   sort applied server-side (highest/lowest = marked score fraction of the week; unmarked-only weeks sort last), subject filter server-side. Opening an item uses the activity
   work_item's `answers[]`.
4. `GET /family/past-work` (new) — same, across all the parent's children (each item carries child ref).
5. `GET /child/activity` (new, requireChild) — the signed-in child's OWN history in the same shape as activity (no parent-only fields, tutor questions without replies hidden? — child may see their own),
   for "Everything you've done". A child can never read another child.

Tests live beside the existing `test_parent_truth*.js`. Keep every existing test green.

## Proof (the commander runs this after build)
Blind drivers on TEST at 1440 and 390, light and dark: family of two children, several weeks of work incl. deliberate wrong answers, a repeatedly-wrong topic, an unmarked written
answer, a 6-mark answer with level, tutor questions, one untracked activity. The page must equal the DB answer for answer. Production request count from TEST runs = 0.
