# B4 — Breathing and gas exchange · author's notes

Five lessons, complete unit. Draft — nothing here has been science-reviewed.
Flags are numbered so they can be answered by number.

Queue resolution and filename convention are in `NOTES-P3.md` §0 and apply
unchanged: slugs are verbatim from `structure.py`.

---

## 1. Statutory coverage

| Lesson | Statements |
|---|---|
| `the-gas-exchange-system` | `KS3.B.GAS.01` — the *structure and functions* clause |
| `how-breathing-works` | `KS3.B.GAS.02` |
| `alveoli-built-for-exchange` | `KS3.B.GAS.01` — the *adaptations to function* clause |
| `exercise-asthma-and-smoking` | `KS3.B.GAS.03` |
| `stomata-and-gas-exchange-in-plants` | `KS3.B.GAS.04` |

All four GAS statements covered. `GAS.01` splits across lessons 1 and 3 for the
same reason `NUT.04` split across three in B3 — it is a compound bullet, and
structure and adaptation are different lessons.

**`GAS.02` is only partly discharged.** The statement asks for *"simple
measurements of lung volume"* and this unit contains none. See flag 1.

---

## 2. Family patterns as applied

- **SYSTEM (b4-01, b4-04)** — b4-01 is a route with a composition table, and the
  route deliberately ends on a sixth item that is *not part of the airway*
  (ribs, intercostals, diaphragm), which hands off to lesson 2. b4-04 inverts
  the B2 `system-switch` idiom: instead of switching a part off, the student is
  given a symptom and must **locate** which part is affected. Same anatomy of
  reasoning, opposite direction.
- **MODEL (b4-02, b4-03)** — two model lessons back to back, treated
  differently on purpose. b4-02 builds the bell jar and then spends a whole
  section on where it fails (four named failures, each with why it is still
  worth having). b4-03 builds a *numerical* model of the gradient and uses it to
  kill a belief. If both had been "build it then break it" the unit would sag.
- **CONTRAST (b4-05)** — the contrast is not plant-versus-animal, which is the
  misconception. It is *respiration versus photosynthesis inside the same
  organism*, and the payoff is that at one light level the difference is zero.

---

## 3. New instruments

### 3.1 `gas-compare` — flagship of `b4-01` (DOM only)

- **Controls:** four gas rows × three prediction buttons (up / down / same);
  *analyse both bags*, locked until all four committed.
- **Readouts:** a two-column table with a proportional bar per cell, a verdict
  word per row, and a closing paragraph that names the two figures that matter.
- **Payload:** `{gases: [{id, name, inPct, outPct, change, inLabel, outLabel, verdict}], predictions: {}, open: bool}`.
- **Note for Code:** bars are `width: pct%` directly, so nitrogen is 78% wide
  and carbon dioxide inhaled is clamped to a 1.5% minimum so it is visible at
  0.04%. That clamp is the only dishonest pixel in the unit and it needs the
  numeral next to it, which it has.

### 3.2 `bell-jar` — flagship of `b4-02`

- **Controls:** a 0–100 diaphragm slider (0 = relaxed/domed, 20 = rest,
  100 = fully contracted/flat); *breathe in* and *breathe out* presets.
- **Readouts:** a chest block whose height scales, a lung circle whose
  `transform: scale()` follows it, four numeric readouts (volume L, pressure
  inside kPa, pressure outside fixed at 0, air movement direction), and a
  **four-step ordered chain** whose text is regenerated per state.
- **Payload:** `{dia: 0-100, volume_l, pressure_kpa, phase: 'in'|'out'|'rest'}`.
- **Design note:** the chain is the instrument, not the picture. Its whole job is
  that the *first* line is always muscle and the *last* line is always air. If
  Code renders the chain as static text, the lesson's central confrontation is
  gone.

### 3.3 `crossing-counter` — flagship of `b4-03`

- **Controls:** two switches — breathing on/off, blood flow on/off. Four states.
- **Readouts:** alveolar and blood oxygen in kPa, net absorbed, and **two bars:
  crossings in and crossings out**, neither of which is ever zero.
- **Payload:** `{breathing: bool, bloodFlow: bool, alveolar_kpa, blood_kpa, in_per_s, out_per_s}`.
- **Note for Code:** the four states are a lookup table, not a simulation, and
  the outward count must stay visible in all four. A student who sees the outward
  bar disappear has learnt the misconception instead of losing it.

### 3.4 `two-process-ledger` — flagship of `b4-05`

- **Controls:** a 0–100 light slider; four presets (midnight / dawn / overcast /
  bright noon).
- **Readouts:** three bars — respiration (flat, 2.0 units, **never moves**),
  photosynthesis (`9 × (1 − e^(−light/32))`), and net, whose colour and label
  flip sign. A three-branch verdict panel, the middle branch being the
  compensation point.
- **Payload:** `{light: 0-100, resp_rate: 2, photo_rate, net_rate, balanced: bool}`.
- **Design note:** the dawn preset (21) is tuned to sit within the ±0.25
  balanced window so the compensation-point branch is reachable by pressing one
  button. If the curve constants change, retune that preset or the payoff is
  unreachable.

---

## 4. Science flags — numbered for review

1. **`GAS.02` asks for simple measurements of lung volume and this unit has
   none.** Options: (a) add a fifth section to `b4-02` with a displacement-jar or
   spirometer-trace reading; (b) add a sixth lesson; (c) accept the gap and
   record it. My recommendation is (a) — it is one section, it is a genuine
   practical, and tidal / vital capacity numbers would strengthen flag 9's
   think-again block. **This needs a decision before the unit freezes.**
2. **Inhaled/exhaled composition** (78/21/0.04 → 78/16/4, warmer and saturated).
   Standard figures. Confirm, and confirm that giving water vapour as
   "variable, often low" → "saturated" rather than as percentages is acceptable.
3. **"You keep roughly a quarter of the oxygen you take in."** 21 → 16 is 24%.
   Confirm the phrasing, which the mouth-to-mouth hook depends on.
4. **~500 million alveoli** (b4-01, b4-03) and **~70 m² total surface**
   (b4-03). Both are commonly quoted with wide ranges in the literature —
   alveolar counts from 270 to 790 million, area from 50 to 100 m². Confirm the
   two numbers, and note this is the same class of problem as B3 flag 17.
5. **"About twenty-three generations of branching."** Weibel's figure. Confirm.
6. **"A piece of fresh lung tissue floats"** (b4-01 think-again). True of
   inflated lung; it is used to argue against the balloon picture. Confirm.
7. **The nitrogen stretch layer** (b4-01) — you breathe your most essential
   element in and straight back out, and get all of it from food via
   nitrogen-fixing bacteria. Confirm; it forward-references B9 and C6.
8. **Pneumothorax as the b4-02 hook.** A puncture wound collapsing an
   undamaged lung. Clinically correct and it is the cleanest possible evidence
   for the target misconception. Confirm you want an injury as a hook, and
   confirm the phrasing does not read as first-aid instruction.
9. **"Halving the radius reduces flow about sixteenfold"** (b4-04). This is
   Poiseuille's fourth-power relationship, stated as a bare factor with no law
   named. It is doing real work in the asthma explanation. Confirm that stating
   it unattributed at KS3 is acceptable, or tell me to soften it to "much less".
10. **Carbon monoxide binds haemoglobin ~200× more strongly than oxygen**, and
    **"a heavy smoker may have a tenth of their haemoglobin unavailable"**
    (b4-04). The 200× figure is standard; the one-tenth figure is at the high
    end of quoted ranges. Confirm both.
11. **Breathing rate driven by carbon dioxide, not oxygen** (b4-04 rung 1 and
    think-again). Correct for normal physiology. Confirm you are happy with the
    flat statement, since the oxygen-driven answer is what most students and
    some textbooks say.
12. **Emphysema described as alveolar walls broken down by enzymes released
    during chronic inflammation, with volume preserved and area lost** (b4-04).
    Confirm the mechanism at this level of detail, and confirm the reversibility
    table: cilia recover over months, CO clears within a day, alveolar walls
    never.
13. **`b4-04` tone.** Same request as B3 flag 9. The lesson states mechanisms
    and reversibility, does not moralise, notes that nicotine dependence is why
    stopping is medical rather than a decision, and signposts a GP or pharmacist.
    The legal line tells a pupil with asthma to follow their own plan and treat a
    failing reliever as an emergency. **Please review the tone as well as the
    science**, and read it against B6 so the two do not diverge.
14. **Doll and Hill** (b4-04 stretch), including Doll giving up smoking two
    years into his own study. Standard history; confirm.
15. **The compensation point is taught by name** (b4-05). It is normally a GCSE
    or A-level term. It is introduced as a label for something the student has
    already produced on the bench rather than as vocabulary to learn. Confirm, or
    tell me to keep the phenomenon and drop the name.
16. **Rates in `b4-05` are relative units, not measured**, and the light level at
    which they balance varies hugely by species. Flagged in the legal line.
    Confirm.
17. **Guard cells described as opening the pore by becoming turgid**, with no
    mention of potassium ions or ABA. Confirm this is the right depth.
18. **CAM photosynthesis in the stretch layer** (b4-05), including the claim that
    a pineapple leaf tastes sour in the morning and not in the evening. Confirm
    the tasting claim — it is repeated widely and I have not verified it.
19. **`b4-05` states that B7 owns the photosynthesis reaction** and confines
    itself to gas movement. Confirm that boundary; B7 is not yet authored and
    this is the second lesson in the course to make a claim about what B7 will
    cover.
20. **No anatomical diagrams anywhere in this unit.** One figure slot is named in
    a lesson legal line and is **not yet in the diagram manifest**:
    `b4-gas-exchange-labelled`. Either add it or remove the reference. A labelled
    stoma / guard-cell pair would be the obvious second slot and I have not
    invented one.

---

## 5. Misconception register — `BREATH` family, minted

Thirteen entries, `BREATH-01` to `BREATH-13`, written into
`docs/ks3/misconception-register.md` under a new `BREATH` family row. Same
minting basis as `DIET`: opened by the unit that needed it, all
`review_state: draft`, statements awaiting your review.

Two register notes matter more than the entries:

- **`BREATH-06`/`BREATH-07` are `PART-10`/`PART-11` for the third time.** The
  register's own `PART-10` entry already names B4 `alveoli-built-for-exchange` as
  a required re-confrontation site, so this is the register working as designed
  rather than duplication. The confrontation B4 adds and the earlier two lack is
  the two-way crossing counter — molecules crossing *outwards* stay visible in
  every state.
- **`BREATH-12`/`BREATH-13` are, in my view, the most persistent misconception in
  KS3 biology**, and B7 is where they do the real damage. The register lists B7
  `the-photosynthesis-reaction` and `why-almost-all-life-depends-on-it` as
  resurfacing sites and they should re-confront, not restate.

`FORCE`, `BODY` and `ATOM` remain unminted and are **not** cited anywhere in this
unit.

---

## 6. For Code

- Four instruments in §3; `gas-compare` is DOM-only and cheapest.
- Every slider is bound to `input` **and** `change`.
- **Nothing in this unit animates and nothing uses a timer.** All four
  instruments are pure functions of state, driven by CSS transitions only, all of
  which are disabled under `prefers-reduced-motion`.
- Rail stops: four in every lesson.
- Cross-links use generator output names. Outward links go to `b1-03`, `b1-05`,
  `b2-03`, `b3-07`, `c1-04`, `c1-05` and `c1-06`.
- **`b4-02` carries a visible "Leans on · Physics" panel** because architecture
  §7.1 marks the lesson *requires P5 Pressure* and P5 does not exist. The panel
  points at C1 `gas-pressure` for the qualitative rule and states that P5 owns
  the quantitative treatment. **When P5 is authored, re-read that panel rather
  than assuming it is still right.** There is no code dependency on P5 — nothing
  imported, nothing shared. The dependency is entirely editorial.
- `b4-03`'s four gradient states are a lookup table in the logic class, not a
  computed simulation. If you want it computed, the two switches become rate
  terms and the table goes — but the four narrative notes are hand-written per
  state and would need rewriting.
