"""B3 L2 — Food tests (INVESTIGATION).

Authored against Design's approved page,
`docs/ks3/design-reference/b3/b3-02-food-tests.dc.html` (643 lines), under the MRB-220 build
contract.

Every student-facing string is lifted from the approved page except the three
listed under "What could not be lifted", none of which is a sentence of
science.

── `covers` is a Working Scientifically statement, and that is the rule ──

architecture.md §5.7.1: an INVESTIGATION lesson teaches no new subject content
by design — this one tests what four colour changes are worth — so it anchors
`covers` on the WS statement it actually delivers. `KS3.WS.ANA.03` is *interpret
observations and data, including identifying patterns and using observations,
measurements and data to draw conclusions*, which is this lesson in one line:
every result panel ends in the sentence the student is licensed to write, and
for a negative it is the hedged one. WS statements are exempt from §5.7's
exactly-once rule, so this collides with nothing — and NOTES-B3 §1 records the
slot as carrying no NUT statement of its own, which is the same finding.

The precedent is `ks3_data/c1/lesson_06_testing_the_model.py`, which anchors on
`KS3.WS.ATT.02` for the same reason.

── The flagship: predicting is what RUNS the test ───────────────────────

`#s-bench` is `test-bench`, on `ks3-block ks3-dark ks3-practical` (page line
105). Five foods × four tests = twenty combinations, each gated by its own
two-option prediction, and there is no separate run control: **the commitment
IS the action**. A student who could watch the tube first and decide afterwards
what they thought has not predicted anything.

⚖️ EVERY RESULT ENDS IN A CLAIM LINE, ruled off from the explanation above it.
NOTES-B3 §2 makes it the pattern of the whole lesson — *what may you write
down* — and the four deliberate false negatives (potato/Biuret at 2% protein,
apple juice/Biuret at 0.3%, and the two that are TRUE negatives and say so) are
only teachable because the licensed sentence is printed under every one of
them. `r_test_bench` raises without both claim templates.

⚖️ THE TUBE'S COLOURS ARE REAL AND ARE NOT TOKENS. NOTES-B3 §3.2 is explicit:
Benedict's blue #2E63B8 to brick red #B03A16, iodine's orange-brown to
blue-black, and so on. They are authored as literal hex on each test, and the
parity drive asserts the tube never resolves to `--ks3-accent` or
`--ks3-alert` — an accent-tinted tube would be teaching a colour change that
does not happen.

── FOUR rail stops — Design's fourth restored (MRB-249) ─────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that
`#s-limits` came off the rail. Design draws FOUR stops and `#s-limits` ticks on
`Object.keys(s.ran).length >= 4` (page line 455) — the BENCH's predicate,
verbatim, one section to the left — and since `#s-limits` is an eyebrow, a
display line, three static cards and a key fact with no control, no commit and
no field, MRB-208's "the rail carries only sections that require the student to
do something" looked to rule it out. So the lesson shipped THREE stops.

Two things overrule that inference.

MRB-205 binds and is not re-argued: Design draws, we render; no invented or
dropped page structure; page wins over engine. Dropping a stop Design drew is
not rendering what Design drew.

And Design's `isDone()` states the tick condition rather than leaving it to be
inferred. It is a rail-level function and it returns the identical expression
for `#s-bench` and then for `#s-limits`. That repetition is not a slip: the
three cards are the payoff of the four tests beside them, and the section holds
no control because the bench has already taken the student's commitment. It is
a MIRROR, and `wireRail`'s `paint()` in `shared/ks3.js` resolves mirrors at
rail level.

So the fourth stop is declared: anchor `s-limits`, `mirrors: "s-bench"`,
`done_when: "four_combinations_run"` — the bench's own predicate, named as
borrowed rather than smuggled, and gated by
`ks3_parity.check_rail_matches_design` against `docs/ks3/rail-manifest.md`.
c1-02's `#s-matrix`, b3-01's `#s-nutrients` and b3-07's `#s-four` are restored
the same way. The section keeps its anchor, as it always did, so the tutor
card's `#s-limits` link and every hash link into it still work.

── What could not be lifted, and why ────────────────────────────────────

1. **The three `It cannot say` tags on the limit cards.** Design's card is
   three parts — a mono uppercase tag, the question in display 700, the answer
   in body — and `r_rule`'s card is two, `term` and `gloss`. The tag is the
   same string on all three cards and the statement above them already says it
   ("Three questions these tests cannot answer."), so it is DROPPED rather than
   folded into a question it would change. Reported; the fix, if the card is to
   win, is a `tag` key on a rule card.

2. **The key fact leaves Design's band panel.** She nests it inside
   `#s-limits`; `r_rule` has no nested key-fact slot (only `r_comparison`
   does), so it renders as its own top-level block directly under the panel, on
   the band ground every other top-level key fact in the key stage takes. The
   words are unchanged and the order is unchanged.

3. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose and §4.8.1 D makes the two mutually exclusive. The KS4 bridge
   edge is what is given up; c1-06, b3-01, b3-07 and all six C2 lessons resolve
   it the same way.

⚑ For Mide's science gate:
  * NOTES-B3 §4 flag 5 — the four false negatives are DESIGNED IN rather than a
    clean grid, and flag 6 asks whether the sucrose case belongs at KS3. Both
    are authored as delivered: the twenty notes below carry them, and the
    stretch layer is the sucrose one.
  * ⚖️ MRB-225 holds. The stretch layer's *"a student who concludes there is no
    sugar in sugar has followed the method correctly and reasoned wrongly"* is
    method criticism, and it lives in GOING FURTHER. Nothing in the lesson body
    is retracted by it — the body already says a negative is a fact about the
    test, and the layer gives that a named mechanism.
  * The hook's answer is *"Nothing about the milk at all"* and the bench's
    milk/Benedict's note says the same result is a positive if heated long
    enough. The two agree; the hook is the under-heated tube.
"""

# ── the four tests (page lines 341–358) ─────────────────────────────────
#
# ⚠️ `detects` and `detects_full` are BOTH authored. Design writes
# `test.detects.split(' (')[0]` wherever the short form is wanted, which is a
# string transformation applied to authored science in the browser; two fields
# is one more line and no transformation anywhere.
#
# ⚠️ `headline` is authored rather than composed from `name`. Design writes
# `name.charAt(0).toUpperCase() + name.slice(1)`, which capitalises a reagent
# colour at runtime. Eight finished sentences cost eight lines and are exactly
# what a student reads.
TESTS = [
    {"id": "iodine", "label": "Iodine",
     "detects": "starch", "detects_full": "starch",
     "method": "A few drops of iodine solution straight onto the food. No "
               "heating.",
     "neg": {"colour": "#B4762A", "name": "orange-brown — unchanged",
             "headline": "Orange-brown — unchanged — not detected."},
     "pos": {"colour": "#1B1B3A", "name": "blue-black",
             "headline": "Blue-black — starch detected."}},
    {"id": "benedict", "label": "Benedict's",
     "detects": "reducing sugar",
     "detects_full": "reducing sugar (glucose, fructose)",
     "method": "Equal volumes of food solution and Benedict’s, then five "
               "minutes in a water bath at 80 °C.",
     "neg": {"colour": "#2E63B8", "name": "blue — unchanged",
             "headline": "Blue — unchanged — not detected."},
     "pos": {"colour": "#B03A16", "name": "brick red",
             "headline": "Brick red — reducing sugar detected."}},
    {"id": "emulsion", "label": "Ethanol emulsion",
     "detects": "lipid", "detects_full": "lipid (fat and oil)",
     "method": "Shake the food with ethanol, let it settle, then pour the "
               "ethanol into water.",
     "neg": {"colour": "#E8E2D2", "name": "clear — unchanged",
             "headline": "Clear — unchanged — not detected."},
     "pos": {"colour": "#FBFBF6", "name": "cloudy white",
             "headline": "Cloudy white — lipid detected."}},
    {"id": "biuret", "label": "Biuret",
     "detects": "protein", "detects_full": "protein",
     "method": "Equal volumes of food solution and Biuret solution, shaken. "
               "No heating.",
     "neg": {"colour": "#3E7ACB", "name": "blue — unchanged",
             "headline": "Blue — unchanged — not detected."},
     "pos": {"colour": "#7B4CA8", "name": "lilac purple",
             "headline": "Lilac purple — protein detected."}},
]

# ── the five foods and their twenty notes (page lines 360–401) ──────────
#
# ⚠️ `lower` is authored beside `label`. Design writes `food.label.toLowerCase()`
# in three places; the day a food is called "Marmite" or "Weetabix" that becomes
# wrong, and it is a transformation of authored text either way.
FOODS = [
    {"id": "potato", "label": "Potato", "lower": "potato",
     "has": {"iodine": True, "benedict": False, "emulsion": False,
             "biuret": False},
     "notes": {
         "iodine": "Potato is mostly starch, and starch is what iodine is "
                   "for. A strong blue-black comes up within seconds.",
         "benedict": "Raw potato stores its carbohydrate as starch, not as "
                     "free glucose, so there is very little reducing sugar to "
                     "find. Leave a potato in a warm cupboard for a fortnight "
                     "and this test starts to go positive — the starch is "
                     "being broken down.",
         "emulsion": "Potato has almost no lipid. Under a hundredth of its "
                     "mass.",
         "biuret": "A potato is about 2% protein — present, but too dilute "
                   "for the school test to show. This is a false negative, "
                   "and it is the most common one in the lesson."}},
    {"id": "milk", "label": "Milk", "lower": "milk",
     "has": {"iodine": False, "benedict": True, "emulsion": True,
             "biuret": True},
     "notes": {
         "iodine": "No starch in milk. This is a true negative — there really "
                   "is none.",
         "benedict": "Lactose, the sugar in milk, is a reducing sugar. Brick "
                     "red if you heat it long enough; green or orange if you "
                     "rush it.",
         "emulsion": "Whole milk is a suspension of fat droplets in water. "
                     "Strong cloudiness.",
         "biuret": "Milk is rich in casein and whey proteins. Clear lilac."}},
    {"id": "eggwhite", "label": "Egg white", "lower": "egg white",
     "has": {"iodine": False, "benedict": False, "emulsion": False,
             "biuret": True},
     "notes": {
         "iodine": "None. Egg white has essentially no carbohydrate.",
         "benedict": "Negative, and truly so — egg white is about 90% water "
                     "and 10% protein, with no sugar to speak of.",
         "emulsion": "The lipid in an egg is all in the yolk. Separate them "
                     "and the white gives a clean negative.",
         "biuret": "The clearest positive in the lesson. Egg white is almost "
                   "pure protein in water."}},
    {"id": "applejuice", "label": "Apple juice", "lower": "apple juice",
     "has": {"iodine": False, "benedict": True, "emulsion": False,
             "biuret": False},
     "notes": {
         "iodine": "No starch — in a ripe apple it has all been converted to "
                   "sugar. An unripe apple would test positive, which is a "
                   "nice reminder that a food is not a fixed thing.",
         "benedict": "Fructose and glucose, both reducing sugars. Rapid brick "
                     "red.",
         "emulsion": "Nothing. Fruit juice is sugar and water.",
         "biuret": "Under 0.3% protein. Negative on the school test, and not "
                   "quite zero in the fruit."}},
    {"id": "oliveoil", "label": "Olive oil", "lower": "olive oil",
     "has": {"iodine": False, "benedict": False, "emulsion": True,
             "biuret": False},
     "notes": {
         "iodine": "No starch.",
         "benedict": "No sugar. Note that a negative here tells you nothing "
                     "about the energy in the tube — olive oil carries more "
                     "energy per gram than anything else on the bench.",
         "emulsion": "Textbook positive: a dense white cloud the moment the "
                     "ethanol hits the water.",
         "biuret": "No protein."}},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 79 character for character.
    "slug":        "food-tests",
    "title":       "Food tests",
    "discipline":  "biology",
    "unit":        "nutrition-and-digestion",
    "family":      "INVESTIGATION",

    # ── curriculum position ─────────────────────────────────────────────────
    # A Working Scientifically statement, per §5.7.1 — see the docstring.
    "covers":      ["KS3.WS.ANA.03"],
    "touches":     ["KS3.B.NUT.01"],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 1},
                    {"id": "cells-and-systems", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    "requires":    ["a-balanced-diet"],
    "assumes":     [],
    "references":  ["enzymes-in-digestion",
                    {"unit": "C1", "lesson": "testing-the-model",
                     "label": "Testing the model",
                     "why": "Where the same question — what a result actually "
                            "licenses you to claim — is asked of a model "
                            "rather than of a tube."}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Required practical: qualitative food tests, plus "
                   "quantitative comparison against known standards.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Four tests, four colour changes. Each one answers exactly "
                    "one question — and three questions you will want to ask, "
                    "none of them can answer.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-limits` is the third: no control
    # of its own, so it mirrors `s-bench` and ticks on the bench's predicate —
    # see the docstring. `short` and `label` are Design's own strings (page
    # lines 333–339).
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "Two tubes",
         "done_when": "committed"},
        # Design's own threshold, kept: FOUR combinations, not one. A stop that
        # ticked on the first prediction would call a bench of twenty finished
        # after a twentieth of it.
        {"anchor": "s-bench",  "short": "BENCH",  "label": "Run the tests",
         "done_when": "four_combinations_run"},
        {"anchor": "s-limits", "short": "LIMITS", "label": "What it is worth",
         "mirrors": "s-bench", "done_when": "four_combinations_run"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3).
    "phenomenon": {
        "kind": "narrative",
        "title": "Two tubes of milk. One goes brick red, one stays blue.",
        "prompt": "Same bottle of milk, same Benedict's solution, same water "
                  "bath. Tube 1 comes out brick red. Tube 2 comes out blue. "
                  "Nobody made a mistake — the difference is that tube 1 was "
                  "heated for five minutes and tube 2 for thirty seconds.",
        "commit": "What can you conclude from tube 2 on its own?",
        "options": [
            "That milk contains no sugar",
            "That milk contains less sugar than tube 1 suggested",
            "Nothing about the milk at all",
            "That the Benedict’s solution had gone off",
        ],
        "reveal": "Nothing. A blue tube means <em>this test did not detect "
                  "sugar here</em> — which is not the same claim as <em>there "
                  "is no sugar in milk</em>. Every negative result in this "
                  "lesson is a statement about the test, not about the food.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ The `DIET` family is NOT in `docs/ks3/misconception-register.md`; see
    # the note in `lesson_01_a_balanced_diet.py`, which carries the full
    # allocation argument. 04 and 05 are this lesson's share.
    "misconceptions": [
        {"id": "DIET-04",
         "statement": "The deeper the colour, the more of the nutrient there "
                      "was.",
         # The bench elicits it: a student running milk with Benedict's reads a
         # note that says the same tube is red or orange depending on how long
         # it was heated, before the block below names the belief.
         "elicited_by": "twenty-combinations",
         "confronted_by": "think-colour"},
        {"id": "DIET-05",
         "statement": "A negative result proves the nutrient is not there.",
         "elicited_by": "twenty-combinations",
         "confronted_by": "think-colour"},
    ],

    # Design draws no keyword block anywhere in B3, so these never reach the
    # lesson body. The TERMS reach a student as the unit page's chips, and the
    # reading-age gate reads them as its exclusion list — which matters here,
    # because "qualitative", "Benedict's" and "emulsion" would otherwise all
    # count against the page.
    "vocabulary": [
        {"term": "food test",
         "definition": "A reagent that changes colour when one particular "
                       "nutrient is present.",
         "note": "One test answers one question and no others."},
        {"term": "qualitative",
         "definition": "Answering ‘present or not detected’, and never ‘how "
                       "much’.",
         "note": None},
        {"term": "reducing sugar",
         "definition": "A sugar that can give an electron to copper, which is "
                       "what Benedict’s solution detects.",
         "note": "Glucose and fructose can; ordinary table sugar cannot."},
        {"term": "emulsion",
         "definition": "A cloudy mixture of tiny droplets of one liquid "
                       "suspended in another.",
         "note": None},
        {"term": "false negative",
         "definition": "A test that shows nothing even though the substance "
                       "is really there, usually because there is too little "
                       "of it to detect.",
         "note": None},
    ],

    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b3/__init__.py::_normalise. Design's block is
        # `ks3-block ks3-dark ks3-practical` (page line 105), so `practical` is
        # measured and not inherited from the flagship next door.
        {"type": "test-bench", "id": "twenty-combinations", "anchor": "s-bench",
         "demand": "investigate",
         "eyebrow": "At the bench · five foods, four tests",
         "heading": "Predict, then run it",
         "head_counter": {"format": "{n} of 20 combinations run", "total": 20,
                          "start": 0},
         "prompt": "Pick a food, pick a test, say what you expect, then run "
                   "it. The tube shows what you would actually see.",

         "groups": {"food": "Food", "test": "Test"},
         "tests": TESTS,
         "foods": FOODS,

         "tube": {"caption": "In the tube", "label_join": " + ",
                  "not_run": "not run yet"},
         "method_label": "Method",
         "detects_label": "Detects: {detects}",

         # ⚖️ PREDICTING RUNS IT. There is no `run` control on Design's page
         # and there is none here: the commitment is the action.
         "predict": {
             "prompt": "Before you run it — will {test} detect {detects} in "
                       "{food_lower}?",
             "options": [
                 "Yes — it will change colour",
                 "No — it will stay as it started",
             ]},
         "verdicts": {"hit": "You predicted this",
                      "miss": "Not what you predicted"},

         # ⚖️ THE CLAIM LINE IS THE LESSON. Two templates, twenty finished
         # sentences, all composed at BUILD time and emitted into the document
         # — see `r_test_bench`. The negative is deliberately the hedged
         # wording and the quotation marks are Design's own U+201C/U+201D.
         "claim_label": "What you may write down:",
         "claims": {
             "positive": "“{food} contains {detects}.” Nothing about how "
                         "much.",
             "negative": "“No {detects} was detected in {food_lower} under "
                         "these conditions.” Not “there is none”.",
         },
         "rail_after": 4},

        # #s-limits — the band panel. Rail stop 3, mirroring `s-bench`; see
        # the docstring. `rule` is the component: band ground, 3px ink border, an accent-text
        # eyebrow and a display statement, then a card grid on the option
        # border — Design's markup (page lines 178–191) minus the repeated tag.
        {"type": "rule", "anchor": "s-limits",
         "eyebrow": "What a colour change is worth",
         "statement": "Three questions these tests cannot answer.",
         "cards": [
             {"term": "How much is there?",
              "gloss": "The test is qualitative. Colour intensity also "
                       "changes with heating time, volume and concentration, "
                       "none of which you controlled — so a deeper colour is "
                       "not evidence of more nutrient."},
             {"term": "Is there really none?",
              "gloss": "A negative means below what this test can detect, "
                       "with this sample, prepared this way. Potato does "
                       "contain protein; Biuret cannot see it at 2%."},
             {"term": "Is this food healthy?",
              "gloss": "Nothing in a colour change is about health. Olive oil "
                       "is one positive out of four and is a required "
                       "nutrient; a glucose solution is one positive and is "
                       "nothing but fuel."},
         ]},

        # Design nests this inside `#s-limits`; `r_rule` has no nested slot, so
        # it renders directly under the panel in document order. See "What
        # could not be lifted" 2.
        {"type": "key-fact", "ref": "qualitative-never-quantity"},

        {"type": "misconception", "id": "think-colour",
         "anchor": "s-think", "targets": "DIET-04"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "qualitative-never-quantity",
         "text": "A food test is qualitative: it says present or not "
                 "detected. It never says how much, and “not detected” is a "
                 "fact about your test, not about the food.",
         "placement": "top-level",
         "ground": "band",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, separated by an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`, and an authored statement wins over the register.
        # The block asks for no commitment, on Design's page and here, so it is
        # not a rail stop and emits no completion contract.
        {"id": "think-colour",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "DIET-04",
         "statements": [
             {"quote": "The redder the Benedict's went, the more sugar there "
                       "was.",
              "body": ["Tempting, and almost useful, but not something you "
                       "may claim from a school test. The colour does move "
                       "through green, yellow and orange to brick red as more "
                       "sugar is present — but it also moves that way if you "
                       "heat it for longer, use more Benedict's, or start "
                       "with a warmer bath. In your experiment those things "
                       "were not controlled, so a redder tube is not evidence "
                       "of more sugar; it is evidence that something was "
                       "different, and you cannot say what. To make the "
                       "colour mean an amount you would have to fix the "
                       "volume, the concentration of Benedict's, the "
                       "temperature and the time, and compare against tubes "
                       "of known sugar concentration. That is a different "
                       "experiment, and it is the one a laboratory actually "
                       "runs."]},
             {"quote": "The iodine stayed orange, so there is no starch in "
                       "it.",
              "body": ["Write the two sentences next to each other and the "
                       "gap is obvious. <em>The test did not detect starch</em> "
                       "is what you observed. <em>There is no starch</em> is a "
                       "claim about the food. Between them sit at least four "
                       "ways the first can be true while the second is false: "
                       "too little starch to see, iodine too dilute, the "
                       "sample not crushed so the iodine never reached the "
                       "inside, or the starch already broken down to sugar — "
                       "which is exactly what happens if you chew bread for "
                       "two minutes before testing it. Negative results are "
                       "the ones that need the most care, because a negative "
                       "feels like nothing happened, and nothing happening is "
                       "very easy to achieve by accident."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⚖️ MRB-177 LENGTH PARITY — MEASURED, AND BOTH MARKED RUNGS PASS.
    #   rung 1: correct 4w against distractors of 6 / 7 / 4 — the correct
    #           option is the SHORTEST, so it cannot be a length tell.
    #   rung 2: correct 7w against distractors of 8 / 14 / 6 — likewise.
    # No distractor was rewritten, because there was nothing to repair.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Read the result",
            # ⚖️ MRB-297, 30 Aug 2026 — a BIOLOGY change made under a
            # PHYSICS ruling. Mide ruled the peanut out of P2's burning-food
            # practical, and the ruling sweeps the estate: this is a
            # different practical, but it is still a nut a child handles.
            # Double cream replaces it — the standard school positive for
            # the ethanol emulsion test, an unmistakable dense white
            # cloud, and a food students actually test. It is a liquid, so
            # "crushes" goes; nothing else about the rung moves. The
            # correct option is still index 2 for the same reason, the
            # options are in the same order, and every option keeps its
            # word count, so the length-parity note above still holds.
            "q": "A student shakes double cream with ethanol, pours the "
                 "ethanol into water and gets a thick white cloud. What "
                 "may they write down?",
            "options": [
                "The cream is high in fat",
                "The cream contains lipid and no protein",
                "The cream contains lipid",
                "The cream is unhealthy",
            ],
            "answer": 2,
            "feedback": {
                0: "Almost right, and ‘high’ is the word that fails. The "
                   "emulsion test detects lipid; it does not measure how much, "
                   "so ‘high’ is not supported by this result.",
                1: "This test says nothing at all about protein. One test "
                   "answers one question — you would need Biuret to make any "
                   "claim about protein.",
                3: "No food test is a judgement about health. Lipid is one of "
                   "the seven required nutrients.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Bread gives a strong blue-black with iodine. A student chews "
                 "a piece for two minutes, spits it out, tests it again, and "
                 "now gets orange-brown and a positive Benedict’s. What "
                 "happened?",
            "options": [
                "The iodine was too dilute the second time",
                "Chewing squashed the starch into smaller pieces so the "
                "iodine could not find it",
                "Saliva broke the starch down into sugar",
                "The starch dissolved in the saliva",
            ],
            "answer": 2,
            "feedback": {
                0: "Same iodine, same drops. Something changed in the bread, "
                   "not in the reagent — and the Benedict’s result tells you "
                   "what.",
                1: "Crushing a sample makes a test more likely to work, not "
                   "less. And crushing cannot create the reducing sugar that "
                   "Benedict’s just found.",
                3: "Dissolving starch does not stop iodine detecting it — the "
                   "standard method uses starch solution. The starch is not "
                   "dissolved, it is gone: converted to something else.",
            }},
        "explain": {
            "title": "Rung 3 · Write the honest conclusion",
            "q": "A group tests potato with Biuret and gets no colour change. "
                 "They conclude “potato contains no protein”. Potato is in "
                 "fact about 2% protein. Explain what is wrong with their "
                 "conclusion, write a version you could defend, and say what "
                 "you would change to detect the protein.",
            "field_label": "Your answer",
            "placeholder": "Their conclusion goes further than the evidence "
                           "because…",
            "success": [
                "Says the observation only supports ‘protein not detected’, "
                "not ‘no protein present’.",
                "Gives the reason: the concentration is below what the test "
                "can detect.",
                "Writes a defensible conclusion using wording such as ‘no "
                "protein was detected under these conditions’.",
                "Suggests a workable change — more concentrated sample, larger "
                "mass of potato in less water, or a more sensitive method.",
                "Does not claim the test was done wrongly; the method was "
                "followed correctly and still gave a false negative.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A company claims its cereal bar is “protein-packed and "
                 "sugar-free”. You have iodine, Benedict’s, ethanol and "
                 "Biuret. Say which tests you would run, what result would "
                 "support each claim, and which of the two claims you could "
                 "never fully check with this equipment.",
            "field_label": "Your answer",
            "placeholder": "I would run… because…",
            "success": [
                "Picks Biuret for the protein claim and Benedict’s for the "
                "sugar claim.",
                "States that a lilac Biuret result supports protein being "
                "present but not ‘packed’, because the test gives no amount.",
                "Identifies ‘protein-packed’ as the claim that cannot be "
                "checked, since it is a quantity claim and these tests are "
                "qualitative.",
                "Notes that a blue Benedict’s does not prove sugar-free either "
                "— sucrose is not a reducing sugar and would not show up.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Iodine turns blue-black with starch. Benedict's solution "
                "turns from blue to brick red with reducing sugar, on heating. "
                "Ethanol then water turns cloudy white with lipid. Biuret "
                "solution turns from blue to lilac with protein. Each result "
                "is positive or not detected — never an amount.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # MRB-225: method criticism lives HERE. Nothing in the body is retracted —
    # the body already says a negative is a fact about the test; this names the
    # mechanism behind the sharpest case of it.
    "stretch": [
        {"type": "explainer", "id": "sugar-that-is-not-a-reducing-sugar",
         "text": "Benedict's test does not detect all sugars. It needs a sugar "
                 "that can hand an electron to copper — a reducing sugar — "
                 "which glucose and fructose can do and sucrose, ordinary "
                 "table sugar, cannot. So a spoonful of caster sugar in water "
                 "gives a blue tube and a perfectly negative result, and a "
                 "student who concludes there is no sugar in sugar has "
                 "followed the method correctly and reasoned wrongly. Boil the "
                 "same solution with a little acid first, splitting the "
                 "sucrose into glucose and fructose, and it goes brick red. "
                 "The test was never asking “is there sugar here” — it was "
                 "asking a narrower question that happens to be easy to "
                 "confuse with that one."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Unsure what a negative result lets you write down?",
              "cta": "Ask about this lesson",
              "anchor": "s-limits"},

    # ⚠️ `safety_note`, and on this lesson it genuinely is one — irritants, a
    # strong alkali, a water bath rather than a flame, and open ethanol near a
    # Bunsen. This is the treatment b3-01's and b3-03's figure caveats are
    # deliberately kept OUT of, so that it still means something here.
    "safety_note": "Benedict's and Biuret solutions are irritants and Biuret "
                   "contains sodium hydroxide — wear eye protection, use a "
                   "water bath rather than a naked flame, and never taste "
                   "anything on the bench. Ethanol is highly flammable: no "
                   "Bunsen alight while it is open.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
