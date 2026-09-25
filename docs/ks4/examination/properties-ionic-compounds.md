# Examination — Properties of ionic compounds (properties-ionic-compounds) — AQA 8464 5.2.2.3 / 8462 4.2.2.3
Verdict: CHANGES REQUIRED
Examiner: Opus, 25 Sep 2026. Spec sources fetched: AQA-8462-SP-2016.PDF and AQA-8464-SP-2016.PDF (filestore.aqa.org.uk, both Version 1.1, 04 Oct 2019), read as text. 8464 5.2.2.3 and 8462 4.2.2.3 are word-for-word identical. Mark-scheme conventions (ions "free to move / mobile"; "ions" or "charged particles" alone not credited; no credit for electrons moving in an ionic compound) are from memory of published AQA 8462/8464 mark schemes.

Design file: `KS4 Lessons/Pilot - Bonding and Electricity/ks4-chemistry-5.2.2.3-properties-ionic-compounds.dc.html`. Source: `src/chemistry-5.2.2.3-properties-ionic-compounds.md` and `ks4-source.js["properties-ionic-compounds"]`. I checked by script that `ks4-source.js` quiz copies CF/CH/TF/TH are identical to the four repo dicts (`all_subtopics_chemistry*.py`, id `properties-ionic-compounds`).

Spec statements relied on (8462 4.2.2.3, verbatim from the fetched PDF):
> "Ionic compounds have regular structures (giant ionic lattices) in which there are strong electrostatic forces of attraction in all directions between oppositely charged ions. These compounds have high melting points and high boiling points because of the large amounts of energy needed to break the many strong bonds. When melted or dissolved in water, ionic compounds conduct electricity because the ions are free to move and so charge can flow. Knowledge of the structures of specific ionic compounds other than sodium chloride is not required."

Also 4.2.2.1: "The stronger the forces between the particles the higher the melting point and boiling point of the substance." 4.2.2.8: "Metals are good conductors of electricity because the delocalised electrons in the metal carry electrical charge through the metal."

## 1. Checked items
| # | Where (element / constant name / template line) | Claim as written | Spec section | Verdict (OK / WRONG / IMPRECISE / CONTRADICTS) | Note |
|---|---|---|---|---|---|
| 1 | header eyebrow | "AQA Chemistry 5.2.2.3 · Contrast" | 8464 5.2.2.3 = 8462 4.2.2.3 | OK | The pilot numbers everything in 8464 form on all routes, which is the house convention. The Triple routes' ref would be 4.2.2.3. No change. |
| 2 | h1 / title | "Properties of ionic compounds" | 4.2.2.3 heading | OK | Matches the spec heading. |
| 3 | `ks3-bigq` | "Salt is made entirely of charged particles, yet a salt crystal will not light a bulb. Melt it, or dissolve it, and it will." | 4.2.2.3 | OK | NaCl is wholly ions, and it conducts when melted or dissolved. |
| 4 | route badges | "Combined · Triple", "Foundation · Higher", no Higher/Triple tag | 4.2.2.3 has no HT marker and no "chemistry only" | OK | Untagged is correct. |
| 5 | hook h2 + prose | "Push two carbon probes into a heap of dry salt crystals … The bulb stays dark. Every crystal is packed with Na⁺ and Cl⁻ ions" | 4.2.2.3 | OK | Solid does not conduct. Ion charges correct. |
| 6 | `hookOptions[0]` + reply | "The ions are held in fixed positions and cannot move" → "Test it: set the ions free…" | 4.2.2.3 | OK | This is the creditworthy idea. Ungraded by design, and the reveal confirms it. |
| 7 | `hookOptions[1]` reply | "They do balance overall, but that is true of molten salt too, and molten salt conducts." | 4.2.2.3 | OK | The counter-argument is sound. |
| 8 | `hookOptions[2]` reply | "It is made of nothing but charged particles: Na⁺ and Cl⁻ ions." | 4.2.2.3 | OK | |
| 9 | `hookOptions[3]` reply | "Crush them tight around the probes and the bulb still stays dark." | 4.2.2.3 | OK | Correct in fact: compacted dry NaCl remains an insulator. |
| 10 | `hookReveal` | "In the solid, the ions are locked into the lattice. They have charge but they cannot move, so no charge can flow." | 4.2.2.3 | OK | |
| 11 | explainer | "A current is a flow of charge, so it needs charged particles that can move." | 4.2.2.3 ("ions are free to move and so charge can flow") | OK | |
| 12 | explainer | "every ion is held in the lattice by strong electrostatic forces from all its neighbours. The ions vibrate but stay put." | 4.2.2.3 ("in all directions") | OK | Vibration about fixed positions is correct particle theory (4.2.2.1). |
| 13 | bench h2 / eyebrow | "Same compound. Change one thing. Watch the ions." | — | OK | Framing only. |
| 14 | `beaker()` circuit | Cell drawn as short thick line (x=184) wired to the left electrode, long thin line (x=196) wired through the bulb to the right electrode; left labelled −, right labelled + | circuit-symbol convention | OK | Long plate = positive terminal, and it feeds the electrode labelled +. The polarity is self-consistent. |
| 15 | `beaker()` solid lattice | 4×7 alternating +/− ions; Na⁺ drawn r=11, Cl⁻ r=15 | 4.2.2.3 (regular structure, oppositely charged ions) | OK | Alternation is correct. Na⁺ smaller than Cl⁻ is correct (≈102 pm vs 181 pm). |
| 16 | `beaker()` solid, bulb | `lit = kind !== 'solid' && on`, so the solid is never lit | 4.2.2.3 | OK | |
| 17 | `beaker()` molten / solution ion drift | `dir = pos ? -1 : 1`, so + ions move left (towards −) and − ions move right (towards +) | 4.2.2.3; electrolysis convention 4.4.3.1 | OK | Cations go to the cathode (−) and anions to the anode (+). |
| 18 | `beaker()` label | "Na⁺ moves to − · Cl⁻ moves to +" | 4.2.2.3 | OK | |
| 19 | `beaker()` alt (solid) | "The ions are fixed in a lattice. The bulb is off." | 4.2.2.3 | OK | |
| 20 | `beaker()` alt (on) | "positive ions towards the negative electrode and negative ions towards the positive electrode. The bulb is lit." | 4.2.2.3 | OK | |
| 21 | `beaker()` alt (not yet on) | "Free ions between two electrodes, before the switch is closed." | — | CONTRADICTS | No switch is drawn in `beaker()`: the circuit is complete. See C5. |
| 22 | `capB` | `(on ? ' · bulb on' : ' · switch open')` | — | CONTRADICTS | Same defect as row 21. The drawing is a complete circuit with free ions and an unlit bulb, and the caption names a switch that is not in the drawing. L13 fixed the same defect by drawing a switch (NOTES §10.11). A minimal text fix is C4. |
| 23 | figcaption A | "A · solid sodium chloride · bulb off" | 4.2.2.3 | OK | |
| 24 | `FORMS[0].q` | "The salt is heated until it melts. Will the bulb light?" | 4.2.2.3 | OK | |
| 25 | `FORMS[1].q` | "The salt is dissolved in water instead. Will the bulb light?" | 4.2.2.3 | OK | |
| 26 | `benchWord` | "It lights." / "It lights anyway." | 4.2.2.3 | OK | Both forms conduct, so both predictions resolve to "lights". |
| 27 | `benchReply` (molten) | "Melting breaks the lattice apart. The ions are now free to move" | 4.2.2.3 | OK | |
| 28 | `benchReply` (solution) | "Water pulls the ions out of the lattice and they spread through the solution, free to move" | 4.2.2.3 | OK | GCSE-appropriate. |
| 29 | `benchReply` tail | "Na⁺ drifts towards the negative electrode and Cl⁻ towards the positive one. Moving ions are a flow of charge. The only difference from beaker A is whether the ions can move." | 4.2.2.3 | OK | |
| 30 | misconception quote | "The molten salt conducts because electrons flow through it, like in a metal wire." | 4.2.2.3 vs 4.2.2.8 | OK | This is the targeted wrong idea, correctly set up as wrong. |
| 31 | `thinkOptions[0]` (correct) | "Ionic compounds have no free electrons. The charge is carried by the ions themselves moving." | 4.2.2.3 | OK | |
| 32 | `thinkOptions[0].reply` | "Every electron is held by an ion. The ions are what move." | 4.2.2.3 | OK | |
| 33 | `thinkOptions[1]` + reply | "the electrons are released when the salt melts" → "Melting frees the ions. It does not release electrons from them." | 4.2.2.3 | OK | |
| 34 | `thinkOptions[2]` + reply | "protons flow" → "Protons stay in the nuclei. Whole ions carry the charge." | 4.2.2.3; 4.1.1 | OK | |
| 35 | `thinkOptions[3]` + reply | "Only solutions conduct; molten salt does not." → "Both molten and dissolved salt conduct." | 4.2.2.3 | OK | |
| 36 | `thinkReveal` | "In a metal, delocalised electrons carry the current. In a molten or dissolved ionic compound, whole ions move and carry it." | 4.2.2.8, 4.2.2.3 | OK | The science is right. Outside my remit: `.replace(/&ldquo;\|&rdquo;/g, '“')` turns the closing quote into an opening one (“…charge“). This is typography only. |
| 37 | `cLinks[0]` | "Solid sodium chloride is a giant lattice of ions held by strong electrostatic forces." | 4.2.2.3 | OK | |
| 38 | `cLinks[1]` | "In the solid, the ions are in fixed positions and cannot move." | 4.2.2.3 | OK | |
| 39 | `cLinks[2]` | "When it melts, the lattice breaks down and the ions are free to move." | 4.2.2.3 | OK | |
| 40 | `cLinks[3]` | "The moving ions carry charge, so the molten compound conducts." | 4.2.2.3 | OK | The chain order is logically forced. |
| 41 | `cHerrings[0]` + why | "When it melts, electrons are released…" → "There are no free electrons in an ionic compound." | 4.2.2.3 | OK | |
| 42 | `cHerrings[1]` + why | "The solid has no charged particles." → "The solid is full of ions. They simply cannot move." | 4.2.2.3 | OK | |
| 43 | chain `done-note` | "Say the word move. “It has ions” alone scores nothing." | AQA MS convention | OK | This matches AQA practice: "ions" alone is not credited without "free to move / mobile". |
| 44 | chain prompt | "An examiner wants each state described, then the difference linked to the ions." | — | OK | |
| 45 | Be-the-examiner question | "Explain why sodium chloride conducts electricity when dissolved in water but not when solid. [3 marks]" | 4.2.2.3 | OK | A realistic AQA 3-mark item. |
| 46 | Be-the-examiner answer | "When it dissolves the bonds break and the solution has charged particles in it. Solid sodium chloride doesn't have any charged particles so it can't conduct." | 4.2.2.3 | OK (as a specimen) | This is a specimen answer to be marked, so its errors are intended. |
| 47 | `exOptions[0]` "0 marks", `correct:false`, reply "It does say something creditworthy about the solution." | — | 4.2.2.3; AQA MS | WRONG | Under this page's own 3-mark scheme (`exReveal`: ions fixed / free to move / carry charge), no point is met. "Has charged particles" without movement is not a marking point. The page says so itself three times: chain done-note, key-note line 6, `exReveal`. The claim that the solid has no charged particles is also false. The answer scores 0. See C1. |
| 48 | `exOptions[1]` "1 mark", `correct:true`, "One mark at most, for the solution containing charged particles…" | — | as above | CONTRADICTS | This rewards the exact idea the key note says "scores nothing". See C2. |
| 49 | `exOptions[2]` reply | "Too generous. Two of its three ideas are wrong." | — | OK | This still holds once 0 is the credited mark. |
| 50 | `exOptions[3]` reply | "It never says the ions can move, which is the whole point." | 4.2.2.3 | OK | |
| 51 | `exReveal` | "the solid does have charged particles; they just cannot move … The 3-mark answer: in the solid the ions are fixed in the lattice; when dissolved the ions are free to move; so they can carry charge through the solution." | 4.2.2.3 | OK | The model answer is creditworthy for 3/3. |
| 52 | command word "Explain" | "Structure first, then the property, joined with because." | AQA command words ("Explain: set out purposes or reasons") | OK | A lesson-specific gloss that is consistent with AQA's definition. |
| 53 | command word "Compare" | "Say what happens in each case and how they differ, in the same answer." | AQA ("Compare: describe the similarities and/or differences … not just write about one") | OK | Adequate. |
| 54 | command word "Predict" | "Say what will happen and give the reason from the structure." | AQA ("Predict: give a plausible outcome") | IMPRECISE | AQA's "predict" does not require a reason. A reason is required only when paired with explain/justify. This lesson's own r2 ("Predict whether each sample conducts") asks for no reason. See C3. |
| 55 | key fact | "Ionic compounds conduct only when molten or dissolved, because only then are the ions free to move and carry charge. It is the ions that move, never electrons." | 4.2.2.3 | OK | |
| 56 | examiner tip (`K.tip`, verbatim) | "say it is the ions that move — ionic compounds have no free electrons … They conduct only when molten or dissolved" | 4.2.2.3 | OK | Verbatim from source, and the science is right. |
| 57 | rung 1 (`K.find` 'State two ways…', fallback 'Explain why ionic compounds conduct electricity when molten') | CF/TF: CF7/TF7 "State two ways of making an ionic compound conduct electricity." CH/TH: no such item in CH or TH, so it falls back to CH2/TH2 "Explain why ionic compounds conduct electricity when molten or dissolved, but not when solid." | 4.2.2.3 | OK (items) | Traced through `ks4-lib.js` `find()`. The first needle misses both the route copy and the TH fallback on CH/TH, returns `item(undefined)=null`, and the `\|\|` second find hits TH2/CH2. |
| 58 | rung 1 overlay | `{ command: 'State', marks: 1, why: 'Melt it or dissolve it in water: both free the ions to move.' }` | AQA command words | IMPRECISE | On CH/TH the stem is an "Explain" item, but the chip says "State", and the `why` answers the CF7 question, not TH2. See C6. |
| 59 | CF7 options/WEs | "Melt it, or dissolve it in water" (correct); distractors cool/crush, keep solid | 4.2.2.3 | OK | |
| 60 | TH2 options/WEs | correct: "ions are free to move and carry charge; in the solid they are held in fixed positions"; WE "ions already exist in the solid" | 4.2.2.3 | OK | |
| 61 | r2 prompt | "Potassium bromide, KBr, is an ionic compound. Predict whether each sample conducts electricity." | 4.2.2.3 ("structures of specific ionic compounds other than sodium chloride is not required") | OK | Only a property prediction from "ionic" is asked. No structure knowledge of KBr is needed, so it is within the spec. |
| 62 | r2 parts | solid → does not conduct (1); above mp → conducts (0); dissolved → conducts (0) | 4.2.2.3 | OK | KBr is soluble (≈68 g/100 g water). |
| 63 | r2 marks | 3 (one per sample) | — | OK | |
| 64 | r2 `right` / `wrong` | "Solid no; molten and dissolved yes." / "Ask one question each time: are the ions free to move?" | 4.2.2.3 | OK | |
| 65 | r2 `model` | "Solid: does not conduct. The ions are fixed in the lattice." / "Molten: conducts. The ions are free to move and carry charge." / "Dissolved: conducts…" | 4.2.2.3 | OK | |
| 66 | r3 prompt | "Explain why sodium chloride has a high melting point." 3 marks | 4.2.2.3 | OK | |
| 67 | r3 links 1–3 | giant ionic lattice of oppositely charged ions → many strong electrostatic forces in all directions → large amount of energy to overcome, so high mp | 4.2.2.3 ("large amounts of energy needed to break the many strong bonds") | OK | The three links match the standard AQA 3-mark scheme (giant lattice / strong electrostatic attraction between oppositely charged ions / lots of energy to overcome). |
| 68 | r3 herring 1 + why | "strong covalent bonds … must be broken" → "Sodium chloride is ionic. There are no covalent bonds to break." | 4.2.2.3 | OK | AQA MS rejects covalent bonds / molecules. |
| 69 | r3 herring 2 + why | "forces between the sodium chloride molecules are strong" → "There are no molecules in an ionic lattice." | 4.2.2.3 | OK | AQA MS: "reference to intermolecular forces / molecules = max 2" (or 0). The herring is apt. |
| 70 | r4 question | "Sodium chloride has a high melting point. It does not conduct electricity when solid, but does when molten. Explain these properties in terms of its structure and bonding." 6 marks | 4.2.2.3 | OK | A standard AQA levels-of-response banker. |
| 71 | r4 point 1 | "Giant ionic lattice of Na⁺ and Cl⁻ ions." | 4.2.2.3 | OK | |
| 72 | r4 point 2 | "Strong electrostatic forces of attraction between oppositely charged ions, in all directions." | 4.2.2.3 | OK | |
| 73 | r4 point 3 | "Large amount of energy needed to overcome these many strong forces: high melting point." | 4.2.2.3 | OK | |
| 74 | r4 point 4 | "In the solid, ions are in fixed positions and cannot move." | 4.2.2.3 | OK | |
| 75 | r4 point 5 | "When molten, the ions are free to move." | 4.2.2.3 | OK | |
| 76 | r4 point 6 | "Moving ions carry charge, so the molten compound conducts." | 4.2.2.3 | OK | |
| 77 | r4 Level 3 · 5–6 | "A detailed, linked explanation of both properties from the giant ionic lattice, with the ions free to move only when molten." | AQA LoR convention | OK | |
| 78 | r4 Level 2 · 3–4 | "Both properties addressed, with some links to structure, but a step is missing from one chain." | AQA LoR convention | OK | |
| 79 | r4 Level 1 · 1–2 | "Relevant statements about ions or forces, but not linked to the properties." | AQA LoR convention | OK | |
| 80 | r4 Level 0 | "No relevant content · 0" | — | OK | |
| 81 | r4 reject 1 | "“Electrons flow through the molten salt.” It is the ions that move." | AQA MS ("do not accept electrons") | OK | |
| 82 | r4 reject 2 | "“Intermolecular forces are overcome.” There are no molecules." | AQA MS | OK | |
| 83 | r4 reject 3 | "“Covalent bonds break.”" | AQA MS | OK | |
| 84 | key note line 1 | "Ionic compounds are giant lattices of oppositely charged ions with strong electrostatic forces in all directions." | 4.2.2.3 | OK | |
| 85 | key note line 2 | "High melting and boiling points: a lot of energy is needed to overcome the many strong forces." | 4.2.2.3 | OK | |
| 86 | key note line 3 | "Solid: does not conduct. The ions are in fixed positions." | 4.2.2.3 | OK | |
| 87 | key note line 4 | "Molten or dissolved in water: conducts. The ions are free to move and carry charge." | 4.2.2.3 | OK | |
| 88 | key note line 5 | "It is the ions that move, never electrons." | 4.2.2.3 | OK | |
| 89 | key note line 6 | "In an answer, say "free to move". "Has charged particles" alone scores nothing." | AQA MS | OK | This is correct, and it is the line that makes rows 47–48 contradictory. |
| 90 | key note `spec` | "AQA 5.2.2.3" | 8464 5.2.2.3 | OK | House convention (see row 1). |
| 91 | key note vs source `key_note` | Design re-authored it and dropped "Brittle…" and "Higher ionic charge → stronger forces → higher MP" | 4.2.2.3 | OK | Both dropped statements are outside 4.2.2.3 (flag 9), so dropping them from the taught key note is correct. |
| 92 | `legal` | "Molten sodium chloride is above 801 °C and is heated in a crucible, not a glass beaker." | data (flag 17) | OK | NaCl mp = 801 °C (data-book value 800.7 °C). A crucible is correct practice. |
| 93 | `legal` | "In solution, water molecules surround each ion; they are left out of the drawing … Ion drift is drawn far faster than it really is." | model limits | OK | This correctly discloses the model's simplifications. |
| 94 | `tutor-line` | "Still thinking electrons carry the current in salt water?" | 4.2.2.3 | OK | |
| 95 | `endPrev` / `endNext` / connects | states-of-matter / properties-small-molecules; ionic-compounds, metals-alloys | spec order 4.2.2.1→4.2.2.4 | OK | |
| 96 | explainer / body: specific compounds | only NaCl in the taught body; KBr only as a property prediction | 4.2.2.3 final sentence | OK | Compliant with "structures of specific ionic compounds other than sodium chloride is not required". |
| 97 | source `theory[2]` (not served) | "Higher charge → … higher electrical conductivity when molten"; "MgO is a more stable compound" | — | OK (not served) | These claims are dubious or outside the spec, but the page does not render `theory`. There is nothing to change on the page. |

## 2. Required changes
| id | where (Design file + the exact `old` string, verbatim, unique in the file) | new string (verbatim) | why | spec section |
|---|---|---|---|---|
| properties-ionic-compounds-C1 | `ks4-chemistry-5.2.2.3-properties-ionic-compounds.dc.html`: `{ text: '0 marks', correct: false, reply: 'It does say something creditworthy about the solution.' }` | `{ text: '0 marks', correct: true, reply: 'Zero. Having charged particles is not a marking point without free to move, and the solid does have charged particles.' }` | The specimen meets none of the page's own three marking points (`exReveal`). "Charged particles" alone is uncreditworthy (the key note says so), and its statement about the solid is false. AQA would award 0. | 8462 4.2.2.3 / 8464 5.2.2.3; AQA MS convention |
| properties-ionic-compounds-C2 | same file: `{ text: '1 mark', correct: true, reply: 'One mark at most, for the solution containing charged particles, and some examiners would withhold even that.' }` | `{ text: '1 mark', correct: false, reply: 'Too generous. The solution having charged particles is not the marking point. The ions being free to move is, and it is never said.' }` | As written, it rewards the exact idea key-note line 6 and the chain done-note say "scores nothing". This is a self-contradiction on one page. | 8462 4.2.2.3; AQA MS |
| properties-ionic-compounds-C3 | same file: `Say what will happen and give the reason from the structure.` | `Give a plausible outcome. Add the reason from the structure when the question also says explain.` | AQA defines Predict as "give a plausible outcome". A reason is not required, and r2 in this lesson asks for none. | AQA command-word list (8462/8464 assessment) |
| properties-ionic-compounds-C4 | same file: `(on ? ' · bulb on' : ' · switch open')` | `(on ? ' · bulb on' : ' · before the test')` | `beaker()` draws a complete circuit with no switch, so "switch open" names a component that is not drawn. The alternative is to draw an AQA switch as L13 did (§10.11). The text fix keeps the layout still. | circuit-diagram convention (8464 6.2.1.1 symbols) |
| properties-ionic-compounds-C5 | same file: `Free ions between two electrodes, before the switch is closed.` | `Free ions between two electrodes, before the bulb is tested.` | The alt text names the same undrawn switch as C4. | as C4 |
| properties-ionic-compounds-C6 | same file: `{ command: 'State', marks: 1, why: 'Melt it or dissolve it in water: both free the ions to move.' }` | `{ command: R.isHigher ? 'Explain' : 'State', marks: 1, why: 'Melting or dissolving frees the ions to move, so they can carry charge; in the solid they are fixed.' }` | On CH/TH, `K.find` falls back to CH2/TH2, an "Explain" stem, because neither copy holds "State two ways…". The chip then contradicts the stem, and the `why` answers a different question. `R.isHigher` exactly selects the two routes lacking CF7/TF7. | AQA command words; 4.2.2.3 |

All six `old` strings were checked with `grep -cF` against the Design file: each occurs exactly once.

## 3. Route tags
| content | Design's tag | spec label | verdict | change id if any |
|---|---|---|---|---|
| Whole lesson (lattice, high mp/bp, conduction molten/dissolved) | base (no `sc-if`) | 4.2.2.3 / 5.2.2.3: no HT, not chemistry only | OK | — |
| Brittleness (bank only: TH4/CH4/CF4/TF4, CF8/TF8) | base | not in 4.2.2.3; standard GCSE application | OK | — |
| Charge vs melting point (bank only) | base, not taught in body | not a 4.2.2.3 statement; no HT label anywhere | OK (see flag 9) | — |
| Metal vs ionic conduction contrast (think, TH7) | base | 4.2.2.8 base + 4.2.2.3 base | OK | — |
| Content that should be tagged but is not | — | none found | OK | — |

## 4. Verbatim layer (the repo's four files)
| route | field | finding | change id if any |
|---|---|---|---|
| all | quiz (all copies) | `ks4-source.js` CF/CH/TF/TH are byte-identical (as parsed JSON) to the four repo dicts. | — |
| all | `higher` / `triple_only` / `rp` / `fifas` | null / null / null / []: correct for 4.2.2.3 | — |
| all | `examiner_tip` | identical across routes, served verbatim, and the science is right | — |
| all | `key_note` (repo) | contains "Higher ionic charge → stronger forces → higher MP" (outside 4.2.2.3), but the page renders its own key lines, not this field | — |
| CF, TF | quiz 1–5 | = TH1–TH5 (sodium chloride forms incl. vapour; conduction; mp/bp; brittleness; structure). All correct. TH1's vapour: the correct option omits vapour, and WE2 covers it. That is acceptable. | — |
| CF, TF | quiz 6, 8, 9 | solid at rt; brittle; ions fixed. All correct. | — |
| CF, TF | quiz 7 | "State two ways…": melt / dissolve. Correct. This is the rung-1 item on these routes. | — |
| CF, TF | quiz 10 | "melting point … as the charges on its ions increase → increases". Correct as science, but outside 4.2.2.3 (flag 9). Keep. | — |
| TF | quiz 11, 12 | giant ionic lattice; ions free to move. Correct. | — |
| CH, TH | quiz 6 | MgO > NaCl by 2+/2− charge. Correct; WE2 "both 1:1" correct. Flag 9: keep. | — |
| CH, TH | quiz 7 | metal (electrons) vs molten NaCl (ions). Correct (4.2.2.8 + 4.2.2.3). | — |
| CH, TH | quiz 8 | Na₂O vs NaCl: Na₂O higher (≈1132 °C vs 801 °C). Correct. Flag 9: keep. | — |
| CH, TH | quiz 9 | mp reflects force strength. Correct (4.2.2.1). | — |
| CH, TH | quiz 10 | MgO furnace lining (very high mp). Correct, and a real refractory use. Flag 9: keep. | — |
| TH | quiz 11 | Al₂O₃ higher mp than NaCl by 3+/2− charges. Correct (≈2072 °C). WE1 "Ion size has a smaller effect than charge" is acceptable at GCSE. Flag 9: keep. | — |
| TH | quiz 12 | current = flow of charge; mobile ions. Correct. | — |
| CH, TH | rung 1 | no "State two ways" item, so rung 1 serves CH2/TH2 (see row 57–58) | C6 (to the page overlay, not to the py) |

No change to any frozen py or to any generated route copy is required for this lesson.

## 5. Flags decided (from NOTES §9 that touch this lesson)
| flag | decision | spec section |
|---|---|---|
| 9 | **Keep all charge-vs-melting-point items, on the routes that carry them, unscored in the bank. Keep them out of the taught body, as Design did.** The item numbers in the flag are off. The charge items are TH6, TH8, TH10, TH11 (and CH6, CH8, CH10), plus CF10/TF10 on the Foundation copies. TH5 is "describe the structure" and TH7 is metal-vs-ionic conduction, and neither is a charge item. None of these items is science-wrong. None is ruled out by an HT or "chemistry only" label: 4.2.2.3 has neither, so the route tagging does not remove them. They apply 4.2.2.1 ("the stronger the forces … the higher the melting point") and are the kind of "given appropriate information" stretch AQA does set (the MgO vs NaCl comparison appears in AQA Higher papers). Their numbers are correct: NaCl 801 °C; MgO 2852 °C as quoted in the source, where the data book gives ≈2825–2852 °C, which is acceptable as rounded; Na₂O ≈1132 °C; Al₂O₃ ≈2072 °C. No DEPARTURE. | 8462 4.2.2.3, 4.2.2.1 |
| 16 | Hash re-ordering of options is fine for this lesson. No option text depends on position ("all of the above", "both A and B"), and the grading reads `correct`, not index. | — |
| 17 | NaCl mp 801 °C, used in `legal`, is correct (data book 800.7 °C). MgO 2852 °C appears only in the unserved source theory. | data book |
| 18 | New science verified. See §6. One defect: the Be-the-examiner mark, fixed in C1/C2. | 4.2.2.3 |
| "structures other than NaCl not required" | Compliant. The body teaches NaCl only. KBr (r2) asks for property prediction only, and the bank's MgO/Na₂O/Al₂O₃ items ask about charge, not structure. | 4.2.2.3 final sentence |

## 6. New science introduced by Design (flag 18) — verified?
- Hook ("why does no current flow", 4 unscored replies + reveal): verified correct (rows 5–10).
- Side-by-side beakers (solid vs molten; solid vs solution; drift directions, polarity, ion sizes, bulb state): verified correct. The one exception is the caption/alt naming an undrawn switch (C4, C5).
- Spot-the-flaw (electrons flow in molten salt): verified correct (rows 30–36).
- Linked-comparison chain (4 links + 2 herrings): verified, and the order is forced and creditworthy (rows 37–44).
- Be the examiner (specimen 3-mark answer): the specimen and model answer are correct, but the credited mark is **wrong, 1 → 0** (C1, C2).
- Command-word cards: Explain and Compare are OK. Predict is imprecise (C3).
- Key fact: verified.
- Rung 1 overlay: the command/why do not match the served item on CH/TH (C6).
- Rung 2 (KBr: solid / molten / dissolved): verified correct, and within the spec limit on named compounds.
- Rung 3 (NaCl high mp chain + herrings): verified, and it matches the AQA 3-mark scheme.
- Rung 4 (6-mark banker: mp + conduction; 6 indicative points, 3 levels, 3 rejects): every point is creditworthy, and the levels follow AQA LoR shape. Verified.
- Key-note lines 1–6: verified.
- `legal` model-limits line: verified (801 °C, crucible, hydration omitted, drift speed).
