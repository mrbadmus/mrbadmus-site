# DEPARTURES — P10, *Magnetism and electromagnetism*

Every difference between Claude Design's five delivered pages and the five
built lessons, and nothing else. MRB-205: she draws, we render; her page wins
outright, and a difference is either a row here or it is a revert.

Method: **her JavaScript constants, never her rendered HTML.** A `.dc.html`
renders its ladder, hook, gate and readouts from `{{ }}` holes, so an
HTML-to-HTML comparison sees holes on both sides and reports a match. Her
`RAIL`, `RUNGS`, `SELF_RUNGS`, `OBJS`, `SETUPS`, `LATS`, `TURNS`, `DIRS` and
the rest were extracted with `tools/extract_design_payload.js`; her
`renderVals()` bodies were read directly and ported — arithmetic into
`shared/ks3.js`, every student-facing sentence into the lesson record as an
authored template.

**Five of the rows below were found by ENUMERATING her own models over their
whole state space** — 150, 100, 54, 150 and 32 states — rather than by reading
her §4 table. Her branch COUNTS all match her table exactly. Three of her
branch PREDICATES do not divide the space the way their own sentences claim,
and one number format prints a real field as zero.

---

## 1. Changed

| # | Where | What she drew | What is built | Why |
|---|---|---|---|---|
| 1 | `p10-02` bench · the neutral point | `nullPoint = rel < 0.6` — a threshold on the READING | a CANCELLATION test: the vector sum of the poles' contributions against the sum of their sizes, `< 0.02` | **Measured over all 100 states her test fires 17 times and is right once.** Ten of the sixteen false positives are on the horseshoe, which has no neutral point at all. The note printed at every one of them reads *"they cancel and the total is zero — not weak, zero"* and *"This is called a neutral point"* — the exact distinction her own *Going further* calls *"one of very few places in physics where a quantity is exactly nothing rather than merely small"*. At the true null the ratio is **0.000**; at the next-nearest state it is **0.298**. Two orders of magnitude, nothing in between. `r_compass_plot` refuses a payload with any count of reachable nulls but one. |
| 2 | `p10-02` bench · what 100 means | 100 = the strongest point on the 13 × 7 ARROW LATTICE | 100 = the strongest of the 25 spots the compass can be put on; readout reworded to *"the strongest spot you can reach here"* | Her reference sits hard against a pole, where no button on the grid can go. Measured across all four layouts: **the highest reading a student can ever obtain on her scale is 18.05**, her top band (`very strong`, ≥ 40) is unreachable, and **78 of the 96 readings fall into the single bottom band**. A scale whose top is invisible is not the scale the readout claims. Bands re-cut to 45 / 18 / 6 / 0, which now hold 20 / 24 / 27 / 24 states. |
| 3 | `p10-03` bench · the flat note at the equator | one `flat` branch: *"…not because the field is level — at {place} the field itself is running into the ground at {dip}°"* | a second branch, `flat_level`, for latitude 0 | At the equator dip IS 0.0 and the field IS level, so her sentence renders *"…running into the ground at 0°"* while denying that the field is level. Two reachable states (flat, at the equator, with nothing or with the steel stand). The new branch still names the mounting — the reading is still a fact about the clamp — and adds that here the clamp and the field agree. |
| 4 | `p10-03` bench · the navigability verdict | `horizRel < 12` → *"barely — it is sluggish"* | `horizRel < 40` | **Unreachable as drawn.** Measured across her own nine latitudes the sideways pull runs 100.0, 94.0, 76.6, 61.6, 50.0, 34.2, 0.0 — nothing is below 12 except the pole, which has its own branch. So the verdict is copy no student can ever see, while **her rung 4 asks the student to explain precisely that state**. At 40 exactly one latitude reads it, 70° north at 34.2, and that is the latitude the rung is written about. Compasses are sold in balancing zones for this reason, so the claim is defensible as well as reachable. `r_dip_circle` refuses a `nav_at` no latitude in the list falls below. |
| 5 | all four relative scales · number format | `toFixed(1)` everywhere | one decimal at or above 1, TWO below it, and a bare `0` where the rounded figure is zero | Measured on `p10-04`: `toFixed(1)` prints **`0.0` for nine real on-states** — six in the strength tile (10 turns at 0.2 A and at 0.5 A, 20 turns at 0.2 A, each with air or with the plastic former) and three in the iron branch's *"drops to 0.0"* — on a page whose own tile insists *zero, not merely small*. A small field that prints as zero confirms `MAG-15` instead of breaking it. `p10-01` already used two decimals for its own lowest band; this is her convention applied to all four. The bare `0` is for `100 × cos(90°)`, which floating point makes 6e-15 and which printed `0.00` on the one page whose argument is that there is no sideways pull left. |
| 6 | `p10-04` · the empty core's wording | one string, `"nothing at all — the coil is empty"`, interpolated into two different sentences | two phrasings per core: `with_phrase` (reads after *with*) and `down_phrase` (reads before *down the middle*) | Her string renders *"…or that there is nothing at all — the coil is empty down the middle"* and *"…40 turns carrying 1.0 A with nothing at all — the coil is empty holds 4 paper clips"* — ungrammatical, in **50 of the 150 states**. The editor-cut law: a seam is re-authored so it lands as a sentence. Her wording is otherwise untouched. |
| 7 | all five bench leads | each ends with a clause naming the controls already on screen | that clause cut; `p10-04`'s lead cut entirely | 5A.1: *"If the paragraph above a bench describes buttons that are already on screen, cut it… cut outright rather than trimmed."* What stays on the other four is the SET-UP — the one thing a student cannot see for themselves: that the track is frictionless, that bearings run clockwise from the top of the page, that the compass is hung at its centre, that the coil is drawn face on. `p10-04`'s lead was four clauses of controls and nothing else. |
| 8 | `p10-03` · the globe's aria label | *"a globe with a tilted bar magnet drawn inside it"* | *"a bar magnet drawn inside it along the spin axis"* | Her `barPath` is `M690 100 H750 V300 H690 Z` — axis-aligned. MRB-254: a description is the whole drawing to a reader who cannot see it, and shipping a knowingly false one because it is the designer's is the wrong reading of MRB-205. Her own legal line says the model lines the magnet up WITH the spin axis, so the DRAWING is right and the sentence was not. Also row 1 of §3 below. |
| 9 | all five benches · the pressed segmented button | the engine's shared dark rule paints it `--ks3-alert` | `--ks3-data`, scoped to P10's five block classes | MRB-252 ruled that **amber warns and never merely labels**, and that category and selection uses move to `--ks3-data`; a pressed tab on a bench is selection and nothing else. Design's own `seg()` in all five files draws exactly that — `--ks3-blue-light` ground with ink text, and `--ks3-blue-light` is what `--ks3-data` is valued at. The shared rule dates from MRB-242, before MRB-252 existed. ⚠️ **Scoped, not changed at source**: that rule dresses every dark segmented control in the key stage and repainting it would move B1's fit tabs and every unit since. Ink on `--ks3-data` is 8.2:1. The corpus-wide question is §5. |
| 10 | every fixed SVG caption | `fill: #8C8177` — 3.08:1 on `--ks3-dark-panel` at 15px | `var(--ks3-on-dark-muted)` — 6.09:1 | Below AA for body-size text, and the exact case `shared/tokens.css` warns about beside that token. P9 rows 1–2 are the precedent and this is the same ruling applied again. Her `#C6B9A7` IS `--ks3-on-dark-muted` to the byte, so every stroke drawn in it moves nowhere. |
| 11 | the meaningful graphics | `#6E6357` — 2.05:1 — for the field lattice, the Earth's field arcs, the solenoid's field loops, `p10-05`'s field lines and its dashed leads | `#8C8177` — 3.08:1 | 3:1 is the bar for a graphic that carries meaning, and every one of these does: the lattice IS the field map, the loops ARE the solenoid's field. `#8C8177` is a colour already on her own drawings, and each stays a step below the instrument mark above it, which is the hierarchy she drew. |
| 12 | `p10-01` · the track | `stroke: #4A4139` — 1.6:1 | `var(--ks3-on-dark-muted)` | The one line on the drawing the caption under it is about (*FREE TO SLIDE EITHER WAY*), and effectively invisible as drawn. |
| 13 | `p10-02` and `p10-05` · the pole letters' tone | fixed at two literal colours per page | an attribute the wiring sets, so the tone follows which half the letter is standing on | On `p10-05` **both** letters are drawn at `#15110C`; only one of the two is ever on the filled pole face, and the other is near-black on the near-black magnet body at **1.1:1** — invisible in half of the 32 states, and it is the letter that names the pole. On `p10-02` her four literals are right for her four layouts and wrong the moment a bar is turned round. Ink on `--ks3-data` is 8.2:1; `--ks3-on-dark-muted` on the body is 6.09:1. |
| 14 | `p10-01` · the Childline block | a bordered `<aside>` with a mono eyebrow and 15px body | the engine's `safeguarding_note` slot: `ks3-legal` type, bottom edge, above the legal line | **MRB-257 audit 6.4, ruled by Mide 19 Aug 2026**, puts the confidential service in small type at the bottom edge and says in terms that it is NEVER a callout block. Her own §5 describes the placement she wanted in exactly those words — *"inline, small type, bottom edge, above the legal line"* — so her §5 and the ruling agree and only her markup differs. Her eyebrow (*"If a magnet has been swallowed, or you are worried about someone"*) becomes the opening condition of the sentence so that no wording of hers is lost; the `<strong>` around the number is dropped because the slot is plain text. Every other word is character for character, including *Childline is free on 0800 1111*. |
| 15 | `p10-01` commit gate, option D | *"It does nothing either time, because a nail is not a magnet"* (12 words) | *"…because only a magnet can be pushed or pulled by another magnet"* (17 words) | MRB-177. Her correct option is 17 words against a longest distractor of 12 — a tell at the ≥4-word threshold, and a tell on a GATE does the most damage of all, because a student who spots the answer never commits and a belief nobody commits to cannot be confronted. **Remedied at the distractor**, which now states its wrong rule completely. The correct answer is untouched. That rule is `MAG-04`, and the id is minted from this option. |
| 16 | `p10-03` rung 2, the calibration option | *"Compasses made today are calibrated differently from compasses made then"* (10 words) | *"…are calibrated to a different north from the ones that were made forty years ago"* (18 words) | MRB-177: correct 19 words against a longest distractor of 13. Remedied at the distractor; her own correction (*"A compass is not calibrated at all — it is a magnet on a pivot"*) answers the finished version word for word and is untouched. |
| 17 | three bank questions | — | one distractor lengthened in each of `p10-03-h04`, `p10-05-s03`, `p10-05-h04` | MRB-177, same remedy, same rule: never shorten a correct answer, never move an index for a tell, never edit a correction. |
| 18 | statutory ownership | §1 gives `MAG.02` to three lessons and `MAG.04` to two, with *"That is correct and needs no notation"* | `MAG.01/.02/.03` owned once each; `MAG.04` split at its own comma into `.04a` (`p10-04`) and `.04b` (`p10-05`); `p10-03` carries `MAG.02` as a **touch** | architecture.md §4.4 rule 3 makes `covers` exactly-once across the key stage and `verify_ks3` asserts it, so a second claim on a parent is a build failure rather than a duplicate. The bullet reads *"the magnetic effect of a current, electromagnets, D.C. motors (principles only)"* and the split falls at the second comma, where every scheme of work splits it. `p10-05` carries `MAG.02` neither way: it draws a field between two magnets and never plots one with a compass, and a `touches` a page does not do is worse than none. See `ks3_data/substatements.py`. |
| 19 | three legal lines | — | one clause added to each | Each discloses something the port made true and the page does not otherwise say: `p10-01` and `p10-02` that the force arrows and the lattice arrows are **clamped** at both ends rather than drawn to scale; `p10-03` that whether a steel object beside the compass wins is decided by a single latitude standing in for a comparison that really depends on size and distance; `p10-04` that the coil is drawn as eight loops at every setting and the chain to ten clips however many are held. Her §8's hedges are load-bearing and every one of them survives unchanged. |

---

## 2. Considered, not changed

| Where | What it is | Why it stands |
|---|---|---|
| `p10-01` · the `nothing` note | *"…nothing moves at any other setting either: try the gap and watch the arrows stay away."* | It names a control and the drawing, which is what 5A.1 cuts — but the rule is about the paragraph ABOVE a bench, and this is a note INSIDE one that teaches a falsification move. Kept verbatim. |
| `p10-01` · `verdictSub` | her `bothMag ? '' : '…'` inside the not-acting branch, where `bothMag` is always false | A dead ternary, not a wrong string. The one reachable value is authored directly. |
| `p10-04` · *"The right-hand end is: a north pole"* | never varies; the bench has no reverse control | True in all 75 on-states, and the note beside it explains what reversing the leads would do. Adding a control she did not draw to make a tile move would be the MRB-205 violation, not the fix. |
| `p10-04` · the gate and rung 2 | both ask what happens to the clips when the switch is opened | Hers, and deliberate: the gate takes the commitment BEFORE the bench and the rung checks it after. A before/after pair on one page is not a restatement. |
| `p10-05` · the turning effect at 0.5 A | prints `13` for a computed 12.5, against a friction of `15` | `toFixed(0)`, hers, and the note says *"worth about 15"*. Her §8 makes the *about* load-bearing. |
| the five band figures | carry `data-stage-done="0"` and no control of their own | Correct and required: the declaration is what `check_nothing_ticks_on_load` reads out of the shipped bytes, and the absence of a control is why the bench marks it. `ks3_instrument_liveness` derives them as STATIC and names them, which is the honest outcome. |
| the band figures' grid | Design draws `minmax(min(240px…))`, `250px` and `260px` on three different pages | Unified at 250px. One stylesheet serves five figures of the same shape; three values for one grid is drift with nothing behind it. |
| every fixed SVG caption's SIZE | 15px in a 1000-unit viewBox → **3.8px at 360, 4.3px at 390, 10.1px at 820** | Measured, and **P9's shipped benches are identical to the pixel** (`ELECTRONS`, `LEFT HAND`, `INSULATING STANDS ON A BENCH` all give 3.8 / 4.3 / 10.1). This is a corpus-wide property of every dark bench, not a P10 defect, and the MRB-254 remedy — a declared `min-width` plus a scroller — would make P10's five figures behave differently from P9's three in the same week. Reported in §5 rather than fixed in one unit. |

---

## 3. Notes versus drawing

Where her NOTES and her DRAWING disagree, the drawing was measured and the
drawing is what is built.

| Her note says | Her page measures | Which was built |
|---|---|---|
| §7: *"a globe carrying a **tilted** internal bar magnet"* | `barPath = 'M690 100 H750 V300 H690 Z'` — axis-aligned, and her legal line says the model lines the magnet up **with** the spin axis | **The drawing.** The bar is drawn along the axis and the aria label now says so (§1 row 8). The eleven-degree tilt the real Earth has is in the legal line as the thing the model leaves out, which is where it belongs. |
| §4: *"Every comparative label is derived at render… The equal case was driven and checked on each."* | two of the five are derived from a PROXY rather than from the property they name — `p10-02`'s neutral point from a threshold on the reading, `p10-03`'s navigability from a threshold no latitude reaches | **Neither, as drawn.** Both corrected (§1 rows 1 and 4). The claim is true of the other three. |
| §2 table: *"`p10-02` … relative field strength, 100 = strongest point on that map"* | 100 is a lattice point no button can reach; the readable maximum is 18.05 | **The claim, made true.** The reference moved to a spot the compass can be put on rather than the sentence being softened (§1 row 2). |
| §6: *"No id is cited on any page… Ranges reserved so parallel batches cannot collide, last of each four the named spare."* | five spares, and all five have a real belief behind them in a gate or a rung distractor | **The content.** All twenty are minted, each from a named option; this register does not hold ids against future need. See `docs/ks3/misconception-register.md`. |
| §1: *"`MAG.02` and `MAG.04` are each claimed twice. That is correct and needs no notation."* | `verify_ks3` asserts `covers` exactly once across the key stage | **The register's rule.** §1 row 18. |
| §7: *"`--ks3-data` is not in the design-system copy bound to this project, so P10 does not use it yet."* | `shared/tokens.css` carries it (MRB-252) | **The engine.** Used directly, no fallback written. Her own token-law addendum grants it *"from P10 onward"* and asks for the fallback only because her copy lacks it. |

---

## 4. Engine policy — no register row

* **MRB-278 · position is authored.** All four of Design's marked rungs per
  page, her hooks and four of her five commit gates put the correct answer at
  index 0. Her option TEXT and every correction are verbatim; only the ORDER
  moves. Across the unit: hooks 2, 0, 3, 1, 2 · gates 3, 2, 0, 2, 1 · rungs
  1, 2 · 3, 0 · 2, 1 · 0, 3 · 3, 1. The bank is 15 / 15 / 15 / 15 over 60
  questions. `p10-02`'s gate is the one marked set in the whole delivery that
  was not at 0 — hers is at 2 and it is kept there.
* **Draft chrome dropped.** Every page carries `<p class="ks3-review-flag">
  Draft — not yet science-reviewed.</p>` behind a `showDraft` prop. MRB-221
  revoked the under-review marker and `verify_ks3` asserts its absence. Not
  ported, on any page.
* **No keyword block; vocabulary authored from her own definitions.** Her
  physics deliveries supply no keyword block, and `verify_ks3` requires every
  authored lesson to carry `vocabulary`. Four terms per lesson, each taken
  from a term her page puts in bold and defines in the same sentence — pole,
  north-seeking pole, magnetic material, magnetised · magnetic field, field
  line, plotting compass, neutral point · compass needle, angle of dip,
  declination, true north · electromagnet, solenoid, core, soft iron · coil,
  turning effect, split-ring commutator, brushes. No `keyword` block is
  placed on any page.
* **Her aria descriptions are ported and kept live**, recomputed on every
  repaint, so each one describes the state actually on screen. The one that
  described something not drawn is §1 row 8.
* **Two SVG class renames**, internal to `ks3_art/p10.py`: the dip bench's
  level LINE and the motor's axle CIRCLE collided with the overlay spans
  named `level` and `axle`, because `_wrap` names every span
  `ks3-<hook>-<key>`. Renamed `-levelline` and `-axlepin`.
* **The latitude list is keyed on `deg`, not on `id`.** A latitude has no id —
  it is its number.
* **The overlay spans hang off an inner bare div, not the padded panel.**
  Found by LOOKING at `p10-05`: the left magnet's `N` sat half off the pole
  face it names. Every live label is placed at a percentage read straight off
  the viewBox, so the box it resolves against has to BE the SVG's box; hung
  off the padded panel the error is `36f − 18` px — nothing at the centre,
  eighteen pixels at either edge, and always outwards. Design's own markup has
  the inner div and does nothing else with it. This was a porting defect of
  mine, not a departure from her, and it is recorded because the next unit
  will copy this shell.
* **TWO AUTHORING SLIPS THAT THE ENGINE SWALLOWED IN SILENCE**, both mine,
  both caught by measurement rather than by reading, and both recorded because
  the next unit will copy this shell.

  * `p10-05` was authored with `references: [{"unit": "P4", "lesson":
    "turning-forces"}]`. **That slug does not exist anywhere in the key
    stage** — P4's lesson on the turning effect of a force is `moments` — and
    the engine DROPPED the edge without a word: the built page simply carried
    one reference where two were authored, `build_ks3.py` exited 0, and every
    gate stayed green. Found by resolving every P10 edge against
    `ks3_data.build_units()` by hand. A `references` entry naming a
    non-existent lesson is a dead authored key that `ks3_key_audit` cannot see,
    because the key IS read — it is its VALUE that resolves to nothing.
  * `p10-03`'s confronting explainer was authored with `id:
    "no-bar-down-there"`. **`_id_attr` reads `anchor` and only `anchor`** —
    `id` names the ACTIVITY a block renders, and reading it as an anchor would
    put an activity's name in the URL. So the explainer shipped with no
    `id=` at all and `MAG-11`'s `confronted_by` pointed at an element that was
    never on the page. Caught by MRB-244's gate on the built bytes, which is
    exactly what that gate exists for, and fixed by authoring `anchor`.

* **No `_head` in this module.** `r_activity`'s shell owns the eyebrow, the
  `<h2>` and the progress readout; P4, P5 and P6 each define a `_head` AND
  author `progress`, and every one of their benches ships its heading twice on
  a live page. Measured on the built P10 bytes: one heading, one eyebrow, one
  readout per bench.

---

## 5. Could not resolve, or belongs to somebody else

1. **The fixed SVG captions are illegible on a phone, on every dark bench in
   the key stage.** Measured, on the built pages: 15px in a 1000-unit viewBox
   renders at **3.8px at 360, 4.3px at 390 and 10.1px at 820** — and P9's
   shipped `charging-by-rubbing` and `forces-between-charges` give exactly the
   same three numbers. MRB-254's remedy is a declared `min-width` on the
   figure plus a scroller; applying it to P10's five figures alone would make
   them behave differently from P9's three in the same week, which is the
   inconsistency the corpus keeps paying for. Reported rather than fixed in
   one unit: the honest shape is one change across every `ks3-dark
   ks3-practical` figure, with its own gate.

2. **The rail does not survive a reload, on any lesson in the key stage.**
   Driven: all four stops tick on all five P10 pages (4 / 4), and after a
   reload the count is 0 / 4. Measured against the shipped `p9-02` and
   `p8-01` with the same script: identical. The engine stores the ladder's
   WORK and its BEST score (`ks3_work_<slug>`, `ks3_ladder4_<slug>`) and
   restores neither the marked answers nor the rail. Engine behaviour on 199
   live lessons; `shared/ks3.js` is a shared file and changing the rail's
   restore would move every KS3 page, so it is a separate unit of work.

3. **The pressed dark segmented button is amber corpus-wide.** §1 row 9 fixes
   it for P10's five blocks only. MRB-252's ruling is general and the shared
   rule predates it; every other unit's dark benches still paint selection in
   the warning colour. One rule, one line, one gate — but it repaints eleven
   units' approved pages and is not a content lane's call.

---

## 6. What was measured, and how

| Bench | States enumerated | Her branch counts | Measured |
|---|---|---|---|
| `track-pair` | 5 × 5 × 6 = **150** | nothing 102 · repel 12 · attract 12 · induced 24 | **exact match** |
| `compass-plot` | 4 × 25 = **100** | on the metal 4 · one neutral point | 4 · **17 as drawn**, 1 as built |
| `dip-circle` | 9 × 3 × 2 = **54** | magnet 18 · steel 4 · flat 16 · tipped 15 · pole 1 | **exact match** |
| `solenoid-bench` | 5 × 5 × 3 × 2 = **150** | off 75 · iron 25 · air 25 · plastic 25 | **exact match** |
| `motor-coil` | 2 × 2 × 2 × 4 = **32** | never 8 · keeps 12 · stops 12 | **exact match** |

Every one of those 486 states was then driven in a headless browser, a fresh
one per page, and checked for an empty note, an empty tile, a tile still at
its em-dash placeholder and a surviving `{token}`. **Zero findings.** The
equal and zero states were driven on purpose: `p10-01`'s 102 states of
nothing, `p10-02`'s neutral point, `p10-03`'s clamped-flat zero and its
vertical needle at the pole, `p10-04`'s 75 switched-off states and its
weakest real field, `p10-05`'s eight states that never start.
