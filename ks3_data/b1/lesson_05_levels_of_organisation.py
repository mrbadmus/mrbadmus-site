"""B1 · L5 — Levels of organisation (SYSTEM), as Design drew it.

Built from `docs/ks3/design-reference/b1/b1-05-levels-of-organisation.dc.html`
(929 lines, delivered unmodified) against the measured inventory in
`docs/ks3/b1-inventory/b1-05-levels-of-organisation.md`. **The approved page is
the specification.** Every authored string below was lifted from it verbatim —
none of it was retyped, none of it is generated, and none of it may be edited
without a new examiner pass (§5.10).

⚠️ **This is not the lesson the generator used to emit.** MRB-203 names this
page by name as one of the two Mide rejected. Design's version teaches the same
statement (`KS3.B.CELLS.06`) through a *plant* — whole plant → shoot → leaf →
palisade layer → palisade cell — where the superseded record taught it through a
human digestive system. Different big question, different hook, different
misconception wording, different ladder, different key note. All ~2,630 of
Design's words are new; the superseded record's ~1,900 are displaced, not
ported. That displacement is Mide's call (inventory §8(b) S4) and it is recorded
here rather than hidden: the old record still stands in
`ks3_data/biology_b1_cells.py` until he rules.

**What survives from the superseded record**, and only this:

- the identity block (slug, unit, family, covers, threads, typical_*) — it is
  the same lesson slot in `structure.py`;
- `vocabulary` — three terms whose definitions Design's page does not
  contradict. Design draws no keyword block, so **none of it renders**; it is
  kept because §10.2's per-lesson gate requires `vocabulary` non-empty and
  because a term register outlives one page's layout;
- the misconception **ids** `CELL-06` / `CELL-07`, which B3, B4 and B9 already
  point back at (`docs/ks3/misconception-register.md`). Their *statements* are
  now Design's wording, which is a register edit that has to follow.

Three instruments are authored as inline `core` blocks — `zoom-ladder`,
`sort-task`, `removal-cases` — because that is how Design draws them: each owns
a whole content payload and a page position. `ks3_data/b1/__init__.py`
normalises them into `activities[]` when it collects the six records, leaving a
`practical` / `check` / `practical` shell with its anchor behind, so §5.1.1's
block vocabulary stays closed at fourteen and §10.2's `ok_vocabtypes` gate
passes untouched. Read the payloads here and the normalisation there.

`illustration_palette` IS new against §4.8 and needs the amendment — see its
note at the foot of this record.
"""


LESSON = {
    # ---- identity ------------------------------------------------------
    # Matches ks3_data/structure.py's B1 slot exactly. The slug is permanent
    # (§8.4); the title is the slot's.
    "slug": "levels-of-organisation",
    "title": "Levels of organisation",
    "discipline": "biology",
    "unit": "cells-and-organisation",
    "family": "SYSTEM",

    # ---- curriculum position -------------------------------------------
    "covers":      ["KS3.B.CELLS.06"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 3},
                    {"id": "structure-function", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 45,

    # ---- progression edges ----------------------------------------------
    # `requires` and `references` are read straight off Design's endmatter:
    # "Before this lesson" links b1-04, "Connects to" links b1-06 and b1-01.
    # ⚑ §4.8 glosses `references` as *cross-discipline* reuse (§4.6). Design
    #   uses that card for two same-unit lessons, so either the gloss widens or
    #   the card needs its own field. Rendering is identical either way.
    "requires":    ["specialised-cells"],
    "assumes":     [],
    "references":  ["unicellular-organisms", "life-processes"],

    # ⚑ `ks4_links` is EMPTY on purpose, and it costs two real edges.
    #   §4.8.1 D: `ks4_becomes` renders in the endmatter's third card *only
    #   when `ks4_links` is empty*. Design writes that card as prose, so the
    #   list has to be empty for the page to render as drawn. The two edges the
    #   superseded record carried are parked here so nothing is lost:
    #
    #       biology/organisation/principles-of-organisation
    #       biology/organisation/plant-tissues
    #
    #   Recommended fix (Mide's / §4.8's, not taken here): let `ks4_becomes`
    #   win when it is present, so a lesson can keep its bridge edges *and*
    #   render Design's prose. Today those two things are mutually exclusive.
    "ks4_links":   [],
    "ks4_becomes": "Organ systems in detail — digestion, circulation, gas "
                   "exchange — and tissue engineering.",

    # ---- the teaching payload -------------------------------------------
    "big_question": "A dish of living stomach cells cannot digest a sandwich. "
                    "Your stomach can. What is the difference?",

    # The hook COMMITS inside the dark block (inventory §3.2): four options
    # and one gated reveal, all inside `#s-hook`. There is no separate light
    # check block and no `answer` key — R3 forbids marking a hook, and the
    # reveal is a single unbranched string served identically whichever option
    # is pressed. ⚑ That includes option D, the one this lesson exists to
    # refute, and it opens "Keep it." — inventory F27 / S3, Design's and Mide's
    # call. Reproduced as delivered.
    "phenomenon": {
        "kind": "demo",
        "eyebrow": "Start here",
        "title": "Same cells. Same number. One digests a meal; the other does "
                 "nothing.",
        "prompt": "Scientists can grow real stomach cells in a dish. They "
                  "live for weeks, making acid and enzymes. Put a sandwich in "
                  "the dish and it sits there. Put it in a stomach and twenty "
                  "minutes later it is gone.",
        "commit": "Nothing is missing from the dish. So what has the stomach "
                  "got?",
        "options": [
            "More cells",
            "The cells arranged into layers that work together",
            "Different kinds of cell",
            "Nothing — the dish just needs more time",
        ],
        "reveal": "Keep it. The five levels below are not five sizes of the "
                  "same thing — each one can do something the level under it "
                  "cannot, and that is the only reason the ladder exists.",
    },

    # ---- misconceptions (§5.3) -------------------------------------------
    # Design carries BOTH in ONE block, both open, split by an alert-border
    # rule (§4.8.2's `statements` extension). The ids are the register's and
    # stay; the statements are Design's wording and replace the register's,
    # which `docs/ks3/misconception-register.md` must follow.
    # The renderer wraps a statement in “ ” itself, so neither carries quotes.
    "misconceptions": [
        {"id": "CELL-06",
         "statement": "An organ is just a bigger tissue.",
         "elicited_by": "s-hard",
         "confronted_by": "organ-is-not-a-bigger-tissue"},
        {"id": "CELL-07",
         "statement": "Blood can’t be a tissue — it’s a liquid.",
         "elicited_by": "s-hard",
         "confronted_by": "organ-is-not-a-bigger-tissue"},
    ],

    # ---- vocabulary (§5.4) -----------------------------------------------
    # Carried from the superseded record because §10.2 requires it non-empty
    # and none of it contradicts Design. ⚠️ NONE of it renders: Design's page
    # has no keyword block and no flip card at all — three reference screens,
    # zero flip cards (inventory §3.1.3, R4 still unarbitrated).
    "vocabulary": [
        {"term": "tissue",
         "definition": "A group of similar cells working together to do one job.",
         "note": None},
        {"term": "organ",
         "definition": "A group of different tissues working together to do one "
                       "job.",
         "note": "A stomach is an organ. So is a leaf — plants have them too."},
        {"term": "organ system",
         "definition": "A group of organs working together to do one big job.",
         "note": "Your digestive system is a chain of organs, from your mouth to "
                 "your intestines."},
    ],

    # ---- figures (§4.10) --------------------------------------------------
    # Empty, and that is a statement rather than an omission: Design draws no
    # <figure> anywhere. The levels are DRAWN, live, on one 1800×1000 canvas
    # (see `core` → zoom-ladder). The superseded record's three "Diagram coming
    # soon" placeholders leave the lesson with it, and with them three rows of
    # docs/ks3/diagram-manifest.md.
    "figures": [],

    # ---- navigation and framing (§4.8.1) ---------------------------------
    # Five stages. `short` ≤6 chars for the 104px side rail; `label` is the
    # sub-1340px top bar's. Both label sets are authored and neither is
    # derivable from a block title.
    #
    # ⚑ `s-hard` watches the reveal, not the work (inventory F25). Its gate is
    #   transitively honest — "Open the answers" is itself locked until all
    #   eight are placed — but the stage is one relaxed guard away from ticking
    #   for free. `all_placed` + threshold 8 is the better predicate and it is
    #   NOT taken here, because it would tick the stage before the student
    #   opened the answers, which is a behaviour change to an approved page.
    #   C2's call, stated not taken.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Cells in a dish",
         "done_when": "committed"},
        {"anchor": "s-zoom", "short": "ZOOM", "label": "Five stops",
         "done_when": "all_stops_seen", "threshold": 5},
        {"anchor": "s-hard", "short": "SORT", "label": "The awkward ones",
         "done_when": "answers_opened"},
        {"anchor": "s-break", "short": "BREAK", "label": "Take a level out",
         "done_when": "all_cases_explored", "threshold": 4},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # One KEY FACT box, a top-level sibling AFTER the misconception block —
    # b1-04 and b1-05 now agree on that position exactly, including the 24px
    # margin (inventory F19). `band` ground, accent shadow, no badge and no
    # mark: `--ks3-band` is also the chosen-WRONG ladder ground, so anything
    # mark-like here would read as a verdict on a line that is simply true.
    "key_facts": [
        {"id": "kf-a-rung-up-is-a-different-kind",
         "text": "A rung up is a different kind of thing, not a bigger one. "
                 "The only thing added between rungs is organisation.",
         "eyebrow": "Key fact", "ground": "band", "placement": "top-level"},
    ],

    # The tutor card's line and its in-page anchor are both authored, on
    # three of three reference screens (inventory F12/G10). The CTA is a real
    # <a>, and it points back into this page's hardest activity.
    "tutor": {
        "prompt": "Stuck on which rung something belongs to?",
        "cta": "Ask about this lesson",
        "anchor": "s-hard",
    },

    # `before_this` is unset — `requires` is non-empty, so the endmatter's
    # first card renders the link (§4.8.1 D).
    # `safety_note` is unset — no apparatus on this page.
    # ⚑ `legal` is DELIBERATELY ABSENT and its absence is load-bearing: Design
    #   emits no `p.ks3-legal` at all (second page with the slot empty). Per
    #   inventory C3 the field is optional and unset means EMIT NOTHING — the
    #   renderer must not fall back to `build_ks3.LEGAL_LINE` here.

    # ---- the block deck (§5.1.1) -----------------------------------------
    # Design's 11 children of `.ks3-lesson`, in order: header · hook · zoom ·
    # sort · break · misconception · KEY FACT · ladder · keynote · stretch
    # layer · endmatter. Eight of those are core blocks; the header, the layer
    # and the endmatter are the renderer's.
    #
    # ⚑ `anchor` is the SECTION ANCHOR and `id` stays the activity reference —
    #   the convention the other five B1 records use. Every anchored section
    #   takes `scroll-margin-top: 92px` whether or not the rail names it:
    #   `#s-think` and `#s-keynote` are anchored and unlisted, and a hash link
    #   from the trail or the tutor CTA lands under the sticky bar otherwise
    #   (G2). ⚠️ `build_ks3._id_attr` currently reads `block["id"]`, which on
    #   this deck would emit an activity id as an element id and drop every
    #   anchor. It must read `anchor`.
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # ── #s-zoom · the five-stop zoom (G4, inventory §7.2) ───────────
        # One instrument that draws five different diagrams from one canvas
        # routine set, with a readout that never changes shape. `gain_label`
        # is authored per level and changes with the rung — that five-string
        # ladder IS the lesson and no template can generate it.
        {"type": "zoom-ladder",
         "anchor": "s-zoom",
         "eyebrow": "Zoom in · five stops",
         "title": "From a whole plant to one cell, without leaving the leaf",
         "intro": "Drag the slider. The orange box shows you where the next "
                  "stop down is hiding inside this one — and the panel "
                  "underneath says what this level can do that the level "
                  "below cannot.",
         "slider": True,
         "slider_label": "Zoom level",  # visually hidden <label for>
         "start": "organism",  # the startZoom prop: organism | cell
         "step_format": "Stop {n} of {total}",
         "human_prefix": "In you:",
         "next_box_label": "NEXT STOP IS HERE",
         # 1800×1000 buffer painted through setTransform(2,…) into a
         # 900×500 design space — 2.018 device px per CSS px at 1280, i.e.
         # crisp at 1× and 2×. Every `next_box` below is in design space.
         "canvas": {"buffer": [1800, 1000], "design_space": [900, 500],
                    "device_scale": 2},
         "levels": [
             {"tick": "Organism",
              "name": "Organism — the whole plant",
              "size": "about 30 cm tall",
              "what": "Everything from the root tips to the newest leaf, "
                      "working as one thing. It grows, it responds, it "
                      "reproduces, it makes its own food.",
              "gain_label": "What it can do that an organ system cannot",
              "gain": "Live. No single system in a plant survives on its own "
                      "— the shoot would starve of water in a day and the "
                      "root would starve of sugar.",
              "human": "You. Roughly thirty trillion cells, and one thing.",
              "alt": "A whole plant with a stem, three leaves and a root "
                     "system, with an orange box round the shoot.",
              "drawing": "plant",
              "next_box": [180, 56, 540, 306]},
             {"tick": "Organ system",
              "name": "Organ system — the shoot",
              "size": "about 20 cm",
              "what": "The stem and all the leaves together. Several organs "
                      "that share one overall job: catch light, make food, "
                      "and move it to wherever it is needed.",
              "gain_label": "What it can do that a single organ cannot",
              "gain": "Run a whole function end to end. One leaf can "
                      "photosynthesise but cannot deliver the sugar anywhere; "
                      "the stem can move sugar but cannot make any.",
              "human": "Your digestive system: mouth, oesophagus, stomach, "
                       "intestines, liver and pancreas, all on one job.",
              "alt": "The same plant with the stem and leaves drawn solid and "
                     "the roots faded, and an orange box round one leaf.",
              "drawing": "plant",
              "drawing_variant": "shoot",  # same routine, roots faded
              "next_box": [548, 150, 232, 124]},
             {"tick": "Organ",
              "name": "Organ — one leaf",
              "size": "about 5 cm long",
              "what": "A structure made of several different tissues, "
                      "arranged so that together they do one job: "
                      "photosynthesis.",
              "gain_label": "What it can do that a single tissue cannot",
              "gain": "Photosynthesise. The palisade layer traps the light, "
                      "but it needs veins to bring water and carry sugar "
                      "away, an epidermis to stop it drying out, and pores to "
                      "let carbon dioxide in. Take any one of those away and "
                      "the job fails.",
              "human": "Your stomach: muscle to churn, lining to make acid "
                       "and enzymes, connective tissue to hold its shape, "
                       "nerves to time it.",
              "alt": "A single leaf with a midrib and branching veins, with "
                     "an orange box marking a slice through it.",
              "drawing": "one-leaf",
              "next_box": [406, 122, 88, 256]},
             {"tick": "Tissue",
              "name": "Tissue — the palisade layer",
              "size": "about 0.2 mm thick",
              "what": "A group of similar cells, all doing the same job, "
                      "packed together so their effect adds up. Here: one "
                      "dense layer of tall cells right under the upper "
                      "surface.",
              "gain_label": "What it can do that a single cell cannot",
              "gain": "Catch nearly all of the light landing on the leaf. One "
                      "palisade cell intercepts a speck; a whole layer of "
                      "them, shoulder to shoulder with no gaps, leaves almost "
                      "nothing to get past.",
              "human": "Blood is a tissue. So is muscle, and so is the lining "
                       "of your gut.",
              "alt": "A cross-section through a leaf showing the upper "
                     "epidermis, a dense palisade layer, a spongy layer with "
                     "air spaces, and the lower epidermis.",
              "drawing": "leaf-section",
              "next_box": [100, 156, 76, 146]},
             {"tick": "Cell",
              "name": "Cell — one palisade cell",
              "size": "about 50 micrometres — 0.05 mm",
              "what": "The one you built two lessons ago: wall, membrane, "
                      "cytoplasm, nucleus, mitochondria, vacuole, and "
                      "chloroplasts crowded against the light.",
              "gain_label": "What it can do that its own parts cannot",
              "gain": "Be alive. A chloroplast on its own is machinery; a "
                      "nucleus on its own is a library nobody reads. The cell "
                      "is the smallest thing on this ladder that does all "
                      "seven life processes.",
              "human": "Your cells too. Same rung, different tuning.",
              "alt": "A single palisade cell with a cell wall, a large "
                     "vacuole, a nucleus at one side and chloroplasts packed "
                     "near the top.",
              "drawing": "one-cell",
              # No box: there is no stop below the cell. The null is
              # semantic — it suppresses the rectangle AND its tab.
              "next_box": None},
         ]},

        # ── #s-hard · eight things that get put on the wrong rung ───────
        # (G7, inventory §7.3.) Eight rows × six choices + one gate = 49
        # buttons, more interactive controls than any other block in B1.
        # Placements are freely revisable and nothing is marked until the
        # student opens the answers; the reveal is one-way.
        #
        # ⚑ `marks_on_reveal` is the one place in KS3 where an activity marks.
        #   It was ruled to PASS R3 on MRB-202 (13 Aug): the mark lands on the
        #   ROW CONTAINER (--ks3-inset/ink right, --ks3-alert-tint/
        #   --ks3-alert-border wrong), never on a button — the chosen choice
        #   keeps its accent-tint treatment unchanged before and after — and
        #   no --ks3-ok green appears anywhere outside #s-ladder. R3's runtime
        #   assertion is scoped to the option button, so this is a reveal.
        {"type": "sort-task",
         "anchor": "s-hard",
         "eyebrow": "Your turn · the awkward ones",
         "title": "Eight things that get put on the wrong rung",
         "intro": "The easy examples teach you nothing. These are the ones "
                  "people argue about. Put each on a rung — change your mind "
                  "as often as you like, nothing is marked — then open the "
                  "answers.",
         "choices": ["Cell", "Tissue", "Organ", "Organ system",
                     "Organism", "Not on the ladder"],
         "gate_label": "Open the answers",
         "counter": "{n} of {total} placed",
         "marks_on_reveal": True,
         "items": [
             {"id": "blood",
              "item": "Blood",
              "answer": "Tissue",
              "note": "A few kinds of cell, in enormous numbers, suspended in "
                      "liquid and all working on transport. Being a liquid "
                      "does not disqualify it."},
             {"id": "skin",
              "item": "Skin",
              "answer": "Organ",
              "note": "Your largest organ, and clearly several tissues: "
                      "layers of epidermis, connective tissue underneath, "
                      "glands, nerve endings and blood vessels running "
                      "through it."},
             {"id": "xylem",
              "item": "Xylem",
              "answer": "Tissue",
              "note": "Similar cells, one job — carrying water up the plant. "
                      "It sits inside an organ (the stem, the root, the leaf) "
                      "the way muscle sits inside your stomach."},
             {"id": "brain",
              "item": "The brain",
              "answer": "Organ",
              "note": "Several tissues — nerve tissue of more than one kind, "
                      "blood vessels, connective tissue and membranes. It is "
                      "the main organ of the nervous system, not the system "
                      "itself."},
             {"id": "chloroplast",
              "item": "A chloroplast",
              "answer": "Not on the ladder",
              "note": "It is a part of a cell, below the bottom rung. That is "
                      "exactly why the ladder starts at the cell: a "
                      "chloroplast is machinery, not a living thing."},
             {"id": "stomach",
              "item": "The stomach",
              "answer": "Organ",
              "note": "An organ of the digestive system. On its own it can "
                      "churn and make acid; it cannot digest a meal and "
                      "deliver it, which is what the system does."},
             {"id": "bone",
              "item": "A bone, such as your femur",
              "answer": "Organ",
              "note": "This is the one worth arguing about, and both sides "
                      "are right about different things. A named bone is an "
                      "organ — it contains bone tissue, marrow, blood vessels "
                      "and nerves. The hard material inside it, \"bone\", is "
                      "a tissue. The wording decides which you mean."},
             {"id": "rootsys",
              "item": "The root system of a tree",
              "answer": "Organ system",
              "note": "Many roots — each an organ — working together on one "
                      "overall job: anchoring the tree and taking up water "
                      "and minerals."},
         ]},

        # ── #s-break · keep every cell alive, remove the organisation ───
        # (G8, inventory §7.4.) Four dark tabs, a predict gate built from the
        # standard dark option, and a cream reveal island inside the ink
        # block. Design gates by ABSENCE — the gate leaves the DOM once
        # answered — not by R5's veil, and there is no veil, blur or disabled
        # control anywhere on this page. R5 stays in the registry for PROCESS
        # and INVESTIGATION; it is simply not what this page does.
        #
        # ⚑ No prediction is marked and no option carries `correct` (R3), and
        #   ⚑ there is no "You said: …" echo — b1-04 added one, this page has
        #     none, so the pattern exists on one of the two SYSTEM pages
        #     (inventory F33). One value needed; not invented here.
        {"type": "removal-cases",
         "anchor": "s-break",
         "eyebrow": "Take a level out",
         "title": "Keep every cell alive. Remove the organisation.",
         "lede": "Nothing here is killed and nothing is taken away. In each "
                 "case the parts are all present and all healthy — only the "
                 "arrangement is gone. Pick one, say what stops, then read "
                 "what actually happens.",
         "counter": "{n} of {total} explored",
         "what_label": "What we did",
         "commit": "Commit first. What stops working?",
         "lost_prefix": "Level lost: ",
         "principle_prefix": "The principle:",
         "cases": [
             {"id": "dish",
              "label": "Stomach cells in a dish",
              "what": "We take a healthy stomach and separate every cell from "
                      "every other cell. Nothing is killed.",
              "intact": "All the cells are alive. All of them are the right "
                        "kinds. There are exactly as many as there were.",
              "lost": "Tissue and above",
              "predict": [
                  "Nothing — the cells still do their jobs",
                  "Nothing can be churned or held together, so no meal is "
                  "ever digested",
                  "The cells die within minutes",
              ],
              "headline": "They keep working. Nothing gets digested.",
              "body": "The acid-making cells make acid, into the dish. The "
                      "muscle cells contract, on their own, in no particular "
                      "direction. There is no cavity to hold food, no wall to "
                      "squeeze it against, no sequence and no timing. "
                      "Everything a stomach is for depended on the cells "
                      "being arranged, and the arrangement is what we took.",
              "principle": "Between the cell and the tissue, the only thing "
                           "added is organisation — and it is doing most of "
                           "the work."},
             {"id": "nomuscle",
              "label": "A stomach with no muscle layer",
              "what": "We leave the stomach whole and remove only its muscle "
                      "tissue. Every other tissue stays where it is.",
              "intact": "The lining still makes acid and enzymes. The shape "
                        "is still there. The nerves are still there.",
              # ⚑ No level named. Design's page concatenates
              #   "Level lost: " + undefined and renders the pill
              #   reading "Level lost: undefined" — a defect, not
              #   authored copy. Inventory C4 is Code's to decide:
              #   an unset `lost` SUPPRESSES the pill entirely.
              "lost": None,
              "predict": [
                  "Acid production stops",
                  "The chemistry works but nothing mixes, so digestion is "
                  "slow and patchy",
                  "The stomach bursts",
              ],
              "headline": "The chemistry is fine. The mixing is gone.",
              "body": "Enzymes only work where they meet the food, and a "
                      "sandwich is not a liquid. Without the muscle layer "
                      "squeezing and folding the contents, acid and enzymes "
                      "reach the outside of the lump and never the middle. "
                      "What should take twenty minutes does not finish at all.",
              "principle": "An organ is several unlike tissues. Remove one "
                           "and the organ does not do a bit less of its job — "
                           "it stops doing the job properly at all."},
             {"id": "leafcells",
              "label": "Leaf cells, unarranged",
              "what": "We take a leaf and shuffle its cells, so palisade, "
                      "spongy and epidermis cells are mixed evenly through a "
                      "blob of the same total size.",
              "intact": "Every cell is alive, with all its chloroplasts. The "
                        "blob has the same volume and mass as the leaf did.",
              # ⚑ No level named. Design's page concatenates
              #   "Level lost: " + undefined and renders the pill
              #   reading "Level lost: undefined" — a defect, not
              #   authored copy. Inventory C4 is Code's to decide:
              #   an unset `lost` SUPPRESSES the pill entirely.
              "lost": None,
              "predict": [
                  "It photosynthesises just as well",
                  "Far less light is caught, and it dries out or suffocates",
                  "It turns yellow immediately",
              ],
              "headline": "It photosynthesises, badly, and not for long.",
              "body": "The chloroplasts are no longer in a dense layer at the "
                      "top, so most of them sit in shade behind other cells. "
                      "There is no epidermis on the outside, so water escapes "
                      "freely; there are no air spaces, so carbon dioxide "
                      "cannot reach the middle; and no veins, so nothing "
                      "arrives or leaves. A leaf is flat and layered for "
                      "reasons, and every one of them is now gone.",
              "principle": "Arrangement is not decoration. In an organ, where "
                           "each tissue sits is part of how it works."},
             {"id": "detached",
              "label": "A leaf cut off the plant",
              "what": "We cut a healthy leaf off and leave it in the light, "
                      "with every cell and every tissue perfectly intact.",
              "intact": "The whole organ is undamaged. It keeps "
                        "photosynthesising for a while.",
              # ⚑ No level named. Design's page concatenates
              #   "Level lost: " + undefined and renders the pill
              #   reading "Level lost: undefined" — a defect, not
              #   authored copy. Inventory C4 is Code's to decide:
              #   an unset `lost` SUPPRESSES the pill entirely.
              "lost": None,
              "predict": [
                  "It carries on indefinitely, since it makes its own food",
                  "It runs out of water and has nowhere to send the sugar, so "
                  "it fails within days",
                  "It stops photosynthesising immediately",
              ],
              "headline": "A perfect organ, for about two days.",
              "body": "It goes on making sugar until the water runs out — and "
                      "there is no root system to replace what evaporates. "
                      "The sugar it makes has nowhere to go, so it "
                      "accumulates and photosynthesis slows. Nothing is wrong "
                      "with the leaf. What is missing is everything it was "
                      "connected to.",
              "principle": "An organ is not self-sufficient. That is exactly "
                           "what an organ system, and then the organism, adds."},
         ]},

        # ── #s-think · ONE block, TWO misconceptions ────────────────────
        # Both open, no hidden reveal, split by a 2px --ks3-alert-border rule.
        # §4.8.2's `statements` extension exists for exactly this shape, which
        # b1-03, b1-04, b1-05 and b1-06 all use.
        {"type": "misconception", "id": "organ-is-not-a-bigger-tissue",
         "anchor": "s-think", "eyebrow": "Think again"},

        {"type": "key-fact", "ref": 0},  # top-level, and Design gives it
                                         # no anchor of its own

        # `class="ks3-ladder"` alone on Design's page, not `ks3-block
        # ks3-ladder` — that single-class set is what gives the ladder h2 its
        # 57.6px line-height (inventory D5/F17, three confirmations).
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},

        # Design's keynote heading is `<p class="ks3-eyebrow">Key note</p>`
        # — 30px/700/uppercase/--ks3-alert — not an `<h2>` (inventory D4/F16,
        # three reference screens agree and all three disagree with the
        # build). The eyebrow text is data so the renderer stops hard-coding
        # the element.
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote",
         "eyebrow": "Key note"},
    ],

    # ---- the chosen layers (§5.6) ----------------------------------------
    # ⚑ ONE bare paragraph. Design's `.ks3-layer-body` holds a `<p>` and
    #   nothing else — no nested card, no check (inventory §3.1.6 #13, third
    #   confirmation). An `explainer` inside a layer must therefore render as
    #   bare prose, not as a `.ks3-block` card. No `id`: the layer carries no
    #   anchor.
    "stretch": [
        {"type": "explainer",
         "text": "The ladder does not stop at the organism. Above it sit "
                 "populations, communities and ecosystems, and the same rule "
                 "holds: each level does something the one below cannot. A "
                 "single rabbit cannot go extinct and cannot evolve — only a "
                 "population can. It runs downwards too, past the cell to "
                 "organelles, molecules and atoms. Biologists put the bottom "
                 "rung at the cell because it is the smallest thing on the "
                 "ladder that is <em>alive</em>."},
    ],

    "support": [],

    # ---- activities (§5.5) -----------------------------------------------
    # Exactly one. The zoom, the sorter and the removal cases are NOT
    # activities and cannot be: §5.5's families describe marked or self-marked
    # tasks, and these three are an instrument, a deferred self-service
    # reveal, and a predict-then-read case set. They carry their own content
    # payloads inside `core` (inventory §5.2).
    "activities": [
        {"id": "organ-is-not-a-bigger-tissue",
         "kind": "confrontation",
         "demand": "confront both level misconceptions in one pass: the "
                   "size error and the solidity error",
         "targets": ["CELL-06", "CELL-07"],
         "statements": [
             {"quote": "An organ is just a bigger tissue.",
              "answer": "Size is not what the ladder measures. A rung up is "
                        "not more of the same thing — it is a different "
                        "<em>kind</em> of thing, made by putting unlike parts "
                        "together. A tissue is many cells of one kind doing "
                        "one job. An organ is several <em>different</em> "
                        "tissues that between them do a job none of them "
                        "could do alone. Your stomach has a muscle layer to "
                        "churn, a lining to make acid and enzymes, connective "
                        "tissue to hold it in shape and nerves to time it. "
                        "Grow the muscle layer to the size of a stomach and "
                        "it still cannot digest anything."},
             {"quote": "Blood can’t be a tissue — it’s a liquid.",
              "answer": "A tissue is defined by what it is made of and what "
                        "it does, not by whether it holds its shape. Blood is "
                        "a huge population of cells of a few kinds, suspended "
                        "in liquid, all working on one job: transport. That "
                        "makes it a tissue, and it is the reason the ladder "
                        "is about organisation rather than about solidity."},
         ]},
    ],

    # ---- the mastery ladder (§5.8) ---------------------------------------
    # Two rungs the page marks, two the student marks — Design's own
    # sub-line. Rung TITLES are authored ("Rung 1 · Put it on a rung"), not
    # "1 · Recall": new against §5.8, which derives them from the key.
    # `feedback` is keyed by option index and carries Design's per-option
    # `correction`; the correct option has none, and a right answer's feedback
    # is "Correct." with no trailing prose.
    "ladder": {
        # ⚑ Design's retry note describes behaviour the page does not have:
        #   onRetry clears rungs 1 and 2 as well (inventory F23, second page,
        #   identical copy and behaviour, so it is systematic). Under standing
        #   law the page wins and the generator reproduces BOTH — note and
        #   behaviour — rather than quietly fixing one of them. shared/ks3.js
        #   currently hard-codes a different sentence.
        "retry_note": "Clears the ticks on rungs 3 and 4 and keeps what you "
                      "wrote.",
        "recall": {
            "title": "Rung 1 · Put it on a rung",
            "q": "Blood is a liquid that flows. Which level of organisation "
                 "is it?",
            "options": [
                "A cell",
                "A tissue",
                "An organ",
                "Not on the ladder at all",
            ],
            "answer": 1,
            "feedback": {
                0: "It contains cells — several kinds of them — so it must be "
                   "at least one rung above a cell.",
                2: "An organ is several different tissues arranged together. "
                   "Blood is one tissue, which travels through organs rather "
                   "than being one.",
                3: "It is on the ladder. Being a liquid is not the "
                   "disqualifier — the ladder measures organisation, not "
                   "solidity.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A dish of living stomach cells cannot digest a sandwich, "
                 "even though every cell is healthy and doing its job. Why "
                 "not?",
            "options": [
                "There are not enough cells in the dish",
                "They are not organised into tissues and layers that work on "
                "the food together",
                "They are the wrong kind of cell for digestion",
                "Cells cannot make enzymes outside the body",
            ],
            "answer": 1,
            "feedback": {
                0: "Add a thousand times more and it still will not digest "
                   "anything. The problem is not quantity.",
                2: "They are exactly the right cells — the same ones that are "
                   "doing it in you right now.",
                3: "They can, and they do. The enzymes are being made; they "
                   "are just being made into a dish.",
            }},
        "explain": {
            "title": "Rung 3 · Explain it",
            "q": "Explain why a leaf is called an organ but the palisade "
                 "layer inside it is called a tissue. Use the word “tissues” "
                 "in your answer.",
            "field_label": "Your explanation",
            "placeholder": "The palisade layer is…",
            "success": [
                "Says the palisade layer is many similar cells all doing the "
                "same job.",
                "Says a leaf contains several different tissues, and names at "
                "least two of them.",
                "Says the leaf does a job that no one of those tissues could "
                "do on its own.",
                "Makes clear the difference is organisation, not size.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A laboratory grows a sheet of living heart muscle cells in "
                 "a dish. It beats, steadily, on its own. A newspaper reports "
                 "that they have grown a heart. Say what they have actually "
                 "made, which rung it is on, and what would still be missing.",
            "field_label": "Your answer",
            "placeholder": "What they have made is…",
            "success": [
                "Says they have made a tissue, not an organ, and says why: "
                "one kind of cell, one job.",
                "Names tissues a real heart has that the sheet does not — "
                "valves, blood vessels, nerve tissue, connective tissue.",
                "Says the arrangement matters too: four chambers in a "
                "particular order, so blood is pushed the right way.",
                "Says that even a complete heart would need to be connected "
                "into the circulatory system to be any use.",
            ]},
    },

    "key_note": "Cells, tissues, organs, organ systems, organism. Each rung "
                "can do something the rung below it cannot — and the only "
                "thing added between rungs is organisation.",

    # ---- illustration palette (G6 / inventory F30) ------------------------
    # The four canvas routines hard-code SIXTEEN hex values that are not KS3
    # tokens (the inventory says eleven in §3.3 and fifteen in §6.2; both
    # undercount — this list was taken from the source and is the true set).
    # They are SUBJECT ARTWORK, not system colour: a leaf is green because
    # leaves are green, and forcing them into the `--ks3-*` namespace would
    # make plant pigment a design token.
    #
    # ⚑ Inventory C5 says these must not be re-invented per lesson. They live
    #   here because there is nowhere else today; the moment a second lesson
    #   draws a plant, this dict moves to a shared registry and the lesson
    #   references it by name. Everything else the routines use (#221E1B,
    #   #C3B191, #E4572E, #FBF3E6, #FFFCF5) already resolves to a token and is
    #   deliberately NOT duplicated here.
    "illustration_palette": {
        "soil":            "#EFE3C9",
        "root":            "#8A6A3C",
        "stem":            "#5E7A3A",
        "leaf-fill":       "#5E9440",
        "leaf-stroke":     "#2F5326",
        "midrib":          "#3E6B2C",
        "epidermis":       "#EFE6D2",
        "cell-fill":       "#EFF3E4",
        "chloroplast":     "#4F7C3B",
        "cell-wall":       "#D9C48D",
        "cytoplasm":       "#F5ECD8",
        "membrane":        "#A2603A",
        "vacuole-fill":    "#E4EDE9",
        "vacuole-stroke":  "#9AB0A6",
        "nucleus-fill":    "#7C6AA6",
        "nucleus-stroke":  "#453A69",
    },

    # ---- working scientifically and governance ----------------------------
    "ws": ["analysis-and-evaluation"],
    "review_state": "draft",
}
