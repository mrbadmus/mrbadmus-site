# NOTES — KS3 Physics P10

**P10 complete.** All five slots (`p10-01` … `p10-05`) authored, one standalone
viewable HTML per lesson. Slugs, titles, families and the lesson count are taken from
`ks3_data/structure.py` character for character. §7 below is the component-family
registration the parity gate needs.

---

## 1. Statutory ownership

Coverage asserts every statement has **at least one** owner. A statement may be claimed
by more than one lesson; no sub-IDs, no `covers_partial`.

| Slot | Statements claimed |
|---|---|
| `p10-01 magnets-and-poles` | `KS3.P.MAG.01` — magnetic poles, attraction and repulsion |
| `p10-02 magnetic-fields` | `KS3.P.MAG.02` — magnetic fields by plotting with a compass, representation by field lines |
| `p10-03 the-earth-is-a-magnet` | `KS3.P.MAG.03` — the Earth's magnetism, compass and navigation; also `MAG.02` (plotting), claimed again |
| `p10-04 electromagnets` | `KS3.P.MAG.04` — the magnetic effect of a current, electromagnets |
| `p10-05 how-a-motor-works` | `KS3.P.MAG.04` — D.C. motors, principles only; also `MAG.02`, claimed again |

`MAG.02` and `MAG.04` are each claimed twice. That is correct and needs no notation.

---

## 2. Formula blocks (MRB-204)

**P10 carries no formula block in any lesson.** Ruled under standing rule 1.

KS3 magnetism names no quantity with a unit that a student can calculate. Field strength
in tesla is GCSE; `F = BIL` is GCSE; the turns-and-current relationship in `p10-04` is a
genuine product but has no named quantity and no unit at this stage, so writing it as a
formula would mean inventing notation to fill the badges — which the formula-setup rule
forbids. The relationship is stated in words, and the instrument shows it by letting the
two controls move independently.

Where a lesson names a number it is a **relative figure against a stated reference**, or
a real angle in degrees:

| Lesson | Numbers the student can read |
|---|---|
| `p10-01` | relative strength, 100 = the closest pair of magnets; gap in cm |
| `p10-02` | bearing in degrees; relative field strength, 100 = strongest point on that map |
| `p10-03` | angle of dip in degrees; sideways pull, 100 = the equator |
| `p10-04` | paper clips held (a count); relative field strength, 100 = strongest setting |
| `p10-05` | relative turning effect, 100 = strongest setting; current in A |

---

## 3. Teaching from nothing

- **`p10-01`, `p10-02` and `p10-04` each define poles from nothing.** Deliberate. A
  school may run P10 in any order.
- **`p10-02` and `p10-03` each state that a compass needle is a small magnet that lines
  up with a field**, rather than depending on each other for it.
- **`p10-05` restates that a current makes a magnetic field**, so it does not depend on
  `p10-04`.
- **`p10-03` restates like-repels-unlike-attracts** in one clause, because the naming of
  the Arctic pole as a magnetic south pole turns on it.
- Every cross-lesson reference is an edge in *Connects to* or an offer in *Going further*.

---

## 4. The benches — whole reachable state space

| Lesson | Instrument | Reachable states | Branches |
|---|---|---|---|
| `p10-01` | Two objects on a low-friction track | 5 × 5 objects × 6 gaps = **150** | 4, keyed to **what the pair does**: nothing (102 states), repel (12), attract as two magnets (12), attract by magnetising the steel (24) |
| `p10-02` | Plotting compass on a field map | 4 layouts × 25 positions = **100** | 5, keyed to **what the compass does**: on the metal (no reading), single bar, unlike poles facing, like poles facing with its own neutral-point branch, horseshoe |
| `p10-03` | Compass free to tip, taken to different latitudes | 9 latitudes × 3 bench objects × 2 mountings = **54** | 5, keyed to **what the needle finds**: captured by a magnet, captured by steel in a weak field, held level, tipped, standing vertical at the pole |
| `p10-04` | Coil, supply, core, switch, paper clips | 5 turns × 5 currents × 3 cores × 2 switch = **150** | 4, keyed to **what the electromagnet is doing**: switched off (75 states), iron core, empty coil, plastic former |
| `p10-05` | Coil on an axle between two magnets | 2 current × 2 magnets × 2 rings × 4 currents = **32** | 3, keyed to **what the coil does**: never starts, turns and keeps turning, turns half a turn and stops |

Standing audit findings, honoured:

- **No bench narrates its own controls.** Every lead is the set-up or an instruction.
- **No figure the instrument computes is hard-coded in prose.** Every number in every
  bench sentence interpolates from the same state the readouts use. The only fixed
  numbers are in stated scenarios in their own headings.
- **Every comparative label is derived at render.** `p10-01`'s strength word and its
  "does this prove both are magnets" verdict; `p10-02`'s crowding word and compass
  direction; `p10-03`'s navigability verdict; `p10-04`'s core word and strength word;
  `p10-05`'s spin direction and "does it keep going". The equal case was driven and
  checked on each.
- **Every control is modelled and its effect stated.** `p10-04`'s plastic former is
  modelled as doing nothing, and the note says so rather than leaving it silent.
  `p10-03`'s "clamped flat" reports dip as zero **and says the mounting is holding it
  there**, not the field.
- **Drawn geometry expresses the ratio its label claims.** `p10-01`'s gap in px is
  proportional to the gap in cm; `p10-02`'s arrow lengths scale with the square root of
  the sampled field; `p10-03`'s needle tilt is the dip angle.
- **Live labels on a diagram are HTML, not `<text>`.** Every moving label is an
  absolutely-positioned `<span>` over a `position: relative` wrapper, with `left`
  computed from the viewBox coordinate. Fixed captions stay as literal `<text>`.

---

## 5. Safeguarding

**`p10-01` carries the Childline block.** Its *Going further* names neodymium magnets
and magnet ingestion, which is a risk to a student's own body and one that lives in their
home rather than in a lab. The block names the school nurse, a pharmacist, a GP and 111
alongside **Childline, free on 0800 1111**, at any hour, no name needed — inline, small
type, bottom edge, above the legal line.

`p10-02`, `p10-03`, `p10-04` and `p10-05` do not carry it. Nothing on those pages touches
a student's own body, health or risk; `p10-04`'s MRI paragraph is information about a
hazard in a hospital, not a risk the student is being asked to disclose.

---

## 6. Misconception ids — pre-allocated, not minted

No opened family exists for magnetism, and nothing in an authored lesson may cite an
unopened family. **No id is cited on any page.** Ranges reserved so parallel batches
cannot collide, last of each four the named spare.

| Lesson | Range | Spare |
|---|---|---|
| `p10-01` … `p10-05` | `MAG-01` … `MAG-20`, four per lesson in slot order | last of each four |

Authored, awaiting minting:

| Proposed id | Statement, as a student holds it | Lesson |
|---|---|---|
| `MAG-01` | All metals are magnetic. | `p10-01` |
| `MAG-02` | It stuck to the magnet, so it must be a magnet. | `p10-01` |
| `MAG-03` | Turning a magnet round makes it stronger or weaker. | `p10-01` |
| `MAG-05` | The field is only where the lines are drawn. | `p10-02` |
| `MAG-06` | The iron filings make the field. | `p10-02` |
| `MAG-07` | Field lines can cross if the field is strong enough. | `p10-02` |
| `MAG-09` | The Earth's North Pole is a magnetic north pole. | `p10-03` |
| `MAG-10` | A compass points at the North Pole. | `p10-03` |
| `MAG-11` | There is a bar of iron inside the Earth. | `p10-03` |
| `MAG-13` | The iron core is what makes the magnetism. | `p10-04` |
| `MAG-14` | More turns means more wire, so more current. | `p10-04` |
| `MAG-15` | Switching off leaves a weak field that drains away. | `p10-04` |
| `MAG-17` | The magnets attract the coil, which is why it turns. | `p10-05` |
| `MAG-18` | The split ring is what makes the motor turn. | `p10-05` |
| `MAG-19` | Reversing the current and the magnets reverses it twice over. | `p10-05` |

---

## 7. For Code — component families registered

**New families minted by this group**

| Family | Debuts in | What it is |
|---|---|---|
| `track-pair` | `p10-01` | Two object blocks on a rail at a computed gap. Body paths, pole-face fills, dimension line and force arrows all computed from three controls; pole letters and object names are absolutely-positioned spans whose `left` is computed from the block centres. Dashed stroke marks a non-magnetic material, so identity is never hue alone. Data: `{a, b, gapIndex}`. |
| `compass-plot` | `p10-02` | A vector field sampled on a 13 × 7 lattice and emitted as **one** path string, each arrow's direction and length from the summed inverse-square field of point poles; points inside a magnet are omitted. A separate needle path marks the movable plotting compass, and is omitted entirely at a neutral point. Bar magnets are drawn from a declarative `bars` list with the north half filled. **This family is why the lesson needs no hand-authored field lines.** |
| `dip-circle` | `p10-03` | A side-on needle at a computed tilt with an arc marking the dip angle, beside a globe carrying a tilted internal bar magnet, four field arcs and a "you are here" marker whose position is computed from latitude. Refuses to draw a needle when the field is vertical or when the compass is captured. |
| `solenoid-bench` | `p10-04` | A coil drawn as eight fixed loops **whatever the turn count** — the drawing is a symbol, the number is the readout — with a computed core, a computed switch path (open or closed), field loops whose stroke width scales with the field, and a chain of paper clips capped at ten drawn marks. |
| `motor-coil` | `p10-05` | A coil face-on between two magnets, with computed current arrows on the two sides, force arrows whose length scales with the turning effect, a split-ring or plain-ring path at the axle, and a rotation arc drawn only when the turning effect beats friction. |

**Reused unchanged from B1–P9**: `ks3-nav`, the top and side progress rails, `ks3-hook`
with `ks3-options`, `ks3-explainer`, `ks3-block ks3-dark ks3-practical`,
`[data-key-fact]`, `ks3-misconception`, `ks3-ladder` with two marked and two self-marked
rungs, `ks3-keynote`, `ks3-layer`, `ks3-endmatter`, `ks3-legal`, `safeguard-block`.

**Notes for the generator**

- **Live labels on a diagram are HTML spans, not `<text>`.** The `<span>`-in-SVG failure
  is silent, so this is not optional. Where a label moves with the diagram, its `left`
  percentage is computed in `renderVals()` from the same viewBox coordinate the geometry
  uses.
- **No `<sc-for>` inside an `<svg>` anywhere.** Repeated marks — lattice arrows, coil
  loops, clip chains, field arcs — are built as one path string in `renderVals()`.
- **Long left-anchored mono captions overflow the viewBox silently.** SVG clips to the
  viewBox and gives no warning. Every caption in this group was measured with `getBBox`;
  the same sweep found and fixed one pre-existing clip in `p8-06`'s log chart, where the
  *roughly where useful conduction gives out* hedge was being cut mid-word.
- All instruments are DOM and inline SVG. No canvas, no timers, no animation loop, no
  `Math.random()` anywhere in the group.
- Every arrow, tick and cross is inline SVG. No `→`, `✓` or `✕` character appears in any
  of the five files; a build check for those three characters passes.
- Props: `showDraft` only, as everywhere else in the build.
- Four rail stops per lesson. Not five.
- Forward and back links use the `.html` form of the slug, matching P5–P9.
- **`--ks3-data` is not in the design-system copy bound to this project**, so P10 does not
  use it yet. See `docs/ks3/design-reference/font-and-token-law.md` for the fallback form
  to use once the shipped token file carries it.

---

## 8. Hedges that are load-bearing

- **"about"** on every dip angle and every relative strength quoted in prose.
- **"in practice"** and **"roughly"** are not used to soften a claim the bench then
  contradicts; where a model is wrong in shape rather than in size, the legal line says so
  directly.
- **`p10-03`'s legal line names the eleven-degree tilt** between the magnetic and spin
  axes, and states that dip measured in the field differs from the figure shown by several
  degrees in most places. Removing that turns a first model into a claim.
- **`p10-01`'s pull on steel is reported in relative words only, never as a figure**,
  because how strongly a piece of steel magnetises depends on its shape, its carbon content
  and its history. Same discipline as `p9-02`'s induced attraction.
- **`p10-04`'s legal line says the largest numbers are optimistic**, because a real core
  saturates and a real coil heats up.
- **`p10-05`'s legal line says the coil is frozen at its strongest position**, and that a
  real single-coil motor's turning effect falls to nothing twice per turn.
- The `.ks3-legal` line on all five pages discloses what the bench leaves out and which
  numbers are conventions rather than measurements.

---

## 9. Rulings made under standing rule 1

1. **No formula block anywhere in P10.** §2 above.
2. **Relative scales, never invented units.** No tesla, no newtons, no newton metres.
   Each relative figure names its reference in the readout.
3. **`p10-03` uses a centred dipole aligned with the spin axis**, giving
   `tan(dip) = 2 tan(latitude)` and a sideways pull going as `cos(latitude)`. Disclosed.
4. **`p10-04` models the plastic former as identical to no core**, and says so on the face
   of the bench rather than leaving the student to infer it.
5. **`p10-05` freezes the coil horizontal.** Disclosed, with the reason real motors use
   several coils given in *Going further*.
6. **`p10-01` carries the safeguarding block**; the other four do not. §5 above. This one
   is Mide's to ratify.

---

## 10. Nothing was committed

Read-only access, as instructed: no branch, no commit, no register edit, and no prompt
written for Code was run.
