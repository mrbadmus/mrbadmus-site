# Bonding unit — content review (MRB-105)

_AQA 5.2 Bonding, Structure and the Properties of Matter. Drafted for Mide's review before the Phase 2 merge. Every question, its options (✔︎ = correct), and a diagnostic line for each wrong option are shown here — you never need to read the Python._

## Amendment delta — `giant-covalent-structures` Foundation coverage (review only this)

**Ruling applied:** follow the AQA spec. Graphene and fullerenes are shared Foundation content (5.2.2.6 / 5.2.3.x), so Foundation must carry recall/describe-level coverage. The prior draft placed **all** graphene/fullerene/nanotube questions at Higher, so Foundation had none. **Only `giant-covalent-structures` changed — every other page in this document is byte-identical to the prior draft.** Counts stay **10 / 10 / 12 / 12** (Combined-F / Combined-H / Triple-F / Triple-H); the TF = CF + 2 and TH = CH + 2 invariant holds; audit still shows **zero critical, zero content majors** on `chemistry/bonding/*`.

**Added** — 3 items, Foundation only (Combined-F **and** Triple-F), recall/describe register:
1. *Describe the structure of graphene and give one of its uses* — single layer of graphite, one atom thick; conducts, used in electronics.
2. *Describe the structure of buckminsterfullerene (C₆₀) and give one of its uses* — hollow cage of 60 carbon atoms; used in drug delivery.
3. *Describe carbon nanotubes and give one of their uses* — cylinders of rolled-up graphene; very strong, used to reinforce materials.

**Retired** — 3 items, Foundation only (pure recall, retired to keep the count at 10; each retired fact is still tested in the CORE graphite-vs-diamond item that every tier sees):
1. *State how many other carbon atoms each carbon is bonded to in diamond* (→ 4)
2. *State how many other carbon atoms each carbon is bonded to in graphite* (→ 3)
3. *State whether giant covalent structures have high or low melting points* (→ high)

**Deepened** — 1 item, Higher only (Combined-H **and** Triple-H); the old version became redundant with the new Foundation fullerene item, so it was deepened rather than duplicated:
- was: *Describe the structure of buckminsterfullerene (C₆₀) and state one of its uses* (apply)
- now: *Explain why buckminsterfullerene (C₆₀) can be used to deliver drugs to specific parts of the body* (reason — a drug molecule is carried inside the hollow cage).

**Moved:** none. The Higher graphene reasoning item, the nanotube "suggest why" item, and all diamond/graphite/silicon-dioxide items are unchanged and stay where they were.

---

## How the tiers work (the difficulty model you set)

- **Difficulty follows the tier, not the pathway.** Combined-Foundation and Triple-Foundation are the **same difficulty**; Combined-Higher and Triple-Higher both **scale up** to genuine Higher demand.
- **Triple's extra is coverage, not a harder version of the same content.** Triple-Foundation = the exact Combined-Foundation set **+ 2 extra Foundation-level questions**; Triple-Higher = the exact Combined-Higher set **+ 2 extra Higher/depth questions**. So Foundation students see the same difficulty on both pathways, and Triple students simply get more.
- **Every stem is exam-register** (uses an AQA command word) and **every wrong option carries a diagnostic** naming the misconception or error.
- **Counts:** Combined 10 / tier, Triple 12 / tier (10 + 2 extra). `nanoparticles` is Triple-only.

### ⭐ Full-review checklist (per the review-tiering rule)

All calculation / formula-derivation items and all FIFA are flagged ⭐ for your full review; recall/comprehension items are left for your sampling. The ⭐ items are:

- **Ionic Bonding** — 5 calc/derivation item(s)
- **Ionic Compounds** — 2 calc/derivation item(s)
- **Covalent Bonding** — 1 calc/derivation item(s)
- **Structure and Properties of Ionic Compounds** — 4 calc/derivation item(s)
- **Nanoparticles** — 2 calc/derivation item(s), FIFA worked examples (TF + TH)

### Audit status (self-checked with `audit_content.py`)

- **Before:** every page had 2 questions with Foundation = Higher = Triple verbatim — 46 count-criticals, 46 mistake-first majors, 45 tier-integrity/triple-depth majors, 38 register-minors across the unit.
- **After:** **zero critical, zero content majors.** The only remaining flags are: **(a)** a systemic `no interactive practice mode` **major** on `nanoparticles` (both Triple tiers) — the current template renders static FIFA steps only, which is the redesign port's job (MRB-113), **not** a content defect; and **(b)** 4 `info` notes on `polymers` (it keeps its polymerisation equation but has no FIFA — expected, since Bonding has no calculation there).

---

## Chemical Bonds  ·  `chemical-bonds`  ·  AQA 5.2.1.1

> 🚩 **Triple-depth call (your review):** MATCHED — AQA 5.2.1.1 (the three bond types) is identical for Combined and Triple. Foundation difficulty is the same across both pathways; Triple sets = Combined + extra same-difficulty coverage. No AQA Triple-only content on this page.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often think that when a simple molecular substance melts, its covalent bonds break. They do not: melting only separates whole molecules from each other by overcoming the weak intermolecular forces between them. The strong covalent bonds inside each molecule stay intact — which is why a low melting point tells you nothing about how strong the covalent bonds themselves are.

**Question sets by tier** (each item shows tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (4 recall / 6 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Sodium chloride is made from a metal and a non-metal. Predict the type of bonding it contains and describe how it forms.
- [✔︎] Ionic — the metal atom transfers electrons to the non-metal, forming oppositely charged ions that attract
- [ ] Covalent — the metal and non-metal share a pair of electrons
    - *why wrong:* Sharing electrons is covalent bonding, and it occurs between two NON-metals — not a metal with a non-metal.
- [ ] Metallic — the atoms sit in a sea of delocalised electrons
    - *why wrong:* Metallic bonding needs metal atoms only (a pure metal or alloy), not a metal combined with a non-metal.
- [ ] Hydrogen bonding — a weak attraction forms between the two atoms
    - *why wrong:* Hydrogen bonding is a weak intermolecular force, not the main bond between a metal and a non-metal.

**Q2. [apply · CFCHTFTH]** Magnesium (Group 2) reacts with oxygen (Group 6) to form magnesium oxide. Identify the type of bonding in MgO.
- [✔︎] Ionic — magnesium transfers 2 electrons to oxygen, forming Mg²⁺ and O²⁻ ions
- [ ] Covalent — they share 2 electrons to fill their outer shells
    - *why wrong:* Sharing electrons is covalent and only happens between two non-metals; magnesium is a metal.
- [ ] Metallic — magnesium releases electrons into a sea
    - *why wrong:* Metallic bonding occurs in metals only, not in a compound of a metal with a non-metal.
- [ ] No bonding — both are stable so they do not react
    - *why wrong:* Magnesium burns vigorously in oxygen — MgO is a stable ionic compound.

**Q3. [apply · CFCHTFTH]** Water (H₂O) is made from two non-metals. Predict the type of bonding it contains.
- [✔︎] Covalent — the non-metal atoms share pairs of electrons
- [ ] Ionic — one atom transfers electrons to the other
    - *why wrong:* Electron transfer (ionic) happens between a metal and a non-metal; hydrogen and oxygen are both non-metals.
- [ ] Metallic — the atoms share a sea of delocalised electrons
    - *why wrong:* Metallic bonding needs metal atoms; water contains none.
- [ ] Ionic — because water can conduct electricity
    - *why wrong:* Pure water barely conducts; where it does, it is due to tiny amounts of ions, not because it is ionic.

**Q4. [reason · CFCHTFTH]** Explain why copper is described as having metallic bonding.
- [✔︎] Its atoms release outer electrons into a delocalised sea, and the positive ions are attracted to that sea
- [ ] Its atoms share pairs of electrons in covalent bonds
    - *why wrong:* Sharing pairs of electrons is covalent bonding, which occurs between non-metals — copper is a metal.
- [ ] It transfers electrons to form positive and negative ions
    - *why wrong:* Transfer forming positive and negative ions is ionic bonding, which needs a non-metal as well.
- [ ] Its atoms are simply packed closely together with no forces between them
    - *why wrong:* There ARE strong forces — the electrostatic attraction between the positive ions and the electron sea.

**Q5. [reason · CFCHTFTH]** Describe the difference in how electrons behave in ionic bonding compared with covalent bonding.
- [✔︎] In ionic bonding electrons are transferred from one atom to another; in covalent bonding electrons are shared between atoms
- [ ] In ionic bonding electrons are shared; in covalent bonding they are transferred
    - *why wrong:* This is the wrong way round: ionic = transfer, covalent = sharing.
- [ ] In both, electrons are transferred, but ionic bonds are stronger
    - *why wrong:* Covalent bonding is sharing, not transfer; only ionic bonding transfers electrons.
- [ ] In both, electrons are shared, but covalent bonds involve metals
    - *why wrong:* Covalent bonding is sharing (not transfer) and occurs between non-metals, not metals.

**Q6. [recall · CFTF]** State why atoms form chemical bonds.
- [✔︎] To gain a full, stable outer shell of electrons, like the noble gases
- [ ] To increase their mass
    - *why wrong:* Bonding rearranges electrons, not mass — the number of protons and neutrons is unchanged.
- [ ] To become radioactive
    - *why wrong:* Bonding has nothing to do with radioactivity, which involves the nucleus.
- [ ] To lose all of their electrons
    - *why wrong:* Atoms aim for a FULL outer shell, not an empty one — many gain or share electrons rather than lose them.

**Q7. [recall · CFTF]** Name the type of bonding that occurs in a pure metal such as iron.
- [✔︎] Metallic
- [ ] Ionic
    - *why wrong:* Ionic bonding needs a metal AND a non-metal; pure iron is a metal only.
- [ ] Covalent
    - *why wrong:* Covalent bonding is sharing between non-metals; iron is a metal.
- [ ] Intermolecular
    - *why wrong:* Intermolecular forces act between molecules; a pure metal has no molecules.

**Q8. [recall · CFTF]** Name the type of bonding that forms between two non-metals.
- [✔︎] Covalent
- [ ] Ionic
    - *why wrong:* Ionic bonding forms between a metal and a non-metal, not two non-metals.
- [ ] Metallic
    - *why wrong:* Metallic bonding needs metal atoms only.
- [ ] No bond forms
    - *why wrong:* Two non-metals do bond — by sharing electrons (covalent).

**Q9. [recall · CFTF]** State whether a metal atom loses or gains electrons when it forms an ion.
- [✔︎] Loses electrons, forming a positive ion
- [ ] Gains electrons, forming a positive ion
    - *why wrong:* Gaining electrons would make it negative; losing them is what makes a metal ion positive.
- [ ] Loses electrons, forming a negative ion
    - *why wrong:* Losing electrons gives a POSITIVE ion (fewer electrons than protons), not a negative one.
- [ ] Gains electrons, forming a negative ion
    - *why wrong:* Gaining electrons is what non-metals do to form negative ions; metals lose electrons.

**Q10. [apply · CFTF]** Identify which substance contains ionic bonding.
- [✔︎] Sodium chloride
- [ ] Oxygen gas
    - *why wrong:* Oxygen (O₂) is two non-metals joined by a covalent bond, not ionic.
- [ ] Copper metal
    - *why wrong:* Copper is a pure metal — its bonding is metallic.
- [ ] Diamond
    - *why wrong:* Diamond is carbon only, held by covalent bonds throughout a giant structure — not ionic.

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Sodium chloride is made from a metal and a non-metal. Predict the type of bonding it contains and describe how it forms.
- [✔︎] Ionic — the metal atom transfers electrons to the non-metal, forming oppositely charged ions that attract
- [ ] Covalent — the metal and non-metal share a pair of electrons
    - *why wrong:* Sharing electrons is covalent bonding, and it occurs between two NON-metals — not a metal with a non-metal.
- [ ] Metallic — the atoms sit in a sea of delocalised electrons
    - *why wrong:* Metallic bonding needs metal atoms only (a pure metal or alloy), not a metal combined with a non-metal.
- [ ] Hydrogen bonding — a weak attraction forms between the two atoms
    - *why wrong:* Hydrogen bonding is a weak intermolecular force, not the main bond between a metal and a non-metal.

**Q2. [apply · CFCHTFTH]** Magnesium (Group 2) reacts with oxygen (Group 6) to form magnesium oxide. Identify the type of bonding in MgO.
- [✔︎] Ionic — magnesium transfers 2 electrons to oxygen, forming Mg²⁺ and O²⁻ ions
- [ ] Covalent — they share 2 electrons to fill their outer shells
    - *why wrong:* Sharing electrons is covalent and only happens between two non-metals; magnesium is a metal.
- [ ] Metallic — magnesium releases electrons into a sea
    - *why wrong:* Metallic bonding occurs in metals only, not in a compound of a metal with a non-metal.
- [ ] No bonding — both are stable so they do not react
    - *why wrong:* Magnesium burns vigorously in oxygen — MgO is a stable ionic compound.

**Q3. [apply · CFCHTFTH]** Water (H₂O) is made from two non-metals. Predict the type of bonding it contains.
- [✔︎] Covalent — the non-metal atoms share pairs of electrons
- [ ] Ionic — one atom transfers electrons to the other
    - *why wrong:* Electron transfer (ionic) happens between a metal and a non-metal; hydrogen and oxygen are both non-metals.
- [ ] Metallic — the atoms share a sea of delocalised electrons
    - *why wrong:* Metallic bonding needs metal atoms; water contains none.
- [ ] Ionic — because water can conduct electricity
    - *why wrong:* Pure water barely conducts; where it does, it is due to tiny amounts of ions, not because it is ionic.

**Q4. [reason · CFCHTFTH]** Explain why copper is described as having metallic bonding.
- [✔︎] Its atoms release outer electrons into a delocalised sea, and the positive ions are attracted to that sea
- [ ] Its atoms share pairs of electrons in covalent bonds
    - *why wrong:* Sharing pairs of electrons is covalent bonding, which occurs between non-metals — copper is a metal.
- [ ] It transfers electrons to form positive and negative ions
    - *why wrong:* Transfer forming positive and negative ions is ionic bonding, which needs a non-metal as well.
- [ ] Its atoms are simply packed closely together with no forces between them
    - *why wrong:* There ARE strong forces — the electrostatic attraction between the positive ions and the electron sea.

**Q5. [reason · CFCHTFTH]** Describe the difference in how electrons behave in ionic bonding compared with covalent bonding.
- [✔︎] In ionic bonding electrons are transferred from one atom to another; in covalent bonding electrons are shared between atoms
- [ ] In ionic bonding electrons are shared; in covalent bonding they are transferred
    - *why wrong:* This is the wrong way round: ionic = transfer, covalent = sharing.
- [ ] In both, electrons are transferred, but ionic bonds are stronger
    - *why wrong:* Covalent bonding is sharing, not transfer; only ionic bonding transfers electrons.
- [ ] In both, electrons are shared, but covalent bonds involve metals
    - *why wrong:* Covalent bonding is sharing (not transfer) and occurs between non-metals, not metals.

**Q6. [reason · CHTH]** A substance has a high melting point and conducts electricity only when molten or dissolved, never when solid. Deduce its type of bonding and justify your answer.
- [✔︎] Ionic — the ions are fixed in the solid but become free to move (and carry charge) when molten or dissolved
- [ ] Metallic — delocalised electrons carry charge in all states
    - *why wrong:* A metal would conduct as a SOLID too (delocalised electrons move in the solid) — this substance does not.
- [ ] Simple covalent — the molecules move when the substance melts
    - *why wrong:* Simple covalent substances have LOW melting points and never conduct (no charged particles).
- [ ] Giant covalent — the electrons are released only on melting
    - *why wrong:* Giant covalent substances (e.g. diamond) do not conduct even when molten — no free charges (graphite excepted).

**Q7. [reason · CHTH]** Compare ionic bonding and metallic bonding in terms of the particles present and the forces holding them together.
- [✔︎] Ionic: oppositely charged ions attracted by electrostatic forces. Metallic: positive ions attracted to a sea of delocalised electrons
- [ ] Both contain only neutral atoms held together by shared electron pairs
    - *why wrong:* Neither is neutral atoms sharing pairs — that describes covalent bonding.
- [ ] Ionic contains delocalised electrons; metallic contains positive and negative ions
    - *why wrong:* This swaps the two over: delocalised electrons are in METALS; positive and negative ions are in IONIC compounds.
- [ ] Both contain positive and negative ions attracting each other
    - *why wrong:* Metals do not contain negative ions — they have positive ions and a sea of (negative) delocalised electrons.

**Q8. [reason · CHTH]** Explain why the type of bonding in a substance can often be predicted from the positions of its elements in the periodic table.
- [✔︎] Metals (left/centre) tend to lose electrons and non-metals (right) tend to gain or share them, so the combination of positions predicts transfer, sharing or a metallic sea
- [ ] Elements in the same period always bond ionically
    - *why wrong:* It is not the period that decides bonding, but whether each element is a metal or a non-metal.
- [ ] The bond type depends only on the atomic mass, which increases across the table
    - *why wrong:* Atomic mass does not determine bond type; whether atoms lose, gain or share electrons does.
- [ ] All elements on the right of the table form metallic bonds
    - *why wrong:* The right-hand side of the table is the NON-metals, which form covalent or ionic bonds, not metallic.

**Q9. [reason · CHTH]** A shiny solid conducts electricity and can be bent into shape without breaking. Deduce its type of bonding and explain both properties.
- [✔︎] Metallic — delocalised electrons carry the current, and layers of ions can slide so it bends rather than shatters
- [ ] Ionic — the ions carry current and slide over each other
    - *why wrong:* Ionic solids do NOT conduct (ions fixed) and are brittle — they shatter, not bend.
- [ ] Simple covalent — the molecules conduct and flex
    - *why wrong:* Simple covalent substances do not conduct at all (no charged particles).
- [ ] Giant covalent — free electrons conduct and the rigid lattice bends
    - *why wrong:* Giant covalent substances are hard and rigid, not bendable, and mostly do not conduct.

**Q10. [reason · CHTH]** Explain why solid magnesium chloride does not conduct electricity, but molten magnesium chloride does.
- [✔︎] In the solid the ions are locked in fixed positions; when molten they are free to move and carry charge
- [ ] Solid magnesium chloride has no ions until it melts
    - *why wrong:* The Mg²⁺ and Cl⁻ ions exist in the solid lattice already — they simply cannot move when solid.
- [ ] Melting adds electrons that carry the current
    - *why wrong:* Conduction in molten ionic compounds is by moving IONS, not by added electrons.
- [ ] The solid is too cold for any current to flow
    - *why wrong:* Temperature alone is not the point — it is whether the charged ions are free to move.

### Triple Foundation — 12 questions (4 recall / 8 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Sodium chloride is made from a metal and a non-metal. Predict the type of bonding it contains and describe how it forms.
- [✔︎] Ionic — the metal atom transfers electrons to the non-metal, forming oppositely charged ions that attract
- [ ] Covalent — the metal and non-metal share a pair of electrons
    - *why wrong:* Sharing electrons is covalent bonding, and it occurs between two NON-metals — not a metal with a non-metal.
- [ ] Metallic — the atoms sit in a sea of delocalised electrons
    - *why wrong:* Metallic bonding needs metal atoms only (a pure metal or alloy), not a metal combined with a non-metal.
- [ ] Hydrogen bonding — a weak attraction forms between the two atoms
    - *why wrong:* Hydrogen bonding is a weak intermolecular force, not the main bond between a metal and a non-metal.

**Q2. [apply · CFCHTFTH]** Magnesium (Group 2) reacts with oxygen (Group 6) to form magnesium oxide. Identify the type of bonding in MgO.
- [✔︎] Ionic — magnesium transfers 2 electrons to oxygen, forming Mg²⁺ and O²⁻ ions
- [ ] Covalent — they share 2 electrons to fill their outer shells
    - *why wrong:* Sharing electrons is covalent and only happens between two non-metals; magnesium is a metal.
- [ ] Metallic — magnesium releases electrons into a sea
    - *why wrong:* Metallic bonding occurs in metals only, not in a compound of a metal with a non-metal.
- [ ] No bonding — both are stable so they do not react
    - *why wrong:* Magnesium burns vigorously in oxygen — MgO is a stable ionic compound.

**Q3. [apply · CFCHTFTH]** Water (H₂O) is made from two non-metals. Predict the type of bonding it contains.
- [✔︎] Covalent — the non-metal atoms share pairs of electrons
- [ ] Ionic — one atom transfers electrons to the other
    - *why wrong:* Electron transfer (ionic) happens between a metal and a non-metal; hydrogen and oxygen are both non-metals.
- [ ] Metallic — the atoms share a sea of delocalised electrons
    - *why wrong:* Metallic bonding needs metal atoms; water contains none.
- [ ] Ionic — because water can conduct electricity
    - *why wrong:* Pure water barely conducts; where it does, it is due to tiny amounts of ions, not because it is ionic.

**Q4. [reason · CFCHTFTH]** Explain why copper is described as having metallic bonding.
- [✔︎] Its atoms release outer electrons into a delocalised sea, and the positive ions are attracted to that sea
- [ ] Its atoms share pairs of electrons in covalent bonds
    - *why wrong:* Sharing pairs of electrons is covalent bonding, which occurs between non-metals — copper is a metal.
- [ ] It transfers electrons to form positive and negative ions
    - *why wrong:* Transfer forming positive and negative ions is ionic bonding, which needs a non-metal as well.
- [ ] Its atoms are simply packed closely together with no forces between them
    - *why wrong:* There ARE strong forces — the electrostatic attraction between the positive ions and the electron sea.

**Q5. [reason · CFCHTFTH]** Describe the difference in how electrons behave in ionic bonding compared with covalent bonding.
- [✔︎] In ionic bonding electrons are transferred from one atom to another; in covalent bonding electrons are shared between atoms
- [ ] In ionic bonding electrons are shared; in covalent bonding they are transferred
    - *why wrong:* This is the wrong way round: ionic = transfer, covalent = sharing.
- [ ] In both, electrons are transferred, but ionic bonds are stronger
    - *why wrong:* Covalent bonding is sharing, not transfer; only ionic bonding transfers electrons.
- [ ] In both, electrons are shared, but covalent bonds involve metals
    - *why wrong:* Covalent bonding is sharing (not transfer) and occurs between non-metals, not metals.

**Q6. [recall · CFTF]** State why atoms form chemical bonds.
- [✔︎] To gain a full, stable outer shell of electrons, like the noble gases
- [ ] To increase their mass
    - *why wrong:* Bonding rearranges electrons, not mass — the number of protons and neutrons is unchanged.
- [ ] To become radioactive
    - *why wrong:* Bonding has nothing to do with radioactivity, which involves the nucleus.
- [ ] To lose all of their electrons
    - *why wrong:* Atoms aim for a FULL outer shell, not an empty one — many gain or share electrons rather than lose them.

**Q7. [recall · CFTF]** Name the type of bonding that occurs in a pure metal such as iron.
- [✔︎] Metallic
- [ ] Ionic
    - *why wrong:* Ionic bonding needs a metal AND a non-metal; pure iron is a metal only.
- [ ] Covalent
    - *why wrong:* Covalent bonding is sharing between non-metals; iron is a metal.
- [ ] Intermolecular
    - *why wrong:* Intermolecular forces act between molecules; a pure metal has no molecules.

**Q8. [recall · CFTF]** Name the type of bonding that forms between two non-metals.
- [✔︎] Covalent
- [ ] Ionic
    - *why wrong:* Ionic bonding forms between a metal and a non-metal, not two non-metals.
- [ ] Metallic
    - *why wrong:* Metallic bonding needs metal atoms only.
- [ ] No bond forms
    - *why wrong:* Two non-metals do bond — by sharing electrons (covalent).

**Q9. [recall · CFTF]** State whether a metal atom loses or gains electrons when it forms an ion.
- [✔︎] Loses electrons, forming a positive ion
- [ ] Gains electrons, forming a positive ion
    - *why wrong:* Gaining electrons would make it negative; losing them is what makes a metal ion positive.
- [ ] Loses electrons, forming a negative ion
    - *why wrong:* Losing electrons gives a POSITIVE ion (fewer electrons than protons), not a negative one.
- [ ] Gains electrons, forming a negative ion
    - *why wrong:* Gaining electrons is what non-metals do to form negative ions; metals lose electrons.

**Q10. [apply · CFTF]** Identify which substance contains ionic bonding.
- [✔︎] Sodium chloride
- [ ] Oxygen gas
    - *why wrong:* Oxygen (O₂) is two non-metals joined by a covalent bond, not ionic.
- [ ] Copper metal
    - *why wrong:* Copper is a pure metal — its bonding is metallic.
- [ ] Diamond
    - *why wrong:* Diamond is carbon only, held by covalent bonds throughout a giant structure — not ionic.

**Q11. [apply · TF]** Identify a property that is typical of ionic compounds.
- [✔︎] A high melting point
- [ ] Conducts electricity when solid
    - *why wrong:* Ionic compounds do NOT conduct when solid — the ions are fixed in the lattice.
- [ ] A low melting point
    - *why wrong:* Ionic compounds have HIGH melting points because of strong forces throughout the lattice.
- [ ] Can be hammered into shape (malleable)
    - *why wrong:* Ionic compounds are brittle and shatter when struck; malleability is a property of metals.

**Q12. [reason · TF]** Carbon dioxide is made from two non-metals. Predict whether it conducts electricity and give a reason.
- [✔︎] It does not conduct, because it is made of molecules with no free electrons or ions
- [ ] It conducts, because it contains carbon which is a good conductor
    - *why wrong:* Graphite conducts, but CO₂ is a small covalent MOLECULE with no delocalised electrons — not the same thing.
- [ ] It conducts, because gases always conduct electricity
    - *why wrong:* Most gases do not conduct; conduction needs free charged particles, which CO₂ molecules lack.
- [ ] It does not conduct, because its covalent bonds are too weak
    - *why wrong:* Bond strength is irrelevant to conduction — what matters is the absence of free charged particles.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Sodium chloride is made from a metal and a non-metal. Predict the type of bonding it contains and describe how it forms.
- [✔︎] Ionic — the metal atom transfers electrons to the non-metal, forming oppositely charged ions that attract
- [ ] Covalent — the metal and non-metal share a pair of electrons
    - *why wrong:* Sharing electrons is covalent bonding, and it occurs between two NON-metals — not a metal with a non-metal.
- [ ] Metallic — the atoms sit in a sea of delocalised electrons
    - *why wrong:* Metallic bonding needs metal atoms only (a pure metal or alloy), not a metal combined with a non-metal.
- [ ] Hydrogen bonding — a weak attraction forms between the two atoms
    - *why wrong:* Hydrogen bonding is a weak intermolecular force, not the main bond between a metal and a non-metal.

**Q2. [apply · CFCHTFTH]** Magnesium (Group 2) reacts with oxygen (Group 6) to form magnesium oxide. Identify the type of bonding in MgO.
- [✔︎] Ionic — magnesium transfers 2 electrons to oxygen, forming Mg²⁺ and O²⁻ ions
- [ ] Covalent — they share 2 electrons to fill their outer shells
    - *why wrong:* Sharing electrons is covalent and only happens between two non-metals; magnesium is a metal.
- [ ] Metallic — magnesium releases electrons into a sea
    - *why wrong:* Metallic bonding occurs in metals only, not in a compound of a metal with a non-metal.
- [ ] No bonding — both are stable so they do not react
    - *why wrong:* Magnesium burns vigorously in oxygen — MgO is a stable ionic compound.

**Q3. [apply · CFCHTFTH]** Water (H₂O) is made from two non-metals. Predict the type of bonding it contains.
- [✔︎] Covalent — the non-metal atoms share pairs of electrons
- [ ] Ionic — one atom transfers electrons to the other
    - *why wrong:* Electron transfer (ionic) happens between a metal and a non-metal; hydrogen and oxygen are both non-metals.
- [ ] Metallic — the atoms share a sea of delocalised electrons
    - *why wrong:* Metallic bonding needs metal atoms; water contains none.
- [ ] Ionic — because water can conduct electricity
    - *why wrong:* Pure water barely conducts; where it does, it is due to tiny amounts of ions, not because it is ionic.

**Q4. [reason · CFCHTFTH]** Explain why copper is described as having metallic bonding.
- [✔︎] Its atoms release outer electrons into a delocalised sea, and the positive ions are attracted to that sea
- [ ] Its atoms share pairs of electrons in covalent bonds
    - *why wrong:* Sharing pairs of electrons is covalent bonding, which occurs between non-metals — copper is a metal.
- [ ] It transfers electrons to form positive and negative ions
    - *why wrong:* Transfer forming positive and negative ions is ionic bonding, which needs a non-metal as well.
- [ ] Its atoms are simply packed closely together with no forces between them
    - *why wrong:* There ARE strong forces — the electrostatic attraction between the positive ions and the electron sea.

**Q5. [reason · CFCHTFTH]** Describe the difference in how electrons behave in ionic bonding compared with covalent bonding.
- [✔︎] In ionic bonding electrons are transferred from one atom to another; in covalent bonding electrons are shared between atoms
- [ ] In ionic bonding electrons are shared; in covalent bonding they are transferred
    - *why wrong:* This is the wrong way round: ionic = transfer, covalent = sharing.
- [ ] In both, electrons are transferred, but ionic bonds are stronger
    - *why wrong:* Covalent bonding is sharing, not transfer; only ionic bonding transfers electrons.
- [ ] In both, electrons are shared, but covalent bonds involve metals
    - *why wrong:* Covalent bonding is sharing (not transfer) and occurs between non-metals, not metals.

**Q6. [reason · CHTH]** A substance has a high melting point and conducts electricity only when molten or dissolved, never when solid. Deduce its type of bonding and justify your answer.
- [✔︎] Ionic — the ions are fixed in the solid but become free to move (and carry charge) when molten or dissolved
- [ ] Metallic — delocalised electrons carry charge in all states
    - *why wrong:* A metal would conduct as a SOLID too (delocalised electrons move in the solid) — this substance does not.
- [ ] Simple covalent — the molecules move when the substance melts
    - *why wrong:* Simple covalent substances have LOW melting points and never conduct (no charged particles).
- [ ] Giant covalent — the electrons are released only on melting
    - *why wrong:* Giant covalent substances (e.g. diamond) do not conduct even when molten — no free charges (graphite excepted).

**Q7. [reason · CHTH]** Compare ionic bonding and metallic bonding in terms of the particles present and the forces holding them together.
- [✔︎] Ionic: oppositely charged ions attracted by electrostatic forces. Metallic: positive ions attracted to a sea of delocalised electrons
- [ ] Both contain only neutral atoms held together by shared electron pairs
    - *why wrong:* Neither is neutral atoms sharing pairs — that describes covalent bonding.
- [ ] Ionic contains delocalised electrons; metallic contains positive and negative ions
    - *why wrong:* This swaps the two over: delocalised electrons are in METALS; positive and negative ions are in IONIC compounds.
- [ ] Both contain positive and negative ions attracting each other
    - *why wrong:* Metals do not contain negative ions — they have positive ions and a sea of (negative) delocalised electrons.

**Q8. [reason · CHTH]** Explain why the type of bonding in a substance can often be predicted from the positions of its elements in the periodic table.
- [✔︎] Metals (left/centre) tend to lose electrons and non-metals (right) tend to gain or share them, so the combination of positions predicts transfer, sharing or a metallic sea
- [ ] Elements in the same period always bond ionically
    - *why wrong:* It is not the period that decides bonding, but whether each element is a metal or a non-metal.
- [ ] The bond type depends only on the atomic mass, which increases across the table
    - *why wrong:* Atomic mass does not determine bond type; whether atoms lose, gain or share electrons does.
- [ ] All elements on the right of the table form metallic bonds
    - *why wrong:* The right-hand side of the table is the NON-metals, which form covalent or ionic bonds, not metallic.

**Q9. [reason · CHTH]** A shiny solid conducts electricity and can be bent into shape without breaking. Deduce its type of bonding and explain both properties.
- [✔︎] Metallic — delocalised electrons carry the current, and layers of ions can slide so it bends rather than shatters
- [ ] Ionic — the ions carry current and slide over each other
    - *why wrong:* Ionic solids do NOT conduct (ions fixed) and are brittle — they shatter, not bend.
- [ ] Simple covalent — the molecules conduct and flex
    - *why wrong:* Simple covalent substances do not conduct at all (no charged particles).
- [ ] Giant covalent — free electrons conduct and the rigid lattice bends
    - *why wrong:* Giant covalent substances are hard and rigid, not bendable, and mostly do not conduct.

**Q10. [reason · CHTH]** Explain why solid magnesium chloride does not conduct electricity, but molten magnesium chloride does.
- [✔︎] In the solid the ions are locked in fixed positions; when molten they are free to move and carry charge
- [ ] Solid magnesium chloride has no ions until it melts
    - *why wrong:* The Mg²⁺ and Cl⁻ ions exist in the solid lattice already — they simply cannot move when solid.
- [ ] Melting adds electrons that carry the current
    - *why wrong:* Conduction in molten ionic compounds is by moving IONS, not by added electrons.
- [ ] The solid is too cold for any current to flow
    - *why wrong:* Temperature alone is not the point — it is whether the charged ions are free to move.

**Q11. [reason · TH]** A compound conducts electricity when molten but not when solid, and shatters when hit. Deduce its structure and bonding, and explain the shattering.
- [✔︎] A giant ionic lattice — when a force shifts the layers, like-charged ions line up and repel, so the crystal shatters
- [ ] A metallic lattice — the layers slide and the metal cracks
    - *why wrong:* Metals do the opposite — layers slide and the metal bends without shattering.
- [ ] A simple molecular structure — the weak molecules break apart
    - *why wrong:* Simple molecular substances do not conduct when molten (no charged particles), so this is not one.
- [ ] A giant covalent structure — the covalent bonds bend and snap
    - *why wrong:* Giant covalent substances do not conduct when molten either (graphite excepted); this compound does.

**Q12. [reason · TH]** Explain why metals and ionic compounds can both have high melting points, even though their bonding is different.
- [✔︎] Both are giant structures with many strong electrostatic attractions throughout (metal: ions to electron sea; ionic: oppositely charged ions), so a lot of energy is needed to break them
- [ ] Both contain molecules held by strong intermolecular forces
    - *why wrong:* Neither is molecular — both are giant structures, which is exactly why their melting points are high.
- [ ] Both contain the same delocalised electrons
    - *why wrong:* Only metals contain delocalised electrons; ionic compounds have fixed ions, yet both still melt at high temperatures.
- [ ] Both are made of the same size of particle
    - *why wrong:* Particle size is not the reason; the strength and number of electrostatic attractions is.


---

## Ionic Bonding  ·  `ionic-bonding`  ·  AQA 5.2.1.2

> 🚩 **Triple-depth call (your review):** MATCHED — AQA 5.2.1.2 is identical for Combined and Triple. Foundation difficulty is the same across both pathways (Triple-Foundation = Combined-Foundation + two extra Foundation-level formula items for coverage). The two Triple-Higher-only items (X²⁺/Y³⁻ formula, dot-and-cross limitation) are genuine HIGHER-tier reasoning, not harder-than-spec content — confirmed for placement at Triple Higher.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often say the ionic bond IS the transfer of electrons from the metal to the non-metal. That is not the bond: the transfer is a one-off event that only creates the ions. The ionic bond itself is the strong electrostatic attraction between the oppositely charged ions produced. Remember too that these charges must balance, so every ionic compound has an overall charge of zero.

**Question sets by tier** (each item shows tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (4 recall / 6 apply+reason+calc)

**Q1. [recall · CFTF]** State the type of bonding that forms when a metal reacts with a non-metal.
- [✔︎] Ionic bonding — electrons are transferred from the metal to the non-metal
- [ ] Covalent bonding — the metal and non-metal share electrons
    - *why wrong:* Covalent bonding is sharing, and it happens between two NON-metals — not a metal with a non-metal.
- [ ] Metallic bonding — the atoms share a sea of delocalised electrons
    - *why wrong:* Metallic bonding occurs in metals and alloys (metal atoms only), not between a metal and a non-metal.
- [ ] No bonding — metals and non-metals do not react together
    - *why wrong:* Metals and non-metals react readily — e.g. sodium burns vigorously in chlorine to make salt.

**Q2. [apply · CFTF]** Identify the pair of elements that will form an ionic bond.
- [✔︎] Magnesium and oxygen
- [ ] Hydrogen and chlorine
    - *why wrong:* Hydrogen and chlorine are both non-metals, so they share electrons — that is a covalent bond, not ionic.
- [ ] Oxygen and nitrogen
    - *why wrong:* Oxygen and nitrogen are both non-metals, so they bond covalently (by sharing), not ionically.
- [ ] Copper and zinc
    - *why wrong:* Copper and zinc are both metals — together they form an alloy held by metallic bonding, not an ionic bond.

**Q3. [recall · CFTF]** Chlorine is in Group 7. State the charge on a chloride ion.
- [✔︎] 1−
- [ ] 1+
    - *why wrong:* Non-metals GAIN electrons to fill their outer shell — gaining makes them negative, not positive.
- [ ] 7−
    - *why wrong:* The charge is not the group number. A Group 7 atom needs just 1 more electron, so it gains 1 and becomes 1−.
- [ ] 7+
    - *why wrong:* Chlorine gains electrons (becoming negative); it does not lose 7 to become 7+.

**Q4. [recall · CFTF]** Magnesium forms a Mg²⁺ ion. State how many electrons a magnesium atom loses.
- [✔︎] 2
- [ ] 1
    - *why wrong:* Losing only 1 electron would give a 1+ ion, not the 2+ ion stated.
- [ ] 6
    - *why wrong:* Magnesium is in Group 2, so it has 2 outer electrons to lose — not 6.
- [ ] 0 — it gains 2 electrons
    - *why wrong:* Magnesium is a metal, so it LOSES electrons to form a positive ion; it does not gain them.

**Q5. [recall · CFTF]** Describe how you can use an element's group number to predict the charge on its ion.
- [✔︎] Group 1, 2 and 3 metals lose that many electrons (1+, 2+, 3+); Group 5, 6 and 7 non-metals gain electrons to reach a full shell (3−, 2−, 1−)
- [ ] The charge is always equal to the group number, whether the element is a metal or a non-metal
    - *why wrong:* For non-metals the charge is NOT the group number — Group 6 gains 2 (not 6) to become 2−.
- [ ] Metals always form 1+ ions and non-metals always form 1− ions, whatever their group
    - *why wrong:* The charge depends on the group: a Group 2 metal forms 2+, a Group 3 metal forms 3+.
- [ ] The charge equals the number of the period (row) the element is in
    - *why wrong:* The charge comes from the group (electrons gained or lost), not the period.

**Q6. [apply · CFCHTFTH]** Sodium (2.8.1) reacts with chlorine (2.8.7) to form sodium chloride. Describe what happens to the electrons.
- [✔︎] Sodium loses its 1 outer electron to form Na⁺ (2.8); chlorine gains it to form Cl⁻ (2.8.8); the oppositely charged ions then attract
- [ ] Sodium and chlorine share one pair of electrons in a single covalent bond
    - *why wrong:* Sharing is covalent bonding. NaCl is a metal + non-metal, so electrons are TRANSFERRED, not shared.
- [ ] Both atoms lose their outer electrons into a shared pool
    - *why wrong:* Only the metal (sodium) loses electrons; the non-metal (chlorine) gains them.
- [ ] Chlorine loses one electron to sodium, so chlorine becomes positive
    - *why wrong:* Chlorine GAINS the electron (it needs 1 more for a full shell), so it becomes the NEGATIVE ion.

**Q7. [reason · CFCHTFTH]** Explain why an ionic compound such as sodium chloride has no overall electrical charge.
- [✔︎] The total positive charge on the metal ions exactly balances the total negative charge on the non-metal ions
- [ ] The electrons transferred are destroyed, leaving neutral atoms
    - *why wrong:* Electrons are transferred, not destroyed — charge is conserved. The compound is neutral because the ion charges balance.
- [ ] The ions are held so tightly that their charges disappear
    - *why wrong:* Charge does not 'disappear' — the ions keep their charges; the compound is neutral because they sum to zero.
- [ ] Only the outer shells carry charge, and these cancel when the shells are full
    - *why wrong:* A full shell is not uncharged. Neutrality comes from equal amounts of positive and negative charge.

**Q8. [calc/derivation · CFCHTFTH] ⭐** Determine the formula of calcium chloride. (Calcium is in Group 2, chlorine is in Group 7.)
- [✔︎] CaCl₂ — Ca²⁺ needs two Cl⁻ ions to balance its charge
- [ ] CaCl — one calcium ion bonds with one chloride ion
    - *why wrong:* CaCl would give +2 + (−1) = +1 overall — not neutral. You need two Cl⁻ to balance one Ca²⁺.
- [ ] Ca₂Cl — two calcium ions bond with one chloride ion
    - *why wrong:* Ca₂Cl would give 2(+2) + (−1) = +3 — not neutral.
- [ ] CaCl₃ — calcium needs three chloride ions to become stable
    - *why wrong:* CaCl₃ would give +2 + 3(−1) = −1 — not neutral. Exactly two Cl⁻ balance one Ca²⁺.

**Q9. [reason · CFCHTFTH]** Explain, in terms of electron arrangement, why metals form positive ions but non-metals form negative ions.
- [✔︎] Metals have few outer electrons and lose them to empty their outer shell, leaving a positive ion; non-metals have nearly full shells and gain electrons, becoming negative
- [ ] Metals are heavier, so their nuclei pull electrons in and become positive
    - *why wrong:* Mass/heaviness does not set the charge — it is how many electrons are lost or gained to reach a full shell.
- [ ] Non-metals contain more protons, which makes them negative
    - *why wrong:* Proton number sets the element's identity, not the sign of the ion; gaining electrons is what makes non-metals negative.
- [ ] Metals gain electrons and non-metals lose them, to reach a full shell
    - *why wrong:* This is the wrong way round: metals LOSE electrons (become +), non-metals GAIN electrons (become −).

**Q10. [apply · CFCHTFTH]** Describe how a dot-and-cross diagram represents the formation of the ions in sodium chloride.
- [✔︎] Electrons from one atom are drawn as dots and from the other as crosses, showing the single outer electron moving from sodium to chlorine so each ion has a full outer shell
- [ ] It shows the sodium and chlorine sharing a pair of electrons drawn between them
    - *why wrong:* That describes a COVALENT dot-and-cross (shared pair). In NaCl the electron is transferred, not shared.
- [ ] It shows a sea of electrons moving freely around fixed positive ions
    - *why wrong:* That is the metallic bonding model, not a dot-and-cross diagram of ionic NaCl.
- [ ] It shows the chlorine atom giving one electron to the sodium atom
    - *why wrong:* The transfer is the other way: sodium (the metal) gives its electron to chlorine (the non-metal).

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Sodium (2.8.1) reacts with chlorine (2.8.7) to form sodium chloride. Describe what happens to the electrons.
- [✔︎] Sodium loses its 1 outer electron to form Na⁺ (2.8); chlorine gains it to form Cl⁻ (2.8.8); the oppositely charged ions then attract
- [ ] Sodium and chlorine share one pair of electrons in a single covalent bond
    - *why wrong:* Sharing is covalent bonding. NaCl is a metal + non-metal, so electrons are TRANSFERRED, not shared.
- [ ] Both atoms lose their outer electrons into a shared pool
    - *why wrong:* Only the metal (sodium) loses electrons; the non-metal (chlorine) gains them.
- [ ] Chlorine loses one electron to sodium, so chlorine becomes positive
    - *why wrong:* Chlorine GAINS the electron (it needs 1 more for a full shell), so it becomes the NEGATIVE ion.

**Q2. [reason · CFCHTFTH]** Explain why an ionic compound such as sodium chloride has no overall electrical charge.
- [✔︎] The total positive charge on the metal ions exactly balances the total negative charge on the non-metal ions
- [ ] The electrons transferred are destroyed, leaving neutral atoms
    - *why wrong:* Electrons are transferred, not destroyed — charge is conserved. The compound is neutral because the ion charges balance.
- [ ] The ions are held so tightly that their charges disappear
    - *why wrong:* Charge does not 'disappear' — the ions keep their charges; the compound is neutral because they sum to zero.
- [ ] Only the outer shells carry charge, and these cancel when the shells are full
    - *why wrong:* A full shell is not uncharged. Neutrality comes from equal amounts of positive and negative charge.

**Q3. [calc/derivation · CFCHTFTH] ⭐** Determine the formula of calcium chloride. (Calcium is in Group 2, chlorine is in Group 7.)
- [✔︎] CaCl₂ — Ca²⁺ needs two Cl⁻ ions to balance its charge
- [ ] CaCl — one calcium ion bonds with one chloride ion
    - *why wrong:* CaCl would give +2 + (−1) = +1 overall — not neutral. You need two Cl⁻ to balance one Ca²⁺.
- [ ] Ca₂Cl — two calcium ions bond with one chloride ion
    - *why wrong:* Ca₂Cl would give 2(+2) + (−1) = +3 — not neutral.
- [ ] CaCl₃ — calcium needs three chloride ions to become stable
    - *why wrong:* CaCl₃ would give +2 + 3(−1) = −1 — not neutral. Exactly two Cl⁻ balance one Ca²⁺.

**Q4. [reason · CFCHTFTH]** Explain, in terms of electron arrangement, why metals form positive ions but non-metals form negative ions.
- [✔︎] Metals have few outer electrons and lose them to empty their outer shell, leaving a positive ion; non-metals have nearly full shells and gain electrons, becoming negative
- [ ] Metals are heavier, so their nuclei pull electrons in and become positive
    - *why wrong:* Mass/heaviness does not set the charge — it is how many electrons are lost or gained to reach a full shell.
- [ ] Non-metals contain more protons, which makes them negative
    - *why wrong:* Proton number sets the element's identity, not the sign of the ion; gaining electrons is what makes non-metals negative.
- [ ] Metals gain electrons and non-metals lose them, to reach a full shell
    - *why wrong:* This is the wrong way round: metals LOSE electrons (become +), non-metals GAIN electrons (become −).

**Q5. [apply · CFCHTFTH]** Describe how a dot-and-cross diagram represents the formation of the ions in sodium chloride.
- [✔︎] Electrons from one atom are drawn as dots and from the other as crosses, showing the single outer electron moving from sodium to chlorine so each ion has a full outer shell
- [ ] It shows the sodium and chlorine sharing a pair of electrons drawn between them
    - *why wrong:* That describes a COVALENT dot-and-cross (shared pair). In NaCl the electron is transferred, not shared.
- [ ] It shows a sea of electrons moving freely around fixed positive ions
    - *why wrong:* That is the metallic bonding model, not a dot-and-cross diagram of ionic NaCl.
- [ ] It shows the chlorine atom giving one electron to the sodium atom
    - *why wrong:* The transfer is the other way: sodium (the metal) gives its electron to chlorine (the non-metal).

**Q6. [calc/derivation · CHTFTH] ⭐** Magnesium reacts with chlorine. Deduce the formula of the compound formed and justify it using the ion charges.
- [✔︎] MgCl₂ — Mg²⁺ has a 2+ charge, so it needs two Cl⁻ ions to balance it
- [ ] MgCl — one magnesium ion pairs with one chloride ion
    - *why wrong:* MgCl gives +2 + (−1) = +1 — not neutral. Two Cl⁻ are needed to balance Mg²⁺.
- [ ] Mg₂Cl — two magnesium ions pair with one chloride ion
    - *why wrong:* Mg₂Cl gives 2(+2) + (−1) = +3 — not neutral.
- [ ] MgCl₃ — magnesium needs three chloride ions
    - *why wrong:* MgCl₃ gives +2 + 3(−1) = −1 — not neutral; only two Cl⁻ are required.

**Q7. [reason · CHTH]** A student writes: 'The ionic bond is the transfer of electrons from sodium to chlorine.' Explain why this statement is not correct.
- [✔︎] The transfer only creates the ions; the ionic bond is the electrostatic attraction between the oppositely charged ions that results
- [ ] It is correct — the ionic bond is the movement of the electron
    - *why wrong:* The transfer is a one-off event, not the ongoing bond — so the statement is not correct.
- [ ] The electrons are shared, not transferred, so the description is wrong
    - *why wrong:* Sodium chloride is ionic (metal + non-metal), so electrons are transferred, not shared.
- [ ] Sodium gains the electron, so the direction of transfer is wrong
    - *why wrong:* Sodium is the metal and LOSES the electron; chlorine gains it. The stated direction is right — the error is calling the transfer 'the bond'.

**Q8. [calc/derivation · CHTFTH] ⭐** Potassium reacts with oxygen. Predict the formula of potassium oxide and justify your answer using ion charges. (K is Group 1, O is Group 6.)
- [✔︎] K₂O — each K⁺ carries 1+, so two are needed to balance one O²⁻
- [ ] KO — one potassium ion balances one oxygen ion
    - *why wrong:* KO gives +1 + (−2) = −1 — not neutral. Two K⁺ are needed to balance one O²⁻.
- [ ] KO₂ — one potassium ion needs two oxide ions
    - *why wrong:* KO₂ gives +1 + 2(−2) = −3 — not neutral.
- [ ] K₂O₃ — by analogy with aluminium oxide
    - *why wrong:* K forms 1+ (not 3+), so the aluminium-oxide pattern does not apply; K₂O is correct.

**Q9. [reason · CHTH]** Explain why the noble gases in Group 0 do not normally form ions.
- [✔︎] Their outer shells are already full, so they have no tendency to lose or gain electrons
- [ ] They are gases, and gases cannot form ions
    - *why wrong:* State of matter does not decide this — many gases form ions when they react. Noble gases don't because their shells are full.
- [ ] Their atoms are too small to hold a charge
    - *why wrong:* Atom size does not prevent ion formation; a full outer shell removes the tendency to react.
- [ ] They already exist as negative ions in nature
    - *why wrong:* Noble gases are neutral atoms with full shells, not naturally occurring ions.

**Q10. [calc/derivation · CHTH] ⭐** Explain, in terms of electron transfer, why the formula of aluminium oxide is Al₂O₃.
- [✔︎] Al loses 3 electrons to form Al³⁺ and O gains 2 to form O²⁻; balancing the charges needs two Al³⁺ (6+) and three O²⁻ (6−)
- [ ] Aluminium and oxygen share three pairs of electrons
    - *why wrong:* Aluminium oxide is ionic (metal + non-metal) — electrons are transferred, not shared.
- [ ] Aluminium forms Al²⁺ and oxygen forms O³⁻, giving Al₃O₂
    - *why wrong:* Aluminium is Group 3 (forms Al³⁺) and oxygen is Group 6 (forms O²⁻); the charges are swapped here, which would give the wrong formula.
- [ ] The subscripts 2 and 3 come from the group numbers 2 and 3
    - *why wrong:* The subscripts come from balancing the CHARGES (3+ and 2− → lowest common multiple 6), not from the group numbers directly.

### Triple Foundation — 12 questions (4 recall / 8 apply+reason+calc)

**Q1. [recall · CFTF]** State the type of bonding that forms when a metal reacts with a non-metal.
- [✔︎] Ionic bonding — electrons are transferred from the metal to the non-metal
- [ ] Covalent bonding — the metal and non-metal share electrons
    - *why wrong:* Covalent bonding is sharing, and it happens between two NON-metals — not a metal with a non-metal.
- [ ] Metallic bonding — the atoms share a sea of delocalised electrons
    - *why wrong:* Metallic bonding occurs in metals and alloys (metal atoms only), not between a metal and a non-metal.
- [ ] No bonding — metals and non-metals do not react together
    - *why wrong:* Metals and non-metals react readily — e.g. sodium burns vigorously in chlorine to make salt.

**Q2. [apply · CFTF]** Identify the pair of elements that will form an ionic bond.
- [✔︎] Magnesium and oxygen
- [ ] Hydrogen and chlorine
    - *why wrong:* Hydrogen and chlorine are both non-metals, so they share electrons — that is a covalent bond, not ionic.
- [ ] Oxygen and nitrogen
    - *why wrong:* Oxygen and nitrogen are both non-metals, so they bond covalently (by sharing), not ionically.
- [ ] Copper and zinc
    - *why wrong:* Copper and zinc are both metals — together they form an alloy held by metallic bonding, not an ionic bond.

**Q3. [recall · CFTF]** Chlorine is in Group 7. State the charge on a chloride ion.
- [✔︎] 1−
- [ ] 1+
    - *why wrong:* Non-metals GAIN electrons to fill their outer shell — gaining makes them negative, not positive.
- [ ] 7−
    - *why wrong:* The charge is not the group number. A Group 7 atom needs just 1 more electron, so it gains 1 and becomes 1−.
- [ ] 7+
    - *why wrong:* Chlorine gains electrons (becoming negative); it does not lose 7 to become 7+.

**Q4. [recall · CFTF]** Magnesium forms a Mg²⁺ ion. State how many electrons a magnesium atom loses.
- [✔︎] 2
- [ ] 1
    - *why wrong:* Losing only 1 electron would give a 1+ ion, not the 2+ ion stated.
- [ ] 6
    - *why wrong:* Magnesium is in Group 2, so it has 2 outer electrons to lose — not 6.
- [ ] 0 — it gains 2 electrons
    - *why wrong:* Magnesium is a metal, so it LOSES electrons to form a positive ion; it does not gain them.

**Q5. [recall · CFTF]** Describe how you can use an element's group number to predict the charge on its ion.
- [✔︎] Group 1, 2 and 3 metals lose that many electrons (1+, 2+, 3+); Group 5, 6 and 7 non-metals gain electrons to reach a full shell (3−, 2−, 1−)
- [ ] The charge is always equal to the group number, whether the element is a metal or a non-metal
    - *why wrong:* For non-metals the charge is NOT the group number — Group 6 gains 2 (not 6) to become 2−.
- [ ] Metals always form 1+ ions and non-metals always form 1− ions, whatever their group
    - *why wrong:* The charge depends on the group: a Group 2 metal forms 2+, a Group 3 metal forms 3+.
- [ ] The charge equals the number of the period (row) the element is in
    - *why wrong:* The charge comes from the group (electrons gained or lost), not the period.

**Q6. [apply · CFCHTFTH]** Sodium (2.8.1) reacts with chlorine (2.8.7) to form sodium chloride. Describe what happens to the electrons.
- [✔︎] Sodium loses its 1 outer electron to form Na⁺ (2.8); chlorine gains it to form Cl⁻ (2.8.8); the oppositely charged ions then attract
- [ ] Sodium and chlorine share one pair of electrons in a single covalent bond
    - *why wrong:* Sharing is covalent bonding. NaCl is a metal + non-metal, so electrons are TRANSFERRED, not shared.
- [ ] Both atoms lose their outer electrons into a shared pool
    - *why wrong:* Only the metal (sodium) loses electrons; the non-metal (chlorine) gains them.
- [ ] Chlorine loses one electron to sodium, so chlorine becomes positive
    - *why wrong:* Chlorine GAINS the electron (it needs 1 more for a full shell), so it becomes the NEGATIVE ion.

**Q7. [reason · CFCHTFTH]** Explain why an ionic compound such as sodium chloride has no overall electrical charge.
- [✔︎] The total positive charge on the metal ions exactly balances the total negative charge on the non-metal ions
- [ ] The electrons transferred are destroyed, leaving neutral atoms
    - *why wrong:* Electrons are transferred, not destroyed — charge is conserved. The compound is neutral because the ion charges balance.
- [ ] The ions are held so tightly that their charges disappear
    - *why wrong:* Charge does not 'disappear' — the ions keep their charges; the compound is neutral because they sum to zero.
- [ ] Only the outer shells carry charge, and these cancel when the shells are full
    - *why wrong:* A full shell is not uncharged. Neutrality comes from equal amounts of positive and negative charge.

**Q8. [calc/derivation · CFCHTFTH] ⭐** Determine the formula of calcium chloride. (Calcium is in Group 2, chlorine is in Group 7.)
- [✔︎] CaCl₂ — Ca²⁺ needs two Cl⁻ ions to balance its charge
- [ ] CaCl — one calcium ion bonds with one chloride ion
    - *why wrong:* CaCl would give +2 + (−1) = +1 overall — not neutral. You need two Cl⁻ to balance one Ca²⁺.
- [ ] Ca₂Cl — two calcium ions bond with one chloride ion
    - *why wrong:* Ca₂Cl would give 2(+2) + (−1) = +3 — not neutral.
- [ ] CaCl₃ — calcium needs three chloride ions to become stable
    - *why wrong:* CaCl₃ would give +2 + 3(−1) = −1 — not neutral. Exactly two Cl⁻ balance one Ca²⁺.

**Q9. [reason · CFCHTFTH]** Explain, in terms of electron arrangement, why metals form positive ions but non-metals form negative ions.
- [✔︎] Metals have few outer electrons and lose them to empty their outer shell, leaving a positive ion; non-metals have nearly full shells and gain electrons, becoming negative
- [ ] Metals are heavier, so their nuclei pull electrons in and become positive
    - *why wrong:* Mass/heaviness does not set the charge — it is how many electrons are lost or gained to reach a full shell.
- [ ] Non-metals contain more protons, which makes them negative
    - *why wrong:* Proton number sets the element's identity, not the sign of the ion; gaining electrons is what makes non-metals negative.
- [ ] Metals gain electrons and non-metals lose them, to reach a full shell
    - *why wrong:* This is the wrong way round: metals LOSE electrons (become +), non-metals GAIN electrons (become −).

**Q10. [apply · CFCHTFTH]** Describe how a dot-and-cross diagram represents the formation of the ions in sodium chloride.
- [✔︎] Electrons from one atom are drawn as dots and from the other as crosses, showing the single outer electron moving from sodium to chlorine so each ion has a full outer shell
- [ ] It shows the sodium and chlorine sharing a pair of electrons drawn between them
    - *why wrong:* That describes a COVALENT dot-and-cross (shared pair). In NaCl the electron is transferred, not shared.
- [ ] It shows a sea of electrons moving freely around fixed positive ions
    - *why wrong:* That is the metallic bonding model, not a dot-and-cross diagram of ionic NaCl.
- [ ] It shows the chlorine atom giving one electron to the sodium atom
    - *why wrong:* The transfer is the other way: sodium (the metal) gives its electron to chlorine (the non-metal).

**Q11. [calc/derivation · CHTFTH] ⭐** Magnesium reacts with chlorine. Deduce the formula of the compound formed and justify it using the ion charges.
- [✔︎] MgCl₂ — Mg²⁺ has a 2+ charge, so it needs two Cl⁻ ions to balance it
- [ ] MgCl — one magnesium ion pairs with one chloride ion
    - *why wrong:* MgCl gives +2 + (−1) = +1 — not neutral. Two Cl⁻ are needed to balance Mg²⁺.
- [ ] Mg₂Cl — two magnesium ions pair with one chloride ion
    - *why wrong:* Mg₂Cl gives 2(+2) + (−1) = +3 — not neutral.
- [ ] MgCl₃ — magnesium needs three chloride ions
    - *why wrong:* MgCl₃ gives +2 + 3(−1) = −1 — not neutral; only two Cl⁻ are required.

**Q12. [calc/derivation · CHTFTH] ⭐** Potassium reacts with oxygen. Predict the formula of potassium oxide and justify your answer using ion charges. (K is Group 1, O is Group 6.)
- [✔︎] K₂O — each K⁺ carries 1+, so two are needed to balance one O²⁻
- [ ] KO — one potassium ion balances one oxygen ion
    - *why wrong:* KO gives +1 + (−2) = −1 — not neutral. Two K⁺ are needed to balance one O²⁻.
- [ ] KO₂ — one potassium ion needs two oxide ions
    - *why wrong:* KO₂ gives +1 + 2(−2) = −3 — not neutral.
- [ ] K₂O₃ — by analogy with aluminium oxide
    - *why wrong:* K forms 1+ (not 3+), so the aluminium-oxide pattern does not apply; K₂O is correct.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Sodium (2.8.1) reacts with chlorine (2.8.7) to form sodium chloride. Describe what happens to the electrons.
- [✔︎] Sodium loses its 1 outer electron to form Na⁺ (2.8); chlorine gains it to form Cl⁻ (2.8.8); the oppositely charged ions then attract
- [ ] Sodium and chlorine share one pair of electrons in a single covalent bond
    - *why wrong:* Sharing is covalent bonding. NaCl is a metal + non-metal, so electrons are TRANSFERRED, not shared.
- [ ] Both atoms lose their outer electrons into a shared pool
    - *why wrong:* Only the metal (sodium) loses electrons; the non-metal (chlorine) gains them.
- [ ] Chlorine loses one electron to sodium, so chlorine becomes positive
    - *why wrong:* Chlorine GAINS the electron (it needs 1 more for a full shell), so it becomes the NEGATIVE ion.

**Q2. [reason · CFCHTFTH]** Explain why an ionic compound such as sodium chloride has no overall electrical charge.
- [✔︎] The total positive charge on the metal ions exactly balances the total negative charge on the non-metal ions
- [ ] The electrons transferred are destroyed, leaving neutral atoms
    - *why wrong:* Electrons are transferred, not destroyed — charge is conserved. The compound is neutral because the ion charges balance.
- [ ] The ions are held so tightly that their charges disappear
    - *why wrong:* Charge does not 'disappear' — the ions keep their charges; the compound is neutral because they sum to zero.
- [ ] Only the outer shells carry charge, and these cancel when the shells are full
    - *why wrong:* A full shell is not uncharged. Neutrality comes from equal amounts of positive and negative charge.

**Q3. [calc/derivation · CFCHTFTH] ⭐** Determine the formula of calcium chloride. (Calcium is in Group 2, chlorine is in Group 7.)
- [✔︎] CaCl₂ — Ca²⁺ needs two Cl⁻ ions to balance its charge
- [ ] CaCl — one calcium ion bonds with one chloride ion
    - *why wrong:* CaCl would give +2 + (−1) = +1 overall — not neutral. You need two Cl⁻ to balance one Ca²⁺.
- [ ] Ca₂Cl — two calcium ions bond with one chloride ion
    - *why wrong:* Ca₂Cl would give 2(+2) + (−1) = +3 — not neutral.
- [ ] CaCl₃ — calcium needs three chloride ions to become stable
    - *why wrong:* CaCl₃ would give +2 + 3(−1) = −1 — not neutral. Exactly two Cl⁻ balance one Ca²⁺.

**Q4. [reason · CFCHTFTH]** Explain, in terms of electron arrangement, why metals form positive ions but non-metals form negative ions.
- [✔︎] Metals have few outer electrons and lose them to empty their outer shell, leaving a positive ion; non-metals have nearly full shells and gain electrons, becoming negative
- [ ] Metals are heavier, so their nuclei pull electrons in and become positive
    - *why wrong:* Mass/heaviness does not set the charge — it is how many electrons are lost or gained to reach a full shell.
- [ ] Non-metals contain more protons, which makes them negative
    - *why wrong:* Proton number sets the element's identity, not the sign of the ion; gaining electrons is what makes non-metals negative.
- [ ] Metals gain electrons and non-metals lose them, to reach a full shell
    - *why wrong:* This is the wrong way round: metals LOSE electrons (become +), non-metals GAIN electrons (become −).

**Q5. [apply · CFCHTFTH]** Describe how a dot-and-cross diagram represents the formation of the ions in sodium chloride.
- [✔︎] Electrons from one atom are drawn as dots and from the other as crosses, showing the single outer electron moving from sodium to chlorine so each ion has a full outer shell
- [ ] It shows the sodium and chlorine sharing a pair of electrons drawn between them
    - *why wrong:* That describes a COVALENT dot-and-cross (shared pair). In NaCl the electron is transferred, not shared.
- [ ] It shows a sea of electrons moving freely around fixed positive ions
    - *why wrong:* That is the metallic bonding model, not a dot-and-cross diagram of ionic NaCl.
- [ ] It shows the chlorine atom giving one electron to the sodium atom
    - *why wrong:* The transfer is the other way: sodium (the metal) gives its electron to chlorine (the non-metal).

**Q6. [calc/derivation · CHTFTH] ⭐** Magnesium reacts with chlorine. Deduce the formula of the compound formed and justify it using the ion charges.
- [✔︎] MgCl₂ — Mg²⁺ has a 2+ charge, so it needs two Cl⁻ ions to balance it
- [ ] MgCl — one magnesium ion pairs with one chloride ion
    - *why wrong:* MgCl gives +2 + (−1) = +1 — not neutral. Two Cl⁻ are needed to balance Mg²⁺.
- [ ] Mg₂Cl — two magnesium ions pair with one chloride ion
    - *why wrong:* Mg₂Cl gives 2(+2) + (−1) = +3 — not neutral.
- [ ] MgCl₃ — magnesium needs three chloride ions
    - *why wrong:* MgCl₃ gives +2 + 3(−1) = −1 — not neutral; only two Cl⁻ are required.

**Q7. [reason · CHTH]** A student writes: 'The ionic bond is the transfer of electrons from sodium to chlorine.' Explain why this statement is not correct.
- [✔︎] The transfer only creates the ions; the ionic bond is the electrostatic attraction between the oppositely charged ions that results
- [ ] It is correct — the ionic bond is the movement of the electron
    - *why wrong:* The transfer is a one-off event, not the ongoing bond — so the statement is not correct.
- [ ] The electrons are shared, not transferred, so the description is wrong
    - *why wrong:* Sodium chloride is ionic (metal + non-metal), so electrons are transferred, not shared.
- [ ] Sodium gains the electron, so the direction of transfer is wrong
    - *why wrong:* Sodium is the metal and LOSES the electron; chlorine gains it. The stated direction is right — the error is calling the transfer 'the bond'.

**Q8. [calc/derivation · CHTFTH] ⭐** Potassium reacts with oxygen. Predict the formula of potassium oxide and justify your answer using ion charges. (K is Group 1, O is Group 6.)
- [✔︎] K₂O — each K⁺ carries 1+, so two are needed to balance one O²⁻
- [ ] KO — one potassium ion balances one oxygen ion
    - *why wrong:* KO gives +1 + (−2) = −1 — not neutral. Two K⁺ are needed to balance one O²⁻.
- [ ] KO₂ — one potassium ion needs two oxide ions
    - *why wrong:* KO₂ gives +1 + 2(−2) = −3 — not neutral.
- [ ] K₂O₃ — by analogy with aluminium oxide
    - *why wrong:* K forms 1+ (not 3+), so the aluminium-oxide pattern does not apply; K₂O is correct.

**Q9. [reason · CHTH]** Explain why the noble gases in Group 0 do not normally form ions.
- [✔︎] Their outer shells are already full, so they have no tendency to lose or gain electrons
- [ ] They are gases, and gases cannot form ions
    - *why wrong:* State of matter does not decide this — many gases form ions when they react. Noble gases don't because their shells are full.
- [ ] Their atoms are too small to hold a charge
    - *why wrong:* Atom size does not prevent ion formation; a full outer shell removes the tendency to react.
- [ ] They already exist as negative ions in nature
    - *why wrong:* Noble gases are neutral atoms with full shells, not naturally occurring ions.

**Q10. [calc/derivation · CHTH] ⭐** Explain, in terms of electron transfer, why the formula of aluminium oxide is Al₂O₃.
- [✔︎] Al loses 3 electrons to form Al³⁺ and O gains 2 to form O²⁻; balancing the charges needs two Al³⁺ (6+) and three O²⁻ (6−)
- [ ] Aluminium and oxygen share three pairs of electrons
    - *why wrong:* Aluminium oxide is ionic (metal + non-metal) — electrons are transferred, not shared.
- [ ] Aluminium forms Al²⁺ and oxygen forms O³⁻, giving Al₃O₂
    - *why wrong:* Aluminium is Group 3 (forms Al³⁺) and oxygen is Group 6 (forms O²⁻); the charges are swapped here, which would give the wrong formula.
- [ ] The subscripts 2 and 3 come from the group numbers 2 and 3
    - *why wrong:* The subscripts come from balancing the CHARGES (3+ and 2− → lowest common multiple 6), not from the group numbers directly.

**Q11. [calc/derivation · TH] ⭐** A compound is made of ions X²⁺ and Y³⁻. Deduce its formula and explain how you worked it out.
- [✔︎] X₃Y₂ — three X²⁺ (total 6+) balance two Y³⁻ (total 6−), the lowest common multiple of the charges
- [ ] XY — one of each ion balances
    - *why wrong:* XY gives +2 + (−3) = −1 — not neutral. You must balance to a total of zero.
- [ ] X₂Y₃ — the charges become the subscripts of the other ion
    - *why wrong:* Swapping the charges to subscripts gives X₂Y₃, which is +4 with −9 = −5 — not neutral. Use the lowest common multiple of the charges (6): 3 × 2+ and 2 × 3−.
- [ ] X₃Y₂ is impossible because the charges are different sizes
    - *why wrong:* Ions of different charge size combine all the time (e.g. Al₂O₃); you just balance the totals.
  > 🚩 **Reviewer note:** Abstract 'X/Y' charge-balancing item — pure reasoning, AQA-standard HT style. Confirm difficulty is right for Triple Higher.

**Q12. [reason · TH]** Explain one limitation of using a dot-and-cross diagram to represent solid sodium chloride.
- [✔︎] It shows only a few ions, so it does not show that the solid is a giant 3D lattice of billions of alternating ions
- [ ] It uses the wrong number of electrons for each ion
    - *why wrong:* A correct dot-and-cross does use the right electron counts — that is not the limitation.
- [ ] It cannot show which atom the electrons came from
    - *why wrong:* Showing which atom each electron came from is exactly what dots and crosses DO; that is a strength, not a limitation.
- [ ] It wrongly suggests the bonding is covalent
    - *why wrong:* A dot-and-cross for NaCl correctly shows transfer (ions with charges), so it does not imply covalent bonding.
  > 🚩 **Reviewer note:** AQA HT 'limitations of models' skill. Confirm this is Triple/Higher-appropriate (not Foundation).


---

## Ionic Compounds  ·  `ionic-compounds`  ·  AQA 5.2.1.3

> 🚩 **Triple-depth call (your review):** MATCHED — AQA 5.2.1.3 (giant ionic lattice + properties) is identical for Combined and Triple. Foundation difficulty is the same across both pathways. The charge/melting-point comparison (⭐) is genuine HIGHER-tier depth (present in both Combined-H and Triple-H). No AQA Triple-only content on this page.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often say that because ionic compounds contain charged ions they should conduct electricity even when solid. They do not: in a solid the ions are locked in fixed positions in the lattice and cannot move. Only when the compound is melted or dissolved are the ions free to move — and it is moving charged particles that carry a current.

**Question sets by tier** (each item shows tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (3 recall / 7 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why solid sodium chloride does not conduct electricity, but molten sodium chloride does.
- [✔︎] In the solid the ions are held in fixed positions and cannot move; when molten the ions are free to move and carry charge
- [ ] Solid sodium chloride contains no ions — they only form when it melts
    - *why wrong:* NaCl is ionic in all states — the Na⁺ and Cl⁻ ions are present in the solid, they just cannot move.
- [ ] Solid sodium chloride is white, and colour prevents conduction
    - *why wrong:* Colour has no effect on electrical conductivity.
- [ ] Molten sodium chloride conducts using free electrons, not ions
    - *why wrong:* Ionic conduction is carried by IONS, not electrons; electron conduction happens in metals.

**Q2. [reason · CFCHTFTH]** Explain why ionic compounds have high melting points.
- [✔︎] Many strong electrostatic forces act between the oppositely charged ions throughout the giant lattice, so a lot of energy is needed to separate them
- [ ] The large size of the crystal means more energy is needed to melt it
    - *why wrong:* The physical size of a crystal does not set the melting point — the strength of the bonding does.
- [ ] Ionic compounds contain strong covalent bonds that must be broken
    - *why wrong:* Ionic compounds contain ionic bonds (electrostatic attraction between ions), not covalent bonds.
- [ ] The electrons in the compound are tightly held and resist heating
    - *why wrong:* Electrons are transferred to form the ions; they are not the reason for the high melting point.

**Q3. [apply · CFCHTFTH]** Describe the structure of a giant ionic lattice.
- [✔︎] A regular 3D arrangement of many oppositely charged ions, held by strong electrostatic forces acting in all directions
- [ ] A small group of a few ions joined into a single molecule
    - *why wrong:* An ionic compound is NOT made of small molecules — it is a giant lattice of billions of ions.
- [ ] A sea of delocalised electrons around fixed positive ions
    - *why wrong:* That is the metallic bonding model; ionic lattices have positive AND negative ions, no electron sea.
- [ ] Long chains of atoms joined by weak forces
    - *why wrong:* That describes polymers; ionic lattices are rigid 3D arrangements of ions, not chains.

**Q4. [reason · CFCHTFTH]** Ionic compounds are hard but brittle. Explain why they shatter when hit.
- [✔︎] A blow shifts the layers of ions so that like-charged ions line up next to each other; they repel strongly and the crystal splits
- [ ] The covalent bonds inside the crystal snap
    - *why wrong:* Ionic compounds have no covalent bonds — they are held by electrostatic attraction between ions.
- [ ] The delocalised electrons stop holding the ions together
    - *why wrong:* Ionic compounds contain no delocalised electrons — that is a metallic feature.
- [ ] The ions melt at the point of impact
    - *why wrong:* Shattering is a mechanical effect of ion repulsion, not melting.

**Q5. [reason · CFCHTFTH]** Explain why many ionic compounds dissolve in water and the solution then conducts electricity.
- [✔︎] Water molecules pull the ions away from the lattice; the freed ions can move through the solution and carry charge
- [ ] The water breaks the ions down into neutral atoms that carry current
    - *why wrong:* The ions keep their charges when they dissolve — they are not turned into neutral atoms.
- [ ] The water adds electrons that carry the current
    - *why wrong:* Conduction in the solution is by the moving IONS, not by added electrons.
- [ ] Dissolving turns the compound into a metal
    - *why wrong:* Dissolving separates the existing ions; it does not create metallic bonding.

**Q6. [recall · CFTF]** State the type of structure that ionic compounds form.
- [✔︎] A giant ionic lattice
- [ ] Small separate molecules
    - *why wrong:* Ionic compounds are not made of discrete molecules; they form a giant repeating lattice.
- [ ] A metallic lattice
    - *why wrong:* A metallic lattice has positive ions and delocalised electrons, not a mix of positive and negative ions.
- [ ] Long polymer chains
    - *why wrong:* Polymer chains are a covalent, molecular arrangement, not ionic.

**Q7. [recall · CFTF]** State the two conditions under which an ionic compound will conduct electricity.
- [✔︎] When it is molten or when it is dissolved in water
- [ ] When it is solid or when it is molten
    - *why wrong:* A solid ionic compound does NOT conduct — its ions are fixed.
- [ ] When it is solid or when it is dissolved
    - *why wrong:* The solid does not conduct; only the dissolved (and molten) states do.
- [ ] Only when it is solid
    - *why wrong:* The solid never conducts, because the ions cannot move.

**Q8. [recall · CFTF]** State whether ionic compounds have high or low melting points.
- [✔︎] High
- [ ] Low
    - *why wrong:* Ionic compounds have HIGH melting points because of the strong forces throughout the lattice.
- [ ] Always exactly 0°C
    - *why wrong:* 0°C is the melting point of ice, not a general rule for ionic compounds.
- [ ] They do not melt at all
    - *why wrong:* Ionic compounds do melt — but only at high temperatures.

**Q9. [apply · CFTF]** Describe how the ions are arranged in solid sodium chloride.
- [✔︎] Positive and negative ions alternate in a regular, repeating 3D pattern
- [ ] The ions are randomly scattered with large gaps between them
    - *why wrong:* The lattice is regular and ordered, not random.
- [ ] All the positive ions are on one side and all the negative ions on the other
    - *why wrong:* Ions alternate so that each is surrounded by oppositely charged ions — they are not separated by charge.
- [ ] The ions are joined in pairs that float freely
    - *why wrong:* The ions are fixed in a giant lattice, not floating pairs.

**Q10. [apply · CFTF]** Predict whether solid potassium bromide will conduct electricity, and give a reason.
- [✔︎] No — its ions are fixed in the lattice and cannot move
- [ ] Yes — it contains ions, which always conduct
    - *why wrong:* Containing ions is not enough — they must be FREE TO MOVE, and in a solid they are fixed.
- [ ] Yes — its delocalised electrons carry the current
    - *why wrong:* Ionic compounds have no delocalised electrons; that is a metallic feature.
- [ ] No — potassium bromide contains no charged particles
    - *why wrong:* It does contain charged particles (K⁺ and Br⁻ ions); the reason it does not conduct is that they cannot move.

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why solid sodium chloride does not conduct electricity, but molten sodium chloride does.
- [✔︎] In the solid the ions are held in fixed positions and cannot move; when molten the ions are free to move and carry charge
- [ ] Solid sodium chloride contains no ions — they only form when it melts
    - *why wrong:* NaCl is ionic in all states — the Na⁺ and Cl⁻ ions are present in the solid, they just cannot move.
- [ ] Solid sodium chloride is white, and colour prevents conduction
    - *why wrong:* Colour has no effect on electrical conductivity.
- [ ] Molten sodium chloride conducts using free electrons, not ions
    - *why wrong:* Ionic conduction is carried by IONS, not electrons; electron conduction happens in metals.

**Q2. [reason · CFCHTFTH]** Explain why ionic compounds have high melting points.
- [✔︎] Many strong electrostatic forces act between the oppositely charged ions throughout the giant lattice, so a lot of energy is needed to separate them
- [ ] The large size of the crystal means more energy is needed to melt it
    - *why wrong:* The physical size of a crystal does not set the melting point — the strength of the bonding does.
- [ ] Ionic compounds contain strong covalent bonds that must be broken
    - *why wrong:* Ionic compounds contain ionic bonds (electrostatic attraction between ions), not covalent bonds.
- [ ] The electrons in the compound are tightly held and resist heating
    - *why wrong:* Electrons are transferred to form the ions; they are not the reason for the high melting point.

**Q3. [apply · CFCHTFTH]** Describe the structure of a giant ionic lattice.
- [✔︎] A regular 3D arrangement of many oppositely charged ions, held by strong electrostatic forces acting in all directions
- [ ] A small group of a few ions joined into a single molecule
    - *why wrong:* An ionic compound is NOT made of small molecules — it is a giant lattice of billions of ions.
- [ ] A sea of delocalised electrons around fixed positive ions
    - *why wrong:* That is the metallic bonding model; ionic lattices have positive AND negative ions, no electron sea.
- [ ] Long chains of atoms joined by weak forces
    - *why wrong:* That describes polymers; ionic lattices are rigid 3D arrangements of ions, not chains.

**Q4. [reason · CFCHTFTH]** Ionic compounds are hard but brittle. Explain why they shatter when hit.
- [✔︎] A blow shifts the layers of ions so that like-charged ions line up next to each other; they repel strongly and the crystal splits
- [ ] The covalent bonds inside the crystal snap
    - *why wrong:* Ionic compounds have no covalent bonds — they are held by electrostatic attraction between ions.
- [ ] The delocalised electrons stop holding the ions together
    - *why wrong:* Ionic compounds contain no delocalised electrons — that is a metallic feature.
- [ ] The ions melt at the point of impact
    - *why wrong:* Shattering is a mechanical effect of ion repulsion, not melting.

**Q5. [reason · CFCHTFTH]** Explain why many ionic compounds dissolve in water and the solution then conducts electricity.
- [✔︎] Water molecules pull the ions away from the lattice; the freed ions can move through the solution and carry charge
- [ ] The water breaks the ions down into neutral atoms that carry current
    - *why wrong:* The ions keep their charges when they dissolve — they are not turned into neutral atoms.
- [ ] The water adds electrons that carry the current
    - *why wrong:* Conduction in the solution is by the moving IONS, not by added electrons.
- [ ] Dissolving turns the compound into a metal
    - *why wrong:* Dissolving separates the existing ions; it does not create metallic bonding.

**Q6. [reason · CHTH] ⭐** Magnesium oxide has a much higher melting point than sodium chloride. Explain why.
- [✔︎] Mg²⁺ and O²⁻ carry 2+/2− charges, larger than the 1+/1− of Na⁺ and Cl⁻, so the electrostatic forces between the ions are stronger and need more energy to break
- [ ] Magnesium oxide has a bigger crystal, so more bonds must be broken
    - *why wrong:* Crystal size is not the factor — both are giant lattices; the strength of each ion-ion attraction is what matters.
- [ ] Magnesium oxide contains more ions per formula unit than sodium chloride
    - *why wrong:* Both MgO and NaCl have a 1:1 ratio of ions — neither has more ions per formula unit.
- [ ] Magnesium is a heavier element than sodium, which raises the melting point
    - *why wrong:* Atomic mass does not set the melting point; the ionic CHARGE does.
  > 🚩 **Reviewer note:** Higher charge → stronger force → higher melting point. Core HT comparative reasoning — please full-review.

**Q7. [reason · CHTH]** Explain, in terms of structure and bonding, why ionic compounds are hard and brittle whereas metals are malleable.
- [✔︎] In an ionic solid, shifting the layers brings like charges together and they repel, so it shatters; in a metal the layers of ions slide and the electron sea keeps them bonded, so it bends
- [ ] Ionic compounds contain delocalised electrons that snap; metals do not
    - *why wrong:* Ionic compounds contain no delocalised electrons; that is a metallic feature.
- [ ] Ionic bonds are weak and metallic bonds are strong
    - *why wrong:* Both bonds are strong — the difference is what happens to the structure when layers move.
- [ ] Metals are molecular and ionic compounds are giant
    - *why wrong:* Both are giant structures; the difference is the electron sea in metals versus fixed ions in ionic solids.

**Q8. [reason · CHTH]** A white solid melts at about 800°C and conducts electricity when molten but not when solid. Deduce its structure and bonding, and justify your answer using its properties.
- [✔︎] A giant ionic lattice with ionic bonding — the high melting point shows strong forces, and it conducts only when the ions become free to move on melting
- [ ] A simple molecular substance — the low forces let it melt and conduct
    - *why wrong:* Simple molecular substances have LOW melting points and never conduct — this melts at 800°C and does conduct when molten.
- [ ] A metallic structure — it conducts because of delocalised electrons
    - *why wrong:* A metal would conduct as a SOLID too; this one does not.
- [ ] A giant covalent structure — it conducts when the covalent bonds melt
    - *why wrong:* Giant covalent substances do not conduct when molten (graphite excepted), and their bonds do not 'melt' into charge carriers.

**Q9. [reason · CHTH]** Explain why ionic compounds do not conduct electricity in the solid state, even though they are made of charged ions.
- [✔︎] The ions are held in fixed positions in the lattice, so although they are charged they cannot move to carry a current
- [ ] The charges on the ions cancel out completely in the solid
    - *why wrong:* The charges do not cancel — the ions keep them; conduction fails only because the ions cannot move.
- [ ] Solids can never conduct electricity
    - *why wrong:* Many solids conduct (metals, graphite); the issue here is that the ions are fixed.
- [ ] The ions turn into neutral atoms when the compound is solid
    - *why wrong:* The ions stay as ions in the solid; they do not become neutral atoms.

**Q10. [reason · CHTH]** Suggest why not all ionic compounds are soluble in water.
- [✔︎] In some compounds the electrostatic forces between the ions are too strong for the water molecules to pull them out of the lattice
- [ ] Insoluble ionic compounds contain no ions
    - *why wrong:* All ionic compounds contain ions; solubility depends on how the ion-ion forces compare with the ion-water attractions.
- [ ] Water can only dissolve metals
    - *why wrong:* Water dissolves many ionic compounds (non-metal-containing), not just metals.
- [ ] Insoluble compounds have covalent bonds instead of ionic bonds
    - *why wrong:* Insoluble ionic compounds are still ionic — the difference is the strength of their lattice forces.

### Triple Foundation — 12 questions (3 recall / 9 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why solid sodium chloride does not conduct electricity, but molten sodium chloride does.
- [✔︎] In the solid the ions are held in fixed positions and cannot move; when molten the ions are free to move and carry charge
- [ ] Solid sodium chloride contains no ions — they only form when it melts
    - *why wrong:* NaCl is ionic in all states — the Na⁺ and Cl⁻ ions are present in the solid, they just cannot move.
- [ ] Solid sodium chloride is white, and colour prevents conduction
    - *why wrong:* Colour has no effect on electrical conductivity.
- [ ] Molten sodium chloride conducts using free electrons, not ions
    - *why wrong:* Ionic conduction is carried by IONS, not electrons; electron conduction happens in metals.

**Q2. [reason · CFCHTFTH]** Explain why ionic compounds have high melting points.
- [✔︎] Many strong electrostatic forces act between the oppositely charged ions throughout the giant lattice, so a lot of energy is needed to separate them
- [ ] The large size of the crystal means more energy is needed to melt it
    - *why wrong:* The physical size of a crystal does not set the melting point — the strength of the bonding does.
- [ ] Ionic compounds contain strong covalent bonds that must be broken
    - *why wrong:* Ionic compounds contain ionic bonds (electrostatic attraction between ions), not covalent bonds.
- [ ] The electrons in the compound are tightly held and resist heating
    - *why wrong:* Electrons are transferred to form the ions; they are not the reason for the high melting point.

**Q3. [apply · CFCHTFTH]** Describe the structure of a giant ionic lattice.
- [✔︎] A regular 3D arrangement of many oppositely charged ions, held by strong electrostatic forces acting in all directions
- [ ] A small group of a few ions joined into a single molecule
    - *why wrong:* An ionic compound is NOT made of small molecules — it is a giant lattice of billions of ions.
- [ ] A sea of delocalised electrons around fixed positive ions
    - *why wrong:* That is the metallic bonding model; ionic lattices have positive AND negative ions, no electron sea.
- [ ] Long chains of atoms joined by weak forces
    - *why wrong:* That describes polymers; ionic lattices are rigid 3D arrangements of ions, not chains.

**Q4. [reason · CFCHTFTH]** Ionic compounds are hard but brittle. Explain why they shatter when hit.
- [✔︎] A blow shifts the layers of ions so that like-charged ions line up next to each other; they repel strongly and the crystal splits
- [ ] The covalent bonds inside the crystal snap
    - *why wrong:* Ionic compounds have no covalent bonds — they are held by electrostatic attraction between ions.
- [ ] The delocalised electrons stop holding the ions together
    - *why wrong:* Ionic compounds contain no delocalised electrons — that is a metallic feature.
- [ ] The ions melt at the point of impact
    - *why wrong:* Shattering is a mechanical effect of ion repulsion, not melting.

**Q5. [reason · CFCHTFTH]** Explain why many ionic compounds dissolve in water and the solution then conducts electricity.
- [✔︎] Water molecules pull the ions away from the lattice; the freed ions can move through the solution and carry charge
- [ ] The water breaks the ions down into neutral atoms that carry current
    - *why wrong:* The ions keep their charges when they dissolve — they are not turned into neutral atoms.
- [ ] The water adds electrons that carry the current
    - *why wrong:* Conduction in the solution is by the moving IONS, not by added electrons.
- [ ] Dissolving turns the compound into a metal
    - *why wrong:* Dissolving separates the existing ions; it does not create metallic bonding.

**Q6. [recall · CFTF]** State the type of structure that ionic compounds form.
- [✔︎] A giant ionic lattice
- [ ] Small separate molecules
    - *why wrong:* Ionic compounds are not made of discrete molecules; they form a giant repeating lattice.
- [ ] A metallic lattice
    - *why wrong:* A metallic lattice has positive ions and delocalised electrons, not a mix of positive and negative ions.
- [ ] Long polymer chains
    - *why wrong:* Polymer chains are a covalent, molecular arrangement, not ionic.

**Q7. [recall · CFTF]** State the two conditions under which an ionic compound will conduct electricity.
- [✔︎] When it is molten or when it is dissolved in water
- [ ] When it is solid or when it is molten
    - *why wrong:* A solid ionic compound does NOT conduct — its ions are fixed.
- [ ] When it is solid or when it is dissolved
    - *why wrong:* The solid does not conduct; only the dissolved (and molten) states do.
- [ ] Only when it is solid
    - *why wrong:* The solid never conducts, because the ions cannot move.

**Q8. [recall · CFTF]** State whether ionic compounds have high or low melting points.
- [✔︎] High
- [ ] Low
    - *why wrong:* Ionic compounds have HIGH melting points because of the strong forces throughout the lattice.
- [ ] Always exactly 0°C
    - *why wrong:* 0°C is the melting point of ice, not a general rule for ionic compounds.
- [ ] They do not melt at all
    - *why wrong:* Ionic compounds do melt — but only at high temperatures.

**Q9. [apply · CFTF]** Describe how the ions are arranged in solid sodium chloride.
- [✔︎] Positive and negative ions alternate in a regular, repeating 3D pattern
- [ ] The ions are randomly scattered with large gaps between them
    - *why wrong:* The lattice is regular and ordered, not random.
- [ ] All the positive ions are on one side and all the negative ions on the other
    - *why wrong:* Ions alternate so that each is surrounded by oppositely charged ions — they are not separated by charge.
- [ ] The ions are joined in pairs that float freely
    - *why wrong:* The ions are fixed in a giant lattice, not floating pairs.

**Q10. [apply · CFTF]** Predict whether solid potassium bromide will conduct electricity, and give a reason.
- [✔︎] No — its ions are fixed in the lattice and cannot move
- [ ] Yes — it contains ions, which always conduct
    - *why wrong:* Containing ions is not enough — they must be FREE TO MOVE, and in a solid they are fixed.
- [ ] Yes — its delocalised electrons carry the current
    - *why wrong:* Ionic compounds have no delocalised electrons; that is a metallic feature.
- [ ] No — potassium bromide contains no charged particles
    - *why wrong:* It does contain charged particles (K⁺ and Br⁻ ions); the reason it does not conduct is that they cannot move.

**Q11. [apply · TF]** Describe what happens to the ions of an ionic compound when it dissolves in water.
- [✔︎] They separate from the lattice and become surrounded by water molecules, free to move through the solution
- [ ] They join together into neutral molecules
    - *why wrong:* Dissolving separates the ions rather than joining them into molecules.
- [ ] They lose their charges and become atoms
    - *why wrong:* The ions keep their charges when they dissolve.
- [ ] They stay locked together as a solid inside the water
    - *why wrong:* If the ions stayed locked together the compound would not have dissolved.

**Q12. [apply · TF]** Identify the property of an ionic compound that is caused by the strong electrostatic forces in its lattice.
- [✔︎] A high melting point
- [ ] Conducting electricity when solid
    - *why wrong:* Conducting when solid is not a property of ionic compounds at all — the ions are fixed.
- [ ] A low density
    - *why wrong:* Density is not determined by the strength of the lattice forces.
- [ ] Being soft and easily scratched
    - *why wrong:* Ionic compounds are hard, not soft; the strong forces make them difficult to scratch.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why solid sodium chloride does not conduct electricity, but molten sodium chloride does.
- [✔︎] In the solid the ions are held in fixed positions and cannot move; when molten the ions are free to move and carry charge
- [ ] Solid sodium chloride contains no ions — they only form when it melts
    - *why wrong:* NaCl is ionic in all states — the Na⁺ and Cl⁻ ions are present in the solid, they just cannot move.
- [ ] Solid sodium chloride is white, and colour prevents conduction
    - *why wrong:* Colour has no effect on electrical conductivity.
- [ ] Molten sodium chloride conducts using free electrons, not ions
    - *why wrong:* Ionic conduction is carried by IONS, not electrons; electron conduction happens in metals.

**Q2. [reason · CFCHTFTH]** Explain why ionic compounds have high melting points.
- [✔︎] Many strong electrostatic forces act between the oppositely charged ions throughout the giant lattice, so a lot of energy is needed to separate them
- [ ] The large size of the crystal means more energy is needed to melt it
    - *why wrong:* The physical size of a crystal does not set the melting point — the strength of the bonding does.
- [ ] Ionic compounds contain strong covalent bonds that must be broken
    - *why wrong:* Ionic compounds contain ionic bonds (electrostatic attraction between ions), not covalent bonds.
- [ ] The electrons in the compound are tightly held and resist heating
    - *why wrong:* Electrons are transferred to form the ions; they are not the reason for the high melting point.

**Q3. [apply · CFCHTFTH]** Describe the structure of a giant ionic lattice.
- [✔︎] A regular 3D arrangement of many oppositely charged ions, held by strong electrostatic forces acting in all directions
- [ ] A small group of a few ions joined into a single molecule
    - *why wrong:* An ionic compound is NOT made of small molecules — it is a giant lattice of billions of ions.
- [ ] A sea of delocalised electrons around fixed positive ions
    - *why wrong:* That is the metallic bonding model; ionic lattices have positive AND negative ions, no electron sea.
- [ ] Long chains of atoms joined by weak forces
    - *why wrong:* That describes polymers; ionic lattices are rigid 3D arrangements of ions, not chains.

**Q4. [reason · CFCHTFTH]** Ionic compounds are hard but brittle. Explain why they shatter when hit.
- [✔︎] A blow shifts the layers of ions so that like-charged ions line up next to each other; they repel strongly and the crystal splits
- [ ] The covalent bonds inside the crystal snap
    - *why wrong:* Ionic compounds have no covalent bonds — they are held by electrostatic attraction between ions.
- [ ] The delocalised electrons stop holding the ions together
    - *why wrong:* Ionic compounds contain no delocalised electrons — that is a metallic feature.
- [ ] The ions melt at the point of impact
    - *why wrong:* Shattering is a mechanical effect of ion repulsion, not melting.

**Q5. [reason · CFCHTFTH]** Explain why many ionic compounds dissolve in water and the solution then conducts electricity.
- [✔︎] Water molecules pull the ions away from the lattice; the freed ions can move through the solution and carry charge
- [ ] The water breaks the ions down into neutral atoms that carry current
    - *why wrong:* The ions keep their charges when they dissolve — they are not turned into neutral atoms.
- [ ] The water adds electrons that carry the current
    - *why wrong:* Conduction in the solution is by the moving IONS, not by added electrons.
- [ ] Dissolving turns the compound into a metal
    - *why wrong:* Dissolving separates the existing ions; it does not create metallic bonding.

**Q6. [reason · CHTH] ⭐** Magnesium oxide has a much higher melting point than sodium chloride. Explain why.
- [✔︎] Mg²⁺ and O²⁻ carry 2+/2− charges, larger than the 1+/1− of Na⁺ and Cl⁻, so the electrostatic forces between the ions are stronger and need more energy to break
- [ ] Magnesium oxide has a bigger crystal, so more bonds must be broken
    - *why wrong:* Crystal size is not the factor — both are giant lattices; the strength of each ion-ion attraction is what matters.
- [ ] Magnesium oxide contains more ions per formula unit than sodium chloride
    - *why wrong:* Both MgO and NaCl have a 1:1 ratio of ions — neither has more ions per formula unit.
- [ ] Magnesium is a heavier element than sodium, which raises the melting point
    - *why wrong:* Atomic mass does not set the melting point; the ionic CHARGE does.
  > 🚩 **Reviewer note:** Higher charge → stronger force → higher melting point. Core HT comparative reasoning — please full-review.

**Q7. [reason · CHTH]** Explain, in terms of structure and bonding, why ionic compounds are hard and brittle whereas metals are malleable.
- [✔︎] In an ionic solid, shifting the layers brings like charges together and they repel, so it shatters; in a metal the layers of ions slide and the electron sea keeps them bonded, so it bends
- [ ] Ionic compounds contain delocalised electrons that snap; metals do not
    - *why wrong:* Ionic compounds contain no delocalised electrons; that is a metallic feature.
- [ ] Ionic bonds are weak and metallic bonds are strong
    - *why wrong:* Both bonds are strong — the difference is what happens to the structure when layers move.
- [ ] Metals are molecular and ionic compounds are giant
    - *why wrong:* Both are giant structures; the difference is the electron sea in metals versus fixed ions in ionic solids.

**Q8. [reason · CHTH]** A white solid melts at about 800°C and conducts electricity when molten but not when solid. Deduce its structure and bonding, and justify your answer using its properties.
- [✔︎] A giant ionic lattice with ionic bonding — the high melting point shows strong forces, and it conducts only when the ions become free to move on melting
- [ ] A simple molecular substance — the low forces let it melt and conduct
    - *why wrong:* Simple molecular substances have LOW melting points and never conduct — this melts at 800°C and does conduct when molten.
- [ ] A metallic structure — it conducts because of delocalised electrons
    - *why wrong:* A metal would conduct as a SOLID too; this one does not.
- [ ] A giant covalent structure — it conducts when the covalent bonds melt
    - *why wrong:* Giant covalent substances do not conduct when molten (graphite excepted), and their bonds do not 'melt' into charge carriers.

**Q9. [reason · CHTH]** Explain why ionic compounds do not conduct electricity in the solid state, even though they are made of charged ions.
- [✔︎] The ions are held in fixed positions in the lattice, so although they are charged they cannot move to carry a current
- [ ] The charges on the ions cancel out completely in the solid
    - *why wrong:* The charges do not cancel — the ions keep them; conduction fails only because the ions cannot move.
- [ ] Solids can never conduct electricity
    - *why wrong:* Many solids conduct (metals, graphite); the issue here is that the ions are fixed.
- [ ] The ions turn into neutral atoms when the compound is solid
    - *why wrong:* The ions stay as ions in the solid; they do not become neutral atoms.

**Q10. [reason · CHTH]** Suggest why not all ionic compounds are soluble in water.
- [✔︎] In some compounds the electrostatic forces between the ions are too strong for the water molecules to pull them out of the lattice
- [ ] Insoluble ionic compounds contain no ions
    - *why wrong:* All ionic compounds contain ions; solubility depends on how the ion-ion forces compare with the ion-water attractions.
- [ ] Water can only dissolve metals
    - *why wrong:* Water dissolves many ionic compounds (non-metal-containing), not just metals.
- [ ] Insoluble compounds have covalent bonds instead of ionic bonds
    - *why wrong:* Insoluble ionic compounds are still ionic — the difference is the strength of their lattice forces.

**Q11. [reason · TH]** Explain why the formula NaCl represents the simplest ratio of ions rather than a molecule made of one sodium atom and one chlorine atom.
- [✔︎] Sodium chloride is a giant lattice of billions of ions; the formula gives the 1:1 ratio of Na⁺ to Cl⁻, not a discrete two-atom molecule
- [ ] There really is only one sodium and one chlorine atom in a crystal of salt
    - *why wrong:* A grain of salt contains billions of ions, not a single pair of atoms.
- [ ] NaCl exists as separate NaCl molecules floating in the solid
    - *why wrong:* There are no discrete NaCl molecules — it is a continuous giant lattice.
- [ ] The formula shows that sodium and chlorine share electrons in a molecule
    - *why wrong:* NaCl is ionic (electrons transferred), not a molecule with shared electrons.

**Q12. [reason · TH] ⭐** Predict, with reasons, whether calcium oxide (CaO) or potassium chloride (KCl) has the higher melting point.
- [✔︎] CaO — its ions carry 2+ and 2− charges, so the electrostatic forces are stronger than in KCl (1+/1−) and more energy is needed to melt it
- [ ] KCl — potassium is a larger atom, which always raises the melting point
    - *why wrong:* Atom size has a smaller effect than ionic charge; the 2+/2− charges in CaO give much stronger forces.
- [ ] They are equal, because both are ionic compounds
    - *why wrong:* Being ionic does not make melting points equal — the ionic charges (and sizes) differ.
- [ ] KCl — it has more ions in its formula
    - *why wrong:* Both have a 1:1 ratio, so KCl does not have more ions per formula unit.
  > 🚩 **Reviewer note:** Comparative charge → lattice-strength reasoning at Triple Higher. Please full-review.


---

## Covalent Bonding  ·  `covalent-bonding`  ·  AQA 5.2.1.4

> 🚩 **Triple-depth call (your review):** MATCHED — AQA 5.2.1.4 (covalent bonds, dot-and-cross) is identical for Combined and Triple. Foundation difficulty is the same across both pathways. NB the page's existing `higher` box mentions bond polarity / electronegativity, which is beyond AQA GCSE — I have NOT written questions on it and left that box untouched (per brief); flagging it for your call.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often say that covalent bonds must be weak because substances like water have low boiling points. The covalent bonds themselves are actually very strong. The low melting and boiling points come from the weak intermolecular forces BETWEEN whole molecules — when the substance melts, those weak forces are overcome, not the strong covalent bonds inside each molecule.

**Question sets by tier** (each item shows tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (5 recall / 5 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Carbon (Group 4) bonds with hydrogen to form methane, CH₄. Determine how many covalent bonds a carbon atom forms.
- [✔︎] 4 — carbon has 4 outer electrons and needs 4 more, so it forms 4 shared pairs
- [ ] 1 — carbon forms only one bond at a time
    - *why wrong:* Carbon forms one bond per shared pair, and it needs 4 shared pairs — not a single bond.
- [ ] 2 — carbon forms 2 bonds like oxygen
    - *why wrong:* Oxygen (Group 6) needs 2 more electrons so forms 2 bonds; carbon (Group 4) needs 4.
- [ ] 8 — carbon needs 8 electrons in total
    - *why wrong:* Carbon needs 8 electrons in its outer shell, but each BOND provides 2 shared electrons, so 4 bonds give the 8.

**Q2. [reason · CFCHTFTH]** Explain why oxygen exists as O₂ molecules rather than as single O atoms.
- [✔︎] Each oxygen atom has 6 outer electrons and needs 2 more; by sharing two pairs with another O atom, both reach a full outer shell of 8
- [ ] Two oxygen atoms join to make a more stable element in the periodic table
    - *why wrong:* Bonding does not change an element's position in the periodic table; O₂ forms because of electron sharing.
- [ ] Oxygen atoms repel each other and pair up to cancel the repulsion
    - *why wrong:* Atoms of the same element do repel slightly, but covalent bonding (sharing) creates a stronger overall attraction.
- [ ] Oxygen forms O₂ so that it can be a gas at room temperature
    - *why wrong:* Whether a substance is a gas depends on intermolecular forces, not on why the molecule forms.

**Q3. [recall · CFCHTFTH]** Describe what is meant by a covalent bond.
- [✔︎] A shared pair of electrons between two non-metal atoms, attracted to both nuclei
- [ ] The transfer of electrons from a metal to a non-metal
    - *why wrong:* Transferring electrons is ionic bonding, which occurs between a metal and a non-metal.
- [ ] A sea of delocalised electrons shared between metal ions
    - *why wrong:* A delocalised electron sea is the metallic bonding model.
- [ ] A weak attraction between two separate molecules
    - *why wrong:* That describes an intermolecular force, which acts BETWEEN molecules, not the bond within one.

**Q4. [apply · CFCHTFTH]** State the number of single covalent bonds present in a water molecule, H₂O.
- [✔︎] 2
- [ ] 1
    - *why wrong:* Oxygen forms 1 bond with each of the 2 hydrogen atoms, giving 2 bonds — not 1.
- [ ] 3
    - *why wrong:* Water has only 2 hydrogen atoms, so only 2 O–H bonds form.
- [ ] 4
    - *why wrong:* That would need 4 hydrogen atoms; water has 2.

**Q5. [reason · CFCHTFTH]** Explain why a chlorine molecule (Cl₂) contains a single covalent bond.
- [✔︎] Each chlorine atom has 7 outer electrons and needs 1 more, so the two atoms share one pair, giving both a full shell of 8
- [ ] Each chlorine atom shares three pairs of electrons
    - *why wrong:* Sharing three pairs would be a triple bond; chlorine needs only 1 more electron, so it shares one pair.
- [ ] One chlorine atom transfers an electron to the other
    - *why wrong:* Transferring an electron is ionic bonding; two identical non-metal atoms share instead.
- [ ] The two atoms are held together by a sea of delocalised electrons
    - *why wrong:* A delocalised electron sea is metallic bonding; Cl₂ is a simple covalent molecule.

**Q6. [recall · CFTF]** State the type of elements that form covalent bonds.
- [✔︎] Non-metals only
- [ ] Metals only
    - *why wrong:* A metal only would give metallic bonding.
- [ ] A metal and a non-metal
    - *why wrong:* A metal with a non-metal gives ionic bonding (transfer), not covalent.
- [ ] Noble gases only
    - *why wrong:* Noble gases rarely bond at all, as their outer shells are already full.

**Q7. [recall · CFTF]** State what is shared between atoms in a covalent bond.
- [✔︎] A pair of electrons
- [ ] A proton
    - *why wrong:* Protons stay in the nucleus and are not shared in bonding.
- [ ] A neutron
    - *why wrong:* Neutrons stay in the nucleus and are not involved in bonding.
- [ ] A whole atom
    - *why wrong:* Atoms are not shared — only a pair of outer electrons is.

**Q8. [recall · CFTF]** Name the type of covalent bond formed when two pairs of electrons are shared between two atoms.
- [✔︎] A double bond
- [ ] A single bond
    - *why wrong:* A single bond shares only one pair of electrons.
- [ ] A triple bond
    - *why wrong:* A triple bond shares three pairs, not two.
- [ ] An ionic bond
    - *why wrong:* An ionic bond involves transfer, not shared pairs.

**Q9. [apply · CFTF]** Identify which substance contains covalent bonds.
- [✔︎] Carbon dioxide
- [ ] Sodium chloride
    - *why wrong:* Sodium chloride is a metal + non-metal — ionic bonding.
- [ ] Magnesium oxide
    - *why wrong:* Magnesium oxide is a metal + non-metal — ionic bonding.
- [ ] Copper
    - *why wrong:* Copper is a pure metal — metallic bonding.

**Q10. [recall · CFTF]** State how many shared pairs of electrons there are in a triple bond.
- [✔︎] 3
- [ ] 1
    - *why wrong:* One shared pair is a single bond.
- [ ] 2
    - *why wrong:* Two shared pairs is a double bond.
- [ ] 6
    - *why wrong:* A triple bond has 3 shared pairs (which is 6 electrons, but only 3 pairs).

### Combined Higher — 10 questions (1 recall / 9 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Carbon (Group 4) bonds with hydrogen to form methane, CH₄. Determine how many covalent bonds a carbon atom forms.
- [✔︎] 4 — carbon has 4 outer electrons and needs 4 more, so it forms 4 shared pairs
- [ ] 1 — carbon forms only one bond at a time
    - *why wrong:* Carbon forms one bond per shared pair, and it needs 4 shared pairs — not a single bond.
- [ ] 2 — carbon forms 2 bonds like oxygen
    - *why wrong:* Oxygen (Group 6) needs 2 more electrons so forms 2 bonds; carbon (Group 4) needs 4.
- [ ] 8 — carbon needs 8 electrons in total
    - *why wrong:* Carbon needs 8 electrons in its outer shell, but each BOND provides 2 shared electrons, so 4 bonds give the 8.

**Q2. [reason · CFCHTFTH]** Explain why oxygen exists as O₂ molecules rather than as single O atoms.
- [✔︎] Each oxygen atom has 6 outer electrons and needs 2 more; by sharing two pairs with another O atom, both reach a full outer shell of 8
- [ ] Two oxygen atoms join to make a more stable element in the periodic table
    - *why wrong:* Bonding does not change an element's position in the periodic table; O₂ forms because of electron sharing.
- [ ] Oxygen atoms repel each other and pair up to cancel the repulsion
    - *why wrong:* Atoms of the same element do repel slightly, but covalent bonding (sharing) creates a stronger overall attraction.
- [ ] Oxygen forms O₂ so that it can be a gas at room temperature
    - *why wrong:* Whether a substance is a gas depends on intermolecular forces, not on why the molecule forms.

**Q3. [recall · CFCHTFTH]** Describe what is meant by a covalent bond.
- [✔︎] A shared pair of electrons between two non-metal atoms, attracted to both nuclei
- [ ] The transfer of electrons from a metal to a non-metal
    - *why wrong:* Transferring electrons is ionic bonding, which occurs between a metal and a non-metal.
- [ ] A sea of delocalised electrons shared between metal ions
    - *why wrong:* A delocalised electron sea is the metallic bonding model.
- [ ] A weak attraction between two separate molecules
    - *why wrong:* That describes an intermolecular force, which acts BETWEEN molecules, not the bond within one.

**Q4. [apply · CFCHTFTH]** State the number of single covalent bonds present in a water molecule, H₂O.
- [✔︎] 2
- [ ] 1
    - *why wrong:* Oxygen forms 1 bond with each of the 2 hydrogen atoms, giving 2 bonds — not 1.
- [ ] 3
    - *why wrong:* Water has only 2 hydrogen atoms, so only 2 O–H bonds form.
- [ ] 4
    - *why wrong:* That would need 4 hydrogen atoms; water has 2.

**Q5. [reason · CFCHTFTH]** Explain why a chlorine molecule (Cl₂) contains a single covalent bond.
- [✔︎] Each chlorine atom has 7 outer electrons and needs 1 more, so the two atoms share one pair, giving both a full shell of 8
- [ ] Each chlorine atom shares three pairs of electrons
    - *why wrong:* Sharing three pairs would be a triple bond; chlorine needs only 1 more electron, so it shares one pair.
- [ ] One chlorine atom transfers an electron to the other
    - *why wrong:* Transferring an electron is ionic bonding; two identical non-metal atoms share instead.
- [ ] The two atoms are held together by a sea of delocalised electrons
    - *why wrong:* A delocalised electron sea is metallic bonding; Cl₂ is a simple covalent molecule.

**Q6. [reason · CHTH]** Explain, in terms of electrons, why a nitrogen molecule (N₂) contains a triple bond.
- [✔︎] Each nitrogen atom has 5 outer electrons and needs 3 more, so the two atoms share three pairs, giving both a full shell of 8
- [ ] Nitrogen atoms share one pair of electrons
    - *why wrong:* Sharing only one pair (a single bond) would leave each nitrogen short of a full shell.
- [ ] Each nitrogen atom transfers 3 electrons to the other
    - *why wrong:* Transfer is ionic bonding; two identical non-metal atoms share electrons instead.
- [ ] Nitrogen forms a triple bond because it is a gas
    - *why wrong:* Being a gas is a consequence of weak intermolecular forces, not the reason for the triple bond.

**Q7. [reason · CHTH]** A dot-and-cross diagram of carbon dioxide shows O=C=O. Explain how this arrangement gives every atom a full outer shell.
- [✔︎] Carbon shares two pairs with each oxygen (two double bonds), reaching 8 electrons; each oxygen shares two pairs with carbon, also reaching 8
- [ ] Carbon transfers 4 electrons to the two oxygen atoms
    - *why wrong:* CO₂ is covalent (all non-metals), so electrons are shared, not transferred.
- [ ] Each atom keeps its own electrons and none are shared
    - *why wrong:* If no electrons were shared, none of the atoms would reach a full shell.
- [ ] Carbon shares one pair with each oxygen, so all reach 8
    - *why wrong:* Sharing only one pair with each oxygen would leave carbon with 6 electrons, not 8 — CO₂ needs double bonds.

**Q8. [reason · CHTH]** Explain why simple molecular substances have low melting and boiling points, despite containing strong covalent bonds.
- [✔︎] Melting and boiling only overcome the weak intermolecular forces between whole molecules; the strong covalent bonds inside the molecules are not broken
- [ ] The covalent bonds are actually very weak and break easily
    - *why wrong:* The covalent bonds are strong — that is why they stay intact when the substance melts.
- [ ] The molecules lose their electrons when heated
    - *why wrong:* No electrons are lost on melting; only the weak intermolecular forces are overcome.
- [ ] Simple molecules have no forces between them at all
    - *why wrong:* There ARE forces between molecules (intermolecular forces) — they are just weak.

**Q9. [reason · CHTH]** Compare a single, a double and a triple covalent bond in terms of the number of shared electrons.
- [✔︎] A single bond shares 2 electrons (1 pair), a double bond 4 electrons (2 pairs) and a triple bond 6 electrons (3 pairs)
- [ ] A single bond shares 1 electron, a double 2 and a triple 3
    - *why wrong:* Each bond is a shared PAIR (2 electrons), so a single bond shares 2 electrons, not 1.
- [ ] All three share the same number of electrons but differ in strength only
    - *why wrong:* The number of shared electrons increases: 2, 4 then 6 — they are not equal.
- [ ] A triple bond shares fewer electrons than a single bond
    - *why wrong:* A triple bond shares MORE electrons (6) than a single bond (2).

**Q10. [apply · CHTH]** Ammonia is NH₃. Deduce the number of covalent bonds nitrogen forms, and explain why.
- [✔︎] 3 — nitrogen has 5 outer electrons and needs 3 more, so it forms 3 single bonds with 3 hydrogen atoms
- [ ] 5 — nitrogen forms one bond for each outer electron
    - *why wrong:* Nitrogen bonds to gain electrons up to 8, not one bond per existing outer electron.
- [ ] 1 — nitrogen forms a single bond only
    - *why wrong:* One bond would leave nitrogen well short of a full shell.
- [ ] 8 — nitrogen needs 8 electrons so forms 8 bonds
    - *why wrong:* Nitrogen needs 8 electrons in its shell, but each bond provides 2 shared electrons, so it needs 3 bonds, not 8.

### Triple Foundation — 12 questions (6 recall / 6 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Carbon (Group 4) bonds with hydrogen to form methane, CH₄. Determine how many covalent bonds a carbon atom forms.
- [✔︎] 4 — carbon has 4 outer electrons and needs 4 more, so it forms 4 shared pairs
- [ ] 1 — carbon forms only one bond at a time
    - *why wrong:* Carbon forms one bond per shared pair, and it needs 4 shared pairs — not a single bond.
- [ ] 2 — carbon forms 2 bonds like oxygen
    - *why wrong:* Oxygen (Group 6) needs 2 more electrons so forms 2 bonds; carbon (Group 4) needs 4.
- [ ] 8 — carbon needs 8 electrons in total
    - *why wrong:* Carbon needs 8 electrons in its outer shell, but each BOND provides 2 shared electrons, so 4 bonds give the 8.

**Q2. [reason · CFCHTFTH]** Explain why oxygen exists as O₂ molecules rather than as single O atoms.
- [✔︎] Each oxygen atom has 6 outer electrons and needs 2 more; by sharing two pairs with another O atom, both reach a full outer shell of 8
- [ ] Two oxygen atoms join to make a more stable element in the periodic table
    - *why wrong:* Bonding does not change an element's position in the periodic table; O₂ forms because of electron sharing.
- [ ] Oxygen atoms repel each other and pair up to cancel the repulsion
    - *why wrong:* Atoms of the same element do repel slightly, but covalent bonding (sharing) creates a stronger overall attraction.
- [ ] Oxygen forms O₂ so that it can be a gas at room temperature
    - *why wrong:* Whether a substance is a gas depends on intermolecular forces, not on why the molecule forms.

**Q3. [recall · CFCHTFTH]** Describe what is meant by a covalent bond.
- [✔︎] A shared pair of electrons between two non-metal atoms, attracted to both nuclei
- [ ] The transfer of electrons from a metal to a non-metal
    - *why wrong:* Transferring electrons is ionic bonding, which occurs between a metal and a non-metal.
- [ ] A sea of delocalised electrons shared between metal ions
    - *why wrong:* A delocalised electron sea is the metallic bonding model.
- [ ] A weak attraction between two separate molecules
    - *why wrong:* That describes an intermolecular force, which acts BETWEEN molecules, not the bond within one.

**Q4. [apply · CFCHTFTH]** State the number of single covalent bonds present in a water molecule, H₂O.
- [✔︎] 2
- [ ] 1
    - *why wrong:* Oxygen forms 1 bond with each of the 2 hydrogen atoms, giving 2 bonds — not 1.
- [ ] 3
    - *why wrong:* Water has only 2 hydrogen atoms, so only 2 O–H bonds form.
- [ ] 4
    - *why wrong:* That would need 4 hydrogen atoms; water has 2.

**Q5. [reason · CFCHTFTH]** Explain why a chlorine molecule (Cl₂) contains a single covalent bond.
- [✔︎] Each chlorine atom has 7 outer electrons and needs 1 more, so the two atoms share one pair, giving both a full shell of 8
- [ ] Each chlorine atom shares three pairs of electrons
    - *why wrong:* Sharing three pairs would be a triple bond; chlorine needs only 1 more electron, so it shares one pair.
- [ ] One chlorine atom transfers an electron to the other
    - *why wrong:* Transferring an electron is ionic bonding; two identical non-metal atoms share instead.
- [ ] The two atoms are held together by a sea of delocalised electrons
    - *why wrong:* A delocalised electron sea is metallic bonding; Cl₂ is a simple covalent molecule.

**Q6. [recall · CFTF]** State the type of elements that form covalent bonds.
- [✔︎] Non-metals only
- [ ] Metals only
    - *why wrong:* A metal only would give metallic bonding.
- [ ] A metal and a non-metal
    - *why wrong:* A metal with a non-metal gives ionic bonding (transfer), not covalent.
- [ ] Noble gases only
    - *why wrong:* Noble gases rarely bond at all, as their outer shells are already full.

**Q7. [recall · CFTF]** State what is shared between atoms in a covalent bond.
- [✔︎] A pair of electrons
- [ ] A proton
    - *why wrong:* Protons stay in the nucleus and are not shared in bonding.
- [ ] A neutron
    - *why wrong:* Neutrons stay in the nucleus and are not involved in bonding.
- [ ] A whole atom
    - *why wrong:* Atoms are not shared — only a pair of outer electrons is.

**Q8. [recall · CFTF]** Name the type of covalent bond formed when two pairs of electrons are shared between two atoms.
- [✔︎] A double bond
- [ ] A single bond
    - *why wrong:* A single bond shares only one pair of electrons.
- [ ] A triple bond
    - *why wrong:* A triple bond shares three pairs, not two.
- [ ] An ionic bond
    - *why wrong:* An ionic bond involves transfer, not shared pairs.

**Q9. [apply · CFTF]** Identify which substance contains covalent bonds.
- [✔︎] Carbon dioxide
- [ ] Sodium chloride
    - *why wrong:* Sodium chloride is a metal + non-metal — ionic bonding.
- [ ] Magnesium oxide
    - *why wrong:* Magnesium oxide is a metal + non-metal — ionic bonding.
- [ ] Copper
    - *why wrong:* Copper is a pure metal — metallic bonding.

**Q10. [recall · CFTF]** State how many shared pairs of electrons there are in a triple bond.
- [✔︎] 3
- [ ] 1
    - *why wrong:* One shared pair is a single bond.
- [ ] 2
    - *why wrong:* Two shared pairs is a double bond.
- [ ] 6
    - *why wrong:* A triple bond has 3 shared pairs (which is 6 electrons, but only 3 pairs).

**Q11. [recall · TF]** State whether the covalent bonds within a molecule are strong or weak.
- [✔︎] Strong
- [ ] Weak
    - *why wrong:* Covalent bonds are strong; it is the forces BETWEEN molecules that are weak.
- [ ] They have no strength
    - *why wrong:* Covalent bonds definitely hold atoms together strongly within a molecule.
- [ ] It depends on the colour of the substance
    - *why wrong:* Colour has nothing to do with bond strength.

**Q12. [apply · TF]** Describe how a dot-and-cross diagram represents the bonding in a hydrogen molecule, H₂.
- [✔︎] The shared pair of electrons is drawn between the two hydrogen atoms, one shown as a dot and one as a cross, giving each atom a full shell of 2
- [ ] Each hydrogen keeps its own electron with none shared
    - *why wrong:* If no electrons were shared, neither hydrogen would reach a full shell.
- [ ] One hydrogen transfers its electron to the other
    - *why wrong:* Transfer is ionic bonding; hydrogen atoms share instead.
- [ ] A sea of electrons is drawn around the two hydrogen atoms
    - *why wrong:* A delocalised electron sea is the metallic model, not a covalent dot-and-cross.

### Triple Higher — 12 questions (1 recall / 11 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Carbon (Group 4) bonds with hydrogen to form methane, CH₄. Determine how many covalent bonds a carbon atom forms.
- [✔︎] 4 — carbon has 4 outer electrons and needs 4 more, so it forms 4 shared pairs
- [ ] 1 — carbon forms only one bond at a time
    - *why wrong:* Carbon forms one bond per shared pair, and it needs 4 shared pairs — not a single bond.
- [ ] 2 — carbon forms 2 bonds like oxygen
    - *why wrong:* Oxygen (Group 6) needs 2 more electrons so forms 2 bonds; carbon (Group 4) needs 4.
- [ ] 8 — carbon needs 8 electrons in total
    - *why wrong:* Carbon needs 8 electrons in its outer shell, but each BOND provides 2 shared electrons, so 4 bonds give the 8.

**Q2. [reason · CFCHTFTH]** Explain why oxygen exists as O₂ molecules rather than as single O atoms.
- [✔︎] Each oxygen atom has 6 outer electrons and needs 2 more; by sharing two pairs with another O atom, both reach a full outer shell of 8
- [ ] Two oxygen atoms join to make a more stable element in the periodic table
    - *why wrong:* Bonding does not change an element's position in the periodic table; O₂ forms because of electron sharing.
- [ ] Oxygen atoms repel each other and pair up to cancel the repulsion
    - *why wrong:* Atoms of the same element do repel slightly, but covalent bonding (sharing) creates a stronger overall attraction.
- [ ] Oxygen forms O₂ so that it can be a gas at room temperature
    - *why wrong:* Whether a substance is a gas depends on intermolecular forces, not on why the molecule forms.

**Q3. [recall · CFCHTFTH]** Describe what is meant by a covalent bond.
- [✔︎] A shared pair of electrons between two non-metal atoms, attracted to both nuclei
- [ ] The transfer of electrons from a metal to a non-metal
    - *why wrong:* Transferring electrons is ionic bonding, which occurs between a metal and a non-metal.
- [ ] A sea of delocalised electrons shared between metal ions
    - *why wrong:* A delocalised electron sea is the metallic bonding model.
- [ ] A weak attraction between two separate molecules
    - *why wrong:* That describes an intermolecular force, which acts BETWEEN molecules, not the bond within one.

**Q4. [apply · CFCHTFTH]** State the number of single covalent bonds present in a water molecule, H₂O.
- [✔︎] 2
- [ ] 1
    - *why wrong:* Oxygen forms 1 bond with each of the 2 hydrogen atoms, giving 2 bonds — not 1.
- [ ] 3
    - *why wrong:* Water has only 2 hydrogen atoms, so only 2 O–H bonds form.
- [ ] 4
    - *why wrong:* That would need 4 hydrogen atoms; water has 2.

**Q5. [reason · CFCHTFTH]** Explain why a chlorine molecule (Cl₂) contains a single covalent bond.
- [✔︎] Each chlorine atom has 7 outer electrons and needs 1 more, so the two atoms share one pair, giving both a full shell of 8
- [ ] Each chlorine atom shares three pairs of electrons
    - *why wrong:* Sharing three pairs would be a triple bond; chlorine needs only 1 more electron, so it shares one pair.
- [ ] One chlorine atom transfers an electron to the other
    - *why wrong:* Transferring an electron is ionic bonding; two identical non-metal atoms share instead.
- [ ] The two atoms are held together by a sea of delocalised electrons
    - *why wrong:* A delocalised electron sea is metallic bonding; Cl₂ is a simple covalent molecule.

**Q6. [reason · CHTH]** Explain, in terms of electrons, why a nitrogen molecule (N₂) contains a triple bond.
- [✔︎] Each nitrogen atom has 5 outer electrons and needs 3 more, so the two atoms share three pairs, giving both a full shell of 8
- [ ] Nitrogen atoms share one pair of electrons
    - *why wrong:* Sharing only one pair (a single bond) would leave each nitrogen short of a full shell.
- [ ] Each nitrogen atom transfers 3 electrons to the other
    - *why wrong:* Transfer is ionic bonding; two identical non-metal atoms share electrons instead.
- [ ] Nitrogen forms a triple bond because it is a gas
    - *why wrong:* Being a gas is a consequence of weak intermolecular forces, not the reason for the triple bond.

**Q7. [reason · CHTH]** A dot-and-cross diagram of carbon dioxide shows O=C=O. Explain how this arrangement gives every atom a full outer shell.
- [✔︎] Carbon shares two pairs with each oxygen (two double bonds), reaching 8 electrons; each oxygen shares two pairs with carbon, also reaching 8
- [ ] Carbon transfers 4 electrons to the two oxygen atoms
    - *why wrong:* CO₂ is covalent (all non-metals), so electrons are shared, not transferred.
- [ ] Each atom keeps its own electrons and none are shared
    - *why wrong:* If no electrons were shared, none of the atoms would reach a full shell.
- [ ] Carbon shares one pair with each oxygen, so all reach 8
    - *why wrong:* Sharing only one pair with each oxygen would leave carbon with 6 electrons, not 8 — CO₂ needs double bonds.

**Q8. [reason · CHTH]** Explain why simple molecular substances have low melting and boiling points, despite containing strong covalent bonds.
- [✔︎] Melting and boiling only overcome the weak intermolecular forces between whole molecules; the strong covalent bonds inside the molecules are not broken
- [ ] The covalent bonds are actually very weak and break easily
    - *why wrong:* The covalent bonds are strong — that is why they stay intact when the substance melts.
- [ ] The molecules lose their electrons when heated
    - *why wrong:* No electrons are lost on melting; only the weak intermolecular forces are overcome.
- [ ] Simple molecules have no forces between them at all
    - *why wrong:* There ARE forces between molecules (intermolecular forces) — they are just weak.

**Q9. [reason · CHTH]** Compare a single, a double and a triple covalent bond in terms of the number of shared electrons.
- [✔︎] A single bond shares 2 electrons (1 pair), a double bond 4 electrons (2 pairs) and a triple bond 6 electrons (3 pairs)
- [ ] A single bond shares 1 electron, a double 2 and a triple 3
    - *why wrong:* Each bond is a shared PAIR (2 electrons), so a single bond shares 2 electrons, not 1.
- [ ] All three share the same number of electrons but differ in strength only
    - *why wrong:* The number of shared electrons increases: 2, 4 then 6 — they are not equal.
- [ ] A triple bond shares fewer electrons than a single bond
    - *why wrong:* A triple bond shares MORE electrons (6) than a single bond (2).

**Q10. [apply · CHTH]** Ammonia is NH₃. Deduce the number of covalent bonds nitrogen forms, and explain why.
- [✔︎] 3 — nitrogen has 5 outer electrons and needs 3 more, so it forms 3 single bonds with 3 hydrogen atoms
- [ ] 5 — nitrogen forms one bond for each outer electron
    - *why wrong:* Nitrogen bonds to gain electrons up to 8, not one bond per existing outer electron.
- [ ] 1 — nitrogen forms a single bond only
    - *why wrong:* One bond would leave nitrogen well short of a full shell.
- [ ] 8 — nitrogen needs 8 electrons so forms 8 bonds
    - *why wrong:* Nitrogen needs 8 electrons in its shell, but each bond provides 2 shared electrons, so it needs 3 bonds, not 8.

**Q11. [reason · TH] ⭐** Explain why the boiling points of the halogens increase from fluorine to iodine, even though each molecule contains a single covalent bond.
- [✔︎] Larger molecules (more electrons) have stronger intermolecular forces, so more energy is needed to separate them — the covalent bond strength is not the reason
- [ ] The covalent bond gets stronger down the group
    - *why wrong:* Boiling separates molecules by overcoming intermolecular forces; it does not break the covalent bond.
- [ ] The molecules gain more atoms down the group
    - *why wrong:* Each halogen molecule is still diatomic (2 atoms) — the atom count does not change down the group.
- [ ] Iodine is ionic while fluorine is covalent
    - *why wrong:* All the halogens form simple covalent molecules; none is ionic.
  > 🚩 **Reviewer note:** Intermolecular-forces trend down a group at Triple Higher. Confirm this is the depth you want here.

**Q12. [reason · TH]** A dot-and-cross diagram shows only the outer-shell electrons. Explain one limitation of using it to represent a molecule such as methane.
- [✔︎] It does not show the molecule's real 3D shape or the inner electrons, so it is a simplified model of the actual molecule
- [ ] It uses the wrong number of shared electrons
    - *why wrong:* A correct dot-and-cross uses the right number of shared electrons — that is not the limitation.
- [ ] It cannot show which atom each electron came from
    - *why wrong:* Showing which atom each electron came from (dots vs crosses) is exactly what the diagram DOES.
- [ ] It wrongly shows the bonding as ionic
    - *why wrong:* A dot-and-cross for methane correctly shows shared pairs (covalent), not transfer.


---

## Metallic Bonding  ·  `metallic-bonding`  ·  AQA 5.2.1.5

> 🚩 **Triple-depth call (your review):** MATCHED — AQA 5.2.1.5 (metallic model, properties, alloys) is identical for Combined and Triple. Foundation difficulty is the same across both pathways. The delocalised-electron and alloy reasoning gives genuine HIGHER lift (both Combined-H and Triple-H). No AQA Triple-only content on this page.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often say the metallic bond is an attraction between neighbouring metal atoms. It is not between atoms: the metal atoms lose their outer electrons to become positive ions, and the bond is the strong electrostatic attraction between those positive ions and the surrounding sea of delocalised electrons. That electron sea is also why metals bend rather than shatter — the layers of ions can slide while the sea holds everything together.

**Question sets by tier** (each item shows tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (3 recall / 7 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why metals are good conductors of electricity.
- [✔︎] They contain delocalised electrons that are free to move through the structure and carry charge
- [ ] Their positive ions move through the metal to carry the current
    - *why wrong:* The positive ions are held in the lattice; it is the mobile delocalised electrons that carry charge.
- [ ] They have more protons than non-metals, which conduct the current
    - *why wrong:* Proton number sets an element's identity, not its conductivity — many non-metals have lots of protons but do not conduct.
- [ ] The regular lattice lets electrical signals jump between fixed ions
    - *why wrong:* Conduction comes from the free electrons moving, not from the fixed ions.

**Q2. [reason · CFCHTFTH]** Explain why steel is harder than pure iron.
- [✔︎] The added carbon atoms are a different size to the iron atoms, so they distort the regular lattice and stop the layers of ions sliding
- [ ] Steel contains more electrons, which makes stronger metallic bonds
    - *why wrong:* There may be more atoms overall, but the KEY reason is the disruption of the lattice by different-sized atoms.
- [ ] The carbon atoms fill the gaps, which increases the density and hardness
    - *why wrong:* Carbon does occupy spaces, but the hardening comes specifically from preventing the layers from sliding.
- [ ] Steel is purer than iron, and purer metals are always harder
    - *why wrong:* Steel is iron made LESS pure (carbon added); it is the added, differently-sized atoms that harden it.

**Q3. [apply · CFCHTFTH]** Describe the structure of a metal according to the metallic bonding model.
- [✔︎] A regular lattice of positive metal ions surrounded by a sea of delocalised electrons
- [ ] A giant lattice of alternating positive and negative ions
    - *why wrong:* Alternating positive and negative ions describes an IONIC lattice, not a metal.
- [ ] Separate metal molecules held by weak intermolecular forces
    - *why wrong:* Metals are giant structures, not separate molecules.
- [ ] Neutral metal atoms sharing pairs of electrons in covalent bonds
    - *why wrong:* Metals do not share pairs in covalent bonds; their outer electrons are delocalised.

**Q4. [reason · CFCHTFTH]** Explain why metals are malleable (can be hammered into shape).
- [✔︎] The layers of positive ions can slide over one another, and the electron sea re-surrounds them in their new positions without the bonding breaking
- [ ] The metallic bonds break and then instantly reform as new bonds
    - *why wrong:* The bonding does not break — the electron sea keeps holding the ions together as the layers slide.
- [ ] The delocalised electrons push the ions apart to let them move
    - *why wrong:* The electrons hold the ions together; they do not push them apart.
- [ ] The ions are so small that they simply flow like a liquid
    - *why wrong:* The ions stay in a solid lattice; they slide as layers rather than flowing freely.

**Q5. [reason · CFCHTFTH]** Explain why metals have high melting points.
- [✔︎] There is strong electrostatic attraction between the many positive ions and the sea of delocalised electrons, so a lot of energy is needed to overcome it
- [ ] Metals contain strong covalent bonds throughout
    - *why wrong:* Metals do not contain covalent bonds; the metallic bond is the ion-to-electron-sea attraction.
- [ ] The delocalised electrons are very heavy
    - *why wrong:* Electrons have almost no mass; the high melting point is due to the strength of the attraction, not electron mass.
- [ ] Metal atoms are simply packed together with no forces to overcome
    - *why wrong:* There ARE strong forces — that is exactly why the melting point is high.

**Q6. [recall · CFTF]** Name the particles that are free to move in a metal.
- [✔︎] Delocalised electrons
- [ ] Positive ions
    - *why wrong:* The positive ions are fixed in the lattice; only the electrons are free to move.
- [ ] Neutrons
    - *why wrong:* Neutrons are locked in the nuclei and never move freely.
- [ ] Whole atoms
    - *why wrong:* The atoms have become fixed positive ions; it is their outer electrons that are free.

**Q7. [recall · CFTF]** State what is meant by an alloy.
- [✔︎] A mixture of a metal with one or more other elements
- [ ] A very pure sample of a single metal
    - *why wrong:* A pure metal is the opposite of an alloy; an alloy is deliberately mixed.
- [ ] A compound of a metal and a non-metal
    - *why wrong:* An alloy is a MIXTURE, not a chemically bonded compound.
- [ ] A metal that contains no electrons
    - *why wrong:* All metals contain delocalised electrons; that is not what defines an alloy.

**Q8. [apply · CFTF]** Identify a pair of properties of metals that both result from metallic bonding.
- [✔︎] Good electrical conductivity and malleability
- [ ] Being brittle and being an electrical insulator
    - *why wrong:* Metals are malleable, not brittle, and they conduct rather than insulate.
- [ ] Low melting point and low density in every case
    - *why wrong:* Most metals have HIGH melting points and are dense.
- [ ] Dissolving in water and conducting only when molten
    - *why wrong:* Conducting only when molten describes ionic compounds, not metals (metals conduct as solids).

**Q9. [recall · CFTF]** State the charge on the metal ions in the metallic bonding model.
- [✔︎] Positive
- [ ] Negative
    - *why wrong:* The ions are positive because the atoms have LOST electrons into the sea.
- [ ] Neutral (no charge)
    - *why wrong:* If the ions were neutral there would be nothing for the electron sea to attract.
- [ ] It changes constantly
    - *why wrong:* The ion charge is fixed at positive; it is the electrons that move.

**Q10. [apply · CFTF]** Identify why alloys are generally harder than the pure metals they are made from.
- [✔︎] The different-sized atoms disrupt the regular lattice so the layers cannot slide as easily
- [ ] Alloys contain many more delocalised electrons
    - *why wrong:* The hardening is about lattice disruption, not the number of electrons.
- [ ] Alloys are purer than the original metal
    - *why wrong:* Alloys are LESS pure (they are mixtures), which is exactly why they are harder.
- [ ] Alloys have no metallic bonding, so they are more rigid
    - *why wrong:* Alloys still have metallic bonding — that is why they remain conductive and are still metals.

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why metals are good conductors of electricity.
- [✔︎] They contain delocalised electrons that are free to move through the structure and carry charge
- [ ] Their positive ions move through the metal to carry the current
    - *why wrong:* The positive ions are held in the lattice; it is the mobile delocalised electrons that carry charge.
- [ ] They have more protons than non-metals, which conduct the current
    - *why wrong:* Proton number sets an element's identity, not its conductivity — many non-metals have lots of protons but do not conduct.
- [ ] The regular lattice lets electrical signals jump between fixed ions
    - *why wrong:* Conduction comes from the free electrons moving, not from the fixed ions.

**Q2. [reason · CFCHTFTH]** Explain why steel is harder than pure iron.
- [✔︎] The added carbon atoms are a different size to the iron atoms, so they distort the regular lattice and stop the layers of ions sliding
- [ ] Steel contains more electrons, which makes stronger metallic bonds
    - *why wrong:* There may be more atoms overall, but the KEY reason is the disruption of the lattice by different-sized atoms.
- [ ] The carbon atoms fill the gaps, which increases the density and hardness
    - *why wrong:* Carbon does occupy spaces, but the hardening comes specifically from preventing the layers from sliding.
- [ ] Steel is purer than iron, and purer metals are always harder
    - *why wrong:* Steel is iron made LESS pure (carbon added); it is the added, differently-sized atoms that harden it.

**Q3. [apply · CFCHTFTH]** Describe the structure of a metal according to the metallic bonding model.
- [✔︎] A regular lattice of positive metal ions surrounded by a sea of delocalised electrons
- [ ] A giant lattice of alternating positive and negative ions
    - *why wrong:* Alternating positive and negative ions describes an IONIC lattice, not a metal.
- [ ] Separate metal molecules held by weak intermolecular forces
    - *why wrong:* Metals are giant structures, not separate molecules.
- [ ] Neutral metal atoms sharing pairs of electrons in covalent bonds
    - *why wrong:* Metals do not share pairs in covalent bonds; their outer electrons are delocalised.

**Q4. [reason · CFCHTFTH]** Explain why metals are malleable (can be hammered into shape).
- [✔︎] The layers of positive ions can slide over one another, and the electron sea re-surrounds them in their new positions without the bonding breaking
- [ ] The metallic bonds break and then instantly reform as new bonds
    - *why wrong:* The bonding does not break — the electron sea keeps holding the ions together as the layers slide.
- [ ] The delocalised electrons push the ions apart to let them move
    - *why wrong:* The electrons hold the ions together; they do not push them apart.
- [ ] The ions are so small that they simply flow like a liquid
    - *why wrong:* The ions stay in a solid lattice; they slide as layers rather than flowing freely.

**Q5. [reason · CFCHTFTH]** Explain why metals have high melting points.
- [✔︎] There is strong electrostatic attraction between the many positive ions and the sea of delocalised electrons, so a lot of energy is needed to overcome it
- [ ] Metals contain strong covalent bonds throughout
    - *why wrong:* Metals do not contain covalent bonds; the metallic bond is the ion-to-electron-sea attraction.
- [ ] The delocalised electrons are very heavy
    - *why wrong:* Electrons have almost no mass; the high melting point is due to the strength of the attraction, not electron mass.
- [ ] Metal atoms are simply packed together with no forces to overcome
    - *why wrong:* There ARE strong forces — that is exactly why the melting point is high.

**Q6. [reason · CHTH]** Explain why metals are good conductors of both electricity and heat.
- [✔︎] The delocalised electrons are free to move: they carry electric charge, and they also transfer kinetic (thermal) energy quickly through the structure
- [ ] The positive ions vibrate and pass on both current and heat
    - *why wrong:* Ion vibration transfers some heat, but electrical current and most heat transfer are carried by the mobile electrons.
- [ ] The covalent bonds carry the current and the heat
    - *why wrong:* Metals have no covalent bonds; conduction is due to delocalised electrons.
- [ ] Metals absorb heat and electricity because they are shiny
    - *why wrong:* Shininess is unrelated to conductivity.

**Q7. [reason · CHTH]** Explain why an alloy such as bronze is harder than the pure copper it is mostly made from.
- [✔︎] The tin atoms are a different size to the copper atoms, distorting the regular layers so they cannot slide over each other as easily
- [ ] Bronze contains stronger covalent bonds than copper
    - *why wrong:* Metals and alloys have no covalent bonds; the hardening is due to lattice distortion.
- [ ] Tin is a gas that fills the gaps in the copper
    - *why wrong:* Tin is a solid metal; it sits within the lattice as differently-sized atoms.
- [ ] Bronze has fewer delocalised electrons than copper
    - *why wrong:* The number of electrons is not the reason — disrupting the layers is.

**Q8. [reason · CHTH]** Compare metallic bonding with ionic bonding in terms of the particles present and whether the solid conducts electricity.
- [✔︎] A metal has positive ions in a sea of delocalised electrons and conducts as a solid; an ionic solid has fixed positive and negative ions and does not conduct until molten or dissolved
- [ ] Both have delocalised electrons and both conduct as solids
    - *why wrong:* Ionic solids have no delocalised electrons and do not conduct as solids, so they are not the same.
- [ ] Both have fixed ions and neither conducts as a solid
    - *why wrong:* Metals DO conduct as solids (mobile electrons), so 'neither conducts' is wrong.
- [ ] A metal has positive and negative ions; an ionic solid has an electron sea
    - *why wrong:* This swaps them over: the electron sea is in the METAL; positive and negative ions are in the IONIC solid.

**Q9. [reason · CHTH]** Explain why metals can be drawn into wires (are ductile) without breaking.
- [✔︎] The layers of positive ions slide into new positions while the delocalised electron sea keeps them bonded, so the structure does not break
- [ ] The metallic bonds are weak, so the metal stretches easily
    - *why wrong:* The bonds are strong; ductility comes from the layers sliding while the electron sea maintains the bonding.
- [ ] The ions turn into a liquid as the wire is drawn
    - *why wrong:* The metal stays solid while being drawn into a wire.
- [ ] The electrons leave the metal, letting the ions move
    - *why wrong:* The electrons stay in the metal (that is what holds it together as it deforms).

**Q10. [reason · CHTH]** Copper is used for electrical wiring. Suggest two properties of copper that make it suitable, and link each to metallic bonding.
- [✔︎] It conducts electricity well (delocalised electrons carry charge) and it is ductile (layers of ions slide, so it can be drawn into wires)
- [ ] It is brittle (so it snaps to length) and it is an insulator (so it is safe)
    - *why wrong:* Brittleness and insulation would make copper useless for wiring — it is ductile and conductive.
- [ ] It has a low melting point (so it melts in use) and it is magnetic
    - *why wrong:* A low melting point would be a disadvantage in a wire, and copper's suitability is not due to magnetism.
- [ ] It is radioactive (so it carries current) and it is transparent
    - *why wrong:* Copper is neither radioactive nor transparent, and neither would help it carry current.

### Triple Foundation — 12 questions (3 recall / 9 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why metals are good conductors of electricity.
- [✔︎] They contain delocalised electrons that are free to move through the structure and carry charge
- [ ] Their positive ions move through the metal to carry the current
    - *why wrong:* The positive ions are held in the lattice; it is the mobile delocalised electrons that carry charge.
- [ ] They have more protons than non-metals, which conduct the current
    - *why wrong:* Proton number sets an element's identity, not its conductivity — many non-metals have lots of protons but do not conduct.
- [ ] The regular lattice lets electrical signals jump between fixed ions
    - *why wrong:* Conduction comes from the free electrons moving, not from the fixed ions.

**Q2. [reason · CFCHTFTH]** Explain why steel is harder than pure iron.
- [✔︎] The added carbon atoms are a different size to the iron atoms, so they distort the regular lattice and stop the layers of ions sliding
- [ ] Steel contains more electrons, which makes stronger metallic bonds
    - *why wrong:* There may be more atoms overall, but the KEY reason is the disruption of the lattice by different-sized atoms.
- [ ] The carbon atoms fill the gaps, which increases the density and hardness
    - *why wrong:* Carbon does occupy spaces, but the hardening comes specifically from preventing the layers from sliding.
- [ ] Steel is purer than iron, and purer metals are always harder
    - *why wrong:* Steel is iron made LESS pure (carbon added); it is the added, differently-sized atoms that harden it.

**Q3. [apply · CFCHTFTH]** Describe the structure of a metal according to the metallic bonding model.
- [✔︎] A regular lattice of positive metal ions surrounded by a sea of delocalised electrons
- [ ] A giant lattice of alternating positive and negative ions
    - *why wrong:* Alternating positive and negative ions describes an IONIC lattice, not a metal.
- [ ] Separate metal molecules held by weak intermolecular forces
    - *why wrong:* Metals are giant structures, not separate molecules.
- [ ] Neutral metal atoms sharing pairs of electrons in covalent bonds
    - *why wrong:* Metals do not share pairs in covalent bonds; their outer electrons are delocalised.

**Q4. [reason · CFCHTFTH]** Explain why metals are malleable (can be hammered into shape).
- [✔︎] The layers of positive ions can slide over one another, and the electron sea re-surrounds them in their new positions without the bonding breaking
- [ ] The metallic bonds break and then instantly reform as new bonds
    - *why wrong:* The bonding does not break — the electron sea keeps holding the ions together as the layers slide.
- [ ] The delocalised electrons push the ions apart to let them move
    - *why wrong:* The electrons hold the ions together; they do not push them apart.
- [ ] The ions are so small that they simply flow like a liquid
    - *why wrong:* The ions stay in a solid lattice; they slide as layers rather than flowing freely.

**Q5. [reason · CFCHTFTH]** Explain why metals have high melting points.
- [✔︎] There is strong electrostatic attraction between the many positive ions and the sea of delocalised electrons, so a lot of energy is needed to overcome it
- [ ] Metals contain strong covalent bonds throughout
    - *why wrong:* Metals do not contain covalent bonds; the metallic bond is the ion-to-electron-sea attraction.
- [ ] The delocalised electrons are very heavy
    - *why wrong:* Electrons have almost no mass; the high melting point is due to the strength of the attraction, not electron mass.
- [ ] Metal atoms are simply packed together with no forces to overcome
    - *why wrong:* There ARE strong forces — that is exactly why the melting point is high.

**Q6. [recall · CFTF]** Name the particles that are free to move in a metal.
- [✔︎] Delocalised electrons
- [ ] Positive ions
    - *why wrong:* The positive ions are fixed in the lattice; only the electrons are free to move.
- [ ] Neutrons
    - *why wrong:* Neutrons are locked in the nuclei and never move freely.
- [ ] Whole atoms
    - *why wrong:* The atoms have become fixed positive ions; it is their outer electrons that are free.

**Q7. [recall · CFTF]** State what is meant by an alloy.
- [✔︎] A mixture of a metal with one or more other elements
- [ ] A very pure sample of a single metal
    - *why wrong:* A pure metal is the opposite of an alloy; an alloy is deliberately mixed.
- [ ] A compound of a metal and a non-metal
    - *why wrong:* An alloy is a MIXTURE, not a chemically bonded compound.
- [ ] A metal that contains no electrons
    - *why wrong:* All metals contain delocalised electrons; that is not what defines an alloy.

**Q8. [apply · CFTF]** Identify a pair of properties of metals that both result from metallic bonding.
- [✔︎] Good electrical conductivity and malleability
- [ ] Being brittle and being an electrical insulator
    - *why wrong:* Metals are malleable, not brittle, and they conduct rather than insulate.
- [ ] Low melting point and low density in every case
    - *why wrong:* Most metals have HIGH melting points and are dense.
- [ ] Dissolving in water and conducting only when molten
    - *why wrong:* Conducting only when molten describes ionic compounds, not metals (metals conduct as solids).

**Q9. [recall · CFTF]** State the charge on the metal ions in the metallic bonding model.
- [✔︎] Positive
- [ ] Negative
    - *why wrong:* The ions are positive because the atoms have LOST electrons into the sea.
- [ ] Neutral (no charge)
    - *why wrong:* If the ions were neutral there would be nothing for the electron sea to attract.
- [ ] It changes constantly
    - *why wrong:* The ion charge is fixed at positive; it is the electrons that move.

**Q10. [apply · CFTF]** Identify why alloys are generally harder than the pure metals they are made from.
- [✔︎] The different-sized atoms disrupt the regular lattice so the layers cannot slide as easily
- [ ] Alloys contain many more delocalised electrons
    - *why wrong:* The hardening is about lattice disruption, not the number of electrons.
- [ ] Alloys are purer than the original metal
    - *why wrong:* Alloys are LESS pure (they are mixtures), which is exactly why they are harder.
- [ ] Alloys have no metallic bonding, so they are more rigid
    - *why wrong:* Alloys still have metallic bonding — that is why they remain conductive and are still metals.

**Q11. [apply · TF]** State why metals can conduct electricity when solid, unlike ionic compounds.
- [✔︎] Their delocalised electrons are free to move even in the solid, whereas the ions in a solid ionic compound are fixed
- [ ] Metals contain free-moving ions in the solid
    - *why wrong:* It is the electrons that move in a metal, not the ions.
- [ ] Metals are always molten at room temperature
    - *why wrong:* Most metals are solid at room temperature and still conduct.
- [ ] Ionic compounds have no charged particles
    - *why wrong:* Ionic compounds do contain charged particles (ions) — they just cannot move when solid.

**Q12. [apply · TF]** Identify a correct pairing of a common alloy with the main metal it is made from.
- [✔︎] Steel — mostly iron
- [ ] Bronze — mostly zinc
    - *why wrong:* Bronze is mostly copper (with tin), not zinc.
- [ ] Brass — mostly tin
    - *why wrong:* Brass is mostly copper (with zinc), not tin.
- [ ] Steel — mostly copper
    - *why wrong:* Steel is mostly iron (with a little carbon), not copper.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why metals are good conductors of electricity.
- [✔︎] They contain delocalised electrons that are free to move through the structure and carry charge
- [ ] Their positive ions move through the metal to carry the current
    - *why wrong:* The positive ions are held in the lattice; it is the mobile delocalised electrons that carry charge.
- [ ] They have more protons than non-metals, which conduct the current
    - *why wrong:* Proton number sets an element's identity, not its conductivity — many non-metals have lots of protons but do not conduct.
- [ ] The regular lattice lets electrical signals jump between fixed ions
    - *why wrong:* Conduction comes from the free electrons moving, not from the fixed ions.

**Q2. [reason · CFCHTFTH]** Explain why steel is harder than pure iron.
- [✔︎] The added carbon atoms are a different size to the iron atoms, so they distort the regular lattice and stop the layers of ions sliding
- [ ] Steel contains more electrons, which makes stronger metallic bonds
    - *why wrong:* There may be more atoms overall, but the KEY reason is the disruption of the lattice by different-sized atoms.
- [ ] The carbon atoms fill the gaps, which increases the density and hardness
    - *why wrong:* Carbon does occupy spaces, but the hardening comes specifically from preventing the layers from sliding.
- [ ] Steel is purer than iron, and purer metals are always harder
    - *why wrong:* Steel is iron made LESS pure (carbon added); it is the added, differently-sized atoms that harden it.

**Q3. [apply · CFCHTFTH]** Describe the structure of a metal according to the metallic bonding model.
- [✔︎] A regular lattice of positive metal ions surrounded by a sea of delocalised electrons
- [ ] A giant lattice of alternating positive and negative ions
    - *why wrong:* Alternating positive and negative ions describes an IONIC lattice, not a metal.
- [ ] Separate metal molecules held by weak intermolecular forces
    - *why wrong:* Metals are giant structures, not separate molecules.
- [ ] Neutral metal atoms sharing pairs of electrons in covalent bonds
    - *why wrong:* Metals do not share pairs in covalent bonds; their outer electrons are delocalised.

**Q4. [reason · CFCHTFTH]** Explain why metals are malleable (can be hammered into shape).
- [✔︎] The layers of positive ions can slide over one another, and the electron sea re-surrounds them in their new positions without the bonding breaking
- [ ] The metallic bonds break and then instantly reform as new bonds
    - *why wrong:* The bonding does not break — the electron sea keeps holding the ions together as the layers slide.
- [ ] The delocalised electrons push the ions apart to let them move
    - *why wrong:* The electrons hold the ions together; they do not push them apart.
- [ ] The ions are so small that they simply flow like a liquid
    - *why wrong:* The ions stay in a solid lattice; they slide as layers rather than flowing freely.

**Q5. [reason · CFCHTFTH]** Explain why metals have high melting points.
- [✔︎] There is strong electrostatic attraction between the many positive ions and the sea of delocalised electrons, so a lot of energy is needed to overcome it
- [ ] Metals contain strong covalent bonds throughout
    - *why wrong:* Metals do not contain covalent bonds; the metallic bond is the ion-to-electron-sea attraction.
- [ ] The delocalised electrons are very heavy
    - *why wrong:* Electrons have almost no mass; the high melting point is due to the strength of the attraction, not electron mass.
- [ ] Metal atoms are simply packed together with no forces to overcome
    - *why wrong:* There ARE strong forces — that is exactly why the melting point is high.

**Q6. [reason · CHTH]** Explain why metals are good conductors of both electricity and heat.
- [✔︎] The delocalised electrons are free to move: they carry electric charge, and they also transfer kinetic (thermal) energy quickly through the structure
- [ ] The positive ions vibrate and pass on both current and heat
    - *why wrong:* Ion vibration transfers some heat, but electrical current and most heat transfer are carried by the mobile electrons.
- [ ] The covalent bonds carry the current and the heat
    - *why wrong:* Metals have no covalent bonds; conduction is due to delocalised electrons.
- [ ] Metals absorb heat and electricity because they are shiny
    - *why wrong:* Shininess is unrelated to conductivity.

**Q7. [reason · CHTH]** Explain why an alloy such as bronze is harder than the pure copper it is mostly made from.
- [✔︎] The tin atoms are a different size to the copper atoms, distorting the regular layers so they cannot slide over each other as easily
- [ ] Bronze contains stronger covalent bonds than copper
    - *why wrong:* Metals and alloys have no covalent bonds; the hardening is due to lattice distortion.
- [ ] Tin is a gas that fills the gaps in the copper
    - *why wrong:* Tin is a solid metal; it sits within the lattice as differently-sized atoms.
- [ ] Bronze has fewer delocalised electrons than copper
    - *why wrong:* The number of electrons is not the reason — disrupting the layers is.

**Q8. [reason · CHTH]** Compare metallic bonding with ionic bonding in terms of the particles present and whether the solid conducts electricity.
- [✔︎] A metal has positive ions in a sea of delocalised electrons and conducts as a solid; an ionic solid has fixed positive and negative ions and does not conduct until molten or dissolved
- [ ] Both have delocalised electrons and both conduct as solids
    - *why wrong:* Ionic solids have no delocalised electrons and do not conduct as solids, so they are not the same.
- [ ] Both have fixed ions and neither conducts as a solid
    - *why wrong:* Metals DO conduct as solids (mobile electrons), so 'neither conducts' is wrong.
- [ ] A metal has positive and negative ions; an ionic solid has an electron sea
    - *why wrong:* This swaps them over: the electron sea is in the METAL; positive and negative ions are in the IONIC solid.

**Q9. [reason · CHTH]** Explain why metals can be drawn into wires (are ductile) without breaking.
- [✔︎] The layers of positive ions slide into new positions while the delocalised electron sea keeps them bonded, so the structure does not break
- [ ] The metallic bonds are weak, so the metal stretches easily
    - *why wrong:* The bonds are strong; ductility comes from the layers sliding while the electron sea maintains the bonding.
- [ ] The ions turn into a liquid as the wire is drawn
    - *why wrong:* The metal stays solid while being drawn into a wire.
- [ ] The electrons leave the metal, letting the ions move
    - *why wrong:* The electrons stay in the metal (that is what holds it together as it deforms).

**Q10. [reason · CHTH]** Copper is used for electrical wiring. Suggest two properties of copper that make it suitable, and link each to metallic bonding.
- [✔︎] It conducts electricity well (delocalised electrons carry charge) and it is ductile (layers of ions slide, so it can be drawn into wires)
- [ ] It is brittle (so it snaps to length) and it is an insulator (so it is safe)
    - *why wrong:* Brittleness and insulation would make copper useless for wiring — it is ductile and conductive.
- [ ] It has a low melting point (so it melts in use) and it is magnetic
    - *why wrong:* A low melting point would be a disadvantage in a wire, and copper's suitability is not due to magnetism.
- [ ] It is radioactive (so it carries current) and it is transparent
    - *why wrong:* Copper is neither radioactive nor transparent, and neither would help it carry current.

**Q11. [reason · TH]** Pure gold is soft, so jewellery is usually made from gold alloyed with copper. Explain, in terms of structure, why the alloy is harder than pure gold.
- [✔︎] The copper atoms are a different size to the gold atoms, so they distort the regular lattice and stop the layers of ions sliding, making the alloy harder
- [ ] The copper adds extra delocalised electrons that make stronger bonds
    - *why wrong:* The hardening is due to lattice distortion by differently-sized atoms, not extra electrons.
- [ ] Alloying removes impurities from the gold, hardening it
    - *why wrong:* Alloying ADDS a different element (it does not purify); that added, differently-sized atom is what hardens it.
- [ ] The copper forms covalent bonds with the gold
    - *why wrong:* Metals and alloys are held by metallic bonding, not covalent bonds.

**Q12. [reason · TH]** Explain why metals are described as having 'giant metallic structures', and how this links to their high melting points.
- [✔︎] A metal contains a huge number of positive ions and delocalised electrons with many strong attractions throughout, so a great deal of energy is needed to break them apart
- [ ] Each metal is a single giant molecule held by covalent bonds
    - *why wrong:* Metals have no covalent bonds; 'giant' refers to the vast lattice of ions and electrons.
- [ ] The word 'giant' means each metal atom is unusually large
    - *why wrong:* 'Giant' refers to the number of particles in the structure, not the size of one atom.
- [ ] Metals are giant because their ions are negative and repel over long distances
    - *why wrong:* Metal ions are positive, and they are attracted to (not repelled by) the electron sea.


---

## States of Matter and State Symbols  ·  `states-of-matter`  ·  AQA 5.2.2.1-5.2.2.2

> 🚩 **Triple-depth call (your review):** MATCHED — the particle model and state symbols (5.2.2.1-2) are identical for Combined and Triple. Foundation difficulty is the same across both pathways. Higher lift is genuine (heating-curve reasoning, limitations of the particle model). The audit's suggested upgrade — replacing the '(d) dissolved / (w)' filler — is done: the (aq) symbol is now tested inside an equation context, and the invented distractors are gone.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often think that melting or boiling a substance must be a chemical change because something clearly happens. It is a physical change: the particles gain or lose energy and rearrange, but the substance itself is unchanged — ice, water and steam are all H₂O. (Remember too that (aq) means dissolved in water specifically, not just any liquid.)

**Question sets by tier** (each item shows tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (5 recall / 5 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Ice melts to form water. State whether this is a physical or a chemical change, and explain your answer.
- [✔︎] A physical change — the substance is still H₂O; only the arrangement of the particles changes
- [ ] A chemical change — a new substance, water, is made from ice
    - *why wrong:* Ice and water are the same substance (H₂O) — water is not a new substance, just a different state.
- [ ] A chemical change — heating must have broken chemical bonds
    - *why wrong:* Melting only overcomes the forces between the water molecules; the covalent O–H bonds are not broken.
- [ ] Neither — melting is not classed as physical or chemical
    - *why wrong:* A change of state IS a physical change, because the composition of the substance does not change.

**Q2. [apply · CFCHTFTH]** Describe the arrangement and movement of the particles in a solid.
- [✔︎] Closely packed in a regular pattern, vibrating about fixed positions
- [ ] Closely packed but able to move around and flow past each other
    - *why wrong:* Particles that can move past each other and flow describes a LIQUID, not a solid.
- [ ] Far apart and moving quickly in all directions
    - *why wrong:* Particles far apart moving quickly describes a GAS.
- [ ] Arranged in long chains that slide over one another
    - *why wrong:* Sliding chains describe a polymer's structure, not the general particle model of a solid.

**Q3. [recall · CFCHTFTH]** Name the change of state that occurs when a liquid turns into a gas.
- [✔︎] Boiling (or evaporation)
- [ ] Condensation
    - *why wrong:* Condensation is the reverse — gas turning into liquid.
- [ ] Freezing
    - *why wrong:* Freezing is liquid turning into solid.
- [ ] Melting
    - *why wrong:* Melting is solid turning into liquid.

**Q4. [apply · CFCHTFTH]** In the equation NaCl(s) → Na⁺(?) + Cl⁻(?), state the symbol that shows the ions are dissolved in water.
- [✔︎] (aq)
- [ ] (l)
    - *why wrong:* (l) means a pure liquid, e.g. molten NaCl(l) or water H₂O(l) — not a substance dissolved in water.
- [ ] (s)
    - *why wrong:* (s) means solid; here the dissolved ions are free in solution, not a solid.
- [ ] (g)
    - *why wrong:* (g) means a gas; dissolved ions in water are not gaseous.

**Q5. [reason · CFCHTFTH]** Explain, in terms of particles, why a gas can be compressed but a solid cannot.
- [✔︎] A gas has large spaces between its particles that can be pushed closer together; a solid's particles are already touching
- [ ] A gas has heavier particles that squash more easily
    - *why wrong:* Particle mass does not control compressibility — the spacing between particles does.
- [ ] A solid has no particles, so there is nothing to compress
    - *why wrong:* A solid is made of particles too; they are just packed closely with no space to compress into.
- [ ] A gas is warmer, and warm things always compress
    - *why wrong:* Temperature is not the reason — it is the spacing of the particles.

**Q6. [recall · CFTF]** Name the three states of matter.
- [✔︎] Solid, liquid and gas
- [ ] Solid, powder and gas
    - *why wrong:* A powder is just a finely divided solid, not a separate state of matter.
- [ ] Ice, water and steam
    - *why wrong:* Ice, water and steam are the three states OF WATER specifically, not the general names.
- [ ] Element, compound and mixture
    - *why wrong:* Element, compound and mixture describe types of substance, not states of matter.

**Q7. [recall · CFTF]** State what happens to the particles of a solid when it melts.
- [✔︎] They gain energy and break free from their fixed positions so they can move past each other
- [ ] They lose energy and pack more tightly together
    - *why wrong:* Melting adds energy, so the particles move more, not less; they do not pack tighter.
- [ ] They are destroyed and new particles form
    - *why wrong:* Melting is a physical change — no particles are destroyed or created.
- [ ] They stop moving completely
    - *why wrong:* Particles move MORE when a solid melts, not less.

**Q8. [recall · CFTF]** Name the change of state from a gas to a liquid.
- [✔︎] Condensation
- [ ] Boiling
    - *why wrong:* Boiling is the reverse — liquid to gas.
- [ ] Sublimation
    - *why wrong:* Sublimation is solid changing directly to gas.
- [ ] Melting
    - *why wrong:* Melting is solid to liquid.

**Q9. [recall · CFTF]** State the state symbol used for a pure liquid.
- [✔︎] (l)
- [ ] (aq)
    - *why wrong:* (aq) means dissolved in water, not a pure liquid.
- [ ] (s)
    - *why wrong:* (s) means solid.
- [ ] (g)
    - *why wrong:* (g) means gas.

**Q10. [apply · CFTF]** Identify the state of matter in which the particles are far apart and move quickly in all directions.
- [✔︎] Gas
- [ ] Solid
    - *why wrong:* In a solid the particles are packed closely and only vibrate in fixed positions.
- [ ] Liquid
    - *why wrong:* In a liquid the particles are still close together, just able to flow.
- [ ] A dissolved solid
    - *why wrong:* A dissolved solid is spread through a liquid, but its particles are not far apart in a gas-like way.

### Combined Higher — 10 questions (1 recall / 9 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Ice melts to form water. State whether this is a physical or a chemical change, and explain your answer.
- [✔︎] A physical change — the substance is still H₂O; only the arrangement of the particles changes
- [ ] A chemical change — a new substance, water, is made from ice
    - *why wrong:* Ice and water are the same substance (H₂O) — water is not a new substance, just a different state.
- [ ] A chemical change — heating must have broken chemical bonds
    - *why wrong:* Melting only overcomes the forces between the water molecules; the covalent O–H bonds are not broken.
- [ ] Neither — melting is not classed as physical or chemical
    - *why wrong:* A change of state IS a physical change, because the composition of the substance does not change.

**Q2. [apply · CFCHTFTH]** Describe the arrangement and movement of the particles in a solid.
- [✔︎] Closely packed in a regular pattern, vibrating about fixed positions
- [ ] Closely packed but able to move around and flow past each other
    - *why wrong:* Particles that can move past each other and flow describes a LIQUID, not a solid.
- [ ] Far apart and moving quickly in all directions
    - *why wrong:* Particles far apart moving quickly describes a GAS.
- [ ] Arranged in long chains that slide over one another
    - *why wrong:* Sliding chains describe a polymer's structure, not the general particle model of a solid.

**Q3. [recall · CFCHTFTH]** Name the change of state that occurs when a liquid turns into a gas.
- [✔︎] Boiling (or evaporation)
- [ ] Condensation
    - *why wrong:* Condensation is the reverse — gas turning into liquid.
- [ ] Freezing
    - *why wrong:* Freezing is liquid turning into solid.
- [ ] Melting
    - *why wrong:* Melting is solid turning into liquid.

**Q4. [apply · CFCHTFTH]** In the equation NaCl(s) → Na⁺(?) + Cl⁻(?), state the symbol that shows the ions are dissolved in water.
- [✔︎] (aq)
- [ ] (l)
    - *why wrong:* (l) means a pure liquid, e.g. molten NaCl(l) or water H₂O(l) — not a substance dissolved in water.
- [ ] (s)
    - *why wrong:* (s) means solid; here the dissolved ions are free in solution, not a solid.
- [ ] (g)
    - *why wrong:* (g) means a gas; dissolved ions in water are not gaseous.

**Q5. [reason · CFCHTFTH]** Explain, in terms of particles, why a gas can be compressed but a solid cannot.
- [✔︎] A gas has large spaces between its particles that can be pushed closer together; a solid's particles are already touching
- [ ] A gas has heavier particles that squash more easily
    - *why wrong:* Particle mass does not control compressibility — the spacing between particles does.
- [ ] A solid has no particles, so there is nothing to compress
    - *why wrong:* A solid is made of particles too; they are just packed closely with no space to compress into.
- [ ] A gas is warmer, and warm things always compress
    - *why wrong:* Temperature is not the reason — it is the spacing of the particles.

**Q6. [reason · CHTH]** Explain, in terms of energy and forces, what happens to the particles when a liquid boils.
- [✔︎] The particles gain enough energy to overcome the forces holding them together and escape into the gas state
- [ ] The particles lose energy and move closer together
    - *why wrong:* Boiling adds energy — the particles move more and separate, they do not lose energy or move closer.
- [ ] The chemical bonds inside the particles break to release a gas
    - *why wrong:* Boiling overcomes the forces BETWEEN particles, not the bonds inside them (that would be a chemical change).
- [ ] The particles shrink so they can float away
    - *why wrong:* Particles do not shrink; they gain energy and move apart.

**Q7. [reason · CHTH]** As a pure solid is heated until it melts, its temperature stays constant during melting even though heating continues. Explain why.
- [✔︎] The energy supplied is used to overcome the forces between the particles (to change the state), rather than to raise the temperature
- [ ] The thermometer stops working at the melting point
    - *why wrong:* The thermometer works fine — the energy is going into the state change, not into heating.
- [ ] No energy is being supplied during melting
    - *why wrong:* Energy is still being supplied; it is being used to separate the particles.
- [ ] The particles stop absorbing energy once melting begins
    - *why wrong:* The particles keep absorbing energy — it is used to break the structure apart, not to warm it.

**Q8. [suggest · CHTH]** The particle model represents particles as small solid spheres. Suggest one limitation of this model.
- [✔︎] It treats particles as solid, identical spheres and ignores the forces between them (and their real shapes and sizes)
- [ ] It shows that particles move, which is incorrect
    - *why wrong:* Particles really do move — that part of the model is correct, so it is not a limitation.
- [ ] It proves that all substances are the same
    - *why wrong:* The model actually shows substances differ (different arrangements); it does not claim they are the same.
- [ ] It cannot be used to explain changes of state
    - *why wrong:* The model IS used to explain changes of state; that is one of its strengths.

**Q9. [reason · CHTH]** Explain why a change of state is classed as a physical change and not a chemical change.
- [✔︎] No new substance is made — the same particles are simply rearranged, and the change can be reversed
- [ ] A new substance is always produced, but it looks the same
    - *why wrong:* If a new substance were made it would be a chemical change; in a change of state the substance is unchanged.
- [ ] Chemical bonds within the particles are broken and remade
    - *why wrong:* The bonds inside the particles are not broken — only the forces between particles change.
- [ ] Energy is released, which defines a physical change
    - *why wrong:* Energy transfer alone does not define the type of change; whether a new substance forms does.

**Q10. [predict · CHTH]** Predict what happens to the water particles when steam condenses on a cold window, in terms of their energy and movement.
- [✔︎] They lose energy, slow down, and the forces between them pull them together into a liquid
- [ ] They gain energy and spread further apart
    - *why wrong:* Condensation removes energy — the particles slow down and come together, they do not gain energy or spread out.
- [ ] They turn into a new chemical substance
    - *why wrong:* Condensation is a physical change; steam and liquid water are the same substance.
- [ ] They break apart into hydrogen and oxygen
    - *why wrong:* The molecules stay as H₂O; the covalent bonds do not break.

### Triple Foundation — 12 questions (5 recall / 7 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Ice melts to form water. State whether this is a physical or a chemical change, and explain your answer.
- [✔︎] A physical change — the substance is still H₂O; only the arrangement of the particles changes
- [ ] A chemical change — a new substance, water, is made from ice
    - *why wrong:* Ice and water are the same substance (H₂O) — water is not a new substance, just a different state.
- [ ] A chemical change — heating must have broken chemical bonds
    - *why wrong:* Melting only overcomes the forces between the water molecules; the covalent O–H bonds are not broken.
- [ ] Neither — melting is not classed as physical or chemical
    - *why wrong:* A change of state IS a physical change, because the composition of the substance does not change.

**Q2. [apply · CFCHTFTH]** Describe the arrangement and movement of the particles in a solid.
- [✔︎] Closely packed in a regular pattern, vibrating about fixed positions
- [ ] Closely packed but able to move around and flow past each other
    - *why wrong:* Particles that can move past each other and flow describes a LIQUID, not a solid.
- [ ] Far apart and moving quickly in all directions
    - *why wrong:* Particles far apart moving quickly describes a GAS.
- [ ] Arranged in long chains that slide over one another
    - *why wrong:* Sliding chains describe a polymer's structure, not the general particle model of a solid.

**Q3. [recall · CFCHTFTH]** Name the change of state that occurs when a liquid turns into a gas.
- [✔︎] Boiling (or evaporation)
- [ ] Condensation
    - *why wrong:* Condensation is the reverse — gas turning into liquid.
- [ ] Freezing
    - *why wrong:* Freezing is liquid turning into solid.
- [ ] Melting
    - *why wrong:* Melting is solid turning into liquid.

**Q4. [apply · CFCHTFTH]** In the equation NaCl(s) → Na⁺(?) + Cl⁻(?), state the symbol that shows the ions are dissolved in water.
- [✔︎] (aq)
- [ ] (l)
    - *why wrong:* (l) means a pure liquid, e.g. molten NaCl(l) or water H₂O(l) — not a substance dissolved in water.
- [ ] (s)
    - *why wrong:* (s) means solid; here the dissolved ions are free in solution, not a solid.
- [ ] (g)
    - *why wrong:* (g) means a gas; dissolved ions in water are not gaseous.

**Q5. [reason · CFCHTFTH]** Explain, in terms of particles, why a gas can be compressed but a solid cannot.
- [✔︎] A gas has large spaces between its particles that can be pushed closer together; a solid's particles are already touching
- [ ] A gas has heavier particles that squash more easily
    - *why wrong:* Particle mass does not control compressibility — the spacing between particles does.
- [ ] A solid has no particles, so there is nothing to compress
    - *why wrong:* A solid is made of particles too; they are just packed closely with no space to compress into.
- [ ] A gas is warmer, and warm things always compress
    - *why wrong:* Temperature is not the reason — it is the spacing of the particles.

**Q6. [recall · CFTF]** Name the three states of matter.
- [✔︎] Solid, liquid and gas
- [ ] Solid, powder and gas
    - *why wrong:* A powder is just a finely divided solid, not a separate state of matter.
- [ ] Ice, water and steam
    - *why wrong:* Ice, water and steam are the three states OF WATER specifically, not the general names.
- [ ] Element, compound and mixture
    - *why wrong:* Element, compound and mixture describe types of substance, not states of matter.

**Q7. [recall · CFTF]** State what happens to the particles of a solid when it melts.
- [✔︎] They gain energy and break free from their fixed positions so they can move past each other
- [ ] They lose energy and pack more tightly together
    - *why wrong:* Melting adds energy, so the particles move more, not less; they do not pack tighter.
- [ ] They are destroyed and new particles form
    - *why wrong:* Melting is a physical change — no particles are destroyed or created.
- [ ] They stop moving completely
    - *why wrong:* Particles move MORE when a solid melts, not less.

**Q8. [recall · CFTF]** Name the change of state from a gas to a liquid.
- [✔︎] Condensation
- [ ] Boiling
    - *why wrong:* Boiling is the reverse — liquid to gas.
- [ ] Sublimation
    - *why wrong:* Sublimation is solid changing directly to gas.
- [ ] Melting
    - *why wrong:* Melting is solid to liquid.

**Q9. [recall · CFTF]** State the state symbol used for a pure liquid.
- [✔︎] (l)
- [ ] (aq)
    - *why wrong:* (aq) means dissolved in water, not a pure liquid.
- [ ] (s)
    - *why wrong:* (s) means solid.
- [ ] (g)
    - *why wrong:* (g) means gas.

**Q10. [apply · CFTF]** Identify the state of matter in which the particles are far apart and move quickly in all directions.
- [✔︎] Gas
- [ ] Solid
    - *why wrong:* In a solid the particles are packed closely and only vibrate in fixed positions.
- [ ] Liquid
    - *why wrong:* In a liquid the particles are still close together, just able to flow.
- [ ] A dissolved solid
    - *why wrong:* A dissolved solid is spread through a liquid, but its particles are not far apart in a gas-like way.

**Q11. [apply · TF]** Identify a pair of properties that describe a gas.
- [✔︎] It has no fixed shape and can be compressed
- [ ] It has a fixed shape and a fixed volume
    - *why wrong:* A fixed shape and fixed volume describe a solid.
- [ ] It has a fixed volume but no fixed shape
    - *why wrong:* A fixed volume but no fixed shape describes a liquid.
- [ ] It cannot be compressed at all
    - *why wrong:* Gases are easily compressed because of the large spaces between particles.

**Q12. [apply · TF]** Identify the correct set of state symbols for solid, liquid, gas and dissolved-in-water.
- [✔︎] (s), (l), (g), (aq)
- [ ] (so), (li), (ga), (aq)
    - *why wrong:* State symbols are single or double letters: (s), (l), (g), (aq) — not abbreviations like (so) or (li).
- [ ] (s), (l), (g), (w)
    - *why wrong:* There is no (w) symbol; 'dissolved in water' is shown by (aq).
- [ ] (s), (aq), (g), (l)
    - *why wrong:* This puts the symbols in the wrong order — (aq) is for dissolved, (l) for a pure liquid.

### Triple Higher — 12 questions (1 recall / 11 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Ice melts to form water. State whether this is a physical or a chemical change, and explain your answer.
- [✔︎] A physical change — the substance is still H₂O; only the arrangement of the particles changes
- [ ] A chemical change — a new substance, water, is made from ice
    - *why wrong:* Ice and water are the same substance (H₂O) — water is not a new substance, just a different state.
- [ ] A chemical change — heating must have broken chemical bonds
    - *why wrong:* Melting only overcomes the forces between the water molecules; the covalent O–H bonds are not broken.
- [ ] Neither — melting is not classed as physical or chemical
    - *why wrong:* A change of state IS a physical change, because the composition of the substance does not change.

**Q2. [apply · CFCHTFTH]** Describe the arrangement and movement of the particles in a solid.
- [✔︎] Closely packed in a regular pattern, vibrating about fixed positions
- [ ] Closely packed but able to move around and flow past each other
    - *why wrong:* Particles that can move past each other and flow describes a LIQUID, not a solid.
- [ ] Far apart and moving quickly in all directions
    - *why wrong:* Particles far apart moving quickly describes a GAS.
- [ ] Arranged in long chains that slide over one another
    - *why wrong:* Sliding chains describe a polymer's structure, not the general particle model of a solid.

**Q3. [recall · CFCHTFTH]** Name the change of state that occurs when a liquid turns into a gas.
- [✔︎] Boiling (or evaporation)
- [ ] Condensation
    - *why wrong:* Condensation is the reverse — gas turning into liquid.
- [ ] Freezing
    - *why wrong:* Freezing is liquid turning into solid.
- [ ] Melting
    - *why wrong:* Melting is solid turning into liquid.

**Q4. [apply · CFCHTFTH]** In the equation NaCl(s) → Na⁺(?) + Cl⁻(?), state the symbol that shows the ions are dissolved in water.
- [✔︎] (aq)
- [ ] (l)
    - *why wrong:* (l) means a pure liquid, e.g. molten NaCl(l) or water H₂O(l) — not a substance dissolved in water.
- [ ] (s)
    - *why wrong:* (s) means solid; here the dissolved ions are free in solution, not a solid.
- [ ] (g)
    - *why wrong:* (g) means a gas; dissolved ions in water are not gaseous.

**Q5. [reason · CFCHTFTH]** Explain, in terms of particles, why a gas can be compressed but a solid cannot.
- [✔︎] A gas has large spaces between its particles that can be pushed closer together; a solid's particles are already touching
- [ ] A gas has heavier particles that squash more easily
    - *why wrong:* Particle mass does not control compressibility — the spacing between particles does.
- [ ] A solid has no particles, so there is nothing to compress
    - *why wrong:* A solid is made of particles too; they are just packed closely with no space to compress into.
- [ ] A gas is warmer, and warm things always compress
    - *why wrong:* Temperature is not the reason — it is the spacing of the particles.

**Q6. [reason · CHTH]** Explain, in terms of energy and forces, what happens to the particles when a liquid boils.
- [✔︎] The particles gain enough energy to overcome the forces holding them together and escape into the gas state
- [ ] The particles lose energy and move closer together
    - *why wrong:* Boiling adds energy — the particles move more and separate, they do not lose energy or move closer.
- [ ] The chemical bonds inside the particles break to release a gas
    - *why wrong:* Boiling overcomes the forces BETWEEN particles, not the bonds inside them (that would be a chemical change).
- [ ] The particles shrink so they can float away
    - *why wrong:* Particles do not shrink; they gain energy and move apart.

**Q7. [reason · CHTH]** As a pure solid is heated until it melts, its temperature stays constant during melting even though heating continues. Explain why.
- [✔︎] The energy supplied is used to overcome the forces between the particles (to change the state), rather than to raise the temperature
- [ ] The thermometer stops working at the melting point
    - *why wrong:* The thermometer works fine — the energy is going into the state change, not into heating.
- [ ] No energy is being supplied during melting
    - *why wrong:* Energy is still being supplied; it is being used to separate the particles.
- [ ] The particles stop absorbing energy once melting begins
    - *why wrong:* The particles keep absorbing energy — it is used to break the structure apart, not to warm it.

**Q8. [suggest · CHTH]** The particle model represents particles as small solid spheres. Suggest one limitation of this model.
- [✔︎] It treats particles as solid, identical spheres and ignores the forces between them (and their real shapes and sizes)
- [ ] It shows that particles move, which is incorrect
    - *why wrong:* Particles really do move — that part of the model is correct, so it is not a limitation.
- [ ] It proves that all substances are the same
    - *why wrong:* The model actually shows substances differ (different arrangements); it does not claim they are the same.
- [ ] It cannot be used to explain changes of state
    - *why wrong:* The model IS used to explain changes of state; that is one of its strengths.

**Q9. [reason · CHTH]** Explain why a change of state is classed as a physical change and not a chemical change.
- [✔︎] No new substance is made — the same particles are simply rearranged, and the change can be reversed
- [ ] A new substance is always produced, but it looks the same
    - *why wrong:* If a new substance were made it would be a chemical change; in a change of state the substance is unchanged.
- [ ] Chemical bonds within the particles are broken and remade
    - *why wrong:* The bonds inside the particles are not broken — only the forces between particles change.
- [ ] Energy is released, which defines a physical change
    - *why wrong:* Energy transfer alone does not define the type of change; whether a new substance forms does.

**Q10. [predict · CHTH]** Predict what happens to the water particles when steam condenses on a cold window, in terms of their energy and movement.
- [✔︎] They lose energy, slow down, and the forces between them pull them together into a liquid
- [ ] They gain energy and spread further apart
    - *why wrong:* Condensation removes energy — the particles slow down and come together, they do not gain energy or spread out.
- [ ] They turn into a new chemical substance
    - *why wrong:* Condensation is a physical change; steam and liquid water are the same substance.
- [ ] They break apart into hydrogen and oxygen
    - *why wrong:* The molecules stay as H₂O; the covalent bonds do not break.

**Q11. [reason · TH]** On a graph of temperature against time, a solid is heated until it becomes a gas. Explain why the graph has two flat (horizontal) sections.
- [✔︎] Each flat section is a change of state (melting, then boiling), where the energy supplied overcomes forces between particles instead of raising the temperature
- [ ] The two flat sections show the substance cooling down twice
    - *why wrong:* The substance is being heated throughout, so it is not cooling.
- [ ] The flat sections show where the thermometer was broken
    - *why wrong:* The thermometer is fine — the energy is being used to change the state.
- [ ] The flat sections are where the substance stops absorbing any energy
    - *why wrong:* Energy is still absorbed during the flat sections; it goes into separating particles, not raising temperature.

**Q12. [reason · TH]** Explain why the simple particle model does not perfectly predict the properties of every substance.
- [✔︎] It assumes all particles are identical solid spheres and ignores the forces between them and their real sizes and shapes
- [ ] It assumes particles never move
    - *why wrong:* The model does include particle movement, so 'never move' is not the issue.
- [ ] It only works for gases and never for solids
    - *why wrong:* The model is applied to solids, liquids and gases — not only gases.
- [ ] It treats every substance as a chemical compound
    - *why wrong:* The model is about physical arrangement of particles, not about classifying substances as compounds.


---

## Structure and Properties of Ionic Compounds  ·  `properties-ionic-compounds`  ·  AQA 5.2.2.3

> 🚩 **Triple-depth call (your review):** MATCHED across pathways, but this page carries genuine HIGHER-tier depth (the ionic charge → force strength → melting-point comparisons). Those comparative items are flagged ⭐ for full review. Present in both Combined-Higher and Triple-Higher; no Combined/Triple divergence.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often say that ionic solutions conduct electricity because electrons flow through them, just like in a metal. They do not: ionic compounds have no free electrons. They conduct only when molten or dissolved, and it is the ions themselves that move and carry the charge. (This is also why ionic compounds are brittle rather than bendy — shifting the lattice brings like charges together, and they repel.)

**Question sets by tier** (each item shows tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (3 recall / 7 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** A student tests whether sodium chloride conducts electricity in four forms: solid, dissolved in water, molten, and as a vapour. Predict in which forms it conducts, and explain why.
- [✔︎] Dissolved in water and molten — in both the ions are free to move and carry charge
- [ ] Only as a solid — the lattice provides a path for the electrons
    - *why wrong:* Solid NaCl has ions but they are FIXED — they cannot move to carry charge, so it does not conduct as a solid.
- [ ] In all four forms — sodium chloride always contains ions
    - *why wrong:* Having ions is not enough; they must be free to move. In the solid (and vapour) they cannot carry a current.
- [ ] Only when dissolved — the water is what carries the current
    - *why wrong:* Molten NaCl also conducts — water is not required. Free ions from melting OR dissolving both allow conduction.

**Q2. [reason · CFCHTFTH]** Explain why ionic compounds conduct electricity when molten or dissolved, but not when solid.
- [✔︎] When molten or dissolved the ions are free to move and carry charge; in the solid they are held in fixed positions
- [ ] Melting or dissolving creates ions that were not there in the solid
    - *why wrong:* The ions already exist in the solid — melting or dissolving frees them to move, it does not create them.
- [ ] Molten ionic compounds conduct using delocalised electrons
    - *why wrong:* Ionic conduction is by moving IONS, not delocalised electrons (that is metals).
- [ ] Solid ionic compounds have no charged particles
    - *why wrong:* Solid ionic compounds do contain charged ions; they simply cannot move.

**Q3. [reason · CFCHTFTH]** Explain why ionic compounds have high melting and boiling points.
- [✔︎] There are many strong electrostatic attractions between the oppositely charged ions throughout the giant lattice, needing a lot of energy to overcome
- [ ] The crystals are large, so more heat is needed
    - *why wrong:* Crystal size does not set the melting point; the strength of the ionic bonding does.
- [ ] Strong covalent bonds throughout the lattice must be broken
    - *why wrong:* Ionic compounds have ionic bonds (ion-to-ion attraction), not covalent bonds.
- [ ] The ions are very heavy and resist heating
    - *why wrong:* Ion mass is not the reason; the strength of the electrostatic attraction is.

**Q4. [reason · CFCHTFTH]** Ionic compounds are hard but brittle. Explain why a crystal shatters when it is struck.
- [✔︎] The blow shifts a layer of ions so like charges line up next to each other; they repel and the crystal splits apart
- [ ] The covalent bonds in the crystal snap
    - *why wrong:* Ionic compounds contain no covalent bonds — they are held by ionic (electrostatic) attraction.
- [ ] The ions melt at the point of impact
    - *why wrong:* Shattering is caused by ion repulsion when layers shift, not by melting.
- [ ] The delocalised electrons are knocked out of place
    - *why wrong:* Ionic compounds have no delocalised electrons; that is a metallic feature.

**Q5. [apply · CFCHTFTH]** Describe the type of structure that is responsible for the properties of ionic compounds.
- [✔︎] A giant ionic lattice — a regular 3D arrangement of oppositely charged ions with strong electrostatic forces in all directions
- [ ] A small molecule of a few ions held weakly together
    - *why wrong:* Ionic compounds are giant lattices, not small molecules.
- [ ] A lattice of positive ions in a sea of delocalised electrons
    - *why wrong:* That is the metallic model; ionic compounds have positive AND negative ions, no electron sea.
- [ ] Long chains of ions joined by weak intermolecular forces
    - *why wrong:* That describes a polymer-like arrangement, not an ionic lattice.

**Q6. [recall · CFTF]** State whether ionic compounds are usually solids, liquids or gases at room temperature.
- [✔︎] Solids
- [ ] Liquids
    - *why wrong:* Their high melting points (strong lattice forces) mean they are solid at room temperature.
- [ ] Gases
    - *why wrong:* Ionic compounds have high melting points, so they are not liquids at room temperature.
- [ ] They are usually a mixture of all three
    - *why wrong:* They are solid at room temperature, not a mix of states.

**Q7. [recall · CFTF]** State two ways of making an ionic compound conduct electricity.
- [✔︎] Melt it, or dissolve it in water
- [ ] Cool it, or crush it into powder
    - *why wrong:* Cooling keeps the ions fixed; crushing a solid still leaves the ions unable to move.
- [ ] Keep it solid, or dissolve it
    - *why wrong:* A solid ionic compound does not conduct — only the dissolved (and molten) states do.
- [ ] Melt it, or keep it solid
    - *why wrong:* The solid state does not conduct; melting is one valid way, dissolving is the other.

**Q8. [recall · CFTF]** State whether ionic compounds are malleable or brittle.
- [✔︎] Brittle
- [ ] Malleable
    - *why wrong:* Malleability is a property of metals; ionic compounds shatter when struck.
- [ ] Both equally
    - *why wrong:* Ionic compounds are clearly brittle, not malleable.
- [ ] Neither — they are always liquid
    - *why wrong:* Ionic compounds are solid at room temperature, not liquid.

**Q9. [apply · CFTF]** Identify the reason solid ionic compounds do not conduct electricity.
- [✔︎] The ions are fixed in position in the lattice and cannot move
- [ ] There are no ions present in the solid
    - *why wrong:* The ions are present in the solid lattice; they simply cannot move.
- [ ] The ions have lost their charge
    - *why wrong:* The ions keep their charges in the solid.
- [ ] The solid contains only neutral molecules
    - *why wrong:* Ionic solids are made of charged ions, not neutral molecules.

**Q10. [apply · CFTF]** State what happens to the melting point of an ionic compound as the charges on its ions increase.
- [✔︎] It increases, because the electrostatic forces between the ions become stronger
- [ ] It decreases, because higher charges repel
    - *why wrong:* Higher charges give stronger attraction between the ions, not repulsion — melting point rises.
- [ ] It stays the same, because charge does not affect melting point
    - *why wrong:* Charge strongly affects melting point; higher charge → stronger forces → higher melting point.
- [ ] It becomes zero
    - *why wrong:* The melting point does not fall to zero; it rises with higher ionic charge.

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** A student tests whether sodium chloride conducts electricity in four forms: solid, dissolved in water, molten, and as a vapour. Predict in which forms it conducts, and explain why.
- [✔︎] Dissolved in water and molten — in both the ions are free to move and carry charge
- [ ] Only as a solid — the lattice provides a path for the electrons
    - *why wrong:* Solid NaCl has ions but they are FIXED — they cannot move to carry charge, so it does not conduct as a solid.
- [ ] In all four forms — sodium chloride always contains ions
    - *why wrong:* Having ions is not enough; they must be free to move. In the solid (and vapour) they cannot carry a current.
- [ ] Only when dissolved — the water is what carries the current
    - *why wrong:* Molten NaCl also conducts — water is not required. Free ions from melting OR dissolving both allow conduction.

**Q2. [reason · CFCHTFTH]** Explain why ionic compounds conduct electricity when molten or dissolved, but not when solid.
- [✔︎] When molten or dissolved the ions are free to move and carry charge; in the solid they are held in fixed positions
- [ ] Melting or dissolving creates ions that were not there in the solid
    - *why wrong:* The ions already exist in the solid — melting or dissolving frees them to move, it does not create them.
- [ ] Molten ionic compounds conduct using delocalised electrons
    - *why wrong:* Ionic conduction is by moving IONS, not delocalised electrons (that is metals).
- [ ] Solid ionic compounds have no charged particles
    - *why wrong:* Solid ionic compounds do contain charged ions; they simply cannot move.

**Q3. [reason · CFCHTFTH]** Explain why ionic compounds have high melting and boiling points.
- [✔︎] There are many strong electrostatic attractions between the oppositely charged ions throughout the giant lattice, needing a lot of energy to overcome
- [ ] The crystals are large, so more heat is needed
    - *why wrong:* Crystal size does not set the melting point; the strength of the ionic bonding does.
- [ ] Strong covalent bonds throughout the lattice must be broken
    - *why wrong:* Ionic compounds have ionic bonds (ion-to-ion attraction), not covalent bonds.
- [ ] The ions are very heavy and resist heating
    - *why wrong:* Ion mass is not the reason; the strength of the electrostatic attraction is.

**Q4. [reason · CFCHTFTH]** Ionic compounds are hard but brittle. Explain why a crystal shatters when it is struck.
- [✔︎] The blow shifts a layer of ions so like charges line up next to each other; they repel and the crystal splits apart
- [ ] The covalent bonds in the crystal snap
    - *why wrong:* Ionic compounds contain no covalent bonds — they are held by ionic (electrostatic) attraction.
- [ ] The ions melt at the point of impact
    - *why wrong:* Shattering is caused by ion repulsion when layers shift, not by melting.
- [ ] The delocalised electrons are knocked out of place
    - *why wrong:* Ionic compounds have no delocalised electrons; that is a metallic feature.

**Q5. [apply · CFCHTFTH]** Describe the type of structure that is responsible for the properties of ionic compounds.
- [✔︎] A giant ionic lattice — a regular 3D arrangement of oppositely charged ions with strong electrostatic forces in all directions
- [ ] A small molecule of a few ions held weakly together
    - *why wrong:* Ionic compounds are giant lattices, not small molecules.
- [ ] A lattice of positive ions in a sea of delocalised electrons
    - *why wrong:* That is the metallic model; ionic compounds have positive AND negative ions, no electron sea.
- [ ] Long chains of ions joined by weak intermolecular forces
    - *why wrong:* That describes a polymer-like arrangement, not an ionic lattice.

**Q6. [reason · CHTH] ⭐** Magnesium oxide (MgO) has a higher melting point than sodium chloride (NaCl). Explain why.
- [✔︎] Mg²⁺ and O²⁻ carry 2+/2− charges, larger than the 1+/1− of Na⁺ and Cl⁻, so the electrostatic forces between the ions are stronger and need more energy to overcome
- [ ] Magnesium oxide has a larger crystal lattice, so more energy is needed
    - *why wrong:* Crystal size is not the determining factor — both are giant lattices; the strength of each ion-ion attraction matters.
- [ ] Magnesium oxide has more ions per formula unit than sodium chloride
    - *why wrong:* Both MgO and NaCl are 1:1 — neither has more ions per formula unit.
- [ ] Magnesium is heavier than sodium, which raises the melting point
    - *why wrong:* Atomic mass does not set the melting point; the ionic charge does.
  > 🚩 **Reviewer note:** Core HT charge → force → melting-point reasoning. Please full-review.

**Q7. [reason · CHTH]** Explain the difference between how a metal conducts electricity and how molten sodium chloride conducts electricity.
- [✔︎] A metal conducts using delocalised electrons that move; molten sodium chloride conducts using its ions that move
- [ ] Both conduct using delocalised electrons
    - *why wrong:* Only the metal uses delocalised electrons; molten NaCl uses moving ions, not electrons.
- [ ] Both conduct using moving ions
    - *why wrong:* The metal does not conduct by moving ions — its ions are fixed; the electrons move.
- [ ] A metal conducts using ions; molten sodium chloride uses electrons
    - *why wrong:* This swaps them over: metals use electrons, molten ionic compounds use ions.

**Q8. [reason · CHTH] ⭐** Predict which has the higher melting point, sodium chloride (NaCl) or sodium oxide (Na₂O), and justify your answer using ionic charge.
- [✔︎] Sodium oxide — its O²⁻ ions carry a 2− charge compared with Cl⁻ at 1−, giving stronger forces and a higher melting point
- [ ] Sodium chloride — because it contains chlorine, which is heavier than oxygen
    - *why wrong:* Atomic mass is not the key factor; the O²⁻ charge (2−) creates stronger attraction than Cl⁻ (1−).
- [ ] They are equal, because both contain sodium ions
    - *why wrong:* Having the same positive ion does not make the melting points equal — the negative ion's charge differs.
- [ ] Sodium oxide — because it has more atoms in its formula
    - *why wrong:* The higher melting point comes from the higher ionic charge (O²⁻), not simply from more atoms.
  > 🚩 **Reviewer note:** Comparative charge reasoning (1− vs 2− anion). Please full-review.

**Q9. [reason · CHTH]** Explain why the melting point of an ionic compound gives information about the strength of the forces between its ions.
- [✔︎] A higher melting point means more energy is needed to separate the ions, which shows the electrostatic forces holding them are stronger
- [ ] A higher melting point means the ions are lighter
    - *why wrong:* Ion mass is not what the melting point reveals; it reflects the strength of the attraction.
- [ ] The melting point depends only on the size of the crystal
    - *why wrong:* Crystal size does not set the melting point; the strength of the ionic forces does.
- [ ] The melting point is unrelated to the forces between ions
    - *why wrong:* The melting point is directly linked to the strength of the forces between the ions.

**Q10. [suggest · CHTH] ⭐** Suggest why magnesium oxide is used to line the inside of furnaces.
- [✔︎] Its 2+/2− ions give very strong ionic bonding and a very high melting point, so it can withstand the high temperatures without melting
- [ ] It is a good electrical conductor when solid
    - *why wrong:* Solid MgO does not conduct electricity (fixed ions); that is not why it is used to line furnaces.
- [ ] It has a low melting point, so it melts to seal the furnace
    - *why wrong:* A low melting point would be useless in a furnace; MgO is chosen for its VERY HIGH melting point.
- [ ] It is a soft, flexible material that absorbs heat
    - *why wrong:* MgO is hard and brittle, not soft and flexible; it is chosen for heat resistance.
  > 🚩 **Reviewer note:** Applies charge → high-melting-point reasoning to a context. Please full-review.

### Triple Foundation — 12 questions (4 recall / 8 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** A student tests whether sodium chloride conducts electricity in four forms: solid, dissolved in water, molten, and as a vapour. Predict in which forms it conducts, and explain why.
- [✔︎] Dissolved in water and molten — in both the ions are free to move and carry charge
- [ ] Only as a solid — the lattice provides a path for the electrons
    - *why wrong:* Solid NaCl has ions but they are FIXED — they cannot move to carry charge, so it does not conduct as a solid.
- [ ] In all four forms — sodium chloride always contains ions
    - *why wrong:* Having ions is not enough; they must be free to move. In the solid (and vapour) they cannot carry a current.
- [ ] Only when dissolved — the water is what carries the current
    - *why wrong:* Molten NaCl also conducts — water is not required. Free ions from melting OR dissolving both allow conduction.

**Q2. [reason · CFCHTFTH]** Explain why ionic compounds conduct electricity when molten or dissolved, but not when solid.
- [✔︎] When molten or dissolved the ions are free to move and carry charge; in the solid they are held in fixed positions
- [ ] Melting or dissolving creates ions that were not there in the solid
    - *why wrong:* The ions already exist in the solid — melting or dissolving frees them to move, it does not create them.
- [ ] Molten ionic compounds conduct using delocalised electrons
    - *why wrong:* Ionic conduction is by moving IONS, not delocalised electrons (that is metals).
- [ ] Solid ionic compounds have no charged particles
    - *why wrong:* Solid ionic compounds do contain charged ions; they simply cannot move.

**Q3. [reason · CFCHTFTH]** Explain why ionic compounds have high melting and boiling points.
- [✔︎] There are many strong electrostatic attractions between the oppositely charged ions throughout the giant lattice, needing a lot of energy to overcome
- [ ] The crystals are large, so more heat is needed
    - *why wrong:* Crystal size does not set the melting point; the strength of the ionic bonding does.
- [ ] Strong covalent bonds throughout the lattice must be broken
    - *why wrong:* Ionic compounds have ionic bonds (ion-to-ion attraction), not covalent bonds.
- [ ] The ions are very heavy and resist heating
    - *why wrong:* Ion mass is not the reason; the strength of the electrostatic attraction is.

**Q4. [reason · CFCHTFTH]** Ionic compounds are hard but brittle. Explain why a crystal shatters when it is struck.
- [✔︎] The blow shifts a layer of ions so like charges line up next to each other; they repel and the crystal splits apart
- [ ] The covalent bonds in the crystal snap
    - *why wrong:* Ionic compounds contain no covalent bonds — they are held by ionic (electrostatic) attraction.
- [ ] The ions melt at the point of impact
    - *why wrong:* Shattering is caused by ion repulsion when layers shift, not by melting.
- [ ] The delocalised electrons are knocked out of place
    - *why wrong:* Ionic compounds have no delocalised electrons; that is a metallic feature.

**Q5. [apply · CFCHTFTH]** Describe the type of structure that is responsible for the properties of ionic compounds.
- [✔︎] A giant ionic lattice — a regular 3D arrangement of oppositely charged ions with strong electrostatic forces in all directions
- [ ] A small molecule of a few ions held weakly together
    - *why wrong:* Ionic compounds are giant lattices, not small molecules.
- [ ] A lattice of positive ions in a sea of delocalised electrons
    - *why wrong:* That is the metallic model; ionic compounds have positive AND negative ions, no electron sea.
- [ ] Long chains of ions joined by weak intermolecular forces
    - *why wrong:* That describes a polymer-like arrangement, not an ionic lattice.

**Q6. [recall · CFTF]** State whether ionic compounds are usually solids, liquids or gases at room temperature.
- [✔︎] Solids
- [ ] Liquids
    - *why wrong:* Their high melting points (strong lattice forces) mean they are solid at room temperature.
- [ ] Gases
    - *why wrong:* Ionic compounds have high melting points, so they are not liquids at room temperature.
- [ ] They are usually a mixture of all three
    - *why wrong:* They are solid at room temperature, not a mix of states.

**Q7. [recall · CFTF]** State two ways of making an ionic compound conduct electricity.
- [✔︎] Melt it, or dissolve it in water
- [ ] Cool it, or crush it into powder
    - *why wrong:* Cooling keeps the ions fixed; crushing a solid still leaves the ions unable to move.
- [ ] Keep it solid, or dissolve it
    - *why wrong:* A solid ionic compound does not conduct — only the dissolved (and molten) states do.
- [ ] Melt it, or keep it solid
    - *why wrong:* The solid state does not conduct; melting is one valid way, dissolving is the other.

**Q8. [recall · CFTF]** State whether ionic compounds are malleable or brittle.
- [✔︎] Brittle
- [ ] Malleable
    - *why wrong:* Malleability is a property of metals; ionic compounds shatter when struck.
- [ ] Both equally
    - *why wrong:* Ionic compounds are clearly brittle, not malleable.
- [ ] Neither — they are always liquid
    - *why wrong:* Ionic compounds are solid at room temperature, not liquid.

**Q9. [apply · CFTF]** Identify the reason solid ionic compounds do not conduct electricity.
- [✔︎] The ions are fixed in position in the lattice and cannot move
- [ ] There are no ions present in the solid
    - *why wrong:* The ions are present in the solid lattice; they simply cannot move.
- [ ] The ions have lost their charge
    - *why wrong:* The ions keep their charges in the solid.
- [ ] The solid contains only neutral molecules
    - *why wrong:* Ionic solids are made of charged ions, not neutral molecules.

**Q10. [apply · CFTF]** State what happens to the melting point of an ionic compound as the charges on its ions increase.
- [✔︎] It increases, because the electrostatic forces between the ions become stronger
- [ ] It decreases, because higher charges repel
    - *why wrong:* Higher charges give stronger attraction between the ions, not repulsion — melting point rises.
- [ ] It stays the same, because charge does not affect melting point
    - *why wrong:* Charge strongly affects melting point; higher charge → stronger forces → higher melting point.
- [ ] It becomes zero
    - *why wrong:* The melting point does not fall to zero; it rises with higher ionic charge.

**Q11. [recall · TF]** State the name of the structure that ionic compounds form.
- [✔︎] A giant ionic lattice
- [ ] A simple molecule
    - *why wrong:* Ionic compounds are giant lattices, not small molecules.
- [ ] A metallic lattice
    - *why wrong:* A metallic lattice has positive ions and delocalised electrons, not positive and negative ions.
- [ ] A polymer chain
    - *why wrong:* Polymer chains are covalent, molecular structures, not ionic.

**Q12. [apply · TF]** Identify what allows a molten ionic compound to conduct electricity.
- [✔︎] The ions become free to move and carry charge
- [ ] Delocalised electrons are released
    - *why wrong:* Ionic compounds have no delocalised electrons; conduction is by moving ions.
- [ ] The compound turns into a metal
    - *why wrong:* Melting an ionic compound frees its ions; it does not turn it into a metal.
- [ ] The covalent bonds break to release electrons
    - *why wrong:* Ionic compounds have no covalent bonds to break.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** A student tests whether sodium chloride conducts electricity in four forms: solid, dissolved in water, molten, and as a vapour. Predict in which forms it conducts, and explain why.
- [✔︎] Dissolved in water and molten — in both the ions are free to move and carry charge
- [ ] Only as a solid — the lattice provides a path for the electrons
    - *why wrong:* Solid NaCl has ions but they are FIXED — they cannot move to carry charge, so it does not conduct as a solid.
- [ ] In all four forms — sodium chloride always contains ions
    - *why wrong:* Having ions is not enough; they must be free to move. In the solid (and vapour) they cannot carry a current.
- [ ] Only when dissolved — the water is what carries the current
    - *why wrong:* Molten NaCl also conducts — water is not required. Free ions from melting OR dissolving both allow conduction.

**Q2. [reason · CFCHTFTH]** Explain why ionic compounds conduct electricity when molten or dissolved, but not when solid.
- [✔︎] When molten or dissolved the ions are free to move and carry charge; in the solid they are held in fixed positions
- [ ] Melting or dissolving creates ions that were not there in the solid
    - *why wrong:* The ions already exist in the solid — melting or dissolving frees them to move, it does not create them.
- [ ] Molten ionic compounds conduct using delocalised electrons
    - *why wrong:* Ionic conduction is by moving IONS, not delocalised electrons (that is metals).
- [ ] Solid ionic compounds have no charged particles
    - *why wrong:* Solid ionic compounds do contain charged ions; they simply cannot move.

**Q3. [reason · CFCHTFTH]** Explain why ionic compounds have high melting and boiling points.
- [✔︎] There are many strong electrostatic attractions between the oppositely charged ions throughout the giant lattice, needing a lot of energy to overcome
- [ ] The crystals are large, so more heat is needed
    - *why wrong:* Crystal size does not set the melting point; the strength of the ionic bonding does.
- [ ] Strong covalent bonds throughout the lattice must be broken
    - *why wrong:* Ionic compounds have ionic bonds (ion-to-ion attraction), not covalent bonds.
- [ ] The ions are very heavy and resist heating
    - *why wrong:* Ion mass is not the reason; the strength of the electrostatic attraction is.

**Q4. [reason · CFCHTFTH]** Ionic compounds are hard but brittle. Explain why a crystal shatters when it is struck.
- [✔︎] The blow shifts a layer of ions so like charges line up next to each other; they repel and the crystal splits apart
- [ ] The covalent bonds in the crystal snap
    - *why wrong:* Ionic compounds contain no covalent bonds — they are held by ionic (electrostatic) attraction.
- [ ] The ions melt at the point of impact
    - *why wrong:* Shattering is caused by ion repulsion when layers shift, not by melting.
- [ ] The delocalised electrons are knocked out of place
    - *why wrong:* Ionic compounds have no delocalised electrons; that is a metallic feature.

**Q5. [apply · CFCHTFTH]** Describe the type of structure that is responsible for the properties of ionic compounds.
- [✔︎] A giant ionic lattice — a regular 3D arrangement of oppositely charged ions with strong electrostatic forces in all directions
- [ ] A small molecule of a few ions held weakly together
    - *why wrong:* Ionic compounds are giant lattices, not small molecules.
- [ ] A lattice of positive ions in a sea of delocalised electrons
    - *why wrong:* That is the metallic model; ionic compounds have positive AND negative ions, no electron sea.
- [ ] Long chains of ions joined by weak intermolecular forces
    - *why wrong:* That describes a polymer-like arrangement, not an ionic lattice.

**Q6. [reason · CHTH] ⭐** Magnesium oxide (MgO) has a higher melting point than sodium chloride (NaCl). Explain why.
- [✔︎] Mg²⁺ and O²⁻ carry 2+/2− charges, larger than the 1+/1− of Na⁺ and Cl⁻, so the electrostatic forces between the ions are stronger and need more energy to overcome
- [ ] Magnesium oxide has a larger crystal lattice, so more energy is needed
    - *why wrong:* Crystal size is not the determining factor — both are giant lattices; the strength of each ion-ion attraction matters.
- [ ] Magnesium oxide has more ions per formula unit than sodium chloride
    - *why wrong:* Both MgO and NaCl are 1:1 — neither has more ions per formula unit.
- [ ] Magnesium is heavier than sodium, which raises the melting point
    - *why wrong:* Atomic mass does not set the melting point; the ionic charge does.
  > 🚩 **Reviewer note:** Core HT charge → force → melting-point reasoning. Please full-review.

**Q7. [reason · CHTH]** Explain the difference between how a metal conducts electricity and how molten sodium chloride conducts electricity.
- [✔︎] A metal conducts using delocalised electrons that move; molten sodium chloride conducts using its ions that move
- [ ] Both conduct using delocalised electrons
    - *why wrong:* Only the metal uses delocalised electrons; molten NaCl uses moving ions, not electrons.
- [ ] Both conduct using moving ions
    - *why wrong:* The metal does not conduct by moving ions — its ions are fixed; the electrons move.
- [ ] A metal conducts using ions; molten sodium chloride uses electrons
    - *why wrong:* This swaps them over: metals use electrons, molten ionic compounds use ions.

**Q8. [reason · CHTH] ⭐** Predict which has the higher melting point, sodium chloride (NaCl) or sodium oxide (Na₂O), and justify your answer using ionic charge.
- [✔︎] Sodium oxide — its O²⁻ ions carry a 2− charge compared with Cl⁻ at 1−, giving stronger forces and a higher melting point
- [ ] Sodium chloride — because it contains chlorine, which is heavier than oxygen
    - *why wrong:* Atomic mass is not the key factor; the O²⁻ charge (2−) creates stronger attraction than Cl⁻ (1−).
- [ ] They are equal, because both contain sodium ions
    - *why wrong:* Having the same positive ion does not make the melting points equal — the negative ion's charge differs.
- [ ] Sodium oxide — because it has more atoms in its formula
    - *why wrong:* The higher melting point comes from the higher ionic charge (O²⁻), not simply from more atoms.
  > 🚩 **Reviewer note:** Comparative charge reasoning (1− vs 2− anion). Please full-review.

**Q9. [reason · CHTH]** Explain why the melting point of an ionic compound gives information about the strength of the forces between its ions.
- [✔︎] A higher melting point means more energy is needed to separate the ions, which shows the electrostatic forces holding them are stronger
- [ ] A higher melting point means the ions are lighter
    - *why wrong:* Ion mass is not what the melting point reveals; it reflects the strength of the attraction.
- [ ] The melting point depends only on the size of the crystal
    - *why wrong:* Crystal size does not set the melting point; the strength of the ionic forces does.
- [ ] The melting point is unrelated to the forces between ions
    - *why wrong:* The melting point is directly linked to the strength of the forces between the ions.

**Q10. [suggest · CHTH] ⭐** Suggest why magnesium oxide is used to line the inside of furnaces.
- [✔︎] Its 2+/2− ions give very strong ionic bonding and a very high melting point, so it can withstand the high temperatures without melting
- [ ] It is a good electrical conductor when solid
    - *why wrong:* Solid MgO does not conduct electricity (fixed ions); that is not why it is used to line furnaces.
- [ ] It has a low melting point, so it melts to seal the furnace
    - *why wrong:* A low melting point would be useless in a furnace; MgO is chosen for its VERY HIGH melting point.
- [ ] It is a soft, flexible material that absorbs heat
    - *why wrong:* MgO is hard and brittle, not soft and flexible; it is chosen for heat resistance.
  > 🚩 **Reviewer note:** Applies charge → high-melting-point reasoning to a context. Please full-review.

**Q11. [reason · TH] ⭐** Aluminium oxide (Al₂O₃) has a very high melting point. Explain, in terms of ionic charge, why it is higher than that of sodium chloride.
- [✔︎] Al³⁺ and O²⁻ carry high charges (3+ and 2−), giving very strong electrostatic forces that need a great deal of energy to overcome — far more than NaCl's 1+/1−
- [ ] Aluminium oxide has smaller ions, which always melt at higher temperatures
    - *why wrong:* Ion size has a smaller effect than charge; the 3+/2− charges are the main reason for the very high melting point.
- [ ] Aluminium oxide is a covalent compound with strong bonds
    - *why wrong:* Aluminium oxide is ionic (metal + non-metal), not covalent.
- [ ] Aluminium is a metal, so aluminium oxide conducts and melts easily
    - *why wrong:* Aluminium oxide is an ionic compound with a very HIGH melting point, and it does not conduct as a solid.
  > 🚩 **Reviewer note:** Extends charge reasoning to a 3+ ion. Please full-review.

**Q12. [reason · TH]** Explain why the ability of a molten ionic compound to conduct electricity depends on its ions acting as charge carriers.
- [✔︎] A current is a flow of charge; in a molten ionic compound the mobile ions carry that charge, so conduction only happens when the ions are free to move
- [ ] The ions carry charge only when they are fixed in place
    - *why wrong:* Fixed ions cannot carry charge; they must be free to move, which happens when the compound is molten.
- [ ] Electrons in the ions carry the charge whether the compound is solid or molten
    - *why wrong:* Ionic conduction is by moving ions, not by electrons, and only when the ions can move.
- [ ] The compound conducts because heat, not moving charge, carries the current
    - *why wrong:* Electrical current is a flow of charge (moving ions here), not simply heat.


---

## Structure and Properties of Small Molecules  ·  `properties-small-molecules`  ·  AQA 5.2.2.4

> 🚩 **Triple-depth call (your review):** MATCHED — AQA 5.2.2.4 is identical for Combined and Triple. Foundation difficulty is the same across both pathways. Higher lift is the intermolecular-forces-increase-with-size reasoning. No AQA Triple-only content on this page.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often say that simple molecular substances melt easily because their covalent bonds are weak. The covalent bonds inside each molecule are actually strong. What is weak are the intermolecular forces BETWEEN the separate molecules — melting or boiling overcomes those and leaves the covalent bonds untouched, which is why the melting point is low.

**Question sets by tier** (each item shows tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (3 recall / 7 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Water (H₂O) boils at 100°C but methane (CH₄) boils at −161°C, although both are simple molecular. Explain why the difference is so large.
- [✔︎] Water molecules have stronger intermolecular forces than methane molecules, so more energy is needed to separate them
- [ ] Water has more covalent bonds, so it takes more energy to break them
    - *why wrong:* Boiling does not break covalent bonds — water has 2 and methane has 4, so bond count is not the reason.
- [ ] Methane is lighter, so it simply evaporates faster
    - *why wrong:* Lighter molecules can evaporate faster, but boiling point is set by the strength of the intermolecular forces.
- [ ] Water contains oxygen, which makes the molecules too heavy to boil easily
    - *why wrong:* The key reason is the stronger intermolecular forces in water, not simply the mass of the molecules.

**Q2. [reason · CFCHTFTH]** Explain why simple molecular substances do not conduct electricity.
- [✔︎] They have no free electrons or ions — there are no charged particles that can move to carry a current
- [ ] Their covalent bonds are too strong to let electrons move
    - *why wrong:* Conduction needs free charged particles, not weaker bonds — even weak bonds would not help without free charges.
- [ ] Their molecules are too small to hold a charge
    - *why wrong:* Molecular size is not the point; metals are large structures and conduct because of free electrons.
- [ ] Simple molecules are always gases, and gases never conduct
    - *why wrong:* Some gases can conduct (e.g. when ionised), and simple molecular substances can be solids or liquids too.

**Q3. [reason · CFCHTFTH]** Explain why simple molecular substances have low melting and boiling points.
- [✔︎] The forces between the molecules (intermolecular forces) are weak, so only a little energy is needed to separate them
- [ ] The covalent bonds within the molecules are very weak
    - *why wrong:* The covalent bonds within molecules are strong; it is the forces between molecules that are weak.
- [ ] The molecules lose electrons easily when warmed
    - *why wrong:* No electrons are lost on melting; the weak intermolecular forces are simply overcome.
- [ ] There are no forces at all between the molecules
    - *why wrong:* There ARE forces between molecules (intermolecular forces) — they are just weak.

**Q4. [apply · CFCHTFTH]** State what is overcome when a simple molecular substance boils.
- [✔︎] The weak intermolecular forces between the molecules
- [ ] The strong covalent bonds within the molecules
    - *why wrong:* The strong covalent bonds inside the molecules are NOT broken on boiling.
- [ ] The ionic bonds between the molecules
    - *why wrong:* Simple molecular substances contain no ionic bonds.
- [ ] The metallic bonds holding the molecules together
    - *why wrong:* There are no metallic bonds in a simple molecular substance.

**Q5. [apply · CFCHTFTH]** Describe what a simple molecular substance is.
- [✔︎] A substance made of small molecules, each with a fixed number of atoms joined by strong covalent bonds
- [ ] A giant lattice of ions held by electrostatic forces
    - *why wrong:* A giant ionic lattice describes an ionic compound, not a simple molecular substance.
- [ ] A giant structure of atoms all joined by covalent bonds
    - *why wrong:* A giant covalent structure (like diamond) is different — its covalent bonds run throughout, with no small molecules.
- [ ] A metal made of positive ions in a sea of electrons
    - *why wrong:* That describes a metal, not a molecular substance.

**Q6. [recall · CFTF]** State whether simple molecular substances have high or low melting points.
- [✔︎] Low
- [ ] High
    - *why wrong:* Simple molecular substances have LOW melting points because of weak intermolecular forces.
- [ ] Always exactly 100°C
    - *why wrong:* 100°C is the boiling point of water specifically, not a general rule.
- [ ] They never melt
    - *why wrong:* They do melt — easily, in fact, at low temperatures.

**Q7. [recall · CFTF]** State whether simple molecular substances conduct electricity.
- [✔︎] No
- [ ] Yes, always
    - *why wrong:* They have no free charged particles, so they do not conduct.
- [ ] Only when solid
    - *why wrong:* They do not conduct in any state (no free electrons or ions).
- [ ] Only as a metal
    - *why wrong:* Simple molecular substances are not metals and do not conduct.

**Q8. [recall · CFTF]** Name the type of force that must be overcome to melt a simple molecular substance.
- [✔︎] Intermolecular forces
- [ ] Covalent bonds
    - *why wrong:* Covalent bonds are within molecules and are not broken on melting.
- [ ] Ionic bonds
    - *why wrong:* There are no ionic bonds in a simple molecular substance.
- [ ] Metallic bonds
    - *why wrong:* There are no metallic bonds in a simple molecular substance.

**Q9. [apply · CFTF]** Identify which of these is a simple molecular substance.
- [✔︎] Carbon dioxide
- [ ] Sodium chloride
    - *why wrong:* Sodium chloride is a giant ionic lattice, not a simple molecule.
- [ ] Copper
    - *why wrong:* Copper is a metal with a giant metallic structure.
- [ ] Diamond
    - *why wrong:* Diamond is a giant covalent structure, not a simple molecule.

**Q10. [apply · CFTF]** State whether the covalent bonds inside the molecules break when a simple molecular substance melts.
- [✔︎] No — only the forces between the molecules are overcome
- [ ] Yes — the covalent bonds break to let it melt
    - *why wrong:* The strong covalent bonds stay intact; melting overcomes the weak forces between molecules.
- [ ] Yes — half of the covalent bonds break
    - *why wrong:* No covalent bonds break on melting, not even some of them.
- [ ] Only if the substance is heated very slowly
    - *why wrong:* The heating rate does not change which forces are overcome; the covalent bonds stay intact.

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Water (H₂O) boils at 100°C but methane (CH₄) boils at −161°C, although both are simple molecular. Explain why the difference is so large.
- [✔︎] Water molecules have stronger intermolecular forces than methane molecules, so more energy is needed to separate them
- [ ] Water has more covalent bonds, so it takes more energy to break them
    - *why wrong:* Boiling does not break covalent bonds — water has 2 and methane has 4, so bond count is not the reason.
- [ ] Methane is lighter, so it simply evaporates faster
    - *why wrong:* Lighter molecules can evaporate faster, but boiling point is set by the strength of the intermolecular forces.
- [ ] Water contains oxygen, which makes the molecules too heavy to boil easily
    - *why wrong:* The key reason is the stronger intermolecular forces in water, not simply the mass of the molecules.

**Q2. [reason · CFCHTFTH]** Explain why simple molecular substances do not conduct electricity.
- [✔︎] They have no free electrons or ions — there are no charged particles that can move to carry a current
- [ ] Their covalent bonds are too strong to let electrons move
    - *why wrong:* Conduction needs free charged particles, not weaker bonds — even weak bonds would not help without free charges.
- [ ] Their molecules are too small to hold a charge
    - *why wrong:* Molecular size is not the point; metals are large structures and conduct because of free electrons.
- [ ] Simple molecules are always gases, and gases never conduct
    - *why wrong:* Some gases can conduct (e.g. when ionised), and simple molecular substances can be solids or liquids too.

**Q3. [reason · CFCHTFTH]** Explain why simple molecular substances have low melting and boiling points.
- [✔︎] The forces between the molecules (intermolecular forces) are weak, so only a little energy is needed to separate them
- [ ] The covalent bonds within the molecules are very weak
    - *why wrong:* The covalent bonds within molecules are strong; it is the forces between molecules that are weak.
- [ ] The molecules lose electrons easily when warmed
    - *why wrong:* No electrons are lost on melting; the weak intermolecular forces are simply overcome.
- [ ] There are no forces at all between the molecules
    - *why wrong:* There ARE forces between molecules (intermolecular forces) — they are just weak.

**Q4. [apply · CFCHTFTH]** State what is overcome when a simple molecular substance boils.
- [✔︎] The weak intermolecular forces between the molecules
- [ ] The strong covalent bonds within the molecules
    - *why wrong:* The strong covalent bonds inside the molecules are NOT broken on boiling.
- [ ] The ionic bonds between the molecules
    - *why wrong:* Simple molecular substances contain no ionic bonds.
- [ ] The metallic bonds holding the molecules together
    - *why wrong:* There are no metallic bonds in a simple molecular substance.

**Q5. [apply · CFCHTFTH]** Describe what a simple molecular substance is.
- [✔︎] A substance made of small molecules, each with a fixed number of atoms joined by strong covalent bonds
- [ ] A giant lattice of ions held by electrostatic forces
    - *why wrong:* A giant ionic lattice describes an ionic compound, not a simple molecular substance.
- [ ] A giant structure of atoms all joined by covalent bonds
    - *why wrong:* A giant covalent structure (like diamond) is different — its covalent bonds run throughout, with no small molecules.
- [ ] A metal made of positive ions in a sea of electrons
    - *why wrong:* That describes a metal, not a molecular substance.

**Q6. [reason · CHTH]** Explain why larger molecules generally have higher melting and boiling points than smaller molecules.
- [✔︎] Larger molecules have more electrons, giving stronger intermolecular forces, so more energy is needed to separate them
- [ ] Larger molecules have stronger covalent bonds inside them
    - *why wrong:* The covalent bonds inside are not what melts; it is the intermolecular forces, which grow with molecule size.
- [ ] Larger molecules are always ionic
    - *why wrong:* Larger molecular substances are still covalent/molecular, not ionic.
- [ ] Larger molecules contain free electrons that raise the melting point
    - *why wrong:* Simple molecular substances have no free electrons; the higher melting point is due to stronger intermolecular forces.

**Q7. [reason · CHTH]** Explain why melting a simple molecular substance does not break its covalent bonds.
- [✔︎] Melting only needs enough energy to overcome the weak intermolecular forces between molecules, which is far less than the energy needed to break the strong covalent bonds
- [ ] The covalent bonds are weaker than the intermolecular forces
    - *why wrong:* Covalent bonds are much STRONGER than intermolecular forces, so melting overcomes the weak forces only.
- [ ] The molecules gain electrons that protect the covalent bonds
    - *why wrong:* No electrons are gained on melting.
- [ ] The covalent bonds are shared out among all the molecules
    - *why wrong:* Covalent bonds stay within each molecule; they are not shared between molecules.

**Q8. [suggest · CHTH]** Many simple molecular substances are gases at room temperature, but iodine is a solid. Suggest why iodine is a solid.
- [✔︎] Iodine molecules are relatively large, so the intermolecular forces between them are strong enough to hold them as a solid at room temperature
- [ ] Iodine has stronger covalent bonds than other molecules
    - *why wrong:* The covalent bond strength inside I₂ is not the reason; it is the stronger intermolecular forces between larger molecules.
- [ ] Iodine is an ionic compound
    - *why wrong:* Iodine (I₂) is a simple molecular substance, not ionic.
- [ ] Iodine molecules contain free electrons
    - *why wrong:* Iodine has no free electrons; its solid state is due to intermolecular forces.

**Q9. [reason · CHTH]** A substance has a low melting point and does not conduct electricity in any state. Deduce its structure and bonding.
- [✔︎] Simple molecular, with covalent bonding — low melting point (weak intermolecular forces) and no charged particles to conduct
- [ ] Ionic — it has a low melting point and free ions
    - *why wrong:* Ionic compounds have HIGH melting points and conduct when molten — this does neither.
- [ ] Metallic — it does not conduct because the electrons are fixed
    - *why wrong:* Metals conduct (delocalised electrons) and usually have high melting points.
- [ ] Giant covalent — low melting point from weak covalent bonds
    - *why wrong:* Giant covalent structures have very HIGH melting points, not low ones.

**Q10. [reason · CHTH]** Explain why the melting point of a simple molecular substance tells you nothing about the strength of its covalent bonds.
- [✔︎] Melting overcomes only the weak intermolecular forces between molecules; the strong covalent bonds inside the molecules are not involved
- [ ] Because the covalent bonds break at exactly the melting point
    - *why wrong:* The covalent bonds are not broken on melting, so the melting point cannot tell you their strength.
- [ ] Because covalent bonds have no strength to measure
    - *why wrong:* Covalent bonds are strong and definitely have a measurable strength — just not one shown by the melting point.
- [ ] Because the melting point measures the ionic bonds instead
    - *why wrong:* There are no ionic bonds in a simple molecular substance.

### Triple Foundation — 12 questions (3 recall / 9 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Water (H₂O) boils at 100°C but methane (CH₄) boils at −161°C, although both are simple molecular. Explain why the difference is so large.
- [✔︎] Water molecules have stronger intermolecular forces than methane molecules, so more energy is needed to separate them
- [ ] Water has more covalent bonds, so it takes more energy to break them
    - *why wrong:* Boiling does not break covalent bonds — water has 2 and methane has 4, so bond count is not the reason.
- [ ] Methane is lighter, so it simply evaporates faster
    - *why wrong:* Lighter molecules can evaporate faster, but boiling point is set by the strength of the intermolecular forces.
- [ ] Water contains oxygen, which makes the molecules too heavy to boil easily
    - *why wrong:* The key reason is the stronger intermolecular forces in water, not simply the mass of the molecules.

**Q2. [reason · CFCHTFTH]** Explain why simple molecular substances do not conduct electricity.
- [✔︎] They have no free electrons or ions — there are no charged particles that can move to carry a current
- [ ] Their covalent bonds are too strong to let electrons move
    - *why wrong:* Conduction needs free charged particles, not weaker bonds — even weak bonds would not help without free charges.
- [ ] Their molecules are too small to hold a charge
    - *why wrong:* Molecular size is not the point; metals are large structures and conduct because of free electrons.
- [ ] Simple molecules are always gases, and gases never conduct
    - *why wrong:* Some gases can conduct (e.g. when ionised), and simple molecular substances can be solids or liquids too.

**Q3. [reason · CFCHTFTH]** Explain why simple molecular substances have low melting and boiling points.
- [✔︎] The forces between the molecules (intermolecular forces) are weak, so only a little energy is needed to separate them
- [ ] The covalent bonds within the molecules are very weak
    - *why wrong:* The covalent bonds within molecules are strong; it is the forces between molecules that are weak.
- [ ] The molecules lose electrons easily when warmed
    - *why wrong:* No electrons are lost on melting; the weak intermolecular forces are simply overcome.
- [ ] There are no forces at all between the molecules
    - *why wrong:* There ARE forces between molecules (intermolecular forces) — they are just weak.

**Q4. [apply · CFCHTFTH]** State what is overcome when a simple molecular substance boils.
- [✔︎] The weak intermolecular forces between the molecules
- [ ] The strong covalent bonds within the molecules
    - *why wrong:* The strong covalent bonds inside the molecules are NOT broken on boiling.
- [ ] The ionic bonds between the molecules
    - *why wrong:* Simple molecular substances contain no ionic bonds.
- [ ] The metallic bonds holding the molecules together
    - *why wrong:* There are no metallic bonds in a simple molecular substance.

**Q5. [apply · CFCHTFTH]** Describe what a simple molecular substance is.
- [✔︎] A substance made of small molecules, each with a fixed number of atoms joined by strong covalent bonds
- [ ] A giant lattice of ions held by electrostatic forces
    - *why wrong:* A giant ionic lattice describes an ionic compound, not a simple molecular substance.
- [ ] A giant structure of atoms all joined by covalent bonds
    - *why wrong:* A giant covalent structure (like diamond) is different — its covalent bonds run throughout, with no small molecules.
- [ ] A metal made of positive ions in a sea of electrons
    - *why wrong:* That describes a metal, not a molecular substance.

**Q6. [recall · CFTF]** State whether simple molecular substances have high or low melting points.
- [✔︎] Low
- [ ] High
    - *why wrong:* Simple molecular substances have LOW melting points because of weak intermolecular forces.
- [ ] Always exactly 100°C
    - *why wrong:* 100°C is the boiling point of water specifically, not a general rule.
- [ ] They never melt
    - *why wrong:* They do melt — easily, in fact, at low temperatures.

**Q7. [recall · CFTF]** State whether simple molecular substances conduct electricity.
- [✔︎] No
- [ ] Yes, always
    - *why wrong:* They have no free charged particles, so they do not conduct.
- [ ] Only when solid
    - *why wrong:* They do not conduct in any state (no free electrons or ions).
- [ ] Only as a metal
    - *why wrong:* Simple molecular substances are not metals and do not conduct.

**Q8. [recall · CFTF]** Name the type of force that must be overcome to melt a simple molecular substance.
- [✔︎] Intermolecular forces
- [ ] Covalent bonds
    - *why wrong:* Covalent bonds are within molecules and are not broken on melting.
- [ ] Ionic bonds
    - *why wrong:* There are no ionic bonds in a simple molecular substance.
- [ ] Metallic bonds
    - *why wrong:* There are no metallic bonds in a simple molecular substance.

**Q9. [apply · CFTF]** Identify which of these is a simple molecular substance.
- [✔︎] Carbon dioxide
- [ ] Sodium chloride
    - *why wrong:* Sodium chloride is a giant ionic lattice, not a simple molecule.
- [ ] Copper
    - *why wrong:* Copper is a metal with a giant metallic structure.
- [ ] Diamond
    - *why wrong:* Diamond is a giant covalent structure, not a simple molecule.

**Q10. [apply · CFTF]** State whether the covalent bonds inside the molecules break when a simple molecular substance melts.
- [✔︎] No — only the forces between the molecules are overcome
- [ ] Yes — the covalent bonds break to let it melt
    - *why wrong:* The strong covalent bonds stay intact; melting overcomes the weak forces between molecules.
- [ ] Yes — half of the covalent bonds break
    - *why wrong:* No covalent bonds break on melting, not even some of them.
- [ ] Only if the substance is heated very slowly
    - *why wrong:* The heating rate does not change which forces are overcome; the covalent bonds stay intact.

**Q11. [apply · TF]** State the two reasons why simple molecular substances do not conduct electricity.
- [✔︎] They have no free electrons and no free ions
- [ ] They have strong covalent bonds and are solid
    - *why wrong:* Bond strength and state are not the reason — the absence of free charged particles is.
- [ ] They are large and heavy
    - *why wrong:* Size and mass do not determine conductivity.
- [ ] They have delocalised electrons that are fixed in place
    - *why wrong:* Simple molecular substances have no delocalised electrons at all.

**Q12. [apply · TF]** Predict the physical state of most simple molecular substances at room temperature.
- [✔︎] Gases or liquids (with some low-melting solids)
- [ ] Always solids with very high melting points
    - *why wrong:* Their weak intermolecular forces give low melting and boiling points, so many are gases or liquids.
- [ ] Always metals
    - *why wrong:* High-melting solids describe giant structures, not simple molecular substances.
- [ ] Always ionic crystals
    - *why wrong:* Simple molecular substances are non-metals; they are not metals or ionic crystals.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Water (H₂O) boils at 100°C but methane (CH₄) boils at −161°C, although both are simple molecular. Explain why the difference is so large.
- [✔︎] Water molecules have stronger intermolecular forces than methane molecules, so more energy is needed to separate them
- [ ] Water has more covalent bonds, so it takes more energy to break them
    - *why wrong:* Boiling does not break covalent bonds — water has 2 and methane has 4, so bond count is not the reason.
- [ ] Methane is lighter, so it simply evaporates faster
    - *why wrong:* Lighter molecules can evaporate faster, but boiling point is set by the strength of the intermolecular forces.
- [ ] Water contains oxygen, which makes the molecules too heavy to boil easily
    - *why wrong:* The key reason is the stronger intermolecular forces in water, not simply the mass of the molecules.

**Q2. [reason · CFCHTFTH]** Explain why simple molecular substances do not conduct electricity.
- [✔︎] They have no free electrons or ions — there are no charged particles that can move to carry a current
- [ ] Their covalent bonds are too strong to let electrons move
    - *why wrong:* Conduction needs free charged particles, not weaker bonds — even weak bonds would not help without free charges.
- [ ] Their molecules are too small to hold a charge
    - *why wrong:* Molecular size is not the point; metals are large structures and conduct because of free electrons.
- [ ] Simple molecules are always gases, and gases never conduct
    - *why wrong:* Some gases can conduct (e.g. when ionised), and simple molecular substances can be solids or liquids too.

**Q3. [reason · CFCHTFTH]** Explain why simple molecular substances have low melting and boiling points.
- [✔︎] The forces between the molecules (intermolecular forces) are weak, so only a little energy is needed to separate them
- [ ] The covalent bonds within the molecules are very weak
    - *why wrong:* The covalent bonds within molecules are strong; it is the forces between molecules that are weak.
- [ ] The molecules lose electrons easily when warmed
    - *why wrong:* No electrons are lost on melting; the weak intermolecular forces are simply overcome.
- [ ] There are no forces at all between the molecules
    - *why wrong:* There ARE forces between molecules (intermolecular forces) — they are just weak.

**Q4. [apply · CFCHTFTH]** State what is overcome when a simple molecular substance boils.
- [✔︎] The weak intermolecular forces between the molecules
- [ ] The strong covalent bonds within the molecules
    - *why wrong:* The strong covalent bonds inside the molecules are NOT broken on boiling.
- [ ] The ionic bonds between the molecules
    - *why wrong:* Simple molecular substances contain no ionic bonds.
- [ ] The metallic bonds holding the molecules together
    - *why wrong:* There are no metallic bonds in a simple molecular substance.

**Q5. [apply · CFCHTFTH]** Describe what a simple molecular substance is.
- [✔︎] A substance made of small molecules, each with a fixed number of atoms joined by strong covalent bonds
- [ ] A giant lattice of ions held by electrostatic forces
    - *why wrong:* A giant ionic lattice describes an ionic compound, not a simple molecular substance.
- [ ] A giant structure of atoms all joined by covalent bonds
    - *why wrong:* A giant covalent structure (like diamond) is different — its covalent bonds run throughout, with no small molecules.
- [ ] A metal made of positive ions in a sea of electrons
    - *why wrong:* That describes a metal, not a molecular substance.

**Q6. [reason · CHTH]** Explain why larger molecules generally have higher melting and boiling points than smaller molecules.
- [✔︎] Larger molecules have more electrons, giving stronger intermolecular forces, so more energy is needed to separate them
- [ ] Larger molecules have stronger covalent bonds inside them
    - *why wrong:* The covalent bonds inside are not what melts; it is the intermolecular forces, which grow with molecule size.
- [ ] Larger molecules are always ionic
    - *why wrong:* Larger molecular substances are still covalent/molecular, not ionic.
- [ ] Larger molecules contain free electrons that raise the melting point
    - *why wrong:* Simple molecular substances have no free electrons; the higher melting point is due to stronger intermolecular forces.

**Q7. [reason · CHTH]** Explain why melting a simple molecular substance does not break its covalent bonds.
- [✔︎] Melting only needs enough energy to overcome the weak intermolecular forces between molecules, which is far less than the energy needed to break the strong covalent bonds
- [ ] The covalent bonds are weaker than the intermolecular forces
    - *why wrong:* Covalent bonds are much STRONGER than intermolecular forces, so melting overcomes the weak forces only.
- [ ] The molecules gain electrons that protect the covalent bonds
    - *why wrong:* No electrons are gained on melting.
- [ ] The covalent bonds are shared out among all the molecules
    - *why wrong:* Covalent bonds stay within each molecule; they are not shared between molecules.

**Q8. [suggest · CHTH]** Many simple molecular substances are gases at room temperature, but iodine is a solid. Suggest why iodine is a solid.
- [✔︎] Iodine molecules are relatively large, so the intermolecular forces between them are strong enough to hold them as a solid at room temperature
- [ ] Iodine has stronger covalent bonds than other molecules
    - *why wrong:* The covalent bond strength inside I₂ is not the reason; it is the stronger intermolecular forces between larger molecules.
- [ ] Iodine is an ionic compound
    - *why wrong:* Iodine (I₂) is a simple molecular substance, not ionic.
- [ ] Iodine molecules contain free electrons
    - *why wrong:* Iodine has no free electrons; its solid state is due to intermolecular forces.

**Q9. [reason · CHTH]** A substance has a low melting point and does not conduct electricity in any state. Deduce its structure and bonding.
- [✔︎] Simple molecular, with covalent bonding — low melting point (weak intermolecular forces) and no charged particles to conduct
- [ ] Ionic — it has a low melting point and free ions
    - *why wrong:* Ionic compounds have HIGH melting points and conduct when molten — this does neither.
- [ ] Metallic — it does not conduct because the electrons are fixed
    - *why wrong:* Metals conduct (delocalised electrons) and usually have high melting points.
- [ ] Giant covalent — low melting point from weak covalent bonds
    - *why wrong:* Giant covalent structures have very HIGH melting points, not low ones.

**Q10. [reason · CHTH]** Explain why the melting point of a simple molecular substance tells you nothing about the strength of its covalent bonds.
- [✔︎] Melting overcomes only the weak intermolecular forces between molecules; the strong covalent bonds inside the molecules are not involved
- [ ] Because the covalent bonds break at exactly the melting point
    - *why wrong:* The covalent bonds are not broken on melting, so the melting point cannot tell you their strength.
- [ ] Because covalent bonds have no strength to measure
    - *why wrong:* Covalent bonds are strong and definitely have a measurable strength — just not one shown by the melting point.
- [ ] Because the melting point measures the ionic bonds instead
    - *why wrong:* There are no ionic bonds in a simple molecular substance.

**Q11. [reason · TH]** Chlorine (Cl₂) is a gas at room temperature but iodine (I₂) is a solid, even though both are simple molecular. Explain this difference.
- [✔︎] Iodine molecules are larger (more electrons), so the intermolecular forces between them are stronger and hold them as a solid, whereas chlorine's weaker forces let it be a gas
- [ ] Iodine has stronger covalent bonds than chlorine
    - *why wrong:* The covalent bond inside each molecule is not what melts; it is the intermolecular forces, stronger for larger iodine.
- [ ] Iodine is ionic while chlorine is covalent
    - *why wrong:* Both are simple covalent molecules; neither is ionic.
- [ ] Chlorine molecules are heavier than iodine molecules
    - *why wrong:* Iodine molecules are actually heavier/larger than chlorine — that is why their intermolecular forces are stronger.

**Q12. [reason · TH]** Explain one limitation of representing a simple molecular substance by drawing just a single molecule.
- [✔︎] A single molecule does not show that the substance contains many molecules with intermolecular forces between them — which is what actually controls its melting and boiling points
- [ ] A single molecule shows the wrong number of atoms
    - *why wrong:* A correct single-molecule diagram shows the right atoms — that is not the limitation.
- [ ] A single molecule wrongly shows ionic bonding
    - *why wrong:* A molecular diagram shows covalent bonding, not ionic; the limitation is about the forces between molecules.
- [ ] A single molecule cannot show the covalent bonds
    - *why wrong:* A single molecule CAN show its covalent bonds; what it cannot show is the forces between separate molecules.


---

## Polymers  ·  `polymers`  ·  AQA 5.2.2.5

> 🚩 **Triple-depth call (your review):** MATCHED — AQA 5.2.2.5 (addition polymers) is identical for Combined and Triple. Foundation difficulty is the same across both pathways. The audit's suggested upgrade is done: the 'name the monomer of poly(ethene)' lookup is upgraded to an explain-why item (ethene polymerises but ethane cannot). This page keeps its polymerisation `equations` and has NO FIFA (no calculation) — so the audit's '4-menu' note (equations present, no FIFA) is expected and correct, not a defect.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often call polymers giant covalent structures because the chains are so large. They are not: a polymer is a very large molecule, and the chains are held to each other only by weak intermolecular forces. In a giant covalent structure such as diamond, strong covalent bonds run all the way through — which is why diamond's melting point is far higher than any polymer's.

**Question sets by tier** (each item shows tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (5 recall / 5 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why polymers have much lower melting points than giant covalent structures such as diamond.
- [✔︎] A polymer is made of separate large molecules held together by weak intermolecular forces, while diamond has strong covalent bonds throughout the whole structure
- [ ] Polymers contain fewer atoms than diamond, so there is less to heat
    - *why wrong:* A single polymer chain can contain millions of atoms — the difference is the TYPE of forces, not the number of atoms.
- [ ] Diamond has ionic bonds, which are stronger than the covalent bonds in polymers
    - *why wrong:* Diamond is entirely covalent, with no ionic bonds; its strong covalent network gives the high melting point.
- [ ] Polymers are man-made, and natural structures are always stronger
    - *why wrong:* Whether a material is natural or synthetic does not set its melting point; structure and bonding do.

**Q2. [reason · CFCHTFTH]** Ethene (CH₂=CH₂) can be used to make poly(ethene), but ethane (C₂H₆) cannot. Explain why.
- [✔︎] Ethene has a C=C double bond that can open up so the monomers join together; ethane is saturated (only single bonds), so it cannot join in this way
- [ ] Ethane is too heavy a molecule to react
    - *why wrong:* Molecular mass is not the barrier; ethane simply has no C=C double bond to open up.
- [ ] Ethane contains no carbon, so it cannot form a carbon chain
    - *why wrong:* Ethane (C₂H₆) does contain carbon — it just has no double bond to enable addition polymerisation.
- [ ] Ethene is an ionic compound, which is needed for polymerisation
    - *why wrong:* Ethene is a covalent molecule, not ionic; the double bond is what matters.

**Q3. [apply · CFCHTFTH]** Describe how a polymer forms from monomers.
- [✔︎] Many small monomer molecules join together to form one long chain molecule
- [ ] A single large molecule breaks apart into many small ones
    - *why wrong:* Polymerisation joins monomers together; it does not break a molecule apart.
- [ ] Two atoms share electrons to form one molecule
    - *why wrong:* A single shared pair between two atoms is one covalent bond, not polymerisation.
- [ ] Positive and negative ions attract to form a lattice
    - *why wrong:* That describes ionic bonding, not the formation of a polymer.

**Q4. [reason · CFCHTFTH]** Explain why poly(ethene) is a solid at room temperature.
- [✔︎] Its molecules are very long chains, so there is enough intermolecular force between them to hold it as a solid
- [ ] Its covalent bonds are ionic and therefore strong
    - *why wrong:* Poly(ethene) has covalent, not ionic, bonds; its solid state is due to intermolecular forces between long chains.
- [ ] It contains a giant lattice of ions
    - *why wrong:* Poly(ethene) is molecular, not a giant ionic lattice.
- [ ] It has delocalised electrons that lock it in place
    - *why wrong:* Poly(ethene) has no delocalised electrons; it is an insulator.

**Q5. [apply · CFCHTFTH]** State what is meant by a monomer.
- [✔︎] A small molecule that can join with many others to form a polymer
- [ ] The long chain molecule made when many small molecules join
    - *why wrong:* The long chain is the POLYMER; the monomer is the small starting molecule.
- [ ] A single atom that makes up a polymer
    - *why wrong:* A monomer is a molecule, not a single atom.
- [ ] A mixture of two different plastics
    - *why wrong:* A monomer is a pure substance (one type of molecule), not a mixture.

**Q6. [recall · CFTF]** State what a polymer is.
- [✔︎] A very large molecule made of many repeating units
- [ ] A small molecule with only a few atoms
    - *why wrong:* Polymers are large, not small, molecules.
- [ ] A giant lattice of ions
    - *why wrong:* Polymers are molecular, not ionic lattices.
- [ ] A pure metal
    - *why wrong:* Polymers are non-metals, not metals.

**Q7. [recall · CFTF]** Name the small molecules that join together to make a polymer.
- [✔︎] Monomers
- [ ] Polymers
    - *why wrong:* The polymer is the final long chain; the small starting molecules are monomers.
- [ ] Isotopes
    - *why wrong:* Isotopes are atoms of the same element with different numbers of neutrons — unrelated.
- [ ] Alloys
    - *why wrong:* An alloy is a mixture of metals, not a building block of a polymer.

**Q8. [recall · CFTF]** State whether polymers conduct electricity.
- [✔︎] No — they are insulators
- [ ] Yes — like metals
    - *why wrong:* Polymers have no free electrons or ions, so they are insulators.
- [ ] Only when solid
    - *why wrong:* Polymers do not conduct in any state — they have no free charged particles.
- [ ] Only when molten
    - *why wrong:* Melting a polymer does not give it free charged particles, so it still does not conduct.

**Q9. [recall · CFTF]** Identify the monomer used to make poly(ethene).
- [✔︎] Ethene
- [ ] Ethane
    - *why wrong:* Ethane is saturated (no C=C), so it cannot undergo addition polymerisation.
- [ ] Ethanol
    - *why wrong:* Ethanol is an alcohol and does not form poly(ethene).
- [ ] Methane
    - *why wrong:* Methane has only one carbon and no double bond, so it cannot form poly(ethene).

**Q10. [recall · CFTF]** State the type of bond in a monomer that allows addition polymerisation to happen.
- [✔︎] A carbon–carbon double bond (C=C)
- [ ] A single carbon–carbon bond
    - *why wrong:* A single C–C bond cannot open up to join monomers; a C=C double bond is needed.
- [ ] An ionic bond
    - *why wrong:* Monomers are covalent molecules, not ionic.
- [ ] A metallic bond
    - *why wrong:* Monomers contain no metallic bonding.

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why polymers have much lower melting points than giant covalent structures such as diamond.
- [✔︎] A polymer is made of separate large molecules held together by weak intermolecular forces, while diamond has strong covalent bonds throughout the whole structure
- [ ] Polymers contain fewer atoms than diamond, so there is less to heat
    - *why wrong:* A single polymer chain can contain millions of atoms — the difference is the TYPE of forces, not the number of atoms.
- [ ] Diamond has ionic bonds, which are stronger than the covalent bonds in polymers
    - *why wrong:* Diamond is entirely covalent, with no ionic bonds; its strong covalent network gives the high melting point.
- [ ] Polymers are man-made, and natural structures are always stronger
    - *why wrong:* Whether a material is natural or synthetic does not set its melting point; structure and bonding do.

**Q2. [reason · CFCHTFTH]** Ethene (CH₂=CH₂) can be used to make poly(ethene), but ethane (C₂H₆) cannot. Explain why.
- [✔︎] Ethene has a C=C double bond that can open up so the monomers join together; ethane is saturated (only single bonds), so it cannot join in this way
- [ ] Ethane is too heavy a molecule to react
    - *why wrong:* Molecular mass is not the barrier; ethane simply has no C=C double bond to open up.
- [ ] Ethane contains no carbon, so it cannot form a carbon chain
    - *why wrong:* Ethane (C₂H₆) does contain carbon — it just has no double bond to enable addition polymerisation.
- [ ] Ethene is an ionic compound, which is needed for polymerisation
    - *why wrong:* Ethene is a covalent molecule, not ionic; the double bond is what matters.

**Q3. [apply · CFCHTFTH]** Describe how a polymer forms from monomers.
- [✔︎] Many small monomer molecules join together to form one long chain molecule
- [ ] A single large molecule breaks apart into many small ones
    - *why wrong:* Polymerisation joins monomers together; it does not break a molecule apart.
- [ ] Two atoms share electrons to form one molecule
    - *why wrong:* A single shared pair between two atoms is one covalent bond, not polymerisation.
- [ ] Positive and negative ions attract to form a lattice
    - *why wrong:* That describes ionic bonding, not the formation of a polymer.

**Q4. [reason · CFCHTFTH]** Explain why poly(ethene) is a solid at room temperature.
- [✔︎] Its molecules are very long chains, so there is enough intermolecular force between them to hold it as a solid
- [ ] Its covalent bonds are ionic and therefore strong
    - *why wrong:* Poly(ethene) has covalent, not ionic, bonds; its solid state is due to intermolecular forces between long chains.
- [ ] It contains a giant lattice of ions
    - *why wrong:* Poly(ethene) is molecular, not a giant ionic lattice.
- [ ] It has delocalised electrons that lock it in place
    - *why wrong:* Poly(ethene) has no delocalised electrons; it is an insulator.

**Q5. [apply · CFCHTFTH]** State what is meant by a monomer.
- [✔︎] A small molecule that can join with many others to form a polymer
- [ ] The long chain molecule made when many small molecules join
    - *why wrong:* The long chain is the POLYMER; the monomer is the small starting molecule.
- [ ] A single atom that makes up a polymer
    - *why wrong:* A monomer is a molecule, not a single atom.
- [ ] A mixture of two different plastics
    - *why wrong:* A monomer is a pure substance (one type of molecule), not a mixture.

**Q6. [reason · CHTH]** Explain, in terms of the double bond, how addition polymerisation forms poly(ethene) from ethene.
- [✔︎] The C=C double bond in each ethene opens up; the freed electrons form new bonds to neighbouring monomers, linking them into a long saturated chain
- [ ] The ethene molecules lose atoms which join to form the chain
    - *why wrong:* In addition polymerisation no atoms are lost — the whole monomer becomes part of the chain.
- [ ] The ethene molecules transfer electrons to form ions that attract
    - *why wrong:* Polymerisation of ethene is by opening the double bond (covalent), not by forming ions.
- [ ] Water is removed between each pair of monomers to join them
    - *why wrong:* Removing water describes condensation polymerisation, not the addition polymerisation of ethene.

**Q7. [reason · CHTH]** Explain why a polymer with longer chains tends to have a higher melting point than one with shorter chains.
- [✔︎] Longer chains have more points of contact, so the total intermolecular forces between chains are stronger and need more energy to overcome
- [ ] Longer chains have stronger covalent bonds along them
    - *why wrong:* The covalent bonds along the chain are not what melts; the intermolecular forces between chains are, and these grow with chain length.
- [ ] Longer chains contain ions that attract strongly
    - *why wrong:* Polymers are molecular, not ionic — there are no ions between the chains.
- [ ] Longer chains are always cross-linked
    - *why wrong:* Chain length and cross-linking are different things; a longer chain is not automatically cross-linked.

**Q8. [suggest · CHTH]** PVC is stiffer and higher-melting than poly(ethene). Suggest why, in terms of intermolecular forces.
- [✔︎] PVC contains polar C–Cl bonds, giving stronger intermolecular forces between the chains than in poly(ethene)
- [ ] PVC has ionic bonds between its chains
    - *why wrong:* PVC is still a molecular polymer, not ionic; the stronger forces come from the polar C–Cl bonds.
- [ ] PVC has weaker covalent bonds, so it sets harder
    - *why wrong:* Weaker covalent bonds would make it less stable, not stiffer; the effect is due to stronger intermolecular forces.
- [ ] PVC chains are metallic and conduct heat away
    - *why wrong:* PVC is an insulator, not metallic.

**Q9. [reason · CHTH]** Explain why melting a polymer does not break the covalent bonds along its chains.
- [✔︎] Melting only supplies enough energy to overcome the weak intermolecular forces between the chains, which is far less than needed to break the strong covalent bonds
- [ ] The covalent bonds are weaker than the forces between chains
    - *why wrong:* Covalent bonds are much stronger than the intermolecular forces, so only the weak forces are overcome.
- [ ] The chains gain electrons that protect the bonds
    - *why wrong:* No electrons are gained on melting.
- [ ] The covalent bonds are shared between the chains
    - *why wrong:* Covalent bonds run along each chain; they are not shared between separate chains.

**Q10. [reason · CHTH]** In addition polymerisation, explain why no small molecule is lost when the monomers join together.
- [✔︎] Every atom of each monomer ends up in the polymer chain, because the monomers simply add together at the opened double bond
- [ ] A water molecule is released, but it is too small to notice
    - *why wrong:* Losing water is condensation polymerisation; addition polymerisation loses nothing.
- [ ] The monomers lose hydrogen atoms as they join
    - *why wrong:* No hydrogen atoms are lost in addition polymerisation.
- [ ] Half of each monomer is left behind as waste
    - *why wrong:* No part of the monomer is left behind — all atoms are kept in the polymer.

### Triple Foundation — 12 questions (5 recall / 7 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why polymers have much lower melting points than giant covalent structures such as diamond.
- [✔︎] A polymer is made of separate large molecules held together by weak intermolecular forces, while diamond has strong covalent bonds throughout the whole structure
- [ ] Polymers contain fewer atoms than diamond, so there is less to heat
    - *why wrong:* A single polymer chain can contain millions of atoms — the difference is the TYPE of forces, not the number of atoms.
- [ ] Diamond has ionic bonds, which are stronger than the covalent bonds in polymers
    - *why wrong:* Diamond is entirely covalent, with no ionic bonds; its strong covalent network gives the high melting point.
- [ ] Polymers are man-made, and natural structures are always stronger
    - *why wrong:* Whether a material is natural or synthetic does not set its melting point; structure and bonding do.

**Q2. [reason · CFCHTFTH]** Ethene (CH₂=CH₂) can be used to make poly(ethene), but ethane (C₂H₆) cannot. Explain why.
- [✔︎] Ethene has a C=C double bond that can open up so the monomers join together; ethane is saturated (only single bonds), so it cannot join in this way
- [ ] Ethane is too heavy a molecule to react
    - *why wrong:* Molecular mass is not the barrier; ethane simply has no C=C double bond to open up.
- [ ] Ethane contains no carbon, so it cannot form a carbon chain
    - *why wrong:* Ethane (C₂H₆) does contain carbon — it just has no double bond to enable addition polymerisation.
- [ ] Ethene is an ionic compound, which is needed for polymerisation
    - *why wrong:* Ethene is a covalent molecule, not ionic; the double bond is what matters.

**Q3. [apply · CFCHTFTH]** Describe how a polymer forms from monomers.
- [✔︎] Many small monomer molecules join together to form one long chain molecule
- [ ] A single large molecule breaks apart into many small ones
    - *why wrong:* Polymerisation joins monomers together; it does not break a molecule apart.
- [ ] Two atoms share electrons to form one molecule
    - *why wrong:* A single shared pair between two atoms is one covalent bond, not polymerisation.
- [ ] Positive and negative ions attract to form a lattice
    - *why wrong:* That describes ionic bonding, not the formation of a polymer.

**Q4. [reason · CFCHTFTH]** Explain why poly(ethene) is a solid at room temperature.
- [✔︎] Its molecules are very long chains, so there is enough intermolecular force between them to hold it as a solid
- [ ] Its covalent bonds are ionic and therefore strong
    - *why wrong:* Poly(ethene) has covalent, not ionic, bonds; its solid state is due to intermolecular forces between long chains.
- [ ] It contains a giant lattice of ions
    - *why wrong:* Poly(ethene) is molecular, not a giant ionic lattice.
- [ ] It has delocalised electrons that lock it in place
    - *why wrong:* Poly(ethene) has no delocalised electrons; it is an insulator.

**Q5. [apply · CFCHTFTH]** State what is meant by a monomer.
- [✔︎] A small molecule that can join with many others to form a polymer
- [ ] The long chain molecule made when many small molecules join
    - *why wrong:* The long chain is the POLYMER; the monomer is the small starting molecule.
- [ ] A single atom that makes up a polymer
    - *why wrong:* A monomer is a molecule, not a single atom.
- [ ] A mixture of two different plastics
    - *why wrong:* A monomer is a pure substance (one type of molecule), not a mixture.

**Q6. [recall · CFTF]** State what a polymer is.
- [✔︎] A very large molecule made of many repeating units
- [ ] A small molecule with only a few atoms
    - *why wrong:* Polymers are large, not small, molecules.
- [ ] A giant lattice of ions
    - *why wrong:* Polymers are molecular, not ionic lattices.
- [ ] A pure metal
    - *why wrong:* Polymers are non-metals, not metals.

**Q7. [recall · CFTF]** Name the small molecules that join together to make a polymer.
- [✔︎] Monomers
- [ ] Polymers
    - *why wrong:* The polymer is the final long chain; the small starting molecules are monomers.
- [ ] Isotopes
    - *why wrong:* Isotopes are atoms of the same element with different numbers of neutrons — unrelated.
- [ ] Alloys
    - *why wrong:* An alloy is a mixture of metals, not a building block of a polymer.

**Q8. [recall · CFTF]** State whether polymers conduct electricity.
- [✔︎] No — they are insulators
- [ ] Yes — like metals
    - *why wrong:* Polymers have no free electrons or ions, so they are insulators.
- [ ] Only when solid
    - *why wrong:* Polymers do not conduct in any state — they have no free charged particles.
- [ ] Only when molten
    - *why wrong:* Melting a polymer does not give it free charged particles, so it still does not conduct.

**Q9. [recall · CFTF]** Identify the monomer used to make poly(ethene).
- [✔︎] Ethene
- [ ] Ethane
    - *why wrong:* Ethane is saturated (no C=C), so it cannot undergo addition polymerisation.
- [ ] Ethanol
    - *why wrong:* Ethanol is an alcohol and does not form poly(ethene).
- [ ] Methane
    - *why wrong:* Methane has only one carbon and no double bond, so it cannot form poly(ethene).

**Q10. [recall · CFTF]** State the type of bond in a monomer that allows addition polymerisation to happen.
- [✔︎] A carbon–carbon double bond (C=C)
- [ ] A single carbon–carbon bond
    - *why wrong:* A single C–C bond cannot open up to join monomers; a C=C double bond is needed.
- [ ] An ionic bond
    - *why wrong:* Monomers are covalent molecules, not ionic.
- [ ] A metallic bond
    - *why wrong:* Monomers contain no metallic bonding.

**Q11. [apply · TF]** Identify an everyday use of poly(ethene).
- [✔︎] Plastic bags and bottles
- [ ] Electrical wiring cores
    - *why wrong:* Electrical wiring cores are made from copper (a conductor), not poly(ethene).
- [ ] Window glass
    - *why wrong:* Window glass is not a polymer.
- [ ] Saucepan bases
    - *why wrong:* Saucepan bases are metal (good heat conductors), not poly(ethene).

**Q12. [apply · TF]** Predict whether a polymer will conduct electricity, and give a reason.
- [✔︎] No — it has no free electrons or ions to carry a charge
- [ ] Yes — its long chains carry the current
    - *why wrong:* Chain length does not give free charged particles, so a polymer does not conduct.
- [ ] Yes — because it contains carbon
    - *why wrong:* Containing carbon does not make a substance a conductor (diamond is carbon and does not conduct).
- [ ] Only when dissolved in water
    - *why wrong:* Polymers do not release ions when in contact with water; they remain insulators.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why polymers have much lower melting points than giant covalent structures such as diamond.
- [✔︎] A polymer is made of separate large molecules held together by weak intermolecular forces, while diamond has strong covalent bonds throughout the whole structure
- [ ] Polymers contain fewer atoms than diamond, so there is less to heat
    - *why wrong:* A single polymer chain can contain millions of atoms — the difference is the TYPE of forces, not the number of atoms.
- [ ] Diamond has ionic bonds, which are stronger than the covalent bonds in polymers
    - *why wrong:* Diamond is entirely covalent, with no ionic bonds; its strong covalent network gives the high melting point.
- [ ] Polymers are man-made, and natural structures are always stronger
    - *why wrong:* Whether a material is natural or synthetic does not set its melting point; structure and bonding do.

**Q2. [reason · CFCHTFTH]** Ethene (CH₂=CH₂) can be used to make poly(ethene), but ethane (C₂H₆) cannot. Explain why.
- [✔︎] Ethene has a C=C double bond that can open up so the monomers join together; ethane is saturated (only single bonds), so it cannot join in this way
- [ ] Ethane is too heavy a molecule to react
    - *why wrong:* Molecular mass is not the barrier; ethane simply has no C=C double bond to open up.
- [ ] Ethane contains no carbon, so it cannot form a carbon chain
    - *why wrong:* Ethane (C₂H₆) does contain carbon — it just has no double bond to enable addition polymerisation.
- [ ] Ethene is an ionic compound, which is needed for polymerisation
    - *why wrong:* Ethene is a covalent molecule, not ionic; the double bond is what matters.

**Q3. [apply · CFCHTFTH]** Describe how a polymer forms from monomers.
- [✔︎] Many small monomer molecules join together to form one long chain molecule
- [ ] A single large molecule breaks apart into many small ones
    - *why wrong:* Polymerisation joins monomers together; it does not break a molecule apart.
- [ ] Two atoms share electrons to form one molecule
    - *why wrong:* A single shared pair between two atoms is one covalent bond, not polymerisation.
- [ ] Positive and negative ions attract to form a lattice
    - *why wrong:* That describes ionic bonding, not the formation of a polymer.

**Q4. [reason · CFCHTFTH]** Explain why poly(ethene) is a solid at room temperature.
- [✔︎] Its molecules are very long chains, so there is enough intermolecular force between them to hold it as a solid
- [ ] Its covalent bonds are ionic and therefore strong
    - *why wrong:* Poly(ethene) has covalent, not ionic, bonds; its solid state is due to intermolecular forces between long chains.
- [ ] It contains a giant lattice of ions
    - *why wrong:* Poly(ethene) is molecular, not a giant ionic lattice.
- [ ] It has delocalised electrons that lock it in place
    - *why wrong:* Poly(ethene) has no delocalised electrons; it is an insulator.

**Q5. [apply · CFCHTFTH]** State what is meant by a monomer.
- [✔︎] A small molecule that can join with many others to form a polymer
- [ ] The long chain molecule made when many small molecules join
    - *why wrong:* The long chain is the POLYMER; the monomer is the small starting molecule.
- [ ] A single atom that makes up a polymer
    - *why wrong:* A monomer is a molecule, not a single atom.
- [ ] A mixture of two different plastics
    - *why wrong:* A monomer is a pure substance (one type of molecule), not a mixture.

**Q6. [reason · CHTH]** Explain, in terms of the double bond, how addition polymerisation forms poly(ethene) from ethene.
- [✔︎] The C=C double bond in each ethene opens up; the freed electrons form new bonds to neighbouring monomers, linking them into a long saturated chain
- [ ] The ethene molecules lose atoms which join to form the chain
    - *why wrong:* In addition polymerisation no atoms are lost — the whole monomer becomes part of the chain.
- [ ] The ethene molecules transfer electrons to form ions that attract
    - *why wrong:* Polymerisation of ethene is by opening the double bond (covalent), not by forming ions.
- [ ] Water is removed between each pair of monomers to join them
    - *why wrong:* Removing water describes condensation polymerisation, not the addition polymerisation of ethene.

**Q7. [reason · CHTH]** Explain why a polymer with longer chains tends to have a higher melting point than one with shorter chains.
- [✔︎] Longer chains have more points of contact, so the total intermolecular forces between chains are stronger and need more energy to overcome
- [ ] Longer chains have stronger covalent bonds along them
    - *why wrong:* The covalent bonds along the chain are not what melts; the intermolecular forces between chains are, and these grow with chain length.
- [ ] Longer chains contain ions that attract strongly
    - *why wrong:* Polymers are molecular, not ionic — there are no ions between the chains.
- [ ] Longer chains are always cross-linked
    - *why wrong:* Chain length and cross-linking are different things; a longer chain is not automatically cross-linked.

**Q8. [suggest · CHTH]** PVC is stiffer and higher-melting than poly(ethene). Suggest why, in terms of intermolecular forces.
- [✔︎] PVC contains polar C–Cl bonds, giving stronger intermolecular forces between the chains than in poly(ethene)
- [ ] PVC has ionic bonds between its chains
    - *why wrong:* PVC is still a molecular polymer, not ionic; the stronger forces come from the polar C–Cl bonds.
- [ ] PVC has weaker covalent bonds, so it sets harder
    - *why wrong:* Weaker covalent bonds would make it less stable, not stiffer; the effect is due to stronger intermolecular forces.
- [ ] PVC chains are metallic and conduct heat away
    - *why wrong:* PVC is an insulator, not metallic.

**Q9. [reason · CHTH]** Explain why melting a polymer does not break the covalent bonds along its chains.
- [✔︎] Melting only supplies enough energy to overcome the weak intermolecular forces between the chains, which is far less than needed to break the strong covalent bonds
- [ ] The covalent bonds are weaker than the forces between chains
    - *why wrong:* Covalent bonds are much stronger than the intermolecular forces, so only the weak forces are overcome.
- [ ] The chains gain electrons that protect the bonds
    - *why wrong:* No electrons are gained on melting.
- [ ] The covalent bonds are shared between the chains
    - *why wrong:* Covalent bonds run along each chain; they are not shared between separate chains.

**Q10. [reason · CHTH]** In addition polymerisation, explain why no small molecule is lost when the monomers join together.
- [✔︎] Every atom of each monomer ends up in the polymer chain, because the monomers simply add together at the opened double bond
- [ ] A water molecule is released, but it is too small to notice
    - *why wrong:* Losing water is condensation polymerisation; addition polymerisation loses nothing.
- [ ] The monomers lose hydrogen atoms as they join
    - *why wrong:* No hydrogen atoms are lost in addition polymerisation.
- [ ] Half of each monomer is left behind as waste
    - *why wrong:* No part of the monomer is left behind — all atoms are kept in the polymer.

**Q11. [reason · TH]** Describe the repeating unit of poly(ethene) and explain how it relates to the ethene monomer.
- [✔︎] The repeating unit is —CH₂—CH₂—, written as [—CH₂—CH₂—]ₙ; it contains the same atoms as ethene but the double bond has become a single bond as the monomers joined
- [ ] The repeating unit is CH₂=CH₂, the same as the monomer including its double bond
    - *why wrong:* In the polymer the C=C double bond has opened to single bonds, so the repeating unit is not still CH₂=CH₂.
- [ ] The repeating unit is a single carbon atom
    - *why wrong:* The repeating unit contains two carbons (—CH₂—CH₂—), not a single carbon atom.
- [ ] The repeating unit contains an extra oxygen atom from the reaction
    - *why wrong:* Addition polymerisation adds no atoms; there is no extra oxygen.

**Q12. [reason · TH]** Explain why polymers are described as having a simple molecular structure, even though the molecules are very large.
- [✔︎] Each polymer chain is a separate molecule, and the chains are held to one another by weak intermolecular forces — the same kind of arrangement as other molecular substances
- [ ] Because the chains are joined by a giant network of covalent bonds
    - *why wrong:* If covalent bonds ran between all the chains it would be a giant covalent structure, not molecular — polymers are held by weak intermolecular forces instead.
- [ ] Because the chains are held together by ionic bonds
    - *why wrong:* There are no ionic bonds between polymer chains.
- [ ] Because the chains contain delocalised electrons
    - *why wrong:* Polymers have no delocalised electrons.


---

## Giant Covalent Structures  ·  `giant-covalent-structures`  ·  AQA 5.2.2.6

> 🚩 **Triple-depth call (your review):** MATCHED across pathways (graphene and fullerenes are in AQA 5.2.2.6 for BOTH Combined and Triple; only 5.2.3 nanoparticles is Triple-only). RESOLVED per Mide's ruling (follow the AQA spec): graphene / fullerenes / nanotubes now carry Foundation-level recall/describe coverage (structure + a use of each) in the CF/TF sets, with the deeper 'explain why / in terms of bonding' reasoning kept at Higher (CH/TH). Foundation difficulty is the same across both pathways.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often assume that because diamond and graphite are both giant covalent structures made of carbon, they must have the same properties. They do not: graphite conducts electricity and is soft and slippery, while diamond does not conduct and is extremely hard. The difference is that in graphite each carbon bonds to only three others, leaving one delocalised electron per atom and weak forces between layers; in diamond every carbon bonds to four others with no free electrons.

**Question sets by tier** (each item shows tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (3 recall / 7 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why graphite conducts electricity but diamond does not.
- [✔︎] In graphite each carbon uses only 3 of its 4 outer electrons for bonds, leaving one delocalised electron per atom free to move; in diamond all 4 are used in bonds, so none are free
- [ ] Graphite contains more carbon atoms, and more atoms means better conductivity
    - *why wrong:* The number of atoms does not determine conductivity — the availability of free electrons does.
- [ ] Diamond is transparent, so electricity cannot pass through it
    - *why wrong:* Transparency and electrical conductivity are unrelated properties.
- [ ] Graphite has metallic bonding while diamond has ionic bonding
    - *why wrong:* Both diamond and graphite are entirely covalent; neither is metallic or ionic.

**Q2. [reason · CFCHTFTH]** Explain why graphite is used as a lubricant.
- [✔︎] Its carbon atoms form layers held together by weak intermolecular forces, so the layers can slide over each other easily
- [ ] It is smooth because it has no atoms on its surface
    - *why wrong:* All surfaces have atoms; graphite is slippery because its layers slide, not because it lacks surface atoms.
- [ ] It dissolves in water to make a slippery solution
    - *why wrong:* Graphite does not dissolve in water; it is a dry lubricant.
- [ ] It is as hard as diamond, which makes surfaces slippery
    - *why wrong:* Graphite is soft, not hard like diamond; hardness would not make it a lubricant.

**Q3. [reason · CFCHTFTH]** Explain why diamond is very hard and has a very high melting point.
- [✔︎] Every carbon atom is joined to four others by strong covalent bonds throughout a rigid giant 3D lattice, so a great deal of energy is needed to break it
- [ ] Its molecules are held together by strong intermolecular forces
    - *why wrong:* Diamond is not made of separate molecules — it is a giant covalent lattice with no intermolecular forces to speak of.
- [ ] It contains ionic bonds, which are very strong
    - *why wrong:* Diamond is entirely covalent; it contains no ionic bonds.
- [ ] It has delocalised electrons that hold the atoms tightly
    - *why wrong:* Diamond has no delocalised electrons — all four outer electrons of each carbon are in bonds.

**Q4. [apply · CFCHTFTH]** Describe what a giant covalent structure is.
- [✔︎] A structure in which a very large number of atoms are all joined together by covalent bonds throughout
- [ ] A structure made of small, separate molecules
    - *why wrong:* Giant covalent structures have no small separate molecules; the covalent bonding is continuous.
- [ ] A lattice of positive and negative ions
    - *why wrong:* A lattice of ions is an ionic compound, not covalent.
- [ ] A metal with delocalised electrons
    - *why wrong:* A metal with delocalised electrons is a metallic structure, not covalent.

**Q5. [apply · CFCHTFTH]** State why diamond and graphite can both be made of carbon yet have very different properties.
- [✔︎] They are different structural forms (allotropes) of carbon — the atoms are joined in different arrangements
- [ ] They contain different elements
    - *why wrong:* Both are pure carbon — they differ only in how the carbon atoms are arranged.
- [ ] One is a metal and the other is a non-metal
    - *why wrong:* Carbon is a non-metal in both forms; neither is a metal.
- [ ] Diamond contains ions and graphite contains molecules
    - *why wrong:* Both are giant covalent structures — neither contains ions or small molecules.

**Q6. [recall · CFTF]** Describe the structure of graphene and give one of its uses.
- [✔︎] A single layer of graphite, one atom thick; it conducts electricity and can be used in electronics
- [ ] A hollow ball of carbon atoms; used as a lubricant
    - *why wrong:* A hollow ball of carbon atoms describes a fullerene, not graphene.
- [ ] A giant 3D lattice with four bonds per carbon; used in cutting tools
    - *why wrong:* A giant 3D lattice with four bonds per carbon (used in cutting tools) describes diamond, not graphene.
- [ ] A long chain of repeating units; used to make plastic bags
    - *why wrong:* A long chain of repeating units used for plastic bags describes a polymer, not graphene.

**Q7. [recall · CFTF]** Describe the structure of buckminsterfullerene (C₆₀) and give one of its uses.
- [✔︎] A hollow ball (cage) of 60 carbon atoms; it can be used to deliver drugs into the body
- [ ] A single flat sheet of carbon one atom thick; used in electronics
    - *why wrong:* A single flat sheet one atom thick describes graphene, not a fullerene.
- [ ] A giant 3D lattice of carbon; used in cutting tools
    - *why wrong:* A giant 3D lattice used in cutting tools describes diamond, not a hollow fullerene molecule.
- [ ] A regular lattice of positive ions in a sea of electrons; used in wiring
    - *why wrong:* Positive ions in a sea of electrons describes a metal; a fullerene is a covalent carbon molecule.

**Q8. [recall · CFTF]** Describe carbon nanotubes and give one of their uses.
- [✔︎] Cylinders (tubes) of carbon atoms, like rolled-up graphene; they are very strong and are used to reinforce materials
- [ ] Hollow balls of carbon; burned as a fuel for energy
    - *why wrong:* Hollow balls of carbon describe fullerenes, and carbon nanostructures are not burned as a fuel.
- [ ] A soft, slippery form of carbon; used as pencil 'lead'
    - *why wrong:* A soft, slippery carbon used as pencil 'lead' describes graphite, not nanotubes.
- [ ] A giant 3D lattice of carbon; used as a gemstone
    - *why wrong:* A giant 3D lattice used as a gemstone describes diamond, not a nanotube.

**Q9. [apply · CFTF]** Identify a use of diamond that depends on its hardness.
- [✔︎] Tips for cutting tools and drill bits
- [ ] Electrical wiring
    - *why wrong:* Diamond does not conduct electricity, so it is not used for wiring.
- [ ] Pencil 'lead'
    - *why wrong:* Pencil 'lead' and lubrication use graphite (soft, layered), not diamond.
- [ ] Lubricating machine parts
    - *why wrong:* Lubrication uses graphite; diamond is hard, not slippery.

**Q10. [apply · CFTF]** Identify which substance is a giant covalent structure.
- [✔︎] Diamond
- [ ] Sodium chloride
    - *why wrong:* Sodium chloride is a giant ionic lattice.
- [ ] Copper
    - *why wrong:* Copper is a metal (giant metallic structure).
- [ ] Carbon dioxide
    - *why wrong:* Carbon dioxide is a simple molecular substance, not giant covalent.

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why graphite conducts electricity but diamond does not.
- [✔︎] In graphite each carbon uses only 3 of its 4 outer electrons for bonds, leaving one delocalised electron per atom free to move; in diamond all 4 are used in bonds, so none are free
- [ ] Graphite contains more carbon atoms, and more atoms means better conductivity
    - *why wrong:* The number of atoms does not determine conductivity — the availability of free electrons does.
- [ ] Diamond is transparent, so electricity cannot pass through it
    - *why wrong:* Transparency and electrical conductivity are unrelated properties.
- [ ] Graphite has metallic bonding while diamond has ionic bonding
    - *why wrong:* Both diamond and graphite are entirely covalent; neither is metallic or ionic.

**Q2. [reason · CFCHTFTH]** Explain why graphite is used as a lubricant.
- [✔︎] Its carbon atoms form layers held together by weak intermolecular forces, so the layers can slide over each other easily
- [ ] It is smooth because it has no atoms on its surface
    - *why wrong:* All surfaces have atoms; graphite is slippery because its layers slide, not because it lacks surface atoms.
- [ ] It dissolves in water to make a slippery solution
    - *why wrong:* Graphite does not dissolve in water; it is a dry lubricant.
- [ ] It is as hard as diamond, which makes surfaces slippery
    - *why wrong:* Graphite is soft, not hard like diamond; hardness would not make it a lubricant.

**Q3. [reason · CFCHTFTH]** Explain why diamond is very hard and has a very high melting point.
- [✔︎] Every carbon atom is joined to four others by strong covalent bonds throughout a rigid giant 3D lattice, so a great deal of energy is needed to break it
- [ ] Its molecules are held together by strong intermolecular forces
    - *why wrong:* Diamond is not made of separate molecules — it is a giant covalent lattice with no intermolecular forces to speak of.
- [ ] It contains ionic bonds, which are very strong
    - *why wrong:* Diamond is entirely covalent; it contains no ionic bonds.
- [ ] It has delocalised electrons that hold the atoms tightly
    - *why wrong:* Diamond has no delocalised electrons — all four outer electrons of each carbon are in bonds.

**Q4. [apply · CFCHTFTH]** Describe what a giant covalent structure is.
- [✔︎] A structure in which a very large number of atoms are all joined together by covalent bonds throughout
- [ ] A structure made of small, separate molecules
    - *why wrong:* Giant covalent structures have no small separate molecules; the covalent bonding is continuous.
- [ ] A lattice of positive and negative ions
    - *why wrong:* A lattice of ions is an ionic compound, not covalent.
- [ ] A metal with delocalised electrons
    - *why wrong:* A metal with delocalised electrons is a metallic structure, not covalent.

**Q5. [apply · CFCHTFTH]** State why diamond and graphite can both be made of carbon yet have very different properties.
- [✔︎] They are different structural forms (allotropes) of carbon — the atoms are joined in different arrangements
- [ ] They contain different elements
    - *why wrong:* Both are pure carbon — they differ only in how the carbon atoms are arranged.
- [ ] One is a metal and the other is a non-metal
    - *why wrong:* Carbon is a non-metal in both forms; neither is a metal.
- [ ] Diamond contains ions and graphite contains molecules
    - *why wrong:* Both are giant covalent structures — neither contains ions or small molecules.

**Q6. [reason · CHTH]** Explain why silicon dioxide (found in sand and quartz) has a very high melting point.
- [✔︎] It is a giant covalent structure in which many strong Si–O covalent bonds must be broken to melt it
- [ ] It is an ionic compound with strong forces between ions
    - *why wrong:* Silicon dioxide is giant covalent, not ionic.
- [ ] It is a simple molecule with strong intermolecular forces
    - *why wrong:* It is not a simple molecule — the covalent bonding runs throughout the whole structure.
- [ ] It is a metal with strong metallic bonds
    - *why wrong:* Silicon dioxide is not a metal.

**Q7. [reason · CHTH]** Graphene is a single layer of graphite. Explain why it conducts electricity and is very strong.
- [✔︎] Each carbon is covalently bonded to three others in a strong hexagonal network, and the fourth outer electron of each carbon is delocalised, so it can carry charge
- [ ] It contains free-moving ions that carry charge
    - *why wrong:* Graphene has no ions; conduction is by delocalised electrons.
- [ ] It is a metal, so it conducts and is strong
    - *why wrong:* Graphene is a form of carbon (covalent), not a metal.
- [ ] Its molecules are held together by strong intermolecular forces
    - *why wrong:* Graphene is a giant covalent sheet, not separate molecules with intermolecular forces.

**Q8. [reason · CHTH]** Explain why buckminsterfullerene (C₆₀) can be used to deliver drugs to specific parts of the body.
- [✔︎] Its molecules are hollow cages, so a drug molecule can be carried inside and released where it is needed
- [ ] It is a metal, so the drug is carried on its surface by delocalised electrons
    - *why wrong:* C₆₀ is a covalent carbon molecule, not a metal, so it has no delocalised-electron surface to carry a drug this way.
- [ ] It reacts with the drug to form a new compound that dissolves in the blood
    - *why wrong:* The drug is held physically inside the hollow cage; C₆₀ does not need to react with it to carry it.
- [ ] It has a giant covalent structure that bonds the drug tightly throughout
    - *why wrong:* C₆₀ is a small hollow molecule (simple molecular), not a giant covalent structure, and the drug is carried inside the cage rather than bonded throughout.

**Q9. [reason · CHTH]** Explain why graphite has a high melting point even though its layers can slide over each other easily.
- [✔︎] Melting requires breaking the strong covalent bonds within the layers (high energy), whereas sliding only overcomes the weak forces between layers (low energy)
- [ ] The layers are held together by ionic bonds that are hard to break
    - *why wrong:* The forces BETWEEN layers are weak (so layers slide), but the covalent bonds WITHIN layers are strong (so it melts at a high temperature).
- [ ] The delocalised electrons must all be removed before it melts
    - *why wrong:* There are no ionic bonds in graphite.
- [ ] Graphite does not really have a high melting point
    - *why wrong:* Graphite does have a very high melting point, due to the strong covalent bonds within its layers.

**Q10. [reason · CHTH]** Compare diamond and graphite in terms of the number of bonds each carbon forms and whether they conduct electricity.
- [✔︎] In diamond each carbon forms 4 covalent bonds and it does not conduct; in graphite each carbon forms 3 covalent bonds, leaving a delocalised electron, so it conducts
- [ ] Both form 4 bonds per carbon and both conduct electricity
    - *why wrong:* Only graphite conducts, and only diamond forms 4 bonds — they are not the same.
- [ ] Both form 3 bonds per carbon and neither conducts
    - *why wrong:* Neither statement is right: diamond forms 4 bonds (not 3) and graphite does conduct.
- [ ] Diamond forms 3 bonds and conducts; graphite forms 4 bonds and does not
    - *why wrong:* This swaps them over: diamond forms 4 bonds and does not conduct; graphite forms 3 and does.

### Triple Foundation — 12 questions (3 recall / 9 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why graphite conducts electricity but diamond does not.
- [✔︎] In graphite each carbon uses only 3 of its 4 outer electrons for bonds, leaving one delocalised electron per atom free to move; in diamond all 4 are used in bonds, so none are free
- [ ] Graphite contains more carbon atoms, and more atoms means better conductivity
    - *why wrong:* The number of atoms does not determine conductivity — the availability of free electrons does.
- [ ] Diamond is transparent, so electricity cannot pass through it
    - *why wrong:* Transparency and electrical conductivity are unrelated properties.
- [ ] Graphite has metallic bonding while diamond has ionic bonding
    - *why wrong:* Both diamond and graphite are entirely covalent; neither is metallic or ionic.

**Q2. [reason · CFCHTFTH]** Explain why graphite is used as a lubricant.
- [✔︎] Its carbon atoms form layers held together by weak intermolecular forces, so the layers can slide over each other easily
- [ ] It is smooth because it has no atoms on its surface
    - *why wrong:* All surfaces have atoms; graphite is slippery because its layers slide, not because it lacks surface atoms.
- [ ] It dissolves in water to make a slippery solution
    - *why wrong:* Graphite does not dissolve in water; it is a dry lubricant.
- [ ] It is as hard as diamond, which makes surfaces slippery
    - *why wrong:* Graphite is soft, not hard like diamond; hardness would not make it a lubricant.

**Q3. [reason · CFCHTFTH]** Explain why diamond is very hard and has a very high melting point.
- [✔︎] Every carbon atom is joined to four others by strong covalent bonds throughout a rigid giant 3D lattice, so a great deal of energy is needed to break it
- [ ] Its molecules are held together by strong intermolecular forces
    - *why wrong:* Diamond is not made of separate molecules — it is a giant covalent lattice with no intermolecular forces to speak of.
- [ ] It contains ionic bonds, which are very strong
    - *why wrong:* Diamond is entirely covalent; it contains no ionic bonds.
- [ ] It has delocalised electrons that hold the atoms tightly
    - *why wrong:* Diamond has no delocalised electrons — all four outer electrons of each carbon are in bonds.

**Q4. [apply · CFCHTFTH]** Describe what a giant covalent structure is.
- [✔︎] A structure in which a very large number of atoms are all joined together by covalent bonds throughout
- [ ] A structure made of small, separate molecules
    - *why wrong:* Giant covalent structures have no small separate molecules; the covalent bonding is continuous.
- [ ] A lattice of positive and negative ions
    - *why wrong:* A lattice of ions is an ionic compound, not covalent.
- [ ] A metal with delocalised electrons
    - *why wrong:* A metal with delocalised electrons is a metallic structure, not covalent.

**Q5. [apply · CFCHTFTH]** State why diamond and graphite can both be made of carbon yet have very different properties.
- [✔︎] They are different structural forms (allotropes) of carbon — the atoms are joined in different arrangements
- [ ] They contain different elements
    - *why wrong:* Both are pure carbon — they differ only in how the carbon atoms are arranged.
- [ ] One is a metal and the other is a non-metal
    - *why wrong:* Carbon is a non-metal in both forms; neither is a metal.
- [ ] Diamond contains ions and graphite contains molecules
    - *why wrong:* Both are giant covalent structures — neither contains ions or small molecules.

**Q6. [recall · CFTF]** Describe the structure of graphene and give one of its uses.
- [✔︎] A single layer of graphite, one atom thick; it conducts electricity and can be used in electronics
- [ ] A hollow ball of carbon atoms; used as a lubricant
    - *why wrong:* A hollow ball of carbon atoms describes a fullerene, not graphene.
- [ ] A giant 3D lattice with four bonds per carbon; used in cutting tools
    - *why wrong:* A giant 3D lattice with four bonds per carbon (used in cutting tools) describes diamond, not graphene.
- [ ] A long chain of repeating units; used to make plastic bags
    - *why wrong:* A long chain of repeating units used for plastic bags describes a polymer, not graphene.

**Q7. [recall · CFTF]** Describe the structure of buckminsterfullerene (C₆₀) and give one of its uses.
- [✔︎] A hollow ball (cage) of 60 carbon atoms; it can be used to deliver drugs into the body
- [ ] A single flat sheet of carbon one atom thick; used in electronics
    - *why wrong:* A single flat sheet one atom thick describes graphene, not a fullerene.
- [ ] A giant 3D lattice of carbon; used in cutting tools
    - *why wrong:* A giant 3D lattice used in cutting tools describes diamond, not a hollow fullerene molecule.
- [ ] A regular lattice of positive ions in a sea of electrons; used in wiring
    - *why wrong:* Positive ions in a sea of electrons describes a metal; a fullerene is a covalent carbon molecule.

**Q8. [recall · CFTF]** Describe carbon nanotubes and give one of their uses.
- [✔︎] Cylinders (tubes) of carbon atoms, like rolled-up graphene; they are very strong and are used to reinforce materials
- [ ] Hollow balls of carbon; burned as a fuel for energy
    - *why wrong:* Hollow balls of carbon describe fullerenes, and carbon nanostructures are not burned as a fuel.
- [ ] A soft, slippery form of carbon; used as pencil 'lead'
    - *why wrong:* A soft, slippery carbon used as pencil 'lead' describes graphite, not nanotubes.
- [ ] A giant 3D lattice of carbon; used as a gemstone
    - *why wrong:* A giant 3D lattice used as a gemstone describes diamond, not a nanotube.

**Q9. [apply · CFTF]** Identify a use of diamond that depends on its hardness.
- [✔︎] Tips for cutting tools and drill bits
- [ ] Electrical wiring
    - *why wrong:* Diamond does not conduct electricity, so it is not used for wiring.
- [ ] Pencil 'lead'
    - *why wrong:* Pencil 'lead' and lubrication use graphite (soft, layered), not diamond.
- [ ] Lubricating machine parts
    - *why wrong:* Lubrication uses graphite; diamond is hard, not slippery.

**Q10. [apply · CFTF]** Identify which substance is a giant covalent structure.
- [✔︎] Diamond
- [ ] Sodium chloride
    - *why wrong:* Sodium chloride is a giant ionic lattice.
- [ ] Copper
    - *why wrong:* Copper is a metal (giant metallic structure).
- [ ] Carbon dioxide
    - *why wrong:* Carbon dioxide is a simple molecular substance, not giant covalent.

**Q11. [apply · TF]** State whether diamond conducts electricity, and give a reason.
- [✔︎] No — all four outer electrons of each carbon are used in bonds, so none are free to move
- [ ] Yes — it has delocalised electrons like graphite
    - *why wrong:* Diamond has no free electrons (unlike graphite), so it does not conduct.
- [ ] Yes — because it is made of carbon
    - *why wrong:* Being made of carbon does not guarantee conduction — graphite conducts but diamond does not.
- [ ] Only when it is molten
    - *why wrong:* Diamond does not conduct even when molten; it has no free charge carriers.

**Q12. [apply · TF]** Name the giant covalent form of carbon used for pencil 'lead' and as electrodes.
- [✔︎] Graphite
- [ ] Diamond
    - *why wrong:* Diamond is too hard and does not conduct, so it is not used for pencils or electrodes.
- [ ] Buckminsterfullerene
    - *why wrong:* Buckminsterfullerene is a molecular cage, not the material used for pencil 'lead'.
- [ ] Poly(ethene)
    - *why wrong:* Poly(ethene) is a polymer, not a form of carbon used as electrodes.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why graphite conducts electricity but diamond does not.
- [✔︎] In graphite each carbon uses only 3 of its 4 outer electrons for bonds, leaving one delocalised electron per atom free to move; in diamond all 4 are used in bonds, so none are free
- [ ] Graphite contains more carbon atoms, and more atoms means better conductivity
    - *why wrong:* The number of atoms does not determine conductivity — the availability of free electrons does.
- [ ] Diamond is transparent, so electricity cannot pass through it
    - *why wrong:* Transparency and electrical conductivity are unrelated properties.
- [ ] Graphite has metallic bonding while diamond has ionic bonding
    - *why wrong:* Both diamond and graphite are entirely covalent; neither is metallic or ionic.

**Q2. [reason · CFCHTFTH]** Explain why graphite is used as a lubricant.
- [✔︎] Its carbon atoms form layers held together by weak intermolecular forces, so the layers can slide over each other easily
- [ ] It is smooth because it has no atoms on its surface
    - *why wrong:* All surfaces have atoms; graphite is slippery because its layers slide, not because it lacks surface atoms.
- [ ] It dissolves in water to make a slippery solution
    - *why wrong:* Graphite does not dissolve in water; it is a dry lubricant.
- [ ] It is as hard as diamond, which makes surfaces slippery
    - *why wrong:* Graphite is soft, not hard like diamond; hardness would not make it a lubricant.

**Q3. [reason · CFCHTFTH]** Explain why diamond is very hard and has a very high melting point.
- [✔︎] Every carbon atom is joined to four others by strong covalent bonds throughout a rigid giant 3D lattice, so a great deal of energy is needed to break it
- [ ] Its molecules are held together by strong intermolecular forces
    - *why wrong:* Diamond is not made of separate molecules — it is a giant covalent lattice with no intermolecular forces to speak of.
- [ ] It contains ionic bonds, which are very strong
    - *why wrong:* Diamond is entirely covalent; it contains no ionic bonds.
- [ ] It has delocalised electrons that hold the atoms tightly
    - *why wrong:* Diamond has no delocalised electrons — all four outer electrons of each carbon are in bonds.

**Q4. [apply · CFCHTFTH]** Describe what a giant covalent structure is.
- [✔︎] A structure in which a very large number of atoms are all joined together by covalent bonds throughout
- [ ] A structure made of small, separate molecules
    - *why wrong:* Giant covalent structures have no small separate molecules; the covalent bonding is continuous.
- [ ] A lattice of positive and negative ions
    - *why wrong:* A lattice of ions is an ionic compound, not covalent.
- [ ] A metal with delocalised electrons
    - *why wrong:* A metal with delocalised electrons is a metallic structure, not covalent.

**Q5. [apply · CFCHTFTH]** State why diamond and graphite can both be made of carbon yet have very different properties.
- [✔︎] They are different structural forms (allotropes) of carbon — the atoms are joined in different arrangements
- [ ] They contain different elements
    - *why wrong:* Both are pure carbon — they differ only in how the carbon atoms are arranged.
- [ ] One is a metal and the other is a non-metal
    - *why wrong:* Carbon is a non-metal in both forms; neither is a metal.
- [ ] Diamond contains ions and graphite contains molecules
    - *why wrong:* Both are giant covalent structures — neither contains ions or small molecules.

**Q6. [reason · CHTH]** Explain why silicon dioxide (found in sand and quartz) has a very high melting point.
- [✔︎] It is a giant covalent structure in which many strong Si–O covalent bonds must be broken to melt it
- [ ] It is an ionic compound with strong forces between ions
    - *why wrong:* Silicon dioxide is giant covalent, not ionic.
- [ ] It is a simple molecule with strong intermolecular forces
    - *why wrong:* It is not a simple molecule — the covalent bonding runs throughout the whole structure.
- [ ] It is a metal with strong metallic bonds
    - *why wrong:* Silicon dioxide is not a metal.

**Q7. [reason · CHTH]** Graphene is a single layer of graphite. Explain why it conducts electricity and is very strong.
- [✔︎] Each carbon is covalently bonded to three others in a strong hexagonal network, and the fourth outer electron of each carbon is delocalised, so it can carry charge
- [ ] It contains free-moving ions that carry charge
    - *why wrong:* Graphene has no ions; conduction is by delocalised electrons.
- [ ] It is a metal, so it conducts and is strong
    - *why wrong:* Graphene is a form of carbon (covalent), not a metal.
- [ ] Its molecules are held together by strong intermolecular forces
    - *why wrong:* Graphene is a giant covalent sheet, not separate molecules with intermolecular forces.

**Q8. [reason · CHTH]** Explain why buckminsterfullerene (C₆₀) can be used to deliver drugs to specific parts of the body.
- [✔︎] Its molecules are hollow cages, so a drug molecule can be carried inside and released where it is needed
- [ ] It is a metal, so the drug is carried on its surface by delocalised electrons
    - *why wrong:* C₆₀ is a covalent carbon molecule, not a metal, so it has no delocalised-electron surface to carry a drug this way.
- [ ] It reacts with the drug to form a new compound that dissolves in the blood
    - *why wrong:* The drug is held physically inside the hollow cage; C₆₀ does not need to react with it to carry it.
- [ ] It has a giant covalent structure that bonds the drug tightly throughout
    - *why wrong:* C₆₀ is a small hollow molecule (simple molecular), not a giant covalent structure, and the drug is carried inside the cage rather than bonded throughout.

**Q9. [reason · CHTH]** Explain why graphite has a high melting point even though its layers can slide over each other easily.
- [✔︎] Melting requires breaking the strong covalent bonds within the layers (high energy), whereas sliding only overcomes the weak forces between layers (low energy)
- [ ] The layers are held together by ionic bonds that are hard to break
    - *why wrong:* The forces BETWEEN layers are weak (so layers slide), but the covalent bonds WITHIN layers are strong (so it melts at a high temperature).
- [ ] The delocalised electrons must all be removed before it melts
    - *why wrong:* There are no ionic bonds in graphite.
- [ ] Graphite does not really have a high melting point
    - *why wrong:* Graphite does have a very high melting point, due to the strong covalent bonds within its layers.

**Q10. [reason · CHTH]** Compare diamond and graphite in terms of the number of bonds each carbon forms and whether they conduct electricity.
- [✔︎] In diamond each carbon forms 4 covalent bonds and it does not conduct; in graphite each carbon forms 3 covalent bonds, leaving a delocalised electron, so it conducts
- [ ] Both form 4 bonds per carbon and both conduct electricity
    - *why wrong:* Only graphite conducts, and only diamond forms 4 bonds — they are not the same.
- [ ] Both form 3 bonds per carbon and neither conducts
    - *why wrong:* Neither statement is right: diamond forms 4 bonds (not 3) and graphite does conduct.
- [ ] Diamond forms 3 bonds and conducts; graphite forms 4 bonds and does not
    - *why wrong:* This swaps them over: diamond forms 4 bonds and does not conduct; graphite forms 3 and does.

**Q11. [suggest · TH]** Carbon nanotubes are rolled sheets of graphene. Suggest why they are useful both for reinforcing materials and in electronics.
- [✔︎] They are very strong along their length (strong covalent network) and they conduct electricity (delocalised electrons), so they can reinforce materials and carry current
- [ ] They are soft and flexible, which helps them conduct
    - *why wrong:* Nanotubes are strong (not soft) and conduct because of delocalised electrons, not because they are soft.
- [ ] They are ionic, so they conduct and are strong
    - *why wrong:* Nanotubes are covalent carbon, not ionic.
- [ ] They dissolve in water to strengthen materials
    - *why wrong:* Nanotubes do not dissolve in water; their strength comes from their covalent structure.

**Q12. [reason · TH]** Explain why graphene is described as both extremely strong and an excellent electrical conductor, in terms of its bonding.
- [✔︎] Each carbon is covalently bonded to three others in a strong two-dimensional network (strength), while the fourth outer electron of each carbon is delocalised across the sheet (conductivity)
- [ ] It has strong ionic bonds and free ions
    - *why wrong:* Graphene has no ionic bonds or free ions; its strength is covalent and its conductivity is from delocalised electrons.
- [ ] It is a metal with a giant metallic lattice
    - *why wrong:* Graphene is a covalent form of carbon, not a metal.
- [ ] It has weak intermolecular forces that let electrons flow
    - *why wrong:* Its conductivity comes from delocalised electrons, not from weak intermolecular forces.


---

## Properties of Metals and Alloys  ·  `metals-alloys`  ·  AQA 5.2.2.7-5.2.2.8

> 🚩 **Triple-depth call (your review):** MATCHED — AQA 5.2.2.7-8 (metals and alloys) is identical for Combined and Triple. Foundation difficulty is the same across both pathways. The alloy and delocalised-electron reasoning is a genuine Foundation→Higher lift. No AQA Triple-only content on this page.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often think that because ionic compounds only conduct when molten, metals must be the same. They are not: a metal conducts in the solid state because its delocalised electrons are already free to move. Ionic compounds cannot conduct as solids because their charge carriers are ions, which stay locked in place until the compound melts or dissolves.

**Question sets by tier** (each item shows tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (3 recall / 7 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why metals can conduct electricity in the solid state, but ionic compounds cannot.
- [✔︎] Metals have delocalised electrons that are free to move even when solid; in an ionic solid the ions are locked in fixed positions and cannot move
- [ ] Metal atoms are smaller than ions, so they move more easily through the solid
    - *why wrong:* Atom or ion size is not the reason — it is the availability of free-moving charge carriers.
- [ ] Metals have more protons, which makes them better at conducting
    - *why wrong:* Proton number does not determine conductivity; many non-metals have lots of protons but do not conduct.
- [ ] Ionic bonds are stronger, which stops any particle from moving
    - *why wrong:* Ionic compounds CAN conduct when molten (ions freed); the issue in the solid is fixed ions, not stronger bonds.

**Q2. [reason · CFCHTFTH]** Explain why brass (copper mixed with zinc) is harder than pure copper.
- [✔︎] The zinc atoms are a different size to the copper atoms, so they distort the regular lattice and stop the layers of atoms sliding over each other
- [ ] Brass has more metallic bonds than copper, and more bonds means harder
    - *why wrong:* More bonds does not necessarily mean harder — the hardening is due to lattice disruption preventing layers sliding.
- [ ] Zinc is a harder metal, so mixing it in makes the product hard
    - *why wrong:* The key mechanism is disrupting the regular copper lattice with differently-sized atoms, not zinc's own hardness.
- [ ] Brass has been purified, and pure metals are always harder
    - *why wrong:* Brass is a mixture (less pure than copper); it is the added, differently-sized atoms that harden it.

**Q3. [reason · CFCHTFTH]** Explain why metals are good conductors of heat.
- [✔︎] The delocalised electrons are free to move and quickly transfer thermal energy through the structure
- [ ] The positive ions carry the heat as they move around
    - *why wrong:* The positive ions are fixed and only vibrate; the mobile delocalised electrons carry most of the heat.
- [ ] Metals contain water that spreads the heat
    - *why wrong:* Metals do not contain water; heat is carried by the delocalised electrons.
- [ ] The covalent bonds pass the heat along
    - *why wrong:* Metals have no covalent bonds; heat is transferred by the electron sea.

**Q4. [apply · CFCHTFTH]** Describe the difference in structure between a pure metal and one of its alloys.
- [✔︎] A pure metal has a regular lattice of same-sized atoms; an alloy has atoms of different sizes that distort the regular arrangement
- [ ] A pure metal contains ions but an alloy contains only atoms
    - *why wrong:* Both have positive ions and a sea of electrons; the difference is that the alloy has differently-sized atoms.
- [ ] A pure metal is molecular but an alloy is a giant lattice
    - *why wrong:* Both are giant metallic structures, not molecular.
- [ ] A pure metal has no bonding but an alloy has metallic bonding
    - *why wrong:* Both are held by metallic bonding; the difference is the mix of atom sizes.

**Q5. [apply · CFCHTFTH]** Explain why pure metals are often too soft for use, so alloys are made instead.
- [✔︎] In a pure metal the layers of same-sized atoms can slide over each other easily, making it soft; alloying adds differently-sized atoms that stop the layers sliding
- [ ] Pure metals contain no metallic bonds, so they fall apart
    - *why wrong:* Pure metals do have metallic bonding; they are soft because their identical-sized atoms let layers slide.
- [ ] Pure metals are always liquids at room temperature
    - *why wrong:* Most pure metals are solid at room temperature; they are simply soft.
- [ ] Pure metals have too many delocalised electrons to be strong
    - *why wrong:* The number of delocalised electrons is not the reason; sliding layers of identical atoms is.

**Q6. [recall · CFTF]** Name the type of structure that a metal has.
- [✔︎] A giant metallic structure (lattice)
- [ ] A simple molecular structure
    - *why wrong:* Metals are giant metallic structures, not made of small molecules.
- [ ] A giant ionic lattice
    - *why wrong:* A giant ionic lattice has positive and negative ions; a metal has positive ions and an electron sea.
- [ ] A single small molecule
    - *why wrong:* A metal is a giant structure, not one small molecule.

**Q7. [recall · CFTF]** State what an alloy is.
- [✔︎] A mixture of a metal with one or more other elements
- [ ] A very pure sample of a single metal
    - *why wrong:* A pure single metal is the opposite of an alloy.
- [ ] A compound of a metal and a non-metal
    - *why wrong:* An alloy is a mixture, not a chemically bonded compound.
- [ ] A metal that has had all its electrons removed
    - *why wrong:* Metals in an alloy keep their delocalised electrons.

**Q8. [apply · CFTF]** Identify a use of copper that depends on it being a good electrical conductor.
- [✔︎] Electrical wiring
- [ ] Making window glass
    - *why wrong:* Window glass is not a metal and is not chosen for conductivity.
- [ ] As a fuel for burning
    - *why wrong:* Copper is not used as a fuel.
- [ ] As a fertiliser
    - *why wrong:* Copper is not used as a fertiliser; wiring uses its high conductivity.

**Q9. [apply · CFTF]** Identify the correct description of steel.
- [✔︎] Iron mixed with a small amount of carbon
- [ ] Pure iron with nothing added
    - *why wrong:* Steel is an ALLOY — pure iron with nothing added is not steel.
- [ ] Copper mixed with zinc
    - *why wrong:* Copper mixed with zinc is brass, not steel.
- [ ] A non-metal element
    - *why wrong:* Steel is a metal alloy, not a non-metal element.

**Q10. [recall · CFTF]** State whether metals are malleable or brittle.
- [✔︎] Malleable — they can be hammered into shape
- [ ] Brittle — they shatter when struck
    - *why wrong:* Brittleness is a property of ionic compounds; metals bend rather than shatter.
- [ ] Neither — they are liquids
    - *why wrong:* Most metals are solid at room temperature, not liquid.
- [ ] Both equally
    - *why wrong:* Metals are clearly malleable, not brittle.

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why metals can conduct electricity in the solid state, but ionic compounds cannot.
- [✔︎] Metals have delocalised electrons that are free to move even when solid; in an ionic solid the ions are locked in fixed positions and cannot move
- [ ] Metal atoms are smaller than ions, so they move more easily through the solid
    - *why wrong:* Atom or ion size is not the reason — it is the availability of free-moving charge carriers.
- [ ] Metals have more protons, which makes them better at conducting
    - *why wrong:* Proton number does not determine conductivity; many non-metals have lots of protons but do not conduct.
- [ ] Ionic bonds are stronger, which stops any particle from moving
    - *why wrong:* Ionic compounds CAN conduct when molten (ions freed); the issue in the solid is fixed ions, not stronger bonds.

**Q2. [reason · CFCHTFTH]** Explain why brass (copper mixed with zinc) is harder than pure copper.
- [✔︎] The zinc atoms are a different size to the copper atoms, so they distort the regular lattice and stop the layers of atoms sliding over each other
- [ ] Brass has more metallic bonds than copper, and more bonds means harder
    - *why wrong:* More bonds does not necessarily mean harder — the hardening is due to lattice disruption preventing layers sliding.
- [ ] Zinc is a harder metal, so mixing it in makes the product hard
    - *why wrong:* The key mechanism is disrupting the regular copper lattice with differently-sized atoms, not zinc's own hardness.
- [ ] Brass has been purified, and pure metals are always harder
    - *why wrong:* Brass is a mixture (less pure than copper); it is the added, differently-sized atoms that harden it.

**Q3. [reason · CFCHTFTH]** Explain why metals are good conductors of heat.
- [✔︎] The delocalised electrons are free to move and quickly transfer thermal energy through the structure
- [ ] The positive ions carry the heat as they move around
    - *why wrong:* The positive ions are fixed and only vibrate; the mobile delocalised electrons carry most of the heat.
- [ ] Metals contain water that spreads the heat
    - *why wrong:* Metals do not contain water; heat is carried by the delocalised electrons.
- [ ] The covalent bonds pass the heat along
    - *why wrong:* Metals have no covalent bonds; heat is transferred by the electron sea.

**Q4. [apply · CFCHTFTH]** Describe the difference in structure between a pure metal and one of its alloys.
- [✔︎] A pure metal has a regular lattice of same-sized atoms; an alloy has atoms of different sizes that distort the regular arrangement
- [ ] A pure metal contains ions but an alloy contains only atoms
    - *why wrong:* Both have positive ions and a sea of electrons; the difference is that the alloy has differently-sized atoms.
- [ ] A pure metal is molecular but an alloy is a giant lattice
    - *why wrong:* Both are giant metallic structures, not molecular.
- [ ] A pure metal has no bonding but an alloy has metallic bonding
    - *why wrong:* Both are held by metallic bonding; the difference is the mix of atom sizes.

**Q5. [apply · CFCHTFTH]** Explain why pure metals are often too soft for use, so alloys are made instead.
- [✔︎] In a pure metal the layers of same-sized atoms can slide over each other easily, making it soft; alloying adds differently-sized atoms that stop the layers sliding
- [ ] Pure metals contain no metallic bonds, so they fall apart
    - *why wrong:* Pure metals do have metallic bonding; they are soft because their identical-sized atoms let layers slide.
- [ ] Pure metals are always liquids at room temperature
    - *why wrong:* Most pure metals are solid at room temperature; they are simply soft.
- [ ] Pure metals have too many delocalised electrons to be strong
    - *why wrong:* The number of delocalised electrons is not the reason; sliding layers of identical atoms is.

**Q6. [reason · CHTH]** Explain, in terms of particles, why metals conduct electricity and heat but simple molecular substances do not.
- [✔︎] Metals contain delocalised electrons that are free to move and carry charge and thermal energy; simple molecular substances have no free electrons or ions
- [ ] Metals contain free ions but molecules do not
    - *why wrong:* Metals conduct via delocalised electrons, not free ions (ions are fixed in a solid metal).
- [ ] Metals have stronger covalent bonds than molecules
    - *why wrong:* Metals have no covalent bonds; conduction is due to the electron sea.
- [ ] Simple molecular substances have delocalised electrons that are fixed
    - *why wrong:* Simple molecular substances have no delocalised electrons at all.

**Q7. [suggest · CHTH]** Stainless steel is used to make cutlery. Suggest two properties that make it suitable and relate them to its structure.
- [✔︎] It is hard and strong (differently-sized atoms disrupt the lattice so layers cannot slide) and it resists corrosion
- [ ] It is soft and brittle, so it can be shaped and snapped
    - *why wrong:* Soft, brittle cutlery would be useless; stainless steel is hard and strong because of its alloy structure.
- [ ] It has a low melting point, so it melts clean
    - *why wrong:* A low melting point would be a disadvantage for cutlery.
- [ ] It is a good insulator, so it is safe to hold
    - *why wrong:* Being a conductor or insulator is not the key reason cutlery is made from stainless steel.

**Q8. [reason · CHTH]** Explain why an alloy is generally harder than the pure metal it is made from, using the idea of layers of atoms.
- [✔︎] The different-sized atoms in the alloy distort the regular layers, so the layers can no longer slide over each other easily
- [ ] The alloy has weaker metallic bonds, which makes it more rigid
    - *why wrong:* Weaker bonds would make it softer, not harder; the hardening is due to lattice distortion.
- [ ] The alloy contains ionic bonds that hold it firmly
    - *why wrong:* Alloys are still held by metallic bonding, not ionic bonds.
- [ ] The alloy has fewer delocalised electrons, so it is stronger
    - *why wrong:* The number of delocalised electrons is not the reason; disrupting the layers is.

**Q9. [suggest · CHTH]** Aluminium is used for aircraft bodies. Suggest why an aluminium alloy is used rather than pure aluminium.
- [✔︎] The alloy is much stronger and harder than pure aluminium while still having a low density, so the aircraft is strong but light
- [ ] Pure aluminium is a better conductor, which is dangerous in flight
    - *why wrong:* Conductivity is not the reason; the alloy is chosen because it is stronger while remaining light.
- [ ] The alloy is cheaper because it contains no aluminium
    - *why wrong:* Aluminium alloys still contain mostly aluminium.
- [ ] Pure aluminium is a gas at room temperature
    - *why wrong:* Aluminium is a solid metal at room temperature.

**Q10. [reason · CHTH]** Explain why metals are malleable but ionic compounds are brittle, in terms of what happens when the layers move.
- [✔︎] In a metal the layers of ions slide and the electron sea keeps them bonded, so it bends; in an ionic solid, shifting the layers brings like charges together, which repel and split the crystal
- [ ] Both bend, but metals bend more quickly
    - *why wrong:* Ionic compounds do not bend at all — they shatter, because of ion repulsion when layers shift.
- [ ] Metals contain covalent bonds that flex; ionic compounds do not
    - *why wrong:* Metals have no covalent bonds; malleability comes from the sliding layers held by the electron sea.
- [ ] Ionic compounds contain delocalised electrons that snap
    - *why wrong:* Ionic compounds have no delocalised electrons; that is a metallic feature.

### Triple Foundation — 12 questions (3 recall / 9 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why metals can conduct electricity in the solid state, but ionic compounds cannot.
- [✔︎] Metals have delocalised electrons that are free to move even when solid; in an ionic solid the ions are locked in fixed positions and cannot move
- [ ] Metal atoms are smaller than ions, so they move more easily through the solid
    - *why wrong:* Atom or ion size is not the reason — it is the availability of free-moving charge carriers.
- [ ] Metals have more protons, which makes them better at conducting
    - *why wrong:* Proton number does not determine conductivity; many non-metals have lots of protons but do not conduct.
- [ ] Ionic bonds are stronger, which stops any particle from moving
    - *why wrong:* Ionic compounds CAN conduct when molten (ions freed); the issue in the solid is fixed ions, not stronger bonds.

**Q2. [reason · CFCHTFTH]** Explain why brass (copper mixed with zinc) is harder than pure copper.
- [✔︎] The zinc atoms are a different size to the copper atoms, so they distort the regular lattice and stop the layers of atoms sliding over each other
- [ ] Brass has more metallic bonds than copper, and more bonds means harder
    - *why wrong:* More bonds does not necessarily mean harder — the hardening is due to lattice disruption preventing layers sliding.
- [ ] Zinc is a harder metal, so mixing it in makes the product hard
    - *why wrong:* The key mechanism is disrupting the regular copper lattice with differently-sized atoms, not zinc's own hardness.
- [ ] Brass has been purified, and pure metals are always harder
    - *why wrong:* Brass is a mixture (less pure than copper); it is the added, differently-sized atoms that harden it.

**Q3. [reason · CFCHTFTH]** Explain why metals are good conductors of heat.
- [✔︎] The delocalised electrons are free to move and quickly transfer thermal energy through the structure
- [ ] The positive ions carry the heat as they move around
    - *why wrong:* The positive ions are fixed and only vibrate; the mobile delocalised electrons carry most of the heat.
- [ ] Metals contain water that spreads the heat
    - *why wrong:* Metals do not contain water; heat is carried by the delocalised electrons.
- [ ] The covalent bonds pass the heat along
    - *why wrong:* Metals have no covalent bonds; heat is transferred by the electron sea.

**Q4. [apply · CFCHTFTH]** Describe the difference in structure between a pure metal and one of its alloys.
- [✔︎] A pure metal has a regular lattice of same-sized atoms; an alloy has atoms of different sizes that distort the regular arrangement
- [ ] A pure metal contains ions but an alloy contains only atoms
    - *why wrong:* Both have positive ions and a sea of electrons; the difference is that the alloy has differently-sized atoms.
- [ ] A pure metal is molecular but an alloy is a giant lattice
    - *why wrong:* Both are giant metallic structures, not molecular.
- [ ] A pure metal has no bonding but an alloy has metallic bonding
    - *why wrong:* Both are held by metallic bonding; the difference is the mix of atom sizes.

**Q5. [apply · CFCHTFTH]** Explain why pure metals are often too soft for use, so alloys are made instead.
- [✔︎] In a pure metal the layers of same-sized atoms can slide over each other easily, making it soft; alloying adds differently-sized atoms that stop the layers sliding
- [ ] Pure metals contain no metallic bonds, so they fall apart
    - *why wrong:* Pure metals do have metallic bonding; they are soft because their identical-sized atoms let layers slide.
- [ ] Pure metals are always liquids at room temperature
    - *why wrong:* Most pure metals are solid at room temperature; they are simply soft.
- [ ] Pure metals have too many delocalised electrons to be strong
    - *why wrong:* The number of delocalised electrons is not the reason; sliding layers of identical atoms is.

**Q6. [recall · CFTF]** Name the type of structure that a metal has.
- [✔︎] A giant metallic structure (lattice)
- [ ] A simple molecular structure
    - *why wrong:* Metals are giant metallic structures, not made of small molecules.
- [ ] A giant ionic lattice
    - *why wrong:* A giant ionic lattice has positive and negative ions; a metal has positive ions and an electron sea.
- [ ] A single small molecule
    - *why wrong:* A metal is a giant structure, not one small molecule.

**Q7. [recall · CFTF]** State what an alloy is.
- [✔︎] A mixture of a metal with one or more other elements
- [ ] A very pure sample of a single metal
    - *why wrong:* A pure single metal is the opposite of an alloy.
- [ ] A compound of a metal and a non-metal
    - *why wrong:* An alloy is a mixture, not a chemically bonded compound.
- [ ] A metal that has had all its electrons removed
    - *why wrong:* Metals in an alloy keep their delocalised electrons.

**Q8. [apply · CFTF]** Identify a use of copper that depends on it being a good electrical conductor.
- [✔︎] Electrical wiring
- [ ] Making window glass
    - *why wrong:* Window glass is not a metal and is not chosen for conductivity.
- [ ] As a fuel for burning
    - *why wrong:* Copper is not used as a fuel.
- [ ] As a fertiliser
    - *why wrong:* Copper is not used as a fertiliser; wiring uses its high conductivity.

**Q9. [apply · CFTF]** Identify the correct description of steel.
- [✔︎] Iron mixed with a small amount of carbon
- [ ] Pure iron with nothing added
    - *why wrong:* Steel is an ALLOY — pure iron with nothing added is not steel.
- [ ] Copper mixed with zinc
    - *why wrong:* Copper mixed with zinc is brass, not steel.
- [ ] A non-metal element
    - *why wrong:* Steel is a metal alloy, not a non-metal element.

**Q10. [recall · CFTF]** State whether metals are malleable or brittle.
- [✔︎] Malleable — they can be hammered into shape
- [ ] Brittle — they shatter when struck
    - *why wrong:* Brittleness is a property of ionic compounds; metals bend rather than shatter.
- [ ] Neither — they are liquids
    - *why wrong:* Most metals are solid at room temperature, not liquid.
- [ ] Both equally
    - *why wrong:* Metals are clearly malleable, not brittle.

**Q11. [apply · TF]** Identify the property that makes copper suitable for the base of a saucepan.
- [✔︎] It is a good conductor of heat
- [ ] It is a good electrical insulator
    - *why wrong:* An insulator would be poor for a saucepan base; copper is chosen for good heat conduction.
- [ ] It has a very low melting point
    - *why wrong:* A very low melting point would be dangerous in cooking.
- [ ] It is brittle
    - *why wrong:* Brittleness would make the pan shatter; copper is malleable and conducts heat well.

**Q12. [apply · TF]** Name the two metals mixed together to make bronze.
- [✔︎] Copper and tin
- [ ] Copper and zinc
    - *why wrong:* Copper and zinc make brass, not bronze.
- [ ] Iron and carbon
    - *why wrong:* Iron and carbon make steel.
- [ ] Iron and chromium
    - *why wrong:* Iron and chromium (with nickel) make stainless steel.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain why metals can conduct electricity in the solid state, but ionic compounds cannot.
- [✔︎] Metals have delocalised electrons that are free to move even when solid; in an ionic solid the ions are locked in fixed positions and cannot move
- [ ] Metal atoms are smaller than ions, so they move more easily through the solid
    - *why wrong:* Atom or ion size is not the reason — it is the availability of free-moving charge carriers.
- [ ] Metals have more protons, which makes them better at conducting
    - *why wrong:* Proton number does not determine conductivity; many non-metals have lots of protons but do not conduct.
- [ ] Ionic bonds are stronger, which stops any particle from moving
    - *why wrong:* Ionic compounds CAN conduct when molten (ions freed); the issue in the solid is fixed ions, not stronger bonds.

**Q2. [reason · CFCHTFTH]** Explain why brass (copper mixed with zinc) is harder than pure copper.
- [✔︎] The zinc atoms are a different size to the copper atoms, so they distort the regular lattice and stop the layers of atoms sliding over each other
- [ ] Brass has more metallic bonds than copper, and more bonds means harder
    - *why wrong:* More bonds does not necessarily mean harder — the hardening is due to lattice disruption preventing layers sliding.
- [ ] Zinc is a harder metal, so mixing it in makes the product hard
    - *why wrong:* The key mechanism is disrupting the regular copper lattice with differently-sized atoms, not zinc's own hardness.
- [ ] Brass has been purified, and pure metals are always harder
    - *why wrong:* Brass is a mixture (less pure than copper); it is the added, differently-sized atoms that harden it.

**Q3. [reason · CFCHTFTH]** Explain why metals are good conductors of heat.
- [✔︎] The delocalised electrons are free to move and quickly transfer thermal energy through the structure
- [ ] The positive ions carry the heat as they move around
    - *why wrong:* The positive ions are fixed and only vibrate; the mobile delocalised electrons carry most of the heat.
- [ ] Metals contain water that spreads the heat
    - *why wrong:* Metals do not contain water; heat is carried by the delocalised electrons.
- [ ] The covalent bonds pass the heat along
    - *why wrong:* Metals have no covalent bonds; heat is transferred by the electron sea.

**Q4. [apply · CFCHTFTH]** Describe the difference in structure between a pure metal and one of its alloys.
- [✔︎] A pure metal has a regular lattice of same-sized atoms; an alloy has atoms of different sizes that distort the regular arrangement
- [ ] A pure metal contains ions but an alloy contains only atoms
    - *why wrong:* Both have positive ions and a sea of electrons; the difference is that the alloy has differently-sized atoms.
- [ ] A pure metal is molecular but an alloy is a giant lattice
    - *why wrong:* Both are giant metallic structures, not molecular.
- [ ] A pure metal has no bonding but an alloy has metallic bonding
    - *why wrong:* Both are held by metallic bonding; the difference is the mix of atom sizes.

**Q5. [apply · CFCHTFTH]** Explain why pure metals are often too soft for use, so alloys are made instead.
- [✔︎] In a pure metal the layers of same-sized atoms can slide over each other easily, making it soft; alloying adds differently-sized atoms that stop the layers sliding
- [ ] Pure metals contain no metallic bonds, so they fall apart
    - *why wrong:* Pure metals do have metallic bonding; they are soft because their identical-sized atoms let layers slide.
- [ ] Pure metals are always liquids at room temperature
    - *why wrong:* Most pure metals are solid at room temperature; they are simply soft.
- [ ] Pure metals have too many delocalised electrons to be strong
    - *why wrong:* The number of delocalised electrons is not the reason; sliding layers of identical atoms is.

**Q6. [reason · CHTH]** Explain, in terms of particles, why metals conduct electricity and heat but simple molecular substances do not.
- [✔︎] Metals contain delocalised electrons that are free to move and carry charge and thermal energy; simple molecular substances have no free electrons or ions
- [ ] Metals contain free ions but molecules do not
    - *why wrong:* Metals conduct via delocalised electrons, not free ions (ions are fixed in a solid metal).
- [ ] Metals have stronger covalent bonds than molecules
    - *why wrong:* Metals have no covalent bonds; conduction is due to the electron sea.
- [ ] Simple molecular substances have delocalised electrons that are fixed
    - *why wrong:* Simple molecular substances have no delocalised electrons at all.

**Q7. [suggest · CHTH]** Stainless steel is used to make cutlery. Suggest two properties that make it suitable and relate them to its structure.
- [✔︎] It is hard and strong (differently-sized atoms disrupt the lattice so layers cannot slide) and it resists corrosion
- [ ] It is soft and brittle, so it can be shaped and snapped
    - *why wrong:* Soft, brittle cutlery would be useless; stainless steel is hard and strong because of its alloy structure.
- [ ] It has a low melting point, so it melts clean
    - *why wrong:* A low melting point would be a disadvantage for cutlery.
- [ ] It is a good insulator, so it is safe to hold
    - *why wrong:* Being a conductor or insulator is not the key reason cutlery is made from stainless steel.

**Q8. [reason · CHTH]** Explain why an alloy is generally harder than the pure metal it is made from, using the idea of layers of atoms.
- [✔︎] The different-sized atoms in the alloy distort the regular layers, so the layers can no longer slide over each other easily
- [ ] The alloy has weaker metallic bonds, which makes it more rigid
    - *why wrong:* Weaker bonds would make it softer, not harder; the hardening is due to lattice distortion.
- [ ] The alloy contains ionic bonds that hold it firmly
    - *why wrong:* Alloys are still held by metallic bonding, not ionic bonds.
- [ ] The alloy has fewer delocalised electrons, so it is stronger
    - *why wrong:* The number of delocalised electrons is not the reason; disrupting the layers is.

**Q9. [suggest · CHTH]** Aluminium is used for aircraft bodies. Suggest why an aluminium alloy is used rather than pure aluminium.
- [✔︎] The alloy is much stronger and harder than pure aluminium while still having a low density, so the aircraft is strong but light
- [ ] Pure aluminium is a better conductor, which is dangerous in flight
    - *why wrong:* Conductivity is not the reason; the alloy is chosen because it is stronger while remaining light.
- [ ] The alloy is cheaper because it contains no aluminium
    - *why wrong:* Aluminium alloys still contain mostly aluminium.
- [ ] Pure aluminium is a gas at room temperature
    - *why wrong:* Aluminium is a solid metal at room temperature.

**Q10. [reason · CHTH]** Explain why metals are malleable but ionic compounds are brittle, in terms of what happens when the layers move.
- [✔︎] In a metal the layers of ions slide and the electron sea keeps them bonded, so it bends; in an ionic solid, shifting the layers brings like charges together, which repel and split the crystal
- [ ] Both bend, but metals bend more quickly
    - *why wrong:* Ionic compounds do not bend at all — they shatter, because of ion repulsion when layers shift.
- [ ] Metals contain covalent bonds that flex; ionic compounds do not
    - *why wrong:* Metals have no covalent bonds; malleability comes from the sliding layers held by the electron sea.
- [ ] Ionic compounds contain delocalised electrons that snap
    - *why wrong:* Ionic compounds have no delocalised electrons; that is a metallic feature.

**Q11. [reason · TH]** Explain why steel is more useful than pure iron for constructing buildings and bridges, linking its hardness to the arrangement of its atoms.
- [✔︎] The carbon atoms in steel are a different size to the iron atoms, disrupting the regular lattice so the layers cannot slide; this makes steel much harder and stronger, so it can bear heavy loads
- [ ] Steel is purer than iron, and pure metals bear more load
    - *why wrong:* Steel is LESS pure than iron (carbon added); it is the differently-sized carbon atoms disrupting the lattice that harden it.
- [ ] Steel contains ionic bonds that make it rigid
    - *why wrong:* Steel is held by metallic bonding, not ionic bonds.
- [ ] Steel is lighter than iron because it contains carbon
    - *why wrong:* The reason steel is chosen is its hardness and strength from lattice disruption, not a large weight saving.

**Q12. [reason · TH]** Explain why a metal's electrical conductivity and its thermal conductivity both depend on the same feature of its structure.
- [✔︎] Both rely on the delocalised electrons: they move to carry electric charge and also transfer thermal energy quickly through the structure
- [ ] Both rely on the positive ions moving through the metal
    - *why wrong:* The positive ions are fixed and only vibrate; it is the delocalised electrons that carry both charge and heat.
- [ ] Both rely on covalent bonds passing energy along
    - *why wrong:* Metals have no covalent bonds; the electron sea carries both current and heat.
- [ ] Both rely on the metal being an ionic lattice
    - *why wrong:* Metals are metallic, not ionic, structures.


---

## Nanoparticles  ·  `nanoparticles`  ·  AQA 5.2.3.3

> 🚩 **Triple-depth call (your review):** TRIPLE-ONLY page (AQA 5.2.3 is not in Combined Science) — so this page exists only in the two Triple files, and there is no Combined comparison to make. Genuine Triple depth: the surface-area-to-volume-ratio calculation is the ONE FIFA (worked-example) page in the whole Bonding unit. Triple-Foundation and Triple-Higher FIFA use different numbers and demands (Foundation: plug whole-number cubes into SA÷V; Higher: the 6÷L relationship, the nanoscale, the nm⁻¹ unit, comparison and a rearrangement). ⚠️ The audit WILL show a 'no interactive practice mode' MAJOR on this page for both tiers — that is systemic (the current template renders static FIFA steps only) and is the redesign port's job (MRB-113), not a content defect. ⭐ All FIFA and the quantitative quiz items are flagged for your full review.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often think that a nanoparticle of gold must be a different substance from ordinary gold because its colour and reactivity are so different. It is the same substance — the same gold atoms. What changes is the scale: nanoparticles have a far larger surface-area-to-volume ratio, so a much greater fraction of their atoms sit on the surface, which changes their properties.

**Question sets by tier** (each item shows tiers it appears in; ⭐ = full-review flag):

### Triple Foundation — 10 questions (2 recall / 8 apply+reason+calc)

**Q1. [reason · TFTH]** Explain why nanoparticles have different properties from the same material in bulk (large-scale) form.
- [✔︎] They have a much larger surface-area-to-volume ratio, so a greater fraction of their atoms are on the surface and available to take part in reactions
- [ ] They are made of different atoms from the bulk material
    - *why wrong:* Nanoparticles are made of the SAME atoms as the bulk material — it is the scale that changes the properties.
- [ ] They have weaker chemical bonds than the bulk material
    - *why wrong:* The bonds are the same type as in the bulk; what differs is the fraction of atoms on the surface.
- [ ] They are always more stable than the bulk material
    - *why wrong:* Nanoparticles are often MORE reactive (so less stable in some ways), not simply more stable.

**Q2. [suggest · TFTH]** Suggest why nanoparticles may pose a greater health risk than the same material in larger particle form.
- [✔︎] Their very small size may let them pass through cell membranes and into cells, and their long-term effects are not yet fully understood
- [ ] They are more toxic because they contain more of the harmful material
    - *why wrong:* A nanoparticle contains LESS material than a larger particle — the concern is its size and reactivity, not the amount.
- [ ] They are heavier, so they stay in the lungs longer
    - *why wrong:* Nanoparticles are lighter than larger particles; the concern is that their small size lets them penetrate the body.
- [ ] They react with water in the body to make dangerous chemicals
    - *why wrong:* The main concern is their ability to penetrate cells because of their size, not a specific reaction with water.

**Q3. [reason · TFTH]** Describe what happens to a particle's surface-area-to-volume ratio as the particle gets smaller.
- [✔︎] The ratio increases — smaller particles have a greater surface area compared with their volume
- [ ] The ratio decreases as the particle gets smaller
    - *why wrong:* Smaller particles have a HIGHER surface-area-to-volume ratio, not a lower one.
- [ ] The ratio stays the same whatever the size
    - *why wrong:* The ratio definitely changes with size — it rises as particles get smaller.
- [ ] The ratio becomes zero for very small particles
    - *why wrong:* The ratio actually becomes very large (not zero) for very small particles.

**Q4. [suggest · TFTH]** Silver nanoparticles are added to wound dressings. Suggest why their small size makes them suitable for this use.
- [✔︎] Their large surface-area-to-volume ratio makes them very reactive, so they are strongly antibacterial and only a small amount is needed
- [ ] Their large size lets them cover the whole wound
    - *why wrong:* Nanoparticles are small, not large; it is their high surface-area-to-volume ratio that makes them effective.
- [ ] They are cheaper than any other material
    - *why wrong:* Cost is not the property being asked about; their antibacterial action comes from their high reactivity.
- [ ] They dissolve completely to form a harmless gas
    - *why wrong:* They do not simply dissolve into a gas; their antibacterial effect is due to their reactive surface.

**Q5. [reason · TFTH]** Explain why nanoparticles make very effective catalysts.
- [✔︎] Their high surface-area-to-volume ratio provides a large surface for reactions, so a small mass is very effective
- [ ] They are used up during the reaction, which speeds it up
    - *why wrong:* Catalysts are not used up in a reaction; nanoparticles work because of their large reactive surface.
- [ ] They dissolve into the reactants to react faster
    - *why wrong:* A catalyst is not consumed and does not dissolve into the reactants; it provides a surface.
- [ ] They increase the temperature of the reaction
    - *why wrong:* Catalysts provide an alternative pathway; they do not simply heat the reaction up.

**Q6. [suggest · TFTH]** Titanium dioxide nanoparticles are used in sunscreen. Suggest why the nanoparticle form is used instead of bulk titanium dioxide.
- [✔︎] At the nanoscale it is transparent on the skin but still absorbs harmful UV radiation, unlike bulk titanium dioxide which is white
- [ ] The nanoparticle form is a different, safer chemical
    - *why wrong:* It is the same chemical (titanium dioxide) — only the particle size differs, which changes its appearance.
- [ ] The nanoparticle form reflects all light so the skin looks white
    - *why wrong:* Bulk TiO₂ is the white one; the nanoparticle form is chosen because it is transparent, not white.
- [ ] The nanoparticle form makes the sunscreen conduct electricity
    - *why wrong:* Conductivity is irrelevant to sunscreen; the point is transparency plus UV absorption.

**Q7. [recall · TF]** State the range of sizes (in nanometres) that defines a nanoparticle.
- [✔︎] 1 to 100 nm
- [ ] 1 to 100 mm
    - *why wrong:* Nanoparticles are measured in nanometres (nm), not millimetres — mm are a million times larger.
- [ ] 1 to 100 cm
    - *why wrong:* Centimetres are far too large; nanoparticles are 1–100 nm.
- [ ] 100 to 1000 nm
    - *why wrong:* Nanoparticles are defined as 1–100 nm, not 100–1000 nm.

**Q8. [apply · TF]** Identify a use of nanoparticles.
- [✔︎] In sunscreens, as an antibacterial agent, or as a catalyst
- [ ] As the main structural beams in a building
    - *why wrong:* Structural beams use bulk metals/alloys, not nanoparticles.
- [ ] As a fuel burned in power stations
    - *why wrong:* Nanoparticles are not burned as a fuel.
- [ ] As window glass
    - *why wrong:* Window glass is a bulk material, not a nanoparticle application.

**Q9. [recall · TF]** Name the carbon nanostructure that is a single layer of graphite, one atom thick.
- [✔︎] Graphene
- [ ] Diamond
    - *why wrong:* Diamond is a 3D giant covalent lattice, not a single layer.
- [ ] Buckminsterfullerene
    - *why wrong:* Buckminsterfullerene is a hollow cage of 60 carbon atoms, not a flat layer.
- [ ] Poly(ethene)
    - *why wrong:* Poly(ethene) is a polymer, not a form of carbon.

**Q10. [apply · TF]** Identify one possible risk of using nanoparticles.
- [✔︎] They may penetrate cells, and their long-term effects are not yet fully understood
- [ ] They always explode when exposed to air
    - *why wrong:* Nanoparticles do not routinely explode in air; the concern is their ability to enter cells.
- [ ] They make materials much heavier
    - *why wrong:* Nanoparticles are extremely light; they do not make materials heavier.
- [ ] They can only ever be used once
    - *why wrong:* Reusability is not the health/environmental risk being described.

### Triple Higher — 11 questions (0 recall / 11 apply+reason+calc)

**Q1. [reason · TFTH]** Explain why nanoparticles have different properties from the same material in bulk (large-scale) form.
- [✔︎] They have a much larger surface-area-to-volume ratio, so a greater fraction of their atoms are on the surface and available to take part in reactions
- [ ] They are made of different atoms from the bulk material
    - *why wrong:* Nanoparticles are made of the SAME atoms as the bulk material — it is the scale that changes the properties.
- [ ] They have weaker chemical bonds than the bulk material
    - *why wrong:* The bonds are the same type as in the bulk; what differs is the fraction of atoms on the surface.
- [ ] They are always more stable than the bulk material
    - *why wrong:* Nanoparticles are often MORE reactive (so less stable in some ways), not simply more stable.

**Q2. [suggest · TFTH]** Suggest why nanoparticles may pose a greater health risk than the same material in larger particle form.
- [✔︎] Their very small size may let them pass through cell membranes and into cells, and their long-term effects are not yet fully understood
- [ ] They are more toxic because they contain more of the harmful material
    - *why wrong:* A nanoparticle contains LESS material than a larger particle — the concern is its size and reactivity, not the amount.
- [ ] They are heavier, so they stay in the lungs longer
    - *why wrong:* Nanoparticles are lighter than larger particles; the concern is that their small size lets them penetrate the body.
- [ ] They react with water in the body to make dangerous chemicals
    - *why wrong:* The main concern is their ability to penetrate cells because of their size, not a specific reaction with water.

**Q3. [reason · TFTH]** Describe what happens to a particle's surface-area-to-volume ratio as the particle gets smaller.
- [✔︎] The ratio increases — smaller particles have a greater surface area compared with their volume
- [ ] The ratio decreases as the particle gets smaller
    - *why wrong:* Smaller particles have a HIGHER surface-area-to-volume ratio, not a lower one.
- [ ] The ratio stays the same whatever the size
    - *why wrong:* The ratio definitely changes with size — it rises as particles get smaller.
- [ ] The ratio becomes zero for very small particles
    - *why wrong:* The ratio actually becomes very large (not zero) for very small particles.

**Q4. [suggest · TFTH]** Silver nanoparticles are added to wound dressings. Suggest why their small size makes them suitable for this use.
- [✔︎] Their large surface-area-to-volume ratio makes them very reactive, so they are strongly antibacterial and only a small amount is needed
- [ ] Their large size lets them cover the whole wound
    - *why wrong:* Nanoparticles are small, not large; it is their high surface-area-to-volume ratio that makes them effective.
- [ ] They are cheaper than any other material
    - *why wrong:* Cost is not the property being asked about; their antibacterial action comes from their high reactivity.
- [ ] They dissolve completely to form a harmless gas
    - *why wrong:* They do not simply dissolve into a gas; their antibacterial effect is due to their reactive surface.

**Q5. [reason · TFTH]** Explain why nanoparticles make very effective catalysts.
- [✔︎] Their high surface-area-to-volume ratio provides a large surface for reactions, so a small mass is very effective
- [ ] They are used up during the reaction, which speeds it up
    - *why wrong:* Catalysts are not used up in a reaction; nanoparticles work because of their large reactive surface.
- [ ] They dissolve into the reactants to react faster
    - *why wrong:* A catalyst is not consumed and does not dissolve into the reactants; it provides a surface.
- [ ] They increase the temperature of the reaction
    - *why wrong:* Catalysts provide an alternative pathway; they do not simply heat the reaction up.

**Q6. [suggest · TFTH]** Titanium dioxide nanoparticles are used in sunscreen. Suggest why the nanoparticle form is used instead of bulk titanium dioxide.
- [✔︎] At the nanoscale it is transparent on the skin but still absorbs harmful UV radiation, unlike bulk titanium dioxide which is white
- [ ] The nanoparticle form is a different, safer chemical
    - *why wrong:* It is the same chemical (titanium dioxide) — only the particle size differs, which changes its appearance.
- [ ] The nanoparticle form reflects all light so the skin looks white
    - *why wrong:* Bulk TiO₂ is the white one; the nanoparticle form is chosen because it is transparent, not white.
- [ ] The nanoparticle form makes the sunscreen conduct electricity
    - *why wrong:* Conductivity is irrelevant to sunscreen; the point is transparency plus UV absorption.

**Q7. [reason · TH]** Explain, using surface-area-to-volume ratio, why nanoparticles are often much more reactive than the same material in bulk.
- [✔︎] A far greater proportion of their atoms are on the surface, where reactions happen, so reactions can occur faster and to a greater extent
- [ ] Their atoms are more reactive elements than those in the bulk
    - *why wrong:* The atoms are the same element as in the bulk; it is the higher fraction on the surface that increases reactivity.
- [ ] Their chemical bonds are much weaker than in the bulk
    - *why wrong:* The bonds are the same type and strength as in the bulk material.
- [ ] They contain more energy per atom than the bulk
    - *why wrong:* The increased reactivity comes from more exposed surface atoms, not from extra energy per atom.

**Q8. [reason · TH] ⭐** As the side length of a cube-shaped particle is halved, deduce what happens to its surface-area-to-volume ratio.
- [✔︎] It doubles — the ratio equals 6 ÷ L, so halving L makes the ratio twice as large
- [ ] It also halves
    - *why wrong:* Because the ratio is 6 ÷ L, a smaller L gives a LARGER ratio — it does not halve.
- [ ] It stays the same
    - *why wrong:* The ratio changes with size (6 ÷ L), so it does not stay the same.
- [ ] It becomes four times larger
    - *why wrong:* The ratio is inversely proportional to L (6 ÷ L), so halving L doubles it, not quadruples it.
  > 🚩 **Reviewer note:** Quantitative reasoning linked to the FIFA (SA:V = 6 ÷ L). Please full-review.

**Q9. [reason · TH]** Evaluate the use of silver nanoparticles in wound dressings by giving one benefit and one risk.
- [✔︎] Benefit: their high surface area makes them strongly antibacterial, helping wounds heal; risk: their small size may let them enter cells, with long-term effects that are not yet fully known
- [ ] Benefit: they are heavy, so they stay on the wound; risk: they are too cheap to be effective
    - *why wrong:* Nanoparticles are light, not heavy, and low cost is not a risk — the real risk is penetration of cells.
- [ ] Benefit: they dissolve into a harmless gas; risk: they make the dressing conduct electricity
    - *why wrong:* They do not dissolve into a gas, and conductivity is not the relevant risk.
- [ ] Benefit: they are a different, safer element; risk: they reflect UV light
    - *why wrong:* Silver nanoparticles are still silver (same element); UV reflection is not the concern here.

**Q10. [reason · TH]** Graphene is one atom thick and conducts electricity. Explain, in terms of its structure, why it is both very strong and a good electrical conductor.
- [✔︎] Each carbon is covalently bonded to three others in a strong hexagonal sheet (strength), and the fourth outer electron of each carbon is delocalised across the sheet (conductivity)
- [ ] It contains free ions that carry charge and hold it together
    - *why wrong:* Graphene has no ions; its conductivity comes from delocalised electrons and its strength from covalent bonds.
- [ ] It is a metal, so it is strong and conducts
    - *why wrong:* Graphene is a covalent form of carbon, not a metal.
- [ ] Its layers are held by strong intermolecular forces
    - *why wrong:* Graphene is a single layer, so 'forces between layers' do not apply; its strength is covalent.

**Q11. [calc/derivation · TH] ⭐** A cube-shaped particle of side 2 nm and one of side 20 nm are compared. Deduce which has the greater surface-area-to-volume ratio, and explain.
- [✔︎] The 2 nm particle — using ratio = 6 ÷ L gives 3 nm⁻¹ for the 2 nm particle and 0.3 nm⁻¹ for the 20 nm particle, so the smaller particle has the greater ratio
- [ ] The 20 nm particle, because it is bigger so has more surface
    - *why wrong:* A bigger particle has more surface in total, but LESS surface relative to its volume — the ratio (6 ÷ L) is smaller.
- [ ] They are equal, because they are the same shape
    - *why wrong:* Same shape does not mean same ratio; the ratio depends on size (6 ÷ L).
- [ ] The 2 nm particle, because bigger particles always have larger ratios
    - *why wrong:* The reasoning is back to front: SMALLER particles have the larger ratio, which is why the 2 nm one wins.
  > 🚩 **Reviewer note:** SA:V comparison calculation. Please full-review.

**FIFA worked examples ⭐ (full review):**

### Triple Foundation FIFA
- **Surface area to volume ratio of a cube (side 2)** — A cube-shaped particle has sides of length 2. Calculate its surface area to volume ratio.
    - **F** — surface area to volume ratio = surface area ÷ volume
    - **I** — surface area = 6 faces × (2 × 2) = 24;  volume = 2 × 2 × 2 = 8
    - **F** — ratio = 24 ÷ 8
    - **A** — surface area to volume ratio = 3 (that is, 3 : 1)
- **A smaller cube (side 1)** — A cube-shaped particle has sides of length 1. Calculate its surface area to volume ratio and compare it with the side-2 cube.
    - **F** — surface area to volume ratio = surface area ÷ volume
    - **I** — surface area = 6 × (1 × 1) = 6;  volume = 1 × 1 × 1 = 1
    - **F** — ratio = 6 ÷ 1
    - **A** — ratio = 6 (that is, 6 : 1) — the smaller cube has the LARGER ratio
- **A larger cube (side 3)** — A cube-shaped particle has sides of length 3. Calculate its surface area to volume ratio.
    - **F** — surface area to volume ratio = surface area ÷ volume
    - **I** — surface area = 6 × (3 × 3) = 54;  volume = 3 × 3 × 3 = 27
    - **F** — ratio = 54 ÷ 27
    - **A** — ratio = 2 (that is, 2 : 1) — the largest cube has the SMALLEST ratio

### Triple Higher FIFA
- **Surface area to volume ratio at the nanoscale** — A nanoparticle is modelled as a cube of side 10 nm. Calculate its surface area to volume ratio.
    - **F** — for a cube, surface area to volume ratio = 6L² ÷ L³ = 6 ÷ L
    - **I** — = 6 ÷ 10
    - **F** — the unit is nm⁻¹ (per nm), because length is in nm
    - **A** — surface area to volume ratio = 0.6 nm⁻¹
- **Comparing a nanoparticle with a bulk grain** — A grain of the same material is modelled as a cube of side 1000 nm. Calculate its surface area to volume ratio and compare it with the 10 nm nanoparticle.
    - **F** — surface area to volume ratio = 6 ÷ L
    - **I** — = 6 ÷ 1000
    - **F** — compare 0.006 nm⁻¹ with 0.6 nm⁻¹ for the nanoparticle
    - **A** — = 0.006 nm⁻¹; the nanoparticle's ratio is 100 times larger, so far more of its atoms are on the surface
- **Working backwards from a given ratio** — A cube-shaped nanoparticle has a surface area to volume ratio of 1.2 nm⁻¹. Calculate the length of its side.
    - **F** — surface area to volume ratio = 6 ÷ L, so L = 6 ÷ ratio
    - **I** — L = 6 ÷ 1.2
    - **F** — the answer is a length, so the unit is nm
    - **A** — L = 5 nm


---

