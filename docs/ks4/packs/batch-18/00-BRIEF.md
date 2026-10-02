# KS4 Batch 18 — Design input pack

Mide's ruling, 2 Oct 2026: **Design authors and draws every KS4 lesson from batch 4 on.** Code built this pack, will port your pages, check the science and ship them, exactly as for the pilot.

## Read first

- `docs/ks4/architecture.md` — the ten laws, the families, the CFIFA amendment, and **the two amendments of 2 Oct 2026** (Design writes the lessons; the four lesson rules).
- The pilot, as the bar and the template: `docs/ks4/design-reference/pilot/` (your delivery, unmodified) and the live pages it became.
- This file, then `FLAGS.md` (science you must not repeat), then each lesson's `04-checked-science-source/` file, then `05-diagram-library/README.md`.

## The four lesson rules (Mide, 2 Oct 2026) — apply to every lesson here

1. **Start here is a two-option guess**, framed as a guess, answerable from everyday experience on every route; the reveal is encouraging either way and leads straight into the teaching.
2. **Equations are formula triangles you can cover** — in the equation block, the equation-sheet panel and CFIFA's Formula step. A square or a ½ gets its own extra line (square-root, ×2).
3. **Teach every step before you test it.** A calculation that chains two equations gets its own "Step 1 … Step 2 …" worked example before any pupil does one; CFIFA on each step.
4. **Practice is the same size in every lesson** — same number of questions at each rung of the end practice and the exam ladder. Set the number once (at least the content-standards floor) and keep it across the batch.

Each lesson below says which calculations chain, which equations need triangles, and how many verbatim quiz items are usable; the rest of each bank is yours to write to the fixed size.

## Lessons

| # | lesson | slug | subject · topic | source file |
|---|---|---|---|---|
| 1 | Poles of a Magnet and Permanent Magnetism | `poles-of-a-magnet` | Phys · magnetism | `04-checked-science-source/physics-6.7.1.1-poles-of-a-magnet.md` |
| 2 | Magnetic Fields | `magnetic-fields` | Phys · magnetism | `04-checked-science-source/physics-6.7.1.2-magnetic-fields.md` |
| 3 | Electromagnetism | `electromagnetism` | Phys · magnetism | `04-checked-science-source/physics-6.7.2.1-electromagnetism.md` |
| 4 | Fleming's Left-Hand Rule and the Motor Effect | `flemings-left-hand-rule` | Phys · magnetism | `04-checked-science-source/physics-6.7.2.2-flemings-left-hand-rule.md` |
| 5 | Electric Motors | `electric-motors` | Phys · magnetism | `04-checked-science-source/physics-6.7.2.3-electric-motors.md` |
| 6 | Loudspeakers and Headphones | `loudspeakers-headphones` | Phys · magnetism | `04-checked-science-source/physics-6.7.2.4-loudspeakers-headphones.md` |
| 7 | Induced Potential and the Generator Effect | `induced-potential` | Phys · magnetism | `04-checked-science-source/physics-6.7.3.1-induced-potential.md` |
| 8 | Uses of the Generator Effect | `uses-generator-effect` | Phys · magnetism | `04-checked-science-source/physics-6.7.3.2-uses-generator-effect.md` |
| 9 | Microphones | `microphones` | Phys · magnetism | `04-checked-science-source/physics-6.7.3.3-microphones.md` |
| 10 | Transformers | `transformers` | Phys · magnetism | `04-checked-science-source/physics-6.7.3.4-transformers.md` |
| 11 | Our Solar System and Gravity | `solar-system-gravity` | Phys · space | `04-checked-science-source/physics-6.8.1-solar-system-gravity.md` |
| 12 | Gravity, Stable Orbits and Orbital Speed | `gravity-stable-orbits` | Phys · space | `04-checked-science-source/physics-6.8.1-gravity-stable-orbits.md` |
| 13 | Dark Matter and Dark Energy | `dark-matter-dark-energy` | Phys · space | `04-checked-science-source/physics-6.8.4-dark-matter-dark-energy.md` |

True routes, layers and families are in each lesson's entry below; they come from the AQA specification's own labels, checked by an examiner, and where they differ from what the site ships today the entry says so.

## Per lesson

### 1. Poles of a Magnet and Permanent Magnetism
`poles-of-a-magnet` · Physics / magnetism · AQA refs (8464 6.7.1.1; 8463 4.7.1.1) · true routes: CF CH TF TH

- **Family:** CONTRAST — permanent vs induced magnet is the spec's own "describe the difference" (BATCH-PLAN's suggestion kept).
- **Flagship (a suggestion, not a spec):** bring a bar magnet's N or S end to a permanent magnet, then to an unmagnetised steel or iron bar, and predict attract/repel before each — the permanent magnet sometimes repels, the induced one always attracts.
- **Route layers:** none — whole page base (8464 6.7.1.1 = 8463 4.7.1.1, no HT or physics-only label).
- **Required practical:** none.
- **Calculations:** none.
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "All metals stick to magnets" — only iron, steel, nickel and cobalt are magnetic materials; aluminium and copper are not.
  - "A magnet can repel a nail" — induced magnetism always causes attraction; repulsion proves both are magnets.
  - "Induced magnets are made of iron" — any magnetic material placed in a field becomes an induced magnet.
  - "A permanent magnet can never lose its magnetism" — it keeps its own field, but can be weakened.
  - "The force is strongest in the middle of the magnet" — the forces are strongest at the poles.
- **"Start here" access note (rule 1):** fridge magnets stick to a steel fridge door but not to an aluminium can or a wooden door.
- **Practice (rule 4):** 1 verbatim quiz item usable on all four routes (q1). q2 not usable (POLES-OF-A-MAGNET-F1). Design tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md` — must draw: two magnets attracting/repelling (`two_magnets()` exists); a magnet inducing an opposite pole in the near end of an iron/steel bar (missing). No domain figure needed (off-spec).
- **Examiner tip:** none approved.

---

### 2. Magnetic Fields
`magnetic-fields` · Physics / magnetism · AQA refs (8464 6.7.1.2; 8463 4.7.1.2) · true routes: CF CH TF TH

- **Family:** MODEL — field lines are a model of an invisible field: direction from the force on a north pole, strength from spacing (BATCH-PLAN's suggestion kept).
- **Flagship (a suggestion, not a spec):** drag a plotting compass round a bar magnet, dropping dots to build field lines that the pupil then joins and arrows.
- **Route layers:** none — whole page base (8464 6.7.1.2 = 8463 4.7.1.2).
- **Required practical:** none. The source's "RP21" is not an AQA RP (MAGNETIC-FIELDS-F1); compass plotting is a spec method skill (WS 2.2), taught without an RP badge.
- **Calculations:** none.
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "Field lines go from S to N" — the direction is the force on a north pole: N → S outside the magnet.
  - "Field lines can cross" — the field has one direction at each point, so lines never cross.
  - "The field is the same everywhere round the magnet" — strongest at the poles, weaker further away; spacing shows it.
  - "A compass's north end points to the Earth's north magnetic pole, so that's a north pole" — opposites attract: the pole near geographic north is a magnetic south pole.
  - "The field only exists where the lines are drawn" — lines are a model; the field fills the whole region.
- **"Start here" access note (rule 1):** a compass needle points north wherever you stand, and swings when a magnet comes near.
- **Practice (rule 4):** 2 verbatim quiz items, both usable on all four routes (q1, q2). Design tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md` — must draw: bar-magnet field pattern (`bar_magnet_field()`); compasses round a magnet (`magnet_compasses()`); Earth's field as a bar magnet with its S pole near geographic north (missing).
- **Examiner tip:** none approved.

---

### 3. Electromagnetism
`electromagnetism` · Physics / magnetism · AQA refs (8464 6.7.2.1; 8463 4.7.2.1) · true routes: CF CH TF TH

- **Family:** SYSTEM — current, coil shape, turns and core each change one strong field; the parts act together (BATCH-PLAN's suggestion kept).
- **Flagship (a suggestion, not a spec):** straighten a wire into a coil, add turns, slide in an iron core and switch the current, watching the field lines (and the paper clips lifted) change at each step.
- **Route layers:**
  - triple (TF TH): "8463 4.7.2.1 (Physics only) Students should be able to interpret diagrams of electromagnetic devices in order to explain how they work." — e.g. the electric bell or a relay.
  - No HT layer: 6.7.2.1 has no HT content. Both frozen `higher` copies are wrong for this page and must not be used (ELECTROMAGNETISM-F1, -F2).
- **Required practical:** none. The source's "RP21" is not an AQA RP (ELECTROMAGNETISM-F4).
- **Calculations:** none.
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "A wire's field goes out from the wire like spokes" — the field lines are circles round the wire.
  - "A steel core is better because steel is stronger" — steel stays magnetised; soft iron switches off with the current.
  - "Current flows through the iron core" — current flows in the coil; the core becomes an induced magnet.
  - "Coiling the wire doesn't change anything, it's the same wire" — in a solenoid the fields of all the turns add up into a strong, uniform field inside.
  - "Further from the wire the field is the same" — it gets weaker with distance.
- **"Start here" access note (rule 1):** a scrapyard crane picks up a car and drops it when the current is switched off.
- **Practice (rule 4):** 1 verbatim quiz item usable on all four routes (q1). q2 not usable as written (ELECTROMAGNETISM-F3). Design tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md` — must draw: field round a straight wire with direction (`current_wire_field()`); solenoid field with N/S ends (`solenoid_field()`, `solenoid()`); TF TH layer: an electric bell or relay (missing).
- **Examiner tip:** none approved.

---

### 4. Fleming's Left-Hand Rule and the Motor Effect
`flemings-left-hand-rule` · Physics / magnetism · AQA refs (8464 6.7.2.2; 8463 4.7.2.2) · true routes: CH TH

- **Family:** QUANTITATIVE — F = BIl is the lesson's calculation; the left-hand rule supplies the direction (BATCH-PLAN's suggestion kept).
- **Flagship (a suggestion, not a spec):** a wire between two poles where the pupil flips the current or the field and sets B, I and l, predicting the force's direction with a left hand before the wire jumps, and its size with F = BIl.
- **Route layers:**
  - higher (whole page): "8464 6.7.2.2 Fleming's left-hand rule (HT only)" = 8463 4.7.2.2 (HT only).
  - No triple layer. Loudspeakers and the generator effect in the source are other lessons' physics-only content (FLEMINGS-LEFT-HAND-RULE-F3, -F4).
- **Required practical:** none.
- **Calculations:**
  - F = B I l (and rearranged for B, I or l). **Chains equations? no.** Units to convert: cm → m, mm → m, mA → A, mT → T. HT.
- **Equations that need formula triangles (rule 2):**
  - F = B I l — On the sheet (8464 sheet for CH; 8463 sheet for TH; both June 2026, HT). Triangle: F on top; B, I, l along the bottom. Cover B → B = F ÷ (I l); cover I → I = F ÷ (B l); cover l → l = F ÷ (B I). No square or ½.
- **Misconceptions to confront:**
  - "Use whichever hand" — it is the LEFT hand.
  - "The force is along the field" or "along the current" — the force is at right angles to both.
  - "A bigger current flips the force" — size changes the force's size; reversing current or field flips its direction.
  - "A wire along the field lines still feels a force" — parallel to the field, there is no force.
  - "Put the length in cm, it's fine" — l must be in metres for F in newtons.
- **"Start here" access note (rule 1):** a fan or toy car motor spins when a battery is connected, and spins the other way when the battery is turned round.
- **Practice (rule 4):** 1 verbatim quiz item usable on CH and TH (q2). q1 not usable — wrong key (FLEMINGS-LEFT-HAND-RULE-F1). The FIFA is usable verbatim with its examined Convert line. Design writes a second worked example that needs a conversion (F7) and tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md` — must draw: Fleming's left hand with three perpendicular fingers labelled; wire between N and S poles with current and force arrows (`motor_effect()`).
- **Examiner tip:** none approved.

---

### 5. Electric Motors
`electric-motors` · Physics / magnetism · AQA refs (8464 6.7.2.3; 8463 4.7.2.3) · true routes: CH TH

- **Family:** SYSTEM — coil, field, commutator and brushes only make continuous rotation working together (BATCH-PLAN's suggestion kept).
- **Flagship (a suggestion, not a spec):** a coil seen end-on between N and S that the pupil steps round a quarter turn at a time, with and without the commutator, marking the force on each side before each step.
- **Route layers:**
  - higher (whole page): "8464 6.7.2.3 Electric motors (HT only)" = 8463 4.7.2.3 (HT only).
  - triple-higher (TH only, optional): regenerative braking — the motor working as a generator, "8463 4.7.3 Induced potential… (physics only) (HT only)". Not on CH (ELECTRIC-MOTORS-F2).
- **Required practical:** none.
- **Calculations:** none. (F = BIl is taught on `flemings-left-hand-rule`; link to it, don't re-teach.)
- **Equations that need formula triangles (rule 2):** none new.
- **Misconceptions to confront:**
  - "Both sides of the coil get pushed the same way" — current runs opposite ways in the two sides, so the forces are opposite and make a turning effect.
  - "The commutator turns AC into DC" — in a motor it reverses the current in the coil every half turn.
  - "At vertical the forces vanish" — they still act but pass through the axis, so they cannot turn it; momentum carries it past and the commutator swaps the current.
  - "The brushes spin with the coil" — the brushes stay still; the commutator turns against them.
  - "Reverse the current and the field together and it spins backwards" — reversing both leaves the direction unchanged.
- **"Start here" access note (rule 1):** a toy car or fan motor spins one way, and the other way when the battery is turned round.
- **Practice (rule 4):** CH: 0 verbatim items usable (q1 wrong wx2 — ELECTRIC-MOTORS-F1; q2 is TH-only content — F2). TH: 1 (q2, feedback caveat in F2). Design tops the bank up to the batch's fixed size on both routes.
- **Diagrams:** see `05-diagram-library/README.md` — must draw: coil end-on between poles with force arrows on each side (`motor_coil_forces()`); split-ring commutator and brushes showing the swap each half turn (missing).
- **Examiner tip:** none approved.

---

### 6. Loudspeakers and Headphones
`loudspeakers-headphones` · Physics / magnetism · AQA refs (8464 —; 8463 4.7.2.4) · true routes: TH

- **Family:** PROCESS — a signal becomes a force becomes a vibration becomes a sound, in a fixed order (BATCH-PLAN's suggestion kept).
- **Flagship (a suggestion, not a spec):** a cross-section speaker where the pupil sets the AC signal's frequency and size and predicts the cone's motion and the sound before it plays.
- **Route layers:**
  - whole page: "8463 4.7.2.4 Loudspeakers (physics only) (HT only)" — no base content to split out.
- **Required practical:** none.
- **Calculations:** none.
- **Equations that need formula triangles (rule 2):** none. (F = BIl is taught on `flemings-left-hand-rule`; link to it, don't re-teach.)
- **Misconceptions to confront:**
  - "DC would work, just less well" — a steady current gives a steady force: the cone moves once and stays (q1).
  - "A bigger current makes a higher note" — current size sets loudness; the signal's frequency sets the pitch.
  - "High frequency means a low, deep sound" — high frequency = high pitch (q2).
  - "The magnet makes the sound" — the magnet only provides the field; the changing current makes the force change.
  - "The coil pushes air out like a fan" — the cone vibrates back and forth, making compressions and rarefactions (pressure variations).
- **"Start here" access note (rule 1):** everyone has felt a speaker cone buzz or seen a bass speaker pulse at a party.
- **Practice (rule 4):** 2 verbatim quiz items, both usable on TH (q2's option 1 is a deliberate distractor, not a defect — LOUDSPEAKERS-HEADPHONES-F4). Design tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md` — must draw: loudspeaker cross-section (permanent magnet, voice coil on the cone, cone, AC in, compressions/rarefactions out); nothing exists to reuse.
- **Examiner tip:** none approved.

---

### 7. Induced Potential and the Generator Effect
`induced-potential` · Physics / magnetism · AQA refs (8464 —; 8463 4.7.3.1) · true routes: TH

- **Family:** MODEL — one idea (relative movement between conductor and field induces a pd) explains every case (BATCH-PLAN's suggestion kept).
- **Flagship (a suggestion, not a spec):** a magnet-and-coil bench: move the magnet in, out or not at all, flip it, change speed and turns, close or open the circuit — predict the meter each time.
- **Route layers:**
  - whole page: "8463 4.7.3.1 Induced potential (HT only)" under "4.7.3 … (physics only) (HT only)" — no base content to split out.
- **Required practical:** none.
- **Calculations:** none.
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "A magnet sitting inside a coil makes a current" — only relative movement or a changing field induces a pd (q1).
  - "A stronger magnet held still gives more current" — still means nothing; strength only matters while moving.
  - "There's always a current" — a pd is induced across the ends; a current flows only in a complete circuit.
  - "The induced current helps the magnet along" — its field opposes the change, so you have to do work.
  - "Pulling the magnet out gives the same current" — reversing the movement (or flipping the magnet) reverses the current.
- **"Start here" access note (rule 1):** a bike dynamo light, or a shake torch, glows brighter the faster you go.
- **Practice (rule 4):** 2 verbatim quiz items, both usable on TH; q2 is alternator content (4.7.3.2) — use it here or in `uses-generator-effect`, not both (INDUCED-POTENTIAL-F6). Design tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md` — must draw: magnet moving into / out of a coil with a centre-zero meter; nothing exists to reuse. Show direction by meter deflection, not by Fleming's right-hand rule (INDUCED-POTENTIAL-F2).
- **Examiner tip:** none approved.

---

### 8. Uses of the Generator Effect
`uses-generator-effect` · Physics / magnetism · AQA refs (8464 —; 8463 4.7.3.2) · true routes: TH

- **Family:** CONTRAST — alternator vs dynamo, one discriminating difference: slip rings or split-ring commutator (BATCH-PLAN's suggestion kept).
- **Flagship (a suggestion, not a spec):** one rotating coil with a swappable connector (slip rings / split ring) drawing its pd–time graph live as it turns; the pupil predicts the graph before each run.
- **Route layers:**
  - whole page: "8463 4.7.3.2 Uses of the generator effect (HT only)" under "4.7.3 … (physics only) (HT only)" — no base content to split out (UK mains 50 Hz is base, 8464 6.2.3.1, prior knowledge).
- **Required practical:** none.
- **Calculations:** none required. (Reading a period off a pd–time graph is graph interpretation, not a set equation.)
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "Spin it faster and you get DC" — speed changes size and frequency; only the connector decides ac or dc (q1).
  - "A stronger magnet makes it AC" — strength changes the size only (q1).
  - "Slip rings swap the connections" — slip rings never swap; the split-ring commutator does.
  - "DC from a dynamo is a flat line" — it is humps, all one side of zero, touching zero twice a turn.
  - "Faster just makes the peaks taller" — faster makes them taller AND closer together.
- **"Start here" access note (rule 1):** a wind-up or hand-crank torch: turn the handle and the bulb lights.
- **Practice (rule 4):** 1 verbatim quiz item usable on TH (q1). Not usable: q2 (back-emf, off-spec — USES-GENERATOR-EFFECT-F1). Design tops the bank up to the batch's fixed size, with pd–time graph items (F2).
- **Diagrams:** see `05-diagram-library/README.md` — must draw: alternator (coil, slip rings, brushes) beside dynamo (coil, split-ring commutator, brushes), each with its pd–time graph; nothing exists to reuse.
- **Examiner tip:** none approved.

---

### 9. Microphones
`microphones` · Physics / magnetism · AQA refs (8464 —; 8463 4.7.3.3) · true routes: TH

- **Family:** PROCESS — sound → diaphragm → coil moves → pd induced → signal, in a fixed order (BATCH-PLAN's suggestion kept); its partner is `loudspeakers-headphones` run backwards.
- **Flagship (a suggestion, not a spec):** the loudspeaker cross-section from lesson 6 with the arrows reversed — the pupil sends in a quiet/loud, low/high sound and predicts the signal that comes out.
- **Route layers:**
  - whole page: "8463 4.7.3.3 Microphones (HT only)" under "4.7.3 … (physics only) (HT only)" — no base content to split out.
- **Required practical:** none.
- **Calculations:** none.
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "A microphone uses the motor effect, like a speaker" — it uses the generator effect: movement in, current out (q1).
  - "The microphone changes the pitch" — the signal has the same frequency as the sound (q2).
  - "The magnet vibrates" — the diaphragm and coil vibrate; the magnet stays still.
  - "Louder sound gives a higher frequency signal" — louder gives a bigger signal at the same frequency.
- **"Start here" access note (rule 1):** tapping a microphone makes a thump through the speakers — your tap became a signal.
- **Practice (rule 4):** 1 verbatim quiz item usable on TH (q1). Not usable as written: q2 (wx2 asserts the wrong answer — MICROPHONES-F2). Design tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md` — must draw: moving-coil microphone cross-section (diaphragm, coil, permanent magnet, output leads), ideally the lesson-6 speaker figure mirrored; nothing exists to reuse.
- **Examiner tip:** none approved.

---

### 10. Transformers
`transformers` · Physics / magnetism · AQA refs (8464 6.2.4.3 HT for Vp Ip = Vs Is; 8463 4.7.3.4) · true routes: TH

- **Family:** QUANTITATIVE — the turns ratio and power balance carry the idea (BATCH-PLAN's suggestion kept); the "why" (ac only) comes first, from the generator effect.
- **Flagship (a suggestion, not a spec):** a transformer with turn-count sliders on both coils and a load: the pupil predicts Vs and both currents before each change, and sees power in = power out.
- **Route layers:**
  - construction, ac-only, turns ratio: "8463 4.7.3.4 Transformers (HT only)" under "4.7.3 … (physics only) (HT only)".
  - Vp Ip = Vs Is: "8464 6.2.4.3 … Higher tier only" (also 8463 4.7.3.4) — a higher point; on this TH page it is simply taught.
  - step-up/step-down in the National Grid and why high pd is efficient: base (8464 6.2.4.3), prior knowledge from `national-grid`.
- **Required practical:** none.
- **Calculations:**
  - Turns ratio: Vp/Vs = np/ns (find Vs, Vp, ns or np). Chains equations? no. Convert: kV → V when the pds are in different units (or keep both in the same unit — the ratio allows it; say so). HT.
  - Current from power: Vp Ip = Vs Is, or Ip = P ÷ Vp for a given power output (100 % efficient). Chains equations? no (one step). Convert: kW → W, kV → V, mA → A. HT.
  - Turns → current: chains equations? **yes** — Step 1 Vs = Vp × ns ÷ np; Step 2 Ip = (Vs × Is) ÷ Vp (or Is from Ip). Convert: kV, mA. HT. Needs its own worked example (TRANSFORMERS-F5).
  - Transmission loss (optional, from theory 3): chains equations? **yes** — Step 1 I = P ÷ V; Step 2 P_loss = I² R. Convert: MW → W, kV → V. Base equations (both on both sheets). If used, needs its own worked example; do not copy the source's "10,000 times less" (TRANSFORMERS-F1).
- **Equations that need formula triangles (rule 2):**
  - Vp/Vs = np/ns — **On the sheet** (8463, HT). Four quantities, so not a three-corner triangle: show the four covered forms (e.g. cover Vs → Vs = Vp × ns ÷ np). Show it in the sheet's form, lowercase n.
  - Vp Ip = Vs Is — **On the sheet** (8463 and 8464, HT). Teach as power in = power out, each side a P = V × I triangle (P top; V, I bottom).
  - P = V I — **On the sheet** (both): P top; V, I bottom.
  - P = I² R — **On the sheet** (both): P top; I², R bottom; finding I needs its own square-root line.
- **Misconceptions to confront:**
  - "A step-up transformer gives you more power" — power out can't exceed power in; pd up means current down.
  - "Transformers work on a battery" — dc gives a steady field, so nothing is induced (q1).
  - "Current flows through the core from one coil to the other" — the coils aren't connected; the changing field links them.
  - "High voltage makes electricity reach homes faster" — it lowers the current, cutting I²R heating (q2).
  - "More turns on the primary steps up" — step-up needs more turns on the secondary.
- **"Start here" access note (rule 1):** a phone charger plugs into a 230 V socket but the phone only takes about 5 V — something in the plug changes it.
- **Practice (rule 4):** 2 verbatim quiz items usable on TH (q1, q2) and the FIFA (one-step, nothing to convert; corrected Convert line in the source). Design tops the bank up to the batch's fixed size, including a conversion example and the chained turns → current case.
- **Diagrams:** see `05-diagram-library/README.md` — must draw: primary and secondary coils on an iron core with turns and pds labelled; National Grid chain (step-up → cables → step-down); nothing exists to reuse.
- **Examiner tip:** none approved.

---

### 11. Our Solar System and Gravity
`solar-system-gravity` · Physics / space · AQA 8463 4.8.1.1; 8463 4.8.1.3 (non-HT core + HT layer); no 8464 ref · true routes TF TH

**Family:** CLASSIFY — the spec's task is "describe the similarities and distinctions between the planets, their moons, and artificial satellites": body → type → what it orbits → what holds it there. (Plan's suggestion kept; "formation" reduced to one line — star formation is `stellar-evolution`'s.)

**Flagship (a suggestion, not a spec):** Sort Sun, planets, dwarf planets, moons and artificial satellites by what each orbits and whether it is natural, with gravity named as the force every time.

**Route layers:**
- Triple Higher — 8463 4.8.1.3 "(HT only) … for a stable orbit, the radius must change if the speed changes" and "(HT only) … changing velocity but unchanged speed": closer orbit = faster. One statement plus a link to `gravity-stable-orbits`; q1 here (F1).

**Required practical:** none.

**Calculations:** None. Scale figures (AU, light-year) are off-spec — no calculation, no CFIFA (F6).

**Equations that need formula triangles (rule 2):** none.

**Misconceptions to confront:**
- "The Moon isn't a satellite — satellites are man-made." — moons are natural satellites (4.8.1.1).
- "Pluto is a planet." — eight planets; Pluto is a dwarf planet (4.8.1.1).
- "In space there's no gravity, that's why satellites float." — gravity is the force that keeps every orbit going (4.8.1.3).
- "The Sun is the biggest thing there is." — the solar system is a small part of the Milky Way galaxy (4.8.1.1).
- (TH) "An orbit is balanced forces." — gravity is unbalanced; it turns the motion towards the centre (4.8.1.3 HT).

**"Start here" access note (rule 1):** Everyone has seen the Moon go round the Earth across a month — what keeps it going round instead of flying off?

**Practice (rule 4):** q2 usable verbatim on TF TH (1). q1 usable on TH only — HT content (F1). Nothing unusable. Design tops the bank up to the batch's fixed size, including items on planet / dwarf planet / moon / artificial satellite and on the nebula line.

**Diagrams:** see `05-diagram-library/README.md` — existing `figlib/physics.py` `solar_system()` for the structure. Must draw: a planet–moon–artificial-satellite comparison (what orbits what, gravity arrow to the centre each time); TH layer: two orbits, smaller one faster.

**Examiner tip:** none approved.

---

### 12. Gravity, Stable Orbits and Orbital Speed
`gravity-stable-orbits` · Physics / space · AQA 8463 4.8.1.3 (HT bullets); supporting 8463 4.5.6.1.3 / 8464 6.5.4.1.3 (HT); no 8464 space ref · true routes TH (route audit's reading, confirmed: this page's content is the HT part of 4.8.1.3; the non-HT core is on `solar-system-gravity`)

**Family:** MODEL — one idea (gravity weakens with distance and is the only force on the orbiter) predicts every change: speed up → bigger orbit, slow down → smaller orbit, drag → decay. (Plan's suggestion kept.)

**Flagship (a suggestion, not a spec):** An orbit instrument: change the satellite's speed at fixed radius, predict out or in, then watch the radius change.

**Route layers:**
- Triple Higher — the whole page: 8463 4.8.1.3 "(physics only)" "(HT only) for circular orbits, the force of gravity can lead to changing velocity but unchanged speed; (HT only) for a stable orbit, the radius must change if the speed changes."

**Required practical:** none.

**Calculations:** None. F = Gm₁m₂/r² is off-spec and not on the 8463 sheet — no triangle, no CFIFA (F2).

**Equations that need formula triangles (rule 2):** none.

**Misconceptions to confront:**
- "Constant speed means no acceleration." — in a circle the velocity changes direction, so it accelerates; gravity does it (4.8.1.3 HT).
- "If it goes faster it stays in the same orbit." — for a stable orbit the radius must change if the speed changes (4.8.1.3 HT).
- "To go higher you slow down." — you speed up to rise; the higher orbit is then slower (4.8.1.3 HT).
- "A falling satellite drops straight down." — drag shrinks the orbit gradually until re-entry.
- "Satellites stay up because there's no gravity there." — gravity is weaker but is the force holding the orbit (4.8.1.3).

**"Start here" access note (rule 1):** Swing a ball on a string round your head and let go — does it fly off in a straight line or keep curving?

**Practice (rule 4):** q1 and q2 usable verbatim on TH (2). Nothing unusable (q1 wx1 wording imprecise but usable — F5). Design tops the bank up to the batch's fixed size, including items on "changing velocity, unchanged speed" and on speed-up → higher orbit.

**Diagrams:** see `05-diagram-library/README.md` — nothing exists (same gap as batch-17 `motion-in-a-circle`). Must draw: circular orbit with velocity tangent and gravity to the centre at several points; speed-change → new orbit radius (no spirals except for drag).

**Examiner tip:** none approved.

---

### 13. Dark Matter and Dark Energy
`dark-matter-dark-energy` · Physics / space · AQA 8463 4.8.2 (physics only, not HT); context 8463 4.8 intro; no 8464 ref (frozen "6.8.4 (HT only)" is wrong — F1) · true routes TF TH (site ships TH; moving under the route-flag PR)

**Family:** CONTRAST — dark matter vs dark energy: one is unseen mass that pulls (holds galaxies together, bends light), the other is the unknown cause of the expansion speeding up. (Plan's suggestion kept.)

**Flagship (a suggestion, not a spec):** Two evidence cards — a galaxy whose outer stars don't slow down, and distant supernovae receding ever faster — each pupil-matched to "dark matter" or "dark energy", ending on "we don't know what either is".

**Route layers:** none — whole page is triple (8463 4.8.2 "(physics only)"), same on TF and TH; never show the frozen `higher` text's "HT only" label (F1).

**Required practical:** none.

**Calculations:** None.

**Equations that need formula triangles (rule 2):** none.

**Misconceptions to confront:**
- "Dark matter and dark energy are the same thing." — one is mass that attracts; the other drives the expansion ever faster (4.8 intro).
- "Dark matter is black stuff you can see as dark patches." — it does not emit electromagnetic radiation; we detect it only by gravity (4.8 intro).
- "Dark matter doesn't affect light at all." — its gravity bends light (4.8 intro, "bends light").
- "Gravity should slow the expansion, so it is slowing." — since 1998 supernovae show distant galaxies receding ever faster (4.8.2).
- "Scientists understand what the universe is made of." — much is not understood, e.g. dark mass and dark energy (4.8.2).

**"Start here" access note (rule 1):** Throw a ball up and it slows down — if the whole universe is flying apart, would you guess it's slowing down or speeding up?

**Practice (rule 4):** q1 and q2 usable verbatim on TF TH (2). Nothing unusable. Design tops the bank up to the batch's fixed size, including items on the 1998 supernova observation and on "not understood"; no item keyed on a percentage (F2).

**Diagrams:** see `05-diagram-library/README.md` — nothing exists. Must draw: galaxy rotation curve (observed flat vs predicted falling from visible mass); a lensing sketch (light bent round unseen mass). A 5 / 27 / 68 composition picture is optional context.

**Examiner tip:** none approved.
