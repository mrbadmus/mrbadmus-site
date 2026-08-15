# -*- coding: utf-8 -*-
"""B1 L1 — Life processes and what living things are made of (CLASSIFY).

Re-authored 13 Aug 2026 from Claude Design's approved page,
`docs/ks3/design-reference/b1/b1-01-life-processes.dc.html`, measured in
`docs/ks3/b1-inventory/b1-01-life-processes.md`. The page is the specification
and this record reproduces it; where the page contradicts a settled ruling, the
ruling wins and that is noted at the field.

⚠️ THIS RECORD SUPERSEDES the L1 record in `ks3_data/biology_b1_cells.py`, and
it teaches a DIFFERENT LESSON. The old record opened on three dishes (seed /
growing crystal / yeast) and taught the rule as *all seven life processes, with
no exceptions*. Design's page opens on a candle flame and teaches the opposite
shape of rule: the flame scores six of seven and is not alive, the oak seed
scores three of seven and is, and what settles it is cells. Every science-
bearing string below is therefore net-new and needs Mide's examiner gate
(§5.10). `review_state` stays `draft`.

Provenance of the strings. The eight authored constants on the page —
`PROCESSES`, `SPECIMENS`, `SORT_ITEMS`, `SORT_CHOICES`, `RUNGS`, `SELF_RUNGS`,
`RAIL`, `RAIL_SHORT` — were lifted byte-identical by
`tools/extract_design_payload.js` and are transcribed here unaltered; the static
prose (header, KEY FACT, misconception block, `#s-rule`, key note, stretch,
endmatter, safety line) is lifted verbatim from the page's `<x-dc>` template.
Nothing here is paraphrased, and it is not asserted on trust: 258 automated
checks compare every payload string against the extracted JSON and every static
string against the `.dc.html` source, and all 258 pass.

Three strings in this record are NOT Design's and are flagged ⚑ at the field:
the `self_check` on the sorter (MRB-196, ruled 13 Aug — Design's sort reveals
the answers and never asks the student whether they had it, which Law 4
forbids), and the caption for the candle art (Design's art is `aria-hidden` and
carries no caption; §4.10 requires one).

Schema. Uses the §4.8.1 fields (`rail`, `key_facts`, `tutor`, `before_this`,
`ks4_becomes`, `safety_note`) and the §4.8.2 extensions (`figures[].kind`
`css-art` + `art`, `explainer.pills`, `misconception.scorecards` and
`.statements`). Six shapes the page needs that neither §4.8 nor the inventory's
gap list names are marked ⊕NEW at the field, with what they carry: `anchor` on
an id-bearing core block, `phenomenon.options` / `.reveal`, the activity
`eyebrow` / `heading` pair, `test-board.predict`, the ladder's `field_label` /
`placeholder`, and `key_facts[].id` + `{"type": "key-fact", "ref": …}`.
"""

LESSON = {

    # ── identity ─────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py's B1 slot 1 exactly.
    "slug":        "life-processes",
    "title":       "Life processes and what living things are made of",
    "discipline":  "biology",
    "unit":        "cells-and-organisation",
    "family":      "CLASSIFY",

    # ── curriculum position ──────────────────────────────────────────────
    # `covers` is PRESERVED. The inventory (§8b) raised whether the candle
    # framing still owns KS3.B.CELLS.01a — "Cells as the fundamental unit of
    # living organisms: everything alive is built from cells, and nothing else
    # is." It does, and more squarely than the framing it replaces: the whole
    # page turns on that clause, states it as its rule ("Every living thing is
    # made of cells."), and the sorter's third category exists to test its
    # edges. The old three-dishes framing spent most of its length on the seven
    # processes, which 01a does not mention. Nothing else is claimed.
    "covers":      ["KS3.B.CELLS.01a"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 40,

    # ── progression edges ────────────────────────────────────────────────
    "requires":    [],
    "assumes":     [],
    # Design's "Connects to" card: two links, no gloss under either. The
    # generator builds that card from `references`, so the two lessons named on
    # the page live here. Both are same-unit rather than cross-discipline,
    # which is a wider use of the field than §4.6 describes — see the report.
    "references":  [
        {"unit": "B1", "lesson": "using-a-microscope"},
        {"unit": "B1", "lesson": "animal-and-plant-cells"},
    ],
    # Still deliberately empty (§10.2): the seven life processes are assumed
    # knowledge at GCSE rather than taught anywhere, so there is no KS4 page to
    # point at. `ks4_becomes` below carries the prose Design puts in the card.
    "ks4_links":   [],

    # ── the teaching payload ─────────────────────────────────────────────
    "big_question": "A candle flame moves, grows, feeds and makes waste. So "
                    "what stops it being alive?",

    # `#s-hook` — ink-dark, two columns: prose + the animated candle, then the
    # commitment. `art` binds the registered CSS art component (§4.8.2).
    "phenomenon": {
        "kind":   "demo",
        "title":  "Watch a candle for a minute",
        "prompt": "It moves. Feed the wick and it grows. It takes in oxygen "
                  "and gives out carbon dioxide, water and soot. Open a door "
                  "and it leans away. Touch a second wick to it and there are "
                  "two flames.",
        "commit": "Is a candle flame alive?",
        "art":    "b1-candle-flame",

        # ⊕NEW `options` + `reveal`. The hook is Law 1 AND Law 4: Design's
        # `.ks3-hook-commit` carries three real `.ks3-option` buttons and a
        # `.ks3-reveal` gated behind them, and today's `r_hook()` renders the
        # commit line alone. R3 holds — there is no `answer` key here and none
        # is wanted; nothing about this reveal is marked, and the options stay
        # re-choosable. Letters A/B/C come from `option_letter(i)`.
        "options": [
            "Yes — it does everything a living thing does",
            "No — but I could not say what is missing",
            "No — and I know what is missing",
        ],
        "reveal": "It is not alive — and the reason is not on that list of "
                  "behaviours. A flame does nearly all of them. What settles "
                  "it is what a flame is <em>made of</em>.",
    },

    # Both register entries survive the re-author with their statements
    # verbatim; only the wiring changes, because the activities they used to
    # name no longer exist. One block kills both — Design's quoted line fuses
    # them ("If it moves and grows, it must be alive.") and the scorecards
    # answer both at once.
    "misconceptions": [
        {"id": "LIFE-01",
         "statement": "If something moves on its own it must be alive, and if "
                      "it never moves it must not be.",
         "elicited_by": "seven-tests",
         "confronted_by": "score-does-not-settle-it"},
        {"id": "LIFE-02",
         "statement": "Doing one of the life processes is enough to count as "
                      "alive — if it grows on its own, it is alive.",
         "elicited_by": "seven-tests",
         "confronted_by": "score-does-not-settle-it"},
    ],

    # Carried for the tutor (§5.9) and the register, NOT rendered: Design's
    # page has no keyword block, and the MRS GREN pills are reference chrome,
    # not vocabulary cards (inventory §5.1). Definitions are unchanged from the
    # superseded record — they are the one part of it the new page does not
    # contradict. Law 7's rendered vocabulary check therefore has no home on
    # this page; raised in the report.
    "vocabulary": [
        {"term": "organism",
         "definition": "A single living thing.",
         "note": "One organism can be one cell, or trillions of them working "
                 "together. You will meet both in this unit."},
        {"term": "cell",
         "definition": "The smallest living unit, and the thing every living "
                       "thing is built from.",
         "note": None},
        {"term": "life process",
         "definition": "One of the seven jobs that every living thing does.",
         "note": "The seven are movement, respiration, sensitivity, growth, "
                 "reproduction, excretion and nutrition. Many people remember "
                 "them by the first letters: MRS GREN."},
    ],

    # §4.8.2 — `kind: "css-art"` plus `art`, the registered art id. The two
    # `needed` figures on the superseded record (`b1-three-dishes`,
    # `b1-everything-is-cells`) are GONE: they belonged to the three-dishes
    # framing and this page renders no figure block, so keeping them would put
    # two sourcing tasks in the diagram manifest for assets nothing shows.
    # ⚑ The caption is mine — Design's art is `aria-hidden="true"` and carries
    # none, and §4.10 requires one.
    "figures": [
        {"id": "b1-candle-flame",
         "kind": "css-art",
         "art": "candle-flame",
         "caption": "A burning candle: a flickering flame above the wick, "
                    "with soot rising from it.",
         "status": "final"},
    ],

    # CLASSIFY's rhythm (§6): lead → decision instrument (commit a prediction,
    # watch resolution) → the reference table → classification drills at rising
    # stakes → ladder, ending with the rule in the student's own words. Design
    # runs it in that exact order and adds two static shells the vocabulary
    # gained on 13 Aug: the key fact between instrument and confrontation, and
    # the rule panel between confrontation and drill.
    #
    # ⊕NEW `anchor`. §4.8.1 A requires every rail `anchor` to name a section
    # the lesson actually emits, and Design's ids (`s-seven`, `s-board`,
    # `s-think`, `s-rule`, `s-sort`) are not derivable from a block type or an
    # activity id. Every id-bearing section carries one, not only the four the
    # rail references — otherwise a hash link from elsewhere lands under the
    # sticky bar.
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # §4.8.2 — `pills` on an explainer. Decorative reference, not a
        # control: no aria-pressed, no cursor, no hover (§7.7).
        {"type": "explainer", "id": "the-seven", "anchor": "s-seven",
         "text": "Biologists describe living things by seven life processes. "
                 "Their initials spell <strong>MRS GREN</strong>.",
         "pills": [
             {"initial": "M", "label": "Movement"},
             {"initial": "R", "label": "Respiration"},
             {"initial": "S", "label": "Sensitivity"},
             {"initial": "G", "label": "Growth"},
             {"initial": "R", "label": "Reproduction"},
             {"initial": "E", "label": "Excretion"},
             {"initial": "N", "label": "Nutrition"},
         ]},

        # The flagship. `check` and not `practical`: Design draws `#s-board` as
        # a light `.ks3-block`, and the `practical` shell is ink-dark.
        {"type": "check", "id": "seven-tests", "anchor": "s-board"},

        {"type": "key-fact", "ref": "what-the-seven-do"},

        {"type": "misconception", "id": "score-does-not-settle-it",
         "anchor": "s-think", "targets": "LIFE-01"},

        # The rule, in the student's words — CLASSIFY's closing move. Inline in
        # `core` per G5; the `rule` shell is `--ks3-band` on a 3px ink border
        # with no shadow, which is what separates it from a `.ks3-block`.
        {"type": "rule", "anchor": "s-rule",
         "eyebrow": "What settles it",
         "statement": "Every living thing is made of cells.",
         "cards": [
             {"term": "A candle flame",
              "gloss": "Hot glowing gas. No cells, so not alive — whatever it "
                       "does."},
             {"term": "An acorn",
              "gloss": "Cells, packed with a food store and ticking over "
                       "slowly."},
             {"term": "You",
              "gloss": "Around thirty trillion cells, all working at once."},
         ],
         "close": "One cell is enough — yeast manages on one. You are "
                  "somewhere near thirty trillion. A flame has none, so "
                  "however it behaves, it never joins the club."},

        # The drill at rising stakes.
        {"type": "check", "id": "living-once-never", "anchor": "s-sort"},

        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    "stretch": [
        {"type": "explainer", "id": "viruses",
         "text": "A virus is not made of cells, and on its own it does none "
                 "of the seven — it cannot even copy itself without getting "
                 "inside a cell. So most biologists do not count viruses as "
                 "living. A few argue the line is in the wrong place, and "
                 "that argument is still open."},
    ],

    "support": [],   # slot present, content deferred — §11 decision 4

    "activities": [

        # ── the flagship: `#s-board`, "Run the seven tests" ───────────────
        # G3's `test-board`. Four specimens × seven tests = 28 authored
        # verdict+note pairs, each specimen holding its own prediction and its
        # own lamps so all four instruments keep independent progress.
        #
        # R3: nothing here marks the student. The prediction is never scored —
        # "Alive" and "Not alive" on the flame produce identical UI — and the
        # lamps report the SPECIMEN's property, not the student's judgement.
        # The verdict states the truth without referring to what was predicted.
        {"id": "seven-tests", "kind": "test-board",
         "demand": "classify",

         # ⊕NEW `eyebrow` + `heading`. Design's activity shells carry BOTH a
         # scoped eyebrow ("Your turn · test four things", not the generator's
         # fixed "Your turn") and an <h2> above the prompt prose; today's
         # `check` shell promotes the prompt itself to the heading, which would
         # lose one of the two lines.
         "eyebrow": "Your turn · test four things",
         "heading": "Run the seven tests",
         "prompt": "Pick a specimen. Say what you think first. Then work "
                   "through the seven tests and see how far they get you.",

         # ⊕NEW `predict`. Law 4's gate, and G3 does not name it. Choosing
         # either option opens the board for THAT specimen only. Unscored, and
         # (F4, Code's call) it should stay visible in its chosen state rather
         # than being removed from the DOM, so the student can still see what
         # they wagered — an addition inside a component Design drew.
         "predict": {
             "prompt": "Before you test it — alive, or not alive?",
             "options": ["Alive", "Not alive"],
         },

         # MRS GREN. Two initials read "R" (Respiration, Reproduction), which
         # is why `key` exists and is `Rp` for the second: `initial` may
         # repeat, `key` may not.
         "tests": [
             {"key": "M",  "initial": "M", "name": "Movement"},
             {"key": "R",  "initial": "R", "name": "Respiration"},
             {"key": "S",  "initial": "S", "name": "Sensitivity"},
             {"key": "G",  "initial": "G", "name": "Growth"},
             {"key": "Rp", "initial": "R", "name": "Reproduction"},
             {"key": "E",  "initial": "E", "name": "Excretion"},
             {"key": "N",  "initial": "N", "name": "Nutrition"},
         ],

         # Every specimen supplies a result for every test key, in test order.
         # `[bool, note]`: the bool is the specimen's property (lamp lights
         # "Yes" or "No"), the note is what the student reads once tapped.
         "specimens": [
             {"id": "flame",
              "name": "Candle flame",
              "blurb": "A wick, some wax and a supply of air.",
              "results": {
                  "M":  [True,  "It climbs and leans. Nothing is carrying it "
                                "— the hot gas rises."],
                  "R":  [False, "Burning is not respiration. Respiration is a "
                                "controlled set of reactions inside cells."],
                  "S":  [True,  "Open a door and it bends away from the "
                                "draught."],
                  "G":  [True,  "Longer wick, bigger flame."],
                  "Rp": [True,  "Touch a second wick to it and there are two "
                                "flames."],
                  "E":  [True,  "Carbon dioxide, water vapour and soot leave "
                                "it."],
                  "N":  [True,  "Wax and oxygen go in and are used up."],
              },
              "verdict_head": "Six of seven — and still not alive.",
              "verdict_body": "Only respiration fails, and even that one is a "
                              "near miss: a flame really does take in oxygen "
                              "and give out carbon dioxide. Counting "
                              "behaviours cannot settle this.",
              "extra_label": "The eighth test",
              "extra_answer": "No cells.",
              "extra_note": "A flame is hot glowing gas. There is nothing to "
                            "look at under a microscope."},

             {"id": "seed",
              "name": "Oak seed",
              "blurb": "An acorn in a drawer. It has been there four years.",
              "results": {
                  "M":  [False, "Nothing about it moves."],
                  "R":  [True,  "Even dry and still, it respires — slowly "
                                "enough to last for years."],
                  "S":  [True,  "Give it water and warmth and it responds by "
                                "starting to grow."],
                  "G":  [False, "Not while it sits in the drawer."],
                  "Rp": [False, "Not yet. That is an oak tree’s job, "
                                "decades from now."],
                  "E":  [True,  "The carbon dioxide from that slow "
                                "respiration leaves it."],
                  "N":  [False, "It is not taking food in. It is living off "
                                "the store packed inside it."],
              },
              "verdict_head": "Three of seven — and it is alive.",
              "verdict_body": "The seven are things an organism can do across "
                              "its life, not a checklist for this second. A "
                              "sleeping seed scores badly and is still alive.",
              "extra_label": "The eighth test",
              "extra_answer": "Made of cells.",
              "extra_note": "Cut it open, look down a microscope, and there "
                            "they are — packed with a food store."},

             {"id": "robot",
              "name": "Robot vacuum",
              "blurb": "Bumps around the kitchen, finds its charger, empties "
                       "into a bin.",
              "results": {
                  "M":  [True,  "It crosses the room on its own."],
                  "R":  [False, "It runs on a battery. Nothing is broken down "
                                "inside it to release energy."],
                  "S":  [True,  "Sensors find the wall, the stairs and the "
                                "dog."],
                  "G":  [False, "It leaves the factory the size it will "
                                "always be."],
                  "Rp": [False, "A factory makes the next one. It cannot."],
                  "E":  [False, "It empties dust it collected. Excretion "
                                "means waste from your own chemistry."],
                  "N":  [False, "Charging is not feeding — no food goes in "
                                "and nothing is digested."],
              },
              "verdict_head": "Two of seven — not alive.",
              "verdict_body": "It is better than a flame at looking alive and "
                              "worse at scoring. Behaviour is a poor test in "
                              "both directions.",
              "extra_label": "The eighth test",
              "extra_answer": "No cells.",
              "extra_note": "Plastic, metal and a battery. Take it apart and "
                            "you find parts, not cells."},

             {"id": "yeast",
              "name": "Yeast in dough",
              "blurb": "A spoonful of dried yeast, warm water, flour and "
                       "sugar.",
              "results": {
                  "M":  [True,  "Its parts move, and it moves through the "
                                "dough as it grows."],
                  "R":  [True,  "It respires the sugar — that is where the "
                                "bubbles of gas come from."],
                  "S":  [True,  "It responds to warmth and to sugar."],
                  "G":  [True,  "Each cell grows."],
                  "Rp": [True,  "One cell buds into two, over and over."],
                  "E":  [True,  "Carbon dioxide and alcohol leave it as "
                                "waste."],
                  "N":  [True,  "It takes in sugar."],
              },
              "verdict_head": "Seven of seven — alive.",
              "verdict_body": "And every one of those jobs is done by a "
                              "single cell. One cell is a whole organism "
                              "here.",
              "extra_label": "The eighth test",
              "extra_answer": "Made of cells.",
              "extra_note": "One cell each. A teaspoon of dried yeast holds "
                            "thousands of millions of them."},
         ],
         "targets": "LIFE-02"},

        # ── the confrontation: `#s-think` ────────────────────────────────
        # §4.8.2 gives the misconception activity `statements` and
        # `scorecards`. `statements` carries the quoted wrong idea AS DRAWN;
        # `targets` still names the register entry. They differ here — see the
        # report — and the page's line is the one that renders.
        {"id": "score-does-not-settle-it", "kind": "confrontation",
         "demand": "explain",
         "statements": ["If it moves and grows, it must be alive."],
         "prompt": "The flame lit six lamps. The seed lit three. One of them "
                   "is alive and it is not the one with the higher score.",
         "scorecards": [
             {"figure": "6 of 7",
              "title": "Candle flame — not alive",
              "note": "Doing the behaviours is not the same as being alive."},
             {"figure": "3 of 7",
              "title": "Oak seed — alive",
              "note": "The seven are things it <em>can</em> do across its "
                      "life, not a checklist for this second."},
         ],
         "targets": "LIFE-01"},

        # ── the drill: `#s-sort`, "Living, once living, never living" ─────
        # G4's `sort-rows`. Eight rows × three categories. Choices stay freely
        # changeable until the reveal; the reveal button is `disabled` until
        # every row is answered; the evidence lands on all eight rows at once.
        # R3: after the reveal a wrong row's chip is pixel-identical to a right
        # one's. Nothing on the page marks anybody.
        {"id": "living-once-never", "kind": "sort-rows",
         "demand": "classify",
         "eyebrow": "Your turn · sort all eight",
         "heading": "Living, once living, never living",
         "prompt": "Three boxes, not two. Something can be made of cells that "
                   "stopped working a long time ago.",
         "categories": ["Living", "Once living", "Never living"],
         "items": [
             {"id": "moss", "name": "Moss on a wall", "answer": "Living",
              "evidence": "Green, growing, made of cells that are working "
                          "right now."},
             {"id": "yeast", "name": "Yeast in bread dough",
              "answer": "Living",
              "evidence": "Single cells, feeding on sugar and budding into "
                          "new ones."},
             {"id": "woodlouse", "name": "A woodlouse under a stone",
              "answer": "Living",
              "evidence": "Moves, feeds, breeds — and it is built from "
                          "cells."},
             {"id": "spoon", "name": "A wooden spoon",
              "answer": "Once living",
              "evidence": "Wood is the leftover walls of tree cells. The "
                          "cells themselves died when the tree was cut."},
             {"id": "leather", "name": "A leather boot",
              "answer": "Once living",
              "evidence": "Skin is a tissue. Tanning preserves it long after "
                          "the animal has gone."},
             {"id": "coal", "name": "A lump of coal",
              "answer": "Once living",
              "evidence": "Squashed plants from around three hundred million "
                          "years ago. No cells left, but it was part of "
                          "living things."},
             {"id": "granite", "name": "A granite pebble",
              "answer": "Never living",
              "evidence": "Crystals that grew from cooling molten rock. No "
                          "cells were ever involved."},
             {"id": "flame", "name": "A candle flame",
              "answer": "Never living",
              "evidence": "Hot glowing gas doing six of the seven processes "
                          "and made of no cells at all."},
         ],
         "reveal_label": "Show what settles each one",

         # ⚑⊕NEW `self_check` — MRB-196, ruled by Mide 13 Aug 2026. NOT
         # Design's; this content is mine and needs the gate.
         #
         # Why it exists: Design's sorter reveals all eight answers and never
         # asks the student whether they had them. The student commits and
         # never finds out, which Law 4 forbids, and eight items is a lot to
         # self-mark unaided with nothing on the page telling you to. R3 rules
         # out the page marking it. So the student is asked, and answers for
         # themselves.
         #
         # It renders only once the evidence is showing — before that there is
         # nothing to compare against. There is no `answer` key and there must
         # never be one: no green, no red, no tone tokens, nothing on any
         # option button and nothing on any row. The page asks; it does not
         # grade. This is the flagship shape for all 15 CLASSIFY lessons.
         "self_check": {
             "question": "Now the answers are showing — how many of your "
                         "eight matched?",
             "options": ["All eight", "Six or seven", "Five or fewer"],
             "note": "Nobody marks this but you. The ones that did not match "
                     "are the ones worth reading again.",
         }},
    ],

    # ── the mastery ladder (§5.8, §5.8.1) ────────────────────────────────
    # Four rungs, all four counting. Rungs 1–2 the page marks: Design's
    # per-option `correction` maps 1:1 onto `feedback`, keyed by option index,
    # and only the wrong options carry one. Rungs 3–4 the student marks: a
    # textarea, then "Check my answer", then the criteria with real checkboxes.
    #
    # ⊕NEW `field_label` + `placeholder` on the self-marked rungs. Design
    # authors both per rung ("Your answer"; "Write two or three sentences." /
    # "Name the test, then say what you would need to see."); `_rung_self()`
    # hard-codes the label as "Write your answer" and emits no placeholder, so
    # without these two keys Design's copy is lost. The placeholder is real
    # scaffolding — it is the only thing on the page that says how long an
    # answer should be.
    "ladder": {
        "recall": {
            "q": "Which one of these is true of every living thing, with no "
                 "exceptions?",
            "options": [
                "It moves from place to place",
                "It is made of one or more cells",
                "It grows bigger every day",
                "It takes in oxygen",
            ],
            "answer": 1,
            "feedback": {
                0: "A tree stays put for two hundred years. Movement inside "
                   "an organism counts, and plenty of living things never "
                   "travel.",
                2: "An acorn in a drawer grows on no day at all, and a "
                   "full-grown adult has stopped. Growth happens somewhere in "
                   "a life, not every day of it.",
                3: "Some organisms respire without oxygen — the yeast in "
                   "dough switches to doing exactly that. Every one of them "
                   "is still made of cells.",
            }},
        "apply": {
            "q": "A robot vacuum crosses the floor on its own, senses the "
                 "stairs and drives to its charger when the battery is low. "
                 "Which statement is right?",
            "options": [
                "It is alive — it does three of the seven",
                "It is not alive — nothing built by people is alive",
                "It is not alive — it is not made of cells",
                "You would have to watch it for longer to say",
            ],
            "answer": 2,
            "feedback": {
                0: "A flame does six and is not alive. Counting processes "
                   "never settles it.",
                1: "True of this one, but not for that reason. Bread dough is "
                   "put together by people and the yeast in it is alive.",
                3: "You would not. Open it up: parts, wiring and a battery. "
                   "No cells, so no.",
            }},
        "explain": {
            "q": "A candle flame moves, grows, gives out waste gases, and can "
                 "start a second flame. Explain why a scientist still says it "
                 "is not alive.",
            "field_label": "Your answer",
            "placeholder": "Write two or three sentences.",
            "success": [
                "I said the flame does several of the seven life processes.",
                "I said the seven processes describe living things — they do "
                "not decide the case on their own.",
                "I said living things are made of one or more cells.",
                "I said the flame is made of hot glowing gas, with no cells.",
            ]},
        "produce": {
            "q": "A probe on Mars finds orange crust that spreads across "
                 "rock, takes in one gas and gives out another. Write the one "
                 "test you would run to settle whether it is alive, and say "
                 "what result would mean “alive”.",
            "field_label": "Your answer",
            "placeholder": "Name the test, then say what you would need to "
                           "see.",
            "success": [
                "I named looking at a sample under a microscope.",
                "I said what I am looking for: cells.",
                "I described what alive would look like — separate units, "
                "each with a boundary around it, repeating.",
                "I said spreading and swapping gases are not enough on their "
                "own, because a chemical reaction can do both.",
            ]},
    },

    # `#s-keynote` — the photographable revision card, ink-dark, last.
    "key_note": "The seven life processes — <strong>MRS GREN</strong> — "
                "describe what living things <em>do</em>. Being made of one "
                "or more cells is what makes a thing <em>living</em>.",

    # ── navigation and framing (§4.8.1) ──────────────────────────────────
    # A · the progress rail. Two authored label sets, neither derivable from
    # the block titles: `short` (≤6 chars, mono, side rail) and `label`
    # (sentence case, top bar). Four stages; the fill is (done)/len(rail).
    #
    # ⚖️ `done_when` names a completion predicate over state the block already
    # owns, and BOTH variants are completion-based with nothing ticked on load
    # (MRB-208, re-affirmed 13 Aug). Design's delivered top bar was scroll-
    # driven and read "4 / 4" for a student who had answered nothing; the
    # ruling wins and the page gets corrected.
    #
    # `all_tests_run` is ONE specimen fully tested, not all four (F3). Design's
    # own predicate — `Object.keys(s.tapped).length >= 7` over a map keyed by
    # specimen id, of which there are four — can never be true, so stage 2's
    # chip stays grey forever. The block's own completion signal ("All seven
    # tested.") fires per specimen, so the rail follows it.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "The flame",
         "done_when": "committed"},
        {"anchor": "s-board",  "short": "TESTS",  "label": "Run the tests",
         "done_when": "all_tests_run"},
        {"anchor": "s-sort",   "short": "SORT",   "label": "Sort all eight",
         "done_when": "all_sorted"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # B · the KEY FACT box. `--ks3-band` ground, 2px ink border, 5px ACCENT
    # offset shadow — the accent shadow is what separates it from a
    # `.ks3-block`. No badge, no letter, no mark: `--ks3-band` is also the
    # chosen-wrong ladder ground (MRB-202) and anything mark-like here would
    # read as a verdict.
    #
    # ⊕NEW `id`, and `{"type": "key-fact", "ref": …}` in `core`. §4.8.1 B makes
    # `key_facts` a top-level list carrying `placement`, and §5.1.1 makes
    # `key-fact` a `core` block type; a `ref` is how this file already joins a
    # `core` block to a top-level record (`hook`→`phenomenon`,
    # `figure`→`figures[]`), so the text lives in one place only.
    "key_facts": [
        {"id": "what-the-seven-do",
         "text": "The seven processes describe what living things <em>do</em>. "
                 "They do not decide whether something is alive.",
         "placement": "top-level",
         "ground": "band",
         "eyebrow": "Key fact"},
    ],

    # C · the tutor card. `anchor` makes the CTA a real in-page link — Design
    # points it at the lesson's own board, which scrolls, asks nobody anything
    # and still reads as a tutor. §8.8's objection (a link to an element no KS3
    # page contains) does not apply to a destination on the same page.
    "tutor": {"prompt": "Stuck on why a flame isn’t alive?",
              "cta": "Ask about this lesson",
              "anchor": "s-board"},

    # D · three prose slots. The first two speak only while `requires` and
    # `ks4_links` are empty; `safety_note` renders ALONGSIDE LEGAL_LINE, never
    # instead of it.
    "before_this":  "Nothing — this is where the unit starts.",
    "ks4_becomes":  "Cell theory, and the argument over where the line around "
                    "“living” belongs.",
    "safety_note":  "Never light a candle to test this at home without an "
                    "adult with you.",

    # ── working scientifically ───────────────────────────────────────────
    "ws": ["scientific-attitudes"],

    # ── governance ───────────────────────────────────────────────────────
    # Every science-bearing string in this record is net-new against the
    # superseded L1 and none of it has been through the examiner gate.
    "review_state": "draft",
}
