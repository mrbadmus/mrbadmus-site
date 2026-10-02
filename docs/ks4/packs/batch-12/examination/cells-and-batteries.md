# Examination — Cells and Batteries (cells-and-batteries) — AQA 8462 4.5.2.1 (chemistry only)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-12/04-checked-science-source/chemistry-4.5.2.1-cells-and-batteries.md`.
Spec sources read as text: `AQA-8462-spec.txt` 4.5.2 intro, 4.5.2.1, 4.5.2.2; `AQA-8464-spec.txt` 5.5 (no 5.5.2 — chemical cells are not in Combined). No equation sheet applies. Route audit read: `chemistry.md` row `cells-and-batteries` (OK, chem-only, TF TH).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. TH copy carries a `higher` field; TF copy's `higher` is null.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8462 | **4.5.2.1** | Cells and batteries | 4.5.2 "Chemical cells and fuel cells (chemistry only)" |
| 8464 | — | not in Combined Science | — |
| Supporting | 8462 4.4.1.2 reactivity series | | base |

Spec statement (verbatim): "Cells contain chemicals which react to produce electricity. The voltage produced by a cell is dependent upon a number of factors including the type of electrode and electrolyte. A simple cell can be made by connecting two different metals in contact with an electrolyte. Batteries consist of two or more cells connected together in series to provide a greater voltage. In non-rechargeable cells and batteries the chemical reactions stop when one of the reactants has been used up. Alkaline batteries are non-rechargeable. Rechargeable cells and batteries can be recharged because the chemical reactions are reversed when an external electrical current is supplied. Students should be able to interpret data for relative reactivity of different metals and evaluate the use of cells. Students do not need to know details of cells and batteries other than those specified." (AT6)

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Cell: two different metals + electrolyte → electricity (th1; key_note) | triple | 4.5.2.1 | OK (C2 imprecise) |
| R2 | Voltage depends on electrodes (reactivity difference) and electrolyte (th1; common_mistake; q1) | triple | 4.5.2.1 | OK; C4 wrong reasoning on temperature |
| R3 | Battery = two or more cells in series → greater voltage; voltages add (th2; common_mistake) | triple | 4.5.2.1 | OK |
| R4 | Non-rechargeable: reactions stop when a reactant is used up; alkaline (th2; key_note) | triple | 4.5.2.1 | IMPRECISE (C7) |
| R5 | Rechargeable: external current reverses the reactions (th2; key_note; q2) | triple | 4.5.2.1 | OK |
| R6 | Interpret reactivity data; evaluate the use of cells (`higher` field) | **triple (not HT)** | 4.5.2.1 — no HT label | ROUTE: carried on TH only; belongs on TF too |
| R7 | Primary/secondary terms; Li-ion, lead-acid, NiMH, zinc-carbon; uses; toxic metals; mAh/Wh capacity (th2–th3; key_note) | off-spec context | "do not need to know details of cells and batteries other than those specified" | OFF-SPEC, not testable |
| R8 | q1, q2 | triple | 4.5.2.1 | OK |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | cell converts chemical energy to electrical energy via redox | OK | Spec: "Cells contain chemicals which react to produce electricity." | 4.5.2.1 |
| C2 | th1 | more reactive metal = negative electrode "(anode)", loses electrons; less reactive = positive "(cathode)", gains electrons; electrons flow negative → positive in the external circuit | IMPRECISE | Science right (in a cell the anode is negative), but pupils have just learned anode = positive in electrolysis (4.4.3). AQA does not ask anode/cathode for cells; use "negative / positive electrode" only. | 4.5.2.1; 4.4.3.1 |
| C3 | th1 | voltage factors: type of metals (reactivity difference), type of electrolyte, concentration | OK | First two are the spec's; concentration is true, off-spec. | 4.5.2.1 |
| C4 | th1 | "TEMPERATURE — affects rate of reaction and therefore voltage" | **WRONG** (reasoning) | A cell's voltage is not set by how fast the reaction goes. Temperature does change voltage slightly, but not "therefore" via rate. Off-spec anyway; delete or say "temperature also has a small effect". | — |
| C5 | th2 | battery = 2+ cells in series; voltages add; 2 × 1.5 V = 3 V | OK | ✓ | 4.5.2.1 |
| C6 | th2 | non-rechargeable = "PRIMARY CELLS"; rechargeable = "SECONDARY CELLS" | OFF-SPEC | Not spec terms; harmless. | 4.5.2.1 |
| C7 | th2; key_note | non-rechargeable: "Chemical reactions are irreversible — the battery is used once" | IMPRECISE | Spec reason: "the chemical reactions stop when one of the reactants has been used up". Lead with that. | 4.5.2.1 |
| C8 | th2 | alkaline examples | OK | Spec's own example. | 4.5.2.1 |
| C9 | th2 | rechargeable: external supply reverses the redox reactions, restoring reactants | OK | ✓ | 4.5.2.1 |
| C10 | th2 | Li-ion, lead-acid, NiMH; degradation over cycles | OK / OFF-SPEC | True; details beyond the spec. | — |
| C11 | th3 | toxic metals "(lead, cadmium, lithium, nickel)" | IMPRECISE | Lithium is a fire/reactivity hazard more than a toxic heavy metal. Off-spec; trim to "lead, cadmium, nickel". | — |
| C12 | th3 | "Capacity measured in mAh or Wh. Higher capacity = more energy stored" | IMPRECISE | mAh measures charge, not energy (Wh is energy). Off-spec; drop. | — |
| C13 | th3 | cell vs battery: battery higher voltage | OK | ✓ | 4.5.2.1 |
| C14 | `higher` (TH only) | voltage vs reactivity difference; evaluate batteries (incl. fuel cells) with data | ROUTE | Not HT in the spec — evaluating cells and interpreting reactivity data is for TF too. Fuel cells are 4.5.2.2's lesson. | 4.5.2.1 |
| C15 | common_mistake | a single cell is not a battery; series raises voltage; bigger reactivity difference → bigger voltage | OK | ✓ (everyday "AA battery" is a cell — worth saying) | 4.5.2.1 |
| C16 | key_note | "Li-ion most common rechargeable" | OFF-SPEC | Not examinable. | 4.5.2.1 |
| C17 | q1 stem / key | "How does changing to more reactive metals affect the voltage?" / "Greater difference in reactivity → greater voltage" | IMPRECISE | Key is the right science, but the stem asks about "more reactive metals", which the key does not directly answer (two more-reactive metals can have a smaller difference). Usable: the key is the only true statement. | 4.5.2.1 |
| C18 | q1 opt1 / wx1 | "more reactive metals always reduces voltage" / "…key factor is the DIFFERENCE" | OK | Aligned ✓ | — |
| C19 | q1 opt2 / wx2 | "no effect — only electrolyte concentration" / "Reactivity difference is a key factor" | OK | Aligned ✓ | — |
| C20 | q1 opt3 / wx3 | "same reactivity gives highest voltage" / "no potential difference — zero" | OK | Aligned ✓ | — |
| C21 | q2 key | redox reactions reversed by external supply | OK | Spec wording. | 4.5.2.1 |
| C22 | q2 opt1–3 / wx1–3 | new chemicals / heat stored / resets with no change | OK | All aligned ✓ | — |
| C23 | matching (to be replaced) | four pairs | OK | ✓ (primary/secondary off-spec) | — |

Count: **1 WRONG** (C4, theory reasoning — re-cuttable). IMPRECISE: C2, C7, C11, C12, C17. ROUTE: C14. OFF-SPEC context: C6, C10, C16. No calculations beyond 1.5 + 1.5 = 3 ✓. No CFIFA in this file.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | correct key; stem slightly loose (C17) | Usable on TF TH. |
| q2 | correct | Usable on TF TH. |

## 5. Calculations
- Battery voltage = sum of cell voltages in series (and cell voltage from a reactivity/voltage data table). Base-triple, one step, no chain, nothing to convert.

## 6. Verdict
SOURCE OK WITH FLAGS. Both quiz items correct and usable on both routes. One wrong causal claim in theory (temperature → rate → voltage); "anode/cathode" for cell electrodes invites confusion with electrolysis; the "evaluate cells / interpret reactivity data" point is spec content for TF too but sits in the TH-only `higher` field; the spec's data-interpretation skill has no item. Much battery detail is beyond what the spec says pupils need. Nothing for Mide.
