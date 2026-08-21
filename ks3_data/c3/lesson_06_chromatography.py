"""C3 L6 — Chromatography (PROCESS).

Authored against Design's approved page,
`docs/ks3/design-reference/c3/c3-06-chromatography.dc.html` (644 lines), and
Design's unit notes `docs/ks3/design-reference/c3/NOTES-C3.md` §2, §3.4, §4, §5
and §6.

Every student-facing string is byte-identical to the approved page. `RAIL`,
`LANES`, `FAULTS`, `RUNGS` and `SELF_RUNGS` came out of the node extractor;
the hook options, the three dial labels and their option labels, the run
button's label, both paper alt texts, the good run's title and text, the
verdict prompt, its note, its four button labels and all five verdict bodies,
the four think options, the explainer, the key fact, the key note and both
"Going further" paragraphs were lifted from `lessonVals(s)` and from the
markup, which is where the other ~700 words of this lesson live.

── Three decisions, three distinct ruins ───────────────────────────────

NOTES §2 (`c3-06`): *"the only lesson in the unit where the student can produce
an unreadable result and be told exactly why."* The three faults are the
teaching, and each one names WHICH decision caused it — pen baseline, solvent
above the spots, paper left in too long — rather than saying merely that
something went wrong. None of them says the student got it wrong, and none of
them is softened. `fault_order` fixes the precedence Design's page computes
(`penline`, then `drowned`, then `overrun`), so a run with two faults set is
explained by the first one rather than by whichever the renderer happens to
test first.

── Rf is a PERCENTAGE OF A LANE, never a pixel ─────────────────────────

NOTES §3.4: `chroma-run` *"positions spots by Rf as a percentage of a
fixed-height lane, so a real figure can replace it without changing the
payload."* So `lanes[].spots[].rf` is authored as the R_f value itself — a
dimensionless 0–1 ratio, which is the actual science — and `lane_geometry`
carries the only two numbers that turn it into a position, both in PERCENT of
the lane's own height. Nothing here is in pixels except the lane height, which
is the fixed height the percentages are of. Swap the lane for a drawn figure
and every rf survives untouched.

── The tug of war, and nothing else ────────────────────────────────────

The explainer, the key fact, the key note, rung 3's criteria and the `#s-think`
reveal all say the same thing in the same terms: each dye is pulled two ways,
sticking to the paper against dissolving in the moving solvent. Nothing in this
lesson is about the size of a particle and nothing is about how much was put
on. That is deliberate and it is what makes MIX-12 confrontable — if height
were about amount, or about size, the confrontation would have nothing to
stand on.

⚑ For Mide's science gate, from Design's NOTES §4:
  * flag 13 — the R_f subscript is authored as `<sub>`, NOT as a Unicode
    subscript, per Design's ruling and now the convention for the whole
    course. KEPT, byte-identical, in three strings: rung 4's fifth criterion,
    the "Going further" first paragraph, and `ks4_becomes`.
    ⊕ RESOLVED (MRB-272). This note used to warn that `rich()`'s allow-list
    was `("em", "strong")` and that these three strings were rendered by
    `t()`, so `<sub>` shipped as visible tag soup. Both halves are fixed:
    `_RICH_OK` now admits `sub` (the ruling is written out in
    `ks3_art/kit.py`), and the three call sites in `build_ks3.py` —
    `r_criteria`, `_rung_self` and the `ks4_becomes` end-matter line — go
    through `rich()`. Verified on the built page: three real `<sub>` elements,
    zero escaped ones.
    KEPT AND MARKED rather than deleted, so that nobody reading a stale
    warning "fixes" these back to a Unicode subscript. THERE IS NO UNICODE
    SUBSCRIPT `f`; the tag is the only way to spell this symbol.
  * Design's font note — the shipped subsets carry no `→`, so no arrow
    character appears in any string in this file.

⚑ Deviations from NOTES §5's misconception register, both forced by
  `verify_ks3.py`'s MRB-244 / MRB-248 gates, which require every
  `confronted_by` and every present `elicited_by` to name an `id=` or
  `data-activity=` the built page actually emits:
  * MIX-11 `elicited_by` is `s-hook`, not the register's `hook-black-ink` —
    the hook section emits `id="s-hook"` and `data-activity="hook"`, and
    nothing on the page is called `hook-black-ink`.
  * MIX-12 `confronted_by` is `think-commit-furthest`, not the register's
    `think-reveal-tug` — the reveal is the second half of that one activity
    and has no id of its own. Both halves of MIX-12 therefore name the same
    element, which is legal and is what C2 L3 does.
  `chroma-run` is unchanged: the instrument's activity id IS `chroma-run`, so
  MIX-11's `confronted_by` resolves exactly as the register wrote it.
"""

# ── the four dye colours, from the page's own constants ─────────────────
# Design's YEL / MAG / CYA / BLU. Named here rather than inlined so the three
# pens that share a dye with the note share the LITERAL, and a colour cannot
# drift between two lanes that are supposed to match — the whole forensic
# payoff is that Pen A's three spots are the note's three spots.
YEL = "#E0A62B"
MAG = "#B3336B"
CYA = "#2F7D8A"
BLU = "#2F5D8A"

# ── the five lanes ──────────────────────────────────────────────────────
# ⚖️ `rf` IS THE R_f VALUE, 0 to 1, and it is not a pixel and not a percentage
# of anything but the solvent's own travel. `lane_geometry` below turns it into
# a position. NOTES §3.4 asks for exactly this so a drawn figure can replace
# the DOM lane later without touching a single number here.
#
# ⚖️ The evidence is in these numbers and nowhere else. The note and Pen A are
# IDENTICAL — same three dyes, same three heights. Pen B is missing the yellow
# and its magenta sits at 0.45 rather than 0.55. Pen C shares two dyes and both
# sit low (0.30 and 0.75 against 0.35 and 0.80), and it has no magenta at all.
# Pen D has one dye the note does not have. Change any of these and the verdict
# prose below stops being true.
LANES = [
    {"id": "note", "label": "The note",
     "spots": [{"c": YEL, "rf": 0.35}, {"c": MAG, "rf": 0.55},
               {"c": CYA, "rf": 0.80}]},
    {"id": "a", "label": "Pen A",
     "spots": [{"c": YEL, "rf": 0.35}, {"c": MAG, "rf": 0.55},
               {"c": CYA, "rf": 0.80}]},
    {"id": "b", "label": "Pen B",
     "spots": [{"c": MAG, "rf": 0.45}, {"c": CYA, "rf": 0.80}]},
    {"id": "c", "label": "Pen C",
     "spots": [{"c": YEL, "rf": 0.30}, {"c": CYA, "rf": 0.75}]},
    {"id": "d", "label": "Pen D",
     "spots": [{"c": BLU, "rf": 0.60}]},
]

# ── the three ruins ─────────────────────────────────────────────────────
# ⚠️ DO NOT SOFTEN THESE. Each `title` states the damage and each `text` names
# the decision that caused it in its first sentence — "You drew the baseline in
# pen", "The solvent level was above the baseline", "You left the paper in
# until the solvent reached the top" — and then says what to do instead. None
# of them says the student got it wrong, and none of them is generic.
#
# `alt` is the whole aria-label of the ruined paper, not a fragment: Design
# builds it as "A ruined chromatogram: " plus a clause, and a screen-reader
# user gets one complete sentence rather than two keys joined at build time.
#
# `spots` names the RENDERING MODE the ruined lane takes, and the numbers
# beside it are Design's own (page lines 452–457):
#   · `none`    — the ink dissolved into the tank; there is nothing to draw.
#   · `smeared` — the baseline's own dyes climbing, so every lane gets the
#     SAME ladder of smears regardless of what was spotted on it: the i-th
#     smear sits at `smear_start_rf + i * smear_step_rf`. That is the point —
#     the ruin is the baseline's, not the samples'.
#   · `crushed` — each spot driven `crush_toward_front` of the remaining way
#     to the top and capped at `crush_cap_rf`, so the fast ones pile up and
#     stop being separable while the slow ones stay just distinguishable.
FAULTS = {
    "penline": {
        "title": "The baseline has run, and it has run through everything.",
        "text": "You drew the baseline in pen. Pen ink is a mixture of dyes "
                "dissolved in a solvent — exactly the thing this experiment "
                "separates — so the line itself climbed the paper and smeared "
                "its own colours across all five lanes. Nothing can be read. "
                "Pencil is graphite: insoluble, so it stays where you drew "
                "it.",
        "alt": "A ruined chromatogram: colour smeared across all five lanes "
               "from the baseline upwards.",
        "spots": "smeared",
        "smear_start_rf": 0.20,
        "smear_step_rf": 0.12,
        # The pen baseline is drawn thicker and in ink rather than the pencil
        # rule, because a line that has run is a line you can see has run.
        "baseline": "ink",
    },
    "drowned": {
        "title": "The spots have gone. All of them.",
        "text": "The solvent level was above the baseline, so the ink dots "
                "were sitting in the liquid rather than above it. They "
                "dissolved straight into the solvent in the tank and were "
                "carried nowhere. The solvent has to start below the spots "
                "and climb up to them.",
        "alt": "A ruined chromatogram: five empty lanes, the ink having "
               "dissolved into the solvent.",
        "spots": "none",
    },
    "overrun": {
        "title": "Every spot is jammed against the top edge.",
        "text": "You left the paper in until the solvent reached the top. "
                "Once the solvent front runs off the end, the fast spots pile "
                "up against the edge and stop being separable — and there is "
                "no solvent front left to measure distances against. Take the "
                "paper out while the front is still short of the top.",
        "alt": "A ruined chromatogram: every spot crushed against the top "
               "edge of the paper.",
        "spots": "crushed",
        "crush_toward_front": 0.85,
        "crush_cap_rf": 0.97,
    },
}


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 203 character for character.
    "slug":        "chromatography",
    "title":       "Chromatography",
    "discipline":  "chemistry",
    "unit":        "mixtures-and-separation",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # NOTES §1. PIS.04 names four techniques and gets four lessons; this is the
    # fourth. ⊕ Authored as the parent `KS3.C.PIS.04` first, on the brief's §5
    # ("a statutory statement may be claimed by more than one lesson"), and
    # changed to the clause after a build: `build_ks3.py`'s DOUBLE-OWNED gate
    # does not allow the parent, and it named this lesson, `distillation` and
    # `evaporation-and-crystallisation` together. The four clauses were minted
    # mid-run in `ks3_data/substatements.py` (MRB-272, the commander's file);
    # this is clause `d`, chromatography — separating substances dissolved in
    # the same solvent from each other.
    #
    # ⚠️ The brief's §5 is untouched by this. It rules that a FACT may be
    # taught in several lessons and that duplication is not to be argued about,
    # which is why the tug of war, the pencil baseline and the solvent level
    # each appear in more than one place here. `covers` records something
    # narrower: which single lesson is answerable for a clause.
    "covers":      ["KS3.C.PIS.04d"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 2},
                    {"id": "particles", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # The page's endmatter: "Before this lesson · Distillation", "Next in this
    # unit · Proving something is pure".
    "requires":    ["distillation"],
    "assumes":     [],
    "references":  ["proving-something-is-pure"],
    "connects_heading": "Next in this unit",
    # Empty ON PURPOSE — `r_endmatter` prints `ks4_becomes` only when there is
    # no KS4 page to link, and Design's sentence is the one drawn on the page.
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Everything in the mixture is dissolved, and all of it is "
                    "the same colour. How do you separate substances that "
                    "will not sit still to be picked apart?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, from the page's own RAIL constant (page lines 326–331), and
    # four is the floor — MRB-249 fails the build on three. NOTES §6 records
    # four for `c3-06` and five or six for every other lesson in the unit;
    # this lesson has the fewest sections in C3 and that is correct, not a gap.
    # Do not add a fifth to make the unit tidy.
    #
    # `done_when` is a GATE field (R2) — the runtime ticks from
    # `data-stage-done`, which each instrument sets from its own predicate.
    # Every predicate below names state its own section owns, taken from the
    # page's `DONE()` (lines 399–405).
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "Four black pens",
         "done_when": "committed"},
        # ⚖️ The RUN stop ticks on the VERDICT, not on pressing Run. A student
        # who runs a ruined paper has not finished the section — there is
        # nothing to read and no pen to accuse — and the page agrees:
        # `s.verdict !== null`, and the verdict panel only exists on a good run.
        {"anchor": "s-lab",    "short": "RUN",    "label": "Run the paper",
         "done_when": "verdict_given"},
        {"anchor": "s-think",  "short": "THINK",  "label": "Furthest spot",
         "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # `kind` is authored and UNREAD, deliberately: build_ks3.py's note at line
    # 744 records that `phenomenon.kind` selects nothing and is reported rather
    # than pressed into service. Kept for consistency with all 58 lessons.
    "phenomenon": {
        "kind": "narrative",
        "title": "Black ink is not black. It is three or four colours "
                 "pretending.",
        "prompt": "A note has been written in black ink and four black pens "
                  "have been collected. All four inks look identical on "
                  "paper, and no amount of staring at them will tell you "
                  "which pen wrote the note.",
        "commit": "Draw a dot of each ink near the bottom of a strip of paper "
                  "and let water creep up through it. What happens?",
        # ⚖️ Option A is MIX-11 in its own words — the paper or the water
        # doing something to the colour — and C is the same belief in its
        # milder form. D is the reason the lesson has four pens rather than
        # one. The reveal answers all three at once.
        "options": [
            "The dots wash away and the paper stays blank",
            "Each dot climbs and splits into separate coloured spots",
            "The dots stay where they are and go paler",
            "All four inks give exactly the same pattern",
        ],
        "reveal": "Each dot climbs and splits into separate coloured spots — "
                  "and the pattern is different for each pen, because each "
                  "manufacturer mixes its black from a different set of dyes. "
                  "The inks are indistinguishable until you separate them. "
                  "Then they are as distinctive as handwriting.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # NOTES §5. See the module docstring for why two of the four ids differ
    # from the register's: verify_ks3.py requires each to name something the
    # built page actually emits.
    "misconceptions": [
        {"id": "MIX-11",
         "statement": "The dye or colour is made by the paper or the solvent.",
         "elicited_by": "s-hook",
         "confronted_by": "chroma-run"},
        {"id": "MIX-12",
         "statement": "The spot that travels furthest is the one there is "
                      "most of.",
         "elicited_by": "think-commit-furthest",
         "confronted_by": "think-commit-furthest"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Design draws one `.ks3-explainer` section with TWO paragraphs;
        # `r_explainer` emits one `<p>` per block, so this is two blocks. Both
        # must stay direct children of `.ks3-lesson` for the 46rem measure.
        {"type": "explainer",
         "text": "<strong>Chromatography</strong> separates substances that "
                 "are all dissolved in the same solvent. The solvent soaks up "
                 "through the paper and carries the dyes with it — but each "
                 "dye is pulled two ways: it sticks to the paper, and it "
                 "dissolves in the moving solvent. A dye that holds the "
                 "solvent's side travels a long way. A dye that clings to the "
                 "paper barely moves."},
        # ⚖️ This paragraph is the fence around the whole lesson. It rules out
        # size and it rules out amount BEFORE the bench opens, which is what
        # gives `#s-think` something to hold the student to later.
        {"type": "explainer",
         "text": "Nothing here is about size, and nothing is about how much "
                 "you put on. It is a tug of war, and each substance loses it "
                 "by a different amount."},

        # ── #s-lab · chroma-run ──────────────────────────────────────────
        # A LIGHT `.ks3-block` (page line 110 carries no `ks3-dark` and no
        # `ks3-practical`), which `_INSTRUMENT_SEGMENTS` must map to the
        # `check` shell. Every instrument section in C3 measures the same way.
        # Painting this on ink would resolve every text token wrong and put a
        # cream paper strip on a black surround.
        #
        # The activity id is `chroma-run` because MIX-11's `confronted_by`
        # names it and that name has to resolve to a `data-activity=` on the
        # built page.
        {"type": "chroma-run", "id": "chroma-run", "anchor": "s-lab",
         "demand": "investigate",
         "targets": "MIX-11",
         "eyebrow": "Your turn · the case of the four pens",
         "heading": "Set the paper up, run it, and see whether it can be read",
         "prompt": "Three decisions before you start. Each one can ruin the "
                   "whole run — and each one ruins it in its own particular "
                   "way.",
         "run_label": "Run the chromatogram",

         # ⚖️ THREE DECISIONS, and every one of them starts on the RIGHT
         # answer (page line 414: `pencil: true, below: true, overrun: false`).
         # The student breaks it deliberately rather than stumbling into a
         # ruin, which is what makes each fault an explanation rather than a
         # punishment. `fault` names which entry of FAULTS the option causes;
         # `None` is the sound choice.
         "decisions": [
             {"id": "baseline", "label": "The baseline is drawn in",
              "start": 0,
              "options": [{"label": "Pencil", "fault": None},
                          {"label": "Pen", "fault": "penline"}]},
             {"id": "solvent", "label": "The solvent in the tank starts",
              "start": 0,
              "options": [{"label": "Below the spots", "fault": None},
                          {"label": "Above the spots", "fault": "drowned"}]},
             {"id": "timing", "label": "You take the paper out",
              "start": 0,
              "options": [{"label": "Before the solvent reaches the top",
                           "fault": None},
                          {"label": "When the solvent reaches the top",
                           "fault": "overrun"}]},
         ],
         # Precedence when more than one decision is wrong, from the page's own
         # nested conditional (line 444). A pen baseline hides everything else,
         # so it is reported first.
         "fault_order": ["penline", "drowned", "overrun"],

         # ⚖️ THE ONLY GEOMETRY, AND IT IS ALL PERCENTAGES. A spot's position
         # is `baseline_pct + rf * span_pct`, in percent of the lane's height,
         # measured up from the lane's foot. NOTES §3.4 requires this so a real
         # figure can replace the DOM lane without a payload change.
         "lane_geometry": {"height_px": 230, "baseline_pct": 12,
                           "span_pct": 78},
         "lanes": LANES,

         "good": {
             "title": "A chromatogram you can read.",
             "text": "Five lanes, run side by side on one piece of paper, in "
                     "one solvent, for the same length of time. That is the "
                     "only way the heights can be compared — and now they "
                     "can be.",
             "alt": "A chromatogram with five lanes. The note and Pen A each "
                    "show a yellow spot low down, a magenta spot in the "
                    "middle and a cyan spot high up, at matching heights. Pen "
                    "B shows magenta and cyan only, Pen C shows yellow and "
                    "cyan at slightly different heights, and Pen D shows a "
                    "single blue spot."},
         "faults": FAULTS,

         # ⚖️ The verdict panel exists ONLY on a readable run. A ruined paper
         # cannot convict anybody, and offering the four buttons under it
         # would say it could.
         "verdict": {
             "prompt": "Which pen wrote the note?",
             "note": "A match means every spot at the same height, and no "
                     "spot that the other one does not have.",
             "match": "a",
             "options": [{"id": "a", "label": "Pen A"},
                         {"id": "b", "label": "Pen B"},
                         {"id": "c", "label": "Pen C"},
                         {"id": "d", "label": "Pen D"}],
             "hit_title": "Pen A. Three spots, three matching heights, "
                          "nothing extra.",
             "hit_text": "The note and Pen A separate into the same three "
                         "dyes at the same three heights. Pen B has no yellow "
                         "at all. Pen C has yellow and cyan but both sit "
                         "slightly low, and it has no magenta. Pen D was "
                         "never in the running: one blue dye, and the note "
                         "has three.",
             # One title for every wrong pick, and it points at the evidence
             # rather than at the student.
             "miss_title": "Pen A is the match — look again at the heights.",
             "miss_text": {
                 "b": "Pen B has magenta and cyan, and its magenta sits lower "
                      "than the note. It is also missing the yellow entirely "
                      "— a missing spot rules a sample out as firmly as a "
                      "wrong one.",
                 "c": "Pen C looks close because it shares yellow and cyan, "
                      "but both spots sit lower than the note and there is no "
                      "magenta. Close is not a match.",
                 "d": "Pen D gives one blue spot. The note gives three, in "
                      "three colours, so they cannot be the same ink."},
         }},

        {"type": "key-fact", "ref": "tug-of-war"},

        {"type": "misconception", "id": "think-commit-furthest",
         "anchor": "s-think", "targets": "MIX-12"},

        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Page lines 174–177. Cream card with the accent offset, never amber.
    # `ground: "card"` is measured — Design's box is `var(--ks3-card)`, not the
    # `band` default.
    "key_facts": [
        {"id": "tug-of-war",
         "text": "Chromatography separates dissolved substances by how "
                 "strongly each one sticks to the paper compared with how "
                 "well it dissolves in the moving solvent. The further a "
                 "substance travels, the more it favoured the solvent.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # Hand-authored `predict`s only. `_normalise()` appends the lifted
    # instruments to this list; it never removes from it.
    "activities": [
        {"id": "think-commit-furthest",
         "kind": "predict",
         "demand": "explain",
         "targets": "MIX-12",
         # ⚖️ The QUOTE Design drew, not the register's wording. The two differ
         # ("travelled furthest … the dye there is most of in the ink" against
         # the register's shorter line) and the page's is the one a student
         # reads, so it is authored here and wins — the b1-01 rule.
         "statements": ["The spot that travelled furthest must be the dye "
                        "there is most of in the ink."],
         "prompt": "It went the furthest, so surely there was the most of it "
                   "pushing. Commit before you read on.",
         # ⚖️ B is right. D is the same error inverted — still reading height
         # as a statement about amount — and C smuggles the amount idea back in
         # behind a condition about the paper. A is the belief said plainly.
         "options": [
             "Right — furthest means most",
             "Wrong — distance depends on the dye, not the amount",
             "Right, as long as the paper is dry to start with",
             "Wrong — the furthest spot is the smallest amount",
         ],
         "reveal": [
             "How far a spot travels says nothing about how much of it there "
             "is. It is decided entirely by the tug of war between the paper "
             "and the solvent — and one particle of a dye is pulled exactly "
             "as hard as a million of them. Put a tiny dot of a fast dye on "
             "the paper and it still goes to the top; put a heavy blob of a "
             "slow dye on and it still crawls.",
             "What the amount changes is the "
             "<strong>size and darkness</strong> of the spot, not its "
             "height. So a chromatogram is read "
             "two ways: <strong>height tells you which substance</strong>, "
             "and <strong>darkness hints at how much</strong>. Confusing the "
             "two is how you end up accusing the wrong pen.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Design's RUNGS map to recall + apply, SELF_RUNGS to explain + produce.
    # Their four titles are already the engine's own defaults ("Recall", "The
    # one that catches people", "Explain", "Take it somewhere new"), so no
    # title is overridden here and none is lost.
    "ladder": {
        "recall": {
            "q": "What kind of mixture can chromatography separate?",
            "options": [
                "Substances dissolved in the same solvent",
                "An insoluble solid from a liquid",
                "Two liquids with different boiling points",
                "A dissolved solid from its solvent",
            ],
            "answer": 0,
            # ⚖️ Every wrong option is one of the unit's other three
            # techniques, so the correction can name the lesson it belongs to
            # rather than say "no".
            "feedback": {
                1: "That is filtration. Chromatography needs everything "
                   "dissolved and moving.",
                2: "That is fractional distillation. Chromatography does not "
                   "boil anything.",
                3: "That is evaporation or distillation. Chromatography "
                   "separates dissolved substances from each other.",
            }},
        "apply": {
            "q": "Why must the baseline be drawn in pencil rather than pen?",
            "options": [
                "Pencil is easier to see against the coloured spots once the "
                     "solvent has moved",
                "Pen ink would react chemically with the solvent and change "
                     "the colours it carries",
                "Pen ink is itself a mixture of dyes and would separate and "
                "smear across the paper",
                "Pencil grips the spots and holds them on the baseline while "
                     "the solvent moves past",
            ],
            "answer": 2,
            "feedback": {
                0: "Visibility is not the reason — and pencil is fainter, not "
                   "clearer.",
                1: "No reaction is involved. The ink simply dissolves and "
                   "travels, like every other dye on the paper.",
                3: "The pencil line does nothing to the spots. It stays put "
                   "because graphite is insoluble, and that is all that is "
                   "asked of it.",
            }},
        "explain": {
            "q": "On one chromatogram, a yellow dye travels a third of the "
                 "way up and a blue dye travels most of the way. Explain what "
                 "makes the difference — and explain why the height of a spot "
                 "says nothing about how much of that dye was in the ink.",
            "field_label": "Your explanation",
            "placeholder": "Each dye is pulled two ways…",
            "success": [
                "Says each dye is caught between sticking to the paper and "
                "dissolving in the moving solvent.",
                "Says the blue dye dissolves in the solvent more readily, or "
                "sticks to the paper less, so it travels further.",
                "Says the yellow dye is held by the paper more strongly, so "
                "it moves less.",
                "Says the pull on a dye does not depend on how much of it is "
                "present.",
                "Says the amount affects how big or dark the spot is, not how "
                "high it goes.",
            ]},
        "produce": {
            "q": "A food company is accused of using a banned red colouring "
                 "in its sweets. You have the sweets, pure samples of the "
                 "banned dye and of three legal red dyes, and ordinary lab "
                 "equipment. Describe the investigation, and say exactly what "
                 "result would convict them.",
            "field_label": "Your answer",
            "placeholder": "First I would dissolve the colouring out of…",
            "success": [
                "Dissolves the colouring out of the sweets to make a solution "
                "to spot.",
                "Runs the extract and all four reference dyes side by side on "
                "the same paper.",
                "Says the baseline is pencil and the solvent starts below the "
                "spots.",
                "Says a spot in the extract at the same height as the banned "
                "dye is the incriminating result.",
                # ⚑ flag 13 — `<sub>`, byte-identical to Design's page.
                "Says running them on the same paper — or comparing "
                "R<sub>f</sub> values — is what makes the comparison fair.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Chromatography separates substances dissolved in the same "
                "solvent. The solvent rises through the paper and each "
                "substance is pulled two ways — sticking to the paper, or "
                "dissolving in the moving solvent. Whichever pull wins "
                "decides how far it travels. The baseline is pencil, the "
                "solvent starts below the spots, and everything being "
                "compared is run on the same paper at the same time.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # Design's "Going further" is one `.ks3-layer` with two paragraphs.
    "stretch": [
        # ⚑ flag 13 — `<sub>` again, and the honest limit on the instrument:
        # the bench compares heights, and heights are only comparable within
        # one run. R_f is what makes the comparison portable.
        {"type": "explainer", "id": "rf-values",
         "text": "Height is only comparable within one run — a warmer room, a "
                 "different paper or a different solvent moves every spot. So "
                 "chemists quote a ratio instead: the distance the spot "
                 "travelled divided by the distance the solvent travelled. "
                 "That number, the R<sub>f</sub> value, is between 0 and 1, "
                 "has no units, and can be compared between one lab and "
                 "another. It is the reason a chromatogram can be evidence "
                 "rather than an anecdote."},
        # ⚖️ The lesson's own honesty clause: everything on the bench is
        # coloured, and almost nothing worth separating is. Nothing earlier in
        # the lesson is retracted by it — the separation is identical, and the
        # paragraph says so.
        {"type": "explainer", "id": "colourless-substances",
         "text": "Most substances worth separating are colourless, which "
                 "makes the school version of this look easy and the real "
                 "version look like a blank sheet of paper. Amino acids from "
                 "a protein, sugars from a plant extract and drugs in an "
                 "athlete's urine all separate perfectly well and all arrive "
                 "invisible; the paper is then sprayed with a chemical that "
                 "reacts to show them, or looked at under ultraviolet light. "
                 "The separation is the same. Only the seeing is harder."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # Page lines 310–314. The CTA points at this page's own flagship, which is
    # where the pencil decision is made.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why the baseline has to be pencil?",
              "cta": "Ask about this lesson",
              "anchor": "s-lab"},

    # ⚑ flag 13 — the third and last `<sub>`.
    "ks4_becomes": "R<sub>f</sub> values calculated and compared, and "
                   "chromatography as a required practical for identifying "
                   "substances.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # Three method decisions is `experimental-skills-and-investigations`;
    # reading a chromatogram and ruling four pens in or out is
    # `analysis-and-evaluation`.
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
