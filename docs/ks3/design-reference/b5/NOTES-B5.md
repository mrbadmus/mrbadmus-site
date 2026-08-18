# B5 — Reproduction · author's notes

**Eight of eight lessons authored.** The unit is complete for the first time.
Draft — nothing here has been science-reviewed. Flags are numbered so they can
be answered by number, and flags 1–13 are carried over unchanged from the
partial-unit version so that numbering stays stable.

Queue resolution and filename convention are in `NOTES-P3.md` §0 and apply
unchanged: slugs are verbatim from `structure.py`.

---

## 0. What exists

| Lesson | Type | Status |
|---|---|---|
| `b5-01-human-reproductive-systems` | SYSTEM | authored |
| `b5-02-gametes-and-fertilisation` | PROCESS | authored |
| `b5-03-the-menstrual-cycle` | PROCESS | **new** |
| `b5-04-gestation-placenta-and-birth` | PROCESS | **new** |
| `b5-05-lifestyle-and-the-developing-foetus` | SYSTEM | **new** |
| `b5-06-flowers-and-pollination` | SYSTEM | **new** |
| `b5-07-fertilisation-seeds-and-fruit` | PROCESS | **new** |
| `b5-08-seed-dispersal` | CLASSIFY | **new** |

**One filename correction.** The previous notes called lesson 4
`gestation-the-placenta-and-birth`. `structure.py` says
`gestation-placenta-and-birth`, without the article, and the convention is that
the generator wins — so the file is `b5-04-gestation-placenta-and-birth` and
every inbound link in the unit uses that. The register entry has been corrected
to match.

Statutory position: `KS3.B.REP.01` (human reproduction) is now **fully
covered** — systems, gametes and fertilisation, menstrual cycle without hormone
detail, gestation and birth, and the effect of maternal lifestyle on the foetus
through the placenta. `KS3.B.REP.02` (plant reproduction) is covered for flower
structure, wind and insect pollination, fertilisation, seed and fruit formation
and dispersal — **except the clause requiring quantitative investigation of some
dispersal mechanisms, which is not covered anywhere.** That is flag 43 and it is
the one coverage decision I would want answered.

---

## 1. Family patterns as applied

- **SYSTEM (b5-01)** — a *match the function* instrument rather than a labelled
  diagram, deliberately. Then five jobs read down a column, where three of the
  five fall to one system only. The asymmetry is the content.
- **PROCESS (b5-02)** — a six-row comparison of two specialised cells with a
  *why* behind each row, then five numbered steps with step 3 visually promoted,
  because step 3 is the only one that is fertilisation.
- **PROCESS (b5-03)** — the instrument is a control the student sets rather than
  a thing they answer: change the cycle length and the release day moves. Then
  four events, with *release* promoted.
- **PROCESS (b5-04)** — commit-then-check on six substances crossing a surface,
  then five stages of the pregnancy with *the exchange surface is built*
  promoted rather than birth, because the supply line is what everything else
  depends on.
- **SYSTEM (b5-05)** — the same commit-then-check shape as b5-04, deliberately,
  because the lesson's whole argument is that the crossing rule from the
  previous lesson does not change when the substance is a harmful one. Then a
  three-row timing table with weeks 3–8 promoted.
- **SYSTEM (b5-06)** — b5-01's instrument in a plant: nine parts, nine jobs, four
  options each drawn from a shared pool. Then insect and wind read down a
  column, five features.
- **PROCESS (b5-07)** — a before/after transformation table (tap a row for the
  *why*), then five numbered steps with fertilisation promoted, exactly
  mirroring b5-02 so the plant and the animal sit in the same shape.
- **CLASSIFY (b5-08)** — eight specimens described only by structure, sorted into
  five methods, checked one at a time with the deciding feature named. Then the
  five methods read down a column against what each costs the plant.

---

## 2. New instruments

All six are DOM-only. Nothing in this unit animates, nothing uses a timer, and
there is no canvas.

### 2.1 `cycle-dial` — flagship of `b5-03`

- **Controls:** three cycle-length chips (21 / 28 / 35), a day slider, and −/+
  day buttons for keyboard and small screens.
- **Readouts:** a track showing the bleeding window, the release day and the
  current day; two panels reading *in an ovary* and *in the uterus*; a note that
  changes with the chosen length.
- **Payload:** `{lengths: [21,28,35], luteal: 14, shed: 5, length, day, seen: {}}`.
- **Note for Code:** the release day is derived as `length − 14`, never stored.
  That is the instrument's whole argument, and hard-coding release days would
  destroy it. Rail credit is given for viewing **two different lengths**, not for
  reaching the end of the slider.

### 2.2 `crossing-bench` — flagship of `b5-04`

- **Controls:** six substance tabs, a two-way direction commit, *check it*.
- **Readouts:** verdict, the direction in a sentence, and a *why* that always
  names the concentration difference.
- **Payload:** `{subs: [{id, label, name, kind, dir, context, answer, why}], picks: {}, opened: {}}`.

### 2.3 `crosses-panel` — flagship of `b5-05`

- **Controls:** six substance tabs, a yes/no commit, *check it*.
- **Readouts:** verdict, answer, *why*, plus a 0–40 week bar showing when that
  exposure matters most and a sentence explaining the bar.
- **Payload:** `{subs: [{id, …, crosses, win: [startPct, endPct], winText}], picks: {}, opened: {}}`.
- **Note for Code:** five of the six cross and one does not. That imbalance is
  the teaching point — the rule is about molecule size — so do not "balance" the
  set.

### 2.4 `flower-jobs` — flagship of `b5-06`

- **Controls:** nine part tabs, four job options each, *check it*.
- **Payload:** `{jobs: {9 strings}, parts: [{id, label, name, group, answer, options: [4 keys], why}], picks: {}, opened: {}}`.
- **Note for Code:** same rule as b5-01. Every distractor is the correct job of a
  different part, drawn from the pool of nine. Inventing wrong answers destroys
  the instrument's second purpose.

### 2.5 `what-it-becomes` — flagship of `b5-07`

- **Controls:** six expandable rows (tap anywhere on the row).
- **Readouts:** a three-column before/after table plus a *why* per row.
- **Payload:** `{rows: [{id, name, before, after, why}], open: {}}`.
- **Design note:** the whole row is the button, as in `gamete-compare`. No
  separate chevron control.

### 2.6 `disperse-sort` — flagship of `b5-08`

- **Controls:** eight specimen tabs, five method options, *check it*.
- **Readouts:** verdict, the method, a *why*, and a separate **deciding feature**
  line — the observable that settles it.
- **Payload:** `{methods: {5 labels}, specimens: [{id, label, name, answer, desc, tell, why}], picks: {}, opened: {}}`.
- **Note for Code:** the specimens are described by structure only and never
  pictured or named in the description text, so the sort has to be done on
  evidence. Three of the eight are wind-dispersed and one of those three (poppy)
  has neither wing nor parachute. That is the instrument's hard case and it
  should not be softened.

---

## 3. Science flags — numbered for review

### Lessons 1–2, carried over

1. **~1 million immature egg cells at birth, ~400 maturing in a lifetime**
   (b5-01 hook and think-again). Commonly quoted; the birth figure is given as
   1–2 million in different sources. Confirm the figures and the rounding.
2. **"Around a thousand sperm per second."** Standard figure (~1500/s, or 200–300
   million a day). Confirm the rounding down.
3. **Egg 0.1 mm, sperm head 0.005 mm.** **RESOLVED, 15 Aug** — the hook says
   "several thousand times", consistent with the arithmetic the lesson itself
   gives. Confirm you are happy with the hedge.
4. **"Fertilisation happens in the oviduct."** Correct, and the target of
   `REPRO-03`. Confirm *oviduct* as the primary term with *fallopian tube*
   parenthetical.
5. **The egg remains fertilisable for "roughly a day"** (b5-02 step 1, and reused
   in b5-03). Usually given as 12–24 hours. Confirm.
6. **"Hundreds of millions set out; a few hundred arrive"** (b5-02 step 2).
   Widely quoted. Confirm.
7. **Implantation at about five days, and "this is where pregnancy begins"**
   (b5-02, and now load-bearing in b5-04). Clinical rather than purely
   biological definition, stated flatly. Confirm you want it at KS3.
8. **The outer layer changing to exclude further sperm** (b5-02 step 3). Confirm
   the level of detail.
9. **Maternal mitochondrial inheritance and the molecular clock** (b5-02
   stretch). Confirm, including the simplification that the sperm's
   mitochondria are destroyed after fusion.
10. **Testes outside the body at ~34 °C, with the undescended testis note**
    (b5-01 stretch). Confirm the temperature and the named clinical condition.
11. **The penis described as also carrying urine** (b5-01). Confirm.
12. **Glandular fluid containing sugar for the sperm to respire** (b5-01 rung 4,
    b5-02 row 4). Confirm the depth.
13. **No diagrams anywhere — now ten named slots, none in the manifest.**
    `b5-male-system-labelled`, `b5-female-system-labelled`,
    `b5-gametes-labelled`, `b5-cycle-timeline`, `b5-placenta-exchange`,
    `b5-what-crosses`, `b5-flower-parts-labelled`, `b5-wind-vs-insect`,
    `b5-pollen-tube`, `b5-dispersal-specimens`. For this unit the
    labelled-diagram question is not only a sourcing one — please confirm what
    you want illustrated and at what level of detail before anything is
    commissioned. The plant slots are the easiest to source and the human ones
    are not.

### b5-03 · The menstrual cycle

14. **The whole arithmetic of the lesson: release day = cycle length − 14.** The
    interval from release to the next period is the steadier one and is usually
    given as 12–16 days; the lesson rounds it to "about a fortnight" and derives
    the release day from it. **This is the lesson's central claim and it needs
    confirming**, including whether deriving a day arithmetically is acceptable
    at KS3 rather than simply teaching a range.
15. **Three fixed cycle lengths (21 / 28 / 35) rather than a free slider.** The
    fixed set makes 7 / 14 / 21 visible at a glance; a free slider would be more
    honest about the messiness. Confirm the choice.
16. **Days 1–5 as the bleeding window.** Commonly given as 2–7 days. Confirm.
17. **No hormones anywhere**, per `KS3.B.REP.01`. The lesson still has to say why
    the lining is maintained and then breaks down, and it does so with *held
    ready* and *no longer held*, naming nothing. **Confirm that vagueness is
    what the exclusion means**, rather than the softer reading that allows
    "chemical messengers" without naming them.
18. **"One person's own cycles vary between themselves."** Correct and important,
    and it is the part of the misconception most often left out. Confirm.
19. **The Going further cites daily-temperature, hormone-test and app-data
    studies without quoting a figure.** Deliberate — every figure I could quote
    dates or is disputed. Confirm the unquantified form.

### b5-04 · Gestation, the placenta and birth

20. **Antibodies described as actively carried across, using energy**, in
    contrast with everything else on the list. Correct. Confirm the depth.
21. **"Foetal haemoglobin holds oxygen more tightly than the adult kind."** One
    sentence, correct, and it is really GCSE material — but it is what keeps the
    gradient up and the lesson is about gradients. Confirm.
22. **Urea leaves via the placenta although the foetus does make urine into the
    amniotic fluid.** Both stated. Confirm the simplification.
23. **"Pregnancy is dated from the first day of the last period, so forty weeks
    is about two weeks longer than the time the foetus has existed"** (legal
    line). Accurate, and the kind of detail that confuses if half-stated.
    Confirm you want it.
24. **The Going further calls immune tolerance of the foetus an open research
    question.** It is. Confirm you are happy to end a lesson on something
    unresolved.
25. **Birth is one card: contractions, cervix opening, delivery, cord cut,
    placenta delivered.** No pain, no intervention, no caesarean, no mention of
    what can go wrong. That is a deliberate scope decision and it is
    reviewable — a Year 8 class will ask.

### b5-05 · Lifestyle and the developing foetus

26. **The six crossing claims as a set** — alcohol, carbon monoxide, caffeine,
    rubella, prescribed medicines, insulin. Each is standard; they have not been
    checked against a single current source together. **Please review these six
    as one block.**
27. **"Under about 200 mg of caffeine a day, roughly two mugs of instant
    coffee."** UK guidance figure; the mug equivalence varies a great deal by
    preparation. Confirm the figure and whether to keep the mug comparison.
28. **The second Think again is not a science misconception — it is an
    attribution error** ("so anything that goes wrong is the mother's fault").
    It names second-hand smoke, pollution, infection, medicines that must be
    continued, constrained food choices, addiction as a condition, and
    unexplained complications, and it ends on risk being a population
    statement. **This is the most significant editorial decision in the unit and
    I want it confirmed explicitly, wording included.** It is also, in my
    judgement, the paragraph that makes the lesson safe to teach.
29. **Thalidomide in Going further** — sold from 1957, McBride and Lenz, withdrawn
    1961, the few-week window that mapped limb development, and its controlled
    use today. Confirm the dates and confirm a named disaster is acceptable in a
    stretch layer here.
30. **Nothing in the lesson addresses the reader as pregnant or as a future
    parent**, and there is no second person anywhere near the exposures. Also
    deliberate: the lesson is about a placenta, not about the class. Confirm.

### b5-06 · Flowers and pollination

31. **Nine parts including the nectary as a part in its own right.** Not every
    textbook does that. Confirm.
32. **"Some petal patterns are visible only in ultraviolet, which bees can see."**
    Correct. Confirm it is worth the sentence.
33. **Darwin's orchid** — 1862 prediction, moth named *praedicta* in 1903, first
    filmed feeding about ninety years after that. Confirm the dates and the
    rounding.
34. **"Wind-pollinated species include a large share of what the world eats."**
    True by way of the grasses. Confirm the unquantified form.

### b5-07 · Fertilisation, seeds and fruit

35. **Double fertilisation and endosperm** (Going further). Correct for flowering
    plants and genuinely striking. Confirm it is not too much for a stretch
    layer at KS3.
36. **"White flour is very nearly pure endosperm."** Correct. Confirm.
37. **Pollen tube timing "hours in some plants, months in some trees."** Correct
    (oak). Confirm.
38. **The fruit/vegetable Think again** names carrot as root, potato as stem,
    celery as leaf stalk, and includes the wheat grain as a fruit. The wheat
    grain is the one most likely to be challenged, since the fruit wall is fused
    to the seed coat. Confirm you want it included.

### b5-08 · Seed dispersal

39. **The eight specimens and their five categories**, especially **poppy as
    wind** by the censer mechanism. It is the deliberate hard case and it is the
    one a marker might get wrong. Confirm.
40. **The burdock and Velcro story** — de Mestral, 1941, patented in the 1950s.
    Confirm the dates.
41. **"On a dry breezy day some dandelion seeds travel a kilometre."** Widely
    quoted; most travel a few metres, which the Going further then says.
    Confirm the pairing.
42. **Dispersal distances measured by genotyping adult trees and seedlings**, and
    the claim that the long tail matters more than the average. Correct, and it
    is the strongest *how do we know* in the plant half. Confirm the level.
43. **`KS3.B.REP.02` requires "quantitative investigation of some dispersal
    mechanisms" and nothing in this unit measures anything.** b5-08 is a
    CLASSIFY by family and does not carry a practical. Either it gains one — the
    obvious candidate is timing the fall of paper sycamore models against wing
    length — or the gap is accepted and recorded. **This is a coverage decision,
    not an authoring preference, and I would want it answered before the unit is
    signed off.**
44. **The teleology paragraph** (b5-08 Think again 1) attacks *so that*, *wants*
    and *tries*, and rung 3 marks a student down for using them. Confirm that is
    the right hill at KS3; it costs a paragraph and it is the reason the rest of
    the unit reads the way it does.

---

## 4. Tone — what was decided, and what still needs review

The previous notes stopped the unit here and asked for the tone treatment to be
reviewed before six more lessons were written to match it. The instruction to
build the rest of B5 has been taken as authority to proceed on the established
treatment, so that is what lessons 3–8 do:

- **Clinical and function-first.** Anatomical names used plainly, no euphemism.
- **No explicit sexual detail beyond the statutory level.**
- **No assumptions** about family structure, and no normative language.
- **Sex and gender are not conflated.** The lessons say *male system* and *female
  system* — properties of organ systems — rather than making claims about people.
- **Every lesson in the human half closes with two signposts:** RSE/PSHE for
  relationships and consent, and a trusted adult, school nurse, doctor or
  midwife for anything personal.

**What is new and needs review as tone rather than as science:**

- **b5-03** never addresses the reader as someone who has cycles. It describes
  *a person's* cycle throughout. Confirm that is right for a mixed class.
- **b5-04** stops at the biology of birth and does not go near pain, choice or
  intervention (flag 25).
- **b5-05** is the one the previous notes were most worried about, and the answer
  it takes is: make the lesson about the placenta rather than about mothers.
  Every exposure is framed as a molecule crossing a surface; the anti-blame
  paragraph is explicit (flag 28); the thalidomide stretch puts the historical
  failure on regulators and testing rather than on any individual; and the legal
  line says in terms that risk is not a verdict on a person. **If any part of
  this unit is going to attract a complaint it is this lesson, and I would
  rather you read it whole than review it by flag.**

---

## 5. Misconception register — `REPRO` family, now seventeen entries

`REPRO-01` to `REPRO-17`, written into `docs/ks3/misconception-register.md`.
Twelve new entries, minted as their lessons were written, per the register's own
rule. The two entries previously **noted without IDs** now have them:

- *Pollination and fertilisation are the same thing* → `REPRO-14`, owned by
  `fertilisation-seeds-and-fruit`.
- *The baby's blood mixes with the mother's blood in the placenta* → `REPRO-08`,
  owned by `gestation-placenta-and-birth`.

`REPRO-11` is unusual for the register and is flagged as such in the file: the
statement it confronts is a reasoning error about attribution rather than a
factual error about biology. It is included because it is what a class will
otherwise take away from b5-05.

`FORCE`, `BODY` and `ATOM` remain unminted and are not cited anywhere in this
unit.

---

## 6. For Code

- Six new instruments in §2, all DOM-only.
- Rail stops: four in every lesson in the unit.
- **The dangling link is gone.** `b5-02` pointed forward to
  `b5-03-the-menstrual-cycle.html`, which now exists. Every inbound and outbound
  link in the unit resolves, with one convention to note: lesson 4 is
  `b5-04-gestation-placenta-and-birth.html`, matching `structure.py` rather than
  the previous notes.
- Outward links now go to `b1-04`, `b3-07`, `b4-03`, `b6-01`, `b6-02`, `b6-03`,
  `b9-04`, `b10-02`, `b11-01` and `b11-02`. All of those lessons exist.
- b5-05 reuses b5-04's instrument shape deliberately (§1). If Code refactors
  either one, keep them identical — the repetition is the argument.
