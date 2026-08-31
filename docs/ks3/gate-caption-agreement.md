# The gate the estate does not have: caption-versus-data agreement

**MRB-297 · design note, 31 August 2026 · nothing is built yet, deliberately.**

This is a specification, not an implementation. It is written now because the
KS3 physics audit (MRB-294, 28 Aug 2026) found the class of defect it would
catch, found nine instances of it in one subject, and found that **no gate in
the repo can see any of them** — and a gate that important should be designed
on purpose rather than in the tail of a fix run.

---

## 1 · The finding that produced it

The physics audit's headline is one sentence:

> Nine benches across the estate behave perfectly while demonstrating the
> negation of the lesson beside them.

Read that carefully, because the important half is the first clause. These are
not broken instruments. The markup renders. The buttons respond. The arithmetic
is internally consistent. Nothing throws. Every existing gate is green. And the
model a child walks away with is the wrong one — frequently the exact
misconception the lesson registers itself as confronting.

Three examples, each from a different unit, each caught only by a human reading
the caption and the number in the same glance:

| Where | The caption says | The data says |
|---|---|---|
| `energy-transfers/heating-and-thermal-equilibrium` | *"the spark is the proof: the fastest particles on the bench, and almost no energy at all"* | spark **5 kJ**, bath **2 kJ** — the spark wins, 2.5 to 1 |
| `magnetism/magnetic-fields` | *"which is why that gap is the strongest part of the whole map"* | the compass reads **9.5** in the gap against **100.0** at the pole faces |
| `electric-circuits/resistance` | *"a large current"* / *"**only** 1.200 A… the reading is small"* | **0.300 A** called large, **1.200 A** called small — four times the current, called small |

The full list of instances the audit filed under this class is in
`docs/ks3/audits/2026-08-28-ks3-physics/REPORT.md` §4b (SYS-5) and §7 (F1b).

---

## 2 · Why no existing gate catches it

Not an oversight. Every KS3 gate is watching something real, and the defect
falls between all of them. This table is the argument for building a new gate
rather than extending an old one.

| Gate | What it asserts | Why this defect passes it |
|---|---|---|
| `ks3_parity` | the built page matches Design's drawing | the bench looks exactly as drawn; the drawing was never the problem |
| `ks3_instrument_liveness` | pressing a control changes the block's DOM | it changes. It changes to the **wrong** thing, and "changed" is the whole assertion |
| `ks3_overflow` | nothing escapes its box | nothing does |
| `ks3_smoke` | no `undefined`, no unsubstituted placeholder | every string is fully substituted; they are substituted with a falsehood |
| `verify_questions` | the bank's structure — twelve, four options, one correct, a real `why` | captions are not questions and are not in the bank |
| `verify_answer_positions`, `verify_answer_lengths` | no MCQ corpus lets position or shape answer the question | a caption is not an MCQ |
| `ks3_mutation` | a deliberate defect injected into the source is caught by some gate | it only catches what some gate already watches — this class is precisely the gap, so mutation testing is silent about it too |
| the per-drawer `raise ValueError` guards in `ks3_art/` | the **payload** is well-formed before drawing | they run at build time on authored data. Most of these captions do not exist at build time: they are composed in `shared/ks3.js` at runtime from bench state |

The last row is the crux and it is worth stating on its own.

> **The lying caption usually does not exist until a student presses something.**
> `wireTwoQuantities`, `wirePrismBench`, `wireCompassGrid` and their siblings
> build the sentence from live state. A build-time check reads the authored
> payload — which is honest — and never sees the string the child reads.

So the gate has to be a **driving** gate (headless Chrome, `speed="slow"` in
`gate_registry.py`), and it has to reach states, not pages.

---

## 3 · What it would check

Six sub-checks, ordered by how mechanical they are. The first three need no
authoring at all and would have caught roughly half the instances on their own.

### 3.1 · Quoted value (fully mechanical)

**Every number that appears in a caption must appear in a readout in the same
state, or be derivable from the readouts by one arithmetic step.**

Catches `P6-08` directly: the slinky bench's note declares the amplitude as
**60 mm** and asserts it as the maximum, while the readout one tile away says
**57 mm** at every one of 21 reachable slider positions. The number 60 appears in
no readout in any state, so the check fires without anyone teaching it physics.

### 3.2 · Printed arithmetic (fully mechanical)

**A rendered `a ⊕ b = c` must satisfy it.**

Catches `P5-12` (`2.4 − 10 = 7.6` printed as the page's own model working) and
`P8-03` (the mantissa of a prefixed answer printed as the quotient, false in 7
of 14 reachable states). The audit already proposed this one separately, in
F1c; it belongs here because it is the same idea at its simplest, and because
building it inside this gate gets it the state enumeration for free.

Add the companion assertion the audit names beside it: **no student-facing text
node may match `/\de[-+]?\d/`** — a float that reached a page in exponent form.

### 3.3 · Superlative (mechanical, one lexicon)

**A caption asserting that the current state is the largest / smallest /
strongest / fastest / furthest of something must be true of that state's own
readouts.**

Catches `P10-8` (*"the strongest part of the whole map"* where the bench reads
9.5 against 100.0). Needs a small lexicon of superlative forms and a rule for
which readout each refers to — which in practice is "the one numeric readout in
the same block", and where it is ambiguous the gate should say so rather than
guess.

### 3.4 · Comparative vocabulary (a lexicon, and a threshold table)

**A size adjective must agree with the value it sits beside, and must agree
with itself across states.**

This is `P8-05`, the most consequential instance in the audit: the adjective is
keyed to the component's *authored band* rather than to the current on screen,
so 0.300 A is "a large current" and 1.200 A is "only… small". The check is not
"is 0.3 A large" — that is unanswerable in the abstract. It is the far easier
**monotonicity** question:

> Within one bench, if state X is called *large* and state Y is called *small*,
> then X's value must exceed Y's.

That formulation needs no physics and no thresholds at all, and it is exactly
what fails here. It also catches `P1-15` (*"the water barely warms"* over a
12 °C → 38 °C rise) as soon as a gentler pair exists on the same bench to
compare against.

### 3.5 · Universal claim (needs full state enumeration)

**A caption containing *every*, *always*, *never*, *all* or *each* must hold in
every reachable state, not merely the authored one.**

Catches `P12-05` — *"Move the slider and every bar changes"*, false in **all 16
states**, because the slider changes no bar at all. Catches `P5-07`'s *"every
single time"*. This is the sub-check that most needs the enumerator of §4 to be
exhaustive rather than sampled: a universal claim is only refuted by the state
that refutes it.

### 3.6 · Direction and sign (per-bench, the least mechanical)

**A caption naming a direction, a sign or an ordering must agree with the
computed one.**

Catches `P9-14` (*"from the positive charge towards the negative one"* printed
beside a computed reading of *"to the left"* with the negative charge on the
right), `P10-11` (*"tips over by 0° … with its north-seeking end down …
because the field is not parallel to the ground"* — four statements wrong at
one latitude) and, in its geometric form, `P7-22`, the prism drawing dispersion
backwards.

This one cannot be generic. The honest shape for it is the pattern the drawers
already use: **a per-instrument assertion, written by whoever owns that
instrument, run by this gate.** `ks3_art/p7.py` should assert that the
highest-frequency ray lands further from the undeviated line than the
lowest-frequency one. `r_two_quantities` should refuse a payload whose
largest-amount-at-lowest-temperature store does not exceed its
smallest-amount-at-highest-temperature store — *because that ordering is the
lesson*. Neither is generic and neither should be.

So the gate is really two halves: **five generic checks, plus a registry of
per-instrument invariants that the gate runs and the registry cannot silently
lose** — the `gate_registry.py` lesson applied one level down.

---

## 4 · What it would cost

The expensive part is not the checks. It is **state enumeration**, and most of
it already exists.

| Piece | State | Note |
|---|---|---|
| Drive every lesson in headless Chrome | **exists** | `verify_ks3.py`, `ks3_instrument_liveness.py` |
| Find every instrument block on a page, derived not listed | **exists** | `ks3_instrument_liveness.py` since MRB-282 — derives from `ks3_art.load().kind_shell` and `ks3_data.build_units()`, 21 units, 157/157 families |
| Press every control | **exists, partly** | liveness presses *the first control that looks like one* and asserts the DOM changed. `student_controls_drive.py` presses every control on the student pages and is the closer model |
| Enumerate the **cross product** of a bench's controls | **does not exist** | this is the new work, and it is where the cost is |
| Read captions and readouts out of a state | **trivial** | they carry `data-*` hooks already (`data-twoq-out`, `data-prism-out`, `data-oflow-note`, …) |
| The five generic checks | **new, small** | each is tens of lines once the state tuples exist |
| Per-instrument invariants | **new, ongoing** | one per bench that has an orderable claim; not all do |

**The cross product is the real question.** P1's two-quantities bench is 3 × 3 =
9 states and can be enumerated exhaustively. P10's compass grid is 100. P7's
prism is inputs × second-prism. A bench with two continuous sliders is
unbounded. So the enumerator needs a declared budget per bench and a documented
sampling rule where exhaustive is impossible — **and it must report which
benches it sampled rather than enumerated, by name**, or it becomes the
eleventh gate whose output overstates its own scope.

**Rough cost, honestly bounded:**

- The enumerator, with the budget and the by-name sampling report: **2–3 days**.
  This is the load-bearing piece and it is worth building well, because
  everything else in this note is cheap once it exists — and because a second
  gate will want it.
- Checks 3.1, 3.2, 3.3: **1 day** together. Fully mechanical.
- Check 3.4 (monotonicity within a bench): **half a day**, plus the lexicon.
- Check 3.5: **half a day**, but only meaningful with an exhaustive enumerator.
- Check 3.6: **not a fixed cost.** One invariant per bench, written with the
  bench, roughly an hour each. The nine benches the audit names are the
  starting set.
- Baselining the estate the day it lands: **1–2 days**, because it will be red
  on arrival across all three subjects and every red needs reading before it is
  either fixed or recorded as debt. Budget it; it is the step that is always
  underestimated.

Call it **a week to a first green run over KS3**, most of it in the enumerator,
and the per-instrument invariants accumulating afterwards.

---

## 5 · The three things that would make it fail as a gate

Recorded now, because each has already happened to a gate in this repo.

1. **Partial coverage that reports as total.** `ks3_instrument_liveness` ended
   runs with *"every registered instrument responded to its own controls"*
   while covering 31 families of 158. This gate must print what it did **not**
   reach, by name, every run — the benches it sampled, the captions it could
   not associate with a readout, the units with no built pages.
2. **Being unrunnable, and therefore unrun.** It is a slow gate. Slow gates get
   skipped unless `prepush_gate.py` demands a receipt bound to the exact tree,
   which is the mechanism that already exists. It needs a `gate_registry.py`
   row on the day it lands, not after.
3. **Guessing at agreement.** Where the gate cannot tell whether a caption and a
   number agree, it must say *"could not decide"* and count that as a finding
   about itself, not as a pass. A caption checker that silently passes what it
   does not understand is worse than none, because it retires the human reading
   that currently does the work.

---

## 6 · Why it is worth a week

The audit's own summary of this class:

> That is the worst failure mode this protocol exists to catch, because it is
> invisible to every gate in the repo: the code is correct, the numbers are
> internally consistent, and the model the child walks away with is wrong.

Thirteen auditors reading at student pace over one subject found nine. Biology
and chemistry have never been read for this class specifically. The defect
survives every automated check we have, survives screenshots, survives parity,
and is found only by a person who reads the sentence and the number together
and notices they disagree.

That is not a thing to keep buying by hand, one subject at a time.
