"""B5 L5 — Lifestyle and the developing foetus (SYSTEM).

Authored against Design's approved page,
`docs/ks3/design-reference/b5/b5-05-lifestyle-and-the-developing-foetus.dc.html` (597 lines),
under the MRB-220 build contract, with `NOTES-B5.md` §2.3, §3 flags 26–30 and
§4 read whole rather than by flag, as Design's own README asks.

Every student-facing string is lifted byte-identical from the approved page,
via `node tools/extract_design_payload.js` for the six substances, the three
windows and all four rungs, and by extraction from the page body for the
static prose. Nothing on this page was retyped. The exceptions are listed
under "What could not be lifted", and none of them is a word of copy.

⚠️ Design's static markup uses STRAIGHT apostrophes (`the mother's blood`) and
her JS constants use CURLY ones (`the mother’s glucose`). Both are reproduced
exactly as delivered rather than normalised. A normalising pass here would be
an edit to safeguarding copy for the sake of tidiness.

── ⚠️ TONE IS THE GATE, AND THE ARCHITECTURE IS WHAT MAKES IT WORK ───────

Read `ks3_data/b5/__init__.py` first; its tone section is about this lesson.
The short version, because it decides how everything below is authored:

**The placenta is taught as a NEUTRAL EXCHANGE SURFACE governed by size and
solubility.** What crosses is decided by the molecule, not by whether the
foetus would be better off without it. That is not a framing choice made for
comfort — it is what makes the lesson's second confrontation answerable at
all. If the surface sorted, then something got through that should not have,
and somebody let it. Because the surface does not sort, there is nothing to
have failed at.

What that means for this record, and none of it is negotiable:

- **Third person throughout.** "The placenta", "the foetus", "a person who is
  pregnant". The page contains no second person anywhere near an exposure
  (NOTES flag 30) and nothing here adds one.
- **No doses, no thresholds, no advice** beyond the two figures Design's own
  page states (caffeine's 200 mg, and the weeks-three-to-eight window), and
  those are hers, in her sentences.
- **Nobody is told to stop a prescribed medicine.** The `meds` substance says
  the opposite in terms — *stopping is often the greater risk* — and that
  sentence is load-bearing, not decorative.
- **The legal line is carried whole**, small, at the bottom edge, never a
  callout (§8.10). See `convention_note` at the foot of this record.

── ⚑ THE ANTI-BLAME PARAGRAPH — NOTES-B5 FLAG 28 ────────────────────────

*"So anything that goes wrong is the mother's fault."* and its answer are the
single most important strings on this page, and Design says so herself: *"it
is, in my judgement, the paragraph that makes the lesson safe to teach"*.

It is LIFTED WHOLE into `activities[] → two-wrong-ideas → statements[1]`. Not
shortened, not reordered, not softened, not improved. Every element of it
survives in Design's order: second-hand smoke, roadside air pollution,
infection caught from someone else, a medicine that must be continued,
food choices constrained by circumstances, addiction as a condition of the
nervous system rather than a repeated decision, unexplained complications, the
shape of the evidence, and the close on risk being a statement about
populations and not a verdict on a person.

**ONE thing in it could not be carried, and it is markup rather than words.**
The paragraph contains an inline link —
`<a href="b6-01-what-drugs-do-to-the-body.html">What drugs do to the body</a>`
— and `rich()` (build_ks3.py:245) allows `<em>` and `<strong>` and nothing
else, by an explicit ruling: *"not `<a>` … a third needs a ruling rather than
a regex"*. So the anchor is dropped and **the link text stays in the sentence
unchanged**: *"which is the point What drugs do to the body spends a whole
lesson establishing"*. Not one word of the paragraph is lost, and the sentence
still names the lesson it defers to.

The DESTINATION is not lost either: `what-drugs-do-to-the-body` is added to
`references[]`, last, so the edge Design drew still exists on the page. That
is b4-01's precedent applied to a link rather than a card — *"The heading is
what is given up; no link is"*. It is the one thing in the tone treatment that
was judged rather than lifted, and it is in the report for Mide to reverse if
he would rather the edge simply went.

── The instrument, and why it is the same shape as b5-04's ──────────────

`#s-cross` is `crosses-panel`, on `ks3-block ks3-dark ks3-practical` (page
line 105), so `practical` is MEASURED from Design's own markup and not
inherited. Six substances, a yes/no commit, then a verdict, a *why*, and a
0–40 week bar saying when that exposure matters most.

NOTES §1 and §6 both say the shape deliberately repeats b5-04's
`crossing-bench`, *"because the lesson's whole argument is that the crossing
rule from the previous lesson does not change when the substance is a harmful
one"*, and asks that the two not be refactored apart. The repetition is the
argument.

⚠️ **FIVE of the six cross and one does not, and that imbalance is the
teaching point** (NOTES §2.3). Do not "balance" the set. Insulin is the only
`crosses: False` row and it is the proof that the rule is about size: nothing
decided that insulin should be kept out.

⚠️ **The panel must never read as a filter that failed.** Every `answer` and
every `why` names the molecule — small and soluble, or a protein that is too
large, or a virus that does not diffuse at all but infects the placenta's own
cells. The week bar is *when a system is being built*, never a verdict on
anyone: `winText` on every row talks about what is forming, and insulin's says
plainly that the bar does not apply because it does not arrive.

── FOUR rail stops — Design's fourth restored (MRB-249) ─────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that a rail
stop came off. Design draws FOUR stops, and `#s-windows` ticks on
`Object.keys(s.opened).length >= 6` (page line 429) — the PANEL's predicate,
verbatim, one section to the left — and because `#s-windows` is an eyebrow, a
statement, a lede, three static rows and a key fact with no control, no
commitment and no field, the reading was that
`ks3_parity.check_rail_reachable` would fail a stop carrying none of the
signals `doneByDom()` reads, and that inventing a demand Design did not draw is
closed to this build. So the lesson shipped THREE stops.

Two things overrule that inference.

MRB-205 was cited for one half of itself. Design draws, we render, and page
wins over engine: inventing a control is forbidden, and so is dropping a stop
Design drew.

And Design's `isDone()` states the tick condition. It is a rail-level function
returning the identical expression for `#s-cross` and then for `#s-windows`.
The three windows are the payoff of the six crossings the student just settled;
the section holds no control because the panel already took the commitment.
That is a MIRROR, resolved at rail level in `wireRail`'s `paint()`.

So the fourth stop is declared: anchor `s-windows`, `mirrors: "s-cross"`,
`done_when: "all_six_checked"` — the panel's own predicate, named as borrowed,
and gated by `check_rail_matches_design` against `docs/ks3/rail-manifest.md`.
b4-01's `#s-parts`, c1-02's `#s-matrix`, c1-05's `#s-scale`, b3-01's
`#s-nutrients` and b3-02's `#s-limits` are restored the same way.

The section KEEPS its `#s-windows` anchor, as it always did, and Design's rail
label for it (`TIMING` / *Three windows*) is no longer given up — it ships.

── Misconceptions: this lesson owns REPRO-09 and REPRO-10 ───────────────

  REPRO-09  "The placenta filters out anything harmful."
  REPRO-10  "So anything that goes wrong is the mother's fault."

⚑ **A THIRD belief is confronted on this page and is NOT minted here.** The
page separates *crosses the placenta* from *harmful at any amount* — twice in
so many words (caffeine's `why`, and rung 4's first criterion), and the whole
of rung 4 depends on the distinction. That is a real and common wrong idea —
*if it reaches the foetus it must do harm* — and it is confronted by the
instrument and the ladder rather than by the "Think again" block. It belongs
to the register as **REPRO-21**, and the commander mints it: this pass owns 09
and 10 and nothing else, so it is reported rather than authored. Nothing in
this record cites REPRO-21.

Note also that REPRO-10 is not a science misconception at all — it is an
attribution error (NOTES flag 28, and NOTES §5 records the register carrying
one such entry knowingly). It is in `misconceptions[]` because it is what a
class otherwise takes away from this lesson.

── What could not be lifted, and why ────────────────────────────────────

1. **The inline `<a>` in the anti-blame paragraph.** Words kept, anchor
   dropped, destination rescued into `references[]`. See above.

2. **The PROMOTED row in the timing table.** Design paints `Weeks 3–8 · the
   embryo` on `--ks3-inset` (`promoted: true`, page line 375) to say that this
   is the window the lesson is about. `r_comparison` has no per-row emphasis —
   its `data-zebra` alternates on row parity and its `row_tones` are per
   COLUMN — so the promotion is not carried. It lands on zebra 1 by position,
   which looks similar and is not the same thing, and it is reported as drift
   rather than smuggled in by reordering the rows. **The words are unchanged
   and the order is unchanged**, and the key fact directly under the table
   says the same thing in prose ("What the substance then does depends on what
   is being built that week"), so nothing is lost but emphasis.

3. **Design draws TWO endmatter link cards; the engine emits one.** Her "Next
   in this unit" (`flowers-and-pollination`) and "Connects to" (`gestation-
   placenta-and-birth`, `alcohol-and-smoking`, `substance-misuse-and-
   decisions`) are one card in `r_endmatter`, headed by `connects_heading`.
   All four links live in it, the forward one first — b3-01, b4-01 and b4-05
   resolve the identical layout identically. The heading is what is given up.

4. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card
   is authored prose and §4.8.1 D makes the two mutually exclusive.

5. **The mono `<span>` around the figure id in the legal line.** A foot line
   is escaped, so `b5-what-crosses` renders in body copy. The words are
   unchanged; b4-01 resolved the same span the same way.

6. **`phenomenon.kind` is not authored.** build_ks3.py:539 records it as read
   by nothing and dispatching on which key is present instead; R5 says a key
   with no read site is not authored. The hook is a narrative one either way.

⊕ **THE RUNG 1 LENGTH TELL IS REPAIRED — MRB-177 RULED 17 Aug 2026.**
Measured before: the correct option was 15 words against distractors of
9 / 9 / 8, the longest by some margin, so a student who read nothing could pick
it on that alone.

Mide ruled the CONSTRUCT rather than this instance: on a recall or apply rung
the correct answer states a RULE — subject, condition, consequence — while the
distractors stated one-clause wrong REASONS, so the correct answer was longer by
construction. A distractor must state a WRONG RULE instead, in the same shape,
with the misconception as the consequence; length parity then follows from the
construct rather than from trimming the correct answer.

Rung 1's three distractors are Mide's own replacement copy, applied verbatim.
**The correct option is unchanged, `answer: 1` is unchanged, and the gate's
threshold is unchanged.** Measured after: 15 against 15 / 17 / 15 — no longer
strictly the longest. All three corrections in `feedback` already answered the
new wording and are byte-identical. Rung 2 is untouched and still clean — the
correct option is one word against 5 / 1 / 1.

⛔ Superseded, kept as history: this note used to read *"here there IS something
to repair and it is still not repaired, because every option is Design's science
copy and MRB-205 says the page wins. Reported for Mide."* It was reported, and
he has ruled — the replacement copy is his, so MRB-205's "the page wins" is not
overridden by an author. The
`("lifestyle-and-the-developing-foetus", "ladder recall")` entry in
`verify_ks3.py`'s `KNOWN_TELLS` is now stale; the commander deletes it.

⚠️ Typographic note, reported rather than corrected: Mide's replacement copy
uses STRAIGHT apostrophes ("the mother's blood") where this page's JS-constant
convention is CURLY, so rung 1 now carries both forms. His instruction was to
apply the copy exactly as given, so it is applied exactly.

⚑ For Mide's science gate — NOTES-B5 flags landing on THIS lesson:
  * flag 26 — **the six crossing claims as one block**: alcohol, carbon
    monoxide, caffeine, rubella, prescribed medicines, insulin. Design asks
    for these to be reviewed together rather than one at a time. Authored
    exactly as delivered; the flag is carried, not answered.
  * flag 27 — *"under about 200 mg a day, roughly two mugs of instant
    coffee"*. The figure and the mug equivalence, in caffeine's `why`.
  * flag 28 — the anti-blame paragraph, wording included. See above.
  * flag 29 — thalidomide in the stretch layer: sold from 1957, McBride and
    Lenz, withdrawn 1961, the few-week window that mapped limb development,
    and its controlled use today.
  * flag 30 — nothing addresses the reader as pregnant or as a future parent,
    and there is no second person anywhere near an exposure. Confirmed intact
    in this record.
  * flag 13 — `b5-what-crosses` is named in Design's legal line and is in no
    manifest. Declared here at `status: "needed"` (§4.10, not a build blocker)
    so it is a tracked sourcing task rather than a dangling reference. It is
    the ONLY diagram slot this page names. Nothing is invented to fill it.
"""

# ── the six substances (page lines 338–369, via extract_design_payload.js) ─
#
# ⚠️ Order is Design's and is load-bearing: the lede promises that "by the
# third one you should be able to predict the rest", which is only true if the
# three easy diffusion cases come first, the virus breaks the mechanism, the
# medicines row breaks the yes/no framing, and insulin — the single `crosses:
# False` row — lands last as the proof that the rule is about size.
#
# ⚠️ `win` is a pair of PERCENTAGES of a 0–40 week bar, not weeks. Insulin's
# [0, 0] is a deliberately empty bar with `win_text` saying why: it does not
# arrive. A row drawn with no bar and no sentence would read as a gap.
SUBS = [
    {"id": "alcohol",
     "label": "Alcohol",
     "name": "Alcohol",
     "kind": "Small molecule · dissolves readily",
     "crosses": True,
     "context": "A small molecule that dissolves in both water and fat — "
                "which is what lets it into every tissue in an adult too.",
     "answer": "Yes — freely, and within minutes.",
     "why": "The foetus ends up with roughly the same concentration in its "
            "blood as the mother has in hers, but a much less developed liver "
            "to break it down, so it stays there longer. Its clearest effects "
            "are on the developing brain and nervous system, and on growth. "
            "UK advice is that no amount is known to be safe, which is a "
            "statement about missing knowledge as much as about the alcohol.",
     "win": [0, 100],
     "win_text": "The whole pregnancy. The brain and nervous system are being "
                 "built and rebuilt from the first weeks to the last, so "
                 "there is no window in which alcohol has nothing to reach."},

    {"id": "co",
     "label": "Carbon monoxide",
     "name": "Carbon monoxide, from smoke",
     "kind": "Small molecule · diffusion",
     "crosses": True,
     # ⚑ The exposure is named as one that is not chosen — "breathed in by
     # anyone in the room, not only the smoker" — in the CONTEXT line, before
     # the anti-blame paragraph reaches the same point. That is the tone
     # treatment doing its work inside the instrument, and it is Design's
     # sentence, not an addition.
     "context": "Produced whenever tobacco burns — and breathed in by anyone "
                "in the room, not only the smoker.",
     "answer": "Yes — and it works by taking up space.",
     "why": "Carbon monoxide binds to haemoglobin far more tightly than "
            "oxygen does, so every molecule of it in the blood is a seat "
            "oxygen cannot use. Less oxygen reaches the placenta, less "
            "crosses it, and a foetus short of oxygen grows more slowly — "
            "which is why smoking during pregnancy lowers birth weight "
            "measurably. Nicotine crosses too, and narrows blood vessels, "
            "which reduces the supply again.",
     "win": [10, 100],
     "win_text": "Mostly the growth half of the pregnancy, because this is a "
                 "supply problem rather than a building problem — though the "
                 "supply matters throughout."},

    {"id": "caffeine",
     "label": "Caffeine",
     "name": "Caffeine",
     "kind": "Small molecule · diffusion",
     "crosses": True,
     "context": "In coffee, tea, cola and energy drinks. A stimulant, and the "
                "most widely used drug in the world.",
     "answer": "Yes — and this one is about dose.",
     # ⚑ NOTES flag 27 (the 200 mg figure and the mug equivalence) and the
     # third belief that becomes REPRO-21 (crossing and harming are two
     # different claims) both live in this one string. Lifted whole.
     "why": "Caffeine crosses easily and the foetus breaks it down slowly. "
            "Unlike alcohol, the advice here is a limit rather than a ban: UK "
            "guidance is to stay under about 200 mg a day, roughly two mugs "
            "of instant coffee. It is a useful case, because it shows that "
            "<em>crosses the placenta</em> and <em>harmful at any amount</em> "
            "are two different statements, and the second one has to be "
            "established separately for every substance.",
     "win": [0, 100],
     "win_text": "No sharply defined window. What the evidence associates "
                 "with high intake is reduced growth, which can happen at any "
                 "stage."},

    {"id": "rubella",
     "label": "Rubella virus",
     "name": "Rubella virus",
     "kind": "Virus · not by diffusion",
     "crosses": True,
     "context": "A mild illness in a child — a few days of rash and fever — "
                "and a serious one for an embryo.",
     "answer": "Yes — but by a completely different route.",
     "why": "A virus is far too large to diffuse anywhere. It crosses by "
            "infecting the placenta’s own cells and being made again on the "
            "other side, cell by cell. Catching rubella early in pregnancy "
            "can damage the developing eyes, ears and heart, which is why the "
            "MMR vaccination given in childhood is as much a protection for "
            "future pregnancies as for the child receiving it.",
     "win": [0, 30],
     "win_text": "Overwhelmingly the first twelve weeks, when the eyes, ears "
                 "and heart are being formed. After about twenty weeks the "
                 "risk is very low."},

    {"id": "meds",
     "label": "Prescribed medicines",
     "name": "Prescribed medicines",
     "kind": "Varies · depends on the molecule",
     "crosses": True,
     "context": "Someone may need treatment for epilepsy, diabetes, asthma, "
                "an infection or a mental health condition while pregnant.",
     "answer": "Many do — and stopping is often the greater risk.",
     # ⚠️ SAFEGUARDING COPY. The last clause — "why nobody should stop a
     # prescribed medicine on their own" — is the reason this row exists in
     # the set at all. It is never abbreviated and never softened.
     "why": "Each medicine has to be judged separately, and the judgement is "
            "not simply <em>does it cross</em>. An untreated seizure, an "
            "untreated infection or uncontrolled asthma can be far more "
            "dangerous to a pregnancy than the drug that prevents it. This is "
            "precisely why the decision belongs to a doctor or pharmacist who "
            "knows the case, and why nobody should stop a prescribed medicine "
            "on their own.",
     "win": [5, 25],
     "win_text": "Weeks three to eight are the most sensitive for structural "
                 "effects, which is why the first appointment asks what "
                 "someone is already taking."},

    {"id": "insulin",
     "label": "Insulin",
     "name": "Insulin",
     "kind": "Large protein · too big",
     # ⚠️ THE ONLY `False` IN THE SET, AND IT STAYS THE ONLY ONE.
     "crosses": False,
     "context": "The hormone that controls blood glucose, and the treatment "
                "for diabetes.",
     "answer": "No — not in any useful amount.",
     "why": "Insulin is a protein, and proteins are enormous compared with "
            "alcohol or caffeine. The placenta lets small dissolved molecules "
            "through and effectively does not pass this one, which is exactly "
            "why insulin is the standard treatment for diabetes in pregnancy: "
            "it controls the mother’s glucose without reaching the foetus. It "
            "is the clearest proof that the rule is about size, not about "
            "safety — nothing has decided that insulin should be kept out.",
     "win": [0, 0],
     "win_text": "Not applicable: it does not arrive. Glucose, on the other "
                 "hand, crosses freely, which is why controlling the mother’s "
                 "blood glucose still matters a great deal."},
]


# ── the three timing windows (page lines 371–381) ────────────────────────
#
# `promoted` is Design's own flag on the middle row and `r_comparison` cannot
# carry it — see "What could not be lifted" 2. It is deliberately NOT authored
# here: R5 forbids a key no code reads, and an unread flag claiming an
# emphasis the page does not show is worse than no flag at all.
WINDOWS = [
    ("Weeks 1–2 · before most people know",
     "The ball of cells divides, implants and begins to build the placenta. "
     "There are as yet no organs to damage.",
     "Very little, or everything. An exposure at this stage tends either to "
     "have no lasting effect at all, or to stop the pregnancy continuing."),

    ("Weeks 3–8 · the embryo",
     "Heart, brain, spine, limbs, eyes and ears are all laid down, in an "
     "organism smaller than your thumb.",
     "Structure. This is the window in which an exposure can change how an "
     "organ is built rather than how well it works — and it is largely over "
     "by week eight."),

    ("Weeks 9–40 · the foetus",
     "The organs that exist grow and mature. The brain keeps developing right "
     "up to birth and beyond.",
     "Growth and function. Birth weight, lung readiness and brain development "
     "— changes in how well something works rather than whether it formed."),
]

WINDOW_ROWS = [{"name": when, "cells": [building, effect]}
               for when, building, effect in WINDOWS]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 126 character for character.
    "slug":        "lifestyle-and-the-developing-foetus",
    "title":       "Lifestyle and the developing foetus",
    "discipline":  "biology",
    "unit":        "reproduction",
    "family":      "SYSTEM",

    # ── curriculum position ─────────────────────────────────────────────────
    # The `e` clause of the split bullet — the effect of maternal lifestyle on
    # the foetus through the placenta. Minted in ks3_data/substatements.py for
    # this unit; §5.7's exactly-once rule means this lesson claims `e` and
    # nothing wider.
    "covers":      ["KS3.B.REP.01e"],
    # Named and leant on, not taught: the placenta as an exchange surface
    # between two separate circulations is `gestation-placenta-and-birth`'s
    # (REP.01d), and this lesson opens by assuming it.
    "touches":     ["KS3.B.REP.01d"],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2},
                    {"id": "substances-and-reactions", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # No `requires`: Design draws no "Before this lesson" card, and the engine
    # omits an empty one. Every forward and sideways link she draws lives in
    # the middle card — see "What could not be lifted" 3.
    "requires":    [],
    "assumes":     [],
    "references":  ["flowers-and-pollination",
                    "gestation-placenta-and-birth",
                    {"unit": "B6", "lesson": "alcohol-and-smoking"},
                    {"unit": "B6", "lesson": "substance-misuse-and-decisions"},
                    # ⊕ The edge rescued from the anti-blame paragraph's inline
                    # link, which `rich()` cannot carry. Last, so Design's four
                    # drawn links keep their order. See the docstring.
                    {"unit": "B6", "lesson": "what-drugs-do-to-the-body"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Substances that affect development, the epidemiology "
                   "behind public health advice, and how risk is estimated "
                   "from large studies.",

    # ── framing ─────────────────────────────────────────────────────────────
    # The whole lesson in one sentence, and the reason the second confrontation
    # is answerable: what crosses is decided by the molecule.
    "big_question": "The placenta is an exchange surface, not a filter. What "
                    "crosses it is decided by the molecule — not by whether "
                    "the foetus would be better off without it.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-windows` is the third: no control
    # of its own, so it mirrors `s-cross` and ticks on the panel's predicate —
    # see the docstring. `short` and `label` are Design's own `RAIL_SHORT` and
    # `RAIL` strings (page lines 330–336), all four of them.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Not a filter",
         "done_when": "committed"},
        # Design's own threshold, kept: `isDone('s-cross')` is
        # `Object.keys(s.opened).length >= 6` (page line 428). All six checked,
        # not one — a stop that ticked on the first substance would call the
        # panel finished at a sixth of it, and the lesson's claim is about the
        # SET.
        {"anchor": "s-cross", "short": "CROSS", "label": "Does it cross?",
         "done_when": "all_six_checked"},
        {"anchor": "s-windows", "short": "TIMING", "label": "Three windows",
         "mirrors": "s-cross", "done_when": "all_six_checked"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3). The right
    # answer is "all four", so the reveal corrects three of the four choices at
    # once and nobody is marked wrong for having believed in a filter.
    "phenomenon": {
        "title": "The placenta cannot tell the difference between oxygen and "
                 "alcohol.",
        "prompt": "It is a surface built for one job: letting small dissolved "
                  "molecules move from where there is more of them to where "
                  "there is less. It has no sorting mechanism, no sense of "
                  "what is wanted, and no way of stopping something simply "
                  "because it is harmful.",
        "commit": "Which of these reaches the foetus within minutes of "
                  "entering the mother's blood?",
        "options": [
            "Alcohol only",
            "Alcohol and nicotine",
            "Alcohol, nicotine, caffeine and carbon monoxide",
            "None of them — the placenta blocks all four",
        ],
        "reveal": "All four. Every one of them is a small molecule that "
                  "dissolves in blood, and that is the only qualification the "
                  "crossing requires. Within a few minutes the concentration "
                  "in the foetus's blood is close to the concentration in the "
                  "mother's. The interesting question is therefore not "
                  "<em>does it get through</em> — it is <em>what does it do "
                  "when it arrives, and does it matter more at some weeks "
                  "than others</em>.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # This pass owns REPRO-09 and REPRO-10 and mints nothing else. The third
    # belief this page confronts — that crossing the placenta and doing harm
    # are the same claim — is REPRO-21 and belongs to the commander; it is
    # named in the docstring and cited nowhere.
    #
    # `elicited_by` is honest per entry. REPRO-09 really is surfaced by the
    # panel — a student commits yes/no on six substances before seeing any
    # verdict, and option D of the hook offers the filter belief in as many
    # words. REPRO-10 is asked for nowhere: it is a conclusion a class draws
    # AFTER the biology, so the block that kills it is named for both.
    "misconceptions": [
        {"id": "REPRO-09",
         "statement": "The placenta filters out anything harmful.",
         "elicited_by": "does-it-cross",
         "confronted_by": "two-wrong-ideas"},
        {"id": "REPRO-10",
         "statement": "So anything that goes wrong is the mother's fault.",
         "elicited_by": "two-wrong-ideas",
         "confronted_by": "two-wrong-ideas"},
    ],

    # Design draws no keyword block anywhere in B5, so these never reach the
    # lesson body. The TERMS reach a student as the unit page's chips, and the
    # reading-age gate reads them as its exclusion list — which matters on a
    # page carrying "placenta", "foetus", "embryo", "haemoglobin" and
    # "rubella". Every definition is composed from this page's own claims and
    # says nothing the page does not; none of them addresses the reader.
    "vocabulary": [
        {"term": "placenta",
         "definition": "The exchange surface between two separate "
                       "circulations, where dissolved substances move between "
                       "the mother's blood and the foetus's blood.",
         "note": "It has no filtering ability."},
        {"term": "embryo",
         "definition": "The developing organism in the first eight weeks, "
                       "while the organs are being laid down.",
         "note": None},
        {"term": "foetus",
         "definition": "The developing organism from about week nine, once "
                       "the organs exist and are growing and maturing.",
         "note": None},
        {"term": "risk",
         "definition": "A probability measured across large numbers of "
                       "pregnancies.",
         "note": "It is not a prediction about any one of them."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # Design's legal line names ONE slot on this page and no artwork exists for
    # it, so it is DECLARED at `needed` rather than dropped: the manifest is
    # generated from this field, which turns a dangling reference into a
    # tracked sourcing task. `needed` is not a build blocker. No `figure` block
    # is added to `core` — Design draws no figure slot on the page.
    #
    # ⚠️ The caption describes the RULE, not a verdict: a size-and-solubility
    # diagram, with insulin drawn stopped by its own size rather than by
    # anything the placenta does. NOTES flag 13 asks Mide to confirm what he
    # wants illustrated on the human pages before anything is commissioned,
    # and this caption is a proposal, not a commission.
    "figures": [
        {"id": "b5-what-crosses",
         "kind": "diagram",
         "caption": "What crosses the placenta and what does not: small "
                    "soluble molecules — oxygen, glucose, alcohol, nicotine, "
                    "carbon monoxide, caffeine — diffusing across the "
                    "exchange surface, with large molecules such as insulin "
                    "shown too big to pass and antibodies shown carried "
                    "across using energy. The two blood supplies are drawn "
                    "separately and never mixing.",
         "status": "needed"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-cross — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b5/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 105), so the segment is measured, not inherited.
        {"type": "crosses-panel", "id": "does-it-cross", "anchor": "s-cross",
         "demand": "investigate",
         "eyebrow": "Six substances · one rule",
         "heading": "Does it cross, and what does it reach?",
         "head_counter": {"format": "{n} of 6 checked", "total": 6},
         "prompt": "Commit to an answer before you check. By the third one "
                   "you should be able to predict the rest — the rule turns "
                   "out to be about the molecule, not about the substance's "
                   "reputation.",

         "subs": SUBS,

         # The two-way commit. Index 0 is "it crosses", which is what
         # `subs[].crosses` is matched against — five of the six.
         "choices": [{"id": "yes", "label": "Yes — it reaches the foetus"},
                     {"id": "no", "label": "No — it does not cross"}],
         "commit_label": "Does it reach the foetus?",

         # ⚖️ The check is LOCKED until the student has committed. A student
         # who could read the verdict first and then say what they expected
         # has predicted nothing — and on this page in particular, the point
         # is that the rule is predictable once you stop reading reputations.
         "check_label": "Check it",
         "hint": {"idle": "Choose an answer first.",
                  "ready": "Ready.",
                  "done": "Now try another substance."},
         "verdict": {"right": "Correct", "wrong": "Not this time"},

         # The 0–40 week bar under every verdict. `label` is the mono caption
         # and `ticks` are the three axis marks, left to right.
         "window": {"label": "When it matters most",
                    "ticks": ["Week 0", "Week 20", "Week 40"]}},

        # #s-windows — the band panel: when an exposure matters and why.
        # Rail stop 3, mirroring `s-cross`; see the docstring. `comparison`
        # is the component —
        # a row name and two captioned columns, which is exactly Design's
        # `when` / `What is happening` / `What an exposure can affect`.
        {"type": "comparison", "anchor": "s-windows",
         "eyebrow": "Timing · three windows",
         "eyebrow_tone": "accent-text",
         "statement": "The same exposure does different things in different "
                      "weeks.",
         "ground": "band",
         "columns": [
             {"caption": "What is happening", "tone": "ink"},
             {"caption": "What an exposure can affect", "tone": "ink"},
         ],
         # Design paints both cells in the same weight here — unlike b3-01,
         # where the consequence column reads one step quieter. Measured from
         # her markup (page lines 175–182): both are the same 18px/1.5 body.
         "row_tones": ["ink", "ink"],
         "rows": WINDOW_ROWS,
         # Nested inside the panel, on the card ground — Design's own
         # arrangement (page lines 188–191).
         "key_fact": {"ref": "size-and-solubility", "ground": "card"}},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "REPRO-09"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside the comparison, on the card ground. It is the neutral-
    # surface claim stated flatly: the deciding property is the molecule, and
    # the timing is about what is being built, not about anyone's conduct.
    "key_facts": [
        {"id": "size-and-solubility",
         "text": "Whether a substance reaches the foetus depends on the size "
                 "of its molecules and whether they dissolve in blood — not "
                 "on whether it is harmful. The placenta has no filtering "
                 "ability. What the substance then does depends on what is "
                 "being built that week.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`, and an authored statement wins over the register.
        # The block asks for no commitment, on Design's page and here, so it
        # is not a rail stop and emits no completion contract.
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "REPRO-09",
         "statements": [
             # ── REPRO-09 ────────────────────────────────────────────────
             # The neutral-surface argument in full, including the two
             # exceptions that prove it is about size: insulin (too large,
             # which is why it treats diabetes in pregnancy) and antibodies
             # (large, and carried over deliberately at a cost in energy).
             {"quote": "The placenta filters out anything harmful.",
              "body": ["It filters nothing. Read the word <em>barrier</em> — "
                       "which is how the placenta is often described — and it "
                       "is easy to picture a sieve deciding what to admit. "
                       "What is actually there is a very thin, very large "
                       "surface designed to let small dissolved molecules "
                       "through as fast as possible, because oxygen and "
                       "glucose have to arrive at the rate a growing organism "
                       "uses them. Anything else small enough and soluble "
                       "enough gets the same easy passage: it is using the "
                       "door built for the food. The one real rule is size. "
                       "Large molecules such as insulin do not cross in any "
                       "useful quantity, which is why insulin can be used to "
                       "treat diabetes during pregnancy; antibodies are large "
                       "too, and cross only because the placenta spends "
                       "energy carrying them over deliberately. Everything "
                       "else is physics, and physics has no opinion about "
                       "what is good for a foetus."]},

             # ── REPRO-10 · NOTES-B5 FLAG 28 ─────────────────────────────
             # ⚠️⚠️ THE SINGLE MOST IMPORTANT STRING ON THIS PAGE, AND THE
             # ONE DESIGN ASKS TO HAVE CONFIRMED IN ITS EXACT WORDING.
             #
             # LIFTED WHOLE. Not shortened, not reordered, not softened, not
             # improved. Every clause is in Design's order and none is
             # paraphrased. The ONLY difference from her markup is that her
             # inline <a> around "What drugs do to the body" is gone, because
             # `rich()` allows <em> and <strong> and nothing else by an
             # explicit ruling (build_ks3.py:236). The LINK TEXT stays in the
             # sentence, so no word is lost, and the destination is preserved
             # in `references[]`. See the docstring.
             #
             # If this paragraph ever has to change, it is Mide's call and
             # nobody else's, and it changes as a whole.
             {"quote": "So anything that goes wrong is the mother's fault.",
              "body": ["That does not follow from any of the biology on this "
                       "page, and it is worth saying why. Much exposure is "
                       "not a choice: second-hand smoke, air pollution at the "
                       "roadside, an infection caught from someone else, a "
                       "medicine that must be continued because stopping it "
                       "would be more dangerous than taking it. Some are "
                       "choices constrained by circumstances — what food is "
                       "affordable and near enough to buy. Addiction is a "
                       "condition of the nervous system rather than a "
                       "decision repeated daily, which is the point What "
                       "drugs do to the body spends a whole lesson "
                       "establishing. And a great many pregnancy "
                       "complications have no identified cause at all. There "
                       "is also the shape of the evidence: what studies "
                       "measure is <em>risk</em> — a probability across large "
                       "numbers of pregnancies — so an exposed pregnancy that "
                       "comes to no harm and an unexposed one that does are "
                       "both entirely ordinary results. Risk is a statement "
                       "about populations. It is not a verdict on a person."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RULED 17 Aug 2026, AND RUNG 1 IS FIXED. Its
    #   three distractors are Mide's own replacement copy, applied verbatim,
    #   and each now states a WRONG RULE in the same shape as the correct
    #   answer. The correct option, `answer: 1` and the gate's threshold are
    #   untouched. Measured after: 15 against 15 / 17 / 15.
    #   rung 2: correct is 1 word against 5 / 1 / 1 — clean, and untouched.
    #
    #   ⛔ Superseded, kept: this block used to read "MEASURED, AND RUNG 1
    #   FAILS IT … Lifted unrepaired and reported: every option is Design's
    #   science copy and MRB-205 says the page wins." It was reported; he
    #   ruled. See the docstring.
    #
    # Design's rung titles are kept verbatim, including "Apply the rule" on the
    # `recall` slot: the engine's slot names are internal and the student reads
    # the title.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Apply the rule",
            "q": "Why does alcohol reach a developing foetus?",
            "options": [
                "Because the mother's blood and the foetus's blood mix, so "
                "anything in hers reaches it",
                "Because it is a small molecule dissolved in blood, so it "
                "diffuses across the placenta",
                "Because the placenta breaks alcohol down slowly, so some of "
                "it gets past before it is destroyed",
                "It does not — the placenta filters out anything harmful "
                "before it can reach the foetus",
            ],
            "answer": 1,
            "feedback": {
                0: "They never mix. Every crossing happens across a surface, "
                   "between two separate circulations.",
                2: "The placenta is not trying to break it down. It is a "
                   "surface for exchange, and small soluble molecules cross "
                   "it as a matter of course.",
                3: "The placenta has no filtering ability. Within minutes the "
                   "foetal concentration is close to the mother’s.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Which of these does NOT cross the placenta in any useful "
                 "amount?",
            "options": [
                "Carbon monoxide from cigarette smoke",
                "Caffeine",
                "Insulin",
                "Alcohol",
            ],
            "answer": 2,
            "feedback": {
                0: "It crosses easily and takes up space on haemoglobin that "
                   "oxygen would otherwise use.",
                1: "It crosses easily, and the foetus breaks it down slowly. "
                   "The advice on caffeine is a limit, not a ban — but it "
                   "does arrive.",
                3: "A small molecule that dissolves in water and fat — it "
                   "crosses within minutes.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the rule",
            "q": "Explain what decides whether a substance reaches a "
                 "developing foetus. Give two examples that cross and one "
                 "that does not, and say why the placenta cannot protect the "
                 "foetus from harmful substances.",
            "field_label": "Your explanation",
            "placeholder": "What decides it is…",
            "success": [
                "Says the deciding factor is the size of the molecule and "
                "whether it dissolves in blood.",
                "Gives two correct examples that cross — for instance "
                "alcohol, nicotine, carbon monoxide, caffeine.",
                "Gives a correct example that does not cross, such as "
                "insulin, and says it is too large.",
                "Says the placenta is an exchange surface, not a filter, and "
                "has no mechanism for sorting.",
                "Says harmful small molecules use the same route as oxygen "
                "and glucose.",
            ]},
        "produce": {
            # ⚑ The rung that carries the third belief (REPRO-21, not minted
            # here): its first criterion separates crossing from harming, and
            # its last one is the anti-blame paragraph's own closing idea —
            # a change in risk across a population, not a prediction about one
            # pregnancy. The lesson ends on a claim about evidence, not on a
            # claim about anybody's conduct.
            "title": "Rung 4 · Take it somewhere new",
            "q": "A headline says: “Coffee in pregnancy harms babies.” Using "
                 "what you know about crossing, dose and evidence, set out "
                 "three questions you would need answered before deciding "
                 "what to make of it.",
            "field_label": "Your answer",
            "placeholder": "First I would want to know how much…",
            "success": [
                "Asks about dose — how much caffeine, since crossing the "
                "placenta and being harmful at a given amount are separate "
                "claims.",
                "Asks how the effect was measured and how large it was, "
                "rather than accepting “harms” as all-or-nothing.",
                "Asks about the study: how many pregnancies, over how long, "
                "and what else differed between the groups compared.",
                "Says the result would be a change in risk across a "
                "population rather than a prediction about one pregnancy.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # ⚠️ It closes on risk, deliberately. The last thing a student photographs
    # off this page is "a probability across many pregnancies, not a certainty
    # about one" — which is the anti-blame paragraph in one sentence.
    "key_note": "The placenta lets small dissolved molecules diffuse across, "
                "and cannot distinguish useful ones from harmful ones. "
                "Alcohol, nicotine, carbon monoxide, caffeine and most "
                "medicines all reach the foetus; large molecules such as "
                "insulin do not. Carbon monoxide from smoke reduces the "
                "oxygen the blood can carry, which is why smoking lowers "
                "birth weight. Alcohol affects the developing brain and "
                "nervous system throughout. Organs are laid down in weeks "
                "three to eight, so that window matters most for structure, "
                "and the brain is being built for the whole pregnancy. Risk "
                "is a probability across many pregnancies, not a certainty "
                "about one.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # NOTES flag 29. The historical failure is put on regulators and on what
    # "safe testing" meant in 1957 — never on any individual — and it closes
    # on the substance not having been the villain. That framing is the same
    # one the whole lesson runs on, and it is Design's.
    "stretch": [
        {"type": "explainer", "id": "thalidomide",
         "text": "Almost everything on this page is known because of "
                 "thalidomide. It was sold from 1957 as a safe sedative, "
                 "prescribed widely for morning sickness, and marketed as "
                 "harmless partly because a large dose did not kill "
                 "laboratory animals — which was, at the time, most of what "
                 "safe testing meant. Thousands of babies were born with "
                 "severely shortened or absent limbs. Two doctors working "
                 "separately, William McBride in Australia and Widukind Lenz "
                 "in Germany, traced the pattern back to the drug, and it was "
                 "withdrawn in 1961. What made the case scientifically "
                 "decisive was the timing: the damage depended on which days "
                 "of the pregnancy the tablets were taken, in a window of "
                 "only a few weeks while the limbs were forming, and the "
                 "specific malformation shifted with the day. That is how "
                 "precisely the sensitive window of development came to be "
                 "mapped. The disaster is the reason drugs are now tested on "
                 "pregnancy specifically, why licensing exists in the form it "
                 "does, and why a pharmacist will not hand over an ordinary "
                 "medicine to someone who is pregnant without checking first. "
                 "Thalidomide itself is still in use today, under tight "
                 "controls, for conditions including a cancer of the blood — "
                 "which is the second lesson: the substance was never the "
                 "villain, the missing knowledge was."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to check why molecule size decides what crosses?",
              "cta": "Ask about this lesson",
              "anchor": "s-cross"},

    # ⚠️⚠️ THE LEGAL LINE, BYTE-IDENTICAL AND WHOLE. It is safeguarding copy
    # and it is load-bearing: risk is not a verdict, nothing here judges any
    # person or family, anyone pregnant or who might be speaks to a midwife,
    # doctor or pharmacist BEFORE STARTING OR STOPPING ANYTHING — prescribed
    # medicines included — and that advice is free and confidential.
    #
    # ⊕ `convention_note`, NOT `safety_note`, and the choice is deliberate.
    # `safety_note` ships `class="ks3-safety"`, the treatment reserved for
    # "never light a candle without an adult with you" — a callout. §8.10 and
    # the MRB-244 brief both say this line is small, at the bottom edge, and
    # never a callout: it is a statement about what risk means and where to
    # take a question, not an instruction shouted at a bench. Plain
    # `ks3-legal` is exactly that treatment, and it sits above the standing
    # legal line. b4-01, b3-05 and b3-07 route their foot lines the same way.
    #
    # ⚠️ Design sets the figure id in mono inside the sentence; a foot line is
    # escaped, so `b5-what-crosses` renders in body copy. The words are
    # unchanged.
    "convention_note": "This lesson describes exposures and risk. Risk is a "
                       "probability measured across large numbers of "
                       "pregnancies, not a prediction about any one of them, "
                       "and nothing here is a judgement about any person or "
                       "family. Anyone who is pregnant or might be should "
                       "speak to a midwife, doctor or pharmacist before "
                       "starting or stopping anything, including prescribed "
                       "medicines; that advice is free and confidential. "
                       "Relationships and consent are covered in your RSE and "
                       "PSHE lessons. The what-crosses diagram is declared in "
                       "the lesson record as b5-what-crosses, awaiting "
                       "illustration.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The panel is commit-then-check across six cases, and rung 4 asks what
    # would have to be true of a study before a headline means anything.
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
