# MRB-335 — KS3 physics bank top-up (P1–P12)

The physics lane's log. One section per unit, in Rainford's autumn teaching
order (P3, P1, P4, P2, P8, P5, then P6…P12). Every unit here reaches **52 rows
in each of the three bands**, appended at `bank_position` 12 and upwards, so
the twelve rows AUTO composition reads are byte-identical to what they were.

Both gates are run after every unit, from the worktree root:

```bash
python3 -m ks3_data.question_bank
python3 verify_questions.py
```

⚠️ **This worktree has a co-tenant.** A chemistry lane is topping up
`ks3_data/c*/` in the same checkout, so the bank totals printed by the gates
include its rows as well as this lane's, and every commit here is scoped by
hand (`git add ks3_data/p<n>/ docs/mrb335/ks3-content-physics.md`) rather than
with `-A`.

---

## P3 · Describing motion — 3 lessons, 120 new rows (40 per band)

Unit total after the top-up: **52 easier / 52 standard / 52 harder**.

| lesson | easier | standard | harder |
|---|---|---|---|
| 01 speed | e05–e17 (13) | s05–s17 (13) | h05–h17 (13) |
| 02 distance–time graphs | e05–e17 (13) | s05–s17 (13) | h05–h17 (13) |
| 03 relative motion | e05–e18 (14) | s05–s18 (14) | h05–h18 (14) |

**Where the demand sits.** Easier rows are one-step recall — the unit, the
division, reading one point off a line, one relative-speed rule. Standard rows
apply the idea in a context the lesson used: light gates, a river, a walkway, a
graph section. Harder rows are two-step or unfamiliar: a unit conversion plus a
rearrangement (`p3-01-h06`, `p3-03-h09`), an average across legs of different
duration (`p3-01-h05`, `p3-02-h14`), or an explain-why with a number attached
(`p3-02-h13`, `p3-03-h18`).

**Lesson 02 and the no-diagrams rule.** Distance–time graphs are described in
words throughout — "a line runs straight from 10 m at 5 s to 40 m at 15 s" —
never "the graph above". That follows the twelve rows already in the file, and
it is what makes the row readable on the assignment page, away from the lesson.

**Review fixes before commit** (cold re-read of all 120 rows, plus a mechanical
length/markup/spelling/position sweep):

- *Length parity, correct option conspicuously the longest* — `p3-01-s11`,
  `p3-01-s16`, `p3-01-h10`, `p3-01-h13`, `p3-01-h16`, `p3-01-e13`,
  `p3-02-e13`, `p3-02-e14`, `p3-03-h12`. Reworded so no option can be picked
  by length alone; the claims themselves are unchanged.
- *Correct option conspicuously the SHORTEST* — `p3-01-e12` ("0 m/s"),
  `p3-02-e09` ("0 m"), `p3-02-h05` ("4 m/s"), `p3-03-s16`. A bare number
  sitting among three wordy distractors is the same tell in reverse; each was
  given the short reason its distractors already carried.
- *Every calculation re-worked from the stem*, including the distractor
  arithmetic each `why` names — the average-speed legs (h05 in lessons 01 and
  02, `p3-02-h14`), the two river/walkway pairs, the passing-trains 400 m, and
  the 630 km headwind leg. All divide cleanly.
- No duplicate stem or answer set inside a lesson (gated), no ladder rung
  restated (gated), no markup, UK spellings, a unit on every quantity.

Gates after P3: `question_bank` OK, `verify_questions` OK — nine checks clean.

---

## P1 · Energy transfers — 8 lessons, 60 new rows (20 per band)

Unit total: **52 / 52 / 52**. Three per band on lessons 01–04, two per band on
05–08.

| lesson | ids added (each band) |
|---|---|
| 01 energy stores | e05–e07, s05–s07, h05–h07 |
| 02 energy transfers: before and after | e05–e07, s05–s07, h05–h07 |
| 03 conservation of energy | e05–e07, s05–s07, h05–h07 |
| 04 heating and thermal equilibrium | e05–e07, s05–s07, h05–h07 |
| 05 conduction | e05–e06, s05–s06, h05–h06 |
| 06 radiation | e05–e06, s05–s06, h05–h06 |
| 07 insulation | e05–e06, s05–s06, h05–h06 |
| 08 simple machines | e05–e06, s05–s06, h05–h06 |

**The store/pathway discrimination carries the unit**, so it is tested from
several sides rather than once: which of four is a store (`p1-01-e05`), which
item on a child's own list of "kinds of energy" is one (`p1-01-h06`), why
electricity is not (`p1-01-s07`), and a wind-up radio whose whole chain has to
be sorted (`p1-01-s06`).

**`ks3_data/quantities.py` was read and not retyped.** No new row states a
definition of temperature; the two lesson-04 rows that come near it ask instead
what a thermal store depends on besides temperature (`p1-04-e06`) and what
thermal equilibrium is (`p1-04-e05`), so the single owned definition is not
duplicated at a fifth site.

**Review fixes:** thirteen length-parity flags (nine where the correct option
was longest — `p1-02-s07`, `p1-02-h06`, `p1-03-s07`, `p1-03-h05`, `p1-03-h07`,
`p1-04-e05`, `p1-04-s06`, `p1-07-s05`; four where it was conspicuously
shortest — `p1-01-h06`, `p1-03-e06`, `p1-06-e05`, `p1-06-e06`, `p1-08-s06`),
all reworded without changing a claim. One authoring slip caught before the
gate: `p1-05-e06` had been written with a `True if False else False` in a
`correct` field — it evaluated correctly but is not something to leave in a
content file, and it is now a plain `False`. Arithmetic re-worked from the
stems: the 1800 J hairdryer split, the 200 kJ kettle tenth, and all four
machine calculations (`50 N × 2 m`, `150 N × 0.80 m ÷ 600 N`, the 4 m ramp,
the 800 N pulley).

---

## P4 · Forces — 9 lessons, 48 new rows (16 per band)

Unit total: **52 / 52 / 52**. Two per band on lessons 01–07, one per band on
08–09.

| lesson | ids added (each band) |
|---|---|
| 01 what a force is | e05–e06, s05–s06, h05–h06 |
| 02 drawing and adding forces | e05–e06, s05–s06, h05–h06 |
| 03 balanced and unbalanced | e05–e06, s05–s06, h05–h06 |
| 04 what forces do to motion | e05–e06, s05–s06, h05–h06 |
| 05 friction | e05–e06, s05–s06, h05–h06 |
| 06 air and water resistance | e05–e06, s05–s06, h05–h06 |
| 07 moments | e05–e06, s05–s06, h05–h06 |
| 08 springs and Hooke's law | e05, s05, h05 |
| 09 non-contact forces | e05, s05, h05 |

Every weight is worked from `mass × 10 N/kg` and the classic slip — reading the
mass in kilograms as a force in newtons — is a distractor at every band.
Moments carry their unit (N m, never N), and the cm-not-converted error is a
named distractor at `p4-07-s05`.

**Review fixes:** six length flags reworded. One finding that was not about
length: `p4-07-h06` (the wheelbarrow) had a distractor — "the handles are
further from the pivot, so a smaller lift gives a bigger moment" — that is
**true physics**, merely not the answer to the question asked. A distractor a
well-taught student can defend is a defective distractor however carefully the
`why` hedges, so it was replaced with a real misconception ("the wheel carries
the whole weight, so the handles take none of it").

**Two REF flags were reviewed and kept.** `p4-02-e05` and `p4-02-s06` use the
word *diagram* — but in the abstract ("where should an arrow start on a
diagram", "on a scale diagram a 20 N arrow is 4 cm long"), never pointing at
one the child is expected to look at. That is exactly how the twelve rows
already in the file read (`p4-02-e01`, `p4-02-s02`), and both new stems carry
every number they need. The lane's mechanical check was narrowed to deictic
references (*above*, *below*, *shown here*) rather than the bare word.

---

## P2 · Energy at home — 5 lessons, 96 new rows (32 per band)

Unit total: **52 / 52 / 52**. Seven per band on lessons 01–02, six per band on
03–05.

| lesson | ids added (each band) |
|---|---|
| 01 energy in food | e05–e11, s05–s11, h05–h11 |
| 02 power ratings in watts | e05–e11, s05–s11, h05–h11 |
| 03 calculating energy transferred | e05–e10, s05–s10, h05–h10 |
| 04 reading a fuel bill | e05–e10, s05–s10, h05–h10 |
| 05 fuels and energy resources | e05–e10, s05–s10, h05–h10 |

This is the unit where the arithmetic does the teaching, so every calculation
divides cleanly and each distractor is a **named** working error rather than a
near miss: the time left in minutes (`p2-03-s05`, `p2-03-h07`), the kilo
dropped or added twice (`p2-03-h05`, `p2-04-s10`), the division inverted, and
the order-of-magnitude check that catches all of them (`p2-03-s07`). The
rate-versus-total confusion that the unit exists to fix is tested from both
ends — a 5 W charger beating a 1200 W toaster over the day (`p2-02-s05`), and
two heaters of different ratings warming the same room to the same temperature
for the same energy (`p2-02-h05`, `p2-02-h07`).

**Review fixes.** Two duplicate stems were caught by the gate and rewritten
rather than nudged: `p2-02-h07` had reproduced the existing `h03` ("when does a
lower wattage genuinely save energy") and became the two-heaters comparison;
`p2-05-h06` had reproduced `h02` (the all-wind-and-solar objection) and became
a grid battery, which asks the same physics of intermittency from the solution
end instead. Both were visible in the stem list before writing and were
authored anyway — the fast gate is what caught them, which is the argument for
running it per lesson rather than per unit.

Two more distractor sets were rewritten on the cold read, not for length but
because they were **incoherent as written**: `p2-03-h06` had an option reading
"the lamp, at 3.6 MJ against the kettle's 3.6 MJ", which states a difference
and an equality in one line, and `p2-03-h08` had a `why` that contradicted its
own option. Both now carry the two symmetric errors (rating-wins and
time-wins) instead. Five length flags fixed, and one authoring slip of the same
shape as P1's: a `True if 0 else False` in a `correct` field, removed before
the append.

**The lane's length checker was corrected twice during this unit.** It had been
counting "18 000 J" as three words, so every large numeric answer looked
conspicuously long; it now collapses a thousands space before counting. It had
also been flagging the bare word *opposite* — `p2-05-h05` says wood and nuclear
sit in "opposite corners of the grid", which is a description, not a
page reference — so it now looks for deictic phrases only.

---

## P8 · Electric circuits — 7 lessons, 72 new rows (24 per band)

Unit total: **52 / 52 / 52**. Four per band on lessons 01–03, three per band on
04–07.

| lesson | ids added (each band) |
|---|---|
| 01 current and circuits | e05–e08, s05–s08, h05–h08 |
| 02 series and parallel | e05–e08, s05–s08, h05–h08 |
| 03 current at a junction | e05–e08, s05–s08, h05–h08 |
| 04 potential difference | e05–e07, s05–s07, h05–h07 |
| 05 resistance | e05–e07, s05–s07, h05–h07 |
| 06 conductors and insulators | e05–e07, s05–s07, h05–h07 |
| 07 building and measuring a circuit | e05–e07, s05–s07, h05–h07 |

The four named misconceptions of lesson 01 — the bulb using up the current, the
cell holding a store of current, the delay down a long wire, the return wire
not mattering — are each given a row that can only be answered by rejecting
them. Two rows go further than the lesson's own framing without leaving its
scope: `p8-01-h06` puts two cells in a holder facing opposite ways (the pushes
cancel, so nothing lights), and `p8-01-h08` asks why a cell-less loop full of
free electrons carries no current at all. Lesson 02's `h07` is the one
genuinely composite item — two lamps in parallel, that pair in series with a
third — and its answer turns on the single lamp carrying what both branches
carry together.

Every resistance is worked as a ratio from two readings, and the three classic
errors (multiplying, inverting, and leaving milliamps unconverted) each appear
as a named distractor: `p8-05-e06`, `p8-05-s05`, `p8-05-h06`.

**Review fixes.** Twelve length flags, ten reworded and two — `p8-01-h05` and
`p8-07-h06` — lengthened because the correct option was a bare four or five
words among wordy distractors.

**The lane's spelling check was wrong, and P8 is what exposed it.** It had been
flagging *meter* and *meters* as an Americanism for *metre*. In UK English the
INSTRUMENT is a meter — ammeter, voltmeter, "both meters read zero" — and only
the unit of length is a metre; the twelve rows already in `questions_07` use
*meters* throughout. Ten flags here were the checker being wrong, not the
content. It now flags *meter* only when a number stands immediately before it,
which is the one place the length is meant.

---

## P5 · Pressure — 4 lessons, 108 new rows (36 per band)

Unit total: **52 / 52 / 52**. Nine per band on every lesson: `e05–e13`,
`s05–s13`, `h05–h13` in each of the four files.

| lesson | ids added (each band) |
|---|---|
| 01 pressure = force ÷ area | e05–e13, s05–s13, h05–h13 |
| 02 pressure in liquids | e05–e13, s05–s13, h05–h13 |
| 03 upthrust, floating and sinking | e05–e13, s05–s13, h05–h13 |
| 04 atmospheric pressure | e05–e13, s05–s13, h05–h13 |

**The area conversion is the trap this unit turns on**, so it is tested three
ways rather than once: as a bare fact (`p5-01-e08`), inside a calculation
(`p5-01-s08`, 300 cm² on a 150 N box), and as a student's own wrong working to
diagnose (`p5-01-h08`, "400 cm² is 4 m²"). Lesson 01 also carries the two
rearrangements — force from pressure and area, area from force and pressure —
with the inverted division as a named distractor in each.

Lesson 02's rows all turn on the same discrimination: depth and the liquid
decide the pressure, and the amount of liquid never does. Two rows put that
under real strain — the thin pipe that bursts a barrel (`h07`) and the two
tanks holding ten times different volumes to the same depth (`s10`). Lesson 03
separates upthrust from weight in both directions: the same-volume aluminium
and lead blocks get the same upthrust (`s06`), and the boat-and-stone level
question (`h06`) is the one item in the unit a well-taught student can still
get wrong for a good reason.

**Review fixes.** Sixteen length flags reworded, including four where the
correct option was a single word ("rises", "Mercury", "They are equal") among
wordy distractors. Every calculation re-worked from its stem; the jack
(`p5-01-h11`) and the elephant-versus-heel comparison (`p5-01-h07`) are the two
that chain two steps, and both were checked end to end.

**The lane's REF check was too blunt, and a pressure unit is where that shows.**
It had flagged the bare words *above* and *below* — but "the water above the
probe", "one ninth above the surface" and "no air above 100 km" are physical
descriptions, not instructions to look at a picture. Nine flags here were the
checker misreading the subject. It now matches deictic phrases only
(*shown above*, *diagram below*, *this graph*).

---

## P6 · Waves and sound — 9 lessons, 48 new rows (16 per band)

Unit total: **52 / 52 / 52**. Two per band on lessons 01–07, one per band on
08–09.

| lesson | ids added (each band) |
|---|---|
| 01 waves on water | e05–e06, s05–s06, h05–h06 |
| 02 transverse waves and superposition | e05–e06, s05–s06, h05–h06 |
| 03 how sound is made | e05–e06, s05–s06, h05–h06 |
| 04 sound is longitudinal | e05–e06, s05–s06, h05–h06 |
| 05 frequency, pitch and loudness | e05–e06, s05–s06, h05–h06 |
| 06 sound needs a medium | e05–e06, s05–s06, h05–h06 |
| 07 echoes, reflection and absorption | e05–e06, s05–s06, h05–h06 |
| 08 hearing and auditory range | e05, s05, h05 |
| 09 ultrasound at work | e05, s05, h05 |

The out-and-back path is the arithmetic this unit gets wrong most often, so it
is asked three ways: as the plain fact (`p6-07-e06`), as a cliff distance
(`p6-07-s05`) and a sonar depth (`p6-07-h05`), and finally as the consequence
of forgetting it (`p6-07-h06` — the answer comes out twice the true distance,
not half). The independence of pitch and loudness is tested from the amplitude
end (`p6-05-h06`, a string plucked harder) and the speed end (`p6-05-s06`, two
notes arriving together).

**Review fixes.** Five length flags reworded. Then a pattern the row-by-row
read would not have caught: across the 48 new rows the correct option sat in
the **last slot only once**, and in the first slot thirteen times. That is a
tell a test-wise student can use without reading a single stem. Eight rows had
two of their four options swapped — the same four options and the same correct
one, in a different order — bringing the spread to 6 / 20 / 13 / 9. The lane's
mechanical check reports this spread after every unit; it is the reason it does.

---

## P7 · Light — 7 lessons, 72 new rows (24 per band)

Unit total: **52 / 52 / 52**. Four per band on lessons 01–02, three per band on
03–07.

| lesson | ids added (each band) |
|---|---|
| 01 light travels | e05–e08, s05–s08, h05–h08 |
| 02 reflection, mirrors and scattering | e05–e08, s05–s08, h05–h08 |
| 03 refraction | e05–e08, s05–s08, h05–h08 |
| 04 lenses and images | e05–e07, s05–s07, h05–h07 |
| 05 the eye and the camera | e05–e07, s05–s07, h05–h07 |
| 06 colour and the spectrum | e05–e07, s05–s07, h05–h07 |
| 07 why things look coloured | e05–e07, s05–s07, h05–h07 |

Lesson 01's harder rows are all the same calculation at four scales — a torch
across a room, a laser to a wall, a satellite round trip, the Sun — so the
powers of ten are the thing being tested, and every distractor is a specific
slip of three or six decimal places rather than a wrong method. Lesson 02
carries the one item that needs a second step: turning a mirror through 10°
turns the reflected ray through 20°, because the normal moves with the mirror.
Lesson 03 keeps the speed change and the direction change welded together —
`h07` asks whether a pulse really does take longer through 5 cm of glass, which
is the fact that makes refraction more than a rule about bending.

**Review fixes.** One duplicate stem caught by the gate: `p7-07-e07` had
reproduced the existing `e04` (what happens to unreflected light) and was
rewritten as which surface warms most in the same sunlight — the same physics
reached from the thermal end. Eleven length flags reworded. Seven rows had
their option order rotated: the correct answer had landed in the last slot only
six times in 72, and the spread is now 12 / 23 / 24 / 13.

**A third narrowing of the lane's REF check.** It flagged *the picture* five
times — but in lesson 04 "the picture" is the lesson's own name for the image
on the pinhole screen, used throughout the twelve rows already there. It now
matches *the picture above* / *below* only. Between P4, P5 and P7 this check
has been wrong three times and right none: every REF it has raised has been the
physics vocabulary of the unit rather than a page reference. It is kept because
the failure it looks for is real and silent, but its output is treated as a
prompt to read the stem, never as a finding on its own.

---

## P9 · Static electricity — 3 lessons, 120 new rows (40 per band)

Unit total: **52 / 52 / 52**. Thirteen per band on lessons 01–02, fourteen on
lesson 03.

| lesson | ids added (each band) |
|---|---|
| 01 charging by rubbing | e05–e17, s05–s17, h05–h17 |
| 02 forces between charges | e05–e17, s05–s17, h05–h17 |
| 03 electric fields | e05–e18, s05–s18, h05–h18 |

Two ideas carry the unit and are attacked from every side. The first is that
**rubbing separates charge and never makes it**: a row that asks where the
charge came from (`h05`), one that rebuts the claim with a measurement of the
duster (`h09`), one that shows both objects cannot be negative (`h11`), and one
that names what is unchanged (`h12`). The second is that **attraction proves
nothing and repulsion proves everything** — `p9-02-e06`, `e14`, `e17`, `s07`,
`s13`, `s17`, `h07`, `h09` and `h16` each approach it from a different
direction, because it is the discrimination a student most often loses.

Lesson 03's rows keep the field as a property of the space rather than of what
is in it: the test charge is trebled and the field does not move (`s05`), the
air is pumped out and nothing changes (`s13`, `h08`), and a null point is no
field rather than a weak one (`h07`).

**Review fixes.** Three duplicate stems caught by the gate — `p9-03-s06` had
reproduced the existing `s03`, `p9-03-s10` the existing `h02` (the metal lift),
and the replacement written for `s10` then collided with `h04` (the charged
comb and the water). All three were rewritten rather than nudged: the arrows
between an unlike pair, what a doubled arrow length means for the force, and
the comb held above and then below the stream. Twenty-nine length flags fixed.

**A pattern the row-by-row read cannot see, and the fix for it.** Across the
120 new rows the correct answer sat in slot 1 sixty-eight times and in slot 4
twice — a tell worth more to a guessing student than most of the physics. The
lane now has `phys_rebalance.py`, which walks a unit's new rows and swaps two
option blocks wherever the correct answer sits in an over-used slot, moving it
to the least-used one. It touches order only: the same four options, the same
correct one, each `why` still attached to its own option (spot-checked, and the
gate's "exactly one correct" and duplicate-answer-set checks both still pass).
P9 went from 16 / 68 / 34 / 2 to **29 / 31 / 31 / 29**.

---

## P10 · Magnetism — 5 lessons, 96 new rows (32 per band)

Unit total: **52 / 52 / 52**. Seven per band on lessons 01–02, six per band on
03–05.

| lesson | ids added (each band) |
|---|---|
| 01 magnets and poles | e05–e11, s05–s11, h05–h11 |
| 02 magnetic fields | e05–e11, s05–s11, h05–h11 |
| 03 the Earth is a magnet | e05–e10, s05–s10, h05–h10 |
| 04 electromagnets | e05–e10, s05–s10, h05–h10 |
| 05 how a motor works | e05–e10, s05–s10, h05–h10 |

Lesson 01 repeats the P9 discipline in a new setting: **attraction proves
nothing, repulsion proves everything** (`e09`, `s05`, `s09`), and the reason is
given its own row — the magnet magnetises the bar first, so the near end always
comes out opposite (`h07`). Lesson 02 keeps insisting that the LINES are a
drawing and the FIELD is real: there is a field between two drawn lines
(`e08`), crowding is how a map shows strength rather than extra lines the
magnet makes (`h07`), and filings show the shape but never which way round it
runs (`e10`, `h11`).

Lesson 04's rows separate the coil's contribution from the core's, since the
lesson names both confusions: pulling the core out while the current still runs
(`s06`), and the "more wire carries more current" reasoning that reaches the
right answer by the wrong route (`h05`). Lesson 05 turns on the two reversals —
one changes the direction, two put it back (`s05`) — and on what the split ring
is actually for (`e08`, `h06`).

**Review fixes.** Seventeen length flags reworded. The correct answer had again
clustered badly — 12 / 57 / 25 / 2 across the 96 rows — and `phys_rebalance.py`
moved 32 of them to give **23 / 25 / 25 / 23**.

---

## P11 · Matter and the particle model — 4 lessons, 108 new rows (36 per band)

Unit total: **52 / 52 / 52**. Nine per band on every lesson.

| lesson | ids added (each band) |
|---|---|
| 01 density | e05–e13, s05–s13, h05–h13 |
| 02 Brownian motion | e05–e13, s05–s13, h05–h13 |
| 03 temperature and internal energy | e05–e13, s05–s13, h05–h13 |
| 04 why ice floats | e05–e13, s05–s13, h05–h13 |

**P11 is the referencing unit, and the folder was read before authoring.** Its
four lessons carry a `references` list pointing at C1 (`solids-liquids-and-gases`,
`changes-of-state`, `diffusion`) and at P1 (`heating-and-thermal-equilibrium`),
each with a stated reason. The rows here lean on those ideas where a lesson
already does — a gas being far less dense because its particles are far apart
(`p11-01-h09`), energy going into the arrangement rather than the temperature
during a change of state (`p11-03-s08`) — but they **test P11's own content**,
never C1's. No row asks what the states of matter are; the density, the
jiggling, the temperature/internal-energy split and the ice anomaly are what is
examined.

**⚠️ `quantities.py` governs lesson 03 and was honoured.** That module owns the
one definition of temperature, and P11 lesson 03 is one of its four sites. No
new row restates it. The nine easier rows go at what the lesson adds instead —
which quantity is in joules and which in degrees, what internal energy also
depends on, when heating stops, and what absolute zero is — and the harder ones
work the distinction rather than the definition (`h07`, `h12`, `h13`).

Lesson 02's rows keep the three named misconceptions in view: the specks are
not alive (`e08`), they are not the molecules (`s12`), and a draught or a
convection current is ruled out by neighbouring specks going different ways at
the same moment (`s07`, `h11`).

**Review fixes.** Fifteen length flags reworded, most of them one-word correct
answers ("No", "Sinks", "It splits") given a short reason so they no longer
stood out among wordy distractors. The spread was 9 / 73 / 23 / 3 and 43 rows
were rotated to give **26 / 30 / 26 / 26**.

---

## P12 · Space — 6 lessons, 84 new rows (28 per band)

Unit total: **52 / 52 / 52**. Five per band on lessons 01–04, four per band on
05–06.

| lesson | ids added (each band) |
|---|---|
| 01 gravity and weight | e05–e09, s05–s09, h05–h09 |
| 02 mass vs weight | e05–e09, s05–s09, h05–h09 |
| 03 gravity: Earth, Moon and Sun | e05–e09, s05–s09, h05–h09 |
| 04 the Sun, stars and galaxies | e05–e09, s05–s09, h05–h09 |
| 05 seasons and the tilt | e05–e08, s05–s08, h05–h08 |
| 06 how far is a light year | e05–e08, s05–s08, h05–h08 |

Every `W = m × g` row carries its field strength in the stem, and the two
standing errors — reading a mass in newtons and a weight in kilograms — are
distractors rather than assumptions. Lesson 02 keeps the pair apart from both
sides: what is unchanged on the Moon (`e07`), what is just as hard there
(`s06`, `h07` — lifting gets easier, shaking does not), and why weightless is
not massless (`h05`).

Lesson 03 refuses the two orbit misconceptions by name: there is no outward
force to balance gravity (`e08`, `h07`), and the two pulls in a gravitational
pair are equal however unequal the masses (`s08`, `h09`). Lesson 05 keeps
distance out of the seasons at every band, including the version that is hardest
to shake — that the TILT itself brings a hemisphere nearer (`h08`, where a few
thousand kilometres is set against 150 million).

**Review fixes.** One duplicate stem caught by the gate: `p12-04-s08` had
reproduced the existing `s04` (how many galaxies) and became "what is the
universe" instead. Ten length flags reworded. The spread was 10 / 63 / 11 / 0 —
the correct answer never once in the last slot — and 39 rows were rotated to
give **20 / 24 / 20 / 20**.

---

## ⚠️ A bias no row-by-row read can see: where the correct answer sat

Measured across all twelve units once `phys_rebalance.py` existed, and it is
the finding of this run that a careful reader would never have caught, because
**every individual row was fine**. The defect lived in the aggregate.

| unit | before | after |
|---|---|---|
| P3 | 40 / 36 / 30 / 14 | 31 / 31 / 30 / 28 |
| P1 | 20 / 17 / 16 / 7 | 16 / 16 / 16 / 12 |
| P4 | 16 / 15 / 14 / 3 | 13 / 13 / 13 / 9 |
| P2 | 24 / 32 / 31 / 9 | 24 / 25 / 25 / 22 |
| P8 | 17 / 23 / 28 / 4 | 17 / 19 / 19 / 17 |
| P5 | 26 / 42 / 35 / 5 | 26 / 28 / 28 / 26 |
| P6 | 6 / 20 / 13 / 9 | 11 / 13 / 13 / 11 |
| P7 | 12 / 23 / 24 / 13 | 17 / 19 / 19 / 17 |
| P9 | 16 / 68 / 34 / 2 | 29 / 31 / 31 / 29 |
| P10 | 12 / 57 / 25 / 2 | 23 / 25 / 25 / 23 |
| P11 | 9 / 73 / 23 / 3 | 26 / 30 / 26 / 26 |
| P12 | 10 / 63 / 11 / 0 | 20 / 24 / 20 / 20 |

**The shape of the bias.** Across the first eight units the fourth slot held
about **10%** of the correct answers where it should hold 25%; in P12 it held
**none at all** out of 84. A student who never read a stem and always guessed
the second option would have beaten chance on this bank, on nine units out of
twelve. That is a bigger edge than most of the distractors take away.

**Why it happened.** Writing four options in order, the correct one gets
written first and then distractors are built around it. Nothing in a single
row looks wrong, and reviewing rows one at a time — which is what a cold
examiner read is — cannot surface it. It needs a count.

**The fix.** `phys_rebalance.py` walks a unit's rows at `bank_position >= 12`,
finds the ones whose correct answer sits in an over-used slot, and swaps two
option blocks so it moves to the least-used one. **It is content-neutral**: the
same four options, the same correct one, every `why` still attached to its own
option, and the correct option still carrying no `why`. Only rows this lane
added are eligible, so the twelve rows AUTO composition reads are untouched.
Verified after every run by `question_bank`'s "exactly one correct" and
"positions 0–11 hold four of each band" checks, by the duplicate-answer-set
check, and by reading rotated rows back.

**What to take from it.** The mechanical sweep earned its place here. Length
parity, duplicate stems and markup are all things it caught that a read might
have caught too; the slot distribution is the one that was invisible without
counting, and it was present in every unit written before the count existed.

---

## ⚠️ `git add` was scoped correctly and a commit still swept in another lane

Found by the commander in this lane's **P5 commit `586aaa0c4`**, which carried
fifteen files belonging to the site lane (`teacher/*`,
`mrbadmus_site/teacher/*`, `shared/set-work.js`) alongside the four that were
this lane's. It photographed a temporary revert of those pages, which then had
to be repaired.

**The `git add` was not the fault.** Every commit in this lane ran exactly the
scoped form the brief asks for:

```bash
git add ks3_data/p5/ docs/mrb335/ks3-content-physics.md
git commit -m "…"
```

**`git commit` is what widened it.** `git commit` records the WHOLE INDEX, not
the paths just added — and in a shared worktree the index is shared too. A
co-tenant lane that has run its own `git add` leaves its files staged, and the
next lane to commit takes them along, whatever that lane added itself. Nothing
in the scoped `add` prevents it, and `git status --short` on your own paths does
not show it either: the extra files sit under a heading you were not reading.

**The form that cannot do this**, used for every unit from P6 onwards:

```bash
git commit ks3_data/p6/ docs/mrb335/ks3-content-physics.md -m "…"
```

A commit with pathspecs commits exactly those paths and **ignores the index
entirely**, so a co-tenant's staged work cannot ride along even if it is
staged at that moment. `git status --short` is checked first regardless, and
`git show --stat` after, to confirm the file list is only this lane's.

**Scope of the damage: P5 only.** The other five commits carry exactly their
own unit plus the log — P3 4 files, P1 9, P4 10, P2 6, P8 8 — checked with
`git show --name-only`. The repair to the teacher pages was the commander's;
this lane has not touched those files.

---

## ⚠️ A gate defect that is NOT content, found while topping up P1

From the moment the biology lane's B1 top-up landed in this worktree,
`python3 verify_questions.py` reports **two check-8 findings**:

```
[check 8] compose_assignment/nearest-first
[check 8] compose_assignment/thin-week
```

**`compose_assignment` is not the problem — it is correct.** It draws through
`auto_pool()`, so it still takes exactly four standard rows from a lesson that
now holds eight, and RISKS D7 holds: a topped-up lesson composes the identical
assignment it composed before. Measured, read-only:

```
B1 lesson 6 standard rows in the file : 8
B1 lesson 6 standard rows auto can see: 4
cap obeyed by compose_assignment      : True
```

**The check's EXPECTATION is what is uncapped.** In
`verify_questions.py::_check_composition`, the two comparisons build their
expected lists from the whole lesson:

```python
own     = [q["id"] for q in bank.get(keys[5], []) if q.get("band") == "standard"]
nearest = [q["id"] for q in bank.get(keys[4], []) if q.get("band") == "standard"]
```

so they expect eight ids where composition can only ever reach four. Re-running
the same two assertions with `qb.auto_pool(...)` wrapped round each expectation
makes both pass:

```
thin-week     (capped expectation): True
nearest-first (capped expectation): True
```

**Why it matters to every lane, not just biology.** B1 is check 8's fixture
unit. The check therefore goes red on the FIRST unit any lane tops up in B1 and
stays red for everyone in the worktree afterwards — including runs whose own
content is perfectly clean. It is the gate measuring the pre-MRB-335 world.

**The fix is two lines**, wrapping each expectation in `qb.auto_pool(...)`. It
is in `verify_questions.py`, which this lane may not edit (scope is
`ks3_data/p*/questions_*.py` plus this file), so it is reported rather than
made. **It must not be "fixed" by relaxing the assertion** — the property it
tests is real and is exactly what protects existing assignments.

**How this lane stayed honest in the meantime.** Every unit from P1 onwards is
gated with a wrapper that fails on any finding that is not that named B1
check-8 pair, so a physics defect cannot hide behind the known red. The fast
gate `python3 -m ks3_data.question_bank` — which runs `validate_lesson` over
every physics lesson, the ids, the positions, the duplicate stems and the
markup rule — stays **OK, unconditionally**, after every unit below.

⊕ **Updated at P8 (still 7 Sep 2026): the red has CLEARED, and that is not a
fix.** `verify_questions.py` now reports all nine checks clean, because the
biology lane's B1 is back at twelve rows a lesson — it has committed B2, B3 and
B7 instead and B1 is not yet topped up. Nothing about `_check_composition`
changed. **The defect returns the moment B1 is topped up**, which the quota
table requires (B1 needs 26 more rows per band), so the two-line fix above is
still owed and should land before or with the biology lane's B1 commit.

The lane's gate wrapper stays in place for the rest of the run: it treats that
one named B1 check-8 pair as known and fails on anything else, so a physics
defect cannot hide behind a red if it comes back.
