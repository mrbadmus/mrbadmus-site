"""C10 L3 — The rock cycle (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c10/c10-03-the-rock-cycle.dc.html`.

── ⚠️ THERE ARE NO AUTHOR'S NOTES FOR THIS LESSON ──────────────────────

`NOTES-C10.md` covers `c10-04` and no other page in the unit. Every science
call below is therefore RULED HERE, from Design's drawing, and written down so
that a reviewer can disagree with a decision rather than having to reconstruct
one. Where Design's drawing and any written text disagreed, the drawing won.

── ONE STATUTORY CLAUSE, AND IT IS A SUB-ID ────────────────────────────

This lesson owns `KS3.C.EA.03b` — the rock cycle. The clause split of
`KS3.C.EA.03` was ruled in the unit spine (`ks3_data/c10/__init__.py`) and
BOTH sub-IDs were minted in one pass by `c10-02`'s author, so nothing is
minted here: the row already exists and this lesson simply claims it.
`KS3.C.EA.03a` — the formation of the three rock types — is
`three-ways-to-make-a-rock`'s and is not touched.

⚠️ **THREE LESSONS COME AFTER THIS ONE AND NOTHING HERE DEPENDS ON THEM.**
`a-planet-with-limits`, `whats-in-the-air` and
`carbon-dioxide-humans-and-climate` are not linked, referenced or assumed.
`inside-the-earth` and `three-ways-to-make-a-rock` come BEFORE and are safe:
this lesson requires the second and leans on the first for what the mantle is.

── ⚖️ MRB-225 · THE VERSION THAT IS TRUE, NOT THE VERSION THAT IS FAMOUS

Eight rulings. The first three are the ones the whole lesson turns on, and the
first one is the reason Design's `#s-think` exists at all.

1. **THE ROCK CYCLE HAS NO FIXED DIRECTION AND NO STARTING POINT.** The
   famous version is the diagram in the front of every textbook: a ring with
   arrows, igneous → sedimentary → metamorphic → igneous, drawn one way
   round like a clock face. It is the single most common KS3 error in this
   topic and it is what `EARTH-08` records. What is true is that there are
   arrows ACROSS the middle as well as round the edge, and that what decides
   the route is not an order of stages but WHERE THE ROCK ENDS UP — at the
   surface, weathering; buried deep, heat and pressure; deeper and hotter
   still, melting. Design's `#s-think` is literally titled "Which way it
   runs", and every other block on the page is built so as not to retract it.

2. **A ROCK CAN SKIP STAGES, AND MELTING IS NOT REQUIRED.** Uplift and
   weathering return a metamorphic rock straight to sediment without it ever
   going near a melt; an igneous rock can be buried and metamorphosed
   without ever being sediment; a sedimentary rock can be pushed deep enough
   to melt and never be metamorphic on the way. `EARTH-09` is the belief
   that every rock must pass through every stage in turn. Three of the six
   processes on `#s-processes` declare an input that is ANY rock in the
   right place, which is the evidence for it stated as a payload rather than
   as a sentence.

3. **THE CYCLE IS NOT A SCHEDULE.** There is no timescale on which a given
   grain must move, and the six processes run at wildly different rates —
   millimetres per lifetime, days, thousands of years, millions of years.
   `EARTH-10` is the belief that the cycle is a clock with a set rate.
   Every process on `#s-processes` therefore carries a `time`, and the
   renderer refuses a payload with one missing: the times are what stop the
   block reading as a timetable, and Design drew every one of them.

   ⚑ **THE `#s-journey` SEQUENCER IS THE ONE BLOCK THAT COULD CONTRADICT
   THIS**, because it walks a full seven-stage circuit and a student could
   read that as "the order". It is closed twice: the closing sentence in the
   panel says it starts again *because the granite at the end is the granite
   at the beginning* — a cycle rather than a sequence — and `#s-think`, the
   very next stop, is the confrontation. The order is a JOURNEY one grain
   took, never the order every rock takes.

4. ⚑ **"THAT ROCK HAS NOT MOVED SIDEWAYS MUCH" IS CUT FROM THE HOOK.**
   Design's prompt says the Everest limestone has not moved sideways much,
   it has gone up. The second half is the point and is true; the first half
   is not — India carried that sea floor thousands of kilometres north
   before the collision lifted it. The built prompt says nobody carried it
   up there, the sea floor itself was lifted, and it is still rising. **A
   change to Design's words, made under MRB-225, and flagged for the science
   gate.**

5. ⚑ **DEPTH ALONE DOES NOT MELT ROCK, AND SAYING SO WOULD CONTRADICT
   `c10-01`.** Design's melting stage reads "Deep enough, the temperature is
   beyond what any rock can resist", and her think-reveal and key note both
   read "deeper still: melting". `inside-the-earth` teaches — with the
   evidence on the page — that the mantle is SOLID ROCK, hotter than
   anything the crust reaches, and that magma exists in pockets where
   conditions let a little of the rock melt. A page in the same unit that
   says depth is what melts rock retracts the lesson before it. So the
   melting stage says the rock is hot enough AND wet enough to pass its
   melting point, and names the mantle as the counter-example; the think
   reveal and the key note read "deeper and hotter still". **Three changes
   to Design's words, made under MRB-225, and flagged for the science gate.**

6. ⚑ **THE MELTING PROCESS'S INPUT GAINS TWO WORDS.** Design's arrow reads
   "any rock, deep enough → igneous rock". Under ruling 5 that label is the
   claim being corrected two lines below it, which is a block retracting
   itself. Built as "any rock, deep and hot enough". **A change to Design's
   words, flagged for the science gate.**

7. ⚑ **COOLING AT DEPTH TAKES FAR LONGER THAN MILLENNIA.** Design's melting
   process reads "Cooling takes days at the surface, millennia at depth". A
   granite body cools over hundreds of thousands to millions of years, which
   is the number the going-further layer is implicitly using when it says a
   complete circuit takes hundreds of millions. Built as "days at the
   surface, up to millions of years at depth". **A change to Design's words,
   flagged for the science gate.**

8. ⚑ **TWO CLAIMS ARE SOFTENED RATHER THAN CORRECTED**, because both are
   defensible and neither is safely quantified. Design's explainer says the
   atoms under your feet have been through the cycle "many times already"
   (built: "have been through it before"), and her going-further layer says
   the Himalayas are "still rising faster than they erode" (built: "still
   rising"). Both flagged for the science gate; neither changes the
   argument.

── ⚑ §5A · WHAT THE INSTRUMENTS COMPUTE, AND WHAT THEY ARE TOLD ────────

`#s-journey` is told seven stages in their real order, a display order, two
verdict TEMPLATES and one closing sentence. It derives: each stage's rank,
which of two authored verdicts the student's order opens, and the name of the
rock the journey returns to. That last one is the lesson's whole claim — the
close reads "the granite at the end is the granite at the beginning" — and it
is NEVER typed: `ks3_art/c10.py` reads `rock` off the first and last stage,
refuses to build if they differ, and fills `{rock}` from them. The badge
number on a placed row is written by the runtime from the press order and
appears nowhere in the payload.

`#s-processes` is told six processes and a threshold. It derives which panel
is open, which button is lit, how many have been opened, and — the checks that
matter — that no two buttons read the same, that no arrow ends where it
started, and that the drawn eyebrow's "six" is the size of the set rather than
a number an author remembered. Both blocks' head counters are asserted against
their payloads the same way, `total` against the set and `start` against what
the resting HTML actually shows.

Every control is modelled: seven rows and a reset on the sequencer, six
buttons on the reference block, and the on-load and zero states of both are in
the emitted bytes — nothing placed, every badge empty, both verdicts hidden,
the panel hidden, one process open and its button lit.

── ⊖ NO `safety_note`, DELIBERATELY ────────────────────────────────────

Nothing on this page is an instruction to do anything in a room. There is no
apparatus, no method and no substance a student handles: every process is
described as something that happens to rock somewhere else, over timescales
that make a practical impossible. Recorded rather than assumed, because an
absent note is indistinguishable from an oversight unless somebody writes down
that it was checked.

── ⊖ NO FIGURES, DELIBERATELY ──────────────────────────────────────────

Design draws none. The obvious drawing — the rock cycle diagram — is the ring
with arrows that ruling 1 above exists to break, and shipping it would hand a
student the thing `#s-think` then has to take away. The six processes carry
the arrows one at a time instead, each with what it takes in, what it turns
that into and how long it takes, which is the treatment that cannot be read as
a fixed loop.

── SAFEGUARDING ────────────────────────────────────────────────────────

CHECKED, AND NOTHING IS OWED. The lesson touches no student's body, health,
home or family circumstances. Everest, the Himalayas and continental collision
appear only as places rock has been; no death, injury, disaster, expedition or
named person is described anywhere, which is the one route by which a mountain
could reach a student who has lost someone on one. Design carried no Childline
block and none is added.

── ⚑ MRB-278 · ANSWER POSITION ─────────────────────────────────────────

Design draws both marked rungs with the correct option at index 0. C10's
ladder corpus stands at [2, 1, 2, 1] across the four indices, so this lesson
takes **recall=1 and apply=3** and brings the unit's eight rungs to
[2, 2, 2, 2] with no index empty. **Only the ORDER moves; no correct option's
text is edited by the move**, which is the treatment every C10 rung has taken.

The twelve bank questions use all four indices, three each.

── ⚑ MRB-177 / MRB-278 · THE DISTRACTORS ARE REWRITTEN, THE ANSWERS ARE NOT

Three option sets on Design's page are length tells, all three in the shape
the MRB-177 ruling names — the correct option states a RULE and each
distractor states a short wrong REASON:

  · recall rung   11w correct against a longest distractor of  5w
  · apply rung    13w correct against a longest distractor of  7w
  · `#s-think`    14w correct against a longest distractor of  9w

Every one is fixed AT THE DISTRACTOR. Each distractor is re-authored as a
WRONG RULE about how rock moves round the cycle, at the correct answer's own
length; not one correct option is shortened, not one is edited, and the
corrections are rewritten only where the option they answer changed. The
hook's four options are Design's, untouched: the hook is a commitment with a
reveal and marks nothing, and its spread is 8 / 11 / 7 / 7 words.
"""

LESSON = {
    "slug":  "the-rock-cycle",
    "title": "The rock cycle",
    "discipline": "chemistry",
    "unit": "The Earth and its atmosphere",
    "family": "PROCESS",

    "covers": ["KS3.C.EA.03b"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "earth-and-universe", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    "requires": ["three-ways-to-make-a-rock"],
    "assumes": [],
    "references": [],
    "ks4_links": [],

    "meta_description": "There are marine fossils near the top of Everest. "
                        "Follow one grain of quartz all the way round the "
                        "rock cycle, and find out why it has no starting "
                        "point.",

    "big_question": "The stone in a cathedral wall was once sand on a beach, "
                    "and before that a mountain, and before that molten. "
                    "Nothing about a rock is permanent except the atoms.",

    "rail": [
        {"anchor": "s-hook",      "short": "HOOK",
         "label": "Fossils on Everest", "done_when": "committed"},
        {"anchor": "s-journey",   "short": "GRAIN",
         "label": "Follow one grain",
         "done_when": "all_seven_stages_placed"},
        # ⚠️ FOUR OF SIX, AND THAT IS DESIGN'S OWN NUMBER, not a slip. Her
        # `DONE('s-processes')` reads `Object.keys(s.seen).length >= 4` over a
        # set of six. The block is a reference a student keeps open beside the
        # sequencer; requiring all six would make the stop a reading receipt
        # rather than a record of having used it.
        {"anchor": "s-processes", "short": "ARROWS",
         "label": "Six processes",      "done_when": "four_of_six_opened"},
        {"anchor": "s-think",     "short": "THINK",
         "label": "Which way it runs",  "done_when": "committed"},
        {"anchor": "s-ladder",    "short": "LADDER",
         "label": "Mastery ladder",     "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "There are marine fossils near the summit of Everest, at "
                 "8800 metres.",
        # ⚑ RULED (MRB-225, ruling 4). Design's third sentence reads "That
        # rock has not moved sideways much — it has gone up", and the sea
        # floor in question was carried thousands of kilometres north on the
        # Indian plate before anything lifted it. The claim that matters is
        # that nothing carried it UP, and that is what is said.
        "prompt": "The rock at the top of the highest mountain on Earth is "
                  "limestone, full of the shells of sea creatures. Limestone "
                  "forms on a warm shallow sea floor. Nobody carried it up "
                  "there — the sea floor itself was lifted, and it is still "
                  "rising today.",
        "commit": "What does that tell you about rock?",
        # ⚑ DESIGN'S FOUR, UNTOUCHED. Nothing here is marked and the reveal is
        # the same for every press, so MRB-177's construct does not arise; the
        # spread is 8 / 11 / 7 / 7 words.
        "options": [
            "The fossils were carried up there by birds",
            "Rock moves, and sea floor can be pushed into a mountain",
            "The sea used to be that high",
            "Limestone can form anywhere, including on mountains",
        ],
        "reveal": "That rock moves, and that the surface of the Earth is not "
                  "fixed. Sea floor was pushed eight kilometres into the sky "
                  "when two continents collided, and it is being weathered "
                  "away up there at this moment — the fragments heading down "
                  "the rivers to become the sediment of somewhere else. "
                  "<strong>Rock is not a thing. It is a stage in a process, "
                  "and the process has no end.</strong>",
    },

    "misconceptions": [
        # ⚑ The belief Design quotes in her own words at `#s-think`. It is the
        # textbook ring with arrows, and it is what the whole lesson is for.
        {"id": "EARTH-08",
         "statement": "Sedimentary rock becomes metamorphic, and metamorphic "
                      "becomes igneous. It goes round one way, like a clock.",
         "elicited_by": "think-commit-direction",
         "confronted_by": "think-reveal-direction"},
        # ⚑ NO `elicited_by`, DELIBERATELY (audit law 15 / MRB-248). Nothing
        # on this page asks a student to commit to "every rock must pass
        # through every stage" as a belief of its own — `#s-think`'s options
        # are about DIRECTION, which is `EARTH-08`. What confronts it is the
        # reference block: three of its six processes take ANY rock in the
        # right place as their input, which is the skipping stated as evidence
        # rather than as a sentence. The question bank carries the elicitation
        # instead, at `c10-03-s02` and `c10-03-h01`.
        {"id": "EARTH-09",
         "statement": "A rock has to go through every stage of the cycle in "
                      "turn, so nothing can become sedimentary without "
                      "melting first.",
         "confronted_by": "process-arrows"},
        # ⚑ The hook IS the elicitation: a rock eight kilometres above where
        # it formed, with three of the four options offering ways for it to
        # have got there without the rock itself having changed. What kills it
        # is following one grain all the way round and finding it in seven
        # different rocks.
        {"id": "EARTH-10",
         "statement": "A rock is a permanent thing, so the stone and the "
                      "mountains around us have always been what they are "
                      "now.",
         "elicited_by": "s-hook",
         "confronted_by": "grain-order"},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "The three rock types are not three separate worlds. Each "
                 "one can be turned into either of the others, given the "
                 "right conditions and enough time, and the whole set of "
                 "routes is called the <strong>rock cycle</strong>."},
        # ⚑ RULED (MRB-225, ruling 8). Design's second sentence ends "have
        # been through it many times already", which is likely and is not
        # safely quantifiable for any particular atom.
        {"type": "explainer",
         "text": "It has no beginning and no end. The atoms in the rock "
                 "beneath your feet have been through it before."},

        # ── #s-journey — seven stages, shuffled, put them in order. Light
        # `ks3-block` in Design's file, so the unit's `_INSTRUMENT_SEGMENTS`
        # map sends it to the `check` shell.
        #
        # ⚠️ THE ORDER IS ONE GRAIN'S JOURNEY, NEVER THE ORDER EVERY ROCK
        # TAKES, and the closing sentence and `#s-think` are what keep it
        # that way. See ruling 3 in the module docstring.
        {"type": "grain-journey", "id": "grain-order", "anchor": "s-journey",
         "eyebrow": "Your turn · follow one grain",
         "heading": "Seven stages, shuffled. Put them in the order they "
                    "happen.",
         "prompt": "One grain of quartz, one complete circuit, back to where "
                   "it started. Tap the stages in order.",
         "demand": "construct",
         "head_counter": {"format": "{n} of {total} placed",
                          "start": 0, "total": 7},
         "reset_label": "Start the order again",

         # ⚠️ `rock` ON THE FIRST AND LAST STAGE IS WHAT MAKES THIS A CYCLE,
         # and it is the only place the word in the closing sentence is
         # written. `ks3_art/c10.py` refuses a payload whose journey does not
         # return to where it started.
         "stages": [
             {"id": "j1", "rock": "granite",
              "text": "Frost and rain break a grain of quartz off a granite "
                      "mountainside.",
              "why": "Weathering. Water gets into cracks, freezes, expands "
                     "and levers the rock apart; acids in rainwater attack "
                     "some minerals chemically. The rock is broken down "
                     "where it stands."},
             {"id": "j2",
              "text": "A stream carries the grain down the valley, rounding "
                      "it as it goes.",
              "why": "Erosion and transport. Moving water, wind or ice picks "
                     "the fragments up and moves them, knocking the corners "
                     "off on the way — which is why beach sand is rounded "
                     "and freshly broken rock is sharp."},
             {"id": "j3",
              "text": "The river slows where it reaches the sea and drops "
                      "the grain on the sea floor.",
              "why": "Deposition. Moving water can only carry sediment while "
                     "it is moving fast enough; when it slows, the heaviest "
                     "particles are dropped first. Layer settles on layer, "
                     "oldest at the bottom."},
             {"id": "j4",
              "text": "Buried under later layers, the grain is squeezed and "
                      "cemented into sandstone.",
              "why": "Compaction and cementation. The weight above squeezes "
                     "the water out, and dissolved minerals crystallise "
                     "between the grains and glue them together. This is now "
                     "sedimentary rock."},
             {"id": "j5",
              "text": "Two continents collide, and the sandstone is pushed "
                      "deep and cooked without melting.",
              "why": "Metamorphism. Heat and pressure make the crystals grow "
                     "and rearrange while the rock stays solid. The "
                     "sandstone becomes quartzite — a metamorphic rock."},
             # ⚑ RULED (MRB-225, ruling 5). Design's why reads "Deep enough,
             # the temperature is beyond what any rock can resist", which
             # retracts `inside-the-earth` — the mantle is hotter than any of
             # this and is solid rock.
             {"id": "j6",
              "text": "Pushed deeper still, the rock passes its melting "
                      "point and becomes magma.",
              "why": "Melting. Deep in the root of a mountain range the rock "
                     "is hot enough, and wet enough, to pass its melting "
                     "point. Depth on its own does not do it — the mantle "
                     "below is hotter still and is solid rock. Everything "
                     "about the old rock, its layers, its crystals and its "
                     "history, is erased."},
             # ⚑ Design's why ends "The grain is back in a granite
             # mountainside". The magma stalls UNDERGROUND, so it is granite
             # long before it is a mountainside; the missing step is the
             # uplift and weathering that strip the rock above it, and saying
             # so is the cycle closing rather than a nicety.
             {"id": "j7", "rock": "granite",
              "text": "The magma stalls underground, cools slowly, and "
                      "crystallises into granite.",
              "why": "Crystallisation. Slow cooling deep underground grows "
                     "large interlocking crystals. The grain is back in "
                     "granite, and once the rock above it has been worn away "
                     "it will be a mountainside again."},
         ],

         # Design's own display order, kept: it is not a derangement — `j2`
         # happens to sit in its answer position — and it does not need to be.
         # What it must not be is the answer order, and `ks3_art/c10.py`
         # refuses that.
         "shuffled": ["j5", "j2", "j7", "j3", "j1", "j6", "j4"],

         "verdict_right": "That is the journey, and every stage has a name.",
         "verdict_wrong": "Not quite the order. Here is the journey and what "
                          "each stage is called.",

         # `{rock}` is filled from the first and last stage's own `rock`.
         "close": "And then it starts again, because the {rock} at the end "
                  "is the {rock} at the beginning. <strong>That is why it is "
                  "called a cycle rather than a sequence.</strong>"},

        # ── #s-processes — six processes, six arrows, one open at a time.
        # Also a light `ks3-block`, and also the `check` shell.
        {"type": "process-arrows", "id": "process-arrows",
         "anchor": "s-processes",
         "eyebrow": "Reference · the six processes",
         "heading": "Tap a process. Each one is an arrow on the diagram.",
         "prompt": "Each one takes a rock from one state to another, and the "
                   "time it takes is part of the answer.",
         "demand": "investigate",
         "head_counter": {"format": "{n} of {total} opened",
                          "start": 1, "total": 6},
         # Design's `DONE('s-processes')` — four, over a set of six.
         "processes_to_open": 4,

         "processes": [
             {"id": "p1", "label": "Weathering", "name": "Weathering",
              "from": "any rock at the surface", "to": "loose fragments",
              "note": "Breaking rock down where it sits. Physical weathering "
                      "is water freezing in cracks and levering them open; "
                      "chemical weathering is slightly acidic rain reacting "
                      "with the minerals. No transport is involved — that is "
                      "the next process along.",
              "time": "Millimetres per human lifetime"},
             {"id": "p2", "label": "Erosion and transport",
              "name": "Erosion and transport",
              "from": "fragments", "to": "sediment somewhere else",
              "note": "Rivers, glaciers, wind and waves pick the fragments "
                      "up and carry them. Particles are rounded and sorted "
                      "by size on the journey — which is why you can tell a "
                      "beach sand from a scree slope by looking at a "
                      "handful.",
              "time": "Days to thousands of years"},
             {"id": "p3", "label": "Deposition", "name": "Deposition",
              "from": "sediment in motion", "to": "layers of sediment",
              "note": "When the water or wind slows down it can no longer "
                      "carry its load, so it drops it — heaviest first. Each "
                      "layer is laid on top of the last, which is why the "
                      "bottom of a cliff is older than the top.",
              "time": "Continuous, layer by layer"},
             {"id": "p4", "label": "Compaction",
              "name": "Compaction and cementation",
              "from": "layers of sediment", "to": "sedimentary rock",
              "note": "The weight of later layers squeezes the water out of "
                      "the sediment below, and minerals dissolved in that "
                      "water crystallise between the grains, cementing them "
                      "together into solid rock.",
              "time": "Thousands to millions of years"},
             {"id": "p5", "label": "Heat and pressure",
              "name": "Heat and pressure",
              "from": "any buried rock", "to": "metamorphic rock",
              "note": "Deep burial, or the heat of a nearby intrusion of "
                      "magma, changes the rock without melting it. Crystals "
                      "grow, minerals rearrange and grains line up — but the "
                      "rock stays solid throughout.",
              "time": "Millions of years"},
             # ⚑ RULED (MRB-225, rulings 6 and 7). Design's arrow reads "any
             # rock, deep enough" and her time reads "millennia at depth".
             {"id": "p6", "label": "Melting and cooling",
              "name": "Melting and cooling",
              "from": "any rock, deep and hot enough", "to": "igneous rock",
              "note": "Past its melting point the rock becomes magma and all "
                      "of its structure is erased. Depth on its own is not "
                      "what does it — the mantle is deeper and hotter and is "
                      "solid rock — but where a collision drives rock and "
                      "water down into the hottest part of the crust, the "
                      "melting point is passed. Cooling reverses it: slowly "
                      "and deep underground gives large crystals, quickly at "
                      "the surface gives tiny ones.",
              "time": "Cooling takes days at the surface, up to millions of "
                      "years at depth"},
         ]},

        {"type": "key-fact", "ref": "no-start-no-end"},

        # ⊕ The keyword block is the ENGINE's, not Design's — she drew none on
        # this page, as she drew none on `c10-01` or `c10-02`, and all three
        # ship one. It is OFF THE RAIL: `docs/ks3/rail-manifest.md` records
        # five stops for this page and `#s-words` is not one of them.
        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. "
                 "If you cannot say it, you do not know it yet.",
         "terms": ["weathering", "erosion", "deposition", "metamorphism",
                   "rock cycle"]},

        {"type": "misconception", "id": "think-commit-direction",
         "anchor": "s-think", "targets": "EARTH-08"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "figures": [],

    "activities": [
        {"id": "think-commit-direction",
         "kind": "predict",
         "demand": "explain",
         "targets": "EARTH-08",
         "reveal_anchor": "think-reveal-direction",
         # ⚠️ THE QUOTE IS NOT REPEATED HERE. `r_misconception` already prints
         # the belief as `.ks3-mis-quote` from the register statement, which
         # is Design's own treatment.
         "prompt": "The diagram in most books is drawn as a circle with "
                   "arrows. Commit before you read on.",
         # ⚑ MRB-177 / MRB-278 — the three distractors are wrong RULES about
         # how rock moves round the cycle, all at the correct option's own
         # length of 14 words. Design's ran 9 / 14 / 9 / 8 with the answer
         # longest, which the predict gate reads as a set a student can solve
         # on shape — and a student who solves it on shape never commits to
         # the belief, so the reveal has nothing to confront.
         "options": [
             "Right — each type always becomes the next one round, and never "
             "any other",
             "Wrong — there are routes across the middle; any rock can "
             "become any other",
             "Right — burial only goes deeper, so a rock can never come back "
             "up",
             "Wrong — a rock keeps the type it was made as and never "
             "changes",
         ],
         # ⚑ RULED (MRB-225, ruling 5). Design's second paragraph reads
         # "Deeper still: melting".
         "reveal": [
             "There are arrows across the middle as well as round the edge. "
             "A metamorphic rock exposed at the surface is weathered into "
             "sediment without ever melting. An igneous rock can be buried "
             "and metamorphosed without ever becoming sediment. A "
             "sedimentary rock can be pushed down deep enough to melt and "
             "skip the metamorphic stage entirely.",
             "What decides the route is not an order of stages — it is "
             "<strong>where the rock ends up</strong>. At the surface: "
             "weathering. Buried deep: heat and pressure. Deeper and hotter "
             "still: melting. <strong>The cycle is a map of possible "
             "journeys, not a timetable.</strong>",
         ]},
    ],

    "key_facts": [
        {"id": "no-start-no-end", "placement": "top-level",
         "ground": "card", "eyebrow": "Key fact",
         "text": "Weathering, erosion, transport, deposition, compaction, "
                 "heat and pressure, melting and cooling turn every rock "
                 "type into every other. The cycle has no starting point and "
                 "no end."},
    ],

    "ladder": {
        # index 1 — moved from Design's 0 (MRB-278). No option text is edited
        # by the move; the three distractors were separately rewritten as
        # wrong rules under MRB-177, and the corrections follow them.
        "recall": {
            "q": "What turns layers of sediment into sedimentary rock?",
            "options": [
                "Heat and pressure deep underground, which bake the grains "
                "together",
                "Compaction under the weight of later layers, and "
                "cementation by minerals",
                "Cooling from molten rock, which sets the loose grains solid",
                "More weathering and erosion, which grind the grains until "
                "they stick",
            ],
            "answer": 1,
            "feedback": {
                0: "That makes metamorphic rock. Sedimentary rock forms much "
                   "nearer the surface, and nothing is baked.",
                2: "That is igneous rock. Sediment was never molten.",
                3: "Those two produce the sediment in the first place. "
                   "Grinding makes the grains smaller and rounder, never "
                   "stickier.",
            }},

        # index 3 — moved from Design's 0 (MRB-278), and the index the unit
        # had nothing at.
        "apply": {
            "q": "Can an igneous rock become a sedimentary rock without ever "
                 "becoming metamorphic?",
            "options": [
                "No — every rock must be metamorphosed before it can become "
                "sediment",
                "No — igneous rock is too hard for weathering to break it "
                "down",
                "Only if it melts first, because melting is what starts the "
                "cycle",
                "Yes — weathering and erosion can act on any rock at the "
                "surface",
            ],
            "answer": 3,
            "feedback": {
                0: "Nothing requires that. Rain does not check what type a "
                   "rock is before it weathers it.",
                1: "Granite weathers perfectly well, and the sand on many "
                   "beaches is what is left of it.",
                2: "Melting would make it igneous again — and the cycle has "
                   "no starting point to melt at.",
            }},

        "explain": {
            "q": "Describe how a grain of rock on a mountainside could end "
                 "up as part of a sedimentary rock on a sea floor, naming "
                 "each process in order.",
            "field_label": "Your explanation",
            "placeholder": "First the rock is broken down by…",
            "success": [
                "Says weathering breaks the rock down where it is.",
                "Says erosion and transport carry the fragments away, "
                "usually by water.",
                "Says the fragments are rounded and sorted on the journey.",
                "Says deposition drops them when the water slows.",
                "Says compaction and cementation turn the layers into solid "
                "rock.",
            ]},

        "produce": {
            "q": "A geologist says the rock cycle explains why almost none "
                 "of the Earth's original crust still exists. Explain what "
                 "they mean, and how it fits with rocks that are billions of "
                 "years old still being found.",
            "field_label": "Your answer",
            "placeholder": "The cycle keeps destroying rock because…",
            "success": [
                "Says rock is continually weathered, buried, melted and "
                "re-formed.",
                "Says a rock that melts loses all trace of what it was "
                "before.",
                "Says the cycle has been running for billions of years.",
                "Says a few very old rocks survive because they were never "
                "buried deep or exposed at the surface.",
                "Says survival is a matter of where a rock happened to sit, "
                "not what it was made of.",
            ]},
    },

    # ⚑ RULED (MRB-225, ruling 5). Design's version reads "deeper still it
    # melts", which is the sentence `inside-the-earth` spends a whole
    # instrument refuting.
    "key_note": "Rocks are broken down by weathering, carried away by "
                "erosion and transport, and deposited as sediment, which is "
                "compacted and cemented into sedimentary rock. Burial brings "
                "heat and pressure, making metamorphic rock; deeper and "
                "hotter still, some of it melts, and cooling magma makes "
                "igneous rock. Any rock type can become any other, and the "
                "cycle has no beginning or end.",

    "stretch": [
        {"type": "explainer", "id": "the-engine-is-internal-heat",
         "text": "The engine driving all of this is heat from inside the "
                 "Earth. Slow currents in the solid mantle drag the rigid "
                 "plates at the surface around; where plates collide, rock "
                 "is forced down and melted or pushed up into mountains; "
                 "where they pull apart, the pressure drops and new igneous "
                 "rock forms. Without that internal heat the continents "
                 "would have been worn flat by rain long ago, and the Earth "
                 "would be a smooth, wet, geologically dead ball."},
        # ⚑ RULED (MRB-225, ruling 8). Design's second sentence reads "and
        # are still rising faster than they erode", which is true of the
        # range as a whole and false in the valleys doing the eroding.
        {"type": "explainer", "id": "the-timescales-are-the-hard-part",
         "text": "The timescales are the hardest part to hold in your head. "
                 "Weathering removes a few millimetres of exposed rock in a "
                 "human lifetime. The Himalayas took fifty million years to "
                 "rise and are still rising. A complete circuit of the rock "
                 "cycle takes hundreds of millions of years, and the oldest "
                 "crustal rocks found so far are around four billion years "
                 "old — meaning most of the original crust has already been "
                 "recycled out of existence."},
    ],

    "support": [],

    # ⚠️ THE CARD FRONTS ARE LOWERCASE, matching `c10-01`'s, `c10-02`'s and
    # `c10-04`'s, and `terms` above joins on this exact string.
    "vocabulary": [
        {"term": "weathering",
         "definition": "The breaking down of rock where it sits, by frost, "
                       "by water in cracks, or by slightly acidic rain "
                       "reacting with its minerals.",
         "note": "Nothing is carried anywhere. That is the next process."},
        {"term": "erosion",
         "definition": "The picking up and carrying away of the fragments "
                       "weathering has produced, by water, wind or ice.",
         "note": "Fragments are rounded and sorted by size on the journey."},
        {"term": "deposition",
         "definition": "The dropping of sediment when the water or wind "
                       "carrying it slows down and can no longer hold it.",
         "note": "Heaviest first, layer on layer, oldest at the bottom."},
        {"term": "metamorphism",
         "definition": "The changing of a rock by heat and pressure while it "
                       "stays solid.",
         "note": "Melt it and it is not metamorphic any more. What cools out "
                 "of a melt is igneous."},
        {"term": "rock cycle",
         "definition": "The whole set of routes by which any rock type can "
                       "become any other.",
         "note": "It has no starting point and no fixed direction. Where a "
                 "rock ends up is what decides its route."},
    ],

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure how a rock gets back to being magma?",
              "cta": "Ask about this lesson",
              "anchor": "s-processes"},

    "ks4_becomes": "Plate tectonics as the driver of the cycle, and "
                   "radiometric dating to put real numbers on how long each "
                   "stage takes.",

    "ws": ["analysis-and-evaluation", "scientific-attitudes"],
    "review_state": "draft",
}
