"""B1 L4 — Specialised cells. SYSTEM, and the family's REFERENCE SCREEN.

Authored 14 Aug 2026 against Design's approved page,
`docs/ks3/design-reference/b1/b1-04-specialised-cells.dc.html`, measured in
`docs/ks3/b1-inventory/b1-04-specialised-cells.md`. The inventory is the
specification for everything below and its section numbers are cited rather
than restated.

**32 lesson slots inherit this screen.** `docs/ks3/design-coverage-manifest.md`
§10.1 names this file — not b1-05 — as SYSTEM's approved reference, and SYSTEM
is one of the two families that had no reference screen at all when the
generator's SYSTEM pages were written.

⚠️ **This record supersedes the `specialised-cells` entry in
`ks3_data/biology_b1_cells.py` wholesale. Nothing is shared.** The two pages
teach different lessons: the generator's is *"shape is its job"* built around
DIFFUSION, with a chemistry-borrowed diffusion sim, a `system-parts` dependency
graph, three "Diagram coming soon" slots and ten flip cards. Design's is *"the
same seven parts, tuned"* — four specimens on one bench, a six-value tuning
dial, and a sabotage-and-consequence engine that follows one broken part out
through three scales. They share a title, a slug and a red blood cell. They do
not share a big question, a hook, a misconception, a ladder or a key note.
Eleven blocks against twenty, with no shared block sequence (inventory §3.1.2).

**Every science-bearing string here is LIFTED, not retyped** — from the
reference's `<script data-dc-script>` constants (`CELLS` 401–574, `RUNGS`
576–593, `SELF_RUNGS` 595–616, `RAIL` 384–389, `RAIL_SHORT` 391) and from its
static markup (header 74–76, hook 84–87, `#s-tuned` 107–109, `#s-break`
155–160, `#s-rule` 213–241, `#s-think` 250–255, KEY FACT 261–262, ladder
268–269 and 331, key note 336–337, stretch 346, endmatter 366–371). ~3,840
authored words, and none of it existed in `ks3_data/` before.

⚑ **The CELL-08 paired contract.** `phenomenon["title"]` is quoted in
MRB-209 §3 and in the inventory §4.4, and B1-06 depends on that exact wording
standing. See the ⚑⚑ comment on the field itself before editing it.

Two block types below are NOT in §5.1.1's closed vocabulary — `system-bench`
and `sabotage`. Both were drawn by Design on this approved page before being
written down, which is the order MRB-205 requires, and §5.2 rules out carrying
either as an `activities` entry. They need the amendment `key-fact`, `rule`,
`formula` and `comparison` were given on 13 Aug 2026.

`review_state` is `draft`. Mide is the sole science gate (§5.10), and the ⚑
marks below are the calls this file is holding for him.
"""


# ── #s-tuned's four specimens (inventory §3.2, §7.2) ─────────────────────
#
# Lifted byte-identical from the reference's `CELLS` constant, lines 401–574,
# minus each cell's `sabotages` list — those live in `_SABOTAGE` below,
# because Design draws them in a different section. §7.2's specimen shape is
# exactly this: {id, name, tag, job, where, problem, caption, alt, drawing,
# tuning}.
#
# `dial` is the six-value vocabulary of gap G6. It is NOT a colour:
#
#     GONE   a part the cell destroyed          ┐
#     NONE   a part it never built              ├─ lost      --ks3-alert-tint
#     HALF   a part deliberately incomplete     ┘
#     MORE   a part turned up                   ┐─ gained    --ks3-accent-tint
#     EXTRA  a structure added                  ┘
#     SHAPE  the whole cell reshaped            ── reshaped  --ks3-band
#
# Six dials, three grounds, and the collapse is deliberate: the tint means
# lost / gained / reshaped and does not identify the dial. The WORD carries
# the state (R2), so the polarity map belongs in the renderer and the six-value
# dial belongs here.
#
# ⚖️ SCIENCE, S2 — RESOLVED 14 Aug 2026, on Mide's instruction to resolve it
#   if the science is certain. It is, and the resolution costs one sentence.
#
#   The tension: the nerve cell's EXTRA row names `Fatty sheath` with no part
#   number, where every other row names a numbered part from last lesson, and
#   the page's own key fact says a specialised cell has NO new parts.
#
#   **A myelin sheath is not one of the nerve cell's parts at all.** It is the
#   membrane of OTHER cells — Schwann cells in the peripheral nerves,
#   oligodendrocytes in the brain and cord — wrapped repeatedly around the
#   axon. The neuron grows no new organelle; a different cell wraps itself
#   around it. So the key fact is not contradicted and neither sentence has to
#   give way.
#
#   Better than that, it is the lesson's own idea. b1-04 is a SYSTEM lesson,
#   and "another cell wraps itself around this one so it can do its job" is
#   the SYSTEM point exactly — parts working together — where "this cell grew
#   a part nobody else has" would have been an exception to the rule the
#   lesson is teaching.
#
#   The added sentence names no cell type: Schwann cell and oligodendrocyte
#   are KS4 vocabulary, on the same ground that keeps prokaryote and eukaryote
#   off b1-06. The dial stays `EXTRA` — something extra IS there — and the row
#   still has no part number, which is now the honest signal rather than an
#   anomaly.
#
# `drawing` names a canvas ROUTINE, not an asset (gap G10). The same routine
# draws the healthy cell here and the sabotaged one in #s-break; which variant
# is drawn comes from the sabotage option's own id, so there is no second
# field. Both canvases are 2× buffers over a fixed 900×560 design space, and
# the dark one is the same routine with a dark palette.
_SPECIMENS = [
    {"id": "red",
     "name": "Red blood cell",
     "tag": "In your blood",
     "job": "Carry oxygen from your lungs to every working cell.",
     "where": "Made in bone marrow, then pushed round your body about once "
              "a minute for four months. Twenty-five trillion are in you "
              "right now.",
     "problem": "Nowhere to put the cargo — and not enough surface to load "
                "it through.",
     "caption": "A capillary, with red blood cells folding through it "
                "single file.",
     "alt": "A narrow blood capillary in cross-section with three biconcave "
            "red blood cells passing through it in single file.",
     "drawing": "red",
     "tuning": [
         {"dial": "GONE",
          "part": "Nucleus (3)",
          "why": "Pushed out and destroyed as the cell matures. The space "
                 "it freed is filled with haemoglobin, the red protein that "
                 "oxygen sticks to."},
         {"dial": "SHAPE",
          "part": "Whole cell",
          "why": "A disc squashed in at the middle — biconcave. Same "
                 "volume, much more surface, so oxygen loads and unloads "
                 "faster. It also folds to squeeze through vessels narrower "
                 "than itself."},
         {"dial": "NONE",
          "part": "Mitochondria (4)",
          "why": "It has none either — which means it cannot use any of the "
                 "oxygen it is carrying. A courier that ate the parcel "
                 "would be no use."},
     ]},
    {"id": "root",
     "name": "Root hair cell",
     "tag": "In a plant root",
     "job": "Pull water and dissolved minerals out of the soil.",
     "where": "Just behind the growing tip of every root, in a fuzz of "
              "millions. They last days, then are replaced further along as "
              "the root pushes on.",
     "problem": "Not enough surface. Water is spread thinly over soil "
                "particles, and it has to be collected.",
     "caption": "A root hair cell, with its hair pushed out between soil "
                "particles.",
     "alt": "A root hair cell in root tissue with a long thin hair "
            "extending into soil between soil particles, and arrows showing "
            "water entering.",
     "drawing": "root",
     "tuning": [
         {"dial": "SHAPE",
          "part": "Whole cell",
          "why": "Drawn out into a long thin finger that pushes between "
                 "soil particles. The hair alone can be more than ten times "
                 "the length of the cell body, and almost all of the "
                 "surface is on it."},
         {"dial": "NONE",
          "part": "Chloroplasts (7)",
          "why": "No light reaches a root, so none are built. This cell is "
                 "a plant cell and it is not green."},
         {"dial": "MORE",
          "part": "Mitochondria (4)",
          "why": "Water arrives on its own, but minerals have to be dragged "
                 "in against the flow, and dragging costs energy. So this "
                 "cell keeps a large supply of mitochondria."},
     ]},
    {"id": "sperm",
     "name": "Sperm cell",
     "tag": "A sex cell",
     "job": "Travel a long way, and deliver half a set of instructions.",
     "where": "Made in the testes, and built for one journey it will make "
              "once. Most never arrive.",
     "problem": "Work that never stops, over a distance that is enormous "
                "for one cell.",
     "caption": "A sperm cell: head, mitochondria-packed midpiece, and tail.",
     "alt": "A sperm cell with a rounded head containing a nucleus, a "
            "midpiece full of mitochondria, and a long wavy tail.",
     "drawing": "sperm",
     "tuning": [
         {"dial": "SHAPE",
          "part": "Whole cell",
          "why": "A streamlined head and a long tail that whips from side "
                 "to side. Nothing about this cell is built to sit still."},
         {"dial": "MORE",
          "part": "Mitochondria (4)",
          "why": "Packed into the middle section, right behind the head, "
                 "feeding the tail. Swimming for hours is expensive and "
                 "there is nowhere to refuel."},
         {"dial": "HALF",
          "part": "Nucleus (3)",
          "why": "It carries half a set of chromosomes, not a full set, so "
                 "that it can be added to the half in the egg. This is the "
                 "one cell on the page whose nucleus is deliberately "
                 "incomplete."},
     ]},
    {"id": "nerve",
     "name": "Nerve cell",
     "tag": "In your nervous system",
     "job": "Carry a signal a long way, fast.",
     "where": "From your spine to your toe can be a single cell over a "
              "metre long — the longest cells in your body by a wide margin.",
     "problem": "Too far to travel, and every handover between cells costs "
                "time.",
     "caption": "A nerve cell: branched ends, and a long sheathed cable "
                "between them.",
     "alt": "A nerve cell with branching dendrites, a long axon covered in "
            "segments of fatty sheath with gaps between them, and branched "
            "terminals.",
     "drawing": "nerve",
     "tuning": [
         {"dial": "SHAPE",
          "part": "Whole cell",
          "why": "Drawn out into one enormous thread. Branches at both ends "
                 "collect signals in and pass them on; the middle is pure "
                 "cable."},
         {"dial": "EXTRA",
          "part": "Fatty sheath",
          "why": "A fatty covering wrapped round the cable in segments with "
                 "tiny gaps between them. The signal jumps from gap to gap "
                 "instead of creeping along, which makes it many times "
                 "faster. The sheath is not one of the nerve cell's own "
                 "parts — it is made of other cells wrapped tightly around "
                 "it, which is why it is not on the list of seven."},
         {"dial": "MORE",
          "part": "Mitochondria (4)",
          "why": "Concentrated at the branched ends, where the signal is "
                 "passed to the next cell. That handover is the expensive "
                 "part."},
     ]},
]

# ── #s-break's eight sabotages, grouped by specimen (§3.4, §7.4) ─────────
#
# Lifted byte-identical from `CELLS[].sabotages`. Two per specimen, always.
# `close` / `close_safe` are the two closing paragraphs the `named_conditions`
# switch chooses between; six of the eight pairs are identical strings and
# only red · sphere and nerve · sheath differ.
#
# `predict` is three options and carries NO `correct` field — R3, and it must
# stay that way. `chain` is always three rows and row 1 is emphasised
# POSITIONALLY: it always means "the cell", because every chain starts there.
_SABOTAGE = [
    {"specimen": "red",
     "options": [
         {"id": "sphere",
          "label": "Make it a sphere",
          "what": "Round it out. Same volume of cell, no dimple in the "
                  "middle, and stiff instead of floppy.",
          "predict": [
              "It cannot carry haemoglobin any more",
              "It has less surface, and it can no longer fold through "
              "narrow vessels",
              "It runs out of energy",
          ],
          "caption": "The same cells, rounded out and stiff, jamming at a "
                     "narrowing.",
          "alt": "Spherical red blood cells too large and rigid to pass "
                 "through a narrowing in the capillary.",
          "chain": [
              {"scale": "The cell",
               "text": "Rounding it up gives the same volume the smallest "
                       "possible surface. Oxygen now has less membrane to "
                       "cross, so loading and unloading both slow down."},
              {"scale": "The vessel",
               "text": "The narrowest capillaries are thinner than a red "
                       "blood cell. A floppy disc folds and slips through; "
                       "a stiff ball wedges, and everything behind it stops "
                       "too."},
              {"scale": "The whole body",
               "text": "Tissues past the blockage get less oxygen than they "
                       "need, and the spleen destroys the misshapen cells "
                       "early, so there are fewer of them as well."},
          ],
          "close": "This is not hypothetical. In hereditary spherocytosis "
                   "the red cells really are round and stiff, and the "
                   "result is exactly this: tiredness, and a spleen working "
                   "overtime.",
          "close_safe": "Shape is not decoration here. There are real "
                        "inherited conditions in which red cells come out "
                        "round and stiff instead of flexible discs, and "
                        "tiredness is the first thing people notice."},
         {"id": "nucleus",
          "label": "Give the nucleus back",
          "what": "Let it keep the nucleus it would normally destroy. "
                  "Everything else stays the same.",
          "predict": [
              "It carries less oxygen",
              "It cannot fit through capillaries at all",
              "It stops being able to divide",
          ],
          "caption": "The same cells, each with the nucleus it should have "
                     "given up.",
          "alt": "Red blood cells each containing a nucleus, with visibly "
                 "less haemoglobin packed around it.",
          "chain": [
              {"scale": "The cell",
               "text": "The nucleus occupies space that haemoglobin was "
                       "using. Less haemoglobin means less oxygen carried "
                       "per cell — and the nucleus is in the way of the "
                       "dimple, so the shape suffers too."},
              {"scale": "The blood",
               "text": "The same volume of blood now delivers noticeably "
                       "less oxygen per beat, because every courier in it "
                       "is carrying a smaller load."},
              {"scale": "The whole body",
               "text": "Climbing stairs becomes hard work. Your muscles ask "
                       "for oxygen at a rate the blood can no longer "
                       "supply, so they respire without it and ache."},
          ],
          "close": "It would gain something: with a nucleus it could repair "
                   "itself and live far longer than a hundred and twenty "
                   "days. The body has judged that trade and chosen cargo "
                   "over lifespan.",
          "close_safe": "It would gain something: with a nucleus it could "
                        "repair itself and live far longer than a hundred "
                        "and twenty days. The body has judged that trade "
                        "and chosen cargo over lifespan."},
     ]},
    {"specimen": "root",
     "options": [
         {"id": "short",
          "label": "Shorten the hair",
          "what": "Cut the hair back to a stub, so the cell is a neat block "
                  "like its neighbours. Nothing inside it changes.",
          "predict": [
              "It cannot make food any more",
              "Far less surface is touching soil water",
              "The cell bursts",
          ],
          "caption": "The same cell with the hair cut back to a stub.",
          "alt": "A root hair cell with only a short stub instead of a long "
                 "hair, touching far fewer soil particles.",
          "chain": [
              {"scale": "The cell",
               "text": "Almost all of this cell’s surface was on the hair. "
                       "Cut it off and the area in contact with soil water "
                       "collapses, so far less can cross the membrane per "
                       "second."},
              {"scale": "The root",
               "text": "Multiply that by millions of cells. The root can "
                       "still absorb, but at a fraction of the rate — and "
                       "it is competing with the soil itself, which holds "
                       "water tightly."},
              {"scale": "The whole plant",
               "text": "The leaves lose water faster than the root can "
                       "replace it, so the vacuoles empty and the plant "
                       "wilts. Minerals like nitrate arrive too slowly to "
                       "build new leaves, so growth stops."},
          ],
          "close": "Surface area is the whole point of this cell. It is the "
                   "same idea your lungs and your small intestine are built "
                   "on, at a scale you can see.",
          "close_safe": "Surface area is the whole point of this cell. It "
                        "is the same idea your lungs and your small "
                        "intestine are built on, at a scale you can see."},
         {"id": "mito",
          "label": "Remove the mitochondria",
          "what": "Take out every mitochondrion. The hair, the wall, the "
                  "vacuole and the nucleus all stay exactly as they were.",
          "predict": [
              "Water stops entering",
              "Minerals stop entering, but water keeps coming",
              "The hair shrivels immediately",
          ],
          "caption": "The same cell with no mitochondria — minerals no "
                     "longer crossing in.",
          "alt": "A root hair cell with no mitochondria; water arrows still "
                 "enter but mineral arrows have stopped.",
          "chain": [
              {"scale": "The cell",
               "text": "Water still soaks in on its own, because it moves "
                       "from where there is more to where there is less. "
                       "Minerals do not: there is more nitrate inside the "
                       "cell than in the soil, so pulling more in has to be "
                       "paid for — and the payment came from the "
                       "mitochondria."},
              {"scale": "The root",
               "text": "The plant keeps drinking and stops feeding. Water "
                       "goes up the stem as usual; the dissolved minerals "
                       "it should be carrying are missing."},
              {"scale": "The whole plant",
               "text": "The leaves turn yellow. Chlorophyll needs nitrogen "
                       "and magnesium to build, and neither is arriving — "
                       "so the plant is standing in wet soil, in full sun, "
                       "slowly starving."},
          ],
          "close": "This is the sabotage that separates two things students "
                   "often merge: water gets in for free, minerals have to "
                   "be bought. Yellow leaves on a well-watered plant is the "
                   "classic sign.",
          "close_safe": "This is the sabotage that separates two things "
                        "students often merge: water gets in for free, "
                        "minerals have to be bought. Yellow leaves on a "
                        "well-watered plant is the classic sign."},
     ]},
    {"specimen": "sperm",
     "options": [
         {"id": "notail",
          "label": "Remove the tail",
          "what": "Take the tail off. The head, the nucleus and every "
                  "mitochondrion stay untouched.",
          "predict": [
              "It can no longer move",
              "It can no longer carry chromosomes",
              "It runs out of energy faster",
          ],
          "caption": "The same cell with no tail. Everything else is intact.",
          "alt": "A sperm cell head and midpiece with no tail attached.",
          "chain": [
              {"scale": "The cell",
               "text": "It has the instructions, the energy and the enzymes "
                       "— and no way to move. A cell this small cannot "
                       "drift anywhere useful on its own."},
              {"scale": "The journey",
               "text": "It never gets near the egg. Distance, for something "
                       "this size, is the hardest part of the whole job."},
              {"scale": "The outcome",
               "text": "No fertilisation. Every other adaptation in the "
                       "cell was in perfect order and none of them mattered."},
          ],
          "close": "This is what a system means. Six things right and one "
                   "thing missing is not five-sixths of a working cell — it "
                   "is a cell that fails.",
          "close_safe": "This is what a system means. Six things right and "
                        "one thing missing is not five-sixths of a working "
                        "cell — it is a cell that fails."},
         {"id": "mito",
          "label": "Empty the midpiece",
          "what": "Take out the mitochondria. The tail is still perfectly "
                  "formed and attached.",
          "predict": [
              "The tail falls off",
              "The tail can beat, but not for long",
              "The nucleus stops working",
          ],
          "caption": "The same cell with an empty midpiece — the tail hangs "
                     "limp.",
          "alt": "A sperm cell with an empty midpiece and a limp, nearly "
                 "straight tail.",
          "chain": [
              {"scale": "The cell",
               "text": "A tail is a motor and a motor needs fuel released. "
                       "With no mitochondria there is nothing turning food "
                       "into usable energy, so the tail beats weakly and "
                       "then stops."},
              {"scale": "The journey",
               "text": "It covers a fraction of the distance and stalls. "
                       "There is no refuelling on the way — everything it "
                       "will ever spend was loaded before it set off."},
              {"scale": "The outcome",
               "text": "No fertilisation, for the same reason as before but "
                       "from the other end: the machine is intact and "
                       "unpowered."},
          ],
          "close": "Notice the pattern. The tail and the mitochondria are "
                   "not two adaptations, they are one — a structure and its "
                   "power supply, useless apart.",
          "close_safe": "Notice the pattern. The tail and the mitochondria "
                        "are not two adaptations, they are one — a "
                        "structure and its power supply, useless apart."},
     ]},
    {"specimen": "nerve",
     "options": [
         {"id": "sheath",
          "label": "Strip the fatty sheath",
          "what": "Remove the fatty covering. The cell is the same length, "
                  "and every other part is intact.",
          "predict": [
              "The signal cannot start at all",
              "The signal still travels, but much more slowly",
              "The cell dies",
          ],
          "caption": "The same cell with the sheath stripped away — bare "
                     "cable.",
          "alt": "A nerve cell with a bare, unsheathed axon and no segments.",
          "chain": [
              {"scale": "The cell",
               "text": "With the sheath on, the signal jumps between the "
                       "gaps. Bare, it has to travel the whole length of "
                       "the membrane step by step, and it leaks as it goes."},
              {"scale": "The nerve",
               "text": "The message arrives many times later, and weaker. "
                       "Timing between different nerves goes out of step, "
                       "which matters as much as the delay itself."},
              {"scale": "The whole body",
               "text": "Movement becomes clumsy and slow to correct, and "
                       "vision and balance are affected too, because those "
                       "signals depend on arriving on time."},
          ],
          "close": "The sheath is what makes a metre-long cell practical. "
                   "In multiple sclerosis the body’s own immune system "
                   "damages it, and these are the effects people describe.",
          "close_safe": "The sheath is what makes a metre-long cell "
                        "practical. Speed here is not a bonus; it is the "
                        "difference between catching yourself as you trip "
                        "and hitting the floor."},
         {"id": "short",
          "label": "Make it short",
          "what": "Replace the one long cell with a relay of short ones "
                  "covering the same distance. Every cell keeps its sheath "
                  "and its mitochondria.",
          "predict": [
              "The signal cannot cross the gaps between cells",
              "Every handover adds a delay, so the total time goes up",
              "The signal gets stronger with each cell",
          ],
          "caption": "The same distance covered by a relay of short cells, "
                     "with junctions between them.",
          "alt": "Three short nerve cells in a row spanning the same "
                 "distance, with junction gaps drawn between them.",
          "chain": [
              {"scale": "The cell",
               "text": "Each short cell works perfectly. But at the end of "
                       "every one, the signal has to be handed to the next "
                       "across a junction, and that handover takes "
                       "chemistry, not electricity."},
              {"scale": "The nerve",
               "text": "Chemistry across a junction is slower than a signal "
                       "running down a cable. Two extra junctions is two "
                       "extra delays; a hundred would be a hundred."},
              {"scale": "The whole body",
               "text": "A reflex that should take a fraction of a second "
                       "takes long enough to matter. You would still be "
                       "deciding to let go of the hot pan after you had "
                       "already been burned."},
          ],
          "close": "This is why the nerve cell is shaped the way it is. "
                   "Length is not a curiosity — it is the adaptation, and "
                   "it exists to avoid handovers.",
          "close_safe": "This is why the nerve cell is shaped the way it "
                        "is. Length is not a curiosity — it is the "
                        "adaptation, and it exists to avoid handovers."},
     ]},
]

# ── #s-rule's four problem cards (§3.5) ──────────────────────────────────
#
# The one substantial content payload on the reference page that is NOT in the
# `<script>` block: all four cards are static markup at lines 217–242, so they
# are lifted from there. Card shape is {label, title, body, examples}.
_PROBLEM_CARDS = [
    {"label": "Problem 1",
     "title": "Not enough surface",
     "body": "Everything enters a cell through its surface. Need more in? "
             "Get more surface: a long thin hair, a folded edge, a "
             "flattened disc.",
     "examples": "Root hair cell · red blood cell"},
    {"label": "Problem 2",
     "title": "Too far to travel",
     "body": "A message from your toe to your spine has a metre to cross. "
             "Passing it from cell to cell costs time at every handover, so "
             "one cell is stretched the whole way.",
     "examples": "Nerve cell"},
    {"label": "Problem 3",
     "title": "Work that never stops",
     "body": "Movement costs energy, and energy comes from mitochondria. A "
             "cell that swims, contracts or sweeps all day is crammed with "
             "them.",
     "examples": "Sperm cell · muscle cell · ciliated cell"},
    {"label": "Problem 4",
     "title": "Nowhere to put the cargo",
     "body": "A cell that carries something needs room for it, and room has "
             "to come from somewhere. This is the only problem on the list "
             "solved by throwing a part away.",
     "examples": "Red blood cell"},
]


LESSON = {
    # ── identity — matches ks3_data/structure.py exactly ───────────
    "slug": "specialised-cells",
    "title": "Specialised cells",
    "discipline": "biology",
    "unit": "cells-and-organisation",
    "family": "SYSTEM",

    # ── curriculum position ───────────────────────────────────────
    # B1 is six lessons for six statements after MRB-199, so CELLS.04
    # is owned here and nowhere else. `touches` keeps the seven-part
    # parts list from L3, which this whole lesson is a re-reading of.
    "covers": ["KS3.B.CELLS.04"],
    "touches": ["KS3.B.CELLS.02"],
    "beyond_statutory": False,
    # ⊖ The superseded record carried a third thread, `particles`
    #   (level 3), for its diffusion teaching. Design's page teaches no
    #   diffusion at all — the word does not appear on it — so the
    #   thread and the `assumes` edge to KS3.C.PIS.03 both go.
    "threads": [
        {"id": "structure-function", "level": 2},
        {"id": "cells-and-systems", "level": 2},
    ],
    "typical_year": 7,
    "typical_minutes": 45,

    # ── progression edges ─────────────────────────────────────────
    # Both `references` targets are B1 lessons that exist after MRB-199
    # dropped `stem-cells-and-meristems`; the endmatter Design drew
    # points at exactly these two files (reference lines 360–361), and
    # both resolve to real pages, which is what MRB-209's link gate
    # wants. No `why` on either edge: Design's card carries the two
    # links and no prose, and the `why` RENDERS to the student (§8.10).
    "requires": ["animal-and-plant-cells"],
    "assumes": [],
    "references": [
        {"unit": "B1", "lesson": "levels-of-organisation"},
        {"unit": "B1", "lesson": "unicellular-organisms"},
    ],
    # ⚑ `ks4_links` is EMPTY so that `ks4_becomes` can render: §4.8.1 D
    #   gives the third endmatter card to the prose only when there are
    #   no links, and Design's card is prose (reference line 366). The
    #   cost is real and is raised in the report — the machine-readable
    #   bridge edges to `cell-specialisation` and `transport-in-cells`
    #   are lost, and the prose names those destinations in words only.
    "ks4_links": [],
    "ks4_becomes": "Cell differentiation, exchange surfaces and surface "
                   "area to volume ratio, and active transport at the root "
                   "hair.",

    # ── the teaching payload ──────────────────────────────────────
    "big_question": "One cell in your body throws its nucleus away. Why "
                    "would anything do that?",

    # The hook, reference lines 82–103. Ink-dark, and it ends in a
    # commitment that is NEVER marked (R3): there is no `answer` key
    # here and there must never be one. `options` + `reveal` are §5.2's
    # gap G13, carried inside `phenomenon` because §4.8.2 already
    # extends `phenomenon` for hook furniture (`tiles`, `art`,
    # `figures`) and b1-03's gap list folded its own hook options in
    # here too. The reveal is Law 4 — hidden until a commitment lands.
    #
    # ⚑⚑ CONTRACT-BEARING — DO NOT REWORD `title`. §4.4 of the
    #    inventory: B1-06 resolves the apparent contradiction between
    #    this sentence and a bacterium that has no nucleus and divides
    #    every twenty minutes. The red cell DESTROYED its nucleus; a
    #    bacterium NEVER HAD ONE. Reword this line without re-reading
    #    B1-06 against it and the contradiction returns with nothing on
    #    the page to catch it. `prompt` ratifies it ("All still true")
    #    and cannot be separated from it.
    #
    #    `pairs_with` is the claim side of that contract, mirroring the
    #    field B1-06 put on its CELL-13 entry — which quotes the line
    #    below byte-identically as its `claim`. Inventory §4.4 records
    #    that the register has NO field for a cross-lesson
    #    claim/qualification pair, so nothing in the build would notice
    #    if one shipped without the other or either were edited alone.
    #    Declared from both ends, the pair is at least findable.
    "phenomenon": {"kind": "narrative",
                   "eyebrow": "Start here",
                   "title": "Last lesson: no nucleus, no instructions, no "
                            "repair, no dividing.",
                   "prompt": "All still true. And yet: a red blood cell "
                             "starts out with a nucleus, in the marrow "
                             "inside your bones, and as it matures it "
                             "pushes that nucleus out and destroys it. It "
                             "can then never repair itself and never "
                             "divide, and it lasts about a hundred and "
                             "twenty days. Your body does this "
                             "deliberately, two million times a second.",
                   "commit": "Something must be worth all that. What does "
                             "losing the nucleus buy the cell?",
                   "options": [
                       "It can fit through narrower vessels",
                       "Room — space for the cargo it carries",
                       "It saves energy by not using the nucleus",
                       "Nothing. It is a mistake in the process",
                   ],
                   "reveal": "Hold it. Every cell below is the same trade, "
                             "made differently: something given up, "
                             "something gained, and a shape that answers "
                             "one physical problem.",
                   "pairs_with": {"lesson": "unicellular-organisms",
                                  "relation": "qualified-by",
                                  "qualifier": "CELL-13"}},

    # ── misconceptions ────────────────────────────────────────────
    # THREE entries, TWO of them quoted. Design draws two quotes in
    # #s-think and neither is in the register, so both are minted;
    # CELL-05 is kept unquoted because the register already owns it
    # HERE and this lesson still kills it outright — the hook is four
    # sentences about a cell that has no nucleus. It renders nothing,
    # because what renders is keyed off the activity's `statements`.
    #
    # ⚑ CELL-14 AND CELL-15 ARE NEW IDS AND THE REGISTER HAS NO ROWS
    #   FOR THEM. The register runs CELL-01..CELL-12 and B1-06 has
    #   already minted CELL-13 in this same batch, which is why these
    #   are 14 and 15 rather than 13 and 14. The rows are NOT written
    #   here: six sibling lessons minting into one hand-maintained file
    #   at once is how ids collide. One reconciling edit, raised in the
    #   report.
    #
    # The register's `statement` is the DIAGNOSTIC wording and the
    # block's `quote` is the student's voice. For CELL-05 they differ
    # and both are needed; for the two minted here they are the same
    # sentence, because Design's quote IS the belief. Same convention
    # as B1-06, which is this lesson's contract partner.
    #
    # `elicited_by` names the BLOCK that surfaces each belief, not an
    # activity id — §5.2 is explicit that the bench and the sabotage
    # engine are instruments and cannot be `activities` entries, so
    # there is no activity slug to name. `confronted_by` still names a
    # real activity, which is what Law 3's gate in verify_ks3.py reads.
    "misconceptions": [
        {"id": "CELL-14",
         "statement": "Specialised cells are made of different parts from "
                      "ordinary cells.",
         "elicited_by": "s-tuned",
         "confronted_by": "same-seven-tuned"},
        {"id": "CELL-15",
         "statement": "A red blood cell is not really a cell, then.",
         "elicited_by": "s-hook",
         "confronted_by": "same-seven-tuned"},
        {"id": "CELL-05",
         "statement": "Every cell in your body has a nucleus.",
         "elicited_by": "s-hook",
         "confronted_by": "same-seven-tuned"},
    ],

    # ── vocabulary (§5.4) ─────────────────────────────────────────
    # Design draws NO keyword block on this page, so nothing here
    # renders as a block — the field feeds term marking and the KS3
    # tutor prompt (§5.9). Three definitions are carried over verbatim
    # from the superseded record because they still hold word for word;
    # `diffusion` is dropped with the diffusion teaching. The last two
    # are written here, from the page's own words, and are flagged for
    # examiner review with everything else in this file.
    "vocabulary": [
        {"term": "specialised",
         "definition": "Built to do one particular job very well.",
         "note": "The price is that a specialised cell is usually no good "
                 "at anything else."},
        {"term": "adaptation",
         "definition": "A feature that helps something do its job.",
         "note": "Here the adaptation is a feature of one single cell. "
                 "Later you will meet adaptations of whole organisms."},
        {"term": "surface area",
         "definition": "The total amount of outside surface something has.",
         "note": "Squash a cell flat, or grow it a long thin hair, and its "
                 "surface area goes up without much more inside to supply."},
        {"term": "haemoglobin",
         "definition": "The red protein that fills a red blood cell and "
                       "that oxygen sticks to.",
         "note": "It is what the nucleus made room for."},
        {"term": "biconcave",
         "definition": "Dished in on both sides — a disc squashed at the "
                       "middle.",
         "note": "Same volume as a ball, much more surface, and floppy "
                 "enough to fold."},
    ],

    # ── figures (§4.10) ───────────────────────────────────────────
    # EMPTY, and that is a statement rather than an omission. Design
    # carries no <figure> and no pending slot on this page: both
    # diagrams are LIVE CANVASES drawn from the data above (gap G10),
    # named per specimen by `drawing` and per sabotage by the option's
    # own id. The superseded record asked for three schematics that
    # nobody has to source now.
    "figures": [],

    # ── the progress rail (§4.8.1 A, gap G1) ──────────────────────
    # Four stages. `short` is the side rail's mono label (≤6 chars),
    # `label` the sub-1340px top bar's sentence-case one; both are
    # authored and neither is derivable from a block title.
    #
    # ⚑ `threshold` on s-break is F21/C2: the page holds EIGHT
    #   sabotages (4 specimens × 2) and the stage ticks at FOUR, so the
    #   student can see "4 of 8 sabotages run" beside a ticked stage.
    #   That is authored, not a bug, and `done_when` alone cannot say
    #   it. §4.8.1 A's shape has no `threshold` yet and r_rail() drops
    #   unknown keys, so this is inert until the renderer reads it.
    #
    # Nothing is ticked on load and both variants are completion-based
    # — MRB-208's ruling, which corrects the delivered top bar (F2).
    "rail": [
        {"anchor": "s-hook",
         "short": "HOOK",
         "label": "The trade",
         "done_when": "committed"},
        {"anchor": "s-tuned",
         "short": "TUNED",
         "label": "Same seven parts",
         "done_when": "all_specimens_seen"},
        {"anchor": "s-break",
         "short": "BREAK",
         "label": "Break it on purpose",
         "done_when": "predictions_made",
         "threshold": 4},
        {"anchor": "s-ladder",
         "short": "LADDER",
         "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the KEY FACT box (§4.8.1 B, gap G3) ───────────────────────
    # One box, top level, between the misconception and the ladder —
    # a sibling of the sections, not a child of one (F19). Band ground
    # per drift 5, and it grows no badge, letter or mark, because
    # --ks3-band is also the chosen-WRONG ladder ground.
    "key_facts": [
        {"text": "A specialised cell has no new parts. The same seven are "
                 "turned up, turned down, or reshaped.",
         "placement": "top-level",
         "ground": "band",
         "eyebrow": "Key fact"},
    ],

    # ── the tutor card (§4.8.1 C, gap G12) ────────────────────────
    # Design's CTA is a LIVE anchor into this page's own statement
    # panel, so the §8.8 <span> objection does not apply: #s-rule is a
    # real destination on the page it is printed on.
    "tutor": {"prompt": "Not sure which problem a cell is solving?",
              "cta": "Ask about this lesson",
              "anchor": "s-rule"},

    # ── the named-conditions switch (gap G9) ──────────────────────
    # ⚑⚑ MIDE'S CALL, S1 — NOT CODE'S. True ships the `close` text,
    #    which names HEREDITARY SPHEROCYTOSIS (red · sphere) and
    #    MULTIPLE SCLEROSIS (nerve · sheath) to Year 7–9 students.
    #    False ships `close_safe`, which describes both conditions
    #    without naming either. Six of the eight pairs are identical
    #    strings, so the switch only moves those two.
    #
    #    ⚖️ RULED FALSE by Mide, 14 Aug 2026. Design's delivered default
    #    was True and shipped both names. Naming a specific inherited
    #    condition and a specific neurological disease to a Year 7 in a
    #    cell-biology lesson is not what either sabotage is teaching —
    #    the science point is that shape and insulation are load-bearing,
    #    and `close_safe` makes it without handing a twelve-year-old a
    #    diagnosis to take home. Design had already written the copy.
    #
    #    Resolved at BUILD time, not at runtime. Design's page keeps both
    #    strings and picks between them from a prop, which leaves the
    #    named condition sitting in the page source whichever way the
    #    switch is set. `r_sabotage` emits one string, and it raises if a
    #    sabotage has no `close_safe` to emit — there is no silent
    #    fallback to the named one.
    "named_conditions": False,

    # ── core blocks, in document order ────────────────────────────
    # Eight blocks against the generator's twenty. Design's shape is
    # hook → bench → sabotage → rule → misconception → key fact →
    # ladder → key note, and the two instruments sit at the demand
    # peaks rather than being parked at the top (§5.1.1).
    #
    # ⚑ `anchor` carries the DOM id on EVERY id-bearing block (gap G2),
    #   and every one takes scroll-margin-top: 92px whether or not the
    #   rail references it. `anchor` is used rather than `id` because
    #   `id` already means the ACTIVITY id on activity-backed blocks
    #   (r_activity reads block['id']); one key, one meaning. The
    #   current _id_attr() reads block['id'] and needs widening.
    #
    # ⚑ `system-bench` and `sabotage` are NOT in §5.1.1's closed
    #   fourteen-type vocabulary and are NOT in BLOCK_RENDERERS. Both
    #   were drawn by Design on this approved page — which is the order
    #   MRB-205 requires — and §5.2 rules out carrying them as
    #   `activities`. They need the same amendment `key-fact`, `rule`,
    #   `formula` and `comparison` got on 13 Aug.
    "core": [
        # 1 · the hook. Ink-dark, accent shadow, commit + gated reveal
        #     all INSIDE the dark block — not split into a light check.
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # 2 · THE SYSTEM FLAGSHIP (gap G5). One bench, four specimens,
        #     a three-row tuning readout that never changes shape, and
        #     a live canvas. `dial` is the six-value vocabulary of gap
        #     G6 — GONE / NONE / HALF / MORE / EXTRA / SHAPE — which
        #     the renderer collapses to a THREE-value polarity for
        #     colour: lost (alert-tint) / gained (accent-tint) /
        #     reshaped (band). Six dials, three grounds, on purpose:
        #     the tint means lost-gained-reshaped and does not identify
        #     the dial. Every state carries a word and the word IS the
        #     state (R2).
        #
        #     `drawing` names a routine, not an asset (gap G10). The
        #     same routine draws the healthy cell here and the
        #     sabotaged one in #s-break; the sabotage option's own id
        #     is what selects the broken variant, so no extra field.
        #     `start` is the delivered `startCell` prop, and the
        #     starting specimen counts as seen on load — three more to
        #     visit before TUNED ticks.
        {"type": "system-bench",
         "anchor": "s-tuned",
         "eyebrow": "The bench · same seven parts",
         "heading": "Nothing new was added. Something was turned up, and "
                    "something was turned down.",
         "prompt": "These are the same seven parts you numbered last "
                   "lesson. Pick a cell and read what has been tuned — "
                   "and what the tuning is for.",
         "start": "red",
         "specimens": _SPECIMENS},

        # 3 · THE SABOTAGE ENGINE (gaps G7/G8). Dark practical, blue
        #     shadow. Break one part, predict what fails, then follow
        #     the failure OUT through three scales — which is where
        #     SYSTEM earns its name against a labelling exercise.
        #
        #     `predict` is three options and is NEVER marked: there is
        #     no `answer` key and there must never be one (R3). The
        #     student's pick is echoed back verbatim above the chain
        #     ("You said: …"), which is this delivery's half-fix for
        #     F4 — echoed, not revisable, not marked.
        #
        #     `chain` is always three rows and row 1 is emphasised
        #     POSITIONALLY, not semantically: it always means "the
        #     cell", because every chain in the data starts there.
        #
        #     §7.4 draws this block per specimen ({'specimen': 'red',
        #     'options': [...]}). Design draws ONE section whose whole
        #     payload swaps with the bench's current specimen, so the
        #     block takes a list of §7.4-shaped groups rather than four
        #     blocks — four would put four sections on a page that has
        #     one. Nothing inside a group is changed.
        {"type": "sabotage",
         "anchor": "s-break",
         "bench": "s-tuned",
         "eyebrow": "Break it on purpose",
         "heading": "Take the adaptation away",
         # {specimen} interpolates the bench's current cell name — the
         # delivered string is '… one thing about ' + cellName + ', say
         # …'. It is the one authored line on the page that is not a
         # flat string, and the token is the only edit made to it.
         "lede": "Knowing the parts is not knowing the system. Sabotage one "
                 "thing about {specimen}, say what you think breaks first, "
                 "and then follow it out from the cell to the whole "
                 "organism.",
         "commit": "Commit first. What breaks first?",
         "specimens": _SABOTAGE},

        # 4 · the statement panel (gap G4). Band ground, 3px ink, no
        #     shadow; the statement takes drift 3's RULED clamp
        #     clamp(28px, 3.9vw, 44px) at a 24ch measure, the sub-line
        #     56ch. Four cards of {label, title, body, examples} —
        #     which is NOT the {term, gloss} + close shape r_rule()
        #     renders today, and the sub-line sits BEFORE the cards
        #     where `close` renders after them. Raised in the report.
        #     All four cards are static markup on the reference page
        #     (lines 217–242), so they are lifted from there.
        {"type": "rule",
         "anchor": "s-rule",
         "eyebrow": "What settles it",
         "statement": "Every adaptation is an answer to a physical problem.",
         "sub": "There are only a few problems a single cell can be up "
                "against. Once you can name the problem, the shape stops "
                "being a fact to memorise and becomes the obvious solution.",
         "cards": _PROBLEM_CARDS},

        # 5 · the misconception block — ONE block, TWO misconceptions,
        #     split by an --ks3-alert-border rule (§4.8.2's
        #     `statements`). The second is the one this lesson's own
        #     hook creates, answered in the same block.
        {"type": "misconception", "id": "same-seven-tuned",
         "anchor": "s-think"},

        # 6 · the KEY FACT box. `ref` indexes `key_facts`; it renders
        #     as a top-level sibling here, with no anchor of its own.
        {"type": "key-fact", "ref": 0},

        # 7 · the ladder, and 8 · the key note.
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the stretch layer (§5.6) ──────────────────────────────────
    # ONE bare paragraph in a violet layer body. Visible and opt-in to
    # every student, never allocated. The generator nests two blocks
    # inside its layer where Design draws one bare <p> (D10) — that is
    # a renderer divergence, not a data one.
    "stretch": [
        {"type": "explainer",
         "id": "the-maintenance-bill",
         "text": "Something has to keep replacing them, and it does: about "
                 "two million new cells a second, from marrow in your ribs, "
                 "spine, hips and the ends of your long bones. That is the "
                 "hidden cost of the trade — cargo space bought with a "
                 "maintenance bill handed to the rest of the body. Why keep "
                 "paying it? Because about a quarter of all your cells are "
                 "red blood cells, and every one would otherwise carry a "
                 "third less oxygen."},
    ],

    # Present-but-empty by design (§11 decision 4). Empty renders
    # NOTHING — no section, no heading, no placeholder.
    "support": [],

    # ── activities ────────────────────────────────────────────────
    # ONE, and that is not an omission. The bench and the sabotage
    # engine are instruments with their own content payloads, and §5.2
    # rules that `activities` cannot carry them; the hook's commitment
    # lives inside `phenomenon`. What is left is the confrontation,
    # which Law 3 requires and verify_ks3.py's gate reads by id.
    #
    # Statement shape is {targets, quote, answer}, matching B1-06.
    # (B1-05 uses {targets, body} and looks the quote up from the
    # register instead — a divergence between siblings, raised in the
    # report rather than resolved unilaterally here.)
    #
    # `quote` carries NO curly quotes: _misconception_quote() already
    # wraps in “ ”, and the reference's literal “…” in the markup is
    # what that reproduces. `statements` is §4.8.2's extension for the
    # two-misconception block, which the single-`statement` shape
    # cannot express.
    "activities": [
        {"id": "same-seven-tuned",
         "kind": "confrontation",
         "demand": "explain",
         "targets": ["CELL-14", "CELL-15"],
         "statements": [
             {"targets": "CELL-14",
              "quote": "Specialised cells are made of different parts from "
                       "ordinary cells.",
              "answer": "There is no such thing as an ordinary cell. Every "
                        "cell in the four you just looked at is built from "
                        "the same seven parts as the cheek cell — the "
                        "tuning is what differs. A nerve cell has a "
                        "nucleus, cytoplasm, a membrane and mitochondria; "
                        "so does a sperm cell; so does a root hair cell, "
                        "plus its wall and its vacuole. Nothing on the "
                        "parts list is new. What changes is how much of "
                        "each, and what shape the whole thing is pulled "
                        "into."},
             {"targets": "CELL-15",
              "quote": "A red blood cell is not really a cell, then.",
              "answer": "It is. It was made in the marrow with a full "
                        "nucleus and everything else, and it gave the "
                        "nucleus up on the way to the job — the way you "
                        "might take the back seats out of a van. It still "
                        "has a membrane, still has cytoplasm, still carries "
                        "oxygen for about a hundred and twenty days. What "
                        "it cannot do is repair itself or divide, and that "
                        "is the price of the room it gained."},
         ]},
    ],

    # ── the mastery ladder (§5.8, §5.8.1) ─────────────────────────
    # Four rungs. Two the page marks, two the student marks, and all
    # four count — the score reads out of 4 (MRB-184). Rungs 1 and 2
    # carry a per-option `correction` for every wrong option and none
    # for the right one, which is what `feedback` keyed by option
    # index expresses; the correct answer's feedback word is
    # "Correct." with no trailing prose.
    #
    # ⚑ `title`, `field_label` and `placeholder` are AUTHORED strings
    #   on Design's page ("Rung 1 · Name the job", "Your
    #   explanation", "The long thin shape means…") and the current
    #   renderer derives the first from LADDER_RUNGS ("1 · Recall")
    #   and hard-codes the second ("Write your answer"). They are
    #   carried here because the page is the specification; the
    #   renderer has to read them. Raised in the report.
    #
    # ⚑ "Retry my misses" also clears rungs 1 and 2, which its own
    #   note denies (F23). The page wins: reproduce both the behaviour
    #   and the note, and flag the copy to Design rather than fix it.
    "ladder": {"recall": {"title": "Rung 1 · Name the job",
                          "q": "A cell is long and thin, has a wall and a "
                               "vacuole, no chloroplasts, and an unusually "
                               "large number of mitochondria. What is it "
                               "built for?",
                          "options": [
                              "Carrying oxygen round the body",
                              "Absorbing water and minerals from soil",
                              "Trapping light to make food",
                              "Carrying a signal from your spine to your toe",
                          ],
                          "answer": 1,
                          "feedback": {0: "That cell has no wall and no "
                                          "vacuole — and no mitochondria at "
                                          "all, so that it does not use the "
                                          "oxygen it carries.",
                                       2: "Then it would be full of "
                                          "chloroplasts. This one has none, "
                                          "which is the clue that no light "
                                          "reaches it.",
                                       3: "A nerve cell is an animal cell. "
                                          "No animal cell has a wall or a "
                                          "permanent vacuole."}},
               "apply": {"title": "Rung 2 · The one that catches people",
                         "q": "A student says a red blood cell is not "
                              "really a cell, because it has no nucleus. "
                              "What is the best reply?",
                         "options": [
                             "They are right — it is just a bag of "
                             "haemoglobin",
                             "It has a nucleus, it is only too small to see",
                             "It started with a nucleus and destroyed it as "
                             "it matured, which is why it cannot repair "
                             "itself and lasts about 120 days",
                             "It keeps the nucleus but switches it off",
                         ],
                         "answer": 2,
                         "feedback": {0: "It has a membrane and cytoplasm "
                                         "and it does a job for four "
                                         "months. Having no nucleus is a "
                                         "cost it paid, not proof it was "
                                         "never a cell.",
                                      1: "It genuinely has none. This is "
                                         "not a limit of the microscope — "
                                         "the nucleus is pushed out and "
                                         "destroyed while the cell matures.",
                                      3: "A switched-off nucleus would "
                                         "still take up the space. The "
                                         "whole point of losing it is the "
                                         "room that the haemoglobin then "
                                         "fills."}},
               "explain": {"title": "Rung 3 · Explain it",
                           "q": "A root hair cell is drawn out into a long "
                                "thin hair. Explain how that shape helps "
                                "the whole plant, and why a rounder cell of "
                                "the same volume would be worse.",
                           "field_label": "Your explanation",
                           "placeholder": "The long thin shape means…",
                           "success": [
                               "Says the long thin shape gives a much "
                               "larger surface area than a round cell of "
                               "the same volume.",
                               "Says water and dissolved minerals can only "
                               "enter through the surface, so more surface "
                               "means a faster rate of absorption.",
                               "Says the hair reaches in between soil "
                               "particles, where the water actually is.",
                               "Connects it to the whole plant: enough "
                               "water to stay firm and enough minerals to "
                               "keep growing.",
                           ]},
               "produce": {"title": "Rung 4 · Take it somewhere new",
                           "q": "Design a cell whose job is to line the "
                                "inside of your windpipe and stop dust "
                                "reaching your lungs. Say which of the "
                                "seven parts you would turn up, what shape "
                                "you would give the cell, and what would go "
                                "wrong in the whole body if that shape "
                                "stopped working. You may invent a "
                                "structure — but say which problem it "
                                "solves.",
                           "field_label": "Your design",
                           "placeholder": "Shape: … Turned up: … If it "
                                          "failed: …",
                           "success": [
                               "Gives the cell something on its exposed "
                               "surface that can move dust along — a fringe "
                               "of hair-like structures, or your own "
                               "equivalent, with a reason.",
                               "Turns up mitochondria, because constant "
                               "sweeping is constant work.",
                               "Says the surface facing the airway is the "
                               "one that matters, and the cells sit in a "
                               "sheet so they can sweep together in one "
                               "direction.",
                               "Follows a failure out to the whole body: "
                               "dust and mucus stay in the airway instead "
                               "of being cleared, so infections take hold.",
                           ]},
               "retry_note": "Clears the ticks on rungs 3 and 4 and keeps "
                             "what you wrote.",
               "sub": "Four rungs. Two the page marks, two you mark."},

    # ── the key note (§5.1.1 n+2) ─────────────────────────────────
    # Ink-dark, alert-yellow shadow. Its label is a p.ks3-eyebrow on
    # Design's page, not an <h2> (F16) — a renderer divergence.
    "key_note": "A specialised cell is not built from different parts. It "
                "is the same seven, tuned — more of one, none of another, "
                "and a shape that answers one physical problem.",

    # ── working scientifically and governance ──────────────────────
    # No legal line at all on this page (F20), and no `safety_note`:
    # nothing here is a hazard and the slot stays unset, which is C3's
    # recommendation — the field is optional and unset emits nothing.
    "ws": ["analysis-and-evaluation"],
    "review_state": "draft",
}
