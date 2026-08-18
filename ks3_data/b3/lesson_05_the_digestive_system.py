"""B3 L5 — The digestive system (SYSTEM).

Authored against Claude Design's approved page,
`KS3 B3 lessons/b3-05-the-digestive-system.dc.html` (571 lines), and its
author's notes, `KS3 B3 lessons/NOTES-B3.md`. Every student-facing string is
lifted byte-identical from the approved page except where this docstring says
otherwise, and every exception is here.

── This lesson owns the TISSUES-AND-ORGANS clause ───────────────────────

`KS3.B.NUT.04` is a compound bullet:

    "the tissues and organs of the human digestive system, including
     adaptations to function and how the digestive system digests food
     (enzymes simply as biological catalysts)"

Three clauses, three lessons, at exactly the grain the unit is written at —
which is what `ks3_data/substatements.py` rule 3 (mint lazily, per unit, at
authoring time) exists for. This lesson owns the first: the organs, what each
one does, and in what order.

⚠️ `KS3.B.NUT.04a` IS NOT YET IN `ks3_data/substatements.py`. The unit wrapper
`ks3_data/biology_b3_nutrition.py` already names the three-way split and the
letters (a = tissues and organs, b = enzymes as catalysts, c = adaptations to
function), so the mapping is settled; what is missing is the SUBSTATEMENTS
entry, and it spans this lesson, b3-06 and b3-07. Nothing in the build depends
on it — `check_statutory` only fires when a sub-ID is registered AND its parent
is also owned — so this ships correct and the minting is one edit across three
lessons, not three edits. **Flagged rather than done here, because a shared
file written from one of three parallel lessons is how two of them get lost.**

⚑ Also flagged: strictly, the bullet PRINTS "adaptations to function" before
"how the digestive system digests food", so clause order would make
adaptations `b` and enzymes `c`. The wrapper's letters are followed rather than
re-derived from one file — but the discrepancy is real and belongs in the same
minting pass.

── FOUR rail stops — Design's fourth restored (MRB-249) ─────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that the rail
lost a stop. Design's stage 3 (`#s-two`) ticks on
`Object.keys(s.seen).length >= 7` — the JOURNEY's predicate, verbatim (page
line 415) — and because `#s-two` is an eyebrow, a display line, two cards and a
key fact with no control, no commit and no field, the reading was that MRB-208
forbade the stop and `ks3_parity.check_rail_reachable` would name the defect.
So the lesson shipped THREE rail stops, not four.

Two things overrule that inference.

MRB-205 binds and is not re-argued: Design draws, we render; nothing invented
and nothing dropped; page wins over engine. A stop Design drew and we did not
render is not rendering what Design drew.

And Design's `isDone()` states the tick condition rather than leaving it to be
inferred. It is rail-level and it returns the identical expression for
`#s-journey` and then for `#s-two`. Mechanical and chemical breaking is the
payoff of the seven stops beside it: the section carries no control because the
journey already took the student's commitment. That is a MIRROR, resolved at
rail level in `wireRail`'s `paint()`.

So the fourth stop is declared: anchor `s-two`, `mirrors: "s-journey"`,
`done_when: "all_seven_stops_visited"` — the journey's own predicate, named as
borrowed. `check_rail_matches_design` gates the built rail against
`docs/ks3/rail-manifest.md`. c1-02's `#s-matrix` is restored the same way. The
section keeps its anchor, as it always did, so hash links still work.

── The journey counter opens at ONE, and that is NOT c1-02's defect ─────

c1-02's bench counted the state it was ABOUT to show while the whole
instrument was still behind a commit gate, so a page nobody had touched read
"1 of 3 states seen" above a bench nobody could see. There is no gate here:
stop one is on screen, complete, from first paint, so "1 of 7 stops visited" is
true at rest. The stage still needs six more taps and `data-stage-done` opens
at 0, so nothing ticks on load. Starting at zero instead would force a student
who had read all seven to press the tab that was already open.

── What could not be lifted byte-identical ─────────────────────────────

* **`#s-two`'s two columns are compressed.** Design draws each as a card with
  a tag, a name, a body and a bold-led answer to "Does it let food into the
  blood?". The §5.1.1 block vocabulary is CLOSED; `rule` — whose shell matches
  Design's section value for value (`--ks3-band`, 3px ink, `--ks3-r-block`,
  34px 32px, accent eyebrow) — carries a `term` and a `gloss` per card. So the
  tag and the name are joined by the system's own middot and the body and the
  blood answer become one gloss, with Design's own `<strong>` lead-in intact.
  Every authored byte is present, in Design's order; what is lost is the card's
  internal rule. Reported.

* **Two endmatter cards become one.** Design draws "Next in this unit"
  (b3-06) and "Connects to" (b1-05, b3-07). The engine emits one `references`
  card under one heading. All three links are present under "Connects to",
  with b3-06 first; nothing is lost but the forward-pointer heading, and
  nothing is mislabelled — putting a cross-unit link under "Next in this unit"
  would be worse than losing the heading.

* **The figure id loses its mono treatment.** Design sets `b3-gut-labelled` in
  `var(--ks3-font-mono)` inside the legal line. The foot-line slot takes plain
  text, so the id renders in body copy. The sentence is byte-identical.

── `b3-gut-labelled` is REGISTERED, not dropped ─────────────────────────

NOTES-B3 flag 24: two figure slots are named in lesson legal lines and are not
in the diagram manifest. The legal line stays — it is Design's, and it is the
honest statement that the drawing is owed — and the figure is declared in
`figures[]` at `status: "needed"`, which is legal and is not a build blocker.
The manifest is GENERATED from `figures`, so declaring it turns a dangling
reference into a tracked sourcing task instead of a promise nothing is keeping.

── Ladder length parity (MRB-177) ───────────────────────────────────────

Measured on both marked rungs, and **both PASS unfixed**:

    rung 1   correct 3 words, tied with a distractor at 3 — not strictly the
             longest, so there is no length tell.
    rung 2   correct 14 words, longest distractor 11. Strictly longest, but
             +3 words and ×1.27 — inside both thresholds (≥4 words or ≥1.4×).

No distractor was touched.

⚑ For Mide's science gate — NOTES-B3's own flags, carried here:
  * flag 12  the transit times (mouth ~1 min, oesophagus ~8 s, stomach ~4 h,
             small intestine ~16 h, large intestine 12–30 h, rectum a few
             hours). Wide natural variation; the caveat is in the foot line.
  * flag 13  "you could live without a stomach", stated flatly.
  * flag 14  the gut-is-outside-you topology argument in GOING FURTHER, with
             the swallowed-coin comparison.

⚑ `DIET-11` / `DIET-12` are PROVISIONAL ids — `docs/ks3/misconception-register.md`
  contains no `DIET` family row at all, although NOTES-B3 §5 says fifteen were
  written into it. Nothing machine-reads the register, so the build is
  unaffected; the numbering across all eight B3 lessons has to be reconciled in
  one pass.
"""

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 107 character for character.
    "slug":        "the-digestive-system",
    "title":       "The digestive system",
    "discipline":  "biology",
    "unit":        "nutrition-and-digestion",
    "family":      "SYSTEM",

    # ── curriculum position ─────────────────────────────────────────────────
    # The tissues-and-organs clause of `KS3.B.NUT.04`. See the docstring: the
    # sub-ID is settled by the unit wrapper and still to be minted in
    # `substatements.py`, in one pass with b3-06's and b3-07's.
    "covers":      ["KS3.B.NUT.04a"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2},
                    {"id": "structure-function", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 40,

    # ── progression edges ───────────────────────────────────────────────────
    # Design draws NO "Before this lesson" card on this page, so `requires` is
    # empty and the card is omitted — an empty card is a promise the lesson did
    # not make. See the docstring for why the two link cards become one.
    "requires":    [],
    "assumes":     [],
    "references":  ["enzymes-in-digestion",
                    {"unit": "B1", "lesson": "levels-of-organisation"},
                    "absorption-and-the-small-intestine"],
    "ks4_links":   [],
    "ks4_becomes": "The digestive system as an organ system, with named "
                   "enzymes, bile, and the role of the liver in metabolism.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "A nine-metre tube with seven jobs along it. Food spends "
                    "four hours in the organ everybody names, and sixteen in "
                    "the one that actually does the work.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-two` is the third: no control of
    # its own, so it mirrors `s-journey` and ticks on the journey's predicate —
    # see the docstring. `short` and `label` are Design's own (page lines
    # 322–327).
    "rail": [
        {"anchor": "s-hook",    "short": "HOOK",    "label": "The blender",
         "done_when": "committed"},
        {"anchor": "s-journey", "short": "JOURNEY", "label": "Seven stops",
         "done_when": "all_seven_stops_visited"},
        {"anchor": "s-two", "short": "BREAK", "label": "Two kinds",
         "mirrors": "s-journey", "done_when": "all_seven_stops_visited"},
        {"anchor": "s-ladder",  "short": "LADDER",  "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    "phenomenon": {
        "kind": "narrative",
        "title": "Blend a meal to a smooth liquid. Is it digested?",
        "prompt": "A cheese sandwich goes into a blender for two minutes on "
                  "high. What comes out is a smooth grey liquid with no lumps "
                  "in it at all — smoother than anything your teeth or stomach "
                  "could manage.",
        "commit": "Could that liquid pass straight into your blood?",
        "options": [
            "Yes — it is a liquid with no lumps in it",
            "Yes, but only the parts that dissolved",
            "No — the molecules in it are still far too large",
            "No — it has not been mixed with stomach acid",
        ],
        "reveal": "No — and not because it is not smooth enough. The starch "
                  "molecules in that liquid are still starch molecules, "
                  "thousands of glucose units long and far too large to cross "
                  "a cell membrane. A blender makes pieces smaller. Digestion "
                  "makes <em>molecules</em> smaller, which is a completely "
                  "different operation and needs enzymes rather than blades.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Two, in the document order Design draws them. Each `statement` is
    # Design's own `.ks3-mis-quote` without its quote marks.
    "misconceptions": [
        {"id": "DIET-11",
         "statement": "Digestion is food being squashed into smaller and "
                      "smaller pieces.",
         "elicited_by": "two-wrong-ideas",
         "confronted_by": "two-wrong-ideas"},
        {"id": "DIET-12",
         "statement": "Food sits in your stomach until it is digested, then "
                      "goes to the intestine.",
         "elicited_by": "two-wrong-ideas",
         "confronted_by": "two-wrong-ideas"},
    ],

    # Design draws no keyword block on this page, so these never reach the
    # lesson body; they reach a student as the unit page's chips and are the
    # reading-age gate's exclusion list.
    "vocabulary": [
        {"term": "digestion",
         "definition": "Breaking large insoluble food molecules into small "
                       "soluble ones that can be absorbed.",
         "note": None},
        {"term": "mechanical digestion",
         "definition": "Breaking food into smaller pieces without changing the "
                       "molecules.",
         "note": "Its whole purpose is to expose more surface for the "
                 "chemical kind."},
        {"term": "chemical digestion",
         "definition": "Cutting the long food molecules into short ones, which "
                       "only enzymes can do.",
         "note": None},
        {"term": "peristalsis",
         "definition": "The wave of muscle contraction that squeezes food "
                       "along the gut.",
         "note": "It does not need gravity — you can swallow upside down."},
        {"term": "egestion",
         "definition": "Removing material that passed through the gut and was "
                       "never absorbed.",
         "note": "Not the same as excretion, which is getting rid of waste "
                 "your own cells produced."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ DECLARED BECAUSE THE LEGAL LINE NAMES IT. Design's foot line says the
    # figures for the labelled diagram "are declared in the lesson record as
    # b3-gut-labelled, awaiting illustration", and NOTES-B3 flag 24 records
    # that the id is in no manifest. `status: "needed"` is legal and is not a
    # build blocker; the manifest is GENERATED from this field, so declaring it
    # turns a dangling reference into a tracked sourcing task. No `figure`
    # block is added to `core` — Design draws none, and a slot on the page
    # would be a component nobody drew.
    "figures": [
        {"id": "b3-gut-labelled",
         "kind": "diagram",
         "caption": "The human digestive system, labelled: mouth, oesophagus, "
                    "stomach, small intestine, large intestine, rectum and "
                    "anus, with the pancreas, liver and gall bladder shown "
                    "feeding into the small intestine without food passing "
                    "through them.",
         "status": "needed"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-journey — the flagship, on `ks3-block ks3-dark ks3-practical`.
        # Authored inline; `_normalise` lifts it into `activities[]` and leaves
        # a `practical` shell behind it.
        {"type": "gut-journey", "id": "seven-stops", "anchor": "s-journey",
         "demand": "investigate",
         "eyebrow": "Follow the meal · seven stops",
         "heading": "Where the sandwich actually goes",
         # Opens at ONE, and the docstring says why that is not c1-02's defect.
         "head_counter": {"format": "{n} of 7 stops visited", "total": 7,
                          "start": 1},
         "tile_labels": {"time": "Time spent here",
                         "breaks": "Molecules broken here",
                         "absorbs": "Absorbed here"},
         "note_label": "Worth knowing:",

         # `chart_name` and `chart_hours` are AUTHORED. Design derives both in
         # JS — the name by splitting the label at its first comma, the hours
         # by a three-branch expression — and both are strings a student reads.
         # See the renderer's docstring.
         "stops": [
             {"id": "mouth", "label": "Mouth", "name": "Mouth",
              "kind": "Mechanical and chemical",
              "hours": 0.02, "time": "about 1 minute",
              "chart_name": "Mouth", "chart_hours": "<1 h",
              "breaks": "Starch, a little", "absorbs": "Nothing",
              "what": "Teeth cut and grind the food into a soft mass, and the "
                      "tongue mixes it with saliva. Saliva does two jobs: it "
                      "lubricates the mass so it can be swallowed, and it "
                      "contains amylase, which starts cutting starch chains "
                      "into shorter ones.",
              "note": "Hold a plain cracker on your tongue without chewing and "
                      "it turns faintly sweet in about ninety seconds. That is "
                      "amylase producing sugar from starch, and it is the only "
                      "digestion you can taste happening."},
             {"id": "oesophagus", "label": "Oesophagus", "name": "Oesophagus",
              "kind": "Transport only",
              "hours": 0.003, "time": "about 8 seconds",
              "chart_name": "Oesophagus", "chart_hours": "<1 h",
              "breaks": "Nothing", "absorbs": "Nothing",
              "what": "A muscular tube from throat to stomach. Rings of muscle "
                      "contract behind the food and relax in front of it, "
                      "squeezing it along. This wave is called peristalsis and "
                      "it happens the whole length of the gut.",
              "note": "Peristalsis does not need gravity. An astronaut can "
                      "swallow upside down in orbit, and so can you — the "
                      "muscle wave, not the fall, moves the food."},
             {"id": "stomach", "label": "Stomach", "name": "Stomach",
              "kind": "Mechanical and chemical",
              "hours": 4, "time": "about 4 hours",
              "chart_name": "Stomach", "chart_hours": "4 h",
              "breaks": "Protein", "absorbs": "Almost nothing",
              "what": "A muscular bag that churns the food, adds hydrochloric "
                      "acid at about pH 2, and adds the enzyme protease to "
                      "begin breaking protein into shorter chains. The acid "
                      "also kills most bacteria swallowed with the meal.",
              "note": "The acid is strong enough to dissolve the stomach "
                      "itself, which is why the lining secretes a layer of "
                      "mucus and replaces its own cells every few days. Ulcers "
                      "are what happens when that defence fails — usually "
                      "because of a bacterium, not because of stress or spicy "
                      "food."},
             {"id": "smallint", "label": "Small intestine",
              "name": "Small intestine",
              "kind": "Chemical, then absorption",
              "hours": 16, "time": "about 16 hours",
              "chart_name": "Small intestine", "chart_hours": "16 h",
              "breaks": "Starch, protein and lipid — all of them, to "
                        "completion",
              "absorbs": "Almost everything",
              "what": "Six or seven metres of narrow tube, and the organ that "
                      "does most of the work. Enzymes from the pancreas and "
                      "from the intestine wall finish breaking every nutrient "
                      "down to molecules small enough to cross a membrane, and "
                      "those molecules are then absorbed into the blood "
                      "through the intestine wall.",
              "note": "Its surface is folded, then covered in villi, then each "
                      "villus cell is covered in microvilli — three levels of "
                      "folding that bring the absorbing surface to around "
                      "30 m². That is the next lesson’s subject and it is the "
                      "single best piece of engineering in the body."},
             {"id": "pancreas", "label": "Pancreas, liver, gall bladder",
              "name": "Pancreas, liver and gall bladder",
              "kind": "Secretion — no food passes through",
              "hours": 0, "time": "no food enters these",
              "chart_name": "Pancreas", "chart_hours": "—",
              "breaks": "They supply what does the breaking",
              "absorbs": "Nothing",
              "what": "These three feed into the small intestine without ever "
                      "holding food. The pancreas supplies amylase, protease "
                      "and lipase together with an alkali that neutralises the "
                      "stomach acid. The liver makes bile; the gall bladder "
                      "stores it and releases it onto fatty food.",
              "note": "Bile is not an enzyme and digests nothing. It breaks "
                      "large fat droplets into many small ones — "
                      "emulsification — which is mechanical digestion "
                      "happening chemically, and it multiplies the surface "
                      "available to lipase enormously."},
             {"id": "largeint", "label": "Large intestine",
              "name": "Large intestine",
              "kind": "Absorption of water",
              "hours": 20, "time": "12 to 30 hours",
              "chart_name": "Large intestine", "chart_hours": "20 h",
              "breaks": "Nothing your enzymes can break",
              "absorbs": "Water, some minerals and some vitamins",
              "what": "Wider and shorter than the small intestine. By the time "
                      "material arrives, the nutrients have gone; what is left "
                      "is water, fibre and bacteria. The wall absorbs most of "
                      "the water back, leaving a solid mass.",
              "note": "This is where the trillions of gut bacteria live, and "
                      "they digest some of the fibre your own enzymes cannot "
                      "touch — releasing fatty acids and making vitamin K and "
                      "some B vitamins as by-products. That is lesson eight."},
             {"id": "rectum", "label": "Rectum and anus",
              "name": "Rectum and anus",
              "kind": "Storage and egestion",
              "hours": 6, "time": "a few hours",
              "chart_name": "Rectum and anus", "chart_hours": "6 h",
              "breaks": "Nothing", "absorbs": "Nothing",
              "what": "The remaining solid material is stored in the rectum "
                      "and leaves through the anus. This is egestion — the "
                      "removal of material that was never absorbed.",
              "note": "Egestion is not excretion, and examiners care about the "
                      "difference. Excretion is getting rid of waste your own "
                      "cells produced, such as urea and carbon dioxide. "
                      "Egestion is getting rid of what you never took in."},
         ],

         # ⚖️ THE CHART IS THE ARGUMENT. Its closing line is what turns seven
         # bars into the claim the lesson's big question makes.
         "chart": {
             "label": "Hours spent in each organ, to scale",
             "close": "The stomach is the organ everyone names first and it "
                      "holds the meal for about four hours. The small "
                      "intestine holds it for four times as long, and that is "
                      "where nearly all digestion is completed and nearly all "
                      "absorption happens."}},

        # #s-two — Design's classless band section, which IS the `rule` shell.
        # Rail stop 3, mirroring `s-journey`; see the docstring.
        {"type": "rule", "anchor": "s-two",
         "eyebrow": "Two kinds of breaking",
         "statement": "Smaller pieces is not smaller molecules.",
         # ⚠️ COMPRESSED, and Design's own <strong> lead-in is kept.
         "cards": [
             {"term": "Mechanical digestion · Making pieces smaller",
              "gloss": "Teeth cutting and grinding, the stomach churning, bile "
                       "splitting fat droplets. The chemical nature of the "
                       "food does not change at all — starch is still starch "
                       "afterwards. "
                       "<strong>Does it let food into the blood?</strong> No. "
                       "A crumb of bread a thousand times smaller is still "
                       "made of the same molecules, and they are still too "
                       "large to cross a membrane."},
             {"term": "Chemical digestion · Making molecules smaller",
              "gloss": "Enzymes cut the long chains at each link: starch to "
                       "glucose, protein to amino acids, lipid to fatty acids "
                       "and glycerol. This is a chemical change and the "
                       "products are different substances from what went in. "
                       "<strong>Does it let food into the blood?</strong> Yes. "
                       "This is the only process that produces molecules small "
                       "enough and soluble enough to be absorbed — which is "
                       "why enzymes, not teeth, are the point of the system."},
         ]},

        {"type": "key-fact", "ref": "digestion-is-chemical"},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "DIET-11"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "digestion-is-chemical",
         "text": "Digestion is the breaking of large insoluble molecules into "
                 "small soluble ones. Chewing and churning only increase "
                 "surface area so the enzymes can work faster — they digest "
                 "nothing on their own.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "DIET-11",
         "statements": [
             {"quote": "Digestion is food being squashed into smaller and "
                       "smaller pieces.",
              "body": [
                  "If that were true, the blender in the hook would have done "
                  "the whole job. Follow the sizes instead. A starch molecule "
                  "in bread is a chain of a few thousand glucose units; a "
                  "glucose unit is about 0.0000009 mm across; the gaps that "
                  "let molecules cross a cell membrane are of that order. "
                  "Cutting the bread into a million crumbs leaves every starch "
                  "molecule exactly as long as it was — you have made more, "
                  "smaller pieces of the same molecule. What has to happen is "
                  "that the chain is cut chemically at each link, and only an "
                  "enzyme does that. The word for what your teeth do is "
                  "<em>mechanical digestion</em>, and its entire purpose is to "
                  "expose more surface for the chemical kind."]},
             {"quote": "Food sits in your stomach until it is digested, then "
                       "goes to the intestine.",
              "body": [
                  "The stomach is not the destination — it is a holding tank "
                  "with an acid bath and a strong set of muscles. It holds a "
                  "meal for roughly four hours, kills most of the bacteria "
                  "that came in with it, starts protein digestion, and "
                  "releases the result into the small intestine a little at a "
                  "time. Almost nothing is absorbed through the stomach wall: "
                  "no glucose, no amino acids, no fatty acids. If your stomach "
                  "were removed — and people do live without one — you could "
                  "still digest and absorb a meal, because the organ that does "
                  "the real work is the next one along."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # ⚖️ NO DISTRACTOR WAS TOUCHED. Both marked rungs pass the MRB-177
    # length-parity check as delivered — see the docstring for the measurement.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Where does the work happen",
            "q": "In which organ is most food digested and most food "
                 "absorbed?",
            "options": [
                "The stomach",
                "The small intestine",
                "The large intestine",
                "The mouth",
            ],
            "answer": 1,
            "feedback": {
                0: "The stomach starts protein digestion and absorbs virtually "
                   "nothing. It holds the meal for four hours; the small "
                   "intestine holds it for sixteen.",
                2: "By the time material reaches the large intestine the "
                   "nutrients have already been absorbed. It takes back water, "
                   "not food.",
                3: "The mouth begins starch digestion and absorbs nothing. The "
                   "food is there for about a minute.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A patient has their gall bladder removed and is advised to "
                 "avoid very fatty meals. Bile contains no enzymes. Why does "
                 "losing bile storage make fat harder to digest?",
            "options": [
                "Bile digests fat, so without it fat is not broken down",
                "Bile emulsifies fat into small droplets, giving lipase far "
                "more surface to work on",
                "Bile neutralises stomach acid, and without it lipase is "
                "destroyed",
                "Without a gall bladder the liver stops making bile",
            ],
            "answer": 1,
            "feedback": {
                0: "Bile contains no enzymes and digests nothing. Lipase does "
                   "the digesting — the question is why lipase becomes less "
                   "effective.",
                2: "Neutralising the acid is done by alkali from the pancreas, "
                   "not by bile, and that still happens.",
                3: "The liver carries on making bile. What is lost is the "
                   "ability to store it and release a large amount at once "
                   "onto a fatty meal.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the blender",
            "q": "A student argues that if you blended a meal finely enough, "
                 "you would not need a digestive system. Explain what is right "
                 "and what is wrong in their reasoning, using the difference "
                 "between mechanical and chemical digestion.",
            "field_label": "Your explanation",
            "placeholder": "They are right that… but wrong that…",
            "success": [
                "Credits what is right: blending does the job of mechanical "
                "digestion, and does it better than teeth.",
                "Says mechanical breakdown makes pieces smaller without "
                "changing the molecules.",
                "States that absorption needs small soluble molecules, and "
                "starch, protein and lipid molecules are too large.",
                "Says only enzymes can cut the molecules, and names at least "
                "one product — glucose, amino acids, or fatty acids.",
                "Concludes that blending removes the need for chewing, not for "
                "the digestive system.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A person has a section of small intestine removed after an "
                 "injury. Predict what will change about their digestion and "
                 "absorption, say why the stomach cannot compensate, and name "
                 "one thing that would not change at all.",
            "field_label": "Your answer",
            "placeholder": "Losing small intestine would mean…",
            "success": [
                "Predicts reduced absorption, because absorbing surface has "
                "been lost.",
                "Explains that the stomach cannot compensate because it barely "
                "absorbs anything even when intact.",
                "Notes that digestion may be less complete too, since enzymes "
                "have less time and less surface to act on.",
                "Names something unchanged — chewing, swallowing, stomach "
                "acid, or egestion.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Food passes through the mouth, oesophagus, stomach, small "
                "intestine and large intestine. The pancreas, liver and gall "
                "bladder add secretions without food passing through them. "
                "Mechanical breakdown increases surface area; chemical "
                "breakdown by enzymes turns large insoluble molecules into "
                "small soluble ones. Almost all absorption happens in the "
                "small intestine.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # MRB-225: the model's edges live HERE, and nothing above is retracted —
    # the seven-stop journey is not withdrawn, it is given a topology.
    "stretch": [
        {"type": "explainer", "id": "outside-you",
         "text": "There is a real sense in which the inside of your gut is "
                 "outside your body. The tube runs from mouth to anus without "
                 "interruption, so its contents are topologically outside you "
                 "in the same way that the hole in a doughnut is outside the "
                 "doughnut — nothing has entered you until it has crossed the "
                 "gut wall into the blood. This is not a word game; it is why "
                 "the gut can hold trillions of bacteria without your immune "
                 "system treating it as an infection, and why swallowing a "
                 "small coin is usually harmless while the same coin in your "
                 "bloodstream would not be. Absorption, not swallowing, is the "
                 "moment food enters you."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Unclear why chewing is not digestion on its own?",
              "cta": "Ask about this lesson",
              "anchor": "s-two"},

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["analysis-and-evaluation"],

    # ⚠️ THE FOOT LINE, BYTE-IDENTICAL. It is a statement about how the numbers
    # on this page were taken, which is exactly what `convention_note` is for
    # (plain `.ks3-legal`, page-specific, before the standing line) rather than
    # `safety_note`, whose treatment is reserved for "never do this without an
    # adult". Design sets the figure id in mono inside the sentence; the slot
    # takes plain text, so the id renders in body copy and the words are
    # unchanged.
    "convention_note": "Transit times are typical figures for a mixed meal in "
                       "a healthy adult and vary widely between people and "
                       "between meals. Figures for the labelled diagram are "
                       "declared in the lesson record as b3-gut-labelled, "
                       "awaiting illustration.",

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
