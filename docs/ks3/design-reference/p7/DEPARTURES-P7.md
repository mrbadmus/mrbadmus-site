# DEPARTURES — P7 *Light*

Ruled by Mide, 24 Aug 2026 and widened 25 Aug 2026: **Design's page is the
default.** A change may be made where it is scientifically incorrect, teaches
the famous version over the true one, is imprecise in a way a student carries
into GCSE, contradicts itself or its own instrument, states something a student
cannot check — or where the lane genuinely judges its own version teaches
better and will defend the row to an examiner. Unsure does not clear the bar;
uncertainty resolves toward her page.

The register is expected to be SHORT. **This one has EIGHT changed rows, and
one of them is a word.** Nothing in her structure moved: four rail stops per
lesson from her own `RAIL`, in her order, with her shorts and labels; her
hooks, gates, branch notes, worked examples, attempt panels and all fourteen
marked rungs are ported from her JavaScript constants, not from her HTML.

⊕ **Rows 5–8 were added 31 Aug 2026 (MRB-297)** and are a different kind of
row from 1–4. They are the KS3 physics audit's findings P7-22, P7-24, P7-23
and P7-19 — two of Design's own bench DRAWINGS, measured from the served path
data and found to be teaching the opposite of what their lessons say. The
first of them draws `LIGHT-23`, a misconception registered on that very page
as the one the instrument exists to kill. Rows 1–4 are judgement; these four
are corrections, and the prism's is now held by a build-time refusal rather
than by anyone's eye.

---

## Changed — 8 rows

### 1. Two rail labels said "four steps" over a five-step block

| | |
|---|---|
| **Where** | `p7-01`'s `s-formula` — *"Triangle and four steps"*; `p7-02`'s `s-beam` — *"The beam and four steps"* |
| **What she wrote** | `four` |
| **What is built** | `five` |
| **The defect in hers** | **The page contradicts its own instrument, twice, on the same screen.** The block those two stops point at is `Cfifa.dc.html`, whose eyebrow reads *"Your turn · the same five steps"*, whose button reads *"All five shown"*, and whose counter reads *"Step n of 5"*. Her own 23 Aug README records the rebuild — *"Worked examples in this unit now run CFIFA: Convert, Formula, Insert, Fine-tune, Answer"* — so the label is a survival from the four-step FIFA the rebuild replaced, and every other page in P4–P6 that took the same rebuild says five. A student reading the rail and then counting the boxes finds the page wrong about itself. |

### 2. Six distractors are finished into full wrong rules

| | |
|---|---|
| **Where** | Four ladder rungs — `p7-01`, `p7-02`, `p7-04` and `p7-05`'s rung 2 — and two hook commits, `p7-04` and `p7-07` |
| **What she wrote** | On those six option sets the correct answer is the longest by `verify_ks3`'s own threshold: four words clear of the longest distractor, or 1.4× it. Measured per set, before and after. `p7-05` rung 2 is the widest — 34 words against 19. |
| **What is built** | Her correct answers are untouched **to the character**, and so is every correction and every other option. ONE distractor per set is finished so that it states a complete wrong rule rather than a clipped one: her *"Paper does not obey the law of reflection"* now says what it does instead of obeying it; her *"Eyes send out rays, but they are too weak"* now says what that would predict about a dark room; her *"The greaseproof paper shows the picture from behind"* now says reversed **both ways at once**. Each carries the same wrong idea her original carried. |
| **The defect in hers** | **A student can score six commitments without reading them, by choosing the longest option.** Measured, not judged. The remedy is the engine's own MRB-177 ruling — distractors on a rule-stating rung state WRONG RULES — and it is always at a distractor: no correct answer was shortened, no answer index was moved to fix a tell, and no correction was edited. |

⚠️ **THE SAME PASS FIXED 31 OF THE 84 QUESTIONS IN P7's OWN BANK, and none of
those is a departure from anything.** The bank is authored here, not by Design,
so a length tell in it is this lane's defect. It is recorded only so the ratio
is honest: six of her sets needed the fix, and thirty-one of mine did.

### 3. `p7-02`'s equality is drawn as the engine's beam, not as her two bars

| | |
|---|---|
| **Where** | `p7-02` `#s-beam`, the `r = i` figure |
| **What she drew** | Two horizontal bars of identical length, labelled `i` (IN) and `r` (OUT), with tie lines and an `=` to the right. Her §10 registers it as `balance-beam`, *"the third member of the beam family alongside `beam-part-whole` and `beam-opposing`"*. |
| **What is built** | `figure: {shape: "balance"}` — the engine's level pan balance, `i` in the left pan and `r` in the right, caption *"always equal"*, and **no cover buttons**, which is the half of her ruling that matters most. |
| **The rationale** | The MRB-223 unit addendum rules this route in terms, and it puts the equality in the one figure the key stage already has for it — `p1-08`'s lever beam and `c2-06`'s conservation beam are the same component, so a student meets one shape for *these two things are equal* rather than a third. The claim is identical and the cover-button ruling is honoured exactly. **The aria description therefore describes OUR drawing** rather than hers: an accessible description of a picture that is not on the page is worse than one of the picture that is (the P6 precedent). |

### 4. `p7-02`'s support line names the drawing that is on the page

| | |
|---|---|
| **Where** | `p7-02` `#s-beam`, the support line under the figure |
| **What she wrote** | *"Two bars of the same length, always. … whatever one bar reads, the other reads too."* |
| **What is built** | *"Two sides that always balance. … whatever one side reads, the other reads too."* The rest of the sentence — *nothing is being added up here and nothing is being shared out, so there is nothing to cover* — is hers, untouched. |
| **The rationale** | Row 3 replaced her two stacked bars with the engine's pan balance, and this sentence is a description of the drawing above it. Left as written it told a student to look for two bars under a picture of two pans — the page contradicting its own figure. It is the same judgement the aria descriptions take: a sentence about a picture describes the picture that is there. Commander's row, added at Phase 3 (25 Aug 2026). |

### 5. `p7-06`'s prism drew the dispersion backwards — MRB-297, P7-22

| | |
|---|---|
| **Where** | `p7-06` `#s-prism`, the fan. Her `lessonVals()`: `inBeam: 'M40 150 L262 210'`, `ys = {R:196, O:208, Y:220, G:234, B:250, V:264}`, each ray drawn to `925, ys[k] + (ys[k] − 210) × 1.9`. |
| **What she drew** | The incident beam tilted DOWN into the prism; extended straight it reaches the screen at y ≈ 389, **below every exit ray**. So every colour was deviated UPWARD, toward the apex, of a prism whose base is the bottom edge — and the amount ran red 219.8 > orange 185.0 > yellow 150.2 > green 109.6 > blue 63.2 > violet 22.6. Measured from the served path data, not read off her source. |
| **What is built** | A horizontal beam at y=160 entering the left face at (261.1, 160); one segment across the glass to (345.5, 171.9) on the right face; six rays landing R 265 · O 276 · Y 284 · G 298 · B 321 · V 358, i.e. deviations of 105 · 116 · 124 · 138 · 161 · **198**, every one of them BELOW the undeviated line. The gaps are in the ratio of the real red→violet spread in crown glass, so they widen toward violet rather than being evenly spaced. |
| **The defect in hers** | **The bench drew the misconception it exists to kill.** `LIGHT-23` — *high-frequency light is bent the least by a prism* — is registered on this very page with `confronted_by: prism`. A prism deviates toward its BASE, and violet most. Hers did neither, and it contradicted its own ladder rung 1 (*"Red, because it has the lowest frequency … and is refracted the least"*) one screen below. It survived every review because the top-to-bottom colour order still reads R,O,Y,G,B,V, which is what a spectrum looks like. |
| **What stops it recurring** | The landings are no longer a runtime constant. `_prism_fan()` in `ks3_art/p7.py` computes every drawn number and REFUSES a fan that is on the apex side, whose deviations do not increase with frequency, whose red is barely deviated, that leaves the frame, or whose exit rays bend toward the normal rather than away from it. The runtime reads the numbers off attributes and joins strings; it computes no geometry at all. |
| **The honest caveat** | The drawing is a schematic and the module says so in terms. A real 60° prism deviates a horizontal ray by about 43° and separates red from violet by well under a degree; drawn to scale on this 1000×420 canvas the fan would leave the frame and the six colours would be one line. The SEPARATION is exaggerated roughly eighteen-fold. The three things a student can be *wrong* about are exact: toward the base, violet furthest, and two bends. |

### 6. `p7-06`'s prism was a box light went into and came out of — MRB-297, P7-24

| | |
|---|---|
| **Where** | `p7-06` `#s-prism`, the path through the glass |
| **What she drew** | The beam stopped at (262, 210), inside the glass; the fan began at (330, 210), also inside it. Sixty-eight units of glass with nothing drawn between them. |
| **What is built** | The beam stops ON the left face, one segment crosses the glass, and the fan starts ON the right face — so the bend at each surface is a bend a student can point at. The segment inside the glass takes the input's colour, as her incident beam does. |
| **The defect in hers** | The lesson's mechanism sentence is *"One bend on the way in, another on the way out"*, and the drawing showed neither: light went in, disappeared, and came out somewhere else already sorted. That is the prism-as-magic-box reading the lesson exists to prevent. |
| **What else moved** | The second prism is now painted BEFORE the rays rather than after. That was harmless while the rays stopped in mid-air at x=640; now that they run through its left face to its far face, a filled triangle painted on top of them would hide the recombination inside the glass. The rays enter the second prism's left face at their own computed points, bend back toward its base — which is uppermost, because it is inverted — and leave as one beam **parallel to the beam that went in**, which is what an inverted identical prism actually does. |

### 7. `p7-06` called blue and red recombined "one white patch" — MRB-297, P7-23

| | |
|---|---|
| **Where** | `p7-06` `#s-prism`, the *On the screen* verdict tile and the `recombined` note, with the second prism in |
| **What she wrote** | `screenWord: two ? (single ? … : 'One white patch — the colours put back together')` — unconditional on which colours went in. The note: *"…they arrive at the screen together as one beam again."* |
| **What is built** | The verdict is authored per mixture. White light keeps her sentence to the character. Blue and red reads *"One patch of pinky-purple — the two colours put back together, and still no yellow or green"*, and the note's phrase becomes *"…together as one pinky-purple beam, with no yellow and no green anywhere in it"* — the rest of her sentence, *if glass made colour, a second piece would make more of it. It makes less*, untouched. A mixture that declares no wording is now refused at build time. |
| **The defect in hers** | Blue and red recombined give magenta. White needs the whole spectrum, and the state's own input sub-line says so — *"two separated bands, no yellows or greens"*. Her own drawing was honest, stroking the outgoing beam `#9A647A`, a dusky pink, so the tile contradicted the picture beside it as well as the physics — and it undercut the lesson's central argument, that a prism gives back only what went in, by claiming two colours in and white out. |

### 8. `p7-05` drew the pupil as a constant and the iris the wrong way round — MRB-297, P7-19

| | |
|---|---|
| **Where** | `p7-05` `#s-eye`, `[data-eyecam-stop]`. Her construction: `'M' + (cx−118) + ' ' + (200 − rPx) + ' V194 M' + (cx−118) + ' 206 V' + (200 + rPx)`, with `rPx = eye ? mm × 9 : mm × 1.7`. |
| **What she drew** | The two marks are the STOP — the opaque part — and their INNER ends were the constants. So the hole was 12 units at every light level, on both instruments, while each blade grew from 12 units in bright sunlight to 66 on a moonless night. Dragging from sunlight to darkness closed the front of the eye into a near-solid pillar with a hairline slit in it. Both rays were routed through `200 ± rPx × 0.7`, which put them INSIDE the opaque marks at every setting, so the drawing also had light passing through the iris. |
| **What is built** | The construction is inverted: the OUTER ends are pinned to the case — the eyeball's own outline at y = 200 ± 72, the camera's lens barrel at 200 ± 74 — and the inner ends move, so the drawn gap is 2 × `rPx` and GROWS in the dark. Measured across all ten states, the eye's gap runs 31 → 124 units for 2.0 → 8.0 mm, exactly proportional, and the camera's 10 → 128 for 3 → 50 mm. `rPx` is clamped ten units inside the case so there is always a blade left to see, and floored at 5 so the smallest aperture still has a visible hole; the floor lifts only the camera's 3 mm state. Her ray waypoints are untouched and are now correct as written, because 0.7 of the half-opening is inside the hole. |
| **The defect in hers** | **The lesson's one adjustable quantity was drawn as unchanging, and the part that changed, changed the wrong way.** A dilating iris opens. The readout beside the drawing said 2.0 mm → 8.0 mm, and the gate question a student answered one screen earlier says the pupil opens in the dark. Every readout and note on the bench was already right; nothing but the drawing changed. |

---

## Considered, not changed — 8 rows

**`p7-04` computes an image height and carries no formula block** (her FLAG 4).
`h_image = h_object × (v ÷ u)` is a genuine product and would take a triangle
cleanly. She leaves it out because `LGT.04` says *qualitative* for the convex
lens, the pinhole clause carries no arithmetic, and a triangle over three
lengths invites magnification, which is GCSE — and she flags it herself:
*"This is the one place in the two units where a reviewer might reasonably want
a block that is not there."* **That is Mide's call, not a lane's, and it is
passed through unresolved.** The bench prints its working in the readout
sub-line, `300 mm × v ÷ u`, at every setting.

**`p7-05`'s bench holds two instruments** (her FLAG 8). An eye and a camera,
switched by a toggle that redraws the whole cross-section. It brushes against
"one practical per bench" and she says why it stands: the comparison IS the
lesson, and a student is never left with two answers to *describe the
apparatus*. Built as drawn. She asks a reviewer to ratify it or ask for two
figures instead.

**`p7-06` and `p7-07` use hue as part of the message** (her FLAG 10). Colour is
the subject, so it cannot be avoided. Kept, with both channels: every state
prints the colour AS A WORD in a readout tile, in the caption and in the note;
the `p7-07` ray goes grey AND dashed when nothing comes back; and both marked
rungs on both pages are answerable from the words alone. Her legal lines
declare the screen colours as approximations of spectral colours.

**`--ks3-data` (her FLAG 9) now exists, and P7 does not need it.** She records
the token as missing and says these pages therefore use `--ks3-blue-light` for
selection on ink-dark and `--ks3-accent-text` on cream. Both are correct today:
MRB-252 minted `--ks3-data` for *category and selection* uses, and P7's
selection is carried by `aria-pressed` on a segmented control that the engine
already styles. Nothing here needed a category hue, so nothing was changed to
use one.

**`d = v × t` appears three times across two units** (her FLAG 5). `p6-06`
teaches it for sound, `p6-07` uses it as given data, and `p7-01` teaches it
again for light. No lesson assumes the others; each states the relationship
from nothing and carries the others as edges. She asks a reviewer to check it
reads as reinforcement rather than as a missing single-source ruling.

**`p7-01`'s attempt head reads "Your gap: 1 m, which is 1 m." at the short
end.** Her own computation is `'Your gap: ' + dLabel + ', which is ' + grp(d) +
' m.'`, and below 1000 m the two halves are the same words. Kept: it is her
sentence, it is never wrong, and the redundancy only appears at the two
shortest of the hundred and one distances.

**`p7-04`'s `verdict` string is computed and never displayed.** Her
`lessonVals()` builds *"sharp, and dim"* / *"a working compromise"* / *"bright,
and blurred"*, and her fourth tile prints the fixed sentence *"Upside down, and
left for right"* instead. The DRAWING was measured and the tile is hers; the
unused string is not authored here, because an authored key nothing reads is
what `ks3_key_audit` exists to catch.

**`p7-05`'s optic-nerve stub is drawn at the FRONT of the eye.** Her path is
`M(cx − 140) 200 h−70`, which puts it on the left edge of the eyeball, the side
the scene is on. Kept: it is her geometry, the caption does not name it, and
moving a line on a simplified cross-section is a change to a drawing with no
defect anybody can state.

---

## Not departures, and why

Everything below is this lane's own defect or the engine's. None is a change to
what Design drew, and none takes a row.

**MRB-278 · ALL FOURTEEN MARKED RUNGS ARE REORDERED, AND IT IS ENGINE POLICY
RATHER THAN A DEPARTURE.** Design's `RUNGS` put the correct option at index 0
on every one of P7's fourteen marked rungs — the exact answer-position defect
`verify_ks3` fails a unit for. Every option's TEXT and every correction is hers
and untouched; only the ORDER changes, the distractors keep their relative
order, and each correction travels with its own option. Measured after:
`{0: 3, 1: 3, 2: 4, 3: 4}` across the unit's fourteen. Recorded in each
lesson's docstring, as P6's are.

**A bare `data-<hook>-out` sat in the readout tiles' own attribute namespace.**
Three benches named an SVG path `data-rsurf-out`, `data-rblock-out` and
`data-clamp-out` while their readout tiles are `data-<hook>-out="id"`, so a
`querySelectorAll("[data-rsurf-out]")` returned the path alongside the four
tiles and read its (empty) text as a readout. Nothing was broken on the page —
the setter is keyed by value — and it would have broken the moment anything
enumerated the readouts. Renamed `-refrays`, `-exit` and `-back`. Found by a
state-space drive, not by a gate.

**Every live label was positioned against the padded panel instead of the
drawing.** Design nests the SVG and its spans one level deeper than the card —
a bare `position: relative` div inside the padded panel — so her percentages
resolve against the viewBox. The first cut made the padded panel the positioned
ancestor, which slid every label on all seven benches up and left by 18px, far
enough on `p7-07` to put "White light" under the lamp so the page read *"hite
light"*. Found by cropping the figure and looking at it: the spans were
present, filled, correctly coloured and in front, so every assertion a sweep
makes was true. `.ks3-<hook>-figinner` is now the positioning context.

**P4, P5 and P6 ship their eyebrow and heading TWICE on every bench, and P7
does not.** Measured in the built bytes of `pressure-force-over-area.html` and
`sound-needs-a-medium.html`: `r_activity` emits a `.ks3-blockhead` with the
eyebrow, the `<h2>` and the progress readout, and then each unit's drawer emits
its own head row with the same three strings. `.ks3-blockhead` IS Design's row
— eyebrow and heading left, right-aligned mono readout right — and MRB-220
built the head counter for exactly this. So every P7 bench authors
`head_counter` with her own two states, the drawers start at the commit gate,
and the wiring drives the shared `[data-count]` through `setCount`. **This is a
departure from the P4–P6 PORT, not from Design**, whose layout it reproduces
rather than doubles. The three shipped units are not touched.

**Two more doubled heads, found by the commander's crop and fixed the same
way (25 Aug 2026).** The first cut of P7 still printed the figure blocks'
eyebrow and heading twice — once from the `check` shell's `.ks3-blockhead`
and once inside `r_light_band`, exactly as P6's `r_wave_band` does on every
shipped P6 figure — and the attempt panel's *"Your turn · the same five
steps"* twice, once from the shell and once from `kit.r_cfifa_attempt`, as
every shipped P4–P6 attempt panel does. `r_light_band` no longer emits its
own head, and `r_p7_attempt` passes `eyebrow: None`, which the kit now reads
as "already printed" (an absent key still takes the default, so P4–P6's
bytes are unchanged and they still print it twice — reported, not fixed
here). Design's pages print each once.

**⚠️ `ks3_art/kit.py` IS EDITED, AND IT IS A SHARED FILE.** `r_cfifa_attempt`
refused fewer than two questions. Design's `p7-02` carries one, and her README
states the reason: *"its quantities are angles in degrees, so conversion cannot
arise and the C step reads as the no-conversion case."* Her own `Cfifa`
component renders `q2 ? [q1, q2] : [q1]`, so one question is a shape she built
for. The payload key `one_question_because` lifts **that check and nothing
else**, and it costs a sentence naming the reason, which is what stops it
becoming the way a lane skips authoring a question. No other unit's output
moves: P4, P5 and P6 all declare two.

**The attempt panel's lede is the `Cfifa` component's own default sentence.**
*"Write each line out yourself — starting by deciding whether anything needs
converting. Then check your working and tick the lines you had."* Her component
renders that string for every write-mode question and reads `lead` only when
the question is blocked, so it is what a student on her page actually sees. P6's
port authored a different sentence there; P7 does not follow it.

**One authored key was read by nothing, and the fix was in the code.**
`ks3_key_audit` reported `p7-05`'s `cam` width dead, because the wiring
composed the attribute name (`"data-" + key`) — a read site no lint and no
reader can see. The two keys are now named as literals in both the drawer and
the runtime, which is also the safer shape: an unknown key reads as NaN rather
than as a silently missing attribute.

**Thirty-one of the bank's eighty-four questions were length tells**, fixed the
same way and at the same place: one distractor per set, finished into a
complete wrong rule. Answer positions across the bank measure
`{0: 21, 1: 21, 2: 21, 3: 21}`.

---

## What remains different, and why

Seven strings of hers are not on our pages, and all seven are **aria
descriptions of drawings**: *"A cross-section of an eye with the scene on the
left…"*, *"A ray arriving at 40 degrees to the normal on plane mirror…"*. Hers
describe HER SVGs; ours describe ours, which are this engine's drawers rather
than her elements — and where the two drawings differ, as on `p7-02`'s beam,
carrying her sentence would describe a picture that is not there. That is the
only category of her text this unit does not carry.
