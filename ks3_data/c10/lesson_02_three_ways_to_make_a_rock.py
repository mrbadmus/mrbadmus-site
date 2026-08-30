"""C10 L2 — Three ways to make a rock (CLASSIFY).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c10/c10-02-three-ways-to-make-a-rock.dc.html`.

── ⚠️ THERE ARE NO AUTHOR'S NOTES FOR THIS LESSON ──────────────────────

`NOTES-C10.md` covers `c10-04` and no other page in the unit. Every science
call below is therefore RULED HERE, from Design's drawing, and written down so
that a reviewer can disagree with a decision rather than having to reconstruct
one. Where Design's drawing and any written text disagreed, the drawing won.

── ONE STATUTORY CLAUSE, AND IT IS A SUB-ID ────────────────────────────

This lesson owns `KS3.C.EA.03a` — the formation of igneous, sedimentary and
metamorphic rocks. The clause split of `KS3.C.EA.03` was ruled in the unit
spine (`ks3_data/c10/__init__.py`) before either lesson existed; the rows land
here, in `ks3_data/substatements.py`, because that file mints lazily and this
is the lesson that needed one. `KS3.C.EA.03b` — the rock cycle — is
`the-rock-cycle`'s and is registered ahead of it.

⚠️ **THIS LESSON COMES BEFORE `the-rock-cycle` AND MUST NOT DEPEND ON IT.**
Nothing here links forward to it, references it or assumes a student has met
the cycle. The three routes are taught as three ways rock is MADE; how a rock
travels between them is the next lesson's whole subject and is not previewed.

── ⚖️ MRB-225 · THE VERSION THAT IS TRUE, NOT THE VERSION THAT IS FAMOUS

Nine rulings. The first four are the ones the whole lesson turns on.

1. **MARBLE IS METAMORPHOSED LIMESTONE. It is not a kind of granite and it
   is not igneous.** The famous version is "marble and granite are both
   posh hard stone", which is a builder's merchant's classification and not
   a scientific one — and the hook kills it in two seconds with dilute acid,
   because marble is calcium carbonate and granite is not. Marble was
   limestone, made from the remains of sea creatures, cooked and squeezed
   until its crystals grew and its fossils were destroyed. `EARTH-06` is
   this belief and the bench is where it dies.

2. **METAMORPHISM DOES NOT MELT THE ROCK, AND THAT IS THE WHOLE
   DISCRIMINATOR.** Melt it and what you get when it cools is igneous. A
   metamorphic rock changed while it stayed solid — its crystals grew,
   re-formed and rotated in place. Every place this lesson could blur it,
   it does not: the reference panel says "without melting", the slate
   verdict says "It never melted — which is exactly what metamorphic
   means", the key fact says it, and the key note says it. `EARTH-07` is
   the belief that metamorphic rock is rock that was melted and re-set.

3. **CRYSTAL SIZE TRACKS COOLING RATE, NOT COMPOSITION.** Slow cooling deep
   underground gives crystals big enough to see; cooling in days at the
   surface gives crystals too small to see. Design's `#s-think` is about
   crystals and her apply rung is about crystal size, so this one is
   load-bearing twice. The apply rung is careful to state that the two
   rocks have the SAME composition, which is what makes cooling rate the
   only remaining answer.

   ⚑ **AND THE BASALT VERDICT IS TIGHTENED FOR IT.** Design's sample 3 ends
   "Same origin as granite, opposite cooling rate." Granite and basalt do
   not in fact have the same composition — read quickly, "same origin"
   invites that — so the built verdict says "Cooled from a melt, exactly
   like the granite, and at the opposite speed", which is the claim that is
   true and is the claim she is making. **A change to Design's words, made
   under MRB-225, and flagged for the science gate.**

4. **SEDIMENTARY GRAINS ARE CEMENTED, NOT GLUED BY HEAT.** Water moving
   through the spaces between buried grains leaves dissolved minerals
   behind, and that mineral is the cement. Nothing is melted and nothing is
   baked. This is also why sandstone soaks up water — the spaces the cement
   did not fill are still there — which is the observation on sample 2.

5. **A FIZZ WITH ACID IDENTIFIES A CARBONATE, NOT A ROCK GROUP.** Limestone
   fizzes and it is sedimentary; marble fizzes and it is metamorphic. The
   hook uses the test to open a question, not to close one, and the bench
   puts the two rocks that share the compound in two different groups on
   purpose. This is the single most useful thing on the page for a student
   who classifies by one observation.

6. **FOSSILS: SEDIMENTARY, AND EFFECTIVELY NOWHERE ELSE.** ⚑ Design's key
   note reads "they are the only rocks that contain fossils" while her own
   reference table reads, for metamorphic, "Rarely, and usually distorted
   beyond recognition". Both cannot stand in one lesson — MRB-225 forbids a
   page retracting itself — so the table's honest version wins and the key
   note is re-worded to "fossils are preserved in them and almost nowhere
   else". The recall rung is untouched: its correct option says the remains
   are buried gently "rather than melted or crushed", and its metamorphic
   correction already carries the nuance in Design's own words.

7. **SLATE'S SHEETS ARE NOT THE MUDSTONE'S LAYERS.** Directed pressure
   rotates the flat mineral grains until they all point the same way, and
   the rock then splits along THAT direction — which can cut clean across
   the original bedding. A student who is told "slate splits along its
   sedimentary layers" has learned something that is usually false and that
   will be corrected at GCSE. The going-further layer says so.

8. **ROCKS ARE GROUPED BY HOW THEY FORMED, NOT BY HOW THEY LOOK.** Colour,
   hardness and weight decide nothing. What decides is texture — whether
   the pieces interlock like a jigsaw or sit as separate grains — plus
   layers, fossils and how the rock breaks. The bench's closing panel is
   this sentence, and it is the rule stated in the student's words that
   CLASSIFY's spine asks for.

9. **"IGNEOUS ROCK NEVER CONTAINS FOSSILS" IS STATED WITHOUT A HEDGE**,
   because at KS3 grain it has none: nothing organic survives silicate melt
   at 700–1200 °C. The reference panel says "never".

── ⚑ §5A · WHAT THE INSTRUMENT COMPUTES, AND WHAT IT IS TOLD ───────────

The bench is told six samples, three groups and two verdict TEMPLATES. It
derives: the number decided, which of the eighteen verdict panels each press
opens, the mid-sentence lower-case name of the group in every one of them,
and — the load-bearing one — the fact that two of the six samples are the same
chemical compound as each other and are in different groups. That claim is
made twice in prose and is NEVER typed as a number: `ks3_art/c10.py` finds the
shared compound in the payload, counts the samples that share one, checks they
span more than one group, and refuses to build if they do not. A payload
edited so that marble and limestone no longer share `calcium carbonate` fails
the build instead of leaving two sentences standing over a set that no longer
supports them.

── ⊖ NO `safety_note`, DELIBERATELY ────────────────────────────────────

Dilute acid is named three times, and every one of them is a REPORTED
observation about a sample somebody else tested — "fizzes with dilute acid" is
a fact about the rock, not an instruction to a student. There is no apparatus,
no method and nothing to run in a room. Recorded rather than assumed, because
an absent note is indistinguishable from an oversight unless somebody writes
down that it was checked.

── ⊖ NO FIGURES, DELIBERATELY ──────────────────────────────────────────

Design draws none, and the drawing the lesson wants — three rocks photographed
close enough to see the texture — is a photograph rather than a diagram. The
bench carries the same information as words a student has to read and decide
on, which is the treatment that makes them look.

── SAFEGUARDING ────────────────────────────────────────────────────────

CHECKED, AND NOTHING IS OWED. The lesson touches no student's body, health,
home or family circumstances. Quarries, mines, roofs and volcanoes appear only
as places rock comes from or ends up; no damage, injury, disaster or named
event is described anywhere, which is the one route by which this topic could
reach a student who has lived through one. Design carried no Childline block
and none is added.

── ⚑ MRB-278 · ANSWER POSITION ─────────────────────────────────────────

Design draws both marked rungs with the correct option at index 0. C10's
ladder corpus already holds `c10-04` at recall=0/apply=2 and `c10-01` at
recall=1/apply=3, so this lesson takes **recall=2 and apply=0** and the unit's
six rungs land two-one-two-one across the four indices with no index empty.
**Only the ORDER moves on the recall rung; no option text is edited by the
move**, which is the treatment every C10 rung has taken.

── ⚑ MRB-177 / MRB-278 · THE DISTRACTORS ARE REWRITTEN, THE ANSWERS ARE NOT

Three option sets on Design's page are length tells, all three in the same
shape the MRB-177 ruling names: the correct option states a RULE and each
distractor states a short wrong REASON.

  · recall rung   13w correct against a longest distractor of 6w
  · apply rung    12w correct against a longest distractor of 6w
  · `#s-think`    14w correct against a longest distractor of 7w

Every one is fixed AT THE DISTRACTOR. Each distractor is re-authored as a
WRONG RULE about rock formation, at the correct answer's own length; not one
correct option is shortened, not one is edited, and the corrections are
rewritten only where the option they answer changed. The hook's four options
are Design's, untouched: the hook is a commitment with a reveal and marks
nothing, and its spread is 6/10/6/6.
"""

LESSON = {
    "slug":  "three-ways-to-make-a-rock",
    "title": "Three ways to make a rock",
    "discipline": "chemistry",
    "unit": "The Earth and its atmosphere",
    "family": "CLASSIFY",

    "covers": ["KS3.C.EA.03a"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "earth-and-universe", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    "requires": ["inside-the-earth"],
    "assumes": [],
    "references": [],
    "ks4_links": [],

    "meta_description": "A granite worktop and a marble statue look alike "
                        "until acid touches them. Read six samples and sort "
                        "them by the one thing that decides it.",

    "big_question": "Every rock on Earth was made in one of three ways, and "
                    "the rock still carries the evidence of which one — if "
                    "you know what to look at.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Granite and marble", "done_when": "committed"},
        # ⊕ MRB-249 — a CONTROLLESS REFERENCE STOP. It is the table a student
        # keeps open while working the bench below it, it takes no commitment
        # of its own, and Design's `DONE('s-table')` is `s.hookChoice !== null`
        # — the hook's own expression, character for character. `mirrors` is
        # what says so, and `docs/ks3/rail-manifest.md` records the same pair.
        # It is a `rule` block, not an instrument, and no family is minted.
        {"anchor": "s-table",  "short": "CLUES",
         "label": "What to look for", "mirrors": "s-hook",
         "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "Six samples",      "done_when": "all_six_decided"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Crystals",         "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",   "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "A kitchen worktop of polished granite, and a statue of "
                 "polished marble. Both hard, both shiny, both full of "
                 "crystals.",
        "prompt": "Look closely and the granite has separate specks of pink, "
                  "white and black locked together like a jigsaw. The marble "
                  "is one colour running in soft swirls. Drip acid on each: "
                  "the granite ignores it and the marble fizzes.",
        "commit": "What does that fizzing tell you about the marble?",
        # ⚑ DESIGN'S FOUR, UNTOUCHED. Nothing here is marked and the reveal is
        # the same for every press, so MRB-177's construct does not arise; the
        # spread is 6 / 10 / 6 / 6 words.
        "options": [
            "That it is softer than granite",
            "That it contains a carbonate, so it was once limestone",
            "That it is an igneous rock",
            "That the acid was too concentrated",
        ],
        "reveal": "That it is a <strong>carbonate</strong> — and that is a "
                  "clue to its history. Marble started life as "
                  "<strong>limestone</strong>, made from crushed shells on a "
                  "sea floor, and was then cooked and squeezed deep in the "
                  "crust until its crystals grew and rearranged. The granite "
                  "crystallised from molten rock and was never anything else. "
                  "Same look, entirely different life story, and the acid "
                  "found the difference in two seconds.",
    },

    "misconceptions": [
        # ⚑ The belief Design's `#s-think` quotes in her own words.
        {"id": "EARTH-05",
         "statement": "If a rock has crystals in it, it must be igneous.",
         "elicited_by": "think-commit-crystals",
         "confronted_by": "think-reveal-crystals"},
        # ⚑ The hook IS the elicitation: two rocks that look alike, and an
        # option offering "it is an igneous rock" on no evidence but the look
        # of it. The bench's closing panel is where it dies, because by then
        # the student has sorted six samples and can be shown that not one of
        # them was decided by colour, hardness or weight.
        {"id": "EARTH-06",
         "statement": "Rocks are grouped by what they look like, so two rocks "
                      "that look alike are the same kind of rock.",
         "elicited_by": "s-hook",
         "confronted_by": "bench-pattern"},
        # ⚑ NO `elicited_by`, DELIBERATELY (audit law 15 / MRB-248). Nothing on
        # this page asks a student to commit to the belief that metamorphic
        # rock was melted and re-set; the bench simply hands them a slate that
        # never melted and a marble that never melted and says so in the
        # verdict of each. Inventing an anchor to fill the column would be the
        # dishonest version. The question bank carries the elicitation instead,
        # at `c10-02-s02` and `c10-02-h01`.
        {"id": "EARTH-07",
         "statement": "Metamorphic rock is rock that was melted and then set "
                      "again as something new.",
         "confronted_by": "bench-samples"},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "Rocks are grouped by <strong>how they formed</strong>, not "
                 "by how they look. There are three routes."},
        {"type": "explainer",
         "text": "<strong>Igneous</strong> rocks cooled from molten rock. "
                 "<strong>Sedimentary</strong> rocks were built up from "
                 "fragments, shells or crystals left behind by water. "
                 "<strong>Metamorphic</strong> rocks were something else "
                 "first, and were changed by heat and pressure without ever "
                 "melting."},

        # ── #s-table — THE REFERENCE BLOCK. No family, no wiring, and a rail
        # stop that mirrors the hook. Design draws a four-column table (type /
        # how it formed / look for / fossils?); the statement panel carries the
        # same four fields per row as term / gloss / chips / limit, which is
        # the component the engine already has and the one C9's four reference
        # stops use.
        {"type": "rule", "anchor": "s-table",
         "eyebrow": "Reference · keep this one open",
         "statement": "What settles it is how the rock formed, and the rock "
                      "still shows it",
         # ⚠️ THE CARD'S FIELD ORDER IS DESIGN'S COLUMN ORDER, and it is why
         # the route is a CHIP rather than the gloss. `_rule_card` emits
         # term → chips → gloss → limit → examples, in that order and in no
         # other; Design's table reads type / how it formed / look for /
         # fossils. Authoring the route as the gloss put the visual clues
         # ABOVE the sentence that says how the rock was made, on all three
         # cards — which quietly inverts the one thing the lesson is for
         # ("grouped by how they formed, NOT by how they look"). One chip per
         # card carries the route as a tag and the four cells land in the
         # order Design drew them.
         "cards": [
             {"term": "Igneous",
              "chips": ["Cooled from molten rock"],
              "gloss": "Interlocking crystals like a jigsaw, and no layers "
                       "anywhere. Large crystals if it cooled slowly deep "
                       "underground; crystals too small to see if it cooled "
                       "fast at the surface.",
              "limit": "Fossils: never. Nothing survives the melt.",
              "examples": "Granite, basalt"},
             {"term": "Sedimentary",
              "chips": ["Settled in layers and cemented"],
              "gloss": "Visible layers, and separate rounded grains rather "
                       "than an interlocking mesh. Often crumbly, and full "
                       "of tiny spaces that soak up water.",
              "limit": "Fossils: yes, and this is the only group in which "
                       "they survive.",
              "examples": "Sandstone, limestone, mudstone"},
             {"term": "Metamorphic",
              "chips": ["Changed by heat and pressure, without melting"],
              "gloss": "Interlocking crystals with bands or swirls running "
                       "through them, or a rock that splits cleanly into "
                       "flat sheets.",
              "limit": "Fossils: rarely, and usually distorted beyond "
                       "recognition.",
              "examples": "Marble, slate"},
         ],
         "close": "Crystal size in an igneous rock is a clock. Big crystals "
                  "mean the melt cooled slowly, deep underground, with time "
                  "for them to grow. Crystals too small to see mean it cooled "
                  "in days at the surface. <strong>Size is set by cooling "
                  "rate, not by what the rock is made of.</strong>"},

        # ── #s-bench — six samples, three groups. Light `ks3-block` in
        # Design's file, so the unit's `_INSTRUMENT_SEGMENTS` map sends it to
        # the `check` shell.
        #
        # ⚠️ NOT ONE NUMBER IN THE PROSE BELOW IS AUTHORED AS A NUMBER. The
        # "two of these six" claim, in both places it is made, is derived in
        # `ks3_art/c10.py` from the samples' own `compound` values and checked
        # against the groups they land in.
        {"type": "rock-bench", "id": "bench-samples", "anchor": "s-bench",
         "eyebrow": "Your turn · six samples",
         "heading": "Read the evidence. Igneous, sedimentary or metamorphic?",
         "demand": "classify",
         "head_counter": {"format": "{n} of {total} decided",
                          "start": 0, "total": 6},
         "samples_to_tick": 6,
         "pattern_anchor": "bench-pattern",

         "groups": [
             {"id": "igneous",     "label": "Igneous"},
             {"id": "sedimentary", "label": "Sedimentary"},
             {"id": "metamorphic", "label": "Metamorphic"},
         ],

         # Two templates, eighteen panels. `{choice}` and `{answer}` are the
         # group's own label, lower-cased at render.
         "verdict_right": "You said {choice} — correct.",
         "verdict_wrong": "You said {choice}. It is {answer}.",

         # ⚠️ `{N}` IS THE CAPITALISED SLOT, and both sentences that quote the
         # count open with it. Neither the count nor the size of the set is
         # ever typed as a number: `ks3_art/c10.py` derives both from the
         # samples' own `compound` values.
         "shared_note": "{N} of these {total} are made of the same compound "
                        "as each other, and they are not in the same group.",

         "samples": [
             {"id": "s1", "code": "Sample 1", "found": "quarry in Cornwall",
              "answer": "igneous",
              "facts": ["Interlocking crystals of pink, white and black, a "
                        "few millimetres across",
                        "No layers of any kind",
                        "Very hard; does not fizz with acid"],
              "why": "Granite. Large interlocking crystals with no layering "
                     "means it crystallised from molten rock, and the size of "
                     "the crystals means it cooled slowly, deep "
                     "underground."},
             {"id": "s2", "code": "Sample 2", "found": "cliff face, Yorkshire",
              "answer": "sedimentary",
              "facts": ["Clear horizontal layers",
                        "Made of rounded grains that rub off on your fingers",
                        "Soaks up water; a drop disappears into it"],
              "why": "Sandstone. Rounded separate grains and visible layers "
                     "mean this was sand carried by water or wind, dropped, "
                     "buried and cemented. The gaps between the grains that "
                     "the cement never filled are why it soaks up water."},
             {"id": "s3", "code": "Sample 3", "found": "near an old volcano",
              "answer": "igneous",
              "facts": ["Dark grey, almost black",
                        "Crystals too small to see even with a hand lens",
                        "Solid all the way through, no layers"],
              "why": "Basalt. Crystals that small mean the melt cooled in "
                     "days rather than millennia — this is lava that reached "
                     "the surface. Cooled from a melt, exactly like the "
                     "granite, and at the opposite speed."},
             {"id": "s4", "code": "Sample 4", "found": "building stone, "
                                                       "quarried",
              "answer": "metamorphic", "compound": "calcium carbonate",
              "facts": ["Interlocking crystals with pale swirls running "
                        "through it",
                        "No fossils, though the surrounding rock is full of "
                        "them",
                        "Fizzes with dilute acid"],
              "why": "Marble. It fizzes because it is calcium carbonate, and "
                     "it sits among fossil-bearing limestone — so it was "
                     "limestone, cooked and squeezed until the crystals grew "
                     "and the fossils were destroyed. It never melted."},
             {"id": "s5", "code": "Sample 5", "found": "coastal cliff",
              "answer": "sedimentary", "compound": "calcium carbonate",
              "facts": ["Pale grey, and shell shapes are visible on the "
                        "broken surface",
                        "Fizzes vigorously with dilute acid",
                        "Soft enough to scratch with a coin"],
              "why": "Limestone. Fossils are the giveaway — no fossil "
                     "survives melting or heavy metamorphism, so a rock full "
                     "of shells was built up gently from the remains of sea "
                     "creatures. Same compound as sample 4, different group."},
             {"id": "s6", "code": "Sample 6", "found": "roof of an old house",
              "answer": "metamorphic",
              # ⚠️ The third bullet used to read "Was originally mudstone"
              # (C10-04, chem audit 25 Aug 2026) — half the answer stated as
              # evidence, and not something anyone can observe on a hand
              # sample. Replaced with the observable clue that points the
              # same way, which is also what the stretch paragraph teaches.
              "facts": ["Dark grey and splits cleanly into thin flat sheets",
                        "Grains far too small to see",
                        "The sheets it splits into cut across the faint "
                        "traces of the original layers"],
              "why": "Slate. Mudstone put under pressure has its flat grains "
                     "rotated until they all point the same way, and the rock "
                     "then splits along that direction. It never melted — "
                     "which is exactly what metamorphic means."},
         ],

         # The panel that opens once every sample has been decided. `{n}` and
         # `{total}` are filled at render from the payload itself.
         "pattern_panel": {
             "title": "Notice which clues actually decided it.",
             "text": [
                 "Not colour, not hardness, not weight. What settled every "
                 "one of those {total} was <strong>texture</strong> — whether "
                 "the pieces interlock like a jigsaw or sit as separate "
                 "grains — plus layers, fossils and how the rock breaks.",
                 "{N} of the samples were the same chemical compound as each "
                 "other and ended up in different groups. A rock is not what "
                 "it is made of. A rock is what happened to it.",
             ]}},

        {"type": "key-fact", "ref": "three-routes"},

        # ⊕ The keyword block is the ENGINE's, not Design's — she drew none on
        # this page, as she drew none on `c10-01`, and both ship one. It is OFF
        # THE RAIL: `docs/ks3/rail-manifest.md` records five stops for this
        # page and `#s-words` is not one of them.
        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. "
                 "If you cannot say it, you do not know it yet.",
         "terms": ["igneous", "sedimentary", "metamorphic", "texture",
                   "cementation"]},

        {"type": "misconception", "id": "think-commit-crystals",
         "anchor": "s-think", "targets": "EARTH-05"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "figures": [],

    "activities": [
        {"id": "think-commit-crystals",
         "kind": "predict",
         "demand": "explain",
         "targets": "EARTH-05",
         "reveal_anchor": "think-reveal-crystals",
         # ⚠️ THE QUOTE IS NOT REPEATED HERE. `r_misconception` already prints
         # the belief as `.ks3-mis-quote` from the register statement, which is
         # Design's own treatment; putting it in the prompt as well ships the
         # sentence twice, eight pixels apart.
         "prompt": "Crystals do form when molten rock cools. Commit before "
                   "you read on.",
         # ⚑ MRB-177 / MRB-278 — the distractors are wrong RULES about where
         # crystals come from, at the answer's own length: 13, 14, 12, 13
         # words. Design's ran 7 / 14 / 7 / 7 with the answer longest, which
         # the predict gate reads as a set a student can solve on shape — and
         # a student who solves it on shape never commits to the belief, so
         # the reveal has nothing to confront.
         "options": [
             "Right — crystals only grow when melted rock cools, so crystals "
             "mean igneous",
             "Wrong — marble and other metamorphic rocks are full of crystals "
             "and never melted",
             "Right, because sedimentary rocks have separate grains and "
             "metamorphic rocks have bands",
             "Wrong — crystals form only where water evaporates, so every "
             "crystal means sedimentary",
         ],
         "reveal": [
             "Marble is packed with interlocking crystals and never melted. "
             "Heat and pressure let the crystals in the original limestone "
             "grow and re-form <em>while the rock stayed solid</em> — the "
             "same thing that happens to slate, and to the bands in a piece "
             "of gneiss.",
             "So crystals narrow the answer to <em>igneous or metamorphic</em> "
             "and no further. What separates the two is the rest of the "
             "evidence: banding, swirls or a rock that splits into sheets "
             "says metamorphic; a random jigsaw of different minerals with no "
             "layering says igneous. <strong>One clue rarely closes a "
             "classification. It just removes an option.</strong>",
         ]},
    ],

    "key_facts": [
        {"id": "three-routes", "placement": "top-level",
         "ground": "card", "eyebrow": "Key fact",
         "text": "Igneous rocks cooled from molten rock and have interlocking "
                 "crystals. Sedimentary rocks are layers of grains and can "
                 "hold fossils. Metamorphic rocks were changed by heat and "
                 "pressure without melting."},
    ],

    "ladder": {
        # index 2 — moved from Design's 0 (MRB-278). No option text is edited
        # by the move; the three distractors were separately rewritten as
        # wrong rules under MRB-177, and the corrections follow them.
        "recall": {
            "q": "Which type of rock can contain fossils, and why only that "
                 "one?",
            "options": [
                "All three, because any rock that buries a shell can hold its "
                "shape",
                "Igneous, because crystals grow around the remains and lock "
                "them in place",
                "Sedimentary, because remains are buried gently in layers "
                "rather than melted or crushed",
                "Metamorphic, because heat bakes the remains hard and "
                "preserves them as stone",
            ],
            "answer": 2,
            "feedback": {
                0: "Only one of the three forms in conditions gentle enough "
                   "to leave a shell or a bone recognisable.",
                1: "Nothing survives molten rock at over 700 °C. Igneous "
                   "rocks never contain fossils.",
                3: "Heat and pressure destroy or distort fossils. Any that "
                   "survive are barely recognisable.",
            }},

        # index 0 — Design's own position, kept, because the unit needed a
        # rung at 0 and this is the one that already had it.
        "apply": {
            "q": "Two igneous rocks have the same composition, but one has "
                 "crystals 5 mm across and the other has crystals too small "
                 "to see. What is the difference between them?",
            "options": [
                "How fast the molten rock cooled — slow cooling grows large "
                "crystals",
                "One is older, and crystals keep growing while the rock sits "
                "underground",
                "One was squeezed harder, and pressure is what makes crystals "
                "grow large",
                "The fine-grained one is sedimentary, because grains that "
                "small must be sand",
            ],
            "answer": 0,
            "feedback": {
                1: "Age has no effect on crystal size. Crystals stop growing "
                   "the moment the melt has solidified.",
                2: "Pressure is what changes a metamorphic rock. In an "
                   "igneous rock the crystal size is set by the cooling rate.",
                3: "Both are described as igneous. Fine-grained igneous rock "
                   "such as basalt is very common.",
            }},

        "explain": {
            "q": "You are handed an unknown rock. Describe the observations "
                 "you would make and explain how each one narrows down which "
                 "of the three types it is.",
            "field_label": "Your method",
            "placeholder": "First I would look for layers…",
            "success": [
                "Looks for layers, which suggest sedimentary.",
                "Looks for fossils, which mean sedimentary.",
                "Checks whether crystals interlock like a jigsaw or sit as "
                "separate grains.",
                "Checks for banding, swirls or splitting into sheets, which "
                "suggest metamorphic.",
                "Says one observation narrows the options and several "
                "together identify it.",
            ]},

        "produce": {
            "q": "A geologist finds a band of marble running through a region "
                 "of limestone, and an old igneous intrusion nearby. Explain "
                 "how the marble got there, and what the arrangement tells "
                 "you about the order of events.",
            "field_label": "Your answer",
            "placeholder": "The marble was originally…",
            "success": [
                "Says the marble was originally limestone.",
                "Says heat from the igneous intrusion changed it.",
                "Says the change happened without the rock melting.",
                "Says the limestone must have formed before the intrusion "
                "arrived.",
                "Says the marble is found closest to the intrusion, where the "
                "heating was strongest.",
            ]},
    },

    # ⚑ RULED (MRB-225, ruling 6 above). Design's version ends "and they are
    # the only rocks that contain fossils", which retracts her own reference
    # table eight blocks higher up.
    "key_note": "Igneous rocks form when molten rock cools and crystallises; "
                "slow cooling underground gives large crystals and fast "
                "cooling at the surface gives small ones. Sedimentary rocks "
                "form when fragments settle in layers and are cemented "
                "together, and fossils are preserved in them and almost "
                "nowhere else. Metamorphic rocks form when existing rock is "
                "changed by heat and pressure without melting.",

    "stretch": [
        {"type": "explainer", "id": "sedimentary-rock-is-history-in-order",
         "text": "Sedimentary rock is history written in order. The layers "
                 "were laid down oldest at the bottom, and each one records "
                 "the conditions of its own moment — a desert leaves rounded "
                 "wind-blown sand, a warm shallow sea leaves shell limestone, "
                 "a swamp leaves coal. Read a cliff face from bottom to top "
                 "and you are reading millions of years in sequence, with the "
                 "fossils in each layer telling you what was alive when it "
                 "formed."},
        {"type": "explainer", "id": "why-slate-roofs-exist",
         "text": "Metamorphic rock is why slate roofs exist. Mudstone "
                 "squeezed under a mountain range has its flat mineral grains "
                 "rotated until they all line up in the same direction, and a "
                 "rock whose grains are all aligned splits cleanly along that "
                 "direction into sheets. Those sheets are <em>not</em> the "
                 "mud's original layers — the split follows the pressure, and "
                 "it can cut clean across the bedding. Nobody designed that "
                 "property; it is a record of the direction the squeeze came "
                 "from, and Welsh slate roofed half of Victorian Britain "
                 "because of it."},
    ],

    "support": [],

    # ⚠️ THE CARD FRONTS ARE LOWERCASE, matching `c10-01`'s and `c10-04`'s,
    # and `terms` above joins on this exact string.
    "vocabulary": [
        {"term": "igneous",
         "definition": "A rock that formed when molten rock cooled and "
                       "crystallised.",
         "note": "Large crystals mean it cooled slowly and deep. Tiny ones "
                 "mean it cooled fast at the surface."},
        {"term": "sedimentary",
         "definition": "A rock built up from fragments, shells or crystals "
                       "that settled in layers and were cemented together.",
         "note": "The only group in which a fossil survives."},
        {"term": "metamorphic",
         "definition": "A rock that was something else first and was changed "
                       "by heat and pressure without melting.",
         "note": "Melt it and it is no longer metamorphic. What cools out of "
                 "a melt is igneous."},
        {"term": "texture",
         "definition": "How the pieces of a rock fit together: interlocking "
                       "like a jigsaw, or separate grains sitting side by "
                       "side.",
         "note": "Texture decides the group. Colour, hardness and weight do "
                 "not."},
        {"term": "cementation",
         "definition": "Minerals left behind by water in the spaces between "
                       "buried grains, sticking them into solid rock.",
         "note": "Nothing is melted and nothing is baked. The spaces the "
                 "cement misses are why sandstone soaks up water."},
    ],

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still unsure how marble and limestone are related?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    "ks4_becomes": "Mineral identification, grain size and cooling rate, and "
                   "using rock sequences to date events in the Earth's "
                   "history.",

    "ws": ["analysis-and-evaluation", "scientific-attitudes"],
    "review_state": "draft",
}
