# plant-tissues

Sources: AQA 8464 4.2.3.1 (CF, CH) and 8461 4.2.3.1 (TF, TH), word for word the same, no HT-only or "(biology only)" lines. Skills: AT 7 observation and drawing of a transverse section of a leaf. Rainford SOW Unit 2 "Plant organs and Tissues" (label the main plant organs and describe their functions; identify the tissues in a leaf and their functions; relate each tissue's structure to its function in photosynthesis; microscopes to see phloem and xylem; key words spongy mesophyll, palisade, diffusion). No required practical, no equation.

Old page: Design batch-5 (`ks4-biology-4.2.3.1-plant-tissues.dc.html`), family Model, routes CF CH TF TH. Practice set = hard-coded `bankSrc` (4 items).

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| Explain how the structures of plant tissues are related to their functions | Reveal 'How each leaf tissue suits its job'; Rung 2; Rung 3; Rung 4; practice Q3, Q5 | CF CH TF TH | ✓ |
| Plant tissues include epidermal tissues, palisade mesophyll, spongy mesophyll, xylem and phloem, meristem tissue found at the growing tips of shoots and roots | Card 'The leaf is a plant organ'; reveal; card 'Meristem' (plantFig); Rung 1; practice Q1, Q2, Q4 | CF CH TF TH | ✓ |
| The leaf is a plant organ. Knowledge limited to epidermis, palisade and spongy mesophyll, xylem and phloem, and guard cells surrounding stomata | Card 'The leaf is a plant organ' (fig:leaf-cross-section); reveal (all seven parts); Key fact | CF CH TF TH | ✓ |
| (skills) AT 7 observe and draw a leaf transverse section | Left out (skills opportunity) | — | left out |

**Gaps and mismatches.**
- None in the content lines.
- Xylem and phloem structure is taught here AND in Transpiration (xylem) and Translocation (phloem, side-by-side comparison). The spec's adaptation statement for xylem and phloem is 4.2.3.2. Proposal: here = where they are in the leaf and one line each; the structure-to-function detail lives in Translocation's comparison table. Avoid three copies.
- "Waxy cuticle" (epidermis): not in the spec's leaf list, but standard; keep as one detail of the epidermis.
- Meristem "cells can differentiate into any type of plant cell, throughout the life of the plant" is 4.1.1.4/4.1.2.3 wording; fine as a link.

**Practice set source.** Hard-coded `bankSrc`, four items, same on all routes. Fixes are `logic_edits`.

**Audit of the ladder and practice set (faults found).**
- Quiz "What is transported in xylem?": credited longest (+7), dash tail; replies in capitals ("PHLOEM").
- Quiz "Why are xylem cells dead?": off the spec (AQA: "hollow tubes strengthened by lignin"; cell death and development are not required). Credited +42 with dash tail; replies "programmed developmental process". Replace.
- Quiz "What is the role of stomata in leaves?": credited +51 with dash tail; reply on cuticle production. Fix lengths.
- Quiz "palisade … near the upper surface": credited longest (+14).
- Rung 1 "State where meristem tissue is found": credited longest (+17). Rung 2 "upper epidermis transparent": credited longest (+16). Rung 2 "petroleum jelly … photosynthesis": credited longest (+28).
- Rung 4 reject "Stomata take in water." ✓; "Xylem carries sugar to the leaf." ✓.

**Old subtopic data.** spec "4.2.5" on all routes: wrong (want 4.2.3.1). CH and TH "higher" block (cohesion-tension theory, potometer, active loading of sucrose with ATP from companion cells): A level, and 4.2 has no HT content.

**Unsure (left out until checked).**
- "Xylem: hollow tubes of dead cells": true; the spec says only "hollow tubes strengthened by lignin". Keep "dead" as a gloss, do not test it.
- "Phloem: living cells": true; "detailed structure of phloem tissue … is not required". Keep to "tubes of elongated cells".

**Removed or moved.**
- Design leaf bench (layer by layer), Think again: off the page; leafFig not used (it labels only one layer); new fig:leaf-cross-section requested. plantFig kept, its two labels moved inside the drawing.
- Practice 'Why are xylem cells dead?' replaced by 'What strengthens the walls of the xylem tubes?' (new id; old id -> null).
- Rung 3 chain 2 rebuilt: it tested 'xylem cells are dead' and two links could swap.
- Xylem and phloem detail moved to Translocation (comparison) and Transpiration (stream); here one line each in the reveal.
- Old subtopic data CH/TH 'higher' block (cohesion-tension, potometer, active loading with ATP): A level; not Higher content.
- Examiner/blind (18 Nov): no change.
