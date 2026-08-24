# DEPARTURES — P3, *Describing motion*

One row per change to Claude Design's delivered content, under Mide's
standing ruling of 24 Aug 2026. The column that matters is **the defect** —
not "why mine is better", but what was WRONG with hers. A row that cannot
fill that column cleanly is not a departure; it is a preference, and her
version stands.

Her page is the DEFAULT and the STRUCTURE. Nothing here re-plans a lesson,
re-cuts a rail or changes what a lesson covers.

---

## CHANGED — 0 rows

**Nothing in P3 changed her science or her content.** Her three lessons are
ported as drawn.

Two engine-policy adjustments are recorded below. Neither is a science
departure and neither takes a row above: one is the standing removal of the
draft marker, and the other is an answer-position rule that applies to every
unit in the key stage.

### Engine policy, applied — not departures

| What | Why it is policy rather than a departure |
|---|---|
| **The `ks3-review-flag` "Draft — not yet science-reviewed" line is not shipped.** It is on all three of her pages by default, as it is on every KS3 delivery. | MRB-221 revoked the review marker. Removing it is standing engine policy for every unit, applies identically to B1–C10, and takes no register row. Swept for by CONCEPT — "draft", "review", "not yet checked", "provisional" — rather than by class name, because the same language survived on 297 pages once by hiding in `LEGAL_LINE`. Built P3 pages: **zero hits.** |
| **Ladder answers are spread across all four option positions.** Design's three lessons put the correct option at index 0 in five of six marked rungs. | MRB-278 is a key-stage-wide gate: no index may hold more than half a corpus, and none may be never-used where the count allows. It failed P2 on exactly this and would have failed P3. Her four CLAIMS and her four feedback lines are unchanged in every rung — only the order. ⚠️ The feedback map is keyed by option INDEX, so the rotation was done structurally and asserted: reordering options without rewriting those keys attaches every explanation to the wrong distractor, and the page still renders. |

---

## CONSIDERED, NOT CHANGED

Design's `NOTES-P3.md` closes with thirteen numbered science flags and five
questions she wants ruled. Every one was weighed. **All thirteen resolve to
"hers stands"**, and the rulings are recorded in the lesson modules where a
future lane will actually read them.

| Flag | What was considered | Why hers stands |
|---|---|---|
| 1 | Add an explicit "we are ignoring friction here" to `p3-01`? | Her page never claims the reading is instantaneous — it says *the speed between the gates*, which is exactly what the measurement is and is true whether or not the trolley slows. A friction caveat would introduce an idea the lesson does not use and would undercut the stretch layer, which is where instantaneous-vs-average is properly raised. No defect. |
| 2 | Mean the TIMES or mean the SPEEDS in rung 3? | Hers: mean the three times, then divide the distance once. It is the method that generalises to the light-gate practical, and it avoids asking a student to average speeds in the one lesson that teaches why you must not. Correct as drawn. |
| 3 | Keep km/h → m/s (÷ 3.6) at KS3, or rewrite compare pair 3 into one unit? | Kept. Pair 3 is a DELIBERATE dead heat (72 km/h against 20 m/s) and it only works if the conversion is done — without it a student picks at random and learns nothing. Carried as `touches`, not `covers`, since MOT.01 names only speed = distance ÷ time. |
| 4 | Fly ≈ 1.9 m/s, airliner = 250 m/s — order-of-magnitude illustrations. | Both check out (houseflies cruise around 2 m/s; 15 000 m in 60 s is 250 m/s ≈ 900 km/h) and both are presented as illustrations rather than looked-up specimens. No defect. |
| 5 | 1.67 m/s rather than 1.7 for 200 ÷ 120. | Matches the lesson's own two-decimal convention, used consistently. No defect. |
| 6 | Hold the line that "velocity" appears nowhere and direction is never a negative number? | Held. It is not in MOT.01–03, direction-as-sign is P4's to open, and opening it here would turn every rung in `p3-03` into a sign-convention question rather than a motion one. |
| 7 | Is "distance travelled vs distance from the start" legitimate stretch or GCSE creep? | Legitimate. It is displacement in everything but name and the page never uses the word; MOT.02 is about REPRESENTING a journey, and a graph that can never come down is a different representation of the same journey. Stays in the stretch layer with no assessment attached beyond rung 4's last criterion. |
| 8 | Is "a flat line is stopped, not slow" attacked hard enough? | Yes. Her page attacks it twice — read-back question 1 and ladder rung 1 — and both make the student COMMIT rather than read a correction. Sufficient as drawn. |
| 9 | Galilean relativity, unnamed, in `p3-03`'s stretch. | Correct for uniform motion, and her wording "smoothly moving" is what keeps acceleration out. Kept including the unnamed attribution: naming Galileo would add a fact to memorise in place of an idea to hold. |
| 10 | Is `p3-03`'s plane-and-wind rung too hard for KS3? | It stays. It is SELF-MARKED with five criteria, so a student who cannot finish it loses nothing, and its last criterion is `FORCE-03` from `p3-01` seen from the other side — the unit closing its own loop. Cutting it would leave the loop open. |
| 11 | A car drawn facing right while drifting left, from the other car's seat. | **Correct, and deliberately kept.** Orientation follows the GROUND velocity; motion follows the relative one. A car does not physically turn round because you changed who was watching. Flagged in `ks3_art/p3.py` and in `shared/ks3.css` so the next lane does not "fix" it. |
| 12 | Earth's orbital speed given as "about 30 km every second" (true value 29.8). | Correctly stated as an approximation, and the approximation is the right size. No defect. |
| 13 | Does `p3-01` own the instantaneous-vs-average distinction? | It raises it in stretch prose only, with no assessment attached, which is the right weight: it is not in MOT.01–03 and is not taught as a term anywhere at KS3. Kept as drawn — and it is where `FORCE-05` is confronted. |

### Her §8 questions, answered

| Question | Ruling |
|---|---|
| §0 — is P3 the intended unit? | **Yes, and it can now be checked properly rather than inferred.** ⚠️ Her note says `half_terms.py` does not exist in the repository, and that was true on 15 Aug. **It exists now** — 1014 lines, added by MRB-176 — as does the `default_sequence.py` it depends on, and I initially repeated her "still absent" without checking. Read: `DEFAULT_SEQUENCE_V1` puts **P3 in Year 7** (with P4 and P11), P1 in Year 8 and P2 in Year 9, and P3 is first among the Year-7 physics units in declaration order. So her resolution was right, and the data that would have settled it now exists. |
| §4 — `FORCE` or a new `MOT` family? | **`FORCE`.** The register's own family table declares it as "forces AND MOTION", so motion is inside it as reserved. Same ruling this register already made for `ENER` against `ENERGY`. P4 continues from `FORCE-12`. |
| flag 3 — km/h in or out? | In. See above. |
| flag 7 — distance travelled as stretch? | Stays as stretch. See above. |
| §1 — is the QUANTITATIVE pattern the one to fix? | Yes, and it is now enforced rather than described: `r_light_gates` REFUSES a payload whose speed readout carries a computed value, because her step (2) — the instrument measures and does not calculate — is the step the family stands on. P2's four QUANTITATIVE lessons already inherit it. |

### Her §7 hand-over note on B1

She reported, without touching the file, that `b1-06` declares a `railLabels`
prop its logic class never reads — a Tweaks control that does nothing.
**Not actioned here, and deliberately: B1 is another lane's unit.** Recorded
so it is not lost.
