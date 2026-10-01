# Examination — Thermoregulation (thermoregulation) — AQA 8461 4.5.2.4 (biology only; HT statement)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-8/04-checked-science-source/biology-4.5.1-thermoregulation.md` (the data's "4.5.1" is the homeostasis section it hangs off; the true AQA ref is 8461 4.5.2.4 Control of body temperature).
Spec sources read as text: `AQA-8461-spec.txt` (Biology v1.0) §4.5.1, §4.5.2.4, §4.5.3.7; `AQA-8464-spec.txt` (Trilogy v1.1) §4.5.1 (body temperature listed as a controlled condition only). Route audit `ks4-routes/docs/ks4/route-audit/biology.md` row `thermoregulation` (TF TH, OK; HT layer = explaining how the mechanisms raise or lower body temperature). Biology has no equation sheet. Mark-scheme conventions from examiner knowledge of AQA 8461 papers 2018–2024; not fetched.

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n. TH copy carries `higher`; TF copy `higher` = null; otherwise identical.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8461 | **4.5.2.4** | Control of body temperature | (biology only); last statement (HT only) |
| 8464 / 8461 | 4.5.1 | Homeostasis | base — lists "body temperature" as a controlled condition; receptors, coordination centres, effectors |
| 8464 | — | no thermoregulation mechanism content | — |

Spec statements (verbatim, 8461 4.5.2.4):
- "Body temperature is monitored and controlled by the thermoregulatory centre in the brain. The thermoregulatory centre contains receptors sensitive to the temperature of the blood. The skin contains temperature receptors and sends nervous impulses to the thermoregulatory centre."
- "If the body temperature is too high, blood vessels dilate (vasodilation) and sweat is produced from the sweat glands. Both these mechanisms cause a transfer of energy from the skin to the environment."
- "If the body temperature is too low, blood vessels constrict (vasoconstriction), sweating stops and skeletal muscles contract (shiver)."
- "(HT only) Students should be able to explain how these mechanisms lower or raise body temperature in a given context."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | 37 °C, enzymes (theory 1) | triple page (fact is base 4.5.1) | 4.5.1 | TF TH | OK, imprecise numbers (C3, C4) |
| R2 | Thermoregulatory centre (hypothalamus) with blood-temperature receptors; skin receptors send impulses (theory 2; key_note) | triple | 4.5.2.4 | TF TH | OK |
| R3 | Too hot: vasodilation, sweating; energy transferred from skin to environment (theory 3; common_mistake; q1; q2) | triple | 4.5.2.4 | TF TH | OK |
| R4 | Too cold: vasoconstriction, sweating stops, shivering (theory 4; q2) | triple | 4.5.2.4 | TF TH | OK |
| R5 | Explaining HOW each mechanism changes temperature: more blood near surface → more energy lost; shivering → respiration releases energy; evaporation (theory 3–4 explanations; `higher`; q3) | triple-higher | 4.5.2.4 (HT only) | `higher` TH only ✓; but theory and q3 reach TF | ROUTE (F2) |
| R6 | Hairs / erector pili; adrenaline raising metabolic rate (theory 3–4; matching) | off-spec | — | TF TH | OFF-SPEC (F4) |
| — | RP, equations, FIFA | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | core temperature ≈ 37 °C | OK | — | — |
| C2 | theory 1 | 37 °C is the optimum temperature for human enzymes | OK | Spec: homeostasis "maintains optimal conditions for enzyme action". | 4.5.1 |
| C3 | theory 1 | "above ~40 °C: enzymes denature → … death (hyperthermia)" | IMPRECISE | Above about 40 °C is dangerous (heat stroke); enzyme denaturation becomes significant somewhat higher. Say "enzymes start to denature". | 4.2.2.1 (enzymes) |
| C4 | theory 1 | "below ~34 °C … (hypothermia)" | IMPRECISE (minor) | Hypothermia is defined as below 35 °C. | — |
| C5 | theory 1 | heat from respiration in all cells | OK | — | 4.4.2 |
| C6 | theory 2 | hypothalamus = thermostat | OK | Spec term is "thermoregulatory centre in the brain"; teach both names. Mark schemes accept hypothalamus. | 4.5.2.4 |
| C7 | theory 2 | central receptors monitor blood temperature; skin receptors detect surface temperature | OK | Spec: skin receptors "send nervous impulses to the thermoregulatory centre". | 4.5.2.4 |
| C8 | theory 2 | corrective signals "via the nervous system and hormones" | OK | — | — |
| C9 | theory 3 | sweat (water + salts); evaporation absorbs latent heat from the body | OK | AQA wording: energy transferred from the skin to evaporate sweat. | 4.5.2.4 |
| C10 | theory 3 | vasodilation: arterioles near the skin widen; more blood near surface; more heat lost by radiation and convection; flushed skin | OK | Good — it is arterioles that dilate, not capillaries "moving". | 4.5.2.4 |
| C11 | theory 3, 4 | hairs lie flat / stand up via erector pili; trapped air insulates; goosebumps | OFF-SPEC (true) | Not in 8461 4.5.2.4. Context only (F4). | — |
| C12 | theory 4 | shivering: skeletal muscles contract rapidly; respiration releases heat; up to 5× resting | OK | 5× is the upper end of published values; fine as context. | 4.5.2.4 |
| C13 | theory 4 | vasoconstriction: vessels near skin narrow; less heat lost; pale/blue extremities | OK | — | 4.5.2.4 |
| C14 | theory 4 | reduced sweating | OK | Spec says "sweating stops". | 4.5.2.4 |
| C15 | theory 4 | "ADRENALINE RELEASED: increases metabolic rate → more heat" | OFF-SPEC | True physiologically in part, but on 8461 adrenaline is fight-or-flight and it is thyroxine that "stimulates the basal metabolic rate" (4.5.3.7, HT). Listing adrenaline as a thermoregulatory effector invites a confusion AQA would not credit. Drop (F4). | 4.5.3.7 |
| C16 | `higher` (TH) | mechanisms restated with explanations | OK | Content right and correctly on TH only. | 4.5.2.4 (HT) |
| C17 | `higher` (TH) | "Students should be able to explain these mechanisms in terms of negative feedback." | IMPRECISE | The HT statement is "explain how these mechanisms lower or raise body temperature **in a given context**". Thermoregulation is negative feedback, so not wrong, but the examined skill is the context explanation (F5). | 4.5.2.4 (HT) |
| C18 | common_mistake | dilation = widen = more heat lost = too hot; constriction = narrow = too cold | OK | — | 4.5.2.4 |
| C19 | key_note | summary | OK | Hairs raised: off-spec (F4). | 4.5.2.4 |
| C20 | matching (to be replaced) | 6 pairs | OK | Two hair pairs off-spec. | — |
| C21 | q1 key | evaporating sweat absorbs energy from the body, cooling it | OK | Spec base statement covers it ("transfer of energy from the skin to the environment"). TF TH. | 4.5.2.4 |
| C22 | q1 wx1 ↔ opt 1 (sweat removes hot blood) | sweating doesn't involve blood; cooling is evaporation | OK, aligned | — | — |
| C23 | **q1 wx2 ↔ opt 2 (salt reacts with skin)** | "Salt in sweat helps retain water on the skin surface longer — the cooling mechanism is evaporation of water, not a chemical reaction." | **WRONG** (first clause) | Aligned to option 2, but its opening claim is invented: salt has no role in holding water on the skin to prolong cooling (if anything, dissolved salt slightly slows evaporation). Correct wx2: "Salt doesn't react with the skin — the cooling comes from water in the sweat evaporating, which transfers energy away from the skin." (F1) | — |
| C24 | q1 wx3 ↔ opt 3 (sweating increases blood flow) | vasodilation is the separate blood-flow mechanism | OK, aligned | — | 4.5.2.4 |
| C25 | q2 key | vasodilation: vessels near skin widen, when too hot, more heat lost | OK | TF TH. | 4.5.2.4 |
| C26 | q2 wx1 ↔ opt 1 (narrow, cold) | that's vasoconstriction | OK, aligned | — | 4.5.2.4 |
| C27 | q2 wx2 ↔ opt 2 (widen when cold) | would lose more heat | OK, aligned | — | 4.5.2.4 |
| C28 | q2 wx3 ↔ opt 3 (contract when hot) | contracting = vasoconstriction, cold | OK, aligned | — | 4.5.2.4 |
| C29 | q3 key | shivering: muscle contractions need respiration; heat released as by-product | OK | "Aerobic" is fine (shivering is mostly aerobic). This is the HT explanation → TH (F2). | 4.5.2.4 (HT) |
| C30 | q3 wx1 ↔ opt 1 (more blood to skin) | that's vasodilation, increases loss | OK, aligned | — | 4.5.2.4 |
| C31 | q3 wx2 ↔ opt 2 (electrical energy) | heat from energy released in respiration | OK, aligned | "CHEMICAL energy released in respiration" — acceptable. | — |
| C32 | q3 wx3 ↔ opt 3 (sweat glands release warm fluid) | sweating less when cold | OK, aligned | — | 4.5.2.4 |
| C33 | CFIFA Convert lines | none (no fifas) | n/a | — | — |

Count: **1 WRONG** (C23, q1 wx2). IMPRECISE: C3, C4, C17. OFF-SPEC: C11, C15. ROUTE: R5. All nine keys aligned to their own option index.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | wx2 contains a false claim (F1) | **Do not use as written.** Usable TF TH with wx2 replaced (C23). |
| q2 | — | Usable TF TH. |
| q3 | Explains how shivering raises temperature — the HT statement | TH only (F2). |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "Blood vessels move closer to / further from the skin" — they widen or narrow; they do not move. Mark schemes reject "move".
- "Capillaries dilate" — arterioles supplying the skin capillaries dilate/constrict.
- "Sweat cools you because it is cold" — cooling is from evaporation transferring energy from the skin.
- "Shivering makes friction heat" — muscle contraction needs respiration, which releases energy.
- "Vasoconstriction warms you up" — it reduces energy loss; it does not produce heat.
- "Heat" used where AQA prefers "energy transferred" — accept in context, but model "energy".

**Command words**: Describe, Explain (HT: "in a given context"), Suggest, Name (the thermoregulatory centre).

**Typical questions** ⚑ examiner-drafted
- *Name the part of the brain that monitors body temperature. [1]* — thermoregulatory centre / hypothalamus.
- *Describe two ways the body responds when it is too cold. [2]* — vasoconstriction; shivering; sweating stops.
- (HT) *A runner's body temperature rises during a race. Explain how vasodilation helps to lower it. [3]* — blood vessels (arterioles) supplying skin capillaries dilate (1); more blood flows near the skin surface (1); more energy transferred from the skin to the environment (1).

**Required practical**: none.
**Equations**: none.

## 6. Verdict
SOURCE HAS ERRORS. One frozen explanation is wrong (q1 wx2's salt claim). Otherwise sound and well-aligned with 4.5.2.4. The HT "explain how" layer sits partly in theory and q3, which TF also sees. Two off-spec effectors (hairs; adrenaline) — drop adrenaline, keep hairs as context only.

**For Mide:** nothing.
