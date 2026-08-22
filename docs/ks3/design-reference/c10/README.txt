MrBadmusAI — KS3 Chemistry
C10: The Earth and its atmosphere — SEVEN OF SEVEN LESSONS. COMPLETE UNIT.

Authored:

  c10-01-inside-the-earth.dc.html                    Inside the Earth                     MODEL
  c10-02-three-ways-to-make-a-rock.dc.html           Three ways to make a rock            CLASSIFY
  c10-03-the-rock-cycle.dc.html                      The rock cycle                       PROCESS
  c10-04-a-planet-with-limits.dc.html                A planet with limits                 SYSTEM
  c10-05-whats-in-the-air.dc.html                    What's in the air                    MODEL
  c10-06-carbon-dioxide-humans-and-climate.dc.html   Carbon dioxide, humans and climate   SYSTEM
  c10-07-the-carbon-cycle.dc.html                    The carbon cycle                     PROCESS

The numbering gap at 04 is closed: c10-04 was authored 21 Aug 2026 into the
slot structure.py had reserved for it, so nothing was renumbered. The forward
link in c10-03 and the back link in c10-05 now resolve.

NOTES-C10.md covers c10-04 only. The other six lessons were packaged without
notes and cannot have them reconstructed reliably after the fact — the
instrument payloads and science flags need to come from whoever authored them.
That gap is unchanged by this pass and is stated at the top of the notes file.

Open any .dc.html file directly in a browser. No connection needed. Keep the
folder structure intact: each lesson loads support.js and the design-system
stylesheets and fonts from _ds/ alongside it.

Standing conventions, same as the rest of the build:
  - Progress rail ticks only on completed activities, right or wrong.
  - One KEY FACT box per lesson. Amber is reserved for misconceptions.
  - Only the mastery ladder marks correctness; benches give a verdict in words.
  - No year or half-term appears anywhere in a lesson page.

Packaged 21 Aug 2026, repackaged the same day with c10-04 — this folder is the
current build.
Every .dc.html here is byte-identical to the working copy it was authored from,
and the _ds/ assets are the same files those working copies load.

Checked before packaging: no U+2192, U+2713, U+2715 or U+2126 anywhere in a
lesson, and no Unicode subscript or superscript digits — formulae use real
<sub> elements in markup and plain digits inside instrument payloads.
Changed in this pass: c10-04 added, README updated, NOTES-C10.md started.
c10-04 carries a Law 7 vocabulary block, so the unit passes gate E with no
named escapes.
