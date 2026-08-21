"""B1 L6 — Unicellular organisms (CONTRAST). Design's approved page, as data.

⚠️ **The CONTRAST reference screen. 18 lesson slots inherit its shapes.**
`docs/ks3/design-coverage-manifest.md` §10.1 names
`docs/ks3/design-reference/b1/b1-06-unicellular-organisms.dc.html` as the
approved screen for the whole family, ruled by Mide on 12 Aug 2026. Every field
below was measured on that page; the evidence is
`docs/ks3/b1-inventory/b1-06-unicellular-organisms.md`, and its section numbers
are cited inline rather than re-argued.

**Every authored string here is lifted byte-identical from the approved page.**
The 147 strings in the page's `<script data-dc-script>` constants (`RAIL`,
`OBJS`, `POND`, `CENTRES`, `RESOLVE`, `COMPARE`, `CASES`, `RUNGS`,
`SELF_RUNGS`) and the 34 in its `<x-dc>` template were extracted mechanically
and pasted in as literals, never retyped. ~2,490 authored words, none of which
existed in `ks3_data/` before — the superseded record in
`ks3_data/biology_b1_cells.py` (from line 2000) is a different lesson with a
different big question and a 16-block stack. What was carried across from it,
deliberately, is listed under DIVERGENCES below.

`BACTERIA` is **not** here: it is a 54-element deterministic LCG, and
`shared/ks3.js` already ships it (with `OBJ_DOF_MM`, `FOCUS_MIN_MM`,
`FOCUS_SPAN_MM` and `SHARP_FRACTION`). `OBJS`' `total` / `fov` / `dof` are
engine constants under MRB-210, not payload, and are not restated here either.

──────────────────────────────────────────────────────────────────────────
⚑ MRB-196 — the settles-it activity gains a self-check. RULED by Mide, 13 Aug
──────────────────────────────────────────────────────────────────────────

The inventory's F36 found the activity computes whether the student agreed
(`agreed = revealed && ((pick === 'yes') === f.settles)`) and then spends it on
one thing: the `why` paragraph's colour, `--ks3-ink` against `--ks3-ink-body`,
about 6 ΔL* apart on 18px text. Not perceptible, and not a mark. Mide ruled:

    "The student is asked whether they had it and answers for themselves. No
     green, no red, nothing on the option button — R3 intact. The page never
     grades anyone; it asks."

So `self_check` below is authored, and the `agreed` computation goes. Two
consequences the renderer must carry, neither of them expressible as data:

  1. The `why` paragraph takes ONE tone regardless of what the student marked.
     Nothing may be computed from the student's mark, anywhere.
  2. The self-check carries no truth value — no `settles`, no `correct`, no
     `answer` key exists anywhere inside it. R3 holds by construction: the
     renderer is given nothing it could grade with.

──────────────────────────────────────────────────────────────────────────
⚑ THE CELL-08 PAIRED CONTRACT — five strings, three blocks. Do not reword.
──────────────────────────────────────────────────────────────────────────

B1-04's hook says of the red blood cell "no nucleus, no instructions, no
repair, no dividing", and ratifies it with "All still true." A bacterium has no
nucleus and divides every twenty minutes. This lesson resolves the
contradiction: the red cell **destroyed** its nucleus and lost the DNA with it,
a bacterium **never had one** and its DNA is present. The discriminator is
whether the instructions are there, not whether the container is.
Prokaryote / eukaryote stay out — KS4 vocabulary, ruled by Mide.

The five strings that carry it, all below and all byte-identical:

  · `misconceptions` CELL-13's `statement`, and the `think-again` activity's
    first statement — its `quote` and its `answer` (the `<em>` on *had* is
    load-bearing typography, not decoration)
  · `s-settle` case c3, feature 1's `why` — "A red blood cell has no nucleus
    either, and that is a part of you."
  · `s-settle` case c3, feature 2's `why` — "A red blood cell can never divide
    again."
  · `ladder.apply` — the whole rung: question, correct option, and the
    distractor correction "The bacterium never had a nucleus at any point."
    ⊕ MRB-177, ruled 17 Aug 2026 — option 1 was rewritten to state a wrong
    RULE, and its correction now opens "Having had one does not help: the red
    blood cell destroyed its nucleus and lost the DNA with it." The contract
    sentence above is unchanged and still closes that correction; the
    superseded opener was "That is the red blood cell."

Shipped apart, in either order, a student is taught something false. If
b1-04's hook changes, all five must be re-read against it, and vice versa.
The misconception register cannot express the edge, which is why CELL-13
carries `pairs_with` (gap G12).

──────────────────────────────────────────────────────────────────────────
DIVERGENCES from the superseded record, each deliberate
──────────────────────────────────────────────────────────────────────────

  · `requires` is `levels-of-organisation` alone, and `references` carries
    `life-processes` + `specialised-cells`. Design's endmatter draws exactly
    that: one "Before this lesson" link, two under "Connects to" (§3.7).
  · `ks4_links` is empty and `ks4_becomes` carries prose, because Design's
    third endmatter card is prose (§4.8.1 D gives the empty-list rule). It also
    keeps `eukaryotes-prokaryotes` — which the renderer would print as the link
    label — off a KS3 page.
  · `figures` is empty. Design's page carries no figure: the live microscope
    replaces `b1-pond-water-micrograph`, and the `comparison` block replaces
    `b1-unicellular-adaptations`, which the inventory §3.1 records as the
    pending placeholder standing in for exactly this table.
  · `vocabulary` is carried over verbatim, but **no `keyword` block is
    emitted** — Design's page has no vocabulary check and no flip cards
    (§8(a)5: five reference screens, zero flip cards). Flagged, not resolved.

──────────────────────────────────────────────────────────────────────────
RENDERER PREREQUISITES — this record cannot build until these land
──────────────────────────────────────────────────────────────────────────

  · `settles-it` is a new block type (gap G7) and `render_blocks` raises on it
    today. §5.1.1's vocabulary is closed at fourteen types and needs the
    amendment before this renders.
  · `phenomenon` needs `options` + `reveal`: Design's commitment lives INSIDE
    the ink-dark hook block and the generator's hook has no options (§3.2).
  · `r_hook` and the `quiz` lambda emit no `id`, so rail stages 1 and 4 point
    at nothing. Every id-bearing section needs `_id_attr` (gap G13).
  · `practical` needs `eyebrow` / `heading` / `lede` / `progress_format`: the
    shell hard-codes the eyebrow "Investigate" and emits no heading.
  · The `misconception` shell needs `statements` (§4.8.2) — one block, two
    misconceptions — and both its quote and its answer must go through
    `rich()`, not `t()`.
  · The sim needs `mounts` / `centres` / `motion_toggle` (gaps G9, G10, G11),
    and `SIM_CONTROLS` + `CONTROL_LABELS` in `shared/ks3.js` need `centre` and
    `motion`.
  · F33 is already ruled: with a centre control present the organisms must stop
    swimming, because the pond mount's own caption tells the student they are
    held still and the slide moves. The page wins over the engine.
  · The ladder needs `title`, `field_label` and `placeholder` per rung; today
    it derives "1 · Recall" from `LADDER_RUNGS` and hard-codes "Write your
    answer".
"""

LESSON = {
    # ---- identity -------------------------------------------------------
    # Matches ks3_data/structure.py's B1 slot exactly: slug, title, family.
    "slug":        "unicellular-organisms",
    "title":       "Unicellular organisms",
    "discipline":  "biology",
    "unit":        "cells-and-organisation",
    "family":      "CONTRAST",

    # ---- curriculum position -------------------------------------------
    "covers":      ["KS3.B.CELLS.05"],
    "touches":     ["KS3.B.CELLS.02"],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 3},
                    {"id": "structure-function", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 45,

    # ---- progression edges ---------------------------------------------
    # Design's endmatter is the specification for all three cards (§3.7).
    "requires":    ["levels-of-organisation"],
    "assumes":     [],
    "references":  [{"unit": "B1", "lesson": "life-processes"},
                    {"unit": "B1", "lesson": "specialised-cells"}],
    "ks4_links":   [],

    # ---- the teaching payload ------------------------------------------
    "big_question": "Two single cells, one much smaller. One is a whole animal. "
                    "One is a piece of you. What tells them apart?",

    # §3.2 — the hook is ink-dark and its commitment stays inside the block:
    # four options and a single static reveal, gated only on having chosen.
    # ⭐ The reveal defers WITHOUT endorsing — it says three of the four settle
    # nothing and never says which three. b1-05's F27 asked for exactly this
    # wording and this page is proposed as the family's answer to it (§8(a)7).
    "phenomenon": {
        "kind": "demo",
        "title": "A quarter of a millimetre long, and it hunts.",
        "prompt": "A Paramecium swims, finds food, eats it, senses obstacles, "
                  "reverses, grows and splits in two. A cheek cell is four "
                  "times smaller and lines your mouth. Neither is more "
                  "alive than the other.",
        "commit": "One is an organism. One is part of one. What settles it?",
        "options": [
            "It can move on its own",
            "It has more structures inside it",
            "It carries out all seven life processes by itself",
            "It lives in water instead of inside a body",
        ],
        "reveal": "Three of those four are true of a Paramecium and settle "
                  "nothing. Telling which fact does the work is the whole of "
                  "this lesson.",
    },

    # §4.5 — CELL-13 is NEW and unregistered. The register keys on
    # {id, statement, elicited_by, confronted_by, owner} and knows nothing of
    # the bacterium / red-blood-cell pair: #s-think's SECOND misconception has
    # an entry (CELL-08) and its FIRST has none, so a build-time check over the
    # register would report this block as fully accounted for. `pairs_with` is
    # gap G12. Add CELL-13 to docs/ks3/misconception-register.md.
    #
    # ⚑ `elicited_by` is None on both #s-think entries and that is honest, not
    # an omission: on Design's page both misconceptions are static markup with
    # no gate and no eliciting activity ("Both are open", §3.6). Law 3's
    # elicit-then-confront is discharged by the settles-it activity for LIFE-03
    # and by nothing at all for these two.
    "misconceptions": [
        {"id": "LIFE-03",
         "statement": "A single cell cannot be a whole living thing — it "
                      "must be part of something bigger.",
         "elicited_by": "s-hook",
         "confronted_by": "s-settle"},
        {"id": "CELL-13",
         "statement": "No nucleus means no instructions — so a bacterium "
                      "cannot divide.",
         "elicited_by": None,
         "confronted_by": "s-think",
         "pairs_with": {"lesson": "specialised-cells",
                        "relation": "qualifies",
                        "claim": "Two lessons ago: no nucleus, no "
                                 "instructions, no repair, no dividing."}},
        {"id": "CELL-08",
         "statement": "A single-celled organism is just a simpler version "
                      "of one of our cells — the same parts, doing less.",
         "elicited_by": None,
         "confronted_by": "s-think"},
    ],

    # Carried verbatim from the superseded record. Design's page renders NO
    # vocabulary check — see DIVERGENCES.
    "vocabulary": [
        {"term": "unicellular",
         "definition": "Made of one single cell, which is the whole organism.",
         "note": None},
        {"term": "multicellular",
         "definition": "Made of many cells, which are usually specialised.",
         "note": "You are multicellular. So is every plant and animal you can "
                 "see without a microscope."},
        {"term": "flagellum",
         "definition": "A long whip that a cell beats in order to swim.",
         "note": "One is a flagellum, several are flagella. You have "
                 "already met one: the tail of a sperm cell."},
        {"term": "cilia",
         "definition": "Short hairs covering a cell's surface, which beat "
                       "together like tiny oars.",
         "note": "One is a cilium. Cilia line your airways too, sweeping dust "
                 "back up out of your lungs."},
    ],

    "figures": [],

    # §1.4 — seven sections, in Design's document order. `anchor` is the DOM id
    # the rail and hash links point at; `id` (where present) is the key into
    # `activities`. The two are different things and a block may carry both.
    "core": [
        {"type": "hook", "anchor": "s-hook"},
        {"type": "practical", "anchor": "s-scope", "id": "microscope-bench"},

        # ── §3.4 / §7.2 — CONTRAST's spine (gap G8) ──────────────────────
        # An unclassed <section> on --ks3-band, the only band-ground block in
        # the delivery, with the KEY FACT box nested as its last child.
        #
        # FLEX, NEVER GRID, fixed at the root and not in a query (§3.4.1):
        #   [data-compare-grid] { display:flex; flex-wrap:wrap; gap:10px 14px }
        #   > [data-compare-label] { flex: 0 0 118px }
        #   > [data-compare-cell]  { flex: 1 1 250px; min-width: 0 }
        # and ONE @media (max-width: 820px) emitting all three narrow
        # declarations together — label to `1 1 100%`, header row to
        # `display:none`, caption to `display:block`. A grid cannot produce the
        # 820px stack without a second query.
        #
        # ⚠️ MRB-210's pixel figures do NOT reproduce on the delivered page and
        # layer-C assertions must not be written from them (§3.4.3). Measured:
        # wide is 118 + 356 + 356 (not 315 + 315); at a 360px lesson column the
        # cells are 258 × 81 (not 211 × 81); section height is 2151.75 (not
        # 2366). Every STRUCTURAL claim reproduces; assert declarations and
        # relations, never derived pixels, and bisect the threshold 821/820.
        #
        # Every cell emits its caption unconditionally, hidden by CSS above
        # 820px — conditional emission would need JS and would break at a
        # container width the query does not know about. The captions ARE the
        # column captions: one authored string used twice per column.
        {"type": "comparison",
         "anchor": "s-compare",
         "eyebrow": "Side by side",
         "eyebrow_tone": "accent-text",
         "statement": "The same seven processes. One cell does all of them; "
                      "one does one.",
         "ground": "band",
         "columns": [
             {"caption": "Paramecium", "tone": "alert"},
             {"caption": "One of your cheek cells", "tone": "on-dark"},
         ],
         # Zebra comes from the row index (i % 2 ? --ks3-inset : --ks3-card)
         # with border-top 2px --ks3-rule on every row, the first included.
         "rows": [
             {"name": "Movement",
              "cells": ["Beats hundreds of cilia and swims, reversing when it "
                        "hits something.",
                        "Does not move. It is held in a sheet by the cells "
                        "around it."]},
             {"name": "Respiration",
              "cells": ["Its own mitochondria, releasing energy for its own "
                        "swimming and feeding.",
                        "Mitochondria too — but the oxygen is delivered to it "
                        "by blood."]},
             {"name": "Sensitivity",
              "cells": ["Senses an obstacle and backs away from it.",
                        "Senses nothing. Nerve cells do that for the whole of "
                        "you."]},
             {"name": "Growth",
              "cells": ["Grows until it is big enough to divide.",
                        "Does not grow. It is replaced when it wears out."]},
             {"name": "Reproduction",
              "cells": ["Splits in two, and then there are two organisms.",
                        "Divides to replace itself, and there is still only "
                        "one of you."]},
             {"name": "Excretion",
              "cells": ["Vacuoles collect the water that keeps seeping in and "
                        "squeeze it back out.",
                        "Waste passes into the blood, and your kidneys deal "
                        "with it."]},
             {"name": "Nutrition",
              "cells": ["Sweeps food into an oral groove and digests it in a "
                        "vacuole inside itself.",
                        "Is fed. Glucose arrives dissolved in blood, already "
                        "digested."]},
         ],
         # Column 2 is deliberately one step quieter than column 1.
         "row_tones": ["ink", "ink-body"],
         # G6 — `card`, because the block itself is `band` and band on band is
         # invisible. Drift 5's outlier has a reason (F34). `ref` names a
         # `key_facts[].id`, so the text lives once and this says only where.
         "key_fact": {"ref": "kf-one-cell-all-seven"}},

        # ── §3.5 / §7.3 — the CONTRAST flagship (gap G7) ─────────────────
        # NOT a check (four independent judgements, gated collectively), NOT a
        # quiz (it does not mark and must not, R3), NOT a misconception (it
        # confronts a habit of reasoning, not a stated belief), NOT a
        # practical.
        #
        # Renderer requirements the payload cannot state, every one measured:
        #   · THREE row grounds keyed ONLY on `settles` and `revealed`, never
        #     on the student's mark: unrevealed --ks3-card on 2px
        #     --ks3-rule-strong; revealed+settles --ks3-band on 2px --ks3-ink;
        #     revealed+not --ks3-row-dim on 2px --ks3-rule.
        #   · TWO guards on the reveal — the `disabled` attribute AND a
        #     re-check of the mark count inside the state updater. `disabled`
        #     alone is bypassable.
        #   · After the reveal every choice is disabled, picked choices are
        #     unchanged and unpicked ones drop to opacity .5.
        #   · Marks are per case and never cleared; switching tabs must not
        #     clear `marks[case][feature]` or `caseOpen[case]`. No retry.
        #   · The progress string switches to "Opened", NOT "M of M marked".
        #   · `tab_label` is AUTHORED, not derived. Design derives it with
        #     label.replace('Mystery cell ', 'Cell '), which silently emits the
        #     full label the moment a lesson names its cases anything else.
        #   · The count of discriminators per case is FREE — 1, 2, 2, 2 here —
        #     and c2's `why` teaches that directly. Never assume one.
        #   · `answer` must not leak into a tab, `aria-label` or `title`: the
        #     reveal is the only place a mystery cell is named (F37).
        #   · The choice buttons are a fifth seg-like control and need
        #     their own registry entry, `settle-choice`: 16px / 700 /
        #     padding 10px 16px / min-height 44px / --ks3-r-control, where
        #     seg() is 17px / 11px 17px.
        {"type": "settles-it",
         "anchor": "s-settle",
         # ks3_data/b1/__init__.py lifts this block into `activities[]` and
         # renders it through the `check` shell, so `demand` is authored rather
         # than left to that collector's "investigate" default.
         "demand": "discriminate: sixteen judgements, and most of the facts "
                   "decide nothing",
         "eyebrow": "Your turn · four mystery cells",
         "heading": "Does that settle it?",
         # The <em> is Design's and is load-bearing — this string needs rich().
         "instruction": "Every fact below each cell is true. Most of them "
                        "settle nothing, because they are true of "
                        "single-celled organisms <em>and</em> of cells inside "
                        "a body. Mark only the ones that decide it.",
         # The same two words on all sixteen rows. Not per-case data.
         "choice_labels": ["Settles it", "Settles nothing"],
         "reveal_label": "Show what settles it",
         "progress_format": "{n} of {total} marked",
         "progress_opened": "Opened",
         # Generated from `settles`, rendered as a display-font <strong>, and
         # NOT part of the authored `why` — the authored string begins after
         # it. Authored rather than built from `choice_labels` + "." so the two
         # can never drift silently across the 18 lessons that inherit this.
         "why_openers": ["Settles it.", "Settles nothing."],

         # ⚑ MRB-196, ruled by Mide 13 Aug 2026. Shown after a case's reveal,
         # on the block's own ground, using the drawn settle-choice button.
         # State is per case and persists across tab switches, exactly like
         # `marks`. It gates NOTHING — the rail's SETTLE stage stays
         # `all_cases_revealed`, so an unanswered self-check can never block a
         # student. Three options and not two, because three of the four cases
         # have two discriminators and a yes/no would force a student who found
         # one of two to answer falsely.
         #
         # Shape is L1's `{question, options, note}` — the same ruling landed
         # on `living-once-never` in lesson_01 and the two must not ship as two
         # shapes. The `note` says what to DO with the answer, which is what
         # keeps it the right side of §8.10.
         "self_check": {
             "question": "Now look back at your four marks. Did you have it?",
             "options": [
                 "Yes — I marked what settles it, and nothing else.",
                 "Partly — I marked one of them, and something else as well.",
                 "No — I went for the vivid facts and missed the quiet ones.",
             ],
             "note": "Nobody marks this but you. The facts you marked wrongly "
                     "are the ones to read again before the next cell.",
         },

         # Exactly four cases, each with exactly four features. The renderer
         # must not accept three or five of either.
         "cases": [
             {"id": "c1",
              "label": "Mystery cell 1",
              "tab_label": "Cell 1",
              "description": "About 0.05 mm long. It is green, and it swims "
                             "using one long whip at the front.",
              "features": [{"text": "It can swim.",
                            "settles": False,
                            "why": "A sperm cell swims. So does a white blood "
                                   "cell, through tissue. Moving on your own "
                                   "tells you nothing about whether you are "
                                   "an organism."},
                           {"text": "It is green, and makes its own food from "
                                    "light.",
                            "settles": True,
                            "why": "Nothing in an animal body makes its own "
                                   "food. A cell feeding itself is not being "
                                   "fed by an organism — so it is one."},
                           {"text": "It has mitochondria.",
                            "settles": False,
                            "why": "Every cell in both columns has "
                                   "mitochondria. A fact that is true of "
                                   "everything discriminates nothing."},
                           {"text": "It is only 0.05 mm long.",
                            "settles": False,
                            "why": "Size never settles it. Your cheek cell is "
                                   "0.06 mm and a Paramecium is 0.25 mm — the "
                                   "bigger one is the organism here, and that "
                                   "is a coincidence."}],
              "verdict_label": "It is an organism",
              "answer": "Euglena — a single-celled organism.",
              "why": "Green, so it makes its own food; a flagellum, so it can "
                     "go and find light. One fact out of four did the work."},
             {"id": "c2",
              "label": "Mystery cell 2",
              "tab_label": "Cell 2",
              "description": "It has a long tail and swims fast in one "
                             "direction. It never feeds.",
              "features": [{"text": "It has a tail and swims.",
                            "settles": False,
                            "why": "So does Euglena. Swimming is the most "
                                   "misleading fact on this page."},
                           {"text": "It never feeds.",
                            "settles": True,
                            "why": "An organism must take in nutrition. A "
                                   "cell that never feeds is being supplied "
                                   "by something larger — and everything it "
                                   "will ever spend was loaded before it set "
                                   "out."},
                           {"text": "It carries half a set of chromosomes.",
                            "settles": True,
                            "why": "Half a set is only useful if it is going "
                                   "to be added to another half. Nothing that "
                                   "lives on its own has half its "
                                   "instructions."},
                           {"text": "It is packed with mitochondria.",
                            "settles": False,
                            "why": "True, and it tells you the cell works "
                                   "hard. A Paramecium is packed with them "
                                   "too."}],
              "verdict_label": "It is part of an organism",
              "answer": "A sperm cell — one cell of a multicellular organism.",
              "why": "Two facts settled it, and neither was the swimming. "
                     "Some cases have more than one discriminator; the skill "
                     "is spotting which facts qualify, not counting them."},
             {"id": "c3",
              "label": "Mystery cell 3",
              "tab_label": "Cell 3",
              "description": "It has no nucleus at all. In warm conditions it "
                             "divides about every twenty minutes.",
              "features": [{"text": "It has no nucleus.",
                            "settles": False,
                            "why": "A red blood cell has no nucleus either, "
                                   "and that is a part of you. Missing a "
                                   "nucleus settles nothing on its own."},
                           {"text": "It divides on its own, over and over.",
                            "settles": True,
                            "why": "A red blood cell can never divide again. "
                                   "A cell that makes more of itself unaided "
                                   "is reproducing — the sixth life process — "
                                   "and so it is an organism."},
                           {"text": "It is very small — about 0.002 mm.",
                            "settles": False,
                            "why": "Size again. It is the smallest thing on "
                                   "the slide and it is still a complete "
                                   "organism."},
                           {"text": "Its DNA sits in a loose loop in the "
                                    "cytoplasm.",
                            "settles": True,
                            "why": "No cell in your body does this. Yours "
                                   "keep their DNA inside a nucleus, always. "
                                   "Loose DNA is a different kind of cell "
                                   "entirely."}],
              "verdict_label": "It is an organism",
              "answer": "A bacterium — a single-celled organism with no "
                        "nucleus.",
              "why": "Its instructions are present; only the container is "
                     "missing. That is exactly why it can divide when a red "
                     "blood cell cannot."},
             {"id": "c4",
              "label": "Mystery cell 4",
              "tab_label": "Cell 4",
              "description": "It changes shape constantly, flows around a "
                             "smaller cell, and takes it inside itself.",
              "features": [{"text": "It changes shape as it moves.",
                            "settles": False,
                            "why": "A white blood cell squeezes out of a "
                                   "blood vessel and crawls through tissue by "
                                   "changing shape. This is not a giveaway."},
                           {"text": "It flows around another cell and engulfs "
                                    "it.",
                            "settles": False,
                            "why": "This is the hardest one. A white blood "
                                   "cell engulfs bacteria in exactly this way "
                                   "— and it is part of you. Behaviour is not "
                                   "evidence."},
                           {"text": "Nothing else feeds it and nothing else "
                                    "positions it.",
                            "settles": True,
                            "why": "It is on its own. Whatever it eats, it "
                                   "found; wherever it is, it went. That is "
                                   "an organism."},
                           {"text": "It has a vacuole that keeps filling with "
                                    "water and squeezing it out.",
                            "settles": True,
                            "why": "Your body holds the fluid around its "
                                   "cells steady, so no cell of yours needs "
                                   "to bail out. A cell that must manage its "
                                   "own water is not inside a body."}],
              "verdict_label": "It is an organism",
              "answer": "Amoeba — a single-celled organism.",
              "why": "The two most vivid facts — shape-changing and engulfing "
                     "— are the two that settle nothing, because a white "
                     "blood cell does both. The quiet facts did the work."},
         ]},

        {"type": "misconception", "anchor": "s-think", "id": "think-again"},
        {"type": "quiz", "anchor": "s-ladder", "ref": "ladder"},
        {"type": "summary", "anchor": "s-keynote", "ref": "key_note"},
    ],

    # §3.7 — the violet layer holds one bare paragraph.
    "stretch": [
        {"type": "explainer", "text": "Euglena is the awkward one. It is "
                                      "green, traps light and makes its own "
                                      "food like a plant; it also swims after "
                                      "food with a flagellum and can feed "
                                      "like an animal in the dark. Biologists "
                                      "spent a century arguing about which "
                                      "kingdom it belonged in, and the answer "
                                      "they settled on was that the question "
                                      "was wrong — it belongs to neither, and "
                                      "single-celled life does not sort "
                                      "neatly into plant and animal at all. "
                                      "Being hard to classify is not a fault "
                                      "in the organism. It is information "
                                      "about the categories."},
    ],

    # R12 — present and empty. Empty renders nothing at all, not a placeholder.
    "support": [],

    "activities": [
        # ── §3.3 — the microscope bench ──────────────────────────────────
        # ⚑ The gate is a prediction with NO marked answer and NO reveal of any
        # kind: the student commits, the question is REMOVED (gating by
        # absence, `gateOpen`/`scopeOpen` are complementary) and the bench
        # arrives in its place. Nothing ever tells them whether ×400 was right
        # — the instrument is the answer, and RESOLVE[100] is where it lives.
        # That is R3-clean, and it is the only commit in the delivery that
        # produces no response at all. Raised for Design as §8(a)3; authored
        # here as drawn, so `answer` and `reveal` are deliberately absent.
        {"id": "microscope-bench", "kind": "lab",
         "demand": "two mounts, one instrument: find, centre, then climb",
         "eyebrow": "At the bench · two slides",
         "heading": "Pond water, then your own cheek",
         "lede": "Same microscope, same magnifications, two mounts. Find "
                 "something, centre it, then climb — exactly as you learnt.",
         "progress_format": "{n} of {total} mounts seen at ×400",
         "prompt": "Commit first. At which magnification will you first be "
                   "able to tell one pond organism from another?",
         "options": [
             "×40 — the lowest power",
             "×100",
             "×400 — the highest",
             "You never can with a school microscope",
         ],
         "sim": {
             "kind": "microscope",
             # `centre` and `motion` do not exist in shared/ks3.js yet; both
             # need CONTROL_LABELS and wireSim entries (gaps G10, G11).
             "controls": ["specimen", "magnification", "centre", "motion",
                          "focus"],
             # §3.3.2 — the four group captions, as drawn. The engine's own
             # CONTROL_LABELS say "Slide on the stage" for `specimen`; Design
             # says "Mount", and the page is the specification.
             "control_labels": {"specimen": "Mount",
                                "magnification": "Objective",
                                "centre": "Move the slide to",
                                "motion": "Movement"},

             # G9 — two mounts on ONE instrument. The engine renders one
             # specimen per payload and has no tab to swap between them.
             # `specimen` is the classifier string _specimen_kind() reads;
             # `label` is the button caption. `alt` is the canvas's
             # aria-label and replaces SIM_ARIA's generic narration, because
             # Design authored one per mount.
             "mounts": [
                 {"id": "pond",
                  "label": "Pond water",
                  "specimen": "pond water",
                  "note": "The dots scattered between them are bacteria, "
                          "about 0.002 mm long. Even at ×400 they are two "
                          "pixels of nothing — you can see that they are "
                          "there, not what they are. Every organism on this "
                          "slide is doing all seven life processes for "
                          "itself.",
                  # ⭐ The page telling the truth about its own model, and the
                  # justification for the centre control against the engine's
                  # swimming (F33). This sentence is why the organisms must be
                  # held still.
                  "caption": "Real ones swim out of the field in seconds. "
                             "These are held for you, and the slide moves "
                             "when you ask it to.",
                  "alt": "A microscope field of pond water containing an "
                         "amoeba, two paramecia, three euglena and scattered "
                         "bacteria at various depths.",
                  # Positions and depths are millimetres on the slide.
                  "organisms": [
                      {"kind": "amoeba",
                       "x": -0.9,
                       "y": 0.3,
                       "depth": -0.045,
                       "len": 0.3,
                       "seed": 0.4},
                      {"kind": "paramecium",
                       "x": 0.15,
                       "y": -0.1,
                       "depth": 0,
                       "len": 0.25,
                       "seed": 1.1},
                      {"kind": "euglena",
                       "x": 0.58,
                       "y": 0.46,
                       "depth": 0.05,
                       "len": 0.05,
                       "seed": 2.3},
                      {"kind": "euglena",
                       "x": -0.3,
                       "y": -0.58,
                       "depth": -0.02,
                       "len": 0.05,
                       "seed": 3.7},
                      {"kind": "paramecium",
                       "x": 1.45,
                       "y": 0.95,
                       "depth": 0.03,
                       "len": 0.25,
                       "seed": 0.8},
                      {"kind": "amoeba",
                       "x": 1.95,
                       "y": -1.15,
                       "depth": -0.07,
                       "len": 0.3,
                       "seed": 2.9},
                      {"kind": "euglena",
                       "x": -1.6,
                       "y": 1.1,
                       "depth": 0.015,
                       "len": 0.05,
                       "seed": 1.6},
                  ]},
                 {"id": "cheek",
                  "label": "Cheek cells",
                  "specimen": "cheek cells",
                  "note": "One layer, one shape, no movement. Racking the "
                          "focus finds nothing behind them, because a smear "
                          "is a sheet. Every cell here does one job, and none "
                          "of them is an organism.",
                  "caption": "Stained, so the nuclei show. Unstained you "
                             "would see almost nothing.",
                  "alt": "A microscope field of flat, still cheek cells in a "
                         "single layer, each with a stained nucleus.",
                  # One layer, so racking the focus finds nothing behind it.
                  "organisms": []},
             ],
             "start_mount": "pond",

             # G10 — panning is a pure translation of the field, applied only
             # on the pond mount; the whole group disappears on cheek. The
             # labels are authored teaching language — how the lesson refers to
             # an organism the student cannot yet name — and must NOT be
             # derived from `kind`. shared/ks3.js line ~1882 already
             # carries the lower-case forms for the "In focus" readout; the
             # two must agree.
             #
             # ⭐ Centring and focusing are two separate operations and the
             # instrument makes the student do both: pan to the blob and the
             # readout still says "the slipper", because the wheel has not
             # moved. The engine, which swims the organisms, cannot teach that.
             "centres": [
                 {"id": "amoeba", "label": "The blob", "x": -0.9, "y": 0.3},
                 {"id": "paramecium",
                  "label": "The slipper",
                  "x": 0.15,
                  "y": -0.1},
                 {"id": "euglena",
                  "label": "The green spindle",
                  "x": 0.58,
                  "y": 0.46},
             ],
             "centre_offered_on": ["pond"],

             # G11 — a reduced-motion escape hatch the STUDENT controls, on top
             # of the prefers-reduced-motion query. With motion off the cilia
             # stop, the contractile vacuoles freeze and the euglena stops
             # bending: the drawing is complete, just still. The two labels are
             # content, not a generic on/off.
             "motion_toggle": True,
             "motion_default": True,
             "motion_labels": ["Swimming", "Held still"],

             # Keyed by TOTAL magnification. The only cream-on-dark inset in
             # the delivery, and where the lesson answers its own gate.
             "resolve_notes": {
                 40: "Specks, and one or two shapes. You can see that "
                     "something in there is alive. You cannot see what it is, "
                     "and nothing you have been told about cilia or eyespots "
                     "is visible yet.",
                 100: "Outlines. You can now tell one kind from another by "
                      "shape and by how it moves — but the insides are still "
                      "a blur.",
                 400: "Structures. Cilia, the eyespot, a vacuole filling and "
                      "emptying. The field is 0.45 mm across, so almost all "
                      "of the slide has gone.",
             },
         }},

        # ── §3.6 — one misconception block, two misconceptions ───────────
        # §4.8.2's `statements` shape. Both are static and open: no gate, no
        # flip. `quote` is the page's wording (the student's voice) and is NOT
        # the register's `statement` (the diagnostic wording) — the two differ
        # by design and both are needed. The renderer adds the curly quotes.
        {"id": "think-again", "kind": "confrontation",
         "demand": "resolve B1-04's rule against a bacterium, then kill "
                   "'one cell means simple'",
         "statements": [
             {"targets": "CELL-13",
              "quote": "No nucleus means no instructions — so a bacterium "
                       "cannot divide.",
              # ⚑ CONTRACT-BEARING. The <em> on *had* is load-bearing.
              # "Two lessons ago" is true only while B1-05 sits between this
              # lesson and B1-04 — F38, and Mide's call (§8(b)2).
              "answer": "Two lessons ago that was exactly right, about a red "
                        "blood cell. It is wrong here, and the difference is "
                        "worth being precise about. A red blood cell "
                        "<em>had</em> a nucleus and destroyed it, and the DNA "
                        "went with it. A bacterium never had one: its DNA is "
                        "there, in a loose loop in the cytoplasm, with no "
                        "membrane around it. Instructions present, container "
                        "absent. That is why a bacterium can divide every "
                        "twenty minutes and a red blood cell can never divide "
                        "again."},
             {"targets": "CELL-08",
              "quote": "One cell means simple.",
              "answer": "Compare what you have just looked at. Your cheek "
                        "cell has a membrane, cytoplasm, a nucleus and "
                        "mitochondria, and it is fed, cleaned, positioned and "
                        "defended by the rest of you. A Paramecium has all of "
                        "that plus cilia to swim, an oral groove to feed, "
                        "food vacuoles to digest, and vacuoles that bail out "
                        "water it cannot stop taking in. It has more "
                        "machinery than your cell, not less, because there is "
                        "nobody to do any of it for it."},
         ]},
    ],

    # §5.8 — four rungs, two the page marks and two the student marks. The key
    # fixes the rung NUMBER (recall 1, apply 2, explain 3, produce 4); `title`
    # is Design's authored name for it and replaces the derived "1 · Recall".
    # Criteria counts vary per rung, 5 and 4, and are authored.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Discriminate",
            "q": "A single cell moves on its own, has mitochondria, and is "
                 "about 0.05 mm long. Which of these would settle whether it "
                 "is an organism or part of one?",
            "options": [
                "How fast it moves",
                "Whether it feeds itself, or is fed",
                "How many mitochondria it has",
                "Whether it is bigger than one of your cells",
            ],
            "answer": 1,
            "feedback": {
                0: "Speed is a detail about the movement. Movement itself "
                   "does not discriminate, so nothing about it can.",
                2: "Both kinds have mitochondria, and busy cells of both "
                   "kinds have many. A shared feature cannot separate them.",
                3: "Size never settles it. A Paramecium is four times the "
                   "size of your cheek cell, and Euglena is smaller than it.",
            }},
        # ⚑ CONTRACT-BEARING RUNG — see the CELL-08 note in the module
        # docstring. Question, correct option and the option-1 correction all
        # carry the pair.
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A red blood cell has no nucleus and can never divide. A "
                 "bacterium has no nucleus and divides every twenty minutes. "
                 "What explains the difference?",
            # ⊕ MRB-177, ruled 17 Aug 2026 — the three distractors now state
            # wrong RULES, in the same shape as the correct option. The
            # correct option and its index are unchanged, and the option-1
            # correction still carries the CELL-08 pair verbatim.
            "options": [
                "The bacterium still has its DNA, loose in the cytoplasm; the "
                "red blood cell lost its DNA with its nucleus",
                "A smaller cell divides more easily, so the smallest cells "
                "are the ones that divide fastest",
                "A cell that loses its nucleus later in life can still "
                "divide, because it had one to begin with",
                "Dividing needs no instructions at all, so any cell without "
                "a nucleus can still copy itself freely",
            ],
            "answer": 0,
            "feedback": {
                1: "Size has nothing to do with it. The difference is about "
                   "the instructions, not the effort.",
                2: "Having had one does not help: the red blood cell "
                   "destroyed its nucleus and lost the DNA with it. The "
                   "bacterium never had a nucleus at any point.",
                3: "Nothing copies itself without instructions. Every new "
                   "bacterium gets a full copy of the loop.",
            }},
        "explain": {
            "title": "Rung 3 · Explain both sides",
            "q": "A Paramecium and one of your cheek cells are both single "
                 "cells. Explain why the Paramecium needs cilia, an oral "
                 "groove and a contractile vacuole, and why your cheek cell "
                 "needs none of the three. Your answer must say something "
                 "about both cells.",
            "field_label": "Your explanation",
            "placeholder": "The Paramecium needs… whereas the cheek cell…",
            "success": [
                "Says the Paramecium has to carry out all seven life "
                "processes by itself.",
                "Links each of the three structures to a process it does for "
                "itself — moving, feeding, and getting rid of water.",
                "Says the cheek cell does one job and the rest of the body "
                "does the others for it.",
                "Names at least one thing the body does for the cheek cell — "
                "feeds it, moves things to it, holds it in place, or keeps "
                "the fluid around it steady.",
                "Ends on the discriminator rather than on size or on how "
                "interesting either cell looks.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A student finds a single cell in a drop of water from a "
                 "plant pot. It has a wall, changes shape a little, has no "
                 "chloroplasts, and buds off smaller copies of itself. They "
                 "say it must be part of a plant because it has a wall. Say "
                 "whether they are right, which fact you would use instead, "
                 "and what you would still want to check.",
            "field_label": "Your answer",
            "placeholder": "The wall does not settle it, because…",
            "success": [
                "Says a wall does not settle it, and gives a reason — walls "
                "are not unique to plants.",
                "Picks budding off copies of itself as the fact that does the "
                "work, and says why: it is reproducing on its own.",
                "Says having no chloroplasts does not rule a plant cell out "
                "either, using the root cell as the reason.",
                "Names something they would still check — whether it feeds "
                "itself, or whether it is attached to anything larger.",
            ]},
    },

    "key_note": "A unicellular organism is one cell that does all seven life "
                "processes for itself. Its adaptations — cilia, an oral "
                "groove, a contractile vacuole, a loose loop of DNA — are "
                "what a whole organ system does for one of your cells.",

    # ---- navigation and framing (§4.8.1) --------------------------------
    # §2.4 — four stages, two authored label sets, neither derivable from the
    # block titles. `short` is ≤6 characters for the 104px mono column.
    # ⭐ Stage 2 names STATES, not a count — the best-formed gate in the
    # delivery, and the shape the others should migrate to.
    # ⚑ Stage 4: `ladder_complete` ticks on two button presses today, with an
    # empty textarea and zero criteria ticked (F31), and it is the first stage
    # in the delivery that can REGRESS, because "Retry my misses" clears
    # `checked` (F32). Whether `done_when` needs a `monotonic` flag is Code's.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "What settles it",
         "done_when": "committed"},
        {"anchor": "s-scope", "short": "SCOPE", "label": "Two slides",
         "done_when": "states_seen", "states": ["pond:400", "cheek:400"]},
        {"anchor": "s-settle", "short": "SETTLE",
         "label": "Four mystery cells",
         "done_when": "all_cases_revealed", "threshold": 4},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # §4.8.1 B + gaps G5 / G6. Fourth distinct position for this box across
    # five pages, so placement is authored and never guessed.
    "key_facts": [
        {"id": "kf-one-cell-all-seven",
         "text": "One cell doing all seven life processes is an organism. One "
                 "cell doing one job is part of one.",
         "eyebrow": "Key fact",
         "placement": "inside:s-compare",
         "ground": "card"},
    ],

    # §4.8.1 C — sixth authored in-page anchor across five pages.
    "tutor": {"prompt": "Not sure which fact settles it?",
              "cta": "Ask about this lesson",
              "anchor": "s-settle"},

    # §4.8.1 D — lab safety, not copyright. Rendered alongside LEGAL_LINE.
    "safety_note": "Pond water is not sterile. Keep it away from your mouth "
                   "and cuts, seal slides with a coverslip, and wash your "
                   "hands before you leave the lab.",

    "ks4_becomes": "Bacterial cell structure, culturing microorganisms, and "
                   "how single-celled organisms cause and fight disease.",

    "ws": ["experimental-skills-and-investigations"],
    "review_state": "draft",
}
