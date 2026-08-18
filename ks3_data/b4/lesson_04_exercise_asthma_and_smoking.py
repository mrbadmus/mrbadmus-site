"""B4 L4 — Exercise, asthma and smoking (SYSTEM).

Authored against Design's approved page,
`docs/ks3/design-reference/b4/b4-04-exercise-asthma-and-smoking.dc.html` (578 lines), under
the MRB-220 build contract and MRB-244.

Every student-facing string is lifted byte-identical from the approved page
except the four listed under "What could not be lifted", none of which is a
sentence of science, and the `vocabulary` definitions, which reach a student
only as the unit page's chips and are worded so nothing on the page
contradicts them.

── TONE IS A GATE ON THIS PAGE, AND IT IS NOT THE AUTHOR'S TO ADJUST ────

NOTES-B4.md flag 13 asks Mide to review this lesson's tone with the same
weight as its science, and to read it against B6 (the drugs unit) so the two
do not diverge. Some students reading this page have asthma; some have a
parent who smokes.

The register on the page is therefore **lifted, not edited**. Nothing is
softened, nothing is sharpened, no warning is added, and no line of scare copy,
no dose and no threshold appears anywhere — because none appears on Design's
page. The three places the tone actually lives are all Design's own words:

  * the asthma factor's `Reversible?` row, which states the reliever relaxes
    airway muscle and that an attack which does not respond to it is a medical
    emergency — a fact, in the same voice as the other two factors' rows;
  * the nicotine card, which says nicotine is "the substance that makes
    stopping physically difficult, which is why stopping is a medical matter
    and not simply a decision" — the one line in the lesson that refuses to
    treat smoking as a choice, and it is stated as mechanism;
  * `safety_note`, below.

The single judgement call is recorded under "What could not be lifted" 4. It
is a punctuation join inside a card and it changes no word.

⚠️ THE MEDICAL DISCLAIMER IS LOAD-BEARING AND IS NOT TRIMMED. Design's
`.ks3-legal` line carries three separate things — this is not medical advice,
follow your own asthma plan, treat a reliever that is not working as an
emergency — plus where to go for help stopping smoking. It is carried whole,
as `safety_note`, which §4.8.1 D renders small at the bottom edge alongside
the standing legal line. §8.10 bars it from being promoted to a callout, and
it is not one here. b3-04 is the precedent and took the same treatment for the
same reason.

── The flagship: `system-switch` run BACKWARDS ──────────────────────────

`#s-bench` is `fault-bench`, on `ks3-block ks3-dark ks3-practical` (page line
104), so `practical` is measured and not inherited. NOTES-B4 §2 describes it
as the B2 `system-switch` idiom inverted: instead of switching a part off and
being told the symptom, the student is given a symptom and must **locate**
which part is at fault. Same anatomy of reasoning, opposite direction.

⚖️ THE THREE FACTORS ACT ON THREE DIFFERENT PARTS OF ONE SYSTEM, and that is
the lesson rather than a property of the data. Exercise → the breathing
muscles. Asthma → the airways. Smoking → the alveoli (and the airways and the
blood as well). The four part options are the SAME every time, which is the
only reason locating is a decision at all — an implementation that let the
three blur into "three things that are bad for your lungs" would have kept the
content and lost the lesson. Design's own lede says so out loud: *"The four
options are the same every time, and only one of the three factors hits the
same part twice."*

The reveal is never withheld for a wrong answer. `verdicts.wrong` is *"Not the
part you chose"* and the answer prints underneath it either way — the bench
locates a fault, it does not mark the student. Only the ladder marks.

── FOUR rail stops — Design's fourth restored (MRB-249) ─────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that
`#s-smoke` came off the rail. Design draws FOUR stops and `#s-smoke` ticks on
`Object.keys(s.opened).length >= 3` (page line 419) — the BENCH's predicate,
verbatim, one section to the right — and because `#s-smoke` is an eyebrow, a
display statement, four static cards and a KEY FACT, with no control, no commit
and no field, the reading was that MRB-208's completion rule left nothing in it
to complete and that inventing a demand Design did not draw is closed to this
build. So the lesson shipped THREE stops.

Two things overrule that inference.

MRB-205 was cited for half of itself. Design draws, we render: it forbids
inventing a control, and it equally forbids dropping a stop Design drew. Page
wins over engine.

And Design's `isDone()` states the tick condition rather than leaving it to be
inferred. It is a rail-level function returning the identical expression for
`#s-bench` and then for `#s-smoke`. The four substances are the payoff of
having located the fault; the section holds no control because the bench has
already taken the student's commitment. That is a MIRROR, resolved at rail
level in `wireRail`'s `paint()`.

So the fourth stop is declared: anchor `s-smoke`, `mirrors: "s-bench"`,
`done_when: "three_factors_opened"` — the bench's own predicate, named as
borrowed, and gated by `check_rail_matches_design` against
`docs/ks3/rail-manifest.md`. b3-02's `#s-limits`, b3-01's `#s-nutrients`,
b3-07's `#s-four` and c1-02's `#s-matrix` are restored the same way. The
section keeps its anchor, as it always did.

And NOTES-B4 §6 — "Rail stops: four in every lesson" — turns out to have been
the plain instruction it looked like. The old passage read it down to a count
of what Design drew rather than a requirement on what we build. It is both.

── What could not be lifted, and why ────────────────────────────────────

1. **The "Next in this unit" card merges into "Connects to".** Design draws
   both (page lines 283–295); `r_endmatter` has three slots and the first is
   headed "Before this lesson" and fed by `requires`, a BACKWARD edge. Putting
   `stomata-and-gas-exchange-in-plants` there would print a forward pointer
   under "Before this lesson" and add a false edge to the progression graph.
   So the forward pointer becomes the first `references` entry and the card
   heading is what is given up. b3-01, b3-05 and b3-07 resolve the identical
   split the identical way. `requires` is EMPTY, which is also what the page
   says: it draws no "Before this lesson" card.

2. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card
   is authored prose and §4.8.1 D makes the two mutually exclusive.

3. **The KEY FACT box leaves Design's band panel.** She nests it inside
   `#s-smoke`; `r_rule` has no nested key-fact slot (only `r_comparison`
   does), so it renders as its own top-level block directly under the panel.
   `ground: "card"` because Design draws it on `--ks3-card` inside a
   `--ks3-band` section and band on band would be invisible. The words and the
   order are unchanged. b3-02 and b3-04 hit this first.

4. ⚠️ **The smoke cards' `where` line folds into the gloss.** Design's card is
   THREE parts — the substance name in display 800, WHERE IT ACTS in mono
   uppercase accent, then the body — and `r_rule`'s card is two, `term` and
   `gloss`. b3-02 hit this and DROPPED its third field, correctly: its tag was
   the same string on all three cards and the statement above already said it.
   **Here it is the opposite case and dropping is not available.** The four
   `where` values differ — Airways and alveoli / The blood / Blood vessels and
   heart / Airways — and naming which part each substance hits is the same
   teaching point the bench is built on. So `where` and `what` are JOINED with
   a full stop and a space, both strings byte-identical, `where` first because
   that is where Design puts it. This is the one judgement call in the tone
   treatment and it changes no word.

   The fix, if the card is to win, is the same `tag` key b3-02 already asked
   for. This is the second unit to need it and the first where the field is
   load-bearing science rather than a repeated label.

⚑ For Mide's science gate — NOTES-B4 §4 flags open on this lesson, all
  authored as delivered:
  * flag 9 — *"halve the radius and flow drops around sixteenfold"* is
    Poiseuille's fourth power stated as a bare factor with no law named. It is
    doing real work in both the asthma factor's `Why it matters so much` row
    and the second think-again.
  * flag 10 — carbon monoxide binding haemoglobin ~200× more strongly, and
    *"a heavy smoker may have a tenth of their haemoglobin unavailable"*.
  * flag 11 — breathing rate driven by carbon dioxide and not oxygen, stated
    flat, in the exercise factor's `What triggers it` row, the first
    think-again and ladder rung 1. The oxygen answer is what most students and
    some textbooks say, and rung 1's distractor 0 is exactly it.
  * flag 12 — emphysema as alveolar walls broken down by enzymes released
    during chronic inflammation, volume preserved and area lost, plus the
    reversibility table: cilia over months, carbon monoxide within a day,
    alveolar walls never.
  * flag 13 — the tone. See the top of this docstring.
  * flag 14 — Doll and Hill, including Doll giving up two years into his own
    study. It is the stretch layer.

⚑ Figures: NONE. This page's `.ks3-legal` line names no figure slot — the
  only one in the unit is `b4-gas-exchange-labelled`, named in b4-01's legal
  line and owned there. Nothing is invented to fill a slot this page does not
  have, so `figures` is present and empty.
"""

# ── the four parts, one list, shared by every factor (page lines 326–331) ──
#
# ⚖️ IDENTICAL FOR ALL THREE FACTORS, and that is the instrument. If the
# options changed per factor the student would be reading the options for the
# answer instead of locating a fault. `factors[].part` is checked against these
# ids by the renderer, which raises on a factor whose answer is not on the list.
PARTS = [
    {"id": "muscles",
     "text": "The breathing muscles — diaphragm and intercostals"},
    {"id": "airways",
     "text": "The airways — bronchi and bronchioles"},
    {"id": "alveoli",
     "text": "The alveoli — the exchange surface itself"},
    {"id": "blood",
     "text": "The blood — what carries the oxygen away"},
]

# ── the three factors (page lines 333–364) ──────────────────────────────
#
# ⚠️ Design's row keys are `k` / `v`; the schema's are `label` / `text`
# (docs/ks3/b4-inventory/PAYLOAD-SCHEMA.md §4). The KEYS are renamed, the
# VALUES are byte-identical.
FACTORS = [
    {"id": "exercise",
     "label": "Exercise",
     "tag": "Factor 1 · during and after hard exercise",
     "scenario": "Someone runs 400 metres flat out. Their breathing rate rises "
                 "from about 14 breaths a minute to over 40, and each breath "
                 "is far deeper. They keep breathing hard for several minutes "
                 "after stopping.",
     "part": "muscles",
     "answer": "The breathing muscles — working harder and faster.",
     "rows": [
         {"label": "What actually changes",
          "text": "The diaphragm and intercostal muscles contract more "
                  "forcefully and more often. Nothing about the airways, the "
                  "alveoli or the blood is altered."},
         # ⚑ NOTES-B4 flag 11 lives in this row.
         {"label": "What triggers it",
          "text": "Rising carbon dioxide in the blood, detected in the brain "
                  "stem. Not a shortage of oxygen — the body monitors the "
                  "waste product, not the fuel."},
         {"label": "Effect on gas exchange",
          "text": "Alveolar air is refreshed more often, so the concentration "
                  "difference across the alveolar wall stays steeper and more "
                  "oxygen diffuses per second."},
         {"label": "Reversible?",
          "text": "Completely, within minutes. The continued hard breathing "
                  "after stopping is clearing the carbon dioxide backlog."},
     ]},
    {"id": "asthma",
     "label": "Asthma attack",
     "tag": "Factor 2 · during an asthma attack",
     # "A pupil with asthma" is Design's own wording and carries no year or
     # half-term, so the sequence-is-data rule is satisfied as drawn.
     "scenario": "A pupil with asthma starts wheezing on a cold morning. "
                 "Breathing out is harder than breathing in, there is a tight "
                 "feeling in the chest, and a blue reliever inhaler helps "
                 "within minutes.",
     "part": "airways",
     "answer": "The airways — narrowed bronchioles.",
     "rows": [
         {"label": "What actually changes",
          "text": "Three things at once: muscle in the bronchiole walls "
                  "contracts, the lining swells, and extra mucus is produced. "
                  "All three reduce the diameter of the tube."},
         # ⚑ NOTES-B4 flag 9 lives in this row.
         {"label": "Why it matters so much",
          "text": "Flow through a tube depends steeply on its radius — halve "
                  "the radius and flow drops around sixteenfold. A modest "
                  "narrowing has a dramatic effect."},
         {"label": "Effect on gas exchange",
          "text": "The alveoli are undamaged and the blood is fine. Not enough "
                  "air is reaching the exchange surface, which is a delivery "
                  "problem, not an exchange problem."},
         # ⚖️ One half of the medical disclaimer, in the body rather than the
         # legal line, and in the same voice as the other two factors'
         # `Reversible?` rows. Not a callout, not amber, not louder.
         {"label": "Reversible?",
          "text": "Yes, with treatment. A reliever inhaler relaxes the airway "
                  "muscle. An attack that does not respond to it is a medical "
                  "emergency."},
     ]},
    {"id": "smoking",
     "label": "Long-term smoking",
     "tag": "Factor 3 · after years of smoking",
     "scenario": "An adult who has smoked for twenty-five years is breathless "
                 "walking uphill, coughs most mornings, and a lung function "
                 "test shows reduced gas transfer that does not improve with "
                 "an inhaler.",
     # ⚖️ The one factor that hits more than one part — which is why Design's
     # lede warns that only one of the three hits the same part twice, and why
     # the answer names the alveoli FIRST and the other two after.
     "part": "alveoli",
     "answer": "The alveoli — and the airways and the blood as well.",
     "rows": [
         # ⚑ NOTES-B4 flag 12 lives in this row and the last one.
         {"label": "What actually changes",
          "text": "Alveolar walls are broken down, merging many small alveoli "
                  "into fewer large ones. The volume is similar; the surface "
                  "area is not. This is emphysema."},
         {"label": "And elsewhere",
          "text": "Cilia are paralysed and destroyed, so mucus must be coughed "
                  "out instead of swept out — the morning cough. Carbon "
                  "monoxide occupies haemoglobin, so the blood carries less "
                  "oxygen."},
         {"label": "Effect on gas exchange",
          "text": "Less surface, so less exchange per second, and less "
                  "carrying capacity in the blood arriving. Two of the four "
                  "requirements from the last lesson are damaged at once."},
         {"label": "Reversible?",
          "text": "The cilia recover over months after stopping and the carbon "
                  "monoxide clears within a day. The lost alveolar walls do "
                  "not grow back — that part is permanent."},
     ]},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 117 character for character.
    "slug":        "exercise-asthma-and-smoking",
    "title":       "Exercise, asthma and smoking",
    "discipline":  "biology",
    "unit":        "breathing-and-gas-exchange",
    "family":      "SYSTEM",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.GAS.03` is owned WHOLE by this lesson — NOTES-B4 §1. It is not
    # split and it is not shared; GAS.01 is the only compound bullet in the
    # unit and it splits across lessons 1 and 3.
    "covers":      ["KS3.B.GAS.03"],
    "touches":     ["KS3.B.GAS.01"],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2},
                    {"id": "structure-function", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 50,

    # ── progression edges ───────────────────────────────────────────────────
    # EMPTY, and deliberately: Design draws no "Before this lesson" card on
    # this page. See "What could not be lifted" 1.
    "requires":    [],
    "assumes":     [],
    # First entry is Design's "Next in this unit"; the rest are her "Connects
    # to", in her order.
    "references":  ["stomata-and-gas-exchange-in-plants",
                    "alveoli-built-for-exchange",
                    {"unit": "B2", "lesson": "antagonistic-muscle-pairs",
                     "label": "Antagonistic muscle pairs",
                     "why": "Where the diaphragm and intercostals' pulling — "
                            "and only pulling — is the whole subject."}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Risk factors for non-communicable disease, correlation and "
                   "cause, and the effect of exercise on respiration.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Three things that change how well you breathe, and they "
                    "act on three different parts of the system. Naming which "
                    "part is most of the answer.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them and as NOTES-B4 §6 requires. `s-smoke`
    # is the third: no control of its own, so it mirrors `s-bench` and ticks on
    # the bench's predicate — see the docstring. `short` and `label` are
    # Design's own strings (page lines 318–324).
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "The inhaler",
         "done_when": "committed"},
        # Design's own threshold, kept: ALL THREE factors opened, not one. A
        # stop that ticked on the first would call the bench finished having
        # located one fault out of three, which is precisely the comparison the
        # section exists to make.
        {"anchor": "s-bench",  "short": "LOCATE", "label": "Locate the fault",
         "done_when": "three_factors_opened"},
        {"anchor": "s-smoke", "short": "SMOKE", "label": "Four substances",
         "mirrors": "s-bench", "done_when": "three_factors_opened"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3). Option A is
    # BREATH-10 stated as a choice, which is how the lesson elicits it before
    # `#s-think` confronts it.
    "phenomenon": {
        "kind": "narrative",
        "title": "An asthma inhaler works in a room full of perfectly good "
                 "air.",
        "prompt": "Someone having an asthma attack is standing outdoors. The "
                  "air around them is 21% oxygen, the same as everyone "
                  "else's. They cannot get enough of it. A puff from a blue "
                  "inhaler helps within minutes, and it contains no oxygen at "
                  "all.",
        "commit": "If the air is fine, what has gone wrong?",
        "options": [
            "The oxygen in the air around them has dropped",
            "Their alveoli have stopped working",
            "The tubes carrying air to the alveoli have narrowed",
            "Their diaphragm has stopped contracting",
        ],
        "reveal": "The route in has narrowed. Muscle in the walls of the "
                  "bronchioles has contracted, the lining has swollen and "
                  "produced extra mucus, and air cannot get through fast "
                  "enough — with 21% oxygen sitting right outside the mouth. "
                  "The inhaler relaxes that muscle. Nothing about the air "
                  "needed fixing.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    #
    # ⚠️ The `BREATH` family is NOT in `docs/ks3/misconception-register.md`.
    # NOTES-B4 §5 says thirteen entries were written into it; they are not
    # there, exactly as `DIET` was not there for B3. The commander maintains
    # the register centrally, so these are MINTED HERE and reported, with
    # NOTES' own numbering preserved so five parallel authors do not collide.
    #
    # ⚠️ The numbering assumes b4-03 ends at BREATH-07, which is the one thing
    # NOTES states outright (§5: "BREATH-06/BREATH-07 are PART-10/PART-11 for
    # the third time") together with b4-05 owning 12 and 13. This lesson
    # therefore opens at 08. Three are minted, not four: three is the number of
    # wrong ideas Design NAMES on the page, each as its own `.ks3-mis-quote`.
    #
    # ⚑ A FOURTH is arguable and is left for the commander rather than taken
    # here — *breathing rate is driven by falling oxygen*. NOTES-B4 flag 11
    # treats it as a first-class item of this lesson, and rung 1's distractor 0
    # is exactly it, but Design quotes it nowhere as a belief sentence, so
    # minting it would mean authoring a statement rather than lifting one.
    #
    # Each `statement` is Design's own `.ks3-mis-quote` without its quote
    # marks — `_quoted()` adds them.
    "misconceptions": [
        {"id": "BREATH-09",
         "statement": "Being out of breath means your lungs cannot hold enough "
                      "air.",
         # The exercise factor elicits it: a student locating a breathlessness
         # scenario reaches for the lungs, and the bench makes them say which
         # part before it answers.
         "elicited_by": "locate-the-fault",
         "confronted_by": "think-what-changed"},
        {"id": "BREATH-10",
         "statement": "During an asthma attack there is not enough oxygen in "
                      "the air.",
         # Hook option A, verbatim as a belief.
         "elicited_by": "hook",
         "confronted_by": "think-what-changed"},
        {"id": "BREATH-11",
         "statement": "Tar is the harmful part of cigarette smoke.",
         "elicited_by": "locate-the-fault",
         "confronted_by": "think-what-changed"},
    ],

    # Design draws no keyword block anywhere in B4, so these never reach the
    # lesson body. They DO reach a student, as the unit page's "Words this unit
    # gives you" chips, and the reading-age gate reads them as its exclusion
    # list — which matters here, because "bronchiole", "haemoglobin",
    # "emphysema" and "cilia" would otherwise all count against the page.
    # Worded so nothing in the lesson contradicts them, and with no dose, no
    # threshold and no advice in any of them.
    "vocabulary": [
        {"term": "bronchiole",
         "definition": "One of the smallest air tubes in the lung, with muscle "
                       "in its wall that can narrow it.",
         "note": "Flow through a tube depends steeply on its radius, so a "
                 "small narrowing matters a great deal."},
        {"term": "asthma",
         "definition": "A condition in which the bronchioles narrow — the "
                       "muscle contracting, the lining swelling and extra "
                       "mucus being produced.",
         "note": "The air is unchanged. What has changed is the route to the "
                 "alveoli."},
        {"term": "reliever inhaler",
         "definition": "A puff of a drug that relaxes the muscle in the airway "
                       "wall, so the tube widens and air can flow again.",
         "note": "It contains no oxygen, because oxygen was never what was "
                 "missing."},
        {"term": "cilia",
         "definition": "Tiny moving hairs on the airway lining that sweep "
                       "mucus up and out of the lungs.",
         "note": "Paralysed cilia leave coughing as the only way to clear "
                 "mucus."},
        {"term": "carbon monoxide",
         "definition": "A gas that binds to haemoglobin far more strongly than "
                       "oxygen does and does not readily let go.",
         "note": "It takes red blood cells out of service, which is a "
                 "circulation problem rather than a lung one."},
        {"term": "emphysema",
         "definition": "Damage in which alveolar walls break down, merging "
                       "many small alveoli into fewer large ones.",
         "note": "Volume stays similar; surface area does not, and the walls "
                 "do not grow back."},
    ],

    # This page's legal line names no figure slot — the unit's only one,
    # `b4-gas-exchange-labelled`, is named in b4-01's legal line and owned
    # there. Present and empty, never absent.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b4/__init__.py::_normalise. Design's block is
        # `ks3-block ks3-dark ks3-practical` (page line 104), so `practical` is
        # measured and not inherited from a neighbour.
        #
        # Payload authored against docs/ks3/b4-inventory/PAYLOAD-SCHEMA.md §4.
        {"type": "fault-bench", "id": "locate-the-fault", "anchor": "s-bench",
         "demand": "predict",
         "targets": "BREATH-09",
         "eyebrow": "Locate the fault · three factors",
         "heading": "Which part of the system does each one hit?",
         "head_counter": {"format": "{n} of 3 opened", "total": 3},
         "prompt": "Commit to a part of the system before opening each one. "
                   "The four options are the same every time, and only one of "
                   "the three factors hits the same part twice.",

         "parts": PARTS,
         "question": "Which part of the system is affected?",
         "factors": FACTORS,
         "start_factor": "exercise",

         "open_label": "Show what happens",
         "hints": {"none": "choose a part first",
                   "ready": "ready",
                   "opened": "opened"},
         # ⚖️ The reveal is NOT withheld for a wrong answer. The verdict says
         # which happened and the answer prints either way — this bench locates
         # a fault, it does not mark a student. Only the ladder marks.
         "verdicts": {"right": "You located it",
                      "wrong": "Not the part you chose"},
         "rail_after": 3},

        # #s-smoke — the band panel. Rail stop 3, mirroring `s-bench`; see the
        # docstring. `rule` is the component: band ground, 3px ink border, an accent-text
        # eyebrow and a display statement, then a card grid — Design's markup
        # (page lines 158–171) with the third card field folded into the gloss.
        {"type": "rule", "anchor": "s-smoke",
         "eyebrow": "Four substances, four different damages",
         "statement": "Cigarette smoke is not one thing doing one thing.",
         # ⚠️ `term` is Design's `name`; `gloss` is her `where` and her `what`
         # joined with ". ", both byte-identical, `where` first. See "What
         # could not be lifted" 4 — the location is the teaching point and
         # cannot be dropped the way b3-02 dropped its repeated tag.
         "cards": [
             {"term": "Tar",
              "gloss": "Airways and alveoli. A sticky mixture containing "
                       "carcinogens. It coats the airway lining, paralyses "
                       "and then destroys cilia, and its irritation drives "
                       "the chronic inflammation that damages alveolar "
                       "walls."},
             {"term": "Carbon monoxide",
              "gloss": "The blood. Binds to haemoglobin about 200 times more "
                       "strongly than oxygen and does not readily let go, "
                       "taking red blood cells out of service. This is a "
                       "circulation effect and it happens immediately, not "
                       "after decades."},
             # ⚖️ The tone-bearing card. Nicotine dependence is stated as the
             # reason stopping is medical rather than a decision. Lifted; not
             # softened and not sharpened.
             {"term": "Nicotine",
              "gloss": "Blood vessels and heart. Narrows blood vessels and "
                       "raises heart rate and blood pressure. It is also the "
                       "substance that makes stopping physically difficult, "
                       "which is why stopping is a medical matter and not "
                       "simply a decision."},
             {"term": "Particulates and heat",
              "gloss": "Airways. Irritate the lining directly, increasing "
                       "mucus production while the cilia that would clear it "
                       "are being disabled. The result is mucus accumulating "
                       "with no way out except coughing."},
         ]},

        # Design nests this inside `#s-smoke`; `r_rule` has no nested slot, so
        # it renders directly under the panel in document order. See "What
        # could not be lifted" 3.
        {"type": "key-fact", "ref": "three-factors-three-parts"},

        {"type": "misconception", "id": "think-what-changed",
         "anchor": "s-think", "targets": "BREATH-09"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # `ground: "card"` because Design draws it on `--ks3-card` with a 2px ink
    # outline and the accent offset shadow, sitting inside a `--ks3-band`
    # section — band on band would be invisible.
    "key_facts": [
        {"id": "three-factors-three-parts",
         "text": "Exercise changes how fast you ventilate and is fully "
                 "reversible. An asthma attack narrows the airways and is "
                 "reversible with treatment. Smoking damages the cilia, the "
                 "alveolar walls and the blood, and the alveolar damage is "
                 "permanent.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # One entry. The instrument is authored inline in `core` and lifted here by
    # `ks3_data/b4/__init__.py::_normalise`, which leaves the `practical` shell
    # behind it.
    "activities": [
        # Design draws THREE wrong ideas in one "Think again", the second and
        # third behind an amber-topped divider (page lines 178–195).
        # `statements` carries all three with their bodies, and
        # `r_confrontation` draws the dividers.
        #
        # ⚖️ NOT a rail stop and NOT `predict`. MRB-220 R1 makes `#s-think` a
        # stop in B2, C1 and C2 because on those pages it asks for a
        # commitment; on this page it is static markup with no options and no
        # gate, which is B1's case. `confrontation` emits no `data-stage-done`
        # and Design's own RAIL excludes it.
        {"id": "think-what-changed",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "BREATH-09",
         "statements": [
             {"quote": "Being out of breath means your lungs cannot hold "
                       "enough air.",
              "body": [
                  "Lung capacity is almost never the limit. During hard "
                  "exercise your muscles are respiring far faster, producing "
                  "far more carbon dioxide, and it is the <em>carbon "
                  "dioxide</em> in your blood that your brain measures and "
                  "responds to — not a shortage of oxygen and not the size of "
                  "your lungs. That is why holding your breath becomes "
                  "unbearable long before your blood oxygen has fallen "
                  "dangerously, and why breathing hard after a sprint "
                  "continues after you have stopped running: there is a "
                  "backlog of carbon dioxide to clear. Trained athletes do not "
                  "generally have much larger lungs than untrained people; "
                  "what they have is a heart, a circulation and a set of "
                  "muscles that use oxygen better once it arrives."]},
             # ⚖️ The second half of the medical disclaimer, in Design's own
             # sentence and in the body rather than in a callout: the correct
             # first response is the inhaler and, if it does not work,
             # emergency help. §8.10 keeps it here and in `safety_note`, and
             # out of any louder treatment.
             {"quote": "During an asthma attack there is not enough oxygen in "
                       "the air.",
              "body": [
                  "The air is unchanged — 21% oxygen, exactly as it was a "
                  "minute earlier. What has changed is the diameter of the "
                  "bronchioles, and a small change in diameter has a very "
                  "large effect on flow: halving the radius of a tube reduces "
                  "the flow through it by about a factor of sixteen. That is "
                  "why an attack can go from mild to serious quickly, why a "
                  "blue inhaler containing a muscle relaxant helps rather "
                  "than an oxygen cylinder, and why the correct first "
                  "response is the inhaler and, if it does not work, "
                  "emergency help. Handing someone oxygen while their airway "
                  "is shut solves nothing."]},
             {"quote": "Tar is the harmful part of cigarette smoke.",
              "body": [
                  "Tar is one of at least four separate problems, and it is "
                  "not the one that acts fastest. Carbon monoxide binds to "
                  "haemoglobin roughly 200 times more strongly than oxygen "
                  "does, so it takes red blood cells out of service "
                  "immediately — a heavy smoker may have a tenth of their "
                  "haemoglobin unavailable at any moment, which is a "
                  "circulation problem rather than a lung one. Nicotine "
                  "narrows blood vessels and raises heart rate. The heat and "
                  "irritants paralyse and destroy the cilia, so mucus is no "
                  "longer swept out and has to be coughed instead. And the "
                  "enzymes released during the resulting chronic inflammation "
                  "break down alveolar walls, merging many small alveoli into "
                  "few large ones and destroying exchange surface that never "
                  "grows back. Four mechanisms, four organs affected, one of "
                  "them irreversible."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⚖️ MRB-177 LENGTH PARITY — MEASURED, AND BOTH MARKED RUNGS PASS.
    #   rung 1: correct 5w against distractors of 5 / 4 / 6 — the correct
    #           option is neither longest nor shortest, and it is tied with
    #           distractor 0, which is the one it has to be indistinguishable
    #           from because distractor 0 IS the misconception.
    #   rung 2: correct 3w against distractors of 4 / 2 / 3 — likewise tied,
    #           and not the longest.
    # No distractor was rewritten, because there was nothing to repair.
    "ladder": {
        "recall": {
            "title": "Rung 1 · What drives faster breathing",
            "q": "What does your body actually detect that makes you breathe "
                 "faster during exercise?",
            "options": [
                "Falling oxygen in the blood",
                "Rising carbon dioxide in the blood",
                "The lungs becoming empty",
                "Muscles signalling that they are tired",
            ],
            "answer": 1,
            "feedback": {
                0: "Blood oxygen changes remarkably little during ordinary "
                   "exercise. The body monitors the waste product instead — "
                   "it is a far more sensitive early signal.",
                2: "Lung volume is not what is sensed. Nothing measures how "
                   "full the lungs are in order to set the rate.",
                3: "Breathing rate rises before any tiredness, and stays "
                   "raised after you stop. It tracks a blood chemical, not "
                   "muscle fatigue.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Which of these effects of smoking is permanent?",
            "options": [
                "Carbon monoxide occupying haemoglobin",
                "Paralysed cilia",
                "Destroyed alveolar walls",
                "Extra mucus production",
            ],
            "answer": 2,
            "feedback": {
                0: "This clears within about a day of the last cigarette. It "
                   "is serious and it is not permanent.",
                1: "Cilia recover over weeks to months after stopping — which "
                   "is why a smoker’s cough often gets temporarily worse "
                   "first, as clearance restarts.",
                3: "This reduces once the irritation stops. The irreversible "
                   "loss is structural.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the inhaler",
            "q": "Explain why a reliever inhaler helps during an asthma attack "
                 "even though it contains no oxygen, and why giving someone "
                 "oxygen instead would not fix the underlying problem.",
            "field_label": "Your explanation",
            "placeholder": "The inhaler works because…",
            "success": [
                "Says the air already contains 21% oxygen, so the air is not "
                "the problem.",
                "Identifies the problem as narrowed bronchioles — muscle "
                "contraction, swelling and mucus.",
                "Says the inhaler relaxes the airway muscle, widening the tube "
                "so air can flow again.",
                "Explains that oxygen cannot help much if air cannot reach the "
                "alveoli in the first place.",
                "Notes that an attack not responding to a reliever needs "
                "emergency help.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A patient with emphysema has almost normal lung volume but "
                 "greatly reduced gas transfer. Explain how both can be true, "
                 "using what you learnt about alveoli, and say which of the "
                 "four requirements for a good exchange surface has been lost.",
            "field_label": "Your answer",
            "placeholder": "The volume is normal because…",
            "success": [
                "Says alveolar walls have broken down, merging small alveoli "
                "into fewer larger ones.",
                "Explains that this keeps total volume similar while reducing "
                "total surface area sharply.",
                "Identifies large surface area as the requirement that has "
                "been lost.",
                "Connects this back to the hook of the alveoli lesson — the "
                "patient has moved partway towards the smooth bag.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Exercise raises breathing rate and depth, triggered by rising "
                "carbon dioxide, and is fully reversible. Asthma narrows the "
                "bronchioles through muscle contraction, swelling and mucus, "
                "and is treated by relaxing that muscle. Smoking paralyses and "
                "destroys cilia, introduces carbon monoxide that occupies "
                "haemoglobin, and destroys alveolar walls — reducing exchange "
                "surface permanently.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B4 flag 14. It is a lesson in how science establishes a cause
    # without an experiment, and the smoking is the case study rather than the
    # subject — which is also why it belongs in GOING FURTHER and not in the
    # body.
    "stretch": [
        {"type": "explainer", "id": "how-the-link-was-established",
         "text": "The link between smoking and lung cancer was established "
                 "without any experiment on humans, which is a genuinely "
                 "interesting problem in how science proves things. Richard "
                 "Doll and Austin Bradford Hill began by surveying hospital "
                 "patients in 1950, then followed 40 000 British doctors for "
                 "decades — watching who smoked, who stopped, and who died of "
                 "what. Correlation alone is never proof, so the case was "
                 "built from several independent strands: the risk rose with "
                 "the number smoked, fell when people stopped, appeared in "
                 "every country studied, and had a mechanism identifiable in "
                 "the chemistry of tar. Doll himself smoked when the study "
                 "began and gave up two years in, on his own evidence. That "
                 "is what changing your mind in response to data actually "
                 "looks like, and it is rarer than it should be."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to check which part of the system each factor "
                      "affects?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⚠️ THE MEDICAL DISCLAIMER. Design's `.ks3-legal` line (page line 307),
    # carried whole and unabridged: not medical advice, does not replace an
    # asthma plan, follow the plan your doctor or nurse gave you, treat a
    # failing reliever as an emergency, and where to start for help stopping
    # smoking. §4.8.1 D renders it small at the bottom edge alongside the
    # standing legal line; §8.10 keeps it out of any callout treatment. Not one
    # clause of it is trimmed.
    "safety_note": "This lesson describes the biology of asthma and of "
                   "smoking. It is not medical advice and does not replace an "
                   "asthma plan: if you have asthma, follow the plan your "
                   "doctor or nurse gave you, and treat a reliever inhaler "
                   "that is not working as an emergency. For help stopping "
                   "smoking, a GP or pharmacist is the right place to start.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
