# DEPARTURES — P4 *Forces*

Ruled by Mide, 24 Aug 2026: **Design's page is the default and it stays
unless the defect in hers can be named.** Valid grounds are that it is
scientifically incorrect, teaches the famous version over the true one, is
imprecise in a way a student carries into GCSE as a misconception,
contradicts itself or its own instrument, or states something a student
cannot check. *Clearer*, *better phrased*, *better analogy*, *better
ordering* and *different example* are not grounds. Unsure does not clear the
bar; uncertainty resolves toward her page.

The register is expected to be SHORT. A long one means rewriting to taste.

---

## Changed — 2 rows

### 1. `p4-08` — the risk assessment moves from an amber callout to the foot

| | |
|---|---|
| **Lesson** | `p4-08 springs-and-hookes-law` |
| **What she wrote** | An amber callout block above the formula block, headed *"Before this one is done for real"*, with five bulleted lines: eye protection; a tray of sand or padded box under the load; nobody's hands, feet or knees under the hanger; the stand clamped or weighted; loading to destruction as a screened demonstration rather than a class activity. |
| **What is built** | The same five requirements, in the same order, in the engine's `safety_note` foot slot — which renders small, at the bottom edge, with `ks3-safety` treatment. Her five bullets become five sentences in one paragraph, because the slot takes one string. |
| **The defect in hers** | **None in the content. This row exists because the shape changed.** The engine has no amber-callout block type, and §5.1.1's vocabulary is closed — a new block type "needs an amendment to architecture.md, not a local addition". Inventing one for a single page is the MRB-205 failure in the other direction: rendering something Design did not draw, on one page, with nothing else in the key stage using it. |

⊖ **CORRECTED 25 Aug 2026, AND THE CORRECTION IS THE POINT OF THIS FILE.**
This row used to read *"the same five requirements, in the same order and
with the same content"*. **That was not true when it was written.** The
recast had run her five bullets into one sentence with semicolons AND
dropped her opening line — *"This is the one investigation in the unit that
needs a risk assessment, because finding the limit of proportionality means
loading a spring until it stops behaving"* — which is the sentence that says
why any of it is needed. A register row asserting no content changed, on a
row about a **safety** block, from which content had in fact been removed, is
the worst kind of entry this file can carry.

Phase 3 caught it by comparing the built page against her drawing rather
than against the row. Every one of her sentences is now on the page, in her
words; only the bulleting is gone, and only because the slot is one string.

⚠️ **THIS IS THE ONE ROW WHERE HER OWN FLAG ASKS FOR A DECISION AND THE
DECISION IS NOT MINE.** Her flag 6: *"This is a deliberate departure from the
describe-don't-instruct rule and a reviewer should either ratify it or move
the block into teacher-facing material."* Nothing here ratifies or moves it —
the block stays on the student page, in full, exactly as she asked. **What
changed is only which slot it renders in, and that is Mide's to overrule.**
If the amber callout is wanted, it is a new §5.1.1 block type and a
`architecture.md` amendment, not a P4 edit.

### 2. Eight distractors are finished into full wrong rules

⊖ **COUNT CORRECTED 25 Aug 2026.** This row used to read *"Three rung-2
distractors"* and *"Six distractors — two per rung"*, and named three
lessons. The measured figure, taken by comparing every option on every built
page against Design's own `HOOK`, `GATE` and `RUNGS` constants, is **eight**:
five ladder options across `p4-06`, `p4-07` and `p4-09`, and three hook
options on `p4-05`, `p4-06` and `p4-07`. The three hooks were not in the old
row at all, because the pass that wrote it measured the ladder only — and
`verify_ks3`'s MRB-177 sweep reads ladder rungs and activity option sets,
not hooks and not bench gates, so nothing else was going to count them.

| | |
|---|---|
| **Lessons** | `p4-05`, `p4-06`, `p4-07` — the hook commit on each — and `p4-06`, `p4-07`, `p4-09` — the *apply* rung on each |
| **What she wrote** | On eight option sets the correct answer is the longest by MRB-177's threshold: four words clear of the longest distractor, or 1.4× it. `p4-06`'s apply rung ran 28 words against 15; its hook ran 14 against 9. |
| **What is built** | Her correct answers are untouched **to the character**, and so is every other option. Eight distractors are finished so that each states a complete wrong rule rather than a clipped one, with the misconception as the consequence. Each carries the same wrong idea her original carried and keeps its own correction verbatim. |
| **The defect in hers** | **A student can score eight commitments without reading them, by choosing the longest option.** Measured, not judged. The remedy is the engine's own ruling: *"distractors on a rule-stating rung now state WRONG RULES … no correct answer was shortened."* None was here either. |

⚠️ **THE SAME PASS FIXED 38 OF P4's OWN 108 BANK QUESTIONS, and none of
those is a departure from anything** — the bank is authored here, not by
Design. It is recorded so the ratio is honest: eight of her sets needed the
fix and thirty-eight of mine did.


---

## Considered, not changed — 5 rows

**`p4-04` rung 2, "just for an instant"** (her flag 3). She asks whether a
reviewer prefers *momentarily at rest*. Considered and left. The physics is
settled and she says so; the hedge is load-bearing, because without it the
question is ambiguous about whether the ball is being held. Preferring one
phrase to another is not a defect.

**`p4-03`'s sheet of paper and its made-up 2 N breaking point** (her flag 4).
Left exactly as drawn. The number is declared invented in the foot line, and
it exists so that *unbalanced* is reachable on a support that is not simply
absent — without it the only route to a leftover force is removing the
support entirely, which teaches that unbalanced means unsupported. A real
figure would be worse: a sheet of 80 gsm A4 held at two edges has no single
failure force, so putting one on the page would turn a teaching threshold
into a false claim about paper.

**`p4-01`'s "about 200 billion billion N"** (her flag 7). Left in words. The
Bricolage and DM Mono latin subsets shipped in `shared/fonts/` carry no
superscript digits beyond ² and ³, so `2 × 10²⁰` drops to a system font
mid-number inside a mono readout. Her own 23 Aug audit later ruled the
general convention (`10^20` in prose); this page predates the need, reads
better in words, and states a true value either way.

**`p4-06`'s terminal velocities and weights** — 55, 80, 6 and 30 m/s, and
750 N. Every one is hedged with *about* and the foot line declares them
typical rather than measured. They are the commonly published figures and
they are internally consistent with the bench's own `drag = weight × f²`
model. Nothing to name.

**`p4-04`'s gate readings** (her flag 5). 2.2 m/s and 3.6 m/s on the sideways
case are `√(2² + 1²)` and `√(2² + 3²)` for a 1 kg trolley under 1 N —
exact, not rounded, and the page never does the vector arithmetic in front
of the student because resolving into components is GCSE. Checked and left.

---

## Not departures, and why they are not in the table

**Ladder answer POSITION.** All eighteen of Design's P4 rungs put the correct
answer at index 0. The built pages cycle 0–3 for a distribution of
[5, 5, 4, 4]. **Her option texts and her correct answers are untouched**;
only the order the four are listed in changes. That is MRB-278 engine
policy — the same class as the draft-flag sweep — and the brief directs it
to be authored from the start rather than left for the gate.

**The draft flag.** Every one of her pages carries
`<p class="ks3-review-flag">Draft — not yet science-reviewed.</p>`. No student
sees one. Engine policy, no row.

**Misconception ids.** Her §6 reserves `FORCE-01`…`FORCE-36`. Those numbers
were spent by P3 three weeks earlier, and the register's own ruling says *"P4
continues from `FORCE-12`"*. **Every STATEMENT is hers**; only the numbers
moved, and she says in terms that her access was read-only. Recorded in
`docs/ks3/misconception-register.md`, not here.

**The key fact's parent element.** She draws `[data-key-fact]` inside the band
or formula section; the engine's `key-fact` is a top-level block type. It is
emitted immediately after the section it belongs to, so the reading order is
unchanged and only the box's parent differs. Same shape P1–P3 shipped.

**The `#s-formula` rail anchor.** MRB-208: a `formula` block carries no demand
and emits no `data-stage-done`, so the stop goes on the block that can tick —
which is what her own `s.buildOpen` is set by.

**"Your turn · the same five steps" is an ADDITION, not a departure.** Her
`Cfifa` component has two halves and only the worked-example half had ever
been ported, in P1, P2 and P3. The second half — the student's own five
lines, on the numbers their own bench is showing — is now built. Her §3 makes
it load-bearing: *"nothing independent is asked until all three have
happened."*

---

## ⊖ Phase 3 reverts — 25 Aug 2026, added after P4 had already shipped

P4 was committed, gated green and pushed as `d52c317f9` before this pass ran.
Phase 3 then compared every built page against her drawing element for
element, rather than against this register, and found content that had been
replaced or dropped without ever reaching a row. **Every item below is a
REVERT, not a departure**: in each case her version is restored, because in
each case no defect could be named in it.

They are recorded here rather than deleted, because the reason they happened
is worth more than the fact that they are fixed: **each one was written by a
pass that believed it was improving the page, and none of them was checked
against her file afterwards.** The register cannot catch a change nobody
thought was a change.

| # | Lesson | What had been done | Now |
|---|---|---|---|
| R1 | `p4-09 non-contact-forces` | The key note was paraphrased, dropping what each force acts BETWEEN — the half a student needs to answer *"will it attract this?"* | Hers, verbatim |
| R2 | `p4-09 non-contact-forces` | Both *Going further* items were replaced: a history of the field concept, and a compressed version of her own fridge-magnet point. Her second item, on machines that touch nothing — maglev, induction hobs, wireless charging, a disk head — had no counterpart at all | Hers, both, verbatim |
| R3 | `p4-02 drawing-and-adding-forces` | The convention note was widened from *"The bars in the beam are drawn to one scale"* to *"Every arrow on the bench and every bar in the beam"* | Hers, verbatim |
| R4 | `p4-08 springs-and-hookes-law` | The safety note dropped her opening sentence — see the correction to row 1 above | Hers, in full |
| R5 | `p4-02`, `p4-03`, `p4-08` | **The beam figures shipped with no caption and no note.** Design writes one line above each beam saying what it shows, and one below saying why the shape is a beam and not a triangle. Both were dropped on the floor: the drawers took no such keys and `r_formula_figure` emitted only the SVG | Hers, all six sentences, and the renderer now has the slots |

⚠️ **R5 IS THE SERIOUS ONE, AND IT IS AN MRB-204 LOSS.** The sentences that
went missing are the ones that carry the ticket's own argument:

> *"That is why this relationship gets a beam and not a triangle: nothing
> here is being multiplied."* — `p4-02`
>
> *"Nothing here has a formula triangle, and putting one on it would teach a
> relationship that does not exist."* — `p4-03`

MRB-204 exists so that a sum is never drawn as a product. Three pages drew
the sum correctly, as a beam, and then said nothing about why — which leaves
a student with a shape and no reason, and leaves the next author free to
"tidy" it into a triangle. The shape was right and the argument for it was
absent, which is the failure that looks most like success.

**The cause was a missing slot, not a decision.** `r_formula_figure`'s `art`
branch returned the SVG and nothing else, so a `caption` or `note` in the
payload would have been silently discarded even if one had been written. Both
are now emitted, both are optional, and no existing figure moves a byte.

---

## ⊖ Phase 3, second pass — 25 Aug 2026

The first Phase 3 pass compared the built pages against her **HTML**. That is
not enough: a `.dc.html` renders its hook, its bench gate, its ladder and its
attempt panel from `{{ }}` holes, so everything a page computes is invisible
to an HTML comparison and reports as a match. P6 lost nine lessons' worth of
ladders that way.

**P4 was then read against her JavaScript, constant by constant, and it is
clean.** Every hook option, every bench gate option, every rung question,
every rung option, every correction and every success criterion on all nine
pages is hers, and so is every worked example and every attempt question.
The only differences are the eight length-tell extensions counted in row 2.

Two things were checked and found sound rather than fixed:

- **Every P4 bench prints a real note in every state it can reach.** Driven
  headlessly, tab by tab and slider end to slider end. `p4-09`'s force sorter
  is empty until a label is chosen, which is correct — nothing has been
  committed yet.
- **Every P4 branch note authored in a payload reaches the page.** Five
  benches carry them and all five emit; the four that carry none use
  per-item `data-note` instead, which works. `p5-01` was the one bench in
  twenty-two that did not, and it is fixed in P5's own register.
