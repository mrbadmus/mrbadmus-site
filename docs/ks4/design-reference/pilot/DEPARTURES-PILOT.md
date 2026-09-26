# DEPARTURES — KS4 pilot (Bonding and Electricity, 14 lessons)

Ruled by Mide, 25 Sep 2026: **Design's page is the default.** A change is made
only where the science examiners (Opus, 25 Sep 2026, spec sources fetched and
read as text from filestore.aqa.org.uk) found it scientifically incorrect,
imprecise in a way a student carries into GCSE, self-contradicting, or
route-tagged wrong (chemistry-only/HT content served on a route that should
not see it, or base content withheld from one). Same bar as `DEPARTURES-P7.md`.

**101 required changes, from 14 examination files** (`docs/ks4/examination/
<lesson-slug>.md`, §2 "Required changes" plus the "applies to each route
copy" findings from §4) **plus 2 commander's rulings** (`metals-alloys-C12`,
`C13`, 26 Sep 2026 — two §4 findings the examiner described but did not
number; see "Resolved by the commander" below). Built by
`ks4_science_rulings.py`: `ROWS` is the data table, `apply()`/`apply_source()`
fire the changes, `--check` proves every row's `old` text is real (101 OK,
0 MISS). Full verbatim `old`/`new` text and per-item scientific reasoning
live in `ks4_science_rulings.py` and in each lesson's own examination file;
this register is the terse index the P7 format calls for.

Two rows are **byte-identical** to rulings the engine executor had
already built independently in `ks4_rulings.py`: `series-parallel-circuits-C1`
(flag 21, the "R_total = R1 + R2 is not on the AQA equation sheet" chip)
mirrors `ks4_rulings.R6`, and `metals-alloys-C8` (flag 17, the "model data"
relabel on the hardness-vs-carbon table) mirrors `ks4_rulings.R8`. Both count
in the 101 (L13's 5 and L11's 13) because the examiners' findings were real
and are recorded here, but `ks4_science_rulings.py` never applies either a
second time — see each row's note and the module's docstring.

## Changed — 99 rows (101 rows total, minus 2 docs-only; 2 of these 99 mirror ks4_rulings.R6/R8 and are not applied a second time by this file)

One row per ruling id. `old`/`new` truncated to ~64 characters — full text is in `ks4_science_rulings.py` and in the source examination file (`docs/ks4/examination/<lesson>.md`).

### L1 Chemical bonds

| id | layer | Design wrote | built | why | spec |
|---|---|---|---|---|---|
| chemical-bonds-C1 | logic | hydrogen is not, even though it sits at the top of the table ab… | hydrogen is not, even though, like sodium, it has one outer ele… | Contradicts the page's own grid (H drawn above Group 4, as on the AQA data sheet); the on… | 8462 4.1.1.7 / 4.2.1.1 |
| chemical-bonds-C2 | logic | 'Hydrogen sits above Group 1, but it is a non-metal. ' | 'Hydrogen has one outer electron, like Group 1, but it is a non… | As C1. | 4.2.1.1 |
| chemical-bonds-C3 | logic | 'Hydrogen sits above Group 1 but it is a non-metal. Two non-met… | 'Hydrogen has one outer electron like Group 1, but it is a non-… | As C1. | 4.2.1.1 |
| chemical-bonds-C4 | logic | 'Hydrogen is a non-metal, even though it sits above Group 1.' | 'Hydrogen is a non-metal, even though it has one outer electron… | As C1. | 4.2.1.1 |
| chemical-bonds-C5 | template | A metal atom has one, two or three outer electrons and gives th… | Most metal atoms have one, two or three outer electrons and giv… | Excludes hydrogen (1 outer electron, non-metal) and Group 4 metals as written. | 4.1.1.7, 4.2.1.1 |
| chemical-bonds-C6 | template | held by strong attraction all the way through, so they melt onl… | held by strong attraction all the way through, so most melt onl… | Spec says 'most metals'; Na (98°C) and K (63°C) are in this page's tray. | 4.2.2.7 |
| chemical-bonds-C7 | logic | 'Ions form when a metal gives electrons to a non-metal. With no… | 'Ionic bonding needs a non-metal to take the electrons. With no… | A metal is a lattice of positive ions; 'ions form when...' denies that and contradicts th… | 4.2.1.5 |
| chemical-bonds-C8 | logic | It builds giant covalent networks such as diamond and graphite,… | It usually builds giant covalent structures such as diamond and… | Fullerenes are molecules of carbon (core content). 'Giant covalent structures' is the spe… | 4.2.1.4, 5.2.3.3 |
| chemical-bonds-C9 | logic | reply: 'Mass matters less than you might think here.' | reply: 'Mass does not decide which type of bond forms.' | Original implies mass partly decides bond type. | 4.2.1.1 |
| chemical-bonds-C10 | logic | '\u2070\u00b9\u00b2\u00b3'[n] | '\u2070\u00b9\u00b2\u00b3\u2074'[n] | Index 4 is undefined: every metal + carbon pair renders 'Cundefined⁻'. (File stores the s… | render defect carrying science text |
| chemical-bonds-C11 | logic | title = 'Ionic: ' + res.name + ', ' + res.formula; | title = 'Ionic: ' + res.name + (res.X.s === 'C' ? '' : ', ' + r… | Metal + carbon formulae (calcium carbide etc.) are false for the named compounds; carbon … | 4.2.1.2 |
| chemical-bonds-C12 | logic | if (res.X.s === 'C') body += ' Carbon rarely forms simple ions,… | if (res.X.s === 'C') body = cap(res.M.n) + ' is a metal and car… | Replaces the body so it no longer states a 'C⁴⁻' ion or a false ratio. | 4.2.1.2 |
| chemical-bonds-C13 | logic | return D.svg(900, 300, D.T(450, 150, res.formula, 96) | if (res.X.s === 'C') return D.svg(900, 300, D.T(450, 160, res.M… | The chamber figure otherwise prints the false formula and 'C⁴⁻' ratio. | 4.2.1.2 |

### L2 Ionic bonding

| id | layer | Design wrote | built | why | spec |
|---|---|---|---|---|---|
| ionic-bonding-C1 | template | Both end up with the electron arrangement of a noble gas. | For Groups 1, 2, 6 and 7, both end up with the electron arrange… | Stated for every metal + non-metal; false for transition-metal ions (4.1.3.2). | 8462 4.2.1.2 / 8464 5.2.1.2 |
| ionic-bonding-C2 | logic | fLocked: fWorked \|\| fZero, fBtnStyle: this.seg(false, fWorked… | fLocked: fWorked \|\| fMin, fBtnStyle: this.seg(false, fWorked … | At a balanced but non-simplest box the verdict says 'Empty the box' while the button is d… | 8462 4.2.1.3 |
| ionic-bonding-C3 | logic | fZero, fHasNext: s.f < 2, | fZero, fHasNext: fMin && s.f < 2, | A non-simplest ratio can be banked as 'balanced' and the pupil moved on. | 8462 4.2.1.3 |
| ionic-bonding-C4 | logic | fProgress: s.fDone.length + ' of 3 balanced' | fProgress: (s.fDone.length + (s.f === 2 && fMin ? 1 : 0)) + ' o… | The third compound has no Next button, so it is never added to fDone; a correct Ca3N2 sho… | self-contradiction |

### L3 Ionic compounds

| id | layer | Design wrote | built | why | spec |
|---|---|---|---|---|---|
| ionic-compounds-C1 | logic | Rock salt that has never been dissolved is cubic as well. | A dry crystal crushed with no water near it breaks into cubes t… | Rock salt formed by evaporation of seawater, so it HAS been dissolved; the replacement us… | 8462 4.2.1.3 / 8464 5.2.1.3 |
| ionic-compounds-C2 | logic | left, right, above and below it on the page. | left and right of it, and one row up and one row down. | 'above and below' is used for the out-of-plane layers in the next tab and figure; reused … | 4.2.1.3 |
| ionic-compounds-C3 | logic | so there is a layer in front and a layer behind. | so there is a layer above this one and a layer below it. | Aligns the note with the tab and figure labels it narrates. | 4.2.1.3 |
| ionic-compounds-C4 | logic | No NaCl unit ever exists on its own. | In the solid, no NaCl unit exists on its own. | 'ever' over-claims (NaCl ion pairs exist in the vapour); scoping to the solid keeps it tr… | 4.2.1.3 |
| ionic-compounds-C5 | logic | Gives no idea of the crystal being three-dimensional. | Shows the alternating pattern, but flat, with no depth. | Equally true of figure A (dot-and-cross), contradicting the 'exactly one model' prompt. | 4.2.1.3 bullet 2 |
| ionic-compounds-C6 | logic | Draws sticks, as if each force acts along one line to one neigh… | Joins the 3D cube with sticks, as if each force acts along one … | Figure B (KS4D.lattice) also joins ions with lines; tying the item to the 3D model makes … | 4.2.1.3 bullet 2 |
| ionic-compounds-C7 | logic | Leaves big gaps between ions that really touch. | Spreads the 3D cube out, with big gaps between ions that really… | Figure B also leaves gaps; tying it to the 3D model makes it unique to C. | 4.2.1.3 bullet 2 |
| ionic-compounds-C8 | source (CH,TH routes) | Giant covalent substances do not conduct when molten (graphite … | Giant covalent substances have no ions to free on melting (grap… | 'graphite excepted' implies molten graphite conducts where others don't; graphite sublime… | 8462 4.2.3.2 |
| ionic-compounds-C9 | source (CH,TH routes) | Water dissolves many ionic compounds (non-metal-containing), no… | Water dissolves many ionic compounds, such as sodium chloride; … | The parenthetical is meaningless and the sentence implies water dissolves metals. | 8462 4.2.1.3 / 4.2.2.3 |

### L4 Covalent bonding

| id | layer | Design wrote | built | why | spec |
|---|---|---|---|---|---|
| covalent-bonding-C1 | template | like diamond and sand, where | like diamond and silicon dioxide (sand), where | 'Sand' is a mixture; the spec names the substance, silicon dioxide. | 8462 4.2.1.4 / 8464 5.2.1.4 |
| covalent-bonding-C2 | logic | why: 'If it were, it could not condense back into water on a co… | why: 'Steam is H₂O molecules. Boiling only overcomes the weak f… | The current reason is a non-sequitur and gives no chemistry. | 8462 4.2.2.4 / 8464 5.2.2.4 |
| covalent-bonding-C3 | source (CF,CH,TF,TH routes) | Atoms of the same element do repel slightly, but covalent bondi… | Pairing up does not cancel a repulsion. Two O atoms bond becaus… | States as fact that neutral atoms of the same element repel — not a GCSE idea and not cor… | 8462 4.2.1.1 / 4.2.1.4 |

### L5 Metallic bonding

| id | layer | Design wrote | built | why | spec |
|---|---|---|---|---|---|
| metallic-bonding-C1 | logic | K.find(slug, R.route, 'Name the particles that are free to move… | K.find(slug, R.route, 'Describe the structure of a metal') \|\|… | On CF/TF rung 1 is a 'Name' item shown under a 'Describe' chip with a why that answers a … | 4.2.1.5; AQA command words |
| metallic-bonding-C2 | logic | 'The hot end vibrates hardest · energy spreads along' | 'The hot end vibrates hardest · delocalised electrons carry the… | Caption named only ion vibration; the credited mechanism in a metal is delocalised electr… | 8462 4.2.2.8 / 8464 5.2.2.8 |
| metallic-bonding-C3 | logic | 'Ions near the heated end vibrate strongly and the vibration sp… | 'Ions near the heated end vibrate strongly and fast-moving delo… | Same omission in the figure's accessible description. | 8462 4.2.2.8 / 8464 5.2.2.8 |

### L6 States of matter

| id | layer | Design wrote | built | why | spec |
|---|---|---|---|---|---|
| states-of-matter-C1 | logic | The molecules separate from each other, but nothing inside them… | The molecules break free of their fixed positions, but nothing … | In a liquid particles are still close together; 'separate from each other' describes boil… | 8464 5.2.2.1 / 8462 4.2.2.1 |
| states-of-matter-C2 | logic | The tube is sealed off from the bath: only energy gets in. | The glass keeps the bath water out: only energy gets in. | A boiling tube in a water bath is open, not sealed. | practical context of 5.2.2.1 |

### L7 Properties of ionic compounds

| id | layer | Design wrote | built | why | spec |
|---|---|---|---|---|---|
| properties-ionic-compounds-C1 | logic | { text: '0 marks', correct: false, reply: 'It does say somethin… | { text: '0 marks', correct: true, reply: 'Zero. Having charged … | The specimen meets none of the page's own three marking points; AQA would award 0. | 8462 4.2.2.3 / 8464 5.2.2.3; AQA MS convention |
| properties-ionic-compounds-C2 | logic | { text: '1 mark', correct: true, reply: 'One mark at most, for … | { text: '1 mark', correct: false, reply: 'Too generous. The sol… | Rewards the exact idea key-note line 6 says 'scores nothing' — a self-contradiction. | 8462 4.2.2.3; AQA MS |
| properties-ionic-compounds-C3 | template | Say what will happen and give the reason from the structure. | Give a plausible outcome. Add the reason from the structure whe… | AQA defines Predict as 'give a plausible outcome'; a reason is not required, and this les… | AQA command-word list |
| properties-ionic-compounds-C4 | logic | (on ? ' \u00b7 bulb on' : ' \u00b7 switch open') | (on ? ' \u00b7 bulb on' : ' \u00b7 before the test') | beaker() draws a complete circuit with no switch, so 'switch open' names a component not … | circuit-diagram convention (8464 6.2.1.1) |
| properties-ionic-compounds-C5 | logic | Free ions between two electrodes, before the switch is closed. | Free ions between two electrodes, before the bulb is tested. | Alt text names the same undrawn switch as C4. | as C4 |
| properties-ionic-compounds-C6 | logic | { command: 'State', marks: 1, why: 'Melt it or dissolve it in w… | { command: R.isHigher ? 'Explain' : 'State', marks: 1, why: 'Me… | On CH/TH, K.find falls back to an 'Explain' stem while the chip says 'State' and the why … | AQA command words; 4.2.2.3 |

### L8 Properties of small molecules

| id | layer | Design wrote | built | why | spec |
|---|---|---|---|---|---|
| properties-small-molecules-C1 | template | Small molecules also never conduct electricity: | Small-molecule substances also do not conduct electricity: | 'Never' is false: HCl(aq) and other acids made from small molecules conduct. | 8462 4.2.2.4; 4.4.2.4 |
| properties-small-molecules-C2 | logic | Now try the other molecules: the bigger the molecule, the hotte… | Now try the other molecules: for chlorine, bromine and iodine, … | Methane is bigger than water and boils 261°C lower, so the unscoped rule contradicts the … | 8462 4.2.2.4; 4.1.2.6 |
| properties-small-molecules-C3 | template | but at atmospheric pressure it does melt at 114 °C. | but at atmospheric pressure it does melt at 114 °C. Water boils… | The bench shows water beside larger methane with no explanation of the anomaly. | 8462 4.2.2.4 |
| properties-small-molecules-C4 | template | The molecules are drawn to scale. | The molecules are drawn roughly to scale. | Drawn radii exaggerate the real Cl:Br:I size ratio. | 8462 4.2.1.4 |
| properties-small-molecules-C5 | logic | molecules drawn to scale, getting larger | molecules drawn roughly to scale, getting larger | As C4 (alt text). | 8462 4.2.1.4 |
| properties-small-molecules-C6 | logic | label: 'The state of hexane at 25 \u00b0C' | label: 'The state of hexane at 25 \u00b0C (it melts at \u221295… | 'Use the data' cannot decide solid against liquid without a melting point, and the model … | 8462 4.2.2.1 |

### L9 Polymers

| id | layer | Design wrote | built | why | spec |
|---|---|---|---|---|---|
| polymers-C1 | logic | r1: Object.assign(K.find(slug, R.route, 'State what is meant by… | r1: Object.assign((R.isTriple ? K.find(slug, R.route, 'State wh… | 'Monomer' is chemistry-only vocabulary (4.7.3.1); Combined routes must get the base item … | 8462 4.7.3.1; 8464 5.2.2.5, 5.2.1.4 |
| polymers-C2 | template | Addition polymerisation · AQA 4.7.3.1 (chemistry only) | Addition polymerisation · AQA 4.7.3.1, 4.10.3.3 (chemistry only) | The block also teaches thermosoftening/thermosetting, which is 4.10.3.3. | 8462 4.10.3.3 |
| polymers-C3 | template | Addition polymerisation and thermosetting polymers are separate… | Addition polymerisation, thermosoftening and thermosetting poly… | Thermosoftening is chemistry-only too; the line implied it was base. | 8462 4.10.3.3 |
| polymers-C6 | source (CF,TF routes) | Polymers are non-metals, not metals. | Polymers are made of non-metal atoms, not metal atoms. | 'Non-metal' classifies elements, not compounds. | 8464 5.2.1.1 |
| polymers-C7 | source (CF routes) | 6 item(s) dropped: Ethene (CH₂=CH₂) can be used to make poly(ethene), but ethane (C₂H₆) … | (removed) | Each tests addition polymerisation / monomer / C=C functional group — 8462 4.7.3.1, chemi… | 8462 4.7.3.1; 8464 5.7.1.4 |
| polymers-C8 | source (CH routes) | 6 item(s) dropped: Ethene (CH₂=CH₂) can be used to make poly(ethene), but ethane (C₂H₆) … | (removed) | 4.7.3.1 chemistry-only items, plus PVC polarity (outside GCSE, flag-6 precedent). | 8462 4.7.3.1; 8464 5.2.2.5 |
| polymers-C9 | source (TH routes) | 1 item(s) dropped: PVC is stiffer and higher-melting than poly(ethene). Suggest why, in … | (removed) | Credited answer rests on bond polarity, not in 8462. | 8462 4.2.2.5, 4.10.3.3 |
| polymers-C10 | source (TH routes) | Explain why polymers are described as having a simple molecular… | Explain why a polymer is a molecular substance, not a giant cov… | AQA classifies small molecules/polymers/giant structures as three separate kinds; 'simple… | 8464 5.2.1.4, 5.2.2.5 |

### L10 Giant covalent structures

| id | layer | Design wrote | built | why | spec |
|---|---|---|---|---|---|
| giant-covalent-structures-C1 | template | prompt="Same element, same very high melting point. What differ… | prompt="Same element, both very high melting points. What diffe… | Diamond and graphite do not have the SAME melting point; the spec only says both are very… | 5.2.2.6 |
| giant-covalent-structures-C2 | logic | right: 'Like diamond: every electron in a bond, bonds in every … | right: 'Like diamond: strong covalent bonds in every direction,… | In SiO2 the oxygen atoms keep lone pairs, so 'every electron in a bond' is false. | 5.2.2.6 |
| giant-covalent-structures-C3 | logic | wrong: 'Silicon dioxide is bonded like diamond: a rigid network… | wrong: 'Silicon dioxide is bonded like diamond: a rigid network… | Same error as C2. | 5.2.2.6 |
| giant-covalent-structures-C4 | logic | 'Both are giant covalent structures of carbon atoms, so both ha… | 'Both are giant covalent structures of carbon atoms: many stron… | The indicative point must carry the structure-to-property link the lesson's own Level 3 d… | 5.2.2.6 |
| giant-covalent-structures-C5 | logic | { command: 'Identify', marks: 1, why: 'Hardness comes from the … | { command: R.isHigher ? 'Explain' : 'Identify', marks: 1, why: … | On CH/TH rung 1 resolves to an 'Explain' item; the 'Identify' chip then contradicts the s… | 5.2.3.1 |

### L11 Metals and alloys

| id | layer | Design wrote | built | why | spec |
|---|---|---|---|---|---|
| metals-alloys-C1 | template | Alloys as useful materials · AQA 4.10.4.2 (chemistry only) | Alloys as useful materials · AQA 4.10.3.2 (chemistry only) | Wrong spec reference; 4.10.4.2 is NPK fertilisers. | 8462 4.10.3.2 |
| metals-alloys-C2 | template | Most wedding rings are 18-carat | Many wedding rings are 18-carat | 'Most' is an unsupported factual claim (9-carat is at least as common in the UK). | 8462 4.10.3.2 (context) |
| metals-alloys-C3 | logic | The other metal atoms are a different size from gold atoms. | Copper atoms are a different size from gold atoms. | Silver, which the hook names, is the same size as gold (both 144 pm); copper is genuinely… | 5.2.2.7 |
| metals-alloys-C4 | logic | so they catch on each other and cannot slide. The alloy is hard… | so they catch on each other and cannot slide easily. The alloy … | Agrees with the key fact, chain and key note; alloys are harder, not undeformable. | 5.2.2.7 |
| metals-alloys-C5 | logic | Ionic compounds need melting because their charge carriers are … | Ionic compounds need melting or dissolving because their charge… | The credited option must include dissolving; 'locked in place' is true only in the solid. | 5.2.2.3 |
| metals-alloys-C6 | template | Steels are iron with carbon or other metals. | Steels are iron with carbon, and sometimes other metals. | Every steel contains carbon. | 8462 4.10.3.2 |
| metals-alloys-C7 | logic | why: 'A mixture of a metal with at least one other element, usu… | why: 'An alloy is a mixture of a metal with at least one other … | On CH/TH rung 1 serves 'Describe the difference in structure...', not 'State what an allo… | 5.2.2.7 |
| metals-alloys-C8 | logic | prompt: 'The table shows the hardness of iron mixed with differ… | prompt: 'The table shows model data for the hardness of iron mi… *(mirrors ks4_rulings.R8 — not applied here)* | The numbers are illustrative, not a cited data set (flag 17). BYTE-IDENTICAL to ks4_rulin… | WS 3.5; flag 17 |
| metals-alloys-C9 | logic | 'Metals have giant structures: positive ions in regular layers,… | 'Metals have giant structures with strong metallic bonding, so … | The 5.2.2.7 melting/boiling-point statement is otherwise absent from the page. | 5.2.2.7 |
| metals-alloys-C10 | template | with one delocalised electron per ion left out for clarity | with the delocalised electrons left out for clarity | Electrons per ion varies by metal (Na 1, Mg 2, Al 3). | 5.2.1.5 |
| metals-alloys-C11 | template | Named alloys and their uses are separate-science content and sh… | Recalling named alloys and their uses is separate-science conte… | Removes the self-contradiction — brass, steel and 18-carat gold appear on all routes as g… | 8462 4.10.3.2 vs 8464 5.2.2.7 |

### L12 Nanoparticles

| id | layer | Design wrote | built | why | spec |
|---|---|---|---|---|---|
| nanoparticles-C1 | logic | a large fraction of the atoms sit on the surface | a far larger fraction of the atoms sit on the surface | A 25 nm gold particle has about 7% of its atoms on the surface; 'a large fraction' reads … | 8462 4.2.4.1 |
| nanoparticles-C2 | template | A nanoparticle holds only a few hundred atoms; an atom is about… | Nanoparticles are of the order of a few hundred atoms; an atom … | The spec's 0.1 nm is a RADIUS, not a diameter; 'only a few hundred' hardens 'of the order… | 8462 4.1.1.4; 4.2.4.1 |
| nanoparticles-C3 | logic | 'A cube of side 1000 nm sliced into ' + (k * k * k) + ' smaller… | 'A cube of side 1000 nm sliced (drawn schematically, not to sca… | The alt text gives false counts (8 instead of 1000, etc.). | MS 5c |
| nanoparticles-C4 | template | The cube splitter draws a cube of each size sliced into smaller… | The cube splitter draws a cube of each size sliced into smaller… | The drawing shows 2, 4 and 8 slices per edge — the model-limits line must say this is sch… | MS 5c |
| nanoparticles-C5 | logic | 0.02 = 300, a thousand times too big. | 0.02 = 300 per micrometre, a thousand times too big for an answ… | 300 µm⁻¹ is a correct value; the error is only in the unit asked for. | MS 1b |
| nanoparticles-C6 | template | Say how many times bigger: divide one ratio by the other. | Describe the similarities or differences; with ratios, say how … | AQA defines 'Compare' as describing similarities and/or differences. | AQA command-word glossary |
| nanoparticles-C7 | logic | K.find(slug, R.route, 'State the range of sizes') \|\| |  | On TF the needle hits a 'State' item while the rung carries command 'Describe' and a why … | 8462 4.2.4.1 |
| nanoparticles-C8 | logic | They contain a few hundred atoms. | They are of the order of a few hundred atoms. | Restores the spec's 'of the order of' (see C2); this is the key-note line pupils memorise. | 8462 4.2.4.1 |

### L13 Series and parallel circuits

| id | layer | Design wrote | built | why | spec |
|---|---|---|---|---|---|
| series-parallel-circuits-C1 | template | <div style="padding: 16px 18px; border-radius: 14px; background… | <div style="padding: 16px 18px; border-radius: 14px; background… *(mirrors ks4_rulings.R6 — not applied here)* | Flag 21: R_total = R1 + R2 is not on either June 2026 equation sheet. BYTE-IDENTICAL to k… | 8463 4.2.2 / 8464 6.2.2; AQA equation sheets, June 2026 |
| series-parallel-circuits-C2 | logic | R\u2081 is still across the battery: 12 V, and its lamp would s… | R\u2081 is still across the battery, so it still has the full 1… | There is no lamp in the circuit. (File stores the subscript as a literal \u2081 escape, n… | 4.2.2 |
| series-parallel-circuits-C3 | logic | name: 'R\u2082 removed' | name: 'R\u2082 branch broken' | The step title is 'The R2 branch breaks.', but the drawn open switch is labelled 'removed… | 4.2.1.1, 4.2.2 |
| series-parallel-circuits-C4 | template | Show every line. The unit earns its own mark. | Show every line. If the answer line does not print the unit, gi… | States a marking rule AQA does not apply; the unit is usually printed on the answer line. | AQA command-word glossary; mark-scheme convention |
| series-parallel-circuits-C5 | source (CF,CH,TF,TH routes) | RP15 (Physics) — Construct series and parallel circuits; measur… | RP15 (Combined Science) / RP3 (Physics) — Use circuit diagrams … | The source describes a practical that does not exist; also mislabels the Combined number … | 8464 6.2.1.3 RP15 / 8463 4.2.1.3 RP3 |

### L14 Resistors and I-V characteristics

| id | layer | Design wrote | built | why | spec |
|---|---|---|---|---|---|
| resistors-C1 | template | Repeat for a range of p.d. values, switching off between readin… | Repeat for a range of p.d. values, switching off between readin… | The method covers the filament lamp too, which MUST heat — that heating is the effect bei… | 8463 RP4 / 8464 RP16; 4.2.1.4 |
| resistors-C2 | logic | Keep it steady; switching off between readings helps. | Keep it steady, so that the only thing heating the filament is … | Switching off does not control room temperature. | WS 2.2; 4.2.1.4 |
| resistors-C3 | logic | and the negative half is a mirror of the positive half. | and the negative readings lie on the same straight line. | An ohmic I-V line continues through the origin; 'mirror' suggests a reflection (V shape). | 4.2.1.4 |
| resistors-C4 | logic | One reading sits well below the curve: an anomaly, to be left o… | A reading that sits well off the curve is an anomaly: leave it … | The anomaly is only planted if the 5th recorded reading is positive; the new sentence hol… | WS 3.5, WS 3.7 |
| resistors-C5 | logic | answer: 13.3, tol: 0.1, | answer: 13.3, tol: 0.35, | Tolerance is absolute; with 2-s.f. data (2.0 V, 150 mA) AQA credits 13 Ω, which the old t… | 4.2.1.3; MS 2a / WS 4.6 |
| resistors-C6 | logic | a range of p.d. values set with the variable resistor, readings… | a range of p.d. values set with the variable resistor, readings… | AQA's Level 3 is holistic; reversal is credited indicative content, not a gate. | AQA 6-mark level-of-response convention; RP4/RP16 |
| resistors-C7 | logic | 'Lamp in series with an ammeter, a variable resistor and a batt… | 'Lamp in series with an ammeter, a variable resistor and a batt… | AQA credits either way of varying the p.d. | RP4/RP16 |
| resistors-C8 | logic | 'Take a range of readings (e.g. at least 5) up to the lamp\u201… | 'Take a range of readings (e.g. at least 5) up to the lamp\u201… | Repeat readings and means are standard AQA indicative content for an RP method. | WS 2.6, WS 3.7; MS 2b |
| resistors-C9 | template | <p style="margin: 0; font-family: var(--ks3-font-display); font… | <span style="display: inline-block; margin-bottom: 8px; font-fa… | V = I R is on both June 2026 sheets; L13's identical card carries the chip, L14's should … | 8463/8464 June 2026 equation sheets |
| resistors-C13 | source (CF,CH,TF,TH routes) | RP16 (Physics) — Construct circuits to investigate I–V characte… | RP16 (Combined Science) / RP4 (Physics) — Construct circuits to… | RP16 is the 8464 number, not the Physics one (8463 RP4); also restores 'at constant tempe… | 8463 §8.2.4 RP4; 8464 RP16 |
| resistors-C14 | source (CF,CH,TF,TH routes) | RP16: investigate I–V graphs for resistor, lamp, diode. | Required practical (RP16 Combined / RP4 Physics): investigate I… | Same numbering error as C13; only matters if the port ever serves key_note verbatim. | 8463 RP4; 8464 RP16 |

### Shared asset (ks4-diagrams.js, both L13 and L14)

| id | layer | Design wrote | built | why | spec |
|---|---|---|---|---|---|
| resistors-C10 | asset | cell: function (x, y, it) { return leads(x, y, 36) + | cell: function (x, y, it) { return leads(x, y, 18) + | Without this the leads stop 9px short of the plates, drawing every cell as an open circui… | 8463 4.2.1.1 (cell symbol) |
| resistors-C11 | asset | battery: function (x, y, it) { var s = leads(x, y, 70); [-22, 1… | battery: function (x, y, it) { var s = leads(x, y, 52) + line(x… | Centres the two cells, brings leads to the outer plates, and joins the cells with AQA's d… | 8463 4.2.1.1 (battery symbol) |
| resistors-C12 | asset | circ(x - 30, y, 5, C.stroke) + circ(x + 30, y, 5, C.stroke) | circ(x - 30, y, 6, C.cream, C.stroke, 2.5) + circ(x + 30, y, 6,… | AQA's switch contacts are hollow circles; filled dots mean junctions. | 8463 4.2.1.1 (switch open/closed) |

## Verbatim layer — the `source` rows (generated route copies)

These never touch `all_subtopics_*.py` — they patch the in-memory dict `build_ks4.build_source_record()` builds, via `apply_source()`.

| id | lesson | op | field | routes | what |
|---|---|---|---|---|---|
| ionic-compounds-C8 | ionic-compounds | edit | quiz | CH,TH | Giant covalent substances do not conduct when molten (graphite … -> Giant covalent substances have no ions to free on melting (grap… |
| ionic-compounds-C9 | ionic-compounds | edit | quiz | CH,TH | Water dissolves many ionic compounds (non-metal-containing), no… -> Water dissolves many ionic compounds, such as sodium chloride; … |
| covalent-bonding-C3 | covalent-bonding | edit | quiz | CF,CH,TF,TH | Atoms of the same element do repel slightly, but covalent bondi… -> Pairing up does not cancel a repulsion. Two O atoms bond becaus… |
| polymers-C6 | polymers | edit | quiz | CF,TF | Polymers are non-metals, not metals. -> Polymers are made of non-metal atoms, not metal atoms. |
| polymers-C7 | polymers | drop_item | quiz | CF | drop 6 item(s): Ethene (CH₂=CH₂) can be used to make poly(ethene), but etha… |
| polymers-C8 | polymers | drop_item | quiz | CH | drop 6 item(s): Ethene (CH₂=CH₂) can be used to make poly(ethene), but etha… |
| polymers-C9 | polymers | drop_item | quiz | TH | drop 1 item(s): PVC is stiffer and higher-melting than poly(ethene). Sugges… |
| polymers-C10 | polymers | edit | quiz | TH | Explain why polymers are described as having a simple molecular… -> Explain why a polymer is a molecular substance, not a giant cov… |
| series-parallel-circuits-C5 | series-parallel-circuits | edit | rp | CF,CH,TF,TH | RP15 (Physics) — Construct series and parallel circuits; measur… -> RP15 (Combined Science) / RP3 (Physics) — Use circuit diagrams … |
| resistors-C13 | resistors | edit | rp | CF,CH,TF,TH | RP16 (Physics) — Construct circuits to investigate I–V characte… -> RP16 (Combined Science) / RP4 (Physics) — Construct circuits to… |
| resistors-C14 | resistors | edit | key_note | CF,CH,TF,TH | RP16: investigate I–V graphs for resistor, lamp, diode. -> Required practical (RP16 Combined / RP4 Physics): investigate I… |
| metals-alloys-C12 | metals-alloys | drop_item | quiz | CF | drop 1 item(s): Identify the correct description of steel. |
| metals-alloys-C13 | metals-alloys | drop_item | quiz | CH | drop 1 item(s): Stainless steel is used to make cutlery. Suggest two prope… |
---

## Documentation-only fixes (never applied — the delivery is committed unmodified)

| id | file | wrong | corrected | why |
|---|---|---|---|---|
| polymers-C4 | `NOTES-KS4-pilot.md` | `8462 4.10.4.3 (chemistry only)` | `8462 4.10.3.3 (chemistry only)` | 4.10.4 is the Haber process / NPK fertilisers, not alloys or polymers |
| polymers-C5 | `README.txt` | `thermosoftening and thermosetting 4.10.4.3` | `thermosoftening and thermosetting 4.10.3.3` | Same wrong section number |

## Considered, not changed

**Flag 9 — charge size vs melting point (MgO vs NaCl, and similar pairs).**
Touches L3 (ionic-compounds: CH6/TH6/TH12) and L7 (properties-ionic-compounds:
CH6/CH8/CH10/TH6/TH8/TH10/TH11, CF10/TF10). Not a 4.2.2.3 statement, but
correct chemistry, an application of 4.2.2.1 ("stronger forces, higher
melting/boiling point"), and the kind of AQA Higher stretch examiners do set.
Kept verbatim in the bank on the routes that already carry it; not taught in
either lesson's body.

**Flag 4 — nanoparticles bank counts (11 items on TH, 10 on TF).** Confirmed
correct as delivered; nothing HT-flagged sits inside 4.2.4 (no HT marker
anywhere in the section), so there is no reason for the two counts to match.

**Carats in the L11 (metals-alloys) hook, all four routes.** 24- and
18-carat gold are 8462 4.10.3.2 content (chemistry only), but here they frame
a 5.2.2.7 phenomenon (why alloying hardens a metal) as GIVEN information, and
no Combined-route item assesses the carat system itself. Kept on all routes;
the legal line is corrected instead (metals-alloys-C11) so it no longer
claims named alloys "show only on Triple routes" when brass, steel and
18-carat gold already appear on every route as supplied context.

**Al³⁺ / N³⁻ in L2 (ionic-bonding)'s Formula Forge, all four routes.**
4.2.1.2's "limited to Groups 1 and 2, and 6 and 7" governs working out a
charge FROM THE GROUP NUMBER and drawing dot-and-cross diagrams. The forge
does neither: it states the ion charges on the buttons and asks only for
charge-balancing practice, which AQA examines freely with given ions
(e.g. Al₂O₃ in 4.4.3.3). The page's own `legal` line already discloses this.

**Flag 6 — dot-and-cross is base; electronegativity dropped.** Touches L1
(chemical-bonds) and L4 (covalent-bonding). Confirmed against both fetched
PDFs: 4.2.1.4/5.2.1.4 carries no HT marker, so drawing the eight named
molecules is base content on every route. Electronegativity and bond
polarity appear nowhere in either specification and are correctly absent.
The one place this needed an actual fix — the frozen `higher` field on
covalent-bonding claiming the drawing list is Higher-only — is a
"do not serve" ruling for the engine, not a text change (no id; noted for
the commander in `docs/ks4/examination/covalent-bonding.md` §4).

**Flag 8 — states-of-matter's HT items, corrected reading.** NOTES-KS4-pilot
mis-numbers them as TH7/TH11; the real HT-only items are **CH8, TH8 and
TH12** (checked by script against the served route copies). No route copy
needs editing — CF and TF correctly carry no limitation item, and the page's
own `sc-if isHigher` wrapper already keeps the HT block off Foundation.

**Flag 11 — draft examiner tips (L13, L14).** Both drafts are factually
correct (L14's has one imprecision: it implies the variable resistor is the
only creditable method, which resistors-C7 already fixes in the RP text
itself). Mide's call, not a science defect: **not approved**. Both drafts
stay out of the built page (the slot is removed, per `ks4_rulings.R7`) and
are preserved verbatim in `docs/ks4/pilot-inventory/draft-exam-tips.md`.

**Flag 15 — no parallel-resistance calculation anywhere in L13.** Confirmed:
the bench computes only branch currents (`I = V/R` per branch, itself
permitted), never a combined-parallel-resistance figure. Compliant with
"Students are not required to calculate the total resistance of two
resistors joined in parallel."

**Flag 19 — alloy hardness kept out of L5 (metallic-bonding)'s taught body
and key note, and placed in L11 instead.** Confirmed: L5's `keyLines`
constant (Design's own, hand-authored) carries no alloy line, and L11
teaches distortion-of-layers hardness in full. The frozen `key_note` for L5,
which DOES mention alloys, is correctly never served (Design's page renders
its own `keyLines`, not `K.keyLines(slug)`).

**Flag 20 — filament-lamp resistance has no ion/electron-collision
mechanism anywhere on L14.** Confirmed compliant across every reference to
the filament (hook, shape text, r3, key fact, key-note line 4, CFIFA Q1):
each states only that resistance rises as temperature rises, never why.

**Flag 3 — nanoparticles' SA:V calculation is NOT gated Higher.** Confirmed:
4.2.4.1 carries no HT marker anywhere in either fetched PDF, so the frozen
source's `higher` field (which implies the calculation is HT-only) is simply
wrong and Design is right to ignore it. Nothing to change on the page; a
"do not serve `higher`" note for the engine, same shape as flag 6's.

### Resolved by the commander, 26 Sep 2026 — metals-alloys-C12/C13

Two findings in `docs/ks4/examination/metals-alloys.md` §4 were real and
described in full, but the examiner had not assigned them a
`metals-alloys-Cn` id (the file's own required-changes table stopped at C11,
and L11's row count in the build contract was 11). The commander has now
ruled both in, minting `metals-alloys-C12` and `metals-alloys-C13` and
raising L11's row count to 13 (`ks4_science_rulings.ROWS` is 101 total,
`--check` 101 OK / 0 MISS):

- **`metals-alloys-C12`** — CF quiz item 9 ("Identify the correct description
  of steel") recalled steel's composition from memory — 8462 4.10.3.2,
  chemistry only, not supplied in the stem. **Dropped from the generated CF
  route copy** (`op='drop_item'`); TF9 keeps the equivalent item.
- **`metals-alloys-C13`** — CH quiz item 7 ("Stainless steel... Suggest two
  properties") credited an answer that depends on recalling stainless steel
  resists corrosion — same chemistry-only recall, not supplied in the stem.
  **Dropped from the generated CH route copy** (`op='drop_item'`); TH7 keeps
  it.

Both are route-tag leaks by the same standard every other `source` row in
this register was fixed to; both are now listed in the Verbatim-layer table
above alongside the rest of L11's `source` rows.

---

## Not departures, and why

Everything below is port mechanics, engine behaviour, or a commander-level
convention — not a change to Design's science, and not a row in `ROWS`.

**The Route `<select>` is removed at compile time.** One route ships per URL;
Design's review affordance is a build-time deletion (`ks4_rulings.R1`), not a
hand edit and not a science finding.

**Three lessons' internal `const slug` is rewritten to the site slug.**
`metals-alloys` (was `metals-and-alloys`), `series-parallel-circuits` (was
`series-and-parallel`) and `resistors` (was `resistors-iv`) — `ks4_rulings.
R-SLUG`. Needed so `KS4.find`/`KS4.bank`/`KS4.tip`/`KS4.keyLines` and the
`ks4-best-<slug>` localStorage key all resolve against a source file keyed by
the URL slug.

**`endPrev`/`endNext` are computed from the site's real per-route subtopic
order, not from Design's hardcoded pilot-internal narrative** (`ks4_rulings.
R-PREVNEXT`). The real order disagrees with Design's on L11→L13→L14 (real:
...→resistors→series-parallel-circuits→(unported); Design assumed the
reverse), and L11's Combined routes have no next lesson at all (nanoparticles
is Triple-only) — noted in the metals-alloys route-tags table as a
navigation issue, not a science one, and left to the engine's per-route prop.

**`endConnects` cross-references are rewritten to real URLs via
`KS4.hrefFor(slug, R)`** (`ks4_rulings.R-CONNECTS`), falling back to the
Triple pathway at the same tier for nanoparticles (Triple-only) when linked
from a Combined page. Design's CHOICE of which lessons to cross-link is
untouched — only the non-existent `.dc.html` URLs are fixed.

**React's four `createElement(...dangerouslySetInnerHTML...)` call sites
become the runtime's figure marker object** (`ks4_rulings.R2`) — a compile
detail, not a content change; every SVG string Design authored ships
unmodified.

**Ks4Chrome's brand link and breadcrumbs point at `/ks4.html`**, not
Design's local `README.md` review index (`ks4_rulings.R-BREADCRUMB`) — the
nearest real page, a bounded simplification recorded there, not here.

**The spec-numbering convention (8464/5.x or 6.x Combined-Science numbers,
shown on every route including Triple) is kept as-is on all 14 pages.** Every
single examination file flags this in its own §1 row 1 as "the pilot's house
convention, not a science error" and explicitly declines to raise a change
id for it — a Triple pupil checking 8463/8462 would need to translate 5.2.1.1
to 4.2.1.1 themselves. This is a COMMANDER decision (Mide, 25 Sep 2026):
ship the Combined numbering pilot-wide for this run; a future pass can make
it route-aware the same way `KS4.hrefFor` made links route-aware.

**The CFIFA restructuring (Formula stated exactly as printed on the AQA
equation sheet — un-rearranged — with the rearrangement moved to the
Fine-tune step) is Mide's standing correction to Design's original
Convert-Formula-Insert-Fix-Answer pattern**, applied across every worked
example and ladder-r2 model in L12, L13 and L14. It changes no number and no
credited answer anywhere the examiners checked (recomputed in full in each
lesson's §6) — it is a presentation ruling from before this examination pass,
not a finding of this pass, and is recorded here only so its many `CFIFA`
mentions across the fourteen `#6` sections are not mistaken for departures.

---

## Flags — all 22, decided (NOTES-KS4-pilot.md §9)

| # | flag | decision | source lesson(s) |
|---|---|---|---|
| 1 | Graphene and fullerenes are core, not Higher | UPHELD — no HT/chemistry-only marker on 5.2.3.3/4.2.3.3 in either fetched PDF; untagged teaching on L1 and L10 is correct | L1, L10 |
| 2 | Nanoparticles spec number (5.2.3.3 vs real 4.2.4) | Page shows 4.2.4 throughout; filename keeps the pilot slug so Code's mapping resolves; no generated text may print 5.2.3.3 for this lesson | L12 |
| 3 | Nanoparticles SA:V gated Higher in the frozen source | WRONG in the source; Design correctly ignores it — 4.2.4.1 carries no HT marker | L12 |
| 4 | Nanoparticles quiz counts: 11 (TH) vs 10 (TF) | CONFIRMED correct, kept verbatim | L12 |
| 5 | PM10/PM2.5 and size ranges added from 4.2.4.1 | CONFIRMED correct — all 6 sort items land in the right bin, no boundary cases | L12 |
| 6 | Covalent dot-and-cross is base; electronegativity dropped | UPHELD — no HT marker on 4.2.1.4/5.2.1.4; electronegativity/polarity are in neither spec | L1, L4 |
| 7 | Addition-polymerisation content leaked into Combined quiz copies | FIXED — CF loses 6 items, CH loses 6, TH loses 1 (PVC), rung 1 re-pointed off Combined | L9 |
| 8 | States-of-matter HT items mis-numbered in NOTES | CORRECTED reading: the real HT items are CH8, TH8, TH12 (not TH7/TH11); no route copy needed editing | L6 |
| 9 | Charge size vs melting point is not a spec statement | Kept verbatim in the bank on every route that already carries it; not taught in either body | L3, L7 |
| 10 | 5.2.2.2 and 5.2.2.8 have no dedicated lesson slot | Folded correctly into states-of-matter (5.2.2.2) and metals-alloys (5.2.2.8) | L6, L11 |
| 11 | No examiner tip exists for either physics lesson | Draft text factually correct; Mide's call to NOT approve — ships without the slot, drafts preserved in `docs/ks4/pilot-inventory/draft-exam-tips.md` | L13, L14 |
| 12 | Series-and-parallel source mis-describes RP15 as "verify the rules" | FIXED — `rp` field rewritten to the real AQA RP15/RP3 (resistance: wire length, series/parallel combinations) | L13 |
| 13 | RP numbering: RP15/RP16 are the 8464 numbers, not Physics' (RP3/RP4) | FIXED — served `rp`/`key_note` name both numbers | L13, L14 |
| 14 | Physics quizzes are thin (2 questions, one route copy) | CONFIRMED; ladder rungs 2-4 supply the new content, examined in full in each §6 | L13, L14 |
| 15 | Parallel resistance is qualitative only at GCSE | CONFIRMED compliant — no parallel-R calculation anywhere on L13 | L13 |
| 16 | Option order: correct answer always first/longest in the frozen bank | ACCEPTED sitewide — keep the deterministic hash re-order (`KS4.item`); no option TEXT changes, so "verbatim" is not breached; scoring reads the `correct` flag, not position | all 14 |
| 17 | Data values (data-book, rounded) | VERIFIED throughout; the one non-real set (L11's hardness-vs-carbon, 70/120/155/220) is relabelled "model data" rather than replaced | all 14 (spot-checked in each §5/§6) |
| 18 | New worked examples and questions need an examiner pass | DONE — every lesson's §6 records the check; this register's "Changed" table is the set of defects that pass found | all 14 |
| 19 | Metallic-bonding's key note mentions alloys; moved to metals-alloys | CONFIRMED — L5's own `keyLines` carries no alloy line; L11 teaches it in full | L5, L11 |
| 20 | Filament-lamp resistance: no ion/electron mechanism story | CONFIRMED compliant — every mention states only that R rises with temperature | L14 |
| 21 | R_total = R1 + R2 is not one of the 35 equation-sheet equations | Chip "Not on the sheet · learn it" added — `ks4_rulings.R6` (mirrored, not duplicated, by `series-parallel-circuits-C1`) | L13 |
| 22 | Equation-sheet URLs are year-stamped ("for use in June 2026 only") | CONFIRMED both `EQ_BY_YEAR[2026]` URLs resolve (HTTP 200, PDF); no June 2027 sheet published yet — add `EQ_BY_YEAR[2027]` and move `EQ_YEAR` when AQA releases it | L13, L14 |

