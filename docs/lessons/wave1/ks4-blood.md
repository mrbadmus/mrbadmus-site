# blood

Sources: AQA 8464 4.2.2.3 (CF, CH) and 8461 4.2.2.3 (TF, TH), word for word the same, no HT-only or "(biology only)" lines. Skills: AT 7 observing and drawing blood cells under a microscope; WS 1.5 evaluate risks related to the use of blood products; WS 3.5. Rainford SOW Unit 2 "The Blood" (four main components; how each is adapted; identify pictures of the blood cells; key words plasma, platelets, white blood cells). No required practical, no equation.

Old page: Design batch-4 (`ks4-biology-4.2.2.3-blood.dc.html`), family Classify, routes CF CH TF TH. Practice set = hard-coded `bankSrc` (5 items).

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| Blood is a tissue consisting of plasma, in which the red blood cells, white blood cells and platelets are suspended | Card 'Blood is a tissue'; Key fact | CF CH TF TH | ✓ |
| Know the functions of each of these blood components | Reveal 'The four components'; cards 'Red blood cells', 'White blood cells'; Rung 1; Rung 4; practice Q3, Q4, Q5 | CF CH TF TH | ✓ |
| Recognise different types of blood cells in a photograph or diagram, and explain how they are adapted to their functions | Card 'Recognising blood cells' (smearFig) and reveal 'The cells in the drawing'; card 'Red blood cells' (rbcFig); Rung 2; Rung 3; practice Q1 | CF CH TF TH | ✓ |
| (skills) AT 7 observe and draw blood cells; WS 1.5 risks of blood products | Left out (skills opportunity); Dive deeper 'Seeing blood cells yourself' names the method | — | left out |

**Gaps and mismatches.**
- None in the content lines. AT 7 and WS 1.5 are skills opportunities; leave them out of the lesson unless a ruling says otherwise.
- White blood cells' three defences (phagocytosis, antibodies, antitoxins) are 4.3.1.6 content (Infection and response). Fine as "function", but the detail belongs there; keep to one line each.

**Practice set source.** Hard-coded `bankSrc`, five items, same on all routes. Fixes are `logic_edits`.

**Audit of the ladder and practice set (faults found).**
- Quiz "Why do red blood cells have no nucleus?": credited longest (+13), dash tail. Distractor "So they can squeeze through capillaries more easily" is not definitely wrong (the reply itself concedes flexibility helps). Replace the distractor.
- Same idea in Rung 3 red herring "They have no nucleus so they can squeeze through capillaries." with why "The examined reason is more room for haemoglobin" — a herring must be definitely wrong. Replace.
- Quiz "very few lymphocytes": credited longest (+34), dash tails; "severe anaemia" (not spec).
- Quiz "role of platelets": credited longest (+47), "fibrin mesh" (beyond the spec), capitals in replies.
- Quiz "Which substance does plasma NOT transport?": credited "Oxygen — …" (+14). A little oxygen does dissolve in plasma, so "not transport" is arguable; reply "most CO₂ travels as bicarbonate ions dissolved in plasma" is A level. Replace the item.
- Quiz "What do antitoxins do?": credited longest (+10).
- Rung 1 "Identify … lobed nucleus": credited longest (+14).
- Rung 4 reject "Platelets are a type of white blood cell." ✓.

**Old subtopic data.** spec "4.2.3.2" on all routes: wrong (want 4.2.2.3). No HT block.

**Unsure (left out until checked).**
- "Phagocyte" and "lymphocyte" names on the smear: not in 4.2.2.3; 4.3.1.6 says white blood cells by phagocytosis, antibody production, antitoxin production, without naming cell types. Common in AQA mark schemes; keep as labels, or say "a white blood cell that engulfs pathogens".
- Plasma list "glucose, amino acids, carbon dioxide, urea, hormones, antibodies": standard; not spec wording.

**Removed or moved.**
- Design smear bench (name and job), sort, Think again: off the page; smearFig is now explained by the reveal 'The cells in the drawing'.
- 'No nucleus so they can squeeze through capillaries' (practice Q1 distractor and Rung 3 herring): not definitely wrong; replaced.
- Practice 'Which substance does plasma NOT transport?' replaced by 'What is plasma?' (new id; old id -> null).
- 'Severe anaemia', 'fibrin mesh', 'bicarbonate ions': gone (beyond the spec).
- Examiner/blind (18 Nov): Rung 3 (i) red blood cells: no nucleus → more room for haemoglobin → more oxygen carried. Rung 3 (ii) white blood cells: a phagocyte reaches a pathogen → engulfs it → digests it. Both ONE order; prompts unchanged.
- Practice Q2 options use 'They'/'Their' for a patient; credited 'They make fewer antibodies against pathogens'.
