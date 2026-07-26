"""C1 — Particles and their behaviour. The Phase 1 vertical slice.

architecture.md §9 (build C1 first) and §10.1 phase 1. Six lessons, authored
end to end against the ten laws (§5.0), the segment vocabulary (§5.1.1) and the
per-lesson done-list (§10.2).

**review_state is `draft` on every lesson.** Mide is the sole science gate
(§5.10). Nothing here publishes until he has reviewed it; `draft` →
`examiner-reviewed` → `frozen`.

**Statutory allocation.** C1 has six lessons and five statutory statements, so
§11 decision 11 bites here first. `KS3.C.PNM.01` is split into three clause-level
sub-IDs (see `substatements.py`); nothing else needed splitting. Every subject-
content clause below is owned exactly once:

    L1 particle-model            KS3.C.PNM.01a
    L2 solids-liquids-and-gases  KS3.C.PNM.01b
    L3 changes-of-state          KS3.C.PNM.02, KS3.P.PHYC.01
    L4 gas-pressure              KS3.C.PNM.01c
    L5 diffusion                 KS3.C.PIS.03, KS3.P.PHYC.04
    L6 testing-the-model         KS3.WS.ATT.02

**WS-primary lessons anchor `covers` on a Working Scientifically statement —
now a rule, architecture.md §5.7.1.** L6 is an INVESTIGATION lesson (§7.5 lists
18 of them across KS3). It teaches no new subject content by design: it tests
the model built in L1–L5. But §10.2 requires `covers` non-empty. Anchoring it on
`KS3.WS.ATT.02` — *theories develop as earlier explanations are modified to take
account of new evidence* — is honest (it is exactly what the lesson does) and
legal (WS is exempt from the exactly-once rule, §5.7).

Raised by this slice as a design decision; **ruled 26 Jul 2026 and promoted to a
general rule in §5.7.1**, so all 18 INVESTIGATION lessons follow one pattern
instead of each author re-deciding. Exactly the kind of finding §9 says the
slice exists to produce.
"""

UNIT = {
    "code":            "C1",
    "slug":            "particles-and-their-behaviour",
    "title":           "Particles and their behaviour",
    "discipline":      "chemistry",
    "statutory_area":  "The particulate nature of matter",
    "split_rationale": None,
    "intro":           "Everything around you — this page, the air in your lungs, "
                       "the water in a glass — is built from particles far too "
                       "small to see. This unit builds that idea, then pushes it "
                       "until it nearly breaks.",
    "lessons": [

# ══════════════════════════════════════════════════════════════════════════
# L1 — The particle model (MODEL)
# ══════════════════════════════════════════════════════════════════════════
{
    "slug":        "particle-model",
    "title":       "The particle model",
    "discipline":  "chemistry",
    "unit":        "particles-and-their-behaviour",
    "family":      "MODEL",

    "covers":      ["KS3.C.PNM.01a"],
    "touches":     [],
    "threads":     [{"id": "particles", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 35,

    "requires":    [],
    "assumes":     [],
    "references":  [],
    "ks4_links":   ["chemistry/bonding/states-of-matter"],

    "big_question": "What is everything made of?",

    "phenomenon": {
        "kind": "demo",
        "title": "Half a glass of water, half a glass of alcohol",
        "prompt": "Pour 50 cm³ of water into 50 cm³ of alcohol. You now have "
                  "100 cm³ of liquid. Except you don't — you have about 97 cm³.",
        "commit": "Where did the missing 3 cm³ go?",
    },

    "misconceptions": [
        {"id": "PART-01",
         "statement": "Matter is continuous — you could keep cutting something "
                      "in half forever and never reach a smallest piece.",
         "elicited_by": "keep-cutting",
         "confronted_by": "mixing-volumes"},
        {"id": "PART-02",
         "statement": "There is air (or dust, or something) in the gaps between "
                      "particles.",
         "elicited_by": "what-is-in-the-gap",
         "confronted_by": "gap-reveal"},
    ],

    "vocabulary": [
        {"term": "particle",
         "definition": "One of the tiny pieces that all matter is made from, far "
                       "too small to see.",
         "note": "In this unit 'particle' means atoms or molecules. You will "
                 "meet those names properly in C2."},
        {"term": "matter",
         "definition": "Anything that has mass and takes up space.",
         "note": None},
        {"term": "model",
         "definition": "A simple picture or idea that helps explain something we "
                       "cannot see directly.",
         "note": "A model does not have to be a perfect copy to be useful. "
                 "L6 asks how far this one can be pushed."},
    ],

    "figures": [
        {"id": "c1-particles-three-states", "kind": "schematic",
         "caption": "Particles drawn as circles in a solid, a liquid and a gas.",
         "status": "needed"},
        {"id": "c1-mixing-volumes", "kind": "apparatus",
         "caption": "Two measuring cylinders, before and after mixing.",
         "status": "needed"},
    ],

    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "explainer", "id": "everything-is-particles",
         "text": "All matter is made of particles. They are far too small to "
                 "see. They are always moving. Between them there is nothing "
                 "at all — not air, not dust. Just empty space."},
        {"type": "misconception", "id": "gap-reveal", "targets": "PART-02"},
        {"type": "keyword", "terms": ["particle", "matter"]},
        {"type": "explainer", "id": "why-97",
         "text": "Water particles are smaller than alcohol particles. When the "
                 "two mix, the water particles slip into the gaps. Nothing is "
                 "lost. The particles just pack more tightly."},
        {"type": "figure", "ref": "c1-particles-three-states"},
        {"type": "check", "id": "draw-the-gap"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "how-small",
         "text": "One drop of water holds more particles than there are drops "
                 "of water in all the oceans on Earth. We really do mean too "
                 "small to see."},
        {"type": "check", "id": "estimate-particles"},
    ],

    "support": [],   # slot present, content deferred — §11 decision 4

    "activities": [
        {"id": "keep-cutting", "kind": "predict",
         "demand": "elicit a prior belief",
         "prompt": "Imagine cutting a piece of copper in half, then in half "
                   "again, over and over. Do you ever reach a piece that cannot "
                   "be cut?",
         "options": ["No — you could go on forever",
                     "Yes — you reach a single particle"],
         "reveal": "You reach a single particle. Matter is not continuous; it "
                   "comes in pieces.",
         "targets": "PART-01"},
        {"id": "mixing-volumes", "kind": "predict-then-reveal",
         "demand": "confront PART-01 with a result it cannot explain",
         "prompt": "50 cm³ of water is added to 50 cm³ of alcohol. Predict the "
                   "total volume.",
         "options": ["100 cm³", "About 97 cm³", "More than 100 cm³"],
         "reveal": "About 97 cm³. If matter were continuous this could not "
                   "happen — there would be nowhere for anything to go.",
         "targets": "PART-01"},
        {"id": "what-is-in-the-gap", "kind": "predict",
         "demand": "elicit PART-02 before correcting it",
         "prompt": "What is in the space between the particles of a gas?",
         "options": ["Air", "Dust", "Nothing at all"],
         "reveal": "Nothing at all. Air is itself made of particles — so saying "
                   "'air is in the gaps' just moves the question along one step.",
         "targets": "PART-02"},
        {"id": "gap-reveal", "kind": "confrontation",
         "demand": "make the wrongness of PART-02 visible",
         "prompt": "If air filled the gaps between air particles, what would be "
                   "in the gaps between *those* particles?",
         "reveal": "The question never ends. The only answer that stops the "
                   "regress is: the gaps are empty.",
         "targets": "PART-02"},
        {"id": "draw-the-gap", "kind": "construct",
         "demand": "produce the model, not recognise it",
         "prompt": "Draw ten particles of a gas in a box. Label what is between "
                   "them.",
         "success": ["Particles drawn as separate circles, not touching",
                     "The space between them labelled 'nothing' or 'empty'",
                     "Particles roughly evenly spread"]},
        {"id": "estimate-particles", "kind": "construct",
         "demand": "transfer the scale idea to a new case",
         "prompt": "Explain to someone in Year 5 why we cannot see a single "
                   "particle with a school microscope.",
         "success": ["Says particles are far smaller than anything a light "
                     "microscope can show",
                     "Does not say 'because they are invisible'"]},
    ],

    "ladder": {
        "recall": {
            "q": "What is between the particles in a gas?",
            "options": ["Air", "Nothing at all", "Dust", "Water vapour"],
            "answer": 1,
            "feedback": {
                0: "Air is itself made of particles — this just moves the "
                   "question along. The gaps are empty. (PART-02)",
                2: "Dust is far bigger than a particle. The gaps are empty. "
                   "(PART-02)",
                3: "Water vapour is made of particles too. The gaps are empty. "
                   "(PART-02)",
            }},
        "apply": {
            "q": "50 cm³ of water is mixed with 50 cm³ of alcohol and the total "
                 "is 97 cm³. What does this tell you about particles?",
            "options": ["Some water particles were destroyed",
                        "The particles have spaces between them",
                        "Alcohol particles are smaller than water particles",
                        "3 cm³ evaporated"],
            "answer": 1,
            "feedback": {
                0: "Particles are never destroyed by mixing — mass is conserved. "
                   "The volume drops because particles pack into spaces.",
                2: "It is the other way round, and either way the point is the "
                   "spaces, not the sizes.",
                3: "Evaporation would take far longer and would not give a "
                   "repeatable 3 cm³.",
            }},
        "explain": {
            "q": "Explain why mixing two liquids can give a total volume smaller "
                 "than the two volumes added together.",
            "success": ["Says matter is made of particles",
                        "Says there are spaces between the particles",
                        "Says the smaller particles fit into those spaces",
                        "Says no particles are lost"]},
        "produce": {
            "q": "A student says: 'If I squash a gas, I am squashing the "
                 "particles smaller.' Write a reply that corrects them.",
            "success": ["Says the particles themselves do not change size",
                        "Says the spaces between particles get smaller",
                        "Uses the word 'particle' correctly"]},
    },

    "key_note": "All matter is made of tiny moving particles. Between them is "
                "empty space — not air. Squashing a substance closes the spaces; "
                "it never shrinks the particles.",

    "ws": ["scientific-attitudes"],
    "review_state": "draft",
},

# ══════════════════════════════════════════════════════════════════════════
# L2 — Solids, liquids and gases (CONTRAST)
# ══════════════════════════════════════════════════════════════════════════
{
    "slug":        "solids-liquids-and-gases",
    "title":       "Solids, liquids and gases",
    "discipline":  "chemistry",
    "unit":        "particles-and-their-behaviour",
    "family":      "CONTRAST",

    "covers":      ["KS3.C.PNM.01b"],
    "touches":     [],
    "threads":     [{"id": "particles", "level": 1},
                    {"id": "structure-function", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 40,

    "requires":    ["particle-model"],
    "assumes":     [],
    "references":  [],
    "ks4_links":   ["chemistry/bonding/states-of-matter"],

    "big_question": "Why does a solid keep its shape but a liquid doesn't?",

    "phenomenon": {
        "kind": "demo",
        "title": "The same stuff, three ways",
        "prompt": "Ice, water and steam are all the same substance. One holds "
                  "its shape, one takes the shape of its container, one fills "
                  "the whole room.",
        "commit": "Same particles. So what is different?",
    },

    "misconceptions": [
        {"id": "PART-03",
         "statement": "The particles themselves change — they melt, or get "
                      "softer, or expand — when a substance changes state.",
         "elicited_by": "what-changed",
         "confronted_by": "same-particles-reveal"},
        {"id": "PART-04",
         "statement": "Particles in a solid are completely still.",
         "elicited_by": "predict-solid-motion",
         "confronted_by": "vibration-sim"},
    ],

    "vocabulary": [
        {"term": "solid",
         "definition": "A state of matter that keeps its own shape and cannot be "
                       "squashed much.",
         "note": None},
        {"term": "liquid",
         "definition": "A state of matter that takes the shape of its container "
                       "but keeps the same volume.",
         "note": None},
        {"term": "gas",
         "definition": "A state of matter that spreads out to fill its whole "
                       "container.",
         "note": "'Gas' is a state. 'Air' is a particular mixture of gases — "
                 "they are not the same word."},
        {"term": "vibrate",
         "definition": "To move quickly back and forth about a fixed position.",
         "note": None},
    ],

    "figures": [
        {"id": "c1-arrangement-compare", "kind": "schematic",
         "caption": "Particle arrangement, movement and spacing in the three "
                    "states, side by side.",
         "status": "needed"},
    ],

    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "explainer", "id": "three-questions",
         "text": "For any state, ask three questions. How are the particles "
                 "arranged? How much do they move? How far apart are they? "
                 "Those three answers explain everything a state does."},
        {"type": "practical", "id": "state-sorter"},
        {"type": "misconception", "id": "same-particles-reveal", "targets": "PART-03"},
        {"type": "figure", "ref": "c1-arrangement-compare"},
        {"type": "keyword", "terms": ["solid", "liquid", "gas", "vibrate"]},
        {"type": "check", "id": "compare-cards"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "why-liquids-dont-squash",
         "text": "Liquids take the shape of the container. But they barely "
                 "squash at all. That is because the particles already touch. "
                 "There is almost no space left to close."},
        {"type": "check", "id": "explain-syringe"},
    ],

    "support": [],

    "activities": [
        {"id": "predict-solid-motion", "kind": "predict",
         "demand": "elicit PART-04",
         "prompt": "In a block of ice, are the particles moving?",
         "options": ["No — it's solid, they are still", "Yes — they vibrate"],
         "reveal": "They vibrate about fixed positions. Solid means fixed "
                   "*places*, not no movement.",
         "targets": "PART-04"},
        {"id": "vibration-sim", "kind": "simulation",
         "demand": "make the invisible motion visible",
         "prompt": "Watch the solid at low temperature. Look closely at any one "
                   "particle.",
         "reveal": "Every particle is vibrating. None of them leaves its place.",
         "targets": "PART-04"},
        {"id": "what-changed", "kind": "predict",
         "demand": "elicit PART-03",
         "prompt": "When ice melts, what happens to the particles themselves?",
         "options": ["They get softer", "They get bigger",
                     "They do not change at all"],
         "reveal": "They do not change at all. What changes is how they are "
                   "arranged and how they move.",
         "targets": "PART-03"},
        {"id": "same-particles-reveal", "kind": "confrontation",
         "demand": "make PART-03 visibly wrong",
         "prompt": "Freeze the water again. If the particles had melted, could "
                   "you get the ice back exactly as it was?",
         "reveal": "You can, every time. The particles were never changed — "
                   "only their arrangement was.",
         "targets": "PART-03"},
        {"id": "state-sorter", "kind": "classify",
         "demand": "apply the three questions, at speed",
         "prompt": "For each substance shown, decide the state and justify it "
                   "using arrangement, movement and spacing.",
         "success": ["State named correctly",
                     "Justification uses at least two of the three questions"]},
        {"id": "compare-cards", "kind": "construct",
         "demand": "force the linked comparison, not two separate descriptions",
         "prompt": "Complete: 'A gas can be squashed but a liquid cannot, "
                   "because …'",
         "success": ["Mentions spacing in BOTH states, not just one",
                     "Says gas particles have large gaps to close",
                     "Says liquid particles are already touching"]},
        {"id": "explain-syringe", "kind": "construct",
         "demand": "transfer to unseen apparatus",
         "prompt": "A sealed syringe holds air. You push the plunger and it "
                   "moves in. You fill it with water instead and it barely "
                   "moves. Explain both results.",
         "success": ["Air: large spaces between particles, so they can close",
                     "Water: particles already touching, almost no space",
                     "Does not say the particles themselves squash"]},
    ],

    "ladder": {
        "recall": {
            "q": "In which state are the particles arranged in a regular pattern "
                 "and vibrating about fixed positions?",
            "options": ["Solid", "Liquid", "Gas", "All three"],
            "answer": 0,
            "feedback": {
                1: "Liquid particles touch but can move past each other — no "
                   "fixed positions.",
                2: "Gas particles are far apart and move freely.",
                3: "Only the solid has fixed positions.",
            }},
        "apply": {
            "q": "A gas is squashed into half its volume. What has happened to "
                 "the particles?",
            "options": ["Each particle is half the size",
                        "The particles are closer together",
                        "Half the particles have gone",
                        "The particles have melted"],
            "answer": 1,
            "feedback": {
                0: "Particles never change size — the spaces change. (PART-03)",
                2: "Nothing escapes a sealed container; mass is conserved.",
                3: "Melting is a change of state, not what squashing does. "
                   "(PART-03)",
            }},
        "explain": {
            "q": "Explain why a gas fills its container but a liquid does not.",
            "success": ["Gas particles are far apart",
                        "Gas particles move freely in all directions",
                        "Liquid particles are touching and stay together",
                        "Links spacing/movement to the observed behaviour"]},
        "produce": {
            "q": "Design a way to show a Year 5 class the difference between the "
                 "three states, using only people standing in a hall.",
            "success": ["Solid: people in rows, on the spot, wobbling",
                        "Liquid: people touching but sliding past each other",
                        "Gas: people far apart, moving fast in all directions",
                        "Makes clear the people themselves never change"]},
    },

    "key_note": "Solid: fixed pattern, vibrating in place, touching. Liquid: "
                "random, sliding past each other, touching. Gas: random, fast, "
                "far apart. The particles themselves never change.",

    "ws": ["experimental-skills-and-investigations"],
    "review_state": "draft",
},

# ══════════════════════════════════════════════════════════════════════════
# L3 — Changes of state (PROCESS)
# ══════════════════════════════════════════════════════════════════════════
{
    "slug":        "changes-of-state",
    "title":       "Changes of state",
    "discipline":  "chemistry",
    "unit":        "particles-and-their-behaviour",
    "family":      "PROCESS",

    "covers":      ["KS3.C.PNM.02", "KS3.P.PHYC.01"],
    "touches":     [],
    "threads":     [{"id": "particles", "level": 2},
                    {"id": "energy", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 45,

    "requires":    ["solids-liquids-and-gases"],
    "assumes":     [],
    "references":  [],
    "ks4_links":   ["chemistry/bonding/states-of-matter"],

    "big_question": "Where does the ice go when it melts?",

    "phenomenon": {
        "kind": "demo",
        "title": "The sealed bag",
        "prompt": "A sealed bag holds an ice cube. It is weighed, left on the "
                  "bench until the ice has melted, then weighed again.",
        "commit": "Will the reading go up, go down, or stay the same?",
    },

    "misconceptions": [
        {"id": "PART-05",
         "statement": "When a substance melts or evaporates, some of it is lost "
                      "or destroyed.",
         "elicited_by": "predict-mass",
         "confronted_by": "sealed-bag-weigh"},
        {"id": "PART-06",
         "statement": "Melting and dissolving are the same thing.",
         "elicited_by": "sort-melting-dissolving",
         "confronted_by": "two-routes-compare"},
        {"id": "PART-07",
         "statement": "Bubbles in boiling water are made of air, or of nothing.",
         "elicited_by": "what-is-in-the-bubble",
         "confronted_by": "bubble-reveal"},
    ],

    "vocabulary": [
        {"term": "melting",
         "definition": "Changing from a solid to a liquid.",
         "note": None},
        {"term": "freezing",
         "definition": "Changing from a liquid to a solid.",
         "note": "Freezing and melting happen at the same temperature for a "
                 "given substance — they are the same doorway, used in "
                 "opposite directions."},
        {"term": "evaporating",
         "definition": "Changing from a liquid to a gas.",
         "note": None},
        {"term": "condensing",
         "definition": "Changing from a gas to a liquid.",
         "note": None},
        {"term": "sublimation",
         "definition": "Changing straight from a solid to a gas, with no liquid "
                       "in between.",
         "note": "Solid carbon dioxide does this — which is why it is called "
                 "dry ice."},
        {"term": "conserved",
         "definition": "Stays the same in total. Nothing is gained or lost.",
         "note": None},
    ],

    "figures": [
        {"id": "c1-state-change-map", "kind": "schematic",
         "caption": "The six changes of state as arrows between solid, liquid "
                    "and gas.",
         "status": "needed"},
        {"id": "c1-sealed-bag", "kind": "apparatus",
         "caption": "Sealed bag with ice on a balance, before and after.",
         "status": "needed"},
    ],

    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "misconception", "id": "sealed-bag-weigh", "targets": "PART-05"},
        {"type": "explainer", "id": "energy-in-energy-out",
         "text": "Heating gives particles more energy. They move more and break "
                 "away from each other. Cooling takes energy away. They settle "
                 "back together. Particles are never made or destroyed. So the "
                 "mass never changes."},
        {"type": "worked-example", "id": "mass-fifa"},
        {"type": "check", "id": "mass-fifa-do"},
        {"type": "figure", "ref": "c1-state-change-map"},
        {"type": "keyword", "terms": ["melting", "freezing", "evaporating",
                                      "condensing", "sublimation", "conserved"]},
        {"type": "misconception", "id": "two-routes-compare", "targets": "PART-06"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "reversible",
         "text": "Every change of state can be run backwards. Freeze the water "
                 "and you get ice again. It is the same substance, not a new "
                 "one. That is what makes it a physical change."},
        {"type": "check", "id": "bubble-reveal"},
    ],

    "support": [],

    "activities": [
        {"id": "predict-mass", "kind": "predict",
         "demand": "elicit PART-05 before the balance settles it",
         "prompt": "The sealed bag of ice is weighed, then weighed again after "
                   "melting. Predict the reading.",
         "options": ["Lower than before", "Exactly the same", "Higher than before"],
         "reveal": "Exactly the same. Nothing entered or left the bag.",
         "targets": "PART-05"},
        {"id": "sealed-bag-weigh", "kind": "confrontation",
         "demand": "make PART-05 visibly wrong with a number",
         "prompt": "Read the balance before and after.",
         "reveal": "Identical readings. The ice did not go anywhere — the same "
                   "particles are still in the bag, arranged differently.",
         "targets": "PART-05"},
        {"id": "sort-melting-dissolving", "kind": "classify",
         "demand": "elicit PART-06",
         "prompt": "Sort these: ice in a warm room; sugar in tea; chocolate in "
                   "your hand; salt in water.",
         "options": ["Melting", "Dissolving"],
         "reveal": "Ice and chocolate melt — one substance, heated. Sugar and "
                   "salt dissolve — two substances, mixed.",
         "targets": "PART-06"},
        {"id": "two-routes-compare", "kind": "confrontation",
         "demand": "separate two ideas students routinely merge",
         "prompt": "Sugar 'disappears' in tea and ice 'disappears' in a warm "
                   "room. Are these the same change?",
         "reveal": "No. Melting needs only heat and involves one substance. "
                   "Dissolving needs a second substance — the liquid — and can "
                   "happen with no heating at all.",
         "targets": "PART-06"},
        {"id": "what-is-in-the-bubble", "kind": "predict",
         "demand": "elicit PART-07",
         "prompt": "Water is boiling. What is inside the bubbles?",
         "options": ["Air", "Nothing — they are empty", "Water as a gas"],
         "reveal": "Water as a gas. The liquid itself is turning into gas "
                   "inside the bubble.",
         "targets": "PART-07"},
        {"id": "bubble-reveal", "kind": "construct",
         "demand": "transfer the conservation idea to a new observation",
         "prompt": "If the bubbles were air, where would the air have come from "
                   "in a sealed, previously boiled flask?",
         "success": ["Recognises there is no source of air",
                     "Concludes the bubbles must be the water itself, as gas"],
         "targets": "PART-07"},
        {"id": "mass-fifa", "kind": "worked-example",
         "demand": "model the calculation before asking for it (Law 5)",
         "prompt": "A sealed flask holds 24.0 g of ice. It is left until all the "
                   "ice has melted. What is the mass of water?",
         "fifa": {
             "formula": "mass before = mass after  (mass is conserved)",
             "insert":  "mass before = 24.0 g",
             "fix":     "no particles enter or leave a sealed flask",
             "answer":  "24.0 g"}},
        {"id": "mass-fifa-do", "kind": "construct",
         "demand": "the same artifact, produced by the student (Law 5)",
         "prompt": "A sealed tube holds 18.5 g of solid iodine. It is warmed "
                   "until it has all sublimed to a purple gas. What is the mass "
                   "of gas? Set it out as Formula, Insert, Fix, Answer.",
         "success": ["States that mass is conserved",
                     "Inserts 18.5 g",
                     "Answer 18.5 g with units",
                     "Notes the tube is sealed"]},
    ],

    "ladder": {
        "recall": {
            "q": "What is the name of the change from a solid straight to a gas?",
            "options": ["Evaporation", "Condensation", "Sublimation", "Melting"],
            "answer": 2,
            "feedback": {
                0: "Evaporation is liquid → gas.",
                1: "Condensation is gas → liquid.",
                3: "Melting is solid → liquid.",
            }},
        "apply": {
            "q": "A sealed flask holds 30 g of ice. After melting completely, "
                 "what is the mass of the water?",
            "options": ["Less than 30 g", "Exactly 30 g", "More than 30 g",
                        "It depends on the temperature"],
            "answer": 1,
            "feedback": {
                0: "Nothing can leave a sealed flask — mass is conserved. "
                   "(PART-05)",
                2: "Nothing can enter a sealed flask either.",
                3: "Temperature changes the state, never the mass. (PART-05)",
            }},
        "explain": {
            "q": "Explain, in terms of particles, why the mass does not change "
                 "when ice melts in a sealed bag.",
            "success": ["Says the same particles are present throughout",
                        "Says no particles enter or leave",
                        "Says only the arrangement and movement change",
                        "Concludes total mass is therefore unchanged"]},
        "produce": {
            "q": "A student leaves a puddle of water on the playground. The next "
                 "day it has gone. They say 'the water was destroyed by the "
                 "sun'. Write a better explanation.",
            "success": ["Says the water evaporated to become a gas",
                        "Says the particles are still there, now in the air",
                        "Says nothing was destroyed",
                        "Mentions energy from the sun giving particles more "
                        "movement"]},
    },

    "key_note": "Heating gives particles energy to break away; cooling lets them "
                "settle back. Mass is always conserved and every change of state "
                "can be reversed. Melting needs heat and one substance; "
                "dissolving needs a liquid and two.",

    "ws": ["measurement", "analysis-and-evaluation"],
    "review_state": "draft",
},

# ══════════════════════════════════════════════════════════════════════════
# L4 — Gas pressure (MODEL)
# ══════════════════════════════════════════════════════════════════════════
{
    "slug":        "gas-pressure",
    "title":       "Gas pressure",
    "discipline":  "chemistry",
    "unit":        "particles-and-their-behaviour",
    "family":      "MODEL",

    "covers":      ["KS3.C.PNM.01c"],
    "touches":     [],
    "threads":     [{"id": "particles", "level": 2},
                    {"id": "forces-and-fields", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 40,

    "requires":    ["solids-liquids-and-gases"],
    "assumes":     [],
    "references":  [],
    "ks4_links":   ["chemistry/bonding/states-of-matter"],

    "big_question": "What is actually pushing on the inside of a balloon?",

    "phenomenon": {
        "kind": "demo",
        "title": "The marshmallow in the vacuum jar",
        "prompt": "A marshmallow sits in a sealed jar. Air is pumped out of the "
                  "jar and the marshmallow swells up. Air is let back in and it "
                  "shrivels.",
        "commit": "Nothing was added to the marshmallow. So why did it grow?",
    },

    "misconceptions": [
        {"id": "PART-08",
         "statement": "Gas pressure is the particles pushing against each other.",
         "elicited_by": "what-causes-pressure",
         "confronted_by": "collision-count-sim"},
        {"id": "PART-09",
         "statement": "Heating a gas makes the particles themselves get bigger, "
                      "which is why the pressure rises.",
         "elicited_by": "predict-heated-can",
         "confronted_by": "speed-not-size"},
    ],

    "vocabulary": [
        {"term": "pressure",
         "definition": "How hard a force pushes on each bit of a surface.",
         "note": "You will meet pressure = force ÷ area as a calculation in "
                 "Physics P5."},
        {"term": "collision",
         "definition": "When a moving particle hits something and bounces off.",
         "note": None},
    ],

    "figures": [
        {"id": "c1-gas-pressure-collisions", "kind": "schematic",
         "caption": "Gas particles colliding with the walls of a container, with "
                    "one collision arrowed.",
         "status": "needed"},
        {"id": "c1-vacuum-marshmallow", "kind": "apparatus",
         "caption": "Marshmallow in a bell jar, before and after pumping.",
         "status": "needed"},
    ],

    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "explainer", "id": "collisions-make-pressure",
         "text": "Gas particles move fast in every direction. Each time one "
                 "hits a wall, it gives that wall a tiny push. There are so "
                 "many hits each second that they feel like one steady push. "
                 "That push is gas pressure."},
        {"type": "misconception", "id": "collision-count-sim", "targets": "PART-08"},
        {"type": "figure", "ref": "c1-gas-pressure-collisions"},
        {"type": "keyword", "terms": ["pressure", "collision"]},
        {"type": "practical", "id": "pressure-sim"},
        {"type": "check", "id": "explain-marshmallow"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "temperature-and-pressure",
         "text": "Heat a sealed can and the particles speed up. They hit the "
                 "walls more often, and harder. So the pressure goes up. Not "
                 "one extra particle was added."},
        {"type": "check", "id": "aerosol-warning"},
    ],

    "support": [],

    "activities": [
        {"id": "what-causes-pressure", "kind": "predict",
         "demand": "elicit PART-08",
         "prompt": "What causes the pressure inside a balloon?",
         "options": ["Particles pushing against each other",
                     "Particles hitting the balloon wall",
                     "Air trying to escape"],
         "reveal": "Particles hitting the wall. Gas particles hardly ever touch "
                   "each other — they are far apart.",
         "targets": "PART-08"},
        {"id": "collision-count-sim", "kind": "simulation",
         "demand": "make the mechanism of pressure visible",
         "prompt": "Watch the wall counter. Every collision adds one.",
         "reveal": "Pressure tracks the number of wall collisions per second, "
                   "not how crowded the particles look.",
         "targets": "PART-08"},
        {"id": "predict-heated-can", "kind": "predict",
         "demand": "elicit PART-09",
         "prompt": "A sealed can of air is heated. The pressure inside rises. "
                   "Why?",
         "options": ["The particles get bigger",
                     "The particles move faster",
                     "More particles appear"],
         "reveal": "They move faster — so they hit the walls more often and "
                   "harder.",
         "targets": "PART-09"},
        {"id": "speed-not-size", "kind": "confrontation",
         "demand": "separate speed from size",
         "prompt": "If the particles had grown, what would happen to the mass of "
                   "gas in the sealed can?",
         "reveal": "It would have to increase — but a sealed can cannot gain "
                   "mass. The particles are the same; only their speed changed.",
         "targets": "PART-09"},
        {"id": "pressure-sim", "kind": "simulation",
         "demand": "vary one thing at a time and read the effect",
         "prompt": "Change the volume, then the temperature, then the number of "
                   "particles. Predict the pressure before each reveal.",
         "success": ["Predicts before each change",
                     "Explains each result using collisions per second"]},
        {"id": "explain-marshmallow", "kind": "construct",
         "demand": "explain the opening phenomenon with the model just built",
         "prompt": "Explain why the marshmallow swelled when air was pumped out "
                   "of the jar.",
         "success": ["Says the gas inside the marshmallow pushes outwards",
                     "Says fewer particles outside means fewer collisions on "
                     "the outside",
                     "Says the inside push is now greater than the outside push",
                     "Does not say the marshmallow 'gained air'"]},
        {"id": "aerosol-warning", "kind": "construct",
         "demand": "transfer to a safety context",
         "prompt": "Explain why an aerosol can carries the warning 'do not place "
                   "on a fire'.",
         "success": ["Heating makes the particles move faster",
                     "More and harder collisions with the walls",
                     "Pressure rises until the can may burst"]},
    ],

    "ladder": {
        "recall": {
            "q": "What causes the pressure of a gas on the walls of its "
                 "container?",
            "options": ["Particles hitting the walls",
                        "Particles pushing each other",
                        "Particles resting on the bottom",
                        "The weight of the particles"],
            "answer": 0,
            "feedback": {
                1: "Gas particles are far apart and rarely touch each other. "
                   "(PART-08)",
                2: "Gas particles move in all directions, not just downwards.",
                3: "Weight is far too small to explain it; collisions do.",
            }},
        "apply": {
            "q": "A sealed syringe of gas is squashed to half its volume. What "
                 "happens to the pressure, and why?",
            "options": ["Falls — the particles have less room",
                        "Rises — the particles hit the walls more often",
                        "Stays the same — the number of particles is unchanged",
                        "Rises — the particles get bigger"],
            "answer": 1,
            "feedback": {
                0: "Less room means *more* frequent collisions, not fewer.",
                2: "The number is unchanged, but they now hit a smaller area "
                   "more often.",
                3: "Particles never change size. (PART-09)",
            }},
        "explain": {
            "q": "Explain why the pressure inside a sealed can rises when it is "
                 "heated.",
            "success": ["Says heating gives particles more energy",
                        "Says the particles move faster",
                        "Says they hit the walls more often and harder",
                        "Says the number of particles has not changed"]},
        "produce": {
            "q": "Predict what happens to a sealed, part-inflated balloon taken "
                 "to the top of a mountain, and explain it.",
            "success": ["Predicts the balloon expands",
                        "Says there are fewer air particles outside at altitude",
                        "Says fewer collisions on the outside surface",
                        "Says the inside pressure now exceeds the outside"]},
    },

    "key_note": "Gas pressure is billions of particles hitting the walls every "
                "second. More particles, less space, or higher temperature all "
                "mean more collisions — and more pressure. The particles never "
                "change size.",

    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],
    "review_state": "draft",
},

# ══════════════════════════════════════════════════════════════════════════
# L5 — Diffusion (MODEL)
# ══════════════════════════════════════════════════════════════════════════
{
    "slug":        "diffusion",
    "title":       "Diffusion",
    "discipline":  "chemistry",
    "unit":        "particles-and-their-behaviour",
    "family":      "MODEL",

    "covers":      ["KS3.C.PIS.03", "KS3.P.PHYC.04"],
    "touches":     [],
    "threads":     [{"id": "particles", "level": 3}],
    "typical_year": 7,
    "typical_minutes": 40,

    "requires":    ["solids-liquids-and-gases"],
    "assumes":     [],
    "references":  [],
    "ks4_links":   ["chemistry/bonding/states-of-matter"],

    "big_question": "How does a smell get across the room with no wind?",

    "phenomenon": {
        "kind": "demo",
        "title": "Perfume at the front of the lab",
        "prompt": "A bottle is opened at the front of a still room. Hands go up "
                  "row by row as the smell reaches each one.",
        "commit": "Nothing is blowing it. So what is moving it?",
    },

    "misconceptions": [
        {"id": "PART-10",
         "statement": "Diffusion needs a draught, a current, or someone to "
                      "waft it — something has to push the particles along.",
         "elicited_by": "predict-still-room",
         "confronted_by": "random-walk-sim"},
        {"id": "PART-11",
         "statement": "Particles move in order to spread out — they 'want' to "
                      "fill the space, or they move from crowded to empty on "
                      "purpose.",
         "elicited_by": "why-spread",
         "confronted_by": "both-directions-sim"},
    ],

    "vocabulary": [
        {"term": "diffusion",
         "definition": "The spreading out of particles from where there are many "
                       "to where there are few, caused by their own random "
                       "movement.",
         "note": None},
        {"term": "concentration",
         "definition": "How many particles of a substance there are in a given "
                       "space.",
         "note": None},
        {"term": "random",
         "definition": "With no pattern and no set direction.",
         "note": "In science 'random' does not mean 'strange'. It means "
                 "genuinely unpredictable, direction by direction."},
    ],

    "figures": [
        {"id": "c1-diffusion-gradient", "kind": "schematic",
         "caption": "Particles spreading from a region of high concentration to "
                    "low, shown at three times.",
         "status": "needed"},
        {"id": "c1-bromine-jars", "kind": "apparatus",
         "caption": "Two gas jars, bromine below air, before and after the "
                    "cover slip is removed.",
         "status": "needed"},
    ],

    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "explainer", "id": "random-movement",
         "text": "Particles in a gas or a liquid never stop moving. They move "
                 "in random directions. Where particles are crowded, more of "
                 "them drift outwards than inwards. That is only because there "
                 "are more of them there to start with. Nothing pushes them."},
        {"type": "misconception", "id": "both-directions-sim", "targets": "PART-11"},
        {"type": "figure", "ref": "c1-diffusion-gradient"},
        {"type": "keyword", "terms": ["diffusion", "concentration", "random"]},
        {"type": "practical", "id": "diffusion-rate-sim"},
        {"type": "check", "id": "explain-bromine"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "why-liquids-slower",
         "text": "Diffusion is much slower in a liquid than in a gas. Liquid "
                 "particles already touch. So each one is knocked off course "
                 "at once. It takes far longer to get anywhere."},
        {"type": "check", "id": "predict-temperature"},
    ],

    "support": [],

    "activities": [
        {"id": "predict-still-room", "kind": "predict",
         "demand": "elicit PART-10",
         "prompt": "The windows are shut and the air is completely still. Will "
                   "the smell still reach the back of the room?",
         "options": ["No — nothing is moving it", "Yes — it will still get there"],
         "reveal": "It still gets there. The particles move themselves.",
         "targets": "PART-10"},
        {"id": "random-walk-sim", "kind": "simulation",
         "demand": "show movement with no external push",
         "prompt": "Follow one highlighted particle. There is no draught in this "
                   "simulation at all.",
         "reveal": "It still travels across the room — by a long, jagged, random "
                   "path, not a straight line.",
         "targets": "PART-10"},
        {"id": "why-spread", "kind": "predict",
         "demand": "elicit PART-11",
         "prompt": "Why do the particles move from the crowded side to the empty "
                   "side?",
         "options": ["They are trying to spread out evenly",
                     "They move randomly, and there are simply more of them on "
                     "the crowded side"],
         "reveal": "The second. No particle knows where it is going.",
         "targets": "PART-11"},
        {"id": "both-directions-sim", "kind": "simulation",
         "demand": "make the randomness visible, and the net effect countable",
         "prompt": "Count particles crossing the middle line, each way, for ten "
                   "seconds.",
         "reveal": "Particles cross in BOTH directions. More cross from the "
                   "crowded side only because more start there. The spreading "
                   "is a result, not a goal.",
         "targets": "PART-11"},
        {"id": "diffusion-rate-sim", "kind": "simulation",
         "demand": "isolate one variable at a time",
         "prompt": "Predict, then test: does diffusion speed up when you warm "
                   "the gas? When you switch to a liquid?",
         "success": ["Predicts before each run",
                     "Warmer → faster, explained by faster particle movement",
                     "Liquid → slower, explained by particles being closer"]},
        {"id": "explain-bromine", "kind": "construct",
         "demand": "explain a standard demonstration with the model",
         "prompt": "Brown bromine gas is in the lower jar, air in the upper. The "
                   "cover is removed and after some minutes both jars are pale "
                   "brown. Explain.",
         "success": ["Bromine particles move randomly",
                     "They spread from high to low concentration",
                     "Air particles also move into the lower jar",
                     "Does not say anything blew or pushed the bromine"]},
        {"id": "predict-temperature", "kind": "construct",
         "demand": "transfer to an everyday case",
         "prompt": "Explain why a teabag colours hot water faster than cold.",
         "success": ["Particles have more energy when hot",
                     "They move faster",
                     "So they spread through the water more quickly"]},
    ],

    "ladder": {
        "recall": {
            "q": "Diffusion is the movement of particles from an area of …",
            "options": ["low concentration to high concentration",
                        "high concentration to low concentration",
                        "cold to hot",
                        "high pressure to low pressure"],
            "answer": 1,
            "feedback": {
                0: "That is the wrong way round — the net movement is away from "
                   "crowding.",
                2: "Temperature changes the speed of diffusion, not its "
                   "direction.",
                3: "That describes wind, not diffusion. (PART-10)",
            }},
        "apply": {
            "q": "A drop of ink is placed in a beaker of still water. After an "
                 "hour the whole beaker is pale blue. Why?",
            "options": ["The water current carried it",
                        "The ink particles moved randomly and spread out",
                        "The ink dissolved and was destroyed",
                        "The ink particles were attracted to the edges"],
            "answer": 1,
            "feedback": {
                0: "The water is still — there is no current. (PART-10)",
                2: "Nothing is destroyed; the particles are still there, spread "
                   "out.",
                3: "Nothing attracts them; the movement is random. (PART-11)",
            }},
        "explain": {
            "q": "Explain why a smell spreads across a room even when the air is "
                 "completely still.",
            "success": ["Says the particles are always moving",
                        "Says the movement is random, with no set direction",
                        "Says there are more particles near the source, so more "
                        "move outwards than back",
                        "Does not rely on wind, draughts or wafting"]},
        "produce": {
            "q": "A student writes: 'Diffusion happens because particles want to "
                 "spread out evenly.' Rewrite this so it is scientifically "
                 "correct, and say what is wrong with the original.",
            "success": ["Removes the idea of particles wanting or trying",
                        "Says movement is random",
                        "Explains the net spread as a numbers effect",
                        "Identifies that particles have no aim or awareness"]},
    },

    "key_note": "Particles move randomly all the time. Where they are crowded, "
                "more happen to move outwards than inwards — so the substance "
                "spreads. Warmer means faster; liquids are much slower than "
                "gases. Nothing pushes and nothing intends it.",

    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],
    "review_state": "draft",
},

# ══════════════════════════════════════════════════════════════════════════
# L6 — Testing the model (INVESTIGATION)
# ══════════════════════════════════════════════════════════════════════════
{
    "slug":        "testing-the-model",
    "title":       "Testing the model: does it explain everything?",
    "discipline":  "chemistry",
    "unit":        "particles-and-their-behaviour",
    "family":      "INVESTIGATION",

    # WS-anchored `covers` per §5.7.1 — the standing rule for all 18
    # INVESTIGATION lessons, not a decision taken here. WS is exempt from the
    # exactly-once rule (§5.7), so this does not collide with any other lesson.
    "covers":      ["KS3.WS.ATT.02"],
    "touches":     ["KS3.C.PNM.01a", "KS3.C.PNM.02", "KS3.C.PIS.03"],
    "threads":     [{"id": "particles", "level": 3}],
    "typical_year": 7,
    "typical_minutes": 45,

    "requires":    ["particle-model", "changes-of-state", "gas-pressure",
                    "diffusion"],
    "assumes":     [],
    "references":  [{"unit": "P11", "lesson": "why-ice-floats",
                     "why": "The ice–water anomaly is the model's most famous "
                            "hard case. P11 owns it (§7.4); this lesson points "
                            "at it and must render gracefully before P11 "
                            "exists."}],
    "ks4_links":   ["chemistry/bonding/states-of-matter"],

    "big_question": "Is the particle model true, or just useful?",

    "phenomenon": {
        "kind": "data",
        "title": "The one that doesn't fit",
        "prompt": "Almost everything shrinks when it freezes — the particles "
                  "settle closer together. Water expands. Ice floats.",
        "commit": "Does that mean the particle model is wrong?",
    },

    "misconceptions": [
        {"id": "PART-12",
         "statement": "A scientific model is either true or false, and one "
                      "exception proves it wrong.",
         "elicited_by": "verdict-vote",
         "confronted_by": "model-limits-sort"},
        {"id": "PART-13",
         "statement": "Scientists' models never change once they are agreed.",
         "elicited_by": "predict-history",
         "confronted_by": "model-history-timeline"},
    ],

    "vocabulary": [
        {"term": "evidence",
         "definition": "Observations or measurements used to decide whether an "
                       "idea works.",
         "note": None},
        {"term": "anomaly",
         "definition": "A result that does not fit the pattern.",
         "note": "An anomaly is interesting, not embarrassing. It is usually "
                 "where the next discovery is hiding."},
        {"term": "peer review",
         "definition": "Other scientists checking a result before it is "
                       "accepted.",
         "note": None},
    ],

    "figures": [
        {"id": "c1-model-scorecard", "kind": "schematic",
         "caption": "A scorecard of observations against whether the simple "
                    "particle model explains them.",
         "status": "needed"},
        {"id": "c1-ice-water-density", "kind": "graph",
         "caption": "Density of water against temperature, showing the maximum "
                    "at 4 °C.",
         "status": "needed"},
    ],

    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "explainer", "id": "what-models-are-for",
         "text": "We judge a model by what it explains. It does not have to be "
                 "a photograph of the real thing. The particle model has "
                 "explained every lesson so far. Now we look for where it "
                 "struggles."},
        {"type": "practical", "id": "model-scorecard"},
        {"type": "misconception", "id": "model-limits-sort", "targets": "PART-12"},
        {"type": "figure", "ref": "c1-model-scorecard"},
        {"type": "keyword", "terms": ["evidence", "anomaly", "peer review"]},
        {"type": "misconception", "id": "model-history-timeline", "targets": "PART-13"},
        {"type": "check", "id": "design-a-test"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "the-ice-anomaly",
         "text": "Water is the famous exception. As it freezes, its particles "
                 "lock into an open pattern. That pattern takes up more room. "
                 "So ice floats, pipes burst, and ponds freeze from the top "
                 "down. That is what lets fish live through the winter."},
        {"type": "check", "id": "anomaly-consequences"},
    ],

    "support": [],

    "activities": [
        {"id": "verdict-vote", "kind": "predict",
         "demand": "elicit PART-12 as a public commitment",
         "prompt": "Water expands when it freezes. The simple particle model "
                   "says things should shrink. What should we do?",
         "options": ["Throw the model away — it is wrong",
                     "Keep it, but record where it fails",
                     "Ignore the water result"],
         "reveal": "Keep it and record the limit. A model that explains a "
                   "hundred things and fails on one is useful — as long as we "
                   "are honest about the one.",
         "targets": "PART-12"},
        {"id": "model-scorecard", "kind": "investigation",
         "demand": "judge the model against evidence, before building anything",
         "prompt": "For each observation, decide: does the simple particle model "
                   "explain it fully, partly, or not at all? Squashing a gas · "
                   "a smell crossing a room · ice floating · why a solid keeps "
                   "its shape · why water boils at exactly 100 °C at sea level.",
         "success": ["Each verdict justified by reference to the model",
                     "Identifies ice floating as the clear failure",
                     "Notices the model does not predict specific temperatures"]},
        {"id": "model-limits-sort", "kind": "confrontation",
         "demand": "replace 'true/false' with 'useful within limits'",
         "prompt": "Sort these statements into 'the model explains this' and "
                   "'the model needs more detail here'.",
         "reveal": "Every model has a boundary. Knowing where the boundary is "
                   "makes a model more useful, not less.",
         "targets": "PART-12"},
        {"id": "predict-history", "kind": "predict",
         "demand": "elicit PART-13",
         "prompt": "Has the scientific picture of the particle stayed the same "
                   "since it was first suggested?",
         "options": ["Yes — once agreed, it was settled",
                     "No — it has been changed several times"],
         "reveal": "It has changed repeatedly, each time because new evidence "
                   "arrived.",
         "targets": "PART-13"},
        {"id": "model-history-timeline", "kind": "confrontation",
         "demand": "show theory change as normal, not as failure",
         "prompt": "Place these on a timeline: particles as tiny solid balls · "
                   "particles with charges inside them · particles as mostly "
                   "empty space.",
         "reveal": "Each version was accepted, published and checked by other "
                   "scientists — and each was modified when evidence demanded "
                   "it. That is how science is supposed to work.",
         "targets": "PART-13"},
        {"id": "design-a-test", "kind": "construct",
         "demand": "design an investigation — the top of the ladder",
         "prompt": "Design a test to find out whether diffusion is faster in "
                   "hot water than cold. State your variables.",
         "success": ["Independent variable: temperature of the water",
                     "Dependent variable: time for colour to spread a set "
                     "distance",
                     "Names at least two control variables",
                     "Says how the result would be measured, not just observed"]},
        {"id": "anomaly-consequences", "kind": "construct",
         "demand": "transfer an anomaly to its real-world consequences",
         "prompt": "Explain why ponds freeze from the top down, and why that "
                   "matters to the animals in them.",
         "success": ["Ice is less dense than water so it floats",
                     "The ice layer sits on top",
                     "Water below stays liquid",
                     "Fish and other animals can survive the winter"]},
    ],

    "ladder": {
        "recall": {
            "q": "What is an anomaly?",
            "options": ["A mistake in an experiment",
                        "A result that does not fit the pattern",
                        "A result that has been repeated",
                        "A model that has been disproved"],
            "answer": 1,
            "feedback": {
                0: "It may be a mistake — but it may also be a real and "
                   "important result.",
                2: "Repeating is how you check an anomaly is genuine.",
                3: "One anomaly does not disprove a model. (PART-12)",
            }},
        "apply": {
            "q": "The particle model predicts substances get denser when they "
                 "freeze. Water does the opposite. What is the best scientific "
                 "response?",
            "options": ["Abandon the particle model",
                        "Keep the model and record where it fails",
                        "Ignore the water result as an error",
                        "Say water is not made of particles"],
            "answer": 1,
            "feedback": {
                0: "The model still explains a great deal. (PART-12)",
                2: "The result is repeatable and real, not an error.",
                3: "Water is certainly made of particles — the arrangement is "
                   "what is unusual.",
            }},
        "explain": {
            "q": "Explain why scientists keep using the particle model even "
                 "though it does not explain everything.",
            "success": ["Says it explains a very wide range of observations",
                        "Says its limits are known and recorded",
                        "Says models are judged by usefulness, not perfection",
                        "Gives at least one thing it explains well"]},
        "produce": {
            "q": "A new substance is discovered that does not behave as the "
                 "particle model predicts. Describe what scientists should do "
                 "next, and why.",
            "success": ["Repeat the measurements to check they are real",
                        "Publish the results so others can check them",
                        "Other scientists repeat the work — peer review",
                        "Modify the model if the evidence holds up",
                        "Does not say the model should simply be thrown away"]},
    },

    "key_note": "A model is judged by what it explains. The particle model "
                "explains states, changes of state, pressure and diffusion — and "
                "struggles with ice floating. Knowing a model's limits makes it "
                "more useful, not less. Models change when evidence demands it.",

    "ws": ["scientific-attitudes", "analysis-and-evaluation",
           "experimental-skills-and-investigations"],
    "review_state": "draft",
},

    ],
}
