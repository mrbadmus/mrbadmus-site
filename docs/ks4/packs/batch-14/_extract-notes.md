# Batch 14 — extraction notes

Facts only, read straight from the 15 extracted files in
`04-checked-science-source/` (each file's header gives the routes; `##`
section presence gives everything else). No route-copy `quiz` section exists
in ANY of the 15 files — every route a lesson appears on serves the identical
TH quiz list, so "quiz count per route" below is one number covering every
route listed. The only field that ever differs by route is `higher`.

| # | Lesson | Routes | Quiz count (same on every route) | examiner_tip | fifas | equations | rp (verbatim) | variables |
|---|---|---|---|---|---|---|---|---|
| 1 | pure-substances | CF CH TF TH | 2 | no | 0 | none | none | none |
| 2 | formulations | CF CH TF TH | 2 | no | 0 | none | none | none |
| 3 | chromatography | CF CH TF TH | 2 | no | **1** | 1 — Rf = distance moved by substance ÷ distance moved by solvent front | verbatim (RP1 — paper chromatography, Rf values vs references, see below) | 1 — `Rf` |
| 4 | testing-for-gases | CF CH TF TH | 2 | no | 0 | 2 — CO₂+Ca(OH)₂→CaCO₃+H₂O; Cl₂+H₂O→HCl+HClO | none | none |
| 5 | flame-tests | TF TH | 2 | no | 0 | none | verbatim (RP Chemistry 4 — identify ions in an unknown compound, incl. flame tests, see below) | none |
| 6 | instrumental-methods | TF TH | 2 | no | 0 | none | none | none |
| 7 | composition-of-atmosphere | CF CH TF TH | 2 | no | 0 | none | none | none |
| 8 | alternative-metal-extraction | CH TH | 2 | no | 0 | 2 — Cu²⁺(aq)+Fe(s)→Cu(s)+Fe²⁺(aq); CuS+O₂+H₂SO₄→CuSO₄+S+H₂O | none | none |
| 9 | life-cycle-assessment | CF CH TF TH | 2 | no | 0 | none | none | none |
| 10 | reducing-use-of-resources | CF CH TF TH | 2 | no | 0 | none | none | none |
| 11 | corrosion-prevention | TF TH | 2 | no | 0 | 1 — 4Fe+3O₂+2xH₂O→2Fe₂O₃·xH₂O (rusting) | none | none |
| 12 | alloys-useful-materials | TF TH | 2 | no | 0 | none | none | none |
| 13 | ceramics-polymers-composites | TF TH | 2 | no | 0 | none | none | none |
| 14 | haber-process | TF TH | 2 | no | **1** | 1 — N₂(g)+3H₂(g)⇌2NH₃(g) (450°C, 200 atm, iron catalyst) | none | none |
| 15 | npk-fertilisers | TF TH | 2 | no | 0 | 2 — NH₃+HNO₃→NH₄NO₃; 2NH₃+H₂SO₄→(NH₄)₂SO₄ | none | none |

Two `fifas` lessons (#3 chromatography, #14 haber-process), matching
BATCH-PLAN's FIFA column exactly. The CFIFA form (step C) was appended to
both files, the four FIFA steps kept byte-identical, Convert step added.
**Neither needed a real conversion** — chromatography's Rf calculation uses
two distances already in matching cm, and Rf itself is dimensionless;
haber-process's FIFA explains a rate-vs-yield trade-off rather than
calculating from a measured quantity, so there is nothing to convert at all
(same shape as batch-12's half-equations case). `rp` is a dedicated,
populated field on chromatography (RP1) and flame-tests (RP Chemistry 4) —
both named in BATCH-PLAN's RP column — kept verbatim.

## wrong_explanations key check

All 30 quiz items across the 15 files were checked mechanically: every item
has exactly 4 options, the `true` option sits at index 0 on all 30, and every
item's `wrong_explanations` keys match exactly the indices of its 3 wrong
options (`1,2,3`) — no shifted index anywhere. **No shifted-key defect found
anywhere in this batch.**

## Anything odd

1. **Spec-number agreement with BATCH-PLAN.md is perfect — all 15 of 15 rows
   match exactly**, including the one ranged spec (`5.8.2.1–5.8.2.4` for
   testing-for-gases and `4.8.3.6–4.8.3.7` for instrumental-methods, both
   reproduced verbatim in the header) and the eight separate-science-
   prefixed rows (flame-tests, instrumental-methods, corrosion-prevention,
   alloys-useful-materials, ceramics-polymers-composites, haber-process,
   npk-fertilisers, all `— · 8462 4.x.x.x`). Continues the zero-disagreement
   run from batch-12 and batch-13.

2. **FIFA/RP/equations columns also match BATCH-PLAN exactly on all 15
   rows** — no mismatch anywhere in this batch's plan at all.

3. **No `examiner_tip` anywhere in this batch** — same pattern as every
   prior batch (4–13). All 15 files omit the `## examiner_tip` section
   entirely.

4. **No filename needed renaming** — all 15 extracted filenames were already
   clean (no spaces, no parentheses). Step B of the task was not needed.

5. **No subject:slug collisions were actually tested** — all 15 slugs were
   passed as `chemistry:<slug>` from the start (BATCH-PLAN marks every row
   `Chem`), so the extractor never searched biology/physics for them; the
   console output was 15 clean `wrote …` lines with no collision error
   printed for any slug. Same reasoning as batch-13's note 5.

6. **`alternative-metal-extraction` is the only lesson in this batch with NO
   `## higher` section at all** — its two routes (CH, TH) are both
   higher-tier, so there is no main-TH-vs-higher-copy question to ask, and
   the canonical record carries no `higher` field. Every other one of this
   batch's 14 lessons has a `## higher` section AND at least one route-copy
   section (unlike batch-13, where two TH-only lessons had a `higher`
   section but no sibling route to diff against — here every lesson that
   HAS `higher` also has a route to copy it against).

7. **Every `higher — … copy` section renders `null`** across all 14 lessons
   that have one (18 copy-sections total: 7 lessons with a single
   Triple-Foundation-only copy since they are TF/TH routes, 7 lessons with
   both a Combined Foundation and a Triple Foundation copy since they are
   CF/CH/TF/TH-route lessons). No route actually diverges in its `higher`
   wording within this batch — same finding as batches 9–13.

8. **No `canonical_record` WARNING was printed by the extractor** — the
   extraction run's console output was 15 `wrote …` lines and nothing else.

9. **All 15 lessons' routes match BATCH-PLAN's routes column exactly** — no
   CF/CH/TF/TH discrepancy anywhere.

10. **This batch spans four different AQA topics** (8462/8464 §4.8–4.10:
    analysis, the atmosphere, and resources) rather than one continuous
    topic the way batch-13 (organic, §4.7) and batch-12 (cells/rates/
    equilibrium, §4.5–4.6) did. The diagram-library audit reflects this
    split: analysis-topic lessons (chromatography, flame-tests,
    composition-of-atmosphere) matched existing `figlib/chemistry.py`
    figures built with the exact same names as the lessons themselves, while
    the resources-topic lessons (corrosion-prevention, alloys-useful-
    materials excepted, ceramics-polymers-composites, haber-process,
    npk-fertilisers) are almost entirely unillustrated — five of this
    batch's fifteen lessons have no matching figure anywhere in the repo,
    the highest proportion of genuine gaps seen in batches 9–14.

11. **`alloys-useful-materials` matched a figure built for a different
    topic entirely.** `shared/ks4-diagrams.js`'s `metallic(cols, rows, opt)`
    was written for the giant-metallic-structures bonding topic and its
    `opt.alloy` option — oversized atoms disrupting the regular lattice —
    was read in full to confirm it is a genuine mechanistic match (not a
    name collision) before being cited in the README as a direct hit.
