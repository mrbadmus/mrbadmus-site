"""B3 L4 — When diet goes wrong (CONTRAST).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b3/b3-04-when-diet-goes-wrong.dc.html` (604 lines), and its
author's notes, `docs/ks3/design-reference/b3/NOTES-B3.md`. Every student-facing string is
lifted byte-identical from the approved page except where this docstring says
otherwise, and every exception is here.

── ⚠️ THE TONE OF THIS LESSON IS SCIENCE, NOT STYLE ─────────────────────

NOTES-B3 flag 9 says so in as many words, and asks that it be reviewed "with
the same weight as its statements". The lesson covers obesity, starvation and
deficiency as three MECHANISMS: it reasons from measurements and clinical
signs, sets no targets, names no ideal body, and the third confrontation
attacks "you can tell what someone eats by looking at them" head-on — Design
calls that "the most important sentence in the lesson" and the sentence is
lifted with the claim intact.

**Nothing in this module softens it, sharpens it, or adds a reassurance Design
did not write.** The clinical descriptions are Design's, the "risk raised, not
certainty" qualifier in imbalance 1 is Design's, "it is not a moral failure"
in clinic 3 is Design's, and the closing line pointing at a trusted adult, a
school nurse or a doctor is Design's. If any of it is to change, it changes on
Mide's ruling and not on an author's instinct.

── One correction to the verdict, and one reversal on the rail ──────────

1. **`#s-three` STAYS ON THE RAIL.** ⊕ **REVERSED 18 Aug 2026 (MRB-249).**
   This item used to say the opposite. Design's stage 2 ticks on
   `s.hookChoice !== null` — the HOOK's predicate, verbatim (page line 430) —
   and because the section is an eyebrow, a display line, a lede, three columns
   and a key fact, emitting no control, no commit and no field, the reading was
   that MRB-208's completion rule forbade the stop and
   `ks3_parity.check_rail_reachable` would name the defect. So the lesson
   shipped THREE stops, not four.

   That is overruled twice over. MRB-205 binds and is not re-argued — Design
   draws, we render, nothing invented and nothing dropped, page wins over
   engine — and dropping a stop Design drew is not rendering what Design drew.
   And the repeated predicate is Design stating the tick condition, not
   overlooking one: `isDone()` is a rail-level function returning the identical
   expression for `#s-hook` and then for `#s-three`, because the three failures
   ARE the reading-back of the hook's own choice. The section holds no control
   because the hook already took the commitment. That is a MIRROR, resolved at
   rail level in `wireRail`'s `paint()`.

   So the stop is declared: anchor `s-three`, `mirrors: "s-hook"`,
   `done_when: "committed"` — the hook's own predicate, named as borrowed
   rather than smuggled, and gated by `check_rail_matches_design` against
   `docs/ks3/rail-manifest.md`. c1-02's `#s-matrix` is restored the same way.
   The section keeps its anchor, as it always did.

2. **The clinic verdict stops marking the student (MRB-196 R10).** Design
   computes whether the ticks matched exactly and spends it on the verdict
   LABEL: "You had it exactly" / "Two imbalances apply here" / "Not quite".
   Two of those three branches are the page marking an activity, which R3
   forbids; R10 replaces them with a self-check the student answers for
   themselves. The third branch is not about the student at all — it is a fact
   about the CASE — so it survives as `verdict_label`, authored per clinic and
   shown to everyone identically.

   That also fixes a defect in Design's own branching, and it is the more
   serious half: a student who ticked BOTH answers on clinic 2 took the
   `exact` branch and therefore **never saw the line telling them two
   imbalances apply**. The page's own teaching sentence was shown only to the
   students who got it wrong.

── What could not be lifted byte-identical ─────────────────────────────

* **`#s-three`'s three columns are compressed.** Design draws each as a card
  carrying a tag, a name and a four-row definition list. The §5.1.1 block
  vocabulary is CLOSED; `comparison` takes exactly two columns and raises on
  three, and `rule` — whose shell matches Design's section value for value
  (`--ks3-band`, 3px ink, `--ks3-r-block`, 34px 32px, accent eyebrow) — carries
  a `term` and a `gloss` per card and nothing finer. So the tag and the name
  are joined by the system's own middot, and the four rows become one gloss
  with each row's label in `<strong>`. **Every authored byte is present, in
  Design's order**; what is lost is the definition-list structure. Reported —
  the section is a candidate for promotion to a drawn component of its own,
  exactly as `scale-cards` was ("a static three-up panel is its own
  component").

* **Design's lede moves below the columns.** `r_rule` emits `close` after its
  cards and has no slot between the statement and them. "Reading across the
  rows is the point of this lesson" reads as an instruction either way, and the
  bytes are unchanged.

* **`verdict_label` for the three single-answer clinics is new copy.**
  "One imbalance applies here" is the mechanical singular of Design's own "Two
  imbalances apply here", written because R10 removed the two branches that
  used to fill that slot for them. Three strings.

── Ladder length parity (MRB-177) ───────────────────────────────────────

Measured on both marked rungs, and **both PASS unfixed**:

    rung 1   correct 4 words, longest distractor 9 — correct is not the
             longest, so there is no length tell to fix.
    rung 2   correct 12 words, longest distractor 10. Strictly longest, but
             +2 words and ×1.20 — inside both thresholds (≥4 words or ≥1.4×).

No distractor was touched. A correct option that is not a length tell must not
be "fixed"; c1-02's rewrite was needed because its correct answer ran double
the longest distractor.

⚑ For Mide's science gate — NOTES-B3's own flags, carried here so they are
  visible beside the content rather than only in a delivery note:
  * flag 9   the tone of the whole lesson (above).
  * flag 10  clinics 2 and 5 each have two answers, and clinic 5's cause is
             not dietary at all — an adequate plate and a shortened intestine.
             Design wants it inside a diet lesson as the bridge into lessons
             5–7. Confirm.
  * flag 11  James Lind's 1747 trial, including that he misread his own result
             and recommended a boiled concentrate that destroyed the vitamin C.
             It lives in GOING FURTHER, which is where MRB-225 puts evidence
             quality and history of science, and it retracts nothing above it.

⚑ `DIET-08` … `DIET-10` are PROVISIONAL ids. NOTES-B3 §5 says the family was
  minted as fifteen entries in `docs/ks3/misconception-register.md`, and **the
  register contains no `DIET` family row at all** — the rows were never
  written. Nothing machine-reads the register, so the build is unaffected, but
  the numbering across all eight B3 lessons has to be reconciled in one pass.
  The two anchors NOTES supplies are honoured here: `DIET-13`/`DIET-14` are the
  enzyme pair (b3-06), and `DIET-10` is the one NOTES flag 9 attaches its ⚠ to,
  which is this lesson's body-image confrontation.
"""

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 106 character for character.
    "slug":        "when-diet-goes-wrong",
    "title":       "When diet goes wrong",
    "discipline":  "biology",
    "unit":        "nutrition-and-digestion",
    "family":      "CONTRAST",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.NUT.03` whole, not a clause: "the consequences of imbalances in
    # the diet, including obesity, starvation and deficiency diseases" is one
    # idea taught as one lesson, and the three imbalances are its three
    # columns. Nothing to split.
    "covers":      ["KS3.B.NUT.03"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2},
                    {"id": "energy", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 40,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's endmatter: "Before this lesson → Energy in food and what you
    # need"; "Connects to → A balanced diet, Bacteria in the gut"; "At GCSE
    # this becomes" is PROSE, so `ks4_links` is empty and `ks4_becomes` carries
    # the sentence (§4.8.1 D renders it only when there is no KS4 page).
    "requires":    ["energy-in-food-and-what-you-need"],
    "assumes":     [],
    "references":  ["a-balanced-diet", "bacteria-in-the-gut"],
    "ks4_links":   [],
    "ks4_becomes": "Risk factors for non-communicable disease, and the "
                   "evidence linking diet to cardiovascular disease and type 2 "
                   "diabetes.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Three different things can be wrong with a diet, and they "
                    "are not three degrees of the same thing. Two of them can "
                    "happen at once, in the same person, on a full plate.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-three` is the second: no control of
    # its own, so it mirrors `s-hook` and ticks on the hook's predicate — see
    # the docstring. `short` is Design's own RAIL_SHORT entry and `label` its
    # own RAIL label, both lifted (page lines 318–323).
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "Full plate",
         "done_when": "committed"},
        {"anchor": "s-three", "short": "THREE", "label": "Three failures",
         "mirrors": "s-hook", "done_when": "committed"},
        {"anchor": "s-cases",  "short": "CLINIC", "label": "Five clinics",
         "done_when": "all_five_diagnosed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    "phenomenon": {
        "kind": "narrative",
        "title": "A patient is eating 13 000 kJ a day and is severely "
                 "malnourished.",
        "prompt": "Not going short of food. Not skipping meals. Taking in more "
                  "energy than an adult needs, every day, and a doctor has "
                  "diagnosed malnutrition. The diagnosis is correct and the "
                  "intake figure is correct.",
        "commit": "How can both be true at once?",
        "options": [
            "The intake figure must have been measured wrongly",
            "Malnutrition is about balance, not quantity",
            "Their body is failing to digest any of the food",
            "13 000 kJ is not actually very much",
        ],
        "reveal": "Malnutrition means the balance is wrong, not that the "
                  "quantity is small. Seven nutrients have to arrive; energy "
                  "is only what three of them carry. A diet can be generous in "
                  "kilojoules and missing iron, or vitamin D, or fibre "
                  "entirely — and the body fails at the missing thing "
                  "regardless of how much of everything else showed up.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Three, in the document order Design draws them. See the docstring on the
    # provisional ids. Each `statement` is Design's own `.ks3-mis-quote`
    # without its quote marks — `_quoted()` adds them.
    "misconceptions": [
        {"id": "DIET-08",
         "statement": "Malnourished means not having enough to eat.",
         "elicited_by": "three-wrong-ideas",
         "confronted_by": "three-wrong-ideas"},
        {"id": "DIET-09",
         "statement": "Deficiency diseases are all in the past.",
         "elicited_by": "three-wrong-ideas",
         "confronted_by": "three-wrong-ideas"},
        # ⚠️ The one NOTES-B3 flag 9 attaches its ⚠ to. It is the lesson's
        # tone question in one sentence, and it is confronted rather than
        # softened.
        {"id": "DIET-10",
         "statement": "You can tell what someone eats by looking at them.",
         "elicited_by": "three-wrong-ideas",
         "confronted_by": "three-wrong-ideas"},
    ],

    # Design draws no keyword block on this page, so these never reach the
    # lesson body. They DO reach a student, as the unit page's "Words this unit
    # gives you" chips, and the reading-age gate reads them as its exclusion
    # list. Worded so nothing in the lesson contradicts them.
    "vocabulary": [
        {"term": "malnutrition",
         "definition": "A diet whose balance is wrong — too much energy, too "
                       "little energy, or a nutrient missing.",
         "note": "It does not mean going short of food. That is one of the "
                 "three things it can mean."},
        {"term": "obesity",
         "definition": "A long-term energy surplus stored as so much lipid "
                       "that health risks rise.",
         "note": None},
        {"term": "deficiency disease",
         "definition": "An illness caused by one nutrient being absent or too "
                       "low in the diet.",
         "note": "Scurvy, rickets and anaemia are three. Each has one missing "
                 "nutrient behind it."},
        {"term": "adipose tissue",
         "definition": "The body tissue that stores lipid.",
         "note": None},
    ],

    # Nothing on this page references a figure, and the three imbalances are
    # argued in words and in five clinical cases rather than drawn. Present and
    # empty, never absent.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-three — Design's classless band section, which IS the `rule`
        # shell: `--ks3-band`, 3px ink, `--ks3-r-block`, 34px 32px padding,
        # 28px top margin and an accent-text eyebrow, matching `.ks3-rule`
        # declaration for declaration. Rail stop 2, mirroring `s-hook`; see
        # the docstring.
        {"type": "rule", "anchor": "s-three",
         "eyebrow": "Three separate failures",
         "statement": "Not one problem with a dial on it.",
         # ⚠️ COMPRESSED. Design draws a tag, a name and a four-row definition
         # list per column; `rule` carries a term and a gloss. The tag and the
         # name are joined by the system's own middot and the four rows become
         # one gloss with each row's label in <strong>. Every byte is present,
         # in Design's order. See the docstring.
         "cards": [
             {"term": "Imbalance 1 · Long-term energy surplus",
              "gloss": "<strong>What is wrong</strong> Energy taken in is "
                       "greater than energy transferred, day after day, for "
                       "months or years. "
                       "<strong>What the body does</strong> The surplus is "
                       "stored as lipid in adipose tissue. Storage is a "
                       "normal, healthy mechanism; the problem is only the "
                       "size of the store when it keeps growing. "
                       "<strong>What follows</strong> Obesity raises the risk "
                       "of type 2 diabetes, high blood pressure, heart disease "
                       "and joint damage. Risk raised, not certainty — these "
                       "are probabilities, not verdicts. "
                       "<strong>What changes it</strong> Any lasting change to "
                       "the balance between intake and activity. Slow, because "
                       "the store took a long time to build."},
             {"term": "Imbalance 2 · Long-term energy shortfall",
              "gloss": "<strong>What is wrong</strong> Energy taken in is less "
                       "than energy transferred, for weeks or months. Causes "
                       "range from food being unavailable to illness that "
                       "prevents eating or absorbing. "
                       "<strong>What the body does</strong> Lipid stores are "
                       "broken down first. When those are gone it breaks down "
                       "its own protein — muscle, including heart muscle. "
                       "<strong>What follows</strong> Growth stops, the immune "
                       "system weakens, and body temperature is hard to "
                       "maintain. In children the effect on growth may not be "
                       "recoverable. "
                       "<strong>What changes it</strong> Refeeding, done "
                       "carefully and medically — restarting food too fast "
                       "after prolonged starvation is itself dangerous."},
             {"term": "Imbalance 3 · A specific nutrient missing",
              "gloss": "<strong>What is wrong</strong> One nutrient is absent "
                       "or too low. Energy intake can be high, normal or low — "
                       "it is a separate question. "
                       "<strong>What the body does</strong> Whatever that "
                       "nutrient was needed for stops working properly. "
                       "Nothing else can substitute: no amount of "
                       "carbohydrate replaces 14 mg of iron. "
                       "<strong>What follows</strong> A named deficiency "
                       "disease. No vitamin C, scurvy. No vitamin D, rickets. "
                       "No iron, anaemia. Each has its own signs. "
                       "<strong>What changes it</strong> Supplying that one "
                       "nutrient. Often a fast and complete recovery, which is "
                       "what makes deficiency diseases so striking to treat."},
         ],
         # Design's lede, which sits between the statement and the columns on
         # the page and which `r_rule` can only place after them. Unchanged.
         "close": "Each of the three has a different cause, a different "
                  "mechanism inside the body, and a different remedy. "
                  "Compare them line by line."},

        # Design nests the key fact INSIDE the band section; `r_rule` has no
        # slot for it, so it renders as the next block on the `card` ground —
        # the same treatment, immediately below. c1-02's precedent exactly.
        {"type": "key-fact", "ref": "three-imbalances"},

        # #s-cases — the flagship, on `ks3-block ks3-dark ks3-practical`.
        # Authored inline; `ks3_data/b3/__init__.py::_normalise` lifts it into
        # `activities[]` and leaves a `practical` shell behind it.
        {"type": "clinic-cases", "id": "five-clinics", "anchor": "s-cases",
         "demand": "investigate",
         "eyebrow": "Your turn · five clinics",
         "heading": "Which imbalance is this?",
         # Opens at ZERO: nothing has been diagnosed until a student presses
         # the button, and nothing is ticked on load (MRB-208).
         "head_counter": {"format": "{n} of 5 diagnosed", "total": 5,
                          "start": 0},
         "prompt": "Each description gives you a diet and a set of signs. Say "
                   "which of the three imbalances fits. Two of the five have "
                   "more than one answer, and being unwilling to pick two is "
                   "itself a mistake.",

         # The three things a clinic can be. A MULTI-select — this is the one
         # control in the key stage where more than one may be pressed.
         "kinds": [
             {"id": "surplus",   "label": "Energy surplus"},
             {"id": "shortfall", "label": "Energy shortfall"},
             {"id": "missing",   "label": "A nutrient missing"},
         ],
         "pick_label": "Tick every imbalance that applies",
         "reveal_label": "Show the diagnosis",
         "count_labels": {"none": "nothing ticked yet",
                          "some": "{n} ticked",
                          "done": "Diagnosed"},

         # ⚠️ `verdict_label` IS A FACT ABOUT THE CASE, never about the
         # student. Design's plural is lifted; the singular is new copy, and
         # the docstring says why there was nothing to lift.
         "cases": [
             {"id": "k1", "label": "Clinic 1", "tab_label": "Clinic 1",
              "description": "An adult reports tiredness, breathlessness on "
                             "stairs and pale skin. Blood tests show low "
                             "haemoglobin. Their diet is bread, pasta, cheese "
                             "and fruit, with no meat, fish or leafy "
                             "vegetables. They are not losing mass.",
              "intake": "Intake about 10 000 kJ / day — close to requirement",
              "kinds": ["missing"],
              "verdict_label": "One imbalance applies here",
              "answer": "Iron-deficiency anaemia. A nutrient missing, and "
                        "nothing else.",
              "why": "Energy intake is fine, mass is stable, and the signs all "
                     "point at haemoglobin. Iron is needed in milligrams and "
                     "this diet supplies almost none. Adding more of the same "
                     "food would change nothing."},
             {"id": "k2", "label": "Clinic 2", "tab_label": "Clinic 2",
              "description": "A 14-year-old has stopped growing in height over "
                             "eighteen months, feels cold constantly, and "
                             "bruises easily. Their family has been unable to "
                             "afford regular meals.",
              "intake": "Intake about 4500 kJ / day — far below requirement",
              "kinds": ["shortfall", "missing"],
              "verdict_label": "Two imbalances apply here",
              "answer": "Energy shortfall, and almost certainly deficiencies "
                        "alongside it.",
              "why": "Both apply, and this is the pair most students refuse to "
                     "tick together. Too little food means too little of "
                     "everything in it — so a prolonged shortfall drags "
                     "specific deficiencies along behind it. The growth arrest "
                     "is the shortfall; the bruising suggests vitamin C or K "
                     "as well."},
             {"id": "k3", "label": "Clinic 3", "tab_label": "Clinic 3",
              "description": "An adult has gained mass steadily over ten "
                             "years. Blood glucose is raised and a doctor has "
                             "diagnosed type 2 diabetes. They eat large "
                             "portions, mostly processed food, and have a desk "
                             "job and a car commute.",
              "intake": "Intake about 14 000 kJ / day — well above requirement",
              "kinds": ["surplus"],
              "verdict_label": "One imbalance applies here",
              "answer": "Long-term energy surplus.",
              "why": "Ten years of intake above requirement, stored as lipid, "
                     "and one of the risks that follow has now appeared. Note "
                     "what this case is not: it is not a moral failure, and "
                     "the fix is a change in the long-term balance, not a "
                     "punishment."},
             {"id": "k4", "label": "Clinic 4", "tab_label": "Clinic 4",
              "description": "A toddler in a smoky northern city in 1900 has "
                             "soft, bowed leg bones and a delayed walk. They "
                             "are fed bread, potatoes, tea and a little meat. "
                             "They are not thin.",
              "intake": "Intake roughly at requirement",
              "kinds": ["missing"],
              "verdict_label": "One imbalance applies here",
              "answer": "Rickets — vitamin D missing.",
              "why": "Enough food, enough energy, no vitamin D. It comes from "
                     "oily fish or from sunlight on skin, and a smoke-darkened "
                     "street supplies neither. Calcium cannot be absorbed "
                     "properly without it, so the bones stay soft. This is the "
                     "classic case of a deficiency in a fed child."},
             {"id": "k5", "label": "Clinic 5", "tab_label": "Clinic 5",
              "description": "An adult recovering from major surgery cannot "
                             "absorb nutrients properly from their shortened "
                             "intestine. They eat willingly and in normal "
                             "quantities but are losing mass and have low "
                             "levels of several vitamins.",
              "intake": "Intake about 9500 kJ / day — at requirement",
              "kinds": ["shortfall", "missing"],
              "verdict_label": "Two imbalances apply here",
              "answer": "Both — and the cause is not the diet at all.",
              "why": "The plate is fine. What has failed is absorption, so "
                     "what reaches the blood is a shortfall even though what "
                     "reaches the mouth is not. This is the case that shows "
                     "why ‘diet’ and ‘nutrition’ are not the same word: the "
                     "next three lessons are about the part of the system that "
                     "has broken here."},
         ],

         # ⊕ MRB-196 R10. NOT Design's; this is the ruling's own component and
         # it is what replaces the two verdict branches that used to grade the
         # student. There is no `answer` key and there must never be one — only
         # the student knows how many of their own ticks matched, and a right
         # answer here would mark an activity option, which R3 forbids. It
         # renders only once all five diagnoses are showing, because before
         # that there is nothing to compare against.
         "self_check": {
             "question": "Now every diagnosis is showing — how many of your "
                         "five did you have?",
             "options": ["All five", "Three or four", "Two or fewer"],
             "note": "Nobody marks this but you. Clinics 2 and 5 each have two "
                     "answers, and those are the two worth reading again.",
         }},

        {"type": "misconception", "id": "three-wrong-ideas",
         "anchor": "s-think", "targets": "DIET-08"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # `ground: "card"` because Design draws it on `--ks3-card` with a 2px ink
    # outline and the accent offset shadow, sitting inside a `--ks3-band`
    # section — band on band would be invisible.
    "key_facts": [
        {"id": "three-imbalances",
         "text": "Too much energy, too little energy and a missing nutrient "
                 "are three different imbalances. A deficiency can occur at "
                 "any level of energy intake, because a specific nutrient "
                 "cannot be substituted by more of the others.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # One entry. The instrument is authored inline in `core` and lifted here by
    # `ks3_data/b3/__init__.py::_normalise`, which leaves the `practical` shell
    # behind it.
    "activities": [
        # Design draws THREE wrong ideas in one "Think again", the second and
        # third behind an amber-topped divider. `statements` carries all three
        # with their bodies, and `r_confrontation` draws the dividers.
        {"id": "three-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "DIET-08",
         "statements": [
             {"quote": "Malnourished means not having enough to eat.",
              "body": [
                  "The word means badly nourished, not under-nourished, and "
                  "the difference is not nit-picking — it changes what you "
                  "look for and what you do. Rickets was widespread in "
                  "industrial British cities among children who were fed "
                  "enough, because vitamin D needs either oily fish or "
                  "sunlight and a smoke-filled street supplies neither. "
                  "Iron deficiency is the most common nutritional disorder "
                  "in the world and it is not concentrated in places where "
                  "food is scarce. If you diagnose every dietary problem as "
                  "a shortage of food, you will treat these by handing over "
                  "more of the same food, and nothing will improve, because "
                  "the missing nutrient is still missing."]},
             {"quote": "Deficiency diseases are all in the past.",
              "body": [
                  "Scurvy still appears in hospitals. So does rickets, so does "
                  "severe iron deficiency, and vitamin B12 deficiency is "
                  "common enough that it is a routine blood test. The reason "
                  "is not that food is unavailable; it is that a nutrient "
                  "needed in milligrams can be absent from a diet that looks "
                  "entirely ordinary, and the early signs — tiredness, aching, "
                  "slow healing, low mood — are the least specific symptoms in "
                  "medicine. A deficiency is easy to miss precisely because it "
                  "does not announce itself as a food problem."]},
             # ⚠️ The tone-bearing one. Lifted exactly; the claim is not
             # hedged and no reassurance is added.
             {"quote": "You can tell what someone eats by looking at them.",
              "body": [
                  "You cannot, and this is the most important sentence in "
                  "the lesson. Body mass is affected by genetics, by "
                  "illness, by medication, by how much someone can move, by "
                  "sleep, by stress and by whether they can afford or reach "
                  "particular foods — as well as by what they eat. Two "
                  "people on the same diet can differ a lot, which is "
                  "exactly what the hook in the energy lesson showed. The "
                  "three imbalances in this lesson are described by "
                  "measurements and by clinical signs, not by appearance, "
                  "and a biologist reasons from the measurements."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # `title` carries Design's finished heading; `_rung_title` strips the
    # "Rung N · " prefix and the engine puts the number back.
    #
    # ⚖️ NO DISTRACTOR WAS TOUCHED ON EITHER MARKED RUNG. Both pass the
    # MRB-177 length-parity check as delivered — see the docstring for the
    # measurement. A correct option that is not the longest cannot be a length
    # tell, and rung 2's +2 words at ×1.20 is inside both thresholds.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Name the imbalance",
            "q": "A patient eats 12 000 kJ a day, is gaining mass slowly, and "
                 "has been diagnosed with scurvy. Which imbalance or "
                 "imbalances apply?",
            "options": [
                "A nutrient missing, only",
                "An energy shortfall",
                "A nutrient missing and an energy shortfall",
                "None — you cannot have scurvy while eating that much",
            ],
            "answer": 0,
            "feedback": {
                1: "They are gaining mass on 12 000 kJ a day. There is no "
                   "shortfall of energy here — scurvy is about vitamin C, "
                   "which carries no energy at all.",
                2: "The deficiency is right; the shortfall is not. Nothing in "
                   "the case suggests too little energy, and gaining mass "
                   "rules it out.",
                3: "You can, and people do. Vitamin C is needed in milligrams "
                   "and is absent from a great many otherwise generous diets.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Two children are the same age and height. Child A eats "
                 "6000 kJ a day; child B eats 11 000 kJ. Both have been "
                 "diagnosed with iron-deficiency anaemia. What does this tell "
                 "you?",
            "options": [
                "Child B must have been misdiagnosed",
                "Iron deficiency does not depend on how much energy a diet "
                "supplies",
                "Child A’s anaemia is more serious because they eat less",
                "Both children need to eat more food",
            ],
            "answer": 1,
            "feedback": {
                0: "There is no contradiction to resolve. A deficiency is a "
                   "statement about one nutrient, and it is independent of the "
                   "total energy intake.",
                2: "Severity depends on how low the iron is, which the case "
                   "does not tell you. The energy figures are not evidence "
                   "about the anaemia either way.",
                3: "This is the trap the lesson exists to set. More of a diet "
                   "that lacks iron delivers more of everything except iron.",
            }},
        "explain": {
            "title": "Rung 3 · Explain why more food does not fix it",
            "q": "A charity responds to a region with widespread anaemia by "
                 "shipping large quantities of white rice. Explain why this "
                 "will reduce hunger but not reduce the anaemia, and what "
                 "would need to be added.",
            "field_label": "Your explanation",
            "placeholder": "Rice will help with… but not with…",
            "success": [
                "Says rice supplies carbohydrate and so addresses an energy "
                "shortfall.",
                "Says rice supplies very little iron, so the specific "
                "deficiency is untouched.",
                "States the general principle: a missing nutrient cannot be "
                "substituted by more of the others.",
                "Names something that would supply iron — pulses, leafy "
                "greens, meat, or fortified flour.",
                "Recognises that both problems can be present at once and both "
                "need addressing.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "The UK adds calcium, iron and B vitamins to white flour by "
                 "law. Using the three imbalances, explain what problem this "
                 "policy targets, why it works at the flour rather than at the "
                 "person, and one limitation you would expect it to have.",
            "field_label": "Your answer",
            "placeholder": "Fortification targets…",
            "success": [
                "Identifies the target as specific nutrient deficiencies, not "
                "energy imbalance.",
                "Explains that flour is eaten by almost everyone, so "
                "fortifying it reaches people who would never seek treatment.",
                "Notes that it requires no change in behaviour, which is why "
                "it works where advice does not.",
                "Gives a real limitation — it misses people who avoid wheat, "
                "cannot be targeted to those who need it, and the dose cannot "
                "be adjusted per person.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "An imbalanced diet can mean a long-term energy surplus, a "
                "long-term energy shortfall, or a specific nutrient missing. "
                "Obesity raises the risk of type 2 diabetes, heart disease and "
                "joint damage. Prolonged energy shortfall breaks down first "
                "fat and then muscle, and stops growth. Deficiency diseases — "
                "scurvy, rickets, anaemia — are caused by one missing nutrient "
                "and can occur at any level of energy intake.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # MRB-225: evidence quality, method criticism and history of science live
    # HERE. Nothing above is retracted by it — the three imbalances are not
    # withdrawn; a story is told about how one of them was discovered and
    # misread.
    "stretch": [
        {"type": "explainer", "id": "lind-and-the-gap",
         "text": "In 1747 the naval surgeon James Lind ran what is often "
                 "called the first controlled clinical trial, on twelve scurvy "
                 "patients divided into six pairs, each pair given a different "
                 "treatment: cider, sulfuric acid, vinegar, seawater, a paste "
                 "of herbs, or two oranges and a lemon. The citrus pair "
                 "recovered. The trial was tiny, it was not blinded, and Lind "
                 "himself did not fully accept the result — he thought the "
                 "fruit worked by helping digestion and later recommended a "
                 "boiled-down concentrate that destroyed the vitamin C "
                 "entirely. The Navy took another forty years to adopt lemon "
                 "juice, and it saved more sailors than any battle of the "
                 "period. Good evidence and correct interpretation are "
                 "different achievements, and the gap between them is measured "
                 "in lives."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to work through why a deficiency can happen on a "
                      "full plate?",
              "cta": "Ask about this lesson",
              "anchor": "s-three"},

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # Every clinic is a set of measurements and signs reasoned from, and the
    # third confrontation is a direct instruction about which evidence counts.
    "ws": ["analysis-and-evaluation"],

    # ⊕ MRB-257 · audit 6.4 — RULED BY MIDE, and the wording is the ruling.
    # The safeguarding blocks named no confidential service: a sweep for
    # childline|0800 1111|nspcc|samaritans|papyrus|frank|shout across all 58
    # rendered pages returned ZERO. This is a public site, and the student who
    # most needs this block is reading it at 11pm, when "your school's PSHE
    # materials" is not reachable. The service is Childline, the number is
    # 0800 1111, joined by a spaced em dash. Shout and FRANK were offered and
    # NOT taken up. The PSHE deferral STAYS as the daytime route — Childline is
    # the out-of-hours one, not a replacement for it.
    #
    # ⚠️ THE TREATMENT IS THE RULING TOO (§8.10): a small `ks3-legal` foot line
    # alongside the existing school-nurse / pharmacist / GP routes, NEVER a
    # callout block. A helpline should be findable and quiet.
    "safeguarding_note": "If any of this is about you or someone you know, "
                         "talk to someone you trust — a parent or carer, a "
                         "teacher, your school nurse, a pharmacist or your "
                         "GP. Out of school hours: Childline — 0800 1111, "
                         "free and confidential.",

    # ⚠️ THE LESSON'S CLOSING LINE, BYTE-IDENTICAL. It sets no targets, gives
    # no advice about anybody's own eating, and points at a trusted adult.
    # `safety_note` is the slot for a page-specific foot line that is not a
    # measurement convention; the engine adds `.ks3-safety`, which is a
    # spacing modifier (`border-top: 0; margin-top: 18px`) and no more, so
    # Design's plain `.ks3-legal` treatment is otherwise unchanged.
    "safety_note": "This lesson describes conditions clinically, as biology. "
                   "It is not advice about anybody's own body or eating, and "
                   "it sets no targets. If any of it worries you about "
                   "yourself or someone you know, speak to a trusted adult, "
                   "your school nurse or a doctor — that is the right next "
                   "step, not a change to what you eat.",

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
