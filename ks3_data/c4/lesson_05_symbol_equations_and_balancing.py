"""C4 L5 — Symbol equations and balancing (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c4/c4-05-symbol-equations-and-balancing.dc.html`
(699 lines), and her author's notes `docs/ks3/design-reference/c4/NOTES-C4.md`
§1, §2, §3 (the `coefficient-balancer` payload), §5 flags 2 and 15, §6
(`REACT-08`, `REACT-09`) and §7.

Every student-facing string is byte-identical to the approved page. `RAIL`,
`EQS`, `RUNGS` and `SELF_RUNGS` came out of the node extractor; the hook
options and reveal, the two explainer paragraphs, the balancer's per-equation
`words` and `note`, the "all four" summary, the forbidden-move panel's two
verdicts, the key fact, the `#s-think` options and its two reveal paragraphs,
the key note and both "Going further" paragraphs were lifted from
`lessonVals(s)` and from the markup, which is where most of this lesson's
words live and where a lift of the top-level constants alone loses them.

⚠️ `EQS` was invisible to the extractor until the hoisting fix landed this
week — the payload builds each term through a page-local `t()` helper, so the
whole four-equation constant came back undefined and c4-05 read as three
constants rather than four. It is present and verified: four equations, each
`{id, tab, words, left, right, target, note}`. Nothing below is reconstructed
by hand.

── THE SUBSCRIPT CONVENTION, WHICH THIS UNIT OWNS ──────────────────────

NOTES §3: every formula on this page renders from `parts: [{sym, sub}]` so
that a subscript is a REAL `<sub>` ELEMENT and never a Unicode subscript
character. C2 flag 13 ruled it for the course; `kit.rich()` admitted `<sub>`
to the inline allow-list for exactly this (MRB-272), and every downstream
chemistry unit inherits it. The full argument lives in the renderer fragment's
docstring, which is where the convention is implemented.

Two consequences visible in THIS file:

  · Prose here carries real `<sub>` markup — `H<sub>2</sub>O` — because
    explainer text, the hook reveal, key facts, the key note, the `#s-think`
    reveal and the stretch layer all reach the page through `rich()`.
  · LADDER strings do not, and must not. `_rung_marked` escapes its question
    and its options with `t()`, and a rung's per-option correction is escaped
    into a `data-feedback` ATTRIBUTE — so a `<sub>` in any of them would ship
    as visible tag soup, which is the escape-as-visible defect the allow-list
    exists to prevent. Design writes every ladder formula flat (`H2O2`,
    `2Mg + O2`) and they are kept exactly as she wrote them.

── THE FORBIDDEN MOVE IS A BUTTON, NOT A WARNING ───────────────────────

NOTES §2 and the whole reason `#s-forbidden` is a section rather than a
sentence: adding a small 2 to the water BALANCES the equation and silently
turns the product into bleach. The student is ALLOWED to make the move and is
then shown what they actually wrote. There is no refusal, no confirm dialog
and no red. `forbidden-move` below offers both moves as ordinary segmented
buttons, both stay pressable afterwards, and the panel that opens says in
words what each one did.

⚑ `REACT-08` is `ATOM-09` in its balancing costume, and the confrontation is
DELIBERATELY the same substance — H₂O₂ — so c2's lesson and this one reinforce
each other (NOTES §6). Cross-referenced here rather than re-minted.

── The two arithmetic facts this lesson's instrument rests on ──────────

Enumerated once, here, because the renderer, the wiring and the "Going
further" paragraph all depend on them and none of them may hard-code a number
the instrument can compute:

  1. **Every target is reachable inside the cap of 4** (flag 15). Water, MgO
     and NaCl are all `[2, 1, 2]`; methane is `[1, 2, 1, 2]`.
  2. **Each equation has exactly TWO balanced states inside the cap** — its
     target and the target DOUBLED (`[4, 2, 4]`, and `[2, 4, 2, 4]` for
     methane). Nothing else in 1–4 balances. The doubled state is balanced and
     is not the answer, and the "Going further" paragraph names that case in
     Design's own words: *"4H₂ + 2O₂ makes 4H₂O is balanced and would still be
     marked down."* The instrument therefore says so at the moment the student
     produces it, rather than praising a state the page later marks down.
     See the renderer for the one new sentence that does it.
  3. **No count is ever zero.** Every coefficient is at least 1 and every term
     carries at least one atom of each element it contributes, so "Too few on
     the left" / "Too few on the right" is always a real shortfall and never
     an empty side.

⚑ For Mide's science gate, from Design's NOTES §5:
  * flag 15 — coefficients capped at 4. CONFIRMED a help, and kept. The cap
    is a property of the CONTROL and is never narrated as a rule of
    chemistry (§11): the stepper simply stops at the bound, shown as a
    disabled control and not as a sentence.
  * flag 2 — rust reversed in a steelworks. This lesson is a NEIGHBOUR to
    that claim and does not make it: nothing here says a reaction can be run
    backwards, on a bench or anywhere else. Deliberately not added.
"""

# ── the arrow, and why it is typed here ────────────────────────────────
#
# ⚠️ `→` IS TYPED IN AUTHORED PROSE AND DRAWN ON THE PAGE. `kit.t()` swaps
# U+2192 for the `.ks3-mark-arrow` inline SVG before anything reaches a
# browser, because Design's five shipped latin woff2 subsets contain no glyph
# for it (SPEC §9.3) and typed as a character it drops to a system font
# mid-line. So a typed arrow in a string below IS the SVG arrow §15 requires;
# the character never reaches a student. The instrument's own equation arrows
# are drawn in the renderer, at Design's own 44×24 geometry.


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 212 character for character.
    "slug":        "symbol-equations-and-balancing",
    "title":       "Symbol equations and balancing",
    "discipline":  "chemistry",
    "unit":        "chemical-reactions",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # NOTES §1 splits `KS3.C.CR.02` across two lessons the way `AEC.03` was
    # split: a word equation is a SENTENCE, a symbol equation is a MODEL WITH
    # NUMBERS IN IT. This is clause `b` — representing a reaction with
    # formulae, as a BALANCED symbol equation. The formula-writing half of
    # "using formulae" is C2's `KS3.C.AEC.03b` and is not re-owned here; the
    # clause is already minted in ks3_data/substatements.py with the full
    # reasoning and is not edited from this file.
    "covers":      ["KS3.C.CR.02b"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "particles", "level": 3},
                    {"id": "substances-and-reactions", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # ⚠️ `requires` IS THE DEPENDENCY GRAPH, NOT THE PREVIOUS SLOT. A symbol
    # equation is a word equation with the names replaced by formulae and the
    # counts made honest, so `word-equations` is what this lesson genuinely
    # cannot be read without. Design's "Before this lesson" card points at
    # `mass-in-a-reaction`, which is the previous SLOT rather than the
    # prerequisite — and MRB-257's "Where to next" card already prints it as
    # `Previous: Mass in a reaction` from the unit order, so her link is on
    # the page either way and the graph stays true.
    #
    # ⚠️ AND THE FORWARD LINK IS THE ENGINE'S, DELIBERATELY. Design's second
    # card links on to Combustion under the heading "Next in this unit", and
    # Combustion is in the NEXT unit — so the heading would be false over a
    # true link. `references` is left empty and the endmatter's "Where to next"
    # card carries the same link with the target unit's title beside it, which
    # is what the card exists for. Authoring the reference as well would put
    # two controls to the same lesson in one endmatter grid.
    "requires":    ["word-equations"],
    "assumes":     [],
    "references":  [],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Written straight out, the equation for making water "
                    "destroys an oxygen atom. Fixing it teaches you the one "
                    "number in chemistry you are allowed to change.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Design's `RAIL`, stop for stop, in her order and with her ids and short
    # labels (MRB-249). Five stops. `done_when` restates her own `DONE()`:
    # the hook and `#s-think` on a commitment, `#s-balance` when every one of
    # the four equations has been driven to its target, `#s-forbidden` the
    # moment either move is taken, the ladder when both marked rungs are
    # answered and both self-marked rungs checked.
    #
    # MRB-208: credit is a RATCHET and NOTHING is ticked on load — both
    # instruments ship `data-stage-done="0"` from their shell registration.
    "rail": [
        {"anchor": "s-hook",      "short": "HOOK",
         "label": "The missing oxygen",  "done_when": "committed"},
        {"anchor": "s-balance",   "short": "BALANCE",
         "label": "Balance four",        "done_when": "all_four_solved"},
        {"anchor": "s-forbidden", "short": "FORBID",
         "label": "The quick way",       "done_when": "either_move_taken"},
        {"anchor": "s-think",     "short": "THINK",
         "label": "Just maths?",         "done_when": "committed"},
        {"anchor": "s-ladder",    "short": "LADDER",
         "label": "Mastery ladder",      "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # `kind` is unread by the generator (it dispatches on which media key is
    # present) and is authored for consistency with the rest of the key stage.
    #
    # ⚠️ ONE MERGE, AND IT IS THE ONLY ONE IN THIS FILE. Design draws TWO
    # `.ks3-hook-prompt` paragraphs — a 26px display line carrying
    # `H₂ + O₂ → H₂O`, then the sentence that reads it — and `r_hook` emits
    # exactly one prompt paragraph from `phenomenon.prompt`. `build_ks3.py` is
    # a shared file and is not this lane's to widen, so the equation opens the
    # prompt and Design's paragraph follows it byte for byte. The arrow is
    # typed and drawn (see the note at the top of this file), and the
    # subscripts are real `<sub>` elements because `phenomenon.prompt` goes
    # through `rich()`.
    "phenomenon": {
        "kind": "narrative",
        "title": "Count the oxygens. One of them has gone missing.",
        "prompt": "H<sub>2</sub> + O<sub>2</sub> → H<sub>2</sub>O. Two oxygen "
                  "atoms on the left. One on the right. Last lesson you "
                  "proved that atoms are never destroyed — so this equation, "
                  "exactly as written, is a claim that one of them was.",
        "commit": "What has to change to fix it?",
        # ⚠️ FLAT FORMULAE, ON PURPOSE. `_option_li` escapes an option with
        # `t()`, so `<sub>` here would ship as literal angle brackets. These
        # are Design's own strings and she writes them flat for the same
        # reason.
        #
        # MRB-177: option B is the answer and is not the longest — A is 9
        # words, B is 9, C is 6, D is 10. Each distractor is a WRONG RULE in
        # B's own shape: A changes the small number (REACT-08, and the move
        # `#s-forbidden` lets them make), C deletes an atom, D spends one as
        # energy.
        "options": [
            "Change H2O to H2O2 so the oxygens match",
            "Change how many particles react, using numbers in front",
            "Remove one oxygen from the left",
            "Nothing — the extra oxygen atom is used up as energy",
        ],
        "reveal": "The number of particles. Two hydrogen particles react with "
                  "one oxygen particle and make <strong>two</strong> water "
                  "particles — and writing a 2 in front of H<sub>2</sub>O "
                  "says so. What you must not touch is the small number "
                  "inside a formula: changing H<sub>2</sub>O to "
                  "H<sub>2</sub>O<sub>2</sub> also balances the oxygen, and "
                  "it does it by quietly replacing the water with bleach.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # NOTES §6, the proposed `REACT` family. Both joins are checked against the
    # markup this page actually emits (MRB-244), not against intent:
    #
    #   REACT-08  elicited_by  `forbidden-small-2`  → id= on the "Add a small
    #                                                  2 to the water" button
    #             confronted_by `forbidden-reveal`  → id= on the panel that
    #                                                  opens under it
    #   REACT-09  elicited_by  `think-commit-maths` → data-activity= on the
    #                                                  `#s-think` section
    #             confronted_by `think-commit-maths` → the same section
    #
    # ⚠️ REACT-09's `confronted_by` IS NOT `think-reveal-peroxide`, and the
    # difference is a fact about the engine rather than a change of mind. The
    # peroxide argument lives in the `#s-think` reveal, and `r_activity` emits
    # that panel as a bare `<div class="ks3-reveal ks3-reveal-panel" hidden
    # data-reveal>` with NO id — there is no authored key that puts one there,
    # and adding one means editing `build_ks3.py`, which is shared. Naming an
    # id the page does not emit would fail MRB-244's gate and, worse, would be
    # a join that reads as resolved and is not. Pointing at the activity is
    # the honest form and it is what c3-03's MIX-06 does for the same reason.
    #
    # It also satisfies Law 3, which asks for at least one misconception
    # confronted by a REAL ACTIVITY ID: `forbidden-reveal` is an element
    # inside an instrument, so REACT-09's join is the one carrying that.
    #
    # ⚠️ `statement` IS THE LINE THE PAGE QUOTES, not the register's shorter
    # handle — `r_confrontation` prints `statement` as the `#s-think` quote and
    # Design's line is the one that must render.
    "misconceptions": [
        {"id": "REACT-08",
         "statement": "An equation can be balanced by changing the small "
                      "numbers in a formula.",
         "elicited_by": "forbidden-small-2",
         "confronted_by": "forbidden-reveal"},
        {"id": "REACT-09",
         "statement": "Balancing is just a maths puzzle — as long as the "
                      "numbers add up, the equation is right.",
         "elicited_by": "think-commit-maths",
         "confronted_by": "think-commit-maths"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Page lines 108–111 — Design draws ONE `.ks3-explainer` section with
        # two paragraphs; `r_explainer` emits one `<p>` per block, so this is
        # two blocks. Both are lifted whole, and together they are the whole
        # of this lesson's §5.2 prose budget (100 words of the 450).
        {"type": "explainer",
         "text": "A <strong>symbol equation</strong> says which substances "
                 "react and <strong>how many particles of each</strong>. The "
                 "small numbers inside a formula are part of the substance's "
                 "name — H<sub>2</sub>O <em>is</em> water. The big numbers in "
                 "front say how many of that particle take part, and those "
                 "are the only numbers you are allowed to change."},
        {"type": "explainer",
         "text": "An equation is <strong>balanced</strong> when every kind of "
                 "atom appears the same number of times on both sides. It has "
                 "to be, because atoms are not created or destroyed."},

        # #s-balance — the flagship. Light `ks3-block` → `check`.
        #
        # ⚠️ THE EQUATIONS ARE DESIGN'S `EQS` CONSTANT, WHOLE. `atoms` is what
        # the counters are DERIVED from at render and on every press (§5A);
        # `target` is what `solved` is decided against, and it is never the
        # same test as "balanced" — see the module docstring's fact 2.
        {"type": "coefficient-balancer", "id": "balance-four",
         "anchor": "s-balance",
         "eyebrow": "Your turn · balance four equations",
         "heading": "Change only the big numbers. Watch the counters.",
         "demand": "construct",
         "min": 1,
         "max": 4,
         "reset_label": "Set them all back to 1",
         "balanced_label": "Balanced.",
         "equations": [
             {"id": "water",
              "tab": "Hydrogen + oxygen",
              "words": "Hydrogen burns in oxygen to make water. The products "
                       "are known; only the numbers in front are in question.",
              "left": [{"parts": [{"sym": "H", "sub": "2"}],
                        "atoms": {"H": 2}},
                       {"parts": [{"sym": "O", "sub": "2"}],
                        "atoms": {"O": 2}}],
              "right": [{"parts": [{"sym": "H", "sub": "2"},
                                   {"sym": "O", "sub": ""}],
                         "atoms": {"H": 2, "O": 1}}],
              "target": [2, 1, 2],
              "note": "Two hydrogen particles to one oxygen particle, making "
                      "two waters. That two-to-one ratio is the fact a word "
                      "equation could never tell you."},
             {"id": "mgo",
              "tab": "Magnesium + oxygen",
              "words": "Magnesium ribbon burns in air to make magnesium "
                       "oxide.",
              "left": [{"parts": [{"sym": "Mg", "sub": ""}],
                        "atoms": {"Mg": 1}},
                       {"parts": [{"sym": "O", "sub": "2"}],
                        "atoms": {"O": 2}}],
              "right": [{"parts": [{"sym": "Mg", "sub": ""},
                                   {"sym": "O", "sub": ""}],
                         "atoms": {"Mg": 1, "O": 1}}],
              "target": [2, 1, 2],
              "note": "One oxygen particle carries two oxygen atoms, so it "
                      "can oxidise two magnesium atoms. That is why the 2 "
                      "lands in front of the Mg and the MgO together."},
             {"id": "nacl",
              "tab": "Sodium + chlorine",
              "words": "Sodium burns in chlorine to make sodium chloride "
                       "— table salt.",
              "left": [{"parts": [{"sym": "Na", "sub": ""}],
                        "atoms": {"Na": 1}},
                       {"parts": [{"sym": "Cl", "sub": "2"}],
                        "atoms": {"Cl": 2}}],
              "right": [{"parts": [{"sym": "Na", "sub": ""},
                                   {"sym": "Cl", "sub": ""}],
                         "atoms": {"Na": 1, "Cl": 1}}],
              "target": [2, 1, 2],
              "note": "The same shape of answer as the magnesium one, for the "
                      "same reason: chlorine travels in pairs, so it takes "
                      "two sodium atoms to use one chlorine particle up."},
             {"id": "methane",
              "tab": "Methane + oxygen",
              "words": "Methane burns on a gas hob to make carbon dioxide and "
                       "water. Four terms this time.",
              "left": [{"parts": [{"sym": "CH", "sub": "4"}],
                        "atoms": {"C": 1, "H": 4}},
                       {"parts": [{"sym": "O", "sub": "2"}],
                        "atoms": {"O": 2}}],
              "right": [{"parts": [{"sym": "CO", "sub": "2"}],
                         "atoms": {"C": 1, "O": 2}},
                        {"parts": [{"sym": "H", "sub": "2"},
                                   {"sym": "O", "sub": ""}],
                         "atoms": {"H": 2, "O": 1}}],
              "target": [1, 2, 1, 2],
              "note": "Balance the carbon and hydrogen first and the oxygen "
                      "falls out last — four oxygen atoms needed on the "
                      "right, so two O2 particles on the left. Working in "
                      "that order saves a lot of guessing."},
         ],
         # The three counter states, as words. R2: the tile's colour is never
         # the only signal, and these are the signal.
         "counter_states": {
             "matched": "Matched.",
             "short_right": "Too few on the right.",
             "short_left": "Too few on the left.",
         },
         # ⚠️ NEW PROSE, AND THE ONLY NEW PROSE IN THIS FILE. Design shows
         # `eq.note` whenever the counts match, and the counts also match at
         # exactly one other reachable state per equation: the target doubled
         # (docstring fact 2). At `4H₂ + 2O₂ → 4H₂O` her water note reads
         # "making two waters", which the drawn equation contradicts, and her
         # own "Going further" paragraph marks that state down. §14 forbids a
         # lesson retracting itself later on the same page, so the doubled
         # state gets this line instead of a note that has stopped being true.
         # `{k}` is DERIVED from the coefficients and the target and is never
         # written down as a 2 (§5A), even though 2 is the only value the cap
         # of 4 allows today.
         "multiple_note": "Balanced, but not in its smallest numbers. Every "
                          "number in front is {k} times what it needs to be "
                          "— and an equation is always written with the "
                          "smallest whole numbers that work.",
         "summary": "All four. In every one of them you changed how many "
                    "particles react and never what a particle is — and in "
                    "every one of them the counters ended up matching, "
                    "because they were always going to have to."},

        # #s-forbidden — the cleverest thing in the unit. Light
        # `ks3-block ks3-misconception` → `misconception`.
        #
        # ⚠️ AN EMPTY `quote` IS DELIBERATE. `_confrontations` emits
        # `.ks3-mis-quote` only when a statement carries one, and Design draws
        # NO quoted line here — the badge, the eyebrow and one paragraph, then
        # the two buttons. The quoted line belongs to `#s-think`.
        {"type": "forbidden-move", "id": "forbidden-move",
         "anchor": "s-forbidden",
         "eyebrow": "The move that looks like it works",
         "demand": "investigate",
         "targets": "REACT-08",
         "statements": [
             {"quote": "",
              "body": ["There is a much quicker way to balance the hydrogen "
                       "and oxygen equation. Add a small 2 to the water "
                       "instead of a big 2 in front of it, and the counters "
                       "agree immediately. Try it and see what it costs."]},
         ],
         # The left-hand side both moves share, drawn from `parts` like every
         # other formula on the page.
         "left": [{"parts": [{"sym": "H", "sub": "2"}]},
                  {"parts": [{"sym": "O", "sub": "2"}]}],
         # ⚠️ EACH MOVE'S id IS THE MISCONCEPTION REGISTER'S OWN HANDLE.
         # `forbidden-small-2` is REACT-08's `elicited_by` and it has to be on
         # the button a student presses to make the mistake.
         "moves": [
             {"id": "forbidden-small-2",
              "value": "small",
              "label": "Add a small 2 to the water",
              # H₂O₂ — no number in front, and the small 2 the student added.
              "product": [{"sym": "H", "sub": "2"},
                          {"sym": "O", "sub": "2"}],
              "text": "The counters agree: two hydrogens and two oxygens on "
                      "each side. And you are no longer describing the "
                      "reaction you were asked about. H<sub>2</sub>O<sub>2"
                      "</sub> is hydrogen peroxide — it bleaches hair, burns "
                      "skin at high concentration and has been used as rocket "
                      "fuel. One small digit, and the equation now says that "
                      "burning hydrogen produces bleach. It does not."},
             {"id": "forbidden-big-2",
              "value": "big",
              "label": "Put a big 2 in front of the water",
              "coeff": "2",
              "product": [{"sym": "H", "sub": "2"}, {"sym": "O", "sub": ""}],
              "text": "Two hydrogens and two oxygens on each side — with "
                      "hydrogen now needing a 2 as well, giving 2H<sub>2</sub>"
                      " + O<sub>2</sub> makes 2H<sub>2</sub>O. The substances "
                      "are untouched: water is still water, and all you have "
                      "changed is how many of each particle take part. That "
                      "is the only kind of change balancing is allowed to "
                      "make."},
         ],
         "reveal_id": "forbidden-reveal"},

        {"type": "key-fact", "ref": "big-numbers-are-yours"},

        {"type": "misconception", "id": "think-commit-maths",
         "anchor": "s-think", "targets": "REACT-09"},

        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # NOTES §7: five instruments, all DOM, no canvas, no animation — and no
    # figure on this lesson. Present and empty rather than absent.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "big-numbers-are-yours",
         "text": "Balancing changes how many particles react, never what the "
                 "particles are. Big numbers in front are yours to change; "
                 "small numbers inside a formula belong to the substance.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # `#s-think` only. The two instrument blocks are lifted out of `core` into
    # this list by `_normalise()` and are never authored here.
    "activities": [
        {"id": "think-commit-maths",
         "kind": "predict",
         "demand": "explain",
         "targets": "REACT-09",
         "prompt": "Every balanced equation does have matching counts on both "
                   "sides. Commit before you read on.",
         # MRB-177: B is the answer and it is the longest by construction —
         # a "wrong, because…" answer cannot be as short as "Right." So the
         # LENGTH TELL IS FIXED AT THE DISTRACTORS, never by trimming B: C
         # carries the same hedge shape as B ("as long as…"), and D is a
         # second "Wrong — …" so that the opening word tells the student
         # nothing. A is 4 words, B is 12, C is 9, D is 6; B is not longest by
         # 1.4× against C. Each is a wrong RULE: A says arithmetic is enough,
         # C says the permitted move guarantees truth, D denies conservation.
         "options": [
             "Right — balancing is arithmetic",
             "Wrong — a balanced equation can still describe a reaction "
             "that does not happen",
             "Right, as long as you only change the numbers in front",
             "Wrong — equations do not have to balance",
         ],
         "reveal": [
             "Matching counts are necessary and nowhere near sufficient. "
             "H<sub>2</sub> + O<sub>2</sub> makes H<sub>2</sub>O<sub>2</sub> "
             "is perfectly balanced and completely false, because that "
             "reaction does not happen and that substance is not water. The "
             "chemistry decides what the products are; the balancing only "
             "makes the arithmetic honest afterwards.",
             "So the order of work matters. <strong>Find out what the "
             "products actually are, write their formulae, and only then "
             "adjust the numbers in front.</strong> An equation that balances "
             "beautifully around the wrong product is worth nothing — and it "
             "is a mistake that a calculator will never catch for you.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Design's `RUNGS` → recall + apply, `SELF_RUNGS` → explain + produce.
    #
    # ⚠️ HER RUNG TITLES ARE THE ENGINE'S OWN DEFAULTS character for character
    # ("Recall", "The one that catches people", "Explain", "Take it somewhere
    # new"), so no rung authors a `title` (§12).
    #
    # ⚠️ EVERY FORMULA HERE IS FLAT. See the module docstring: a marked rung's
    # question and options are escaped with `t()` and its corrections are
    # escaped into a `data-feedback` attribute, so `<sub>` would ship as
    # visible angle brackets. Design writes them flat and they stay flat.
    #
    # `feedback` is keyed by the INT index of each wrong option, which is what
    # `_rung_marked` reads.
    "ladder": {
        # MRB-177 · recall. Correct option 0 is 8 words; distractors are 6, 8
        # and 7. Not longest, nowhere near 1.4×. Each is a wrong rule about
        # WHICH numbers move: option 1 is REACT-08 itself, option 2 is
        # REACT-09, option 3 mistakes the equation for the chemistry.
        "recall": {
            "q": "In a symbol equation, which numbers are you allowed to "
                 "change when balancing?",
            "options": [
                "The small numbers inside a formula",
                "The big numbers written in front of a formula",
                "Either, as long as the counts end up matching",
                "Neither — you change the substances instead",
            ],
            "answer": 1,
            "feedback": {
                0: "Those are part of the substance. Changing H2O to H2O2 "
                   "changes water into hydrogen peroxide.",
                2: "Matching counts around the wrong substance is a false "
                   "equation. Only the numbers in front may change.",
                3: "The substances are decided by the chemistry, which is "
                   "exactly what the equation is reporting.",
            }},
        # MRB-177 · apply. Correct option 0 is 11 words; distractors are 8, 9
        # and 8. Ratio 11/9 = 1.22, under the 1.4× bar, and the gap is 2
        # words, under 4. This is REACT-09's marked elicitation: option 1 is
        # the misconception stated plainly.
        "apply": {
            "q": "A student balances the equation as H2 + O2 makes H2O2, and "
                 "points out that both sides now have two hydrogens and two "
                 "oxygens. What is wrong?",
            "options": [
                "Nothing — it is balanced, so it is correct",
                "It balances, but the product is hydrogen peroxide, not water",
                "The hydrogen is wrong — there should be four",
                "You cannot have a number 2 in a formula",
            ],
            "answer": 1,
            "feedback": {
                0: "Balanced is not the same as true. This equation describes "
                   "a different reaction, making a substance that bleaches "
                   "hair.",
                2: "The counts really do match. The fault is in what was "
                   "changed to make them match.",
                3: "H2O2 is a real formula for a real substance. That is the "
                   "problem: the student has written the equation for making "
                   "it.",
            }},
        "explain": {
            "q": "Balance the equation for magnesium burning in oxygen, and "
                 "explain why a 2 is needed in front of both the Mg and the "
                 "MgO — and why putting a small 2 in the MgO would be wrong.",
            "field_label": "Your answer",
            "placeholder": "The balanced equation is…",
            "success": [
                "Gives the balanced equation: 2Mg + O2 makes 2MgO.",
                "Says one oxygen particle contains two oxygen atoms.",
                "Says those two oxygen atoms need two magnesium atoms, so two "
                "units of MgO are made.",
                "Says MgO2 would be a different substance, not magnesium "
                "oxide.",
                "Says small numbers belong to the formula and only the "
                "numbers in front may be changed.",
            ]},
        "produce": {
            "q": "A hydrogen car burns hydrogen with oxygen from the air. The "
                 "engineers need to know how much oxygen to supply for a "
                 "given amount of hydrogen. Explain what the balanced "
                 "equation tells them that a word equation cannot, and what "
                 "would happen if they supplied too little.",
            "field_label": "Your answer",
            "placeholder": "The balanced equation says that…",
            "success": [
                "States the ratio the balanced equation gives: two hydrogen "
                "particles to one oxygen particle.",
                "Says a word equation names the substances but not the ratio.",
                "Says the ratio lets them work out the amount of oxygen "
                "needed for a given amount of hydrogen.",
                "Says supplying too little oxygen leaves hydrogen unreacted, "
                "so fuel is wasted.",
                "Notes that the atoms cannot come from anywhere else, which "
                "is why the ratio is fixed and not adjustable.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "A symbol equation says which substances react and how many "
                "particles of each. It is balanced when every kind of atom "
                "appears the same number of times on both sides — which it "
                "must, because atoms are never created or destroyed. Balance "
                "by changing the big numbers in front of formulae only: the "
                "small numbers inside a formula are part of the substance, "
                "and changing one changes what the equation is about.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # Both paragraphs lifted whole from Design's "Going further".
    #
    # ⚑ The second paragraph is what makes the balancer's doubled state
    # teachable rather than a trap: "4H₂ + 2O₂ makes 4H₂O is balanced and
    # would still be marked down" is exactly the state `multiple_note` above
    # names at the moment the student produces it. The two agree on purpose.
    "stretch": [
        {"type": "explainer", "id": "why-the-ratio-matters",
         "text": "The big numbers are not decoration; they are the reason "
                 "this notation was worth inventing. 2H<sub>2</sub> + "
                 "O<sub>2</sub> makes 2H<sub>2</sub>O says that hydrogen and "
                 "oxygen react in a two-to-one ratio, so a hydrogen fuel cell "
                 "needs exactly twice as many hydrogen particles as oxygen "
                 "ones, and a plant scaling that up needs the ratio right to "
                 "the tonne. Word equations cannot carry that. This is the "
                 "whole reason your course spends a year learning symbols."},
        {"type": "explainer", "id": "two-conventions",
         "text": "Two conventions worth having now. The numbers in front must "
                 "be whole — you may not write half a particle, even though "
                 "1/2 O<sub>2</sub> would sometimes be tidier — and they are "
                 "written in the smallest whole numbers that work, so "
                 "4H<sub>2</sub> + 2O<sub>2</sub> makes 4H<sub>2</sub>O is "
                 "balanced and would still be marked down. At GCSE two more "
                 "things get added to the same line: state symbols in "
                 "brackets, and the fact that this identical logic runs the "
                 "calculation of how much product a reaction can make."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    # Every technical term this lesson introduces, in the lesson's own words.
    # `definition` is the card back and `note` is the line under it —
    # `r_keywords` reads `v["definition"]` by hard index, so the key is not
    # optional and is not spelled `gloss`. Shape copied from
    # `ks3_data/c3/lesson_02_dissolving_and_solutions.py`.
    #
    # ⚠️ FLAT FORMULAE HERE TOO. `r_keywords` escapes both fields with `t()`,
    # so a `<sub>` would ship as visible angle brackets — the same constraint
    # as the ladder, and the same reason.
    #
    # "Coefficient" is deliberately ABSENT. The page never says it to a
    # student — Design writes "the big numbers in front" throughout — and a
    # keyword list is not the place to introduce a word the lesson took care
    # to avoid.
    "vocabulary": [
        {"term": "Symbol equation",
         "definition": "A reaction written with formulae instead of names.",
         "note": "It says which substances react AND how many particles of "
                 "each. A word equation cannot carry the second half."},
        {"term": "Formula",
         "definition": "How a substance is spelled in symbols.",
         "note": "The small numbers in it are part of the name. H2O is water "
                 "and H2O2 is not."},
        {"term": "Balanced",
         "definition": "Every kind of atom appears the same number of times "
                       "on both sides.",
         "note": "It has to, because atoms are never made or destroyed. "
                 "Balanced is not the same as true."},
        {"term": "Hydrogen peroxide",
         "definition": "H2O2 — a real substance that bleaches hair, and not "
                       "water.",
         "note": "It is what a small 2 added to the water turns the equation "
                 "into."},
    ],

    # ── safety (§1.5) ───────────────────────────────────────────────────────
    # No `safety_note` and no safeguarding block. Nothing on this page is a
    # bench instruction: there is no method, no apparatus and nothing a
    # student is asked to do with a substance. Hydrogen peroxide is NAMED as
    # what a wrong equation describes, and naming a hazard in an argument is
    # not the same as putting a bottle in front of somebody. C3 carried no
    # safeguarding line and was right to; this is the same shape of lesson,
    # one step further from the bench.

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # ⚠️ The tutor CTA points at `#s-forbidden`, which is Design's own anchor:
    # the student who is unsure why the small numbers are off limits is sent
    # to the section that lets them break the rule and shows them the result.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why the small numbers are off limits?",
              "cta": "Ask about this lesson",
              "anchor": "s-forbidden"},

    "ks4_becomes": "Balanced equations with state symbols, half equations and "
                   "ionic equations — and using the ratio to calculate "
                   "reacting masses.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
