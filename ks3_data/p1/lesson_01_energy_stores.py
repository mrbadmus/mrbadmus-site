"""P1 L1 — Energy stores (CLASSIFY).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p1/p1-01-energy-stores.dc.html`.

Her page wins outright. Every scenario, every sort word, every rung and every
line of the two notes below is hers; what this file adds is the engine's shape
and the rulings the record has to carry. Where her `NOTES-P1.md` and her
drawing could have disagreed, the drawing was measured — see §RAIL.

── ⚖️ RULED · WHICH STATUTORY CLAUSE THIS LESSON OWNS ───────────────────

`KS3.P.CIS.02` is a compound bullet:

    "comparing the starting with the final conditions of a system and
     describing increases and decreases in the amounts of energy associated
     with movements, temperatures, changes in positions in a field, in
     elastic distortions and in chemical compositions"

Two genuinely separable teaching ideas, and Design teaches them as two
lessons. The LIST — movements, temperatures, positions in a field, elastic
distortions, chemical compositions — is the set of stores, and it is this
lesson. The COMPARISON of starting with final conditions is `p1-02`, where a
student says which one went down and which went up. Split as `.02a` / `.02b`
in `ks3_data/substatements.py`; the parent's verbatim text is untouched.

⚠️ The split is not cosmetic. Putting the whole bullet here would have the
stores lesson teach a before-and-after comparison before the word *transfer*
has been defined, and would leave `p1-02` with empty `covers`, which §10.2
forbids.

── ⚖️ RULED · EIGHT STORES, AND LIGHT/SOUND/ELECTRICAL ARE NOT AMONG THEM

Design's science flag 1 asks for a ruling and this is it: the eight-store list
is correct and it stays.

The national curriculum bullet names five categories — movement, temperature,
position in a field, elastic distortion, chemical composition. Design's eight
are those five with the field category opened out into its three physically
distinct cases (gravitational, magnetic, electrostatic), plus nuclear. That is
the standard KS3 treatment and the one every GCSE specification then builds
on, so a student who learns it here does not have to unlearn it.

The older "types of energy" vocabulary — light energy, sound energy,
electrical energy — is the thing this lesson exists to correct, not an
alternative it could be rewritten into. `#s-think` is that correction, and
Rungs 3 and 4 both turn on it. If the vocabulary were ever changed back, this
lesson would not need relabelling; it would need deleting.

── ⚖️ RULED · THE FAMILY IS `ENER`, NOT `ENERGY` ───────────────────────

Design's `NOTES-P1.md` §1 says fourteen misconceptions were minted as
`ENERGY-01` to `ENERGY-14` and added to the register on 15 Aug 2026. Neither
half of that is true of this repository: there is no `ENERGY-` id anywhere in
`docs/ks3/misconception-register.md`, and the register carries an explicit,
dated ruling against ever opening one —

    "The reserved prefix was `ENERGY`; Design's C7 delivery proposed `ENER`
     and drew eight entries against it… It is the same family — a wrong idea
     about which way energy travels is the same wrong idea whether it is met
     in a beaker or on a ramp — so the reservation is DISCHARGED rather than
     left standing beside it. A physics lane meeting an energy misconception
     adds to `ENER`; it does not open `ENERGY`."

So P1's mints continue C7's family from `ENER-08`. This lesson opens
`ENER-09` and `ENER-10`. Reported, not escalated: the register's ruling is
explicit and reasoned, and Design's note predates nothing — it simply
describes a register edit that never landed.

── ⚠️ RAIL · FOUR STOPS, AND `s-think` IS ONE OF THEM ───────────────────

Design's audit records that P1–P3 were cut to four rail stops and that "the
remaining nine drop THINK only". That sentence does NOT apply to this lesson,
and the drawing was measured rather than the note trusted: `p1-01` carries
four sections and four rail stops, so nothing was dropped from it at all.

The reason is real rather than an oversight. On `p1-02`–`p1-06`, `s-think` is
a misconception block with a commit, and under the `NOTES-C9` §10 correction
it loses its stop where the lesson has a fuller third section. Here `s-think`
holds the store/pathway SORT — six items a student actually completes — so it
IS the fuller section, and it keeps the stop. Counted, not assumed.

── ⚠️ SHELLS ARE MEASURED OFF DESIGN'S CLASS ATTRIBUTE ──────────────────

    #s-audit   `ks3-block`                    → `check`
    #s-think   `ks3-block ks3-misconception`  → `misconception`

Not inferred from the family name: §4 of the build contract records that B1
got two of six shells wrong by inferring them.

── ⚠️ NO MARKUP IN A RUNG QUESTION ─────────────────────────────────────

`r_ladder` puts a rung's `q` through `t()`, which escapes, so an `<em>` typed
into one ships as visible `&lt;em&gt;`. Rung prose that wants emphasis finds
it in word order instead. (`rich()` is applied to reveals and notes, so markup
is fine there.)
"""

LESSON = {
    "slug":  "energy-stores",
    "title": "Energy stores",
    "discipline": "physics",
    "unit": "Energy transfers",
    "family": "CLASSIFY",

    "covers": ["KS3.P.CIS.02a"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "energy", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 55,

    "requires": [],
    "assumes": [],
    "references": [],
    "ks4_links": [],

    "meta_description": "A ball rolls across a carpet and stops. Nothing took "
                        "its energy away, and energy is never destroyed — "
                        "so where did it go? Learn the eight stores, and the "
                        "one distinction almost everyone gets wrong.",

    "big_question": "Roll a ball across a carpet and it stops. The energy it "
                    "had is gone. Except that nothing in physics is ever "
                    "gone — so where is it?",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "The rolling ball", "done_when": "committed"},
        {"anchor": "s-audit",  "short": "AUDIT",
         "label": "Store audit",      "done_when": "three_ledgers_balanced"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Store or pathway", "done_when": "all_six_sorted"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",   "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The ball stops. The energy does not.",
        "prompt": "A ball rolls across a carpet, slows, and stops. Before, it "
                  "was moving and had energy. After, it is still. Nothing hit "
                  "it and nothing took it away.",
        "commit": "Commit to where the energy went.",
        # ⚑ MRB-177 — the distractors are wrong ACCOUNTS of where it went, at
        # the answer's own length. Design's four are kept verbatim: each is a
        # sentence a real student says, and only the second names a
        # destination rather than an ending.
        # ⊕ AMENDED MRB-297, 31 Aug 2026 — "at the answer's own length" was
        # never true, and was never gated: as delivered the four ran 30 / 59 /
        # 43 / 36 characters, so the correct one was the visibly longest and
        # the hook could be answered without reading any physics. The hook's
        # `answer` index now exists, so `verify_answer_lengths` measures it.
        # THE CORRECT OPTION IS UNCHANGED, byte for byte — the reasoning in
        # it is the teaching. The three distractors were lengthened to its
        # length, so "kept verbatim" no longer holds of them; each is still a
        # wrong account a real student gives. Kept rather than deleted so the
        # provenance is not silently overstated.
        "options": [
            "It was used up by the friction, the way petrol is used up",
            "Into the carpet and the ball, as a tiny rise in temperature",
            "It was absorbed by the ground and destroyed somewhere down there",
            "The ball never really had any energy — moving things store none",
        ],
        # ⊕ MRB-297 — THE HOOK'S ANSWER INDEX, ADDED SO THE GATES CAN SEE IT.
        # P1's eight hooks were the only ones in physics with no `answer`,
        # which is why `verify_answer_lengths` and any position check skipped
        # them: the audit recorded them as "the 8 that do not resolve". They
        # resolve perfectly well — every reveal names one option — so the key
        # is written down rather than left to prose-matching. It is INERT to
        # the page: `data-correct` is emitted only by `_rung_marked`, the
        # ladder renderer, and nothing in build_ks3 reads `phenomenon.answer`.
        "answer": 1,
        "reveal": "Into the carpet and the ball, as a very small rise in "
                  "temperature — a few thousandths of a degree, spread "
                  "across a wide area, far too little to feel but exactly "
                  "enough to account for every joule. A sensitive enough "
                  "thermometer would find it. <strong>“Used up” is "
                  "what it looks like; “moved somewhere hard to "
                  "notice” is what happened.</strong>",
    },

    "misconceptions": [
        {"id": "ENER-09",
         "statement": "Energy gets used up. When something stops, the energy "
                      "it had has been spent and is gone.",
         "elicited_by": "s-hook",
         "confronted_by": "store-audit-ledger"},
        {"id": "ENER-10",
         "statement": "Light, sound and electricity are kinds of energy that "
                      "things store.",
         "elicited_by": "store-pathway-sort",
         "confronted_by": "store-pathway-sort"},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "Energy is not a substance and it is not a fuel. It is a "
                 "<strong>number</strong> — a quantity you can calculate "
                 "for a situation, which comes out the same before and after "
                 "no matter what happened in between. To keep track of that "
                 "number you need somewhere to write it down, and the places "
                 "you write it down are called <em>stores</em>. This lesson "
                 "is about learning the list, and about one distinction that "
                 "trips up almost everyone."},

        # ── #s-audit — the ledger, in the `check` shell.
        {"type": "store-audit", "id": "store-audit-ledger",
         "anchor": "s-audit",
         "demand": "classify",
         "targets": "ENER-09",
         "eyebrow": "The store audit · fill in the ledger",
         # ── ⚖️ SCIENCE · THE LEDGER ASKS WHICH STORE *CHANGES*, NOT WHICH
         # STORE HOLDS. The columns used to read "Filled at the start" /
         # "Filled at the end" over a prompt asking which stores *hold*
         # energy, and the data underneath has only ever encoded which store
         # empties and which store fills. So a physically true tick was
         # marked wrong: thermal on a braking car (warm brakes, warm tyres),
         # chemical on the same car (it has a fuel tank), nuclear on the
         # kettle (every nucleus in it). That marks the lesson's own key
         # fact wrong. The framing is now `changes`, which is what the
         # `before`/`after` lists have always meant.
         "heading": "Which store empties, and which store fills?",
         "prompt": "Pick a scenario. Tick the store that empties and the "
                   "store that fills. Then check.",
         "head_counter": {"format": "{n} of 5 ledgers balanced", "total": 5,
                          "start": 0},
         # ⚖️ THREE OF FIVE, WHICH IS DESIGN'S OWN NUMBER — her
         # `DONE('s-audit')` is `Object.keys(s.solved).length >= 3`. The fifth
         # scenario is the hardest in the unit; requiring all five would make
         # the stop a completion badge rather than a record of the idea
         # landing.
         "ledgers_to_balance": 3,
         "before_title": "Emptied",
         "after_title": "Filled",
         "check_label": "Check the ledger",
         "clear_label": "Clear it",

         "stores": [
             {"id": "kin",   "label": "Kinetic — something moving"},
             {"id": "grav",  "label": "Gravitational — something raised "
                                      "up"},
             {"id": "el",    "label": "Elastic — something stretched or "
                                      "squashed"},
             {"id": "therm", "label": "Thermal — something warm"},
             {"id": "chem",  "label": "Chemical — fuel, food, a "
                                      "battery"},
             {"id": "mag",   "label": "Magnetic — magnets held apart or "
                                      "together"},
             {"id": "est",   "label": "Electrostatic — separated "
                                      "charges"},
             {"id": "nuc",   "label": "Nuclear — inside the nucleus"},
         ],

         "scenarios": [
             {"id": "sc1", "label": "Catapult",
              "text": "A stone is loaded into a stretched catapult and "
                      "released. It flies off horizontally.",
              "before": ["el"], "after": ["kin"],
              "verdict": "Elastic before, kinetic after. Notice the count "
                         "does not go up: the energy in the stretch is the "
                         "energy in the flight. Whoever pulled the catapult "
                         "back put it there, out of their own chemical "
                         "store. A real catapult warms its band a little "
                         "too — we are counting only the stores that "
                         "change enough to matter."},
             {"id": "sc2", "label": "Diver on a board",
              "text": "A diver stands still on a high board, then steps off "
                      "and falls. Judge the moment just before they hit the "
                      "water.",
              "before": ["grav"], "after": ["kin"],
              "verdict": "Gravitational before, kinetic after. Height is "
                         "emptied and speed is filled. The diver was not "
                         "moving at the start and is not raised up at the "
                         "end — the ledger swaps sides completely."},
             {"id": "sc3", "label": "Braking car",
              "text": "A car travelling at 30 mph brakes hard and comes to a "
                      "complete stop.",
              "before": ["kin"], "after": ["therm"],
              "verdict": "Kinetic before, thermal after. This is the hook, "
                         "with a bigger ball: the energy is in the brake "
                         "discs, the tyres and the road, and after a hard "
                         "stop the discs are genuinely too hot to touch. "
                         "<strong>Nothing was used up.</strong>"},
             {"id": "sc4", "label": "Kettle",
              "text": "A kettle is switched on at the wall and boils a litre "
                      "of water.",
              "before": ["chem"], "after": ["therm"],
              "verdict": "Chemical before, thermal after — with the "
                         "chemical store sitting in a fuel somewhere in a "
                         "power station, not in the kettle. The electric "
                         "current is how it got here; it is a pathway, not a "
                         "store, which is the next section of this lesson."},
             {"id": "sc5", "label": "Bouncing ball",
              "text": "A ball is dropped, squashes flat against the floor "
                      "for an instant, and bounces back up. Judge the drop, "
                      "and the moment of maximum squash.",
              "before": ["grav"], "after": ["el", "therm"],
              "verdict": "Gravitational before; elastic and thermal at full "
                         "squash. The thermal one is the interesting tick "
                         "— it is why the ball never returns to the "
                         "height it was dropped from, and why a ball "
                         "squashed and released over and over gets warm."},
         ]},

        {"type": "key-fact", "ref": "never-used-up"},

        # ── #s-think — the sort, in the `misconception` shell.
        {"type": "store-pathway-sort", "id": "store-pathway-sort",
         "anchor": "s-think",
         "demand": "classify",
         "targets": "ENER-10",
         # ⚠️ AUTHORED, NOT LEFT TO THE REGISTER. `r_confrontation` falls back
         # to the register statement only when a block names none of its own,
         # and b1-01 shipped the register's line where Design had drawn a
         # different one. Design's sentence is the one on the page.
         "statements": ["A torch turns electrical energy into light energy "
                        "and sound energy."],
         # ── ⚖️ SCIENCE · "two" IS WRONG, AND IT IS WRONG IN THE DIRECTION
         # THAT UNDOES THE LESSON.
         #
         # Design's sentence reads "…and two of them are not stores at all."
         # Her quote names THREE energy labels — electrical, light and sound
         # — and all three are pathways. Saying two concedes, by arithmetic,
         # that one of the three is a store; the only candidate a student
         # would pick is `electrical`, which is precisely the one her own
         # sort card calls "the one almost everyone gets wrong".
         #
         # So the number contradicts the card sitting ten centimetres below
         # it, and it contradicts the whole point of `#s-think`. Ruled to
         # three under the standing science authority; nothing else in the
         # sentence changes. Reported, not escalated.
         "prompt": "Every word of that is in common use and three of them "
                   "are not stores at all. Sort each one before you read "
                   "on.",
         "store_label": "A store",
         "path_label": "A pathway",

         "sort_items": [
             {"id": "q1", "name": "Kinetic", "store": True,
              "right": "A store. Pause the film and a moving object still "
                       "has it.",
              "wrong": "This one is a store — pause the film and the "
                       "object is still moving, and you can still calculate "
                       "the number."},
             {"id": "q2", "name": "Light", "store": False,
              "right": "A pathway. Light carries energy from one store to "
                       "another; it is not a place energy sits.",
              "wrong": "Not a store. Light is energy on its way somewhere "
                       "— there is no object holding “light "
                       "energy” once you pause."},
             {"id": "q3", "name": "Chemical", "store": True,
              "right": "A store. Food, fuel and batteries hold it whether "
                       "or not anything is happening.",
              "wrong": "This one is a store. A battery in a drawer still "
                       "has it a year later."},
             {"id": "q4", "name": "Sound", "store": False,
              "right": "A pathway. Sound is energy travelling through a "
                       "material as a wave.",
              "wrong": "Not a store. Nothing sits holding “sound "
                       "energy” — the sound is the transfer "
                       "itself."},
             {"id": "q5", "name": "Elastic", "store": True,
              "right": "A store. A stretched band holds it indefinitely, "
                       "doing nothing.",
              "wrong": "This one is a store. Leave a bow drawn overnight "
                       "and the energy is still in it."},
             {"id": "q6", "name": "Electrical", "store": False,
              "right": "A pathway. A current is a way of moving energy "
                       "along a wire, not somewhere it rests.",
              "wrong": "Not a store — this is the one almost everyone "
                       "gets wrong. The battery has a chemical store; the "
                       "current is the route out of it."},
         ],

         "settle": [
             "A <strong>store</strong> is somewhere energy sits and can be "
             "counted while nothing is happening. Pause the world and a "
             "stretched spring still has its energy; a hot cup still has its "
             "energy. A <strong>pathway</strong> is a way energy travels "
             "from one store to another. Pause the world and there is no "
             "light in transit to count — light is a journey, not a "
             "destination.",
             "So the torch does not turn electrical energy into light "
             "energy. It empties a chemical store in the battery and fills a "
             "thermal store in the room, and the light and the electric "
             "current are the two routes by which it happens. Saying it "
             "properly takes longer, and it is the difference between "
             "describing what happened and just naming things.",
         ]},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "figures": [],

    "key_facts": [
        {"id": "never-used-up", "placement": "top-level",
         "ground": "card", "eyebrow": "Key fact",
         "text": "Energy is never used up or created. It moves between "
                 "stores, and the total is always the same before and "
                 "after."},
    ],

    # ── ⚖️ MRB-278 · WHERE THE CORRECT ANSWER SITS ──────────────────────
    #
    # Design put the correct option FIRST in both marked rungs. Her pages
    # predate the 21 Aug 2026 ruling, and that ruling exists because of
    # exactly this: all 58 marked rungs on every Chemistry page had the answer
    # at index 0, so pressing button one scored full marks without reading,
    # and index 3 was correct 0 times in 174 rungs key-stage-wide.
    #
    # The gate wants no index over half and no index unused, per unit. P1's
    # eight lessons carry sixteen marked rungs, planned 4/4/4/4; this lesson
    # takes indices 0 and 2.
    #
    # ⚠️ WHAT MOVED IS THE ORDER OF FOUR BUTTONS AND NOTHING ELSE. Every
    # option's words and every distractor's feedback are Design's, verbatim.
    # Reordering is not overriding her drawing — a rung is not a picture,
    # and the alternative is shipping a unit a student can beat without
    # reading.
    "ladder": {
        "recall": {
            "q": "A stretched elastic band holds energy in which store?",
            "options": [
                "Elastic",
                "Kinetic",
                "Chemical",
                "Elastic energy is not a store, it is a pathway",
            ],
            "answer": 0,
            "feedback": {
                1: "Kinetic means moving. A stretched band held still is not "
                   "moving and still has the energy.",
                2: "Chemical means fuel, food or a battery — energy "
                   "released by rearranging particles.",
                3: "It is a store: pause everything and the stretched band "
                   "still holds it.",
            }},
        "apply": {
            "q": "A cyclist freewheels down a hill and then brakes to a stop "
                 "at the bottom. Which describes the energy correctly?",
            "options": [
                "The energy is gradually used up by the brakes until "
                "none remains",
                "Gravitational becomes kinetic on the way down, then the "
                "kinetic energy disappears",
                "Gravitational store empties, kinetic fills, then thermal "
                "fills as the brakes warm",
                "The cyclist creates new kinetic energy by pedalling on "
                "the way down",
            ],
            "answer": 2,
            "feedback": {
                0: "Nothing uses energy up. The brake discs are measurably "
                   "hotter afterwards, and that is where it is.",
                1: "It goes into a thermal store in the brakes, the tyres "
                   "and the air. Disappearing is not something energy does.",
                3: "They are freewheeling. And even if they pedalled, they "
                   "would be emptying a chemical store, not creating "
                   "anything.",
            }},
        "explain": {
            # ⚠️ No markup in a rung question — `r_ladder` escapes it.
            "q": "A wind-up torch is cranked for thirty seconds and then "
                 "shines for two minutes. Describe the energy stores at the "
                 "start, in the middle and at the end — and say which "
                 "parts of the description are pathways rather than stores.",
            "field_label": "Your description",
            "placeholder": "The person cranking has a chemical store…",
            "success": [
                "Starts with a chemical store in the person turning the "
                "handle.",
                "Names the store filled by cranking — elastic in the "
                "spring, or kinetic in a flywheel.",
                "Ends with a thermal store in the room and the torch.",
                "Identifies light as a pathway, not a store.",
                "Identifies the electric current as a pathway, not a store.",
            ]},
        "produce": {
            "q": "A student says: “A phone battery holds electrical "
                 "energy, and when it goes flat that energy has been used "
                 "up.” Two things in that sentence are wrong. Correct "
                 "both.",
            "field_label": "Your correction",
            "placeholder": "A battery does not hold electrical energy "
                           "because…",
            "success": [
                "Says the battery holds a chemical store, not an electrical "
                "one.",
                "Says electricity is a pathway — a way energy travels "
                "out of the battery.",
                "Says the energy is not used up when the battery goes flat.",
                "Says where it has gone — thermal stores in the phone "
                "and the room, and out as light and sound.",
                "Says the total energy is the same before and after.",
            ]},
    },

    "key_note": "Energy is a number you can calculate for a situation. It is "
                "held in stores — kinetic, gravitational, elastic, "
                "thermal, chemical, magnetic, electrostatic and nuclear "
                "— and it moves between them along pathways. Light, "
                "sound and electric current are pathways, not stores.",

    "stretch": [
        # ⚖️ Design's science flag 4: attributed in substance to Feynman, not
        # quoted. This states the position and names him as its source without
        # putting words in his mouth, which is the form the flag asks for.
        {"type": "explainer", "id": "nobody-has-seen-energy",
         "text": "Nobody has ever seen energy. There is no instrument that "
                 "detects it and no sample of it in any laboratory in the "
                 "world. Richard Feynman made the point to his own students "
                 "as plainly as it can be made: physics has no idea what "
                 "energy <em>is</em>. What it has is a rule for working out "
                 "a number from a situation, and the discovery — the "
                 "whole discovery — is that if you work that number out "
                 "before something happens and again afterwards, you get the "
                 "same answer. Every time. That is not a description of a "
                 "substance; it is a fact about arithmetic that the universe "
                 "turns out to obey. It is also why “where did the "
                 "energy go?” always has an answer."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "energy",
         "definition": "A quantity that can be calculated for a situation. "
                       "Its total is the same before and after any change. "
                       "Measured in joules (J)."},
        {"term": "store",
         "definition": "Somewhere energy sits and can be counted while "
                       "nothing is happening — kinetic, gravitational, "
                       "elastic, thermal, chemical, magnetic, electrostatic "
                       "or nuclear."},
        {"term": "pathway",
         "definition": "A way energy travels from one store to another. "
                       "Light, sound, an electric current and heating are "
                       "pathways, not stores."},
        {"term": "joule",
         "definition": "The unit energy is measured in. Symbol J."},
    ],

    # ⚠️ `body` AND `cta`, NOT `starter`. `r_tutor` reads `prompt`, `body`,
    # `cta` and `anchor` and nothing else; a `starter` key was authored here
    # first and `ks3_key_audit` caught it — content that reaches no student is
    # content that is not on the page.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why electricity is a pathway and not a "
                      "store?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Energy stores and transfers quantified — kinetic "
                   "energy as ½mv², gravitational potential energy as "
                   "mgh, and efficiency as a calculated fraction.",

    "ws": ["scientific-attitudes", "analysis-and-evaluation"],
}
