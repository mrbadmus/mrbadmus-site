# MRB-220 — build contract for B2, C1 (rebuild) and C2

One document that the engine pass and the sixteen authoring passes both build against, so a
kind name, a shell choice or a payload key is decided **once** rather than sixteen times.

Written 16 Aug 2026 by the MRB-220 commander, from Design's three `NOTES-*.md`, the three
`*-inventory/PAYLOAD-MAP.md` measurements, and the generator as it stands on `main` at
`a4109aae6`.

**If this document and a payload map disagree, the map wins on measurement (what Design drew)
and this document wins on naming and schema (what we call it and how it is authored).** Where a
map records something this contract has not anticipated, follow the map and say so in the report.

---

## 0. File ownership — who writes what

| Files | Owner |
|---|---|
| `build_ks3.py`, `shared/ks3.css`, `shared/ks3.js`, `ks3_parity.py`, `verify_ks3.py` | **The engine pass, alone.** No authoring pass edits these. |
| `ks3_data/b2/`, `ks3_data/c1/`, `ks3_data/c2/` and their unit wrappers | **The authoring passes**, one lesson per module, no two passes in one file. |
| `docs/ks3/*` | Commander. |

An authoring pass that finds it needs an engine change **does not make it**. It records the need
and authors against this contract's schema. A schema that turns out to be wrong is one report line;
two passes editing `build_ks3.py` at once is a lost afternoon.

---

## 1. Rulings that bind, and are not re-argued

- **MRB-205** — Design draws, we render. No invented component, block type, layout or page
  structure. Behaviour, physics and detail may be added *inside* a component Design drew where the
  page is silent; an addition may never contradict the page. **Page wins over engine.**
- **MRB-204 as amended 15 Aug 2026** — every formula gets its own block alone, a drawn diagram, a
  staged-reveal worked example, then the student fills the steps before any independent question.
  **TRIANGLE for products** (`A = B × C`). **BALANCE-BEAM / part–whole BAR for sums and
  conservation statements.** A triangle on a sum teaches a false relationship.
  → `c2-06` is a SUM. It gets the beam and the bar. This is settled; see §4.
- **MRB-208** — the trail is carried inline in the header, never a separate breadcrumb row. The
  progress rail is completion-based, never scroll-based, on **both** the ≥1340px side rail and the
  narrow top bar, and **nothing is ticked on load**. KEY FACT is a cream band, 2px ink outline,
  hard orange offset shadow, mono label, display type — **never amber**.
- **MRB-210** — one microscope depth-of-field table for all of KS3: `0.100 mm` at ×40 total,
  `0.040` at ×100, `0.008` at ×400. No unit re-declares it.
- **MRB-196 R10** — CLASSIFY's sort and CONTRAST's settles-it get a lightweight self-check: the
  student is asked whether they had it and answers for themselves. **No green, no red, nothing on
  the option button.** Every other activity kind: no per-option feedback at all.
- **Only the ladder marks correctness** — green tint + drawn ✓ for right, dark ✕ for wrong, never
  the accent for either. **Amber is a wrong IDEA being confronted, never the student.**
- **Sequence is data** — year and half-term never appear in a lesson URL or in a lesson page's
  bytes. Write "a student your age", never "a Year 7".
- **§8.10, no platform self-explanation** — student pages carry no meta-text about how the platform
  works. Default is cut. Legal/safety notes stay, small, at the bottom edge, never a callout.
- **Prose bar** — if a sentence is not teaching or setting up a decision, cut it.
- **Every lesson carries `Draft — not yet science-reviewed`.**

---

## 2. Commander's rulings made for this run

These are decisions the run needed and did not have. Each is recorded so it is not re-taken.

**R1 — `#s-think` is a rail stop in B2, C1 and C2, and renders as `predict`.**
B1's `confrontation` kind deliberately emits no `data-stage-done`, because on B1's approved pages
`#s-think` is static markup with no gate — there is nothing to complete. On these three units'
pages `#s-think` asks for a commitment (options, then a gated reveal), which is a `predict`. A
block that demands a commitment and then reveals **is** a completed activity, and MRB-208 says the
rail is completion-based. So: author these as `predict`, and they tick. This is not a reversal of
B1's ruling; it is the same rule meeting a different block.

**R2 — `done_when` becomes load-bearing in the GATE, not in the runtime.**
`done_when` is authored on every rail stage of every lesson, serialised into `data-rail-stages`,
and read by **nothing** — the runtime decides completion from `data-stage-done` and DOM
heuristics in `doneByDom()`. It is a dead authored key on all twelve live lessons.
B1's own source records the symptom it causes: *"a stage that can never tick"*.

It is **not** wired into the runtime in this run. Re-deriving completion from a declared string
would change ticking behaviour on twelve lessons that are live, verified and in front of students,
to fix a defect that is invisible to them. Instead `verify_ks3.py` gains an assertion that every
declared `done_when` names a condition the page can actually reach, and that every rail stage can
reach done. A wrong value then fails the build, which is what "wired" has to mean for the field to
be worth authoring. Runtime unification is a follow-up ticket, not this run's business.

**R3 — the shipped stylesheet wins over per-page KEY FACT drift.**
Design's B2 pages draw the KEY FACT box with a `6px 6px` shadow, 25px body and `22px 26px`
padding; `shared/ks3.css` ships `5px 5px`, 22px and `18px 22px`. One stylesheet serves all 183
lesson slots, so adopting the page's values restyles B1 — six lessons Mide has already approved —
to match four he has not seen. The ruled *identity* of the box (band ground, 2px ink outline, hard
**accent** offset shadow, mono label, display statement, never amber) is what MRB-208 fixes, and
the shipped CSS satisfies all of it. The numeric drift is recorded in the report as drift, and it
is Mide's to rule on if he wants the page's figures.

**R4 — a defect on an approved page that a ruling already covers is corrected, not reproduced.**
`b2-03` starts its animation loop without consulting `prefers-reduced-motion` (it reads
`this.reduced` once at construction and never checks it in the tick), where `b2-02` does check.
Reduced motion is an accessibility contract, not a matter of taste, and the same page's sibling
implements it correctly — so this is a slip, not an intention. Corrected in the engine, reported.

**R5 — no key is authored without a read site, in the same pass.**
The B1 replay shipped 234 authored keys of which 146 were read by nothing, one of them an approved
science correction that therefore never reached a student. `ks3_key_audit.py` gates this run:
`python3 ks3_key_audit.py B2 C1 C2`. If a key has no read site, either wire the read or do not
author the key. "It documents intent" is not a read site — put it in a comment.

**R6 — the nav brand tile is PARKED and stays parked.**
Design's B2/C1/C2 pages draw the brand as a cream `#FBF3E6` chevron inside a 34px `#E4572E`
tile. MRB-197 (Mide's ruling) is an accent chevron on the ground, and that is what `NAV_BRAND`
emits for all 294 KS3 pages. These three deliveries are **evidence added to the parked entry in
`architecture.md` §8**, not authority to change the mark. Do not adopt the tile. Do not delete the
note.

---

## 3. Where a lesson record goes

Follow B1 exactly (`ks3_data/b1/`), which is the current pattern and supersedes the single-file
shape:

```
ks3_data/b2/__init__.py                  # lessons(), + _normalise() lifting instruments
ks3_data/b2/lesson_01_what_the_skeleton_does.py     # exports LESSON
...
ks3_data/biology_b2_movement.py          # thin UNIT wrapper: from .b2 import lessons
```

C1 is a **rebuild over a live unit**: `ks3_data/chemistry_c1_particles.py` loses its inline
lessons and becomes the wrapper, exactly as `biology_b1_cells.py` did. The superseded bodies stay
reachable in git history — that is the record, and nothing is deleted to tidy up.

**Slugs are permanent (§8.4) and must match `ks3_data/structure.py` character for character.**
They are the join for scheme-of-work rows, progress records and every `requires` edge. Titles may
differ from `structure.py`; slugs may not.

> Known title divergence, for the report, not for silent correction: `structure.py` names C1 L6
> *"Testing the model: does it explain everything?"*; Design's page titles it *"Testing the
> model"*. The page is what a student reads.

**Every student-facing string is lifted byte-identical** from the approved page, via
`node tools/extract_design_payload.js <page> [CONST...]`. Extracted JSON for all sixteen pages is
already in the run's scratchpad. Never retype science-bearing copy; a typo in retyped prose is
invisible and crosses the examiner gate.

---

## 4. The kind roster

`segment` is the SHELL the block renders in and it is a real decision, not a label: `practical` is
ink-dark, `check` is a plain light `ks3-block`. B1 got two of six wrong and it took a layer-C
assertion to catch — an instrument painted on the wrong ground. **Measure the shell from Design's
own markup** (`ks3-block` alone → `check`; `ks3-block ks3-dark ks3-practical` → `practical`) and
follow the measurement, not this table, where they disagree.

### B2 — Movement: skeleton and muscles

| kind | lesson | segment | canvas? | payload |
|---|---|---|---|---|
| `system-switch` | b2-01 | measure | DOM | `{parts:[{id,name,tab,title,does,prompt,options[4],chain:[{level,text}],close}], show_levels}` |
| `job-sort` | b2-01/02/03 | measure | DOM | per-item immediate-reveal sorter — 14 items, the largest single win in the unit |
| `joint-bench` | b2-02 | measure | canvas | `{joints:[…12 fields…], bend_deg, bend_range, twist_allowed, twisting}` |
| `muscle-pair` | b2-03 | measure | canvas + rAF | `{mode:'biceps'|'triceps'|'both'|'none', dead:{biceps,triceps}, angle_deg}` |
| `arm-lever` | b2-04 | measure | canvas, static | `{load_kg, d_muscle_cm, d_load_cm, g:10, meter_fitted}` |
| `lever-steps` | b2-04 | measure | DOM | the four-step scaffolded attempt |
| `meter-compare` | b2-04 | measure | DOM | three meters × three readings + mean |

### C1 — Particles and their behaviour (rebuild)

| kind | lesson | canvas? | notes |
|---|---|---|---|
| `halving-bench` | c1-01 | canvas | cut / undo / cut-ten; **floor is 24 cuts** and the number is load-bearing in rung 2 |
| `gap-test-rig` | c1-01 | DOM | three tests × gap-filled or not |
| `state-bench` | c1-02 | canvas | state ×3, freeze, paths, squash. **The fixed-size reference particle is drawn in every state and may not be removed for layout** |
| `heating-bench` | c1-03 | canvas | scrub 0–100, three jump targets; **boiling plateau ~7:1 longer than melting, and rung 4 depends on it** |
| `collision-counter` | c1-04 | canvas | temp ×3, volume ×3, count ×3; particle–particle bumps are **drawn and explicitly excluded** |
| `random-walk-bench` | c1-05 | canvas + rAF | **the two crossing counters must not reset when `even` flips** — that is the whole confrontation of `PART-11` |
| `evidence-bench` | c1-06 | DOM | 7 tests, 4 pass 3 fail |
| `model-timeline` | c1-06 | DOM | five steps; stops short of "and now we know" |

### C2 — Atoms, elements and compounds

| kind | lesson | canvas? | notes |
|---|---|---|---|
| `claim-switch` | c2-01 | DOM | 3 claims × 4 observations; an observation reads *no longer explained* when a claim it needs is off |
| `test-budget-bench` | c2-02 | DOM | **the budget is the pedagogy.** Default 8. Drop it and the lesson becomes a click-through |
| `mixture-compound-dish` | c2-03 | canvas | proportion control **disabled once heated** — that is itself the lesson |
| `formula-builder` | c2-05 | canvas | five reachable substances; most combinations say **"not a substance"** |
| `balance-bench` | c2-06 | measure | 2 reactions × 2 vessels; third tile reads *not measured — you work it out* |

### Shared

| kind | used by | notes |
|---|---|---|
| `cover-triangle` | b2-04 | **exists** as `r_formula_triangle` with corrected, derived geometry. Payload widens: a `result` slot (Design shows the arrangement in display type *and* a sentence), three closing blocks not one, and Design's button order `F, T, d` with `F` pre-covered |
| `cover-bar` | c2-06 | **NEW.** The part–whole bar: one long bar for *everything before*, split beneath into *left in the flask* + *the gas*, same three cover buttons. Cover keys are `whole` / `left` / `gas`. Verified from the page: **c2-06 contains the word "triangle" zero times** and draws a balance beam with pans |

---

## 5. What is NOT in scope

- **P1–P3 are authored and deliberately held for MRB-223.** If they appear on disk, ignore them.
- No new page structure, no new layout, no component Design has not drawn.
- No change to the nav brand (R6), the carve-out date `verify_ks3.py:27 CARVE_OUT_EXPIRY`
  (needs an explicit §12 amendment with Mide's decision on the record), or `shell()`'s signature —
  it is composed from two sessions' work and the single `trail_html or crumb_html` slot is
  deliberate.

---

## 6. Gates — a failing gate is a finding, never an obstacle

Never weaken a gate to make something pass.

1. `python3 verify_ks3.py` green.
2. `python3 ks3_key_audit.py B2 C1 C2` green.
3. Byte-identical output across **both** generator orders (KS4-then-KS3 and the reverse).
4. Zero console errors on every new page.
5. Every new assertion **mutation-tested** — an assertion that still passes against a deliberately
   broken page is not an assertion.
6. Every new component has **markup AND CSS AND JS**. A dispatch-table entry is not a component;
   instruments have shipped as bare bullet lists past a green kinds gate.
7. **Freeze transitions before driving any state.** `.ks3-option` transitions background over
   160ms, so a computed-style read straight after a click returns the colour it is *leaving*.
8. Use the harness **device-metrics override** for viewport queries. Shrinking a container does not
   fire a `max-width` media query and will pass silently over a broken layout.
9. Verify CSS against elements that **actually exist on the page**. Dead CSS is evidence to a grep
   and nothing to a browser.
10. Every state seen in a browser, not described: resting, chosen-correct, chosen-wrong, spent,
    locked, reduced-motion.

**Browser harness, learned the hard way:** run a **fresh headless Chrome per page** — the KS3
canvas loops keep running after the driver moves on, and one shared browser accumulates enough of
them to drop the DevTools socket around the twelfth page.
