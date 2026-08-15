# B1 — *Cells and organisation*: review pack

Companion to `ks3_data/biology_b1_cells.py`. Eight lessons, Year 7 Biology, all
`review_state: draft`.

This pack exists so the science review and the rulings can be done without
reading 1,900 lines of Python. **It is not the content** — every teaching
decision lives in the module, and where the two disagree the module is right.

Written by Claude Design, 9 August 2026. Nothing committed.

---

## 1. The unit at a glance

| # | Lesson | Family | `covers` | Misconceptions | Flagship | Figures |
|---|---|---|---|---|---|---|
| 1 | Life processes and what living things are made of | CLASSIFY | `CELLS.01a` | `LIFE-01` `LIFE-02` | classify drill, rising stakes | 2 |
| 2 | Using a microscope | INVESTIGATION | `WS.EXP.05` + `CELLS.01b` | `CELL-01` `CELL-02` | `microscope` ⊕ | 3 |
| 3 | Animal and plant cells | MODEL | `CELLS.02` `CELLS.03` | `CELL-03` `CELL-04` | `system-parts` ⊕ | 3 |
| 4 | Specialised cells | SYSTEM | `CELLS.04` | `CELL-05` **`PART-10`** | `system-parts` ⊕ (mid-size: C1's `diffusion`) | 3 |
| 5 | Levels of organisation | SYSTEM | `CELLS.06` | `CELL-06` `CELL-07` | `system-parts` ⊕ | 3 |
| 6 | Unicellular organisms | CONTRAST | `CELLS.05` | `LIFE-03` `CELL-08` | `microscope` ⊕ | 2 |
| 7 | Stem cells and meristems | PROCESS | — *beyond statutory* | `CELL-09` `CELL-10` | Law 5 stepper pair | 2 |
| 8 | Enzymes and what changes their rate | MODEL | — *beyond statutory* | `CELL-11` `CELL-12` | Law 5 read-the-curve pair | 3 |

⊕ = needs a component that does not exist yet. **`PART-10` is re-used from C1,
not re-minted** — the same wrong idea in a biological costume.

**Exactly-once check.** Six statutory statements, one split into two clauses,
seven clauses owned by seven lessons, no clause owned twice, none unowned:

```
CELLS.01a → L1     CELLS.02 → L3     CELLS.04 → L4     CELLS.06 → L5
CELLS.01b → L2     CELLS.03 → L3     CELLS.05 → L6
```

---

## 2. Eight things that need a ruling

Fuller reasoning for each is in the module docstring; this is the decision and
the recommendation.

| # | The call | Recommendation |
|---|---|---|
| 1 | **L2 owns a subject statement as well as its WS anchor.** §5.7.1 clause 3 allows it "only if the lesson genuinely owns it and no other lesson does". `CELLS.01b` is *how to observe, interpret and record cell structure using a light microscope* — the whole lesson, taught nowhere else. | Allow. First use of clause 3; confirm rather than assume. |
| 2 | **Two B1 lessons have no statutory home.** Stem cells appear nowhere in the programme of study; enzymes appear once, parenthetically, inside `B.NUT.04`, which B3 owns and needs. §10.2 leaves only `beyond_statutory: True`. | Accept both as `beyond_statutory`, placed last in the unit. They become the first two rows of `bridge-register.md` — which wants a column separating *bridge-unit lesson* from *beyond-statutory lesson inside a KS3 unit*, since their URLs say `/cells-and-organisation/` not `/gcse-bridge-…/`. Moving them would change the 185-lesson scope and is not an authoring decision. |
| 3 | **`beyond_statutory` is absent from all six C1 lessons.** §4.8 lists it; §10.2 says absent is a defect. | Present and explicit on all eight here. Sweep C1. |
| 4 | **`CELL-11`/`CELL-12` are enzyme misconceptions in a cell family**, exactly as `PART-12`/`PART-13` are nature-of-science misconceptions in a particle family. | Leave them. If B3 or C6 later want an `ENZ` family, the `PART-12` ruling applies unchanged: IDs do not move, the register cross-references. |
| 5 | **`SIM_CONTROLS` needs four new names** — `specimen`, `magnification`, `focus`, `part` — plus `CONTROL_LABELS` entries in `shared/ks3.js`. `r_sim()` validates and fails the build without them. | Schedule with the two components. Five of eight lessons block on it. |
| 6 | **No `rate-curve` instrument was declared, and L8 wants one.** It leans on a declared graph plus a Law 5 pair instead. | Build it for a unit that needs it more — B7 `rate-of-photosynthesis`, C6 `catalysts`, C7 `measuring-a-temperature-change` all want the same instrument. Two blocking components is the limit for one unit. |
| 7 | **The schema has nowhere to put a stepper's steps.** §6 gives PROCESS a "worked stepper"; the only authored `worked-example` in the course is a calculation carried by `fifa`. L7's steps are numbered inside the `prompt`, which renders today. | Add a `steps` field when a PROCESS unit is next authored. Nothing here depends on it. |
| 8 | **New figure kind `micrograph`, and a third sourcing effort.** Five figures are photographs *through an objective lens*, of named specimens. A schematic does not substitute for one — L2's entire lesson is that the real view is disappointing, and a tidy drawing of onion cells destroys it. Nor is this the Platform Backlog photography ticket, which is real-life context photography. | Track as its own kind. Three efforts, not two: schematic, micrograph, photography. |

---

## 3. Science review — what to check, per lesson

Everything below is a science-bearing field under §5.10. The list is the claims
worth a second look, not the full text.

**L1 — Life processes**
- The all-seven rule is taught as absolute, because a rule that accepts "most of
  them" cannot exclude a candle flame. The confrontation handles the obvious
  objections by saying a living thing has the *equipment* for all seven even when
  it is not using it — a resting seed, a mule. **Check that wording.**
- The crystal is scored as doing three of the seven (movement, growth, and
  "reproduction" of its shape). That generosity is deliberate: three is still not
  seven.
- ⚑ **Stretch block on viruses** — one life process, only inside a host, not made
  of cells, and scientists disagree. Beyond the programme of study, opt-in, and
  it is the question every Year 7 asks. Ruling wanted.
- "About thirty trillion cells" (unit intro).

**L2 — Using a microscope**
- Total magnification = eyepiece × objective; ×10 × ×40 = ×400.
- Air bubbles: perfectly round, thick dark rim, floating apart. Onion cells:
  straight sides, packed in rows. This is the whole hook.
- Higher magnification → smaller field of view → refocus needed.
- Stretch: field of view 1.8 mm ÷ 6 onion cells ≈ 0.3 mm; cheek cell ≈ 0.06 mm.
  Both are order-of-magnitude claims presented as approximate.

**L3 — Animal and plant cells**
- Seven parts and seven jobs, matching `CELLS.02` exactly.
- The `system-parts` dependency graph makes claims about what fails when a part
  is switched off. The one to check: **no nucleus → the cell cannot make new
  parts or divide, and carries on for a while first.** Nothing is said to burst.
- ⚑ **Osmosis is never named.** The vacuole "pushes outwards and keeps the cell
  firm"; a short-of-water plant wilts. Osmosis is not in the KS3 programme of
  study.
- Only cells that receive light have chloroplasts; a potato greening on a
  windowsill is used as the everyday case.

**L4 — Specialised cells**
- Red blood cell: no nucleus, ~4 months, ~2 million made per second, packed with
  haemoglobin, dented for surface area and short diffusion distance.
- **The root hair cell is never given as an example of diffusion** — it "takes in
  water and minerals", mechanism unnamed, because neither is diffusion.
- Diffusion into a cell is taught as two-way, net one-way, nothing pushing — the
  `PART-10` re-confrontation.
- Nerve cell ≈ 1 m, in the stretch block; the point made is that *width* is what
  diffusion cares about, not length.

**L5 — Levels of organisation**
- Bone is a tissue; skin is an organ; the pituitary is an organ smaller than a
  leg bone is a tissue. Size decides nothing.
- **Blood is a tissue**, and it is used as the case that tests the definition: it
  is liquid and holds more than one kind of cell, and it is the *shared job* that
  makes a tissue. Worth checking the wording is one an examiner would accept.
- The stomach wall is taught as three tissues: muscular, glandular, lining.
- Stretch: skin tissue is grown for burns patients; whole organs are far harder.
  No claim is made about which organs have been grown.

**L6 — Unicellular organisms**
- Euglena: flagellum, eyespot, chloroplasts. Amoeba: pseudopod for movement and
  feeding, contractile vacuole. Paramecium: cilia, oral groove, contractile
  vacuole.
- ⚑ The contractile vacuole is described as bailing out water that "seeps in",
  again avoiding osmosis by name.
- ⚑ **Bacteria have no nucleus; their instructions sit in a loop in the
  cytoplasm** (stretch block). Standard KS3, needed to make `CELLS.05`'s
  "structural adaptations" honest. *Prokaryote* and *eukaryote* are not used —
  they are KS4 and XC1 owns them.
- The claim that a Euglena carries everything one of our cells has *plus* extra
  equipment. Check that the empty second list is fair.

**L7 — Stem cells and meristems** *(beyond statutory)*
- Differentiation is taught as one-way, with scars as the everyday evidence.
- Meristems at root and shoot tips; a plant keeps stem cells for life.
- ⚑ Bone marrow makes new blood cells; a cut heals, a finger does not regrow.
  Beyond the programme of study, inside a beyond-statutory lesson.
- Stretch: bone marrow transplant, described mechanically (donated unspecialised
  cells divide and differentiate). **No ethics content** — that felt like a call
  for you rather than for me.

**L8 — Enzymes and rate** *(beyond statutory)*
- ⚑ **"Killed" is attacked directly** and replaced with *denatured*, using L1's
  seven processes as the argument: an enzyme does none of them, so it was never
  alive. This is the lesson's spine.
- Denaturing is taught as permanent — it does not undo on cooling.
- ⚑ **"Everything moves quicker, so the enzyme and the substance meet more
  often"** is collision theory in Year 7 clothing, said once, without the name,
  because the rising half of the curve is otherwise magic. XC1 owns collision
  theory. Cut it if you would rather it waited.
- ⚑ Enzyme shape "fits the substance it works on, the way a key fits a lock" —
  the KS3 treatment, stopping short of lock-and-key as a model. XB1 owns that.
- Optimum near 37 °C; stomach enzyme optimum pH 2 (used in the do-mode task).
- Liver + hydrogen peroxide → water and oxygen; the foam is the oxygen.

---

## 4. Patches, ready to apply

### 4.1 `ks3_data/substatements.py`

One bullet split, minted lazily, at the grain the lessons are written at.

```python
    # Minted for B1 (2026-08-09). The bullet reads:
    #   "cells as the fundamental unit of living organisms, including how to
    #    observe, interpret and record cell structure using a light microscope"
    # Two separable teaching ideas, taught a week apart by every scheme of work.
    "KS3.B.CELLS.01": [
        ("a", "Cells as the fundamental unit of living organisms: everything "
              "alive is built from cells, and nothing else is.", "B1"),
        ("b", "How to observe, interpret and record cell structure using a "
              "light microscope.", "B1"),
    ],
```

`KS3.B.CELLS.06` was **not** split, though splitting it would have given every
lesson a statement of its own. The hierarchy bullet is one idea and L5 teaches
all of it; splitting a bullet to relieve an allocation squeeze is how a register
stops meaning anything.

### 4.2 `docs/ks3/misconception-register.md` — two families opened

Add to the family-prefix table:

| Prefix | Domain | Opened |
|---|---|---|
| `LIFE` | What counts as living, and the life processes | 2026-08-09, by B1 |
| `CELL` | Cells, microscopy and the organisation of living things | 2026-08-09, by B1 |

#### `LIFE` — what counts as living

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `LIFE-01` | If something moves on its own it must be alive, and if it never moves it must not be. | `three-dishes-vote` | `seed-or-crystal` | `life-processes` |
| `LIFE-02` | Doing one of the life processes is enough to count as alive — if it grows on its own, it is alive. | `crystal-check` | `seven-out-of-seven` | `life-processes` |
| `LIFE-03` | A single cell cannot be a whole living thing — it must be part of something bigger. | `how-many-processes` | `one-cell-does-all-seven` | `unicellular-organisms` |

#### `CELL` — cells, microscopy and organisation

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `CELL-01` | Those neat round circles in the field of view are the cells. | `count-the-cells` | `bubble-or-cell` | `using-a-microscope` |
| `CELL-02` | The highest magnification is always the best one to use, because it shows you the most. | `pick-a-lens` | `microscope-lab` | `using-a-microscope` |
| `CELL-03` | Every plant cell is green, because plants are green. | `plant-extras` | `not-all-green` | `animal-and-plant-cells` |
| `CELL-04` | The cell membrane and the cell wall are the same thing — animal cells have a wall, it is just called a membrane. | `whats-holding-it-up` | `wall-or-membrane` | `animal-and-plant-cells` |
| `CELL-05` | Every cell in your body has a nucleus. | `which-has-no-nucleus` | `no-nucleus-reveal` | `specialised-cells` |
| `CELL-06` | The levels are just about size: small things are cells, medium things are tissues and big things are organs. | `size-trap` | `not-about-size` | `levels-of-organisation` |
| `CELL-07` | Blood is not a tissue, because a tissue is solid and blood is a liquid. | `blood-check` | `blood-is-a-tissue` | `levels-of-organisation` |
| `CELL-08` | A single-celled organism is just a simpler version of one of our cells — the same parts, doing less. | `same-or-extra` | `more-not-fewer` | `unicellular-organisms` |
| `CELL-09` | A stem cell is a cell from the stem of a plant. | `where-does-the-word-come-from` | `stem-not-stem` | `stem-cells-and-meristems` |
| `CELL-10` | A specialised cell can change into a different kind whenever the body needs it — a skin cell can become a nerve cell. | `where-from` | `once-you-choose` | `stem-cells-and-meristems` |
| `CELL-11` | The enzymes were killed by the heat. | `what-did-boiling-do` | `not-killed-changed` | `enzymes-and-rate` |
| `CELL-12` | The hotter it is the faster any reaction goes, so an enzyme works best as hot as possible. | `predict-the-curve` | `two-halves-of-the-curve` | `enzymes-and-rate` |

**Expected to resurface** (`reappears_in`, for filling as later units are
authored):

- `CELL-04` (wall/membrane) → B7 `leaves-built-for-the-job`, and again at KS4.
- `CELL-05` (every cell has a nucleus) → B10 `chromosomes-genes-and-dna`, where
  it does real damage.
- `CELL-06`/`CELL-07` (levels) → B3 `the-digestive-system`, B4
  `the-gas-exchange-system`, B9 `food-chains-and-food-webs`. Every SYSTEM lesson
  in Biology re-tests this pair.
- `CELL-11` (killed, not denatured) → B3 `enzymes-in-digestion`, C6 `catalysts`.
  It is a *wording* habit, and wording habits are killed early or not at all.

#### One edit to an existing entry

`PART-10` and `PART-11` already name B1 under *where these are expected to
resurface*, and they name `animal-and-plant-cells`. **`PART-10` lands in
`specialised-cells` instead** — that is where `CELLS.04` is owned and where
diffusion does visible work. One word:

```diff
- `PART-10`/`PART-11` … → B1 `animal-and-plant-cells` and B4 `alveoli-built-for-exchange`
+ `PART-10`/`PART-11` … → B1 `specialised-cells` and B4 `alveoli-built-for-exchange`
```

`PART-10`'s own row keeps its C1 `elicited_by`/`confronted_by`. B1 carries its
own pair in the lesson record — `how-does-oxygen-get-in` and
`membrane-diffusion-lab` — because the register row records where an idea was
*opened*, not everywhere it is fought.

### 4.3 `docs/ks3/diagram-manifest.md`

Regenerates from the lesson data. It goes from 11 figures to 32: B1 adds 13
schematics, 5 micrographs, 2 apparatus and 1 graph, all `needed`. `micrograph`
is a new value in the Kind column — see ruling 8.

---

## 5. What B1 is blocked on

Nothing in the content. **MRB-198** (ticketed 10 Aug 2026) covers all of it.

| Blocker | Blocks | Note |
|---|---|---|
| `microscope` component + aria label | L2, L6 | Contract in `B1 Instrument Spec`; payload `specimens[]`. |
| `system-parts` component + aria label | L3, L4, L5 | Payload-driven, not bespoke: `parts: [{id, name, job, needs}]`. The SYSTEM flagship the family has never had, and the pattern for 47 lessons. |
| `SIM_CONTROLS` + `CONTROL_LABELS` | both | Add `specimen`, `magnification`, `focus`, `part`. The cheap half of the ticket, and the half that fails loudest — `r_sim()` raises. |

L1, L7 and L8 build today with no new work. L4's mid-size instrument is C1's
`diffusion` component **unchanged** — same kind, same controls, and the dashed
centre line reads as the cell membrane. A Year 7 meets the identical instrument
in chemistry and then in biology, which is the misconception register's whole
argument made visible.

---

## 6. Done-list (§10.2), honestly

Per lesson, all eight:

- ✅ One idea, statable in one sentence — the `big_question` is that sentence.
- ✅ `covers` non-empty and owned once — **except L7/L8, `beyond_statutory: True`
  with `covers` empty and `ks4_links` resolving**, which is the other legal half
  of the pair.
- ✅ Opens with a phenomenon, not a definition.
- ✅ First commitment inside ~90 words; total prose 137–242 words against a 450
  ceiling; no single explainer over 91.
- ✅ `misconceptions` non-empty, at least one confronted by an activity.
- ✅ Every stateful reveal gated by a prediction — every `lab` carries options and
  a keyed answer before its sim.
- ✅ Every `worked-example` paired with its `check` (L2, L7, L8).
- ✅ Concrete → representational → abstract in every lesson.
- ✅ `vocabulary` authored and recalled; every lesson has a `keyword` block and a
  recall mechanic, and every card grid asks for the declaration in words (§5.1.2a).
- ✅ Four-rung ladder; rungs 1–2 keyed with a written correction on **every** wrong
  option; rungs 3–4 plain-English criteria, no tariffs.
- ✅ Blocks drawn only from the §5.1.1 vocabulary, arranged by family.
- ✅ `support` present and empty (§11 decision 4); `figures` authored;
  `beyond_statutory` present and explicit; `typical_year` present.
- ✅ `requires` authored, 0–2 edges per lesson, acyclic:
  `life-processes → using-a-microscope → animal-and-plant-cells →
  specialised-cells → levels-of-organisation`, with `unicellular-organisms`
  hanging off L1 and L3, `stem-cells-and-meristems` off L4 and `enzymes-and-rate`
  off L3.
- ⏳ Motion animated with a reduced-motion fallback — **specified, not built**
  (§5). R6 applies to both new components.
- ⏳ Keyboard-complete, WCAG AA, touch-tested — after the components land.
- ⏳ Science examiner-reviewed, `review_state: frozen` — this pack.

**§10.3's review question, answered per lesson**: *which wrong idea does this
lesson kill, and would a student holding it be forced to notice?*

| Lesson | The idea it kills | Where they are forced to notice |
|---|---|---|
| L1 | Movement means life | They vote on three dishes, and the one that moved and grew is the dead one |
| L2 | Those circles are the cells | They commit to a number of cells, and the answer is none |
| L3 | A membrane is a wall | They are asked what holds a plant up without a skeleton |
| L4 | Every cell has a nucleus | They are asked which of six has none, before being told any cell can lack one |
| L5 | The levels are about size | A pea-sized gland is an organ and a leg bone is a tissue, side by side |
| L6 | One cell must be part of something bigger | Their own cell dies in the pond water beside the Amoeba |
| L7 | Cells change job when needed | Scars are the evidence that they do not |
| L8 | Heat kills enzymes | An enzyme is scored against L1's seven life processes and fails all seven |
