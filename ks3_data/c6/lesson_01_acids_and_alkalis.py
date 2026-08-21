"""C6 L1 — Acids and alkalis (CLASSIFY).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c6/c6-01-acids-and-alkalis.dc.html` (601 lines), and
her author's notes `docs/ks3/design-reference/c6/NOTES-C6.md` §1, §3, §5 flags
1, 2, 3, 7, §6 (`ACID-01`, `ACID-02`) and §7.

Every student-facing string is byte-identical to the approved page except
where a change is marked ⚑ below and reported to the commander. `RAIL`,
`BENCH`, `JUDGEMENTS`, `RUNGS` and `SELF_RUNGS` came out of the node extractor;
the hook options and reveal, the three explainer paragraphs, the bench's
eyebrow / heading / lead, the key fact, the hazard block's eyebrow / heading /
lead, the `#s-think` options and its two reveal paragraphs, the key note and
both "Going further" paragraphs were lifted from `lessonVals(s)` and from the
markup, which is where most of this lesson's words live.

── THE BENCH IS BUILT TO PRODUCE ITS OWN PAYOFF ────────────────────────

NOTES-C6 §3 states it: "an eight-bottle sorter (acid / alkali / neutral) with a
where-it-lives tag on each. The reveal is that the most dangerous bottle on the
bench is an alkali."

Everything about the eight is chosen to make that arrive as a finding rather
than as an assertion. Four of the eight are things a student eats, drinks or
has in their own body; the where-it-lives tag puts the acids in the food
cupboard and the alkalis in the cleaning cupboard and the shed; and the closing
panel — which is `ACID-01`'s confrontation, and only opens when all eight are
decided — reads the distribution back rather than announcing it.

⚑ AND THE VERDICT IS ONE SENTENCE, NOT A MARK. Design's page composes
`chosen === row.answer ? 'You said ' + chosen + ' — that is what it is.' :
'It is ' + row.answer + '.'`. That is a mark, assembled in JavaScript, in two
voices, and R3 reserves marking for the mastery ladder. The refinement is
inside the shape she drew — a card, a commitment, a two-paragraph reveal: the
headline is one authored sentence naming what the bottle IS, identical
whichever button was pressed, and her `why` paragraph is unchanged underneath
it. `r_bottle_sorter` reads `answer` at BUILD time and refuses any bottle whose
verdict does not name it, so the flag cannot drift from the sentence.

── SCIENCE FLAGS, ALL RULED, ALL KEPT ──────────────────────────────────

⚑ Flag 1 — "an acid is a substance that releases hydrogen into solution".
KEPT. The raised plus and the word "ion" stay out of the main body; the GCSE
card at the foot names them, at baseline. ⚠️ It CANNOT raise them: that field
goes through `rich()`, whose allow-list is `em`, `strong` and `sub` and has no
`sup`, so a superscript tag there ships its literal characters to a child. See
the note on `ks4_becomes` below.

⚑ Flag 2 — the base/alkali distinction, stated in the explainer and expanded
in the stretch. KEPT. It is what makes `making-a-pure-dry-salt`'s whole method
make sense three lessons later: you can filter off an excess of a base that
will not dissolve, and you cannot filter off an excess of one that will.

⚑ Flag 3 — the classroom pH figures. KEPT, all conventional.

⚑ Flag 7 — sodium hydroxide "turning the fat in your skin into soap". KEPT.
It is saponification, it is true, and it is the sentence that explains why the
lack of pain is the hazard rather than the reassurance.

── SAFEGUARDING: NONE, AND A `safety_note` INSTEAD ─────────────────────

⊖ NO CHILDLINE FOOTER. Ruled by the commander: the footer is for material
touching a student's own body, health or risk in the safeguarding sense —
drugs, alcohol, puberty, mental health, abuse. Oven cleaner and battery acid
are LAB AND HOUSEHOLD SAFETY, which is a different thing, and C5 handled the
same class of content the same way.

⊕ A `safety_note` IS earned, and it is a different thing — small, at the foot,
beside the standing legal line, not a callout. The hazard on this page is
specific and it is the one the page has just taught: an alkali does not
announce itself.
"""

# ── the eight bottles (Design's `BENCH`) ────────────────────────────────
#
# In her order, which is not sorted by answer: kitchen, cleaning cupboard,
# wash bottle, kitchen, chemist, garage, salt in water, shed. A bench sorted
# acid-acid-acid-alkali-alkali would be answerable by position within three
# cards.
#
# ⚑ `verdict` is NEW PROSE and is the only new prose in this list — see the
# docstring for why the composed two-voice headline is not reproduced. Each is
# one sentence naming what the bottle is; `why` is Design's, unchanged.
# `answer` reaches no markup and is read at build time by `r_bottle_sorter`,
# which refuses a bottle whose verdict does not name its own answer.
_BENCH = [
    {"id": "b1", "name": "Lemon juice", "where": "kitchen", "answer": "acid",
     "verdict": "Lemon juice is an acid.",
     "why": "Citric acid, pH about 2. Sharp enough to taste and weak enough "
            "to drink — which is the first sign that acid and danger are "
            "separate questions."},
    {"id": "b2", "name": "Oven cleaner", "where": "cleaning cupboard",
     "answer": "alkali",
     "verdict": "Oven cleaner is an alkali.",
     "why": "Sodium hydroxide, pH about 13. It dissolves baked-on fat by "
            "taking it apart chemically, and it will do the same to skin. The "
            "most dangerous bottle on this bench is not an acid."},
    {"id": "b3", "name": "Pure water", "where": "wash bottle",
     "answer": "neutral",
     "verdict": "Pure water is neutral.",
     "why": "pH exactly 7 — the definition of neutral. Tap water is usually a "
            "shade either side of it depending on what the rock it travelled "
            "through was made of."},
    {"id": "b4", "name": "Vinegar", "where": "kitchen", "answer": "acid",
     "verdict": "Vinegar is an acid.",
     "why": "Ethanoic acid, pH about 3. The same acid that will strip "
            "limescale off a kettle goes on chips."},
    {"id": "b5", "name": "Indigestion tablet in water", "where": "chemist",
     "answer": "alkali",
     "verdict": "An indigestion tablet in water is an alkali.",
     "why": "A mild alkali, pH about 9 or 10 — sold precisely because it "
            "cancels out stomach acid. Mild enough to swallow, which is the "
            "whole point of it."},
    {"id": "b6", "name": "Battery acid", "where": "garage", "answer": "acid",
     "verdict": "Battery acid is an acid.",
     "why": "Sulfuric acid, pH close to 0. This is the one that matches the "
            "mental picture: it burns cloth, skin and metal on contact."},
    {"id": "b7", "name": "Sodium chloride solution", "where": "salt in water",
     "answer": "neutral",
     "verdict": "Sodium chloride solution is neutral.",
     "why": "pH 7. It is made from an acid and an alkali reacting together, "
            "and what is left over sits exactly in the middle — which is the "
            "next lesson but one."},
    {"id": "b8", "name": "Garden lime", "where": "shed", "answer": "alkali",
     "verdict": "Garden lime is an alkali.",
     "why": "Calcium hydroxide, pH about 12. It is spread on soil that has "
            "turned too acidic for crops — neutralisation used on a "
            "field-sized scale."},
]

# ── the three judgements (Design's `JUDGEMENTS`) ────────────────────────
#
# Yes/no on all three, which is Design's own control. Her page has no answer
# key for them at all — the reply is the same paragraph whichever button was
# pressed, and only the ladder marks. `answer` is added HERE, reaches no
# markup, and is read once at build time so that a reply and the verdict it
# reports cannot quietly disagree.
#
# ⭐ `j1` IS `ACID-02`'s ELICITATION SITE and its reply is the confrontation,
# so both carry a real `id` — MRB-244/248 resolve a join against the built
# page and `data-ajudge-card` is not a name a browser exposes.
_JUDGEMENTS = [
    {"id": "j1",
     "dom_id": "judgement-dilute",
     "reveal_id": "judgement-dilute-reveal",
     "q": "A bottle of concentrated acid is diluted with a lot of water. Is "
          "it still an acid?",
     "options": [{"id": "yes", "label": "Yes"}, {"id": "no", "label": "No"}],
     "answer": "yes",
     "reply": "Yes. Diluting adds water, so there is less acid in each cm³ "
              "and it does far less damage — but every drop of it is still "
              "acid and the pH is still below 7. Weaker in effect, unchanged "
              "in kind. That difference between how much acid and how fierce "
              "the acid is has caught out generations of students."},
    {"id": "j2",
     "q": "Someone spills sodium hydroxide on their hand and feels nothing "
          "much. Should they wash it off?",
     "options": [{"id": "yes", "label": "Yes"}, {"id": "no", "label": "No"}],
     "answer": "yes",
     "reply": "Immediately, under running water, for a long time. Alkalis do "
              "not sting on contact the way acids do — they feel soapy, "
              "because they are turning the fat in your skin into soap. By "
              "the time it hurts, the damage is done. The lack of pain is the "
              "hazard."},
    {"id": "j3",
     "q": "Is the acid in your stomach stronger than the acid in vinegar?",
     "options": [{"id": "yes", "label": "Yes"}, {"id": "no", "label": "No"}],
     "answer": "yes",
     "reply": "Considerably. Stomach acid is hydrochloric acid at roughly pH "
              "2; vinegar is around pH 3, and the scale is not evenly spaced "
              "— each step is a factor of ten. Your own stomach is more "
              "corrosive than a bottle of malt vinegar, and it is kept in by "
              "a lining that replaces itself every few days."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 224 character for character.
    "slug":        "acids-and-alkalis",
    "title":       "Acids and alkalis",
    "discipline":  "chemistry",
    "unit":        "acids-and-alkalis",
    "family":      "CLASSIFY",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.C.CR.04` is "defining acids and alkalis in terms of neutralisation
    # reactions", and THIS is the lesson that defines them. `neutralisation`
    # teaches the reaction the definition is made in terms of and TOUCHES the
    # same bullet rather than owning it a second time: `validate()` rule 4
    # fails a statement owned twice, and repetition across lessons is expressed
    # by `touches`, which is the field that exists for it.
    "covers":      ["KS3.C.CR.04"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # The page's "Before this lesson" card links to c5-05. Nothing here needs
    # a reaction type by name, but the unit assumes a student for whom "a
    # reaction makes new substances" already means something specific.
    "requires":    ["which-reaction-is-this"],
    "assumes":     [],
    "references":  [],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Two clear, colourless liquids. One will strip the skin "
                    "off your hand and the other is safe to drink — and "
                    "nothing you can see tells you which is which.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, Design's `RAIL`, in her order with her ids and her short
    # labels. `done_when` restates her own `DONE()`: the hook on a commitment,
    # the bench when all eight bottles are decided, the hazard block when all
    # three judgements are, `#s-think` on a commitment, and the ladder when
    # every rung is answered and both self-marked rungs checked.
    #
    # MRB-208: nothing is ticked on load and credit is a ratchet.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Two beakers", "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "Eight bottles", "done_when": "all_eight_decided"},
        {"anchor": "s-hazard", "short": "JUDGE",
         "label": "Three judgements", "done_when": "all_three_decided"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Which one burns", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚠️ THE HOOK CLOSES EVERY DOOR EXCEPT THE ONE THE LESSON OPENS. "They are
    # the same temperature, they pour the same, they smell of nothing.
    # Everything your eyes can do has already been done" is what makes the
    # answer "add something that changes colour" rather than one more guess:
    # acid and alkali are things a substance DOES, and the only way to read
    # them is to make them act on something.
    "phenomenon": {
        "kind": "narrative",
        "title": "Two beakers, both clear, both colourless. One is "
                 "hydrochloric acid. One is sodium hydroxide.",
        "prompt": "The labels have come off. Both are dangerous, so tasting "
                  "is out and so is touching. They are the same temperature, "
                  "they pour the same, they smell of nothing. Everything your "
                  "eyes can do has already been done.",
        "commit": "How do you find out which is which?",
        # MRB-177: 6, 8, 9, 9 words. The correct option is index 1 and is the
        # SHORTEST of the four. Design's set, unchanged.
        "options": [
            "Smell them from a safe distance",
            "Add a dye that changes colour in each",
            "Weigh equal volumes — the acid will be heavier",
            "Leave them out; the acid will evaporate first",
        ],
        "reveal": "Add something that changes colour. Acid and alkali are not "
                  "things you can see, weigh or smell — they are things a "
                  "substance <strong>does</strong>, and the only way to read "
                  "them is to make them act on something. A dye that turns "
                  "one colour in acid and another in alkali answers the "
                  "question in a second. That dye is called an "
                  "<strong>indicator</strong>, and it is the whole of the "
                  "next lesson.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ BOTH JOINS RESOLVE AGAINST THIS PAGE'S OWN MARKUP (MRB-244/248), and
    # the universe of legal names is exactly `id="…"` and `data-activity="…"`.
    #
    # ⊖ NOTES-C6 §6 proposes `think-reveal-oven-cleaner` for `ACID-01`'s
    # confrontation. NO `think-reveal-*` ID CAN BE EMITTED FROM A LANE: the
    # `#s-think` reveal panel is drawn by `build_ks3.py`'s shared `r_activity`,
    # which emits `<div class="ks3-reveal ks3-reveal-panel" hidden data-reveal>`
    # and NO id, and `build_ks3.py` is not a file this lane may touch. The two
    # confronting paragraphs are INSIDE the activity whose `data-activity` is
    # `think-commit-danger`, so that is what the join names — the same
    # reconciliation `c5-02` made for `REACT-12` and `c4-01` for `REACT-01`. It
    # is also what satisfies Law 3, which requires at least one `confronted_by`
    # to be a real ACTIVITY id.
    #
    # ⊕ `ACID-02`'s two names ARE both emitted, on the judgement card itself:
    # `id="judgement-dilute"` on the card that takes the commitment and
    # `id="judgement-dilute-reveal"` on the panel that answers it. Design's
    # NOTES calls them `judgement-1` / `judgement-1-reveal`; the names are
    # changed to say what they are about rather than where they sit, because a
    # positional name is wrong the moment a judgement is inserted above it.
    "misconceptions": [
        {"id": "ACID-01",
         "statement": "Acids are the dangerous ones. Alkalis are what you use "
                      "to make things safe.",
         "elicited_by": "think-commit-danger",
         "confronted_by": "think-commit-danger"},
        {"id": "ACID-02",
         "statement": "A dilute acid is no longer really an acid.",
         "elicited_by": "judgement-dilute",
         "confronted_by": "judgement-dilute-reveal"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Page lines 105–107 — three paragraphs, so three blocks:
        # `r_explainer` draws one <p>.
        #
        # ⚑ Flag 1 lives in the first of them and flag 2 in the second, both
        # KEPT WHOLE. "Releases hydrogen into solution" avoids H⁺ and the word
        # ion; "a base that dissolves in water is an alkali" is the sentence
        # `making-a-pure-dry-salt` cashes in.
        {"type": "explainer",
         "text": "An <strong>acid</strong> is a substance that releases "
                 "hydrogen into solution when it dissolves in water. That is "
                 "what makes vinegar sharp, what makes your stomach able to "
                 "break down meat, and what makes battery acid eat through "
                 "cloth. Acids have a pH below 7."},
        {"type": "explainer",
         "text": "An <strong>alkali</strong> is the opposite kind of "
                 "substance: it cancels acids out. Alkalis are the ones that "
                 "dissolve; the wider family they belong to is called "
                 "<strong>bases</strong>, and a base that dissolves in water "
                 "is an alkali. Alkalis have a pH above 7."},
        {"type": "explainer",
         "text": "Everything else is <strong>neutral</strong> — pH exactly 7, "
                 "neither one nor the other. Pure water is the obvious "
                 "example, and so is most of what you drink."},

        # #s-bench — the flagship. Light `ks3-block` → `check`.
        #
        # ⚠️ THE LEAD IS NOT A NARRATION OF THE CONTROLS. Design's own line is
        # "N of 8 decided. Guessing is allowed — nothing here is marked, and
        # the ones you get wrong are the ones worth reading." The count is the
        # block head's counter, which is the platform's own live readout; the
        # first clause of the rest is teaching stance and is kept; "nothing
        # here is marked" is platform self-explanation and is cut under §8.10.
        {"type": "bottle-sorter", "id": "bench-eight", "anchor": "s-bench",
         "eyebrow": "Your turn · eight bottles on the bench",
         "heading": "Acid, alkali or neutral? Commit on all eight.",
         "prompt": "Guessing is allowed — the ones you get wrong are the ones "
                   "worth reading.",
         "demand": "classify",
         "head_counter": {"format": "{n} of {total} decided", "start": 0},
         "options": [{"id": "acid", "label": "Acid"},
                     {"id": "alkali", "label": "Alkali"},
                     {"id": "neutral", "label": "Neutral"}],
         "bottles": _BENCH,
         # ⭐ `ACID-01` is not confronted here — its elicitation is in
         # `#s-think` and so is its answer. This panel is the EVIDENCE the
         # think block then argues from, which is why it opens only on the
         # eighth bottle: seven cannot show a distribution.
         "pattern": {"id": "bench-pattern",
                     "title": "Look at where they turn up.",
                     "text": "The acids are in the food cupboard and in your "
                             "own stomach. The alkalis are in the cleaning "
                             "cupboard, and one of them is in the soil bag. "
                             "Neither list is a list of poisons — you eat "
                             "acids every day, and the alkali in indigestion "
                             "tablets is sold in a chemist. "
                             "<strong>Dangerous</strong> and "
                             "<strong>acidic</strong> are two different "
                             "questions, and the bench proves it: the most "
                             "dangerous thing here is an alkali."}},

        {"type": "key-fact", "ref": "either-side-of-seven"},

        # #s-hazard — three judgements. Light `ks3-block` → `check`.
        {"type": "acid-judgements", "id": "hazard-three", "anchor": "s-hazard",
         "eyebrow": "Three judgements",
         "heading": "How dangerous, and why",
         "prompt": "Commit to each before you read what happens. Two of the "
                   "three catch almost everybody.",
         "demand": "explain",
         "head_counter": {"format": "{n} of {total} decided", "start": 0},
         "items": _JUDGEMENTS},

        {"type": "misconception", "id": "think-commit-danger",
         "anchor": "s-think", "targets": "ACID-01"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # None. Design draws no diagram on this page — the bench IS the picture,
    # eight bottles with a where-it-lives tag on each — and §5.4 allows an
    # empty list where it does not allow an absent one.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "either-side-of-seven",
         "text": "Acids have a pH below 7 and alkalis have a pH above 7. An "
                 "alkali is a base that dissolves in water, and it cancels an "
                 "acid out. Neutral is exactly 7.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # `#s-think` only. The two instrument blocks are lifted out of `core` into
    # this list by `_normalise()` and are never authored here.
    "activities": [
        {"id": "think-commit-danger",
         "kind": "predict",
         "demand": "explain",
         "targets": "ACID-01",
         "prompt": "Every hazard film you have seen involves an acid. Commit "
                   "before you read on.",
         # MRB-177: 8, 13, 5, 8 words. The correct option is index 1 and IS
         # strictly the longest, by five words and at 1.63x — the construct
         # §13 measures. The three distractors are re-authored at its own
         # length and in its own shape below; Design's B is untouched and the
         # answer has not moved.
         "options": [
             "Right — alkalis are the safe half of the scale, and acids are "
             "the dangerous half",
             "Wrong — a strong alkali burns as badly as a strong acid, "
             "sometimes worse",
             "Right, because an alkali neutralises an acid and neutral is "
             "always the safe state",
             "Wrong — alkalis are the dangerous ones and acids are the half "
             "you can safely handle",
         ],
         "reveal": [
             "Strong alkalis are, if anything, worse. Sodium hydroxide — the "
             "alkali in oven cleaner and drain unblocker — dissolves fat and "
             "skin, and eye damage from it can be permanent. It does not "
             "sting straight away, which is exactly why people leave it on "
             "their hands. A strong acid announces itself; a strong alkali "
             "feels soapy.",
             "Meanwhile the acid in an orange is safe enough to drink a litre "
             "of. <strong>Being an acid or an alkali says which side of 7 it "
             "sits on. It does not say how hard it hits.</strong> That is a "
             "separate question, and it has its own scale — coming next "
             "lesson.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Design's RUNGS → recall + apply, SELF_RUNGS → explain + produce. Her rung
    # labels are the engine's own defaults character for character, so no rung
    # authors a `title`. `feedback` is keyed by the INT index of each wrong
    # option, which is what `_rung_marked` reads.
    "ladder": {
        # Design's set, untouched, and the answer stays at index 0. MRB-177:
        # 10, 6, 7, 9 words — the correct option is longest by ONE word and at
        # 1.11x, which is ordinary unevenness rather than a tell.
        #
        # MRB-278: index 0 here and index 1 on the rung below. The twelve
        # marked rungs across C6's six lessons are authored level at three
        # apiece, from the start rather than rebalanced afterwards.
        "recall": {
            "q": "What is an alkali?",
            "options": [
                "A base that dissolves in water, with a pH above 7",
                "Any substance that is dangerous to touch",
                "A substance with a pH below 7",
                "A substance that has no effect on an indicator",
            ],
            "answer": 0,
            "feedback": {
                1: "Danger is not the test. Battery acid is dangerous and is "
                   "not an alkali; an indigestion tablet is an alkali you can "
                   "swallow.",
                2: "That is an acid. Alkalis are above 7.",
                3: "Alkalis change indicators strongly — that is how they are "
                   "detected. Nothing here has no effect.",
            }},
        # ⚑ MRB-177 — THE THREE DISTRACTORS ARE RE-AUTHORED AND THE CORRECT
        # OPTION IS UNTOUCHED. Design's set ran 17 words against 11, 11 and 10:
        # strictly the longest by six and at 1.55x, and a student could take it
        # without reading the quotation. Each distractor now states a WRONG
        # RULE in the correct answer's own "being an acid says X" shape and at
        # its own length — 18, 17, 19, 19. Every one of Design's corrections is
        # unchanged and still answers its own option, because each distractor
        # still carries the same wrong idea it always carried: that the taste
        # is not really an acid, that the flaw is about quantity, and that
        # something could be both.
        "apply": {
            "q": "A student says: “Orange juice is an acid, so it must "
                 "be dangerous.” What is wrong with the reasoning?",
            "options": [
                "Being sharp to taste is not the same as being an acid, and "
                "orange juice is only sharp",
                "Being an acid says which side of 7 it sits on, not how "
                "strongly it acts",
                "Being an acid does say how dangerous it is; the flaw is that "
                "one glass is a small amount",
                "Being an acid says how dangerous it is, unless it is an "
                "alkali as well, which cancels that out",
            ],
            "answer": 1,
            "feedback": {
                0: "It genuinely is one: citric acid, pH about 3. The taste "
                   "is the acid.",
                2: "Quantity is a different argument. The flaw is treating "
                   "acidic and dangerous as the same word.",
                3: "Nothing is both. A substance sits on one side of 7 or the "
                   "other.",
            }},
        "explain": {
            "q": "Two unlabelled colourless liquids are on the bench: one is "
                 "an acid and one is an alkali. Explain how you would find "
                 "out which is which, and why looking at them cannot answer "
                 "it.",
            "field_label": "Your explanation",
            "placeholder": "I would add…",
            "success": [
                "Says to add an indicator to a sample of each.",
                "Says the indicator changes to different colours in acid and "
                "in alkali.",
                "Says acid gives a pH below 7 and alkali above 7.",
                "Says being an acid or alkali is a chemical property, so it "
                "cannot be seen.",
                "Says to test a small sample rather than the whole bottle, "
                "and not to taste or touch.",
            ]},
        "produce": {
            "q": "A gardener is told their soil is too acidic for the crop "
                 "they want to grow. Explain what they should add and why it "
                 "works — and say what could go wrong if they add far too "
                 "much.",
            "field_label": "Your answer",
            "placeholder": "They should add…",
            "success": [
                "Says to add an alkali, such as lime or calcium hydroxide.",
                "Says the alkali cancels out or neutralises the acid in the "
                "soil.",
                "Says this raises the pH towards 7.",
                "Says too much would push the soil past neutral and make it "
                "alkaline.",
                "Says the soil should be tested afterwards rather than "
                "assumed to be right.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # Byte-identical. It is the only sentence on the page that states all four
    # of the lesson's claims at once: the two sides of 7, the neutral point,
    # what an alkali is, and that none of it is a statement about danger.
    "key_note": "Acids have a pH below 7, alkalis above 7, and neutral "
                "substances exactly 7. An alkali is a base that dissolves in "
                "water, and the two cancel each other out. Whether something "
                "is acidic tells you nothing about whether it is safe: lemon "
                "juice is an acid you can drink and oven cleaner is an alkali "
                "that will burn you.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ Flag 2's expansion is the first paragraph and it is kept whole: it is
    # the method `making-a-pure-dry-salt` is built on, arriving here as the
    # reason the base/alkali distinction is worth having at all.
    "stretch": [
        {"type": "explainer", "id": "bases-that-do-not-dissolve",
         "text": "Not every base is an alkali. Copper oxide, magnesium oxide "
                 "and calcium carbonate all neutralise acids perfectly well, "
                 "but they barely dissolve in water — so they are bases and "
                 "not alkalis. The distinction matters in the lab: to "
                 "neutralise an acid with a base that will not dissolve, you "
                 "warm the acid and stir the solid in until no more will "
                 "react, then filter off what is left. That is a method you "
                 "will meet again when you make a salt on purpose."},
        {"type": "explainer", "id": "your-own-stomach",
         "text": "Your stomach runs at about pH 2, which is strong enough to "
                 "dissolve iron filings and does dissolve the meat you eat. "
                 "The lining survives because it is replaced constantly and "
                 "coated in mucus; where that coating fails, the acid attacks "
                 "the stomach itself and the result is an ulcer. For a long "
                 "time ulcers were treated as a stress problem. In 1984 an "
                 "Australian doctor drank a flask of bacteria to prove they "
                 "were an infection, gave himself gastritis, and eventually "
                 "won a Nobel Prize for it."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    # ⚠️ The key is `definition`, NOT `gloss` — `build_ks3.py` hard-indexes
    # `v["definition"]`.
    "vocabulary": [
        {"term": "Acid",
         "definition": "A substance that releases hydrogen into solution when "
                       "it dissolves in water. Acids have a pH below 7."},
        {"term": "Alkali",
         "definition": "A base that dissolves in water. Alkalis have a pH "
                       "above 7 and they cancel acids out."},
        {"term": "Base",
         "definition": "Any substance that cancels an acid out. The ones that "
                       "dissolve in water are called alkalis; plenty of "
                       "others do not dissolve.",
         "note": "Every alkali is a base. Most bases are not alkalis."},
        {"term": "Neutral",
         "definition": "Neither acidic nor alkaline — pH exactly 7. Pure "
                       "water is the standard example."},
        {"term": "pH",
         "definition": "The number that says how acidic or alkaline "
                       "something is. Below 7 is acidic, 7 is neutral, above "
                       "7 is alkaline."},
        {"term": "Indicator",
         "definition": "A dye that changes colour depending on whether it is "
                       "in an acid or an alkali. It is how the two are told "
                       "apart when looking cannot."},
        {"term": "Corrosive",
         "definition": "Able to attack and destroy materials it touches, "
                       "including skin. Strong acids and strong alkalis are "
                       "both corrosive."},
    ],

    # ── safety (§1.5) — not a callout, and not a safeguarding block ─────────
    # ⚑ NEW PROSE, and the only new prose outside the bench verdicts. Reported
    # to the commander (contract §16) rather than added silently.
    #
    # ⊖ NO SAFEGUARDING BLOCK, and that is the commander's ruling: the
    # Childline footer is for material touching a student's own body, health or
    # risk in the safeguarding sense. Household and lab hazards are health
    # education and take a plain safety note, as C5's do.
    #
    # Scoped so it does not retract the lesson's own content. It does not say
    # "never touch a cleaning product" — the page is about the ones under
    # everybody's sink — and it does not contradict the judgement block, which
    # says to wash immediately; it names the thing that makes that judgement
    # hard, which is that there is nothing to feel.
    "safety_note": "Oven cleaner and drain unblocker are strong alkalis and "
                   "battery acid is a strong acid. None of them is a thing to "
                   "test at home: a strong alkali does not hurt on contact, "
                   "so there is no signal telling you to wash it off, and by "
                   "the time there is one the damage is done.",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still unsure why a base is not always an alkali?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⚑ Flag 1's ion notation lives HERE and nowhere else, and it is written
    # at BASELINE rather than raised.
    #
    # ⚠️ `ks4_becomes` GOES THROUGH `rich()`, WHOSE ALLOW-LIST IS `em`,
    # `strong` and `sub` — THERE IS NO `sup`. A `<sup>+</sup>` here would be
    # escaped and would ship the literal characters `&lt;sup&gt;` to a child.
    # Design's page can raise it because it is hand-written HTML; this field
    # cannot, so the charge is written on the line: `H+` and `OH−`, with
    # U+2212 for the minus, which IS in the shipped subsets. The ions are named
    # in words as well, which is what a KS3 reader needs from this card anyway.
    "ks4_becomes": "Acids as sources of hydrogen ions (H+) in solution, "
                   "alkalis as sources of hydroxide ions (OH−), and the "
                   "difference between a strong acid and a concentrated one.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["scientific-attitudes", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
