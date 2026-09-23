# The examiner brief — what an Opus examiner checks before a row lands

Every changed question and every new figure goes through this. The pass is
load-bearing: it is the only thing standing between a repaired stem and a
diagram that quietly makes a distractor correct.

The examiner is checking Mide's own gate — **science accuracy, and whether
AQA would credit the answer**. Nothing else in this run may overrule it.

## For each CHANGED QUESTION

1. **Is the science still right?** Unchanged from before the edit — same
   physics, same chemistry, same biology. A repair that also "improves" the
   science is out of scope and must be flagged, not waved through.
2. **Is the difficulty the same?** A stem that stops describing and starts
   showing is usually EASIER to read. That is intended. But the demand must
   not drop: if the old stem made the pupil build the picture and the new one
   hands it over, check the question still asks for the same cognitive step.
   Where showing the picture removes the whole difficulty, say so — that row
   may need a harder ask to stay at its band.
3. **Does the stem now POINT at the figure rather than describe it?**
   ✅ "Which component is shown in the diagram?"
   ❌ "Which component is drawn as a rectangle with an arrow through it?"
   A stem that shows the figure AND still describes it in words has not been
   repaired; it has been padded.
4. **Band and tier unchanged?** easier/standard/harder as before; at KS4 the
   tier too. Check against the before-snapshot, not against impression.
5. **Is the correct answer still the correct answer, and still at the same
   index?** `correct_index` must be re-derived from the new options, not
   assumed to have survived.

## For each FIGURE — the part that catches the dangerous errors

6. **Does the figure match the stem?** The thing the question asks about must
   actually be in the picture.
7. **Does the figure match the CORRECT ANSWER?** Draw a variable resistor,
   mark "fixed resistor" correct, and the question is now wrong in a way no
   structural gate can see.
8. **Does the figure make any DISTRACTOR true?** The most likely new defect
   in this whole run. If the drawing accidentally shows two lamps in parallel
   when the stem says series, a distractor becomes defensible and the
   question has two right answers.
9. **AQA symbol accuracy.** Every circuit symbol must match the AQA GCSE
   physics symbol sheet exactly. Specifically check the pairs pupils confuse
   and these stems turn on:
     - plain rectangle = FIXED RESISTOR; rectangle with a line through it = FUSE
     - variable resistor, thermistor and LDR must be mutually distinguishable
     - cell (one long + one short line) vs battery (repeated cells)
     - ammeter in SERIES, voltmeter in PARALLEL across the component
     - diode/LED orientation — the triangle points the way conventional
       current may pass
10. **Graphs carry labelled axes WITH UNITS** ("time / s", "distance / m").
    A graph without units is a defect even if the shape is right. Check the
    shape too: a distance–time graph that curves the wrong way teaches the
    wrong thing.
11. **Alt text names what is SHOWN and never gives away the answer.**
    For a symbol-naming question the alt describes GEOMETRY —
    "a rectangle with an arrow drawn diagonally across it" — never the
    identification, "variable resistor". Describing geometry is not giving
    the answer away: it is what a sighted pupil already sees, and a screen
    reader user is entitled to the same.

## Verdicts
- **PASS** — lands as written.
- **PASS WITH FIX** — name the exact change needed; it is applied and re-read.
- **REJECT** — say why. A rejected row stays as it was and is listed in the
  report as deliberately left, with the reason.

## For BORDERLINE rows specifically
The question is not "could a picture be added" but **"does a picture
genuinely belong"**. A convention question that merely uses a visual word
("state what the dots and crosses show") needs no diagram and must be left
alone — the audit's own §1 lists this as the largest source of false
positives. Leaving a borderline row is a legitimate, expected outcome and
must be recorded with its reason, not quietly fixed to look productive.
