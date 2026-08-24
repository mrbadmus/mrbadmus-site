# NOTES-P2 — Energy at home

Five lessons, all authored 2026-08-15. Every lesson is `review_state: draft`.

Four of the five are QUANTITATIVE — the highest concentration in KS3 so far — so the
family pattern established by `p3-01 speed` does most of the structural work here.

---

## §1 Misconception coverage

| Lesson | Elicits | Confronts head-on (Law 3) |
|---|---|---|
| `p2-01` energy in food | re-confronts `ENERGY-01` | `ENERGY-01` in Think again — the gym, and where the joules actually go |
| `p2-02` power ratings | `ENERGY-12` | `ENERGY-12` at the power bench crossover, kettle vs charger |
| `p2-03` calculating energy | (unit discipline, no ID) | the ×60 error, shown as a size-of-answer check |
| `p2-04` reading a fuel bill | `ENERGY-13` | `ENERGY-13` at the equal-area rectangles + Think again |
| `p2-05` fuels and resources | `ENERGY-14` | `ENERGY-14` at the two-axis grid — both "impossible" corners occupied |

`ENERGY-01` arriving here was predicted in the register's `reappears_in` list. `p2-01`'s
Think again names the rolling ball, the braking car and the flat battery in one sentence so
the student sees it as one belief rather than four unrelated corrections.

## §2 Instruments

| Lesson | Instrument | Controls | What it measures |
|---|---|---|---|
| `p2-01` | Calorimeter | food ×4, mass slider, burn/pause, fresh, record | temperature rise → kJ per gram |
| `p2-01` | Energy-density triangle | solve-for ×3 | E = e × m |
| `p2-02` | Power bench | run/pause, reset, 3 jump targets | power bar vs cumulative energy bar |
| `p2-02` | Power/energy sort | 6 cards × power or energy | which quantity a unit or sentence names |
| `p2-03` | E = P × t triangle | solve-for ×3 | plus the two legal unit pairings |
| `p2-03` | Appliance bench | appliance ×5, time slider, 3 presets | J and kWh side by side, and cost |
| `p2-04` | Equal-area rectangles | 4 ways to spend one unit | one kWh, four shapes, same area |
| `p2-04` | Bill builder | 5 hours-per-day sliders | a live itemised bill with standing charge |
| `p2-04` | Balance beam | (follows the bill) | sum of products = amount due |
| `p2-05` | Renewable sort | 8 resources × renewable or finite | one question at a time |
| `p2-05` | Two-axis grid | axis ×3 (carbon, reliability, land) | renewability against each, independently |

## §3 Science flags

1. **`p2-01` — the calorimeter reads 30–46% of the label figure, deliberately.** Every error
   source is one-directional and the lesson says so; Rung 3 criterion 5 is that repeating a
   measurement does nothing about a systematic leak. If review "fixes" the capture fractions
   to match labels, the whole point of the lesson is lost.
2. **`p2-01` — escaping energy is drawn as orange specks leaving the flame sideways.** This is
   the visual argument for flag 1.
3. **`p2-01` — 1 kcal = 4.18 kJ throughout.** Labels commonly use 4.184 or 4.2; the packet
   figures quoted in the hook (229 kcal / 958 kJ) are consistent with 4.18. Flagging in case
   review wants 4.2 for arithmetic simplicity — it would change the hook numbers.
4. **`p2-01` — Think again distinguishes burning in air from respiration.** Both release
   nearly identical energy; the body does it in controlled steps at 37 °C. Biology-adjacent,
   so worth Mide's eye given B3 references this lesson.
5. **`p2-01` — fat ≈ 37 kJ/g, carbohydrate ≈ 17 kJ/g quoted in prose.** Standard values;
   confirm before freeze.
6. **`p2-02` — the kettle/charger numbers are exact and the result is counter-intuitive.**
   2000 W × 180 s = 360 kJ; 15 W × 28 800 s = 432 kJ. The crossover at 6.67 h is computed,
   not asserted, and the bench marks it.
7. **`p2-02` — Think again says swapping to a lower-wattage kettle can cost slightly more.**
   Correct (longer heating time, more loss to the room) and counter to common advice.
   Examiner-sensitive; flagging deliberately.
8. **`p2-02` — Going further calls Watt's horsepower figure "arguably deliberately" generous.**
   A judgement about motive. Soften or cut if review objects.
9. **`p2-03` — the canvas states "W × min IS ALWAYS WRONG" in the triangle panel.** The ×60
   error is the whole misconception; naming it flatly is the intent.
10. **`p2-03` — the fridge outranks the oven on the bench at realistic settings.** 90 W × 24 h
    beats 2200 W × 45 min. This is `ENERGY-12` paying off one lesson later.
11. **`p2-03` — Going further uses the 1999 Mars Climate Orbiter loss.** Figures ($327 m,
    ~170 km) are checkable.
12. **`p2-04` — 27p/kWh and 53p/day standing charge.** Plausible mid-2020s UK values, not
    live figures. They will date; they are single constants (`PRICE`, `STANDING`) at the top
    of the logic class for that reason.
13. **`p2-04` — Going further explains why the standing charge exists rather than just
    resenting it,** and points out that halving usage does not halve the bill. Rung 3
    criterion 5 depends on this.
14. **`p2-04` — the four "one kWh" rectangles are drawn with equal area.** The 9 W LED for
    111 h case is the one that lands; it is also the argument for the filament-bulb ban that
    `p1-02` raised.
15. **`p2-05` — nuclear is placed as non-renewable and low-carbon, and wood as renewable and
    high-carbon.** These two cells are the confrontation of `ENERGY-14` and the lesson does
    not soften either. Politically sensitive; flagging for Mide explicitly.
16. **`p2-05` — three axes, each reordering the ranking.** Carbon, availability on demand,
    land taken. The lesson refuses to name a best resource, and Think again says anyone who
    does "has stopped counting axes early".
17. **`p2-05` — carbon and reliability figures are relative positions, not measured values.**
    They are `0`–`1` for plotting only. Do not let them be read as data.
18. **`p2-05` — Going further traces almost everything to the Sun, and names the three
    exceptions** (geothermal, tidal, nuclear). Ties "renewable" to the length of the delay.

## §4 RULED-BY-PRECEDENT — formula diagrams in this unit

Following the rule recorded in NOTES-P1 §5:

- `p2-01` — E = e × m. A genuine product. **Triangle**, and the canvas says so.
- `p2-03` — E = P × t. A genuine product. **Triangle**, plus a panel naming the two legal
  unit pairings and the illegal one.
- `p2-04` — each bill row is P × t (**triangle**); the amount due is a sum of every row
  (**balance beam**). Both diagrams appear, and §s-shape names why one cannot do both jobs.
- `p2-02`, `p2-05` — no formula diagram; neither lesson has a calculable relationship at its
  centre.

`p2-04` is the lesson that makes the rule visibly necessary rather than pedantic — it is the
only place in KS3 so far where a product and a sum sit in the same calculation.

## §5 The FIFA sequence

`p2-01` and `p2-03` run the four-line sequence established by `p3-01 speed` — Formula,
Insert, Fine-tune, Answer — and both run it **on the student's own recorded numbers** where a
run exists, falling back to a stated worked example where it does not. `p1-08` does the same.

`p2-03`'s Insert line carries the unit conversion deliberately: converting there rather than
afterwards is the habit that prevents flag 9.

## §6 Ownership

`p2-01 energy-in-food` is the OWNER per `structure.py` §4.6 — B3's `a-balanced-diet` carries
the `⇄ Owned by Physics P2` marker and references this lesson rather than duplicating it. The
endmatter of `p2-01` names B3 explicitly under "Also used by". When B3 is authored it must
link here and must not restate the energy figures.

## §7 Onward references

- `p2-05` hands to `p3-01 speed`, which is already built.
- `ENERGY-05`/`ENERGY-06` are due to resurface at P11 `temperature-and-internal-energy` and
  C7 `energy-and-changes-of-state`.
- `p2-04`'s standing-charge argument is the seed for any future economics-adjacent content;
  no unit currently claims it.
