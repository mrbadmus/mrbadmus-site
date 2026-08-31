"""B3 L7 — Absorption and the small intestine (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b3/b3-07-absorption-and-the-small-intestine.dc.html` (533 lines),
and its author's notes, `docs/ks3/design-reference/b3/NOTES-B3.md` §3.5 and flags 17–19.
Schema per architecture.md §4.8 as amended by §4.8.1 and §4.8.2; shape follows
`ks3_data/c1/lesson_02_solids_liquids_and_gases.py`.

Every student-facing string is byte-identical to the approved page, with the
four documented exceptions listed under "What could not be lifted" below.

── ⚠️ THE SURFACE AREA IS ~30 m², AND THAT IS NOT A TYPO ────────────────

NOTES-B3 flag 17, and it is the flag its author most wanted a ruling on. The
older figure, still widely in print, came from measuring folds and villi on
tissue that had been fixed, dried and stretched. Careful measurements on FRESH
tissue, published in 2014, put the area closer to 30 m². The biology did not
change; the method did.

**Do not "correct" this back to the famous number.** MRB-225 is explicit that a
lesson teaches the version that is TRUE, not the version that is FAMOUS, and
this is the exact case that rule was written for: a well-meaning editor who
recognises the older number and does not recognise 30 m² will change it, and
every number on the page is wired to it — the hook's "sixty times", the four
bench notes, the three multipliers and the readout.

✅ RULED BY MIDE, 31 Aug 2026 (MRB-233 · 3c): **~30 m² STANDS.** flag 17 is
CLOSED and this page does not move.

⊕ AND THE HEDGE IS OUT WITH IT. This block used to end by pointing at "the
stretch layer that explains the revision", and to say that layer "prints BOTH
figures and says the older one is still in print, which is Design's own
handling and is the honest one". That layer is GONE — see the `stretch` key
below, which quotes it in full. The page now carries ONE figure and no
commentary about which books disagree. A comparison may be drawn to the
figure, but it must FIT ~30 m², and **a tennis court is the OLD figure's
comparison and must never appear on this page again.**

⚠️ WHY "A THIRD OF A BADMINTON COURT", AND NOT A HALF OR A WHOLE ONE. Mide's
ruling names badminton — "a badminton court is close" — and the object is his.
The FRACTION is arithmetic, and the arithmetic is the reason the page says a
third: a doubles badminton court is 13.4 m × 6.1 m = 81.7 m², so a whole one is
2.7× the figure, a half is 40.9 m² (36% high) and a third is 27.2 m² — within
10% of 30, and the only one of the three that satisfies the rule above. For
scale, a doubles tennis court is 23.77 m × 10.97 m = 260.8 m², which is not a
coincidence: it IS the 200–300 m² figure, and that is why it was the old
comparison. The wording this replaced, "roughly the floor of a small bedroom",
failed the rule in the other direction — a small UK bedroom is 7–10 m².

⚑ The remaining half of flag 17 STILL BINDS: **if the course's other materials
say otherwise, the two must be made to agree, and this page is not the one
that should move on its own.** The MRB-233 sweep checked, and found nothing to
reconcile — KS4 biology states no intestinal surface area at all, and the
ladder carries no figure.

── FOUR rail stops — Design's fourth restored (MRB-249) ────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to read "the rail is
THREE stops, not Design's four", and it took `ks3_data/c1/lesson_02`'s handling
of `#s-matrix` with it. Design's rail lists `s-hook`, `s-fold`, `s-four`,
`s-ladder`, and its own tick function reads:

    if (id === 's-fold')  return s.on.folds && s.on.villi && s.on.microvilli;
    if (id === 's-four')  return s.on.folds && s.on.villi && s.on.microvilli;

— stage three's predicate is stage two's, character for character. Because
`#s-four` is an eyebrow, a statement, four cards and a key fact, emitting no
control, no commitment and no field, the argument ran: MRB-208 confines the
rail to sections that require the student to DO something,
`ks3_parity.check_rail_reachable` fails a stop whose section carries none of
the signals `doneByDom()` reads, and inventing a control Design did not draw is
closed to this build — so the stop came off.

That is overruled on two grounds.

MRB-205 binds and is not re-argued: Design draws, we render; no invented and no
dropped page structure; page wins over engine. Dropping a stop Design drew is
not rendering what Design drew, whatever the engine would have preferred.

And read the two lines above again as a statement rather than a duplication.
`isDone()` is a rail-level function, and Design writing the same expression for
two consecutive ids is Design saying how the second one ticks. The four
features ARE the reading of the surface the student just built: the section
carries no control because `#s-fold` already took the commitment. That is a
MIRROR, resolved at rail level in `wireRail`'s `paint()` and serialised into
`data-rail-stages` by `build_ks3.py`.

So the stop is declared: anchor `s-four`, `mirrors: "s-fold"`,
`done_when: "all_three_levels_on"` — stage two's predicate, named as borrowed
rather than smuggled, and gated by `ks3_parity.check_rail_matches_design`
against `docs/ks3/rail-manifest.md`. `#s-four` keeps its anchor and its
scroll-margin, as it always did. `#s-think` is still not a candidate — Design
does not draw a stop on it, and on this page it is two quotes and two
paragraphs with nothing to answer, unlike C1's, which commit.

── What could not be lifted byte-identical, and why ────────────────────

1. **The two inline links in `#s-think`.** Design writes "the same process you
   met in <a href="c1-05-diffusion.html">Diffusion</a>". `rich()` allows `<em>`
   and `<strong>` and nothing else — an anchor would render as visible tag soup
   — so the WORDS are unchanged and the hyperlink is dropped. The destination
   is not lost: `references` renders it in the end matter, which is where the
   engine puts cross-lesson navigation.
2. **The mono span in the legal line.** Design sets `b3-villus-labelled` in
   `var(--ks3-font-mono)`; `t()` escapes markup in a foot line, so the figure
   id renders as plain text. The sentence is otherwise unchanged.
3. **The `#s-four` card TAGS.** Design's card carries a mono accent tag
   ("Feature 1") above the name; the shipped `rule` card is `term` + `gloss`
   and has no tag slot. Tag and name are joined with Design's own middle-dot
   idiom — the same joiner it uses in "Level 1 · Circular folds" and
   "Nutrition and digestion · Model" — so both strings survive and neither is
   invented. Same for the "Remove it and:" line, which keeps Design's own
   `<strong>` and joins the paragraph above it.
4. **Two endmatter cards become one.** Design draws "Next in this unit" and
   "Connects to" as two link cards; the engine's end matter is a fixed three
   (prereqs / connects / KS4). All three links are kept, under "Connects to",
   because dropping the forward link to `bacteria-in-the-gut` would lose
   navigation Design drew, and heading the card "Next in this unit" would
   describe `Diffusion` — which is in another unit entirely — as the next
   lesson.

── Design decisions corrected ──────────────────────────────────────────

Only the rail (above) and the ladder's rung-1 option set (below); nothing else
on this page needed one. The ~30 m² figure is NOT a correction — it is Design's
number, deliberately kept, and the note above exists so it stays kept.
"""

# ── the three folding levels (page lines 307–314) ───────────────────────
# ⊕ MRB-257 (5.47) — MULTIPLIERS ×3, ×5, ×4 ON A 0.5 m² BASE LAND AT EXACTLY
# 30.0 m² AND ×60. Design's ×3, ×7, ×3 land at 31.5 m², which printed as
# "32 m²" and "×63" — the only two figures on the page that were not 30 and
# sixty. Four separate prose sites say otherwise and all four are right:
# the readout note ("About 30 m² … and sixty times the plain tube"), the hook
# ("Same length, same width, sixty times the surface"), the key fact ("roughly
# 30 m² … about a sixtieth as fast"). The instrument was the one thing on the
# page disagreeing with the lesson, on the number the lesson is about.
# ⊕ MRB-233 (3c) — a FOURTH site used to be listed here, GOING FURTHER's
# "fresh-tissue measurements closer to 30 m²". That layer was removed by
# Mide's ruling; the three prose sites above are now the whole set, and they
# still all say 30 and sixty.
#
# ⚑ NOTES-B3 flag 18 already recorded that the factors are chosen to land on
# ~30 m² and are NOT separately sourced measurements — the block is a model of
# compounding and the legal line says the figures are approximate. That is what
# makes this a build correction rather than a science one: no sourced figure
# moved, because there was never a sourced figure here. Villi remain the
# largest single factor, which is what note 2 claims. If sourced factors are
# ever supplied they replace these and every note below is recomputed with them.
LEVELS = [
    {"id": "folds", "name": "Level 1 · Circular folds", "factor": 3,
     "scale": "Visible without a microscope — ridges a few millimetres deep",
     "what": "The whole wall is thrown into ridges running round the tube, "
             "like the inside of a concertina. Nothing is added; the same "
             "sheet is corrugated."},
    {"id": "villi", "name": "Level 2 · Villi", "factor": 5,
     "scale": "About 1 mm long — visible with a hand lens, like velvet",
     "what": "Every square millimetre of that folded wall carries thousands "
             "of finger-shaped projections. Each villus has a network of "
             "capillaries inside it and a wall one cell thick."},
    {"id": "microvilli", "name": "Level 3 · Microvilli", "factor": 4,
     "scale": "About 0.001 mm — needs an electron microscope",
     "what": "Each cell covering a villus has its own outer surface thrown "
             "into hundreds of tiny projections. Folds on folds on folds — "
             "the third and last level."},
]

# ── the four cumulative bench notes (page lines 422–427) ────────────────
# ⚠️ Indexed by HOW MANY levels are on, and therefore TRUE ONLY OF THE PREFIX
# STATES — folds, then folds+villi, then all three, which is the stack these
# four sentences were written for. `FOLD_SET_NOTES` below covers the four
# states that are NOT prefixes, and the renderer refuses a payload that leaves
# any of the eight with nothing true to say. See 5.18.
FOLD_NOTES = [
    "A plain tube. Half a square metre — about a tea towel. A meal would be "
    "through you long before much of it crossed the wall.",
    "Corrugating the wall triples it — one and a half square metres. Still "
    "nothing like enough, and this is the only level you could see with the "
    "naked eye.",
    "Villi are where most of the gain comes from. Seven and a half square "
    "metres of absorbing surface, in a tube you could coil in your hands.",
    "About 30 m² — roughly a third of a badminton court, and sixty "
    "times the plain tube. The length is still six metres.",
]

# ── the four set notes (MRB-257 · 5.18) ─────────────────────────────────
# ⚠️ THE FOUR STATES THAT ARE NOT PREFIXES. The note used to be keyed on HOW
# MANY levels were on rather than WHICH, so:
#   villi only        → "Corrugating the wall triples it"  (that is the FOLDS)
#   microvilli only   → the same sentence, about a level that "needs an
#                       electron microscope"
#   folds+microvilli  → "Villi are where most of the gain comes from. Ten
#                       square metres" — with the villi switched off
# Keyed by the "+"-joined ids of the levels that are ON, in document order.
# The four prefix states ("", folds, folds+villi, folds+villi+microvilli) are
# not here: `FOLD_NOTES` is already true of them, and duplicating a sentence
# is how the two copies drift apart.
FOLD_SET_NOTES = {
    "villi":
        "Villi alone multiply it by five — two and a half square metres. This "
        "is the level that gives the most, and here it is doing it on a wall "
        "nobody has corrugated.",
    "microvilli":
        "Microvilli alone multiply it by four — two square metres. Every one "
        "of them sits on a cell surface you would need an electron microscope "
        "to see.",
    "folds+microvilli":
        "Twelve times the plain tube, six square metres — with the middle "
        "level missing. Leaving the villi out costs more than leaving out "
        "either of the others.",
    "villi+microvilli":
        "Twenty times the plain tube: ten square metres of velvet, on a wall "
        "that was never corrugated.",
}

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 109 character for character. Slugs are
    # permanent (§8.4) and are the join for every `requires` edge.
    "slug":        "absorption-and-the-small-intestine",
    "title":       "Absorption and the small intestine",
    "discipline":  "biology",
    "unit":        "nutrition-and-digestion",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # ⚑ `KS3.B.NUT.04c`, not the parent. The bullet is compound — tissues and
    # organs / enzymes as catalysts / adaptations to function — and B3 teaches
    # it as three lessons. The allocation is the unit wrapper's
    # (`ks3_data/biology_b3_nutrition.py`), which names L5 → `04a`, L6 → `04b`
    # and this lesson → `04c`; it is followed rather than re-derived so the
    # three modules cannot disagree about which clause each owns.
    #
    # ⚠️ `KS3.B.NUT.04` is NOT yet registered in `ks3_data/substatements.py`.
    # Nothing fails: `validate()` rule 5 only refuses a parent and its clause
    # being owned together, and the parent is owned by nobody. But rule 4 of
    # that file says a sub-ID is permanent once referenced, so the three
    # clauses need minting in ONE pass — a/b/c together, by whoever owns the
    # unit — and not three times from three lesson modules that would each
    # write the same dict key. Reported rather than done here for exactly that
    # reason; L5 and L6 were authored in parallel with this file.
    "covers":      ["KS3.B.NUT.04c"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "structure-function", "level": 3},
                    {"id": "cells-and-systems", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 45,

    # ── progression edges ───────────────────────────────────────────────────
    # No `requires`: Design draws no "Before this lesson" card here, and the
    # engine omits an empty one. All three of Design's forward and sideways
    # links live in the middle card — see "What could not be lifted" 4.
    "requires":    [],
    "assumes":     [],
    "references":  ["bacteria-in-the-gut",
                    {"unit": "C1", "lesson": "diffusion"},
                    {"unit": "B4", "lesson": "alveoli-built-for-exchange"}],
    "ks4_links":   [],
    # Renders only because `ks4_links` is empty — Design's card 3 is prose,
    # not a link, and this is the slot §4.8.1 D added for exactly that.
    "ks4_becomes": "Exchange surfaces and the surface area to volume ratio, "
                   "plus active transport of glucose against a gradient.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "A tube six metres long has half a square metre of inside "
                    "surface. Yours has about thirty. Nothing was made longer.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-four` is the third: no control of
    # its own, so it mirrors `s-fold` and ticks on the fold's predicate — see
    # the docstring. `short` is ≤6 characters and both are Design's own
    # `RAIL_SHORT` and `RAIL` strings (page lines 297–303).
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "Hose and gut",
         "done_when": "committed"},
        {"anchor": "s-fold",   "short": "FOLD",   "label": "Build the surface",
         "done_when": "all_three_levels_on"},
        {"anchor": "s-four", "short": "FOUR", "label": "Four features",
         "mirrors": "s-fold", "done_when": "all_three_levels_on"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3).
    "phenomenon": {
        "kind": "narrative",
        "title": "A garden hose six metres long, and your small intestine. "
                 "Same length.",
        "prompt": "Both about six metres. Both about two and a half "
                  "centimetres across. The hose has roughly half a square "
                  "metre of inner surface — the area of a tea towel. Your "
                  "small intestine has about thirty square metres, roughly "
                  "a third of a badminton court.",
        "commit": "Same length, same width, sixty times the surface. How?",
        "options": [
            "The intestine is coiled up, which adds surface",
            "Its wall is folded at three different scales",
            "It stretches when food is inside it",
            "Its wall is much thicker than a hose’s",
        ],
        "reveal": "Folding, three times over, at three different scales. "
                  "Surface area is not fixed by length and width — a crumpled "
                  "sheet occupies the same box as a flat one and has the same "
                  "area, but a sheet with folds <em>on</em> its folds fits far "
                  "more surface into the same box. That is the whole design.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ THE `DIET` FAMILY IS NOT YET IN `docs/ks3/misconception-register.md`.
    # NOTES-B3 §5 says fifteen entries were "minted, not proposed", and the
    # register has no `DIET` row at all — so these ids are the unit's to
    # register in one pass, and this module deliberately does not write them
    # (the register is shared with the other seven lessons, authored in
    # parallel). Nothing fails meanwhile: `_misconception_quote` resolves from
    # THIS list, and both blocks carry their own `statements` anyway, which win
    # over the register (build_ks3.py:2504).
    #
    # `DIET-16` is pinned by NOTES-B3 §5: "DIET-16 is PART-10/PART-11 in
    # biological costume, and absorption-and-the-small-intestine is the first
    # lesson where the belief costs a mark. The confrontation names C1
    # explicitly." Design's second block does name C1 explicitly. `DIET-15` is
    # the adjacent slot for this lesson's other wrong idea; reported.
    "misconceptions": [
        {"id": "DIET-15",
         "statement": "Villi make the intestine longer.",
         # The bench is what elicits it: a student watching the area climb
         # while the length caption does not move is being shown the
         # distinction before it is named.
         "elicited_by": "fold-builder",
         "confronted_by": "villi-and-length"},
        {"id": "DIET-16",
         "statement": "The muscles push the food through the gut wall into "
                      "the blood.",
         "elicited_by": "villi-and-length",
         "confronted_by": "villi-and-length"},
    ],

    # Design draws no keyword block anywhere in B3, so these definitions never
    # reach the lesson body. The TERMS do reach a student, as the unit page's
    # "Words this unit gives you" chips, and the reading-age gate reads them as
    # its exclusion list — which matters here, because "microvilli" and
    # "villus" would otherwise both count against the page's reading age.
    "vocabulary": [
        {"term": "absorption",
         "definition": "The movement of small, soluble molecules out of the "
                       "gut and into the blood.",
         "note": None},
        {"term": "villus",
         "definition": "One of the millions of finger-shaped projections that "
                       "line the small intestine.",
         "note": "One villus, many villi. Each one has capillaries inside it "
                 "and a wall a single cell thick."},
        {"term": "microvilli",
         "definition": "The hundreds of tiny projections on the outer surface "
                       "of each cell covering a villus.",
         "note": None},
        {"term": "surface area",
         "definition": "The total area of a surface. Folding increases it "
                       "without changing length or width.",
         "note": None},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⊕ REGISTERED, not dropped. Design's legal line names `b3-villus-labelled`
    # in the lesson record and the manifest had never heard of it — NOTES-B3
    # flag 24 records the gap for this figure and `b3-gut-labelled`. The
    # manifest is GENERATED from this field, so declaring it turns a dangling
    # reference in a page's foot into a tracked sourcing task. `needed` is
    # legal and is not a build blocker (§4.10).
    #
    # No `core` block renders it: Design draws no figure on this page, only the
    # declaration. The caption describes what the drawing has to show and
    # nothing beyond it — no lacteal, because the lesson does not teach one and
    # a caption naming untaught structure would commission a diagram this page
    # could not use.
    # ⊕ MRB-254 — DRAWN. Design's, ported element for element, with three
    # collisions in her delivery repaired: three crossing labels moved clear of
    # their own arrow shafts, five scatter circles moved off two lines of text,
    # and frame 3's heading pulled inside the viewBox it was four units outside
    # of. All three were collisions rather than compositions, which is what
    # puts them inside MRB-205's "refine inside a shape she drew".
    "figures": [
        {"id": "b3-villus-labelled",
         "kind": "diagram",
         "status": "drawn",
         "art": "villus",
         "title": "Three scales of folding in the small intestine, and one "
                  "villus cut through",
         "desc": "Three framed drawings across the top, each a magnified "
                 "callout of the one before it. The first shows a length of "
                 "the small intestine as a tube, cut open at the near end, "
                 "its inner wall thrown into ring-shaped ridges rather than "
                 "being smooth. A callout from one ridge opens into the "
                 "second frame, where the surface of that single ridge is "
                 "covered in upright finger-shaped villi. A callout from one "
                 "villus opens into the third frame, where the surface of a "
                 "single villus cell is covered in far smaller projections, "
                 "the microvilli. A second callout from the same row of villi "
                 "opens downward into a wide panel beneath, showing one "
                 "villus cut lengthways. Its wall is drawn as a single row of "
                 "cells, divided by cross lines so the count can be checked, "
                 "and inside the villus a capillary runs up to the tip and "
                 "back. Three arrows cross the wall from the gut into the "
                 "capillary, labelled glucose, amino acids and fatty acids.",
         "caption": "Each frame is drawn from a callout of the frame before "
                    "it, so the folding is one thing at three sizes rather "
                    "than three separate facts: the tube is ridged, every "
                    "ridge is covered in villi, and every cell of every "
                    "villus is covered in microvilli. The panel underneath "
                    "shows why it is worth doing. Count the cells across the "
                    "wall of the villus — there is one. On the far side of "
                    "that single cell is a capillary, which is why a glucose "
                    "molecule in the gut is in the bloodstream a moment "
                    "later."}
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-fold — the flagship. Ink-dark `practical`, per the measured table
        # in `ks3_data/b3/__init__.py`: every B3 flagship sits on
        # `ks3-block ks3-dark ks3-practical`, and this one is no exception.
        # Authored inline here, where its position in the document is obvious,
        # and lifted into `activities[]` by `_normalise`.
        {"type": "fold-builder", "id": "fold-builder", "anchor": "s-fold",
         "demand": "investigate",
         "targets": "DIET-15",
         "eyebrow": "Build the surface · three levels",
         "heading": "Switch each level on and watch the area",
         # Opens at ZERO: Design's `startAllFolds` prop defaults false, so the
         # resting page is a plain tube and "0 of 3 levels on" is true of it.
         "head_counter": {"format": "{n} of 3 levels on", "total": 3,
                          "start": 0},
         "prompt": "Start with a plain tube and add the folds one level at a "
                   "time. The length never changes.",

         "base_area": 0.5,
         "levels": LEVELS,
         "notes": FOLD_NOTES,
         "set_notes": FOLD_SET_NOTES,

         # The readout's three authored strings. `{a}` and `{x}` are the two
         # live numbers; everything else is finished text, so the runtime
         # composes an area and a multiple and never a sentence.
         "readout_label": "Absorbing surface",
         "area_format": "{a} m²",
         "multiple_format": "Compared with the plain tube: ×{x}",

         # `{factor}` is filled at build time, so each button ships both of its
         # finished faces and the runtime only swaps between them.
         "labels": {"off": "Add this level", "on": "On · ×{factor}"}},

        # #s-four — Design's band-on-3px-ink statement panel with four cards.
        # That IS the `rule` shell (§5.1.1): `--ks3-band`, 3px ink, no shadow,
        # accent eyebrow, display statement, auto-fit card grid. NOT a `check`
        # activity — there is nothing to do in it, which is why its rail stop
        # mirrors `s-fold` rather than carrying a predicate of its own.
        {"type": "rule", "anchor": "s-four",
         "eyebrow": "What a good exchange surface needs",
         "statement": "Area is only one of four, and the villus has all four.",
         "cards": [
             {"term": "Feature 1 · Very large surface area",
              "gloss": "Three levels of folding bring roughly 30 m² of "
                       "absorbing surface into a tube six metres long. "
                       "<strong>Remove it and:</strong> A plain tube of the "
                       "same size absorbs about a sixtieth as fast. A meal "
                       "would pass through largely unabsorbed."},
             {"term": "Feature 2 · Wall one cell thick",
              "gloss": "The distance from the gut contents to the blood "
                       "inside a villus is a single cell — the shortest "
                       "diffusion path the body can build. "
                       "<strong>Remove it and:</strong> Diffusion slows "
                       "sharply as the distance grows. A wall ten cells thick "
                       "would be a tenth as fast for the same area."},
             {"term": "Feature 3 · Dense blood supply",
              "gloss": "A capillary network runs through every villus, "
                       "carrying absorbed molecules away as fast as they "
                       "arrive. <strong>Remove it and:</strong> The blood "
                       "side fills up, the concentration difference "
                       "disappears, and diffusion stops — with the surface "
                       "and the thin wall entirely intact."},
             {"term": "Feature 4 · Moist surface",
              "gloss": "Everything is in solution. Molecules can only diffuse "
                       "through a membrane dissolved in water. "
                       "<strong>Remove it and:</strong> A dry surface absorbs "
                       "nothing at all. This is why every exchange surface in "
                       "every organism is wet."},
         ]},

        # Design nests the key fact INSIDE `#s-four`; the engine's key-fact box
        # is a direct child of `.ks3-lesson` positioned by document order, so
        # it renders immediately below the panel instead of inside it. Same
        # sequence, same treatment — `card` ground on the accent shadow, which
        # is what Design draws.
        {"type": "key-fact", "ref": "diffusion-not-a-push"},

        # ⊕ MRB-254 — THE FIGURE ANSWERS THE BENCH'S OWN INSTRUCTION. The fold

        # builder says "Switch each level on and watch the area" and only a

        # NUMBER changes: three levels of physical nesting delivered as three

        # text cards. "Folds on folds on folds" is the whole idea and it is the

        # one thing the instrument cannot draw. The section underneath then

        # says what the folding is for — a wall a student can count the cells

        # across, with the blood already on the other side of it.

        {"type": "figure", "ref": "b3-villus-labelled", "anchor": "s-folds"},


        {"type": "misconception", "id": "villi-and-length",
         "anchor": "s-think", "targets": ["DIET-15", "DIET-16"]},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "diffusion-not-a-push",
         "text": "Small soluble molecules cross the villus wall by diffusion, "
                 "from high concentration in the gut to low concentration in "
                 "the blood. Nothing pushes them. The blood supply keeps the "
                 "concentration low on its side, which is what keeps the "
                 "diffusion going.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # One entry. `fold-builder` is authored inline in `core` and lifted here by
    # `ks3_data/b3/__init__.py::_normalise`, which leaves the `practical` shell
    # behind it.
    "activities": [
        # Design's `#s-think` is STATIC on this page — two quotes and two
        # paragraphs, with nothing to answer — so it is a `confrontation` and
        # not C1's `predict`. That is measured off the markup, not assumed: the
        # section contains no `ks3-options`, no commit and no reveal. It
        # therefore carries no completion contract and is correctly absent from
        # the rail; a stop here could only ever tick on load.
        #
        # ⚠️ Both `answer` strings drop an inline `<a href>` and keep every
        # word. See "What could not be lifted" 1.
        {"id": "villi-and-length",
         "kind": "confrontation",
         "demand": "confront both length errors in one pass: the geometric "
                   "one and the mechanical one",
         "targets": ["DIET-15", "DIET-16"],
         "statements": [
             {"quote": "Villi make the intestine longer.",
              "answer": "They do not add a millimetre of length. Every figure "
                        "in this lesson holds the length fixed at six metres "
                        "— that is the point of the comparison with the hose. "
                        "Villi are projections into the space the tube "
                        "already has, so they add <em>surface</em> without "
                        "adding <em>length</em>, which is a distinction worth "
                        "getting straight because it is the same distinction "
                        "that makes lungs, gills and leaves work. If "
                        "lengthening were the strategy, evolution would have "
                        "taken it: a sixty-metre intestine would need a "
                        "sixty-metre animal to put it in, and folding gets "
                        "the same area into the abdomen you already have."},
             {"quote": "The muscles push the food through the gut wall into "
                       "the blood.",
              "answer": "Peristalsis moves food <em>along</em> the tube; it "
                        "never moves anything <em>through</em> the wall. "
                        "Absorption is diffusion — the same process you met "
                        "in Diffusion, doing biological work here. Glucose "
                        "molecules are moving randomly in all directions all "
                        "the time, and there are more of them in the gut than "
                        "in the blood, so more happen to cross inwards than "
                        "outwards. Nothing pushes them, nothing wants to "
                        "spread, and no muscle is involved. What the body "
                        "does is keep the numbers unequal: blood flows past "
                        "constantly, carrying absorbed glucose away, so the "
                        "concentration on the blood side stays low and the "
                        "net movement continues. Stop the blood flow and "
                        "absorption stops within minutes — not because the "
                        "pushing stopped, but because the difference did."},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # `title` carries Design's finished heading; `_rung_title` strips the
    # "Rung N · " prefix and the engine puts the number back.
    "ladder": {
        "recall": {
            "title": "Rung 1 · What the folding does",
            "q": "Villi increase the small intestine’s…",
            # ⚖️ LENGTH PARITY: PASSES AS DRAWN, and is deliberately not
            # "fixed". Word counts are 1 / 2 / 1 / 2. The correct option is
            # TIED for longest with a distractor, not strictly the longest, so
            # it carries no length tell — and MRB-177 says an option that is
            # not the longest cannot be one. Padding these four one-word
            # answers into sentences would turn a fast recall check into a
            # reading exercise for no gain.
            "options": [
                "length",
                "volume",
                "surface area",
                "muscle strength",
            ],
            "answer": 2,
            "feedback": {
                0: "The length is unchanged — six metres before and after. "
                   "That is exactly the comparison the hose in the hook was "
                   "for.",
                1: "Villi project into the space, so if anything they slightly "
                   "reduce the volume available to food. Volume is not what "
                   "limits absorption.",
                3: "Villi contain no muscle. Peristalsis is done by muscle in "
                   "the wall and moves food along, not through.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A villus keeps its full surface area and its "
                 "one-cell-thick wall, but its blood supply is blocked. What "
                 "happens to absorption there?",
            # ⚖️ LENGTH PARITY: PASSES AS DRAWN. 11 / 9 / 8 / 9 words. The
            # correct option is NOT the longest — option A beats it by two —
            # so there is nothing to fix and nothing to pad.
            "options": [
                "It continues normally — the surface and the thin wall are "
                "intact",
                "It reverses, pushing glucose back into the gut",
                "It speeds up, because nothing is carrying molecules away",
                "It stops within minutes, because the concentration difference "
                "disappears",
            ],
            "answer": 3,
            "feedback": {
                0: "Two of the four features are intact and it still fails. "
                   "Diffusion needs a concentration difference, and only "
                   "flowing blood maintains one.",
                1: "Once the two sides equalise, movement is equal in both "
                   "directions and there is no net transfer. It stops rather "
                   "than reverses.",
                2: "Carrying molecules away is what keeps absorption going. "
                   "Removing it removes the gradient.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the whole design",
            "q": "Explain how three levels of folding, a wall one cell thick "
                 "and a dense blood supply work together to absorb a meal in "
                 "a few hours. Say what each contributes, and why no one of "
                 "them would be enough alone.",
            "field_label": "Your explanation",
            "placeholder": "The folding contributes… the thin wall… the blood "
                           "supply…",
            "success": [
                "Says the folding gives a very large surface area, so many "
                "molecules can cross at once.",
                "Says the one-cell wall gives a short diffusion distance, so "
                "each crossing is fast.",
                "Says the blood supply removes absorbed molecules and so "
                "maintains the concentration difference.",
                "Names diffusion as the process, and says it happens because "
                "of a concentration difference rather than a push.",
                "Explains why one alone is not enough — e.g. a huge area with "
                "no blood flow still stops once the two sides equalise.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            # ⚑ NOTES-B3 flag 19, for Mide's gate: coeliac disease, villous
            # atrophy and iron deficiency on an adequate diet. Confirm the
            # level of detail. Lifted unchanged.
            "q": "In coeliac disease, an immune reaction to gluten flattens "
                 "the villi. Predict what a patient would experience, explain "
                 "it using this lesson, and say why they might be short of "
                 "iron even while eating plenty of it.",
            "field_label": "Your answer",
            "placeholder": "Flattened villi would mean…",
            "success": [
                "Predicts poor absorption and consequences such as mass loss, "
                "tiredness, or poor growth.",
                "Explains it as a loss of surface area — the folding is gone, "
                "so far fewer molecules can cross.",
                "Says iron is eaten but not absorbed, so it never reaches the "
                "blood.",
                "Connects this to the earlier lesson: a deficiency with an "
                "adequate diet, caused by the gut rather than the plate.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "The small intestine is adapted for absorption by a very large "
                "surface area — folds, villi and microvilli — a wall one cell "
                "thick, and a dense blood supply that maintains the "
                "concentration difference. Small soluble molecules cross by "
                "diffusion. Water is absorbed here and in the large intestine.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⊕ MRB-233 (3c), RULED BY MIDE 31 Aug 2026 — THE REVISION EXPLAINER IS OUT.
    #
    # This slot used to hold `how-the-figure-was-revised`, whose text was:
    #     "The figure for intestinal surface area has been revised downwards …
    #      Textbooks for decades gave 200 to 300 m² — a tennis court — a figure
    #      that came from measuring folds and villi on tissue that had been
    #      fixed, dried and stretched. Careful measurements on fresh tissue
    #      published in 2014 put it closer to 30 m², about the floor of a
    #      bedroom … The older number is still in print in many places, so you
    #      will meet both, and the honest thing to say in an exam is that the
    #      area is very large and why, rather than committing to a figure
    #      someone may have learnt differently."
    #
    # It is quoted in full rather than deleted silently, because it was good
    # writing and a future pass WILL want to restore it. Mide's ruling is that
    # ~30 m² STANDS and the page carries NO hedge about textbooks: a KS3
    # student meeting one number on one page does not need to be told that a
    # library book disagrees, and telling them converts a lesson about villi
    # into a lesson about how to sit on a fence. The tennis court leaves with
    # it — it was only ever the OLD figure's comparison, and MUST NOT reappear.
    #
    # ⚠️ THE FIGURE ITSELF DID NOT MOVE. Everything the docstring says about
    # ~30 m² still binds, and the ×3/×5/×4 instrument still lands on it. What
    # went is the commentary about the number's history, not the number.
    #
    # Empty and PRESENT — §5.6: may be empty, never absent. Nothing replaces
    # it; a substitute stretch item was not asked for and would be gap-filling.
    "stretch": [],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # Design heads the card "Ask Mr Badmus AI" and puts the question in the
    # paragraph under it; the CTA points back up at the four features.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to work through why blood flow keeps diffusion "
                      "going?",
              "cta": "Ask about this lesson",
              "anchor": "s-four"},

    # ⊕ MRB-228's `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph here and nothing in it is a safety instruction —
    # it is a note about where the numbers came from and a declaration about a
    # figure that has not been drawn yet. Routing it through `safety_note`
    # would print it in the treatment reserved for "never light a candle
    # without an adult", which devalues the safety line.
    #
    # ⚠️ The figure id keeps its plain text; Design sets it in mono and a foot
    # line is escaped. See "What could not be lifted" 2.
    # ⊕ MRB-257 · C4 / audit 4.6 — the "… is declared in the lesson record
    # as `b5-…`, awaiting illustration" sentence was our own build metadata,
    # printed to a student on eleven pages (§8.10). Cut. The measurement
    # caveat before it is the part that was doing work and it stays.
    "convention_note": "Area figures are approximate and follow the 2014 "
                       "fresh-tissue measurements.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # `analysis-and-evaluation` for the four-features reasoning (remove one,
    # predict the consequence); `scientific-attitudes` for the stretch layer,
    # which is a worked example of a measurement being revised and of what to
    # do when two published figures disagree.
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
