MrBadmusAI — KS3 Physics
P4: Forces · P5: Pressure · P6: Waves and sound

STATUS: P4, P5 and P6 all complete. This folder ships P4 only; P5 and P6
ship as their own folders, each with its own README and the same _ds assets.

  P4 (9 slots) — all authored
  p4-01-what-a-force-is.dc.html            What a force is                 MODEL        ✔
  p4-02-drawing-and-adding-forces.dc.html  Drawing and adding forces       MODEL        ✔
  p4-03-balanced-and-unbalanced.dc.html    Balanced and unbalanced         CONTRAST     ✔
  p4-04-what-forces-do-to-motion.dc.html   What forces do to motion        MODEL        ✔
  p4-05-friction.dc.html                   Friction                        PROCESS      ✔
  p4-06-air-and-water-resistance.dc.html   Air and water resistance        SYSTEM       ✔
  p4-07-moments.dc.html                    Moments: the turning effect     QUANTITATIVE ✔
  p4-08-springs-and-hookes-law.dc.html     Springs and Hooke's law         INVESTIGATION✔
  p4-09-non-contact-forces.dc.html         Non-contact forces              CLASSIFY     ✔

  P5 (4 slots) — all authored
  p5-01-pressure-force-over-area.dc.html   Pressure = force ÷ area        QUANTITATIVE ✔
  p5-02-pressure-in-liquids.dc.html        Pressure in liquids            MODEL        ✔
  p5-03-upthrust-floating-and-sinking.dc.html  Upthrust, floating and sinking  MODEL    ✔
  p5-04-atmospheric-pressure.dc.html       Atmospheric pressure           SYSTEM       ✔

  P6 (9 slots) — all authored, shipped in the KS3 P6 lessons folder.

Formula blocks: p4-07 (triangle — P4's only product), p4-08 (beam plus graph),
p5-01 (triangle, force at the apex because the product is force = pressure ×
area), p5-02 and p5-04 (a stack of layers), p5-03 (a beam of two opposed
forces). Only the triangles carry cover buttons. The other seven lessons carry no formula block, because
their statutory content is qualitative and nothing was invented to fill one.

p4-08 carries the group's only risk assessment. It is also the only page in the
group that instructs rather than describes — see NOTES §9 flag 6.

Open any .dc.html file directly in a browser. No connection needed. Keep the
folder structure intact: each lesson loads support.js and the design-system
stylesheets and fonts from _ds/ alongside it.

Read NOTES-P4-P6.md before reviewing. It carries the flags, the misconception
id pre-allocation, and the §10 component-family register.

Standing conventions, unchanged from B1 onwards:
  - Four rail stops per lesson. The misconception block is present on every
    page and is deliberately not a rail stop.
  - One [data-key-fact] block and one .ks3-keynote block per lesson.
  - Only the mastery ladder marks correctness. Benches reveal, never verdict —
    the p4-09 sorter therefore prints the label you chose and the force it
    actually is, side by side, and does not mark you.
  - Amber is reserved for a wrong idea being confronted, and for loss.
  - No year, half-term, slot code or unit code anywhere in student prose.

Physics conventions this unit group holds to:
  - Weight in newtons is mass in kilograms × 10 N/kg, stated where it is used.
  - Formula triangle for products only. Sums, differences and equalities get a
    beam; a part–whole bar counts as a beam.
  - Every readout, worked step and scaffold line carries its unit.
  - FIFA worked examples reveal one step at a time, four steps, one line of
    maths and one sentence per step.
  - No arrow, tick or cross characters anywhere. All are inline SVG.

Packaged 21 Aug 2026, status block corrected 23 Aug 2026.

Changed 23 Aug 2026 — CFIFA and the structural conventions
----------------------------------------------------------
p4-02, p4-03, p4-07 and p4-08 rebuilt on the five-step block.

Worked examples in this unit now run CFIFA: Convert, Formula, Insert,
Fine-tune, Answer, revealed one step at a time, with two worked examples
(one where nothing needs converting, one where a quantity arrives in the
wrong size) and two write-it-out student attempts labelled only Question 1
and Question 2. The block itself is Cfifa.dc.html, sitting beside the
lessons in this folder — one implementation, mounted by every lesson that
needs it.

Every lesson carries four rail stops, one [data-key-fact] block and two
misconception quotes.

The full record is in PHYSICS-AUDIT-2026-08-23.md.
