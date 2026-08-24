KS3 P7 — Light
========================================

Each lesson is one standalone HTML file. Open any of them directly in a
browser; nothing needs to be installed and nothing is fetched from the
network. The design-system files each page needs sit in the _ds folder
beside them, and support.js is the runtime.

Lessons in slot order:

p7-01-light-travels.dc.html                      Light travels
p7-02-reflection-mirrors-and-scattering.dc.html  Reflection: mirrors and scattering
p7-03-refraction.dc.html                         Refraction
p7-04-lenses-and-images.dc.html                  Lenses and images
p7-05-the-eye-and-the-camera.dc.html             The eye and the camera
p7-06-colour-and-the-spectrum.dc.html            Colour and the spectrum
p7-07-why-things-look-coloured.dc.html           Why things look coloured

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
  p7-02-reflection-mirrors-and-scattering.dc.html  the surface caption
  p7-03-refraction.dc.html                    the material caption
  p7-05-the-eye-and-the-camera.dc.html        the system caption
  p7-06-colour-and-the-spectrum.dc.html       the bench caption
  p7-07-why-things-look-coloured.dc.html      both captions

Packaged 21 Aug 2026, repackaged 23 Aug 2026 with the caption fix above.

Changed 23 Aug 2026 — CFIFA and the structural conventions
----------------------------------------------------------
p7-01 rebuilt on the five-step block. p7-02 keeps a single example and a
single question: its quantities are angles in degrees, so conversion cannot
arise and the C step reads as the no-conversion case.

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
