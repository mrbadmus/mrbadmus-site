> **Raw extraction notes, written before the examination.** Where they disagree with `examination/`, `FLAGS.md` or `00-BRIEF.md` (spec references, required-practical numbers, quiz-key alignment), those win.

# Batch 18 — extraction notes

Facts only, read straight from the 13 extracted files in
`04-checked-science-source/` (each file's header gives the routes; `##`
section presence gives everything else). No route-copy `quiz` section exists
in ANY of the 13 files — every route a lesson appears on serves the identical
quiz list, so "quiz count per route" below is one number covering every route
listed. The only field that ever differs by route is `higher`.

| # | Lesson | Routes | Quiz count (same on every route) | examiner_tip | fifas | equations | rp (verbatim) | variables |
|---|---|---|---|---|---|---|---|---|
| 1 | poles-of-a-magnet | CF CH TF TH | 2 | no | 0 | none | none | 0 |
| 2 | magnetic-fields | CF CH TF TH | 2 | no | 0 | none | verbatim (RP21 — plot field pattern with a compass, see below) | 0 |
| 3 | electromagnetism | CF CH TF TH | 2 | no | 0 | none | verbatim (RP21 — electromagnet strength vs turns/current, see below) | 0 |
| 4 | flemings-left-hand-rule | CH TH | 2 | no | **1** | 1 — F = B × I × l | none | 4 |
| 5 | electric-motors | CH TH | 2 | no | 0 | none | none | 0 |
| 6 | loudspeakers-headphones | TH | 2 | no | 0 | none | none | 0 |
| 7 | induced-potential | TH | 2 | no | 0 | none | none | 0 |
| 8 | uses-generator-effect | TH | 2 | no | 0 | none | none | 0 |
| 9 | microphones | TH | 2 | no | 0 | none | none | 0 |
| 10 | transformers | TH | 2 | no | **1** | 2 — Vs/Vp = Ns/Np; Vp×Ip = Vs×Is | none | 4 |
| 11 | solar-system-gravity | TF TH | 2 | no | 0 | none | none | 0 |
| 12 | gravity-stable-orbits | TH | 2 | no | 0 | none | none | 0 |
| 13 | dark-matter-dark-energy | TH | 2 | no | 0 | none | none | 0 |

Two `fifas` lessons (`flemings-left-hand-rule`, `transformers`), matching
BATCH-PLAN's FIFA column exactly. The CFIFA form (step C) was appended to
both files, the four FIFA steps kept byte-identical, Convert step added to
each.

**Neither FIFA in this batch needed a real unit conversion.**
`flemings-left-hand-rule`'s worked example gives flux density in tesla,
current in amperes and length in metres — all already SI. `transformers`'s
worked example gives turns as dimensionless counts (nothing to convert at
all) and voltage already in volts.

## No worked example chains two equations (rule 3)

Both FIFAs in this batch (`F = B × I × l` and `Vs/Vp = Ns/Np`) apply a single
equation once. Neither states two relationships in one `F` step the way
batch-16's `half-lives` or this run's own batch-17 `stopping-distance-
braking` do — nothing to flag under rule 3 for this batch.

## wrong_explanations key check

All 26 quiz items across the 13 files were checked mechanically: every item
has exactly 4 options, the `true` option sits at index 0 on all 26, and every
item's `wrong_explanations` keys match exactly the indices of its 3 wrong
options (`1,2,3`) — no shifted index anywhere.

Read by hand, one real content defect was found, in the OPTION TEXT itself
rather than in a `wrong_explanations` string: **loudspeakers-headphones**,
quiz item 2 ("A loudspeaker produces a loud, low-pitched sound…"), wrong
option 1 reads *"High frequency (low pitch) and large amplitude (loud)"* —
pairing "High frequency" with "(low pitch)" is internally self-contradictory
(high frequency means HIGH pitch, as the lesson's own theory and the item's
`wrong_explanations["1"]` both correctly state: *"Low pitch = LOW frequency
AC — high frequency would produce a high-pitched sound"*). The explanation
text is correct; the option it is attached to mislabels itself. A genuine
content defect in the verbatim source, kept byte-identical here per the port
rule; flagged for Mide's gate rather than silently fixed. No other item in
this batch showed a comparable defect.

## Anything odd

1. **Spec-number agreement with BATCH-PLAN.md is good**, with the usual "6."
   vs "4." convention difference on every 8463-only lesson
   (`loudspeakers-headphones` through `dark-matter-dark-energy`,
   `solar-system-gravity`), already explained in batch-15/16's notes — not a
   mismatch. `solar-system-gravity` and `gravity-stable-orbits` both reduce
   to the same filename spec stem (`6.8.1`) but remain distinct files because
   the slug differs — no collision, the same shape batch-16 found for
   `resolving-forces`/`free-body-diagrams`. **One row is a real wrinkle**:
   `dark-matter-dark-energy`'s data `spec` is `"6.8.4"` against BATCH-PLAN's
   own `?`-flagged guess `"8463 4.8.2?"` — a bigger gap than the usual single-
   digit wrinkle (BATCH-PLAN itself is uncertain here too), unconfirmed
   against AQA's own numbering.

2. **FIFA/equations/RP columns match BATCH-PLAN exactly on all 13 rows** — no
   mismatch anywhere in this batch's plan. RP: BATCH-PLAN marks exactly two
   lessons RP=Y (`magnetic-fields`, `electromagnetism`) and those are the only
   two files carrying an `## rp` section — exact agreement. **Both reuse the
   SAME RP number, `RP21`**, for two different practicals (compass-plotting a
   field pattern vs measuring electromagnet strength against turns/current) —
   the same reuse pattern batch-17 found with RP19/RP20. Every RP number cited
   anywhere in this pack is **(frozen label, unverified)** against AQA's own
   numbering, verbatim from each file's `rp` field only.

3. **No `examiner_tip` anywhere in this batch** — same pattern as every prior
   batch. All 13 files omit the `## examiner_tip` section entirely.

4. **Nine filenames needed renaming** (step B): `loudspeakers-headphones`,
   `induced-potential`, `uses-generator-effect`, `microphones`,
   `transformers`, `gravity-stable-orbits` and `dark-matter-dark-energy`
   (all `(HT only, physics only)`) plus `solar-system-gravity` (`(physics
   only)`) had their parenthetical annotation stripped from the filename
   (spec digits only), kept verbatim in the header. `electromagnetism`
   needed no rename despite carrying route-copy content (its spec has no
   parenthetical). No filename collisions.

5. **No subject:slug collisions were actually tested** — all 13 slugs were
   passed as `physics:<slug>` from the start, so the extractor never searched
   biology/chemistry for them; the console output was 13 clean `wrote …`
   lines with no collision error printed for any slug.

6. **Eight of thirteen lessons carry a `higher` section**: `electromagnetism`,
   `loudspeakers-headphones`, `induced-potential`, `uses-generator-effect`,
   `microphones`, `transformers`, `gravity-stable-orbits` and
   `solar-system-gravity`. The other five (`poles-of-a-magnet`,
   `magnetic-fields`, `flemings-left-hand-rule`, `electric-motors`,
   `dark-matter-dark-energy` — the last because its entire content is
   already HT-only with no Foundation sibling to extend from) have none.
   Only two lessons produce route-copy sections at all:
   `electromagnetism` (CF+TF copies) and `solar-system-gravity` (TF copy).

7. **One lesson breaks the "every copy renders null" pattern, continuing what
   batch-17 found.** `electromagnetism`'s Combined Foundation and Triple
   Foundation `higher` copies are REAL, non-null text — identical to each
   other, but different wording from the canonical Triple Higher `higher`
   field (the TH copy names Fleming's Left-Hand Rule AND the generator
   effect together in one paragraph; the CF/TF copy covers only the motor
   effect and F=BIl, naming Fleming's rule by finger rather than by name, and
   omits the generator effect entirely). `solar-system-gravity`'s one TF copy
   still renders `null`, continuing the pattern every batch through 16 found
   with no exception. So in this batch, exactly one of two route-copy-bearing
   lessons shows the real-content divergence — the same EM/electromagnetism-
   adjacent pattern batch-17 found on its two `properties-em-waves-*`
   lessons.

8. **No `canonical_record` WARNING was printed by the extractor** — the
   extraction run's console output was 13 `wrote …` lines and nothing else.

9. **All 13 lessons' routes match BATCH-PLAN's routes column exactly** —
   including the Combined-and-Triple-Higher-only pair
   (`flemings-left-hand-rule`, `electric-motors`, both CH/TH), the five
   Triple-Higher-only lessons and the one Triple-Foundation-and-Higher
   lesson (`solar-system-gravity`) — no discrepancy anywhere.

10. **No authored batch-2/batch-3 lesson links forward to any slug in this
    batch** — a clean contrast with batch 17, where five already-authored
    lessons link forward to six of its slugs (see batch-17's
    `_extract-notes.md` note 10). Searched the same `connects`/`endConnects`
    arrays across `ks4_lessons/authored/batch-2/` and `batch-3/`; none
    mentions any of this batch's 13 slugs.

11. **This batch spans two AQA topics** (magnetism §6.7, space §6.8). KS3
    precedent is strong for magnetism and absent for space mechanics:
    `ks3_art/p10.py` (Magnetism and electromagnetism, five lessons) covers
    five of the first six lessons in this batch directly or contingently
    (poles, fields, electromagnetism, motor effect, motors) but stops at the
    motor effect — it never reaches the generator effect, so lessons 6–10
    (`loudspeakers-headphones` through `transformers`) have NO KS3 precedent
    at all, the same "content starts at KS4" shape batch-16 found for
    radioactivity and batch-17 found for momentum and circular motion.
    `ks3_art/p12.py` (Space, six lessons sharing one `space-bench` shell)
    covers `solar-system-gravity`'s W=mg and light-year/AU-scale content
    contingently but never models orbital speed vs radius, so
    `gravity-stable-orbits` has no KS3 precedent either, and
    `dark-matter-dark-energy` has none at all — not even P12's non-
    quantitative `space-think` shell, which "draws NOTHING, deliberately"
    by its own module docstring.
