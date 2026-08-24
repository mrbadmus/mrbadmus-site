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

## CHANGED — 1 row

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
