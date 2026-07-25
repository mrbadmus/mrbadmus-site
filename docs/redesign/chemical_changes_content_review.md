# Chemical Changes unit — content review (MRB-105)

_AQA 5.4 Chemical Changes. Drafted for Mide's review before the Phase 2 merge. Every question, its options (✔︎ = correct) and a diagnostic line for each wrong option are shown here — you never need to read the Python. This unit is mostly conceptual (reactivity, extraction, redox, acids, salts, the pH scale, electrolysis) with two genuine-calculation pages (titrations and half equations) that carry FIFA._

## How the tiers work (the difficulty model you set)

- **Difficulty follows the tier, not the pathway.** Combined-Foundation and Triple-Foundation are the **same difficulty**; Combined-Higher and Triple-Higher both **scale up** to genuine Higher demand.
- **Triple's extra is coverage, not a harder version of the same content.** Triple-Foundation = the exact Combined-Foundation set **+ 2 extra Foundation-level questions**; Triple-Higher = the exact Combined-Higher set **+ 2 extra Higher/depth questions**. So Foundation students see the same difficulty on both pathways, and Triple students simply get more.
- **Foundation and Higher are genuinely different question sets** — not the same questions with a harder badge. Higher uses exam command words, keeps recall under 30%, and adds the electron-level reasoning (OIL RIG, half equations) and calculations that Foundation does not carry.
- **Every wrong option carries a diagnostic** naming the misconception or error, so a student learns *which* mistake they made.
- **Counts:** Combined 10 / tier, Triple 12 / tier. Cell presence varies by page (detected from the four data files): **Strong & Weak Acids** and **Half Equations** are **Higher-only** (no Foundation); **Titrations** is **Triple-only** (no Combined).

- **FIFA is a menu, not a mandate.** It appears only on the two pages with real step-by-step calculation — **Titrations** (mean titre / concentration) and **Half Equations** (balancing). The descriptive pages (reactivity series, salts, electrolysis products, etc.) are exam-register questions, not step-throughs, so they carry no FIFA by design.

### ⭐ Full-review checklist (per the review-tiering rule)

All calculation / half-equation-derivation items and all FIFA are flagged ⭐ for your full review; recall/comprehension items are left for your sampling. The ⭐ items are:

- **Oxidation and Reduction** — 2 calc/derivation item(s)
- **The pH Scale and Neutralisation** — 3 calc/derivation item(s)
- **Strong and Weak Acids** — 2 calc/derivation item(s)
- **Titrations** — 11 calc/derivation item(s), FIFA worked examples (TF + TH)
- **Electrolysis of Molten Ionic Compounds** — 4 calc/derivation item(s)
- **Using Electrolysis to Extract Metals** — 4 calc/derivation item(s)
- **Electrolysis of Aqueous Solutions** — 4 calc/derivation item(s)
- **Half Equations for Electrode Reactions** — 12 calc/derivation item(s), FIFA worked examples (CH + TH)

### Audit status (self-checked with `audit_content.py`)

- **Before:** every one of the 13 pages carried only **2 questions**, identical across all tiers — across the unit that was **46 count-criticals** (2 < the floor of 5), **46 mistake-first majors** (every Common Mistake opened with correct info, not a student mistake), **21 tier-integrity majors** (Higher = Foundation verbatim) and **22 triple-depth majors** (Triple = Combined verbatim), plus register minors.
- **After:** **zero critical, zero content majors, zero minors.** The only remaining flags are **(a)** 4 systemic `no interactive practice mode` **majors** — one per FIFA cell (Titrations TF+TH, Half Equations CH+TH). The current template renders static FIFA steps only; the interactive practice mode is the redesign port's job (**MRB-113**), **not** a content defect. And **(b)** 34 `info` notes on descriptive pages that keep their chemical equations but carry no FIFA — expected, since those pages have no calculation.

---

## Reactivity of Metals and Metal Oxides  ·  `reactivity-series`  ·  AQA 5.4.1.1–5.4.1.2

> 🚩 **Triple-depth call (your review):** MATCHED — this AQA sub-topic is identical for Combined and Triple. Foundation difficulty is the same across both pathways; each Triple set = the Combined set + extra same-difficulty coverage. No AQA Triple-only content on this page.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often get the direction of displacement the wrong way round — they see iron and copper sulfate and write that copper displaces the iron. It is always the MORE reactive metal that pushes the less reactive one out of its compound, never the reverse. So iron (more reactive) displaces copper from copper sulfate; copper cannot displace iron from iron sulfate because copper sits below iron in the reactivity series.

### Combined Foundation — 10 questions

_These 10 also appear verbatim in Triple Foundation._

**Q1. [recall]** State what the reactivity series of metals shows.
- [✔︎] A list of metals in order of how reactive they are, from most reactive to least reactive
- [ ] A list of metals in order of their density
    - *why wrong:* The series orders metals by reactivity, not density — lead is dense but not very reactive.
- [ ] A list of metals in order of when they were discovered
    - *why wrong:* Discovery date is a rough consequence of reactivity, not what the series measures directly.
- [ ] A list of metals in order of their melting points
    - *why wrong:* Melting point is a physical property unrelated to the reactivity order.

**Q2. [apply]** A piece of magnesium is placed in blue copper(II) sulfate solution. Predict what you would observe.
- [✔︎] The magnesium becomes coated in reddish-brown copper and the blue colour fades
- [ ] No change — magnesium is too stable to react
    - *why wrong:* Magnesium is MORE reactive than copper, so it displaces it — a reaction does happen.
- [ ] The magnesium becomes coated in a silvery layer and the solution stays blue
    - *why wrong:* The displaced metal is copper (reddish-brown), not silvery, and the blue fades as Cu²⁺ leaves solution.
- [ ] The solution turns from colourless to blue
    - *why wrong:* The solution is already blue; as copper is displaced the blue actually fades.

**Q3. [apply]** Predict whether copper will react when placed in magnesium sulfate solution.
- [✔︎] No reaction — copper is less reactive than magnesium, so it cannot displace it
- [ ] Yes — copper displaces the magnesium because copper is a metal
    - *why wrong:* Being a metal is not enough; copper is BELOW magnesium, so it cannot displace it.
- [ ] Yes — the copper dissolves and magnesium metal forms
    - *why wrong:* That would need copper to be more reactive than magnesium, which it is not.
- [ ] Yes — a gas is given off
    - *why wrong:* No reaction occurs at all, so no gas is produced.

**Q4. [apply]** Metal X fizzes slowly in dilute acid; metal Y fizzes vigorously. Deduce which metal is more reactive.
- [✔︎] Metal Y — the more vigorous the reaction with acid, the more reactive the metal
- [ ] Metal X — slower bubbling means the reaction lasts longer so it is more reactive
    - *why wrong:* Rate, not duration, indicates reactivity; vigorous fizzing means MORE reactive.
- [ ] They are equally reactive because both produce bubbles
    - *why wrong:* Both react, but the rate differs, so their reactivities are not equal.
- [ ] Neither — fizzing shows the metals are unreactive
    - *why wrong:* Fizzing (hydrogen gas) is exactly the sign of a reactive metal reacting with acid.

**Q5. [recall]** Name the two products formed when a reactive metal reacts with a dilute acid.
- [✔︎] A salt and hydrogen
- [ ] A salt and water
    - *why wrong:* Salt + water is the product of an acid with a metal OXIDE or hydroxide, not with the metal itself.
- [ ] A salt, water and carbon dioxide
    - *why wrong:* That set of products comes from an acid reacting with a metal CARBONATE.
- [ ] A metal oxide and hydrogen
    - *why wrong:* The metal forms a salt (dissolved in solution), not a metal oxide, when it reacts with acid.

**Q6. [apply]** Using the reactivity series, place potassium, iron and copper in order from most to least reactive.
- [✔︎] Potassium, iron, copper
- [ ] Copper, iron, potassium
    - *why wrong:* This is reversed — potassium is one of the most reactive metals, copper one of the least.
- [ ] Iron, potassium, copper
    - *why wrong:* Potassium is far more reactive than iron, so it must come first.
- [ ] Potassium, copper, iron
    - *why wrong:* Iron is more reactive than copper, so iron comes before copper.

**Q7. [reason]** Explain why gold is found in the Earth as the pure metal rather than as a compound.
- [✔︎] Gold is very unreactive, so it does not react with oxygen, water or other substances to form compounds
- [ ] Gold is so dense that it sinks to where no chemicals can reach it
    - *why wrong:* Density does not stop chemical reactions; gold stays as the element because it is unreactive.
- [ ] Gold melts easily and separates from its compounds naturally
    - *why wrong:* Melting point is irrelevant; gold is uncombined because it does not react to form compounds.
- [ ] Gold reacts so quickly that it immediately turns back into the metal
    - *why wrong:* Unreactive metals do not react at all — the opposite of reacting quickly.

**Q8. [apply]** When magnesium is heated in air it burns brightly. Name the product formed.
- [✔︎] Magnesium oxide
- [ ] Magnesium hydroxide
    - *why wrong:* Hydroxide forms when magnesium reacts with water, not when it burns in oxygen.
- [ ] Magnesium carbonate
    - *why wrong:* Carbonate would need carbon dioxide; burning in air combines magnesium with oxygen.
- [ ] Magnesium chloride
    - *why wrong:* Chloride would need chlorine or hydrochloric acid, not oxygen from the air.

**Q9. [apply]** In which pair will a displacement reaction occur when the metal is added to the solution?
- [✔︎] Zinc added to copper(II) sulfate solution
- [ ] Copper added to zinc sulfate solution
    - *why wrong:* Copper is less reactive than zinc, so it cannot displace it — no reaction.
- [ ] Silver added to copper(II) sulfate solution
    - *why wrong:* Silver is less reactive than copper, so it cannot displace copper.
- [ ] Copper added to iron(II) sulfate solution
    - *why wrong:* Copper is less reactive than iron, so no displacement happens.

**Q10. [apply]** Which metal could be used to displace iron from iron(II) sulfate solution?
- [✔︎] Zinc, because it is more reactive than iron
- [ ] Copper, because it is a good conductor
    - *why wrong:* Conductivity is irrelevant; copper is less reactive than iron so cannot displace it.
- [ ] Silver, because it is a precious metal
    - *why wrong:* Silver is far less reactive than iron and cannot displace it.
- [ ] Gold, because it is very stable
    - *why wrong:* Gold is the least reactive of these and cannot displace iron.

### Triple Foundation — 2 extra Foundation-level questions

_On top of the 10 above (so Triple Foundation shows 12)._

**Q11. [recall]** Name a metal that reacts vigorously with cold water.
- [✔︎] Potassium
- [ ] Copper
    - *why wrong:* Copper does not react with cold water at all — it is low in the reactivity series.
- [ ] Iron
    - *why wrong:* Iron reacts only very slowly with water (rusting), not vigorously.
- [ ] Gold
    - *why wrong:* Gold is unreactive and does not react with water.

**Q12. [apply]** Magnesium is added to dilute hydrochloric acid and a gas is collected. Identify the gas and the test for it.
- [✔︎] Hydrogen — it makes a squeaky pop with a lit splint
- [ ] Carbon dioxide — it turns limewater cloudy
    - *why wrong:* Metal + acid gives hydrogen; carbon dioxide comes from carbonates, not metals.
- [ ] Oxygen — it relights a glowing splint
    - *why wrong:* Metal + acid produces hydrogen, not oxygen.
- [ ] Chlorine — it bleaches damp litmus paper
    - *why wrong:* The chloride stays in solution as the salt; the gas released is hydrogen.

### Combined Higher — 10 questions

_A different, harder set from Foundation. These 10 also appear verbatim in Triple Higher._

**Q1. [reason]** Explain what makes one metal more reactive than another.
- [✔︎] The more easily a metal atom loses its outer electrons to form a positive ion, the more reactive it is
- [ ] The heavier the metal atom, the more reactive it is
    - *why wrong:* Reactivity depends on tendency to lose electrons, not on atomic mass — gold is heavy but unreactive.
- [ ] The more electrons a metal gains, the more reactive it is
    - *why wrong:* Metals LOSE electrons to form positive ions; they do not gain them.
- [ ] The harder the metal, the more reactive it is
    - *why wrong:* Hardness is a physical property with no link to how readily electrons are lost.

**Q2. [apply]** A metal reacts slowly with cold water and vigorously with dilute acid. A second metal reacts with neither. Deduce the more reactive metal and justify it.
- [✔︎] The first metal — reacting with water and acid shows it is higher in the reactivity series
- [ ] The second metal, because it is more stable
    - *why wrong:* Being unreactive means LOWER in the series, so the second metal is less reactive.
- [ ] They are equally reactive because both are metals
    - *why wrong:* Their reactions differ markedly, so their reactivities are not equal.
- [ ] Cannot be decided without their densities
    - *why wrong:* Reactivity is judged from reactions, not density — the reactions already tell us.

**Q3. [reason]** In terms of electrons, explain why a more reactive metal displaces a less reactive one from its salt solution.
- [✔︎] The more reactive metal loses electrons more readily, so it gives electrons to the less reactive metal's ions, which are then deposited as metal
- [ ] The more reactive metal is denser, so it pushes the other metal out
    - *why wrong:* Displacement is about electron transfer, not density.
- [ ] The less reactive metal gives its electrons to the more reactive metal
    - *why wrong:* It is the more reactive metal that loses electrons; the less reactive ions gain them.
- [ ] The two metals swap protons in their nuclei
    - *why wrong:* Nuclei are unchanged; only outer electrons are transferred.

**Q4. [apply]** Iron filings are added to copper(II) sulfate solution. Identify the salt formed in solution.
- [✔︎] Iron(II) sulfate
- [ ] Copper(II) sulfate remains unchanged
    - *why wrong:* Iron displaces the copper, so the copper sulfate is converted to iron sulfate.
- [ ] Iron(II) oxide
    - *why wrong:* No oxide forms in a displacement in solution; the sulfate ion stays in solution with the iron.
- [ ] Copper(II) oxide
    - *why wrong:* Copper is displaced as the metal, not as an oxide.

**Q5. [reason]** Explain why copper does not react with dilute hydrochloric acid.
- [✔︎] Copper is less reactive than hydrogen, so it cannot displace hydrogen from the acid
- [ ] Copper is a transition metal, so it never reacts
    - *why wrong:* Transition metals can react; copper's lack of reaction is because it is below hydrogen in reactivity.
- [ ] Copper reacts but the reaction is invisible
    - *why wrong:* There genuinely is no reaction — copper cannot displace hydrogen from acid.
- [ ] The acid is too dilute for any metal to react
    - *why wrong:* More reactive metals such as magnesium react readily with the same dilute acid.

**Q6. [apply]** An unknown metal displaces lead but not iron from their salt solutions. Deduce its position relative to lead and iron.
- [✔︎] More reactive than lead but less reactive than iron
- [ ] More reactive than both lead and iron
    - *why wrong:* If it were above iron it would displace iron too, but it does not.
- [ ] Less reactive than both lead and iron
    - *why wrong:* If it were below lead it could not displace lead, but it does.
- [ ] Equally reactive to lead
    - *why wrong:* Displacing lead shows it is more reactive than lead, not equal to it.

**Q7. [reason]** Explain why reactive metals such as potassium were isolated only after electricity became available in the 1800s.
- [✔︎] They are too reactive to be extracted by heating with carbon, so they need electrolysis, which requires an electric current
- [ ] They are rare, so there was not enough ore until then
    - *why wrong:* Reactive metals such as sodium and potassium are common; the barrier was the extraction method, not supply.
- [ ] They only form compounds at high temperatures reached later
    - *why wrong:* Their compounds form readily; the difficulty is splitting those compounds, which needs electrolysis.
- [ ] They were hidden deep underground until mining improved
    - *why wrong:* The limiting factor was chemistry (electrolysis), not the depth of the ore.

**Q8. [apply]** In the displacement Mg + ZnSO₄ → MgSO₄ + Zn, identify the reducing agent.
- [✔︎] Magnesium — it donates electrons to the zinc ions
- [ ] Zinc — it gains electrons
    - *why wrong:* Gaining electrons makes zinc the species reduced; the reducing agent is the one that DONATES electrons.
- [ ] The sulfate ion — it carries the charge
    - *why wrong:* Sulfate is a spectator ion and takes no part in the electron transfer.
- [ ] Water — it acts as the solvent
    - *why wrong:* Water is only the solvent here; magnesium is the electron donor.

**Q9. [recall]** State the name given to a reaction in which a more reactive element takes the place of a less reactive one in a compound.
- [✔︎] A displacement reaction
- [ ] A neutralisation reaction
    - *why wrong:* Neutralisation is the reaction of an acid with a base, not metal-for-metal replacement.
- [ ] A precipitation reaction
    - *why wrong:* Precipitation forms an insoluble solid from two solutions; displacement swaps a metal for a metal.
- [ ] A combustion reaction
    - *why wrong:* Combustion is burning in oxygen, not the replacement of one metal by another.

**Q10. [apply]** Predict whether silver will react when added to magnesium nitrate solution, and justify your answer.
- [✔︎] No reaction — silver is less reactive than magnesium, so it cannot displace it
- [ ] Yes — silver displaces magnesium and a grey solid forms
    - *why wrong:* Silver is below magnesium, so it cannot displace it; no solid forms.
- [ ] Yes — silver nitrate and magnesium metal form
    - *why wrong:* That needs silver to be more reactive than magnesium, which it is not.
- [ ] Yes — hydrogen gas is released
    - *why wrong:* No reaction occurs, and in any case this is a salt solution, not an acid.

### Triple Higher — 2 extra Higher/depth questions

_On top of the 10 above (so Triple Higher shows 12)._

**Q11. [reason]** In the reaction Zn + CuSO₄ → ZnSO₄ + Cu, deduce which metal is oxidised.
- [✔︎] Zinc — it loses electrons to form Zn²⁺ ions
- [ ] Copper — it loses electrons as it comes out of solution
    - *why wrong:* Copper ions GAIN electrons to become copper metal, so copper is reduced, not oxidised.
- [ ] Neither — displacement reactions are not redox
    - *why wrong:* Displacement is a redox reaction: electrons pass from the more reactive metal to the less reactive metal ion.
- [ ] Both are oxidised because both change
    - *why wrong:* Only one species loses electrons (zinc); the copper ions gain them, so copper is reduced.

**Q12. [reason]** A table shows metal A displaces B and C, and B displaces C but not A. Deduce the order of reactivity, most reactive first.
- [✔︎] A, B, C
- [ ] C, B, A
    - *why wrong:* This is reversed — A displaces the others, so A is the MOST reactive, not the least.
- [ ] B, A, C
    - *why wrong:* A displaces B, so A must be above B, not below it.
- [ ] A, C, B
    - *why wrong:* B displaces C, so B is above C in reactivity.

---

## Extraction of Metals and Reduction  ·  `extraction-of-metals`  ·  AQA 5.4.1.3

> 🚩 **Triple-depth call (your review):** MATCHED — this AQA sub-topic is identical for Combined and Triple. Foundation difficulty is the same across both pathways; each Triple set = the Combined set + extra same-difficulty coverage. No AQA Triple-only content on this page.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often try to extract every metal by heating its ore with carbon, and so write that aluminium oxide is reduced by carbon. It cannot be. Carbon only works for metals BELOW carbon in the reactivity series (such as iron, zinc and copper), because carbon can take the oxygen from those oxides. Aluminium sits ABOVE carbon, so carbon cannot pull the oxygen off — aluminium must be extracted by electrolysis instead.

### Combined Foundation — 10 questions

_These 10 also appear verbatim in Triple Foundation._

**Q1. [recall]** State what is meant by an ore.
- [✔︎] A rock that contains enough of a metal or metal compound to make extracting the metal worthwhile
- [ ] Any rock that contains a metal in any amount
    - *why wrong:* It must contain ENOUGH metal to be worth extracting — otherwise it is not called an ore.
- [ ] A pure lump of metal found in the ground
    - *why wrong:* That is a native metal (like gold); an ore is a compound-bearing rock, not pure metal.
- [ ] A rock that has been heated to release its metal
    - *why wrong:* An ore is the raw rock before extraction, not the product of heating it.

**Q2. [apply]** Iron is below carbon in the reactivity series. Predict the method used to extract iron from iron oxide.
- [✔︎] Reduction by heating with carbon
- [ ] Electrolysis of the molten oxide
    - *why wrong:* Electrolysis is used for metals ABOVE carbon; iron is below carbon so carbon reduction works.
- [ ] Reacting the oxide with an acid
    - *why wrong:* Acids make salts, they do not extract the metal from its oxide.
- [ ] Simply filtering the metal out of the rock
    - *why wrong:* The metal is chemically combined as an oxide and must be reduced, not filtered.

**Q3. [apply]** Aluminium is above carbon in the reactivity series. Predict the method used to extract it.
- [✔︎] Electrolysis of the molten aluminium oxide
- [ ] Heating the oxide with carbon
    - *why wrong:* Aluminium is more reactive than carbon, so carbon cannot remove the oxygen — electrolysis is needed.
- [ ] Heating the oxide on its own
    - *why wrong:* Simply heating aluminium oxide does not break it down; electrolysis is required.
- [ ] Reacting it with hydrochloric acid
    - *why wrong:* That would make a salt, not extract aluminium metal.

**Q4. [recall]** Define reduction in terms of oxygen.
- [✔︎] The loss of oxygen from a substance
- [ ] The gain of oxygen by a substance
    - *why wrong:* That describes oxidation; reduction is the LOSS of oxygen.
- [ ] The gain of hydrogen by a substance
    - *why wrong:* In this topic reduction is defined by loss of oxygen, not gain of hydrogen.
- [ ] The loss of electrons from a substance
    - *why wrong:* Loss of electrons is oxidation; reduction in terms of electrons is a GAIN.

**Q5. [apply]** In the extraction reaction Fe₂O₃ + 3CO → 2Fe + 3CO₂, identify the substance that is reduced.
- [✔︎] Iron(III) oxide — it loses its oxygen to become iron
- [ ] Carbon monoxide — it loses oxygen
    - *why wrong:* Carbon monoxide GAINS oxygen (CO → CO₂), so it is oxidised, not reduced.
- [ ] Carbon dioxide — it is the product
    - *why wrong:* Carbon dioxide is the oxidised product of the reducing agent, not the substance reduced.
- [ ] Iron — it is the metal
    - *why wrong:* Iron is what is produced BY the reduction; the oxide is the thing reduced.

**Q6. [apply]** Which of these metals must be extracted by electrolysis rather than by carbon reduction?
- [✔︎] Aluminium
- [ ] Iron
    - *why wrong:* Iron is below carbon, so it is extracted by cheaper carbon reduction.
- [ ] Zinc
    - *why wrong:* Zinc is below carbon and is extracted by carbon reduction.
- [ ] Copper
    - *why wrong:* Copper is well below carbon, so carbon reduction (or other cheap methods) works.

**Q7. [reason]** Explain why extracting aluminium is more expensive than extracting iron.
- [✔︎] Aluminium needs electrolysis, which uses a large amount of electrical energy, whereas iron is reduced by cheaper carbon
- [ ] Aluminium ore is much rarer than iron ore
    - *why wrong:* Aluminium ore (bauxite) is abundant; the cost is the electrical energy for electrolysis.
- [ ] Aluminium has a much higher melting point than iron
    - *why wrong:* The main cost is the electricity for electrolysis, not melting point differences.
- [ ] Aluminium reacts with carbon to form a poison
    - *why wrong:* The reason carbon is not used is that it cannot reduce aluminium oxide at all, and electrolysis is costly.

**Q8. [recall]** Name the process used to extract zinc from zinc oxide.
- [✔︎] Heating with carbon (carbon reduction)
- [ ] Electrolysis of molten zinc oxide
    - *why wrong:* Zinc is below carbon, so the cheaper carbon reduction is used, not electrolysis.
- [ ] Reacting zinc oxide with water
    - *why wrong:* Zinc oxide does not react with water to give the metal.
- [ ] Distillation of the ore
    - *why wrong:* Distillation separates liquids by boiling point; it does not reduce an oxide.

**Q9. [apply]** In the reaction ZnO + C → Zn + CO₂, state the job that carbon does.
- [✔︎] It removes the oxygen from the zinc oxide — it is the reducing agent
- [ ] It adds oxygen to the zinc
    - *why wrong:* Carbon takes oxygen AWAY from zinc oxide; it does not add oxygen to zinc.
- [ ] It melts the zinc so it can be poured out
    - *why wrong:* Carbon reacts chemically to remove oxygen; it is not just a heat source.
- [ ] It colours the zinc so it can be seen
    - *why wrong:* Carbon's role is chemical reduction, not colouring.

**Q10. [reason]** Explain why gold can be found in the ground as the metal itself and needs no chemical extraction.
- [✔︎] Gold is so unreactive that it does not combine with oxygen or other elements to form compounds
- [ ] Gold is too valuable to leave combined with other elements
    - *why wrong:* Value has nothing to do with it; gold is uncombined because it is chemically unreactive.
- [ ] Gold decomposes any compound it forms
    - *why wrong:* Gold simply does not form compounds under normal conditions; it is not decomposing them.
- [ ] Gold is always found dissolved in underground water
    - *why wrong:* Gold is found as the solid metal, not dissolved, because it is unreactive.

### Triple Foundation — 2 extra Foundation-level questions

_On top of the 10 above (so Triple Foundation shows 12)._

**Q11. [recall]** State whether copper is extracted by carbon reduction or by electrolysis.
- [✔︎] Carbon reduction, because copper is below carbon in the reactivity series
- [ ] Electrolysis, because copper is above carbon
    - *why wrong:* Copper is well BELOW carbon, so carbon reduction works.
- [ ] Neither — copper is always found as the pure metal
    - *why wrong:* Some copper is found native, but most is extracted from copper compounds by reduction.
- [ ] By reacting it with acid
    - *why wrong:* Acid makes a copper salt, it does not extract copper from its ore.

**Q12. [apply]** Name the gas given off when iron oxide is reduced by carbon monoxide in the blast furnace.
- [✔︎] Carbon dioxide
- [ ] Hydrogen
    - *why wrong:* Hydrogen is produced by metal-acid reactions, not by the reduction of iron oxide with carbon monoxide.
- [ ] Oxygen
    - *why wrong:* The oxygen ends up combined in carbon dioxide, not released as oxygen gas.
- [ ] Carbon monoxide only
    - *why wrong:* Carbon monoxide is the reactant; it is oxidised to carbon dioxide, which is given off.

### Combined Higher — 10 questions

_A different, harder set from Foundation. These 10 also appear verbatim in Triple Higher._

**Q1. [reason]** Explain why a metal's position in the reactivity series decides how it is extracted.
- [✔︎] Metals below carbon can have their oxygen removed by carbon (reduction); metals above carbon are too reactive for this and need electrolysis
- [ ] More reactive metals are always found as pure metals, so need no extraction
    - *why wrong:* The opposite is true — reactive metals are strongly combined in compounds and are hardest to extract.
- [ ] Less reactive metals need electrolysis because they hold oxygen tightly
    - *why wrong:* It is the MORE reactive metals (above carbon) that hold oxygen tightly and need electrolysis.
- [ ] The position tells you the melting point, which sets the method
    - *why wrong:* Position reflects reactivity, not melting point; reactivity is what determines the method.

**Q2. [apply]** In the extraction 2Fe₂O₃ + 3C → 4Fe + 3CO₂, identify what is oxidised and what is reduced.
- [✔︎] Iron oxide is reduced (loses oxygen); carbon is oxidised (gains oxygen)
- [ ] Iron oxide is oxidised; carbon is reduced
    - *why wrong:* Iron oxide LOSES oxygen (reduced) and carbon GAINS oxygen (oxidised) — this is reversed.
- [ ] Both iron oxide and carbon are reduced
    - *why wrong:* Only iron oxide is reduced; carbon is oxidised, so both cannot be reduced.
- [ ] Neither is oxidised because carbon is an element
    - *why wrong:* An element can still be oxidised — here carbon gains oxygen to form CO₂.

**Q3. [reason]** Explain why carbon cannot be used to extract aluminium even though it would be far cheaper than electrolysis.
- [✔︎] Aluminium is more reactive than carbon, so carbon cannot take the oxygen away from aluminium oxide
- [ ] Carbon reacts with aluminium to form a dangerous alloy
    - *why wrong:* The real reason is that carbon cannot reduce aluminium oxide, not that a hazardous alloy forms.
- [ ] Aluminium oxide has too high a melting point for carbon to reach
    - *why wrong:* Even molten, aluminium oxide is not reduced by carbon because aluminium is above carbon in reactivity.
- [ ] Carbon is more expensive than electricity
    - *why wrong:* Carbon is cheaper; the reason it is not used is chemical, not cost.

**Q4. [apply]** A newly discovered metal sits between magnesium and zinc in the reactivity series. Predict how it is most likely extracted.
- [✔︎] By electrolysis, because it lies above carbon in the reactivity series
- [ ] By carbon reduction, because it lies below carbon
    - *why wrong:* Between magnesium and zinc still places it above carbon, so electrolysis is needed.
- [ ] It is found native and needs no extraction
    - *why wrong:* A metal that reactive is always combined in compounds, never found native.
- [ ] By heating the ore on its own
    - *why wrong:* Heating alone will not decompose the compound of such a reactive metal.

**Q5. [reason]** In terms of electrons, explain what 'reduction' means for the metal ions during the electrolysis of a molten ore.
- [✔︎] The metal ions gain electrons to become neutral metal atoms
- [ ] The metal ions lose electrons to become neutral atoms
    - *why wrong:* Losing electrons is oxidation; reduction is a GAIN of electrons.
- [ ] The metal atoms gain oxygen
    - *why wrong:* During electrolytic extraction the metal ions gain electrons; no oxygen is added to the metal.
- [ ] The metal ions gain neutrons
    - *why wrong:* Only electrons are transferred; the nucleus (protons and neutrons) is unchanged.

**Q6. [apply]** Copper can be extracted by heating copper oxide with carbon. Identify the reducing agent in this reaction.
- [✔︎] Carbon — it removes the oxygen from the copper oxide
- [ ] Copper oxide — it provides the oxygen
    - *why wrong:* The copper oxide is reduced; the reducing agent is the substance that removes its oxygen, i.e. carbon.
- [ ] Copper — it is the product
    - *why wrong:* Copper is produced by the reduction; it is not the reducing agent.
- [ ] Carbon dioxide — it carries the oxygen away
    - *why wrong:* Carbon dioxide is the product; the reducing agent that acted was carbon.

**Q7. [reason]** Explain why some copper is extracted using scrap iron rather than by heating with carbon.
- [✔︎] Iron is more reactive than copper, so it displaces copper from solutions of copper salts
- [ ] Iron is cheaper than copper oxide
    - *why wrong:* The reason is chemical — iron displaces copper because it is more reactive, not simply cost.
- [ ] Iron lowers the melting point of copper
    - *why wrong:* Displacement, not melting-point change, is why iron is used to obtain copper from solution.
- [ ] Iron is less reactive than copper so it protects it
    - *why wrong:* Iron is MORE reactive than copper, which is exactly why it can displace it.

**Q8. [apply]** Given the order K, Na, Ca, Mg, C, Zn, Fe, Cu, deduce which of zinc and calcium is extracted by electrolysis.
- [✔︎] Calcium, because it lies above carbon; zinc lies below carbon so uses carbon reduction
- [ ] Zinc, because it lies above carbon
    - *why wrong:* Zinc is below carbon in this list, so it uses carbon reduction.
- [ ] Both, because both are metals
    - *why wrong:* Only metals above carbon need electrolysis; zinc is below carbon.
- [ ] Neither, because both can be reduced by carbon
    - *why wrong:* Calcium is above carbon and cannot be reduced by carbon, so it needs electrolysis.

**Q9. [reason]** Explain why extracting metals by electrolysis has a larger environmental impact than carbon reduction.
- [✔︎] Electrolysis uses large amounts of electricity, which is often generated by burning fossil fuels, releasing carbon dioxide
- [ ] Electrolysis always releases toxic chlorine gas
    - *why wrong:* Not all electrolytic extractions release chlorine; the main issue is the energy demand.
- [ ] Carbon reduction releases no gases at all
    - *why wrong:* Carbon reduction also releases carbon dioxide; the point is that electrolysis uses much more energy.
- [ ] Electrolysis destroys the ore permanently
    - *why wrong:* Both methods use up ore; the greater impact of electrolysis is its high energy use.

**Q10. [recall]** Define oxidation in terms of oxygen.
- [✔︎] The gain of oxygen by a substance
- [ ] The loss of oxygen by a substance
    - *why wrong:* That is reduction; oxidation is a GAIN of oxygen.
- [ ] The gain of electrons by a substance
    - *why wrong:* Gain of electrons is reduction, not oxidation.
- [ ] The loss of hydrogen by a substance
    - *why wrong:* In this topic oxidation is defined as gain of oxygen, not loss of hydrogen.

### Triple Higher — 2 extra Higher/depth questions

_On top of the 10 above (so Triple Higher shows 12)._

**Q11. [reason]** In Fe₂O₃ + 3CO → 2Fe + 3CO₂, identify the species that is oxidised and justify your choice.
- [✔︎] Carbon monoxide — it gains oxygen to become carbon dioxide
- [ ] Iron(III) oxide — it gains oxygen
    - *why wrong:* Iron oxide LOSES oxygen to become iron, so it is reduced, not oxidised.
- [ ] Iron — it loses oxygen
    - *why wrong:* Iron gains no oxygen; it is the product of reduction, so it is not oxidised.
- [ ] Carbon dioxide — it is fully oxidised
    - *why wrong:* Carbon dioxide is the product; the species that IS oxidised during the reaction is the carbon monoxide.

**Q12. [reason]** Explain, in terms of electrons, what happens to the metal ions when a metal is extracted from its molten ore by electrolysis.
- [✔︎] The metal ions gain electrons at the cathode and are reduced to metal atoms
- [ ] The metal ions lose electrons and are oxidised
    - *why wrong:* At the cathode positive metal ions GAIN electrons, so they are reduced, not oxidised.
- [ ] The metal ions gain protons to become neutral
    - *why wrong:* Charge is neutralised by gaining electrons, not protons — nuclei are unchanged.
- [ ] The metal ions simply melt without changing
    - *why wrong:* Melting frees the ions to move, but the chemical change is the gain of electrons at the cathode.

---

## Oxidation and Reduction  ·  `oxidation-reduction`  ·  AQA 5.4.1.4

> 🚩 **Triple-depth call (your review):** MATCHED — this AQA sub-topic is identical for Combined and Triple. Foundation difficulty is the same across both pathways; each Triple set = the Combined set + extra same-difficulty coverage. No AQA Triple-only content on this page.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often think oxidation only ever means 'gaining oxygen', so they get stuck the moment there is no oxygen in the equation. Gaining oxygen is only one case. The deeper meaning is about electrons: OIL RIG — Oxidation Is Loss of electrons, Reduction Is Gain of electrons. So when magnesium loses electrons to form Mg²⁺, it is oxidised even though no oxygen is written, and gaining oxygen simply happens to be one way a substance loses electrons.

### Combined Foundation — 10 questions

_These 10 also appear verbatim in Triple Foundation._

**Q1. [recall]** Define oxidation in terms of oxygen.
- [✔︎] The gain of oxygen by a substance
- [ ] The loss of oxygen by a substance
    - *why wrong:* Losing oxygen is reduction; oxidation is a GAIN of oxygen.
- [ ] The gain of hydrogen by a substance
    - *why wrong:* Oxidation here is defined by oxygen, not hydrogen — and gaining hydrogen is not it.
- [ ] The loss of mass by a substance
    - *why wrong:* Oxidation is about oxygen transfer; mass may even increase as oxygen is added.

**Q2. [recall]** Define reduction in terms of oxygen.
- [✔︎] The loss of oxygen from a substance
- [ ] The gain of oxygen by a substance
    - *why wrong:* Gaining oxygen is oxidation; reduction is the LOSS of oxygen.
- [ ] The gain of mass by a substance
    - *why wrong:* Reduction removes oxygen, which tends to lower mass, and it is defined by oxygen not mass.
- [ ] The loss of electrons from a substance
    - *why wrong:* Loss of electrons is oxidation; reduction in terms of electrons is a GAIN.

**Q3. [apply]** In the reaction 2Mg + O₂ → 2MgO, identify the substance that is oxidised.
- [✔︎] Magnesium — it gains oxygen to form magnesium oxide
- [ ] Oxygen — it joins with the magnesium
    - *why wrong:* Oxygen is the substance being added; it is magnesium that gains oxygen and is oxidised.
- [ ] Magnesium oxide — it is the product
    - *why wrong:* Magnesium oxide is the result of the oxidation, not the thing being oxidised.
- [ ] Neither — no oxidation occurs
    - *why wrong:* Magnesium clearly gains oxygen, so it is oxidised.

**Q4. [apply]** In the reaction Fe₂O₃ + 3CO → 2Fe + 3CO₂, identify the substance that is reduced.
- [✔︎] Iron(III) oxide — it loses oxygen to become iron
- [ ] Carbon monoxide — it loses oxygen
    - *why wrong:* Carbon monoxide GAINS oxygen to become CO₂, so it is oxidised, not reduced.
- [ ] Iron — it is the metal produced
    - *why wrong:* Iron is the product of the reduction, not the substance reduced.
- [ ] Carbon dioxide — it holds the oxygen
    - *why wrong:* Carbon dioxide is the oxidised product; the reduced substance is the iron oxide.

**Q5. [reason]** Explain why the rusting of iron is described as an oxidation.
- [✔︎] The iron gains oxygen (and water) to form hydrated iron(III) oxide
- [ ] The iron loses oxygen to the air
    - *why wrong:* Rusting adds oxygen to iron; losing oxygen would be reduction.
- [ ] The iron loses electrons to become lighter
    - *why wrong:* Rust actually adds mass; rusting is oxidation because iron gains oxygen.
- [ ] The iron melts and reforms
    - *why wrong:* Rusting is a chemical reaction with oxygen, not a physical melting.

**Q6. [apply]** In CuO + H₂ → Cu + H₂O, identify the substance that is oxidised.
- [✔︎] Hydrogen — it gains oxygen to form water
- [ ] Copper oxide — it gains oxygen
    - *why wrong:* Copper oxide LOSES oxygen to become copper, so it is reduced, not oxidised.
- [ ] Copper — it is produced
    - *why wrong:* Copper is the reduced product; the substance oxidised is the hydrogen.
- [ ] Water — it contains oxygen
    - *why wrong:* Water is the product formed when hydrogen is oxidised; it is not itself being oxidised.

**Q7. [recall]** State what the phrase 'OIL RIG' helps you remember.
- [✔︎] Oxidation Is Loss of electrons, Reduction Is Gain of electrons
- [ ] Oxidation Is Gain of electrons, Reduction Is Loss of electrons
    - *why wrong:* This is reversed — oxidation is LOSS and reduction is GAIN of electrons.
- [ ] Oxidation Involves Liquids, Reduction Involves Gases
    - *why wrong:* OIL RIG is about electron loss and gain, not about states of matter.
- [ ] Oxygen In Liquid, Reduces In Gas
    - *why wrong:* OIL RIG stands for the electron definitions of oxidation and reduction.

**Q8. [apply]** A metal oxide loses its oxygen during a reaction. State whether the oxide has been oxidised or reduced.
- [✔︎] Reduced — it has lost oxygen
- [ ] Oxidised — it has reacted
    - *why wrong:* Reacting is not the same as being oxidised; losing oxygen is specifically reduction.
- [ ] Neither — losing oxygen is not a redox change
    - *why wrong:* Losing oxygen is exactly reduction, which is one half of a redox change.
- [ ] Both at the same time
    - *why wrong:* A single substance losing oxygen is reduced; it cannot be both for that change.

**Q9. [reason]** Explain why oxidation and reduction always happen together in these reactions.
- [✔︎] If one substance loses oxygen (is reduced), another substance must gain that oxygen (is oxidised)
- [ ] Because oxidation causes a separate reduction to start later
    - *why wrong:* They occur at the same time in the same reaction, not one after another.
- [ ] Because every reaction needs oxygen to take part
    - *why wrong:* Many redox reactions involve no oxygen at all — the pairing is about electron transfer.
- [ ] Because heat from oxidation drives reduction
    - *why wrong:* The link is the transfer of oxygen or electrons, not heat.

**Q10. [apply]** During combustion, carbon reacts to form carbon dioxide. Classify this change as oxidation or reduction.
- [✔︎] Oxidation — the carbon gains oxygen
- [ ] Reduction — the carbon is broken down
    - *why wrong:* Carbon gains oxygen to form CO₂, which is oxidation, not reduction.
- [ ] Neither — burning is only a physical change
    - *why wrong:* Combustion is a chemical reaction in which carbon is oxidised.
- [ ] Both — it is oxidised then reduced
    - *why wrong:* The carbon only gains oxygen here, so it is simply oxidised.

### Triple Foundation — 2 extra Foundation-level questions

_On top of the 10 above (so Triple Foundation shows 12)._

**Q11. [apply]** Magnesium ribbon burns in air with a bright white flame. State what has happened to the magnesium in terms of oxygen.
- [✔︎] It has been oxidised — it has gained oxygen to form magnesium oxide
- [ ] It has been reduced — it has lost oxygen
    - *why wrong:* Burning adds oxygen to magnesium, so it is oxidised, not reduced.
- [ ] It has been neutralised
    - *why wrong:* Neutralisation is an acid-base reaction, not burning in oxygen.
- [ ] It has been displaced
    - *why wrong:* Displacement swaps one element for another in a compound; here magnesium simply gains oxygen.

**Q12. [recall]** State the name given to a reaction in which oxidation and reduction happen together.
- [✔︎] A redox reaction
- [ ] A neutralisation reaction
    - *why wrong:* Neutralisation is acid + base; a reaction with both oxidation and reduction is 'redox'.
- [ ] A combustion reaction
    - *why wrong:* Combustion is one example of a redox reaction, but the general name is 'redox'.
- [ ] A thermal decomposition reaction
    - *why wrong:* Thermal decomposition is breaking down with heat; the term for combined oxidation and reduction is 'redox'.

### Combined Higher — 10 questions

_A different, harder set from Foundation. These 10 also appear verbatim in Triple Higher._

**Q1. [reason]** Define oxidation in terms of electrons.
- [✔︎] The loss of electrons
- [ ] The gain of electrons
    - *why wrong:* Gain of electrons is reduction; oxidation is a LOSS of electrons (OIL).
- [ ] The gain of oxygen only
    - *why wrong:* Gaining oxygen is one case of oxidation, but the electron definition is loss of electrons.
- [ ] The loss of protons
    - *why wrong:* Redox involves electrons, not protons; the nucleus is unchanged.

**Q2. [reason]** Define reduction in terms of electrons.
- [✔︎] The gain of electrons
- [ ] The loss of electrons
    - *why wrong:* Loss of electrons is oxidation; reduction is a GAIN of electrons (RIG).
- [ ] The loss of oxygen only
    - *why wrong:* Losing oxygen is one case of reduction, but the electron definition is gain of electrons.
- [ ] The gain of protons
    - *why wrong:* Reduction is about gaining electrons, not protons.

**Q3. [apply]** In Mg + Cu²⁺ → Mg²⁺ + Cu, identify the species that is oxidised.
- [✔︎] Magnesium — it loses electrons to form Mg²⁺
- [ ] Copper ions — they change into copper
    - *why wrong:* Copper ions gain electrons and are reduced; the oxidised species is magnesium.
- [ ] Magnesium ions — they are formed
    - *why wrong:* Magnesium ions are the product of oxidation, not the species being oxidised.
- [ ] Copper — it is deposited
    - *why wrong:* Copper is the reduced product; magnesium is the species oxidised.

**Q4. [apply]** In Mg + Cu²⁺ → Mg²⁺ + Cu, identify the species that is reduced.
- [✔︎] The copper ions — they gain electrons to become copper atoms
- [ ] Magnesium — it forms ions
    - *why wrong:* Magnesium LOSES electrons, so it is oxidised, not reduced.
- [ ] Magnesium ions — they gain electrons
    - *why wrong:* Magnesium ions are formed by oxidation; it is the copper ions that gain electrons.
- [ ] Neither — it is not a redox reaction
    - *why wrong:* Electrons pass from magnesium to copper ions, so it is a redox reaction with a reduced species.

**Q5. [reason]** Explain why a displacement reaction between a metal and a metal-salt solution is classed as a redox reaction.
- [✔︎] Electrons are transferred: the more reactive metal loses electrons (oxidised) and the less reactive metal ions gain them (reduced)
- [ ] Oxygen is added to one metal and removed from the other
    - *why wrong:* No oxygen need be involved; the redox classification comes from the electron transfer.
- [ ] The two metals swap places without any electron change
    - *why wrong:* Electrons are transferred, which is exactly why it is redox.
- [ ] Heat is released, which drives an oxidation
    - *why wrong:* It is redox because of electron transfer, not because heat is released.

**Q6. [apply] ⭐** The half-equation Cu²⁺ + 2e⁻ → Cu is given. State whether it shows oxidation or reduction.
- [✔︎] Reduction — the copper ions gain electrons
- [ ] Oxidation — the copper ions react
    - *why wrong:* Electrons are gained (shown on the left), so this is reduction, not oxidation.
- [ ] Neither — half-equations are not redox
    - *why wrong:* Half-equations show exactly one half of a redox process; here it is reduction.
- [ ] Both at once
    - *why wrong:* A single half-equation shows only one of the two — here, reduction.

**Q7. [apply] ⭐** The half-equation Mg → Mg²⁺ + 2e⁻ is given. Classify the change it shows.
- [✔︎] Oxidation — magnesium loses two electrons
- [ ] Reduction — magnesium gains stability
    - *why wrong:* Electrons are lost (shown on the right), so this is oxidation regardless of stability.
- [ ] Neutralisation — a salt is formed
    - *why wrong:* No acid or base is involved; losing electrons is oxidation.
- [ ] Displacement — a metal is replaced
    - *why wrong:* This half-equation shows only the loss of electrons by magnesium, which is oxidation.

**Q8. [reason]** Explain how the 'gain of oxygen' and 'loss of electrons' definitions of oxidation fit together for magnesium burning in oxygen.
- [✔︎] As magnesium gains oxygen it loses electrons to the oxygen atoms, forming Mg²⁺ and O²⁻ — so both definitions describe the same change
- [ ] They describe two different reactions happening separately
    - *why wrong:* They are two ways of describing the SAME change to the magnesium.
- [ ] Only the oxygen definition applies when oxygen is present
    - *why wrong:* The electron definition also applies — magnesium loses electrons to the oxygen.
- [ ] The electron definition contradicts the oxygen definition
    - *why wrong:* They agree: gaining oxygen here is accompanied by losing electrons.

**Q9. [recall]** State what OIL RIG stands for.
- [✔︎] Oxidation Is Loss, Reduction Is Gain — of electrons
- [ ] Oxidation Is Gain, Reduction Is Loss — of electrons
    - *why wrong:* This is reversed; oxidation is loss and reduction is gain of electrons.
- [ ] Oxygen In Lattice, Removed In Gas
    - *why wrong:* OIL RIG is a memory aid for the electron definitions, not about lattices or gases.
- [ ] Oxidation In Liquids, Reduction In Gases
    - *why wrong:* OIL RIG has nothing to do with states — it describes electron loss and gain.

**Q10. [apply]** In the ionic equation Zn + Fe²⁺ → Zn²⁺ + Fe, identify the species oxidised.
- [✔︎] Zinc — it loses electrons to form Zn²⁺
- [ ] Iron(II) ions — they change to iron
    - *why wrong:* Iron ions gain electrons and are reduced; zinc is the species oxidised.
- [ ] Iron — it is deposited
    - *why wrong:* Iron is the reduced product; zinc is oxidised.
- [ ] Zinc ions — they carry charge
    - *why wrong:* Zinc ions are the product of oxidation; the species oxidised is the zinc metal.

### Triple Higher — 2 extra Higher/depth questions

_On top of the 10 above (so Triple Higher shows 12)._

**Q11. [reason]** In the reaction Zn + Cu²⁺ → Zn²⁺ + Cu, identify the species oxidised and explain your choice in terms of electrons.
- [✔︎] Zinc — it loses two electrons to become Zn²⁺
- [ ] Copper ions — they lose electrons to become copper
    - *why wrong:* Copper ions GAIN electrons to become copper, so they are reduced, not oxidised.
- [ ] Zinc ions — they are formed
    - *why wrong:* Zinc ions are the product; the species oxidised is the zinc metal that lost electrons.
- [ ] Neither — no electrons move
    - *why wrong:* Electrons transfer from zinc to copper ions, so a redox change certainly occurs.

**Q12. [apply]** An iron(II) ion changes into an iron(III) ion: Fe²⁺ → Fe³⁺ + e⁻. Classify this change and justify it.
- [✔︎] Oxidation — the ion loses an electron (its charge becomes more positive)
- [ ] Reduction — the ion becomes more stable
    - *why wrong:* Losing an electron is oxidation regardless of stability; the charge rising to 3+ confirms loss of an electron.
- [ ] Neutralisation — an acid is involved
    - *why wrong:* No acid or base is present; this is a redox change, specifically oxidation.
- [ ] No change in oxidation state
    - *why wrong:* The charge rises from 2+ to 3+, so an electron is lost and the ion is oxidised.

---

## Reactions of Acids with Metals and Bases  ·  `reactions-of-acids`  ·  AQA 5.4.2.1–5.4.2.2

> 🚩 **Triple-depth call (your review):** MATCHED — this AQA sub-topic is identical for Combined and Triple. Foundation difficulty is the same across both pathways; each Triple set = the Combined set + extra same-difficulty coverage. No AQA Triple-only content on this page.

**Common Mistake (reformatted — ✅ mistake-first):**

> When an acid reacts with a metal carbonate, students often write only 'salt + water' and forget the carbon dioxide, or write 'salt + carbon dioxide' and drop the water. A carbonate always gives THREE products: salt + water + carbon dioxide. The fizzing you see is that carbon dioxide escaping — so if bubbles form, the CO₂ must be in your equation.

### Combined Foundation — 10 questions

_These 10 also appear verbatim in Triple Foundation._

**Q1. [recall]** Name the two products formed when a dilute acid reacts with a metal.
- [✔︎] A salt and hydrogen
- [ ] A salt and water
    - *why wrong:* Salt + water comes from an acid with a metal oxide or hydroxide, not with the metal itself.
- [ ] A salt and carbon dioxide
    - *why wrong:* Carbon dioxide is released only when the acid reacts with a carbonate.
- [ ] A metal oxide and water
    - *why wrong:* The metal forms a dissolved salt and hydrogen gas, not an oxide.

**Q2. [recall]** Name the three products formed when a dilute acid reacts with a metal carbonate.
- [✔︎] A salt, water and carbon dioxide
- [ ] A salt and hydrogen
    - *why wrong:* Hydrogen comes from acid + metal; a carbonate gives water and carbon dioxide instead.
- [ ] A salt and water only
    - *why wrong:* This forgets the carbon dioxide — the gas that makes the mixture fizz.
- [ ] A salt and carbon dioxide only
    - *why wrong:* This forgets the water — a carbonate gives all three products.

**Q3. [apply]** Name the salt produced when hydrochloric acid reacts with magnesium.
- [✔︎] Magnesium chloride
- [ ] Magnesium sulfate
    - *why wrong:* Sulfate salts come from sulfuric acid; hydrochloric acid makes chlorides.
- [ ] Magnesium nitrate
    - *why wrong:* Nitrate salts come from nitric acid; hydrochloric acid makes chlorides.
- [ ] Magnesium hydroxide
    - *why wrong:* A hydroxide is a base, not the salt; the salt from HCl is a chloride.

**Q4. [apply]** Name the salt produced when sulfuric acid reacts with zinc oxide.
- [✔︎] Zinc sulfate
- [ ] Zinc chloride
    - *why wrong:* Chloride salts come from hydrochloric acid; sulfuric acid makes sulfates.
- [ ] Zinc nitrate
    - *why wrong:* Nitrate salts come from nitric acid; sulfuric acid makes sulfates.
- [ ] Zinc oxide
    - *why wrong:* Zinc oxide is the reactant base; the salt formed is zinc sulfate.

**Q5. [apply]** A gas given off when magnesium reacts with dilute acid gives a squeaky pop with a lit splint. Identify the gas.
- [✔︎] Hydrogen
- [ ] Carbon dioxide
    - *why wrong:* Carbon dioxide turns limewater cloudy and puts out a splint; it does not pop.
- [ ] Oxygen
    - *why wrong:* Oxygen relights a glowing splint; it does not give a squeaky pop.
- [ ] Chlorine
    - *why wrong:* Chlorine bleaches litmus and has a sharp smell; the pop test identifies hydrogen.

**Q6. [apply]** A gas given off when a carbonate reacts with acid turns limewater cloudy. Identify the gas.
- [✔︎] Carbon dioxide
- [ ] Hydrogen
    - *why wrong:* Hydrogen gives a squeaky pop; it does not turn limewater cloudy.
- [ ] Oxygen
    - *why wrong:* Oxygen relights a glowing splint; it does not turn limewater cloudy.
- [ ] Water vapour
    - *why wrong:* Water vapour is not a test gas here; the limewater test identifies carbon dioxide.

**Q7. [reason]** Explain why bubbles are seen when a metal carbonate is added to a dilute acid.
- [✔︎] Carbon dioxide gas is produced and escapes from the mixture as bubbles
- [ ] Hydrogen gas is produced and escapes
    - *why wrong:* Carbonates release carbon dioxide, not hydrogen; hydrogen comes from acid + metal.
- [ ] The acid is boiling
    - *why wrong:* The bubbles are a gas made in the reaction, not boiling — the mixture need not be hot.
- [ ] Oxygen is released from the carbonate
    - *why wrong:* The gas released is carbon dioxide, not oxygen.

**Q8. [recall]** Name the two products formed when a dilute acid reacts with a metal hydroxide.
- [✔︎] A salt and water
- [ ] A salt and hydrogen
    - *why wrong:* Hydrogen comes from acid + metal; a hydroxide (a base) gives salt + water.
- [ ] A salt, water and carbon dioxide
    - *why wrong:* Carbon dioxide appears only with carbonates, not with hydroxides.
- [ ] A base and water
    - *why wrong:* The acid and base react to form a salt and water, not another base.

**Q9. [apply]** Which acid must be used to produce a nitrate salt?
- [✔︎] Nitric acid
- [ ] Hydrochloric acid
    - *why wrong:* Hydrochloric acid produces chloride salts, not nitrates.
- [ ] Sulfuric acid
    - *why wrong:* Sulfuric acid produces sulfate salts, not nitrates.
- [ ] Carbonic acid
    - *why wrong:* Carbonic acid is a weak acid and does not give nitrate salts; nitrates come from nitric acid.

**Q10. [apply]** Complete the products: copper carbonate + sulfuric acid → ?
- [✔︎] Copper sulfate + water + carbon dioxide
- [ ] Copper sulfate + hydrogen
    - *why wrong:* A carbonate gives water and carbon dioxide, not hydrogen.
- [ ] Copper sulfate + water only
    - *why wrong:* This forgets the carbon dioxide that a carbonate always releases.
- [ ] Copper chloride + water + carbon dioxide
    - *why wrong:* Sulfuric acid gives a sulfate salt, not a chloride.

### Triple Foundation — 2 extra Foundation-level questions

_On top of the 10 above (so Triple Foundation shows 12)._

**Q11. [apply]** Name the salt produced when hydrochloric acid is neutralised by sodium hydroxide.
- [✔︎] Sodium chloride
- [ ] Sodium sulfate
    - *why wrong:* Sulfate salts come from sulfuric acid; hydrochloric acid gives chlorides.
- [ ] Sodium nitrate
    - *why wrong:* Nitrate salts come from nitric acid; hydrochloric acid gives chlorides.
- [ ] Sodium hydroxide
    - *why wrong:* Sodium hydroxide is the base reactant; the salt formed is sodium chloride.

**Q12. [recall]** Name a metal that reacts with dilute hydrochloric acid to give off hydrogen.
- [✔︎] Magnesium
- [ ] Copper
    - *why wrong:* Copper is below hydrogen in the reactivity series and does not react with dilute acid.
- [ ] Gold
    - *why wrong:* Gold is unreactive and does not react with dilute acid.
- [ ] Silver
    - *why wrong:* Silver is less reactive than hydrogen and does not react with dilute acid.

### Combined Higher — 10 questions

_A different, harder set from Foundation. These 10 also appear verbatim in Triple Higher._

**Q1. [apply]** Predict the products when sulfuric acid reacts with copper(II) oxide, and name the salt.
- [✔︎] Copper sulfate and water
- [ ] Copper sulfate and hydrogen
    - *why wrong:* A metal oxide gives salt + water; hydrogen comes only from acid + metal.
- [ ] Copper chloride and water
    - *why wrong:* Sulfuric acid gives a sulfate salt, not a chloride.
- [ ] Copper sulfate, water and carbon dioxide
    - *why wrong:* Carbon dioxide appears with carbonates, not with a metal oxide.

**Q2. [apply]** Identify the correctly balanced equation for calcium carbonate reacting with hydrochloric acid.
- [✔︎] CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂
- [ ] CaCO₃ + HCl → CaCl₂ + H₂O + CO₂
    - *why wrong:* The chlorines are not balanced — two HCl are needed to give CaCl₂.
- [ ] CaCO₃ + 2HCl → CaCl₂ + CO₂
    - *why wrong:* This drops the water; a carbonate gives salt + water + carbon dioxide.
- [ ] CaCO₃ + 2HCl → CaCl₂ + H₂ + CO₂
    - *why wrong:* The product is water, not hydrogen — carbonates do not release hydrogen.

**Q3. [reason]** Explain why a metal carbonate fizzes with dilute acid but a metal oxide does not.
- [✔︎] The carbonate releases carbon dioxide gas, which bubbles off, whereas the oxide only forms a salt and water
- [ ] The carbonate is more reactive, so it releases hydrogen
    - *why wrong:* Carbonates release carbon dioxide, not hydrogen; oxides simply do not release a gas.
- [ ] The oxide dissolves without any reaction
    - *why wrong:* The oxide does react (forming salt + water); it just produces no gas.
- [ ] The carbonate contains a metal and the oxide does not
    - *why wrong:* Both contain a metal; the difference is the carbonate produces a gas (CO₂).

**Q4. [apply]** A salt is identified as potassium nitrate. Deduce the acid and the alkali used to make it.
- [✔︎] Nitric acid and potassium hydroxide
- [ ] Hydrochloric acid and potassium hydroxide
    - *why wrong:* That would give potassium chloride; a nitrate needs nitric acid.
- [ ] Nitric acid and sodium hydroxide
    - *why wrong:* That would give sodium nitrate; the potassium must come from potassium hydroxide.
- [ ] Sulfuric acid and potassium hydroxide
    - *why wrong:* That would give potassium sulfate; a nitrate needs nitric acid.

**Q5. [reason]** Explain why the reaction of an acid with an alkali is described as neutralisation.
- [✔︎] The H⁺ ions from the acid react with the OH⁻ ions from the alkali to form water, cancelling both out and leaving a neutral salt solution
- [ ] The acid destroys the alkali completely
    - *why wrong:* Neither is destroyed; their ions combine to form water and a salt.
- [ ] The alkali turns the acid into a gas
    - *why wrong:* No gas is produced; the ions form water in neutralisation.
- [ ] The two liquids simply mix without reacting
    - *why wrong:* A reaction does occur: H⁺ and OH⁻ combine to form water.

**Q6. [apply]** Predict the products when nitric acid reacts with sodium hydroxide.
- [✔︎] Sodium nitrate and water
- [ ] Sodium nitrate and hydrogen
    - *why wrong:* Acid + alkali gives salt + water; no hydrogen is released.
- [ ] Sodium chloride and water
    - *why wrong:* Nitric acid gives a nitrate salt, not a chloride.
- [ ] Sodium hydroxide and water
    - *why wrong:* Sodium hydroxide is the reactant; the salt formed is sodium nitrate.

**Q7. [apply]** Deduce the volume of hydrogen relationship: which metal will react fastest with the same dilute acid — magnesium or iron?
- [✔︎] Magnesium, because it is more reactive than iron
- [ ] Iron, because it is denser
    - *why wrong:* Reaction rate with acid follows reactivity, not density; magnesium is more reactive.
- [ ] They react at the same rate because the acid is the same
    - *why wrong:* The metal's reactivity also matters; magnesium reacts faster than iron.
- [ ] Iron, because it is more common
    - *why wrong:* Abundance is irrelevant; magnesium's higher reactivity makes it react faster.

**Q8. [reason]** Explain why using nitric acid with copper oxide is a suitable way to make copper nitrate, but using it with copper metal is not part of this method.
- [✔︎] Copper oxide is a base that neutralises the acid to give the salt and water; copper metal is below hydrogen and does not react with the acid in the simple salt-and-hydrogen way
- [ ] Copper metal reacts too violently with acids
    - *why wrong:* Copper metal is unreactive with dilute acid, not violent.
- [ ] Copper oxide is an acid, so it makes a stronger salt
    - *why wrong:* Copper oxide is a base, not an acid; it neutralises the acid.
- [ ] Copper nitrate can only be made from a carbonate
    - *why wrong:* It can be made from the oxide (a base) too; the point is the metal does not react.

**Q9. [recall]** State what is meant by a base.
- [✔︎] A substance that neutralises an acid, such as a metal oxide or metal hydroxide
- [ ] A substance that turns litmus red
    - *why wrong:* That describes an acid; a base neutralises acids and turns litmus blue if soluble.
- [ ] A substance that always dissolves in water
    - *why wrong:* Only soluble bases (alkalis) dissolve; many bases are insoluble.
- [ ] A substance with a pH below 7
    - *why wrong:* A pH below 7 is acidic; bases are neutral-to-alkaline and neutralise acids.

**Q10. [apply]** Predict whether magnesium carbonate reacting with nitric acid produces a gas, and name any gas formed.
- [✔︎] Yes — carbon dioxide is produced (along with the salt and water)
- [ ] Yes — hydrogen is produced
    - *why wrong:* A carbonate releases carbon dioxide, not hydrogen.
- [ ] No gas is produced
    - *why wrong:* Carbonates always release carbon dioxide when they react with acids.
- [ ] Yes — oxygen is produced
    - *why wrong:* The gas from a carbonate-acid reaction is carbon dioxide, not oxygen.

### Triple Higher — 2 extra Higher/depth questions

_On top of the 10 above (so Triple Higher shows 12)._

**Q11. [apply]** Identify the correctly balanced symbol equation for magnesium reacting with hydrochloric acid.
- [✔︎] Mg + 2HCl → MgCl₂ + H₂
- [ ] Mg + HCl → MgCl + H
    - *why wrong:* MgCl and H are not real formulae; magnesium chloride is MgCl₂ and hydrogen is H₂.
- [ ] Mg + 2HCl → MgCl₂ + 2H
    - *why wrong:* Hydrogen gas is H₂, a molecule, not two separate H atoms.
- [ ] 2Mg + 2HCl → 2MgCl + H₂
    - *why wrong:* MgCl is the wrong formula; magnesium forms Mg²⁺ so the chloride is MgCl₂.

**Q12. [reason]** Explain why copper does not react with dilute sulfuric acid, unlike magnesium.
- [✔︎] Copper is less reactive than hydrogen, so it cannot displace hydrogen from the acid, whereas magnesium can
- [ ] Copper is a solid, so acids cannot reach its surface
    - *why wrong:* Magnesium is also a solid yet reacts; the difference is copper's low reactivity.
- [ ] Sulfuric acid is too weak to react with any metal
    - *why wrong:* Sulfuric acid reacts readily with magnesium; the issue is copper being below hydrogen.
- [ ] Copper instantly forms a protective salt layer
    - *why wrong:* There is no reaction to form a layer — copper simply cannot displace hydrogen.

---

## Making Salts and Neutralisation  ·  `salts-neutralisation`  ·  AQA 5.4.2.2–5.4.2.3

> 🚩 **Triple-depth call (your review):** MATCHED — this AQA sub-topic is identical for Combined and Triple. Foundation difficulty is the same across both pathways; each Triple set = the Combined set + extra same-difficulty coverage. No AQA Triple-only content on this page.

**Common Mistake (reformatted — ✅ mistake-first):**

> When making a soluble salt from an acid and an insoluble base, students often stop adding the base as soon as it starts to disappear, but then some acid is left unreacted and contaminates the salt. You must add the base in EXCESS — keep adding until no more dissolves — so that ALL the acid is used up. Then filter off the leftover excess base; the pure salt is dissolved in the filtrate.

### Combined Foundation — 10 questions

_These 10 also appear verbatim in Triple Foundation._

**Q1. [recall]** Name the two products formed when an acid reacts with an alkali.
- [✔︎] A salt and water
- [ ] A salt and hydrogen
    - *why wrong:* Hydrogen comes from acid + metal; acid + alkali gives salt + water.
- [ ] A salt and carbon dioxide
    - *why wrong:* Carbon dioxide comes from carbonates, not from an acid-alkali reaction.
- [ ] An alkali and water
    - *why wrong:* The acid and alkali react to form a salt, not another alkali.

**Q2. [apply]** Describe the first step in making copper sulfate crystals from copper oxide and sulfuric acid.
- [✔︎] Add copper oxide to warm dilute sulfuric acid until no more will dissolve (excess)
- [ ] Add a few drops of copper oxide and stop straight away
    - *why wrong:* You must add EXCESS copper oxide so all the acid reacts, not just a few drops.
- [ ] Add sodium hydroxide to the acid first
    - *why wrong:* Sodium hydroxide is not part of making copper sulfate from copper oxide.
- [ ] Boil the acid dry before adding anything
    - *why wrong:* The acid must stay in solution to react with the copper oxide.

**Q3. [apply]** Explain why the mixture is filtered after the acid has reacted with the excess base.
- [✔︎] To remove the leftover excess solid base, leaving the salt dissolved in the filtrate
- [ ] To remove the salt from the water
    - *why wrong:* The salt stays dissolved in the filtrate; filtering removes the undissolved excess base.
- [ ] To add more acid to the mixture
    - *why wrong:* Filtering separates a solid from a liquid; it does not add acid.
- [ ] To cool the mixture down quickly
    - *why wrong:* Filtering is to remove excess solid, not to cool the mixture.

**Q4. [apply]** Name the process used to obtain pure dry salt crystals from the salt solution.
- [✔︎] Crystallisation
- [ ] Filtration
    - *why wrong:* Filtration removes the excess solid earlier; crystals are obtained by crystallisation.
- [ ] Distillation
    - *why wrong:* Distillation collects the evaporated water, not the salt crystals.
- [ ] Chromatography
    - *why wrong:* Chromatography separates dissolved colours, not salt crystals from solution.

**Q5. [recall]** State what is meant by neutralisation.
- [✔︎] The reaction of an acid with a base or alkali to form a salt and water
- [ ] The reaction of an acid with a metal to form hydrogen
    - *why wrong:* That is acid + metal; neutralisation is acid + base forming salt + water.
- [ ] The evaporation of water from a salt solution
    - *why wrong:* That is crystallisation, not neutralisation.
- [ ] The mixing of two salts to form a solid
    - *why wrong:* That is precipitation; neutralisation is an acid-base reaction.

**Q6. [reason]** Explain why the dilute acid is warmed gently before the base is added.
- [✔︎] Warming speeds up the reaction between the acid and the base
- [ ] Warming makes the salt change colour
    - *why wrong:* Warming is to speed up the reaction, not to change colour.
- [ ] Warming turns the acid into an alkali
    - *why wrong:* Warming does not change an acid into an alkali; it only speeds the reaction.
- [ ] Warming removes the hydrogen gas
    - *why wrong:* No hydrogen is produced here; warming simply speeds up the reaction.

**Q7. [apply]** Name the salt made when nitric acid reacts with copper oxide.
- [✔︎] Copper nitrate
- [ ] Copper sulfate
    - *why wrong:* Sulfate salts come from sulfuric acid; nitric acid makes nitrates.
- [ ] Copper chloride
    - *why wrong:* Chloride salts come from hydrochloric acid; nitric acid makes nitrates.
- [ ] Copper oxide
    - *why wrong:* Copper oxide is the base reactant; the salt formed is copper nitrate.

**Q8. [recall]** State what is meant by an alkali.
- [✔︎] A soluble base — a base that dissolves in water
- [ ] An acid that is very concentrated
    - *why wrong:* An alkali is a soluble base, the opposite of an acid.
- [ ] Any solid that neutralises water
    - *why wrong:* An alkali neutralises acids, and it is specifically a soluble base.
- [ ] A metal that reacts with acid
    - *why wrong:* That is a reactive metal; an alkali is a soluble base such as sodium hydroxide.

**Q9. [apply]** Place these steps in the correct order for making a pure dry salt: filter, add excess base to acid, crystallise.
- [✔︎] Add excess base to acid, filter, crystallise
- [ ] Filter, add excess base to acid, crystallise
    - *why wrong:* You must react the acid with excess base first; there is nothing to filter before that.
- [ ] Crystallise, filter, add excess base to acid
    - *why wrong:* Crystallisation is the last step, once the pure salt solution is ready.
- [ ] Add excess base to acid, crystallise, filter
    - *why wrong:* You filter off the excess base BEFORE crystallising the salt.

**Q10. [reason]** Explain why the salt solution is left to crystallise slowly rather than boiled completely dry.
- [✔︎] Slow crystallisation produces good, pure crystals; boiling dry can make the crystals decompose or trap impurities
- [ ] Boiling dry would turn the salt back into acid
    - *why wrong:* Boiling dry does not reform the acid; it simply damages the crystals.
- [ ] Slow crystallisation makes the salt dissolve again
    - *why wrong:* Slow crystallisation forms solid crystals; it does not redissolve them.
- [ ] Boiling dry is dangerous because the salt is explosive
    - *why wrong:* The salt is not explosive; boiling dry just gives poorer crystals.

### Triple Foundation — 2 extra Foundation-level questions

_On top of the 10 above (so Triple Foundation shows 12)._

**Q11. [recall]** Name the apparatus used to separate the excess solid base from the salt solution.
- [✔︎] A filter funnel with filter paper
- [ ] A measuring cylinder
    - *why wrong:* A measuring cylinder measures volume; it does not separate solids from liquids.
- [ ] A pipette
    - *why wrong:* A pipette measures a fixed volume of liquid; it does not filter.
- [ ] A Bunsen burner
    - *why wrong:* A Bunsen burner heats the mixture; the solid is separated by filtering.

**Q12. [apply]** State how you can tell that enough excess base has been added to react with all the acid.
- [✔︎] Some undissolved base remains at the bottom even after stirring
- [ ] The mixture starts to fizz
    - *why wrong:* Fizzing would suggest a carbonate reacting; the sign of excess is undissolved solid remaining.
- [ ] The solution turns bright red
    - *why wrong:* Colour change is not the test; leftover undissolved base shows excess has been added.
- [ ] All of the base dissolves completely
    - *why wrong:* If it all dissolves, there may not be excess and some acid could remain unreacted.

### Combined Higher — 10 questions

_A different, harder set from Foundation. These 10 also appear verbatim in Triple Higher._

**Q1. [apply]** Write the ionic equation for the neutralisation reaction between hydrochloric acid and sodium hydroxide.
- [✔︎] H⁺(aq) + OH⁻(aq) → H₂O(l)
- [ ] Na⁺(aq) + Cl⁻(aq) → NaCl(s)
    - *why wrong:* Na⁺ and Cl⁻ are spectator ions; the reaction that occurs is H⁺ + OH⁻ → water.
- [ ] HCl(aq) + NaOH(aq) → NaCl(aq) + H₂O(l)
    - *why wrong:* That is the full equation; the IONIC equation shows only the ions that react: H⁺ + OH⁻.
- [ ] H⁺(aq) + Cl⁻(aq) → HCl(l)
    - *why wrong:* The ionic equation for neutralisation is H⁺ combining with OH⁻ to form water.

**Q2. [reason]** Explain why an excess of the insoluble base is used when preparing a soluble salt.
- [✔︎] Excess base guarantees that all the acid is used up; the leftover base is then filtered off so the salt is not contaminated with acid
- [ ] Excess base makes the salt crystals larger
    - *why wrong:* Excess base is about using up all the acid, not crystal size.
- [ ] Excess base speeds up crystallisation
    - *why wrong:* Excess base ensures complete reaction of the acid; it does not drive crystallisation.
- [ ] Excess base lowers the pH of the solution
    - *why wrong:* Adding base raises the pH; the point of excess is to react with all the acid.

**Q3. [apply]** Describe how you would obtain pure dry crystals from a copper sulfate solution.
- [✔︎] Heat the solution to evaporate some water, then leave it to crystallise slowly and pat the crystals dry
- [ ] Filter the solution to collect the crystals
    - *why wrong:* The salt is dissolved, so filtering collects nothing; crystals form by crystallisation.
- [ ] Boil the solution completely dry
    - *why wrong:* Boiling dry damages the crystals; you evaporate only some water then crystallise slowly.
- [ ] Add more acid to force the crystals out
    - *why wrong:* Adding acid contaminates the salt; crystals form by evaporating water and cooling.

**Q4. [reason]** Explain why the excess-solid method works for an insoluble base but not for making a salt from an acid and a soluble alkali.
- [✔︎] The unreacted excess of an insoluble base can be filtered off, but a soluble alkali cannot be filtered out, so exact volumes must be measured instead
- [ ] A soluble alkali reacts too slowly to use
    - *why wrong:* Soluble alkalis react quickly; the issue is that excess cannot be filtered off.
- [ ] An insoluble base gives a different salt
    - *why wrong:* Both can give the same salt; the difference is whether excess can be removed by filtering.
- [ ] A soluble alkali does not form a salt
    - *why wrong:* It does form a salt; the problem is removing the excess, which filtering cannot do.

**Q5. [apply]** Deduce which base should be reacted with sulfuric acid to make zinc sulfate.
- [✔︎] Zinc oxide (or zinc carbonate/hydroxide)
- [ ] Sodium oxide
    - *why wrong:* Sodium oxide would give sodium sulfate; the zinc must come from a zinc base.
- [ ] Copper oxide
    - *why wrong:* Copper oxide would give copper sulfate, not zinc sulfate.
- [ ] Zinc chloride
    - *why wrong:* Zinc chloride is a salt, not a base; a base such as zinc oxide is needed.

**Q6. [reason]** Explain what happens to the H⁺ and OH⁻ ions during a neutralisation reaction.
- [✔︎] They combine together to form water molecules
- [ ] They join to form hydrogen gas
    - *why wrong:* H⁺ and OH⁻ form water, not hydrogen gas.
- [ ] They stay separate as spectator ions
    - *why wrong:* H⁺ and OH⁻ are the reacting ions; the spectators are the salt's ions.
- [ ] They form the solid salt directly
    - *why wrong:* The salt comes from the spectator ions; H⁺ and OH⁻ specifically form water.

**Q7. [apply]** Predict the products and the observation when copper carbonate reacts with dilute sulfuric acid.
- [✔︎] Copper sulfate, water and carbon dioxide — the mixture fizzes
- [ ] Copper sulfate and hydrogen — it fizzes
    - *why wrong:* A carbonate gives carbon dioxide, not hydrogen.
- [ ] Copper sulfate and water — no fizzing
    - *why wrong:* Carbon dioxide is released, so the mixture does fizz.
- [ ] Copper chloride, water and carbon dioxide — it fizzes
    - *why wrong:* Sulfuric acid gives a sulfate salt, not a chloride.

**Q8. [reason]** Explain why the crystals are patted dry with filter paper rather than warmed in an oven.
- [✔︎] Strong heating can drive off the water of crystallisation and change or damage the crystals, so gentle drying is used
- [ ] Warming would dissolve the crystals again
    - *why wrong:* Dry crystals do not dissolve in air; the risk is losing water of crystallisation.
- [ ] Filter paper adds mass to the crystals
    - *why wrong:* Filter paper only absorbs surface water; the reason to avoid heat is protecting the crystals.
- [ ] Warming would turn the salt back into acid
    - *why wrong:* Heating does not reform the acid; it can remove water of crystallisation.

**Q9. [recall]** State the difference between a base and an alkali.
- [✔︎] A base neutralises an acid; an alkali is a base that is soluble in water
- [ ] A base is soluble and an alkali is insoluble
    - *why wrong:* This is reversed — an alkali is the SOLUBLE kind of base.
- [ ] A base is an acid and an alkali is neutral
    - *why wrong:* A base is not an acid; both bases and alkalis neutralise acids.
- [ ] There is no difference between them
    - *why wrong:* There is a difference: an alkali is specifically a soluble base.

**Q10. [apply]** Deduce which acid and metal oxide would be used to prepare magnesium chloride.
- [✔︎] Hydrochloric acid and magnesium oxide
- [ ] Sulfuric acid and magnesium oxide
    - *why wrong:* Sulfuric acid would give magnesium sulfate, not chloride.
- [ ] Hydrochloric acid and copper oxide
    - *why wrong:* Copper oxide would give copper chloride; magnesium must come from magnesium oxide.
- [ ] Nitric acid and magnesium oxide
    - *why wrong:* Nitric acid would give magnesium nitrate, not chloride.

### Triple Higher — 2 extra Higher/depth questions

_On top of the 10 above (so Triple Higher shows 12)._

**Q11. [apply]** Write the ionic equation for the neutralisation of any acid by any alkali.
- [✔︎] H⁺(aq) + OH⁻(aq) → H₂O(l)
- [ ] H⁺(aq) + OH⁻(aq) → H₂O₂(l)
    - *why wrong:* The product of neutralisation is water, H₂O, not hydrogen peroxide H₂O₂.
- [ ] H⁺(aq) + Cl⁻(aq) → HCl(aq)
    - *why wrong:* The ionic equation for neutralisation involves OH⁻ forming water, not chloride reforming the acid.
- [ ] 2H⁺(aq) + O²⁻(aq) → H₂O(l)
    - *why wrong:* The reacting ions are H⁺ and OH⁻; oxide ions are not present in the alkali solution.

**Q12. [reason]** Explain why a titration, rather than the excess-solid method, must be used to make a salt from an acid and a soluble alkali.
- [✔︎] Both the acid and the alkali are soluble, so excess alkali cannot be filtered off; the exact volumes must instead be measured by titration
- [ ] The alkali is too dangerous to add in excess
    - *why wrong:* The real reason is that soluble excess cannot be filtered out, so exact volumes are needed.
- [ ] A soluble alkali does not react with acids
    - *why wrong:* Soluble alkalis react readily; the issue is that excess cannot be removed by filtering.
- [ ] Titration makes the salt crystals form faster
    - *why wrong:* Titration is used to get the exact amounts right, not to speed up crystallisation.

---

## The pH Scale and Neutralisation  ·  `ph-scale`  ·  AQA 5.4.2.4

> 🚩 **Triple-depth call (your review):** MATCHED — this AQA sub-topic is identical for Combined and Triple. Foundation difficulty is the same across both pathways; each Triple set = the Combined set + extra same-difficulty coverage. No AQA Triple-only content on this page.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often think a bigger pH number means more acidic, so they label pH 12 as 'strongly acidic'. It is the other way round. LOW pH (near 0) means strongly ACIDIC, with lots of H⁺ ions; HIGH pH (near 14) means strongly ALKALINE, with lots of OH⁻ ions; pH 7 is neutral. So pH 2 is a strong acid and pH 12 is a strong alkali — the further from 7, the stronger.

### Combined Foundation — 10 questions

_These 10 also appear verbatim in Triple Foundation._

**Q1. [recall]** State what the pH scale measures.
- [✔︎] How acidic or alkaline a solution is
- [ ] How concentrated a solution is
    - *why wrong:* Concentration is a separate idea; pH measures acidity/alkalinity.
- [ ] How much salt is dissolved in a solution
    - *why wrong:* pH is about acidity/alkalinity, not the amount of salt.
- [ ] The temperature of a solution
    - *why wrong:* Temperature is measured with a thermometer; pH measures acidity/alkalinity.

**Q2. [recall]** State the pH of a neutral solution.
- [✔︎] 7
- [ ] 0
    - *why wrong:* pH 0 is strongly acidic, not neutral.
- [ ] 14
    - *why wrong:* pH 14 is strongly alkaline, not neutral.
- [ ] 1
    - *why wrong:* pH 1 is strongly acidic; a neutral solution is pH 7.

**Q3. [apply]** A solution has a pH of 2. Classify it as acidic, neutral or alkaline.
- [✔︎] Strongly acidic
- [ ] Strongly alkaline
    - *why wrong:* pH below 7 is acidic; alkaline solutions have pH above 7.
- [ ] Neutral
    - *why wrong:* Only pH 7 is neutral; pH 2 is well into the acidic range.
- [ ] Weakly acidic
    - *why wrong:* pH 2 is close to the bottom of the scale, so it is strongly, not weakly, acidic.

**Q4. [apply]** A solution has a pH of 13. Classify it as acidic, neutral or alkaline.
- [✔︎] Strongly alkaline
- [ ] Strongly acidic
    - *why wrong:* pH above 7 is alkaline; acidic solutions have pH below 7.
- [ ] Neutral
    - *why wrong:* Only pH 7 is neutral; pH 13 is near the top of the alkaline range.
- [ ] Weakly alkaline
    - *why wrong:* pH 13 is close to the top of the scale, so it is strongly, not weakly, alkaline.

**Q5. [apply]** Name a method used to measure the pH of a solution.
- [✔︎] Universal indicator (matching its colour to a chart) or a pH probe
- [ ] Litmus paper, which gives an exact pH number
    - *why wrong:* Litmus only shows acid or alkali, not an exact pH; universal indicator or a probe gives pH.
- [ ] A thermometer
    - *why wrong:* A thermometer measures temperature, not pH.
- [ ] A balance
    - *why wrong:* A balance measures mass, not pH.

**Q6. [reason]** Explain why universal indicator turns red when added to a strong acid.
- [✔︎] A strong acid has a very low pH and a high concentration of H⁺ ions, which gives the red colour
- [ ] The acid is hot, which turns the indicator red
    - *why wrong:* Colour depends on pH (H⁺ concentration), not on temperature.
- [ ] The acid contains lots of OH⁻ ions
    - *why wrong:* OH⁻ ions make solutions alkaline (purple); acids have H⁺ ions and turn it red.
- [ ] Red simply means a liquid is present
    - *why wrong:* The red colour specifically signals a low pH / strong acid, not just any liquid.

**Q7. [apply]** Identify the ion that makes a solution acidic.
- [✔︎] The hydrogen ion, H⁺
- [ ] The hydroxide ion, OH⁻
    - *why wrong:* Hydroxide ions make a solution alkaline, not acidic.
- [ ] The sodium ion, Na⁺
    - *why wrong:* Sodium ions are spectator ions and do not make a solution acidic.
- [ ] The chloride ion, Cl⁻
    - *why wrong:* Chloride ions are spectators; acidity comes from H⁺ ions.

**Q8. [apply]** Identify the ion that makes a solution alkaline.
- [✔︎] The hydroxide ion, OH⁻
- [ ] The hydrogen ion, H⁺
    - *why wrong:* Hydrogen ions make a solution acidic, not alkaline.
- [ ] The chloride ion, Cl⁻
    - *why wrong:* Chloride ions are spectators and do not make a solution alkaline.
- [ ] The oxygen molecule, O₂
    - *why wrong:* Dissolved oxygen does not control alkalinity; OH⁻ ions do.

**Q9. [reason]** A student states that every solution with a pH of 7 must be pure water. Evaluate this statement.
- [✔︎] It is incorrect — many salt solutions (such as sodium chloride solution) are also neutral at pH 7, not just pure water
- [ ] It is correct — only pure water can ever be neutral
    - *why wrong:* Neutral salt solutions such as sodium chloride are also pH 7, so this is wrong.
- [ ] It is correct — water is the only liquid with any pH
    - *why wrong:* All aqueous solutions have a pH; pH 7 is not unique to water.
- [ ] It is incorrect — pure water is actually acidic
    - *why wrong:* Pure water is neutral (pH 7); the error is claiming ONLY water is neutral.

**Q10. [apply]** Three solutions have pH values 1, 6 and 9. Place them in order from most acidic to most alkaline.
- [✔︎] pH 1, then pH 6, then pH 9
- [ ] pH 9, then pH 6, then pH 1
    - *why wrong:* This is reversed — the lowest pH (1) is the most acidic, not the least.
- [ ] pH 6, then pH 1, then pH 9
    - *why wrong:* pH 1 is more acidic than pH 6, so pH 1 must come first.
- [ ] pH 1, then pH 9, then pH 6
    - *why wrong:* pH 6 is more acidic than pH 9, so pH 6 comes before pH 9.

### Triple Foundation — 2 extra Foundation-level questions

_On top of the 10 above (so Triple Foundation shows 12)._

**Q11. [recall]** State the colour of universal indicator in a neutral solution.
- [✔︎] Green
- [ ] Red
    - *why wrong:* Red shows a strong acid, not a neutral solution.
- [ ] Purple
    - *why wrong:* Purple shows a strong alkali, not a neutral solution.
- [ ] Colourless
    - *why wrong:* Universal indicator is green at neutral; it is not colourless.

**Q12. [apply]** Lemon juice has a pH of about 3. Classify lemon juice as acidic, neutral or alkaline.
- [✔︎] Acidic
- [ ] Alkaline
    - *why wrong:* pH 3 is below 7, so lemon juice is acidic, not alkaline.
- [ ] Neutral
    - *why wrong:* Only pH 7 is neutral; pH 3 is acidic.
- [ ] It has no pH
    - *why wrong:* All aqueous solutions have a pH; lemon juice at pH 3 is acidic.

### Combined Higher — 10 questions

_A different, harder set from Foundation. These 10 also appear verbatim in Triple Higher._

**Q1. [reason]** Explain what decides the pH of an aqueous solution in terms of ions.
- [✔︎] The concentration of hydrogen ions (H⁺) — the higher the H⁺ concentration, the lower the pH
- [ ] The total number of ions of any kind
    - *why wrong:* Only the H⁺ (and OH⁻) concentration sets the pH, not the total ion count.
- [ ] The concentration of sodium ions
    - *why wrong:* Sodium ions are spectators; pH depends on H⁺ concentration.
- [ ] The colour of the solution
    - *why wrong:* Colour does not set pH; the H⁺ concentration does.

**Q2. [apply] ⭐** The H⁺ concentration of a solution increases by a factor of 10. Deduce the change in pH.
- [✔︎] The pH falls by 1
- [ ] The pH rises by 1
    - *why wrong:* A higher H⁺ concentration is more acidic, so pH falls, not rises.
- [ ] The pH falls by 10
    - *why wrong:* A ten-fold change in H⁺ shifts pH by 1 unit, not 10.
- [ ] The pH stays the same
    - *why wrong:* pH tracks H⁺ concentration, so it must change.

**Q3. [apply]** The pH of a solution changes from 5 to 3. Deduce how the H⁺ concentration has changed.
- [✔︎] It has increased 100-fold
- [ ] It has increased 2-fold
    - *why wrong:* Each 1-unit fall in pH is a ×10 change; a 2-unit fall is 10×10 = 100-fold.
- [ ] It has decreased 100-fold
    - *why wrong:* A falling pH means MORE H⁺, so the concentration increases, not decreases.
- [ ] It has increased 20-fold
    - *why wrong:* The relationship is powers of 10: two pH units is ×100, not ×20.

**Q4. [reason]** Explain why adding an alkali to an acid raises the pH.
- [✔︎] The OH⁻ ions from the alkali react with H⁺ ions to form water, lowering the H⁺ concentration so the pH rises
- [ ] The alkali adds more H⁺ ions
    - *why wrong:* Alkalis provide OH⁻ ions, which remove H⁺; they do not add H⁺.
- [ ] The alkali dilutes the acid with extra water only
    - *why wrong:* Even undiluted, the OH⁻ ions chemically remove H⁺; it is not just dilution.
- [ ] The alkali heats the acid, raising the pH
    - *why wrong:* pH change here is due to OH⁻ neutralising H⁺, not temperature.

**Q5. [apply]** Predict the pH at the exact point where an acid has been completely neutralised by an alkali.
- [✔︎] 7 (neutral)
- [ ] 0 (strongly acidic)
    - *why wrong:* At exact neutralisation the acid is used up, giving a neutral pH of 7, not 0.
- [ ] 14 (strongly alkaline)
    - *why wrong:* Exact neutralisation leaves neither excess acid nor excess alkali, so pH is 7, not 14.
- [ ] It cannot be predicted
    - *why wrong:* Complete neutralisation of a strong acid by a strong alkali gives pH 7.

**Q6. [reason]** A pH probe and universal indicator are both used to measure pH. Explain one advantage of the pH probe.
- [✔︎] It gives a precise numerical pH value, rather than an estimate from matching a colour
- [ ] It changes colour more clearly than the indicator
    - *why wrong:* A probe does not use colour; its advantage is a precise number.
- [ ] It works only on acids, not alkalis
    - *why wrong:* A pH probe works across the whole scale; that is not an advantage anyway.
- [ ] It does not need the solution to be a liquid
    - *why wrong:* pH is measured in solution for both methods; the probe's advantage is precision.

**Q7. [apply]** Two acids have the same concentration, but acid A has pH 1 and acid B has pH 3. Deduce which has the higher H⁺ concentration.
- [✔︎] Acid A — a lower pH means a higher H⁺ concentration
- [ ] Acid B — a higher pH number means more H⁺
    - *why wrong:* A higher pH means FEWER H⁺ ions, so acid B has less, not more.
- [ ] They have equal H⁺ concentrations because the concentrations are equal
    - *why wrong:* Same concentration but different pH shows their H⁺ concentrations differ.
- [ ] It cannot be decided from pH
    - *why wrong:* pH directly reflects H⁺ concentration, so the lower-pH acid has more H⁺.

**Q8. [reason]** Explain why a neutral solution is not the same as a solution containing no ions.
- [✔︎] A neutral solution has equal (small) concentrations of H⁺ and OH⁻ ions — they balance, rather than being absent
- [ ] A neutral solution contains no H⁺ or OH⁻ ions at all
    - *why wrong:* Neutral means equal H⁺ and OH⁻, not zero ions.
- [ ] A neutral solution contains only OH⁻ ions
    - *why wrong:* Equal H⁺ and OH⁻ give neutrality; only OH⁻ would be alkaline.
- [ ] A neutral solution must be pure water
    - *why wrong:* Neutral salt solutions also have balanced H⁺ and OH⁻; it need not be pure water.

**Q9. [recall]** State the ion responsible for a solution being alkaline.
- [✔︎] The hydroxide ion, OH⁻
- [ ] The hydrogen ion, H⁺
    - *why wrong:* H⁺ ions make a solution acidic, not alkaline.
- [ ] The oxide ion, O²⁻
    - *why wrong:* Alkalinity in solution is due to OH⁻ ions, not free oxide ions.
- [ ] The sodium ion, Na⁺
    - *why wrong:* Sodium ions are spectators; OH⁻ ions cause alkalinity.

**Q10. [apply]** Equal volumes of equal-concentration hydrochloric acid and sodium hydroxide are mixed. Predict the pH of the mixture.
- [✔︎] About 7, because the acid and alkali exactly neutralise each other
- [ ] Below 7, because acid always wins
    - *why wrong:* Equal amounts of a strong acid and strong alkali neutralise fully to about pH 7.
- [ ] Above 7, because alkalis are stronger
    - *why wrong:* With equal amounts they neutralise each other, giving about pH 7.
- [ ] 14, because the two combine their pH values
    - *why wrong:* pH values are not added; equal neutralisation gives about pH 7.

### Triple Higher — 2 extra Higher/depth questions

_On top of the 10 above (so Triple Higher shows 12)._

**Q11. [reason] ⭐** As the concentration of H⁺ ions in a solution increases by a factor of 10, deduce how the pH changes.
- [✔︎] The pH decreases by 1
- [ ] The pH increases by 1
    - *why wrong:* More H⁺ means more acidic, so the pH goes DOWN, not up.
- [ ] The pH decreases by 10
    - *why wrong:* Each ten-fold rise in H⁺ changes pH by 1 unit, not 10.
- [ ] The pH does not change
    - *why wrong:* pH is a measure of H⁺ concentration, so it must change when H⁺ changes.

**Q12. [apply] ⭐** The pH of an acid falls from 4 to 2. Deduce how many times greater the H⁺ concentration becomes.
- [✔︎] 100 times greater
- [ ] 2 times greater
    - *why wrong:* Each drop of 1 pH unit is a ×10 change; a drop of 2 units is 10×10 = 100 times.
- [ ] 10 times greater
    - *why wrong:* That is the change for a drop of just 1 pH unit; here the pH falls by 2 units.
- [ ] 1000 times greater
    - *why wrong:* A drop of 2 pH units is ×100 (10²), not ×1000, which would be 3 units.

---

## Strong and Weak Acids  ·  `strong-weak-acids`  ·  AQA 5.4.2.5

> 🚩 **Triple-depth call (your review):** HIGHER-ONLY — AQA lists this content at Higher tier only, so there is no Foundation cell. Triple-Higher = the exact Combined-Higher set + 2 extra Higher/depth questions.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often treat 'strong' and 'concentrated' as the same word, so they call a concentrated acid 'strong'. They are different ideas. STRENGTH is about how fully the acid ionises: a strong acid is fully ionised, a weak acid only partly. CONCENTRATION is about how many moles are dissolved per dm³. So you can have a dilute strong acid (little HCl in lots of water) and a concentrated weak acid (lots of ethanoic acid) — the two properties are independent.

### Combined Higher — 10 questions

_There is no Foundation tier for this page. These 10 also appear verbatim in Triple Higher._

**Q1. [reason]** Define a strong acid in terms of ionisation.
- [✔︎] An acid that is completely ionised in aqueous solution
- [ ] An acid that is very concentrated
    - *why wrong:* That is concentration, not strength; strength is about complete ionisation.
- [ ] An acid that partly ionises in water
    - *why wrong:* Partial ionisation describes a WEAK acid; a strong acid is fully ionised.
- [ ] An acid with a pH above 7
    - *why wrong:* All acids have a pH below 7; strength is about how fully it ionises.

**Q2. [reason]** Define a weak acid in terms of ionisation.
- [✔︎] An acid that is only partially ionised in aqueous solution
- [ ] An acid that is very dilute
    - *why wrong:* That is concentration, not strength; a weak acid is only partly ionised.
- [ ] An acid that is completely ionised in water
    - *why wrong:* Complete ionisation describes a STRONG acid, not a weak one.
- [ ] An acid that does not react with metals
    - *why wrong:* Weak acids do react (just more slowly); the definition is partial ionisation.

**Q3. [apply]** Classify ethanoic acid (found in vinegar) as a strong or weak acid.
- [✔︎] Weak — it is only partially ionised in solution
- [ ] Strong — it is fully ionised
    - *why wrong:* Ethanoic acid only partly ionises, so it is a weak acid.
- [ ] Neither — it is neutral
    - *why wrong:* Ethanoic acid is acidic (pH below 7); it is a weak acid.
- [ ] It depends on how much water is added
    - *why wrong:* Dilution changes concentration, not strength; ethanoic acid is always weak.

**Q4. [apply]** Classify hydrochloric acid as a strong or weak acid.
- [✔︎] Strong — it is completely ionised in solution
- [ ] Weak — it only partly ionises
    - *why wrong:* Hydrochloric acid ionises completely, so it is a strong acid.
- [ ] Neither — it is a salt
    - *why wrong:* Hydrochloric acid is an acid, and it is fully ionised, so it is strong.
- [ ] It depends on the temperature
    - *why wrong:* Hydrochloric acid is a strong acid regardless of temperature.

**Q5. [reason]** Explain why a strong acid has a lower pH than a weak acid of the same concentration.
- [✔︎] The strong acid is fully ionised, so it releases more H⁺ ions, giving a higher H⁺ concentration and a lower pH
- [ ] The strong acid contains more acid molecules
    - *why wrong:* At the same concentration both have the same number of molecules; the strong one ionises more fully.
- [ ] The weak acid contains no hydrogen
    - *why wrong:* A weak acid does contain hydrogen; it simply releases fewer H⁺ ions.
- [ ] The strong acid is more concentrated
    - *why wrong:* They are at the SAME concentration; the difference is degree of ionisation.

**Q6. [reason]** Explain the difference between the concentration and the strength of an acid.
- [✔︎] Concentration is the number of moles of acid per dm³; strength is how completely the acid ionises in water
- [ ] They mean the same thing
    - *why wrong:* They are independent: one is amount per volume, the other is degree of ionisation.
- [ ] Concentration is degree of ionisation; strength is moles per dm³
    - *why wrong:* This is reversed — concentration is moles per dm³, strength is ionisation.
- [ ] Concentration applies to acids and strength to alkalis
    - *why wrong:* Both terms apply to acids; they describe different properties.

**Q7. [apply] ⭐** Solution X is 0.1 mol/dm³ and has pH 1; solution Y is 0.1 mol/dm³ and has pH 3. Deduce which is the stronger acid.
- [✔︎] Solution X — the same concentration but a lower pH means it is more fully ionised
- [ ] Solution Y — the higher pH shows it is stronger
    - *why wrong:* A higher pH means fewer H⁺ ions, so Y is the WEAKER acid.
- [ ] They are equally strong because the concentrations match
    - *why wrong:* Equal concentration but different pH shows different strengths.
- [ ] Neither — strength cannot be judged from pH
    - *why wrong:* At equal concentration, the lower-pH acid is the stronger one.

**Q8. [apply]** In the equation CH₃COOH ⇌ CH₃COO⁻ + H⁺, state what the ⇌ symbol tells you.
- [✔︎] The ionisation is reversible and only partial — the acid is weak
- [ ] The reaction goes fully to the right
    - *why wrong:* A full single arrow would show complete ionisation; ⇌ shows it is only partial.
- [ ] The acid does not ionise at all
    - *why wrong:* The ⇌ shows some ionisation occurs, just not complete ionisation.
- [ ] The acid is strong
    - *why wrong:* The reversible ⇌ arrow indicates partial ionisation, which is a WEAK acid.

**Q9. [reason]** Explain why it is possible to have both a concentrated weak acid and a dilute strong acid.
- [✔︎] Concentration (moles per dm³) and strength (degree of ionisation) are independent, so any combination of the two is possible
- [ ] It is not possible — weak acids are always dilute
    - *why wrong:* Strength and concentration are independent, so a weak acid can be concentrated.
- [ ] Strong acids can never be diluted
    - *why wrong:* Any acid can be diluted; diluting a strong acid keeps it strong but lowers concentration.
- [ ] Only strong acids can be concentrated
    - *why wrong:* Weak acids can be concentrated too; the two properties are unrelated.

**Q10. [recall]** Name the weak acid present in vinegar.
- [✔︎] Ethanoic acid
- [ ] Hydrochloric acid
    - *why wrong:* Hydrochloric acid is a strong acid and is not the acid in vinegar.
- [ ] Sulfuric acid
    - *why wrong:* Sulfuric acid is a strong acid, not the weak acid in vinegar.
- [ ] Nitric acid
    - *why wrong:* Nitric acid is a strong acid; the weak acid in vinegar is ethanoic acid.

### Triple Higher — 2 extra Higher/depth questions

_On top of the 10 above (so Triple Higher shows 12)._

**Q11. [apply] ⭐** A strong acid has pH 1 and a weak acid of the same concentration has pH 3. Deduce how many times greater the H⁺ concentration of the strong acid is.
- [✔︎] 100 times greater
- [ ] 2 times greater
    - *why wrong:* Each 1-unit pH difference is a ×10 factor; a difference of 2 units is 10×10 = 100 times.
- [ ] 3 times greater
    - *why wrong:* The factor is powers of 10, not the pH difference itself; 2 units means ×100.
- [ ] 10 times greater
    - *why wrong:* That is the factor for a 1-unit difference; here the pH differs by 2 units, so ×100.

**Q12. [reason]** Explain why a weak acid reacts more slowly than a strong acid of the same concentration with the same piece of magnesium.
- [✔︎] The weak acid is only partly ionised, so it has a lower H⁺ concentration, and a lower H⁺ concentration means a slower reaction
- [ ] The weak acid contains less acid overall
    - *why wrong:* At the same concentration both contain the same amount; the weak one releases fewer H⁺ ions.
- [ ] The weak acid is colder
    - *why wrong:* Temperature is not the factor here; the weak acid simply has fewer H⁺ ions available.
- [ ] The weak acid cannot react with magnesium at all
    - *why wrong:* It does react, just more slowly, because of its lower H⁺ concentration.

---

## Titrations  ·  `titrations`  ·  AQA 4.4.2.5

> 🚩 **Triple-depth call (your review):** TRIPLE-ONLY — AQA places this content on the Triple (separate sciences) pathway only, so there is no Combined cell. Foundation and Higher are authored as genuinely different difficulties (the Higher set adds the concentration calculations).

**Common Mistake (reformatted — ✅ mistake-first):**

> At the end point students often keep swirling and add 'just a bit more' to be sure, or stop the moment they see a flash of colour that then fades. Both spoil the titre. The end point is the moment ONE drop gives a PERMANENT colour change that does not fade on swirling — you stop exactly there. And when working out the mean, only concordant titres (within 0.10 cm³ of each other) are averaged; rough runs and outliers are left out.

**FIFA worked examples (Triple Foundation) — ⭐ full review:**

> **Working Out a Single Titre**  
> In a titration the initial burette reading is 0.50 cm³ and the final reading is 25.10 cm³. Calculate the titre.  
> &nbsp;&nbsp;**F** — Titre = final burette reading − initial burette reading  
> &nbsp;&nbsp;**I** — Titre = 25.10 − 0.50  
> &nbsp;&nbsp;**F** — = 24.60  
> &nbsp;&nbsp;**A** — Titre = 24.60 cm³  
>
> **Mean of Concordant Titres**  
> Three titres are recorded: 24.60, 24.55 and 24.65 cm³. All are concordant. Calculate the mean titre.  
> &nbsp;&nbsp;**F** — Mean = (sum of concordant titres) ÷ (number of titres)  
> &nbsp;&nbsp;**I** — Mean = (24.60 + 24.55 + 24.65) ÷ 3 = 73.80 ÷ 3  
> &nbsp;&nbsp;**F** — = 24.60  
> &nbsp;&nbsp;**A** — Mean titre = 24.60 cm³  
>
> **Discarding an Outlier**  
> A student records titres of 22.40, 23.10, 23.15 and 23.05 cm³. Calculate the mean titre.  
> &nbsp;&nbsp;**F** — First identify concordant results (within 0.10 cm³); discard any outlier  
> &nbsp;&nbsp;**I** — Concordant: 23.10, 23.15, 23.05. Discard 22.40 (a rough run, too far from the others)  
> &nbsp;&nbsp;**F** — Mean = (23.10 + 23.15 + 23.05) ÷ 3 = 69.30 ÷ 3  
> &nbsp;&nbsp;**A** — Mean titre = 23.10 cm³  
>

### Triple Foundation — 12 questions

_There is no Combined tier for this page. Foundation focuses on the practical technique._

**Q1. [recall]** State the purpose of a titration.
- [✔︎] To find the exact volumes of acid and alkali that react together completely
- [ ] To measure the temperature change of a reaction
    - *why wrong:* That is calorimetry; a titration finds reacting volumes.
- [ ] To separate a salt from its solution
    - *why wrong:* That is crystallisation; a titration measures reacting volumes.
- [ ] To measure how fast a reaction happens
    - *why wrong:* That is a rate experiment; a titration finds the volumes that exactly react.

**Q2. [recall]** Name the piece of apparatus used to add the acid a little at a time during a titration.
- [✔︎] A burette
- [ ] A pipette
    - *why wrong:* A pipette measures one fixed volume of the other solution; the burette delivers the acid gradually.
- [ ] A measuring cylinder
    - *why wrong:* A measuring cylinder is not accurate enough and cannot deliver drop by drop; a burette is used.
- [ ] A conical flask
    - *why wrong:* The conical flask holds the solution being tested; the burette adds the acid.

**Q3. [apply]** State why a pipette, rather than a measuring cylinder, is used to measure the alkali into the conical flask.
- [✔︎] A pipette measures a fixed volume much more accurately
- [ ] A pipette can hold a larger volume
    - *why wrong:* Accuracy, not volume, is the reason a pipette is chosen.
- [ ] A pipette adds the solution drop by drop
    - *why wrong:* That is the burette's job; the pipette delivers one accurate fixed volume.
- [ ] A pipette changes colour at the end point
    - *why wrong:* The indicator shows the end point; the pipette is used for accurate measuring.

**Q4. [apply]** Name a suitable indicator for a titration.
- [✔︎] Phenolphthalein (or methyl orange)
- [ ] Universal indicator
    - *why wrong:* Universal indicator changes through many colours, so the end point is unclear; a single indicator is used.
- [ ] Limewater
    - *why wrong:* Limewater is a test for carbon dioxide, not a titration indicator.
- [ ] Litmus solution
    - *why wrong:* Litmus gives a vague colour change; phenolphthalein or methyl orange give a sharp end point.

**Q5. [apply] ⭐** The initial burette reading is 1.20 cm³ and the final reading is 26.70 cm³. Calculate the titre.
- [✔︎] 25.50 cm³
- [ ] 27.90 cm³
    - *why wrong:* You should subtract, not add, the readings: 26.70 − 1.20.
- [ ] 26.70 cm³
    - *why wrong:* You must subtract the initial reading (1.20) from the final reading.
- [ ] 1.20 cm³
    - *why wrong:* The titre is the difference between the readings, not the initial reading.

**Q6. [reason]** Explain how you know you have reached the end point of the titration.
- [✔︎] One further drop produces a permanent colour change that does not fade when the flask is swirled
- [ ] The solution starts to fizz
    - *why wrong:* There is no gas in an acid-alkali titration; the end point is a permanent colour change.
- [ ] The colour flashes and then disappears
    - *why wrong:* A flash that fades means you are not there yet; the change must be permanent.
- [ ] The burette becomes empty
    - *why wrong:* The end point is judged by the colour change, not by emptying the burette.

**Q7. [recall] ⭐** State what is meant by concordant titres.
- [✔︎] Titres that are within 0.10 cm³ of each other
- [ ] Titres that are all exactly the same to the nearest whole number
    - *why wrong:* Concordant means within 0.10 cm³, which is more precise than the nearest whole number.
- [ ] The very first two titres recorded
    - *why wrong:* Being first does not make results concordant; they must agree within 0.10 cm³.
- [ ] Titres taken from different students
    - *why wrong:* Concordant refers to close agreement (within 0.10 cm³), not who took them.

**Q8. [apply]** State why a titration is repeated several times.
- [✔︎] To obtain concordant results so a reliable mean titre can be calculated
- [ ] To use up the leftover acid
    - *why wrong:* Repeats are for reliability, not to use up chemicals.
- [ ] To make the reaction go faster
    - *why wrong:* Repeating does not change the rate; it improves reliability.
- [ ] To change the indicator each time
    - *why wrong:* The same indicator is used; repeats give concordant results for a reliable mean.

**Q9. [apply] ⭐** Explain why the first, rough titration is usually not included when working out the mean titre.
- [✔︎] The rough run is only an approximate guide, so it is usually not concordant with the accurate runs
- [ ] The rough run uses a different acid
    - *why wrong:* The same acid is used throughout; the rough run is simply less accurate.
- [ ] The rough run is always the most accurate
    - *why wrong:* The rough run is the least accurate; that is why it is excluded.
- [ ] The rough run does not use an indicator
    - *why wrong:* An indicator is used every time; the rough run is excluded for being approximate.

**Q10. [apply]** State why the conical flask is swirled continuously during the titration.
- [✔︎] To mix the acid and alkali thoroughly so the reaction keeps up as acid is added
- [ ] To warm the mixture up
    - *why wrong:* Swirling does not heat the flask; it mixes the reactants.
- [ ] To speed up the crystallisation of the salt
    - *why wrong:* No crystals form during a titration; swirling ensures thorough mixing.
- [ ] To stop the indicator from working
    - *why wrong:* Swirling helps the indicator show the true end point by mixing the solution.

**Q11. [apply]** State why the acid is run in quickly at first and then added drop by drop near the end point.
- [✔︎] To save time early on, then to avoid adding too much and overshooting the exact end point
- [ ] To warm the flask before the reaction
    - *why wrong:* The change of pace is about accuracy at the end point, not warming.
- [ ] To make more salt form in the flask
    - *why wrong:* The pace is about hitting the end point precisely, not making more salt.
- [ ] Because the burette empties faster near the end
    - *why wrong:* The slow drop-wise addition near the end is to avoid overshooting, not about how fast it empties.

**Q12. [recall]** State which part of the liquid in the burette you line up with the scale when taking a reading.
- [✔︎] The bottom of the meniscus (the curved surface of the liquid)
- [ ] The top of the meniscus
    - *why wrong:* Readings are taken from the BOTTOM of the meniscus, consistently, not the top.
- [ ] The middle of the burette tube
    - *why wrong:* You read the liquid level at the bottom of the meniscus, not a fixed point on the tube.
- [ ] Wherever the colour change appears
    - *why wrong:* The colour change signals the end point; the reading is taken at the bottom of the meniscus.

**FIFA worked examples (Triple Higher) — ⭐ full review:**

> **Concentration from a Titration (1:1)**  
> 25.0 cm³ of sodium hydroxide is exactly neutralised by 20.0 cm³ of 0.100 mol/dm³ hydrochloric acid. NaOH + HCl → NaCl + H₂O. Calculate the concentration of the sodium hydroxide.  
> &nbsp;&nbsp;**F** — moles = concentration × volume (in dm³); use the 1:1 ratio; concentration = moles ÷ volume  
> &nbsp;&nbsp;**I** — moles HCl = 0.100 × (20.0 ÷ 1000) = 0.00200 mol; ratio 1:1 so moles NaOH = 0.00200 mol  
> &nbsp;&nbsp;**F** — concentration NaOH = 0.00200 ÷ (25.0 ÷ 1000) = 0.00200 ÷ 0.0250  
> &nbsp;&nbsp;**A** — Concentration = 0.0800 mol/dm³  
>
> **Converting mol/dm³ to g/dm³**  
> The sodium hydroxide solution above has a concentration of 0.0800 mol/dm³. Calculate its concentration in g/dm³. (Ar: Na = 23, O = 16, H = 1)  
> &nbsp;&nbsp;**F** — concentration in g/dm³ = concentration in mol/dm³ × relative formula mass (Mr)  
> &nbsp;&nbsp;**I** — Mr of NaOH = 23 + 16 + 1 = 40; so 0.0800 × 40  
> &nbsp;&nbsp;**F** — = 3.2  
> &nbsp;&nbsp;**A** — Concentration = 3.2 g/dm³  
>
> **Using a 1:2 Ratio to Find a Volume**  
> 25.0 cm³ of 0.100 mol/dm³ sulfuric acid is neutralised by 0.200 mol/dm³ sodium hydroxide. H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O. Calculate the volume of sodium hydroxide needed.  
> &nbsp;&nbsp;**F** — moles acid = c × V; use the 1:2 ratio for NaOH; volume = moles ÷ concentration  
> &nbsp;&nbsp;**I** — moles H₂SO₄ = 0.100 × (25.0 ÷ 1000) = 0.00250 mol; moles NaOH = 2 × 0.00250 = 0.00500 mol  
> &nbsp;&nbsp;**F** — volume NaOH = 0.00500 ÷ 0.200 = 0.0250 dm³  
> &nbsp;&nbsp;**A** — Volume = 0.0250 dm³ = 25.0 cm³  
>

### Triple Higher — 12 questions

_A genuinely harder set: adds the concentration calculations._

**Q1. [recall]** Name the piece of apparatus used to deliver the acid drop by drop in a titration.
- [✔︎] A burette
- [ ] A pipette
    - *why wrong:* A pipette delivers one fixed volume; the burette adds acid gradually and is read at the end.
- [ ] A measuring cylinder
    - *why wrong:* A measuring cylinder is too imprecise; a burette is used for accurate, drop-wise addition.
- [ ] A gas syringe
    - *why wrong:* A gas syringe collects gas; the burette delivers the acid in a titration.

**Q2. [apply]** Explain why a single indicator such as phenolphthalein is used in a titration rather than universal indicator.
- [✔︎] It gives one sharp colour change at the end point, whereas universal indicator changes through several colours
- [ ] It is cheaper than universal indicator
    - *why wrong:* The reason is a sharp single colour change, not cost.
- [ ] It works only with strong acids
    - *why wrong:* Phenolphthalein works with strong acid-alkali titrations; the point is its clear end point.
- [ ] It measures the exact pH value
    - *why wrong:* An indicator shows the end point by colour; a single indicator gives a sharp change.

**Q3. [apply] ⭐** 25.0 cm³ of sodium hydroxide is neutralised by 20.0 cm³ of 0.100 mol/dm³ hydrochloric acid (1:1). Calculate the moles of hydrochloric acid used.
- [✔︎] 0.00200 mol
- [ ] 0.00250 mol
    - *why wrong:* Use moles = c × V(dm³) = 0.100 × (20.0÷1000) = 0.00200, not 0.00250.
- [ ] 2.00 mol
    - *why wrong:* The volume must be converted to dm³ (÷1000): 0.100 × 0.0200 = 0.00200 mol.
- [ ] 0.0800 mol
    - *why wrong:* That is closer to a concentration value; moles HCl = 0.100 × 0.0200 = 0.00200 mol.

**Q4. [apply] ⭐** In the titration above, the moles of hydrochloric acid are 0.00200 mol and the reaction is 1:1. Calculate the concentration of the 25.0 cm³ of sodium hydroxide.
- [✔︎] 0.0800 mol/dm³
- [ ] 0.0500 mol/dm³
    - *why wrong:* Divide moles by volume in dm³: 0.00200 ÷ 0.0250 = 0.0800, not 0.0500.
- [ ] 0.00200 mol/dm³
    - *why wrong:* 0.00200 is the moles; divide by the volume (0.0250 dm³) to get concentration.
- [ ] 1.25 mol/dm³
    - *why wrong:* Divide moles by volume, not volume by moles: 0.00200 ÷ 0.0250 = 0.0800 mol/dm³.

**Q5. [apply] ⭐** A solution has a concentration of 0.0800 mol/dm³ sodium hydroxide (Mr = 40). Calculate its concentration in g/dm³.
- [✔︎] 3.2 g/dm³
- [ ] 0.002 g/dm³
    - *why wrong:* Multiply concentration by Mr: 0.0800 × 40 = 3.2 g/dm³.
- [ ] 40 g/dm³
    - *why wrong:* That is just the Mr; multiply it by the concentration: 0.0800 × 40 = 3.2.
- [ ] 320 g/dm³
    - *why wrong:* 0.0800 × 40 = 3.2, not 320 — check the decimal place.

**Q6. [apply] ⭐** In H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O, 0.00250 mol of sulfuric acid is used. Calculate the moles of sodium hydroxide that react.
- [✔︎] 0.00500 mol
- [ ] 0.00250 mol
    - *why wrong:* The ratio is 1:2, so twice as much NaOH reacts: 2 × 0.00250 = 0.00500 mol.
- [ ] 0.00125 mol
    - *why wrong:* That halves the acid; the 1:2 ratio means you DOUBLE it to 0.00500 mol.
- [ ] 0.0100 mol
    - *why wrong:* The ratio is 1:2, giving 2 × 0.00250 = 0.00500 mol, not four times.

**Q7. [reason] ⭐** Explain why the volumes must be converted from cm³ to dm³ before calculating a concentration in mol/dm³.
- [✔︎] Concentration in mol/dm³ uses volume in dm³, so cm³ must be divided by 1000 to match the units
- [ ] Because dm³ is larger, so the numbers look neater
    - *why wrong:* It is a units requirement, not about neatness: mol/dm³ needs dm³.
- [ ] Because cm³ cannot be used in any calculation
    - *why wrong:* cm³ is fine elsewhere; it is converted here because the unit mol/dm³ requires dm³.
- [ ] Because the burette is marked in dm³
    - *why wrong:* Burettes are marked in cm³; the conversion is because the concentration unit uses dm³.

**Q8. [apply] ⭐** A titre needs 0.00500 mol of sodium hydroxide at a concentration of 0.200 mol/dm³. Calculate the volume of sodium hydroxide required.
- [✔︎] 0.0250 dm³ (25.0 cm³)
- [ ] 0.00100 dm³
    - *why wrong:* Use volume = moles ÷ concentration = 0.00500 ÷ 0.200 = 0.0250 dm³, not 0.00100.
- [ ] 0.0400 dm³
    - *why wrong:* Divide moles by concentration: 0.00500 ÷ 0.200 = 0.0250 dm³.
- [ ] 0.100 dm³
    - *why wrong:* 0.00500 ÷ 0.200 = 0.0250 dm³; 0.100 dm³ is four times too large.

**Q9. [reason] ⭐** Explain why only concordant titres are used to calculate the mean titre.
- [✔︎] Concordant titres agree within 0.10 cm³, so they are reliable; including a rough or anomalous run would make the mean less accurate
- [ ] Concordant titres are always the largest values
    - *why wrong:* Concordant means close agreement, not largest; anomalies are excluded for accuracy.
- [ ] Using all the titres would take too long
    - *why wrong:* It is about accuracy, not time; anomalous runs would distort the mean.
- [ ] Non-concordant titres use a different indicator
    - *why wrong:* The same indicator is used; non-concordant runs are excluded because they are unreliable.

**Q10. [apply]** Explain why the tip of the burette should be filled with solution (no air bubble) before the titration begins.
- [✔︎] An air bubble that leaves during the titration would add to the apparent titre, making the reading too large
- [ ] An air bubble would change the colour of the indicator
    - *why wrong:* The bubble does not affect the indicator; it makes the volume reading inaccurate.
- [ ] An air bubble would slow the reaction down
    - *why wrong:* The issue is an inaccurate titre volume, not the reaction rate.
- [ ] An air bubble would neutralise some of the acid
    - *why wrong:* Air does not neutralise acid; a bubble leaving the tip inflates the measured titre.

**Q11. [reason]** Explain why burette readings are taken at eye level with the bottom of the meniscus.
- [✔︎] To avoid parallax error, so the volume is read accurately and consistently each time
- [ ] To make the reading look larger
    - *why wrong:* Eye-level reading is for accuracy, not to change the apparent value.
- [ ] To warm the solution to room temperature
    - *why wrong:* Reading position has nothing to do with temperature; it prevents parallax error.
- [ ] Because the burette only works at eye level
    - *why wrong:* The burette works at any angle of viewing; eye-level reading simply avoids parallax error.

**Q12. [apply] ⭐** 25.0 cm³ of 0.0500 mol/dm³ sodium hydroxide is exactly neutralised by 20.0 cm³ of hydrochloric acid (1:1). Calculate the concentration of the acid.
- [✔︎] 0.0625 mol/dm³
- [ ] 0.0400 mol/dm³
    - *why wrong:* Find moles NaOH = 0.0500 × 0.0250 = 0.00125, then divide by 0.0200 dm³ = 0.0625, not 0.0400.
- [ ] 0.0500 mol/dm³
    - *why wrong:* The acid volume (20.0 cm³) differs from the alkali volume, so the concentration is not the same 0.0500.
- [ ] 0.00125 mol/dm³
    - *why wrong:* 0.00125 is the number of moles; divide by the acid volume (0.0200 dm³) to get 0.0625 mol/dm³.

---

## The Process of Electrolysis  ·  `electrolysis-principles`  ·  AQA 5.4.3.1

> 🚩 **Triple-depth call (your review):** MATCHED — this AQA sub-topic is identical for Combined and Triple. Foundation difficulty is the same across both pathways; each Triple set = the Combined set + extra same-difficulty coverage. No AQA Triple-only content on this page.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often mix up which electrode is which, guessing the cathode is positive because 'cations go to it'. The cathode is the NEGATIVE electrode — it is exactly because it is negative that the positive ions (cations) are drawn to it. The anode is the POSITIVE electrode, which attracts the negative ions (anions). A useful check: AN OX (ANode = OXidation) and RED CAT (REDuction at the CAThode).

### Combined Foundation — 10 questions

_These 10 also appear verbatim in Triple Foundation._

**Q1. [recall]** State what is meant by electrolysis.
- [✔︎] Using an electric current to break down an ionic compound into its elements
- [ ] Using heat to break down a compound
    - *why wrong:* Breaking down by heat is thermal decomposition; electrolysis uses an electric current.
- [ ] Dissolving a compound in water
    - *why wrong:* Dissolving alone is not electrolysis; electrolysis passes a current to break the compound down.
- [ ] Mixing two solutions to form a solid
    - *why wrong:* That is precipitation; electrolysis splits a compound using electricity.

**Q2. [recall]** Name the negative electrode used in electrolysis.
- [✔︎] The cathode
- [ ] The anode
    - *why wrong:* The anode is the POSITIVE electrode; the negative one is the cathode.
- [ ] The electrolyte
    - *why wrong:* The electrolyte is the substance being broken down, not an electrode.
- [ ] The cation
    - *why wrong:* A cation is a positive ion, not an electrode.

**Q3. [recall]** Name the positive electrode used in electrolysis.
- [✔︎] The anode
- [ ] The cathode
    - *why wrong:* The cathode is the NEGATIVE electrode; the positive one is the anode.
- [ ] The electrolyte
    - *why wrong:* The electrolyte is the substance broken down, not an electrode.
- [ ] The anion
    - *why wrong:* An anion is a negative ion, not an electrode.

**Q4. [recall]** State what is meant by an electrolyte.
- [✔︎] A molten or dissolved ionic compound that conducts electricity and is broken down
- [ ] A metal wire that carries the current
    - *why wrong:* The wires are conductors; the electrolyte is the ionic liquid being broken down.
- [ ] A gas produced at an electrode
    - *why wrong:* The electrolyte is the starting substance, not a product gas.
- [ ] A solid ionic compound
    - *why wrong:* A solid ionic compound cannot conduct; the electrolyte must be molten or dissolved.

**Q5. [reason]** Explain why an ionic compound must be molten or dissolved before it can be electrolysed.
- [✔︎] Its ions must be free to move to the electrodes, which only happens when it is molten or dissolved
- [ ] The heat is needed to start the current
    - *why wrong:* It is the freeing of the ions, not heat itself, that allows electrolysis.
- [ ] Water is always needed to break the bonds
    - *why wrong:* Molten compounds contain no water yet can be electrolysed; the key is mobile ions.
- [ ] Solid compounds have no ions
    - *why wrong:* Solids do contain ions, but the ions are locked in place and cannot move.

**Q6. [apply]** State which electrode positive ions move towards during electrolysis.
- [✔︎] The cathode (the negative electrode)
- [ ] The anode (the positive electrode)
    - *why wrong:* Positive ions are attracted to the NEGATIVE electrode, the cathode, not the anode.
- [ ] Neither — positive ions do not move
    - *why wrong:* Positive ions do move; they are attracted to the negative cathode.
- [ ] Both electrodes equally
    - *why wrong:* Opposite charges attract, so positive ions move specifically to the negative cathode.

**Q7. [apply]** State which electrode negative ions move towards during electrolysis.
- [✔︎] The anode (the positive electrode)
- [ ] The cathode (the negative electrode)
    - *why wrong:* Negative ions are attracted to the POSITIVE electrode, the anode, not the cathode.
- [ ] Neither — negative ions stay still
    - *why wrong:* Negative ions do move; they are attracted to the positive anode.
- [ ] Both electrodes equally
    - *why wrong:* Opposite charges attract, so negative ions move specifically to the positive anode.

**Q8. [reason]** Explain why solid sodium chloride does not conduct electricity but molten sodium chloride does.
- [✔︎] In the solid the ions are locked in a fixed lattice; when molten the ions are free to move and carry charge
- [ ] Solid sodium chloride has no ions until it melts
    - *why wrong:* The ions exist in the solid too; they are simply not free to move.
- [ ] Melting adds electrons that carry the current
    - *why wrong:* No electrons are added; melting frees the existing ions to move.
- [ ] Solid sodium chloride is a metal
    - *why wrong:* Sodium chloride is an ionic compound, not a metal; conduction needs mobile ions.

**Q9. [recall]** State what type of substance is produced at the electrodes during electrolysis.
- [✔︎] Elements
- [ ] More of the same compound
    - *why wrong:* Electrolysis breaks the compound down into its elements, not more compound.
- [ ] Only gases
    - *why wrong:* The products are elements, which may be solids (metals) as well as gases.
- [ ] New compounds with the electrodes
    - *why wrong:* The products are the elements of the electrolyte, not new compounds.

**Q10. [apply]** Identify what carries the electric charge through the molten or dissolved electrolyte.
- [✔︎] Moving ions
- [ ] Moving electrons
    - *why wrong:* Electrons carry charge in the wires; inside the electrolyte the charge is carried by moving ions.
- [ ] Moving atoms
    - *why wrong:* Neutral atoms carry no charge; it is the charged ions that move through the electrolyte.
- [ ] The electrodes themselves
    - *why wrong:* The electrodes stay in place; the charge through the liquid is carried by ions.

### Triple Foundation — 2 extra Foundation-level questions

_On top of the 10 above (so Triple Foundation shows 12)._

**Q11. [recall]** Name the substance that is broken down during electrolysis.
- [✔︎] The electrolyte
- [ ] The electrode
    - *why wrong:* The electrode carries the current in; the substance broken down is the electrolyte.
- [ ] The cathode
    - *why wrong:* The cathode is an electrode, not the substance broken down.
- [ ] The circuit
    - *why wrong:* The circuit delivers the current; the electrolyte is what is broken down.

**Q12. [apply]** State whether electrolysis is used to break down ionic compounds or covalent (molecular) compounds.
- [✔︎] Ionic compounds, because they contain ions that can move and be discharged
- [ ] Covalent compounds, because they share electrons
    - *why wrong:* Covalent molecules have no ions to move; electrolysis breaks down ionic compounds.
- [ ] Both equally well
    - *why wrong:* Only compounds with mobile ions (ionic, molten or dissolved) can be electrolysed.
- [ ] Only pure metals
    - *why wrong:* Pure metals are elements already; electrolysis breaks down ionic compounds.

### Combined Higher — 10 questions

_A different, harder set from Foundation. These 10 also appear verbatim in Triple Higher._

**Q1. [reason]** Explain what must be true of an ionic compound before it can be electrolysed.
- [✔︎] Its ions must be free to move, which requires it to be molten or dissolved in water
- [ ] It must be a solid so the ions stay in place
    - *why wrong:* Fixed ions cannot move to the electrodes; the compound must be molten or dissolved.
- [ ] It must be a covalent compound
    - *why wrong:* Covalent compounds have no ions; electrolysis needs mobile ions from an ionic compound.
- [ ] It must first be heated until it glows
    - *why wrong:* It is mobile ions, not glowing, that is required — dissolving works without melting.

**Q2. [apply]** During electrolysis, predict which electrode the positive ions move to and state what happens to them there.
- [✔︎] They move to the cathode and gain electrons (are reduced)
- [ ] They move to the anode and lose electrons
    - *why wrong:* Positive ions go to the negative cathode and GAIN electrons, not to the anode to lose them.
- [ ] They move to the cathode and lose electrons
    - *why wrong:* At the cathode positive ions gain electrons; losing electrons happens to negative ions at the anode.
- [ ] They stay in the middle and share electrons
    - *why wrong:* Positive ions travel to the cathode and are discharged by gaining electrons.

**Q3. [reason]** Explain why the cathode is described as the negative electrode.
- [✔︎] It is connected to the negative terminal of the supply, so it attracts the positive ions
- [ ] It is where negative ions are discharged
    - *why wrong:* Negative ions are discharged at the positive anode; the cathode is negative and attracts positive ions.
- [ ] It produces electrons by breaking down
    - *why wrong:* The cathode does not create electrons; it is negative because of the power supply.
- [ ] It is made of a negative metal
    - *why wrong:* Electrode charge comes from the power supply's terminal, not the metal itself.

**Q4. [reason]** Explain, in terms of electrons, what happens to negative ions at the anode.
- [✔︎] They lose electrons to the anode and are oxidised
- [ ] They gain electrons and are reduced
    - *why wrong:* At the anode negative ions LOSE electrons (oxidation); gaining happens at the cathode.
- [ ] They gain protons and become neutral
    - *why wrong:* Discharge involves electrons, not protons; negative ions lose electrons at the anode.
- [ ] They pass straight into the wire unchanged
    - *why wrong:* They are chemically changed at the anode — they lose electrons and become atoms/molecules.

**Q5. [apply]** Classify the change that happens to ions at the cathode as oxidation or reduction.
- [✔︎] Reduction — the ions gain electrons
- [ ] Oxidation — the ions lose electrons
    - *why wrong:* Losing electrons is oxidation and happens at the anode; the cathode is where ions gain electrons.
- [ ] Neither — no electrons are transferred
    - *why wrong:* Electrons are transferred at both electrodes; at the cathode ions gain them (reduction).
- [ ] Both oxidation and reduction together
    - *why wrong:* A single electrode does one or the other; the cathode does reduction.

**Q6. [apply]** Classify the change that happens to ions at the anode as oxidation or reduction.
- [✔︎] Oxidation — the ions lose electrons
- [ ] Reduction — the ions gain electrons
    - *why wrong:* Gaining electrons is reduction and happens at the cathode; the anode is where ions lose electrons.
- [ ] Neither — the anode is inert
    - *why wrong:* Even an inert anode is where negative ions lose electrons — that is oxidation.
- [ ] Both oxidation and reduction together
    - *why wrong:* A single electrode does one or the other; the anode does oxidation.

**Q7. [reason]** Explain why a solid ionic lattice cannot be electrolysed.
- [✔︎] The ions are held in fixed positions in the lattice, so they cannot move to the electrodes to be discharged
- [ ] The lattice contains no charged particles
    - *why wrong:* The lattice is made of ions (charged particles); they are simply not free to move.
- [ ] Solids cannot conduct any form of energy
    - *why wrong:* Solids can conduct heat and some conduct electricity (metals); the issue is fixed ions.
- [ ] The electrodes cannot touch a solid
    - *why wrong:* Electrodes can touch a solid; electrolysis fails because the ions cannot move.

**Q8. [recall]** State what is meant by an electrolyte.
- [✔︎] A molten or dissolved ionic compound that conducts electricity during electrolysis
- [ ] The wire connecting the electrodes to the supply
    - *why wrong:* That wire is a conductor; the electrolyte is the ionic liquid being decomposed.
- [ ] The positive electrode
    - *why wrong:* The positive electrode is the anode; the electrolyte is the substance broken down.
- [ ] A compound that shares electrons
    - *why wrong:* Electron-sharing describes covalent bonding; an electrolyte is an ionic conductor.

**Q9. [reason]** Use 'AN OX' and 'RED CAT' to state where oxidation takes place in electrolysis.
- [✔︎] At the anode — 'AN OX' means ANode = OXidation
- [ ] At the cathode
    - *why wrong:* 'RED CAT' shows the cathode is reduction; oxidation ('AN OX') is at the anode.
- [ ] In the electrolyte, not at an electrode
    - *why wrong:* Oxidation happens at the anode surface, where ions lose electrons.
- [ ] At both electrodes equally
    - *why wrong:* Oxidation is at the anode; reduction is at the cathode — not both at each.

**Q10. [apply]** The electrodes are labelled + and −. Deduce the direction that the negative ions travel.
- [✔︎] Towards the + electrode (the anode)
- [ ] Towards the − electrode (the cathode)
    - *why wrong:* Negative ions are repelled by the − electrode and attracted to the + anode.
- [ ] They do not move because they are negative
    - *why wrong:* Negative ions do move — they are attracted to the positive electrode.
- [ ] They move to whichever electrode is nearer
    - *why wrong:* Movement is set by charge, not distance: negative ions go to the positive anode.

### Triple Higher — 2 extra Higher/depth questions

_On top of the 10 above (so Triple Higher shows 12)._

**Q11. [reason]** Explain, in terms of electrons, what happens to positive metal ions when they reach the cathode.
- [✔︎] They gain electrons from the cathode and are reduced to neutral metal atoms
- [ ] They lose electrons and are oxidised
    - *why wrong:* At the cathode positive ions GAIN electrons (reduction), they do not lose them.
- [ ] They gain protons to become neutral
    - *why wrong:* Ions are discharged by gaining electrons, not protons; the nucleus is unchanged.
- [ ] They simply stick to the electrode unchanged
    - *why wrong:* They are chemically changed — they gain electrons and become atoms.

**Q12. [reason]** Explain why electrons flow through the external wires while ions carry the charge inside the electrolyte.
- [✔︎] Metal wires contain free electrons that can move, but the electrolyte has no free electrons — its charge is carried by moving ions instead
- [ ] Ions can travel through metal wires as well
    - *why wrong:* Ions cannot move through solid metal wires; only the free electrons do.
- [ ] Electrons move through the electrolyte too
    - *why wrong:* The electrolyte carries charge by ion movement, not by free electrons.
- [ ] The wires contain ions and the electrolyte contains electrons
    - *why wrong:* It is the reverse: wires carry electrons, the electrolyte carries ions.

---

## Electrolysis of Molten Ionic Compounds  ·  `electrolysis-molten`  ·  AQA 5.4.3.2

> 🚩 **Triple-depth call (your review):** MATCHED — this AQA sub-topic is identical for Combined and Triple. Foundation difficulty is the same across both pathways; each Triple set = the Combined set + extra same-difficulty coverage. No AQA Triple-only content on this page.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often guess the products the wrong way round, putting the non-metal at the cathode. In a molten ionic compound the METAL always forms at the CATHODE (the negative electrode), because the positive metal ions are attracted there and gain electrons. The NON-METAL always forms at the ANODE (the positive electrode), because the negative non-metal ions are attracted there and lose electrons.

### Combined Foundation — 10 questions

_These 10 also appear verbatim in Triple Foundation._

**Q1. [apply]** Predict the product formed at the cathode when molten lead bromide is electrolysed.
- [✔︎] Lead (the metal)
- [ ] Bromine (the non-metal)
    - *why wrong:* Bromine, the non-metal, forms at the ANODE; the metal lead forms at the cathode.
- [ ] Hydrogen
    - *why wrong:* There is no water in a molten compound, so no hydrogen forms; the metal lead is produced.
- [ ] Lead bromide
    - *why wrong:* Electrolysis breaks the compound down; lead metal, not lead bromide, forms at the cathode.

**Q2. [apply]** Predict the product formed at the anode when molten lead bromide is electrolysed.
- [✔︎] Bromine (the non-metal)
- [ ] Lead (the metal)
    - *why wrong:* The metal lead forms at the CATHODE; the non-metal bromine forms at the anode.
- [ ] Oxygen
    - *why wrong:* There is no oxygen source in molten lead bromide; the non-metal bromine is produced.
- [ ] Hydrogen
    - *why wrong:* There is no water present, so no hydrogen forms; bromine forms at the anode.

**Q3. [recall]** State where the metal is always produced when a molten ionic compound is electrolysed.
- [✔︎] At the cathode (the negative electrode)
- [ ] At the anode (the positive electrode)
    - *why wrong:* The anode produces the non-metal; the metal forms at the negative cathode.
- [ ] In the electrolyte, not at an electrode
    - *why wrong:* The metal is deposited at the cathode surface, not in the middle of the liquid.
- [ ] At both electrodes
    - *why wrong:* The metal forms only at the cathode; the non-metal forms at the anode.

**Q4. [recall]** State where the non-metal is always produced when a molten ionic compound is electrolysed.
- [✔︎] At the anode (the positive electrode)
- [ ] At the cathode (the negative electrode)
    - *why wrong:* The cathode produces the metal; the non-metal forms at the positive anode.
- [ ] In the wires of the circuit
    - *why wrong:* The non-metal forms at the anode surface, not in the wires.
- [ ] At both electrodes
    - *why wrong:* The non-metal forms only at the anode; the metal forms at the cathode.

**Q5. [apply]** Predict the product at the cathode when molten sodium chloride is electrolysed.
- [✔︎] Sodium
- [ ] Chlorine
    - *why wrong:* Chlorine, the non-metal, forms at the anode; sodium (the metal) forms at the cathode.
- [ ] Hydrogen
    - *why wrong:* There is no water in molten sodium chloride, so sodium metal forms, not hydrogen.
- [ ] Sodium chloride
    - *why wrong:* The compound is broken down; sodium metal is produced at the cathode.

**Q6. [apply]** Predict the product at the anode when molten sodium chloride is electrolysed.
- [✔︎] Chlorine
- [ ] Sodium
    - *why wrong:* Sodium, the metal, forms at the cathode; chlorine (the non-metal) forms at the anode.
- [ ] Oxygen
    - *why wrong:* Molten sodium chloride contains no oxygen; chlorine forms at the anode.
- [ ] Hydrogen
    - *why wrong:* There is no water present, so hydrogen cannot form; chlorine forms at the anode.

**Q7. [reason]** Explain why the ionic compound must be molten for this electrolysis to work.
- [✔︎] Melting frees the ions so they can move to the electrodes and be discharged
- [ ] Melting adds electrons that carry the current
    - *why wrong:* No electrons are added; melting simply frees the existing ions to move.
- [ ] Melting turns the compound into a metal
    - *why wrong:* Melting does not change it into a metal; it frees the ions to move.
- [ ] Melting removes the non-metal first
    - *why wrong:* Both ions remain; melting just allows them to move to the electrodes.

**Q8. [apply]** Predict the two elements formed when molten potassium iodide is electrolysed.
- [✔︎] Potassium at the cathode and iodine at the anode
- [ ] Iodine at the cathode and potassium at the anode
    - *why wrong:* This is reversed — the metal (potassium) forms at the cathode, the non-metal (iodine) at the anode.
- [ ] Hydrogen and oxygen
    - *why wrong:* There is no water in a molten compound, so hydrogen and oxygen do not form.
- [ ] Potassium iodide at both electrodes
    - *why wrong:* The compound is broken down into its elements, not reformed.

**Q9. [reason]** Explain why lead forms at the cathode when molten lead bromide is electrolysed.
- [✔︎] Lead ions are positive, so they are attracted to the negative cathode, where they gain electrons to form lead
- [ ] Lead is heavier, so it sinks to the cathode
    - *why wrong:* Product formation is due to ion charge and discharge, not weight.
- [ ] Lead ions are negative and attracted to the cathode
    - *why wrong:* Lead ions are POSITIVE; that is why they go to the negative cathode.
- [ ] Lead is a non-metal that collects at the cathode
    - *why wrong:* Lead is a metal, and metals form at the cathode because their ions are positive.

**Q10. [apply]** Predict the product formed at the cathode when molten aluminium oxide is electrolysed.
- [✔︎] Aluminium
- [ ] Oxygen
    - *why wrong:* Oxygen, the non-metal, forms at the anode; aluminium (the metal) forms at the cathode.
- [ ] Aluminium oxide
    - *why wrong:* The compound is broken down; aluminium metal forms at the cathode.
- [ ] Carbon dioxide
    - *why wrong:* Carbon dioxide can form at the carbon anode, not at the cathode where aluminium forms.

### Triple Foundation — 2 extra Foundation-level questions

_On top of the 10 above (so Triple Foundation shows 12)._

**Q11. [apply]** Name the two elements formed when molten zinc chloride is electrolysed.
- [✔︎] Zinc (at the cathode) and chlorine (at the anode)
- [ ] Chlorine (at the cathode) and zinc (at the anode)
    - *why wrong:* This is reversed — the metal zinc forms at the cathode, the non-metal chlorine at the anode.
- [ ] Hydrogen and chlorine
    - *why wrong:* There is no water in molten zinc chloride, so hydrogen does not form; zinc does.
- [ ] Zinc oxide and chlorine
    - *why wrong:* Electrolysis gives the elements zinc and chlorine, not zinc oxide.

**Q12. [recall]** State the charge on the electrode where the metal is deposited.
- [✔︎] Negative (the cathode)
- [ ] Positive (the anode)
    - *why wrong:* The metal forms at the NEGATIVE cathode; the anode is positive and forms the non-metal.
- [ ] It has no charge
    - *why wrong:* The electrode carrying the metal is charged negative — that is why positive metal ions go there.
- [ ] It changes charge during the reaction
    - *why wrong:* The cathode stays negative throughout; the metal deposits there.

### Combined Higher — 10 questions

_A different, harder set from Foundation. These 10 also appear verbatim in Triple Higher._

**Q1. [apply]** Predict and explain the products at each electrode when molten lead bromide is electrolysed.
- [✔︎] Lead at the cathode (metal ions gain electrons) and bromine at the anode (non-metal ions lose electrons)
- [ ] Bromine at the cathode and lead at the anode
    - *why wrong:* This is reversed — the metal forms at the cathode and the non-metal at the anode.
- [ ] Hydrogen at the cathode and oxygen at the anode
    - *why wrong:* There is no water in a molten compound, so no hydrogen or oxygen forms.
- [ ] Lead bromide at both electrodes
    - *why wrong:* The compound is decomposed into its elements, not reformed at the electrodes.

**Q2. [reason]** Explain why the metal is always formed at the cathode in the electrolysis of a molten salt.
- [✔︎] Metal ions are positively charged, so they move to the negative cathode where they gain electrons and are reduced to metal atoms
- [ ] Metal ions are negative and attracted to the cathode
    - *why wrong:* Metal ions are POSITIVE; that is why they are attracted to the negative cathode.
- [ ] Metals are denser and sink onto the cathode
    - *why wrong:* It is charge and discharge, not density, that puts the metal at the cathode.
- [ ] The cathode gives out metal atoms of its own
    - *why wrong:* The metal comes from the electrolyte's ions gaining electrons, not from the electrode.

**Q3. [apply] ⭐** Write the cathode half-equation for the electrolysis of molten sodium chloride.
- [✔︎] Na⁺ + e⁻ → Na
- [ ] Na⁺ → Na + e⁻
    - *why wrong:* At the cathode sodium ions GAIN an electron; the electron belongs on the left.
- [ ] Na⁺ + e⁻ → Na⁻
    - *why wrong:* Sodium forms a neutral atom (Na), not a negative ion, when it gains an electron.
- [ ] Cl⁻ + e⁻ → Cl
    - *why wrong:* That describes a chloride ion; the cathode reaction is for the metal ion, Na⁺ + e⁻ → Na.

**Q4. [apply] ⭐** Write the anode half-equation for the electrolysis of molten sodium chloride.
- [✔︎] 2Cl⁻ → Cl₂ + 2e⁻
- [ ] 2Cl⁻ + 2e⁻ → Cl₂
    - *why wrong:* At the anode chloride ions LOSE electrons, so the electrons go on the right.
- [ ] Cl⁻ → Cl₂ + e⁻
    - *why wrong:* This is not balanced — two chloride ions are needed to make one Cl₂, releasing two electrons.
- [ ] Na⁺ + e⁻ → Na
    - *why wrong:* That is the cathode (metal) reaction; the anode reaction is 2Cl⁻ → Cl₂ + 2e⁻.

**Q5. [apply]** Predict the products and their electrodes for the electrolysis of molten magnesium chloride.
- [✔︎] Magnesium at the cathode and chlorine at the anode
- [ ] Chlorine at the cathode and magnesium at the anode
    - *why wrong:* This is reversed — the metal (magnesium) forms at the cathode, the non-metal (chlorine) at the anode.
- [ ] Hydrogen at the cathode and oxygen at the anode
    - *why wrong:* There is no water present, so hydrogen and oxygen are not produced.
- [ ] Magnesium oxide at the anode
    - *why wrong:* No oxygen is present; the anode product is chlorine, not magnesium oxide.

**Q6. [reason]** Explain, in terms of electrons, why the non-metal forms at the anode.
- [✔︎] The negative non-metal ions are attracted to the positive anode, where they lose electrons and are oxidised
- [ ] The non-metal ions gain electrons at the anode
    - *why wrong:* At the anode ions LOSE electrons (oxidation); gaining happens at the cathode.
- [ ] The non-metal ions are positive and repelled to the anode
    - *why wrong:* Non-metal ions are NEGATIVE, which is why they are attracted to the positive anode.
- [ ] The anode releases non-metal atoms of its own
    - *why wrong:* The non-metal comes from the electrolyte's ions losing electrons, not from the electrode.

**Q7. [apply]** Deduce the products when molten aluminium oxide is electrolysed.
- [✔︎] Aluminium at the cathode and oxygen at the anode
- [ ] Oxygen at the cathode and aluminium at the anode
    - *why wrong:* This is reversed — the metal (aluminium) forms at the cathode, the non-metal (oxygen) at the anode.
- [ ] Hydrogen and oxygen
    - *why wrong:* Molten aluminium oxide has no water, so no hydrogen forms; aluminium forms at the cathode.
- [ ] Aluminium oxide is not broken down
    - *why wrong:* Electrolysis does decompose it into aluminium and oxygen.

**Q8. [reason]** Explain why the electrolysis of molten compounds is carried out at high temperatures.
- [✔︎] A high temperature is needed to melt the compound so that its ions become free to move
- [ ] A high temperature adds electrons to the ions
    - *why wrong:* Heat frees the ions to move; it does not add electrons.
- [ ] A high temperature is needed to start the electric current
    - *why wrong:* The current comes from the supply; heat is needed to free the ions by melting.
- [ ] A high temperature makes the metal more reactive
    - *why wrong:* The temperature is about melting the electrolyte, not changing reactivity.

**Q9. [recall]** State the two types of element produced when a molten binary ionic compound is electrolysed.
- [✔︎] A metal (at the cathode) and a non-metal (at the anode)
- [ ] Two metals
    - *why wrong:* A binary salt gives one metal and one non-metal, not two metals.
- [ ] Two non-metals
    - *why wrong:* One of the elements is the metal; only the other is a non-metal.
- [ ] A metal and a compound
    - *why wrong:* Electrolysis gives the two elements — a metal and a non-metal — not a compound.

**Q10. [apply]** State which electrode gains a coating of solid metal during the electrolysis of molten zinc chloride.
- [✔︎] The cathode
- [ ] The anode
    - *why wrong:* The anode produces chlorine gas; the solid metal (zinc) forms at the cathode.
- [ ] Both electrodes
    - *why wrong:* Only the cathode gains metal; the anode produces a non-metal gas.
- [ ] Neither — the metal stays dissolved
    - *why wrong:* The metal is deposited as a solid on the cathode, not left dissolved.

### Triple Higher — 2 extra Higher/depth questions

_On top of the 10 above (so Triple Higher shows 12)._

**Q11. [apply] ⭐** Write the cathode half-equation for the electrolysis of molten magnesium chloride.
- [✔︎] Mg²⁺ + 2e⁻ → Mg
- [ ] Mg²⁺ → Mg + 2e⁻
    - *why wrong:* That shows magnesium ions LOSING electrons; at the cathode they GAIN electrons.
- [ ] Mg²⁺ + e⁻ → Mg
    - *why wrong:* Magnesium ions carry a 2+ charge, so they gain two electrons, not one.
- [ ] Mg⁺ + e⁻ → Mg
    - *why wrong:* Magnesium forms a 2+ ion, so the half-equation is Mg²⁺ + 2e⁻ → Mg.

**Q12. [apply] ⭐** Write the anode half-equation for the electrolysis of molten lead bromide.
- [✔︎] 2Br⁻ → Br₂ + 2e⁻
- [ ] 2Br⁻ + 2e⁻ → Br₂
    - *why wrong:* At the anode the bromide ions LOSE electrons, so the electrons go on the right.
- [ ] Br⁻ → Br₂ + e⁻
    - *why wrong:* This is not balanced — two bromide ions form one Br₂ and release two electrons.
- [ ] Pb²⁺ + 2e⁻ → Pb
    - *why wrong:* That is the cathode (metal) reaction; the anode reaction is 2Br⁻ → Br₂ + 2e⁻.

---

## Using Electrolysis to Extract Metals  ·  `electrolysis-extraction`  ·  AQA 5.4.3.3

> 🚩 **Triple-depth call (your review):** MATCHED — this AQA sub-topic is identical for Combined and Triple. Foundation difficulty is the same across both pathways; each Triple set = the Combined set + extra same-difficulty coverage. No AQA Triple-only content on this page.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often put the impure copper as the cathode when purifying copper by electrolysis. It is the other way round. The IMPURE copper must be the ANODE (positive): it dissolves as the copper is oxidised to Cu²⁺ ions. The PURE copper builds up on the CATHODE (negative), where the Cu²⁺ ions gain electrons. The impurities simply drop off the anode and collect as a sludge below it.

### Combined Foundation — 10 questions

_These 10 also appear verbatim in Triple Foundation._

**Q1. [recall]** Name the metal that is extracted by the electrolysis of its molten oxide.
- [✔︎] Aluminium
- [ ] Iron
    - *why wrong:* Iron is below carbon, so it is extracted by cheaper carbon reduction, not electrolysis.
- [ ] Copper
    - *why wrong:* Most copper is not extracted by electrolysis of its oxide; aluminium is the metal extracted this way.
- [ ] Gold
    - *why wrong:* Gold is unreactive and found native; it needs no electrolysis.

**Q2. [apply]** State the electrode at which aluminium forms during its extraction.
- [✔︎] The cathode (the negative electrode)
- [ ] The anode (the positive electrode)
    - *why wrong:* Oxygen forms at the anode; the aluminium metal forms at the negative cathode.
- [ ] Both electrodes
    - *why wrong:* Aluminium forms only at the cathode; oxygen forms at the anode.
- [ ] Neither — it stays dissolved
    - *why wrong:* The aluminium is deposited as molten metal at the cathode.

**Q3. [reason]** Explain why cryolite is mixed with the aluminium oxide before electrolysis.
- [✔︎] It lowers the melting point of the aluminium oxide, so less energy is needed to keep it molten
- [ ] It makes the aluminium more reactive
    - *why wrong:* Cryolite lowers the melting point; it does not change the aluminium's reactivity.
- [ ] It adds extra aluminium to the mixture
    - *why wrong:* Cryolite is a separate compound used to lower the melting point, not a source of aluminium.
- [ ] It colours the mixture so it can be seen
    - *why wrong:* Cryolite's job is to lower the melting point and save energy, not to add colour.

**Q4. [reason]** Explain why the carbon (graphite) anodes in aluminium extraction must be replaced regularly.
- [✔︎] The oxygen produced at the anode reacts with the hot carbon, so the anodes gradually burn away
- [ ] The aluminium sticks to them and cannot be removed
    - *why wrong:* The anodes wear away because oxygen burns the carbon, not because aluminium sticks.
- [ ] They dissolve in the cryolite
    - *why wrong:* The anodes are lost because oxygen reacts with the carbon, not by dissolving in cryolite.
- [ ] They cool down and stop working
    - *why wrong:* They are consumed by reaction with oxygen; cooling is not the reason.

**Q5. [apply]** State the product formed at the anode during aluminium extraction.
- [✔︎] Oxygen
- [ ] Aluminium
    - *why wrong:* Aluminium forms at the cathode; oxygen forms at the anode.
- [ ] Carbon
    - *why wrong:* The carbon is the electrode material, not a product; the anode product is oxygen.
- [ ] Hydrogen
    - *why wrong:* There is no water in molten aluminium oxide, so no hydrogen forms; oxygen is produced.

**Q6. [recall]** State why aluminium is extracted by electrolysis rather than by heating with carbon.
- [✔︎] Aluminium is more reactive than carbon, so carbon cannot remove the oxygen from aluminium oxide
- [ ] Aluminium is cheaper to extract by electrolysis
    - *why wrong:* Electrolysis is actually more expensive; it is used because carbon cannot reduce aluminium oxide.
- [ ] Carbon would make the aluminium impure
    - *why wrong:* The real reason is that carbon cannot reduce aluminium oxide at all, as aluminium is above carbon.
- [ ] Aluminium melts at too low a temperature for carbon
    - *why wrong:* The reason is reactivity: aluminium is above carbon, so carbon cannot remove its oxygen.

**Q7. [reason]** Explain why extracting aluminium by electrolysis is expensive.
- [✔︎] It uses a large amount of electrical energy to melt the oxide and to run the electrolysis
- [ ] Aluminium ore is extremely rare
    - *why wrong:* Aluminium ore is abundant; the cost comes from the large amount of electricity used.
- [ ] Cryolite is very difficult to obtain
    - *why wrong:* The main cost is the electrical energy, not the cryolite.
- [ ] Aluminium reacts violently and wastes material
    - *why wrong:* The high cost is the energy demand of electrolysis, not wasted material.

**Q8. [apply]** In the purification of copper by electrolysis, state which electrode is made of impure copper.
- [✔︎] The anode (the positive electrode)
- [ ] The cathode (the negative electrode)
    - *why wrong:* The pure copper forms on the cathode; the impure copper is the anode, which dissolves.
- [ ] Both electrodes
    - *why wrong:* Only the anode is impure copper; the cathode is pure copper.
- [ ] Neither — both are carbon
    - *why wrong:* In copper purification the electrodes are copper: impure at the anode, pure at the cathode.

**Q9. [apply]** In the purification of copper, state where the pure copper is deposited.
- [✔︎] On the cathode (the negative electrode)
- [ ] On the anode (the positive electrode)
    - *why wrong:* The anode is the impure copper that dissolves; pure copper forms on the cathode.
- [ ] In the electrolyte as a powder
    - *why wrong:* Pure copper is deposited as a solid on the cathode, not left as powder in solution.
- [ ] On both electrodes equally
    - *why wrong:* Pure copper builds up only on the cathode; the anode loses copper.

**Q10. [reason]** Explain why the aluminium oxide is melted before it is electrolysed.
- [✔︎] Melting frees the ions so they can move to the electrodes and be discharged
- [ ] Melting removes the impurities first
    - *why wrong:* Melting is to free the ions; cryolite and the process handle the setup, not impurity removal by melting.
- [ ] Melting adds electrons to the aluminium ions
    - *why wrong:* Melting frees the ions to move; it does not add electrons.
- [ ] Melting turns the oxide into a metal directly
    - *why wrong:* Melting alone does not extract the metal; electrolysis of the molten oxide does.

### Triple Foundation — 2 extra Foundation-level questions

_On top of the 10 above (so Triple Foundation shows 12)._

**Q11. [recall]** Name the substance added to aluminium oxide to lower its melting point.
- [✔︎] Cryolite
- [ ] Limestone
    - *why wrong:* Limestone is used in iron extraction, not to lower the melting point of aluminium oxide.
- [ ] Cryogen
    - *why wrong:* The substance used is called cryolite; 'cryogen' is a general term for a coolant.
- [ ] Carbon
    - *why wrong:* Carbon is used for the electrodes; cryolite is what lowers the melting point.

**Q12. [apply]** State the gas that forms at the anode and reacts with the carbon electrodes.
- [✔︎] Oxygen
- [ ] Hydrogen
    - *why wrong:* There is no water in molten aluminium oxide; the anode gas is oxygen, which burns the carbon.
- [ ] Chlorine
    - *why wrong:* There are no chloride ions here; the anode gas is oxygen.
- [ ] Carbon dioxide arrives from the air
    - *why wrong:* The oxygen made at the anode reacts with the carbon to form carbon dioxide; the anode gas itself is oxygen.

### Combined Higher — 10 questions

_A different, harder set from Foundation. These 10 also appear verbatim in Triple Higher._

**Q1. [reason]** Explain why aluminium must be extracted by electrolysis instead of reduction with carbon.
- [✔︎] Aluminium is more reactive than carbon, so carbon cannot remove the oxygen from aluminium oxide
- [ ] Aluminium oxide is a gas that carbon cannot reach
    - *why wrong:* Aluminium oxide is a solid/molten ionic compound; the reason is reactivity, not state.
- [ ] Carbon reduction would make radioactive aluminium
    - *why wrong:* Carbon simply cannot reduce aluminium oxide; radioactivity is not involved.
- [ ] Electrolysis is always cheaper than carbon reduction
    - *why wrong:* Electrolysis is more expensive; it is used because carbon cannot reduce aluminium oxide.

**Q2. [reason]** Explain the purpose of mixing cryolite with the molten aluminium oxide.
- [✔︎] Cryolite lowers the melting point, so the electrolysis runs at a lower temperature and uses less energy
- [ ] Cryolite increases the melting point to keep it solid
    - *why wrong:* Cryolite LOWERS the melting point; the mixture is kept molten, not solid.
- [ ] Cryolite provides the aluminium ions
    - *why wrong:* The aluminium ions come from the aluminium oxide; cryolite lowers the melting point.
- [ ] Cryolite speeds up the flow of electrons in the wires
    - *why wrong:* Cryolite affects the melt's temperature, not the electron flow in the wires.

**Q3. [apply] ⭐** Write the cathode half-equation for the extraction of aluminium.
- [✔︎] Al³⁺ + 3e⁻ → Al
- [ ] Al³⁺ → Al + 3e⁻
    - *why wrong:* At the cathode the ions GAIN electrons; the electrons belong on the left.
- [ ] Al²⁺ + 2e⁻ → Al
    - *why wrong:* Aluminium ions carry a 3+ charge, so they gain three electrons, not two.
- [ ] 3Al³⁺ + 3e⁻ → 3Al
    - *why wrong:* The electrons and ions are not balanced; one Al³⁺ gains three electrons: Al³⁺ + 3e⁻ → Al.

**Q4. [apply] ⭐** Write the anode half-equation for the extraction of aluminium.
- [✔︎] 2O²⁻ → O₂ + 4e⁻
- [ ] 2O²⁻ + 4e⁻ → O₂
    - *why wrong:* At the anode oxide ions LOSE electrons, so the electrons go on the right.
- [ ] O²⁻ → O₂ + 2e⁻
    - *why wrong:* This is unbalanced — two oxide ions make one O₂ molecule and release four electrons.
- [ ] 4OH⁻ → O₂ + 2H₂O + 4e⁻
    - *why wrong:* That is the anode reaction in AQUEOUS solution; molten aluminium oxide uses oxide ions: 2O²⁻ → O₂ + 4e⁻.

**Q5. [reason]** Explain why the positive carbon electrodes gradually burn away and need replacing.
- [✔︎] The oxygen produced at the anode reacts with the hot carbon to form carbon dioxide, wearing the electrodes down
- [ ] The molten aluminium dissolves the carbon
    - *why wrong:* The carbon is lost by reacting with oxygen to form CO₂, not by dissolving in aluminium.
- [ ] The current melts the carbon electrodes
    - *why wrong:* The electrodes are consumed by reaction with oxygen, not simply melted by the current.
- [ ] The cryolite corrodes the carbon
    - *why wrong:* It is the oxygen at the anode that burns the carbon away, not the cryolite.

**Q6. [reason]** Explain why the extraction of aluminium has such a high energy cost.
- [✔︎] A lot of electrical energy is needed both to melt the aluminium oxide and to drive the electrolysis
- [ ] Aluminium ore has to be transported very far
    - *why wrong:* The dominant cost is the electrical energy of the process, not transport.
- [ ] The cryolite has to be made by electrolysis too
    - *why wrong:* The high cost is the electricity used to melt and electrolyse the oxide.
- [ ] Aluminium is only found in tiny amounts
    - *why wrong:* Aluminium ore is abundant; the cost is the energy-intensive electrolysis.

**Q7. [apply]** In the purification of copper, describe what happens at the impure copper anode.
- [✔︎] The copper atoms lose electrons and dissolve into the solution as Cu²⁺ ions (Cu → Cu²⁺ + 2e⁻)
- [ ] Copper ions gain electrons and are deposited
    - *why wrong:* That happens at the cathode; at the anode copper dissolves by losing electrons.
- [ ] Oxygen gas is released
    - *why wrong:* In copper purification the anode dissolves as copper ions; oxygen is not the product.
- [ ] The anode stays unchanged
    - *why wrong:* The anode is steadily eaten away as its copper dissolves into solution.

**Q8. [apply] ⭐** Write the cathode half-equation for the purification of copper.
- [✔︎] Cu²⁺ + 2e⁻ → Cu
- [ ] Cu → Cu²⁺ + 2e⁻
    - *why wrong:* That is the ANODE reaction (copper dissolving); at the cathode Cu²⁺ gains electrons.
- [ ] Cu²⁺ + e⁻ → Cu
    - *why wrong:* Copper ions are 2+, so they gain two electrons, not one.
- [ ] Cu²⁺ + 2e⁻ → Cu²⁻
    - *why wrong:* The product is neutral copper metal (Cu), not a negative ion.

**Q9. [reason]** Explain what happens to the impurities in the impure copper anode during purification.
- [✔︎] They fall to the bottom of the cell as a sludge below the anode, because they are not discharged like copper
- [ ] They dissolve and deposit on the cathode with the copper
    - *why wrong:* Only copper is deposited on the cathode; the impurities drop off as anode sludge.
- [ ] They evaporate as gases at the anode
    - *why wrong:* The impurities collect as a solid sludge, not as gases.
- [ ] They stay locked in the anode, which is left unchanged
    - *why wrong:* The anode dissolves, releasing the impurities, which fall as sludge.

**Q10. [recall]** State the product formed at the cathode during the extraction of aluminium.
- [✔︎] Molten aluminium metal
- [ ] Oxygen gas
    - *why wrong:* Oxygen forms at the anode; the cathode product is aluminium.
- [ ] Carbon dioxide
    - *why wrong:* Carbon dioxide forms where oxygen burns the carbon anode, not at the cathode.
- [ ] Aluminium oxide
    - *why wrong:* The oxide is broken down; the cathode product is aluminium metal.

### Triple Higher — 2 extra Higher/depth questions

_On top of the 10 above (so Triple Higher shows 12)._

**Q11. [apply] ⭐** Write the anode half-equation for the impure copper anode dissolving during copper purification.
- [✔︎] Cu → Cu²⁺ + 2e⁻
- [ ] Cu²⁺ + 2e⁻ → Cu
    - *why wrong:* That is the CATHODE reaction (copper being deposited); the dissolving anode loses electrons.
- [ ] Cu → Cu²⁺ + e⁻
    - *why wrong:* Forming a 2+ ion means losing two electrons, not one.
- [ ] Cu²⁺ → Cu + 2e⁻
    - *why wrong:* The impure anode is copper metal dissolving to Cu²⁺: Cu → Cu²⁺ + 2e⁻.

**Q12. [reason]** During copper purification, explain why the anode loses mass while the cathode gains mass.
- [✔︎] Copper dissolves from the anode as Cu²⁺ ions and is deposited as copper metal on the cathode, so copper transfers from one to the other
- [ ] Copper evaporates from the anode and condenses on the cathode
    - *why wrong:* Copper does not evaporate; it dissolves as ions and is deposited by electrolysis.
- [ ] The cathode grows because new copper is made from the electrolyte's water
    - *why wrong:* The deposited copper comes from the dissolving anode, not from water.
- [ ] The anode loses mass because it melts
    - *why wrong:* The anode loses mass because its copper dissolves as ions, not because it melts.

---

## Electrolysis of Aqueous Solutions  ·  `electrolysis-aqueous`  ·  AQA 5.4.3.4

> 🚩 **Triple-depth call (your review):** MATCHED — this AQA sub-topic is identical for Combined and Triple. Foundation difficulty is the same across both pathways; each Triple set = the Combined set + extra same-difficulty coverage. No AQA Triple-only content on this page.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often predict that the metal is always deposited at the cathode, so they say sodium forms when sodium chloride SOLUTION is electrolysed. In water it does not. Sodium is more reactive than hydrogen, so HYDROGEN is produced at the cathode instead, from the water. The rule: at the cathode you get the metal ONLY if it is LESS reactive than hydrogen (like copper); if it is more reactive, you get hydrogen.

### Combined Foundation — 10 questions

_These 10 also appear verbatim in Triple Foundation._

**Q1. [reason]** Explain why electrolysing a solution is more complicated than electrolysing a molten compound.
- [✔︎] The water also provides H⁺ and OH⁻ ions, which compete with the salt's ions to be discharged
- [ ] The solution is colder, so the ions move more slowly
    - *why wrong:* The added complexity is the water's ions competing, not temperature.
- [ ] Dissolving destroys the salt's ions
    - *why wrong:* The salt's ions remain; the extra factor is the water's own ions.
- [ ] Water stops the current from flowing
    - *why wrong:* Water actually helps conduct by adding ions; the complication is that its ions can be discharged.

**Q2. [apply]** Predict the product at the cathode when sodium chloride solution is electrolysed.
- [✔︎] Hydrogen
- [ ] Sodium
    - *why wrong:* Sodium is more reactive than hydrogen, so hydrogen is produced at the cathode, not sodium.
- [ ] Chlorine
    - *why wrong:* Chlorine forms at the anode; the cathode produces hydrogen here.
- [ ] Oxygen
    - *why wrong:* Oxygen would form at the anode if no halide were present; the cathode produces hydrogen.

**Q3. [apply]** Predict the product at the anode when sodium chloride solution is electrolysed.
- [✔︎] Chlorine
- [ ] Oxygen
    - *why wrong:* Oxygen forms only when no halide is present; chloride ions are present here, so chlorine forms.
- [ ] Hydrogen
    - *why wrong:* Hydrogen forms at the cathode, not the anode; the anode gives chlorine.
- [ ] Sodium
    - *why wrong:* Sodium is a metal formed (if at all) at the cathode; the anode gives chlorine.

**Q4. [apply]** Predict the product at the cathode when copper sulfate solution is electrolysed.
- [✔︎] Copper
- [ ] Hydrogen
    - *why wrong:* Copper is LESS reactive than hydrogen, so the copper metal is deposited, not hydrogen.
- [ ] Oxygen
    - *why wrong:* Oxygen forms at the anode; the cathode deposits copper here.
- [ ] Sulfur
    - *why wrong:* Sulfur is not discharged; the cathode deposits copper.

**Q5. [apply]** Predict the product at the anode when copper sulfate solution is electrolysed.
- [✔︎] Oxygen
- [ ] Chlorine
    - *why wrong:* There are no chloride ions in copper sulfate solution, so oxygen forms, not chlorine.
- [ ] Copper
    - *why wrong:* Copper is deposited at the cathode; the anode gives oxygen.
- [ ] Hydrogen
    - *why wrong:* Hydrogen forms at the cathode; the anode gives oxygen when no halide is present.

**Q6. [recall]** State the rule for what forms at the cathode in aqueous electrolysis.
- [✔︎] The metal forms if it is less reactive than hydrogen; otherwise hydrogen is produced
- [ ] The metal always forms at the cathode
    - *why wrong:* In water, a reactive metal is not deposited; hydrogen forms instead.
- [ ] Hydrogen always forms at the cathode
    - *why wrong:* A less-reactive metal such as copper IS deposited; it is not always hydrogen.
- [ ] Oxygen forms at the cathode
    - *why wrong:* Oxygen forms at the anode; the cathode gives a metal or hydrogen.

**Q7. [recall]** State the rule for what forms at the anode in aqueous electrolysis.
- [✔︎] A halogen forms if a halide ion is present; otherwise oxygen is produced
- [ ] Oxygen always forms at the anode
    - *why wrong:* If a halide (Cl⁻, Br⁻, I⁻) is present, the halogen forms instead of oxygen.
- [ ] A halogen always forms at the anode
    - *why wrong:* Without a halide, oxygen forms; the halogen only forms when a halide is present.
- [ ] Hydrogen forms at the anode
    - *why wrong:* Hydrogen forms at the cathode; the anode gives a halogen or oxygen.

**Q8. [apply]** Predict the two products when dilute sulfuric acid is electrolysed.
- [✔︎] Hydrogen at the cathode and oxygen at the anode
- [ ] Oxygen at the cathode and hydrogen at the anode
    - *why wrong:* This is reversed — hydrogen forms at the cathode and oxygen at the anode.
- [ ] Sulfur and hydrogen
    - *why wrong:* Sulfur is not discharged; the products are hydrogen and oxygen (from the water).
- [ ] Chlorine and hydrogen
    - *why wrong:* There are no chloride ions in sulfuric acid; oxygen forms at the anode, not chlorine.

**Q9. [reason]** Explain why sodium is not produced at the cathode when sodium chloride solution is electrolysed.
- [✔︎] Sodium is more reactive than hydrogen, so hydrogen from the water is discharged instead of the sodium
- [ ] Sodium ions are too large to reach the cathode
    - *why wrong:* Sodium ions do reach the cathode; hydrogen is discharged because sodium is too reactive.
- [ ] There are no sodium ions in the solution
    - *why wrong:* Sodium ions are present; they simply stay in solution because hydrogen is discharged instead.
- [ ] Sodium reacts with the anode first
    - *why wrong:* The reason is that sodium is more reactive than hydrogen, so hydrogen is discharged at the cathode.

**Q10. [apply]** Predict the product at the cathode when potassium nitrate solution is electrolysed.
- [✔︎] Hydrogen
- [ ] Potassium
    - *why wrong:* Potassium is more reactive than hydrogen, so hydrogen is produced at the cathode, not potassium.
- [ ] Oxygen
    - *why wrong:* Oxygen forms at the anode; the cathode gives hydrogen here.
- [ ] Nitrogen
    - *why wrong:* Nitrogen is not discharged; the cathode gives hydrogen.

### Triple Foundation — 2 extra Foundation-level questions

_On top of the 10 above (so Triple Foundation shows 12)._

**Q11. [apply]** Predict the product at the anode when potassium bromide solution is electrolysed.
- [✔︎] Bromine
- [ ] Oxygen
    - *why wrong:* A halide (bromide) is present, so the halogen bromine forms, not oxygen.
- [ ] Hydrogen
    - *why wrong:* Hydrogen forms at the cathode, not the anode; the anode gives bromine here.
- [ ] Potassium
    - *why wrong:* Potassium is a metal; if discharged it would be at the cathode, but here hydrogen forms there and bromine at the anode.

**Q12. [recall]** State the two ions that water provides in an aqueous solution.
- [✔︎] Hydrogen ions (H⁺) and hydroxide ions (OH⁻)
- [ ] Sodium ions and chloride ions
    - *why wrong:* Those come from a dissolved salt, not from the water itself.
- [ ] Oxygen ions and hydrogen ions
    - *why wrong:* Water provides H⁺ and OH⁻, not free oxygen ions.
- [ ] Only hydrogen ions
    - *why wrong:* Water provides both H⁺ and OH⁻ ions.

### Combined Higher — 10 questions

_A different, harder set from Foundation. These 10 also appear verbatim in Triple Higher._

**Q1. [reason]** Explain the rule that decides which product forms at the cathode in aqueous electrolysis.
- [✔︎] If the metal is less reactive than hydrogen it is deposited; if it is more reactive, hydrogen is produced from the water instead
- [ ] The metal is always deposited at the cathode
    - *why wrong:* A metal more reactive than hydrogen is not deposited from solution; hydrogen forms instead.
- [ ] Hydrogen is always produced at the cathode
    - *why wrong:* A less-reactive metal such as copper or silver IS deposited, so it is not always hydrogen.
- [ ] The most abundant ion is always discharged
    - *why wrong:* It is the metal's reactivity relative to hydrogen, not abundance, that decides.

**Q2. [reason]** Explain the rule that decides which product forms at the anode in aqueous electrolysis.
- [✔︎] If a halide ion (Cl⁻, Br⁻, I⁻) is present the halogen is produced; if not, oxygen is produced from hydroxide ions
- [ ] Oxygen is always produced at the anode
    - *why wrong:* When a halide is present, the halogen is produced instead of oxygen.
- [ ] The halogen is always produced at the anode
    - *why wrong:* Without a halide ion, oxygen forms; the halogen only appears when a halide is present.
- [ ] The metal is discharged at the anode
    - *why wrong:* Metals are discharged (if at all) at the cathode; the anode gives a non-metal.

**Q3. [apply]** Predict and justify the products of electrolysing copper chloride solution.
- [✔︎] Copper at the cathode (less reactive than hydrogen) and chlorine at the anode (halide present)
- [ ] Hydrogen at the cathode and oxygen at the anode
    - *why wrong:* Copper is less reactive than hydrogen so copper is deposited, and chloride ions give chlorine, not oxygen.
- [ ] Copper at the cathode and oxygen at the anode
    - *why wrong:* A halide (chloride) is present, so chlorine forms at the anode, not oxygen.
- [ ] Hydrogen at the cathode and chlorine at the anode
    - *why wrong:* Copper is less reactive than hydrogen, so copper — not hydrogen — is deposited at the cathode.

**Q4. [apply]** Predict and justify the products of electrolysing sodium sulfate solution.
- [✔︎] Hydrogen at the cathode (sodium too reactive) and oxygen at the anode (no halide present)
- [ ] Sodium at the cathode and oxygen at the anode
    - *why wrong:* Sodium is more reactive than hydrogen, so hydrogen forms at the cathode, not sodium.
- [ ] Hydrogen at the cathode and sulfur at the anode
    - *why wrong:* Sulfate ions are not discharged to sulfur; oxygen forms at the anode.
- [ ] Sodium at the cathode and sulfur at the anode
    - *why wrong:* Hydrogen forms at the cathode and oxygen at the anode; neither sodium nor sulfur is discharged.

**Q5. [apply] ⭐** Write the cathode half-equation for the discharge of hydrogen in aqueous electrolysis.
- [✔︎] 2H⁺ + 2e⁻ → H₂
- [ ] 2H⁺ → H₂ + 2e⁻
    - *why wrong:* At the cathode the ions gain electrons; the electrons belong on the left.
- [ ] H⁺ + e⁻ → H₂
    - *why wrong:* This is not balanced — two H⁺ and two electrons are needed to form one H₂ molecule.
- [ ] 2H₂O + 2e⁻ → H₂ + O₂
    - *why wrong:* The cathode produces only hydrogen; oxygen forms separately at the anode.

**Q6. [apply] ⭐** Write the anode half-equation for the discharge of chlorine in aqueous electrolysis.
- [✔︎] 2Cl⁻ → Cl₂ + 2e⁻
- [ ] 2Cl⁻ + 2e⁻ → Cl₂
    - *why wrong:* At the anode chloride ions LOSE electrons, so the electrons go on the right.
- [ ] Cl⁻ → Cl₂ + e⁻
    - *why wrong:* This is not balanced — two chloride ions form one Cl₂, releasing two electrons.
- [ ] 4OH⁻ → O₂ + 2H₂O + 4e⁻
    - *why wrong:* That is the oxygen (no-halide) reaction; with chloride present the anode gives 2Cl⁻ → Cl₂ + 2e⁻.

**Q7. [reason]** Explain why copper is deposited from copper sulfate solution but sodium is not deposited from sodium sulfate solution.
- [✔︎] Copper is less reactive than hydrogen so it is discharged, but sodium is more reactive than hydrogen, so hydrogen is discharged instead of sodium
- [ ] Copper ions are larger, so they reach the cathode first
    - *why wrong:* It is reactivity relative to hydrogen, not ion size, that decides which is discharged.
- [ ] Sodium sulfate does not contain sodium ions
    - *why wrong:* It does contain sodium ions; they stay in solution because hydrogen is discharged instead.
- [ ] Copper is more reactive than sodium
    - *why wrong:* Copper is far LESS reactive than sodium; that is why copper is discharged and sodium is not.

**Q8. [apply]** Predict the products of electrolysing concentrated sodium chloride solution (brine).
- [✔︎] Hydrogen at the cathode and chlorine at the anode, leaving sodium hydroxide in solution
- [ ] Sodium at the cathode and chlorine at the anode
    - *why wrong:* Sodium is too reactive to be deposited from solution; hydrogen forms at the cathode.
- [ ] Hydrogen at the cathode and oxygen at the anode
    - *why wrong:* Chloride ions are present in brine, so chlorine forms at the anode, not oxygen.
- [ ] Sodium and chlorine only, with nothing left in solution
    - *why wrong:* Sodium hydroxide is left in the solution as the H⁺ and Cl⁻ are removed.

**Q9. [reason]** Explain why oxygen is produced at the anode when a solution contains no halide ions.
- [✔︎] With no halide to discharge, the hydroxide ions from the water lose electrons at the anode to form oxygen
- [ ] The metal ions move to the anode and release oxygen
    - *why wrong:* Metal ions go to the cathode; oxygen comes from hydroxide ions at the anode.
- [ ] Oxygen is pulled directly out of the water molecules by heat
    - *why wrong:* Oxygen is produced by discharging OH⁻ ions at the anode, not by heating water.
- [ ] The sulfate ions break down to give oxygen
    - *why wrong:* Sulfate ions are not discharged; the oxygen comes from hydroxide ions.

**Q10. [apply]** Deduce the product at the cathode when silver nitrate solution is electrolysed.
- [✔︎] Silver, because silver is less reactive than hydrogen
- [ ] Hydrogen, because water is always discharged first
    - *why wrong:* Silver is less reactive than hydrogen, so the silver metal is deposited, not hydrogen.
- [ ] Oxygen, because nitrate contains oxygen
    - *why wrong:* Oxygen (if any) forms at the anode; the cathode deposits silver.
- [ ] Nitrogen, from the nitrate ion
    - *why wrong:* Nitrate is not discharged at the cathode; silver metal is deposited there.

### Triple Higher — 2 extra Higher/depth questions

_On top of the 10 above (so Triple Higher shows 12)._

**Q11. [apply] ⭐** Write the cathode half-equation for the production of hydrogen from an aqueous solution.
- [✔︎] 2H⁺ + 2e⁻ → H₂
- [ ] 2H⁺ → H₂ + 2e⁻
    - *why wrong:* At the cathode the ions GAIN electrons, so the electrons go on the left, not the right.
- [ ] H⁺ + e⁻ → H
    - *why wrong:* Hydrogen gas is the molecule H₂; two H⁺ ions gain two electrons to form H₂.
- [ ] 2OH⁻ → H₂ + O₂ + 2e⁻
    - *why wrong:* That is not the cathode reaction; hydrogen is formed from H⁺: 2H⁺ + 2e⁻ → H₂.

**Q12. [apply] ⭐** Write the anode half-equation for the production of oxygen from the hydroxide ions in solution.
- [✔︎] 4OH⁻ → O₂ + 2H₂O + 4e⁻
- [ ] 4OH⁻ + 4e⁻ → O₂ + 2H₂O
    - *why wrong:* At the anode ions LOSE electrons, so the electrons belong on the right.
- [ ] 2OH⁻ → O₂ + 2e⁻
    - *why wrong:* This is not balanced for oxygen or hydrogen; the correct equation is 4OH⁻ → O₂ + 2H₂O + 4e⁻.
- [ ] O²⁻ → O₂ + 4e⁻
    - *why wrong:* In solution oxygen comes from hydroxide ions, not oxide ions: 4OH⁻ → O₂ + 2H₂O + 4e⁻.

---

## Half Equations for Electrode Reactions  ·  `half-equations`  ·  AQA 5.4.3.5

> 🚩 **Triple-depth call (your review):** HIGHER-ONLY — AQA lists this content at Higher tier only, so there is no Foundation cell. Triple-Higher = the exact Combined-Higher set + 2 extra Higher/depth questions.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often put the electrons on the wrong side, or forget them altogether. The rule follows OIL RIG: at the CATHODE, positive ions GAIN electrons, so the electrons go on the LEFT (e.g. Cu²⁺ + 2e⁻ → Cu). At the ANODE, negative ions LOSE electrons, so the electrons go on the RIGHT (e.g. 2Cl⁻ → Cl₂ + 2e⁻). Always balance the atoms first, then add electrons until the charges match on both sides.

**FIFA worked examples (Combined Higher & Triple Higher) — ⭐ full review:**

> **Balancing an Anode Half-Equation (chloride)**  
> Write the balanced half-equation for chloride ions forming chlorine gas at the anode: Cl⁻ → Cl₂.  
> &nbsp;&nbsp;**F** — Balance the atoms first, then add electrons to balance the charges  
> &nbsp;&nbsp;**I** — 2Cl⁻ → Cl₂ (2 Cl on each side). Charge: left = 2 × (−1) = −2; right = 0  
> &nbsp;&nbsp;**F** — Add 2e⁻ to the RIGHT (anode = ions lose electrons): left −2, right −2 ✓  
> &nbsp;&nbsp;**A** — 2Cl⁻ → Cl₂ + 2e⁻  
>
> **Balancing a Cathode Half-Equation (aluminium)**  
> Write the balanced half-equation for aluminium ions forming aluminium at the cathode: Al³⁺ → Al.  
> &nbsp;&nbsp;**F** — Atoms are already balanced (1 Al each side); add electrons to balance the charge  
> &nbsp;&nbsp;**I** — Charge: left = +3; right = 0  
> &nbsp;&nbsp;**F** — Add 3e⁻ to the LEFT (cathode = ions gain electrons): left +3 − 3 = 0, right 0 ✓  
> &nbsp;&nbsp;**A** — Al³⁺ + 3e⁻ → Al  
>
> **Balancing a Cathode Half-Equation (hydrogen)**  
> Write the balanced half-equation for hydrogen ions forming hydrogen gas at the cathode: H⁺ → H₂.  
> &nbsp;&nbsp;**F** — Balance the H atoms first, then add electrons to balance the charge  
> &nbsp;&nbsp;**I** — 2H⁺ → H₂ (2 H on each side). Charge: left = +2; right = 0  
> &nbsp;&nbsp;**F** — Add 2e⁻ to the LEFT (cathode = ions gain electrons): left +2 − 2 = 0, right 0 ✓  
> &nbsp;&nbsp;**A** — 2H⁺ + 2e⁻ → H₂  
>

### Combined Higher — 10 questions

_There is no Foundation tier for this page. These 10 also appear verbatim in Triple Higher._

**Q1. [apply] ⭐** Complete the cathode half-equation: Cu²⁺ + ___ → Cu.
- [✔︎] + 2e⁻ (Cu²⁺ + 2e⁻ → Cu)
- [ ] + 2e⁻ on the right instead
    - *why wrong:* At the cathode the ion gains electrons, so the electrons must be on the LEFT, with the ion.
- [ ] + e⁻ (one electron)
    - *why wrong:* A Cu²⁺ ion has a 2+ charge, so it must gain two electrons, not one.
- [ ] nothing — it is already balanced
    - *why wrong:* The charges do not balance (left +2, right 0); two electrons are needed on the left.

**Q2. [apply] ⭐** Complete the anode half-equation: 2Cl⁻ → Cl₂ + ___.
- [✔︎] + 2e⁻ (2Cl⁻ → Cl₂ + 2e⁻)
- [ ] + 2e⁻ on the left instead
    - *why wrong:* At the anode the ions lose electrons, so the electrons go on the RIGHT.
- [ ] + e⁻ (one electron)
    - *why wrong:* Two chloride ions each lose one electron, so two electrons are released, not one.
- [ ] + H₂
    - *why wrong:* No hydrogen is involved here; the chloride ions simply release electrons to form Cl₂.

**Q3. [recall] ⭐** State on which side of a cathode half-equation the electrons are written.
- [✔︎] On the left, because the positive ions gain electrons (reduction)
- [ ] On the right, because the ions lose electrons
    - *why wrong:* That describes the anode; at the cathode ions gain electrons, written on the left.
- [ ] On both sides equally
    - *why wrong:* Electrons appear on one side only — the left — in a cathode half-equation.
- [ ] Electrons are not written in half-equations
    - *why wrong:* Electrons are essential in half-equations; at the cathode they go on the left.

**Q4. [recall] ⭐** State on which side of an anode half-equation the electrons are written.
- [✔︎] On the right, because the negative ions lose electrons (oxidation)
- [ ] On the left, because the ions gain electrons
    - *why wrong:* That describes the cathode; at the anode ions lose electrons, written on the right.
- [ ] On both sides equally
    - *why wrong:* Electrons appear on one side only — the right — in an anode half-equation.
- [ ] Electrons are only shown for metals
    - *why wrong:* All half-equations include electrons; at the anode they go on the right.

**Q5. [apply] ⭐** Balance the cathode half-equation for aluminium: Al³⁺ → Al.
- [✔︎] Al³⁺ + 3e⁻ → Al
- [ ] Al³⁺ + 2e⁻ → Al
    - *why wrong:* Aluminium ions carry a 3+ charge, so they need three electrons, not two.
- [ ] Al³⁺ → Al + 3e⁻
    - *why wrong:* At the cathode the ion GAINS electrons; the electrons belong on the left.
- [ ] Al³⁺ + 3e⁻ → Al³⁻
    - *why wrong:* The product is neutral aluminium metal (Al), not a 3− ion.

**Q6. [apply] ⭐** Balance the cathode half-equation for hydrogen: H⁺ → H₂.
- [✔︎] 2H⁺ + 2e⁻ → H₂
- [ ] H⁺ + e⁻ → H₂
    - *why wrong:* This is not balanced — two H⁺ ions and two electrons are needed to form one H₂ molecule.
- [ ] 2H⁺ → H₂ + 2e⁻
    - *why wrong:* At the cathode the ions gain electrons; the electrons go on the left, not the right.
- [ ] 2H⁺ + 2e⁻ → 2H
    - *why wrong:* Hydrogen gas is the molecule H₂, not two separate H atoms.

**Q7. [apply] ⭐** Write the anode half-equation for bromide ions forming bromine.
- [✔︎] 2Br⁻ → Br₂ + 2e⁻
- [ ] 2Br⁻ + 2e⁻ → Br₂
    - *why wrong:* At the anode the ions lose electrons, so the electrons go on the right.
- [ ] Br⁻ → Br₂ + e⁻
    - *why wrong:* This is not balanced — two bromide ions form one Br₂ and release two electrons.
- [ ] Br₂ → 2Br⁻ + 2e⁻
    - *why wrong:* This is written backwards; bromide ions form bromine: 2Br⁻ → Br₂ + 2e⁻.

**Q8. [apply] ⭐** From the pair Zn²⁺ + 2e⁻ → Zn and 2O²⁻ → O₂ + 4e⁻, identify the oxidation half-equation.
- [✔︎] 2O²⁻ → O₂ + 4e⁻, because the ions lose electrons (electrons on the right)
- [ ] Zn²⁺ + 2e⁻ → Zn, because a metal is formed
    - *why wrong:* That half-equation shows electrons being GAINED (reduction); forming a metal does not make it oxidation.
- [ ] Both are oxidation
    - *why wrong:* Only one shows electrons being lost; Zn²⁺ + 2e⁻ → Zn is reduction.
- [ ] Neither is oxidation
    - *why wrong:* 2O²⁻ → O₂ + 4e⁻ has electrons on the right, so it is oxidation.

**Q9. [reason] ⭐** Explain why the number of electrons must be equal when two half-equations are combined into an overall equation.
- [✔︎] The electrons lost at the anode must exactly equal the electrons gained at the cathode, so none are left over
- [ ] Because both electrodes must be the same size
    - *why wrong:* Electrode size is irrelevant; the electrons lost and gained must simply balance.
- [ ] Because electrons have no charge to balance
    - *why wrong:* Electrons carry a 1− charge each; they must balance so charge is conserved.
- [ ] Because the metal and non-metal have equal masses
    - *why wrong:* It is the electrons, not the masses, that must balance between the half-equations.

**Q10. [apply] ⭐** Complete the cathode half-equation: Na⁺ + ___ → Na.
- [✔︎] + e⁻ (Na⁺ + e⁻ → Na)
- [ ] + 2e⁻
    - *why wrong:* A sodium ion has only a 1+ charge, so it gains just one electron.
- [ ] + e⁻ on the right
    - *why wrong:* At the cathode the ion gains the electron, so it is written on the left.
- [ ] nothing — it is already balanced
    - *why wrong:* The charges do not match (left +1, right 0); one electron is needed on the left.

### Triple Higher — 2 extra Higher/depth questions

_On top of the 10 above (so Triple Higher shows 12)._

**Q11. [apply] ⭐** Write the anode half-equation for hydroxide ions forming oxygen in aqueous electrolysis.
- [✔︎] 4OH⁻ → O₂ + 2H₂O + 4e⁻
- [ ] 2OH⁻ → O₂ + 2e⁻
    - *why wrong:* This does not balance the oxygen or hydrogen atoms; four hydroxide ions are needed.
- [ ] 4OH⁻ + 4e⁻ → O₂ + 2H₂O
    - *why wrong:* At the anode the ions lose electrons, so the electrons belong on the right.
- [ ] 2O²⁻ → O₂ + 4e⁻
    - *why wrong:* In solution the oxygen comes from hydroxide ions, not oxide ions: 4OH⁻ → O₂ + 2H₂O + 4e⁻.

**Q12. [apply] ⭐** Write the anode half-equation for the impure copper anode dissolving during copper purification.
- [✔︎] Cu → Cu²⁺ + 2e⁻
- [ ] Cu²⁺ + 2e⁻ → Cu
    - *why wrong:* That is the CATHODE reaction (copper being deposited); the anode reaction is copper dissolving.
- [ ] Cu → Cu²⁺ + e⁻
    - *why wrong:* Forming a 2+ ion means losing two electrons, not one.
- [ ] Cu²⁻ → Cu + 2e⁻
    - *why wrong:* Copper metal is neutral (Cu); it dissolves by losing electrons: Cu → Cu²⁺ + 2e⁻.

---

