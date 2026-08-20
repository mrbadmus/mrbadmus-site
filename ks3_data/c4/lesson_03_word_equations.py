"""C4 L3 — Word equations (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c4/c4-03-word-equations.dc.html` (715 lines), and
her author's notes `docs/ks3/design-reference/c4/NOTES-C4.md` §1, §2, §5
flags 9 and 10, §6 (`REACT-05`, `REACT-06`) and §7.

Every student-facing string is byte-identical to the approved page. `RAIL`,
`CASES`, `READINGS`, `RUNGS` and `SELF_RUNGS` came out of the node extractor;
the hook title, prompt, options and reveal, both explainer paragraphs, the
builder's bench and equation labels, all four verdict branches, the key fact,
the `#s-read` headings, the `#s-think` options and its two reveal paragraphs,
the key note and both "Going further" paragraphs were lifted from
`lessonVals(s)` and from the markup, which is where most of this lesson's
words live and where a lift of the top-level constants alone loses them.

── The builder's distractors ARE the lesson ────────────────────────────

NOTES §2 on this page: "the equation builder, with distractors that are the
real errors: heat, energy, a flame, limewater from a different test tube, and
'bubbles' instead of the gas's name." Every one of the five is a WRONG RULE in
the correct answer's own shape — each is a noun a student can point at on the
bench, offered in the same list and with the same two buttons as the real
substances, so nothing about the CONTROL says which is which. Only the reason
does.

That is why the corrections below name the wrong rule rather than saying no:
"a substance that is only present does not go in the equation", "it is a
condition, and conditions are written above the arrow", "bubbles are what you
saw, not a substance". A student who has read those five can sort a sixth.

⚠️ THE ARROW IS DRAWN, NEVER TYPED. Every arrow inside an equation on this
page is an SVG path — Design's C4 convention, and a hard one: the shipped font
subsets do not contain U+2192, so a typed arrow is a missing glyph in the
middle of the notation the lesson is teaching. `t()` / `rich()` draw the mark
for authored prose (the hook reveal's equation below is the only place this
file relies on that); the instrument draws Design's own 44×24 arrow itself.

⚑ For Mide's science gate, from Design's NOTES §5 — BOTH ALREADY RULED:
  * flag 9 — marble + acid giving calcium chloride, water and carbon dioxide.
    CONFIRMED correct for HYDROCHLORIC acid, and naming the salt is right at
    KS3. Kept. The case story names the acid ("dropped into hydrochloric
    acid") and so does rung 3's question, because "acid" alone would make the
    salt name wrong — a different acid gives a different salt.
  * flag 10 — iron rusting deliberately EXCLUDED from the word-equation cases.
    OMISSION STANDS, ruled. Rust is hydrated iron oxide and an honest equation
    for it needs water as a reactant, which is a complication this lesson
    cannot afford; C5's oxidation lesson teaches rust as hydrated iron oxide
    and the two are consistent. No rusting case was added, and nothing here
    teaches "iron + oxygen makes iron oxide" as if it were rusting. The one
    place rust is named at all is the second "Going further" paragraph, which
    is Design's own and which says exactly why a rusting word equation is
    hard: the name is not agreed.

── Where the misconception joins land (MRB-244 / MRB-248) ──────────────

Both joins resolve against markup this page really emits:

  REACT-06  elicited_by  `builder-distractor`  → `id="builder-distractor"`,
            the bench panel that offers heat, energy, a flame, limewater and
            "bubbles" beside the real substances (`ks3_art/c4.py`).
            confronted_by `builder-check`      → `data-activity="builder-check"`,
            the builder itself. The instrument's activity id is `builder-check`
            rather than the anchor's `s-builder` for exactly this reason: Law 3
            wants a wrong idea taken apart by a real ACTIVITY, and the check
            panel is where this one is taken apart.

  REACT-05  elicited_by  `s-think`             → the section's own anchor id.
            confronted_by `think-reveal-direction` → `data-activity=…`, the
            commit-and-reveal activity in that section.

⚖️ ONE RENAME, AND IT IS REPORTED. NOTES §6 proposes `think-commit-arrow` for
REACT-05's elicitation. The engine emits exactly TWO names on a confrontation
section — the anchor as `id` and the activity as `data-activity` — and a
generic reveal panel carries no id of its own, so the register's two names
cannot both be emitted. The mandatory key keeps its register name
(`confronted_by: think-reveal-direction`, which is also an activity id and so
satisfies Law 3 twice over) and the optional one names the section it happens
in. C1's `PART-03` is the standing precedent: one activity both elicits and
confronts, in one commit.
"""

# ── the three cases (Design's `CASES`) ──────────────────────────────────
#
# ONE object, read by the instrument for the bench, the model equation and
# every verdict branch. `reactants` and `products` are the answer; `distractors`
# maps a name that must NOT appear to the sentence that says why. The bank is
# built as reactants + products + distractors in this order — Design's own
# `names` — so the real substances are never last and the distractors are
# never marked out by position.
#
# ⚠️ THE NAMES ARE CAPITALISED HERE AND LOWER-CASED IN A SENTENCE. Design
# renders the chip and the model equation from these strings as written, and
# the wrong-side branch lower-cases the name mid-sentence. That is the
# instrument's job, not the author's: there is one spelling of every name in
# this file.
_CASES = [
    {"id": "mg",
     "tab": "Burning magnesium",
     "story": "A ribbon of magnesium is held in a hot flame with tongs. It "
              "burns with a fierce white light, taking oxygen out of the air "
              "as it goes, and leaves a white powder called magnesium oxide. "
              "The tongs are unchanged. Air also contains nitrogen, which "
              "takes no part.",
     "reactants": ["Magnesium", "Oxygen"],
     "products": ["Magnesium oxide"],
     "distractors": [
         ("Nitrogen", "Nitrogen was in the air and took no part in the "
                      "reaction. A substance that is only present does not "
                      "go in the equation — only what reacts and what is "
                      "made."),
         ("Heat", "Heat is not a substance. It is a condition, and "
                  "conditions are written above the arrow if they are "
                  "written at all."),
     ]},
    # ⚑ Science flag 9. The acid is NAMED in the story, and it has to be:
    # calcium chloride is the salt hydrochloric acid gives, and "acid" alone
    # would make the product name wrong.
    {"id": "marble",
     "tab": "Marble and acid",
     "story": "Marble chips — calcium carbonate — are dropped into "
              "hydrochloric acid. The mixture fizzes hard. The gas given off "
              "turns limewater cloudy, so it is carbon dioxide. Left in the "
              "flask are water and a dissolved salt, calcium chloride. The "
              "limewater was in a separate test tube.",
     "reactants": ["Calcium carbonate", "Hydrochloric acid"],
     "products": ["Calcium chloride", "Water", "Carbon dioxide"],
     "distractors": [
         ("Limewater", "Limewater was used to test the gas in a different "
                       "tube. It never met the marble, so it is not part of "
                       "this reaction."),
         ("Bubbles", "Bubbles are what you saw, not a substance. The "
                     "substance is carbon dioxide — name it."),
     ]},
    {"id": "methane",
     "tab": "A gas hob",
     "story": "Methane from the gas supply burns in the oxygen of the air. "
              "Carbon dioxide goes up into the room and water vapour "
              "condenses on a cold window above the hob. The flame itself is "
              "the reaction happening, not an ingredient.",
     "reactants": ["Methane", "Oxygen"],
     "products": ["Carbon dioxide", "Water"],
     "distractors": [
         ("Energy", "Energy is given out, and it is still not a substance. "
                    "It has no place on either side of a word equation."),
         ("Flame", "The flame is the reaction, seen. Nothing is made of "
                   "flame."),
     ]},
]

# ── the three readings (Design's `READINGS`) ────────────────────────────
#
# Two options each, so there is no lettered list and no length gate to clear:
# the pair IS the question. `answer` is the index Design marks correct and
# `reply` is the paragraph that opens once the card is decided — one
# commitment per card, final, and the reply is on screen the instant it is
# made.
_READINGS = [
    {"id": "x1",
     "left": "zinc + copper sulfate",
     "right": "zinc sulfate + copper",
     "options": [
         "Zinc and copper sulfate react to make zinc sulfate and copper",
         "Zinc plus copper sulfate equals zinc sulfate plus copper",
     ],
     "answer": 0,
     "reply": "The first. \"Plus\" and \"equals\" describe an arithmetic sum; "
              "this is a reaction, so it is read as \"and\" and \"makes\". "
              "Say it out loud the wrong way and you will write it the wrong "
              "way."},
    {"id": "x2",
     "left": "copper carbonate",
     "right": "copper oxide + carbon dioxide",
     "options": [
         "One substance has broken down into two",
         "Two substances have joined to make one",
     ],
     "answer": 0,
     # ⊕ MRB-246 — "next unit" came out. Design wrote "you will meet this
     # as thermal decomposition next unit", which names no year, no
     # half-term and no unit code, so it is not a §14 sequence leak by
     # the letter. It is one by the argument: a school teaches these
     # units in ITS OWN order, `school_schemes.py` exists so that it
     # can, and "next" is false for every school that meets reaction
     # types before it meets equations. C3's "the next lesson but one"
     # is not a precedent for this — WITHIN a unit the order is fixed.
     # The forward pointer and the term both survive; only the claim
     # about when goes.
     "reply": "One reactant, two products: the copper carbonate has been "
              "broken apart. Nothing joined it and nothing needed to — "
              "this kind of reaction has a name of its own, thermal "
              "decomposition."},
    {"id": "x3",
     "left": "iron + sulfur",
     "right": "iron sulfide",
     "options": [
         "A mixture of iron and sulfur has been made",
         "A compound has been made, and the iron is no longer magnetic",
     ],
     "answer": 1,
     "reply": "The arrow means a reaction happened, so the product is a "
              "compound, not a mixture. A mixture of iron and sulfur would "
              "still be separable with a magnet; iron sulfide is not."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 210 character for character.
    "slug":        "word-equations",
    "title":       "Word equations",
    "discipline":  "chemistry",
    "unit":        "chemical-reactions",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # NOTES §1: `KS3.C.CR.02` is split across two lessons — a word equation is
    # a sentence, a symbol equation is a model with numbers in it. Clause `a`
    # is the words half and is already minted in `ks3_data/substatements.py`
    # with its reasoning; it is not re-minted or edited here.
    "covers":      ["KS3.C.CR.02a"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 3},
                    {"id": "particles", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # The page's "Before this lesson" card links to the rearrangement lesson,
    # and it has to: "the atoms are rearranged, not made" is what stops a
    # missing substance in an equation looking harmless.
    "requires":    ["reactions-rearrange-atoms"],
    "assumes":     [],
    "references":  ["chemical-vs-physical-change"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "You can describe a reaction in a paragraph and still not "
                    "have said what reacted. What has to be in the sentence "
                    "for it to count?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, Design's `RAIL` in her order with her ids and her shorts.
    # `done_when` restates her own `DONE()` (page line 447): the hook on a
    # commitment, the builder when all three cases have been checked, the
    # readings when all three are decided, `#s-think` on a commitment, the
    # ladder when every rung is answered and both self-marked rungs checked.
    "rail": [
        {"anchor": "s-hook",    "short": "HOOK",
         "label": "Twenty-two words", "done_when": "committed"},
        {"anchor": "s-builder", "short": "BUILD",
         "label": "Build it", "done_when": "all_cases_checked"},
        {"anchor": "s-read",    "short": "READ",
         "label": "Read it back", "done_when": "all_readings_decided"},
        {"anchor": "s-think",   "short": "THINK",
         "label": "Not an equals sign", "done_when": "committed"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚠️ OPTION D IS THE ONE STRING IN THIS BLOCK THAT IS NOT DESIGN'S, and it
    # is a §13 fix made AT THE DISTRACTOR. Her four options measure 5 / 10 / 5
    # / 7 words, so the correct one is strictly the longest and clears the
    # longest distractor by 1.43× — a length tell, and a student can take it
    # without reading a word of the sentence above. Her D was "Nothing — it
    # describes the reaction fully"; this one makes the same claim in the
    # correct option's own shape, naming two things the sentence supposedly
    # says, and the set now measures 5 / 10 / 5 / 10. Nothing else moved: the
    # correct option is untouched and the answer is in the same place.
    #
    # The reveal's second half is Design's equation line, which she draws as a
    # display row under the paragraph. The engine's hook reveal is one
    # paragraph, so the seam is re-authored as a sentence rather than deleted
    # — and the arrow is a real U+2192 in this file ONLY because `rich()`
    # replaces it with the drawn mark before it reaches the page.
    "phenomenon": {
        "kind": "narrative",
        "title": "Twenty-two words, and not one of them says what the "
                 "reaction was.",
        "prompt": "“I held the magnesium ribbon in the flame with tongs and "
                  "it burned with a really bright white light and left a "
                  "white powder behind.” Every word is true. A chemist "
                  "reading it still does not know what reacted with what.",
        "commit": "What is missing from that sentence?",
        "options": [
            "The temperature of the flame",
            "What the magnesium reacted with, and what the powder is",
            "How long it burned for",
            "Nothing — it says what happened and what was left",
        ],
        "reveal": "The other reactant, and the name of the product. The "
                  "sentence describes what it looked like; it never says "
                  "that the magnesium joined with the <strong>oxygen in the "
                  "air</strong>, or that the white powder is "
                  "<strong>magnesium oxide</strong>. A word equation says "
                  "all of it in six words and cannot avoid saying it: "
                  "magnesium + oxygen → magnesium oxide.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ `REACT-05`'s `statement` is the PAGE's quoted line, not NOTES §6's
    # shorter register handle ("The arrow in an equation means equals, so the
    # sides can be swapped"). `r_confrontation` prints `statement` as the
    # `#s-think` quote and Design's line is the one that must render — the
    # same reconciliation c3-03 made for MIX-06. `REACT-06` is not quoted
    # anywhere on the page, so it keeps the register's wording.
    #
    # Both joins and the one rename are set out in the module docstring.
    "misconceptions": [
        {"id": "REACT-05",
         "statement": "The arrow is like an equals sign, so you could write "
                      "the equation the other way round.",
         "elicited_by": "s-think",
         "confronted_by": "think-reveal-direction"},
        {"id": "REACT-06",
         "statement": "Heat, energy or a flame can be written into an "
                      "equation as a reactant.",
         "elicited_by": "builder-distractor",
         "confronted_by": "builder-check"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Page lines 108-109. Two paragraphs, two blocks: `explainer` carries
        # one `text`, and running them together would put the plus sign's rule
        # inside the arrow's.
        {"type": "explainer",
         "text": "A <strong>word equation</strong> puts the substances you "
                 "start with — the <strong>reactants</strong> — on the left, "
                 "and the substances you end with — the "
                 "<strong>products</strong> — on the right. The arrow is read "
                 "as <strong>“makes”</strong> or <strong>“turns into”</strong>. "
                 "It is not an equals sign, and the two sides are not "
                 "interchangeable: a reaction runs one way, and so does the "
                 "arrow."},
        {"type": "explainer",
         "text": "The plus sign is read as <strong>“and”</strong>. It never "
                 "means add up."},

        # #s-builder — the flagship. Light `ks3-block` → `check`.
        # ⚠️ The activity id is `builder-check` and NOT the anchor. See the
        # docstring: it is REACT-06's `confronted_by`, and Law 3 wants that to
        # be an activity.
        {"type": "equation-builder", "id": "builder-check",
         "anchor": "s-builder",
         "eyebrow": "Your turn · build the equation",
         "heading": "Read what happened. Put each substance where it belongs.",
         "demand": "construct",
         "cases": _CASES,
         "bench_label": "On the bench · not everything here belongs in the "
                        "equation",
         "equation_label": "Your equation",
         "empty_label": "nothing yet",
         "place_labels": {"left": "Reactant", "right": "Product",
                          "out": "Leave it out"},
         "check_label": "Check this equation",
         "clear_label": "Clear it",
         # ⚠️ TEMPLATES, NOT SENTENCES, and only where a NAME has to be
         # substituted. The two branches that quote a substance are the only
         # strings the instrument composes; every other verdict sentence —
         # including all six distractor corrections above — is emitted as
         # real markup and shown, never assembled. `{Name}` is the name as
         # written, `{name}` is the same name lower-cased mid-sentence.
         "verdict": {
             "perfect_title": "That is the equation.",
             "perfect_text": "Every reactant on the left, every product on "
                             "the right, nothing in it that is not a "
                             "substance, and nothing in it that was only "
                             "watching.",
             "distractor_title": "One thing in there does not belong.",
             "side_title": "{Name} is on the wrong side.",
             "side_product": "You have said {name} was there before the "
                             "reaction started. It was made by the reaction, "
                             "so it belongs on the right of the arrow.",
             "side_reactant": "You have said {name} was made by the "
                              "reaction. It was one of the things you "
                              "started with, so it belongs on the left.",
             "missing_title": "Something is missing.",
             "missing_text": "You have left out {names}. A word equation "
                             "with a missing substance implies the atoms in "
                             "it came from nowhere.",
             "missing_join": " and ",
         }},

        {"type": "key-fact", "ref": "only-substances"},

        # #s-read — three equations, read back. Light `ks3-block` → `check`.
        {"type": "equation-read", "id": "read-back", "anchor": "s-read",
         "eyebrow": "Read it back",
         "heading": "Which sentence is the equation actually saying?",
         "demand": "explain",
         "readings": _READINGS},

        {"type": "misconception", "id": "think-reveal-direction",
         "anchor": "s-think", "targets": "REACT-05"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # None. Design draws no diagram on this page and NOTES §7 declares none:
    # the equation IS the model, and it is drawn by the instrument at the
    # point the student builds it. Present and empty, never absent.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "only-substances",
         "text": "Reactants on the left, products on the right, and the "
                 "arrow means “makes”. Only substances go in a word equation "
                 "— never conditions, never energy, and never anything that "
                 "was only watching.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # `#s-think` only. The two instrument blocks are lifted out of `core` into
    # this list by `_normalise()` and are never authored here.
    "activities": [
        {"id": "think-reveal-direction",
         "kind": "predict",
         "demand": "explain",
         "targets": "REACT-05",
         "prompt": "The two sides do have the same atoms in them, which is "
                   "exactly why this is tempting. Commit before you read on.",
         "options": [
             "Right — both sides have the same atoms",
             "Wrong — the arrow says which way the reaction went",
             "Right, as long as you keep the plus signs",
             "Wrong — the two sides do not have the same atoms",
         ],
         "reveal": [
             "The two sides balance in atoms and they are not the same "
             "thing. Written the other way round, “magnesium oxide makes "
             "magnesium and oxygen” claims that white powder spontaneously "
             "turns back into burning metal and air, which it does not — it "
             "takes a furnace, and it is a different reaction with a "
             "different equation.",
             "So the arrow carries information an equals sign does not: "
             "<strong>which way it went.</strong> Two other habits follow "
             "from the same mistake. You cannot cancel a substance that "
             "appears on both sides the way you cancel in algebra — it is "
             "doing something on each side. And “heat”, “energy” and “a "
             "flame” are not substances, so they never appear in the "
             "equation; if the conditions matter, they are written above the "
             "arrow.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Design's RUNGS → recall + apply, SELF_RUNGS → explain + produce. Her four
    # headings are the engine's own defaults character for character, so no
    # rung authors a `title`. `feedback` is keyed by the INT index of each
    # wrong option, which is what `_rung_marked` reads.
    #
    # ⚑ MRB-177, measured rather than eyeballed. Rung 1 is 4 / 1 / 1 / 4
    # words: the correct option is not strictly the longest, so there is no
    # tell to fix. Rung 2 is 12 / 9 / 10 / 8: strictly longest by 2 words at
    # 1.2×, which clears both thresholds. Neither set was touched.
    "ladder": {
        "recall": {
            "q": "In a word equation, what does the arrow mean?",
            "options": [
                "Makes, or turns into",
                "Equals",
                "And",
                "Is heated to give",
            ],
            "answer": 0,
            "feedback": {
                1: "An equals sign works both ways. The arrow says which way "
                   "the reaction went, and reversing it usually describes "
                   "something that does not happen.",
                2: "That is the plus sign. The arrow separates the reactants "
                   "from the products.",
                3: "Heating may or may not be involved. Many reactions need "
                   "no heat, and the arrow means the same thing in all of "
                   "them.",
            }},
        # ⚑ REACT-06 again, marked this time. The rung is Design's and it is
        # the same wrong rule the builder's `Heat` chip offers.
        "apply": {
            "q": "A student writes: magnesium + oxygen + heat makes "
                 "magnesium oxide. What is wrong with it?",
            "options": [
                "Heat is not a substance, so it does not belong in the "
                "equation",
                "Nothing — heat is needed, so it should be included",
                "Heat should be on the right, because burning gives out heat",
                "The reactants and products are the wrong way round",
            ],
            "answer": 0,
            "feedback": {
                1: "Heat is needed, and it is a condition rather than a "
                   "reactant. Conditions go above the arrow, not in the line "
                   "of substances.",
                2: "Energy does give out — and it still is not a substance. "
                   "Neither side of a word equation is the place for it.",
                3: "Those are in the right places. The problem is the extra "
                   "term between them.",
            }},
        "explain": {
            "q": "Write the word equation for marble chips reacting with "
                 "hydrochloric acid, then explain how someone reading only "
                 "your equation would know that a gas was given off and that "
                 "a new substance was made.",
            "field_label": "Your equation and explanation",
            "placeholder": "calcium carbonate + hydrochloric acid makes…",
            "success": [
                "Gives the correct reactants on the left: calcium carbonate "
                "and hydrochloric acid.",
                "Gives all three products: calcium chloride, water and "
                "carbon dioxide.",
                "Says the arrow means the reactants made the products, so a "
                "change happened.",
                "Identifies carbon dioxide as the gas, and says how that is "
                "known — it turns limewater cloudy.",
                "Says the products are substances that were not there "
                "before, which is what makes it a chemical reaction.",
            ]},
        "produce": {
            "q": "A student says word equations are pointless because you "
                 "could just describe the reaction in a sentence. Give two "
                 "things a word equation forces you to say that a "
                 "description can leave out, and one thing a word equation "
                 "cannot say at all.",
            "field_label": "Your answer",
            "placeholder": "A word equation forces you to name…",
            "success": [
                "Says it forces you to name every reactant, including one "
                "from the air that is easy to forget.",
                "Says it forces you to name the products rather than "
                "describing their appearance.",
                "Says it makes the direction of the change explicit.",
                "Says it cannot show how many particles of each substance "
                "are involved.",
                "Draws the consequence — you cannot work out amounts from a "
                "word equation, which is why symbol equations exist.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "A word equation puts the reactants on the left, the "
                "products on the right, and reads the arrow as “makes”. Plus "
                "means “and”, never add. Only substances appear — not heat, "
                "not energy, not a flame, and not anything that was merely "
                "present. The arrow runs one way, because so does the "
                "reaction.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # Design's two "Going further" paragraphs, whole. The second is where
    # NOTES §5 flag 10 lands on the page: rust is named, and what is said
    # about it is that "iron oxide" names three compounds and rust is a
    # hydrated one — which is the reason there is no rusting case in the
    # builder, stated as chemistry rather than as an apology.
    "stretch": [
        {"type": "explainer", "id": "what-words-cannot-say",
         "text": "Word equations run out of road quickly, and it is worth "
                 "knowing exactly where. They can say which substances react "
                 "and which are made. They cannot say <em>how many</em> "
                 "particles of each — and that turns out to be most of "
                 "chemistry. Two hydrogen particles react with one oxygen "
                 "particle; \"hydrogen + oxygen makes water\" cannot tell "
                 "you that, so it cannot tell you how much oxygen to supply "
                 "or how much water to expect."},
        {"type": "explainer", "id": "the-name-has-to-be-agreed",
         "text": "They also depend on the name being agreed. \"Iron oxide\" "
                 "names three different compounds, and rust is a hydrated "
                 "one, so a word equation for rusting is honest only if "
                 "everyone reading it knows which iron oxide is meant. "
                 "Symbols fix both problems at once, and that is the next "
                 "lesson but one: formulae name the substance exactly, and "
                 "the numbers in front of them say how many."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    # Every technical term this lesson introduces or leans on hard enough to
    # need pinning. `condition` earns its place: it is the word that makes
    # "heat goes above the arrow" a rule rather than an exception, and it is
    # doing that work in the key fact, the key note, rung 2 and two of the six
    # distractor corrections.
    "vocabulary": [
        {"term": "word equation",
         "definition": "A line that names the substances a reaction starts with "
                  "and the substances it ends with, separated by an arrow."},
        {"term": "reactant",
         "definition": "A substance you start with. Reactants go on the left of "
                  "the arrow."},
        {"term": "product",
         "definition": "A substance the reaction makes. Products go on the right "
                  "of the arrow."},
        {"term": "condition",
         "definition": "Something a reaction needs but is not made of — heat, "
                  "light, a catalyst. Conditions are written above the "
                  "arrow, never in the line of substances."},
        {"term": "limewater",
         "definition": "A clear liquid used to test for carbon dioxide. It turns "
                  "cloudy when the gas is bubbled through it."},
    ],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why heat cannot go in the equation?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Balanced symbol equations with state symbols, ionic "
                   "equations, and half equations.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
