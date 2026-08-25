# NOTES — KS3 Physics P6 / P7

**P6 and P7 complete.** All nine P6 slots (`p6-01` … `p6-09`) and all seven P7
slots (`p7-01` … `p7-07`) are authored, one standalone viewable HTML per lesson,
one folder per unit. This file is the delivery record for both units. §10 is the
component-family registration the coverage gate needs.

---

## 1. Recon: what was and was not available

| Input the brief names | State in this project |
|---|---|
| `ks3_data/structure.py` | Present. Slugs, titles, families and lesson counts taken from it character for character. |
| `ks3_statutory.py` | **Absent.** Ownership checked against `docs/ks3/statutory-register.md`, the generated companion. No ID minted; access is read-only. |
| `docs/ks3/mrb-220-build-contract.md`, incl. §5A | **Absent**, as `NOTES-P4-P6.md` §1 recorded on 19 Aug and `docs/ks3/gates/README.md` on 17 Aug. Worked to `architecture.md`, the gates README, `CLAUDE.md` (which now carries the settled FIFA and formula-block law) and the frozen reference set. |
| `docs/ks3/design-reference/` | Present — `KS3 Reference Set (offline).html`. B9–B11 taken as the current model, via the P4/P5 pages built from them. |
| `docs/ks3/audits/2026-08-18-ks3-biology.md` | **Not at that path.** A file of that name is present at `uploads/2026-08-18-ks3-biology.md`. Its finding 6.4 (safeguarding blocks naming no confidential service) was read directly and is acted on in §6 below; the rest was taken from the brief's summary. |
| Coverage manifest | **Absent.** §10 below is therefore delivered here, as P4/P5 and C9 did. |

---

## 2. Statutory ownership

P6 owns six statements over nine slots (ratio 0.67); P7 owns six over seven
(0.86). Both are the surplus-slots case, so most statements are whole and only
the genuinely compound ones are split. Every clause is claimed exactly once.

| Slot | Statements claimed |
|---|---|
| `p6-01 waves-on-water` | `KS3.P.OBW.01` clause *"waves on water as undulations which travel through water with transverse motion"* |
| `p6-02 transverse-waves-and-superposition` | `KS3.P.OBW.01` clauses *"these waves can be reflected"* and *"add or cancel – superposition"* |
| `p6-03 how-sound-is-made` | `KS3.P.SND.03` clauses *"sound produced by vibrations of objects, in loudspeakers"* and *"detected by their effects on microphone diaphragm and the ear drum"* |
| `p6-04 sound-is-longitudinal` | `KS3.P.SND.03` clause *"sound waves are longitudinal"* |
| `p6-05 frequency-pitch-and-loudness` | `KS3.P.SND.01` clause *"frequencies of sound waves, measured in hertz (Hz)"* |
| `p6-06 sound-needs-a-medium` | `KS3.P.SND.02` whole |
| `p6-07 echoes-reflection-and-absorption` | `KS3.P.SND.01` clause *"echoes, reflection and absorption of sound"* |
| `p6-08 hearing-and-auditory-range` | `KS3.P.SND.04` whole |
| `p6-09 ultrasound-at-work` | `KS3.P.EAW.01` whole |
| `p7-01 light-travels` | `KS3.P.LGT.01` whole; `KS3.P.LGT.02` whole |
| `p7-02 reflection-mirrors-and-scattering` | `KS3.P.LGT.03` clauses *"diffuse scattering"* and *"specular reflection at a surface"*; `KS3.P.LGT.04` clause *"imaging in mirrors"* |
| `p7-03 refraction` | `KS3.P.LGT.04` clause *"the refraction of light"* |
| `p7-04 lenses-and-images` | `KS3.P.LGT.04` clauses *"the pinhole camera"* and *"action of convex lens in focusing (qualitative)"* |
| `p7-05 the-eye-and-the-camera` | `KS3.P.LGT.04` clause *"the human eye"*; `KS3.P.LGT.05` whole |
| `p7-06 colour-and-the-spectrum` | `KS3.P.LGT.06` clauses *"colours and the different frequencies of light"* and *"white light and prisms (qualitative only)"* |
| `p7-07 why-things-look-coloured` | `KS3.P.LGT.03` clause *"absorption"*; `KS3.P.LGT.06` clause *"differential colour effects in absorption and diffuse reflection"* |

**FLAG 1 — clause-level ownership still has no notation** (repeat of P4's FLAG 1,
unresolved). `OBW.01`, `SND.01`, `SND.03`, `LGT.03`, `LGT.04` and `LGT.06` are
each split across two or more slots, and `LGT.04` across four. A gate counting
statements per lesson will read `LGT.04` as claimed four times. Mide's call: the
register needs `.a` / `.b` sub-IDs, or lesson records need `covers_partial`.

**FLAG 2 — `p6-01` names no frequency, deliberately.** A wave has one, and the
lesson is about the shape of a wave rather than its rate. Putting a hertz readout
on the ripple tank would have made `p6-01` a second claimant of `SND.01`, so the
tank reports amplitude and wavelength in millimetres and the paddle rate is
described in words only, with `p6-05` carried as an edge. `p6-03` does report
"how many times a second" for each source, because the alternative was a bench
that names a quantity it will not let a student read — but it teaches no pitch
and claims no clause. A reviewer who reads Hz-anywhere as a claim on `SND.01`
should say so; it is a two-line change.

---

## 3. Formula blocks (MRB-204): triangle, beam, or nothing

Six of the sixteen lessons carry a formula block. Each has one relationship,
alone, in its own block, in the locked order: diagram, tap-to-reveal FIFA, then
the student's own four lines on live bench numbers, before anything independent
is asked.

| Lesson | Relationship | Figure | Why |
|---|---|---|---|
| `p6-01` | none | **no block** | `OBW.01` is qualitative. Wave speed = frequency × wavelength is GCSE and was not invented to have something to put in a triangle. |
| `p6-02` | `R = a + b` (in step), `R = a - b` (out of step) | **part–whole bar**, with cover buttons | A sum. A triangle here would teach a product that does not exist. The out-of-step case is the one permitted extra display line. |
| `p6-03` | none | **no block** | A process. Nothing to calculate. |
| `p6-04` | none | **no block** | A contrast. Nothing to calculate. |
| `p6-05` | `N = f × t` | **triangle** | A genuine product, and the unit-defining one: 1 Hz is 1 vibration each second. The extra display line is exactly that unit pairing. |
| `p6-06` | `d = v × t` | **triangle** | A product. The speed of sound is the statutory content and the triangle is what makes it usable. |
| `p6-07` | `s = d + d` | **part–whole bar**, with cover buttons | The out-and-back path is a sum of two equal parts. The load-bearing shortcut `d = s ÷ 2` is the extra display line. |
| `p6-08` | none | **no block** | A system lesson about ranges. |
| `p6-09` | none | **no block** | See FLAG 3. |
| `p7-01` | `d = c × t` | **triangle** | A product, and the speed of light is statutory in `LGT.02`. |
| `p7-02` | `r = i` | **beam, two equal bars**, no cover buttons | An equality, not a product and not a sum. Follows the `p1-08` precedent: a balance has nothing to cover. |
| `p7-03` | none | **no block** | Statute is qualitative; Snell's law and refractive index are GCSE. |
| `p7-04` | none | **no block** | See FLAG 4. |
| `p7-05` | none | **no block** | A system lesson. |
| `p7-06` | none | **no block** | Statute says *qualitative only* in terms. |
| `p7-07` | none | **no block** | A contrast. |

**FLAG 3 — `p6-09` has a relationship and no block, on purpose.** The ultrasonic
gauge computes depth from an echo time, which is `d = v × t` followed by halving
— `p6-06`'s triangle and `p6-07`'s bar, both already owned. Minting a third
speed block in the same unit would have been the fourth `d = v × t` triangle in
two units. Instead the bench prints its own working line by line and both owning
lessons are carried as edges. **If the contract requires a block wherever a page
computes, `p6-09` needs one and it will be a duplicate.**

**FLAG 4 — `p7-04` computes an image height and has no block.** `h_image =
h_object × (v ÷ u)` is a genuine product and would take a triangle cleanly. It
is left out because `LGT.04` says *qualitative* for the convex lens and the
pinhole clause carries no arithmetic, and because a triangle over three lengths
invites magnification, which is GCSE. The bench shows the working in its readout
sub-lines. **This is the one place in the two units where a reviewer might
reasonably want a block that is not there.**

**FLAG 5 — `d = v × t` appears three times** (`p6-06`, `p7-01`, and inside
`p6-07`'s worked example as given data). No lesson assumes the others: each
states the relationship from nothing and carries the others as edges. It is
still worth a reviewer checking that the repetition reads as reinforcement
rather than as a missing single-source ruling.

---

## 4. Where these units must teach from nothing

- **No lesson assumes sequence.** Every cross-lesson reference is an edge in
  *Connects to* or a link inside *Going further*, phrased as an offer. `p6-07`
  restates the speed of sound rather than saying "you met this in `p6-06`";
  `p7-01` restates that sound needs a medium rather than assuming `p6-06`;
  `p7-02` and `p6-07` each teach reflection from first principles for their own
  wave.
- **`p6-04` and `p7-01` both define transverse from nothing.** `p6-01` does too.
  Three definitions of the same word is deliberate: a school may run P7 before
  P6, or Waves before Motion and forces.
- **`p7-06` and `p7-07` are two halves of colour and neither depends on the
  other.** `p7-06` establishes that white light is a mixture; `p7-07` restates
  that in one clause before using it.
- **`p6-09` restates what ultrasound is** rather than depending on `p6-08` for
  the 20 000 Hz boundary.

---

## 5. The benches: one practical each, and the whole state space

| Lesson | Instrument | Reachable states | Notes authored |
|---|---|---|---|
| `p6-01` | Ripple tank, 1.00 m across | 8 amplitudes × 9 wavelengths | 3 branches keyed to **steepness** (height ÷ wavelength): breaking, ordinary, low swell. Every state falls in one band; both live values named in every branch. |
| `p6-02` | Two paddles in one channel | 11 × 11 amplitudes × 2 phases | 5 branches keyed to **what the two waves do**: nothing running, one wave only, adding, cancelling exactly, partly cancelling. |
| `p6-03` | Source and detector, 0.5 m apart | 5 sources × 2 detectors | 5 source notes × 2 detector clauses, so all 10 states carry a note. |
| `p6-04` | Slinky, 1.20 m, driven two ways | 2 drives × 21 marker positions | 6 branches keyed to **which region the marked coil sits in**: crest, trough, crossing; compression, rarefaction, between. |
| `p6-05` | Signal generator and oscilloscope | 20 frequencies × 10 amplitudes | 3 branches keyed to **pitch band**, each with an always-present second sentence naming the other dial's independence with live figures. |
| `p6-06` | Striker and microphone across a gap | 5 materials × 20 distances | 5 branches keyed to **which material**, each interpolating the live distance and comparing with the same gap in air. Vacuum is its own branch and reports "it never arrives". |
| `p6-07` | Shout at a surface | 100 distances × 5 surfaces | 3 branches keyed to **why there is or is not an echo**: too little returns, too close in time, both conditions met. |
| `p6-08` | One tone, one listener | 7 listeners × 101 frequencies | 3 branches keyed to **where the tone sits relative to that listener's band**: inside, below, above; each names a second species at the same frequency. |
| `p6-09` | Ultrasonic gauge on a block | 3 materials × 40 depths | 3 branches keyed to **which material**, each naming the live depth, path and echo time and comparing with another material at the same depth. |
| `p7-01` | Flash and bang, set off together | 101 distances × 2 media | 2 branches keyed to **whether there is a medium**; the vacuum branch names the air time for the same gap so the difference is never implicit. |
| `p7-02` | Ray box on four surfaces | 17 angles × 4 surfaces | 4 branches keyed to **which surface**, each naming the live angle and the fraction leaving. |
| `p7-03` | Ray into a rectangular block | 15 angles × 3 materials | 3 material branches × a zero-angle branch, so the straight-through state is its own note rather than a special case of a bend. |
| `p7-04` | Pinhole camera | 19 object distances × 11 box lengths × 3 holes | 3 branches keyed to **hole width**, each naming the live picture height, blur and brightness and stating that the height did not move. |
| `p7-05` | Eye and camera, same scene | 2 instruments × 5 light levels | 2 branches keyed to **which instrument**, each naming both openings at the current light level. |
| `p7-06` | Ray box, prism, screen | 4 inputs × 2 second-prism states | 3 branches: single-colour input, white recombined, white dispersed. |
| `p7-07` | One lamp, one object, dark room | 5 objects × 4 lamps | 3 branches keyed to **what the surface can send back**: nothing, everything, some. All 20 states covered. |

Deliberate consequences of the audit findings:

- **No bench narrates its own controls.** No lead sentence says which readout to
  watch. Every lead is either the physical set-up or an instruction.
- **No figure the instrument computes is hard-coded in prose.** Every number in
  every bench sentence is interpolated from the same state the readouts use. The
  worked examples are the only fixed numbers, and each is a stated scenario in
  its own heading.
- **Every comparative label is computed.** `p6-02`'s verdict word, `p6-07`'s
  three-way verdict, `p7-07`'s "almost black" and `p6-08`'s "inside / below /
  above" are all derived from the live values, never authored per control.
- **Every control is modelled and its effect stated.** `p7-04` has three
  controls and the note names what each one did and, crucially, what the hole
  width did *not* do. `p7-06`'s second prism has an authored consequence.
- **Every quantity the lesson names is readable as a number.** Amplitude and
  wavelength in mm, frequency in Hz, speeds in m/s, times in s or ms, depths in
  mm, angles in degrees, pupil widths in mm, echo fractions in per cent.
- **One practical per bench.** The bell jar in `p6-06` is described in the hook
  and in *Going further* and is not an instrument; the bench there is a single
  striker-and-microphone range. `p6-09`'s bench is a flaw gauge only, and the
  four applications are a figure. See FLAG 8 for the one deliberate exception.
- **Log scales where the data demands them.** `p6-08`'s auditory ranges span
  1 Hz to 110 000 Hz and `p7-01`'s distances 1 m to 100 km; both axes multiply by
  ten at every mark, and both say so on the face of the drawing. `p6-06`'s
  speeds span a factor of fifteen and take a linear bar, which fits.

---

## 6. Safeguarding

`p6-08` and `p7-05` and `p6-09` carry the block. All three name **Childline,
0800 1111**, inline, in small type, at the bottom edge above the legal line, and
each says the service is free, confidential, open at any hour and does not
require a name. This closes audit finding 6.4 for these three pages: the
corpus-wide sweep that returned zero now returns three.

- `p6-08` — hearing damage is the student's own body, the loss is permanent, and
  the block is worded around ringing ears and creeping volume.
- `p7-05` — the eye, retinal damage from the Sun, welding arcs and lasers, and a
  line about telling someone the same day if sight changes.
- `p6-09` — medical scanning and physiotherapy, worded around anxiety about a
  scan that has been mentioned to you.

No other lesson in the two units touches a student's own body, health or risk.

---

## 7. Misconception ids — pre-allocated, not minted

`docs/ks3/misconception-register.md` lists no opened family for waves, sound or
light, and states that nothing in an authored lesson may cite an unopened
family. Access here is read-only, so **no id is cited on any page.** Ranges are
reserved below so parallel batches cannot collide, with the last of each four as
the named spare.

| Lesson | Range | Spare |
|---|---|---|
| `p6-01` … `p6-09` | `WAVE-01` … `WAVE-36`, four per lesson in slot order | last of each four |
| `p7-01` … `p7-07` | `LIGHT-01` … `LIGHT-28`, four per lesson in slot order | last of each four |

Authored so far, awaiting minting:

| Proposed id | Statement, as a student holds it | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `WAVE-01` | The water travels along with the wave. | `hook-gull` | `s-think`, `s-tank` | `p6-01` |
| `WAVE-02` | A bigger wave is a longer wave. | `gate-deeper-dip` | `s-think`, `s-tank` | `p6-01` |
| `WAVE-05` | When two waves cancel they destroy each other. | `gate-crest-on-trough` | `s-think`, `s-meet` | `p6-02` |
| `WAVE-06` | If the water is flat the energy has gone. | *(none — nothing asks for this commitment)* | `s-think` | `p6-02` |
| `WAVE-07` | Two waves meeting average out. | `r1` | `r1` | `p6-02` |
| `WAVE-09` | Sound is made by the air, not by the object. | `hook-throat` | `s-think`, `s-chain` | `p6-03` |
| `WAVE-10` | If you cannot see it moving it is not vibrating. | `gate-tuning-fork` | `s-think` | `p6-03` |
| `WAVE-11` | A microphone is a quiet loudspeaker. | `r2` | `r2` | `p6-03` |
| `WAVE-13` | Sound is transverse, because it is drawn as a wavy line. | `hook-slinky`, `r2` | `s-think`, `s-compare` | `p6-04` |
| `WAVE-14` | In a compression the air travels to your ear. | `gate-cone` | `s-think`, `s-slinky` | `p6-04` |
| `WAVE-17` | A loud note is a high note. | `hook-guitar` | `s-think`, `s-signal` | `p6-05` |
| `WAVE-18` | A higher note travels faster. | `r2` | `s-think`, `r2` | `p6-05` |
| `WAVE-19` | Turning the volume up adds vibrations each second. | `gate-double-frequency` | `s-signal` | `p6-05` |
| `WAVE-21` | Sound crosses a vacuum, faintly. | `hook-jar` | `s-think`, `s-range` | `p6-06` |
| `WAVE-22` | Sound is fastest in air, because air is easiest to get through. | `gate-steel-vs-air` | `s-think`, `s-range` | `p6-06` |
| `WAVE-25` | An echo is a new sound the wall makes. | *(none)* | `s-think` | `p6-07` |
| `WAVE-26` | Soft materials stop sound travelling. | `r2` | `s-think`, `r2` | `p6-07` |
| `WAVE-27` | The distance to the cliff is speed × time. | `hook-cliff`, `r1` | `s-bar`, `r1` | `p6-07` |
| `WAVE-29` | A dog whistle makes no sound. | `hook-whistle`, `gate-30khz` | `s-think`, `s-range` | `p6-08` |
| `WAVE-30` | Losing the top of your range just makes things quieter. | *(none)* | `s-think` | `p6-08` |
| `WAVE-33` | Ultrasound gets through solids where ordinary sound cannot. | `r2` | `s-think`, `r2` | `p6-09` |
| `WAVE-34` | A scan looks at what comes out of the other side. | *(none)* | `s-think`, `s-gauge` | `p6-09` |
| `LIGHT-01` | Light is instant. | `hook-storm` | `s-think`, `s-race` | `p7-01` |
| `LIGHT-02` | Light is slowed by empty space, or needs something to travel in. | `r2` | `s-think`, `r2` | `p7-01` |
| `LIGHT-05` | Rough surfaces break the law of reflection. | `gate-mirror-to-paper` | `s-think`, `s-ray` | `p7-02` |
| `LIGHT-06` | Angles are measured from the mirror. | `r1` | `s-think`, `r1`, `s-beam` | `p7-02` |
| `LIGHT-09` | The straw really bends in water. | `hook-straw` | `s-think`, `s-inout` | `p7-03` |
| `LIGHT-10` | Light bends because the water pushes it sideways. | `gate-along-the-normal` | `s-think`, `s-block` | `p7-03` |
| `LIGHT-13` | The pinhole flips the picture, so a lens flips it back. | `hook-pinhole` | `s-think`, `s-lens` | `p7-04` |
| `LIGHT-14` | A bigger hole makes a bigger picture. | `r2` | `s-think`, `s-camera` | `p7-04` |
| `LIGHT-17` | Your eyes send something out in order to see. | `r2` | `s-think`, `r2` | `p7-05` |
| `LIGHT-18` | In the dark you see because your pupils open, and that is all. | `hook-dark` | `s-think`, `s-eye` | `p7-05` |
| `LIGHT-21` | The prism adds the colour. | `hook-prism`, `gate-where-were-they` | `s-think`, `s-prism` | `p7-06` |
| `LIGHT-22` | A rainbow has seven colours with lines between them. | *(none)* | `s-think`, `s-band` | `p7-06` |
| `LIGHT-25` | An object has a colour and the light just reveals it. | `hook-jumper`, `gate-red-under-green` | `s-think`, `s-lamp` | `p7-07` |
| `LIGHT-26` | A red filter turns white light red. | *(none)* | `s-think` | `p7-07` |

Five entries have no `elicited_by`, which §5.3 allows: nothing on those pages
asks the student to commit to the belief, and each is confronted because it sits
underneath one that is elicited.

---

## 8. Distractors (MRB-177), and hedges that are load-bearing

Every ladder distractor in the sixteen lessons is a **wrong rule in the correct
answer's own shape**. Four worth pointing at:

- `p6-02` r1 option C is *"5 mm — take the average, because the surface can only
  be in one place at a time"*. The premise is correct and the rule drawn from it
  is wrong, which is exactly why students reach for it.
- `p6-05` r2 option D is the **right verdict with the wrong rule** — *"They
  arrive together, because the band members are all the same distance away"* —
  and is marked wrong because the reasoning is what is assessed.
- `p6-07` r1 option A, *"1020 m — multiply the speed by the time and that is the
  distance to the cliff"*, is the correct first step offered as the whole answer.
  It is the single most common wrong answer in this topic and the correction says
  so.
- `p7-02` r2 option D, *"Paper is not shiny enough"*, is answered with crumpled
  foil, which separates shiny from smooth in one object.

Rungs 3 and 4 are written as checks on an answer, not recipes: each criterion
names a thing that must be *present in what you wrote*, and every rung 4 is
reachable from the lesson alone. Where an answer needs an order, the word is
written into the criterion (`p6-03` r4 criterion 5 says "the two stretches").

Hedges that must not be tidied:

- **"about"** on every speed of sound, every auditory range, every reflection
  percentage and every material speed in `p6-09`. Removing it turns typical
  values into claims.
- **"about 340 m/s"** for sound in air, with **"at about 20 °C"** wherever it is
  qualified. It rises roughly 0.6 m/s per degree.
- **"roughly 1 in 7"** for the breaking steepness in `p6-01`; it varies with
  depth, wind and how the wave was made.
- **"about a tenth of a second"** and **"roughly 17 m"** in `p6-07`. Both are
  approximate thresholds fixed so the states can be reached.
- **"almost black"** everywhere in `p7-07`, never "black". Real dyes and real
  lamps are broad bands; the perfect case does not occur.
- **"qualitative"** discipline in `p7-03`, `p7-04` and `p7-06`: no refractive
  index, no magnification formula, no wave equation.
- **"300 000 000 m/s"** is stated as a rounded figure and the exact 299 792 458
  m/s is given in the legal line and *Going further* of `p7-01`.
- **"typical"** on every source amplitude and rate in `p6-03`, and on the pupil
  and aperture widths in `p7-05`.
- **"about two thirds"** for the speed of light in glass in `p7-03`.
- The `.ks3-legal` line on all sixteen pages discloses what the bench leaves out
  and which numbers are conventions rather than measurements.

---

## 9. Flags for review

1. **FLAG 1–5 above** are the substantive ones: clause-level ownership (data
   model), `p6-01`'s deliberate silence on frequency, `p6-09` and `p7-04`
   computing without a block, and `d = v × t` appearing three times.
2. **FLAG 6 — the steel speed of sound is 5000 m/s here and published values run
   5000–5900 m/s.** 5000 is used in `p6-06` and `p6-09` for consistency and the
   legal line on `p6-09` says the range. If the corpus standardises on 5900, both
   pages and one rung need changing together.
3. **FLAG 7 — auditory ranges differ between sources.** The figures used
   (human 20–20 000, dog 67–45 000, cat 45–64 000, bat 2000–110 000, elephant
   16–12 000, mouse 1000–91 000) are the commonly published set, and studies
   disagree partly because they disagree about how quiet a sound must be before
   an animal counts as hearing it. The legal line says so. **Contested enough to
   be worth a reviewer's source of record.**
4. **FLAG 8 — `p7-05`'s bench holds two instruments.** An eye and a camera are
   switched by a toggle, which brushes against "one practical per bench". It is
   deliberate: the comparison *is* the lesson, the toggle names which instrument
   is drawn, and the whole drawing changes with it, so a student is never left
   with two answers to "describe the apparatus". A reviewer should ratify or ask
   for two figures instead.
5. **FLAG 9 — `--ks3-data` still does not exist** (repeat of P4/P5 FLAG 1).
   These pages use `--ks3-blue-light` for selection on ink-dark blocks and
   `--ks3-accent` / `--ks3-accent-tint` on cream, always with a word in the state
   so hue is never the only channel. Amber appears only in misconception blocks
   and the FIFA reveal panel's eyebrow. **Either the token needs adding or audit
   law 9 needs amending.**
6. **FLAG 10 — `p7-06` and `p7-07` use hue as part of the message.** Colour is
   the subject, so it cannot be avoided; every state also carries the colour as a
   word in the readout tiles and in the note, and the ladder questions are
   answerable from the words alone. The screen colours are declared in the legal
   line as approximations of spectral colours.
7. **`p6-01`'s ripple tank draws both axes to one scale** so the 1-in-7 steepness
   claim is drawable. That makes the largest amplitude 35 px on a 1000-wide
   viewBox. It is deliberate: exaggerating the vertical would have made the
   drawn geometry contradict the label.
8. **Four rail stops on every page**, per the brief and matching B9–B11 and
   P4/P5. `NOTES-C9.md` §10 records five citing the same MRB-249; if five is
   current this is a one-line change per lesson.
9. **No practical in these two units needs a risk assessment beyond ordinary
   classroom practice.** Two are worth a teacher's eye and are described rather
   than instructed: the bell jar in `p6-06` (evacuated glass, screened) and any
   demonstration of a prism in a sunbeam in `p7-06` (never through a lens, never
   towards a face). `p7-05` carries the only hard prohibition on the page itself:
   never look at the Sun, a welding arc or a laser.
10. **Nothing was committed to the repo.** Read-only access, as instructed: no
    branch, no commit, no register edit, and no prompt written for Code was run.

---

## 10. For Code — component families registered

**New families minted by this group**

| Family | Debuts in | What it is |
|---|---|---|
| `ripple-tank` | `p6-01` | A side-on tank drawn to one scale in both directions, a sine surface built as a single sampled path, a float at mid-tank riding the surface, and a swing gauge with arrowheads showing twice the amplitude. Data: `{amp, wavelength, tankWidth}`. |
| `wave-anatomy` | `p6-01` | A fixed reference wave with a four-way selector; the chosen part is drawn as a dimension line or a set of markers, and the unselected state shows the wave with nothing marked and its own note. |
| `superposition-lanes` | `p6-02` | Three stacked traces on one px-per-millimetre scale — two inputs and their sum — with a phase toggle that inverts the second. Draws a flat line rather than nothing at zero amplitude. |
| `vibration-chain` | `p6-03` | A source drawn from a per-source path pair (shape plus dashed extremes) with a motion arrow, columns of air bunched and spread, and a detector diaphragm. Data: `{sources[], detectors[]}`. |
| `stage-strip` | reused from `p4-06` | The fixed four-column process figure, reused by `p6-03` for source → air → sheet → signal. |
| `slinky-dual` | `p6-04` | One slinky rendered either as a sampled transverse curve or as a row of coil ticks whose positions carry a longitudinal displacement, with a marked coil, its rest position dashed, and a motion arrow that switches between across and along. |
| `scope-trace` | `p6-05` | An oscilloscope window of fixed duration with time ticks, a sampled trace at a chosen frequency and amplitude, and an amplitude bracket. Both axes to one scale. |
| `medium-range` | `p6-06` | A striker and a microphone with a settable gap, the medium drawn as its own particle pattern (scattered dots, close rows, or a linked lattice), and a distance dimension line. Refuses to report a speed for a vacuum and prints "it never arrives". |
| `speed-bars` | `p6-06` | A fixed comparison chart: one row per material, a bar to one linear scale, a particle glyph at the row's spacing, and a zero-length row that prints words instead of a bar. |
| `echo-range` | `p6-07` | A figure and a wall at a distance drawn to scale, an outgoing arrow at full weight and a returning arrow whose stroke width is the fraction reflected, dashed below the audible threshold, plus a distance dimension line. |
| `surface-bars` | `p6-07` | Fixed bars of the fraction reflected for five surfaces, with a dashed threshold line drawn across the chart and labelled. |
| `log-range-axis` | `p6-08` | A decade axis with literal decade labels, a species band drawn as a rect between two logarithms, and a movable marker. Reused by `p7-01` for distance. **The family exists because a linear bar cannot carry these ranges.** |
| `range-chart` | `p6-08` | A fixed multi-row version of the same axis with the human band shaded behind every row and the infrasound / ultrasound boundaries drawn as dashed lines. All geometry computed from logarithms at build time. |
| `flaw-gauge` | `p6-09` | A block in cross-section with a probe, a reflector at a depth drawn to scale, down and up arrows, a depth dimension, and a timing trace with a sent pip at zero and an echo pip placed to scale in a fixed window. |
| `use-panels` | `p6-09` | A four-panel figure split into energy uses and information uses, each with its own drawn glyph and frequency. |
| `two-speed-race` | `p7-01` | Two arrows on one log distance axis, one reaching the far end and one stopping short and dashed when there is no medium, with both arrival times as HTML labels. |
| `ray-surface` | `p7-02` | A ray box on a selectable surface profile (flat, wavy, faceted), a dashed normal, incidence and reflection arcs, and either one reflected ray or a fan of five, thinned and faded when most of the light is absorbed. |
| `balance-beam` | `p7-02` | The equality figure: two bars of identical length with tie lines and an equals sign, **no cover buttons**, following the `p1-08` ruling. The third member of the beam family alongside `beam-part-whole` and `beam-opposing`. |
| `refraction-block` | `p7-03` | A rectangular block with a ray refracted at both faces, angles computed and drawn to scale, a second normal at the exit face, and a dashed continuation of the original direction to compare against. |
| `apparent-depth` | `p7-03` | A fixed figure: a straw in a glass, one ray refracting at the surface to an eye, and a dashed back-projection to the apparent position, both positions marked. |
| `pinhole-camera` | `p7-04` | Object and image arrows drawn to one height scale, with the hole placed along the axis so the drawn rays stay straight at any ratio; blur is the stroke width of the image arrow, to the same scale, with a minimum. |
| `lens-pair` | `p7-04` | Two fixed lens diagrams: parallel rays to a focus, and an object to an inverted image through three rays. |
| `eye-camera` | `p7-05` | One cross-section that switches wholesale between an eye and a camera, with the opening drawn to scale in millimetres, a lens, an absorbing surface and an inverted image arrow that follows whichever back surface is in use. |
| `prism-bench` | `p7-06` | A prism with an input beam of selectable composition, up to six coloured output rays fanned to fixed angles, and an optional second inverted prism that recombines them. |
| `spectrum-band` | `p7-06` | A fixed six-segment band with the names below it and two arrows underneath pointing the same way — frequency, and how far a prism bends it. |
| `colour-bench` | `p7-07` | A lamp, an object rectangle filled with the computed seen-colour, and an outgoing ray that is drawn dashed and grey when nothing is reflected. Every colour also stated as a word. |

**Reused unchanged from B1–P5**: `ks3-nav`, the top and side progress rails,
`ks3-hook` with `ks3-options`, `ks3-explainer`, `ks3-block ks3-dark ks3-practical`,
`[data-key-fact]`, `ks3-misconception`, `ks3-ladder` with two marked and two
self-marked rungs, `ks3-keynote`, `ks3-layer`, `ks3-endmatter`, `ks3-legal`,
`formula-triangle`, `beam-part-whole`, `fifa-reveal`, `fifa-scaffold`.

**New this group and worth registering separately**: `safeguard-block` — an
`<aside>` at the bottom edge, small type, on card ground with a strong rule
border, carrying an uppercase mono eyebrow and one sentence that names Childline
and 0800 1111 inline. Debuts on `p6-08`, reused by `p6-09` and `p7-05`. **This is
the family audit finding 6.4 asked for and no page in the corpus had.**

**Notes for the generator**

- **Live labels on a diagram are HTML, not `<text>`.** Every value label in these
  sixteen pages is an absolutely-positioned `<span>` over a `position: relative`
  wrapper whose percentages match the viewBox. Fixed captions stay as literal
  `<text>`. Attribute holes (`d`, `x`, `width`, `transform`) are unaffected. The
  `<span>`-in-SVG failure is silent, so this is not optional.
- **No `<sc-for>` inside an `<svg>` anywhere.** Repeated marks — coil ticks,
  particle grids, air columns, ray fans — are built as one path string in
  `renderVals()`.
- All instruments are DOM and inline SVG. No canvas, no timers, no animation
  loop, no `Math.random()` anywhere in the group.
- Every arrow, tick and cross is inline SVG. No `→`, `✓` or `✕` character appears
  in any of the sixteen files; a build check for those three characters passes.
- Props: `showDraft` only, as everywhere else in the build.
- Every page is a standalone `.dc.html` with its own `support.js` and `_ds`
  folder alongside it, matching P4 and P5.
- Forward and back links use the `.html` form of the slug, matching P5.
