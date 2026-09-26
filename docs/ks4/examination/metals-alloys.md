# Examination — Metals and alloys (metals-alloys) — AQA 8464 5.2.2.7–5.2.2.8 / 8462 4.2.2.7–4.2.2.8; Triple block 8462 4.10.3.2
Verdict: CHANGES REQUIRED
Examiner: Opus, 25 Sep 2026. Spec sources fetched: AQA-8462-SP-2016.PDF and AQA-8464-SP-2016.PDF (filestore.aqa.org.uk, Version 1.1, 04 Oct 2019), read as text. Data values from standard data-book figures (from memory, stated as such where used).

Design file: `docs/ks4/design-reference/pilot/KS4 Lessons/Pilot - Bonding and Electricity/ks4-chemistry-5.2.2.7-metals-alloys.dc.html`. Design's internal slug is `metals-and-alloys` (KS4SRC key, `KS4.find/bank/tip`, ladder `slug`); the site slug is `metals-alloys`. The port must map one to the other (not a science matter; noted in §4).

Spec statements relied on (quoted from the fetched PDFs):
- 8464 5.2.2.7 = 8462 4.2.2.7: "Metals have giant structures of atoms with strong metallic bonding. This means that most metals have high melting and boiling points. In pure metals, atoms are arranged in layers, which allows metals to be bent and shaped. Pure metals are too soft for many uses and so are mixed with other metals to make alloys which are harder. Students should be able to explain why alloys are harder than pure metals in terms of distortion of the layers of atoms in the structure of a pure metal."
- 8464 5.2.2.8 = 8462 4.2.2.8: "Metals are good conductors of electricity because the delocalised electrons in the metal carry electrical charge through the metal. Metals are good conductors of thermal energy because energy is transferred by the delocalised electrons."
- 8464 5.2.2.3: "When melted or dissolved in water, ionic compounds conduct electricity because the ions are free to move and so charge can flow."
- 8462 4.10.3.2 Alloys as useful materials (in 4.10.3 "Using materials (chemistry only)"): "Most metals in everyday use are alloys. Bronze is an alloy of copper and tin. Brass is an alloy of copper and zinc. Gold used as jewellery is usually an alloy with silver, copper and zinc. The proportion of gold in the alloy is measured in carats. 24 carat being 100% (pure gold), and 18 carat being 75% gold. Steels are alloys of iron that contain specific amounts of carbon and other metals. High carbon steel is strong but brittle. Low carbon steel is softer and more easily shaped. Steels containing chromium and nickel (stainless steels) are hard and resistant to corrosion. Aluminium alloys are low density." Students should "recall a use of each of the alloys specified" and "interpret and evaluate the composition and uses of alloys other than those specified given appropriate information."
- 8464 contains no statement naming steel, bronze, brass, stainless steel, carats or aluminium alloys (text search of the fetched 8464 PDF: "alloy" occurs only at 5.2.1.5 "Metallic bonding occurs in metallic elements and alloys", 5.2.2.7 and 5.7.2 list of products).
- ⚠️ 8462 4.10.4.2 is "Production and uses of NPK fertilisers", not alloys. Design's page and NOTES §8 cite alloys as 4.10.4.2; the correct reference is **4.10.3.2**.

## 1. Checked items
| # | Where (element / constant name / template line) | Claim as written | Spec section | Verdict (OK / WRONG / IMPRECISE / CONTRADICTS) | Note |
|---|---|---|---|---|---|
| 1 | `<title>` / h1 | "Metals and alloys" | 5.2.2.7 | OK | |
| 2 | header eyebrow | "AQA Chemistry 5.2.2.7–5.2.2.8 · Contrast" | 8464 5.2.2.7–5.2.2.8 (8462 4.2.2.7–4.2.2.8) | OK | 5.x numbering used consistently across the pilot; flag 10 fold-in is correct |
| 3 | `.ks3-bigq` | "Pure gold bends between your fingers, and pure iron is too soft for a bridge." | 5.2.2.7 "Pure metals are too soft for many uses" | OK | phenomenon framing of the spec sentence |
| 4 | `.ks3-bigq` | "Mix in a few atoms of something else and the metal turns hard. How can adding a little of another element change so much?" | 5.2.2.7 | OK | |
| 5 | header badges | "Combined · Triple", "Foundation · Higher", "Contains Triple" | 5.2.2.7 (no HT), 4.10.3.2 (chemistry only) | OK | no HT content anywhere in 5.2.2.7/5.2.2.8; Triple block present |
| 6 | hook h2 | "24-carat gold scratches. 18-carat gold lasts a lifetime." | 4.10.3.2 (context) | OK | given as phenomenon; see flag decision on carats in §5 |
| 7 | hook prose | "Pure, 24-carat gold is so soft that a ring made from it dents and scratches in weeks." | 4.10.3.2 "24 carat being 100% (pure gold)"; 5.2.2.7 | OK | |
| 8 | hook prose | "Most wedding rings are 18-carat" | — | IMPRECISE | factual overreach: 9-carat and 18-carat are both common in the UK (and platinum); "most" is unsupported → metals-alloys-C2 |
| 9 | hook prose | "three parts gold mixed with one part of other metals such as copper and silver" | 4.10.3.2 "18 carat being 75% gold"; "alloy with silver, copper and zinc" | OK | 75% = 3 : 1 by mass; composition stated as information |
| 10 | hook prose | "They keep their shape for decades." | 5.2.2.7 alloys harder | OK | |
| 11 | `hookOptions[0]` | "The different-sized atoms get in the way of the layers moving" / reply "Push some layers and find out." | 5.2.2.7 | OK | the credited idea; unscored reply |
| 12 | `hookOptions[1]` | "copper and gold react to make a hard compound" / "An alloy is a mixture. No new compound forms." | 5.2.2.7 "mixed with other metals" | OK | GCSE model: alloy = mixture |
| 13 | `hookOptions[2]` | "Copper atoms are harder than gold atoms" / "Pure copper is soft too. It is the mixture that is hard." | 5.2.2.1 "atoms themselves do not have the bulk properties of materials"; 5.2.2.7 | OK | |
| 14 | `hookOptions[3]` | "The extra metal fills gaps…" / "Close: the added atoms do change the packing. See what that does." | 5.2.2.7 | OK | reply is non-committal and leads to the mixer; not wrong |
| 15 | `hookReveal` | "The other metal atoms are a different size from gold atoms." | 5.2.2.7 | WRONG | the hook names silver as one of the other metals; silver's metallic radius (144 pm) is the same as gold's (144 pm) to within 1%, so the sentence is false for silver. Copper (128 pm) is different. → metals-alloys-C3 |
| 16 | `hookReveal` | "They distort the neat layers, and distorted layers cannot slide past each other easily." | 5.2.2.7 "distortion of the layers" | OK | |
| 17 | explainer | "In a pure metal, all the atoms are the same size, so they pack in regular layers." | 5.2.2.7 "In pure metals, atoms are arranged in layers" | OK | |
| 18 | explainer | "When a force is applied, whole layers can slide over each other and the metal bends: that is why pure metals such as gold, copper, iron and aluminium are soft." | 5.2.2.7 "allows metals to be bent and shaped. Pure metals are too soft" | OK | |
| 19 | explainer | "An alloy is a mixture of a metal with other elements, usually other metals." | 5.2.2.7 "mixed with other metals"; 4.10.3.2 steels contain carbon | OK | |
| 20 | explainer | "The added atoms are a different size." | 5.2.2.7 | OK | |
| 21 | `mix()` SVG | identical ions drawn as circles marked "+", in 4 regular rows | 5.2.1.5 / 5.2.2.7 | OK | delocalised electrons not drawn — disclosed in legal line |
| 22 | `mix()` SVG | added atoms drawn larger (r 36 vs 26), gold fill, neighbours displaced 7 px | 5.2.2.7 "distortion of the layers" | OK | added atoms carry no "+" although in a metal–metal alloy they are also positive ions; acceptable model simplification, disclosed in legal line ("Added atoms are drawn larger") |
| 23 | `mix()` SVG | pure: top two rows slide one full spacing; alloy: top rows move ≤8 px; labels "layers slide" / "layers jam" | 5.2.2.7 | OK | shear plane drawn dashed between rows 2 and 3 |
| 24 | `mix()` alt text | "Pure metal: identical ions in regular layers" / "Alloy: n larger atoms distort the layers" / "The top layers have slid one place along." / "have barely moved." | 5.2.2.7 | OK | |
| 25 | `LEVEL_TEXT` | "Pure metal", "Alloy · 1 added atom" … "4 added atoms" | 5.2.2.7 | OK | |
| 26 | `askOpts` | "The layers slide over each other and the metal changes shape" / "The layers hardly move: the metal resists the push" | 5.2.2.7 | OK | `predRight` = option 0 for pure, 1 for alloy — correct |
| 27 | `pushText` (pure) | "Every ion is the same size, so the layers are flat and slide one place along. The electron sea keeps holding them. Soft and malleable." | 5.2.2.7; 5.2.1.5 | OK | |
| 28 | `pushText` (alloy) | "The larger atoms push the neighbouring ions out of line. The layers are no longer flat, so they catch on each other and cannot slide. The alloy is harder." | 5.2.2.7 | IMPRECISE | absolute "cannot slide" contradicts the page's own key fact, hook reveal, chain and key note ("cannot slide … easily"); alloys are harder, not undeformable → metals-alloys-C4 |
| 29 | `pushText` (level 1) | "Even one added atom in this patch is enough to jam it." | 5.2.2.7 | OK | refers to the drawn patch |
| 30 | `pushWord` | "As you said." / "Not what you predicted." | — | OK | words, not ticks |
| 31 | misconception quote | "Ionic compounds only conduct when molten, so a metal must melt before it can conduct too." | 5.2.2.3, 5.2.2.8 | OK | it is the wrong idea being quoted; the reveal corrects "molten or dissolved" |
| 32 | `thinkOptions[0]` (correct) | "A metal's delocalised electrons are already free to move in the solid." | 5.2.2.8 | OK | |
| 33 | `thinkOptions[0]` (correct) | "Ionic compounds need melting because their charge carriers are ions, locked in place." | 5.2.2.3 "When melted or dissolved in water" | IMPRECISE | omits dissolving, and "locked in place" is true only in the solid; the credited option must match 5.2.2.3 → metals-alloys-C5 |
| 34 | `thinkOptions[1]` | "copper wires warm up, which melts them slightly" / "A warm wire is still solid. It conducts from the moment the switch closes." | 5.2.2.8 | OK | |
| 35 | `thinkOptions[2]` | "positive ions move" / "The ions stay in the lattice. The delocalised electrons move." | 5.2.2.8 | OK | |
| 36 | `thinkOptions[3]` | "need a coating" / "Bare copper conducts perfectly well." | 5.2.2.8 | OK | |
| 37 | `thinkReveal` | "In a metal, delocalised electrons carry the charge, and they move in the solid. In an ionic compound, ions carry it, and they move only when it is molten or dissolved." | 5.2.2.8; 5.2.2.3 | OK | |
| 38 | Ks4Choice words | right-word "That is the flaw." / wrong-word "That keeps the wrong idea." | — | OK | |
| 39 | chain title/prompt | "Why is an alloy harder than the pure metal?" "The classic 3-mark explanation. Four links in order; two are false." | 5.2.2.7 | OK | 4 links for 3 marks is fine (first two links together are the pure-metal half) |
| 40 | `cLinks[0]` | "In a pure metal, the atoms are all the same size and arranged in regular layers." | 5.2.2.7 | OK | |
| 41 | `cLinks[1]` | "The layers can slide over each other easily, so pure metals are soft." | 5.2.2.7 | OK | |
| 42 | `cLinks[2]` | "In an alloy, atoms of a different size distort the layers." | 5.2.2.7 | OK | |
| 43 | `cLinks[3]` | "The distorted layers cannot slide over each other easily, so the alloy is harder." | 5.2.2.7 | OK | |
| 44 | `cHerrings[0]` | "The alloy forms stronger ionic bonds between its metals." / why "An alloy is a mixture held by metallic bonding. No ions are transferred." | 5.2.1.5 "Metallic bonding occurs in metallic elements and alloys" | OK | |
| 45 | `cHerrings[1]` | "The added atoms remove the delocalised electrons…" / "Alloys still have delocalised electrons; they still conduct." | 5.2.1.5, 5.2.2.8 | OK | |
| 46 | chain done-note | "Examiners want both halves: the pure metal's layers slide, and the alloy's distorted layers cannot." | 5.2.2.7 | OK | "cannot" here is shorthand in a summary of the chain whose link says "easily"; acceptable |
| 47 | Triple block eyebrow | "Alloys as useful materials · AQA 4.10.4.2 (chemistry only)" | 8462 4.10.3.2 | WRONG | 4.10.4.2 is NPK fertilisers → metals-alloys-C1 |
| 48 | Triple block prompt | "Bronze is copper and tin. Brass is copper and zinc." | 4.10.3.2 | OK | verbatim to spec |
| 49 | Triple block prompt | "Steels are iron with carbon or other metals." | 4.10.3.2 "Steels are alloys of iron that contain specific amounts of carbon and other metals" | IMPRECISE | "or" implies a steel may contain no carbon; every steel contains carbon → metals-alloys-C6 |
| 50 | Triple block prompt | "Aluminium alloys are low density." | 4.10.3.2 | OK | verbatim |
| 51 | `pBins` | Steel / Aluminium alloy / Bronze or brass | 4.10.3.2 | OK | |
| 52 | `pItems[0]` | bridge girder → steel; "Steel is much harder and stronger than pure iron." | 4.10.3.2 | OK | |
| 53 | `pItems[1]` | kitchen knives that must not rust → steel; "Stainless steel: iron alloyed with chromium and nickel resists corrosion." | 4.10.3.2 "Steels containing chromium and nickel (stainless steels) are hard and resistant to corrosion" | OK | |
| 54 | `pItems[2]` | aircraft body → aluminium alloy; "low density but are stronger than pure aluminium" | 4.10.3.2 "Aluminium alloys are low density"; 4.2.2.7 alloys harder | OK | |
| 55 | `pItems[3]` | racing bicycle frame → aluminium alloy; "Low density and strong." | 4.10.3.2 | OK | best of the three bins given |
| 56 | `pItems[4]` | ship's propeller → bronze or brass; "Bronze is hard and resists corrosion in sea water." | 4.10.3.2 recall a use of each alloy | OK | standard textbook use (bronze propellers); true |
| 57 | `pItems[5]` | door handle and musical instruments → bronze or brass; "Brass is hard, easy to shape and does not corrode easily." | 4.10.3.2 | OK | |
| 58 | Triple block done-note | "Every choice rests on one property the alloy has and the pure metal lacks, or on density." | 4.10.3.2 | OK | |
| 59 | command word "Explain" | "Different-sized atoms, distorted layers, cannot slide: say all three." | 5.2.2.7 | OK | card shorthand; the credited answer is modelled in full elsewhere |
| 60 | command word "Compare" | "Pure metal and alloy side by side, in the same sentence." | AQA command words: Compare = describe similarities and/or differences | OK | |
| 61 | command word "Use the data" | "Describe the trend, then quote numbers from the table." | AQA "Use … the information/data" | OK | |
| 62 | key fact | "In an alloy, atoms of different sizes distort the layers, so they cannot slide over each other easily. That makes alloys harder than pure metals." | 5.2.2.7 | OK | |
| 63 | examiner tip (`K.tip`, verbatim) | "metals conduct as solids because their delocalised electrons are already free to move — don't say they must melt first like ionic compounds; and alloys are harder because different-sized atoms distort the layers so they can't slide." | 5.2.2.8, 5.2.2.7 | OK | verbatim frozen field |
| 64 | ladder r1 needle 1 | `K.find(slug, route, 'State what an alloy is')` | — | OK | present in CF7, TF7 only |
| 65 | ladder r1 needle 2 (fallback) | 'Describe the difference in structure between a pure metal and one of its alloys' | — | OK | CH4 / TH4 — so CH and TH get a different r1 question from CF and TF (`KS4.find` falls back to TH, which also lacks needle 1) |
| 66 | ladder r1 `why` | "A mixture of a metal with at least one other element, usually another metal." | 5.2.2.7 | CONTRADICTS | on CH and TH the rung-1 question is "Describe the difference in structure…", so the `why` answers a different question from the one asked → metals-alloys-C7 |
| 67 | r1 item (CF7/TF7) | correct "A mixture of a metal with one or more other elements" | 5.2.2.7 | OK | |
| 68 | r1 item (CH4/TH4) | correct "A pure metal has a regular lattice of same-sized atoms; an alloy has atoms of different sizes that distort the regular arrangement" | 5.2.2.7 | OK | |
| 69 | r2 prompt | "The table shows the hardness of iron mixed with different percentages of carbon." | 4.2.2.7 / WS 3.5 | IMPRECISE | the values 70/120/155/220 are not a real data set (flag 17); presented without a label they read as measured data → metals-alloys-C8 |
| 70 | r2 table | Carbon % 0.0/0.2/0.4/0.8; hardness 70/120/155/220 | — | OK as model data | real annealed Brinell hardness (ASM data-book values, from memory): iron ≈ 70 HB, 0.2 %C ≈ 111, 0.4 %C ≈ 149, 0.8 %C ≈ 174; normalised 0.8 %C ≈ 290. Design's set is monotonic and the same order of magnitude, so the trend taught is real; the 0.8 % value matches neither condition, hence relabel as model data rather than cite |
| 71 | r2 table alt | "Hardness rises from 70 with no carbon to 120 at 0.2 percent, 155 at 0.4 percent and 220 at 0.8 percent." | — | OK | matches the table |
| 72 | r2 part 1 | trend: "hardness increases as carbon increases" (answer 0) | WS 3.5 | OK | |
| 73 | r2 part 2 | "Best estimate of hardness at 0.6% carbon": about 190 (answer 1) | WS 3.5 / MS 4 interpolation | OK | recomputed: (155 + 220) ÷ 2 = 187.5 ≈ 190; distractors 100 and 260 lie outside the bracket |
| 74 | r2 `wrong` | "Read along the row. 0.6% lies between 0.4% (155) and 0.8% (220)." | — | OK | |
| 75 | r2 `model` | "As the percentage of carbon increases, the hardness increases." / "At 0.6% the hardness lies between 155 and 220: about 190." | — | OK | |
| 76 | r2 on Combined routes | steel data served on CF/CH | 5.2.2.7 + "given appropriate information" | OK | composition is supplied in the table; no steel recall required |
| 77 | r3 prompt | "Explain why brass (copper mixed with zinc) is harder than pure copper." 3 marks | 5.2.2.7 | OK | composition given in the stem, so fair on Combined |
| 78 | r3 links | pure copper same size, regular layers slide easily / zinc different size distorts / layers cannot slide so easily, harder | 5.2.2.7 | OK | Zn (134 pm) vs Cu (128 pm): genuinely different size |
| 79 | r3 herring 1 | "Copper and zinc react to form a hard compound." / "Brass is a mixture, not a compound." | 5.2.2.7 | OK | |
| 80 | r3 herring 2 | "The zinc atoms make the metallic bonds weaker." / "Hardness comes from the layers being unable to slide, not from weaker bonding." | 5.2.2.7 | OK | |
| 81 | r4 question | "Compare how solid copper and molten sodium chloride conduct electricity." 4 marks | 5.2.2.8, 5.2.2.3 | OK | NaCl is the spec's named ionic compound |
| 82 | r4 point 1 | "Copper has a lattice of positive ions and delocalised electrons." | 5.2.1.5 | OK | |
| 83 | r4 point 2 | "In copper, the delocalised electrons move and carry the charge, even in the solid." | 5.2.2.8 | OK | |
| 84 | r4 point 3 | "Molten sodium chloride contains Na⁺ and Cl⁻ ions that are free to move." | 5.2.2.3 | OK | |
| 85 | r4 point 4 | "In molten sodium chloride, the ions move and carry the charge; there are no free electrons." | 5.2.2.3 | OK | |
| 86 | r4 reject | "Electrons flow through the molten salt." / "Copper ions move through the wire." | 5.2.2.3, 5.2.2.8 | OK | both are standard non-creditable answers |
| 87 | `keyLines[0]` | "Metals have giant structures: positive ions in regular layers, surrounded by delocalised electrons." | 5.2.2.7 | IMPRECISE (omission) | the 5.2.2.7 statement "strong metallic bonding … most metals have high melting and boiling points" is nowhere on the page, and the verbatim key note ("High MP/BP") that carried it was replaced → metals-alloys-C9 |
| 88 | `keyLines[1]` | "Pure metals are soft: the layers slide over each other easily." | 5.2.2.7 | OK | |
| 89 | `keyLines[2]` | "An alloy is a mixture of a metal with other elements." | 5.2.2.7 | OK | |
| 90 | `keyLines[3]` | "In an alloy, different-sized atoms distort the layers so they cannot slide easily: alloys are harder." | 5.2.2.7 | OK | |
| 91 | `keyLines[4]` | "Metals conduct electricity and heat as solids: the delocalised electrons carry charge and energy." | 5.2.2.8 | OK | |
| 92 | `keyLines[5]` | "Ionic compounds need to be molten or dissolved to conduct; metals do not." | 5.2.2.3 | OK | |
| 93 | key note `spec` | "AQA 5.2.2.7–5.2.2.8" | 8464 | OK | |
| 94 | legal line | "The mixer is a two-dimensional model with one delocalised electron per ion left out for clarity." | 5.2.1.5 | IMPRECISE | the number of delocalised electrons per ion depends on the metal (Na 1, Mg 2, Al 3); the sentence also reads as though only one electron is omitted → metals-alloys-C10 |
| 95 | legal line | "Added atoms are drawn larger; in some alloys, such as steel, the added carbon atoms are smaller and sit in the gaps, which distorts the layers in the same way." | 5.2.2.7 | OK | correct: carbon is interstitial in iron |
| 96 | legal line | "Named alloys and their uses are separate-science content and show only on Triple routes." | 4.10.3.2 | CONTRADICTS | brass is named on every route (ladder r3, bank CF2/CH2), steel on every route (r2 table, this legal line), 18-carat gold in the hook → metals-alloys-C11 |
| 97 | Ks4End `tutor-line` | "Not sure why a few extra atoms matter so much?" | — | OK | |
| 98 | Ks4End `endNext` | "Nanoparticles (Triple)" on every route | 8462 4.2.4 chemistry only | route leak | see §3 — port item, no text change |
| 99 | Ks4End `endConnects` | Metallic bonding; Properties of ionic compounds | 5.2.1.5, 5.2.2.3 | OK | |
| 100 | RAIL | Gold rings / alloy mixer / think again / chain / ladder | — | OK | Triple block not a rail node, so Combined rails are complete |
| 101 | bank (all routes) | `K.bank(slug, route)` → the route's verbatim copy | — | OK | CF 10, CH 10, TF 12, TH 12 items; byte-identical to the repo's four py dicts (checked by script) |

## 2. Required changes
| id | where (Design file + the exact `old` string, verbatim, unique in the file) | new string (verbatim) | why | spec section |
|---|---|---|---|---|
| metals-alloys-C1 | `ks4-chemistry-5.2.2.7-metals-alloys.dc.html`: `Alloys as useful materials · AQA 4.10.4.2 (chemistry only)` | `Alloys as useful materials · AQA 4.10.3.2 (chemistry only)` | wrong spec reference; 4.10.4.2 is NPK fertilisers | 8462 4.10.3.2 |
| metals-alloys-C2 | same file: `Most wedding rings are 18-carat` | `Many wedding rings are 18-carat` | "most" is an unsupported factual claim (9-carat is at least as common in the UK) | 8462 4.10.3.2 (context) |
| metals-alloys-C3 | same file: `The other metal atoms are a different size from gold atoms.` | `Copper atoms are a different size from gold atoms.` | silver, which the hook names, is the same size as gold (both 144 pm); the statement is false for it. Copper is genuinely different (128 pm) | 5.2.2.7 |
| metals-alloys-C4 | same file: `so they catch on each other and cannot slide. The alloy is harder.` | `so they catch on each other and cannot slide easily. The alloy is harder.` | agrees with the key fact, chain and key note; alloys are harder, not undeformable | 5.2.2.7 |
| metals-alloys-C5 | same file: `Ionic compounds need melting because their charge carriers are ions, locked in place.` | `Ionic compounds need melting or dissolving because their charge carriers are ions, locked in place in the solid.` | the credited option must include dissolving; "locked in place" is true only in the solid | 5.2.2.3 |
| metals-alloys-C6 | same file: `Steels are iron with carbon or other metals.` | `Steels are iron with carbon, and sometimes other metals.` | every steel contains carbon | 8462 4.10.3.2 |
| metals-alloys-C7 | same file: `why: 'A mixture of a metal with at least one other element, usually another metal.'` | `why: 'An alloy is a mixture of a metal with at least one other element; its different-sized atoms distort the regular layers of the pure metal.'` | on CH/TH, rung 1 serves "Describe the difference in structure…" (CH4/TH4), not "State what an alloy is"; the `why` must fit both questions | 5.2.2.7 |
| metals-alloys-C8 | same file: `prompt: 'The table shows the hardness of iron mixed with different percentages of carbon.'` | `prompt: 'The table shows model data for the hardness of iron mixed with different percentages of carbon.'` | flag 17: the numbers are illustrative, not a cited data set | WS 3.5; flag 17 |
| metals-alloys-C9 | same file: `'Metals have giant structures: positive ions in regular layers, surrounded by delocalised electrons.'` | `'Metals have giant structures with strong metallic bonding, so most have high melting and boiling points.'` | the 5.2.2.7 melting/boiling-point statement is otherwise absent from the page; the layers and electrons are carried by lines 2, 4 and 5 | 5.2.2.7 |
| metals-alloys-C10 | same file: `with one delocalised electron per ion left out for clarity` | `with the delocalised electrons left out for clarity` | electrons per ion varies by metal | 5.2.1.5 |
| metals-alloys-C11 | same file: `Named alloys and their uses are separate-science content and show only on Triple routes.` | `Recalling named alloys and their uses is separate-science content, taught only on Triple routes; elsewhere an alloy's make-up is given in the question.` | removes the self-contradiction (brass, steel and 18-carat gold appear on all routes as given information) | 8462 4.10.3.2 vs 8464 5.2.2.7 |

All eleven `old` strings verified with `grep -cF` = 1 in the Design file.

## 3. Route tags
| content | Design's tag | spec label | verdict | change id if any |
|---|---|---|---|---|
| Pure metals, layers, alloys harder (mixer, chain, key fact) | base | 8464 5.2.2.7, no HT | OK | |
| Metals conduct electricity and heat (think, r4, key line 5) | base | 8464 5.2.2.8, no HT | OK | |
| High mp/bp of metals | (absent) | 8464 5.2.2.7 base | add as base key line | metals-alloys-C9 |
| Engineer's pick (bronze, brass, steels, stainless, aluminium alloys) | `triple` (`sc-if isTriple`, blue border, Triple badge) | 8462 4.10.3.2, chemistry only | OK (reference number wrong) | metals-alloys-C1, C6 |
| Hook: 24- and 18-carat gold | base | 8462 4.10.3.2 content used as context | OK — supplied as information in the hook, never asserted as knowledge to recall, never assessed on a Combined route; 8464 5.2.2.7 is itself about why pure metals are alloyed | C2, C3 |
| r2 steel hardness data | base | 5.2.2.7 + data given | OK | C8 |
| r3 brass chain | base | 5.2.2.7 (composition given in stem) | OK | |
| Header "Contains Triple" | — | — | OK | |
| Ks4End next link "Nanoparticles (Triple)" | untagged, all routes | 8462 4.2.4 chemistry only | route leak: on CF/CH there is no nanoparticles page. Port must point CF/CH `endNext` at the next Combined lesson (not a text substitution; resolve in the generator's prev/next wiring) | — |
| Anything Higher | none | none in 5.2.2.7–5.2.2.8 | OK | |

## 4. Verbatim layer (the repo's four files)
| route | field | finding | change id if any |
|---|---|---|---|
| all | quiz | `ks4-source.js` `metals-and-alloys` quiz copies CF/CH/TF/TH are identical to the `metals-alloys` dicts in `all_subtopics_chemistry.py`, `_higher.py`, `_triple_foundation.py`, `_triple_higher.py` (script comparison). `higher: None`, `triple_only: None`, `rp: None` on all four. | — |
| all | slug | Design keys the source and ladder as `metals-and-alloys`; site slug is `metals-alloys`. Port must map (else `K.find/bank/tip` return empty and the best-score key differs). | — |
| CF | quiz item 9 "Identify the correct description of steel." (correct: "Iron mixed with a small amount of carbon") | pure recall of steel's composition — 8462 4.10.3.2 chemistry only; 8464 names no steel. **Remove from the generated CF route copy** (TF9 keeps it). This is a change to the generated route copy, not to the frozen py. | — (route-copy ruling) |
| CH | quiz item 7 "Stainless steel is used to make cutlery. Suggest two properties…" (correct includes "it resists corrosion") | the credited answer depends on recalling that stainless steel resists corrosion — 8462 4.10.3.2 ("Steels containing chromium and nickel (stainless steels) are hard and resistant to corrosion"), chemistry only; not supplied in the stem. **Remove from the generated CH route copy** (TH7 keeps it). | — (route-copy ruling) |
| CF, CH | item 2 "Explain why brass (copper mixed with zinc) is harder than pure copper." | composition given in the stem; tests 5.2.2.7. Keep. | — |
| CH | item 9 aluminium alloy for aircraft | context given; credited option answerable from 5.2.2.7 (alloys harder) plus the everyday lightness of aluminium, and every distractor is eliminable on core knowledge. Keep. | — |
| CH, TH | item 10 "metals are malleable but ionic compounds are brittle" | ionic brittleness is not a 5.2.2.3 statement (same class as flag 9); science correct. Keep verbatim in the bank; not taught in the body. | — |
| TF | items 9, 12 (steel; bronze = copper + tin) | 4.10.3.2 content on a Triple route — correct placement. | — |
| TH | items 7, 9, 11 (stainless steel, aluminium alloy, steel for bridges) | Triple route — correct. TH11 "carbon atoms in steel are a different size to the iron atoms" is accurate (interstitial carbon). | — |
| all | examiner_tip | verbatim; correct (5.2.2.7, 5.2.2.8). | — |
| CF, CH | key_note | ends "Steel, bronze, brass are key examples." — chemistry-only content. Design's page does not render the verbatim key note (it uses its own `keyLines`), so nothing leaks today; if any generator path ever serves the frozen `key_note` on a Combined route, that sentence must be sliced off. | — |
| all | quiz wrong_explanations | read all 44 CF/TF/TH distinct items' explanations: no science errors found (CF3 "positive ions are fixed and only vibrate; the mobile delocalised electrons carry most of the heat" is correct for metals). | — |

## 5. Flags decided (from NOTES §9 that touch this lesson)
| flag | decision | spec section |
|---|---|---|
| 10 (5.2.2.8 folded into metals and alloys) | Correct. Electrical conduction is taught (think-again, r4) and thermal conduction is carried by key line 5 and bank items CF3/TH3/TH12; together they meet both 5.2.2.8 statements. | 8464 5.2.2.8 |
| 16 (option order) | Re-ordering by stable hash changes no text and cannot change what AQA credits. Keep the sort on — an always-first correct option is a leak. | — |
| 17 (tungsten >3400 °C, iron bp ~2860 °C) | Neither value appears on this page (they are on metallic-bonding, L5). Checked anyway: W mp 3422 °C, so ">3400" is correct; Fe bp 2862 °C, so "~2860" is correct (data-book values, from memory). | — |
| 17 (hardness vs carbon 70/120/155/220) | No real cited set matches it (annealed Brinell ≈ 70/111/149/174; normalised 0.8 %C ≈ 290 — from memory of ASM/MatWeb values). The trend is real, so relabel as **model data** rather than replace. The 0.6 % interpolation answer (≈190) is recomputed and correct for the numbers shown. | WS 3.5 → metals-alloys-C8 |
| 17 (steel carbon %) | The page states no carbon percentage; the source theory's "iron + 0.1–2% carbon" is not rendered. Nothing to change. | 4.10.3.2 |
| 18 (new science: chain banker №3, engineer's pick, ladder r2–r4) | Verified in §6; changes C6, C7, C8 apply. | 5.2.2.7, 5.2.2.8, 4.10.3.2 |
| 19 (alloy key-note moved from metallic bonding) | Correct placement: alloys are 5.2.2.7. Design's L11 key lines 3–4 carry it; the named-alloy sentence of the frozen key note is correctly not shown on Combined routes. | 8464 5.2.2.7 |
| — (carats in the hook, all routes) | Keep on all routes. Carat values are 8462 4.10.3.2 content, but here they are given information framing a 5.2.2.7 phenomenon; no Combined item assesses them. The legal line is corrected (C11) so the page no longer claims named alloys never appear on Combined routes. | 8462 4.10.3.2; 8464 5.2.2.7 |
| — (spec reference for named alloys) | Design's "4.10.4.2" (page eyebrow and NOTES §8) is wrong; it is **8462 4.10.3.2**. Page fixed by C1; NOTES §8 row should read 4.10.3.2 too. | 8462 4.10.3.2 |

## 6. New science introduced by Design (flag 18) — verified?
- Hook (carat rings, four replies, reveal): verified; C2 (most → many), C3 (silver is not a different size from gold).
- Alloy mixer (model, predictions, push outcomes, alt text): verified; C4 (cannot slide → cannot slide easily).
- Think-again spot-the-flaw (four options and reveal): verified; C5 (melting or dissolving).
- Chain banker №3 "Why is an alloy harder than the pure metal?" (4 links, 2 herrings): verified, OK as written.
- Triple engineer's pick (6 items, 3 bins, whys): verified; C1 (spec ref), C6 (steels always contain carbon).
- Ladder r1 `why`: C7 (must fit the CH/TH fallback question).
- Ladder r2 steel hardness data rung: arithmetic verified (≈190 at 0.6 %); data relabelled model data, C8.
- Ladder r3 brass chain: verified, OK.
- Ladder r4 "Compare solid copper and molten sodium chloride" (4 points, 2 rejects): verified, OK — a creditable 4-mark scheme.
- Key lines (6): verified; C9 restores the high mp/bp statement.
- Command-word cards, key fact: verified, OK.
- Legal line: C10, C11.
