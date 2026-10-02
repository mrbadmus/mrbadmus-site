# Batch 9 — diagram library audit

Method: grepped `figlib/biology.py`, `figlib/biochem.py`, `figlib/chemistry.py`,
`figlib/physics.py`, `figlib/ks4phys.py`, `figlib/charts.py`,
`shared/ks4-diagrams.js`, `ks3_art/*.py` and `ks4_lessons/authored/batch-2/`
+ `batch-3/*.dc.html` for function names and docstrings naming each lesson's
subject matter, then read the matching function/docstring to confirm it is a
real match and not a substring collision. Near-hits checked and ruled out:
`ks4_lessons/authored/batch-2/eukaryotes-prokaryotes.dc.html` (promising by
name for classification-living-organisms — checked in full for
`kingdom`/`domain`/`archaea`/`classif`/`taxonom`, zero hits: it is a cell-
biology lesson about cell structure, not taxonomy) and
`ks4_lessons/authored/batch-2/chromosomes-mitosis.dc.html` (promising by name
for variation — checked in full for `mutation`/`variation`, zero hits: it
contrasts mitosis and meiosis as processes, not as a source of genetic
variation). No `K.hrefFor(...)`/connects-array forward reference to any of
this batch's 15 slugs exists anywhere in `ks4_lessons/authored/batch-2/` or
`batch-3/` (checked against every slug individually). `shared/ks4-diagrams.js`
remains entirely circuit-symbol and bonding/particle-model primitives —
nothing in it concerns any Batch-9 topic; listed here as checked, not cited
again below.

| # | Lesson | Existing drawing code that already covers it |
|---|---|---|
| 1 | dna-structure | **Direct match, three pieces:** `figlib/biology.py:353 dna_schematic()` ("DNA as a ladder with sugar-phosphate backbone and base pairs") and `figlib/biology.py:811 dna_ladder()` ("DNA untwisted into a ladder... every rung the same width") both draw the double-helix/backbone/base-pair structure this lesson teaches directly. `ks3_art/b10.py:813 _nested_scale()` is a reusable KS3 five-panel figure (cell → nucleus → chromosome → gene → bases, one continuous orange strand threading all five) that draws exactly the chromosome/gene/DNA relationship this lesson's spec point turns on, drawn as a DOM figure for a different key stage. `figlib/biochem.py:56 xray_pattern()` ("dark dashes along the four arms of an X on a pale oval... no text at all") is a reusable generic X-ray-diffraction figure with no current caller anywhere (checked) — relevant to the Franklin/Wilkins X-ray crystallography history this spec point covers, but not currently wired to any DNA-history content. |
| 2 | genetic-inheritance | **Direct match:** `figlib/biology.py:60 punnett_square()` — "2x2 Punnett square for two heterozygous (or any) parents" — exactly this lesson's dominant/recessive cross content. **Reusable KS3 instrument:** `ks3_art/b10.py:464 _punnett()` / `_punnett_gamete()` / `_punnett_flower()` — a DOM Punnett-square bench for a different key stage, same cross mechanism. |
| 3 | inherited-disorders | **Reusable, same mechanism:** `figlib/biology.py:60 punnett_square()` draws the identical cross this lesson applies to a named disorder (cystic fibrosis, polydactyly) rather than an abstract trait — a genuine reuse, not a disorder-specific figure. No screening-method or pedigree-chart figure exists anywhere. |
| 4 | sex-determination | None found anywhere searched. No XX/XY chromosome cross or sex-determination figure exists in figlib or ks3_art. |
| 5 | variation | **Direct match, KS3 instrument:** `ks3_art/b10.py:1263 r_variation_plotter()` — "predict the shape, then plot it", a continuous-vs-discontinuous variation bar-chart bench — exactly this lesson's genetic-vs-environmental-variation distinction, drawn as a DOM instrument for a different key stage. No figlib static figure exists. |
| 6 | evolution-natural-selection | **Direct match:** `figlib/biology.py:875 moth_pair()` — "the same pale moth and the same dark moth, on two barks, side by side" — the classic peppered-moth industrial-melanism example this lesson is built around. **Reusable KS3 instrument family:** `ks3_art/b11.py` — `r_advantage_bench()` (change the environment, watch survival change), `r_selection_runner()` (run the generations, peppered-moth allele frequency over time), `r_pressure_bench()` (species × pressure resilience grid) — all drawn as DOM benches for a different key stage's natural-selection unit. |
| 7 | selective-breeding | **Reusable, contingent match:** `ks3_art/b11.py:1132 r_blight_bench()` — "plant it, then release the blight" — a crop-variety bench where genetic diversity (versus a cloned, zero-diversity field) determines how many plants survive disease — the same selection-for-a-trait mechanism this lesson teaches, drawn for crop blight resistance specifically rather than selective breeding's artificial-selection procedure (choosing parents, repeating over generations). |
| 8 | genetic-engineering | None found anywhere searched. No plasmid/vector/restriction-enzyme figure exists in figlib or ks3_art. |
| 9 | cloning | **Reusable, contingent match:** `ks3_art/b11.py:1132 r_blight_bench()`'s "clone field" specifically returns zero survivors by construction (zero genetic variation = zero resistance) — a genuine illustration of cloning's core drawback (no variation), though the bench is framed as a crop-variety comparison, not a cloning-technique (tissue culture, embryo splitting, adult cell cloning) figure. No figure of any actual cloning method exists. |
| 10 | theory-of-evolution | None found anywhere searched. No Darwin-vs-Lamarck contrast or speciation figure exists; the `ks3_art/b11.py` natural-selection bench family (cited under #6) is background-relevant to the mechanism but draws no history-of-ideas or speciation content. |
| 11 | understanding-genetics | **Reusable, contingent match:** `figlib/biology.py:60 punnett_square()` draws the Mendelian cross (the 3:1 ratio) this lesson's history turns on, though with no attribution to Mendel or pea plants — `ks3_art/b10.py`'s own code comments name "Mendel's 3:1" when describing its Pp × Pp ordering, confirming the cross IS Mendel's, but nothing in either file draws Mendel himself, his pea-plant experiments, or how his work was received. |
| 12 | evidence-for-evolution | None found anywhere searched. No fossil-record, comparative-anatomy or molecular-evidence figure exists. |
| 13 | fossils-extinction | None found anywhere searched. No fossil-formation process figure or extinction-cause figure exists; `figlib/chemistry.py:2332` draws a "Fossil fuels" box inside `carbon_cycle()` — a substring collision, not a match (fossil FUELS, not fossils as evidence of past life). |
| 14 | resistant-bacteria | **Reusable, contingent match:** `ks3_art/b11.py:876 r_pressure_bench()` ("who survives what" — a species × selective-pressure grid) is the same selection-under-pressure mechanism antibiotic resistance runs on, though drawn for named animal species against named environmental pressures, not bacteria against antibiotics. No bacteria/antibiotic/culture-specific figure exists anywhere (checked `bacteri`, `antibiotic`, `culture`, `petri`, `agar` across figlib — the only hits are `nitrogen_cycle()`'s unrelated soil-bacteria boxes). |
| 15 | classification-living-organisms | None found anywhere searched. No Linnaean-rank, kingdom or domain classification figure exists in figlib or ks3_art. |

## Figures still needed

1. **dna-structure** — a labelled nucleotide figure (phosphate, sugar, base, complementary base pairing A–T/C–G) distinct from `dna_schematic()`/`dna_ladder()`'s whole-molecule view, plus a short scientific-history figure (Watson, Crick, Franklin, Wilkins, the X-ray diffraction evidence) — `xray_pattern()` exists for the evidence half but has no caller yet.
2. **genetic-inheritance** — none needed for the core cross; `punnett_square()` already covers it directly. A genotype/phenotype/homozygous/heterozygous vocabulary figure would complement the cross.
3. **inherited-disorders** — a named-disorder figure: polydactyly (dominant, autosomal) alongside cystic fibrosis (recessive, autosomal) with their inheritance patterns contrasted, plus a short note on embryo screening.
4. **sex-determination** — an XX/XY cross figure (father's sperm X or Y determines sex), the one genuinely missing figure in this batch with zero existing code to reuse.
5. **variation** — a genetic-vs-environmental-vs-combined variation classification figure, distinct from `r_variation_plotter()`'s continuous/discontinuous distribution angle.
6. **evolution-natural-selection** — none needed for the peppered-moth example; `moth_pair()` already covers it. A general variation → selection pressure → differential survival → allele frequency change flow figure (the PROCESS this lesson is built around) is still needed.
7. **selective-breeding** — a step-by-step selective-breeding figure (choose desired trait → select parents showing it → breed → repeat over generations → inbreeding-depression risk), distinct from `r_blight_bench()`'s disease-resistance framing.
8. **genetic-engineering** — a cut (restriction enzyme) → insert (into a vector) → transfer (into target cell) flow figure — the PROCESS family's example lesson and currently has nothing to reuse at all.
9. **cloning** — a technique-classification figure: tissue culture (plant) vs embryo splitting vs adult cell cloning (animal, Dolly-style), distinct from `r_blight_bench()`'s contingent variation angle.
10. **theory-of-evolution** — a Darwin-vs-Lamarck contrast figure (natural selection acting on existing variation vs inheritance of acquired characteristics) plus a simple speciation figure (populations separated → different selection pressures → unable to interbreed).
11. **understanding-genetics** — a Mendel pea-plant figure (his crosses, the 3:1 ratio he observed, and why his work was not recognised until decades after his death), distinct from the generic, unattributed Punnett-square figures already available.
12. **evidence-for-evolution** — a weighing-the-evidence figure: fossil record + comparative anatomy (homologous structures) + molecular evidence (DNA/protein similarity) as three independent lines converging on one conclusion.
13. **fossils-extinction** — a fossil-formation process figure (hard parts in sediment → mineral replacement → rock, or amber/ice preservation) alongside a causes-of-extinction figure (environmental change, new predators/competitors/disease, catastrophic event).
14. **resistant-bacteria** — an antibiotic-resistance-by-natural-selection figure centred on bacteria specifically (population exposed to antibiotic → susceptible bacteria die → resistant survivors multiply → resistant population dominates), distinct from `r_pressure_bench()`'s animal-and-environmental-pressure framing.
15. **classification-living-organisms** — a Linnaean hierarchy figure (kingdom → phylum → class → order → family → genus → species) alongside a three-domain figure (Bacteria, Archaea, Eukarya) showing why Woese's molecular evidence moved Archaea out of the old five-kingdom Bacteria/Prokaryote grouping — the one genuinely missing figure with zero existing code anywhere to reuse.
