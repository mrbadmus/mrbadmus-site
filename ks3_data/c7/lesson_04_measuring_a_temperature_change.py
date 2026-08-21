"""C7 L4 — Measuring a temperature change (INVESTIGATION).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c7/c7-04-measuring-a-temperature-change.dc.html`,
and her author's notes `docs/ks3/design-reference/c7/NOTES-C7.md` §1, §2, §3,
§4 flags 12, 13, 14, §5 (`ENER-07`, `ENER-08`) and §6.

Every student-facing string is byte-identical to the approved page except
where a change is marked ⚑ below and reported to the commander. `RAIL`, `PLAN`,
`RIGS`, `RUNGS` and `SELF_RUNGS` came out of the node extractor; the hook
options and reveal, the two explainer paragraphs, both instrument heads, the
dial labels and option labels, the readout labels, both closing panels, the key
fact, the `#s-think` options and its two reveal paragraphs, the key note and
both "Going further" paragraphs were lifted from `lessonVals(s)` and from the
markup.

── CRITIQUE BEFORE CONSTRUCT, AND THE ORDER IS THE ARGUMENT ────────────

NOTES-C7 §2: "a plan critique (five steps, sound or flawed) followed by a
three-dial rig builder with eight combinations and a true value the student
never reaches."

`#s-plan` comes FIRST, and that is the map's rule for an INVESTIGATION lesson
and c3-07's standing precedent: ruling on somebody else's method is what makes
building your own a decision instead of a recipe. A student who has already
decided that "go and write up the method while it reacts" wrecks the result
does not then need to be told that timing is one of the three dials.

── THE TRUE VALUE IS NEVER REACHED, AND THAT IS THE WHOLE INSTRUMENT ───

The rig builder has eight combinations and a true value of 7.0 °C. The best
arrangement a school bench can produce reads 6.8, and no dial recovers the last
two tenths. So the payoff panel is not "well done, you found it" — it is
"you found the best rig, and it still reads low", which is the only honest
place `ENER-08` can be confronted from.

`r_rig_builder` enforces all of that at build time (§5A):

  · all eight combinations of the three dials are authored and none is
    surplus — a missing cell would show the previous rig's reading under the
    new rig's label;
  · every reading is STRICTLY BELOW the true value, because the lesson's claim
    is that the error runs one way;
  · the rig named `best` really is the highest reading, derived rather than
    trusted;
  · the "lost" figure beside each reading is `true − reading`, computed, never
    authored twice.

── THE FLAGS ──────────────────────────────────────────────────────────

⚑ flag 12 — +7.0 °C TRUE AND 6.8 BEST. ACCEPTED as drawn, and the numbers are
LABELLED. NOTES says plainly "correct in kind; the numbers are invented", and
MRB-225 says an invented number may never be presented as a measurement. So the
bench's lead now names them as illustrative figures chosen to show what heat
loss does. Nothing else about them moves: the gap is attributed to warming the
cup, the lid and the thermometer, which is where it really goes.

⚑ flag 13 — SYSTEMATIC AGAINST RANDOM ERROR. ACCEPTED at KS3, and NOTES gives
the argument for it: "the experiment cannot be honestly evaluated without it."
It is the most advanced idea in the unit and it is nature-of-science rather
than chemistry, but a lesson that teaches a student to repeat and average
without teaching them what averaging cannot fix has taught a ritual.

⚑ flag 14 — BOMB CALORIMETER AND FOOD PACKET CALORIES stay in the stretch, as
drawn. It is the one place a student is shown that the polystyrene cup is a
cheap version of a real instrument rather than a school compromise, and the
second stretch paragraph says so directly.

⚠️ `rig-plan-critique`, NOT `plan-critique`. `ks3_art/c3.py` already owns
`plan-critique` and the shell class `ks3-critique-block` for c3-07. Same shape,
different plan, different owner — a lane may not edit another unit's module, so
C7 registers its own family and its own class.
"""

# ── the five steps of somebody else's plan (Design's `PLAN`) ────────────
#
# ⚠️ `sound` AND `fatal` ARE GUARDS AND REACH NO MARKUP AS MARKS.
# `r_rig_plan_critique` reads them three ways at build time: to check that each
# step's `verdict` OPENS with the word the record believes, to derive the
# counts the block's lead claims, and to check that exactly one step is fatal.
# Nothing here paints a control — the reveal is the same panel whichever button
# was pressed, and only the ladder marks (R3).
#
# ⚑ Design writes one prose paragraph per step. It is split here into a VERDICT
# line and a REASON, which is c3-07's shape and the shape the renderer draws.
# Her words are kept; only where the sentence breaks is chosen — except on step
# 1, where her opening ("Sound as far as it goes, but the glass beaker is the
# weak point") would have a student who pressed "Sound" reading a verdict that
# opens by agreeing with them and then disagrees. The judgement is stated
# first and her sentence follows it whole.
_PLAN = [
    {"id": "p1", "tag": "Step 1", "sound": False, "fatal": False,
     "step": "Measure 25 cm³ of acid into a glass beaker.",
     "verdict": "Flawed — sound as far as it goes, but the glass beaker is "
                "the weak point.",
     "why": "Glass conducts heat away into the bench and the air, and it "
            "absorbs a share of the energy warming itself up. A polystyrene "
            "cup does neither, and costs less."},
    {"id": "p2", "tag": "Step 2", "sound": True, "fatal": False,
     "step": "Take the temperature of the acid before adding anything.",
     "verdict": "Sound — essential, in fact, and easy to skip.",
     "why": "Without a starting value there is no change to calculate — only "
            "a final number that means nothing on its own. It should be "
            "recorded, not remembered."},

    # The fatal one. It is the only step on this page that is wrong about the
    # QUANTITY rather than about the apparatus, and it is the step the rig
    # builder's third dial is about.
    {"id": "p3", "tag": "Step 3", "sound": False, "fatal": True,
     "step": "Add the alkali, then go and write up the method while it "
             "reacts.",
     "verdict": "Flawed, and this is the one that ruins the experiment.",
     "why": "The peak temperature arrives within seconds and then falls as "
            "heat escapes to the room. Come back two minutes later and you "
            "record a number that is mostly a measure of how long you were "
            "away."},
    {"id": "p4", "tag": "Step 4", "sound": False, "fatal": False,
     "step": "Stir with the thermometer.",
     "verdict": "Flawed — stirring is right, stirring with the thermometer "
                "is not.",
     "why": "Without stirring the thermometer reads one warm pocket rather "
            "than the mixture. But it is a fragile instrument, and a broken "
            "one in a beaker of acid is a genuine incident. Use a stirring "
            "rod."},
    {"id": "p5", "tag": "Step 5", "sound": True, "fatal": False,
     "step": "Record the highest temperature reached, and subtract the "
             "starting temperature.",
     "verdict": "Sound, and the right quantity to record.",
     "why": "The peak is the closest the apparatus gets to the true value, "
            "because from that moment on heat loss is winning. Subtracting "
            "gives the temperature change, which is what the energy transfer "
            "is judged by."},
]

# ── the eight rigs (Design's `RIGS`) ────────────────────────────────────
#
# ⚠️ THE KEY IS `vessel|cover|speed` AND IT IS THE WHOLE STATE SPACE. Two
# containers × two tops × two timings is eight, and all eight are here.
# `r_rig_builder` cross-checks this list against the dials and raises on a
# missing combination or a surplus one.
#
# ⚑ Flag 12: every `v` below is Design's own and is an ILLUSTRATIVE figure. The
# block's lead says so.
#
# ⚠️ NOTES §6: "If a fourth dial is ever added the table doubles — worth
# converting to a computed loss model at that point rather than extending the
# literal." Recorded, not acted on: eight authored explanations are eight
# things a student reads, and a loss model would have to generate them.
_RIGS = [
    {"id": "beaker|open|slow", "v": 2.1,
     "why": "A glass beaker, open to the room, read two minutes late. Almost "
            "two-thirds of the rise has leaked away before anyone looked at "
            "the thermometer. This is the group that reported +2 °C."},
    {"id": "beaker|open|fast", "v": 4.9,
     "why": "Reading promptly saved a great deal — but an open glass beaker "
            "still loses heat upwards and into the bench the whole time."},
    {"id": "beaker|lid|slow", "v": 3.4,
     "why": "The lid helps, and then two minutes of waiting throws the "
            "benefit away. Good apparatus does not rescue slow measurement."},
    {"id": "beaker|lid|fast", "v": 5.6,
     "why": "Better. What is still missing is the insulation: glass conducts, "
            "and some of the energy is warming the beaker itself rather than "
            "the mixture."},
    {"id": "cup|open|slow", "v": 4.2,
     "why": "The cup insulates well, but an open top loses heat by "
            "evaporation and convection — and two minutes is long enough for "
            "that to matter."},
    {"id": "cup|open|fast", "v": 6.3,
     "why": "Close. The polystyrene is doing its job; what is escaping now is "
            "going straight up out of the open top."},
    {"id": "cup|lid|slow", "v": 5.1,
     "why": "Good apparatus, poor timing. The rig would have given you 6.8 if "
            "you had read it when the reaction finished."},
    {"id": "cup|lid|fast", "v": 6.8,
     "why": "The best a school bench will do: insulated, covered, read at the "
            "peak. The missing 0.2 °C went into warming the cup, the lid and "
            "the thermometer, and no arrangement of this apparatus recovers "
            "it."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 237 character for character.
    "slug":        "measuring-a-temperature-change",
    "title":       "Measuring a temperature change",
    "discipline":  "chemistry",
    "unit":        "energy-changes-in-reactions",
    "family":      "INVESTIGATION",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.C.ENER.02` clause `c`, minted in `ks3_data/substatements.py`. NOTES
    # §1 says this lesson "owns no new content", and the clause is what makes
    # that legal rather than a gap: "(qualitative)" is the word in the bullet
    # that makes deciding-by-measurement statutory, and this is the lesson that
    # teaches how the deciding is actually done.
    "covers":      ["KS3.C.ENER.02c"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 3},
                    {"id": "measurement-and-evidence", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Every figure in this unit came out of an apparatus that leaks, so this
    # lesson needs both of the two before it: the plan critique and the rig are
    # both built on a neutralisation, which is C6's, and the whole point of
    # measuring the change is deciding which of `c7-02` and `c7-03` a reaction
    # belongs to.
    "requires":    ["endothermic-reactions"],
    "assumes":     [],
    "references":  ["neutralisation", "exothermic-reactions"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Four groups run the same reaction and get four different "
                    "answers. One of them is closest to right — and it is not "
                    "the one with the neatest handwriting.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, Design's `RAIL`, matching `docs/ks3/rail-manifest.md` stop
    # for stop (MRB-249). `done_when` restates her own `DONE()` — including
    # `s-bench`, which she ticks at THREE rigs run rather than at all eight:
    # three is enough to have compared arrangements, and requiring all eight
    # would make the stop a completionist errand rather than a record of the
    # comparison having been made.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Four answers", "done_when": "committed"},
        {"anchor": "s-plan",   "short": "PLAN",
         "label": "Judge the plan", "done_when": "all_five_ruled_on"},
        {"anchor": "s-bench",  "short": "RIG",
         "label": "Build the rig", "done_when": "three_rigs_run"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "What averaging fixes", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚠️ "NOBODY MADE ANYTHING UP" IS THE DOOR THIS HOOK CLOSES. Without it the
    # obvious answer is that somebody wrote down the wrong number, and the
    # lesson would be about honesty instead of about measurement.
    "phenomenon": {
        "kind": "narrative",
        "title": "Same acid, same alkali, same volumes, same room. Four groups "
                 "report +5, +7, +2 and +7 °C.",
        "prompt": "Nobody made anything up. All four wrote down what their "
                  "thermometer said. The reaction cannot have released a "
                  "different amount of energy in four beakers on the same "
                  "bench.",
        "commit": "What is the most likely reason for the spread?",
        "options": [
            "The reaction released different amounts in each beaker",
            "Differences in how much heat escaped before the reading",
            "Some groups used the wrong chemicals",
            "Thermometers are simply unreliable",
        ],
        "reveal": "How much heat each beaker lost to the room before the "
                  "thermometer was read. A glass beaker on a cold bench with "
                  "an open top is leaking energy the whole time the reaction "
                  "is running, and the slower the group, the more escapes "
                  "before they look. <strong>The reaction is not the "
                  "variable. The measurement is.</strong>",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ EVERY JOIN RESOLVES AGAINST THIS PAGE'S OWN MARKUP (MRB-244/248).
    #
    # ⊖ NOTES-C7 §5 proposes `think-reveal-systematic` for `ENER-07`. No
    # `think-reveal-*` id can be emitted from a lane, so the join names the
    # ACTIVITY that owns both the commitment and the reveal.
    #
    # ⊖ NOTES also proposes `rung-2` / `rung-2-feedback` for `ENER-08`, and the
    # ladder emits no per-rung id, so that join could never resolve. It is
    # re-pointed at the rig builder, which is where the belief is actually
    # taken apart: eight readings that all agree in being too low, and a
    # closing panel that says the error runs one way. `rig-build` is the
    # instrument's own `data-activity`; `rig-close` is an `id` this lesson
    # authors and `r_rig_builder` emits on the payoff panel.
    "misconceptions": [
        {"id": "ENER-07",
         "statement": "Repeating an experiment and averaging makes the result "
                      "accurate.",
         "elicited_by": "think-commit-average",
         "confronted_by": "think-commit-average"},
        {"id": "ENER-08",
         "statement": "Results that agree closely with each other must be "
                      "correct.",
         "elicited_by": "rig-build",
         "confronted_by": "rig-close"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Energy change is measured by measuring temperature — and a "
                 "temperature reading is only as good as the arrangement "
                 "around it. Heat leaks out of an open beaker, into the "
                 "bench, and into the thermometer itself."},
        {"type": "explainer",
         "text": "This lesson is about the decisions that decide whether your "
                 "number means anything: what to measure, what to keep the "
                 "same, and what to insulate against."},

        # #s-plan — critique before construct. Light `ks3-block` → `check`.
        {"type": "rig-plan-critique", "id": "plan-judge", "anchor": "s-plan",
         "eyebrow": "Before you run it · judge someone else's plan",
         "heading": "A student has written a method. Five decisions. Rule on "
                    "each.",
         "demand": "evaluate",
         "head_counter": {"format": "{n} of {total} ruled on", "start": 0,
                          "total": 5},
         # ⚑ Design's live line reads "{n} of 5 ruled on. Two of the five are
         # sound, two are flawed, and one would wreck the result on its own."
         # The COUNT is the head-row readout; the teaching half is the lead,
         # and every number in it is DERIVED from the steps and asserted
         # against this sentence at build time.
         "prompt": "Two of the five are sound, two are flawed, and one would "
                   "wreck the result on its own.",
         "sound_claim": 2,
         "flawed_claim": 2,
         "fatal_claim": 1,
         "options": [
             {"id": "ok", "label": "Sound"},
             {"id": "bad", "label": "Flawed"},
         ],
         "steps": _PLAN},

        # #s-bench — the rig builder. Light `ks3-block` → `check`.
        #
        # ⚠️ NO NARRATION OF THE CONTROLS (§5A). The lead states the true value
        # and what the reading will do; it does not say "press the buttons".
        {"type": "rig-builder", "id": "rig-build", "anchor": "s-bench",
         "eyebrow": "Your turn · build the apparatus",
         "heading": "Three choices, then run it and see what your setup was "
                    "worth.",
         "demand": "investigate",
         # ⚑ Flag 12's label. Design's lead is the first sentence; the second
         # is new prose and is the honesty MRB-225 requires — a figure that was
         # chosen rather than measured has to say so where it is reported.
         "prompt": "The true temperature rise for this reaction is 7.0 °C. "
                   "Your reading will be lower than that by however much heat "
                   "your apparatus lets escape. Both that value and the eight "
                   "readings are illustrative figures chosen to show what "
                   "heat loss does, not measurements from one afternoon.",
         # Design's `dials`. `phrase` is the wording the rig's TITLE uses,
         # which is not the wording on the button — "lid fitted" against "Lid
         # with a hole" — so both are authored and the title is composed from
         # the phrases at build time, once per combination, in the document.
         "dials": [
             {"id": "vessel", "label": "The container", "options": [
                 {"id": "beaker", "label": "Glass beaker",
                  "phrase": "Glass beaker"},
                 {"id": "cup", "label": "Polystyrene cup",
                  "phrase": "Polystyrene cup"},
             ]},
             {"id": "cover", "label": "The top", "options": [
                 {"id": "open", "label": "Open", "phrase": "open to the room"},
                 {"id": "lid", "label": "Lid with a hole",
                  "phrase": "lid fitted"},
             ]},
             {"id": "speed", "label": "When you read it", "options": [
                 {"id": "slow", "label": "After two minutes",
                  "phrase": "read after two minutes"},
                 {"id": "fast", "label": "At the peak",
                  "phrase": "read at the peak"},
             ]},
         ],
         "rigs": _RIGS,
         "true_value": 7.0,
         "true_label": "True value",
         "reading_label": "Your reading",
         "lost_suffix": " °C lost",
         "run_label": "Run it",
         # Derived and checked: `best` must be the highest reading in `rigs`,
         # and every reading must be strictly below `true_value`.
         "best": "cup|lid|fast",
         # Design's own `DONE('s-bench')`: three rigs run, not eight.
         "done_after": 3,
         # ⭐ `ENER-08`'s confrontation site, and the reason the instrument
         # exists. Not "well done", but "you found the best rig and it still
         # reads low".
         "close_id": "rig-close",
         "close_title": "You found the best rig — and it still reads low.",
         "close": [
             "A polystyrene cup with a lid and a fast reading gets you to 6.8 "
             "of the 7.0 degrees. The last two tenths went into warming the "
             "cup, the thermometer and the lid, and no school apparatus "
             "recovers them.",
             "That is worth saying plainly: <strong>every reading here is an "
             "underestimate, and the error runs one way.</strong> An error "
             "that always points the same direction is not random scatter — "
             "it is a systematic error, and repeating the experiment will not "
             "remove it.",
         ]},

        {"type": "key-fact", "ref": "start-peak-difference"},

        # ⊖ NOT A RAIL STOP. Design's own `RAIL` does not carry `#s-words`.
        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. If "
                 "you cannot say it, you do not know it yet.",
         "terms": ["Temperature change", "Insulation", "Peak temperature",
                   "Systematic error", "Random error"]},

        {"type": "misconception", "id": "think-commit-average",
         "anchor": "s-think", "targets": "ENER-07"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # None. NOTES-C7 §6 declares no figure anywhere in the unit — the rig IS
    # the apparatus diagram, and it is one the student assembles.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "start-peak-difference",
         "text": "Measure the start temperature, the highest or lowest "
                 "reading, and take the difference. Insulate, use a lid, and "
                 "read quickly — every escape of heat makes the measured "
                 "change too small.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        {"id": "think-commit-average",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-07",
         "prompt": "Repeating and averaging is genuinely good practice. "
                   "Commit before you read on.",
         # ⚑ MRB-177 / MRB-278 — THE THREE DISTRACTORS ARE RE-AUTHORED AND THE
         # CORRECT OPTION IS UNTOUCHED. Design's set ran 15 words against 8, 7
         # and 8 — clear of the field by seven. Each distractor now states its
         # wrong rule at full length: 14, 15, 14, 13.
         "options": [
             "Right — averaging three results is what makes a measurement "
             "accurate rather than lucky",
             "Wrong — averaging fixes random scatter, not an error that "
             "always runs one way",
             "Right, because more data is always better and three runs beat "
             "one every time",
             "Wrong — repeating an experiment tells you nothing you did not "
             "already know",
         ],
         "reveal": [
             "Averaging fixes <strong>random</strong> error — the scatter "
             "from reading a scale slightly differently each time, or "
             "stirring a bit harder. Those errors fall on both sides of the "
             "truth, so they cancel out.",
             "Heat loss is not like that. It makes every single reading too "
             "low, so the average of three low readings is a low average. "
             "<strong>An error that always points the same way survives any "
             "number of repeats.</strong> The only cure is to change the "
             "apparatus — which is why the lid matters more than the third "
             "run.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # ⚑ MRB-278 · ANSWER POSITION. This lesson holds index 3 and index 2 of
    # C7's level eight. Only the ORDER moves, and every `feedback` key is
    # re-keyed to the index its own option now sits at.
    "ladder": {
        "recall": {
            "q": "What two readings do you need to find the temperature "
                 "change of a reaction?",
            "options": [
                "The room temperature and the final temperature",
                "The temperature at the start and the temperature ten minutes "
                "later",
                "Only the highest temperature reached",
                "The starting temperature and the highest (or lowest) "
                "temperature reached",
            ],
            "answer": 3,
            "feedback": {
                0: "The room may not be at the same temperature as your "
                   "solution. Measure the solution before you start.",
                1: "Ten minutes later the mixture has cooled back towards "
                   "room temperature. You need the peak.",
                2: "Without a starting value there is nothing to subtract "
                   "from, and the number on its own says nothing.",
            }},
        # ⚑ MRB-177 — THE THREE DISTRACTORS ARE RE-AUTHORED AND THE CORRECT
        # OPTION IS UNTOUCHED. Design's set ran 14 words against 8, 9 and 5:
        # the answer states a RULE (what kind of error, and the direction that
        # makes it one) and each distractor stated a short wrong reason. Each
        # now states a WRONG RULE in the same shape at 12, 13 and 13 words, and
        # every one of Design's corrections still answers its own option.
        "apply": {
            "q": "A group insulates the cup, fits a lid, and repeats the "
                 "experiment five times. Their answers are all close together "
                 "but all lower than the true value. What kind of error is "
                 "this?",
            "options": [
                "A random error, which more repeats and a better average "
                "would fix",
                "No error — close agreement between five readings means the "
                "results are correct",
                "A systematic error — heat loss makes every reading low in "
                "the same direction",
                "A mistake in the calculation, repeated the same way in all "
                "five runs",
            ],
            "answer": 2,
            "feedback": {
                0: "Random errors scatter both sides of the truth. These are "
                   "all low, which is the signature of a systematic error.",
                1: "Precise and accurate are different. Five readings can "
                   "agree closely and all be wrong in the same way.",
                3: "A calculation error would not produce consistently low "
                   "readings from a rig that is known to leak heat.",
            }},
        "explain": {
            "q": "Write a method for measuring the temperature change when an "
                 "acid is neutralised by an alkali. Include what you would "
                 "keep the same, and explain the reason behind two of your "
                 "choices.",
            "field_label": "Your method",
            "placeholder": "I would measure 25 cm³ of acid into…",
            "success": [
                "Measures a fixed volume of acid into an insulated container "
                "such as a polystyrene cup.",
                "Records the starting temperature before adding anything.",
                "Adds the alkali, stirs, and records the highest temperature "
                "reached.",
                "Keeps volumes, concentrations and starting temperature the "
                "same between runs.",
                "Explains that a lid and insulation reduce heat loss, so the "
                "measured change is closer to the true value.",
            ]},
        "produce": {
            "q": "A group wants to compare which of three fuels releases the "
                 "most energy, by heating a beaker of water with each in "
                 "turn. Identify the main sources of error in that plan and "
                 "say what they should keep the same.",
            "field_label": "Your answer",
            "placeholder": "The main problem is that most of the heat…",
            "success": [
                "Says much of the heat from the flame escapes into the air "
                "instead of reaching the water.",
                "Says the same volume or mass of water must be used each "
                "time.",
                "Says the distance from flame to beaker must be kept the "
                "same.",
                "Says the same mass of fuel should be burned, or the mass "
                "burned should be measured.",
                "Says the readings will all be underestimates, so the "
                "comparison between fuels is more trustworthy than the "
                "absolute values.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "To measure an energy change, record the starting temperature "
                "and the highest or lowest temperature reached, and subtract. "
                "Insulating the container, fitting a lid and reading promptly "
                "all reduce heat loss to the surroundings. Heat loss makes "
                "every reading too small, and because the error always runs "
                "the same way, repeating the experiment will not correct it.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ Flag 14 lives here and is KEPT byte-identical.
    "stretch": [
        {"type": "explainer", "id": "bomb-calorimeter",
         "text": "Professional versions of this experiment are done in a bomb "
                 "calorimeter: a sealed steel vessel sitting in a measured "
                 "mass of water inside an insulated jacket, with the whole "
                 "assembly weighed and its own heat capacity measured "
                 "beforehand. The reaction is ignited electrically and the "
                 "water temperature is tracked to a hundredth of a degree. "
                 "The calorie figures on the back of a food packet come from "
                 "a machine like that, burning a sample of the food and "
                 "measuring the water."},
        {"type": "explainer", "id": "the-cup-is-real-apparatus",
         "text": "The polystyrene cup you chose is a genuine piece of "
                 "scientific apparatus, not a school compromise. It works "
                 "because polystyrene foam is mostly trapped air, and air is "
                 "a poor conductor; the same principle is in a wetsuit, a "
                 "duvet and the walls of a house. What makes it good enough "
                 "for a classroom is that its own heat capacity is small — a "
                 "glass beaker absorbs a noticeable share of the energy just "
                 "warming itself up, and a plastic cup barely does."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    # ⚠️ The first five `term` strings match the `keyword` block's `terms` BYTE
    # FOR BYTE.
    "vocabulary": [
        {"term": "Temperature change",
         "definition": "The highest or lowest temperature reached, minus the "
                       "starting temperature. It is the quantity an energy "
                       "change is judged by.",
         "note": "One reading on its own says nothing. You need both."},
        {"term": "Insulation",
         "definition": "Material that slows heat escaping. Polystyrene foam "
                       "works because it is mostly trapped air, and air is a "
                       "poor conductor."},
        {"term": "Peak temperature",
         "definition": "The highest reading the thermometer reaches. From "
                       "that moment on, heat loss to the room is winning and "
                       "the number falls.",
         "note": "Read it when the reaction finishes, not when you get round "
                 "to it."},
        {"term": "Systematic error",
         "definition": "An error that pushes every reading the same way. Heat "
                       "loss is one: it makes every measured change too "
                       "small.",
         "note": "Repeating and averaging will not remove it. Only changing "
                 "the apparatus will."},
        {"term": "Random error",
         "definition": "An error that scatters readings on both sides of the "
                       "true value — reading a scale slightly differently "
                       "each time, for instance.",
         "note": "This is the kind that repeating and averaging really does "
                 "reduce."},
        {"term": "True value",
         "definition": "The value a perfect measurement would give. Real "
                       "apparatus gets close to it and this apparatus never "
                       "quite reaches it."},
    ],

    # ── safety (§1.5) ───────────────────────────────────────────────────────
    # ⊖ NO `safety_note`, AND THAT IS DELIBERATE. This is the one lesson in the
    # unit that teaches its own safety INSIDE the content: step 4 of the plan
    # critique rules on stirring with the thermometer and says in as many words
    # that a broken one in a beaker of acid is a genuine incident. A note at
    # the foot repeating it would be the platform saying twice what the lesson
    # has already taught once, which is what the prose bar is for.

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why averaging does not fix heat loss?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Calorimetry with real calculations, energy per gram of "
                   "fuel, and evaluating systematic error in a required "
                   "practical.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation",
           "measurement-and-units"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
