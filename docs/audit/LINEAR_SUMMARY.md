# Phase 1 content audit — Linear summary (MRB-105)

Paste-ready. Source: the 12 `all_subtopics_*.py` data files, audited at source (where fixes land), not generated HTML. Audit script: `audit_content.py`. Full table: `docs/audit/phase1_defects.csv`.

**Coverage:** 264 unique subtopic pages · **865 page-variants** (subject × pathway × tier).

## Defects by severity
- 🔴 critical: 837
- 🟠 major: 2,146
- 🟡 minor: 819
- ⚪ info: 143

## Defects by rule
| Rule | Defect | Severity | Count |
|---|---|---|---|
| 1 (count) | Below floor of 5 questions | critical | 837 |
| 1 (count) | 5–9 questions, below target 10 | major | 28 |
| 1 (register) | No AQA command word in any stem | minor | 819 |
| 1 (triple depth) | Triple quiz identical to Combined; no Triple-only depth | major | 367 |
| 2 (FIFA) | No interactive practice mode (template renders static steps) | major | 210 |
| 2 (FIFA) | Fewer than 3 worked examples | major | 206 |
| 2 (FIFA) | FIFA values identical across tiers (fake differentiation) | major | 96 |
| 3 (common mistake) | First sentence states fact, not the student mistake | major | 827 |
| 4 (menu) | Equations present but no FIFA — deliberate-choice check | info | 143 |
| 5 (tier integrity) | Higher quiz identical to Foundation ("same page, harder badge") | major | 412 |

## The three headline findings

1. **Every page fails the count rule.** All 865 variants are under target; 837 are below the absolute floor of 5. Quiz-length distribution: 2 Qs (666 pages), 3 (135), 4 (36), 5 (28). Nothing reaches 10. This alone caps the value of everything else on the page.

2. **Tier differentiation is structural, not cosmetic — and mostly absent.** The Higher data files are largely the Foundation content plus extra pages; on shared pages the Higher quiz, FIFA set and common-mistake block are byte-identical to Foundation. Confirmed programmatically per subject: physics 50/50 combined + 64/64 triple, biology 67/67 + 87/89, chemistry 61 + 83. The only differentiation lever anyone pulled is an optional `higher_box` prose note present on ~⅓ of pages. So a Higher page today is a Foundation page with 0–1 extra box.

3. **The good news: where questions exist, they're exam-grade.** All three judgement readers independently found distractor quality and exam register to be genuinely strong — wrong options encode real misconceptions and classic working errors (forgot to convert units, wrong rearrangement, diffusion vs active transport, squared the wrong variable), and calculation/Higher stems read like AQA items. The fix is therefore **volume + tier-lift**, not a rewrite of existing items. (Full judgement findings: `docs/audit/judgement/`.)

### Pilot-specific: the Bonding unit needs the content fix, not just the reskin
The chemistry reader checked all 11 Bonding pages (the Phase 2 pilot). Their distractors and register are strong, but every page has **only 2 questions** and **Foundation = Higher = Triple verbatim**. So Phase 2c must lift counts and author real tier differentiation for Bonding — a straight visual port would propagate a 2-question single-difficulty quiz. The two weak per-item spots to clean up in the pilot: `bonding/states-of-matter` and `bonding/polymers` (lookup stems + filler options).

## Nuance on the 827 common-mistake flags
Mechanically correct against the three-beat rule (they don't open by naming the student's mistake), but most are *reformat, not rewrite* — the misconception is present, phrasing just leads with the correction (e.g. "In P = I²R, current is squared, not resistance"). Cheap to fix by inverting the first sentence. Only 38 blocks currently pass the mistake-first pattern.

## Rule 4 — lineup default, not menu
One optional-block lineup (`key_note + common_mistake + matching + quiz`) is shared by 286 page-variants; a second by 110. The template menu is being applied as a default, per the standard's warning.

## Recommended fix priority (for Phase 2 sequencing)
1. **Lift question counts to target** across the site (biggest single win — clears all 837 critical defects).
2. **Author Higher/Triple variants as Higher/Triple** — rearrangement, unit conversion, two-formula chains, Triple-only depth — clearing 412 + 367 major tier defects.
3. **Build FIFA interactive-practice mode** into the redesign template (clears the systemic 210 practice-absent defects) and give FIFA ≥3 escalating, tier-differentiated examples.
4. **Reformat common-mistake blocks** to mistake-first, or cut where no genuine misconception exists.

## Blockers / notes for Mide
- **Linear is not authenticated in this session**, so I could not post to MRB-105 directly. This file is the paste-ready summary. Reactivate MRB-105 with `content_standards.md` as its spec (per the code brief) and paste the above.
- The three companion docs were missing from disk; I recovered them from the brief text into `docs/redesign/`. Confirm they match your latest versions before Phase 2.
- **No content was modified.** This is audit-only. Phase 2 (Bonding pilot) starts only after your review of this table.
