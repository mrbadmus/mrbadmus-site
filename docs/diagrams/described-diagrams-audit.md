# Described-diagrams audit — MRB-342.2 Part 5

Read-only audit. **No content, code, or generator was changed to produce this
report.** Nothing was built; `build_all.py` was never run.

Date: 23 Sep 2026. Scope: every KS3 and KS4 authored question stem, checked
against Mide's rule below. This report went through **two corrections** after
independent coordinator review — a corpus-completeness gap (§2.1) and a
keyword-net completeness gap (§2.2) — both found by checking the audit's own
claims rather than trusting them, and both are written up here in full
rather than quietly folded in, because a reader who finds the old numbers
elsewhere and doesn't know they were superseded will trust the wrong ones.

---

## 1. The rule, and what this audit did and did not flag

Mide's rule, verbatim: **a question about a diagram must SHOW the diagram,
never describe it in words.** Canonical bad example: *"A rectangle with a
line running through it is drawn in the wire leaving the supply…"* — a
circuit-symbol question whose stem paints the symbol in prose because there
is no picture. The fault generalises to a stem that describes a graph's axes
and trace instead of plotting it, describes apparatus layout where a labelled
diagram belongs, or describes a table/ray diagram/food web/cell drawing in
words the pupil must privately reconstruct before they can even attempt the
question.

**The test applied to every row:** does the pupil have to build a specific
image in their head — a picture the question is really about — because the
question refuses to show it? If yes, it is a fault regardless of subject or
key stage. If the stem merely sets a scene, states a physical situation, or
uses a visual word ("diagram", "arrow", "graph", "drawn", "plotted", "food
web") in a general/definitional/**convention** sense that needs no specific
mental image, it is not.

**Deliberately NOT flagged**, with real examples pulled from this corpus
during triage (the last three were added after coordinator review specifically
because the wider net kept re-finding this exact shape of false positive):

- A physical scenario in words — *"A rabbit eats grass and a fox eats the
  rabbit. Where did the energy in the fox's food enter the food chain?"* —
  is ordinary exam scene-setting, not a described diagram.
- A food chain or sequence written out as plain text — *"A food chain is
  written: lettuce, slug, hedgehog. Which way do the arrows point, and
  why?"* — the text-form chain **is** an acceptable diagram-substitute, not a
  description of one.
- Definitional/notation questions that name a diagram element generically
  without requiring a specific mental picture — *"What does an arrow tell a
  reader that an equals sign would not?"*, *"How is potential difference
  shown as a symbol in an equation?"*
- A described experiment or real-world process the pupil must reason about
  conceptually, with no spatial arrangement to reconstruct.
- **A convention question that only sounds like a picture question.**
  *"State what the length of each arrow on a free body diagram represents."*
  is answered "force magnitude" from knowledge — there is no specific arrow
  being read. *"Describe how a dot-and-cross diagram represents the bonding
  in a hydrogen molecule, H₂"* and *"In a dot-and-cross diagram, state what
  the dots and the crosses are used to show"* both ask the pupil to explain
  the **notation itself**, not to read one instance of it. This is the
  single largest source of false positives once the net is widened (§2.2),
  and it is the one most likely to fool a fast read: the word "diagram" is
  present, a picture is *discussed*, but nothing specific was ever withheld.
- A real chemical/structural notation string used as itself (e.g. a repeat
  unit written `–CH₂–CH₂–`) — the text **is** the structure, in its normal
  written form, not a description of a picture of it.

## 2. The corpus map

Four corpora hold every question stem in the estate. All four were scanned.

| Key stage | Corpus | Where it lives | Shape | Stems found |
|---|---|---|---|---|
| KS3 | Lesson ladder (recall/apply/explain/produce) | `ks3_data/<unit>/lesson_NN_*.py`, `LESSON["ladder"]` — four rungs per lesson, each with a `"q"` field. No `figure` key exists on a rung at all. | one dict per rung | 740 |
| KS3 | Assignment bank | `ks3_data/<unit>/questions_NN_*.py`, `QUESTIONS` list — twelve-or-more MCQs per lesson, each `{"id","band","text","options","figure"}`. `bank_position` **is** the row's index in `QUESTIONS` (no reordering — confirmed by reading `ks3_data/question_bank.py`'s `validate_lesson`, which checks bands sit at positions 0–11 in *authored* order). | one dict per question | 16,946 |
| KS4 | Assignment bank | `ks4_data/questions/<subject>/*.py`, `QUESTIONS` list — `{"id","subtopic_slug","band","tier","triple_only","text","options","correct_index","why"}`. **No `figure` field exists in the KS4 record shape at all.** `bank_position` is computed by `ks4_data.load_pool()` (imported and called directly, not re-implemented): per `subtopic_slug`, the first four of each band come first (positions 0–11), then extras append in authored order. | one dict per question | 16,765 |
| KS4 | Lesson-page quiz | `all_subtopics_<subject>{,_higher,_triple_foundation,_triple_higher}.py`, `<SUBJECT>_SUBTOPICS_ALL[topic][i]["quiz"]` — the "Test yourself" MCQs printed on the topic page itself. No `bank_position`, no `figure` field. Scanned as the **union of all four tier/pathway variant files per subject, deduplicated by exact stem text** — see §2.1. | one dict per quiz item | 800 |

**Total stems scanned: 35,251.**

Not one of the 413 rows the *original* keyword net flagged had a real figure
attached (every `figure` field on a flagged KS3 row was `None`), and the
same holds for every candidate found by the wider net in §2.2 — no `figure`
field exists on any KS4 row, and no KS3 row this audit flagged carried one
either. So this audit never had to adjudicate "does the description match
the shown picture" — every confirmed and borderline row is a stem with
literally nothing to look at.

### 2.1 Correction #1 — the KS4 lesson-quiz corpus was undercounted (fixed 23 Sep 2026)

This report originally scanned the lesson-page quiz corpus via only the
`_triple_higher` variant per subject, reasoning (from `ks4_brief.py`'s own
comment) that it is the documented superset of the other three tier/pathway
variant files. **That superset claim was tested and is false for
chemistry.** Measured directly, per subject, by comparing the quiz-stem
TEXT set of each of the four variant files against their union:

| Subject | `_triple_higher` alone | Union of all four | Missed by scanning `_triple_higher` only |
|---|---:|---:|---:|
| Biology | 247 | 247 | 0 |
| Physics | 164 | 164 | 0 |
| **Chemistry** | 310 | **389** | **79** |

Biology and physics genuinely are strict supersets in `_triple_higher`.
**Chemistry is not**: the base variant (`all_subtopics_chemistry.py`) holds
55 quiz stems absent from `_triple_higher`, and `_triple_foundation` holds
79 (a superset of that 55). Example stems the original scan never saw:
*"Describe how you can use an element's group number to predict the charge
on its ion,"* *"State the type of bond in a monomer that allows addition
polymerisation to happen,"* *"Identify a use of copper that depends on it
being a good electrical conductor,"* *"Name the type of force that must be
overcome to melt a simple molecular substance."*

**The fix, applied uniformly, not special-cased to chemistry:** the scan now
reads all four variant files for every subject and takes the union of quiz
stems, deduplicated by exact text (first-seen wins for topic/leaf
provenance, in a fixed variant order — base, higher, triple_foundation,
triple_higher — so the result is deterministic). The 79 newly-included
chemistry stems were run back through the keyword net that was live at the
time; **zero matched**, so no re-adjudication was needed for those 79
specifically — but see §2.2, because the net itself changed two days later.

One side effect of text-based dedup, found while checking this: one genuine
authored duplicate exists in `all_subtopics_biology_triple_higher.py` — the
stem *"Why was Darwin's theory of natural selection initially
controversial?"* is authored verbatim under both `evolution-natural-
selection` and `theory-of-evolution`. Deduping by text collapses it to one
row, which is why biology's own scanned count moves by one stem even though
its `_triple_higher`-vs-union comparison shows 0 missed. This stem was never
a keyword-net candidate either way.

**Checked whether the same variant-file assumption affects any other
corpus**, rather than leaving it implied: it does not. `ks3_data/` (both the
lesson ladder and the assignment bank) has no `_higher`/`_triple_foundation`/
`_triple_higher` sibling files at all — confirmed by listing every unit
directory — because KS3 has no tier/pathway split at the content-file level
(the easier/standard/harder band inside one file does that job instead). The
KS4 assignment bank is read via `ks4_data.load_pool()`, which globs
`ks4_data/questions/<subject>/*.py` as a single unified file set per
subject, not four parallel tier files. So this correction changed the KS4
lesson-page quiz corpus and nothing else: total stems scanned moved from
35,173 to **35,251** (+78: +79 genuinely new chemistry stems, −1 from the
biology duplicate above).

### 2.2 Correction #2 — the keyword net itself only reached about a fifth of the candidate space (fixed 23 Sep 2026)

This is the larger correction, and it changes the confirmed/borderline
counts, not just the denominator. **Say this plainly, because a future
reader needs to know the net was tested, not just described:** the first
net was a list of roughly 80 remembered *phrases* — `"a rectangle"`,
`"the diagram shows"`, `"an arrow"`, `"circuit diagram"`, and so on — and it
missed a bare, unqualified `\bdiagram\b`. So a stem reading *"A diagram
shows a small rectangle inside a circle. Name that component"* — nearly a
word-for-word restatement of Mide's own canonical bad example — was never
even a candidate, because `\ba rectangle\b` does not match "a small
rectangle" and no pattern matched bare "diagram" at all. The same held for
bare `graph`, `symbol`, `chart`, `drawn`/`draw`, `labelled`, `sketch`.

**Coordinator review measured the gap directly** by building a net on the
actual tell — *the stem refers to a visual artefact that is not there* —
rather than on a list of phrases someone happened to think of, and running
it over all 35,251 stems. That net (reproduced in Appendix A as
`wide_net.py`) matches on:

- **artefact nouns, bare and unqualified:** `diagram|graph|chart|figure|
  sketch|image|picture|photograph|trace|plot|circuit|axis|axes|scale
  drawing|pyramid of (biomass|numbers)|food web|table`
- **depiction verbs:** `is/are/was/were (drawn|shown|plotted|marked|
  labelled|sketched)`, and bare `draws?|drawn|labelled|shown`
- **visual primitives:** `arrow(s)`, `symbol(s)`, `rectangle|triangle|
  circle|square|zig-zag|dotted/solid/curved/straight line`
- **deixis to a page position** near a showing verb: `(above|below|
  opposite|left|right)` within ~20 characters of `shows?|shown|drawn`,
  either order
- **apparatus:** `apparatus|clamp(ed)|tripod|gauze`
- **labelled points:** `(point|position|box|branch) [A-Z]`
- **instrument readings:** `the needle|the pointer|reading on the`

kept as a **union with the original ~80-phrase list**, not a replacement of
it — the phrase list cost nothing to keep and catches a few things the
categories don't explicitly name (e.g. "food chain").

**The measurement:**

| | Original net | Wide net |
|---|---:|---:|
| Total candidates (of 35,251 stems) | 413 | 2,351 |
| Never reached by the original net | — | 1,938 |

The original net reached **17.6%** of the candidate space the wide net
finds — "about a fifth," as the coordinator estimated before the exact count
was run. The two sets do not overlap at all (verified: the intersection of
the two candidate-text sets is empty in both directions), so the wide net's
1,938 new candidates are genuinely new, not a re-slicing of the same 413.

**Adjudication.** The original 413 candidates' verdicts stand — they were
made against the same rule, by the same method (Opus examiners, batched),
and re-litigating them was explicitly out of scope for this correction. The
1,938 new candidates were adjudicated the same way: 33 batches of up to 60
rows, one parallel Opus examiner agent per batch, same CONFIRMED /
BORDERLINE / REJECTED rubric — but with the examiner brief **tightened**
first, because the coordinator's own spot-check predicted (correctly) that
a wide net finds mostly convention questions that merely use a visual word.
The brief for this pass added the explicit REJECT examples now in §1
(dot-and-cross convention, free-body arrow-length convention) verbatim, and
opened with an explicit warning that the batch was flagged by "a
deliberately very wide keyword net… the large majority of these rows will
be REJECTED. Read carefully — do not let the presence of a trigger word
bias you toward CONFIRMED." Full method in Appendix B.

**Result of the 1,938 new candidates:** 67 CONFIRMED, 63 BORDERLINE, 1,808
REJECTED (93.3% REJECTED — the tightened brief held; there was no flood of
false confirmations). Combined with the original 413's 43 CONFIRMED / 29
BORDERLINE / 341 REJECTED, across the full 2,351-candidate set:

**CONFIRMED moved from 43 to 110. BORDERLINE moved from 29 to 92.** Every
count in §3 onward is the corrected, combined figure — the old numbers are
not reprinted as a comparison table because doing so risks a reader copying
the wrong one; the §2.2 measurement above is the record of what changed and
by how much.

One further correction, caught while re-deriving these tables and unrelated
to either gap above: the KS3 lesson ladder's `topic` field used to be read
from `LESSON["unit"]` (a descriptive slug/title, e.g. `"Describing
motion"`), while the assignment-bank scan below labels the same unit by its
**code** (`"P3"`). Two label conventions for one column meant a
confirmed/borderline ladder row could split away from its own unit's bank
rows in the per-topic tables in §3.5 — invisible while the ladder had zero
confirmed rows, and it now has three. Fixed by reading the unit code from
the ladder's own file path instead, matching the bank's convention; see
Appendix A.

## 3. Counts

### 3.1 Headline

| | Count |
|---|---|
| Total stems scanned | 35,251 |
| Candidates (wide-net keyword match, both nets combined) | 2,351 |
| **CONFIRMED** (Opus examiner) | **110** |
| **BORDERLINE** | **92** |
| REJECTED (false positive) | 2,149 |
| Confirmed **in the frozen window** (`bank_position ≤ 11`) | **14** |
| Borderline in the frozen window | 14 |

### 3.2 Per key stage

| Key stage | Scanned | Candidates | Confirmed | Borderline |
|---|---:|---:|---:|---:|
| KS3 | 17,686 | 1,285 | 46 | 47 |
| KS4 | 17,565 | 1,066 | 64 | 45 |

### 3.3 Per subject

| Subject | Scanned | Candidates | Confirmed | Borderline |
|---|---:|---:|---:|---:|
| Physics | 11,895 | 1,263 | **93** | 61 |
| Chemistry | 11,826 | 585 | 8 | 15 |
| Biology | 11,530 | 503 | 9 | 16 |

The fault is overwhelmingly a physics problem: 93 of 110 confirmed rows
(85%). It clusters where physics genuinely lives on symbols, traces and
labelled geometry — circuit diagrams, graph traces, force-resolution
triangles, motor/field diagrams — and comparatively little elsewhere.

### 3.4 Per corpus

| Corpus | Candidates | Confirmed | Borderline |
|---|---:|---:|---:|
| KS3 assignment bank | 1,233 | 43 | 45 |
| KS3 lesson ladder | 52 | 3 | 2 |
| KS4 assignment bank | 1,031 | 60 | 42 |
| KS4 lesson-page quiz | 35 | 4 | 3 |

**The ladder is no longer clean** — the correction in §2.2 found 3 confirmed
rows in it (all physics: a P3 distance-time "describe this journey" rung, a
P4 two-arrow force diagram rung, a P9 field-map rung), where the original
scan found none. It is still by far the smallest source of the fault: 52
candidates out of 740 ladder stems (7%), versus 1,233 of 16,946 bank stems
(7.3%) — proportionally about the same rate, in fact, once the net is wide
enough to see it. The lesson ladder was never specially resistant to this
fault; the original net was just too narrow to find its few instances.

### 3.5 Per topic (key stage / subject / topic), confirmed + borderline only

| Key stage | Subject | Topic | Candidates | Confirmed | Borderline |
|---|---|---|---:|---:|---:|
| KS4 | physics | electricity | 177 | **40** | 11 |
| KS4 | physics | forces | 186 | **16** | 12 |
| KS3 | physics | P8 — Electric circuits | 132 | 10 | 5 |
| KS3 | physics | P3 — Describing motion | 63 | 9 | 7 |
| KS3 | physics | P10 — Magnetism and electromagnetism | 63 | 4 | 3 |
| KS3 | physics | P6 — Waves and sound | 62 | 4 | 2 |
| KS3 | biology | B9 — Ecosystems and interdependence | 81 | 3 | 3 |
| KS4 | chemistry | bonding | 49 | 3 | 3 |
| KS3 | physics | P4 — Forces | 96 | 2 | 5 |
| KS3 | physics | P12 — Space | 53 | 2 | 1 |
| KS3 | physics | P9 — Static electricity | 29 | 2 | 1 |
| KS4 | biology | homeostasis | 19 | 2 | 1 |
| KS3 | biology | B4 — Breathing and gas exchange | 16 | 2 | 0 |
| KS4 | physics | magnetism | 85 | 1 | 6 |
| KS3 | biology | B10 — Inheritance and DNA | 46 | 1 | 5 |
| KS3 | chemistry | C1 — Particles and their behaviour | 23 | 1 | 2 |
| KS4 | physics | waves | 83 | 1 | 2 |
| KS3 | biology | B5 — Reproduction | 12 | 1 | 1 |
| KS3 | chemistry | C3 — Mixtures and separation | 36 | 1 | 1 |
| KS3 | chemistry | C6 — Acids and alkalis | 19 | 1 | 1 |
| KS3 | chemistry | C10 — The Earth and its atmosphere | 31 | 1 | 0 |
| KS3 | chemistry | C2 — Atoms, elements and compounds | 89 | 1 | 0 |
| KS3 | physics | P1 — Energy transfers | 14 | 1 | 0 |
| KS4 | physics | atomic-structure | 24 | 1 | 0 |
| KS3 | biology | B8 — Respiration | 13 | 0 | 2 |
| KS3 | chemistry | C4 — Chemical reactions | 18 | 0 | 2 |
| KS3 | physics | P7 — Light | 101 | 0 | 2 |
| KS4 | biology | ecology | 141 | 0 | 2 |
| KS4 | chemistry | organic | 10 | 0 | 2 |
| KS4 | physics | space | 7 | 0 | 2 |
| KS3 | biology | B3 — Nutrition and digestion | 28 | 0 | 1 |
| KS3 | chemistry | C7 — Energy changes in reactions | 12 | 0 | 1 |
| KS3 | chemistry | C9 — Metals and materials | 5 | 0 | 1 |
| KS3 | physics | P11 — Matter and the particle model | 8 | 0 | 1 |
| KS4 | biology | inheritance | 25 | 0 | 1 |
| KS4 | chemistry | energy-changes | 13 | 0 | 1 |
| KS4 | chemistry | resources | 11 | 0 | 1 |
| KS4 | physics | energy | 16 | 0 | 1 |

**Two topics carry over half the confirmed total: KS4 electricity (40 of
110) and KS4 forces (16 of 110).** Add their KS3 physics siblings — P8
Electric circuits (10), P3 Describing motion (9), P10 Magnetism (4), P6
Waves and sound (4) — and six topics account for 83 of the 110 confirmed
rows (75%). This is still a narrow, well-defined defect concentrated in
physics symbol/trace/geometry content, not an estate-wide one — it is simply
a bigger and more spread-out narrow defect than the first pass found.

### 3.6 Per leaf (subtopic/lesson), confirmed rows only

| Key stage/subject/topic/leaf | Confirmed |
|---|---:|
| KS4/physics/electricity/**circuit-symbols** | 36 |
| KS3/physics/P3/**distance-time-graphs** | 9 |
| KS3/physics/P8/**current-and-circuits** | 7 |
| KS4/physics/forces/**distance-time-graphs** | 7 |
| KS4/physics/forces/**resolving-forces** | 5 |
| KS3/physics/P6/sound-is-longitudinal | 3 |
| KS4/physics/electricity/direct-alternating-pd | 3 |
| KS3/biology/B4/stomata-and-gas-exchange-in-plants | 2 |
| KS3/biology/B9/food-chains-and-food-webs | 2 |
| KS3/physics/P10/how-a-motor-works | 2 |
| KS3/physics/P10/magnetic-fields | 2 |
| KS3/physics/P4/drawing-and-adding-forces | 2 |
| KS3/physics/P8/conductors-and-insulators | 2 |
| KS4/chemistry/bonding/covalent-bonding | 2 |
| KS4/physics/forces/free-body-diagrams | 2 |
| KS3/biology/B10/variation-continuous-and-discontinuous | 1 |
| KS3/biology/B5/the-menstrual-cycle | 1 |
| KS3/biology/B9/predator-and-prey | 1 |
| KS3/chemistry/C1/solids-liquids-and-gases | 1 |
| KS3/chemistry/C10/whats-in-the-air | 1 |
| KS3/chemistry/C2/compounds | 1 |
| KS3/chemistry/C3/distillation | 1 |
| KS3/chemistry/C6/the-ph-scale-and-indicators | 1 |
| KS3/physics/P1/heating-and-thermal-equilibrium | 1 |
| KS3/physics/P12/gravity-and-weight | 1 |
| KS3/physics/P12/how-far-is-a-light-year | 1 |
| KS3/physics/P6/waves-on-water | 1 |
| KS3/physics/P8/potential-difference | 1 |
| KS3/physics/P9/electric-fields | 1 |
| KS3/physics/P9/forces-between-charges | 1 |
| KS4/biology/homeostasis/homeostasis | 1 |
| KS4/biology/homeostasis/human-reproduction-hormones | 1 |
| KS4/chemistry/bonding/ionic-bonding | 1 |
| KS4/physics/atomic-structure/mass-number-isotopes | 1 |
| KS4/physics/electricity/electric-fields | 1 |
| KS4/physics/forces/acceleration | 1 |
| KS4/physics/forces/forces-elasticity | 1 |
| KS4/physics/magnetism/electromagnetism | 1 |
| KS4/physics/waves/wave-front-refraction | 1 |

`circuit-symbols` alone (KS3 + KS4 combined) is 43 of the 110 confirmed
rows — the fault has a single, very sharp centre of gravity, with a long
tail of one-and-two-row leaves everywhere else physics draws a symbol,
arrow, or trace.

## 4. Frozen-window rows (`bank_position ≤ 11`)

MRB-335's rule: positions 0–11 of any bank lesson/subtopic are what
`bankFor()` (backend) and `compose_assignment()` / `auto_pool()` (Python)
read for **automatic weekly composition**, forever — inserting into or
reordering that window changes every auto-composed assignment the estate has
ever produced. This audit treats those rows as **not safely editable in
place** by a content fix; they need to be worked around, not touched,
without an explicit ruling from Mide that touching a frozen row's *text*
(keeping its id, band and position unchanged) is safe under that rule. That
is a policy call belonging to Mide, not to this audit — the rule as written
governs composition *positions*, not per-row content immutability, so it is
genuinely unclear whether an in-place text edit is forbidden by the letter of
MRB-335 or only by the spirit of "don't touch what's frozen." Flagging it
rather than assuming an answer.

**28 rows total sit in the frozen window** (14 confirmed, 14 borderline —
up from 6 and 3 in the first-pass count, for the same reason every other
number above grew: the wider net reaches rows the phrase list walked past,
frozen ones included):

| Verdict | Row | Leaf | Position | Stem |
|---|---|---|---:|---|
| CONFIRMED | `b10-01-e01` | KS3 biology B10 | 0 | "The height graph on the bench is drawn with the bars touching. What are the touching bars claiming?" |
| CONFIRMED | `b4-05-e04` | KS3 biology B4 | 3 | "On the bench the third bar is labelled 'What a sensor outside the leaf measures'. What is that bar showing?" |
| CONFIRMED | `b9-01-e03` | KS3 biology B9 | 2 | "In the oak wood web, exactly one arrow touches the ladybirds: it runs from the aphids to the ladybirds. What does that tell you?" |
| CONFIRMED | `b9-01-s03` | KS3 biology B9 | 6 | "In the oak wood web, one arrow runs from the mice all the way up to the sparrowhawk, crossing a whole row. What does that arrow show?" |
| CONFIRMED | `c1-02-e01` | KS3 chemistry C1 | 0 | "The state bench draws one extra particle at the side, labelled 'one particle, actual size'… Why is it drawn that way?" |
| CONFIRMED | `p10-05-h02` | KS3 physics P10 | 9 | "On a motor diagram the two force arrows are always drawn the same length as each other, whatever the current is set to. Why must that be right?" |
| CONFIRMED | `p4-02-h02` | KS3 physics P4 | 9 | "A student draws a 40 N arrow and a 25 N arrow pointing opposite ways, then a 15 N arrow underneath. Why do the two lower bars on the lesson's beam exactly fill the top one?" |
| CONFIRMED | `p8-01-e04` | KS3 physics P8 | 3 | "In the circuit symbols, a circle with a cross inside it means…" |
| CONFIRMED | `p9-02-s04` | KS3 physics P9 | 7 | "In the nine-case table of every charge combination, how many of the nine give no force at all?" |
| CONFIRMED | `ks4-circuit-symbols-e01` | KS4 physics electricity | 0 | "Which component is drawn as a rectangle with an arrow through it?" |
| CONFIRMED | `ks4-circuit-symbols-s03` | KS4 physics electricity | 6 | "A circuit diagram shows a cell, a closed switch and two lamps all in one loop. Describe the change needed…" |
| CONFIRMED | `ks4-circuit-symbols-h02` | KS4 physics electricity | 9 | "Two students draw the sensing part of a fire alarm. Student A draws a resistor rectangle with a diagonal line through it; student B draws…" |
| CONFIRMED | `ks4-circuit-symbols-h04` | KS4 physics electricity | 11 | "A circuit has a battery, a switch, and two branches — one holding a lamp and one holding a motor. An ammeter must read the total current…" |
| CONFIRMED | `ks4-acceleration-h03` | KS4 physics forces | 10 | "A skydiver's velocity–time graph rises steeply from the origin, then curves so that its gradient falls to zero…" |
| BORDERLINE | `b10-03-h01` | KS3 biology B10 | 8 | "The diagram draws A and G wide and C and T narrow. Suppose the rule had instead been A with G and C with T…" |
| BORDERLINE | `b3-05-s04` | KS3 biology B3 | 7 | "The chart puts the stomach at about four hours and the small intestine at about sixteen…" |
| BORDERLINE | `b5-02-h01` | KS3 biology B5 | 8 | "The lesson draws the egg's bar twenty times as long as the sperm head's…" |
| BORDERLINE | `c1-02-e03` | KS3 chemistry C1 | 2 | "100 cm³ of water is poured from a tall measuring cylinder into a wide flat dish. Which of the contrast table's rows has changed?" |
| BORDERLINE | `p10-02-s03` | KS3 physics P10 | 6 | "Between the jaws of a horseshoe magnet the arrows on a field map are nearly parallel and nearly the same length…" |
| BORDERLINE | `p8-06-s03` | KS3 physics P8 | 6 | "Why does the chart of resistances use an axis where every mark is a thousand times the one before?" |
| BORDERLINE | `p9-03-s01` | KS3 physics P9 | 4 | "At a point on a field map the arrow points to the right. A small NEGATIVE charge is placed there…" |
| BORDERLINE | `ks4-food-chains-webs-s02` | KS4 biology ecology | 5 | "In a moorland food web, heather is eaten by mountain hares and by red grouse, and foxes eat both…" |
| BORDERLINE | `ks4-covalent-bonding-s04` | KS4 chemistry bonding | 7 | "A student's dot-and-cross diagram of ammonia shows the nitrogen atom with only six electrons…" |
| BORDERLINE | `ks4-condensation-polymerisation-h02` | KS4 chemistry organic | 9 | "A student draws a polyester repeat unit in which an –OH group and a –COOH group are still shown…" |
| BORDERLINE | `ks4-circuit-symbols-e04` | KS4 physics electricity | 3 | "Describe how the symbol for a battery differs from the symbol for a single cell." |
| BORDERLINE | `ks4-circuit-symbols-e02` | KS4 physics electricity | 1 | "Which description matches the standard symbol for an open switch?" |
| BORDERLINE | `ks4-direct-alternating-pd-h02` | KS4 physics electricity | 9 | "Trace X shows 5 complete cycles across an oscilloscope screen. Trace Y shows 10 complete cycles across the same screen…" |
| BORDERLINE | `ks4-distance-time-graphs-h02` | KS4 physics forces | 9 | "A runner's distance–time graph rises steeply from the origin and then curves, becoming gradually less steep…" |

**KS4 electricity/circuit-symbols alone carries five of the 28 frozen rows**
(four confirmed, one borderline) — the fault was baked in from
`bank_position` 0, the very first question ever authored for that subtopic,
and stayed baked in through position 11.

## 5. The full confirmed list (110 rows), grouped by subject → topic → leaf

Format: `key_stage/subject/topic/leaf · corpus · band/rung · pos N[ FROZEN] · id`
then the stem on the next line.

```
KS3/biology/B10/variation-continuous-and-discontinuous · assignment-bank · easier · pos 0 [FROZEN] · b10-01-e01
    "The height graph on the bench is drawn with the bars touching. What are the touching bars claiming?"
KS3/biology/B4/stomata-and-gas-exchange-in-plants · assignment-bank · easier · pos 3 [FROZEN] · b4-05-e04
    "On the bench the third bar is labelled "What a sensor outside the leaf measures". What is that bar showing?"
KS3/biology/B4/stomata-and-gas-exchange-in-plants · assignment-bank · harder · pos 78 · b4-05-h17
    "Respiration's line against light is flat and straight. Photosynthesis rises then levels off. Explain why the NET movement curve against light is not a straight line either."
KS3/biology/B5/the-menstrual-cycle · assignment-bank · harder · pos 85 · b5-03-h26
    "A poster draws the cycle as a clock face with day 1 at the top and release at the bottom. Is that drawing fair for a 35-day cycle?"
KS3/biology/B9/food-chains-and-food-webs · assignment-bank · easier · pos 2 [FROZEN] · b9-01-e03
    "In the oak wood web, exactly one arrow touches the ladybirds: it runs from the aphids to the ladybirds. What does that tell you?"
KS3/biology/B9/food-chains-and-food-webs · assignment-bank · standard · pos 6 [FROZEN] · b9-01-s03
    "In the oak wood web, one arrow runs from the mice all the way up to the sparrowhawk, crossing a whole row. What does that arrow show?"
KS3/biology/B9/predator-and-prey · assignment-bank · harder · pos 84 · b9-02-h25
    "A student plots predator numbers against prey numbers for twenty years and gets a loop rather than a straight line. What does the loop show?"
KS3/chemistry/C1/solids-liquids-and-gases · assignment-bank · easier · pos 0 [FROZEN] · c1-02-e01
    "The state bench draws one extra particle at the side, labelled "one particle, actual size", and it is drawn the same size beside the solid, beside the liquid and beside the gas. Why is it drawn that way?"
KS3/chemistry/C10/whats-in-the-air · assignment-bank · standard · pos 67 · c10-05-s30
    "The bar chart's scale note names both gases affected by the drawing floor AND states their true combined share. Why does it need to give BOTH pieces of information, rather than just one?"
KS3/chemistry/C2/compounds · assignment-bank · easier · pos 14 · c2-03-e07
    "The particle diagram of the heated dish shows every iron atom joined to one sulfur atom, all the way through. What is that a picture of?"
KS3/chemistry/C3/distillation · assignment-bank · harder · pos 76 · c3-05-h13
    "A refinery column is at 350 °C at the bottom, about 200 °C a third of the way up, about 100 °C two thirds up and about 25 °C at the top. Kerosene condenses between 150 °C and 250 °C. Where is it drawn off?"
KS3/chemistry/C6/the-ph-scale-and-indicators · assignment-bank · easier · pos 72 · c6-02-e32
    "The printed pH scale is drawn as a row of coloured cells, one for each whole number. How many cells are there?"
KS3/physics/P1/heating-and-thermal-equilibrium · assignment-bank · harder · pos 73 · p1-04-h14
    "A student measures a beaker of water cooling and plots temperature against time. The graph falls steeply at first and then levels off, approaching room temperature without quite reaching it in the recorded time. What does the levelling off represent?"
KS3/physics/P10/how-a-motor-works · assignment-bank · harder · pos 9 [FROZEN] · p10-05-h02
    "On a motor diagram the two force arrows are always drawn the same length as each other, whatever the current is set to. Why must that be right?"
KS3/physics/P10/how-a-motor-works · assignment-bank · harder · pos 29 · p10-05-h10
    "On a motor diagram the two force arrows are drawn the same length as each other whatever the current is. Why?"
KS3/physics/P10/magnetic-fields · assignment-bank · harder · pos 75 · p10-02-h16
    "A field map correctly shows crowding near the poles of a bar magnet. A second, completely separate map of the SAME magnet is drawn with twice as many lines throughout, still correctly crowded near the poles in the same proportion. Do the two maps disagree about anything physical?"
KS3/physics/P10/magnetic-fields · assignment-bank · harder · pos 86 · p10-02-h27
    "A single bar magnet's field is mapped at two points the same distance from its centre: point X level with a pole, and point Y level with the middle of the magnet's side. Explain which point reads stronger, and why."
KS3/physics/P12/gravity-and-weight · assignment-bank · easier · pos 38 · p12-01-e21
    "On the weight triangle, W sits above the line and m and g sit below it, side by side. If you cover 'g', what are you left looking at?"
KS3/physics/P12/how-far-is-a-light-year · assignment-bank · easier · pos 31 · p12-06-e16
    "A formula triangle shows d over c and t. Which rearrangement finds the TIME, given a distance and a speed?"
KS3/physics/P3/distance-time-graphs · ladder · explain · pos (n/a) · P3/distance-time-graphs#explain
    "A graph rises steeply, then flattens, then rises gently. Describe that journey in words and say how you know each part, without using the words up or down."
KS3/physics/P3/distance-time-graphs · assignment-bank · standard · pos 26 · p3-02-s06
    "A graph rises for 20 s, stays flat for 10 s, then rises again for 10 s. For how long was the object moving?"
KS3/physics/P3/distance-time-graphs · assignment-bank · harder · pos 38 · p3-02-h05
    "A distance-from-start graph rises to 100 m in 10 s, stays flat for 20 s, then falls back to 0 m over the next 20 s. What is the average speed for the whole 50 s?"
KS3/physics/P3/distance-time-graphs · assignment-bank · harder · pos 43 · p3-02-h10
    "A graph rises 30 m in 10 s, is flat for 20 s, then rises 30 m in 5 s. Which section is fastest, and how fast?"
KS3/physics/P3/distance-time-graphs · assignment-bank · harder · pos 49 · p3-02-h16
    "A pupil's distance-from-home graph shows a walk to school 800 m away taking 600 s, then six hours at school, then the walk home. Which part is horizontal, and at what height?"
KS3/physics/P3/distance-time-graphs · assignment-bank · standard · pos 68 · p3-02-s22
    "On a graph the time axis is marked every 5 s, and the line reaches 45 m at the fourth mark. What is the average speed up to that point?"
KS3/physics/P3/distance-time-graphs · assignment-bank · standard · pos 74 · p3-02-s28
    "Two lines on the same axes are parallel, but one stays 20 m above the other throughout. What does that tell you?"
KS3/physics/P3/distance-time-graphs · assignment-bank · standard · pos 76 · p3-02-s30
    "Line A is steeper than line B, but B's line ends higher up the distance axis. Which object finished further from the start?"
KS3/physics/P3/distance-time-graphs · assignment-bank · harder · pos 78 · p3-02-h19
    "The same journey is drawn twice, once with the distance axis running to 100 m and once to 1000 m. Why does the line look far steeper on the first?"
KS3/physics/P4/drawing-and-adding-forces · ladder · apply · pos (n/a) · P4/drawing-and-adding-forces#apply
    "Two arrows on a diagram are drawn the same length, one pointing left and one pointing right. What does the diagram say?"
KS3/physics/P4/drawing-and-adding-forces · assignment-bank · harder · pos 9 [FROZEN] · p4-02-h02
    "A student draws a 40 N arrow and a 25 N arrow pointing opposite ways, then a 15 N arrow underneath. Why do the two lower bars on the lesson's beam exactly fill the top one?"
KS3/physics/P6/sound-is-longitudinal · assignment-bank · harder · pos 69 · p6-04-h10
    "A wave diagram marks 6 consecutive compressions, evenly spaced 30 cm apart from each other. What is the distance from the first marked compression to the last?"
KS3/physics/P6/sound-is-longitudinal · assignment-bank · harder · pos 79 · p6-04-h20
    "A diagram marks 4 consecutive compressions, 22 cm apart from each other. What is the total span from the first to the last?"
KS3/physics/P6/sound-is-longitudinal · assignment-bank · harder · pos 88 · p6-04-h29
    "A diagram shows 3 evenly spaced compressions, marked from left to right, with nothing shown before the first or after the last. How many complete wavelengths are shown between the marked compressions?"
KS3/physics/P6/waves-on-water · assignment-bank · harder · pos 73 · p6-01-h14
    "A photograph of a ripple tank shows 6 evenly spaced crests along a 1.5 m stretch of water, with one crest at each end of the stretch. What is the wavelength?"
KS3/physics/P8/conductors-and-insulators · assignment-bank · harder · pos 68 · p8-06-h09
    "On the resistance chart, copper's bar looks only slightly shorter than nichrome's, even though nichrome resists about twenty times more. Why doesn't the bar length show that clearly?"
KS3/physics/P8/conductors-and-insulators · assignment-bank · harder · pos 80 · p8-06-h21
    "Two materials' bars on the log chart look almost the same length, yet a caption says one resists "about four hundred times as much" as the other. How can bars that look similar represent such different numbers?"
KS3/physics/P8/current-and-circuits · assignment-bank · easier · pos 24 · p8-01-e09
    "In the circuit symbols, two long-and-short line pairs drawn one after the other represent…"
KS3/physics/P8/current-and-circuits · assignment-bank · easier · pos 28 · p8-01-e13
    "What turns a plain resistor's symbol into a variable resistor's symbol?"
KS3/physics/P8/current-and-circuits · assignment-bank · harder · pos 86 · p8-01-h27
    "A component's symbol is a plain rectangle with a diagonal arrow drawn across it. A student says the arrow must mean current can only pass through it in one direction, like a one-way valve. Assess this."
KS3/physics/P8/current-and-circuits · assignment-bank · easier · pos 3 [FROZEN] · p8-01-e04
    "In the circuit symbols, a circle with a cross inside it means…"
KS3/physics/P8/current-and-circuits · assignment-bank · easier · pos 25 · p8-01-e10
    "One long line and one short line, side by side, is the symbol for…"
KS3/physics/P8/current-and-circuits · assignment-bank · easier · pos 27 · p8-01-e12
    "A plain rectangle drawn in the wire, with nothing else added to it, is the symbol for…"
KS3/physics/P8/current-and-circuits · assignment-bank · easier · pos 29 · p8-01-e14
    "A circle with the letter V inside it, rather than the letter A, is the symbol for…"
KS3/physics/P8/potential-difference · assignment-bank · harder · pos 87 · p8-04-h28
    "A student wants a single circuit where moving a voltmeter from position A to position B gives a SMALLER reading, while moving an ammeter from the SAME position A to the SAME position B in a single, unbranched loop always gives an IDENTICAL reading. Is this combination possible in an ordinary single loop?"
KS3/physics/P9/electric-fields · ladder · recall · pos (n/a) · P9/electric-fields#recall
    "A field map shows arrows pointing outwards in every direction, away from a single object at the centre. What can you say about the object and about a small negative charge released nearby?"
KS3/physics/P9/forces-between-charges · assignment-bank · standard · pos 7 [FROZEN] · p9-02-s04
    "In the nine-case table of every charge combination, how many of the nine give no force at all?"
KS4/biology/homeostasis/homeostasis · assignment-bank · harder · pos 59 · ks4-homeostasis-h22
    "A student is given two unlabelled graphs of a body condition over time: one oscillates gently around a fixed line, the other rises steadily with no correction. Determine which shows a homeostatic system working."
KS4/biology/homeostasis/human-reproduction-hormones · assignment-bank · standard · pos 22 · ks4-human-reproduction-hormones-s07
    "A hormone graph shows a sharp, brief peak around the middle of the cycle. Identify the hormone."
KS4/chemistry/bonding/covalent-bonding · assignment-bank · standard · pos 33 · ks4-covalent-bonding-s18
    "A student draws methane with four dots on the carbon and one cross on each hydrogen, none of them between the atoms. Explain what is wrong."
KS4/chemistry/bonding/covalent-bonding · lesson-quiz · quiz-7 · pos (n/a) · bonding/covalent-bonding#quiz7(higher)
    "A dot-and-cross diagram of carbon dioxide shows O=C=O. Explain how this arrangement gives every atom a full outer shell."
KS4/chemistry/bonding/ionic-bonding · assignment-bank · standard · pos 37 · ks4-ionic-bonding-s22
    "A dot-and-cross diagram of magnesium oxide draws the oxide ion with eight outer electrons, two of them crosses. Explain what the two crosses show."
KS4/physics/atomic-structure/mass-number-isotopes · assignment-bank · standard · pos 22 · ks4-mass-number-isotopes-s07
    "A nuclide is written in nuclear notation with 23 above the element symbol and 11 below it. Determine the number of neutrons in its nucleus."
KS4/physics/electricity/circuit-symbols · assignment-bank · easier · pos 0 [FROZEN] · ks4-circuit-symbols-e01
    "Which component is drawn as a rectangle with an arrow through it?"
KS4/physics/electricity/circuit-symbols · lesson-quiz · quiz-2 · pos (n/a) · electricity/circuit-symbols#quiz2(base)
    "What does the symbol of a circle with a cross inside represent?"
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 9 [FROZEN] · ks4-circuit-symbols-h02
    "Two students draw the sensing part of a fire alarm. Student A draws a resistor rectangle with a diagonal line through it; student B draws a resistor rectangle with two arrows pointing in towards it. Evaluate which student is correct."
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 11 [FROZEN] · ks4-circuit-symbols-h04
    "A circuit has a battery, a switch, and two branches — one holding a lamp and one holding a motor. An ammeter must read the total current supplied by the battery. Determine where it should be drawn."
KS4/physics/electricity/circuit-symbols · assignment-bank · easier · pos 14 · ks4-circuit-symbols-e07
    "A diagram shows a small rectangle inside a circle. Name that component."
KS4/physics/electricity/circuit-symbols · assignment-bank · easier · pos 16 · ks4-circuit-symbols-e09
    "On a diagram, one of the rectangles carries no extra mark. State which component that is."
KS4/physics/electricity/circuit-symbols · assignment-bank · standard · pos 29 · ks4-circuit-symbols-s14
    "On a diagram of a cell, a switch and a lamp, one wire stops short of the cell and does not reach it. A technician builds the circuit exactly as drawn. Predict what happens."
KS4/physics/electricity/circuit-symbols · assignment-bank · standard · pos 30 · ks4-circuit-symbols-s15
    "A diagram shows two rectangles: one is plain, and one has a line drawn along its length. State what each one is."
KS4/physics/electricity/circuit-symbols · assignment-bank · standard · pos 38 · ks4-circuit-symbols-s23
    "A diagram shows one circle with the letter A in the main wire and another circle with the letter M on a branch. State what each one shows."
KS4/physics/electricity/circuit-symbols · assignment-bank · standard · pos 39 · ks4-circuit-symbols-s24
    "A circuit must be drawn in its switched-off state. A pupil draws the lever resting on the contact. Explain the error."
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 43 · ks4-circuit-symbols-h06
    "A diagram was meant to protect a circuit with a fuse, but a plain rectangle has been drawn instead. Predict what the built circuit does if the current becomes far too large."
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 44 · ks4-circuit-symbols-h07
    "A diagram shows two circles: one lies in the loop itself, the other on a short pair of wires bridging a resistor. Determine which meter is which."
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 46 · ks4-circuit-symbols-h09
    "A pupil labels a supply as two cells but draws only one long line with one short line. Evaluate the diagram."
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 48 · ks4-circuit-symbols-h11
    "A circuit divides into two branches, one with a lamp and one with a buzzer. A gap is left in the lamp branch only, and the circuit is built as drawn. Determine what works."
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 52 · ks4-circuit-symbols-h15
    "Two lamps are wired from one cell. One lamp fails, and the other stays lit. Determine which diagram matches what happened."
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 59 · ks4-circuit-symbols-h22
    "A diagram is ruled neatly, but a lamp sits at a corner and one wire stops short of the cell. Evaluate the diagram."
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 61 · ks4-circuit-symbols-h24
    "A diagram places an ammeter in the lamp branch, but the technician builds it into the motor branch instead. Evaluate whether the reading is still the one wanted."
KS4/physics/electricity/circuit-symbols · assignment-bank · standard · pos 6 [FROZEN] · ks4-circuit-symbols-s03
    "A circuit diagram shows a cell, a closed switch and two lamps all in one loop. Describe the change needed so that one lamp can be switched off while the other stays lit."
KS4/physics/electricity/circuit-symbols · assignment-bank · easier · pos 12 · ks4-circuit-symbols-e05
    "State what a circle with a sine wave drawn inside it stands for."
KS4/physics/electricity/circuit-symbols · assignment-bank · easier · pos 13 · ks4-circuit-symbols-e06
    "Which component is drawn as a circle with the letter M inside it?"
KS4/physics/electricity/circuit-symbols · assignment-bank · easier · pos 15 · ks4-circuit-symbols-e08
    "One symbol is a rectangle with a thin line running along its length. Which component is it?"
KS4/physics/electricity/circuit-symbols · assignment-bank · easier · pos 17 · ks4-circuit-symbols-e10
    "A diode symbol is drawn with two arrows pointing away from it. Which component does this show?"
KS4/physics/electricity/circuit-symbols · assignment-bank · standard · pos 20 · ks4-circuit-symbols-s05
    "A student drawing a torch uses a circle with the letter M inside it for the torch bulb. Explain the error."
KS4/physics/electricity/circuit-symbols · assignment-bank · standard · pos 21 · ks4-circuit-symbols-s06
    "A cell, a switch and a motor are joined in one loop. Describe where a voltmeter is drawn to measure the potential difference across the motor."
KS4/physics/electricity/circuit-symbols · assignment-bank · standard · pos 23 · ks4-circuit-symbols-s08
    "A supply is drawn as three long lines, each paired with a short line, joined end to end. State what it shows."
KS4/physics/electricity/circuit-symbols · assignment-bank · standard · pos 28 · ks4-circuit-symbols-s13
    "A diagram carries a circle with the letter A inside it, labelled as the buzzer. Explain what is wrong."
KS4/physics/electricity/circuit-symbols · assignment-bank · standard · pos 32 · ks4-circuit-symbols-s17
    "A lamp's brightness must be adjustable while the circuit runs, but the diagram shows a plain rectangle. Suggest the correction."
KS4/physics/electricity/circuit-symbols · assignment-bank · standard · pos 33 · ks4-circuit-symbols-s18
    "On a diagram the cell is drawn with its long line on the left. State what this tells a student."
KS4/physics/electricity/circuit-symbols · assignment-bank · standard · pos 36 · ks4-circuit-symbols-s21
    "A rectangle with a line running through it is drawn in the wire leaving the supply. Describe what this component does."
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 45 · ks4-circuit-symbols-h08
    "A cell feeds a main wire that divides into two branches, one holding a motor and one holding a buzzer. A switch is drawn in the buzzer branch only. Determine what that switch controls."
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 49 · ks4-circuit-symbols-h12
    "A model railway controller must let its user change the current to the track while the train runs. Compare a plain rectangle with a rectangle carrying an arrow."
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 51 · ks4-circuit-symbols-h14
    "A supply feeds two branches, one holding a motor and one holding a lamp. An ammeter is to read the current in the motor alone. Determine where it is drawn."
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 54 · ks4-circuit-symbols-h17
    "A cell feeds two branches. One branch holds a lamp on its own; the other holds a lamp with a rectangle carrying an arrow beside it. Determine which lamp can be dimmed."
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 56 · ks4-circuit-symbols-h19
    "A circuit is powered by three cells in a battery holder, but the diagram shows the supply as a circle with a sine wave. Suggest the correction."
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 57 · ks4-circuit-symbols-h20
    "A single loop is drawn holding a cell, a lamp and two switches. Determine what the lamp does when one switch is closed and the other is left open."
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 60 · ks4-circuit-symbols-h23
    "One loop is drawn holding a cell, a circle with A, a rectangle with an arrow through it and a circle with a cross. Determine what this circuit is for."
KS4/physics/electricity/direct-alternating-pd · assignment-bank · standard · pos 23 · ks4-direct-alternating-pd-s08
    "An oscilloscope displays a wave that rises 2.5 divisions above the centre line and falls the same 2.5 divisions below it, using a y-gain setting of 2.0 V per division. Determine the peak potential difference shown."
KS4/physics/electricity/direct-alternating-pd · assignment-bank · standard · pos 41 · ks4-direct-alternating-pd-s26
    "A trace shows 2.5 complete cycles across a screen 10 divisions wide, with the time base at 4.0 ms per division. Calculate the frequency of the supply."
KS4/physics/electricity/direct-alternating-pd · lesson-quiz · quiz-1 · pos (n/a) · electricity/direct-alternating-pd#quiz1(base)
    "An oscilloscope shows a horizontal line above the zero axis. What does this represent?"
KS4/physics/electricity/electric-fields · assignment-bank · harder · pos 55 · ks4-electric-fields-h18
    "At point A the field lines around a charged object are 2 mm apart; at point B they are 8 mm apart. Compare the electric force on the same small charge placed at each of the two points."
KS4/physics/forces/acceleration · assignment-bank · harder · pos 10 [FROZEN] · ks4-acceleration-h03
    "A skydiver's velocity–time graph rises steeply from the origin, then curves so that its gradient falls to zero at a velocity of 55 m/s after 14 s. Determine what is happening to her acceleration and her velocity at 14 s."
KS4/physics/forces/distance-time-graphs · assignment-bank · harder · pos 59 · ks4-distance-time-graphs-h22
    "A cyclist's plot has a straight section of gradient 9.0 m/s followed by a curve that flattens to horizontal. Determine what the cyclist does."
KS4/physics/forces/distance-time-graphs · assignment-bank · harder · pos 61 · ks4-distance-time-graphs-h24
    "Two lines on one plot have the same gradient, but one of them is twice as long. Determine what is the same and what is different about the journeys."
KS4/physics/forces/distance-time-graphs · lesson-quiz · quiz-1 · pos (n/a) · forces/distance-time-graphs#quiz1(base)
    "A d–t graph shows a horizontal (flat) line for 5 seconds. What is the object doing?"
KS4/physics/forces/distance-time-graphs · assignment-bank · standard · pos 26 · ks4-distance-time-graphs-s11
    "Between 0 s and 60 s a train's plotted line is a smooth curve that keeps getting steeper. State how the train is moving."
KS4/physics/forces/distance-time-graphs · assignment-bank · standard · pos 27 · ks4-distance-time-graphs-s12
    "Two cars start from one place at the same moment. Car J's plotted line is straight; car K's curves upwards more and more steeply and crosses J's line at 40 s. Describe what happens at 40 s."
KS4/physics/forces/distance-time-graphs · assignment-bank · standard · pos 28 · ks4-distance-time-graphs-s13
    "A plotted line is horizontal for 25 s and then rises steeply. Explain what the driver did."
KS4/physics/forces/distance-time-graphs · assignment-bank · harder · pos 55 · ks4-distance-time-graphs-h18
    "A lift's motion is plotted as a series of straight sections with flat parts between them. Determine what that shape shows."
KS4/physics/forces/forces-elasticity · assignment-bank · harder · pos 61 · ks4-forces-elasticity-h24
    "A best-fit line of force against extension is straight but crosses the extension axis well to the right of the origin. Suggest the most likely reason."
KS4/physics/forces/free-body-diagrams · assignment-bank · harder · pos 44 · ks4-free-body-diagrams-h09
    "A small ring is in equilibrium. Its diagram shows 8 N acting vertically upwards, 6 N acting horizontally to the right and one unknown force. Determine the unknown."
KS4/physics/forces/free-body-diagrams · assignment-bank · harder · pos 46 · ks4-free-body-diagrams-h11
    "A car passes over the top of a humpback bridge, following a curve that bends downwards. Compare the two vertical arrows there."
KS4/physics/forces/resolving-forces · assignment-bank · easier · pos 14 · ks4-resolving-forces-e07
    "A pull of 50 N acts along the longest side of a 3-4-5 right-angled triangle whose horizontal side is the 4 and whose vertical side is the 3. Calculate the vertical component."
KS4/physics/forces/resolving-forces · assignment-bank · easier · pos 21 · ks4-resolving-forces-e14
    "A rope pulls a sledge with a force of 100 N along a line that makes a 6-8-10 right-angled triangle with the ground, the 8 lying along the ground and the 6 vertical. Calculate the horizontal component."
KS4/physics/forces/resolving-forces · assignment-bank · standard · pos 26 · ks4-resolving-forces-s05
    "A garden roller is pushed with a force of 250 N along a line making a 3-4-5 right-angled triangle with the ground, the 4 along the ground and the 3 vertical. Calculate the downward component of the push."
KS4/physics/forces/resolving-forces · assignment-bank · standard · pos 37 · ks4-resolving-forces-s16
    "A wheelbarrow handle is pulled with 260 N along a line making a 5-12-13 right-angled triangle with the ground, the 12 lying along the ground. Calculate the vertical component."
KS4/physics/forces/resolving-forces · assignment-bank · harder · pos 51 · ks4-resolving-forces-h16
    "A pull of 500 N acts along a line making a 3-4-5 right-angled triangle with a horizontal floor, the 4 lying along the floor. Determine both components and state which is larger."
KS4/physics/magnetism/electromagnetism · assignment-bank · harder · pos 50 · ks4-electromagnetism-h07
    "A solenoid lies horizontally on a bench with its axis running left to right in front of you. At the top of each turn the current flows away from you, and along the bottom of each turn it returns towards you. Determine which end is the north pole."
KS4/physics/waves/wave-front-refraction · assignment-bank · harder · pos 49 · ks4-wave-front-refraction-h14
    "A student's refraction diagram shows the wave fronts closer together in the second material and the wave bending away from the normal. Explain why this cannot be right."
```

## 6. The full borderline list (92 rows)

Kept separate per instructions — not part of any "confirmed" total or fix
count above, but worth Mide's eye because several turn on a genuinely fine
distinction (a symbol-comparison question with nothing to compare, versus a
purely definitional/conceptual use of "drawn"/"plotted"/"arrow").

```
KS3/biology/B10/how-we-worked-out-dna · assignment-bank · harder · pos 8 [FROZEN] · b10-03-h01
    "The diagram draws A and G wide and C and T narrow. Suppose the rule had instead been A with G and C with T. What would the molecule have been like?"
KS3/biology/B10/how-we-worked-out-dna · assignment-bank · easier · pos 32 · b10-03-e13
    "An X-ray image of DNA fibres shows a cross-shaped pattern of spots. What does that cross indicate?"
KS3/biology/B10/variation-continuous-and-discontinuous · assignment-bank · standard · pos 21 · b10-01-s07
    "A class of 12 students plots its own heights and gets a lumpy graph with two separate peaks rather than one smooth hump. What is the best explanation?"
KS3/biology/B10/variation-continuous-and-discontinuous · assignment-bank · standard · pos 64 · b10-01-s24
    "A student plots 60 heights in 1 cm groups and gets a jagged graph with many empty bars. What should she do?"
KS3/biology/B10/variation-continuous-and-discontinuous · assignment-bank · harder · pos 84 · b10-01-h25
    "A class plots the boys' and the girls' heights as two curves that overlap heavily. A student says the graph proves height is discontinuous, since there are two groups. Evaluate."
KS3/biology/B3/the-digestive-system · assignment-bank · standard · pos 7 [FROZEN] · b3-05-s04
    "The chart puts the stomach at about four hours and the small intestine at about sixteen. What does that comparison tell you about the two organs?"
KS3/biology/B5/gametes-and-fertilisation · assignment-bank · harder · pos 8 [FROZEN] · b5-02-h01
    "The lesson draws the egg's bar twenty times as long as the sperm head's. A student concludes the egg is twenty times as much cell. Where does that go wrong?"
KS3/biology/B8/aerobic-vs-anaerobic · assignment-bank · easier · pos 44 · b8-05-e25
    "Which row of a comparison table correctly matches 'what it is for' to each route?"
KS3/biology/B8/anaerobic-respiration-in-humans · assignment-bank · standard · pos 56 · b8-03-s17
    "A student sees a graph showing anaerobic energy supply rising sharply during a sprint and concludes the aerobic supply must be falling at the same time. Evaluate this conclusion."
KS3/biology/B9/food-chains-and-food-webs · assignment-bank · harder · pos 74 · b9-01-h15
    "A pyramid of numbers for an oak wood comes out upside down: one oak at the bottom supporting thousands of caterpillars above it. Does that contradict the tenth-of-the-energy rule?"
KS3/biology/B9/food-chains-and-food-webs · assignment-bank · standard · pos 49 · b9-01-s11
    "A student draws a garden food web. Two arrows point into the blackbird: one from the earthworms and one from the berry bush. What does that tell you?"
KS3/biology/B9/predator-and-prey · assignment-bank · standard · pos 51 · b9-02-s13
    "A student draws a graph of a wood in which the owl line sits above the vole line at every point. What is wrong with the drawing?"
KS3/chemistry/C1/solids-liquids-and-gases · assignment-bank · easier · pos 2 [FROZEN] · c1-02-e03
    "100 cm³ of water is poured from a tall measuring cylinder into a wide flat dish. Which of the contrast table's rows has changed?"
KS3/chemistry/C1/solids-liquids-and-gases · assignment-bank · harder · pos 22 · c1-02-h05
    "Liquid crystals flow like a liquid while their particles stay lined up like a solid's. Which two rows of the contrast table disagree about them?"
KS3/chemistry/C3/distillation · assignment-bank · standard · pos 66 · c3-05-s28
    "A student clamps the thermometer so the bulb sits high in the neck of the flask, well above the side arm and out of the vapour's path. What happens to the reading?"
KS3/chemistry/C4/chemical-vs-physical-change · assignment-bank · easier · pos 16 · c4-01-e09
    "The comparison table lists where you meet each kind of change. Which list is the CHEMICAL one?"
KS3/chemistry/C4/mass-in-a-reaction · assignment-bank · standard · pos 23 · c4-04-s10
    "The lesson says conservation of mass is drawn as a bar and never as a triangle. Why does the shape matter?"
KS3/chemistry/C6/neutralisation · assignment-bank · harder · pos 55 · c6-03-h10
    "A titration trace is flat at the start, jumps, then is flat again. Explain why it is flat at BOTH ends."
KS3/chemistry/C7/energy-and-changes-of-state · assignment-bank · standard · pos 68 · c7-01-s22
    "A student heats a substance steadily and their graph shows one flat step and then a steady climb to the end of the run. What did they most likely do?"
KS3/chemistry/C9/ceramics-polymers-and-composites · assignment-bank · standard · pos 65 · c9-04-s23
    "Which TWO materials on the shelf both meet "stiff under load" AND "cheap by the square metre"?"
KS3/physics/P10/magnetic-fields · assignment-bank · standard · pos 6 [FROZEN] · p10-02-s03
    "Between the jaws of a horseshoe magnet the arrows on a field map are nearly parallel and nearly the same length. What does that tell you about the field there?"
KS3/physics/P10/magnetic-fields · assignment-bank · standard · pos 56 · p10-02-s16
    "A horseshoe magnet's field between its two jaws is drawn as almost parallel, evenly-spaced lines. Why do scientists value a region of field shaped like this?"
KS3/physics/P10/magnetic-fields · assignment-bank · harder · pos 72 · p10-02-h13
    "A field map is drawn showing a magnetic field line that starts on the north pole and simply fades away into nothing, without reaching the south pole. An examiner marks this map as scientifically wrong. Explain the reasoning."
KS3/physics/P11/brownian-motion · assignment-bank · harder · pos 37 · p11-02-h12
    "A speck's path is drawn as straight segments joined at random angles. Why is that a fair picture?"
KS3/physics/P12/the-sun-stars-and-galaxies · assignment-bank · harder · pos 81 · p12-04-h22
    "An axis is marked 1, 10, 100, 1000, 10 000 and 100 000, each mark the same distance from the next. Is that a logarithmic or a straight-line scale?"
KS3/physics/P3/distance-time-graphs · ladder · recall · pos (n/a) · P3/distance-time-graphs#recall
    "A distance–time graph is horizontal between 20 s and 35 s. What was happening in those fifteen seconds?"
KS3/physics/P3/distance-time-graphs · ladder · apply · pos (n/a) · P3/distance-time-graphs#apply
    "Two journeys are drawn on the same axes. Line A is steeper than line B. Which statement must be true?"
KS3/physics/P3/distance-time-graphs · assignment-bank · standard · pos 29 · p3-02-s09
    "On the same axes, line A runs from the origin to 50 m at 10 s and line B from the origin to 50 m at 25 s. Which is true?"
KS3/physics/P3/distance-time-graphs · assignment-bank · harder · pos 80 · p3-02-h21
    "A train's graph has time in minutes along the bottom and distance in kilometres up the side. One section climbs 6 km in 4 minutes. What is that speed in metres per second?"
KS3/physics/P3/distance-time-graphs · assignment-bank · easier · pos 22 · p3-02-e15
    "Two journeys are plotted on the same axes and the two lines cross at 20 s. What does the crossing point mean?"
KS3/physics/P3/distance-time-graphs · assignment-bank · easier · pos 52 · p3-02-e19
    "Two walkers are plotted on the same axes. One line begins at 0 s and the other begins at 20 s. What does that tell you?"
KS3/physics/P3/speed · assignment-bank · easier · pos 57 · p3-01-e24
    "In the formula triangle for speed, which letter sits on its own above the dividing line?"
KS3/physics/P4/drawing-and-adding-forces · assignment-bank · easier · pos 22 · p4-02-e11
    "On one diagram, two arrows are drawn 4 cm and 8 cm long. What does that say about the two forces?"
KS3/physics/P4/drawing-and-adding-forces · assignment-bank · standard · pos 46 · p4-02-s11
    "A student draws a 30 N arrow and a 45 N arrow the same length. What has the diagram now claimed?"
KS3/physics/P4/drawing-and-adding-forces · assignment-bank · standard · pos 52 · p4-02-s17
    "One diagram shows a 12 N arrow 3 cm long and a 20 N arrow 4 cm long. Why is the diagram wrong?"
KS3/physics/P4/drawing-and-adding-forces · assignment-bank · standard · pos 59 · p4-02-s24
    "On a diagram drawn at 1 cm to 10 N, the pull right is 7 cm and the pull left is 3 cm. What is the resultant?"
KS3/physics/P4/drawing-and-adding-forces · assignment-bank · harder · pos 80 · p4-02-h21
    "A diagram shows a 50 N arrow and a 10 N arrow, both drawn 5 cm long and pointing opposite ways. Which two false things does it now say?"
KS3/physics/P6/waves-on-water · assignment-bank · easier · pos 42 · p6-01-e17
    "The leading edge of one crest is marked, and the matching leading edge of the very next crest is marked 0.45 m further along. What is the wavelength?"
KS3/physics/P6/waves-on-water · assignment-bank · harder · pos 89 · p6-01-h30
    "A student sketches a water wave whose crests and troughs get progressively closer together from left to right, all with the same height. A second student says this cannot be a real single wave, because 'a wave's wavelength has to stay constant all the way along.' Assess this second claim, and suggest what such a changing spacing might show instead."
KS3/physics/P7/colour-and-the-spectrum · assignment-bank · standard · pos 49 · p7-06-s13
    "A textbook drawing shows the colours leaving a prism fanned very widely apart. Why is that drawing not to scale?"
KS3/physics/P7/lenses-and-images · assignment-bank · harder · pos 79 · p7-04-h20
    "A textbook diagram of a pinhole camera draws only one ray from the top of the object and one from the bottom, crossing at the hole. Does this mean only two rays are really involved in forming the picture?"
KS3/physics/P8/conductors-and-insulators · assignment-bank · standard · pos 6 [FROZEN] · p8-06-s03
    "Why does the chart of resistances use an axis where every mark is a thousand times the one before?"
KS3/physics/P8/conductors-and-insulators · assignment-bank · standard · pos 49 · p8-06-s13
    "The resistance chart uses a scale where equal steps mean ×1000, not +1000. Why does that suit this data better than an equal-steps-of-one scale?"
KS3/physics/P8/current-and-circuits · assignment-bank · standard · pos 67 · p8-01-s30
    "A student sketches a battery symbol using three pairs of long and short lines instead of two. What has changed about what the symbol represents?"
KS3/physics/P8/current-and-circuits · assignment-bank · easier · pos 26 · p8-01-e11
    "A switch that is open is drawn as…"
KS3/physics/P8/current-at-a-junction · assignment-bank · harder · pos 78 · p8-03-h19
    "A junction's main wire reading is plotted over time as a component in one branch heats up and its resistance rises steadily. The OTHER branch is untouched throughout. Describe the shape of the main-wire graph, and the unchanged branch's own graph."
KS3/physics/P9/electric-fields · assignment-bank · standard · pos 4 [FROZEN] · p9-03-s01
    "At a point on a field map the arrow points to the right. A small NEGATIVE charge is placed there. Which way is it pushed?"
KS4/biology/ecology/food-chains-webs · assignment-bank · standard · pos 5 [FROZEN] · ks4-food-chains-webs-s02
    "In a moorland food web, heather is eaten by mountain hares and by red grouse, and foxes eat both the hares and the grouse. A disease kills most of the mountain hares. Predict the effect on the foxes."
KS4/biology/ecology/food-chains-webs · assignment-bank · harder · pos 62 · ks4-food-chains-webs-h25
    "A chain is drawn with its arrows running from each predator back to its prey. Explain why the species are right but the science is wrong."
KS4/biology/homeostasis/endocrine-system · assignment-bank · standard · pos 37 · ks4-endocrine-system-s22
    "A pupil labels the pancreas, the ovaries and the pituitary on an outline of the body. Identify the one label that is in the wrong place if the pituitary is drawn below the stomach."
KS4/biology/inheritance/variation · assignment-bank · harder · pos 51 · ks4-variation-h14
    "A scientist plots the masses of 500 seeds and gets a smooth curve with one peak. Deduce what this tells her."
KS4/chemistry/bonding/covalent-bonding · assignment-bank · standard · pos 7 [FROZEN] · ks4-covalent-bonding-s04
    "A student's dot-and-cross diagram of ammonia shows the nitrogen atom with only six electrons in its outer shell. Explain what has gone wrong."
KS4/chemistry/bonding/covalent-bonding · assignment-bank · harder · pos 60 · ks4-covalent-bonding-h23
    "A student draws carbon dioxide with one shared pair between the carbon and each oxygen. Explain why the diagram cannot be right."
KS4/chemistry/bonding/states-of-matter · lesson-quiz · quiz-11 · pos (n/a) · bonding/states-of-matter#quiz11(triple_higher)
    "On a graph of temperature against time, a solid is heated until it becomes a gas. Explain why the graph has two flat (horizontal) sections."
KS4/chemistry/energy-changes/reaction-profiles · assignment-bank · harder · pos 42 · ks4-reaction-profiles-h05
    "A student sketches an endothermic profile in which the peak is drawn LOWER than the product level. Identify why the sketch must be wrong."
KS4/chemistry/organic/condensation-polymerisation · assignment-bank · harder · pos 9 [FROZEN] · ks4-condensation-polymerisation-h02
    "A student draws a polyester repeat unit in which an –OH group and a –COOH group are still shown between the two monomer units. Explain what is wrong."
KS4/chemistry/organic/condensation-polymerisation · assignment-bank · standard · pos 27 · ks4-condensation-polymerisation-s10
    "A student draws a polyester's repeat unit showing a free –OH and a free –COOH group still present within it. Explain what is wrong with this drawing."
KS4/chemistry/resources/haber-process · assignment-bank · easier · pos 14 · ks4-haber-process-e07
    "What does the symbol used in place of an arrow in the Haber equation tell you about the reaction?"
KS4/physics/electricity/circuit-symbols · assignment-bank · easier · pos 1 [FROZEN] · ks4-circuit-symbols-e02
    "Which description matches the standard symbol for an open switch?"
KS4/physics/electricity/circuit-symbols · assignment-bank · standard · pos 31 · ks4-circuit-symbols-s16
    "A diode must let the current pass from the cell to a buzzer. Describe how its triangle should be drawn."
KS4/physics/electricity/circuit-symbols · assignment-bank · standard · pos 37 · ks4-circuit-symbols-s22
    "A diagram has a lamp drawn at the corner where two wires meet. Explain why this is poor practice."
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 55 · ks4-circuit-symbols-h18
    "A diagram shows a cell joined to a lamp by two ruled wires, and a pupil complains that the lamp cannot be turned off. Determine which symbol is missing."
KS4/physics/electricity/circuit-symbols · assignment-bank · harder · pos 63 · ks4-circuit-symbols-h26
    "A diagram shows only a cell and a lamp joined in a loop. Determine what must be added so the lamp can be dimmed and also switched off."
KS4/physics/electricity/circuit-symbols · assignment-bank · easier · pos 3 [FROZEN] · ks4-circuit-symbols-e04
    "Describe how the symbol for a battery differs from the symbol for a single cell."
KS4/physics/electricity/circuit-symbols · assignment-bank · easier · pos 18 · ks4-circuit-symbols-e11
    "How is a closed switch shown on a circuit diagram?"
KS4/physics/electricity/direct-alternating-pd · assignment-bank · harder · pos 9 [FROZEN] · ks4-direct-alternating-pd-h02
    "Trace X shows 5 complete cycles across an oscilloscope screen. Trace Y shows 10 complete cycles across the same screen at the same time base setting. Compare the two supplies."
KS4/physics/electricity/direct-alternating-pd · assignment-bank · harder · pos 55 · ks4-direct-alternating-pd-h18
    "An oscilloscope trace initially shows 4 complete cycles spread across a 10-division-wide screen, with the time base set to 2.0 ms per division. The supply's frequency is then halved while the time base stays the same. Work out how many complete cycles now appear across the screen."
KS4/physics/electricity/electrical-charge-current · assignment-bank · easier · pos 18 · ks4-electrical-charge-current-e11
    "A single loop contains a cell and two lamps. One lamp is unscrewed from its holder. State the current in the wire on the far side of the loop."
KS4/physics/electricity/resistors · assignment-bank · harder · pos 47 · ks4-resistors-h10
    "A student's I–V graph for a fixed resistor is straight at low potential differences but bends over at the highest ones. Suggest what happened and how to avoid it."
KS4/physics/energy/efficiency · assignment-bank · standard · pos 27 · ks4-efficiency-s12
    "In a Sankey diagram for a device, the input arrow is 100 mm wide and the useful output arrow is 35 mm wide. Determine the efficiency."
KS4/physics/forces/distance-time-graphs · assignment-bank · harder · pos 9 [FROZEN] · ks4-distance-time-graphs-h02
    "A runner's distance–time graph rises steeply from the origin and then curves, becoming gradually less steep, until it is horizontal at 400 m after 80 s. Determine her average speed and compare it with her speed at 70 s."
KS4/physics/forces/distance-time-graphs · assignment-bank · standard · pos 22 · ks4-distance-time-graphs-s07
    "A plot of distance against time for a school bus is a straight line for the first 200 s, then a flat section, then another straight line of the same steepness. Describe the journey."
KS4/physics/forces/distance-time-graphs · assignment-bank · standard · pos 37 · ks4-distance-time-graphs-s22
    "On one plot of distance against time, one line is straight and another curves so that it flattens off. Compare what the two lines show."
KS4/physics/forces/distance-time-graphs · lesson-quiz · quiz-2 · pos (n/a) · forces/distance-time-graphs#quiz2(base)
    "On a distance–time graph, two straight sections are drawn. Section A has gradient 8 m/s and section B has gradient 2 m/s. Which section shows faster motion?"
KS4/physics/forces/distance-time-graphs · assignment-bank · harder · pos 48 · ks4-distance-time-graphs-h11
    "A runner's plotted line rises steeply at first and then bends until it is flat at 2400 m after 600 s. Determine her average speed and describe how her speed changed."
KS4/physics/forces/forces-elasticity · assignment-bank · standard · pos 34 · ks4-forces-elasticity-s19
    "On one set of axes, the straight line for spring X is steeper than the straight line for spring Y. Compare the two springs."
KS4/physics/forces/forces-elasticity · assignment-bank · standard · pos 38 · ks4-forces-elasticity-s23
    "Loads are added to a spring well past its limit of proportionality, with force up the vertical axis. Describe how the line changes."
KS4/physics/forces/free-body-diagrams · assignment-bank · standard · pos 37 · ks4-free-body-diagrams-s16
    "A diagram for a hanging sign shows three arrows from one point: 40 N down, 40 N up and nothing else. Deduce the state of the sign."
KS4/physics/forces/free-body-diagrams · assignment-bank · harder · pos 52 · ks4-free-body-diagrams-h17
    "For a descending parachutist a student draws weight down, drag up, and a third arrow up labelled 'the pull of the parachute'. Assess the third arrow."
KS4/physics/forces/free-body-diagrams · assignment-bank · harder · pos 50 · ks4-free-body-diagrams-h15
    "One arrow on a book's free body diagram reads 'the table pushes up on the book'. Identify its interaction partner and say where that partner is drawn."
KS4/physics/forces/gravity · assignment-bank · harder · pos 45 · ks4-gravity-h08
    "Results from an unnamed planet give a straight line of weight against mass through the origin with a gradient of 3.7. Interpret this value."
KS4/physics/forces/gravity · assignment-bank · harder · pos 46 · ks4-gravity-h09
    "Weight against mass is plotted for two worlds on one set of axes, giving two straight lines from the origin, one much steeper. Interpret the steeper line."
KS4/physics/magnetism/electromagnetism · assignment-bank · harder · pos 59 · ks4-electromagnetism-h16
    "A graph of an electromagnet's strength against current rises almost as a straight line at first, then bends over and becomes nearly flat at high currents. Explain the flat part."
KS4/physics/magnetism/magnetic-fields · lesson-quiz · quiz-1 · pos (n/a) · magnetism/magnetic-fields#quiz1(base)
    "A student plots a magnetic field using iron filings around a bar magnet. The filings cluster densely near the poles. What does this show?"
KS4/physics/magnetism/magnetic-fields · assignment-bank · standard · pos 35 · ks4-magnetic-fields-s16
    "Two plotting compasses are put down close to the north pole of a bar magnet, one on each side of it. Describe the directions their needles take."
KS4/physics/magnetism/magnetic-fields · assignment-bank · standard · pos 40 · ks4-magnetic-fields-s21
    "A bar magnet lies east to west on a bench with its north pole to the east. A plotting compass is set down beside the middle of the magnet, close enough that the magnet's field is far stronger there than the Earth's. State the direction the needle's north end points."
KS4/physics/magnetism/magnetic-fields · assignment-bank · harder · pos 68 · ks4-magnetic-fields-h25
    "Two plotting compasses are placed on the axis of a long bar magnet, one a little beyond each end. Compare the directions their needles settle in."
KS4/physics/magnetism/uses-generator-effect · assignment-bank · easier · pos 12 · ks4-uses-generator-effect-e05
    "A generator has two slip rings, one joined to each end of the rotating coil, with a carbon brush pressed against each ring. State what kind of current this arrangement supplies to the circuit outside."
KS4/physics/space/red-shift-big-bang · assignment-bank · harder · pos 67 · ks4-red-shift-big-bang-h24
    "A graph plotting the recession speed of forty galaxies against their distance shows a clear overall upward trend, but the points do not lie on a perfectly straight line — several sit noticeably above or below it. Evaluate whether this scatter means Hubble's Law should be rejected."
KS4/physics/space/red-shift-big-bang · assignment-bank · harder · pos 62 · ks4-red-shift-big-bang-h19
    "On a graph of recession speed against distance, one galaxy plots at (50 Mpc, 3500 km/s) and another at (150 Mpc, 10 500 km/s), and both points lie on the same straight line through the origin. Calculate the gradient of that line."
KS4/physics/waves/sound-waves-hearing · assignment-bank · harder · pos 49 · ks4-sound-waves-hearing-h14
    "A fishing boat's sonar trace shows the seabed and, above it, a second fainter line. Suggest what produces the second line."
KS4/physics/waves/transverse-longitudinal-waves · assignment-bank · harder · pos 49 · ks4-transverse-longitudinal-waves-h12
    "A student draws a longitudinal sound wave as a smooth curve on axes of pressure against distance. Evaluate whether this drawing is acceptable."
```

## 7. What diagram-rendering capability already exists

This matters because most of the fix is **wiring existing capability to a
new place**, not inventing new capability from nothing — except at KS4,
where the gap is real and total. The wider confirmed set (§2.2) does not
change this picture; it mostly adds MORE rows in the same shapes (more
circuit symbols, more graph traces, more force diagrams) plus a handful of
genuinely new shapes (dot-and-cross molecule diagrams, oscilloscope traces,
force-resolution triangles), noted below.

### 7.1 KS3 — a real SVG figure system, plus a much bigger interactive-instrument system next to it

- **The figure mechanism.** A KS3 lesson can declare `LESSON["figures"]`, a
  list of `{"id", "kind", "status", "art", "title", …}` records. `"art"`
  names a drawer function registered in that unit's `ks3_art/<unit>.py`
  module, built on a shared SVG primitive kit in **`ks3_art/kit.py`**:
  `_svg_open`, `_rect`, `_circle`, `_ellipse`, `_line`, `_path`, `_label`,
  `_mono` — real vector primitives, not a bitmap pipeline. A figure is
  placed on the lesson page via a `core[]` block `{"type": "figure", "ref":
  "<id>", "anchor": …}`. **A bank or ladder question can already point at
  one of these by id** — the `"figure"` key on a `QUESTIONS` row (e.g.
  `b10-03-h07` references `b10-base-pairs`, `b11-02-...` references
  `b11-moth-pair`) — so the reference-a-static-figure path is proven and
  already shipping; it is just unused on the confirmed rows.

- **A much larger family of drawers already exists for the shapes driving
  most of the fault.** `ks3_art/p8.py` (Electric circuits) contains
  `r_circuit_loop`, `r_two_arrangement_loop`, `r_junction_bench`,
  `r_voltmeter_tap`, `r_component_under_test`, `r_meter_placement`, and a
  `_symbols(specs, act_id)` function that renders circuit **symbols** by
  name. `ks3_art/p10.py` (Magnetism) contains `r_motor_coil`, `r_mag_band`,
  `r_compass_plot`, `r_dip_circle`, `r_solenoid_bench`, and named
  field-pattern arts `_art_repel`, `_art_attract`, `_art_crowd`,
  `_art_nocross`, `_art_outin`, `_art_readings`. `ks3_art/p4.py` (Forces)
  is the same story for **force-arrow diagrams**: the confirmed P4 rows are
  exactly "two arrows drawn a stated length, pointing opposite ways" — the
  ladder rung even references "the lesson's beam", i.e. an existing
  interactive force-bar instrument in that unit's own module.
  **The pictures the confirmed KS3 circuit/motor/force rows are missing
  already have drawing code sitting in the same unit's `ks3_art` module** —
  registered as an *instrument* (interactive, used on the lesson page), not
  extracted as a *static figure* a bank question can cite. Turning an
  existing instrument's static rendering into a referenceable figure is a
  much smaller job than writing a new drawer.

- The generic-graph gap is smaller than it looks: `ks3_art/p8.py` already
  has `_table` and `_bars` primitives, which are most of what a simple
  bar-chart or scatter figure needs. Nothing generic for a smooth line/curve
  trace (cooling curves, distance-time graphs — now the single largest KS3
  leaf at 9 confirmed rows — distribution histograms, wave-compression
  diagrams) exists yet and would need a small new plotting primitive in
  `kit.py`, usable by every one of P3/P6/B4/B9/B10's confirmed rows at once.

- **Formula triangles are a new, small, and very repeatable shape.** Three
  confirmed rows (P12 weight, P12 light-year/speed, and the P3-adjacent
  speed-triangle borderline) all describe the same primitive: a triangle
  split into an upper cell and two lower cells. One drawer covers every
  formula triangle in the estate (speed, weight, density, and so on),
  KS3 and KS4 alike.

### 7.2 KS4 — no drawer system at all; this is the real gap, and it is now the largest single cluster in the audit

`ks4_data/questions/**/*.py` has **no `figure` field in its record shape**,
and there is no Python SVG kit analogous to `ks3_art/` anywhere in the KS4
content path. `all_subtopics_*.py` (the lesson-page content, including the
`quiz` blocks) likewise has no figure/drawer mechanism. This means:

- **The single largest confirmed cluster in the whole audit — 40 rows in
  KS4 physics/electricity, 36 of them in circuit-symbols alone — has
  literally nothing to attach a diagram to.** Building this is not "wire up
  an existing figure", it is "build a KS4 figure system from nothing": a
  record-shape addition (`"figure"` key), a rendering path from that key to
  whatever renders a served KS4 assignment on the student side, and either
  porting the KS3 circuit-symbol SVG drawers to a KS4-side module or sharing
  `ks3_art/kit.py`'s primitives directly (recommended, since they carry no
  KS3-specific dependency once the unit registries are excluded).
- **Three further KS4-only shapes need new drawers, once the system
  exists.** (a) **Dot-and-cross molecule diagrams** (bonding, 3 confirmed +
  3 borderline: methane, carbon dioxide, magnesium oxide, ammonia, a
  polyester repeat unit) — a specialised drawer, atoms as labelled circles
  with dot/cross pairs placed between or around them, parametrised by
  formula. (b) **Oscilloscope traces** (electricity, direct-alternating-pd,
  3 confirmed + 2 borderline) — a sine-wave-on-a-grid drawer, parametrised
  by cycle count and amplitude, which is also most of what the generic
  line-trace plotter in §7.1 already needs, so build them together. (c)
  **Force-resolution triangles** (forces, 5 confirmed) — a right-angled
  triangle with a hypotenuse force and two labelled sides, closely related
  to (and possibly the same drawer as) the formula-triangle primitive in
  §7.1, since both are "a triangle whose three parts a pupil reads back".
- Same generic-line-trace gap as KS3 for KS4 forces/distance-time-graphs (7
  confirmed, the corpus's second-largest leaf) — build once, share both
  key stages.

### 7.3 Front-end JS widgets — none of them fit, but one sets a useful precedent

`shared/periodic-table.js` (an HTML/CSS periodic table overlay, not an
image), `shared/chain-builder.js` (drag-free polymer chain assembly),
`shared/formula-deducer.js` (ionic-formula prediction widget) are all
purpose-built for something unrelated to circuit/graph diagrams and are not
a fit. `shared/seating-canvas.js` is the one worth citing as **architectural
precedent**: it deliberately chose SVG over `<canvas>` for a free-placement
diagram, precisely because hit-testing and accessibility (`aria-label`,
focusable elements) come free with real DOM nodes — the same reasoning that
should govern any new circuit/graph SVG renderer, KS3 or KS4.

### 7.4 3D Studio

`3d-studio/` is a Vite-built 3D anatomy/asset viewer. Nothing about 2D
circuit symbols, motor diagrams, or line graphs fits its purpose or its
asset pipeline. Not a candidate for this fix.

### 7.5 The worksheet renderer (backend, read-only checked at
`/Users/midebadmus/Documents/GitHub/mrbadmus-backend-worktrees/mrb342-2/worksheet.js`)

- **PDF path (PDFKit):** PDFKit has a native 2D vector drawing API
  (`doc.rect`, `.circle`, `.moveTo/.lineTo`, `.path`) already used
  implicitly by the library itself — nothing in `worksheet.js` currently
  draws a shape beyond the brand mark, but a circuit/graph diagram could be
  drawn **directly as vectors** in the PDF, with no rasterisation step
  needed. This is the easier of the two output formats to add diagrams to.
- **DOCX path (the `docx` library):** DOCX can only embed a **raster**
  image via `ImageRun` — there is no vector-drawing API exposed to a Word
  document from this library. Today the only image anywhere in the file is
  `markPng()`, a **hand-built PNG constructed byte-by-byte via `zlib`** for
  the trivial two-polyline brand mark — there is no SVG-to-raster dependency
  in the backend at all. Shipping a diagram into a DOCX worksheet needs
  either (a) a new server-side rasterisation dependency (e.g. `sharp`,
  `resvg`, or an equivalent that can take an SVG string and return a PNG
  buffer), or (b) hand-porting each diagram type's draw calls into a small
  bespoke raster routine the way `markPng()` was — viable for a handful of
  fixed symbol shapes (circuit components), painful for anything
  parametrised (a distance-time graph with data-dependent geometry).
- **No image path exists today for a *question's* diagram at all** — the
  worksheet's only image is brand, never content. This is a build item
  regardless of which side (PDF or DOCX) ships diagrams first.

## 8. Proposed fix-run plan

Sequenced by leverage (existing capability first, then the KS4 build, then
the estate-wide edge cases), with the frozen-window constraint respected
throughout and gates named per phase. Numbers below are the corrected
(§2.2) totals.

**Phase 0 — the frozen-window ruling (blocking, ask Mide first).**
Get an explicit answer to the question in §4: may a frozen row's *text* (and
its `figure` key, once one exists) be edited in place, keeping id/band/
position untouched? If yes, Phase 1 onward can fix all 28 frozen rows
directly. If no, each frozen row instead needs a same-band replacement
question appended at position ≥ 12, with the frozen original either left
live (duplicating the concept, which is mostly harmless — repetition across
a large bank is not a new fault) or excluded from *auto* composition only (a
bigger, riskier change to `AUTO_POSITIONS`/`bankFor()` logic that this audit
does NOT recommend touching for 28 rows). Effort: a five-minute question to
ask, zero build work.

**Phase 1 — KS3 circuit symbols, motor/field diagrams, and force-arrow
diagrams (highest leverage: existing drawer code, smallest gap).** Covers
P8 (10 confirmed + 5 borderline), P10 (4 + 3), P9 (2 + 1), P4 (2 + 5).
Extract static, referenceable figures from `ks3_art/p8.py`'s `_symbols()`,
`ks3_art/p10.py`'s `r_motor_coil`/`_art_crowd` family, and `ks3_art/p4.py`'s
force-bar instrument — one figure per distinct symbol/diagram these rows
need (resistor, cell/battery, ammeter, voltmeter, variable-resistor
symbols; a two-equal-arrow motor-effect diagram; a two-named-point
bar-magnet field map; a radial single-charge field map; a two-force
addition bar). Register each in the relevant lesson's `LESSON["figures"]`,
then set `"figure"` on each affected `QUESTIONS` row (purely additive — no
id, band or position changes, so it is safe even for the seven frozen
P8/P9/P4 rows if Phase 0 allows it). Estimate: 2–3 days. Gate:
`ks3_figure_sweep.py` plus a manual spot-check that each new figure renders
on the actual question-serving page (not just the lesson page) — confirm
the practice/assignment UI actually displays a `figure` key on a bank row.

**Phase 2 — the KS3 generic-trace and formula-triangle primitive.** Covers
P3 (9 confirmed + 7 borderline, now the largest single KS3 leaf), P6 (4 +
2), P1, B4, B9, B10, C1, C3, C6, C10 (1 confirmed each, several with
borderline siblings), and the three formula-triangle rows in P3/P12. One new
generic line/curve plotter in `ks3_art/kit.py` (a list of (x, y) points, or
a small DSL for "rises then levels off" / "loop" / "flat-then-steep"
shapes) plus one formula-triangle drawer, both reused across every leaf in
this phase. Estimate: 3–4 days (mostly the two new primitives; each
individual figure after that is quick). Gate: same `ks3_figure_sweep.py`.

**Phase 3 — KS4 circuit symbols and electric fields (the single biggest
cluster: 40 confirmed + 11 borderline, 36 of the confirmed in one leaf).**
This is the real build: (a) add a `"figure"` key to the KS4 question record
shape in `ks4_data/__init__.py`'s validator and `load_pool()`/export path
(`export_ks4_questions.py`, and the `ks4_assignment_bank` table/migration if
the column doesn't already exist — check first, don't assume); (b) share
`ks3_art/kit.py`'s primitives directly rather than forking a KS4-specific
kit, plus a **new** small module of KS4 circuit-symbol drawers (resistor,
LED, diode, thermistor, LDR, variable resistor, a.c. supply, motor, buzzer —
a superset of KS3's); (c) confirm/build the actual rendering path on
whatever serves a KS4 assignment/practice question to a student today — this
audit did not verify that path exists or what it expects, and that
verification should happen **before** authoring any figures, since it
determines the record shape. Estimate: 5–7 days, dominated by (c)'s
discovery and the new drawer module. Gate: `ks4_pool_check.py` (extended to
validate the new `figure` field), plus a new drive analogous to
`ks4_pool_drive.py` that actually serves a figure-bearing question and
confirms it renders.

**Phase 4 — KS4 forces, bonding, and the remaining new shapes.** Once
Phase 3's rendering path exists: **forces** (16 confirmed + 12 borderline —
distance-time-graphs reuses the generic line-trace plotter from Phase 2/3;
resolving-forces and free-body-diagrams need the force-triangle drawer
shared with §7.1's formula triangles); **bonding** (3 confirmed + 3
borderline — one new dot-and-cross molecule drawer, parametrised by
formula, covers methane/CO₂/MgO/NH₃/the polyester repeat unit); **the
oscilloscope-trace rows** in electricity/direct-alternating-pd (3 confirmed
+ 2 borderline — reuses the line-trace plotter with a sine-wave preset);
one-off confirmed rows in atomic-structure (nuclide notation), homeostasis
(two unlabelled graphs), and magnetism (solenoid current direction). Every
other borderline-only topic (ecology, inheritance, energy-changes,
resources, magnetism's remaining rows, space, waves' remaining rows,
KS3's B3/B8/C4/C7/C9/P7/P11) can be deferred to ordinary content review
rather than a dedicated phase, since none of them reached CONFIRMED.
Estimate: 4–5 days.

**Phase 5 — the worksheet renderer (backend, separate repo, separate
release).** Once a figure exists for a question (Phases 1–4), the printable
worksheet (`worksheet.js`) needs its own path to draw it: PDF via PDFKit's
native vector API directly (cheap, once the same shape data used for the SVG
figure is available as draw instructions rather than only as an SVG
string), DOCX via a new raster dependency or per-shape hand-built PNGs
(§7.5) — recommend deferring DOCX diagram support to a follow-up ticket
given the dependency decision it requires, and shipping PDF-only diagram
support first if a worksheet needs to go out before DOCX catches up. This
phase is explicitly OUT OF SCOPE for the site-side gates above; it needs its
own gate in the backend repo along the lines of the existing worksheet
tests, extended to assert a figure-bearing question's PDF contains drawn
vector content (not just that it doesn't crash).

**What this plan deliberately does NOT do:** it does not touch
`AUTO_POSITIONS`/the frozen-window composition logic itself (MRB-335 RISKS
D7), does not attempt to retrofit every borderline row (left for ordinary
content review, not a dedicated phase), and does not change any content —
this audit and the plan above are report-only; no file under `ks3_data/`,
`ks4_data/`, `ks3_art/`, or any generator was modified to produce this
report.

## Appendix A — reproducing the counts

Everything in §2–§6 comes from two deterministic scans plus one
non-deterministic step. The deterministic parts: `scan.py` (unchanged in
shape from the first pass, corrected per §2.1 and the topic-label fix noted
at the end of §2.2 — reproduced in full below) produces `all_stems.tsv`
(35,251 rows) and `candidates.tsv` (413 rows, the original net); `wide_net.py`
(§2.2, reproduced in full below) is applied to `all_stems.tsv` and, after
excluding any stem whose text already appears in `candidates.tsv`, produces
`wide_new_candidates.json` (1,938 rows). Both scans only read `ks3_data/`,
`ks4_data/` and the `all_subtopics_*.py` variants via Python import, do no
network or random-order work, and are reproducible byte-for-byte.

The non-deterministic part: 42 parallel Opus examiner passes total (9 over
the original 413, batches of ~46; 33 over the wide net's 1,938, batches of
up to 60), verdicts recorded verbatim in `verdicts/batch_*.txt` and
`wide/verdicts/batch_*.txt` in the scratch directory this audit used — not
checked into this repo. This will vary slightly run to run, which is why
every confirmed/borderline row is listed in full in §5–§6 rather than only
summarised. Two integrity checks anchor the adjudication regardless: (1) the
original 413 candidates were re-attached to the corrected corpus by exact
stem TEXT, not by row position, and the resulting text set was diffed
against the pre-correction set and found identical in both directions
(`old − new = ∅`, `new − old = ∅`); (2) the wide net's candidate set and the
original net's candidate set were diffed and confirmed to have zero
overlap, so the 1,938 new candidates are genuinely new rows, not a
re-slicing of the already-judged 413.

To reproduce both scans:

```bash
cd /Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/mrb342-2-audit
python3 /path/to/scan.py
# prints: total stems scanned (35,251), candidates flagged (413), and a
# per-(key_stage,corpus) breakdown of both. Writes all_stems.tsv and
# candidates.tsv into the script's own directory.
python3 /path/to/wide_net_scan.py
# reads all_stems.tsv and candidates.tsv from the same directory, applies
# the wide net, excludes any stem already in candidates.tsv by exact text,
# and writes wide_new_candidates.json (1,938 rows) plus prints the same
# per-(key_stage,subject,corpus) breakdown used in §2.2 and §3.
```

```python
#!/usr/bin/env python3
"""MRB-342.2 Part 5 — described-diagram audit scan. Read-only.

Walks four corpora (KS3 lesson ladder, KS3 assignment bank, KS4 assignment
bank via ks4_data.load_pool(), KS4 lesson-page quiz via the UNION of all
four tier/pathway variant files per subject, deduplicated by exact stem
text), extracts every question/rung stem with full provenance, and flags
candidates against the original ~80-phrase keyword net (superseded as the
primary net by wide_net.py, §2.2, but kept as part of the union). No file in
the worktree is modified — only Python modules are imported and their data
structures read.

Corrected 23 Sep 2026 (two fixes):
1. The lesson-page quiz scan originally read only the `_triple_higher`
   variant per subject, on the assumption that it is a strict superset of
   the other three variants' quiz content. Measured directly, that holds
   for biology and physics (0 missed) but not chemistry (79 quiz stems
   present in `_triple_foundation`/base and absent from `_triple_higher`).
   Fixed by reading all four variants unconditionally, for every subject.
2. The KS3 ladder's `topic` field used to be read from LESSON["unit"] (a
   descriptive slug/title, e.g. "cells-and-organisation", "Describing
   motion"), while the bank scan below labels the same unit by its CODE
   ("B1", "P3"). Fixed by reading the unit code from the ladder's own file
   path instead, matching the bank's convention.
"""

import importlib
import os
import re
import sys

REPO = "/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/mrb342-2-audit"
sys.path.insert(0, REPO)
os.chdir(REPO)

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

PATTERNS = [
    r"\bis drawn\b", r"\bis shown\b", r"\bare shown\b", r"\bthe diagram shows\b",
    r"\bthe graph shows\b", r"\bthe circuit shows\b", r"\ba rectangle\b",
    r"\ba circle with\b", r"\bthe circle\b", r"\ba zig-?zag\b",
    r"\bthe symbol for\b", r"\bapparatus is set up\b", r"\bapparatus was set up\b",
    r"\bin the diagram\b", r"\bas shown\b", r"\bthe figure\b", r"\bthe trace\b",
    r"\bthe arrow points\b", r"\ban arrow\b", r"\bthe axes\b", r"\bon the axes\b",
    r"\bthe line rises\b", r"\bthe line then\b", r"\ba triangle with\b",
    r"\bthe box marked\b", r"\bboxes marked\b", r"\blabelled [A-Z]\b",
    r"\blabeled [A-Z]\b", r"\bpoint [A-Z]\b", r"\bpoints [A-Z] and [A-Z]\b",
    r"\bthe sketch\b", r"\bthe picture\b", r"\bthe photograph\b",
    r"\bthe image shows\b", r"\bthe image below\b", r"\bbelow shows\b",
    r"\ba beaker sits\b", r"\bis clamped\b", r"\bclamped \d", r"\bclamp stand\b",
    r"\ba ray diagram\b", r"\bthe ray diagram\b", r"\bfood web\b", r"\bfood chain\b",
    r"\bthe cell drawing\b", r"\bthe table shows\b", r"\bthe table below\b",
    r"\ba wire runs\b", r"\bin the wire\b", r"\bthe wire leading\b",
    r"\bconnected in series as shown\b", r"\bconnected in parallel as shown\b",
    r"\bcurved line\b", r"\bstraight line from\b", r"\bdotted line\b",
    r"\bsolid line\b", r"\bshaded region\b", r"\bshaded area\b",
    r"\bthe key shows\b", r"\bkey:\s", r"\bscale drawing\b", r"\bto scale\b",
    r"\bthe pie chart\b", r"\bbar chart shows\b", r"\bthe bar chart\b",
    r"\bpictured\b", r"\billustrated\b", r"\billustrates\b",
    r"\bthe pattern shown\b", r"\bpattern below\b",
    r"\ba wiring diagram\b", r"\bcircuit diagram\b",
    r"\bposition A\b", r"\bposition B\b", r"\bat point A\b", r"\bat point B\b",
    r"\bplotted\b", r"\bplots\b",
    r"\ba force arrow\b", r"\bforce arrows\b",
    r"\bthe cross-section\b", r"\bcross section shows\b",
]

def flag_reason(text):
    hits = []
    for pat in PATTERNS:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            hits.append(m.group(0))
    return hits

ALL_ROWS, CAND_ROWS = [], []

def record(row):
    ALL_ROWS.append(row)
    hits = flag_reason(row["text"])
    if hits:
        row = dict(row)
        row["hits"] = "; ".join(sorted(set(hits)))
        CAND_ROWS.append(row)

def scan_ks3_ladder():
    import ks3_data
    pkg_dir = os.path.dirname(ks3_data.__file__)
    for unit_name in sorted(os.listdir(pkg_dir)):
        unit_path = os.path.join(pkg_dir, unit_name)
        if not os.path.isdir(unit_path) or not re.match(r"^[bcp]\d+$", unit_name):
            continue
        for fname in sorted(os.listdir(unit_path)):
            if not fname.startswith("lesson_") or not fname.endswith(".py"):
                continue
            modname = "ks3_data.%s.%s" % (unit_name, fname[:-3])
            mod = importlib.import_module(modname)
            L = getattr(mod, "LESSON", None)
            if L is None:
                continue
            subject = {"b": "biology", "c": "chemistry", "p": "physics"}[unit_name[0]]
            unit = unit_name.upper()
            for rung in ("recall", "apply", "explain", "produce"):
                r = L.get("ladder", {}).get(rung)
                if not r or "q" not in r:
                    continue
                record({
                    "key_stage": "KS3", "subject": subject,
                    "topic": unit,  # ← corrected, was L.get("unit", "?")
                    "unit": unit, "leaf": L.get("slug", "?"), "corpus": "ladder",
                    "band_or_rung": rung, "bank_position": "",
                    "id": "%s/%s#%s" % (unit, L.get("slug", "?"), rung),
                    "figure": "n/a", "text": r["q"].strip(), "source": modname,
                })

def scan_ks3_bank():
    import ks3_data
    pkg_dir = os.path.dirname(ks3_data.__file__)
    for unit_name in sorted(os.listdir(pkg_dir)):
        unit_path = os.path.join(pkg_dir, unit_name)
        if not os.path.isdir(unit_path) or not re.match(r"^[bcp]\d+$", unit_name):
            continue
        for fname in sorted(os.listdir(unit_path)):
            if not fname.startswith("questions_") or not fname.endswith(".py"):
                continue
            modname = "ks3_data.%s.%s" % (unit_name, fname[:-3])
            mod = importlib.import_module(modname)
            qs = getattr(mod, "QUESTIONS", None)
            if qs is None:
                continue
            subject = {"b": "biology", "c": "chemistry", "p": "physics"}[unit_name[0]]
            for pos, q in enumerate(qs):
                record({
                    "key_stage": "KS3", "subject": subject,
                    "topic": unit_name.upper(),
                    "unit": getattr(mod, "UNIT", unit_name.upper()),
                    "leaf": getattr(mod, "LESSON", "?"),
                    "corpus": "assignment-bank", "band_or_rung": q.get("band", "?"),
                    "bank_position": pos, "id": q.get("id", "?"),
                    "figure": q.get("figure"), "text": (q.get("text") or "").strip(),
                    "source": modname,
                })

def scan_ks4_bank():
    import ks4_data
    cls = ks4_data.classify()
    for q in ks4_data.load_pool(strict=False):
        meta = cls.get(q["subtopic_slug"], {})
        record({
            "key_stage": "KS4", "subject": q["subject"],
            "topic": meta.get("topic", "?"), "unit": meta.get("topic", "?"),
            "leaf": q["subtopic_slug"], "corpus": "assignment-bank",
            "band_or_rung": q["band"], "bank_position": q["bank_position"],
            "id": q["id"], "figure": "n/a (KS4 bank has no figure field)",
            "text": (q.get("text") or "").strip(),
            "source": "ks4_data/questions/%s/*.py" % q["subject"],
        })

VARIANTS = ("", "_higher", "_triple_foundation", "_triple_higher")

def scan_ks4_quiz():
    for subject, varname in (("biology", "BIOLOGY_SUBTOPICS_ALL"),
                              ("chemistry", "CHEMISTRY_SUBTOPICS_ALL"),
                              ("physics", "PHYSICS_SUBTOPICS_ALL")):
        seen_texts = set()
        for variant in VARIANTS:
            modname = "all_subtopics_%s%s" % (subject, variant)
            mod = importlib.import_module(modname)
            for topic, subtopics in getattr(mod, varname).items():
                for st in subtopics:
                    leaf = st.get("id", "?")
                    for i, item in enumerate(st.get("quiz", []) or []):
                        q_text = (item.get("q") or "").strip()
                        if not q_text or q_text in seen_texts:
                            continue
                        seen_texts.add(q_text)
                        record({
                            "key_stage": "KS4", "subject": subject, "topic": topic,
                            "unit": topic, "leaf": leaf, "corpus": "lesson-quiz",
                            "band_or_rung": "quiz-%d" % (i + 1), "bank_position": "",
                            "id": "%s/%s#quiz%d(%s)" % (
                                topic, leaf, i + 1, variant.lstrip("_") or "base"),
                            "figure": "n/a (page quiz has no figure field)",
                            "text": q_text, "source": modname,
                        })

def main():
    scan_ks3_ladder(); scan_ks3_bank(); scan_ks4_bank(); scan_ks4_quiz()
    cols = ["key_stage", "subject", "topic", "unit", "leaf", "corpus",
            "band_or_rung", "bank_position", "id", "figure", "source", "text"]
    with open(os.path.join(OUT_DIR, "all_stems.tsv"), "w", encoding="utf-8") as f:
        f.write("\t".join(cols) + "\n")
        for r in ALL_ROWS:
            f.write("\t".join(str(r.get(c, "")).replace("\t", " ").replace("\n", " ")
                               for c in cols) + "\n")
    cand_cols = cols + ["hits"]
    with open(os.path.join(OUT_DIR, "candidates.tsv"), "w", encoding="utf-8") as f:
        f.write("\t".join(cand_cols) + "\n")
        for r in CAND_ROWS:
            f.write("\t".join(str(r.get(c, "")).replace("\t", " ").replace("\n", " ")
                               for c in cand_cols) + "\n")
    print("Total stems scanned: %d" % len(ALL_ROWS))
    print("Candidates flagged:  %d" % len(CAND_ROWS))

if __name__ == "__main__":
    main()
```

**`wide_net.py`** — the net that replaced the phrase list above as the
primary net (§2.2). Applied to every row already written to `all_stems.tsv`
by the script above:

```python
#!/usr/bin/env python3
"""wide_net.py — built on the actual tell (refers to a visual artefact that
is not there) rather than on a list of remembered phrases. Union of the
original PATTERNS from scan.py (kept — costs nothing, catches a few things
the categories below don't explicitly name, e.g. "food chain") plus new
category-based patterns.
"""
import re
from scan import PATTERNS as OLD_PATTERNS  # the list reproduced above

NEW_PATTERNS = [
    # artefact nouns, bare and unqualified
    r"\bdiagrams?\b", r"\bgraphs?\b", r"\bcharts?\b", r"\bfigures?\b",
    r"\bsketch(es|ed)?\b", r"\bimages?\b", r"\bpictures?\b", r"\bphotographs?\b",
    r"\btraces?\b", r"\bplots?\b", r"\bplotted\b", r"\bplotting\b",
    r"\bcircuits?\b", r"\baxis\b", r"\baxes\b", r"\bscale drawings?\b",
    r"\bpyramid of (biomass|numbers)\b", r"\bfood webs?\b", r"\btables?\b",

    # depiction verbs
    r"\b(is|are|was|were)\s+(drawn|shown|plotted|marked|labelled|sketched)\b",
    r"\bdraws?\b", r"\bdrawn\b", r"\blabelled\b", r"\blabeled\b", r"\bshown\b",

    # visual primitives
    r"\barrows?\b", r"\bsymbols?\b", r"\brectangles?\b", r"\btriangles?\b",
    r"\bcircles?\b", r"\bsquares?\b", r"\bzig-?zags?\b",
    r"\b(dotted|solid|curved|straight)\s+lines?\b",

    # deixis to a page position, near a showing verb, either order
    r"\b(above|below|opposite|left|right)\b[^.]{0,20}\b(shows?|shown|drawn)\b",
    r"\b(shows?|shown|drawn)\b[^.]{0,20}\b(above|below|opposite|left|right)\b",

    # apparatus
    r"\bapparatus\b", r"\bclamp(ed|s)?\b", r"\btripods?\b", r"\bgauzes?\b",

    # labelled points
    r"\b(point|position|box|branch)\s+[A-Z]\b",

    # instrument readings
    r"\bthe needle\b", r"\bthe pointer\b", r"\breading on the\b",
]

PATTERNS = OLD_PATTERNS + NEW_PATTERNS


def flag_reason(text):
    hits = []
    for pat in PATTERNS:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            hits.append(m.group(0))
    return hits
```

**Driving script** (loads `all_stems.tsv`, excludes anything already in
`candidates.tsv` by exact text, writes `wide_new_candidates.json`):

```python
import csv, json, sys
sys.path.insert(0, '.')
from wide_net import flag_reason

all_rows = list(csv.DictReader(open('all_stems.tsv'), delimiter='\t'))
old_texts = set(r['text'] for r in csv.DictReader(open('candidates.tsv'), delimiter='\t'))

new_cands = []
for r in all_rows:
    if r['text'] in old_texts:
        continue
    hits = flag_reason(r['text'])
    if hits:
        r2 = dict(r); r2['hits'] = '; '.join(sorted(set(hits)))
        new_cands.append(r2)

json.dump(new_cands, open('wide_new_candidates.json', 'w'), indent=1)
print("never-adjudicated (new) candidates:", len(new_cands))
```

## Appendix B — the Opus adjudication method

**Pass 1 (original 413 candidates, 23 Sep 2026 morning).** Split into 9
batches of ~46 rows each, no provenance or matched-keyword shown to the
examiner to avoid biasing the ruling. Each batch sent to a separate Opus
agent in parallel with the rule and the do/don't-flag examples from §1,
asked to rule CONFIRMED / BORDERLINE / REJECTED with a one-line reason per
row. All 413 rows returned a verdict.

**Pass 2 (wide net's 1,938 new candidates, 23 Sep 2026 afternoon).** Split
into 33 batches of up to 60 rows each, same no-provenance presentation. The
brief was **tightened** before this pass, based on the coordinator's
prediction that a wide net finds mostly convention questions: every batch
opened with an explicit warning that it was flagged by "a deliberately very
wide keyword net… the large majority of these rows will be REJECTED. Read
carefully — do not let the presence of a trigger word bias you toward
CONFIRMED," and the REJECT-example list was extended with the four
convention-question examples now in §1 (genetic-diagram purpose, free-body
arrow-length meaning, dot-and-cross convention ×2), given verbatim so the
examiner would recognise the shape rather than have to infer it. All 1,938
rows returned a verdict; the result (67 CONFIRMED / 63 BORDERLINE / 1,808
REJECTED — 93.3% rejected) matches the prediction that motivated the
tightening.

Verdicts were merged back onto the full provenance record by row id (within
each pass) and then combined across passes by joining on exact stem text
(§2.2) to produce the combined 2,351-row judged set, from which every count
and list in this report was computed. The merge scripts (`merge.py`,
`merge_wide.py`) are mechanical — a regex over `ROW <n>: <VERDICT> —
<reason>` lines joined on row id or stem text — and are not reproduced here.
