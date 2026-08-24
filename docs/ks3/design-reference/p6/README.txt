KS3 P6 — Waves and sound
========================================

Each lesson is one standalone HTML file. Open any of them directly in a
browser; nothing needs to be installed and nothing is fetched from the
network. The design-system files each page needs sit in the _ds folder
beside them, and support.js is the runtime.

Lessons in slot order:

p6-01-waves-on-water.dc.html                     Waves on water: what a wave is
p6-02-transverse-waves-and-superposition.dc.html Transverse waves, reflection and superposition
p6-03-how-sound-is-made.dc.html                  How sound is made
p6-04-sound-is-longitudinal.dc.html              Sound is longitudinal
p6-05-frequency-pitch-and-loudness.dc.html       Frequency, pitch and loudness
p6-06-sound-needs-a-medium.dc.html               Sound needs a medium
p6-07-echoes-reflection-and-absorption.dc.html   Echoes, reflection and absorption
p6-08-hearing-and-auditory-range.dc.html         Hearing and auditory range
p6-09-ultrasound-at-work.dc.html                 Ultrasound at work

NOTES-P6-P7.md carries the delivery record for both units: statutory
ownership, the formula-block rulings, every bench's state space, the
pre-allocated misconception ids, the review flags and the component
families registered for the coverage gate.

Draft — not yet science-reviewed. Every page says so on its face until
that flag is cleared.


Changed 23 Aug 2026
-------------------
The bench caption on the pages listed below was a template hole inside an SVG
<text> element, which renders nothing — the caption was invisible on every
state. Each one is now an absolutely-positioned HTML <span> over the diagram,
the same technique those pages already use for their other live labels. No
caption wording, diagram geometry or bench logic changed.
  p6-06-sound-needs-a-medium.dc.html         the material caption
  p6-07-echoes-reflection-and-absorption.dc.html  the surface caption
  p6-09-ultrasound-at-work.dc.html            the material caption

Packaged 21 Aug 2026, repackaged 23 Aug 2026 with the caption fix above.

Changed 23 Aug 2026 — CFIFA and the structural conventions
----------------------------------------------------------
p6-02, p6-05, p6-06 and p6-07 rebuilt on the five-step block.

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
