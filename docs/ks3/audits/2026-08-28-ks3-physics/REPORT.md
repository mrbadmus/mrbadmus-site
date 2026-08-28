# KS3 PHYSICS — BIG AUDIT — CONSOLIDATED REPORT
### MRB-294 · 28 August 2026 · 70 lessons · 12 units · two personas each

Twelve unit auditors (P1–P12) drove every physics lesson on the live estate at
reading pace, twice — once as an average Year 7–9 student on a 390px phone, once
as an AQA examiner — and ran every instrument to its edges. A thirteenth pass
(the commander's) measured the whole estate from data. This report merges all
thirteen records. **Every number in it was recomputed from the records; no
auditor's self-reported total was carried forward unchecked.**

---

## 1 · HEADLINE

### Is physics September-ready?

**Yes for reading, no for trusting.** All 70 lessons load, render, link and
teach; there is not one broken link in 1,399, not one console error, not one
line of AI slop in some 90,000 words, and the AQA stores-and-transfers model — the
single most common way a KS3 physics course goes wrong — holds on all 70 pages.
A class could be sent to any of these pages tomorrow and would learn from it.

But **63 findings are S1** — the science is wrong or a misconception is being
taught — and the largest cluster of them is in the *instruments*, not the prose.
Nine benches across the estate behave perfectly while demonstrating the negation
of the lesson beside them. That is the worst failure mode this protocol exists to
catch, because it is invisible to every gate in the repo: the code is correct,
the numbers are internally consistent, and the model the child walks away with is
wrong. Separately, **every one of the 70 lesson pages is illegible in its top-left
corner on a phone**, and phones are about half the audience.

**Concrete distance to September:**

| What | Size |
|---|---|
| **Rulings Mide must make before a fix run can start** | **14** (§6) — of which **one (M1) is safety/safeguarding wording, covering eight units**, his gate alone. *(This row originally read "of which 8 are safety/safeguarding wording"; the 8 counts units inside M1, not items in §6.)* |
| **Fix runs** | **4**, plus an unblock step: **F0** the rulings, **F1** the 63 S1s (science), **F2** the 12 shared-chrome and gate fixes, **F3** the 100 S2s (pedagogy), **F4** the 133 S3/S4s |
| **Design batch** | **34 briefs** (count confirmed), of which **11 are drawings that do not exist at all** — a pendulum, the calorimeter's thermometer, the plane-mirror image, the Brownian random walk, the ice/water two-panel, Newton's cannon, **the Sun–Earth force pair**, the parallel-axis orbit, the spread beam, a neutral-object drawing, and the motor's circuit and brushes. *(This list originally ended "and two motor redraws", which omitted the Sun–Earth force pair and double-counted the motor: Group A holds one motor item, and the motor-coil **redraw** is item 17, in Group B — a redraw is by definition not a drawing that does not exist.)* |
| **Blocked on nothing** | **167 findings are Code alone** — no ruling, no drawing — and can start the moment a fix run opens. A further 88 are Code with a wording sign-off, 55 need a Design brief first, 5 are Mide's alone (counted over the 315 as filed, since a deduplicated item still needs its one fix) |

F1 alone is roughly a week. F1 + F2 is the honest "September-safe" line: after
those two the estate teaches nothing false and is legible on a phone. F3 and F4
are quality, not safety, and can run through the autumn term.

### The three worst findings in the estate

1. **XU-1 — the estate holds contradictory definitions of temperature across four
   lessons and three units, and the correct one is met second, outnumbered three
   to one.** ⊕ **Corrected by the cold double-check, 28 Aug** — this entry
   originally read *"three contradictory definitions… the correct one is taught
   first and then contradicted twice"*, naming P11, P1 and C7. A fourth site was
   missed, it is the **earliest** one, and it inverts the narrative. **C1 chemistry
   `changes-of-state` (Year 7, half-term 1)** says *"temperature is a measure of
   **how fast the particles are moving**"* — wrong, and it is a **ladder marking
   criterion**, so the wrong definition is what earns credit in the first half-term
   of Year 7. **P11 (Y7 HT6)** then says *"the average kinetic energy"* — correct.
   **P1 (Y8 HT2)** says *"the average speed of the particles"* — wrong, and its
   ladder criterion marks against the correct answer. **C7 (Y9 HT1)** says *"how
   fast the particles are moving"* — wrong, and its whole latent-heat argument
   depends on it. So a child meets the **wrong** answer at eleven, the right one
   later the same year, and the wrong one twice more. It crosses two subjects, so
   it needs one owner, not two. (Chemistry's own audit of 25 Aug caught neither the
   C7 nor the C1 instance; this audit's first pass caught only C7.)

2. **P1-13 — the flagship bench on `heating-and-thermal-equilibrium` proves the
   opposite of its own lesson.** The thermal-store readout is `n × T` with an
   invented particle index, so it shows a **spark at 1500 °C holding 5 kJ and a
   bath at 40 °C holding 2 kJ — the spark wins, 2.5 to 1**. Directly beneath those
   two numbers the bench's own closing paragraph reads *"the spark is the proof:
   the fastest particles on the bench, and almost no energy at all."* The hook,
   the think-again and the rung-2 feedback all say the bath wins. The real figures
   are out by a factor of about 8,000 (100 kg of water at 40 °C holds 16.7 MJ, not
   2 kJ), and the scale note claiming a 10⁹ range describes a bench whose actual
   range is 1.5 × 10³.

3. **P7-22 — the prism bench draws dispersion backwards, and it is the instrument
   built to kill that exact misconception.** Measured from the served path data:
   every colour is deviated *towards the apex* (a prism deviates towards the
   base), and the deviation runs red > orange > yellow > green > blue > violet —
   `LIGHT-23` exactly, registered on that page as the belief the bench confronts.
   The top-to-bottom colour order still *looks* like a spectrum, which is why it
   survived. Its own ladder rung 1, one screen below, marks the opposite as
   correct.

**Close behind, and in the same class:** **P10-22** (the motor bench draws the
force along the same line as the current, denying "at right angles to both" — the
one new fact the lesson says it rests on); **P11-09** (the Brownian jiggle is
computed with no reference to the speck at all, so a pollen grain and a smoke
speck jiggle identically — the exact opposite of the paragraph beside it);
**P3-11** (two journeys drawn on one set of axes at two different vertical scales,
so the steeper line is the slower one, on the page whose key fact is that
steepness is speed); **P9-1** (the triboelectric ladder ranks acetate below wool,
so the canonical UK school demonstration comes out with the wrong sign).

### What Mide must rule

Fourteen items, listed in full in §6. The eight that block a fix run:

- **Safety and safeguarding wording on eight units** (P2, P5, P7, P8, P9, P10,
  P11, P12) — no auditor drafted a word, per protocol. The one that most needs
  his eye is **P9's lightning-in-a-car stretch**: real safety information about a
  hazard that kills people in the UK most summers, given to twelve-year-olds with
  no framing, and assessed in rung 4.
- **P8-01** — a 400 kV power line used as the example for "volts alone are not
  the danger", which is the one object where volts nearly are; and the sentence
  line-breaks as *"a 400 000 V power line is not / dangerous"*. Science **and**
  hazard description: squarely his.
- **The 840 authored physics bank questions that have never been exported.**
  Product scope: physics cannot be set as a weekly assignment and produces no
  dashboard flashcards, while biology and chemistry can. Lesson pages unaffected.
- **XU-1's replacement Key fact wording** (Key facts are his sign-off).
- **Money: the 27p/kWh and 53p/day tariffs**, undated on eight surfaces.
- **P10-26 — amber as the "selected" colour** on dark benches, against the
  design-system rule that amber means warning/loss. Three units have now stopped
  at this; it is unresolved rather than ruled.
- **P2-26** — whether "Reading a fuel bill" should cover gas (the larger bill in
  most UK homes) or be retitled.
- **M12 — which fix for P8's prefix ladder**, if the Design batch is running.
  *(⊕ Corrected by the cold double-check: this bullet previously named the
  60-character Complete gate (M8). §7's F0 is right that M8 gates nothing — the
  ruled threshold can stand and the silent-button fix needs no ruling — so M8 is
  moved out of the blocking eight and set out below as context Mide will still
  want.)*

**And one he will want to see, though it blocks nothing:**

- **The 60-character Complete gate.** Not a defect claim and not a request to
  relitigate: four units independently produced *correct* answers that left the
  button dead with no signal of any kind (P5's 59-char answer used all three
  required words and satisfied four of five criteria). P8 found the fix already
  written three sections away on the same page — the "Check my five lines" button
  says *"Write at least one line first"*. The threshold can stay exactly as ruled
  and the silence still go.

---

## 2 · PREAMBLE — what was audited, and how it was verified

All facts in this section were measured at run start by the cross-unit pass and
are copied here, not re-derived.

| Fact | Value | Method |
|---|---|---|
| Commit audited | **`38fb338308d3a25f9cd6596afdbce20dc8af9921`** | `git rev-parse HEAD` after `--ff-only` to `origin/main`; tree clean |
| Branch | `feat/content-phys` (fast-forwarded; was 6 behind at session start) | `git rev-list --left-right --count` |
| Physics units | **12** (P1–P12) | `ks3_data/physics_p*_*.py` |
| Physics lessons | **70** | `ks3_data/p*/lesson_*.py` = 70; built non-index HTML = 70. Both agree, and match the brief |
| Physics HTML files served | **83** (70 lessons + 12 unit indexes + 1 subject index) | `find mrbadmus_site/ks3/physics -name '*.html'` |
| **Live-vs-local parity** | **83 / 83 byte-identical** | SHA-256 of every file against `curl -sL https://mrbadmus.com/ks3/physics/...`; **0 differ** |
| Free disk at start | 11 GiB (never fell below the 5 GiB floor) | `df -h .` |
| Accounts | **None created, none needed.** Lesson pages require no sign-in; every auditor browsed signed out throughout | protocol |
| Posture | Read-only. No build, no gate run, no DB write, no `apply_migration` | protocol |

**Because parity is proven, every auditor drove the local copy.** Identical
bytes, faster, and twelve headless Chromes never touched Cloudflare.

⚠️ **Parity method note, for anyone re-running it:** the `.html` URL
308-redirects to the extensionless form. `curl` **without** `-L` returns an empty
body and hashes to `e3b0c44298fc1c14…` (the SHA-256 of the empty string) for
every page, which looks like a total mismatch. The sweep used `-L`.

### Database pools — counts only, per the run constants

| Pool | Physics rows | Total rows | Units present |
|---|---|---|---|
| `ks3_assignment_bank` | **0** | 1356 | B1–B11, C1–C10 |
| `ks3_ladder_questions` | **0** | 226 | B1–B11, C1–C10 |
| `ks3_cards` | **0** | 612 | B1–B11, C1–C10 |

**The 70 lesson pages are unaffected** — the lesson ladder is baked in by
`build_ks3.py` and performs no runtime pool read (CLAUDE.md, MRB-288). What does
not exist is everything downstream: a weekly assignment cannot be composed from a
physics unit, and the dashboard flashcard round has no physics cards. See §6 for
the scope decision, and SYS-9 below for the 840 questions that are authored and
have never shipped.

### Estate-level positives, measured across all 70 lessons

These are findings too. They are the reason the estate is teachable now.

| Probe | Result |
|---|---|
| **Broken internal links** | **0**, out of 1,399 hrefs resolved across 83 files. *Re-derived by the cold double-check and confirmed exactly: 1,399 is the count of internal, path-bearing `href` values (excluding pure `#` anchors and external schemes) across the 83 files; every one resolves, as do all 293 `src` attributes* |
| **Forward `requires` / `assumes`** | **0** — every declared prerequisite points backwards in the *real* delivery order (which interleaves the units across three years and is **not** P1→P12) |
| **AI faff and slop** | 29 named phrases swept: **all zero** except `journey` (39), which is domain vocabulary (a journey on a distance–time graph) |
| **Meta-text / platform self-explanation** | 16 patterns swept: **1 borderline instance in 70 lessons** (`what-a-force-is`: *"The job on this page is…"*, which is lesson framing, not platform meta) |
| **Energy stores vs transfers (the AQA model)** | "types of energy" 0 · "forms of energy" 0 · "heat energy" 0 · "energy is lost" 0 · "transformed into" 0. One "converted into", and it is a **negation** confronting the misconception. ⊕ **"used up" corrected from 0 to 22 by the cold double-check** — the phrase *is* present 22 times across 8 lessons, and **not one instance asserts it**: every one is an MCQ distractor, a "Think again" misconception quoted in order to be demolished, a Key fact saying energy is *never* used up, or a marking criterion crediting *"says the energy is not used up"*. The substantive claim stands and is stronger than the zero suggested — **the estate names the misconception in order to kill it** — but anyone re-running this sweep will get 22, not 0, and must read the contexts |
| **`g` consistency** | `10 N/kg` **×39 in rendered text** (47 in lesson source; the "×49" originally printed here is corrected); one `9.81`, and it is an authored convention note that *confesses* the simplification — *"Earth's true mean value is 9.81 N/kg and varies by about 0.5% between the poles and the equator; 10 is the figure used throughout KS3"* — verified served on `space/gravity-and-weight`. Exemplary |
| **Weight given in kilograms** | **none found** |
| **UK conventions and unit symbols** | Ω/N m/m·s⁻¹/Hz/Pa/kWh all correct in rendered text; **0** US spellings; the *metre* (length) / *meter* (instrument) distinction held correctly across 70 lessons written by different runs |
| **SYS-1** (chemistry's widest defect — "Next in this unit" pointing at the wrong lesson) | **ABSENT in physics.** The string "Next in this unit" appears on **0 of 70** lessons; every card that exists reads the honest **"Connects to"**. *Precision added by the cold double-check: **59 of the 70** lessons carry such a card at all — the other 11 (7 in P1, 2 in P3, 2 in P2) carry none, which is not a defect but does mean "every card" is not "every lesson"* |
| **SYS-10** (authored `ks4_becomes` prose not rendering) | **ABSENT.** 70/70 lessons render the authored prose; 0 bare links. Physics is the model chemistry should adopt |
| **Console errors** | **0** on all 83 pages, before and after interaction bursts, in every unit |
| **The empty `<img src="">` on all 70 pages** | **NOT a defect** — verified. One `<img id="imgPreview">` per page inside the hidden tutor-chat panel; fires no request, renders 0×0, no student ever sees it. Recorded so no future audit spends time on it |

⚠️ **The physics units are NOT taught in P1→P12 order**, and any prerequisite
check that assumes they are is wrong. The published sequence is:
**Y7** P3 → P4 → P11 · **Y8** P5 → P1 → P6 → P7 → P8 · **Y9** P2 → P9 → P10 → P12.
So P11 (matter) precedes P1 (energy transfers), which is why XU-1's "correct
first, contradicted second" ordering is what it is.

---

## 3 · HOW THIS REPORT COUNTS — and what was deduplicated

**315 findings were filed by the twelve unit auditors.** That figure is the count
of distinct `FINDING P<n>-<k>` entries, extracted by ID from the twelve records,
with the severity taken from each finding's own header line. It is not a `grep -c`
of severity tokens: those tokens also appear in cross-references, in summary
tables and in prose, and a naive mechanical recount returns **326** — eleven
phantom findings. Counting by ID resolves the gap exactly, and the by-ID total
agrees with the twelve auditors' own self-reported totals (28+35+25+27+25+18+35+25+19+28+25+25 = 315).

Two housekeeping notes from the recount, both benign:

- **P2 has no P2-30.** Its record explains: the finding was drafted for the `p2-05`
  resource sorter and merged into P2-12, which covers both sorters in one entry.
- **P3 has no P3-17** — an unexplained numbering gap. P3's own severity list and
  total both agree with 25 findings, so nothing is missing.
- **P3's own per-lesson tally disagrees with its own finding headers by one item**
  (it reports S1=8 S2=6 where the headers give S1=9 S2=5; the total, 25, is
  identical). The header is authoritative here — the protocol gives each finding
  exactly one severity, on its header line — so this report uses S1=9 S2=5 for P3.

### Deduplication

**A systemic defect is counted ONCE.** The rule applied: an item is deduplicated
only where **one fix closes every instance and the instances are the same defect**.
Where each instance needs its own authored edit (SYS-5's lying captions, SYS-8's
per-unit option rewrites), the instances stay counted as unit findings and the
systemic entry names the shared remedy — collapsing those would delete real work
from the plan.

| Systemic item | Instances filed | Collapsed to |
|---|---|---|
| **SYS-2** ladder header announces a finished verdict mid-ladder | 10 (P1-27, P2-34, P5-24, P6-04, P7-32, P8-19, P9-19, P10-24, P11-24, P12-23) | 1 |
| **SYS-3** `.ks3-brand` overprints the breadcrumb at 390px | 8 (P1-28, P2-35, P5-25, P6-01, P7-31, P9-18, P10-25, P12-22) | 1 |
| **SYS-V** authored `vocabulary` renders nowhere | 4 (P3-7, P4-07, P7-30, P8-20) | 1 |
| **SYS-B** the `ks3-beam` drawer clips its own text | 2 (P1-26, P2-22) | 1 |
| **XU-1** contradictory definitions of temperature | 2 (P1-14, P11-15) | 1 |
| | **26 → 5** | **21 removed** |

One adjudication changes a severity: **P9-2 is downgraded S1 → S2** (XU-2, set
out in full at the head of P9 in §5 — *not* in §4, as this line originally said).

Two findings were added that no unit auditor could have seen, both from the
cross-unit pass: **SYS-R** (reading load — 152 prose sentences of 42+ words) and
**SYS-F** (eight of P4's nine lessons carry the same cross-year forward reference).

### The arithmetic

| | S1 | S2 | S3 | S4 | Total |
|---|---|---|---|---|---|
| Filed by the twelve unit auditors | 64 | 100 | 45 | 106 | **315** |
| After the P9-2 adjudication | 63 | 101 | 45 | 106 | 315 |
| After deduplication (−26, +5) | 63 | 98 | 36 | 97 | **294** |
| Plus 2 estate-level items only the cross-unit pass could see | 63 | 100 | 36 | 97 | **296** |

### Per unit, deduplicated — and the columns add up

| Unit | Lessons | S1 | S2 | S3 | S4 | Total |
|---|---|---|---|---|---|---|
| P1 energy transfers | 8 | 8 | 8 | 0 | 8 | 24 |
| P2 energy at home | 5 | 7 | 10 | 7 | 8 | 32 |
| P3 describing motion | 3 | 9 | 4 | 5 | 6 | 24 |
| P4 forces | 9 | 4 | 8 | 5 | 9 | 26 |
| P5 pressure | 4 | 3 | 7 | 5 | 8 | 23 |
| P6 waves and sound | 9 | 3 | 5 | 2 | 6 | 16 |
| P7 light | 7 | 5 | 13 | 2 | 12 | 32 |
| P8 electric circuits | 7 | 7 | 9 | 3 | 4 | 23 |
| P9 static electricity | 3 | 3 | 7 | 0 | 7 | 17 |
| P10 magnetism | 5 | 5 | 7 | 1 | 13 | 26 |
| P11 matter | 4 | 5 | 9 | 2 | 7 | 23 |
| P12 space | 6 | 3 | 10 | 1 | 9 | 23 |
| **Unit subtotal** | **70** | **62** | **97** | **33** | **97** | **289** |
| Systemic (§4) | — | 1 | 3 | 3 | 0 | 7 |
| **TOTAL** | **70** | **63** | **100** | **36** | **97** | **296** |

---

## 4 · SYSTEMIC FINDINGS

Seven counted entries, then five patterns whose instances are counted per unit
because each needs its own edit. Every "lessons affected" figure is **computed
from data across all 70 lessons**, not sampled.

---

### XU-1 · Contradictory definitions of temperature · **S1** · 4 lessons, 3 units, 2 subjects
*(Collapses P1-14 and P11-15; extends both to chemistry C7 and C1.)*

⊕ **Corrected by the cold double-check, 28 Aug 2026.** This entry was filed as
*"Three contradictory definitions … 3 lessons, 2 subjects"*, with *"Lessons
affected: 3 of 70 physics + 1 chemistry"* and the table below beginning at P11.
Both figures were wrong and the ordering was wrong. An estate-wide sweep of all
185 KS3 lesson pages for a speed-based temperature statement returns **exactly
three lessons carrying the error** — P1, C7 and **C1 `changes-of-state`, which
the original pass missed entirely** — plus P11, which carries the correct one.
Only **one** physics lesson states the error (P1); the other three sites are the
correct P11 and two chemistry lessons. Half-term placement derived from
`ks3_data/half_terms.py` puts **C1 first**, so the estate does not teach the
right answer first: it teaches the wrong one first, in a marking criterion.

**Lessons affected: 4 — 2 physics (one wrong, one correct) and 2 chemistry (both
wrong).** Measured: `internal energy` appears **27 times on P11's temperature
lesson** (31 across the P11 unit) **and 0 times anywhere in P1**; `thermal store`
appears **34 times across P1 and 0 times in P11**; neither lesson references the
other.

| Order met | Unit · lesson | Delivered | The sentence | Verdict |
|---|---|---|---|---|
| **1st** | **C1** `changes-of-state` | Y7 HT1 | *"Says temperature is a measure of **how fast the particles are moving**."* — **a ladder marking criterion** | ❌ wrong, and it is what earns credit |
| **2nd** | **P11** `temperature-and-internal-energy` | Y7 HT6 | *"Temperature measures the average **kinetic energy** of a single particle…"* | ✅ correct |
| **3rd** | **P1** `heating-and-thermal-equilibrium` | Y8 HT2 | *"Temperature is the average **speed** of the particles."* | ❌ wrong |
| **4th** | **C7** `energy-and-changes-of-state` | Y9 HT1 | *"Temperature is **how fast the particles are moving**."* | ❌ wrong, and loosest |

**The science.** Temperature is proportional to the average *kinetic energy*, not
the average speed. ⟨v⟩ ≠ √⟨v²⟩ for any real distribution, and the definition
breaks across substances: at one temperature heavier particles move more slowly
and lighter ones faster while their average kinetic energies are equal. "Average
speed" makes the false prediction that two gases at the same temperature have
particles moving at the same speed — and P1's own unit compares two materials, in
`conduction` and `insulation`.

**It reaches the marking — twice, not once.** P1's ladder criterion reads *"Says
temperature measures the average **speed** of the particles"*, so a Year 8 who
correctly learned P11's version in Year 7 is answering against a criterion that
names the other phrase. **C1's criterion does the same thing a year earlier**
(*"Says temperature is a measure of how fast the particles are moving"*), so the
wrong definition is the one that earns credit at the first opportunity a child
has to be marked on it. C7 is worse in a different way: its latent-heat plateau
argument *depends* on the wrong definition, so a pupil who accepts the paragraph
must accept the error to follow an otherwise excellent point.

**Proposed solution — one wording at all sites. There are seven, not three.**
Adopt P11's quantity, since it is the correct one.
- **P1** Key fact → *"Temperature is the average kinetic energy of the particles.
  The energy in a thermal store depends on that and on how many particles there
  are."* (The second sentence is already there and already correct.)
- **P1** ladder criterion → credit "average kinetic energy" (accept "average
  speed" as a partial for one cycle if a soft landing is wanted).
- **P1** hook reveal — ⊕ **added by the cold double-check; the original solution
  would have left it standing.** The same page's hook reveal reads *"Temperature
  tells you **how fast the particles are moving** on average."* It is a third site
  on one lesson and needs the same edit. (The bench prompt's *"how fast its
  particles are moving"* is an instruction to move a control, not a definition,
  and can stay.)
- **C1** `changes-of-state` ladder criterion — ⊕ **added by the cold
  double-check.** → *"Says temperature is a measure of the average kinetic energy
  of the particles."*
- **C7** → *"Temperature is a measure of the average kinetic energy of the
  particles."* The surrounding argument survives unchanged and is **easier** to
  make with the correct definition. **C7 carries a second site** — *"A thermometer
  measures how fast the particles are moving"* — which needs the same edit.
- **P11** Key note → tighten *"of a single particle"* to *"per particle, on
  average"* (P11's body text already gets this right).
- **One bridging clause in P1** naming internal energy and thermal store as one
  quantity under two names. A student should not have to work that out.

**Who fixes:** Code (standing authority — science correction) + **Mide sign-off**
on the final Key-fact wording. **It crosses the physics/chemistry boundary, so it
needs one owner, not two.** **Effort:** small (six sentences and two criteria — no
argument anywhere has to be rebuilt).

---

### SYS-3 · The header wordmark overprints the breadcrumb at 390px · **S3** · **70 / 70 LESSONS**

Chemistry's C3-03, present on **every physics lesson page at phone width**.
Measured, not sampled: all 70 lessons driven at a true 390px viewport (device
metrics override, so the media queries fire as on a real phone).

**What happens.** `.ks3-brand` sits in `.ks3-nav-rail` with `flex-shrink: 1`,
`min-width: 0`, `overflow: visible` (all three confirmed from computed style).
Its content needs **177px**, on every one of the 70 pages. At 390px the rail
shrinks the *box* to **53–137px** depending on breadcrumb length. Because
overflow is visible the wordmark neither clips nor wraps — **it paints straight
out of its box**, through the divider, over the first crumb.

⊕ **Magnitudes corrected by the cold double-check, 28 Aug 2026.** The table below
originally gave an overflow range of *"+60px to +124px"* and a worst five of
+124/+116/+110/+108/+108. Those figures are **about 26px too large across the
board** and they contradicted this finding's own strike paragraph, which gives
P11 as +98. Re-measured on all 70 lessons with a `Range` over the wordmark's text
node against `trail.getBoundingClientRect().left`: the range is **+14px to
+98px**, median +60. **The defect is 70/70 either way** — every page overprints;
only the sizes were overstated.

| | |
|---|---|
| Lessons measured at 390px | **70** |
| Lessons where the wordmark paints into the breadcrumb | **70** |
| Lessons clean | **0** |
| Overflow range | **+14px to +98px** (median +60; 36 of 70 at +60 or worse) |

Worst five: P11 `temperature-and-internal-energy` (+98), P6
`transverse-waves-and-superposition` (+90), P10 `the-earth-is-a-magnet` (+84),
P10 `how-a-motor-works` (+82), P10 `magnets-and-poles` (+82). Least bad, and
still broken: P4 `friction` (+14), P7 `refraction` (+17). A reader sees
`MrBadm[Describi]usAI` — three overlapping strings, none readable.

> ⚠️ **THE TEST THAT MISSES IT.** The layout boxes never intersect, so a
> `getBoundingClientRect()` overlap test returns **false** and the defect looks
> absent. `document.scrollWidth` is exactly 390 and no per-element overflow sweep
> fires either. **Three unit auditors (P11, P4, P8) reported SYS-3 ABSENT on
> exactly this evidence, and all three are STRUCK** — re-measured on their own
> pages with a `Range` over the wordmark's text node: P11
> `temperature-and-internal-energy` box 53px, ink overprints the trail by **98px**;
> P4 `what-a-force-is` overprints by **34px** and `air-and-water-resistance` by
> **53px**; all seven P8 lessons collide. P10's auditor diagnosed the false
> negative *before* it was found: *"I nearly recorded it absent… the measurement
> needs a `Range` over the text node."* The only valid test is
> **`brand.x + brand.scrollWidth > trail.x`**. The three strikes affect no other
> finding in those three records.

**Proposed solution** — two rules in `shared/ks3.css`, no content touched:
1. `.ks3-brand { flex-shrink: 0; min-width: max-content; }` — the brand stops
   being the thing that gives way.
2. `.ks3-trail { min-width: 0; overflow: hidden; }` with ellipsis truncation —
   which the trail **already does** (it renders "Describi…" and "Pressure …"), so
   the machinery exists and is simply applied to the wrong element.
   Fallback if 177px of wordmark plus a usable trail still will not fit: hide the
   wordmark below ~420px and keep Design's chevron, which is recognisable alone.

⚠️ **Shared KS3 chrome — the same fix lands on every biology and chemistry lesson
too, and chemistry's C3-03 is the same defect. Fix once, verify across all three
subjects.** Add a **Range-based ink-overflow assertion** to the 390 sweep so a
box-clean page can never hide it again.

**Who fixes:** Code (standing authority). **Effort:** small.

---

### SYS-2 · The ladder header announces a finished verdict after one rung · **S3** · **70 / 70 LESSONS**

Reported present by all twelve units (ten filed it; P3 and P4 recorded it in
their probes). The shared kernel's header flips from *"Not started yet."* to
*"**You got 0 of 4.** You marked rungs 3 and 4 yourself."* the instant the **first**
rung is answered — a past-tense finished verdict with three rungs untouched and
both self-marked rungs never opened. It is delivered into an `aria-live` region.

Two units sharpen it. **P10:** two of the four rungs are self-marked and cannot
contribute to "you got n of 4" until the student marks them, so the header asserts
a score about rungs that are not machine-marked — *precisely the reading
`is_correct` NULL is ruled never to carry*. **P9:** a student who gets rung 1
wrong is told they scored zero out of four at the worst possible moment.

**Proposed solution:** progress phrasing while any rung is unanswered ("1 of 4
rungs done"); the tally sentence only in the end state. **One branch in the
kernel's header function fixes every lesson in both key stages** — aggregate with
chemistry's C2-3 / C3-02 rather than fixing twice. P12-23 adds one condition: hold
the **"Retry my misses"** control until every rung has been attempted (it appears
at the same moment and offers to reopen misses that cannot exist yet), and P12-04
notes the identical shape in a *second* component — the CFIFA tally prints "0 of 5
lines you had. Rewrite the ones you missed" before a single line can be ticked.

**Who fixes:** Code (standing authority). **Effort:** small.

---

### SYS-V · 246 authored vocabulary definitions never reach a physics student · **S2** · **69 / 70 LESSONS**

Two independent measurements at two grains, both reported here because the
unit-level one explains why the chemistry audit missed it.

⊕ **Three denominators corrected by the cold double-check, 28 Aug 2026** (185 for
182, 852 for 843, 643 for 650), each re-derived by walking the Python AST of all
185 `lesson_*.py` files rather than by regex — a regex over `"vocabulary"` blocks
overcounts biology, whose entries nest. **Every load-bearing figure in this
finding survived unchanged**: 246 physics definitions, 39 lessons rendering,
34/4/1 by subject, 25 of 33 units, 11 of 12 physics units. Only the totals moved.

**Lesson grain (cross-unit + P7-30):** every one of the **185** KS3 lessons
authors a `vocabulary` list — **852 entries key-stage-wide, 246 of them physics**
(biology 309, chemistry 297) — each a term plus a written definition. **39 of 185
lessons render them. In physics, exactly one does**
(`describing-motion/speed` — verified as the only physics page in the estate
carrying a `ks3-keyword` block), which proves the mechanism works.

| Subject | Lessons rendering vocabulary flip cards |
|---|---|
| Chemistry | **34** |
| Biology | 4 |
| **Physics** | **1** |

**Unit grain (P8-20):** **25 of 33 KS3 units carry `vocabulary` and author no
`keyword` block — 643 definitions reaching no student, 236 of them physics —
including 11 of 12 physics units** (P3 is the sole exception, and it is the unit
that renders). As P8 puts it: *"chemistry missed it because 7 of its 10 units
happen to be in the minority that renders."*

**Why, and it is not a renderer bug.** `build_ks3.py`'s `r_keyword()` renders
vocabulary as flip cards and works. It only fires when a lesson's `core` authors a
**`keyword` block naming its terms**. A lesson can author fifty definitions; with
no `keyword` block, `r_keyword` is never called and every definition is dead. The
generator's own comment records the same shape being found once before.

**The definitions are good, and several are better than the prose treatment.**
P1's *"wasted energy — energy that ends up in a store you did not want filled…
It has not been destroyed, only spread out too thinly to be useful."* P4's
*"moment — not a newton; a moment is not a force."* P7's *"denser — used here of
a transparent material that slows light more."* **None of those strings appears
anywhere in the built estate.** It has a named victim in this audit: **P7-11**
flags "denser" used unglossed in the refraction Key fact — and P7's own authored
vocabulary already contains the definition that would have fixed it.

⚠️ **Partial mitigation, so the finding is not overclaimed:** the *term names*
(not the definitions) are aggregated into a "Words this unit gives you" chip box
on the year/half-term browse pages, capped at eight, in mixed casing. So a student
sees some physics words listed on a page they may never visit, and the meanings
nowhere.

**Proposed solution:** add a `keyword` block to each physics lesson's `core`,
naming the terms that lesson introduces, placed after the first teaching block as
chemistry does. **The definitions, the renderer, the flip interaction, the
rail-stop anchor and Design's heading treatment all already exist and are proven
on 39 lessons — this is wiring, not authoring.** Mide's eye is wanted on two
things only: which terms each lesson should front (the lists are longer than a
card grid should show — chemistry heads them "Four words"), and whether any
definition needs updating before a class reads it. Add a **build warning**: a
lesson that authors `vocabulary` and places no block consuming it is authoring
into a void, and today that fails silently. ⚠️ **Biology is in the same position
(4 of its lessons render); take the decision once for the key stage.**

**Who fixes:** Code (wiring); Mide picks the per-lesson shortlist. **Effort:**
medium (70 lessons × one block, mechanical, no new prose).

---

### SYS-R · Reading load — 152 sentences of 42+ words, and they are the estate's best writing · **S2** · concentrated in P10, P5, P9

**Whole estate: roughly 89,000–99,000 prose words over 70 lessons — call it
~1,300–1,400 words per lesson (see the method note at the foot of this finding;
the "92,585 / 1,322" originally printed here does not reproduce). Mean sentence
15.9 words, median 13, p90 30 — these three, and every sentence-count column
below, were independently confirmed.** For ages 11–14 that is a sound target
and most of the estate sits comfortably inside it. The spread is the finding.

| Unit | Lessons | Words/lesson | >30-word sentences per lesson | >40-word per lesson |
|---|---|---|---|---|
| **P10 magnetism** | 5 | 1450 | **12.2** | **5.2** |
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

**P10 carries 17× describing-motion's rate of very-long sentences**, and P10 is
the newest unit with the least classroom exposure. Inspecting the 152 sentences of
42+ words shows what they mostly are: **honesty footers and convention notes** —
the bench's modelling assumptions, what a figure is rounded from, why a number is
not given in newtons. Verbatim, 67 words, `static-electricity/forces-between-charges`:
*"Both charges are treated as equal in size and as sitting at the centre of each
sphere, and the strength is reported as a relative figure with the closest fully
charged case set to 100 — no force in newtons is given anywhere on the bench,
because the equation for it is beyond this stage and any number in newtons here
would be invented rather than measured."*

**Proposed solution: keep every one of these notes — they are the estate's
integrity and deleting them would be a regression.** Split them at the semicolons
and em-dashes into two or three sentences each, which costs nothing and halves the
load; and give a convention note a consistent visual treatment marking it *for
reference, not for reading now*, so a struggling Year 7 knows they may pass it.
Start with P10, P5 and P9. **Who fixes:** Code, wording past Mide. **Effort:**
medium (152 sentences, mechanical, no science changes).

⚠️ **Method correction, recorded deliberately.** A first attempt stripped all tags
and split on sentence punctuation, reporting a mean of 20.1 words and "sentences"
of up to 232 words. Those were artefacts — MCQ options and bench labels are
separate block elements with no terminal punctuation, so tag-stripping
concatenates them. **Those numbers are withdrawn.** The figures above come from
`<p>` elements only, excluding option/label/gauge/dial/chip/readout/crumb classes.
Anyone re-running this must exclude the control chrome.

⊕ **Second method note, added by the cold double-check, 28 Aug 2026 — the stated
method is incomplete, and the word totals do not reproduce under it.** Re-running
exactly as described (`<p>` only, those seven classes excluded) gives **99,319
words, mean 12.9, median 10, p90 28** — a mean three words below the one printed.
The gap is a filter the method does not mention: **counting only segments that
actually end in terminal punctuation**, which drops ~1,850 caption and label
fragments. Under *that* rule the sentence statistics reproduce almost exactly —
**mean 15.8, median 13, p90 30, and 151 sentences of 42+ words against the 152
claimed** — so the **sentence** figures above, including the whole `>30` and
`>40` columns of the per-unit table and the P10-versus-P3 ratio, all stand and
were independently confirmed. The **word** figures do not: the true total is
**88,572 (strict) or 99,319 (loose)**, and 92,585 sits between the two under
neither rule. Treat every "words per lesson" number in this section, and the
"92,585 words" in §1, as **approximate to ±7%**. Nothing in the finding's
substance turns on them; the load-bearing 152 sentences of 42+ words is real.

---

### SYS-F · Eight of P4's nine lessons carry the same cross-year forward link · **S2** · 10 lessons

38 `references` point forward. Because they render as **"Connects to"** — which
does not claim to be next — a forward pointer is not the lie chemistry's SYS-1 was,
and 28 of the 38 move by one or two half-terms inside the same year. **Ten cross a
school year**, so a Year 7 clicking one lands in a Year 8 lesson they have no
grounding for:

- **Eight of P4's nine lessons** (`what-a-force-is`, `drawing-and-adding-forces`,
  `balanced-and-unbalanced`, `what-forces-do-to-motion`, `friction`,
  `air-and-water-resistance`, `moments`, `springs-and-hookes-law`) → **P5
  `pressure-force-over-area`** (Y7 HT2–4 → Y8 HT1).
- P11 `brownian-motion` and `temperature-and-internal-energy` → P1
  `heating-and-thermal-equilibrium` (Y7 HT5–6 → Y8 HT2).

Eight identical forward links across one unit is the signal: it reads as a
template applied, not eight considered links. Verified as unconditionally rendered
(a live `<a href>` on `what-a-force-is`, no gating).

**Proposed solution — two options, because one touches the ruled covered-lessons
scoping and this report does not relitigate that.** (a) Leave them and let the
"Connects to" heading carry it — defensible, no work. (b) Drop
`pressure-force-over-area` from the seven P4 lessons where it is template-applied,
keeping it on `what-a-force-is` where the connection is genuinely instructive.
**Recommendation: (b)** — eight identical forward links teach a student that the
card is noise. **Who fixes:** Code once the option is picked. **Effort:** small.

---

### SYS-B · The `ks3-beam` drawer clips its own text at every viewport width · **S3** · 2 lessons (+3 cosmetic)

`_BEAM` in `build_ks3.py` draws two pans 120 units wide inside a 520 × 210
viewBox and centres a 27px `<text>` on each, with `overflow: hidden`. That geometry
was written for `c2-06`, whose labels are "before" and "after" (6 and 5
characters). Two physics lessons pass 16–26-character labels:

- **`energy-transfers/simple-machines`** — the pans read *"ce × your distance"* and
  *"load force × load d"* at **1280px and at 390px**. This is the drawn statement
  of the lesson's central relationship, and it is unreadable. Measured: the two
  `<text>` nodes span 313→624 and 660→963 against an svg spanning 405→875.
- **`energy-at-home/reading-a-fuel-bill`** — the caption renders *"ducts — triangle
  for one row, balance"*, the left pan *"ry row, added"*, the right loses its final
  letter. **169 units of overflow.** It is the only figure on the lesson and it
  carries the claim the lesson exists to make.

An estate-wide sweep of all 185 KS3 lesson pages found SVG text escaping its own
SVG on **five** pages; `ks3-beam` is the worst two. ⊕ **Independently re-run by
the cold double-check — the same five pages, and no sixth.** The finding's scope
is exactly right; two magnitudes are corrected. The fuel-bill caption overflows by
**187 units**, not the 169 printed above. And the other three
(`upthrust-floating-and-sinking` **+28**, `echoes-reflection-and-absorption`
**+39**, `how-sound-is-made` **+29**) overflow by **28–39 units**, not "3–26" —
still cosmetic against viewBoxes of 700–1000, but all three exceed the ceiling
this sentence claims for them.

**Proposed solution:** fit the text to the frame rather than the frame to the
drawing — widen the viewBox to ~760 and size the pans to their content, or split
the caption onto two `<tspan>` lines, or (best at 390px) move the caption into an
HTML `<p>` beneath the SVG where it can wrap. Then **add a build assertion that no
`<text>` extends beyond its own `viewBox`** — the drawer already carries five
assertions of exactly this character, and this class would have been caught by a
sixth. **Who fixes:** Code; geometry past Design. **Effort:** small per page,
medium with the assertion.

---

## 4b · SYSTEMIC PATTERNS — counted per unit, shared remedy named once

These five are real patterns with a shared root, but each instance needs its own
authored edit, so the instances stay in the per-unit counts.

### SYS-5 · Fixed captions that lie at reachable states · **PRESENT in 11 of 12 units · 30+ instances**

The chemistry audit's SYS-5, and the largest single family in this audit. Every
unit but one found it. The shape is always the same: a caption keyed to a *branch*
rather than to the *value*, written for the expected state, surviving to a state
the controls reach.

The instances are listed in §5 under their units. The worst, by consequence:

- **P8-05** — the size adjective is keyed to the component's authored band, so
  0.300 A is called *"a large current"* and 1.200 A is called *"only… the reading
  is small"*. Four times the current, called small. It teaches that "large" and
  "small" belong to the component, on the lesson whose whole thesis is that current
  depends on V and R together.
- **P2-11** — the button labelled *"Jump to the crossover"* lands on the one state
  where the caption reads *"**Past** the crossover… has now transferred more"* over
  two totals printed **equal**.
- **P3-1** — a fixed closing panel *prescribes a method* ("average the three times,
  divide the distance by it") that is invalid for the readings the instrument just
  allowed the student to take.
- **P10-8** — the setup note calls the gap *"the strongest part of the whole map"*;
  the bench reads **9.5** there against **100.0** at the pole faces.
- **P12-05** — *"Move the slider and every bar changes"*, false in **all 16 states**:
  the slider changes no bar at all.

**Shared remedy, in addition to the per-instance wording fixes:** extend the bench
guard chemistry's audit proposed — **assert that a rendered caption's vocabulary
agrees with the value it sits beside** (a "far too weak to see" must not accompany
a full-length arrow; a note quoting a value equal to `data-amp-mm` must only fire
in a state whose readout equals it; a "sinks" remedy naming a mass must, re-fed to
the same predicate, yield "holds"). That guard would have caught at least eleven
of the instances below.

### SYS-8 · Answer tells outside the gates · **FOUR distinct forms** · 11 of 12 units

`verify_answer_positions.py` (MRB-278) watches answer **position** in the **ladder
and the bank**. It does not watch option **length**, option **shape**, or the
**hook** and **bench-gate** corpora at all. All four gaps were measured.

**Form 1 — position, in the hook corpus, which no gate reaches.** The hook carries
no `answer` key in the built page, so the correct option is recoverable only by
matching the `reveal` prose back to an option, which is why it has escaped
measurement entirely. Three independent measurements agree on the substance:

| Source | Method | Result |
|---|---|---|
| **P4's auditor** (report this one) | resolved 62 of 70 hooks | **A 13 · B 32 · C 13 · D 4** — **B on ~52%**, and B on 7 of P4's own 9 lessons |
| P8's auditor | its own 7 lessons | index **0 (A) on 6 of 7**, longest in 5 of those |
| Cross-unit check | deliberately conservative matcher, resolved only 31 of 70 | A 6 · B 15 · C 7 · D 3 — **B 48%** |

P4's numbers are the finding; the cross-unit figure is corroboration from a
different method (it refuses a match when the top two options score within 0.15 —
the right posture for a check, the wrong one for a headline). **P8 is the outlier
that skews to A**, and its auditor was right about its own unit. P2 (B 5/5), P7
(B 6/7) and P9 (A 3/3) are the other single-unit extremes.

⊕ **Settled by the cold double-check, 28 Aug 2026 — measured from ground truth,
not matched from prose, and P4's auditor was exactly right.** The premise above is
half wrong in a way that matters. The hook carries no `answer` key **in the built
page** — true — but it **does carry one in `ks3_data`**: `phenomenon` is a
top-level key on the lesson dict with `options` and an integer `answer` beside it.
Reading it directly across all 70 lessons resolves **62** (the 8 that do not
resolve are **all of P1**, whose hook is shaped differently — not a scattered 8)
and gives **A 13 · B 32 · C 13 · D 4, B on 51.6%** — **identical, to the last
finding, to P4's prose-matched result**, including "B on 7 of P4's own 9 lessons",
P2 5/5, P7 6/7, P9 3/3 and P8's 6-of-7 skew to A. Prose-matching reproduced the
ground truth perfectly; the finding needs no hedging at all.

⚠️ **This kills proposed solution 1 below, which would not fix the stated problem.**
Solution 1 asks to *"give the hook an explicit `answer` index in `ks3_data`"* — but
that index **is already there**, on 62 of 70 lessons. Nothing needs authoring. The
real gap is that (a) `build_ks3.py` does not emit it to the page and (b)
`verify_answer_positions.py` never reads it. **The correct fix is to point the
existing gate at the key that already exists** — a change to the gate, not to 70
data files — plus giving P1's eight hooks the same shape as the other 62. That is
substantially less work than solution 1 implies, and it can land immediately.

⊕ **One measurement the original pass did not take: the hook corpus carries the
Form 2 length tell more heavily than the bank does.** On the same 62 hooks the
correct option is **uniquely the longest on 29 of them — 46.8%**, against 35.1% in
the 840-question bank and 25% by chance. The hooks are **live on the pages now**,
unlike the bank. Whatever is done about Form 2's authoring should start here, not
with the bank.

**Form 2 — length, across all 840 authored bank questions, and it runs BOTH ways.**

| | Count | Share | z vs 25% |
|---|---|---|---|
| Correct is uniquely the **longest** | 295 | **35.1%** | **+6.8** |
| Correct is uniquely the **shortest** | 127 | **15.1%** | **−6.6** |
| Correct is an **extreme** (either end) | 422 | 50.2% | ≈ chance |

**A student who ignores the physics entirely and always picks the longest option
scores 35% instead of 25%.** Worst units: **P11 56.2%**, P5 45.8%, P2 43.3%. *In
P11 a student picking the longest option gets more than half of the unit's bank
right without reading a word of physics.* The bias is **directional, not extremal**
— which is why a symmetric test finds nothing overall — but P11 (70.8%) and P3
(69.4%) carry a large extremal signal from both ends at once.
**Position, by contrast, passes comfortably:** across all 840, index 0/1/2/3 =
23.5% / 26.3% / 26.7% / 23.6%, and seven of twelve units cycle the index
deliberately (P3's source file documents it). MRB-278 is doing its job.

**Form 3 — the em-dash shape tell on recall rungs · 17 of 70 lessons, 7 units ·
PHYSICS ONLY.** On 17 recall rungs the correct answer is the **only option without
an em-dash tail**: the right answer is a bare quantity and all three distractors
carry a clause explaining the error that produced them.

> P5 `pressure-force-over-area` rung 1 — correct: **"2000 Pa"**; distractors:
> *"180 Pa — multiply the force by the area"*, *"2000 N — a press on the floor is a
> force…"*, *"0.0005 Pa — divide the area by the force"*.

**A student can answer all seventeen without doing any physics: pick the option
with no dash.** By unit: **P5 4 of 4 — 100%** (which is why its auditor saw the
pattern), P6 3, P8 3, P4 2, P7 2, P12 2, P11 1. Re-run across **every KS3 lesson in
all three subjects: all 17 are in physics; biology and chemistry return zero.** It
is not a platform-wide habit and needs no cross-subject fix.
*(P12's auditor independently measured a related mirrored-**length** threshold over
all 370 four-option sets in KS3 and reported **26 hits across 14 units**, 24 of them
ladder recall. The two tests measure different features — dash presence versus
strict length-mirror — and agree on the substance: one construct on recall rungs,
not a scatter of slips. Both numbers stand with their definitions.)*

**Form 4 — bench chip and sort-key order.** P1-8: two sort benches whose answer
keys alternate perfectly by position (`0,1,0,1`), so a student who spots the
alternation after two items scores the rest without reading — on benches whose
whole purpose is that the reading is the work.

**Proposed solution, in four parts:**
1. **Give the hook an explicit `answer` index in `ks3_data`.** It needs one
   anyway: today the correct option is recoverable only by prose matching, which is
   fragile and is why this corpus went unmeasured for a year.
2. **Extend MRB-278's deterministic build-time shuffle to `phenomenon.options` and
   to every instrument `gate.options`**, keying reveals and per-option feedback by
   option identity rather than index — the ladders already do this and the
   mechanism exists.
3. **Make the tell gate two-sided and shape-aware**: flag a corpus where the
   correct option is uniquely longest **or** uniquely shortest materially more
   often than chance, flag **per unit as well as per corpus** (P11 and P3 are
   invisible in the estate-wide total), and flag any rung where the correct option
   is the unique odd-one-out on a structural feature (dash present/absent, trailing
   clause, units present/absent). Add a **per-rung scope** to the ladder check:
   P4's ladder passes MRB-278 on the pooled count while its recall answers are A/C
   on all nine lessons and its apply answers B/D on all nine — a fully learnable
   pattern that a pooled count cannot see.
   ⊕ **Widened by the cold double-check, 28 Aug 2026: this is three units, not
   one, and P4 is not the worst of them.** All 70 physics ladders were read from
   `ks3_data`. Estate-wide the position is healthy (recall 22/12/24/12, apply
   11/24/12/23 across A/B/C/D), which is exactly why a pooled check sees nothing.
   Per unit, **P2, P4 and P5** each place **every** recall answer in {A, C} and
   **every** apply answer in {B, D}:

   | Unit | Recall answers, in lesson order | Apply answers | Learnable after |
   |---|---|---|---|
   | **P2** | 0 · 2 · 0 · 2 · 0 | 1 · 3 · 1 · 3 · 1 | **2 lessons** — it is a perfect alternation |
   | **P5** | 0 · 2 · 0 · 2 | 1 · 3 · 1 · 3 | **2 lessons** — perfect alternation |
   | **P4** | 0 · 2 · 0 · 2 · 0 · 2 · 0 · 2 · **2** | 1 · 3 · 1 · 3 · 1 · 3 · 1 · 3 · **3** | 2–3 lessons; breaks only at lesson 9 |

   **P2's and P5's are cleaner than P4's** — they alternate without a single
   break, so a student who notices it after two lessons is right every time
   afterwards. The other nine units cycle their indices genuinely and are fine.
   The per-rung scope must therefore run **per unit per rung**, and it will flag
   three units on the day it lands.
4. **Authoring, and the remedy differs by direction.** Where the correct answer is
   long: **lengthen the distractors** so each carries its own plausible reasoning —
   do not shorten the correct answers, the reasoning in them is the teaching, and a
   curt wrong option is easy to dismiss for the wrong reason. Where the correct
   answer is bare: **give it a clause of the same shape** — *"2000 Pa — 600 N shared
   over 0.30 m²"* confirms the method as well as the answer, which is what a recall
   rung is for. P6 notes the remedy already exists on three of its six calculate
   rungs, so the pattern to copy is in the estate.

⚠️ **Scope note.** Form 2 measures the **authored bank**, which has **0 rows on
production**, so no student is exposed to it *today*. It matters at the moment the
export runs — which is why it belongs in the same decision as SYS-9 below.
Form 1 (hooks), Form 3 (rungs) and Form 4 (benches) are **live on the pages now**.

### SYS-A · No ray, force vector or field line in physics carries an arrowhead · S1/S4 · estate-wide

| Probe | Physics files | All KS3 |
|---|---|---|
| `marker-end` | **0** | 2 |
| `marker-start` | **0** | 0 |
| `<marker` | **0** | 2 |

**No SVG in any of the 70 physics lessons defines or uses an arrowhead marker.**
The `ks3-mark-arrow` hits on the light pages are *navigation* arrows in the end
matter. This is not a limitation of the stack: `ks3.js` hand-composes arrowheads
as path segments on P7's race lanes and object arrows and on P10's `out-in` tile —
**rays and field lines are the one thing that never get them.**

It lands hardest as **P7-04 (S1)**: a line with no arrow is not a ray, arrows on
rays are the first thing a UK teacher marks and a standard GCSE mark loss, and on
three P7 diagrams the absence makes the drawing readable as the *opposite* of the
lesson — the reflection bench is mirror-symmetric so nothing distinguishes
incident from reflected; the refraction block read right-to-left shows light
bending *away* from the normal on entering glass; and the eye bench draws
undirected lines between a scene and an eye in the two lessons whose registered
misconception is *your eyes send something out*. **P10-10** is the same defect on
field lines, on the lesson that makes the arrow a rule.

**Proposed solution:** define **one shared `<marker>` arrowhead in the KS3 SVG kit**
and apply it per drawer to every ray, force vector and field line — **not** to
construction lines (normals, ghost paths, the deliberately-impossible "no crossing"
tile), which must stay headless so the distinction reads. Where a path is a
multi-segment polyline, split it or use a mid-path marker so the head sits at the
far end of travel. Then add one sentence to P7's reflection explainer: *"a ray is
always drawn with an arrow on it, because which way the light is going is part of
the answer"* — the unit currently never tells a student to draw one while its GCSE
card promises "ray diagrams". **Who fixes:** Code + a Design brief for placement
convention. **Effort:** medium.

### SYS-D · Two units ship no drawings at all · S2 · P11 (4 lessons) + P12 (6 lessons)

`figures: []` on all ten lessons of **P11 "Matter and the particle model"** and
**P12 "Space"**; zero `<canvas>` and zero content `<svg>` on any of their pages
(the 9–11 SVGs per page are brand, rail and end-matter chrome). Between them they
own: the particle model, Brownian motion, why ice floats, gravity, orbits, and the
seasons. **"Matter and the particle model" contains no drawing of a particle.**

The six drawings that are missing are named in the Design pile (§5b): the Brownian
random walk, the ice/water two-panel, Newton's cannon, the Sun–Earth force pair,
the parallel-axis orbit and the spread beam. Five of the six are the canonical
picture of their topic and are in every KS3 scheme in the country, because each is
the one idea a single picture settles and a paragraph does not.

### SYS-9 · 840 physics bank questions are authored and have never shipped · Mide pile

Refining the row counts, because "physics has no bank" would be the wrong
conclusion. **Physics bank questions exist, fully written**, in
`ks3_data/p<N>/questions_*.py` — twelve per lesson, banded easier/harder, four
options each, a `why` on every distractor:

| P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 | P11 | P12 | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 96 | 60 | 36 | 108 | 48 | 108 | 84 | 84 | 36 | 60 | 48 | 72 | **840** |

**840 authored in the repo. 0 in `ks3_assignment_bank` on production.** The export
that shipped biology and chemistry (1,356 rows) never ran for physics. Same for the
ladder mirror and the cards. **This does not affect the 70 lesson pages.** It means
physics cannot be set as a weekly assignment and produces no dashboard flashcards —
the largest single gap between physics and the other two subjects. Effort to close:
an export run, not authoring. **Fix SYS-8 form 2 before the export runs, not
after.** ⚠️ The number 840 also appears in an older memory note as "KS3's old bank
size"; that is a coincidence — this 840 is 70 lessons × 12 and is a different
quantity.

---

## 5 · PER-UNIT FINDINGS

P1 → P12, severity order within each unit. Every finding keeps its proposed
solution. Full evidence — driven DOM states, screenshots, path data, quoted
source — is in `records/p<N>.md` against the same ID. Findings moved into §4 are
listed at the head of each unit as a reminder, not repeated.

---

### P1 · Energy transfers · 8 lessons · **24 findings** (S1 8 · S2 8 · S3 0 · S4 8)
*In §4: P1-14 → XU-1 · P1-26 → SYS-B · P1-27 → SYS-2 · P1-28 → SYS-3.*

**S1**
- **P1-13** · `heating-and-thermal-equilibrium` · two-quantities bench — **the unit's worst finding, and one of the estate's three.** Thermal store computed as `n × T` with an invented index (spark 3 / mug 22 / bath 60), so the spark at 1500 °C shows **5 kJ** and the bath at 40 °C shows **2 kJ**; the bench contradicts its own hook, think-again, rung-2 feedback and closing paragraph, and its scale note claims a 10⁹ range over a bench spanning 1.5 × 10³. Real figures out by ~8,000×. → Make `n` a real relative particle count (spark ≈ 0.00045, mug 1254, bath 418000, from mass × specific heat), extend the formatter to MJ and sub-joule, normalise the bar logarithmically instead of the hard-coded ×22, **and add a guard to `r_two_quantities` refusing a payload whose largest-amount-at-lowest-temperature store is not greater than its smallest-amount-at-highest-temperature store — because that ordering IS the lesson.** *Code + Mide sign-off (new values); medium.*
- **P1-1** · `energy-stores` · store-audit ledger — the columns ask which stores *hold* energy and the machine marks which stores *change*, so physically true ticks are marked wrong (thermal on a braking car, chemical on a car with a fuel tank, nuclear on a kettle), contradicting the lesson's own key fact. → Reframe *holds* → *changes*: headings "Emptied" / "Filled", prompt *"Tick the store that empties and the store that fills"*; one clause on the sc1 idealisation in the register sc5 already uses. *Code + Mide sign-off (idealisation clause); small.*
- **P1-5** · `energy-transfers-before-and-after` · hook — the reveal endorses *"Energy has no mass"* (false: 40 kJ is 4.4 × 10⁻¹³ kg) and, worse, **the distractor is the physically correct account** — "the balance is not sensitive enough" is right, and the milligram premise was chosen deliberately. → Option B → *"Energy is not a substance — it is a number, so there is nothing to pour out"*; replace option A with a distractor that is actually wrong ("Batteries are sealed, so nothing can get out"). Nothing about mass–energy equivalence belongs at KS3; the fix is to stop asserting its negation. *Code + Mide sign-off; small.*
- **P1-9** · `conservation-of-energy` · the "Continue" control at rest — pressing it silently restarts the run and **empties the thermal store back into the gravitational and kinetic ones**: 120 J thermal at rest becomes 15 J thermal / 104 J gravitational 1.2 s later. The total is preserved so no gate catches it, but a child watches 105 J flow spontaneously out of the surroundings — a second-law violation shown as normal behaviour, on the page arguing a pendulum's energy cannot come back. The label is what makes it harmful: "Continue" promises resumption. → Disable the control at the stopped state and point at the reset ("Pull it back and release"), with one honest clause on the reset path: *"Fresh run — the room keeps the energy from the last one."* *Code + Mide sign-off; small.*
- **P1-15** · `heating-and-thermal-equilibrium` · flow bench pair 2 — the note says *"the water barely warms"* while the water goes **12 °C → 38 °C** in large type directly above it; the bench's implied capacity ratio is 2:1 where a real hot spoon in a beaker gives ~1 degree. → Give each pair a capacity weighting (spoon 1 : water 60 lands at ~13 °C) and use the weighted mean; or, minimally, change the numbers so the printed claim is true. *Code + Mide sign-off (temperatures); small.*
- **P1-16** · `heating-and-thermal-equilibrium` · flow bench pair 1 — "Ice" runs from −4 °C to **5 °C and is still labelled Ice**, climbing smoothly through 0 °C with no melt, in a lesson that `assumes: solids-liquids-and-gases`. → Rename the cold body so the label stays true and add one clause: *"The ice reaches 0 °C, melts, and the meltwater goes on warming with the drink — which is why the drink ends up colder than a simple average suggests."* *Code + Mide sign-off; small.*
- **P1-24** · `simple-machines` · think-again — *"the last column is always slightly the larger"* names **Energy out**, i.e. it states that output exceeds input on the page arguing the opposite; it contradicts its own next sentence, rung 3, and the bench's own closing paragraph. → Two words: *"the **input column** is always slightly the larger"*. While there, "every row has the same number in the last two columns" should read "nearly the same". *Code; small.*
- **P1-25** · `simple-machines` · lever table — the lesson drills E = F × d and then prints a table whose rows fail it: 600 N × 0.050 m printed as 30.6 J; 5400 N × 0.006 m printed as 30.4 J against 32.4 J. Two causes: the friction bias is applied to the **energy** and not to the force it should come from, and the distance is rounded to three decimals so the product cannot close. The live readout shows 30.0/30.0 for the same fulcrum the table records as 30.6/30.0, unlabelled. → Apply the bias to the **force** (`F_measured = F_ideal × (1 + bias)`, column 3 = F_measured × d) so each row multiplies out exactly and the friction story is told by a bigger push; print distance to 4 s.f. or switch to centimetres; label the live readout "ideal — press Record to measure it". *Code + Mide sign-off; medium.*

**S2**
- **P1-2** · `energy-stores` — "Check the ledger" reveals the full verdict on **any** press including with nothing ticked, so all five scenarios are answerable in five clicks. → Gate the prose verdict on at least one tick in each column; the chip-level marking can keep firing. *Code; small.*
- **P1-6** · `energy-transfers-before-and-after` · tally gate — committing to *"Used up making the bulb work"* (`ENER-11` itself) closes the gate, opens the bench, advances the counter and produces **no feedback of any kind**; the misconception register claims this block confronts it. Told neither *why* nor *that*. → Emit a one-line reveal on commit: *"The other 57 J fill a thermal store in the bulb and the room. Nothing is used up."* This is not a right-answer feedback line — it is the missing statement of the answer that every other hook gives. *Code; small.*
- **P1-7** · `energy-transfers-before-and-after` · tally counter — "tallied" means merely *selected*: four clicks with the slider untouched reads "all four tallied" and ticks the rail stop, so the lesson's actual work is optional and never asked for. → Count a device tallied only once its slider has moved; add the target to the prompt ("hunt for the real figure"). *Code; small.*
- **P1-10** · `conservation-of-energy` — **the unit's flagship instrument has no picture of a pendulum**: three bars, a line, four readouts, no canvas/SVG/img, while the prose refers to "the bob", "twice a swing" and "the pivot". → **Design brief**: a small pendulum beside the bar stack sharing its state — pivot, string, bob, arc, and the release height marked with a faint rule so the falling return height (the lesson's own big question) is visible. Static three-panel fallback if animation is too costly. *Design brief → Code; medium.*
- **P1-11** · `conservation-of-energy` · rung 1 feedback — *"The first half is often true"* concedes *"turned into heat"*, the exact phrasing the unit has spent three lessons demolishing, at the moment of correction. → *"Two things wrong. It is not turned into anything — it is transferred; and there is no store called heat."* Same length, teaches twice. *Code; small.*
- **P1-20** · `conduction` / `radiation` — "convection" is used as the explanatory contrast three times (including the **first sentence of radiation's big question**) before it is ever defined; the only gloss is buried in radiation's think-again. Checked: convection is correctly **not** in the KS3 programme of study, so this is a gloss, not a coverage gap. → Nine words at first use on `conduction`: *"…different from **convection** — energy carried along by a liquid or gas that physically moves, which is why it cannot happen inside a solid."* *Code; small.*
- **P1-22** · `radiation` · key note — *"Only the high-energy end… can do harm"* is false (infrared burns, intense visible light damages the retina), and the same page's bench close says it correctly three blocks earlier. The key note is the sentence copied into a book. → Bring the note into line with the close it summarises: only the ionising end carries enough energy in a single wave to break molecules; *"The rest can still warm you, and enough of anything will burn."* *Code + **Mide sign-off** (risk wording); small.*
- **P1-23** · `insulation` · results table at 390px — 774px inside a 314px wrapper; the fourth column, **"What it blocks"** — the only place the lesson says *why* foil and wool differ — is entirely off-screen with no scroll affordance. → Below ~600px stack each row as a card; or lift "What it blocks" out of the table into a four-line legend (it is static text and does not need to be a column), which fits the rest into 390px and is probably better on desktop too. *Code, layout past Design; small.*

**S4**
- **P1-3** · `energy-stores` hook — correct option 12 words against 6/8/7, and the source comment claims the opposite ("distractors at the answer's own length"). → Lengthen the three distractors without making them more plausible. → SYS-8. *Code; small.*
- **P1-4** · `energy-stores` and the whole unit — **"joule" is used from lesson 1 and first explained in lesson 8.** The definition is authored in `vocabulary` and never renders (→ SYS-V). → One clause in L1: *"energy is measured in **joules (J)**; a joule is about the energy it takes to lift an apple a metre."* *Code; small.*
- **P1-8** · waste sort and conduction's touch test — both answer keys alternate perfectly by position (`0,1,0,1`), so two items give away the other two. → SYS-8 form 4. Reorder the authored items (waste → W/W/P/P; touch → C/C/N/N, which also groups the conductors and reads better), or shuffle bench items at build time as MRB-278 does for rungs. *Code; small.*
- **P1-12** · `conservation-of-energy` — the resting note says *"Press start"*; there is no Start button (the control reads "Release it"). → Name the button. *Code; small.*
- **P1-17** · `heating-and-thermal-equilibrium` — the scale note renders the literal string **"10^9"** to students; a Year 8 reads "ten, hat, nine", and the page can render superscripts (it prints ½mv² correctly). → "about a **billion** times". *Code; small.*
- **P1-18** · `heating-and-thermal-equilibrium` — the axes are hard-wired, so **four of the nine reachable states are physically impossible** (a 300 g mug and a 100 kg bath at 1500 °C) and the bench reports numbers for them with a straight face. → Give each amount its own three temperatures (spark 400/900/1500; mug 20/40/95; bath 20/40/60) so every reachable state is real. *Code + Mide sign-off; small.*
- **P1-19** · `heating-and-thermal-equilibrium` · flow pair 3 — both blocks read 30 °C to show neither is hotter, and the drawing paints one with the *hot* treatment and one with the *cold*; the ghost arrow "no cold travels this way" is still drawn where nothing travels either way. → Paint both neutral when the temperatures are equal (the wiring already knows — it hides the real arrow), hide the ghost, and print "no flow either way". *Code; small.*
- **P1-21** · `conduction` · model footnote — *"the ORDER and the rough ratios are right"*: glass is 17× copper on the bench against a real ~400×, undercutting the page's own "metals conduct roughly a thousand times better than wood". The footnote is otherwise exemplary. → Delete four words: *"The ORDER is right; the exact seconds are chosen so a lesson can watch them."* *Code; small.*

---

### P2 · Energy at home · 5 lessons · **32 findings** (S1 7 · S2 10 · S3 7 · S4 8)
*In §4: P2-22 → SYS-B · P2-34 → SYS-2 · P2-35 → SYS-3.*

**S1**
- **P2-09** · `power-ratings-in-watts` · hook, bench, rungs 2 and 3, big question — the flagship comparison draws a **15 W phone charger at a constant 15 W for eight hours** (432 kJ) and credits it as beating the kettle. A charger draws near its rating for one to two hours and then trickles; a plugged-in idle supply is legally limited to a fraction of a watt; 15 W for 8 h would deliver seven phone batteries. Realistically the charger transfers ~90 kJ and **the kettle wins** — so the answer the lesson credits is wrong for the appliance it names, and the page refutes itself two blocks later ("Standby is a low power, not no power"). → **Swap the appliance, not the physics**: a home router is rated in the same range, genuinely draws its rating all night, and every student has one. Every number in the hook, bench, crossover, rung 2 and rung 3 survives untouched. Apply at all five sites plus the bench label. *Code + Mide sign-off; small.*
- **P2-19** · `calculating-energy-transferred` · bench payoff (also rung 4 and `p2-04`'s bill builder) — *"The fridge… is the biggest consumer of the five, because it never switches off"* depends on modelling a fridge at 90 W for 24 h = 2.16 kWh/day. Real fridge-freezers cycle: 0.4–1.2 kWh/day, behind the oven (1.65) and the shower (1.42). **The closing insight is false, in the direction that teaches the misconception the previous lesson spent itself killing** — and the renderer *enforces* the fiction (`r_appliance_bench` raises unless a lower-rated appliance outranks a higher-rated one). → Keep the inversion, scope the claim: *"…gets through more energy in a day than the kettle does, because it keeps coming back on all day and night."* True at any realistic figure. Better: model a ~45 W average with a one-line duty-cycle note, updating rung 4 and the bill row in step. *Code + Mide sign-off; small / medium.*
- **P2-24** · `reading-a-fuel-bill` · CFIFA example 2 — *"A 900 W fridge compressor"* against the same page's own bill row of **90 W** and `p2-03`'s 90 W; 900 W is a commercial chiller, and 3.6 kWh/day is three to nine times a real fridge-freezer's whole consumption. The Answer note compounds it ("3600 units a day — more than a house uses in a year", against this page's own 412/month = 4,944/year). → **"A 120 W fridge compressor runs for 4.0 hours a day"** → 0.48 kWh, a real figure, still needs the ÷1000 step, and the note then reads "480 units a day — more than the whole house uses in a month", which is true against the page's own 412. *Code + Mide sign-off; small.*
- **P2-02** · `energy-in-food` · think-again — attributing the calorimeter/label gap to what the body *"cannot get at"* is wrong and points the wrong way: the classroom measures combustion, and UK label energies use Atwater factors so digestive losses make the **label** lower, not higher. The page teaches the correct one-directional heat-loss account two blocks later. → End the sentence at the true part: *"…which is why the number on the label is what a body can actually use rather than what a fire could release."* *Code + Mide sign-off; small.*
- **P2-15** · `calculating-energy-transferred` — *"6000 J is roughly the energy in a mouthful of bread"*: bread is ~10–11 kJ/g, so 6000 J is **half a gram**, out by ~30×, in the sentence teaching students to sanity-check magnitudes, and checkable against this unit's own previous lesson. → Use an anchor the unit already owns: *"about what it takes to carry yourself up two flights of stairs"* (60 kg × 10 m ≈ 5900 J). *Code + Mide sign-off; small.*
- **P2-16** · `calculating-energy-transferred` — *"A kettle boiling a mugful needs about 360 000 J"*: a 250 ml mug needs ~89–110 kJ; 360 kJ boils **a litre**, which is what the same page says two sentences earlier and what its own worked example computes. → One word: *"boiling a full litre"*. *Code + Mide's nod; small.*
- **P2-31** · `fuels-and-energy-resources` · think-again — *"considerably worse than a small diesel on a coal-heavy grid"* is not supported: lifecycle analyses put battery-electric below comparable petrol even on coal-heavy grids and roughly level with the most efficient small diesels. It is also the fastest-moving number in the topic and is undated. → *"…and barely better than a petrol one on a coal-heavy grid."* Keeps the whole force of the pathway argument and survives decarbonisation longer. *Code + Mide sign-off; small.*

**S2**
- **P2-01** · `energy-in-food` — the stretch says the calorimeter reads "20 to 60 per cent below the label"; the instrument on the same page produces 57–73% below, the lesson's own rung 3 is 62.5% below, and the drawer's docstring states the design intent as 54–70% below. A student who does exactly what the page asks is told their honest result is abnormal. → *"…usually it recovers only a third to a half of the label figure."* True of the bench, the rung and the practical. *Code + Mide's nod; small.*
- **P2-07** · `energy-in-food` — **no safety wording anywhere in the unit**, on a lesson modelling a naked flame, hot glass and a **peanut** ("the classic school sample"); `safety_note` appears nowhere in `ks3_data/p2/`, while the mechanism exists and is used elsewhere in physics. **Flagged, not drafted.** → §6, Mide's gate alone. *Mide sign-off; small once ruled.*
- **P2-10** · `power-ratings-in-watts` — the set-top-box reversal ("70 kWh against 60 kWh") rests on a kettle at 30 hours a year, i.e. five minutes a day; UK kettle use is 120–170 kWh/yr, at which the reversal is simply false. The box is a good choice; the kettle figure was chosen lowest. → Keep the surprise against something that survives it, or tell the truth about the ranking: *"70 kWh, not far off what the kettle itself gets through — from a box you thought was off."* *Code + Mide's nod; small.*
- **P2-12** · both sorters — a **wrong** and a **right** selection render identically (same amber pill, same class, same `aria-pressed`), and on `p2-05` the rail stop completes with **all eight resources sorted wrongly**. The ladder on the same page distinguishes properly, so the inconsistency is within one page. Amber is also the warning/loss token being used to mean "you picked this". → Both sorters already carry the truth and authored right/wrong strings: add `is-correct`/`is-wrong` using the ladder's two tokens; and either count only correct sorts toward the stop or rename the demand honestly. *Code; small.*
- **P2-13** · rung 2 feedback — *"2000 × 180 = 360 kJ; 15 × 28 800 = 432 kJ"*: both equations are false as printed (the kilo is applied silently after the multiplication) — the exact habit this unit's CFIFA method exists to eliminate. → *"2000 W × 180 s = 360 000 J; 15 W × 28 800 s = 432 000 J."* *Code; small.*
- **P2-20** · money on eight surfaces across two lessons — 27p/kWh and 53p/day, never dated. The drawer's own docstring says *"it will date"*; the constants are isolated, and the **page** is what never says so. → Date them once per lesson: *"At 27p per kWh (2026)"*; and one clause in the hook — *"the price in 2026; yours will be different, and the arithmetic will not be"* — which converts a liability into the lesson's own point. *Code; prices are Mide's (money); small.*
- **P2-26** · `reading-a-fuel-bill` — **gas is absent entirely** (the larger bill in most UK homes, and its m³ → kWh calorific conversion is squarely physics), and **VAT is absent** (5% on every real bill, so the modelled total is not the amount due) on a lesson otherwise scrupulous about the parts of a bill that are not units × price. → VAT is one clause. Gas is a product decision: retitle to "Reading an electricity bill", or add a "Going further" on the gas meter — which would be a strong stretch for this audience and would close the statutory bullet properly. → §6. *Mide ruling then Code; small / medium.*
- **P2-29** · `fuels-and-energy-resources` grid — the vertical axis is labelled at both ends on every view; **the horizontal axis carries one centred question and no label on either side**, so nothing says left means finite and right means renewable — while the lede promises exactly that label. → Two text nodes: `FINITE` and `RENEWABLE` under the two columns. *Code; small.*
- **P2-32** · `fuels-and-energy-resources` — the stretch names **geothermal** as one of "three things on the list" and geothermal is not on the list; **oil** is also absent, though the stretch discusses it and it is the fossil fuel a child knows best. → Add oil and geothermal to the sorter and grid (geothermal is the closest thing to a counterexample to "no resource wins on every axis" and is worth confronting); or add geothermal alone and change *"on the list"* to *"in the world"*. *Code + Mide sign-off; medium.*
- **P2-36** · all five hooks and three of four gates — **the correct option is B in all five hooks** and in three of the four instrument gates: eight of nine pre-instrument commits answered by pressing B, on the widgets whose whole purpose is a genuine commitment. The contrast is the finding: the **ladders** were deliberately shuffled and the reasoning is written down in the source; the same author applied it to everything the gate watches and to nothing it does not. Length tells measured **absent** here. → SYS-8. *Code; small / medium.*

**S3**
- **P2-03** · calorimeter — "Record this run" can be pressed repeatedly on one burn, so three byte-identical rows satisfy `three_runs_recorded`, tick the rail and reveal a closing panel that reasons about *scatter versus systematic error* over a dataset with no scatter. → Make Record consume the run (the same latch the burn button already uses); optionally require the three runs to be distinguishable. *Code; small.*
- **P2-04** · calorimeter alt text — describes *"a thermometer in the water"*; **the drawing contains no thermometer**, and no flame. A screen-reader user is told about a component that is not there, and the apparatus diagram omits the one component the reading comes from. → Code: correct the alt now. **Design brief:** add the thermometer (bulb in the water, stem out of the tube) and a visible flame; a draught shield would let the drawing carry the lesson's own error analysis. *Code + Design brief; small / medium.*
- **P2-11** · power bench — the button *"Jump to the crossover"* lands on the one state where the caption says *"**Past** the crossover… has now transferred **more** energy"* over two totals printed **equal**. → Split the branch at equality: *"The crossover. The 15 W charger has now transferred exactly as much energy as the 2000 W kettle did all day."* Two lines, and it turns the button's destination into the lesson's best moment. → SYS-5. *Code; small.*
- **P2-17** · appliance bench — kWh is rendered with `toFixed(2)`, so with the **LED lamp** selected every slider position below 34 minutes prints `0.00 kWh` beside `10,800 J`, under a caption reading *"The two readouts are the same energy in both legal unit pairings."* → Render to significant figures below 0.01 (`0.0030 kWh`), which is also the honest teaching moment for why bills are in kWh. *Code; small.*
- **P2-18** · appliance bench — an appliance counts as "priced" **only** by pressing a preset chip, so the obvious route (select an appliance, move the slider) records nothing; and `appliances_to_price: 3` means the **Oven and Fridge** chips are never rendered, so the two appliances the closing panel is *about* are the two the instrument never sends the student to. Their authored preset labels sit unused in the data. → Mark priced on selection + slider movement, and raise the count to 5 so the authored chips render. *Code; small.*
- **P2-23** · bill builder — the amount due is computed from the unrounded total while every row is printed rounded, so **10 of 25 driven slider settings disagree by 1p**, including the default (£77.36 printed, £77.35 due), on the lesson whose claim is "the amount due is every row added" and whose figure is a balance beam. → Sum the rounded rows — which is also how a real itemised bill works. *Code; small.*
- **P2-28** · fuels grid — on the **default** axis Wind, Solar, Hydro and Tidal plot within four pixels at one x, so four of eight labels render as one unreadable smudge, in the region the caption reasons about. Guaranteed, not accidental: all four are correctly near zero. → De-collide in `r_two_axis_grid` (stack labels beside a shared marker cluster, or nudge with leader lines); or bucket the axis into named bands, which is honest about the tie. *Code, Design sees the layout; medium.*

**S4**
- **P2-05** · rung 3 poses the explain task on 9 and 24 kJ/g while the instrument the student just drove gives 10.6 and 24.5. → Reword the rung to use their own run — it becomes the stronger question. *Code; small.*
- **P2-06** · the hook's crisp packet (958 kJ / 50 g = 19.2 kJ/g) disagrees 14% with the worked example's 22.0 kJ/g, on the one lesson that trains students to divide energy by mass. → Move the hook's number (263 kcal, 1100 kJ); the bench's 22.0 is the accurate one. *Code; small.*
- **P2-08** · *"Weigh the room's air and you would find the energy has not left the building"* — weighing does not detect thermal energy, and the instrument the paragraph wants is a thermometer. → One noun. *Code; small.*
- **P2-14** · *"your own body sustains around 100 W of useful output"* — 100 W is total metabolic power, almost all of it heat. → *"runs at around 100 W all day — about an old filament bulb — and nearly all of that leaves you as heat; in a sprint you can put out near 1000 W of actual work."* The factor-of-twenty comparison survives. *Code + Mide's nod; small.*
- **P2-21** · the appliance bench's JS-composed note uses straight ASCII quotes where every other quotation mark in the unit is typographic. → Curly pair in the JS string. *Code; small.*
- **P2-25** · the anchor household is 412 units/month (≈2× Ofgem typical) while the bill builder at its own defaults produces **227.6** — the instrument is well calibrated and the headline is the outlier. → Either bring the hook to 228, or keep 412 and say what it is: *"A typical home uses around 230 units a month. The bill at the top of this page is 412 — an all-electric house with an electric shower."* *Code; small.*
- **P2-27** · the bill-builder gate asks for the largest single **item** and three of four options are groups; the credited answer assumes an electric shower, which fewer than half of UK homes have. → Scope it to the household the student is about to build: *"In this house, which of these do you think will cost the most?"* *Code; small.*
- **P2-33** · the hydro note claims it *"takes more land than anything else on the grid"* — true per installation, false per unit of energy against biomass, which is on the same grid and plotted adjacent. → *"…more land in one place than anything else here."* *Code; small.*

---

### P3 · Describing motion · 3 lessons · **24 findings** (S1 9 · S2 4 · S3 5 · S4 6)
*In §4: P3-7 → SYS-V. (P3 filed no SYS-2/SYS-3 finding; both were recorded present in its probes.)*

P3's **writing** is the strongest in the estate: the flat-line question — the
single sentence most often taught wrong in British KS3 physics — is answered
correctly, committed to and defended in four separate places; average-versus-
instantaneous is handled better than most GCSE textbooks; and there is no absolute
rest anywhere in lesson 3. **All nine S1s are in the instruments and the captions,
not the teaching.** Three benches each contradict, in code or in a fixed string,
the exact sentence beside them. None needs new content and only one is larger than
small.

**S1**
- **P3-11** · `distance-time-graphs` · journey matcher — **the target line and the student's line are drawn on two different vertical scales, on the same axes, at the same time.** `draw()` recomputes `dmax` from the union; `paint()` always redraws the target at `dmax = 12`. Four jogs (36 m) puts the student's 9 m segment at exactly the height of the target's 3 m segment — a walk and a jog identical on screen — with the target's 12 m peak drawn *above* the student's 27 m point. Directly beneath rung 2 ("Line A is steeper than line B → A is travelling faster"), the instrument shows the steeper line as the slower one. Reachable in two taps. → Hoist one `dmax` out of `draw()` for both polylines, or better **pin the scale to a fixed 0–36 m** — the four modes over four blocks cannot exceed 36, so a fixed axis is possible and is the right teaching choice: a graph whose scale moves is the wrong thing to show a class learning to read steepness. *Code; small.*
- **P3-12** · journey matcher — "Walk back · 2 m/s" from 0 m is clamped away, so four walk-backs draw **a flat line along the bottom** and report **"0.0 m from the start"**, byte-identical to standing still — on the page whose key fact is *"A flat line is not slow. It is stopped."* Nothing says the move was refused. → Refuse the move visibly (*"You are already at the start"*) and never print "0.0 m" for a block that moved; or drop the clamp and let the line fall below the axis, which needs a signed axis. *Code; small.*
- **P3-9** · graph plotter — **the joined line does not pass through the plotted points.** The dots are cell-centre buttons at `(i + 0.5)/n`; the polyline maps `value/max × 100`, half a cell out in each direction. The first vertex is drawn *outside the grid frame*; on a 644 × 429 graph the endpoint misses by ~48 × 32 px; and the flat run — the lesson's key fact — is the part most visibly out of register. → Map the polyline through the same cell-centre formula, or give the grid a half-cell padding (which fixes P3-10 in the same pass). Add a render assertion that each vertex falls inside its own plotted cell. *Code; small.*
- **P3-10** · graph plotter — **the graph has no scale.** Two axis titles with units and **not a single number, tick or origin marker**. Read-back q3 asks for the speed over the last four seconds; rung 3's fifth criterion is *"Reads at least one time or distance off the axes"*, which the page's own axes make impossible; "which part was fastest?" can only be answered by eye — the habit the unit exists to break. The scale *does* exist in the grid's `aria-label`, so a screen-reader user is told it and a sighted user is not. → Render the authored `t_values` and `d_values` as two flex strips aligned to cell centres; both arrays already reach the renderer and are used only for button counts. *Code, layout past Design; small.*
- **P3-1** · `speed` · light gates — the instrument lets the student change gate separation and ramp between runs (the table has columns for both) and the fixed closing panel says *"the same distance every time… the mean of the three times is what you divide into"*. It **prescribes a method** that is invalid for the readings just taken, and the rail ticks on any three runs. → Either lock the setup after the first run (what a real repeat-readings protocol does), or compose the closing sentence from the recorded rows: same distance and ramp → the current sentence; otherwise *"You changed the setup between runs, so these three times are not repeats of one measurement."* Option two turns the defect into the lesson's own point about fair repeats. *Code, new branch wording past Mide; small.*
- **P3-18** · `relative-motion` · frames bench closing panel — *"One of the four readings is always zero"*, asserted at the moment the rail ticks and the lesson is meant to land. At the shipped defaults the four readings are **25.0, 20.0, 5.0, 5.0** in all three viewpoints; no reading is zero. The opening prompt makes the mirror-image error (*"Only the numbers do"* change — the numbers are precisely what does not). → Add the missing tile and the sentence becomes true: render a fifth readout for the observer's own frame ("A from car A · 0.0 m/s"). Otherwise rewrite both strings to what the instrument does. **A visible zero is the thing the lesson is about**, so the tile is the better fix. *Code; wording past Design and Mide; small.*
- **P3-19** · `relative-motion` · the scene — **neither car ever moves, in any viewpoint.** Both are at fixed `left:` percentages; the only motion is the road's dash pattern, which animates only in a car seat and always at a fixed 1.1 s regardless of speed. From the roadside — the default — *"From the roadside both cars are moving"* is printed over a completely static picture. This is the "correct behaviour, wrong model" case exactly: every number is right, and what a child walks away with is that changing viewpoint changes which number is in a box. → Animate the cars from the relative velocities already computed (per-frame drift of `v − v_observer`, wrapping at the scene edges) and drive the road's duration from `|v_observer|`, stopping at zero (which also fixes P3-24). The observer's own car then visibly holds still while everything else moves past it — the sentence the closing panel is trying to write. *Code, motion feel past Design; medium.*
- **P3-20** · `relative-motion` · passes block — the heading states an unqualified rule, *"Same way, subtract. Opposite ways, add."*, repeated in the key note and the vocabulary card. **Pass 4 asks a different question** — composition through a moving frame (walking forward on a train) — where the answer is an **addition**: 30 + 1.5 = 31.5. The heading's rule gives 28.5, which is listed as option A, and the `why` explains the right answer without ever mentioning that the rule six inches above does not cover this case. Rung 4 has the same shape. → Scope the rule to the question it answers (*"How fast does one pass the other? Same way, subtract…"*) and let Pass 4 teach the scope: *"This one is not a pass — you are inside one of the moving things."* Turns the lesson's strongest defect into its best item. *Code + Mide sign-off; small.*
- **P3-21** · `relative-motion` · Pass 3 — *"25 − 20 = 5 m/s. **Walking pace.**"* 5 m/s is a 3:20/km run. The unit's own previous lesson sets the scale: "Walk · 1 m/s", "Jog · 3 m/s". This is the one place P3 asks a student to *feel* a number. → *"**A jog.**"* (or "a bit faster than a jog"). *Code + Mide sign-off; small.*

**S2**
- **P3-3** · `speed` — `s = d ÷ t` is **never rearranged with a worked route**; the triangle is the only route offered, and two of its three faces are taught in a tooltip and then never used — every calculation in the lesson finds `s`. A student handed a distance and a speed at GCSE has met the move zero times. → One extra staged worked example or one retargeted rung using a different face, plus one sentence under the triangle: *"the triangle is a reminder, not a reason — `d = s × t` is what `s = d ÷ t` says, read the other way round."* *Code; new numbers past Mide; medium.*
- **P3-4** · `speed` hook — correct option 48 chars / 10 words against 35/19/33, and the only one with two clauses; it is the commitment that elicits `FORCE-02`, so the tell weakens the confrontation it exists to set up. → Even the weights, as `lesson_03` already did for its apply rung. → SYS-8. *Code; small.*
- **P3-16** · graph plotter at 390px — the 49 cells measure **45 × 30 px**, below the 44 px minimum on the short axis, on the one instrument requiring a precise tap, and with no axis numbers to aim by (P3-10). Two scripted taps landed one cell off. → Taller aspect ratio at narrow widths (7×7 at 44 px is 308 px tall, no worse than the current height), or fewer, larger rows on phones. Land with P3-10, which makes an off-by-one tap self-correcting. *Code, sizing past Design; small.*
- **P3-22** · `relative-motion` think-again — *"takes ten seconds to slide past… 200 km/h between them instead of 5"*: at 5 km/h relative, a 200 m train takes about two and a half **minutes**; ten seconds covers under 14 m. The slip argues against the paragraph's own point (that the overtake feels endless). → *"takes most of a minute"*, or keep ten seconds and raise the relative speed to a realistic overtake. *Code + Mide sign-off; small.*

**S3**
- **P3-2** · light-gate track `aria-label` is a fixed string reading *"1.20 metres apart"* while the visible readout says 2.00 m — the one measurement the lesson is built on, wrong, for exactly the students who cannot see the readout. → Repaint the label in `paint()` from the authored template. **Worth a general rule: an instrument's `role="img"` name is state, not decoration.** *Code; small.*
- **P3-13** · journey matcher — the rail stop's authored condition is `target_matched` and the wiring credits it on `sent`, so four "Stand still" blocks tick it. The only comparison offered is end-point equality, which several unrelated journeys satisfy. → Keep the ruled no-marking design and make the verdict *describe the shape* ("…they differ between 3 s and 9 s: yours is climbing there and the target is flat"), then rename `done_when` to `journey_sent` so the key stops claiming a match. *Code; small / medium.*
- **P3-15** · graph plotter — **no feedback of any kind for a non-visual user**: no `aria-pressed` on plotted cells, no `aria-live` on the "Looking for:" line, no live region in the block. A screen-reader student can tab all 49 buttons and never learn which point is wanted, whether a press was accepted, or that it was wrong — the keyboard access Design deliberately preserved is unusable because the feedback half was not built. → Two attributes: `aria-live="polite"` on the seek line (which already carries the right sentence) and `aria-pressed` on every cell. Check the same pattern on the estate's other button-grid instruments. *Code; small.*
- **P3-23** · frames direction toggle — the visible label **is** the state and `aria-pressed` is the same state, so they cancel: a screen reader announces "Opposite ways, not pressed" at the moment the cars are going opposite ways. → Fixed name + `aria-pressed`, or a two-button segmented control like every other choice in the unit. *Code; small.*
- **P3-24** · frames status line at zero speed — *"the road is sliding underneath it"* printed while `data-slide` is `0` and nothing moves. → Branch on the observer's own ground speed. (P3-19's fix makes this branch fall out naturally.) → SYS-5. *Code; small.*

**S4**
- **P3-5** · the fly crosses the view "in half a second" in the hook and "1.5 m in **0.8 s**" in the compare pair *explicitly labelled "the one from the top of the page"* — changing one of the two measurements between question and answer, on the page arguing you cannot compare until you have both. → Make them one number (0.5 s → 3.0 m/s, and "over eighty times faster" replaces "over a hundred"). *Code, flag Design (hook copy); small.*
- **P3-6** · the opening example calls 8.33 m/s "far faster" than 5.83 m/s (43%), two blocks before the same page uses "far" for 130×. → Soften the adjective, or use a club-level marathon time (3.33 m/s) so it earns it — the second is stronger teaching. *Code + Mide sign-off; small.*
- **P3-8** · the speed camera measures "a few metres" in one block and "about half a metre" four screens later — a factor of six, on the one quantity the argument turns on. → Pick "half a metre" and use it twice; the contrast with the average-speed camera's two kilometres then becomes a factor of four thousand, which is the point. *Code; small.*
- **P3-14** · the wrong-tap message renders as *"Looking for: you chose 8 s, 12 m · still looking for 0 s, 0 m"* — not a sentence, at the only moment the instrument speaks to a student who has just made a mistake. → Compose the whole line in one place. *Code; small.*
- **P3-25** · the car-viewpoint status line is a tautology (*"From car A, car A is parked"*) and says nothing about the only interesting thing on screen. → *"From car A you are not moving. The road is sliding backwards past you at 25 m/s, and car B is drifting backwards at 5 m/s."* That sentence is the lesson, and needs no new data. *Code, wording past Design; small.*
- **P3-26** · the unit's ruled position is that **"velocity" appears nowhere**, and the body copy honours it — but the word appears once on **every** lesson page, in the end-matter GCSE card, undefined. → Gloss it once, or write the cards in the unit's own register ("Speed with a direction attached…"). The second is more consistent with the ruling. → §6. *Code; Mide ruling on which; small.*

---

### P4 · Forces · 9 lessons · **26 findings** (S1 4 · S2 8 · S3 5 · S4 9)
*In §4: P4-07 → SYS-V. P4's SYS-3 probe was **struck** (box test); the defect is present on all nine pages.*

**S1**
- **P4-04** · `balanced-and-unbalanced`, `air-and-water-resistance`, `moments` · **every bench force arrow below ~9 N** — two defects in one drawing, on the unit whose stated doctrine is that an arrow's length **is** the size of the force. **(a)** The shared `arrowV`/`arrowH` primitives use a **fixed 26px head**, so any force whose scaled length is under the head renders as a glyph exactly `head` px long whatever its size: measured on the support rig at 0.5 kg on paper, **weight 5 N, upward 2 N and resultant 3 N are three identical 26px arrows** — while the SVG's own `aria-label` asserts *"drawn to the same scale"*. On the fall bench at 25% the resistance and resultant arrows total 148 px against a 130 px weight arrow, so **the three arrows visibly fail to add up**, on a bench headed "Watch the two arrows close the gap". **(b)** On the support rig the weight and upward arrows are drawn at x = 760 and x = 240 while the load spans 430–570 — **both float clear of the object, on opposite sides of it** — two lessons after the unit teaches *"it starts on the object being pushed or pulled"* and marks equal-length arrows for unequal forces wrong in its own think-again. → (a) In `arrowV`/`arrowH`, scale the head down with the arrow when `len < head` so a 2 N arrow is a 6 px stub; **26 call sites across the key stage use these two functions, so re-measure every unit's benches after the change.** (b) Move the rig's two arrows onto the load as free-body convention requires. *Code (a); **Design brief** (b); Mide sign-off on the redrawn free-body diagram; medium.*
- **P4-01** · `friction` · rule 1 — *"Always the opposite way to **the movement**… **Friction never pushes something along.**"* The referent is silently swapped from the *sliding between the surfaces* to the *movement of the object*, and then stated as an absolute. It is false for the two cases every child needs: walking and every driving wheel. **The page contradicts itself inside the same block** — four items below, *"the same force that wears out a brake pad is the force that lets you walk"* — and the key fact and vocabulary get it right. As installed, this is the belief that makes "how do you walk?" unanswerable at GCSE, in the numbered rule a student revises from. **Second site:** `questions_05_friction.py` repeats it verbatim as a distractor rationale — authored, not yet served, **so it must be fixed before that pool is populated**. → Restore the referent and make walking the teaching: *"Always the opposite way to the sliding between the two surfaces… That is not always the opposite way to the object: when you walk, your shoe pushes backwards on the ground, so friction pushes your shoe forwards. It is what you walk on."* *Code + Mide sign-off; small.*
- **P4-02** · `springs-and-hookes-law` · YOUR TURN past the limit — the model lines a student self-marks against apply proportionality **at the loads where the lesson has just proved it fails**: at 8 N the FORMULA line prints its own caveat ("true while the spring is on the straight line") and the next three lines ignore it, giving 23 mm/N and a 368 mm prediction against the bench's own 440 mm. The only feedback frames the failure as the apparatus's **range** ("the bench only goes to 10 N"), not as the proportionality giving out — so the wrong reasoning is left standing and endorsed. The lesson registers `FORCE-41` as confronted **by this instrument**. → Branch the five lines on `load > LIMIT` and make them the honest ones ("this reading is at 8 N, past this spring's limit of proportionality of 6 N… no prediction can be made from this reading"); or refuse the panel above the limit exactly as the sledge bench already refuses at 0 N — that pattern is already in the engine. *Code + Mide sign-off; medium.*
- **P4-03** · `springs-and-hookes-law` · spring bench — the bench announces permanent deformation (*"taking the load off will not bring it back… reads wrongly at every load afterwards"*) and then, on the next drag, **denies it**: back at 2 N it reads 40 mm, "On the straight line"; at 0 N, 0 mm. `ext(L)` is a pure function of the current load with no memory. It demonstrates on screen the exact belief the lesson registers as `FORCE-43`, and the way back is one drag a child will certainly make after reaching the most dramatic state on the bench. → Track `maxSeen` and carry the permanent set into every later reading and into the zero, so unloading leaves the spring visibly longer; add a "Fit a new spring" control beside "Clear the readings"; distinguish pre- and post-overload points on the graph. Minimum honest fix: freeze the bench once ruined and say so. *Code + Mide sign-off; medium.*

**S2**
- **P4-08** · all nine lessons · two position tells in corpora no gate watches — hooks answer **B on seven of nine and C on the other two, never A or D**; bench gates skew A×3 B×3 C×1 **D×0**; and the ladder passes MRB-278 on the pooled count while **the recall answer is A or C on all nine lessons and the apply answer B or D on all nine** — trivially learnable in three lessons. (Length tells measured absent across all 120 ungated predicts: position is the whole of it.) → SYS-8, including the per-rung gate scope. *Code; small / medium.*
- **P4-11** · five of six arrow benches label their arrows with a **magnitude only** — the drag lane shows "66 N" and "66 N" with nothing saying which is the pull and which the friction. The names exist in the tiles below and in the aria-labels, **so the screen-reader description of these diagrams is better than the diagram**. Naming each arrow is a marked step in every GCSE free-body question, and this is the unit where the habit is formed. → **Design brief:** a short caption under each arrow using the tile wording that already exists (drag lane "your pull"/"friction"; rig "weight"/"push of the support"/"resultant"; …). The interaction board's `cap_a`/`cap_b` is the model. *Design brief → Code; medium.*
- **P4-05** · `what-forces-do-to-motion` · trolley bench — *"**This is how an orbit works**"* printed on a state where the reading rises 2.0 → 3.6 m/s. The bench's sideways force is fixed in direction, so it is a projectile; in an orbit the force keeps turning and **the speed does not change at all** — which is exactly what rung 4, two screens below, requires. → Keep the bend, drop the identification, and make the difference the teaching: *"…the trolley is going right and sideways at once, so it ends up faster. An orbit is this move with one change: the pull keeps swinging round to stay side-on, so it never adds any speed, only turn."* *Code + Mide sign-off; small.*
- **P4-06** · `air-and-water-resistance` · fall bench at 125% — the note identifies the state as *"the second after the canopy opens"*; the slider is a share of that object's own steady speed (6 m/s), so 125% is 7.5 m/s, while the real moment is 55 m/s and ~8 g. The page's own think-again describes the violent version. The model is fine; the identification overreaches. → Keep the state, stop it claiming to be the real moment, and say what the real one is. *Code + Mide sign-off; small.*
- **P4-09** · `balanced-and-unbalanced` · the paper support authors a `note_ok` for when the paper holds, and **no student can ever read it**: the mass slider's minimum is 0.5 kg (5 N) against the paper's 2 N cap, so it tears at all ten reachable masses. The unreachable sentence is the richest state on the bench — a support in balance *at its limit* — and it is what Going Further's whole second paragraph is about. → Raise the cap to 10 N so balance exists at 0.5 and 1.0 kg and tearing from 1.5 kg; the note's hard-coded "gives way at about 2 N" becomes `{cap}` in the same edit. *Code + Mide sign-off (the made-up value); small.*
- **P4-10** · `non-contact-forces` — the lesson's opening phenomenon (balloon and hair) and its rung 3 (ruler and paper) are both **charged attracts uncharged**, and the rule the lesson gives ("like charges repel, opposite attract") cannot explain either. P9 teaches induced charge properly, so the estate has the idea; it is missing where it is first needed. → One clause on the "tell it by" card: *"…and a charged object also pulls on things with no charge at all, by tugging their charges slightly out of line. That is what the balloon does to the hair, and the ruler to the paper."* *Code + Mide sign-off; small.*
- **P4-12** · `springs-and-hookes-law` — the distinction the lesson exists to install arrives in its **longest sentence**: 53 words, four clauses, three numbers and a negation, carrying the single most examinable idea. The sentence after it does the right thing in eleven words. → Split into three, one idea each. → SYS-R. *Code; small.*
- **P4-13** · `moments` — **"moment" is never glossed against its everyday meaning**, the clearest such collision in KS3 physics; the unit itself demonstrates it, since the friction lesson two pages earlier writes *"given a moment at rest"*. The lesson is otherwise scrupulous about vocabulary. → One clause where pivot and moment are introduced: *"It is an unlucky name — nothing to do with a moment of time."* *Code; small.*

**S3**
- **P4-14** · three of nine bench counters are frozen at their opening string forever — "0 of 5 cases opened" after all five, "No readings plotted yet" after eleven, **while the graph's own aria-label correctly says "with 5 points plotted"**: the screen-reader user is told the truth and the sighted user is told a lie. Cause: three lessons author `progress` as a finished sentence with no `{n}`, and `setCount` overwrites the live direct write. → Author the three as templates and delete the redundant direct write so there is one writer. **Add a build assertion: a `[data-count]` whose wiring calls `setCount` must carry a `data-format` containing `{n}`.** (Repo sweep: 189 KS3 counters carry `data-format`, 31 lack `{n}`, and these three are the only ones whose wiring also calls `setCount`.) *Code; small.*
- **P4-15** · `what-a-force-is` — the board's verdict paragraph **renders twice on screen** on all five cases, because the aria-live region is styled with the same visible panel treatment the other benches use for their note. → Make `.ks3-iboard-live` screen-reader-only here (a separate selector; the other nine families legitimately share the visible style). *Code; small.*
- **P4-16** · `drawing-and-adding-forces` — at the bench's **default** state the note reads *"The single arrow is 15 N **to the to the** right"*: the template supplies the preposition and the wiring supplies it again. → Fix the template, not `dirWord` — the readout and aria-label consume `dirWord` correctly. *Code; small.*
- **P4-17** · `non-contact-forces` — the sorter's SVG carries `role="img"` and an **empty `aria-label`** on all eight cases, while the block's own lead tells the student *"The diagram marks the gap or the contact for you"*. A screen-reader user is directed to the one piece of information they cannot reach, and the touching/not-touching judgement the bench turns on is carried only in the drawing. → Author the eight `alt` strings in lesson 1's register. **Add a build assertion so a case with no `alt` fails rather than shipping an empty accessible name** — the second time a renderer's silent default has hidden authored teaching. *Code + Mide sign-off (eight sentences); small.*
- **P4-18** · `balanced-and-unbalanced` — the rig's composed accessible name reads *"A 2.0 kilogram load **with resting on** a table top"* on three of four supports. → Drop the literal " with " and author the fourth support's word as a clause. Land with P4-26. *Code; small.*

**S4**
- **P4-19** · the Moon case renders *"Earth and moon"* (lower-cased second name) while every other line on the page capitalises it. → Author a `pair` string per case. *Code; small.*
- **P4-20** · the kicked-ball case gives 300 N over a hundredth of a second = 3 N s, which on a 0.43 kg ball is 7 m/s — a gentle pass, not "leaves a boot at speed" (20–30 m/s needs ~1000 N). The bench's explicit job is teaching students to give a force's size in newtons. → Raise to "about 1 000 N" (≈23 m/s) or soften the prompt to a pass; the number and the phenomenon must agree. *Code + Mide sign-off; small.*
- **P4-21** · the FINE-TUNE justification a student self-marks against is the wrong branch's sentence: *"Kilograms times newtons per kilogram leaves newtons"* printed under `50 − 2 = 48`, and *"Keep the direction of the bigger pull"* under `30 − 30 = 0`. → Branch the note with the formula it belongs to. *Code; small.*
- **P4-22** · at a zero resultant the closing line says *"the arrow on the bench is drawn that length"* while the bench prints "no arrow to draw · 0 N". → A zero branch. *Code; small.*
- **P4-23** · one "still speeding up" note serves 25%, 50% and 75%, naming *"at half speed"* at all three and calling 421.9 N — 56% of the weight — *"how little"*. → Split the branch; the observation is exactly right at 50%. *Code; small.*
- **P4-24** · the "What changed" tile is a per-case constant, so at 1 second it reads *"slower, then reversed"* while the trolley is still moving forwards. → Make it per-duration, as the reading and note already are. *Code; small.*
- **P4-25** · at the longest spanner the success note still offers *"the same 100 N further out"*, sending the student to a control that does not exist. → Branch on whether a longer arm is available, and close the loop with the failure note's own pipe sentence. *Code; small.*
- **P4-26** · three composed aria-labels are ungrammatical at reachable states — *"A 8 kilogram block"*, a sentence beginning lower-case on the fall bench, and *"a moment of 1 newton metres"*. Invisible to sighted students, and the only description a screen-reader user gets. → Article agreement, capitalise the composed first character, and pluralise on the value — the same branch chemistry's C6-05 needed, so **write one shared helper for both key stages**. *Code; small.*
- **P4-27** · rung 4 says *"Gravity pulls down with 700 N"* where the unit's own discipline (and its next lesson's vocabulary) says **weight**; "the parachute pushes up" is air resistance on the canopy. Every other page in the unit says weight here. → Reword; no numbers change. *Code; small.*

---

### P5 · Pressure · 4 lessons · **23 findings** (S1 3 · S2 7 · S3 5 · S4 8)
*In §4: P5-24 → SYS-2 · P5-25 → SYS-3. P5 is the unit whose auditor found SYS-8's em-dash form (4 of 4 lessons — the only unit at 100%).*

**S1**
- **P5-07** · `pressure-in-liquids` · big question, hook prompt, hook commit **and rung-4 criterion 1** — *"The bottom jet shoots out furthest, every single time."* **Speed is right; range is not.** A jet from depth *d* leaves at √(2gd), so the bottom hole is unambiguously fastest — but its water has least height to fall. For a can standing on the surface the jets land on, range is R = 2√(h(H−h)), **maximised at h = H/2 — the middle hole.** The bottom hole only wins if the can is raised above the landing surface by more than the water depth, which the page neither specifies nor draws. *"Every single time"* is the claim that cannot stand: the commonest classroom setup gives the middle hole, so a teacher running the demonstration gets a flat contradiction — and **rung 4 marks the true answer wrong.** The lesson's own reveal already gets it right (*"and a faster jet"*). → Move the lesson onto the observable the physics delivers: *"comes out hardest and fastest, every single time"*, and criterion 1 → *"the fastest, hardest jet"*. If the range image is worth keeping (it is vivid), keep it truthfully by naming the setup — which would make it the best extension question on the page. That second option adds content, so it is Mide's call; the wording swap is the minimum repair. *Code; **Mide ruling** if the extension version is preferred; small.*
- **P5-12** · `upthrust-floating-and-sinking` · Your turn Q1 — **the page prints false arithmetic as its own model working.** Hold any floater under and the marked lines read Insert *"2.4 N − 10 N"*, **Fine-tune "2.4 − 10 = 7.6"**, Answer "7.6 N upwards". Three reachable states, all wrong (pine "5 − 10 = 5", cork "2.4 − 10 = 7.6", ice "9.2 − 10 = 0.8"), three clicks from load, on the one step whose entire job is to be the arithmetic. The engine already branches correctly on the **sign** for the note; only the equation is wrong. → Order the subtraction to match the answer: when upthrust exceeds weight render *"upthrust − weight"* and *"10 − 5 = 5"*, with the Formula line branching to *"the bigger force − the smaller one, and it acts the bigger one's way"*. Printing "5 − 10 = −5" is more honest to R = W − U but introduces negative forces at Year 8, which the unit avoids. **Add a build assertion that every rendered Fine-tune line evaluates true.** *Code; small.*
- **P5-13** · `upthrust-floating-and-sinking` · float tank — the tile labelled **"On a spring balance in the water"** shows **negative** forces for held-under floaters (cork −7.6 N, pine −5 N, ice −0.8 N). No spring balance reads negative; it goes slack. What is happening is the student's hand pushing **down**, which the bench's own narration two lines below describes correctly. The resting float state has an authored special case and the negative state has none — the SYS-5 signature. → Relabel the tile per state: *"The push your hand must give · 7.6 N downwards"*. The label already changes elsewhere in this bench, so the mechanism exists; keep the balance label for sinkers, where it is literally true. *Code + **Mide sign-off** (science wording); small.*

**S2**
- **P5-22** · all four lessons · Rung 1 — **on every one of P5's four Rung 1s the correct answer is the only option with no explanatory em-dash tail**, so a student scores 4/4 on the calculating rung of every lesson in the unit without reading a question. Answer *position* is properly varied (0, 2, 0, 2), so MRB-278 passes and the tell slips underneath it. → SYS-8 form 3, of which P5 is the estate's 100% case. *Code; small per lesson, medium for the gate.*
- **P5-03** · all four lessons · the attempt panel's lead says *"The numbers are the ones your own bench is showing"* while the bench is showing nothing (it is locked until the predict is committed) — false for every student who reads down the page in order. Worse on p5-03, where the resting default reduces the five-step working to "5 − 5 = 0". → Swap in a pre-bench lead while locked: *"Do the bench above first; these numbers will be the ones it shows you."* The engine already re-renders this panel on every bench change. *Code; small.*
- **P5-04** · `pressure-force-over-area` — the whole unit converts mass to weight, and this lesson introduces **10 N/kg in a bench sub-line with no gloss**, while its declared prerequisite (`non-contact-forces`) contains **zero** occurrences of "N/kg". The lesson that does teach it (`balanced-and-unbalanced`, 19 occurrences) is not linked from here at all. → Add `balanced-and-unbalanced` to `requires` (or at minimum `references`), and give the sub-line its half-clause the first time it appears — p5-03's Convert note already carries exactly that sentence. *Code; small.*
- **P5-09** · `pressure-in-liquids` · Your turn Q2 — a **side** hatch is the right transfer item, and the stem transfers the downward-column phrasing to it without the clause that makes it legal: nothing rests on a vertical hatch, and *"1600 N above it"* is a fictional equivalent column, on the page whose central repair is that pressure is not a downward thing. → One clause in the stem (*"…sits 4 m down, where a column of water of that area would weigh 1600 N"*) or one sentence in the Formula note. *Code, wording past Mide's science gate; small.*
- **P5-16** · `upthrust-floating-and-sinking` — the lesson prints **R = W − U** (R never expanded; "resultant" appears 0 times on the page) and then works examples of a *different* relationship (*upthrust = weight in air − reading in water*), while Q1 — the first independent item — uses a **third** form. Of the unit's eight attempt questions this is the only one whose relationship has no worked example on its own page, so the fading that works cleanly on the other three lessons is broken here. → Expand the symbols where the equation is printed, and make one of the two worked examples use the printed relationship (the natural pairing is a second stage on the stone the first example already uses). *Code; medium.*
- **P5-17** · `upthrust-floating-and-sinking` vs P11 — **the course gives a student two complete, unconnected accounts of floating, a year apart, and neither lesson mentions the other.** P11 (Y7) teaches it by density alone and the word "upthrust" appears **zero** times on either of its pages; P5-03 (Y8) gives the full force account and "density" appears only in its GCSE card. They agree numerically to the decimal (both give ice 92% submerged), which makes the silence more striking. P11's stated rule is about "a material", which its own rung 3 contradicts with a steel ship — and P5-03 is the lesson that could make the average-density distinction and does not. → Cross-reference both ways, add one reconciling sentence to P5-03 (*"being less dense than water is exactly what it takes to push aside your own weight of it before you are all the way under"*), and trim P5-03's GCSE card so it stops billing density-as-the-test as new (the C8-15 pattern). *Code + **Mide sign-off**; small.*
- **P5-21** · all four lessons · **safety wording** — no `safety_note` anywhere in P5, while p5-04's hook and subtitle describe a real demonstration in **imperative, do-it terms** (*"Boil a splash of water in an empty can, seal it, and cool it"* → boiling water, steam, a sealed vessel, a hot can, a violent implosion), p5-02's rung 4 opens *"You punch three holes down the side of a full can"*, and p5-01's hook says *"Hold a drawing pin between finger and thumb and squeeze"*. P4's springs lesson and P1 both carry the slot, so it exists and this unit does not use it. **Flagged, not drafted.** → §6. *Mide sign-off; small once ruled.*

**S3**
- **P5-01** · sand bench at the exact threshold — at 3 kg on 0.005 m² (exactly 6000 Pa) the verdict is "OVER THE LIMIT — IT SINKS IN" and the remedy names **the configuration the student is already in** ("bring the mass down to 3 kg or less"), because `holdmass` uses `floor` where its sibling `needmass` correctly uses `ceil` under the same `>=`. Plus a double full stop in every sinking state (the JS string and the authored template both supply it). → Two one-token edits. **Worth a bench guard asserting that the mass named in a "sinks" remedy, re-fed to the same predicate, yields "holds".** *Code; small.*
- **P5-02** · all four lessons · the head-row note tracks a **different variable** from the one that opens the bench, so it is wrong in both directions: change a control without committing → *"Both controls live"* over a hidden readout; commit without touching a control → the whole readout appears while the note still says *"Change a control to begin"*. A phone student who scrolls to the controls first hits a dead instrument and is told it is working. → Three states, not two; the rail's own `done_when: gate_and_a_control` already names both conditions. *Code; small.*
- **P5-08** · `pressure-in-liquids` at depth 0.0 m (one drag from the default) — the attempt panel becomes *"0 ÷ 0.02 = 0"* with the caption *"At 0.0 m down in fresh water, **pressing equally in every direction**"* — asserting a push of zero magnitude in the lesson whose subject is that liquids push, and handing the student a degenerate calculation as their one independent item. → Raise the slider minimum to 0.5 m (0.0 m has no teaching), or branch the answer note at zero and suppress the attempt panel's use of that state. → SYS-5. *Code; small.*
- **P5-14** · `upthrust-floating-and-sinking` · the opposed-beam figure at 390px — 480px wide in a 390px viewport, centred, so it bleeds 45px off each edge. **Six of its seven labels are damaged** and the seventh — **"17.0 N OVER"**, the whole point of the sinking panel — sits entirely outside the viewport and is invisible. The page does not scroll horizontally, so there is no way to reach it. → Stack the two panels vertically below ~430px, each at full width; the figure's scale is already parameterised, so a narrower viewBox at phone width is the smallest change. *Code, layout past Design; small.*
- **P5-15** · `upthrust-floating-and-sinking` — with a sinker selected, "Hold it right under" relabels itself to "Let it go" and **changes nothing else** (readout, narration, arrows and attempt panel byte-identical), on 40% of the bench's block choices, with a second label that is untrue. The null result is physically correct and worth teaching; the defect is that the bench says nothing, so a student cannot tell a correct null from a broken button. → Make the null the teaching: disable with a one-line reason, or keep it live and add *"Holding it under changes nothing here: it was already pushing aside a full litre, which is all the upthrust there is."* Do not leave the label toggling. *Code; small.*

**S4**
- **P5-05** · the sand bench heading *"Same weight. Different face. Different hole in the sand."* — "same weight" is false the moment the mass slider moves (one of only two controls), and the sand is binary, so there is one hole of one size or none. → Retitle to what the bench does, or make the mass control a preset. *Code; heading is Design's copy, so flag; small.*
- **P5-06** · Going further names the moments lesson and does not link it, and it is not in the page's `references`. → Add `moments` (and/or `simple-machines`, which owns the belief being re-confronted). *Code; small.*
- **P5-10** · *"a hosepipe on a hill runs harder than the same hose at the top of the slope"* — the comparison has no fixed term and reads as comparing a thing with itself. → *"…runs harder at the bottom of a hill than at the top of it."* *Code; small.*
- **P5-11** · p5-01 prints `P = F ÷ A` **with a symbol key**; p5-02 and p5-04 then print `P = W ÷ A`, introducing a new letter for the force slot **with no key at all** — exactly where *"the force here is a particular force, the weight of what is above you"* would be worth saying. → Give the stack/beam blocks the same three-line key the triangle block gets. *Code; small.*
- **P5-18** · the Archimedes sentence introduces **"fluid"** and **"displaced"** once each, unglossed, in an opt-in stretch — while "displaced" is the word an AQA candidate has to write and the page's own GCSE card promises Archimedes' principle. → One parenthesis: *"the weight of the fluid (a liquid or a gas) pushed out of the way — displaced, in the word you will meet at GCSE."* *Code; small.*
- **P5-19** · the altitude bench captions 1000 m as *"a Lake District summit"*; Scafell Pike is 978 m. It is the one anchor that is wrong and it is the UK one, which is the one a British class can check — every other place-name on the page is exact. → "a Snowdonia summit" (Snowdon 1085 m), or move the height to 950 m. *Code; small.*
- **P5-20** · `atmospheric-pressure` · the core explainer uses **"fluid"** as load-bearing ("as with any fluid — it presses in every direction") and never defines it, while its everyday meaning is "liquid", making the clause read as a non-sequitur in a paragraph about air. Precisely the everyday-vs-physics trap the protocol asks to be quoted. → Gloss in place: *"as with any fluid — any liquid or gas — it presses in every direction at once."* *Code; small.*
- **P5-23** · on three of four lessons the correct hook option is the longest, worst on p5-02 (77 chars / 14 words against a 30-char distractor). → SYS-8; lengthen the short distractors — p5-02's outlier would become a *better* wrong answer as the belief the page's own second Think Again confronts. *Code; small.*

---

### P6 · Waves and sound · 9 lessons · **16 findings** (S1 3 · S2 5 · S3 2 · S4 6)
*In §4: P6-01 → SYS-3 · P6-04 → SYS-2.*

**S1**
- **P6-07** · `how-sound-is-made` · chain bench, tuning-fork state — *"Its prongs move much less far than a plucked string **and it still fills a room, because it goes on doing it for a long time**."* Two things wrong. It contradicts its own lesson **twice** on the same page (Going further: *"A tuning fork held in the air is quiet, because two thin prongs push very little air"*; think-again: *"Rest a struck fork on a table top and the note jumps in volume"* — both of which depend on a bare fork being quiet). And the reason given is not physics: loudness is amplitude, and a sound sustained longer is not louder — so it plants a duration-equals-loudness claim one lesson before the amplitude lesson has to kill it. A real classroom contradicts it directly: this is the demonstration where the class complains they cannot hear the fork until it is put on the bench. → *"…and two thin prongs push very little air, so a fork held up on its own is quiet; stand its base on a table and the whole table pushes the air for it."* The bench then sets up Going further instead of contradicting it. *Code + Mide sign-off; small.*
- **P6-08** · `sound-is-longitudinal` · slinky bench — the lead declares the amplitude as **60 mm** and the branch notes assert it as the maximum (*"and that is as far across as any coil goes"*), while the readout one tile away says **57 mm**. All 21 slider positions on both drives were swept: the readout takes exactly three magnitudes — 0, 35 and 57 — and **never reaches 60 at any reachable position**, because the marked coil snaps to a drawn coil and its phase is quantised to eighteenths (57 = 60·cos 18°). On the lesson whose entire subject is *how far the material is displaced*, the page prints two values for the same coil in the same panel and calls the unreachable one the maximum. The SVG's live `aria-label` agrees with the readout, not the note. → (a) Cheapest: report the coil's actual displacement and keep 60 as the stated maximum — which turns the mismatch into teaching about sampling. (b) Better: place one drawn coil exactly at each crest/trough/compression/rarefaction so the note becomes true as written. Either way, **the bench guard should assert that a note quoting a value equal to `data-amp-mm` is only emitted where the readout equals it.** *Code + Mide sign-off; small (a) / medium (b).*
- **P6-10** · `frequency-pitch-and-loudness` · Going further — *"a road drill near 100 dB — **a million times** the energy of the whisper"*. By the page's own rule stated two sentences earlier ("every 10 dB is ten times the energy"), 70 dB is **ten million**. The paragraph exists specifically to teach that the scale is multiplicative, and it is the one place a student is invited to do the multiplication — so a student who does it correctly is contradicted by the page. No other pairing rescues it. → Two words. Worth checking the same claim is not repeated anywhere else in the estate. *Code + Mide sign-off; small.*

**S2**
- **P6-02** · three of six calculate rungs · **an inverse length tell** — the correct option is a bare quantity and *every* distractor carries a "because" clause: word counts [16, 16, **6**, 16], [18, **2**, 14, 18], [10, 12, 18, **3**]. A ten-to-sixteen-word gap, far outside MRB-278's own stated threshold — **but that gate is directional and a correct answer that is uniquely the shortest passes it untouched.** The unit already contains the remedy on its other three calculate rungs, where a second bare option (a unit trap) breaks the pattern. So this is three sets that were not finished, not a policy. → Give each of the three a second bare distractor in the pattern the other three use, and make the gate two-sided. → SYS-8. *Code; small each, medium for the gate.*
- **P6-05** · `transverse-waves-and-superposition` — the lesson is **titled** "Transverse waves, reflection and superposition" and carries that title in the breadcrumb, the unit index and four other lessons' end-matter, while **reflection gets one sentence** in the body, one clause in the key note, and one Going-further paragraph existing only to set up standing waves. No instrument, no worked example, no rung, no think-again, no drawing: all four rungs, both commits and the bench are superposition. A student who has done this lesson has met the word and nothing else, while the title tells them — and their teacher planning from the index — that a third of it was reflection. **The slug already disagrees with the title, and the slug is the honest one.** (Reflection of sound is properly taught two lessons later; the content is not missing from the course, only from the lesson that claims it.) → Drop "reflection" from the title, bringing it into line with the slug the URL already uses; or earn it with one short block. *Code; title wording past Mide; small.*
- **P6-14** · `sound-needs-a-medium` — the lesson never answers the question **every class asks** at the bell jar: *the jar is still there — why doesn't the sound come out through the glass?* The thread is mentioned once and never explained; nothing says the buzzer is suspended so it touches nothing, or that a buzzer resting on the base plate would still be heard. The gap is made **sharper** by the lesson's own next paragraph, which teaches that sound travels **fastest in solids** — so a student is told solids are the best carriers and asked to accept that a buzzer inside a solid glass jar goes silent. Rung 3 then asks them to explain it. It is also the standard GCSE follow-up. → One clause in the hook: *"it hangs on a thread so that it touches nothing solid: if it sat on the base plate you would still hear it through the glass and the bench, and the experiment would prove nothing."* Answers the question, pre-empts the contradiction, teaches the control that makes the demonstration valid, and gives rung 3 something to reward. *Code + Mide sign-off; small.*
- **P6-16** · `echoes-reflection-and-absorption` — the unit sets a stated threshold (*"15% — below this, no separate echo"*) and places **Mown grass at 20%**, so the bench positively predicts a hearable echo off a playing field at any distance over ~17 m: at 500 m it reports *"Your own shout, coming back… Both conditions are met."* No student has ever heard their shout come back off a school field, and this is the one claim in the unit a class can falsify at lunchtime. (The 20% coefficient is defensible for grass at normal incidence — which is why this is S2, not S1. The defect is the exemplar: the bench's own assumptions note treats every surface as *"flat and facing you squarely"*, which applied to grass produces a vertical wall of turf.) → Change the exemplar to something that really is a vertical surface of that reflectivity — a hedge, a treeline, a wooden fence — keeping 20% and gaining a case students genuinely can test. *Code + Mide sign-off; small.*
- **P6-17** · `echoes-reflection-and-absorption` · bar model — "cover the part you want" applied to a bar whose two parts are **both `d`** yields **`d = s − d`** as the on-screen result: an equation with the unknown on both sides, the one form a KS3 student cannot use, and the form that looks like the algebra error they are trained to avoid. The page then spends two sentences undoing its own instrument. It is the only place in the unit where an instrument makes a topic harder than the prose. → Special-case a bar whose two parts carry the same symbol: render `d = s ÷ 2` as the covered result and keep `d = s − d` as the *reasoning* line beneath it. The two sentences already written then explain a correct headline instead of correcting a confusing one. *Code, behaviour past Design; small.*

**S3**
- **P6-09** · `sound-is-longitudinal` and `ultrasound-at-work` — two of the unit's eleven sliders have a value readout **frozen at its build-time literal**: "25%" at all 21 positions, and "100 mm" from 10 mm to 200 mm. The slider works and every tile below it updates, so the one element whose entire job is to report the control's value is the one element that lies. Cause found in source: `_slider()` pre-fills the readout and it is only refreshed if the bench's runtime writes that key — the slinky bench never writes `mark`, the gauge never writes `d`. → Write the keys, as the other nine do. **Then add a build/gate assertion that every `data-*-out` key emitted by `_slider()` is in the set its bench writes** — a key with no writer is a readout that can only ever be wrong, and it is invisible to every existing gate because it renders, contains plausible text and never throws. The same assertion would have caught the near-miss `ks3_art/p6.py` records as having shipped two dead rail stops in silence. *Code; small each, gate small-to-medium.*
- **P6-11** · `frequency-pitch-and-loudness` · signal bench — every branch closes with *"Move the second dial to X mm"*, and X is 0.4 mm at maximum and **0.2 mm otherwise — the dial's own minimum**. So whenever the amplitude dial is at 0.2 mm the sentence instructs the student to move it to where it already is: following the instruction changes nothing, and the sentence whose whole purpose is to demonstrate that the two dials are independent demonstrates nothing. It fires in **6 of 18 states**, including the one a student reaches by dragging the loudness dial down to see what "quiet" looks like. → Suggest the far end of the dial from wherever it is. *Code; small.*

**S4**
- **P6-03** · ripple bench, at **the default state** — one string covers every non-breaking state from 1 in 30 to 1 in 8, saying *"well short of the roughly 1 in 7 at which a crest breaks"*. At 1 in 8 the wave is at 87% of the limit, and 1 in 8 is the **opening** state, so it is the sentence most students read. → Split the branch at about 1 in 12 and tell the truth about how close it is, which also makes the default state teach something. → SYS-5. *Code; small.*
- **P6-06** · superposition Your-turn at slider zero — the exercise sets *"Your two waves: 0 mm and 0 mm, arriving crest on crest"* and asks for five FIFA lines on 0 + 0; with one at zero, "arriving crest on crest" is meaningless, as the bench's own verdict says one line above. The bench handles zero beautifully; the exercise fed from it does not. → Substitute a fixed pair and say so, borrowing the sentence shape p6-06 already uses for its vacuum state. *Code; small.*
- **P6-12** · at 50 Hz — the bench's minimum, and the first state reached by dragging the pitch dial down — the captions read *"only **1 of those fit**"* and *"keeps exactly **1 vibrations**"*. Chemistry's C6-05 class. → A pluralisation helper in the composed-caption path; **if one is written it should serve both key stages**, with a sweep for other count-of-one states. *Code; small.*
- **P6-13** · the assumptions note vouches for *"45 pixels per millimetre up"*; measured from the rendered SVG it is **65** — off by 44%, while the horizontal figure checks out, which is what makes the vertical one read as authoritative. S4 because no student reasons from these numbers — but the note exists precisely so a reader can trust the drawing. → Correct the figure, or better **derive both from the drawer's constants at build time**: three P6 lessons publish hand-written pixels-per-unit figures describing generated geometry. *Code; small.*
- **P6-15** · `sound-needs-a-medium` Your-turn in the vacuum state — the panel correctly announces the substitution (*"…so these five steps use air across your 200 m gap"*) and the fixed line directly beneath still reads *"The gap and the material are the ones your own bench is showing"*. The page contradicts itself in consecutive sentences, and it is the fixed one that is wrong. → *"The gap is the one your own bench is showing."* True in both states. → SYS-5. *Code; small.*
- **P6-18** · echo bench verdict strings — three composed-caption defects: **"Foam wedges sends"** and "Heavy curtain sends" (subject–verb agreement, on a page read aloud in class); *"**Plenty** is coming back"* used for both 90% and 20%, where 20% is five points above the page's own "not enough" line; and *"so **the room** sounds live"* printed for bare rock (glossed "a quarry") and mown grass ("a playing field"). → Compose the verb correctly or give each surface a `verb`; branch the quantity word on the percentage; take the scene word from the surface's own gloss, which already exists in the figure data. *Code; small.*

---

### P7 · Light · 7 lessons · **32 findings** (S1 5 · S2 13 · S3 2 · S4 12)
*In §4: P7-30 → SYS-V · P7-31 → SYS-3 · P7-32 → SYS-2. P7-04 is also the estate-wide arrowhead finding (SYS-A).*
*⚠️ The lesson order in this run's own briefing was wrong (it came from an alphabetical directory listing). The unit runs light-travels → reflection → refraction → lenses → eye → colour → why-things-look-coloured, which is what the `prev`/`next` chain, the index and the file numbering all say. **P7's auditor audited in the correct order and said so — no finding is affected**, but a fix run must not inherit the briefing's order.*

**S1**
- **P7-22** · `colour-and-the-spectrum` · prism bench — **one of the estate's three worst.** Measured from the served path data: the incident beam extended straight reaches the screen at y ≈ 389, **below every exit ray**, so every colour is deviated *upward, toward the apex* (a prism deviates toward the base), and the deviation runs **red 219.8 > orange 185.0 > yellow 150.2 > green 109.6 > blue 63.2 > violet 22.6** — exactly backwards. That is `LIGHT-23`, registered on this page as the misconception this bench confronts, **drawn by the instrument built to kill it**, and contradicted by its own rung 1 one screen below. The top-to-bottom colour order is R,O,Y,G,B,V, which *looks* like a spectrum — which is why it survives a glance. → Recompute the fan so it sits entirely on the base side of the extended incident beam with red nearest it (simplest: flip the prism apex-down and keep the current y-values). **Add a build assertion in `ks3_art/p7.py`: the ray for the highest-frequency key must be further from the incident line's screen intercept than the ray for the lowest** — so this class cannot ship again. Also draw the faint dashed "where it would have gone" line: rung 1 asks about exactly that line and the bench does not show it. *Code; **Mide signs the redrawn geometry**; Design sees it; medium.*
- **P7-04** · every ray drawing in the unit — **not one light ray anywhere in P7 carries a direction arrowhead.** A line with no arrow is not a ray; arrows on rays are the first thing a UK teacher marks and a standard GCSE mark loss. Three diagrams become readable as the opposite of what they teach: the reflection bench is perfectly mirror-symmetric so nothing distinguishes incident from reflected; the refraction block read right-to-left shows light bending **away** from the normal on entering glass; and the eye bench and straw figure draw undirected lines between a scene and an eye in the two lessons whose registered misconception is *your eyes send something out*. Not a stack limitation — `ks3.js` hand-composes arrowheads on the race lanes and the object arrows. → SYS-A: one shared `<marker>`, applied to ray classes and **not** to normals or ghosts, plus one sentence in the reflection explainer telling students to draw one. *Code; Design sees the arrowhead; medium.*
- **P7-19** · `the-eye-and-the-camera` · the pupil — **the drawn opening never changes size, and the part that does change, changes the wrong way.** From the path data at all five light levels on both instruments: the gap between the two marks is *always* 12 units; each mark grows from 12 units in bright sunlight to **66 units on a moonless night**. The marks are the *stop* — the opaque part — so the hole is drawn constant and the blades are drawn growing as the light falls, when a dilating iris does the opposite. A student dragging from sunlight to darkness watches the front of the eye **close** into a near-solid pillar, while the readout beside it says the opening goes 2.0 → 8.0 mm and the gate question they answered a minute ago says the pupil opens in the dark. Compounding it, both rays are routed to land **inside the opaque marks at every setting**, so the drawing also has light passing through the iris. → Invert the construction: pin the marks' **outer** ends to the case and let the inner ends move with the opening, so the gap is `2 × rPx` and grows in the dark; `rPx` needs rescaling and a minimum visible blade. The ray waypoints then become correct as written. **Re-drive all ten states after the change**; every readout and note is already right. *Code; Design sees the redrawn iris; small (but must be checked at all ten states).*
- **P7-10** · `refraction` · the straw figure — **the figure that exists to explain the illusion draws the illusion wrongly.** The dashed "back" line is not the backward extension of the ray reaching the eye: from (520,140) the emergent ray's backward direction is (−280, +50), and the drawn dashed line runs (+220, +156) — the wrong quadrant — leaving the glass through its right-hand wall and ending in mid-air. The **"WHERE IT LOOKS"** marker is not on that dashed line either; it sits on the **real in-water ray**, i.e. on a point the light genuinely passes through. So the drawing asserts that the straw's end appears at a place on its own actual light path, and the one construction line that would show why points somewhere else. The figure's `aria-label` describes the *correct* figure, which is not the one drawn. Every rung-3 and rung-4 answer depends on this. → Minimum: redraw the back-projection as the true extension (`M520 140 L392 163`) and move the marker onto it, directly above "WHERE IT IS", so the gap between them *is* the apparent-depth story. **Better (Design brief):** draw **two** rays from the straw's end to two nearby points on the surface, refract both, and let their two dashed back-projections **intersect** at the apparent position — the honest construction, which delivers the "higher **and closer**" the alt text already promises. Add arrowheads while the drawer is open; note also that the drawn emergent angle (~80° against ~32° inside) is far steeper than water allows, and the convention note covers only the bench. *Design brief → Code; Mide signs the redrawn science; medium.*
- **P7-23** · `colour-and-the-spectrum` · prism readout — with **blue and red** in and the second prism placed, the verdict tile reads *"One white patch — the colours put back together"*. Blue and red recombine to **magenta**; white needs the whole spectrum, and the state's own input sub-line says so. The **drawing is honest** (the outgoing beam is stroked a dusky pink), so the tile contradicts the picture beside it as well as the physics — and it undercuts the lesson's argument that a prism only gives back what went in. → Branch the recombined verdict on the input tab, which already carries `data-word` and `data-colour`: *"One patch of pinky-purple — the two colours put back together, and still no yellow or green."* **This state is arguably the best teaching state on the bench once it tells the truth**, because it separates "recombined" from "white". *Code + Mide sign-off on the colour word; small.*

**S2**
- **P7-07** · `reflection-mirrors-and-scattering` vs its claimed statement `LGT.04a` "imaging in mirrors" — **the one genuine curriculum gap in P7.** The lesson explains beautifully *why* a mirror can form an image and never treats the image itself. Full-text search of all eight built files: nowhere does a student meet *the image is as far behind the mirror as the object is in front*, *upright*, *same size*, *virtual*, or *laterally inverted*; "behind the mirror" appears **zero** times; and there is **no plane-mirror ray diagram at all** in the unit that owns the statement. A student finishing P7 cannot answer "why does writing look backwards in a mirror?" or "where is your reflection?" — the two questions a KS3 class actually asks — while the lesson's GCSE card promises "ray diagrams for plane and curved mirrors, **virtual images**" as if the KS3 half had been done. → One figure and one short explainer between the specular/diffuse block and the formula block. **The drawing:** an object arrow before a plane mirror, two rays to the mirror obeying i = r, both arrowed, reflections continuing to an eye, both back-projected as dashed lines meeting at the image behind the mirror, with the two equal distances marked. **The prose:** same size, upright, as far behind as in front, and virtual — *"no light ever goes behind the mirror; the light only looks as if it started there"*, which reuses the refraction lesson's own brain-traces-back move. Then add a self-marked rung, or swap rung 4's wet-road question for the mirror-writing one. *Design brief + Code; **Mide signs the science and the extra teaching time**; medium.*
- **P7-29** · all seven lessons · **every ray diagram at 390px** — this is the ray-diagram unit, and on a phone every figure in it renders about **110 px tall with in-figure labels at roughly 4 CSS pixels** (1000-unit viewBoxes scaled to 286px, a factor of 0.286). The angle annotations are unreadable and the caption strips wrap inside the figure — while the four readout tiles beneath each bench each get a full-width card with 20px+ type. **The drawing — the thing the whole unit is about, and the thing a student must copy into a book — is given the least space on the screen half the audience uses.** → Below ~560px put the figure in its own `overflow-x: auto` scroller at a fixed 560–640px SVG width, **exactly as the band tables already do** (`.ks3-lband-scroller`, which is why the comparison tables stay legible at 390 while the ray diagrams do not). One horizontal swipe reveals it and the page still does not overflow. *Code; Design signs the phone treatment; medium.*
- **P7-20** · `the-eye-and-the-camera` — each ray's single vertex is at the **aperture** (x=402), not at the lens (x=416–504), so the drawing shows light changing direction at the hole and passing through the lens without deviating — **pinhole geometry with a lens ornament behind it**, one lesson after an entire lesson distinguishing the two, on a page that says *"A convex lens behind that opening refracts the rays so that all the light from one point lands at one point."* Only one ray is drawn per object point, so nothing is gathered and nothing is brought back together: the lens's whole job is invisible. → Draw two or three rays from the scene's top through different heights of the lens, bending at the lens face(s) and converging on the retina — the construction the previous lesson's own panel already draws correctly. At minimum, move the vertex from the aperture to the lens. *Design brief → Code; medium.*
- **P7-24** · `colour-and-the-spectrum` · the path through the glass — the incident beam stops at (262,210) **inside** the prism and the exit rays begin at (330,210), also inside it: **68 units of glass with nothing drawn between them.** The lesson's mechanism sentence is *"One bend on the way in, another on the way out"*, and the drawing shows neither: light goes in, disappears, and comes out already sorted — the "prism as magic box" reading the lesson exists to prevent. → Draw the internal path (one white segment from entry to exit face, bent toward the normal at entry) and start the coloured fan at the exit face. Land with P7-22 — same drawer. *Design brief → Code; medium.*
- **P7-25** · `colour-and-the-spectrum` · the spectrum band — drawn as **six hard-edged blocks with visible vertical joins**, directly above a paragraph reading *"a band that has **no joins in it** — between yellow and green there is no line, only a gradual change"*. The drawing asserts `LIGHT-22`, the misconception the caption and the second think-again both exist to demolish; students hold the picture as the authority over the words. → Paint the band with an SVG `linearGradient` red→violet with the six named stops, and move the six names to tick labels beneath a continuous strip. The two arrows and the layout stay exactly as drawn. *Design brief → Code; small.*
- **P7-03** · `light-travels` vs `reflection` — lesson 1 says shadows are **sharp**, lesson 2 says they are **soft**, two pages apart, and neither mentions the other. The first claim is also wrong unqualified (an extended source gives a penumbra), and lesson 2 has just given the mechanism without connecting it back. → Qualify the first (*"a small, bright source casts a shadow with sharp edges"*) and add one clause to the second (*"which is why the shadows in a real room are softer than the ray model on its own predicts"*). The pair then teaches the point instead of colliding on it. *Code, science wording past Mide; small.*
- **P7-05** · `reflection` — on the three scattering surfaces the bench draws a fan at visibly different angles while the tile reads *"ANGLE OF REFLECTION / 80° / **measured from the normal**"*, and the drawn normal is the only normal on screen — so the tile says all five fanned rays leave at 80° from that line, false of four of them. The note underneath rescues it in words (*"from the normal **of the facet it hit**"*) but the tile is what a student reads. → Branch the sub-line on `spread`. One conditional; the wording already exists to copy. *Code; small.*
- **P7-06** · `reflection` at 0° — the incident ray, the reflected ray and the normal are drawn on the same line, and the 7px solid blue rays completely cover the 3px dashed grey normal, so the figure becomes **one blue vertical line labelled NORMAL** — on the page whose central vocabulary point is that the normal is a construction line and **not light**. It is the state that answers the lesson's own "arrives straight on" case. → Offset the two rays a few units either side and label them "in"/"out", or draw the normal on top and let P7-04's arrowheads carry direction, plus a per-state note. *Code; Design sees the offset; small.*
- **P7-11** · `refraction` · Key fact and Key note — **"denser" appears only in the two summary cards** (the exact sentences a student copies into a book) and nowhere in the teaching that precedes them, unglossed, **two blocks after the lesson's own think-again has demolished "water is thicker"**. So the page retires one everyday thickness word and hands the student another. "Optically denser" is not the mass density they meet in P11, and the unqualified form carries the single sentence most often taught wrong in British KS3 classrooms. **The fix already exists and is not reaching anyone**: the authored `vocabulary` for this lesson contains *"denser — used here of a transparent material that slows light more"* (→ SYS-V). → Gloss in place: *"a denser transparent material (one that slows light more — which is not the same as a heavier one)"*, keeping the word the GCSE specification uses. *Code + Mide sign-off; small.*
- **P7-12** · `refraction` at 0° — the ray covers the normal completely, giving one blue line labelled NORMAL, **and this is the state the lesson deliberately sends the student to**: rung 2 ("the one that catches people") and the bench gate are both this case. The caption strip is also struck through by the ray. → Draw the normal after the rays, or offset the 0° ray; move the caption below the drawing's baseline (there is room in the viewBox). *Code; small.*
- **P7-13** · `refraction` · Going further — *"keeps striking the inside of the wall at a **steep angle**"*. Steep to what? The lesson has spent three blocks insisting every angle is measured from the normal, and read the natural way (steep to the surface) it is **the wrong condition**: TIR needs a large angle from the normal, i.e. a grazing angle to the wall. The one sentence describing TIR describes it ambiguously, in the lesson that made a virtue of never doing that. → *"at a large angle to the normal — a glancing angle to the glass"*. Reinforces the convention instead of undercutting it. *Code + Mide sign-off; small.*
- **P7-15** · `lenses-and-images` — the picture on the screen is drawn as **a bare vertical line with no arrowhead**, sitting on top of the screen line, while the object beside it is a proper arrow and **three separate labels call the picture an arrow** ("the two arrow heights are to one scale", the aria-label's "inverted picture arrow", the convention note). The readout tile asserts "Upside down, and left for right" about a line that has no way up. **The next lesson's bench draws the same inverted image with an arrowhead**, so the unit contradicts itself one page apart. → Compose the same two head strokes the eye bench uses, pointing down, and inset the image a few units left of the screen line. *Code; small.*
- **P7-16** · `lenses-and-images` at u = 2000 / v = 50 — the drawing degenerates into **a picture of a lens**: the hole sits at x = 861.5 so the "box" is an 18-unit sliver, the 8 mm picture is 2.3 units and invisible, and the two rays appear to converge to a single point on the screen — which is the lens figure directly below, **on the page whose whole argument is that a pinhole selects one ray and a lens gathers a bundle.** Correct behaviour, wrong model: a student who lands here concludes a pinhole focuses. → Clamp the hole's stand-off from the screen and give the image the same minimum the blur already has, so a box always reads as a box; the tiles stay exact because only the drawing is compressed and the axis label already declares the compression. Add a state note at the extremes. *Code; Design sees the clamp; small.*

**S3**
- **P7-14** · `refraction` figure `aria-label` at 0° — the fixed template always ends *"shifted sideways from the path it would have taken"*, and at 0° there is no shift; **the code knows** — it sets the ghost path to `M0 0` and hides it at exactly this state. So a screen-reader user is told the opposite of what the lesson's central zero-angle case teaches, at the state the gate sends them to. The visible note is correct at the same moment, so only the non-visual channel lies. → Branch the label on the same condition the ghost already branches on. *Code; small.*
- **P7-26** · prism figure `aria-label`, **every state** — *"with 6 coloured **ray or rays** drawn leaving it"*: an unresolved pluralisation template shipped to students as text, on the one channel a screen-reader user has for the figure that carries the whole lesson. → One ternary; while there, branch the single-colour + second-prism state, which ends *"recombined into one beam"* when the note correctly says there is nothing to recombine. Grep the other six P7 wirings for the same construction. *Code; small.*

**S4**
- **P7-01** · hooks · the correct option is at **index 1 on six of the seven lessons** and is also the longest on five. A student who notices can predict every reveal in the unit — defeating the commit-then-reveal design, whose whole point is that the student's own wrong prediction is what gets confronted. → SYS-8. *Code; small each, gate medium.*
- **P7-02** · `light-travels` · the FINE-TUNE model line prints **`3.33e-6`** — calculator-display notation, not standard form, not KS3, and inconsistent with the unit's own style (it spells every large number with thin spaces and never uses a power of ten in seven lessons). The line below already translates it, so the untranslated line does no work except introducing an unexplained symbol where a struggling student is checking their arithmetic. → `0.000 003 33` in the unit's own spaced style. Sweep the other P7 attempt panels for the same formatter. *Code; small.*
- **P7-08** · at 80° on a scattering surface the fan generator clamps to ±80°, so **three distinct rays are drawn, not the five the convention note declares**, and the fan is one-sided — silently suggesting that scattering favours one side at glancing incidence. → Compress the spread by the headroom so five distinct rays are always drawn, or cap the slider at 70° as the refraction bench already does. *Code; small.*
- **P7-09** · all three numerical rung-1s — **the correct option is the only one that is just the answer**; every distractor carries a "because" clause ("65°" against 10/12/12-word distractors). The giveaway is brevity, which the existing directional gate will not see. → SYS-8 form 3. *Code; small each.*
- **P7-17** · at the narrowest hole the tile reads *"**about 1 times** / against the narrowest hole"* — a comparison of a thing with itself, in broken English. Same family as chemistry's C6-05. → Branch at 1 and drop the sub-line in that state. Sweep the other P7 benches for the same unbranched "N times" formatter. *Code; small.*
- **P7-18** · the lens figure's caption says *"Every ray is refracted **twice**"* and the drawing bends each ray **once**, at the lens's mid-line. The single bend is the standard convention and is right for KS3; the caption is what makes the drawing look wrong. → Add the half-clause that makes the convention explicit (*"the drawing shows the two bends as one, which is the usual shortcut"*) — cheaper than redrawing, and the convention is worth having before GCSE. *Code; Design flagged; small.*
- **P7-21** · the eye's case path ends with a **70-unit unlabelled grey stub protruding from the front of the eyeball at pupil height**, with nothing on the page naming it. A student hunting for the optic nerve — the one part of an eye that sticks out — will find this, on the wrong side. The caption strip claims to list what is drawn. → Label it or delete it. *Design brief → Code; small.*
- **P7-27** · on a single-colour input both middle tiles name the same colour, one as *"the lowest frequency present"* and one as *"the highest"*. Defensible (in a narrow band the only frequency present is both) but it reads as a broken instrument, on the two states a student picks precisely to check whether the bench is honest. → Collapse the pair on `single`, which the wiring already computes. *Code; small.*
- **P7-28** · when the whole of the arriving light is reflected — **seven of twenty states** — the tile reads *"ABSORBED / **nothing**"* with the fixed sub-line *"its energy warms the object slightly"* still underneath it. → Blank the sub-line when the absorbed list is empty (the wiring composes that list, so the test is free). → SYS-5. *Code; small.*
- **P7-33** · on five lessons the **third rail stop ticks before the second**: the fixed-figure stop is marked done the instant the *bench's* gate is answered, before the student has scrolled past the bench. The rail visibly goes 1 ✓, 2 ✗, 3 ✓ — reads as a bug and credits a section that has not been seen. Documented as Design's own `DONE` threshold, so a deliberate choice with an undesired consequence. → Move the sibling mark to the same threshold the bench uses (gate **and** a control touched) so stops tick in order; or tick on first scroll into view. *Code; Design ratifies; small.*
- **P7-34** · the two sentences carrying the hardest mechanism in each of two lessons are **48 and 51 words**, three clauses, a colon and an em-dash apiece — the two sentences a struggling Year 8 most needs to hold, and the two longest on their pages. → Split each at its colon; the three-way split then reads as three things, which is what it is. → SYS-R. *Code; small.*
- **P7-35** · six of seven lessons carry **no safety line** while three describe things a student will do — full pinhole-camera build instructions, a convex lens gathering light to a point, a prism in white sunlight, and ray boxes at the bench. **The Sun is the obvious hazard, and it is exactly what a child will point a pinhole camera or a lens at.** The unit's one good safety line — *"Never look directly at the Sun, at a welding arc or into a laser, even briefly — the damage is to the retina, it is painless at the time, and it does not heal"* — sits on lesson 5, which a student doing lesson 4 or 6 has no reason to have read. **Flagged, not drafted.** → §6. *Mide sign-off; small once ruled.*

---

### P8 · Electric circuits · 7 lessons · **23 findings** (S1 7 · S2 9 · S3 3 · S4 4)
*In §4: P8-19 → SYS-2 · P8-20 → SYS-V (P8's unit-grain measurement — 25 of 33 units, 650 definitions — is the half that explains why the chemistry audit missed it). P8's SYS-3 probe was **struck** (box test); all seven lessons collide.*

**S1**
- **P8-01** · `potential-difference` · Going further — *"a **400 000 V power line is not dangerous because of the number**, and a car battery at 12 V can weld metal."* Two problems. **(a)** The paragraph's point — volts alone do not measure danger — is correct and worth teaching, and a 400 kV transmission line is **the one object in the world where volts alone very nearly are** the danger: it arcs several metres through air, so you need not touch it. **(b)** At every width rendered, the sentence breaks after "is not", so a scanning Year 8 reads *"a 400 000 V power line is not dangerous"* — on a page whose sibling lesson carries a never-touch-mains safeguarding note. → Keep the teaching point, change the example to one where it is true — the static shock, which also connects to P9: *"…the ten thousand volts that jump from a door handle to your finger leave you unhurt, while a car battery at 12 V can weld metal. The volts say how much energy each bit of charge carries; the amps say how many bits go past each second. Damage needs both — and a power line has both, in enormous quantities, which is why you never go near one."* → §6. ***Mide ruling*** — science accuracy **and** how a hazard is described to a child. Code executes once ruled. *Small.*
- **P8-02** · `resistance` — *"A thick short copper wire is a couple of ohms"*, and the bench models copper at exactly **2.0 Ω**, showing 6.000 A at 12.00 V under *"a small push buys a lot of flow"*. A thick short copper lead is a few **thousandths** of an ohm; 2 Ω of copper is over a hundred metres of 1 mm² wire. And **the unit contradicts itself one lesson later**: `conductors-and-insulators` puts copper at 0.05 Ω / 10 cm and states *"a short piece of copper is a few hundredths of an ohm"* — **two resistances forty times apart in consecutive lessons, with an instrument vouching for each**, while the next lesson explicitly invites the comparison ("the value every other specimen here is compared against"). Second consequence: two of the three places in the estate refuse to print an ammeter reading for copper *and say why* (a bare copper wire across a supply is a short circuit, so there is no honest figure); `resistance` shows the same object drawing a calm 6.000 A and calls it ordinary. → Replace the "Thick copper wire" specimen with **"A 2 Ω resistor"** (or a coil of thin constantan): the other four components, all the arithmetic, the note text and the ratio teaching are untouched. Reword the explainer to agree with L6. *Code; **Mide sign-off** on the replacement component; small.*
- **P8-04** · `building-and-measuring-a-circuit` · voltmeter-in-loop states, and rungs 1 and 2 — the bench reports **2.94 V**, and that value cannot be produced by the model the same panel states. Battery 3.00 V, lamp 10 Ω, voltmeter 1 MΩ, and the bench's own caption "about 3 millionths of an amp". At 3.0 µA a 1 MΩ meter reads **3.00 V**, leaving the lamp 30 microvolts. For 2.94 V the lamp would need 20 kΩ — a factor of two thousand. **Three numbers sit in one frame and no two are consistent**, on the lesson about taking trustworthy readings, using exactly the calculation the previous two lessons taught. It propagates into rung 1's evidence and rung 2's whole stem. → Make the reading **3.00 V** and tell the truth about why it looks identical to a correct build — a better lesson than the fudge: *"…the whole battery p.d. is now across the meter itself and the lamp is left with microvolts. That reading is correct and completely misleading: on its own it looks exactly like a working circuit, and only the ammeter's 0.00 A gives the fault away."* Rungs 1 and 2 then become **sharper**, not weaker. (Keeping 2.94 V would need a ~490 Ω meter, which is not a voltmeter. There is one honest repair.) *Code + **Mide sign-off** (a printed value in a bench and two rungs); small.*
- **P8-05** · `resistance` · component bench — the note's size adjective is keyed to the component's authored **band**, not to the current on screen: thin nichrome at 1.50 V passes **0.300 A** and is called *"a large current… that is what a low resistance means"*, while the 10 Ω resistor at 12.00 V passes **1.200 A** and is called *"**only** 1.200 A… the reading is small because the resistance is high."* **Four times the current, called small.** And 0.300 A is the exact current this unit has used for a working torch lamp since lesson 1. The model it installs is the damage: "large" and "small" become fixed labels belonging to the *component*, on the lesson whose thesis is that current depends on V and R together and that only the ratio belongs to the component. SYS-5 in its most consequential form. → Derive the adjective from the rendered current (≥1 A "a large current", 0.1–1 A "a healthy current", 10–100 mA "a small current", <10 mA "a tiny current") and drop the fixed "only". Keep the ratio sentence — it is the teaching and is correct in every state. **Then extend the bench guard: assert that a caption's size vocabulary agrees with the value beside it.** *Code; **Mide sign-off** on the thresholds; small (medium with the guard).*
- **P8-03** · `conductors-and-insulators` · Your turn Q1 — the Fine-tune line prints **the mantissa of the prefixed answer instead of the quotient**, so it asserts false arithmetic in **7 of 14 reachable states**: `6.0 ÷ 0.0000012 = 5.0` (true value 5 000 000) → `R = 5.0 MΩ`; `6.0 ÷ 3e-12 = 2.0` → `R = 2.0 TΩ`. The step note beneath each reads *"Volts divided by amps leaves ohms"*, so the student is told the printed number **is** in ohms and the answer line silently multiplies it by a thousand, a million or 10¹². **That is exactly the unit-prefix error the whole five-step method exists to prevent, printed as the model answer.** A student who followed the method correctly and wrote 5 000 000 marks themselves wrong. → Compute and print Fine-tune in **base units** and let the Answer line do the prefixing, which is what it is for. **Add a build assertion that a printed `a ÷ b = c` satisfies `a / b ≈ c`** — this class would then be closed estate-wide. *Code; small (medium with the assertion).*
- **P8-06** · `conductors-and-insulators` · Your turn, copper states — the bench deliberately gives no ammeter reading for copper and the lesson says why in its own footer (*"a bare copper wire across a supply is a short circuit… so there is no honest figure for the meter to show"*), and the check button is disabled with an unusually good affordance (*"Waiting on a specimen the ammeter can read"*). **Typing one character into any box enables the button**, and the marked panel then supplies the figure the page has just said does not exist: **"120.0 A stays 120.0 A"** → `R = 0.05 Ω`. Two harms: the page contradicts itself within one screen, and **120 A is presented to a Year 8 as an ordinary bench measurement with no comment** — a current that would vaporise the wire, and the same object `building-and-measuring-a-circuit` correctly refuses to quantify. → (1) Make the specimen guard authoritative: the gate predicate currently ORs "has a reading" with "has written a line"; it must **AND** them. (2) Remove the copper figures from the composition so a future wiring change cannot expose them — the marked panel should say what the footer says. *Code; **Mide sign-off** if the copper panel gains any new sentence; small.*
- **P8-07** · `conductors-and-insulators` · conductor-band note — one fixed template over three specimens, false about two. Under **pencil lead**: *"…which is why it is used where you want heat rather than where you want a wire"* — that clause is nichrome's, printed verbatim under a pencil; graphite is not used as a heating element, and the student is told a false fact about a familiar object in the lesson whose method is "the difference is measured, not declared". Under **nichrome at 10 cm**: *"passes **5.5 A**… enough to light a lamp comfortably"* — eighteen times this unit's own torch-lamp current, and 33 W in 10 cm of thin nichrome is a glowing-red wire and a burn. (The 1.10 Ω itself is reasonable; the narration is not.) → Split the closing clause per specimen and derive "enough to light a lamp comfortably" from the current rather than the band. Same SYS-5 mechanism as P8-05. *Code; **Mide sign-off** on the graphite clause; small.*

**S2**
- **P8-09** · all seven hooks — the correct option is **A on six of seven**, and in five of those six it is also the longest or joint-longest. MRB-278's reorder covers the fourteen marked rungs and does its job (indices properly spread); hooks are outside its reach, and the source docstring records the reorder as applying to the marked rungs only. The hook is not machine-marked, so the tell is softer — but the reveal restates the correct reasoning immediately, so across six lessons a student learns that A is the answer and carries the habit into the rungs that **are** scored. → SYS-8. *Code; small per unit, medium for the gate.*
- **P8-10** · three "Rung 1 · Calculate" rungs — **the correct option is the only one with no reasoning attached** while all three distractors carry an explanatory clause, so a student scores 3/3 by picking the naked number. The shape is understandable (distractors must name the misconception they encode) but the result is a positional-equivalent tell MRB-278 cannot see. **The fix already exists in the unit**: the two Calculate rungs that do *not* have it give all four options a clause. → Give the correct option a clause of the same shape ("0.15 A — the branch currents add to the main current"), and extend the gate with the shape check. *Code; **Mide sign-off** on the three added clauses; small.*
- **P8-11** · `current-and-circuits`, `current-at-a-junction`, `potential-difference` — **the ohm reaches students two and one lessons before the lesson that defines it**, and not only in adult-facing footers: lesson 1's symbol key says *"Resistor · a fixed value"* (of what?); lesson 3's branch tiles read "a lamp, 10 ohms" on every one of sixteen bench states; lesson 4 has a **control the student presses** labelled "A 20 ohm resistor" and a rung-3 stem using it. None is load-bearing, but a Year 8 meets an unexplained unit on a control they are pressing, three times over, with no way to know it is safe to ignore. → One clause at first student-facing use, in lesson 3's bench lead — which also does real work, because "why is the split uneven?" is that lesson's whole question — and rewrite lesson 1's *"a fixed value"* to *"makes the current harder to push through"*. (Swapping the taught order is **not** recommended: resistance needs potential difference and the junction lesson does not.) *Code; **Mide sign-off** on the clause; small.*
- **P8-12** · `series-and-parallel` · rung 4 criterion 5 — the student must produce and then **self-mark** a sentence containing *"short them out"*, a phrase this page never explains; the unit does not explain it until two lessons later, and the proper definition lives in authored vocabulary that never renders (SYS-V). On the one rung where they mark their own work and cannot ask. → Gloss in place, where the idea does its work: *"…give the charge an easy path straight past them, so they get nothing."* *Code; small.*
- **P8-13** · `current-and-circuits` — the bench's gate sets a scenario at **0.30 A** and the correct answer is "Exactly 0.30 A"; the moment the student commits, the bench opens at **one cell** and the meter, in exactly the position the gate named, reads **0.15 A**. The number they have just reasoned about is contradicted by the apparatus at the instant of the payoff — and checking the bench against the commitment is the behaviour the gate is designed to produce. → One attribute: `data-start-cells="2"`, so the bench opens on the 3.0 V / 0.30 A state the gate describes. The 1-cell state stays reachable as the first press. *Code; small.*
- **P8-14** · unit-wide, decided in `current-and-circuits` — the unit's thesis is that current is not used up, and **the strongest available argument for it is a rate argument** (a current is charge per second, and a rate is not a substance any more than a speed is). That argument is never made in the main teaching: the per-second idea exists correctly, but only in `Going further` — the layer students skip. The explainer, Key fact and Key note all define current as "a flow of charge" without the rate, and the unit's answer to "what is used up then?" is energy, which is true but is a second quantity the student must now also hold. A gap rather than an error ("flow of charge" is the national curriculum's own wording). → Promote one clause where amperes are introduced: *"An amp is a **rate** — it says how much charge goes past a point each second, not how much charge there is. That is why a bulb cannot use it up: you cannot use up a speed."* The Think-again's existing answer then lands on prepared ground. *Code; **Mide sign-off** — it is a pitch decision about bringing a GCSE framing forward; small.*
- **P8-15** · `conductors-and-insulators` · verdict tile — the same material **changes category when you make it longer** (pencil lead "a conductor" at 10 cm, "a poor conductor" at 100 cm; tap water "a poor conductor" → "an insulator, in practice"). Defensible — the lesson does say the word is a practical judgement — but the bench never says it is doing it, and it lands two screens below the hook whose **wrong** answer is *"It depends on the length"*. A student who watched tap water become an insulator by being stretched has been shown something that looks a great deal like the answer they were told was wrong. → One clause on the sub-label when a specimen's two lengths straddle a boundary: *"the same water, a longer path — the word follows the current, not the material."* Turns the contradiction into the lesson's own point. *Code; **Mide sign-off**; small.*
- **P8-08** · `conductors-and-insulators` · Your turn Q1 — the practice item tracks whatever is clipped into the bench, so it can be any of fourteen, and **seven require a unit conversion the page never teaches**: both worked examples convert milliamps only, and the student can land on µA, nA or **pA**, needing division by a million, a billion or a million million and, at the pA end, standard form — which is KS4. **The first practice item can be harder than anything worked**, which is the scaffolding failure the protocol names explicitly, and the page's own instruction does not help because the pA states *are* readable. → (a) Restrict Q1 to states whose current is in A or mA — a one-predicate change; or (b) teach the prefix ladder once, in the figure that already spans fourteen orders of magnitude, with a small "mA, µA, nA, pA — each a thousand times smaller" strip beside the axis. **(b) is the better lesson and a small Design ask; (a) is the safe fix if this must land before September.** Neither removes the need for P8-03 and P8-17. → §6 for which. *Code (a) / Design brief + Code (b); **Mide ruling**; small / medium.*
- **P8-25** · all seven lessons · **safety wording** — P8 carries exactly one safety-related line in the whole unit (the `safeguarding_note` on `conductors-and-insulators`, which reads well and is Design's text in the ruled slot). **No lesson sets `safety_note` at all.** Uncovered: `building-and-measuring-a-circuit` is the unit's **practical** lesson, teaches building circuits from a diagram, has a bench state the page itself calls *"a dangerous current pours through the meter"* and a fault table instructing *"Open the switch at once"*; `series-and-parallel` puts 230 V house wiring, sockets, fuse boxes and breakers in front of Year 8; `current-at-a-junction`'s rung 4 is a domestic overload totalling 20.3 A on a 13 A lead; `potential-difference` names 230 V mains and a 400 kV line. **The distribution is the point:** the one lesson that has a line is the classification lesson, and the one that runs the practical does not — the shape of an oversight rather than a policy. **Flagged, not drafted.** → §6. *Mide sign-off; small once ruled.*

**S3**
- **P8-16** · `potential-difference` · when the second component is "A second lamp", the composed note calls **both** components "the lamp", so it cannot distinguish them and the note at the second lamp is character-for-character identical to the note at the first. **Moving the voltmeter — the one thing this bench exists to let you do — produces no change in the sentence that explains the reading.** In the across-the-battery state it yields *"1.50 V across the lamp and 1.50 V across the lamp"*. The tile and the alt text both resolve it correctly, so the engine has the information. → Resolve the name per **slot** (first/second) rather than per component type, and use the *other* component's name in the "other share" clause. The tile is the model. *Code; small.*
- **P8-17** · `conductors-and-insulators` — raw JavaScript exponential notation reaches students at three reachable states: **`1.2e-7`**, `3e-12`, `3e-13`, in *"120.0 nA ÷ 1 000 000 000 = 1.2e-7 A"* and *"R = 6.0 V ÷ 1.2e-7 A"* — machine output, not mathematics, in the one panel the student is told to check their own work against. → Format as decimals or proper standard form with a superscript. **A build-time assertion that no student-facing text node matches `/\de[-+]?\d/` would close the class across the estate.** *Code; small.*
- **P8-18** · four of seven lessons · the comparison table at 390px scrolls inside its own `overflow-x:auto` wrapper — the right containment choice, and the document never scrolls sideways — but the wrapper carries **no `tabindex="0"` and no `role="region"`**, and the tables contain no focusable content, so **there is nothing for the keyboard to focus and no way to scroll the container from the keyboard** (WCAG 2.1.1). A keyboard-only student can read the "Series" column and never reach "Parallel". No visual affordance either, which is why persona 1 found the second column by accident. → `tabindex="0"`, `role="region"` and an `aria-label` in the **shared renderer** that emits `.ks3-cband-scroll`, so every scrollable table in both key stages gets it at once; plus a fading right edge or "scroll →" cue. *Code — shared renderer, fixes the class estate-wide; small.*

**S4**
- **P8-21** · the log-scale figure's caption says *"each mark is a thousand times the one before it"* and **the first step is a hundred** (0.01 Ω → 1 Ω); every other step is a thousand. The **axis geometry is correct** (measured: 49.0 px for the first two-decade gap, 48.7 px per decade after, every bar within a pixel of log₁₀R) — a false caption over an honest drawing, which is the reverse of the usual failure and much cheaper to fix. It matters because the figure's own instruction is *"Read the gaps, not the bar lengths"*. → Relabel the first tick 0.001 Ω and move it half a decade left, or reword the caption to admit the first step. Copper at 0.05 Ω sits comfortably above 0.001 either way. *Code; flag the relabel to Design if the tick spacing is hers; small.*
- **P8-22** · `current-at-a-junction` · the formula support list defines I, a and b and **introduces `c` in the equation without ever defining it** — and it is not decorative: rung 1 is a three-branch junction, so the three-branch form is the one the student must use and `c` is the one symbol they were not given. The two-branch form the bar model teaches (I = a + b) is never written in the support list at all. → Add the missing line and lead with the form the bar teaches. *Code; small.*
- **P8-23** · Convert-line formatting — the composed lines write *"There are **1 000** milliamps in an amp"* (thin space) while the fixed worked examples one screen above write **1000**; and significant figures are dropped in the conversion (*"200.0 mA ÷ 1 000 = 0.2 A"*, four figures to one) on a page otherwise careful about precision. → One thousands convention across the component, and carry the significant figures through. *Code; small.*
- **P8-24** · `current-and-circuits` · **"filament"** appears in a rung-4 criterion the student must satisfy and is never glossed before `resistance`, five lessons later. A Year 8 who does not know it cannot self-mark honestly — and the word carries the answer, since "broken filament" is the whole explanation of why one dead fairy light kills the string. → Gloss once in the rung-4 **stem**: *"its filament, the thin wire inside that glows, has broken."* *Code; small.*

---

### P9 · Static electricity · 3 lessons · **17 findings** (S1 3 · S2 7 · S3 0 · S4 7)
*In §4: P9-18 → SYS-3 · P9-19 → SYS-2. **P9-2 was filed S1 and is downgraded to S2 by adjudication XU-2** (below).*

> **XU-2 · Adjudication — P9 vs P8 on what an insulator does · S1 → S2.**
> P9's record raises P9-2 as S1, stating that P9 lesson 1's insulator vocabulary *"states P8's registered misconception `CIRC-21` verbatim"*. Resolved against the national curriculum, both positions recorded.
> **P8's `CIRC-21`:** *"An insulator blocks electricity completely — absolutely nothing gets through."* P8 confronts it well and the confrontation is served: *"Not quite nothing. Put 6 V across a plastic ruler and a current does flow: about three millionths of a millionth of an amp… which is exactly why we call the plastic an insulator — but the word describes **how little, not none**."*
> **What P9 actually says:** *"It only works with insulators, because a conductor lets the charge escape"*; *"a conductor would let the charge run straight back or away to earth through your hand"*; and ladder criterion 5, *"…because plastic is an insulator and **the charge cannot travel** along it to the wire."*
> **Resolution.** P9 does **not** state `CIRC-21` verbatim, and that claim is not supported — none of its sentences asserts that nothing gets through. What is real is narrower and still worth fixing: **the ladder criterion credits an absolute "cannot travel"** where P8, taught two half-terms earlier, has explicitly taught "how little, not none". **The physics in P9's context is defensible**: at electrostatic scale on a plastic bottle charge genuinely does not migrate fast enough to earth — that is precisely why static persists on insulators — and P8's nuance concerns ~3 × 10⁻¹² A, negligible by any classroom measure. So this is a **consistency of language** defect, not a science error. **Severity S2.**
> **Proposed solution:** soften criterion 5 to *"…because the charge cannot travel along it fast enough to reach the wire"* — true at both scales, four words — and optionally one clause naming P8's "how little, not none" so the two lessons visibly agree. *Code; small.*
> P9's other three S1s are unaffected and stand as recorded.

**S1**
- **P9-1** · `charging-by-rubbing` · triboelectric ladder — **the ladder ranks Acetate strip at 5, below Wool duster at 3**, in the "gains electrons" band beside polythene and PVC. The lesson's own rule then makes an acetate strip rubbed with a woollen duster come out **negative**, and the bench prints it as a definite result (wool +7.3 nC, acetate −7.3 nC). **This is the opposite of the standard UK school result.** Cellulose-acetate strips are stocked in every prep room *precisely because* they charge **positively** when rubbed with a duster — which is why the polythene/acetate pair is the canonical way to demonstrate the two signs of charge from one cloth. A teacher who runs the demonstration this page describes gets a flat contradiction; a student carries a wrong sign into GCSE, where acetate-vs-polythene is a routine contrast. **This is the C9-5 failure mode exactly: no bench state, gate, rung or build gate exposes it, because every derived quantity is internally consistent around the wrong rank — the wrong model works perfectly.** The lesson's hedge does not cover it (*Going further* calls the list "a reliable guide for glass, polythene and PVC, and a rough one in the middle" — which neither names acetate as unreliable nor licenses reversing the canonical school pair). → Re-rank acetate **above** wool: **1 Human hair · 2 Glass rod · 3 Acetate strip · 4 Wool duster · 5 Cotton cloth · 6 Polythene rod · 7 PVC pipe**. Then acetate + duster → positive (correct), polythene + duster → negative (unchanged), glass + wool → glass positive (rung 1 unchanged). Two consequential edits: move the *"middling"* tell from row 4 to **cotton at row 5** (where *Going further* already puts it), and change the badge split from Design's 3/1/3 to **4 loses / 1 middle / 2 gains**, because wool badged as a gainer would be wrong and it is the duster in the headline demonstration. **No authored sentence quotes a rank number or an electron count**, so every note, tile and rung stays true after the rebuild. *Code + **Mide sign-off** (science content); note to Design for the badge split; small.*
- **P9-9** · `forces-between-charges` · induced states, plus hook reveal, key fact, key note, vocabulary and rung-3 criteria — induction is explained with a **sign-agnostic verb** at six of the eight places the lesson describes it: the charged object *"pushes the neutral one's own charges along"*. Two things go wrong. It **un-learns lesson 1**, which establishes over four paragraphs that only electrons move and nothing positive is ever moved (`CHRG-02`) — "pushes its charges to one side" invites exactly the two-way picture L1 exists to prevent. And at half the reachable bench states the verb is simply wrong: when the charged sphere is **positive** the near face turns negative because electrons are **pulled towards** it. The drawing is right and the sentence describing it is not. The two sites that name electrons get it exactly right, which shows the fix is already written on the page. → Name electrons everywhere and let the verb follow the sign — branch the bench clause as the wiring already branches `{nearsign}`/`{farsign}`. In the six prose sites the minimum edit is "charges" → "electrons" (the balloon and rod are negative in every worked example, so *push* stays correct). **Rung 3's criterion should say electrons too**, so a student who writes the right mechanism is credited. *Code + Mide sign-off; small.*
- **P9-14** · `electric-fields` · dipole direction tile — the sub-caption is a fixed string for the whole arrangement — *"from the positive charge towards the negative one"* — while the reading above it is computed. **Outside the pair the two contradict each other in the same tile**: at step 0 the tile reads *"to the left"* with that sub-caption beneath, and the negative charge is on the right. True at roughly half the slider's reachable positions (steps 0–5 and 19–24). The note beside it is scrupulous where the tile is not (*"every arrow **in the middle** runs from the positive towards the negative"*). On the lesson whose examinable skill is reading a field's direction, **a caption asserting that field arrows run + → − everywhere teaches a false general rule** — one GCSE will penalise the first time a candidate meets a point outside a pair. The other three arrangements' sub-captions are true at every position, so the dipole is the single outlier. → Split the dipole branch by region, the way the two-positives arrangement is already split from its null point: between the charges as now; left of the positive, *"away from the positive charge"*; right of the negative, *"towards the negative charge"*. All three are in the lesson's existing vocabulary and the branch machinery already exists. *Code + Mide sign-off; small.*

**S2**
- **P9-2** · `charging-by-rubbing` — *"A material charge cannot travel through."* → **See XU-2 above.** ⊕ **Materially corrected by the cold double-check, 28 Aug 2026.** This entry was filed against the **vocabulary card "insulator"** and asserted that *"the defect is confined to the card, which is the one place a child re-reads"*. **That is false, and this report contains the measurement that refutes it.** Per SYS-V, physics renders vocabulary flip cards on exactly one page — `describing-motion/speed` — and `charging-by-rubbing` authors no `keyword` block. Verified: `ks3-keyword` occurs **0** times on the served page, and the string "A material charge cannot travel through" appears **nowhere** in the served HTML. **No student has ever read this card.** What *is* served, and is the real defect, is the **ladder criterion** on the same page — *"…because plastic is an insulator and **the charge cannot travel** along it to the wire"* — which XU-2's resolution and proposed fix already correctly target. So: **fix the criterion** (XU-2's four words, *"cannot travel along it fast enough to reach the wire"*). The card is one of the 236 stranded physics definitions, and rewording it is **contingent on SYS-V being wired**, not independently useful. The repo-wide check of every KS3 `insulator` card against P8's definition is still worth doing and should be scheduled with SYS-V. **The S2 severity is confirmed correct** — on the served evidence alone it is, if anything, generous. *Code + Mide sign-off; small.*
- **P9-3** · all three lessons · **every P9 bench gate asks a real question with a real authored answer, and the answer is never used.** `_gate()` never emits the `answer` index and `p9Gate()` reveals the body on *any* press: no option marked, none disabled, no feedback. The authored answers (1, 2, 1) are dead keys. It bites hardest on **L1**, whose gate answer is the same-material null result — a state the bench does not open on and that a student who believes "polythene always ends up negative" has no reason to visit. → Emit the answer index and have `p9Gate` do what the ladder already does: mark the pressed option, reveal the correct one, then open the body — the commitment is still not blocked, merely *acknowledged*. Minimum if marking is unwanted: echo the commitment above the bench and open L1 and L3 in the state that answers their own gate, so the instrument does the correcting. *Code; small (medium if opening states change).*
- **P9-4** · `charging-by-rubbing` · the bench drawing — when both hands hold the same material the two blocks are drawn **completely empty** with "0.0 nC" in each, and **there is no "before rubbing" state anywhere on the page**. So the only picture a student ever gets of a *neutral* object is an empty box, on a page whose second sentence is *"in a neutral object the two exactly balance"*. The drawing vouches for "neutral = nothing there", which is the exact gap `CHRG-02` lives in: if a neutral object contains nothing, a positive object must have had something positive **added**. The unit already holds the right pattern one lesson later — L2 draws the neutral sphere's induced − and + *"so its total is visibly still zero"*. → **Design brief:** draw a neutral block as a balanced pair (faint interleaved + and −) and the charged states as that same set plus the net imbalance, so a student can see the + marks were there all along. Cheaper alternative: one fixed caption inside the frame saying an unmarked block is balanced, not empty. *Design brief → Code; Mide sign-off on the drawn science; medium (redraw) / small (caption).*
- **P9-10** · `forces-between-charges` · the nine-case matrix at 390px — the lesson's payoff figure and the rail's third stop is 620px inside a 314px scroller, so a student sees the row headers, all of "Positive" and a third of "Neutral"; **the third column is entirely invisible**, with no scrollbar, no edge fade, no hint. The closing rule the whole lesson builds to — *"Attraction proves nothing… only repulsion is proof"* — is only defensible if you have seen that **four of the nine cells are induction**, which lives in the columns you cannot see. → A right-edge gradient fade below ~480px (one rule in `ks3.css`) — the standard cue, and it should land first. Better if Design will take it: restack the 3×3 as three labelled groups below ~480px. *Code (fade) / **Design brief** (restack); small / medium.*
- **P9-11** · `forces-between-charges` · force arrows — an undeclared floor of 22 units means the arrow barely moves across the induced case's whole range: **strength falls 625× from 4 cm to 20 cm and the arrow falls 27%**, while the lesson's own note at that state says the induced pull *"dies away faster still as you separate them"*. At the edge the strength tile reads *"far too weak to see"* beside two clearly drawn arrows, and the `aria-label` says *"pulled together, weakly"* — **three channels giving three accounts of one state.** → Declare the clamp in the convention note (in L3's own words), make the band word and the drawing agree at the bottom of the range (dashed or hairline, or drop the arrow), and feed the computed band word into the `aria-label` instead of the literal "weakly". **Extend the SYS-5 guard: a rendered "far too weak to see" must not accompany a full-length arrow.** *Code; drawn treatment past Design; small.*
- **P9-16** · all three lessons — **the unit is called *Static electricity* and never defines "static".** The word appears four times in body text and is glossed nowhere; it is absent from all three vocabulary lists. With it goes the join to P8: this unit sits directly after seven lessons of *current*, declares one of them as its prerequisite, and **never says the sentence that separates them** — that static electricity is charge that **stays put** while a current is charge **on the move**. A Year 8 arrives with one word, "electricity", covering both, and the unit never takes it apart. (To its credit the unit never gets this *wrong*: a full sweep for "flow", "current", "travel", "escape" and "runs away" found no sentence implying static flows. **The problem is silence, not error.**) → Add a vocabulary card to L1 and one clause in its first explainer joining it to P8: *"you met charges moving round a circuit as a current; here they are separated and stay put, which is where the word *static* comes from."* **That is the sentence that makes P8 and P9 one course rather than two.** *Code + Mide sign-off; small.*
- **P9-17** · all three lessons · **all three hooks put the correct answer at option A.** MRB-278 reaches the two marked rungs on each page and the three bench gates happen to vary; the hooks are outside its reach and all three sit at index 0. A student who notices after two lessons does not genuinely commit on the third — and **the source itself states why that matters, twice**: *"a student who spots the answer never commits, and a belief nobody commits to cannot be confronted."* → SYS-8. (The gate case only becomes meaningful once P9-3 is fixed and the gate answer is used.) *Code; small / medium.*

**S4**
- **P9-5** · the shared sentence helper title-cases after lower-casing, turning the acronym into **"Pvc"** — two inches under a tab reading "PVC" and a caption reading "PVC PIPE". The `aria-label` has it in lower case. → Carry a `sentence_name` per material, or exempt fully upper-case tokens from the lower-casing pass — **the second is the general fix and protects every future acronym in the key stage.** *Code; small.*
- **P9-6** · the row of charge marks is capped at six, so **above ~19.5 nC the drawing stops responding while the tiles keep climbing** (hair/PVC reads +22.0 nC at 8 strokes and +38.4 nC at 20 with an identical path). The cap is Design's deliberate choice and the count lives in the tile; the defect is that nothing says so, while the convention note is otherwise scrupulous about declaring exactly this class of thing — and L3's note declares its own arrow clamp in one clause. → One clause in L1's `convention_note`. No drawing change. *Code; small.*
- **P9-7** · end-matter — the prerequisite is declared as P8's **`building-and-measuring-a-circuit`** (ammeters, voltmeters, building a circuit), none of which this lesson uses, while the lesson it actually needs (`conductors-and-insulators`) is filed two headings lower as a see-also. **A student who is stuck and clicks "Before this lesson" is sent to the one P8 lesson that cannot help.** `requires` appears to be carrying "the lesson immediately before this one" — which is already shown as "Previous:" — rather than "what you need to know". → Swap them. If `requires` is *deliberately* the skeleton predecessor, then the **heading** "Before this lesson" is what should change, key-stage-wide → §6. *Code; **Mide ruling** if the current use is intended; small.*
- **P9-8** · the rail — one press of the bench gate ticks stop **3 (THINK)** while stop 2 is still open, so the rail reads done · not-done · done and the counter jumps by completing a section the student has not scrolled to. `#s-think` is the misconception block; marking it complete before a word has been seen is the rail making a false claim about the student. **Faithfully ported** — Design's own `DONE` reads `if (id === 's-think') return s.gate !== null;` — so it is a design question, not a code defect. → §6 (it recurs on P11 and P12). *Mide ruling, then Code; small.*
- **P9-12** · `forces-between-charges` GCSE card promises *"Electric field lines and **their direction**"* as future material, and **the very next lesson, one click away, teaches field direction at KS3 and makes it a key fact.** Stale in the C8-15 form. (The inverse-square half is accurate and stays.) → Trim to the half that is true and hand the other half to the lesson that owns it. *Code; small.*
- **P9-13** · the drawn separation is not proportional to its own label: doubling 4 cm to 8 cm grows the drawn gap by **1.84×, not 2×**, and the lesson's central quantitative claim is about doubling the separation. The convention note declares a great deal and not this. → `gap = 700 × (d / 20)` puts 4 cm at 140 units and still leaves 44 units clear between the two spheres, so nothing overlaps at any reachable separation. *Code; geometry past Design; small.*
- **P9-15** · `electric-fields` · the gravitational-field card — *"Always a pull, never a push, **which is why** there is no opposite of mass"* inverts the causation: there is only one kind of mass, *which is why* gravity can only attract. A student asked why there is no negative mass has been handed "because gravity always pulls", which explains nothing. It matters slightly more than usual because the card's whole job is to line charge up against gravity, and the point about charge is that it comes in **two** kinds. → Turn the clause round. Same length, and it explains rather than asserts. *Code; small.*

---

### P10 · Magnetism and electromagnetism · 5 lessons · **26 findings** (S1 5 · S2 7 · S3 1 · S4 13)
*In §4: P10-24 → SYS-2 · P10-25 → SYS-3 (and it was P10's auditor who diagnosed the box-test false negative before it was found elsewhere). **P10 measured SYS-8 ABSENT in its own corpora** — the one unit that does. It is also the unit carrying the heaviest reading load (SYS-R) and the newest, built 25 Aug with the least classroom exposure.*

**S1**
- **P10-22** · `how-a-motor-works` · the coil bench — **the bench draws the force on each side of the coil along exactly the same line as the current in it.** The loop is a flat rectangle in the plane of the page; the current arrows run vertically in that plane; the force arrows run vertically in the same plane, starting at each member's midpoint, **so the red force arrow is drawn on top of the blue current arrow and points the same way**; and the field is three horizontal lines, also in the plane. All three quantities coplanar and two collinear — physically impossible, since **F = I L × B** is perpendicular to both, **and the lesson's own first explainer says so in its first sentence**: *"the wire is pushed sideways — at right angles both to the field and to the current. **This is the one new fact the whole lesson rests on.**"* What a student reads instead is "the current pushes the wire the way it is flowing" — a new misconception, adjacent to `MAG-17`, which the page's think-again exists to kill. **The drawing is nearly the correct one already:** the axle is drawn as a **circle**, meaning we are looking along it, and the rotation arc is in the plane of the page, which is right for that view. Flattening the two current-carrying sides into a rectangle is what lost the perpendicularity. → Draw the end-on view the axle pin already implies: replace the two vertical members with **two circles** carrying ⊙ and ⊗ (swapping when the current reverses), with a small key; keep the field horizontal and the force arrows vertical exactly as they are; keep the loop's top and bottom as a faint outline round the back. Everything downstream is then true as written and the reversal arithmetic is untouched. **Also amend the bench lead, which says "The coil is drawn face on"** — in the fixed drawing it is drawn end on, and saying so is the sentence that makes the picture readable. *Design brief → Code; **Mide sign-off** on the redrawn science; medium.*
- **P10-6** · `magnetic-fields` · the crowding tile — the tile that teaches crowding draws **five lines on the STRONG side and three on the WEAK side**. What a student can count is a different *number* of lines, which is **`MAG-08` exactly**, the misconception this page mints — and which this page's own rung-1 feedback refutes in terms: *"Every line that leaves the north pole arrives at the south pole, so the count is the same everywhere. What differs is how much space they are spread over."* The drawing shows the count differing and the space barely differing (48 px against 56 px). **The drawer's own comment says the two groups "differ only in how much room the same marks are given" — and the code draws five and three.** → Draw the **same number of lines in both groups** (five and five) and let spacing carry the whole difference: 8 px pitch on the left, 24 px on the right. Better still, one continuous fan converging into a bundle at one end — which is what a real map does and removes the two-boxes reading entirely. *Design brief → Code; small.*
- **P10-7** · `magnetic-fields` · the compass grid — the `on_magnet` branch exists to say that a field map is drawn for the space **around** a magnet and that the lines inside run the other way. It fires only within 10 px of a **point pole**, while the magnet is *drawn* as a rectangle spanning the whole bar — so in **11 of 100 states the compass dial is drawn sitting visibly on the magnet body and the bench prints a full reading**: at the dead centre of the drawn magnet it reports **270°, "west on the page"**, the exact opposite of what the bench's own `on_magnet` note tells students the field inside a magnet does. → Make the no-reading test the **drawn bar**, not the point poles (`x1 ≤ x ≤ x2` and `|y − b.y| ≤ 34`), keeping the pole-proximity test as well. Three lines in `paint()`; the count of no-reading states rises from 4 to 15, all honest, and every one then carries the inside-runs-the-other-way sentence. *Code; small.*
- **P10-8** · `magnetic-fields` · the N-facing-S setup note — printed at all 25 of that setup's states: *"…the lines run straight across the gap from one to the other, **which is why that gap is the strongest part of the whole map**."* On this bench the gap is the **weakest** interesting part: the compass in the middle reads **9.5** on the bench's own 0–100 scale against **100.0** at the pole faces, and ten of twenty-three readable spots beat it. The claim is true of two magnets whose pole faces are *close*; this layout's gap is 300 units across with 220-unit magnets, so the model refuses it. A student who reads the sentence and does the obvious thing is contradicted by the instrument in the same breath. → (a) Change the sentence to what the bench shows (*"…and they are strongest right at the two pole faces, thinning out towards the middle of a gap this wide"*); or (b) narrow the geometry so the sentence becomes true, which also makes the layout look like the horseshoe it is contrasted with. **(a) is smaller, (b) is the better lesson.** The other three layout notes were swept and verified true. *Code; small.*
- **P10-11** · `the-earth-is-a-magnet` · the `tipped` branch at the equator — with the compass **free to tip at the equator** the page prints *"…tips over by **0°** from level, with its **north-seeking end down**. That happens because **the field is not parallel to the ground**…"* At the equator the field **is** parallel to the ground — that is what makes the equator the equator, magnetically — the needle tips by nothing, neither end is down, and the drawing correctly shows it dead level. **Four statements wrong at one latitude**, on the page whose bench exists to teach that dip varies with where you stand. It also contradicts the same bench's own `flat_level` branch, which at the *same* latitude says *"at the equator that is the one place where the mounting and the field agree, because the field really is level here."* **The build already found and fixed this hole for the clamped branch — `flat_level` was minted for it — and the free-to-tip branch has the same hole and was not split.** → Mint a `tipped_level` branch reached when `!flat && !atPole && |dip| < 0.5`, and guard the three `deg >= 0` words so `tipword`, `tipend` and the dip sub-line emit nothing rather than "north end down" at zero dip. *Code; small.*

**S2**
- **P10-2** · `magnets-and-poles` · the `nothing_inert` branch covers 72 of 150 states with one fixed sentence, *"One of these is {inert}, and a magnet does nothing at all to aluminium, wood, copper or brass."* In 48 it is exactly right. In the other **24** — steel against aluminium or wood, and their mirrors — **there is no magnet on the track at all**, and the sentence explains the null by the aluminium while the operative reason is that neither object is magnetised. A student trying to work out why nothing happened is handed an answer about a magnet that is not there, and is left with the impression that the steel bar was doing something the aluminium refused. **The bench already owns the correct sentence** in its `nothing_steel` branch; it just is not reached. → Split the branch on whether a magnet is present. One extra key, one extra test. *Code; small.*
- **P10-3** · `magnets-and-poles` · think-again — invites the test at home (*"Take a magnet to a handful of metal objects"*) and names what will respond: *"the steel tin, **the fridge door**, the paper clip, the nail."* Austenitic (18/10) stainless steel is **not** attracted, and it is what cutlery, sinks, most kettles and the fronts of a great many modern fridges are made of. A child who does exactly what the page asks, with the most available "steel" in the house, gets a null result from an object the page has just named — and the conclusions available are that the page is wrong, or that steel is not magnetic after all, which is the misconception the lesson exists to sharpen. **The one place in the unit where a real kitchen contradicts the page.** → Drop the fridge door from the responding list and add the exception as a sentence, because it is genuinely interesting rather than a caveat: *"One steel will surprise you: the shiny stainless steel used for cutlery and sinks has enough nickel and chromium mixed in to stop it responding at all, so a fork can sit on a magnet and do nothing while a nail jumps to it."* *Code, wording past Mide's gate; small.*
- **P10-9** · `magnetic-fields` — two joined halves. **(a)** The fourth readout tile is labelled **"Lines near the compass"** and reports "packed tightly together" / "far apart" — while the drawing beside it **contains no lines at all**, only a 13 × 7 arrow lattice whose spacing is a **constant** 73.3 × 53.3 px in every one of the 100 states. **(b)** The `single` layout note says *"the arrows get shorter and further apart… they crowd in and lengthen"* — the arrows do lengthen and shorten (with √field) but **never crowd or spread**, because they sit on a fixed grid. On the page whose second rule card is "crowded lines mean a strong field", the one instrument that could let a student verify that rule shows uniform spacing and then tells them in words that the spacing changed. → (a) Relabel the tile so it stops describing the picture ("If you drew lines here they would be…") and cut "and further apart" / "and they crowd in" from the note, leaving what the drawing does. (b) The lesson the page actually wants: a **"show the lines" toggle** replacing the lattice with streamlines traced from the same field function, so the crowding rule is verified by the instrument that measures it. **(a) should land regardless, because the note is false as it stands.** *Code (a); Design brief (b); small / medium.*
- **P10-12** · `the-earth-is-a-magnet` · the globe — the drawing gets the lesson's **headline fact right and then makes it unreadable**: the buried bar magnet has its coloured half at the **bottom** (north pole at the geographic south — the correct and unusual thing to draw, and the single most important claim on the page), and **neither half is labelled**. No N, no S, no legend, and nothing else on the page establishes what the colour means (the compass needle beside it is drawn entirely in the same blue). The `aria-label` says only *"a globe with a bar magnet drawn inside it along the spin axis"*. **So a student who has just been told the Arctic pole is a south pole cannot check that against the one picture that proves it.** Two smaller faults in the same drawing: the four field lines carry **no arrowheads** (→ SYS-A), and all four converge on a single point at each pole, which is what "lines crossing" looks like to a student who read the previous lesson's third rule the day before. The unit already labels pole faces on `p10-05`. → Put an **N** on the lower half and an **S** on the upper, in `p10-05`'s treatment, and one caption line: *"the buried magnet's north end is at the geographic south — which is why a compass points the other way."* Separate the four line endpoints a few pixels either side of the pole. *Design brief → Code; small.*
- **P10-13** · `the-earth-is-a-magnet` · the "On the bench beside it" control — two of its three states (**a steel clamp stand**, **a speaker magnet**) change every readout and rotate the drawn needle to a new fixed angle, **while nothing whatever is added to the drawing.** In **22 of 54 states** the student sees a needle at an angle with no visible cause, and the sub-line says *"the needle is on the bench object"*, which is not what has happened either. This is the mirror of the rule the unit's own drawers enforce ("a control that is DRAWN must be MODELLED"): here a control is modelled and not drawn — **and the teaching point (that a compass lies near steel or a magnet, which is why you use one away from loudspeakers and railings) is the one thing on the bench a picture would carry best.** The `aria-label` even names the object that is drawn nowhere. → Draw it: a small labelled rectangle or disc at the end of the level line the needle turns towards (the needle already turns to a predictable angle for each). Three short paths and one fill span. Reword `on_bench` to *"the needle has turned to the bench object"*. *Design brief → Code; small.*
- **P10-18** · `electromagnets` · the drawn field — the energised coil's field is **two arcs over the top and nothing else**: no line through the bore, nothing below the coil, no arrowheads. The explainer three paragraphs above says *"inside the coil they all point the same way, so the fields stack up"*, and the key fact says the coil's field "is the same shape as a bar magnet's" — which is closed loops above and below with the field running through the body. **A student asked where an electromagnet is strongest has a picture in which the middle of the coil is empty.** → Mirror the two arcs below the coil and add straight segments through the bore from S to N so the loops close and the interior is where the lines are densest. Arrowheads with SYS-A. Contained in one path string. *Design brief → Code; small.*
- **P10-27** · `magnetic-fields` against P4 and P9 · **the estate carries two different definitions of its most important shared word, and P10 uses the one the other two do not.** P4: a field is *"what a magnet, a charge or a mass does to the space around it"*; P9: *"the state a charged object puts the space around it into"*, with a card saying explicitly that every non-contact force is described this way. P10: *"the region around a magnet where another magnet would feel a force."* P4 and P9 define a field as a **state the first object creates**; P10 as a **region where a force would be felt**. Both are defensible and P10's is AQA's own wording — so this is consistency, not error — but P10 is the unit where "field" is the headline noun, it lists P9's lesson in its `references`, and it never picks up P9's framing. **In the same seam: P10 never names magnetism as a non-contact force**, though P4 names it as one of exactly three and P9 puts it beside gravity and charge on a comparison card (grep of all five P10 pages for "non-contact" / "at a distance": zero). → Keep P10's region wording (it is what a student meets at GCSE) and add one sentence to `p10-02`'s first explainer joining it to what P9 taught and naming the term. Whether P4 and P9 should also converge on one definition is a bigger call and belongs in one estate-wide ticket. *Code; small.*

**S3**
- **P10-1** · three lessons · **every caption drawn inside a bench SVG is set at a fixed 15px in a 1000 × 400 user space, so it scales with the drawing**: 17px at 1280, **5px at 390** — a smear, on the device half the audience uses. Five captions affected, two of them load-bearing: *"SEEN FROM THE SIDE, LOOKING WEST"* is the only thing telling a student which way they are looking at the dip circle, and *"PAPER CLIPS HANGING FROM THE END"* is the only thing naming what the row of marks is. **The HTML overlay fills on the same drawings do not have this problem** — they carry `font-size: clamp(9px, 1.3vw, 15px)` — so the fix already exists in the same file, one class away. → Give the three caption classes a viewport-floored size (emitted as an HTML overlay span, or `style="font-size:clamp(11px,1.6vw,15px)"` on the `<text>` so it stops inheriting the SVG's scale). **Add caption height to the 390 sweep** so the class cannot ship again. *Code; small.*

**S4**
- **P10-4** · `electromagnet` is used in lesson 1's think-again and is not taught until lesson 4 — **breaking the unit's own explicit authoring rule** that every P10 lesson teaches from nothing because a school may run the unit in any order (lesson 1 has `requires: []` and `assumes: []`). → Gloss in place, or use the plain word: the point being made is about steel versus aluminium, not about switching. *Code; small.*
- **P10-5** · all three `nothing_*` branches share one sub-line, *"no magnet acting on a magnetic material"* — which parses two ways (and a Year 9 reads the wrong one first, because the tile above says "do nothing"), and is **inaccurate for two of the three branches it covers**: for steel-against-steel there *is* a magnetic material, twice over. → Give each branch its own sub-line, as the note already does. Three strings, no wiring change. *Code; small.*
- **P10-10** · four lessons · **field lines drawn without arrowheads** — this page makes the arrow a rule (*"The arrow is the way a compass points"*, and a marked rung-3 criterion), and of the four places a field line is drawn only one carries a head: the crowd tile's eight lines have none, the readings tile's needles have no marked north end, `p10-03`'s globe draws four Earth field lines with no arrows **on the lesson whose whole subject is which way that field runs**, and `p10-04`'s solenoid arcs have none. The bench lattice *does* carry heads, **so a student meets both conventions on one page.** → SYS-A, plus a marked north end on the readings needles. Leave the "no-cross" tile's ghost lines unarrowed — they are deliberately impossible. *Design brief → Code; small.*
- **P10-14** · in the two captured branches three of four tiles correctly say the Earth has been overruled and **the fourth carries on reporting the Earth's horizontal component under the label "Sideways pull to work with"** — 61.6 at 52° N with the speaker magnet, a true fact about the place and emphatically not what the needle is working with. 22 of 54 states. The label is the problem, not the number. → Reclaim it with a sub-line (*"the Earth's, but the bench is winning here"*) or suppress the value. *Code; small.*
- **P10-15** · gate option B is *"It spins round and round, because every direction is south"* and is not the marked answer — and the bench's `flat_at_pole` note then prints, as plain truth, *"Every direction from here is south, and a compass has run out of anything to say"*, alongside "settles nowhere" and "it drifts". **A student who committed to B is handed the second half of their own sentence back as correct**, with the first half described in words close enough that nothing tells them they were wrong. The free-to-tip pole state confronts it properly, but that is a different control setting and the gate carries no feedback. → One clause naming the difference: *"It does not spin — there is simply nothing pulling it round, so it drifts and stops wherever it happens to be."* Confronts the belief at the state that elicits it, which is the pattern the rest of the unit uses. *Code; small.*
- **P10-16** · two latitude labels name a country the latitude does not cross: **20° N "southern Egypt"** (Egypt's southern border is the 22nd parallel; 20° N is Sudan, ~220 km outside) and **40° S "southern New Zealand"** (40° S crosses the lower **North** Island). Both are read by every student who moves the slider, and the unit's geography is right everywhere else. → Change the **name**, not the degree — changing the degree would shift the dip and pull figures. *Code; small.*
- **P10-17** · *"above a few hundred **degrees** a magnet loses its magnetism"* — no unit, on a page whose very next section prints "69°" of arc. → "degrees Celsius". (The claim is right: neodymium ~310 °C, iron 770 °C.) *Code; small.*
- **P10-19** · one of the bench's four readout tiles carries the same value in **every state it can reach** ("a north pole" ×75, "not a pole" ×75) — a restatement of the switch occupying a quarter of the readout row. Meanwhile the page asserts **three times** that the poles can be swapped, and **the bench has no control that reverses the current**, so the claim is asserted three times and demonstrable zero times (the student first sees it happen one lesson later). → Add a two-state "Which way the current goes" picker (`p10-05`'s `dirs` control is the model), flip the pole readout and the fill spans with it, and reverse the arrowheads once SYS-A lands. Or cut the tile and use the space for the turn count (P10-20). *Code; small.*
- **P10-20** · the coil is drawn as **eight loops at every setting** while the **current** *is* visible in the picture (the stroke width grows with it) — so of the two independent variables the bench exists to separate, one is drawn and the other is not. That asymmetry sits directly on **`MAG-14`**, the belief that turns and current are the same variable. The legal line discloses the eight loops, so this is a disclosed limitation rather than a lie — disclosed in the place least likely to be read. → Draw 4 / 6 / 8 / 12 / 16 loops over the same core length so the loops visibly crowd as turns rise; keep the legal line, amended to say the count is indicative. *Design brief → Code; small.*
- **P10-21** · the figure is headed *"Four jobs only a switchable magnet can do"* and three tiles are exactly that; **the fourth is a loudspeaker**, which is not an electromagnet attracting anything — it is the **motor effect**, the whole subject of the next lesson, untaught. It also collides mildly with `p10-03`, where "a speaker magnet" is the *permanent* magnet that overrules the Earth. → Swap it for a genuine switching job (an electric bell's make-and-break is the classic KS3 example), **or** keep it and make it the forward reference it already is: *"…A changing current makes a changing push on the coil, and the cone moves with it. That push is the next lesson."* The second is better teaching and costs one clause. *Code; small.*
- **P10-23** · `how-a-motor-works` — **there is no visible circuit on the motor bench.** No battery or supply is drawn (`p10-04`'s bench draws one, with a switch), and the two leads run **in the same tone as the field lines, at exactly the same y as the middle field line, from the face of each magnet to the coil** — so on screen they are indistinguishable from the field line they lie on, and the readings available to a student are "there are no wires" or "the current comes out of the magnets". And the figure directly below names **"The brushes — fixed contacts that press on the split ring"** as one of the four parts of a motor, while the bench draws **no brushes at all**: the split ring is there, correctly split, with nothing touching it. Three of four named parts are on the drawing. → Route the circuit where a circuit goes (down and round), draw a cell symbol as `p10-04` does, draw two brushes pressing on the ring, and give `.ks3-mcoil-lead` a tone distinct from `.ks3-mcoil-field` so a wire never reads as a field line. Travels with P10-22. *Design brief → Code; small.*
- **P10-26** · all five lessons · **amber as the "selected" state** — on the dark bench blocks the SELECTED state of every segmented control is painted with `var(--ks3-alert)`, the design system's **warning/loss** channel, on five controls per bench and up to four benches per page. Nothing has gone wrong when a student picks "Free to tip", and a student who has learnt the amber convention elsewhere reads a chosen setting as a flagged one. Shared rule, so estate-wide. **The P10 build commit records that P10 originally carried a per-unit override, that it was removed on 25 Aug to keep one control behaving one way on 199 pages, and that "the amber-as-selection question is raised as a finding by all three units" of that run.** → §6 — unresolved rather than ruled, and three units have now stopped at it. *Mide ruling, then Code; small once ruled.*
- **P10-28** · two consecutive lessons use **"core"** for two different things and neither flags it: `p10-03` for the Earth's core (four times, including *"far too hot"* to be magnetised) and `p10-04` as a vocabulary term meaning *"whatever sits down the middle of a coil"*, used about thirty times. A student who reads them a day apart meets "a soft iron core" the day after being told the Earth's iron core is too hot to hold magnetism. **The collision is one clause from being an asset** — both are iron; one is too hot to hold magnetism, the other is chosen because it does not. → One clause at first use in `p10-04`. *Code; small.*

---

### P11 · Matter and the particle model · 4 lessons · **23 findings** (S1 5 · S2 9 · S3 2 · S4 7)
*In §4: P11-15 → XU-1 · P11-24 → SYS-2. P11's SYS-3 probe was **struck** (box test) — `temperature-and-internal-energy` is the **worst page in the estate** at +124px. P11 also carries the estate's heaviest bank length tell (56.2% longest-is-correct) and its heaviest extremal tell (70.8%).*
*P11 was additionally probed against chemistry C1's known defects: **C1-08, C1-01, C1-09 and C1-14 are all NOT PRESENT.** P11 and C1 agree on every claim tested except one gap (P11-14).*

**S1**
- **P11-09** · `brownian-motion` · the jiggle bar — **the jiggle is computed with no reference to the speck at all** (`jig = 2.5 * k`, where `k` is only the temperature root). A pollen grain (100,000× a molecule) and a fat droplet in milk (3,000×) both report **2.5 µm per second** at 20 °C. The bar sits directly beneath a bar announcing the size ratio and directly beneath a paragraph reading *"This is why the speck has to be the right size. Something as small as a molecule would be knocked clean across the cell; something as large as a grain of sand is struck so evenly that the imbalance is nothing."* **The instrument then demonstrates that size makes no difference whatever** — the protocol's own worst case, and the model it teaches is the one the lesson exists to install. Real Brownian displacement goes as r^(−1/2) (Stokes–Einstein): a 30 µm pollen grain wanders 5–6× less than a 1 µm smoke speck, which is why Brown needed a good microscope and why schools use smoke cells. → Make the jiggle depend on the tab, which the payload already carries the data for: keep smoke as the reference at 2.5 µm/s and scale by √(ratio), giving pollen ≈ 0.6, dust ≈ 0.8, milk fat ≈ 3.2 — right to within the "illustrative displacement rate" the convention note already claims, one line of code, and it turns the size bar into **evidence for** the paragraph beside it. Plus one clause in the note. **Minimum honest repair if the derivation is thought too much: remove the jiggle figure from the per-tab display entirely** — a constant presented as a measurement of the selected speck is a false reading. *Code + Mide sign-off; small.*
- **P11-18** · `why-ice-floats` · the verdict card, **every tab** — the card prints, verbatim, the misconception the page is built to destroy: *"floats / **solid is the lighter of the two**"* and *"sinks / solid is the heavier of the two"*. Inches above, the hook's wrong option A is *"Ice is lighter than water, because it is frozen"*; inches below, the think-again opens with *"Ice floats because it is lighter than water"* and answers *"**What matters is not the weight of the object but its density**"*. `PART-20` is that exact sentence. **So the instrument — which a student trusts over prose, and which is the thing they actually operate — vouches for the belief the page marks wrong twice.** Lesson 1's bench gets this right by being careful ("a cubic centimetre of it is heavier than the cubic centimetre of water it would have to push out of the way"); here the qualification is gone and "lighter"/"heavier" stand bare. → Replace the two strings: *"the solid is the LESS DENSE of the two"* / *"the solid is the DENSER of the two"*. Every word is then one the page has defined, and the readout becomes the confrontation instead of the counter-example. *Code + **Mide sign-off** (wording on a marked misconception); small.*
- **P11-02** · `density` · bench sub-line **and** Your-turn Q1's Convert step — `p11Mass()` prints a mass ≥ 1000 g in **kilograms** while the density tile's working line always uses **grams**, so at six reachable states the bench reads *"THE BALANCE SAYS 9.65 kg"* beside *"9650.0 ÷ 500"* — a first number that appears on no other tile and carries no unit. **Worse**, the Your-turn refills from the same live state and its Convert step reveals *"9650.0 g stays 9650.0 g… The balance reads grams and the cylinder reads cubic centimetres, so **there is nothing to convert**."* **The balance does not read grams; it reads 9.65 kg** — so the page teaches "nothing to convert" at precisely the state where its own first rule says converting is the first line of the working. Gold at the default 100 cm³ needs no slider move at all. → (a) Add a `mass_g` token that always prints grams *with its unit* and use it in the working line. (b) **Better, and it earns its keep:** branch the Convert line so that when the balance shows kilograms it reads *"9.65 kg × 1000 = 9650 g — the balance is reading kilograms and the cylinder cubic centimetres, so this one DOES need converting."* That turns the defect into the lesson's best teaching moment, and the branch condition is what `p11Mass` already computes. *Code; the new Convert sentence past Mide's science gate; medium.*
- **P11-01** · `density` · Q2's Answer note — *"Insert 0.039 instead of 39 and the bolt comes out **less dense than air**."* 0.039 ÷ 5.0 = 0.0078 g/cm³ against air at ~0.0012 — six and a half times **denser** than air. The sibling note one block above is correct and checkable, which makes this a copy-shaped slip. It is the last sentence of the lesson's last worked step, so it is the line a student finishes on — and the unit gives no density for air anywhere, so nothing lets a student check it and nothing corrects it. → *"…comes out at 0.008 g/cm³ — a hundredth the density of water, which would make a steel bolt float."* *Code + Mide sign-off; small.*
- **P11-13** · `temperature-and-internal-energy` · hook — *"A bath run too hot at **40 °C** will take the skin off you"*, and the reveal's *"the bath would scald you at a quarter of its temperature"*. A normal adult bath is 37–40 °C; 40 °C is what a bath is *supposed* to be. Scalding needs roughly 50 °C and above (which is why water is stored at 60 °C and thermostatic mixers exist). **Every child in the room has had a bath at about this temperature, so this is a claim a real classroom contradicts out loud** — at the opening sentence of the one page where the student most needs persuading that a counter-intuitive comparison is true. The physics does not depend on the exaggeration: a 40 °C bath really does hold ~10⁸ times a spark's internal energy. **The estate already has this calibrated correctly** — P1 runs the same hook and writes it honestly: *"a bath at 40 °C, barely more than body temperature, will make you flinch and can genuinely injure a small child."* → Take P1's calibration, so the two pages agree. *Code + Mide sign-off; small.*

**S2**
- **P11-14** · `temperature-and-internal-energy` · coverage — the lesson owns `KS3.P.EIM.01`, *"changes with temperature in **motion and spacing** of particles"*, covers motion thoroughly and **never mentions spacing at all** (full-text search for "spacing", "further apart", "closer together", "expand", "gaps": nothing). The consequence is bigger than a missing half-statement: ***"heating makes the particles themselves expand"* is the single most-taught-wrong sentence in British lower-school physics, and P11 confronts it nowhere.** The register books it as `PART-03`, re-confronted on `why-ice-floats` — where the only confrontation is a rung-3 self-mark criterion a student sees after typing an answer, which never states the negative. **Chemistry does this superbly** on pages P11 links to but does not restate: C1's *"A water particle in ice and a water particle in steam are identical. Same size, same mass"*, and *"If heating made particles swell, a hot gas would be harder to squash than a cold one. It is not."* A student taking physics but not reading the chemistry pages meets the physics statement about spacing nowhere. → One explainer between the current 1 and 2, doing the missing half of EIM.01 and killing `PART-03` in physics' own voice: *"Warming something does two things: they move faster, and they end up a little further apart, which is why nearly everything expands when it is heated. What does **not** happen is the particles themselves getting bigger. A water particle in a kettle is exactly the same size as one in a fridge."* Then add `PART-03` to this lesson's `misconceptions` and the expansion sentence to the key note. *Code + **Mide sign-off** (new teaching text); medium.*
- **P11-03** · `density` · the bar panel — the bars are honestly proportional and **that is the problem**: gold at 19.30 sets the scale, so oak fills 3.4%, ice 4.8%, water 5.2%, aluminium 14%. Four of six bars are slivers, and the three that matter most — oak, ice, water, which straddle the 1.00 float line the whole of `why-ice-floats` is read against — are **visually identical**. The lead calls it "the density league table"; a league table you cannot read the middle of is not doing its job, and **a student cannot see from it that ice is less dense than water**. → Draw the 1.00 g/cm³ water line as a marked rule across the panel (the ice bench already has the idea with its muted comparison bar), so the four sub-2.70 materials are read against a visible reference rather than against gold's far end; optionally add a second zoomed row for 0–1.5, labelled as a zoom. **Do not switch this panel to a log scale — see P11-16.** *Design brief → Code; medium.*
- **P11-05** · `density` · hook, explainer 2 and rung 2 — the lesson's central move is *"the word people usually reach for is **heavy**, and it is the wrong word"* — **and it never says what the right word is.** *"Heavy is a property of the object; density is a property of the material"* leaves *heavy* standing as if it were a legitimate technical term for the object property. The right word is **mass**, and the page's own vocabulary defines it. Compounding it, the page uses *weigh* and *heavier* for mass throughout (*"They weigh the same, because the balance is level"*) — **and the very next lesson in the taught skeleton is P12 `gravity-and-weight`**, whose whole argument is that weight is a force in newtons and that a pan balance measures mass anywhere. A level balance does not mean two things weigh the same; it means they have the same mass. → One clause in explainer 2 naming **mass**, then let the hook's everyday "heavier" stand as the loose word the reveal corrects, and change the reveal to *"They have the same mass — that is what a level balance means"*, which is the sentence P12 will need a fortnight later. *Code + **Mide sign-off** (wording and the cross-unit call); small.*
- **P11-10** · `brownian-motion` · the temperature slider — the gate makes the student **commit** that warming gets "faster and wilder", and across the slider's full range the jiggle goes **2.4 → 2.7 µm/s: an 11% change over 80 degrees.** The payoff the student was made to predict is, on screen, almost nothing. It is also the wrong scaling for the two water tabs: √T is right for molecular *speed*, but Brownian displacement goes as √(T/η) and water's viscosity falls about fivefold from 0 to 80 °C, so the honest change is roughly **2.5×**, not 1.14×. → Fix with P11-09 in one edit; **keep the molecular-speed bar on the true √T — the two bars moving by *different* amounts is itself the teaching point**, and the note can say so. *Code + Mide sign-off; small.*
- **P11-11** · `brownian-motion` · the bar panel — **three bars in one panel, in one visual language, on three different and undeclared scales, one of them logarithmic.** Speed is linear against 800 m/s, jiggle linear against 4 µm/s, size is `log10(ratio)/5`. So "5,000 × wider" draws at 74% and "100,000 × wider" — twenty times bigger — draws at 100%. **`ks3_art/p11.py` states the panel's own contract in its docstring: *"THE FILL IS THE RATIO THE LABEL CLAIMS… the drawing cannot disagree with the number beside it."*** The size bar breaks it, and at rest all three bars sit at 62.5 / 62.5 / 74%, inviting a child to read three unrelated quantities as comparable. → **The size comparison is not a bar.** Move it into the readout row as a fifth card, where a number carries no implied length, and let the panel hold the two quantities that share a temperature-driven story. If it stays a bar, the caption must declare the scale. *Design brief → Code; small.*
- **P11-16** · `temperature-and-internal-energy` · the bar panel — the panel is logarithmic (a decade per 8.6% of track), so at 40 °C the four bars fill 38.6 / 58.4 / 68.1 / 87.5% and **a child reading bar length reads "a bathful holds roughly twice a teaspoon"** where the truth, stated by the page's own readout card, is **16,000 times**. The lead says *"they are nothing like each other"* and the bars look very much like each other. The mitigation is the caption, **and the caption is false as written**: *"EACH BAR STEP IS TEN TIMES THE ONE BEFORE"* — the steps are 50×, 6.8× and 47×. Read as a claim about the *scale* it cannot be checked either: there are no gridlines, ticks or labelled decades. **P1's version of the same bench states it correctly**, and is the model to copy. → (1) Rewrite the caption to P1's honest form (*"The scale is squashed — every 8.6% along the track is ten times the energy — because a bathful and a teaspoon cannot be drawn on one straight scale."*) (2) Design: decade gridlines labelled 100 J → 10 MJ, so the squashing is visible rather than asserted. The "16,000 ×" card is doing the real teaching and stays exactly as it is. *Code (caption) + Design brief (gridlines); small / medium.*
- **P11-19** · `why-ice-floats` — the same event carries **two numbers on one page** and nothing reconciles them: the prose says water *"expands sharply — by roughly **9%**"* (in the reveal, explainer 2, the key fact, the key note and rung 3's first criterion), and the bench says *"FREEZING CHANGES THE DENSITY BY **−8.0%**"*, with rung 1 marking "About 8%" correct. **Both are right** (volume rises 9%, density falls 8%) — but a Year 7 has no way to know they are the same fact from two ends, on a page that explicitly asks students to compare its two numbers. The 8% also does double duty as the fraction of an iceberg above the surface, a third quantity sharing the digit. → One clause where the two meet: *"…8.0% less dense rather than more — the same fact as saying the ice takes up about 9% more room, counted from the other end."* *Code + Mide sign-off; small.*
- **P11-22** · `why-ice-floats` · `references` — **C1's `testing-the-model` names "why ice floats" as the declared failure of the simple particle model** (*"Identical spheres cannot produce that"*), and its rung 1 marks it correct as the answer to "name one thing the particle model cannot explain". **This lesson is the answer to that question — and neither page points at the other.** So the student who was told the model fails never learns it was repaired, and the student reading the repair never learns it was an open question. **The single best continuity opportunity in the unit, unspent.** → Add the reference both ways and one clause naming the repair: *"This is the one the simple sphere model could not do: identical spheres cannot make an open cage. What it was missing is the *shape* of the water molecule."* *Code; the added sentence past Mide's science gate; small.*
- **P11-23** · all four lessons · **`figures: []` on every lesson — "Matter and the particle model" contains no drawing of a particle, or of anything else.** No canvas, no diagram SVG anywhere in the unit; `ks3_art/p11.py` says so outright. The four benches are bar charts and number cards, which is the right instrument for density and internal energy and **the wrong one twice**: `brownian-motion` is a lesson about a *visible movement* whose entire instrument is three static bars, so **a student finishes it without ever having seen a random walk**; and `why-ice-floats` turns entirely on *"an open hexagonal cage with a gap in the middle"* versus the same molecules jostling closer — a two-panel diagram, and the most-reproduced picture in this part of school science, here in prose. It also removes the only route by which P11 could carry the "same size, bigger gaps" drawing P11-14 needs. → **Two Design briefs**, specified in §5b. *Design brief → Code; Mide sign-off on the drawn science; medium (batch of two).*

**S3**
- **P11-08** · `density` · after Check, touching **any** bench control silently rewrites the question, the five model lines and the final answer, **while the verdict line and the student's own typed text stay in place** — so a student who scrolls up to re-read the bars is marked against a question they never answered. Driven: checked at gold/500 (model answer 19.30), pressed the Oak tab, and the panel read "325.0 g of oak… density = 0.65 g/cm³" with the old answers and the unchanged verdict still there. → Freeze the attempt's tokens at the moment Check is pressed and re-arm only when the student re-opens the question; or, if live coupling is wanted, withdraw the marked panel with a visible line saying the question has changed (the affordance chemistry asked for on C3's crystallising bench). *Code; withdraw wording past Design; small.*
- **P11-25** · all four lessons · the ladder's **"Retry my misses" button is rendered enabled on page load**, before any rung has been answered and therefore before any miss can exist — and pressing it does nothing at all (verified by DOM read: header unchanged, no rung reopens, no state change, no console output). **A control that is enabled and inert teaches a student their press did not register.** Kernel-level, so it is on every ladder in the key stage; reported once. → Disable until at least one rung is answered **and** at least one is wrong, with the same "nothing to retry yet" affordance the Complete button already has. Land with SYS-2 and P12-23. *Code; small.*

**S4**
- **P11-04** · `density` · **two false universals, stated twice each** — *"Those are the only two pairings you will meet"* and *"there is no such unit as kg/cm³ or g/m³"*. g/m³ is real and common (absolute humidity); kg/cm³ is unusual but legal; and — the one that will actually bite — **GCSE chemistry runs on g/dm³**, grams paired with neither of the two "only" volumes. The teaching point survives without the universal claim. Same shape as chemistry's c1-09, rated the same. → *"the two pairings you will meet in this lesson"*, and *"mixing the two families gives you kg/cm³, which is not a unit anyone uses, so if a question gives you a mass in one family and a volume in the other, converting one of them is the first line of the working."* *Code + Mide sign-off; small.*
- **P11-06** · `density` · Rung 1 — a structural tell the length gate cannot see: the correct answer is the **shortest** (2 words against 7/9/9) and the only one without an em-dash clause. MRB-177 looks for the correct answer being longest, so the inverted tell passes untouched. (Checked across all eight P11 rungs: this is the only one; three others have the correct answer longest but all inside the ≤3-word margin, **so MRB-177's remediation is holding**.) → SYS-8 form 3: *"3.0 g/cm³ — divide the mass by the volume"*, which states the rule the rung is testing. *Code; small.*
- **P11-07** · `density` · end matter reads *"Before this lesson: Nothing — this is where the unit starts"* while four inches below the footer reads *"Previous: How a motor works"*. The source records why: `requires` was left empty because P10 was in a different worktree and an unresolvable prerequisite fails `validate()`, with the note *"it is one line to add when the lanes merge"*. **The lanes have merged** — P10's lesson is in this tree and the footer already resolves it — so the registered temporary is now a live contradiction. → Add the P10 edge the source note already names. *Code; small.*
- **P11-12** · `brownian-motion` · *"struck so evenly that the imbalance is nothing against its **weight**"* — what resists the unbalanced push is **inertia**, i.e. mass; the argument holds in orbit, where the grain has no weight at all. One lesson away from P12, which spends two lessons insisting weight is a force in newtons, and it is one of the words the protocol names as an everyday/physics trap. → "against its mass". *Code; small.*
- **P11-17** · `temperature-and-internal-energy` · on the **largest** tab — the one a student is most likely to press, because it is the one the lesson keeps naming — the card reads *"A BATHFUL HOLDS / **this one** / at exactly the same temperature"*, which is not English read as the sentence the other three tabs make. → *"the most of the four"*, or better, use the ratio the model already computes: *"16,000 × a teaspoon"*. *Code; small.*
- **P11-20** · `why-ice-floats` · explainer 1 — *"they **no longer need as much room** to move about in"*: particles do not *need* anything (the teleology chemistry hunted in C1's diffusion lesson), and **"need room" is the exact phrasing through which children arrive at "particles get bigger when hot"** — the closest any P11 page comes to the unit's named misconception, in the opening sentence of the lesson that has to defeat it. → *"…so they no longer push each other as far apart, and they settle closer together — the particles themselves are unchanged; it is the gaps between them that shrink."* Plants P11-14's sentence in a second place, cheaply. *Code + Mide sign-off; small.*
- **P11-21** · `why-ice-floats` · on the **water** tab the third bar duplicates the second exactly (both "1.00 g/cm³", both 94.34% fill), and the `aria-label` says it twice. The comparison bar earns its place on the other three tabs; on the one tab the lesson is named after, it is a stutter inviting a student to hunt for a difference. → Suppress it when the substance **is** water (the model already knows), which the alt text then follows automatically. *Code; small.*

---

### P12 · Space · 6 lessons · **23 findings** (S1 3 · S2 10 · S3 1 · S4 9)
*In §4: P12-22 → SYS-3 · P12-23 → SYS-2. P12 is the second unit with **no drawings at all** (SYS-D), and its auditor produced the estate's mirrored-length measurement (26 hits across 14 units).*

**S1**
- **P12-07** · `gravity-earth-moon-and-sun` · **the Sun's mass is understated by a factor of 1000.** *"the same force barely stirs a body of **two thousand trillion trillion kilograms** and swings a smaller one right round it."* The body barely stirred is unambiguously the Sun. As written that is 2 × 10³ × 10²⁴ = **2 × 10²⁷ kg**; the Sun is **1.989 × 10³⁰ kg**. **The number as printed describes a large planet — it is almost exactly Jupiter (1.90 × 10²⁷) — and it is doing so in the one sentence whose entire job is to explain why the Sun barely moves.** On a page otherwise exact to three significant figures, this is the one figure written in words rather than computed. *(Independently verified by the cross-unit pass, which also confirms the file: it is on `gravity-earth-moon-and-sun`, not `the-sun-stars-and-galaxies`. The unit's other large numbers on both pages are **right** — "around two trillion galaxies" and Sgr A* at "about four million solar masses" both check out. This is an isolated slip, not a pattern.)* → *"two million trillion trillion kilograms"* is the correct words-form. **Recommended instead: the comparison form, which cannot be mis-scaled** — *"barely stirs a body 330,000 times the mass of the Earth"* — since "thousand/million trillion trillion" is exactly the construction that produced the slip. *Code; **Mide sign-off** on which form (a choice about register); small.*
- **P12-01** · `gravity-and-weight` · CFIFA with the bench on **"Deep space"** — the question is live-templated from the tab and the place label is interpolated into four prepositional slots that only work for a body. One click gives, verbatim: *"50 kg standing **on deep space**"*; *"the one for **deep space** — the place you are standing"*; ***"Downwards, towards the centre of deep space"***; *"The five lines give 0 N **on deep space**"*. Three are broken English. **The fourth is a physics claim**: it asserts a downward direction towards a centre of deep space, in the one state whose entire teaching point is that there is nothing there to be pulled towards, on the page whose think-again exists to kill *"there is no gravity in space"*. A weight of 0 N has no direction and deep space has no centre. Reachability was **driven, not inferred**: with the reveal open and the tab switched, all four strings render (the blocked panel hides only the input rows), and the panel simultaneously says *"the five lines come back"* while the five lines are displayed beneath it. → Give the Deep space row its own prepositional forms (a `place_in` field: "in deep space" / "on Earth" / "on the Moon") and a per-row `direction` string whose Deep space value states the physics: *"No direction at all — with no field there is no pull to have one."* The zero-field row already has a bespoke `zero` branch on the bench, so the data model supports it. *Code; the replacement sentence past Mide sign-off; small.*
- **P12-09** · `the-sun-stars-and-galaxies` · the distance readout on two of five rungs — the panel is captioned *"Distance from Earth in light years"* and the card is labelled *"DISTANCE FROM EARTH · how long its light has been travelling"*. **Two of the five objects are things the Earth is inside, and for both the figure shown is the object's *size*:** the solar system at "11.0 light hours", and **the Milky Way at "100 thousand ly" — which is the galaxy's diameter, and the card immediately to its right says so ("SIZE · about 100,000 ly across")**. The note then asserts *"At 100 thousand ly from Earth, the light reaching you from the Milky Way set out that long ago"* — false in every reading (light from the Milky Way has been travelling between about 4 and 80,000 years, and we sit ~26,000 ly from the centre). **This is the exact confusion the lesson exists to remove**: a student just taught that a solar system sits inside a galaxy is shown a card saying they are 100,000 light years from their own galaxy. It also undercuts the lesson's real and lovely point that every distance is a look into the past, by attaching it to two figures that are not distances. → (a) Split the card — keep "Distance from Earth" for the Sun, Proxima and Andromeda, show "How far across" for the two inside-objects, and recaption the panel; or (b) keep one axis and give the two inside-objects real distances (the solar system's edge is 11.0 light hours *out*; the Milky Way's centre is 26,000 ly away), which also fixes the note. **Either way the two "look into the past" sentences must be suppressed where they are false.** *Code; the relabelling past Mide sign-off; small.*

**S2**
- **P12-14** · `seasons-and-the-tilt`, and the unit as a whole — **nothing anywhere in KS3 teaches that the Earth turns on its axis once a day, or that this is what causes day and night**, and this unit is the slot that owns it. Across all six Space lessons: "day and night" **0**, "24 hours" **0**, "rotation" **2** (both inside rung 4's self-mark criteria — *"the tilt can keep a place in sunlight through a whole rotation"*), "spin" **1** (inside a hook distractor, a wrong answer). A repo-wide sweep of the entire KS3 estate returns five matches for "day and night / turns on its axis / Earth rotates", of which **the two physics ones are both wrong answers**. So the lesson talks continuously about hours of daylight, noon and the Sun climbing, and asks a student to reason about "a whole rotation", while the 24-hour spin and its distinction from the 365-day orbit are never stated. **That is the single commonest conflation in the topic — students answer "it is night because the Earth goes round the Sun" — and the unit neither commits it nor forestalls it.** → One explainer paragraph at the top of this lesson, before the tilt: the Earth turns once on its axis every 24 hours, which makes day and night; it also travels round the Sun every 365¼ days, which makes a year; **the seasons come from the second motion and the tilt, not from the first**. Rung 4's "whole rotation" then has a referent, and two sentences close the KS3 day-length ground nothing currently covers. *Code; the new teaching past Mide sign-off; small.*
- **P12-15** · `how-far-is-a-light-year` — **the page is titled with a question and answers it by assertion, three times, with no worked route anywhere.** `9.46 × 10^15 m` appears in the second explainer, the key fact and the key note; the page contains **no 365, no × 24, no × 60 × 60, no seconds-in-a-year figure** — the derivation that gives the lesson its title is absent. The protocol's named scaffolding defect ("a finished result shown with no worked route to it") landing on the one page whose title is the question — and it is the most winnable arithmetic in the unit: the student has just been given `d = c × t`, has just watched minutes converted to seconds, and every ingredient is on the page. → A third staged worked example, *"How far does light travel in one year?"*, using the block that already exists: **C** 365 × 24 × 60 × 60 = 3.15 × 10⁷ s · **F** d = c × t · **I** 3.0 × 10⁸ × 3.15 × 10⁷ · **F** 3.0 × 3.15 = 9.46, powers add to 10¹⁵ · **A** 9.46 × 10¹⁵ m — one light year. **That single block answers the title, teaches the year→seconds conversion the CFIFA has removed (P12-16), and demonstrates the power-adding step the CFIFA never shows (P12-17) — one addition closes three findings.** *Code; the new worked example past Mide sign-off; medium.*
- **P12-13** · `seasons-and-the-tilt` · **the most diagram-dependent lesson in KS3 physics ships with no diagram.** Two geometric arguments are made entirely in words: (i) a tilt fixed in space plus an orbital position determines which hemisphere leans sunwards — the mechanism the lesson exists to teach, and the thing the second think-again has to *deny* in prose because there is no picture to deny; and (ii) *"the same beam is concentrated onto a smaller patch"*, which **rung 2 then tests directly, having never been shown**. The spread-beam drawing is in every KS3 scheme in the country because it is the one idea a single picture settles and a paragraph does not. → Two drawings, specified in §5b. *Design brief → Code; Mide sign-off on the drawn science; medium.*
- **P12-08** · `gravity-earth-moon-and-sun` · **explains an orbit — a curved path from a radial force acting on a body with a sideways velocity — entirely in prose, with no drawing at all.** Newton's cannon has been the canonical drawing for this idea since 1728. Rung 3 then asks the student to *write* the falling-and-missing account from five criteria having never been shown it, and the force-pair claim (*"equal and opposite, however different the masses"*) is the one place in KS3 where two arrows of identical length on two very different bodies does the teaching in one glance. → Two drawings, specified in §5b. *Design brief → Code; Mide sign-off; medium.*
- **P12-12** · `seasons-and-the-tilt` — **a seasons lesson that never names two of the four seasons.** "Autumn" appears **nowhere** on the page or anywhere in the unit; "spring" appears **once**, as a bench-gate distractor the student is being taught to reject — so the only time a student meets the word it is attached to a wrong answer. The bench's verdict for both equinoxes is the unnamed *"a season in between"*, on both hemispheres. Separately, **"solstice" and "equinox" each appear exactly once**, as bare readout sub-labels, never glossed — a Year 7 meets both cold. And the lesson never says *why* 21 March and 23 September produce identical readouts, which is a genuinely interesting consequence of its own model, one press apart on the bench. → Name them in the verdict branch the bench already has (*"That is spring here and autumn in the other hemisphere"* and the reverse) — the model knows the date and the hemisphere, so no new data is needed. Gloss both technical words once at first use: *"an equinox — the two days a year when every place on Earth gets twelve hours of daylight"*, which the bench's own 12.0 h readings then confirm in front of the student. *Code; wording past Mide sign-off; small.*
- **P12-03** · three lessons · CFIFA Fine-tune vs Answer — the two lines **disagree about how a number is written, with no step between them**, inside the block that asks the student to tick "I had this" line by line. Three strands: **silent rounding** (`6 × 24.8 = 148.8` → `W = 149 N`; `185 × 3.7 = 684.5` → `685 N`), with no rounding convention stated anywhere, so a student who correctly wrote 148.8 cannot honestly decide whether they had it; **spurious trailing zeros** (`1200 × 10.0 = 12000.0`, while p12-01's identical component prints `1000` with no `.0`); and **thousands separators in the Answer and never in Fine-tune** (`29760.0` then `29,760 N` on consecutive lines). Displayed answers are not to a consistent precision either. → Format both lines through **one** formatter, and where the Answer rounds, say so in its stepnote (*"684.5 N, which is 685 N to the nearest newton"*). Declare the convention once in the key fact. *Code; the rounding convention past Mide sign-off; small.*
- **P12-16** · `how-far-is-a-light-year` · **the fading sequence runs backwards at the last step.** Worked example 1 has nothing to convert and says so; worked example 2 converts minutes to seconds and closes *"Convert first, then the same four lines. Your turn below."* **The "your turn" block then pre-converts the time inside the question stem for all five states** ("whose light takes 1.34 × 10^8 s to arrive") and prints, as the model Convert line, *"the time is already in seconds"*. So: full example **without** the conversion → full example **with** it → independent practice **without** it. The one skill the second example exists to teach is the one skill the independent step never asks for, and **the years→seconds conversion (4.24 years → 1.34 × 10⁸ s) — the hardest and most valuable on the page — is done off-screen and never shown.** → State the time in the stem in its natural unit (*"whose light takes 4.24 years to arrive"*) and let the Convert line do the work it is there for. The Moon state then legitimately keeps "nothing to convert", **which makes the contrast teach rather than disappear.** *Code; small.*
- **P12-17** · `how-far-is-a-light-year` · Fine-tune → Answer — the step makes **two unexplained moves at once in standard form**, in every state: *"3.0 × 7.89 = 23.67, and the powers add"* → *"d = 2.37 × 10^22 m"* — **the mantissa is renormalised from 23.67 to 2.367 (with a compensating exponent change) *and* rounded, neither named.** Worked example 2 does it in the other direction with no step at all. **Renormalising a mantissa is precisely where a KS3 student loses this calculation**, and the clause "and the powers add" shows the page knows the step needs naming — it names the easy half and skips the hard half. → Extend the Fine-tune line to carry it explicitly: *"3.0 × 7.89 = 23.67, and the powers add: 23.67 × 10²¹ = 2.37 × 10²²"* — same five steps, the move shown where it happens. *Code; small.*
- **P12-19** · `how-far-is-a-light-year` · Going further — *"the **fastest object humans have ever launched** would take about 70 000 years to cover those 4.24 light years."* 70,000 years is **Voyager 1's** figure (17 km/s). The fastest object ever launched is the Parker Solar Probe at ~192 km/s, which would take about **6,600 years** — an order of magnitude out. **A checkable superlative on a page about scale, in a stretch paragraph written for exactly the student who will check it.** → *"the fastest spacecraft ever sent out of the solar system"* — one clause, keeps the number and the point. (Naming Voyager 1 explicitly would also connect it to the paragraph above, which already uses Voyager for the signal delay.) *Code; value past Mide sign-off; small.*
- **P12-24** · all six lessons (and 14 units key-stage-wide) · **the mirrored length tell.** MRB-177 flags a set only when the correct option is **strictly the longest** by ≥4 words or ≥1.4×; the mirror is unmeasured and live. On three of P12's six recall rungs the correct answer is strictly the **shortest** by a large margin (2 words against 9/10/12; 2 against 6/9/9; 4 against 9/10/11), because the correct option is a bare numeric answer while every distractor carries an appended "— wrong reason" clause. A student can score all three calculation rungs by picking the only option that does not explain itself. **Measuring the mirrored threshold over all 370 four-option sets in the key stage returns 26 hits across 14 units, 24 of them ladder recall — one construct, not 26 slips**, which is precisely the shape MRB-177's own comment warns about. *(No P12 set trips the existing "longest" gate — the longest-construct really has been fixed — and p12-04's gate and recall are built at exactly equal lengths, 36/36/36/36 and 37/37/37/37, which is the authoring doing it right.)* → Strip the trailing clauses from the **distractors** on the three P12 rungs (the reasons already exist in the per-option feedback the student sees after answering, so nothing is lost), and **make `length_tell()` symmetric**, then sweep the other 23. → SYS-8. *Code; small per question, small for the gate, medium for the sweep.*

**S3**
- **P12-05** · `mass-vs-weight` · the closing note, **all 16 states** — *"**Move the slider and every bar changes** while the words 'mass still 1 kg' underneath do not."* **Both halves are false.** The slider is *Where it is* (Earth / Moon / Mars / Jupiter) and the bars show all four places at once, so moving it changes **no bar** — driven at all four positions, values and fill widths byte-identical; all it moves is a highlight. The control that *does* change the bars is the **object tab** — and when it does, it also changes the very sub-labels the sentence promises will not move ("mass still 1 kg" → "6 kg" → "55 kg" → "1200 kg"). The root looks like reuse: p12-01's bench has a *mass* slider, where the identical sentence is true. **On this page it names the wrong control and the wrong invariant, and it is the sentence carrying the lesson's entire mass-vs-weight contrast.** → *"Change the object and every bar changes together, because they all scale with the same mass. Move the slider and no bar moves at all — the four places are already side by side; the slider only says which one you are standing in."* Better still, point at the readout that genuinely holds still: *"The Mass card never moves. Everything else does."* *Code; small.*

**S4**
- **P12-02** · three lessons · **all three formula triangles author `"text": ""` on all three faces**, so three `<p class="ks3-tri-note">` ship empty — one of them not even hidden, rendering as blank vertical space under the result. Every other formula triangle in KS3 physics carries a per-face sentence explaining the rearrangement; P12 gives only the generic close, once, for all three faces, **so the student who covers *m* and gets `m = W ÷ g` is never told which arrangement produced it.** → Author the three notes on each page, matching the estate's existing pattern. If the blank is deliberate, drop the elements rather than emitting empty paragraphs. *Code; small.*
- **P12-04** · all four CFIFA questions in the unit — **the moment the reveal opens**, with no tick yet possible, the tally prints *"0 of 5 lines you had. Rewrite the ones you missed before moving on."* A finished verdict and an instruction to rewrite, before the student has been given the chance to claim a single line. **The same shape as SYS-2, in a second component.** → Hold the tally at a neutral progress string ("Tick each line you had") until the first tick. One branch, the same fix shape. *Code; small.*
- **P12-06** · `mass-vs-weight` · *"Move the slider and **only the last four change**."* Driven at three positions, the lines that change and the line that does not are the wrong way round: line 1 (Convert) **does** change because it carries the field strength; line 2 (Formula, `W = m × g`) is the only one that never changes. Exactly four lines change — 1, 3, 4 and 5. → *"Move the slider and only the formula line stays the same — the field strength reaches into four of the five."* True, and a better teaching point than the original. *Code; small.*
- **P12-10** · the bench note says the Sun is *"about **two thirds** of the way out"* of the Milky Way; three sections later the same lesson says 26,000 ly from the centre of a galaxy 100,000 across — a radius of 50,000, so **a little over half**. The lesson supplies the numbers that contradict its own adjective, on the page whose whole subject is getting scales straight. → *"about 26 000 light years from the centre, a little over halfway to the rim."* *Code; small.*
- **P12-11** · two lessons · three strands of one notation problem. **(a)** The panel caption reads *"Distance from Earth in light years"* while its first two rows are in light **minutes** and light **hours**. **(b)** *"each bar step is ten times the one before"* is a statement about the **axis** and reads as a claim about the objects (the real steps are ×80, ×3400, ×24,000, ×25) — and the lead above the panel says it properly, so the terse caption beside the drawing is the version that misleads. **(c)** Powers are written with a **caret** — `9.46 × 10^15 m` — **28 times across three pages, and `^` is never glossed anywhere in the unit or the key stage**, while UK exam boards and KS3 maths write standard form with a superscript. *(This does not re-open the ruling that standard form is in scope for KS3 — only how it is rendered.)* → (a) Recaption. (b) Move the lead's confession clause into the caption, so the scale is declared where the drawing is. (c) Render powers as `<sup>`, or gloss the caret once on first use. → §6 if (c) sets an estate-wide convention. *Code; small each.*
- **P12-18** · `how-far-is-a-light-year` · **the Earth–Sun distance is given three different ways on one page, and one pair is presented as identical when it is not**: the bench card reads **149.7 million km**, the card beside it reads **1.50 × 10^11 m** under the sub-label *"the same number, written out"* (1.50 × 10¹¹ m is 150 million km), and worked example 2 computes **149.4 million km**. The legal line declares the Sun's light time as **499 s** while the bench displays **8.3 minutes** = 498 s — and 499 vs 498 is exactly what produces the 149.7/149.4 split. Lesson 4's hook gives 150 million km. **On the page teaching that a time and a distance are the same statement, the page's own arithmetic does not close.** → Pick one travel time (498 s is what "8.3 minutes" means and what the worked example uses) and derive every display from it, so the cards read 149.4 million km and 1.494 × 10¹¹ m and the "same number, written out" claim becomes true. *Code; the chosen value past Mide sign-off; small.*
- **P12-20** · `the-sun-stars-and-galaxies` · *"A red dwarf. **Its light left in the year you were about ten.**"* Proxima's light takes 4.24 years, so the sentence is true only for a reader of about fourteen — the very top of the KS3 band. **A Year 7 reading this is eleven, and 4.24 years ago they were about seven**, in a card whose whole job is to make the number personal. → Make it arithmetic instead of an assumption: *"Its light left a little over four years ago — work out what year that was, and how old you were."* Truer, personal for every reader, and turns a claim into a task. *Code; small.*
- **P12-21** · `how-far-is-a-light-year` · the "So the distance is" card carries the fixed sub-label *"300 000 000 m/s × the time"* in all five states — but on the two stellar rungs the value shown is "4.24 light years" and "2.50 million light years", **where nothing has been multiplied**: the time has been restated with the word "light" inserted. The card does a different job on those two rungs while claiming the same derivation. The restatement is arguably the lesson's own point, but the sub-label vouches for arithmetic that did not happen. → Branch the sub-label: keep it for the three km rungs, and for the stellar ones *"which is what a light year means — no multiplying needed"*, **which converts the inconsistency into the teaching point.** → SYS-5. *Code; small.*
- **P12-25** · unit index and one lesson · two breadcrumb links fall below the 24 × 24 CSS-px minimum (WCAG 2.5.8): `Physics` at 44 × 22 and `Space` at 20 × 46. Every other control in the unit measured comfortably above at 390px, so it is confined to the trail. → `padding: 4px 6px` on `.ks3-trail a` with a matching negative margin, or a `min-height`/`min-width` with `inline-flex`. *Code; small.*

---

## 5b · DESIGN BRIEF PILE

Everything below is written so Design can act without reading the rest of this
report. **34 briefs in four groups.** Where a finding ID is given, the full
evidence — path data, measured geometry, screenshots — is in
`records/p<N>.md` under that ID.

### Group A — eleven drawings that do not exist at all

These are not redraws. In each case the lesson currently does the drawing's job
in prose, and in five of the eleven the missing picture is the canonical diagram
of the topic.

1. **A pendulum** (P1-10, `conservation-of-energy`). The unit's flagship
   instrument is three stacked bars, four readouts and four buttons with **no
   picture of a pendulum**, while the prose beside it says "watch the top of the
   bar rather than **the bob**", "twice a swing", "the thermal store of the air
   and **the pivot**". Draw a small pendulum beside or above the bar stack,
   sharing its state: fixed pivot, string, bob, arc, and **the release height
   marked with a faint horizontal rule** so the student can see the return height
   falling swing by swing — that falling height is what the lesson's own big
   question is about ("comes back almost as high — but only almost") and nothing
   on the page shows it. Animate on the same clock as the bars (bob at the arc's
   end when gravitational is full, at the bottom when kinetic is full, hanging
   still at the end). If animation is too costly, a static three-panel figure —
   released / at the bottom / hanging still — with the three bar states beneath
   carries most of it.
2. **A calorimeter with a thermometer and a flame** (P2-04, `energy-in-food`).
   The drawing is a boiling tube of tinted water, a sample mark and a few orange
   specks. Its own alt text describes *"a thermometer in the water"*, and there
   is no thermometer element of any kind. This is a required-practical apparatus
   diagram and **the thermometer is where the number the whole lesson depends on
   comes from.** Add the thermometer (bulb in the water, stem out of the tube
   top) and a visible flame under the tube. A draught shield would let the
   drawing carry the lesson's own explanation of where the energy goes.
3. **A plane-mirror image ray diagram** (P7-07, `reflection-mirrors-and-scattering`).
   **The one genuine curriculum gap in P7.** An object arrow in front of a plane
   mirror; two rays from its tip to the mirror obeying i = r, both arrowed; their
   reflections continuing to an eye; both back-projected as **dashed** lines
   meeting at the image behind the mirror; and the two equal distances marked.
   The dashed/solid distinction is load-bearing — the prose to go with it is *"no
   light ever goes behind the mirror; the light only looks as if it started
   there."*
4. **The Brownian random walk** (P11-23a, `brownian-motion`). A square cell. One
   visible speck as a filled disc, with its past 12–15 positions joined by
   **straight segments meeting at sharp angles — never a smooth curve** — and a
   scatter of much smaller open circles for the molecules, with arrows arriving
   at the speck from all sides. **Caption inside the frame, non-negotiable:**
   *"the molecules are drawn thousands of times too big and millions of times too
   few — you could never see one."* Animate if cheap; a still with a traced path
   teaches most of it. A student currently finishes this lesson without ever
   having seen a random walk.
5. **Ice versus liquid water, two panels** (P11-23b, `why-ice-floats`). **Same
   number of molecules in each panel, same molecule size in each, at one declared
   scale.** LEFT (ice): the hexagonal arrangement, molecules held at fixed angles
   with a visible hole at the centre of each ring. RIGHT (liquid): the same
   molecules disordered and on average slightly closer — **the outline of the
   right panel must be visibly smaller for the same count.** Label both boxes
   with their volumes so the 9% is readable off the drawing. **Do not draw
   anything inside the cage's hole, and say so in the caption** — *"the gap is
   empty — there is nothing in it at all"* — which forecloses the "air in the
   ice" reading that rung 2 has to fight.
6. **Newton's cannon** (P12-08a, `gravity-earth-moon-and-sun`). A cannon on a
   mountain top; three trajectories from one muzzle — too slow (falls to the
   ground), right speed (closes into a circle), too fast (opens away) — with the
   gravity arrow drawn **radially inwards** at one point on each path and the
   velocity arrow **tangentially**, in two visibly different colours. One caption
   line: *"the same pull, three sideways speeds."*
7. **The Sun–Earth force pair** (P12-08b, same lesson). Sun and Earth at true
   relative **size** (not separation), a broken-scale mark on the gap, and **two
   arrows of identical drawn length** pointing at each other, both labelled
   3.54 × 10²² N. The equality is the whole point, and equal arrow lengths on
   unequal bodies is the fastest way to teach it.
8. **The orbit with a parallel axis** (P12-13a, `seasons-and-the-tilt`). A
   near-circle (with a footer *beside the drawing* confessing that the 3%
   eccentricity is too small to draw), Sun at the centre, Earth at four
   positions, and **the axis drawn parallel in all four — the parallelism is the
   entire teaching point and must be visually unmistakable.** Shade the sunlit
   half at each position; label only "June" and "December".
9. **The spread beam** (P12-13b, same lesson). One beam of fixed width striking
   flat ground at 60° and at 15°, the two illuminated patches drawn **to the
   correct relative length (1 : 3.9)**, with the page's own numbers as the
   caption: "88% per square metre" and "25% per square metre". Rung 2 tests this
   directly and the student has never been shown it.
10. **A neutral object that is not an empty box** (P9-4, `charging-by-rubbing`).
    Today a neutral block is drawn completely empty with "0.0 nC" in it — the only
    picture of *neutral* a student ever gets, on a page whose second sentence is
    *"in a neutral object the two exactly balance"*. Draw it as a **balanced pair**
    (faint interleaved + and −), and draw the charged states as that same balanced
    set **plus** the net imbalance, so a student can see the + marks were there all
    along and only the electron count changed. Lesson 2's induced sphere is the
    model. Cheaper fallback: one fixed caption inside the frame saying an unmarked
    block is balanced, not empty.
11. **The motor's circuit and brushes** (P10-23, `how-a-motor-works`). The figure
    below the bench names *"the brushes — fixed contacts that press on the split
    ring"* as one of four parts of a motor, **and the bench draws no brushes at
    all**; there is also no supply drawn, and the two leads run in the field
    lines' own tone at the field line's own y, so they read as field lines. Route
    the circuit down and round, draw a cell symbol as the electromagnet bench
    already does, draw two brushes pressing on the two halves of the ring, and
    give the lead its own tone.

### Group B — six drawings that assert the misconception they exist to kill

Highest priority in this pile. Each currently teaches, in a picture, the belief
its own page marks wrong.

12. **The prism fan** (P7-22, `colour-and-the-spectrum`) — draws violet deviated
    least and red most, and deviates everything toward the apex instead of the
    base. Recompute so the fan sits entirely on the base side of the extended
    incident beam with **red nearest it**; simplest is to flip the prism apex-down
    and keep the current y-values. **Also draw the faint dashed "where it would
    have gone" line** — the ladder's rung 1 asks about exactly that line.
13. **The prism's internal path** (P7-24, same drawer, land together) — 68 units
    of glass with nothing drawn between the entering beam and the exiting fan, on
    a lesson whose mechanism sentence is *"one bend on the way in, another on the
    way out"*. Draw one white internal segment from the entry face to the exit
    face, bent toward the normal at entry, and start the coloured fan at the exit
    face.
14. **The spectrum band** (P7-25) — six hard-edged blocks with visible joins,
    directly above a caption saying *"a band that has no joins in it"*. Paint it
    as a `linearGradient` red→violet with the six named stops, and move the six
    names to tick labels beneath a continuous strip. The two arrows and the layout
    stay exactly as drawn.
15. **The iris** (P7-19, `the-eye-and-the-camera`) — the drawn opening is a
    constant 12 units at every light level and the **blades** grow from 12 to 66
    units as the light falls, so the eye visibly *closes* in the dark while the
    readout says the pupil opens. Pin the blades' **outer** ends to the case and
    let the inner ends move with the opening, so the gap is the aperture and grows
    in the dark. Re-check all ten states (five levels × two instruments).
16. **The crowding tile** (P10-6, `magnetic-fields`) — five lines on the strong
    side and three on the weak, which is the misconception `MAG-08` verbatim, and
    the page's own rung-1 feedback refutes it. Draw the **same five lines in both
    groups** and let spacing carry the whole difference (8 px pitch versus 24 px).
    Better still, one continuous fan converging into a bundle at one end.
17. **The motor coil, end-on** (P10-22, `how-a-motor-works`) — the force is drawn
    along the same line as the current, denying *"at right angles to both"*, which
    the lesson calls the one new fact it rests on. **The drawing is nearly right
    already**: the axle is a circle, so we are looking along it. Replace the two
    vertical members with **two circles carrying ⊙ and ⊗** (swapping when the
    current reverses), add a small key ("● current towards you · ✕ current away
    from you"), keep the field horizontal and the force arrows vertical exactly as
    they are, and keep the loop's top and bottom as a faint outline round the back.

### Group C — the arrowhead system, and eight drawings that need it

18. **One shared `<marker>` arrowhead in the KS3 SVG kit** (SYS-A). No SVG in any
    of the 70 physics lessons defines or uses an arrowhead marker. **Convention to
    settle and write down:** a head at the far end of travel; on a long multi-segment
    ray, a mid-path head as well; **never** on a construction line — normals, ghost
    paths, and P10's deliberately-impossible "no crossing" tile must stay headless
    so the distinction reads. Then apply per drawer to: P7's reflection, refraction,
    pinhole, eye, prism and clamp rays (P7-04); **P10's globe field lines**, solenoid
    arcs, crowd-tile lines and the readings needles' north end (P10-10, P10-12);
    and P4's force vectors alongside brief 20 below.
19. **The straw / apparent-position construction** (P7-10, `refraction`). The
    dashed "back" line runs into the wrong quadrant, leaves the glass through its
    side wall, and the "WHERE IT LOOKS" marker sits on the **real** ray. Minimum:
    redraw the back-projection as the true backward extension and move the marker
    onto it, directly above "WHERE IT IS". **Better:** draw **two** rays from the
    straw's end to two nearby points on the surface, refract both, and let their
    two dashed back-projections **intersect** at the apparent position — the honest
    construction, which delivers the "higher **and closer**" the alt text already
    promises and removes the single-ray arbitrariness.
20. **Named force arrows on five benches** (P4-11). Five of six arrow benches
    label their arrows with a magnitude only ("66 N" and "66 N", nothing saying
    which is the pull and which the friction) — while the names already exist in
    the tiles below and in the aria-labels, **so the screen-reader description of
    these diagrams is better than the diagram.** Add a short caption under each
    arrow using the tile wording: drag lane "your pull" / "friction"; support rig
    "weight" / "push of the support" / "resultant"; sledge "pull right" / "pull
    left" / "resultant"; fall "weight" / "air resistance" / "resultant"; spanner
    "your pull". The interaction board's existing `cap_a`/`cap_b` is the model. **At
    390px the captions must sit inside the existing scroll container rather than
    widening it.**
21. **Free-body geometry on the support rig** (P4-04b). The weight and upward
    arrows are drawn at opposite ends of the frame, both floating clear of the load
    block; only the resultant is anchored. Move both onto the load as free-body
    convention requires (weight from the block's centre-bottom downwards, the
    support's push from the contact point upwards), keeping the resultant offset or
    clearly labelled as the sum rather than a fourth force.
22. **The eye's ray construction** (P7-20). Each ray bends at the **aperture**,
    not the lens, so the drawing is pinhole geometry with a lens ornament behind
    it. Draw two or three rays from the scene's top through different heights of
    the lens, bending at the lens face(s) and converging on the retina — the
    construction the previous lesson's own panel already draws correctly.
23. **The globe's buried magnet** (P10-12). It gets the headline fact right — the
    magnet's north end at the geographic south — **and neither half is labelled**,
    so the one picture that proves the lesson's central claim cannot be read. Put
    an **N** on the lower half and an **S** on the upper, in the treatment
    `how-a-motor-works` already uses, and one caption line under the globe. Separate
    the four field lines' endpoints a few pixels either side of the pole so they
    read as entering a region rather than crossing at a point.
24. **The solenoid's field** (P10-18). Two arcs over the top and nothing else — no
    line through the bore, nothing below — while the explainer says the fields stack
    up **inside** the coil and the key fact says the shape is a bar magnet's. Mirror
    the arcs below and add straight segments through the bore, so the loops close
    and the interior is where the lines are densest.
25. **The bench object that is modelled and not drawn** (P10-13). "A steel clamp
    stand" and "a speaker magnet" change every readout and rotate the needle, and
    **nothing is added to the drawing** in 22 of 54 states. Draw a small labelled
    rectangle / disc at the end of the level line the needle turns towards.
26. **A coil whose turn count is visible** (P10-20). Eight loops at every setting,
    while the *current* is visible (the stroke thickens with it) — so of the two
    variables the bench separates, one is drawn and one is not, directly on the
    misconception that they are the same variable. Draw 4 / 6 / 8 / 12 / 16 loops
    over the same core length so the loops visibly crowd as turns rise.

### Group D — layout, scale and phone legibility

27. **Ray diagrams at 390px** (P7-29). On a phone every ray diagram in the
    ray-diagram unit renders ~110px tall with in-figure labels at ~4 CSS pixels,
    while the readout tiles beneath each bench get full-width cards with 20px+
    type. **The pattern to copy already exists in the same unit:** put the figure
    in its own `overflow-x: auto` scroller at a fixed 560–640px SVG width below
    ~560px, exactly as `.ks3-lband-scroller` already does for the comparison tables
    (which is why those stay legible at 390 and the drawings do not).
28. **In-SVG captions at 390px** (P10-1). Five captions across three lessons are
    set at a fixed 15px in a 1000 × 400 user space, so they scale with the drawing
    and render at **5px** on a phone — including *"SEEN FROM THE SIDE, LOOKING
    WEST"*, the only thing telling a student which way they are looking at the dip
    circle. The HTML overlay fills on the same drawings already floor at 9px with
    `clamp()`; adopt that treatment for the `<text>` captions.
29. **The opposed-beam figure at 390px** (P5-14). 480px wide in a 390px viewport,
    centred, bleeding 45px off each edge: six of seven labels damaged and the
    seventh — **"17.0 N OVER"**, the whole point of the sinking panel — entirely
    outside the viewport, with no horizontal scroll to reach it. Stack the two
    panels vertically below ~430px.
30. **The `ks3-beam` drawer** (SYS-B). Two pans of 120 units carrying 16–26
    character labels inside a 520-unit box with `overflow: hidden`, so
    `simple-machines` renders *"ce × your distance"* at every width. Widen the
    viewBox and size the pans to their content, or (better at 390) move the caption
    into an HTML `<p>` beneath the SVG where it can wrap.
31. **The nine-case charge matrix at 390px** (P9-10). 620px inside a 314px
    scroller with **no affordance of any kind**, so the third column is invisible —
    and the lesson's closing rule is only defensible if you have seen that four of
    the nine cells are induction. A right-edge gradient fade is the minimum and
    should land first; restacking as three labelled groups below ~480px is better.
32. **The insulation results table at 390px** (P1-23). The fourth column, *"What
    it blocks"* — the only place the lesson says why foil and wool differ — is
    entirely off-screen. Simplest and probably better on desktop too: lift that
    column out of the table into a four-line legend underneath, since it is static
    text that never changes as the clock runs.
33. **The density league table** (P11-3). Honest proportional bars against gold at
    19.30 leave oak at 3.4%, ice at 4.8% and water at 5.2% — **so a student cannot
    see from the panel that ice is less dense than water**, which is the next
    lesson's entire subject. Draw the **1.00 g/cm³ water line as a marked rule
    across the panel** so the four light materials are read against a visible
    reference. **Do not switch this panel to a log scale** — see the next item.
34. **Decade gridlines on the two logarithmic panels** (P11-16, P11-11). The
    internal-energy panel is logarithmic with no gridlines, ticks or labelled
    decades, so a child reading bar length reads "a bathful holds twice a
    teaspoon" where the truth is 16,000 times. Add decade gridlines labelled
    100 J / 1 kJ / 10 kJ / 100 kJ / 1 MJ / 10 MJ, so the squashing is **visible
    rather than asserted**. On the Brownian panel, the third bar is on a log scale
    while its two neighbours are linear, breaking the drawer's own stated contract
    — **move the size comparison out of the proportional panel into the readout
    row as a card**, where a number carries no implied length.

**Two conventions worth settling once, because several briefs depend on them:**
the arrowhead (brief 18) and **whether a declared scale must be drawn** — three
P6 lessons publish hand-written pixels-per-unit figures describing generated
geometry, and one of them is wrong by 44% (P6-13). Deriving those figures from the
drawer's constants at build time would close that class permanently.

---

## 6 · MIDE PILE — the rulings only he can make

Fourteen items. Each is two lines of finding plus concrete options. **Safety and
safeguarding items carry NO drafted wording, per protocol — the auditors flagged
the gap and stopped.** Nothing else in this report is escalated: science is
standing authority and has been corrected in place.

### M1 · Safety and safeguarding wording — eight units, no wording drafted
**Finding.** Physics ships **two** safety-adjacent lines in 70 lessons: the
neodymium-magnet safeguarding note on `magnets-and-poles` and the mains note on
`conductors-and-insulators` (both in the MRB-257 ruled treatment, both verified
present and correct on the served page). `safety_note` is set on **no physics
lesson in P2, P5, P7, P8, P9, P10, P11 or P12** — while the slot exists and is
used elsewhere in physics (`springs-and-hookes-law`, **P4**).

⊕ **Corrected by the cold double-check, 28 Aug 2026.** That parenthesis originally
read *"(`springs-and-hookes-law`, P1)"*. `springs-and-hookes-law` is in **P4**, not
P1, and it is the **only** physics lesson in the estate with a `safety_note` set —
no P1, P3 or P6 lesson has one either. So the honest framing is **11 physics units
of 12 have no safety note at all**, not 8 of 12; the eight named above are the
eight where an auditor found something a child could actually do. Estate-wide,
`safety_note` is used in b1, b3, b4, b7, c2, c3, c5, c6, c7, c8, c9 and p4 —
**physics is the outlier subject, not merely a set of outlier units**, which
strengthens M1 rather than weakening it. Both safety-adjacent prose lines named
above were re-verified as served, as was the P7 point: the Sun-safety line
(*"Never look directly at the Sun, at a welding arc or into a laser…"*) is on
`the-eye-and-the-camera` and on **no other P7 lesson**, so a student on
`lenses-and-images` or `colour-and-the-spectrum` never meets it.

**The gaps, ranked by what a child could actually do:**

| Unit | What is described | Auditor's note |
|---|---|---|
| **P9** `electric-fields` | *"You are safe inside a car in a thunderstorm, and it is not the tyres"*, and **rung 4 requires the student to reproduce that reasoning** | Real safety information about a hazard that kills people in the UK most summers, given to twelve-year-olds with **no framing of what the claim does not cover** (a convertible, a fibreglass boat, an open tractor cab, touching metal inside the car) and no line about what to do in a storm when you are not in a car. The physics as written is correct. **The one that most needs his decision.** ⚠️ The 21 Aug ruling recorded in that lesson's docstring — "no Childline block anywhere in P9" — is about the *safeguarding-disclosure* block and does **not** speak to a practical safety note. |
| **P2** `energy-in-food` | Weighed food set alight under a boiling tube; the food list includes a **peanut**, its note calling it *"the classic school sample"* | Naked flame, hot glass, combustion products, **and a nut in a classroom**. Nut allergy is a safeguarding question, not a science one. |
| **P5** `atmospheric-pressure` | *"**Boil a splash of water in an empty can, seal it, and cool it.**"* — imperative, do-it terms | Boiling water, steam, a sealed vessel, a hot can handled hot, a violent implosion, **described as a method rather than as something seen.** Also p5-02's *"You punch three holes down the side of a full can"* and p5-01's *"Hold a drawing pin between finger and thumb and squeeze"*. |
| **P7** `lenses-and-images`, `colour-and-the-spectrum` | Full pinhole-camera build instructions, a convex lens gathering light to a point, a prism in white sunlight, ray boxes at the bench | **The Sun is the hazard, and it is exactly what a child will point a pinhole camera or a lens at.** The unit's one good line (*"Never look directly at the Sun… it is painless at the time, and it does not heal"*) sits on lesson 5, which a student doing lesson 4 or 6 has no reason to have read. |
| **P8** `building-and-measuring-a-circuit` | The unit's **practical** lesson; a bench state the page calls *"a dangerous current pours through the meter"*; a fault table instructing *"Open the switch at once"*; 230 V wiring and a 20.3 A overload elsewhere in the unit | **The distribution is the point:** the one lesson with a line is the classification lesson, and the one that runs the practical has none. The shape of an oversight rather than a policy. |
| **P10** `electromagnets`, `how-a-motor-works` | An electromagnet build (a nail, a cell and wire is the standard Year 8 build) whose legal line notes a real coil *"would get hot enough to matter within a minute"*; a motor rig with a supply and a spinning part | Neither carries a `safety_note`. Also **for sign-off as shipped**: the MRI paragraph's *"an oxygen cylinder brought too close is pulled in hard enough to kill"* — factually correct, referring to a real documented death, the only sentence in the unit naming a fatality, and attached to nothing the student is asked to do. |
| **P11** `density`, `brownian-motion` | Rung 3 asks students to describe finding a stone's density with a balance, cylinder and water — a method a class will then run; the smoke cell is described in enough detail to be attempted | Both low-stakes; c9-03 is the precedent for a footer note on a class practical. |
| **P12** `the-sun-stars-and-galaxies` | **Actively invites naked-eye sky observation three times**, and rung 4 says *"Explain what you are actually seeing when you look at it"* | The unit's only Sun-safety wording is **one clause inside a narrative hook sentence** (*"it is so bright you must never look at it directly"*) — not in a safety slot, and the third clause of a sentence whose first two are facts about size and distance. Whether that covers the three invitations is his call. |

**Options.** (a) Author a `safety_note` per lesson where he judges one is needed —
the slot, the renderer and the ruled treatment all exist. (b) Rule that specific
absences are **deliberate** and record them as such, as the chemistry audit did for
c7-04, so no future audit re-raises them. (c) A middle path for P5 and P7: leave
the safety slot empty but recast p5-04's imperative hook into the passive form its
own second paragraph already uses, and move or repeat P7's Sun line onto the two
lessons that invite the hazard. **Recommendation: rule on P9, P2, P5 and P8 before
September; the other four can wait.**

### M2 · P8-01 · The 400 kV power line — science **and** hazard description
**Finding.** *"…a **400 000 V power line is not dangerous because of the number**,
and a car battery at 12 V can weld metal."* The teaching point is right; the
example is the one object in the world where volts alone very nearly are the
danger (400 kV arcs several metres, so you need not touch it). And at every width
rendered the sentence **breaks after "is not"**, so a scanning Year 8 reads *"a
400 000 V power line is not dangerous"*.
**Options.** (a) Swap the example to the static shock, which is true, keeps the
whole teaching point and connects to P9 — the auditor's suggested wording is in
`records/p8.md`, for his editing, and closes with *"a power line has both, in
enormous quantities, which is why you never go near one"*. (b) Keep the power line
and add the missing qualifier plus a never-go-near clause. (c) Cut the sentence.
**Recommendation: (a).** *This is his gate because it is a science call and a
hazard description at once; Code executes once ruled.*

### M3 · The 840 authored bank questions that have never shipped — product scope
**Finding.** 840 physics bank questions exist, fully written and banded, in
`ks3_data/p<N>/questions_*.py` — and there are **0 physics rows** in
`ks3_assignment_bank`, `ks3_ladder_questions` and `ks3_cards`. The export that
shipped biology and chemistry (1,356 rows) never ran for physics. **Lesson pages
are unaffected**; what does not exist is the weekly assignment and the dashboard
flashcards. It is the largest single gap between physics and the other two
subjects, and closing it is an export run, not authoring.
**Options.** (a) Export before September, so physics can be set as an assignment
in the autumn term. (b) Ship physics lesson-pages-only for September and export at
half-term. (c) Leave it and say so in the docs, so it stops being rediscovered.
⚠️ **If (a), fix SYS-8 form 2 first**: in the authored bank a student who always
picks the longest option scores 35% instead of 25% (56% in P11), and no student is
exposed to that today **only because the pool is empty**. Exporting first would
ship the tell to students.

### M4 · XU-1 · The replacement Key-fact wording for temperature
**Finding.** Three definitions across two subjects; the correct one is taught
first and contradicted twice; P1's **ladder criterion marks against the correct
answer**. The science is settled (§4) and is standing authority — **what needs his
sign-off is the wording, because two of the three sites are Key fact / Key note
boxes.**
**Options.** (a) Adopt the proposed wording verbatim (§4). (b) Edit it. (c) Accept
"average speed" as a partial credit for one cycle in P1's ladder so the change
lands softly for students already taught it. **One owner for both subjects, not
two.**

### M5 · Money — the 27p and 53p tariffs
**Finding.** 27p per kWh and a 53p daily standing charge appear on **eight
surfaces across two lessons**, undated, presented as what a bill says. Both are
good 2026 figures; the Ofgem cap moves every quarter. The drawer's own docstring
says *"it is a plausible mid-2020s tariff, **it will date**, and when it does it
changes in one place"* — **the isolation is already done; the page is what never
says so.**
**Options.** (a) Date them where they are shown ("At 27p per kWh (2026)") plus one
clause in the hook, which converts a dating liability into the lesson's own point.
(b) Update the figures now and revisit each September. (c) Leave. **Recommendation:
(a) — it is one clause and it teaches something.** *Money is his gate.*

### M6 · P10-26 · Amber as the "selected" colour — a design-system ruling
**Finding.** On dark bench blocks the SELECTED state of every segmented control is
painted with `var(--ks3-alert)` — the warning/loss token — on five controls per
bench and up to four benches per page. Nothing has gone wrong when a student picks
"Free to tip". **Three units have now stopped at this**: the P10 build commit of
25 Aug records that a per-unit override was removed to keep one control behaving
one way on 199 pages, and that "the amber-as-selection question is raised as a
finding by all three units" of that run. **Unresolved rather than ruled.**
**Options.** (a) Amber **is** the selection channel on ink grounds, and the
"amber only warning/loss" rule is amended to say so. (b) The pressed state moves
to the accent token (as the light-ground branch already uses) and amber is
reserved. **Either is fine; what matters is that it is written down**, because it
will otherwise be raised a fourth time.

### M7 · P2-26 · Should "Reading a fuel bill" cover gas? — product scope
**Finding.** The lesson's statutory bullet is *"domestic fuel bills, fuel use and
costs"*. **Gas is absent entirely** — for most UK households the larger bill, and
its meter reads cubic metres and converts to kWh through a calorific value, which
is squarely physics. A student who takes this lesson to the kitchen table and
picks up the gas bill finds nothing on the page applies. (VAT is also absent, but
that is one clause and Code can do it.)
**Options.** (a) Retitle to "Reading an electricity bill" and follow the unit
index — honest, no new content. (b) Add a "Going further" on the gas meter's
m³ → kWh conversion — a strong stretch for exactly this audience, and it closes
the statutory bullet properly. **Recommendation: (b) if there is authoring time,
(a) if not.**

### M8 · The 60-character Complete gate — ruled item, observed harm
**Not a defect claim and not a request to relitigate the 19 Aug no-copy ruling.**
Four units independently produced **correct** answers that left the Complete button
dead with **no message, no counter and no `aria-disabled`**:

| Unit | Answer typed | Chars | Button |
|---|---|---|---|
| P5 | *"Same force, tiny area at the point, so huge pressure there."* — uses all three required words, satisfies four of five criteria | 59 | **dead** |
| P3 | *"Take the mean of the three times, then divide 1.20 by it."* — satisfies criteria 3 and 4 outright | 57 | **dead** |
| P4 | *"The handle is far from the pivot, so the moment is big."* — both required words, would be credited | 55 | **dead** |
| P8 | measured the threshold precisely: dead at 20, 40, 55, 58; enabled at 60 | — | — |

Counter-evidence, recorded honestly: **P9 found a terse-but-right 33-character
answer that DID pass** ("Electrons moved, protons did not."), and P10, P11 and P12
found no harm because their rungs demand five distinct criteria and a genuinely
complete answer cannot be that short. So the harm is real and **rung-dependent**.
**P8 found the fix already written, three sections away on the same page:** the
"Check my five lines" button says *"Write at least one line first"* and, in the
copper state, *"Waiting on a specimen the ammeter can read"*.
**Options.** (a) **Keep the threshold exactly as ruled and add the affordance** —
one line under the disabled button ("a sentence or two — the button opens when you
have written enough"). Costs nothing, removes the dead end, does not touch the
ruling. (b) Lower to ~40 characters, which would have passed all four answers
above. (c) Switch to a word count (P5's answer is 11 words). **Recommendation: (a),
and it can ship without any ruling on the threshold itself.**

### M9 · `#s-think` as a rail stop — Design's `DONE`, raised by three units
**Finding.** On P9, P11 and P12, the rail's THINK stop ticks from the **hook** or
from **ladder rung 1** — both outside the section — so the rail can read 2/4 with
the misconception block unread, and reads done · not-done · done. **Faithfully
ported**: Design's own `DONE` is `if (id === 's-think') return s.gate !== null`,
and the package notes argue that a `mirrors` predicate would tick it *late* and
fail `check_rail_matches_design`. P11 adds the sharper observation: on three of its
lessons the THINK section **contains zero controls of any kind**, so a student who
clicks the rail link arrives somewhere there is nothing to do and may find it
already ticked.
**Options.** (a) Leave it and accept Design's contract, recording the reasoning
where a future auditor will find it — it is already logged against p9-01 in the
misconception register. (b) Give `#s-think` its own completion signal (a control in
the confrontation block), which changes what Design drew. **Already parked; three
more units have now hit it, which is why it is here.**

### M10 · P9-7 · What does "Before this lesson" mean?
**Finding.** P9 L1 declares `requires` = P8's `building-and-measuring-a-circuit`
(ammeters, voltmeters, building a circuit) — **none of which this lesson uses** —
while the lesson it actually needs, `conductors-and-insulators`, is filed two
headings lower as a see-also. A stuck student who clicks the link labelled *"Before
this lesson"* is sent to the one P8 lesson that cannot help. `requires` appears to
be carrying "the lesson immediately before this one in the skeleton", which is
already shown separately as "Previous:".
**Options.** (a) Treat this instance as a data error and swap them — Code, small.
(b) If `requires` is **deliberately** the skeleton predecessor, then the heading
*"Before this lesson"* is what should change, **key-stage-wide**. **Recommendation:
(a) unless he intends (b).**

### M11 · SYS-F · Eight of P4's nine lessons point forward across a school year
**Finding.** Eight of P4's nine lessons (Year 7) carry the same `references` entry
to P5's `pressure-force-over-area` (Year 8), rendered as an unconditional live
link. It reads as a template applied, not eight considered links. It is not a lie
— the card says "Connects to", not "next" — but eight identical forward links
teach a student that the card is noise. **Touching the covered-lessons scoping is
his call, which is why this is here rather than fixed.**
**Options.** (a) Leave them. (b) Drop the reference from the seven where it is
template-applied and keep it on `what-a-force-is`, where the connection is
genuinely instructive. **Recommendation: (b).**

### M12 · P8-08 · Which fix for the prefix ladder
**Finding.** The practice item tracks the bench, so seven of fourteen reachable
states demand a conversion the page never teaches (µA, nA and **pA**, the last
needing standard form, which is KS4). **The first practice item can be harder than
anything worked.**
**Options.** (a) Restrict the coupling to states in A or mA — one predicate, safe
before September. (b) **Teach the prefix ladder once**, with a small "mA, µA, nA,
pA — each a thousand times smaller than the last" strip beside the figure that
already spans fourteen orders of magnitude — the better lesson, and a small Design
ask. **Recommendation: (b) if the Design batch runs before September, (a) if not.**
Neither removes the need for P8-03 and P8-17.

### M13 · P6 · Should the sound unit make a sound? — product scope
**Finding.** Verified estate-wide, not just in P6: **there is no audio anywhere in
the key stage.** `<audio>` 0 · Web Audio 0 · `new Audio(...)` 0 · `.mp3`/`.wav`/
`.ogg` 0, across all 182 lessons. Every instrument in the sound unit — the tuning
fork, the slinky, the pitch bench, the auditory-range bars, ultrasound — is silent
and visual. **Plainly a deliberate posture** (silent-by-default is right for thirty
students on shared devices, and for accessibility), and P6's audit shows the visual
instruments teach the physics correctly. **But it has never been written down**,
P6 is the one unit where the phenomenon itself is audible, and a pitch slider that
changes an actual pitch is the single most persuasive demonstration available in
the topic.
**Options.** (a) Keep it silent **and say so in the docs**, so it stops being
rediscovered. (b) Allow audio in `frequency-pitch-and-loudness` only, gated behind
an explicit press, never autoplay, with a visible mute. **Recommendation: (b) for
that one instrument, where the gain is largest and the scope is one bench.**

### M14 · Three smaller calls, grouped
- **P7-07 — extra teaching time.** Closing the plane-mirror-image gap adds a figure
  and a short explainer to `reflection`, i.e. teaching time, not just a fix. It is
  the one genuine curriculum gap in P7 and a student currently cannot answer "why
  does writing look backwards in a mirror?". *Ruling: add it, or accept the gap.*
- **P12-14 — the missing day/night teaching.** Nothing anywhere in KS3 teaches
  that the Earth turns once a day; P12 is the slot that owns it, and the two
  physics mentions in the whole estate are both **wrong answers**. One explainer
  paragraph closes it. *Ruling: add it (recommended — it also closes curriculum
  ground nothing covers), or leave.*
- **P3-26 / P12-11c — two notation conventions.** P3's ruled position is that
  "velocity" appears nowhere, and it appears once on **every** P3 page in the
  end-matter GCSE card, unglossed. And P12 writes powers with a **caret**
  (`10^15`) 28 times, never glossed, where UK exam boards use a superscript. Both
  are one-line fixes; both adjust or set a convention, which is why they are here.
  *Ruling: gloss, or rewrite the P3 cards in the unit's own register; and adopt
  `<sup>` estate-wide or gloss the caret once.*

---

## 7 · FIX-RUN PLAN

Grouped and ordered by what blocks what. **167 findings are Code alone and can
start immediately**; 88 more are Code with a wording sign-off, 45 want a Design
brief first, 10 want both, and 5 are Mide's alone. Nothing in F0 or F1a–F1d except
the four drawing-dependent items waits on the Design batch.

### F0 · Unblock (Mide, before or alongside F1)
The eight rulings in §6 that gate work: **M1** (safety wording — rule P9, P2, P5,
P8 first), **M2** (400 kV), **M3** (bank export — and it must be answered *before*
the export runs, not after), **M4** (temperature Key-fact wording), **M5**
(tariffs), **M6** (amber), **M7** (gas scope), **M12** (prefix ladder, only if the
Design batch is running). M8–M11, M13 and M14 do not block anything.

⊕ **Contradiction resolved by the cold double-check, 28 Aug 2026.** §1's bullet
list of *"the eight that block a fix run"* ends with **M8** (the 60-character
Complete gate) and omits **M12**; this list says M8 blocks nothing. **This list is
right and §1's has been corrected.** M8 is explicitly filed as *"not a defect
claim and not a request to relitigate"* — the ruled threshold can stand untouched
and the silent-button fix is ordinary Code work needing no ruling at all, so it
gates nothing. §1 now names M12 in its place.

### F1 · The 63 S1s — science and misconceptions · **the September-safe line, part 1**
Runs in five waves, ordered so the shared machinery lands before the instances
that depend on it.

**F1a — the estate-wide corrections (start here; small, and they unblock nothing else but are the widest).**
XU-1 (**seven sites: four prose statements across P1, C1 and C7, two ladder
criteria — P1's and C1's — and one bridging clause; corrected upward by the cold
double-check from "three sites + one criterion"** — **one owner across physics and
chemistry**) · P12-07 (the Sun's mass) · P4-01 (friction
never pushes along — **and the second site in `questions_05_friction.py`, which
must be fixed before that pool is ever populated**) · P9-1 (the triboelectric
re-rank, plus the two consequential edits; no authored sentence quotes a rank, so
nothing else moves).

**F1b — the nine benches that demonstrate the negation of their own lesson.**
These are the estate's worst class and every one is contained.
P1-13 (thermal store `n × T`, **plus the `r_two_quantities` guard**) ·
P7-22 + P7-24 (the prism, **plus the build assertion on dispersion order**) ·
P10-22 + P10-23 (the motor, end-on — needs Design brief 17, so schedule it with
the batch) · P11-09 + P11-10 (the Brownian jiggle — one line, one sentence) ·
P3-11 + P3-12 (the journey matcher's two scales and its clamp) ·
P3-1 (the light gates' prescribed method) · P3-18 + P3-19 (the frames bench's
missing zero and its static cars) · P10-7 + P10-8 + P10-11 (the compass on the
magnet, the gap note, the equator tip) · P7-19 (the iris — **re-drive all ten
states after the arithmetic changes**) · P2-19 (the fridge claim).

**F1c — the arithmetic that is printed false.**
P5-12 (`2.4 − 10 = 7.6`) · P8-03 (mantissa printed as quotient, 7 of 14 states) ·
P1-25 (the lever table's three failures) · P8-04 (2.94 V, plus rungs 1 and 2) ·
P2-13 (the kilo applied silently). **Land the build assertion with them: a printed
`a ÷ b = c` must satisfy `a / b ≈ c`, and no student-facing text node may match
`/\de[-+]?\d/`.** That one assertion closes P8-17 and P7-02 as well, estate-wide.

**F1d — the wrong numbers and wrong claims in prose.**
P2-09 (the charger → a router, five coordinated sites) · P2-24 (900 W → 120 W
fridge) · P2-15, P2-16 (the two magnitude anchors) · P2-02, P2-31 · P5-07 (the
bottom jet, four sites including a rung criterion) · P6-07 (the tuning fork) ·
P6-08 (57 vs 60 mm) · P6-10 (a million → ten million) · P8-02 (copper at 2 Ω) ·
P8-05, P8-06, P8-07 (the three `conductors-and-insulators` / `resistance` notes) ·
P11-01, P11-02, P11-13, P11-18 · P12-01, P12-09 · P1-1, P1-5, P1-9, P1-15, P1-16,
P1-24 · P3-9, P3-10, P3-20, P3-21 · P4-02, P4-03, P4-04a · P7-04 (needs Design
brief 18) · P7-10, P7-23 · P9-9, P9-14 · P10-2, P10-3, P10-6 (needs brief 16).

**F1e — verify.** Re-drive every touched bench to its edges. Several of these
fixes change values that other strings quote (P1-13's readouts, P8-04's 2.94 V,
P9-1's badge split, P2-09's five sites), so the check is per-bench, not per-file.

### F2 · Shared chrome and the gates · **the September-safe line, part 2**
Twelve items. Each is small, and **each closes many instances at once** — several
across all three subjects.
1. **SYS-3** — two CSS rules. **Verify across biology and chemistry too**, and add
   the Range-based ink-overflow assertion to the 390 sweep.
2. **SYS-2** — one branch in the ladder kernel's header (closes 70 physics lessons
   plus chemistry's C2-3 / C3-02), **plus P12-23's Retry condition and P11-25's
   enabled-but-inert Retry button**, plus P12-04's identical shape in the CFIFA
   tally.
3. **SYS-8 gate work** — give the hook an explicit `answer` key; extend MRB-278's
   shuffle to `phenomenon.options` and bench `gate.options`; make the length check
   **two-sided and per-unit**; add the **shape** check (unique odd-one-out on
   dash / trailing clause / units); add a **per-rung** scope to the ladder check.
4. **SYS-8 authoring** — the 17 em-dash rungs, the hook rebalances (P2, P7, P8, P9,
   P4), and P12-24's three recall rungs. *(The 295 bank-length rewrites belong with
   M3, not here.)*
5. **SYS-V** — one `keyword` block per lesson (70 lessons, mechanical), plus the
   build warning for authored vocabulary with no consuming block.
6. **SYS-B** — the `ks3-beam` geometry, plus the build assertion that no `<text>`
   escapes its own `viewBox` (closes the three cosmetic instances too).
7. **The counter and readout assertions** — P4-14's `{n}`-in-`data-format` check
   and P6-09's every-slider-key-has-a-writer check. Both classes are **invisible to
   every existing gate** because the element renders, contains plausible text and
   never throws.
8. **The SYS-5 caption guard** — assert that a caption's size vocabulary agrees
   with the value beside it. Would have caught at least eleven instances.
9. **P8-18** — `tabindex`/`role`/`aria-label` in the shared `.ks3-cband-scroll`
   renderer: every scrollable table in both key stages, at once.
10. **The empty-`alt` assertion** (P4-17) — a case with no `alt` should fail the
    build rather than ship an empty accessible name. Second time a renderer's
    silent default has hidden authored teaching.
11. **The pluralisation helper** (P4-26, P6-12, P7-17, P7-26) — one helper for
    both key stages, plus a sweep for other count-of-one states.
12. **P8-06's gate predicate** — change the OR to an AND. One character of logic,
    and it stops 120 A being presented to a Year 8 as an ordinary reading.

### F3 · The 100 S2s — pedagogy
Runs after F1 and F2 and can overlap the Design batch. Natural groupings:
- **Vocabulary and first-use glosses** (11 findings): P1-4, P1-20, P4-13, P5-04,
  P5-18, P5-20, P7-11, P8-11, P8-12, P8-24, P9-16, P10-4, P10-28. Cheap, and
  several are one clause.
- **Scaffolding and fading** (6): P3-3, P5-16, P8-08, P12-15, P12-16, P12-17 —
  **P12-15's single new worked example closes three of them.**
- **Cross-unit bridges** (5): P5-17 (P5↔P11 floating), P9-16 (P8↔P9 static),
  P11-22 (P11↔C1 the model's declared failure), P10-27 (the field definition),
  P12-14 (day and night).
- **Coverage** (4): P6-05 (the title that promises reflection), P7-07 (mirror
  images), P11-14 (spacing / `PART-03`), P2-26 (gas).
- **Dead ends and unmarked commits** (4): P1-2, P1-6, P1-7, P9-3.
- **Instrument honesty** (the SYS-5 residue, ~20): each is its own wording fix;
  batch by unit.
- **Reading load** (SYS-R): the 152 long convention sentences, starting with P10,
  P5 and P9.

### F4 · The 36 S3s and 97 S4s — bugs and polish
Lowest risk, highest count, and several are a single token. Best done unit by unit
in one pass each, after F1–F3 have settled the values they depend on. **Do not do
these first** — a dozen of them quote numbers that F1 changes.

### What blocks what
- **F1b's motor fix (P10-22/23) and P7's ray work (P7-04, P7-10, P7-20) wait on
  the Design batch**; everything else in F1 does not.
- **M3 (the bank export) must not run before SYS-8 form 2** — exporting first
  ships a 35% guess rate to students.
- **F4 must not run before F1**, because a dozen S4s quote numbers F1 changes
  (P1-17's scale note, P2-25's 412, P12-18's 149.7, P11-19's 8%/9%).
- **The three build assertions in F1c and F2 should land with the fixes they
  describe**, not after — each was proposed by an auditor precisely because the
  class it catches is silent.
- **Nothing waits on the DB.** Physics has 0 rows in all three pools, so no fix in
  F1–F4 touches production data.

---

## 8 · COULD NOT REACH

Named honestly. Every unit reported the same four; the fifth and sixth are
unit-specific.

1. **The "Ask Mr Badmus AI" tutor round-trip** — present, wired and correct on all
   70 lessons (each with a lesson-specific prompt line, several of them good). The
   panel was opened and the controls verified on every unit; **no message was
   sent.** Sending POSTs anonymously to the production Claude backend and consumes
   quota, which is outside a read-only audit. Shared platform chrome, not physics
   content. *(Two accessibility observations recorded in passing and not filed,
   because they are shared chrome: the chat text input carries no label and no
   `aria-label` on all nine P4 pages, and the tutor close button is 30 × 32 px at
   390.)*
2. **Signed-in behaviour** — per-answer save, class attempt recording, the
   dashboard practice round. **The protocol forbids accounts, and none was
   needed**: lesson pages require no sign-in. Moot for physics in any case, since
   all three serving pools have 0 physics rows.
3. **The assignment bank as served content** — out of scope by the run constants.
   The `questions_*.py` files were read as *source* where a finding depended on it
   (P4-01's second site, P5's four misconception greps) but **840 authored bank
   questions have never been swept for content**, and chemistry's SYS-9 found
   defects in two of the two units it spot-checked. **If M3 approves the export,
   that corpus needs its own pass before it ships.**
4. **Live-origin console state.** All driving was against byte-identical local
   copies under the run's proven 83/83 parity. Serving from `localhost` adds an
   origin-specific `/api/health` CORS line that does not occur on mrbadmus.com; it
   was filtered where it appeared (and on several units it did not appear at all).
   **Live-origin consoles were not separately driven** — though 0 errors were seen
   on all 83 pages locally, before and after interaction.
5. **Real assistive technology and real touch.** Focus order, `aria-pressed`
   agreement, alt presence, labelled SVGs, heading structure and tap targets were
   all measured programmatically; **nothing was driven through an actual screen
   reader**, so findings like P2-04, P3-15 and P4-18 come from reading the string
   against the drawing rather than from hearing it. Similarly, 390px work used a
   true device-metrics override, but **gestures were synthetic** — so P9-10's
   horizontal swipe and pinch-zoom on P7's small figures are untested. Pinch-zoom
   in particular would *soften but not remove* P7-29.
6. **Unit-specific, three items.** (a) **Design's delivered reference pages** for
   P7 and P11 were not opened — P11's are not in this worktree at all, and P7's
   were not consulted, so for four P7 findings (P7-10, P7-19, P7-21, P7-22) **it is
   not established which side of the port the defect originated on**. P11's seven
   registered departures were instead verified *behaviourally* and all checked out.
   (b) **`prefers-reduced-motion` branches** in `wireLightGates`, `wireJourneyWalk`
   and the road animation were read in source and judged sound, but not driven
   under an emulated media feature. (c) **Real apparatus.** Several findings rest
   on physics rather than a bench run — P5-07's jets, P8-02's copper, P8-07's
   5.5 A nichrome, P9-1's acetate. Each gives its arithmetic or its authority in
   full, and none needs apparatus to check.

**Nothing failed to load, render or respond anywhere in the estate.** No page,
control, bench state, ladder rung or rail stop was unreachable. Across the twelve
units: every control on every page was pressed; every reachable bench state was
enumerated and read (486 on P10 alone, 132 on P8, 79 on P12, 150 on P10-01's
track, 100 on P10-02's compass grid, 40 on P8's component bench, 24 on P4's fall
and spanner benches, all 21 slinky positions on both drives); every ladder rung was
answered wrongly and then correctly; every textarea was typed short and long;
reload-mid-activity was driven; and all 83 pages were measured at a true 390px
reflow.

---


---

## 9 · COLD DOUBLE-CHECK

*28 August 2026. An independent reviewer who wrote none of the above, briefed to
break it. Everything below was re-derived from the records, the source data, the
served pages and the production database — nothing was carried forward from the
report or from any auditor's self-reported tally. **24 findings were re-opened
across 11 of the 12 units and all four severities; 22 reproduced in full, 1 was
partly struck, 1 was upheld as adjudicated.** Twenty-six corrections were made to
this report — thirteen of them numeric, one material to a headline finding
(XU-1), one proposed solution struck as unable to fix its own stated problem, one
finding widened from one unit to three, and two places where the report
contradicted itself resolved.*

### 9.1 · Counts, recomputed from zero

Every finding ID was re-extracted from the twelve records by regex on the header
line, with the severity taken from that same line. **The arithmetic is sound and
reproduces exactly at every step.**

| Step | S1 | S2 | S3 | S4 | Total | Verdict |
|---|---|---|---|---|---|---|
| Filed by ID across the twelve records | 64 | 100 | 45 | 106 | **315** | ✅ matches |
| After the P9-2 adjudication (S1→S2) | 63 | 101 | 45 | 106 | 315 | ✅ matches |
| After deduplication (−26 instances, +5 entries) | 63 | 98 | 36 | 97 | **294** | ✅ matches |
| Plus 2 estate-level items | 63 | 100 | 36 | 97 | **296** | ✅ matches |
| Unit subtotal (dedup) | 62 | 97 | 33 | 97 | **289** | ✅ matches |
| Systemic (§4) | 1 | 3 | 3 | 0 | **7** | ✅ matches |

**All twelve per-unit rows of §3's table reproduce to the finding.** The 26
deduplicated IDs all exist, all are unique, and their severities sum correctly to
the −1/−4/−12/−9 that the collapse removes. **Also confirmed:** 315 is the number
of unique `FINDING P<n>-<k>` IDs *and* the number of occurrences of the token
"FINDING" in the records — there are no duplicate or foreign IDs anywhere.

**ID gaps.** Verified by walking each unit's ID sequence: **P2-30 and P3-17 are
the only two gaps in the whole corpus.** Every other unit is contiguous 1…n.
Nothing is missing. The report's claim that a naive recount returns **326** also
reproduces: 315 finding headers plus the 11 `**S1**`-style severity sub-headings
in the records = 326 exactly, so the "eleven phantom findings" are accounted for.

**"Who fixes", recomputed by parsing every finding's own field:** Code alone
**167** · Code + Mide sign-off **88** · Design brief involved **55** · Mide's
alone **5** = **315**. ✅ §1's table is exactly right.

**Other structural counts confirmed:** 70 lessons (`ks3_data` and built HTML
agree) · 83 physics HTML files · per-unit lesson counts 8/5/3/9/4/9/7/7/3/5/4/6 ·
**34** Design briefs in §5b in four groups, Group A holding exactly 11 ·
**14** items in §6.

### 9.2 · Parity, database and estate-level positives — re-verified independently

| Claim | Method | Result |
|---|---|---|
| **83/83 live-vs-local byte parity** | fresh SHA-256 sweep of all 83 files against `curl -sL https://mrbadmus.com/…` | ✅ **SAME=83, DIFFER=0, EMPTY=0.** Confirmed. All later driving is therefore legitimate |
| **0 physics rows in all three pools** | `execute_sql` read-only on prod `urklkrwevjtlfbwnipjn` | ✅ `ks3_assignment_bank` 1356 · `ks3_ladder_questions` 226 · `ks3_cards` 612 — **totals exact, unit codes B1–B11 and C1–C10 only, not one P row** |
| **840 authored physics bank questions** | AST walk of `ks3_data/p*/questions_*.py` | ✅ **840**, and the per-unit row 96/60/36/108/48/108/84/84/36/60/48/72 is exact |
| **0 broken links in 1,399** | resolved every `href` three ways (file, +`.html`, `/index.html`) | ✅ **0 broken.** And 1,399 reproduces exactly as the count of internal path-bearing hrefs across the 83 files. All 293 `src` attributes also resolve |
| **0 console errors on all 83 pages** | drove all 83 through CDP | ✅ **0**, and none appeared during any of the interaction bursts below |
| **Zero AI slop** | independent sweep of **51** phrases (wider than the report's 29) | ✅ **Confirmed.** One hit, "takeaway", and it is a takeaway shop selling chips and ice cream. The 3 "in this lesson" and 2 "on this page" hits are all referential prose or convention notes, not platform meta |
| **SYS-1 absent** | string sweep | ✅ "Next in this unit" on **0 of 70** |
| **Weight given in kilograms / US spellings** | regex sweep | ✅ **none**, and **0** US spellings. "meters" ×13, every one an ammeter, voltmeter or utility meter — the metre/meter distinction is genuinely held |
| **The `9.81` convention note** | read on the served page | ✅ present, and it does confess the simplification. Exemplary, as claimed |
| **SYS-D: no drawings in P11/P12** | source + built HTML | ✅ `figures: []` on all ten lessons, **0** `<canvas>`, 9–11 SVGs per page and all of them chrome |

### 9.3 · The twenty-four findings re-opened

| # | Finding | Sev | Result |
|---|---|---|---|
| 1 | **P7-22** prism draws dispersion backwards | S1 | ✅ **Reproduced, every number exact.** Incident beam `M40 150 L262 210` extended to the screen at x=925 gives y=**389.19** — the report's "≈389". All six exit rays sit *above* it, i.e. deviated toward the apex of a prism whose base is at y=270. Deviations R **219.8** > O **185.0** > Y **150.2** > G **109.6** > B **63.2** > V **22.6** — matching the report to one decimal place, and exactly backwards |
| 2 | **P1-13** thermal bench proves the opposite of its lesson | S1 | ✅ **Reproduced, every number exact.** Drove all 9 states: store = n × T exactly. Spark at 1500 °C = **5 kJ**; bath at 40 °C = **2 kJ**. The closing paragraph beneath still reads *"the spark is the proof… almost no energy at all."* Bench range 60 J→90 kJ = **1.5 × 10³**, against a scale note claiming 10⁹. Real bath figure 100 kg × 4184 × 40 = **16.7 MJ**, so out by **8,368×** — the report's "~8,000" |
| 3 | **XU-1** contradictory temperature definitions | S1 | ⚠️ **Reproduced and CORRECTED — undercounted.** See 9.4 |
| 4 | **P9-1** triboelectric ladder ranks acetate wrongly | S1 | ✅ **Reproduced exactly.** Ladder served as 1 hair · 2 glass · 3 wool · 4 cotton · **5 acetate** · 6 polythene · 7 PVC. Drove the bench: acetate + wool → acetate **−7.3 nC**, wool **+7.3 nC**, the report's figures verbatim, printed with a confident explanation. Polythene + wool → polythene −11.0 nC, correctly — which is precisely what collapses the canonical two-sign school demonstration, since both then come out negative |
| 5 | **P11-09** Brownian jiggle ignores the speck | S1 | ✅ **Reproduced exactly.** All four tabs report **2.5 µm each second** at an identical 62.5% bar fill, while the size bar beneath them runs 3,000× → 100,000×. Pollen and milk fat jiggle identically |
| 6 | **P8-05** four times the current, called small | S1 | ✅ **Reproduced verbatim.** Nichrome at 1.50 V: *"passes 0.300 A, **a large current**"*. 10 Ω resistor at 12.00 V: *"passes **only** 1.200 A… the reading is **small**"*. Sharper still: the 30 Ω resistor at 12.00 V passes 0.400 A and is also called small, against nichrome's 0.300 A called large |
| 7 | **P3-11** two journeys, two vertical scales | S1 | ✅ **Reproduced, and re-derived independently from source.** `draw()` computes `dmax` from the union, but `paint()` calls `draw(tline, points(TARGET))`, so the target's union collapses to its own max. Payload: SECS=3, target walk\|still\|jog\|back, speeds 0/1.0/3.0/−2.0 → target max **12**. Four jogs → 36. Target's 3 m plots at y=**122.5**; the student's 9 m plots at y=**122.5** — identical. Target's 12 m peak at y=10 sits above the student's 27 m at y=47.5. **Two taps reach it** (2 jogs = 18 m > 12) |
| 8 | **P12-07 / XU-3** the Sun's mass | S1 | ✅ **Arithmetic verified.** "two thousand trillion trillion" = 2×10³×10²⁴ = **2×10²⁷ kg**; Sun = 1.989×10³⁰; error **1000×**; 2×10²⁷ ≈ Jupiter (1.898×10²⁷) ✓. Both proposed corrections check out: "two million trillion trillion" = 2×10³⁰ ✓, and Sun/Earth = 1.989e30/5.972e24 = **333,000**, so "330,000 times" is sound. The two cross-checks also hold (≈2×10¹² galaxies; Sgr A* ≈4.3 million solar masses) |
| 9 | **SYS-3** wordmark overprints the breadcrumb | S3 | ✅ **Reproduced 70/70, and the strike of P11/P4/P8 is CORRECT** — see 9.5. Magnitudes corrected |
| 10 | **SYS-2** finished verdict after one rung | S3 | ✅ **Reproduced.** Drove four ladders across four units: header goes *"Not started yet."* → *"**You got 1 of 4.**"* / *"**You got 0 of 4.**"* on the first answer, three rungs untouched. P12-23's rider also confirmed: on `mass-vs-weight` the "Retry my misses" control becomes visible at that same moment |
| 11 | **SYS-V** stranded vocabulary | S2 | ✅ **Reproduced; three denominators corrected** — see 9.4 |
| 12 | **SYS-B** the beam drawer clips its text | S3 | ✅ **Reproduced. Independently swept all 185 KS3 lesson pages for `<text>` escaping its own `viewBox`: exactly 5 pages, the same 5, no sixth.** Two magnitudes corrected |
| 13 | **SYS-8 Form 2** the 840-question length tell | — | ✅ **Reproduced to the decimal.** Uniquely longest **295 (35.1%, z=+6.8)** · uniquely shortest **127 (15.1%, z=−6.6)** · extreme **422 (50.2%)** · position **23.5/26.3/26.7/23.6** · P11 **56.2%**, P5 **45.8%**, P2 **43.3%** · P11 extremal **70.8%**, P3 **69.4%**. Not one figure off |
| 14 | **SYS-8 Form 3** the em-dash tell | — | ✅ **Reproduced exactly, including "physics only".** 17 rungs, all recall, all physics; per unit P5 4 · P6 3 · P8 3 · P4 2 · P7 2 · P12 2 · P11 1. Biology and chemistry return **zero**, and no other rung type carries it |
| 15 | **SYS-8 Form 1** hook positions | — | ✅ **Reproduced from ground truth, better than the report's own method** — see 9.6. A proposed solution is struck |
| 16 | **P4-08** per-rung ladder pattern | S2 | ✅ **Reproduced exactly** (recall A/C on all 9, apply B/D on all 9) — **and widened to three units.** See 9.6 |
| 17 | **P2-11** "Jump to the crossover" | S2 | ✅ **Reproduced verbatim.** The button lands on a state printing **Kettle total 360 kJ / Charger total 360 kJ** — equal — under the caption *"**Past** the crossover. The 15 W charger has now transferred **more** energy than the 2000 W kettle did all day."* |
| 18 | **P12-05** the inert slider | S2 | ✅ **Reproduced.** Drove all four slider positions: bar text and fill widths byte-identical at every one. The note claiming *"Move the slider and every bar changes"* is false, as is its second half |
| 19 | **P7-24** 68 units of undrawn glass | S2 | ✅ **Reproduced.** Beam stops at (262,210); fan starts at (330,210); **68 units**. Both points lie inside the prism (at y=210 the glass spans x 233.3→366.7) |
| 20 | **P1-18** impossible bench states | S4 | ✅ **Reproduced.** Nine reachable states; a 300 g mug and a 100 kg bath at 1500 °C, and a "spark" at 20 °C and 40 °C — **four** are physically impossible, as claimed |
| 21 | **P9-2** the insulator card | S2 | ⚠️ **PARTLY STRUCK** — see 9.4 |
| 22 | **P4-09** the unreachable "it holds" note | S2 | ✅ **Reproduced exactly.** The mass slider runs min 0.5, max 5, step 0.5 — **ten reachable masses** — and driving all ten shows the paper **tears at every one**. The authored `note_ok` for the paper holding is unreachable, as filed |
| 23 | **P6-10** the decibel arithmetic | S1 | ✅ **Reproduced exactly.** Served: *"every 10 dB is ten times the energy… A whisper sits near **30 dB**… a road drill near **100 dB** — **a million times** the energy of the whisper."* 100 − 30 = **70 dB**, which by the page's own rule is 10⁷ = **ten million**. The page contradicts a student who does the multiplication it just taught |
| 24 | **XU-2** the P9-2 adjudication itself | S1→S2 | ✅ **UPHELD.** Both load-bearing quotes verified verbatim on the served pages — P8's *"…the word describes how little, not none"* and P9's criterion 5 *"…the charge cannot travel along it to the wire"*. The reasoning is sound and the downgrade is right. On the served evidence it is, if anything, generous |

**Also re-opened and confirmed:** **M1** (safety wording) — both safety-adjacent prose lines verified served; `safety_note` verified set on exactly one physics lesson; the P7 point verified exactly (the Sun line is on `the-eye-and-the-camera` and no other P7 lesson). **P10-8** — structurally confirmed: the *"strongest part of the whole map"* sentence is a fixed `data-note` **attribute of the setup**, not of a state, and the setup has **25** probe spots, so it is necessarily printed identically at all 25. The specific 9.5-versus-100.0 magnitudes were not independently re-measured and are recorded here as unre-verified rather than confirmed.

### 9.4 · Struck and materially corrected

**STRUCK — one item, and it was struck by this report's own evidence.**

> **P9-2's stated harm.** The finding was filed against the **vocabulary card
> "insulator"** with the claim that *"the defect is confined to the card, **which
> is the one place a child re-reads**."* That is false. Per **SYS-V** — measured
> in this same report — physics renders vocabulary flip cards on exactly one page,
> `describing-motion/speed`, and `charging-by-rubbing` authors no `keyword` block.
> Verified directly: `ks3-keyword` occurs **0** times on the served page and the
> string "A material charge cannot travel through" appears **nowhere** in the
> served HTML. **No student has ever read this card.** Two findings in this report
> contradicted each other, and SYS-V is the one that is right.
>
> What survives, and is served, is the **ladder criterion** on the same page —
> which is what XU-2's resolution and proposed fix already correctly target. The
> **S2 severity stands**; the entry has been rewritten and the fix repointed.

**MATERIALLY CORRECTED — XU-1, and it inverts the finding's narrative.**

> XU-1 was filed as *"three contradictory definitions… **the correct one is taught
> first** and then contradicted twice"*, naming P11, P1 and C7, with "Lessons
> affected: 3 of 70 physics + 1 chemistry".
>
> An estate-wide sweep of **all 185 KS3 lesson pages** for a speed-based
> temperature statement returns **three lessons carrying the error** — and one of
> them, **C1 `changes-of-state`, the original pass missed entirely.** Worse, its
> instance is a **ladder marking criterion**: *"Says temperature is a measure of
> how fast the particles are moving."* Half-term placement derived from
> `ks3_data/half_terms.py` puts it at **Year 7, half-term 1** — the earliest
> temperature statement in the estate.
>
> | Order | Unit · lesson | Delivered | Verdict |
> |---|---|---|---|
> | 1st | **C1** `changes-of-state` | **Y7 HT1** | ❌ wrong, **in a marking criterion** |
> | 2nd | P11 `temperature-and-internal-energy` | Y7 HT6 | ✅ correct |
> | 3rd | P1 `heating-and-thermal-equilibrium` | Y8 HT2 | ❌ wrong |
> | 4th | C7 `energy-and-changes-of-state` | Y9 HT1 | ❌ wrong |
>
> So **the correct definition is met second, not first, and is outnumbered three
> to one** — and the wrong one is what earns credit at the first opportunity a
> child has to be marked on it. "3 of 70 physics" was wrong in both terms: only
> **one** physics lesson carries the error. The finding is **worse than filed**,
> not better.
>
> A second gap: the proposed solution named **three** fix sites and would have left
> at least three standing — P1's own **hook reveal** (*"Temperature tells you how
> fast the particles are moving on average"*), C7's **second** site (*"A
> thermometer measures how fast the particles are moving"*) and C1's criterion.
> There are **seven**. All are now listed.
>
> The finding's supporting measurements were re-derived: `thermal store` **34**
> across P1 and **0** in P11 ✅ exact; `internal energy` **0** anywhere in P1 ✅,
> but **27** on P11's temperature lesson (31 across the unit), not the 26 printed —
> corrected.

**Numeric corrections made** (each re-derived; none changes a severity or a count):

| Where | Was | Is | How measured |
|---|---|---|---|
| **SYS-3** overflow range | +60 to +124px | **+14 to +98px**, median +60 | `Range` over the wordmark text node vs `trail.left`, all 70 lessons at a true 390px |
| **SYS-3** worst five | 124/116/110/108/108 | **98/90/84/82/82** | as above; the *set* of five is right, the sizes were ~26px high, and they contradicted this finding's own strike paragraph, which gives P11 as 98 |
| **SYS-3** brand box range | 53–117px | **53–137px** | measured |
| **SYS-V** KS3 lessons | 182 | **185** | file count; the report already uses 185 in SYS-B |
| **SYS-V** vocabulary entries | 843 | **852** (B 309 · C 297 · P **246** ✅) | AST walk — a regex overcounts biology, whose entries nest |
| **SYS-V** stranded definitions | 650 | **643** (236 of them physics) | AST walk |
| **SYS-B** fuel-bill overflow | 169 units | **187 units** | `getBBox()` against `viewBox` |
| **SYS-B** the other three | "3–26 units" | **28 / 39 / 29** | all three exceed the stated ceiling |
| **Estate positives** — "used up" | 0 | **22** — and **not one asserts it** | every instance is a distractor, a "Think again" quotation, a Key fact saying energy is *never* used up, or a criterion crediting *"the energy is not used up"*. The substantive claim is stronger than the zero suggested; the count as printed is simply wrong, and a re-run will get 22 |
| **Estate positives** — `10 N/kg` | ×49 | **×39** rendered (47 in source) | text sweep |
| **Estate positives** — SYS-1 | "every card reads Connects to" | **59 of 70** lessons carry a card at all | the SYS-1 verdict (ABSENT) is unaffected |
| **§1** safety rulings | "of which 8 are safety wording" | **one item (M1), covering eight units** | the 8 counts units inside M1, not items in §6 |
| **§1** Group A list | "…and two motor redraws" | **the Sun–Earth force pair, and the motor's circuit and brushes** | Group A holds one motor item; the motor *redraw* is item 17, in Group B |
| **M1** | "(`springs-and-hookes-law`, P1)" | **P4**, and it is the only physics lesson with a `safety_note` | 11 of 12 physics units have none, not 8 of 12 — which strengthens M1 |
| **§3** | "(§4, XU-2)" | XU-2 is in **§5**, at the head of P9 | dangling cross-reference |
| **SYS-R** word totals | 92,585 words / 1,322 per lesson | **~89,000–99,000** depending on the rule | see below |

**SYS-R's method is incomplete and its word figures do not reproduce.** Run
exactly as stated (`<p>` only, seven classes excluded) gives **99,319 words, mean
12.9, median 10, p90 28**. The missing step is *counting only segments ending in
terminal punctuation*, which drops ~1,850 caption fragments; under that rule the
**sentence** statistics reproduce almost perfectly — **mean 15.8, median 13, p90
30, and 151 sentences of 42+ words against the 152 claimed**. So the entire `>30`
and `>40` per-unit table, the P10-versus-P3 ratio and the 152 headline all stand
and were independently confirmed; only the **words-per-lesson** column and the
92,585 total are unreproducible, and they are consistently ~7% low. Nothing in the
finding's substance turns on them.

### 9.5 · SYS-3: the three struck auditors were wrong, and the strike is upheld

This was the most contested item and it was tested both ways on all 70 lessons at
a true 390px device-metrics override.

| Test | Pages flagged |
|---|---|
| `getBoundingClientRect()` box intersection — the test P11, P4 and P8 used | **0 of 70** |
| `brand.x + brand.scrollWidth > trail.x` | **70 of 70** |
| `Range` over the wordmark's text node vs `trail.left` | **70 of 70** |

**The false negative is total and reproducible.** `document.documentElement.scrollWidth`
is exactly **390** on all 70 pages, so no document-overflow sweep fires either;
`.ks3-brand` computes to `overflow: visible`, `flex-shrink: 1`, `min-width: 0px`
on every page; and its content needs **177px** on every page, exactly as stated.
The three struck probes were measuring the one thing that cannot see this defect.

The strike paragraph's own per-page figures are **exact**: P11
`temperature-and-internal-energy` box **52.6px**, overprint **98.4px**; P4
`what-a-force-is` **34.2px**; P4 `air-and-water-resistance` **53.2px**; and all
**seven** P8 lessons collide (45–76px). **The strikes are correct and stand.** Only
the summary table's magnitudes were wrong, and they have been corrected above.

### 9.6 · Two things the original pass got right, and one it aimed at the wrong target

**SYS-8 Form 1 is right, and the prose-matching was flawless.** The report treats
P4's hook figures as the best of three imperfect measurements. They are not
imperfect. The `phenomenon` block in `ks3_data` carries an integer `answer`
alongside its options, so ground truth is directly readable. Reading it across all
70 lessons resolves **62** — and the 8 that do not resolve are **all of P1**, whose
hook is shaped differently, not a scattered 8 — giving **A 13 · B 32 · C 13 · D 4,
B on 51.6%**. That is **identical, to the last finding**, to P4's prose-matched
result, including "B on 7 of P4's own 9 lessons", P2 5/5, P7 6/7, P9 3/3 and P8's
6-of-7 skew to A. The finding needs no hedging.

⚠️ **But its proposed solution 1 would not fix the stated problem.** It asks to
*"give the hook an explicit `answer` index in `ks3_data`"* — and that index is
**already there**, on 62 of 70 lessons. Nothing needs authoring. The real gap is
that `build_ks3.py` does not emit it and `verify_answer_positions.py` never reads
it. The fix is to point the existing gate at the key that already exists, plus
reshaping P1's eight hooks. That is much less work than the solution implies.

**One measurement the original pass did not take:** on those same 62 hooks the
correct option is **uniquely the longest 29 times — 46.8%**, against 35.1% in the
bank and 25% by chance. **The hooks are live on the pages today and the bank is
not.** Form 2's authoring remedy should start with the hooks.

**P4-08 is right and is bigger than P4.** All 70 ladders were read from source.
Estate-wide the position is healthy (recall 22/12/24/12, apply 11/24/12/23), which
is exactly why the pooled check sees nothing — but **P2, P5 and P4** each place
every recall answer in {A, C} and every apply answer in {B, D}, and **P2's and
P5's alternations are cleaner than P4's** (perfect, with no break; P4 breaks at
lesson 9). Three units, not one. The per-rung scope must run per unit per rung.

### 9.7 · Verdict, reached independently

**I agree with "yes for reading, no for trusting", and after checking it myself I
would put the emphasis harder on the second half.**

What this estate does well is not in doubt and I confirmed the best of it from
scratch: 83 of 83 pages byte-identical to production, not one broken link in
1,399, not one console error on 83 pages, and — against a slop list twice the size
of the one the auditors used — not one line of generated-sounding prose in ninety
thousand words. The stores-and-transfers model holds, and the pages that quote
"used up" quote it *in order to demolish it*. The convention notes that confess
their own simplifications are better than most published KS3 material. A class
could be sent to any of these seventy pages tomorrow and would learn from them.

The reason that is not enough is the shape of what is wrong. **The serious defects
are concentrated in the instruments, and the instruments are the part a child
trusts most.** I drove seven of them myself and every one behaved perfectly while
demonstrating the negation of the lesson beside it: a prism whose every colour
bends the wrong way and in the wrong order, on the page built to kill that exact
misconception; a thermal bench where the spark beats the bath 2.5 to 1, directly
above a paragraph saying the spark has almost no energy; a Brownian bench where a
pollen grain and a fat droplet jiggle identically, beneath a paragraph explaining
why size decides everything; a distance–time bench that draws the faster line
shallower, on the page whose one idea is that steepness is speed. **None of these
is a bug in the ordinary sense.** The code is correct, the arithmetic is
internally consistent, and no gate in the repo can see any of them — which is why
they shipped and why they will ship again unless the build assertions the auditors
propose land with the fixes.

The double-check moved one thing in the wrong direction. **XU-1 is worse than
filed**: the estate does not teach the right definition of temperature first, it
teaches the wrong one first, in a Year 7 marking criterion, in a chemistry unit
neither the chemistry audit nor this audit's first pass caught. Three of the four
sites are wrong; two of them mark against the correct answer. A child can be
marked wrong for being right, twice, in two subjects, in two different years.
**That is the finding I would fix first**, and it is small — seven sentences.

Against that, the counting is honest and the method is sound. I recomputed all
296 findings from the records and every step of the arithmetic reproduced; I
re-derived twelve independent estate-level measurements and all twelve came back
right; the em-dash tell, the 840-question length bias, the hook positions and the
whole per-unit reading-load table reproduced to the decimal by methods the
auditors did not use. The report's corrections are almost all *understatements* —
overflow magnitudes too large, a stranded-vocabulary total slightly off, a "used
up" zero that is really twenty-two harmless mentions. **I found nothing inflated
in a self-serving direction**, which is the failure mode I was looking for hardest.
The one place two findings contradicted each other, the report's own systemic
measurement was the one that was right.

**September-ready, on my own reading:** ship it for reading, and treat F1 + F2 as
genuinely blocking. **F1 is not a week's polish, it is the difference between a
site that teaches and a site that teaches falsehoods with a straight face** — and
because the falsehoods live in instruments rather than sentences, no student will
ever suspect them and no teacher will catch them in marking. **Do XU-1 and the
seven benches first, add the build assertions with them, and fix SYS-3 in the same
run** — it is two CSS rules and it currently makes every page in the estate
illegible in its top-left corner on the device half the audience uses. Everything
after that is quality, and quality can take the autumn term.

---

*Consolidated from twelve unit records and one cross-unit pass, 28 August 2026.
Every count in this report was recomputed from the records by ID. Per-finding
evidence — driven DOM states, screenshots, measured geometry, quoted source —
lives in `records/p1.md` … `records/p12.md` and `records/cross-unit.md` under the
same identifiers.*
