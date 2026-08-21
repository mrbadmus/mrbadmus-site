"""B2 L2 — Joints (MODEL).

Authored against Design's approved page,
`docs/ks3/design-reference/b2/b2-02-joints.dc.html` (896 lines), and its
measured specification, `docs/ks3/b2-inventory/PAYLOAD-MAP.md` §2.

MODEL's spine, applied: build the model on the bench, then take it to four real
places in the body — and the fourth (the base of the thumb) **is none of the
four types**. The closing line is that a model which fits everything has
stopped telling you anything.

Every student-facing string is byte-identical to the approved page. `JOINTS`,
`CASES`, `RUNGS`, `SELF_RUNGS` and `RAIL` were lifted with
`tools/extract_design_payload.js`; the hook options, the bench gate's four
options, the twist button's two labels, the idle twist note and the three tile
captions were lifted from the line ranges §2.2 records, because they live
inside `renderVals()` and no constant holds them.

⚑ **Statutory ownership.** This lesson owns `KS3.B.SKEL.01b`, a clause minted
for B2 — see `ks3_data/biology_b2_movement.py`. Design's NOTES §1 says this
lesson "has no statement of its own"; §10.2 says every authored lesson must
have one. Flagged for Mide, not decided here.

⚠ **NOTES vs PAGE, recorded rather than reconciled.** NOTES §3.2 lists three
bench controls and no gate. The page gates the whole bench behind a four-option
commitment that DISAPPEARS when answered, and that gate is `BODY-05`'s
elicitation. The page wins (MRB-205), so the gate is authored.
"""

# ── the four types, offered against every case ──────────────────────────
# A five-option set with an off-model answer, and it is the family's whole
# point: `k4` answers "None of these." Authored once and shared by all four
# cases, exactly as Design's `CASES` does.
_TYPES = ["Hinge", "Ball and socket", "Pivot", "Fixed", "None of these"]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 72 character for character.
    "slug":        "joints",
    "title":       "Joints",
    "discipline":  "biology",
    "unit":        "movement-skeleton-and-muscles",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    "covers":      ["KS3.B.SKEL.01b"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 50,

    "requires":    ["what-the-skeleton-does"],
    "assumes":     [],
    "references":  ["antagonistic-muscle-pairs"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Shoulders dislocate all the time. Elbows almost never do. "
                    "What is the shoulder buying with that risk?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Page lines 367–373; tick conditions 716–723. `all_joints_tried` is keyed
    # by JOINT ID and is set by a tab click, a slider move OR a twist press —
    # four distinct joints must be touched, by any of the three routes.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "Range or stability",
         "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",  "label": "Drive the joint",
         "done_when": "all_joints_tried"},
        {"anchor": "s-cases",  "short": "CASES",  "label": "Four places",
         "done_when": "all_cases_decided"},
        {"anchor": "s-think",  "short": "THINK",  "label": "Tendon or ligament",
         "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    "phenomenon": {
        "kind": "narrative",
        "title": "The joint that comes apart most is the one that moves best.",
        "prompt": "The shoulder is the most frequently dislocated joint in the "
                  "body. The elbow is one of the least. They are joined by the "
                  "same kind of tissue, in the same arm, in the same person.",
        "commit": "Why is the shoulder the one that gives way?",
        "options": [
            "Shoulder muscles are weaker than elbow muscles",
            "It moves in far more directions, so far more directions can push "
            "it out",
            "People use their shoulders more",
            "The bones there are softer",
        ],
        "reveal": "Every direction a joint can be moved in is a direction it "
                  "cannot hold against. The shoulder can be swung almost "
                  "anywhere, which is exactly why almost anything can push it "
                  "out. The elbow refuses every direction but one, and that "
                  "refusal is what makes it hard to break.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # BODY-04's statement is the PAGE's line (line 227), which the register
    # paraphrases identically here.
    #
    # ⊕ MRB-244 — BODY-06 named "ladder", and the ladder's section is emitted
    # as `s-ladder` (its `anchor`). The belief is genuinely confronted there —
    # only the name was one the document does not carry. `s-ladder` is what a
    # student's browser can reach, so `s-ladder` is what the register says.
    "misconceptions": [
        {"id": "BODY-04",
         "statement": "Muscles hold the bones together at a joint.",
         "elicited_by": "tendon-or-ligament",
         "confronted_by": "tendon-or-ligament"},
        {"id": "BODY-05",
         "statement": "All joints work the same way; some are just stiffer "
                      "than others.",
         "elicited_by": "joint-bench",
         "confronted_by": "joint-bench"},
        {"id": "BODY-06",
         "statement": "A joint could rotate further if the muscles were "
                      "stronger or the ligaments looser.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A joint is a place where two bones meet. Ligaments strap "
                 "them together, and a layer of smooth cartilage keeps the "
                 "ends from grinding. What the joint can do after that is "
                 "decided by one thing: the shape of the two ends."},

        # #s-bench — the flagship, on an INK-DARK `practical` shell (measured:
        # `ks3-block ks3-dark ks3-practical`, page line 115).
        {"type": "joint-bench", "id": "joint-bench", "anchor": "s-bench",
         "eyebrow": "The model · drive the joint",
         "heading": "Four shapes, four sets of rules",
         "head_counter": {"format": "{n} of 4 joints tried", "total": 4},
         "demand": "investigate",
         "targets": "BODY-05",
         "prompt": "Bend each one as far as it goes, then try to twist it. Two "
                   "of them will refuse, and the refusal is the point.",
         # C6's commit gate. It DISAPPEARS when answered and the bench arrives
         # in the space the question was occupying.
         "gate": {
             "prompt": "Commit first. Your knee and your shoulder are both "
                       "joints. How do they compare?",
             "options": [
                 "Both move in one direction only",
                 "The knee moves one way; the shoulder moves in several",
                 "Both move in every direction, but the knee is stiffer",
                 "The knee moves in more directions, because it carries more "
                 "weight",
             ]},
         "labels": {
             "axes": "Directions it moves in",
             "where": "Where you have one",
             "hold": "What holds it together",
             "trade": "The trade:",
             "locked": "locked",
             "twist": "Try to twist it",
             "twisting": "Twisting",
             # The one twist note that is NOT per joint: it is what a joint
             # that CAN twist says while it is not twisting.
             "twist_idle": "Press it and watch what happens.",
         },
         # Composed, never authored as a finished sentence: it quotes three
         # live values and would go stale the moment the slider moved.
         # The starting angle lives ON each joint, not in a map keyed by joint
         # id beside them: a map makes every joint's name a dict key, and a key
         # reached only by iteration is invisible to `ks3_key_audit.py`. The
         # ball joint opens at 40° because a shoulder drawn at 0° reads as a
         # dead arm rather than a joint with range.
         "alt": {
             "template": "A two-bone model of a {name}. The moving bone is set "
                         "at {angle} degrees within a range of 0 to {max} "
                         "degrees, and the joint {twist}",
             "can": "can be turned about its long axis.",
             "cannot": "cannot be turned about its long axis at all.",
         },
         "joints": [
             {"id": "hinge",
              "tab": "Hinge",
              "name": "Hinge joint",
              "bend": [0, 145],
              "start": 20,
              "twist": False,
              "axes": "1",
              "angle_label": "Bend the joint",
              "where": "Elbow, knee, fingers",
              "hold": "Ligaments down both sides",
              "trade": "One direction, and a very strong refusal of every other one. You can hang your whole body weight from a bent elbow and it will not fold sideways.",
              "twist_yes": "",
              "twist_no": "It will not. The end of one bone sits in a groove in the other, and a groove only lets you go one way."},
             {"id": "ball",
              "tab": "Ball and socket",
              "name": "Ball-and-socket joint",
              "bend": [0, 180],
              "start": 40,
              "twist": True,
              "axes": "3",
              "angle_label": "Swing the limb",
              "where": "Shoulder, hip",
              "hold": "A ring of ligaments and a deep cuff of muscle",
              "trade": "Almost every direction at once — and nothing much saying no. The shoulder is the most dislocated joint you own and the only one that can throw a ball.",
              "twist_yes": "It turns, and it keeps turning. A round end in a round socket has no direction to refuse.",
              "twist_no": ""},
             {"id": "pivot",
              "tab": "Pivot",
              "name": "Pivot joint",
              "bend": [0, 0],
              "start": 0,
              "twist": True,
              "axes": "1 — a turn",
              "angle_label": "This joint does not bend",
              "where": "Top of the neck, and between the two bones of the forearm",
              "hold": "A ring of ligament that one bone turns inside",
              "trade": "It cannot bend at all, and it turns further than anything else. Shaking your head \"no\" happens here; nodding \"yes\" happens at the joint above it.",
              "twist_yes": "It turns about 80 degrees each way. That is the whole of its job.",
              "twist_no": ""},
             {"id": "fixed",
              "tab": "Fixed",
              "name": "Fixed joint",
              "bend": [0, 0],
              "start": 0,
              "twist": False,
              "axes": "0",
              "angle_label": "This joint does not bend",
              "where": "Between the plates of the skull, and in the adult pelvis",
              "hold": "The bones are locked together along a jagged seam",
              "trade": "No movement at all, and nothing can be pushed out of place. A box that has to protect a brain should not have moving parts in it.",
              "twist_yes": "",
              "twist_no": "Nothing moves. The two bones interlock along a wavy join and are effectively one bone."},
         ]},

        {"type": "key-fact", "ref": "shape-decides"},

        # #s-cases — the same per-item sorter as b2-01, with a per-item option
        # set and a closing band gated on all-decided.
        {"type": "job-sort", "id": "four-places", "anchor": "s-cases",
         "ground": "inset",
         "eyebrow": "Your turn · four places in the body",
         "heading": "Which of the four is this?",
         "head_counter": {"format": "{n} of 4 decided", "total": 4},
         "demand": "classify",
         "prompt": "A model is worth having when it makes the right "
                   "prediction, and worth understanding when it fails. One of "
                   "these four is not any of the types.",
         "items": [
             {"id": "k1",
              "text": "Your knee: it bends behind you and straightens, and it does not turn.",
              "options": _TYPES,
              "answer": "Hinge.",
              "why": "One direction only, held by strong ligaments at each side. It is also why a twisting tackle damages a knee so badly — the twist is the one thing it cannot give way to."},
             {"id": "k2",
              "text": "Your hip: it swings your leg forwards, backwards, out to the side, and lets you turn your foot outwards.",
              "options": _TYPES,
              "answer": "Ball and socket.",
              "why": "Same shape as the shoulder, but with a much deeper socket. Deeper socket, less range, far fewer dislocations — the same trade made differently."},
             {"id": "k3",
              "text": "The seams across the top of an adult skull, where the plates meet along a jagged line.",
              "options": _TYPES,
              "answer": "Fixed.",
              "why": "They move in a baby, while the skull is still growing, and then lock. A protective box is worth more than a movable one."},
             {"id": "k4",
              "text": "The joint at the base of your thumb, which lets you swing the thumb across your palm and press it against every finger.",
              "options": _TYPES,
              "answer": "None of these.",
              "why": "It is a saddle joint: both bone ends are curved one way and hollow the other, like two saddles crossed. It moves in two directions but not three, and no other joint in the body is quite like it."},
         ],
         "close_all": "Three fitted and one did not. That is not a fault in the "
                      "model — a model that fits everything has stopped "
                      "telling you anything. Four types cover most of the "
                      "skeleton and then hand you a short list of joints worth "
                      "looking at properly."},

        # ⊕ #s-words — the five words this lesson USES and never stops to
        # define. Design draws no words section on this page and the RAIL IS
        # NOT TOUCHED: the block carries an `anchor` because that is what a
        # section carries, and `check_rail_matches_design` compares the built
        # rail against the one Design drew.
        # `terms` must match `vocabulary[].term` byte for byte — `r_keyword`
        # drops a term it cannot resolve, silently, and renders nothing at all
        # if it drops them all.
        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. "
                 "If you cannot say it, you do not know it yet.",
         "terms": ["Joint", "Ligament", "Tendon", "Cartilage",
                   "Dislocation"]},

        {"type": "misconception", "id": "tendon-or-ligament", "anchor": "s-think",
         "targets": "BODY-04"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "key_facts": [
        {"id": "shape-decides",
         "text": "The shape of the bone ends decides what a joint can do. "
                 "Every direction it can move in is a direction it cannot "
                 "resist.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    "activities": [
        {"id": "tendon-or-ligament",
         "kind": "predict",
         "demand": "explain",
         "targets": "BODY-04",
         "prompt": "The Achilles tendon is the thick cord you can feel at the "
                   "back of your ankle. Commit before you read on.",
         # ⊕ MRB-177, ruled 17 Aug 2026 — all four options now state a full
         # rule in the same three-part shape, so no option is a length
         # outlier in EITHER direction. ⚠️ There is no answer key on a
         # `predict`: the correct option is index 1, and it is correct
         # because the reveal below says a tendon joins muscle to bone. It
         # was EXPANDED to sit in the band, never shortened — shortening it
         # is what MRB-177 forbids. The three distractors carry the same
         # wrong beliefs they always did: the tendon/ligament swap, muscle-
         # to-muscle, and the ligament's job described as the tendon's.
         "options": [
             "It joins one bone to another, so the whole skeleton stays "
             "connected",
             "It joins a muscle to a bone, so the pull reaches the skeleton",
             "It joins two muscles together, so they can pull as one unit",
             "It is a strap that holds the ankle joint closed and steady",
         ],
         "reveal": [
             "A <strong>tendon</strong> joins muscle to bone. It is how the "
             "pull gets from the muscle to the thing being moved, and the "
             "Achilles is the biggest one you have. A <strong>ligament</strong> "
             "joins bone to bone, straps the joint together and stops it "
             "moving in directions it should not.",
             "The two words are easy to swap and the consequences are not. "
             "Tear a tendon and the muscle can no longer move that bone at "
             "all. Tear a ligament and the joint still moves — it moves too "
             "much, in a direction it was never meant to, and that is why a "
             "bad ankle sprain takes longer to trust than a broken bone.",
         ]},
    ],

    "ladder": {
        "recall": {
            "q": "Which of these joints allows movement in more than one "
                 "direction?",
            "options": [
                "The shoulder",
                "The elbow",
                "The knee",
                "The seams of the skull",
            ],
            "answer": 0,
            "feedback": {
                1: "A hinge. It bends and straightens along one line and "
                   "refuses everything else.",
                2: "Also a hinge — the biggest one you have, and it turns "
                   "almost not at all.",
                3: "Those are fixed joints. They allow no movement in any "
                   "direction at all.",
            }},
        "apply": {
            "q": "Why can your shoulder rotate when your elbow cannot?",
            # ⊕ MRB-177, ruled 17 Aug 2026 — the three distractors now state
            # wrong RULES, in the same shape as the correct option. The
            # correct option and its index are unchanged.
            "options": [
                "A joint turns when the muscles around it are strong enough, "
                "and the elbow's are not",
                "Cartilage is what lets a joint turn, so a joint with less of "
                "it turns less",
                "The shape of the bone ends: a round ball in a socket turns, a "
                "groove does not",
                "Ligaments stretch with use, so a joint you have never "
                "trained to rotate will not rotate",
            ],
            "answer": 2,
            "feedback": {
                0: "Strength is not the limit. Nothing you could train would "
                   "make a groove turn.",
                1: "Cartilage is the smooth facing that stops grinding. It "
                   "does not decide the directions.",
                3: "Stretching ligaments does not add a direction; it just "
                   "makes an unstable joint. The shape is what decides.",
            }},
        "explain": {
            "q": "Explain why the shoulder is worth having even though it "
                 "dislocates, and why the knee is built the opposite way. Use "
                 "both joints in your answer.",
            "field_label": "Your explanation",
            "placeholder": "The shoulder is a ball-and-socket joint, which "
                           "means…",
            "success": [
                "Says the shoulder is a ball-and-socket joint and names "
                "something it lets you do that a hinge could not.",
                "Says the range comes at the cost of stability — nothing is "
                "refusing those directions.",
                "Says the knee is a hinge, and names what it has to do "
                "instead: carry weight without folding.",
                "Says every direction a joint allows is a direction it cannot "
                "resist.",
                "Uses the shape of the bone ends, not muscle strength, as the "
                "reason for both.",
            ]},
        "produce": {
            "q": "You are designing a robot arm that has to lift a kettle off "
                 "a worktop and pour it into a cup. Choose a joint type for "
                 "the shoulder, the elbow and the wrist, justify each one, and "
                 "then say one thing your robot will not be able to do that a "
                 "person can.",
            "field_label": "Your design",
            "placeholder": "At the shoulder I would use…",
            "success": [
                "Chooses a ball-and-socket shoulder and gives the reason: "
                "reaching in more than one direction.",
                "Chooses a hinge elbow and gives the reason: strength and "
                "control along one line.",
                "Gives the wrist a joint that can turn, so the kettle can be "
                "tipped.",
                "Says something about the cost of the choices — more "
                "directions means less stability, or a heavier joint.",
                "Names a limitation compared with a person, and links it to a "
                "joint the design does not have.",
            ]},
    },

    "key_note": "A joint is where two bones meet, strapped together by "
                "ligaments and faced with cartilage. Hinge joints move one "
                "way; ball-and-socket joints move many; pivot joints turn; "
                "fixed joints do not move at all. Range and stability are "
                "bought from each other.",

    "stretch": [
        {"type": "explainer", "id": "cartilage-has-no-blood-supply",
         "text": "The smooth cartilage on the end of a bone has no blood "
                 "supply of its own. It is fed by fluid squeezed through it "
                 "every time the joint is loaded and unloaded — which means "
                 "the only way to feed it is to use it, and the only way to "
                 "starve it is to stop. It also means that when it is damaged "
                 "it heals slowly and often not at all, because there is no "
                 "bloodstream delivering material to repair it with. That "
                 "single fact is behind most of what a physiotherapist tells "
                 "people to do."},
    ],

    "support": [],

    # ── vocabulary (§10.2, §12) ─────────────────────────────────────────────
    # ⚠️ `definition` + `note`, not `gloss`. The build contract's §12 names the
    # key `gloss`; the SHIPPED schema is `{"term", "definition", "note"}` — that
    # is what `r_keyword` reads (build_ks3.py:908) and what every live lesson
    # authors. Authored to the shipped spelling so the terms reach the unit
    # page's "Words this unit gives you" chips and the reading-age gate's
    # exclusion list.
    #
    # Every definition is a KEY FACT (MRB-225): the version that is TRUE, not
    # the famous one. Where this lesson's own `key_facts` entry says the same
    # thing, the card agrees with it rather than restating it loosely.
    #
    # `Cartilage` and `ligament` are named in the opening explainer and neither
    # is defined there; `tendon` is defined only inside the `#s-think` reveal,
    # which a student reaches after the confusion the card exists to fix.
    "vocabulary": [
        {"term": "Joint",
         "definition": "A place where two or more bones meet.",
         "note": "Meeting is what makes it a joint, not bending. Some joints "
                 "swing in every direction, some only turn, and some do not "
                 "move at all."},
        {"term": "Ligament",
         "definition": "A tough strap joining one bone to another, holding a "
                       "joint together.",
         "note": "Tear one and the joint still moves — it moves too far, in a "
                 "direction it was never meant to."},
        {"term": "Tendon",
         "definition": "A tough cord joining a muscle to a bone, so that the "
                       "muscle's pull reaches the skeleton.",
         "note": "Bone to bone is a ligament; muscle to bone is a tendon. The "
                 "Achilles, at the back of your ankle, is the biggest tendon "
                 "you have."},
        {"term": "Cartilage",
         "definition": "The smooth, slippery layer facing the ends of the "
                       "bones inside a joint, which stops them grinding on "
                       "each other.",
         "note": "It has no blood supply of its own. It is fed by being used, "
                 "and it heals slowly and often not at all."},
        {"term": "Dislocation",
         "definition": "A joint pushed out of place, so that the two bone "
                       "ends no longer sit together properly.",
         "note": "The shoulder is the most dislocated joint you own, because "
                 "it is the one that refuses the fewest directions."},
    ],

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Mixing up tendons and ligaments?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Joint injury and repair, and the mechanics of levers in "
                   "the body.",

    "ws": ["analysis-and-evaluation"],

    "review_state": "draft",
}
