"""B4 L2 — How breathing works (MODEL).

Authored against Design's approved page,
`KS3 B4 lessons/b4-02-how-breathing-works.dc.html` (581 lines), under the
MRB-220 build contract, with the instrument payload authored against
`docs/ks3/b4-inventory/PAYLOAD-SCHEMA.md` §2 (the engine pass's own contract —
it existed by the time this record reached the instrument, so `r_bell_jar` was
not reverse-engineered).

Every student-facing string is lifted byte-identical from the approved page
except the items listed under "What could not be lifted", none of which is a
sentence of science.

── ⚑ THE STATUTORY GAP IS RULED, AND IT IS NOT CLOSED HERE ──────────────

`KS3.B.GAS.02` reads *"the mechanism of breathing to move air in and out of the
lungs, using a pressure model to explain the movement of gases, including
simple measurements of lung volume"*. This page delivers the mechanism and the
pressure model in full. It delivers **no measurement**: the bell jar is a
pressure model with volume READOUTS, and a student reads them rather than
taking them. NOTES-B4 flag 1 raises it and recommends a fifth section.

Ruled on 16 Aug 2026 (MRB-244): **build what is on disk.** Inventing a
displacement-jar or spirometer section would be a component Design did not draw
(MRB-205), and this record does not invent one. `covers` claims `GAS.02` WHOLE
and unnarrowed, so the statutory register reads *covered, with a gap* rather
than *covered* — the full argument is in `ks3_data/b4/__init__.py` and
`ks3_data/biology_b4_breathing.py`.

── The flagship: the CHAIN is the instrument, not the picture ───────────

`#s-model` is `bell-jar`, on `ks3-block ks3-dark ks3-practical` (page line 111),
lifted into `activities[]` by `ks3_data/b4/__init__.py::_normalise`.

⚖️ THE FOUR-STEP CHAIN CARRIES THE LESSON AND EVERY LINE OF IT IS AUTHORED.
Design's note is explicit and it is a build instruction, not a flourish: the
FIRST line of every phase is the muscle and the LAST line is the air. That
ordering is the entire confrontation of `BREATH-05` — a student who believes
the air is the cause reads three lines before the air is mentioned, in all
three phases, every time they move the slider. Twelve lines are authored below,
four per phase, and the schema raises on any phase that does not carry exactly
four. If the chain ever degrades to static text the lesson's central argument
is gone and nothing else on the page replaces it.

The slider is the only control that changes state; `Breathe in` and `Breathe
out` are presets onto the same slider, which is why they are `presets[]` and
not a second instrument.

── FOUR rail stops — Design's fourth restored (MRB-249) ─────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that
`#s-limits` came off the rail. Design draws FOUR stops and `#s-limits` ticks on
`s.moved` (page line 405) — `#s-model`'s predicate, character for character,
one section to the left — and because `#s-limits` is an eyebrow, a display
statement, four static cards, a key fact and a prose panel, with no control, no
commitment and no field, the reading was that MRB-208 forbade the stop and
`ks3_parity.check_rail_reachable` would fail it for carrying none of the
signals `doneByDom()` reads. So the lesson shipped THREE stops.

Two things overrule that inference.

MRB-205 binds and is not re-argued: Design draws, we render; nothing invented,
nothing dropped; page wins over engine.

And `s.moved` written twice is Design stating the tick condition, not Design
duplicating by accident. `isDone()` is rail-level and returns the identical
expression for `#s-model` and then for `#s-limits`. Where the bell jar fails is
the payoff of having moved the diaphragm: the section carries no control
because the model already took the student's commitment. That is a MIRROR,
resolved at rail level in `wireRail`'s `paint()`.

So the fourth stop is declared: anchor `s-limits`, `mirrors: "s-model"`,
`done_when: "diaphragm_moved"` — the model's own predicate, named as borrowed,
and gated by `check_rail_matches_design` against `docs/ks3/rail-manifest.md`.
c1-02's `#s-matrix`, c1-05's `#s-scale`, b3-02's own `#s-limits`, b3-01's
`#s-nutrients` and b3-07's `#s-four` are restored the same way. The section
keeps its anchor, as it always did, so every hash link into it still works.

── ⚑ THE P5 FORWARD REFERENCE, AND WHAT WAS DONE ABOUT IT ───────────────

The page carries a visible "Leans on · Physics" panel (line 190) whose prose
names **P5 *Pressure***, which is not authored and has no slug on disk. A
forward reference to an unauthored unit has failed builds before, so:

* **No `references` edge to P5 was created.** The dependency is editorial, not
  structural — NOTES-B4 §6 says so in as many words ("There is no code
  dependency on P5 — nothing imported, nothing shared"). An edge would need a
  lesson slug that does not exist, and `KNOWN_FORWARD` in the validator exists
  because that failure is silent until it is not.
* **The panel's words are kept in full, P5 included**, as prose inside an
  `explainer`. `references` carries exactly the two edges Design drew in her
  own end matter — C1 `gas-pressure` and C1 `testing-the-model`.
* When P5 *is* authored, re-read that paragraph rather than assuming it is
  still right. That is NOTES-B4 §6's instruction and it survives this build.

── What could not be lifted, and why ────────────────────────────────────

1. **The three inline `<a href>`s.** Design links `Testing the model` in the
   limits lede, `Gas pressure` in the leans-on panel and `Diffusion` in the
   third confrontation. `rich()` allows `<em>` and `<strong>` and nothing else
   — an anchor renders as visible tag soup — so the WORDS are unchanged and the
   hyperlinks are dropped. Two of the three destinations survive as `references`
   edges, which is where the engine puts cross-lesson navigation. **Diffusion
   was deliberately NOT added as a third edge**: Design draws two links in her
   end matter and a third card link is a navigation component she did not draw
   (MRB-205). b3-07 resolved the identical case the same way, and its Diffusion
   edge was already drawn in its own end matter.

2. **The limits cards' TAGS.** Design's card is four parts — a mono accent tag
   ("Wrong 1"), the name in display 700, what it gets wrong, then a ruled-off
   "Still worth having because:" line. `r_rule`'s card is `term` + `gloss`. Tag
   and name are joined with Design's own middle-dot idiom (the same joiner in
   "Breathing and gas exchange · Model" and "The bell-jar model · work the
   diaphragm"), and the worth line joins the paragraph above it keeping
   Design's own `<strong>`. Every string survives and nothing is invented.
   Same resolution as b3-07's feature cards.

3. **The limits lede moves below the cards.** Design puts "A model that got
   everything right would be a chest…" between the statement and the card grid;
   `r_rule` has eyebrow / statement / cards / close and no slot between
   statement and cards. It is authored as `close`, so it reads as the panel's
   payoff rather than its lede. Words unchanged, order within the block moved.

4. **The key fact leaves Design's band panel.** She nests it inside `#s-limits`;
   `r_rule` has no nested key-fact slot (only `r_comparison` does), so it
   renders as its own top-level block directly under the panel, on the band
   ground every other top-level key fact in the key stage takes. Words and
   order unchanged. Same as b3-02.

5. **The "Leans on · Physics" panel loses its dashed inset and its eyebrow
   treatment.** §5.1.1's block vocabulary is CLOSED and `explainer` is the only
   prose block in it; there is no aside/inset component and inventing one is
   MRB-205's exact prohibition. The eyebrow's WORDS are kept as a `<strong>`
   lead-in on the paragraph — Design's own idiom, as in "Still worth having
   because:" — at the cost of one added full stop. That full stop is the only
   punctuation in this record that is not Design's.

6. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose and §4.8.1 D makes the two mutually exclusive.

── Design decisions corrected ──────────────────────────────────────────

**One, and it is a rendered double negative, not a science change.** Design's
`in` chain reads *"pressure falls to " + pressure.toFixed(2) + " kPa below
atmospheric"* (page line 457) with a SIGNED pressure, so at any breathing-in
setting it prints *"falls to -0.79 kPa below atmospheric"*. The `out` chain
already uses the magnitude (line 462). PAYLOAD-SCHEMA §2 offers both
`{pressure}` and `{pressure_abs}`, takes no view, and flags the drawn page as
defective here — so the `in` chain below takes `{pressure_abs}`. **No word
changes**; one numeral loses a minus sign it should never have carried. ⚑ For
Mide: this is the only place this record differs from what the reference screen
renders.

⚑ For Mide's science gate:
  * NOTES-B4 flag 8 — **pneumothorax is the hook**. A puncture wound collapsing
    an undamaged lung with a clear airway. It is authored as delivered because
    it is the cleanest evidence in the topic that a lung does not inflate
    itself. Design asks you to confirm you want an injury as a hook and that
    the phrasing does not read as first-aid instruction; it describes a
    mechanism and instructs nobody to do anything.
  * NOTES-B4 flag 1 — the lung-volume measurement gap, above. Ruled, recorded,
    not closed.
  * The pressure figures are illustrative and say so in the page's own foot
    line, which ships as `convention_note` — the plain legal treatment, not the
    `ks3-safety` one. There is no safety line on this lesson: nothing is heated,
    handled or tasted, and borrowing the safety treatment for a units caveat
    devalues it on the lessons that need it (MRB-228's convention-line ruling).
"""

# ── the four model limits (page lines 344–357) ──────────────────────────
#
# ⚠️ `term` is authored as Design's tag and name joined with her own middle
# dot; `gloss` is her `wrong` paragraph joined to her `worth` line behind her
# own `<strong>` lead-in. Both are compositions of delivered strings, done here
# at authoring time rather than by a transformation in the browser, and no
# word is added or removed. See "What could not be lifted" 2.
LIMITS = [
    {"term": "Wrong 1 · No ribs, no intercostal muscles",
     "gloss": "The jar is rigid, so the only thing that can move is the base. "
              "In you, the ribs swing up and out at the same time, and the "
              "intercostal muscles supply roughly a third of quiet breathing. "
              "<strong>Still worth having because:</strong> It isolates one "
              "variable. Seeing what the diaphragm alone does is easier than "
              "seeing two muscle groups act at once."},
    {"term": "Wrong 2 · Balloons are bags, not alveoli",
     "gloss": "A balloon has one smooth inner surface. A lung ends in 500 "
              "million alveoli, which is the entire reason gas exchange can "
              "happen fast enough to keep you alive. "
              "<strong>Still worth having because:</strong> This model is not "
              "about exchange — it is about ventilation. The next lesson takes "
              "the alveoli seriously."},
    {"term": "Wrong 3 · A flat sheet, not a dome",
     "gloss": "The rubber sheet is pulled down into a cone. A real diaphragm "
              "is a dome at rest and <em>flattens</em> when it contracts — so "
              "it moves down by flattening, not by being pulled. "
              "<strong>Still worth having because:</strong> The direction of "
              "movement and its effect on volume are still right, which is "
              "what the model is for."},
    {"term": "Wrong 4 · Nothing is alive",
     "gloss": "The jar has no elastic recoil to speak of, no surfactant "
              "keeping the alveoli from sticking shut, no nerves, and nothing "
              "regulating the rate. "
              "<strong>Still worth having because:</strong> A model with all "
              "of that in it would be a chest, and you could not see inside "
              "it."},
]

# ── the instrument's three phases (page lines 453–524) ──────────────────
#
# ⚖️ THE FIRST LINE IS ALWAYS THE MUSCLE AND THE LAST LINE IS ALWAYS THE AIR,
# in all three phases. That is the instrument. `{volume}` and `{pressure_abs}`
# are filled by the engine at one and two decimal places respectively
# (PAYLOAD-SCHEMA §2); nothing else in a chain line is computed.
#
# ⚠️ `in` takes `{pressure_abs}`, not Design's signed `{pressure}` — the
# sentence carries "below atmospheric" in words and the signed value makes it a
# double negative. See "Design decisions corrected".
#
# ⚠️ `in` and `out` share one `note`, which is Design's own arrangement (she
# authors one moving-state note and shows it in both). It is repeated rather
# than referenced because the schema takes a string per phase.
_MOVING_NOTE = ("Read the list downwards. The muscles are the cause, the "
                "pressure difference is the mechanism, and the air moving is "
                "the result — never the other way round.")

PHASES = {
    "in": {
        "phase_label": "Diaphragm contracted — breathing in",
        "dia_label": "contracted, flattened",
        "air": "inwards",
        "chain": [
            "Diaphragm contracts and flattens; intercostals lift the ribs.",
            "Chest volume increases — now {volume} litres.",
            "The same air fills a bigger space, so pressure falls to "
            "{pressure_abs} kPa below atmospheric.",
            "Air moves in, from higher pressure outside to lower pressure "
            "inside.",
        ],
        "note": _MOVING_NOTE},
    "out": {
        "phase_label": "Diaphragm relaxed — breathing out",
        "dia_label": "relaxed, domed up",
        "air": "outwards",
        "chain": [
            "Diaphragm relaxes and domes upwards; ribs drop.",
            "Chest volume decreases — now {volume} litres.",
            "The same air fills a smaller space, so pressure rises to "
            "{pressure_abs} kPa above atmospheric.",
            "Air moves out, from higher pressure inside to lower pressure "
            "outside.",
        ],
        "note": _MOVING_NOTE},
    "rest": {
        "phase_label": "At rest between breaths",
        "dia_label": "resting position",
        "air": "none",
        "chain": [
            "Diaphragm at rest, domed upwards.",
            "Chest volume steady at {volume} litres.",
            "Pressure inside equals atmospheric.",
            "No net air movement in either direction.",
        ],
        "note": "Move the diaphragm and this list fills in with real numbers. "
                "Notice which line changes first."},
}

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 115 character for character.
    "slug":        "how-breathing-works",
    "title":       "How breathing works",
    "discipline":  "biology",
    "unit":        "breathing-and-gas-exchange",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # ⚑ Owned WHOLE and deliberately unnarrowed — see the docstring. The
    # measurement clause is not delivered and narrowing the claim would hide
    # that from every gate that reads the register.
    "covers":      ["KS3.B.GAS.02"],
    # The particle account of pressure is borrowed, not taught: the leans-on
    # panel restates C1's rule and rung 4 puts it under water.
    "touches":     ["KS3.C.PNM.01"],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2},
                    {"id": "particles", "level": 2},
                    {"id": "structure-function", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # ⚑ NO P5 EDGE. The leans-on panel names Physics P5 in prose; P5 is not
    # authored and has no slug. The dependency is editorial and stays prose —
    # see the docstring.
    "requires":    ["the-gas-exchange-system"],
    "assumes":     [],
    "references":  [{"unit": "C1", "lesson": "gas-pressure",
                     "label": "Gas pressure",
                     "why": "Where the rule this lesson borrows is derived: "
                            "the same particles in a bigger space collide with "
                            "the walls less often."},
                    {"unit": "C1", "lesson": "testing-the-model",
                     "label": "Testing the model",
                     "why": "Where knowing exactly where a model stops being "
                            "true is the point, rather than an admission."}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Ventilation, lung volumes and spirometer traces, with "
                   "pressure and volume treated quantitatively.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Your lungs contain no muscle at all. They cannot pull air "
                    "in, and they never have. Something else moves, and the "
                    "air follows.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-limits` is the third: no control of
    # its own, so it mirrors `s-model` and ticks on the model's predicate — see
    # the docstring. `short` and `label` are Design's own strings (page lines
    # 336–342).
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "Collapsed lung",
         "done_when": "committed"},
        # Design's own threshold, kept: any movement of the diaphragm. There is
        # nothing to complete beyond working the model, and a count would
        # invent a demand she did not draw.
        {"anchor": "s-model",  "short": "MODEL",  "label": "Bell jar",
         "done_when": "diaphragm_moved"},
        {"anchor": "s-limits", "short": "LIMITS", "label": "Model limits",
         "mirrors": "s-model", "done_when": "diaphragm_moved"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3).
    "phenomenon": {
        "kind": "narrative",
        "title": "A puncture wound between two ribs, and the lung collapses.",
        "prompt": "A narrow wound opens the space between the chest wall and "
                  "the lung to the outside air. Nothing has touched the lung "
                  "itself — it is undamaged, and the airway is completely "
                  "clear. Within seconds that lung has emptied and will not "
                  "reinflate.",
        "commit": "Nothing is blocking it. Why can it not fill?",
        "options": [
            "The wound is letting air escape faster than it can go in",
            "The lung needs the pressure around it to be lower than the air "
            "inside it",
            "The lung muscles have been cut",
            "Blood has filled the alveoli",
        ],
        "reveal": "Because a lung has never inflated itself. It is filled by "
                  "being at a lower pressure than the outside air, and that "
                  "difference is produced by muscles enlarging the chest. Let "
                  "air into the space around the lung and the difference "
                  "vanishes — the lung is intact, the airway is clear, and it "
                  "still cannot fill.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ The `BREATH` family is minted by this unit and is NOT yet in
    # `docs/ks3/misconception-register.md` — the commander maintains that file
    # centrally, and these three ids are reported for it. NOTES-B4 §5 mints
    # thirteen across five lessons and pins `BREATH-06`/`07` to
    # `alveoli-built-for-exchange` and `BREATH-12`/`13` to
    # `stomata-and-gas-exchange-in-plants`, so 03–05 is this lesson's share and
    # leaves 01–02 to `the-gas-exchange-system`.
    #
    # All three are elicited by the instrument rather than by a separate
    # commitment: the chain's ordering is what makes each belief visibly wrong
    # while the student is holding the slider, which is Law 4's requirement met
    # by the component Design drew rather than by one added for the purpose.
    "misconceptions": [
        {"id": "BREATH-04",
         "statement": "The lungs expand and pull the air in.",
         "elicited_by": "work-the-diaphragm",
         "confronted_by": "think-what-moves-first"},
        {"id": "BREATH-05",
         "statement": "Air rushes in, and that is what makes the chest get "
                      "bigger.",
         "elicited_by": "work-the-diaphragm",
         "confronted_by": "think-what-moves-first"},
        {"id": "BREATH-14",
         "statement": "Something sucks the air in.",
         "elicited_by": "work-the-diaphragm",
         "confronted_by": "think-what-moves-first"},
    ],

    # Design draws no keyword block anywhere in B4, so these never reach the
    # lesson body. The TERMS reach a student as the unit page's chips, and the
    # reading-age gate reads them as its exclusion list — which matters here,
    # because "diaphragm", "intercostal" and "atmospheric" would otherwise all
    # count against the page.
    "vocabulary": [
        {"term": "diaphragm",
         "definition": "The sheet of muscle under the lungs. It is domed at "
                       "rest and flattens when it contracts.",
         "note": "Flattening it makes the chest bigger, which is where a "
                 "breath starts."},
        {"term": "intercostal muscles",
         "definition": "The muscles between the ribs, which swing the ribs up "
                       "and out.",
         "note": "About a third of quiet breathing."},
        {"term": "ventilation",
         "definition": "Moving air in and out of the lungs.",
         "note": "Not the same as respiration, which happens inside cells."},
        {"term": "atmospheric pressure",
         "definition": "The pressure of the air around you, from its particles "
                       "colliding with every surface.",
         "note": "Every breath you take is the atmosphere doing the pushing."},
        {"term": "elastic recoil",
         "definition": "A stretched tissue returning to its resting size on "
                       "its own.",
         "note": "This is what pushes most quiet breaths back out."},
    ],

    # Design's page names no figure slot — the foot line is a units caveat, not
    # a diagram reference, and there is no diagram anywhere on the page. NOTES
    # flag 20's `b4-gas-exchange-labelled` belongs to `the-gas-exchange-system`
    # and is that lesson's to declare. Nothing is invented to fill a slot.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-model — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b4/__init__.py::_normalise. Design's block is
        # `ks3-block ks3-dark ks3-practical` (page line 111), so `practical` is
        # measured, not inherited.
        #
        # Payload keys and their values follow PAYLOAD-SCHEMA.md §2 exactly.
        # The four numbers in `model` are Design's own (page lines 442–443):
        # volume = 2.2 + 3.3 × dia/100 litres, pressure = −(dia/100 − 0.2) ×
        # 1.1 kPa. `pressure_zero` must equal `rest`/100 or the renderer raises
        # — 0.2 and 20 are the same statement about where atmospheric sits.
        {"type": "bell-jar", "id": "work-the-diaphragm", "anchor": "s-model",
         "demand": "investigate",
         "eyebrow": "The bell-jar model · work the diaphragm",
         "heading": "Pull the sheet down and read the pressure",
         "prompt": "A sealed jar, a rubber sheet across the bottom, and a "
                   "balloon on a tube through the lid. Move the sheet and "
                   "watch the order in which things change.",
         "head_counter": {"off": "not moved yet", "on": "model worked"},

         "start": 20,
         "rest": 20,
         "model": {"volume_base": 2.2, "volume_span": 3.3,
                   "pressure_zero": 0.2, "pressure_span": 1.1},

         "jar_label": "The jar",
         "readouts_label": "Readouts",
         "slider_label": "Diaphragm",
         "slider_aria": "Diaphragm position",
         "chain_label": "The order of events",

         # ⚠️ `outside_value` is FIXED and never computed. Atmospheric pressure
         # is the reference the whole model is quoted against, and a student
         # who sees both numbers move has been shown two variables where the
         # science has one.
         "readouts": {
             "volume_label": "Chest volume",
             "volume_format": "{volume} L",
             "pressure_label": "Pressure inside",
             "pressure_format": "{pressure} kPa",
             "outside_label": "Pressure outside",
             "outside_value": "0.00 kPa (atmospheric)",
             "air_label": "Air movement"},

         "presets": [{"id": "in", "label": "Breathe in", "value": 92},
                     {"id": "out", "label": "Breathe out", "value": 4}],

         "phases": PHASES},

        # #s-limits — the band panel. Rail stop 3, mirroring `s-model`; see
        # the docstring. `close` carries Design's lede, which `r_rule` can only place after
        # the cards.
        {"type": "rule", "anchor": "s-limits",
         "eyebrow": "Where the model fails",
         "statement": "Four things the bell jar gets wrong, and why it is "
                      "still the right model.",
         "cards": LIMITS,
         "close": "A model that got everything right would be a chest. "
                  "Knowing precisely where a model stops being true is what "
                  "makes it usable — the same argument as in Testing the "
                  "model."},

        # Design nests this inside `#s-limits`; `r_rule` has no nested slot, so
        # it renders directly under the panel in document order. See "What
        # could not be lifted" 4.
        {"type": "key-fact", "ref": "volume-first-air-last"},

        # The "Leans on · Physics" panel. Prose is the only block §5.1.1 has
        # for it — see "What could not be lifted" 5. P5 is named here and
        # nowhere in the edges.
        {"type": "explainer", "id": "leans-on-physics",
         "text": "<strong>Leans on · Physics.</strong> The pressure reasoning "
                 "here is the same as in Gas pressure: pressure comes from "
                 "particles colliding with the walls, so the same number of "
                 "particles in a bigger space collide less often and the "
                 "pressure falls. Physics P5 <em>Pressure</em> owns the full "
                 "quantitative treatment; this lesson uses only the "
                 "qualitative rule, and nothing here needs to be unlearnt when "
                 "you meet it."},

        {"type": "misconception", "id": "think-what-moves-first",
         "anchor": "s-think", "targets": "BREATH-04"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "volume-first-air-last",
         "text": "Muscles change the volume of the chest. Changing the volume "
                 "changes the pressure. Air then moves from higher pressure to "
                 "lower pressure. Volume first, pressure second, air last — "
                 "always in that order.",
         "placement": "top-level",
         "ground": "band",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # THREE wrong ideas in one "Think again" block, each behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`, and an authored statement wins over the register.
        # The block asks for no commitment, on Design's page and here, so it is
        # not a rail stop and emits no completion contract.
        #
        # ⚠️ The three inline links are dropped and every word is kept; see
        # "What could not be lifted" 1.
        {"id": "think-what-moves-first",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "BREATH-04",
         "statements": [
             {"quote": "The lungs expand and pull the air in.",
              "body": ["The lungs have no muscle tissue anywhere in them, so "
                       "there is nothing in a lung that could pull. They are "
                       "elastic bags that are stretched by the space around "
                       "them growing, in the way a plastic bag pressed against "
                       "the inside of a widening box is stretched by the box. "
                       "The muscles that do the work are the diaphragm "
                       "underneath and the intercostals between the ribs, and "
                       "neither of them is part of a lung. This is not a "
                       "technicality: it is the whole explanation of the "
                       "collapsed lung in the hook, of why a ventilator has to "
                       "push rather than persuade, and of why paralysis of the "
                       "diaphragm stops breathing while leaving perfectly "
                       "healthy lungs in place."]},
             {"quote": "Air rushes in, and that is what makes the chest get "
                       "bigger.",
              "body": ["This gets the causation exactly backwards, and it is "
                       "the most common wrong answer in the topic. Watch the "
                       "readouts on the model: the volume changes <em>first</em>, "
                       "the pressure changes <em>because</em> of it, and the "
                       "air moves <em>last</em>, in response. Nothing about "
                       "incoming air can enlarge a chest — if it could, you "
                       "would inflate when the wind blew. The test that "
                       "settles it is the sealed jar: clamp the tube so no air "
                       "can enter, pull the sheet down, and the volume still "
                       "increases and the pressure still falls. The chest "
                       "moving is the cause; the air arriving is the "
                       "consequence."]},
             {"quote": "Something sucks the air in.",
              "body": ["Sucking is not a thing that exists. There is no force "
                       "that reaches out and draws air towards a low pressure; "
                       "there is only air at higher pressure being pushed by "
                       "its own particles into a space where fewer particles "
                       "are pushing back. The atmosphere does all the work of "
                       "every breath you take, and your muscles only ever make "
                       "room for it. This matters for the same reason it "
                       "mattered in Diffusion — describing a pressure "
                       "difference as a pull invents a mechanism that is not "
                       "there, and then you cannot explain why a straw stops "
                       "working at the top of a very tall glass."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⚖️ MRB-177 LENGTH PARITY — MEASURED, AND BOTH MARKED RUNGS PASS.
    #   rung 1: correct 10w against distractors of 10 / 10 / 7 — the correct
    #           option ties the longest, ratio 1.0.
    #   rung 2: correct 13w against distractors of 10 / 10 / 9 — ratio 1.3,
    #           under the 1.4 threshold.
    # No distractor was rewritten, because there was nothing to repair.
    #
    # ⚠️ The arrows in rung 1 are U+2192 and are in TEXT nodes only (question
    # and option labels), which `t()` renders as the drawn `.ks3-mark` glyph.
    # No `feedback` string carries one: feedback is emitted into a
    # `data-feedback` attribute, where an SVG would terminate the attribute.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Get the order right",
            "q": "Put these in the order they happen when you breathe in.",
            "options": [
                "Muscles contract → chest volume increases → pressure falls → "
                "air moves in",
                "Air moves in → chest volume increases → muscles contract → "
                "pressure falls",
                "Pressure falls → muscles contract → air moves in → chest "
                "volume increases",
                "Lungs expand → air moves in → muscles contract",
            ],
            "answer": 0,
            "feedback": {
                1: "This has the air as the cause. Clamp the tube on the model "
                   "so no air can enter: the volume still increases and the "
                   "pressure still falls.",
                2: "Nothing can make the pressure fall before the volume "
                   "changes. The muscles are always first.",
                3: "The lungs contain no muscle and cannot expand themselves. "
                   "They are stretched by the space around them growing.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "You seal the tube on the bell-jar model so no air can get in "
                 "or out, then pull the rubber sheet down. What happens?",
            "options": [
                "Nothing at all — without air movement there is no change",
                "The volume increases and the pressure inside falls; the "
                "balloon does not inflate",
                "The balloon inflates anyway, using the air already in it",
                "The pressure rises because the sheet is being stretched",
            ],
            "answer": 1,
            "feedback": {
                0: "The sheet still moves and the space still enlarges. "
                   "Something must change, and it is the pressure.",
                2: "The air already inside is what is being spread over a "
                   "larger volume — that is why the pressure falls. There is "
                   "nothing extra to inflate it with.",
                3: "Same number of particles in a larger space means fewer "
                   "collisions per second with the walls, so the pressure "
                   "falls. Stretching the rubber is irrelevant to the gas.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the collapsed lung",
            "q": "Explain why a small wound between the ribs can collapse an "
                 "undamaged lung with a clear airway. Use the words volume, "
                 "pressure and diaphragm, and say why enlarging the chest no "
                 "longer helps.",
            "field_label": "Your explanation",
            "placeholder": "The lung collapses because…",
            "success": [
                "States that a lung is inflated by being at lower pressure "
                "than the outside air, not by its own effort.",
                "Says the wound lets air into the space around the lung, "
                "equalising the pressure across its surface.",
                "Explains that enlarging the chest now draws air through the "
                "wound instead of through the airway.",
                "Says the lung and airway are both undamaged, so the failure "
                "is in the pressure difference, not the structure.",
                "Names the diaphragm and intercostals as the muscles doing the "
                "work, and notes the lung has none.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A snorkel 2 m long is used to breathe while lying on the "
                 "bottom of a pool. Explain, using pressure, why this is far "
                 "harder than snorkelling at the surface — and why the "
                 "difficulty is about the chest rather than the tube.",
            "field_label": "Your answer",
            "placeholder": "At 2 m deep the water pressure on the chest is…",
            "success": [
                "Says water pressure squeezes the chest from outside, and that "
                "pressure increases with depth.",
                "Says the air at the top of the snorkel is still at "
                "atmospheric pressure.",
                "Explains that the muscles must now work against the water "
                "pressure to enlarge the chest at all.",
                "Concludes the tube is not the problem — the pressure "
                "difference the muscles must overcome is.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Breathing in: the diaphragm contracts and flattens, the "
                "intercostal muscles contract and lift the ribs up and out, "
                "chest volume increases, pressure inside falls below "
                "atmospheric, and air moves in. Breathing out reverses it, "
                "mostly by the muscles relaxing and the chest recoiling "
                "elastically. Volume changes first; air moves last.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    "stretch": [
        {"type": "explainer", "id": "the-iron-lung",
         "text": "The iron lungs used during polio epidemics worked on exactly "
                 "the principle this lesson describes, and worked on the "
                 "outside of the patient. The machine sealed the body from the "
                 "neck down and cycled the pressure in the tank: drop it, and "
                 "the patient's chest expands because the outside pressure is "
                 "now lower than the pressure in their airway, so air flows in "
                 "through the mouth. No tube, no pushing, nothing entering the "
                 "body — the ventilator enlarged the chest and let the "
                 "atmosphere do the rest. Modern ventilators reverse the "
                 "geometry and push air in under positive pressure through a "
                 "tube, which is more practical and, unlike the iron lung, is "
                 "not how a healthy person breathes at all."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to check you have the order of events the right "
                      "way round?",
              "cta": "Ask about this lesson",
              "anchor": "s-model"},

    # ⚠️ NOT `safety_note`. Design's foot line is a units convention — what the
    # model's kilopascals are quoted against and how far they are from a real
    # chest — and `safety_note` ships `class="ks3-safety"`, the treatment
    # reserved for "never light a candle without an adult". MRB-228 added
    # `convention_note` for exactly this line's shape.
    "convention_note": "Pressure values on the model are illustrative, in "
                       "kilopascals relative to an atmosphere of about 101 "
                       "kPa. Real intrapulmonary pressure swings during quiet "
                       "breathing are under 1 kPa.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
