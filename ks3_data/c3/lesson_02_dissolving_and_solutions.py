"""C3 L2 — Dissolving and solutions (MODEL).

Authored against Design's approved page,
`docs/ks3/design-reference/c3/c3-02-dissolving-and-solutions.dc.html` (709
lines), and her unit notes, `docs/ks3/design-reference/c3/NOTES-C3.md`
(§2, §3.2, §4, §5, §6).

Every student-facing string is byte-identical to the approved page. `RAIL`,
`SOLUTES`, `TEMPS`, `CARDS`, `RUNGS` and `SELF_RUNGS` came out of the node
extractor; the hook, gate and think options, the dial and readout labels, the
beaker captions, both alt texts, the verdict and summary sentences and the two
key statements were lifted from `lessonVals()` at the foot of that page, which
is where the majority of this lesson's words live.

── THE RATE / AMOUNT SPLIT IS THE WHOLE LESSON ──────────────────────────

Read this before touching the bench payload. NOTES §3.2: *"if Code lets
stirring change the grams the lesson is worthless."*

    HOW MUCH dissolves   ← the solute, and the temperature.  NOTHING ELSE.
    HOW FAST it dissolves ← the temperature, stirring, and how finely ground.

The data is shaped so that split cannot be got wrong by accident, and that
shape is LOAD-BEARING, not tidiness:

  * the grams live in `solutes[].grams`, keyed by TEMPERATURE ONLY. There is
    no stir key and no powder key anywhere near them, so an amount that
    responded to stirring could not be looked up — it would have to be
    invented.
  * every factor that touches the clock lives in `bench["timing"]`, and
    `timing` holds no grams at all.

Two dials therefore feed the seconds readout and cannot reach the grams
readout, because the number they would have to change does not exist in
their half of the payload. Do not "simplify" these two blocks into one map.

── Salt is on the bench to BREAK the rule ───────────────────────────────

NOTES §2: salt's solubility barely moves with temperature — 35.8 / 36.4 /
38.1 g — and it is there precisely because "hot water dissolves more" is what
a student is about to over-learn from sugar's 190 / 240 / 360 g. The bench
summary and the stretch layer both say so in as many words. Keep both.

── The one LOCKED instrument in the unit ────────────────────────────────

`#s-gate` is a predict-gate: the student commits to which dial changes HOW
MUCH before `#s-lab` opens at all (`bench["locked_by"]`). `demo_mode` is the
front-of-class dial that opens the bench without it, and NOTES §6 is explicit
that it must never be the default in a student build — it is authored `False`
here and nothing should change that.

⚑ For Mide's science gate, from Design's NOTES §4 (rulings in the report):
  * flag 1 — sugar 190 / 240 / 360 g per 100 g water at 10 / 40 / 80 °C. Kept.
  * flag 2 — salt 35.8 / 36.4 / 38.1 g, and foregrounded. Kept, and it is the
    best teaching point in the unit.
  * flag 3 — chalk. See the comment on the chalk entry: the page shows the
    word "none", and its 0.001 g never reaches a readout.
  * flag 4 — the SECONDS are computed from a base time and three factors.
    They are plausible and they are not measurements, and nothing on this page
    calls them measured, timed or observed. The readout is labelled "Time for
    10 g to disappear" and the bench is a model.
  * flag 5 — gases becoming less soluble when warmed, with the fizzy drink and
    the river. Kept, in the stretch layer and in rung 4.
"""

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 199 character for character.
    "slug":        "dissolving-and-solutions",
    "title":       "Dissolving and solutions",
    "discipline":  "chemistry",
    "unit":        "mixtures-and-separation",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # ⚠️ KS3.C.PIS.02 reads "mixtures, including dissolving" — one bullet, two
    # clauses, and NOTES §1 splits it deliberately: `pure-or-mixture` teaches
    # what a mixture IS, this lesson teaches the one kind of mixture the
    # statutory wording singles out. Under §4.4 rule 3 a statement is owned
    # exactly once, so the two lessons cannot both own the parent — this one
    # claims the SECOND clause in the order the bullet prints.
    # 👉 `KS3.C.PIS.02b` needs minting in `ks3_data/substatements.py`
    #    ("dissolving", C3), with `02a` ("mixtures") going to `pure-or-mixture`.
    #    That file is not this lesson's to edit; it is called out in the report.
    "covers":      ["KS3.C.PIS.02b"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "particles", "level": 3},
                    {"id": "substances-and-reactions", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # `references` is deliberately empty. The think-reveal points forward to
    # getting the sugar back "two lessons from now", which is
    # `evaporation-and-crystallisation` — but Design's end matter draws exactly
    # two links (back to L1, on to L3) and a `references` edge would add a
    # third the approved page does not have.
    "requires":    ["pure-or-mixture"],
    "assumes":     [],
    "references":  [],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Sugar stirred into water vanishes without a trace. Where "
                    "has it gone, and what decides how much of it can go "
                    "there?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Six stops — the most in C3 (NOTES §6), and the extra one is the gate.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",    "label": "The vanishing sugar",
         "done_when": "committed"},
        {"anchor": "s-gate",   "short": "PREDICT", "label": "Predict first",
         "done_when": "committed"},
        {"anchor": "s-lab",    "short": "BENCH",   "label": "The bench",
         "done_when": "all_temperatures_run"},
        {"anchor": "s-words",  "short": "WORDS",   "label": "Five words",
         "done_when": "all_cards_turned"},
        {"anchor": "s-think",  "short": "THINK",   "label": "Melting",
         "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",  "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    "phenomenon": {
        "kind": "demo",
        "title": "Stir sugar into water and it disappears. Nothing else in "
                 "science does that.",
        "prompt": "100 g of water in a beaker on a balance. 10 g of sugar "
                  "tipped in. Stir until the last grain vanishes and you "
                  "cannot see any sugar anywhere.",
        "commit": "What does the balance read now?",
        "options": [
            "100 g — the sugar has gone",
            "Somewhere between 100 g and 110 g",
            "110 g — everything that went in is still there",
            "More than 110 g — the sugar takes up water",
        ],
        "reveal": "110 g. Every gram of sugar is still in the beaker — you "
                  "just cannot see it, because it has been broken up into "
                  "particles far too small to see and spread evenly through "
                  "the water. Nothing was destroyed and nothing was made. "
                  "<strong>Dissolving hides a substance; it does not remove "
                  "it.</strong>",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # IDs from NOTES §5's proposed MIX family. ⚠️ `elicited_by` and
    # `confronted_by` are JOINS, not descriptions: MRB-244 and MRB-248 fail the
    # build unless each names an `id="…"` or `data-activity="…"` this page
    # actually emits. Design's notes name the finer beats inside a block
    # (`think-commit-melting`, `think-reveal-melting`, `hook-balance`), and a
    # beat is not a name the document carries — so the section anchor or the
    # activity id that CONTAINS the beat is what is recorded here.
    "misconceptions": [
        {"id": "MIX-03",
         "statement": "Dissolving destroys the solute, or turns it into "
                      "liquid.",
         # NOTES: elicited by `hook-balance` — the balance commitment, which is
         # the hook section itself.
         "elicited_by": "s-hook",
         "confronted_by": "think-again-melting"},
        {"id": "MIX-04",
         "statement": "Stirring harder makes more dissolve.",
         "elicited_by": "gate-which-dial",
         "confronted_by": "dissolve-lab"},
        {"id": "MIX-05",
         "statement": "Dissolving is melting.",
         # NOTES: elicited by `think-commit-melting` and confronted by
         # `think-reveal-melting` — the commit and the reveal of one block.
         "elicited_by": "s-think",
         "confronted_by": "think-again-melting"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Design draws ONE `.ks3-explainer` section holding two paragraphs;
        # `r_explainer` renders one paragraph per block, so the two are
        # authored as two blocks rather than run together into a wall. The
        # words are unchanged. Flagged for the commander.
        {"type": "explainer",
         "text": "The substance that dissolves is the <strong>solute</strong>. "
                 "The liquid it dissolves in is the <strong>solvent</strong>. "
                 "Together they make a <strong>solution</strong> — a mixture, "
                 "spread so evenly that every spoonful is the same."},
        {"type": "explainer",
         "text": "A solute that dissolves is <strong>soluble</strong>; one "
                 "that does not is <strong>insoluble</strong>. And there is a "
                 "limit: keep adding solute and eventually no more will go in. "
                 "The solution is then <strong>saturated</strong>."},

        # #s-gate — THE PREDICT-GATE. Amber, and rightly so: it is a wrong idea
        # (MIX-04) being walked into on purpose, one section before the bench
        # takes it apart. The bench below does not exist on the page until this
        # is answered.
        {"type": "misconception", "id": "gate-which-dial", "anchor": "s-gate"},

        # #s-lab — the flagship. `class="ks3-block"` alone on Design's page:
        # light ground, so the segment is `check`, not `practical`.
        {"type": "dissolve-lab", "id": "dissolve-lab", "anchor": "s-lab",
         "eyebrow": "Your turn · the dissolving bench",
         "heading": "100 g of water. Four dials. Watch which readout moves.",
         "demand": "investigate",
         "targets": "MIX-04",

         # ⚠️ Props Design declares (NOTES §6). `demo_mode` opens the bench
         # WITHOUT the predict-gate — it is the front-of-class dial and it must
         # never be true in a student build.
         "demo_mode": False,
         "show_solubility_numbers": True,

         # The gate that unlocks this bench, by activity id. Nothing else in
         # C3 is locked.
         "locked_by": "gate-which-dial",

         # Where the student finds the dials set when the section opens.
         # `seen` starts holding `warm`, so two more temperatures are needed
         # before the rail stop can tick and before the summary appears.
         "start_state": {"solute": "salt", "temp": "warm",
                         "stir": False, "powder": False, "seen": ["warm"]},

         # ── the four dials ─────────────────────────────────────────────
         "dials": [
             {"id": "solute", "label": "What you are dissolving"},
             {"id": "temp",   "label": "Water temperature"},
             {"id": "stir",   "label": "Stirring",
              "options": [{"value": False, "label": "Left to stand"},
                          {"value": True,  "label": "Stirred"}]},
             {"id": "powder", "label": "The solid",
              "options": [{"value": False, "label": "One lump"},
                          {"value": True,  "label": "Ground to powder"}]},
         ],

         # ── HOW MUCH ───────────────────────────────────────────────────
         # `grams` is keyed by temperature and by nothing else. This is the
         # rate/amount split as data; see the module docstring.
         "solutes": [
             {"id": "salt", "name": "Salt", "colour": "#E4572E",
              "soluble": True,
              "grams": {"cold": 35.8, "warm": 36.4, "hot": 38.1},
              "base_seconds": 90,
              "note": "Sodium chloride. Almost the same amount dissolves "
                      "however hot the water is."},
             {"id": "sugar", "name": "Sugar", "colour": "#8C8377",
              "soluble": True,
              "grams": {"cold": 190, "warm": 240, "hot": 360},
              "base_seconds": 120,
              "note": "Sucrose. Hot water takes nearly twice as much as "
                      "cold."},
             # ⚑ NOTES §4 flag 3. Calcium carbonate is about 0.0013 g per
             # 100 g of water, and this record carries 0.001 g — but the
             # figure NEVER REACHES A READOUT, because `soluble` is False and
             # the amount readout prints `value_insoluble` instead. The number
             # is kept so the payload does not claim chalk is literally zero
             # (sand is), and so a later lesson that wants to say "a trace"
             # has the value rather than inventing one.
             {"id": "chalk", "name": "Chalk", "colour": "#B9AEA0",
              "soluble": False,
              "grams": {"cold": 0.001, "warm": 0.001, "hot": 0.001},
              "base_seconds": 0,
              "note": "Calcium carbonate. Insoluble — it sits there and goes "
                      "cloudy."},
             {"id": "sand", "name": "Sand", "colour": "#9C8F62",
              "soluble": False,
              "grams": {"cold": 0, "warm": 0, "hot": 0},
              "base_seconds": 0,
              "note": "Insoluble in water at any temperature you can reach "
                      "in a beaker."},
         ],

         "temps": [
             {"id": "cold", "label": "10 °C · cold"},
             {"id": "warm", "label": "40 °C · warm"},
             {"id": "hot",  "label": "80 °C · hot"},
         ],

         # ── HOW FAST ───────────────────────────────────────────────────
         # Every factor that touches the clock, and NO grams anywhere in it.
         # seconds = round(base_seconds × temperature[temp]
         #                 ÷ (stirred? 2.2 : 1) ÷ (powder? 1.8 : 1))
         # ⚑ NOTES §4 flag 4: this is a model, not a measurement. Nothing on
         # the page presents these numbers as timed or observed.
         # ⊕ MRB-272 — `round_to: "second"` REMOVED. It had one possible
         # value and nothing read it: both `_dlab_secs` in `ks3_art/c3.py`
         # and `wireDissolveLab` in `shared/ks3.js` round to a whole second
         # outright. Wiring it would have added a branch that can never be
         # taken, which §5A.1 calls authored copy no student will read, and
         # R5 says a key documenting intent belongs in a comment. This is
         # the comment.
         # ⚠️ THE TWO ROUNDINGS MUST STAY IDENTICAL. The renderer writes the
         # resting readout and the wiring recomputes it on every dial press;
         # if they ever round differently the number would flicker by a
         # second on the first interaction, with nothing in the model having
         # changed.
         "timing": {"temperature": {"cold": 2.2, "warm": 1.0, "hot": 0.5},
                    "stirred_divisor": 2.2,
                    "powder_divisor": 1.8},

         # ── the three readouts ─────────────────────────────────────────
         # `note_insoluble: None` means "print the solute's own `note`" — the
         # amount readout is the one place the bench explains WHY there is no
         # number, and the reason is a fact about that solute.
         "readouts": [
             {"id": "amount",
              "label": "How much dissolves in 100 g water",
              "value_format": "{grams} g",
              "value_hidden": "a lot",
              "value_insoluble": "none",
              "note": "Changed only by the solute and the temperature.",
              "note_insoluble": None},
             {"id": "time",
              "label": "Time for 10 g to disappear",
              "value_format": "{seconds} s",
              "value_insoluble": "never",
              "note": "Changed by temperature, stirring and how finely "
                      "ground it is.",
              "note_insoluble": "No amount of stirring will do it."},
             {"id": "appearance",
              "label": "The solution",
              "value": "clear",
              "value_insoluble": "cloudy",
              "note": "Transparent, and coloured only if the solute is "
                      "coloured.",
              "note_insoluble": "The solid is suspended or sitting on the "
                                "bottom, not dissolved."},
         ],

         # ── the beaker diagram ─────────────────────────────────────────
         # DOM circles, not canvas (NOTES §3.2). `{solute}` is the solute's
         # name lower-cased; `{Solute}` is its name as written.
         "beaker": {
             "caption": "In the beaker, particle by particle",
             "water_colour": "#2F5D8A",
             "water_dots": 26,
             "water_dot_size": 11,
             "solute_dot_size": 9,
             # Sugar draws more dissolved particles than salt because far more
             # of it goes in. Insoluble solutes draw none in the solution.
             "dissolved_dots": {"sugar": 12, "salt": 7},
             "undissolved_dots": 10,
             "undissolved_dot_size": 13,
             "alt_soluble": "A particle diagram of a solution: water "
                            "particles with {solute} particles spread evenly "
                            "among them.",
             "alt_insoluble": "A particle diagram of a suspension: water "
                              "particles above, with a layer of undissolved "
                              "{solute} particles resting on the bottom.",
             "bottom_note": "{Solute} on the bottom of the beaker, unchanged. "
                            "Stirring lifts it up; it settles again."},

         # ── the verdict band, under the diagram ────────────────────────
         # `{note}` is the solute's own note. The tail is the rate/amount
         # split said out loud, in whichever of the two states the dials are.
         "verdict": {
             "soluble": "{Solute} is soluble in water. {note} {tail}",
             "tail_worked": "Stirring and grinding got you there faster and "
                            "did not change the grams.",
             "tail_still": "Leave it standing as a lump and it still gets "
                           "there — it just takes longer.",
             "insoluble": "{Solute} is insoluble. {note} The clock and the "
                          "dials make no difference at all."},

         # ── the payoff, once all three temperatures have been run ──────
         # This is the sentence the whole bench exists to earn, and it is the
         # one that names salt as the counter-example.
         "summary": {
             "after_temperatures_seen": 3,
             "text": "You have run all three temperatures. Stirring and "
                     "grinding changed the clock and never changed the "
                     "grams. Heating changed both — and it changed the grams "
                     "by a lot for sugar and hardly at all for salt, which "
                     "is a warning against the phrase \"hot water dissolves "
                     "more\". <strong>How much</strong> depends on the solute "
                     "and the temperature. Nothing else on this bench moves "
                     "it."}},

        {"type": "key-fact", "ref": "how-fast-how-much"},

        # #s-words — five cards, read out of `vocabulary` below.
        {"type": "keyword", "anchor": "s-words",
         # Design's own head and lead, lifted from the approved
         # page. `r_keyword` fell back to "Words to know" and a
         # softer lead until MRB-272 made both authorable.
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each "
                 "card over. If you cannot say it, you do not "
                 "know it yet.",
         "terms": ["Solute", "Solvent", "Solution", "Insoluble", "Saturated"]},

        {"type": "misconception", "id": "think-again-melting",
         "anchor": "s-think"},

        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "how-fast-how-much",
         "text": "Dissolving spreads a solute through a solvent as particles "
                 "too small to see. Stirring and grinding change how fast. "
                 "Temperature changes how much — and by how much depends on "
                 "the solute.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # Both predicts are authored here by hand; `_normalise()` lifts the bench
    # in on top of them.
    "activities": [
        # #s-gate. ⚠️ NO `targets` ON THIS ACTIVITY, deliberately: `targets`
        # is what pulls the register's wrong idea onto the page as a quote,
        # and MIX-04's statement is "Stirring harder makes more dissolve" —
        # printing it directly above "Which dial changes how much will
        # dissolve?" would answer the question the gate exists to ask. Design
        # draws no quote here for the same reason. The join to MIX-04 is made
        # in `misconceptions` above, by this activity's id.
        {"id": "gate-which-dial",
         "kind": "predict",
         "demand": "predict",
         "eyebrow": "Predict first",
         "paragraphs": [
             "The bench below has four dials: what you are dissolving, how "
             "hot the water is, whether you stir, and whether the solid is a "
             "lump or a powder. Two of them change <strong>how fast</strong> "
             "it dissolves. One of them also changes <strong>how much</strong> "
             "can dissolve at all."],
         "prompt": "Which dial changes how much will dissolve?",
         "options": [
             "Stirring",
             "Grinding the solid to a powder",
             "The temperature of the water",
             "All three change how much dissolves",
         ],
         "reveal": "Committed. Go and find out — the bench is below."},

        # #s-think. The quote IS authored rather than taken from the register:
        # MIX-05's register line is "Dissolving is melting", and the line
        # Design drew is the one a student actually says.
        {"id": "think-again-melting",
         "kind": "predict",
         "demand": "explain",
         "targets": "MIX-05",
         "statements": [
             {"quote": "The sugar melted into the water and turned into "
                       "liquid.",
              "body": []},
         ],
         "prompt": "It went in as a solid and now there is only liquid. "
                   "Commit before you read on.",
         "options": [
             "Right — dissolving is melting in water",
             "Wrong — the sugar is still sugar, spread through the water",
             "Right, because both turn a solid into a liquid",
             "Wrong — the sugar has reacted with the water",
         ],
         "reveal": [
             "Melting and dissolving are different events with different "
             "causes. <strong>Melting</strong> needs heat and needs nothing "
             "else present: sugar melts at about 186 °C, and it goes brown "
             "and turns into caramel while it does. <strong>Dissolving</strong> "
             "needs a solvent and happens perfectly well in cold water, at "
             "nothing like 186 °C.",
             "And the sugar has not become water. Boil the solution dry and "
             "the sugar comes back, as sugar, weighing what it weighed. That "
             "is the difference between a mixture and a reaction: "
             "<strong>nothing new was made, so everything can be got "
             "back.</strong> You will get it back on purpose two lessons from "
             "now.",
         ]},
    ],

    # ── vocabulary (§5.4) — Design's five cards ─────────────────────────────
    # `front` → term, `def` → definition, `note` → note, in the page's order.
    "vocabulary": [
        {"term": "Solute",
         "definition": "The substance that dissolves.",
         "note": "The sugar, not the tea."},
        {"term": "Solvent",
         "definition": "The liquid the solute dissolves in.",
         "note": "Usually water. Not always — nail varnish remover is a "
                 "solvent too."},
        {"term": "Solution",
         "definition": "The even mixture a solute and solvent make.",
         "note": "Every spoonful has the same amount in it."},
        {"term": "Insoluble",
         "definition": "Will not dissolve in that solvent.",
         "note": "Sand in water is insoluble. Insoluble in water does not "
                 "mean insoluble in everything."},
        {"term": "Saturated",
         "definition": "No more solute will dissolve at that temperature.",
         "note": "Add more and it just sits on the bottom."},
    ],

    # Design declares no figure on this page — the bench is the figure
    # (NOTES §6). Present and empty, never absent.
    "figures": [],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # RUNGS → recall + apply, SELF_RUNGS → explain + produce. `feedback` is
    # keyed by the INT index of each wrong option, which is what
    # `_rung_marked` reads; the correct index carries none.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Recall",
            "q": "Salt is stirred into water until it disappears. Which is "
                 "the solvent?",
            "options": [
                "The water",
                "The salt",
                "The salt solution",
                "Neither — you need a third substance to be the solvent",
            ],
            "answer": 0,
            "feedback": {
                1: "The salt is the solute — the substance that dissolves. "
                   "The solvent is what it dissolves in.",
                2: "That is the solution: the two of them together, once "
                   "mixed.",
                3: "The solvent is simply the liquid doing the dissolving. "
                   "Here that is the water.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A saturated sugar solution has undissolved sugar on the "
                 "bottom. A student stirs harder to get it in. What happens?",
            "options": [
                "It all dissolves, because stirring makes more dissolve",
                "It all dissolves, but only if you stir for a long time",
                "The sugar on the bottom melts",
                "Nothing more dissolves — stirring changes the speed, not "
                "the limit",
            ],
            "answer": 3,
            "feedback": {
                0: "Stirring only moves solvent past the solid faster. At "
                   "saturation there is nowhere for more to go, however hard "
                   "you stir.",
                1: "Time is not the barrier at saturation. The solution is "
                   "already holding as much as it can at that temperature.",
                2: "Melting needs about 186 °C. Nothing in a cup of tea melts "
                   "sugar.",
            }},
        "explain": {
            "title": "Rung 3 · Explain",
            "q": "10 g of sugar is stirred into 100 g of water and disappears "
                 "completely. A student says the sugar has gone. Use the "
                 "balance reading and the particle model to explain what has "
                 "actually happened, and how you could get the sugar back.",
            "field_label": "Your explanation",
            "placeholder": "The balance still reads 110 g, which shows…",
            "success": [
                "Says the balance still reads 110 g, so nothing has been "
                "destroyed.",
                "Says the sugar has broken up into particles too small to "
                "see.",
                "Says those particles are spread evenly through the water — "
                "that is what a solution is.",
                "Says no new substance was made, so this is a mixture and not "
                "a reaction.",
                "Says evaporating or boiling off the water would leave the "
                "sugar behind.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A fizzy drink goes flat much faster when it is warm, and a "
                 "river in a heatwave can suffocate its fish. Both are about "
                 "a gas dissolved in water. Explain what these two facts have "
                 "in common, and why \"hot water dissolves more\" is a rule "
                 "you should not trust.",
            "field_label": "Your answer",
            "placeholder": "Gases become…",
            "success": [
                "Says gases become less soluble as the temperature rises — "
                "the opposite of sugar.",
                "Applies it to the drink: warm water cannot hold the carbon "
                "dioxide, so it escapes.",
                "Applies it to the river: warm water holds less dissolved "
                "oxygen, so the fish have less to breathe.",
                "Says the temperature rule depends on the solute, so it is "
                "not a general law.",
                "Says a solubility statement needs the solute, the solvent "
                "and the temperature to mean anything.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "A solute dissolves in a solvent to make a solution — a "
                "mixture spread so evenly you cannot see the solute at all. "
                "Nothing is destroyed: the mass stays the same and the solute "
                "can be got back. Stirring and grinding change how fast it "
                "dissolves; temperature changes how much can dissolve, and by "
                "how much depends on the solute. When no more will go in, the "
                "solution is saturated.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES §4 flag 5. Two paragraphs on Design's page, two blocks here for
    # the same reason as the explainer above.
    "stretch": [
        {"type": "explainer", "id": "gases-go-the-other-way",
         "text": "Gases dissolve too, and they break the rule you have just "
                 "learned. Warm a fizzy drink and it goes flat faster, "
                 "because carbon dioxide becomes <em>less</em> soluble as the "
                 "water gets hotter — the opposite of sugar. Cold water holds "
                 "more dissolved oxygen than warm water, which is why a "
                 "heatwave can kill the fish in a shallow river without "
                 "anything being added to it at all."},
        {"type": "explainer", "id": "name-the-solute-and-the-temperature",
         "text": "So \"hot water dissolves more\" is not a law of nature; it "
                 "is a rough rule about solids that has exceptions in both "
                 "directions. Salt barely cares about temperature. Calcium "
                 "sulfate gets slightly <em>less</em> soluble as it warms, "
                 "which is why it plates out inside kettles and boilers. Any "
                 "real solubility claim has to name the solute, the solvent "
                 "and the temperature — which is exactly what the numbers on "
                 "the bench were doing."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why stirring does not get more sugar "
                      "in?",
              "cta": "Ask about this lesson",
              "anchor": "s-lab"},

    "ks4_becomes": "Solubility curves you read values off, and concentration "
                   "in grams per cubic decimetre and in moles.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
