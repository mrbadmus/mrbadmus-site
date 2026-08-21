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

