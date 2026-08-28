# Cross-unit computations — commander's own pass — 28 Aug 2026

Everything here is computed FROM DATA across all 70 physics lessons (or all 83
physics HTML files where stated), not sampled and not inferred from a unit
auditor's summary. No single unit auditor can see the estate, so these belong
here rather than in a `p<N>.md`. Method is given per item so the cold
double-checker can recompute.

## Preamble facts (verified at run start)

| Fact | Value | Method |
|---|---|---|
| Commit audited | `38fb338308d3a25f9cd6596afdbce20dc8af9921` | `git rev-parse HEAD` after `--ff-only` to `origin/main`; tree clean |
| Branch | `feat/content-phys` (fast-forwarded; was 6 behind at session start) | `git rev-list --left-right --count` |
| Physics units | 12 (P1–P12) | `ks3_data/physics_p*_*.py` |
| Physics lessons | **70** | `ks3_data/p*/lesson_*.py` = 70; built non-index HTML = 70. Both agree; matches the brief's figure |
| Physics HTML files served | 83 (70 lessons + 12 unit indexes + 1 subject index) | `find mrbadmus_site/ks3/physics -name '*.html'` |
| Live-vs-local parity | **83 / 83 byte-identical** | SHA-256 of every file vs `curl -sL https://mrbadmus.com/ks3/physics/...`; 0 differ |
| Free disk at start | 11 GiB | `df -h .` |
| Posture | read-only; no build, no DB write, no account | — |

⚠️ Parity method note: the `.html` URL 308-redirects to the extensionless form.
`curl` WITHOUT `-L` returns an empty body and hashes to
`e3b0c44298fc1c14…` (the SHA-256 of the empty string) for every page, which
looks like a total mismatch. The sweep used `-L`. Anyone re-running this must
too.

## Assignment-bank / DB pools — physics row counts (pre-ruled: counts only)

Read-only `execute_sql` against production ref `urklkrwevjtlfbwnipjn`.

| Pool | Physics rows | Total rows | Units present |
|---|---|---|---|
| `ks3_assignment_bank` | **0** | 1356 | B1–B11, C1–C10 only |
| `ks3_ladder_questions` | **0** | 226 | B1–B11, C1–C10 only |
| `ks3_cards` | **0** | 612 | B1–B11, C1–C10 only |

Physics is absent from all three database pools. The brief scoped the bank to
counts only and this record respects that — no bank content is audited, because
for physics there is none.

**This is a September-readiness fact, not a lesson defect.** The lesson-page
ladder is baked into the page by `build_ks3.py` and performs no runtime pool
read (CLAUDE.md, MRB-288), so **the 70 lesson pages are unaffected and work
fully**. What does not exist for physics is anything downstream of the pools:
a weekly assignment cannot be composed from a physics unit, and the dashboard
flashcard round has no physics cards. Biology and chemistry both have all three.
Whether that is intended for September is Mide's call — it is in the Mide pile,
not scored as a finding against any unit.

## SYS-1 · "Next in this unit" heading lying about `references` — **ABSENT IN PHYSICS**

Chemistry's widest defect (~23 lessons over 6 units, sending students backwards,
cross-unit, and in two cases into biology). Computed across all 70 physics
lessons:

- `connects_heading` is authored **nowhere** in `ks3_data/p1..p12` — 0 of 70
  lessons override it.
- `build_ks3.py:4389` falls back to `"Connects to"` when the key is absent.
- The built pages agree: **0 occurrences of the string "Next in this unit"** in
  any of the 83 physics HTML files. Every lesson that emits the card emits
  **"Connects to"**.

Method: `grep -o 'Next in this unit\|Connects to\|Where to next\|Before this
lesson' -r mrbadmus_site/ks3/physics`.

So the heading is honest even where the reference genuinely is cross-unit — and
in physics it very often is by design (P4's lessons reference P5's
`pressure-force-over-area`; P12's reference P4 and P7; P11's reference C1). The
one that would have been chemistry's worst case — **P4 `moments` references
`biomechanics-forces-in-the-body`, a biology lesson** — is safe *because* the
heading does not claim it is next in the unit. Under chemistry's heading it
would have been the same defect as c7-03.

**No action. Recorded because "not found" is worth having**, and because it
means chemistry's SYS-1 fix must not be applied blind across the estate: the
physics half is already correct and a mechanical sweep could regress it.

## Energy stores vs transfers — the AQA model — **HELD CLEANLY ACROSS PHYSICS**

Mide named this in the brief as a primary hunt. Swept all 83 physics HTML files
for the vocabulary that signals the model has slipped:

| Phrase | Hits across all physics |
|---|---|
| "types of energy" / "type of energy" | **0** |
| "forms of energy" | **0** |
| "heat energy" | **0** |
| "energy is lost" | **0** |
| "energy is used up" | **0** |
| "transformed into" | **0** |
| "converted into" | 1 — and it is a **negation** |

The single "converted into" is in `light/why-things-look-coloured.html`,
confronting a misconception: *"The energy that does not come out has not been
converted into red — it has been absorbed by the filter."* Correct usage.

Store/pathway vocabulary concentrates exactly where it should: `energy-transfers`
196 hits, `energy-at-home` 46, then a long tail; `describing-motion`, `pressure`,
`space` and `static-electricity` use it not at all, which is right for their
topics.

Method: `grep -roi "<phrase>" mrbadmus_site/ks3/physics`.

**No action. This is a headline positive** — the single most common way a KS3
physics course goes wrong is absent from all 70 lessons. Unit auditors were
still asked to check it per-lesson at sentence level, since a page can hold the
right vocabulary and still teach "energy is a substance"; their findings govern
where they contradict this sweep, which only proves the words are clean.

## `g` — cross-unit consistency — **CLEAN, with an exemplary convention note**

| Value | Occurrences |
|---|---|
| `10 N/kg` | 49 |
| `9.81 N/kg` | 1 |

The lone `9.81` is not drift. It is in `space/gravity-and-weight.html`, from an
authored `convention_note` (`ks3_data/p12/lesson_01_gravity_and_weight.py:700`)
that states the bench's surface values (Earth 10.0, Moon 1.6, Mars 3.7, Jupiter
24.8 N/kg), records that *"Earth's true mean value is 9.81 N/kg and varies by
about 0.5% between the poles and the equator; 10 is the figure used throughout
KS3"*, and notes Jupiter's figure is quoted at the cloud tops because Jupiter
has no surface. The lesson file's own comment marks `g = 10 N/kg` as statutory
under `KS3.P.SPACE.01`.

Seven files state a `g` value, spanning three units (P4 forces, P5 pressure,
P12 space) — all `10 N/kg`.

**No action.** Flagged here as the model the SYS-6 family wants: an admitted
simplification confessed where the number is, rather than left to be discovered
as an inconsistency. It is the same template chemistry's C10 auditor named
(c10-05's always-visible distortion footer).

## Weight given in kilograms — **NONE FOUND**

Swept for `weight (of|is|=) <number> (kg|kilogram)`. One regex hit, and it is a
false positive: `pressure/pressure-force-over-area.html` reads *"The weight is
4 kg × 10 N/kg"* — mass times field strength, giving 40 N, which is correct and
is the FIFA-style insert line. Left to P5's auditor to judge the phrasing in
context (a picky reader could stop at "the weight is 4 kg"); not scored here.

Method: `grep -roiE "weight (of|is|=)? ?[0-9.,]+ ?(kg|kilogram)"`.

## "Current gets used up" — swept, **all hits are confrontations**

26 hits of "used up" across physics. Inspected: they are the misconception
blocks and key notes that KILL the idea, not instances of it —
`electric-circuits/current-and-circuits.html` carries
`data-activity="think-nothing-used-up"`, and `energy-transfers/energy-stores.html`
states *"Energy is never used up or created."* P8's and P1's auditors verify at
sentence and instrument level, including whether any ammeter reading in any
bench state contradicts the text; this sweep only establishes that the phrase
appears in physics solely as a target.

## Open at time of writing

Per-unit records land in `records/p1.md` … `records/p12.md`. SYS-2, SYS-3, SYS-5
and SYS-8 are engine-level and are probed per unit rather than computed here,
because each needs a driven page rather than a grep.

## AI faff and slop — swept by name across all 70 lessons — **ESSENTIALLY ABSENT**

Mide named the phrases to hunt. Swept all 83 physics HTML files for 29 of them
(`let's dive in`, `dive into`, `in today's lesson`, `we will explore`, `great
job`, `well done!`, `fantastic`, `awesome`, `you've got this`, `buckle up`,
`let's get started`, `it's important to note`, `in conclusion`, `to sum up`,
`at the end of the day`, `unlock`, `delve`, `realm`, `tapestry`, `crucial`,
`vital to understand`, `fundamental concept`, and others).

**Every one returns 0 hits** except `journey` (39). Its distribution shows it is
domain vocabulary, not filler: `describing-motion` 19, `waves-and-sound` 11,
`space` 6 — a journey on a distance–time graph, a sound's journey to the
reflector, light's journey. P3, P6 and P12's auditors judge it in context.

Method: `grep -roi "<phrase>" mrbadmus_site/ks3/physics` per phrase.

**No action.** For a 70-lesson estate this is an unusually clean result and it
should be said plainly in the headline: the physics writing does not read as
generated.

## Meta-text (platform self-explanation) — **1 borderline instance in 70 lessons**

Swept 16 meta-text patterns (`this website`, `this platform`, `click the button
below`, `scroll down`, `the simulation below`, `by the end of this lesson`,
`learning objective`, `success criteria`, …). All return 0 except `this page`
(7) — and 6 of the 7 are the page as a **physical object**, which is good
teaching, not meta:

- `energy-transfers/radiation.html` ×2 — *"Everything above absolute zero emits
  it — you, this page, a block of ice"*
- `forces/non-contact-forces.html` — *"Acts between anything with mass — you and
  the Earth, the Earth and the Moon, you and this page."*
- `space/gravity-earth-moon-and-sun.html` — *"Every object in the universe is
  pulling on every other object, including you and this page."*
- `waves-and-sound/hearing-and-auditory-range.html` — *"Every range on this page
  is an approximate figure for a typical healthy adult of that species…"*
  (a convention note, not platform meta)

The seventh is borderline and is the only candidate:
`forces/what-a-force-is.html` — *"The job on this page is to get into the habit
of naming both ends of it, and giving its size in newtons."* This is lesson
framing rather than platform self-explanation, and it is doing pedagogical work
(it states the lesson's demand). Referred to P4's auditor and to the
double-checker rather than scored here; if it is called, it is S4, one clause,
Code.

## Reading load — measured, per unit, per lesson

⚠️ **Method correction, recorded deliberately.** A first attempt stripped all
HTML tags and split on sentence punctuation. It reported a mean of 20.1 words
and "sentences" of up to 232 words. Those were artefacts: MCQ option lists and
bench control labels are separate block elements with no terminal punctuation,
so tag-stripping concatenates them into one pseudo-sentence. **Those numbers are
withdrawn and appear nowhere in this report.** The figures below come from
`<p>` elements only, excluding option/label/gauge/dial/chip/readout/eyebrow/
crumb/trail/score/button classes — i.e. prose a student actually reads as
prose. Anyone re-running this must exclude the control chrome or they will
reproduce the wrong answer.

**Whole estate: 92,585 prose words over 70 lessons = 1,322 words per lesson.
Mean sentence 15.9 words, median 13, p90 30.** For ages 11–14 that is a sound
target and most of the estate sits comfortably inside it.

Per unit, normalised per lesson (the fair comparison — P6 has 9 lessons, P9 has 3):

| Unit | Lessons | Words/lesson | >30-word sentences per lesson | >40-word per lesson |
|---|---|---|---|---|
| **P10 magnetism** | 5 | **1450** | **12.2** | **5.2** |
| P5 pressure | 4 | 1551 | 8.5 | 4.0 |
| P9 static electricity | 3 | 1317 | 10.7 | 3.7 |
| P6 waves and sound | 9 | 1447 | 9.4 | 3.6 |
| P7 light | 7 | 1372 | 10.9 | 3.1 |
| P4 forces | 9 | 1374 | 9.1 | 1.9 |
| P8 electric circuits | 7 | 1513 | 9.0 | 1.9 |
| P12 space | 6 | 1322 | 6.3 | 1.8 |
| P2 energy at home | 5 | 1023 | 4.0 | 1.6 |
| P1 energy transfers | 8 | 1092 | 5.0 | 1.1 |
| P11 matter | 4 | 1261 | 5.8 | 1.0 |
| P3 describing motion | 3 | 911 | 2.0 | 0.3 |

**The spread is the finding: P10 carries 17× describing-motion's rate of
very-long sentences.** P10 is also the newest unit (built 25 Aug 2026) and the
one with the least classroom exposure. P5 and P9 are next, and both are short
units carrying dense convention notes.

Inspecting the 152 prose sentences of 42+ words shows what they mostly are:
**honesty footers and convention notes** — the bench's modelling assumptions,
what a figure is rounded from, why a number is not given in newtons. That is the
good pattern (it is exactly the c10-05 template chemistry's auditors named), but
it is written at teacher register on a student page. Examples, verbatim:

- 67w · `static-electricity/forces-between-charges.html` — *"Both charges are
  treated as equal in size and as sitting at the centre of each sphere, and the
  strength is reported as a relative figure with the closest fully charged case
  set to 100 — no force in newtons is given anywhere on the bench, because the
  equation for it is beyond this stage and any number in newtons here would be
  invented rather than measured."*
- 62w · `magnetism-and-electromagnetism/electromagnets.html` — *"The number of
  paper clips is worked out from a simple rule in which the field goes up in
  proportion to the turns and to the current, and an iron core multiplies it by
  a fixed factor of twenty-five; a real core's multiplication depends on the
  iron and falls away sharply once the iron saturates, so the largest numbers
  here are optimistic."*
- 60w · `magnetism-and-electromagnetism/the-earth-is-a-magnet.html` — *"The
  magnetic axis is tilted about eleven degrees from the spin axis, so magnetic
  latitude and geographic latitude are not the same and dip measured in the
  field differs from the figure here by several degrees in most places…"*

**Proposed solution (cross-unit, S2):** keep every one of these notes — they are
the estate's integrity and deleting them would be a regression. Split them at
the semicolons and em-dashes into two or three sentences each, which costs
nothing and halves the load; and consider a consistent visual treatment that
marks a convention note as *for reference, not for reading now*, so a struggling
Year 7 knows they may pass it. Start with P10, P5 and P9, which carry the
heaviest rates. **Who fixes: Code, wording past Mide. Effort: medium (152
sentences, mechanical, no science changes).**

## Safeguarding text — present where expected

`waves-and-sound/hearing-and-auditory-range.html` carries the Childline line
(*"free, confidential and open at any hour, on 0800 1111, and you do not have to
give your name"*) and `magnetism-and-electromagnetism/magnets-and-poles.html`
carries swallowed-magnet guidance naming a pharmacist, GP, 111, the school nurse
or any member of staff. Both are RULED SLOTS (the P10 build of 25 Aug placed the
Childline text "character for character in the ruled slot"). **Recorded as
present and untouched. No auditor drafts or amends safety wording** — per unit
findings go to the Mide pile.

## Unit symbols and UK conventions — **CLEAN across all 70 lessons**

Swept every unit symbol and spelling that physics estates normally get wrong.
Raw `grep -F` counts throw false positives on substrings, so every suspect was
re-checked against **rendered text** (tags stripped, `<script>`/`<style>`
removed, word boundaries enforced). Findings after that second pass:

| Checked | Result |
|---|---|
| `Ω` for resistance | 72 uses; `Ohms` 0. Clean (` ohms` 50 is the word in prose, correct) |
| `N m` for moment | 26; **`Nm` 0** — the run-together form never appears |
| `m/s` for speed | 227; `ms-1` 0; "meters per second" 0 |
| `Hz` | 92; `Hertz` **0 in rendered text** |
| `Pa` | 160; `Pascal` 1 — and it is sentence-initial (*"Pascals are newtons per square metre"*), correct |
| `kWh` | correct form only; lowercase `kwh` **0 in rendered text** (markup attributes only) |
| `Watts` / `Joules` capitalised | 4 + 2, **all sentence-initial**, correct |
| US spellings (`liter`, `color`, `center`, `aluminum`, `traveling`, `modeling`) | **0 each** |
| `sulphur` | 0 (correct — UK science uses "sulfur") |

**The one apparent US spelling is not one, and it is evidence of unusual care.**
`grep` finds "meter" 344 times raw / 55 in rendered text. Every rendered instance
is the **instrument** — *"A meter in the wrong place does not give you a wrong
reading. It gives you a different circuit"*, *"the two meters are opposites"*,
ammeter, voltmeter. Meanwhile the **unit** of moment is written "newton metre"
15 times. The single "newton meter" is in
`forces/springs-and-hookes-law.html` and is the spring-balance **device**
(*"A newton meter has a scale of equally spaced marks alongside its spring"*).

That is the correct UK distinction — a *metre* is a length, a *meter* measures
something — held consistently across 70 lessons written by different runs.

**No action.**

Also noted while sweeping, as the answer to a risk this audit was briefed to
hunt: `energy-at-home/calculating-energy-transferred.html` carries an explicit
legal-pairings note — *"watts × seconds gives joules; kilowatts × hours gives
kilowatt-hours. Watts × minutes is always wrong."* — and a key note *"Convert
the time on the Insert line, not afterwards."* P2's auditor judges whether the
scaffolding around it fades properly; the unit discipline itself is present and
correct.

## Ordering and prerequisites — computed against the REAL delivery order

⚠️ **The physics units are NOT taught in P1→P12 order, and any prerequisite
check that assumes they are is wrong.** The published default sequence
(`ks3_data/default_sequence.py`, `half_terms.py` — Mide's ruling of 26 Jul 2026)
interleaves all 33 KS3 units across three years. Physics lands:

| Year | Physics units, in order |
|---|---|
| **Y7** | P3 describing motion → P4 forces → P11 matter and the particle model |
| **Y8** | P5 pressure → P1 energy transfers → P6 waves and sound → P7 light → P8 electric circuits |
| **Y9** | P2 energy at home → P9 static electricity → P10 magnetism → P12 space |

So P11 (matter) is a **Year 7** unit taught before P1 (energy transfers), and
P5 (pressure) is taught before P1 too. Reasoning from the unit numbers alone
would place both the other way round.

Method: `half_terms.derive()` gives `(unit, slug) → (year, half-term)`;
`INTRA_YEAR_UNIT_ORDER` breaks ties within a half-term; authored `lesson_NN`
file order breaks ties within a unit.

### Forward `requires` / `assumes` — **NONE across all 70 lessons**

Every declared prerequisite points backwards in the real delivery order. Zero
violations. The unit-opening lessons show a deliberate spine — each new physics
unit's first lesson requires the previous physics unit's last lesson (P5's
opener requires P4's `non-contact-forces`; P1's chain follows P5; P2's opener
requires P1's `simple-machines`; P9's opener requires P8's
`building-and-measuring-a-circuit`).

**No action. Strong positive** — Mide's brief asked "does any lesson depend on
something taught later?" and across 70 lessons the answer is no.

### `references` pointing forward — 38, of which **10 cross a school year**

`references` render as the "Connects to" card, which does not claim to be next,
so a forward pointer is not a lie the way chemistry's SYS-1 was. 28 of the 38
point forward by one or two half-terms inside the same unit and year — that is
legitimate "this connects to what you're about to do".

The 10 that cross a **year** boundary are worth a decision, because a Year 7
clicking one lands in a Year 8 lesson they have no grounding for:

| From (year taught) | To (year taught) |
|---|---|
| P4 `what-a-force-is` (Y7 HT2) | P5 `pressure-force-over-area` (Y8 HT1) |
| P4 `drawing-and-adding-forces` (Y7 HT2) | P5 `pressure-force-over-area` (Y8 HT1) |
| P4 `balanced-and-unbalanced` (Y7 HT2) | P5 `pressure-force-over-area` (Y8 HT1) |
| P4 `what-forces-do-to-motion` (Y7 HT3) | P5 `pressure-force-over-area` (Y8 HT1) |
| P4 `friction` (Y7 HT3) | P5 `pressure-force-over-area` (Y8 HT1) |
| P4 `air-and-water-resistance` (Y7 HT3) | P5 `pressure-force-over-area` (Y8 HT1) |
| P4 `moments` (Y7 HT4) | P5 `pressure-force-over-area` (Y8 HT1) |
| P4 `springs-and-hookes-law` (Y7 HT4) | P5 `pressure-force-over-area` (Y8 HT1) |
| P11 `brownian-motion` (Y7 HT5) | P1 `heating-and-thermal-equilibrium` (Y8 HT2) |
| P11 `temperature-and-internal-energy` (Y7 HT6) | P1 `heating-and-thermal-equilibrium` (Y8 HT2) |

**Eight of P4's nine lessons point at the same Year 8 pressure lesson.** That
repetition is the signal: it looks like a template applied across the unit
rather than eight considered links. Verified as unconditionally rendered — the
built card on `forces/what-a-force-is.html` emits a live
`<a href="/ks3/physics/pressure/pressure-force-over-area.html">` with no
gating.

**S2. Proposed solution:** two options for Mide, because one of them touches the
already-ruled covered-lessons scoping and this record does not relitigate that.
(a) Leave the links and let the "Connects to" heading carry it — defensible,
and no work. (b) Drop `pressure-force-over-area` from the seven P4 lessons where
it is clearly template-applied, keeping it on `what-a-force-is` where the
connection is genuinely instructive. Recommendation is (b): eight identical
forward links across one unit teach a student that the card is noise.
**Who fixes: Code (standing authority) once the option is picked. Effort: small
(one key per lesson file).**

### "Where to next" — correct

Spot-checked against the real order: `forces/what-a-force-is.html` emits
*"Next: Drawing and adding forces"* and *"Previous: Relative motion"* with
"Describing motion" as the sub-label — which is exactly right, since P3 precedes
P4 and the link crosses a unit. The cross-unit case is labelled rather than
hidden. **No action.**

## SYS-10 · "At GCSE this becomes" rendering — **ABSENT IN PHYSICS**

Chemistry's C1-06: five of six C1 lessons showed only a bare lowercase
slug-derived link while the authored `ks4_becomes` prose sat unrendered.

Computed across all 70 physics lessons:

| | Count |
|---|---|
| Lessons rendering authored **prose** (`ks3-endmatter-prose`) | **70 / 70** |
| Lessons showing only a bare link | **0** |
| Lessons with no GCSE card at all | **0** |

Example, `forces/what-a-force-is.html`: *"Contact and non-contact forces,
free-body diagrams, and Newton's third law as interaction pairs."*

**No action.** Recorded because it means the SYS-10 ruling chemistry is waiting
on (how the card should render) is already answered correctly in physics, and
the physics rendering is the model to adopt. Unit auditors still check whether
each statement is *accurate* — that is a separate question from whether it
renders, and their findings govern.

## SYS-3 · Header brand collides with the breadcrumb at 390px · S3 · **70 / 70 LESSONS**

Chemistry's C3-03, present in physics, on **every physics lesson page at phone
width**. Measured, not sampled: all 70 lessons driven at a true 390px viewport
(device-metrics override, so the media queries fire as on a real phone).

### What actually happens — and why a box-intersection test says it is fine

`.ks3-brand` sits in `div.ks3-nav-rail` with `flex-shrink: 1`, `min-width: 0`,
`overflow: visible`, `white-space: normal`. Its content needs **177px**. At
390px the flex rail shrinks the BOX to 72–117px depending on how long the
breadcrumb is. Because `overflow` is `visible`, the wordmark does not clip and
does not wrap — **it paints straight out of its box**, through the
`.ks3-nav-divider`, and over the first breadcrumb crumb.

The layout boxes never intersect (`speed.html`: brand box x=16 w=108 ending at
124, divider at 136, trail at 150). **So an `getBoundingClientRect()` overlap
test returns `false` and the defect looks absent.** This audit's first pass made
exactly that mistake and recorded "overlap: false". The correct test compares
the brand's `x + scrollWidth` (where the text really ends) against the trail's
`x`. Anyone re-verifying this must use the paint extent, not the box.

### Result across the unit

| | |
|---|---|
| Lessons measured at 390px | **70** |
| Lessons where the wordmark paints into the breadcrumb | **70** |
| Lessons clean | **0** |
| Overflow range | +60px to **+124px** |

Worst five: P11 `temperature-and-internal-energy` (+124px), P6
`transverse-waves-and-superposition` (+116), P10 `the-earth-is-a-magnet` (+110),
P10 `magnets-and-poles` (+108), P10 `how-a-motor-works` (+108). The pattern is
that a longer unit/lesson name squeezes the brand harder, so **P10 and P6 are
hit hardest** — four of the worst eight are P10.

### Evidence

`evidence/sys3-header-zoom-p3-shortest.png` (3× upscale of a true 390px render)
shows the dark bold **"MrBadmusAI"** with the rust-coloured breadcrumb crumb
**"Describi…"** printed straight through the middle of it, both illegible in the
collision zone — the reader sees `MrBadm[Describi]usAI`.
`evidence/sys3-header-zoom-p10-worst.png` shows the same on P10 electromagnets.
Full-height 390px captures: `evidence/sys3-brand-390-p3-shortest.png`,
`evidence/sys3-brand-390-p10-worst.png`. **No console errors on any page**, and
`document.scrollWidth == 390` throughout — the page does not scroll sideways;
the damage is confined to the header.

Phones are about half the audience, and this is the first thing on every page.

### Proposed solution

Two changes in `shared/ks3.css`, no content touched, no rebuild of lesson data:

1. `.ks3-brand { flex-shrink: 0; min-width: max-content; }` — the brand stops
   being the thing that gives way.
2. Move the shrinking to the trail: `.ks3-trail { min-width: 0; overflow:
   hidden; }` with the crumbs truncating by ellipsis, which they already do
   (the trail is already showing "Describi…" and "S…", so the truncation
   machinery exists — it is simply being applied to the wrong element).

If 177px of wordmark plus a usable trail still will not fit at 390px, the
fallback chemistry proposed applies: hide the wordmark below ~420px and keep
Design's chevron, which is recognisable alone.

**⚠️ This is shared KS3 chrome — the same fix lands on every biology and
chemistry lesson too, and chemistry's C3-03 is the same defect.** Fix once,
verify across all three subjects.

**Who fixes: Code (standing authority). Effort: small.**

## The physics assignment bank is AUTHORED but NEVER SHIPPED — 840 questions

Refining the DB row counts above, because "physics has no bank" would be the
wrong conclusion. Physics bank questions **exist, fully written**, in
`ks3_data/p<N>/questions_*.py` — twelve per lesson, banded easier/harder, each
with four options and a `why` on every distractor:

| Unit | Lessons | Bank questions authored |
|---|---|---|
| P1 | 8 | 96 |
| P2 | 5 | 60 |
| P3 | 3 | 36 |
| P4 | 9 | 108 |
| P5 | 4 | 48 |
| P6 | 9 | 108 |
| P7 | 7 | 84 |
| P8 | 7 | 84 |
| P9 | 3 | 36 |
| P10 | 5 | 60 |
| P11 | 4 | 48 |
| P12 | 6 | 72 |
| **Total** | **70** | **840** |

**840 authored in the repo. 0 in `ks3_assignment_bank` on production.** The
export that shipped biology and chemistry (1356 rows) never ran for physics.
Same story for the ladder mirror and the cards.

⚠️ Note for anyone reading alongside earlier notes: the number 840 also appears
in an older memory as "KS3's old bank size". That is a coincidence — this 840 is
exactly 70 physics lessons × 12 questions and is a different quantity.

**This does not affect the 70 lesson pages**, whose ladders are baked in at
build time. It means physics cannot be set as a weekly assignment and produces
no dashboard flashcards. **Mide pile** — it is a deploy/scope decision, not a
lesson defect, and it is the largest single gap between physics and the other
two subjects. Effort to close: an export run, not authoring.

## SYS-8 · Answer tells — position **CLEAN**, length **A REAL TELL** · S2

`verify_answer_positions.py` (MRB-278, permanent gate) watches answer POSITION.
It does not watch option LENGTH, and it does not reach hooks or benches. Both
gaps were measured across all 840 authored physics bank questions.

### Position — passes comfortably

| Index | Count | Share |
|---|---|---|
| 0 | 197 | 23.5% |
| 1 | 221 | 26.3% |
| 2 | 224 | 26.7% |
| 3 | 198 | 23.6% |

All 840 questions have exactly four options and exactly one correct. MRB-278's
thresholds (no index above 50%, no index at zero) pass with a maximum share of
26.7%. Per unit, seven of twelve are *perfectly* balanced (P1, P2, P3, P6, P7,
P9, P10, P11 cycle the index deliberately — P3's source file even documents it:
*"⚠ POSITION IS AUTHORED — index cycles 1, 2, 3, 0"*). The loosest is P5 at 33%,
still well inside. **No action.**

### Length — the correct option is measurably the longest one

| | |
|---|---|
| Mean correct-option length | **56.3 characters** |
| Mean wrong-option length | **47.7 characters** |
| Correct option is *uniquely the longest* | **295 / 840 = 35.1%** (chance ≈ 25%) |
| Significance | **z = 6.8** |

**A student who ignores the physics entirely and always picks the longest option
scores 35% instead of 25%** — a free ten points, and more in some units:

| Unit | n | Longest = correct | Mean correct | Mean wrong |
|---|---|---|---|---|
| **P11 matter** | 48 | **56.2%** | 50.5 | 40.8 |
| **P5 pressure** | 48 | **45.8%** | 60.5 | 41.9 |
| **P2 energy at home** | 60 | **43.3%** | 45.3 | 35.5 |
| P3 describing motion | 36 | 38.9% | 41.2 | 32.5 |
| P1 energy transfers | 96 | 38.5% | 60.3 | 59.3 |
| P12 space | 72 | 34.7% | 47.3 | 45.7 |
| P7 light | 84 | 34.5% | 65.5 | 48.2 |
| P10 magnetism | 60 | 33.3% | 59.4 | 57.5 |
| P6 waves and sound | 108 | 32.4% | 68.4 | 50.4 |
| P8 electric circuits | 84 | 28.6% | 55.8 | 52.8 |
| P4 forces | 108 | 26.9% | 50.2 | 40.0 |
| P9 static electricity | 36 | 19.4% | 55.7 | 59.2 |

**In P11 a student picking the longest option gets more than half of the unit's
bank right without reading a word of physics.**

The cause is visible in the worst cases and it is an honest authoring habit, not
carelessness: the correct answer carries its reasoning while the distractors are
curt. P3 `p3-03-h04` — correct option 65 characters longer than any distractor:

> **CORRECT:** *"Because no experiment inside a smoothly moving room can tell
> you how fast the room is going, so there is no way to…"*
> wrong: *"Because the ground is already that thi…"* / *"Because instruments are
> not yet accura…"* / *"Because speeds would then all be far t…"*

Same shape in `p3-01-h03` (+63), `p3-01-h02` (+46), `p2-02-h03` (+41),
`p2-02-h01` (+39), `p2-05-s01` (+38).

**Proposed solution:** do not shorten the correct answers — the reasoning in
them is the teaching. **Lengthen the distractors** so each carries its own
plausible reasoning at comparable length, which also makes them better
distractors (a curt wrong option is easy to dismiss for the wrong reason).
Start with P11, P5 and P2, which carry the tell hardest. Then **extend
`verify_answer_positions.py` with a length check** — flag any corpus where the
correct option is uniquely the longest in materially more than ~25% of
questions — so the habit cannot silently return. The same measurement should be
run against biology and chemistry, which this audit did not check and which
share the authoring pattern.

**Who fixes: Code (standing authority) for the gate; the rewrites are authoring
and want Mide's eye on the science of each new distractor. Effort: medium
(295 questions to lengthen, mechanical per item); gate extension small.**

⚠️ Scope note: this measures the AUTHORED bank, which is what would be served
if it shipped. Since the physics bank has 0 rows on production, **no student is
currently exposed to this tell through the weekly assignment.** It matters at
the moment the export runs, which is why it belongs in the same decision as the
840-question gap above. Hooks, predicts and bench chips are driven per unit by
the twelve auditors; their findings cover the part a grep cannot reach.

## Link integrity — **CLEAN**

All 83 physics HTML files, every internal `href` resolved against the built
tree (accepting `path`, `path.html` and `path/index.html`, since Cloudflare
Pages serves the extensionless form and 308-redirects the rest).

| | |
|---|---|
| Pages checked | 83 |
| Internal hrefs resolved | **1,399** |
| Broken internal links | **0** |

External references are 221 absolute `https://mrbadmus.com/...` links (canonical
and Open Graph tags, one set per page) and 83 inline `data:image/svg+xml`
sources — no third-party hosts are linked from any physics lesson.

**No action.** Records the answer to the brief's "broken links and wrong
next/previous targets" sweep at estate level; the *semantic* correctness of
next/previous targets is covered in the ordering section above and was also
clean.

### ⚠️ CORRECTION — P11's record reports SYS-3 "absent". It is present. STRUCK.

`records/p11.md` records SYS-3 as *"absent — measured at true 390 px reflow, no
brand/trail overlap and no overflow on any of the five pages"*. That conclusion
is **wrong, and it is wrong for exactly the reason predicted above**: it tests
whether the two layout BOXES intersect, and they never do.

Re-measured on P11's own pages at a true 390px reflow:

| Page | Brand box | Brand needs | Box ends | **Text ends** | Trail starts | Boxes intersect | **Paint intrudes** |
|---|---|---|---|---|---|---|---|
| `temperature-and-internal-energy` | 53px | 177px | 69px | **193px** | 95px | **false** | **true, by 98px** |
| `density` | 87px | 177px | 103px | **193px** | 129px | **false** | **true, by 64px** |

`temperature-and-internal-energy` is the **worst page in the whole physics
estate** (+124px overflow), and its brand box is squeezed to 53px — under a
third of the 177px the wordmark needs.

Evidence: `evidence/sys3-p11-zoom.png` (3× upscale of a true 390px render)
shows dark bold **"MrBadmusAI"** with the rust crumb **"Matter…"** printed
through the middle of it and grey **"…emperatu…"** across its tail —
`Mr[Matter]BadmusAI[emperatu…]`, three overlapping strings, none readable.
Raw captures: `evidence/sys3-p11-p11-worst.png`,
`evidence/sys3-p11-p11-density.png`.

**P11's SYS-3 probe is struck and replaced by this measurement. The count stands
at 70 / 70.** P11's other 25 findings are unaffected — this is one probe result,
not a defect in the unit audit.

**Method note for the consolidator and for any future audit:** a header overlap
caused by `overflow: visible` text escaping a flex-shrunk box is INVISIBLE to
`getBoundingClientRect()` intersection. The only valid test is
`brand.x + brand.scrollWidth > trail.x`. Any auditor reporting SYS-3 absent
from a box-intersection test should be re-checked, not believed.

## XU-1 · Two contradictory Key facts define temperature · **S1** · P1 + P11

Raised by P11's auditor as a vocabulary mismatch. Verified at estate level, and
it is more than vocabulary: **two "Key fact" boxes — the highest-authority
element on a KS3 page — define the same quantity differently, and one of them
is wrong.**

| Unit | Taught | The box | What it says |
|---|---|---|---|
| **P11** `temperature-and-internal-energy` | **Y7 HT6 (first)** | Key note | *"Temperature measures the **average kinetic energy** of a single particle and is read in degrees Celsius."* |
| **P1** `heating-and-thermal-equilibrium` | **Y8 HT2 (second)** | Key fact | *"Temperature is the **average speed** of the particles."* |

The split is total, and measured: `internal energy` appears **26 times in P11
and 0 times anywhere in P1**; `thermal store` appears **34 times across P1 and
0 times in P11**. Neither lesson references the other. P1 contains no "you met
this in Year 7", no link to P11, and no mention of the particle-model unit by
name.

It reaches the marking, not just the prose. Both ladders credit their own
version:
- P11 rung: *"Says temperature measures the **average kinetic energy** of the particles."*
- P1 rung: *"Says temperature measures the **average speed** of the particles."*

So a Year 8 student who correctly learned P11's version in Year 7 and writes it
in P1 is answering against a criterion that names the other phrase.

### The science — P1's sentence is the incorrect one

Temperature is proportional to the **average kinetic energy** of the particles,
not to their average speed. The two are not interchangeable:

1. Kinetic energy is ½mv², so average KE is not a function of average speed —
   ⟨v⟩ ≠ √⟨v²⟩ for any real distribution of speeds.
2. **The definition breaks across substances.** At the same temperature,
   heavier particles move *more slowly* and lighter ones *faster*, while their
   average kinetic energies are equal. "Temperature is the average speed" makes
   the false prediction that two gases at the same temperature have particles
   moving at the same speed.

Within P1 the error is not exposed, because P1's bench varies only *how fast*
and *how much* for one substance. It becomes wrong the moment a student compares
two different materials — which P1's own unit does in `conduction` and
`insulation`, and which P11 has already taught them to do.

This is not a criticism of the P1 lesson's design, which is strong: the bench
separates temperature from thermal store with a logarithmic bar and states
outright *"They are two different quantities, and the spark is the proof: the
fastest particles on the bench, and almost no energy at all."* That is exactly
the right teaching. **One sentence in the Key fact is carrying a wrong
definition inside an otherwise excellent lesson.**

### Proposed solution

1. **Change P1's Key fact** to the correct quantity and make it agree with the
   unit taught before it: *"Temperature is the average kinetic energy of the
   particles. The energy in a thermal store depends on that and on how many
   particles there are."* — the second sentence is already there and already
   correct, and the change is one noun phrase.
2. **Update P1's ladder criterion** to credit "average kinetic energy" (accept
   "average speed" as a partial for one cycle if Mide prefers a soft landing).
3. **Bridge the two vocabularies once, in P1**, since P1 is met second: one
   clause naming internal energy as the quantity P11 called by that name. A
   student should not have to work out that "thermal store" and "internal
   energy" are the same idea.
4. Tighten P11's *"of a single particle"* to *"per particle, on average"* —
   P11's own body text already gets this right (*"how much kinetic energy one
   particle has, on average"*), so only the Key note needs it.

**Who fixes: Code (standing authority — this is a science correction, not a
ruling). Mide sign-off on the final Key-fact wording, since it is a Key fact.
Effort: small (one noun phrase, one criterion, one bridging clause).**

⚠️ **Check the same error in biology and chemistry.** Chemistry C1
(particles and their behaviour) teaches the particle model and was audited on
25 Aug without this being raised; this audit did not check C1's temperature
wording, and it should be checked before the fix is called complete.

### ⊕ XU-1 EXTENDED — the estate has THREE definitions of temperature, across two subjects

Swept every KS3 lesson in all three subjects for a sentence defining
temperature. There are three, and **the correct one is taught first and then
contradicted twice**:

| Order met | Unit · lesson | Delivery | The sentence | Verdict |
|---|---|---|---|---|
| **1st** | **P11** `temperature-and-internal-energy` | **Y7 HT6** | *"Temperature measures the average **kinetic energy** of a single particle…"* | ✅ correct |
| **2nd** | **P1** `heating-and-thermal-equilibrium` | **Y8 HT2** | *"Temperature is the average **speed** of the particles."* | ❌ wrong |
| **3rd** | **C7** `energy-and-changes-of-state` | **Y9 HT1** | *"Temperature is **how fast the particles are moving**."* | ❌ wrong, and loosest |

A pupil meets the right definition in Year 7, a looser wrong one in Year 8, and
the loosest wrong one in Year 9 — the sequence runs backwards.

**The chemistry audit of 25 Aug did not catch the C7 instance.** C7 was audited
(9 findings) and this was not among them, which is worth saying plainly: it is
invisible from inside a single unit, and only a cross-subject sweep surfaces it.

C7's instance is doing real work in its argument, which makes it worse rather
than better. In context: *"…while it is being spent, none is left over to make
the particles move faster. **Temperature is how fast the particles are moving.**
During a change of state they are not speeding up; they are being separated."*
The plateau explanation **depends** on the definition, so a pupil who accepts
the paragraph has to accept the wrong definition to follow the (otherwise
correct and well-made) point about latent heat.

**Revised proposed solution — one wording, applied at all three sites:**

Adopt P11's quantity everywhere, since it is correct and is met first:

- **P1** Key fact → *"Temperature is the average kinetic energy of the
  particles. The energy in a thermal store depends on that and on how many
  particles there are."*
- **C7** → *"Temperature is a measure of the average kinetic energy of the
  particles."* The surrounding argument survives unchanged: during a change of
  state the particles are not gaining kinetic energy, they are being pulled
  apart — which is the point C7 is making, and it is *easier* to make with the
  correct definition, not harder.
- **P11** Key note → tighten *"of a single particle"* to *"per particle, on
  average"*.
- **P1's ladder criterion** → credit "average kinetic energy".
- One bridging clause in P1 naming internal energy / thermal store as the same
  quantity under two names.

**Who fixes: Code (standing authority — science correction). Mide sign-off on
the final Key-fact wording, since two of the three are Key fact/note boxes.
Effort: small (three sentences, one criterion, one bridging clause) — but it
crosses the physics/chemistry boundary, so it needs one owner, not two.**

## SYS-8 EXTENDED · the length tell runs in BOTH directions, and the gate is directional

P6's auditor found the tell **inverted** on its calculate rungs — the correct
answer is the only *bare* option beside 14–18-word distractors — and noted that
MRB-278's tell gate "only watches for the correct answer being longest, so the
short-correct form passes untouched". Measured across all 840 authored physics
bank questions:

| | Count | Share | z vs 25% chance |
|---|---|---|---|
| Correct is uniquely the **longest** | 295 | **35.1%** | **+6.8** |
| Correct is uniquely the **shortest** | 127 | **15.1%** | **−6.6** |
| Correct is an **extreme** (either end) | 422 | 50.2% | ≈ chance (50%) |

So across the bank as a whole the bias is **directional, not extremal**: the
correct option is pushed toward *longest* and away from *shortest*. Overall
"extremeness" sits exactly at chance, which is why a symmetric test would find
nothing. Per unit, though, two carry a large extremal signal from both ends at
once — **P11 70.8%** and **P3 69.4%** of questions have the correct option at one
end or the other.

| Unit | longest | shortest | either extreme |
|---|---|---|---|
| P11 | 56.2% | 14.6% | **70.8%** |
| P3 | 38.9% | 30.6% | **69.4%** |
| P1 | 38.5% | 21.9% | 60.4% |
| P2 | 43.3% | 13.3% | 56.7% |
| P5 | 45.8% | 10.4% | 56.2% |
| P12 | 34.7% | 20.8% | 55.6% |
| P10 | 33.3% | 20.0% | 53.3% |
| P8 | 28.6% | 20.2% | 48.8% |
| P7 | 34.5% | 7.1% | 41.7% |
| P4 | 26.9% | 13.0% | 39.8% |
| P6 | 32.4% | 5.6% | 38.0% |
| P9 | 19.4% | 13.9% | 33.3% |

Worst inverted cases, where the bare option is the right one:
`p9-02-h03` (correct 50 chars shorter than any distractor — *"It is unchanged"*
against three explained wrongs), `p8-01-s03` (−48, *"is the same in both
places"*), `p10-01-h03` (−46, *"The bar is a magnet"*), `p8-03-s03` (−41,
*"All three read 0.00 A"*).

**Revised proposed solution:** the gate extension proposed above must be
**two-sided** — flag a corpus where the correct option is uniquely longest OR
uniquely shortest materially more often than chance, and flag per-unit as well
as per-corpus, since P11 and P3 are invisible in the estate-wide total. The
authoring remedy differs by direction: lengthen the distractors where the
correct answer is long; give the *correct* answer its reasoning where it is
bare. P6's record notes the remedy already exists on three of its six calculate
rungs, so the pattern to copy is in the estate.

**Who fixes: Code (gate, two-sided); authoring wants Mide's eye. Effort: gate
small; rewrites medium.**

## No KS3 lesson ever plays a sound — raised by P6, verified estate-wide

P6's auditor flagged that *"nothing in nine lessons about sound ever plays a
sound"* and put it forward as a product question rather than a defect. Verified,
and it is broader than P6:

| Probe | Physics | All of KS3 |
|---|---|---|
| `<audio>` element | 0 | **0** |
| Web Audio (`AudioContext`, `createOscillator`, `OscillatorNode`) | 0 | **0** |
| `new Audio(...)`, `playSound` | 0 | **0** |
| `.mp3` / `.wav` / `.ogg` reference | 0 | 0 |

**There is no audio anywhere in the key stage.** Every instrument in the sound
unit — the tuning fork, the slinky, the frequency/pitch bench, the auditory
range bars, ultrasound — is silent and visual.

This is recorded as a **Mide pile** item, not a finding. It is plainly a
deliberate posture (silent-by-default is the right call for a classroom of
thirty on shared devices, and for accessibility), and P6's own audit shows the
visual instruments teach the physics correctly. But P6 is the one unit where the
phenomenon itself is audible, a pitch slider that changes an actual pitch is the
single most persuasive demonstration available in the topic, and the decision has
never been written down. Options: (a) keep it silent, and say so in the docs so
it stops being rediscovered; (b) allow audio in P6 only, gated behind an explicit
press and never autoplay, with a visible mute. Recommendation: (b) for
`frequency-pitch-and-loudness` alone, where the pedagogical gain is largest and
the scope is one instrument.

**Who decides: Mide (product scope). Effort if approved: medium, one unit.**

## XU-2 · Adjudication of P9-2 (P9 vs P8 on what an insulator does) — **downgraded S1 → S2**

P9's record raises P9-2 as **S1**, stating that P9 lesson 1's insulator
vocabulary *"states P8's registered misconception `CIRC-21` verbatim"*. The
brief makes the consolidator resolve cross-unit science disagreements against
the national curriculum and record both positions. Resolved as follows.

**P8's registered misconception** (`ks3_data/p8/lesson_06`, id `CIRC-21`):
> *"An insulator blocks electricity completely — absolutely nothing gets through."*

**P8 confronts it well**, and the confrontation is served on the page:
> *"Not quite nothing. Put 6 V across a plastic ruler and a current does flow:
> about three millionths of a millionth of an amp… which is exactly why we call
> the plastic an insulator — but the word describes **how little, not none**."*

**What P9 actually says** — every insulator sentence on `charging-by-rubbing`:
> *"It only works with insulators, because a conductor lets the charge escape."*
> *"…a conductor would let the charge run straight back or away to earth through your hand."*
> ladder criterion 5: *"Says earthing a plastic bottle achieves nothing, because
> plastic is an insulator and **the charge cannot travel** along it to the wire."*

**Resolution.** P9 does **not** state `CIRC-21` verbatim, and the claim that it
does is not supported — none of P9's sentences asserts that nothing gets
through. What is real is narrower and still worth fixing: **the ladder criterion
credits an absolute "cannot travel"** where P8, taught two half-terms earlier
(P8 is Y8 HT6, P9 is Y9 HT2), has explicitly taught "how little, not none". A
pupil who absorbed P8's nuance meets a marking criterion phrased against it.

**The physics in P9's context is defensible.** At electrostatic scale on a
plastic bottle, charge genuinely does not migrate fast enough to earth — that
is precisely why static persists on insulators, and it is the correct
explanation of the phenomenon P9 is teaching. P8's nuance concerns ~3 × 10⁻¹² A
across a ruler at 6 V, which is negligible by any classroom measure. So this is
a **consistency of language** defect, not a science error.

**Severity revised to S2.** Proposed solution: soften P9's criterion 5 to
*"…because the charge cannot travel along it fast enough to reach the wire"*,
which is true at both scales and costs four words; optionally one clause in P9
naming P8's "how little, not none" so the two lessons visibly agree.
**Who fixes: Code (standing authority). Effort: small.**

P9's other three S1s (P9-1 triboelectric ordering, P9-9 induction verb, P9-14
dipole caption) are unaffected by this adjudication and stand as recorded.

## NOT A DEFECT — the empty `<img src="">` on all 70 lesson pages · do not re-derive

A mechanical sweep flags a "broken image on every page". P3's auditor checked
before reporting it and did not report it. Independently verified here, and the
conclusion is confirmed — recorded so no future audit spends time on it again.

There is **exactly one `<img>` in the whole physics estate**: 70 instances of
`<img id="imgPreview" src="" alt="preview">`, one per lesson page, inside
`div.img-preview-row` in the **tutor chat panel**. It is the placeholder that
receives a `src` when a student attaches a picture to a chat message.

Measured on a served page:

| Probe | Result |
|---|---|
| `src` / `currentSrc` | `""` |
| `naturalWidth` | 0 |
| Rendered size | 0 × 0 |
| Inside a hidden ancestor | **true** (`offsetParent` null) |
| Network requests for the page URL | **none** — the empty `src` fires no fetch |
| Console errors | **none** |

No student ever sees it, it costs no request, and it is doing its job. **Not a
finding.** (Worth knowing generally: an empty `src` used to re-request the
current document in older browsers; it does not here, which is why the check
was worth running rather than assuming either way.)

## SYS-8, THIRD FORM · the em-dash shape tell on recall rungs · S2 · **17 of 70 lessons, 7 units**

Raised by P5's auditor ("on all four Rung 1s the correct answer is the only
option without an em-dash tail"). Verified across every ladder rung in the
physics estate, and the claim is **exactly right**, including its estate-wide
count.

Method: load all 70 `ks3_data/p*/lesson_*.py`, take each ladder rung with four
string options and an integer `answer`, and test whether the correct option is
the **only one without an em/en-dash**.

| Rung | Rungs with the tell | Rungs examined |
|---|---|---|
| **recall** | **17** | 70 |
| apply | **0** | 70 |
| explain / produce | 0 | 0 (free-text) |

**Every instance is a recall rung on a calculation lesson**, and the shape is
identical each time: the correct answer is a bare quantity, and all three
distractors carry an em-dash clause explaining the error that produced them.

> P5 `pressure-force-over-area`, rung 1 —
> correct: **"2000 Pa"**
> distractor: *"180 Pa — multiply the force by the area"*
> distractor: *"2000 N — a press on the floor is a force, so…"*

**A student can answer all seventeen without doing any physics: pick the option
with no dash.** It is the first rung of the mastery ladder, so it is also the
student's first impression of whether the ladder is worth engaging with.

The 17, by unit:

| Unit | Lessons | Which |
|---|---|---|
| **P5** | **4 of 4 — 100%** | `pressure-force-over-area`, `pressure-in-liquids`, `upthrust-floating-and-sinking`, `atmospheric-pressure` |
| P6 | 3 | `waves-on-water`, `transverse-waves-and-superposition`, `echoes-reflection-and-absorption` |
| P8 | 3 | `current-at-a-junction`, `potential-difference`, `resistance` |
| P4 | 2 | `moments`, `springs-and-hookes-law` |
| P7 | 2 | `reflection-mirrors-and-scattering`, `lenses-and-images` |
| P12 | 2 | `gravity-and-weight`, `mass-vs-weight` |
| P11 | 1 | `density` |

**P5 is the only unit at 100%**, which is why its auditor saw the pattern — in
every other unit it is intermittent enough to look like coincidence.

**This is a third, independent form of SYS-8**, alongside the length tell
(estate-wide, both directions) and the positional tell (hooks). All three sit
underneath `verify_answer_positions.py`, which watches **position only**. A
corpus can be perfectly balanced positionally — P5's is — and still be
answerable by shape.

**Proposed solution:** give the correct option an em-dash clause too. It costs
one clause per rung, it is the pattern the distractors already use, and on a
recall rung the clause is worth having pedagogically — *"2000 Pa — 600 N shared
over 0.30 m²"* confirms the method as well as the answer, which is what a recall
rung is for. Then extend the gate with a **shape check**: flag any rung where
the correct option is the unique odd-one-out on a structural feature (dash
present/absent, trailing clause present/absent, units present/absent).

**Who fixes: Code (standing authority) for the 17 clauses and the gate; the
clauses are one line each and want no new science. Effort: small (17 items),
gate medium.**

⚠️ The same test should be run on biology and chemistry, which share the
authoring pattern and were not checked here.

### ⊕ SYS-8 third form — extended to the whole key stage: **PHYSICS ONLY**

The note above said the em-dash shape test "should be run on biology and
chemistry". It has been. Re-run across **every** KS3 lesson in all three
subjects:

| Rung | With the tell | Examined |
|---|---|---|
| recall | **17** | 182 |
| apply | 0 | 182 |

**All 17 are in physics. Biology and chemistry return zero.** The tell is not a
platform-wide authoring habit — it is specific to the physics calculation
lessons, in seven of the twelve physics units, and it does not need a
cross-subject fix. That narrows the remedy to the 17 rungs already listed.

(P12's auditor independently measured a related mirrored-length threshold over
all 370 four-option sets in KS3 and reported 26 hits across 14 units, 24 of them
ladder recall. The two measurements test different features — dash presence
versus strict length-mirror — and agree on the substance: **one construct on
recall rungs, not a scatter of slips.** The consolidator should report both
numbers with their definitions rather than reconciling them into one, since
neither is wrong.)

## XU-3 · The Sun's mass is understated by a factor of 1000 · **S1** · VERIFIED

P12's record raises this as P12-07. Independently verified, and it is correct.
Noting for the consolidator that it is on **`gravity-earth-moon-and-sun`**, not
on `the-sun-stars-and-galaxies` — worth pinning so the fix lands on the right
file.

Served text, in context:

> *"A gravitational pull always comes as a pair of equal and opposite forces.
> The Sun pulls the Earth and the Earth pulls the Sun, with exactly the same
> number of newtons. What differs is the result: the same force barely stirs a
> body of **two thousand trillion trillion kilograms** and swings a smaller one
> right round it."*

"A body… that barely stirs" while "swings a smaller one right round it" is
unambiguously **the Sun**.

| | |
|---|---|
| As written | two thousand trillion trillion = 2 × 10³ × 10¹² × 10¹² = **2 × 10²⁷ kg** |
| The Sun's actual mass | **1.989 × 10³⁰ kg** |
| Error | **1000× too small** |
| What 2 × 10²⁷ kg actually is | ≈ **Jupiter** (1.898 × 10²⁷ kg) |

The number as printed describes a large *planet*, not a star — and it is doing
so **in the one sentence whose entire job is to explain why the Sun barely
moves**. Understating the Sun's mass by three orders of magnitude undercuts the
argument at the moment it is made.

**Proposed correction:** *"two million trillion trillion kilograms"*
(2 × 10⁶ × 10²⁴ = 2 × 10³⁰ ✓). If Mide prefers to avoid stacked multipliers for
Year 9 — and there is a case, since "thousand/million trillion trillion" is
exactly the construction that produced the slip — the comparison form carries
the point better and cannot be mis-scaled: *"…barely stirs a body 330,000 times
the mass of the Earth, and swings the smaller one right round it."*
Recommendation: the comparison form.

**Who fixes: Code (standing authority — arithmetic correction). Mide sign-off on
which of the two forms, since it is a choice about register. Effort: small (one
phrase).**

⚠️ Checked while here: the unit's other large numbers on that page and on
`the-sun-stars-and-galaxies` are **right** — "around two trillion galaxies"
(≈2 × 10¹², correct) and the Milky Way's central black hole at "about four
million solar masses" (correct for Sgr A*). This is an isolated slip, not a
pattern of magnitude errors.

## XU-4 · 246 authored vocabulary definitions never reach a physics student · **S2** · 69 of 70 lessons

Raised by P7 as P7-30. Verified, and it is the largest single body of authored
teaching in the estate that no student can see.

**Every one of the 182 KS3 lessons authors a `vocabulary` list** — 843 entries
key-stage-wide, **246 of them in physics** — each a `term` plus a written
`definition`. They are good. Verbatim examples from P1:

> **store** — *"Somewhere energy sits and can be counted while nothing is
> happening — kinetic, gravitational, elastic, thermal, chemical, magnetic,
> electrostatic or nuclear."*
> **wasted energy** — *"Energy that ends up in a store you did not want filled —
> almost always a thermal store in the surroundings. It has not been destroyed,
> only spread out too thinly to be useful."*
> **conservation of energy** — *"The rule that the total energy before a change
> is exactly equal to the total after it. No exception has ever been found."*

**None of those three strings appears anywhere in the built estate.** Searched
all of `mrbadmus_site/ks3/`: zero hits each.

### Why — and it is not a renderer bug

`build_ks3.py`'s `r_keyword()` renders vocabulary as flip cards ("Say it, then
tap →"), and it works. But it only fires when a lesson's `core` authors a
**`keyword` block** naming the terms it wants. A lesson can author fifty
definitions; if it authors no `keyword` block, `r_keyword` is never called and
every definition is dead. The generator's own comment records the same shape
being discovered before: *"NO LESSON IN B1–C2 AUTHORS A `keyword` BLOCK: C3
places the first three in the key stage."*

### Who actually renders it

| Subject | Lessons rendering vocabulary flip cards |
|---|---|
| Chemistry | **34** |
| Biology | 4 |
| **Physics** | **1** — `describing-motion/speed` and nothing else |
| KS3 total | 39 of 182 |

**So 69 of 70 physics lessons author definitions that no student ever sees**,
while chemistry surfaces them on 34 lessons. A pupil moving between subjects
gets vocabulary support in chemistry and almost none in physics, from the same
platform, with the physics definitions already written and sitting in the repo.

⚠️ Partial mitigation, stated so the finding is not overclaimed: the *term
names* (not the definitions) are aggregated into a "Words this unit gives you"
chip box on the year/half-term **browse** pages, and physics terms do reach it —
`upthrust`, `moment` and `potential difference` each appear on a year page.
`refraction` and `energy store` do not. So a student sees some physics words
listed on a browse page they may never visit, and the definitions nowhere.

This also has a named victim elsewhere in this audit: P7-11 flags "denser" used
unglossed in the refraction lesson — and P7's `vocabulary` **already contains
the definition that would have fixed it**.

### Proposed solution

Add a `keyword` block to each physics lesson's `core`, listing the terms that
lesson introduces. The definitions, the renderer, the flip-card interaction, the
rail-stop anchor and Design's heading treatment all already exist and are
already proven on 39 lessons — **this is wiring, not authoring.** Place it after
the lesson's first teaching block, as chemistry does.

Sequence it with Mide's eye on two things only: which terms each lesson should
front (the `vocabulary` lists are longer than a card grid should show — chemistry
heads them "Four words" / "Five words"), and whether any definition needs
updating before it goes in front of students, since none has yet been read by a
class.

**Who fixes: Code (standing authority) for the wiring; Mide picks the per-lesson
term shortlist. Effort: medium (70 lessons × one block, mechanical, no new
prose).**

⚠️ **Biology is in the same position** — 4 of its lessons render vocabulary and
the rest do not. Out of scope here, but the same one-block fix applies, and the
decision should be taken once for the key stage rather than twice.

## Arrowheads on ray diagrams — P7-04 confirmed estate-wide

| Probe | Physics files | All KS3 files |
|---|---|---|
| `marker-end` | **0** | 2 |
| `marker-start` | **0** | 0 |
| `<marker` | **0** | 2 |
| `markerWidth` | **0** | 2 |

**No SVG in any of the 70 physics lessons defines or uses an arrowhead marker.**
The two `ks3-mark-arrow` hits on each light page are the *navigation* arrows in
the end-matter links, not ray arrows.

This confirms P7-04 as recorded, and shows it is not a light-unit problem but an
estate-wide one: it is equally true of P4's force arrows and P10's field lines,
both of which this audit's other records flag. A ray or field line without a
direction arrowhead is the standard exam mark loss, and in P7 it lands on the
two lessons whose registered misconception is *your eyes send something out* —
where an undirected line between a scene and an eye is precisely the ambiguity
the lesson exists to remove.

**Proposed solution:** define one shared `<marker>` arrowhead in the KS3 SVG
kit and apply it to every ray, force vector and field line. One definition,
applied per drawer. **Who fixes: Code + Design brief for placement conventions
(arrow at the ray's end, mid-line for long rays). Effort: medium.**

## ⚠️ Correction to this audit's own briefing — P7's lesson order

P7's auditor recorded a deviation: the lesson order given in its brief
(colour → why-coloured → lenses → eye) is **not** the unit's order. It is right.
The unit's `prev`/`next` chain, its index, and the `ks3_data/p7` file numbering
all run **light-travels → reflection → refraction → lenses → eye → colour →
why-things-look-coloured**, which is also what this record's delivery-order
computation produced. The brief took its order from an alphabetical directory
listing. **The auditor audited in the correct order and said so — no finding is
affected.** Recorded because the same slip would mislead a fix run.

### ⚠️ SYS-3 — THREE unit auditors reported it absent. All three used a box test. All three STRUCK.

| Unit record | Reported | Re-measured (text-ink `Range` over the wordmark's text node) | Verdict |
|---|---|---|---|
| **P11** | absent | `temperature-and-internal-energy`: box 53px, needs 177, ink overprints trail by **98px** | **STRUCK** |
| **P4** | absent — *"docW = 390, brand/trail never collide"* | `what-a-force-is`: box 117px, ink ends 193px, trail starts 159 → overprints by **34px**. `air-and-water-resistance`: box 98px → overprints by **53px** | **STRUCK** |
| **P8** | absent — *"measured on all 8 pages"* | covered by the estate sweep: all 7 P8 lessons collide | **STRUCK** |

Seven auditors (P3, P5, P6, P7, P9, P10, P12) reported it **present**, and
**P10's auditor diagnosed the false negative before it was found**:

> *"SYS-3 is PRESENT on all five P10 pages and a standard overflow sweep reports
> them clean. `scrollWidth` is exactly 390 and no element box crosses the edge;
> the wordmark's text ink overflows its shrunk box by ~105–110px and the
> breadcrumb paints over ~60% of 'MrBadmusAI'. I nearly recorded it absent.
> Other unit auditors using a box-based test will get a false negative — the
> measurement needs a `Range` over the text node."*

That is exactly what happened, three times. In every struck case
`document.scrollWidth == 390` and `boxesCollide == false` — both true, both
irrelevant.

Evidence for the P4 strike: `evidence/sys3-p4-zoom.png` shows dark bold
**"MrBadmusAI"** with the rust crumb **"Forces"** printed through it and
**"Air and wa…"** running into its tail.

**The count stands at 70 / 70 lessons.** No unit is exempt. The three struck
probes do not affect any other finding in those three records.

## SYS-8, FOURTH FORM · hook answer position · S2 · a corpus no gate measures

P4 and P8 both found it independently, in a corpus P4 correctly notes **no gate
in the repo measures**: the hook (`phenomenon`) options. `verify_answer_positions.py`
covers ladder and bank only.

The hook has **no `answer` key** — the correct option is identifiable only by
matching the `reveal` prose back to an option, which is why it has escaped
measurement.

| Source | Method | Result |
|---|---|---|
| **P4's auditor** | resolved 62 of 70 hooks | **A 13 · B 32 · C 13 · D 4** — B on ~52%, and B on 7 of P4's own 9 lessons |
| **P8's auditor** | its own 7 lessons | index **0 (A) on 6 of 7**, longest in 5 of those |
| **This record** (independent check) | deliberately conservative token-overlap matcher; resolved only **31 of 70** confidently | **A 6 · B 15 · C 7 · D 3** — **B 48%** |

**The three agree on the substance.** The estate skews hard to **B** (~48–52%
against 25% chance), and **P8 is the outlier that skews to A** — which is why
its auditor saw a different pattern in its own unit and was right about it.

⚠️ **Report P4's numbers as the finding, not this record's.** My matcher
resolved fewer than half the hooks because it refuses a match when the top two
options score within 0.15; that is the right posture for a corroborating check
and the wrong one for a headline count. Both are recorded so the double-checker
can see the methods differ rather than suspecting a contradiction.

**Proposed solution:** give the hook an explicit `answer` index in
`ks3_data` — it needs one anyway, since today the correct option is only
recoverable by prose matching, which is fragile and is why this went unmeasured.
Then extend `verify_answer_positions.py` to cover the hook corpus with the same
MRB-278 thresholds, and rebalance the 70 hooks. **Who fixes: Code (standing
authority). Effort: small for the key, small for the gate, medium to rebalance.**

### Vocabulary — P8 independently measured the same gap, unit-level

P8-20 reports **25 of 33 KS3 units carry `vocabulary` and author no `keyword`
block — 650 definitions reaching no student — including 11 of 12 physics
units**, and notes *"chemistry missed it because 7 of its 10 units happen to be
in the minority that renders."*

That reconciles exactly with XU-4 above, measured lesson-level: 843 authored
entries, 39 of 182 lessons rendering. Two independent measurements, two grains,
same conclusion. **Report both grains** — the unit-level number explains why the
chemistry audit did not find it.

## XU-5 · The shared `_BEAM` drawer clips its own labels · **S3** · 2 physics lessons

P1 (P1-26) and P2 (P2-22) reported this independently, and P1 diagnosed the cause
correctly: the drawer's 120-unit pans were written for chemistry `c2-06`'s short
"before"/"after" labels, and any page passing longer labels overflows them.
Measured here on every page that uses the drawer.

`_BEAM` (`build_ks3.py:3565`) draws two 120-unit pans with `<text>` labels
centred at x=70 and x=450, inside a **`viewBox="0 0 520 210"`**. The text is not
clipped by the pan — it is clipped by the **viewBox**, at both ends.

| Page | Label | Text width | Rendered span | Cut off |
|---|---|---|---|---|
| chemistry `conservation-of-mass` | "before" | 87 | — | ✅ fits |
| chemistry `conservation-of-mass` | "after" | 65 | — | ✅ fits |
| physics `light/reflection-mirrors-and-scattering` | "i" | 8 | — | ✅ fits |
| physics `light/reflection-mirrors-and-scattering` | "r" | 12 | — | ✅ fits |
| **physics `energy-transfers/simple-machines`** | "your force × your distance" | **344** | x = **−102** → 242 | **102 units off the left edge** |
| **physics `energy-transfers/simple-machines`** | "load force × load distance" | **335** | x = 282 → **618** | **98 units off the right edge** |
| **physics `energy-at-home/reading-a-fuel-bill`** | "every row, added" | **226** | x = **−43** → 183 | **43 units off the left** |
| **physics `energy-at-home/reading-a-fuel-bill`** | "amount due" | 158 | x = 371 → **529** | **9 units off the right** |

**Both labels on both physics pages are clipped.** `simple-machines` is the worst
— a 344-unit label in a 120-unit pan, nearly 3× over, losing a third of itself off
the canvas. On `reading-a-fuel-bill` P2's auditor recorded the visible result as
*"cut-off word fragments"* while the prose beside it instructs the student to read
pans whose labels have been clipped.

Only **2 of the 4** pages that use the drawer are affected, and **both are
physics** — chemistry and the light lesson pass short labels and are fine. So
this is not a chemistry regression risk, but the fix is in shared code.

**Proposed solution:** the drawer must size to its content rather than assume it.
Either (a) widen the pans and the viewBox to fit the longest label passed, computed
at build time; or (b) wrap long labels onto two lines at a sensible break (both
physics labels are "X × Y" and break naturally at the ×); or (c) place long labels
*beneath* the pans rather than inside them, which is what a real balance diagram
does anyway. Recommendation: (c) for labels over ~100 units, (a) otherwise — it
keeps chemistry's drawing byte-identical.

⚠️ **Verify all four pages after the change**, chemistry included — this is shared
code and `conservation-of-mass` is currently correct.

**Who fixes: Code (standing authority). Effort: small.**

## Adjudication · P1-4's vocabulary claim — correct in substance, overstated in scope

P1's record states that all 185 lessons author a `vocabulary` block and **"no
lesson page in the estate renders the definitions"**. The first half is right; the
second is too strong. Measured: **39 of 182 lesson dicts do render them** — 34
chemistry, 4 biology, 1 physics (`describing-motion/speed`).

The physics claim P1 is really making is correct and is the one that matters:
**69 of 70 physics lessons author definitions that never render.** P8-20 and
XU-4 above carry the measured version at both grains. P1's underlying point —
that "joule" is used from lesson 1 and only explained in lesson 8, with the
definition sitting unrendered in the source the whole time — stands and is a good
illustration of the cost.
