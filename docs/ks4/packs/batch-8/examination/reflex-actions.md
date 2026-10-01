# Examination — Reflex Actions (reflex-actions) — AQA 8464 4.5.2 / 8461 4.5.2.1
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-8/04-checked-science-source/biology-4.5.2-reflex-actions.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Trilogy v1.1) §4.5.2, §6.5.4.3.2; `AQA-8461-spec.txt` (Biology v1.0) §4.5.2.1, §4.5.2.2; `AQA-8463-spec.txt` §4.5.6.3.2. Route audit row `reflex-actions`. No equation sheet applies.

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n, which explains option index n (credited answer = index 0). The file's "4.5.2" is the true 8464 ref; the 8461 ref is 4.5.2.1. No `higher` field and no route copies.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.5.2** | The human nervous system | base |
| 8461 | **4.5.2.1** | Structure and function | base |
| Supporting | 8461 4.5.2.2 The brain (cerebral cortex, cerebellum, medulla) | | (biology only) — q3 distractors only |

Spec statements (verbatim, 8464 4.5.2 = 8461 4.5.2.1): "Students should be able to explain how the various structures in a reflex arc – including the sensory neurone, synapse, relay neurone and motor neurone – relate to their function. Students should understand why reflex actions are important. Reflex actions are automatic and rapid; they do not involve the conscious part of the brain." Also: "stimulus → receptor → coordinator → effector → response".

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Reflex = automatic, rapid, no conscious thought (theory 1; key_note) | base | 4.5.2 / 4.5.2.1 | all four | OK |
| R2 | Reflexes are protective / why important (theory 1, 3) | base | 4.5.2 / 4.5.2.1 | all four | OK |
| R3 | Examples (theory 1) | base (context) | — | all four | OK; see C4 |
| R4 | Reflex arc: stimulus → receptor → sensory → relay → motor → effector → response (theory 2; key_note; matching) | base | 4.5.2 / 4.5.2.1 | all four | OK but **synapses missing** — GAP (F1) |
| R5 | Brain aware after the response (theory 2; common_mistake; q2) | base | 4.5.2 / 4.5.2.1 | all four | OK |
| R6 | Reflex vs voluntary pathway; why faster (theory 3; q1; q2) | base | 4.5.2 / 4.5.2.1 | all four | OK, numbers IMPRECISE (C14) |
| R7 | Processed in the spinal cord (theory 2; common_mistake; q3) | base | 4.5.2 / 4.5.2.1 | all four | IMPRECISE as a general rule (F2) |
| R8 | Cerebral cortex, cerebellum, medulla named (theory 3; q3 distractors) | triple vocabulary | 8461 4.5.2.2 (biology only) | all four | acceptable as distractors (C26) |
| — | `higher`, RP, equations | none | — | — | correct: no HT content in 4.5.2 |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | reflex = rapid, automatic, no conscious thought | OK | Spec wording. | 4.5.2 |
| C2 | theory 1 | protective; respond before conscious brain processes it | OK | The "why important" point. | 4.5.2 |
| C3 | theory 1 | automatic, rapid, involuntary, stereotyped | OK | — | — |
| C4 | theory 1 | examples: hand withdrawal, knee-jerk, pupil reflex, sneeze, cough, blink, grasp | OK | All are reflexes. But pupil, blink, sneeze and cough are processed in the brainstem (an unconscious part of the brain), not the spinal cord: see C7. | — |
| C5 | theory 2 | reflex arc is a specific nerve pathway | OK | — | 4.5.2 |
| C6 | theory 2 steps 1–7 | stimulus, receptor, sensory, relay (spinal cord), motor, effector, response | OK but GAP | The spec names the **synapse** as a reflex-arc structure; the file never mentions synapses in the arc (sensory→relay and relay→motor). | 4.5.2 (F1) |
| C7 | theory 2 | "Crucially, it passes through the SPINAL CORD rather than up to the conscious brain" | IMPRECISE | True for spinal reflexes (withdrawal, knee-jerk). Cranial reflexes (pupil, blink) pass through the unconscious brain. Spec: "they do not involve the conscious part of the brain." Re-cut: "passes through the spinal cord or an unconscious part of the brain — never the conscious part." | 4.5.2 (F2) |
| C8 | theory 2 | relay neurone also sends a signal up to the brain; brain aware after | OK | GCSE-level simplification; correct in effect. | — |
| C9 | theory 2 | effector: muscle contracts or gland secretes | OK | — | 4.5.2 |
| C10 | theory 3 | voluntary path goes up to brain and back down | OK | — | — |
| C11 | theory 3 | reflex path: receptor → sensory → spinal cord (relay) → motor → effector | OK | — | 4.5.2 |
| C12 | theory 3 | bypasses conscious brain (cerebral cortex) | OK | "Cerebral cortex" is biology-only vocabulary (8461 4.5.2.2); fine as a gloss. | 8461 4.5.2.2 |
| C13 | theory 3 | voluntary 0.2–0.3 s; reflex 0.04–0.1 s | OK | Reasonable. Note AQA physics gives typical reaction times as 0.2–0.9 s (8464 6.5.4.3.2 / 8463 4.5.6.3.2); 0.2–0.3 s is the simple lab stimulus. | — |
| C14 | theory 3 | "This 3–5× speed advantage" | IMPRECISE | The file's own ranges give about 2–7×. Say "several times faster". | — |
| C15 | theory 3 | prevents injury: moves before the pain is consciously felt | OK | — | — |
| C16 | common_mistake | "processed in the SPINAL CORD … the brain is only aware of them afterwards" | IMPRECISE | As C7: true of spinal reflexes. The examined fact is "does not involve the conscious part of the brain". | 4.5.2 |
| C17 | key_note | arc sequence; faster because it bypasses the conscious brain; involuntary | OK | Add synapses (F1). | 4.5.2 |
| C18 | q1 key | bypass the conscious brain; spinal cord; shorter pathway | OK | Matches the mark scheme. | 4.5.2 |
| C19 | q1 opt 1 / wx1 | conduction speed depends on myelination, not reflex vs voluntary | OK | Aligned. | — |
| C20 | q1 opt 2 / wx2 | "Synaptic delay is similar in both — the key saving is the elimination of the brain processing step entirely." | IMPRECISE | Each synapse delays about the same, but a reflex arc has **fewer synapses**, so less total synaptic delay. AQA mark schemes credit "fewer synapses" as a reason. The wx could lead a pupil to reject a creditworthy point. Aligned. | (F3) |
| C21 | q1 opt 3 / wx3 | brain does not prioritise reflexes; it is not involved in initiating them | OK | Aligned. | — |
| C22 | q2 key | arc bypasses the conscious brain; withdrawal before pain processed | OK | — | 4.5.2 |
| C23 | q2 wx1 | pain receptors do work; pain felt a fraction of a second after | OK | Aligned. | — |
| C24 | q2 wx2 | brain does not speed up for emergencies | OK | Aligned. | — |
| C25 | q2 wx3 | motor and sensory have similar speeds; pathway is the key | OK | Aligned. | — |
| C26 | q3 key | spinal cord; relay neurones connect sensory and motor there | OK | The stem says "spinal reflex arc", which gives the answer away (minor). Distractors use biology-only brain regions (8461 4.5.2.2), but the key is base and answerable on all routes. | 4.5.2 |
| C27 | q3 wx1 | cerebral cortex is the conscious brain; bypassed | OK | Aligned. | 8461 4.5.2.2 |
| C28 | q3 wx2 | cerebellum: balance and coordination | OK | Aligned. | 8461 4.5.2.2 |
| C29 | q3 wx3 | medulla controls heart rate; withdrawal reflexes are in the spinal cord | OK | Aligned. | 8461 4.5.2.2 |

Count: **0 WRONG**; **IMPRECISE**: C7, C14, C16, C20; **GAP**: synapse in the arc (C6). wrong_explanations: all 9 keys aligned to their own option index. No calculations.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | wx2 understates synapse number | Usable on all four routes, provided theory teaches "fewer synapses" as a creditworthy reason, and the wx is read as "each synapse takes about as long" (F3). |
| q2 | — | Usable on all four routes. |
| q3 | stem gives the key away; distractors use biology-only names | Usable on all four routes (weak item; Recall rung only). |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: "the brain controls the reflex"; omitting the relay neurone or the synapses from the arc; "the receptor is the stimulus"; effector given as "the nerve"; "reflexes are faster because the neurones are faster"; "you can choose to stop a reflex".

**Command words**: Describe (the path of a reflex), Explain (why reflexes are important; why they are fast; how a structure relates to its function), Complete the diagram / Label, Suggest (a reflex's survival value).

**Typical questions** ⚑ examiner-drafted
- *Describe the pathway of a reflex action when a finger touches a hot object. [4]* — receptor detects heat (1); impulse along sensory neurone to the spinal cord (1); across synapse to relay neurone, then synapse to motor neurone (1); motor neurone to effector/muscle, which contracts (1).
- *Explain why reflex actions are important. [2]* — rapid/automatic (1); protect the body from harm, e.g. prevent burning (1).
- *Explain why a reflex action is faster than a voluntary response. [2]* — does not involve the conscious part of the brain (1); shorter pathway / fewer synapses (1).

**Required practical**: none (reaction-time RP lives in `reaction-time`).

## 6. Verdict
SOURCE OK WITH FLAGS. The arc and the reasons are correct, and all three quiz items are usable on all routes with aligned explanations. The spec names the synapse as a reflex-arc structure but the file leaves it out (GAP; quoted in the source). "Always through the spinal cord" overgeneralises. q1 wx2 could undermine the creditworthy "fewer synapses". Nothing for Mide.
