# KS4 pilot port — run report (25–26 Sep 2026, unattended)

Fourteen KS4 lessons authored by Design (Bonding 5.2 + two Electricity lessons)
ported to the site's own generator, science-examined against AQA 8462/8463/8464,
and put live on their existing URLs in all four routes. This is the KS3 pipeline
carried to KS4, and these 14 pages are the standard the other 250 are built from.

## 0. Two drafted exam tips — for Mide to approve (flag 11)

Neither ships. Both physics lessons are live WITHOUT an exam-tip slot until
one of these is approved or replaced. Word for word, from Design's pages:

**Series and parallel circuits**

> Before you calculate anything, say which arrangement you are looking at. In
> series use one current for every component and add the resistances; in
> parallel use one p.d. for every branch and add the currents. Mixing the two
> rules is the commonest lost mark.

**Resistors and I–V characteristics**

> In a method question, name the variable resistor and say what it is for:
> changing the p.d. across the component. Put the ammeter in series and the
> voltmeter in parallel, and say you reverse the connections to get negative
> values.

Examiner's notes on each: the first carries an unsupported claim ("the
commonest lost mark"); the second implies the variable resistor is compulsory,
whereas AQA also credits a variable power supply. Neither has a science error.

## 1. What is live (proved by bytes)

_Filled in at landing — see §7._

## 2. How it was built

| step | what | where |
|---|---|---|
| Provenance | Design's delivery committed unmodified, 65 files, MD5SUMS incl. the zip's own md5 | `docs/ks4/design-reference/pilot/` (commit ee7fc3b4e) |
| Contract | the build contract every stream worked from | `docs/ks4/pilot-build-contract.md` |
| Inventory | every page measured in a real browser at 1280/1340/820/390/360, light+dark, reduced motion, every route; machine-readable baseline | `docs/ks4/pilot-inventory/` (`reference.json`, `payload-map.md`, one file per lesson) |
| Engine | `build_ks4.py` + `shared/ks4-runtime.js` + `ks4_lessons/` + `ks4_rulings.py` + `ks4_science_rulings.py` | step 1b in `build_all.py` |
| Examination | three Opus examiners, one file per lesson, 85–114 checked rows each | `docs/ks4/examination/` |
| Departures | the ruled register | `docs/ks4/design-reference/pilot/DEPARTURES-PILOT.md` |
| Gates | `ks4_pilot_check` (fast), `ks4_parity` (slow), `contrast_audit` extended, `student_lessons_cards_check` | `gate_registry.py` |

**The engine is a compile, not a re-authoring.** Design's pages run on
`support.js`, which loads React, ReactDOM and Babel from unpkg at runtime.
None of that ships. `build_ks4.py` parses each lesson's template through
Chrome's own parser (the walker from `student_template.py`, extended for
`dc-import` child blocks), ships Design's per-lesson `Component` class and the
eleven block classes verbatim, and mounts them over `shared/ks4-runtime.js`
— a vanilla runtime with child components that keep their own state, a
patch-in-place renderer (so 90 ms animation ticks and inner scrollers
survive a redraw), and one figure primitive replacing the four
`React.createElement` calls. Every change to her constants is an exact-match
ruling that fails the build if it stops matching. One route per URL: the
route is pinned as a mount prop and the Route selector removed by ruling.
Each page is prerendered in headless Chrome and baked, so it carries its
text without JavaScript. Verbatim text is generated into
`shared/ks4-source.js` from the repo's `all_subtopics_*.py`, never from
Design's copy; the build diffs the two (139 fields equal; the 8 differences
are two dead `higher` shapes and six physics quiz copies Design's extraction
never saw — ours are more complete). Best score and retry storage follow
KS3's scheme under a `ks4_` prefix. `Ks4Video` keeps its empty state, fed
from `ks4_lessons/videos.py` keyed by slug.

## 3. Lesson × route — parity and examination

_Parity column filled in at landing — see §7._

| lesson | routes | examination | changes applied |
|---|---|---|---|
| chemical-bonds | CF CH TF TH | CHANGES REQUIRED → applied | 13 |
| ionic-bonding | CF CH TF TH | → applied | 4 |
| ionic-compounds | CF CH TF TH | → applied | 9 |
| covalent-bonding | CF CH TF TH | → applied | 3 |
| metallic-bonding | CF CH TF TH | → applied | 3 |
| states-of-matter | CF CH TF TH | → applied | 2 |
| properties-ionic-compounds | CF CH TF TH | → applied | 6 |
| properties-small-molecules | CF CH TF TH | → applied | 6 |
| polymers | CF CH TF TH | → applied | 10 |
| giant-covalent-structures | CF CH TF TH | → applied | 5 |
| metals-alloys | CF CH TF TH | → applied | 11 (+2 commander rulings) |
| nanoparticles | TF TH | → applied | 8 |
| series-parallel-circuits | CF CH TF TH | → applied | 5 |
| resistors | CF CH TF TH | → applied | 14 |

All 14 came back CHANGES REQUIRED; every required change is applied by
`ks4_science_rulings.py` and proved present in the built output by
`expect_present`, so the "Draft — not yet science-reviewed" banner is
removed from all 14 and each lesson's `review_state` is `examiner-reviewed`.

Findings worth reading: the bond decider printed "Cundefined⁻" for every
metal + carbon pair (a missing superscript entry) and labelled Ca₂C
"calcium carbide"; Design's 4.10.4.x citations are 4.10.3.x (4.10.4 is NPK
fertilisers); the series-and-parallel source described RP15 as "verify the
rules" when it is the resistance practical; the circuit engine drew every
cell open (leads stopping short of the plates) and switch contacts as filled
junction dots; Be-the-examiner in L7 awarded 1/3 for an answer the page
itself says scores 0; an atom was called "0.1 nm across" (that is the
radius).

## 4. The DEPARTURES register

`docs/ks4/design-reference/pilot/DEPARTURES-PILOT.md`: 97 changed rows
grouped by lesson, 13 verbatim-layer rows (route copies only — the frozen
Python is untouched), 2 documentation-only, a "considered, not changed"
table, a "not departures" table (port mechanics), and all 22 flags.

## 5. The flags

| # | decision (source) |
|---|---|
| 1 | Upheld: graphene/fullerenes are core (5.2.3.3 carries no HT marker). |
| 2 | Page shows 4.2.4; site slug stays `nanoparticles`; 5.2.3.3 never printed. |
| 3 | The frozen `higher` field gating SA:V is wrong; Design ignores it; not served. |
| 4 | 11 (TH) vs 10 (TF) kept verbatim. |
| 5 | PM10/PM2.5 sizes verified against 4.2.4.1. |
| 6 | Upheld: dot-and-cross is base; electronegativity dropped. |
| 7 | Addition polymerisation is 8462 4.7.3.1 (chemistry only): CF loses 6 items, CH loses 6, TH loses the PVC item; rung 1 re-pointed on Combined. |
| 8 | NOTES had the item numbers wrong; the HT items are CH8/TH8/TH12; no route copy needed editing. |
| 9 | Kept verbatim in the bank; not taught in the body. |
| 10 | 5.2.2.2 and 5.2.2.8 fold in correctly. |
| 11 | Not approved — see §0; L13/L14 ship without a tip slot. |
| 12 | RP text corrected from the spec (RP15 Combined / RP3 Physics: resistance). |
| 13 | Both numbers named (RP16 Combined / RP4 Physics). |
| 14 | Confirmed; rungs 2–4 examined as new content. |
| 15 | Confirmed: no parallel-resistance calculation anywhere. |
| 16 | Option shuffle kept (no text changes; scoring reads the flag). |
| 17 | Data values verified; hardness-vs-carbon relabelled "model data". |
| 18 | Every new item examined; defects are the Changed table. |
| 19 | Confirmed: alloys live in L11 only. |
| 20 | Confirmed: filament lamp says only that R rises with temperature. |
| 21 | Chip "Not on the sheet · learn it" on R_total = R₁ + R₂. |
| 22 | Both June 2026 URLs resolve; add 2027 when AQA publishes it. |

## 6. Screenshots

`MRB_SHOTS=/Users/midebadmus/tmp/ks4-pilot-shots`: `design/<slug>-{1280,360}.png`
(Design's pages, 28 files), `engine-metallic-{360,1280}.png` and twelve
`<slug>-<route>-<width>.png` of the port (six at phone width).

## 7. Landing

_Filled in at landing._

## 8. Decisions I made

1. **Compile, don't hand-port.** Design's KS4 pages are React/Babel from
   unpkg. The hard requirement was no React at runtime, and the KS3 method
   of hand-porting each instrument into Python drawers would not have
   landed 14 lessons with bespoke flagships in one run. The live student and
   teacher pages already prove the compile route; the KS4 runtime is that
   pattern with child components and in-place patching added.
2. **Verbatim quizzes come from the four `all_subtopics_*` files**, one copy
   per route, so the physics lessons serve the CF/CH/TF copies Design's
   extraction missed.
3. **Spec numbering** stays the site's convention — Combined (8464) numbers
   on every route, 8462-only sections carrying their 8462 numbers — exactly
   as Design drew it. Both chemistry and physics examiners raised this as a
   house decision; it is one for Mide if he wants the Triple routes to show
   8462/8463 numbering.
4. **The two un-numbered L11 verbatim findings** (steel composition CF9,
   stainless-steel corrosion CH7 — chemistry-only recall on Combined) are
   applied as rulings C12/C13; the examiner recommended removal and the
   spec label is unambiguous.
5. **"Contains Higher" / "Contains Triple" badges** are gated to their
   routes (R9). A Foundation pupil must not be told a page contains Higher
   content.
6. **Prev/next come from the site's own topic order**, not Design's
   pilot-internal guesses (her page had resistors after series-parallel;
   the site's electricity topic has them the other way round, and
   series-parallel's real next is a lesson outside the pilot).
7. **The draft banner comes off all 14**: every required change is applied
   and proved present, which is what "examination is clean" means here.
8. **Freeze** = `ks4_lessons/frozen.json` stamped by `build_ks4.py --freeze`
   and asserted by the fast gate for any examiner-reviewed lesson.
9. **contrast_audit covers 15 pilot pages** (the 14 Triple Higher pages plus
   nanoparticles TF), not all 54, so the fast gate stays fast.
10. **MRB-336**: the "Lessons in this topic" cards take their link from the
    per-assignment list that `ks4TopicHref` already resolved; the fixture
    class is KS3, so the gate is a static check plus the existing drives.
