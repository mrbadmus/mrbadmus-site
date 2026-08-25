"""P10 L1 — Magnets and poles (CONTRAST).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p10/p10-01-magnets-and-poles.dc.html`.

Her page wins outright. The two bar magnets on the bench, the five-object
drawer, the three-outcome figure and all four rungs are hers.

── ⚖️ THE LESSON IS A CONTRAST AND THE FOURTH TILE IS THE WHOLE OF IT ──

Three things can happen when you bring a magnet up to something, and only one
of them answers the question you asked. *Does this prove both are magnets*
reads `yes — repulsion proves it` on twelve of the bench's hundred and fifty
states and one of three different `no`s on the other hundred and thirty-eight.
Everything else on the page is in service of that tile.

── ⚖️ THE STATE SPACE, MEASURED RATHER THAN READ OFF HER TABLE ────────

Five objects each side over six gaps is 150 states, and her four branches
divide them:

    nothing   102   and it is not filler — see below
    induced    24   a magnet and a bar of plain steel
    repel      12   the only proof there is
    attract    12   the case that settles nothing

The `nothing` branch has three different things to say, because there are
three different reasons for it, and all three are authored:

    neither object is a magnetic material            24 states
    both are steel and neither is magnetised          6 states
    one of the two is wood or aluminium              72 states

⚠️ **102 STATES OF NOTHING IS THE POINT, NOT A GAP.** `MAG-01` is *all metals
are magnetic*, and the only way to break it is to put a magnet next to
aluminium and watch the arrows stay away. A bench where every combination did
something would confirm the belief it exists to break.

── ⚖️ NO FIGURE FOR THE PULL ON STEEL ────────────────────────────────

Her §8: how strongly a piece of steel magnetises depends on its shape, its
carbon content and what has happened to it, so any coefficient here would be a
guess. All twenty-four magnet-and-steel states print
*"reported in words, not on the scale"* where the other benches print a
number. Same discipline as `p9-02`'s induced attraction.

── ⚖️ THE FOURTH POWER, AND IT IS NOT THE INVERSE SQUARE ─────────────

Two bar magnets end to end fall roughly as the fourth power of the gap, which
is what her model uses and what her legal line declares — and the legal line
also says in terms that this is NOT the inverse-square law that applies to
charges. A student who has just finished P9 is one page away from assuming it
is. Measured over her six gaps: 100.0 at 2 cm, 19.8 at 3, 6.3 at 4, 1.2 at 6,
0.39 at 8, 0.08 at 12.

── ⚠️ MRB-278 · POSITION IS AUTHORED ─────────────────────────────────

Design's two marked rungs, her hook and her commit gate all put the correct
answer at index 0. **Her option TEXT and every correction are verbatim; only
the ORDER moves.** This lesson takes indices 2 (hook), 3 (gate), 1 (rung 1)
and 2 (rung 2). Engine policy, not a register row.

── ⚠️ MRB-177 · ONE LENGTH TELL, REMEDIED AT THE DISTRACTOR ──────────

Her commit gate's correct option is 17 words against a longest distractor of
12 — a tell at the ≥4-word threshold, and a tell on a GATE does most of the
damage a tell can do, because a student who spots the answer never commits and
a belief nobody commits to cannot be confronted. Remedied at the distractor,
which now states its wrong rule completely: *only a magnet can be pushed or
pulled by another magnet*. That is `MAG-04`, and it is minted from this
option. The correct answer is untouched.

── ⚠️ CHILDLINE. NO DRAFT MARKINGS. ─────────────────────────────────

This is the one page in P10 that carries the safeguarding line, and it carries
it in the engine's ruled treatment: small type, bottom edge, above the legal
line, never a callout (MRB-257 audit 6.4).
"""

LESSON = {
    "slug": "magnets-and-poles",
    "title": "Magnets and poles",
    "discipline": "physics",
    "unit": "Magnetism and electromagnetism",
    "family": "CONTRAST",

    "covers": ["KS3.P.MAG.01"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "forces-and-fields", "level": 2}],
    "typical_year": 9,
    "typical_minutes": 60,

    # ⚠️ NOTHING IS ASSUMED. Design's §3: every lesson in P10 teaches from
    # nothing, because a school may run the unit in any order — and this one
    # is the unit's first slot in any case, so the engine's "Before this
    # lesson" card correctly reads that the unit starts here.
    "requires": [],
    "assumes": [],
    "references": [{"unit": "P9", "lesson": "electric-fields"},
                   {"unit": "P9", "lesson": "forces-between-charges"}],
    "ks4_links": [],

    "meta_description": "Every magnet has two ends that behave oppositely — "
                        "and only one of the things a magnet does is proof "
                        "that the other object is a magnet too.",

    "big_question": "Every magnet has two ends that behave oppositely, and "
                    "only one of the things a magnet does is proof that the "
                    "other object is a magnet too.",

    "rail": [
        {"anchor": "s-hook",  "short": "MAGNETS",
         "label": "Turn one round",       "done_when": "committed"},
        {"anchor": "s-bench", "short": "BENCH",
         "label": "Two on a track",       "done_when": "gate_and_a_control"},
        # ⚠️ Design's `DONE` gives this stop the GATE alone, before the bench
        # beside it is finished. The bench marks it through `band_anchor` /
        # `band_at`; `mirrors` would tick it late and would also fail
        # `check_rail_matches_design`, which derives the mirror map from her
        # `isDone()` and finds two different expressions here.
        {"anchor": "s-proof", "short": "PROOF",
         "label": "What counts as proof", "done_when": "gate_committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",       "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Two bar magnets. Same two magnets, two different answers.",
        "prompt": "Slide two bar magnets towards each other along the bench "
                  "and they snap together hard enough to click. Pick one up, "
                  "turn it end for end, put it back and slide them together "
                  "again — and now they fight you, and the harder you push "
                  "the harder they push back.",
        "commit": "Nothing about either magnet changed. What did?",
        # ⚠️ MRB-278 — her order is A B C D with A correct. Position 2 here.
        "options": [
            "One of them lost its magnetism when it was picked up",
            "Turning it round made it stronger, so it could push instead of "
            "pull",
            "Which pole of each magnet is facing the gap",
            "The bench pushed back the second time because of friction",
        ],
        "answer": 2,
        "reveal": "Which poles were facing each other. Each magnet has a "
                  "north-seeking end and a south-seeking end, and turning one "
                  "magnet round swapped which end was in the gap. Unlike "
                  "poles pull together; like poles push apart. Neither magnet "
                  "gained or lost anything — the same two objects give "
                  "opposite answers depending only on how they are turned.",
    },

    "misconceptions": [
        {"id": "MAG-01",
         "statement": "All metals are magnetic.",
         "elicited_by": "track",
         "confronted_by": "s-think"},
        {"id": "MAG-02",
         "statement": "It stuck to the magnet, so it must be a magnet.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "MAG-03",
         "statement": "Turning a magnet round makes it stronger or weaker.",
         "elicited_by": "s-hook",
         "confronted_by": "track"},
        # ⊕ MINTED FROM THE COMMIT GATE'S FOURTH OPTION, which states it as a
        # complete rule: *only a magnet can be pushed or pulled by another
        # magnet*. Separate from `MAG-01`, which is about WHICH MATERIALS, and
        # from `MAG-02`, which is about what attraction PROVES: a student can
        # have both of those right and still expect a plain steel nail to sit
        # there.
        {"id": "MAG-04",
         "statement": "A magnet only does anything to another magnet, so "
                      "plain steel just sits there.",
         "elicited_by": "track",
         "confronted_by": "track"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A magnet has two <strong>poles</strong>, one at each end. "
                 "They are named for what a hanging magnet does: the end that "
                 "swings round to point towards the Earth's north is the "
                 "<strong>north-seeking pole</strong>, written N, and the "
                 "other end is the <strong>south-seeking pole</strong>, "
                 "written S. The names are about direction, not about the "
                 "material — both ends are the same steel."},
        {"type": "explainer",
         "text": "The rule between two magnets is one line. <strong>Like "
                 "poles repel; unlike poles attract.</strong> N against N "
                 "pushes apart, S against S pushes apart, N against S pulls "
                 "together. The two forces are always the same size and in "
                 "opposite directions, whichever magnet is bigger, and they "
                 "get rapidly weaker as the gap grows."},
        {"type": "explainer",
         "text": "Poles always come in pairs. Snap a bar magnet in half and "
                 "you do not get a north piece and a south piece: you get two "
                 "shorter magnets, each with its own N and S. Nobody has ever "
                 "found a single pole on its own."},
        {"type": "explainer",
         "text": "Only some materials feel a magnet at all. <strong>Iron, "
                 "steel, nickel and cobalt</strong> are magnetic materials; "
                 "aluminium, copper, brass, gold, wood and plastic are not, "
                 "and a magnet does nothing to them. A magnet <em>attracts</em> "
                 "a piece of unmagnetised steel, either way round, because "
                 "being near a magnet turns the steel into a weak magnet "
                 "itself for as long as it stays there. That is why "
                 "<strong>attraction proves nothing</strong> about the other "
                 "object, and <strong>repulsion is the only proof</strong> "
                 "that both objects are magnets."},

        # ── #s-bench · two objects on a low-friction track ─────────────
        {"type": "track-pair",
         "id": "track",
         "anchor": "s-bench",
         "eyebrow": "At the bench · two objects on a low-friction track",
         "heading": "Put two things end to end.",
         # ⚠️ A MAP OF NAMED STATES, NOT A STRING — the shell routes a dict to
         # `_progress_readout` and a string to the count formatter, and this
         # readout has no number in it.
         "progress": {"idle": "Change a control to begin",
                      "live": "Three controls live"},
         # ⚠️ HER SECOND SENTENCE IS CUT. It read "Choose what each one is,
         # choose which pole a magnet turns towards the gap, and set how far
         # apart they start" — three clauses naming three controls that are
         # already on screen, which is the bench-intro narration 5A.1 rules
         # out. The set-up sentence stays; it is the only thing here a student
         # cannot see for themselves.
         "lead": "Two objects sit on a track that lets them slide freely.",
         # ⚖️ HER MODEL, EXACTLY. Two bar magnets end to end fall as the
         # FOURTH power of the gap — about right for this arrangement, and
         # deliberately not the inverse square that applies to charges. 100 is
         # the closest pair, which is a setting the slider lands on.
         "k": 100,
         "ref_gap": 2,
         "gap_px": 26,
         "gaps": [2, 3, 4, 6, 8, 12],
         "band_anchor": "s-proof",
         "band_at": 1,
         "start_a": 0,
         "start_b": 2,
         "a_label": "On the left",
         "b_label": "On the right",
         "track_label": "FREE TO SLIDE EITHER WAY",
         "gate": {
             "prompt": "Commit first. A bar magnet is brought near an "
                       "ordinary steel nail, then turned end for end and "
                       "brought near again. What happens?",
             # ⚠️ MRB-278 position 3, and MRB-177 remedied at option D — see
             # the module docstring. Her other three options are verbatim.
             "options": [
                 "It is pulled in once and pushed away once, like two magnets",
                 "It is pulled in once and does nothing the second time",
                 "It does nothing either time, because only a magnet can be "
                 "pushed or pulled by another magnet",
                 "It is pulled in both times, because the magnet magnetises "
                 "the nail whichever way round it is",
             ],
             "answer": 3,
         },
         "gap_control": {"label": "Gap between them", "min": 0, "max": 5,
                         "step": 1, "start": 2, "value": "4 cm"},
         "objects": [
             {"id": "mag-n", "label": "Magnet, N to the gap",
              "short": "BAR MAGNET", "kind": "mag", "near": "N", "far": "S",
              "word": "a bar magnet with its north pole facing the gap"},
             {"id": "mag-s", "label": "Magnet, S to the gap",
              "short": "BAR MAGNET", "kind": "mag", "near": "S", "far": "N",
              "word": "a bar magnet with its south pole facing the gap"},
             {"id": "steel", "label": "Steel bar", "short": "STEEL",
              "kind": "ferro",
              "word": "an unmagnetised steel bar"},
             {"id": "alu", "label": "Aluminium bar", "short": "ALUMINIUM",
              "kind": "non",
              "word": "an aluminium bar"},
             {"id": "wood", "label": "Wooden block", "short": "WOOD",
              "kind": "non",
              "word": "a wooden block"},
         ],
         # ⚠️ FIVE WORDS, READ HIGHEST-FIRST BY THE WIRING. A comparative
         # label over per-state values is COMPUTED, never authored beside
         # them (5A.1) — which is what makes it true at the closest gap and
         # at the widest by construction rather than by somebody remembering.
         "strength_bands": [
             {"at_least": 50, "word": "very strong"},
             {"at_least": 15, "word": "strong"},
             {"at_least": 4, "word": "moderate"},
             {"at_least": 1, "word": "weak"},
             {"at_least": 0, "word": "far too weak to feel"},
         ],
         "readouts": [
             {"id": "verdict", "label": "They", "sub": "—"},
             {"id": "strength", "label": "How strong", "sub": "—"},
             {"id": "gap", "label": "Gap", "sub": "face to face"},
             {"id": "proof",
              "label": "Does this prove both are magnets"},
         ],
         # ⚠️ THE TOKENS, AND THE TWO SHAPES A POLE COMES IN. `{d}` is the gap
         # in cm and `{strength}` the relative figure. A pole is a LETTER in
         # the tile's sub-line — `{anear}` and `{bnear}`, N and S, because
         # that is what is printed on the drawing — and a WORD in the note,
         # `{anearword}` / `{bnearword}` / `{near}`, because "its N pole"
         # reads as an abbreviation in a sentence. `{magside}` and
         # `{steelside}` say which side carries which object, `{magpole}` is
         # the magnet's facing pole in words, and `{inert}` is the phrase for
         # whichever object is not a magnetic material.
         "branches": {
             "nothing_neither": {
                 "verdict": "do nothing",
                 "sub": "no magnet acting on a magnetic material",
                 "proof": "no — nothing happened",
                 "note": "Nothing moves at {d} cm, and nothing moves at any "
                         "other setting either: try the gap and watch the "
                         "arrows stay away. Neither object is a magnetic "
                         "material, so a magnet would do nothing to either of "
                         "them and they certainly do nothing to each other."},
             "nothing_steel": {
                 "verdict": "do nothing",
                 "sub": "no magnet acting on a magnetic material",
                 "proof": "no — nothing happened",
                 "note": "Nothing moves at {d} cm, and nothing moves at any "
                         "other setting either: try the gap and watch the "
                         "arrows stay away. Both are steel, and steel is a "
                         "magnetic material — but neither of them is "
                         "magnetised, so there is nothing to line the other "
                         "one up. Two paper clips ignore each other."},
             "nothing_inert": {
                 "verdict": "do nothing",
                 "sub": "no magnet acting on a magnetic material",
                 "proof": "no — nothing happened",
                 "note": "Nothing moves at {d} cm, and nothing moves at any "
                         "other setting either: try the gap and watch the "
                         "arrows stay away. One of these is {inert}, and a "
                         "magnet does nothing at all to aluminium, wood, "
                         "copper or brass. There is no pull to weaken with "
                         "distance because there was never any pull."},
             "repel": {
                 "verdict": "push apart",
                 "sub": "like poles: {anear} facing {bnear}",
                 "proof": "yes — repulsion proves it",
                 "note": "Both magnets have their {near} pole turned towards "
                         "the gap. Like poles repel, so each is pushed away "
                         "from the other with an equal and opposite force, "
                         "and at {d} cm the strength reads {strength} on this "
                         "scale. Halve the gap and the push grows several "
                         "times over; open it out and it collapses. This is "
                         "the one result on the whole bench that proves both "
                         "objects are magnets, because nothing else in the "
                         "drawer can be pushed away by a magnet."},
             "attract": {
                 "verdict": "pull together",
                 "sub": "unlike poles: {anear} facing {bnear}",
                 "proof": "no — steel does this too",
                 "note": "One magnet offers its {anearword} pole and the "
                         "other its {bnearword}. Unlike poles attract, so "
                         "each is pulled towards the other with an equal and "
                         "opposite force, and at {d} cm the strength reads "
                         "{strength} on this scale — the same size as the "
                         "push between two like poles at the same gap. Only "
                         "the direction changed. Watching this alone you "
                         "could not tell whether the far object was a magnet "
                         "or a plain steel bar."},
             "induced": {
                 "verdict": "pull together",
                 "sub": "the steel is being magnetised",
                 "proof": "no — this is what steel does",
                 "note": "The {magside} object is a magnet with its {magpole} "
                         "pole facing the gap, and the {steelside} one is "
                         "steel that started with no magnetism of its own. "
                         "Being near the magnet lines the steel up, so its "
                         "near face becomes the opposite pole and the two are "
                         "pulled together. Turn the magnet end for end and it "
                         "happens again, because the steel simply lines up "
                         "the other way. That is why this result settles "
                         "nothing: put a magnet there instead and it would "
                         "look exactly the same."},
         },
         # ⚖️ `scale_sub` IS THE ONLY PLACE A FIGURE IS PRINTED, AND IT SAYS
         # WHAT THE FIGURE IS. Never a newton; a position on a declared
         # scale. The magnet-and-steel case never reaches it at all.
         "words": {
             "north": "north",
             "south": "south",
             "left": "left",
             "right": "right",
             "nothing_word": "nothing at all",
             "nothing_sub": "no force either way",
             "steel_word": "a real pull, weaker than magnet on magnet",
             "steel_sub": "reported in words, not on the scale",
             "scale_sub": "{strength} where 100 is the closest pair",
         }},

        # ── #s-proof · one test settles it, the other two do not ───────
        {"type": "mag-band",
         "id": "proof",
         "anchor": "s-proof",
         "eyebrow": "The figure",
         "heading": "One test settles it. The other two do not.",
         "lead": "You are handed a steel bar and told to find out whether it "
                 "is a magnet. You have one magnet you trust. There are three "
                 "things that can happen when you bring them together, and "
                 "only one of them is an answer.",
         "tiles": [
             {"id": "proof-repel", "art": "repel", "accent": True,
              "aria_label": "Two bars pushing apart, with arrows pointing "
                            "away from the gap.",
              "title": "Proof",
              "body": "Only a magnet can be pushed away by a magnet. Nothing "
                      "else does it, so the bar is a magnet."},
             {"id": "proof-attract", "art": "attract",
              "aria_label": "Two bars pulling together, with arrows pointing "
                            "into the gap.",
              "title": "No answer",
              "body": "A magnet pulls a magnet, and it pulls plain steel too. "
                      "Both are still possible, so you have learnt nothing."},
             {"id": "proof-nothing", "art": "nothing",
              "aria_label": "Two bars sitting still with no arrows between "
                            "them.",
              "title": "Different answer",
              "body": "The bar is not a magnetic material at all. It is not "
                      "steel — aluminium and brass both look like this."},
         ],
         "panels": [
             {"label": "A magnet works on",
              "text": "iron · steel · nickel · cobalt"},
             {"label": "A magnet does nothing to",
              "text": "aluminium · copper · brass · gold · wood · plastic"},
         ]},

        {"type": "key-fact", "ref": "repulsion-is-the-only-proof"},

        {"type": "misconception", "id": "think-all-metals",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        # ⚠️ PLAIN `predict`, as everywhere in the key stage except `p9-01`.
        # `#s-think` is NOT a rail stop on any P10 page — Design's third stop
        # is the figure beside the bench — so the section needs no completion
        # contract of its own.
        {"id": "think-all-metals",
         "kind": "predict",
         "demand": "explain",
         "targets": "MAG-01",
         "statements": [
             {"quote": "All metals are magnetic.",
              "targets": "MAG-01",
              "body": [
                  "Most are not. Take a magnet to a handful of metal objects "
                  "and the aluminium drinks can, the copper pipe, the brass "
                  "key and the gold ring all ignore it completely. What "
                  "responds is the iron in things: the steel tin, the fridge "
                  "door, the paper clip, the nail. That is why a recycling "
                  "plant can pull steel cans out of a moving stream of "
                  "rubbish with an electromagnet and leave the aluminium ones "
                  "behind — the separation is free, and it works because "
                  "“metal” and “magnetic” were never the same word.",
              ]},
             {"quote": "It stuck to the magnet, so it must be a magnet.",
              "targets": "MAG-02",
              "body": [
                  "A paper clip sticks to a magnet and a paper clip is not a "
                  "magnet. Being close to a magnet lines up the iron inside "
                  "the clip so that it becomes a weak magnet for as long as "
                  "it stays there, with its near end always turning out "
                  "opposite to the pole facing it — which is why it is pulled "
                  "in whichever way round you hold the magnet. Turn the "
                  "magnet end for end and the clip still comes. A real magnet "
                  "would have pushed away one of those two times, and that "
                  "push is the only thing that settles it.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "repulsion-is-the-only-proof",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Every magnet has a north-seeking and a south-seeking pole, "
                 "and they always come as a pair. Like poles repel and unlike "
                 "poles attract, with equal and opposite forces that weaken "
                 "quickly with distance. A magnet also attracts unmagnetised "
                 "iron, steel, nickel and cobalt either way round — so "
                 "repulsion is the only proof that both objects are magnets."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson's rungs take indices 1
    # and 2. Design put both at 0; her option TEXT and every correction are
    # verbatim and only the ORDER moves.
    "ladder": {
        "recall": {
            "q": "You hold a bar magnet near an unlabelled steel bar and it "
                 "is pulled towards you. You turn the magnet end for end and "
                 "try again, and it is pulled towards you again. What do you "
                 "now know about the bar?",
            "options": [
                "It is a magnet, because it was attracted both times",
                "It is a magnetic material, but whether it is a magnet is "
                "still open",
                "It is not a magnet, because a magnet would have been "
                "attracted only once",
                "It is not a magnetic material, because nothing was pushed "
                "away",
            ],
            "answer": 1,
            "feedback": {
                0: "Being attracted both times is exactly what a plain piece "
                   "of steel does. A magnet would have been pushed away one "
                   "of those two times.",
                2: "A magnet would indeed have been repelled once — but it "
                   "was not repelled, and it was not tested at every angle "
                   "either. Attraction both ways is what unmagnetised steel "
                   "does; it does not rule a weak magnet out on its own.",
                3: "It moved, so it is certainly a magnetic material. A "
                   "non-magnetic bar would have sat there.",
            },
            "title": "Rung 1 · Read the result"},
        "apply": {
            "q": "Two identical bar magnets repel each other across a 4 cm "
                 "gap. They are then moved to a 2 cm gap, still the same way "
                 "round. What happens to the force pushing them apart?",
            "options": [
                "It doubles, because the gap halved",
                "It stays the same, because neither magnet has changed",
                "It grows a great deal — far more than doubling",
                "It falls, because they are being forced closer against the "
                "push",
            ],
            "answer": 2,
            "feedback": {
                0: "The force does not simply track the gap. Halving the gap "
                   "between two bar magnets multiplies the push several times "
                   "over, which is why the last centimetre is the one you "
                   "feel.",
                1: "Neither magnet changed, but the force between two magnets "
                   "depends on the gap as well as on the magnets.",
                3: "Pushing them closer takes effort precisely because the "
                   "force is getting bigger, not smaller.",
            },
            "title": "Rung 2 · Apply the rule"},
        "explain": {
            "q": "A paper clip hangs from the north pole of a magnet. It "
                 "hangs just as well from the south pole. Explain why, using "
                 "the idea of poles.",
            "field_label": "Your explanation",
            "placeholder": "The clip is not a magnet to start with, so…",
            "success": [
                "Says the paper clip is made of steel, which is a magnetic "
                "material.",
                "Says the clip is not a magnet before the magnet arrives.",
                "Says being near the magnet turns the clip into a weak magnet "
                "while it is there.",
                "Says the end of the clip nearest the magnet always becomes "
                "the opposite pole to the one facing it.",
                "Concludes that unlike poles attract in both cases, so the "
                "clip is pulled in whichever end of the magnet is used.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A scrapyard sorts crushed drinks cans. Steel cans and "
                 "aluminium cans go past on the same belt, and a magnet lifts "
                 "one kind out. Say which kind is lifted, and explain how you "
                 "would check that a can that was left behind really is "
                 "aluminium rather than a steel one the magnet missed.",
            "field_label": "Your answer",
            "placeholder": "The magnet lifts the…",
            "success": [
                "Says the steel cans are lifted, because steel is a magnetic "
                "material and aluminium is not.",
                "Says aluminium is a metal that a magnet does nothing to, so "
                "“metal” does not mean “magnetic”.",
                "Describes bringing a magnet to the can that was left behind "
                "and looking for any pull at all.",
                "Says that any attraction at all means it is a magnetic "
                "material and so was missed, not aluminium.",
                "Says that no movement either way round means it is not a "
                "magnetic material.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "A magnet has two poles, north-seeking and south-seeking, and "
                "they cannot be separated: break the magnet and each piece "
                "grows the pole it is missing. Like poles repel and unlike "
                "poles attract, always with equal and opposite forces, and "
                "the force falls away sharply as the gap opens. Only iron, "
                "steel, nickel and cobalt respond at all, and an unmagnetised "
                "piece of any of them is attracted whichever pole you offer "
                "it, because the magnet lines it up first. Attraction is "
                "therefore not evidence. Repulsion is.",

    "stretch": [
        {"id": "cut-it-in-half",
         "type": "explainer",
         "text": "Cut a magnet in half and you get two magnets. Cut those in "
                 "half and you get four. Keep going and the pattern never "
                 "breaks, because the magnetism is not stored in the ends — "
                 "it comes from countless tiny magnetic regions inside the "
                 "metal, all lined up the same way. In an unmagnetised piece "
                 "of steel those regions point in every direction at once and "
                 "cancel out; magnetising it is the act of lining them up, "
                 "and dropping it hard or heating it in a flame knocks them "
                 "out of line again. Nobody has ever isolated a single north "
                 "pole, and physicists have looked hard: a lone pole would be "
                 "a genuinely new object, and searches for one have been "
                 "running for decades."},
        {"id": "very-strong-magnets",
         "type": "explainer",
         "text": "Magnets that are much stronger than the ones in a school "
                 "lab are ordinary items now. The small silver discs in "
                 "headphones, cordless-tool motors, wind turbines and fridge "
                 "catches are usually neodymium, and a disc the size of a "
                 "coin can pinch skin badly between two of them or shatter if "
                 "two are allowed to snap together. The serious hazard is "
                 "swallowing: two or more strong magnets that end up in "
                 "different parts of the gut can pull towards each other "
                 "through the wall between them, and that is a surgical "
                 "emergency rather than something that passes. They are kept "
                 "away from small children for exactly that reason."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "pole",
         "definition": "One of the two ends of a magnet, where its effect is "
                       "strongest. Every magnet has a north-seeking one and a "
                       "south-seeking one, and they always come as a pair: "
                       "break a magnet in half and each piece grows the pole "
                       "it is missing."},
        {"term": "north-seeking pole",
         "definition": "The end of a magnet that swings round to point "
                       "towards the Earth's north, written N. The name is "
                       "about direction, not about the material — both ends "
                       "are the same steel."},
        {"term": "magnetic material",
         "definition": "A material a magnet acts on at all. Iron, steel, "
                       "nickel and cobalt are magnetic materials; aluminium, "
                       "copper, brass, gold, wood and plastic are not, and a "
                       "magnet does nothing to them."},
        {"term": "magnetised",
         "definition": "Turned into a magnet, by lining up the tiny magnetic "
                       "regions inside a magnetic material. Being near a "
                       "magnet magnetises a piece of steel for as long as it "
                       "stays there, which is why the steel is attracted "
                       "whichever way round the magnet is held."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Not sure whether a test proves something is a magnet?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Permanent and induced magnetism, magnetic flux density in "
                   "tesla, and the field patterns that let a motor and a "
                   "generator be explained rather than described.",

    # ⊕ HER SAFEGUARDING BLOCK, IN THE ENGINE'S RULED TREATMENT.
    #
    # Design draws it as a bordered `<aside>` with a mono eyebrow. MRB-257
    # audit 6.4 — ruled by Mide on 19 Aug 2026 — puts the confidential service
    # in `ks3-legal` type at the bottom edge and says in terms that it is
    # NEVER a callout block. Her own §5 describes the placement she wanted in
    # exactly those words: *"inline, small type, bottom edge, above the legal
    # line"*. Her eyebrow becomes the opening condition of the sentence so
    # that no wording of hers is lost; the rest is character for character.
    # ⊕ Integration, 25 Aug 2026 — HER WORDS, CHARACTER FOR CHARACTER: the
    # eyebrow line and the body as she drew them (the body keeps her
    # <strong> around the helpline). The SLOT is still the engine's ruled foot
    # line; see DEPARTURES-P10.md row 14.
    "safeguarding_note": {
        "eyebrow": "If a magnet has been swallowed, or you are worried about "
                   "someone",
        "body": "Swallowing a strong magnet is treated urgently even when the "
                "person seems fine, so it is worth telling an adult straight "
                "away rather than waiting to see — a pharmacist, your GP or "
                "111 will tell you what to do next, and at school the school "
                "nurse or any member of staff can start that. If you would "
                "rather talk to somebody outside all of that, <strong>Childline "
                "is free on 0800 1111</strong>, at any hour, and you do not "
                "have to give your name.",
    },

    "convention_note": "The bench is a teaching model. Strength is reported "
                       "as a relative figure with the closest pair of magnets "
                       "set to 100, and no force in newtons is given anywhere "
                       "on this bench: the equation for the force between two "
                       "magnets is well beyond this stage and any number in "
                       "newtons here would be invented rather than measured. "
                       "The relative figure falls as the fourth power of the "
                       "gap, which is about right for two bar magnets end to "
                       "end and is not the inverse-square law that applies to "
                       "charges. The pull on unmagnetised steel is reported "
                       "in relative words only, never as a figure, because "
                       "how strongly a piece of steel magnetises depends on "
                       "its shape, its carbon content and what has happened "
                       "to it, and any coefficient chosen here would be a "
                       "guess. The force arrows are clamped at both ends, so "
                       "the closest setting and the widest are drawn shorter "
                       "and longer than the figures alone would give. Both "
                       "magnets are treated as identical and equally strong, "
                       "the track as frictionless, and the objects as staying "
                       "where you put them.",

    "ws": ["measurement"],
}
