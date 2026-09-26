# Examination — Ionic bonding (ionic-bonding) — AQA 8464 5.2.1.2 / 8462 4.2.1.2
Verdict: CHANGES REQUIRED
Examiner: Opus, 25 Sep 2026. Spec sources fetched: AQA-8462-SP-2016.PDF (v1.1, 04 Oct 2019) and AQA-8464-SP-2016.PDF (v1.1, 04 Oct 2019), filestore.aqa.org.uk, text extracted and quoted below; aqa.org.uk 8462 subject-content page (summary only). Group 0 statement cited from the same 8462 PDF (§4.1.2.1). AQA command-word glossary from memory.

Spec statements relied on (8462 4.2.1.2 ≡ 8464 5.2.1.2, identical text, no HT marker, not chemistry-only):
- "When a metal atom reacts with a non-metal atom electrons in the outer shell of the metal atom are transferred. Metal atoms lose electrons to become positively charged ions. Non-metal atoms gain electrons to become negatively charged ions. The ions produced by metals in Groups 1 and 2 and by non-metals in Groups 6 and 7 have the electronic structure of a noble gas (Group 0)."
- "Students should be able to draw dot and cross diagrams for ionic compounds formed by metals in Groups 1 and 2 with non-metals in Groups 6 and 7."
- "Students should be able to work out the charge on the ions of metals and non-metals from the group number of the element, limited to the metals in Groups 1 and 2, and non-metals in Groups 6 and 7."
- 4.2.1.3 / 5.2.1.3: "Ionic compounds are held together by strong electrostatic forces of attraction between oppositely charged ions. These forces act in all directions in the lattice and this is called ionic bonding." "describe the limitations of using dot and cross … diagrams to represent a giant ionic structure".
- 4.2.1.1 / 5.2.1.1: "Ionic bonding occurs in compounds formed from metals combined with non-metals." "Covalent bonding occurs in most non-metallic elements and in compounds of non-metals."

## 1. Checked items
| # | Where (element / constant name / template line) | Claim as written | Spec section | Verdict (OK / WRONG / IMPRECISE / CONTRADICTS) | Note |
|---|---|---|---|---|---|
| 1 | header eyebrow (l.36) | "AQA Chemistry 5.2.1.2 · Process" | 8464 5.2.1.2 / 8462 4.2.1.2 | OK | Correct for Combined. Triple routes would cite 4.2.1.2 (8462); see §3 note — cross-lesson, not a change here. |
| 2 | `ks3-bigq` (l.38) | soft metal + poisonous gas → the salt on your chips | 4.2.1.2 | OK | Na is soft, Cl₂ toxic, NaCl table salt. |
| 3 | badges (l.40–41) | Combined · Triple / Foundation · Higher | 4.2.1.2 no HT, not chemistry-only | OK | Whole lesson is base content on all four routes. |
| 4 | hook h2 + prose (l.53–54) | hot Na burns in Cl₂ with a bright yellow flame; white crystals of NaCl | 4.2.1.2 (context) | OK | Standard demonstration; yellow flame and white solid are correct observations. |
| 5 | hook prose (l.54) | Na has one outer electron; Cl has seven | 4.1.1.7 electronic structure; 4.2.1.2 | OK | 2.8.1 and 2.8.7. |
| 6 | `hookOptions[0]` | "It moves across to the chlorine atom" / reply "Hold that thought and test it below." | 4.2.1.2 | OK | Unscored; the correct idea is not confirmed until the reveal (by design). |
| 7 | `hookOptions[1]` reply | "Sharing is real, but it is not what happens here." | 4.2.1.1 | OK | Sharing = covalent, non-metal + non-metal. |
| 8 | `hookOptions[2]` reply | "Something has to change, or sodium would still fizz in water." | 4.2.1.2 | OK | Rhetorical; implies a chemical change occurred, which is right. |
| 9 | `hookOptions[3]` reply | "The light is energy released, not the electron." | 4.2.1.2 / 4.5.1.1 | OK | Energy is released as light; electron is not emitted. |
| 10 | `hookReveal` | electron moves Na→Cl; Na full shell + one more proton than electrons; Cl full shell + one extra electron; crystals are charged particles not atoms | 4.2.1.2 | OK | Correct and precise (charge explained by proton/electron count). |
| 11 | explainer 1 (l.63) | "A full outer shell is stable: that is why the noble gases barely react." | 8462 4.1.2.1 ("unreactive … because their atoms have stable arrangements of electrons") | OK | |
| 12 | explainer 1 | "Sodium (2.8.1) is one electron past a full shell; chlorine (2.8.7) is one short." | 4.1.1.7 | OK | |
| 13 | explainer 1 | metal atom loses its outer electrons, non-metal gains them | 4.2.1.2 | OK | Matches spec wording. |
| 14 | explainer 1 | "Both end up with the electron arrangement of a noble gas." (said of any metal + non-metal) | 4.2.1.2 limits this to Groups 1, 2, 6, 7 | IMPRECISE | Stated generally; false for e.g. Fe²⁺/Fe³⁺, Cu²⁺ (8462 4.1.3.2 transition-metal ions). The spec scopes it deliberately. → ionic-bonding-C1. |
| 15 | explainer 1 | "each is an ion, a particle with a charge" | 4.2.1.2 | OK | Acceptable GCSE definition. |
| 16 | `WORKED` | Na+Cl n=1, Mg+O n=2 | 4.2.1.2 (Groups 1/2 with 6/7) | OK | Both inside the spec's drawing limit; both 1:1 so `ionicTransfer()` draws them correctly. |
| 17 | `ionicTransfer('Na','Cl', 0/1)` | Na 2.8.1 (crosses), Cl 2.8.7 (dots); arrow from Na outer shell to Cl | 4.2.1.2 dot-and-cross | OK | CONFIG values correct. |
| 18 | `ionicTransfer('Na','Cl', 2)` | [Na]⁺ 2.8, [Cl]⁻ 2.8.8 with one cross in Cl outer shell, brackets + charges | 4.2.1.2 | OK | Matches the spec's NaCl diagram convention (brackets, charge top right). |
| 19 | `ionicTransfer('Mg','O', 2)` | [Mg]²⁺ 2.8, [O]²⁻ 2.8 with two crosses | 4.2.1.2 | OK | `sup(2)`→"2+", `sup(-2)`→"2−". 1:1 compound, so the one-ion-each drawing is correct. |
| 20 | `wCaption[0..2]` | before: neutral atoms, crosses Na, dots Cl; transfer arrow; after: two ions, full outer shell, square brackets + charge | 4.2.1.2 | OK | |
| 21 | gate 1 `q` / options | "Which atom will lose electrons?" [metal, non-metal, "Neither: they share a pair"], a=0 | 4.2.1.2 | OK | |
| 22 | gate 1 `yes` | "Sodium is the metal. Its single outer electron moves to chlorine." / Mg: "Its 2 outer electrons move to oxygen." | 4.2.1.2 | OK | |
| 23 | gate 1 `no[1]` | "It is the other way round. Chlorine is the non-metal and gains electrons; sodium loses them." | 4.2.1.2 | OK | |
| 24 | gate 1 `no[2]` | "Sharing happens between two non-metals. Sodium is a metal, so electrons transfer." | 4.2.1.1 | OK | |
| 25 | gate 2 `q` / options | charge on metal ion: [n+, n−, "None: its shell is full"], a=0 | 4.2.1.2 | OK | |
| 26 | gate 2 `yes` | lost n electrons, kept all protons → n+; non-metal gained them → n− | 4.2.1.2 | OK | For n=1 "gained them" is a grammar slip (style, not remit). |
| 27 | gate 2 `no[1]` | "Losing negative electrons leaves the protons in charge, so the metal ion is positive." | 4.2.1.2 | OK | Wordplay, but the reasoning (protons outnumber electrons) is right and is stated exactly in `yes`, which is always appended. |
| 28 | gate 2 `no[2]` | "A full shell does not mean no charge. It has n more proton(s) than electrons now." | 4.2.1.2 | OK | Targets a real misconception correctly. |
| 29 | gate 3 `q` / options | what holds the ions: [transfer, "strong electrostatic attraction between the oppositely charged ions", shared pair], a=1 | 4.2.1.3 | OK | Spec wording. |
| 30 | gate 3 `yes` | "That attraction is the ionic bond. It acts in every direction, so each ion pulls on all its neighbours in the lattice." | 4.2.1.3 ("act in all directions in the lattice") | OK | |
| 31 | gate 3 `no[0]` | "The transfer has already finished. It made the ions; it is not what holds them." | 4.2.1.3 | OK | |
| 32 | gate 3 `no[2]` | "Nothing is shared here. Every electron now belongs to one ion or the other." | 4.2.1.2 | OK | |
| 33 | misconception panel (l.99–100) | quote "The ionic bond is the transfer of the electron." + correction: transfer makes ions; the pull between + and − ions is the bond | 4.2.1.3 | OK | Genuine, well-documented misconception; three-beat format met. |
| 34 | `wConfront` logic | opens after Na+Cl always, after Mg+O only if transfer chosen | — | OK | Behaviour consistent with NOTES §7 L2. |
| 35 | explainer 2 (l.106) | Group 1 loses one → 1+; Group 2 → 2+; Group 7 gains one → 1−; Group 6 → 2− | 4.2.1.2 (charge from group, Groups 1, 2, 6, 7) | OK | Exactly the spec's scope. |
| 36 | explainer 2 | ions held by strong electrostatic forces acting in every direction, "which is why ionic compounds are giant lattices, not pairs" | 4.2.1.3 | OK | |
| 37 | draw intro (l.112) | "Metal electrons are crosses, non-metal electrons are dots." | 4.2.1.2 | OK | This is the bench's key, not a rule; AQA credits either assignment provided the two sources are distinguished. The `legal` line frames it as the page's convention. |
| 38 | draw intro | marks for: right electrons moved, full outer shell on each ion, charge on each bracket | AQA mark-scheme practice for dot-and-cross (from memory) | OK | Matches how AQA mark schemes award (electron arrangement + charges). |
| 39 | `DRAW` | Li/F n1, K/Cl n1, Ca/O n2, Mg/S n2 | 4.2.1.2 (Groups 1/2 with 6/7) | OK | All inside the drawing limit; all 1:1, so single-ion figures are correct. |
| 40 | `CONFIG` Li, F, K, Cl, Ca, O, Mg, S | 2.1, 2.7, 2.8.8.1, 2.8.7, 2.8.8.2, 2.6, 2.8.2, 2.8.6 | 4.1.1.7 | OK | |
| 41 | `drawFig` | moved electrons leave metal outer shell first, then inner; non-metal outer shell gains them, drawn as crosses | 4.2.1.2 | OK | Over-moving correctly shows inner-shell loss and >8 on the non-metal, which the verdict names. |
| 42 | `dLines` electrons right | "Lithium has lost its outer shell and fluorine now has eight." | 4.2.1.2 | OK | "lost its outer shell" = lost its only outer-shell electron; acceptable GCSE phrasing. |
| 43 | `dLines` electrons too few | "Fluorine's outer shell is not full yet." | 4.2.1.2 | OK | |
| 44 | `dLines` electrons too many | non-metal >8 in outer shell and metal "started losing inner electrons" | 4.2.1.2 | OK | True for every DRAW pair with moved ≤3. |
| 45 | `dLines` metal charge right/wrong | "Losing n electron(s) leaves n+." / "Each one leaves one unbalanced proton, so the charge is positive." | 4.2.1.2 | OK | |
| 46 | `dLines` non-metal charge right/wrong | "Gaining n makes it n−, and the two charges cancel." / "Each extra electron adds one negative charge." | 4.2.1.2 | OK | |
| 47 | `dMetalLabel` / `dNonLabel` + `ION` | "Charge on the lithium ion" / "…fluoride / chloride / oxide / sulfide ion" | 4.1.1.1 naming | OK | Anion names correct. |
| 48 | `chargeOpts` | 3+, 2+, 1+, 1−, 2−, 3− | — | OK | Distractors plausible. |
| 49 | `FORGE[0]` aluminium oxide | Al³⁺ ×2 (6+), O²⁻ ×3 (6−) → Al₂O₃ | 8462 4.1.1.1 formulae; 4.4.3.3 (aluminium oxide) | OK | Charges given on the buttons; see §5 decision on Al³⁺/N³⁻. |
| 50 | `FORGE[1]` lithium sulfide | Li⁺ ×2, S²⁻ ×1 → Li₂S | 4.2.1.2 | OK | |
| 51 | `FORGE[2]` calcium nitride | Ca²⁺ ×3 (6+), N³⁻ ×2 (6−) → Ca₃N₂ | 4.1.1.1 formulae | OK | N³⁻ is outside the charge-from-group limit but the charge is given on the button. |
| 52 | `fLead` (worked) | "aluminium forms Al³⁺, oxide is O²⁻. The lowest total both charges reach is 6, so two Al³⁺ (6+) balance three O²⁻ (6−)." | 4.1.1.1 | OK | LCM reasoning correct. |
| 53 | `fLead` (pupil) | "Use as few as you can: the formula is the simplest ratio." | 4.2.1.3 (empirical formula of an ionic compound) | OK | |
| 54 | `fDone` (minimal) | e.g. "Formula: Li₂S. 2 × 1+ = 2+, and 1 × 2− = 2−. The subscripts come from balancing the charges, not from the group numbers." | 4.1.1.1 | OK | Arithmetic recomputed for all three: 6/6, 2/2, 6/6. |
| 55 | `fDone` (non-minimal) + `fLocked` | "It balances, but it is not the simplest ratio. Empty the box and use fewer ions." while `fLocked = fWorked \|\| fZero` disables "Empty the box" | — | CONTRADICTS | At any balanced non-simplest box (e.g. 4 Li⁺ + 2 S²⁻) the page tells the pupil to empty the box and has disabled that button. → ionic-bonding-C2. |
| 56 | `fHasNext` | "Next compound" offered whenever balanced, including non-simplest | 4.2.1.3 (simplest ratio) | CONTRADICTS | Lets the pupil bank a non-simplest formula as "balanced" straight after being told it is not the formula. → ionic-bonding-C3. |
| 57 | `fProgress` | "n of 3 balanced" — counts only compounds left via Next; the third (no Next button) is never counted | — | CONTRADICTS | After Ca₃N₂ is balanced correctly the page reads "2 of 3 balanced". → ionic-bonding-C4. |
| 58 | `fAddM` / `fAddX` / `fTally` / `fNet` | "Add Al³⁺", "Add N³⁻", "Net charge −3" etc. | — | OK | Superscripts via `SUP` correct for 1–3. |
| 59 | command word Describe | "Say what happens, in order. No reason needed." | AQA command words (from memory): "give an account … not required to account for why" | OK | |
| 60 | command word Explain | "Say why. Link each step to the next with 'so' or 'because'." | AQA command words (from memory) | OK | |
| 61 | command word Deduce | "Work it out from what you are given. Here: from the group numbers." | 4.2.1.3 uses "deduce" | OK | |
| 62 | command word Draw | "Marks are for content, not art: electrons, brackets, charges." | AQA command words (from memory) | OK | |
| 63 | key fact (l.201) | transfer makes the ions; the bond is the strong electrostatic attraction between oppositely charged ions; charges balance to zero | 4.2.1.2, 4.2.1.3 | OK | |
| 64 | examiner tip (`K.tip`) — verbatim | don't stop at "electrons transfer"; bond = strong electrostatic attraction; check charges balance to zero | 4.2.1.3 | OK | Identical in all four py files and ks4-source.js. |
| 65 | ladder r1 needle | `K.find(slug, route, 'no overall electrical charge')` | — | OK | Needle present in CF7, CH2, TF7, TH2: every route gets its own copy; no TH fallback. |
| 66 | ladder r1 item | "Explain why an ionic compound such as sodium chloride has no overall electrical charge." key: total + balances total − | 4.2.1.2 | OK | Distractor explanations correct (charge conserved, ions keep charges). |
| 67 | ladder r1 `why` | "The charges on the ions add up to zero. Nothing is destroyed; the electrons just moved." | 4.2.1.2 | OK | |
| 68 | ladder r2 prompt | Ba Group 2, F Group 7, deduce barium fluoride | 4.2.1.2 (Groups 1, 2, 6, 7) | OK | Inside the charge-from-group limit. |
| 69 | ladder r2 `accept` | ['BaF2','BaF₂'] (norm maps subscripts, strips spaces, case-sensitive) | — | OK | Case sensitivity is correct for formulae. 2 marks for charge + formula matches AQA practice. |
| 70 | ladder r2 `right`/`wrong`/`model` | Ba²⁺ (loses 2), F⁻ (gains 1), two F⁻ balance one Ba²⁺ → BaF₂ | 4.2.1.2 | OK | |
| 71 | ladder r3 link 1 | "Magnesium (2.8.2) loses its two outer electrons and oxygen (2.6) gains them." | 4.2.1.2 | OK | |
| 72 | ladder r3 link 2 | "This forms Mg²⁺ and O²⁻ ions, each with a full outer shell." | 4.2.1.2 | OK | |
| 73 | ladder r3 link 3 | "The oppositely charged ions are held together by strong electrostatic attraction: the ionic bond." | 4.2.1.3 | OK | |
| 74 | ladder r3 herring 1 + why | "share two pairs" / "Sharing is covalent. Magnesium is a metal, so its electrons transfer." | 4.2.1.1 | OK | |
| 75 | ladder r3 herring 2 + why | "Oxygen loses two electrons to magnesium." / "The non-metal gains electrons. Oxygen ends up 2−." | 4.2.1.2 | OK | |
| 76 | ladder r4 question | Li + F → LiF; give electron arrangements and charges (Li 2.1, F 2.7) | 4.2.1.2 | OK | 4 marks, Describe. |
| 77 | ladder r4 point 1–2 | Li loses its one outer electron; F gains that electron | 4.2.1.2 | OK | |
| 78 | ladder r4 point 3 | "This forms Li⁺ (2) and F⁻ (2.8) ions, each with a full outer shell." | 4.2.1.2 | OK | Li⁺ = 2 (full first shell, He arrangement), F⁻ = 2.8. |
| 79 | ladder r4 point 4 | oppositely charged ions attract: strong electrostatic forces, the ionic bond | 4.2.1.3 | OK | Note: strictly "describe" does not require the bond, but the question asks what happens to form LiF; AQA 4-mark schemes include the attraction. |
| 80 | ladder r4 `reject` | "share an electron" = covalent; "the bond is the transfer" | 4.2.1.1, 4.2.1.3 | OK | Both genuine AQA "do not accept" patterns. |
| 81 | keyLines[0] | "Ionic bonding happens between a metal and a non-metal." | 4.2.1.1 | OK | |
| 82 | keyLines[1] | metal atom loses outer electrons → positive ion | 4.2.1.2 | OK | |
| 83 | keyLines[2] | non-metal gains them → negative ion. "Both now have full outer shells." | 4.2.1.2 | OK | Same generalisation as row 14, but the very next line scopes the card to Groups 1, 2, 6, 7, and a key note is a recall card; not changed. |
| 84 | keyLines[3] | Group 1 → 1+, Group 2 → 2+, Group 6 → 2−, Group 7 → 1− | 4.2.1.2 | OK | Uses AQA's "1+" order (the frozen py key_note's "+1" is not rendered by this page). |
| 85 | keyLines[4] | bond = strong electrostatic attraction between oppositely charged ions | 4.2.1.3 | OK | |
| 86 | keyLines[5] | charges balance, no overall charge: MgCl₂, Al₂O₃ | 4.2.1.2 / 4.1.1.1 | OK | Both formulae correct. |
| 87 | KeyNote `spec` | "AQA 5.2.1.2" | 8464 5.2.1.2 | OK | See row 1. |
| 88 | `legal` sentence 1 | figures show every shell; metal's electrons crosses, non-metal's dots | — | OK | True of this page's figures. |
| 89 | `legal` sentence 2 | real ions not in pairs; each surrounded on all sides by opposite ions in a giant lattice | 4.2.1.3 (limitations of dot-and-cross for a giant ionic structure) | OK | |
| 90 | `legal` sentence 3 | "GCSE draws only compounds of Group 1 and 2 metals with Group 6 and 7 non-metals; the forge adds nitride and aluminium ions for charge-balancing practice only." | 4.2.1.2 | OK | Accurate statement of the drawing limit and a correct disclosure. |
| 91 | `endPrev` / `endNext` / `endConnects` | chemical bonds ← → ionic compounds; covalent bonding, properties of ionic compounds | 4.2.1 / 4.2.2.3 | OK | Spec order. |
| 92 | tutor line | "Not sure which way the electrons go, or how many?" | — | OK | |
| 93 | bank CF1–CF10 (verbatim) | metal+non-metal → ionic; MgO pair; Cl⁻ 1−; Mg loses 2; charge from group; NaCl electrons; neutrality; CaCl₂; why + / −; NaCl dot-and-cross | 4.2.1.1–4.2.1.2 | OK | All keys and wrong-explanations checked; see §4 for CF5. |
| 94 | bank CH1–CH10 | incl. CH6 MgCl₂, CH7 "bond is the transfer", CH8 K₂O, CH9 noble gases, CH10 Al₂O₃ | 4.2.1.2, 4.1.2.1 | OK | All arithmetic in wrong-explanations recomputed (±1, +3, −1, −3 etc.). |
| 95 | bank TF1–TF12 | CF set + MgCl₂ + K₂O | 4.2.1.2 | OK | |
| 96 | bank TH1–TH12 | CH set + TH11 X²⁺/Y³⁻ → X₃Y₂ + TH12 dot-and-cross limitation | 4.2.1.2, 4.2.1.3 | OK | TH11 w2: X₂Y₃ = +4 −9 = −5, correct. |
| 97 | `K.item` option order | options re-ordered by FNV hash of stem+text; reply bound by original index before the sort | — | OK | Feedback stays attached to the right option (checked in ks4-lib.js). Flag 16. |

## 2. Required changes
| id | where (Design file + the exact `old` string, verbatim, unique in the file) | new string (verbatim) | why | spec section |
|---|---|---|---|---|
| ionic-bonding-C1 | `ks4-chemistry-5.2.1.2-ionic-bonding.dc.html`: `Both end up with the electron arrangement of a noble gas.` | `For Groups 1, 2, 6 and 7, both end up with the electron arrangement of a noble gas.` | Stated for every metal + non-metal; the spec restricts the noble-gas arrangement to ions of Groups 1, 2, 6 and 7, and it is false for transition-metal ions pupils meet in 4.1.3.2 (Fe²⁺, Cu²⁺). | 8462 4.2.1.2 / 8464 5.2.1.2 |
| ionic-bonding-C2 | `ks4-chemistry-5.2.1.2-ionic-bonding.dc.html`: `fLocked: fWorked \|\| fZero, fBtnStyle: this.seg(false, fWorked \|\| fZero),` | `fLocked: fWorked \|\| fMin, fBtnStyle: this.seg(false, fWorked \|\| fMin),` | Behaviour that contradicts the page's own instruction: at a balanced but non-simplest box the verdict says "Empty the box and use fewer ions" while the Empty button is disabled. Locking only on the simplest ratio makes the instruction possible. (Pipes are escaped as `\|` only because this is a Markdown table; in both the old and new strings each `\|\|` is a plain JavaScript OR, two pipe characters.) | 8462 4.2.1.3 (empirical formula) |
| ionic-bonding-C3 | `ks4-chemistry-5.2.1.2-ionic-bonding.dc.html`: `fZero, fHasNext: s.f < 2,` | `fZero, fHasNext: fMin && s.f < 2,` | A non-simplest ratio can currently be banked as "balanced" and the pupil moved on, immediately after being told it is not the formula. | 8462 4.2.1.3 |
| ionic-bonding-C4 | `ks4-chemistry-5.2.1.2-ionic-bonding.dc.html`: `fProgress: s.fDone.length + ' of 3 balanced'` | `fProgress: (s.fDone.length + (s.f === 2 && fMin ? 1 : 0)) + ' of 3 balanced'` | The third compound has no Next button, so it is never added to `fDone`; a correct Ca₃N₂ shows "2 of 3 balanced". (`fMin` is declared above the return object.) Rail completion (`fDone.length >= 2`) is unaffected. | — (self-contradiction) |

All four `old` strings were verified with `grep -cF` against the Design file: each matches exactly once.

## 3. Route tags
| content | Design's tag | spec label | verdict | change id if any |
|---|---|---|---|---|
| Whole lesson (ions, charges from group, dot-and-cross, electrostatic bond) | base (no `sc-if`) | 4.2.1.2 / 5.2.1.2 — no HT, not chemistry-only | OK | — |
| Worked Na+Cl, Mg+O; Draw Li+F, K+Cl, Ca+O, Mg+S | base | 4.2.1.2 drawing limit (Groups 1, 2 with 6, 7) | OK | — |
| Formula forge (Al₂O₃, Li₂S, Ca₃N₂) | base | formulae from given ion charges: 4.1.1.1 base, all tiers | OK — see §5 | — |
| Ladder r1–r4 | base | 4.2.1.2 / 4.2.1.3 base | OK | — |
| Content that should be tagged and is not | — | — | None found. Nothing in the lesson is HT or chemistry-only. | — |
| Spec number shown on Triple routes (eyebrow, KeyNote `spec`) | "5.2.1.2" on all routes | 8462 numbers it 4.2.1.2 | Note for Code (cross-lesson, all 14 pages): consider route-dependent numbering. Not a science error. | — |

## 4. Verbatim layer (the repo's four files)
| route | field | finding | change id if any |
|---|---|---|---|
| CF/CH/TF/TH | quiz vs ks4-source.js | Byte-identical per route (10/10/12/12 items), proven by script. | — |
| CF/CH/TF/TH | `higher` / `triple_only` / `rp` / `fifas` | None / None / None / [] on all four. Correct: 4.2.1.2 has no HT or chemistry-only content, no RP, no calculation. | — |
| CF/CH/TF/TH | `examiner_tip` | Identical on all four; correct (4.2.1.3). Served verbatim. | — |
| CF/CH/TF/TH | `key_note` | "Group 1 → +1, Group 7 → −1" uses oxidation-state order rather than AQA's ion-charge order (1+, 1−). IMPRECISE notation but NOT rendered: Design's page uses its own `keyLines`, which write 1+ / 1−. No change to the frozen py. | — |
| CF/CH/TF/TH | `common_mistake` | Correct ("the bond is the transfer" misconception); not rendered separately (Design's amber panel carries it). | — |
| CF, TF | CF5 / TF5 key | "Group 1, 2 and 3 metals … (1+, 2+, 3+); Group 5, 6 and 7 non-metals … (3−, 2−, 1−)" goes beyond the spec's Groups 1, 2, 6, 7 limit, but is chemically correct (Al³⁺, N³⁻) and consistent with the forge. OK, keep. | — |
| CF/CH/TF/TH | CF6/CH1/TF6/TH1 | Na⁺ (2.8), Cl⁻ (2.8.8): correct. | — |
| CH, TH | CH9 / TH9 (noble gases do not form ions) | 8462 4.1.2.1 base content; fine on Higher routes; its absence from CF/TF is fine. | — |
| CH, TH | CH10 / TH10 (Al₂O₃, "Aluminium is Group 3") | Correct in AQA's group numbering (the AQA periodic table uses 3 for B–Tl). | — |
| TH | TH11 (X²⁺ + Y³⁻ → X₃Y₂) | Correct; wrong-explanation arithmetic correct. Suitable for Higher. | — |
| TH | TH12 (limitation of dot-and-cross for solid NaCl) | Correct; it is 4.2.1.3 base content, not HT, so its being TH-only is a coverage choice, not a tagging error. | — |
| CF/CH/TF/TH | ladder r1 source item | "no overall electrical charge" found in each route's own copy (CF7, CH2, TF7, TH2); no silent TH fallback. | — |

## 5. Flags decided (from NOTES §9 that touch this lesson)
| flag | decision | spec section |
|---|---|---|
| 16 (option order) | Keep the deterministic hash re-order. "Verbatim" governs the wording of stems, options and explanations, which is untouched; AQA keys are not position-fixed, and the frozen always-first key is the defect (council #6). Checked: each option's reply is bound before the sort, so feedback cannot detach. Note (not a change): the worked stepper's own gate options are authored with the key at index 0 for gates 1 and 2 of both pairs; these are unscored process steps, so left as authored. | — (assessment practice) |
| 18 (new science) | Every new item in this lesson verified — see §6. All correct. | 4.2.1.2, 4.2.1.3 |
| Al³⁺ / N³⁻ in the Formula forge (parent's question) | Acceptable on all four routes. The spec's "limited to Groups 1 and 2, and 6 and 7" governs working out a charge FROM THE GROUP NUMBER and drawing dot-and-cross diagrams; the forge does neither — it states Al³⁺ and N³⁻ on the buttons and asks only for charge balancing, which AQA examines freely with given ions (e.g. Al₂O₃ in 4.4.3.3, and the frozen CH10/TH10). The `legal` line already discloses it. No route tag needed. | 8462 4.2.1.2, 4.1.1.1, 4.4.3.3 |

## 6. New science introduced by Design (flag 18) — verified?
- Hook (Na in Cl₂, yellow flame, white crystals) and reveal — correct.
- Worked stepper, 3 gates × 2 pairs (Na+Cl, Mg+O), all `yes`/`no` replies — correct (rows 21–32).
- Misconception panel "the ionic bond is the transfer" — correct.
- Draw bench (Li+F, K+Cl, Ca+O, Mg+S) and every verdict line — correct (rows 39–46).
- Formula forge: Al₂O₃ worked (6+/6−), Li₂S (2+/2−), Ca₃N₂ (6+/6−) — correct formulae and arithmetic; three behaviour contradictions fixed by C2–C4.
- Explainers 1 and 2 — correct except the noble-gas generalisation (C1).
- Key fact, four command-word cards — correct.
- Ladder r2 BaF₂ (accept BaF2/BaF₂) — correct.
- Ladder r3 MgO chain (3 links, 2 herrings) — correct order and herring reasons.
- Ladder r4 LiF 4-mark Describe, 4 points + 2 rejects — correct; Li⁺ (2) and F⁻ (2.8) right.
- Key-note lines (6) — correct.
- `legal` line — correct.
