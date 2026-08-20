# Student preview pages — parity report

**Date** 20 August 2026 · MRB-270 phase 8
**Against** Design's 19 August 2026 22:56 delivery, vendored at
`docs/ks3/design-reference/student/`
**Pages** `student/class-preview.html`, `student/assignment-preview.html`

The live pages — `student/class.html` and `student/assignment.html` — are
untouched. `build_student.py` refuses to write either, by name, and that refusal
is tested.

---

## 1. What matches Design's file

**At desktop, exactly.** Both pages, measured side by side with Design's own
standalone file in the same browser at 1460px:

| | Design | generated |
| --- | --- | --- |
| class view — nodes | 563 | **563** |
| class view — root box | 1460 × 2400 | **1460 × 2400** |
| assignment — nodes | 177 | **177** |
| assignment — root box | 1460 × 1200 | **1460 × 1200** |
| tag census | — | **identical, both** |
| visible text | — | **identical, both** |
| resolved font / ground / ink | Instrument Sans / #FBF3E6 / #221E1B | **identical** |
| horizontal overflow | none | **none** |

That is not a coincidence and not an effort. **The markup is Design's, not a
retyping of it.** `build_student.py` loads Design's standalone file in headless
Chrome, lets Design's own logic render it, and takes the DOM. The only way the
output can differ from Design's file is if Design's file changed.

Every section is registered and present — 30 named landmarks on the class view,
12 on the assignment — and the registry is checked in both directions, so it
cannot drift from the delivery either.

**One deliberate, measured improvement.** Design's standalone inlines every
font face as base64: 28 `@font-face` blocks, 1.63 MB, three quarters of the
page. Right for a file you double-click on a plane; wrong for a Year 7 on
school wifi. The site already self-hosts all seven faces at `/shared/fonts/`,
and every one is **byte-identical** to Design's copy — verified by sha256
across all seven, not assumed from the matching filenames. So the base64 comes
out and Design's own `fonts.css` goes in against the served path.

2.19 MB → **551 KB** (class view) and **404 KB** (assignment).

---

## 2. What does not match, and why

### 2.1 The class view scrolls sideways at 390px. Design's file does not.

| | scrollWidth | clientWidth | elements overflowing |
| --- | --- | --- | --- |
| Design's class view | 390 | 390 | 0 |
| generated class view | **610** | 390 | **101** |
| Design's assignment | 390 | 390 | 0 |
| generated assignment | 390 | 390 | 0 |

**This is structural, not a bug to fix in the generator.** Design builds
responsiveness two ways, and §6 of both handoff notes says so:

- everything **continuous** is a `clamp(min, Ncqw, max)` container query in the
  element's own inline style. These survive the snapshot perfectly, which is
  why the type and the padding do shrink at 390px;
- everything **discrete** is one of **ten** switches (eight on the assignment)
  computed in JavaScript from the measured root width. Design's own note calls
  these values ones that "cannot be interpolated": `benchCols`, `docketOrder`,
  `statsBasis`, `railDisplay`, `spineCols`, `rowCols`, `chaseCols`, `boardCols`,
  `recallCols`, `optCols`, `ghostRight`.

A photograph taken at 1460px carries the **desktop** value of all ten, baked
into the inline styles, and no later width changes them. The twelve-column term
spine alone needs 662px against Design's phone rule of two rows of six; the
work-row grid should drop from `46px 20px 1fr auto` to `18px 1fr auto`; the
docket should move above the copy. None of that happens, because none of it is
CSS.

The assignment is clean at 390px only because it is one question in a single
column — its eight frozen switches happen to overflow nothing. That is luck,
not correctness, and `student_parity.py` records it per page so that a
regression on either side is a failure.

**Not approximated, deliberately.** Hand-writing media queries Design did not
draw would disagree with the logic class the moment either changed. The
faithful fix is to reproduce the switch **table** — Design published all ten
values for all three bands — as a small runtime shim. That is behaviour, and
behaviour is §3.

### 2.2 There is no behaviour at all

The pages are a photograph of one state (`layout: Auto`, `classState: Work
set`, the assignment mid-way on Q07). None of Design's logic class comes with
the DOM. Specifically absent:

**Class view** — the recall round (pick, Check, per-distractor feedback, Next,
Skip, streak, round-score card), the term-spine week filter, the three work
tabs, work-row expand/collapse with the inline feedback panel, the bench task
ticks and their meter, the leaderboard's week chips and top-5/top-10 toggle,
the account sheet, `Clear filters`.

**Assignment** — select, **Confirm answer**, the marking moment and its five
option states, the explanation attached to the option, Back/Next, the marker
sheet, jump-to-question, the figure enlarge, the timer and its idle pause,
`NEXT UNANSWERED`, hand-in and the stamp, the end screen, review mode, offline
hold-and-drain.

### 2.3 There is no real data

Every name, score, date, lesson title and question on both pages is Design's
authored example content. Nothing is read from Supabase. `Ayo B.`, `Tiwa A.`,
`98 points`, `DUE THU 18 SEP`, the six recall questions and the fifteen
assignment questions are all fixtures.

### 2.4 Design's own open items, carried forward unchanged

These are Design's, listed in their READMEs, and none is resolved here:

1. **The class view says eight questions; the assignment is fifteen.** The
   docket (`QUESTIONS 8`), the bench task ("Answer the eight questions") and
   the blurb all need `assignment.questionCount`. Design has deliberately not
   touched the approved v1 file.
2. **`Open the assignment` is not wired.** Route `/class/8r-sc1/assignments/:id`.
3. **The leaderboard bar split is an approximation** drawn for layout only
   (`onTime = round(pts × 0.4)` capped at 40, `recall = round(pts × 0.19)`
   capped at 20, score the remainder). Real per-component values must come from
   the API. Design says explicitly: do not ship the approximation.
4. **`--st-ok-room: #55B36A` is not in the token files.** Design measured it at
   6.6:1 on `--st-room-panel` and asks for a line in `src-styles-tokens.css`.
   It is currently declared inline on the design root. **This is a ruling for
   Mide** — see §4.
5. **The recall questions and the assignment questions are authored examples.**
   The API must serve rungs 1–2 with all four per-distractor feedback strings.
   Design's note: "A question without all four is not shippable."
6. **The six figures are schematic stand-ins.** The frame, the
   `clamp(132px, 34cqw, 232px)` cap, `preserveAspectRatio="meet"`, the caption
   row and the enlarge tap are the specification; the drawings are not.
7. **Every date string is fixed.** Late, and the hand-in stamp, must come from
   the server clock, not the device's.

### 2.5 One claim in Design's notes that this run can now answer

Both READMEs say 360px is "verified in a desktop browser, not on a device", and
both call the open KS3 overflow ticket the reason to re-check.

**That KS3 defect does not exist.** Phase 6 drove all 295 built KS3 pages at
390px: `documentElement.scrollWidth` equals `clientWidth` on every one, and
every element wider than the viewport is already inside its own
`overflow-x: auto` scroller. MRB-229 fixed the header trail below 700px in
August and `shared/ks3.css` says so in as many words. The finding Design was
warned about was stale. A real-device check is still worth doing for the font
load; the KS3 precedent is not the reason.

---

## 3. What remains before these could replace the live pages

In the order they block each other.

1. **The ten breakpoint switches, as a runtime shim.** Without them the class
   view is unusable on the primary target width. Design published the complete
   table for all three bands, so this is transcription, not invention.
2. **The behaviour** in §2.2. This is the bulk of the work and it is what the
   snapshot approach explicitly does not provide. A decision is due here:
   either hand-port Design's logic class to vanilla JS the way KS3 instruments
   are written, or ship Design's own compiled bundle. The first is consistent
   with the rest of the platform and is a large build; the second is fast and
   puts React on a student page for the first time.
3. **Identity-scoped data**, per the brief: year scoping computed from the
   academic year's dates and never from `is_current`; a student sees only their
   own current-year class; no year picker; no meta-text explaining the
   platform; the Render URL called directly.
4. **Design's seven open items** in §2.4, including the eight-vs-fifteen
   question count and the leaderboard split.
5. **An end-to-end drive** against production, signed in, at 390px and desktop:
   reach the class, open the assignment, answer, submit, and confirm the rows
   land with the correct fields — including that a self-marked written rung
   records no correctness claim.
6. **Page weight.** 551 KB and 404 KB against the live pages' 56 KB and 11 KB.
   Most of the remainder is the design-system CSS bundle inlined whole, of
   which the pages mount exactly one component (`BrandMark`). Coverage-trimming
   it is straightforward once the behaviour is settled — not before, because a
   trim done against a static snapshot would drop every rule the interactive
   states need.
7. **The brand ruling** in §4.

---

## 4. Reserved for Mide

Two, and both are genuinely his.

**The student-surface brand.** The previews carry Design's orange double
chevron and the "MrBadmusAI" wordmark. `CLAUDE.md` splits the brand three ways
and puts "all current/future student dashboards" under the plain-white-text
dashboard rule — and the live `student/class.html` follows it, with no logo
asset at all. Design has drawn the opposite, deliberately, and says so: "Designed
to your reading that student surfaces are the student's own product surface. If
Mide reads the plain-white-text rule as covering these too, it is one component
swap in the header."

This is a product decision about what a student's own page is, not a technical
one. It is one swap either way, and it should be made before the pages ship
rather than discovered afterwards.

**`--st-ok-room: #55B36A`.** Design asks for one new token: a dark-room success
green, because `--ks3-ok` #12A150 measures 2.3:1 on `--st-room-panel` #1E1913,
under the 3:1 graphic threshold. Design measured the replacement at 6.6:1 and
scoped it to graphics only — bar segments, the recall tick, a 3px panel edge —
never text. It currently lives inline on the design root and wants a line in
`src-styles-tokens.css`.

The contrast arithmetic is checked and correct. What is Mide's is whether the
KS3 token set gains a colour, which is the kind of decision the frozen
reference exists to make deliberate.

---

## 5. How to check any of this yourself

```bash
python3 build_student.py     # regenerate both previews from Design's delivery
python3 student_parity.py    # A structural · B registrations · C the 390px gap
```

`student_parity.py` exits non-zero on any parity failure, any unregistered
section, any registration that has drifted from the delivery, and on the 390px
gap being **fixed** without this report being updated.
