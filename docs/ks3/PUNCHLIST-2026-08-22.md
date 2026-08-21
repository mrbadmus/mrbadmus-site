# Run log — the live-page punch list, 22 August 2026

Follows `3ae1ae6a1`. Nine field defects Mide found walking the live student
pages himself. This file is the blow-by-blow; the report for Mide is
`MORNING-2026-08-23.md`.

**Production project ref: `urklkrwevjtlfbwnipjn` — ends in N.** Stated before
the first write, per the contract.

**Machine date at start of run: see the timestamps below.** The contract heads
itself 22 August; the machine, Supabase and the backend say 21 August. As last
run, the filenames follow the contract and every timestamp inside is the real
one.

---

## Recon

| fact | value |
|---|---|
| `8r/Sc1` class id | `d9740ab8-c4e3-4c22-bce9-629b650782c5` |
| its academic year | `2026-27`, 1 Sep 2026 → 31 Aug 2027 |
| today vs that year | **before it starts** — the pre-year window |
| therefore week 1 is | **Autumn**, per the standing ruling. P8 confirmed. |

`academic_years.is_current` still points at **2025-26**, which is exactly the
trap MRB-261 documents: the flag is moved by hand on 1 September. Nothing in
this run reads it.

---

## Log

### Unit 1 — P8 (the term name) and P9 (the Week 04 dot)

**P8. "SUMMER TERM" was not welded — it was COMPUTED, and computed wrongly.**
The brief says the term names are "welded and wrong ... never authored as
literals". Half right. `termLabel` had already been seamed on 21 August, and
`shared/student-live.js` computed it — from the CALENDAR MONTH and nothing
else:

    if (month >= 9 && month <= 12) return "AUTUMN TERM";
    if (month >= 1 && month <= 3)  return "SPRING TERM";
    return "SUMMER TERM";

Correct for eleven months a year and wrong for the one that matters. Today is
21 August, month 8, so it fell through to SUMMER — while the class it was
labelling belongs to **2026-27, a year that has not started**, whose first week
is Autumn Week 1.

Fixed by asking the academic year, which is the thing that knows. Anchored on
the year's own `start_date`, not on a hardcoded September:

| when | term |
|---|---|
| before `start_date` (the pre-year window — **today**) | AUTUMN |
| `start_date` … 31 Dec | AUTUMN |
| 1 Jan … 31 Mar | SPRING |
| 1 Apr … `end_date` | SUMMER |

Proved on twelve dated cases including both sides of every boundary and the
BST edge (23:30 UTC on 31 Aug is 00:30 on 1 Sep in London, and must read
Autumn). With no academic year readable it falls back to the old month rule
rather than refusing to draw a breadcrumb.

The other three sites the brief names — the breadcrumb strip, the work-list
caption and `boardScopeNote` — all read `termLabel`, so all three were fixed by
the one change. Verified by grep, not assumed.

**P9. The spine's "now" was THREE fours, not one.**

    trough:   n <= 4 ? 'var(--st-rule-fact)' : 'var(--st-crumb-bg)'
    numColor: … n === 4 ? 'var(--ks3-accent-text)' : …
    nowDot:   n === 4 ? 'var(--st-accent)' : 'transparent'

The brief names the dot. `trough` was not on it, and it shades weeks 1-4 as
ALREADY ELAPSED — three weeks of school that have not happened, drawn in the
"done" tone, directly under the wrong dot. Found by reading the whole block
rather than the line the brief pointed at. All three now read
`MRB_DATA('currentWeek')`, via two REWRITE seams (two rather than one because
the three are not contiguous and `rewrite_seams` splices literally).

**FIXTURE_TELLS widened, and one tell REMOVED.** Added `SIX QUESTIONS`,
`Six a round`, `SUMMER TERM`, `SPRING TERM`. **Removed `AUTUMN TERM`** — it was
a tell only while the correct answer was something else. Today Autumn IS
correct, so leaving it in would fail a right page, and a check that cries wolf
gets ignored. That is the whole reason the docket shipped.

**And a tell could never have caught P9, so it is not a tell.** Every entry in
that list is a string; the now-marker is a COLOUR. `innerText` cannot see one,
which is why the list went green twice over a picture that was visibly wrong.
Added `MARKER_PROBE` to `student_page_drive.py`: it reads the dots out of the
DOM, asks which are painted, and asserts the painted set is exactly
`window.__MRB_DATA__.currentWeek`. It checks the drawing against the page's own
data rather than against a hardcoded 1 — which would go red in September for
the right reason and get "fixed" by bumping the constant.

Gates: `student_parity.py` PASS, `student_behaviour.py` PASS. Seam count 26 → 28.

### Unit 2 — P1 and P3, the two buttons that went nowhere

**P1.** `openAssignment` ticked a checklist item and navigated nowhere. That is
not a bug in Design's file — Design drew ONE page, and in one page "open it" IS
a state change. It became a defect the moment there were two pages, and nothing
had told it so. It now navigates, and falls back to Design's tick when there is
nowhere to go, so the fixture is unchanged and no divergence was needed.

**P3.** One expression served five labels:

    primary: w.status === 'open' || w.retake ? this.openAssignment
                                             : () => this.go('recall')

Everything that was not the assignment fell into the recall round — so "Open the
lesson" opened recall, and so did "Ask for an extension".

⚠️ **THE BRIEF'S LESSON URL IS WRONG.** It says `/ks3/<subject>/<slug>.html`.
The real shape is `/ks3/<subject>/<unit>/<slug>.html` —
`/ks3/biology/breathing-and-gas-exchange/the-gas-exchange-system.html`. Building
what the brief said would have shipped 183 dead links.

And the unit directory is not derivable client-side. A student CAN walk
`assignment_questions.source_ref` → the bank/ladder tables → `(unit_code,
lesson_slug)` — all three readable under RLS, checked in `pg_policies`. What
they cannot learn is that `B4` lives at `biology/breathing-and-gas-exchange`;
that mapping is in `ks3_data`, which is Python. So `build_student_port.py` now
emits **`shared/ks3-lesson-urls.js`** — 183 lessons, 11 KB — built from
`ks3_data` and then CHECKED against the built tree. Reading the directory
listing instead would have produced a map that is self-consistent and wrong the
moment a lesson is renamed.

`source_ref` has **two shapes**, and both are real: `b4-01-s01` (a bank id) and
`chemistry/particles-and-their-behaviour/particle-model` (a path — how the
hand-seeded May demo was written). The demo is still the only MARKED work on the
platform, so the shape that looks like a legacy accident is the one a student
actually has feedback on. Both resolve through the same index.

Every real assignment draws on exactly ONE lesson (checked against production),
so "the first lesson" IS the lesson. The whole distinct list is carried anyway.

---

### Unit 3 — P2, P5, P6, P7

**P2. The counter was already right; the brief's premise is half wrong.**
`recallMeter` and `qCounter` read `this.questions.length`, and `student-live.js`
already stops filling the pool at six — so the round IS `min(6, pool)` and 01/02
was CORRECT for a class with one covered lesson. Nothing about round size or
composition needed changing, and it returns to six on its own when the banks
land, which is the ruling's own test.

What was wrong was the page ANNOUNCING six in four places, all of which spell
the number as a WORD, which is why no search for a digit found any of them:

| where | was | now |
|---|---|---|
| recall panel blurb | "Six a round, unlimited rounds." | "Two a round, unlimited rounds." |
| recall header eyebrow | "SIX QUESTIONS · UNLIMITED ROUNDS" | "TWO QUESTIONS · UNLIMITED ROUNDS" |
| round card | "RIGHT OUT / OF SIX" | "OF TWO" |
| the crumb rail | "SIX A ROUND" | "TWO A ROUND" |

The last had been *deliberately* left by a previous seam as "the recall view's
own label and not data". True while a round was six.

**"STREAK BROKEN" before anything was answered.** Zero meant two different
things and the page could not tell them apart. Now three states: silent, running,
broken. ⚠️ A first wrong answer is NOT a broken streak either — nothing was
built — so `broke` is set only on the transition FROM a streak, never on
reaching zero, which is where it starts. Invisible to the behaviour gate because
Design's fixture opens at streak 3; proved by driving.

**P5. Sign out** was `<a href="#top">` with no handler, on a shared school
machine. Needed a THIRD ruling mechanism — `SET_ON` — because `LOGIC` rewrites
logic, `PRUNE` removes nodes and `BINDINGS` only changes text; none can attach a
handler. It clears this device's `mrbadmusai.*` caches FIRST (the assignment
draft included — otherwise the next child gets this child's answers already
filled in), then ends the session through the guard the other student pages use.

**P6. The PROD badge** is now data with a new `drop` flag: when the value is
empty the ELEMENT goes with the text, because blanking a bordered chip leaves a
small empty box, which is worse than either state. Not pruned — pruning would
take the badge from localhost and the test project too, which is where it stops
someone driving the wrong database. ⚠️ Provable only on mrbadmus.com: every
local drive runs `localhost?env=prod`, where showing the badge is correct.

**P7. Settings removed** (nodes 26 and 30). ⚠️ The first draft pruned 26 and 30
on BOTH pages because both obviously have a header. **They do not have the same
one** — node indices are per-page, and on the assignment page 26/27/30/31 are the
deadline `sc-if`, the LATE chip, the HANDED IN chip and a chevron. That would
have silently deleted a student's LATE and HANDED IN badges, in the commit that
claimed to fix a dead button. Caught by checking rather than assuming.

**The behaviour gate needed a second half.** `RULED_DIVERGENCE` strips ruled text
from Design's side but does nothing to the CONTROL list, which is compared as a
plain list. Every divergence until now removed FIGURES; P7 is the first that
removes something a student can press, so the gap had never been reached. Added
`RULED_CONTROLS`, asserted both ways on the same split of scopes. Also: the
pattern needs its trailing space, or Design's side reads "Ayo␣␣Sign out" and all
nineteen drives go red over whitespace.

Gates: parity PASS, behaviour PASS (2 new ruled assertions).

### Rebase log

**Rebase 1 — before the Unit 2/3 push.** `origin/main` had moved from my parent
`510f8e7c6` to `dccb1918b`: the parallel content lane merged PR #8
(`feat/content-chem`) — MRB-281, C6 and C7, ten lessons and forty questions,
671 files. `git pull --rebase` replayed my commit cleanly on top; no conflict,
never force-pushed.

**No overlap, and it was checked rather than assumed.** They touched
`shared/ks3.css`, `shared/ks3.js`, `ks3_data/` and the `ks3/` output tree — none
of which this run edits, and three of which it is forbidden to. The one place
the two lanes could have collided is the new `shared/ks3-lesson-urls.js`, which
is generated from `ks3_data`: regenerated after the rebase and **byte-identical**
(183 lessons). C6 and C7 added content to existing lesson slots, not new slots.

---

### ⚠️ Design delivered the bench redraw MID-RUN — this is Mide's, not mine

At **16:44 tonight**, while this run was in progress, an untracked folder
appeared in the repo root: **`Student class view fixes/`**, with
`ks3-class-view-bench-done.html` and `ks3-class-view-bench-open.html`. It is
Design's answer to the very thing P4 says is coming.

**I have not ported it, and I have not committed it.** P4's ruling is explicit —
build an interim from existing tokens, "structure yours so their delivery
replaces it cleanly" — and the delivery is far larger than a done-state: six
themes with a new Harbour default, a flashcard deck, the nav "Recall" item
REMOVED, the recall round rebuilt as a standalone surface, and a reward slot.
That is a redesign, and adopting it is a product decision.

**It independently confirms three of tonight's rulings**, which is worth Mide
knowing:

| Design's note | tonight's ruling |
|---|---|
| §8 — "SIX A ROUND / SIX QUESTIONS removed from the recall header … only the live counter states a number" | P2, reached from the other direction |
| §6 — the done bench, one line: "Good week, AY." | P4 |
| "THEME PERSISTENCE … write the student pref to `data-bench-theme`" | P7 — this is the job Settings gets back |
| "REWARD SURFACE … `bench-reward-slot` is a real, empty 64px region" | the prompt's noted-and-NOT-built reward surface |

Design's §"CODE'S JOB" also asks for a recall bank of hundreds with six drawn
per round, weighted to what the student got wrong, "and never repeat inside a
round". That does not conflict with P2 — for a large bank both say six — and the
never-repeat property already holds.

I have used one thing from it: the done-state COPY, so the interim reads like
the real one and the swap is a component change rather than a rewrite.

