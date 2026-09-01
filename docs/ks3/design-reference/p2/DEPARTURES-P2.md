# DEPARTURES — P2, *Energy at home*

One row per change to Claude Design's delivered content, under Mide's
standing ruling of 24 Aug 2026. The column that matters is **the defect** —
not "why mine is better", but what was WRONG with hers. A row that cannot
fill that column cleanly is not a departure; it is a preference, and her
version stands.

Her page is the DEFAULT and the STRUCTURE. Nothing here re-plans a lesson,
re-cuts a rail or changes what a lesson covers.

**Expect this to be short.** A long register means rewriting to taste.

---

## CHANGED — 2 rows

### D-P2-01 · `p2-01 energy-in-food` · the calorimeter's sample mass

| | |
|---|---|
| **What she wrote** | `<input id="mass" type="range" min="5" max="30" step="1">` — a burnt sample of 5 g to 30 g, against `WATER_G = 20` and `SHC = 4.18`, with `rise = (consumed × kJperG × capture × scatter × 1000) / (WATER_G × SHC)`. |
| **What I wrote** | The same instrument, the same water, the same constant, the same four foods and the same capture fractions. Only the slider's range: **0.10 g to 0.50 g, step 0.05, starting at 0.30 g.** |
| **THE DEFECT** | **The thermometer reads a temperature liquid water cannot have, in every state the instrument can reach.** Her own arithmetic, run on her own constants, gives a rise of 275 °C at the slider's MINIMUM (5 g of the weakest food at the lowest scatter) and 4449 °C at its maximum — a water temperature of 295 °C to 4469 °C in a boiling tube. There is no setting of food, mass or scatter that produces a physically possible reading. It is scientifically incorrect; a student can check it against the one number about water they are certain of; and it contradicts the lesson's own instrument, whose canvas draws warmth as `min(1, rise / 60)` and is therefore drawn for rises up to 60 °C. |

**What this does NOT change, and the reason the fix is this one:** the value
the lesson actually teaches is `measured = (rise × WATER_G × SHC / 1000) ÷
consumed`, which reduces to `kJperG × capture × scatter` and is **completely
independent of the sample mass**. Peanut reads 11.27 kJ/g against a 24.5
label at 0.1 g, at 0.3 g, at 12 g and at 30 g alike. So the "reads 30–46% of
the label" story, Rung 3's five criteria, the systematic-vs-random argument,
the Going-further paragraph and the CFIFA question that runs on the
student's own recorded figure are all arithmetically untouched. The
scientific defect is removed and not one teaching number moves.

The range was chosen so that **every** combination of the four foods and the
±10% scatter stays below boiling: 0.30 g gives 38 °C for cheese and dry
pasta, 53 °C for crisps, 60 °C for peanut. That is also what the real school
practical does — a fraction of a gram under 20–25 cm³ of water — so the
bench now agrees with the apparatus its own prose describes.

Her prose is untouched: "a boiling tube holding 20 g of water" was already
correct and stays.

⊕ **AMENDED 31 Aug 2026 — the two peanut figures in this row are the record
of what the bench held when D-P2-01 was written, and are kept rather than
corrected.** The peanut has since been ruled out of the practical; see
D-P2-02. On today's bench the same 0.30 g gives 18 °C for cheese and dry
pasta, 33 °C for crisps and 30 °C for the cheese puff, and the highest
`kJperG × capture` is the crisps' 9.24 rather than the peanut's 11.27 — so
the boiling-point margin this row bought is wider now, not narrower.

⊕ **CORRECTED 1 Sep 2026 (MRB-297) — the amendment above quietly changed
the QUANTITY, and so read as a correction of figures that were never
wrong.** It is kept above rather than rewritten in place, because the two
sets of numbers look like a disagreement and are not one, and a later
reader who "reconciles" them will break the row's argument.

**Both sets are right. They are different quantities.** The engine's
`riseNow()` is `consumed × kJperG × capture × scatter × 1000 / (WATER ×
SHC)`, and `paint()` prints TWO readouts from it: `rise`, and `temp` which
is `START + rise` with `START` = 20 °C. At 0.30 g into 20 g of water at
scatter 1.0:

| food | `kJperG × capture` | rise | temp = 20 + rise |
|---|---|---|---|
| Cheese (17.0 × 0.30) | 5.10 | 18.30 °C | **38.30 °C** |
| Dry pasta (15.0 × 0.34) | 5.10 | 18.30 °C | **38.30 °C** |
| Crisps (22.0 × 0.42) | 9.24 | 33.16 °C | **53.16 °C** |
| Cheese puff (21.6 × 0.38) | 8.21 | 29.45 °C | **49.45 °C** |
| Peanut, retired (24.5 × 0.46) | 11.27 | 40.44 °C | **60.44 °C** |

So the original row's "38 °C for cheese and dry pasta, 53 °C for crisps,
60 °C for peanut" are the FINAL TEMPERATURES, and are exact. The 31 Aug
amendment's "18 °C … 33 °C … 30 °C" are the RISES for three of the same
states, and are also right (the cheese puff is 29.45, so 29 rather than
30). Nothing about the peanut swap moved cheese or pasta, and nothing
could have: neither food's constants were touched.

⚠️ **AND THE ROW'S ARGUMENT ONLY WORKS ON THE TEMPERATURE.** The claim
being made is that every combination "stays below boiling". A rise of
18 °C is not a fact about boiling; 38.30 °C is. Restated as rises, the
sentence stops supporting its own conclusion. The conclusion still holds
at the top of the scatter band, which is the case it was chosen for: at
scatter 1.1 the hottest state on today's bench is the crisps at 56.47 °C,
and even the retired peanut only reached 64.49 °C.

What the amendment was right about stands: the peanut is out, and the
highest `kJperG × capture` a student can now reach is the crisps' 9.24
rather than the peanut's 11.27, so the boiling-point margin is wider than
when D-P2-01 was written. **D-P2-01 needed no correction of its figures —
only that note about the margin.**

---

### D-P2-02 · `p2-01 energy-in-food` · the peanut comes out of the practical

| | |
|---|---|
| **What she wrote** | `{ id: 'peanut', label: 'Peanut', kJperG: 24.5, capture: 0.46 }` as the bench's second sample and its default (`startFood: 'Peanut'`), noted as "the highest of the four … the classic school sample"; the commit-gate option "A peanut — it is mostly fat"; and Rung 3, "Your calorimeter gives 9 kJ per gram for a peanut. The packet says 24 kJ per gram." |
| **What I wrote** | A cheese puff in the same slot, same default: **`kj_per_g` 21.6, `capture` 0.38.** 21.6 is the UK nutrition label — 2156 kJ per 100 g, 516 kcal, fat 30.3 g per 100 g. 0.38 is a modelling constant, not a measurement, and the reasoning is in the file: a puffed snack is mostly air, so it flares fast and loses more sideways than a dense nut, which puts it below the peanut's 0.46 and inside the ruled 0.30–0.46 band. The gate option becomes "A cheese puff — it is mostly fat" and Rung 3 is re-derived: 21.6 × 0.38 = 8.2 measured against a 21.6 label. |
| **THE DEFECT** | **A nut sample in a classroom practical, ruled out by Mide on 30 Aug 2026.** Not a wording problem and not something a safety note reaches: a child who reacts to airborne particles from burning nut is not protected by a line of prose. The instrument, the water, the constant, the other three foods, the capture band and every rung's teaching are unchanged. |

**What this costs, stated rather than hidden:** the peanut was the highest of
the four and the cheese puff is not — the crisps at 22.0 kJ/g now top the
bench. No non-nut classroom food beats a crisp on energy density, because a
crisp is already about a third fat and near the ceiling for a dry snack,
while nuts led precisely because they are about half fat. The figure was NOT
adjusted to preserve the old ordering. The sample's note is rewritten to say
what is true of a puff instead, and "the classic school sample" is deleted
with the peanut it described.

**Swept beyond P2, and it leaves the physics lane.** The ruling is about nuts
in classrooms, not about this bench, so `ks3_data/b3/lesson_02_food_tests.py`
rung 1 — a crushed peanut in the ethanol emulsion test — takes double cream
instead. Same order, same correct option, same teaching, every option the
same word count. Two nut mentions were left alone because nothing is handled:
B5's hazelnut as an example of a fruit, and B9's almond as a
pollinator-dependent crop.

---

## ENGINE POLICY, APPLIED — not departures

These changed Design's WORDS, so they are recorded here in the open rather
than buried. Neither is a claim that her science was wrong; both are
key-stage-wide gates that were RED on her option sets, and a red gate is not
something this run may override.

| What | Why it is policy rather than a departure |
|---|---|
| **The `ks3-review-flag` "Draft — not yet science-reviewed" line is not shipped.** It is on all five of her pages by default. | MRB-221 revoked the review marker. Standing engine policy for every unit, identical for B1–C10, and it takes no register row. Swept by CONCEPT — "draft", "review", "not yet checked", "provisional" — not by class name, because that language once survived on 297 pages by hiding in `LEGAL_LINE`. Built P2 pages: **zero hits.** |
| **Three option sets had their weights evened out.** `p2-03`'s two marked rungs (correct 3w against a longest distractor of 2w, and 13w against 7w) and `p2-04`'s bill-builder gate (6w against 4w). | MRB-177: no option set may give its answer away by length — a student can score those without reading them. Her CLAIMS are unchanged and in her order in all three; only the weights move. ⚠️ Worth naming the defect honestly: it is an ASSESSMENT defect, not a science one, and it does not clear the science bar Mide set. It is here because the gate was red and this run does not override gates. |
| **Ladder answers spread across all four positions.** All ten of the unit's marked rungs put the correct option at index 0. | MRB-278: no index may hold more than half a corpus. Now 3/3/2/2. Her four claims and four feedback lines are unchanged in every rung — only the order. ⚠️ The feedback map is keyed by option INDEX, so the rotation was done structurally and asserted: reordering options without rewriting those keys attaches every explanation to the wrong distractor, and the page still renders. |

---

## CONSIDERED, NOT CHANGED

These were weighed and HER VERSION STANDS. Recorded so Mide can see what was
looked at and rejected, not just what was altered.

| Lesson | What was considered | Why hers stands |
|---|---|---|
| `p2-01` | Her science flag 3 offers **4.2 kJ per kcal** instead of 4.18 "for arithmetic simplicity". | 4.18 is kept — and not merely because it is more precise. Her hook quotes a real packet, 229 kcal / 958 kJ, and 229 × 4.18 = 957.2, which rounds to the printed 958. At 4.2 it gives 961.8 and the hook stops landing on the number the student can read off the bag. Changing it would break her own page. No defect in hers; a defect would be created by changing it. |
| `p2-01` | Her capture fractions make the bench read 30–46% of the label. Tempting to "fix" them upward so the measurement agrees with the packet. | That gap IS the lesson, and Rung 3 criterion 5 — that repeating a measurement does nothing about a systematic leak — can only be answered by a student who has watched their own value come out low. Her flag 1 says so explicitly. Nothing wrong with hers. |
| `p2-01` | Her Think-again distinguishes burning in air from respiration at 37 °C. | Correct as written, and correctly hedged ("nearly identical"). Biology-adjacent but not biology's to own — B3 references this lesson. No defect. |
| `p2-01` | Fat ≈ 37 kJ/g, carbohydrate ≈ 17 kJ/g quoted in prose (her flag 5). | Standard values, correctly stated as approximations, consistent with her four foods' densities. No defect. |
| `p2-02` | Her Think-again says swapping to a **lower-wattage kettle can cost slightly more** (her flag 7, flagged as examiner-sensitive). | It is correct — a lower-power kettle takes longer and loses more to the room over that longer time — and it is the counter-intuitive case that makes the power/energy distinction bite. Correct science is not a defect, and "a reviewer might query it" is not one either. Stands. |
| `p2-02` | Her Going further calls Watt's horsepower figure "arguably deliberately" generous — a claim about motive (her flag 8). | A hedged historical judgement, marked as a judgement by the word "arguably". Not a science claim and not something a student carries into GCSE as a misconception. Stands. |
| `p2-03` | The canvas states "W × min IS ALWAYS WRONG" flatly (her flag 9). | The flatness is the point: the ×60 error is the lesson's whole misconception, and a hedge would weaken the one sentence that has to stick. It is also true. Stands. |
| `p2-03` | Her Going further uses the 1999 Mars Climate Orbiter loss, $327 m and ~170 km. | Checkable and checked: the mission cost is standardly given as $327.6 m and the trajectory error put it roughly 170 km lower than intended. Accurate. Stands. |
| `p2-04` | 27p/kWh and 53p/day standing charge (her flag 12) — plausible mid-2020s UK values that will date. | Dating is not a defect, they are correctly presented as an example rather than a live tariff, and she has already isolated them as two named constants for exactly this reason. Stands. |
| `p2-05` | **Nuclear placed as non-renewable and low-carbon; wood as renewable and high-carbon** (her flag 15, flagged as politically sensitive). | Both are scientifically correct, and the two cells are the entire confrontation of the "renewable means clean" belief — if either were softened the grid would have empty corners and the misconception would survive. Sensitivity is not a defect. Stands, unsoftened. |
| `p2-05` | Her carbon and reliability figures are relative positions on 0–1, not measured data (her flag 17). | Correctly labelled as positions rather than values, and the lesson's claim is about ORDERING, which is what a relative position can honestly carry. Stands. |
