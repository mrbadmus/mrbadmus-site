"""P10 L4 — Electromagnets (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p10/p10-04-electromagnets.dc.html`.

Her page wins outright. The scrapyard crane, the coil with its four controls,
the four jobs and all four rungs are hers.

── ⚖️ THREE THINGS MAKE IT STRONGER AND ONE THING MAKES IT DIFFERENT ──

More turns, more current, an iron core — and, unlike every permanent magnet
ever made, a switch. The bench holds all four as separate controls precisely
so that a student can hold three still and move one, which is the only way
`MAG-14` (*more turns means more wire, so more current*) can be broken: turn
the current slider off the question entirely and the field still rises with
the turns.

── ⚖️ NO FORMULA BLOCK, AND THE PRODUCT IS STILL REAL ────────────────

Field goes as turns × current × core, which is a genuine product and would
take MRB-204's triangle cleanly. It gets no block, because at this stage the
quantity has no name and no unit, so the three badges could only be filled
with notation invented for the purpose — which the formula-setup rule forbids.
Her §2 rules it and her own audit agrees. The relationship is stated in words
in the explainer and shown by the two sliders moving independently.

── ⚖️ THE PLASTIC FORMER IS MODELLED AS NO CORE, AND SAYS SO ─────────

Her §9 ruling 4. A control that is DRAWN must be MODELLED (5A.1), and here the
honest model is that it does nothing — so the note says that outright rather
than leaving the student to notice that a number did not move. Its factor and
air's are asserted equal in the drawer, so the ruling cannot be lost to an
edit.

── ⚖️ SWITCHED OFF IS ZERO, AND IS SAID TO BE ZERO ───────────────────

Seventy-five of the hundred and fifty states are switch-open, and the strength
tile reads `zero, not merely small` rather than a number. `MAG-15` is
*switching off leaves a weak field that drains away*, and this is what breaks
it.

── ⚠️ ONE MEASURED CORRECTION, AND IT IS ABOUT THAT SAME SENTENCE ────

Design prints every relative figure to one decimal place. Measured over her
150 states, that makes **nine on-states print `0.0`** for a field that is real
— six in the strength tile (10 turns at 0.2 A and at 0.5 A, and 20 turns at
0.2 A, each with air or with the plastic former) and three in the iron
branch's *"drops to 0.0"* clause. On a page whose own tile insists that zero
means zero, a small field that prints as zero confirms `MAG-15` instead of
breaking it. Below 1 the figure takes two decimals here, which is `p10-01`'s
own convention for its lowest band, and the smallest reading on the bench then
prints `0.01`. A `DEPARTURES-P10.md` row.

── ⚠️ AND ONE BROKEN SEAM ────────────────────────────────────────────

Her core list gives the empty coil the word *"nothing at all — the coil is
empty"*, and two of her sentences interpolate it: *"…or that there is nothing
at all — the coil is empty down the middle"* and *"…40 turns carrying 1.0 A
with nothing at all — the coil is empty holds 4 paper clips"*. Both are
ungrammatical, in fifty of the hundred and fifty states. Under the editor-cut
law a seam has to land as a sentence, so the empty core carries two phrasings
— one that reads after *with*, one that reads before *down the middle* — and
every sentence is a sentence in every state. Her wording is otherwise
untouched.

── ⚖️ THE STATE SPACE ────────────────────────────────────────────────

    5 turns × 5 currents × 3 cores × 2 switch positions   150
      switched off                                         75
      a soft iron core                                     25
      an empty coil                                        25
      a plastic former                                     25

    field  =  turns × current × core factor,   100 at 160 turns, 4.0 A, iron
    clips  =  whole number of clips the field will hold, 0 to 64

── ⚠️ MRB-278 · POSITION IS AUTHORED ─────────────────────────────────

Design's hook, gate and both rungs all put the correct answer at index 0.
**Her option TEXT and every correction are verbatim; only the ORDER moves.**
This lesson takes indices 1 (hook), 2 (gate), 0 (rung 1, hers) and 3 (rung 2).

── ⚠️ NO SAFEGUARDING BLOCK. NO DRAFT MARKINGS. ─────────────────────

Her §5: the MRI paragraph in *Going further* is information about a hazard in
a hospital, not a risk a student is being asked to disclose. Adding the
Childline line here would dilute it where it does mean something, which is
`p10-01`.
"""

LESSON = {
    "slug": "electromagnets",
    "title": "Electromagnets",
    "discipline": "physics",
    "unit": "Magnetism and electromagnetism",
    "family": "MODEL",

    # ⚠️ `.04a`, NOT the parent. Design's §1 gives `MAG.04` to this lesson AND
    # to `p10-05` and records that as needing no notation; `covers` is
    # exactly-once and `verify_ks3` asserts it. The bullet is split at its own
    # comma in `ks3_data/substatements.py`.
    "covers": ["KS3.P.MAG.04a"],
    "touches": ["KS3.WS.MEA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "electricity", "level": 3},
                {"id": "forces-and-fields", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 60,

    # ⚠️ Design's §3: this page defines a pole from nothing. The edge is the
    # honest reading order and nothing is assumed.
    "requires": ["the-earth-is-a-magnet"],
    "assumes": [],
    "references": [{"unit": "P8", "lesson": "current-and-circuits"},
                   {"unit": "P8", "lesson": "series-and-parallel"}],
    "ks4_links": [],

    "meta_description": "A current in a coil makes a magnetic field — so a "
                        "magnet can be built, made stronger three different "
                        "ways, and switched off.",

    # ⊕ Integration, 25 Aug 2026 — HER LEDE, verbatim (Phase 3 revert; the
    # authored question was a paraphrase no row claimed).
    "big_question": "A current makes a magnetic field. Wind the wire into a coil, "
                    "drop a piece of iron down the middle, and you have a magnet "
                    "with a switch.",

    "rail": [
        {"anchor": "s-hook",  "short": "CRANE",
         "label": "The crane lets go", "done_when": "committed"},
        {"anchor": "s-bench", "short": "BENCH",
         "label": "Build one",         "done_when": "gate_and_a_control"},
        # ⚠️ Design's `DONE` gives this stop the GATE alone; the bench marks
        # it through `band_anchor` / `band_at`. See `ks3_art/p10.py`.
        {"anchor": "s-uses",  "short": "USES",
         "label": "Four jobs",         "done_when": "gate_committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",    "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The crane lifts a car. Then it lets go.",
        "prompt": "A scrapyard crane swings a flat disc over a wrecked car, "
                  "lowers it until it touches, and lifts the whole car clear "
                  "of the ground. It swings across to a skip — and the car "
                  "falls off. Nobody unhooked anything and nothing moved on "
                  "the disc.",
        "commit": "How does it let go?",
        # ⚠️ MRB-278 — position 1.
        # ⊕ MRB-297, 1 Sep 2026 — distractor 3 widened. The correct option
        # was the longest by 5, which is a tell below the gate's constant
        # as well as at it. The balance now holds at 1.
        "options": [
            "The disc is turned over so its south pole faces the car instead",
            "The disc is an electromagnet, and the operator switches the "
            "current off",
            "The car is shaken loose, because a magnet cannot be switched",
            "The magnet is worn out by the heavy lift and has to recover "
            "between cars",
        ],
        "answer": 1,
        "reveal": "The disc is a coil of wire with an iron core, and it is "
                  "only magnetic while a current runs through it. The "
                  "operator closes a switch to pick the car up and opens it "
                  "to drop the car. A permanent magnet strong enough to lift "
                  "a car would be a serious problem, because nothing would "
                  "ever get it off again.",
    },

    "misconceptions": [
        {"id": "MAG-13",
         "statement": "The iron core is what makes the magnetism. The coil "
                      "just holds it.",
         "elicited_by": "coil",
         "confronted_by": "s-think"},
        {"id": "MAG-14",
         "statement": "Adding more turns makes it stronger because there is "
                      "more wire, so more current.",
         "elicited_by": "coil",
         "confronted_by": "s-think"},
        {"id": "MAG-15",
         "statement": "Switching off leaves a weak field that drains away.",
         "elicited_by": "coil",
         "confronted_by": "coil"},
        # ⊕ MINTED FROM THE COMMIT GATE'S FIRST OPTION AND RUNG 2'S. Separate
        # from `MAG-15`, and the two are opposite predictions rather than one
        # belief: `MAG-15` expects the field to FADE, this one expects it to
        # STAY for good. A student holding this one has understood that iron
        # can be magnetised and has not met the difference between soft iron
        # and hardened steel, which is what *Going further* is about.
        {"id": "MAG-16",
         "statement": "Once the iron core has been magnetised it stays a "
                      "magnet, so switching off changes nothing.",
         "elicited_by": "coil",
         "confronted_by": "coil"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Any wire with a current in it has a magnetic field around "
                 "it. Around a single straight wire that field is a set of "
                 "rings, and it is weak — you need a sensitive compass right "
                 "against the wire to see it at all."},
        {"type": "explainer",
         "text": "Winding the wire into a <strong>coil</strong> changes that. "
                 "Every turn adds its field to the turns beside it, and "
                 "inside the coil they all point the same way, so the fields "
                 "stack up. A coil like this is called a "
                 "<strong>solenoid</strong>, and the field it makes outside "
                 "itself is the same shape as a bar magnet's: it has a north "
                 "end, a south end and lines that loop from one to the "
                 "other."},
        {"type": "explainer",
         "text": "Putting an <strong>iron core</strong> down the middle makes "
                 "it dramatically stronger. The iron is magnetised by the "
                 "coil's field and adds its own, many times over. Soft iron "
                 "is chosen because it lets go again the moment the current "
                 "stops, which steel does not."},
        {"type": "explainer",
         "text": "Three things make an electromagnet stronger: <strong>more "
                 "turns on the coil</strong>, <strong>more current through "
                 "it</strong>, and <strong>an iron core</strong>. And one "
                 "thing makes it different from every permanent magnet: "
                 "<strong>switch the current off and the magnetism "
                 "goes</strong>. Reverse the current and the north and south "
                 "ends swap over."},

        # ── #s-bench · a coil, a supply and a pile of paper clips ──────
        {"type": "solenoid-bench",
         "id": "coil",
         "anchor": "s-bench",
         "eyebrow": "At the bench · a coil, a supply and a pile of paper clips",
         "heading": "Build one and see what it lifts.",
         "progress": {"idle": "Change a control to begin",
                      "live": "Four controls live"},
         # ⚠️ HER LEAD IS CUT ENTIRELY, and this bench ships without one. It
         # read "Wind as many turns as you like, set the supply, choose what
         # goes down the middle of the coil, and use the switch" — four
         # clauses naming four controls and teaching nothing, which is exactly
         # what 5A.1 says to cut outright rather than trim. `disturbing-a-
         # food-web` ships no intro paragraph and loses nothing; so does this.
         "band_anchor": "s-uses",
         "band_at": 1,
         "turns": [10, 20, 40, 80, 160],
         "currents": [0.2, 0.5, 1, 2, 4],
         # ⚖️ THE CLIPS PER UNIT OF FIELD. The count is the thing a student
         # can see across a room, and it is what makes the strongest setting
         # feel different from the middle one: 0 clips at the bottom, 64 at
         # the top, with the drawing capped at ten marks.
         "clip_rate": 0.004,
         "start_core": 2,
         "start_switch": 1,
         "core_label": "Down the middle",
         "switch_label": "The switch",
         "turns_control": {"label": "Turns on the coil", "min": 0, "max": 4,
                           "step": 1, "start": 2, "value": "40 turns"},
         "current_control": {"label": "Current through it", "min": 0,
                             "max": 4, "step": 1, "start": 2,
                             "value": "1.0 A"},
         "gate": {
             "prompt": "Commit first. An electromagnet is holding a chain of "
                       "paper clips. The switch is opened. What happens to "
                       "the clips?",
             # ⚠️ MRB-278 — position 2.
             "options": [
                 "They stay put, because the iron core is now a permanent "
                 "magnet",
                 "They hold on for a few seconds while the field drains out "
                 "of the core",
                 "They all fall at once, because the field goes when the "
                 "current does",
                 "The bottom ones fall and the top ones stay, because the top "
                 "ones are touching the iron",
             ],
             "answer": 2,
         },
         # ⚠️ TWO PHRASINGS PER CORE, AND BOTH ARE NEEDED. `with_phrase` reads
         # after the word `with`; `down_phrase` reads as the whole object of
         # `there is …`. One string cannot do both jobs for the empty coil,
         # which is what broke fifty of Design's states — see the module
         # docstring.
         "cores": [
             {"id": "air", "label": "Nothing (air)", "factor": 1,
              "with_phrase": "an empty middle",
              "down_phrase": "nothing at all down the middle"},
             {"id": "plastic", "label": "A plastic former", "factor": 1,
              "with_phrase": "a plastic former",
              "down_phrase": "a plastic former down the middle"},
             # ⚠️ THE FACTOR AND THE WORD `twenty-five` IN THE IRON NOTE AND
             # IN THE LEGAL LINE ARE THE SAME CLAIM, SAID TWICE. The figures
             # the student reads are all derived from THIS number, so they can
             # never disagree with each other; only the spelt-out word could
             # drift, and it is here beside the number so that a later edit
             # sees both at once.
             {"id": "iron", "label": "A soft iron core", "factor": 25,
              "with_phrase": "a soft iron core",
              "down_phrase": "a soft iron core down the middle"},
         ],
         "switches": [
             {"id": "off", "label": "Open"},
             {"id": "on", "label": "Closed"},
         ],
         "strength_bands": [
             {"at_least": 40, "word": "very strong"},
             {"at_least": 10, "word": "strong"},
             {"at_least": 1, "word": "moderate"},
             {"at_least": 0.05, "word": "weak"},
             {"at_least": 0, "word": "very weak"},
         ],
         "readouts": [
             {"id": "clips", "label": "Paper clips held", "sub": "—"},
             {"id": "strength", "label": "Field strength", "sub": "—"},
             {"id": "pole", "label": "The right-hand end is"},
             {"id": "core", "label": "What the core is doing"},
         ],
         # ⚠️ `{turns}` is the turn count, `{current}` the current in amps to
         # one decimal, `{clips}` the clip count as a phrase with its own
         # one/many handling, `{rel}` the relative reading, `{bare}` what the
         # same coil would read with the core taken out, `{withiron}` what it
         # would read with one dropped in, and `{corewith}` / `{coredown}` the
         # two phrasings the chosen core carries.
         "branches": {
             "off": {
                 "note": "The switch is open, so no current flows, and there "
                         "is no magnetic field at all — not a weak one, none. "
                         "Every clip has fallen off, and it makes no "
                         "difference that the coil still has {turns} turns on "
                         "it or that there is {coredown}. This is the whole "
                         "difference between an electromagnet and a permanent "
                         "magnet, and it is why a scrapyard crane can put a "
                         "car down."},
             "iron": {
                 "note": "{turns} turns carrying {current} A, with a soft "
                         "iron core, holds {clips} and reads {rel} on this "
                         "scale. Take the core out and leave everything else "
                         "alone and it drops to {bare} — the iron is worth "
                         "about twenty-five times the coil on its own here. "
                         "The right-hand end is a north pole; reverse the "
                         "leads at the supply and it becomes a south pole "
                         "with the same strength."},
             "air": {
                 "note": "{turns} turns carrying {current} A with {corewith} "
                         "holds {clips} and reads {rel} on this scale. There "
                         "is a real field here — a compass at either end "
                         "finds a definite pole — it is simply small. The "
                         "coil is empty, and this is the field the current "
                         "makes on its own. Drop a soft iron core in and the "
                         "same coil at the same current would read about "
                         "{withiron}."},
             "plastic": {
                 "note": "{turns} turns carrying {current} A with {corewith} "
                         "holds {clips} and reads {rel} on this scale. There "
                         "is a real field here — a compass at either end "
                         "finds a definite pole — it is simply small. The "
                         "plastic former does nothing magnetic whatever; it "
                         "is there to wind the wire on, and the reading is "
                         "the same as it is with the coil left empty. Drop a "
                         "soft iron core in and the same coil at the same "
                         "current would read about {withiron}."},
         },
         "words": {
             "no_field": "no field at all",
             "zero_sub": "zero, not merely small",
             "scale_sub": "{rel} where 100 is the strongest setting here",
             "north_end": "a north pole",
             "no_pole": "not a pole — there is no field",
             "core_off": "nothing — no current to respond to",
             "core_iron": "multiplying the coil’s field",
             "core_plastic": "nothing — plastic is not magnetic",
             "core_air": "there is no core",
             "clip_none": "not enough to lift even one",
             "clip_chain": "hanging in a chain",
             "clip_off": "the switch is open",
             "clip_zero": "no clips at all",
             "clip_one": "paper clip",
             "clip_many": "paper clips",
         }},

        # ── #s-uses · four jobs only a switchable magnet can do ────────
        {"type": "mag-band",
         "id": "uses",
         "anchor": "s-uses",
         "eyebrow": "The figure",
         "heading": "Four jobs only a switchable magnet can do",
         "tiles": [
             {"id": "use-crane", "eyebrow": "Scrapyard crane", "accent": True,
              "body": "Lifts a car, then drops it on command. A permanent "
                      "magnet would never let go."},
             {"id": "use-door", "eyebrow": "Door lock",
              "body": "Holds a fire door shut while current flows. Cut the "
                      "power and every door in the building is free — which "
                      "is the point."},
             {"id": "use-relay", "eyebrow": "Relay",
              "body": "A small current pulls an iron arm across and closes a "
                      "second, much bigger circuit. That is how a car starter "
                      "is worked by a key."},
             {"id": "use-speaker", "eyebrow": "Loudspeaker",
              "body": "A coil in a permanent magnet's field, driven by a "
                      "current that changes thousands of times a second, "
                      "pushing a cone in and out."},
         ],
         "panels": [
             {"label": "Stronger",
              "text": "more turns · more current · an iron core"},
             {"label": "Different",
              "text": "switch it off and it stops · reverse the current and "
                      "the poles swap"},
         ]},

        {"type": "key-fact", "ref": "a-current-makes-a-field"},

        {"type": "misconception", "id": "think-the-core-does-it",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-the-core-does-it",
         "kind": "predict",
         "demand": "explain",
         "targets": "MAG-13",
         "statements": [
             {"quote": "The iron core is what makes the magnetism. The coil "
                       "just holds it.",
              "targets": "MAG-13",
              "body": [
                  "The other way round. Take the core out and the coil still "
                  "works — weakly, but it works, and a compass held at either "
                  "end shows a definite north and a definite south. Leave the "
                  "core in and switch off, and a soft iron core does "
                  "essentially nothing. The current makes the field; the iron "
                  "responds to it and multiplies it. You can prove which is "
                  "which on the bench in one move: set an air core and turn "
                  "the current up, and clips lift. Set an iron core and open "
                  "the switch, and they fall.",
              ]},
             {"quote": "Adding more turns makes it stronger because there is "
                       "more wire, so more current.",
              "targets": "MAG-14",
              "body": [
                  "More wire is more resistance, not more current — if "
                  "anything a longer coil on the same supply carries slightly "
                  "less. What extra turns give you is more contributions of "
                  "field in the same place. Each turn produces its own field, "
                  "all the turns are wrapped round the same middle, and "
                  "inside the coil they all point the same way, so twenty "
                  "turns produce roughly twenty times what one does at the "
                  "same current. That is why the bench keeps turns and "
                  "current as separate controls: they are two different "
                  "reasons for the same result.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "a-current-makes-a-field",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "A current in a wire makes a magnetic field. Wound into a "
                 "coil the fields of the turns add together, and the coil's "
                 "field is the same shape as a bar magnet's. More turns, more "
                 "current and an iron core each make it stronger; switching "
                 "the current off removes the magnetism entirely, and "
                 "reversing the current swaps the north and south ends."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. Rungs take indices 0 and 3. Design
    # put both at 0; her option TEXT and every correction are verbatim and
    # only the ORDER moves.
    "ladder": {
        "recall": {
            "q": "An electromagnet holds four paper clips. You want it to "
                 "hold more, and you may change one thing. Which of these "
                 "will not help at all?",
            "options": [
                "Swapping the soft iron core for a plastic one of the same "
                "size",
                "Winding twice as many turns onto the coil",
                "Turning the supply up so twice as much current flows",
                "Putting a soft iron core in where there was only air",
            ],
            "answer": 0,
            "feedback": {
                1: "That does help. Every extra turn adds its own field in "
                   "the same place, so doubling the turns roughly doubles the "
                   "field.",
                2: "That does help. The field a coil makes goes up with the "
                   "current through it.",
                3: "That helps enormously — it is the single biggest change "
                   "available on the bench.",
            },
            "title": "Rung 1 · Choose the change"},
        "apply": {
            "q": "An electromagnet with a soft iron core is holding a chain "
                 "of clips. The switch is opened. What happens?",
            "options": [
                "The clips stay, because the iron core has become a permanent "
                "magnet",
                "The clips stay for a while and then fall as the field slowly "
                "drains away",
                "The clips fall, because the iron core has become a south "
                "pole",
                "The clips fall, because the field goes when the current does",
            ],
            "answer": 3,
            "feedback": {
                0: "Soft iron is chosen precisely because it does not stay "
                   "magnetised. Wrap the coil round hardened steel instead "
                   "and you would have a point.",
                1: "There is nothing stored to drain. The field is made by "
                   "the current, and when the current stops there is no field "
                   "to run down.",
                2: "The clips do fall, but not for that reason. There are no "
                   "poles at all once the current stops — and in any case a "
                   "south pole would attract them just as well as a north "
                   "one.",
            },
            "title": "Rung 2 · Predict the switch"},
        "explain": {
            "q": "Explain why a scrapyard crane uses an electromagnet rather "
                 "than a very strong permanent magnet, and say what the iron "
                 "core in it is for.",
            "field_label": "Your explanation",
            "placeholder": "A permanent magnet would be able to lift the car, "
                           "but…",
            "success": [
                "Says a permanent magnet is always on and could not release "
                "the car.",
                "Says the electromagnet is magnetic only while a current "
                "flows through its coil.",
                "Says opening the switch stops the current, so the field goes "
                "and the car drops.",
                "Says the iron core is magnetised by the coil and makes the "
                "field many times stronger.",
                "Says soft iron is used because it loses its magnetism as "
                "soon as the current stops.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A fire door in a school is held open by an electromagnet on "
                 "the wall, and closes by itself when the fire alarm sounds. "
                 "Explain how the alarm makes the door close, and explain why "
                 "this design is safer than a catch that has to be released "
                 "by someone.",
            "field_label": "Your answer",
            "placeholder": "While there is no fire, a current…",
            "success": [
                "Says a current flows through the electromagnet all the time "
                "the building is normal.",
                "Says that current makes the field that holds the steel plate "
                "on the door.",
                "Says the alarm cuts the current, so the field goes and the "
                "door is released.",
                "Says the door then closes on its own, with no person needed.",
                "Says a power cut or a broken wire also releases it, so the "
                "failure leaves the door safe rather than stuck open.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "A current in a wire produces a magnetic field around it. "
                "Winding the wire into a coil puts many turns round the same "
                "space so their fields add, and the result has the same shape "
                "as a bar magnet's field, with a north end and a south end. A "
                "soft iron core is magnetised by that field and multiplies it "
                "many times over, and lets go again the instant the current "
                "stops. More turns, more current and an iron core each make "
                "the magnet stronger. Switching off removes the magnetism "
                "completely, and reversing the current swaps the ends over — "
                "neither of which a permanent magnet can do.",

    "stretch": [
        {"id": "soft-iron-and-hard-steel",
         "type": "explainer",
         "text": "Soft iron and hard steel are the same element doing two "
                 "different jobs. Soft iron takes on magnetism easily and "
                 "loses it just as easily, which is exactly what a crane or a "
                 "relay needs. Steel is harder to magnetise and hangs on to "
                 "it, which is what a permanent magnet needs. Wrap a coil "
                 "round a steel bar, run a current, switch off, and you have "
                 "made a permanent magnet — one of the standard ways of "
                 "making one."},
        {"id": "the-mri-magnet",
         "type": "explainer",
         "text": "Electromagnets are why an MRI scanner exists. Its main "
                 "magnet is a coil of superconducting wire kept at a few "
                 "degrees above absolute zero, where the wire has no "
                 "resistance at all, so an enormous current runs round it for "
                 "years without a supply and without heating up. The field it "
                 "makes is tens of thousands of times the Earth's, which is "
                 "why nothing steel goes into the room: an oxygen cylinder "
                 "brought too close is pulled in hard enough to kill."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "electromagnet",
         "definition": "A magnet made by running a current through a coil of "
                       "wire, usually wound round an iron core. It is "
                       "magnetic only while the current flows, which is what "
                       "makes it switchable."},
        {"term": "solenoid",
         "definition": "A coil of wire. Every turn adds its field to the "
                       "turns beside it and inside the coil they all point "
                       "the same way, so the field outside is the same shape "
                       "as a bar magnet's."},
        {"term": "core",
         "definition": "Whatever sits down the middle of a coil. A soft iron "
                       "core is magnetised by the coil's field and multiplies "
                       "it many times over; a plastic former does nothing "
                       "magnetic at all and is only there to wind the wire "
                       "on."},
        {"term": "soft iron",
         "definition": "Iron chosen because it takes on magnetism easily and "
                       "loses it again the instant the current stops. "
                       "Hardened steel does the opposite, which is why a coil "
                       "wound round steel is how a permanent magnet is made."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Want to check which end of a coil is north?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "The field pattern round a solenoid worked out from the "
                   "right-hand grip rule, and the transformer, where one "
                   "coil's changing field induces a voltage in another.",

    # ⚖️ MRB-297 · Mide's wording. Approved 1 Sep 2026, recorded on the
    # ticket as `## RULED — 1 Sep 2026`. Not to be edited.
    #
    # ⊕ 1 Sep 2026 — THE TWO P10 RIGS NOW CARRY DIFFERENT NOTES, AND THE
    # DIFFERENCE IS THE POINT. This lesson and `lesson_05_how_a_motor_works.py`
    # used to share ONE note, character for character, and it named a
    # spinning part. An electromagnet rig has no spinning part: `grep -i
    # "spin|rotat|revolv"` over this lesson now returns nothing outside this
    # comment. A note that warns about hardware the rig has not got teaches a
    # student that the note was not written for them.
    #
    # The audit that prompted the safety work had already split the two rigs
    # by hazard — `docs/ks3/audits/2026-08-28-ks3-physics/records/p10.md:312-314`:
    #     "Electromagnet rigs: hot coils, short-circuited cells, low-voltage
    #      supplies only. Motor rigs: bare wires, spinning parts, eye
    #      protection."
    #
    # ⊕ The previous run RAISED this and refused to act on it, and that
    # judgement was right: an approved safety line goes in verbatim or not at
    # all, never adapted. Its refusal is what sent the conflict to Mide. He
    # has now written the split himself and approved both halves, so the
    # spinning-part sentence is gone from here and the short-circuit
    # sentence — this rig's own listed hazard, and the one the old note was
    # missing — stands in its place.
    "safety_note": "Eye protection on. The coil gets hot within a minute, "
                   "so switch off between tries and let it cool. Never "
                   "connect the coil straight across the cell on its own "
                   "— that makes a large current and the wires heat up "
                   "fast. Use only the low-voltage supply your teacher "
                   "gives you.",

    "convention_note": "The bench is a teaching model. The number of paper "
                       "clips is worked out from a simple rule in which the "
                       "field goes up in proportion to the turns and to the "
                       "current, and an iron core multiplies it by a fixed "
                       "factor of twenty-five; a real core's multiplication "
                       "depends on the iron and falls away sharply once the "
                       "iron saturates, so the largest numbers here are "
                       "optimistic. The plastic former is treated as having "
                       "exactly the same effect as no core at all, which is "
                       "right to well within anything a school bench could "
                       "measure. The supply is treated as delivering whatever "
                       "current is set whatever the coil, and the coil is "
                       "treated as not heating up — a real coil at the top "
                       "settings would get hot enough to matter within a "
                       "minute. The coil is drawn as eight loops at every "
                       "setting, because the drawing is a symbol and the turn "
                       "count is the readout beside it, and the hanging chain "
                       "is drawn to ten clips however many are held. Field "
                       "strength is a relative figure with the strongest "
                       "setting on this bench set to 100, and no value in "
                       "tesla is given because the unit is beyond this stage.",

    "ws": ["measurement", "analysis"],
}
