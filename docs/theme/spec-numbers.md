# Spec section numbers: Combined 8464 vs separate-science 8462/8463

## Purpose

Every KS4 lesson header currently shows a single AQA spec section number,
taken from Combined Science: Trilogy (8464), regardless of whether the
student viewing the page is on the Combined pathway or the Triple/separate
Science pathway. That is wrong for Triple pupils: their own spec (8462
Chemistry or 8463 Physics) is numbered independently by AQA and its section
numbers do not reliably match 8464's, even though — for the specific 14
lessons audited here — they turn out to follow the same "chapter.2.x"
pattern by coincidence, not by rule.

This document exists to feed the ruling on a **route-aware spec number**:
show 8464's number to a Combined-pathway reader and the matching 8462/8463
number to a Triple-pathway reader, for the same lesson. Every row below was
verified by reading the actual AQA specification PDF text (via
`pdftotext -layout`), matching sections by their content and heading text —
never by assuming a numeric pattern — per the brief's warning that a prior
Design delivery got two citations wrong in ways that did not follow any
simple pattern (a topic-over section number, and a required-practical
number swapped for a different RP).

**Headline finding: for all 14 lessons in this pilot, the "chapter.2.x"
pattern (Combined `5.2.x` ↔ Chemistry `4.2.x`; Combined `6.2.x` ↔ Physics
`4.2.x`) held exactly, once verified against the real heading text and
content of both documents, sub-point for sub-point.** This was checked, not
assumed — see the "How this was verified" section below — but it means the
separate-science number for 13 of the 14 lessons can be produced by a
mechanical rule (drop the leading chapter digit, replace with `4`). The one
exception is **nanoparticles**, which has **no Combined 8464 equivalent at
all** (it is Chemistry-only / Triple-only content), so no route-aware
substitution is possible there — the Combined route simply has no page for
this lesson today, which the build already reflects.

## Sources read

| Spec | URL | Version stamp (from the PDF footer) |
|---|---|---|
| 8462 GCSE Chemistry | `https://filestore.aqa.org.uk/resources/chemistry/specifications/AQA-8462-SP-2016.PDF` | Version 1.1, 04 October 2019 |
| 8463 GCSE Physics | `https://filestore.aqa.org.uk/resources/physics/specifications/AQA-8463-SP-2016.PDF` | Version 1.1, 30 September 2019 |
| 8464 Combined Science: Trilogy | `https://filestore.aqa.org.uk/resources/science/specifications/AQA-8464-SP-2016.PDF` | Version 1.1, 04 October 2019 |

All three URLs given in the brief resolved (HTTP 200, valid PDFs). Each was
converted with `pdftotext -layout` and read as text; page numbers below are
the spec's own **printed page number** (the footer "Visit aqa.org.uk/8462
for the most up-to-date specification… *NN*"), which lines up with the PDF's
physical page count in all three documents (no cover-page offset to correct
for).

## The table

| Site slug | Lesson title | Combined 8464 number + title | Separate-science number + title | Citation |
|---|---|---|---|---|
| chemical-bonds | Chemical bonds | **5.2.1.1** "Chemical bonds" (p.76) | **8462 4.2.1.1** "Chemical bonds" (p.26) | 8462 PDF, p.26; 8464 PDF, p.76 — headings and body text identical between the two specs |
| ionic-bonding | Ionic bonding | **5.2.1.2** "Ionic bonding" (p.76) | **8462 4.2.1.2** "Ionic bonding" (p.27) | 8462 PDF, p.27; 8464 PDF, p.76 |
| ionic-compounds | Ionic compounds | **5.2.1.3** "Ionic compounds" (p.77) | **8462 4.2.1.3** "Ionic compounds" (p.27–28) | 8462 PDF, p.27–28; 8464 PDF, p.77 |
| covalent-bonding | Covalent bonding | **5.2.1.4** "Covalent bonding" (p.78) | **8462 4.2.1.4** "Covalent bonding" (p.29) | 8462 PDF, p.29; 8464 PDF, p.78 |
| metallic-bonding | Metallic bonding | **5.2.1.5** "Metallic bonding" (p.79) | **8462 4.2.1.5** "Metallic bonding" (p.30) | 8462 PDF, p.30; 8464 PDF, p.79 |
| states-of-matter | States of matter | **5.2.2.1** "The three states of matter" (p.80) | **8462 4.2.2.1** "The three states of matter" (p.31) | 8462 PDF, p.31; 8464 PDF, p.80. Note: AQA's actual heading is "**The** three states of matter" — the site's shorter title is fine, but flagging in case the header ever quotes AQA's heading verbatim |
| properties-ionic-compounds | Properties of ionic compounds | **5.2.2.3** "Properties of ionic compounds" (p.81) | **8462 4.2.2.3** "Properties of ionic compounds" (p.32) | 8462 PDF, p.32; 8464 PDF, p.81 |
| properties-small-molecules | Properties of small molecules | **5.2.2.4** "Properties of small molecules" (p.81) | **8462 4.2.2.4** "Properties of small molecules" (p.32) | 8462 PDF, p.32; 8464 PDF, p.81 |
| polymers | Polymers | **5.2.2.5** "Polymers" (p.82) | **8462 4.2.2.5** "Polymers" (p.33) | 8462 PDF, p.33; 8464 PDF, p.82 |
| giant-covalent-structures | Giant covalent structures | **5.2.2.6** "Giant covalent structures" (p.82) | **8462 4.2.2.6** "Giant covalent structures" (p.33) | 8462 PDF, p.33; 8464 PDF, p.82 |
| metals-alloys | Metals and alloys | **5.2.2.7** "Properties of metals and alloys" **+ 5.2.2.8** "Metals as conductors" (both p.82) | **8462 4.2.2.7** "Properties of metals and alloys" **+ 4.2.2.8** "Metals as conductors" (both p.33) | 8462 PDF, p.33; 8464 PDF, p.82. Both numbers carry straight across, sub-point for sub-point |
| nanoparticles | Nanoparticles | **NO EQUIVALENT** — confirmed absent from the 8464 spec entirely (searched the full text for "nanopartic" and for "4.2.4"/"5.2.4"; zero hits) | **8462 4.2.4** "Bulk and surface properties of matter including nanoparticles **(chemistry only)**" — split into **4.2.4.1** "Sizes of particles and their properties" (p.35) and **4.2.4.2** "Uses of nanoparticles" (p.36) | 8462 PDF, p.35–36. **The site's current "4.2.4" is already the correct, verified 8462 number** — no change needed there. See flag below |
| series-parallel-circuits | Series and parallel circuits | **6.2.2** "Series and parallel circuits" (p.131) | **8463 4.2.2** "Series and parallel circuits" (p.27) | 8463 PDF, p.27; 8464 PDF, p.131 |
| resistors | Resistors and I-V characteristics | **6.2.1.4** "Resistors" (p.130) | **8463 4.2.1.4** "Resistors" (p.26–27) | 8463 PDF, p.26–27; 8464 PDF, p.130. Note: AQA's own heading in both specs is just "**Resistors**" — the site's longer title ("…and I-V characteristics") is descriptive, not AQA's wording; doesn't affect the number |

## Flags for human review

1. **Nanoparticles has no Combined-route page, and that's correct, not a
   bug.** Content unique to 8462 §4.2.4 does not exist anywhere in 8464.
   There is no "Combined number" to show a Combined-pathway reader for this
   lesson because AQA never asked a Combined-pathway student to learn it —
   confirm the build already skips generating a Combined page for this
   slug (the brief states this is already the case) and that any
   route-aware header logic has an explicit "Triple-only, no Combined
   number" branch rather than falling through to a blank or a wrong
   number.

2. **Required-practical numbers differ between the two specs for the two
   electricity lessons — a real trap of exactly the shape the brief warned
   about.** The *content* of RP3/RP4 (separate Physics 8463) is identical
   to RP15/RP16 (Combined 8464) — same practical, same wording — but the
   **numbers are not the same**: separate Physics numbers its own 8
   required practicals 1–8, while Combined 8464 numbers all 21 combined-
   science required practicals 1–21 in one continuous sequence. This
   wasn't asked for in the table (which only covers spec **section**
   numbers), but if any lesson page also displays a "Required practical
   N" label, that label needs the same route-aware treatment as the
   section number — hard-coding one spec's RP number for both routes would
   reproduce the exact kind of Design-delivery error the brief flagged
   (a required practical cited under the wrong number).

3. **Two lesson titles on the site are AQA-adjacent but not AQA's literal
   heading wording:** "States of matter" (AQA: "The three states of
   matter") and "Resistors and I-V characteristics" (AQA: "Resistors").
   Neither affects the section *number*, so neither blocks this ruling,
   but flagging in case a future pass wants headers to quote AQA's heading
   text verbatim alongside the number.

4. **No low-confidence matches in this batch.** Every one of the 14
   mappings above was confirmed by reading matching heading text and
   near-identical body content in both specs side by side (the wording of
   8462/8463's content statements is, section for section, the same
   prose AQA also placed in 8464 — AQA writes the shared content once and
   reuses it under each spec's own numbering scheme). None required a
   judgement call between two plausible sections.

## How this was verified (method, not just conclusion)

For each spec, the PDF was fetched, converted with `pdftotext -layout`, and
grepped for its own numbered heading pattern (`^N\.N\.N` etc.) to build a
complete list of section headings in that spec's own numbering — not by
searching for the Combined number and assuming the separate spec would use
the same digits. For 8462, this produced the full run
4.2 → 4.2.1.1…4.2.1.5 → 4.2.2.1…4.2.2.8 → 4.2.3.1…4.2.3.3 → 4.2.4.1…4.2.4.2,
which was then matched heading-by-heading against 8464's 5.2 run, and
similarly for 8463's 4.2 Electricity run against 8464's 6.2 run. Only after
independently building both lists were they compared — at which point they
turned out to line up one-for-one for this particular pair of topics (KS4
"Bonding, structure and properties of matter" and "Electricity"). That
correspondence is reported here as a **verified finding for these 14
lessons specifically**, not as a general rule for the rest of the spec —
the brief's example of Design's team misciting "4.10.4.x" for "4.10.3.x"
concerns a different topic area entirely, and nothing here should be read
as evidence that pattern holds anywhere outside this batch.

## Commander's check of the two extended citations (27 Sep 2026)

Decision 4 of the build report said the extended ranges on `states-of-matter`
and `giant-covalent-structures` were mapped by the digit-drop rule rather than
looked up. They have now been looked up, by heading text, in the same three
PDFs (`pdftotext -layout`, line numbers in the extracted text):

| 8464 | heading | 8462 | heading |
|---|---|---|---|
| 5.2.2.2 (l.3584) | State symbols | 4.2.2.2 (l.1225) | State symbols |
| 5.2.3 (l.3695) | Structure and bonding of carbon | 4.2.3 (l.1336) | Structure and bonding of carbon |
| 5.2.3.1 (l.3696) | Diamond | 4.2.3.1 (l.1337) | Diamond |
| 5.2.3.2 (l.3712) | Graphite | 4.2.3.2 (l.1353) | Graphite |
| 5.2.3.3 (l.3729) | Graphene and fullerenes | 4.2.3.3 (l.1375) | Graphene and fullerenes |

Every number shown on a Triple page is therefore now a looked-up citation.

## D13 update (theme-run audit, 27 Sep 2026) — Combined now names its own spec too

Everything above this section is unchanged and still the citation record —
every number in the table is still correct. What changed is presentation,
not citation: **the Combined side of all 13 Combined-route lessons now
shows "(8464)" in the eyebrow and key note**, in the same position the
Triple side has always shown "(8462)"/"(8463)". Before this, a Combined
pupil saw a bare section number ("AQA Chemistry 5.2.1.1") with no spec
code at all, while a Triple pupil on the very same lesson saw one ("AQA
Chemistry (8462) 4.2.1.1") — inconsistent, and the kind of asymmetry an
independent audit (not this document's own author) caught live. The fix
is in `build_ks4.SPEC_TEXT`'s "combined" values; `ks4_rulings.
apply_r14_spec_number` itself is unchanged (it still just finds Design's
original literal and swaps in the `{{ specEyebrow }}`/`{{ specNote }}`
placeholder — `build_ks4.compile_lesson()` now derives that original
literal by stripping "(8464) "/" (8464)" back out of `SPEC_TEXT`'s new
value, rather than storing the pre-8464 text a second time).

**Nanoparticles' flag above — "the site's current '4.2.4' is already the
correct, verified 8462 number — no change needed there" — is superseded,
not wrong.** The section number was, and remains, correct. What it lacked
was the SAME thing every other lesson lacked before this run: the spec
CODE beside the number. `ks4_rulings.apply_r5_nanoparticles_spec` (was
`check_r5_nanoparticles_spec`, a no-op assertion; now a real rewrite) adds
"(8462)" to both the eyebrow and the `Ks4KeyNote` `spec=` attribute, in the
same position its 13 combined/triple siblings carry their own code. The
tutor's context string picks up the same code for nanoparticles via a
small dedicated branch in `build_ks4.tutor_block()` (nanoparticles is the
one lesson outside `SPEC_TEXT`, so it cannot read the code from there the
way every other lesson's tutor context does).

Proof this moved nothing else: `build_ks4.extract_freeze_pieces()` was
diffed before/after on all 54 pages — only the two eyebrow/keynote strings
(and, on the 12 Combined-route lessons plus nanoparticles' tutor context,
the derived spec text fed to the template) differ; `ks4_lessons/
frozen.json` was re-stamped with `python3 build_ks4.py --freeze` afterward.
