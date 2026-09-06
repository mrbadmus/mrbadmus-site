# My classes — Design's card list against the built page

**MRB-326 JOB 5.** Column 1 is Design's v3 classes screen in DOM order
(`Teacher Dashboard.dc.html`, `sc-if isClasses`, node 157 and its subtree).
Column 2 is what the built page carried BEFORE this run
(`teacher_fixtures/classes-fixture.html` plus the live screenshot at
`v3 targets/Screenshot 2026-09-06 at 05.22.41.png`). Column 3 is the verdict.

**Mide's rule for the card, verbatim from the JOB 5a brief:** *"A card = class
name + the '14 students · no work set' chip (or the homework-this-week block) +
the activity line. Nothing else."*

---

## 1. The screen

| # | Design (node) | Live state before this run | Verdict |
|---|---|---|---|
| 1 | eyebrow "AUTUMN TERM · 2026–27" (161) | present | MATCHES |
| 2 | `<h1>` My classes (162) | present | MATCHES |
| 3 | `classLine` "12 classes · 227 students" (163) | present | MATCHES |
| 4 | **Set work** (165) | absent | REMOVED — `DEAD`, MRB-287. |
| 5 | **Weekly digest** (166) | present | MATCHES |
| 6 | **Import students** (167) | present | MATCHES |
| 7 | KS tabs All / KS3 / KS4 (170–171) | present | MATCHES |
| 8 | `shownLine` "12 shown" (172) | present | MATCHES |
| 9 | Sort — Class code / Most missing (174–176) | present | MATCHES |
| 10 | card grid, `minmax(310px,1fr)`, gap 16 (177) | present | MATCHES |
| — | — | empty-filter panel | RULED ADDITION — `INSERT_AT (158, 177)`. STAYS. |
| 11 | "Viewing 2026–27" · **Previous years** (203–206) | present | MATCHES |
| — | — | year-switch strip | RULED ADDITION — `INSERT_AT (203, 206)`, MRB-261, marker `year-open`. STAYS. |
| — | — | `#state-empty`, `#state-error`, `#year-band`, `#year-switch` | RULED ADDITION — live regions, hidden until needed. STAYS. |

## 2. The card itself (node 179 and below)

| # | Design (node) | Live state before this run | Verdict |
|---|---|---|---|
| 1 | class code, 33px (181) | present | MATCHES |
| 2 | **`c.meta` eyebrow (182)** — "14 STUDENTS · SCIENCE" | present, exactly that | **REMOVED (redundancy)** — JOB 5a. The count is printed again on the chip eleven pixels below ("14 students · no work set"), and the subject is already in the class code above (MRB-263, `7h/Sc5`). Node pruned by the new `REDUNDANT` table, the `meta` property deleted from the `cards` builder, and `BIND_ATTR[182]` deleted with it. |
| 3 | `<if c.live>` block — "HOMEWORK THIS WEEK" + `weekLabel` "2 of 2 in" + bar + `weekSub` (183–190) | present | MATCHES |
| 3a | `weekSub`, all-in arm — "Everyone in — nothing to chase" (190) | present | **REMOVED (redundancy)** — JOB 5b. `weekLabel` on the row directly above already reads "2 of 2 in". The *node* stays: its other arm ("Chase Jasmine O, Kaleb A +3 more") names children and repeats nothing. |
| 4 | `<if c.noWork>` chip — `emptyLine` "14 students · no work set" + **Set work** (191–194) | chip present, button absent | MATCHES / button REMOVED — `DEAD`, MRB-287. |
| 5 | `<if c.empty>` chip — "No students yet" + **Import** (195–198) | present | MATCHES |
| 6 | footer — `c.activity` "LAST ACTIVITY 13 DAYS AGO" + chevron (199–201) | present | MATCHES |

A card now reads, top to bottom: **class code → homework chip or block →
activity line.** Nothing else, which is the rule.

## 3. The byte guard, flipped

`build_teacher_port.py` carried a guard on this line that has now been flipped
twice, and both flips are recorded in place rather than rewritten over:

* **originally (MRB-287 E1)** — refuse a build where the card meta did NOT
  state the class's own academic year, catching a card that read the
  dashboard's *working* year instead;
* **MRB-325 ruling 8** — flipped to refuse a build where it DID
  (`c.yearName` must not appear), because the year became a page-level fact
  stated once;
* **MRB-326 JOB 5a, this run** — the substring test is gone, because there is
  no line left to test a substring inside. Looking for `c.yearName` inside a
  `meta:` that no longer exists would pass by finding nothing, which is the
  exact failure mode the whole rulings file is written against. It now asserts
  **absence plus the ruling's own presence**: `c.meta` may not appear anywhere
  in ANY of the six emitted pages (the `cards` builder ships on all of them),
  AND the sentinel `MRB-326 JOB 5a` must be in the emitted logic — so a build
  where the `LOGIC` anchor silently stopped matching cannot read as a build
  where the line was removed.

The class-HEADER guard below it keeps the substring shape and gains a second
row: `k.subject` may no longer appear in `klass.meta` either (JOB 4e).

## 4. Cousins of "nothing to chase", and what happened to each

Mide's rule: these become the numeric form ("2/2 in") counted from data —
EXCEPT where the same count is already displayed immediately beside them, where
the sentence is simply cut, because the numeric form would repeat the number.

| String | Where | Outcome |
|---|---|---|
| "Everyone in — nothing to chase" | class card, `cards.weekSub` | **CUT.** `weekLabel` on the row above reads "2 of 2 in". |
| "Everyone's in — nothing to chase." | class detail, node 238, `glance.allIn` | **CUT.** The card's 34px `openIn` three lines above reads "4 of 4 in". |
| "All N homeworks in — nothing to chase" | Design's `TODAY_LESSONS` map | Already gone — `LOGIC` replaced that whole block with `const lessons = []` under MRB-306 (the four lessons were invented). Nothing to do. |
| "N of M in · nothing to chase" | **`teacher/today.html:1273`** | **NOT TOUCHED — another lane owns Today.** Listed for the commander. It is already the numeric form with a sentence appended; whether the tail survives is that lane's call. `today_drive.py:437` asserts `"nothing to chase" in t`, so changing it means changing that drive too. |

Both cut cases produce an empty string rather than a deleted property:
`weekSubFg` still colours it, `c.live` still gates the block, and the div's own
`margin-top:8px` collapses to nothing with no text in it — measured, not
assumed.
