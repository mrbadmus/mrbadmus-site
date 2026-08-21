"""C2 L6 — Conservation of mass (QUANTITATIVE).

Authored against Design's approved page,
`docs/ks3/design-reference/c2/c2-06-conservation-of-mass.dc.html` (942 lines),
and its measured specification, `docs/ks3/c2-inventory/PAYLOAD-MAP.md` §7.

Every student-facing string is byte-identical to the approved page.

── MRB-204 as amended: this formula is a SUM ───────────────────────────

NOTES-C2 flag 14 asked whether "drawn as a triangle" is literal. MRB-204 as
amended 15 Aug 2026 answers it: **TRIANGLE for products, BALANCE-BEAM and
part–whole BAR for sums and conservation statements.** A triangle encodes one
quantity as the product or quotient of two others; "everything before =
everything after" is neither, and drawing it as one would teach a false
relationship in order to make a rule fit.

Design's page is already compliant, and it was measured rather than assumed:
`c2-06` contains the word "triangle" **zero** times, and the bar's parts sum
to the whole to the pixel (296 + 8 + 146 = 450). All four parts of the ruling
are met — the rule gets its own block alone, it is drawn, the worked example
reveals one step at a time, and the student fills the same four steps on the
other reaction before any independent question.

The bar's part widths are DERIVED from the authored weights below rather than
laid out by flex, because the arithmetic is the teaching: a bar model whose
halves do not add up is a bar model that lies.

── The third tile never measures ───────────────────────────────────────

`Mass before` and `Mass after` are read off the balance. `Where it went` reads
*not measured — you work it out*, takes no data, and never changes. It is the
QUANTITATIVE family's refusal-to-tell, exactly as `p3-01`'s light gates do it,
and it is a real tile beside the two that report — not prose.

── Two corrections, both reported ──────────────────────────────────────

1. **The progress readout.** Design's is `'{n} of 4 runs done'` while the
   stage ticks at three (page lines 773 and 723; map F5). Corrected to three,
   which is what the stage requires, in line with every other counter in C2 —
   all of which are completion bars whose total IS their tick condition. The
   count is clamped, so a student who runs all four reads "3 of 3 runs done":
   a completion bar that has completed, rather than a promise the gate does
   not keep. **The label changed; what ticks did not.**

2. **`magnesium:sealed` is NOT corrected**, and that is deliberate. See the
   flag on the runs below — the masses cross Mide's examiner gate and they are
   his to rule on, not a build's.

⚑ For Mide's science gate, from Design's NOTES:
  * flag 18 — 2.40 g Mg → 4.00 g MgO is exact for Mg 24 and O 16. The
    marble-and-acid pair (152.00 → 149.80, so 2.20 g of CO₂) is plausible
    bench data, not measured. Confirm both, and confirm 2 d.p. on a balance.
  * flag 19 — phlogiston in the stretch layer, and whether a second
    nature-of-science stretch belongs in the same unit as c2-01's.
"""

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 172 character for character.
    "slug":        "conservation-of-mass",
    "title":       "Conservation of mass",
    "discipline":  "chemistry",
    "unit":        "atoms-elements-and-compounds",
    "family":      "QUANTITATIVE",

    # ── curriculum position ─────────────────────────────────────────────────
    # AEC.04's wording covers changes of state AND chemical reactions; C1's
    # `changes-of-state` owns the first half, which is why the sideways link
    # below is load-bearing rather than decorative.
    #
    # ⊕ NARROWED to clause `a` on 2026-08-20 (MRB-246), when C4's
    # `mass-in-a-reaction` arrived and needed the reactions half. The bullet
    # names its two contexts out loud and is now split at that seam; the
    # reasoning is written out in full against `KS3.C.AEC.04` in
    # `ks3_data/substatements.py`.
    #
    # ⚠️ NOT A CONTENT CHANGE. This lesson still teaches both contexts and not
    # one student-facing byte of it moved. `covers` records which lesson is
    # ANSWERABLE for a clause, never which lesson may mention it — the same
    # distinction PIS.04's four clauses are minted on.
    "covers":      ["KS3.C.AEC.04a"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 3},
                    {"id": "particles", "level": 3}],
    "typical_year": 7,
    "typical_minutes": 60,

    # ── progression edges ───────────────────────────────────────────────────
    # ⚠️ `connects_heading` is DELIBERATELY ABSENT. This is the last lesson in
    # the unit, so the middle end-matter card takes the generator's default
    # heading `Connects to` and points SIDEWAYS at C1 — which is exactly what
    # Design draws (page line 457). Every other C2 lesson overrides it to
    # "Next in this unit".
    "requires":    ["formulae"],
    "assumes":     [],
    "references":  [{"unit": "C1", "lesson": "changes-of-state"}],
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "A candle burns down to nothing. A nail rusts and gets "
                    "heavier. One of those looks like mass being destroyed and "
                    "one like mass being made. Neither is.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FIVE stops. ⚠️ There is NO rail stop for the rule block or the worked
    # example: they are read, not done, and MRB-208 says the rail carries only
    # sections that require the student to do something. The QUANTITATIVE
    # four-part sequence occupies three page sections and one rail stage.
    "rail": [
        {"anchor": "s-hook",    "short": "HOOK",
         "label": "Where the wax went", "done_when": "committed"},
        {"anchor": "s-balance", "short": "BALANCE",
         "label": "Open and sealed", "done_when": "three_runs_done"},
        {"anchor": "s-build",   "short": "STEPS",
         "label": "Your own four steps", "done_when": "steps_opened"},
        {"anchor": "s-think",   "short": "THINK",
         "label": "Burning and mass", "done_when": "committed"},
        {"anchor": "s-ladder",  "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    "phenomenon": {
        "kind": "narrative",
        "title": "Sixty grams of candle, and by morning there is nothing on "
                 "the plate.",
        "prompt": "Light a candle in the evening and leave it. In the morning "
                  "the wax is gone, the plate is clean, and the balance reads "
                  "what an empty plate reads. Nothing was taken away and "
                  "nobody touched it.",
        "commit": "So where did sixty grams of wax go?",
        "options": [
            "It was destroyed",
            "It turned into heat and light",
            "It left as invisible gases",
            "It soaked into the plate",
        ],
        "reveal": "Into the air, as two invisible gases, and it weighs "
                  "<em>more</em> than the wax did — because oxygen from the "
                  "room joined it. Every atom that was in the wax is still "
                  "somewhere in the room. Catching them is a matter of "
                  "choosing the right container.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚑ ATOM-11 is PART-05 in a chemical costume, exactly as the register
    # predicted. Minted as its own ID because the confrontation is different —
    # a sealed flask, not a sealed bag — and it carries the cross-reference.
    "misconceptions": [
        {"id": "ATOM-11",
         "statement": "When something burns, the mass is destroyed — it turns "
                      "into heat and light.",
         "elicited_by": "think-commit-burning",
         "confronted_by": "think-commit-burning"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A reaction rearranges atoms. It does not make any and it "
                 "does not destroy any. So the mass of everything you started "
                 "with must equal the mass of everything you end with — as "
                 "long as you can weigh all of it."},

        # #s-balance — the flagship. Ink-dark practical, one canvas.
        {"type": "balance-bench", "id": "open-and-sealed", "anchor": "s-balance",
         "eyebrow": "At the bench · two reactions, two vessels",
         "heading": "The balance reports. It does not explain.",
         # ⊖ CORRECTED. Design's readout says "of 4" and the stage ticks at
         # three. The label is corrected to what ticks; what ticks is not
         # changed, and the clamp means a fourth run still reads "3 of 3".
         "head_counter": {"format": "{n} of 3 runs done", "total": 3},
         "done_at": 3,
         "demand": "investigate",
         "targets": "ATOM-11",
         "prompt": "One reaction gives off a gas and one takes a gas in. Run "
                   "each of them open to the air and then sealed, and read "
                   "what the balance says.",
         "gate": {"prompt": "Commit first. Marble chips react with acid in an "
                            "open flask, fizzing hard. What does the balance "
                            "do?",
                  "options": ["The reading goes down", "The reading goes up",
                              "The reading does not change",
                              "It goes up while it fizzes, then back down"]},
         "reactions": [
             {"id": "marble", "label": "Marble chips and acid"},
             {"id": "magnesium", "label": "Burning magnesium"},
         ],
         "vessels": [
             {"id": "open", "label": "Open flask"},
             {"id": "sealed", "label": "Sealed flask"},
         ],
         "start_vessel": "open",
         "labels": {
             "reaction": "Reaction",
             "vessel": "Vessel",
             "unit": "g",
             "unmeasured": "—",
             "before_tag": "BEFORE",
             "after_tag": "AFTER",
             "open": "open flask",
             "sealed": "sealed flask",
             "status_idle": "The balance is zeroed with everything on it, "
                            "flask included.",
             "status_done": "Read the two numbers, then change something and "
                            "run it again.",
             "idle_note": "Nothing has happened yet. The display shows the "
                          "mass of the whole apparatus before the reaction "
                          "starts.",
         },
         "run_labels": {"idle": "Start the reaction",
                        "done": "Reaction finished"},
         "liquid_colours": {"marble": "rgba(143,183,255,0.35)",
                            "magnesium": "rgba(255,197,61,0.28)"},
         "gas_labels": {"out": "gas leaving the flask",
                        "in": "oxygen joining from the air"},
         "alt": {"template": "A flask on a top-pan balance, {vessel}. The "
                             "display reads {mass} grams {when} the reaction.",
                 "open": "open to the air",
                 "sealed": "sealed with a bung",
                 "before": "before",
                 "after": "after"},
         "decimals": 2,
         # ⚖️ THE THIRD TILE NEVER MEASURES ANYTHING. It is the family's
         # refusal-to-tell and it is a real tile, not prose.
         "tiles": [
             {"id": "before", "label": "Mass before"},
             {"id": "after", "label": "Mass after"},
             {"id": "gone", "label": "Where it went",
              "body": "not measured — you work it out"},
         ],
         # ⚑ **FOR MIDE — `magnesium:sealed` reuses the MARBLE masses.**
         # `magnesium:open` runs 2.40 → 4.00 and `magnesium:sealed` runs
         # 152.00 → 152.00, so switching from open to sealed on the magnesium
         # reaction jumps the display from 2.40 g to 152.00 g with nothing on
         # the page explaining it. It is arguably defensible — a sealed flask
         # weighs the whole apparatus, and 152.00 g is a plausible
         # flask-plus-contents mass — and the note never quotes the number.
         # But it is undocumented in NOTES, unmentioned in flag 18, and it is
         # the one place in the unit where two runs share a number for no
         # stated reason (map F7).
         #
         # **Reproduced exactly as Design drew it, and NOT corrected here.**
         # These masses cross the examiner gate, which is Mide's alone. If he
         # wants it coherent, the smallest change that keeps "sealed changes
         # nothing" true is a magnesium-consistent pair — e.g. 152.00 → 152.00
         # becomes 84.60 → 84.60 with a line saying the flask is on the
         # balance too — and it is one number in each of two places below.
         "runs": {
             "marble:open": {"before": 152.00, "after": 149.80, "gas": "out",
                                "note": "The balance falls by 2.20 g. Carbon dioxide is bubbling out of the flask and into the room, and it has mass — the reading is not wrong, the weighing is incomplete."},
             "marble:sealed": {"before": 152.00, "after": 152.00, "gas": "none",
                                "note": "Exactly the same reading. The gas is still made, and it is still in the flask, so it is still on the balance. Nothing about the reaction changed; what changed is how much of it you weighed."},
             "magnesium:open": {"before": 2.40, "after": 4.00, "gas": "in",
                                "note": "The balance rises by 1.60 g. Nothing was added by hand — oxygen from the air has joined the magnesium, and it weighs something."},
             "magnesium:sealed": {"before": 152.00, "after": 152.00, "gas": "none",
                                "note": "No change. The oxygen that joins the magnesium was already inside the sealed flask and already on the balance, so moving it from the air into the powder changes nothing."},
         }},

        # ── the rule, alone in its own block (MRB-204 part 1) ──────────────
        # Not a rail stop: it is read, not done.
        {"type": "formula", "id": "the-rule",
         "eyebrow": "The rule",
         "statement": "total mass of everything before = total mass of "
                      "everything after",
         "support": ["everything means the gases too",
                     "mass is measured in grams (g)"],
         # part 2 — DRAWN, in the shape the relationship has.
         "figure": {
             "shape": "balance",
             "aria_label": "A balance beam, level. On the left pan: the total "
                           "mass of everything you started with. On the right "
                           "pan: the total mass of everything you ended with. "
                           "The two are equal.",
             "pans": {"left": "before", "right": "after"},
             "caption": "always level"},
         # the cover interaction, on a part–whole BAR.
         "cover": {
             "shape": "bar",
             "eyebrow": "The bar",
             "heading": "Cover the one you want",
             "aria_label": "A bar model. One long bar is everything before the "
                           "reaction. Underneath, the same length is split "
                           "into two: what is left in the flask, and the gas. "
                           "Covering one part leaves the way to work it out.",
             "whole": {"id": "whole", "label": "everything before",
                       "button": "Cover the whole"},
             # ⚖️ The weights ARE the arithmetic: 296 + 8 + 146 = 450, Design's
             # own pixels. Derived, never laid out by flex.
             "parts": [
                 {"id": "left", "label": "left in the flask",
                  "button": "Cover what is left", "weight": 296},
                 {"id": "gas", "label": "the gas",
                  "button": "Cover the gas", "weight": 146},
             ],
             # Radio, never none, and it opens covered.
             "covered": "gas",
             "results": {
                 "whole": {"result": "before = left in the flask + the gas",
                            "sentence": "Cover the whole bar and you are left with the two parts side by side — add them."},
                 "left": {"result": "left in the flask = before − the gas",
                            "sentence": "Cover the left part and you are left with the whole bar and the gas — take the gas away from the whole."},
                 "gas": {"result": "the gas = before − left in the flask",
                            "sentence": "Cover the gas and you are left with the whole bar and what stayed behind — take one away from the other. This is the one an open flask asks you for."},
             },
             "close": "Two parts side by side make the whole. Cover the part "
                      "you want and take the other one away from the whole."}},

        # ── the worked example (MRB-204 part 3) — read, not done ───────────
        {"type": "worked-example", "id": "magnesium-worked"},

        # ── #s-build (MRB-204 part 4) — the student fills the same four ────
        {"type": "fifa-pick", "id": "your-four-steps", "anchor": "s-build",
         "ground": "inset",
         "eyebrow": "Your turn · the same four steps",
         "heading": "Marble and acid, open flask: 152.00 g before, 149.80 g "
                    "after.",
         "demand": "construct",
         "prompt": "Work out the mass of gas that left the flask. Commit to "
                   "each line, then open the worked version.",
         "picks": [
             {"label": "Step 1 · The rule",
              "options": [
                  "total mass before = total mass after",
                  "mass of solid before = mass of solid after",
                  "mass after = mass before + mass of gas",
              ]},
             {"label": "Step 2 · Insert",
              "options": [
                  "152.00 = 149.80 + mass of gas",
                  "149.80 = 152.00 + mass of gas",
                  "mass of gas = 152.00 + 149.80",
              ]},
         ],
         "field": {"label": "Steps 3 and 4 · Work it out, then answer",
                   "hint": "Your answer as a number",
                   "placeholder": "0.00",
                   "unit_hint": "Unit",
                   # ⚠️ The placeholder is its own key because it renders with
                   # an EMPTY value. Design's page gives it `value=""`; giving
                   # it a real value satisfies the gate and lets a student
                   # open the model without ever choosing a unit.
                   "unit_placeholder": "choose a unit",
                   "units": ["g", "kg", "cm³", "N"]},
         "button": "Show the four steps",
         "progress": {"format": "{n} of 3 lines committed", "done": "Opened"},
         "reveal_head": "The open flask, done four ways",
         "steps": [
             {"letter": "F", "label": "Formula",
              "line": "total mass before = total mass after",
              "note": "The gas counts, even though it has left the flask."},
             {"letter": "I", "label": "Insert",
              "line": "152.00 = 149.80 + mass of gas",
              "note": "Everything that started on the balance is on the left; "
                      "everything that ended up anywhere is on the right."},
             {"letter": "F", "label": "Fine-tune",
              "line": "mass of gas = 152.00 − 149.80",
              "note": "Cover the gas on the bar. Rearranged so the unknown is "
                      "alone, and both masses are already in grams."},
             {"letter": "A", "label": "Answer",
              "line": "mass of gas = 2.20 g",
              "note": "That is carbon dioxide, now in the room. Seal the flask "
                      "and those 2.20 g stay on the balance."},
         ],
         # ⚖️ Quotes the student's own input back beside the worked answer.
         # A comparison they make, never a mark the page makes.
         "close": {"template": "You wrote {answer} {unit}. The worked answer "
                               "is 2.20 g.",
                   "blank": "—"}},

        {"type": "key-fact", "ref": "rearranged-never-made"},

        {"type": "misconception", "id": "think-commit-burning",
         "anchor": "s-think", "targets": "ATOM-11"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "rearranged-never-made",
         "text": "Atoms are rearranged in a reaction, never created or "
                 "destroyed. If the mass appears to change, a gas has come in "
                 "from the air or escaped into it.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # The worked example (MRB-204 part 3). Staged: one step at a time, on
        # tap, one-way. `label` on each step takes Design's chipped treatment —
        # a 38px accent square holding the letter, a mono label, a display line
        # and a note — rather than the shipped `letter · name` concatenation.
        {"id": "magnesium-worked",
         "kind": "worked-example",
         "demand": "explain",
         "eyebrow": "Worked example · one step at a time",
         "heading": "2.40 g of magnesium burns and leaves 4.00 g of white "
                    "powder.",
         "head_counter": {"format": "Step {n} of 4", "total": 4},
         "staged": True,
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All four shown",
                     "done_note": "Now the same four steps on the other "
                                  "reaction."},
         "fifa": [
             {"letter": "F", "label": "Formula",
              "line": "total mass before = total mass after",
              "note": "Nothing is created and nothing is destroyed. Everything has to be counted, including the gas."},
             {"letter": "I", "label": "Insert",
              "line": "2.40 g + mass of oxygen = 4.00 g",
              "note": "The magnesium was weighed; the oxygen came from the air and was not."},
             {"letter": "F", "label": "Fine-tune",
              "line": "mass of oxygen = 4.00 − 2.40",
              "note": "Cover the part you want on the bar. Rearranged so the unknown is on its own, with both masses in grams."},
             {"letter": "A", "label": "Answer",
              "line": "1.60 g of oxygen joined from the air",
              "note": "The powder is heavier than the metal because it contains something that was not on the balance to start with."},
         ]},

        # ── #s-think · commit, then two paragraphs (contract R1) ────────────
        {"id": "think-commit-burning",
         "kind": "predict",
         "demand": "explain",
         "targets": "ATOM-11",
         "prompt": "This is the same wrong idea you met when a puddle dried "
                   "up, wearing different clothes. Commit before you read on.",
         "options": [
             "Burning uses a fuel up, so the mass really is destroyed "
             "and gone",
             "The mass leaves as gases, and the products weigh more than the "
             "fuel did",
             "Heat has weight of its own, so the mass turns into heat "
             "and escapes",
             "Gases weigh nothing, so all of the mass stays behind in "
             "the ash",
         ],
         "reveal": [
             "Heat and light are not made of atoms, so nothing that leaves as "
             "heat or light can account for a gram of anything. Burn 60 g of "
             "candle wax in a sealed box and weigh the box afterwards: it "
             "reads exactly what it read before, warm or not.",
             "What actually happens is that the wax joins with oxygen from the "
             "air and leaves as carbon dioxide and water vapour — which "
             "together weigh <strong>more</strong> than the wax did. The "
             "reason it looks like destruction is that the products are "
             "invisible and they float away. Put a lid on and the illusion "
             "goes with them.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    "ladder": {
        "recall": {
            "q": "18 g of a metal reacts completely with 32 g of sulfur in a sealed tube. What mass of metal sulfide is made?",
            "options": [
                "14 g",
                "32 g",
                "50 g",
                "It cannot be worked out without knowing the metal",
            ],
            "answer": 2,
            "feedback": {
                0: "That is 32 − 18. Nothing has been taken away here; the two substances joined.",
                1: "That is the sulfur alone. The metal is still in the tube and still has mass.",
                3: "Conservation of mass does not care which metal it is. Everything that went in is still in the sealed tube.",
            }},
        "apply": {
            "q": "An iron nail is weighed, left to rust for a month, and weighed again. It is heavier. Why?",
            "options": [
                "Rust is denser than iron",
                "Oxygen from the air has joined the iron, and it has mass",
                "Water has been absorbed into the metal",
                "Mass is not conserved when something is left for a long time",
            ],
            "answer": 1,
            "feedback": {
                0: "Density is mass in a given space. The balance measures mass, and mass does not increase by rearranging what is already there.",
                2: "Water speeds rusting up, but the extra mass is oxygen that has chemically joined the iron.",
                3: "Time changes nothing. The nail was simply never a closed system — the air was part of the reaction all along.",
            }},
        "explain": {
            "q": "A candle is weighed, burnt for an hour, and weighed again. It has lost 12 g. Explain where the 12 g went, and describe an experiment that would prove you right.",
            "field_label": "Your explanation",
            "placeholder": "The wax has reacted with…",
            "success": [
                "Says the wax reacted with oxygen from the air.",
                "Says the products are gases — carbon dioxide and water vapour — which floated away.",
                "Says the gases have mass, and that they were not weighed.",
                "Says the total mass of the products is more than 12 g, because the oxygen is in them too.",
                "Describes burning the candle in a sealed container and weighing the whole thing before and after.",
            ]},
        "produce": {
            "q": "A sealed bag of steel wool is weighed, shaken and left until the wool has rusted, then weighed again. Predict the reading, then say what would be different if the bag had a small hole in it, and explain both.",
            "field_label": "Your answer",
            "placeholder": "In the sealed bag the reading would…",
            "success": [
                "Predicts no change in the sealed bag.",
                "Says the oxygen that joins the iron was already inside the bag and already on the balance.",
                "Says with a hole the reading would go up.",
                "Explains that more oxygen can be drawn in from outside through the hole.",
                "States conservation of mass as the reason both readings make sense.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Total mass before a reaction equals total mass after it, "
                "because atoms are only rearranged. In an open vessel a gas "
                "can leave or join, so the balance changes; seal the vessel "
                "and it never does.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    "stretch": [
        {"type": "explainer", "id": "phlogiston",
         "text": "For two hundred years chemists explained burning by saying "
                 "that a substance called phlogiston escaped from things as "
                 "they burnt. It fitted: burning wood loses mass, and a candle "
                 "goes out in a sealed jar because the air is full of "
                 "phlogiston and cannot take any more. Then someone weighed a "
                 "burning metal carefully, found it got <em>heavier</em>, and "
                 "the theory needed phlogiston to have negative mass. That is "
                 "the point at which a model stops being repairable — and the "
                 "weighing had been possible the whole time."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── safety (§1.5) — not copyright, and not a callout ────────────────────
    "safety_note": "Burning magnesium is dangerously bright. Never look "
                   "straight at it, and never seal a flask that is being "
                   "heated.",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Not sure why a sealed flask behaves differently?",
              "cta": "Ask about this lesson",
              "anchor": "s-balance"},

    "ks4_becomes": "Balancing equations by mass, reacting masses, and "
                   "calculating what a reaction can produce.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["measurement", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
