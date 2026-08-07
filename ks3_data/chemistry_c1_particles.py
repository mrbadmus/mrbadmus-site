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

──────────────────────────────────────────────────────────────────────────
REVISION — MRB-177, 6 Aug 2026. "Content is all over the place; the texts
don't really link together."
──────────────────────────────────────────────────────────────────────────

Four structural defects were found and fixed. All six lessons stay `draft`.

1. **Seventeen activities were never placed in any composition.** Every single
   elicitation `predict` — the activity each misconception names in its
   `elicited_by` field — sat in `activities` and was referenced by no `core`,
   `stretch` or `support` block, so it never rendered. Two of the five
   "simulations" (`vibration-sim`, `random-walk-sim`) were orphaned the same
   way. The register said "PART-01 is elicited by keep-cutting"; the student
   never saw keep-cutting. Every activity is now placed, at the moment the
   error is born.

2. **Five declared figures were never placed** (`c1-mixing-volumes`,
   `c1-sealed-bag`, `c1-vacuum-marshmallow`, `c1-bromine-jars`,
   `c1-ice-water-density`). All five now sit beside the thing they show. No
   `figures` entry was added, removed or reworded.

3. **Hooks were not paid off where the student was still holding them.** L1 in
   particular posed "where did the missing 3 cm³ go?" and answered it four
   blocks later. Every lesson now answers its hook one block after it is asked
   — the intervening block being the student's committed wager, which Law 4
   requires.

4. **The five `kind: "simulation"` activities had no motion of any kind**, so
   Law 9 was unsatisfied on all of them. Four are now `kind: "lab"` records
   carrying a `sim` block (`particle-states` | `gas-pressure` | `diffusion`),
   each gated by a committed prediction with a keyed answer. The fifth,
   `diffusion-rate-sim`, is demoted to a do-mode task driving L5's flagship
   lab rather than being a third instrument in one lesson (§5.1 budget).

Also applied, from `docs/redesign/content_standards.md` (the two rules there
that are not KS4-shaped and are not already in architecture.md):

- **Distractor length parity.** No option set lets a student score by picking
  the longest line. Where the key was conspicuously longer, a distractor was
  made equally precise rather than the key truncated.
- **The three-beat misconception format.** Every `misconception` block now
  states the mistake in a student's own words *first*, then why it is wrong,
  then the correct version. Nine blocks needed this; all nine previously
  opened with a Socratic question and asserted the right answer without ever
  naming the wrong one out loud.

⚑ No net-new science was introduced. The one place it was tempting — naming
`deposition` as the sixth arrow on `c1-state-change-map` — was declined,
because it is outside the KS3 statutory language and would need a new
vocabulary entry and therefore a science review of its own.
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
         "elicited_by": "mixing-volumes",
         "confronted_by": "keep-cutting"},
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

    # Narrative order: the hook is wagered on (block 2) and paid off
    # immediately (block 3). Everything after that is the model being built
    # out of the payoff, one stated link at a time.
    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "check", "id": "mixing-volumes"},
        {"type": "explainer", "id": "why-97",
         "text": "Here is the answer. Everything is made of tiny particles with "
                 "gaps between them. Water particles and alcohol particles are "
                 "not the same size. Pour them together. The smaller particles "
                 "drop into the gaps between the bigger ones. So the mixture "
                 "packs tighter. Nothing is lost. Nothing is destroyed. Every "
                 "particle you poured in is still there. The total just takes up "
                 "less room than the two volumes added together."},
        {"type": "figure", "ref": "c1-mixing-volumes"},
        {"type": "check", "id": "keep-cutting"},
        {"type": "check", "id": "what-is-in-the-gap"},
        {"type": "misconception", "id": "gap-reveal", "targets": "PART-02"},
        {"type": "figure", "ref": "c1-particles-three-states"},
        {"type": "explainer", "id": "everything-is-particles",
         "text": "So here is the whole model, in three lines. All matter is made "
                 "of particles. The particles are always moving. Between them is "
                 "empty space — nothing at all. Every single thing in this unit "
                 "is worked out from those three lines."},
        {"type": "keyword", "terms": ["particle", "matter", "model"]},
        {"type": "check", "id": "word-check"},
        {"type": "check", "id": "draw-the-gap"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "how-small",
         "text": "Just how small is too small to see? One drop of water holds "
                 "more particles than there are drops of water in all the oceans "
                 "on Earth. So no microscope in any school will ever show you "
                 "one."},
        {"type": "check", "id": "estimate-particles"},
    ],

    "support": [],   # slot present, content deferred — §11 decision 4

    "activities": [
        {"id": "mixing-volumes", "kind": "predict-then-reveal",
         "demand": "elicit PART-01 by forcing a commitment on the hook",
         "prompt": "Before anyone explains it — commit to an answer. Where did "
                   "the missing 3 cm³ go?",
         "options": ["3 cm³ of liquid was destroyed when the two mixed",
                     "3 cm³ leaked out of the cylinder and evaporated",
                     "Nothing was lost — it just takes up less room"],
         "answer": 2,
         "reveal": "Nothing was lost. Every particle you poured in is still "
                   "there; the mixture simply packs into less space. The next "
                   "block explains exactly how.",
         "targets": "PART-01"},
        {"id": "keep-cutting", "kind": "predict",
         "demand": "confront PART-01 — matter comes in pieces, and the pieces "
                   "have a smallest size",
         "prompt": "So matter comes in pieces with gaps between them. How small "
                   "do the pieces go? Imagine cutting a lump of copper in half, "
                   "then in half again, over and over.",
         "options": ["No — you could keep halving it forever",
                     "Yes — you reach one single particle of copper"],
         "answer": 1,
         "reveal": "You reach a single particle. Matter is not continuous. It "
                   "comes in pieces, and copper's smallest piece is one copper "
                   "particle.",
         "targets": "PART-01"},
        {"id": "what-is-in-the-gap", "kind": "predict",
         "demand": "elicit PART-02 before correcting it",
         "prompt": "The model needs gaps. So what is actually inside a gap "
                   "between two particles of a gas?",
         "options": ["Air, the same air that is in the room",
                     "Tiny specks of dust too small to see",
                     "Nothing at all — empty space"],
         "answer": 2,
         "reveal": "Nothing at all. Most people say air — but air is itself made "
                   "of particles, so that answer only moves the question along "
                   "one step.",
         "targets": "PART-02"},
        {"id": "gap-reveal", "kind": "confrontation",
         "demand": "make the wrongness of PART-02 visible",
         "prompt": "Here is the idea to kill, in the words students really "
                   "write: 'the gaps between the particles are filled with air.' "
                   "If that were true, what would be in the gaps between the air "
                   "particles?",
         "reveal": "That answer never ends. Air is made of particles, which "
                   "would need air in their gaps, which is made of particles, "
                   "and on forever. The only answer that stops it is the right "
                   "one: the gaps are empty. There is nothing at all between "
                   "particles.",
         "targets": "PART-02"},
        {"id": "word-check", "kind": "reveal-cards",
         "demand": "recall",
         "prompt": "Three words this lesson runs on. Say the word out loud "
                   "before you tap each card — no peeking first.",
         "cards": [
             {"front": "The tiny pieces that all stuff is made from, far too "
                       "small to see",
              "back": "Particle"},
             {"front": "Anything that has mass and takes up space",
              "back": "Matter"},
             {"front": "A simple picture or idea that explains something we "
                       "cannot see directly",
              "back": "Model"},
         ]},
        {"id": "draw-the-gap", "kind": "construct",
         "demand": "produce the model, not recognise it",
         "prompt": "Now build the model yourself instead of reading it. Draw ten "
                   "particles of a gas in a box, and label what is between them.",
         "success": ["Particles drawn as separate circles, not touching",
                     "The space between them labelled 'nothing' or 'empty'",
                     "Particles roughly evenly spread"]},
        {"id": "estimate-particles", "kind": "construct",
         "demand": "transfer the scale idea to a new case",
         "prompt": "Use that number on someone else. Explain to a Year 5 student "
                   "why we cannot see a single particle with a school "
                   "microscope.",
         "success": ["Says particles are far smaller than anything a light "
                     "microscope can show",
                     "Does not say 'because they are invisible'"]},
    ],

    "ladder": {
        "recall": {
            "q": "What is between the particles in a gas?",
            "options": ["Air from the room around it", "Nothing at all",
                        "Tiny specks of floating dust", "Water vapour"],
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
        "commit": "Your model from last lesson says the particles are the same "
                  "in all three. So what is different?",
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

    # CONTRAST rhythm (§6): lead → predict-gated A/B instrument → parallel
    # compare-cards as reference → explanation-chain builder forcing the
    # linked comparison → ladder.
    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "check", "id": "what-changed"},
        {"type": "explainer", "id": "three-questions",
         "text": "So the particles themselves are identical in ice, water and "
                 "steam. Only three things change. How are the particles "
                 "arranged? How much do they move? How far apart are they? "
                 "Answer those three and you have explained everything a state "
                 "does — including why a solid keeps its shape and a liquid "
                 "does not."},
        {"type": "misconception", "id": "same-particles-reveal", "targets": "PART-03"},
        {"type": "check", "id": "predict-solid-motion"},
        {"type": "practical", "id": "vibration-sim"},
        {"type": "check", "id": "state-cards"},
        {"type": "figure", "ref": "c1-arrangement-compare"},
        {"type": "keyword", "terms": ["solid", "liquid", "gas", "vibrate"]},
        {"type": "practical", "id": "state-sorter"},
        {"type": "check", "id": "compare-cards"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "why-liquids-dont-squash",
         "text": "Here is one the three questions answer in a single line. A "
                 "liquid takes the shape of its container, so it looks like it "
                 "ought to squash. It barely does. That is because its particles "
                 "already touch — there is almost no space left to close."},
        {"type": "check", "id": "explain-syringe"},
    ],

    "support": [],

    "activities": [
        {"id": "what-changed", "kind": "predict",
         "demand": "elicit PART-03",
         "prompt": "Commit before you read on. When ice melts, what happens to "
                   "the particles themselves?",
         "options": ["They get softer, the way warm wax does",
                     "They get bigger as they warm up",
                     "They do not change at all"],
         "answer": 2,
         "reveal": "They do not change at all. What changes is how they are "
                   "arranged, how much they move, and how far apart they are.",
         "targets": "PART-03"},
        {"id": "same-particles-reveal", "kind": "confrontation",
         "demand": "make PART-03 visibly wrong",
         "prompt": "The wrong idea, said out loud: 'when ice melts, the "
                   "particles melt too — they go soft and runny.' Now freeze the "
                   "puddle again. If the particles really had melted, could you "
                   "ever get the ice back exactly as it was?",
         "reveal": "You can, every time, as often as you like. Nothing that had "
                   "truly melted away could come back identical. So the "
                   "particles were never changed at all — only their arrangement "
                   "and their movement were.",
         "targets": "PART-03"},
        {"id": "predict-solid-motion", "kind": "predict",
         "demand": "elicit PART-04",
         "prompt": "Those three questions include movement. So take the hardest "
                   "case. In a block of ice, are the particles moving?",
         "options": ["No — in a solid the particles are completely still",
                     "Yes — they vibrate without leaving their places"],
         "answer": 1,
         "reveal": "They vibrate. 'Solid' means fixed *places*, not no movement "
                   "at all.",
         "targets": "PART-04"},
        {"id": "vibration-sim", "kind": "lab",
         "demand": "investigate",
         "prompt": "Now watch it happen. Predict first: as you slide the "
                   "temperature up from very cold, what does a solid's particles "
                   "do first?",
         "options": ["Each particle swells and takes up more room",
                     "Each particle vibrates faster but stays in place",
                     "The particles break apart straight away"],
         "answer": 1,
         "sim": {"kind": "particle-states",
                 "controls": ["temperature"],
                 "readouts": ["average particle speed", "state"],
                 "caption": "Watch one particle. In the solid it never leaves "
                            "its place — it only wobbles further and faster."},
         "reveal": "They vibrate faster and further, still around the same fixed "
                   "places. Nothing swells. Turn the temperature up far enough "
                   "and they finally break free of each other — that is melting, "
                   "and it is the whole of the next lesson.",
         "targets": "PART-04"},
        {"id": "state-cards", "kind": "reveal-cards",
         "demand": "recall",
         "prompt": "Three states, three answers each: arrangement, movement, "
                   "spacing. Say your three answers out loud, then tap to check.",
         "cards": [
             {"front": "Solid",
              "back": "Fixed regular pattern · vibrating on the spot · touching"},
             {"front": "Liquid",
              "back": "Jumbled, no pattern · sliding past each other · touching"},
             {"front": "Gas",
              "back": "Jumbled, no pattern · moving fast in all directions · "
                      "far apart"},
         ]},
        {"id": "state-sorter", "kind": "classify",
         "demand": "apply the three questions, at speed",
         "prompt": "Now use the three questions at speed. For each substance "
                   "shown, decide the state and justify it using arrangement, "
                   "movement and spacing.",
         "success": ["State named correctly",
                     "Justification uses at least two of the three questions"]},
        {"id": "compare-cards", "kind": "construct",
         "demand": "force the linked comparison, not two separate descriptions",
         "prompt": "One last job, and it is the hardest one on the page: a "
                   "comparison has to mention BOTH sides. Complete: 'A gas can "
                   "be squashed but a liquid cannot, because …'",
         "success": ["Mentions spacing in BOTH states, not just one",
                     "Says gas particles have large gaps to close",
                     "Says liquid particles are already touching"]},
        {"id": "explain-syringe", "kind": "construct",
         "demand": "transfer to unseen apparatus",
         "prompt": "Same idea, apparatus you have not seen. A sealed syringe "
                   "holds air. You push the plunger and it moves in. You fill it "
                   "with water instead and it barely moves. Explain both "
                   "results.",
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
        "prompt": "Ice, water and steam turned out to be the same particles "
                  "rearranged. So here is the test. A sealed bag holds an ice "
                  "cube. It is weighed, left on the bench until the ice has "
                  "melted, then weighed again.",
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

    # PROCESS rhythm (§6): lead → mechanism → worked stepper with predict-gates
    # → do-mode construction of the same artifact → what follows from the
    # mechanism → ladder.
    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "check", "id": "predict-mass"},
        {"type": "misconception", "id": "sealed-bag-weigh", "targets": "PART-05"},
        {"type": "figure", "ref": "c1-sealed-bag"},
        {"type": "explainer", "id": "energy-in-energy-out",
         "text": "So the ice did not go anywhere. Here is what it did instead. "
                 "Heating gives the particles more energy, so they move more and "
                 "break away from each other. Cooling takes energy away, so they "
                 "settle back together. Not one particle is made and not one is "
                 "destroyed. That is why the balance never moved."},
        {"type": "practical", "id": "heating-sim"},
        {"type": "figure", "ref": "c1-state-change-map"},
        {"type": "keyword", "terms": ["melting", "freezing", "evaporating",
                                      "condensing", "sublimation", "conserved"]},
        {"type": "check", "id": "state-change-cards"},
        {"type": "worked-example", "id": "mass-fifa"},
        {"type": "check", "id": "mass-fifa-do"},
        {"type": "check", "id": "sort-melting-dissolving"},
        {"type": "misconception", "id": "two-routes-compare", "targets": "PART-06"},
        {"type": "check", "id": "what-is-in-the-bubble"},
        {"type": "check", "id": "bubble-reveal"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "reversible",
         "text": "Every one of those arrows runs both ways. Freeze the water and "
                 "you get ice again — the same substance, not a new one. Nothing "
                 "has been made and nothing destroyed. That is exactly what "
                 "makes a change of state a physical change."},
        {"type": "check", "id": "run-it-backwards"},
    ],

    "support": [],

    "activities": [
        {"id": "predict-mass", "kind": "predict",
         "demand": "elicit PART-05 before the balance settles it",
         "prompt": "Commit before the balance settles it. What will the second "
                   "reading say?",
         "options": ["Lower — some of the ice was lost",
                     "Exactly the same as before",
                     "Higher — melted water is heavier"],
         "answer": 1,
         "reveal": "Exactly the same. Nothing entered the bag and nothing left "
                   "it.",
         "targets": "PART-05"},
        {"id": "sealed-bag-weigh", "kind": "confrontation",
         "demand": "make PART-05 visibly wrong with a number",
         "prompt": "Name the wrong idea first. Plenty of students write: 'the "
                   "ice melted, so some of it was lost.' Now read the two "
                   "balance readings again.",
         "reveal": "The two readings are identical, to the last decimal place. "
                   "Nothing was lost, because losing something means particles "
                   "leaving — and a sealed bag lets nothing out. The same "
                   "particles are still in there, just arranged differently. "
                   "That is what 'mass is conserved' means.",
         "targets": "PART-05"},
        {"id": "heating-sim", "kind": "lab",
         "demand": "investigate",
         "prompt": "This is the same particle lab you used last lesson, now with "
                   "a heater on it. Predict first: you heat a solid steadily. "
                   "What happens at the moment it melts?",
         "options": ["The particles suddenly get bigger",
                     "The particles break out of their fixed places",
                     "Some particles disappear into the air"],
         "answer": 1,
         "sim": {"kind": "particle-states",
                 "controls": ["temperature"],
                 "readouts": ["state", "number of particles"],
                 "caption": "The particle counter never changes. Only the "
                            "arrangement and the speed do."},
         "reveal": "They break out of their fixed places and start sliding past "
                   "each other. Now check the particle counter before and after: "
                   "the number never changes. That is exactly why the mass never "
                   "changes either."},
        {"id": "state-change-cards", "kind": "reveal-cards",
         "demand": "recall",
         "prompt": "Every arrow on that map has a name. Say the name out loud, "
                   "then tap to check it.",
         "cards": [
             {"front": "Solid → liquid", "back": "Melting"},
             {"front": "Liquid → solid", "back": "Freezing"},
             {"front": "Liquid → gas", "back": "Evaporating"},
             {"front": "Gas → liquid", "back": "Condensing"},
             {"front": "Solid → gas, with no liquid in between",
              "back": "Sublimation"},
             {"front": "The total stays the same — nothing gained, nothing lost",
              "back": "Conserved"},
         ]},
        {"id": "mass-fifa", "kind": "worked-example",
         "demand": "model the calculation before asking for it (Law 5)",
         "prompt": "Watch this one set out in full, because you do the next one. "
                   "A sealed flask holds 24.0 g of ice. It is left until all the "
                   "ice has melted. What is the mass of water?",
         "fifa": {
             "formula": "mass before = mass after  (mass is conserved)",
             "insert":  "mass before = 24.0 g",
             "fix":     "no particles enter or leave a sealed flask",
             "answer":  "24.0 g"}},
        {"id": "mass-fifa-do", "kind": "construct",
         "demand": "the same artifact, produced by the student (Law 5)",
         "prompt": "Your turn, same four steps. A sealed tube holds 18.5 g of "
                   "solid iodine. It is warmed until it has all sublimed to a "
                   "purple gas. What is the mass of gas? Set it out as Formula, "
                   "Insert, Fix, Answer.",
         "success": ["States that mass is conserved",
                     "Inserts 18.5 g",
                     "Answer 18.5 g with units",
                     "Notes the tube is sealed"]},
        {"id": "sort-melting-dissolving", "kind": "classify",
         "demand": "elicit PART-06",
         "prompt": "Two words students mix up constantly. Sort these: ice in a "
                   "warm room; sugar in tea; chocolate in your hand; salt in "
                   "water.",
         "options": ["Melting", "Dissolving"],
         "reveal": "Ice and chocolate melt — one substance, heated. Sugar and "
                   "salt dissolve — two substances, mixed.",
         "targets": "PART-06"},
        {"id": "two-routes-compare", "kind": "confrontation",
         "demand": "separate two ideas students routinely merge",
         "prompt": "Say the wrong idea out loud: 'sugar melts in tea.' Sugar in "
                   "tea and ice in a warm room both look like disappearing. Are "
                   "they the same change?",
         "reveal": "No — and 'sugar melts in tea' is wrong twice over. Melting "
                   "needs heat and involves one substance on its own. Dissolving "
                   "needs a second substance, the liquid, and works perfectly "
                   "well in cold tea. Sugar in tea dissolves; it does not melt.",
         "targets": "PART-06"},
        {"id": "what-is-in-the-bubble", "kind": "predict",
         "demand": "elicit PART-07",
         "prompt": "One more disappearing act, and it needs the same idea. Water "
                   "is boiling hard. What is inside the bubbles?",
         "options": ["Air, pulled down from above the water",
                     "Nothing — the bubbles are empty",
                     "Water itself, now a gas"],
         "answer": 2,
         "reveal": "Water itself, now a gas. The liquid is turning into gas "
                   "inside the bubble — evaporation happening all through the "
                   "water, not just at the top.",
         "targets": "PART-07"},
        {"id": "bubble-reveal", "kind": "construct",
         "demand": "transfer the conservation idea to a new observation",
         "prompt": "Push it one step further. If those bubbles really were air, "
                   "where would the air have come from in a sealed flask that "
                   "had already been boiled once?",
         "success": ["Recognises there is no source of air in a sealed, "
                     "already-boiled flask",
                     "Concludes the bubbles must be the water itself, as gas",
                     "Says no particles were created — they only changed state"],
         "targets": "PART-07"},
        {"id": "run-it-backwards", "kind": "construct",
         "demand": "transfer the reversibility idea to an everyday case",
         "prompt": "Steam meets a cold window and turns into drops of water. "
                   "Name that change, then name the change that would undo it.",
         "success": ["Names condensing",
                     "Names evaporating (or boiling) as the reverse",
                     "Says it is the same substance both ways",
                     "Says the mass of water is unchanged"]},
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
        "prompt": "You already know gas particles are far apart and moving fast. "
                  "Here is what that lets them do. A marshmallow sits in a "
                  "sealed jar. Air is pumped out of the jar and the marshmallow "
                  "swells up. Air is let back in and it shrivels.",
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

    # MODEL rhythm (§6): lead → flagship parameter instrument with predict-gates
    # at each regime change → property blocks anchored back to the model →
    # ladder. The marshmallow bookends the page: answered briefly at block 3,
    # produced in full by the student at block 12.
    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "check", "id": "what-causes-pressure"},
        {"type": "explainer", "id": "collisions-make-pressure",
         "text": "Gas particles move fast in every direction. Each time one hits "
                 "a wall it gives that wall a tiny push. There are so many hits "
                 "each second that they add up to one steady push. That push is "
                 "gas pressure. So the marshmallow has gas pushing out from "
                 "inside. It has air pushing in from outside. Pump the outside "
                 "air away and the inside push has nothing left to balance it. "
                 "So the marshmallow swells."},
        {"type": "figure", "ref": "c1-gas-pressure-collisions"},
        {"type": "misconception", "id": "collision-count-sim", "targets": "PART-08"},
        {"type": "keyword", "terms": ["pressure", "collision"]},
        {"type": "check", "id": "predict-heated-can"},
        {"type": "misconception", "id": "speed-not-size", "targets": "PART-09"},
        {"type": "practical", "id": "pressure-sim"},
        {"type": "check", "id": "pressure-cards"},
        {"type": "figure", "ref": "c1-vacuum-marshmallow"},
        {"type": "check", "id": "explain-marshmallow"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "temperature-and-pressure",
         "text": "Heating does two jobs at once. Most answers only mention one "
                 "of them. Faster particles reach the walls more often. They "
                 "also arrive harder, because they are moving faster when they "
                 "land. Both of those raise the pressure. And not one extra "
                 "particle was added to do it."},
        {"type": "check", "id": "aerosol-warning"},
    ],

    "support": [],

    "activities": [
        {"id": "what-causes-pressure", "kind": "predict",
         "demand": "elicit PART-08",
         "prompt": "Commit first. What causes the pressure inside a blown-up "
                   "balloon?",
         "options": ["The particles pushing against each other",
                     "The particles hitting the balloon wall",
                     "The air inside trying to escape"],
         "answer": 1,
         "reveal": "The particles hitting the wall. Gas particles are so far "
                   "apart that they hardly ever touch each other at all.",
         "targets": "PART-08"},
        {"id": "collision-count-sim", "kind": "lab",
         "demand": "investigate",
         "prompt": "The wrong idea, out loud: 'the particles are squashed up "
                   "against each other, and that squashing is what pushes.' "
                   "Predict before you run it — spread the same particles out "
                   "into a bigger box. What happens to the pressure?",
         "options": ["It rises — the particles have more room to move",
                     "It falls — fewer wall hits every second",
                     "It stays the same — same number of particles"],
         "answer": 1,
         "sim": {"kind": "gas-pressure",
                 "controls": ["volume"],
                 "readouts": ["collisions per second", "pressure"],
                 "caption": "Every wall hit adds one to the counter. Watch the "
                            "counter and the pressure gauge move together."},
         "reveal": "The pressure falls. The particles never touched each other "
                   "in either box, so crowding cannot be the cause — and the "
                   "counter and the gauge move together, which tells you what "
                   "is. Pressure is wall hits per second, and nothing else.",
         "targets": "PART-08"},
        {"id": "predict-heated-can", "kind": "predict",
         "demand": "elicit PART-09",
         "prompt": "Now change something else instead. A sealed can of air is "
                   "heated and the pressure inside rises. Why?",
         "options": ["Each particle swells to a bigger size",
                     "Each particle moves faster than before",
                     "Extra particles appear inside the can"],
         "answer": 1,
         "reveal": "They move faster — so they hit the walls more often, and "
                   "harder.",
         "targets": "PART-09"},
        {"id": "speed-not-size", "kind": "confrontation",
         "demand": "separate speed from size",
         "prompt": "Name it: 'heating makes the particles themselves get "
                   "bigger.' Now test it. If every particle really had grown, "
                   "what would happen to the mass of gas in the sealed can?",
         "reveal": "The mass would have to go up — more stuff means more mass — "
                   "but a sealed can cannot gain a single particle, and a "
                   "balance proves it does not. So the particles did not grow. "
                   "Only their speed changed.",
         "targets": "PART-09"},
        {"id": "pressure-sim", "kind": "lab",
         "demand": "investigate",
         "prompt": "Here is the full instrument. Predict first: what happens to "
                   "the pressure if you squash the gas into half the space?",
         "options": ["Pressure halves", "Pressure stays the same",
                     "Pressure doubles"],
         "answer": 2,
         "sim": {"kind": "gas-pressure",
                 "controls": ["volume", "temperature", "particles"],
                 "readouts": ["pressure", "collisions per second"],
                 "caption": "Each wall hit is one push. More hits per second "
                            "means more pressure. Change one control at a time."},
         "reveal": "Squashing the gas into half the space doubles how often the "
                   "particles hit the walls, so the pressure doubles. Now try "
                   "the temperature and the particle count the same way — "
                   "predict first, one control at a time."},
        {"id": "pressure-cards", "kind": "reveal-cards",
         "demand": "recall",
         "prompt": "Three ways to raise the pressure, and one trap. Say why each "
                   "one works before you tap it.",
         "cards": [
             {"front": "Squash the gas into half the space",
              "back": "Same particles, smaller box → twice as many wall hits "
                      "each second → pressure doubles"},
             {"front": "Heat the gas in a sealed can",
              "back": "Particles move faster → they hit the walls more often "
                      "AND harder → pressure rises"},
             {"front": "Pump in twice as many particles",
              "back": "Twice as many particles → twice as many wall hits each "
                      "second → pressure doubles"},
             {"front": "Make each particle bigger",
              "back": "You cannot. Particles never change size — this is the "
                      "trap, not a fourth method."},
         ]},
        {"id": "explain-marshmallow", "kind": "construct",
         "demand": "explain the opening phenomenon with the model just built",
         "prompt": "Back to the marshmallow, this time in full and in your own "
                   "words. Explain why it swelled when the air was pumped out of "
                   "the jar.",
         "success": ["Says the gas inside the marshmallow pushes outwards",
                     "Says fewer particles outside means fewer collisions on "
                     "the outside",
                     "Says the inside push is now greater than the outside push",
                     "Does not say the marshmallow 'gained air'"]},
        {"id": "aerosol-warning", "kind": "construct",
         "demand": "transfer to a safety context",
         "prompt": "Same two effects, somewhere they matter. Explain why an "
                   "aerosol can carries the warning 'do not place on a fire'.",
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
        "prompt": "Gas particles move fast in every direction — that is how "
                  "pressure works. Here is the other thing it lets them do. A "
                  "bottle is opened at the front of a still room. Hands go up "
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

    # MODEL rhythm (§6). Two instruments only, per the §5.1 budget: the
    # random-walk lab is the flagship, the crossing-counter lab is the
    # mid-size. `diffusion-rate-sim` is a do-mode task ON the flagship, not a
    # third instrument.
    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "check", "id": "predict-still-room"},
        {"type": "explainer", "id": "random-movement",
         "text": "Nothing is moving it except the particles themselves. "
                 "Particles in a gas or a liquid never stop moving. They move in "
                 "random directions — no pattern, no aim. Near the open bottle "
                 "the perfume particles are crowded together. So more of them "
                 "happen to drift outwards than inwards. Do that for a few "
                 "minutes and the smell has crossed the room. Nothing pushed it. "
                 "That spreading has a name: diffusion."},
        {"type": "practical", "id": "random-walk-sim"},
        {"type": "check", "id": "why-spread"},
        {"type": "misconception", "id": "both-directions-sim", "targets": "PART-11"},
        {"type": "figure", "ref": "c1-diffusion-gradient"},
        {"type": "keyword", "terms": ["diffusion", "concentration", "random"]},
        {"type": "check", "id": "diffusion-rate-sim"},
        {"type": "figure", "ref": "c1-bromine-jars"},
        {"type": "check", "id": "explain-bromine"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "why-liquids-slower",
         "text": "You will have seen this in the lab above. Diffusion is far "
                 "slower in a liquid than in a gas. Liquid particles already "
                 "touch. So a moving particle is knocked off course almost at "
                 "once. It still gets there. It just takes a very long time."},
        {"type": "check", "id": "predict-temperature"},
    ],

    "support": [],

    "activities": [
        {"id": "predict-still-room", "kind": "predict",
         "demand": "elicit PART-10",
         "prompt": "Commit first. The windows are shut and the air is completely "
                   "still. Will the smell still reach the back row?",
         "options": ["No — with no draught nothing carries it",
                     "Yes — it gets there anyway"],
         "answer": 1,
         "reveal": "It gets there anyway. Nothing carries the particles — they "
                   "carry themselves.",
         "targets": "PART-10"},
        {"id": "random-walk-sim", "kind": "lab",
         "demand": "investigate",
         "prompt": "There is no draught anywhere in this lab. Predict first: "
                   "what path does the one tagged particle take to the far side?",
         "options": ["A straight line towards the empty side",
                     "A long jagged path with no set direction",
                     "It never reaches the far side at all"],
         "answer": 1,
         "sim": {"kind": "diffusion",
                 "controls": ["temperature", "medium"],
                 "readouts": ["tagged particle path",
                              "concentration on each side"],
                 "caption": "One particle is tagged so you can follow it. There "
                            "is no wind, no current and no waft in this "
                            "simulation."},
         "reveal": "A long jagged path. It gets there in the end, but by "
                   "wandering, not by aiming. Nothing pushes it — the knocks it "
                   "takes from other particles are the only thing steering it.",
         "targets": "PART-10"},
        {"id": "why-spread", "kind": "predict",
         "demand": "elicit PART-11",
         "prompt": "Harder question, and it is the one people get wrong. Why do "
                   "more particles end up on the empty side?",
         "options": ["They are trying to spread out evenly, so they head for "
                     "the empty side",
                     "They move randomly, and there are simply more of them on "
                     "the crowded side"],
         "answer": 1,
         "reveal": "The second. No particle knows where it is going, or where "
                   "the empty space is.",
         "targets": "PART-11"},
        {"id": "both-directions-sim", "kind": "lab",
         "demand": "investigate",
         "prompt": "The wrong idea in students' own words: 'the particles want "
                   "to spread out evenly.' Predict before you count — over ten "
                   "seconds, which way do particles cross the middle line?",
         "options": ["Only from the crowded side to the empty side",
                     "Both ways, but more from the crowded side",
                     "Both ways, in exactly equal numbers"],
         "answer": 1,
         "sim": {"kind": "diffusion",
                 "controls": ["temperature"],
                 "readouts": ["crossings left to right",
                              "crossings right to left",
                              "concentration on each side"],
                 "caption": "Two counters, one for each direction. Watch them "
                            "both."},
         "reveal": "Both counters climb the whole time. Particles cross in both "
                   "directions, and more cross from the crowded side only "
                   "because more of them started there. So 'wanting to spread "
                   "out' is wrong twice over: particles have no wants, and the "
                   "movement is not one-way. The even spread is a result of the "
                   "numbers, never a goal.",
         "targets": "PART-11"},
        {"id": "diffusion-rate-sim", "kind": "construct",
         "demand": "run the flagship lab yourself, one variable at a time",
         "prompt": "Go back to the diffusion lab above and drive it yourself. "
                   "Write your prediction down first, then change one control at "
                   "a time: warm the gas, then switch the medium to a liquid.",
         "success": ["A written prediction before each run, not after",
                     "Warmer → faster, because the particles move faster",
                     "Liquid → much slower, because the particles already touch "
                     "and knock each other off course",
                     "Only one control changed at a time"]},
        {"id": "explain-bromine", "kind": "construct",
         "demand": "explain a standard demonstration with the model",
         "prompt": "Now the classic version of the same thing. Brown bromine gas "
                   "sits in the lower jar, air in the upper. The cover is "
                   "removed and after some minutes both jars are pale brown. "
                   "Explain what happened.",
         "success": ["Bromine particles move randomly, with no set direction",
                     "They spread from where they are crowded to where they are "
                     "not",
                     "Air particles move down into the lower jar at the same "
                     "time",
                     "Uses the words diffusion, concentration and random",
                     "Does not say anything blew or pushed the bromine"]},
        {"id": "predict-temperature", "kind": "construct",
         "demand": "transfer to an everyday case",
         "prompt": "Same idea, in a mug. Explain why a teabag colours hot water "
                   "faster than cold.",
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
        "prompt": "Five lessons, one model, and it has explained everything so "
                  "far. Now here is a result it gets wrong. Almost everything "
                  "shrinks when it freezes — the particles settle closer "
                  "together. Water expands. Ice floats.",
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

    # INVESTIGATION rhythm (§6): lead with the ambiguous result → critique
    # before construct → run it in simulation and get messy data → analyse →
    # ladder ending in a designed investigation. The run at block 13 is the
    # test the student designed at block 12, using L5's diffusion instrument.
    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "check", "id": "verdict-vote"},
        {"type": "explainer", "id": "what-models-are-for",
         "text": "Most people vote to keep it. That is the right answer. We "
                 "judge a model by how much it explains. It does not have to be "
                 "a photo of the real thing. This one has explained states, "
                 "changes of state, pressure and spreading. So the job now is "
                 "not to defend it. The job is to find where it stops working."},
        {"type": "figure", "ref": "c1-ice-water-density"},
        {"type": "practical", "id": "model-scorecard"},
        {"type": "misconception", "id": "model-limits-sort", "targets": "PART-12"},
        {"type": "figure", "ref": "c1-model-scorecard"},
        {"type": "keyword", "terms": ["evidence", "anomaly", "peer review"]},
        {"type": "check", "id": "word-flip"},
        {"type": "check", "id": "predict-history"},
        {"type": "misconception", "id": "model-history-timeline", "targets": "PART-13"},
        {"type": "check", "id": "design-a-test"},
        {"type": "practical", "id": "run-your-test"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "the-ice-anomaly",
         "text": "So what is water doing? As it freezes, its particles lock "
                 "into an open, cage-like pattern. That pattern takes up more "
                 "room than the jumbled liquid did. So ice floats. Pipes burst "
                 "in winter. Ponds freeze from the top down — and that is what "
                 "lets fish live through to spring."},
        {"type": "check", "id": "anomaly-consequences"},
    ],

    "support": [],

    "activities": [
        {"id": "verdict-vote", "kind": "predict",
         "demand": "elicit PART-12 as a public commitment",
         "prompt": "Vote before you read on, and be honest about it. Water "
                   "expands when it freezes; the simple particle model says "
                   "things should shrink. What should we do with the model?",
         "options": ["Throw the model away — it has been proved wrong",
                     "Keep it, but write down where it fails",
                     "Ignore the water result and move on"],
         "answer": 1,
         "reveal": "Keep it and record the limit. A model that explains a "
                   "hundred things and fails on one is still worth having — as "
                   "long as we are honest about the one.",
         "targets": "PART-12"},
        {"id": "model-scorecard", "kind": "investigation",
         "demand": "judge the model against evidence, before building anything",
         "prompt": "So score it. For each observation, decide: does the simple "
                   "particle model explain it fully, partly, or not at all? "
                   "Squashing a gas · a smell crossing a room · ice floating · "
                   "why a solid keeps its shape · why water boils at exactly "
                   "100 °C at sea level.",
         "success": ["Each verdict justified by reference to the model",
                     "Identifies ice floating as the clear failure",
                     "Notices the model does not predict specific temperatures"]},
        {"id": "model-limits-sort", "kind": "confrontation",
         "demand": "replace 'true/false' with 'useful within limits'",
         "prompt": "The wrong idea, stated plainly: 'a model is either true or "
                   "false, and one exception proves it false.' Now sort your own "
                   "scorecard into two piles — 'the model explains this' and "
                   "'the model needs more detail here'.",
         "reveal": "Neither pile came out empty, and that is the whole point. A "
                   "model is not true or false; it is useful within limits. One "
                   "exception does not destroy it — it marks its boundary. And "
                   "knowing exactly where the boundary lies makes a model more "
                   "useful, not less.",
         "targets": "PART-12"},
        {"id": "word-flip", "kind": "reveal-cards",
         "demand": "recall",
         "prompt": "Three words this lesson depends on. Say the word before you "
                   "tap the card.",
         "cards": [
             {"front": "One reading sits nowhere near the pattern the others "
                       "make",
              "back": "An anomaly"},
             {"front": "Other scientists check your result before it is "
                       "accepted",
              "back": "Peer review"},
             {"front": "The observations and measurements you use to decide "
                       "whether an idea works",
              "back": "Evidence"},
         ]},
        {"id": "predict-history", "kind": "predict",
         "demand": "elicit PART-13",
         "prompt": "One more question, about scientists rather than particles. "
                   "Has the scientific picture of the particle stayed the same "
                   "since it was first suggested?",
         "options": ["Yes — once scientists agreed, it was settled",
                     "No — it has been changed several times since"],
         "answer": 1,
         "reveal": "It has been changed several times, and every change came "
                   "from new evidence arriving.",
         "targets": "PART-13"},
        {"id": "model-history-timeline", "kind": "confrontation",
         "demand": "show theory change as normal, not as failure",
         "prompt": "Say the wrong idea out loud: 'once scientists agree on "
                   "something, it never changes again.' Now place these three "
                   "pictures of the particle on a timeline: tiny solid balls · "
                   "balls with charges inside them · mostly empty space.",
         "reveal": "All three were the accepted picture in their day. Each one "
                   "was published, checked by other scientists — that is peer "
                   "review — and then modified when evidence arrived that it "
                   "could not explain. Changing a model is not scientists being "
                   "wrong. It is science working exactly as it is supposed to.",
         "targets": "PART-13"},
        {"id": "design-a-test", "kind": "construct",
         "demand": "design an investigation — the top of the ladder",
         "prompt": "Last job, and it is the real one. Design a test to find out "
                   "whether diffusion is faster in hot water than in cold. State "
                   "your variables.",
         "success": ["Independent variable: temperature of the water",
                     "Dependent variable: time for colour to spread a set "
                     "distance",
                     "Names at least two control variables",
                     "Says how the result would be measured, not just observed"]},
        {"id": "run-your-test", "kind": "lab",
         "demand": "investigate",
         "prompt": "Now run the test you just designed, on the diffusion lab "
                   "from last lesson. Predict first: how much faster is "
                   "diffusion in hot water than in cold?",
         "options": ["Exactly twice as fast, every single time",
                     "Faster, but not by a fixed neat number",
                     "No faster — temperature does not affect it"],
         "answer": 1,
         "sim": {"kind": "diffusion",
                 "controls": ["temperature", "medium"],
                 "readouts": ["time to spread 5 cm",
                              "concentration on each side"],
                 "caption": "Set the temperature, run it, and read the time. Run "
                            "each temperature more than once."},
         "reveal": "Faster — but the times come out messy. Run the same "
                   "temperature twice and you will not get the same number. That "
                   "is what real data looks like, and it is why scientists "
                   "repeat readings before they trust a result, and why one odd "
                   "reading is an anomaly to investigate rather than proof of "
                   "anything."},
        {"id": "anomaly-consequences", "kind": "construct",
         "demand": "transfer an anomaly to its real-world consequences",
         "prompt": "One anomaly, and a pond full of consequences. Explain why "
                   "ponds freeze from the top down, and why that matters to the "
                   "animals in them.",
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
