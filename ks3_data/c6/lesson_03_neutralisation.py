"""C6 L3 — Neutralisation (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c6/c6-03-neutralisation.dc.html` (608 lines), and
her author's notes `docs/ks3/design-reference/c6/NOTES-C6.md` §1, §3, §4, §5
flags 6 and 8, §6 (`ACID-05`, `ACID-06`) and §7.

── THE INSTRUMENT IS THE LESSON ────────────────────────────────────────

NOTES-C6 §3 says it outright: "a drop-by-drop titration with a live pH readout
and a bar trace. The instrument is the lesson: the trace makes the cliff
visible." Everything on this page exists to put one shape in front of a
student — flat, cliff, flat — and to put it there as something they produced
rather than as a claim in a paragraph.

⚑ **SCIENCE FLAG 6, RULED AND KEPT EXACTLY.** The curve is
1,1,1,1,2,2,2,2,3,3,7,11,11,12,12,12,13,13,13,13,13 — integers, equivalence at
drop 10, shaped correctly for a strong acid with a strong alkali. It is not
smoothed, no value is rounded and nothing the instrument computes from it is
hard-coded anywhere on this page.

**AND NOTHING ON THE PAGE IS ALLOWED TO GET AHEAD OF IT.** Design's own page
hard-codes "the first nine drops", "the tenth" and `seenJump: next >= 11` in
three separate places, so a curve pointed at a different acid would leave three
sentences describing a shape no longer on screen. `r_titration_dial` derives
every one of those from the curve at build time — the equivalence point, the
drop the payoff panel opens on, the colour of the beaker at every position, the
height of all twenty-one bars — and asserts four things that ARE the lesson:

  1. the curve only ever rises,
  2. exactly one reading is 7 ("neutral is a single point you cross"),
  3. the step across it is at least four pH units (a cliff, not a climb),
  4. every authored state agrees with what its own pH says.

A future pass that smooths the curve fails the build rather than shipping a
page whose closing paragraph describes something that is no longer true.

── `KS3.C.CR.07` AND `KS3.C.CR.04`, AND WHY ONLY ONE IS `covers` ───────

NOTES-C6 §1 gives this lesson both bullets, and it is right about the teaching:
`CR.04` defines acids and alkalis IN TERMS OF neutralisation, which is this
reaction, and `CR.07` is the reaction itself.

`validate()` rule 4 fails a statement owned twice, and `acids-and-alkalis`
already owns `CR.04` because it is the lesson that defines them. Repetition
across lessons is right and is expressed by `touches`, which is not an
ownership claim and is not gated. So `touches` names `CR.04`, and it is owned
once by the lesson that defines the two words.

`CR.07` is a different problem and it is not solved here either. Five C6
bullets against six C6 lessons is an arithmetic conflict between `validate()`
rules 3 and 4, and the architecture's mechanism for it is a minted clause —
which the commander's brief forbade this lane to write. So `covers` names
`KS3.C.CR.07a`, `making-a-pure-dry-salt` names `KS3.C.CR.07b`, **neither
clause exists yet**, and the block that mints them is written out for the
commander rather than spliced in here. See that lesson's docstring for the
full reasoning.

── SCIENCE FLAGS ───────────────────────────────────────────────────────

⚑ Flag 8 — "toothpaste is mildly alkaline", in use 3. KEPT. It is true of most
formulations, the answer says "mildly alkaline" rather than "alkaline", and it
credits the scrubbing as well so the chemistry is not made to carry the whole
claim.

⚑ FONT LAW. The word equation on this page is drawn by the platform's own
`r_equation`, which puts a real SVG arrow between the two halves and holds the
WORD it means in `arrow`. There is no field on that component an author could
type U+2192 into, and it raises if one appears. Every other mention of the
equation — the key fact, the key note, rung 1 — says **makes**, which is
Design's own 21 August font-law pass.
"""

# ── the curve (Design's `CURVE`) ────────────────────────────────────────
#
# ⚑ FLAG 6. Twenty-one readings for twenty-one positions, 0 through 20 drops.
# Index IS the drop count. Every number the page prints about this run is read
# off this list at build time; see the module docstring for the four assertions
# `r_titration_dial` makes against it.
_CURVE = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 7,
          11, 11, 12, 12, 12, 13, 13, 13, 13, 13]

# ── the six states (Design's `note` ternary chain, enumerated) ──────────
#
# §5A: enumerate the whole state space including on-load and zero, and key
# every note to WHICH positions it covers rather than to how many presses have
# happened. Design's chain is six branches deep and two of them are single
# positions — drop 0 and drop 9 — which is exactly the shape that is easy to
# lose when a chain is transcribed.
#
# `at` must tile 0..20 with no gap and no overlap, and `side` must agree with
# what the curve says at every position it claims. Both are checked, walking
# every drop rather than a sample.
_STATES = [
    {"id": "start", "at": [0], "side": "acid", "label": "Still acidic",
     "note": "Red, and strongly acidic. Every drop of alkali that goes in "
             "will be destroyed on contact by the acid already there."},
    {"id": "early", "at": [1, 2, 3, 4, 5, 6, 7, 8], "side": "acid",
     "label": "Still acidic",
     "note": "The reading has barely moved. There is far more acid in the "
             "beaker than alkali added so far, so each drop is used up as "
             "fast as it arrives."},
    {"id": "brink", "at": [9], "side": "acid", "label": "Still acidic",
     "note": "Orange, pH 3, and almost all the acid is gone. The next drop "
             "has almost nothing left to react with."},
    # ⭐ THE ONE POSITION THE WHOLE BLOCK IS FOR.
    {"id": "equal", "at": [10], "side": "neutral",
     "label": "Neutral — exactly",
     "note": "Green. Every particle of acid has met a particle of alkali and "
             "both are gone, replaced by salt and water. One drop either side "
             "of this and you would miss it."},
    {"id": "past", "at": [11, 12, 13], "side": "alkali",
     "label": "Now alkaline",
     "note": "Past it. There is no acid left to consume the alkali, so alkali "
             "is now simply accumulating in the beaker."},
    {"id": "flat", "at": [14, 15, 16, 17, 18, 19, 20], "side": "alkali",
     "label": "Now alkaline",
     "note": "Deep purple. From here, adding more barely moves the reading "
             "either — the same flattening as at the start, in the other "
             "direction."},
]

# ── the four problems (Design's `USES`) ─────────────────────────────────
#
# Every one is neutralisation doing a job outside a laboratory, and the four
# are chosen to span the scales it runs at: a field, a stomach, a mouth and an
# industrial tank.
#
# ⚑ Flag 8 is `u3`'s answer and it is kept, with its own hedge intact: "mildly
# alkaline", and the scrubbing credited alongside the chemistry.
_USES = [
    {"id": "u1",
     "q": "A field is too acidic for wheat. What does the farmer spread on it?",
     "options": [{"id": "a", "label": "Lime"},
                 {"id": "b", "label": "Vinegar"},
                 {"id": "c", "label": "More fertiliser"}],
     "answer": "a",
     "reply": "Lime — calcium hydroxide or calcium carbonate, an alkali. It "
              "neutralises the acid in the soil and brings the pH up towards "
              "7, where most crops take up nutrients best. Vinegar would make "
              "it worse; fertiliser feeds the plant but does nothing about "
              "the pH."},
    {"id": "u2",
     "q": "Someone has indigestion: stomach acid where it should not be. What "
          "is in the tablet they take?",
     "options": [{"id": "a", "label": "A weak acid"},
                 {"id": "b", "label": "A base"},
                 {"id": "c", "label": "Salt"}],
     "answer": "b",
     "reply": "A base — usually magnesium hydroxide or calcium carbonate. It "
              "neutralises the excess acid on contact. It has to be a mild "
              "one: a strong alkali would do more damage than the acid it was "
              "sent to deal with."},
    {"id": "u3",
     "q": "Bacteria in your mouth make acid that dissolves tooth enamel below "
          "about pH 5.5. What does toothpaste do about it?",
     "options": [{"id": "a", "label": "Nothing — it only scrubs"},
                 {"id": "b", "label": "It is mildly alkaline and neutralises "
                                      "the acid"},
                 {"id": "c", "label": "It coats the teeth in acid-proof "
                                      "plastic"}],
     "answer": "b",
     "reply": "It is mildly alkaline, so it neutralises the acid the bacteria "
              "produce and lifts the mouth back above the level at which "
              "enamel dissolves. The scrubbing matters too — it removes the "
              "plaque the bacteria live in — but the chemistry is "
              "neutralisation."},
    {"id": "u4",
     "q": "A factory must dispose of a tank of dilute sulfuric acid. Pouring "
          "it into the river would kill the fish. What is done first?",
     "options": [{"id": "a", "label": "Dilute it with much more water"},
                 {"id": "b", "label": "Neutralise it with a base, then check "
                                      "the pH"},
                 {"id": "c", "label": "Boil it away"}],
     "answer": "b",
     "reply": "Neutralise it, then measure the pH before anything is "
              "released. Dilution lowers the concentration but the water "
              "going into the river is still acidic, and a river has its own "
              "life that depends on staying near neutral. Boiling it "
              "concentrates the acid rather than removing it."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 226 character for character.
    "slug":        "neutralisation",
    "title":       "Neutralisation",
    "discipline":  "chemistry",
    "unit":        "acids-and-alkalis",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # See the module docstring: `CR.07` is owned here and `CR.04` is touched.
    # ⚠️ `KS3.C.CR.07a` DOES NOT EXIST YET — see the module docstring and
    # `making-a-pure-dry-salt`'s. Owning the PARENT here while that lesson owns
    # `CR.07b` would trip `validate()` rule 5 (a parent and its own clause both
    # owned), so both lessons name a clause and the pair is minted together or
    # not at all.
    "covers":      ["KS3.C.CR.07a"],
    "touches":     ["KS3.C.CR.04"],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 3},
                    {"id": "measurement-and-uncertainty", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires":    ["the-ph-scale-and-indicators"],
    "assumes":     [],
    "references":  ["acids-and-alkalis"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Mix the two most dangerous bottles in the lab in the "
                    "right amounts and you can pour the result down the sink. "
                    "Where did the danger go?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FIVE stops, Design's `RAIL`, in her order with her ids and short labels.
    # `done_when` restates her own `DONE()`: the hook on a commitment, the
    # titration when the run has passed the cliff (`s.drops >= 12`, which is
    # DERIVED here from the curve rather than typed), the uses when all four
    # are decided, `#s-think` on a commitment, and the ladder when every rung
    # is answered and both self-marked rungs checked.
    #
    # ⚠️ NOTES-C6 §7 says six stops on this page. The RAIL const says five and
    # `docs/ks3/rail-manifest.md` records five, derived from that const. The
    # drawing wins (MRB-205) and the gate compares against the drawing.
    "rail": [
        {"anchor": "s-hook",    "short": "HOOK",
         "label": "Two dangerous bottles", "done_when": "committed"},
        {"anchor": "s-titrate", "short": "DROPS",
         "label": "Drop by drop", "done_when": "cliff_crossed"},
        {"anchor": "s-uses",    "short": "USES",
         "label": "Four problems", "done_when": "all_four_decided"},
        {"anchor": "s-think",   "short": "THINK",
         "label": "Where the acid went", "done_when": "committed"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚠️ THE HOOK CARRIES THE EVIDENCE THAT RULES OUT "IT DISAPPEARED", AND IT
    # CARRIES IT BEFORE THE COMMITMENT. "Boil the water off and there are white
    # crystals in the bottom of the dish" is the whole of `ACID-05`'s answer,
    # sitting in plain sight, and the option list is still worth answering
    # because a student who has decided in advance that neutralising destroys
    # an acid reads that sentence and does not see it.
    "phenomenon": {
        "kind": "narrative",
        "title": "Hydrochloric acid in one beaker. Sodium hydroxide in the "
                 "other. Both would burn you. Mixed carefully, the result is "
                 "salty water.",
        "prompt": "The mixture warms up while it happens. Test it afterwards "
                  "and universal indicator comes out green — pH 7. Boil the "
                  "water off and there are white crystals in the bottom of "
                  "the dish. Taste them, if it were a kitchen and not a "
                  "laboratory, and they would taste of table salt.",
        "commit": "What happened to the acid and the alkali?",
        # MRB-177: 7, 7, 11, 8 words. The correct option is index 1 and is the
        # JOINT SHORTEST. Design's set, unchanged.
        "options": [
            "They cancelled out and both disappeared",
            "They reacted and made two new substances",
            "The acid was diluted until it was too weak to matter",
            "The alkali evaporated and left the acid behind",
        ],
        "reveal": "They reacted, and made two new substances. Nothing "
                  "vanished — the atoms are all still in the beaker, "
                  "rearranged into <strong>water</strong> and a compound "
                  "called a <strong>salt</strong>. The white crystals are the "
                  "proof: they were not in either bottle at the start. This "
                  "is a chemical reaction like any other, and it has a name: "
                  "<strong>neutralisation</strong>.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⊖ `think-reveal-salt` cannot be emitted from a lane — the `#s-think`
    # reveal panel is drawn by the shared `r_activity` with no id. `ACID-05`
    # names the activity that holds both its commitment and its answer, which
    # is the `c5-02` reconciliation and what satisfies Law 3.
    #
    # ⊕ `ACID-06` names two things the page really does emit. Design's NOTES
    # proposes `titration-dial` for the elicitation, which is a FAMILY name
    # rather than a DOM id and resolves to nothing; the section the dial is in
    # carries `id="s-titrate"` and is where the student commits by adding
    # drops and watching the reading crawl. `curve-reveal` is the closing
    # panel's own id, authored on the payload rather than composed in the
    # renderer, and it is the paragraph that takes the belief apart.
    "misconceptions": [
        {"id": "ACID-05",
         "statement": "Neutralising an acid destroys it; only water is left.",
         "elicited_by": "think-commit-gone",
         "confronted_by": "think-commit-gone"},
        {"id": "ACID-06",
         "statement": "The pH climbs steadily as alkali is added.",
         "elicited_by": "s-titrate",
         "confronted_by": "curve-reveal"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "<strong>Neutralisation</strong> is the reaction between an "
                 "acid and a base. With an alkali the products are always the "
                 "same two things, whichever acid and whichever alkali you "
                 "started with."},

        # ⭐ THE WORD EQUATION, DRAWN. Design sets it as a 24px display line
        # with an inline SVG arrow between two spans (page line 106). An
        # `explainer` cannot carry it: `rich()` allows `<em>`, `<strong>` and
        # `<sub>` and escapes everything else, so an SVG in explainer text
        # ships as literal angle brackets to a child. `r_equation` — reached
        # through the `rule` block — is the platform's own component for
        # exactly this, it draws the same arrow, and it REFUSES a typed U+2192
        # in any of its three fields.
        #
        # ⚖️ NO TRIANGLE AND NO PART-WHOLE BAR, and that is MRB-204 as amended
        # rather than an omission. The triangle belongs to `A = B x C` and the
        # bar to a sum or a conservation statement; a word equation is neither,
        # and a triangle over `acid + alkali makes salt + water` would teach
        # that `alkali = salt x water / acid`, which is not merely unhelpful
        # but false. `r_equation`'s own docstring makes the same ruling for
        # photosynthesis.
        {"type": "rule", "id": "the-two-products",
         "eyebrow": "The rule",
         "statement": "An acid and an alkali always make the same two things.",
         "equation": {"reactants": "acid + alkali",
                      "arrow": "makes",
                      "products": "salt + water",
                      # Commentary on the whole equation rather than a
                      # condition on the arrow — the b8-01 shape. There is no
                      # condition on this reaction: it needs no heat, no light
                      # and no catalyst, and inventing one to satisfy the key
                      # would teach a requirement that does not exist.
                      "condition": "the salt takes its metal from the alkali "
                                   "and its family name from the acid"},
         "close": "“Salt” here does not only mean the stuff on chips. It "
                  "means the whole family of compounds made when the hydrogen "
                  "in an acid is swapped for a metal — sodium chloride is one "
                  "of thousands. Which salt you get depends on which acid and "
                  "which alkali you started with, and that is a lesson of its "
                  "own."},

        # #s-titrate — the flagship, and the lesson. Light `ks3-block` →
        # `check`.
        #
        # ⚠️ NO `prompt` NARRATING THE CONTROLS. §5A forbids it and Design does
        # not: her lead is "Alkali goes in one drop at a time. Watch the
        # number, not the colour — the colour is only the number in disguise",
        # which is an instruction about what to ATTEND to rather than which
        # button to press, and it is the sentence that makes the trace mean
        # something. Kept whole.
        {"type": "titration-dial", "id": "drop-by-drop", "anchor": "s-titrate",
         "eyebrow": "Your turn · add the alkali drop by drop",
         "heading": "25 cm³ of hydrochloric acid. Universal indicator already "
                    "added.",
         "prompt": "Alkali goes in one drop at a time. Watch the number, not "
                   "the colour — the colour is only the number in disguise.",
         "demand": "investigate",
         "curve": _CURVE,
         "states": _STATES,
         "add_buttons": [{"n": 1, "label": "Add 1 drop"},
                         {"n": 5, "label": "Add 5 drops"}],
         "reset_label": "Start again",
         "count_format": "{n} drops of alkali added",
         "count_zero": "0 drops of alkali added",
         "trace_label": "The reading, drop by drop",
         "axis_label": "0 drops · · · 20 drops",
         # ⭐ `ACID-06`'s confrontation site. The id is authored here rather
         # than composed in the renderer, so the register's join and the
         # markup have one source.
         "close": {"id": "curve-reveal",
                   "title": "Look at the shape of what you just did.",
                   "paras": [
                       "For the first nine drops almost nothing moves. Then "
                       "one single drop takes the reading from 3 to 11 and "
                       "the colour goes straight through green without "
                       "stopping. After that it flattens off again.",
                       "That cliff is the moment the last of the acid is used "
                       "up. Before it, every drop of alkali is consumed "
                       "instantly by acid that is still there. After it, "
                       "there is no acid left to consume anything, so the "
                       "alkali just piles up. <strong>Neutral is not a region "
                       "you drift into. It is a single point you "
                       "cross.</strong>",
                   ]}},

        {"type": "key-fact", "ref": "salt-and-water"},

        # #s-uses — four problems. Light `ks3-block` → `check`.
        {"type": "acid-judgements", "id": "uses-four", "anchor": "s-uses",
         "eyebrow": "Four problems · one reaction",
         "heading": "What would you add, and why that?",
         "prompt": "Every one of these is neutralisation doing a job outside "
                   "a laboratory. Commit before you read.",
         "demand": "explain",
         "head_counter": {"format": "{n} of {total} decided", "start": 0},
         "items": _USES},

        {"type": "misconception", "id": "think-commit-gone",
         "anchor": "s-think", "targets": "ACID-05"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # None. The trace IS the picture, and it is a live one: a frozen drawing of
    # the same curve beside it would be a second copy of something the
    # instrument already shows and could disagree with. §5.4 allows an empty
    # list where it does not allow an absent one.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # ⚑ "makes" rather than a typed arrow — Design's own 21 Aug font-law pass.
    # A formula LINE draws the mark; prose says the word.
    "key_facts": [
        {"id": "salt-and-water",
         "text": "acid + alkali makes salt + water. Nothing is destroyed: the "
                 "atoms are rearranged into two new substances, and the pH "
                 "ends at 7 only if the amounts match exactly.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        {"id": "think-commit-gone",
         "kind": "predict",
         "demand": "explain",
         "targets": "ACID-05",
         "prompt": "The beaker does end up looking like water. Commit before "
                   "you read on.",
         # MRB-177: 10, 15, 10, 8 words. The correct option is index 1 and is
         # strictly the longest by five words at 1.5x — the construct §13
         # measures. The three distractors are re-authored at its own length
         # and in its own shape; Design's B is untouched and the answer has not
         # moved.
         "options": [
             "Right — the acid is destroyed and only water is left in the "
             "beaker afterwards",
             "Wrong — a salt is dissolved in the water, made from the acid "
             "and the alkali",
             "Right, because pH 7 means empty and the crystals came out of "
             "the dish itself",
             "Wrong — the acid is still there unchanged, just hidden by all "
             "the water around it",
         ],
         "reveal": [
             "Boil the water off and the answer is sitting in the dish. A "
             "neutralised beaker contains a <strong>salt</strong> dissolved "
             "in water, and that salt is made of atoms that came out of the "
             "acid and the alkali. Weigh everything before and after: the "
             "mass is unchanged, because this is conservation of mass and no "
             "reaction escapes it.",
             "What has gone is the <em>behaviour</em>. The thing that made "
             "the acid corrosive has been used up in making water, and so has "
             "the thing that made the alkali corrosive. "
             "<strong>Neutralisation does not delete the atoms. It puts them "
             "somewhere harmless.</strong>",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    "ladder": {
        # Design's options, untouched; the answer moves to index 1 (MRB-278 —
        # see `lesson_02`'s note on the twelve rungs). MRB-177: 3, 3, 2, 3
        # words, so nothing here is a length tell in either direction.
        #
        # ⚑ The question reads "makes what?" rather than carrying an arrow —
        # Design's own 21 Aug font-law pass, and the correct option is the two
        # products rather than an equation with a mark in it.
        "recall": {
            "q": "Complete the word equation: acid + alkali makes what?",
            "options": [
                "water only",
                "salt + water",
                "salt + hydrogen",
                "a weaker acid",
            ],
            "answer": 1,
            "feedback": {
                0: "Water is one product. The atoms from the metal part of "
                   "the alkali and the rest of the acid have to go somewhere "
                   "— they become the salt.",
                2: "That is what an acid does with a metal, not with an "
                   "alkali. No gas is produced here.",
                3: "Neutralisation makes new substances, not a diluted "
                   "version of the old one.",
            }},
        # ⚑ MRB-177 — THE THREE DISTRACTORS ARE RE-AUTHORED AND THE CORRECT
        # OPTION IS UNTOUCHED. Design's set ran 20 words against 9, 7 and 6:
        # strictly the longest by eleven words and at 2.2x, the widest tell in
        # the unit. Each distractor now states a WRONG RULE in the correct
        # answer's own "X, so Y" shape and at close to its length — 18, 17, 17
        # against 20. Every one of Design's corrections is unchanged and still
        # answers its own option, because each distractor still names the same
        # wrong cause: a stronger drop, a failed indicator, boiling.
        "apply": {
            "q": "A beaker of acid has alkali added drop by drop. After nine "
                 "drops the pH is 3; after ten it is 11. What happened at the "
                 "tenth drop?",
            "options": [
                "The tenth drop was more concentrated than the ones before "
                "it, so it moved the reading much further",
                "The indicator stopped working at that point, so the colour "
                "it showed after ten drops means nothing",
                "The last of the acid was used up, so the next drop of alkali "
                "had nothing to react with",
                "The solution boiled from the heat of the reaction, so it "
                "turned alkaline as the water left",
            ],
            "answer": 2,
            "feedback": {
                0: "Every drop came from the same bottle. What changed was "
                   "what was waiting for it in the beaker.",
                1: "The indicator reported the change faithfully — the change "
                   "was real and sudden.",
                3: "The mixture warms slightly but nothing boils, and warming "
                   "does not move a solution across the scale.",
            }},
        "explain": {
            "q": "A student neutralises hydrochloric acid with sodium "
                 "hydroxide and says “the acid has disappeared”. "
                 "Explain what has actually happened to the atoms, and how "
                 "you could prove it.",
            "field_label": "Your explanation",
            "placeholder": "The atoms have not disappeared — they have…",
            "success": [
                "Says the acid and alkali reacted to form new substances.",
                "Names the products as a salt (sodium chloride) and water.",
                "Says the atoms are all still present, just rearranged.",
                "Says mass is conserved and could be checked on a balance.",
                "Says evaporating the water would leave the salt behind as "
                "crystals.",
            ]},
        "produce": {
            "q": "A lake has become acidic because of pollution and the fish "
                 "are dying. Explain how you would decide how much lime to "
                 "add, and why adding a very large amount all at once would "
                 "be a bad idea.",
            "field_label": "Your answer",
            "placeholder": "First I would measure…",
            "success": [
                "Says to measure the pH of the lake water first.",
                "Says lime is a base and will neutralise the acid.",
                "Says to add it gradually and re-test the pH as you go.",
                "Says too much would push the water past 7 and make it "
                "alkaline.",
                "Says a sudden large change in pH would itself harm the fish.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Neutralisation is the reaction of an acid with a base: acid "
                "+ alkali makes salt + water. The pH moves towards 7 as the "
                "acid is used up, and the change is sudden rather than "
                "gradual. Nothing is destroyed — the salt formed is still "
                "dissolved in the beaker, and boiling the water off leaves it "
                "behind as crystals.",

    # ── the stretch layer (§5.6) ────────────────────────────────────────────
    "stretch": [
        {"type": "explainer", "id": "titration",
         "text": "The cliff you plotted is why a chemist measuring an unknown "
                 "acid uses a single drop of a sharp indicator rather than "
                 "universal indicator. Run alkali in from a burette, watch "
                 "for the one drop that flips the colour, and read the volume "
                 "off the scale: that volume tells you exactly how much acid "
                 "was in the flask. The technique is called titration and it "
                 "is how the strength of everything from vinegar to blood "
                 "plasma is checked."},
        {"type": "explainer", "id": "chimneys-and-plasterboard",
         "text": "Neutralisation also runs on an industrial scale where "
                 "nobody would call it chemistry. Power station chimneys are "
                 "washed with a spray of calcium hydroxide to catch the "
                 "sulfur dioxide that would otherwise fall as acid rain; the "
                 "salt produced is calcium sulfate, which is plasterboard. A "
                 "reaction that started as two beakers on a bench ends up as "
                 "the walls of a house."},
    ],

    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    "vocabulary": [
        {"term": "Neutralisation",
         "definition": "The reaction between an acid and a base. With an "
                       "alkali it makes a salt and water."},
        {"term": "Salt",
         "definition": "The compound left when the hydrogen in an acid is "
                       "swapped for a metal. Sodium chloride is one of "
                       "thousands.",
         "note": "Not only the stuff on chips."},
        {"term": "Base",
         "definition": "Any substance that neutralises an acid. The ones that "
                       "dissolve in water are alkalis."},
        {"term": "Equivalence point",
         "definition": "The moment when exactly enough alkali has been added "
                       "to use up all the acid. On this page it is the single "
                       "drop where the reading jumps."},
        {"term": "Titration",
         "definition": "Adding one solution to another a little at a time "
                       "until the reaction is exactly complete, and measuring "
                       "how much it took."},
    ],

    # ── safety (§1.5) ───────────────────────────────────────────────────────
    # ⚑ NEW PROSE. ⊖ No safeguarding block — lab safety, and it takes a plain
    # note. Scoped to add to the method rather than withdraw it: the page is
    # about mixing an acid with an alkali on purpose, and this says what makes
    # that safe to do.
    # The second paragraph is Mide's, approved 28 Aug 2026, and reproduced
    # VERBATIM — it closes the second C6 gap the audit flagged: the existing
    # note covers the titration but not the HOOK's "mix the two most
    # dangerous bottles" demonstration. Do not reword it.
    "safety_note": "The mixture warms as it reacts, and a concentrated acid "
                   "mixed with a concentrated alkali warms enough to boil and "
                   "spit. School titrations use dilute solutions of both, a "
                   "drop at a time, with eye protection on — which is also "
                   "the only way to find the one drop that matters. "
                   "Teacher demonstration. Eye protection on, and watch from "
                   "your seat. The acid and alkali here are dilute, but both "
                   "sting in the eyes.",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why the pH jumps instead of climbing?",
              "cta": "Ask about this lesson",
              "anchor": "s-titrate"},

    # ⚑ FONT LAW, AND ONE ENGINE FACT THAT OVERRIDES DESIGN'S MARKUP HERE.
    # `ks4_becomes` goes through `rich()`, whose allow-list is `em`, `strong`
    # and `sub` — there is no `sup`, so a `<sup>+</sup>` would ship the literal
    # characters to a child. The charges are written at baseline (`H+`, `OH−`,
    # with U+2212 for the minus, which the shipped subsets do carry) and
    # `H<sub>2</sub>O` keeps its subscript, which `rich()` does allow. "makes"
    # rather than an arrow, per Design's own 21 Aug pass.
    "ks4_becomes": "Titration with a burette, the ionic equation H+ + OH− "
                   "makes H<sub>2</sub>O, and calculating concentrations from "
                   "titration results.",

    "ws": ["experimental-skills-and-investigations", "measurement"],

    "review_state": "draft",
}
