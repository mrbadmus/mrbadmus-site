# NOTES-C1 — Particles and their behaviour

Six lessons, all authored 2026-08-15. Every lesson is `review_state: draft`.

C1 opened the misconception register back in Phase 0, so its thirteen entries
(`PART-01` to `PART-13`) already existed before these pages were written. Nothing in
this unit waited on an ID ruling, and nothing in it mints a new one.

---

## §1 Misconception coverage

Every one of the thirteen `PART` entries is elicited and confronted somewhere in the unit.

| Lesson | Elicits | Confronts head-on (Law 3) |
|---|---|---|
| `c1-01` particle model | `PART-01`, `PART-02` | `PART-01` at the cutting bench, `PART-02` at the gap tests |
| `c1-02` solids, liquids and gases | `PART-03`, `PART-04` | `PART-03` in Think again, `PART-04` at the motion toggle |
| `c1-03` changes of state | `PART-05`, `PART-06`, `PART-07` | `PART-05` at the sealed-flask mass readout, `PART-06` in the melt/dissolve sort, `PART-07` at the bubble commit |
| `c1-04` gas pressure | `PART-08`, `PART-09` | `PART-08` at the wall-hit counter, `PART-09` in Think again |
| `c1-05` diffusion | `PART-10`, `PART-11` | `PART-10` at the still-tank run, `PART-11` at the two-way crossing counters |
| `c1-06` testing the model | `PART-12`, `PART-13` | `PART-12` at the verdict commit, `PART-13` at the five-model timeline |

## §2 Instruments

Nine controls across six benches. All canvas work is drawn at 2× and scaled by CSS;
every canvas carries `role="img"` and an `aria-label` that updates with state.

| Lesson | Instrument | Controls | What it measures |
|---|---|---|---|
| `c1-01` | Halving bench | cut / undo / cut ten | edge length, piece count, floor at 24 |
| `c1-01` | Gap test rig | three tests × gap-filled or not | which observation each answer kills |
| `c1-02` | State bench | state ×3, freeze, paths, squash | arrangement, movement, compressibility |
| `c1-03` | Heating bench | scrub 0–100, three jump targets | temperature, phase, mass (constant) |
| `c1-04` | Collision counter | temperature ×3, volume ×3, count ×3, bump marks | wall hits per second |
| `c1-05` | Random-walk bench | run/pause, reset, follow one, warm | two-way crossings, crowding profile |
| `c1-06` | Evidence bench | explains / cannot, ×7 | 4 pass, 3 fail |
| `c1-06` | Model timeline | five steps | claim, what broke it |

## §3 Science flags

1. **`c1-01` — the floor is 24 cuts, not a round number.** 1 cm halved 24 times is 0.6 nm,
   about the width of a sucrose molecule. The bench is honest about this and the number is
   load-bearing in Rung 2. If review wants a different substance the count changes and both
   the prose and `FLOOR` must move together.
2. **`c1-01` — "you can cut a particle, you just don't get sugar" is the deliberate line.**
   Not "particles cannot be cut". The stronger claim is false at GCSE and the weaker one is
   what the model actually says. Think again is built on this distinction.
3. **`c1-02` — the fixed-size reference particle is drawn in every state.** It is the visual
   confrontation of `PART-03` and it must not be removed for layout reasons.
4. **`c1-03` — the boiling plateau is drawn much longer than the melting one.** That ratio is
   real (about 7:1 for water) and Rung 4's answer depends on students having seen it.
5. **`c1-03` — "steam is invisible" is stated in the bubble reveal.** Examiner-sensitive
   wording; flagging for Mide because the everyday use of the word is the opposite.
6. **`c1-04` — pressure is reported as wall hits per second, not in pascals.** A pascal needs
   force and area, which is P5. The bench deliberately stops at a count.
7. **`c1-04` — particle-to-particle bumps are drawn and explicitly excluded.** Showing them
   and then discounting them is the confrontation; hiding them would leave `PART-08` untouched.
8. **`c1-05` — the two crossing counters keep climbing after the tank evens out.** This is the
   whole confrontation of `PART-11` and the counters must not be reset when `even` flips.
9. **`c1-06` — three failures, and all three share one cause.** Ice floating, diamond vs
   graphite, and rubber all fail because the model has identical featureless spheres with no
   bonds. The tally text says so, and it is the bridge into C2.
10. **`c1-06` — the timeline stops short of "and now we know".** Bohr's entry says what has
    not been broken *yet*, for chemistry. Deliberate, per `PART-13`.
11. **`c1-06` — the Going further paragraph pre-empts the over-correction.** "Scientists keep
    changing their minds so nothing is trustworthy" is reachable from this lesson's own
    evidence and is closed off explicitly.
12. **Cross-unit — `PART-05` is the same belief as `ENERGY-04`.** Recorded in the register
    under the `ENERGY` entries. `c1-03`'s sealed-bag confrontation may not be dropped on the
    grounds that P1 covers it.

## §4 Onward references

- `c1-01` is named as the prerequisite by `c2-01`. That link already exists in the C2 folder.
- `c1-06` hands directly to `c2-01`: the "identical featureless spheres" limit is what
  Dalton's kinds-of-atom claim removes.
- `PART-03` is due to resurface in P1 `heating-and-thermal-equilibrium` and must be
  re-confronted there, not restated.
