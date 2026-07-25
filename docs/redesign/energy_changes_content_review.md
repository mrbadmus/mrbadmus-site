# Energy Changes unit — content review (MRB-105)

_AQA 5.5 Energy Changes (plus the Triple-only electrochemistry pages: cells, batteries and fuel cells). Drafted for Mide's review before the Phase 2 merge. Every question, its options (✔︎ = correct), and a diagnostic line for each wrong option are shown here — you never need to read the Python._

## How the tiers work (the difficulty model you set)

- **Difficulty follows the tier, not the pathway.** Combined-Foundation and Triple-Foundation are the **same difficulty**; Combined-Higher and Triple-Higher both **scale up** to genuine Higher demand.
- **Triple's extra is coverage, not a harder version of the same content.** Triple-Foundation = the exact Combined-Foundation set **+ extra Foundation-level questions**; Triple-Higher = the exact Combined-Higher set **+ extra Higher/depth questions**. So Foundation students see the same difficulty on both pathways, and Triple students simply get more.
- **Every stem is exam-register** (uses an AQA command word) and **every wrong option carries a diagnostic** naming the misconception or error. On the calculation pages every distractor encodes a classic slip (added instead of subtracted, swapped break/make, dropped the sign, forgot the J→kJ conversion).
- **Counts:** Combined 10 / tier, Triple 12 / tier (10 + 2 extra). Some pages exist only at certain tiers — see each page's note.

### Page map (tier presence detected from the four data files)

| Page | CF | CH | TF | TH | AQA |
|---|:--:|:--:|:--:|:--:|---|
| Exothermic and Endothermic Reactions | ✓ | ✓ | ✓ | ✓ | 5.5.1.1 |
| Reaction Profiles | ✓ | ✓ | ✓ | ✓ | 5.5.1.2 |
| Bond Energy Calculations | — | ✓ | — | ✓ | 5.5.1.3 |
| Cells and Batteries | — | — | ✓ | ✓ | 4.5.2.1 |
| Fuel Cells | — | — | ✓ | ✓ | 4.5.2.2 |

### ⭐ Full-review checklist (per the review-tiering rule)

All calculation / derivation items and all FIFA are flagged ⭐ for your full review; recall/comprehension items are left for your sampling. The ⭐ items are:

- **Exothermic and Endothermic Reactions** — 4 calc/derivation item(s); FIFA worked examples (foundation, higher)
- **Reaction Profiles** — 3 calc/derivation item(s); FIFA worked examples (foundation, higher)
- **Bond Energy Calculations** — 8 calc/derivation item(s); FIFA worked examples (higher)

### Audit status (self-checked with `audit_content.py`)

- **Before:** every energy-changes cell shipped only 2 Test-Yourself questions (count-criticals on all 16 cells), Common Mistakes that opened with a statement rather than a named mistake, and no real differentiation between Foundation and Higher or between Combined and Triple — the same defect pattern the Bonding audit surfaced.
- **After (chemistry `energy-changes` pages only):** **zero critical, zero content majors, zero minors.** The only remaining flags are:
  - **10 systemic `2-practice-absent` majors** — one per FIFA cell (exothermic-endothermic ×4, reaction-profiles ×4, bond-energy-calculations ×2). The current template renders static FIFA steps only; wiring the interactive step-by-step practice is the redesign port's job (**MRB-113**), **not** a content defect.
  - **2 `info` `4-menu` notes** on `fuel-cells` (Triple-Foundation and Triple-Higher) — the page keeps its overall equation (2H₂ + O₂ → 2H₂O) but has no numeric FIFA. That is deliberate: fuel-cells is a conceptual page and the equation is a chemical equation, not a calculation. Info-level only.
- The critical/major rows the raw audit shows against the string "energy-changes" belong to a **different, out-of-scope unit** — `physics/energy/energy-changes-in-systems` — which shares the substring but is not part of AQA 5.5.

---

## Exothermic and Endothermic Reactions  ·  `exothermic-endothermic`  ·  AQA 5.5.1.1

> 🚩 **Triple-depth call (your review):** MATCHED — AQA 5.5.1.1 (exothermic/endothermic reactions and their energy changes) is identical for Combined and Triple, and is taught at both tiers. Foundation difficulty is the same on both pathways; Triple sets = Combined + extra same-difficulty coverage. Higher adds real calorimetry arithmetic (J→kJ, per-mole, rearrangement), not a harder badge on the same questions.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often think that because an endothermic reaction takes energy IN, it must make the surroundings feel hotter — and that a negative ΔH means the reaction has 'lost' energy and gone wrong. Both are back to front. An endothermic reaction absorbs energy FROM the surroundings, so the surroundings get COLDER (the temperature falls); an exothermic reaction releases energy TO the surroundings, so they get HOTTER. And a negative ΔH is simply the label for exothermic — energy released — not a sign that anything is lost or wrong; a positive ΔH means energy absorbed (endothermic).

**Question sets by tier** (each item shows tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (4 recall / 6 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** A camping stove burns butane and the surroundings get hotter. Deduce whether the reaction is exothermic or endothermic, and give a reason.
- [✔︎] Exothermic — it releases energy to the surroundings, so their temperature rises
- [ ] Endothermic — energy is taken in, which is what makes the surroundings feel hot
    - *why wrong:* This reverses the idea: endothermic reactions take energy IN and make the surroundings COLDER. Releasing energy (exothermic) is what warms them.
- [ ] Endothermic — burning always absorbs energy from the air
    - *why wrong:* Burning (combustion) RELEASES energy — it is exothermic. It needs a little energy to start, but far more is given out.
- [ ] Neither — the heat comes from the match, not the reaction
    - *why wrong:* The match only supplies the energy to start it; the sustained heat is released by the exothermic combustion itself.

**Q2. [apply · CFCHTFTH]** When ammonium nitrate is stirred into water the beaker feels cold. Predict whether dissolving it is exothermic or endothermic, and explain the temperature change.
- [✔︎] Endothermic — it absorbs energy from the water, so the water's temperature falls
- [ ] Exothermic — the cold shows energy is being released
    - *why wrong:* A temperature FALL means energy is being absorbed FROM the surroundings — that is endothermic, not exothermic.
- [ ] Endothermic — energy is released, cooling the water
    - *why wrong:* Endothermic is the right label, but the reason is wrong: endothermic means energy is ABSORBED, not released.
- [ ] Neither — dissolving is never an energy change
    - *why wrong:* Dissolving does involve energy changes; here energy is absorbed, which is exactly how instant cold packs work.

**Q3. [reason · CFCHTFTH]** Describe what happens to the energy of the surroundings during an exothermic reaction and during an endothermic reaction.
- [✔︎] Exothermic: energy is transferred TO the surroundings (they heat up). Endothermic: energy is taken FROM the surroundings (they cool down)
- [ ] Exothermic: the surroundings cool. Endothermic: the surroundings heat up
    - *why wrong:* This is the wrong way round — exothermic HEATS the surroundings; endothermic COOLS them.
- [ ] Both transfer energy to the surroundings, warming them
    - *why wrong:* Only exothermic warms the surroundings; endothermic absorbs energy and cools them.
- [ ] Both take energy from the surroundings, cooling them
    - *why wrong:* Only endothermic cools the surroundings; exothermic releases energy and warms them.

**Q4. [reason · CFCHTFTH]** Explain why the temperature of the reaction mixture rises during the neutralisation of an acid with an alkali.
- [✔︎] Neutralisation is exothermic — it releases energy to the mixture, so its temperature rises
- [ ] The mixture absorbs energy from the surroundings as it reacts
    - *why wrong:* Absorbing energy would make it COLDER; a temperature rise shows energy is being released (exothermic).
- [ ] The acid and alkali are already hot before they are mixed
    - *why wrong:* The rise is caused by the reaction releasing energy, not by the starting temperature of the reactants.
- [ ] Stirring the mixture adds energy and heats it up
    - *why wrong:* Stirring adds a negligible amount of energy; the heating is due to the exothermic neutralisation reaction.

**Q5. [apply · CFCHTFTH]** A student adds a reactant to a solution and the temperature falls by 6 °C. Determine the type of reaction and state the sign of its enthalpy change, ΔH.
- [✔︎] Endothermic, ΔH is positive — energy was absorbed from the solution, so it cooled
- [ ] Exothermic, ΔH is negative — energy was released, cooling the solution
    - *why wrong:* A temperature FALL means energy was absorbed (endothermic, positive ΔH); releasing energy would warm the solution.
- [ ] Endothermic, ΔH is negative — energy was absorbed
    - *why wrong:* Endothermic is right, but a positive ΔH goes with endothermic; a negative ΔH is exothermic.
- [ ] Exothermic, ΔH is positive — energy was released
    - *why wrong:* Both parts are wrong: a temperature fall is endothermic, and exothermic reactions have a NEGATIVE ΔH.

**Q6. [recall · CFTF]** State what happens to the temperature of the surroundings during an exothermic reaction.
- [✔︎] It increases (the surroundings get hotter)
- [ ] It decreases (the surroundings get colder)
    - *why wrong:* A temperature decrease is endothermic; exothermic reactions release energy and warm the surroundings.
- [ ] It stays exactly the same
    - *why wrong:* Exothermic reactions release energy, which raises the temperature of the surroundings.
- [ ] It falls to below 0 °C every time
    - *why wrong:* Exothermic reactions raise the temperature; they do not cool anything, let alone below freezing.

**Q7. [recall · CFTF]** State the sign of the enthalpy change, ΔH, for an exothermic reaction.
- [✔︎] Negative
- [ ] Positive
    - *why wrong:* A positive ΔH is endothermic (energy absorbed); an exothermic reaction releases energy, so ΔH is negative.
- [ ] Zero
    - *why wrong:* ΔH is zero only if there is no energy change; an exothermic reaction releases energy, so ΔH is negative.
- [ ] It has no sign
    - *why wrong:* ΔH always carries a sign: negative for exothermic, positive for endothermic.

**Q8. [recall · CFTF]** Name an everyday product that works by an endothermic change.
- [✔︎] An instant cold pack (for example, for a sports injury)
- [ ] A hand warmer
    - *why wrong:* A hand warmer gets HOT, so it is exothermic — the opposite of endothermic.
- [ ] A self-heating food can
    - *why wrong:* Self-heating cans release energy to warm the food, so they are exothermic, not endothermic.
- [ ] A burning candle
    - *why wrong:* A burning candle releases heat and light — combustion is exothermic.

**Q9. [recall · CFTF]** Name the piece of equipment used to reduce heat loss when measuring a temperature change in a school calorimetry experiment.
- [✔︎] A polystyrene (expanded-foam) cup
- [ ] A glass beaker
    - *why wrong:* Glass conducts heat away quickly; a polystyrene cup insulates far better and reduces heat loss.
- [ ] A metal can
    - *why wrong:* Metal is a good conductor, so it would lose heat rapidly — the opposite of what is wanted.
- [ ] A gas syringe
    - *why wrong:* A gas syringe measures the volume of gas, not a temperature change; a polystyrene cup is used for calorimetry.

**Q10. [apply · CFTF]** A thermometer reading rises from 21 °C to 29 °C during a reaction. Calculate the temperature change and state whether the reaction is exothermic or endothermic.
- [✔︎] ΔT = 8 °C; exothermic (the temperature rose)
- [ ] ΔT = 8 °C; endothermic (the temperature rose)
    - *why wrong:* The temperature change is right, but a RISE in temperature means exothermic, not endothermic.
- [ ] ΔT = 50 °C; exothermic
    - *why wrong:* ΔT is the DIFFERENCE, 29 − 21 = 8 °C, not the two readings added together.
- [ ] ΔT = 29 °C; exothermic
    - *why wrong:* ΔT is the change (29 − 21 = 8 °C), not the final reading.

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** A camping stove burns butane and the surroundings get hotter. Deduce whether the reaction is exothermic or endothermic, and give a reason.
- [✔︎] Exothermic — it releases energy to the surroundings, so their temperature rises
- [ ] Endothermic — energy is taken in, which is what makes the surroundings feel hot
    - *why wrong:* This reverses the idea: endothermic reactions take energy IN and make the surroundings COLDER. Releasing energy (exothermic) is what warms them.
- [ ] Endothermic — burning always absorbs energy from the air
    - *why wrong:* Burning (combustion) RELEASES energy — it is exothermic. It needs a little energy to start, but far more is given out.
- [ ] Neither — the heat comes from the match, not the reaction
    - *why wrong:* The match only supplies the energy to start it; the sustained heat is released by the exothermic combustion itself.

**Q2. [apply · CFCHTFTH]** When ammonium nitrate is stirred into water the beaker feels cold. Predict whether dissolving it is exothermic or endothermic, and explain the temperature change.
- [✔︎] Endothermic — it absorbs energy from the water, so the water's temperature falls
- [ ] Exothermic — the cold shows energy is being released
    - *why wrong:* A temperature FALL means energy is being absorbed FROM the surroundings — that is endothermic, not exothermic.
- [ ] Endothermic — energy is released, cooling the water
    - *why wrong:* Endothermic is the right label, but the reason is wrong: endothermic means energy is ABSORBED, not released.
- [ ] Neither — dissolving is never an energy change
    - *why wrong:* Dissolving does involve energy changes; here energy is absorbed, which is exactly how instant cold packs work.

**Q3. [reason · CFCHTFTH]** Describe what happens to the energy of the surroundings during an exothermic reaction and during an endothermic reaction.
- [✔︎] Exothermic: energy is transferred TO the surroundings (they heat up). Endothermic: energy is taken FROM the surroundings (they cool down)
- [ ] Exothermic: the surroundings cool. Endothermic: the surroundings heat up
    - *why wrong:* This is the wrong way round — exothermic HEATS the surroundings; endothermic COOLS them.
- [ ] Both transfer energy to the surroundings, warming them
    - *why wrong:* Only exothermic warms the surroundings; endothermic absorbs energy and cools them.
- [ ] Both take energy from the surroundings, cooling them
    - *why wrong:* Only endothermic cools the surroundings; exothermic releases energy and warms them.

**Q4. [reason · CFCHTFTH]** Explain why the temperature of the reaction mixture rises during the neutralisation of an acid with an alkali.
- [✔︎] Neutralisation is exothermic — it releases energy to the mixture, so its temperature rises
- [ ] The mixture absorbs energy from the surroundings as it reacts
    - *why wrong:* Absorbing energy would make it COLDER; a temperature rise shows energy is being released (exothermic).
- [ ] The acid and alkali are already hot before they are mixed
    - *why wrong:* The rise is caused by the reaction releasing energy, not by the starting temperature of the reactants.
- [ ] Stirring the mixture adds energy and heats it up
    - *why wrong:* Stirring adds a negligible amount of energy; the heating is due to the exothermic neutralisation reaction.

**Q5. [apply · CFCHTFTH]** A student adds a reactant to a solution and the temperature falls by 6 °C. Determine the type of reaction and state the sign of its enthalpy change, ΔH.
- [✔︎] Endothermic, ΔH is positive — energy was absorbed from the solution, so it cooled
- [ ] Exothermic, ΔH is negative — energy was released, cooling the solution
    - *why wrong:* A temperature FALL means energy was absorbed (endothermic, positive ΔH); releasing energy would warm the solution.
- [ ] Endothermic, ΔH is negative — energy was absorbed
    - *why wrong:* Endothermic is right, but a positive ΔH goes with endothermic; a negative ΔH is exothermic.
- [ ] Exothermic, ΔH is positive — energy was released
    - *why wrong:* Both parts are wrong: a temperature fall is endothermic, and exothermic reactions have a NEGATIVE ΔH.

**Q6. [calc/derivation · CHTH] ⭐** In a calorimetry experiment, 25.0 g of solution rises in temperature by 12.0 °C. Using c = 4.18 J/g °C, calculate the energy released, in kJ.
- [✔︎] 1.254 kJ (Q = 25.0 × 4.18 × 12.0 = 1254 J = 1.254 kJ)
- [ ] 1254 kJ
    - *why wrong:* This is the answer in joules (1254 J) wrongly labelled kJ; convert J→kJ by dividing by 1000, giving 1.254 kJ.
- [ ] 0.1045 kJ
    - *why wrong:* The temperature change was left out (25.0 × 4.18 = 104.5 J only). Q = m × c × ΔT needs the ×12.0 as well.
- [ ] 125.4 kJ
    - *why wrong:* A place-value slip in the J→kJ conversion: 1254 J ÷ 1000 = 1.254 kJ, not 125.4 kJ.
  > 🚩 **Reviewer note:** Calorimetry with a J→kJ conversion. Please full-review.

**Q7. [calc/derivation · CHTH] ⭐** A reaction transfers 2090 J of energy to 100 g of water (c = 4.18 J/g °C). Calculate the temperature rise of the water.
- [✔︎] 5.0 °C (rearrange to ΔT = Q ÷ (m × c) = 2090 ÷ 418)
- [ ] 873 620 °C — multiplied all three values
    - *why wrong:* To find ΔT you must REARRANGE to ΔT = Q ÷ (m × c); multiplying gives a nonsensical value.
- [ ] 20.9 °C — divided Q by the mass only
    - *why wrong:* You must divide by m × c (100 × 4.18 = 418), not by mass alone; 2090 ÷ 418 = 5.0 °C.
- [ ] 0.2 °C — divided (m × c) by Q
    - *why wrong:* The rearrangement is ΔT = Q ÷ (m × c), i.e. 2090 ÷ 418, not 418 ÷ 2090.
  > 🚩 **Reviewer note:** Requires rearrangement of Q = mcΔT. Please full-review.

**Q8. [reason · CHTH]** Two reactions have ΔH = −120 kJ/mol and ΔH = +65 kJ/mol. Compare them in terms of energy transfer and the temperature change you would observe.
- [✔︎] The −120 kJ/mol reaction is exothermic (releases energy, temperature rises); the +65 kJ/mol reaction is endothermic (absorbs energy, temperature falls)
- [ ] The −120 kJ/mol reaction is endothermic because its value is more negative
    - *why wrong:* A negative ΔH is exothermic regardless of size; −120 kJ/mol releases energy and warms the surroundings.
- [ ] Both are exothermic because both involve an energy change
    - *why wrong:* Only the negative ΔH is exothermic; the +65 kJ/mol reaction has a positive ΔH, so it is endothermic.
- [ ] The +65 kJ/mol reaction releases more energy because its number looks larger
    - *why wrong:* A positive ΔH means energy is ABSORBED, not released; the +65 kJ/mol reaction takes energy in (endothermic).

**Q9. [reason · CHTH]** Explain why the energy change measured in a school calorimetry experiment is usually smaller than the true value.
- [✔︎] Some energy is lost to the surroundings and the apparatus (heat escapes), so the measured temperature rise is smaller than it should be
- [ ] The reaction stops before it is finished every time
    - *why wrong:* The main cause is heat loss to the surroundings, not the reaction stopping early.
- [ ] The thermometer adds energy to the solution
    - *why wrong:* A thermometer does not add a significant amount of energy; the loss is heat escaping to the surroundings and apparatus.
- [ ] The specific heat capacity increases during the reaction
    - *why wrong:* c is taken as constant (4.18 J/g °C for water); the shortfall is due to heat loss, not a change in c.

**Q10. [calc/derivation · CHTH] ⭐** Burning 0.010 mol of a fuel releases 6.7 kJ of energy. Calculate the molar enthalpy change, in kJ/mol, and state its sign.
- [✔︎] −670 kJ/mol (6.7 ÷ 0.010 = 670; negative because combustion releases energy)
- [ ] +670 kJ/mol
    - *why wrong:* The magnitude is right (6.7 ÷ 0.010 = 670) but combustion RELEASES energy, so ΔH is negative, not positive.
- [ ] −0.067 kJ/mol — multiplied instead of divided
    - *why wrong:* Energy per mole is energy ÷ moles (6.7 ÷ 0.010 = 670), not energy × moles.
- [ ] −6.7 kJ/mol — did not divide by the number of moles
    - *why wrong:* The 6.7 kJ is for 0.010 mol; dividing by 0.010 scales it up to 670 kJ per mole.
  > 🚩 **Reviewer note:** Energy-per-mole with a sign judgement. Please full-review.

### Triple Foundation — 12 questions (4 recall / 8 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** A camping stove burns butane and the surroundings get hotter. Deduce whether the reaction is exothermic or endothermic, and give a reason.
- [✔︎] Exothermic — it releases energy to the surroundings, so their temperature rises
- [ ] Endothermic — energy is taken in, which is what makes the surroundings feel hot
    - *why wrong:* This reverses the idea: endothermic reactions take energy IN and make the surroundings COLDER. Releasing energy (exothermic) is what warms them.
- [ ] Endothermic — burning always absorbs energy from the air
    - *why wrong:* Burning (combustion) RELEASES energy — it is exothermic. It needs a little energy to start, but far more is given out.
- [ ] Neither — the heat comes from the match, not the reaction
    - *why wrong:* The match only supplies the energy to start it; the sustained heat is released by the exothermic combustion itself.

**Q2. [apply · CFCHTFTH]** When ammonium nitrate is stirred into water the beaker feels cold. Predict whether dissolving it is exothermic or endothermic, and explain the temperature change.
- [✔︎] Endothermic — it absorbs energy from the water, so the water's temperature falls
- [ ] Exothermic — the cold shows energy is being released
    - *why wrong:* A temperature FALL means energy is being absorbed FROM the surroundings — that is endothermic, not exothermic.
- [ ] Endothermic — energy is released, cooling the water
    - *why wrong:* Endothermic is the right label, but the reason is wrong: endothermic means energy is ABSORBED, not released.
- [ ] Neither — dissolving is never an energy change
    - *why wrong:* Dissolving does involve energy changes; here energy is absorbed, which is exactly how instant cold packs work.

**Q3. [reason · CFCHTFTH]** Describe what happens to the energy of the surroundings during an exothermic reaction and during an endothermic reaction.
- [✔︎] Exothermic: energy is transferred TO the surroundings (they heat up). Endothermic: energy is taken FROM the surroundings (they cool down)
- [ ] Exothermic: the surroundings cool. Endothermic: the surroundings heat up
    - *why wrong:* This is the wrong way round — exothermic HEATS the surroundings; endothermic COOLS them.
- [ ] Both transfer energy to the surroundings, warming them
    - *why wrong:* Only exothermic warms the surroundings; endothermic absorbs energy and cools them.
- [ ] Both take energy from the surroundings, cooling them
    - *why wrong:* Only endothermic cools the surroundings; exothermic releases energy and warms them.

**Q4. [reason · CFCHTFTH]** Explain why the temperature of the reaction mixture rises during the neutralisation of an acid with an alkali.
- [✔︎] Neutralisation is exothermic — it releases energy to the mixture, so its temperature rises
- [ ] The mixture absorbs energy from the surroundings as it reacts
    - *why wrong:* Absorbing energy would make it COLDER; a temperature rise shows energy is being released (exothermic).
- [ ] The acid and alkali are already hot before they are mixed
    - *why wrong:* The rise is caused by the reaction releasing energy, not by the starting temperature of the reactants.
- [ ] Stirring the mixture adds energy and heats it up
    - *why wrong:* Stirring adds a negligible amount of energy; the heating is due to the exothermic neutralisation reaction.

**Q5. [apply · CFCHTFTH]** A student adds a reactant to a solution and the temperature falls by 6 °C. Determine the type of reaction and state the sign of its enthalpy change, ΔH.
- [✔︎] Endothermic, ΔH is positive — energy was absorbed from the solution, so it cooled
- [ ] Exothermic, ΔH is negative — energy was released, cooling the solution
    - *why wrong:* A temperature FALL means energy was absorbed (endothermic, positive ΔH); releasing energy would warm the solution.
- [ ] Endothermic, ΔH is negative — energy was absorbed
    - *why wrong:* Endothermic is right, but a positive ΔH goes with endothermic; a negative ΔH is exothermic.
- [ ] Exothermic, ΔH is positive — energy was released
    - *why wrong:* Both parts are wrong: a temperature fall is endothermic, and exothermic reactions have a NEGATIVE ΔH.

**Q6. [recall · CFTF]** State what happens to the temperature of the surroundings during an exothermic reaction.
- [✔︎] It increases (the surroundings get hotter)
- [ ] It decreases (the surroundings get colder)
    - *why wrong:* A temperature decrease is endothermic; exothermic reactions release energy and warm the surroundings.
- [ ] It stays exactly the same
    - *why wrong:* Exothermic reactions release energy, which raises the temperature of the surroundings.
- [ ] It falls to below 0 °C every time
    - *why wrong:* Exothermic reactions raise the temperature; they do not cool anything, let alone below freezing.

**Q7. [recall · CFTF]** State the sign of the enthalpy change, ΔH, for an exothermic reaction.
- [✔︎] Negative
- [ ] Positive
    - *why wrong:* A positive ΔH is endothermic (energy absorbed); an exothermic reaction releases energy, so ΔH is negative.
- [ ] Zero
    - *why wrong:* ΔH is zero only if there is no energy change; an exothermic reaction releases energy, so ΔH is negative.
- [ ] It has no sign
    - *why wrong:* ΔH always carries a sign: negative for exothermic, positive for endothermic.

**Q8. [recall · CFTF]** Name an everyday product that works by an endothermic change.
- [✔︎] An instant cold pack (for example, for a sports injury)
- [ ] A hand warmer
    - *why wrong:* A hand warmer gets HOT, so it is exothermic — the opposite of endothermic.
- [ ] A self-heating food can
    - *why wrong:* Self-heating cans release energy to warm the food, so they are exothermic, not endothermic.
- [ ] A burning candle
    - *why wrong:* A burning candle releases heat and light — combustion is exothermic.

**Q9. [recall · CFTF]** Name the piece of equipment used to reduce heat loss when measuring a temperature change in a school calorimetry experiment.
- [✔︎] A polystyrene (expanded-foam) cup
- [ ] A glass beaker
    - *why wrong:* Glass conducts heat away quickly; a polystyrene cup insulates far better and reduces heat loss.
- [ ] A metal can
    - *why wrong:* Metal is a good conductor, so it would lose heat rapidly — the opposite of what is wanted.
- [ ] A gas syringe
    - *why wrong:* A gas syringe measures the volume of gas, not a temperature change; a polystyrene cup is used for calorimetry.

**Q10. [apply · CFTF]** A thermometer reading rises from 21 °C to 29 °C during a reaction. Calculate the temperature change and state whether the reaction is exothermic or endothermic.
- [✔︎] ΔT = 8 °C; exothermic (the temperature rose)
- [ ] ΔT = 8 °C; endothermic (the temperature rose)
    - *why wrong:* The temperature change is right, but a RISE in temperature means exothermic, not endothermic.
- [ ] ΔT = 50 °C; exothermic
    - *why wrong:* ΔT is the DIFFERENCE, 29 − 21 = 8 °C, not the two readings added together.
- [ ] ΔT = 29 °C; exothermic
    - *why wrong:* ΔT is the change (29 − 21 = 8 °C), not the final reading.

**Q11. [apply · TF]** Dissolving a salt makes the temperature of the water fall from 20 °C to 14 °C. Describe what this shows about the energy change, and name a product that works this way.
- [✔︎] Energy is absorbed from the water (endothermic), so it cools — this is how instant cold packs work
- [ ] Energy is released to the water (exothermic), like a hand warmer
    - *why wrong:* A temperature FALL means energy is absorbed (endothermic); hand warmers get hot and are exothermic.
- [ ] No energy change happens; the salt just mixes in
    - *why wrong:* The 6 °C fall shows energy IS being absorbed from the water — an endothermic change.
- [ ] Energy is absorbed (endothermic), like a self-heating can
    - *why wrong:* Endothermic is right, but self-heating cans get HOT (exothermic); a cold pack is the endothermic example.

**Q12. [reason · TF]** Describe a simple method a student could use to compare how much energy is released by two different liquid fuels.
- [✔︎] Burn each fuel to heat the same volume of water in the same container, and measure the temperature rise — the bigger the rise, the more energy released
- [ ] Weigh each fuel before and after burning; the heavier one releases more energy
    - *why wrong:* Mass lost does not directly measure energy released; you compare the temperature rise of a fixed mass of water.
- [ ] Smell each fuel; the stronger the smell, the more energy released
    - *why wrong:* Smell is not a measure of energy; measure the temperature rise of water heated by each fuel.
- [ ] Time how long each fuel takes to light; the slower one releases more energy
    - *why wrong:* Ignition time does not measure energy released; the temperature rise of heated water does.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** A camping stove burns butane and the surroundings get hotter. Deduce whether the reaction is exothermic or endothermic, and give a reason.
- [✔︎] Exothermic — it releases energy to the surroundings, so their temperature rises
- [ ] Endothermic — energy is taken in, which is what makes the surroundings feel hot
    - *why wrong:* This reverses the idea: endothermic reactions take energy IN and make the surroundings COLDER. Releasing energy (exothermic) is what warms them.
- [ ] Endothermic — burning always absorbs energy from the air
    - *why wrong:* Burning (combustion) RELEASES energy — it is exothermic. It needs a little energy to start, but far more is given out.
- [ ] Neither — the heat comes from the match, not the reaction
    - *why wrong:* The match only supplies the energy to start it; the sustained heat is released by the exothermic combustion itself.

**Q2. [apply · CFCHTFTH]** When ammonium nitrate is stirred into water the beaker feels cold. Predict whether dissolving it is exothermic or endothermic, and explain the temperature change.
- [✔︎] Endothermic — it absorbs energy from the water, so the water's temperature falls
- [ ] Exothermic — the cold shows energy is being released
    - *why wrong:* A temperature FALL means energy is being absorbed FROM the surroundings — that is endothermic, not exothermic.
- [ ] Endothermic — energy is released, cooling the water
    - *why wrong:* Endothermic is the right label, but the reason is wrong: endothermic means energy is ABSORBED, not released.
- [ ] Neither — dissolving is never an energy change
    - *why wrong:* Dissolving does involve energy changes; here energy is absorbed, which is exactly how instant cold packs work.

**Q3. [reason · CFCHTFTH]** Describe what happens to the energy of the surroundings during an exothermic reaction and during an endothermic reaction.
- [✔︎] Exothermic: energy is transferred TO the surroundings (they heat up). Endothermic: energy is taken FROM the surroundings (they cool down)
- [ ] Exothermic: the surroundings cool. Endothermic: the surroundings heat up
    - *why wrong:* This is the wrong way round — exothermic HEATS the surroundings; endothermic COOLS them.
- [ ] Both transfer energy to the surroundings, warming them
    - *why wrong:* Only exothermic warms the surroundings; endothermic absorbs energy and cools them.
- [ ] Both take energy from the surroundings, cooling them
    - *why wrong:* Only endothermic cools the surroundings; exothermic releases energy and warms them.

**Q4. [reason · CFCHTFTH]** Explain why the temperature of the reaction mixture rises during the neutralisation of an acid with an alkali.
- [✔︎] Neutralisation is exothermic — it releases energy to the mixture, so its temperature rises
- [ ] The mixture absorbs energy from the surroundings as it reacts
    - *why wrong:* Absorbing energy would make it COLDER; a temperature rise shows energy is being released (exothermic).
- [ ] The acid and alkali are already hot before they are mixed
    - *why wrong:* The rise is caused by the reaction releasing energy, not by the starting temperature of the reactants.
- [ ] Stirring the mixture adds energy and heats it up
    - *why wrong:* Stirring adds a negligible amount of energy; the heating is due to the exothermic neutralisation reaction.

**Q5. [apply · CFCHTFTH]** A student adds a reactant to a solution and the temperature falls by 6 °C. Determine the type of reaction and state the sign of its enthalpy change, ΔH.
- [✔︎] Endothermic, ΔH is positive — energy was absorbed from the solution, so it cooled
- [ ] Exothermic, ΔH is negative — energy was released, cooling the solution
    - *why wrong:* A temperature FALL means energy was absorbed (endothermic, positive ΔH); releasing energy would warm the solution.
- [ ] Endothermic, ΔH is negative — energy was absorbed
    - *why wrong:* Endothermic is right, but a positive ΔH goes with endothermic; a negative ΔH is exothermic.
- [ ] Exothermic, ΔH is positive — energy was released
    - *why wrong:* Both parts are wrong: a temperature fall is endothermic, and exothermic reactions have a NEGATIVE ΔH.

**Q6. [calc/derivation · CHTH] ⭐** In a calorimetry experiment, 25.0 g of solution rises in temperature by 12.0 °C. Using c = 4.18 J/g °C, calculate the energy released, in kJ.
- [✔︎] 1.254 kJ (Q = 25.0 × 4.18 × 12.0 = 1254 J = 1.254 kJ)
- [ ] 1254 kJ
    - *why wrong:* This is the answer in joules (1254 J) wrongly labelled kJ; convert J→kJ by dividing by 1000, giving 1.254 kJ.
- [ ] 0.1045 kJ
    - *why wrong:* The temperature change was left out (25.0 × 4.18 = 104.5 J only). Q = m × c × ΔT needs the ×12.0 as well.
- [ ] 125.4 kJ
    - *why wrong:* A place-value slip in the J→kJ conversion: 1254 J ÷ 1000 = 1.254 kJ, not 125.4 kJ.
  > 🚩 **Reviewer note:** Calorimetry with a J→kJ conversion. Please full-review.

**Q7. [calc/derivation · CHTH] ⭐** A reaction transfers 2090 J of energy to 100 g of water (c = 4.18 J/g °C). Calculate the temperature rise of the water.
- [✔︎] 5.0 °C (rearrange to ΔT = Q ÷ (m × c) = 2090 ÷ 418)
- [ ] 873 620 °C — multiplied all three values
    - *why wrong:* To find ΔT you must REARRANGE to ΔT = Q ÷ (m × c); multiplying gives a nonsensical value.
- [ ] 20.9 °C — divided Q by the mass only
    - *why wrong:* You must divide by m × c (100 × 4.18 = 418), not by mass alone; 2090 ÷ 418 = 5.0 °C.
- [ ] 0.2 °C — divided (m × c) by Q
    - *why wrong:* The rearrangement is ΔT = Q ÷ (m × c), i.e. 2090 ÷ 418, not 418 ÷ 2090.
  > 🚩 **Reviewer note:** Requires rearrangement of Q = mcΔT. Please full-review.

**Q8. [reason · CHTH]** Two reactions have ΔH = −120 kJ/mol and ΔH = +65 kJ/mol. Compare them in terms of energy transfer and the temperature change you would observe.
- [✔︎] The −120 kJ/mol reaction is exothermic (releases energy, temperature rises); the +65 kJ/mol reaction is endothermic (absorbs energy, temperature falls)
- [ ] The −120 kJ/mol reaction is endothermic because its value is more negative
    - *why wrong:* A negative ΔH is exothermic regardless of size; −120 kJ/mol releases energy and warms the surroundings.
- [ ] Both are exothermic because both involve an energy change
    - *why wrong:* Only the negative ΔH is exothermic; the +65 kJ/mol reaction has a positive ΔH, so it is endothermic.
- [ ] The +65 kJ/mol reaction releases more energy because its number looks larger
    - *why wrong:* A positive ΔH means energy is ABSORBED, not released; the +65 kJ/mol reaction takes energy in (endothermic).

**Q9. [reason · CHTH]** Explain why the energy change measured in a school calorimetry experiment is usually smaller than the true value.
- [✔︎] Some energy is lost to the surroundings and the apparatus (heat escapes), so the measured temperature rise is smaller than it should be
- [ ] The reaction stops before it is finished every time
    - *why wrong:* The main cause is heat loss to the surroundings, not the reaction stopping early.
- [ ] The thermometer adds energy to the solution
    - *why wrong:* A thermometer does not add a significant amount of energy; the loss is heat escaping to the surroundings and apparatus.
- [ ] The specific heat capacity increases during the reaction
    - *why wrong:* c is taken as constant (4.18 J/g °C for water); the shortfall is due to heat loss, not a change in c.

**Q10. [calc/derivation · CHTH] ⭐** Burning 0.010 mol of a fuel releases 6.7 kJ of energy. Calculate the molar enthalpy change, in kJ/mol, and state its sign.
- [✔︎] −670 kJ/mol (6.7 ÷ 0.010 = 670; negative because combustion releases energy)
- [ ] +670 kJ/mol
    - *why wrong:* The magnitude is right (6.7 ÷ 0.010 = 670) but combustion RELEASES energy, so ΔH is negative, not positive.
- [ ] −0.067 kJ/mol — multiplied instead of divided
    - *why wrong:* Energy per mole is energy ÷ moles (6.7 ÷ 0.010 = 670), not energy × moles.
- [ ] −6.7 kJ/mol — did not divide by the number of moles
    - *why wrong:* The 6.7 kJ is for 0.010 mol; dividing by 0.010 scales it up to 670 kJ per mole.
  > 🚩 **Reviewer note:** Energy-per-mole with a sign judgement. Please full-review.

**Q11. [calc/derivation · TH] ⭐** Burning 1.5 g of a fuel raises the temperature of 200 g of water by 25 °C (c = 4.18 J/g °C). Calculate the energy released, in kJ.
- [✔︎] 20.9 kJ (Q = 200 × 4.18 × 25 = 20 900 J = 20.9 kJ)
- [ ] 20 900 kJ — did not convert joules to kilojoules
    - *why wrong:* 200 × 4.18 × 25 = 20 900 J; dividing by 1000 gives 20.9 kJ.
- [ ] 0.157 kJ — used the fuel mass (1.5 g) instead of the water mass
    - *why wrong:* In Q = mcΔT, m is the mass of WATER being heated (200 g), not the mass of fuel burned.
- [ ] 0.836 kJ — left out the temperature change (×25)
    - *why wrong:* Q = m × c × ΔT needs all three: 200 × 4.18 × 25 = 20 900 J = 20.9 kJ.
  > 🚩 **Reviewer note:** Calorimetry using the correct mass (water, not fuel) and J→kJ. Please full-review.

**Q12. [reason · TH]** A student claims that because a reaction has a very negative ΔH it must happen quickly. Evaluate this claim.
- [✔︎] The claim is wrong — ΔH tells you how much energy is released (how exothermic), not how fast; rate depends on the activation energy and conditions, not on ΔH
- [ ] The claim is correct — a more negative ΔH always means a faster reaction
    - *why wrong:* ΔH is about energy released, not speed; a very exothermic reaction can still be slow (for example, rusting).
- [ ] The claim is correct because releasing more energy pushes the reaction along faster
    - *why wrong:* The energy released (ΔH) does not set the rate; the activation energy and the conditions do.
- [ ] The claim is wrong because a negative ΔH means the reaction is endothermic and slow
    - *why wrong:* A negative ΔH is exothermic, not endothermic; and the real point is that ΔH does not determine rate at all.

**FIFA worked examples ⭐ (full review):**

#### Foundation (Combined-Foundation & Triple-Foundation) FIFA
- **Energy released heating water** — A reaction heats 50 g of water. The temperature rises from 20 °C to 30 °C. Calculate the energy transferred. (c = 4.18 J/g °C)
    - **F** — Q = m × c × ΔT
    - **I** — m = 50 g, c = 4.18 J/g °C, ΔT = 30 − 20 = 10 °C
    - **F** — Q = 50 × 4.18 × 10
    - **A** — Q = 2090 J (exothermic — the temperature rose)
- **A larger mass of water** — A reaction heats 100 g of water from 18 °C to 28 °C. Calculate the energy transferred. (c = 4.18 J/g °C)
    - **F** — Q = m × c × ΔT
    - **I** — m = 100 g, c = 4.18 J/g °C, ΔT = 28 − 18 = 10 °C
    - **F** — Q = 100 × 4.18 × 10
    - **A** — Q = 4180 J
- **An endothermic change (temperature falls)** — Dissolving a salt cools 40 g of water from 25 °C to 19 °C. Calculate the energy absorbed. (c = 4.18 J/g °C)
    - **F** — Q = m × c × ΔT
    - **I** — m = 40 g, c = 4.18 J/g °C, ΔT = 25 − 19 = 6 °C
    - **F** — Q = 40 × 4.18 × 6
    - **A** — Q = 1003.2 J (endothermic — the temperature fell)

#### Higher (Combined-Higher & Triple-Higher) FIFA
- **Energy released, in kilojoules** — A reaction raises the temperature of 150 g of water by 20 °C. Calculate the energy released, in kJ. (c = 4.18 J/g °C)
    - **F** — Q = m × c × ΔT
    - **I** — m = 150 g, c = 4.18 J/g °C, ΔT = 20 °C, so Q = 150 × 4.18 × 20
    - **F** — Q = 12 540 J; convert to kJ by dividing by 1000
    - **A** — Q = 12.54 kJ
- **Molar enthalpy of combustion** — Burning 0.020 mol of a liquid fuel raises the temperature of 200 g of water by 43 °C. Calculate the molar enthalpy change, in kJ/mol. (c = 4.18 J/g °C)
    - **F** — Q = m × c × ΔT, then ΔH = Q ÷ number of moles
    - **I** — Q = 200 × 4.18 × 43 = 35 948 J = 35.948 kJ
    - **F** — ΔH = 35.948 ÷ 0.020, and it is negative because combustion is exothermic
    - **A** — ΔH = −1797 kJ/mol (to 4 significant figures)
- **Working backwards to a temperature rise** — A reaction releases 6270 J of energy to 100 g of water. Calculate the temperature rise of the water. (c = 4.18 J/g °C)
    - **F** — Q = m × c × ΔT, rearranged to ΔT = Q ÷ (m × c)
    - **I** — ΔT = 6270 ÷ (100 × 4.18) = 6270 ÷ 418
    - **F** — divide
    - **A** — ΔT = 15 °C


---

## Reaction Profiles  ·  `reaction-profiles`  ·  AQA 5.5.1.2

> 🚩 **Triple-depth call (your review):** MATCHED — AQA 5.5.1.2 (reaction profiles, activation energy) is identical for Combined and Triple and taught at both tiers. Foundation reads ΔH and Ea off a given profile by a single subtraction; Higher adds forward/reverse activation energy, sign interpretation and working backwards. Triple sets = Combined + extra same-tier coverage.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often confuse the activation energy with the overall energy change on a reaction profile, and read both from the same two points. They are different measurements: the activation energy (Ea) is the climb from the REACTANT level up to the PEAK of the curve, while the overall energy change (ΔH) is the step from the REACTANT level across to the PRODUCT level. A second common slip is to think a downhill profile (products lower than reactants) is endothermic — it is the opposite: products lower means energy was released, so the reaction is exothermic.

**Question sets by tier** (each item shows tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (4 recall / 6 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** On a reaction profile the products are drawn LOWER than the reactants. Deduce whether the reaction is exothermic or endothermic, and give the sign of ΔH.
- [✔︎] Exothermic, ΔH is negative — energy is released, so the products end up at a lower energy than the reactants
- [ ] Endothermic, ΔH is positive — the products are lower because they absorbed energy
    - *why wrong:* Products LOWER than reactants means energy was released (exothermic, ΔH negative); absorbing energy would raise the products.
- [ ] Exothermic, ΔH is positive — energy is released
    - *why wrong:* Exothermic is right, but exothermic reactions have a NEGATIVE ΔH, not positive.
- [ ] It cannot be decided without knowing the activation energy
    - *why wrong:* The relative heights of reactants and products alone show the reaction is exothermic; the activation energy is a separate feature.

**Q2. [apply · CFCHTFTH]** On a reaction profile the products are drawn HIGHER than the reactants. Deduce whether the reaction is exothermic or endothermic, and explain how the diagram shows this.
- [✔︎] Endothermic — the products are at a higher energy than the reactants, so energy was absorbed from the surroundings
- [ ] Exothermic — the products are higher because energy was released
    - *why wrong:* Releasing energy LOWERS the products; products higher than reactants means energy was absorbed (endothermic).
- [ ] Endothermic — because the activation energy is very large
    - *why wrong:* A large activation energy does not make a reaction endothermic; it is the products being HIGHER than the reactants that shows it.
- [ ] Neither — the heights of the lines do not matter
    - *why wrong:* The relative heights are exactly what the profile shows: products higher than reactants means endothermic.

**Q3. [reason · CFCHTFTH]** Describe what the activation energy represents on a reaction profile.
- [✔︎] The minimum energy the reactants must gain to react — shown as the climb from the reactant level up to the peak of the curve
- [ ] The energy difference between the reactants and the products
    - *why wrong:* That is the overall energy change (ΔH); the activation energy is the climb up to the PEAK, not the reactant-to-product step.
- [ ] The energy released when the products form
    - *why wrong:* Energy released relates to ΔH for an exothermic reaction; the activation energy is the barrier that must be climbed to start the reaction.
- [ ] The total energy stored in the reactants
    - *why wrong:* The activation energy is not the reactants' total energy; it is the extra energy needed to reach the peak so the reaction can proceed.

**Q4. [reason · CFCHTFTH]** Explain why every reaction, even an exothermic one, needs a minimum amount of energy to get started.
- [✔︎] Existing bonds in the reactants must be broken before new ones can form, and breaking bonds needs energy — this is the activation energy
- [ ] Because all reactions absorb energy overall
    - *why wrong:* Not all reactions absorb energy overall (exothermic ones release it); the start-up energy is the activation energy needed to break bonds.
- [ ] Because the products always have more energy than the reactants
    - *why wrong:* In an exothermic reaction the products have LESS energy; the start-up energy is still needed to break the reactant bonds first.
- [ ] Because energy can be created only at the start of a reaction
    - *why wrong:* Energy is conserved (neither created nor destroyed); the reason a reaction needs a push is the activation energy to break bonds.

**Q5. [apply · CFCHTFTH]** A catalyst is added to a reaction. Describe its effect on the reaction profile and explain how this speeds up the reaction.
- [✔︎] It provides a different pathway with a lower activation energy (a lower peak), so more colliding particles have enough energy to react
- [ ] It lowers the energy of the products, making ΔH more negative
    - *why wrong:* A catalyst does not change ΔH (the reactant and product levels are unchanged); it lowers the activation-energy peak.
- [ ] It raises the activation energy so the reaction releases more energy
    - *why wrong:* A catalyst LOWERS the activation energy, and it does not change how much energy is released (ΔH).
- [ ] It removes the activation energy completely
    - *why wrong:* A catalyst lowers the activation energy but does not remove it; some energy is still needed to react.

**Q6. [recall · CFTF]** State what the vertical (y) axis represents on a reaction profile.
- [✔︎] Energy
- [ ] Time
    - *why wrong:* Time is not shown on a reaction profile; the vertical axis is energy and the horizontal axis is the progress of the reaction.
- [ ] Temperature
    - *why wrong:* The vertical axis is energy, not temperature; profiles compare the energy of reactants and products.
- [ ] Mass
    - *why wrong:* Mass is not plotted on a reaction profile; the vertical axis shows energy.

**Q7. [recall · CFTF]** State where the activation energy is measured from and to on a reaction profile.
- [✔︎] From the reactant level up to the peak (top) of the curve
- [ ] From the reactant level across to the product level
    - *why wrong:* That is the overall energy change (ΔH); the activation energy is measured up to the PEAK.
- [ ] From the peak down to the product level
    - *why wrong:* That distance is the energy released as products form, not the activation energy, which is measured UP to the peak from the reactants.
- [ ] From the bottom of the axis up to the product level
    - *why wrong:* Activation energy is measured from the reactants to the peak, not from the axis origin.

**Q8. [recall · CFTF]** State the name given to the overall energy difference between the reactants and the products.
- [✔︎] The enthalpy change, ΔH
- [ ] The activation energy
    - *why wrong:* The activation energy is the barrier up to the peak; the reactant-to-product difference is the enthalpy change, ΔH.
- [ ] The specific heat capacity
    - *why wrong:* Specific heat capacity is a property of a substance used in calorimetry, not the reactant-to-product energy difference.
- [ ] The rate of reaction
    - *why wrong:* Rate is how fast a reaction goes; the energy difference between reactants and products is ΔH.

**Q9. [recall · CFTF]** State what happens to the height of the activation-energy peak when a catalyst is used.
- [✔︎] It becomes lower
- [ ] It becomes higher
    - *why wrong:* A catalyst LOWERS the activation-energy peak, providing an easier pathway.
- [ ] It stays exactly the same
    - *why wrong:* The whole point of a catalyst is to LOWER the activation-energy peak.
- [ ] It disappears completely
    - *why wrong:* A catalyst lowers the peak but does not remove it; some activation energy is still needed.

**Q10. [apply · CFTF]** On a reaction profile the reactants are at 200 kJ and the products are at 150 kJ. Calculate the overall energy change and state whether the reaction is exothermic or endothermic.
- [✔︎] ΔH = 150 − 200 = −50 kJ; exothermic (the products are lower)
- [ ] ΔH = 200 − 150 = +50 kJ; endothermic
    - *why wrong:* ΔH = energy of products − energy of reactants = 150 − 200 = −50 kJ; products lower means exothermic.
- [ ] ΔH = 200 + 150 = 350 kJ; exothermic
    - *why wrong:* ΔH is the DIFFERENCE (products − reactants), not the sum of the two levels.
- [ ] ΔH = −50 kJ; endothermic
    - *why wrong:* The value is right, but a negative ΔH (products lower) is exothermic, not endothermic.

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** On a reaction profile the products are drawn LOWER than the reactants. Deduce whether the reaction is exothermic or endothermic, and give the sign of ΔH.
- [✔︎] Exothermic, ΔH is negative — energy is released, so the products end up at a lower energy than the reactants
- [ ] Endothermic, ΔH is positive — the products are lower because they absorbed energy
    - *why wrong:* Products LOWER than reactants means energy was released (exothermic, ΔH negative); absorbing energy would raise the products.
- [ ] Exothermic, ΔH is positive — energy is released
    - *why wrong:* Exothermic is right, but exothermic reactions have a NEGATIVE ΔH, not positive.
- [ ] It cannot be decided without knowing the activation energy
    - *why wrong:* The relative heights of reactants and products alone show the reaction is exothermic; the activation energy is a separate feature.

**Q2. [apply · CFCHTFTH]** On a reaction profile the products are drawn HIGHER than the reactants. Deduce whether the reaction is exothermic or endothermic, and explain how the diagram shows this.
- [✔︎] Endothermic — the products are at a higher energy than the reactants, so energy was absorbed from the surroundings
- [ ] Exothermic — the products are higher because energy was released
    - *why wrong:* Releasing energy LOWERS the products; products higher than reactants means energy was absorbed (endothermic).
- [ ] Endothermic — because the activation energy is very large
    - *why wrong:* A large activation energy does not make a reaction endothermic; it is the products being HIGHER than the reactants that shows it.
- [ ] Neither — the heights of the lines do not matter
    - *why wrong:* The relative heights are exactly what the profile shows: products higher than reactants means endothermic.

**Q3. [reason · CFCHTFTH]** Describe what the activation energy represents on a reaction profile.
- [✔︎] The minimum energy the reactants must gain to react — shown as the climb from the reactant level up to the peak of the curve
- [ ] The energy difference between the reactants and the products
    - *why wrong:* That is the overall energy change (ΔH); the activation energy is the climb up to the PEAK, not the reactant-to-product step.
- [ ] The energy released when the products form
    - *why wrong:* Energy released relates to ΔH for an exothermic reaction; the activation energy is the barrier that must be climbed to start the reaction.
- [ ] The total energy stored in the reactants
    - *why wrong:* The activation energy is not the reactants' total energy; it is the extra energy needed to reach the peak so the reaction can proceed.

**Q4. [reason · CFCHTFTH]** Explain why every reaction, even an exothermic one, needs a minimum amount of energy to get started.
- [✔︎] Existing bonds in the reactants must be broken before new ones can form, and breaking bonds needs energy — this is the activation energy
- [ ] Because all reactions absorb energy overall
    - *why wrong:* Not all reactions absorb energy overall (exothermic ones release it); the start-up energy is the activation energy needed to break bonds.
- [ ] Because the products always have more energy than the reactants
    - *why wrong:* In an exothermic reaction the products have LESS energy; the start-up energy is still needed to break the reactant bonds first.
- [ ] Because energy can be created only at the start of a reaction
    - *why wrong:* Energy is conserved (neither created nor destroyed); the reason a reaction needs a push is the activation energy to break bonds.

**Q5. [apply · CFCHTFTH]** A catalyst is added to a reaction. Describe its effect on the reaction profile and explain how this speeds up the reaction.
- [✔︎] It provides a different pathway with a lower activation energy (a lower peak), so more colliding particles have enough energy to react
- [ ] It lowers the energy of the products, making ΔH more negative
    - *why wrong:* A catalyst does not change ΔH (the reactant and product levels are unchanged); it lowers the activation-energy peak.
- [ ] It raises the activation energy so the reaction releases more energy
    - *why wrong:* A catalyst LOWERS the activation energy, and it does not change how much energy is released (ΔH).
- [ ] It removes the activation energy completely
    - *why wrong:* A catalyst lowers the activation energy but does not remove it; some energy is still needed to react.

**Q6. [calc/derivation · CHTH] ⭐** On a reaction profile the reactants are at 350 kJ, the peak is at 500 kJ and the products are at 220 kJ. Calculate the activation energy and the overall energy change, ΔH.
- [✔︎] Ea = 500 − 350 = 150 kJ; ΔH = 220 − 350 = −130 kJ (exothermic)
- [ ] Ea = 500 − 220 = 280 kJ; ΔH = −130 kJ
    - *why wrong:* Activation energy is measured from the REACTANTS (350), not the products: Ea = 500 − 350 = 150 kJ.
- [ ] Ea = 150 kJ; ΔH = 350 − 220 = +130 kJ
    - *why wrong:* ΔH = products − reactants = 220 − 350 = −130 kJ; doing reactants − products gives the wrong sign.
- [ ] Ea = 500 kJ; ΔH = 220 kJ
    - *why wrong:* Both are differences: Ea = peak − reactants = 150 kJ and ΔH = products − reactants = −130 kJ, not the raw peak and product values.
  > 🚩 **Reviewer note:** Reads Ea and ΔH off a profile. Please full-review.

**Q7. [calc/derivation · CHTH] ⭐** For the same profile (reactants 350 kJ, peak 500 kJ, products 220 kJ), calculate the activation energy of the reverse reaction (products → reactants).
- [✔︎] 280 kJ (Ea reverse = peak − product level = 500 − 220)
- [ ] 150 kJ — the same as the forward reaction
    - *why wrong:* The reverse reaction starts from the PRODUCTS (220), so its barrier is 500 − 220 = 280 kJ, larger than the forward 150 kJ.
- [ ] 130 kJ — the size of ΔH
    - *why wrong:* That is the overall energy change, not the reverse activation energy; the reverse Ea is peak − products = 280 kJ.
- [ ] 720 kJ — added the peak and the products
    - *why wrong:* The reverse activation energy is the DIFFERENCE peak − products = 500 − 220 = 280 kJ, not their sum.
  > 🚩 **Reviewer note:** Reverse activation energy from a profile. Please full-review.

**Q8. [reason · CHTH]** Explain why a catalyst changes the activation energy of a reaction but does not change the value of ΔH.
- [✔︎] A catalyst provides an alternative pathway with a lower peak (lower Ea), but the reactant and product energy levels are unchanged, so their difference (ΔH) stays the same
- [ ] A catalyst lowers the product level, so both Ea and ΔH decrease
    - *why wrong:* A catalyst does not move the product level; it only lowers the peak, so ΔH is unchanged.
- [ ] A catalyst is used up, releasing energy that changes ΔH
    - *why wrong:* A catalyst is not used up and does not change the energy of the reactants or products, so ΔH is unchanged.
- [ ] A catalyst raises the reactant level up towards the peak
    - *why wrong:* A catalyst does not raise the reactants; it lowers the activation-energy barrier by offering a new pathway.

**Q9. [reason · CHTH]** A reaction has a small activation energy but a large positive ΔH. Deduce what this tells you about how easily it starts and its overall energy change.
- [✔︎] It starts easily (a low barrier to overcome) but is strongly endothermic overall (the products are much higher in energy than the reactants)
- [ ] It is hard to start and exothermic overall
    - *why wrong:* A SMALL activation energy means it starts easily, and a POSITIVE ΔH is endothermic, not exothermic.
- [ ] It starts easily and is exothermic overall
    - *why wrong:* A positive ΔH is endothermic (energy absorbed), not exothermic.
- [ ] The two quantities are the same thing measured twice
    - *why wrong:* Activation energy (the barrier) and ΔH (the overall change) are different features of the profile, measured between different points.

**Q10. [reason · CHTH]** Describe how the reaction profile of an endothermic reaction differs from that of an exothermic reaction.
- [✔︎] In an endothermic profile the products are HIGHER than the reactants (ΔH positive); in an exothermic profile the products are LOWER than the reactants (ΔH negative)
- [ ] Both have products lower than the reactants, but the endothermic one has a bigger peak
    - *why wrong:* An endothermic reaction has products HIGHER than the reactants; peak height (the activation energy) is a separate feature.
- [ ] The endothermic profile has no activation-energy peak
    - *why wrong:* Both types have an activation-energy peak; the difference is the product level relative to the reactants.
- [ ] The exothermic profile has products higher than the reactants
    - *why wrong:* That is the endothermic case; exothermic profiles have products LOWER than the reactants.

### Triple Foundation — 12 questions (4 recall / 8 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** On a reaction profile the products are drawn LOWER than the reactants. Deduce whether the reaction is exothermic or endothermic, and give the sign of ΔH.
- [✔︎] Exothermic, ΔH is negative — energy is released, so the products end up at a lower energy than the reactants
- [ ] Endothermic, ΔH is positive — the products are lower because they absorbed energy
    - *why wrong:* Products LOWER than reactants means energy was released (exothermic, ΔH negative); absorbing energy would raise the products.
- [ ] Exothermic, ΔH is positive — energy is released
    - *why wrong:* Exothermic is right, but exothermic reactions have a NEGATIVE ΔH, not positive.
- [ ] It cannot be decided without knowing the activation energy
    - *why wrong:* The relative heights of reactants and products alone show the reaction is exothermic; the activation energy is a separate feature.

**Q2. [apply · CFCHTFTH]** On a reaction profile the products are drawn HIGHER than the reactants. Deduce whether the reaction is exothermic or endothermic, and explain how the diagram shows this.
- [✔︎] Endothermic — the products are at a higher energy than the reactants, so energy was absorbed from the surroundings
- [ ] Exothermic — the products are higher because energy was released
    - *why wrong:* Releasing energy LOWERS the products; products higher than reactants means energy was absorbed (endothermic).
- [ ] Endothermic — because the activation energy is very large
    - *why wrong:* A large activation energy does not make a reaction endothermic; it is the products being HIGHER than the reactants that shows it.
- [ ] Neither — the heights of the lines do not matter
    - *why wrong:* The relative heights are exactly what the profile shows: products higher than reactants means endothermic.

**Q3. [reason · CFCHTFTH]** Describe what the activation energy represents on a reaction profile.
- [✔︎] The minimum energy the reactants must gain to react — shown as the climb from the reactant level up to the peak of the curve
- [ ] The energy difference between the reactants and the products
    - *why wrong:* That is the overall energy change (ΔH); the activation energy is the climb up to the PEAK, not the reactant-to-product step.
- [ ] The energy released when the products form
    - *why wrong:* Energy released relates to ΔH for an exothermic reaction; the activation energy is the barrier that must be climbed to start the reaction.
- [ ] The total energy stored in the reactants
    - *why wrong:* The activation energy is not the reactants' total energy; it is the extra energy needed to reach the peak so the reaction can proceed.

**Q4. [reason · CFCHTFTH]** Explain why every reaction, even an exothermic one, needs a minimum amount of energy to get started.
- [✔︎] Existing bonds in the reactants must be broken before new ones can form, and breaking bonds needs energy — this is the activation energy
- [ ] Because all reactions absorb energy overall
    - *why wrong:* Not all reactions absorb energy overall (exothermic ones release it); the start-up energy is the activation energy needed to break bonds.
- [ ] Because the products always have more energy than the reactants
    - *why wrong:* In an exothermic reaction the products have LESS energy; the start-up energy is still needed to break the reactant bonds first.
- [ ] Because energy can be created only at the start of a reaction
    - *why wrong:* Energy is conserved (neither created nor destroyed); the reason a reaction needs a push is the activation energy to break bonds.

**Q5. [apply · CFCHTFTH]** A catalyst is added to a reaction. Describe its effect on the reaction profile and explain how this speeds up the reaction.
- [✔︎] It provides a different pathway with a lower activation energy (a lower peak), so more colliding particles have enough energy to react
- [ ] It lowers the energy of the products, making ΔH more negative
    - *why wrong:* A catalyst does not change ΔH (the reactant and product levels are unchanged); it lowers the activation-energy peak.
- [ ] It raises the activation energy so the reaction releases more energy
    - *why wrong:* A catalyst LOWERS the activation energy, and it does not change how much energy is released (ΔH).
- [ ] It removes the activation energy completely
    - *why wrong:* A catalyst lowers the activation energy but does not remove it; some energy is still needed to react.

**Q6. [recall · CFTF]** State what the vertical (y) axis represents on a reaction profile.
- [✔︎] Energy
- [ ] Time
    - *why wrong:* Time is not shown on a reaction profile; the vertical axis is energy and the horizontal axis is the progress of the reaction.
- [ ] Temperature
    - *why wrong:* The vertical axis is energy, not temperature; profiles compare the energy of reactants and products.
- [ ] Mass
    - *why wrong:* Mass is not plotted on a reaction profile; the vertical axis shows energy.

**Q7. [recall · CFTF]** State where the activation energy is measured from and to on a reaction profile.
- [✔︎] From the reactant level up to the peak (top) of the curve
- [ ] From the reactant level across to the product level
    - *why wrong:* That is the overall energy change (ΔH); the activation energy is measured up to the PEAK.
- [ ] From the peak down to the product level
    - *why wrong:* That distance is the energy released as products form, not the activation energy, which is measured UP to the peak from the reactants.
- [ ] From the bottom of the axis up to the product level
    - *why wrong:* Activation energy is measured from the reactants to the peak, not from the axis origin.

**Q8. [recall · CFTF]** State the name given to the overall energy difference between the reactants and the products.
- [✔︎] The enthalpy change, ΔH
- [ ] The activation energy
    - *why wrong:* The activation energy is the barrier up to the peak; the reactant-to-product difference is the enthalpy change, ΔH.
- [ ] The specific heat capacity
    - *why wrong:* Specific heat capacity is a property of a substance used in calorimetry, not the reactant-to-product energy difference.
- [ ] The rate of reaction
    - *why wrong:* Rate is how fast a reaction goes; the energy difference between reactants and products is ΔH.

**Q9. [recall · CFTF]** State what happens to the height of the activation-energy peak when a catalyst is used.
- [✔︎] It becomes lower
- [ ] It becomes higher
    - *why wrong:* A catalyst LOWERS the activation-energy peak, providing an easier pathway.
- [ ] It stays exactly the same
    - *why wrong:* The whole point of a catalyst is to LOWER the activation-energy peak.
- [ ] It disappears completely
    - *why wrong:* A catalyst lowers the peak but does not remove it; some activation energy is still needed.

**Q10. [apply · CFTF]** On a reaction profile the reactants are at 200 kJ and the products are at 150 kJ. Calculate the overall energy change and state whether the reaction is exothermic or endothermic.
- [✔︎] ΔH = 150 − 200 = −50 kJ; exothermic (the products are lower)
- [ ] ΔH = 200 − 150 = +50 kJ; endothermic
    - *why wrong:* ΔH = energy of products − energy of reactants = 150 − 200 = −50 kJ; products lower means exothermic.
- [ ] ΔH = 200 + 150 = 350 kJ; exothermic
    - *why wrong:* ΔH is the DIFFERENCE (products − reactants), not the sum of the two levels.
- [ ] ΔH = −50 kJ; endothermic
    - *why wrong:* The value is right, but a negative ΔH (products lower) is exothermic, not endothermic.

**Q11. [apply · TF]** A reaction profile shows reactants at 120 kJ and products at 180 kJ. Determine the overall energy change and state whether energy is absorbed or released.
- [✔︎] ΔH = 180 − 120 = +60 kJ; energy is absorbed (endothermic)
- [ ] ΔH = 120 − 180 = −60 kJ; energy is released
    - *why wrong:* ΔH = products − reactants = 180 − 120 = +60 kJ; products higher means energy absorbed.
- [ ] ΔH = +60 kJ; energy is released
    - *why wrong:* The value is right, but a positive ΔH (products higher) means energy is ABSORBED, not released.
- [ ] ΔH = 300 kJ; energy is absorbed
    - *why wrong:* ΔH is the difference (180 − 120 = 60 kJ), not the sum of the two levels.

**Q12. [reason · TF]** Describe what a catalyst does to the activation energy and give one everyday benefit of using one.
- [✔︎] It lowers the activation energy (an easier pathway), which lets the reaction go faster or work at a lower temperature — saving energy in industry
- [ ] It raises the activation energy, so the reaction gives out more heat
    - *why wrong:* A catalyst LOWERS the activation energy, and it does not change how much heat is released.
- [ ] It increases ΔH so that more product is made
    - *why wrong:* A catalyst does not change ΔH or the amount of product; it lowers the activation energy to speed things up.
- [ ] It is used up, so more must be added each time
    - *why wrong:* A catalyst is not used up in the reaction; it can be used over and over again.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** On a reaction profile the products are drawn LOWER than the reactants. Deduce whether the reaction is exothermic or endothermic, and give the sign of ΔH.
- [✔︎] Exothermic, ΔH is negative — energy is released, so the products end up at a lower energy than the reactants
- [ ] Endothermic, ΔH is positive — the products are lower because they absorbed energy
    - *why wrong:* Products LOWER than reactants means energy was released (exothermic, ΔH negative); absorbing energy would raise the products.
- [ ] Exothermic, ΔH is positive — energy is released
    - *why wrong:* Exothermic is right, but exothermic reactions have a NEGATIVE ΔH, not positive.
- [ ] It cannot be decided without knowing the activation energy
    - *why wrong:* The relative heights of reactants and products alone show the reaction is exothermic; the activation energy is a separate feature.

**Q2. [apply · CFCHTFTH]** On a reaction profile the products are drawn HIGHER than the reactants. Deduce whether the reaction is exothermic or endothermic, and explain how the diagram shows this.
- [✔︎] Endothermic — the products are at a higher energy than the reactants, so energy was absorbed from the surroundings
- [ ] Exothermic — the products are higher because energy was released
    - *why wrong:* Releasing energy LOWERS the products; products higher than reactants means energy was absorbed (endothermic).
- [ ] Endothermic — because the activation energy is very large
    - *why wrong:* A large activation energy does not make a reaction endothermic; it is the products being HIGHER than the reactants that shows it.
- [ ] Neither — the heights of the lines do not matter
    - *why wrong:* The relative heights are exactly what the profile shows: products higher than reactants means endothermic.

**Q3. [reason · CFCHTFTH]** Describe what the activation energy represents on a reaction profile.
- [✔︎] The minimum energy the reactants must gain to react — shown as the climb from the reactant level up to the peak of the curve
- [ ] The energy difference between the reactants and the products
    - *why wrong:* That is the overall energy change (ΔH); the activation energy is the climb up to the PEAK, not the reactant-to-product step.
- [ ] The energy released when the products form
    - *why wrong:* Energy released relates to ΔH for an exothermic reaction; the activation energy is the barrier that must be climbed to start the reaction.
- [ ] The total energy stored in the reactants
    - *why wrong:* The activation energy is not the reactants' total energy; it is the extra energy needed to reach the peak so the reaction can proceed.

**Q4. [reason · CFCHTFTH]** Explain why every reaction, even an exothermic one, needs a minimum amount of energy to get started.
- [✔︎] Existing bonds in the reactants must be broken before new ones can form, and breaking bonds needs energy — this is the activation energy
- [ ] Because all reactions absorb energy overall
    - *why wrong:* Not all reactions absorb energy overall (exothermic ones release it); the start-up energy is the activation energy needed to break bonds.
- [ ] Because the products always have more energy than the reactants
    - *why wrong:* In an exothermic reaction the products have LESS energy; the start-up energy is still needed to break the reactant bonds first.
- [ ] Because energy can be created only at the start of a reaction
    - *why wrong:* Energy is conserved (neither created nor destroyed); the reason a reaction needs a push is the activation energy to break bonds.

**Q5. [apply · CFCHTFTH]** A catalyst is added to a reaction. Describe its effect on the reaction profile and explain how this speeds up the reaction.
- [✔︎] It provides a different pathway with a lower activation energy (a lower peak), so more colliding particles have enough energy to react
- [ ] It lowers the energy of the products, making ΔH more negative
    - *why wrong:* A catalyst does not change ΔH (the reactant and product levels are unchanged); it lowers the activation-energy peak.
- [ ] It raises the activation energy so the reaction releases more energy
    - *why wrong:* A catalyst LOWERS the activation energy, and it does not change how much energy is released (ΔH).
- [ ] It removes the activation energy completely
    - *why wrong:* A catalyst lowers the activation energy but does not remove it; some energy is still needed to react.

**Q6. [calc/derivation · CHTH] ⭐** On a reaction profile the reactants are at 350 kJ, the peak is at 500 kJ and the products are at 220 kJ. Calculate the activation energy and the overall energy change, ΔH.
- [✔︎] Ea = 500 − 350 = 150 kJ; ΔH = 220 − 350 = −130 kJ (exothermic)
- [ ] Ea = 500 − 220 = 280 kJ; ΔH = −130 kJ
    - *why wrong:* Activation energy is measured from the REACTANTS (350), not the products: Ea = 500 − 350 = 150 kJ.
- [ ] Ea = 150 kJ; ΔH = 350 − 220 = +130 kJ
    - *why wrong:* ΔH = products − reactants = 220 − 350 = −130 kJ; doing reactants − products gives the wrong sign.
- [ ] Ea = 500 kJ; ΔH = 220 kJ
    - *why wrong:* Both are differences: Ea = peak − reactants = 150 kJ and ΔH = products − reactants = −130 kJ, not the raw peak and product values.
  > 🚩 **Reviewer note:** Reads Ea and ΔH off a profile. Please full-review.

**Q7. [calc/derivation · CHTH] ⭐** For the same profile (reactants 350 kJ, peak 500 kJ, products 220 kJ), calculate the activation energy of the reverse reaction (products → reactants).
- [✔︎] 280 kJ (Ea reverse = peak − product level = 500 − 220)
- [ ] 150 kJ — the same as the forward reaction
    - *why wrong:* The reverse reaction starts from the PRODUCTS (220), so its barrier is 500 − 220 = 280 kJ, larger than the forward 150 kJ.
- [ ] 130 kJ — the size of ΔH
    - *why wrong:* That is the overall energy change, not the reverse activation energy; the reverse Ea is peak − products = 280 kJ.
- [ ] 720 kJ — added the peak and the products
    - *why wrong:* The reverse activation energy is the DIFFERENCE peak − products = 500 − 220 = 280 kJ, not their sum.
  > 🚩 **Reviewer note:** Reverse activation energy from a profile. Please full-review.

**Q8. [reason · CHTH]** Explain why a catalyst changes the activation energy of a reaction but does not change the value of ΔH.
- [✔︎] A catalyst provides an alternative pathway with a lower peak (lower Ea), but the reactant and product energy levels are unchanged, so their difference (ΔH) stays the same
- [ ] A catalyst lowers the product level, so both Ea and ΔH decrease
    - *why wrong:* A catalyst does not move the product level; it only lowers the peak, so ΔH is unchanged.
- [ ] A catalyst is used up, releasing energy that changes ΔH
    - *why wrong:* A catalyst is not used up and does not change the energy of the reactants or products, so ΔH is unchanged.
- [ ] A catalyst raises the reactant level up towards the peak
    - *why wrong:* A catalyst does not raise the reactants; it lowers the activation-energy barrier by offering a new pathway.

**Q9. [reason · CHTH]** A reaction has a small activation energy but a large positive ΔH. Deduce what this tells you about how easily it starts and its overall energy change.
- [✔︎] It starts easily (a low barrier to overcome) but is strongly endothermic overall (the products are much higher in energy than the reactants)
- [ ] It is hard to start and exothermic overall
    - *why wrong:* A SMALL activation energy means it starts easily, and a POSITIVE ΔH is endothermic, not exothermic.
- [ ] It starts easily and is exothermic overall
    - *why wrong:* A positive ΔH is endothermic (energy absorbed), not exothermic.
- [ ] The two quantities are the same thing measured twice
    - *why wrong:* Activation energy (the barrier) and ΔH (the overall change) are different features of the profile, measured between different points.

**Q10. [reason · CHTH]** Describe how the reaction profile of an endothermic reaction differs from that of an exothermic reaction.
- [✔︎] In an endothermic profile the products are HIGHER than the reactants (ΔH positive); in an exothermic profile the products are LOWER than the reactants (ΔH negative)
- [ ] Both have products lower than the reactants, but the endothermic one has a bigger peak
    - *why wrong:* An endothermic reaction has products HIGHER than the reactants; peak height (the activation energy) is a separate feature.
- [ ] The endothermic profile has no activation-energy peak
    - *why wrong:* Both types have an activation-energy peak; the difference is the product level relative to the reactants.
- [ ] The exothermic profile has products higher than the reactants
    - *why wrong:* That is the endothermic case; exothermic profiles have products LOWER than the reactants.

**Q11. [calc/derivation · TH] ⭐** A reaction profile shows reactants at 80 kJ, a peak at 340 kJ and products at 300 kJ. Calculate the forward activation energy, the reverse activation energy, and ΔH.
- [✔︎] Ea forward = 340 − 80 = 260 kJ; Ea reverse = 340 − 300 = 40 kJ; ΔH = 300 − 80 = +220 kJ (endothermic)
- [ ] Ea forward = 260 kJ; Ea reverse = 260 kJ; ΔH = +220 kJ
    - *why wrong:* The reverse barrier is measured from the PRODUCTS: 340 − 300 = 40 kJ, not the same as the forward barrier.
- [ ] Ea forward = 340 − 300 = 40 kJ; Ea reverse = 260 kJ; ΔH = +220 kJ
    - *why wrong:* Forward and reverse are swapped: forward is peak − reactants = 260 kJ; reverse is peak − products = 40 kJ.
- [ ] Ea forward = 260 kJ; Ea reverse = 40 kJ; ΔH = 80 − 300 = −220 kJ
    - *why wrong:* ΔH = products − reactants = 300 − 80 = +220 kJ (endothermic); doing reactants − products gives the wrong sign.
  > 🚩 **Reviewer note:** Forward/reverse activation energy and ΔH from one profile. Please full-review.

**Q12. [reason · TH]** Two reactions have the same ΔH, but reaction A has a much larger activation energy than reaction B. Predict which is likely to be slower at room temperature, and explain why.
- [✔︎] Reaction A — its larger activation energy means fewer colliding particles have enough energy to react, so it goes more slowly
- [ ] Reaction B, because a smaller activation energy releases less energy
    - *why wrong:* A smaller activation energy makes B FASTER, not slower; and activation energy is not about how much energy is released.
- [ ] They react at the same rate because they have the same ΔH
    - *why wrong:* ΔH sets the overall energy change, not the rate; the different activation energies mean different rates.
- [ ] Reaction A, because a large activation energy means it is very exothermic
    - *why wrong:* Reaction A is slower because of the high barrier, but activation-energy size does not tell you how exothermic a reaction is (that is ΔH).

**FIFA worked examples ⭐ (full review):**

#### Foundation (Combined-Foundation & Triple-Foundation) FIFA
- **Overall energy change from a profile** — On a reaction profile the reactants are at 250 kJ and the products at 190 kJ. Calculate the overall energy change, ΔH, and state whether the reaction is exothermic or endothermic.
    - **F** — ΔH = energy of products − energy of reactants
    - **I** — ΔH = 190 − 250
    - **F** — subtract
    - **A** — ΔH = −60 kJ (exothermic — the products are lower)
- **Activation energy from a profile** — On the same profile the peak of the curve is at 320 kJ and the reactants are at 250 kJ. Calculate the activation energy.
    - **F** — activation energy = energy of peak − energy of reactants
    - **I** — Ea = 320 − 250
    - **F** — subtract
    - **A** — Ea = 70 kJ
- **An endothermic profile** — On another profile the reactants are at 100 kJ and the products at 175 kJ. Calculate ΔH and state the type of reaction.
    - **F** — ΔH = energy of products − energy of reactants
    - **I** — ΔH = 175 − 100
    - **F** — subtract
    - **A** — ΔH = +75 kJ (endothermic — the products are higher)

#### Higher (Combined-Higher & Triple-Higher) FIFA
- **Both Ea and ΔH from one profile** — A reaction profile has reactants at 400 kJ, a peak at 560 kJ and products at 290 kJ. Calculate the activation energy and ΔH, and classify the reaction.
    - **F** — Ea = energy of peak − energy of reactants;  ΔH = energy of products − energy of reactants
    - **I** — Ea = 560 − 400;  ΔH = 290 − 400
    - **F** — Ea = 160 kJ;  ΔH = −110 kJ
    - **A** — Ea = 160 kJ, ΔH = −110 kJ — exothermic (ΔH is negative)
- **Reverse activation energy** — For the same profile (peak 560 kJ, products 290 kJ), calculate the activation energy of the reverse reaction.
    - **F** — Ea(reverse) = energy of peak − energy of products
    - **I** — = 560 − 290
    - **F** — subtract
    - **A** — Ea(reverse) = 270 kJ (larger than the forward 160 kJ, as expected for an exothermic reaction)
- **Working backwards to the product energy** — A reaction has reactants at 500 kJ and ΔH = +90 kJ. Calculate the energy of the products.
    - **F** — ΔH = energy of products − energy of reactants, so energy of products = reactants + ΔH
    - **I** — energy of products = 500 + 90
    - **F** — add
    - **A** — energy of products = 590 kJ (higher than the reactants, confirming it is endothermic)


---

## Bond Energy Calculations  ·  `bond-energy-calculations`  ·  AQA 5.5.1.3

> 🚩 **Triple-depth call (your review):** HIGHER-ONLY page (AQA 5.5.1.3 bond-energy calculations are Higher-tier content), so it exists only in the Combined-Higher and Triple-Higher files — there is no Foundation cell. Triple-Higher = the exact Combined-Higher set + 2 extra Higher-depth items (hydrogen combustion; evaluating fuels from their ΔH). Both tiers use the same FIFA (the calculation skill is identical); the Triple extra is additional coverage, exactly as your model specifies.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often mix up which way round to subtract in a bond-energy calculation, writing ΔH = (energy to make bonds) − (energy to break bonds). It is the other way round: ΔH = (energy IN to BREAK the reactant bonds) − (energy OUT to MAKE the product bonds). A second frequent slip is to forget that breaking bonds is endothermic (takes energy in) while making bonds is exothermic (gives energy out), then to drop the minus sign — so an exothermic reaction, where the bonds made release more than the bonds broken absorb, gets wrongly reported as positive.

**Question sets by tier** (each item shows tiers it appears in; ⭐ = full-review flag):

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [calc/derivation · CHTH] ⭐** Hydrogen reacts with chlorine: H₂ + Cl₂ → 2HCl. Bond energies (kJ/mol): H–H = 436, Cl–Cl = 242, H–Cl = 431. Calculate ΔH.
- [✔︎] −184 kJ/mol (break 436 + 242 = 678; make 2 × 431 = 862; ΔH = 678 − 862)
- [ ] +184 kJ/mol — subtracted the wrong way round (made − broken)
    - *why wrong:* ΔH = bonds broken − bonds made = 678 − 862 = −184 kJ/mol; doing made − broken flips the sign.
- [ ] +1540 kJ/mol — added broken and made
    - *why wrong:* You must SUBTRACT (broken − made): 678 − 862 = −184 kJ/mol, not add them (678 + 862 = 1540).
- [ ] +247 kJ/mol — counted only one H–Cl bond made
    - *why wrong:* 2 mol of HCl form, so two H–Cl bonds are made (2 × 431 = 862 kJ); using one gives the wrong answer.
  > 🚩 **Reviewer note:** Diatomic bond-energy calculation. Please full-review.

**Q2. [reason · CHTH]** Explain, in terms of bond breaking and bond making, why some reactions are exothermic overall.
- [✔︎] More energy is released making the new bonds in the products than is taken in breaking the bonds in the reactants, so there is a net release of energy (ΔH negative)
- [ ] Breaking the reactant bonds releases energy, which heats the surroundings
    - *why wrong:* Breaking bonds ABSORBS energy (endothermic); the net release comes from making bonds giving out more than breaking takes in.
- [ ] The products always contain more bonds than the reactants
    - *why wrong:* It is not the number of bonds but the balance of energy: bonds made release more than bonds broken absorb.
- [ ] No energy is needed to break bonds in an exothermic reaction
    - *why wrong:* Energy is always needed to break bonds; a reaction is exothermic when making bonds releases MORE than breaking them absorbs.

**Q3. [reason · CHTH]** Describe the energy change when bonds are broken and when bonds are made, and state the sign each contributes to ΔH.
- [✔︎] Breaking bonds is endothermic (takes energy in — a positive contribution); making bonds is exothermic (gives energy out — a negative contribution)
- [ ] Breaking bonds is exothermic; making bonds is endothermic
    - *why wrong:* This is reversed — breaking bonds takes energy IN (endothermic); making bonds gives energy OUT (exothermic).
- [ ] Both breaking and making bonds release energy
    - *why wrong:* Only making bonds releases energy; breaking bonds absorbs it.
- [ ] Both breaking and making bonds absorb energy
    - *why wrong:* Only breaking bonds absorbs energy; making bonds releases it.

**Q4. [calc/derivation · CHTH] ⭐** Hydrogen reacts with bromine: H₂ + Br₂ → 2HBr. Bond energies (kJ/mol): H–H = 436, Br–Br = 193, H–Br = 366. Calculate ΔH.
- [✔︎] −103 kJ/mol (break 436 + 193 = 629; make 2 × 366 = 732; ΔH = 629 − 732)
- [ ] +103 kJ/mol — worked out made − broken
    - *why wrong:* ΔH = broken − made = 629 − 732 = −103 kJ/mol; reversing the subtraction flips the sign.
- [ ] +1361 kJ/mol — added broken and made
    - *why wrong:* ΔH is broken − made = 629 − 732, not the sum (629 + 732 = 1361).
- [ ] +263 kJ/mol — counted only one H–Br bond made
    - *why wrong:* 2 mol of HBr form, so two H–Br bonds are made (2 × 366 = 732 kJ); using one gives the wrong answer.
  > 🚩 **Reviewer note:** Diatomic bond-energy calculation. Please full-review.

**Q5. [apply · CHTH] ⭐** In a reaction the total energy needed to break the reactant bonds is 1650 kJ and the total energy released making the product bonds is 1806 kJ. Calculate ΔH and state whether the reaction is exothermic or endothermic.
- [✔︎] ΔH = 1650 − 1806 = −156 kJ; exothermic (more energy released making bonds than absorbed breaking them)
- [ ] ΔH = 1806 − 1650 = +156 kJ; endothermic
    - *why wrong:* ΔH = energy to break − energy to make = 1650 − 1806 = −156 kJ; the reaction is exothermic.
- [ ] ΔH = 1650 + 1806 = 3456 kJ; exothermic
    - *why wrong:* ΔH is the DIFFERENCE (break − make), not the sum of the two totals.
- [ ] ΔH = −156 kJ; endothermic
    - *why wrong:* The value is right, but a negative ΔH is exothermic, not endothermic.
  > 🚩 **Reviewer note:** ΔH from break/make totals. Please full-review.

**Q6. [calc/derivation · CHTH] ⭐** Methane burns completely: CH₄ + 2O₂ → CO₂ + 2H₂O. Bond energies (kJ/mol): C–H = 412, O=O = 498, C=O = 743, O–H = 463. Calculate ΔH.
- [✔︎] −694 kJ/mol (break 4×412 + 2×498 = 2644; make 2×743 + 4×463 = 3338; ΔH = 2644 − 3338)
- [ ] +694 kJ/mol — subtracted the wrong way round (made − broken)
    - *why wrong:* ΔH = broken − made = 2644 − 3338 = −694 kJ/mol; reversing the subtraction flips the sign.
- [ ] +232 kJ/mol — counted only 2 O–H bonds instead of 4
    - *why wrong:* 2 H₂O molecules form, each with 2 O–H bonds, so 4 O–H bonds are made (4 × 463); using 2 gives the wrong answer.
- [ ] +5982 kJ/mol — added broken and made instead of subtracting
    - *why wrong:* ΔH is broken − made = 2644 − 3338, not the sum (2644 + 3338 = 5982).
  > 🚩 **Reviewer note:** Multi-bond combustion calculation. Please full-review.

**Q7. [calc/derivation · CHTH] ⭐** For H₂ + Br₂ → 2HBr the enthalpy change is ΔH = −103 kJ/mol. Bond energies (kJ/mol): H–H = 436, Br–Br = 193. Calculate the bond energy of the H–Br bond.
- [✔︎] 366 kJ/mol (ΔH = 629 − 2 × H–Br = −103, so 2 × H–Br = 732, H–Br = 366)
- [ ] 732 kJ/mol — forgot that two H–Br bonds form
    - *why wrong:* 2 mol of HBr form, so ΔH = 629 − 2 × (H–Br); dividing by 2 gives H–Br = 366, not 732.
- [ ] 263 kJ/mol — subtracted ΔH instead of adding it
    - *why wrong:* Rearranging 629 − 2X = −103 gives 2X = 629 + 103 = 732, so X = 366; subtracting 103 gives 263.
- [ ] 314.5 kJ/mol — averaged the two reactant bond energies
    - *why wrong:* The H–Br bond energy comes from rearranging the ΔH equation (X = 366), not from averaging the reactant bonds.
  > 🚩 **Reviewer note:** Rearrangement to find a missing bond energy. Please full-review.

**Q8. [calc/derivation · CHTH] ⭐** The Haber process: N₂ + 3H₂ → 2NH₃. Bond energies (kJ/mol): N≡N = 945, H–H = 436, N–H = 391. Calculate ΔH.
- [✔︎] −93 kJ/mol (break 945 + 3×436 = 2253; make 6×391 = 2346; ΔH = 2253 − 2346)
- [ ] +93 kJ/mol — subtracted made − broken
    - *why wrong:* ΔH = broken − made = 2253 − 2346 = −93 kJ/mol; reversing the subtraction flips the sign.
- [ ] +1080 kJ/mol — used only 3 N–H bonds instead of 6
    - *why wrong:* 2 NH₃ molecules form, each with 3 N–H bonds, so 6 N–H bonds are made (6 × 391); using 3 gives the wrong answer.
- [ ] −4599 kJ/mol — added broken and made
    - *why wrong:* ΔH is broken − made = 2253 − 2346, not the sum (2253 + 2346 = 4599).
  > 🚩 **Reviewer note:** Multi-bond calculation with a triple bond. Please full-review.

**Q9. [reason · CHTH]** In a bond-energy calculation a student finds the energy to break the reactant bonds is greater than the energy released making the product bonds. Deduce the sign of ΔH and the type of reaction.
- [✔︎] ΔH is positive and the reaction is endothermic — more energy is absorbed breaking bonds than is released making them
- [ ] ΔH is negative and the reaction is exothermic
    - *why wrong:* If breaking takes MORE energy than making releases, the net is energy absorbed → a positive ΔH, endothermic.
- [ ] ΔH is positive and the reaction is exothermic
    - *why wrong:* A positive ΔH is endothermic, not exothermic.
- [ ] ΔH is zero because the two roughly cancel
    - *why wrong:* They do not cancel here — breaking needs more than making releases, so there is a net positive ΔH.

**Q10. [calc/derivation · CHTH] ⭐** Ethene is hydrogenated: C₂H₄ + H₂ → C₂H₆. Bond energies (kJ/mol): C–H = 412, C=C = 612, H–H = 436, C–C = 347. (Ethene has 4 C–H and 1 C=C; ethane has 6 C–H and 1 C–C.) Calculate ΔH.
- [✔︎] −123 kJ/mol (break 4×412 + 612 + 436 = 2696; make 6×412 + 347 = 2819; ΔH = 2696 − 2819)
- [ ] +123 kJ/mol — subtracted made − broken
    - *why wrong:* ΔH = broken − made = 2696 − 2819 = −123 kJ/mol; reversing the subtraction flips the sign.
- [ ] −388 kJ/mol — used a C–C single-bond value (347) for the C=C double bond
    - *why wrong:* Ethene has a C=C DOUBLE bond (612 kJ/mol); using the single-bond value understates the energy needed to break it.
- [ ] +5515 kJ/mol — added broken and made instead of subtracting
    - *why wrong:* ΔH is broken − made = 2696 − 2819, not the sum (2696 + 2819 = 5515).
  > 🚩 **Reviewer note:** Bond-energy calculation from a described structure. Please full-review.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [calc/derivation · CHTH] ⭐** Hydrogen reacts with chlorine: H₂ + Cl₂ → 2HCl. Bond energies (kJ/mol): H–H = 436, Cl–Cl = 242, H–Cl = 431. Calculate ΔH.
- [✔︎] −184 kJ/mol (break 436 + 242 = 678; make 2 × 431 = 862; ΔH = 678 − 862)
- [ ] +184 kJ/mol — subtracted the wrong way round (made − broken)
    - *why wrong:* ΔH = bonds broken − bonds made = 678 − 862 = −184 kJ/mol; doing made − broken flips the sign.
- [ ] +1540 kJ/mol — added broken and made
    - *why wrong:* You must SUBTRACT (broken − made): 678 − 862 = −184 kJ/mol, not add them (678 + 862 = 1540).
- [ ] +247 kJ/mol — counted only one H–Cl bond made
    - *why wrong:* 2 mol of HCl form, so two H–Cl bonds are made (2 × 431 = 862 kJ); using one gives the wrong answer.
  > 🚩 **Reviewer note:** Diatomic bond-energy calculation. Please full-review.

**Q2. [reason · CHTH]** Explain, in terms of bond breaking and bond making, why some reactions are exothermic overall.
- [✔︎] More energy is released making the new bonds in the products than is taken in breaking the bonds in the reactants, so there is a net release of energy (ΔH negative)
- [ ] Breaking the reactant bonds releases energy, which heats the surroundings
    - *why wrong:* Breaking bonds ABSORBS energy (endothermic); the net release comes from making bonds giving out more than breaking takes in.
- [ ] The products always contain more bonds than the reactants
    - *why wrong:* It is not the number of bonds but the balance of energy: bonds made release more than bonds broken absorb.
- [ ] No energy is needed to break bonds in an exothermic reaction
    - *why wrong:* Energy is always needed to break bonds; a reaction is exothermic when making bonds releases MORE than breaking them absorbs.

**Q3. [reason · CHTH]** Describe the energy change when bonds are broken and when bonds are made, and state the sign each contributes to ΔH.
- [✔︎] Breaking bonds is endothermic (takes energy in — a positive contribution); making bonds is exothermic (gives energy out — a negative contribution)
- [ ] Breaking bonds is exothermic; making bonds is endothermic
    - *why wrong:* This is reversed — breaking bonds takes energy IN (endothermic); making bonds gives energy OUT (exothermic).
- [ ] Both breaking and making bonds release energy
    - *why wrong:* Only making bonds releases energy; breaking bonds absorbs it.
- [ ] Both breaking and making bonds absorb energy
    - *why wrong:* Only breaking bonds absorbs energy; making bonds releases it.

**Q4. [calc/derivation · CHTH] ⭐** Hydrogen reacts with bromine: H₂ + Br₂ → 2HBr. Bond energies (kJ/mol): H–H = 436, Br–Br = 193, H–Br = 366. Calculate ΔH.
- [✔︎] −103 kJ/mol (break 436 + 193 = 629; make 2 × 366 = 732; ΔH = 629 − 732)
- [ ] +103 kJ/mol — worked out made − broken
    - *why wrong:* ΔH = broken − made = 629 − 732 = −103 kJ/mol; reversing the subtraction flips the sign.
- [ ] +1361 kJ/mol — added broken and made
    - *why wrong:* ΔH is broken − made = 629 − 732, not the sum (629 + 732 = 1361).
- [ ] +263 kJ/mol — counted only one H–Br bond made
    - *why wrong:* 2 mol of HBr form, so two H–Br bonds are made (2 × 366 = 732 kJ); using one gives the wrong answer.
  > 🚩 **Reviewer note:** Diatomic bond-energy calculation. Please full-review.

**Q5. [apply · CHTH] ⭐** In a reaction the total energy needed to break the reactant bonds is 1650 kJ and the total energy released making the product bonds is 1806 kJ. Calculate ΔH and state whether the reaction is exothermic or endothermic.
- [✔︎] ΔH = 1650 − 1806 = −156 kJ; exothermic (more energy released making bonds than absorbed breaking them)
- [ ] ΔH = 1806 − 1650 = +156 kJ; endothermic
    - *why wrong:* ΔH = energy to break − energy to make = 1650 − 1806 = −156 kJ; the reaction is exothermic.
- [ ] ΔH = 1650 + 1806 = 3456 kJ; exothermic
    - *why wrong:* ΔH is the DIFFERENCE (break − make), not the sum of the two totals.
- [ ] ΔH = −156 kJ; endothermic
    - *why wrong:* The value is right, but a negative ΔH is exothermic, not endothermic.
  > 🚩 **Reviewer note:** ΔH from break/make totals. Please full-review.

**Q6. [calc/derivation · CHTH] ⭐** Methane burns completely: CH₄ + 2O₂ → CO₂ + 2H₂O. Bond energies (kJ/mol): C–H = 412, O=O = 498, C=O = 743, O–H = 463. Calculate ΔH.
- [✔︎] −694 kJ/mol (break 4×412 + 2×498 = 2644; make 2×743 + 4×463 = 3338; ΔH = 2644 − 3338)
- [ ] +694 kJ/mol — subtracted the wrong way round (made − broken)
    - *why wrong:* ΔH = broken − made = 2644 − 3338 = −694 kJ/mol; reversing the subtraction flips the sign.
- [ ] +232 kJ/mol — counted only 2 O–H bonds instead of 4
    - *why wrong:* 2 H₂O molecules form, each with 2 O–H bonds, so 4 O–H bonds are made (4 × 463); using 2 gives the wrong answer.
- [ ] +5982 kJ/mol — added broken and made instead of subtracting
    - *why wrong:* ΔH is broken − made = 2644 − 3338, not the sum (2644 + 3338 = 5982).
  > 🚩 **Reviewer note:** Multi-bond combustion calculation. Please full-review.

**Q7. [calc/derivation · CHTH] ⭐** For H₂ + Br₂ → 2HBr the enthalpy change is ΔH = −103 kJ/mol. Bond energies (kJ/mol): H–H = 436, Br–Br = 193. Calculate the bond energy of the H–Br bond.
- [✔︎] 366 kJ/mol (ΔH = 629 − 2 × H–Br = −103, so 2 × H–Br = 732, H–Br = 366)
- [ ] 732 kJ/mol — forgot that two H–Br bonds form
    - *why wrong:* 2 mol of HBr form, so ΔH = 629 − 2 × (H–Br); dividing by 2 gives H–Br = 366, not 732.
- [ ] 263 kJ/mol — subtracted ΔH instead of adding it
    - *why wrong:* Rearranging 629 − 2X = −103 gives 2X = 629 + 103 = 732, so X = 366; subtracting 103 gives 263.
- [ ] 314.5 kJ/mol — averaged the two reactant bond energies
    - *why wrong:* The H–Br bond energy comes from rearranging the ΔH equation (X = 366), not from averaging the reactant bonds.
  > 🚩 **Reviewer note:** Rearrangement to find a missing bond energy. Please full-review.

**Q8. [calc/derivation · CHTH] ⭐** The Haber process: N₂ + 3H₂ → 2NH₃. Bond energies (kJ/mol): N≡N = 945, H–H = 436, N–H = 391. Calculate ΔH.
- [✔︎] −93 kJ/mol (break 945 + 3×436 = 2253; make 6×391 = 2346; ΔH = 2253 − 2346)
- [ ] +93 kJ/mol — subtracted made − broken
    - *why wrong:* ΔH = broken − made = 2253 − 2346 = −93 kJ/mol; reversing the subtraction flips the sign.
- [ ] +1080 kJ/mol — used only 3 N–H bonds instead of 6
    - *why wrong:* 2 NH₃ molecules form, each with 3 N–H bonds, so 6 N–H bonds are made (6 × 391); using 3 gives the wrong answer.
- [ ] −4599 kJ/mol — added broken and made
    - *why wrong:* ΔH is broken − made = 2253 − 2346, not the sum (2253 + 2346 = 4599).
  > 🚩 **Reviewer note:** Multi-bond calculation with a triple bond. Please full-review.

**Q9. [reason · CHTH]** In a bond-energy calculation a student finds the energy to break the reactant bonds is greater than the energy released making the product bonds. Deduce the sign of ΔH and the type of reaction.
- [✔︎] ΔH is positive and the reaction is endothermic — more energy is absorbed breaking bonds than is released making them
- [ ] ΔH is negative and the reaction is exothermic
    - *why wrong:* If breaking takes MORE energy than making releases, the net is energy absorbed → a positive ΔH, endothermic.
- [ ] ΔH is positive and the reaction is exothermic
    - *why wrong:* A positive ΔH is endothermic, not exothermic.
- [ ] ΔH is zero because the two roughly cancel
    - *why wrong:* They do not cancel here — breaking needs more than making releases, so there is a net positive ΔH.

**Q10. [calc/derivation · CHTH] ⭐** Ethene is hydrogenated: C₂H₄ + H₂ → C₂H₆. Bond energies (kJ/mol): C–H = 412, C=C = 612, H–H = 436, C–C = 347. (Ethene has 4 C–H and 1 C=C; ethane has 6 C–H and 1 C–C.) Calculate ΔH.
- [✔︎] −123 kJ/mol (break 4×412 + 612 + 436 = 2696; make 6×412 + 347 = 2819; ΔH = 2696 − 2819)
- [ ] +123 kJ/mol — subtracted made − broken
    - *why wrong:* ΔH = broken − made = 2696 − 2819 = −123 kJ/mol; reversing the subtraction flips the sign.
- [ ] −388 kJ/mol — used a C–C single-bond value (347) for the C=C double bond
    - *why wrong:* Ethene has a C=C DOUBLE bond (612 kJ/mol); using the single-bond value understates the energy needed to break it.
- [ ] +5515 kJ/mol — added broken and made instead of subtracting
    - *why wrong:* ΔH is broken − made = 2696 − 2819, not the sum (2696 + 2819 = 5515).
  > 🚩 **Reviewer note:** Bond-energy calculation from a described structure. Please full-review.

**Q11. [calc/derivation · TH] ⭐** Hydrogen burns as a fuel: 2H₂ + O₂ → 2H₂O. Bond energies (kJ/mol): H–H = 436, O=O = 498, O–H = 463. Calculate ΔH.
- [✔︎] −482 kJ/mol (break 2×436 + 498 = 1370; make 4×463 = 1852; ΔH = 1370 − 1852)
- [ ] +482 kJ/mol — subtracted made − broken
    - *why wrong:* ΔH = broken − made = 1370 − 1852 = −482 kJ/mol; reversing the subtraction flips the sign.
- [ ] +444 kJ/mol — used only 2 O–H bonds instead of 4
    - *why wrong:* 2 H₂O molecules form, each with 2 O–H bonds, so 4 O–H bonds are made (4 × 463); using 2 gives the wrong answer.
- [ ] −918 kJ/mol — counted only one H–H bond (forgot 2H₂)
    - *why wrong:* 2 mol of H₂ react, so two H–H bonds are broken (2 × 436 = 872 kJ); using one gives the wrong answer.
  > 🚩 **Reviewer note:** Combustion of hydrogen — Triple-Higher extra. Please full-review.

**Q12. [reason · TH]** The combustion of hydrogen has ΔH = −482 kJ/mol and the combustion of methane has ΔH = −694 kJ/mol (per mole of fuel). Evaluate the claim that methane releases more energy per mole, and give one limitation of judging a fuel by ΔH alone.
- [✔︎] The claim is supported — methane's ΔH (−694) is more negative than hydrogen's (−482), so it releases more energy per mole; but ΔH per mole ignores energy per gram, cost, and the products formed (methane makes CO₂, hydrogen makes only water)
- [ ] Hydrogen releases more energy per mole, because −482 is a smaller number
    - *why wrong:* −694 is MORE negative than −482, so methane releases more energy per mole; −482 releases less.
- [ ] The two cannot be compared because both values are negative
    - *why wrong:* Both being negative just means both are exothermic; you compare their sizes — −694 is larger than −482.
- [ ] Energy per mole is the only thing that matters when choosing a fuel
    - *why wrong:* Energy per mole is one factor; energy per gram, cost, availability and the products (CO₂ versus water) also matter.

**FIFA worked examples ⭐ (full review):**

#### Higher (Combined-Higher & Triple-Higher) FIFA
- **A simple diatomic reaction** — Hydrogen reacts with chlorine: H₂ + Cl₂ → 2HCl. Bond energies (kJ/mol): H–H = 436, Cl–Cl = 242, H–Cl = 431. Calculate ΔH.
    - **F** — ΔH = (energy to break the reactant bonds) − (energy to make the product bonds)
    - **I** — break = 436 + 242 = 678;  make = 2 × 431 = 862
    - **F** — ΔH = 678 − 862
    - **A** — ΔH = −184 kJ/mol (exothermic — more energy is released making bonds than is absorbed breaking them)
- **A molecule with several bonds (combustion)** — Methane burns completely: CH₄ + 2O₂ → CO₂ + 2H₂O. Bond energies (kJ/mol): C–H = 412, O=O = 498, C=O = 743, O–H = 463. Calculate ΔH.
    - **F** — ΔH = (bonds broken) − (bonds made)
    - **I** — break = (4 × 412) + (2 × 498) = 1648 + 996 = 2644;  make = (2 × 743) + (4 × 463) = 1486 + 1852 = 3338
    - **F** — ΔH = 2644 − 3338
    - **A** — ΔH = −694 kJ/mol (exothermic)
- **Working backwards to a missing bond energy** — For H₂ + Br₂ → 2HBr, ΔH = −103 kJ/mol. Bond energies (kJ/mol): H–H = 436, Br–Br = 193. Calculate the H–Br bond energy.
    - **F** — ΔH = (H–H + Br–Br) − (2 × H–Br), so rearrange for H–Br
    - **I** — −103 = (436 + 193) − (2 × H–Br) = 629 − 2 × H–Br
    - **F** — 2 × H–Br = 629 + 103 = 732, so H–Br = 732 ÷ 2
    - **A** — H–Br = 366 kJ/mol


---

## Cells and Batteries  ·  `cells-and-batteries`  ·  AQA 4.5.2.1

> 🚩 **Triple-depth call (your review):** TRIPLE-ONLY page (chemical cells and batteries are not in Combined Science), so it exists only in the two Triple files — there is no Combined comparison to make. Difficulty follows the tier: Triple-Foundation is pitched at Foundation demand (more recall, simple series-voltage sums), Triple-Higher scales up (opposing cells, reactivity-series ranking, evaluate reversible vs irreversible). The two tiers share an 8-question core and each add 4 tier-appropriate questions.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often call a single cell a 'battery' and think that adding more cells makes each one produce a bigger voltage. Neither is right: a battery is two or more cells joined in SERIES, and it is the voltages of the separate cells that ADD together — each individual cell still produces the same voltage. A second common error is to think a rechargeable cell never runs down; it does, but its reactions can be reversed by passing an external current through it, unlike a non-rechargeable cell whose reactions are irreversible.

**Question sets by tier** (each item shows tiers it appears in; ⭐ = full-review flag):

### Triple Foundation — 12 questions (4 recall / 8 apply+reason+calc)

**Q1. [reason · TFTH]** Explain how a simple chemical cell produces a voltage.
- [✔︎] Two different metals (the electrodes) are placed in an electrolyte; the difference in their reactivity drives a flow of electrons through the external circuit, producing a voltage
- [ ] The electrolyte is heated, which pushes electrons around the circuit
    - *why wrong:* The voltage comes from the reactivity DIFFERENCE between the two metals, not from heating the electrolyte.
- [ ] Two identical metals in the electrolyte create a large voltage
    - *why wrong:* The metals must be DIFFERENT; two identical metals have no reactivity difference and produce almost no voltage.
- [ ] Light shining on the metals releases the electrons
    - *why wrong:* A chemical cell is not light-powered; the voltage comes from the reactivity difference between two different metals.

**Q2. [apply · TFTH]** Predict what happens to the voltage of a cell if the two metals chosen are further apart in the reactivity series.
- [✔︎] The voltage increases — a bigger difference in reactivity produces a bigger voltage
- [ ] The voltage decreases
    - *why wrong:* A LARGER reactivity difference gives a LARGER voltage, not a smaller one.
- [ ] The voltage stays the same, whatever the metals
    - *why wrong:* The voltage depends on the metals; a bigger reactivity gap gives a bigger voltage.
- [ ] The cell stops working completely
    - *why wrong:* The cell still works; a wider reactivity gap simply increases the voltage.

**Q3. [apply · TFTH]** A single cell produces 1.5 V. Determine the voltage of a battery made from four of these cells connected in series.
- [✔︎] 6.0 V — the voltages of cells in series add together (4 × 1.5 V)
- [ ] 1.5 V — connecting cells in series does not change the voltage
    - *why wrong:* In series the voltages ADD, so four 1.5 V cells give 6.0 V.
- [ ] 0.375 V — the voltage is shared between the four cells
    - *why wrong:* Voltages in series add, they do not divide; 4 × 1.5 = 6.0 V.
- [ ] 3.0 V — only two of the cells count
    - *why wrong:* All four cells in series add: 4 × 1.5 = 6.0 V, not 2 × 1.5.

**Q4. [reason · TFTH]** Describe the difference between a rechargeable cell and a non-rechargeable cell in terms of their reactions.
- [✔︎] In a rechargeable cell the reactions can be reversed by passing an external current through it; in a non-rechargeable cell the reactions are irreversible, so it cannot be recharged
- [ ] A rechargeable cell never uses up its chemicals; a non-rechargeable one does
    - *why wrong:* A rechargeable cell does use up its chemicals as it runs, but an external current REVERSES the reactions to restore it.
- [ ] A non-rechargeable cell can be recharged more times than a rechargeable one
    - *why wrong:* This is back to front — only the rechargeable cell can be recharged (its reactions are reversible).
- [ ] Rechargeable cells produce a voltage without any reactions
    - *why wrong:* All chemical cells rely on reactions; the difference is whether those reactions can be reversed.

**Q5. [reason · TFTH]** Explain why a battery gives a higher voltage than a single one of the cells inside it.
- [✔︎] A battery is two or more cells connected in series, and the voltages of cells in series add together
- [ ] The cells inside a battery are bigger than a single cell
    - *why wrong:* It is not size but the number of cells in series; their voltages add together.
- [ ] A battery reverses its reactions to boost the voltage
    - *why wrong:* Reversing reactions is recharging; the higher voltage comes from adding cells in series.
- [ ] The battery is connected to the mains, which raises the voltage
    - *why wrong:* A battery is not mains-powered; its voltage is the sum of its cells in series.

**Q6. [apply · TFTH]** Suggest why a cell made from magnesium and copper produces a larger voltage than one made from zinc and copper.
- [✔︎] Magnesium is further from copper in the reactivity series than zinc is, so the bigger reactivity difference gives a bigger voltage
- [ ] Magnesium is a better electrical conductor than zinc
    - *why wrong:* The voltage depends on the reactivity DIFFERENCE between the electrodes, not on how well the metal conducts.
- [ ] Copper becomes more reactive when it is paired with magnesium
    - *why wrong:* Copper's reactivity does not change; magnesium simply has a bigger reactivity gap from copper than zinc does.
- [ ] Magnesium cells are always larger in size
    - *why wrong:* Size is not the reason; the larger voltage comes from the greater reactivity difference.

**Q7. [recall · TFTH]** State what a simple chemical cell is made from.
- [✔︎] Two different metals (electrodes) dipped in an electrolyte
- [ ] Two identical metals in pure water
    - *why wrong:* The metals must be DIFFERENT, and pure water is a poor electrolyte.
- [ ] A single metal connected to a light bulb
    - *why wrong:* A cell needs TWO different metals in an electrolyte, not one metal alone.
- [ ] Two non-metals dipped in an electrolyte
    - *why wrong:* The electrodes are metals with different reactivities, not non-metals.

**Q8. [recall · TFTH]** Name the metal used in the rechargeable batteries found in most phones and laptops.
- [✔︎] Lithium (lithium-ion batteries)
- [ ] Sodium, as sodium chloride
    - *why wrong:* Sodium chloride is table salt (an electrolyte), not the metal used in phone batteries — that is lithium.
- [ ] Copper
    - *why wrong:* Copper is used in wiring; modern rechargeable phone and laptop batteries are lithium-ion.
- [ ] Iron
    - *why wrong:* Iron is not the basis of modern phone batteries; lithium-ion cells are used.

**Q9. [recall · TF]** State what happens to a non-rechargeable cell once its chemical reactions are complete.
- [✔︎] It stops producing a voltage (goes flat) and cannot be recharged
- [ ] It recharges itself if it is left to rest
    - *why wrong:* A non-rechargeable cell cannot recharge; its reactions are irreversible.
- [ ] It produces a higher voltage than before
    - *why wrong:* Once the reactants are used up the cell goes flat; it does not produce more voltage.
- [ ] It can be refilled with more electrolyte to restart
    - *why wrong:* The reactants at the electrodes are used up irreversibly; topping up the electrolyte does not restore it.

**Q10. [recall · TF]** State one factor, other than the choice of metals, that can affect the voltage of a cell.
- [✔︎] The type or concentration of the electrolyte
- [ ] The colour of the connecting wires
    - *why wrong:* Wire colour has no effect on voltage; the electrolyte and the metals do.
- [ ] The time of day the cell is used
    - *why wrong:* Time of day does not affect a cell; the factors are the metals and the electrolyte.
- [ ] The size of the light bulb attached to it
    - *why wrong:* The bulb is part of the external circuit; the cell's voltage depends on the electrodes and electrolyte.

**Q11. [apply · TF]** A torch needs 3 V to work. Determine how many 1.5 V cells must be connected in series to power it.
- [✔︎] Two cells (2 × 1.5 V = 3 V)
- [ ] Four cells
    - *why wrong:* Four 1.5 V cells in series give 6 V, double what is needed; two cells give 3 V.
- [ ] One cell
    - *why wrong:* One 1.5 V cell gives only 1.5 V; two in series are needed for 3 V.
- [ ] Three cells
    - *why wrong:* Three 1.5 V cells give 4.5 V, more than needed; two give exactly 3 V.

**Q12. [apply · TF]** Suggest one environmental advantage of using rechargeable batteries instead of single-use ones.
- [✔︎] They can be reused many times, so fewer batteries are thrown away, reducing waste and the use of raw materials
- [ ] They never contain any harmful chemicals
    - *why wrong:* Rechargeable batteries still contain chemicals that need careful disposal; the advantage is that they are reused, cutting waste.
- [ ] They produce more voltage, which is better for the environment
    - *why wrong:* Voltage is not the environmental point; reusing them reduces the number of batteries discarded.
- [ ] They can be thrown in with normal household rubbish safely
    - *why wrong:* Batteries should be recycled, not binned; the environmental benefit is reuse reducing waste.

### Triple Higher — 12 questions (2 recall / 10 apply+reason+calc)

**Q1. [reason · TFTH]** Explain how a simple chemical cell produces a voltage.
- [✔︎] Two different metals (the electrodes) are placed in an electrolyte; the difference in their reactivity drives a flow of electrons through the external circuit, producing a voltage
- [ ] The electrolyte is heated, which pushes electrons around the circuit
    - *why wrong:* The voltage comes from the reactivity DIFFERENCE between the two metals, not from heating the electrolyte.
- [ ] Two identical metals in the electrolyte create a large voltage
    - *why wrong:* The metals must be DIFFERENT; two identical metals have no reactivity difference and produce almost no voltage.
- [ ] Light shining on the metals releases the electrons
    - *why wrong:* A chemical cell is not light-powered; the voltage comes from the reactivity difference between two different metals.

**Q2. [apply · TFTH]** Predict what happens to the voltage of a cell if the two metals chosen are further apart in the reactivity series.
- [✔︎] The voltage increases — a bigger difference in reactivity produces a bigger voltage
- [ ] The voltage decreases
    - *why wrong:* A LARGER reactivity difference gives a LARGER voltage, not a smaller one.
- [ ] The voltage stays the same, whatever the metals
    - *why wrong:* The voltage depends on the metals; a bigger reactivity gap gives a bigger voltage.
- [ ] The cell stops working completely
    - *why wrong:* The cell still works; a wider reactivity gap simply increases the voltage.

**Q3. [apply · TFTH]** A single cell produces 1.5 V. Determine the voltage of a battery made from four of these cells connected in series.
- [✔︎] 6.0 V — the voltages of cells in series add together (4 × 1.5 V)
- [ ] 1.5 V — connecting cells in series does not change the voltage
    - *why wrong:* In series the voltages ADD, so four 1.5 V cells give 6.0 V.
- [ ] 0.375 V — the voltage is shared between the four cells
    - *why wrong:* Voltages in series add, they do not divide; 4 × 1.5 = 6.0 V.
- [ ] 3.0 V — only two of the cells count
    - *why wrong:* All four cells in series add: 4 × 1.5 = 6.0 V, not 2 × 1.5.

**Q4. [reason · TFTH]** Describe the difference between a rechargeable cell and a non-rechargeable cell in terms of their reactions.
- [✔︎] In a rechargeable cell the reactions can be reversed by passing an external current through it; in a non-rechargeable cell the reactions are irreversible, so it cannot be recharged
- [ ] A rechargeable cell never uses up its chemicals; a non-rechargeable one does
    - *why wrong:* A rechargeable cell does use up its chemicals as it runs, but an external current REVERSES the reactions to restore it.
- [ ] A non-rechargeable cell can be recharged more times than a rechargeable one
    - *why wrong:* This is back to front — only the rechargeable cell can be recharged (its reactions are reversible).
- [ ] Rechargeable cells produce a voltage without any reactions
    - *why wrong:* All chemical cells rely on reactions; the difference is whether those reactions can be reversed.

**Q5. [reason · TFTH]** Explain why a battery gives a higher voltage than a single one of the cells inside it.
- [✔︎] A battery is two or more cells connected in series, and the voltages of cells in series add together
- [ ] The cells inside a battery are bigger than a single cell
    - *why wrong:* It is not size but the number of cells in series; their voltages add together.
- [ ] A battery reverses its reactions to boost the voltage
    - *why wrong:* Reversing reactions is recharging; the higher voltage comes from adding cells in series.
- [ ] The battery is connected to the mains, which raises the voltage
    - *why wrong:* A battery is not mains-powered; its voltage is the sum of its cells in series.

**Q6. [apply · TFTH]** Suggest why a cell made from magnesium and copper produces a larger voltage than one made from zinc and copper.
- [✔︎] Magnesium is further from copper in the reactivity series than zinc is, so the bigger reactivity difference gives a bigger voltage
- [ ] Magnesium is a better electrical conductor than zinc
    - *why wrong:* The voltage depends on the reactivity DIFFERENCE between the electrodes, not on how well the metal conducts.
- [ ] Copper becomes more reactive when it is paired with magnesium
    - *why wrong:* Copper's reactivity does not change; magnesium simply has a bigger reactivity gap from copper than zinc does.
- [ ] Magnesium cells are always larger in size
    - *why wrong:* Size is not the reason; the larger voltage comes from the greater reactivity difference.

**Q7. [recall · TFTH]** State what a simple chemical cell is made from.
- [✔︎] Two different metals (electrodes) dipped in an electrolyte
- [ ] Two identical metals in pure water
    - *why wrong:* The metals must be DIFFERENT, and pure water is a poor electrolyte.
- [ ] A single metal connected to a light bulb
    - *why wrong:* A cell needs TWO different metals in an electrolyte, not one metal alone.
- [ ] Two non-metals dipped in an electrolyte
    - *why wrong:* The electrodes are metals with different reactivities, not non-metals.

**Q8. [recall · TFTH]** Name the metal used in the rechargeable batteries found in most phones and laptops.
- [✔︎] Lithium (lithium-ion batteries)
- [ ] Sodium, as sodium chloride
    - *why wrong:* Sodium chloride is table salt (an electrolyte), not the metal used in phone batteries — that is lithium.
- [ ] Copper
    - *why wrong:* Copper is used in wiring; modern rechargeable phone and laptop batteries are lithium-ion.
- [ ] Iron
    - *why wrong:* Iron is not the basis of modern phone batteries; lithium-ion cells are used.

**Q9. [reason · TH]** Explain, in terms of its reactions, why a rechargeable lithium-ion cell can be used many times but an alkaline cell cannot.
- [✔︎] In the lithium-ion cell the reactions are reversible, so passing an external current reverses them and restores the reactants; in the alkaline cell the reactions are irreversible, so once the reactants are used up it cannot be restored
- [ ] The lithium-ion cell makes new reactants from the air as it runs
    - *why wrong:* It does not make reactants from air; recharging reverses its reactions to restore the original reactants.
- [ ] The alkaline cell has no reactions, so there is nothing to reverse
    - *why wrong:* The alkaline cell does have reactions — they are simply irreversible, so it cannot be recharged.
- [ ] Both cells are recharged in the same way, by resting them
    - *why wrong:* Only the lithium-ion cell recharges, and only by an external current, not by resting.

**Q10. [apply · TH]** A student connects two identical cells so that their voltages oppose each other (positive terminal joined to positive terminal). Predict the effect on the overall voltage and explain.
- [✔︎] The voltages cancel to give zero overall, because the two equal cells push in opposite directions
- [ ] The voltages still add to give the largest possible voltage
    - *why wrong:* Voltages add only when cells face the same way; opposing them makes the voltages subtract.
- [ ] The overall voltage doubles because there are two cells
    - *why wrong:* Two cells double the voltage only when connected the same way; opposing them cancels rather than adds.
- [ ] The cells explode because the voltages fight each other
    - *why wrong:* The voltages simply subtract; connecting them in opposition reduces the net voltage, it does not cause an explosion.

**Q11. [apply · TH]** Using the reactivity series, predict which pair of metals gives the largest voltage in a cell: (a) zinc and iron, (b) magnesium and silver, (c) copper and silver. Justify your choice.
- [✔︎] (b) magnesium and silver — magnesium is very reactive and silver very unreactive, so this pair has the largest reactivity difference and the largest voltage
- [ ] (a) zinc and iron, because they are both fairly reactive
    - *why wrong:* Zinc and iron are close together in the reactivity series, so their small difference gives a small voltage.
- [ ] (c) copper and silver, because they are both shiny metals
    - *why wrong:* Copper and silver are both unreactive and close together, so the reactivity difference (and voltage) is small.
- [ ] All three pairs would give exactly the same voltage
    - *why wrong:* Voltage depends on the reactivity gap, which is largest for magnesium and silver, so they are not all the same.

**Q12. [reason · TH]** Evaluate one advantage and one disadvantage of rechargeable batteries compared with non-rechargeable ones.
- [✔︎] Advantage: they can be recharged and reused many times, reducing waste and long-term cost. Disadvantage: they usually cost more to buy at first and lose some capacity (hold less charge) as they age
- [ ] Advantage: they never need charging. Disadvantage: they are cheaper to buy
    - *why wrong:* Rechargeable batteries DO need charging (that is the point), and being cheaper would be an advantage, not a disadvantage.
- [ ] Advantage: they hold their full capacity forever. Disadvantage: they cannot be reused
    - *why wrong:* Rechargeable batteries lose some capacity over time and CAN be reused — that reuse is their main advantage.
- [ ] Advantage: they produce no chemicals. Disadvantage: they give a lower voltage
    - *why wrong:* They still rely on chemical reactions, and the trade-off is upfront cost and ageing, not voltage.


---

## Fuel Cells  ·  `fuel-cells`  ·  AQA 4.5.2.2

> 🚩 **Triple-depth call (your review):** TRIPLE-ONLY page (hydrogen fuel cells are not in Combined Science), so it exists only in the two Triple files. Difficulty follows the tier: Triple-Foundation is recall and simple advantage/disadvantage reasoning; Triple-Higher adds the balanced overall equation, the electron-transfer (oxidation) idea at the electrode, and an evaluation against rechargeable batteries. Shared 8-question core + 4 tier-appropriate extras each.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often think a hydrogen fuel cell is just a kind of battery that eventually runs flat, and that it releases carbon dioxide like burning a fuel. Both are wrong. A fuel cell does not store its reactants and run down — it is continuously supplied with hydrogen and oxygen, so it keeps working as long as the fuel is provided. And the only product of a hydrogen fuel cell is WATER; no carbon dioxide is made at the point of use, because there is no carbon in the reaction.

**Question sets by tier** (each item shows tiers it appears in; ⭐ = full-review flag):

### Triple Foundation — 12 questions (4 recall / 8 apply+reason+calc)

**Q1. [recall · TFTH]** State the only product formed when a hydrogen fuel cell operates.
- [✔︎] Water
- [ ] Carbon dioxide
    - *why wrong:* There is no carbon in the reaction, so no CO₂ is made; the only product is water.
- [ ] Hydrogen
    - *why wrong:* Hydrogen is a reactant (the fuel), not a product; the product is water.
- [ ] Oxygen and carbon dioxide
    - *why wrong:* Oxygen is a reactant and no CO₂ is produced; the only product is water.

**Q2. [recall · TFTH]** State the overall reaction that takes place in a hydrogen fuel cell, in words.
- [✔︎] Hydrogen + oxygen → water
- [ ] Hydrogen + carbon → carbon dioxide
    - *why wrong:* A hydrogen fuel cell uses oxygen, not carbon, and makes water, not CO₂.
- [ ] Water → hydrogen + oxygen
    - *why wrong:* That is the reverse process (electrolysis of water); a fuel cell combines hydrogen and oxygen to make water.
- [ ] Hydrogen + oxygen → hydrogen peroxide
    - *why wrong:* The product is water (H₂O), not hydrogen peroxide (H₂O₂).

**Q3. [reason · TFTH]** Explain why a hydrogen fuel cell can keep producing electricity for as long as it is needed, unlike an ordinary battery.
- [✔︎] A fuel cell is continuously supplied with hydrogen and oxygen from outside, so its reactants do not run out the way a battery's fixed store of chemicals does
- [ ] A fuel cell recharges itself from the mains as it runs
    - *why wrong:* It is not recharged from the mains; it keeps working because fuel is continuously supplied.
- [ ] A fuel cell contains an unlimited store of chemicals sealed inside
    - *why wrong:* The reactants are supplied from OUTSIDE continuously; they are not an unlimited internal store.
- [ ] A fuel cell does not use up any reactants at all
    - *why wrong:* It does use up hydrogen and oxygen, but they are continuously replaced, so it does not run down.

**Q4. [apply · TFTH]** Suggest one advantage of using a hydrogen fuel cell instead of a petrol engine in a vehicle.
- [✔︎] The only product is water, so there are no carbon dioxide or other polluting emissions at the point of use
- [ ] It produces carbon dioxide more cleanly than petrol does
    - *why wrong:* A hydrogen fuel cell produces NO carbon dioxide at all — only water.
- [ ] The hydrogen is completely free to produce
    - *why wrong:* Producing hydrogen costs energy and money; the real advantage is that only water is emitted.
- [ ] It never needs any fuel to be supplied
    - *why wrong:* It does need a supply of hydrogen; the advantage is that it emits only water.

**Q5. [apply · TFTH]** Suggest one disadvantage of hydrogen fuel cells that limits their everyday use in cars.
- [✔︎] Hydrogen is difficult and potentially dangerous to store and transport (very flammable and low density), and there are few refuelling stations
- [ ] They release large amounts of carbon dioxide
    - *why wrong:* Fuel cells release only water, not CO₂; the real problems are hydrogen storage and supply.
- [ ] They can only ever be used once and then thrown away
    - *why wrong:* A fuel cell works continuously while fuelled; the difficulty is storing and supplying the hydrogen.
- [ ] They produce a poisonous gas as they run
    - *why wrong:* The only product is water; the challenges are hydrogen storage, cost and refuelling infrastructure.

**Q6. [reason · TFTH]** Describe how a hydrogen fuel cell differs from simply burning hydrogen as a fuel.
- [✔︎] In a fuel cell the reaction produces electrical energy directly (and more efficiently), whereas burning hydrogen releases the energy as heat and light; both make only water
- [ ] Burning hydrogen makes water but a fuel cell makes carbon dioxide
    - *why wrong:* Neither makes CO₂ (no carbon is involved); the difference is that a fuel cell produces electricity directly.
- [ ] A fuel cell burns the hydrogen with a flame inside it
    - *why wrong:* A fuel cell does not burn the hydrogen; it converts the reaction's energy into electricity electrochemically.
- [ ] There is no difference — they are exactly the same process
    - *why wrong:* They differ: a fuel cell produces electricity directly and efficiently, while burning releases heat and light.

**Q7. [reason · TFTH]** Explain why hydrogen fuel cells are described as environmentally friendly at the point of use.
- [✔︎] They emit only water at the point of use, releasing no carbon dioxide or other pollutants, unlike fossil-fuel engines which release CO₂ and other gases
- [ ] They use no energy at all to run
    - *why wrong:* They do use energy (from hydrogen); the environmental point is that only water is emitted at the point of use.
- [ ] They remove carbon dioxide from the air as they run
    - *why wrong:* They do not remove CO₂; they simply do not produce any, emitting only water.
- [ ] They are silent, which stops all air pollution
    - *why wrong:* Being quiet reduces noise, not air pollution; the clean point is that only water is emitted.

**Q8. [apply · TFTH]** Suggest why a hydrogen fuel cell may not be as environmentally friendly overall as it first appears.
- [✔︎] The hydrogen itself is often produced from fossil fuels (such as natural gas) or by electrolysis using electricity, which can release carbon dioxide elsewhere
- [ ] The fuel cell releases carbon dioxide while it runs
    - *why wrong:* The fuel cell itself releases only water; the emissions come from PRODUCING the hydrogen, not from running the cell.
- [ ] Water is a harmful pollutant
    - *why wrong:* Water is harmless; the environmental catch is how the hydrogen is made.
- [ ] Fuel cells always use more petrol than a normal engine
    - *why wrong:* Fuel cells do not use petrol; the concern is the energy and fossil fuels used to make the hydrogen.

**Q9. [recall · TF]** State the two substances that must be supplied to a hydrogen fuel cell for it to work.
- [✔︎] Hydrogen and oxygen
- [ ] Hydrogen and carbon dioxide
    - *why wrong:* The reactants are hydrogen and oxygen; CO₂ is not involved.
- [ ] Water and oxygen
    - *why wrong:* Water is the product, not a reactant; hydrogen and oxygen are supplied.
- [ ] Petrol and air
    - *why wrong:* A hydrogen fuel cell runs on hydrogen and oxygen, not petrol.

**Q10. [recall · TF]** State one advantage and one disadvantage of hydrogen fuel cells.
- [✔︎] Advantage: only water is produced (no pollutants at the point of use). Disadvantage: hydrogen is hard to store and transport
- [ ] Advantage: they produce carbon dioxide. Disadvantage: they are silent
    - *why wrong:* They produce water, not CO₂ (which would not be an advantage), and being silent is not a disadvantage.
- [ ] Advantage: hydrogen is free. Disadvantage: they emit smoke
    - *why wrong:* Hydrogen is not free to produce, and fuel cells emit only water, no smoke.
- [ ] Advantage: they never stop. Disadvantage: they make water
    - *why wrong:* They do need fuel supplied, and making water is a benefit, not a disadvantage.

**Q11. [apply · TF]** Suggest why hydrogen fuel cells are being considered for buses and cars in cities.
- [✔︎] They emit only water at the point of use, so they do not add carbon dioxide or pollutants to city air
- [ ] They make the streets cleaner by producing carbon dioxide
    - *why wrong:* They produce no CO₂; they help by emitting only water instead of pollutants.
- [ ] They are the cheapest possible way to power a vehicle
    - *why wrong:* Cost is a challenge, not the reason; the appeal is clean emissions in cities.
- [ ] They run without needing any fuel supply in a city
    - *why wrong:* They still need hydrogen; the appeal is that only water is emitted where people live.

**Q12. [apply · TF]** A car maker calls its hydrogen car 'zero emission'. Suggest whether this is completely true, giving a reason.
- [✔︎] It is true at the point of use (only water is emitted), but not necessarily overall, because making the hydrogen can release carbon dioxide elsewhere
- [ ] It is completely true because hydrogen never causes any emissions anywhere
    - *why wrong:* Producing the hydrogen can release CO₂; 'zero emission' is only true at the point of use.
- [ ] It is completely false because the car emits carbon dioxide as it drives
    - *why wrong:* The car itself emits only water; any emissions come from making the hydrogen, not from driving.
- [ ] It is false because the water vapour it emits is a dangerous pollutant
    - *why wrong:* Water is not a dangerous pollutant; the caveat is emissions from producing the hydrogen.

### Triple Higher — 12 questions (2 recall / 10 apply+reason+calc)

**Q1. [recall · TFTH]** State the only product formed when a hydrogen fuel cell operates.
- [✔︎] Water
- [ ] Carbon dioxide
    - *why wrong:* There is no carbon in the reaction, so no CO₂ is made; the only product is water.
- [ ] Hydrogen
    - *why wrong:* Hydrogen is a reactant (the fuel), not a product; the product is water.
- [ ] Oxygen and carbon dioxide
    - *why wrong:* Oxygen is a reactant and no CO₂ is produced; the only product is water.

**Q2. [recall · TFTH]** State the overall reaction that takes place in a hydrogen fuel cell, in words.
- [✔︎] Hydrogen + oxygen → water
- [ ] Hydrogen + carbon → carbon dioxide
    - *why wrong:* A hydrogen fuel cell uses oxygen, not carbon, and makes water, not CO₂.
- [ ] Water → hydrogen + oxygen
    - *why wrong:* That is the reverse process (electrolysis of water); a fuel cell combines hydrogen and oxygen to make water.
- [ ] Hydrogen + oxygen → hydrogen peroxide
    - *why wrong:* The product is water (H₂O), not hydrogen peroxide (H₂O₂).

**Q3. [reason · TFTH]** Explain why a hydrogen fuel cell can keep producing electricity for as long as it is needed, unlike an ordinary battery.
- [✔︎] A fuel cell is continuously supplied with hydrogen and oxygen from outside, so its reactants do not run out the way a battery's fixed store of chemicals does
- [ ] A fuel cell recharges itself from the mains as it runs
    - *why wrong:* It is not recharged from the mains; it keeps working because fuel is continuously supplied.
- [ ] A fuel cell contains an unlimited store of chemicals sealed inside
    - *why wrong:* The reactants are supplied from OUTSIDE continuously; they are not an unlimited internal store.
- [ ] A fuel cell does not use up any reactants at all
    - *why wrong:* It does use up hydrogen and oxygen, but they are continuously replaced, so it does not run down.

**Q4. [apply · TFTH]** Suggest one advantage of using a hydrogen fuel cell instead of a petrol engine in a vehicle.
- [✔︎] The only product is water, so there are no carbon dioxide or other polluting emissions at the point of use
- [ ] It produces carbon dioxide more cleanly than petrol does
    - *why wrong:* A hydrogen fuel cell produces NO carbon dioxide at all — only water.
- [ ] The hydrogen is completely free to produce
    - *why wrong:* Producing hydrogen costs energy and money; the real advantage is that only water is emitted.
- [ ] It never needs any fuel to be supplied
    - *why wrong:* It does need a supply of hydrogen; the advantage is that it emits only water.

**Q5. [apply · TFTH]** Suggest one disadvantage of hydrogen fuel cells that limits their everyday use in cars.
- [✔︎] Hydrogen is difficult and potentially dangerous to store and transport (very flammable and low density), and there are few refuelling stations
- [ ] They release large amounts of carbon dioxide
    - *why wrong:* Fuel cells release only water, not CO₂; the real problems are hydrogen storage and supply.
- [ ] They can only ever be used once and then thrown away
    - *why wrong:* A fuel cell works continuously while fuelled; the difficulty is storing and supplying the hydrogen.
- [ ] They produce a poisonous gas as they run
    - *why wrong:* The only product is water; the challenges are hydrogen storage, cost and refuelling infrastructure.

**Q6. [reason · TFTH]** Describe how a hydrogen fuel cell differs from simply burning hydrogen as a fuel.
- [✔︎] In a fuel cell the reaction produces electrical energy directly (and more efficiently), whereas burning hydrogen releases the energy as heat and light; both make only water
- [ ] Burning hydrogen makes water but a fuel cell makes carbon dioxide
    - *why wrong:* Neither makes CO₂ (no carbon is involved); the difference is that a fuel cell produces electricity directly.
- [ ] A fuel cell burns the hydrogen with a flame inside it
    - *why wrong:* A fuel cell does not burn the hydrogen; it converts the reaction's energy into electricity electrochemically.
- [ ] There is no difference — they are exactly the same process
    - *why wrong:* They differ: a fuel cell produces electricity directly and efficiently, while burning releases heat and light.

**Q7. [reason · TFTH]** Explain why hydrogen fuel cells are described as environmentally friendly at the point of use.
- [✔︎] They emit only water at the point of use, releasing no carbon dioxide or other pollutants, unlike fossil-fuel engines which release CO₂ and other gases
- [ ] They use no energy at all to run
    - *why wrong:* They do use energy (from hydrogen); the environmental point is that only water is emitted at the point of use.
- [ ] They remove carbon dioxide from the air as they run
    - *why wrong:* They do not remove CO₂; they simply do not produce any, emitting only water.
- [ ] They are silent, which stops all air pollution
    - *why wrong:* Being quiet reduces noise, not air pollution; the clean point is that only water is emitted.

**Q8. [apply · TFTH]** Suggest why a hydrogen fuel cell may not be as environmentally friendly overall as it first appears.
- [✔︎] The hydrogen itself is often produced from fossil fuels (such as natural gas) or by electrolysis using electricity, which can release carbon dioxide elsewhere
- [ ] The fuel cell releases carbon dioxide while it runs
    - *why wrong:* The fuel cell itself releases only water; the emissions come from PRODUCING the hydrogen, not from running the cell.
- [ ] Water is a harmful pollutant
    - *why wrong:* Water is harmless; the environmental catch is how the hydrogen is made.
- [ ] Fuel cells always use more petrol than a normal engine
    - *why wrong:* Fuel cells do not use petrol; the concern is the energy and fossil fuels used to make the hydrogen.

**Q9. [reason · TH]** Write the balanced overall equation for the reaction in a hydrogen fuel cell, and state what it shows about the products.
- [✔︎] 2H₂ + O₂ → 2H₂O — the only product is water, and no carbon-containing gases are formed
- [ ] 2H₂ + O₂ → 2H₂O₂ — the product is hydrogen peroxide
    - *why wrong:* The product is water (H₂O), not hydrogen peroxide (H₂O₂).
- [ ] H₂ + O₂ → H₂O — the equation is already balanced
    - *why wrong:* This is not balanced (the oxygen and hydrogen do not balance); the correct equation is 2H₂ + O₂ → 2H₂O.
- [ ] CH₄ + 2O₂ → CO₂ + 2H₂O — the products are carbon dioxide and water
    - *why wrong:* That is the combustion of methane; a hydrogen fuel cell uses hydrogen and makes only water.

**Q10. [reason · TH]** At the negative electrode of a hydrogen fuel cell, hydrogen is oxidised. Deduce what 'oxidised' means here in terms of electrons.
- [✔︎] The hydrogen loses electrons (oxidation is loss of electrons), and these flow through the external circuit as the current
- [ ] The hydrogen gains electrons from the circuit
    - *why wrong:* Oxidation is LOSS of electrons; hydrogen at the negative electrode loses electrons (gaining them would be reduction).
- [ ] The hydrogen simply reacts with oxygen at that electrode
    - *why wrong:* Oxidation here means losing electrons; at the negative electrode the hydrogen loses electrons, which then travel round the circuit.
- [ ] The hydrogen gains oxygen atoms directly
    - *why wrong:* In this electron-transfer sense, oxidation means loss of electrons, not gaining oxygen atoms.

**Q11. [apply · TH]** Evaluate the use of a hydrogen fuel cell compared with a rechargeable battery for powering a long-distance vehicle.
- [✔︎] A fuel cell can be refuelled quickly and gives a long range for its weight, but needs a hydrogen supply and storage; a battery recharges easily from electricity but is heavy and slow to charge — so a fuel cell can suit long distances where hydrogen is available
- [ ] A battery is always better because a fuel cell produces carbon dioxide
    - *why wrong:* A fuel cell produces only water, not CO₂; the real trade-offs are refuelling speed, range, weight and hydrogen supply.
- [ ] A fuel cell is always worse because it must be recharged from the mains
    - *why wrong:* A fuel cell is refuelled with hydrogen, not recharged from the mains; that quick refuelling is one of its advantages.
- [ ] There is no difference between the two for a vehicle
    - *why wrong:* They differ in refuelling method, range, weight and infrastructure, so the best choice depends on the use.

**Q12. [reason · TH]** Explain why hydrogen fuel cells are often described as more efficient than burning hydrogen in an engine.
- [✔︎] A fuel cell converts the energy of the reaction directly into electrical energy, so less energy is wasted as heat than in an engine that burns the fuel first
- [ ] Burning hydrogen produces no heat, so it wastes more energy
    - *why wrong:* Burning hydrogen releases a lot of heat, much of which is wasted; a fuel cell avoids this by making electricity directly.
- [ ] A fuel cell produces more hydrogen than it uses
    - *why wrong:* A fuel cell cannot make more fuel than it uses; its efficiency comes from converting energy directly into electricity.
- [ ] An engine turns all of its heat into motion with no waste
    - *why wrong:* Engines waste a large fraction of the energy as heat; that inefficiency is why fuel cells can be more efficient.


---
