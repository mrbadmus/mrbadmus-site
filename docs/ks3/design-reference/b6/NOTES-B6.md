# B6 — Health and drugs · author's notes

**Complete unit: three of three lessons authored.** Draft — nothing here has been
science-reviewed. Flags are numbered so they can be answered by number.

Queue resolution and filename convention are in `NOTES-P3.md` §0 and apply
unchanged: slugs are verbatim from `structure.py`.

---

## 0. What exists

| Lesson | Type | Status |
|---|---|---|
| `b6-01-what-drugs-do-to-the-body` | SYSTEM | **authored** |
| `b6-02-alcohol-and-smoking` | SYSTEM | **authored** |
| `b6-03-substance-misuse-and-decisions` | INVESTIGATION | **authored** |

Statutory position: `KS3.B.HLTH.01` is the unit's only statement and is now
**fully covered** — recreational drugs including substance misuse, and their
effects on behaviour, health and life processes. B6 is the worst
statement-to-lesson ratio in biology (1 statement, 3 lessons, 0.33), so the
three lessons divide one clause three ways rather than covering three clauses:
b6-01 takes *what a drug is and what it does to the body*, b6-02 takes the two
legal drugs the statement's "including substance misuse" clause is really about
in a UK school, and b6-03 takes the decisions half — treated as evidence
evaluation, not as a moral lecture.

---

## 1. Tone — the B5 §4 treatment, applied and extended

B5's notes asked for the sensitive-content treatment to be reviewed before more
lessons were written to match it. That review has not come back, so B6 uses the
same treatment, because leaving the unit unwritten looked worse than writing it
consistently with b3-04, b4-04 and B5:

- **Clinical and function-first.** Drugs are named plainly, their effects
  described as biology. No euphemism.
- **No preaching, no scare copy, no reassurance copy.** The reason a student
  should not want a racing heart is that a racing heart is what the drug does,
  not that an adult disapproves.
- **No doses, thresholds or methods** for any substance, legal or illegal.
  b6-01's tracer deliberately shows a route without a quantity.
- **No assumptions about the student's home.** Alcohol at home, smoking at home
  and a relative's use are all live possibilities in any Year 9 class, so
  nothing addresses the reader as someone whose family does not do these things.
- **Every lesson closes with two signposts** in a `ks3-layer ks3-support`
  block: PSHE/RSE for decisions, pressure and the law; and a trusted adult,
  school nurse, pharmacist or GP for anything personal. National services are
  referred to as "the ones listed in your school's PSHE materials" rather than
  named, because a named helpline in a lesson page goes stale and is a
  safeguarding decision rather than an authoring one. **Flag: confirm you want
  them named instead.**

**What I still need from review:** whether that treatment is right for Year 9 in
this school, and whether b6-02's vape paragraph (§3 flag 9) is where you want the
line drawn.

---

## 2. New instruments

### 2.1 `route-tracer` — flagship of `b6-01` (DOM only)

- **Controls:** four drug tabs (caffeine, paracetamol, nicotine, alcohol);
  *take the dose* advancing one stage at a time; *new dose*.
- **Readouts:** five stages revealed in order, then an *and everywhere else*
  panel of three organs with the effect on each, and a verdict line.
- **Payload:** `{drugs: [{id, label, name, klass, where, entry, target, elsewhere: [{organ, effect}], verdict}], step: 0..5}`.
- **Note for Code:** stage 3 — *once round the whole body* — is the entire point
  of the instrument and kills `DRUG-02`. Do not let a future revision collapse
  stages 2 and 3 to save space.

### 2.2 `clearance-clock` — flagship of `b6-02`

- **Controls:** five drinks that add units; six "ways to sober up"; *wait an
  hour*; *empty the glass*.
- **Readouts:** units drunk, hours to clear, a falling blood bar, a note on the
  chosen intervention, and a verdict.
- **Payload:** `{drinks: [{id, label, units}], fixes: [{id, label, note}], units, fix, hour}`.
- **Design note:** the intervention **must not change the number of hours** —
  that is the instrument. The *big meal first* option is the one honest
  exception and it changes the peak, not the clock; its note says so.

### 2.3 `claim-check` — flagship of `b6-03`

- **Controls:** five claim tabs; five faults (radio-style); *check it*.
- **Readouts:** verdict eyebrow, the fault named in a sentence, why, and *what
  would settle it*.
- **Payload:** `{claims: [{id, label, text, evidence, answer, why, settle}], faults: [5], picks: {}, opened: {}}`.
- **Note for Code:** the fault pool works like b5-01's function pool — each of
  the five faults is the right answer for exactly one claim, so every wrong pick
  is still a true statement about evidence. Do not add invented distractors.
- Bench marking follows the house rule: the fault list does **not** turn green
  and red. It highlights the pick; the verdict panel names the answer, as
  `b5-01` does.

---

## 3. Science flags — numbered for review

1. **"A drug is any substance that changes the way the body works."** The
   definition all three lessons are built on, and it is the one that makes
   caffeine a drug. Confirm you want this rather than a
   medicine/recreational split.
2. **~90 mg of caffeine in a mug of coffee** (b6-01 hook). Varies enormously
   with the drink. Confirm the rounding, or give me a figure.
3. **Nicotine reaching the brain in about ten seconds** (b6-01, b6-02).
   Standard. Confirm.
4. **Paracetamol and the liver** (b6-01 elsewhere panel, rung 4). The lesson
   says a large dose damages liver cells, that the damage can be permanent, and
   that the person may feel fine for a day or two. All correct and all
   deliberately included, because the *feeling fine* clause is the part that
   saves lives. **Confirm you want it at KS3.**
5. **Alcohol at "roughly one unit an hour"** (b6-02 throughout, and the whole
   arithmetic of the clock). Usually given as 1 unit/hour, sometimes as
   1 unit in 60–90 minutes. Confirm the figure, since six statements and the
   instrument all depend on it.
6. **The drink unit values** — half of beer 1, single shot 1, can of cider 2,
   large wine 3, pint of strong lager 3. Plausible and rounded. Confirm.
7. **Carbon monoxide binding haemoglobin in oxygen's place** (b6-02 long-term
   card, rung 3). Correct; the lesson does not use the word
   *carboxyhaemoglobin*. Confirm the depth.
8. **Cigarette filters** (b6-02 think-again): removes some tar, does nothing to
   carbon monoxide, encourages deeper inhaling, and ventilation holes inflate
   machine-measured tar figures. All defensible. Confirm you want the
   ventilation-hole detail, which is the least well known.
9. **Vapes** (b6-02 *Going further*): no tar, no carbon monoxide, same or
   stronger nicotine dependence, very likely less harmful than cigarettes, not
   known to be safe, nothing to gain for a non-smoker, illegal to sell to
   under-18s. **RESOLVED, 16 Aug — keep the vape paragraph.** Unchanged, word for
   word.
10. **"Alcohol and nicotine cause more illness and death in the UK than every
    illegal drug combined"** (b6-01 think-again). True, and stated without
    numbers on purpose, because every number I could quote dates. Confirm you
    are happy with the unquantified form.
11. **The foxglove/digoxin dose–response layer** (b6-01 *Going further*),
    including "even water" at several litres an hour. Confirm.
12. **The claims in b6-03 are invented**, including their sample sizes and
    findings, and the legal line says so. The doctors' study in *Going further*
    is real: Doll and Hill, around 40,000 British doctors from 1951. Confirm the
    number and that you want it named.
13. **"Regular use is a clear minority at this age"** (b6-03 think-again) and the
    claim that correcting the misperception changes behaviour. Both are well
    supported and both are given without a citation a student could check.
    **Flag: this is the one place in the unit where I would accept a footnote
    with a source if you want one.**
14. **No diagrams anywhere, and no figure slots named.** Unlike B5 this unit does
    not need any: the tracer, the clock and the claim board are the visuals. If
    you want a labelled organ diagram in b6-01 it needs a manifest entry first.

---

## 4. For Code

- Three instruments in §2, all DOM-only. Nothing animates, nothing uses a timer,
  no canvas.
- Rail stops: four in all three lessons.
- Cross-links: b6-01 → b3-07, b1-05, b6-02, b4-04. b6-02 → b6-01, b4-04, b3-06.
  b6-03 → b6-01, b6-02, c1-06, b3-02. **All targets exist.** No dangling links in
  this unit.
- b6-02 links to b4-04 twice (think-again and endmatter) rather than repeating
  BREATH-11's content. Smoke damage to airways is b4-04's, and b6-02 says so
  out loud in two places. Keep that if the lessons are edited.
- Tweak props: `showDraft` on all three; `startDrug` (enum) on b6-01;
  `startUnits` (int) on b6-02.

---

## 5. Misconception register — `DRUG` family, opened with six entries

`DRUG-01` to `DRUG-06`, written into `docs/ks3/misconception-register.md`
with a new prefix row. Two per lesson, which is the shape the register prefers.

`DRUG-01` is cited by all three lessons and confronted in b6-01; the register's
`reappears_in` records that rather than minting three near-duplicates.
