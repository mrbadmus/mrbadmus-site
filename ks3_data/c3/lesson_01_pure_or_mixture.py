"""C3 L1 — Pure or mixture? (CLASSIFY).

Authored against Design's approved page,
`docs/ks3/design-reference/c3/c3-01-pure-or-mixture.dc.html` (685 lines), and
her unit notes, `docs/ks3/design-reference/c3/NOTES-C3.md` §§1–6.

Every student-facing string below is byte-identical to the approved page.
`RAIL`, `SAMPLES`, `CARDS`, `RUNGS` and `SELF_RUNGS` came out of the node
extractor; the hook and think options, the tally format, the two verdict
button labels, the all-decided close and the explainer paragraphs were lifted
from `lessonVals()` and from the markup, where between 240 and 900 words a
lesson live and where a lift of the top-level constants alone loses them.

── One question, asked eight times ──────────────────────────────────────

NOTES §2: the flagship is deliberately **not** C2's test-budget bench. There
is no budget, no evidence economy and no sequencing — eight independent
commitments, because the teaching point is the repeated application of ONE
question. Three of the eight are labelled or sold as pure and are mixtures
(the juice, the ring, the milk); one is invisible and is pure (the oxygen),
sitting beside an invisible sample that is not (the air). MIX-02 — *if it
looks the same all the way through, it is pure* — is the spine of the whole
unit, and this is the first of its three confrontations.

⚖️ **THE INGREDIENT LIST IS HIDDEN UNTIL THE STUDENT COMMITS.** Design's
`showIngredients` is `showAll || decided`, with the `revealIngredients` prop
defaulting to FALSE. That gate is the instrument: a card that shows "37.5%
gold, the rest copper and silver" before the student presses anything is a
reading exercise, not a decision. The drawer must keep it, along with the
one-shot commit — `verdicts[x.id]` is never overwritten once set.

`showParticles` (default TRUE) is Design's other dial. The particle strips are
DOM circles, each carrying its own `aria-label` from `diagramLabel`, and they
are authored here for all eight samples.

── Reproduced, not corrected ───────────────────────────────────────────

* **The instrument never marks.** Every card opens its verdict panel on the
  student's commitment, whether or not that commitment was right, and the
  panel is one tone either way (R3). `pure` is authored on every sample per
  NOTES §3.1 and is read by NOTHING — correctness data waiting for a marker
  that R3 says must not arrive here. Kept and flagged, exactly as c2-02 keeps
  its unread `element`.

── Corrected ───────────────────────────────────────────────────────────

* **The think-again reveal no longer puts a number on it.** Design wrote
  "Distilled water is pure and will keep you alive for about a week before
  something else kills you." The teaching point is right — pure says how many
  substances, not how good — but the week is not, and it is the kind of number
  a student can check and find wrong. RULED (MRB-246): the timescale comes out
  and the point stays. The clause is now "Distilled water is pure and has
  nothing in it you could live on", which is a claim about composition, which
  is what the paragraph is about, and it runs parallel to the sodium clause
  beside it rather than cutting across it.

* **"Four pure, four mixtures" was wrong and is now "Three pure, five
  mixtures".** The close paragraph on the approved page quotes a count the
  instrument beside it contradicts: the eight samples are three pure (the
  distilled water, the oxygen, the sugar) and five mixtures. §6 of the
  authoring brief — the instrument is the measurement and the prose changes —
  so the sentence moved and not a sample. Nothing else in the paragraph is
  touched; the three uniform-looking mixtures it names are all still there.

⚑ For Mide's science gate:
  * None of NOTES §4's fifteen numbered flags falls on this lesson.
  * "Under a third of it by count is gold" (the ring). True — 9-carat gold is
    37.5% gold BY MASS, and gold atoms are heavy, so by count it is nearer a
    sixth. The looser statement is the true one and it stays.
"""

# ── the particle strips (NOTES §3.1) ─────────────────────────────────────
#
# Design's `dots()` and her three colours, transliterated rather than
# retyped: the style strings this produces were diffed against the extracted
# payload (`payloads/c3-01-pure-or-mixture.json`) and are byte-identical for
# all eight samples, all one hundred circles.
#
# ⚠️ The three hex literals are Design's, on her page, in an inline style on a
# DOM element. They are NOT the SVG-art ruling's territory (that binds drawers
# emitting inline SVG to `--ks3-*` tokens, and there is no SVG here) — but
# `#E4572E` is `--ks3-accent` spelled out, and a drawer that wants tokens
# instead needs Design's word, not mine. Raised in the report.
BLUE = "#2F5D8A"
ORANGE = "#E4572E"
GREY = "#8C8377"


def _dots(spec):
    """`[(count, colour, big), …]` → the strip Design's `dots()` builds."""
    out = []
    for count, colour, big in spec:
        px = "15" if big else "11"
        for _ in range(count):
            out.append({"style": "display:block;width:%spx;height:%spx;"
                                 "border-radius:99px;background:%s;"
                                 "border:1.5px solid var(--ks3-ink);"
                                 % (px, px, colour)})
    return out


# ── the eight samples ────────────────────────────────────────────────────
#
# Page lines 445–518. The order is Design's and it is doing work: the two
# invisible samples (4 and 6) are separated so the second one lands as a
# surprise, and the three uniform-looking mixtures (2, 7, 8) are spread out
# rather than grouped, so the student meets the same trap three times without
# noticing it is the same trap.
# ⊕ MRB-272 — `pure` REMOVED, AND THE REASON IS TWO RULES MEETING.
#
# Each sample carried a boolean `pure`. Nothing read it, and nothing was ever
# going to: R3 and MRB-196 R10 say only the mastery ladder marks correctness,
# so a renderer that reached for this flag would be marking an option button
# outside the ladder — the one thing this instrument must not do. It was
# authored as documentation of which samples are which.
#
# R5 is explicit that this is not enough: a key with no read site is content
# that never reaches a student, and *"it documents intent" is not a read
# site — put it in a comment*. So here is the comment.
#
#     PURE (3)     distilled water · oxygen from a cylinder · granulated sugar
#     MIXTURE (5)  orange juice · sea water · air · 9-carat gold ring · milk
#
# Nothing is lost from the page. `verdict` names the answer in a word and
# `why` argues it, and BOTH ARE READ — they are what opens on the card when
# the student commits. The flag was a second source for a fact the strings
# already carry, which is exactly the drift shape §5A.1 warns about.
#
# ⚠️ Three of the five mixtures are LABELLED OR SOLD AS PURE (the juice, the
# ring, and sea water read as "just water"), and one of the three pure ones
# is invisible (the oxygen). That distribution is the lesson, and it is why
# the samples are interleaved rather than grouped.
SAMPLES = [
    {"id": "water", "name": "Distilled water",
     "look": "A colourless liquid from the bottle on the prep-room shelf.",
     "ingredients": "Water and nothing else.",
     "dots": _dots([(14, BLUE, False)]),
     "diagramLabel": "A particle diagram of distilled water: fourteen "
                     "identical particles, all the same kind.",
     "verdict": "Pure.",
     "why": "One substance. Every particle in the bottle is a water particle, "
            "and you cannot make it more or less watery."},
    {"id": "juice", "name": "Orange juice, \"100% pure\"",
     "look": "Cloudy orange, straight from the carton in the fridge.",
     "ingredients": "Water, three sugars, citric acid, pulp, vitamin C, and "
                    "more.",
     "dots": _dots([(7, BLUE, False), (3, ORANGE, True), (2, GREY, False),
                    (2, ORANGE, False)]),
     "diagramLabel": "A particle diagram of orange juice: mostly water "
                     "particles with several different other kinds mixed "
                     "among them.",
     "verdict": "Mixture.",
     "why": "Dozens of substances, and the amounts differ between oranges. "
            "Nothing was added — that is what the label claims — but plenty "
            "is in there."},
    {"id": "sea", "name": "Sea water",
     "look": "Clear, colourless, and it tastes of salt.",
     "ingredients": "Water with sodium chloride and several other salts "
                    "dissolved in it.",
     "dots": _dots([(11, BLUE, False), (3, ORANGE, False)]),
     "diagramLabel": "A particle diagram of sea water: water particles with a "
                     "few dissolved salt particles spread evenly among them.",
     "verdict": "Mixture.",
     "why": "The Dead Sea is nine times saltier than the Atlantic and both "
            "are sea water. A composition you can vary is the signature of a "
            "mixture."},
    {"id": "oxygen", "name": "Oxygen from a cylinder",
     "look": "Invisible. You cannot see it, smell it or taste it.",
     "ingredients": "Oxygen and nothing else.",
     "dots": _dots([(9, GREY, False)]),
     "diagramLabel": "A particle diagram of oxygen gas: nine identical "
                     "particles, far apart.",
     "verdict": "Pure.",
     "why": "Being invisible tells you nothing about purity. This cylinder "
            "holds one substance; the air outside it holds several."},
    {"id": "sugar", "name": "Granulated sugar",
     "look": "White crystals from a paper bag.",
     "ingredients": "Sucrose and nothing else.",
     "dots": _dots([(12, ORANGE, True)]),
     "diagramLabel": "A particle diagram of sugar: twelve identical large "
                     "particles packed in a regular arrangement.",
     "verdict": "Pure.",
     "why": "A bag of sugar is one substance, sucrose, refined until nothing "
            "else is left. Being made in a factory does not make it impure."},
    {"id": "air", "name": "Air",
     "look": "Invisible, exactly like the oxygen.",
     "ingredients": "Nitrogen, oxygen, argon, carbon dioxide, water vapour.",
     "dots": _dots([(6, BLUE, False), (2, GREY, False), (1, ORANGE, False)]),
     "diagramLabel": "A particle diagram of air: mostly nitrogen particles "
                     "with fewer oxygen particles and one other kind among "
                     "them.",
     "verdict": "Mixture.",
     "why": "Several gases, and the proportions change with where you are "
            "standing. Two invisible samples, two different answers."},
    {"id": "ring", "name": "A 9-carat gold ring",
     "look": "Uniform, shiny, gold-coloured all the way through.",
     "ingredients": "37.5% gold, the rest copper and silver.",
     "dots": _dots([(5, ORANGE, True), (6, GREY, True), (3, BLUE, True)]),
     "diagramLabel": "A particle diagram of 9-carat gold: three different "
                     "kinds of particle packed together in one regular "
                     "arrangement.",
     "verdict": "Mixture.",
     "why": "Under a third of it by count is gold. It is uniform, hard-wearing "
            "and worth having — and it is a mixture, on purpose."},
    {"id": "milk", "name": "Milk",
     "look": "Uniform white, with no bits you can pick out.",
     "ingredients": "Water, fats, proteins, sugars, minerals.",
     "dots": _dots([(8, BLUE, False), (3, GREY, True), (3, ORANGE, False)]),
     "diagramLabel": "A particle diagram of milk: water particles with larger "
                     "fat particles and other kinds dispersed through them.",
     "verdict": "Mixture.",
     "why": "Leave it to stand and the cream rises, which no pure substance "
            "ever does. Looking uniform is not the same as being one "
            "substance."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 198 character for character.
    "slug":        "pure-or-mixture",
    "title":       "Pure or mixture?",
    "discipline":  "chemistry",
    "unit":        "mixtures-and-separation",
    "family":      "CLASSIFY",

    # ── curriculum position ─────────────────────────────────────────────────
    # ⚑ NOTES §1 splits PIS.02 deliberately: this lesson teaches what a mixture
    # IS, and `dissolving-and-solutions` teaches the one kind of mixture the
    # statutory wording singles out. Teaching both in one sitting is what
    # produces students who think dissolving is the definition of mixing.
    # `KS3.C.PIS.02a` is the mixture half, minted for C3 in
    # `ks3_data/substatements.py`; `dissolving-and-solutions` owns `02b`. The
    # parent is therefore never owned, which is what §4.4 rule 3 and the
    # PARENT-AND-CLAUSE gate require.
    "covers":      ["KS3.C.PIS.01", "KS3.C.PIS.02a"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 1},
                    {"id": "particles", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # NOTES §6: c3-01 links back to c2-06, which exists.
    "requires":    ["conservation-of-mass"],
    "assumes":     [],
    "references":  ["dissolving-and-solutions"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "A carton of juice, a gold ring and a bottle of lab water "
                    "all claim to be pure. Only one of them is — so what is "
                    "the chemist actually asking?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FIVE stops, from `RAIL` (page lines 320–326). No mirrors: Design's
    # `DONE()` gives every stop its own predicate.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "Two labels",
         "done_when": "committed"},
        {"anchor": "s-sorter", "short": "SORT",   "label": "Eight samples",
         "done_when": "all_samples_decided"},
        {"anchor": "s-words",  "short": "WORDS",  "label": "Four words",
         "done_when": "all_cards_flipped"},
        {"anchor": "s-think",  "short": "THINK",  "label": "Pure juice",
         "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    "phenomenon": {
        "kind": "narrative",
        "title": "One of these two labels means nothing to a chemist.",
        "prompt": "A carton says <strong>100% pure orange juice</strong>. A "
                  "bottle in the lab says <strong>distilled water</strong>. "
                  "Both are honest labels. Only one of them describes "
                  "something a chemist would call pure.",
        "commit": "Which one is pure, and what is the word doing in the other?",
        "options": [
            "The juice — it says 100% pure on the carton",
            "The water — it is one substance and the juice is many",
            "Both — neither has anything added to it",
            "Neither — nothing is ever completely pure",
        ],
        "reveal": "The water is pure. The juice contains water, three "
                  "different sugars, citric acid, pulp, vitamin C and more — "
                  "dozens of substances, and no two cartons contain quite the "
                  "same amounts. On the carton, <em>pure</em> means nothing "
                  "was added to it. To a chemist it means something far "
                  "stricter: one substance, and nothing else.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Statements stored WITHOUT curly quotes; the renderer adds them.
    #
    # ⚠️ MIX-01's statement is the page's own `.ks3-mis-quote`, not NOTES §5's
    # summary of it ("Pure means clean, natural or with nothing added"). The
    # quote is what `_misconception_quote` prints into #s-think, so the
    # register's wording and the page's wording cannot differ without the page
    # ceasing to be Design's. The register keeps the ID and the meaning; the
    # string is the student-voice one Design drew.
    #
    # ⚠️ `elicited_by` / `confronted_by` resolve against names the BUILT PAGE
    # emits — `id="…"` or `data-activity="…"` — and MRB-244/248 gate both. So
    # NOTES §5's proposed handles `hook-two-labels`, `think-again-juice`,
    # `sample-ring` and `sorter-reveal` land as follows: `think-again-juice`
    # survives as the predict activity's own id; `hook-two-labels` becomes
    # `s-hook`, the section that carries the two labels and the commitment;
    # and `sample-ring` / `sorter-reveal` are two MOMENTS inside one
    # instrument, which the DOM can only name once — `eight-samples` — because
    # the ring's card and the reveal that follows it are the same activity.
    # Same shape as c2-02's ATOM-04/05, both of which name `six-samples`
    # twice.
    "misconceptions": [
        {"id": "MIX-01",
         "statement": "It says 100% pure on the carton, and there is nothing "
                      "bad in it, so it is pure.",
         "elicited_by": "s-hook",
         "confronted_by": "think-again-juice"},
        {"id": "MIX-02",
         "statement": "If it looks the same all the way through, it is pure.",
         "elicited_by": "eight-samples",
         "confronted_by": "eight-samples"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Design draws ONE `.ks3-explainer` section carrying two paragraphs;
        # `r_explainer` emits one `<p>` per block, so the paragraphing is kept
        # by authoring two. The second is the one that does the work — it is
        # the test, not the definition.
        {"type": "explainer",
         "text": "A <strong>pure substance</strong> contains one substance and "
                 "nothing else — every particle in it is the same kind. A "
                 "<strong>mixture</strong> contains two or more substances "
                 "that are not chemically joined, and its recipe can be "
                 "varied: you can make sea water saltier, or brass with more "
                 "copper in it, and it is still sea water and still brass."},
        {"type": "explainer",
         "text": "That second half is the useful test. A pure substance has a "
                 "<strong>fixed composition</strong> you cannot change without "
                 "turning it into something else. A mixture does not."},

        # #s-sorter — the flagship. A LIGHT `.ks3-block` (→ `check`): C3 has no
        # ink-dark practical block on any of its seven pages.
        {"type": "purity-sorter", "id": "eight-samples", "anchor": "s-sorter",
         "eyebrow": "Your turn · eight samples on the bench",
         "heading": "Pure, or mixture? Decide on all eight.",
         "head_counter": {"format": "{n} of 8 decided", "total": 8,
                          "tone": "accent"},
         "demand": "classify",
         "targets": "MIX-02",
         "prompt": "Commit before you read the answer. Three of these are "
                   "labelled or sold as pure and are not; one of them you "
                   "cannot even see.",
         # The two buttons on every card, in Design's order. One shot: once a
         # card is decided both buttons disable and the verdict opens.
         "options": ["Pure substance", "Mixture"],
         # The card's mono eyebrow. `{n}` is the sample's position, 1-based.
         "sample_label": "Sample {n}",
         "samples": SAMPLES,
         # ⚖️ CORRECTED COUNT — see the module docstring. Design's page says
         # "Four pure, four mixtures"; the eight samples beside it are three
         # and five.
         "close": "Three pure, five mixtures — and not one of the eight was "
                  "settled by looking at it. The gold ring, the milk and the "
                  "juice all look completely uniform and all three are "
                  "mixtures; the oxygen is invisible and is pure. Every "
                  "verdict came down to the same question: is there one "
                  "substance in there, or more than one?"},

        {"type": "key-fact", "ref": "one-substance-fixed"},

        # #s-words — `ks3-block ks3-keywords`, four flip cards. The FIRST
        # `keyword` block authored in the key stage: Design has drawn no
        # keyword section on any page before this one.
        {"type": "keyword", "anchor": "s-words",
         # Design's own head and lead, lifted from the approved
         # page. `r_keyword` fell back to "Words to know" and a
         # softer lead until MRB-272 made both authorable.
         "eyebrow": "Four words",
         "lead": "Say your answer out loud before you turn each "
                 "card over. If you cannot say it, you do not "
                 "know it yet.",
         "terms": ["Pure substance", "Mixture", "Composition", "Impurity"]},

        {"type": "misconception", "id": "think-again-juice", "anchor": "s-think",
         "targets": "MIX-01"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "one-substance-fixed",
         "text": "A pure substance contains only one substance, in a fixed "
                 "composition. A mixture contains more than one, in any "
                 "proportion you like — and looking uniform is no evidence "
                 "either way.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── the flip cards (Law 7) ──────────────────────────────────────────────
    # Design's `CARDS` (page lines 520–525): front → term, def → definition,
    # note → note. The `keyword` block above selects all four, in this order.
    "vocabulary": [
        {"term": "Pure substance",
         "definition": "A substance containing only one substance — every "
                       "particle the same kind.",
         "note": "Fixed composition. You cannot make it more or less of "
                 "itself."},
        {"term": "Mixture",
         "definition": "Two or more substances together, not chemically "
                       "joined.",
         "note": "The proportions can be varied and it is still the same "
                 "mixture."},
        {"term": "Composition",
         "definition": "What a sample is made of, and how much of each.",
         "note": "Fixed for a pure substance; adjustable for a mixture."},
        {"term": "Impurity",
         "definition": "Anything present that is not the substance you "
                       "wanted.",
         "note": "Not the same as dirt. An impurity can be perfectly clean."},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # Hand-authored: `_normalise()` lifts INSTRUMENT blocks out of `core` and
    # appends them to whatever is already here, so the predict lives here and
    # the sorter arrives on top of it.
    "activities": [
        {"id": "think-again-juice",
         "kind": "predict",
         "demand": "explain",
         "targets": "MIX-01",
         "prompt": "Everything in that sentence is true about the juice. "
                   "Commit before you read on.",
         "options": [
             "It is pure — nothing was added to it",
             "It is not pure — it contains many substances, added or not",
             "It is pure until you add sugar to it",
             "It is pure because it came from real oranges",
         ],
         "reveal": [
             "The carton is not lying. In food labelling, <em>pure</em> means "
             "nothing was added — no water, no sugar, no preservative. It is "
             "a promise about what was <strong>put in</strong>. A chemist's "
             "<em>pure</em> is a claim about what is <strong>there</strong>: "
             "one substance only. Orange juice fails that on its own, with "
             "nothing added at all.",
             "The same word is used for clean, safe, natural and untouched, "
             "and none of those are chemistry. Distilled water is pure and "
             "has nothing in it you could live on. Pure sodium is pure and "
             "will set fire to your hand. "
             "<strong>Pure says how many substances, not how good.</strong>",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # `RUNGS` → recall + apply, `SELF_RUNGS` → explain + produce. Design's four
    # headings are already the engine's four defaults — "Recall", "The one that
    # catches people", "Explain", "Take it somewhere new" — so no rung needs a
    # `title` override to render the page's own words.
    "ladder": {
        "recall": {
            "q": "What does a chemist mean by a pure substance?",
            "options": [
                "It has had nothing added to it",
                "It contains only one substance",
                "It is clean and safe to drink or eat",
                "It is natural rather than made in a factory",
            ],
            "answer": 1,
            "feedback": {
                0: "That is the food-label meaning. Orange juice has had nothing added and contains dozens of substances.",
                2: "Pure sodium will set fire to your hand and pure carbon monoxide will kill you. Purity is a count, not a safety rating.",
                3: "Sea water is natural and is a mixture; factory-refined sugar is pure. Where it came from is not the test.",
            }},
        "apply": {
            "q": "Which one of these is a pure substance?",
            "options": [
                "Sea water that has been filtered until it is completely clear",
                "Nitrogen from a gas cylinder",
                "Rainwater collected in a clean jar",
                "Milk labelled \"no additives\"",
            ],
            "answer": 1,
            "feedback": {
                0: "Filtering removed the bits you could see. Everything dissolved in it is still there — clear is not pure.",
                2: "Rain falls through the atmosphere and arrives with dissolved gases and dust in it. Clean, and still a mixture.",
                3: "\"No additives\" is a promise about what was put in. Milk is water, fats, proteins and sugars before anyone adds anything.",
            }},
        "explain": {
            "q": "A student filters sea water until it is completely clear and says \"it is pure now — look at it\". Explain why the sample is not pure, and what the clearness does tell you.",
            "field_label": "Your explanation",
            "placeholder": "Filtering removed…",
            "success": [
                "Says the salt is dissolved, so it passes straight through the filter paper.",
                "Says the sample still contains more than one substance, so it is still a mixture.",
                "Says clearness only tells you there are no undissolved bits left.",
                "Gives a test that would show the salt is still there — taste, boil it dry, or weigh what is left.",
                "Notes that \"looks uniform\" is never evidence of purity.",
            ]},
        "produce": {
            "q": "A bottle of mineral water lists fourteen dissolved minerals on the label and calls itself pure. A ring is sold as 9-carat gold and is only 37.5% gold. Neither seller is breaking the law. Explain what \"pure\" is doing in the first case, why the ring is deliberately not pure, and what a chemist would say about both.",
            "field_label": "Your answer",
            "placeholder": "On the label, pure means…",
            "success": [
                "Says the label uses pure to mean untouched or nothing added, not one substance.",
                "Says a chemist would call the mineral water a mixture, because of the dissolved minerals.",
                "Says pure gold is too soft for a ring, so other metals are added on purpose.",
                "Says the ring is therefore a mixture by design, not by carelessness.",
                "Draws the general point — one word, two meanings, and only one of them is chemistry.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "A pure substance contains one substance only, and its "
                "composition is fixed. A mixture contains two or more "
                "substances, not chemically joined, in proportions you can "
                "vary. Neither can be identified by looking: air and oxygen "
                "are both invisible, and only one of them is pure.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # Design draws two paragraphs under "Going further"; one block each, for
    # `r_explainer`'s reason.
    "stretch": [
        {"type": "explainer", "id": "two-meanings-in-law",
         "text": "Chemists and food labels are both allowed their meanings, "
                 "and the law is on the label's side: in the UK, calling a "
                 "juice \"100% pure\" is a claim that nothing was added, not a "
                 "claim about composition. The chemist's version is the one "
                 "that matters when it has to work — paracetamol is sold at "
                 "99.9% purity, and the missing 0.1% is checked, named and "
                 "limited, because a tablet is swallowed by someone who "
                 "cannot inspect it."},
        {"type": "explainer", "id": "impure-on-purpose",
         "text": "Some things are deliberately made impure. Pure gold is soft "
                 "enough to mark with a fingernail, so a ring is an alloy — "
                 "9-carat gold is only 37.5% gold, and it lasts. Pure iron is "
                 "soft too; adding a little carbon makes steel. In the same "
                 "way, road salt is not pure sodium chloride, and that is on "
                 "purpose. Mixtures designed for a job have their own name at "
                 "GCSE: formulations."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why the gold ring counts as a mixture?",
              "cta": "Ask about this lesson",
              "anchor": "s-sorter"},

    "ks4_becomes": "Pure substances have sharp melting points, and mixtures "
                   "designed for a job — paints, fuels, alloys, medicines — "
                   "are called formulations.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
