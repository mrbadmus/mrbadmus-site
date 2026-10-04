# KS4 Biology — route audit against AQA 8464 / 8461

Audited 1 Oct 2026. Sources: `site-routes.tsv` (89 biology rows), AQA 8464 (Combined
Science: Trilogy, v1.1) and AQA 8461 (Biology), and the page content in
`all_subtopics_biology*.py`. The page-count check holds: CF 67 / CH 67 / TF 87 / TH 89,
which is 67 base + 20 `TF TH` + 2 `TH`. No biology page is `CH TH`.

**The rule applied.** A page sits on every route where AQA teaches any of its CORE content. A part
of a page that is HT-only or biology-only is a **layer** inside the page and does not change the
route.

**The spec refs are AQA's own numbers.** The site's `site_spec` column often uses different
numbers from AQA's (for example, classification is labelled 4.6.5 but AQA numbers it 4.6.4, and
theory-of-evolution is labelled 4.6.3.3 but AQA numbers it 4.6.3.1). The refs below come from the
spec files, not from the site.

Route key: base = `CF CH TF TH`; Higher-only = `CH TH`; Biology-only = `TF TH`; Biology-only and HT-only = `TH`.

## 1. Every biology subtopic

| slug | site routes | true route | 8464 ref | 8461 ref | verdict | note (layers) |
|---|---|---|---|---|---|---|
| eukaryotes-prokaryotes | CF CH TF TH | CF CH TF TH | 4.1.1.1 | 4.1.1.1 | OK | |
| animal-plant-cells | CF CH TF TH | CF CH TF TH | 4.1.1.2 | 4.1.1.2 | OK | |
| cell-specialisation | CF CH TF TH | CF CH TF TH | 4.1.1.3–4 | 4.1.1.3–4 | OK | |
| microscopy | CF CH TF TH | CF CH TF TH | 4.1.1.5 | 4.1.1.5 | OK | |
| chromosomes-mitosis | CF CH TF TH | CF CH TF TH | 4.1.2.1–2 | 4.1.2.1–2 | OK | |
| stem-cells | CF CH TF TH | CF CH TF TH | 4.1.2.3 | 4.1.2.3 | OK | |
| transport-in-cells | CF CH TF TH | CF CH TF TH | 4.1.3.1–3 | 4.1.3.1–3 | OK | |
| culturing-microorganisms | TF TH | TF TH | — | 4.1.1.6 (biology only) | OK | HT layer: answers in standard form. RP2 in 8461 |
| principles-of-organisation | CF CH TF TH | CF CH TF TH | 4.2.1 | 4.2.1 | OK | |
| digestive-system | CF CH TF TH | CF CH TF TH | 4.2.2.1 | 4.2.2.1 | OK | |
| enzymes | CF CH TF TH | CF CH TF TH | 4.2.2.1 | 4.2.2.1 | OK | |
| heart-blood-vessels | CF CH TF TH | CF CH TF TH | 4.2.2.2 | 4.2.2.2 | OK | |
| blood | CF CH TF TH | CF CH TF TH | 4.2.2.3 | 4.2.2.3 | OK | |
| coronary-heart-disease | CF CH TF TH | CF CH TF TH | 4.2.2.4 | 4.2.2.4 | OK | |
| health-disease | CF CH TF TH | CF CH TF TH | 4.2.2.5–6 | 4.2.2.5–6 | OK | |
| cancer | CF CH TF TH | CF CH TF TH | 4.2.2.7 | 4.2.2.7 | OK | |
| plant-tissues | CF CH TF TH | CF CH TF TH | 4.2.3.1 | 4.2.3.1 | OK | |
| transpiration | CF CH TF TH | CF CH TF TH | 4.2.3.2 | 4.2.3.2 | OK | |
| translocation | CF CH TF TH | CF CH TF TH | 4.2.3.2 | 4.2.3.2 | OK | |
| communicable-diseases-defence | CF CH TF TH | CF CH TF TH | 4.3.1.1, 4.3.1.6 | 4.3.1.1, 4.3.1.6 | OK | |
| viral-diseases | CF CH TF TH | CF CH TF TH | 4.3.1.2 | 4.3.1.2 | OK | |
| bacterial-diseases | CF CH TF TH | CF CH TF TH | 4.3.1.3 | 4.3.1.3 | OK | |
| fungal-protist-diseases | CF CH TF TH | CF CH TF TH | 4.3.1.4–5 | 4.3.1.4–5 | OK | |
| vaccination | CF CH TF TH | CF CH TF TH | 4.3.1.7 | 4.3.1.7 | OK | |
| antibiotics-painkillers | CF CH TF TH | CF CH TF TH | 4.3.1.8 | 4.3.1.8 | OK | |
| drug-discovery-development | CF CH TF TH | CF CH TF TH | 4.3.1.9 | 4.3.1.9 | OK | |
| plant-disease-detection-defence | TF TH | TF TH | — | 4.3.3 (biology only) | OK | HT layer: detection and identification methods (the "(HT only) Plant diseases can be detected by:" line) |
| monoclonal-antibodies | TH | TH | — | 4.3.2 (biology only) (HT only) | OK | |
| photosynthesis | CF CH TF TH | CF CH TF TH | 4.4.1.1 | 4.4.1.1 | OK | |
| rate-of-photosynthesis | CF CH TF TH | CF CH TF TH | 4.4.1.2 | 4.4.1.2 | OK | HT layer: interacting limiting factors, inverse square law, economics |
| uses-of-glucose | CF CH TF TH | CF CH TF TH | 4.4.1.3 | 4.4.1.3 | OK | |
| aerobic-respiration | CF CH TF TH | CF CH TF TH | 4.4.2.1 | 4.4.2.1 | OK | |
| anaerobic-respiration | CF CH TF TH | CF CH TF TH | 4.4.2.1 | 4.4.2.1 | OK | |
| response-to-exercise | CF CH TF TH | CF CH TF TH | 4.4.2.2 | 4.4.2.2 | OK | HT layer: lactic acid to liver, oxygen debt |
| metabolism | CF CH TF TH | CF CH TF TH | 4.4.2.3 | 4.4.2.3 | OK | |
| homeostasis | CF CH TF TH | CF CH TF TH | 4.5.1 | 4.5.1 | OK | |
| nervous-system | CF CH TF TH | CF CH TF TH | 4.5.2 | 4.5.2.1 | OK | |
| reflex-actions | CF CH TF TH | CF CH TF TH | 4.5.2 | 4.5.2.1 | OK | |
| reaction-time | CF CH TF TH | CF CH TF TH | 4.5.2 (RP6) | 4.5.2.1 (RP7) | OK | |
| thermoregulation | TF TH | TF TH | — (4.5.1 lists "body temperature" only as a controlled condition) | 4.5.2.4 (biology only) | OK | HT layer: explaining how the mechanisms raise or lower body temperature |
| endocrine-system | CF CH TF TH | CF CH TF TH | 4.5.3.1 | 4.5.3.1 | OK | HT layer: thyroxine/adrenaline negative feedback (8464 4.5.3.6 / 8461 4.5.3.7, both whole-section HT only) |
| blood-glucose-diabetes | CF CH TF TH | CF CH TF TH | 4.5.3.2 | 4.5.3.2 | OK | HT layer: glucagon |
| human-reproduction-hormones | CF CH TF TH | CF CH TF TH | 4.5.3.3 | 4.5.3.4 | OK | HT layer: interactions of FSH, LH, oestrogen and progesterone |
| contraception-fertility | CF CH TF TH | CF CH TF TH | 4.5.3.4 (+4.5.3.5 HT) | 4.5.3.5 (+4.5.3.6 HT) | OK | HT layer: infertility treatment / IVF (the whole section is HT only). The core (contraception) is base |
| the-brain | TF TH | TF TH | — | 4.5.2.2 (biology only) | OK | HT layer: the difficulty of treating the brain, mapping its regions |
| the-eye | TF TH | TF TH | — | 4.5.2.3 (biology only) | OK | |
| defects-of-the-eye | TF TH | TF TH | — | 4.5.2.3 (biology only) | OK | |
| sexual-asexual-reproduction | CF CH TF TH | CF CH TF TH | 4.6.1.1 | 4.6.1.1 | OK | Leak: the page's advantages/disadvantages lists are 8461 4.6.1.3 (biology only), but they are served on base |
| **meiosis** | TF TH | **CF CH TF TH** | **4.6.1.2** | 4.6.1.2 (unmarked) | **MOVE WIDER → CF CH TF TH** | The page's `triple_only` note ("biology-only — not in Combined Science") is false. Its meiosis I/II detail goes beyond both specs ("Knowledge of the stages of meiosis is not required") |
| advantages-sexual-asexual | TF TH | TF TH | — | 4.6.1.3 (biology only) | OK | |
| dna-genome | CF CH TF TH | CF CH TF TH | 4.6.1.3 | 4.6.1.4 | OK | Leak: the "DNA Structure" section teaches nucleotides and A–T/C–G pairing. That is 8461 4.6.1.5 (biology only), and complementary pairing is also HT only there. It is served on CF |
| dna-structure | TF TH | TF TH | — | 4.6.1.5 (biology only) | OK | HT layer: protein synthesis, complementary strands, mutations |
| genetic-inheritance | CF CH TF TH | CF CH TF TH | 4.6.1.4 | 4.6.1.6 | OK | HT layer: constructing a Punnett square |
| inherited-disorders | CF CH TF TH | CF CH TF TH | 4.6.1.5 | 4.6.1.7 | OK | |
| sex-determination | CF CH TF TH | CF CH TF TH | 4.6.1.6 | 4.6.1.8 | OK | |
| variation | CF CH TF TH | CF CH TF TH | 4.6.2.1 | 4.6.2.1 | OK | |
| evolution-natural-selection | CF CH TF TH | CF CH TF TH | 4.6.2.2 | 4.6.2.2 | OK | Leak: the "Why Darwin's theory took time" and "Alfred Russel Wallace" sections are 8461 4.6.3.1 (biology only). 8464 has no mention of Wallace |
| theory-of-evolution | TF TH | TF TH | — | 4.6.3.1–2 (biology only) | OK | Overlaps heavily with evolution-natural-selection |
| selective-breeding | CF CH TF TH | CF CH TF TH | 4.6.2.3 | 4.6.2.3 | OK | |
| genetic-engineering | CF CH TF TH | CF CH TF TH | 4.6.2.4 | 4.6.2.4 | OK | HT layer: the main steps of genetic engineering |
| cloning | TF TH | TF TH | — (8464 has clones only within asexual reproduction and stem cells) | 4.6.2.5 (biology only) | OK | |
| evidence-for-evolution | CF CH TF TH | CF CH TF TH | 4.6.3.1 | 4.6.3.4 | OK | |
| understanding-genetics | TF TH | TF TH | — | 4.6.3.3 (biology only) | OK | |
| fossils-extinction | CF CH TF TH | CF CH TF TH | 4.6.3.2–3 | 4.6.3.5–6 | OK | |
| resistant-bacteria | CF CH TF TH | CF CH TF TH | 4.6.3.4 | 4.6.3.7 | OK | |
| **classification-living-organisms** | TF TH | **CF CH TF TH** | **4.6.4** | 4.6.4 (unmarked) | **MOVE WIDER → CF CH TF TH** | The page's `triple_only` note ("biology-only — not in Combined Science") is false |
| ecosystems | CF CH TF TH | CF CH TF TH | 4.7.1.1 | 4.7.1.1 | OK | |
| abiotic-biotic-factors | CF CH TF TH | CF CH TF TH | 4.7.1.2–3 | 4.7.1.2–3 | OK | |
| adaptations | CF CH TF TH | CF CH TF TH | 4.7.1.4 | 4.7.1.4 | OK | |
| food-chains-webs | CF CH TF TH | CF CH TF TH | 4.7.2.1 | 4.7.2.1 | OK | |
| population-competition | CF CH TF TH | CF CH TF TH | 4.7.1.1, 4.7.2.1 | 4.7.1.1, 4.7.2.1 | OK | |
| sampling-techniques | CF CH TF TH | CF CH TF TH | 4.7.2.1 (RP7) | 4.7.2.1 (RP9) | OK | |
| carbon-cycle | CF CH TF TH | CF CH TF TH | 4.7.2.2 | 4.7.2.2 | OK | Carries the base "microorganisms return CO₂" point |
| water-cycle | CF CH TF TH | CF CH TF TH | 4.7.2.2 | 4.7.2.2 | OK | |
| **decomposition** | CF CH TF TH | **TF TH** | (4.7.2.2 role of microorganisms only) | **4.7.2.3 (biology only)** | **MOVE NARROWER → TF TH** | The page's RP is labelled "RP7". Combined RP7 is quadrats; decay is 8461 **RP10** (milk, pH) |
| biodiversity | CF CH TF TH | CF CH TF TH | 4.7.3.1 | 4.7.3.1 | OK | |
| waste-management | CF CH TF TH | CF CH TF TH | 4.7.3.2 | 4.7.3.2 | OK | |
| land-use | CF CH TF TH | CF CH TF TH | 4.7.3.3 | 4.7.3.3 | OK | |
| deforestation | CF CH TF TH | CF CH TF TH | 4.7.3.4 | 4.7.3.4 | OK | |
| global-warming | CF CH TF TH | CF CH TF TH | 4.7.3.5 | 4.7.3.5 | OK | |
| maintaining-biodiversity | CF CH TF TH | CF CH TF TH | 4.7.3.6 | 4.7.3.6 | OK | |
| trophic-levels | TF TH | TF TH | — | 4.7.4.1 (biology only) | OK | |
| pyramids-of-biomass | TF TH | TF TH | — | 4.7.4.2 (biology only) | OK | |
| transfer-of-biomass | TF TH | TF TH | — | 4.7.4.3 (biology only) | OK | |
| environmental-change | TH | TH | — | 4.7.2.4 (biology only) (HT only) | OK | The site labels it 4.7.4 |
| factors-affecting-food-security | TF TH | TF TH | — | 4.7.5.1 (biology only) | OK | |
| farming-techniques | TF TH | TF TH | — | 4.7.5.2 (biology only) | OK | |
| sustainable-fisheries | TF TH | TF TH | — | 4.7.5.3 (biology only) | OK | |
| role-of-biotechnology | TF TH | TF TH | — | 4.7.5.4 (biology only) | OK | |

## 2. Changes (non-OK rows only)

1. **meiosis: `TF TH` → `CF CH TF TH` (MOVE WIDER).**
   - In 8464 it is section **4.6.1.2 Meiosis**, with no HT marker. The section says: "Students
     should be able to explain how meiosis halves the number of chromosomes in gametes and
     fertilisation restores the full number of chromosomes. … the cell divides twice to form four
     gametes, each with a single set of chromosomes … all gametes are genetically different from
     each other. … Knowledge of the stages of meiosis is not required."
   - 8461 4.6.1.2 has the same heading, also with no "(biology only)" marker.
   - Fix the page's false `triple_only` note at the same time.
   - When the page moves to CF, cut its meiosis I/II detail down to what 8464 asks for (the spec
     explicitly does not require the stages).
2. **classification-living-organisms: `TF TH` → `CF CH TF TH` (MOVE WIDER).**
   - In 8464 it is section **4.6.4 Classification of living organisms**, with no HT marker.
   - The section covers Linnaeus ("kingdom, phylum, class, order, family, genus and species …
     binomial system"), Woese's "'three-domain system' … Archaea … Bacteria … Eukaryota", and
     "Evolutionary trees".
   - 8461 4.6.4 has the same content, with no "(biology only)" marker.
   - Fix the page's false `triple_only` note at the same time.
3. **decomposition: `CF CH TF TH` → `TF TH` (MOVE NARROWER).**
   - The page's core is 8461 **"4.7.2.3 Decomposition (biology only)"**: "explain how temperature,
     water and availability of oxygen affect the rate of decay … compost … Biogas generators", and
     "Required practical activity 10: investigate the effect of temperature on the rate of decay of
     fresh milk by measuring pH change."
   - That covers two of the page's three sections ("Factors Affecting Decomposition Rate",
     "Decomposition in Human Contexts") and its RP. Combined (8464) has no decomposition section,
     no biogas, and only 7 RPs, none on decay.
   - The only base content on the page is the 8464 4.7.2.2 line ("explain the role of
     microorganisms in cycling materials … returning carbon to the atmosphere as carbon dioxide and
     mineral ions to the soil"). The carbon-cycle page already carries the CO₂ half of that.
   - Before narrowing, check that **"mineral ions to the soil"** still appears on a base page,
     ideally carbon-cycle. Also correct the RP label from RP7 to RP10.

## 3. Unsettled / worth knowing

- **Decomposition is the one judgement call.** If someone reads "What is Decomposition?" (the
  microorganisms' role) as the page's core, the page stays base, and only the rate factors,
  compost/biogas and RP become a biology-only layer. The best-evidenced reading is MOVE NARROWER:
  two of three sections and the RP are biology-only, the page title names an 8461-only section,
  and the base point already lives on carbon-cycle.
- **Biology-only content leaking onto base pages.** None of these changes a route, but each one
  shows Combined pupils content they will not be examined on. They should become layers:
  - sexual-asexual-reproduction carries the advantages/disadvantages lists (8461 4.6.1.3).
  - dna-genome carries nucleotides and complementary base pairing (8461 4.6.1.5, and the base
    pairing is HT only there).
  - evolution-natural-selection carries Wallace and the acceptance of Darwin's theory (8461 4.6.3.1).
  - Both flagged pages' content also duplicates the biology-only pages that already exist for it.
- **Biology-only content with no page at all.** There is no 8461 page for:
  - 4.5.3.3 *Maintaining water and nitrogen balance* (kidney, ADH, dialysis — the word "dialysis"
    appears nowhere in the site data)
  - 4.5.4 *Plant hormones* (auxin, gibberellins, RP8 — none appear)
  - 4.6.3.2 *Speciation*, which only appears in passing inside evolution pages.

  These are coverage gaps for TF/TH, not route errors.
- **The site's `site_spec` labels often do not match AQA's numbering.** Examples: cloning 4.6.4
  (really 4.6.2.5), understanding-genetics 4.6.3.4 (really 4.6.3.3), classification 4.6.5 (really
  4.6.4), environmental-change 4.7.4 (really 4.7.2.4), heart 4.2.3 (really 4.2.2.2). Use the refs
  in the table above.
