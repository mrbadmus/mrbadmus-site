# KS4 Chemistry — route audit against AQA 8464 (Trilogy) and 8462 (Chemistry)

Audited 1 Oct 2026. Sources: `site-routes.tsv` (93 chemistry rows), AQA 8464 §5 and AQA 8462 §4
spec text, and the four `all_subtopics_chemistry*.py` route files (read for page core where the
title/spec label alone did not settle it).

Rule applied: a page belongs on every route on which AQA teaches any of its CORE content; HT-only or
chemistry-only parts of an otherwise wider page are **layers**, not route changes.

Route codes: base = `CF CH TF TH`; HT-only = `CH TH`; chemistry-only = `TF TH`; chemistry-only + HT = `TH`.

**Result: 93 subtopics checked, 0 route changes required.** Every page's route matches the spec.
Four spec-label errors and several off-route layers are noted below for whoever next touches the data.

## 1. Every chemistry subtopic

| slug | site routes | true route | 8464 ref | 8462 ref | verdict | note (layers) |
|---|---|---|---|---|---|---|
| atoms-elements-compounds | CF CH TF TH | base | 5.1.1.1 | 4.1.1.1 | OK | HT layer: balanced half/ionic equations |
| mixtures | CF CH TF TH | base | 5.1.1.2 | 4.1.1.2 | OK | |
| model-of-the-atom | CF CH TF TH | base | 5.1.1.3 | 4.1.1.3 | OK | |
| subatomic-particles | CF CH TF TH | base | 5.1.1.4–5.1.1.5 | 4.1.1.4–4.1.1.5 | OK | |
| relative-atomic-mass | CF CH TF TH | base | 5.1.1.6 | 4.1.1.6 | OK | |
| electronic-structure | CF CH TF TH | base | 5.1.1.7 | 4.1.1.7 | OK | |
| periodic-table | CF CH TF TH | base | 5.1.2.1 | 4.1.2.1 | OK | |
| development-periodic-table | CF CH TF TH | base | 5.1.2.2 | 4.1.2.2 | OK | |
| metals-non-metals | CF CH TF TH | base | 5.1.2.3 | 4.1.2.3 | OK | |
| group-0 | CF CH TF TH | base | 5.1.2.4 | 4.1.2.4 | OK | |
| group-1 | CF CH TF TH | base | 5.1.2.5 | 4.1.2.5 | OK | |
| group-7 | CF CH TF TH | base | 5.1.2.6 | 4.1.2.6 | OK | |
| transition-metals | TF TH | chem-only | — | 4.1.3.1–4.1.3.2 | OK | TH `higher` field (d-electron configuration, oxidation-state calculation) is beyond the spec |
| chemical-bonds | CF CH TF TH | base | 5.2.1.1 | 4.2.1.1 | OK | |
| ionic-bonding | CF CH TF TH | base | 5.2.1.2 | 4.2.1.2 | OK | |
| ionic-compounds | CF CH TF TH | base | 5.2.1.3 | 4.2.1.3 | OK | |
| covalent-bonding | CF CH TF TH | base | 5.2.1.4 | 4.2.1.4 | OK | |
| metallic-bonding | CF CH TF TH | base | 5.2.1.5 | 4.2.1.5 | OK | |
| states-of-matter | CF CH TF TH | base | 5.2.2.1–5.2.2.2 | 4.2.2.1–4.2.2.2 | OK | HT layer: limitations of particle theory |
| properties-ionic-compounds | CF CH TF TH | base | 5.2.2.3 | 4.2.2.3 | OK | |
| properties-small-molecules | CF CH TF TH | base | 5.2.2.4 | 4.2.2.4 | OK | |
| polymers | CF CH TF TH | base | 5.2.2.5 | 4.2.2.5 | OK | |
| giant-covalent-structures | CF CH TF TH | base | 5.2.2.6 + 5.2.3.1–5.2.3.3 | 4.2.2.6 + 4.2.3.1–4.2.3.3 | OK | This page is where graphene/fullerenes (5.2.3.3, base) are taught on all four routes (theory + quiz). Label says only 5.2.2.6 |
| metals-alloys | CF CH TF TH | base | 5.2.2.7–5.2.2.8 | 4.2.2.7–4.2.2.8 | OK | |
| nanoparticles | TF TH | chem-only | — (5.2.3.3 overlap only) | 4.2.4.1–4.2.4.2 | OK | **Spec label wrong**: site says 5.2.3.3 (graphene & fullerenes, base); page core is nanoparticles, 8462 4.2.4 "(chemistry only)". Graphene/fullerene recap here is an overlap with giant-covalent-structures, not a reason to widen |
| conservation-of-mass | CF CH TF TH | base | 5.3.1.1 | 4.3.1.1 | OK | |
| relative-formula-mass | CF CH TF TH | base | 5.3.1.2 | 4.3.1.2 | OK | |
| mass-changes-reactions | CF CH TF TH | base | 5.3.1.3 | 4.3.1.3 | OK | |
| chemical-measurements | CF CH TF TH | base | 5.3.1.4 | 4.3.1.4 | OK | |
| percentage-yield | TF TH | chem-only | — | 4.3.3.1 | OK | HT layer: theoretical mass of product |
| atom-economy | TF TH | chem-only | — | 4.3.3.2 | OK | HT layer: choice of reaction pathway |
| concentration-of-solutions | CF CH TF TH | base | 5.3.2.5 | 4.3.2.5 (+4.3.4) | OK | HT layer (5.3.2.5): relate mass, volume, concentration. The page's `higher` field teaches mol/dm³ and titration calcs — that is 8462 4.3.4 "(chemistry only) (HT only)", so it is off-spec on CH (should be TH only). c₁V₁=c₂V₂ is not in either spec |
| moles | CH TH | HT | 5.3.2.1 (HT only) | 4.3.2.1 (HT only) | OK | |
| amounts-in-equations | CH TH | HT | 5.3.2.2 (HT only) | 4.3.2.2 (HT only) | OK | |
| using-moles-calculations | CH TH | HT | 5.3.2.3–5.3.2.4 (HT only) | 4.3.2.3–4.3.2.4 (HT only) | OK | Key note includes c = n ÷ V in mol/dm³ — 8462 4.3.4 chemistry-only, so off-spec on CH (TH-only layer) |
| reactivity-series | CF CH TF TH | base | 5.4.1.1–5.4.1.2 | 4.4.1.1–4.4.1.2 | OK | HT layer: ionic displacement equations (5.4.1.4) |
| extraction-of-metals | CF CH TF TH | base | 5.4.1.3 | 4.4.1.3 | OK | Phytomining/bioleaching in `higher` field belongs to 5.10.1.4 (has its own page) |
| oxidation-reduction | CF CH TF TH | base | 5.4.1.1 / 5.4.1.3 core; 5.4.1.4 (HT only) layer | 4.4.1.1 / 4.4.1.3; 4.4.1.4 (HT only) | OK | **Spec label misleading**: site cites only 5.4.1.4, which is "(HT only)". Page core (summary: "in terms of oxygen gain/loss") is base. Electron definition is an HT layer — but the CF key note states "lose electrons / gain electrons" and reducing/oxidising-agent electron language **unlabelled** on the Foundation route |
| reactions-of-acids | CF CH TF TH | base | 5.4.2.1–5.4.2.2 | 4.4.2.1–4.4.2.2 | OK | HT layer: redox in terms of electrons |
| salts-neutralisation | CF CH TF TH | base | 5.4.2.2–5.4.2.3 | 4.4.2.2–4.4.2.3 | OK | Key note's "titration to find volumes" route to a salt is chemistry-only (4.4.2.5) |
| ph-scale | CF CH TF TH | base | 5.4.2.4 | 4.4.2.4 | OK | `higher` field duplicates strong/weak acids (HT) |
| titrations | TF TH | chem-only | — | 4.4.2.5 (chemistry only) | OK | HT layer: mol/dm³ and g/dm³ calculations |
| electrolysis-principles | CF CH TF TH | base | 5.4.3.1 | 4.4.3.1 | OK | HT layer: half equations |
| electrolysis-molten | CF CH TF TH | base | 5.4.3.2 | 4.4.3.2 | OK | |
| electrolysis-extraction | CF CH TF TH | base | 5.4.3.3 | 4.4.3.3 | OK | |
| electrolysis-aqueous | CF CH TF TH | base | 5.4.3.4 | 4.4.3.4 | OK | |
| strong-weak-acids | CH TH | HT | 5.4.2.5 (HT only) | 4.4.2.6 (HT only) | OK | Note 8462 numbers it 4.4.2.6 |
| half-equations | CH TH | HT | 5.4.3.5 (HT only) | 4.4.3.5 (HT only) | OK | |
| exothermic-endothermic | CF CH TF TH | base | 5.5.1.1 | 4.5.1.1 | OK | |
| reaction-profiles | CF CH TF TH | base | 5.5.1.2 | 4.5.1.2 | OK | |
| cells-and-batteries | TF TH | chem-only | — | 4.5.2.1 | OK | |
| fuel-cells | TF TH | chem-only | — | 4.5.2.2 | OK | HT layer: electrode half equations |
| bond-energy-calculations | CH TH | HT | 5.5.1.3 (HT only) | 4.5.1.3 (HT only) | OK | |
| calculating-rates | CF CH TF TH | base | 5.6.1.1 | 4.6.1.1 | OK | HT layer: mol/s, tangent gradient |
| factors-affecting-rate | CF CH TF TH | base | 5.6.1.2 | 4.6.1.2 | OK | |
| collision-theory | CF CH TF TH | base | 5.6.1.3 | 4.6.1.3 | OK | |
| catalysts | CF CH TF TH | base | 5.6.1.4 | 4.6.1.4 | OK | |
| reversible-reactions-equilibrium | CF CH TF TH | base | 5.6.2.1–5.6.2.3 | 4.6.2.1–4.6.2.3 | OK | `higher` field (Le Chatelier) duplicates the HT page below |
| effect-of-conditions-equilibrium | CH TH | HT | 5.6.2.4–5.6.2.7 (all HT only) | 4.6.2.4–4.6.2.7 (all HT only) | OK | |
| crude-oil-hydrocarbons | CF CH TF TH | base | 5.7.1.1 | 4.7.1.1 | OK | |
| fractional-distillation | CF CH TF TH | base | 5.7.1.2 | 4.7.1.2 | OK | |
| properties-of-hydrocarbons | CF CH TF TH | base | 5.7.1.3 | 4.7.1.3 | OK | |
| cracking-alkenes | CF CH TF TH | base | 5.7.1.4 | 4.7.1.4 | OK | `higher` field (addition/condensation polymer formulae) is chemistry-only 4.7.3 — off-spec on CH |
| structure-of-alkenes | TF TH | chem-only | — | 4.7.2.1 | OK | |
| reactions-of-alkenes | TF TH | chem-only | — | 4.7.2.2 | OK | |
| alcohols | TF TH | chem-only | — | 4.7.2.3 | OK | |
| carboxylic-acids | TF TH | chem-only | — | 4.7.2.4 | OK | HT layer: why carboxylic acids are weak |
| addition-polymerisation | TF TH | chem-only | — | 4.7.3.1 | OK | |
| condensation-polymerisation | TH | chem-only + HT | — | 4.7.3.2 (HT only) | OK | |
| amino-acids | TH | chem-only + HT | — | 4.7.3.3 (HT only) | OK | |
| dna-naturally-occurring-polymers | TF TH | chem-only | — | 4.7.3.4 | OK | |
| pure-substances | CF CH TF TH | base | 5.8.1.1 | 4.8.1.1 | OK | |
| formulations | CF CH TF TH | base | 5.8.1.2 | 4.8.1.2 | OK | |
| chromatography | CF CH TF TH | base | 5.8.1.3 | 4.8.1.3 | OK | |
| testing-for-gases | CF CH TF TH | base | 5.8.2.1–5.8.2.4 | 4.8.2.1–4.8.2.4 | OK | |
| flame-tests | TF TH | chem-only | — | 4.8.3.1 | OK | |
| metal-hydroxides | TF TH | chem-only | — | 4.8.3.2 | OK | |
| carbonates-halides-sulfates | TF TH | chem-only | — | 4.8.3.3–4.8.3.5 | OK | |
| instrumental-methods | TF TH | chem-only | — | 4.8.3.6–4.8.3.7 | OK | |
| composition-of-atmosphere | CF CH TF TH | base | 5.9.1.1 | 4.9.1.1 | OK | |
| early-atmosphere | CF CH TF TH | base | 5.9.1.2–5.9.1.4 | 4.9.1.2–4.9.1.4 | OK | Miller–Urey in `higher` field is not on either spec |
| greenhouse-gases | CF CH TF TH | base | 5.9.2.1–5.9.2.4 | 4.9.2.1–4.9.2.4 | OK | |
| atmospheric-pollutants | CF CH TF TH | base | 5.9.3.1–5.9.3.2 | 4.9.3.1–4.9.3.2 | OK | |
| earths-resources | CF CH TF TH | base | 5.10.1.1 | 4.10.1.1 | OK | |
| potable-water | CF CH TF TH | base | 5.10.1.2–5.10.1.3 | 4.10.1.2–4.10.1.3 | OK | |
| life-cycle-assessment | CF CH TF TH | base | 5.10.2.1 | 4.10.2.1 | OK | |
| reducing-use-of-resources | CF CH TF TH | base | 5.10.2.2 | 4.10.2.2 | OK | |
| corrosion-prevention | TF TH | chem-only | — | 4.10.3.1 | OK | |
| alloys-useful-materials | TF TH | chem-only | — | 4.10.3.2 | OK | |
| ceramics-polymers-composites | TF TH | chem-only | — | 4.10.3.3 | OK | |
| haber-process | TF TH | chem-only | — | 4.10.4.1 | OK | HT layer: interpret rate/yield graphs, compromise conditions |
| npk-fertilisers | TF TH | chem-only | — | 4.10.4.2 | OK | |
| alternative-metal-extraction | CH TH | HT | 5.10.1.4 (HT only) | 4.10.1.4 (HT only) | OK | |

## 2. Changes (non-OK rows)

**None.** No page needs to move route.

Every `TF TH` page maps to an 8462 section headed "(chemistry only)" with no 8464 equivalent
(4.1.3, 4.2.4, 4.3.3, 4.4.2.5, 4.5.2, 4.7.2, 4.7.3, 4.8.3, 4.10.3, 4.10.4). Every `CH TH` page maps
to a section headed "(HT only)" in both specs (5.3.2.1–5.3.2.4, 5.4.2.5, 5.4.3.5, 5.5.1.3,
5.6.2.4–5.6.2.7, 5.10.1.4). The two `TH` pages are "(HT only)" inside a chemistry-only section
(4.7.3.2, 4.7.3.3).

### Non-route corrections worth making (spec labels and layer leaks)

1. **nanoparticles — wrong spec label.** Site: `5.2.3.3`. 8464 5.2.3.3 is "Graphene and fullerenes"
   (base). The page is 8462 "4.2.4 Bulk and surface properties of matter including nanoparticles
   (chemistry only)" → relabel `4.2.4.1–4.2.4.2`. Route stays TF TH.
2. **oxidation-reduction — misleading label + unlabelled HT content on Foundation.** Site: `5.4.1.4`,
   which is "Oxidation and reduction in terms of electrons (HT only)". Core is 5.4.1.1 "explain
   reduction and oxidation in terms of loss or gain of oxygen" / 5.4.1.3 "Reduction involves the loss
   of oxygen" → relabel `5.4.1.1, 5.4.1.3 (+5.4.1.4 HT)`. The CF/TF key note teaches "lose
   electrons / gain electrons" with no HT marker — should be ⭐-labelled or moved into `higher`.
3. **giant-covalent-structures — label understates scope.** Carries 5.2.3.1–5.2.3.3 (diamond, graphite,
   graphene, fullerenes) on every route; label is 5.2.2.6 only.
4. **Chemistry-only HT content leaking onto CH** via `higher` fields: concentration-of-solutions
   (mol/dm³ and titration calcs = 4.3.4 / 4.4.2.5 HT, chemistry only), using-moles-calculations
   (c = n ÷ V in mol/dm³ = 4.3.4), cracking-alkenes (polymer formulae, condensation = 4.7.3).
   These belong in the TH layer only. They are layer fixes, not route changes.

## 3. Not settled / worth Mide's eye

- **No page exists for 8462 4.3.5 "Use of amount of substance in relation to volumes of gases
  (chemistry only) (HT only)"** (24 dm³, gas volume calculations) — a TH-only spec point with no
  home. 4.3.4 (mol/dm³) is partly covered inside concentration-of-solutions / using-moles-calculations /
  titrations but has no page of its own. Best reading: add a TH page (or a TH layer on
  using-moles-calculations) for 4.3.5; it is a gap, not a mis-route.
- **nanoparticles widening was considered and rejected.** Its site label points at a base spec point
  (5.2.3.3), which on the face of it argues MOVE WIDER. But the page's title and core are
  nanoparticles (4.2.4, chemistry only), and 5.2.3.3 is already taught on all four routes inside
  giant-covalent-structures (theory and quiz confirmed in all four route files). So TF TH stands.
- **oxidation-reduction narrowing was considered and rejected.** Its label (5.4.1.4) is wholly HT,
  which would argue MOVE NARROWER → CH TH. But the page's stated purpose is oxygen-based redox, base
  content in 5.4.1.1/5.4.1.3, and no other base page owns that definition. Base stands; the electron
  part is a layer.
- Content accuracy (whether specific statements in the frozen data are credit-worthy) was not
  audited beyond what was needed to decide each page's core.
