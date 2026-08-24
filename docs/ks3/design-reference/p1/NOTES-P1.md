# NOTES-P1 — Energy transfers

Eight lessons, all authored 2026-08-15. Every lesson is `review_state: draft`.

---

## §1 The ENERGY family was minted to unblock this unit

`ENERGY-01` to `ENERGY-14` were added to `docs/ks3/misconception-register.md` on
2026-08-15, opened by `p1-01 energy-stores`. All fourteen are draft — `statement` is
science-bearing under §5.10 and needs Mide's review before any freeze.

This was a judgement call to avoid blocking. It is a different case from `FORCE`, `BODY`
and `ATOM`, which have proposed IDs from the P3/B2/C2 pass and are **still not minted** —
the register carries an explicit note that no authored lesson may cite them until they are.

⚠️ **`ENERGY-04` and `PART-05` are the same underlying belief** — that a quantity stops
existing when it stops being visible. Separate IDs because the confrontations genuinely
differ (a balance for mass, a thermometer for energy), but a student holding one almost
always holds the other. Neither `c1-03` nor `p1-03` may drop its confrontation on the
grounds that the other covers it. Same shape as the `CELL-08` lock.

`p1-03` §s-think names the `c1-03` sealed-bag result explicitly and calls the two
"the same belief in different clothes". That cross-reference is deliberate and load-bearing.

## §2 Misconception coverage

| Lesson | Elicits | Confronts head-on (Law 3) |
|---|---|---|
| `p1-01` energy stores | `ENERGY-01`, `ENERGY-02` | `ENERGY-01` at the store-audit ledger, `ENERGY-02` in the store/pathway sort |
| `p1-02` before and after | `ENERGY-03` | `ENERGY-03` at the balance in the hook + the before/after tally |
| `p1-03` conservation | `ENERGY-04` | `ENERGY-04` at the running total with the thermal store hidden/shown |
| `p1-04` heating and equilibrium | `ENERGY-05`, `ENERGY-06`, re-confronts `PART-03` | `ENERGY-05` at the two-quantities bench, `ENERGY-06` at the one-way flow, `PART-03` at the fixed-size reference particle |
| `p1-05` conduction | `ENERGY-07` | `ENERGY-07` at the touch test — four objects, all 20 °C |
| `p1-06` radiation | `ENERGY-08`, `ENERGY-09` | `ENERGY-08` at the three-routes bench, `ENERGY-09` in the word sort |
| `p1-07` insulation | `ENERGY-10` | `ENERGY-10` at the ice trial — wrapped ice lasts four times longer |
| `p1-08` simple machines | `ENERGY-11` | `ENERGY-11` at the student's own run table |

## §3 Instruments

Eleven benches. Canvas drawn at 2× and CSS-scaled; every canvas carries `role="img"` and a
state-dependent `aria-label`. All animation loops respect `prefers-reduced-motion`.

| Lesson | Instrument | Controls | What it measures |
|---|---|---|---|
| `p1-01` | Store audit | scenario ×5, 8 before-ticks, 8 after-ticks, check, clear | which stores are filled |
| `p1-01` | Store/pathway sort | 6 cards × store or pathway | can energy sit here when paused |
| `p1-02` | Before-and-after tally | device ×4, useful-fraction slider | two columns, one total |
| `p1-02` | Wasted/point sort | 4 cards | is the thermal store the job or not |
| `p1-03` | Running total | release, pause, reset, friction on/off, **hide thermal store** | four stores, fixed total |
| `p1-03` | Balance beam | 4 moments in the swing | the sum, at every stage |
| `p1-04` | Two-quantities bench | amount ×3, particle speed ×3 | temperature vs thermal store |
| `p1-04` | One-way flow | run, reset, pair ×3 | direction of transfer, equilibrium |
| `p1-05` | Conduction bench | material ×4, flame, cool, **free electrons** | time to melt the wax, gradient |
| `p1-05` | Touch test | 4 objects × cold or neutral | hand vs thermometer |
| `p1-06` | Three routes | scenario ×4 (air/vacuum, above/beside/touching) | which routes survive |
| `p1-06` | Radiation word sort | 6 cards × harmless or risky | where the danger boundary sits |
| `p1-07` | Insulation trial | run, reset, jump to 30 min | four cooling curves + results table |
| `p1-07` | Ice trial | run, fresh cubes | the decisive result |
| `p1-08` | Lever bench | fulcrum slider, lift-and-record, clear | force, distance, both products |
| `p1-08` | Balance beam + triangles | solve-for ×4 | product per pan, sum across |

## §4 Science flags

1. **`p1-01` — eight stores; light/sound/electrical are not among them.** If review prefers
   the older "types of energy" vocabulary, Think again and Rungs 3–4 need rewriting, not
   relabelling.
2. **`p1-01` — the bouncing-ball scenario ticks thermal at maximum squash.** Deliberate; it
   is why a ball never returns to its drop height. Hardest of the five, placed last.
3. **`p1-01` — the kettle scenario puts the chemical store in a power station.** Invites the
   "where does electricity come from" question one lesson early; handled in one clause.
4. **`p1-01` — Going further says nobody has ever seen energy.** Attributed in substance to
   Feynman, not quoted. Examiner-gated wording.
5. **`p1-02` — the tally's slider lets students set a physically wrong efficiency.** Intended:
   the total never budges whatever they set, which is the teaching point. The real figure is
   named in the note when they land within ±6%.
6. **`p1-02` — "wasted" is framed as a judgement about intent, not about physics.** Flagging
   because it is a wording choice a reviewer may want tightened.
7. **`p1-03` — the hide-thermal-store control deliberately makes the law look false.** This is
   the confrontation of `ENERGY-04` and must not be removed as a "confusing" control.
8. **`p1-03` — friction-off mode is physically impossible and labelled as idealised.**
9. **`p1-03` — Going further uses the 1930 neutrino prediction.** Dates and the 26-year gap
   are checkable; flagging for verification.
10. **`p1-04` — the thermal-store bar is logarithmic and says so on the canvas.** The spark-to-bath
    range is ~10⁹ and a linear bar would show nothing.
11. **`p1-04` — the "no cold travels this way" dashed arrow is drawn and labelled as not existing.**
    Drawing the thing that does not happen is the confrontation of `ENERGY-06`.
12. **`p1-04` — Going further credits Rumford's 1798 cannon-boring.** Ties the caloric theory's
    failure to `c1-06`'s model-has-edges lesson explicitly.
13. **`p1-05` — grey home-position rings show particles never travel.** Required for
    Rung 3 criterion 3; do not remove for visual tidiness.
14. **`p1-05` — free electrons are shown only for metals, and the control says so for non-metals.**
15. **`p1-05` — conduction times (Cu 9 s, Fe 22 s, glass 150 s, wood never) are illustrative,
    not measured.** Ratios are right; absolute values need review before any claim of realism.
16. **`p1-06` — infrared is placed at the harmless end and UV named as the boundary.**
    Examiner-sensitive; the word sort is the mechanism, not the prose.
17. **`p1-06` — "heat rises" is corrected to "warm air rises".** The phrase is quoted as
    student wording and never used approvingly.
18. **`p1-07` — the ice trial is the only decisive evidence in the lesson.** Hot-water cooling
    curves alone are consistent with "insulation adds warmth"; only the ice result rules it out.
    Do not cut it for length.
19. **`p1-07` — the plan-the-trial section marks variable control before any data exists.**
    INVESTIGATION-family requirement.
20. **`p1-08` — force meter readings scatter ~+0.5 to +3.5%, always upward.** Friction costs
    energy, so measured input exceeds the ideal — never below. Rung 3 criterion 5 depends on it.
21. **`p1-08` — Going further cites the 1911 US Patent Office working-model rule.** Checkable.

## §5 RULED-BY-PRECEDENT — the formula-diagram rule

NOTES-C2 §8 flag 14 recorded the `c2-06` decision: conservation of mass is a sum, not a
product or quotient, so the triangle diagram teaches a false relationship; a balance beam was
drawn instead and the other three parts of the formula sequence kept.

**Applied here as a rule, pending Mide's ruling:**

> Triangle for a product or a quotient. Balance beam for a sum. Never a triangle over a
> relationship that is neither.

- `p1-03 conservation-of-energy` — a sum. **Balance beam**, four configurations, beam always level.
- `p1-08 simple-machines` — F₁×d₁ = F₂×d₂. A balance *of two products*, so **beam at the top
  level with a triangle on each pan**. The canvas states this in words.
- `p2-03 calculating-energy-transferred` — E = P×t is a genuine product. **Triangle**, legitimately.
- `p2-04 reading-a-fuel-bill` — rows are products, the total is a sum. **Both.**

If the ruling goes the other way this is a diagram swap per lesson, not a rewrite — the FIFA
sequence and all prose are independent of the choice.

## §6 Authoring convention adopted mid-unit

`c1-04`'s `startTemp` shipped briefly with a dead enum value because the prop was declared in
`d_props_json` first and the state read wired afterwards; `Math.max(0, findIndex(...)) || 1`
silently collapses index 0. Same defect class as the `b1-06 railLabels` orphan.

**Convention, applied from `p1-02` onward and to every lesson in P1 and P2: declare a prop and
its state read in the same pass, and use `idx >= 0 ? idx : fallback` for index lookups — never
`|| fallback`.** Numeric props use `Number.isFinite(Number(x)) ? clamp(x) : default`.

## §7 Onward references

- `p1-04` lists `c1-02` as a prerequisite alongside `p1-03`. `PART-03` is re-confronted there,
  not restated — the fixed-size reference particle is the mechanism.
- `p1-08` hands to `p2-01`. `ENERGY-11` is due to resurface at P4 `moments` and P5 `hydraulics`.
- `p1-02`'s second-law paragraph is the seed for P11 `temperature-and-internal-energy`.
