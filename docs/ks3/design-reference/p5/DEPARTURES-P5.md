# DEPARTURES — P5 *Pressure*

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

## Changed — 1 row

### 1. Ten distractors are finished into full wrong rules

⊖ **COUNT CORRECTED 25 Aug 2026.** This row used to say *"one distractor per
rung"* across four rungs. The measured figure, taken against Design's own
`HOOK` and `RUNGS` constants rather than against the row, is **ten**: eight
ladder options across all four lessons, and two hook options on `p5-03` and
`p5-04`. Three of the eight had already been extended by the pass that built
the unit, without reaching a row at all.

| | |
|---|---|
| **Lessons** | All four — the *apply* rung on each, and the hook commit on `p5-03` and `p5-04` |
| **What she wrote** | On ten option sets the correct answer is the longest by MRB-177's threshold. `p5-03`'s apply rung ran 31 words against 12; `p5-04`'s ran 24 against 19. |
| **What is built** | Her correct answers are untouched **to the character**, and so is every other option. Ten distractors are finished so that each states a complete wrong rule rather than a clipped one. Each carries the same wrong idea her original carried and keeps its own correction verbatim. |
| **The defect in hers** | **A student can score ten commitments without reading them, by choosing the longest option.** Measured, not judged, and the remedy is the engine's own: fix the construct at the distractor, never shorten a correct answer. |

⚠️ **THE SAME PASS FIXED 22 OF P5's OWN 48 BANK QUESTIONS**, which are this
lane's and not hers.


---

## Considered, not changed — 6 rows

**`p5-01`'s triangle, on a relationship taught as a division.** MRB-204
allows a triangle only where `A = B × C`, and the page teaches
`pressure = force ÷ area`. Considered at length and kept: `force = pressure ×
area` is the same statement rearranged and IS a genuine product, so the
triangle is legal, and it is the one the student will meet at GCSE. The three
other P5 relationships are sums and differences and take a stack and a beam,
which is the discrimination the rule exists to protect.

**`p5-02` reports gauge pressure and calls it "the pressure".** This is the
one place in the unit that could actively mislead — a surface reading of 0 Pa
is not a vacuum. Considered as a candidate for the *imprecise in a way a
student carries into GCSE* ground, and kept, because **her page already
declares it**: the foot line says the probe reads the liquid alone and that
the atmosphere adds about 100 000 Pa everywhere in the tank, and `p5-04` then
picks that seam up as its whole subject. A stated simplification a student can
check is not a misconception.

**`p5-03` teaches floating with no use of the word "density".** Considered
and kept. `PRES.02` is written as displacement — the weight of what you push
out of the way — and that is what makes her ship-and-bolt case work at all; a
density comparison would need a quantity C1 owns and `p11` teaches. The
densities on the bench are declared as model numbers in the foot line and are
never taught as the explanation.

**`p5-04`'s "Nothing sucks: air pushes."** Blunt to the point of being a
slogan, and exactly right. Considered as a candidate for softening, and kept
without hesitation: the whole page exists to break the sucking model, and a
hedged version of that sentence would leave it intact.

**The round teaching figures throughout** — the sand giving way at 6000 Pa,
one litre of water weighing 10 N, `g` taken as 10 N/kg, the standard-
atmosphere heights. Every one is chosen so that a state is reachable rather
than measured from a real bench, and every one is declared in the page's own
foot line. Considered and kept: a declared model figure a student can check
against the stated convention is not a thing a student can be misled by.

**`ρ g h` is never named.** Her `p5-02` teaches the depth relationship as
force over area again, with the weight of the column as the force, rather
than as `pressure = ρ g h`. Considered and kept — `ρgh` is KS4, and her route
reuses the quantity `p5-01` has just built rather than introducing a second
one.

---

## Not departures, and why

**The four `rest` maps.** Every "Your turn" panel's Question 1 is live on the
bench above it, so its resting text has to be the bench's opening state or a
reader without JavaScript is shown a raw `{token}`. All four shipped with an
empty `rest` map and would have put nine braces on the page; `kit._rest_fill`
refused the build. **This is a hole being filled, not a change to her page** —
the words are hers and the resting numbers are the bench's own.

**`ground` → `base_y`.** Two benches used `ground` for a y-coordinate. It is a
RESERVED payload key — `r_activity` reads `a["ground"]` on every instrument
with no opt-out and admits only band / card / ground / inset — so the build
died with `unknown ground 470`. The key is renamed and the attribute with it.
Invisible to a student; no row.

**Two MRB-254 repairs.** The float tank's "left over" caption was an SVG
`<text>` that shipped empty and was filled by JS, and three of `p5-04`'s five
stack bands drew an empty `<text>` because they are deliberately unlabelled.
The first is now an overlay span at the same place in the viewBox — the
remedy Design applied to her own ten bench captions — and the second draws no
element at all when there is no label. Engine, no row.

**One internal slug removed from student prose.** `p5-04`'s stretch text
referred to *"`p5-02`'s manometer"*. That sentence was not Design's; it came
from the pass that replaced her *Going further* section, and `ks3_smoke
--static` caught it. Both the slug and the replacement are gone — see the
reverts below.

**The "Your turn" half of `Cfifa`.** Design's shared component has two halves
and only the worked-example half had ever been ported. The second half — the
student's own five lines, two questions, self-marked — is an **addition**
that restores a component she drew, not a departure from it.

---

## ⊖ Phase 3 reverts

Phase 3 compared every built page against her drawing element for element.
**Each item below is a REVERT, not a departure**: her version is restored,
because in each case no defect could be named in it.

| # | Lesson | What had been done | Now |
|---|---|---|---|
| R1 | `p5-02` | The key fact was paraphrased. The paraphrase even added something true — *"and on the liquid"* — but "mine is clearer" is not a ground | Hers, verbatim |
| R2 | `p5-04` | All three *Going further* items were replaced: her weather-map paragraph, her Torricelli-and-millimetres-of-mercury paragraph and her cabins-summits-and-kitchens paragraph, swapped for two of the replacement's own | Hers, all three, verbatim |
| R3 | `p5-04` | The key note was rewritten: it added a true sentence about where the atmosphere's mass sits and dropped hers about what suction actually is | Hers, verbatim |
| R4 | `p5-04` | The convention note changed a claim — *"rounded to the nearest kilopascal"* became *"each within a kilopascal of the international standard"* — and dropped her sentence explaining what the *air left above you* readout is | Hers, verbatim |
| R5 | `p5-04` | The *At GCSE this becomes* line was rewritten to name the gas laws instead of why the decrease with height is not a straight line | Hers, verbatim |

⚠️ **ALL FIVE ARE ON `p5-04`, AND FOUR OF THEM ARE END MATTER.** Key note,
convention note, GCSE line, *Going further*: the four things nobody rereads,
on the last page of the unit. That is worth naming as a pattern rather than
as five incidents — end matter is where an unchecked rewrite survives longest,
because it is furthest from anything a gate measures.

---

## What the register does not cover, and did not catch

**A cross-unit defect found while checking P5, affecting five units.**
`r_key_fact` resolves its text through `ref`, naming an entry in
`key_facts[]`. A core block written `{"type": "key-fact", "id": ...}` sets no
`ref`, so the renderer emitted the label with an **empty body** — the cream
band, the ink outline, the orange shadow, the words *Key fact*, and then
nothing. **24 pages shipped without the one line §4.8.1 B says must survive
the lesson**: P1 (1), P2 (7), P3 (3), P4 (9), P5 (4).

Nothing caught it. The build was green, `verify_ks3` was green, and the
23 Aug audit's own note that *"any gate counting `[data-key-fact]` now passes
on all seventy"* was true and measured the WRAPPER. Counting a block is not
reading it.

All 24 are fixed, all 13 P4/P5 key facts now match Design's word for word,
and `verify_ks3` has gained a check that sweeps the served tree for an empty
key-fact body. It was proved by reintroducing the defect on one page and
confirming the sweep reports it.

---

## ⊖ Phase 3, second pass — 25 Aug 2026, after P5 had shipped

The first Phase 3 pass compared the built pages against her **HTML**. That is
not enough: a `.dc.html` renders its hook, its bench gate, its ladder, its
branch notes and its attempt panel from `{{ }}` holes, so everything a page
computes is invisible to an HTML comparison and reports as a match. Reading
her **JavaScript** found five more.

| # | Where | What had been done | Now |
|---|---|---|---|
| R6 | `p5-02`, `p5-03`, `p5-04` | **Three hook commits were invented.** Her prompt had been ported on each and her four answers had not — eleven options in all | Hers, ported, permuted for position |
| R7 | `p5-03`, `p5-04` | Both attempt Question 2s were **different questions with different numbers** — hers are a 0.60 kg sinker reading 4.5 N, and a 1.5 m² windscreen at 98 kPa | Hers, ported |
| R8 | `p5-04` | One step note was paraphrased, losing the word *pushing* — the word this page spends its whole length on | Hers, verbatim |
| R9 | `p5-01` | **The sand bench's three branch notes never reached the page.** `r_block_on_sand` read no `branches` key at all, so its note panel was empty in every state — the same defect as `p6-08`'s log-range, in a unit that had already shipped | Emitted, and the drawer now refuses a payload missing a branch |
| R10 | four hooks, eight rungs | Length tells — see the corrected row 1 above | Distractors finished |

⚠️ **R9 IS THE ONE A STUDENT WOULD HAVE NOTICED.** `p5-01` is the unit's
first lesson and its bench is the drawing pin made quantitative; the panel
under it that explains what just happened was blank on every setting. It was
found by asking the built bytes rather than the payload, and every other P4,
P5 and P6 bench was then checked the same way — one defect in twenty-two.

⚠️ **P4 WAS CHECKED THE SAME WAY AND ITS LADDERS, HOOKS AND GATES ARE ALL
HERS.** Only the length-tell extensions differ, which row 2 of its own
register now counts correctly.

---

## ⊕ Fixed 25 Aug 2026 (MRB-223) — the duplicated head row, on live pages

Every bench, band figure and attempt panel in this unit printed its head row
TWICE on the live page: `r_activity`'s `.ks3-blockhead` drew Design's row
(eyebrow, `<h2>`, progress readout) from the activity's `eyebrow` / `heading`
/ `progress`, and the unit's own `_head()` helper drew it again inside the
instrument — first found on P9's first bench screenshot and recorded in
`DEPARTURES-P9.md`. No gate saw it: two correct head rows are two correct
head rows.

**Fix, in this unit's own module and its own wiring block only:** `_head()`
returns nothing; the band figures (`fband` / `wanat` / `wband`) no longer
print their eyebrow and heading a second time; the CFIFA attempt passes
`eyebrow=None` to the kit helper (P7's opt-out); and each bench's wiring now
writes its readout into the shell's own `[data-count]`, so the words a
student reads are unchanged — "Both controls live", "0 of 5 cases opened" —
they are simply printed once. Nothing in any lesson record moved.

**Measured on the built bytes, page by page (all 22 P4/P5/P6 lesson pages):**
duplicated `<h2>` — one per page before, ZERO after; the second
`.ks3-<hook>-head` row — present on every bench before, absent after (the
only `-head` classes left are SVG arrowheads). The one eyebrow still printed
twice on the twelve formula pages is Design's own: her two worked examples
both carry *"Worked example · one step at a time"*.
