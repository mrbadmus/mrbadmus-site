"""C4 L2 — Reactions rearrange atoms (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c4/c4-02-reactions-rearrange-atoms.dc.html` (725
lines), and her author's notes `docs/ks3/design-reference/c4/NOTES-C4.md` §1,
§2, §3, §5 flags 6, 7 and 8, §6 (`REACT-03`, `REACT-04`) and §7.

Every student-facing string is byte-identical to the approved page except
where a comment below says otherwise and says why. `RAIL`, `EL`, `REACTIONS`,
`ASKS`, `RUNGS` and `SELF_RUNGS` came out of the node extractor; the hook
options and reveal, both explainer paragraphs, the three stage names, the
three stage texts, the three `role="img"` labels, the atom-count table's
headings, the two advance labels, "Put it back", the all-done summary, the key
fact, the `#s-think` options and its two reveal paragraphs, the key note and
both "Going further" paragraphs were lifted from `lessonVals(s)` and from the
markup, which is where roughly half this lesson's words live and where a lift
of the top-level constants alone silently loses them.

── The lesson in one line ──────────────────────────────────────────────

A reaction breaks joins and makes new ones, and it can only ever use the atoms
it was given. The page teaches that twice: the rearranger shows it happening,
and the impossible-product panel shows what follows when you ask for something
the atoms cannot spell.

── THE LOOSE-ATOM STAGE IS HONEST ABOUT BEING UNREAL, AND THAT IS THE POINT ──

Stage 1 draws every join broken and nothing else done, and its own text says
"This stage is not real — no chemist ever sees it". NOTES §2 names that honesty
as the reason the stage exists: it is the only view in which the atom budget is
visible as a countable set of objects, and pretending it were a real moment in
a real reaction would buy a tidier story at the cost of the one true thing the
picture is for. It stays whole, and no later sentence on the page retracts it
(§7 / MRB-225).

── FORMULAE ARE `formula`, NOT A FLAT STRING (⊕ deviation, reported) ────

Design writes each particle's name as a flat `label: 'H2O'`. This record
authors `formula: [("H", 2), ("O", 1)]` instead, for two reasons that both
matter more than the extra bracket:

  1. C4 standardises on REAL `<sub>` elements — NOTES §3 says so for `c4-05`
     ("`parts: [{sym, sub}]` … the convention this unit standardises on"), and
     `ks3_art/kit.py`'s 20 Aug ruling admitting `<sub>` to `rich()` cites C4 by
     name as the reason. `H2O` rendered flat here and `H₂O` rendered properly
     three lessons later is drift inside one unit.
  2. It makes a CONTENT-TRUTH ASSERTION possible. `r_atom_rearranger` expands
     every formula and checks it against that particle's own `atoms[]`, then
     tallies both sides of every reaction and checks the tally against
     `counts[]`. Conservation of atoms IS this lesson, so a payload in which it
     silently failed would be the one defect this instrument cannot carry. The
     check walks every particle and every element, not a sample.

── THE ELEMENT COLOUR TABLE IS ONE TABLE (NOTES §3) ────────────────────

`_EL` below is Design's `EL`, verbatim, plus the element's full NAME — which
the count-table assertion needs and which is on the page anyway ("Hydrogen",
"Oxygen", "Magnesium", "Carbon"). NOTES §3 asks for one table "so that C8 and
every KS4 bonding lesson can reuse it". It lives here because a lane may not
write a shared file; when C8 arrives it should be PROMOTED (to `ks3_art/kit.py`
or to `shared/tokens.css` as `--ks3-el-*`) rather than copied. Flagged to the
commander.

⚑ For Mide's science gate, from Design's NOTES §5 — all three answered in the
  build brief and applied here:
  * flag 6 — the hydrogen + oxygen balloon hook. CONFIRMED, KEPT whole. There
    is no method and no quantity anywhere in this file, and there must not be
    one.
  * flag 7 — nuclear transmutation named as "not chemistry", twice (the
    `#s-think` reveal and rung 4's fifth criterion). CONFIRMED, BOTH KEPT. The
    hedge is the true version: changing one element into another does happen,
    it is nuclear, and it is not a chemical reaction. Teaching "elements never
    change" flat would be the famous version, and rung 4 would then credit a
    sentence the lesson had told the student was true (MRB-225, §7).
  * flag 8 — bond breaking costs energy, bond making gives it back.
    CONFIRMED CORRECT and beyond statutory. It stays as PROSE in `stretch`
    with nothing assessed on it: no rung, no gate option and no question in
    the bank turns on it.
  * ⚑ ONE THING TO WATCH, RAISED HERE FOR c4-04's AUTHOR. The hook's third
    clause reads "both weightless in the hand". That is a sensation, not a
    claim about mass, and it is Design's approved copy so it is kept
    byte-identical — but `REACT-07` is "gases have no mass, so a gas escaping
    cannot change a balance reading", and c4-04 is the lesson that confronts
    it. Whoever writes c4-04 should know this sentence is upstream of them.
"""

# ── the element colour table (NOTES §3) ─────────────────────────────────
#
# Design's `EL`, verbatim, plus `name`. `colour` is the chip fill, `ink` the
# symbol on it. ONE TABLE — see the docstring for where it goes when C8 needs
# it. Do not fork it to fix a contrast reading; that is a change to a shared
# decision, not to this lesson.
#
# ⚑ MEASURED AND REPORTED, NOT SILENTLY CHANGED: #FFFDF8 on the oxygen chip's
# #E4572E is 3.64:1, which is below AA for text at 15px. It is Design's own
# value and the table is meant to be reused, so it is kept and flagged. The
# information is not carried by the chip alone — every particle box prints its
# formula underneath, every stage plate carries a `role="img"` label naming
# what is drawn, and the atom-count table names each element in words beside
# its number — so nothing on this page is legible only to a reader who can
# resolve a symbol against that orange.
_EL = {
    "H":  {"colour": "#F3EDE1", "ink": "#1A1714", "name": "Hydrogen"},
    "O":  {"colour": "#E4572E", "ink": "#FFFDF8", "name": "Oxygen"},
    "Mg": {"colour": "#2F5D8A", "ink": "#FFFDF8", "name": "Magnesium"},
    "C":  {"colour": "#1A1714", "ink": "#FFFDF8", "name": "Carbon"},
}

# ── the three reactions (NOTES §3) ──────────────────────────────────────
#
# Design's `REACTIONS`, with `label: 'H2O'` replaced by `formula: [("H", 2),
# ("O", 1)]` — see the docstring. `atoms` is kept exactly as she wrote it and
# is what the picture draws; `formula` is what the caption spells; the renderer
# asserts the two agree, particle by particle.
#
# ⚠️ THE GATES ARE COMMITMENTS, NOT MARKED QUESTIONS. No option carries a
# `correct` flag and nothing green or red ever reaches one. The answer arrives
# as the next stage: press through and `product_text` says what was actually
# built. That is the consequence answering the commitment, which is the only
# marking any instrument in this key stage does.
_REACTIONS = [
    {"id": "water",
     "tab": "Hydrogen + oxygen",
     "words": "hydrogen + oxygen makes water",
     "reactants": [
         {"formula": [("H", 2)], "atoms": ["H", "H"]},
         {"formula": [("H", 2)], "atoms": ["H", "H"]},
         {"formula": [("O", 2)], "atoms": ["O", "O"]},
     ],
     "products": [
         {"formula": [("H", 2), ("O", 1)], "atoms": ["H", "H", "O"]},
         {"formula": [("H", 2), ("O", 1)], "atoms": ["H", "H", "O"]},
     ],
     "counts": [{"el": "Hydrogen", "n": 4}, {"el": "Oxygen", "n": 2}],
     "gate": {
         "q": "The loose atoms are on the table. How many oxygen atoms will "
              "be in the water you make?",
         "options": [
             "One — water only needs one",
             "Two — the same two that were there",
             "Four — one for each hydrogen",
         ]},
     "product_text": "Two water particles, each one oxygen atom joined to two "
                     "hydrogen atoms. Four hydrogens and two oxygens, exactly "
                     "as before — and a liquid, from two gases."},

    {"id": "mgo",
     "tab": "Magnesium + oxygen",
     "words": "magnesium + oxygen makes magnesium oxide",
     "reactants": [
         {"formula": [("Mg", 1)], "atoms": ["Mg"]},
         {"formula": [("Mg", 1)], "atoms": ["Mg"]},
         {"formula": [("O", 2)], "atoms": ["O", "O"]},
     ],
     "products": [
         {"formula": [("Mg", 1), ("O", 1)], "atoms": ["Mg", "O"]},
         {"formula": [("Mg", 1), ("O", 1)], "atoms": ["Mg", "O"]},
     ],
     "counts": [{"el": "Magnesium", "n": 2}, {"el": "Oxygen", "n": 2}],
     "gate": {
         "q": "Two magnesium atoms and two oxygen atoms are loose. How many "
              "magnesium oxide units can you build?",
         "options": ["One", "Two", "Four"]},
     # ⚑ This sentence is science flag 5's sibling and it is the mass argument
     # in one line, three lessons before c4-04 makes it quantitative. Kept
     # whole: "weighs more than the ribbon did — because the oxygen atoms came
     # from the air" is the version that is true, and the version that stops
     # "burning destroys matter" before it starts.
     "product_text": "Two magnesium oxide units, each one magnesium joined to "
                     "one oxygen. The white powder weighs more than the "
                     "ribbon did — because the oxygen atoms came from the air "
                     "and are now part of it."},

    {"id": "methane",
     "tab": "Methane + oxygen",
     "words": "methane + oxygen makes carbon dioxide + water",
     "reactants": [
         {"formula": [("C", 1), ("H", 4)],
          "atoms": ["C", "H", "H", "H", "H"]},
         {"formula": [("O", 2)], "atoms": ["O", "O"]},
         {"formula": [("O", 2)], "atoms": ["O", "O"]},
     ],
     "products": [
         {"formula": [("C", 1), ("O", 2)], "atoms": ["C", "O", "O"]},
         {"formula": [("H", 2), ("O", 1)], "atoms": ["H", "H", "O"]},
         {"formula": [("H", 2), ("O", 1)], "atoms": ["H", "H", "O"]},
     ],
     "counts": [{"el": "Carbon", "n": 1}, {"el": "Hydrogen", "n": 4},
                {"el": "Oxygen", "n": 4}],
     "gate": {
         "q": "One carbon, four hydrogens and four oxygens are loose. Which "
              "set of products uses all of them exactly?",
         "options": [
             "One carbon dioxide and one water",
             "One carbon dioxide and two waters",
             "Two carbon dioxides and two waters",
         ]},
     "product_text": "One carbon dioxide and two waters — and every one of the "
                     "nine atoms is used, with none left over and none "
                     "invented. This is what a gas hob does, several times a "
                     "second."},
]

# ── the impossible-product bench (NOTES §2) ─────────────────────────────
#
# ⚖️ **THE REFUSAL BRANCHES ON WHICH ATOMS ARE PRESENT, AND ON NOTHING ELSE.**
# Design's payload carries `possible: true/false` per ask. That flag is a
# PROXY: it is the answer written down beside the question, and an instrument
# that reads it is one where the chemistry and the verdict are two independent
# facts free to disagree. §5A forbids exactly that.
#
# So `possible` is NOT authored here. Each ask declares `needs` — the elements
# the product is built from — and `r_impossible_ask` derives the verdict by
# asking whether every one of them is on `table`. Ammonia is refused because
# there is no N on the table; gold because there is no Au. Both refusals are
# the same test with different atoms in it, which is the sentence the lesson
# is trying to leave behind.
#
# The derivation is also what names each verdict panel: a possible ask gets
# `id="ask-<id>-verdict"`, a refused one `id="ask-<id>-refusal"`. The id is
# therefore evidence of which branch the atoms produced, not a label somebody
# typed. `ask-gold-refusal` is where `REACT-04` is confronted.
_ASK_TABLE = ["H", "O"]

_ASKS = [
    {"id": "water", "label": "Water", "needs": ["H", "O"],
     "title": "Built. Two hydrogens and one oxygen, and you had both.",
     "text": "Everything water needs was on the table. That is the only "
             "condition a reaction has to meet."},
    {"id": "peroxide", "label": "Hydrogen peroxide", "needs": ["H", "O"],
     "title": "Built — and it is a different substance from water.",
     "text": "Two hydrogens and two oxygens. Same two elements as water, one "
             "extra oxygen atom, and a substance that bleaches hair rather "
             "than quenching thirst. The atoms decide, and so does how many "
             "of them."},
    {"id": "ammonia", "label": "Ammonia", "needs": ["N", "H"],
     "title": "Refused. There is no nitrogen on this table.",
     "text": "Ammonia is nitrogen joined to three hydrogens, and nothing in "
             "either balloon contains a nitrogen atom. No reaction can make "
             "one — atoms are not created. If you want nitrogen in your "
             "product, you have to put nitrogen in your reactants."},
    # ⚑ `REACT-04`'s confrontation. The button is `id="ask-gold"` and this
    # panel is `id="ask-gold-refusal"`; both are emitted by
    # `r_impossible_ask` and both are named in `misconceptions` below.
    {"id": "gold", "label": "Gold", "needs": ["Au"],
     "title": "Refused, and not because the bench is not trying hard enough.",
     "text": "Gold is an element. The only way to have gold atoms at the end "
             "is to have had gold atoms at the start. Fifteen hundred years "
             "of alchemy is the evidence, and this rule is why it never "
             "worked."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 209 character for character.
    "slug":        "reactions-rearrange-atoms",
    "title":       "Reactions rearrange atoms",
    "discipline":  "chemistry",
    "unit":        "chemical-reactions",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # NOTES §1 gives c4-01 and c4-02 the two halves of `KS3.C.CR.01`: what
    # counts as a reaction, then what a reaction DOES to the atoms. The clauses
    # are already minted in `ks3_data/substatements.py` with the reasoning;
    # this is clause `b`, the rearrangement half.
    "covers":      ["KS3.C.CR.01b"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 3},
                    {"id": "particles", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # The page's "Before this lesson" card links to c4-01. Nothing here works
    # until "a new substance appeared" already means something.
    "requires":    ["chemical-vs-physical-change"],
    "assumes":     [],
    "references":  [],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "A new substance appears where two old ones were. Nothing "
                    "was added and nothing left — so what actually happened?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, Design's `RAIL` in her order with her ids and her `short`
    # labels. `done_when` restates the page's own `DONE()`: the hook on a
    # commitment; the rearranger when every reaction has been carried to its
    # products (`Object.keys(s.done).length >= REACTIONS.length`); the ask
    # bench on any one ask (`s.ask !== null`); `#s-think` on a commitment; the
    # ladder when both marked rungs are answered and both self-marked rungs
    # checked.
    #
    # MRB-208: credit is a RATCHET and nothing is ticked on load. Both
    # instruments ship `data-stage-done="0"`.
    "rail": [
        {"anchor": "s-hook",       "short": "HOOK",   "label": "Two balloons",
         "done_when": "committed"},
        {"anchor": "s-rearr",      "short": "ATOMS",  "label": "Take it apart",
         "done_when": "all_three_reactions_rebuilt"},
        {"anchor": "s-impossible", "short": "RULE",   "label": "Break the rule",
         "done_when": "one_product_asked"},
        {"anchor": "s-think",      "short": "THINK",  "label": "New atoms?",
         "done_when": "committed"},
        {"anchor": "s-ladder",     "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚑ Science flag 6, CONFIRMED and kept whole. A teacher may well
    # demonstrate this; the page gives no method, no volumes and no ratio, and
    # adding any of the three would turn a hook into an instruction.
    #
    # `kind` is unread by the generator (it dispatches on which media key is
    # present) and is authored for consistency with C1, C2 and C3.
    "phenomenon": {
        "kind": "narrative",
        "title": "Two invisible gases. Set fire to them and you get something "
                 "you can drink.",
        "prompt": "Hydrogen in one balloon, oxygen in another. Both "
                  "colourless, both weightless in the hand, neither of them "
                  "wet. Light them and what condenses on the cold glass "
                  "afterwards is water.",
        "commit": "Where did the water come from?",
        # MRB-177 checked: 7 / 9 / 8 / 6 words. The right answer (C) is not
        # the longest, and each wrong option is a wrong rule about where
        # matter comes from — made by the flame, hidden all along, or one kind
        # of atom turning into another.
        "options": [
            "The flame made it out of the heat",
            "It was hidden in the balloons all along as water",
            "The same atoms, joined together in a new way",
            "Hydrogen atoms turned into water atoms",
        ],
        "reveal": "Nothing arrived and nothing left. The same atoms that were "
                  "in the two balloons are in the water — hydrogen atoms and "
                  "oxygen atoms, joined up differently. <strong>A reaction "
                  "does not make new matter. It rearranges the matter it is "
                  "given.</strong> Every reaction you will ever meet is that "
                  "sentence with different atoms in it.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ BOTH JOINS RESOLVE AGAINST MARKUP THIS PAGE ACTUALLY EMITS (MRB-244 /
    # MRB-248), and both differ slightly from the name NOTES §6 proposes.
    # Reported to the commander; the reasoning is here so it is not re-argued:
    #
    #  * `REACT-03` — NOTES proposes `think-commit-mgo-atom` /
    #    `think-reveal-no-such-atom`. The first is this lesson's `#s-think`
    #    activity id and is emitted as `data-activity="think-commit-mgo-atom"`.
    #    The second names the REVEAL PANEL, and `build_ks3.py` emits that panel
    #    as `<div class="ks3-reveal ks3-reveal-panel" hidden data-reveal>` with
    #    no id at all — the engine has never given a confrontation's reveal an
    #    id, and a lane may not change the engine to mint one. So
    #    `confronted_by` names the ACTIVITY that owns both the commitment and
    #    the reveal, which is C3's `MIX-06` precedent exactly. It is also what
    #    keeps Law 3 satisfied: `verify_ks3.py` requires at least one
    #    `confronted_by` to be a real activity id, and this is it.
    #  * `REACT-04` — NOTES proposes `ask-gold` / `ask-refusal`. `ask-gold` is
    #    emitted verbatim, on the gold button. `ask-refusal` cannot be, because
    #    TWO asks are refused and an id is unique; the refusal that confronts
    #    "new atoms can be made if the conditions are right" is gold's, so the
    #    join names `ask-gold-refusal`. The suffix is derived from the atoms
    #    (see `_ASKS` above), not typed.
    #
    # ⚑ `REACT-03` IS `ATOM-01` GROWN UP — NOTES §6 says so, and C2's register
    # already carries `ATOM-01` ("an atom of a substance has the properties of
    # the substance — a copper atom is orange and conducts"), elicited and
    # confronted on `the-atom-daltons-model`. This is a CROSS-REFERENCE, not a
    # re-mint: an atom that carries its substance's properties becomes an atom
    # that BECOMES another substance, and the `#s-think` reveal below names the
    # copper case out loud so the two lessons join in the student's head as
    # well as in the register.
    #
    # `statement` is the line the PAGE quotes where the page quotes one —
    # `r_confrontation` prints it — so `REACT-03` carries Design's `#s-think`
    # quote rather than the register's shorter handle. `REACT-04` is never
    # quoted on the page, so it carries the register's wording.
    "misconceptions": [
        {"id": "REACT-03",
         "statement": "When magnesium burns, the magnesium atoms turn into "
                      "magnesium oxide atoms.",
         "elicited_by": "think-commit-mgo-atom",
         "confronted_by": "think-commit-mgo-atom"},
        {"id": "REACT-04",
         "statement": "New atoms can be made if the conditions are right.",
         "elicited_by": "ask-gold",
         "confronted_by": "ask-gold-refusal"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Page lines 105–107. Design draws ONE `.ks3-explainer` holding two
        # paragraphs; `r_explainer` emits one `<p>` per block, so this is two
        # blocks. Both must stay direct children of `.ks3-lesson` (R11's
        # reading measure), which they are.
        {"type": "explainer",
         "text": "Atoms are joined together in the substances you start with. "
                 "A chemical reaction <strong>breaks those joins and makes "
                 "different ones</strong>. The atoms are not changed, created "
                 "or destroyed — they are the same atoms throughout, and only "
                 "their partners are new."},
        {"type": "explainer",
         "text": "That is why a new substance can appear out of two old ones, "
                 "and why the atom count on each side is always identical. It "
                 "has to be. There is nowhere else for an atom to come from."},

        # ── #s-rearr — the flagship's first half ───────────────────────────
        # A light `ks3-block` → segment `check`. Measured off Design's markup:
        # `class="ks3-block"` and nothing else. There is no ink-dark practical
        # block anywhere in C4.
        {"type": "atom-rearranger", "id": "atom-rearranger", "anchor": "s-rearr",
         "eyebrow": "Your turn · take a reaction apart",
         "heading": "Break the joins, count the atoms, make the new joins",
         "demand": "investigate",

         "elements": _EL,
         "reactions": _REACTIONS,
         # NOTES §3's payload carries the component's stage. It is 0 at rest
         # and the renderer refuses anything else: a page that opened at stage
         # 1 would show a broken-joins picture nobody had asked for, and the
         # resting DOM would disagree with the first thing a student does.
         "stage": 0,

         "tabs_label": "The reaction",
         "count_label": "Atom count",
         "count_headings": {"atom": "Atom", "before": "Before",
                            "after": "After"},
         # What the "After" column reads before the products exist. An em
         # dash, not a zero: nothing has been counted yet, and a zero would
         # claim something has.
         "count_pending": "—",

         "stage_names": [
             "Before · the substances you start with",
             "The joins are broken · loose atoms on the table",
             "After · the new substances",
         ],
         # ⚑ STAGE 1'S TEXT IS THE HONESTY, AND IT IS NOT NEGOTIABLE. See the
         # module docstring. "This stage is not real — no chemist ever sees
         # it" is the sentence that makes the budget argument honest rather
         # than a cartoon, and the last clause is what the gate under it asks
         # the student to use.
         "stage_texts": [
             "Each box is one particle of a starting substance, and the atoms "
             "inside it are joined together. Nothing has happened yet.",
             "Every join has been broken and nothing else has been done. This "
             "stage is not real — no chemist ever sees it — but it is the "
             "honest way to see what a reaction has to work with. Count what "
             "is on the table: that is your entire budget.",
             # Stage 2's text is each reaction's own `product_text`. There is
             # no third string here, because there is no third string on the
             # page.
         ],
         # The `role="img"` label on the stage plate, per stage. `{n}` is the
         # NUMBER OF PARTICLES and is filled by the renderer from the payload
         # — §5A forbids hard-coding a figure the instrument computes, and
         # these two numbers differ per reaction and per stage.
         "stage_labels": [
             "A particle diagram of the reactants: {n} separate particles, "
             "each drawn as its atoms joined inside one outline.",
             "The same atoms, all separate, with no joins between any of "
             "them.",
             "A particle diagram of the products: {n} new particles, built "
             "from exactly the same atoms.",
         ],
         # Two labels, one button. Which one shows is the stage, so neither is
         # composed at run time.
         "advance_labels": ["Break the joins", "Make the new joins"],
         "reset_label": "Put it back",
         "summary": "All three reactions taken apart, and the atom count came "
                    "out identical every time — because at the loose-atom "
                    "stage there was nothing to add and nothing to take away. "
                    "Whatever the products turn out to be, they can only be "
                    "built from the atoms on the table."},

        # ── #s-impossible — the flagship's second half (NOTES §2) ──────────
        # Light `ks3-block` → `check`. This is where balancing is born three
        # lessons later: once "a reaction can only use the atoms it was given"
        # is a rule with teeth, counting them on both sides is the obvious
        # next question rather than an arbitrary exercise.
        {"type": "impossible-ask", "id": "impossible-product-ask",
         "anchor": "s-impossible",
         "eyebrow": "The rule has teeth · try to break it",
         "heading": "Ask the bench for a product it cannot build",
         "prompt": "You have hydrogen and oxygen on the table and nothing "
                   "else. Pick something for the bench to make.",
         "demand": "investigate",
         "table": _ASK_TABLE,
         "asks": _ASKS},

        {"type": "key-fact", "ref": "atoms-rearranged"},

        {"type": "misconception", "id": "think-commit-mgo-atom",
         "anchor": "s-think", "targets": "REACT-03"},

        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # EMPTY, and deliberately. NOTES §7: five instruments, all DOM, no canvas
    # and no drawn figure in the unit. The particle pictures on this page are
    # the rearranger's own stages — an INSTRUMENT, with a demand and a
    # commitment, not a diagram — so authoring them a second time as a `drawn`
    # figure would put the same atoms on the page twice and give the parity
    # gate two drawings to keep in step.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "atoms-rearranged",
         "text": "A chemical reaction breaks the joins between atoms and "
                 "makes new ones. The atoms themselves are unchanged, and "
                 "there are exactly as many of each kind afterwards as there "
                 "were before.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # `#s-think` only. The two instruments are lifted out of `core` into this
    # list by `_normalise()` and are never authored here.
    "activities": [
        # ⚑ `REACT-03`, elicited and confronted. `ATOM-01` grown up — see the
        # misconceptions note above.
        #
        # ⊕ ONE STRING IS NOT DESIGN'S, AND THIS IS THE FLAG (§13). Option D
        # read "Wrong — the magnesium atoms are destroyed" (7 tokens) against
        # the right answer's 12, with the other two at 7 and 8. By the MRB-177
        # measure that is a tell: 12 − 8 = 4, which is the threshold exactly.
        #
        # ⚠️ THE GATE WOULD NOT HAVE CAUGHT IT. `length_tell` needs an
        # `answer` index, and a predict authors none — ONLY THE LADDER MARKS,
        # so there is no answer key here and never will be. The tell is real
        # to a student all the same: they scan four lines, one is half as long
        # again as the rest, and it is the right one. Checked by hand, as §13
        # asks.
        #
        # FIXED AT THE DISTRACTOR, as the ruling requires — the correct option
        # is untouched, no option was reordered, and D now says where the
        # atoms are supposed to have gone, which is the wrong rule a student
        # actually holds ("burning destroys it"). Longest distractor is now 10
        # against the right answer's 12: no tell by either sub-condition.
        {"id": "think-commit-mgo-atom",
         "kind": "predict",
         "demand": "explain",
         "targets": "REACT-03",
         "prompt": "It sounds right, and it uses the right words in the right "
                   "order. Commit before you read on.",
         "options": [
             "Right — that is what burning does",
             "Wrong — there is no such thing as a magnesium oxide atom",
             "Right, because the powder is a new substance",
             "Wrong — the magnesium atoms are destroyed in the flame",
         ],
         # ⚑ Science flag 7, first of two. The hedge in the last sentence is
         # the point: transmutation is real, it is nuclear, and it is not
         # chemistry. Kept exactly.
         "reveal": [
             "There is no such thing as a magnesium oxide atom. Magnesium "
             "oxide is a <strong>compound</strong>, built from magnesium "
             "atoms and oxygen atoms held together — and both kinds of atom "
             "are still exactly what they were. Nothing in the flame changed "
             "one element into another; the periodic table has not been "
             "edited.",
             "This is the same idea as thinking a copper atom is orange and "
             "conducts. <strong>An atom does not carry the properties of the "
             "substance it ends up in.</strong> Turning one element into "
             "another is possible, but not with a Bunsen burner and not in "
             "chemistry — it takes a nuclear reaction, and that is a "
             "different subject.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Design's RUNGS → recall + apply, SELF_RUNGS → explain + produce. Her four
    # rung headings are the engine's own defaults character for character
    # ("Recall", "The one that catches people", "Explain", "Take it somewhere
    # new"), so no rung authors a `title`. `feedback` is keyed by the INT index
    # of each wrong option, which is what `_rung_marked` reads.
    "ladder": {
        # MRB-177 checked: 11 / 9 / 9 / 12 tokens. The correct answer is not
        # the longest, and every distractor is a wrong RULE in the correct
        # answer's own shape — atoms destroyed and made, atoms turned into
        # other atoms, atoms left with the partners they had.
        "recall": {
            "q": "What happens to the atoms during a chemical reaction?",
            "options": [
                "Some atoms are destroyed and new ones are made",
                "The atoms themselves change into different kinds of atom",
                "The atoms stay exactly as they were, joined to the same "
                "partners",
                "The joins between them are broken and new joins are made",
            ],
            "answer": 3,
            "feedback": {
                0: "Atoms are not created or destroyed in a chemical "
                   "reaction. Count them on each side and the numbers match.",
                # ⚑ Science flag 7, second of two. Same hedge, same reason.
                1: "That takes a nuclear reaction, not chemistry. A magnesium "
                   "atom is still a magnesium atom after it burns.",
                2: "Then nothing would have happened. New partners are "
                   "precisely what makes it a reaction.",
            }},

        # ⊕ ONE STRING IS NOT DESIGN'S, AND THIS IS THE FLAG (§13). Option 3
        # read "It depends how much oxygen there is" — 7 tokens against the
        # correct answer's 10, with the others at 7 and 6. The MRB-177 gate
        # measures 10 >= 1.4 x 7, which is true, so this set was a length
        # tell. FIXED AT THE DISTRACTOR by one word: "It depends ON how much
        # oxygen there is", which is 8 tokens and the more natural English
        # anyway. The correct option is untouched, the answer index has not
        # moved, and no correction was edited to make a number work.
        "apply": {
            "q": "Methane burns in oxygen. There are four hydrogen atoms in "
                 "the methane. How many hydrogen atoms are in the products?",
            "options": [
                "Two, because water only has two hydrogens",
                "Four — the same four, now in two water particles",
                "None — they are burnt up",
                "It depends on how much oxygen there is",
            ],
            "answer": 1,
            "feedback": {
                0: "Water has two hydrogens each, and two waters are made. "
                   "Four atoms in, four atoms out.",
                2: "Burning is not disappearing. The hydrogen atoms end up in "
                   "the water that condenses on a cold window above a hob.",
                3: "The oxygen decides whether the reaction can finish, not "
                   "how many hydrogen atoms exist. Those were fixed by the "
                   "methane.",
            }},

        "explain": {
            "q": "A ribbon of magnesium is weighed, burned in air, and the "
                 "white powder left behind is weighed. It is heavier. Explain "
                 "how the powder can be heavier than the ribbon if atoms are "
                 "never created.",
            "field_label": "Your explanation",
            "placeholder": "The magnesium atoms have joined with…",
            "success": [
                "Says the magnesium has joined with oxygen from the air.",
                "Says the oxygen atoms are now part of the powder, so their "
                "mass is included in the reading.",
                "Says no atoms were created — the oxygen atoms already "
                "existed, in the air.",
                "Says the mass of the ribbon plus the mass of the oxygen used "
                "equals the mass of the powder.",
                "Notes that weighing the air is what makes the sum come out "
                "right, and that this is why an open dish seems to gain mass.",
            ]},

        # ⚑ Rung 4 is where `REACT-04` is TESTED rather than confronted, and
        # its fifth criterion is science flag 7 for the third time on this
        # page. It credits a student who says the nuclear route exists — which
        # is why the `#s-think` reveal must keep its hedge: a lesson that told
        # a student elements never change and then marked them right for
        # saying they can would be retracting itself (§7, MRB-225).
        "produce": {
            "q": "A student proposes making gold by reacting two cheap "
                 "substances together, and says the reason nobody has done it "
                 "is that no-one has found the right conditions. Use what you "
                 "know about reactions and atoms to explain why the plan "
                 "cannot work, and what would be needed instead.",
            "field_label": "Your answer",
            "placeholder": "Gold is an element, which means…",
            "success": [
                "Says gold is an element, so it is made of gold atoms only.",
                "Says a reaction can only rearrange the atoms it is given.",
                "Says there is no gold atom in the starting materials, so "
                "there can be none in the products.",
                "Says conditions — heat, pressure, catalyst — change how a "
                "reaction goes, not which atoms exist.",
                "Says making gold from another element means changing the "
                "atoms themselves, which is a nuclear change, not chemistry.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "A chemical reaction breaks the joins between atoms and makes "
                "new ones. The atoms are the same atoms all the way through: "
                "not created, not destroyed, and never changed into other "
                "kinds of atom. So the count of each kind of atom is "
                "identical before and after, and a reaction can only build "
                "products from the atoms it was given.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ Science flag 8 is the first paragraph, CONFIRMED CORRECT and beyond
    # statutory. It stays as PROSE with NOTHING ASSESSED ON IT: no rung, no
    # gate option and no question in `questions_02_reactions_rearrange_atoms.py`
    # turns on bond energetics. The second paragraph is the same idea used to
    # answer a real question a student asks out loud — why the balloon needs a
    # match at all — and it is the honest answer rather than "it needs energy
    # to start", which explains nothing.
    "stretch": [
        {"type": "explainer", "id": "bond-energy",
         "text": "The reason a reaction takes or gives out energy sits exactly "
                 "here. Breaking the joins between atoms always costs energy, "
                 "and making new joins always gives energy back. If the new "
                 "joins give back more than the old ones cost, the surplus "
                 "leaves as heat and the reaction warms its surroundings; if "
                 "they give back less, the reaction takes the difference from "
                 "its surroundings and everything gets cold. Nothing else "
                 "needs to be added to that story — it is bookkeeping on "
                 "joins."},
        {"type": "explainer", "id": "why-it-needs-a-match",
         "text": "It also explains why some reactions need a match. A mixture "
                 "of hydrogen and oxygen will sit in a balloon indefinitely, "
                 "even though the reaction gives out an enormous amount of "
                 "energy, because the first joins still have to be broken and "
                 "nothing has paid for them. A flame pays for the first few, "
                 "those release enough energy to pay for the next few, and "
                 "the balloon goes off. Chemistry is full of things that are "
                 "worth doing and still need starting."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent. Design
    # draws no support layer on this page and nothing here needs one that the
    # rearranger's three stages do not already give: a student who cannot yet
    # do it in their head can press through and count circles.
    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    # ⚠️ THE KEY IS `definition`, NOT `gloss`. §12 of the build contract says
    # `{"term", "gloss"}`; `build_ks3.py` line 939 reads `v["definition"]`, and
    # `gloss` is a `rule` CARD's key, a different construct. Authored to what
    # the engine actually reads, so that a future `keyword` block placed on
    # this page renders instead of raising. Reported to the commander.
    #
    # Only terms this lesson INTRODUCES or leans its whole weight on. "Atom"
    # and "element" are C2's and are not re-glossed here.
    "vocabulary": [
        {"term": "chemical reaction",
         "definition": "A change in which the joins between atoms are broken "
                       "and new joins are made, so one or more new substances "
                       "appear.",
         "note": None},
        {"term": "reactant",
         "definition": "A substance you start with, before the reaction "
                       "happens.",
         "note": None},
        {"term": "product",
         "definition": "A substance made by the reaction.",
         "note": "The atoms in a product were all in the reactants first. "
                 "There is nowhere else for them to come from."},
        {"term": "rearrange",
         "definition": "To keep the same things and put them together "
                       "differently.",
         "note": "It is the whole of what a reaction does to atoms."},
        {"term": "compound",
         "definition": "A substance made of two or more kinds of atom joined "
                       "together.",
         "note": "Magnesium oxide is a compound. There is no such thing as a "
                 "magnesium oxide atom."},
    ],

    # ── safety (§1.5) ───────────────────────────────────────────────────────
    # DELIBERATELY ABSENT, and the reasoning is here so it is not re-opened.
    # C3 carried one because it ended with a camping filter bottle and the
    # thing a twelve-year-old might do next was drink something. This page asks
    # nobody to do anything: there is no method, no apparatus and no quantity
    # anywhere on it, by Design's decision and confirmed under flag 6. A safety
    # line about hydrogen would be the first instruction on the page, and it
    # would be an instruction to do the demonstration.
    #
    # No safeguarding block either (§16). This is a substance lesson — nothing
    # in it touches a student's own body, health or risk — which is the same
    # reading C3's seven took and were right to.

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why no reaction can make gold?",
              "cta": "Ask about this lesson",
              "anchor": "s-impossible"},

    "ks4_becomes": "Bond breaking and bond making as the energy story of a "
                   "reaction, and balanced symbol equations with state "
                   "symbols.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The rearranger is a model being used to predict and then checked against
    # what the model itself produces; rung 3 and rung 4 are both evaluation of
    # a claim.
    "ws": ["scientific-attitudes", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
