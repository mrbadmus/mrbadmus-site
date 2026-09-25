# Examination — Covalent bonding (covalent-bonding) — AQA 8464 5.2.1.4 / 8462 4.2.1.4
Verdict: CHANGES REQUIRED
Examiner: Opus, 25 Sep 2026. Spec sources fetched: AQA-8462-SP-2016.PDF (v1.1, 04 Oct 2019) §4.2.1.1, 4.2.1.4, 4.2.2.4; AQA-8464-SP-2016.PDF (v1.1, 04 Oct 2019) §5.2.1.1, 5.2.1.4 — text identical between the two; no (HT only) marker and no "chemistry only" label anywhere in 4.2.1.4 / 5.2.1.4. 4.2.2.4 cited from the same fetched 8462 PDF.

Spec statements relied on (verbatim, 8462 4.2.1.4 = 8464 5.2.1.4):
- "When atoms share pairs of electrons, they form covalent bonds. These bonds between atoms are strong."
- "Covalently bonded substances may consist of small molecules." / "Some covalently bonded substances have very large molecules, such as polymers." / "Some covalently bonded substances have giant covalent structures, such as diamond and silicon dioxide."
- "Students should be able to: draw dot and cross diagrams for the molecules of hydrogen, chlorine, oxygen, nitrogen, hydrogen chloride, water, ammonia and methane; represent the covalent bonds in small molecules … using a line to represent a single bond; describe the limitations of using dot and cross, ball and stick, two and three-dimensional diagrams to represent molecules or giant structures; deduce the molecular formula of a substance from a given model or diagram …"
- 4.2.1.1: "For covalent bonding the particles are atoms which share pairs of electrons." "Covalent bonding occurs in most non-metallic elements and in compounds of non-metals." "Students should be able to explain chemical bonding in terms of electrostatic forces and the transfer or sharing of electrons."
- 4.2.2.4 (8462) / 5.2.2.4 (8464): small molecules have "relatively low melting and boiling points … These substances have only weak forces between the molecules (intermolecular forces). It is these intermolecular forces that are overcome, not the covalent bonds, when the substance melts or boils. The intermolecular forces increase with the size of the molecules …"

## 1. Checked items
| # | Where (element / constant name / template line) | Claim as written | Spec section | Verdict | Note |
|---|---|---|---|---|---|
| 1 | header eyebrow | "AQA Chemistry 5.2.1.4 · Process" | 8464 5.2.1.4 / 8462 4.2.1.4 | IMPRECISE (numbering only) | Correct for Combined; Triple routes' spec number is 4.2.1.4. Same pattern on all 14 pilot pages — a generator-level decision, not a science change; no change raised here. |
| 2 | `h1` / `<title>` | "Covalent bonding" | 5.2.1.4 | OK | Spec heading. |
| 3 | `.ks3-bigq` | "When two atoms both want electrons, neither will give any away. How do they still end up with full shells?" | 4.2.1.1 / 4.2.1.4 | OK | Framing question; answer (sharing) is the spec statement. |
| 4 | header badges | "Combined · Triple", "Foundation · Higher" | 5.2.1.4 (no HT / chem-only label) | OK | Whole lesson is base on every route. |
| 5 | hook h2 | "Two hydrogen atoms. One electron each. Both need two." | 4.1.1.4 electronic structure; 4.2.1.4 | OK | H: 1 electron; first shell holds 2. |
| 6 | hook para | "Hydrogen gas … made of H₂ molecules, and pulling one apart takes a lot of energy." | 4.2.1.4 "These bonds … are strong" | OK | H–H bond enthalpy ≈ 436 kJ/mol. |
| 7 | hook para | "Neither atom is a metal, so neither will hand its electron over." | 4.2.1.1 ionic = metal + non-metal | OK | |
| 8 | `hookOptions[0]` | "They share their two electrons, and both count the pair as their own" / reply "Watch that idea build a real molecule below." | 4.2.1.4 | OK | Correct answer; ungraded hook. |
| 9 | `hookOptions[1]` | "One gives its electron to the other, making ions" / "Then one would have none left. Both are non-metals and hold on." | 4.2.1.1 | OK | |
| 10 | `hookOptions[2]` | "They borrow electrons from the air around them" / "No outside electrons are involved." | 4.2.1.4 | OK | |
| 11 | `hookOptions[3]` | "They cannot: H₂ has half-empty shells" / "If so, H₂ would fall apart easily. It takes a lot of energy to split." | 4.2.1.4 | OK | |
| 12 | `hookReveal` | "…overlap and share their electrons as a pair. Each atom now counts two electrons in its shell. The pair is attracted to both nuclei, which holds the molecule together." | 4.2.1.1 "explain … in terms of electrostatic forces and … sharing" | OK | Electrostatic attraction of shared pair to both nuclei — exactly the spec's explain statement. |
| 13 | explainer 1 | "Two non-metal atoms overlap their outer shells and share a pair of electrons, one from each." | 4.2.1.4 | OK | |
| 14 | explainer 1 | "Both atoms count the shared pair as their own. The pair sits between the two nuclei and is attracted to both of them, and that attraction holds the atoms together: one shared pair is one covalent bond." | 4.2.1.1, 4.2.1.4 | OK | |
| 15 | explainer 1 | "Covalent bonds are strong." | 4.2.1.4 "These bonds between atoms are strong." | OK | Verbatim spec sense. |
| 16 | explainer 1 | "An atom forms as many bonds as it needs electrons: hydrogen one, oxygen two, nitrogen three, carbon four." | 4.2.1.4 (dot-and-cross list) | OK | Valencies correct for H, O, N, C. |
| 17 | `wSteps[0]` | "Oxygen is in Group 6: six outer electrons, two short of eight. Each hydrogen has one electron, one short of two." | 4.1.1.4, 4.2.1.4 | OK | |
| 18 | `waterSvg(0)` labels | "O: 6 outer, needs 2 more", "H: 1, needs 1"; O drawn outer shell 6 dots, each H 1 cross | 4.2.1.4 (water) | OK | Counts drawn match labels. |
| 19 | `waterSvg(1)` | arrows H→O; alt "The hydrogen atoms move in so their shells overlap the oxygen shell" | 4.2.1.4 | OK | |
| 20 | `wSteps[1]` | "In each overlap, the hydrogen puts in one electron and the oxygen puts in one." | 4.2.1.4 | OK | |
| 21 | gate prompt | "How many covalent bonds will the oxygen atom form?" options 1, 2, 6 | 4.2.1.4 | OK | Key = 2 (`wRight = s.wPick === 2`). |
| 22 | gate reply (2) | "Yes, two. Oxygen needs two more electrons, so it shares one pair with each hydrogen." | 4.2.1.4 | OK | |
| 23 | gate reply (6) | "Six is how many outer electrons it has, not how many it needs. It is two short, so it forms two bonds." | 4.2.1.4 | OK | Names the real error (valence vs deficit). |
| 24 | gate reply (1) | "One bond would give oxygen only seven. It needs two shared pairs to reach eight." | 4.2.1.4 | OK | 6 + 1 = 7. |
| 25 | `wSteps[2]` | "Two shared pairs, so two single covalent bonds. Oxygen now counts eight outer electrons: four in the two shared pairs and four in two lone pairs … Each hydrogen counts two." | 4.2.1.4 (water) | OK | 2×2 + 2×2 = 8; H 2. |
| 26 | `waterSvg(2)` → `KS4D.covalent('H2O')` | 2 bonding pairs (dot+cross each), 2 lone pairs on O | 4.2.1.4 | OK | Electron counts verified in `ks4-diagrams.js` MOLDEF (commander check). Alt text matches. |
| 27 | `VAL` | H 1, C 4, N 5, O 6, Cl 7 | 4.1.1.4 / group numbers | OK | |
| 28 | `need()` | H → 2, every other atom → 8 | 4.1.1.4 | OK | H chip reads "n of 2", not 8 — correct. |
| 29 | builder totals | atom total = own outer electrons + one per shared pair it takes part in | 4.2.1.4 | OK | Correct counting rule (each pair contributes one partner electron). |
| 30 | `MOLS` HCl | single H–Cl | 4.2.1.4 (hydrogen chloride) | OK | H 1+1=2, Cl 7+1=8. |
| 31 | `MOLS` Cl2 | single Cl–Cl | 4.2.1.4 (chlorine) | OK | 7+1=8 each. |
| 32 | `MOLS` O2 | double O=O | 4.2.1.4 (oxygen) | OK | 6+2=8 each. |
| 33 | `MOLS` N2 | triple N≡N | 4.2.1.4 (nitrogen) | OK | 5+3=8 each. |
| 34 | `MOLS` NH3 | three single N–H | 4.2.1.4 (ammonia) | OK | N 5+3=8; H 2. |
| 35 | `MOLS` CH4 | four single C–H | 4.2.1.4 (methane) | OK | C 4+4=8; H 2. |
| 36 | `MOLS` CO2 | two double C=O | beyond the spec's eight | OK | Not one of the eight named molecules but correct and standard AQA exam context (CO₂ appears in AQA papers as a "deduce/draw" item); acceptable practice. |
| 37 | coverage | H₂ (hook), H₂O (worked), HCl, Cl₂, O₂, N₂, NH₃, CH₄ (builder) | 4.2.1.4 draw list | OK | All eight spec molecules appear on every route. |
| 38 | builder cap | bond order clamped 0–3 | 4.2.1.4 | OK | Triple is the maximum at GCSE. |
| 39 | `bWord` / `bText` (full) | "Every shell is full. This is <name>: a single/double/triple bond X–Y. Here is the dot-and-cross diagram an examiner wants." | 4.2.1.4 | OK | Order words index correctly (1 single, 2 double, 3 triple). |
| 40 | `bText` (over) | "At least one atom now counts more than a full shell. An atom shares only as many pairs as it is short of a full shell." | 4.2.1.4 | OK | |
| 41 | `bText` (short) | "At least one atom is still short. Each shared pair adds one electron to each atom it joins." | 4.2.1.4 | OK | |
| 42 | `bDC` → `KS4D.covalent(m.key)` for HCl, Cl2, O2, N2, NH3, CH4, CO2 | outer-shell dot-and-cross | 4.2.1.4 | OK | All keys exist in MOLDEF; counts verified. |
| 43 | `displayed()` | one line per shared pair; dashed line when 0 | 4.2.1.4 "using a line to represent a single bond" | OK | |
| 44 | explainer 2 | "Most covalent substances are small molecules like these: a fixed number of atoms, strong bonds inside, and separate molecules that are only weakly attracted to each other." | 4.2.1.4, 4.2.2.4 | OK | |
| 45 | explainer 2 | "Some are very large molecules, such as the polymers in plastic." | 4.2.1.4 "very large molecules, such as polymers" | OK | |
| 46 | explainer 2 | "Some are giant covalent structures, like diamond and sand, where the bonds never stop." | 4.2.1.4 "such as diamond and silicon dioxide" | IMPRECISE | "Sand" is a mixture, not a substance; the spec names silicon dioxide. → C1. |
| 47 | explainer 2 | "The strong bond is always the one between atoms." | 4.2.1.4, 4.2.2.4 | OK | |
| 48 | `.ks3-mis-quote` | "Water boils at only 100 °C, so its covalent bonds must be weak." | 4.2.2.4 | OK | Correctly presented as the misconception. |
| 49 | Ks4Sort prompt/bins | "Accurate" / "The weak-bond mistake" | 4.2.2.4 | OK | |
| 50 | `sItems[0]` | "The O–H bonds inside each water molecule are strong." → ok; why "Every covalent bond is strong." | 4.2.1.4 | OK | Spec: "These bonds between atoms are strong." |
| 51 | `sItems[1]` | "When water boils, the O–H bonds break." → mis; why "Steam is H₂O. The molecules separate; the bonds inside them stay." | 4.2.2.4 | OK | |
| 52 | `sItems[2]` | "Water boils at a low temperature because the forces between its molecules are weak." → ok | 4.2.2.4 | OK | AQA credits "weak intermolecular forces". |
| 53 | `sItems[3]` | "Covalent bonds are weaker than ionic bonds, which is why water melts so easily." → mis; why "Melting ice does not touch the covalent bonds at all." | 4.2.2.4 | OK | |
| 54 | `sItems[4]` | "Splitting water into hydrogen and oxygen takes far more energy than boiling it." → ok; why "Splitting breaks the strong covalent bonds; boiling does not." | 4.2.2.4 | OK | ~928 kJ/mol (2 O–H) vs ~41 kJ/mol vaporisation. |
| 55 | `sItems[5]` | "Steam is made of separate H and O atoms." → mis | 4.2.2.4 | OK (bin) | |
| 56 | `sItems[5].why` | "If it were, it could not condense back into water on a cold window." | 4.2.2.4 | IMPRECISE | Non-sequitur: it gives no chemistry and the inference is unsound (free atoms could recombine on cooling). It should state the spec reason — boiling overcomes intermolecular forces, not covalent bonds. → C2. |
| 57 | sort `done-note` | "Boiling separates whole molecules. Steam is still H₂O: every O–H bond survives." | 4.2.2.4 | OK | |
| 58 | command word State | "A number or a fact. No explanation asked for." | AQA command words (State) | OK | |
| 59 | command word Draw | "Outer shells only. Shared pairs in the overlap, lone pairs on the atom." | 4.2.1.4 | OK | Advice, not a rule AQA enforces (inner shells are also credited), but outer-only is the credited convention and costs nothing. |
| 60 | command word Explain | "Count electrons: how many each atom has, needs, and shares." | AQA command words (Explain) | OK | Lesson-specific gloss; consistent with how AQA credits these explains. |
| 61 | key fact | "A covalent bond is a shared pair of electrons between two non-metal atoms. One pair is a single bond, two a double, three a triple, and every covalent bond is strong." | 4.2.1.1, 4.2.1.4 | OK | |
| 62 | exam tip (`K.tip`) | "Never call covalent bonds weak. To explain a low boiling point, the marks are for the weak intermolecular forces between molecules being overcome — the covalent bonds inside each molecule are strong and stay intact." | 4.2.2.4 | OK | Matches AQA mark-scheme practice ("reference to breaking covalent bonds = max 0/1"). |
| 63 | r1 needle | `'single covalent bonds present in a water molecule'` | — | OK | Present in CF4, CH4, TF4, TH4 — never falls back to TH. |
| 64 | r1 item | "State the number of single covalent bonds present in a water molecule, H₂O." key "2" | 4.2.1.4 | OK | |
| 65 | r1 wrong explanations | w1 "…giving 2 bonds — not 1."; w2 "Water has only 2 hydrogen atoms, so only 2 O–H bonds form."; w3 "That would need 4 hydrogen atoms; water has 2." | 4.2.1.4 | OK | |
| 66 | r1 `why` | "Oxygen shares one pair with each of the two hydrogens." | 4.2.1.4 | OK | |
| 67 | r1 fallback needle | `'triple bond'` | — | OK | Never reached (primary needle present on all routes). |
| 68 | r2 prompt | "Silicon is in Group 4. It forms a simple molecule with hydrogen. Deduce the formula …" | 4.2.1.4 "deduce the molecular formula" | OK | Silane SiH₄ is real; valency reasoning identical to CH₄. New science (flag 18) — verified. |
| 69 | r2 `accept` | ['SiH4', 'H4Si'] | — | OK | Both orders credited; case-sensitive element symbols are the right standard. |
| 70 | r2 `right` / `wrong` | "Silicon has four outer electrons and needs four more, so it shares with four hydrogens." / "Count how many electrons silicon is short of eight…" | 4.2.1.4 | OK | |
| 71 | r2 `model` | "Silicon, Group 4: four outer electrons, four short of eight." "Each hydrogen shares one pair, so silicon forms four single bonds." "Formula: SiH₄." | 4.2.1.4 | OK | |
| 72 | r3 prompt | "Explain, in terms of electrons, why a nitrogen molecule, N₂, contains a triple bond." | 4.2.1.4 (nitrogen) | OK | |
| 73 | r3 links (order) | 5 outer, needs 3 → share three pairs → triple bond, each counts eight | 4.2.1.4 | OK | Order is logically forced. |
| 74 | r3 herring 1 | "One nitrogen atom transfers three electrons to the other." / "Both are non-metals, so electrons are shared, not transferred." | 4.2.1.1 | OK | |
| 75 | r3 herring 2 | "Each nitrogen atom shares five pairs, one for each outer electron." / "An atom shares only as many pairs as it is short: three for nitrogen." | 4.2.1.4 | OK | |
| 76 | r4 question | "Describe the bonding in a molecule of ammonia, NH₃ … before and after bonding. (N is in Group 5.)" 4 marks | 4.2.1.4 (ammonia) | OK | |
| 77 | r4 point 1 | "Nitrogen has five outer electrons; each hydrogen has one." | 4.1.1.4 | OK | |
| 78 | r4 point 2 | "Nitrogen shares one pair of electrons with each of the three hydrogen atoms." | 4.2.1.4 | OK | |
| 79 | r4 point 3 | "That makes three single covalent bonds (shared pairs)." | 4.2.1.4 | OK | |
| 80 | r4 point 4 | "Afterwards nitrogen has eight outer electrons (including one lone pair) and each hydrogen has two." | 4.2.1.4 | OK | 3×2 + 2 = 8. |
| 81 | r4 reject 1 | "Nitrogen gives electrons to hydrogen." — ionic language | 4.2.1.1 | OK | AQA rejects transfer language in a covalent answer. |
| 82 | r4 reject 2 | "Ammonia has four bonds because N has a lone pair." — a lone pair is not a bond | 4.2.1.4 | OK | |
| 83 | keyLines[0] | "Covalent bonds form between non-metal atoms." | 4.2.1.1 | OK | |
| 84 | keyLines[1] | "A covalent bond is a shared pair of electrons, attracted to both nuclei." | 4.2.1.1, 4.2.1.4 | OK | |
| 85 | keyLines[2] | "Single bond: 1 shared pair. Double: 2. Triple: 3." | 4.2.1.4 | OK | |
| 86 | keyLines[3] | "An atom forms as many bonds as it is short of a full shell: H 1, O 2, N 3, C 4." | 4.2.1.4 | OK | |
| 87 | keyLines[4] | "Draw dot-and-cross with outer shells only: H₂, Cl₂, O₂, N₂, HCl, H₂O, NH₃, CH₄." | 4.2.1.4 draw list | OK | Exactly the spec's eight. Untagged — correct (flag 6). |
| 88 | keyLines[5] | "Covalent bonds are strong. Weak forces act between molecules, not inside them." | 4.2.1.4, 4.2.2.4 | OK | |
| 89 | KeyNote `spec` prop | "AQA 5.2.1.4" | — | IMPRECISE (numbering only) | As row 1. |
| 90 | `legal` | "Dot-and-cross diagrams show outer shells only, the AQA convention for covalent molecules; one atom's electrons are dots and the other's crosses." | 4.2.1.4 | OK | AQA's own spec figures for covalent molecules show outer shells; describes this page's drawings. |
| 91 | `legal` | "The builder's line drawing is a displayed formula: each line is one shared pair." | 4.2.1.4 | OK | |
| 92 | `legal` | "Real molecules have shapes in three dimensions that neither drawing shows." | 4.2.1.4 limitations bullet | OK | A spec-named limitation. |
| 93 | End `tutor-line` | "Not sure how many pairs a molecule shares?" | — | OK | No science claim. |
| 94 | End prev/next/connects | Ionic compounds / Metallic bonding; connects 5.2.2.4, 5.2.2.6, 5.2.2.5 | 4.2.1.4 → 4.2.2.4–6 | OK | Sensible links. |
| 95 | `RAIL` labels | "Two hydrogen atoms", "Worked: water", "Shared-pair builder", "Strong bond or weak force", "Exam ladder" | — | OK | |
| 96 | Question bank | `K.bank(slug, route)` — verbatim route copy | — | OK | See §4 for item-level findings. |

## 2. Required changes
| id | where (Design file + the exact `old` string, verbatim, unique in the file) | new string (verbatim) | why | spec section |
|---|---|---|---|---|
| covalent-bonding-C1 | `ks4-chemistry-5.2.1.4-covalent-bonding.dc.html` — `like diamond and sand, where` (count-verified: 1 match) | `like diamond and silicon dioxide (sand), where` | "Sand" is a mixture; the spec names the substance, silicon dioxide, and pupils must be able to name it as a giant covalent example. Keeps Design's everyday anchor in brackets. | 8462 4.2.1.4 / 8464 5.2.1.4 "giant covalent structures, such as diamond and silicon dioxide" |
| covalent-bonding-C2 | `ks4-chemistry-5.2.1.4-covalent-bonding.dc.html` — `why: 'If it were, it could not condense back into water on a cold window.'` (count-verified: 1 match) | `why: 'Steam is H₂O molecules. Boiling only overcomes the weak forces between them; the O–H bonds stay.'` | The current reason is a non-sequitur and gives no chemistry; the feedback must carry the credited idea (intermolecular forces overcome, covalent bonds intact). | 8462 4.2.2.4 / 8464 5.2.2.4 "It is these intermolecular forces that are overcome, not the covalent bonds, when the substance melts or boils." |
| covalent-bonding-C3 | Route bank copy, not the Design file: `ks4-source.js` → `KS4SRC["covalent-bonding"].quiz.{CF,CH,TF,TH}[1].wrong_explanations["2"]` = `Atoms of the same element do repel slightly, but covalent bonding (sharing) creates a stronger overall attraction.` (4 occurrences in ks4-source.js — one per route copy; apply to each via a `ks4_rulings.py` substitution on the served item; the frozen `all_subtopics_*.py` stays untouched) | `Pairing up does not cancel a repulsion. Two O atoms bond because sharing two pairs gives each a full outer shell of 8.` | States as fact that neutral atoms of the same element repel — not a GCSE idea and not correct as a general statement; the feedback on a distractor must not teach a new misconception. | 8462 4.2.1.1 (bonding explained by electrostatic forces and sharing) / 4.2.1.4 |

## 3. Route tags
| content | Design's tag | spec label | verdict | change id if any |
|---|---|---|---|---|
| Whole lesson (sharing, single/double/triple bonds, valency) | base (all four routes) | 5.2.1.4 / 4.2.1.4 — no HT, not chemistry-only | OK | — |
| Dot-and-cross drawing of the eight molecules (worked water, builder `bDC`, keyLines[4]) | base | 5.2.1.4 — no HT marker (flag 6) | OK | — |
| CO₂ in builder | base | not named in spec; standard practice | OK | — |
| Small molecules / polymers / giant covalent recognition (explainer 2) | base | 5.2.1.4 | OK | — |
| Weak-bond misconception sort (intermolecular forces) | base | 8464 5.2.2.4 (Combined, both tiers) | OK | — |
| Limitations line in `legal` (3D shape) | base | 5.2.1.4 limitations bullet — no HT | OK | — |
| Electronegativity / bond polarity | absent | not in 8462 or 8464 at all | OK (correctly dropped) | — |
| Reverse check — untagged content that should be tagged | none found | — | OK | — |

## 4. Verbatim layer (the repo's four files)
| route | field | finding | change id if any |
|---|---|---|---|
| CH, TH | `higher` | "Draw dot-and-cross diagrams for: H₂ … CO₂ … Understand bond polarity in terms of electronegativity differences…" — (a) presents the dot-and-cross list as Higher-only, but 5.2.1.4 has no HT marker; (b) electronegativity/bond polarity is not in 8462 or 8464. The Design page does not render this field. The port must NOT serve `higher` for this subtopic on any route (or, if a Higher box is generated, strip it). Change to the generated route copy only; frozen py untouched. | flag 6 (no id — a "do not serve" ruling; commander to record in DEPARTURES) |
| CF, TF | `higher` | None — correct; dot-and-cross is taught on the page on every route regardless. | — |
| all | `triple_only`, `rp`, `fifas` | None / None / [] — correct (no chemistry-only content, no RP, no calculation). | — |
| all | `examiner_tip` | identical on all four; correct (4.2.2.4). | — |
| all | `key_note` | "…Single bond: 1 shared pair. Double bond: 2 shared pairs. Covalent bonds within molecules are STRONG. Intermolecular forces between molecules are WEAK → low melting points." — correct; not rendered (Design uses its own six `keyLines`, which add the triple bond and the spec's eight). | — |
| all | `common_mistake` | correct (4.2.2.4); not rendered separately (the sort carries it). | — |
| CF/CH/TF/TH | quiz 1 (CH₄ bonds) | Correct; w3 correct (4 bonds × 2 = 8). | — |
| CF/CH/TF/TH | quiz 2 (O₂) w2 | "Atoms of the same element do repel slightly…" — wrong as stated. | covalent-bonding-C3 |
| CF/CH/TF/TH | quiz 2 w1, w3 | Correct. | — |
| CF/CH/TF/TH | quiz 3 (definition) | "A shared pair of electrons between two non-metal atoms, attracted to both nuclei" — correct (4.2.1.1). | — |
| CF/CH/TF/TH | quiz 4 (water bonds) | Correct; ladder r1 source. | — |
| CF/CH/TF/TH | quiz 5 (Cl₂) | Correct. | — |
| CF, TF | quiz 6 "Non-metals only" | 4.2.1.1 says "most non-metallic elements and … compounds of non-metals"; "non-metals only" is the answer AQA credits at GCSE. w3 "Noble gases rarely bond" — correct. OK. | — |
| CF, TF | quiz 7–10 | Correct (pair of electrons; double bond; CO₂ covalent; triple = 3 pairs). | — |
| CH, TH | quiz 6 (N₂ triple) | Correct; duplicates ladder r3 content (fine — bank is unscored). | — |
| CH, TH | quiz 7 (CO₂ O=C=O) | Correct; w3 "would leave carbon with 6" — correct (4+2). | — |
| CH, TH | quiz 8 (low mp/bp) | Correct (4.2.2.4). | — |
| CH, TH | quiz 9 (2/4/6 electrons) | Correct. | — |
| CH, TH | quiz 10 (NH₃ 3 bonds) | Correct. | — |
| TF | quiz 11 (strong) | Correct. | — |
| TF | quiz 12 (H₂ dot-and-cross) | Correct; the only bank item that tests dot-and-cross representation directly. CF has none — acceptable (MCQ cannot test drawing; the page teaches and exercises all eight on CF). | — |
| TH | quiz 11 (halogen bp) | Correct — "intermolecular forces increase with the size of the molecules" (4.2.2.4, base content). | — |
| TH | quiz 12 (limitation of dot-and-cross) | Correct — limitations bullet is base 5.2.1.4; on TH only is a bank-selection difference, not a tagging error. | — |
| CH, TH | any electronegativity / polarity quiz item | None present in any copy. | — |
| all | `ks4-source.js` vs `all_subtopics_*.py` | Byte-identical on quiz, examiner_tip, key_note (commander's check). | — |

## 5. Flags decided (from NOTES §9 that touch this lesson)
| flag | decision | spec section |
|---|---|---|
| 6 — dot-and-cross is base; electronegativity dropped | UPHELD. Dot-and-cross for H₂, Cl₂, O₂, N₂, HCl, H₂O, NH₃, CH₄ is base on all four routes (no HT marker). Electronegativity and bond polarity appear nowhere in 8462 or 8464; correctly dropped. The frozen CH/TH `higher` field (which says both the opposite things) must not be served. | 8462 4.2.1.4 / 8464 5.2.1.4 (fetched PDF) |
| 16 — option order | UPHELD: keep the hash re-order. Order carries no science; AQA does not fix the key's position; no option in this lesson's bank refers to another's position ("both of the above" etc.), and numeric-option items (r1: 2/1/3/4) remain unambiguous in any order. The text stays verbatim. | — (assessment practice) |
| 18 — new science | Verified — see §6. Two feedback strings need changes (C1, C2); all numbers and answers correct. | 4.2.1.4, 4.2.2.4 |

## 6. New science introduced by Design (flag 18) — verified?
- Hook (H₂, four options + reveal) — verified correct.
- Worked water in 3 steps + bond-count gate (1/2/6 with three replies) — verified; all counts correct.
- Shared-pair builder: 7 molecules, valence/need model (H needs 2), totals rule, three verdict texts, dot-and-cross reveal — verified correct; CO₂ is beyond the eight but correct.
- Explainer 1 and 2 — correct except "sand" (C1).
- Weak-bond sort, 6 items: all bins correct; item 6's `why` is an unsound argument (C2).
- Command-word cards (State, Draw, Explain), key fact, six key-note lines, `legal` — verified correct.
- Ladder r2 (SiH₄ deduction, accept SiH4/H4Si) — verified correct.
- Ladder r3 (N₂ triple bond chain + 2 herrings) — verified correct.
- Ladder r4 (NH₃ describe, 4 points, 2 rejects) — verified correct; AQA-style points.
