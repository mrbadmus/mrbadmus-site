# cancer

Sources: AQA 8464 4.2.2.7 (CF, CH) and 8461 4.2.2.7 (TF, TH), word for word the same, no HT-only or "(biology only)" lines. Rainford SOW Unit 3 "Cancer" (causes of cancer, e.g. viruses, smoking, alcohol, carcinogens and ionising radiation; benign vs malignant; how cancer spreads to form a secondary tumour; key words benign, malignant, metastasis) and Unit 2 "lifestyle and cancer" (what cancer is, risk factors, the two types of tumour). No required practical, no equation.

Old page: Design batch-6 (`ks4-biology-4.2.2.7-cancer.dc.html`), family Model, routes CF CH TF TH. Practice set = hard-coded `bankSrc` (5 items).

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| Describe cancer as the result of changes in cells that lead to uncontrolled growth and division | Card 'What cancer is'; Key fact; Rung 1 Q1; practice Q3 | CF CH TF TH | ✓ |
| Benign tumours are growths of abnormal cells which are contained in one area, usually within a membrane. They do not invade other parts of the body | Card 'Benign and malignant tumours' (tumourFig, drawn at its last step); reveal 'Comparing the two'; Rung 3 chain 2; Rung 4; practice Q1, Q2 | CF CH TF TH | ✓ |
| Malignant tumour cells are cancers. They invade neighbouring tissues and spread to different parts of the body in the blood where they form secondary tumours | Card 'Benign and malignant tumours'; reveal; Rung 1 Q2; Rung 2 Q2; Rung 3 chain 1; practice Q4 | CF CH TF TH | ✓ |
| Scientists have identified lifestyle risk factors for various types of cancer. There are also genetic risk factors for some cancers | Card 'Risk factors for cancer'; Rung 2 Q1; practice Q5 | CF CH TF TH | ✓ |

**Gaps and mismatches.**
- None in the spec lines. Carcinogens and ionising radiation as risk factors are 4.2.2.6 (Health lesson); link.
- Rainford "metastasis": not a spec word; the page uses it once in a quiz option. Fine as a gloss, not to be learned.

**Practice set source.** Hard-coded `bankSrc`, five items, same on all routes. Fixes are `logic_edits`.

**Audit of the ladder and practice set (faults found).**
- Quiz "key difference between a benign and a malignant tumour": credited longest (+26); reply "Malignant tumours typically grow FASTER" — not spec, capitals; "chemotherapy … surgery" reply off spec.
- Quiz "How does UV radiation cause skin cancer?": off spec (mutation mechanism; physics "photons" in a reply). Distractor "reduces the immune system's ability to detect … abnormal cells" — the reply concedes it is partly true, so it is not definitely wrong. Replace the item.
- Quiz "What is cancer the result of?": credited longest (+23).
- Quiz "genetic risk factor": credited longest (+22); otherwise ok.
- Rung 1 "State what cancer is the result of": credited longest (+17). Rung 2 "tumour in the liver made of lung cells": credited longest (+21).
- Hook "A wart on a hand": a wart is a benign growth caused by a virus (HPV); calling it a benign tumour is common but contested. Keep only if the hook does not assert it as a tumour; otherwise choose a mole or a lipoma.
- Rung 3 herring "Benign tumours spread more slowly." ✓ (definitely wrong: they do not spread).

**Old subtopic data.** spec "4.2.4.1" on all routes: wrong (want 4.2.2.7). CH and TH "higher" block (metastasise via blood or lymph, asbestos/mesothelioma, BRCA1/2, chemotherapy and radiotherapy): 4.2 has no HT content, and most of it is beyond the spec.

**Unsure (left out until checked).**
- Named examples (UV and skin cancer; alcohol and liver cancer; inherited genes and some breast cancers): true, not spec wording. Keep as examples.
- "A benign tumour can cause problems if it presses on an organ": true, not spec. Keep one line.

**Removed or moved.**
- Design two-tumour stepper and risk taps, Think again: off the page; tumourFig drawn at its last step.
- Wart hook: gone (a wart's status as a benign tumour is contested).
- Practice 'How does UV radiation cause skin cancer?' replaced by a benign/malignant identification item (new id; old id -> null).
- Rung 3 herring 'Benign tumours are caused by a virus' (true of some): replaced.
- 'Metastasis' kept as one Dive deeper gloss; chemotherapy, radiotherapy, BRCA, mesothelioma (old 'higher' data block) gone.
- Examiner/blind (18 Nov): Rung 2 (ii) credited 'Lung tumour cells spread, forming a secondary tumour'; practice Q1 credited 'Benign tumours stay in one area; malignant tumours spread.'; tumour figure 'secondary tumour' label inside the drawing.
