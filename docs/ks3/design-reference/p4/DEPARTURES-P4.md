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
| **What is built** | The same five requirements, in the same order and with the same content, in the engine's `safety_note` foot slot — which renders small, at the bottom edge, with `ks3-safety` treatment — recast from five bullets into one sentence with semicolons. |
| **The defect in hers** | **None in the content, and this row exists only because the shape changed.** The engine has no amber-callout block type, and §5.1.1's vocabulary is closed — a new block type "needs an amendment to architecture.md, not a local addition". Inventing one for a single page is the MRB-205 failure in the other direction: rendering something Design did not draw, on one page, with nothing else in the key stage using it. |

⚠️ **THIS IS THE ONE ROW WHERE HER OWN FLAG ASKS FOR A DECISION AND THE
DECISION IS NOT MINE.** Her flag 6: *"This is a deliberate departure from the
describe-don't-instruct rule and a reviewer should either ratify it or move
the block into teacher-facing material."* Nothing here ratifies or moves it —
the block stays on the student page, in full, exactly as she asked. **What
changed is only which slot it renders in, and that is Mide's to overrule.**
If the amber callout is wanted, it is a new §5.1.1 block type and a
`architecture.md` amendment, not a P4 edit.

### 2. Three rung-2 distractors are rewritten as full wrong rules

| | |
|---|---|
| **Lessons** | `p4-06 air-and-water-resistance`, `p4-07 moments`, `p4-09 non-contact-forces` — the *apply* rung on each |
| **What she wrote** | Each correct answer states a full RULE (subject, condition, consequence) and each distractor states one short wrong clause. `p4-06`: correct 28 words against a longest distractor of 15. `p4-07`: 21 against 13. `p4-09`: 22 against 12. |
| **What is built** | Her correct answers are untouched **to the character**. Six distractors — two per rung — are rewritten as full wrong rules of comparable length, with the misconception as the consequence rather than as a bare clause. |
| **The defect in hers** | **A student can score all three rungs without reading them, by choosing the longest option.** That is not a stylistic judgement: it is measured, and MRB-177's gate names it — *"the correct answer is a length tell — a student can score these without reading them"*. It is also the defect the ruling of 17 Aug 2026 already fixed across twenty other rungs. |

⚠️ **THE FIX IS AT THE DISTRACTOR, AND THAT IS THE ENGINE'S OWN RULING, NOT A
CHOICE MADE HERE.** `verify_ks3.py` states it in terms: *"The ruling fixes the
CONSTRUCT rather than the threshold: distractors on a rule-stating rung now
state WRONG RULES — the same three-part shape, with the misconception as the
consequence"*, and *"no correct answer was shortened"*. None was here either.
The rewritten distractors carry the same wrong ideas her originals carried,
and each keeps its own correction verbatim.

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
