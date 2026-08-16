# C2 — Atoms, elements and compounds · author's notes

**All six lessons. The unit is complete.** Everything is draft and unreviewed.
(An earlier drop of this folder carried four lessons and a plan for the last
two; §6 now describes what was actually built.)

Queue resolution and filename convention: `NOTES-P3.md` §0, unchanged. C2 is
the second Year-7 Chemistry unit by declaration order in `structure.py`.

---

## 1. Statutory coverage — and the gap

| Lesson | Statements |
|---|---|
| `the-atom-daltons-model` | `KS3.C.AEC.01` |
| `elements` | `KS3.C.AEC.02` (the element half) |
| `compounds` | `KS3.C.AEC.02` (the compound and mixture half) |
| `chemical-symbols` | `KS3.C.AEC.03` (the symbols half) |
| `formulae` | `KS3.C.AEC.03` (the formulae half) |
| `conservation-of-mass` | `KS3.C.AEC.04` |

**All four AEC statements are covered, none twice.** AEC.03 is deliberately
split across two lessons: symbols are a notation to be read, formulae are a
model of what is in a particle, and teaching them in one sitting is what makes
students think a formula is just a longer symbol.

---

## 2. What the four lessons do

- **`c2-01` (MODEL)** — Dalton's three claims are toggles. Switch one off and
  the observations it was holding up stop being explained: the failure of
  alchemy, fixed proportions in water, conservation of mass, and the fact that
  copper and oxygen make two compounds and nothing in between. The lesson ends
  with the model being *wrong* about two claims and still being the right tool,
  which is the `PART-12`/`PART-13` nature-of-science pair doing real work
  rather than being restated.
- **`c2-02` (CLASSIFY)** — six unlabelled samples, four tests, and only eight
  tests to spend across all six. The budget is the teaching: it forces the
  student to notice that *looks like a metal*, *conducts* and *is shiny* are
  the three most interesting results they can buy and all three are worthless.
  Brass is on the bench precisely because it is the most convincing-looking
  sample and is not an element.
- **`c2-03` (CONTRAST)** — iron and sulfur, before and after heating, with a
  particle diagram that changes from two scattered kinds to a one-to-one
  lattice. Four tests, and the pattern the family demands holds: the vivid
  test (the glow, the colour change) settles nothing, and the quiet one —
  weigh what actually combines — settles everything.
- **`c2-04` (CLASSIFY)** — where each symbol comes from, then reading formulae
  by counting capitals. `CO` and `Co` sit next to each other on purpose.

---

## 3. New instruments

### 3.1 `claim-switch` — flagship of `c2-01` (DOM only)

Three claim toggles and four observations; each observation lists which claims
it depends on, and reads *no longer explained* — with its text replaced by the
reason it fails — when any of them is off.

- **Payload:** `{claims: [{id, text}], observations: [{id, text, needs: [claimId], fail}], off: {}}`.
- **Why it is worth having as a kind:** every INVESTIGATION and MODEL lesson in
  the map needs "what does this claim actually buy?" — `C1 testing-the-model`,
  `C8 mendeleev`, `B10 how-we-worked-out-dna` and `B11 natural-selection` all
  want exactly this instrument with different data.

### 3.2 `test-budget-bench` — flagship of `c2-02` (DOM only)

Samples, a fixed list of tests, and **a global budget of test runs**. Each test
costs one; a verdict per sample is required.

- **Payload:** `{budget: int, samples: [{id, look, results: {testId: string}, verdict, why}], tests: [{id, label}], ran: {}, used: int, verdicts: {}}`.
- **The budget is the pedagogy, not a game mechanic.** With unlimited tests the
  student runs everything and learns nothing about which evidence discriminates.
  If Code drops the budget the lesson quietly becomes a click-through.

### 3.3 `mixture-compound-dish` — flagship of `c2-03`

Two states (stirred / heated), a proportion control that is **disabled once
heated** — which is itself the lesson — four tests, and a particle diagram that
redraws for each state.

- **Payload:** `{heated: bool, ratio: 0|1|2, test: id, tests: [{id, name, before, after, settles, verdict}]}`.
- **aria-label:** *"A particle diagram of iron sulfide: every iron particle is
  joined to one sulfur particle, in a regular repeating arrangement."*

`c2-04` needs no instrument: it is two commit-and-reveal grids.

---

## 4. Science flags — numbered for review

1. **Dalton's three claims, as worded.** I have used: atoms of one element are
   identical and differ from other elements'; atoms cannot be split, created or
   destroyed; atoms combine in simple whole-number ratios. Dalton's own list is
   longer and includes "all matter is made of atoms". Confirm three is the
   right number for KS3 and that these are the three.
2. **"About a hundred kinds of atom."** The table has 118 entries; roughly 94
   occur naturally. The pages say "about a hundred" and the stretch layer in
   `c2-02` says fewer than thirty are known to be needed by living things.
   Confirm all three numbers.
3. **"A phone contains about sixty of them"** (`c2-02` hook). Commonly quoted
   as around 60–70 elements in a smartphone. Confirm, or give me a figure you
   are happy to defend.
4. **The alchemy hook.** "Fifteen hundred years" and "not one of them ever
   produced a single grain of gold" — an argument from a long, well-documented
   failure. It is also the one place a student could ask about nuclear
   transmutation, which *does* turn lead into gold and is not chemistry. The
   page says "nothing you can do in a flask", and the stretch layer draws the
   boundary explicitly. Confirm that is enough of a hedge.
5. **Sodium's entry in `c2-02`.** The test result says reacting violently with
   water builds a compound rather than taking sodium apart. Sodium hydroxide
   and hydrogen are produced. The wording avoids naming them; confirm you are
   happy not to name products in a lesson about elements.
6. **Water electrolysis in `c2-02`** — "two different gases, in a fixed ratio
   of two to one by volume". Correct for hydrogen and oxygen by volume.
   Confirm the "by volume" qualifier is wanted at KS3 or should be dropped.
7. **Iron sulfide, 7 g to 4 g** (`c2-03`). Fe:S is 56:32, which is 7:4 exactly.
   The reaction is exothermic and self-sustaining once started. Confirm the
   ratio is the one you want quoted, and confirm the safety line at the bottom
   of the page (fume cupboard, hydrogen sulfide, teacher demonstration).
8. **"Every iron atom joined to one sulfur atom"** and the drawn lattice.
   Iron(II) sulfide is a 1:1 giant structure, so the diagram is a fair KS3
   picture. It is not molecules. Confirm the drawing does not imply molecules
   more strongly than you would like — this is the single visual in the unit I
   would most want an examiner's eye on.
9. **Steel as a mixture** (`c2-03` sort item 3). Steel is an alloy, and alloys
   are mixtures at KS3. Confirm "mixture" is the answer you want, given that
   carbon in steel is not simply stirred in.
10. **The hydrogen/oxygen stretch** (`c2-03`) — a 2:1 mixture detonates, and
    water puts fires out. Both true. The phrase "same ratio by atoms" is doing
    careful work: confirm it reads correctly to you.
11. **Symbol origins in `c2-04`.** Mg is given as "first and third letter, not
    the first two" and Cl as "not Ch". The real history is looser than any rule
    I could state, and the page says so ("the rule is looser than it looks").
    Confirm you are happy with a rule that admits its own exceptions, rather
    than a clean rule that is false.
12. **Berzelius, 1813** (`c2-04` stretch). Confirm the date and the attribution.
13. **`CaCO₃` uses a subscript character (₃).** It renders in the shipped
    fonts, unlike the arrow and tick characters. If the generator's font subset
    differs, this needs checking — it is the one place in four units where a
    non-ASCII character carries meaning rather than decoration.

---

## 5. Misconception register — proposed `ATOM` family

`PART` is particles and states, opened by C1. These are about atoms having
kinds and about substances versus their ingredients. Same request as before:
**rule on the family before the IDs are referenced.**

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `ATOM-01` | An atom of a substance has the properties of the substance — a copper atom is orange and conducts. | `think-commit-copper` | `think-reveal-copper` | `the-atom-daltons-model` |
| `ATOM-02` | A model that turns out to be wrong about something has been disproved and should be discarded. | `ladder-r2` | `stretch-boundary` | `the-atom-daltons-model` |
| `ATOM-03` | If it looks like a metal, it is an element. | `think-commit-brass` | `think-reveal-brass` | `elements` |
| `ATOM-04` | An element is a pure substance, so anything pure is an element. | `sample-water` | `sample-reveal` | `elements` |
| `ATOM-05` | Reacting violently means being broken down. | `sample-sodium` | `sample-reveal` | `elements` |
| `ATOM-06` | A compound is a very thoroughly mixed mixture. | `bench-gate-proportions` | `weigh-what-combines` | `compounds` |
| `ATOM-07` | The elements are still in there behaving as themselves, so the compound keeps their properties. | `think-commit-magnet` | `think-reveal-magnet` | `compounds` |
| `ATOM-08` | A symbol is the English name shortened, so any sensible abbreviation will do. | `think-commit-co` | `think-reveal-co` | `chemical-symbols` |

`ATOM-01` is the big one and it resurfaces everywhere: C4 (`reactions-rearrange-atoms`),
C8 (`metals-and-non-metals`), P11 (`density`) and every bonding lesson at KS4.
`ATOM-02` belongs with `PART-12`/`PART-13`, and is the third piece of evidence
that a `NOS` family is wanted — the register's own ruling says the call should
be made before `C8 mendeleev` is authored, and this lesson has now made the
same shape of argument a second time.

---

## 6. The plan I wrote for the last two lessons — **superseded by §8**

Kept because the reasoning is still the argument for what got built, and
because two of the calls in it were changed during authoring. §8 is what is
actually in the folder.

### `c2-05 formulae` (MODEL)

- **Phenomenon:** two bottles labelled H₂O and H₂O₂. One is drinking water, one
  bleaches hair and can be used as rocket fuel. One atom of difference.
- **Flagship:** a **formula builder** — pick elements and counts, and the
  instrument names the substance and shows the particle picture; the student
  discovers that changing a subscript makes a different substance, not more of
  the same one. Payload `{parts: [{symbol, count}]}`.
- **The four-part treatment does not apply** (no calculation), but the MODEL
  family's "find where it breaks" step does: giant structures. NaCl is not a
  molecule of one sodium and one chlorine; the formula is a *ratio*. That is
  the limit of the model and it is worth an honest paragraph.
- **Misconception:** `ATOM-09` (reserved) — "the small number multiplies
  everything after it" / "H₂O means two waters".
- **KEY FACT candidate:** *A formula says which elements and how many of each,
  in the smallest whole-number ratio. Change a number and you have changed the
  substance.*

### `c2-06 conservation-of-mass` (QUANTITATIVE)

- Follows the QUANTITATIVE pattern in `NOTES-P3.md` §1 without modification.
- **Phenomenon:** a candle burns away to nothing and a rusting nail gets
  heavier. Both look like mass appearing and disappearing, and neither does.
- **Flagship:** a **balance bench** — a reaction on a top-pan balance, with a
  choice of open flask or sealed flask, and reactions that release a gas
  (marble + acid) or take one in (burning magnesium). The balance reports
  masses and refuses to say what happened to them. Predict-first gate:
  "sealed or open, what will the balance do?"
- **The formula:** total mass before = total mass after; triangle treatment
  applies to the mass sums rather than to a division, which is the first place
  the four-part ruling will need interpreting — flag it when it is authored.
- **Misconceptions:** `PART-05` returns here in its chemical costume ("the
  mass went down when it burned"), which the register already predicts, plus
  a new one for gases having mass at all.
- **Ladder rung 4 candidate:** the rusting nail — heavier afterwards, and the
  extra mass came from the air. Weigh the air.

---

## 7. For Code

- Three instruments in §3, all cheap: two are DOM-only and the third has one
  small canvas.
- No animation loops in this unit at all — nothing here moves, and nothing
  needs to. `prefers-reduced-motion` therefore has nothing to degrade.
- Rail stops: five in `c2-01` and `c2-03`, four in `c2-02`, five in `c2-04`.
- `c2-01` links back to `c1-01-particle-model.html`, which exists.
  `c2-04` links forward to `c2-05-formulae.html`, **which does not exist yet** —
  the generator should render that as a coming-soon row rather than a dead
  link, per §11 decision 8. Same for the `Next` link at the end of `c2-04`.
- The `testBudget` prop on `c2-02` is a real teaching dial (4 makes it brutal,
  24 makes it pointless). Default 8.

---

## 8. `c2-05` and `c2-06` as built — and the ruling c2-06 needs

Both are now authored, so the unit is complete and the two coming-soon rows in
§1 are gone. Two things changed from the §6 plan, and one of them is a ruling.

### `c2-05 formulae` (MODEL)

Built as planned. Two elements and a count for each, chosen with real buttons;
the instrument names the substance and draws its particles, or says **"not a
substance"** — which is most of the combinations, and is the first honest thing
a formula builder can teach. Five real substances are reachable: H₂O, H₂O₂, CO,
CO₂ and NaCl.

The MODEL family's *where it breaks* step is NaCl: it is drawn as a repeating
stack rather than a particle, and the follow-up question asks what the formula
is then telling you. The answer — a ratio — is the same answer it was giving
for molecules all along, which is the strongest form this idea can take at KS3.

New instrument kind: **`formula-builder`**.
`{pairs: [{id, a, b}], a: int, b: int, known: {key: {name, note, atoms: [{s,x,y,r}], bonds: [[i,j]], giant: bool}}}`.
Its aria-label names the substance and says whether it is drawn as one particle
or as a repeating stack.

### `c2-06 conservation-of-mass` (QUANTITATIVE)

Two reactions × two vessels on one balance: marble and acid (a gas leaves) and
burning magnesium (a gas joins), each open and sealed. Open goes down, open
goes up, both sealed do nothing. The balance reports two masses and a third
tile that reads *not measured — you work it out*, exactly as the light gates do
in `p3-01`.

New instrument kind: **`balance-bench`**.
`{reaction: id, vessel: 'open'|'sealed', before_g, after_g, gas: 'in'|'out'|'none', ran: {}}`.

**14. ⚠️ THE RULING THIS UNIT NEEDS. The four-part formula ruling assumes a
formula you can draw as a triangle. Conservation of mass is a sum, and a
triangle is the wrong shape for it** — a triangle encodes one quantity as the
product or quotient of two others, and "everything before = everything after"
is neither. Drawing it as one would teach a false relationship to make a rule
fit. What I have done instead:

- the rule still gets **its own block, alone** (part 1);
- it is **drawn, not typed** — as a level balance beam with *before* on one pan
  and *after* on the other (part 2, in spirit: the ruling says *drawn as a
  triangle*, and this is a drawn diagram that is not a triangle);
- the worked example still **reveals one step at a time** (part 3);
- the student still **fills in the same four steps** on the other reaction
  before meeting a full question (part 4).

So three of the four parts are untouched and one is reinterpreted. Please rule:
either the ruling means *drawn, in whatever shape the relationship actually
has*, or triangles are mandatory and I will redraw it — but I would want to
argue against that, and the same question will arrive again at C4
`mass-in-a-reaction`, P1 `simple-machines` and every energy-conservation lesson
in the course.

### Further flags on these two lessons

15. **The five reachable substances in `c2-05`.** H₂O₂ is described as
    bleaching hair, burning skin and having been used as rocket fuel — all true
    of concentrated peroxide, not of the 3% bottle in a bathroom. Confirm the
    wording is not alarming about the household one.
16. **Glucose and ethanoic acid** (`c2-05` stretch): C₆H₁₂O₆ and C₂H₄O₂ both
    reduce to CH₂O. Correct, and it is empirical-formula territory a year early.
    Confirm it stays as stretch prose with nothing assessed on it.
17. **Na₁Cl₁** (`c2-05` rung 4) — the answer expects both "a 1 is never
    written" and "salt is not separate particles". Confirm you are happy with a
    rung that requires two independent corrections.
18. **The masses in `c2-06`.** 2.40 g Mg → 4.00 g MgO is exact for Mg 24 and
    O 16. The marble-and-acid pair (152.00 g → 149.80 g, so 2.20 g of CO₂) is
    plausible bench data, not measured. Confirm both, and confirm 2 d.p. is the
    convention you want on a balance readout.
19. **Phlogiston** (`c2-06` stretch) — the theory, the weighing that broke it,
    and "negative mass". Historically fair but compressed. Confirm, and confirm
    you want a second nature-of-science stretch in the same unit as `c2-01`'s.

### Register additions for these two

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `ATOM-09` | The small number in a formula changes how much of the substance there is. | `builder-gate` | `formula-builder` | `formulae` |
| `ATOM-10` | 2H₂O and H₂O₂ are the same thing written two ways. | `think-commit-big-small` | `think-reveal-big-small` | `formulae` |
| `ATOM-11` | Burning destroys matter — the mass turns into heat and light. | `think-commit-burning` | `sealed-flask-run` | `conservation-of-mass` |

`ATOM-11` **is `PART-05` in a chemical costume**, exactly as the register
predicted when it wrote that "the puddle dried up" becomes "the mass went down
when it burned". It is minted as its own ID because the confrontation is
different — a sealed flask, not a sealed bag — but it should carry a
cross-reference to `PART-05` rather than pretending to be new.

### Code notes for these two

- `c2-05` and `c2-06` both link only to lessons that now exist; the
  coming-soon rows this unit previously needed are gone.
- `c2-06` links sideways to `c1-03-changes-of-state.html`, which is where the
  same rule was met for a physical change. That link is load-bearing: AEC.04's
  wording covers changes of state *and* chemical reactions, and C1 owns the
  first half.
- Neither lesson animates. `c2-06`'s bench redraws on control changes only.


---

## Change log — 15 Aug 2026 (review round 2)

Four changes from Mide's review, applied across every lesson that carries a
formula. Nothing else was touched.

1. **FIFA is now visible as FIFA.** The worked example and the scaffolded
   attempt both show a lettered badge on each step — **F**ormula, **I**nsert,
   **F**ine-tune, **A**nswer — matching the pattern set in `b1-02`. Step 3 was
   called "Work it out" in round one and is now **Fine-tune**, which is the
   step the letter stands for: do the arithmetic, sort the units, rearrange if
   the thing asked for is not the one on the left. The terser round-one copy is
   kept — the badges were added, the prose was not.
2. **Every formula now carries the cover-the-one-you-want panel.** A drawn
   figure with the chosen quantity physically covered, three cover buttons, the
   arrangement that falls out, and one sentence saying why. It is a real
   instrument, not a static picture.
3. **Ramp height is now visible in the light-gate bench** (`p3-01` only): low,
   medium and high each draw a different ramp, with the slope picked out and a
   height bracket up the back. Changing the setting changes the picture, which
   is what a student needs before the times change too.
4. Notes updated; the three unit zips were rebuilt.

### New instrument kind: `cover-triangle`

Shared shape across all three lessons that use it, and the one to build once.

- **Controls:** one button per quantity in the relationship ("Cover s",
  "Cover d", "Cover t").
- **Readouts:** the drawn figure with an opaque plate over the chosen
  quantity (the covered label stays faintly visible underneath, so a student
  can see what they covered); the arrangement that results, in display type;
  one sentence naming the operation and why.
- **Payload:** `{shape: 'triangle'|'bar', cells: [{id, label, slot:
  'top'|'left'|'right'}], covered: id, results: {id: {result, sentence}}}`.
- **aria-label** describes the mechanism: *"A formula triangle. Distance sits
  above a dividing line; speed and time sit below it, multiplied together.
  Covering one letter leaves the way to work it out."*
- **Reduced motion:** nothing animates; the plate simply appears.

### Flag 14 — partly answered by the cover panel, still needs your ruling

Conservation of mass is still a sum, so it still has no triangle. What it now
has is the **same cover interaction on the shape the relationship actually
has**: a part–whole bar — one long bar for *everything before*, split
underneath into *left in the flask* + *the gas* — with the same three cover
buttons. Cover the gas and you are left with before − left in the flask, which
is exactly the calculation an open flask asks for.

So the four-part ruling is now met in substance on all three of its drawn
lessons, with one of them drawn as a bar instead of a triangle. **The ruling I
asked for in flag 14 is unchanged and still needed**: is "drawn as a triangle"
shorthand for *drawn, in whatever shape the relationship has* — in which case
this is compliant and C4, P1 and the energy lessons inherit it — or are
triangles literal, in which case tell me and I will redraw, under protest.
