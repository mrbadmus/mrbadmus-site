"""C4 L1 — Chemical change vs physical change (CONTRAST).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c4/c4-01-chemical-vs-physical-change.dc.html`
(704 lines), and her author's notes `docs/ks3/design-reference/c4/NOTES-C4.md`
§1, §2, §3, §5 flags 1–5 and §6 (`REACT-01`, `REACT-02`).

Every student-facing string is byte-identical to the approved page except
where a change is marked ⚑ below and reported to the commander. `RAIL`,
`PAIRS`, `CHAIN_A`, `CHAIN_B`, `RUNGS` and `SELF_RUNGS` came out of the node
extractor; the hook options and reveal, the two definition paragraphs, the
pairs block's eyebrow / heading / prompt / close, the two reference columns,
the chain block's labels and its two notes and its model sentence, the key
fact, the `#s-think` options and its two reveal paragraphs, the key note and
both "Going further" paragraphs were lifted from `lessonVals(s)` and from the
markup, which is where most of this lesson's words live and where a lift of
the top-level constants alone loses them.

── THE CONTRAST IS THE INSTRUMENT, AND THE PAIRING IS THE ARGUMENT ─────

NOTES §2: three pairs, each chosen so the *visible* clue appears on BOTH
sides. That is the whole lesson — the clue never decides it, the new
substance does — so `_PAIRS` below is authored as three pairs of two, never
as six independent cards, and `r_change_pairs` draws them that way. Six
commitments, each final, each opening its own evidence and its own verdict.

⚠️ NOTHING IN THE INSTRUMENT MARKS. `chemical: True/False` is in the payload
because it is Design's own classification of each side, and it is emitted
NOWHERE — no `data-correct`, no green, no red. The verdict panel says in
words what happened whichever button was pressed, and only the mastery ladder
marks correctness. Six sides therefore carry the answer in `verdict` (the
sentence a student reads afterwards) and in nothing a student could see
before committing.

── The chain builder is the CONTRAST family's linked-comparison step ────

NOTES §2 again: it is "the one place in the unit where the model answer is
shown in full". Two slots of three clauses, every combination legal, and the
note that follows branches on whether the two halves are *linked* rather than
on whether they are true — Design's own `chainNote`, both branches lifted.
The full-marks sentence is `_CHAIN_MODEL`, one Python object, so the sentence
in the reveal and the ideal clause pair below it cannot drift apart.

⚑ For Mide's science gate — the five NOTES §5 flags, and what was done:

  * flag 1 — the fried-egg hook. RULED ACCEPTED at KS3, with the condition
    that the justification argues from NEW SUBSTANCES and never from "you
    cannot get the raw egg back". Design's reveal argued from both: it named
    the new substance and then added ", and there is nothing you can do to
    the pan to get the old one back". That clause is `REACT-01` — the exact
    belief this lesson exists to break — stated in the lesson's own voice two
    sentences before the same paragraph demotes reversibility to a clue, so
    it was a lesson body retracted by a later sentence (MRB-225). The clause
    is RE-AUTHORED to argue from properties; nothing else in the hook moved
    and the example is still the egg, not toast.
  * flag 1, second half — the hook's HEADLINE ("…Fry an egg and nothing
    brings it back") is KEPT. It is the elicitation, not the justification:
    hook option C is "Whether the change can be undone", and a headline that
    did not lead with reversibility would elicit nothing for `#s-think` to
    confront. It states two true observations and claims neither is the test.
  * flag 2 — rust reversed in a steelworks. CONFIRMED TRUE and KEPT in all
    three places it appears (pair 3's evidence, the `#s-think` reveal, rung
    1's first correction). Each names a steelworks, a furnace or carbon, and
    pair 3's opens "Not by cooling or drying", so none can be read as a
    bench-scale reversal. Unchanged.
  * flag 3 — steel and brass as mixtures. Not present on this page; nothing
    to keep or change here.
  * flag 4 — whipped cream and butter, in `stretch`. Design wrote "whipping
    it too far is not [physical], which is how you end up with butter", which
    says butter-making is a reaction. It is not: the fat droplets coalesce
    and no new substance is made. RE-AUTHORED. The paragraph keeps its job —
    a change that looks dramatic and is not — which is a better example for
    this lesson than the boundary flip Design intended.
  * flag 5 — "the atoms are all still there" in burning wax. CONFIRMED and
    KEPT byte-identical. The sentence says the candle LOSES mass and that the
    PRODUCTS outweigh the wax because oxygen joined in, so it cannot be read
    as the wax getting heavier.

⚑ And one correction of the author's own, under the contract's §18:

  * PAIR 2 WAS LABELLED "both fizz, both feel like something happening" AND
    ONLY ONE SIDE FIZZES. Salt stirred into water does not fizz — Design's
    own `what` for that side says the crystals disappear and the water stays
    clear. The label therefore claimed a shared clue the pair does not show,
    on the one pair whose shared clue IS the misconception (`REACT-02`: a
    solid vanishing into a liquid). The label is re-authored to name what the
    two sides actually share, and the closing panel's matching clause with
    it. The other two pairs' shared clues — heat twice, colour twice — are
    true as drawn and are untouched.

    The big question and the key note both named bubbling as a clue that
    appears on both sides of the line, and the commander SPLIT them (MRB-246):

      · THE BIG QUESTION IS CHANGED. It is a promise about the six changes
        immediately ahead — "two changes can look identical, same X, same Y" —
        and after the pair-2 correction there is no bubbling pair for it to be
        pointing at. It now names the three clues the instrument's own close
        panel measures: heat twice, a solid vanishing twice, colour twice.
      · THE KEY NOTE IS KEPT. It generalises PAST the six, and its claim is
        true in the world: a fizzy drink bubbles and makes nothing new, marble
        in acid bubbles and does. A key note narrowed to only the evidence on
        its own page would be a smaller and no truer sentence.

    The two are not in conflict. One says what this lesson is about to show;
    the other says what the lesson means once it has.

⚑ And one distractor set the commander re-authored, under MRB-177:

  * `#s-think`'s four options ran 7, 18, 6 and 12 words, with the CORRECT one
    the longest by six. It is unmarked and carries no `answer`, so the length
    gate skips it — which makes it worse, not safer. This is the activity that
    ELICITS `REACT-01`, and a visibly-longest right answer means the student
    never commits to the wrong idea at all. An unelicited misconception is
    invisible to its owner (Law 4), so the tell costs the lesson its whole
    mechanism rather than costing one mark. Fixed AT THE DISTRACTORS, as wrong
    rules in the correct option's shape; index 1 is Design's and unmoved.
"""

# ── the three pairs (NOTES §2) ──────────────────────────────────────────
#
# Design's `PAIRS`, out of the extractor. `chemical` is her classification of
# each side and is DELIBERATELY NOT RENDERED — see the docstring. `evidence`
# is three tests in her order, and the order is the argument: does it come
# back, has it new properties, what happened to the mass. `verdict` and `why`
# are the ink panel a decided card opens.
_PAIRS = [
    {"id": "p1",
     "label": "Pair 1 · both involve a candle and a flame",
     "sides": [
         {"id": "wax-melt",
          "name": "Wax melting",
          "what": "The wax near the flame turns to a clear liquid and runs "
                  "down the side.",
          "chemical": False,
          "evidence": [
              {"test": "Does it come back?",
               "result": "It sets again as it cools, into wax."},
              {"test": "New properties?",
               "result": "Liquid wax and solid wax burn the same way, smell "
                         "the same and weigh the same."},
              {"test": "Mass",
               "result": "The wax that ran down weighs what it weighed "
                         "before."},
          ],
          "verdict": "Physical change.",
          "why": "A change of state. Same substance, different arrangement "
                 "of the same particles."},
         # ⚑ Science flag 5 lives in this side's `Mass` line and is KEPT
         # WHOLE. It says the candle LOSES mass, and that the PRODUCTS —
         # not the wax — weigh more, because oxygen joined in. Shortening
         # it to "the mass goes up" would be the famous version and the
         # false one.
         {"id": "wax-burn",
          "name": "Wax burning",
          "what": "The wick burns with a yellow flame and the candle gets "
                  "shorter.",
          "chemical": True,
          "evidence": [
              {"test": "Does it come back?",
               "result": "Nothing you can do to the air above the candle "
                         "turns it back into wax."},
              {"test": "New properties?",
               "result": "Carbon dioxide and water vapour come off. Neither "
                         "is waxy, neither burns."},
              {"test": "Mass",
               "result": "The candle loses mass — and the products, if you "
                         "could weigh them all, weigh more than the wax did, "
                         "because oxygen joined in."},
          ],
          "verdict": "Chemical change.",
          "why": "The wax has been turned into different substances. The "
                 "atoms are all still there, joined up differently."},
     ]},
    # ⚑ RE-AUTHORED LABEL. Design's read "Pair 2 · both fizz, both feel like
    # something happening", and salt stirred into water does not fizz — her
    # own `what` for that side says the water stays clear. What these two
    # sides really share is a solid vanishing into a liquid, which is
    # `REACT-02` exactly, so the label now names it. See the docstring.
    {"id": "p2",
     "label": "Pair 2 · both make a solid vanish into a liquid",
     "sides": [
         {"id": "salt",
          "name": "Salt stirred into water",
          "what": "The crystals disappear and the water stays clear.",
          "chemical": False,
          "evidence": [
              {"test": "Does it come back?",
               "result": "Evaporate the water and the salt is back, to the "
                         "gram."},
              # SYS-7 — this evidence line credited tasting a beaker one
              # card away from marble chips in acid. The claim it makes is
              # "no new properties", and it can make that claim without
              # asking anyone to taste anything.
              {"test": "New properties?",
               "result": "None that are new. The salt is still salt — it "
                         "just cannot be seen while it is dissolved."},
              {"test": "Mass",
               "result": "Unchanged. 100 g of water plus 10 g of salt weighs "
                         "110 g."},
          ],
          "verdict": "Physical change.",
          "why": "Dissolving is mixing at the particle scale. Nothing new "
                 "was made — which is exactly why you could get it back."},
         {"id": "marble",
          "name": "Marble chips in acid",
          "what": "The chips fizz vigorously and slowly disappear.",
          "chemical": True,
          "evidence": [
              {"test": "Does it come back?",
               "result": "Evaporate the liquid and you get a different white "
                         "solid, not marble chips."},
              {"test": "New properties?",
               "result": "The gas given off puts out a lit splint and turns "
                         "limewater cloudy. Marble does neither."},
              {"test": "Mass",
               "result": "The open flask gets lighter, because the gas "
                         "leaves. Seal it and the mass does not change at "
                         "all."},
          ],
          "verdict": "Chemical change.",
          "why": "Marble and acid have become a gas, a salt and water. \"It "
                 "dissolved\" is the same phrase describing a completely "
                 "different event."},
     ]},
    {"id": "p3",
     "label": "Pair 3 · both change colour, both take time",
     "sides": [
         {"id": "ice",
          "name": "Ice left in a warm room",
          "what": "The clear block goes cloudy at the edges and becomes a "
                  "puddle.",
          "chemical": False,
          "evidence": [
              {"test": "Does it come back?",
               "result": "Put the puddle in the freezer and you have ice "
                         "again."},
              {"test": "New properties?",
               "result": "Ice and water are the same substance. Both are "
                         "water."},
              {"test": "Mass",
               "result": "The puddle weighs what the block weighed."},
          ],
          "verdict": "Physical change.",
          "why": "Melting. The particles have not changed at all — they "
                 "have only broken out of a fixed arrangement."},
         # ⚑ Science flag 2, site 1 of 3. "A steelworks … with a furnace and
         # carbon", after "Not by cooling or drying" — industrial plant,
         # named, and no bench-scale reading available.
         {"id": "rust",
          "name": "An iron nail left outside",
          "what": "The grey nail turns orange-brown and flakes.",
          "chemical": True,
          "evidence": [
              {"test": "Does it come back?",
               "result": "Not by cooling or drying. A steelworks can get "
                         "iron back from rust, with a furnace and carbon."},
              {"test": "New properties?",
               "result": "Rust is soft, crumbly and not magnetic in the way "
                         "iron is. Iron is strong and grey."},
              {"test": "Mass",
               "result": "The nail gets heavier. The extra mass came out of "
                         "the air."},
          ],
          "verdict": "Chemical change.",
          "why": "Iron and oxygen have become iron oxide, a new substance "
                 "with new properties — including being useless as a nail."},
     ]},
]

# ── the chain builder's clauses (Design's CHAIN_A / CHAIN_B) ────────────
#
# Index 0 of each is the clause that earns the marks, and the two of them
# concatenated ARE `_CHAIN_MODEL` below — which is why the model sentence is
# built from these two strings rather than typed a second time. A future edit
# to either clause moves the model answer with it, and cannot leave the page
# showing a full-marks sentence the student was never offered.
_CHAIN_A = [
    "Melting wax is a physical change because the wax is still wax and cools "
    "back to a solid,",
    "Melting wax is a physical change because it can be undone,",
    "Melting wax turns a solid into a liquid,",
]
_CHAIN_B = [
    "whereas burning wax is a chemical change because the wax is turned into "
    "carbon dioxide and water, which cannot be turned back into wax by "
    "cooling.",
    "and burning wax is a chemical change.",
    "but burning wax gives off heat and light.",
]
_CHAIN_MODEL = "%s %s" % (_CHAIN_A[0], _CHAIN_B[0])

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 208 character for character.
    "slug":        "chemical-vs-physical-change",
    "title":       "Chemical change vs physical change",
    "discipline":  "chemistry",
    "unit":        "chemical-reactions",
    "family":      "CONTRAST",

    # ── curriculum position ─────────────────────────────────────────────────
    # NOTES §1 gives this lesson the "what counts" half of `KS3.C.CR.01`. The
    # clause is minted in `ks3_data/substatements.py` (the commander's file)
    # with the reasoning: a student who meets "what counts as a reaction" and
    # "a reaction is a rearrangement" in one sitting never has `REACT-01`
    # elicited at all, so the recognition half is taught first and taught
    # wrong-first. This lesson is clause `a`.
    "covers":      ["KS3.C.CR.01a"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 3},
                    {"id": "particles", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # The page's "Before this lesson" card links to c3-07. Pair 2 also leans
    # on dissolving meaning something already, which is c3-02's job.
    "requires":    ["proving-something-is-pure"],
    "assumes":     [],
    "references":  ["dissolving-and-solutions"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    # ⊕ THE PROMISE NAMES WHAT THE PAGE ACTUALLY PAIRS (MRB-246).
    # Design wrote "same bubbling, same colour, same heat". Bubbling is
    # not one of the three shared clues the instrument delivers — its own
    # close panel measures heat twice, a solid vanishing twice and colour
    # twice — so the opening promised a pair the lesson never shows. §6:
    # the instrument is the measurement and the prose changes.
    #
    # ⚠️ The KEY NOTE still says "Bubbling" and that is correct, not an
    # inconsistency. This sentence is a promise about the six changes
    # ahead; the key note is a generalisation past them, and its own
    # comment says so. A fizzy drink bubbles and makes nothing new.
    "big_question": "Two changes can look identical — the same heat, the "
                    "same colour change, the same disappearing solid — and "
                    "only one of them makes something new. Which question "
                    "separates them every time?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, Design's `RAIL`, in her order with her ids and her short
    # labels. `done_when` restates her own `DONE()`: the hook on a
    # commitment, the pairs when all six verdicts are in, the chain when both
    # halves are picked, `#s-think` on a commitment, the ladder when every
    # rung is answered and both self-marked rungs checked.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Chocolate and egg", "done_when": "committed"},
        {"anchor": "s-pairs",  "short": "PAIRS",
         "label": "Three pairs", "done_when": "all_six_decided"},
        {"anchor": "s-chain",  "short": "SENTENCE",
         "label": "One sentence", "done_when": "both_halves_chosen"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Undo it", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚑ SCIENCE FLAG 1. The reveal's second sentence used to end ", and there
    # is nothing you can do to the pan to get the old one back" — a
    # justification from irreversibility, in a lesson whose whole job is to
    # break that rule, two sentences before the same paragraph calls
    # reversibility a clue. Re-authored to argue from properties. The rest of
    # the reveal, including the closing "Everything else … is a clue. This is
    # the question", is byte-identical.
    "phenomenon": {
        "kind": "narrative",
        "title": "Melt a chocolate bar and it comes back. Fry an egg and "
                 "nothing brings it back.",
        "prompt": "Both changes were caused by heat. Both changed how the "
                  "thing looked, felt and poured. In one of them you still "
                  "have chocolate. In the other you no longer have egg white "
                  "— you have something else that happens to be sitting "
                  "where the egg white was.",
        "commit": "What is the difference that actually matters?",
        "options": [
            "How much heat was used",
            "Whether a new substance was made",
            "Whether the change can be undone",
            "Whether the thing changed colour",
        ],
        "reveal": "Whether a <strong>new substance</strong> was made. Melted "
                  "chocolate is chocolate — same substance, different state. "
                  "Fried egg is not egg white with the temperature turned "
                  "up; it is a different substance with different properties "
                  "— firm where the old one was runny, white where it was "
                  "clear. Everything else — the colour, the smell, the "
                  "bubbling, whether it can be undone — is a clue. This is "
                  "the question.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ BOTH JOINS RESOLVE AGAINST THIS PAGE'S OWN MARKUP (MRB-244/248), and
    # the universe of legal names is exactly `id="…"` and `data-activity="…"`.
    #
    # `REACT-01`'s `statement` is the line the PAGE quotes, not the register's
    # shorter handle — `r_confrontation` prints `statement` as the `#s-think`
    # quote, and Design's line is the one that must render.
    #
    # ⊖ NOTES §6 proposes `think-reveal-glass` as REACT-01's confrontation
    # site. NO SUCH ID CAN BE EMITTED FROM A LANE: the `#s-think` reveal panel
    # is drawn by `build_ks3.py`'s shared `r_activity`, which emits
    # `<div class="ks3-reveal" hidden data-reveal>` and no id, and
    # `build_ks3.py` is not a file this lane may touch. The confronting
    # paragraphs are INSIDE the activity whose `data-activity` is
    # `think-commit-reverse`, so that is what the join names — the same
    # reconciliation c3-03 made for `MIX-06`, and it is also what satisfies
    # Law 3, which requires at least one `confronted_by` to be a real
    # ACTIVITY id.
    "misconceptions": [
        {"id": "REACT-01",
         "statement": "If you can undo it, it is physical. If you cannot "
                      "undo it, it is chemical.",
         "elicited_by": "think-commit-reverse",
         "confronted_by": "think-commit-reverse"},
        # ⊖ NOTES §6 proposes `pair-2-reveal`. `r_change_pairs` emits one
        # reveal PER SIDE — Design draws them inside the two cards, not once
        # per pair — so the id is qualified by the side that does the
        # confronting. The marble card is the one that takes the belief
        # apart: its verdict panel is where "it dissolved" is shown to be one
        # phrase describing two different events.
        {"id": "REACT-02",
         "statement": "Something disappearing into a liquid is always the "
                      "same kind of change.",
         "elicited_by": "pair-2-commit",
         "confronted_by": "pair-2-reveal-marble"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Page lines 105–107 — the two definitions the rest of the lesson
        # uses. Two paragraphs, so two blocks: `r_explainer` draws one <p>.
        {"type": "explainer",
         "text": "In a <strong>physical change</strong>, the same substances "
                 "are still there. They have moved, changed state, or mixed "
                 "— and the particles themselves are untouched."},
        {"type": "explainer",
         "text": "In a <strong>chemical change</strong> — a <strong>chemical "
                 "reaction</strong> — at least one new substance is made. "
                 "The atoms are all still there, but they have been joined "
                 "up differently, and what you have now behaves differently "
                 "from what you started with."},

        # #s-pairs — the flagship. Light `ks3-block` → `check`.
        #
        # ⚑ The prompt's last clause read "Then buy the evidence and see
        # which of your two verdicts survives." There is no cost and no
        # budget in this instrument — that is C2's test-budget mechanic, and
        # §5A forbids narrating a control that is not modelled. One word
        # changed, "buy" to "read", so the sentence describes what the
        # instrument actually does.
        {"type": "change-pairs", "id": "pairs-three", "anchor": "s-pairs",
         "eyebrow": "Your turn · three pairs, side by side",
         "heading": "Each pair looks alike. In each pair, one is a reaction "
                    "and one is not.",
         "demand": "investigate",
         "prompt": "Commit on both halves of a pair before you run any tests "
                   "on it. Then read the evidence and see which of your two "
                   "verdicts survives.",
         "options": ["Physical", "Chemical"],
         "pairs": _PAIRS,
         # ⚑ RE-AUTHORED FIRST CLAUSE, and only the first. Design's read
         # "Bubbles appeared in two of them and only one was a reaction",
         # which the six changes do not show — only the marble fizzes. The
         # clause now names the clue pair 2 really does show on both sides.
         # Heat twice and colour twice are true as drawn and are untouched.
         "close": "Six changes. A solid vanished into a liquid in two of "
                  "them and only one was a reaction. Something got hot in "
                  "two of them and only one was a reaction. Colour changed "
                  "in two and only one was a reaction. <strong>Every clue "
                  "you can see appears on both sides of the "
                  "line.</strong> The only question that sorted all six was "
                  "whether the substance you ended with was a different "
                  "substance."},

        {"type": "key-fact", "ref": "new-substance-or-not"},

        # The reference block. Design draws two panels of four bullets each,
        # and the bullets PAIR — new substance, particles, reversing it,
        # where you meet it — so this is `comparison`, §5.1.1's CONTRAST
        # spine, rather than two explainers that leave the reader to align
        # them. ⚑ The four row NAMES are new prose; every cell is Design's,
        # byte-identical.
        {"type": "comparison",
         "eyebrow": "Reference · the two columns",
         "statement": "What each kind of change does and does not do",
         "ground": "band",
         "columns": [{"caption": "Physical change"},
                     {"caption": "Chemical change"}],
         # Neither column is the quiet one — that is the argument of a
         # CONTRAST panel, and the reason both tones are `ink`.
         "row_tones": ["ink", "ink"],
         "rows": [
             {"name": "New substances",
              "cells": ["No new substance.",
                        "At least one new substance, with different "
                        "properties."]},
             {"name": "The particles",
              "cells": ["The particles are unchanged — only their "
                        "arrangement or spacing.",
                        "The atoms are the same atoms, joined up "
                        "differently."]},
             {"name": "Reversing it",
              "cells": ["Usually easy to reverse, and the same mass comes "
                        "back.",
                        "Usually hard to reverse, and never by cooling it "
                        "down."]},
             {"name": "Where you meet it",
              "cells": ["Melting, boiling, dissolving, breaking, mixing.",
                        "Burning, rusting, cooking, acid on marble, "
                        "respiration."]},
         ]},

        # #s-chain — the linked-comparison step. Light `ks3-block` → `check`.
        {"type": "chain-build", "id": "chain-wax", "anchor": "s-chain",
         "eyebrow": "Say it as one sentence",
         "heading": "Build the comparison, not two descriptions",
         "demand": "construct",
         "prompt": "Melting wax and burning wax. Pick one clause for each "
                   "half — then read what a linked comparison has to do that "
                   "two separate statements do not.",
         "slots": [
             {"id": "a", "label": "First half", "options": _CHAIN_A},
             {"id": "b", "label": "Second half", "options": _CHAIN_B},
         ],
         # The clause pair that earns the marks. Read by the renderer to
         # choose which of the two notes below is shown, and NEVER used to
         # mark a control: no option in this instrument takes a tick, a
         # cross, green or red, and both notes open the same panel.
         "ideal": {"a": 0, "b": 0},
         "sentence_label": "Your sentence",
         "notes": {
             "ideal": "That is the sentence. Both halves name the change, "
                      "both give the reason, and the second half answers the "
                      "first — the wax is still wax against the wax is now "
                      "something else. An examiner is looking for the link, "
                      "and \"whereas\" is where it lives.",
             "other": "Every clause you could pick is true. What decides the "
                      "marks is whether the two halves are about the same "
                      "thing: a comparison has to say what is different, not "
                      "describe two changes and leave the reader to spot it. "
                      "\"It can be undone\" and \"it gives off heat and "
                      "light\" are both true and neither is the difference — "
                      "one is a consequence and the other happens in "
                      "physical changes too.",
         },
         "model_label": "A sentence that would get full marks",
         "model": _CHAIN_MODEL},

        {"type": "misconception", "id": "think-commit-reverse",
         "anchor": "s-think", "targets": "REACT-01"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # None. Design draws no diagram on this page — the instrument IS the
    # picture, six cards of words either side of a line — and §5.4 allows an
    # empty list where it does not allow an absent one.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "new-substance-or-not",
         "text": "A chemical change makes at least one new substance. A "
                 "physical change does not — the same substances are still "
                 "there, in a different state or a different place.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # `#s-think` only. The two instrument blocks are lifted out of `core` into
    # this list by `_normalise()` and are never authored here.
    "activities": [
        # ⚑ Science flag 2, sites 2 and 3, both KEPT byte-identical: the
        # steelworks is named, and so is the ore it works on. Nothing here
        # can be read as reversing rust on a bench.
        {"id": "think-commit-reverse",
         "kind": "predict",
         "demand": "explain",
         "targets": "REACT-01",
         "prompt": "This rule gets the right answer most of the time, which "
                   "is exactly what makes it dangerous. Commit before you "
                   "read on.",
         "options": [
             # ⚠️ MRB-246 — these three were 7, 6 and 12 words against a
             # correct option of 18: the strongest length tell in the
             # unit, sitting on the one activity whose JOB is to make a
             # student commit to REACT-01. A visibly-longest right answer
             # does not merely leak a mark here — it stops the wrong idea
             # being committed to at all, and an unelicited misconception
             # is invisible to its owner (Law 4). So this set matters MORE
             # than a marked one, not less, and the gate cannot see it:
             # an option set with no `answer` key is skipped.
             #
             # Re-authored AT THE DISTRACTOR, as wrong RULES in the
             # correct option's own shape. Index 1 is Design's, unchanged,
             # and still index 1.
             "A good rule — if you cannot get the starting substances "
             "back, something new has been made",
             "Not the test — smashing glass is irreversible and physical, "
             "and rust can be turned back into iron",
             "A good rule for solids — a solid that cannot be put back "
             "together has reacted",
             "Wrong the other way round — chemical changes are the "
             "reversible ones and physical changes are the permanent ones",
         ],
         "reveal": [
             "Smash a glass and you cannot undo it — and no new substance "
             "was made, so it is a physical change. It is broken glass, "
             "which is glass. Meanwhile a rusty nail can be turned back into "
             "iron: a steelworks does exactly that to iron ore, which is "
             "mostly rust, and rusting is unquestionably a chemical change.",
             "Reversibility is about <strong>how hard</strong> the change is "
             "to undo, and that is a fact about energy and equipment, not "
             "about what happened to the substances. It is a useful hint and "
             "it is not the test. <strong>Ask what you have now, not whether "
             "you can get back.</strong>",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Design's RUNGS → recall + apply, SELF_RUNGS → explain + produce. Her
    # rung labels are the engine's own defaults character for character
    # ("Recall", "The one that catches people", "Explain", "Take it somewhere
    # new"), so no rung authors a `title`. `feedback` is keyed by the INT
    # index of each wrong option, which is what `_rung_marked` reads.
    "ladder": {
        # ⚑ MRB-177 — THE THREE DISTRACTORS ARE RE-AUTHORED AND THE CORRECT
        # OPTION IS UNTOUCHED. Design's set was "At least one new substance
        # has been made" (8 words) against "It cannot be reversed" (4), "The
        # colour has changed" (4) and "Heat was involved" (3): the correct
        # answer strictly the longest and clear of the field by 4 words, which
        # is exactly the construct §13 measures — a rule needs three parts, a
        # wrong reason needs one, so the answer is longer BY CONSTRUCTION.
        # The fix is at the distractor, as ruled: each now states a WRONG RULE
        # in the correct answer's own shape and at its own length (8, 7, 7
        # against 8). Every correction below is Design's, unchanged, and each
        # still answers the option it is attached to.
        "recall": {
            "q": "What single thing tells you that a change is a chemical "
                 "change?",
            "options": [
                "The change cannot be reversed by any means",
                "The colour of the substance has changed",
                "At least one new substance has been made",
                "Heat was needed to make it happen",
            ],
            "answer": 2,
            "feedback": {
                0: "Smashing a glass cannot be reversed and is physical; "
                   "rusting can be reversed in a furnace and is chemical.",
                1: "Ice going cloudy and a nail going orange both change "
                   "colour, and only one of them is a reaction.",
                3: "Melting needs heat and makes nothing new. Rusting needs "
                   "no heat at all.",
            }},
        # The one that catches people, and it is `REACT-02` at the ladder:
        # two events described with one phrase. The correct option is the
        # SHORTEST here, which is Design's construction and is not a tell in
        # the direction MRB-177 measures — the two four-word options are the
        # two verdict pairs, and a student choosing by length has a 50/50.
        "apply": {
            "q": "Salt dissolving in water and marble fizzing in acid are "
                 "both described as \"it dissolved\". Which pair of verdicts "
                 "is right?",
            "options": [
                "Both physical — in both cases the solid disappears into the "
                "liquid",
                "Both chemical — the solid is destroyed in both",
                "Salt: physical. Marble: chemical.",
                "Salt: chemical. Marble: physical.",
            ],
            "answer": 2,
            "feedback": {
                0: "The marble has become a gas, a salt and water, and the "
                   "gas can be tested. Something disappearing is not "
                   "evidence of anything.",
                1: "The salt is not destroyed. Evaporate the water and every "
                   "gram of it comes back unchanged.",
                3: "Exactly the wrong way round. Test the gas from the "
                   "marble: it turns limewater cloudy, so it is a new "
                   "substance.",
            }},
        "explain": {
            "q": "A student heats sugar in a pan. First it melts to a clear "
                 "syrup; then it turns brown, smells of caramel and sets "
                 "hard. They say \"the whole thing was one change\". Explain "
                 "how many changes happened, which kind each was, and what "
                 "evidence separates them.",
            "field_label": "Your explanation",
            "placeholder": "There were two changes. The first…",
            "success": [
                "Says there were two changes, not one.",
                "Says melting is a physical change — still sugar, and it "
                "would set back to sugar on cooling.",
                "Says the browning is a chemical change, because new "
                "substances with new properties were made.",
                "Uses evidence for the second: the new smell, the new "
                "colour, and that cooling does not bring the sugar back.",
                "Makes the comparison linked, not two separate descriptions "
                "— for example using \"whereas\".",
            ]},
        "produce": {
            "q": "A cook says \"cooking is just heating food up\". Take two "
                 "examples from a kitchen — one physical change and one "
                 "chemical — and use them to explain why that sentence is "
                 "wrong, and why it is easy to believe.",
            "field_label": "Your answer",
            "placeholder": "Boiling a potato is mostly…",
            "success": [
                "Names a kitchen change that is physical, and says why no "
                "new substance is made.",
                "Names a kitchen change that is chemical, and names or "
                "describes a new substance.",
                "Uses the new-substance test explicitly as the thing that "
                "distinguishes them.",
                "Explains why the sentence is tempting — heat is involved in "
                "both, and both look dramatic.",
                "Notes that one of them can be undone and the other cannot, "
                "and that this is a consequence rather than the definition.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # Byte-identical. "Bubbling" here is a claim about clues in the world, not
    # about the six changes above — a fizzy drink bubbles and makes nothing
    # new, marble in acid bubbles and does. See the docstring.
    "key_note": "A chemical change makes at least one new substance, with "
                "properties the starting materials did not have. A physical "
                "change makes none — the same substances are still there, "
                "melted, dissolved, broken or moved. Bubbling, colour "
                "change, heat and irreversibility are clues that appear on "
                "both sides of the line, so none of them is the test. The "
                "test is: what have you got now?",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ Science flag 4 is in the second paragraph. Design wrote "Whipping
    # cream is physical, and whipping it too far is not, which is how you end
    # up with butter", which makes butter-making a reaction. It is not — the
    # fat droplets coalesce and no new substance is made — so the clause is
    # re-authored. The paragraph keeps its work and gains a better example
    # for this lesson than the one it lost: a change that looks dramatic,
    # smells different and pours differently, and is still physical.
    "stretch": [
        {"type": "explainer", "id": "boundary-cases",
         "text": "Some changes are genuinely awkward to place, and that is "
                 "not a flaw in the definition — it is what happens at a "
                 "boundary. Dissolving salt in water is physical: the salt "
                 "is still there and evaporating gets it back. Dissolving "
                 "marble chips in acid is chemical: the marble is gone, "
                 "replaced by a gas, a salt and water. Both are described in "
                 "everyday speech as \"it dissolved\", and the word is doing "
                 "two completely different jobs."},
        {"type": "explainer", "id": "cooking",
         "text": "Cooking is the case worth arguing about. Boiling a potato "
                 "is mostly physical — heat and water soften it. Browning a "
                 "steak is chemical: hundreds of new substances form between "
                 "the amino acids and sugars on the surface, which is why it "
                 "smells of something the raw meat did not. Whipping cream "
                 "is physical, and so is whipping it too far: the fat "
                 "droplets clump together into butter, and nothing new has "
                 "been made. The same pan can host both kinds of change in "
                 "the same minute."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    # Every technical term the lesson introduces, glossed at the reading age
    # the lesson is written for.
    "vocabulary": [
        {"term": "substance",
         "definition": "One material, with its own properties — water, iron, "
                  "salt. Two different substances behave differently."},
        {"term": "property",
         "definition": "Something you can find out about a substance by testing "
                  "it: its colour, whether it burns, whether a magnet pulls "
                  "it."},
        {"term": "physical change",
         "definition": "A change that makes no new substance. The same stuff is "
                  "still there, melted, dissolved, broken or moved."},
        {"term": "chemical change",
         "definition": "A change that makes at least one new substance, with "
                  "properties the starting materials did not have."},
        {"term": "chemical reaction",
         "definition": "Another name for a chemical change. The atoms are all "
                  "still there and have been joined up differently."},
        {"term": "reversible",
         "definition": "Able to be turned back. It is a clue about how much "
                  "energy and equipment a change would take to undo, and it "
                  "is not what decides whether a change is chemical."},
    ],

    # ⊖ NO `safety_note`, and the decision is deliberate rather than an
    # omission. This page gives no method and asks for nothing to be done at
    # a bench: the acid, the candle and the pan are all described, never
    # carried out.
    #
    # ⊕ 28 Aug 2026 (MRB-295, SYS-7). This note used to continue: "The one
    # line that could invite an action is pair 2's 'The solution still tastes
    # of salt', and a blanket never-taste line would retract the evidence the
    # page uses to prove the salt is still salt — which is the
    # self-retraction §7 forbids. Reported to the commander rather than added
    # silently." It was reported, it was ruled, and it is resolved from the
    # other end: pair 2 no longer credits tasting, so there is no longer a
    # line inviting the action, and STILL no safety_note is needed. No safety
    # wording was written here — the ruling was to remove the invitation, not
    # to add a warning.

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why irreversible is not the same as "
                      "chemical?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Reaction profiles, bond breaking and bond making, and "
                   "why a chemical change involves an energy change every "
                   "time.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
