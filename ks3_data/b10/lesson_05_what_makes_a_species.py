"""B10 L5 — What makes a species (CLASSIFY).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b10/b10-05-what-makes-a-species.dc.html` (580 lines), her
author's notes `docs/ks3/design-reference/b10/NOTES-B10.md` §1.5 and §2 flags 15–18,
and the B10 payload schema `docs/ks3/b10-inventory/PAYLOAD-SCHEMA.md` §0, §1, §6,
§7, §8, §9, §10, §11, §12, §13, §14, §15 and §16, under the MRB-220 build
contract.

Every student-facing string is lifted byte-identical from the approved page
except the one listed under "What could not be lifted" and the three rung-1
distractors rewritten under MRB-177, each recorded below with its before and
after. The three verdicts, the seven cases, the four test cards, both marked
rungs and both self-marked rungs came out of the page's own `VERDICTS`,
`CASES`, `TEST_CARDS`, `RUNGS` and `SELF_RUNGS` arrays via
`tools/extract_design_payload.js`, not off a keyboard.

── `covers` is one clause, and it is the whole lesson ───────────────────

`KS3.B.INH.03` reads, in full: *differences between species*. It is one of the
four `INH` statements B10 owns and the only one with no minted sub-IDs, so it is
claimed whole. `INH.01` is b10-04's, `INH.02` is b10-02's and b10-03's, `INH.04`
is b10-01's; `build_ks3.validate()` enforces exactly-once ownership, so a second
claim would fail the build rather than quietly double up.

The statement says *differences between* species, and the page's answer is that
you cannot state a difference until you can say where one species stops. That is
why the lesson is a definition and its limits rather than a list of contrasts.

── ⚠️ THREE VERDICTS, AND COLLAPSING THEM TO TWO WOULD DELETE THE LESSON ──

Schema §6.1. `VERDICTS` is `same` → "Same species", `different` → "Different
species", `unclear` → **"The test does not settle it"**, in that order, and the
A/B/C letters on the buttons are derived from position.

**The third verdict is not a hedge, not an "I don't know", and not a way out.**
It is the CORRECT answer on three of the seven cases — bacteria, dandelions and
the ring of gulls — and a student who never selects it cannot score above four
out of seven. Those three are the cases where the breeding test is not hard, it
is *inapplicable*: two of them describe organisms that do not breed at all, and
the third describes a chain of populations where the test returns a different
answer depending on where along the ring you apply it.

⛔ **A later pass that "simplifies" this to a yes/no would turn a lesson about
the limits of a definition into a quiz.** The whole intellectual content of
b10-05 is that a good definition can have a boundary as well as a rule, and the
boundary is where the science actually is: it is why the key note ends on DNA
comparison, why the third and fourth test cards exist, and why rung 4 marks a
student for saying *"not yet decided"* is a reasonable answer. Two verdicts
would leave every one of those stranded, and the page would still look finished.

`r_species_cases` must refuse a `verdicts` list that is not three long, for the
same reason `r_chain_ledger` refuses a factor that is not ten.

── The lesson's own point, and the ONE WORD the two beliefs turn on ─────

The KEY FACT (schema §13, lifted verbatim): *two organisms belong to the same
species if they can breed together to produce **fertile** offspring; members of a
species vary enormously in appearance, and organisms of different species may
look almost identical — appearance is a clue, not the test.*

`GENE-09` ("organisms that look alike are the same species") and `GENE-10` ("if
two animals can have a baby together, they are the same species") are precisely
the two ways to get that wrong, and they fail in opposite directions:

    GENE-09  trusts appearance      → the dane/chihuahua case and the
                                      pipistrelles are its two counterexamples,
                                      one in each direction
    GENE-10  drops the word FERTILE → the mule, the liger and the false killer
                                      whale are its counterexamples

⚖️ **NOTHING ON THIS PAGE MAY BLUR "can have a baby" WITH "can have FERTILE
offspring".** That single word is the entire difference between the two beliefs,
it is the word Design italicises in the hook's reveal (*the word doing the work
is <em>fertile</em>*), it is the word the second confrontation opens on (*"the
definition has a second word in it, and it is the one people drop"*), it is the
first criterion of rung 3, and it is the first test card's closing sentence
(*"Both words matter: offspring, and fertile."*). Six authored strings say it.
A bench verdict, a ladder correction or a comment that says "can breed" where it
means "can produce fertile offspring" makes `GENE-10` true.

── The instrument: seven cases, and the last three are the argument ─────

`#s-bench` is `species-cases`, on `ks3-block ks3-dark ks3-practical` (page line
105), so `practical` is MEASURED from Design's own class attribute rather than
inferred from the kind name — payload schema §0 rule 2, and contract §4 records
that B1 got two of six wrong by inferring it.

⚖️ **THE CASE ORDER IS AUTHORED AND IS NOT SORTED.** Schema §6.2: one `same`,
three `different`, three `unclear`, and the three `unclear` cases are LAST and
CONSECUTIVE. The instrument spends its first four cases establishing the test —
appearance can mislead in both directions, and the word is *fertile* — and its
last three showing where the test runs out. Design's own bench lead tells the
student to *"read the last two carefully"*, which is a sentence about the order.
Re-ordering the list, or sorting it by verdict, breaks that sentence and turns a
built argument into seven unrelated items.

⚖️ **COMMIT THEN REVEAL, PER CASE, AND THE PICK FREEZES.** `run_label` is
disabled until a verdict is chosen for the current case, and once pressed the
pick is locked and the two unchosen verdicts drop to half opacity. Same gate and
same reason as `variation-plotter` (schema §6.3).

⛔ **NO RUNTIME STATE IS AUTHORED** (schema §0 rule 3). `caseId`, `picks` and
`opened` are the runtime's; `wireSpeciesCases` initialises them itself, and under
R5 a key with no read site fails `ks3_key_audit.py`.

⊖ **NO `start` KEY EITHER.** Schema §0 rule 3's exception is for an opening
selection that is NOT the first entry in its list. Design's `caseId` opens on
`'dogs'`, which IS `cases[0]`, so the renderer's default of index 0 reproduces
the page exactly and authoring the key would restate the shipped default in a
second place where a later edit could make the two disagree. (b10-02, b10-03 and
b10-04 each author theirs, because on those three the opening selection is a
teaching choice — b10-03's opens on Pauling's wrong triple helix.)

⚖️ **THE BENCH ADJUDICATES, AND THAT IS RULED RATHER THAN DRIFTED.** Schema
§0.6: `verdict_tags` prints "That is the answer" / "Not quite", which B7 §0.6
forbade and which schema §0.6 explicitly re-permits for three of the five B10
benches, measured off Design's own pages. It is words and only words — a mono
tag in accent-text on the cream panel, the same tone whichever way it went — and
it confronts the IDEA, never the student. **It must not gain the amber `is-wrong`
ladder treatment, a colour, a badge or a mark on a verdict button.** Only the
mastery ladder marks correctness (MRB-196 R10), and this stays inside the spirit
of that rule because the thing being named right or wrong is a classification,
not a person.

── FOUR rail stops, and the third is a MIRROR (MRB-249) ────────────────

Design draws four (page script, `RAIL`), and her `isDone()` gives `s-test` the
BENCH's predicate, character for character, one section to the left:

    if (id === 's-bench') return opened >= 5;
    if (id === 's-test') return opened >= 5;      // page lines 408–409

`#s-test` is an eyebrow, a display statement, four static cards and the key fact
box: no control, no commitment, no field, no reveal. It is the PAYOFF of the
bench beside it, and it carries no control precisely because the bench has
already taken the student's commitment. That relationship is a MIRROR,
`wireRail`'s `paint()` resolves it at rail level — which is the level Design
computes it at — and `ks3_parity.check_rail_matches_design` gates the built rail
against `docs/ks3/rail-manifest.md`, where this page's row reads
`s-hook s-bench s-test s-ladder | s-test=s-bench`.

⚠️ Payload schema §8's tables are correct as MEASUREMENT and its instruction to
*author three stops and drop the band* is REVERSED at the head of the same
section, by the ⊕ block dated 18 Aug 2026. Four is what Design drew and four is
what ships. Shipping three fails the build.

`done_when` is `five_cases_opened` on BOTH `s-bench` and `s-test`, which is
Design's own threshold and is deliberately five of seven rather than seven: a
student who has settled five cases has necessarily met at least one `unclear`
case, because only four cases in the whole list resolve to `same` or
`different`. Move the threshold to four and the rail can complete without the
student ever having seen the lesson's point. It is not a tuning constant, and
moving it moves TWO stops, not one.

`#s-think` and `#s-keynote` are on no rail, and that is Design's too:
`#s-keynote` asks nothing, and `#s-think` here is static markup — two quotes,
two bodies, no options, no reveal, no button — so it is a `confrontation` and
not contract R1's `predict`. Schema §9, measured on all five B10 pages, and the
rail independently confirms it by not listing `s-think`.

── What could not be lifted byte-identical, and why ────────────────────

One string, and it is a hyperlink rather than a science word.

1. **The `natural selection` hyperlink in the *Going further* layer.** `rich()`
   allows `<em>` and `<strong>` and nothing else, so no anchor survives anywhere
   on the page. Here that costs nothing at all: the link TEXT is already the
   lesson's own name, so every word is kept and only the tag goes.

       Design:  which is exactly what <a href="…">natural selection</a> predicts
       Built:   which is exactly what natural selection predicts

   The destination is not lost — `natural-selection` is Design's own first
   *Connects to* card and is carried in `references`.

The four `<em>` runs that DO survive are all kept, because `rich()` renders them
and each is load-bearing: `<em>fertile</em>` in the hook's reveal and again in
the second confrontation (the word the whole lesson turns on), `<em>Canis
familiaris</em>` (a binomial, which is italicised because that is the
convention, not for emphasis) and `<em>cryptic species</em>` (a term being
introduced).

⚠️ No sequence leak to repair: `Year`, `year 7/8/9` and `half-term` appear zero
times in Design's bytes — grepped, not assumed. The page does contain "four
thousand years" and "for a century", which are durations in the content, and
"In the 1990s", which is a date the science needs and which NOTES flag 16
confirms.

── ⊕ MRB-177 LENGTH PARITY — RUNG 1 REPAIRED, RUNG 2 CLEAN ─────────────

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one). The gate flags a
correct option that is strictly the longest AND clears the longest distractor by
≥4 words or by ≥1.4×.

    rung 1  correct 15w vs  9 /  8 /  8  — gap 6, ratio 1.67    ✗ TRIPPED (both)
    rung 1  correct 15w vs 16 / 15 / 16  — not strictly longest ✓ repaired
    rung 2  correct  7w vs  6 /  8 /  9  — not strictly longest ✓ as drawn

**Rung 2 is Design's, untouched, and it did not need touching.** Its correct
answer is the SHORTEST but one, because all four options are single "Because …"
clauses of the same shape — a name, the fertile-offspring test, a chromosome
count, a shared ancestor. Four wrong rules of the same size about the same
thing, and the parity falls out of the construct rather than being imposed on
it.

**Rung 1 tripped both arms at once** and it is the construct MRB-177 named,
exactly: Design's correct option states a RULE with a classification consequence
(*the offspring must be fertile FOR THE PARENTS TO COUNT AS ONE SPECIES*) while
all three distractors stated a one-clause wrong verdict with no consequence
attached. The correct answer was therefore longer BY CONSTRUCTION, and a student
could have scored the rung without reading it — on the one rung in the lesson
that tests the word `fertile`.

Each distractor is rewritten as a WRONG RULE in the correct answer's own shape —
a verdict, then what that verdict implies about the species question — keeping
Design's clause verbatim at the front and gaining the consequence the belief
licenses:

    r1 B  Yes — they produced offspring, which is the test
          + ", so the parents count as one species"                   9w → 16w
    r1 C  Yes, if the chicks look like both parents
          + ", because resemblance is what settles the species"       8w → 15w
    r1 D  It cannot be decided without seeing more pairs
          + ", so one infertile brood proves nothing either way"      8w → 16w

**The correct option is unchanged, `answer: 0` is unchanged, Design's option
ORDER is unchanged, and all three of her corrections are byte-identical.** Each
still answers exactly the belief its rewritten distractor states, and two of the
three now land harder:

  * B now ends on *the parents count as one species*, which is `GENE-10` stated
    as a rule rather than as a shrug, and the correction's first words are
    "Half the test."
  * D now claims *one infertile brood proves nothing either way*, and the
    correction contradicts precisely that: "the result described — healthy but
    infertile offspring — is exactly the signature of two species."

⚖️ **The four options now run 15 / 16 / 15 / 16, so the correct answer is one of
the two shortest and there is no tell in either direction.** That was
deliberate: padding the distractors well past the correct answer would trade one
tell for its mirror image, which a class works out just as fast.

⚑ For Mide's science gate — every NOTES-B10 flag landing on THIS lesson, and
  what was checked against it. Four flags, four checked, **none corrected.**
  Flags 15 and 16 are the two the dispatch named, and schema §16 has already
  ruled both *ship as drawn*; they are not re-derived here, only confirmed to
  have shipped unaltered.

  * flag 15  **Horse 64, donkey 62, mule 63, and "almost always infertile".**
             RULED IN SCHEMA §16 AND SHIPPED AS DRAWN. The three numbers appear
             in exactly three places — the `mule` case's `facts`, the second
             confrontation's body, and rung 3's second criterion — and all three
             agree. The hedge is carried in four: "almost always unable to
             reproduce" (case facts), "in almost every case it cannot reproduce"
             (confrontation), "almost always infertile" (rung 3 criterion 4),
             and the legal line, which is the one that does the real work
             because it says WHY the hedge is there: *"rare exceptions are
             recorded, including a small number of fertile female mules."*
             **The one thing that must not happen is a later pass tidying those
             hedges into "always".** That would make the legal line contradict
             the body of the page, and it would also make the `liger` case's
             *"a few females have had offspring"* read as an error.

  * flag 16  **The pipistrelle cryptic-species case.** RULED IN SCHEMA §16 AND
             SHIPPED AS DRAWN. Real; the split was recognised in the 1990s on
             echolocation frequency. It appears twice, in the `pipistrelle` case
             and in the first confrontation, and the two do not disagree: the
             case says *"roosting separately and not interbreeding"* and the
             confrontation says *"echolocated at different frequencies and never
             bred with each other"*. The frequency is the CLUE and the breeding
             is the TEST, which is the same order the key fact states, so the
             example is doing the lesson's own argument rather than illustrating
             it. ⚑ The page deliberately does not print the two species' names.
             That is Design's choice and it is the right one at KS3 — the point
             is that they were indistinguishable, and naming them invites a
             student to think there was something to see.

  * flag 17  **Ring species, and the caveat that the gull case is messier than
             the textbook version.** CHECKED AND LEFT, and the caveat is the
             reason the example is worth having. It appears twice — the `gulls`
             case's `why` ("the gull example is also messier than the textbook
             version, and honest sources say so") and the *Going further* layer
             ("has been picked over by biologists … which is worth knowing
             too") — and both are hedges on the EXAMPLE, not on the claim. The
             claim itself is the safe one: species boundaries are real without
             being sharp. That survives whatever the gulls turn out to be, which
             is exactly MRB-225 — the claim is already stated at the size that
             is true. Same editorial choice as B9 flag 6.

  * flag 18  **Liger fertility: males infertile, a few females fertile.**
             CHECKED AND LEFT. Correct as stated, and the sentence Design builds
             on it is the valuable part: *"the occasional fertile female is a
             genuine complication and is the kind of exception that makes
             biologists talk about how strongly two populations are separated
             rather than whether they are."* That is the third verdict being
             foreshadowed on a case that resolves to the second, three cases
             before the student meets it. Cutting the exception to keep the case
             clean would remove the bridge.

  * flag 19  **No diagrams anywhere in B10.** MEASURED on this page rather than
             assumed: `<img>`, `<figure>` and `<picture>` each appear ZERO
             times, and every `<svg>` is the nav chevron, a rail tick or a
             `ks3-mark`. `figures` is therefore empty by §4.10 and schema §11.
             Neither of the flag's two named candidates is this lesson's — both
             are b10-02's and b10-03's — so there is nothing here to source, and
             declaring a slot the page never references would invent a task in
             `docs/ks3/diagram-manifest.md`. ⚑ Reported anyway, per the brief: I
             do NOT think this lesson needs one. Its subject is a definition and
             the cases that stress it, all of which are prose; the nearest thing
             to a picture worth drawing would be the ring of gulls, and a ring
             diagram would have to assert a tidiness the *Going further* layer
             spends a sentence retracting.

── MRB-225, checked across the whole lesson: NO body sentence is retracted ─

Traced the claim the lesson makes: *fertile offspring is the test; appearance is
not; and the test does not reach everything.* The big question, the hook's
reveal, the four test cards, the key fact, both confrontations, rung 3's five
criteria and the key note all say the same thing at the same size — and each of
the three parts is stated with its limit attached the first time it appears,
rather than asserted and walked back later. The `unclear` cases are not a
retraction of the definition; they are the third clause of it, and the key note
carries that clause too ("does not work for organisms that never breed
sexually"). The stretch layer adds the ring-species case and retracts nothing.

── Misconception ids: GENE-09 and GENE-10, and the spare is NOT claimed ─

Schema §12 pre-allocates `GENE-09` and `GENE-10` to this lesson with `GENE-15`
as the named spare, BEFORE five parallel authors were dispatched, precisely so
that a third belief could not collide. **This lesson found no third belief and
`GENE-15` is therefore left permanently unused**, like `DRUG-07` and
`REPRO-17`/`20`/`21`/`23`. It is never re-pointed at a different belief.

Both statements are Design's own bytes, page lines 178 and 183, in register
voice with the curly quotes dropped (`_quoted()` in `build_ks3.py` supplies
those). Both rows already exist in `docs/ks3/misconception-register.md` at lines
947–948, written by the register pass, and this record agrees with them on all
four fields — checked rather than assumed, because that file is not this pass's
to edit (contract §0).

Both `elicited_by` values are `s-hook`, and that is a measurement rather than a
default: the hook's four options ARE the two beliefs and two neighbours —

    A  "They look similar enough to be grouped together"          → GENE-09
    B  "They can produce offspring together"                      → GENE-10
    C  correct
    D  "They live in the same place and have the same number of chromosomes"

— so the hook is the one place on the page where each belief is offered as
something to commit to, before any argument against it has been made. The ladder
restates both (rung 1's option B is `GENE-10` and rung 2's whole premise is
`GENE-09`), but by then the student has met the bench and the confrontation, so
the ladder TESTS the beliefs where the hook ELICITS them. Both `confronted_by`
values are `s-think`, which is where each is quoted and answered. All three
anchors resolve against the BUILT page (MRB-244).

── Keys this pass authors that the RENDERER reads (contract R5) ────────

Named explicitly rather than left to be discovered. Every one is measured off
Design's `renderVals()` and follows schema §6's shape and §1's spellings:

    progress_suffix  "settled" → `_progress_suffix`, composed into the head row's
                     "{n} of {total} settled" the same way `variation-plotter`
                     composes "{n} of {total} plotted"
    options_label    the mono label over the seven case tabs
    cases            tabs + one panel each, every panel in the document
    commit_label     the line above the three verdict buttons
    verdicts         THREE, ordered; the A/B/C letters are derived from position
    run_label /
    run_done_label   the check button's two states
    verdict_tags     the mono tag on the opened panel — schema §0.6's departure
    tally            the line beside the button, in its two forms

⚠️ **`species-cases` was not yet registered in `ACTIVITY_KIND_RENDERERS` when
this record was written** — grepped `build_ks3.py`, `shared/ks3.js` and
`ks3_parity.py`, zero hits. That is EXPECTED: the engine pass is in flight in
those files and this pass may not touch them (contract §0). The payload is
authored to schema §6 exactly, which is the document both passes read. No
renderer is added here and no key is invented to work around the gap.

⚠️ **THIS INSTRUMENT IS ON INK.** `.ks3-dark p` is (0,1,1) and beats a bare
component class at (0,1,0); every B10 colour rule is written at (0,2,0) under
`.ks3-dark …` and `ks3_parity.check_dark_text_specificity()` resolves it on the
real cascade. Recorded here because this payload is what feeds it.

── Design's page and the ENGINE: no disagreement to report on this one ─

Checked, because b9-01 had one. Design's `#s-test` runs eyebrow, display
statement, four cards, THEN the key fact box, and `r_rule()` emits exactly that
order — eyebrow, statement, cards, nested key fact, close. There is no `close`
paragraph on this page, so nothing lands after the box and the built section is
Design's, element for element.
"""


# ── the three verdicts (page script, `VERDICTS`) ─────────────────────────
#
# ⛔ THREE, ORDERED, AND THE ORDER IS THE BUTTON LETTERING. `String.fromCharCode(
# 65 + i)` in Design's `verdictOptions` derives A/B/C from position, so no letter
# is authored and re-ordering the list re-letters the instrument.
#
# ⚖️ The third is the instrument, not a hedge. See the docstring: it is the
# correct answer on three of the seven cases, and a student who never picks it
# cannot score above four out of seven.
VERDICTS = [
    {"id": "same", "text": "Same species"},
    {"id": "different", "text": "Different species"},
    {"id": "unclear", "text": "The test does not settle it"},
]

# ── the seven cases (page script, `CASES`) ───────────────────────────────
#
# ⚖️ THE ORDER IS AUTHORED AND IS NOT SORTED — schema §6.2. Four cases that
# establish the test, then three that show where it runs out, consecutive and
# last. Design's bench lead says "read the last two carefully", which is a
# sentence about this order; sorting the list by verdict would falsify it.
#
# One `same`, three `different`, three `unclear`. `dogs` is `cases[0]` and is
# therefore the tab the page opens on, which is Design's own `caseId` default —
# so no `start` key is authored (schema §0 rule 3).
CASES = [
    # `same`. The counterexample to GENE-09 in the first direction: one species
    # containing two animals that look nothing alike. The last sentence is doing
    # the comparison work — a wolf and a coyote are TWO species and look more
    # alike than these two, which is the point stated as a measurement.
    {"id": "dogs", "label": "Dane and chihuahua", "answer": "same",
     "title": "A great dane and a chihuahua",
     "facts": "A mass difference of about forty times, and skulls so different "
              "that a vet can tell the breeds apart from a single bone. Mating "
              "them naturally is impractical; with veterinary help the puppies "
              "are healthy and can themselves have puppies.",
     "why": "One species. Every dog breed is a variety of the same species, and "
            "the offspring are fertile — which is the only thing that counts. "
            "The pair also demonstrates how far appearance can differ within "
            "one species: these two look less alike than a wolf and a coyote, "
            "which are two."},
    # `different`, and the case the definition was written around. ⚑ NOTES flag
    # 15: 64 / 62 / 63 and "almost always unable to reproduce". Ruled in schema
    # §16 and shipped as drawn; the hedge is load-bearing and the legal line
    # says why. See the docstring.
    {"id": "mule", "label": "Horse and donkey", "answer": "different",
     "title": "A horse and a donkey",
     "facts": "They mate readily and produce mules, which are healthy, strong "
              "and long-lived. A horse has 64 chromosomes, a donkey 62, and a "
              "mule 63. Mules are almost always unable to reproduce.",
     "why": "Two species. The offspring exists but is infertile, and the reason "
            "is visible in the numbers: 63 chromosomes cannot be sorted into "
            "pairs when gametes are made. This is the case the definition was "
            "written around."},
    # `different`. ⚑ NOTES flag 18 — males infertile, a few females fertile.
    # The last sentence is this case's real job: it foreshadows the third
    # verdict on a case that resolves to the second, three cases before the
    # student meets one. Cutting the exception would remove the bridge.
    {"id": "liger", "label": "Lion and tiger", "answer": "different",
     "title": "A lion and a tiger",
     "facts": "They do not meet in the wild, but in captivity they have "
              "produced ligers and tigons. The hybrids are large, and the males "
              "are infertile; a few females have had offspring.",
     "why": "Two species. The male hybrids are infertile and the animals never "
            "breed together in nature. The occasional fertile female is a "
            "genuine complication and is the kind of exception that makes "
            "biologists talk about how strongly two populations are separated "
            "rather than whether they are."},
    # `different`. The counterexample to GENE-09 in the OTHER direction, and the
    # page says so: "the reverse of the dog case". ⚑ NOTES flag 16 — real, and
    # ruled in schema §16. The frequency is the clue and the breeding is the
    # test, which is the key fact's own order.
    {"id": "pipistrelle", "label": "Two pipistrelles", "answer": "different",
     "title": "Two bats that nobody could tell apart",
     "facts": "Common pipistrelles in Britain were treated as one species for a "
              "century. In the 1990s researchers noticed two groups "
              "echolocating at clearly different frequencies, roosting "
              "separately and not interbreeding.",
     "why": "Two species, and they look effectively identical — the reverse of "
            "the dog case. These are called cryptic species, and DNA work has "
            "since found a great many of them. Appearance failed completely "
            "here, and the breeding test settled it."},
    # ── the three `unclear` cases ────────────────────────────────────────
    #
    # ⚖️ These three are the lesson. Each names what biologists do INSTEAD, so
    # the third verdict is never left as "nobody knows": DNA similarity here,
    # consistent inherited differences on the dandelions, and on the gulls an
    # explanation of why no single answer exists. "Openly somewhat arbitrary"
    # is MRB-225 in one phrase and must not be softened — the line IS chosen,
    # and saying so is the honest form of the claim.
    {"id": "bacteria", "label": "Two bacteria", "answer": "unclear",
     "title": "Two bacteria in a petri dish",
     "facts": "Bacteria reproduce by dividing in two, not by breeding. They "
              "also swap sections of DNA with unrelated bacteria, including "
              "ones that would never be called the same species.",
     "why": "The test does not settle it, because it asks about breeding and "
            "these organisms do not breed. Biologists classify bacteria by "
            "comparing DNA sequences and drawing a line at a chosen level of "
            "similarity — a line that is useful, agreed, and openly somewhat "
            "arbitrary."},
    {"id": "dandelion", "label": "Two dandelions", "answer": "unclear",
     "title": "Two dandelions on a school field",
     "facts": "Most British dandelions produce seed without fertilisation, so "
              "each plant produces clones of itself. Botanists have named over "
              "two hundred British microspecies.",
     "why": "The test does not settle it. With no interbreeding there is "
            "nothing for the definition to test, so botanists fall back on "
            "consistent inherited differences — and end up with a number of "
            "species that depends on how finely they choose to divide."},
    # The seventh, and the one the stretch layer picks up. ⚑ NOTES flag 17 — the
    # caveat is a hedge on the EXAMPLE, not on the claim, and the claim survives
    # whatever the gulls turn out to be.
    {"id": "gulls", "label": "A ring of gulls", "answer": "unclear",
     "title": "Herring gulls and lesser black-backed gulls",
     "facts": "A chain of gull populations circles the Arctic. Each interbreeds "
              "with its neighbours all the way round, but where the two ends "
              "meet in Britain, the birds behave as two separate species.",
     "why": "The test gives different answers depending on where you apply it, "
            "which is not a fault in the gulls. It is what you should expect if "
            "species form gradually as populations drift apart — catch the "
            "process halfway and there is no sharp line to find. The gull "
            "example is also messier than the textbook version, and honest "
            "sources say so."},
]

# ── the four test cards (page script, `TEST_CARDS`) ──────────────────────
#
# Design's `kind` is the mono accent tag and maps to `role`, which is the slot
# `_rule_card()` reads for it; `name` and `body` keep their own names.
#
# ⚖️ The four cards are the definition's shape in one row: what it says, where
# it works, where it strains, and what it is NOT. Cards 3 and 4 are the two the
# bench's last three cases and `GENE-09` respectively depend on, so neither is
# a rounding-out card. Card 1's closing sentence — "Both words matter:
# offspring, and fertile." — is the sentence the whole lesson turns on.
TEST_CARDS = [
    {"role": "The definition", "name": "Fertile offspring",
     "body": "Two organisms are the same species if they can breed to produce "
             "offspring that can themselves reproduce. Both words matter: "
             "offspring, and fertile."},
    {"role": "Where it works", "name": "Animals that breed sexually",
     "body": "Clean and decisive for most animals and many plants, and it "
             "explains hybrids like the mule without needing an extra rule."},
    {"role": "Where it strains", "name": "Organisms that do not breed",
     "body": "Bacteria divide, many dandelions clone themselves, and fossils "
             "cannot be bred at all. For these, biologists compare DNA or "
             "inherited features instead."},
    {"role": "What it is not", "name": "Looking alike",
     "body": "One species can look wildly different individual to individual, "
             "and two species can be indistinguishable. Appearance is where "
             "you start, not where you finish."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 167 character for character.
    "slug":        "what-makes-a-species",
    "title":       "What makes a species",
    "discipline":  "biology",
    "unit":        "inheritance-and-dna",
    "family":      "CLASSIFY",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.INH.03` — differences between species — owned whole. It mints no
    # sub-IDs, so there is nothing to split. INH.01, .02 and .04 belong to
    # b10-04, b10-02/03 and b10-01 and are not touched here.
    "covers":      ["KS3.B.INH.03"],
    # Named, used, and owned elsewhere. INH.04 is b10-01's and is what the
    # dane/chihuahua case rests on — the page says variation within a species is
    # enormous and does not re-teach continuous versus discontinuous. INH.05 is
    # B11's, and the stretch layer's last clause ("exactly what natural
    # selection predicts") uses it as an explanation without teaching it.
    "touches":     ["KS3.B.INH.04", "KS3.B.INH.05"],
    "beyond_statutory": False,
    # `genes-and-evolution` at `secure`: the student has variation from b10-01,
    # the chromosome/gene/DNA model from b10-02, its history from b10-03 and
    # heredity from b10-04, and this is where all four are used together on a
    # question none of them answers on its own. B11 develops the thread further
    # rather than securing it again.
    "threads":     [{"id": "genes-and-evolution", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" card, in her order. Both are B10's own and
    # both resolve against the flat slug registry.
    "requires":    ["passing-it-on-heredity",
                    "variation-continuous-and-discontinuous"],
    "assumes":     [],
    # Design's "Connects to" card, in her order.
    #
    # ⚠️ Both carry their unit. A bare slug in `references` is resolved against
    # the CURRENT unit — unlike `requires`, which resolves across the key stage
    # — so a bare `natural-selection` would build a link to
    # `/ks3/biology/inheritance-and-dna/natural-selection.html`, which is not a
    # page.
    #
    # ⊕ B11 IS NOT YET AUTHORED, AND THAT IS FINE HERE. `natural-selection` is
    # a `reference` rather than a `requires` precisely so this lesson can ship
    # before B11 does: an unknown `requires` target FAILS the build, while an
    # unbuilt reference renders as "Natural selection (Evolution, extinction
    # and biodiversity — coming soon)". That is the structure-first guarantee
    # working, not a gap — the same shape b9-06 used to point forward at this
    # very unit before it existed. `unicellular-organisms` is B1's, is authored
    # and shipped, and resolves to a real page today; it is the destination the
    # `bacteria` case implicitly points at.
    "references":  [{"unit": "B11", "lesson": "natural-selection"},
                    {"unit": "B1", "lesson": "unicellular-organisms"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Speciation, isolation mechanisms, classification systems "
                   "and the use of DNA sequencing to work out relationships.",

    # ── framing ─────────────────────────────────────────────────────────────
    # Design's `.ks3-bigq`. It states both beliefs as the two things the lesson
    # will refuse, in one sentence each, before the hook has started.
    "big_question": "A great dane and a chihuahua are one species. A donkey and "
                    "a horse are two, even though they can have offspring "
                    "together. Looking similar is not the test, and neither is "
                    "being able to breed.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-test` is the third: no control of its
    # own, so it mirrors `s-bench` and ticks on the bench's predicate — Design's
    # own `isDone()`, page lines 408–409. `short` and `label` are her
    # `RAIL_SHORT` and `RAIL` strings. Shipping three fails
    # `check_rail_matches_design`; see the docstring.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "The mule",
         "done_when": "committed"},
        # ⚖️ FIVE of seven, and it is Design's own number rather than a round
        # one. Only four cases in the list resolve to `same` or `different`, so
        # a student who has settled five has necessarily opened at least one
        # `unclear` case — the threshold is what makes the rail refuse to
        # complete on the easy half of the bench. Moving it moves TWO stops.
        {"anchor": "s-bench", "short": "CASES", "label": "Hard cases",
         "done_when": "five_cases_opened"},
        {"anchor": "s-test", "short": "TEST", "label": "The test",
         "mirrors": "s-bench", "done_when": "five_cases_opened"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key, and Design's own
    # reveal is gated on `hookChoice !== null` rather than on a right answer.
    # C is the correct one and the reveal says so at once; the hook is not a
    # trick, it is the claim the bench then has to earn across seven cases.
    #
    # ⚖️ A IS `GENE-09` AND B IS `GENE-10`, IN THE STUDENT'S OWN WORDS, which
    # is why both misconceptions name `s-hook` as their `elicited_by`. D is a
    # fourth wrong rule of the same size — place plus chromosome count — and is
    # answered by rung 2's option C rather than by a misconception id.
    #
    # ⚖️ The reveal italicises ONE word and it is the lesson's whole hinge:
    # "the word doing the work is <em>fertile</em>". `rich()` renders `<em>`,
    # so it survives. Losing it would make B and C read as near-synonyms.
    "phenomenon": {
        "kind": "narrative",
        "title": "A mule has a horse for a mother and a donkey for a father.",
        "prompt": "Mules are strong, healthy, long-lived and have been bred "
                  "deliberately for four thousand years. They are also, almost "
                  "without exception, unable to have offspring of their own. "
                  "Horses and donkeys are classed as two species, and the mule "
                  "is the reason.",
        "commit": "So what is the test for two organisms being the same "
                  "species?",
        "options": [
            "They look similar enough to be grouped together",
            "They can produce offspring together",
            "They can produce offspring that can themselves reproduce",
            "They live in the same place and have the same number of "
            "chromosomes",
        ],
        "reveal": "Whether they can produce offspring that can themselves "
                  "reproduce. Not whether they look alike, and not merely "
                  "whether they can have young — the word doing the work is "
                  "<em>fertile</em>. A mule is a living animal and a genetic "
                  "dead end, which is why its parents belong to different "
                  "species.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Schema §12's pre-allocation, and the two beliefs Design's `#s-think`
    # quotes. Both statements are her own bytes, page lines 178 and 183, in
    # register voice with the curly quotes dropped — `_quoted()` supplies those.
    #
    # ⛔ `GENE-15` IS THIS LESSON'S NAMED SPARE AND IS NOT CLAIMED. No third
    # belief was found, so it stays permanently unused, like `DRUG-07`. It is
    # never re-pointed at a different belief, in this family or any other.
    # ⛔ `GENE-06` MUST NOT BE MINTED by any B10 pass — it is a permanent gap
    # and its belief is `NOS-03` (schema §12, ruled 18 Aug 2026).
    #
    # Both rows already exist in `docs/ks3/misconception-register.md` (lines
    # 947–948) and agree with these four fields exactly; that file is not this
    # pass's to edit (contract §0) and was read, not written.
    #
    # `elicited_by` is `s-hook` on both, and it is a measurement: the hook's
    # options A and B ARE the two beliefs, offered as something to commit to
    # before any argument against them has been made. The ladder restates both
    # but by then TESTS them. `confronted_by` is `s-think`, where each is quoted
    # and answered. All three anchors resolve against the BUILT page (MRB-244).
    "misconceptions": [
        {"id": "GENE-09",
         "statement": "Organisms that look alike are the same species.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "GENE-10",
         "statement": "If two animals can have a baby together, they are the "
                      "same species.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B10 (schema §7's chassis table
    # lists six sections and none of them is one), so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its
    # exclusion list. Every definition below is authored, not lifted.
    #
    # ⚖️ "fertile" gets its own chip although it is an ordinary English word.
    # It is the word `GENE-10` drops, and a student who reads it as "able to
    # have babies" rather than "able to have babies THAT CAN THEMSELVES HAVE
    # BABIES" has the misconception back. The gloss is the correction.
    "vocabulary": [
        {"term": "species",
         "definition": "A group of organisms that can breed together to "
                       "produce fertile offspring.",
         "note": "The test is breeding, not appearance."},
        {"term": "fertile",
         "definition": "Able to reproduce — to produce offspring of its own.",
         "note": "The word the definition turns on. A mule is alive and "
                 "healthy and is not fertile."},
        {"term": "hybrid",
         "definition": "The offspring of two different species, such as a mule "
                       "or a liger.",
         "note": "Usually infertile, which is the evidence that its parents "
                 "are two species."},
        {"term": "cryptic species",
         "definition": "Two species that look effectively identical and were "
                       "filed under one name until closer study separated "
                       "them.",
         "note": "Britain's pipistrelle bats, split on their echolocation "
                 "frequency."},
        {"term": "ring species",
         "definition": "A chain of populations where each interbreeds with its "
                       "neighbours, but the two ends of the chain do not.",
         "note": "The case where the definition gives different answers "
                 "depending on where you apply it."},
    ],

    # ── figures (§4.10, schema §11) ─────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED. `<img>`, `<figure>` and `<picture>` each appear
    # zero times on this page — grepped — and every `<svg>` is chrome: the nav
    # chevron, the rail tick, the ladder tick and cross, the endmatter arrows.
    # NOTES-B10 flag 19's two candidates are b10-02's and b10-03's, not this
    # lesson's, so there is nothing here to source; declaring a slot the page
    # never references would invent a task in `docs/ks3/diagram-manifest.md`.
    # See the docstring for why I do not think this lesson wants one.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b10/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 105), so the segment is MEASURED and not inherited.
        #
        # Payload keys follow docs/ks3/b10-inventory/PAYLOAD-SCHEMA.md §6 and
        # the §1 spelling table. The read sites are listed in the docstring;
        # `caseId`, `picks`, `opened` and a `start` key are all deliberately
        # absent and each has its own reason there.
        {"type": "species-cases", "id": "same-species-or-not",
         "anchor": "s-bench", "segment": "practical",
         "demand": "classify",
         "eyebrow": "At the bench · seven hard cases",
         "heading": "Same species or not?",
         "prompt": "Every one of these is chosen because the obvious answer is "
                   "wrong, or because the test itself struggles. Commit before "
                   "you check — and read the last two carefully, because they "
                   "are the ones biologists still argue about.",
         # Design's `benchProgress` is `openedCount + ' of ' + CASES.length +
         # ' settled'` — one count, one denominator, one authored word at the
         # end. §1 names that word `progress_suffix` and the format is composed
         # in `_KIND_HEAD_FROM`, exactly as `variation-plotter`'s is, so the
         # braces are the engine's problem and not an author's.
         "progress_suffix": "settled",

         "options_label": "The pair",
         "cases": CASES,

         "commit_label": "Same species?",
         # ⛔ THREE, AND THE BUILD MUST REFUSE TWO. See the docstring: the third
         # is the correct answer on three of the seven cases and is the whole
         # intellectual content of the lesson.
         "verdicts": VERDICTS,

         "run_label": "Check it",
         "run_done_label": "Settled",
         # ⚖️ Schema §0.6's ruled departure from B7 §0.6. Words only — a mono
         # tag in accent-text on the cream panel, the same tone either way. No
         # colour, no badge, no mark on a verdict button, and never the amber
         # `is-wrong` ladder treatment.
         "verdict_tags": {"right": "That is the answer", "wrong": "Not quite"},
         # Design's `tallyLabel`, both branches: the finished sentence and the
         # suffix after the remaining count.
         "tally": {"all": "all seven settled",
                   "remaining_suffix": "still to settle"}},

        # #s-test — the band panel, and the payoff of the bench beside it. Rail
        # stop 3, mirroring `s-bench`. It holds this lesson's KEY FACT, which is
        # why MRB-249 refused to drop the stop: the section is teaching, not a
        # spacer.
        #
        # Design draws eyebrow, statement, four cards, key fact — and `r_rule()`
        # emits exactly that order, so there is no engine disagreement to report
        # on this page. There is no closing paragraph, so no `close` key.
        {"type": "rule", "anchor": "s-test",
         "eyebrow": "The test, and where it runs out",
         "statement": "A good definition that does not cover everything.",

         "cards": TEST_CARDS,

         # Design nests the key fact inside this section on the CARD ground with
         # the 5px accent offset shadow. `card`, because the section itself is
         # `--ks3-band` and band on band is invisible — the same arrangement and
         # the same reason as b7-01's, b8-01's and b9-01's.
         "key_fact": {"ref": "fertile-offspring-is-the-test", "ground": "card"}},

        {"type": "misconception", "id": "looks-alike-and-can-have-a-baby",
         "anchor": "s-think", "targets": "GENE-09"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside #s-test on the card ground — Design's own arrangement,
    # measured: `--ks3-card`, 2px ink border, `box-shadow: 5px 5px 0
    # var(--ks3-accent)`. Never amber. Lifted byte-identical from page line 172
    # and identical to payload schema §13's b10-05 entry.
    #
    # ⚖️ Three sentences, and each one kills a different wrong reading: the
    # first is the rule (with `fertile` in it), the second is `GENE-09` in both
    # directions at once, the third is the one-line summary a student will
    # actually carry. Contract §2 R3 stands — the shipped `shared/ks3.css`
    # figures win over Design's per-page shadow drift.
    "key_facts": [
        {"id": "fertile-offspring-is-the-test",
         "text": "Two organisms belong to the same species if they can breed "
                 "together to produce fertile offspring. Members of a species "
                 "vary enormously in appearance; organisms of different "
                 "species may look almost identical. Appearance is a clue, not "
                 "the test.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment on Design's page
        # (measured: static markup, no options, no reveal, no button, schema
        # §9), so it is a `confrontation` and not a `predict`, it is not a rail
        # stop, and it emits no completion contract. Contract R1's `predict`
        # branch applies where `#s-think` gates a reveal behind a commitment;
        # no B10 page does.
        {"id": "looks-alike-and-can-have-a-baby",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "GENE-09",
         "statements": [
             # GENE-09. The `<em>` runs are kept — `rich()` renders them —
             # because both are conventional italics rather than emphasis: a
             # binomial, and a term being introduced.
             #
             # ⚖️ "Fails in both directions at once" is the paragraph's whole
             # structure and both directions are needed. One species that looks
             # different (dogs), and two species that look the same
             # (pipistrelles). Cutting either half leaves a rule a student can
             # satisfy by adding "unless they are very different", which is not
             # what the lesson is claiming.
             {"quote": "Organisms that look alike are the same species.",
              "body": ["Appearance fails in both directions at once, which is "
                       "why it cannot be the test. In one direction, a great "
                       "dane and a chihuahua differ in mass by a factor of "
                       "forty and are unquestionably one species — every breed "
                       "of dog is <em>Canis familiaris</em>, and a great dane "
                       "and a chihuahua are more different in appearance than "
                       "a wolf and a coyote, which are two species. In the "
                       "other direction, biologists regularly find <em>cryptic "
                       "species</em>: populations that are visually identical, "
                       "that entomologists happily filed under one name for a "
                       "century, and that turn out on closer study not to "
                       "interbreed at all. There are pipistrelle bats in "
                       "Britain that were recognised as two species only when "
                       "someone noticed they echolocated at different "
                       "frequencies and never bred with each other. Looking at "
                       "an organism tells you what to guess. Only breeding "
                       "tells you the answer."]},
             # GENE-10, and the paragraph that carries the chromosome
             # arithmetic. ⚑ NOTES flag 15 lives in the middle sentence and is
             # ruled in schema §16; the hedge "in almost every case" is
             # load-bearing and agrees with the legal line.
             #
             # ⚖️ "The definition has a second word in it, and it is the one
             # people drop" is the sentence the whole misconception turns on,
             # and `<em>fertile</em>` at the end is the same word italicised for
             # the second time on the page. This is a correction of a WORD, not
             # of a fact: nothing here disputes that hybrids exist.
             {"quote": "If two animals can have a baby together, they are the "
                       "same species.",
              "body": ["The definition has a second word in it, and it is the "
                       "one people drop. A lion and a tiger can produce a "
                       "liger; a horse and a donkey produce a mule; a false "
                       "killer whale and a bottlenose dolphin have produced "
                       "offspring in captivity. In each case the hybrid is a "
                       "real, living, often healthy animal, and in almost "
                       "every case it cannot reproduce. The reason is usually "
                       "chromosome number: a horse has 64 chromosomes and a "
                       "donkey 62, so a mule has 63 — an odd number that "
                       "cannot be sorted into matching pairs when gametes are "
                       "made, and the process stalls. So the test is "
                       "<em>fertile</em> offspring, and hybrids are precisely "
                       "the evidence that two populations have separated far "
                       "enough to count as two species. They are not a "
                       "loophole in the definition; they are how it is "
                       "applied."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RUNG 1 REPAIRED, RUNG 2 CLEAN AS DRAWN. rung 1
    # correct 15w against 9 / 8 / 8 as delivered, which tripped BOTH arms of the
    # gate, and 16 / 15 / 16 after each distractor is rewritten as a wrong RULE
    # in the correct answer's own shape; rung 2 correct 7w against 6 / 8 / 9
    # (not strictly longest). The correct option, `answer`, Design's option
    # ORDER and every one of her six corrections are byte-identical. Full
    # working, with the before and after of all three, in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Apply the definition",
            "q": "Two birds mate and produce healthy chicks. The chicks grow "
                 "up and are unable to have young of their own. Same species?",
            # ⊕ MRB-177, 18 Aug 2026. Options 1, 2 and 3 rewritten as wrong
            # RULES in the correct answer's shape — a verdict, then what that
            # verdict implies about the species question. Option 0 and `answer`
            # are Design's, unchanged. Each rewrite keeps Design's own clause
            # verbatim at the front.
            #
            #   A  correct, Design's, unchanged
            #   B  GENE-10 — "they produced offspring, which is the test"
            #   C  GENE-09 applied to the OFFSPRING rather than the parents:
            #      resemblance as the thing that settles it
            #   D  authored belief: a single result cannot settle a
            #      classification, so infertility is not evidence
            "options": [
                # 15w — Design's, unchanged.
                "Yes — they produced offspring, which is the test, so the "
                "parents count as one species",
                # 16w. Was "Yes — they produced offspring, which is the test"
                # (9w). The added clause is GENE-10 stated as a rule with its
                # classification consequence, which is what the correction's
                # "Half the test" answers.
                "No — the offspring must be fertile for the parents to count "
                "as one species",
                # 15w. Was "Yes, if the chicks look like both parents" (8w).
                # Now states resemblance as the deciding rule, which
                # "Appearance is not part of the definition at all"
                # contradicts precisely.
                "Yes, if the chicks look like both parents, because "
                "resemblance is what settles the species",
                # 16w. Was "It cannot be decided without seeing more pairs"
                # (8w). The consequence the belief licenses: that the observed
                # result carries no information.
                "It cannot be decided without seeing more pairs, so one "
                "infertile brood proves nothing either way",
            ],
            "answer": 1,
            # All three unchanged from Design, and each still answers exactly
            # the belief its rewritten distractor states — which is the test of
            # whether the rewrite changed what the question measures.
            "feedback": {
                0: "Half the test. The offspring must be able to reproduce, or "
                   "the two lines are still going nowhere together.",
                2: "Appearance is not part of the definition at all. A mule "
                   "looks like both its parents and settles nothing.",
                3: "More pairs would confirm it, but the result described — "
                   "healthy but infertile offspring — is exactly the signature "
                   "of two species.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A great dane and a chihuahua look nothing alike. Why are "
                 "they the same species?",
            # Design's four, untouched, and they did not need touching: all
            # four are single "Because …" clauses of the same size about the
            # same thing, so a student cannot pick by shape.
            #
            #   A  authored belief: the name decides the species
            #   B  correct
            #   C  authored belief: chromosome number is the test — the one the
            #      hook's option D also offers
            #   D  authored belief: shared ancestry is the test
            "options": [
                "Because they are both called dogs",
                "Because their offspring can themselves have offspring",
                "Because they have the same number of chromosomes",
                "Because they were bred from the same original animal",
            ],
            "answer": 1,
            "feedback": {
                0: "A name is a decision people made. The species question is "
                   "about biology, and the answer here happens to agree with "
                   "the name — but not because of it.",
                2: "True, and it is a reason the breeding works rather than "
                   "the test itself. Some different species share a chromosome "
                   "number.",
                3: "Sharing an ancestor is a fact about history. Two species "
                   "also share ancestors, further back.",
            }},
        # ⚖️ Criterion 1 is the definition WITH the word `fertile` in it and
        # criterion 5's last clause is `GENE-10` refused explicitly — "producing
        # offspring alone is not enough". The rung marks the arithmetic in
        # between, but those two criteria are what stop a student scoring it by
        # reciting chromosome numbers.
        "explain": {
            "title": "Rung 3 · Explain the mule",
            "q": "Explain why horses and donkeys are classed as two species "
                 "even though they readily produce mules, and use the "
                 "chromosome numbers in your answer.",
            "field_label": "Your explanation",
            "placeholder": "A horse has 64 chromosomes…",
            "success": [
                "States the definition: same species means fertile offspring.",
                "Says a horse has 64 chromosomes and a donkey 62, so a mule "
                "has 63.",
                "Says an odd number cannot be sorted into matching pairs when "
                "gametes are made.",
                "Concludes the mule cannot produce working gametes and so is "
                "almost always infertile.",
                "Concludes that horses and donkeys are therefore two species, "
                "and notes that producing offspring alone is not enough.",
            ]},
        # ⚖️ CRITERION 5 IS THE THIRD VERDICT, MADE ASSESSABLE. The question
        # asks for three things and the third is "why the answer might
        # reasonably be 'not yet decided'" — so a student is MARKED for
        # producing the bench's third verdict on a case they have never seen.
        # That is what stops "the test does not settle it" being a button the
        # student pressed three times and forgot. Criterion 3 is `GENE-09` and
        # criterion 4 is the escape route the key note names.
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A biologist finds two populations of beetle on either side "
                 "of a mountain range. They look identical. Describe what she "
                 "would need to find out to decide whether they are one "
                 "species or two, what she should do if they cannot be brought "
                 "together, and why the answer might reasonably be \"not yet "
                 "decided\".",
            "field_label": "Your answer",
            "placeholder": "The test is whether they can produce fertile "
                           "offspring, so…",
            "success": [
                "Says the test is whether they can breed together and produce "
                "fertile offspring.",
                "Proposes bringing them together and observing whether they "
                "mate and whether the offspring can then reproduce.",
                "Notes that looking identical proves nothing, referring to "
                "cryptic species or giving an equivalent reason.",
                "Says that if they cannot be bred, comparing DNA is the "
                "alternative approach.",
                "Explains that populations separated recently may be partway "
                "to becoming separate species, so a clear answer may not exist "
                "yet.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # Four sentences: the rule, the refusal of appearance in both directions,
    # what a hybrid is evidence OF, and the boundary. The last sentence is the
    # third verdict written down, and it is what a student photographs.
    "key_note": "A species is a group of organisms that can breed together to "
                "produce fertile offspring. Appearance is not the test: one "
                "species can contain wildly different-looking individuals, and "
                "two species can look identical. Hybrids such as the mule show "
                "two populations have separated far enough to count as "
                "different species. The definition does not work for organisms "
                "that never breed sexually, and for those biologists compare "
                "DNA instead.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B10 flag 17 lives in the fifth sentence and is checked and left;
    # the working is in the docstring. ⚠️ The `natural selection` hyperlink
    # loses its tag and keeps every word — "What could not be lifted" 1 — and
    # `natural-selection` is carried in `references`.
    #
    # ⚖️ MRB-225 holds: the layer applies the lesson's own claim to a case the
    # definition cannot decide and retracts nothing above it. Design's own
    # hedge — "the gull case in particular turns out to be messier than the
    # textbook version, which is worth knowing too" — is load-bearing and must
    # not be trimmed: it is the difference between teaching a real result and
    # teaching a tidy story about one. The claim the paragraph actually makes
    # ("species boundaries are real without being sharp") survives whatever the
    # gulls turn out to be, which is why the hedge costs nothing.
    "stretch": [
        {"type": "explainer", "id": "ring-species-and-the-line-you-cannot-draw",
         "text": "Ring species are the case that shows the definition bending "
                 "in real time. Around the Arctic, herring gulls and lesser "
                 "black-backed gulls form a chain of populations that circles "
                 "the pole. Each population interbreeds happily with its "
                 "neighbours all the way round — but where the two ends of the "
                 "chain meet again, in Britain, they behave as two clearly "
                 "separate species and do not interbreed. There is no point "
                 "along the ring where you could draw a line and say a species "
                 "ends here. The example has been picked over by biologists "
                 "and the gull case in particular turns out to be messier than "
                 "the textbook version, which is worth knowing too. What it "
                 "demonstrates is that species boundaries are real without "
                 "being sharp: they are the product of populations drifting "
                 "apart over time, and if you catch one in the middle of that "
                 "process you should expect the definition to strain — which "
                 "is exactly what natural selection predicts."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination on
    # the page it is printed on (§4.8.1 C), and the invitation is exact: the
    # bench covers seven pairs and the tutor is where an eighth goes.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to test the definition on a pair the bench does "
                      "not cover?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph and nothing in it is a safety instruction — it is a
    # note about how far the bench's cases and figures can be trusted. Routing
    # it through `safety_note` would print it in the treatment reserved for
    # "never light a candle without an adult".
    #
    # ⚑ NOTES-B10 flag 15's fourth and last site, and the one that does the real
    # work: it names the exception by name. It must keep saying the same thing
    # as the `mule` case, the second confrontation and rung 3's fourth
    # criterion, all four of which hedge rather than assert.
    "convention_note": "The seven cases are chosen to stress the definition "
                       "rather than to illustrate it comfortably, and several "
                       "are genuinely contested among biologists. Chromosome "
                       "numbers are as usually given; hybrid fertility is "
                       "described as \"almost always infertile\" rather than "
                       "\"always\" because rare exceptions are recorded, "
                       "including a small number of fertile female mules.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # `analysis-and-evaluation`: the bench is seven judgements against a stated
    # criterion, three of which the criterion cannot decide, and rung 4 asks for
    # a method AND an honest account of why it may not settle the question.
    # `scientific-attitudes`: the third verdict is a scientific attitude made
    # operable — the page marks a student for saying a definition has run out,
    # and says of its own bacterial classification that the line is "useful,
    # agreed, and openly somewhat arbitrary". Nothing on this page is measured,
    # so `measurement` is not claimed, and rung 4's "bring them together and
    # observe" is one criterion rather than the lesson's subject, so
    # `experimental-skills` is not claimed either.
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
