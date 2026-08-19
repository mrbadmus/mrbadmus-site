"""B10 L3 — How we worked out DNA's structure (INVESTIGATION).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b10/b10-03-how-we-worked-out-dna.dc.html` (584 lines), her
author's notes `docs/ks3/design-reference/b10/NOTES-B10.md` §2 flags 8–12, and the B10
payload schema `docs/ks3/b10-inventory/PAYLOAD-SCHEMA.md` §0, §1, §4, §7, §8, §9,
§10, §11, §12, §13, §14, §15 and §16, under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the three rung-1 distractors rewritten under MRB-177, each recorded below
with its before and after. The three dials, the four evidence cards, the four
people cards, both marked rungs and both self-marked rungs came out of the
page's own `DIALS`, `EVIDENCE`, `PEOPLE`, `RUNGS` and `SELF_RUNGS` arrays via
`tools/extract_design_payload.js`, not off a keyboard. The historical passage in
`support[]` was lifted from the page's `ks3-support` layer in one piece and not a
word of it was retyped — see the section on it below, which is the reason.

── THE TITLE: ONE STRING, NO RECONCILIATION NEEDED ─────────────────────

Design's page and `ks3_data/structure.py` agree character for character, ASCII
apostrophe and all, so `"title"` below is simply both:

    <title>How we worked out DNA's structure · MrBadmusAI KS3</title>   line 12
    breadcrumb, aria-current="page"                                     line 40
    <h1>How we worked out DNA's structure</h1>                          line 76
    structure.py line 165                                               same

⚠️ **No divergence was found and none is recorded here**, because writing down a
reconciliation that never happened is how a phantom becomes permanent. The
shorter form *"How we worked out DNA"* exists in exactly two places, and neither
is a title: the file name `b10-03-how-we-worked-out-dna.dc.html`, which is the
slug, and the contents table of
`docs/ks3/design-reference/b10/README.txt`, which is a short label in a
fixed-width column. Reading a delivery's index as if it were the artefact is
what produced the claim; measuring the page is what settles it, and the b10-02
author reached the same result independently. The dispatch brief and
`ks3_data/b10/__init__.py` have both been corrected by the commander.

── `covers` is the one statutory clause in the key stage that names PEOPLE ─

`KS3.B.INH.02b` reads, in full: *The part played by Watson, Crick, Wilkins and
Franklin in developing the DNA model, and how the evidence settled it.*
(`ks3_data/substatements.py`.) Both halves of that clause are the two halves of
this page — `#s-who` answers *the part played by* with four named cards, and
`#s-bench` answers *how the evidence settled it* by making the student eliminate
eleven of twelve models with four pieces of 1952 evidence.

`INH.02a` — the nesting model of chromosomes, genes and DNA — is b10-02's and is
`touches` here. `build_ks3.validate()` enforces exactly-once ownership, so a
second claim would fail the build rather than quietly double up.

⚑ Because the clause names people, **the history on this page is statutory
content and not enrichment.** Schema §16 flag 9 says so, NOTES §0 says so, and it
is why a passage a later pass might read as "background" must not be trimmed.

── The instrument: elimination, opened at the worst possible model ─────

`#s-bench` is `model-builder`, on `ks3-block ks3-dark ks3-practical` (page line
102), so `practical` is MEASURED from Design's own class attribute rather than
inferred from the kind name — schema §0 rule 2, and contract §4 records that B1
got two of six wrong by inferring it.

⚖️ **`start` IS THE UNIQUE 0-OF-4 ROW AND THAT IS THE TEACHING.** Three strands,
bases outside, any base with any base is Pauling's published model, it is row 12
of schema §4.2's worked matrix, and it is the only one of the twelve that fails
every single test. The bench therefore opens with four red cards and every dial
the student touches can only improve it: elimination as a method, drawn as a
monotone descent. It is an authored opening selection and not runtime state
(schema §0 rule 3's one exception), which is why it gets a key while `model` and
`solved` do not.

⛔ **THE `pauling` CARD IS NOT REDUNDANT AND MUST NOT BE TIDIED.** §4.2 works it
out: it fails only rows 11 and 12, both of which already fail `photo` and
`water`, so it eliminates nothing on its own. Its job is to make the opening
state cost FOUR failures instead of three, and to be the lesson's only worked
example of a serious rival being ruled out — which is `NOS-03`'s confrontation
performed at the bench rather than asserted in prose. NOTES flag 8 asks whether
it is wanted; schema §16 rules it correct and wanted.

⛔ **NO `run_label` AND NO `reset_label`** (schema §4.3). The four cards
re-evaluate live on every dial press; Design draws no run button and no reset
button. B7's `reactant-remover` and `method-breaker` both had one and copying
that pattern across would add a control Design did not draw.

⛔ **NO RUNTIME STATE IS AUTHORED** (schema §0 rule 3). Design's state bag holds
`model` and `solved`; both are the runtime's, and under R5 a key with no read
site fails `ks3_key_audit.py`. `solved` is sticky by construction on Design's own
page (`solved: st.solved || ok`) and that stickiness is what `data-stage-done`
must mirror — it is a wiring fact for the engine pass, not a key for this one.

⚖️ **`label` AND `phrase` ARE BOTH CONTENT AND THEY GENUINELY DIFFER.** `label`
is the button text; `phrase` is the same option's sentence fragment, and the
panel heading is the three phrases joined with ", " (Design's `modelLine`, page
lines 468–470). `Two` versus `Two strands`, `Inside, facing each other` versus
`bases on the inside`, `A with T, C with G` versus `A with T and C with G` — six
of the seven differ, so neither form can be derived from the other. Both are
lifted; the join is the renderer's.

── FOUR rail stops, and the third is a MIRROR (MRB-249) ────────────────

Design draws four (page lines 293–298) and her `isDone()` gives `s-who` the
BENCH's predicate, character for character, one section to the right:

    if (id === 's-bench') return s.solved;
    if (id === 's-who') return s.solved;        // page line 414

`#s-who` is an eyebrow, a display statement, four static people cards and a key
fact: no control, no commitment, no field, no reveal. It is the PAYOFF of the
bench beside it, and it carries no control precisely because the bench has
already taken the student's commitment. That relationship is a MIRROR,
`wireRail`'s `paint()` resolves it at rail level — which is the level Design
computes it at — and `ks3_parity.check_rail_matches_design` gates the built rail
against `docs/ks3/rail-manifest.md`, where this page's row reads
`s-hook s-bench s-who s-ladder | s-who=s-bench`. Shipping three FAILS the build.

⚠️ Payload schema §8's tables are correct as MEASUREMENT and its instruction to
*author three stops and drop the band* is REVERSED at the head of the same
section. Four is what Design drew and four is what ships.

`done_when` is `solved` on both the bench and its mirror, which is Design's own
state name and her own threshold, not a convenient one: two stops read it.

`#s-think` and `#s-keynote` are on no rail, and that is Design's too:
`#s-keynote` asks nothing, and `#s-think` here is static markup — two quotes, two
bodies, no options, no reveal, no button, no `sc-if` — so it is a `confrontation`
and not contract R1's `predict`. Schema §9, measured on all five pages.

── ⊕ MRB-177 LENGTH PARITY — RUNG 1 REPAIRED, RUNG 2 CLEAN ─────────────

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one). The gate flags a
correct option that is strictly the longest AND clears the longest distractor by
≥4 words or by ≥1.4×.

    rung 1  correct 10w vs  5 /  5 /  7  — gap 3, ratio 1.429       ✗ TRIPPED
    rung 1  correct 10w vs 11 / 12 / 12  — not strictly longest     ✓ repaired
    rung 2  correct 13w vs  3 /  6 / 10  — gap 3, ratio 1.300       ✓ as drawn

**Rung 1 tripped the RATIO arm only** — the gap is three words, one short of the
absolute threshold — and it is the construct MRB-177 named: Design's correct
option states a two-branch RULE (*A pairs with T and C pairs with G*) while all
three distractors state a one-clause wrong CONCLUSION with no reason attached.
The correct answer was longer BY CONSTRUCTION and a student could have scored
the rung without reading it.

Each distractor is rewritten as a WRONG RULE in the correct answer's own shape —
what the ratios supposedly showed, and the reason they supposedly showed it —
keeping Design's clause verbatim at the front:

    r1 B  That DNA is a helix
          + ", because its base amounts repeat regularly"          5w → 11w
    r1 C  That there are two strands
          + ", because there are two pairs of bases"               5w → 12w
    r1 D  That the phosphates are on the outside
          + ", because he measured whole molecules"                7w → 12w

**The correct option is unchanged, `answer: 0` is unchanged, Design's option
ORDER is unchanged, and all three of her corrections are byte-identical.** Each
correction still answers exactly the belief its rewritten distractor states,
because every one of Design's three corrections has the same shape — *that came
from <the real source>* — and every rewrite stays an attribution claim about what
a table of chemical amounts can establish:

  * B now says a regular repeat in the AMOUNTS implies a regular SHAPE, and the
    correction's "Chargaff worked with chemical amounts, not images" is that
    inference denied in its own terms.
  * C now infers the strand count from the pair count, and the correction names
    the measured width in the diffraction pattern as where it actually came from.
  * D now claims a whole-molecule chemical analysis locates the parts, and the
    correction hands the phosphate position to Franklin's water work.

⚖️ **The four options now run 10 / 11 / 12 / 12, so the correct answer is the
SHORTEST by one word and there is no tell in either direction.** That was
deliberate, and it is where b9-01's repair landed too: padding the distractors
far past the correct answer trades one tell for its mirror image, which a class
works out just as fast.

⚠️ **Rung 2 is Design's, untouched, and it did not need touching.** Its correct
option is 13 words against a longest distractor of 10 — a gap of 3 and a ratio
of 1.3, under both arms — and the parity falls out of the construct rather than
being imposed on it: all four options name an ACT and three of them name a real
act by real people in a real year, so the wrong answers are wrong about WHO and
WHEN rather than being obviously slight.

── ⚑ RUNG 4 — THE ACTIVE CHECK SCHEMA §16 ASKS FOR, AND ITS RESULT ─────

NOTES flag 10 asks whether a values judgement belongs in a marked rung. Schema
§16 rules it SHIPS, because *"the part played by"* is the statutory clause and
the rung assesses accuracy of attribution rather than values — **and makes that
ruling conditional on the criteria, which this pass is required to verify rather
than assume.** Every criterion must reward a FACT; none may reward arriving at a
particular moral conclusion.

Verified, one at a time, against Design's five:

  1. *Names Franklin specifically, and what her contribution was — the
     diffraction images and the measurements taken from them.*
     **FACT.** Who did what. Marks a name and a contribution.
  2. *Notes that the data was seen without her knowledge or permission.*
     **FACT.** What happened, and it is the fact schema §16 lists as checked and
     the page's own legal line calls not in dispute. It marks the event, not an
     opinion about the event.
  3. *Recognises that Watson and Crick's own contribution — assembling a model
     that fitted everything — was real and worth credit too.*
     **FACT.** This is the criterion that would fail if any did, and it does not:
     it marks the OTHER attribution, and it marks it in the direction that costs
     a student who has read the passage as a morality tale. A student cannot
     satisfy 1, 2 and 3 together while holding either simple stance.
  4. *States a general rule, such as: data should be credited to whoever produced
     it, and used only with their knowledge.*
     **FACT-SHAPED, and this is the one worth stating the reasoning for.** It
     marks the STATING of a rule about practice, and the example given is a
     convention of scientific attribution — the same class of thing as "arrows
     point from eaten to eater". "such as" makes the example a sample and not a
     required answer, and the criterion is met by any defensible rule about using
     other people's data. It rewards articulating a rule, not adopting a verdict.
  5. *Avoids treating the episode as a simple story of heroes and villains —
     acknowledges that the history is contested or that several factors were
     involved.*
     **FACT.** It marks the acknowledgement that the history is contested, which
     is true and is what the page's own legal line and the credit note both say.
     It is a rule about reasoning under disputed evidence, which is exactly where
     schema §16 draws the line.

**Verdict: all five criteria reward a fact or the accuracy of a claim. None
rewards a moral conclusion, and none can be satisfied by a stance alone. All five
ship, verbatim.** The rung marks whether a student can say who did what and what
was published — which is `INH.02b` — and it is deliberately impossible to score
5/5 by taking either side.

⚖️ Note what the question does NOT ask: it does not ask whether the treatment of
Franklin was right. It asks what a fair ACKNOWLEDGEMENT would have said, which is
a question about attribution with a checkable answer.

── THE HISTORY, AND THE TWO SENTENCES IN IT THAT ARE LOAD-BEARING ──────

Schema §16 flag 9 rules the credit note SHIP AS DRAWN with every fact checked.
It is lifted in one piece and two things in it are actively protected here,
because they are the two a later "tidying" pass would break:

⛔ **THE PASSAGE DOES NOT SAY FRANKLIN WAS DENIED THE NOBEL OVER THE CREDIT
DISPUTE, AND IT MUST NEVER BE MADE TO.** She was INELIGIBLE: she died in 1958 and
a Nobel cannot be awarded posthumously. Design's sentence puts the death, the
1962 award and the rule in that order and joins them with a semicolon, which
says exactly that and no more. Schema §16 calls this the single most important
sentence in the passage. **Do not sharpen it into a grievance and do not soften
it into a coincidence.**

⛔ **IT NAMES NO VILLAIN AND IT SAYS HISTORIANS STILL DISAGREE.** The
*"Historians still argue about how much of this was…"* sentence and the
*"What is not in dispute is…"* sentence do opposite and necessary jobs: the first
refuses to settle what cannot be settled, the second refuses to leave unsettled
what is. Both survive; neither may be trimmed as hedging. The page's own legal
line repeats it a third time and is carried in `convention_note`.

⚑ Schema §16 records one observation that is NOT a science point and is Mide's:
`ks3-support` is the *"Need a hand?"* layer, i.e. scaffolding for a stuck student,
and a credit note is neither scaffolding nor stretch. Design drew it there,
MRB-205 says the page wins, so it ships there — under `support_heading`, which is
Design's own eyebrow *"A note on the credit"* and not the fixed label. That
override is exactly the mechanism B6 minted for the same reason: the hard-coded
"Need a hand?" would have offered a student help with the homework above a
passage that is not about their difficulty.

── Misconception ids: GENE-05 and NOS-03, and GENE-06 MUST NOT EXIST ───

⛔ **`GENE-06` IS NOT MINTED HERE OR ANYWHERE.** Schema §12's ⊕ ruling of
18 Aug 2026 makes it a PERMANENT GAP: `docs/ks3/misconception-register.md`'s
`NOS` section, written 17 Aug 2026, already records the second belief on this
page as `NOS-03` and lists `GENE-06` among the numbers that must never be issued.
`NOTES-B10` §4 says otherwise and is superseded — and §12's own standing note is
that a delivery's §4 is an allocation PROPOSAL to be checked against the register,
four times over now.

*"A great discovery is one person's flash of insight"* is a belief about how
knowledge is made, not about genes, so it belongs to the nature-of-science
family. That is the third application of one ruling this repo has already made
twice — `ECO-12` → `NOS-04` (minted 18 Aug by b9-06) and `REACT-18` → `NOS-06`
(reserved) — and `ks3_data/b9/lesson_06_sampling_an_ecosystem.py` is the file
this one follows: an id from another family sitting in a lesson's
`misconceptions` list is normal and already shipped.

**The spare is `GENE-13` and it is NOT claimed.** Two beliefs, two ids. A spare
is never re-pointed and an unclaimed one stays permanently unused, like `DRUG-07`.

⚠️ **Neither the `GENE` prefix row nor `NOS-03`'s entry state is this pass's to
write** — `docs/ks3/*` is the commander's under contract §0, and a sibling agent
is in the register right now. Both statements below are authored in register
voice, byte-identical to Design's own quoted beliefs with her curly quotes
removed (`_quoted()` adds them back at render). No gate resolves an id against
the register file, so the lesson builds either way; what is at risk is the
register's completeness, and the two rows it needs are named in the report.

Both `confronted_by` values resolve against the BUILT page (MRB-244): `s-think`
is the confrontation block's emitted anchor. `GENE-05`'s `elicited_by` is
`s-ladder`, the quiz block's anchor, because rung 2's option A is *"They
discovered DNA"* — the belief in the student's own words, offered as something to
commit to before any correction names it.

⚖️ **`NOS-03` gets no `elicited_by`, and that is measured rather than forgotten.**
Nothing on this page asks a student to commit to the flash-of-insight story.
The hook's four options are about what KIND of evidence could show a shape, and
none of them is about who did the showing; rung 2's four options are all about
what Watson and Crick DID, and none of them offers "one person worked it out
alone" as a choice; rung 4 asks a student to avoid the heroes-and-villains
framing, which confronts the belief rather than eliciting it; and `#s-think` is
static. Absence is legal (MRB-248) and inventing an element name to fill the key
would be worse than the gap — this is `ECO-11`'s case exactly, one file over.

── What could not be lifted byte-identical, and why ────────────────────

**Nothing, apart from the three MRB-177 rung-1 distractors above.** Checked
rather than claimed:

  * No slot code (`b10-02`, `c1-06`, `b6-03`) appears anywhere in Design's prose
    — grepped. The three internal destinations are drawn as end-matter cards with
    their own titles and are carried in `requires` and `references`, so nothing
    of b9-01's `b7-04` problem arises here.
  * No `<a>` appears inside any prose block, so nothing is lost to `rich()`,
    which allows `<em>` and `<strong>` and nothing else. The ONE `<em>` run on
    the page — *structure* in the first think-again body — is kept, because
    `rich()` renders it and the italic is what carries the sentence's contrast
    between discovering DNA and working out its structure.
  * ⚠️ No sequence leak to repair: `year`, `Year` and `half-term` appear zero
    times in Design's bytes, checked rather than assumed. The lesson is full of
    DATES — 1869, 1944, 1950, 1952, 1953, 1958, 1962, "eighty-four years",
    "five years later" — and every one of them is historical content, which the
    rule has never touched.
  * §8.10 checked across every authored string: nothing explains the platform,
    the rail, the bench or the ladder to the student. The one sentence that names
    the instrument — the bench prompt's *"which is what Watson and Crick were
    doing with pieces of cardboard and bent metal"* — describes 1953, not this
    page.

⊖ One resolution the BUILD will make, recorded so it is not read later as a lift
error: Design's *Before this lesson* card reads `Testing the model`, and
`structure.py` titles c1-06 *"Testing the model: does it explain everything?"*.
`requires` carries slugs and `r_endmatter` prints the registry's title, so the
built card will be the longer form. That is the registry being authoritative
about its own titles, it is what every other cross-unit card on the site does,
and no science word is involved.

── Keys this pass authors that a RENDERER must read (contract R5) ──────

Named explicitly rather than left to be discovered, because `model-builder` has
no renderer yet (see the last section). Every one is measured off Design's
`renderVals()` and named by schema §1 and §4:

    dials           three, 3 × 2 × 2 buttons        page lines 306–333
    dials[].phrase  the sentence fragment, joined    page lines 468–470
    start           row 12 of §4.2 — Pauling's       page line 336
    correct         row 5 of §4.2 — the helix        page line 337
    evidence        four cards; `what` always, `why` only on failure
    requires/forbids  §4's declarative form of Design's four predicates
    verdict_tags    the mono tag over the verdict panel
    verdicts        the verdict body, two branches
    progress_suffix the head counter's authored word

── ⚠️ TWO ENGINE-SIDE READS THIS RECORD NEEDS AND DOES NOT HAVE ────────

Both are reported, neither is patched: `build_ks3.py` is the engine pass's file
under contract §0, and that agent is mid-flight in it right now.

1. **`model-builder` is not in `ACTIVITY_KIND_RENDERERS`.** `variation-plotter`
   landed (build_ks3.py L16363) and the other four B10 kinds have not. That is
   EXPECTED mid-flight and it is why this file authors the payload ahead of the
   renderer rather than waiting for it. Nothing here invents a renderer.

2. **`_rule_card()` has no slot for `initials`.** It reads role/label,
   term/name/title, chips, gloss/body/close and examples (L17267–17278). Design
   draws an ordered list with an accent INITIALS BADGE — `RF`, `MW`, `EC`, `WC`
   (page line 158) — and schema §7 records b10-03's card shape as
   `{initials, name, role, body}`. `initials` is authored here because the page
   draws it and the schema names it; three of the four values are derivable from
   the name but `WC` for *Watson and Crick* is not, so dropping the key would
   lose content that cannot be recomputed. Until a slot exists it is a dead key
   and `ks3_key_audit.py B10` will name it. **The badge is `aria-hidden` on
   Design's page, so nothing a screen reader gets is at risk either way** — what
   is at risk is the MRB-245 failure mode, a card rendering a box that looks
   deliberate with a part of it silently missing.

⚑ For Mide's science gate — every NOTES-B10 flag landing on THIS lesson, and what
  was checked against it. Five flags, five checked, **none corrected**:

  * flag 8   **The four evidence cards, and whether the Pauling card is wanted.**
             CHECKED AND KEPT. Schema §16 rules it correct and unusually
             valuable, and §4.2's worked matrix shows why it cannot be dropped as
             redundant: removing it leaves the opening state at three failures
             instead of four and deletes the lesson's only worked example of a
             rival being ruled out. Pauling's January 1953 triple helix with the
             phosphates inside is real, was wrong for the reason the card gives,
             and its publication is what put Watson and Crick back on the
             problem.

  * flag 9   **The credit note.** CHECKED AND SHIPPED AS DRAWN, and the two
             sentences that must not move are pinned in their own section above.
             Every fact in it is right: Gosling took Photo 51 under Franklin at
             King's; Wilkins showed it to Watson without her knowledge; her
             unpublished MRC report reached Crick through the MRC Biophysics
             Committee; the 1953 paper acknowledged only having been "stimulated
             by" unpublished King's results; she died in 1958 aged 37; the prize
             was 1962 and cannot be posthumous.

  * flag 10  **A values judgement in a marked rung.** CHECKED CRITERION BY
             CRITERION, all five ship. The full working is in its own section
             above; the short form is that every criterion marks a fact or the
             accuracy of a claim, and criterion 3 in particular marks the
             attribution that costs a student who has read the episode as a
             morality tale.

  * flag 11  **Miescher 1869, and Avery, MacLeod and McCarty 1944.** CHECKED AND
             LEFT. Miescher isolated nuclein from the pus on used surgical
             bandages at Tübingen in 1869; Avery, MacLeod and McCarty published
             the transforming-principle work in 1944, and the page's framing —
             that it was surprising because most biochemists expected protein —
             is the right one. Both are named once, in prose, at the depth a KS3
             student can hold, and rung 2's corrections are what make them
             examinable.

  * flag 12  **Meselson and Stahl, and the closing sentence paraphrased rather
             than quoted.** CHECKED AND LEFT. Meselson and Stahl published in
             1958, five years after 1953, and semi-conservative replication is
             what they showed. The paraphrase is the better choice at this age:
             the original sentence's force is entirely in its understatement, and
             a direct quotation printed cold would need a gloss longer than
             itself. Design's paraphrase keeps the understatement and says it is
             understatement, which is what a student needs to see.

  * flag 19  **No diagrams anywhere in B10, and Photo 51 is one of the two
             candidates.** MEASURED on this page rather than assumed: `<img>`,
             `<figure>` and `<picture>` each appear ZERO times, and every `<svg>`
             is the nav chevron, a rail tick or a `ks3-mark`. `figures` is
             therefore empty by §4.10 and §11. ⚠️ **Photo 51 is a specific
             historical photograph with rights attached.** If it is wanted that
             is a LICENSING decision and Mide's, and it cannot be met by
             commissioning something that looks similar — a drawing of an X-ray
             diffraction pattern is not Photo 51 and the lesson's claim is about
             that image. The flag is NOT dropped by the empty `figures`, and
             declaring a slot the page never references would invent a sourcing
             task in `docs/ks3/diagram-manifest.md` that nobody can discharge.

── MRB-225, checked across the whole lesson: NO body sentence is retracted ─

Traced the claim the lesson makes seven times: *the structure was deduced from
other people's measurements, by eliminating what could not fit.* The hook's
reveal ("the pattern is not a picture of the molecule… worked backwards"), the
bench prompt ("four pieces of evidence that each rule something out"), the
solved verdict ("the evidence did not show you the answer — it eliminated
everything else"), the Watson-and-Crick card ("model building is a legitimate
method, and it was the right one here"), `#s-think`'s second body, rung 2's
correct option and the key note all say the same thing at the same size. The
stretch layer adds the replication argument and Meselson and Stahl, and retracts
nothing. The legal line narrows the BENCH — three decisions and four tests out of
a two-year argument — and narrows nothing that was taught as settled.

⚠️ **THIS INSTRUMENT IS ON INK.** `.ks3-dark p` is (0,1,1) and beats a bare
component class at (0,1,0); every B10 colour rule has to be written at (0,2,0)
under `.ks3-dark …` and `ks3_parity.check_dark_text_specificity()` resolves it on
the real cascade. Recorded here because this payload is what feeds it, and
because the failing-card text is `--ks3-alert` on the dark panel — amber on a
WRONG IDEA, which is the one place §8 reserves it for, and never on the student.
"""

from ._base_pairs import base_pairs



# ── the three dials (page lines 306–333, and `modelLine` at 468–470) ─────
#
# `label` is the button text and `phrase` is the same option's sentence
# fragment; six of the seven pairs genuinely differ, so both are content and
# neither can be derived from the other (schema §4). The panel heading is the
# three phrases joined with ", " — three dials, one authored fragment each, and
# twelve headings that cannot disagree with the dials above them.
#
# ⚠️ THE OPTION IDS ARE FIXED. `requires`, `forbids`, `start` and `correct` all
# join on them, and §4.2's twelve-row matrix is worked in these exact names.
DIALS = [
    {"id": "strands", "name": "How many strands",
     "options": [
         {"id": "1", "label": "One", "phrase": "A single strand"},
         {"id": "2", "label": "Two", "phrase": "Two strands"},
         {"id": "3", "label": "Three", "phrase": "Three strands"},
     ]},
    {"id": "bases", "name": "Where the bases sit",
     "options": [
         {"id": "in", "label": "Inside, facing each other",
          "phrase": "bases on the inside"},
         {"id": "out", "label": "Outside, facing the water",
          "phrase": "bases on the outside"},
     ]},
    {"id": "pairing", "name": "How the bases pair",
     "options": [
         {"id": "specific", "label": "A with T, C with G",
          "phrase": "A with T and C with G"},
         {"id": "any", "label": "Any base with any base",
          "phrase": "any base with any base"},
     ]},
]

# ── the four evidence cards (page lines 339–354) ─────────────────────────
#
# `what` renders always; `why` renders in alert colour ONLY when the card
# fails, and it is the ELIMINATION TEXT — the line that names what the evidence
# rules out. All eight strings are Design's, and schema §4.1 quotes the four
# `why` texts verbatim because they are the ones a retype would damage.
#
# `requires` / `forbids` are §4's declarative form of Design's four JS
# predicates: a card passes when every `requires` pair matches AND the `forbids`
# map is not matched in full. Three are a single equality; `pauling` is the
# negated conjunction, and it is the only one of the four that needs `forbids`.
EVIDENCE = [
    {"id": "photo", "name": "Photo 51 · Franklin and Gosling, 1952",
     "what": "An X-ray diffraction image of DNA fibres. The cross-shaped "
             "pattern of spots is the signature of a helix, and the spacing of "
             "the spots gives its width and the distance per turn.",
     "why": "The measured width does not fit this. A single strand is too "
            "narrow and three strands are too wide — the pattern says two.",
     "requires": {"strands": "2"}},
    {"id": "water", "name": "Franklin’s water measurements",
     "what": "DNA takes up a great deal of water, which means its "
             "water-attracting parts — the phosphate groups — must be on the "
             "outside of the molecule, in contact with it.",
     "why": "If the bases are on the outside then the phosphates are on the "
            "inside, which contradicts the water measurements — and the "
            "negative phosphates would repel each other.",
     "requires": {"bases": "in"}},
    {"id": "chargaff", "name": "Chargaff’s ratios, 1950",
     "what": "In DNA from any organism, the amount of A always equals the "
             "amount of T, and the amount of C always equals the amount of G — "
             "while the ratio of A to C varies from species to species.",
     "why": "If any base could pair with any other there would be no reason "
            "for A and T to come in equal amounts in every organism ever "
            "measured.",
     "requires": {"pairing": "specific"}},
    # ⛔ NOT REDUNDANT. §4.2: it fails only rows 11 and 12, both of which already
    # fail `photo` and `water`, so it eliminates nothing on its own — and that
    # is not a reason to cut it. It is what makes the opening state cost four
    # failures instead of three, and it is the lesson's only worked example of a
    # serious rival being ruled out. NOTES flag 8; schema §16 rules it wanted.
    {"id": "pauling", "name": "Pauling’s triple helix, early 1953",
     "what": "The most respected chemist alive published a model with three "
             "strands and the bases facing outwards. It was wrong, and seeing "
             "why it was wrong narrowed the field for everyone else.",
     "why": "This is Pauling’s model, and it has already been ruled out. Its "
            "phosphates were crowded into the centre where their negative "
            "charges would push the molecule apart.",
     "forbids": {"strands": "3", "bases": "out"}},
]

# ── the four people cards (page lines 156–165) ───────────────────────────
#
# Design's ordered list with an accent initials badge. `role` is the mono accent
# line and maps to the slot `_rule_card()` reads for it; `name` and `body` are
# its `term` and `gloss` slots under their own words.
#
# ⚠️ `initials` HAS NO SLOT IN `_rule_card()` YET — see the docstring's
# engine-side section. It is authored because Design draws the badge and schema
# §7 names the shape, and because `WC` for *Watson and Crick* cannot be
# recomputed from the name.
#
# ⚖️ The FOURTH card is the one a scheme of work usually gets wrong, and its
# last clause is why it is here: "model building is a legitimate method, and it
# was the right one here". The lesson spends four sections establishing that
# Watson and Crick did no experiments, and without this sentence a student
# leaves believing that means they did nothing. That is the failure mode of
# teaching this episode honestly, and it is answered on the page rather than
# left to the teacher.
PEOPLE = [
    {"initials": "RF", "name": "Rosalind Franklin",
     "role": "King’s College London · X-ray crystallography",
     "body": "Produced the diffraction images, including Photo 51 with her "
             "student Raymond Gosling, and calculated from them that the "
             "molecule was a helix of a particular width with the phosphates "
             "on the outside. Hers is the evidence the model had to fit."},
    {"initials": "MW", "name": "Maurice Wilkins",
     "role": "King’s College London · X-ray crystallography",
     "body": "Began the X-ray work on DNA and continued it alongside Franklin, "
             "in a working relationship that was difficult from the start. He "
             "showed Photo 51 to Watson."},
    {"initials": "EC", "name": "Erwin Chargaff",
     "role": "Columbia University · biochemistry",
     "body": "Measured the amounts of the four bases in DNA from many species "
             "and found the equalities that carry his name — without proposing "
             "what they meant. The pairing rule was sitting in his tables for "
             "three years."},
    {"initials": "WC", "name": "Watson and Crick",
     "role": "Cambridge · model building",
     "body": "Built physical models and tested them against everyone else’s "
             "measurements until one fitted all of them. They did no "
             "experiments on DNA themselves, which is not a criticism — model "
             "building is a legitimate method, and it was the right one here."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # ⚠️ Slug AND title both match `ks3_data/structure.py` line 165 character
    # for character, and both match Design's page — one string, not two. See the
    # docstring for where the phantom divergence came from.
    "slug":        "how-we-worked-out-dna",
    "title":       "How we worked out DNA's structure",
    "discipline":  "biology",
    "unit":        "inheritance-and-dna",
    "family":      "INVESTIGATION",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.INH.02b` — the part played by Watson, Crick, Wilkins and Franklin,
    # and how the evidence settled it — owned whole. `#s-who` discharges the
    # first half and `#s-bench` the second. `02a` is b10-02's; see the docstring.
    "covers":      ["KS3.B.INH.02b"],
    # Named, used, and owned elsewhere. `INH.02a` is b10-02's nesting model —
    # this page says "DNA", "bases", "strands" and "helix" and re-teaches none
    # of them. `INH.04` is b10-01's: rung 1 and the whole `chargaff` card turn on
    # reading a table of measured amounts, which is where that skill was built.
    "touches":     ["KS3.B.INH.02a", "KS3.B.INH.04"],
    "beyond_statutory": False,
    # `genes-and-evolution` is at `develop`: b10-01 and b10-02 opened it and
    # this is where the molecule stops being a diagram and becomes something
    # that had to be established. `evidence-and-explanation` is at `secure` —
    # c1-06 tested a model, b9-06 separated bias from sample size, and this
    # lesson runs the whole loop on a real episode with the answer known.
    "threads":     [{"id": "genes-and-evolution", "level": 2},
                    {"id": "evidence-and-explanation", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" card, in her order. `requires` resolves
    # across the whole key stage — unlike `references`, which resolves against
    # the current unit — so `testing-the-model` needs no unit qualifier.
    # ⊖ The built card will print c1-06's registry title, which is longer than
    # Design's link text. See the docstring's last lift note.
    "requires":    ["chromosomes-genes-and-dna", "testing-the-model"],
    "assumes":     [],
    # Design's "Connects to" card, in her order.
    #
    # ⚠️ `substance-misuse-and-decisions` MUST carry its unit. A bare slug in
    # `references` is resolved against the CURRENT unit, so the bare form would
    # build a link to
    # /ks3/biology/inheritance-and-dna/substance-misuse-and-decisions.html,
    # which is not a page. `check_internal_links` catches it; the dict form is
    # what b8-01 and b9-01 use for the same reason.
    #
    # ⚖️ The b6-03 edge looks odd on a DNA page and it is Design's, deliberately:
    # b6-03 is the lesson about testing a claim you have been handed, and this
    # is the lesson where a claim about who discovered what is tested against
    # what was actually published. Same skill, different subject matter.
    "references":  ["passing-it-on-heredity",
                    {"unit": "B6", "lesson": "substance-misuse-and-decisions"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "The structure of DNA in detail, the history of the model as "
                   "an example of how science works, and DNA replication.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Nobody has ever seen a DNA molecule. Its structure was "
                    "deduced from a photograph of scattered X-rays, a table of "
                    "chemical ratios, and a set of metal models built on a "
                    "bench in Cambridge.",

    # ── the progress rail (§8) ──────────────────────────────────────────────
    # FOUR stops, as Design draws them (page lines 293–298). `s-who` is the
    # third: no control of its own, so it mirrors `s-bench` and ticks on the
    # bench's predicate — Design's own `isDone()`, page line 414. `short` and
    # `label` are her `RAIL_SHORT` and `RAIL` strings. Shipping three fails
    # `check_rail_matches_design`; see the docstring.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Too small to see",
         "done_when": "committed"},
        # Design's own threshold and her own state name: `s.solved`, sticky by
        # construction (`solved: st.solved || ok`). Monotonic by design as well
        # as by MRB-208 — a student who reaches the double helix and then breaks
        # the model to explore has still reached it.
        {"anchor": "s-bench", "short": "BENCH", "label": "Build the model",
         "done_when": "solved"},
        {"anchor": "s-who", "short": "WHO", "label": "Who did what",
         "mirrors": "s-bench", "done_when": "solved"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key, and Design's own
    # reveal is gated on `hookChoice !== null` rather than on a right answer.
    # B is the correct one and the reveal says so at once; the hook is not a
    # trick, it is the claim the bench then has to earn in eliminations.
    #
    # ⚖️ None of the four is `GENE-05` or `NOS-03`, which is why neither
    # misconception names `s-hook` as its `elicited_by`. All four are answers to
    # "what could show a shape too small to see", and the three wrong ones are
    # the three a class actually offers: a better microscope, a colour test, and
    # a computer.
    "phenomenon": {
        "kind": "narrative",
        "title": "A molecule far too small to see, worked out in 1953.",
        "prompt": "DNA is a hundred thousand times thinner than a hair. No "
                  "microscope of the 1950s could resolve it, and no microscope "
                  "today can show you the shape of a single molecule directly. "
                  "Yet by April 1953 the structure was published, and it was "
                  "right.",
        "commit": "What kind of evidence could possibly show the shape?",
        "options": [
            "A very powerful light microscope",
            "The pattern X-rays make when they scatter off it",
            "A chemical test that changes colour",
            "A computer simulation",
        ],
        "reveal": "X-ray diffraction. Fire X-rays at a crystal or fibre and "
                  "they scatter off the atoms in a pattern; the pattern is not "
                  "a picture of the molecule, but its geometry can be worked "
                  "backwards to the arrangement that produced it. Rosalind "
                  "Franklin was one of the best in the world at it, and the "
                  "image known as Photo 51 is the reason this lesson exists.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Schema §12's pre-allocation as CORRECTED by its ⊕ ruling of 18 Aug 2026,
    # and the two beliefs Design's `#s-think` quotes. Both statements are her
    # own bytes, page lines 176 and 181, in register voice.
    #
    # ⛔ `GENE-06` MUST NOT BE MINTED by any pass. It is a PERMANENT GAP and the
    # second belief is `NOS-03` — the third application of a ruling this repo
    # made for `ECO-12`→`NOS-04` and `REACT-18`→`NOS-06`. `NOTES-B10` §4 says
    # otherwise and is superseded. See the docstring.
    #
    # ⛔ The spare `GENE-13` is NOT claimed. Two beliefs, two ids.
    #
    # ⚠️ The register rows are not written here — `docs/ks3/*` is the
    # commander's under contract §0 and a sibling agent is in that file. The two
    # rows it needs are named in the report.
    "misconceptions": [
        # `elicited_by` is `s-ladder`: rung 2's option A is "They discovered
        # DNA", the belief word for word, offered as something to commit to
        # before the correction names it (MRB-248: a value that is present must
        # be true).
        {"id": "GENE-05",
         "statement": "Watson and Crick discovered DNA.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        # ⛔ `NOS-03`, NOT `GENE-06`. The belief is about how knowledge is made,
        # not about genes, and the register allocated it to this lesson by name
        # on 17 Aug 2026.
        #
        # No `elicited_by`, and it is measured rather than forgotten: nothing on
        # this page offers the flash-of-insight story as a choice. The hook asks
        # what kind of evidence could show a shape; rung 2's four options are
        # all about what Watson and Crick DID; rung 4 confronts the framing
        # rather than eliciting it; `#s-think` is static. Absence is legal and
        # inventing an element name to fill the key would be worse than the gap.
        {"id": "NOS-03",
         "statement": "A great discovery is one person's flash of insight.",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B10, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its
    # exclusion list. Every definition below is authored, not lifted.
    #
    # ⚖️ "X-ray diffraction" and "model" are glossed as a PAIR and against each
    # other, because the single commonest thing a student takes out of this
    # lesson is that somebody photographed DNA. Nobody did. One entry says what
    # the image actually is; the other says what was built from it.
    "vocabulary": [
        {"term": "double helix",
         "definition": "Two strands wound round each other in a spiral, which "
                       "is the shape of a DNA molecule.",
         "note": "Two strands, not one and not three. The width in the X-ray "
                 "pattern is what settled it."},
        {"term": "base",
         "definition": "One of the four chemical units — A, T, C and G — whose "
                       "order along a DNA strand carries the information.",
         "note": "They sit on the inside of the helix, facing each other."},
        {"term": "base pairing",
         "definition": "The rule that A always pairs with T and C always pairs "
                       "with G across the two strands.",
         "note": "Chargaff measured the equal amounts; the pairing rule is "
                 "what explains them."},
        {"term": "X-ray diffraction",
         "definition": "Firing X-rays at a substance and reading the pattern "
                       "they scatter into, which can be worked backwards to "
                       "the arrangement of atoms that produced it.",
         "note": "Not a photograph of the molecule. Photo 51 is a pattern of "
                 "spots, not a picture."},
        {"term": "crystallography",
         "definition": "The science of working out how atoms are arranged in a "
                       "solid from the way it scatters X-rays.",
         "note": "Franklin's field, and one of the hardest kinds of "
                 "measurement there is."},
        {"term": "model",
         "definition": "A representation of something built so it can be "
                       "tested against evidence and thrown away if it fails.",
         "note": "Watson and Crick built theirs out of metal. Pauling's was "
                 "wrong, and that was still useful."},
    ],

    # ── figures (§11) ───────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED. `<img>`, `<figure>` and `<picture>` each appear
    # zero times on this page — grepped — and every `<svg>` is chrome.
    # NOTES-B10 flag 19 asks for Photo 51 and is NOT dropped by this: it is a
    # specific historical photograph with rights attached, so it is a LICENSING
    # decision and Mide's, and it cannot be met by drawing something similar.
    # Declaring a slot the page never references would invent a sourcing task in
    # `docs/ks3/diagram-manifest.md` that nobody can discharge.
    # ⊕ DRAWN, 18 Aug 2026 — Mide's diagram ruling, and this lesson is the one
    # in B10 that earns one. `model-builder` beside it is a REASONING instrument:
    # the student sets dials, the evidence cards rule models out, and they argue
    # their way to two strands with the bases paired inside without ever seeing
    # it. The KEY FACT is then a purely structural claim, and a structural claim
    # with nothing drawn is a sentence to be memorised.
    #
    # It also teaches the REASON for the pairing rule, which is normally met as
    # an arbitrary fact. A and G are the big bases, C and T the small ones, so
    # big-with-small is the only pairing that keeps every rung the same length —
    # and a molecule whose rungs varied could not have the constant width
    # Franklin measured off the diffraction pattern, which is on this same page.
    # `_base_pairs` RAISES on a rung that pairs two bases of the same size, so
    # the drawing cannot quietly contradict that.
    #
    # ⚠️ This is NOT Photo 51 and does not stand in for it. Schema §11: Photo 51
    # is a specific historical photograph with rights attached, that is Mide's
    # licensing decision, and it explicitly cannot be met by drawing something
    # similar. The flag stays open.
    "figures": [
        base_pairs(
            "b10-base-pairs",
            title="How the bases pair across the two strands of DNA, and the "
                  "same ladder twisted",
            # ⊕ MRB-254 — REWRITTEN FOR WHAT IS NOW DRAWN. The old text said
            # the constant width was "marked down the right-hand side", which
            # was an accurate description of a mark that was measuring the
            # wrong axis, and it stopped at the ladder. Both halves changed.
            desc="On the left, two backbones running down the sides with five "
                 "rungs between them. Each rung is one base from the left "
                 "strand meeting one from the right: A with T, T with A, C "
                 "with G, G with C, and A with T again. A and G are drawn "
                 "wide and C and T narrow, because A and G are the big bases "
                 "and C and T the small ones. Every rung pairs a big base "
                 "with a small one, so every rung comes to the same width. "
                 "That width is measured twice, by a dimension line drawn "
                 "straight across the first rung and another drawn straight "
                 "across the last — both the same length, both starting and "
                 "finishing at the same two points. On the right the same "
                 "ladder is drawn again with the twist put back into it: the "
                 "two backbones wind round each other as a double helix with "
                 "rungs running between them all the way down, and two dashed "
                 "lines mark "
                 "the widest points of the spiral with a third dimension line "
                 "measured across them. That third measurement is the same "
                 "length as the two on the ladder, because the width of the "
                 "twisted molecule is its diameter and the ladder is what "
                 "sets it. It is the constant width measured from the "
                 "diffraction images on this page.",
            caption="The reason is width. Every rung is one big and one "
                    "small and every rung comes out the same length. Two "
                    "big bases would bulge; two small ones would pinch — and "
                    "twisting the ladder up into the shape you already know "
                    "does not change it, because that width has become the "
                    "width of the spiral.",
            rungs=[("A", "T"), ("T", "A"), ("C", "G"), ("G", "C"), ("A", "T")]),
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b10/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 102), so the segment is MEASURED and not inherited.
        #
        # Payload keys follow docs/ks3/b10-inventory/PAYLOAD-SCHEMA.md §4. The
        # read sites are listed in the docstring; `model`, `solved`, `run_label`
        # and `reset_label` are all deliberately absent and each has its own
        # reason there.
        {"type": "model-builder", "id": "build-a-model-that-fits-all-of-it",
         "anchor": "s-bench", "segment": "practical",
         "demand": "investigate",
         "eyebrow": "At the bench · the evidence available in 1952",
         "heading": "Build a model that fits all of it",
         "prompt": "Three decisions to make, and four pieces of evidence that "
                   "each rule something out. Exactly one combination survives "
                   "all four — which is what Watson and Crick were doing with "
                   "pieces of cardboard and bent metal.",

         "dials": DIALS,
         # ⚖️ ROW 12 OF §4.2 — the unique 0-of-4 combination, and Pauling's own
         # published model. The bench opens with every card red and every dial
         # the student touches can only improve it. An authored opening
         # selection is content, not runtime state (§0 rule 3's one exception).
         "start":   {"strands": "3", "bases": "out", "pairing": "any"},
         # ⚖️ ROW 5 OF §4.2 — the unique 4-of-4, and the structure published in
         # April 1953. Read by the renderer to set `solved`; authored here so
         # the claim "exactly one combination survives" is data rather than a
         # sentence that could go out of step with the evidence predicates.
         "correct": {"strands": "2", "bases": "in", "pairing": "specific"},
         "evidence": EVIDENCE,

         # The mono tag over the verdict panel. `{n}` is the number of failing
         # cards; Design's expression is
         # `(EVIDENCE.length - passes) + ' test' + (…===1 ? '' : 's') + ' still
         # failing'`, so the singular and the plural are two authored strings
         # rather than a suffix the renderer pluralises. Four failing is the
         # opening state, so both branches are on screen in ordinary use.
         "verdict_tags": {"pass": "Every test passed",
                          "fail_one": "{n} test still failing",
                          "fail_many": "{n} tests still failing"},
         # ⚖️ THE SOLVED VERDICT'S LAST SENTENCE IS THE LESSON. "The evidence
         # did not show you the answer — it eliminated everything else" is the
         # claim `NOS-03` is confronted with, stated at the moment the student
         # has just done it. It is the one string on the bench that must never
         # be shortened for fit.
         "verdicts": {
             "pass": "Two strands, bases paired on the inside, A with T and C "
                     "with G. This is the only combination on the bench that "
                     "survives all four pieces of evidence, and it is the "
                     "structure published in April 1953. Notice what just "
                     "happened: the evidence did not show you the answer — it "
                     "eliminated everything else.",
             "fail": "Each failing test is telling you which decision to "
                     "change, and none of them requires you to know the "
                     "answer in advance — which is exactly the position "
                     "everyone was in during 1952.",
         },
         # The head counter's authored word. Design's `benchProgress` is
         # `passes + ' of ' + EVIDENCE.length + ' tests passed'`, so the
         # denominator is a fact about the payload and only the word is authored
         # (§1, and §4's shape).
         "progress_suffix": "tests passed"},

        # #s-who — the band panel, and the section that discharges the first
        # half of KS3.B.INH.02b. Rail stop 3, mirroring `s-bench`.
        #
        # ⚠️ `initials` has no slot in `_rule_card()` yet — reported, not
        # patched; `build_ks3.py` is the engine pass's file. See the docstring.
        {"type": "rule", "anchor": "s-who",
         "eyebrow": "Who did what",
         "statement": "Four names, two laboratories, one structure.",

         "cards": PEOPLE,

         # Design nests the key fact inside this section (page lines 168–171) on
         # the CARD ground with the 5px accent offset shadow. `card`, because
         # the section itself is `--ks3-band` and band on band is invisible —
         # the same arrangement and the same reason as b7-01's, b8-01's and
         # b9-01's. Design draws no closing paragraph here, so there is no
         # `close` key and the r_rule ordering question b9-01 reported does not
         # arise on this page.
         "key_fact": {"ref": "dna-is-a-double-helix", "ground": "card"}},

        # The drawing of the KEY FACT immediately above it. Placed AFTER `#s-who`
        # rather than inside it: `r_rule` renders a statement, cards, the nested
        # key fact and a close, in that order, and a figure is none of those.
        # `figure` is an existing registered block type (§10.2), so this renders
        # a component rather than inventing one.
        {"type": "figure", "ref": "b10-base-pairs", "anchor": "s-pairs"},

        {"type": "misconception", "id": "who-discovered-what",
         "anchor": "s-think", "targets": "GENE-05"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§13) ──────────────────────────────────────────────
    # Nested inside #s-who on the card ground — Design's own arrangement,
    # measured: `--ks3-card`, 2px ink border, `box-shadow: 5px 5px 0
    # var(--ks3-accent)`. Never amber. Lifted byte-identical from page line 171
    # and identical to payload schema §13's b10-03 entry.
    #
    # ⚖️ It names all four people and what each contributed, in one sentence,
    # because that IS the statutory clause. A later pass trimming it for length
    # would be trimming `INH.02b`.
    "key_facts": [
        {"id": "dna-is-a-double-helix",
         "text": "DNA is a double helix: two strands twisted round each other, "
                 "with the bases paired on the inside — A always with T, C "
                 "always with G. The structure was deduced in 1953 from X-ray "
                 "diffraction images taken by Rosalind Franklin and Maurice "
                 "Wilkins, and from Erwin Chargaff's base ratios, by James "
                 "Watson and Francis Crick.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment on Design's page
        # (measured: static markup, no options, no reveal, no button, no
        # `sc-if`, schema §9), so it is a `confrontation` and not a `predict`,
        # it is not a rail stop, and it emits no completion contract.
        {"id": "who-discovered-what",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "GENE-05",
         "statements": [
             # GENE-05. The `<em>` run on *structure* is kept — `rich()` renders
             # it — because the contrast between discovering DNA and working out
             # its structure is the whole paragraph and the italic is how it is
             # made. `_quoted()` adds Design's curly quotes at render, so the
             # quote is authored bare.
             {"quote": "Watson and Crick discovered DNA.",
              "body": ["DNA was discovered in 1869 by Friedrich Miescher, who "
                       "isolated it from the pus on used surgical bandages and "
                       "called it nuclein — eighty-four years before 1953. By "
                       "the 1940s Avery, MacLeod and McCarty had shown it was "
                       "the material carrying inherited information, which was "
                       "the genuinely surprising result, since most "
                       "biochemists had assumed the genetic material must be "
                       "protein. What Watson and Crick worked out was the "
                       "<em>structure</em>, and even that was model-building "
                       "from other people's measurements: they did no "
                       "experiments on DNA themselves. Getting this right is "
                       "not pedantry about credit. It is the difference "
                       "between imagining science as a series of individual "
                       "discoveries and understanding it as what it is — a "
                       "slow accumulation where the person who assembles the "
                       "final piece is standing on twenty years of other "
                       "people's work."]},
             # NOS-03, and the reason the bench is upstream of it in the
             # document: "Look at what 1953 actually required" is a real
             # instruction about an argument the student has just run, four
             # cards at a time.
             #
             # ⚖️ "Five laboratories, three countries, two decades" is the
             # sentence the whole misconception turns on, and the last clause is
             # what makes it a correction of a PICTURE rather than of a fact:
             # mostly it looks like checking whether your idea is consistent
             # with someone else's data. Nothing in the paragraph names a
             # villain, and it must not be edited into one.
             {"quote": "A great discovery is one person's flash of insight.",
              "body": ["Look at what 1953 actually required. Franklin and "
                       "Wilkins produced the diffraction images at King's "
                       "College London and Franklin calculated the "
                       "measurements from them. Chargaff, in New York, had "
                       "published the base ratios years earlier without seeing "
                       "what they meant. Linus Pauling in California published "
                       "a triple-helix model that was wrong, which mattered, "
                       "because ruling out a serious rival narrows the field. "
                       "Watson and Crick built physical models in Cambridge "
                       "and tested them against everyone else's numbers until "
                       "one fitted. Five laboratories, three countries, two "
                       "decades. The flash-of-insight story survives because "
                       "it is easier to tell, and it gives students a false "
                       "picture of what doing science looks like: mostly it "
                       "looks like checking whether your idea is consistent "
                       "with someone else's data."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RUNG 1 REPAIRED, RUNG 2 CLEAN AS DRAWN. rung 1
    # correct 10w against 5 / 5 / 7 as delivered, which tripped the RATIO arm
    # (1.429 against a 1.4 threshold), and 11 / 12 / 12 after each distractor is
    # rewritten as a wrong RULE in the correct answer's own shape; rung 2
    # correct 13w against 3 / 6 / 10, gap 3 and ratio 1.3, under both arms. The
    # correct options, both `answer` indices, Design's option ORDER and every
    # one of her six corrections are byte-identical. Full working, with the
    # before and after of all three rewrites, in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · What the evidence showed",
            "q": "What did Chargaff’s ratios contribute to the model?",
            # ⊕ MRB-177, 18 Aug 2026. Options 1, 2 and 3 rewritten as wrong
            # RULES in the correct answer's shape — what the ratios supposedly
            # showed, and the reason they supposedly showed it. Option 0 and
            # `answer` are Design's, unchanged. Each rewrite keeps Design's own
            # clause verbatim at the front.
            #
            #   A  correct, Design's, unchanged
            #   B  authored belief: a regular repeat in the AMOUNTS reveals the
            #      SHAPE — i.e. chemistry can do an image's job
            #   C  authored belief: the number of pairs gives the number of
            #      strands
            #   D  authored belief: a whole-molecule chemical analysis locates
            #      the parts of the molecule
            "options": [
                # 10w — Design's, unchanged.
                "That A pairs with T and C pairs with G",
                # 11w. Was "That DNA is a helix" (5w). The added clause is the
                # amounts-give-shape inference, which the correction's
                # "Chargaff worked with chemical amounts, not images" denies in
                # its own terms.
                "That DNA is a helix, because its base amounts repeat "
                "regularly",
                # 12w. Was "That there are two strands" (5w). Two pairs of
                # bases therefore two strands is the non sequitur; the
                # correction hands the strand count back to the measured width.
                "That there are two strands, because there are two pairs of "
                "bases",
                # 12w. Was "That the phosphates are on the outside" (7w). The
                # consequence the belief licenses: that measuring the whole
                # molecule chemically tells you where its parts sit.
                "That the phosphates are on the outside, because he measured "
                "whole molecules",
            ],
            "answer": 0,
            # All three unchanged from Design, and each still answers exactly
            # the belief its rewritten distractor states — which is the test of
            # whether the rewrite changed what the question measures.
            "feedback": {
                1: "That came from the X-ray diffraction pattern. Chargaff "
                   "worked with chemical amounts, not images.",
                2: "The number of strands came from the measured width in the "
                   "diffraction pattern.",
                3: "That came from Franklin’s work on how much water DNA takes "
                   "up.",
            }},
        # ⚖️ Design's, untouched, and the rung that carries `GENE-05`: option A
        # is the belief word for word, which is why the misconception names
        # `s-ladder` as its `elicited_by`. All four options name an ACT and
        # three of them name a real act by real people in a real year, so the
        # parity falls out of the construct.
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "What did Watson and Crick actually do in 1953?",
            "options": [
                "They discovered DNA",
                "They worked out its structure, by building models that fitted "
                "other people’s measurements",
                "They proved DNA carries genetic information",
                "They took the X-ray photographs that revealed the double "
                "helix",
            ],
            "answer": 1,
            "feedback": {
                0: "DNA was discovered in 1869 by Miescher. It had been known "
                   "for over eighty years.",
                2: "Avery, MacLeod and McCarty had shown that in 1944 — which "
                   "is why the structure was worth chasing.",
                3: "Those were taken at King’s College London by Franklin and "
                   "Gosling. Watson and Crick did no experiments on DNA at "
                   "all.",
            }},
        # ⚖️ Criterion 5 is the rung's whole point: it asks WHY equal amounts of
        # A and T imply pairing, which is the one step in the lesson that is an
        # inference rather than a fact to be recalled. A student can meet the
        # first four by matching evidence to conclusion from the bench; only the
        # fifth needs the argument.
        "explain": {
            "title": "Rung 3 · Match evidence to conclusion",
            "q": "For each of the three features of the DNA model — two "
                 "strands, bases on the inside, and A pairing with T — say "
                 "which piece of evidence established it and how.",
            "field_label": "Your answer",
            "placeholder": "The two strands came from…",
            "success": [
                "Links the two strands to the X-ray diffraction pattern, and "
                "says the spacing gave the width.",
                "Says the cross-shaped pattern in the image showed the "
                "molecule was a helix.",
                "Links the bases being on the inside to Franklin’s water "
                "measurements and the phosphates being outside.",
                "Links the A-with-T and C-with-G pairing to Chargaff’s ratios.",
                "Explains why equal amounts of A and T in every species implies "
                "they must pair with each other.",
            ]},
        # ⚑ NOTES-B10 flag 10, and schema §16's ONE ACTIVE CHECK on this pass.
        # All five criteria verified one at a time against the rule that every
        # criterion must reward a FACT and none may reward a moral conclusion.
        # **All five pass and all five ship, verbatim.** The full working is in
        # the docstring; the short form is that criterion 3 marks the
        # attribution that costs a student who has read the episode as a
        # morality tale, and criterion 4's "such as" makes its example a sample
        # rather than a required answer.
        #
        # ⛔ The question asks what a fair ACKNOWLEDGEMENT would have said. It
        # does not ask whether the treatment of Franklin was right, and it must
        # not be edited into asking that — the first has a checkable answer and
        # the second does not.
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "The 1953 paper acknowledged only that the authors had been "
                 "\"stimulated by\" unpublished results from King’s College. "
                 "Using what you know about how the structure was worked out, "
                 "write what you think a fair acknowledgement would have said "
                 "— and explain what rule about using other people’s data you "
                 "would draw from this episode.",
            "field_label": "Your answer",
            "placeholder": "A fair acknowledgement would have named…",
            "success": [
                "Names Franklin specifically, and what her contribution was — "
                "the diffraction images and the measurements taken from them.",
                "Notes that the data was seen without her knowledge or "
                "permission.",
                "Recognises that Watson and Crick’s own contribution — "
                "assembling a model that fitted everything — was real and "
                "worth credit too.",
                "States a general rule, such as: data should be credited to "
                "whoever produced it, and used only with their knowledge.",
                "Avoids treating the episode as a simple story of heroes and "
                "villains — acknowledges that the history is contested or that "
                "several factors were involved.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "DNA's structure — a double helix with paired bases inside — "
                "was deduced in 1953 from evidence nobody could see directly. "
                "Franklin and Wilkins produced the X-ray diffraction images; "
                "Franklin's measurements showed the helix's dimensions and "
                "that the phosphates lie outside; Chargaff's ratios showed A "
                "pairs with T and C with G; Watson and Crick built the model "
                "that fitted all of it. The structure immediately suggested "
                "how DNA could be copied.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B10 flags 12 lives here and is checked and left; the working is in
    # the docstring. ⚖️ MRB-225 holds: the layer adds the replication argument
    # and retracts nothing above it.
    #
    # ⛔ THE CLOSING SENTENCE OF THE 1953 PAPER IS PARAPHRASED, NOT QUOTED, AND
    # THAT IS DELIBERATE (NOTES flag 12, ruled correct by schema §16). Its whole
    # force is understatement, and Design's paraphrase both keeps the
    # understatement and says it is understatement — which a cold quotation
    # cannot do at this age without a gloss longer than itself. A later pass
    # "restoring the quote" would be undoing a decision, not correcting a
    # sloppiness.
    "stretch": [
        {"type": "explainer", "id": "why-the-structure-mattered-so-much",
         "text": "The paper announcing the structure ran to about a page, and "
                 "it closed with a single sentence, phrased with deliberate "
                 "understatement, noting that the pairing they had proposed "
                 "immediately suggested a way the material could copy itself. "
                 "That sentence is the reason the structure mattered so much. "
                 "If A always pairs with T and C always with G, then each "
                 "strand carries the full information: unzip the double helix "
                 "and each half specifies exactly what must be built alongside "
                 "it. A structure that explains, in its own geometry, how "
                 "inheritance can work is a rare thing in science — most "
                 "structures have to have their function worked out "
                 "afterwards. Five years later Meselson and Stahl showed "
                 "experimentally that copying does happen that way, and the "
                 "model stopped being a proposal."},
    ],

    # ── the support layer (§5.6) — Design's, and statutory content ──────────
    # ⚑ NOTES-B10 flag 9, ruled SHIP AS DRAWN by schema §16 with every fact
    # checked. Lifted in one piece; not one word is retyped.
    #
    # ⛔ TWO SENTENCES IN THIS PARAGRAPH ARE LOAD-BEARING AND MUST NOT MOVE:
    #
    #   1. Franklin was INELIGIBLE for the Nobel, not denied it over the credit
    #      dispute. She died in 1958 and a Nobel cannot be posthumous. Design's
    #      semicolon joins the death, the 1962 award and the rule in that order
    #      and says exactly that and no more. Schema §16 calls this the single
    #      most important sentence in the passage. Do NOT sharpen it into a
    #      grievance and do NOT soften it into a coincidence.
    #   2. "Historians still argue about how much of this was…" and "What is not
    #      in dispute is…" do opposite and necessary jobs — the first refuses to
    #      settle what cannot be settled, the second refuses to leave unsettled
    #      what is. Neither is hedging and neither may be trimmed.
    #
    # The passage names no villain. It ships that way.
    "support": [
        {"type": "explainer", "id": "a-note-on-the-credit",
         "text": "Photo 51 was taken in Franklin's laboratory by her research "
                 "student Raymond Gosling. It was shown to Watson by Wilkins "
                 "without her knowledge, and a report containing her "
                 "unpublished measurements reached Crick through a research "
                 "council committee, also without her being asked. Watson and "
                 "Crick's 1953 paper acknowledged only that they had been "
                 "\"stimulated by\" unpublished results from King's. Franklin "
                 "died of ovarian cancer in 1958, aged 37, probably from her "
                 "exposure to X-rays; the Nobel Prize was awarded to Watson, "
                 "Crick and Wilkins in 1962, and the rules do not allow it to "
                 "be given posthumously. Historians still argue about how much "
                 "of this was ordinary scientific rivalry, how much was the "
                 "treatment of a woman in a hostile department, and how much "
                 "was the Nobel's own rules. What is not in dispute is that "
                 "the data were used without permission and that the "
                 "acknowledgement understated what was owed."},
    ],

    # ⚠️ DESIGN'S OWN EYEBROW, NOT THE FIXED LABEL. `r_layer`'s fallback is
    # "Need a hand?", which is a study-support offer — the right words above a
    # hint for a student stuck on the science, and the wrong words entirely
    # above a note about who was credited for what. B6 minted this override for
    # the same class of reason; schema §16 records the layer-semantics question
    # (a credit note is neither scaffolding nor stretch) as Mide's, not this
    # pass's, and MRB-205 says the page wins meanwhile.
    "support_heading": "A note on the credit",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination on
    # the page it is printed on (§4.8.1 C).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to talk through what Photo 51 actually shows?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph (page line 288) and nothing in it is a safety
    # instruction — it is a note about how far the bench and the history can be
    # trusted. Routing it through `safety_note` would print it in the treatment
    # reserved for "never light a candle without an adult".
    #
    # ⚖️ ITS LAST SENTENCE IS THE THIRD PLACE THE PAGE SAYS THE HISTORY IS
    # CONTESTED, after the credit note and rung 4's fifth criterion. All three
    # have to keep saying the same thing: one of them marks it, one of them
    # states it, and this one scopes it.
    "convention_note": "The bench is a simplification of a two-year argument "
                       "into three decisions and four tests. The real work "
                       "involved crystallography mathematics well beyond this "
                       "level, several intermediate wrong models by everyone "
                       "concerned, and evidence not listed here. The "
                       "historical account in the credit note follows the "
                       "mainstream of what historians of science have "
                       "established; several details remain contested.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is an elimination argument run over four pieces of real
    # evidence, and rungs 3 and 4 ask a student to match evidence to conclusion
    # and then to reason about how evidence should be credited — which is the
    # analysis-and-evaluation strand plus the attitudes one. Nothing on this
    # page is measured by the student, so `experimental-skills-and-
    # investigations` and `measurement` are not claimed.
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
