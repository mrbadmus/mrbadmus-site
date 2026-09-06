# MRB-332 — findings that need Mide

Everything else in this run was decided under the Autonomy Contract and is
reported in the run summary. These are the items that are genuinely his call,
collected here rather than raised mid-run.

---

## 1. ⚠️ SCIENCE / SPEC ACCURACY — eleven KS4 lesson pages teach HT-only content as BASE

**This is the important one, it is examiner territory, and it predates MRB-332.**

Two cold science reviewers, working independently on different files, each
found that **Foundation-flagged KS4 lesson pages** teach material AQA 8463
marks Higher-tier-only, Physics-only, or does not teach at all. Eleven in
total. The
assignment questions were authored to those pages, as instructed, so the
questions faithfully reflect what the page teaches — which means the exposure
is on the pages, not on the pool.

| # | content | AQA status | page that teaches it as BASE | questions reached |
|---|---|---|---|---|
| 1 | Non-collinear resultants (Pythagoras) | HT **and** Physics-only | `scalar-vector-quantities`, `resultant-forces` — both print "FORCES AT RIGHT ANGLES: use Pythagoras" | `ks4-scalar-vector-quantities-s04`, `ks4-resultant-forces-s04`, `-h04` |
| 2 | Area under a velocity–time graph | HT-only (§5.5.4.1.6) | `acceleration` — teaches it with a worked triangle+rectangle | `ks4-acceleration-s02`, `-h01`, `-h04` |
| 3 | Ee = ½ke² | HT-only | `forces-elasticity` | `ks4-forces-elasticity-h01` |
| 4 | Braking force from ½mv² | HT-only | `stopping-distance-braking` — prints `F × d = ½mv²` | `ks4-work-done-energy-transfer-h04` |
| 5 | Change in momentum, `F = Δp/t` | **Physics-only** (§5.5.5.3) | `momentum` is flagged `tier='higher', triple_only=False`, so a **Combined Higher** class sits it; the page teaches impulse, crumple zones and air bags in full | `ks4-momentum-s04`, `-h03` |

A second reviewer, working independently on Energy, Electricity and Particle
Model, found the same pattern again — six more:

| # | content | AQA status | page that teaches it as BASE |
|---|---|---|---|
| 6 | `Vp/Vs = np/ns` (the transformer equation) | HT-only **and** Physics-only | `national-grid`, flagged BASE, teaches it with a worked example |
| 7 | `E = F/q`, and N/C as a unit | **not in AQA 8463 at all** | `electric-fields` teaches both |
| 8 | `pV = constant`, and the pressure/temperature relation | HT-only; the p/T relation is not in AQA | `particle-motion-pressure`, flagged BASE — the whole subtopic |
| 9 | peak vs effective mains voltage (325 V), rms | AQA does not teach rms | `direct-alternating-pd` |
| 10 | "deposition" as the name of a state change | AQA never uses the term | `changes-of-state-e01` keys it, because the page teaches it |
| 11 | W/m·K as a unit | not required by AQA | `thermal-conductivity` prints it |

**Neither reviewer rewrote any of these, and that was the right call.**
Rewriting the questions would put a child's homework out of step with the page
they revise from — the worse of the two failures. The mismatch is between the
site's own curriculum data and AQA, not between the questions and the pages.
The fix, if you want one, is on the page or on the flag, and it is a content
ruling.

**Two I would look at first:**

- **Item 5 (momentum, `F = Δp/t`)** is not a tier question but a *pathway*
  question: a Combined Higher class currently sits questions built on a
  Physics-only spec point.
- **Item 8 (`particle-motion-pressure`)** is a whole BASE subtopic — twelve
  questions — resting on an HT-only relationship, so it is the largest single
  exposure.

**Nothing is blocked on this.** The questions ship as they are unless you say
otherwise; they match the pages today, and a student revising from the page
will be able to answer them.

### The upside, for balance

Both reviewers checked the reverse direction too and found **no leak**: nothing
Higher-only or Triple-only appears in a BASE question *except* where the page
itself teaches it. Two real tier breaches were found and fixed — a keyed answer
in `properties-em-waves-1-h02` that used the HT-only wave-front explanation of
refraction, and an HT radio-wave-production distractor in `types-of-em-waves-e04`.

---

## 2. ⚠️ SCIENCE / SPEC — two subtopics may be flagged Triple-only when AQA Trilogy teaches them

Found by the Rainford KS4 mapping, and it cuts the opposite way to finding 1 —
this would deny Combined students content they are entitled to.

`meiosis` and `classification-living-organisms` are flagged `triple_only=True`
on the platform. Rainford teaches both **unprefixed**, i.e. to everyone, and
the mapper's reading is that AQA Trilogy covers both.

This matters here because the flags are DERIVED from
`generate_site_v5.PATHWAY_TOPIC_MAP` — the same source the scheme of work is
built from — so if the map is wrong, the pool inherits the error and a
Combined class is refused questions it should be served. Nothing was changed:
`PATHWAY_TOPIC_MAP` is pre-existing platform data and outside this ticket.

If you confirm AQA Trilogy teaches them, the fix is one edit to
`PATHWAY_TOPIC_MAP` and a re-run of `ks4_seed_sow.py` and the export — the
pool needs no re-authoring, because the flags are computed rather than typed.

---

## 3. ⚠️ A real hole in Year 11 Biology — about a fortnight with no platform page

The Rainford KS4 mapping found eight lessons the school teaches that the
platform has no page for at all. Six of them are one contiguous gap:

| Rainford lesson | AQA |
|---|---|
| Y11 Bio L95 — Removing waste product w/ deamination | 4.5.3.4 |
| Y11 Bio L96 — Kidney & ADH | 4.5.3.4 |
| Y11 Bio L97 — Kidney failure | 4.5.3.4 |
| Y11 Bio L101 — Plant Hormones | 4.5.4 |
| Y11 Bio L102 — Growth of seedling RP | 4.5.4 |
| Y11 Bio L103 — Growth of seedling RP2 | 4.5.4 |

Plus two singletons: Y10 Bio L32 *Breathing & gas exchange* (4.2.2.3, the
lungs) and Y11 Chem L80 *(CHEM) Gas Calculations* (4.3.4.3, molar gas volume).

Osmoregulation and plant hormones are examinable AQA content. They have no
lesson page, so they also have no assignment questions — this pool cannot
cover what the curriculum data does not contain.

---

## 4. ⚠️ The lesson pages publish each subtopic's whole examinable core, already paired

This one is structural, and it limits what a twelve-question homework set can
ever be.

Every KS4 lesson page carries a `matching` block, and it is printed **already
paired** — it is effectively a glossary of that subtopic's examinable content.
Three independent cold reviewers hit the same wall: a *recall* question on a
saturated subtopic is answerable by reading one line the page publishes.

The Waves and Magnetism reviewer put it plainly after checking all seventeen of
its subtopics: **this is not a handful of thin cases at the margin, it is how
every page is built.** Four subtopics had no honest alternative at all —

| subtopic | what the matching block publishes |
|---|---|
| `properties-of-waves` | a five-line glossary of amplitude, wavelength, frequency, period and wave speed — the whole of 6.6.1.2 |
| `uses-em-waves` | five pairs that *are* AQA's named use list |
| `transverse-longitudinal-waves` | every standard example already sorted into transverse/longitudinal — which is the identification task itself |
| `loudspeakers-headphones` | every component's role, so the construction is fully published |

plus `uses-of-nuclear-radiation`, `stellar-evolution`, `poles-of-a-magnet`,
`resistors`, `mains-electricity`, `changes-of-state`, `internal-energy` and
`electromagnetism` from the other reviewers.

**Now measured, not estimated.** I extended `pool_ownership.py` to compare each
question's stem *and its keyed option* against both halves of every matching
pair. Across the whole authored pool:

> **447 questions, in 164 of the 264 subtopics, examine a fact the lesson page
> already prints paired.** That is about one question in six.

Worst affected: `mass-number-isotopes` (10 of 12), `subatomic-particles` (9),
`forces-elasticity` (9), `structure-of-atom` (8), `nuclear-equations` (8),
`electronic-structure` (7), `chemical-bonds` (7), `percentage-yield` (7).

The gate reports this figure on every run and never fails on it, so the number
stays visible and moves if the pages change.

**A second, sharper measure — and three questions I ruled on.** A cold reviewer
noticed that string similarity cannot see a task that is *semantically* the
same but worded differently: "Name the two elements that bronze is made from"
against the page's "name the two metals mixed together to make bronze" scores
0.59, comfortably under any workable threshold. What such pairs share is not
their wording but their ANSWER. So the gate now also flags a pool question
whose keyed answer matches a published question's answer **in the same
subtopic**.

Estate-wide that finds **three** questions out of 3,168 — it independently
rediscovered the two the reviewer had found by hand, and added one it had not:

| question | subtopic |
|---|---|
| `ks4-metals-alloys-e01` | bronze = copper + tin |
| `ks4-metals-alloys-e03` | what an alloy is |
| `ks4-properties-small-molecules-e02` | state at room temperature |

**I ruled that all three stay.** They are the saturated case this section
describes, not carelessness. `metals-alloys` publishes twelve quiz tasks plus a
five-row matching block covering the alloy definition, the hardness mechanism,
bronze, steel, stainless steel and the aluminium-aircraft case;
`properties-small-molecules` publishes nineteen tasks and five pairs against a
one-sentence spec statement. Each question examines a printed *fact* — which
the TASK/FACT line permits — and every alternative the reviewer drafted
collided with a published *task*. Rewriting them would have traded a permitted
fact for a forbidden task, or left the spec.

Three in 3,168 is the residue, and it is small. But it is the clearest single
illustration of finding 4: where a page publishes everything, homework has
nowhere left to stand.

**How I ruled it, so the run could finish.** I drew a line in
`docs/ks4/pool-authoring.md` §2: **a published TASK may never be reproduced; a
published FACT may be examined.** A `quiz` question and a worked `fifas`
example are tasks printed with their answers — off-limits, numbers included. A
`matching` pair is a fact, and where the lesson has published the whole spec
point, examining it is correct; inventing an off-spec question to dodge it is
the worse defect.

That ruling immediately proved itself: one reviewer had already rewritten
eighteen questions to dodge pairings, re-audited them against the line, and
**reverted six** because its own substitutes had left the AQA spec — an
amplitude→energy question where amplitude-and-energy is not in 6.6.1.2, a
"digital camera sensor" where AQA names the remote control, a vitamin-D fact
where AQA names MRI.

**What is actually yours to decide:** whether the lesson pages should publish
quite so much, already paired. Nothing is blocked either way — the questions
ship as they stand — but if a matching block is meant to be a revision aid
rather than an answer key, that is a page-design ruling, and it would widen
what homework can ask.

---

## 5. ⚠️ SCIENCE ERROR in a lesson page's own "common mistake" field

Found by the ecology author, which declined to write the question the brief was
steering it toward. I have verified it against the source.

`all_subtopics_biology_triple_higher.py`, the `pyramids-of-biomass` record,
`common_mistake` field:

> "Pyramids of BIOMASS are almost always true pyramid shapes — **the ONE
> exception can occur with parasites** (many small parasites on fewer large
> hosts). Pyramids of NUMBERS can be inverted (e.g. one tree → many insects)."

**That is the wrong way round.** Many small parasites on fewer large hosts
inverts the pyramid of **numbers**, not of biomass — the total biomass of the
parasites is far *less* than the biomass of their hosts, which is what makes
parasitism viable at all. The genuine inverted-biomass case is
phytoplankton→zooplankton in open ocean, where the producers' standing biomass
at any instant is smaller than the consumers' because turnover is so fast.

**The same page already knows this.** Four lines below, its `higher` field
says: *"Interpret unusual pyramid shapes (e.g. parasites,
phytoplankton-zooplankton in oceans)"* — listing the correct example alongside
the incorrect one. The record contradicts itself.

Why this one matters more than an ordinary slip: `common_mistake` is the field
the authoring brief presents as **the primary source for distractors**, so an
error there propagates into questions as a *keyed answer*. The author caught
it, refused it, and wrote the real textbook case instead (sheep and ticks —
numbers inverted at the top, biomass still a true pyramid). Had it not, this
pool would now teach the misconception as fact.

**I have not changed the lesson page.** Editing KS4 content is your science
gate and outside this ticket. The pool is clean either way.

---

## 6. Rainford's Year 9 sits under both key stages

Rainford begins KS4 in Year 9, so its Year 9 now has 22 KS3 override rows and
112 KS4 override rows in the same table. That is a legitimate consequence of
the school's own structure and nothing refuses it — but it is a product
question about what a Year 9 class should be offered, and it is yours.

---

## 7. Rainford's KS3 overrides collide with an existing seed

`supabase/seeds/20260726182000_ks3_school_schemes.sql` already claims
**exclusive** ownership of Rainford's KS3 override rows, with the same
school-scoped `DELETE`. The new Rainford KS3 seed claims the same rows. Both
cannot be applied — last one wins, silently.

| | rows | source | shape |
|---|---|---|---|
| existing (MRB-103) | 185 | the unit→year map | platform order, synthetically complete |
| new (MRB-332) | 162 | the school's actual spreadsheet | Rainford's real order, 34 honest gaps |

Neither is wrong; they answer different questions. Nothing was modified —
`ks3_seed_sow.py` and `school_schemes.py` are untouched, and both seeds are on
disk. Your call which one owns Rainford's KS3 rows.

---

## 8. Two genuine platform content gaps at KS3, found by the Rainford mapping

Not scope decisions — things Rainford teaches that the platform has no lesson
for at all:

- **Convection.** P1 has conduction, radiation and insulation, but no
  convection lesson. It appears only as a distractor in a question.
- **The Year 9 disease and immunity strand** — Microbes & disease, Preventing
  transmission, Defence against disease, Vaccination. The word "pathogen"
  appears nowhere in `ks3_data`.

Seventeen further unmapped entries are ordinary scope differences (beyond
statutory KS3, or enrichment) and are listed in
`docs/ks4/rainford-ks3-sow-mapping.md`.

---

## 9. A near-duplicate stem across two subjects

`ks4-changes-of-state-e04` (physics, particle-model) asked *"Describe the
arrangement and movement of the particles in a **gas**"*; the chemistry
`states-of-matter` lesson page prints *"…in a **solid**"*. One word apart, and
a Combined Science student reads both pages.

I ruled this a violation of the standard's §2 (which forbids "light
rewording") and had it rewritten. Recorded here because it is a content
judgement you may want to see rather than one to re-litigate.

---

## 10. Operational — the machine ran out of disk twice

Two agents hit `ENOSPC` mid-run; one had to clear caches to finish. I
reclaimed what was safely mine (`__pycache__` across all worktrees). The large
remaining caches are your own applications — Chrome 2.3 GB, Spotify 949 MB,
Playwright 853 MB — and I left them alone.

There is ~2.6 GB free. Below roughly 500 MB, gates crash in ways that look
like real failures, so it is worth a clear-out before the next long session.
