# Examination — Evolution and Natural Selection (evolution-natural-selection) — AQA 8464 4.6.2.2 / 8461 4.6.2.2
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-9/04-checked-science-source/biology-4.6.5-evolution-natural-selection.md` (the data's "4.6.5" is the site's internal number; AQA's is 4.6.2.2).
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 4.6.2.1, 4.6.2.2, 4.6.4; `AQA-8461-spec.txt` (v1.0) 4.6.2.1, 4.6.2.2, 4.6.3.1, 4.6.3.2, 4.6.3.4. No equation sheet applies. Route audit read: `ks4-routes/docs/ks4/route-audit/biology.md` row `evolution-natural-selection` and its "biology-only content leaking onto base pages" note.

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n (explains option n, 0-based); th1–th4 = theory chunks. The CF and TF copies differ from TH only in `higher` (`null` = not shown).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 Combined Trilogy | **4.6.2.2** | Evolution | base |
| 8461 Biology | **4.6.2.2** | Evolution | base |
| 8461 Biology | 4.6.3.1 | Theory of evolution | (biology only) — th3, q2 |
| 8461 Biology | 4.6.3.2 | Speciation | (biology only) — th4, `higher` speciation steps, Wallace |
| Supporting | 8464/8461 4.6.2.1 Variation (mutation is the source of variants); 8464/8461 4.6.4 Classification (evolutionary trees, DNA-based classification, base) | | base |

Spec statement (verbatim, 8464 4.6.2.2 = 8461 4.6.2.2): "Students should be able to describe evolution as a change in the inherited characteristics of a population over time through a process of natural selection which may result in the formation of a new species. The theory of evolution by natural selection states that all species of living things have evolved from simple life forms that first developed more than three billion years ago. Students should be able to explain how evolution occurs through natural selection of variants that give rise to phenotypes best suited to their environment. If two populations of one species become so different in phenotype that they can no longer interbreed to produce fertile offspring they have formed two new species." WS 1.2: "Use the theory of evolution by natural selection in an explanation."

8461 4.6.3.1 (biology only), verbatim extract: "The theory of evolution by natural selection was only gradually accepted because: • the theory challenged the idea that God made all the animals and plants that live on Earth • there was insufficient evidence at the time the theory was published to convince many scientists • the mechanism of inheritance and variation was not known until 50 years after the theory was published."
8461 4.6.3.2 (biology only), verbatim extract: "Alfred Russel Wallace independently proposed the theory of evolution by natural selection. He published joint writings with Darwin in 1858 which prompted Darwin to publish On the Origin of Species (1859) the following year. … Students should be able to describe the steps which give rise to new species."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Evolution = change in inherited characteristics of a population over time (th1; key_note) | base | 4.6.2.2 | all four | OK |
| R2 | All species evolved from simple life forms > 3 billion years ago | base | 4.6.2.2 | — | **GAP** (ENS-F1) |
| R3 | Natural selection of variants → phenotypes best suited to environment; five steps (th2; key_note) | base | 4.6.2.2; 4.6.2.1 | all four | OK; "survival of the fittest" needs unpacking (C8) |
| R4 | Darwin, HMS Beagle, Origin of Species 1859 (th2, th3) | base (context) / triple (history) | 4.6.2.2; 8461 4.6.3.1 | all four | OK |
| R5 | Why Darwin's theory was slowly accepted (th3) | triple | 8461 4.6.3.1 (biology only) | all four | **ROUTE** (ENS-F2) |
| R6 | Wallace; Linnean Society 1858; biogeography; Wallace's line (th4) | triple | 8461 4.6.3.2 (biology only) | all four | **ROUTE** (ENS-F2) |
| R7 | Two populations can no longer interbreed to produce fertile offspring → two new species | base | 4.6.2.2 | CH TH only (inside `higher`) | **ROUTE / GAP** (ENS-F3) |
| R8 | Speciation steps via geographic isolation (`higher`) | triple (not HT) | 8461 4.6.3.2 (biology only) | CH TH | **ROUTE** (ENS-F3) |
| R9 | DNA-based classification / phylogenetics (`higher`) | base (belongs to classification lesson) | 4.6.4 | CH TH | **ROUTE** (ENS-F3) |
| R10 | common_mistake: NS doesn't cause mutations; populations evolve; fittest = best adapted | base | 4.6.2.1; 4.6.2.2 | all four | OK |
| R11 | q1 — dark mice on dark soil | base | 4.6.2.2 | all four | wx2 WRONG (ENS-F4) |
| R12 | q2 — why Darwin's theory was controversial | triple | 8461 4.6.3.1 | all four | **ROUTE + WRONG** (ENS-F5) |
| R13 | q3 — "survival of the fittest" | base | 4.6.2.2 | all four | OK |
| — | RP, equations, FIFA, examiner_tip | none | — | — | correct (none in spec) |

True routes: CF CH TF TH (matches the site), with a triple layer (th3, th4, speciation steps, q2).

## 3. Check table
| # | item | claim (verbatim or abridged) | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | evolution = change in inherited characteristics of a population over many generations | OK | Spec says "over time"; equivalent. | 4.6.2.2 |
| C2 | th1 | driven by natural selection — individuals better suited more likely to survive and reproduce | OK | — | 4.6.2.2 |
| C3 | th1 | explains change, diversity, common ancestry, adaptation; supported by fossils, genetics, anatomy, observation | OK | Missing the spec's "simple life forms … more than three billion years ago" (ENS-F1). | 4.6.2.2; 4.6.3.4 |
| C4 | th2 | Darwin 1809–1882; HMS Beagle 1831–1836 | OK | Both dates correct. | — |
| C5 | th2 | step 1 variation | OK | Spec: variants arise from mutations (4.6.2.1). | 4.6.2.1 |
| C6 | th2 | steps 2–3 overproduction; struggle for survival / competition | OK | Not spec wording, standard and creditable. | — |
| C7 | th2 | step 5 surviving individuals pass on their alleles; advantageous alleles become more common | OK | Mark schemes credit "genes" or "alleles". | 4.6.2.2 |
| C8 | th2; q3 | "SURVIVAL OF THE FITTEST" | IMPRECISE (wording) | AQA mark schemes do not credit "survival of the fittest" on its own; pupils must write "better adapted / best suited to the environment, so more likely to survive and breed". Teach the phrase only as a label to be unpacked. | 4.6.2.2 |
| C9 | th3 | Origin of Species 1859 | OK | — | 8461 4.6.3.1 |
| C10 | th3 | not accepted: religious opposition; no mechanism of inheritance; insufficient evidence (fossil gaps) | OK | All three are the spec's reasons. Biology only. | 8461 4.6.3.1 |
| C11 | th3 | "Difficulty of the concept — evolution over millions of years is hard to observe directly" | OK (beyond spec) | True; not one of the spec's three reasons. Do not teach as a reason to recall. | 8461 4.6.3.1 |
| C12 | th3 | "as genetics was discovered (first Mendel, then Watson and Crick …)" | OK | Spec: mechanism not known until 50 years after publication. | 8461 4.6.3.1; 4.6.3.3 |
| C13 | th4 | Wallace 1823–1913; sent ideas to Darwin 1858; papers read at Linnean Society 1858 | OK | Dates correct (Linnean Society reading, 1 July 1858). Spec: joint writings 1858 prompted Darwin to publish in 1859. | 8461 4.6.3.2 |
| C14 | th4 | biogeography; Wallace's line between Asian and Australian distributions | OK (beyond spec) | True. Spec names Wallace's warning colouration and speciation work — not stated here. | 8461 4.6.3.2 |
| C15 | higher | "geographic isolation divides a population → different selection pressures → allele frequencies diverge → … reproductive isolation → no longer able to interbreed → two species" | IMPRECISE; ROUTE | The end point must be "can no longer interbreed to produce **fertile offspring**" (spec wording; mark-scheme point). Speciation steps are 8461 4.6.3.2 (biology only), **not HT**. | 4.6.2.2; 8461 4.6.3.2 |
| C16 | higher | "Wallace co-developed the theory … independently" | OK; ROUTE | Biology only, not HT. | 8461 4.6.3.2 |
| C17 | higher | "Modern classification uses DNA sequence comparisons … (phylogenetics)" | OK; ROUTE | True; belongs to 4.6.4 classification (base, both specs), not HT and not this lesson. | 4.6.4 |
| C18 | common_mistake | NS doesn't cause mutations; mutations random; NS selects from existing variation; populations not individuals evolve; fittest ≠ strongest | OK | Strong. | 4.6.2.1; 4.6.2.2 |
| C19 | key_note | summary as th2 | OK | "survival of the fittest" — see C8. | — |
| C20 | matching | 5 pairs | OK | To be replaced. | — |
| C21 | q1 key | dark mice better camouflaged, survive predation, reproduce, pass on dark-colour alleles | OK | Model natural-selection answer. | 4.6.2.2 |
| C22 | q1 wx1 | animals cannot deliberately change genetic traits | OK, aligned | — | — |
| C23 | q1 wx2 | (option 2 "Dark soil contains minerals that cause mice to become darker") "Environmental exposure doesn't directly change DNA — this would be Lamarckian evolution, which has been disproved. …" | **WRONG** | Two false claims. (a) Environmental agents *do* change DNA — ionising radiation and chemical mutagens cause mutations. (b) AQA does not say Lamarckism is "disproved": "We now know that in the vast majority of cases this type of inheritance cannot occur." Also, Lamarck is biology-only (8461 4.6.3.1) and this item is served on Combined. (ENS-F4) | 8461 4.6.3.1 |
| C24 | q1 wx3 | migration possible but NS primary; lighter mice more visible to predators | OK, aligned | — | — |
| C25 | q2 key | contradicted religious beliefs; Darwin lacked knowledge of the mechanism of inheritance | OK; ROUTE | Correct, but 8461 4.6.3.1 (biology only) — not on Combined. | 8461 4.6.3.1 |
| C26 | q2 option 3 | "Darwin published it before collecting sufficient evidence, making it speculative" | **WRONG (ambiguous distractor)** | Overlaps the spec's own third reason: "there was insufficient evidence at the time the theory was published to convince many scientists". A pupil who learned the spec can defend this option. (ENS-F5) | 8461 4.6.3.1 |
| C27 | q2 wx1 | Darwin travelled extensively (Galapagos, South America, Australia) | OK, aligned | Beagle did call at Australia. | — |
| C28 | q2 wx2 | "Darwin actually delayed publication for over 20 years … he published when he felt the evidence was compelling." | **WRONG** | The spec (and th4 of this same file) says Wallace's 1858 joint writings **prompted** Darwin to publish. The delay (~1838 → 1859) is right; the reason given is not. (ENS-F5) | 8461 4.6.3.2 |
| C29 | q2 wx3 | "The theory was considered TOO radical and COMPLICATED for many" | IMPRECISE | "Complicated" was not the objection; radical / contrary to religious belief was. | 8461 4.6.3.1 |
| C30 | q3 key | best adapted most likely to survive and reproduce — not necessarily strongest | OK | — | 4.6.2.2 |
| C31 | q3 wx1 | strength one possible advantage; toxic frog example | OK, aligned | — | — |
| C32 | q3 wx2 | size can be a disadvantage | OK, aligned | — | — |
| C33 | q3 wx3 | "many highly successful organisms (bacteria, insects) have no intelligence" | IMPRECISE (minor) | "Insects have no intelligence" is arguable; the point (intelligence is not what "fittest" means) stands. Usable. | — |

wrong_explanations alignment: all 9 keys read in full; every key n explains option n. No shifted keys. Count: **3 WRONG** (C23 q1 wx2; C26 + C28 q2 — one flag each item); **IMPRECISE**: C8, C15, C29, C33; **GAP**: C3 (three billion years); **ROUTE**: R5, R6, R7–R9, R12. No `[NEW — to be examined]` lines in this file.
