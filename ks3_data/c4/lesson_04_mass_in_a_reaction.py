"""C4 L4 — Mass in a reaction (QUANTITATIVE).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c4/c4-04-mass-in-a-reaction.dc.html` (813 lines),
and her author's notes `docs/ks3/design-reference/c4/NOTES-C4.md` §1, §2, §3,
§4 (the four-part treatment and flag 14), §5 flags 11–14, §6 (`REACT-07`) and
§7.

Every student-facing string is byte-identical to the approved page. `RAIL`,
`RUNS`, `WORKED`, `CHECKS`, `COVERS`, `RUNGS` and `SELF_RUNGS` came out of the
node extractor; the hook options and reveal, the bench's dials, prediction and
closing summary, the rule block, the bar's labels and its closing sentence,
the key fact, the `#s-think` options and both reveal paragraphs, the key note
and both "Going further" paragraphs were lifted from `lessonVals(s)` and from
the markup — which is where most of this lesson's words live, and where a lift
of the top-level constants alone silently loses them.

The three places prose was deliberately re-authored are marked ⚠️ NEW PROSE
where they sit, and every one is in the report.

── SEVEN RAIL STOPS, AND WHY (NOTES §7) ────────────────────────────────

The most in the course so far. Three of the seven are MRB-204's four-part
treatment costing a stop each — the drawing, the watched worked example and
the student's own run are three separate things a student does, not one — and
that is exactly what the treatment is for. MRB-249 matches Design stop for
stop, so the count is read off her `RAIL` rather than tidied to five.

── THE FOUR-PART TREATMENT, AND FLAG 14 (MRB-204, MRB-246) ─────────────

  1. the rule ALONE in its own block  → the `formula` block below;
  2. DRAWN, as a PART–WHOLE BAR       → `#s-cover`;
  3. the worked example one step at a time, F / I / F / A badges visible
                                      → `#s-worked`;
  4. the same four steps done by the STUDENT, compare-button PER STEP
                                      → `#s-check`.

⚖️ **CONSERVATION OF MASS IS A SUM, SO IT TAKES A BAR AND NEVER A TRIANGLE.**
RULED (MRB-246), answering Design's NOTES-C4 §4 flag 14: "drawn" means drawn
in whatever shape the relationship HAS. A triangle is for `A = B × C`. A beam
or a part–whole bar is for sums and conservation statements. A triangle on a
sum teaches a relationship that does not exist — it invites a student to
multiply two masses together, which is not a thing. Design built it as a bar,
the bar is CORRECT, and a later pass must not "fix" it into a triangle.
`c2-06` is the same ruling one unit earlier and the two now agree.

── ⚠️ `#s-cover` IS AN ACTIVITY, NOT A `formula` BLOCK'S `cover` KEY ───

`build_ks3.py` around line 2022 carries a comment saying `cover-triangle` is
NOT an activity kind, that it is a `formula` block sub-key "exactly as its bar
variant is", that it has no `data-stage-done`, and that "the block is read,
not done, and MRB-208 keeps it off the rail". **That comment is true of C2's
READ-ONLY variant and it does not govern this lesson.**

Design's own page settles it. `RAIL` (page line 449) contains `s-cover`, and
`DONE()` (page line 553) reads:

    if (id === 's-cover') return s.cover !== null;

which ticks when the student has PRESSED A COVER BUTTON. A press is a
commitment, so `#s-cover` has a real completion signal and MRB-249 requires
the stop. So it is authored inline in `core` as `"type": "mass-cover"`, its
shell ships `data-stage-done="0"`, and `wireMassCover` calls `markStage` on
the first cover press.

⚠️ AND THE BENCH IS `mass-bench`, NOT `balance-bench`. The build contract's
§8 table assigned `balance-bench`; that family is ALREADY REGISTERED, by
`ks3_art/c2.py` for c2-06's `#s-balance`, which is very nearly this instrument
one unit earlier. The registry fails loudly on a duplicate family across
modules and it is right to: a silent last-one-wins would render this bench with
C2's renderer and tell nobody. §8's own rule applies — a family is registered as
THIS UNIT'S OWN even where another unit has one that looks like it, because
reuse would mean depending on another unit's module or promoting into the
shared `ks3_art/core.py`. So the family took a distinct name and kept its
assigned `bbench` prefix, which was already collision-free. Same correction the
commander made for `cover-bar`, same reason.

⚠️ The family is `mass-cover` / prefix `mcov`, NOT `cover-bar`. `r_cover_bar`
already exists in `build_ks3.py` as C2's read-only part–whole model; two
different things called `cover-bar` in one build is precisely the
`data-critique` / `data-critiq` trap. Distinct name, distinct hooks, no
collision. It is still a BAR — the naming and status are what changed, not the
drawing.

⚑ For Mide's science gate, from Design's NOTES §5 — all four answered in the
authoring brief and all four kept:

  * flag 11 — the masses. CONFIRMED and kept at 2 d.p. throughout.
    152.00 → 149.80 g losing 2.20 g of CO₂ sums exactly and is plausible bench
    data. 2.40 g Mg → 4.00 g MgO is EXACT (Mg 24, MgO 40: 0.100 mol × 40 g).
    8.00 g CaCO₃ → 4.48 g CaO is EXACT (CaCO₃ 100, CaO 56: 0.0800 mol × 56 g),
    leaving 3.52 g of CO₂. Two decimal places is correct for a school
    three-figure balance and every readout on the page keeps them.
  * flag 12 — "the air in a classroom weighs around 150 kg". CONFIRMED: air is
    about 1.2 kg per cubic metre, so 150 kg is a room of about 125 m³, which
    is an ordinary classroom. Kept, with Design's own hedge "around".
  * flag 13 — phlogiston, and negative mass. CONFIRMED and KEPT WHOLE. It is
    real nature-of-science and it is the best setup there is for why weighing
    a sealed flask ended the argument.
  * flag 14 — "mass is not quite conserved in nuclear reactions". TRUE, and
    easy to over-read, so the HEDGE WAS STRENGTHENED rather than the claim
    dropped. See the `stretch` list.
"""

# ── the four mass-bench runs (NOTES §3, Design's `RUNS`) ────────────────
#
# TWO DIALS, FOUR COMBINATIONS, AND ALL FOUR ARE AUTHORED. §5A: enumerate the
# whole state space, and key the note to WHICH dials are set rather than to how
# many have been touched. Each note branches on the thing the lesson teaches —
# whether the vessel can let a gas across the pan — and never on a proxy.
#
# ⚠️ THE THIRD TILE IS NOT MEASURED ON THE OPEN RUNS, AND THAT IS THE LESSON.
# An open flask never tells you the mass of the gas; it tells you two readings
# and leaves the subtraction to you. Printing a number there would answer
# `#s-worked` three sections early. On the sealed runs the honest reading is
# `0.00 g`, and it is a reading rather than an absence.
#
# ⚠️ NOTHING HERE IS COMPUTED. All four runs are in the document at rest and
# one is shown (EMIT-BOTH-SHOW-ONE), so the deltas quoted in Design's own
# notes — "fell by 2.20 g", "rose by 1.60 g" — are authored reveal sentences
# and not a figure the instrument works out and then contradicts.
_RUNS = [
    {"id": "marble:open",
     "before": "152.00 g",
     "after": "149.80 g",
     "third": "not measured — you work it out",
     "third_note": "The mass of carbon dioxide that left the flask.",
     "note": "The reading fell by 2.20 g. Nothing was destroyed: carbon "
             "dioxide bubbled out of the open neck and walked off the pan. "
             "The 2.20 g is now in the room."},
    {"id": "marble:sealed",
     "before": "152.00 g",
     "after": "152.00 g",
     "third": "0.00 g",
     "third_note": "Nothing left the flask.",
     "note": "Not a hundredth of a gram. The same reaction happened — the "
             "chips still fizzed away — and with the gas trapped on the pan "
             "the balance has nothing to report."},
    # ⊕ RULED 28 Aug 2026 (MRB-295, C4-7 / C2-9). This run used to read
    # 2.40 g → 4.00 g — the MAGNESIUM ALONE — under tiles that say "Flask,
    # contents and everything on the pan", which makes a 2.40 g reading
    # physically impossible. Ruled: whole apparatus on the pan in BOTH runs,
    # preserving the +1.60 g gain. 84.60 g is an 82.20 g crucible plus
    # 2.40 g of magnesium; 86.20 g is the same crucible plus 4.00 g of
    # magnesium oxide. The chemistry underneath is unchanged and still
    # exact, and the FIFA worked example still states 2.40 and 4.00 outright.
    # C2's conservation-of-mass bench now carries the identical pair.
    {"id": "magnesium:open",
     "before": "84.60 g",
     "after": "86.20 g",
     "third": "not measured — you work it out",
     "third_note": "The mass of oxygen that joined the magnesium.",
     "note": "The reading rose by 1.60 g. The extra mass came out of the air: "
             "oxygen atoms are now part of the white powder, and they are "
             "being weighed for the first time."},
    {"id": "magnesium:sealed",
     "before": "250.00 g",
     "after": "250.00 g",
     "third": "0.00 g",
     "third_note": "Nothing entered or left the flask.",
     "note": "Sealed, with the air already inside and weighed. The magnesium "
             "still burns and still takes oxygen, but the oxygen was on the "
             "pan before the reaction and is on the pan after it. No change."},
]

# ── the four FIFA steps, watched (MRB-204 part 3, Design's `WORKED`) ────
#
# `Fine-tune` rather than `Fix` for the second F, which is Design's wording on
# every C4 page and is the better word: what the step does is rearrange, not
# repair. The badges are `aria-hidden` reinforcement; each step's real name is
# real text beside it.
_WORKED = [
    {"letter": "F", "name": "Formula",
     "maths": "total mass of reactants = total mass of products",
     "note": "Write the rule before you touch a number. It is the same rule "
             "for every question in this lesson."},
    {"letter": "I", "name": "Insert",
     "maths": "152.00 = 149.80 + mass of gas",
     "note": "The flask started at 152.00 g. Afterwards, 149.80 g is still on "
             "the balance and the rest of the products left as gas."},
    {"letter": "F", "name": "Fine-tune",
     "maths": "mass of gas = 152.00 − 149.80",
     "note": "The quantity asked for is not on the left, so rearrange until "
             "it is on its own. Covering \"the gas\" on the bar gives you "
             "this line."},
    {"letter": "A", "name": "Answer",
     "maths": "mass of carbon dioxide = 2.20 g",
     "note": "Two decimal places, because that is what the balance gave you, "
             "and grams — the unit belongs to the answer."},
]

# ── the same four, done by the STUDENT (MRB-204 part 4, `CHECKS`) ───────
#
# ⚖️ A COMPARE BUTTON PER STEP, NOT ONE REVEAL AT THE END. That is the whole
# difference between part 3 and part 4 and it is what NOTES §4 asks for: a
# student who writes all four lines and then opens one panel has marked an
# answer; a student who commits to a line and opens THAT line has been caught
# at the step they got wrong, while it still matters.
#
# The reaction is deliberately the OTHER one — magnesium gains where marble
# loses — so that the transfer being asked for is real. The formula does not
# move; the rearranging does.
_CHECKS = [
    {"letter": "F", "name": "Formula",
     "prompt": "Write the rule down.",
     "maths": "total mass of reactants = total mass of products",
     "note": "Unchanged. It does not matter that this reaction gains mass "
             "rather than losing it."},
    {"letter": "I", "name": "Insert",
     "prompt": "Put in what you know. The reactants are the magnesium and the "
               "oxygen; the product is the magnesium oxide.",
     "maths": "2.40 + mass of oxygen = 4.00",
     "note": "Both reactants go on the left of the equals sign, because both "
             "of them were there at the start — even though one came out of "
             "the air."},
    {"letter": "F", "name": "Fine-tune",
     "prompt": "Rearrange so the quantity you want is on its own.",
     "maths": "mass of oxygen = 4.00 − 2.40",
     "note": "A part, again — so a subtraction, again. The bar with \"the "
             "gas\" covered is the same picture, with the gas joining instead "
             "of leaving."},
    {"letter": "A", "name": "Answer",
     "prompt": "Work it out, and give the unit.",
     "maths": "mass of oxygen = 1.60 g",
     "note": "1.60 g of oxygen came out of the air and is now part of the "
             "powder. Weigh the flask before and after in a sealed vessel and "
             "you would see no change at all."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 211 character for character.
    "slug":        "mass-in-a-reaction",
    "title":       "Mass in a reaction",
    "discipline":  "chemistry",
    "unit":        "chemical-reactions",
    "family":      "QUANTITATIVE",

    # ── curriculum position ─────────────────────────────────────────────────
    # ⚖️ RULED (MRB-246), and the full reasoning is written against
    # `KS3.C.AEC.04` in `ks3_data/substatements.py`. Design's NOTES-C4 §1 asked
    # whether this lesson may REFERENCE a statement C2 already owns without
    # double-counting coverage. It may not: `validate()` requires a non-empty
    # `covers` on every authored lesson, so "reference and own nothing" is not
    # a shape this build has. The alternative Design offered — fold the lesson
    # into C2 and lose the four-part treatment — was the worse trade, because
    # the treatment IS what makes a QUANTITATIVE lesson, and mass in a
    # REACTION belongs in the reactions unit.
    #
    # So the bullet was split at the seam it names out loud — "conservation of
    # mass changes of state AND chemical reactions". c2-06 owns clause `a` and
    # establishes the principle where nothing new is made; this lesson owns
    # clause `b` and carries it into the case where something is, and weighs
    # it. Not one student-facing byte of c2-06 moved: `covers` records which
    # lesson is ANSWERABLE for a clause, never which lesson may mention it.
    "covers":      ["KS3.C.AEC.04b"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "particles", "level": 2},
                    {"id": "substances-and-reactions", "level": 4}],
    "typical_year": 8,
    "typical_minutes": 60,

    # ── progression edges ───────────────────────────────────────────────────
    # ⚠️ `requires` IS THE ARGUMENT'S EDGE, NOT THE PAGE ORDER. Design's
    # "Before this lesson" card links to `word-equations`, which is simply the
    # lesson before this one; the real dependency is `reactions-rearrange-atoms`
    # — mass is conserved BECAUSE the atoms are rearranged rather than made,
    # and a student who has not met that has no reason to believe the rule.
    # Nothing is lost by saying so: the endmatter's "Where to next" card
    # renders both neighbours from the unit order, so `word-equations` is still
    # one click away as "Previous".
    "requires":    ["reactions-rearrange-atoms"],
    "assumes":     ["conservation-of-mass"],
    "references":  ["symbol-equations-and-balancing"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "One reaction on a balance loses two grams and another "
                    "gains one and a half. Both obey the same rule — so what "
                    "is the balance actually telling you?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # SEVEN stops, Design's `RAIL` in her order with her ids and her `short`
    # labels. `done_when` restates her own `DONE()` (page lines 549–558) rather
    # than guessing: the hook and `#s-think` on a commitment, the bench when
    # all four runs have been run, the bar on the first cover press, the worked
    # example when all four steps are open, `#s-check` when all four have been
    # compared, the ladder when every rung is answered and both self-marked
    # rungs checked.
    #
    # MRB-208: credit is a RATCHET and nothing is ticked on load. All four
    # instruments ship `data-stage-done="0"`.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Candle and steel wool", "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "The balance bench",     "done_when": "all_four_run"},
        {"anchor": "s-cover",  "short": "COVER",
         "label": "The rule, drawn",       "done_when": "cover_chosen"},
        {"anchor": "s-worked", "short": "WORKED",
         "label": "Watched first",         "done_when": "all_steps_opened"},
        {"anchor": "s-check",  "short": "CHECK",
         "label": "Now you",               "done_when": "all_steps_compared"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Do gases weigh?",       "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",        "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚠️ THREE DISTRACTORS RE-AUTHORED FOR LENGTH PARITY (MRB-177 / §13).
    # Design's set ran 7 / 15 / 8 / 10 words with the correct answer at 15 —
    # strictly longest by 5 words and by 1.5×, which is a set a student can
    # score without reading. **Fixed AT THE DISTRACTOR, exactly as the ruling
    # requires**: the correct option is byte-identical to Design's, and A, C
    # and D were rewritten as WRONG RULES IN THE CORRECT ANSWER'S OWN SHAPE —
    # a claim about what happens, then a clause about what the balance is
    # therefore showing. They now run 15 / 15 / 15 / 16, so the correct answer
    # is not the longest at all.
    #
    # Each rewritten distractor is a rule a real student holds: matter is
    # created and destroyed by burning (A); heat is a substance with mass (C);
    # which way the reading moves is decided by the state of the thing burning
    # (D). C is `REACT-07`'s sibling and rung 1 confronts it again.
    "phenomenon": {
        "kind": "narrative",
        "title": "A candle burns away to almost nothing. Steel wool burns and "
                 "gets heavier.",
        "prompt": "Both are burning. Both are on a balance. One reading falls "
                  "and the other rises, and neither of them is doing anything "
                  "strange — the same rule is behind both.",
        "commit": "What is the rule?",
        "options": [
            "Burning destroys some matter and creates some — the balance is "
            "showing both of those",
            "The total mass never changes — the balance only weighs what "
            "stays on the pan",
            "Heat has mass — the balance only weighs what is still warm on "
            "the pan",
            "Solids gain mass as they burn and liquids lose it — the state "
            "decides which way",
        ],
        "reveal": "Nothing is created and nothing is destroyed — but the "
                  "balance only weighs what is <strong>on the pan</strong>. "
                  "The candle's products float away, so the reading falls. "
                  "The steel wool takes oxygen out of the air and keeps it, "
                  "so the reading rises. Count everything, including the "
                  "gases, and the total never changes at all.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ BOTH JOINS RESOLVE TO SOMETHING THE PAGE ACTUALLY EMITS (MRB-244/248):
    #
    #   elicited_by  "think-commit-gas"  → the `#s-think` activity's own id,
    #                                      rendered as data-activity="think-commit-gas"
    #   confronted_by "sealed-flask-run" → the balance bench's activity id,
    #                                      rendered as data-activity="sealed-flask-run"
    #                                      on the `#s-bench` section
    #
    # The bench is named for what confronts the belief rather than for where it
    # sits, because the sealed runs ARE the confrontation: seal the flask so
    # the gas cannot leave and the reading does not move by a hundredth of a
    # gram. That is the confrontation being a real ACTIVITY id, which Law 3
    # requires of at least one entry.
    #
    # ⚠️ `statement` is the line the PAGE quotes (page line 304), not NOTES
    # §6's shorter register handle ("Gases have no mass, so a gas escaping
    # cannot change a balance reading"). `r_confrontation` prints `statement`,
    # and Design's is the one a student says out loud. Same reconciliation
    # c3-03 made for MIX-06.
    #
    # ⚑ CROSS-REFERENCE, NOT A RE-MINT (NOTES §6). `REACT-07` is `ATOM-11` and
    # `PART-05` in a chemical costume — the belief that something you cannot
    # feel the weight of has no mass. The chain is four IDs long. Design's own
    # note asks for a cross-family "same belief" link TYPE in the register
    # rather than a prose note; that is a request on the register's owner and
    # not something this lesson may invent, so it is recorded here in prose and
    # nothing is re-minted. The `#s-think` reveal makes the link out loud —
    # "the same wrong idea as thinking a dried-up puddle was destroyed".
    "misconceptions": [
        {"id": "REACT-07",
         "statement": "Gases do not weigh anything, so the missing 2.20 g "
                      "cannot be the carbon dioxide.",
         "elicited_by": "think-commit-gas",
         "confronted_by": "sealed-flask-run"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the balance bench. Light `ks3-block` → `check`.
        # Its ACTIVITY id is `sealed-flask-run`; see the misconception note.
        {"type": "mass-bench", "id": "sealed-flask-run", "anchor": "s-bench",
         "eyebrow": "Your turn · the balance bench",
         "heading": "Two reactions, two flasks. Predict what the balance "
                    "does.",
         "demand": "investigate",
         "dials": [
             {"id": "reaction", "label": "The reaction",
              "options": [{"id": "marble", "label": "Marble chips + acid"},
                          {"id": "magnesium", "label": "Burning magnesium"}]},
             {"id": "vessel", "label": "The flask",
              "options": [{"id": "open", "label": "Open to the air"},
                          {"id": "sealed", "label": "Sealed"}]},
         ],
         # Law 4: the reading is not shown until the student has said what they
         # expect. The gate takes the Run button's place until they commit.
         "predict": {
             "prompt": "Before you run it: what will the balance reading do?",
             "options": ["Go down", "Stay the same", "Go up"],
             "run_label": "Run the reaction"},
         # The two fixed tiles. The third tile's value and note come from the
         # run, because they are the only part of the readout that is not the
         # same sentence four times.
         "tiles": [
             {"id": "before", "label": "Balance before",
              "note": "Flask, contents and everything on the pan."},
             {"id": "after", "label": "Balance after",
              "note": "The same pan, once the reaction has finished."},
             {"id": "gas", "label": "Mass of gas"},
         ],
         "runs": _RUNS,
         "close": "All four runs. Open and fizzing: the reading falls. Open "
                  "and burning: the reading rises. Sealed, either reaction: "
                  "the reading does not move by so much as a hundredth of a "
                  "gram. <strong>The reaction never changes the mass. The lid "
                  "decides whether the balance can see it.</strong>"},

        # ── MRB-204 part 1 — THE RULE ALONE IN ITS OWN BLOCK ───────────────
        # No anchor and no rail stop: it is read, not done, and MRB-208 keeps
        # anything that cannot tick off the rail. Design draws it as a
        # classless section between the bench and the bar.
        #
        # ⚠️ ONE SENTENCE CUT (§8.10). Design's support line reads "Nothing
        # else is in this block, because nothing else needs to be. Every
        # calculation in this lesson is that line with one of its numbers
        # missing." The first sentence is the platform explaining its own
        # layout decision to a reader who did not ask — §8.10's test, applied:
        # it is not telling the student what to do with the thing in front of
        # them. The second sentence is teaching and is kept whole, so the seam
        # lands as a complete sentence rather than as a raw string delete.
        {"type": "formula", "id": "the-rule",
         "eyebrow": "The rule",
         "statement": "total mass of reactants = total mass of products",
         "support": ["Every calculation in this lesson is that line with one "
                     "of its numbers missing."]},

        # ── MRB-204 part 2 — DRAWN, AS A PART–WHOLE BAR ────────────────────
        # ⚖️ A BAR, NEVER A TRIANGLE. See the module docstring; this is the
        # ruled shape for a sum and it must not be redrawn.
        # ⚠️ AN ACTIVITY, NOT `r_cover_bar`. See the module docstring: Design's
        # RAIL and DONE() both name `s-cover`, so it ticks a stop and carries
        # `data-stage-done="0"`.
        {"type": "mass-cover", "id": "cover-the-bar", "anchor": "s-cover",
         "eyebrow": "The bar",
         "heading": "Cover the one you want",
         "demand": "investigate",
         # Design draws the plain-English restatement in a bordered card at the
         # top of this section, above the eyebrow. The activity shell emits its
         # eyebrow and <h2> first, so the card is the instrument's own opening
         # element and lands one row lower than on the reference — the only
         # ordering difference between this section and Design's, and reported
         # as such. The two statements are the same rule in two registers: the
         # formal one above, the plain one here, and they cannot disagree.
         "rule": "Total mass of everything before = total mass of everything "
                 "after",
         "aria_label": "A part-whole bar. One long bar labelled everything "
                       "before, 152.00 grams, sits above two shorter bars "
                       "that together fill the same width: left in the flask, "
                       "149.80 grams, and the gas, 2.20 grams. The two shorter "
                       "bars are sized to be readable rather than to scale.",
         "whole": {"id": "total", "label": "Everything before",
                   "value": "152.00 g", "button": "Cover everything before"},
         # ⚠️ THE WEIGHTS ARE DESIGN'S OWN 68 / 32 GRID, AND THEY ARE NOT THE
         # RATIO OF THE MASSES. 2.20 g is one part in about seventy of 152.00 g;
         # drawn true, the gas cell would be a six-pixel sliver with a 24px
         # number in it and nothing would be readable at 390px. §5A says drawn
         # geometry must express the ratio its label claims, so the honest fix
         # is to SAY SO rather than to lie or to shrink the cell into
         # illegibility — see `scale_note` below, which turns the disclaimer
         # into a quantity a student can read.
         "parts": [
             {"id": "left", "label": "Left in the flask",
              "value": "149.80 g", "weight": 68,
              "button": "Cover left in the flask"},
             {"id": "gas", "label": "The gas",
              "value": "2.20 g", "weight": 32,
              "button": "Cover the gas"},
         ],
         # ⚠️ NEW PROSE, and it is a science-honesty line rather than a
         # decoration. See the weights note above.
         "scale_note": "The cells are sized so you can read them. Drawn to "
                       "scale, the gas would be about one part in seventy of "
                       "the whole bar.",
         # Radio, never a toggle, and it opens with NOTHING covered — Design's
         # `cover: null`. The stop ticks on the first press.
         #
         # ⚠️ THE `sentence` FIELD IS RESTORED. Design authored a `sentence`
         # for all three covers in her `COVERS` constant and her NOTES §4
         # describes the panel as "the arrangement that falls out, AND one
         # sentence naming the operation" — but her markup renders only
         # `coverResult`, so the three sentences never reach the page. That
         # reads as an oversight rather than a cut: the data is authored, the
         # notes promise it, and the sentences are where the addition/
         # subtraction is actually named. Rendered here, byte-identical.
         "results": {
             "total": {
                 "result": "everything before = left in the flask + the gas",
                 "sentence": "An addition. Use this when you know what stayed "
                             "and what left, and want the mass you started "
                             "with — 149.80 + 2.20 = 152.00 g."},
             "left": {
                 "result": "left in the flask = everything before − the gas",
                 "sentence": "A subtraction. Use this when you know the "
                             "starting mass and how much gas escaped, and "
                             "want the mass remaining."},
             "gas": {
                 "result": "the gas = everything before − left in the flask",
                 "sentence": "A subtraction, and the one an open flask always "
                             "asks for: the gas is the quantity nobody "
                             "measured, so it is the difference between the "
                             "two readings."},
         },
         "close": "Two parts side by side make the whole. Cover the part you "
                  "want and take the other one away from the whole.",
         # The unit belongs to the quantity, and the page says so three times
         # before the worked example's Answer step says it once more.
         "units": [
             {"quantity": "everything before, gases included", "unit": "g"},
             {"quantity": "left in the flask", "unit": "g"},
             {"quantity": "the gas that left", "unit": "g"},
         ]},

        # ── MRB-204 part 3 — WATCHED, ONE STEP AT A TIME ───────────────────
        {"type": "mass-worked", "id": "worked-marble", "anchor": "s-worked",
         "eyebrow": "Watched first · FIFA",
         "heading": "How much carbon dioxide left the open flask?",
         "demand": "investigate",
         "prompt": "Marble chips and acid in an open flask. The balance read "
                   "152.00 g at the start and 149.80 g when the fizzing "
                   "stopped. Four steps, one at a time.",
         "steps": _WORKED,
         # EMIT-BOTH-SHOW-ONE: both labels are in the document and one is
         # shown, so neither sentence is composed in JS.
         "first_label": "Show the first step",
         "next_label": "Show the next step"},

        # ── MRB-204 part 4 — THE STUDENT'S OWN RUN, COMPARED PER STEP ──────
        {"type": "mass-check", "id": "check-magnesium", "anchor": "s-check",
         "eyebrow": "Now you · same four steps",
         "heading": "2.40 g of magnesium burns and leaves 4.00 g of magnesium "
                    "oxide. What mass of oxygen joined in?",
         "demand": "construct",
         "prompt": "Do each step yourself, then open it to compare. The steps "
                   "are the same four; only the numbers and the missing "
                   "quantity have moved.",
         "steps": _CHECKS,
         # A TEMPLATE, not four sentences: the number is the instrument's, and
         # §5A forbids hard-coding a figure the instrument owns.
         "compare_label": "Compare step {n}",
         "close": "Notice what changed between the two questions and what did "
                  "not. The formula did not change. The rearranging did — in "
                  "the first one the missing quantity was a part, in this one "
                  "it is also a part, but it was on the other side of the "
                  "arrow. <strong>Which side a substance is on decides "
                  "whether it is added or subtracted; the rule itself never "
                  "moves.</strong>"},

        {"type": "key-fact", "ref": "the-balance-only-sees-the-pan"},

        {"type": "misconception", "id": "think-commit-gas", "anchor": "s-think",
         "targets": "REACT-07"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # None. The one drawing this lesson has is the part–whole bar, and the bar
    # is not a figure: its cells are covered and uncovered by the student, so
    # it belongs inside the instrument that covers them. A `figure` block would
    # be a second, uncoverable copy of the same picture.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "the-balance-only-sees-the-pan",
         "text": "Total mass of reactants = total mass of products. A balance "
                 "reading that changes is telling you a gas has entered or "
                 "left the pan — not that mass has been created or destroyed.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # `#s-think` only. The four instruments are lifted out of `core` into this
    # list by `_normalise()` and are never authored here.
    #
    # ⚠️ Option lengths measured (MRB-177): 5 / 11 / 7 / 10 tokens, correct at
    # 11 against a longest distractor of 10 — one token, well inside both
    # thresholds. Design's set is kept byte-identical.
    "activities": [
        {"id": "think-commit-gas",
         "kind": "predict",
         "demand": "explain",
         "targets": "REACT-07",
         "prompt": "You cannot feel the air, and nothing you have ever picked "
                   "up has felt heavier for having gas in it. Commit before "
                   "you read on.",
         "options": [
             "Right — gases are weightless",
             "Wrong — gases have mass, and a sealed flask proves it",
             "Right, unless the gas is under pressure",
             "Wrong — gases have mass but it cannot be measured",
         ],
         # ⚑ Science flag 12 is the first sentence of the first paragraph and
         # it is KEPT with Design's own hedge. Air is about 1.2 kg per cubic
         # metre, so "around 150 kilograms" is a room of about 125 m³ — an
         # ordinary classroom. The football is the version a student can
         # actually do.
         "reveal": [
             "Gases have mass, and it is easy to measure. The air in an "
             "ordinary classroom weighs around 150 kilograms. A cubic metre "
             "of carbon dioxide is nearly two kilograms. Weigh a football, "
             "pump it up hard, weigh it again: the reading goes up, and the "
             "only thing you added was air.",
             "What gases lack is not mass but <strong>weight you can "
             "notice</strong> — they are spread out, and the air around you "
             "pushes up on everything, so nothing feels heavier for "
             "containing gas. The sealed flask settles it: seal the reaction "
             "so the gas cannot leave and the balance does not move at all. "
             "The gas was on the pan the whole time. This is the same wrong "
             "idea as thinking a dried-up puddle was destroyed, in a chemical "
             "costume.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Design's RUNGS → recall + apply, SELF_RUNGS → explain + produce.
    #
    # Her headings for rungs 1, 2 and 4 are the engine's own defaults character
    # for character ("Recall", "The one that catches people", "Take it
    # somewhere new"), so those three author no `title`. Rung 3 overrides the
    # default "Explain" with "Produce a calculation", which is Design's wording
    # and the honest one: the rung asks for four worked lines and a prediction,
    # not for a paragraph.
    #
    # ⚠️ Length measured on both marked rungs (MRB-177), in the gate's own
    # tokens. Rung 1: 4 / 7 / 7 / 8, correct is the SHORTEST. Rung 2: 11 / 10 /
    # 7 / 8, correct clears the longest distractor by one token. Both pass on
    # both thresholds and neither needed a distractor rewritten.
    "ladder": {
        "recall": {
            "q": "A reaction is carried out in a sealed flask on a balance. "
                 "What happens to the reading?",
            "options": [
                "It stays the same",
                "It falls, because a gas is made",
                "It rises, because new substances are made",
                "It depends whether the reaction gives out heat",
            ],
            "answer": 0,
            "feedback": {
                1: "A gas may well be made — and in a sealed flask it is "
                   "still on the pan, so the balance does not notice.",
                2: "New substances are made from the atoms already present. "
                   "No atoms were added, so no mass was added.",
                3: "Heat leaving does not take any measurable mass with it. "
                   "The reading is unmoved.",
            }},
        "apply": {
            "q": "2.40 g of magnesium is burned in an open dish and 4.00 g of "
                 "white powder is left. What has happened?",
            "options": [
                "1.60 g of mass has been created by the reaction",
                "The balance has drifted and needs re-zeroing",
                "The magnesium has absorbed heat, which has mass",
                "1.60 g of oxygen from the air has joined the magnesium",
            ],
            "answer": 3,
            "feedback": {
                0: "Mass is never created. Every gram of the extra 1.60 g can "
                   "be traced to oxygen that was in the air before the "
                   "reaction.",
                1: "A gain of 1.60 g on 2.40 g is far too large to be drift, "
                   "and it is repeatable — the same gain every time.",
                2: "Heat carries no measurable mass. What was absorbed was "
                   "oxygen, and it is now part of the powder.",
            }},
        # ⚑ Science flag 11's third figure pair. 8.00 g CaCO₃ → 4.48 g CaO is
        # exact (CaCO₃ 100, CaO 56), so the carbon dioxide is 3.52 g exactly.
        "explain": {
            "title": "Produce a calculation",
            "q": "8.00 g of calcium carbonate is heated in an open crucible. "
                 "It decomposes to calcium oxide and carbon dioxide, and 4.48 "
                 "g of calcium oxide is left. Work out the mass of carbon "
                 "dioxide given off, showing all four steps, and then explain "
                 "what the balance would have read if the crucible had been "
                 "sealed.",
            "field_label": "Your calculation and explanation",
            "placeholder": "Formula: total mass of reactants = total mass of "
                           "products…",
            "success": [
                "Writes the rule down as the first step.",
                "Inserts the values correctly: 8.00 = 4.48 + mass of carbon "
                "dioxide.",
                "Rearranges to make the unknown the subject: mass of carbon "
                "dioxide = 8.00 − 4.48.",
                "Gives the answer as 3.52 g, with the unit.",
                "Says a sealed crucible would show no change, because the gas "
                "would still be on the pan.",
            ]},
        "produce": {
            "q": "A student burns a candle on a balance and records a loss of "
                 "4.10 g. They conclude that burning destroys matter. Design "
                 "the measurement that would prove them wrong, say what "
                 "result you would expect, and explain why their reading was "
                 "not evidence of destruction.",
            "field_label": "Your answer",
            "placeholder": "The problem with the open balance is…",
            "success": [
                "Identifies the problem: the products are gases and left the "
                "pan.",
                "Proposes enclosing the reaction so nothing can enter or "
                "leave — a sealed vessel with enough air in it.",
                "Predicts the result: the balance reading does not change.",
                "Explains that the candle wax and the oxygen used are "
                "together equal in mass to the carbon dioxide and water made.",
                "Says the open reading measured what stayed behind, not what "
                "existed — which is a limitation of the method, not a fact "
                "about matter.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Total mass of reactants = total mass of products. Atoms are "
                "rearranged, never created or destroyed, so the total cannot "
                "change. A balance reading that falls means a gas has left "
                "the pan; one that rises means a gas has joined from the air. "
                "Seal the vessel and the reading does not move. The "
                "relationship is a sum, so it is drawn as a part-whole bar: "
                "cover the quantity you want and what is left is the "
                "calculation.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ Science flag 13 is the first paragraph and it is KEPT WHOLE. Phlogiston
    # is real nature-of-science and it is the best setup there is for why
    # weighing a sealed flask ended an argument — the negative-mass line is the
    # part that shows what a theory looks like when it is losing.
    #
    # ⚑ Science flag 14 is the second paragraph's second half, and ⚠️ THE HEDGE
    # WAS STRENGTHENED. Design's read: "mass is conserved in chemical reactions
    # and in nuclear reactions it is not quite: a tiny amount of mass becomes
    # energy, which is where the Sun's output comes from. Nothing you do in a
    # flask goes anywhere near that, and the rule you have just learned is safe
    # for the whole of chemistry."
    #
    # That is true, and it is easy to over-read as "so the rule has exceptions".
    # The rewrite makes the hedge do four jobs instead of two: it says WHERE
    # (a star or a reactor), it says WHAT IS DIFFERENT (the atoms themselves
    # change rather than rearrange — which is c4-02's sentence, so the two
    # lessons agree), it says NOTHING ON A BENCH BEHAVES THAT WAY, and it says
    # IT IS NEVER AN EXCEPTION A CHEMISTRY ANSWER NEEDS. "First," is untouched
    # and the seam lands as a whole sentence.
    "stretch": [
        {"type": "explainer", "id": "phlogiston",
         "text": "This rule was the argument that ended a whole theory. For "
                 "most of the eighteenth century, burning was explained by "
                 "<em>phlogiston</em> — a substance said to escape from "
                 "things as they burned, which neatly explained why a candle "
                 "got lighter. Then metals were burned in sealed vessels and "
                 "weighed, and they got <em>heavier</em>. Defenders of the "
                 "theory were reduced to suggesting phlogiston had negative "
                 "mass. Lavoisier weighed everything, including the air, and "
                 "showed that the gain in the metal was exactly the loss from "
                 "the air in the vessel. The theory did not survive a "
                 "balance."},
        {"type": "explainer", "id": "two-footnotes",
         "text": "Two honest footnotes. First, a school balance reads to a "
                 "hundredth of a gram, so a reaction losing a milligram of "
                 "gas looks perfectly conserved — the rule is exact and the "
                 "measurement is not. Second, mass is conserved in every "
                 "chemical reaction there is. In a <strong>nuclear</strong> "
                 "reaction — inside a star or a reactor, where the atoms "
                 "themselves change rather than rearrange — a tiny amount of "
                 "mass becomes energy instead, and that is where the Sun's "
                 "output comes from. That is not chemistry, nothing on any "
                 "bench in any school behaves that way, and it is never an "
                 "exception a chemistry answer needs. The rule you have just "
                 "learned is exact for the whole of chemistry."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent. Design
    # draws no "Need a hand?" layer on this page, and the scaffolding a
    # struggling student needs is already the lesson's spine: `#s-check` is a
    # supported repeat of `#s-worked` with a compare button on every line.
    "support": [],

    # ── vocabulary (§10.2, §12) ─────────────────────────────────────────────
    # ⚠️ `definition` + `note`, not `gloss`. The build contract's §12 names the
    # key `gloss`; the SHIPPED schema is `{"term", "definition", "note"}` —
    # that is what `r_cards` reads (build_ks3.py:922) and what all 58 live
    # lessons author. Authored to the shipped spelling so the terms reach the
    # unit page's "Words this unit gives you" chips and the reading-age gate's
    # exclusion list; reported to the commander.
    #
    # Design draws no keyword block on this page, so none of these definitions
    # reaches the lesson body — the list is the lesson's term record.
    "vocabulary": [
        {"term": "Conservation of mass",
         "definition": "The rule that the total mass of the products of a "
                       "reaction equals the total mass of the reactants.",
         "note": "It is a sum, which is why it is drawn as a bar and never "
                 "as a triangle."},
        {"term": "Reactant",
         "definition": "A substance that is there at the start of a reaction "
                       "and is used up in it.",
         "note": "Oxygen from the air is a reactant even though nobody "
                 "weighed it out."},
        {"term": "Product",
         "definition": "A substance that is made by a reaction.",
         "note": None},
        {"term": "Sealed vessel",
         "definition": "A container closed so that no gas can enter it or "
                       "leave it.",
         "note": "Sealing does not change the reaction. It changes what the "
                 "balance can see."},
    ],

    # ── safety (§1.5) ───────────────────────────────────────────────────────
    # None, deliberately, and the reasoning is in the report. This page carries
    # no method: burning magnesium is described as something that happens on a
    # bench, not as something the reader is asked to set up, and there is
    # nothing here a student could do at home. C3's filtration earned a
    # `safety_note` because its own rung 3 credited tasting; this lesson asks
    # for no action at all. A safeguarding block is a different thing again
    # (§16) and this is a substance lesson, not a lesson about a student's own
    # body, health or risk.

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure how burning magnesium can get heavier?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    "ks4_becomes": "Relative formula mass, moles, and reacting-mass "
                   "calculations — all of them this rule with the arithmetic "
                   "done in particles.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # `measurement` because the whole lesson is what a balance reading means
    # and what it does not, and the stretch layer names the resolution of the
    # instrument as a real limit.
    "ws": ["measurement", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
