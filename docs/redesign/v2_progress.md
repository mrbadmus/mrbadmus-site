# Bonding v2 — Phase 0 + Phase 1 run · progress / resume file

**Run start:** 19 July 2026 · branch `content/bonding` · worktree `mrbadmus-worktrees/content/bonding`
**Tickets:** MRB-132 (Phase 0 — Make it honest), MRB-133 (Phase 1 — Sharpen what exists)
**Plan of record:** `docs/redesign/council_bonding_review.md` (v2 architecture source) → synthesized into `docs/redesign/architecture_v2.md`.

## Guards

- **HEAD at run start:** `e0f7b46c0970327f578d9cfc13caa0582eb6de06` ("council of five review" — Mide committed the council docs himself, so the pre-flight standalone commit was already done). If HEAD moves mid-run: STOP, first hypothesis is Mide committed via GitHub Desktop.
- **Content freeze:** the 8 protected fields (`quiz`, `matching`, `common_mistake`, `key_note`, `theory`, `fifas`, `higher`, `triple_only`) stay byte-identical in the 4 chemistry data files. SHA256 baseline in scratchpad `freeze_baseline.txt`:
  - `dfed1c59…b79562  all_subtopics_chemistry.py`
  - `3fb40a0d…343740  all_subtopics_chemistry_higher.py`
  - `7f91148b…62d72a9  all_subtopics_chemistry_triple_foundation.py`
  - `8046fb50…2bd7b  all_subtopics_chemistry_triple_higher.py`
- Approved examiner tips: placement may change, text never.
- **No commits at any point.** One consolidated stop at the end (Phase F) with a proposed commit grouping.
- Failure containment: blocked items are skipped and logged here, never kill the run.

## Phase status

| Phase | Item | Status |
|---|---|---|
| Part 0 | Guards + baseline + this file | ✅ done |
| Part 0 | `architecture_v2.md` | ✅ done |
| 0a | TapMatch engine (`shared/tap-match.js`), DnD retired from all 8 match pages; de-leak texts → packet | ✅ done |
| 0b | categorise-bins keyboard fix (bin heads = real buttons, aria-pressed) | ✅ done |
| 0c | Hero aria (role=img + per-state labels on stepper/lattice/two-state) + `mrbEDrift` gated + FIFA CSS gate | ✅ done |
| 0d | quiz.js extraction — verbatim first (rendered-DOM verified: quiz markup byte-identical, engine verbatim), then evolved to v1 | ✅ done |
| 0e | Persistence: `quiz_best_<stId>` (quiz.js), `lab_best_<stId>` (TapMatch + bins), delta at end, retry-misses | ✅ done |
| 1a | PredictWrapper (`shared/predict-wrapper.js`) + hooks in 3 hero modules + 6 authored predict configs (→ packet) | ✅ done |
| 1b | mistakeCheck v2 (reset + item bank; singles migrate unchanged) | ✅ done |
| 1c | Exam-paper quiz (chunks 4/4/4 minus relocations, details, sticky chip, per-chunk check) + 28 checkpoint relocations (→ packet) | ✅ done |
| 1d | Key Note revision card + cover-and-recall (`shared/rd-page.js`), moved last per §3.2 r8 | ✅ done |
| 1e | Mode chooser (Teach me / Labs / Test me) in topic-header, anchors rd-teach/rd-labs/rd-test | ✅ done |
| 1f | Dedup (ionic 6-step+example, covalent 5-step, nanoparticles FIFA boxes) + mistake placement (4× hero, 1× block) + tip split (9× quiz, 3× activity success) | ✅ done |
| 1g | Tone pass (quiz fb, end messages diagnosis+route, RD star routes, bins 🎉 cut) + mono kickers | ✅ done |
| smoke | 2 headless-Chrome iframe drivers, 55/55 assertions PASS (gates, TapMatch, bins keyboard, checkpoints, exam flow, retry-misses, persistence, keynote, modes, variants) | ✅ done |
| V | Determinism: 2 runs → 2,013 HTML byte-identical · freeze: 4 files SHA-OK · non-bonding: zero diff · contrast: 21 pairs, all essential ≥4.79:1 (2 hint tints darkened to #716A60) · keyboard: 154 controls all native buttons/links · 390px probe: 4 pages no overflow · screenshots: 4×390px + reduced-motion metallic (scratchpad) · audit: bonding 0 crit / 0 major (319 minor = frozen length-parity → MRB-122) | ✅ done |
| F | `gate0_packet_bonding_v2.md` + `.rtf` written · review server on :8899 (mrbadmus_site) · commit proposal in packet §8 · Linear comments posted on MRB-132 + MRB-133 (build + verification) | ✅ done |

## Run complete — 19 July 2026

NOTHING COMMITTED. HEAD still `e0f7b46c0`. Working tree = Phase 0 + Phase 1 built and verified.
Awaiting Mide: Gate 0 packet sign-offs (spec defects §1, de-leak texts §2) and Gate 1 pilot review (ionic-bonding, giant-covalent-structures).
Commit grouping proposal: packet §8. Mide commits/pushes via GitHub Desktop only.

## Blocked / skipped log

- (none yet)

## Notes for resume

- Bonding pages render via `make_pathway_subtopic_page` (generate_site_v5.py:3816), redesign branch at :4115 keyed on `BONDING_REDESIGN` (bonding_redesign.py).
- 50 bonding HTML files per tree (12 pages × triple×2 tiers, 11 × combined×2 — nanoparticles Triple-only — + 4 topic pages), mirrored into `mrbadmus_site/`.
- Old matching engine: `make_matching_widget` (:2963) + inline `matching_js` (:4023) — HTML5 DnD, to be retired from bonding output.
- Quiz: `.rd` pages use `make_pilot_quiz` (:3057) + `PILOT_QUIZ_JS` (:3110) inline — to extract to shared/quiz.js.
- Linear MCP may be unauthenticated in this session — if comments fail, draft them in the packet instead and log here.
