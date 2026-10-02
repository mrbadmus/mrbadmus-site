> **Raw extraction notes, written before the examination.** Where they disagree with `examination/`, `FLAGS.md` or `00-BRIEF.md` (spec references, required-practical numbers, quiz-key alignment), those win.

# Batch 17 — extraction notes

Facts only, read straight from the 16 extracted files in
`04-checked-science-source/` (each file's header gives the routes; `##`
section presence gives everything else). No route-copy `quiz` section exists
in ANY of the 16 files — every route a lesson appears on serves the identical
quiz list, so "quiz count per route" below is one number covering every route
listed. The only field that ever differs by route is `higher`, and (unlike
every prior batch) it does not always render `null` here — see note 6.

| # | Lesson | Routes | Quiz count (same on every route) | examiner_tip | fifas | equations | rp (verbatim) | variables |
|---|---|---|---|---|---|---|---|---|
| 1 | moments-levers-gears | TF TH | 2 | no | **1** | 2 — M = F×d; Σ clockwise = Σ anticlockwise | none | 3 |
| 2 | distance-speed-velocity | CF CH TF TH | 2 | no | **1** | 1 — v = d ÷ t | none | 4 |
| 3 | distance-time-graphs | CF CH TF TH | 2 | no | **1** | 1 — speed = gradient = Δd ÷ Δt | none | 3 |
| 4 | acceleration | CF CH TF TH | 2 | no | **1** | 2 — a = (v−u)÷t; v² = u²+2as | none | 5 |
| 5 | newtons-laws | CF CH TF TH | 2 | no | **1** | 1 — F = m × a | none | 3 |
| 6 | stopping-distance-braking | CF CH TF TH | 2 | no | **1** | 3 — stopping = thinking+braking; thinking = speed×reaction time; braking ∝ v² | none | 0 |
| 7 | pressure-in-a-fluid | TF TH | 2 | no | **1** | 2 — P = F÷A; P = h×ρ×g | none | 5 |
| 8 | momentum | CH TH | 2 | no | **1** | 3 — p = m×v; conservation; impulse F×t=Δp | none | 3 |
| 9 | upthrust-floating | TH | 2 | no | **1** | 1 — Upthrust = ρ×V×g | none | 4 |
| 10 | motion-in-a-circle | TH | 2 | no | 0 | none | none | 0 |
| 11 | transverse-longitudinal-waves | CF CH TF TH | 2 | no | 0 | none | verbatim (RP19/RP20 — slinky + ripple tank, see below) | 0 |
| 12 | properties-of-waves | CF CH TF TH | 2 | no | **1** | 2 — v = f×λ; T = 1÷f | verbatim (RP19 — ripple tank/oscilloscope, see below) | 5 |
| 13 | properties-em-waves-1 | CF CH TF TH | 2 | no | 0 | none | verbatim (RP20 — refraction through glass/perspex, see below) | 0 |
| 14 | wave-front-refraction | TH | 2 | no | 0 | 1 — v = f×λ (frequency unchanged) | none | 0 |
| 15 | properties-em-waves-2 | CF CH TF TH | 2 | no | 0 | none | none | 0 |
| 16 | radiation-balance-temperature | TH | 2 | no | 0 | none | none | 0 |

Ten `fifas` lessons (#1–#9, #12 in the table order above), matching
BATCH-PLAN's FIFA column exactly. The CFIFA form (step C) was appended to all
ten files, the four FIFA steps kept byte-identical, Convert step added to
each.

**No FIFA in this batch needed a real unit conversion.** All ten worked
examples give every quantity already in SI (N/m, m/s, kg/m³/N·kg⁻¹, s, kg,
Hz) — moments-levers-gears (N, m), pressure-in-a-fluid (m, kg/m³, N/kg),
upthrust-floating (m³, kg/m³, N/kg), distance-speed-velocity (m, s),
distance-time-graphs (m, s), acceleration (m/s, s), newtons-laws (N, kg),
stopping-distance-braking (m/s, s, m), momentum (kg, m/s) and
properties-of-waves (Hz, m/s). Turns on a transformer-style ratio do not
appear in this batch (that case is batch 18's `transformers`).

## One worked example chains two equations (rule 3)

**#6 stopping-distance-braking.** Its single FIFA's `F` step states BOTH
relationships at once — `Stopping distance = thinking distance + braking
distance` AND `thinking distance = speed × reaction time` — then genuinely
uses the second to compute thinking distance (the next `F` step) before
folding the first relationship's addition directly into the `A` step
(`12 + 40 = 52`) rather than giving it an `F` step of its own. This is a real
two-equation chain under the 2 Oct 2026 four-lesson-rules ruling (rule 3: "a
calculation that chains two equations… gets its own worked example, set out
as 'Step 1 … Step 2 …', before any pupil is asked to do one") — the same
shape batch-16 found in its `half-lives` FIFA, except there the second
equation got its own `F` step and here it is folded into `A` instead. Flagged
here for Design's lesson-writing to split properly, not silently ported as a
single FIFA. No other FIFA in this batch chains two equations.

## wrong_explanations key check

All 32 quiz items across the 16 files were checked mechanically: every item
has exactly 4 options, the `true` option sits at index 0 on all 32, and every
item's `wrong_explanations` keys match exactly the indices of its 3 wrong
options (`1,2,3`) — no shifted index anywhere.

Read by hand, one real content defect was found: **moments-levers-gears**,
quiz item 2 ("A bicycle is in a low gear…"), `wrong_explanations["1"]` reads
*"Small driving → large driven gear gives MORE SPEED not more force"* — this
is the OPPOSITE of the lesson's own theory text two sections earlier ("LARGE
GEAR driven by SMALL GEAR: Output gear rotates SLOWER but with MORE FORCE")
and of the quiz item's own marked-`true` answer ("turns slowly but with more
turning force"). The explanation does not refute wrong option 1 ("turns
faster than the pedals") — it agrees with it. A genuine
science-accuracy/internal-consistency defect in the verbatim source, kept
byte-identical here per the port rule; flagged for Mide's gate rather than
silently fixed. No other item in this batch showed a comparable
self-contradiction.

## Anything odd

1. **Spec-number agreement with BATCH-PLAN.md is good but not perfect.** 10 of
   16 rows match exactly (`distance-speed-velocity`, `distance-time-graphs`,
   `acceleration`, `newtons-laws`, `momentum`, `transverse-longitudinal-waves`,
   `properties-of-waves`, `properties-em-waves-1`, `properties-em-waves-2`, and
   `stopping-distance-braking` to the usual "less granular" degree). The
   `8463`-only lessons (`moments-levers-gears`, `pressure-in-a-fluid`,
   `upthrust-floating`) show the familiar "6." vs "4." convention difference
   already explained in batch-15/16's notes — not a mismatch. **Two rows are
   real wrinkles beyond that convention:**
   - `motion-in-a-circle`'s data `spec` is `"6.5.6"`, which BATCH-PLAN's own
     "Odd things" section (top-level `docs/ks4/BATCH-PLAN.md`) already lists
     by name as one of the data's KNOWN-WRONG spec entries — this extraction
     reproduces that documented defect exactly, it is not a new finding.
   - `radiation-balance-temperature`'s data `spec` is `"6.6.5.4"` against
     BATCH-PLAN's guessed `"8463 4.6.3.2"` — a two-level digit mismatch
     (`6.5`/`6.6` vs `4.6.3`), bigger than the usual single-digit wrinkle and
     NOT on BATCH-PLAN's documented-wrong list. Reported here as the same
     category of defect, unconfirmed against AQA's own numbering.
   `wave-front-refraction`'s data spec `"6.6.2 (HT only)"` is one digit short
   of BATCH-PLAN's own guessed, `?`-flagged `"6.6.2.2?"` — the same
   "data is less granular than BATCH-PLAN's own speculative number" pattern
   batch-16 found for `resolving-forces`/`free-body-diagrams`, not a fresh
   wrinkle.

2. **FIFA/equations/RP columns match BATCH-PLAN exactly on all 16 rows** — no
   mismatch anywhere in this batch's plan. RP: BATCH-PLAN marks exactly three
   lessons RP=Y (`transverse-longitudinal-waves`, `properties-of-waves`,
   `properties-em-waves-1`) and those are the only three files carrying an
   `## rp` section — exact agreement. **RP numbers are reused across
   different practicals within this batch**: `RP19` labels both the slinky
   demonstration (`transverse-longitudinal-waves`) and the ripple-tank wave-
   speed practical (`properties-of-waves`); `RP20` labels both the ripple-tank
   half of `transverse-longitudinal-waves`'s own text and the glass/perspex
   refraction practical (`properties-em-waves-1`). Reported as the data gives
   it — every RP number cited anywhere in this pack is **(frozen label,
   unverified)** against AQA's own numbering, verbatim from each file's `rp`
   field only.

3. **No `examiner_tip` anywhere in this batch** — same pattern as every prior
   batch. All 16 files omit the `## examiner_tip` section entirely.

4. **Six filenames needed renaming** (step B): the two `(physics only)`
   lessons (`moments-levers-gears`, `pressure-in-a-fluid`), the one lesson
   carrying both tags (`upthrust-floating`, `(HT only)`) and the three
   `(HT only)` TH-only lessons (`motion-in-a-circle`, `wave-front-refraction`,
   `radiation-balance-temperature`) all had their parenthetical annotation
   stripped from the filename (spec digits only), kept verbatim in the
   header. No filename collisions.

5. **No subject:slug collisions were actually tested** — all 16 slugs were
   passed as `physics:<slug>` from the start, so the extractor never searched
   biology/chemistry for them; the console output was 16 clean `wrote …`
   lines with no collision error printed for any slug.

6. **Nine of sixteen lessons carry a `higher` section**: `moments-levers-gears`,
   `distance-speed-velocity`, `distance-time-graphs`, `acceleration`,
   `newtons-laws`, `stopping-distance-braking`, `pressure-in-a-fluid`,
   `upthrust-floating`, `motion-in-a-circle` all render it as plain prose with
   no divergent copy, plus `wave-front-refraction`, `properties-em-waves-1`,
   `properties-em-waves-2` and `radiation-balance-temperature` (13 lessons
   total carry `## higher`; `momentum`, `transverse-longitudinal-waves` and
   `properties-of-waves` have none — these three are taught identically at
   Foundation and Higher with no HT extension). Nine lessons produce 16
   route-copy sections total (one TF copy each for the two 8463-only pairs
   `moments-levers-gears`/`pressure-in-a-fluid`'s TF route, one TH-only
   lesson with no copy at all, and CF+TF copies for the five CF/CH/TF/TH
   lessons that differ).

7. **⚠️ Unlike every batch through 16, not every route-copy here renders
   `null`.** `properties-em-waves-1` and `properties-em-waves-2` BOTH have
   real, non-null text in their Combined Foundation and Triple Foundation
   `higher` copies — and in both lessons the CF and TF copies are
   byte-identical to each other, but genuinely different wording from the
   canonical Triple Higher `higher` field (e.g. `properties-em-waves-1`'s
   TH copy is a long paragraph on total internal reflection and the critical
   angle; its CF/TF copy is three shorter sentences covering the same ground
   with different phrasing and no mention of "critical angle" terminology
   choice). The other 12 route-copy sections in this batch (across the other
   seven lessons that produce any) all still render `null`, continuing the
   pattern every prior batch found. This is a genuine, confirmed divergence —
   not a rendering artefact — and the two lessons that show it both sit on
   the EM-waves spec point (6.6.2.x); worth Design's attention when writing
   the Foundation route of either page.

8. **No `canonical_record` WARNING was printed by the extractor** — the
   extraction run's console output was 16 `wrote …` lines and nothing else.

9. **All 16 lessons' routes match BATCH-PLAN's routes column exactly** —
   including the three Triple-Higher-only lessons (`upthrust-floating`,
   `motion-in-a-circle`, `radiation-balance-temperature`) and the two-route
   8463-only pair (`moments-levers-gears`, `pressure-in-a-fluid`, both
   TF/TH) — no discrepancy anywhere.

10. **Five authored batch-2/batch-3 lessons already link forward to six of
    this batch's slugs.** `ks4_lessons/authored/batch-3/types-of-em-waves.
    dc.html` links to both `properties-of-waves` and `properties-em-waves-1`;
    `ks4_lessons/authored/batch-3/waves-detection-exploration.dc.html` links
    to both `transverse-longitudinal-waves` and `wave-front-refraction`;
    `ks4_lessons/authored/batch-3/sound-waves-hearing.dc.html` links to both
    `transverse-longitudinal-waves` and `properties-of-waves`;
    `ks4_lessons/authored/batch-3/particle-motion-pressure.dc.html` links to
    `pressure-in-a-fluid`; `ks4_lessons/authored/batch-2/lenses.dc.html`
    links to `wave-front-refraction`. All five are real `connects`/
    `endConnects` navigation arrays (`K.hrefFor`-gated), not diagrams —
    confirming these six slugs are expected destinations from already-built
    pages. No batch-18 slug is linked from anywhere in `ks4_lessons/
    authored/`.

11. **This batch spans two AQA topics** (forces §6.5 continuing from batch
    16, waves §6.6 starting fresh). KS3 precedent is strong but uneven:
    `ks3_art/p3.py` (Describing motion), `p4.py` (Forces) and `p1.py`
    (Energy transfers, for levers) cover most of the motion/forces half
    contingently; `p5.py` (Pressure) covers `pressure-in-a-fluid` and
    `upthrust-floating` contingently; `p6.py` (Waves and sound) and `p7.py`
    (Light) cover four of the six waves lessons directly or contingently.
    Three lessons have NO KS3 precedent at all: `motion-in-a-circle` and
    `momentum` (both genuinely KS4-only content, like batch-16's
    radioactivity), and `radiation-balance-temperature` — though for the
    last of these, a KS3 CHEMISTRY module outside this step's own
    `ks3_art/p*.py` brief, `ks3_art/c10.py`'s `r_greenhouse_steps`, teaches
    the identical absorb/re-emit/balance chain; named in
    `05-diagram-library/README.md` as a cross-subject find worth Design's
    attention even though it falls outside the brief's own search scope.
