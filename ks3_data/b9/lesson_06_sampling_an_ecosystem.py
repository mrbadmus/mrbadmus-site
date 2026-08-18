"""B9 L6 — Sampling an ecosystem (INVESTIGATION).

Authored against Claude Design's approved page,
`KS3 B9 lessons/b9-06-sampling-an-ecosystem.dc.html` (617 lines), her author's
notes `KS3 B9 lessons/NOTES-B9.md`, and the B9 payload schema
`docs/ks3/b9-inventory/PAYLOAD-SCHEMA.md` §0, §1, §2, §4, §10, §11, §12 and
§14, under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the two listed under "What could not be lifted", neither of which is a
science word. The four rule cards, both marked rungs, both self-marked rungs,
the three method labels, the three count labels, the four verdict branches and
the three grid captions came out of the page's own `RULE_CARDS`, `RUNGS`,
`SELF_RUNGS`, `METHODS`, `COUNTS` and `renderVals()`, not off a keyboard.

── The whole lesson is ONE sentence, and it is a sentence about ERROR ────

⚖️ **INCREASING THE SAMPLE SIZE FIXES RANDOM ERROR AND DOES NOTHING AT ALL FOR
BIAS.** Three random quadrats → eight → twenty-five converge on the true mean.
Twenty-five drawn from the flowery corner are drawn from a pool of exactly
twenty-five squares, all of them inside the cluster, so the LARGEST sample on
the biased setting is the most stably wrong: it exhausts its pool, becomes
deterministic, and returns the same wrong answer every time. Measured on the
built page, twenty runs at each random setting and ten at each biased one:
random placement 34% mean error at three quadrats → 18% at eight → 12% at
twenty-five, converging; the flowery corner 102% over at three and 99% over at
twenty-five, with a spread of **exactly zero** across six runs; the path edge
59% under.

⚠️ **Those figures are one field's, and the next reload draws a different one.**
The field is unseeded (see below), so the numbers above are the SHAPE of the
result and not a reproducible measurement — what is reproducible is the
ordering, and that is what `ks3_parity`'s `b9-field-revealed` drive asserts
rather than any percentage.

⛔ **NEVER "BALANCE" THE THREE POOLS.** `random` is all 100 squares, `corner` is
the 25-square bottom-left quadrant, `path` is the 30 squares of the top three
rows. Those sizes are not an oversight and they are not tidy. A revision that
evens them out, or that lets the sample-size dial shrink the bias, deletes
`NOS-04`'s confrontation and leaves a bench that teaches "more is better" —
which is the belief the lesson exists to take apart. `r_quadrat_bench` measures
the two biased pools against the field's own clustering model and refuses a set
that is not biased in both directions; `ks3_parity`'s `b9-field-revealed` drive
re-measures it in a browser, twelve runs at each setting.

── The field is UNSEEDED, and that is the design ────────────────────────

⚠️ 100 `Math.random()` calls, once, at mount — the only `Math.random()` in B9.
The field is regenerated on every reload, so two students never see the same
field and no student sees the same one twice. The estimate cannot be memorised
and the reveal cannot be spoiled. **The page is therefore not
screenshot-reproducible, deliberately.** Design's legal line states the
behaviour and it is carried across as delivered — see `convention_note`.

⚑ NOTES-B9 §3 asks Mide to confirm this is wanted rather than a fixed seed. It
is a PRODUCT decision, not a port decision, and it is carried with the
behaviour: a seed would make the verdict percentages reproducible for a teacher
demonstrating at the front, and would cost the two properties above.

── FOUR rail stops, and the third is a MIRROR (MRB-249) ─────────────────

Design draws four (page lines 320–326) and her `isDone()` gives `s-rules` the
BENCH's predicate, character for character, one section to the right:

    if (id === 's-bench') return s.truthShown;
    if (id === 's-rules') return s.truthShown;      // page lines 407–408

`#s-rules` is an eyebrow, a display statement, four static cards and a key
fact: no control, no commitment, no reveal. It carries none of the five DOM
signals `doneByDom()` reads, which is why the payload schema's §4 first told
this unit to author three stops and drop it. **That instruction is reversed and
the reversal is the unit ruling** (`ks3_data/b9/__init__.py`): MRB-205 binds and
is not re-argued — Design draws, we render, and the page wins over the engine.
A band holding four fact cards and the KEY FACT is 5 KB of teaching, not a
spacer. `ks3_parity.check_rail_matches_design` gates the built rail against
`docs/ks3/rail-manifest.md`, whose row for this lesson reads
`s-hook s-bench s-rules s-ladder | s-rules=s-bench`, so three stops FAIL the
build.

⚖️ **THE BENCH STOP TICKS ON THE REVEAL, NOT ON THE SAMPLE**, which is Design's
own threshold (`s.truthShown`, not `s.picked.length`) and is a teaching claim
rather than a wiring detail: an estimate you have not checked against the truth
is not the lesson. `done_when` is `truth_revealed` on both the bench and its
mirror.

⚠️ **THE PREDICATE IS MONOTONIC HERE AND IS NOT MONOTONIC ON DESIGN'S PAGE.**
Design's `takeSample()` and both dial handlers set `truthShown: false`, so her
rail stop UNTICKS the moment a student re-samples or switches method — a
student who has surveyed the field three ways is shown less progress than one
who surveyed it once. MRB-208 rules the rail records participation, and what a
student found out cannot be un-found. `wireQuadratBench` therefore keeps its
own sticky `everRevealed` and passes that to `markStage`, while the FIGURES and
the verdict still clear exactly as Design draws them. The drive asserts both
halves: switching method must clear the previous survey's figures, and must not
untick the stop.

── `#s-think` is a `confrontation` and is on NO rail ────────────────────

Measured, per payload schema §3: two `ks3-mis-quote`s, two bodies, a
`border-top` divider, and no `ks3-options`, no `sc-if` reveal, no button and no
state. Contract R1 makes `#s-think` a `predict` only where it asks for a
commitment and then reveals; that is B2, C1 and C2's shape and not B9's. So it
is a `confrontation`, emits no `data-stage-done`, and is not a rail stop on
Design's own page either.

── What could not be lifted byte-identical, and why ─────────────────────

Two, and no science word moves in either.

1. ⚖️ **`#s-think`'s second body pointed the student at two dial settings the
   bench does not have.** Design writes *"You can see both on the bench above
   by taking five random quadrats and then thirty, and then doing the same on
   the flower-rich corner."* The bench offers 3, 8 and 25. Five and thirty are
   not on it, so the sentence sends a student to press two controls that are
   not there, and the one instruction on the page that names the instrument is
   the one instruction that cannot be followed.

       Design:  by taking five random quadrats and then thirty
       Built:   by taking three random quadrats and then twenty-five

   **The figures are Design's own**, from the corner verdict two sections up:
   *"Take twenty-five instead of three and the answer does not improve"*. The
   page supplies its own correction, the sentence's work — smallest setting
   against largest, first fairly and then crookedly — is unchanged, and the
   claim it is making is the one the bench now demonstrably shows. This is a
   page contradicting itself rather than a page contradicting the engine, so
   MRB-205's "page wins" does not resolve it; the page's own instrument does.

2. **Rung 1's three distractors, under MRB-177.** See the ladder note below.
   The correct option is untouched, and every one of the three corrections is
   byte-identical.

⚑ **No slot code reaches a student on this page.** Grepped: the only `b9-`,
`b6-` and `b10-` strings in the delivered file are endmatter `href`s, and no
prose sentence names a lesson by code. There was nothing of b8-01's shape to
resolve. Every endmatter destination survives as a real `requires` or
`references` edge.

── The two failures are the KEY FACT, and the KEY FACT is nested ────────

Design nests the box inside `#s-rules` (page lines 178–181) on `--ks3-card`
with the 5px accent offset shadow, because the section itself is `--ks3-band`
and band on band is invisible. Authored `{"ref": …, "ground": "card"}` inside
the `rule` block; `r_rule()` takes a nested key fact and defaults it to `card`
for exactly that reason. Never amber: measured, the box is card + 2px ink
outline + accent shadow, which is what MRB-208 fixes as its identity.

The four `RULE_CARDS` keep all three of their parts. Design's `kind` is the
mono accent tag and maps to `role`, which is the slot `_rule_card()` reads for
it — the repair `_rule_card` took under MRB-245 after b7-01's part cards
shipped as empty `<li>`s. Nothing is joined, dropped or invented.

── ⊕ MRB-177 LENGTH PARITY — RUNG 1 REPAIRED, RUNG 2 CLEAN ──────────────

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`).

**Rung 2 passes as delivered and nothing was touched.** Correct 11w against
8 / 5 / 9 — strictly the longest, but the gap to the longest distractor is 2
and the ratio is 1.22, inside both thresholds. That is not luck: the correct
option names a FAULT in the estimate and states what does not fix it, and all
three distractors name a fault in the estimate and state what would — nothing
wrong here, the quadrats were too small, they should have counted the lot.
Same subject, same shape, same kind of consequence, which is what the MRB-177
ruling asks for and is why the parity falls out rather than being imposed.
⚖️ Option C is five words and is still not a tell: the gate measures the
correct option against the LONGEST distractor, not the shortest, and padding a
short belief makes it sound more considered than the student's own version of
it. Recorded so a later pass does not "fix" a clean rung.

**Rung 1 FAILED as delivered and was repaired at the distractor.** Design's set
runs `About 4800` / `60` / `800` / `80` — 2w against 1 / 1 / 1. The correct
answer is strictly the longest and clears the longest distractor by 2.0×, which
is over the 1.4× threshold, so `length_tell()` flags it and the build fails.
A student who has worked out that the odd-one-out is usually right — and a
class works that out early — can take this rung without reading the numbers.

The repair follows b2-04's precedent exactly, which is the other numeric rung
in the key stage: **four options of equal length cannot be a length tell, and
shortening or padding a numeric answer would be tampering with a calculation.**
So each distractor takes the correct option's own hedge and keeps its number
and its misconception unchanged:

    Design:  About 4800  ·  60          ·  800          ·  80
    Built:   About 4800  ·  About 60    ·  About 800    ·  About 80

2 / 2 / 2 / 2, no strict maximum, gate clean. The correct option is UNCHANGED
because it is the science; all three corrections are unchanged because they
name the arithmetic, and each still reads exactly against its option ("That is
the total found in the ten quadrats"). Nothing quantitative moves.

⚑ Neither of rung 1's distractors is a register belief — they are three
arithmetic errors (report the raw total, report the area, divide by the wrong
quadrat size), and the corrections say so. Rung 2's option A **is** `NOS-04`
in a student's own words: *"Nothing — 30 quadrats is a large sample"*. That is
recorded in a comment on the option, and it is why `NOS-04` names `s-ladder` as
its `elicited_by`.

── Misconception ids: `ECO-11` and `NOS-04`, and `ECO-12` MUST NOT EXIST ─

⛔ **`ECO-12` IS NOT MINTED HERE OR ANYWHERE.**
`docs/ks3/misconception-register.md` permanently reserves it — *"`ECO-12` — is
`NOS-04`"* — in the "Re-homed before they were minted" list, alongside
`GENE-06` and `REACT-18`. NOTES-B9 §4 says this unit opens *"`ECO-01` to
`ECO-12`, two per lesson"* and §1.6 says the sample-size separation is the point
of `ECO-12`. **Both are superseded by the register and neither is followed.**
The second belief on this page — *a large sample is an accurate sample* — is a
belief about how evidence settles a question rather than about ecosystems, so
it belongs to the nature-of-science family, and the register has already
allocated `NOS-04` to this exact lesson by name.

⚠️ **`NOS-04` already has a row and it is in the RESERVED table, not the
entries table.** It is reserved with the statement *"A large sample is an
accurate sample."*, the lesson `B9 sampling-an-ecosystem`, and the note that
each reserved id *"is minted by the pass that authors the page, not by this
one"*. This pass is that pass — but `docs/ks3/*` is the commander's file under
contract §0, so the row is not written here. The statement below is
byte-identical to the reserved one, and the report names the two edits the
register needs: promote `NOS-04` into the `NOS` entries table with its elicited
/ confronted values, and strike its line from "Reserved, not minted here".

⚠️ **The `ECO` prefix row is not yet open** — grepped, no `ECO-*` row exists.
Five sibling passes mint `ECO-01`…`ECO-10`; this one mints `ECO-11` and the
family stops there for ever. No gate resolves an id against the register file
(`build_ks3.py`, `verify_ks3.py` and `ks3_parity.py` do not read it), so the
lesson builds either way; what is at risk is the register's completeness.

Both values resolve against the BUILT page (MRB-244 / MRB-248): `s-think` is
the confrontation block's emitted anchor, `s-ladder` is the quiz block's.
`ECO-11` gets no `elicited_by`, and that is measured rather than forgotten —
nothing on this page asks a student to commit to *throwing the quadrat makes it
random*. The hook's four options are about how to get a number at all, not
about how a quadrat is placed, and `#s-think` is static. Absence is legal
(MRB-248) and inventing an element name to fill the key would be worse than the
gap.

── Keys this pass authors, and where each is read (contract R5) ─────────

Every one is measured off `r_quadrat_bench` and `wireQuadratBench`:

    side              the grid, and `_KIND_HEAD_TOTAL`   build_ks3 L14937, L15635
    field             the clustering model, term for term  build_ks3 L14953, ks3.js L14371
    progress          {before, after} → the head readout   build_ks3 L15702
    methods/labels    the three tabs; the ids are FIXED    build_ks3 L14981
    counts            the dial, strictly increasing        build_ks3 L14968
    count_label       "{n} quadrats", `{n}` per count      build_ks3 L15088
    default_count     which count the bench opens on       build_ks3 L14974
    figures           three slots, in this order           build_ks3 L15035
    hidden_value      what the `real` slot says until then ks3.js L14458
    captions          three grid states                    ks3.js L14453
    sample/resample   the button's two labels              ks3.js L14465
    truth_label       the reveal button                    build_ks3 L15125
    verdicts          four branches, composed              ks3.js L14472
    direction         {over, under} → the corner's `{dir}`  ks3.js L14476

⊕ **`direction` and `count_label` are engine-pass additions the schema had not
anticipated.** Payload schema §10's sketch has neither: it writes the counts as
whole labels (`"3 quadrats"`) and does not mention the corner verdict's
over/under fork at all. Design composes both in JS — `(over ? 'far too high' :
'wrong')` at page line 501, and `c.id + ' quadrats'` in `COUNTS`. Following the
schema literally would have authored the word "quadrats" three times and would
have forced the corner verdict to pick one direction and be wrong whenever the
field fell the other way. **The map wins on measurement**, per the schema's own
opening rule, and both keys are authored.

⛔ **NO RUNTIME STATE IS AUTHORED** (payload schema §0 rule 3). Design's state
bag holds `field`, `picked`, `truthShown`, `method`, `count`, `active`,
`answers`, `text`, `checked`, `ticks`. Every one is a value the runtime owns;
under R5 a key with no read site fails `ks3_key_audit.py`. The renderer builds
its own field and initialises its own state.

⚠️ **THIS INSTRUMENT IS ON INK.** `ks3-block ks3-dark ks3-practical`, measured
from Design's own class attribute at page line 104, so `segment: "practical"`
is measured and not inferred from the kind name — contract §4 records that B1
got two of six wrong by inferring it. `.ks3-dark p` is (0,1,1) and beats a bare
instrument class at (0,1,0); as of MRB-245 `ks3_parity`'s
`check_dark_text_specificity()` gates it.

── `covers`: the one statement this lesson owns is a WORKING one ────────

`KS3.WS.EXP.06` reads, in full: *apply sampling techniques*. That is this
lesson and nothing else in the key stage claims it — grepped. NOTES-B9 §0 says
b9-06 *"carries no statement of its own"* and reads that as a weakness; it is
not, it is a lesson whose statement is in Working Scientifically rather than in
`ECO`. The other five B9 lessons discharge `ECO.01`–`ECO.03` between them and
this one is the fieldwork the rest of the unit would otherwise be asserting
without method — NOTES' own phrase for it.

`KS3.WS.ANA.05` — *evaluate data, showing awareness of potential sources of
random and systematic error* — is `touches`, not `covers`. Bias is systematic
error and chance is random error, and separating them is the whole bench; but
`b6-03` owns that statement and discharges it on health claims, and WS
statements being exempt from the exactly-once rule is not a licence to claim
one twice. The lesson names it, uses it, and does not own it.

⚑ For Mide's science gate — every NOTES-B9 item landing on THIS lesson:

  * §1.6 / §3  **The unseeded field.** Carried across as delivered, with the
               question. See the ⚠️ above; it is a product decision.
  * §1.6       **The `ECO-12` pointer.** Re-pointed to `NOS-04`, per the
               register and payload schema §14. Reported, not edited.
  * flag 16    **Capture–mark–recapture in *Going further*,** including
               trap-shy and trap-happy animals. CHECKED AND LEFT. The method
               and every one of the four assumptions Design lists — mixing
               back in, the mark not changing predation or trap behaviour, no
               births/deaths/migration in between — are the standard Lincoln
               index assumptions and are stated as assumptions rather than as
               facts, which is what makes the paragraph a *how do we know*
               story. Trap-happiness in small mammals is real and well
               documented; the mouse-returning-for-free-food sentence is the
               textbook illustration of it. It is beyond the KS3 programme of
               study, which is exactly what the stretch layer is for, and
               NOTES asks Mide to confirm the depth rather than the content.
  * flag 17    **No diagrams anywhere in B9.** `figures: []` here is MEASURED
               — `<img>`, `<figure>` and `<picture>` each appear zero times on
               this page, grepped, and the foot line names no slot. §4.10
               allows an empty `figures` for a lesson carried by its
               interactives. The flag names a drawn food web for b9-01 and
               b9-03 and is not dropped by this; it is Mide's to rule on.

── MRB-225, checked across the whole lesson ─────────────────────────────

The claim this page makes six times is *bias and sample size are independent
problems, and only one of them yields to more work*. Hook reveal ("everything
that can go wrong with it comes down to two things"), the bench's four
verdicts, the `Bias` and `Too few quadrats` cards, the display statement, the
KEY FACT, `#s-think`'s second body, rung 2 and the key note all state it at the
same size. Nothing above is walked back below, and the stretch layer adds a
method for animals and retracts nothing.
"""

# ── the three placements (page lines 344–348) ────────────────────────────
#
# ⛔ THE IDS ARE FIXED and `r_quadrat_bench` refuses any other set: the POOL
# each one draws from is the pedagogy and is implemented against these three
# names in `wireQuadratBench`. `random` is all 100 squares, `corner` is the
# 25-square bottom-left quadrant — the cluster — and `path` is the 30 squares
# of the top three rows, farthest from it. One pool overstates and one
# understates, which is what proves bias has no favourite direction.
METHODS = [
    {"id": "random", "label": "Random coordinates"},
    {"id": "corner", "label": "The flowery corner"},
    {"id": "path", "label": "Along the path edge"},
]

# ── the four fact cards (page lines 355–360) ─────────────────────────────
#
# Design's `kind` is the mono accent tag and maps to `role`, the slot
# `_rule_card()` reads for it. Two of the four ARE the lesson: `Bias` and
# `Too few quadrats` are the two failure modes the bench separates, and the
# order is Design's — the method, then the failure more work cannot fix, then
# the failure more work does fix.
RULE_CARDS = [
    {"role": "The method", "name": "Mean, then scale up",
     "body": "Add the counts, divide by the number of quadrats to get a mean "
             "per quadrat, then multiply by how many quadrat-sized areas fit "
             "in the whole site."},
    {"role": "Failure one", "name": "Bias",
     "body": "Sampling where you chose to rather than where chance sent you. "
             "Every extra quadrat repeats the same error, so the estimate is "
             "wrong and confident."},
    {"role": "Failure two", "name": "Too few quadrats",
     "body": "Chance alone can land three quadrats on a bare patch. The "
             "estimate is not biased, just unreliable, and more samples "
             "genuinely fix it."},
    {"role": "Also worth knowing", "name": "Quadrat size and edges",
     "body": "The quadrat must suit the organism, and everyone must agree the "
             "rule for plants on the line — usually count two sides and not "
             "the others."},
]

# ── the four verdict branches (page lines 500–504) ───────────────────────
#
# ⚖️ COMPOSED, NEVER AUTHORED AS FOUR FIXED SENTENCES. `{err}` is the signed
# percentage error the bench has just produced and `{n}` is how many squares
# were counted; a verdict that quoted a fixed figure would be wrong on every
# setting but one, and `_b9_placeholders` fails the build for a branch that
# names the wrong braces. `{dir}` is the corner branch's over/under fork —
# see `DIRECTION` below.
#
# The ORDER is Design's and the third branch is tested LAST of the three that
# can fire: a biased three-quadrat sample is biased AND unlucky, and only one
# of those is the thing more work cannot fix, so bias is named first.
#
# ⛔ The corner branch's last two sentences are `NOS-04`'s confrontation in
# words, and the path branch's last sentence is `ECO-11`'s consequence. Neither
# may be softened: they are the only place on the page where the separation is
# stated as a measured result rather than as a rule.
VERDICTS = {
    "corner": "Out by {err}%, and {dir}. Every quadrat landed in the richest "
              "part of the field, so the mean describes that corner rather "
              "than the field. Take twenty-five instead of three and the "
              "answer does not improve — it just stops wobbling. That is what "
              "bias means, and it is the one error more work cannot fix.",
    "path": "Out by {err}%, and this time too low. The path edge is trampled "
            "and the daisies are thin there, so the sample understates the "
            "field by as much as the flowery corner overstated it. Bias has "
            "no favourite direction; it simply follows wherever you chose to "
            "look.",
    "chance": "Out by {err}%. The placement was fair, so this error is chance "
              "rather than bias — three squares out of a hundred is not much "
              "to go on. Run it again and you will get a different answer; "
              "run it with twenty-five and the answers cluster much more "
              "tightly.",
    "good": "Within {err}% of the real total, from {n} squares out of a "
            "hundred. Random placement kept it honest and the sample size "
            "kept it steady. This is the whole method, and it is how every "
            "population figure you have ever read was produced.",
}

# ⊕ ENGINE-PASS ADDITION, not in payload schema §10. Design composes the
# corner verdict's third clause in JS — `(over ? 'far too high' : 'wrong')`,
# page line 501 — and the two are not interchangeable: the flowery corner
# normally overstates, but on a field whose cluster the noise term has moved it
# can come out low, and "far too high" would then be a lie printed beside a
# negative number. `{dir}` is filled from here.
DIRECTION = {"over": "far too high", "under": "wrong"}


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 159 character for character.
    "slug":        "sampling-an-ecosystem",
    "title":       "Sampling an ecosystem",
    "discipline":  "biology",
    "unit":        "ecosystems-and-interdependence",
    "family":      "INVESTIGATION",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.WS.EXP.06` — "apply sampling techniques" — owned whole and
    # discharged by `#s-bench`, `#s-rules` and rungs 1 and 3. See the
    # docstring: this lesson's statement is a Working Scientifically one, which
    # is not the same thing as having none.
    "covers":      ["KS3.WS.EXP.06"],
    # Named, used, owned elsewhere. ANA.05 is b6-03's random-vs-systematic
    # error statement, which the two failure cards and the whole bench lean on
    # and none of them restates. ECO.01 is b9-01's and b9-03's; this page
    # supplies the method the rest of the unit's numbers would need and teaches
    # none of the interdependence itself.
    "touches":     ["KS3.WS.ANA.05", "KS3.B.ECO.01"],
    "beyond_statutory": False,
    "threads":     [{"id": "evidence-and-explanation", "level": 2},
                    {"id": "structure-function", "level": 1}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" card, in her order (page lines 289–290).
    # Both exist and both build. `substance-misuse-and-decisions` is B6's and
    # takes the dict form for a cross-unit edge; the registry is flat, so the
    # unit code is accepted and ignored, but writing it is what §4.6 asks for
    # and is what stopped b7-03 raising `cannot use 'dict' as a dict key`.
    #
    # ⚑ b6-03 is the right prerequisite and is not decoration: it is where a
    # student first meets "more people does not fix a confused comparison",
    # which is this lesson's sentence in a health costume. The register agrees
    # from the other end — `NOS-05` lives there, and `NOS-04` reappears there.
    "requires":    ["food-chains-and-food-webs",
                    {"unit": "B6", "lesson": "substance-misuse-and-decisions"}],
    "assumes":     [],
    # Design's "Connects to" card, in her order (page lines 296–297).
    # ⚠️ `variation-continuous-and-discontinuous` is B10's first slot and is
    # NOT YET AUTHORED. That is why it is a `references` edge and not a
    # `requires` one: an unknown `requires` target is a build failure, while an
    # unbuilt reference renders as "Variation: continuous and discontinuous
    # (Inheritance and DNA — coming soon)", which is the structure-first
    # guarantee working rather than a gap. NOTES-B9 §3 flags the same edge.
    # It resolves the moment B10 lands and nothing here changes.
    "references":  ["predator-and-prey",
                    {"unit": "B10",
                     "lesson": "variation-continuous-and-discontinuous"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Required practical fieldwork: random and systematic "
                   "sampling, transects along an environmental gradient, and "
                   "capture–mark–recapture.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Nobody has ever counted the daisies in a field. Every "
                    "number you have ever read about how many of something "
                    "there are was worked out from a sample — and a sample can "
                    "be taken badly.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them (page lines 320–326). `s-rules` is the
    # third: no control of its own, so it mirrors `s-bench` and ticks on the
    # bench's predicate — see the docstring, which also supersedes payload
    # schema §4's three-stop instruction. `short` and `label` are Design's own
    # `RAIL_SHORT` and `RAIL` strings, "Two failures" included.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "How many daisies",
         "done_when": "committed"},
        # ⚖️ Design's own threshold, kept: `s.truthShown` (page line 407), not
        # `s.picked.length`. The stop ticks when the student has checked the
        # estimate against the truth, not when a sample has been drawn — an
        # estimate you have not checked is not the lesson.
        {"anchor": "s-bench", "short": "BENCH", "label": "Survey it",
         "done_when": "truth_revealed"},
        {"anchor": "s-rules", "short": "RULES", "label": "Two failures",
         "mirrors": "s-bench", "done_when": "truth_revealed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key. B is the method the
    # lesson goes on to build, and the reveal says so at once; the hook is not
    # a trick, it is the claim the bench then has to earn against a real total.
    #
    # ⚖️ Option C — "the squares that look typical" — is the bias belief in its
    # most reasonable-sounding form, and it is deliberately the option that
    # sounds most sensible. It is NOT `ECO-11`: `ECO-11` is a claim about what
    # makes a placement random, and nothing here asks the student to make one.
    # See the misconceptions note.
    "phenomenon": {
        "kind": "narrative",
        "title": "How many daisies are in the school field?",
        "prompt": "It is a fair question with a real answer, and counting them "
                  "would take a class about four days. Every ecologist, every "
                  "conservation charity and every government report faces the "
                  "same problem, and none of them counts.",
        "commit": "What is the best way to get a trustworthy number?",
        "options": [
            "Count every one, carefully",
            "Count a few small squares chosen at random and scale up",
            "Count the squares that look typical and scale up",
            "Estimate by eye — nobody can check it anyway",
        ],
        "reveal": "Count a small number of small squares, chosen at random, "
                  "and scale up. That is a quadrat survey, and everything that "
                  "can go wrong with it comes down to two things: how the "
                  "squares were chosen, and how many of them there were.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # The commander's pre-allocation, payload schema §14. Both statements are
    # Design's own quoted beliefs in register voice.
    #
    # ⛔ `ECO-12` IS NOT MINTED, HERE OR ANYWHERE — the register reserves it
    # permanently as `NOS-04`'s old name. NOTES-B9 §4 and §1.6 both say
    # otherwise and both are superseded. See the docstring.
    #
    # ⚠️ Neither the `ECO` prefix row nor `NOS-04`'s entry row exists yet, and
    # `docs/ks3/*` is not this pass's to edit (contract §0). The two register
    # edits are named in the report.
    #
    # Both `confronted_by` values resolve against the BUILT page (MRB-244):
    # `s-think` is the confrontation block's emitted anchor. `NOS-04`'s
    # `elicited_by` is `s-ladder`, the quiz block's anchor, because rung 2's
    # option A is the belief word for word and the student commits to it or
    # declines to before the correction names it (MRB-248: a value that is
    # present must be true).
    "misconceptions": [
        # No `elicited_by`, and it is measured rather than forgotten: nothing
        # on this page asks a student to state that throwing makes a placement
        # random, or offers it as an option. The hook asks how to get a number
        # at all; `#s-think` is static. Absence is legal and inventing an
        # element name to fill the key would be worse than the gap.
        {"id": "ECO-11",
         "statement": "Throwing the quadrat over your shoulder makes the "
                      "placement random.",
         "confronted_by": "s-think"},
        # ⛔ `NOS-04`, NOT `ECO-12`. The belief is about what a large sample
        # can settle, not about ecosystems, and the register allocated it to
        # this lesson by name. Statement byte-identical to the reserved row.
        {"id": "NOS-04",
         "statement": "A large sample is an accurate sample.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B9, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its
    # exclusion list. Every definition below is authored, not lifted.
    #
    # ⚖️ "bias" and "random" are glossed as a PAIR and against each other,
    # because the single commonest thing a student takes out of this lesson is
    # that the two words mean "unfair" and "careless". They do not, and the
    # definitions say what each one actually rules out.
    "vocabulary": [
        {"term": "quadrat",
         "definition": "A square frame of a known size, placed on the ground "
                       "so that what is inside it can be counted.",
         "note": "The size has to suit the organism — a daisy quadrat is no "
                 "use for counting trees."},
        {"term": "random sample",
         "definition": "A sample whose positions were chosen by a process with "
                       "no preferences, such as pairs of random numbers read "
                       "against a numbered grid.",
         "note": "Random means the surveyor did not choose. It does not mean "
                 "haphazard."},
        {"term": "bias",
         "definition": "An error that comes from where you chose to look, so "
                       "every sample is wrong in the same direction.",
         "note": "More samples do not reduce it — they repeat it."},
        {"term": "population estimate",
         "definition": "The mean count per quadrat multiplied by the number of "
                       "quadrat-sized areas in the whole site.",
         "note": "Every population figure you have ever read is one of these."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED. `<img>`, `<figure>` and `<picture>` each appear
    # zero times on this page — grepped — and the foot line names no slot.
    # Every `<svg>` on the page is the nav chevron or a `ks3-mark` tick, cross
    # or arrow, all of it chrome. Declaring a slot would invent a sourcing task
    # in `docs/ks3/diagram-manifest.md`. NOTES-B9 flag 17 is not dropped by
    # this.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b9/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 104), so the segment is MEASURED and not inherited.
        {"type": "quadrat-bench", "id": "survey-it-then-see-the-truth",
         "anchor": "s-bench", "segment": "practical",
         "demand": "investigate",
         "eyebrow": "At the bench · a field you can check your answer against",
         "heading": "Survey it, then see the truth",
         "prompt": "A hundred-square field with daisies in it. The daisies are "
                   "not spread evenly — they never are — and the real total is "
                   "hidden until you have committed to an estimate.",
         # Design's mono line beside the heading (page line 527). `after`
         # carries `{n}`, which `_KIND_HEAD_FROM` turns into the head
         # counter's format; `before` becomes its bespoke zero, so the resting
         # page reads "field unsurveyed" and never a brace.
         "progress": {"before": "field unsurveyed",
                      "after": "{n} quadrats counted"},

         "side": 10,
         # ⛔ THE CLUSTERING MODEL, term for term (page lines 333–341). The
         # daisies peak at row 7, column 2 — the bottom-left — and `richness`
         # is SQUARED, which is what makes a tight cluster rather than a
         # gradient. A gradient would leave every method very nearly right and
         # the lesson with nothing to show. `noise` is the ±3 wobble that stops
         # the field being readable off its own model; `shade_max` is the count
         # at which a square is drawn fully saturated.
         "field": {"centre_row": 7, "centre_col": 2, "reach": 11,
                   "base": 2, "peak": 26, "noise": 6, "shade_max": 34},

         "methods_label": "Where you put the quadrats",
         "methods": METHODS,
         "counts_label": "How many",
         # ⚖️ 3 → 8 → 25, strictly increasing, and 25 is load-bearing: it is
         # the size of the WHOLE corner pool, so the largest sample exhausts it
         # and the biased answer becomes deterministic. That is what makes bias
         # visibly different from chance, and `r_quadrat_bench` refuses a
         # largest sample smaller than the corner pool for exactly this reason.
         "counts": [3, 8, 25],
         # Design writes the labels whole in `COUNTS` ("3 quadrats"). Authored
         # once with the number substituted, so the word "quadrats" is written
         # once and a fourth count would need no new prose.
         "count_label": "{n} quadrats",
         # Design's initial state is `count: 8` (page line 424) — the middle
         # setting, so the first thing a student does is move it in one
         # direction or the other. Authored rather than left to the fallback:
         # the fallback happens to be `counts[1]`, and a bench that opened on
         # the wrong dial because a list was reordered would teach the wrong
         # lesson silently.
         "default_count": 8,

         # THREE figures in this order: the mean, what it scales up to, and
         # the answer — which stays hidden until the student has committed to
         # the other two. The slot is on screen from the start and SAYS
         # "hidden"; a blank one reads as the bench failing to compute it.
         "figures": [{"id": "mean", "label": "Mean per quadrat"},
                     {"id": "estimate", "label": "Estimated total"},
                     {"id": "real", "label": "Real total",
                      "hidden_value": "hidden"}],

         "sample_label": "Take the sample",
         "resample_label": "Survey again",
         "truth_label": "Show the real total",
         # The grid's three states (page line 546). The third is the sentence
         # the whole instrument is built to earn.
         "captions": {
             "unsampled": "one hundred square metres, contents hidden",
             "sampled": "outlined squares are the ones you counted",
             "revealed": "every square revealed — the daisies were never "
                         "spread evenly"},
         "verdicts": VERDICTS,
         "direction": DIRECTION},

        # #s-rules — the band panel, and rail stop 3, mirroring `s-bench`.
        # Design draws it with no class at all: band ground, 3px ink border,
        # `--ks3-r-block`, 34px 32px padding (page line 164) — which is the
        # `rule` type, exactly as payload schema §2 measures it.
        {"type": "rule", "anchor": "s-rules",
         "eyebrow": "The method, and the two ways it fails",
         # ⚖️ The lesson in nine words, and the sentence every other part of
         # the page is evidence for.
         "statement": "More quadrats fixes one problem and not the other.",
         "cards": RULE_CARDS,
         # Design nests the key fact inside this section (page lines 178–181)
         # on the CARD ground with the accent offset shadow. `card`, because
         # the section itself is `band` and band on band is invisible.
         "key_fact": {"ref": "two-failures-two-fixes", "ground": "card"}},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "ECO-11"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside #s-rules on the card ground — Design's own arrangement,
    # measured: `--ks3-card`, 2px ink border, `box-shadow: 5px 5px 0
    # var(--ks3-accent)`. Never amber. Lifted byte-identical from page line 181
    # and identical to payload schema §12's b9-06 entry.
    "key_facts": [
        {"id": "two-failures-two-fixes",
         "text": "Estimate a population by counting in randomly placed "
                 "quadrats and scaling up: mean per quadrat, multiplied by the "
                 "number of quadrat-sized areas in the whole site. Random "
                 "placement removes bias; more quadrats reduces the effect of "
                 "chance. They are different problems and need different "
                 "fixes.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment on Design's page
        # (measured: static markup, no options, no reveal, no button, payload
        # schema §3), so it is a `confrontation` and not a `predict`, it is not
        # a rail stop, and it emits no completion contract.
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "ECO-11",
         "statements": [
             # `ECO-11`. ⚖️ The paragraph's move is the one MRB-225 asks for:
             # it concedes what is true of throwing — it IS unpredictable —
             # and then locates the difference where it actually is. A person
             # throwing AIMS: further on open grass than into brambles, away
             # from the hedge, downhill more easily than up. Every one of those
             # is a preference, and a preference is what random placement
             # exists to remove. The definition it lands on is the operative
             # one and must not be trimmed to the first half: random means
             # chosen by a process with no preferences, not chosen without
             # thinking.
             {"quote": "Throw the quadrat over your shoulder — that makes it "
                       "random.",
              "body": ["It makes it unpredictable, which is not the same "
                       "thing. You throw further on open grass than into "
                       "brambles, you throw away from the hedge because you do "
                       "not want to climb into it, and you throw downhill more "
                       "easily than up. Every one of those is a preference, "
                       "and a preference is exactly what random placement is "
                       "supposed to eliminate. It is also unsafe with a metal "
                       "frame. The real method is dull and works: lay two tape "
                       "measures at right angles to make a grid of "
                       "coordinates, generate pairs of random numbers, and put "
                       "a quadrat wherever each pair lands, whether that spot "
                       "is convenient or not. The word <em>random</em> in "
                       "science means <em>chosen by a process with no "
                       "preferences</em>, not <em>chosen without "
                       "thinking</em> — and a human trying to be random is one "
                       "of the more reliably biased instruments available."]},
             # `NOS-04`. ⚠️ THE TWO SETTINGS NAMED HERE ARE CORRECTED — Design
             # writes "five random quadrats and then thirty" and the bench
             # offers 3, 8 and 25. See "What could not be lifted" 1; the
             # replacement figures are Design's own, from the corner verdict.
             #
             # ⛔ The last sentence is not a footnote. Choosing where to sample
             # after looking at the field is the trap a student falls into
             # having learned everything else on this page correctly, and it is
             # the only place in the key stage it is named.
             {"quote": "We took twenty quadrats, so the answer is accurate.",
              "body": ["Twenty biased quadrats give a confidently wrong "
                       "answer, and taking a hundred would make it no better — "
                       "it would only make the wrong number more stable. "
                       "Sample size and bias are independent problems. Chance "
                       "error, the kind that comes from happening to land on a "
                       "patch, does shrink as you take more samples: the "
                       "estimate wobbles less. Bias does not shrink, because "
                       "every extra sample is drawn the same crooked way, and "
                       "the error does not average out. You can see both on "
                       "the bench above by taking three random quadrats and "
                       "then twenty-five, and then doing the same on the "
                       "flower-rich corner. There is one more trap worth "
                       "naming: choosing where to sample <em>after</em> "
                       "looking at the field is bias even if you use random "
                       "numbers afterwards, because the area you chose was not "
                       "random."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RUNG 1 REPAIRED AT THE DISTRACTOR, RUNG 2 CLEAN
    # AND UNTOUCHED. Design's rung 1 ran 2w against 1 / 1 / 1: the correct
    # answer is strictly the longest and clears the longest distractor by 2.0×,
    # over the 1.4× threshold, so the gate flags it and the build fails. Full
    # working, and the b2-04 precedent it follows, are in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Do the calculation",
            "q": "Ten quadrats of 1 m² give a mean of 6 daisies each. The "
                 "field is 800 m². What is the estimated population?",
            # ⚖️ ALL FOUR NOW READ AS ESTIMATES, WHICH IS WHAT THE QUESTION
            # ASKS FOR. The correct option is Design's, unchanged, because it
            # is the science; the three distractors keep their numbers and
            # their errors exactly and take the correct option's own hedge, so
            # the set is 2 / 2 / 2 / 2 and has no strict maximum. Padding or
            # shortening a numeric answer would be tampering with a
            # calculation — see b2-04's identical note.
            #
            # None of the three is a register belief: they are the three
            # arithmetic errors this calculation invites — report the raw
            # total, report the area, divide by the wrong quadrat size — and
            # each correction names which. Written here, not lifted from the
            # register, because the register supplies none.
            "options": [
                "About 4800",
                "About 60",
                "About 800",
                "About 80",
            ],
            "answer": 0,
            # Byte-identical to Design's three `correction` strings.
            "feedback": {
                1: "That is the total found in the ten quadrats. It needs "
                   "scaling up to the whole field.",
                2: "That is the area of the field in square metres, not a "
                   "number of daisies.",
                3: "That is how many quadrat-sized areas would fit in the "
                   "field if each were 10 m². Each is 1 m², so there are 800 "
                   "of them, each with about 6 daisies.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A group samples 30 quadrats, all along the sunny edge of the "
                 "field where the flowers look best. What is wrong with their "
                 "estimate?",
            # ⚖️ NOTHING WAS TOUCHED AND NOTHING NEEDED TO BE. Correct 11w
            # against 8 / 5 / 9 — gap 2, ratio 1.22, inside both thresholds.
            # The correct option names a fault and says what does not fix it;
            # all three distractors name a fault and say what would. Same
            # subject, same shape, same kind of consequence.
            #
            # ⛔ Option A IS `NOS-04`, in a student's own words, and it is why
            # the misconception above names `s-ladder` as its `elicited_by`.
            # A student who picks A has stated the belief before the page
            # corrects it. Do not rewrite it: the register's statement and this
            # option are the same claim, and this is the only place on the page
            # a student can commit to it.
            "options": [
                "Nothing — 30 quadrats is a large sample",
                "It is biased, and taking more quadrats would not fix it",
                "The quadrats were too small",
                "They should have counted the whole field to check",
            ],
            "answer": 1,
            "feedback": {
                0: "Sample size is not the issue. Thirty samples taken the "
                   "same crooked way give a stable wrong answer.",
                2: "Possibly, but that is not what has gone wrong here. The "
                   "problem is where they were placed.",
                3: "If you could count the whole field you would not be "
                   "sampling. The fix is to place the quadrats at random.",
            }},
        "explain": {
            "title": "Rung 3 · Write the method",
            "q": "Write a method for estimating the number of dandelions on a "
                 "school field, as instructions another class could follow. "
                 "Include how you make the placement random and how you "
                 "calculate the final number.",
            "field_label": "Your method",
            "placeholder": "First, measure the area of the field…",
            # Criterion 3 is `ECO-11` marked as a criterion rather than as
            # prose — "rather than throwing it" — which is what lets the
            # confrontation above stay static and still be assessed.
            "success": [
                "Measures the area of the whole field.",
                "Lays out two tape measures at right angles to make a grid of "
                "coordinates.",
                "Uses random numbers to choose coordinate pairs, and places a "
                "quadrat at each — rather than throwing it.",
                "Counts the dandelions in each quadrat and finds the mean per "
                "quadrat.",
                "Multiplies the mean by the number of quadrat-sized areas in "
                "the field, and says that more quadrats give a more reliable "
                "estimate.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A class wants to test whether daisies grow better in the "
                 "mown half of a field than the unmown half. Explain how the "
                 "survey design differs from simply estimating a total, and "
                 "how they would decide whether any difference they find is "
                 "real.",
            "field_label": "Your answer",
            "placeholder": "They would need to sample both halves…",
            # Criteria 4 and 5 are the `analysis-and-evaluation` half of `ws`:
            # name a confounding factor, and say what would tell you a
            # difference between two means is more than chance.
            "success": [
                "Says both halves must be sampled, using random placement "
                "within each half.",
                "Says the same number of quadrats and the same quadrat size "
                "must be used in both.",
                "Says the comparison is between the two mean counts, not "
                "between two totals of different areas.",
                "Identifies another factor that could differ between the "
                "halves — shade, trampling, slope, drainage — and says it "
                "would confuse the result.",
                "Says a small difference between the means could easily be "
                "chance, and that more quadrats or repeating the survey is how "
                "you find out.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Populations are estimated, not counted. Place quadrats at "
                "random using coordinates from a grid, count what is inside "
                "each one, find the mean, and multiply by the number of "
                "quadrat areas in the whole site. Random placement removes "
                "bias; taking more quadrats reduces the effect of chance. A "
                "biased sample stays wrong however large it is.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B9 flag 16. Checked and left; the working is in the docstring.
    # ⚖️ MRB-225 holds: the layer adds a method for animals that stay still for
    # nobody, and retracts nothing above it. Its last sentence is the lesson's
    # own claim generalised — knowing an assumption is what separates using a
    # method from trusting it — and it is the sentence that makes this a
    # stretch rather than an extra fact.
    "stretch": [
        {"type": "explainer", "id": "counting-things-that-move",
         "text": "Quadrats only work on things that stay still. To estimate a "
                 "population of animals, ecologists use "
                 "capture–mark–recapture: catch some, mark them harmlessly, "
                 "release them, and come back a few days later. If a tenth of "
                 "the animals in the second catch are marked, then the number "
                 "you marked must be about a tenth of the population. It is "
                 "elegant, and it rests on assumptions worth interrogating — "
                 "that the marked animals mixed back in properly, that the "
                 "mark did not make them easier for a predator to spot or more "
                 "wary of traps, that nothing was born, died or moved away in "
                 "between. Trap-shy and trap-happy animals are both real "
                 "problems: a mouse that has once found free food in a live "
                 "trap will often go straight back in. Every one of those "
                 "assumptions is a way the estimate can go wrong, and knowing "
                 "what they are is the difference between using a method and "
                 "trusting it."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination
    # on the page it is printed on (§4.8.1 C).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to plan a survey of your own school grounds?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph (page line 313) and nothing in it is a safety
    # instruction — it is a note about how the field was made and how far the
    # bench can be trusted. Routing it through `safety_note` would print it in
    # the treatment reserved for "never light a candle without an adult", which
    # devalues the safety line. b3-05, b4-01, b7-04 and b8-01 resolve the
    # identical foot line the identical way.
    #
    # ⚑ Its first clause is the unseeded-field behaviour stated to the student,
    # and it is load-bearing: it is the page saying that the field is real
    # ground and not a fixed puzzle, which is why re-running the survey gives a
    # different answer. Its last clause is the honest one — the real total is a
    # luxury no fieldworker has, and the whole lesson is about what you do
    # without it.
    #
    # ⚠️ The one practical-safety line on this page is inside `#s-think` ("It
    # is also unsafe with a metal frame"), where Design put it, as one clause
    # of a paragraph about method. It is not lifted into a callout: §8.10 keeps
    # safety notes small and at the bottom edge, and an INVESTIGATION chassis
    # is not a licence to promote one.
    "convention_note": "The field is generated once when the page loads, with "
                       "the daisies clustered towards one corner as they "
                       "usually are in real ground. Random quadrats are drawn "
                       "without replacement, so a sample never counts the same "
                       "square twice. The real total is the sum of the whole "
                       "grid, which is a luxury no fieldworker has.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is a sampling technique carried out against a known answer,
    # which is `experimental-skills-and-investigations` in its purest form.
    # `analysis-and-evaluation` is the two-failures separation — random against
    # systematic error — and rung 4's last two criteria. `measurement` is rung
    # 1: mean per quadrat, scaled by the number of quadrat areas.
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation",
           "measurement"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
