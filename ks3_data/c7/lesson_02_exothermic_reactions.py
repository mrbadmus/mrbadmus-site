"""C7 L2 — Exothermic reactions (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c7/c7-02-exothermic-reactions.dc.html`, and her
author's notes `docs/ks3/design-reference/c7/NOTES-C7.md` §1, §2, §3, §4 flags
5, 6, 7, 8, §5 (`ENER-03`, `ENER-04`) and §6.

Every student-facing string is byte-identical to the approved page except
where a change is marked ⚑ below and reported to the commander. `RAIL`,
`REACTIONS`, `USES`, `RUNGS` and `SELF_RUNGS` came out of the node extractor;
the hook options and reveal, the two explainer paragraphs, the bench's eyebrow
/ heading / lead / predict prompt / readout labels, the closing panel, the key
fact, the `#s-uses` eyebrow and heading, the `#s-think` options and its two
reveal paragraphs, the key note and both "Going further" paragraphs were
lifted from `lessonVals(s)` and from the markup.

── THE ODD BEAKER IS THE LESSON, AND IT IS THE HANDOVER ────────────────

NOTES-C7 §2: "a five-beaker bench with predict-then-run and a start/peak/delta
readout. Four exothermic, one not — the odd one out is the handover to
`c7-03`." So the fifth beaker is not a spare: it is the only place in this
lesson where the student meets a temperature going the other way, and it is
what makes the next lesson a discovery rather than an announcement.

Three things follow and all three are load-bearing:

  · THE STOP TICKS ON THE FIFTH RUN, not the first. Design's
    `DONE('s-bench')` is `Object.keys(s.ran).length >= REACTIONS.length`, and
    the closing panel ("Four went up. One went down.") is a claim no four of
    these beakers can support.
  · EVERY RUN IS GATED BY A PREDICTION (Law 4). `needPredict` is `!ran` and
    the readout is not on screen until the student has said which way the
    thermometer will go.
  · THE VERDICT IS DERIVED FROM THE ARITHMETIC, NEVER AUTHORED BESIDE IT.
    `r_temp_bench` computes `end − start`, derives exothermic from the SIGN,
    and raises if the authored `exo` flag disagrees or if a run's delta is
    zero. A bench that can reach a state it has no label for is the §5A defect
    this unit's other three instruments are also checked against.

── THE FLAGS ──────────────────────────────────────────────────────────

⚑ flag 5 — THE FIVE TEMPERATURE PAIRS ARE ILLUSTRATIVE CLASSROOM VALUES, NOT
MEASUREMENTS, and the page now SAYS SO. Design's numbers are kept exactly
(21→60, 20→27, 20→34, 21→50, 20→12); what is added is one sentence in the
bench's lead making their status plain. MRB-225: a figure that is illustrative
must be labelled as one, and a number left unlabelled on a bench reads as a
reading somebody took.

⚑ flag 6 — THE HAND WARMER STAYS, AND SO DOES THE ADMISSION. Trial 4 is sodium
ethanoate crystallising out of a supersaturated solution, and the run's own
reason says in as many words that it is a change of state rather than a
chemical reaction. ACCEPTED as drawn: the honesty is the teaching. It is also
the only run on this bench that connects to `c7-01`, which is what stops the
previous lesson reading as a detour.

⚑ flag 7 — IRON RUSTING IN A DISPOSABLE HAND WARMER (use 1). Correct, and it
cashes in C5's oxidation lesson: rusting is exothermic like any oxidation, and
the only trick is making it fast enough to feel.

⚑ flag 8 — COMPOST HEAPS AT 60 °C AND SELF-IGNITING HAY stay in the stretch.
Both are real. Not tangential: it is the one place in the unit where the same
arithmetic is shown running without any apparatus at all.

⚑ NOTES §6 asks for SVG ARROWS in the start→peak readout, and that is what
`r_temp_bench` draws. Never the character U+2192 — the shipped font subsets do
not carry it, so a typed arrow drops to a system font mid-line inside a 26px
display row.
"""

# ── the five beakers (Design's `REACTIONS`) ─────────────────────────────
#
# ⚠️ `exo` IS A GUARD, NOT A RENDERED FIELD. `r_temp_bench` derives the verdict
# from `end − start` and raises if this flag disagrees with the sign, which is
# the §5A "drive the equal state and check it" rule applied to a bench whose
# whole readout is one subtraction. Nothing here reaches the page as a mark.
#
# ⚑ Flag 5: every `start` / `end` pair below is Design's own and is an
# ILLUSTRATIVE classroom value rather than a measurement. The bench's lead says
# so on the page.
_REACTIONS = [
    {"id": "x1", "label": "Burning magnesium", "start": 21, "end": 60,
     "exo": True,
     "setup": "A coil of magnesium ribbon lowered into a beaker of water, lit "
              "at the top with a Bunsen. Thermometer in the water.",
     "why": "Combustion, and one of the fiercest exothermic reactions in a "
            "school lab. It needed a flame to start — and then gave out "
            "enough energy to be dangerous to look at directly."},
    {"id": "x2", "label": "Acid + alkali", "start": 20, "end": 27,
     "exo": True,
     "setup": "25 cm³ of hydrochloric acid with 25 cm³ of sodium hydroxide "
              "stirred in. Thermometer in the mixture.",
     "why": "Neutralisation is exothermic, and you noticed this without being "
            "told: the beaker warmed while you were titrating in the acids "
            "unit. A rise of seven degrees from two clear liquids that look "
            "unchanged afterwards."},
    {"id": "x3", "label": "Magnesium + acid", "start": 20, "end": 34,
     "exo": True,
     "setup": "A strip of magnesium dropped into 25 cm³ of dilute "
              "hydrochloric acid. Thermometer in the acid.",
     "why": "A metal reacting with an acid is strongly exothermic. This is "
            "the reaction that produced the squeaky pop, and the warm tube "
            "was evidence you had already collected without naming it."},

    # ⚑ Flag 6, KEPT WHOLE. "Not strictly a chemical reaction — it is a change
    # of state" is the sentence NOTES asks about, and it stays. A lesson that
    # quietly filed a crystallisation as a reaction would be teaching a wrong
    # boundary in order to keep a tidy list of five.
    {"id": "x4", "label": "Hand warmer", "start": 21, "end": 50,
     "exo": True,
     "setup": "A commercial reusable hand warmer, snapped and placed against "
              "the thermometer bulb.",
     "why": "Sodium ethanoate crystallising out of a supersaturated solution. "
            "Not strictly a chemical reaction — it is a change of state — but "
            "the energy accounting is identical: the particles fall together "
            "and release what was stored."},

    # The handover. It is fifth on purpose: four runs establish the pattern,
    # and the fifth breaks it in front of a student who now expects it not to.
    {"id": "x5", "label": "Citric acid + baking soda", "start": 20, "end": 12,
     "exo": False,
     "setup": "Citric acid solution with sodium hydrogencarbonate stirred in. "
              "Thermometer in the mixture.",
     "why": "The temperature fell by eight degrees. Energy went from the "
            "surroundings into the reaction rather than out of it — the "
            "opposite of every other beaker on this bench, and the subject of "
            "the next lesson."},
]

# ── the three judgements (Design's `USES`) ──────────────────────────────
#
# ⚠️ `use-fireworks` IS `ENER-04`'s CONFRONTATION SITE and its `id` is emitted
# on the card, with `use-fireworks-reveal` on the answer paragraph. Both names
# are authored here rather than composed in the renderer, so the register's
# join and the markup have one source.
_USES = [
    {"id": "use-rust", "correct": "a",
     "q": "A disposable hand warmer contains iron powder, salt and sawdust, "
          "and gets warm when the packet is opened to the air. What is the "
          "reaction?",
     "options": [
         {"id": "a", "label": "The iron rusting"},
         {"id": "b", "label": "The salt dissolving"},
         {"id": "c", "label": "The sawdust burning"},
     ],
     "answer": "The iron oxidising — rusting, deliberately made fast. Salt "
               "speeds it up and the sawdust holds everything in contact with "
               "air. Rusting is exothermic like any oxidation; normally it is "
               "so slow that the energy escapes unnoticed, and the trick here "
               "is simply making it fast enough to feel."},
    {"id": "use-engines", "correct": "b",
     "q": "Why do power stations, cars and your own body all rely on "
          "exothermic reactions?",
     "options": [
         {"id": "a", "label": "They are the only reactions that work"},
         {"id": "b", "label": "Because energy given out can be used to do "
                              "something"},
         {"id": "c", "label": "Because they are cheaper"},
     ],
     "answer": "Because getting energy out is the entire point. A power "
               "station burns fuel, a car burns petrol, and your cells "
               "respire glucose — three very different settings running the "
               "same accounting. An endothermic reaction would take energy "
               "in, which is useful for cooling but no use for driving "
               "anything."},
    {"id": "use-fireworks", "correct": "b",
     "q": "A student says fireworks prove chemical reactions create energy. "
          "Are they right?",
     "options": [
         {"id": "a", "label": "Yes"},
         {"id": "b", "label": "No — the energy was already stored in the "
                              "chemicals"},
         {"id": "c", "label": "Only for large fireworks"},
     ],
     "answer": "No, and this is the important sentence in the lesson. Energy "
               "cannot be created. It was stored in the chemicals before the "
               "firework was lit, and the reaction released it as light, heat "
               "and sound. The firework is a container for energy that was "
               "put there when it was manufactured — the same accounting as a "
               "battery."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 235 character for character.
    "slug":        "exothermic-reactions",
    "title":       "Exothermic reactions",
    "discipline":  "chemistry",
    "unit":        "energy-changes-in-reactions",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.C.ENER.02` is one bullet naming two opposite behaviours and claimed
    # by three lessons, so its clauses are minted in `ks3_data/substatements.py`
    # on the pattern C5 used for `CR.03a–e`. This lesson is clause `a`.
    "covers":      ["KS3.C.ENER.02a"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 3},
                    {"id": "substances-and-reactions", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # The page's "Before this lesson" card links to c7-01, and it has to: the
    # hand warmer run is a change of state, and a student who has not met
    # `c7-01` cannot be told that a crystallisation and a combustion share
    # their energy accounting. Two beakers on the bench are reactions the
    # student has already run and not named — neutralisation and metal with
    # acid — so both are referenced, as is oxidation for use 1.
    "requires":    ["energy-and-changes-of-state"],
    "assumes":     [],
    "references":  ["neutralisation", "acid-plus-metal", "oxidation"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Every fire you have ever seen is one reaction giving out "
                    "more energy than it took to start it. Nothing was added "
                    "— so where does the heat come from?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, Design's `RAIL`, matching `docs/ks3/rail-manifest.md` stop
    # for stop (MRB-249). `done_when` restates her own `DONE()`.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "The hand warmer", "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "Five beakers", "done_when": "all_five_run"},
        {"anchor": "s-uses",   "short": "USES",
         "label": "Three judgements", "done_when": "all_three_decided"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Starting versus running", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚠️ THE HOOK CLOSES EVERY OTHER DOOR. "No battery, no flame, nothing
    # plugged in, and nothing added from outside" is what makes the question
    # answerable: without it, "it was plugged in" is not a wrong answer.
    "phenomenon": {
        "kind": "narrative",
        "title": "A hand warmer is a sealed plastic pouch. Snap the metal disc "
                 "inside and it reaches 50 °C, in a pocket, on a cold day.",
        "prompt": "No battery, no flame, nothing plugged in, and nothing "
                  "added from outside. The pouch was sitting at the same "
                  "temperature as the room a moment before. It stays hot for "
                  "about an hour, then goes cold — and it can be reset by "
                  "boiling it.",
        "commit": "Where does the heat come from?",
        "options": [
            "From your body, stored up in the pocket",
            "From energy already stored in the chemicals",
            "From friction when the disc is snapped",
            "It is created by the reaction out of nothing",
        ],
        "reveal": "From energy that was already stored in the chemicals. "
                  "Snapping the disc starts a change, and as the contents "
                  "rearrange they release energy that was locked in the "
                  "arrangement they had before. Nothing is created — the "
                  "energy was there all along, stored where a thermometer "
                  "could not see it. A change that <strong>gives energy "
                  "out</strong> to its surroundings is called "
                  "<strong>exothermic</strong>.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ EVERY JOIN RESOLVES AGAINST THIS PAGE'S OWN MARKUP (MRB-244/248).
    #
    # ⊖ NOTES-C7 §5 proposes `think-reveal-balance` for `ENER-03`. No
    # `think-reveal-*` id can be emitted from a lane — `build_ks3.py`'s shared
    # `r_activity` draws the confrontation reveal with no id at all — so the
    # join names the ACTIVITY that owns both the commitment and the reveal.
    #
    # ⊕ `ENER-04`'s two names ARE both emitted here, by `r_energy_uses`:
    # `id="use-fireworks"` on the card and `id="use-fireworks-reveal"` on the
    # answer paragraph that says energy cannot be created.
    #
    # ⚑ `ENER-03` overlaps C8's `PTAB-07` ("sodium melted because the water was
    # hot"): both are heat coming OUT of a reaction being read as heat that
    # went in. NOTES-C8 §5 asks for the cross-reference to be recorded rather
    # than merged. They are elicited by different phenomena and stay separate.
    #
    # ⊕ CORRECTED 21 Aug 2026 (MRB-281). This used to be recorded as PROSE in
    # `docs/ks3/misconception-register.md` instead of as a `reappears_in`
    # value, on the stated ground that "C8 is drawn but not yet authored" and
    # that `group-1-the-alkali-metals` "is not in ks3_data/structure.py".
    #
    # BOTH HALVES WERE FALSE. C8 was authored and delivered on 21 Aug — six
    # lessons, notes and support — and had been sitting in the main worktree's
    # working directory the whole time. A worktree shares `.git` but NOT its
    # working directory, so an UNTRACKED delivery dropped into one tree is
    # invisible from every other tree, and looking from this lane and finding
    # nothing was read as the unit not existing. The slug was then absent from
    # `structure.py` only because §7's five-slot plan had never been updated to
    # C8's real lesson list.
    #
    # ⊖ CORRECTED AGAIN, SAME DAY, AND THE SECOND CORRECTION IS THE ONE THAT
    # STUCK. The first attempt authored `reappears_in` as a LESSON KEY here.
    # It is not one: `reappears_in` is a REGISTER COLUMN and the register is
    # the only place it exists. `grep -rn reappears_in build_ks3.py ks3_data/`
    # returns docstring mentions and NO READ SITE, so a key authored here is
    # dead under contract R5 — `ks3_key_audit.py` reported it as "read by
    # nothing", which is exactly what it was. `ks3_data/b11/lesson_01` had
    # already ruled this and said so in as many words.
    #
    # So the edge lives in `docs/ks3/misconception-register.md`, in the ENER
    # section's "Where these are expected to resurface" list, which is the
    # established form and the one the register's own §52 schema describes.
    # That is still a correction of the original defect: the original recorded
    # the overlap as a REASON NOT TO record an edge, on a false premise. The
    # edge is now recorded, in the form this project keeps edges in.
    "misconceptions": [
        {"id": "ENER-03",
         "statement": "A reaction that needs heating to start cannot be "
                      "exothermic.",
         "elicited_by": "think-commit-spark",
         "confronted_by": "think-commit-spark"},
        {"id": "ENER-04",
         "statement": "Chemical reactions create energy.",
         "elicited_by": "use-fireworks",
         "confronted_by": "use-fireworks-reveal"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "An <strong>exothermic</strong> change transfers energy to "
                 "its surroundings. The surroundings get warmer — which is "
                 "why the test for one is a thermometer in the beaker, not in "
                 "the flame."},
        {"type": "explainer",
         "text": "Most reactions you have met are exothermic. Combustion, "
                 "neutralisation, respiration, a metal reacting with acid, "
                 "and every reaction in the displacement grid gave out "
                 "energy. It is common enough that people forget it needs "
                 "explaining at all."},

        # #s-bench — the flagship. Light `ks3-block` → `check`.
        #
        # ⚠️ NO NARRATION OF THE CONTROLS (§5A). Design draws the eyebrow, the
        # h2 and the live progress line, with no instruction between them. The
        # predict prompt and the button labels ARE the instruction.
        {"type": "temp-bench", "id": "bench-five", "anchor": "s-bench",
         "eyebrow": "Your turn · five beakers, one thermometer",
         "heading": "Predict the temperature change, then run it.",
         "demand": "investigate",
         "head_counter": {"format": "{n} of {total} run", "start": 0,
                          "total": 5},
         # ⚑ Design's live line reads "{n} of 5 run. Four of these five do the
         # same thing. Run all five — the odd one out is the point." The COUNT
         # is the head-row readout, which is the platform's one live element
         # for it, and the teaching half stays here as the block's lead. The
         # third sentence is new prose and is flag 5's label: the numbers on
         # this bench are illustrative, and a bench that does not say so is a
         # bench presenting invented figures as readings.
         "prompt": "Four of these five do the same thing. Run all five — the "
                   "odd one out is the point. The temperatures are typical "
                   "classroom values chosen to show the pattern, not readings "
                   "from one particular afternoon.",
         "reactions": _REACTIONS,
         "setup_label": "The set-up",
         # Law 4. The readout is not on screen until the student has said
         # which way the thermometer will go, and the gate stays visible
         # afterwards so the commitment can be compared with the reading.
         "predict": {"prompt": "Predict before you run it.",
                     "options": [
                         {"id": "up", "label": "Temperature rises"},
                         {"id": "same", "label": "No change"},
                         {"id": "down", "label": "Temperature falls"},
                     ]},
         "start_label": "Start",
         "peak_label": "Highest reading",
         "arrow_word": "rises to",
         # Derived at build time from `end − start` and checked against `exo`.
         "label_exo": "exothermic",
         "label_not_exo": "not exothermic",
         "close_id": "bench-close",
         "close_title": "Four went up. One went down.",
         "close": [
             "Combustion, neutralisation, metal with acid and the hand warmer "
             "all warmed their surroundings — they are exothermic, and "
             "between them they cover most of the chemistry you have done so "
             "far. The fifth got colder, which means energy went the other "
             "way. That one has its own name and its own lesson.",
             "Note what the thermometer is actually in. <strong>It is in the "
             "mixture, and it is reading the surroundings getting "
             "warmer.</strong> Exothermic is defined by what happens outside "
             "the reaction, not inside it.",
         ]},

        {"type": "key-fact", "ref": "energy-out"},

        # #s-uses — three judgements. Light `ks3-block` → `check`.
        {"type": "energy-uses", "id": "uses-exo", "anchor": "s-uses",
         "eyebrow": "Three judgements",
         "heading": "Exothermic on purpose, and exothermic by accident",
         "demand": "classify",
         "head_counter": {"format": "{n} of {total} decided", "start": 0,
                          "total": 3},
         "uses": _USES},

        # ⊖ NOT A RAIL STOP. Design's own `RAIL` does not carry `#s-words`.
        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. If "
                 "you cannot say it, you do not know it yet.",
         "terms": ["Exothermic", "Surroundings", "Chemical store",
                   "Combustion", "Neutralisation"]},

        {"type": "misconception", "id": "think-commit-spark",
         "anchor": "s-think", "targets": "ENER-03"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # None. NOTES-C7 §6 declares no figure anywhere in the unit; the bench's
    # start→peak readout is the picture, and its arrow is drawn as SVG inside
    # the instrument rather than as a separate figure.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "energy-out",
         "text": "An exothermic change gives energy out to its surroundings, "
                 "so the temperature of the mixture rises. The energy was "
                 "stored in the chemicals before the reaction started.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        {"id": "think-commit-spark",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-03",
         "prompt": "A Bunsen really is needed to light the magnesium. Commit "
                   "before you read on.",
         # ⚑ MRB-177 / MRB-278 — THE THREE DISTRACTORS ARE RE-AUTHORED AND THE
         # CORRECT OPTION IS UNTOUCHED. Design's set ran 15 words against 9,
         # 10 and 7 — strictly longest and clear of the field by five, which a
         # student can answer on shape alone. Each distractor now states its
         # wrong rule at full length: 14, 15, 13, 14.
         "options": [
             "Right — a reaction that needs energy put in cannot be giving "
             "energy out",
             "Wrong — the spark only starts it; far more energy comes out "
             "than went in",
             "Right, because the Bunsen is the real source of the heat you "
             "feel",
             "Wrong — a truly exothermic reaction would never need starting "
             "in the first place",
         ],
         "reveal": [
             "Starting a reaction and running it are two different accounts. "
             "Petrol needs a spark; a match needs striking; magnesium needs a "
             "flame. That initial energy gets the reaction going — and once "
             "it is going, it gives out far more than the spark ever "
             "supplied, which is why the flame keeps burning after you take "
             "the match away.",
             "The test is the balance, not the beginning. <strong>Exothermic "
             "means more energy comes out than went in.</strong> If the spark "
             "were the whole story, a car would need to be lit continuously — "
             "and a forest fire would go out the moment the lightning "
             "stopped.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # ⚑ MRB-278 · ANSWER POSITION. Design puts the correct option first on both
    # marked rungs. C7's eight marked rungs are authored level across the four
    # indices; this lesson holds index 2 and index 3. Only the ORDER moves —
    # no option text is edited and every `feedback` key is re-keyed to the
    # index its own option now sits at.
    "ladder": {
        "recall": {
            "q": "What happens to the temperature of the surroundings during "
                 "an exothermic change?",
            "options": [
                "It falls, because the reaction takes energy in",
                "It stays the same, because energy is conserved",
                "It rises, because energy is transferred out of the reaction",
                "It rises only if the reaction is lit with a flame",
            ],
            "answer": 2,
            "feedback": {
                0: "That describes an endothermic change — the next lesson.",
                1: "Energy is conserved, but it moves. Conservation does not "
                   "mean nothing happens.",
                3: "A hand warmer needs no flame and still warms its "
                   "surroundings.",
            }},
        # ⚑ MRB-177 — THE THREE DISTRACTORS ARE RE-AUTHORED AND THE CORRECT
        # OPTION IS UNTOUCHED. Design's set ran 12 words against 8, 6 and 6:
        # the answer states a RULE about the balance of energy and each
        # distractor stated a short wrong reason. Each now states a WRONG RULE
        # at the same length — 11, 11, 11 against 12 — and every one of
        # Design's corrections still answers its own option, because each
        # option still makes the claim it always made.
        "apply": {
            "q": "Burning methane needs a spark to start. Does that make it "
                 "endothermic?",
            "options": [
                "Yes, because energy has to be supplied before it will start",
                "It is endothermic at first and exothermic once the flame "
                "catches",
                "It depends how big the spark is compared with the fuel",
                "No — far more energy comes out than the spark put in",
            ],
            "answer": 3,
            "feedback": {
                0: "Supplying a start is not the same as the reaction taking "
                   "energy in overall. The flame keeps burning after the "
                   "spark is gone.",
                1: "The reaction is exothermic throughout. The spark only "
                   "gets the first molecules going.",
                2: "The size of the spark changes nothing about the energy "
                   "the reaction releases.",
            }},
        "explain": {
            "q": "A student mixes an acid and an alkali and the thermometer "
                 "rises by 7 °C. Explain what this shows, where the energy "
                 "came from, and why the beaker cools down again after a few "
                 "minutes.",
            "field_label": "Your explanation",
            "placeholder": "The temperature rise shows…",
            "success": [
                "Says the temperature rise shows the reaction is exothermic.",
                "Says energy has been transferred from the reaction to the "
                "surroundings.",
                "Says the energy was stored in the chemicals beforehand, not "
                "created.",
                "Says the reaction finishes, so no more energy is released.",
                "Says the warm beaker then loses heat to the room until it "
                "reaches room temperature.",
            ]},
        "produce": {
            "q": "A company wants to sell a self-heating food can. Explain "
                 "what they need from the chemistry, and give two safety "
                 "problems they would have to solve.",
            "field_label": "Your answer",
            "placeholder": "They need a reaction that…",
            "success": [
                "Says they need an exothermic reaction.",
                "Says it must release enough energy to warm the food to a "
                "useful temperature.",
                "Says it must not get so hot that it burns the user or bursts "
                "the can.",
                "Says the reactants must be kept separate until the user "
                "starts it.",
                "Says the chemicals must not contaminate the food, or must be "
                "sealed away from it.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "An exothermic change transfers energy to the surroundings, "
                "so the temperature of the mixture rises. Combustion, "
                "neutralisation, respiration and metals reacting with acids "
                "are all exothermic. Needing energy to get started does not "
                "stop a reaction being exothermic — what matters is that more "
                "energy comes out than went in.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ Flag 8 lives here and is KEPT byte-identical. The compost heap is not
    # a curiosity: it is the same accounting with no apparatus and no chemist,
    # which is the strongest version of the lesson's own claim.
    "stretch": [
        {"type": "explainer", "id": "self-heating-cans",
         "text": "Self-heating cans of coffee use the reaction between "
                 "calcium oxide and water, which is exothermic enough to "
                 "bring a drink to serving temperature in three minutes from "
                 "a chemical reaction in a sealed compartment. The same "
                 "reaction is a genuine hazard on building sites: quicklime "
                 "dust in a wet eye releases its energy exactly where you "
                 "would least want it."},
        {"type": "explainer", "id": "compost-and-hay",
         "text": "Compost heaps are exothermic on a scale that surprises "
                 "people. Bacteria respiring their way through grass cuttings "
                 "release enough energy to hold the middle of a heap at 60 °C "
                 "through a frost, and a large enough badly-managed pile of "
                 "hay can reach the point of catching fire on its own. "
                 "Farmers have lost barns to it. The energy is coming out of "
                 "the chemical bonds in the plant material, and it makes no "
                 "difference to the arithmetic that the reaction is being run "
                 "by bacteria rather than a Bunsen."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    # ⚠️ The first five `term` strings match the `keyword` block's `terms` BYTE
    # FOR BYTE. `r_keyword` matches by exact string and silently drops a
    # non-match, which renders nothing at all.
    "vocabulary": [
        {"term": "Exothermic",
         "definition": "A change that transfers energy out to its "
                       "surroundings, so the surroundings get warmer.",
         "note": "The test is a thermometer in the mixture, not in the flame."},
        {"term": "Surroundings",
         "definition": "Everything that is not the reaction itself — the "
                       "water, the beaker, the bench and the air. It is the "
                       "surroundings whose temperature you measure.",
         "note": "Exothermic and endothermic are defined by what happens to "
                 "these, not by what happens inside the reaction."},
        {"term": "Chemical store",
         "definition": "Energy held in the way a substance's particles are "
                       "arranged. A reaction can release it or take more in, "
                       "but nothing creates it.",
         "note": "A firework is a container for energy that was put there "
                 "when it was made."},
        {"term": "Combustion",
         "definition": "A substance reacting with oxygen and releasing "
                       "energy. Every combustion is exothermic.",
         "note": "Needing a flame to start is not the same as taking energy "
                 "in overall."},
        {"term": "Neutralisation",
         "definition": "An acid reacting with an alkali to make a salt and "
                       "water. It is exothermic, which is why the beaker "
                       "warms."},
        {"term": "Energy transfer",
         "definition": "Energy moving from one place to another. It is never "
                       "created and never destroyed, so every temperature "
                       "change is energy going somewhere."},
    ],

    # ── safety (§1.5) — not a callout, and not a safeguarding block ─────────
    # ⚑ NEW PROSE, reported to the commander (contract §16) rather than added
    # silently.
    #
    # ⊖ NO SAFEGUARDING BLOCK. Nothing on this page touches a student's own
    # body, health or circumstances in the safeguarding sense — a hand warmer
    # is an object, not a personal risk — so the standing legal line and this
    # note are the right weight. C3, C4 and C5 carried none for the same
    # reason.
    #
    # ⊕ A `safety_note` IS earned, and it is scoped to what THIS bench does.
    # Two of the five runs on it reach 50 °C and 60 °C, one of them is a
    # burning metal, and the hand warmer is the one object here a student can
    # buy. It does not retract the lesson: the page is about running these
    # reactions, and this says how.
    "safety_note": "These are demonstrations. Burning magnesium is blinding "
                   "to look at directly and is watched through the eye "
                   "protection everyone in the room is already wearing. A "
                   "reusable hand warmer is reset by boiling it in a pan of "
                   "water on a hob, never in a microwave and never by an "
                   "unsupervised student.",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why a match does not disprove this?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Energy level diagrams, activation energy, and bond "
                   "breaking and making as the reason a reaction gives energy "
                   "out.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
