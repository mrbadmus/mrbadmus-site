MrBadmusAI — KS3 Chemistry
C10: The Earth and its atmosphere — SIX OF SEVEN LESSONS. PARTIAL UNIT.

This folder is not a complete unit. Do not review it as one.

Authored:

  c10-01-inside-the-earth.dc.html                    Inside the Earth                     MODEL
  c10-02-three-ways-to-make-a-rock.dc.html           Three ways to make a rock            CLASSIFY
  c10-03-the-rock-cycle.dc.html                      The rock cycle                       PROCESS
  c10-05-whats-in-the-air.dc.html                    What's in the air                    MODEL
  c10-06-carbon-dioxide-humans-and-climate.dc.html   Carbon dioxide, humans and climate   SYSTEM
  c10-07-the-carbon-cycle.dc.html                    The carbon cycle                     PROCESS

Not yet written:

  c10-04-a-planet-with-limits                        Resources and recycling              SYSTEM

The numbering gap at 04 is deliberate — slot numbers follow structure.py, so
the unwritten lesson keeps its position rather than renumbering the rest.

This folder was packaged after the lessons were authored, and it has no
NOTES-C10.md. Every other unit in the build ships one, and this is the only
gap of its kind. The notes cannot be reconstructed reliably after the fact —
the instrument payloads and the science flags need to come from whoever
authored the lessons.

Open any .dc.html file directly in a browser. No connection needed. Keep the
folder structure intact: each lesson loads support.js and the design-system
stylesheets and fonts from _ds/ alongside it.

Standing conventions, same as the rest of the build:
  - Progress rail ticks only on completed activities, right or wrong.
  - One KEY FACT box per lesson. Amber is reserved for misconceptions.
  - Only the mastery ladder marks correctness; benches give a verdict in words.
  - No year or half-term appears anywhere in a lesson page.

Packaged 21 Aug 2026 — this folder is the current build.
Every .dc.html here is byte-identical to the working copy it was authored from,
and the _ds/ assets are the same files those working copies load.

Checked before packaging: no U+2192, U+2713, U+2715 or U+2126 anywhere in a
lesson, and no Unicode subscript or superscript digits — formulae use real
<sub> elements in markup and plain digits inside instrument payloads.
Changed in this pass: CO2 labels in the c10-05, c10-06 and c10-07 payloads
are plain digits. This unit has no NOTES file — see above.
