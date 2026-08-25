# DEPARTURES — P8 *Electric circuits*

Ruled by Mide, 24 Aug 2026 and widened 25 Aug 2026: **Design's page is the
default and it stays unless a change can be defended.** The bar was originally
"name the defect in hers"; it is now "you may make a DELIBERATE, REGISTERED
improvement where you genuinely judge yours teaches better" — *"if code
genuinely think it's clearer his way, let him effect the changes, it's fine."*

That is a licence for a judgement, not a licence to rewrite by default. Her
STRUCTURE is untouched: four rail stops per page from her own `RAIL`, in her
order, with her shorts and labels; no lesson re-planned; no block type
invented. Every row below is one I would defend to an examiner. Everything
else is hers, and the register is short because it should be.

**This one has THREE changed rows and eleven considered-not-changed rows.**

---

## Changed — 3 rows

### 1. Eight distractors are finished into full wrong rules

| | |
|---|---|
| **Where** | Five ladder rungs (`p8-02` r2, `p8-04` r2, `p8-05` r2, `p8-06` r2, `p8-07` r2), one hook commit (`p8-06`) and two bench gates (`p8-06`, `p8-07`) |
| **What she wrote** | On those eight option sets the correct answer is the longest by `audit_content.length_tell`'s threshold — four words clear of the longest distractor, or 1.4× it. Measured, per set, before and after: r2 rungs at 36 vs 24, 26 vs 22, 27 vs 23, 34 vs 17 and 35 vs 19; the `p8-06` hook at 6 vs 4 (a ratio tell on a numeric ladder); the two gates at 19 vs 12 and 23 vs 15. |
| **What is built** | Her correct answers are untouched **to the character**, and so is every other option and every correction. ONE distractor per set is finished so that it states a complete wrong RULE rather than a clipped one — the series-brightness one now says what it thinks brightness depends on, the lamp-resistance one says why a glowing filament could never be measured, the plastic-ruler one names the all-or-nothing model it rests on, the `p8-07` gate one states the even-splitting rule it assumes. Each carries the same wrong idea her original carried. |
| **The rationale** | **A student can score eight commitments without reading them, by choosing the longest option.** Measured, not judged. The remedy is the engine's own MRB-177 ruling — *"distractors on a rule-stating rung now state WRONG RULES … no correct answer was shortened"* — and none was here either. Two of the eight also teach better as a result: `p8-06`'s hook distractor now names a REAL comparison (copper against tap water really is about a million times), which is exactly the near-miss a student reaching for it has in mind, and `p8-07`'s gate distractor restates `CIRC-09` one lesson later, where it is worth meeting again. |

⚠️ **THE SAME PASS FIXED TEN OF THE 84 QUESTIONS IN P8's OWN BANK, and none
of those is a departure from anything.** The bank is authored by this lane,
not by Design, so a length tell in it is this lane's defect. It is recorded
only so the ratio is honest: eight of her sets needed the fix and ten of mine
did.

---

### 2. `p8-06`'s Question 2 ships write-it-out rather than pick-the-line

| | |
|---|---|
| **Where** | `p8-06` `#s-formula`, the second CFIFA attempt |
| **What she wrote** | `{ tab: 'Question 2', mode: 'pick', convOptions: […], formOptions: […], insertOptions: […] }` — three multiple-choice steps and a number-and-unit box, deliberately the lighter form. Her README says so in terms: *"Seven of those eight attempts are write-it-out … `p8-06`'s second question keeps the pick-the-line variant."* |
| **What is built** | The same question, with HER head, HER five model lines, HER five notes and HER closing sentence, in the engine's write-it-out shape: five inputs, a Check button that unlocks on one written line, and a self-marked reveal. |
| **The rationale** | **A capability difference, not a judgement.** `ks3_art.kit.r_cfifa_attempt` has exactly one shape and it is write-it-out; it is shared by P4, P5, P6 and P8, and giving it a second mode is a change to a shared file (`docs/ks3/worktrees.md` §2) for one question in one lesson. The brief anticipated this and asked for exactly this fallback: *"port the pick variant faithfully if the kit supports it; if the kit's attempt is write-it-out only, build Q2 as write-it-out with her lines and REGISTER the difference."* Nothing a student reads changes; what changes is whether they type the line or choose it. ⚑ **If a reviewer wants the lighter form back, it is a `mode` key on the kit and a branch in `wireCfifaAttempt*`, and it would then be worth doing for the whole key stage rather than for this one panel.** |

---

### 3. The filament cross stays legible when the lamp is dark

| | |
|---|---|
| **Where** | Every lamp on `p8-01`, `p8-02` and `p8-07` — the drawn bulbs, in the unlit state |
| **What she drew** | `bulbStyle` fills an unlit lamp `#15110C` and the cross across it is stroked `#221E1B`. Measured: about 1.2:1. The cross is invisible, so a dark lamp reads as a plain circle with a ring round it. Lit, the same cross is dark ink on `#8FB7FF` and perfectly clear. |
| **What is built** | Her treatment exactly when the lamp is LIT. When it is dark the cross takes `--ks3-on-dark-muted`, which is 6.08:1 on the ink ground. Nothing else moves: same stroke width, same geometry, same two paths. |
| **The rationale** | **The cross IS the lamp symbol, and `p8-01` spends a whole figure teaching a student to read it.** A symbol that disappears exactly when the page asks *why is it dark?* is missing at the one moment it has to be there — and the dark state is not incidental on these three pages, it is the answer to the hook on two of them. This is also the only place in the unit where a drawing carries an identity that its own readout does not repeat: the tiles say `dark`, `dim`, `taken out`, and none of them says *lamp*. ⚑ It is a legibility judgement rather than a defect in her physics, which is why it is a row rather than a revert. |

---

## Considered, not changed — 11 rows

**Two part–whole bars three slots apart** (her FLAG 5). `p8-03`'s `I = a + b`
and `p8-04`'s `V = a + b` are the same figure at the same size. She asks a
reviewer to confirm it reads as a designed pairing rather than a copied
component. **Kept, and it IS the pairing**: current splits at a junction, p.d.
splits round a loop, and they are the two rules students most often swap. Each
block states its own relationship from nothing, and `p8-03`'s parts are
337:213 against `p8-04`'s 177:373 — the same shape carrying opposite splits,
which is the comparison.

**The filament lamp is a straight line** (her FLAG 6). Ruled by Mide on 21 Aug
2026: **the linear model STAYS.** The teaching point is that resistance is not
fixed; the true concave I–V curve is GCSE, and correcting it here would move
the results table in the same lesson and both would have to change together —
which is her own reason for flagging rather than fixing. What the ruling adds
is that the page may not claim the rise is EVEN, and `r_component_under_test`
sweeps its payload at build time and refuses one that does. ⊖ **The sweep
removes nothing of hers**: measured before authoring, her delivered `p8-05`
uses none of *steadily*, *evenly*, *in step*, *at a constant rate* or *the same
amount each time* anywhere on the page. Her own legal line already says the
model *"fixes the two ends of that rise and makes no claim about its shape in
between"*. The ruling is enforced against ours.

**`p8-06` prints no current for bare copper** (her FLAG 7). Ruled by Mide on
21 Aug 2026: 6.0 V ÷ 0.05 Ω is 120 A, which is a division result rather than a
reading, because the supply's own internal resistance is what limits the
current there. **Her DELIVERED PAGE had already drawn it that way** — see the
notes-vs-drawing section below — so nothing changed. The resistance readout
keeps its real value, the copper bar still draws on the chart because it is the
reference, and the legal line discloses it. Nothing on the built page says
120 A; checked by sweep.

**`p8-06` carries a `V = I × R` triangle three slots after `p8-05`'s** (her
FLAG 3). She flagged the duplication and asked for a ruling; Mide ruled the
triangle in on 21 Aug 2026 and closed the objection — repetition is a feature
here, because this bench divides 6.0 V by an ammeter reading in five different
unit prefixes. **Her DELIVERED PAGE had already drawn it**, again against her
own notes. Kept exactly as drawn, including the fact that `#s-formula` takes no
rail stop: her `RAIL` for the page is four entries and the formula section is
not among them.

**`p8-07` owns no subject-content clause** (her FLAG 2). Her sentence: *"If a
coverage gate requires every slot to own something, `p8-07` needs either a WS
tag it can count or a split of `CUR.02`."* It takes the WS tag —
`KS3.WS.EXP.03`, planning an enquiry and identifying its variables — which is
what rung 4 asks for and what the lesson teaches. §5.7 exempts WS statements
from the exactly-once rule, so nothing else in the key stage moves. ⚑ Her page
is unchanged; this is a data-model decision, and it is recorded here because a
reviewer asked for one.

**Clause-level ownership has no notation** (her FLAG 1, third repeat). She is
right about the defect and right about the fix, and could not see that the fix
already existed: `ks3_data/substatements.py` has minted `.a`/`.b`/`.c` sub-IDs
per unit since C1, and it is not in the read-only reference set she works from.
`CUR.01` is split three ways and `CUR.02` two, minted lazily under that file's
own rule. No new mechanism.

**The ohm sign is U+03A9** (her FLAG 10). Kept, and measured on the built
pages: 38 occurrences of U+03A9 on `resistance.html` and none of U+2126.
Subscript digits are absent from the shipped subsets, which is why `p8-03` and
`p8-04` label their bar parts `a` and `b` — kept as she drew them.

**`--ks3-data` does not exist in Design's token file** (her FLAG 11, fourth
repeat). Her `design-reference-font-and-token-law.md` grants the token and
scopes it: *"It applies from P10 onward … P8 and P9 use the substitution
recorded in `NOTES-P8-P9.md` §9 and are not being reworked."* Kept. Readings
and live marks on the ink-dark benches take `--ks3-blue-light`, captions take
`--ks3-on-dark-muted`, and the only amber on any P8 page is `p8-07`'s LOOSE
marker, which is a fault state — which is what §8 reserves amber for.

**`p8-01`'s `#s-think` is a rail stop and every other page's is not.** Design's
`DONE('s-think', s)` on `p8-01` alone reads `s.gate !== null`. Kept exactly:
her `RAIL` is the manifest's reference and the built rail matches it stop for
stop. What it cost was a family — see *Not departures* below.

**Every hedge she asks to keep is on the built page.** *"about"* on every
resistance in `p8-06`; *"in practice"* on the verdict tile's `an insulator, in
practice`; *"typical"* on the specimens and on the ratings; *"almost"* on the
voltmeter drawing no current, the ammeter having no resistance and the battery
having none; *"of that lamp, at that moment, at that temperature"* in `p8-05`;
*"roughly where useful conduction gives out"* with *"no sharp line"* on the
chart boundary. Checked string by string against her pages.

**Her aria descriptions of her own SVGs are not carried, and that is the one
category of her text this unit does not have.** See *What remains different*.

---

## Notes vs drawing — two contradictions, both resolved by measuring the drawing

⚠️ **BOTH ARE IN HER FAVOUR, AND BOTH WOULD HAVE COST A REAL BLOCK IF THE
NOTES HAD BEEN BUILT FROM.**

| # | Her NOTES say | Her DRAWING does | Built |
|---|---|---|---|
| N1 | §3's table lists `p8-06` as **no block**, and FLAG 3 asks for a ruling on whether a page that computes must carry one | `p8-06-conductors-and-insulators.dc.html` carries `#s-formula` — the `V = I × R` triangle, both worked examples and both attempts, 190 lines of it | The drawing. Mide's ruling of 21 Aug agrees with it independently. |
| N2 | FLAG 7 says the copper state **prints 120 A** and asks whether a reviewer would prefer it removed | The page prints no current at all: `iSupplyLimited` renders *"limited by the supply, not by the wire"*, `iSub` says *"a bare wire across a supply is a short circuit"*, the mark on the drawing reads `SUPPLY-LIMITED`, and the legal line discloses the whole thing | The drawing. Mide's ruling of 21 Aug agrees with it independently. |

The notes are dated 21 August and the audit beside them 23 August; the delivery
was repackaged in between. **The notes are older than the pages, and where they
disagree the pages are what she last decided.**

---

## What remains different, and why

Seven strings of hers are still not on our pages, and all seven are **aria
descriptions of drawings**: *"A single loop with 1 cell, a switch drawn
closed…"*, *"A chart of resistance for seven specimens on a logarithmic
axis…"*. Hers describe HER SVG elements; ours describe ours, which are this
engine's drawers rather than her elements. The bench SVGs are transcribed
from her viewBoxes and her path data, so most of what each sentence describes
IS there — but each one names live figures her runtime computed and ours
computes separately, and a description that quotes a number the drawing does
not show is worse than one that quotes the number it does. An accessible
description that describes a different picture is worse
than one that describes this one, so ours stay. That is the only category of
her text this unit does not carry.

⚑ Where the two drawings ARE the same, her sentence is used verbatim: the
symbol key's eight `aria-label`s, the bar models' and the triangles'
descriptions and the decade chart's are hers to the character.

---

## Not departures, and why

Everything below is this lane's own work or the engine's. None is a change to
what Design drew, and none takes a row.

**The marked rungs' OPTION ORDER moved.** Measured before a line was written:
every one of her fourteen marked rungs in P8 has its correct answer at index 0
— the exact defect MRB-278 exists for, and the shape that made every Chemistry
ladder scorable by pressing button one. The commander ruled it engine policy
rather than a register row, and the built unit runs 4/3/4/3 across the four
indices. **Every option's text is hers to the character and so is every
correction; only the order changed, and the `answer` index followed the correct
option.** Each lesson's docstring records the indices it takes.

**The question bank is this lane's, all 84 of it.** Design authors no bank. Ten
of its option sets carried a length tell and were fixed at a distractor;
positions run 21/21/25/17 across the unit, worst index 30%.

**Vocabulary lists are authored here.** §5.4 requires every lesson to name and
define the words it introduces, and `verify_ks3` gates it key-stage-wide with
no exemptions. Design's pages carry no vocabulary block, so all four lists per
lesson are this lane's.

**`circ-think` exists because of a gate, not because of a judgement.**
`p8-01`'s `#s-think` is on her rail, `ks3_parity.check_rail_reachable` reads
the SHIPPED BYTES for one of five completion signals, and neither
`confrontation` (`ks3_art/core.py`, a shared file this lane may not edit) nor
`predict` emits `data-stage-done`. The family puts her two quotes into the same
`ks3-misconception` shell with the attribute, renders the identical three
classes `r_confrontation` renders, and adds nothing a student sees.

**The safeguarding block loses its eyebrow and keeps its words.** §8.10 rules
the TREATMENT — one quiet foot line above the legal line, never a callout —
and her *"If something at home worries you"* eyebrow is the callout's heading.
Her sentence is carried character for character into `safeguarding_note`. Same
ruling as P6's R7.

**Her `ks3-review-flag` and `showDraft` are not ported.** Engine policy; swept
by concept as well as by string, and the built pages carry no *draft*,
*review*, *not yet checked* or *provisional*.

**Three figure sections take no anchor**, because her own sections carry no
`id`: `p8-01`'s symbol key, `p8-04`'s ratings table and `p8-05`'s results
table. Her `RAIL` on each page is four entries and none of the three is among
them.

**The Check button accepted an EMPTY attempt, on all four CFIFA pages.** The
kit's contract is that Check refuses one — *"a student who taps it first has
been handed the answer before writing anything, which is the whole thing this
half of the block exists to prevent"*. `p8-06` is the first panel in the key
stage that can be BLOCKED and then come back (the copper specimen has no
current to divide), and the first cut re-enabled the button on unblocking with
a bare `removeAttribute("disabled")`. Every bench publishes to the panel on its
FIRST paint, so that line ran on load and left the button live with nothing
typed — on `p8-03`, `p8-04` and `p8-05` too, none of which has a blocked state
at all. The state is now RECOMPUTED from the boxes rather than asserted.
⚠️ **Nothing at rest looked wrong**: the panel renders identically either way,
and the only way to see it is to press the button before typing. Found by
driving that exact order.

**The decade chart's scale was wrong, and her drawing is what caught it.**
`p8-06`'s chart computes every bar from logarithms, and the first cut anchored
the scale on `axis_max: 1e14` because her own aria description says the axis
runs *"to a hundred teraohms"*. It does — the RULE does. The SCALE is fixed by
her ticks, 0.01 Ω at x=180 and 1 TΩ at x=863, which is fourteen decades and
not sixteen, and the plastic ruler's bar legitimately overshoots the last
tick. Measured against her SVG: the wrong anchor gave bars of 30 / 87 / 148 /
196 / 282 / 371 / 610 px and a boundary at 479; hers are 34 / 100 / 170 / 224 /
322 / 424 / 697 and 521. The built chart now reproduces every one of them to
within a pixel. ⚠️ **A chart computed from the wrong two anchor points is
internally consistent and looks entirely correct**, which is why it was found
by comparing pixels with her drawing rather than by reading the code.

**P6 SHIPS ITS BENCH TITLES TWICE, AND P8 ALMOST DID.** `r_activity`'s shell
already draws Design's head row from the payload's `eyebrow`, `heading` and
`progress`; an instrument that draws a second one prints the eyebrow and the
`<h2>` one under the other. The first cut of `ks3_art/p8.py` copied P6's
`_head()` and every P8 bench duplicated its own title — caught in a browser,
not by reading. ⚠️ **The same defect is live on P6 today**:
`ks3/physics/waves-and-sound/sound-needs-a-medium.html` carries *"At the bench
· a striker and a microphone…"* twice, forty characters apart, and so do its
other eight benches, its wave-anatomy figure and its six band blocks —
sixteen placements, measured. It is fixed in P8 and left in P6,
which is not this lane's unit. Worth a pass on P6 whenever somebody is next in
it — it is one `_head()` call per renderer and a `progress` map per payload.

**Every hard-coded figure in a bench sentence is now interpolated**, which is
§5A.1 and which her own §5 already claims (*"No figure the instrument computes
is hard-coded in prose"*). Her JavaScript builds those sentences by
concatenation from the same state; ours fills `{token}` holes from the same
state. Identical output, and the reason it is worth saying is that a token that
is never published ships the brace itself — which `ks3_smoke --static` gates.
