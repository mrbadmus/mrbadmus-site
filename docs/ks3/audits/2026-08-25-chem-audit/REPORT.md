# Chemistry audit — consolidated report — 25 Aug 2026

Ten unit auditors, C1–C10, 57 lessons, both personas per lesson, live-vs-local
byte parity proven for every page before driving. All counts below are
recomputed from the ten record files in `records/`, not from the auditors'
summaries.

**Recomputed totals: 106 findings — 25 × S1 · 28 × S2 · 11 × S3 · 42 × S4** —
plus 3 "ruled items causing observed harm" entries (inputs for Mide, not
defects) and a unit-by-unit safety-wording sign-off pile.

| Unit | Lessons | S1 | S2 | S3 | S4 | Total |
|---|---|---|---|---|---|---|
| C1 Particles | 6 | 5 | 2 | 2 | 6 | 15 |
| C2 Atoms, elements, compounds | 6 | 3 | 4 | 1 | 1 | 9 |
| C3 Mixtures and separation | 7 | 3 | 4 | 3 | 3 | 13 |
| C4 Chemical reactions | 5 | 1 | 3 | 0 | 4 | 8 |
| C5 Types of reaction | 5 | 0 | 1 | 0 | 4 | 5 |
| C6 Acids and alkalis | 7 | 6 | 2 | 1 | 3 | 12 |
| C7 Energy changes | 4 | 4 | 3 | 0 | 2 | 9 |
| C8 Periodic table | 7 | 1 | 2 | 2 | 11 | 16 |
| C9 Metals and materials | 4 | 1 | 5 | 2 | 1 | 9 |
| C10 Earth and atmosphere | 6 | 1 | 2 | 0 | 7 | 10 |
| **Total** | **57** | **25** | **28** | **11** | **42** | **106** |

---

## 1. The headline: is chemistry September-ready?

**Not yet — but it is one ruling session, one fix-run and one small Design
batch away from yes.** Nothing found requires a rebuild. The course's teaching
writing and instrument engineering are repeatedly described by independent
auditors as the best they have seen at this level (the C1 collision counter is
quantitatively honest on screen; C4's conservation bench, C3's chromatography
and melting-point benches, C8's oxide bench, C10's climate lesson all drove
clean and confront the classic misconceptions head-on). C5 and C10 are close
to clean.

What stands between here and yes:

1. **25 S1 science errors.** Almost all are one-sentence or one-constant fixes,
   but ~10 need a genuine ruling from Mide, not just a nod (§5A). The worst
   three: C6-11 (the catalysts lesson's discriminating experiment is invented
   chemistry — a real classroom run contradicts the page), C9-5 (a printed
   reactivity series ranks carbon below iron, contradicting the same unit's
   lesson 1 and making its lesson 3 impossible), and C7-07 (an endothermic hook
   claims a kitchen-accessible reaction does a demo it physically cannot do).
2. **Three drawings that teach the misconception their lesson exists to kill**
   (C1-08 state bench, C2-5 iron/sulfur dish, C3-09 filtration figure) — a
   contained Design batch (§4).
3. **One platform-wide navigation lie** — "Next in this unit" cards that send
   students backwards, out of the unit, and in two cases into biology, on ~23
   lessons across six units (SYS-1). Mechanical one-key fix.
4. **11 S3 functional bugs**, all small, two of which silently disable authored
   teaching (C8-7's misconception confrontation is emitted hidden forever;
   C8-6's rail can never complete).

The S2/S4 tail (70 findings) is polish and pedagogy tightening that can land in
a second pass without blocking September.

---

## 2. Systemic findings (cross-unit patterns — one finding each, full instance list)

### SYS-1 · "Next in this unit" heading lies about `references` links · S2 (worst instances) · ~23 lessons, 6 units

The end-matter card headed "Next in this unit" renders the lesson's
`references` (see-also) list. Wherever a reference is cross-unit or backwards
— which is most places — the heading is false: students are sent two lessons
back, into a different unit, or (c7-03) to two **biology** lessons, while the
correct "Where to next" card sits inches below contradicting it.

Instances (unit finding IDs): **C3-10** (c3-03, c3-05, c3-07 — 3 of 7 lessons),
**C4-1** (c4-01 → C3, c4-03 → backwards), **C5-1** (c5-01, c5-02, c5-04,
c5-05 — only c5-03 authors the honest "Connects to"), **C7-02** (all 4 C7
lessons; c7-03 lists two biology lessons), **C8-1** (all 7 C8 lessons; c8-01
also duplicates "Elements" under two headings), **C9-3** (all 4 C9 lessons;
c9-01 lists the same C5 lesson as both prerequisite AND next).
Evidence: `c5-combustion-endmatter-next-in-unit.png`,
`c7-l03-next-in-unit.png`, `c3-filtration-next-in-unit.png`, plus built-HTML
quotes in each record.

Proposed solution: change `connects_heading` to **"Connects to"** (the
convention already live on c5-03 and ~42 lessons) in every lesson file where
the reference is not genuinely the next lesson; de-duplicate references that
already appear under "Before this lesson" (c8-01, c9-01). One key per
`ks3_data/*/lesson_*.py`, rebuild once. Consider a build gate: a
`connects_heading` containing "Next" must point at the lesson the skeleton
says is next.
Who fixes: Code (standing authority). Effort: small (mechanical, wide).

### SYS-2 · Ladder kernel header claims a verdict mid-ladder · S4 · every lesson in the key stage

The shared ladder kernel's header flips from "Not started yet." to "You got
0 of 4. You marked rungs 3 and 4 yourself." the moment the FIRST rung is
answered — a past-tense finished verdict with three rungs untouched.
Instances recorded: **C2-3** (`c2-01-ladder-header.png`), **C3-02** (DOM
capture). Both auditors independently traced it to the shared kernel — one
branch fixes every lesson in both key stages.
Proposed solution: progress phrasing ("1 of 4 rungs done") while any rung is
unanswered; the tally sentence only at the end state. One branch in the
kernel's header function.
Who fixes: Code (standing authority). Effort: small.

### SYS-3 · KS3 header brand overflows at 390px · S3 · every KS3 lesson at phone width

At 390px the `.ks3-brand` box flex-shrinks to ~80px while the wordmark needs
177px; the breadcrumb trail renders ON TOP of it — an illegible jumble at the
top of every page, and phones are half the audience. Recorded as **C3-03**
(`c3-dissolving-header-390-top.png`), reproduced on c3-01 and on a B1 lesson —
shared header, platform-wide.
Proposed solution: `flex-shrink:0` / `min-width:max-content` on the brand and
truncate the TRAIL with ellipsis instead; or hide the wordmark below ~420px
leaving Design's chevron.
Who fixes: Code (standing authority). Effort: small.

### SYS-4 · Signed-out reload/state persistence is inconsistent — and inconsistently reported · S3 · platform-wide

**C1-05** reports a reload silently discarding ALL progress including typed
rung answers. C4, C5, C7 and C10's auditors, driving the same engine, verified
the opposite for typed answers: they SURVIVE reload via the `ks3_work_*`
localStorage store, while MCQ marks, rail ticks and instrument state reset by
design (MRB-208 — credit is a ratchet within a visit). C9 adds a nuance: the
engine SAVES a best score (`ks3_ladder4_*`) it never reads back on load.

So the consolidated picture: (a) the auditors contradicted each other on
whether typed answers persist — **resolved by the verification pass (25 Aug):
on C1's own particle-model lesson, a typed rung answer was saved to
`ks3_work_particle-model` and survived reload intact. C1-05's typed-answer
and "never saved locally" clauses are struck; C4/C5/C10's account is
correct.** What stands of C1-05 is the by-design part: (b) the deliberate
MRB-208 reset behaviour still costs a phone student their MCQ marks, rail
ticks and instrument progress on tab eviction mid-homework; (c) the
saved-but-never-read best score is dead weight either way.
Proposed solution: one platform ticket — decide what persists for signed-out
students (at minimum the two typed textareas everywhere, which most units
already have), rehydrate or delete the best-score write, and document the
ruling.
Who fixes: Code (standing authority), worth a ticket. Effort: medium.

### SYS-5 · Fixed instrument labels that lie at reachable edge states · S1–S3 · 5 units

A family, not a coincidence: benches compose fixed caption strings, and the
guards check verdict signs or value presence — never caption vocabulary — so
an edge state ships with a label that contradicts the data beside it.

Instances: **C7-04** (S1 — beaker 5 falls 20→12 °C under "rises to / HIGHEST
READING", at the lesson's handover moment; `c7-l02-bench-x5.png`),
**C3-12** (S1 — distillation gauges show end-of-run values from stage 1:
"Pure water" collected before anything has condensed;
`c3-distillation-stage1-gauges.png`), **C4-7** (S1 — "Flask, contents and
everything on the pan" over a 2.40 g metal-only reading;
`c4-l4-bench-mg-open.png`) with its sibling **C2-9** (S2 — same
magnesium-run convention jump, source-flagged F7; `c2-06-mag-sealed-jump.png`),
**C1-12** (S3 — "Twenty-four particles" resting note under a 12-particle
canvas; `c1-gp-hole-12particles-note24.png`), **C6-05** (S3 — "1 DROPS OF
ALKALI ADDED"; `c6-l3-dial-1drop.png`), **C3-07** (S4 — "insoluble" printed
twice in three clauses).
Proposed solution: fix each per its record, AND extend the bench guards the
way C7-04's record proposes — assert the rendered caption pair matches the
sign/state it describes, so the next bench with a falling run or an unusual
count cannot ship this again. A pluralisation branch in the dial renderer
covers the C6-05 class everywhere.
Who fixes: Code (standing authority); C4-7/C2-9's numbers need Mide sign-off.
Effort: small each; guard extension medium.

### SYS-6 · Drawings that vouch for the wrong model against their own lesson's words · S1–S2 · 4 units

Students hold the picture as authority over the words. Repeatedly, the drawing
(or its legend) asserts the exact misconception the text kills:

**C1-08** (S1 — solid drawn NOT touching under "all touching"; liquid drawn
sparse/clumped under "Same crowding" — the unit's most important finding;
`c1-slg-canvas-{solid,liquid,gas}.png`), **C2-1** (S1 — zoom frame labelled
1 nm holds ~13 atoms, ~3× off its own scale; `c2-01-zoom-crop.png`),
**C2-2** (S2 — glossy specular-highlight "copper atoms" beside text saying
atoms have no colour), **C2-5** (S1 — heating a lopsided iron/sulfur mixture
silently destroys the excess atoms, priming against the conservation lesson;
`c2-03-dish-mostlyiron-{before,after}.png`), **C2-8** (S2 — NaCl "giant
structure" is the only drawing with nothing visibly joined, beside molecule
views that draw bonds; `c2-05-builder-nacl-crop.png`), **C3-09** (S1 — a
"drawn to one scale" legend publishes schematic ratios beside a caption saying
"thousands of times wider"; `c3-filtration-particle-panels.png`),
**C10-02** (S4 — "drawn to scale" heading over a ~10× exaggerated crust, with
the confession locked behind completing the instrument;
`c10-inside-the-earth-layers-open.png`).

The model pattern already exists on-site: **c10-05's always-visible
distortion footer** directly under the mix bar ("Argon and carbon dioxide are
drawn wider on the bar than they really are…") — C10's auditor explicitly
names it the fix template.
Proposed solution: one Design batch (briefs in §4): redraw the three
packing/scale drawings, and adopt the rule *a legend never vouches for a
schematic ratio; every admitted distortion is confessed where the drawing is,
not behind a gate*.
Who fixes: Design brief, then Code; Mide sign-off on redrawn science. Effort:
medium (batch).

### SYS-7 · The course contradicts itself on tasting lab samples · S2 · C3 + C4, one ruling

c3-07 teaches, in so many words: "Nothing in a laboratory is tasted… an
unknown white powder is exactly the thing that can be poisonous." Meanwhile
FIVE sites credit or model tasting: c3-01 rung-3 criterion, c3-03 rung-3
criterion, c3-05 result panel ("Taste the distillate…") and rung-2 premise
(**C3-01**, with the c3-03 source explicitly defending the criterion), and
c4-01's salt evidence line "The solution still tastes of salt" one card away
from marble chips in acid (**C4-2**, whose source records the decision was
"reported to the commander"). This is a considered authoring position vs an
explicit safety rule — the unit keeps both. One Mide ruling decides which side
the course keeps, then Code applies it at all five sites.
Who fixes: Mide ruling (safety wording is his gate). Effort: small once ruled.

### SYS-8 · Answer tells in instruments outside the MRB-177/278 gates' reach · S2 · C4 + C10

The ladder's answer-position and length-tell gates do not cover benches or
hooks, and both leak: **C4-5** (S2 — the word-equation builder's chips render
reactants-first/products-middle/distractors-last in all three cases; a perfect
equation is scorable by position without reading), **C10-08** (S4 — hook's
correct option is 17 words with a qualifying clause vs 6–8-word flat
distractors; C10's record notes hooks are "evidently outside the predict
gate's reach, which is how it survived").
Proposed solution: shuffle builder bench order at build time (deterministic,
as MRB-278 already does for rungs); lengthen the C10 hook distractors; extend
the tell gate to hook options and bench chip order.
Who fixes: Code (standing authority). Effort: small each; gate extension
medium.

### SYS-9 · The assignment bank is outside every audit gate — and it shows · S1–S4 · C6 + C7

MRB-177 never swept the bank (known), and source-reading found three defects
in just two units: **C7-08** (S1 — feedback asserts "every one of them makes
something new" of endothermic changes, contradicting the unit's own
melting-is-endothermic + physical-change teaching), **C6-12** (S2 — two
lesson-1-tagged questions require lesson-2 content: litmus colours, rain-CO2),
**C7-03** (S4 — "Two identical blocks… one has twice the mass"). Also
**C6-11**'s invented chemistry is repeated as fact in bank questions
c6-07-s02/h03.
Proposed solution: fix the four named items now; schedule a bank-wide fairness
and accuracy sweep as its own unit of work (the three-corpora note in memory
already frames it).
Who fixes: Code (standing authority); composition policy question inside
C6-12 may need Mide. Effort: small now, medium for the sweep.

### SYS-10 · End-matter "At GCSE this becomes" renders wrongly or stale · S4 · C1 + C8

**C1-06**: on five of six C1 lessons the card shows only a bare, lowercase
slug-derived link ("states of matter") while the authored `ks4_becomes` prose
sits unrendered in source — flagged there as awaiting a ruling; c1-06 shows
what the card should look like. **C8-15**: c8-01's card claims oxide-character
prediction is GCSE material, but c8-07 now teaches it as KS3 (PT.06 closed
23 Aug) six lessons later in the same unit.
Proposed solution: rule the rendering (show `ks4_becomes` as body with links
beneath), trim c8-01's line to the metallic-bonding half.
Who fixes: Mide ruling (rendering), then Code; C8-15 Code alone. Effort: small.

---

## 3. Per-unit findings (severity order; systemic items by reference only)

### C1 — Particles and their behaviour (15 findings; record `records/c1.md`)

- **c1-08 · S1** — state-bench canvas draws solids not touching and liquids
  sparse/clumped, contradicting the lesson's own text; draws the exact
  misconception the unit exists to kill. → SYS-6; Design brief D1 (§4).
- **c1-14 · S1** — "perfume crosses a 4 m still room by diffusion in two
  minutes" is off by orders of magnitude for pure diffusion; five touch-points
  (big question, hook, scale card, rung 3, plus c1-06 observation 2). Fix:
  soften per the record's proposal. Who: **Mide ruling**. Effort: medium
  (wording only, five sites must stay consistent).
- **c1-01 · S1** — rung-4 model answer: "the space [between gas particles] is
  smaller than a particle" — real gas spacing is ~10× particle diameter. Fix:
  reword criterion per record. Who: Code + Mide sign-off. Small.
- **c1-02 · S1** — think reveal: cutting a sugar particle gives "carbon,
  hydrogen and oxygen… one of them is a gas" — wrong mechanism and wrong
  count; already queued for Mide's gate. Who: **Mide ruling**. Small.
- **c1-13 · S1** — "100,000 Pa… the weight of roughly ten metres of
  atmosphere" — 1000× short; it is the whole air column (≈ ten metres of
  water); passage contradicts its own follow-on arithmetic. Who: **Mide
  ruling**. Small.
- **c1-03 · S2** — cutting-bench readout walks mm → µm → nm with no scale
  scaffold at the lesson's central number
  (`c1-particle-model-cutbench-floor.png`). Fix: one comparison clause. Who:
  Code, wording past Mide. Small.
- **c1-15 · S2** — diffusion bench takes ~2 min (warm) to ~7–8 min (default
  cool) to reach "evened out", where the rail tick and the lesson's payoff
  live; nothing says warming shortens the wait. Fix options (a)–(c) in record.
  Who: **Mide ruling** on pacing, then Code. Small.
- **c1-05 · S3** — reload wipes progress → SYS-4. ⚠️ Partially struck by the
  verification pass: typed rung answers DO persist on this very lesson
  (verified live-parity build, `ks3_work_particle-model` rehydrates on
  reload); what stands is the MRB-208 instrument/rail reset cost on tab
  eviction, folded into the SYS-4 ticket.
- **c1-12 · S3** — 12-particle state falls back to the "Twenty-four particles"
  note → SYS-5. Fix: author the missing `fewer_particles` branch; sentence
  past Mide's gate. Small.
- **c1-04 · S4** — gap-canvas aria-label reveals the answer pre-choice to
  screen-reader users (pre-interaction DOM read: "…Right: the same picture,
  because the answer was that nothing is there."). Code. Small.
- **c1-06 · S4** — bare "states of matter" GCSE card, all six lessons →
  SYS-10.
- **c1-07 · S4** — key note assumes "tonight" (homework framing). **Mide
  ruling** (his flagged item). Small.
- **c1-09 · S4** — rung 2 asserts "a liquid cannot be squashed at all" two
  blocks after the lesson teaches "almost not at all" (same overstatement
  recurs in c1-06 observation 1 — fix together). Code + Mide sign-off. Small.
- **c1-10 · S4** — rung-2 feedback answers about an insulated "flask" the
  beaker-stem never described. Code + Mide sign-off. Small.
- **c1-11 · S4** — sugar "melts at 160 °C" (commonly quoted ~186 °C;
  160 °C is caramelisation, a chemical change, inside the
  melt-vs-dissolve lesson). **Mide ruling**. Small.

### C2 — Atoms, elements and compounds (9 findings; `records/c2.md`)

- **C2-1 · S1** — 1 nm zoom frame draws ~13 copper atoms; should be ~4
  (MRB-257's own correction never reached the drawing) → SYS-6; Design brief
  D2. Small.
- **C2-4 · S1** — "every one of the atoms in you was made inside a star" —
  false for hydrogen (~3/5 of the body's atoms, Big Bang). Fix: one clause per
  record. Code + Mide sign-off. Small.
- **C2-5 · S1** — iron/sulfur dish destroys the excess atoms on heating,
  contradicting its own weigh-test → SYS-6; Design brief D3. Medium.
- **C2-2 · S2** — glossy "shiny orange" atom spheres render the exact
  misconception the next block demolishes → SYS-6; Design brief D2 (same
  drawer). Small.
- **C2-6 · S2** — heated-dish caption "every iron atom joined to one sulfur
  atom" invites the molecule reading; row gaps read as floating chains. This
  is Design's requested examiner's-eye on her flag 8. Who: **Mide ruling**
  (his flag), then Design brief D3. Small.
- **C2-8 · S2** — NaCl lattice drawn unconnected beside bonded molecule views
  → SYS-6; Design brief D4. Small.
- **C2-9 · S2** — magnesium bench weighs metal-alone open (2.40 g) but whole
  apparatus sealed (152.00 g, the marble flask's reused numbers) → SYS-5.
  Who: **Mide ruling** (masses cross the examiner gate), then Code. Small.
- **C2-3 · S4** — ladder header mid-ladder verdict → SYS-2.
- **C2-7 · S3** — NaCl canvas caption drawn under the atom rows, illegible
  (worse at 390px; `c2-05-builder-nacl-crop.png`,
  `c2-05-mobile-builder-crop.png`). Fix: reserve a caption band. Code. Small.
- *(Ruled-harm entry: flat formulae erase the big-vs-small-number distinction
  in c2-05's ladder — §5D.)*

### C3 — Mixtures and separation (13 findings; `records/c3.md`)

- **C3-12 · S1** — distillation still's three gauges jump to end-of-run values
  at stage 1 ("Pure water" collected before anything condensed) → SYS-5. Fix:
  per-gauge stage thresholds (data model already has per-gauge `reads`). Code,
  behaviour past Design. Medium.
- **C3-09 · S1** — filtration figure's "drawn to one scale" legend publishes
  schematic ratios beside "thousands of times wider" — reinforces MIX-07 →
  SYS-6; Design brief D5. Small.
- **C3-05 · S1** — "calcium sulfate… plates out inside kettles" — kettle
  scale is calcium carbonate via decomposition, not retrograde solubility.
  **Mide ruling** (drop "kettles and"). Small.
- **C3-01 · S2** — taste credited as a test at four C3 sites while c3-07
  teaches the opposite rule → SYS-7. **Mide sign-off**.
- **C3-11 · S2** — crystallising bench: a post-run dial move silently
  withdraws Run with no affordance; the auditor's own scripted pass never
  found the re-arm and never saw the lesson's payoff
  (`c3-evap-bench-run-withdrawn.png`). Fix: one line in the Run slot. Code,
  wording past Design. Small.
- **C3-13 · S2** — the distillation lesson ships with NO apparatus diagram;
  the unit's one declared figure is status "needed" and renders nothing; the
  brief already exists in source. Design brief D6. Medium.
- **C3-06 · S2** — rung 4 requires the gas-solubility fact taught only in
  Going-further, below the ladder. **Mide ruling** (may be intended
  transfer). Small.
- **C3-03 · S3** — 390px header overlap → SYS-3.
- **C3-04 · S3** — rail stop "3 BENCH" is a silently dead link while the bench
  is gate-locked. Fix: point locked stops at the gate anchor. Code
  (engine-level). Small.
- **C3-10 · S3** — "Next in this unit" mislabels on 3 of 7 lessons → SYS-1.
- **C3-02 · S4** — ladder header tense → SYS-2.
- **C3-07 · S4** — "insoluble" duplicated in the chalk verdict seam → SYS-5
  family. Code. Small.
- **C3-08 · S4** — filtration summary calls the just-used paper "clean, dry,
  empty". **Mide ruling** (science wording). Small.

### C4 — Chemical reactions (8 findings; `records/c4.md`)

- **C4-7 · S1** — magnesium open run: 2.40 g presented as a whole-pan reading
  under "Flask, contents and everything on the pan" — physically impossible,
  and the sealed run reads 250.00 g under the same note → SYS-5. Fix:
  vessel-inclusive readings preserving the +1.60 g delta. Code + **Mide
  sign-off** on the new numbers. Small.
- **C4-5 · S2** — builder bench chip order fully positional in all three
  cases → SYS-8. Code (build-time shuffle in ks3_art/c4.py). Small.
- **C4-8 · S2** — big-2 verdict claims "Two hydrogens and two oxygens on each
  side" — false for both the drawn state (2 vs 4 H) and the final equation
  (4 H each side), at the legal-vs-illegal-move comparison
  (`c4-l5-forbidden-big2.png`). Fix per record. Code, flag to Design, Mide
  sign-off on the counting sentence. Small.
- **C4-3 · S2** — hook says gas balloons are "both weightless in the hand" in
  the lesson's own voice — plants REACT-07 two lessons before c4-04 confronts
  it; source-flagged. **Mide ruling** (Design's approved copy). Small.
- **C4-1 · S4** — "Next in this unit" mislinks (c4-01 cross-unit, c4-03
  backwards) → SYS-1.
- **C4-2 · S4** — salt card credits tasting as evidence → SYS-7. **Mide
  sign-off**.
- **C4-4 · S4** — oxygen chip ink 3.64:1 contrast, below WCAG AA, in Design's
  shared element-colour table destined for C8/KS4 reuse
  (`c4-l2-stage1-loose.png`). Design brief D7 — fix once before it is
  inherited. Small.
- **C4-6 · S4** — hook headline "Twenty-two words" over a 25-word quote, on
  the page teaching precision about sentences. Code, flag to Design. Small.
- *(Ruled-harm entry: flat formulae in c4-05's ladder on the page teaching
  big-vs-small numbers — §5D.)*

### C5 — Types of reaction (5 findings; `records/c5.md`) — the cleanest unit

Unit science is exceptionally clean: every classic misconception predicted
pre-audit is actively confronted on-page; zero console errors, zero 390px
breaks.

- **C5-5 · S2** — the classifier's lede promises "a defensible second answer"
  on the awkward items, but the thermite reveal never credits a student who
  answers Oxidation — the move the lesson's own think-again teaches
  (`c5-which-reaction-i6-oxidation-press.png`). Fix: one clause mirroring
  item 1's own pattern. **Mide ruling** (wording), then Code. Small.
- **C5-1 · S4** — "Next in this unit" false on 4 of 5 lessons → SYS-1.
- **C5-4 · S4** — displacement pattern panel opens at ANY 12 of 16 cells
  (diagonals count), so it can narrate tubes not yet run
  (`c5-displacement-pattern-at-12.png`). Fix: count only the 12 decidable
  cells. Code. Small.
- **C5-3 · S4** — sort item s4 says "Baking powder" where the instrument
  teaches "baking soda" — a different kitchen substance whose rise is partly
  acid–carbonate. **Mide ruling** (science call), then Code. Small.
- **C5-2 · S4** — three clean-beaker complete-combustion runs pair "None —
  the beaker stays clean" with the soot-definition note → SYS-5 family. Fix:
  per-run note as the hydrogen runs already do. Code. Small.

### C6 — Acids and alkalis (12 findings; `records/c6.md`) — most S1s of any unit

- **C6-11 · S1 — the audit's single most serious finding.** The catalysts
  lesson's discriminating fifth flask asserts dilute acid speeds up H2O2
  decomposition (19 cm³ vs control's 2 cm³, "consumed as it goes"). Real
  chemistry: acid STABILISES peroxide; a teacher who runs this bench gets a
  flat contradiction of the page, and bank questions c6-07-s02/h03 repeat the
  invented premise as fact (`c6-l7-bench-acid.png`). Two honest repairs
  sketched in the record; whichever is chosen must update the bank in step.
  **Mide ruling**. Medium.
- **C6-04 · S1** — L3's rule "an acid and a base always make the same two
  things" is contradicted by the unit's own L1 (calcium carbonate named a
  base) and L5 (acid + carbonate → three products). Fix: scope to "alkali".
  Code + Mide sign-off. Small.
- **C6-09 · S1** — L6 teaches "add copper oxide until no more will DISSOLVE"
  (hook + method step) — the dissolve/react blur the unit itself polices in
  L1 and L5. Fix: "react" in both places. Code + Mide sign-off. Small.
- **C6-02 · S1** — "a hundred thousand times more acidic than vinegar" —
  the page's own factor-of-ten rule and L1's vinegar pH 3 make it a thousand
  (`c6-l2-battery-acid.png`). Code + Mide sign-off. Small.
- **C6-08 · S1** — "Seawater is mildly acidic" in L4's stretch — seawater is
  pH ~8.1, and L5 phrases the same chemistry correctly. Fix: drop the acidity
  claim. Code + Mide sign-off. Small.
- **C6-01 · S1** — L1 calls "most of what you drink" neutral (pH exactly 7) —
  plants the near-7-is-neutral error its own bank question penalises. Code +
  Mide sign-off. Small.
- **C6-10 · S2** — naming bench's generic excess-and-filter note fails for
  sulfuric + calcium carbonate (insoluble product; the method doesn't work;
  known GCSE question; `c6-l6-namer-caco3.png`). Fix: special-case the note
  into teaching. Code + Mide sign-off. Small.
- **C6-12 · S2** — two lesson-1 bank questions need lesson-2 content →
  SYS-9. Code; composition policy may need Mide. Small.
- **C6-05 · S3** — "1 DROPS OF ALKALI ADDED" → SYS-5. Code. Small.
- **C6-03 · S4** — bench heading promises a "drop the indicator" step that
  doesn't exist. Code. Small.
- **C6-06 · S4** — 0-drop state card says alkali "will be DESTROYED on
  contact" on the page whose key fact is "Nothing is destroyed". Code. Small.
- **C6-07 · S4** — salt defined as "an acid loses its hydrogen TO a metal" —
  invites hydrogen-sticks-to-metal; collides with L4. Code + Mide sign-off.
  Small.
- *(Ruled-harm entry: 60-char Complete gate leaves a correct 55-char answer
  with a dead button and no signal — §5D.)*

### C7 — Energy changes in reactions (9 findings; `records/c7.md`)

- **C7-04 · S1** — beaker 5 falls 20→12 °C yet the readout says "rises to /
  HIGHEST READING 12 °C" — wrong-direction labels at the lesson's handover
  moment → SYS-5. Fix: derive labels from the sign as the verdict already is;
  extend the guard. Code. Small.
- **C7-07 · S1** — hook credits citric acid + bicarbonate with the
  freeze-beaker-to-bench demo (that is barium hydroxide's, ≈−20 °C;
  citric/bicarb cannot go sub-zero — the previous lesson's own bench runs the
  same mixture 20→12 °C). Kitchen-accessible: students will try it. Two
  options in record; option (b) would need new safety wording. **Mide
  ruling**. Small once ruled.
- **C7-06 · S1** — stretch: "energy coming out of the chemical bonds" — the
  bonds-as-store phrasing AQA penalises, on a page that defines "chemical
  store" correctly. Fix: one phrase. Code (note to Mide). Small.
- **C7-08 · S1** — bank c7-03-h03 feedback claims every endothermic change
  "makes something new" — contradicts the unit's own teaching → SYS-9. Code.
  Small.
- **C7-01 · S2** — hook and rail promise four flat minutes at 0 °C; the
  instrument and its own closing panel count three. Fix: prose follows the
  instrument. Code. Small.
- **C7-02 · S2** — "Next in this unit" lists other units' and two biology
  lessons → SYS-1.
- **C7-05 · S2** — subtitle "Nothing was added — so where does the heat come
  from?" un-learns C5's oxygen-is-added teaching. Code + Mide sign-off on
  wording. Small.
- **C7-03 · S4** — bank stem "Two identical blocks… one has twice the mass" →
  SYS-9. Code. Small.
- **C7-09 · S4** — two hook groups report +7 °C, equal to the "unreachable"
  true value (`c7-l04-hook-plus7.png`); one resolution phrase fixes it and
  teaches resolution. Code. Small.

### C8 — The periodic table (16 findings; `records/c8.md`)

- **C8-8 · S1** — aluminium readout: "the last [metal] to be discovered" —
  false, and directly contradicted by c8-02's gallium-1875/germanium-1886
  story one lesson earlier. Fix per record. Code. Small.
- **C8-4 · S2** — Mendeleev gap-filler prints the 1871-vs-1886 answers table
  on-screen below the three untouched prediction cards, spoiling the central
  predict-into-the-unknown move (`c8-mendeleev-gap-before-predictions.png`).
  Fix is trivial (emit hidden, reveal with the close panel) but the static
  table is documented as intended. **Mide ruling**. Small.
- **C8-2 · S2** — bench Sample A: "Bends around a former without cracking" —
  workshop jargon that parses as broken English, on the first card a student
  decides. Code. Small.
- **C8-6 · S3** — c8-03's TABLE rail stop can never tick — rail maxes at 4/5
  for every student; the authored rail is missing the `mirrors:"s-hook"` key
  its wiring assumes (`c8-groups-and-periods-rail-stuck-4of5.png`). One-line
  fix. Code. Small.
- **C8-7 · S3** — c8-03's PTAB-06 confrontation panel (#table-close, "The
  group number is not how many electrons the atom has") is emitted hidden and
  nothing ever reveals it — a registered misconception confrontation no
  student will ever read; the gate resolves ids, not reachability. Code.
  Small.
- **C8-1 · S4** — "Next in this unit" on all seven lessons → SYS-1.
- **C8-3 · S4** — prev/next chain follows unit numbering while the taught
  skeleton is year-ordered: c8-01's "Previous" is a Year 9 lesson. Affects
  every seam where year and number disagree. **Mide ruling** (sequencing
  rule). Medium.
- **C8-5 · S4** — hook's compressed period skips the non-metals ("…ordinary
  metals, then a violent gas"). Code. Small.
- **C8-9 · S4** — "non- metals" broken-string rendering in group 3's family
  line. Code. Small.
- **C8-10 · S4** — hydrogen's readout asserts the alkali-metal family banner
  before the "not a metal" note takes it back. Code. Small.
- **C8-11 · S4** — trough resting line teaches the spoiling order ("Choose a
  metal, predict, then drop it in" — choosing IS the drop). Code. Small.
- **C8-12 · S4** — "Iodine water" row header vs the cells' own "iodine
  solution". Code. Small.
- **C8-13 · S4** — "they want opposite things" — the atoms-want teleology,
  immediately followed by the correct mechanism. Code. Small.
- **C8-14 · S4** — flipped "Unreactive" card leaks the internal anchor id
  "#s-uses" into student-facing text (`c8-group0-s-uses-leak.png`). Code.
  Small.
- **C8-15 · S4** — stale "At GCSE this becomes" → SYS-10. Code. Small.
- **C8-16 · S4** — c8-07 burns magnesium and sulfur with an empty
  `safety_note` while every other demonstration lesson carries one. **Mide
  sign-off** (he authors the line). Small.

### C9 — Metals and materials (9 findings; `records/c9.md`)

- **C9-5 · S1** — L2's printed series strip ranks carbon BELOW iron,
  contradicting L1's series and the fact L3's extraction bench stands on; no
  card or gate can expose it — the wrong model works perfectly
  (`c9-l2-strip-carbon-below-iron.png`). Fix: re-rank (no observation,
  count or equation changes). Code + **Mide sign-off** (science content).
  Small.
- **C9-1 · S2** — L1 bench's "Say it before you look" predict step is
  decorative: tube click reveals instantly, commitments never checked and
  silently wiped (`c9-l1-bench-reveal-without-predict.png`). Fix: borrow
  c9-02's commit-then-reveal engine. Code. Medium.
- **C9-2 / C9-8 · S2** — read/found cells look identical to unread on the L1
  and L3 benches ("9 of 12 read" with no way to find the remainder; the
  payoff is gated on completion, so the stall lands at the end). L4's job
  buttons share the pattern — one shared paint fix covers all three benches.
  Code. Small.
- **C9-4 · S2** — rung 4 turns on "displaced from its sulfate", a word this
  lesson never glosses. Code. Small.
- **C9-3 · S2** — "Next in this unit" on all four lessons; L1 lists the same
  C5 lesson as prerequisite AND next → SYS-1.
- **C9-6 / C9-7 · S3** — all 10 word equations on L2+L3 render live as raw
  Python list literals — `['zinc + copper sulfate', 'zinc sulfate + copper']`
  on screen, no arrow, in the one place the lessons model the word-equation
  form (`c9-l2-eq-python-list.png`, `c9-l3-eq-python-list.png`). Repo-wide
  grep confirms the leak is confined to these two C9 renderers. Fix: format
  `eq[0] → eq[1]` as c9-01's renderer does, plus a build-time "no text node
  contains `['`" assertion so the class cannot ship again. Code. Small.
- **C9-9 · S4** — all 24 L4 verdict titles stack articles ("Polythene for the
  A bottle for a fizzy drink"). Fix: compose "%s — %s". Code. Small.

### C10 — The Earth and its atmosphere (10 findings; `records/c10.md`) — near-clean

Every classic misconception predicted pre-audit is actively confronted; all
instruments drove clean; zero console errors, zero 390px overflow.

- **C10-07 · S1** — bench draws new aluminium at 45 MJ/kg (below PET's 85)
  while the bauxite panel calls it "one of the most energy-hungry processes"
  (`c10-planet-limits-bench-al90.png`). Fix: raise to ~170/8.5 — keeps every
  ruled sentence (95% / "a twentieth") true, restores the real ordering,
  touches nothing else. **Mide sign-off** (values), Code executes. Small.
- **C10-04 · S2** — rock-bench Sample 6 lists "Was originally mudstone" as an
  observation — half the answer stated as evidence, undercutting the
  texture-decided-it payoff. Fix: observable clue per record. Code + Mide
  sign-off. Small.
- **C10-10 · S2** — "isotopes" arrives undefined in the climate lesson's
  strongest evidence card (KS4 word; one-clause gloss fixes it). Code + Mide
  sign-off. Small.
- **C10-02 · S4** — layers-bar heading claims "drawn to scale" over a ~10×
  exaggerated crust; the confession unlocks only after all four layers —
  c10-05's always-visible footer is the right pattern → SYS-6. **Mide
  ruling** (adjusts Design's drawn heading). Small.
- **C10-01 · S4** — inner core "roughly the size of the Moon" (≈70% of its
  width). Code + Mide sign-off. Small.
- **C10-03 · S4** — "behaving like plastic" unglossed in the hook. Code.
  Small.
- **C10-05 · S4** — "gneiss" unglossed in a misconception-resolving reveal.
  Code. Small.
- **C10-06 · S4** — key-fact card omits cementation; p4 tab reads
  "Compaction" only, against the lesson's own insistence on the pair. Code.
  Small.
- **C10-08 · S4** — hook option length tell → SYS-8. Code. Small.
- **C10-09 · S4** — "bya"/"mya" chips never expanded. Code. Small.

---

## 4. The Design brief pile

Each written ready to send. All are contained changes to existing drawers in
`ks3_art/`; Mide sees redrawn science before ship.

**D1 — C1 state bench packing constants (c1-08, S1).** Redraw the spacing:
solid = particles on a grid at pitch ≈ 1.0–1.1 diameters (edges touching),
rows filling the box; liquid = the SAME number of particles as the solid, same
touching density, disordered, below the surface line, voids no bigger than ~1
particle; gas unchanged. Vibration amplitude in the solid < 0.2 diameter so
the lattice never looks loose. Contained in the state-bench drawer's spacing
constants. Evidence: `c1-slg-canvas-{solid,liquid,gas}.png`.

**D2 — C2 zoom lattice (C2-1 + C2-2, S1+S2).** Final zoom level: ~4 atom
diameters spanning the frame width (2 rows visible) to match its own
"0.000001 mm" label — or relabel "0.000003 mm" (redraw preferred: atoms should
feel bigger at arrival). Same brief: flat-fill the spheres (drop the specular
highlight) and add one mono caption line inside the frame: "the colour is a
label, not what an atom looks like" (Design's wording). Evidence:
`c2-01-zoom-crop.png`.

**D3 — C2 iron/sulfur dish heated state (C2-5, S1; + C2-6 after Mide rules
his flag 8).** When a lopsided ratio was chosen, draw the 1:1 lattice AND the
unreacted excess (leftover grey circles clustered at the dish edge, labelled
"left over, unreacted"); at half-and-half draw the pure lattice as now. Turns
the drawing into positive evidence for its own weigh-test. Plus (post-ruling)
caption to ratio language and close the row gaps so the lattice reads as one
connected solid. Evidence: `c2-03-dish-mostlyiron-{before,after}.png`.

**D4 — C2 NaCl giant-structure view (C2-8, S2).** Draw the lattice circles
touching (as c2-03's after-state rows do) or add faint connecting strokes;
keep the no-molecule point by NOT grouping into pairs. Also reserve a caption
band so the caption never underlaps the atoms (C2-7 — Code can do the band).
Evidence: `c2-05-builder-nacl-crop.png` vs `c2-05-builder-water-crop.png`.

**D5 — C3 filtration particle-panels legend (C3-09, S1).** Keep the panels;
stop the legend vouching for the ratios. Replace "drawn to one scale · gaps 16
units · a grain of sand 22–30 · dissolved salt 7–10" with wording that says
the opposite ("both panels share one scale — but a real grain would be wider
than this whole page; no drawing can show it"), or add a broken-scale mark on
the sand lump. Dot sizes may stay; the false vouching line is the defect.
Mide signs the wording. Evidence: `c3-filtration-particle-panels.png`.

**D6 — C3 distillation apparatus figure (C3-13, S2).** The unit's one
declared figure (`c3-distillation-apparatus`, status "needed") renders
nothing — the distillation lesson has no drawing of a still at all. The full
brief already exists in the authored source
(`ks3_data/c3/lesson_05_distillation.py` lines 213–233: flask, side arm,
thermometer bulb at the still-head, Liebig condenser with counter-current
cold water in at the bottom/out at the top, anti-bumping granules).
Commission the drawer for `ks3_art/c3.py` and flip the status.

**D7 — C4 shared element-colour table, oxygen chip (C4-4, S4).** "O" ink
#FFFDF8 on #E4572E = 3.64:1, below WCAG AA. Either darken the chip ground
(e.g. #C33E1B ≈ 4.6:1) or switch the O chip's ink to near-black #1A1714 as
the H chip does. Fix once, in the one table, before C8/KS4 bonding inherit
it. Evidence: `c4-l2-stage1-loose.png`.

**D8 — flag, not a brief: C4-6 hook headline** ("Twenty-two words" over a
25-word quote) is Design's approved copy; Code will retitle to "Twenty-five
words" unless she prefers trimming the quote.

Also passing through Design for sign-off on feel/wording (Code executes):
C3-11's re-arm affordance line, C3-12's staged-gauge behaviour, c1-15(a)'s
diffusion pacing if that option is ruled.

---

## 5. The Mide pile

### 5A. Rulings needed (blocking the S1 fix-run)

1. **C6-11 — catalysts fifth flask.** The invented dilute-acid result (and
   bank c6-07-s02/h03). Choose repair (a) or (b) from the record. *The most
   consequential single item in the audit.*
2. **C7-07 — endothermic hook demo.** Keep citric/bicarb and tell the truth
   about it, or keep the freeze-to-bench climax and name barium hydroxide
   (teacher-only; needs new safety wording).
3. **c1-14 — "perfume crosses a still room in two minutes".** Five
   touch-points across two lessons; softened wording proposed in the record.
4. **c1-13 — "ten metres of atmosphere".** Proposed true replacement keeps
   the ten-metre image (as water).
5. **c1-02 — cutting a sugar particle "gives carbon, hydrogen and oxygen".**
   Already queued for the science gate.
6. **c1-11 — sugar "melts at 160 °C".** 186 °C, drop the number, or teach
   the caramelisation honesty.
7. **C2-6 — his flag 8:** iron-sulfide caption and lattice reading.
8. **C2-9 / C4-7 — the balance conventions** on the magnesium runs (both
   units show the same jump; rule one convention).
9. **SYS-7 — tasting.** One ruling covers c3-01, c3-03, c3-05 (×2), c4-01.
10. **C3-05** (kettle scale), **C3-06** (rung-4 transfer demand intended?),
    **C3-08** ("clean, dry" filter paper).
11. **C4-3 — "both weightless in the hand"** (Design's approved copy).
12. **C5-3** (baking powder vs soda), **C5-5** (thermite oxidation clause
    wording).
13. **C8-3 — the sequencing rule:** does prev/next follow the year-ordered
    skeleton or unit numbering? Affects every seam where they disagree.
14. **C8-4 — Mendeleev answers table:** documented-as-intended static render
    vs the trivial hide-until-predicted fix.
15. **C10-02 — layers heading** (adjusts Design's drawn heading).
16. **c1-06 / SYS-10 — render `ks4_becomes`?** The source asks for this
    ruling explicitly.
17. **c1-07** ("tonight"), **c1-15** (diffusion pacing option a/b/c).
18. **C6-12 policy question** — is the bank only ever served after a whole
    unit is taught? (Decides whether retagging is needed.)

### 5B. Science sign-offs (Code drafts, Mide nods — can be batched in one pass)

c1-01, c1-03, c1-09, c1-10 · C2-4 · C4-7 (numbers), C4-8 (counting sentence)
· C6-01, C6-02, C6-04, C6-07, C6-08, C6-09, C6-10 · C7-05, C7-06 · C9-5
(re-ranked strip) · C10-01, C10-04, C10-07 (energy values), C10-10 — plus the
redrawn D1/D3/D5 science before ship.

### 5C. Safety wording sign-offs (flagged per protocol; no rewrites proposed)

- **C2**: c2-03 fume-cupboard line (his flag 7); c2-06 "never seal a flask
  that is being heated".
- **C3**: c3-03 pond/river-water note; c3-04 bench hazard lines ×3 +
  over-heating warning + foot note; SYS-7 sites.
- **C5**: c5-01 foot note + fire-triangle close; c5-02 suck-back note; c5-04
  thermite note; c5-05's deliberate absence (auditor concurs).
- **C6**: all seven foot notes listed in the record, plus two gaps worth his
  eye (L1 bench eye protection; L3 hook demo not covered by the titration
  note).
- **C7**: c7-01, c7-02 (incl. quicklime register), c7-03 notes; c7-04's
  deliberate absence; new wording needed if C7-07 goes to barium hydroxide.
- **C8**: c8-01, c8-04, c8-05 notes (all read well per the auditor); c8-05
  chlorine-1915 stretch as shipped; **C8-16 — c8-07 has NO safety line while
  burning Mg and S; Mide to author one.**
- **C9**: c9-01 potassium cell + footer note; c9-02 thermite-excluded stretch
  + footer; c9-03 class-practical footer.

### 5D. Ruled items causing observed harm (inputs, not defect claims)

1. **Flat formulae (ruled) erase the exact distinction under test** in the
   two formula-teaching lessons: c2-05's ladder asks "What is the difference
   between 2CO2 and C2O4?" with every character the same size while option B
   speaks of big and small numbers (`c2-05-ladder-flat.png`); c4-05's ladder
   prints coefficient and subscript identically on the page whose whole
   argument is that they differ. Both records propose the same candidate
   resolution: keep stored strings flat (mirror consistency), render `<sub>`
   at display time in ladder options as the hooks already do — or add one
   sentence naming position as the cue. Mide's call entirely.
2. **The 60-character Complete gate** (his 19 Aug no-copy ruling): a genuine,
   correct 55-char answer leaves the button dead with no signal of any kind
   (`c6-l1-complete-dead-58chars.png`) — the terse-but-right writer is
   precisely who the threshold was meant to let through. C1's auditor watched
   the same gate and saw no harm; C6's evidence is concrete. A threshold
   nearer 40, or word-count, would have passed both real answers observed.

---

## 6. Proposed fix-run plan (Code, under standing authority, the moment Mide nods)

Order: S1 science first, then S3 bugs, then S2, then S4. One unit of work =
one commit = one push = verify live, per the autonomy contract. Rebuild via
`build_all.py` only; never `generate_site_v5.py` alone.

**Run 0 — the ruling session (Mide, ~1 sitting).** Everything in §5A, the
§5B nod-batch, §5C safety pile, §5D. Without this, only ~40 of 106 findings
are actionable.

**Run 1 — S1 wording fixes, no ruling needed beyond the §5B nod
(~15 edits, all small; est. one session).**
C6-01, C6-02, C6-04, C6-08, C6-09 · C7-06 · C8-8 · C2-4 · c1-01 · C9-5
(strip re-rank) · C10-07 (values as signed) · C7-08, C7-03, C6-12 (bank
items) · C4-8. Each is a one-sentence/one-constant edit in `ks3_data/`;
rebuild once, verify live once.

**Run 2 — S1 items unblocked by rulings (est. one session once ruled).**
C6-11 repair (+ its two bank questions, in step) · C7-07 prose swap · c1-14
five-site consistency edit · c1-13 · c1-02 · c1-11 · C4-7/C2-9 convention ·
C3-05 · C3-12 (staged gauges — the one medium item here).

**Run 3 — S3 bugs (est. one session).**
C9-6/C9-7 (equation formatting + the `['` build assertion) · C8-6 (one line)
· C8-7 (unhide) · C6-05 (pluralisation branch, checked across units) · C1-12
(wiring; sentence from Mide's gate) · C3-04 · C3-10 + the full SYS-1 sweep
(~23 lesson files, one key each) · SYS-3 header CSS · C2-7 caption band ·
SYS-2 kernel branch. SYS-4 becomes a platform ticket (medium, separate unit).

**Run 4 — S2 pedagogy (est. two sessions).**
C4-5 shuffle · C9-1 (commit gate — medium) · C9-2/C9-8 shared paint fix ·
C9-4 · C3-11 · C8-2, C8-4 (if ruled) · C6-10 · C10-04, C10-10 · C2-2/C2-6/
C2-8 land with the Design batch · c1-03 · c1-15 (as ruled) · C5-5 (as ruled)
· C3-06/C3-13 as ruled/drawn · SYS-8 gate extension (medium) · SYS-5 guard
extension (medium).

**Run 5 — S4 polish batch (est. one session).**
All 42 S4s not already swept up above — nearly all one-line: C5-2, C5-3 (as
ruled), C5-4, C8-5/9/10/11/12/13/14/15, C10-01/03/05/06/08/09, C9-9, C7-09,
C6-03/06/07, C4-6, C3-07/08 (as ruled), c1-04/06/07/09/10/11 (as ruled),
C2-3 (in SYS-2), C8-16 (Mide's line).

**Design batch (parallel with Runs 1–3).** D1–D7 from §4; Mide reviews
redrawn science; Code lands the drawer changes with the relevant run.

**Bank sweep (separate ticket).** SYS-9's full fairness/accuracy sweep of
`ks3_assignment_bank` sources — the audit only spot-checked two units and
found defects both times.

Total estimated effort: one Mide ruling session + roughly five Code sessions
+ one contained Design batch. September is reachable.

---

## 7. What the audit could NOT reach

All ten units reported; no unit is missing. Aggregated honestly from every
record's Unreachable section:

1. **The "Ask Mr Badmus AI" tutor chat round-trip** — on every lesson, no
   unit exercised it beyond opening the panel and verifying the control is
   wired. Sending messages POSTs anonymously to the production Claude
   backend; out of read-only scope (C1, C6, C7, C9 recorded it explicitly;
   the same applies platform-wide).
2. **Signed-in behaviour** — per-answer save, dashboards, class attempt
   recording, and the weekly-assignment surfaces that SERVE the question
   banks. Protocol forbids accounts. Bank findings (C6-12, C7-03, C7-08,
   C6-11's bank echoes) were evidenced from the authored source, which is
   the serving truth for those surfaces — but no auditor saw a bank question
   rendered to a student.
3. **Live-origin console state** — all units audited byte-identical local
   copies (parity proven per lesson via curl + cmp); localhost serving adds
   an origin-specific `/api/health` CORS log line absent on mrbadmus.com.
   Live-origin consoles were not separately driven.
4. **Evidence pruning result: nothing deleted.** All 61 files in `evidence/`
   are cited by at least one record's findings or evidence index, so none
   met the deletion criterion. Two caveats recorded instead:
   - `c3-pure-or-mixture-rung3-taste.png` (cited by C3-01) is a degenerate
     24×24 px, 116-byte capture — it cannot actually show the rung-3
     criteria list it is cited for. C3-01 stands on its quoted page text;
     if screenshot evidence is wanted for the ruling, recapture it.
   - Two files are cited only from evidence-index/walkthrough context rather
     than a numbered finding (`c5-displacement-mgzn-colourless.png`,
     `c8-oxides-cao-cuo-compare.png` — both retained as persona-2
     verification proof, per their records' explicit statements). Kept.
5. **One inter-auditor contradiction — now resolved**: C1-05 claimed typed
   answers are lost on reload; C4/C5/C10 verified persistence via
   `ks3_work_*` (SYS-4). The verification pass re-drove C1's own
   particle-model lesson (25 Aug): the typed answer was saved to
   `ks3_work_particle-model` and survived reload. C1-05's typed-answer claim
   is struck in this report (the record is kept as raw evidence); the SYS-4
   platform ticket scopes only the by-design MRB-208 resets and the dead
   best-score write.
