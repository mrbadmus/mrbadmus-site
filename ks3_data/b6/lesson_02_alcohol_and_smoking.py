"""B6 L2 — Alcohol and smoking (SYSTEM).

Authored against Design's approved page,
`KS3 B6 lessons/b6-02-alcohol-and-smoking.dc.html` (588 lines), under the
MRB-220 build contract, with `NOTES-B6.md` §1, §2.2, §3 and §4 as the
delivery's own notes.

**Every student-facing string is lifted byte-identical** from the approved
page, except the items listed under "What could not be lifted", none of which
is a sentence of science. The five drinks, the six interventions, the two
long-term cards and all four ladder rungs came out of
`node tools/extract_design_payload.js`, not off a keyboard. On this unit that
is a safeguarding rule as much as an accuracy one: the register was ruled once
(NOTES-B6 §1) and an author who paraphrases is re-taking that ruling.

── ⚠️ TONE IS A GATE, AND IT WAS RULED BEFORE THIS PASS ─────────────────

Clinical, function-first, no scare copy, no reassurance copy, no euphemism,
and **no doses, thresholds or methods**. Nothing on this page addresses the
reader as someone whose family does not drink or smoke, because in any class
that is not true. Nothing here is softened and nothing is sharpened.

⚑ **The vape paragraph (NOTES-B6 flag 9) is APPROVED BY MIDE, resolved
16 Aug 2026, and ships exactly as written.** It is the `stretch` layer's whole
body, below. Every clause is load-bearing and the paragraph is balanced **as a
whole**: no tar, no carbon monoxide, the same or stronger nicotine dependence,
very likely less harmful than cigarettes, **not known to be safe**, nothing to
gain for a non-smoker, illegal to sell to under-18s. Trimming any one clause
tips it into either advertisement or scare copy. It is one string, lifted
whole, including both `<em>` spans; nothing about it is reordered, shortened
or annotated. Verified clause for clause against the page — see the report.

The `ks3-layer ks3-support` referral block points at "the services listed in
your school's PSHE materials" rather than at a named helpline. That is
Design's decision and NOTES-B6 §1 says why: a named helpline goes stale, and
naming one is a safeguarding decision rather than an authoring one. Carried as
drawn.

── The instrument IS the lesson ─────────────────────────────────────────

`#s-clock` is `clearance-clock` on `ks3-block ks3-dark ks3-practical` (page
line 105), so `practical` is MEASURED from Design's own markup.

⚖️ **NO INTERVENTION CHANGES THE NUMBER OF HOURS.** Six things a student can
try, every one of them something people genuinely believe, and the hours are
`units` for all six. That identity is not a simplification of the instrument —
it is the instrument. The single honest exception is *A big meal first*, which
changes the PEAK and not the clock, and its own note says so in as many words:
*"The total amount to break down has not changed, so the hours have not
changed."* A payload in which any `fix` carried an hours delta would have
destroyed the lesson, so no `fix` carries one and there is no key it could be
written in.

The arithmetic is `hours = units`, `remaining = max(0, units - hour)`, cap 12.
That is Design's own `renderVals` (page lines 461–478) and it is why the
verdict can say *"which is exactly the number of units"*.

── FOUR rail stops — Design's fourth restored (MRB-249) ──────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that
`#s-years` came off the rail. Design draws FOUR stops (page lines 327–332) and
`#s-years` ticks on `s.everRan` (page line 420) — the CLOCK's predicate,
verbatim, one section to the left — and because `#s-years` is an eyebrow, a
statement, two static cards and a key fact, with no control, no commitment and
no field, the reading was that MRB-208's completion rule ruled it out and
`ks3_parity.check_rail_reachable` would fail a `rule` section for carrying none
of the signals `doneByDom()` reads. So the lesson shipped THREE stops.

Two things overrule that inference.

MRB-205 binds and is not re-argued: Design draws, we render; nothing invented,
nothing dropped; page wins over engine. Dropping a stop Design drew is not
rendering what Design drew.

And `s.everRan` written twice is Design stating the tick condition, not Design
repeating herself. `isDone()` is rail-level and returns the identical
expression for `#s-clock` and then for `#s-years`. Years of nights is the
payoff of one night on the clock; the section holds no control because the
clock has already taken the student's commitment. That is a MIRROR, resolved at
rail level in `wireRail`'s `paint()`.

So the fourth stop is declared: anchor `s-years`, `mirrors: "s-clock"`,
`done_when: "clock_run"` — the clock's own predicate, named as borrowed, and
gated by `check_rail_matches_design` against `docs/ks3/rail-manifest.md`.
b4-01's `#s-parts`, c1-02's `#s-matrix`, c1-05's `#s-scale`, b3-01's
`#s-nutrients` and b3-02's `#s-limits` are restored the same way. The section
keeps its anchor, as it always did, so every hash link into it still works.

── What could not be lifted, and why ────────────────────────────────────

1. **The long-term cards' ROW STRUCTURE flattens into the card gloss.** Design
   draws `#s-years` as two cards, each with a mono accent `kind`, a display
   `name` and a `<ul>` of four `organ` / `effect` rows (page lines 160–175).
   `r_rule`'s card is two fields — `term` and `gloss` — and §5.1.1's vocabulary
   is closed, so there is no block type with a nested row list. Every string
   survives: `kind` and `name` are joined into the term with " · " in Design's
   own document order (b4-01's `#s-parts` precedent, and Design's own separator
   elsewhere on the page), and the four rows become the gloss with each organ
   in `<strong>` and its effect after an em dash. Nothing is dropped, nothing
   is summarised, and the two-card contrast the statement depends on
   ("Each one damages a different set of organs") survives because there are
   still exactly two cards. Reported: the fix, if the rows are to keep their
   list, is a nested `rows` slot on `rule` — not a new block type.

2. **The key fact leaves Design's band panel.** She nests it inside `#s-years`
   (page lines 177–180); `r_rule` has no nested key-fact slot (only
   `r_comparison` does), so it renders as its own top-level block directly
   under the panel, on the band ground every other top-level key fact in the
   key stage takes. The words are unchanged and the order is unchanged. Same
   resolution as b4-01.

3. **The confrontation's LINK to b4-04 becomes a `references` edge; its words
   stay.** The second wrong idea ends *"…is the subject of Exercise, asthma and
   smoking"* with `Exercise, asthma and smoking` as an `<a>` (page line 193).
   `rich()` admits `<em>` and `<strong>` and nothing else, so the anchor cannot
   render inside the body. The sentence is lifted byte-identical without the
   markup, and the EDGE lives once in `references` — which is where the
   endmatter's "Connects to" card is generated from. So b4-04 is cited twice in
   words, exactly as NOTES-B6 §4 asks, and declared once as data. §4.6's
   single-source rule holds: the smoke-damage content itself is b4-04's and is
   not repeated here in any form.

4. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose and §4.8.1 D makes the two mutually exclusive.

5. **The foot line is `convention_note`, not `safety_note`.** Design draws ONE
   plain `.ks3-legal` paragraph (page line 317); `safety_note` would emit
   `class="ks3-legal ks3-safety"`, a treatment she did not use here. The line
   is a statement of what the model ignores, and its last sentence is a limit
   on what the model may be used for — a note about how the numbers on this
   page were taken, which is exactly what MRB-228 minted `convention_note` for.
   It sits small at the bottom edge, never a callout (§8.10). b3-05, b3-07 and
   b4-01 resolve the identical foot line the identical way.

⚑ For Mide's science gate — NOTES-B6 §3 flags landing on THIS lesson:
  * flag 5 — **alcohol at "roughly one unit an hour"**. Six statements and the
    whole arithmetic of the instrument depend on it; usually given as
    1 unit/hour, sometimes as 1 unit in 60–90 minutes. Authored as delivered.
  * flag 6 — **the drink unit values**: half of beer 1, single shot 1, can of
    cider 2, large wine 3, pint of strong lager 3. Plausible and rounded.
    Authored as delivered, as `DRINKS` below.
  * flag 7 — carbon monoxide binding haemoglobin in oxygen's place, in the
    long-term card and in rung 3. The lesson does not use the word
    *carboxyhaemoglobin*; confirm the depth.
  * flag 8 — cigarette filters: removes some tar, does nothing to carbon
    monoxide, encourages deeper inhaling, and ventilation holes inflate
    machine-measured tar figures. The ventilation-hole detail is the least
    well known of the four.
  * flag 9 — **the vape paragraph. RESOLVED 16 Aug — keep, word for word.**
    Recorded here because the resolution is what this module implements.
  * flag 14 — **no diagrams and no figure slots anywhere in B6.** Verified on
    this page: it draws no figure, and its `.ks3-legal` line names no diagram
    id. So `figures` is `[]` — measured, not omitted, and nothing is invented
    to fill it.

⚑ Two wording flags of my own, and the page WINS on both (MRB-205):
  1. **An internal lesson code reaches a student.** The last long-term row
     reads *"Which substance does which damage is b4-04's subject, not this
     lesson's."* — `b4-04` is a filename, not something a student can resolve,
     and the same page names the same lesson properly twice ("Exercise, asthma
     and smoking"). Lifted byte-identical because the page wins and this is
     teaching copy rather than a build fault, but it is the one string on the
     page I would ask you to change, to the lesson's title.
  2. The hook's option D is *"A large meal afterwards"* while the bench's fix
     is *"A big meal first"*. Not a contradiction — the two differ on purpose,
     and the timing is the difference — but they are one letter apart in a
     student's memory, and the hook never says which one it meant.
"""

# ── the five drinks (page lines 335–341, via extract_design_payload.js) ──
#
# NOTES-B6 flag 6. `units` is what the instrument adds; the button prints
# "label · units", so the number a student presses is the number the arithmetic
# uses and there is no second place for it to drift.
DRINKS = [
    {"id": "beer",  "label": "Half of beer",        "units": 1},
    {"id": "shot",  "label": "Single shot",         "units": 1},
    {"id": "cider", "label": "Can of cider",        "units": 2},
    {"id": "wine",  "label": "Large wine",          "units": 3},
    {"id": "lager", "label": "Pint of strong lager", "units": 3},
]

# ── the six interventions (page lines 343–356) ──────────────────────────
#
# ⚖️ NOT ONE OF THESE CARRIES AN HOURS DELTA, AND THERE IS NO KEY IT COULD BE
# WRITTEN IN. `note` is the whole of an intervention's effect. `food` is the
# one that does something real and its own note says what: the peak moves, the
# clock does not.
FIXES = [
    {"id": "time", "label": "Nothing but time",
     "note": "The only thing on this bench that moves the number. One unit an "
             "hour, set by how much enzyme the liver has, and it is the same "
             "rate whether the person is asleep, awake, worried or in a hurry."},
    {"id": "coffee", "label": "Black coffee",
     "note": "Caffeine is a stimulant, so they feel more awake. The alcohol is "
             "untouched. You have converted a sleepy drunk person into an "
             "alert drunk person, and the alert one is the one who thinks they "
             "can drive."},
    {"id": "shower", "label": "Cold shower",
     "note": "Cold skin, sharp intake of breath, no change whatever in the "
             "blood. The liver is not on the outside of the body."},
    {"id": "air", "label": "Fresh air and a walk",
     "note": "Only a trace of alcohol leaves through the lungs — which is "
             "exactly why a breath test works, and why breathing harder cannot "
             "clear it. The rest goes through the liver."},
    {"id": "food", "label": "A big meal first",
     "note": "This one does something real, and it is not what people claim. "
             "Food in the stomach slows absorption, so the peak in the blood "
             "is lower and the person is less impaired at their worst. The "
             "total amount to break down has not changed, so the hours have "
             "not changed."},
    {"id": "water", "label": "Pints of water",
     "note": "Genuinely helps the dehydration, the headache and the thirst. "
             "Does nothing at all to the alcohol — you cannot dilute your way "
             "out of a fixed amount."},
]

# ── the two long-term cards (page lines 358–371) ────────────────────────
#
# `kind` and `name` are joined into the rule card's TERM in Design's document
# order; the four rows become its GLOSS. See "What could not be lifted" 1. The
# strings themselves are untouched — the joining is the only thing authored
# here, and it is done once, below, rather than by hand eight times.
LONG_TERM = [
    ("Depressant", "Alcohol, over years", [
        ("Liver",
         "Working cells are replaced by scar tissue. Early damage recovers if "
         "drinking stops; scarring does not."),
        ("Brain",
         "Tissue is lost, and memory and judgement are affected long before "
         "anyone would call the person unwell."),
        ("Stomach and gut",
         "Lining irritated and inflamed, which is why heavy drinkers bleed and "
         "vomit."),
        ("Whole body",
         "Raised risk of several cancers, high blood pressure and stroke — "
         "and, because judgement goes first, a large share of accidents and "
         "injuries."),
    ]),
    ("Stimulant plus a poison plus tar", "Tobacco smoke, over years", [
        ("Brain",
         "Nicotine reaches it in about ten seconds and the reward pathways "
         "adapt to expect it. That adaptation is why stopping is hard, and it "
         "is not what causes the disease."),
        ("Blood",
         "Carbon monoxide binds to haemoglobin in place of oxygen and holds "
         "on. Less oxygen is delivered to every tissue, and a smoker is out of "
         "breath sooner for that reason alone."),
        ("Heart and vessels",
         "Vessels narrow, blood pressure rises, and clots form more readily — "
         "heart attack and stroke risk both climb."),
        # ⚑ The internal lesson code that reaches a student — flag 1 in the
        # docstring. Lifted byte-identical, curly apostrophes and all, because
        # the page wins.
        ("Airways and alveoli",
         "Damaged by tar and by the other substances in the smoke. Which "
         "substance does which damage is b4-04’s subject, not this lesson’s."),
    ]),
]

LONG_TERM_CARDS = [
    {"term": "%s · %s" % (kind, name),
     "gloss": " ".join("<strong>%s</strong> — %s" % (organ, effect)
                       for organ, effect in rows)}
    for kind, name, rows in LONG_TERM
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 134 character for character (§8.4 —
    # slugs are permanent and are the join for every progress record).
    "slug":        "alcohol-and-smoking",
    "title":       "Alcohol and smoking",
    "discipline":  "biology",
    "unit":        "health-and-drugs",
    "family":      "SYSTEM",

    # ── curriculum position ─────────────────────────────────────────────────
    # The `b` clause of the split bullet — the effects of alcohol and of
    # tobacco smoke on behaviour, health and life processes. Minted in
    # ks3_data/substatements.py, where the split is flagged for Mide as this
    # file's weakest-provenance mint. `a` is b6-01's and `c` is b6-03's;
    # §5.7's exactly-once rule fails the build on any overlap.
    "covers":      ["KS3.B.HLTH.01b"],
    # Named but not taught. Each is a lesson that owns it and is linked:
    # GAS.03 is b4-04's (what smoke does to the airways — deferred to twice
    # and taught nowhere here), NUT.04b is b3-06's (the liver's rate is set by
    # "how much enzyme it contains"), RESP.01 is B8's (rung 3 ends at muscles
    # that "cannot respire aerobically as fast").
    "touches":     ["KS3.B.GAS.03", "KS3.B.NUT.04b", "KS3.B.RESP.01"],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2},
                    {"id": "substances-and-reactions", "level": 2}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design draws a "Before this lesson" card with one link (page line 296)
    # and a "Connects to" card with two (page lines 302–303). b4-04 is the
    # first of the two and is the edge the confrontation also names in words —
    # see "What could not be lifted" 3.
    "requires":    ["what-drugs-do-to-the-body"],
    "assumes":     [],
    "references":  [{"unit": "B4", "lesson": "exercise-asthma-and-smoking"},
                    {"unit": "B3", "lesson": "enzymes-in-digestion"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Risk factors for non-communicable disease, the difference "
                   "between correlation and cause in population studies, and "
                   "how a causal link is established.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Two drugs that are legal for adults, sold openly, and "
                    "between them responsible for more illness in this country "
                    "than every illegal drug put together. Both are worth "
                    "understanding as biology before anyone argues about them.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-years` is the third: no control of
    # its own, so it mirrors `s-clock` and ticks on the clock's predicate — see
    # the docstring. `short` and `label` are Design's own `RAIL_SHORT` and
    # `RAIL` strings (page lines 327–333).
    #
    # ⚠️ MRB-208: nothing is ticked on load. `done_when` is R2's gate field —
    # every stop names the condition that completes it, and every named
    # condition is one the page can actually reach, whether the stop owns the
    # control or mirrors the section that does.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Three tricks",
         "done_when": "committed"},
        # Design's own threshold, kept: `isDone('s-clock')` is `s.everRan`,
        # which is true once the student has pressed "Wait an hour" at least
        # once. Adding drinks is not completion — a student who filled the
        # glass and walked away has not seen the clock refuse to move.
        {"anchor": "s-clock", "short": "CLOCK", "label": "Beat the liver",
         "done_when": "clock_run"},
        {"anchor": "s-years", "short": "YEARS", "label": "Years of nights",
         "mirrors": "s-clock", "done_when": "clock_run"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3).
    "phenomenon": {
        "kind": "narrative",
        "title": "Black coffee, a cold shower, a walk in the fresh air.",
        "prompt": "Three things people are certain will sober someone up. Two "
                  "of them do nothing at all to the alcohol in their blood, "
                  "and the third does nothing either. The alcohol is not on "
                  "their skin or in their lungs — it is in the blood, and only "
                  "one organ can take it out.",
        "commit": "What actually lowers the alcohol in someone's blood?",
        "options": [
            "Strong black coffee",
            "Cold air and a walk home",
            "Time, and nothing else",
            "A large meal afterwards",
        ],
        "reveal": "The liver, working at its own fixed rate of roughly one "
                  "unit an hour. Nothing raises that rate. Coffee makes a "
                  "drunk person more awake without making them less drunk, "
                  "which is worse than useless — it is an alert person with "
                  "the judgement and reaction times of a drunk one.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ The `DRUG` family is PRE-ALLOCATED per lesson (see ks3_data/b6/
    # __init__.py), because B4's five parallel authors collided twice on
    # `BREATH` ids. This lesson owns DRUG-03 and DRUG-04 and mints nothing
    # else of its own.
    #
    # ⚑ THE PAGE CARRIES THREE BELIEFS IN TWO DRAWN QUOTES. Design's second
    # quote is a conjunction — "A few cigarettes now and then is basically
    # fine, AND filters make them safer" — and the body treats the two halves
    # as separate arguments, spending four sentences on the filter alone
    # ("The filter is the more interesting half of the claim"). They are two
    # beliefs, a student can hold either without the other, and the register
    # cannot record one entry for both. The third takes **DRUG-08**, which is
    # outside my allocation and is declared here for the commander to mint;
    # it is confronted on this page, in the same drawn quote.
    #
    # ⊕ DRUG-01 IS CITED HERE AND DELIBERATELY NOT DECLARED — commander's
    # ruling, MRB-244, normalising the two opposite calls this unit produced.
    #
    # This page's big question IS b6-01's belief ("legal for adults … more
    # illness than every illegal drug put together"), so the id is reused
    # rather than near-duplicated, exactly as NOTES-B6 §5 asks. But a
    # `misconceptions` row is not a citation — `confronted_by` names the
    # ACTIVITY that does the confronting, and every other value in the key
    # stage names a place on its OWN page. The first cut here named a lesson
    # slug, which is a pointer no page can resolve and a join that reads as
    # working precisely because nothing checks it.
    #
    # The precedent is `CELL-08` in b3-08: a borrowed id is re-declared only
    # where the page genuinely RE-CONFRONTS the belief with a real activity.
    # This page does not confront it — it opens on it. So the reappearance
    # lives in the register's DRUG section as a reappears note, which is what
    # NOTES-B6 §5 asked for in the first place, and b6-03 read correctly.
    "misconceptions": [
        {"id": "DRUG-03",
         "statement": "Coffee, a cold shower or fresh air will sober you up.",
         "elicited_by": "beat-the-liver",
         "confronted_by": "two-wrong-ideas"},
        {"id": "DRUG-04",
         "statement": "A few cigarettes now and then is basically fine.",
         "elicited_by": "two-wrong-ideas",
         "confronted_by": "two-wrong-ideas"},
        {"id": "DRUG-08",
         "statement": "Filters make cigarettes safer.",
         "elicited_by": "two-wrong-ideas",
         "confronted_by": "two-wrong-ideas"},
    ],

    # Design draws no keyword block anywhere in B6, so these never reach the
    # lesson body. The TERMS reach a student as the unit page's chips, and the
    # reading-age gate reads them as its exclusion list — which matters here,
    # because "depressant", "stimulant", "haemoglobin" and "dependence" would
    # otherwise all count against the page.
    #
    # ⚠️ Definitions are the only student-facing strings in this module that
    # are NOT on Design's page, because she draws nowhere to put them. Each is
    # built from a sentence the page already says, in the page's own register:
    # clinical, no dose, no threshold, no judgement.
    "vocabulary": [
        {"term": "depressant",
         "definition": "A drug that slows the nervous system, so reactions, "
                       "coordination and judgement all worsen.",
         "note": "Alcohol is one."},
        {"term": "stimulant",
         "definition": "A drug that raises alertness and speeds the body up.",
         "note": "Caffeine and nicotine are both stimulants."},
        {"term": "unit",
         "definition": "The measure used for the amount of alcohol in a drink, "
                       "so that different drinks can be compared.",
         "note": "The liver clears about one unit an hour."},
        {"term": "tar",
         "definition": "The sticky mixture in tobacco smoke that damages the "
                       "airways and the alveoli.",
         "note": None},
        {"term": "carbon monoxide",
         "definition": "A gas in tobacco smoke that binds to haemoglobin in "
                       "place of oxygen and holds on.",
         "note": "Less oxygen then reaches every tissue."},
        {"term": "dependence",
         "definition": "The state in which the body has adapted to expect a "
                       "drug, so stopping is physically difficult.",
         "note": "Nicotine is what makes smoking hard to stop."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # NOTES-B6 flag 14: B6 names no diagram slots and draws none, its visuals
    # being the three instruments. VERIFIED ON THIS PAGE: it contains no
    # `<figure>`, no figure slot and no image, and its `.ks3-legal` line names
    # no diagram id (unlike b4-01's, which is why b4-01 declares one). So this
    # is measured absence, not an omission — nothing is declared and nothing is
    # invented to fill it.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-clock — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b6/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 105), so the segment is MEASURED and not inherited.
        {"type": "clearance-clock", "id": "beat-the-liver", "anchor": "s-clock",
         "demand": "investigate",
         "eyebrow": "At the bench · one liver, one clock",
         "heading": "Try to beat the liver",
         "prompt": "Build an evening's drinks, pick something to speed the "
                   "clearing up, then run the clock. Every trick on this bench "
                   "is one people genuinely believe in. Only one of them "
                   "changes anything, and not the thing they think.",

         # The mono readout on the eyebrow row (page line 111). THREE states,
         # driven by the instrument's own arithmetic: nothing run yet, running,
         # and cleared.
         "progress": {"idle": "clock not started",
                      "running": "clock running",
                      "clear": "cleared"},

         "drinks": DRINKS,
         "fixes": FIXES,

         # Design's own props and state (page lines 326, 428–436). `start_fix`
         # is `coffee` deliberately: the page opens on the intervention the
         # hook has just named, so the first thing a student reads on the
         # bench is why the coffee does nothing.
         "start_units": 4,
         "start_fix": "coffee",
         "max_units": 12,

         # The two control-group labels (page lines 116, 125).
         "add_label": "Add a drink",
         "fix_label": "And to sober up faster",

         # The readout panel (page lines 135–147). `{n}` is a count and `{s}`
         # is its plural; `{h}` is hours elapsed and `{r}` is units left. Every
         # string is Design's, with her runtime concatenations written as one
         # template each rather than as fragments — the fragments are not
         # sentences and could not be checked by a reader.
         "units_label": "{n} unit{s} drunk",
         "hours_label": "{n} hour{s} to clear",
         "hours_none": "nothing to clear",
         "blood_label": "Alcohol still in the blood",
         "remaining_label": "{h} hour{s} elapsed · {r} unit{s} left",

         # ⚖️ "Wait an hour" is the ONLY control that advances the clock, and
         # it is disabled once the blood is clear. There is no run-to-the-end
         # control, on Design's page or here: a student who wants to see six
         # hours pass has to press it six times, and pressing it is what makes
         # the point that nothing else would have gone faster.
         "wait_label": "Wait an hour",
         "clear_label": "Blood is clear",
         "reset_label": "Empty the glass",

         # The three verdict states (page lines 474–477). The middle one is
         # the lesson: every route gives the same number of hours.
         "verdicts": {
             "empty": "Nothing drunk, nothing to clear.",
             "clear": "Clear — after {n} hour{s}, which is exactly the number "
                      "of units. Every route you tried gave the same number of "
                      "hours, because the liver sets the rate and nothing else "
                      "has a vote.",
             "running": "{r} unit{s} still in the blood after {h} hour{s}. "
                        "Reactions, coordination and judgement are still "
                        "affected, whatever the person says about feeling "
                        "fine."}},

        # #s-years — the band panel. Rail stop 3, mirroring `s-clock`; see the
        # docstring. `rule` is the component: band ground, 3px ink border, an accent-text
        # eyebrow and a display statement, then a card grid — Design's markup
        # (page lines 156–175) with the row lists folded into the glosses.
        {"type": "rule", "anchor": "s-years",
         "eyebrow": "Not one night — years of nights",
         "statement": "Each one damages a different set of organs.",
         "cards": LONG_TERM_CARDS},

        # Design nests this inside `#s-years`; `r_rule` has no nested slot, so
        # it renders directly under the panel in document order. See "What
        # could not be lifted" 2.
        {"type": "key-fact", "ref": "two-drugs-two-mechanisms"},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "DRUG-03"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "two-drugs-two-mechanisms",
         "text": "Alcohol is a depressant: it slows the nervous system, and "
                 "the liver clears it at about one unit an hour whatever "
                 "anyone does. Nicotine is a stimulant and is what makes "
                 "smoking hard to stop; carbon monoxide in the same smoke "
                 "takes the places oxygen should occupy in the blood.",
         "placement": "top-level",
         "ground": "band",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO drawn quotes in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`, and an authored statement wins over the register
        # (which matters here: the second quote is a conjunction and no single
        # register entry says it). The block asks for no commitment, on
        # Design's page and here, so it is not a rail stop and emits no
        # completion contract.
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "DRUG-03",
         "statements": [
             {"quote": "Coffee, a cold shower or fresh air will sober you up.",
              "body": ["Alcohol leaves the body almost entirely through the "
                       "liver, which breaks it down at a rate set by how much "
                       "enzyme it contains — about one unit an hour, and that "
                       "rate does not respond to encouragement. Cold water on "
                       "the skin does not reach the liver. Breathing harder "
                       "does not either, because only a trace leaves through "
                       "the lungs, which is precisely why a breath test can "
                       "measure what is in the blood. Coffee is the dangerous "
                       "one, because it works on a different organ: caffeine "
                       "is a stimulant and makes the person feel awake, so the "
                       "outward signs of being drunk fade while the impairment "
                       "is untouched. Someone who feels capable and is not is "
                       "more likely to drive than someone who feels terrible. "
                       "The only variable that matters is time, and a large "
                       "evening does not fit inside a night's sleep: six units "
                       "finished at midnight are not cleared until around six "
                       "in the morning."]},
             # ⚑ Two beliefs in one drawn quote — DRUG-04 and DRUG-08. The
             # closing sentence is where b4-04 is named in words; its link is
             # the `references` edge, not markup here. See "What could not be
             # lifted" 3.
             {"quote": "A few cigarettes now and then is basically fine, and "
                       "filters make them safer.",
              "body": ["There is no threshold below which smoke stops damaging "
                       "tissue — the risk rises from the first cigarette, and "
                       "social smokers develop dependence too, because "
                       "nicotine's grip is about how quickly it reaches the "
                       "brain rather than how many are smoked in a week. The "
                       "filter is the more interesting half of the claim. It "
                       "removes some tar, and it was introduced when the link "
                       "with cancer became public, but it does nothing to "
                       "carbon monoxide, and by making the smoke smoother it "
                       "encourages deeper inhaling. Ventilation holes in the "
                       "paper also inflate the tar figures measured by "
                       "machines above what a human hand covering the filter "
                       "actually receives. So a filter changes the taste, "
                       "changes the number in the test, and does not make the "
                       "habit safe. What smoke does to the airways and to the "
                       "alveoli themselves is the subject of Exercise, asthma "
                       "and smoking."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⚖️ MRB-177 LENGTH PARITY — MEASURED, AND BOTH MARKED RUNGS PASS.
    #   rung 1: correct 5w against distractors of 9 / 6 / 8 — the correct
    #           option is the SHORTEST, so length cannot give it away.
    #   rung 2: correct 11w against distractors of 11 / 5 / 8 — joint longest,
    #           not strictly longest, so `length_tell` does not fire and a
    #           student counting words learns nothing.
    # No distractor was rewritten, because there was nothing to repair.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Read the clock",
            "q": "Someone drinks six units, finishing at midnight. Roughly "
                 "when is the alcohol cleared from their blood?",
            "options": [
                "About six in the morning",
                "Within an hour or two, since alcohol is absorbed quickly",
                "As soon as they fall asleep",
                "It depends whether they drink water and coffee",
            ],
            "answer": 0,
            "feedback": {
                1: "Absorbed quickly, cleared slowly. Getting in is fast; "
                   "getting out runs at one unit an hour.",
                2: "Sleep passes time and nothing more. The liver works at the "
                   "same rate whether they are asleep or awake.",
                3: "Neither changes the rate. Water helps the headache, coffee "
                   "helps them feel awake, and the clock is unmoved by both.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A drunk person drinks two strong black coffees. What has "
                 "changed?",
            "options": [
                "The alcohol is broken down faster, so they sober up sooner",
                "They feel more awake, and are exactly as impaired as before",
                "Nothing at all has changed",
                "Their reactions improve because caffeine is a stimulant",
            ],
            "answer": 1,
            "feedback": {
                0: "Caffeine acts on the brain and heart, not on the liver "
                   "enzymes that break alcohol down. The rate is unchanged.",
                2: "Something has — and it is the dangerous half. Feeling "
                   "capable while still impaired is worse than feeling as bad "
                   "as you are.",
                3: "A stimulant raises alertness; it does not undo a "
                   "depressant. The two drugs are both in the blood at once, "
                   "and the impairment stays.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the carbon monoxide",
            "q": "A smoker gets out of breath climbing stairs sooner than a "
                 "non-smoker of the same fitness, even before any lung damage "
                 "has developed. Explain why, using what the blood carries.",
            "field_label": "Your explanation",
            "placeholder": "Carbon monoxide in the smoke…",
            "success": [
                "Says carbon monoxide is in the smoke and is absorbed into the "
                "blood.",
                "Says it binds to haemoglobin in the red blood cells, in the "
                "places oxygen would occupy.",
                "Says it holds on, so those places are unavailable for oxygen.",
                "Says less oxygen therefore reaches the working muscles.",
                "Concludes the muscles cannot respire aerobically as fast, so "
                "the person is out of breath sooner — without any lung damage "
                "being needed to explain it.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "An energy drink is advertised as a mixer for spirits, and "
                 "someone claims it \"keeps you sober because caffeine cancels "
                 "out alcohol\". Judge the claim using the two drug classes, "
                 "say what actually happens to the person, and explain why "
                 "this combination is more dangerous than the alcohol alone.",
            "field_label": "Your answer",
            "placeholder": "Alcohol is a depressant and caffeine is a "
                           "stimulant…",
            "success": [
                "Identifies alcohol as a depressant and caffeine as a "
                "stimulant.",
                "Says the two act on different things, so neither cancels the "
                "other — both drugs are in the blood doing their own job.",
                "Says the liver still clears alcohol at about one unit an "
                "hour, so the person is as impaired as the units say.",
                "Says the caffeine hides the tiredness, so the person does not "
                "feel drunk and keeps drinking or takes risks they otherwise "
                "would not.",
                "Concludes that masking the signs of impairment without "
                "removing the impairment is what makes the mixture more "
                "dangerous.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Alcohol is a depressant. It slows nerve signals, so "
                "reactions, coordination and judgement all worsen, and only "
                "the liver removes it — at about one unit an hour, whatever "
                "anyone tries. Long term it scars the liver and damages the "
                "brain. In tobacco smoke, nicotine is the stimulant that makes "
                "stopping hard, carbon monoxide takes oxygen's place in the "
                "blood, and tar and the other substances damage the airways.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    #
    # ⚑⚑ THE VAPE PARAGRAPH. NOTES-B6 flag 9, APPROVED BY MIDE 16 Aug 2026,
    # SHIPS EXACTLY AS WRITTEN. One string, lifted whole from page line 278,
    # both `<em>` spans included. Seven load-bearing clauses, balanced as a
    # whole — no tar, no carbon monoxide, dependence the same or stronger,
    # very likely less harmful than cigarettes, NOT KNOWN TO BE SAFE, nothing
    # to gain for someone who has never smoked, illegal to sell to under-18s.
    # Trimming any one of them tips the paragraph into advertisement or into
    # scare copy. Do not edit, reorder, shorten or annotate it.
    "stretch": [
        {"type": "explainer", "id": "vapes-and-what-is-not-known",
         "text": "A vape has no tar and no carbon monoxide, because nothing is "
                 "burned — so a smoker who switches removes two of the three "
                 "harms in the list above. It still delivers nicotine, often "
                 "faster and in larger amounts than a cigarette, so the "
                 "dependence is the same or stronger, and a person who has "
                 "never smoked gains nothing at all and takes on the "
                 "dependence for nothing. The honest position is the one a "
                 "scientist has to be comfortable with: vapes are very likely "
                 "less harmful than cigarettes and are not known to be safe, "
                 "because the long-term studies do not exist yet — the devices "
                 "are too new for anyone to have used one for forty years. "
                 "Selling either to under-18s is illegal in the UK. This is a "
                 "good example of a question where the evidence is genuinely "
                 "incomplete and where <em>less harmful than the worst "
                 "option</em> and <em>harmless</em> are miles apart."},
    ],

    # ── the support layer (§5.6) ────────────────────────────────────────────
    #
    # ⚠️ The referral block, carried as drawn. It names no national service:
    # Design points at "the services listed in your school's PSHE materials"
    # because a named helpline in a lesson page goes stale and naming one is a
    # safeguarding decision rather than an authoring one (NOTES-B6 §1).
    # Mide may override; an author may not.
    #
    # ⊕ `support_heading` (MRB-244, PAYLOAD-SCHEMA §0) carries Design's own
    # eyebrow. It landed mid-authoring; before it, `r_layer`'s support heading
    # was fixed at the call site as "Need a hand?", and this page would have
    # offered a student living with someone else's drinking help with their
    # homework. The two headings are not interchangeable in register, so this
    # is a content fix and not a cosmetic one.
    "support_heading": "If any of this is about you or someone you know",
    "support": [
        {"type": "explainer", "id": "where-to-take-this",
         "text": "This lesson covers the biology only. Pressure from friends, "
                 "family drinking, and what the law says belong in your PSHE "
                 "and RSE lessons, and they are worth raising there. If "
                 "something here is about your own home or your own habits, "
                 "talk to a trusted adult, the school nurse, a pharmacist or a "
                 "GP — stopping smoking in particular is one of the few things "
                 "where free NHS help genuinely doubles the success rate. Your "
                 "school's PSHE materials list the national confidential "
                 "services by name."},
    ],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to work out why the liver's rate cannot be "
                      "hurried?",
              "cta": "Ask about this lesson",
              "anchor": "s-clock"},

    # ⊕ MRB-228's `convention_note`, not `safety_note` — see "What could not be
    # lifted" 5. Design draws ONE plain `.ks3-legal` paragraph and this is it:
    # a statement of what the model ignores, ending in a limit on what the
    # model may be used for. Small, at the bottom edge, never a callout (§8.10).
    "convention_note": "The clock is a simplified model: one unit an hour, "
                       "cleared in whole hours, ignoring body mass, sex, "
                       "medication, food already eaten and how quickly the "
                       "drinks were finished. Real clearance varies between "
                       "people and is slower, not faster, than this model when "
                       "the liver is already damaged. It is a teaching model "
                       "and must not be used to judge whether anyone is fit to "
                       "drive.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is a claim under test: six interventions people believe in,
    # every one of them run against the same clock, and the finding is a null
    # result the student produces themselves.
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
