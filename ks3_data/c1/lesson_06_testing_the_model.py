"""C1 L6 — Testing the model: does it explain everything? (INVESTIGATION).

Authored against Design's approved page,
`docs/ks3/design-reference/c1/c1-06-testing-the-model.dc.html` (666 lines), and
its measured specification, `docs/ks3/c1-inventory/PAYLOAD-MAP.md` §6.

Every student-facing string is byte-identical to the approved page. The module
constants below were lifted by `node tools/extract_design_payload.js` into
`scratchpad/payloads/c1/c1-06-testing-the-model.json` and pasted, not retyped;
`VERDICTS` was lifted by hand from lines 490–499, because Design authored it
INSIDE `renderVals` rather than at module scope and no constants sweep reaches
it.

── The largest lesson in the unit, and the only one with no canvas ──────

≈2,327 authored words across three DOM instruments and no drawing at all. It is
also the only lesson with THREE anchored sections that are not the hook, the
think block or the ladder, and the only one whose KEY FACT box sits AFTER the
dark practical rather than straight after the flagship. Design's order is kept
exactly; see `core` below.

── The full title is the title ─────────────────────────────────────────

`README.txt` line 11 and c1-05's endmatter link both abbreviate this to
"Testing the model". The page's own `<h1>` (line 75) carries the full question
and matches `ks3_data/structure.py:163` character for character. The full form
is what a student reads.

── `covers` is a Working Scientifically statement, and that is the rule ──

architecture.md §5.7.1: an INVESTIGATION lesson teaches no new subject content
by design — this one tests the model built in L1–L5 — so it anchors `covers` on
the WS statement it actually delivers. `KS3.WS.ATT.02` is *theories develop as
earlier explanations are modified to take account of new evidence*, which is
the lesson in one line. WS statements are exempt from the exactly-once rule
(§5.7), so this collides with nothing.

── Three corrections to Design, all reported ───────────────────────────

1. **The rail's history predicate.** Design's stage 4 is `s.history !== 1`.
   The timeline OPENS on index 1 (Dalton), so that ticks the moment any other
   entry is chosen and **unticks** when a student who has read all five comes
   back to Dalton. The predicate wants "has visited more than the default",
   which is a SET. `done_when` below says so and `wireModelTimeline` counts a
   set that is never emptied. Same class of defect as c1-04 stage 2.

2. **The tally counts the FIRST call, not the current one.** Design recomputes
   "you called N of the seven" from live state, so a student who changes an
   answer after reading the verdict moves a number whose own sentence says
   "before opening the verdict". `wireEvidenceBench` latches the scored call on
   the first press. No authored string changes; the sentence simply becomes
   true.

3. **`ks4_links` gives way to `ks4_becomes`.** The superseded body carried
   `["chemistry/bonding/states-of-matter"]`; Design's third endmatter card is
   authored PROSE (line 330), and §4.8.1 D makes the two mutually exclusive —
   `ks4_becomes` renders only when `ks4_links` is empty. The page wins, and all
   six shipped C2 lessons resolve it the same way. Flagged in the build report:
   the KS4 bridge edge is the thing given up, and it is Mide's to restore.

⚑ For Mide's science gate:
  * The tally scores a commitment the block's own lede says it is not marking
    ("You are not being marked on the sorting"). That tension is Design's and
    it is deliberate — the number exists so the surprise lands, not so anyone
    is graded. Kept exactly.
  * PAYLOAD-MAP §6.6 — NOTES flag 9 says the three failures "all fail because
    the model has identical featureless spheres with no bonds". The three
    cases are attributed to three DIFFERENT repairs: k3 wants particles with a
    shape held at arm's length, k5 wants particles that can bond, k6 wants long
    tangled chains. The static shared-cause paragraph makes the unifying claim
    carefully ("different from each other, or … joined together in some
    particular way"), so it holds — but it is the sentence the whole C1 → C2
    bridge rests on.
  * Bohr's `broke` reads "Nothing yet, for chemistry." The timeline stops short
    of "and now we know" on purpose (NOTES §3 flag 10, NOS-02).

⊕ MRB-248 — RE-HOMED TO `NOS`. This lesson's two beliefs were minted as
`PART-12` and `PART-13` because C1 opened the register, and both are about how
models and evidence work rather than about particles. The 26 Jul 2026 ruling
kept them where they were; the commander has now reversed it and opened the
`NOS` family. `PART-12` → **`NOS-01`**, `PART-13` → **`NOS-02`**. `PART-12` and
`PART-13` are permanent gaps and are never reissued. Every reference in this
module moved with them; NOTES-C1 and PAYLOAD-MAP are frozen delivery records
and still say `PART-12`/`PART-13`, which is what they said when they were
written.
"""

# ── the evidence bench · seven observations ─────────────────────────────
#
# Page lines 356–371, the largest single payload in C1. Four the model handles,
# three it cannot, and the order is Design's: the failures are not grouped, so
# a student cannot answer the set by position.
#
# `ok` is the model's verdict, never the student's — it drives which of the two
# verdict grounds the panel takes and which of the two mono labels it carries.
CASES = [
    {"id": "k1", "tag": "Observation 1",
     "text": "A gas can be squashed into a fraction of its volume; a liquid "
             "cannot be squashed at all.",
     "ok": True,
     "verdict": "Handled completely. A gas is mostly empty space and a liquid "
                "is not. Nothing else needs to be added to the model to get "
                "this right."},
    {"id": "k2", "tag": "Observation 2",
     "text": "A smell crosses a completely still room in about two minutes.",
     "ok": True,
     "verdict": "Handled completely. Random movement plus collisions gives "
                "both the spreading and the length of time it takes."},
    {"id": "k3", "tag": "Observation 3",
     "text": "Ice floats on water. Almost every other solid sinks in its own "
             "liquid.",
     "ok": False,
     "verdict": "Fails. The model predicts that a solid — packed and ordered "
                "— must be denser than the same substance jumbled and looser. "
                "For water it is the other way round. Identical spheres cannot "
                "produce this; you need particles with a shape, that hold each "
                "other at arm’s length in a fixed pattern."},
    {"id": "k4", "tag": "Observation 4",
     "text": "Seal a melting ice cube in a bag and the mass does not change by "
             "a milligram.",
     "ok": True,
     "verdict": "Handled completely. Particles are neither made nor destroyed "
                "by a change of state — they are only rearranged."},
    {"id": "k5", "tag": "Observation 5",
     "text": "Diamond and graphite are both nothing but carbon. Diamond is the "
             "hardest natural substance known; graphite is soft enough to "
             "write with.",
     "ok": False,
     "verdict": "Fails, and badly. In this model the particles are identical, "
                "so the same substance can only have one set of properties. To "
                "explain this you need the particles to be joined together in "
                "different arrangements — which means particles that can bond, "
                "and the model has no bonds in it."},
    {"id": "k6", "tag": "Observation 6",
     "text": "A rubber band stretches to five times its length and snaps back. "
             "A glass rod of the same thickness shatters.",
     "ok": False,
     "verdict": "Fails. Loose spheres sliding past each other cannot stretch "
                "and recoil. Rubber needs particles joined into long tangled "
                "chains that straighten out and spring back — a structure this "
                "model cannot represent at all."},
    {"id": "k7", "tag": "Observation 7",
     "text": "A sealed helium balloon is noticeably smaller after three days, "
             "even though it has no hole.",
     "ok": True,
     "verdict": "Handled completely — and it is a good test, because the "
                "answer is not obvious. The rubber is itself made of particles "
                "with gaps between them, and helium particles are small enough "
                "to work their way through."},
]

# ── the model timeline · five models, 25 authored strings ───────────────
#
# Page lines 373–394. `default_index` is 1 — the timeline OPENS on Dalton,
# because Dalton is the model the student has been using all unit and the point
# of the row is that it already has a before and an after.
HISTORY = [
    {"year": "c. 400 BC", "who": "Democritus", "label": "The uncuttable",
     "claim": "Matter cannot be divided forever — there must be a smallest "
              "piece.",
     "body": "Reached by pure argument, with no experiment behind it and no "
             "way to test it. For two thousand years it sat alongside the "
             "rival view that matter is continuous, and there was nothing to "
             "choose between them.",
     "broke": "Nothing broke it — which was the problem. An idea that cannot "
              "be tested cannot win, and it did not, for twenty centuries."},
    {"year": "1803", "who": "Dalton", "label": "Solid spheres",
     "claim": "Every element is made of identical solid atoms that cannot be "
              "split, created or destroyed.",
     "body": "The first version with numbers attached: fixed proportions by "
             "mass, whole-number ratios, mass conserved through reactions. "
             "This is the model you have been using all unit.",
     "broke": "Thomson found electrons — pieces knocked off an atom that was "
              "supposed to have no pieces. And atoms of one element turned out "
              "to have different masses."},
    {"year": "1897", "who": "Thomson", "label": "Plum pudding",
     "claim": "An atom is a ball of positive charge with tiny negative "
              "electrons dotted through it.",
     "body": "Kept everything Dalton got right about reactions, and added the "
             "one thing he could not have known: atoms have parts, and one of "
             "those parts carries charge.",
     "broke": "Rutherford fired alpha particles at gold foil and a few bounced "
              "straight back — impossible if the positive charge were spread "
              "thinly through the whole atom."},
    {"year": "1911", "who": "Rutherford", "label": "The nucleus",
     "claim": "Almost all the mass sits in a tiny dense nucleus, with "
              "electrons somewhere around it and empty space in between.",
     "body": "An atom turns out to be overwhelmingly empty. If the nucleus "
             "were a marble on the centre spot of a football pitch, the "
             "nearest electron would be somewhere in the stands.",
     "broke": "The maths said the orbiting electrons should spiral into the "
              "nucleus within a fraction of a second. Every atom in existence "
              "should have collapsed already."},
    # ⚠️ The year carries U+2192. `t()` draws it as MARK_ARROW, because the five
    # latin woff2 subsets Design shipped contain no arrow glyph — typed as a
    # character it would drop to a system font inside a 12px mono span.
    {"year": "1913 → now", "who": "Bohr and after", "label": "Shells, then clouds",
     "claim": "Electrons are restricted to particular energy levels, and are "
              "better described as clouds of probability than as balls.",
     "body": "This is the model behind the periodic table, chemical bonding "
             "and every reaction you will meet at GCSE and beyond.",
     # ⚑ NOTES §3 flag 10, verified: the timeline deliberately stops short of
     # "and now we know". NOS-02 (ex-`PART-13`) is the reason.
     "broke": "Nothing yet, for chemistry. It has limits of its own at very "
              "high energies, and the search for what lies past them is a live "
              "field of research right now."},
]

# ── the verdict commit · four options, each carrying its own reply ──────
#
# ⚠️ Page lines 490–499, authored INSIDE `renderVals`. Lifted by hand: a
# "constants live at the top of the script" extraction misses this entirely.
#
# This is the shape `keyed-commit` takes across the unit (PAYLOAD-MAP §6.5.2) —
# the reply hangs off the option rather than being branched in code, and
# c1-03's bubble commit is expressed in it.
VERDICTS = [
    {"text": "Throw the model away — it makes wrong predictions",
     "reply": "That is the strictest possible standard, and no model in "
              "science survives it. Applied consistently it would leave you "
              "with nothing to think with."},
    {"text": "Keep using it where it works, and record exactly where it fails",
     "reply": "This is what was actually done, and it is the answer."},
    {"text": "The exceptions are rare, so they can safely be ignored",
     "reply": "Ice floating is not a curiosity — it is why lakes do not freeze "
              "solid and why life survives winter. And the exceptions are "
              "where the next model came from, so ignoring them costs you the "
              "discovery."},
    {"text": "Change the name to a theory, which is allowed to have exceptions",
     "reply": "A word change fixes nothing. A theory that predicts ice will "
              "sink has exactly the same problem as a model that does."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 163 character for character, full
    # question and all.
    "slug":        "testing-the-model",
    "title":       "Testing the model: does it explain everything?",
    "discipline":  "chemistry",
    "unit":        "particles-and-their-behaviour",
    "family":      "INVESTIGATION",

    # ── curriculum position ─────────────────────────────────────────────────
    # WS-anchored `covers` per §5.7.1 — the standing rule for all 18
    # INVESTIGATION lessons, not a decision taken here. WS is exempt from the
    # exactly-once rule (§5.7), so this does not collide with any other lesson.
    "covers":      ["KS3.WS.ATT.02"],
    "touches":     ["KS3.C.PNM.01a", "KS3.C.PNM.02", "KS3.C.PIS.03"],
    "beyond_statutory": False,
    "threads":     [{"id": "particles", "level": 3}],
    "typical_year": 7,
    "typical_minutes": 45,

    # ── progression edges ───────────────────────────────────────────────────
    # ⊖ The superseded body named four prerequisites. Design's endmatter draws
    # ONE (line 319, Diffusion), which is also §4.9's own advice — a graph where
    # everything requires everything carries no information. The three dropped
    # edges are all reachable through `diffusion`'s own chain.
    "requires":    ["diffusion"],
    "assumes":     [],
    # Two forward links, and both leave the unit. P11 comes first because it is
    # the one the page has already promised: the hook is ice floating, and the
    # lesson that owns it is the natural next step from here.
    #
    # ⊖ §8.10 — `why` RENDERS to the student, in the "Connects to" card, and this
    #   one has been live on the published C1 draft. It read "P11 owns it (§7.4);
    #   this lesson points at it and must render gracefully before P11 exists" —
    #   a build requirement, addressed to nobody the reader is. Rewritten to say
    #   what the connection IS, which is also the more interesting sentence.
    "references":  [{"unit": "P11", "lesson": "why-ice-floats",
                     "why": "Nearly everything shrinks when it freezes. Water "
                            "does the opposite, which is why ice floats instead "
                            "of sinking — and it is the hardest thing this "
                            "model has to explain."},
                    # C2 opens on the model this lesson has just finished
                    # breaking. `why-ice-floats` is not authored yet, so the
                    # first entry renders as un-linked pending text and this one
                    # renders as a live link; the card carries both.
                    {"unit": "C2", "lesson": "the-atom-daltons-model"}],
    # ⊕ Design heads this card `Next unit`, not `Next in this unit` — the one
    # variation across the six pages (§0.5), because this is where C1 ends.
    "connects_heading": "Next unit",
    # ⊖ Empty so `ks4_becomes` can render Design's authored prose. See the
    # module docstring: §4.8.1 D makes the two mutually exclusive.
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "You have spent five lessons being shown how well the "
                    "particle model works. Here are seven things it has to "
                    "account for. Three of them it cannot. What should be done "
                    "about that?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    #
    # ⚠️ `short` runs to 8 characters on stage 2 and 7 on stages 3 and 4.
    # §4.8.1 A advises ≤6; these are Design's own delivered strings (page lines
    # 348–354) and the side rail's label is mono 11px on line-height 1.2 in a
    # 104px column, so it wraps rather than clips. Byte-identity wins over the
    # advisory.
    #
    # ⚖️ Stage 4's predicate is NOT Design's `history !== 1`. See the module
    # docstring: an inequality against the default unticks when a student
    # returns to it, and a rail that goes backwards is worse than one that
    # never moved.
    "rail": [
        {"anchor": "s-hook",    "short": "HOOK",     "label": "Ice floats",
         "done_when": "committed"},
        {"anchor": "s-bench",   "short": "EVIDENCE", "label": "Evidence bench",
         "done_when": "all_seven_judged"},
        {"anchor": "s-verdict", "short": "VERDICT",  "label": "The verdict",
         "done_when": "committed"},
        {"anchor": "s-history", "short": "HISTORY",  "label": "Five models",
         "done_when": "visited_beyond_default"},
        {"anchor": "s-ladder",  "short": "LADDER",   "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # `kind` is authored on every KS3 lesson and read by nothing — build_ks3's
    # own `_hook_media` comment says so and dispatches on which media key is
    # present instead. Design draws no media beside this lede, so there is none.
    "phenomenon": {
        "kind": "narrative",
        "title": "Ice floats.",
        "prompt": "The model says a solid is particles packed tightly in rows, "
                  "and a liquid is the same particles jumbled and slightly "
                  "further apart. Follow that through and every solid should "
                  "be denser than its own liquid, and should sink in it. "
                  "Almost all of them do. Water does not — ice floats, which "
                  "is why lakes freeze from the top and fish survive the "
                  "winter.",
        "commit": "The model has just made a wrong prediction. Commit to what "
                  "that means.",
        "options": [
            "The model is wrong and should be abandoned",
            "Water is a special case and can be ignored",
            "The model has found a limit, and the limit is worth knowing",
            "Someone measured it wrong",
        ],
        # ⚖️ The hook deliberately refuses to settle. MRB-225 in reverse: the
        # answer is the lesson, so the reveal says so rather than pre-empting it.
        "reveal": "Hold your answer. By the end of this lesson you will have "
                  "seen the model succeed four times and fail three, and the "
                  "right thing to do about that is the actual content of the "
                  "lesson — not a tidy verdict either way.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⊕ MRB-248 — these two were `PART-12` and `PART-13` and are now `NOS-01`
    # and `NOS-02`. The 26 Jul 2026 ruling that froze them under `PART` has
    # been reversed by the commander and the `NOS` family is open; the old
    # numbers are permanent gaps and are never reissued. The statements below
    # are unchanged, byte for byte — a re-home moves the label, never the
    # science.
    #
    # The statements are the register's wording; where Design's page quotes the
    # wrong idea in different words, the ACTIVITY carries `statements` and wins
    # over the register — which is the b1-01 lesson, learned once.
    "misconceptions": [
        {"id": "NOS-01",
         "statement": "A scientific model is either true or false, and one "
                      "exception proves it wrong.",
         "elicited_by": "the-verdict",
         "confronted_by": "the-verdict"},
        {"id": "NOS-02",
         "statement": "Scientists' models never change once they are agreed.",
         # ⚑ NOTES §1 names the five-model timeline as this belief's
         # confrontation, and it is the evidence — but the block that asks the
         # student to commit and then answers them is `#s-think`, which is why
         # both fields name it. `five-models` runs immediately before it and is
         # what the reveal points back at ("the timeline above").
         "elicited_by": "settled-science",
         "confronted_by": "settled-science"},
    ],

    # ⊖ TWO OF THE SUPERSEDED BODY'S THREE TERMS ARE GONE, because the lesson
    # they belonged to is gone. `anomaly` and `peer review` were the vocabulary
    # of an INVESTIGATION that ran a simulation, collected messy data and
    # analysed it. The rebuilt page runs no experiment: it judges seven finished
    # observations, commits to a verdict and walks a timeline. Neither word
    # appears anywhere on it, and a term the lesson never uses is a chip on the
    # unit page promising a word the student will not meet.
    #
    # Design draws no keyword block anywhere in C1 (PAYLOAD-MAP §0.7), so the
    # definitions do not reach the lesson body; the terms do, as the unit page's
    # "Words this unit gives you" chips, and the reading-age gate reads them as
    # its exclusion list.
    "vocabulary": [
        {"term": "evidence",
         "definition": "Observations or measurements used to decide whether an "
                       "idea works.",
         "note": None},
        # ⊕ ADDED. The hook turns on it — "the model has just made a wrong
        # prediction" — the apply rung asks what to do about that one, and the
        # verdict's closing paragraph is the note below in Design's own words.
        {"term": "prediction",
         "definition": "What a model says should happen, worked out before "
                       "anyone checks.",
         "note": "A wrong prediction is not a disgrace. It is the most useful "
                 "thing a model can produce, because it tells you where to "
                 "look next."},
        # ⊕ ADDED. This is the lesson's own idea and its key fact: a model is
        # judged by what it explains AND where it fails. The word carries the
        # explainer ("you know where its edges are"), the hook's correct option
        # and the closing verdict.
        {"term": "limit",
         "definition": "The point where a model stops giving the right answer.",
         "note": "Every model has limits. Knowing where they are is part of "
                 "understanding it, not a reason to throw it away."},
    ],

    # Nothing on the rebuilt page references a figure — it is the only lesson in
    # the unit with no drawing at all, and all three instruments are DOM. The
    # superseded body's `c1-model-scorecard` is now the evidence bench itself,
    # and its `c1-ice-water-density` graph has no block to sit in: the ice
    # anomaly arrives here as the hook's prose and observation 3, with no
    # measured curve anywhere on the page. Declaring either would put a sourcing
    # task in the diagram manifest for a drawing nothing would show. Present and
    # empty, never absent.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    #
    # ⚠️ TWO STRUCTURAL FIRSTS, both Design's and both kept. The KEY FACT box
    # sits at position 5, AFTER the dark practical rather than straight after
    # the flagship instrument; and this is the only lesson in the unit with
    # THREE anchored sections that are not the hook, the think block or the
    # ladder. Reordering either would be tidying away the argument: the key
    # fact is the sentence the verdict block has just earned.
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Every lesson so far has handed you evidence that fits. That "
                 "is not how the model was tested and it is not how you should "
                 "judge it. A model is only worth anything if you know where "
                 "its edges are — so this lesson goes looking for them "
                 "deliberately."},

        # ── #s-bench · the evidence bench ──────────────────────────────────
        # Light `.ks3-block` (page line 110) → the `check` shell.
        #
        # ⚠️ NO GATE, and it is the only flagship instrument in C1 without one
        # (PAYLOAD-MAP §6.5.1). Not an omission: the seven judgements ARE the
        # commitment, so a four-option gate in front of them would ask the
        # student to commit to committing.
        #
        # ⚖️ THE TALLY SCORES A COMMITMENT THE BLOCK SAYS IT IS NOT MARKING.
        # The lede is explicit — "You are not being marked on the sorting" —
        # and the closing line still counts how many were called before the
        # verdicts opened. That is Design's, it is deliberate, and it is what
        # makes the surprise land: the number is evidence about the model's
        # reputation, not a grade. Kept exactly as drawn.
        {"type": "evidence-bench", "id": "seven-observations",
         "anchor": "s-bench",
         "demand": "evaluate",
         "eyebrow": "The evidence bench · judge each one",
         "heading": "Seven observations. Does the model handle it?",
         # `benchProgress` (page line 544) has two shapes: the running count,
         # and a bespoke label once every case is judged. `head_counter` covers
         # the count; `progress_all` is the second, read by
         # `wireEvidenceBench` when the set closes.
         "head_counter": {"format": "{n} of {total} judged", "total": 7},
         "progress_all": "all seven judged",
         "prompt": "Decide before you open the verdict. You are not being "
                   "marked on the sorting — you are being asked to commit, so "
                   "that a surprise can land.",
         "buttons": {"yes": "Explains it", "no": "Cannot"},
         "verdict_labels": {"ok": "The model handles this",
                            "fail": "The model cannot do this"},
         "cases": CASES,
         "tally": "Four explained, three not — and you called {n} of the seven "
                  "before opening the verdict.",
         # ⚠️ THE SHARED-CAUSE CLAIM IS MARKUP, NOT THE TALLY. NOTES §3 flag 9
         # says "the tally text says so"; it does not — the tally (page 567) is
         # the count line and the claim is the STATIC paragraph at page 146.
         # That is why this is one authored string with an <em> in it rather
         # than something assembled around a number.
         "shared_cause": "The three failures have one thing in common, and it "
                         "is worth naming: every one of them needs the "
                         "particles to be <em>different from each other</em>, "
                         "or to be joined together in some particular way. The "
                         "model you have is a model of identical featureless "
                         "spheres. That is exactly the assumption that is "
                         "about to be replaced."},

        # ── #s-verdict · the verdict commit ────────────────────────────────
        # Ink-dark `practical` (page line 151). This is the real question of
        # the lesson, which is why Design paints it on ink.
        #
        # `keyed-commit` is shared with c1-03 and takes THIS shape — the reply
        # attached per option (PAYLOAD-MAP §6.5.2).
        {"type": "keyed-commit", "id": "the-verdict", "anchor": "s-verdict",
         "demand": "evaluate",
         "targets": "NOS-01",
         "eyebrow": "The verdict · this is the real question",
         "heading": "Three failures. What should be done?",
         "prompt": "Commit to one. Then read what scientists actually did, "
                   "which is on the record and is not a matter of opinion.",
         "options": VERDICTS,
         # ⚠️ Read at BUILD TIME only — `r_keyed_commit` checks it is in range
         # and that the option it names carries a reply. Nothing marks it and
         # nothing may: R3 says an activity option shows only that it was
         # chosen. Its job is to name, for the examiner, the option the lesson
         # is arguing for.
         "answer_index": 1,
         # The two paragraphs Design draws as STATIC markup under the chosen
         # reply (page lines 170–171).
         "closing": [
             "Nobody threw it away. The particle model is still used every "
             "day, by everyone, including the people who know exactly where it "
             "breaks — because for melting, pressure, diffusion and dissolving "
             "it gives the right answer with almost no effort. What happened "
             "instead is that the failures were treated as a map: each one "
             "marked a place where a better model was needed, and each one "
             "eventually got built. Ice floating was explained once particles "
             "could be shaped and could pull on each other in particular "
             "directions. Diamond and graphite were explained once particles "
             "could be joined in patterns. Rubber was explained once particles "
             "could be long chains.",
             "A wrong prediction is not a disgrace. It is the most useful "
             "thing a model can produce, because it tells you where to look "
             "next.",
         ]},

        {"type": "key-fact", "ref": "judged-by-what-it-explains"},

        # ── #s-history · the model timeline ────────────────────────────────
        # Light `.ks3-block` (page line 181) → the `check` shell.
        {"type": "model-timeline", "id": "five-models", "anchor": "s-history",
         "demand": "explain",
         "eyebrow": "Not a straight line",
         "heading": "The model has already been replaced four times",
         "prompt": "Each one of these was, in its day, what \"everyone knew\". "
                   "Each was overturned by evidence, and each left something "
                   "behind that is still in use.",
         "steps": HISTORY,
         # Dalton, not Democritus — page line 447. The row opens on the model
         # the student has been using all unit, because the point of it is
         # that Dalton already has a before and an after.
         "default_index": 1,
         "broke_label": "What broke it:"},

        {"type": "misconception", "id": "settled-science", "anchor": "s-think",
         "targets": "NOS-02"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # `ground: "card"` per R3 — the shipped stylesheet wins over the page's own
    # 6px/25px geometry drift, and one stylesheet serves 183 lesson slots.
    "key_facts": [
        {"id": "judged-by-what-it-explains",
         "text": "A scientific model is judged by what it explains and where "
                 "it fails — not by being completely true. Knowing a model's "
                 "limits is part of understanding it.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # The three instruments are authored inline in `core` above and lifted here
    # by `ks3_data/c1/__init__.py`. This list holds the one activity that is
    # not an instrument.
    "activities": [
        # ══ #s-think · the confrontation ═══════════════════════════════════
        #
        # R1: every C1 `#s-think` asks for a commitment, so it is a `predict`
        # and it DOES tick its rail stage. It is not B1's static confrontation.
        #
        # `statements` carries Design's own wording of the wrong idea (page
        # line 208), which differs from the register's NOS-02 statement. An
        # authored statement wins over the register — the b1-01 defect, where
        # the register's line rendered and Design's did not.
        {"id": "settled-science",
         "kind": "predict",
         "demand": "explain",
         "targets": "NOS-02",
         "statements": [
             "Once scientists agree on something, it is settled — that is what "
             "makes it science.",
         ],
         "prompt": "Commit before you read on.",
         "options": [
             "True — agreement is what makes something scientific",
             "Being open to revision by evidence is what makes it scientific",
             "Nothing in science can be trusted, then",
             "Only old science gets overturned; modern science is settled",
         ],
         "reveal": [
             "The opposite is nearer the truth. What makes an idea scientific "
             "is that it is the kind of thing evidence could overturn — and "
             "the timeline above is five overturnings in a row, each by people "
             "who were not being careless. Dalton was not sloppy; he was "
             "working with the evidence he had.",
             "This does not mean nothing is reliable. The particle model has "
             "survived two centuries of people trying to break it, and the "
             "parts that survived are about as solid as human knowledge gets. "
             "\"Open to revision\" and \"as good as we have got\" are not "
             "opposites — they are the same sentence, said twice.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # Rung titles are omitted: Design's four (`Recall`, `The one that catches
    # people`, `Explain`, `Take it somewhere new`) are byte-identical to
    # `LADDER_RUNGS`' defaults after MRB-228's relabel, so authoring them would
    # be a second copy free to drift.
    "ladder": {
        "recall": {
            "q": "Name one thing the simple particle model cannot explain.",
            "options": [
                "Why a gas can be squashed",
                "Why a smell spreads across a room",
                "Why ice floats on water",
                "Why mass stays the same when ice melts",
            ],
            "answer": 2,
            "feedback": {
                0: "It explains this well — a gas is mostly empty space.",
                1: "It explains this well — random movement and collisions.",
                3: "It explains this well — particles are rearranged, not "
                   "destroyed.",
            }},
        "apply": {
            "q": "The particle model makes a wrong prediction about ice. What "
                 "is the right response?",
            "options": [
                "Throw it out — a model that gets something wrong is worthless",
                "Keep using it where it works, and note the limit",
                "Ignore the exception, since it is only water",
                "Call it a theory instead of a model, which allows exceptions",
            ],
            "answer": 1,
            "feedback": {
                0: "Then chemistry would have no models at all. Every one of "
                   "them has limits, including the current ones.",
                2: "Ignoring the failure is how you miss the discovery. The "
                   "exceptions are where the next model comes from.",
                3: "Renaming it changes nothing. A theory that makes a wrong "
                   "prediction has exactly the same problem.",
            }},
        "explain": {
            "q": "The particle model cannot explain why diamond and graphite — "
                 "both pure carbon — have completely different properties. "
                 "Explain why not, and say what would have to be added to the "
                 "model to fix it.",
            "field_label": "Your explanation",
            "placeholder": "In this model, all the particles of one substance "
                           "are…",
            "success": [
                "Says the model treats all particles of a substance as "
                "identical featureless spheres.",
                "Says identical particles should give identical properties, so "
                "one substance could only ever behave one way.",
                "States the observation clearly: same element, two very "
                "different materials.",
                "Says the model would need particles that can be joined "
                "together in different arrangements.",
                "Says this is a limit of the model, not a mistake in the "
                "observation.",
            ]},
        "produce": {
            "q": "A student reads the timeline and concludes: \"Scientists "
                 "keep being wrong, so there is no point trusting what they "
                 "say now.\" Reply to them, using at least one specific "
                 "example from this lesson.",
            "field_label": "Your reply",
            "placeholder": "Each new model had to explain…",
            "success": [
                "Says each new model had to reproduce everything the old one "
                "already explained.",
                "Gives a specific example — Dalton’s explanation of "
                "conservation of mass is still used, or Newton is still used "
                "to land spacecraft.",
                "Says being open to revision by evidence is what makes an idea "
                "scientific, not a weakness in it.",
                "Distinguishes between an idea being replaced and an idea "
                "being useless.",
                "Says the current model is the best-tested account available, "
                "not a guess.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "The particle model explains melting, pressure, diffusion and "
                "dissolving, and fails on ice floating, diamond versus "
                "graphite, and stretchy materials. All three failures come "
                "from the same assumption — that particles are identical "
                "featureless spheres. That is the assumption the next unit "
                "removes.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    #
    # ⚖️ MRB-225: history of science and the over-correction it invites live
    # HERE, not in the body. The lesson body says models get replaced; the
    # sentence that stops "so you cannot trust any of it" is in Going further,
    # where it cannot be read as the body retracting itself.
    "stretch": [
        {"type": "explainer", "id": "over-correction",
         "text": "There is a version of this that goes too far. \"Scientists "
                 "are always changing their minds, so you cannot trust any of "
                 "it\" is a conclusion people reach from exactly the evidence "
                 "on this page, and it does not follow. Look at what actually "
                 "survived each revision: Dalton was wrong that atoms cannot "
                 "be split, and every single thing he used that claim to "
                 "explain is still explained the same way today. Newton was "
                 "superseded by Einstein, and NASA still uses Newton to land "
                 "spacecraft. Replacement in science is almost never "
                 "demolition — it is a new model that has to reproduce "
                 "everything the old one got right, plus the thing that broke "
                 "it. That constraint is why the changes accumulate instead of "
                 "cancelling out."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The CTA points back at `#s-verdict`, which is where the question the card
    # names is actually answered.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Unsure how a model can be wrong and still be right to "
                      "use?",
              "cta": "Ask about this lesson",
              "anchor": "s-verdict"},

    "ks4_becomes": "Bonding and structure — where every failure on this page "
                   "gets its proper explanation.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["scientific-attitudes", "analysis-and-evaluation",
           "experimental-skills-and-investigations"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
