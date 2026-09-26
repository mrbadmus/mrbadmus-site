# Examination — Ionic compounds (ionic-compounds) — AQA 8464 5.2.1.3 / 8462 4.2.1.3
Verdict: CHANGES REQUIRED
Examiner: Opus, 25 Sep 2026. Spec sources fetched: AQA-8462-SP-2016.PDF (v1.1, 04 Oct 2019) §4.2.1.3, §4.2.2.3, §4.2.2.7; AQA-8464-SP-2016.PDF (v1.1) §5.2.1.3 (text identical to 8462 §4.2.1.3; no HT marker, no "chemistry only" marker). Cited below as "8462 4.2.1.3 / 8464 5.2.1.3, fetched PDF".

Spec statements relied on (verbatim, 8462 4.2.1.3 = 8464 5.2.1.3):
- "An ionic compound is a giant structure of ions. Ionic compounds are held together by strong electrostatic forces of attraction between oppositely charged ions. These forces act in all directions in the lattice and this is called ionic bonding."
- "deduce that a compound is ionic from a diagram of its structure in one of the specified forms"
- "describe the limitations of using dot and cross, ball and stick, two and three-dimensional diagrams to represent a giant ionic structure"
- "work out the empirical formula of an ionic compound from a given model or diagram that shows the ions in the structure."
- "Students should be familiar with the structure of sodium chloride but do not need to know the structures of other ionic compounds."

Design file: `docs/ks4/design-reference/pilot/KS4 Lessons/Pilot - Bonding and Electricity/ks4-chemistry-5.2.1.3-ionic-compounds.dc.html` (abbrev. **IC**).

## 1. Checked items
| # | Where (element / constant name / template line) | Claim as written | Spec section | Verdict (OK / WRONG / IMPRECISE / CONTRADICTS) | Note |
|---|---|---|---|---|---|
| 1 | header eyebrow | "AQA Chemistry 5.2.1.3 · Model" | 8464 5.2.1.3 = 8462 4.2.1.3 | OK | Trilogy numbering used across the pilot; the 8462 equivalent is 4.2.1.3. Not a science defect. |
| 2 | h1 / `ks3-bigq` | "The formula says NaCl. So is a grain of salt made of little NaCl molecules, or of something else entirely?" | 4.2.1.3 | OK | Question, not a claim. |
| 3 | header badges | "Combined · Triple" / "Foundation · Higher" | 4.2.1.3 (no HT, no chem-only) | OK | Whole lesson is base content. |
| 4 | hook h2 | "Crush a salt crystal. You get smaller cubes." | 4.2.1.3 (NaCl structure) | OK | Halite has perfect cubic cleavage. |
| 5 | hook prose | grains are cubes with flat faces; crushed fragments break along flat faces into smaller cubes; slow growth gives dice-sized cubes | 4.2.1.3 | OK | Consistent with NaCl's cubic lattice/cleavage. |
| 6 | `hookOptions[0]` + reply | "The particles inside stack in one regular pattern that repeats" | 4.2.1.3 "giant structure", "lattice" | OK | The intended answer; unscored. |
| 7 | `hookOptions[1]` + reply | "Salt molecules are shaped like tiny cubes" / "Hold that idea. You are about to meet a problem with it." | 4.2.1.3 | OK | Reply flags the misconception without endorsing it. |
| 8 | `hookOptions[2]` reply | "Salt grown in a jar at home comes out as cubes too." | 4.2.1.3 | OK | True. |
| 9 | `hookOptions[3]` reply | "Rock salt that has never been dissolved is cubic as well." | general chemistry (halite formation) | WRONG | Rock salt (halite) deposits formed by evaporation of ancient seas, so it HAS been dissolved; the rebuttal is false and actually concedes the pupil's point. Replace with the crushing evidence the hook already gives. IC-C1. |
| 10 | `hookReveal` | "A crystal is a pattern that repeats in three dimensions. Salt's repeat is a cube of alternating sodium and chloride ions, so it grows, and breaks, along square faces." | 4.2.1.3 | OK | Correct and within "familiar with the structure of sodium chloride". |
| 11 | explainer ¶1 | "When sodium reacts with chlorine, the ions do not pair off. Each Na⁺ pulls on every Cl⁻ near it, and each Cl⁻ pulls on every Na⁺." | 4.2.1.3 "forces act in all directions" | OK | |
| 12 | explainer ¶1 | "giant ionic lattice: a regular, three-dimensional arrangement in which positive and negative ions alternate in every direction. The strong electrostatic forces act in all directions at once." | 4.2.1.3 verbatim sense | OK | "alternate in every direction" is true of NaCl specifically, which is the context. |
| 13 | explainer ¶1 | "a single grain holds around 10¹⁸ ions" | numeric check | OK | 0.3 mm cube: 2.7×10⁻⁵ cm³ × 2.17 g cm⁻³ = 5.9×10⁻⁵ g ÷ 58.44 = 1.0×10⁻⁶ mol → 6×10¹⁷ formula units = 1.2×10¹⁸ ions. Order of magnitude right. |
| 14 | explainer ¶1 | "The cube you see is the repeat you cannot." | 4.2.1.3 | OK | Figurative; not a false claim. |
| 15 | lens h2 / commit prompt | "In a real salt crystal, how many chloride ions sit right next to one sodium ion?" | 4.2.1.3 (NaCl structure) | OK | |
| 16 | `lensOpts` | options 2, 4, 6, 8; `lensRight = s.lensPick === 6` | NaCl coordination 6:6 | OK | 6 is correct. 8 is a fair distractor (CsCl). |
| 17 | `lensSvg` view 0 | 5 × 5 grid, ion at (r,k) positive when (r+k) even; labels Na⁺/Cl⁻ | 4.2.1.3 | OK | Counted: 13 Na⁺, 12 Cl⁻; every row and column alternates; no like ions adjacent. Na⁺ drawn smaller (r 20) than Cl⁻ (r 29). |
| 18 | `lensSvg` view 1 | centre (2,2) is Na⁺; its four orthogonal neighbours highlighted; label "4 in this layer" | 4.2.1.3 | OK | Centre (2+2 even) = Na⁺; the four |Δ|=1 cells are Cl⁻. Correct. |
| 19 | `lensSvg` view 2 | two extra Cl⁻ drawn right of the grid labelled "layer above" / "layer below", arrows to centre; label "4 + 2 = 6" | 4.2.1.3 | OK | Schematic placement, but count and ion identity correct. |
| 20 | `lensSvg` alt texts | "…six chloride neighbours: four in its own layer and one directly above and below" | 4.2.1.3 | OK | |
| 21 | `lensNotes[0]` | "Positive and negative ions alternate along every row and every column: no two like charges touch." | 4.2.1.3 | OK | True of the NaCl layer drawn. |
| 22 | `lensNotes[1]` | "the centre Na⁺ touches four Cl⁻ ions: left, right, above and below it on the page." | 4.2.1.3 | IMPRECISE (self-contradicting) | Uses "above and below" for IN-PLANE neighbours, while the very next tab ("Add the layers above and below") and the figure ("layer above"/"layer below") use "above/below" for the OUT-OF-PLANE neighbours. A pupil told the four in-layer ions include "above and below" then told to "add the layers above and below" can double-count or conclude 4. IC-C2. |
| 23 | `lensNotes[2]` | "there is a layer in front and a layer behind. Each adds one more Cl⁻. Every Na⁺ has six Cl⁻ neighbours, and every Cl⁻ has six Na⁺." | 4.2.1.3 | IMPRECISE (contradicts own figure) | Science correct (6:6), but the tab and figure call these the layers "above" and "below"; the note calls the same two ions "in front" and "behind". Align to the figure. IC-C3. |
| 24 | `lensNotes[2]` tail | "Your six was right." / "You said n; the layers above and below are what most people miss." | 4.2.1.3 | OK | Tail already uses "above and below" — consistent with C3. |
| 25 | lens tab labels | "One layer", "Neighbours in the layer", "Add the layers above and below" | 4.2.1.3 | OK | Reference wording that C2/C3 align to. |
| 26 | misconception quote | "The formula is NaCl, so salt is made of NaCl molecules: one sodium stuck to one chlorine." | 4.2.1.3 | OK | Stated as the wrong idea (amber). |
| 27 | `thinkOptions[0]` (correct) | "There are exactly as many Na⁺ ions as Cl⁻ ions in the whole lattice: a 1 : 1 ratio, not a molecule." | 4.2.1.3 "empirical formula" | OK | |
| 28 | `thinkOptions[1]` reply | "The attraction acts equally on all six neighbours. There is no partner." | 4.2.1.3 "forces act in all directions" | OK | |
| 29 | `thinkOptions[2]` reply | "A molecule is a fixed group of atoms held by covalent bonds. There are none in salt." | 4.2.1.3 / 4.2.1.4 | OK | |
| 30 | `thinkOptions[3]` reply | "The ions go straight into the lattice. No NaCl unit ever exists on its own." | 4.2.1.3 | IMPRECISE | "ever" over-claims: NaCl ion-pair units do exist in the vapour at high temperature. Scope it to the solid. IC-C4. |
| 31 | `thinkReveal` | "Every ion is held by all its neighbours at once, so there is no such thing as one NaCl unit. The formula counts ions: one sodium ion for every chloride ion in the lattice." | 4.2.1.3 | OK | "in the lattice" scopes it correctly. |
| 32 | Ks4Choice right/wrong words | "That is it." / "That keeps the wrong idea." | — | OK | Not science. |
| 33 | deduce intro | "The exam shows part of a lattice and asks for the empirical formula. Count each kind of ion in the diagram, then cancel down." | 4.2.1.3 bullet 3 | OK | Matches the spec skill exactly. |
| 34 | `dxSvg` builder | draws each figure from the item's own `grid` strings with the page's `ion()` helper — NOT `KS4D.lattice()` | — | OK | Checked specifically: the strict 1:1 `(r+c)%2` pattern of `KS4D.lattice` is NOT used for DX, so the 1:2 and 2:1 figures are not drawn as 1:1. |
| 35 | `DX[0]` MgO figure | grid `MXMX/XMXM/MXMX` | 4.2.1.3 bullet 3 | OK | Counted: M 2+2+2 = 6, X 2+2+2 = 6 → 1:1. |
| 36 | `DX[0].why` | "6 Mg²⁺ and 6 O²⁻: 6 : 6 cancels to 1 : 1, so MgO. The 2+ and 2− charges agree." | 4.2.1.2 charges from group; 4.2.1.3 | OK | Mg Group 2 → 2+, O Group 6 → 2−. |
| 37 | `DX[0].accept` | ['MgO'] | — | OK | |
| 38 | `DX[1]` CaF₂ figure | grid `XMX/XMX/XMX` | 4.2.1.3 bullet 3 | OK | Counted: M 1×3 = 3, X 2×3 = 6 → 1:2. Figure agrees with answer. |
| 39 | `DX[1].why` | "3 Ca²⁺ and 6 F⁻: 3 : 6 cancels to 1 : 2, so CaF₂. Check: 2+ balances 2 × 1−." | 4.2.1.2 / 4.2.1.3 | OK | Ca Group 2, F Group 7. |
| 40 | `DX[2]` Li₂O figure | grid `MXM/MXM/MXM` | 4.2.1.3 bullet 3 | OK | Counted: M 2×3 = 6, X 1×3 = 3 → 2:1. Figure agrees. |
| 41 | `DX[2].why` | "6 Li⁺ and 3 O²⁻: 6 : 3 cancels to 2 : 1, so Li₂O. Check: two 1+ balance one 2−." | 4.2.1.2 / 4.2.1.3 | OK | |
| 42 | DX figures, ion sizes | cations r 20, anions r 29 for every compound | — | OK | Only the NaCl size claim is made (legal line). CaF₂/Li₂O/MgO are not structures pupils must know ("do not need to know the structures of other ionic compounds"); stylised grids are the exam convention. |
| 43 | `norm()` + accept | subscripts normalised to digits; whitespace removed; case-sensitive | — | OK | `mgo` rejected is correct chemistry (symbol case matters). |
| 44 | `dxText` (wrong) | "Count each kind of ion separately and write the two numbers as a ratio. Then divide both by the biggest number that goes into both." | 4.2.1.3 / MS 1a | OK | |
| 45 | explainer ¶2 | "A dot-and-cross diagram shows where the electrons went but not the lattice." | 4.2.1.3 bullet 2 | OK | |
| 46 | explainer ¶2 | "A 2D diagram shows the alternating pattern but only one layer." | 4.2.1.3 bullet 2 | OK | |
| 47 | explainer ¶2 | "A ball-and-stick model shows the 3D repeat but draws the ions far apart and joins them with sticks, as if the force ran along a line." | 4.2.1.3 bullet 2 | OK | Both standard AQA-credited limitations. |
| 48 | explainer ¶2 | "Every model trades one truth for another. AQA asks you to say which." | 4.2.1.3 bullet 2 | OK | |
| 49 | `mFigA` | `ionicTransfer('Na','Cl',2)`: [Na]⁺ 2.8 all crosses; [Cl]⁻ 2.8.8 with 7 dots + 1 cross, both bracketed | 4.2.1.2 (dot and cross for NaCl) | OK | Read `ks4-diagrams.js` `ionicTransfer` stage 2: metal loses outer shell, non-metal outer shell gains `lose` crosses, brackets and charges `+`/`−`. Matches the AQA exemplar. |
| 50 | `mFigB` | `KS4D.lattice('Na⁺','Cl⁻',5,4)`: 20 ions, 1:1 alternating, joined by thin grey grid lines, ions spaced apart | 4.2.1.3 | OK (advisory) | Chemistry right for NaCl. Note: the library draws connecting lines and gaps, so figure B also shows "gaps" and "lines" — which is why sort items 5–6 must say they are about the 3D model (IC-C6, IC-C7). A space-filling 2D plate would be better in the shared library; out of this file's scope. |
| 51 | `mFigC` `ballStick()` | 3 × 3 × 3 cube, 27 balls; small (r 13, metal colour) where (i+j+k) even, large (r 19) where odd; sticks to nearest neighbours only | 4.2.1.3 (NaCl ball-and-stick) | OK | Counted 14 small, 13 large; each interior ball bonded to 6. Correct NaCl topology. |
| 52 | figure captions | "A · dot-and-cross", "B · 2D lattice", "C · ball-and-stick" | 4.2.1.3 bullet 2 | OK | |
| 53 | Ks4Sort prompt | "Each statement is a limitation of exactly one of the three models above." | — | CONTRADICTS (with items 57–59) | Three items are true of more than one figure as drawn. Fixed by C5–C7 rather than by changing the prompt. |
| 54 | `mItems[0]` → a | "Shows only one pair of ions, not the giant lattice they are part of." / why "…never the lattice." | 4.2.1.3 bullet 2 | OK | Unique to A. |
| 55 | `mItems[1]` → a | "Suggests each ion belongs with one partner." / why "Drawn as a pair, the ions look like a molecule." | 4.2.1.3 bullet 2 | OK | Unique to A. |
| 56 | `mItems[2]` → b | "Shows a single layer, so each ion seems to have four neighbours, not six." / why "The layers in front and behind are missing." | 4.2.1.3 bullet 2 | OK | Unique to B. ("in front and behind" is fine here: no figure contradicts it. Left unchanged.) |
| 57 | `mItems[3]` → b | "Gives no idea of the crystal being three-dimensional." | 4.2.1.3 bullet 2 | CONTRADICTS | Equally true of A (the dot-and-cross pair is flat too), so it is not a limitation of "exactly one" model and a pupil who bins it under A is marked wrong for a correct statement. IC-C5. |
| 58 | `mItems[4]` → c | "Draws sticks, as if each force acts along one line to one neighbour." | 4.2.1.3 bullet 2 | CONTRADICTS (as drawn) | Figure B, as the library draws it, also joins every ion to its neighbours with lines. Tie the statement to the 3D model. IC-C6. |
| 59 | `mItems[5]` → c | "Leaves big gaps between ions that really touch." | 4.2.1.3 bullet 2 | CONTRADICTS (as drawn) | Figure B also leaves gaps (radii 0.26s + 0.36s = 0.62s < spacing s). Tie to the 3D model. IC-C7. |
| 60 | `mItems[4].why` | "Electrostatic forces act in all directions; there are no sticks." | 4.2.1.3 | OK | |
| 61 | `mItems[5].why` | "The ions in a real lattice are closely packed." | 4.2.1.3 | OK | |
| 62 | sort `done-note` | "An exam limitation names what the model shows wrongly or leaves out, then says what is really true." | 4.2.1.3 bullet 2 | OK | Correct exam technique. |
| 63 | command word "Describe" | "Give the features: regular, 3D, alternating, forces in all directions." | AQA command words | OK | |
| 64 | command word "Deduce" | "Reach the formula from the diagram you are given. Show the count." | AQA command words ("Draw/reach conclusion(s) from the information provided") | OK | |
| 65 | command word "Evaluate" | "Give strengths and limitations, then judge." | AQA command words ("Use the information supplied as well as your knowledge… to consider evidence for and against") | OK | |
| 66 | key fact | "An ionic compound is a giant lattice of alternating positive and negative ions held by strong electrostatic forces in all directions. Its formula is the simplest ratio of ions, not a molecule." | 4.2.1.3 | OK | |
| 67 | exam tip slot | `K.tip('ionic-compounds')` → frozen tip on conduction ("you must say the ions are free to move…") | 4.2.2.3 | OK (science) | Science correct and AQA-true, but it is 4.2.2.3 content, not taught on this page. See §4 row V1 — scope note, not a science change. |
| 68 | r1 source | `K.find(slug, route, 'Describe the structure of a giant ionic lattice')` | 4.2.1.3 | OK | Needle present in all four copies (CF3, CH3, TF3, TH3); the second needle ('Describe how the ions are arranged', CF9/TF9) and the TH fallback are never reached. |
| 69 | r1 item (verbatim) | correct: "A regular 3D arrangement of many oppositely charged ions, held by strong electrostatic forces acting in all directions" | 4.2.1.3 | OK | |
| 70 | r1 distractor replies | molecule / electron sea / polymer chains replies | 4.2.1.3, 4.2.1.4, 4.2.1.5 | OK | All correct. |
| 71 | r1 `why` | "Regular, three-dimensional, alternating, and held by strong forces in all directions." | 4.2.1.3 | OK | |
| 72 | r2 prompt | "part of the lattice of an ionic compound of potassium and oxygen. Deduce its empirical formula." marks 2 | 4.2.1.3 bullet 3 | OK | Exactly the spec skill. |
| 73 | r2 figure | grid `MMX/XMM/MXM`, M = K⁺, X = O²⁻ | 4.2.1.3 bullet 3 | OK | Counted M 2+2+2 = 6, X 1+1+1 = 3 → 2:1. Rows are successive one-place shifts of `MMX`, so it is a regular repeating 2:1 pattern, not a random scatter. |
| 74 | r2 accept | ['K2O'] | — | OK | |
| 75 | r2 `right` | "Two K⁺ for every O²⁻." | — | OK | |
| 76 | r2 `model[0]` | "Count: 6 K⁺ and 3 O²⁻, a ratio of 6 : 3, which cancels to 2 : 1." | — | OK | Recounted from the figure. |
| 77 | r2 `model[1]` | "Check the charges: 2 × (1+) balances 1 × (2−)." | 4.2.1.2 | OK | K Group 1, O Group 6. |
| 78 | r2 `model[2]` | "Empirical formula: K₂O." | — | OK | |
| 79 | r2 figure sizes | K⁺ drawn r 20, O²⁻ r 29 | — | OK | Real radii nearly equal (K⁺ 138 pm, O²⁻ 140 pm), but the legal line claims relative size only for NaCl, and the exam convention does not scale ions. No change. |
| 80 | r3 prompt | "Explain why sodium chloride has a high melting point." marks 3 | 4.2.2.3 | OK | Uses 4.2.2.3 content on a 4.2.1.3 page; acceptable connective (the next lesson), all links correct. |
| 81 | r3 link 1 | "Sodium chloride is a giant lattice of oppositely charged Na⁺ and Cl⁻ ions." | 4.2.1.3 | OK | |
| 82 | r3 link 2 | "There are strong electrostatic forces of attraction between the ions, acting in all directions." | 4.2.1.3 | OK | |
| 83 | r3 link 3 | "A lot of energy is needed to overcome these many strong forces, so the melting point is high." | 4.2.2.3 "large amounts of energy to break the many strong bonds" | OK | |
| 84 | r3 herring 1 | "A lot of energy is needed to break the covalent bonds." / why "There are no covalent bonds in sodium chloride: it is ionic." | 4.2.1.3 | OK | Classic AQA "do not accept". |
| 85 | r3 herring 2 | "The forces between the NaCl molecules are strong." / why "There are no NaCl molecules…" | 4.2.1.3 | OK | |
| 86 | r4 question | "Evaluate how well [ball-and-stick] represents the real structure. Give one strength and at least two limitations." marks 4 | 4.2.1.3 bullet 2 | OK | |
| 87 | r4 point 1 | "Strength: it shows the regular, three-dimensional, alternating arrangement of ions (or the 1 : 1 ratio)." | 4.2.1.3 | OK | The drawn 27-ball cube is 14:13, but the ratio strength refers to the repeating pattern, which AQA credits. |
| 88 | r4 point 2 | "Limitation: the sticks suggest bonds along lines, but electrostatic forces act in all directions." | 4.2.1.3 | OK | |
| 89 | r4 point 3 | "Limitation: the ions are shown far apart, but in the real lattice they are closely packed and touching." | 4.2.1.3 | OK | |
| 90 | r4 point 4 | "Limitation: it shows only a few ions; the real lattice is giant, with a huge number of ions." | 4.2.1.3 | OK | |
| 91 | r4 reject 1 | "“It shows molecules of NaCl.” There are none." | 4.2.1.3 | OK | |
| 92 | r4 reject 2 | "“The sticks are covalent bonds.” Sodium chloride is ionic." | 4.2.1.3 | OK | |
| 93 | r4 scoring | ≥ half of 4 = 2 (NOTES §10.3) | — | OK | |
| 94 | keyLines[0] | "Ionic compounds form a giant ionic lattice." | 4.2.1.3 | OK | Hard-coded; the frozen `key_note` (properties) is not used on this page. |
| 95 | keyLines[1] | "The lattice is a regular 3D arrangement of alternating positive and negative ions." | 4.2.1.3 | OK | |
| 96 | keyLines[2] | "Strong electrostatic forces act between the ions in all directions." | 4.2.1.3 | OK | |
| 97 | keyLines[3] | "In NaCl each ion has six neighbours of the opposite charge." | 4.2.1.3 (NaCl) | OK | |
| 98 | keyLines[4] | "The formula is the simplest ratio of ions: deduce it by counting ions in a diagram." | 4.2.1.3 bullet 3 | OK | |
| 99 | keyLines[5] | "Every model misses something: dot-and-cross shows no lattice, 2D shows one layer, ball-and-stick shows sticks and gaps." | 4.2.1.3 bullet 2 | OK | |
| 100 | Ks4KeyNote spec | "AQA 5.2.1.3" | 8464 5.2.1.3 | OK | |
| 101 | Ks4End tutor-line | "Stuck counting ions in a lattice diagram?" | — | OK | |
| 102 | `legal` | "Lattice figures are two-dimensional slices or small cut-outs of a crystal that extends in three dimensions." | 4.2.1.3 | OK | |
| 103 | `legal` | "In sodium chloride the chloride ion is larger than the sodium ion; the figures draw them at roughly the right relative size." | data (Na⁺ 102 pm, Cl⁻ 181 pm, ratio 0.56) | OK | Drawn ratios 0.69 (`ion()`), 0.72 (`lattice`), 0.68 (`ballStick`): "roughly" holds. |
| 104 | `legal` | "The ball-and-stick model is drawn with gaps and sticks on purpose, so that its limitations can be discussed." | 4.2.1.3 bullet 2 | OK | |
| 105 | Ks4End connects/prev/next | prev ionic bonding, next covalent bonding; connects properties of ionic compounds, giant covalent structures | — | OK | |
| 106 | route `sc-if` wrappers | none in this file | 4.2.1.3 | OK | Correct: no HT or chemistry-only content in 4.2.1.3. |

## 2. Required changes
| id | where (Design file + the exact `old` string, verbatim, unique in the file) | new string (verbatim) | why | spec section |
|---|---|---|---|---|
| ionic-compounds-C1 | IC, `hookOptions[3].reply`: `Rock salt that has never been dissolved is cubic as well.` | `A dry crystal crushed with no water near it breaks into cubes too.` | False: rock salt formed by evaporation of seawater, so it has been dissolved. The replacement uses the page's own crushing evidence. | 8462 4.2.1.3 / 8464 5.2.1.3 (NaCl structure), fetched PDF |
| ionic-compounds-C2 | IC, `lensNotes[1]`: `left, right, above and below it on the page.` | `left and right of it, and one row up and one row down.` | "above and below" is used for the out-of-plane layers in the next tab and figure; using it for in-plane neighbours self-contradicts. Same length class. | 8462 4.2.1.3 / 8464 5.2.1.3, fetched PDF |
| ionic-compounds-C3 | IC, `lensNotes[2]`: `so there is a layer in front and a layer behind.` | `so there is a layer above this one and a layer below it.` | Aligns the note with the tab ("Add the layers above and below") and figure labels ("layer above"/"layer below") that it narrates. | 8462 4.2.1.3 / 8464 5.2.1.3, fetched PDF |
| ionic-compounds-C4 | IC, `thinkOptions[3].reply`: `No NaCl unit ever exists on its own.` | `In the solid, no NaCl unit exists on its own.` | "ever" over-claims (NaCl ion pairs exist in the vapour); scoping to the solid keeps it true. | 8462 4.2.1.3 / 8464 5.2.1.3, fetched PDF |
| ionic-compounds-C5 | IC, `mItems[3].text`: `Gives no idea of the crystal being three-dimensional.` | `Shows the alternating pattern, but flat, with no depth.` | As written it is equally true of A (dot-and-cross), contradicting the "exactly one model" prompt. The new wording can only be B (A shows no alternating pattern; C has depth). `bin` and `why` unchanged. | 8462 4.2.1.3 bullet 2, fetched PDF |
| ionic-compounds-C6 | IC, `mItems[4].text`: `Draws sticks, as if each force acts along one line to one neighbour.` | `Joins the 3D cube with sticks, as if each force acts along one line.` | Figure B, as drawn by `KS4D.lattice`, also joins ions with lines; tying the item to the 3D model makes it unique to C. | 8462 4.2.1.3 bullet 2, fetched PDF |
| ionic-compounds-C7 | IC, `mItems[5].text`: `Leaves big gaps between ions that really touch.` | `Spreads the 3D cube out, with big gaps between ions that really touch.` | Figure B also leaves gaps between ions; tying it to the 3D model makes it unique to C. | 8462 4.2.1.3 bullet 2, fetched PDF |
| ionic-compounds-C8 | GENERATED route copy, not the Design file: `ks4-source.js` line 5 (`KS4SRC["ionic-compounds"]`), items CH8 and TH8 `wrong_explanations["3"]`; frozen origin `all_subtopics_chemistry_higher.py` / `all_subtopics_chemistry_triple_higher.py`. `old`: `Giant covalent substances do not conduct when molten (graphite excepted), and their bonds do not 'melt' into charge carriers.` (occurs **twice** in that line — once per route; the ruling must apply to both occurrences, which is the one departure from "exactly once") | `Giant covalent substances have no ions to free on melting (graphite conducts, but as a solid), and their bonds do not 'melt' into charge carriers.` | "graphite excepted" implies molten graphite conducts where others don't; graphite does not melt at normal pressure (it sublimes ≈ 3650 °C) and conducts as a solid. | 8462 4.2.3.2 (graphite conducts: delocalised electrons), fetched PDF |
| ionic-compounds-C9 | GENERATED route copy, not the Design file: `ks4-source.js` line 5, items CH10 and TH10 `wrong_explanations["2"]`; frozen origin as C8. `old`: `Water dissolves many ionic compounds (non-metal-containing), not just metals.` (occurs twice — CH and TH; apply to both) | `Water dissolves many ionic compounds, such as sodium chloride; it does not dissolve metals.` | The parenthetical is meaningless (every ionic compound contains a non-metal) and the sentence implies water dissolves metals. | 8462 4.2.1.3 / 4.2.2.3, fetched PDF |

All seven `old` strings for IC were count-verified with `grep -oF … | wc -l` = 1 against the Design file (`lensNotes[1]` is stored with `⁺`/`⁻` escapes earlier in the same string, so the `old` is taken from the plain-ASCII tail, which is unique). C8 and C9 were count-verified = 2 in `ks4-source.js` (one per route copy).

## 3. Route tags
| content | Design's tag | spec label | verdict | change id if any |
|---|---|---|---|---|
| Whole lesson (giant ionic lattice, NaCl structure, empirical formula from diagrams, model limitations) | base (no `sc-if`) | 8462 4.2.1.3 / 8464 5.2.1.3 — no HT, not "chemistry only" | OK | — |
| Lattice lens (6 neighbours in NaCl) | base | "familiar with the structure of sodium chloride" | OK | — |
| Deduce the formula (MgO, CaF₂, Li₂O; r2 K₂O) | base | 4.2.1.3 bullet 3 (no HT) | OK | — |
| Model limitations sort / r4 evaluate | base | 4.2.1.3 bullet 2 (no HT) | OK | — |
| r3 (high melting point of NaCl) | base | 4.2.2.3 (no HT) | OK | — |
| Content that should be tagged but isn't | — | none found | OK | — |

## 4. Verbatim layer (the repo's four files)
`ks4-source.js` quiz/tip/key_note proven byte-identical to the four `all_subtopics_chemistry*.py` dicts (CF 10, CH 10, TF 12, TH 12). `higher`, `triple_only`, `rp` are all `None` on all four — consistent with §3.

| route | field | finding | change id if any |
|---|---|---|---|
| all | `examiner_tip` | Science correct ("ions are free to move"), but it is 4.2.2.3 (properties) content; this page teaches 4.2.1.3. Not a science defect. Scope note for Mide/content_standards §8 (tip should be on this page's spec point). | — |
| all | `key_note` | Frozen key note is 4.2.2.3 content (MP, brittle, conduction). NOT served: the page hard-codes its own 6 key lines (§1 rows 94–99). Correct choice. | — |
| all | `common_mistake` | Solid-ionic conduction; correct; not served on this page. | — |
| CF1–CF10 / CH1–CH5 / TF1–TF10 / TH1–TH5 | quiz | Shared items checked: all keyed answers correct; all `wrong_explanations` correct. Most items test 4.2.2.3 (properties) rather than 4.2.1.3 — base content on every route, so no route violation. | — |
| CF4, CH4, TF4, TH4 | quiz | Brittleness by layer shift and like-charge repulsion: beyond the 4.2.2.3 statement but standard and correct. | — |
| CH6, TH6 | quiz | MgO > NaCl by ionic charge: correct, but not a 4.2.1.3/4.2.2.3 statement (NOTES flag 9 names the same item in L7). Not HT-labelled in spec, so it is not wrong on CH; keep verbatim. | — |
| CH7, TH7 | quiz | Ionic brittle vs metal malleable: correct (4.2.2.3 + 4.2.2.7). | — |
| CH8, TH8 | `wrong_explanations[3]` | "(graphite excepted)" implies molten graphite conducts. | ionic-compounds-C8 |
| CH9, TH9 | quiz | Correct. | — |
| CH10, TH10 | quiz | Solubility is beyond spec but a fair "Suggest"; key correct. `wrong_explanations[2]` is garbled. | ionic-compounds-C9 |
| TF11 | quiz | Ions separate and are surrounded by water: correct, base. Suitable on TF. | — |
| TF12 | quiz | High MP from strong forces: correct, base. | — |
| TH11 | quiz | NaCl formula = simplest ratio, not a molecule: correct and the most on-spec item in the bank. Only on TH — it is base content and would be suitable on every route, but absence from CF/CH/TF is not a route violation. | — |
| TH12 | quiz | CaO vs KCl by charge: correct; same scope note as CH6. | — |
| CF9, TF9 | quiz | NaCl ions alternate in regular 3D pattern: correct. | — |
| all | option order | Correct option is index 0 in every frozen item and usually the longest (e.g. CF3, CF2, CH6). `KS4.item` re-orders by stable hash, so position no longer leaks; length still does. See flag 16. | — |

## 5. Flags decided (from NOTES §9 that touch this lesson)
| flag | decision | spec section |
|---|---|---|
| 16 (option order) | **Keep the hash re-order on.** "Verbatim" governs the wording an examiner credits, not option position; AQA MCQs carry no meaning in option order, and the frozen index-0 key is a known leak (council defect 6). No option text changes. The length leak (correct option longest in e.g. CF2, CF3, CH6, CH8) remains a frozen-content defect outside this pass. | content_standards §1 (length parity); 8462 4.2.1.3 unaffected |
| 18 (new science) | Examined item by item in §6. Seven changes to Design's new material (C1–C7); everything else verified. | 8462 4.2.1.3 / 8464 5.2.1.3 |
| 9 (charge size vs melting point) | Touches this lesson's bank too (CH6, TH6, TH12). Decision: keep verbatim, correct science, not taught in the body — consistent with the L7 handling. | 8462 4.2.2.3 (no statement on charge size) |

## 6. New science introduced by Design (flag 18) — verified?
- Hook (cubic crystals), 4 options and replies — verified; option 4 reply WRONG → C1.
- Hook reveal (repeat is a cube of alternating ions; grows and breaks on square faces) — verified OK.
- Explainer ¶1 (no pairing off; lattice; forces in all directions; ~10¹⁸ ions per grain) — verified OK; 10¹⁸ recomputed (≈1.2 × 10¹⁸ for a 0.3 mm grain).
- Lattice lens (5 × 5 layer, 4 in-layer + 2 out-of-layer = 6; 6:6 coordination) — science verified OK; wording self-contradiction → C2, C3.
- Spot-the-flaw (NaCl is not a molecule) — verified OK; one over-claim → C4.
- Deduce the formula: MgO (6:6), CaF₂ (3:6), Li₂O (6:3) — each figure's ions counted from its grid, each matches its answer; the `KS4D.lattice` 1:1 trap does NOT apply (the page draws DX with its own grid builder). Verified OK.
- Explainer ¶2 (limitations of dot-and-cross / 2D / ball-and-stick) — verified OK against 4.2.1.3 bullet 2.
- Model limitations sort (6 items, 3 bins) — two items unique and correct per bin; three items true of more than one figure → C5, C6, C7.
- Ladder r2 (K₂O from a drawn lattice, 6 K⁺ : 3 O²⁻) — recounted, verified OK.
- Ladder r3 chain (NaCl high MP) + 2 herrings — verified OK.
- Ladder r4 (evaluate ball-and-stick, 4 points, 2 rejects) — verified OK.
- Command-word cards, key fact, 6 key lines, legal line — verified OK.
