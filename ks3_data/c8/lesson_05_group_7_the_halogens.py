"""C8 L5 — Group 7: the halogens (CONTRAST).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c8/c8-05-group-7-the-halogens.dc.html`, and her
author's notes `NOTES-C8.md` §1, §3, §4, §5 flags 13–16, §6 (`PTAB-08`) and §7.

── ⭐ THIS IS THE LESSON THE UNIT IS BUILT AROUND ───────────────────────

`PTAB-08` — "reactivity always increases going down a group" — is the most
valuable entry in the C8 register, and it exists ONLY as a pair: c8-04 builds
the trend on a water trough, and this grid breaks it. That pairing is the whole
argument for keeping three group lessons rather than §7's merged one (R1).

The archetype is **CONTRAST**, not Design's "PATTERN" (which is not one of the
seven families). Two things — group 1 and group 7 — and ONE discriminating
difference: the direction of the trend. §6 also gives CONTRAST the heaviest
rung 3, which is right for the lesson that breaks the rule the student has just
learned.

── ⚠️ `halogen-grid`, NOT `reactivity-grid` ─────────────────────────────

NOTES-C8 §4 names this instrument `reactivity-grid` "from C5-04 with halogens
substituted", and counts it as that family's third use. That name and its shell
class `ks3-rgrid-block` are OWNED by `ks3_art/c5.py`; re-registering raises on
the duplicate-family gate, and editing c5.py to generalise it would be this
lane reaching into another unit's module. C8 mints its own — the same call C6
made for `acid-metal-grid` and C7 for `rig-plan-critique`. The full reasoning
is in `ks3_art/c8.py`'s header.

⚖️ **What DOES carry from C5 is the ruling about the data: ORDER IS DATA.**
Every cell's verdict is decided by comparing `rank`, in exactly one function
(`_hgrid_reacts`), and every authored cell is checked against it. Re-sorting
the payload cannot change a verdict.

── ⚖️ ALL NINE CELLS ARE AUTHORED, NONE IS COMPOSED ─────────────────────

Design's page builds each cell's title and setup sentence at run time out of
the halogen's name and the salt's ending. Reproducing that would put an
element's name into a sentence by string surgery and make the three "nothing
happens" cells literally one paragraph. All nine are authored, on the C6
`acid-metal-grid` precedent, so each carries its own observation and each
non-reacting cell says what stayed the same rather than repeating a stock
sentence.

Three cells react, three are an element meeting its own salt, and three are a
halogen that cannot beat the one already there. The diagonal is not padding:
it is what shows a student that "nothing happened" is a result.

── ⚑ MRB-278 · ANSWER POSITION ──────────────────────────────────────────

This lesson holds **index 0** (recall, Design's own) and **index 3** (apply,
moved). ⚑ Distractors on BOTH rungs are re-authored for length (MRB-177):
recall ran 11 against 7/8/5 (ratio 1.375, inside the threshold but only just),
apply ran 13 against 5/6/5 (longest by seven). Each is rewritten as a wrong
RULE in the answer's shape; they now run 11 against 10/10/9 and 13 against
12/12/10.

── SCIENCE FLAGS ────────────────────────────────────────────────────────

⚑ Flag 14 — halogen states and colours: fluorine pale yellow gas, chlorine
green gas, bromine red-brown liquid, iodine grey-black solid with violet
vapour. KEPT (R4), all correct.

⚑ Flag 13 — the astatine predictions on rung 4 are extrapolations and the rung
says so. KEPT; predicting a member you have not met IS `PT.04a`'s skill being
re-used, and rung 4 is where it belongs.

⚑ FLAG 15 — CHLORINE AS A 1915 WEAPON STAYS, CONSTRAINED (R4). It is the
strongest thing in that stretch box: the dual-use point is what makes the
chlorination paragraph mean something. FACTUAL AND BRIEF. **No casualty
figures and no description of physiological effects** — neither appears, and
neither may be added.

⊖ Design's closing line was "Dose is the whole difference." It is REPLACED,
not deleted, and the replacement is R4's own teaching: *a substance is not
good or evil — what is done with it is.* Dose is true of the chlorination
half and is not the whole difference between disinfecting a reservoir and
releasing a gas over a trench; leaving it as the summary would teach that the
only thing separating the two is a concentration.

⚑ Flag 16 — fluorine's isolation injuring chemists, Moissan 1886. KEPT and
correct.

⚠️ NOTE THE HALOGENS *DO* HAVE A DENSITY TREND and the key fact states it.
That is not in tension with c8-04's flag-11 ruling: group 1's densities are
0.53, 0.97, 0.86 and are NOT monotonic, while group 7's rise steadily down the
column. The assertion that forbids a density trend is on `water-trough` alone,
for that reason.
"""

LESSON = {
    "slug":  "group-7-the-halogens",
    "title": "Group 7 — the halogens",
    "discipline": "chemistry",
    "unit": "The periodic table",
    "family": "CONTRAST",

    "covers": ["KS3.C.PT.04b"],
    "touches": ["KS3.C.PT.03a", "KS3.C.PT.04a"],
    "beyond_statutory": False,
    "threads": [{"id": "substances-and-reactions", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 55,

    "requires": ["group-1-the-alkali-metals"],
    "assumes": [],
    "references": ["displacement", "groups-and-periods"],
    "connects_heading": "Next in this unit",
    "ks4_links": [],

    "big_question": "Group 1 got fiercer the further down you went. Group 7 "
                    "is the same kind of column with the same kind of "
                    "family — so does it do the same thing?",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Three sealed tubes",  "done_when": "committed"},
        # ⚠️ NO CONTROL ON THIS STOP — see the same note on c8-01's
        # `#s-table`. Design's own `isDone()` gives `{'s-family': 's-hook'}`,
        # which is what this declares.
        {"anchor": "s-family", "short": "FAMILY",
         "label": "The four you need",   "mirrors": "s-hook",
         "done_when": "committed"},
        {"anchor": "s-grid",   "short": "GRID",
         "label": "Nine tubes",          "done_when": "all_nine_run"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Not every group goes the same way",
         "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",      "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Three sealed tubes on the bench: a pale green gas, a "
                 "red-brown liquid and a grey-black solid.",
        "prompt": "They are all in the same group of the periodic table, one "
                  "under the other. Nothing about them looks like a family: a "
                  "gas, a liquid and a solid, in three different colours. "
                  "Warm the grey-black solid gently and it turns straight "
                  "into a violet vapour.",
        "commit": "If they are so different, why are they in the same group?",
        "options": [
            "Because they were all discovered around the same time",
            "Because a group is about chemical behaviour, not appearance",
            "Because they all have similar melting points",
            "Because they are all the same colour underneath",
        ],
        "reveal": "Because a group is about <strong>chemical behaviour</"
                  "strong>, not appearance. All three react with metals to "
                  "make the same kind of compound — a chloride, a bromide, an "
                  "iodide, all with the same formula pattern. Whether an "
                  "element happens to be a gas, a liquid or a solid at room "
                  "temperature is a detail about melting points, and those "
                  "change steadily down the column. The chemistry is the "
                  "family resemblance.",
    },

    "misconceptions": [
        {"id": "PTAB-08",
         "statement": "Reactivity always increases going down a group.",
         "elicited_by": "grid-nine",
         "confronted_by": "grid-close"},
    ],

    # ── the confrontation (Law 3) ───────────────────────────────────────
    # ⚠️ AUTHORED IN `activities`, NOT LIFTED FROM `core`. `_normalise`
    # lifts INSTRUMENT kinds only, so a `misconception` core block whose id
    # names no activity renders as NOTHING AT ALL — `r_activity` returns an
    # empty string and the section, its `id`, its `data-activity` and its
    # rail stop all vanish. The page still builds and still reads.
    #
    # ⚑ The QUOTE is not authored here: `_confrontations` takes it from the
    # row for `targets` in `docs/ks3/misconception-register.md`, so the
    # register and the page have one source and cannot drift.
    "activities": [
        {"id": "think-commit-trend",
         "kind": "predict",
         "demand": "explain",
         "targets": "PTAB-08",
         "prompt": "Group 1 was unambiguous about it. Commit before you read on.",
         # ⚑ MRB-177 / MRB-278 — THE DISTRACTORS ARE RE-AUTHORED AND THE
         # CORRECT OPTION IS UNTOUCHED. Design's set gave the answer away on
         # length alone, which turns a commitment device into a shape puzzle:
         # a student picks the long one, never commits to the belief, and is
         # therefore never confronted with it. Each distractor now states its
         # wrong RULE at full length, which is what MRB-177 asks for.
         # 16, 18, 15, 16 words.
         "options": [
             "Right — every group in the periodic table gets more reactive as"
             " you go further down",
             "Wrong — group 7 gets less reactive downwards, because those"
             " atoms gain an electron instead of losing one",
             "Right, because bigger atoms lower down a group always react more"
             " readily than smaller ones",
             "Wrong — reactivity has nothing to do with an element's position"
             " in a group at all",
         ],
         "reveal": [
             "The two groups do opposite things because they want opposite"
             " things. A group 1 atom reacts by <strong>losing</strong> its"
             " outer electron, and the further out that electron sits, the"
             " easier it goes — so bigger atoms lower down react more. A"
             " group 7 atom reacts by <strong>gaining</strong> an electron,"
             " and a bigger atom pulls an incoming electron in less strongly"
             " — so bigger atoms lower down react less.",
             "One rule about atom size, two opposite trends. <strong>Learn"
             " the reason and you never have to remember which group goes"
             " which way.</strong>",
         ]},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "Group 7 — the <strong>halogens</strong> — are coloured, "
                 "poisonous non-metals. Going down the column they get darker "
                 "and their melting points rise, which is why the top of the "
                 "group is a gas and the bottom is a solid."},
        {"type": "explainer",
         "text": "And going down, they get <strong>less</strong> reactive. "
                 "Fluorine at the top is the most reactive element in the "
                 "whole table; iodine near the bottom is mild enough to be "
                 "painted on skin as an antiseptic. That is the reverse of "
                 "group 1, and it is the fact this lesson is built on."},

        # ── #s-family — the reference. No control; ticked by the hook.
        {"type": "comparison", "anchor": "s-family",
         "eyebrow": "Reference · keep this one open",
         "eyebrow_tone": "accent-text",
         "statement": "The four you need",
         "ground": "card",
         "columns": [{"caption": "At room temperature", "tone": "on-dark"},
                     {"caption": "Reactivity", "tone": "accent-text"}],
         "row_tones": ["band", "accent-tint"],
         "rows": [
             {"name": "Fluorine",
              "cells": ["Pale yellow gas",
                        "The most reactive element in the table"]},
             {"name": "Chlorine",
              "cells": ["Green gas, choking",
                        "Very reactive — kills bacteria in tap water"]},
             {"name": "Bromine",
              "cells": ["Red-brown liquid, orange vapour",
                        "Reactive, but less so than chlorine"]},
             {"name": "Iodine",
              "cells": ["Grey-black solid, violet vapour",
                        "The mildest of the four — used as an antiseptic"]},
         ],
         },

        # ⚑ NOT A `foot` KEY — see the same note on c8-01's comparison block.
        {"type": "explainer",
         "text": "Read the last column downwards. Group 1 got fiercer as you "
                 "descended; this one calms down."},

        # ── #s-grid — nine tubes. Light `ks3-block` → `check`.
        {"type": "halogen-grid", "id": "grid-nine", "anchor": "s-grid",
         "eyebrow": "Your turn · nine tubes",
         "heading": "Three halogens, three salt solutions. Pick a cell, "
                    "predict, then run it.",
         "demand": "predict",
         "resting": "Pick a cell to set up the tube.",
         "resting_mark": "?",
         "row_fmt": "%(name)s water",
         "col_fmt": "potassium %(salt)s",
         "verdict_yes": "A reaction. The colour changes.",
         "verdict_no": "No reaction. Nothing changes.",
         "predict_prompt": "Predict before you run it.",
         "predict_options": [
             {"id": "yes", "label": "The colour changes"},
             {"id": "no",  "label": "Nothing happens"},
         ],
         # ORDER IS DATA. `rank` decides every verdict; see `_hgrid_reacts`.
         "halogens": [
             {"id": "cl", "name": "Chlorine", "rank": 0, "salt": "chloride",
              "colour": "pale green solution"},
             {"id": "br", "name": "Bromine", "rank": 1, "salt": "bromide",
              "colour": "orange solution"},
             {"id": "i",  "name": "Iodine",  "rank": 2, "salt": "iodide",
              "colour": "brown solution"},
         ],
         "cells": {
             "cl:cl": {"reacts": False,
                       "title": "Chlorine water added to potassium chloride",
                       "setup": "A few cm³ of colourless potassium chloride "
                                "solution, with pale green chlorine water "
                                "added on top and shaken.",
                       "obs": "The pale green stays exactly as pale green as "
                              "it went in. Chlorine cannot displace itself, "
                              "and there is nothing else here for it to "
                              "take."},
             "cl:br": {"reacts": True,
                       "title": "Chlorine water added to potassium bromide",
                       "setup": "A few cm³ of colourless potassium bromide "
                                "solution, with pale green chlorine water "
                                "added on top and shaken.",
                       "obs": "The colourless solution turns <strong>orange"
                              "</strong>. That orange is bromine, pushed out "
                              "of its own salt by the more reactive chlorine.",
                       "eq": "chlorine + potassium bromide → potassium "
                             "chloride + bromine"},
             "cl:i":  {"reacts": True,
                       "title": "Chlorine water added to potassium iodide",
                       "setup": "A few cm³ of colourless potassium iodide "
                                "solution, with pale green chlorine water "
                                "added on top and shaken.",
                       "obs": "The colourless solution turns <strong>brown"
                              "</strong> almost at once. The brown is iodine, "
                              "displaced by chlorine from two places above "
                              "it.",
                       "eq": "chlorine + potassium iodide → potassium "
                             "chloride + iodine"},
             "br:cl": {"reacts": False,
                       "title": "Bromine water added to potassium chloride",
                       "setup": "A few cm³ of colourless potassium chloride "
                                "solution, with orange bromine water added on "
                                "top and shaken.",
                       "obs": "Nothing. The orange of the bromine water is "
                              "the only colour in the tube and it does not "
                              "change. Bromine is below chlorine, so it "
                              "cannot take chlorine's place."},
             "br:br": {"reacts": False,
                       "title": "Bromine water added to potassium bromide",
                       "setup": "A few cm³ of colourless potassium bromide "
                                "solution, with orange bromine water added on "
                                "top and shaken.",
                       "obs": "The orange stays orange. An element cannot "
                              "displace itself — there is no more reactive "
                              "halogen in this tube than the one already in "
                              "the salt."},
             "br:i":  {"reacts": True,
                       "title": "Bromine water added to potassium iodide",
                       "setup": "A few cm³ of colourless potassium iodide "
                                "solution, with orange bromine water added on "
                                "top and shaken.",
                       "obs": "The orange darkens to <strong>brown</strong>. "
                              "Bromine could not beat chlorine, but it beats "
                              "iodine — which places it between the two.",
                       "eq": "bromine + potassium iodide → potassium bromide "
                             "+ iodine"},
             "i:cl":  {"reacts": False,
                       "title": "Iodine solution added to potassium chloride",
                       "setup": "A few cm³ of colourless potassium chloride "
                                "solution, with brown iodine solution added "
                                "on top and shaken.",
                       "obs": "No change at all. Iodine is the least reactive "
                              "of the three and chlorine is the most, so this "
                              "is the furthest a displacement could be from "
                              "happening."},
             "i:br":  {"reacts": False,
                       "title": "Iodine solution added to potassium bromide",
                       "setup": "A few cm³ of colourless potassium bromide "
                                "solution, with brown iodine solution added "
                                "on top and shaken.",
                       "obs": "No change. Bromine is above iodine in the "
                              "group, so iodine cannot take its place — even "
                              "though it managed nothing anywhere else "
                              "either."},
             "i:i":   {"reacts": False,
                       "title": "Iodine solution added to potassium iodide",
                       "setup": "A few cm³ of colourless potassium iodide "
                                "solution, with brown iodine solution added "
                                "on top and shaken.",
                       "obs": "The brown stays brown, which is the third time "
                              "an element has met its own salt and done "
                              "nothing. That result is as real as the three "
                              "that changed colour."},
         },
         "close_id": "grid-close",
         "close_title": "Half the grid is empty, and it is the other half "
                        "from last time.",
         "close": [
             "Chlorine displaced both the others. Bromine displaced only "
             "iodine. Iodine displaced nothing at all. Read that as an order "
             "and it says chlorine, then bromine, then iodine — which is the "
             "order they appear going down the column.",
             "<strong>Reactivity decreases going down group 7.</strong>",
             "Same experiment you ran on the metals, same logic, opposite "
             "direction. <strong>A group has a trend; it is not always the "
             "same trend.</strong>",
         ]},

        {"type": "key-fact", "ref": "more-displaces-less"},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. "
                 "If you cannot say it, you do not know it yet.",
         "terms": ["Halogen", "Displacement", "Halide", "Antiseptic",
                   "Trend"]},

        {"type": "misconception", "id": "think-commit-trend",
         "anchor": "s-think", "targets": "PTAB-08"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "figures": [],

    "key_facts": [
        {"id": "more-displaces-less", "placement": "top-level",
         "ground": "card", "eyebrow": "Key fact",
         "text": "The halogens get darker, denser and less reactive going "
                 "down the group. A more reactive halogen displaces a less "
                 "reactive one from its salt — never the other way round."},
    ],

    "ladder": {
        # index 0 — Design's own. ⚑ Distractors re-authored for length.
        "recall": {
            "q": "What happens to reactivity going down group 7?",
            "options": [
                "It decreases — fluorine at the top is the most reactive",
                "It increases going down, exactly as it does in group 1",
                "It stays the same all the way down the group",
                "It increases and then decreases lower down the group",
            ],
            "answer": 0,
            "feedback": {
                1: "Group 1 increases downwards; group 7 does the opposite, "
                   "because those atoms react by gaining an electron rather "
                   "than losing one.",
                2: "Chlorine displaces bromine and bromine displaces iodine. "
                   "That is a clear order.",
                3: "There is no turning point — the trend runs one way from "
                   "fluorine to astatine.",
            }},

        # index 3 — moved from Design's 0. ⚑ Distractors re-authored.
        "apply": {
            "q": "Bromine water is added to potassium chloride solution and "
                 "nothing happens. Why not?",
            "options": [
                "Potassium chloride does not dissolve, so there is nothing "
                "there to react",
                "The bromine water was too dilute for the reaction to be "
                "seen",
                "Bromine only reacts with metals, never with a dissolved "
                "salt",
                "Bromine is below chlorine, so it is less reactive and cannot "
                "displace it",
            ],
            "answer": 3,
            "feedback": {
                0: "It dissolves readily. The solution is there; the reaction "
                   "is not.",
                1: "Concentration changes the speed of a reaction that can "
                   "happen. This one cannot happen at all.",
                2: "Bromine displaces iodine from potassium iodide perfectly "
                   "well. It just cannot beat chlorine.",
            }},

        "explain": {
            "q": "Chlorine water is added to colourless potassium iodide "
                 "solution. Describe what you would see, name the products, "
                 "and explain why the reaction happens.",
            "field_label": "Your explanation",
            "placeholder": "The solution would turn…",
            "success": [
                "Says the colourless solution turns brown.",
                "Says the brown colour is iodine being released.",
                "Names the products as potassium chloride and iodine.",
                "Says chlorine is more reactive than iodine.",
                "Says chlorine is higher up group 7, and reactivity decreases "
                "down the group.",
            ]},

        "produce": {
            "q": "Astatine sits below iodine in group 7. Predict its "
                 "appearance and its reactivity, and explain how you would "
                 "test your prediction about reactivity using only the "
                 "halogens in this lesson.",
            "field_label": "Your answer",
            "placeholder": "Astatine would be…",
            "success": [
                "Predicts a dark, almost black solid.",
                "Predicts it is less reactive than iodine.",
                "Says the trend down the group is towards darker colour and "
                "lower reactivity.",
                "Proposes adding astatine to a solution of a chloride, "
                "bromide and iodide.",
                "Says no displacement in any of them would confirm it is the "
                "least reactive.",
            ]},
    },

    "key_note": "The halogens are coloured, poisonous non-metals that exist "
                "as pairs of atoms. Going down the group they become darker "
                "and change from gas to liquid to solid, and they become less "
                "reactive. A more reactive halogen displaces a less reactive "
                "one from a solution of its salt, which is how their order is "
                "established.",

    "stretch": [
        # ⚑ FLAG 15, CONSTRAINED (R4). Factual and brief. No casualty figures
        # and no physiological effects — and none may be added. The closing
        # sentence is R4's teaching, replacing Design's "Dose is the whole
        # difference"; see the docstring for why that one could not stand.
        {"type": "explainer", "id": "chlorine-both-ways",
         "text": "Chlorine is the reason tap water is safe. Added at about "
                 "one part per million it kills the bacteria that cause "
                 "cholera and typhoid, and the introduction of chlorination "
                 "to city water supplies saved more lives than almost any "
                 "medicine. The same element was released as a weapon in "
                 "1915. <strong>A substance is not good or evil — what is "
                 "done with it is.</strong>"},
        {"type": "explainer", "id": "fluorine-and-its-compounds",
         "text": "Fluorine is so reactive that isolating it killed or injured "
                 "several chemists before Henri Moissan managed it in 1886, "
                 "and it still has to be handled in vessels that have been "
                 "deliberately coated with their own fluoride. Yet its "
                 "compounds are the tamest things imaginable: fluoride in "
                 "toothpaste, and PTFE — a chain of carbon wrapped in "
                 "fluorine — as the coating on a non-stick pan. An element "
                 "and its compounds are different substances, and this group "
                 "proves it four times over."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "Halogen",
         "definition": "One of the group 7 elements — a coloured, poisonous "
                       "non-metal that reacts with metals to make a salt.",
         "note": "The name means salt-maker."},
        {"term": "Displacement",
         "definition": "A reaction in which a more reactive element pushes a "
                       "less reactive one out of its compound.",
         "note": "Never the other way round, which is what makes it an "
                 "order."},
        {"term": "Halide",
         "definition": "The compound a halogen makes with a metal — a "
                       "chloride, a bromide or an iodide.",
         "note": "The colourless solutions in every tube on the grid."},
        {"term": "Antiseptic",
         "definition": "A substance that kills bacteria on skin or on a "
                       "wound.",
         "note": "Iodine is mild enough to be one. Fluorine is not."},
        {"term": "Trend",
         "definition": "A change that runs steadily in one direction down a "
                       "group.",
         "note": "Group 1 rises going down. Group 7 falls. Same reason."},
    ],

    "safety_note": "Chlorine, bromine and iodine are all toxic and their "
                   "vapours are harmful. The nine tubes on this page are a "
                   "simulation of a demonstration done in a fume cupboard, "
                   "and the halogen solutions are handled by the teacher. "
                   "Bromine water in particular burns skin.",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why this group runs the other way?",
              "cta": "Ask about this lesson",
              "anchor": "s-grid"},

    "ks4_becomes": "Explaining both trends with atomic radius and shielding, "
                   "displacement as electron transfer, and writing ionic "
                   "half-equations for the halogens.",

    "ws": ["analysis-and-evaluation", "experimental-skills-and-investigations"],
    "review_state": "draft",
}
