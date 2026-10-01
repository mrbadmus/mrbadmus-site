# Examination — The Human Nervous System (nervous-system) — AQA 8464 4.5.2 / 8461 4.5.2.1
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-8/04-checked-science-source/biology-4.5.2-nervous-system.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Trilogy v1.1) §4.5.2, §4.1.1.3, §4.5.3.1; `AQA-8461-spec.txt` (Biology v1.0) §4.5.2.1, §4.5.2.2, §4.1.1.3, §4.5.3.1. Route audit row `nervous-system`. No equation sheet applies.

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n, which explains option index n (credited answer = index 0). The file's "4.5.2" is the true 8464 ref; the 8461 ref is 4.5.2.1. `higher` CF and TF copies are `null`.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.5.2** | The human nervous system | base |
| 8461 | **4.5.2.1** | Structure and function | base |
| Supporting | 8464/8461 4.1.1.3 (nerve cells are specialised); 4.5.3.1 (nervous vs hormonal speed) | | base |

Spec statements (verbatim, 8464 4.5.2 = 8461 4.5.2.1): "Students should be able to explain how the structure of the nervous system is adapted to its functions. The nervous system enables humans to react to their surroundings and to coordinate their behaviour. Information from receptors passes along cells (neurones) as electrical impulses to the central nervous system (CNS). The CNS is the brain and spinal cord. The CNS coordinates the response of effectors which may be muscles contracting or glands secreting hormones. stimulus → receptor → coordinator → effector → response. Students should be able to explain how the various structures in a reflex arc – including the sensory neurone, synapse, relay neurone and motor neurone – relate to their function. … Students should be able to extract and interpret data from graphs, charts and tables, about the functioning of the nervous system. [MS 2c]"

Nothing in 4.5.2 / 4.5.2.1 is "(HT only)". Drugs acting at synapses, myelin, saltatory conduction and SSRIs appear nowhere in 8461 or 8464.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Nervous system detects stimuli, coordinates fast responses (theory 1) | base | 4.5.2 / 4.5.2.1 | all four | OK |
| R2 | CNS = brain + spinal cord; nerves link CNS to body (theory 1; key_note) | base | 4.5.2 / 4.5.2.1 | all four | OK ("PNS" is accepted, not required) |
| R3 | Electrical impulses along neurones; faster than hormones (theory 1) | base | 4.5.2; 4.5.3.1 | all four | OK |
| R4 | Sensory, relay, motor neurones and their direction (theory 2; key_note; q1) | base | 4.5.2 / 4.5.2.1 | all four | OK, one IMPRECISE (C9) |
| R5 | stimulus → receptor → coordinator → effector → response (q1) | base | 4.5.2 / 4.5.2.1 | all four | OK |
| R6 | Effectors: muscles contracting or glands secreting hormones | base | 4.5.2 / 4.5.2.1 | all four | in file as "muscles or glands" — OK |
| R7 | Synapse: gap; chemical crosses by diffusion; binds receptors; new impulse (theory 3; common_mistake; key_note; q2) | base | 4.5.2 / 4.5.2.1 ("synapse" named in the reflex arc) | all four | OK |
| R8 | One-way transmission; neurotransmitter broken down/reabsorbed (theory 3; `higher`; q3) | none — beyond spec | — | all four / CH TH | OFF-SPEC (F2) |
| R9 | Drugs at synapses: stimulants, depressants, SSRIs (theory 4; `higher`) | none — OFF-SPEC | (8461/8464 4.2.2.6 names alcohol only as a lifestyle risk factor) | all four / CH TH | OFF-SPEC (F1) |
| R10 | Myelin sheath; saltatory conduction (theory 2; `higher`) | none — OFF-SPEC | — | all four / CH TH | OFF-SPEC (F1); imprecise (C9) |
| R11 | Interpreting data on nervous-system function | base | 4.5.2 MS 2c | — | not in file — GAP (F4) |
| — | `higher` field | **no higher layer exists** | 4.5.2 has no HT statement | CH TH | ROUTE (F1) |
| — | RP | none here | reaction-time RP is in `reaction-time` | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | detects stimuli and coordinates rapid responses | OK | — | 4.5.2 |
| C2 | theory 1 | CNS = brain and spinal cord | OK | Spec verbatim. | 4.5.2 |
| C3 | theory 1 | PNS = all the nerves connecting CNS to the body | OK | Not a spec term; correct. | — |
| C4 | theory 1 | electrical impulses along neurones, up to 120 m/s | OK | ~120 m/s is the upper end for large myelinated fibres; context only. | — |
| C5 | theory 1 | faster than hormonal communication | OK | — | 4.5.3.1 |
| C6 | theory 2 | sensory: receptor → CNS; long dendron to cell body, then axon | OK | Dendron/axon not required. | 4.5.2 |
| C7 | theory 2 | relay: entirely within CNS, links sensory to motor | OK | — | 4.5.2 |
| C8 | theory 2 | motor: CNS → effectors; axon can be over 1 m | OK | — | 4.5.2 |
| C9 | theory 2 | motor neurone "Covered in a MYELIN SHEATH … speeds up signal conduction" | IMPRECISE / OFF-SPEC | Placed under motor only, so it implies sensory neurones lack myelin; many are myelinated too. Myelin is not on the spec. | — |
| C10 | theory 3 | synapse = junction; tiny gap (synaptic cleft) | OK | — | 4.5.2 |
| C11 | theory 3 | electrical impulses cannot cross; transmission is chemical | OK | The point AQA credits. | 4.5.2 |
| C12 | theory 3 | steps 1–6: impulse arrives; vesicles; neurotransmitter released; diffuses; binds receptors; triggers new impulse | OK | Mark-scheme points: chemical released / diffuses across gap / binds to receptors on next neurone / starts impulse. Vesicles are beyond the spec but correct. | 4.5.2 |
| C13 | theory 3 | step 7 broken down or reabsorbed; one-way only | OK, OFF-SPEC | Correct, not required (F2). | — |
| C14 | theory 4 | stimulants increase neurotransmitter activity (caffeine, nicotine, cocaine, amphetamines) | IMPRECISE, OFF-SPEC | Caffeine works by blocking adenosine receptors. The net effect is more nervous activity, but it is not "more neurotransmitter release". Off-spec (F1). | — |
| C15 | theory 4 | depressants reduce neurotransmitter activity; alcohol slows CNS, increases reaction time | IMPRECISE, OFF-SPEC | Alcohol mainly enhances an inhibitory transmitter. "Slows nervous activity / increases reaction time" is the safe GCSE statement, and the reaction-time part is on spec (8464 6.5.4.3.2 / 8463 4.5.6.3.2). | — |
| C16 | theory 4 | SSRIs block serotonin reabsorption | OK, OFF-SPEC | Correct; not on 8461/8464. | — |
| C17 | `higher` | synapse one-way; drugs; "myelin … saltatory (jumping) transmission" | OFF-SPEC, ROUTE | No HT content in 4.5.2. Saltatory conduction is A-level. | F1 |
| C18 | common_mistake | within neurone electrical; across synapse chemical | OK | Strong, usable on all routes. | 4.5.2 |
| C19 | key_note | CNS/PNS; sensory, relay, motor; synapse electrical → chemical → electrical; one-way | OK | "One-way" off-spec (keep as a phrase only). | — |
| C20 | q1 key | receptor → sensory → relay → motor → effector | OK | — | 4.5.2 |
| C21 | q1 opt 1 / wx1 | motor and sensory swapped | OK | Aligned. | — |
| C22 | q1 opt 2 / wx2 | starts at effector, ends at receptor — reversed | OK | Aligned. | — |
| C23 | q1 opt 3 / wx3 | receptor → CNS → sensory → motor: sensory comes after the receptor | OK | Aligned. | — |
| C24 | q2 key | neurotransmitters released, diffuse, bind receptors | OK | — | 4.5.2 |
| C25 | q2 wx1 | gap is liquid-filled; impulse cannot jump | OK | Aligned. | — |
| C26 | q2 wx2 | neurones never fuse | OK | Aligned. | — |
| C27 | q2 wx3 | "Synaptic transmission takes microseconds — blood flow is far too slow." | IMPRECISE | Synaptic delay is about 0.5–1 ms (a fraction of a millisecond), not "microseconds" in the everyday sense. The argument (blood is far too slow) stands. Aligned. | — |
| C28 | q3 | "Why is synaptic transmission one-directional?" + key | OK science, OFF-SPEC | Correct; not on 8461/8464 (F2). | — |
| C29 | q3 wx1 | an isolated axon can conduct both ways | OK | Correct (A-level detail). Aligned. | — |
| C30 | q3 wx2 | gap width irrelevant to direction | OK | Aligned. | — |
| C31 | q3 wx3 | enzymes break down transmitter to stop prolonged stimulation, not for direction | OK | Aligned. | — |

Count: **0 WRONG**; **IMPRECISE**: C9, C14, C15, C27; **OFF-SPEC**: theory 4 entire, `higher` entire, myelin, q3. wrong_explanations: all 9 keys aligned to their own option index. No calculations.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | — | Usable on all four routes. |
| q2 | wx3 "microseconds" imprecise, not in the key | Usable on all four routes. |
| q3 | one-way transmission is off-spec | **Do not use in the practice bank** (F2). Enrichment at most. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: "electrical signal jumps the synapse"; "nerves carry messages in the blood"; sensory and motor swapped; "the spinal cord is not part of the CNS"; "neurones are joined to each other"; effector given as "a nerve".

**Command words**: Name (CNS parts; neurone types), Describe (path of an impulse; how a synapse passes the signal), Explain (how a structure is adapted to its function), Use the data / Interpret (MS 2c).

**Typical questions** ⚑ examiner-drafted
- *Name the two parts of the central nervous system. [2]* — brain (1); spinal cord (1).
- *Describe how an impulse passes from one neurone to the next. [3]* — chemical released at the end of the neurone (1); diffuses across the gap / synapse (1); binds to receptors on the next neurone / starts an impulse in it (1).
- *Give the function of a motor neurone. [1]* — carries impulses from the CNS to an effector.

**Required practical**: none in this lesson (reaction-time RP lives in `reaction-time`).

## 6. Verdict
SOURCE OK WITH FLAGS. The core (CNS, three neurone types, pathway, chemical synapse) is correct and on spec. q1 and q2 are usable on all routes, and their explanations are aligned. Theory 4 (drugs at synapses) and the entire `higher` field are off-spec, and nothing in 4.5.2 is HT, so the CH/TH `higher` layer should not exist. q3 (synapse direction) is off-spec. Nothing for Mide.
