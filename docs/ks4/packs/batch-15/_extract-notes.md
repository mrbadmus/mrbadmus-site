> **Raw extraction notes, written before the examination.** Where they disagree with `examination/`, `FLAGS.md` or `00-BRIEF.md` (spec references, required-practical numbers, quiz-key alignment), those win.

# Batch 15 — extraction notes

Facts only, read straight from the 15 extracted files in
`04-checked-science-source/` (each file's header gives the routes; `##`
section presence gives everything else). No route-copy `quiz` section exists
in ANY of the 15 files — every route a lesson appears on serves the identical
TH quiz list, so "quiz count per route" below is one number covering every
route listed. The only field that ever differs by route is `higher`.

| # | Lesson | Routes | Quiz count (same on every route) | examiner_tip | fifas | equations | rp (verbatim) | variables |
|---|---|---|---|---|---|---|---|---|
| 1 | energy-stores-systems | CF CH TF TH | 2 | no | 0 | none | none | 1 |
| 2 | energy-changes-in-systems | CF CH TF TH | 2 | no | **1** | 1 — ΔE = m × c × Δθ | verbatim (RP14 — SHC with heater/thermometer/balance, see below) | 4 |
| 3 | energy-transfers-in-a-system | CF CH TF TH | 2 | no | 0 | none | none | 0 |
| 4 | circuit-symbols | CF CH TF TH | 2 | no | 0 | none | verbatim (RP15/RP16 — set up circuits, I–V characteristics, see below) | 0 |
| 5 | electrical-charge-current | CF CH TF TH | 2 | no | **1** | 1 — Q = I × t | verbatim (RP15 — series/parallel ammeter readings, see below) | 3 |
| 6 | current-resistance-pd | CF CH TF TH | 2 | no | **1** | 1 — V = I × R | verbatim (RP15 — V/I for components, R = V/I, see below) | 3 |
| 7 | direct-alternating-pd | CF CH TF TH | 2 | no | **1** | 1 — f = 1 ÷ T | none | 3 |
| 8 | mains-electricity | CF CH TF TH | 2 | no | 0 | none | none | 0 |
| 9 | power-electricity | CF CH TF TH | 2 | no | **1** | 4 — P=VI; P=I²R; E=Pt; E=VQ | none | 6 |
| 10 | energy-transfers-appliances | CF CH TF TH | 2 | no | **1** | 2 — E=Pt; Energy(kWh)=Power(kW)×time(h) | none | 3 |
| 11 | national-grid | CF CH TF TH | 2 | no | **1** | 2 — Vp÷Vs=np÷ns; P_lost=I²R | none | 6 |
| 12 | static-charge | TF TH | 2 | no | 0 | none | none | 0 |
| 13 | electric-fields | TF TH | 2 | no | 0 | 1 — E = F ÷ q | none | 3 |
| 14 | density-of-materials | CF CH TF TH | 2 | no | **1** | 1 — ρ = m ÷ V | verbatim (RP17 — regular/irregular solids + liquids, ρ=m/V, see below) | 3 |
| 15 | changes-of-state | CF CH TF TH | 2 | no | 0 | none | none | 0 |

Eight `fifas` lessons (#2, #5, #6, #7, #9, #10, #11, #14), matching BATCH-PLAN's
FIFA column exactly. The CFIFA form (step C) was appended to all eight files,
the four FIFA steps kept byte-identical, Convert step added to each.

**Two FIFAs needed a real conversion:** #5 electrical-charge-current
(minutes → seconds: 5 min = 300 s, before Q = It) and #10
energy-transfers-appliances, which needed TWO conversions in the same FIFA
(kW → W: 1.5 kW = 1500 W, AND minutes → seconds: 4 min = 240 s, before
E = Pt gives joules) — flagged as the first two-conversion FIFA seen in this
pack series. **Six needed none**: #2 (mass already kg, c already J/kg°C,
the 85−25=60 step is arithmetic inside the SAME equation, not a conversion),
#6 and #9 (V and I both already SI), #7 (T already in seconds), #11 (turns
are a dimensionless ratio, Vp already in V), and #14 density-of-materials —
worth flagging on its own: the question gives mass in g and volume in cm³
and asks for the answer in g/cm³, so nothing needs converting to kg/m³ at
all; a pupil who "corrects" to SI here would get the wrong-shaped answer.

## No equation-chaining found (rule 3)

None of this batch's 8 FIFAs chains two distinct equations — every one
applies a single formula (Formula → Insert → Fix → Answer), including #2's
Δθ = 85 − 25 sub-step, which belongs to the one equation ΔE = mcΔθ rather
than being a second formula. Nothing in this batch needs a "Step 1 … Step 2
…" treatment under the 2 Oct 2026 four-lesson-rules ruling.

## wrong_explanations key check

All 30 quiz items across the 15 files were checked mechanically: every item
has exactly 4 options, the `true` option sits at index 0 on all 30, and every
item's `wrong_explanations` keys match exactly the indices of its 3 wrong
options (`1,2,3`) — no shifted index anywhere. **No shifted-key defect found
anywhere in this batch.**

## Anything odd

1. **Spec-number agreement with BATCH-PLAN.md is perfect on slug/topic/route
   for all 15 of 15 rows, but the exact digit string differs by design on
   the 2 triple-only lessons.** `static-charge` and `electric-fields` are
   8463-only (BATCH-PLAN cites `— · 8463 4.2.5.1` / `4.2.5.2`, AQA's real
   separate-physics clause numbers), but the data's own `spec` field reads
   `6.2.5 (physics only)` / `6.2.6 (physics only)` — i.e. physics keeps its
   internal "6." prefix for EVERY lesson regardless of route and marks
   restriction with an inline `(physics only)` annotation, rather than
   switching to AQA's real 8463 "4." numbering the way chemistry's
   internal `4.x`/`5.x` split did in batch-14. This is a genuine difference
   in convention between subjects, not a data error — reproduced verbatim
   in both headers.

2. **FIFA/RP/equations columns match BATCH-PLAN exactly on all 15 rows** —
   no mismatch anywhere in this batch's plan at all (RP: #2, #4, #5, #6,
   #14 — 5 lessons, exactly as BATCH-PLAN's RP=Y column lists).

3. **No `examiner_tip` anywhere in this batch** — same pattern as every
   prior batch. All 15 files omit the `## examiner_tip` section entirely.

4. **Two filenames needed renaming** (step B): `physics-6.2.5 (physics
   only)-static-charge.md` → `physics-6.2.5-static-charge.md` and
   `physics-6.2.6 (physics only)-electric-fields.md` →
   `physics-6.2.6-electric-fields.md`. Both follow the rule exactly: spec
   digits only, the `(physics only)` annotation (not a spec digit) dropped
   from the filename but kept verbatim in the file's own header line.

5. **No subject:slug collisions were actually tested** — all 15 slugs were
   passed as `physics:<slug>` from the start (BATCH-PLAN marks every row
   `Phys`), so the extractor never searched biology/chemistry for them; the
   console output was 15 clean `wrote …` lines with no collision error
   printed for any slug.

6. **Only the two triple-only lessons carry a `higher` section**
   (`static-charge`, `electric-fields`) — every one of the other 13 lessons
   (all CF/CH/TF/TH) has NO `higher` field at all. This is the OPPOSITE
   pattern from batch-14, where every CF/CH/TF/TH lesson that had `higher`
   also had a sibling route to diff it against, and only one CH/TH-only
   lesson lacked `higher` entirely. Here, the 13 all-route lessons simply
   never carry higher-tier inline content in physics' electricity/particle-
   model topics, while the two triple-only lessons do (both render `null`
   on their Triple Foundation copy — see #7).

7. **Both `higher — Triple Foundation copy` sections render `null`** — no
   route actually diverges in its `higher` wording within this batch, same
   finding as every prior batch.

8. **No `canonical_record` WARNING was printed by the extractor** — the
   extraction run's console output was 15 `wrote …` lines and nothing else.

9. **All 15 lessons' routes match BATCH-PLAN's routes column exactly** — no
   CF/CH/TF/TH discrepancy anywhere.

10. **Three authored batch-2/batch-3 lessons already link forward to this
    batch's slugs.** `ks4_lessons/authored/batch-3/temperature-changes-shc.
    dc.html` links to `energy-changes-in-systems`, and `ks4_lessons/
    authored/batch-3/power.dc.html` links to `power-electricity`. (A fourth,
    `work-done-energy-transfer`, is a batch-16 slug also linked from
    `power.dc.html` — noted here because the search was run across both
    batches at once; see batch-16's own notes for its forward references.)
    These are navigation `hrefFor`/`endConnects` links, not diagrams, and
    confirm these lessons are expected destinations from already-built
    pages, not evidence toward the diagram-library audit.

11. **This batch spans three AQA topics** (energy §6.1, electricity §6.2,
    particle model §6.3) rather than one continuous topic. The
    diagram-library audit (see `05-diagram-library/README.md`) found this
    batch far better covered by existing drawing code than any prior batch:
    `figlib/physics.py`, `figlib/ks4phys.py` and `figlib/ks4elec.py` were
    all built with KS4 physics specifically in mind, and between them cover
    circuits, Sankey/energy-transfer diagrams, the heating curve, the
    particle-model states-of-matter figure and a dedicated radial electric
    field figure — a markedly lower proportion of genuine gaps than the
    chemistry batches 9–14 saw.
