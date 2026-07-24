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

---

# Phase 1.6 run — visible-motion refactor (MRB-134 Fix 1 + Fix 6 remainder)

**Run start:** 24 July 2026 · branch `content/bonding`

## Guards (this run)

- **HEAD at run start:** `54fd89804300476eea992acd83633fafc6363145` ("covalent bonding pages redesign").
  **Part 0 resolution:** the Phase 1.5 changeset that the previous session *proposed* was
  **already committed by Mide himself via GitHub Desktop** as `54fd89804` (author `mrbadmus`,
  2026-07-24 05:31). It contains the proposed 109 files (12 source + 46 root HTML + 46 mirror
  HTML + 5 mirror shared JS) **plus** `docs/redesign/gate0_packet_bonding_v2.rtf` — Mide chose
  to track the .rtf where the proposal said leave it untracked. Working tree was clean at run
  start; there was nothing to commit, so no duplicate commit was created. This IS the guard
  scenario ("if HEAD moves, first hypothesis is Mide committed via GitHub Desktop"). If HEAD
  moves again mid-run: STOP, same hypothesis.
- **Chemistry freeze baseline (SHA256, current committed state — the 4 files are NOT touched this run):**
  - `b44669d4…c824fdf9  all_subtopics_chemistry.py`
  - `4d13b977…a0a42b61e  all_subtopics_chemistry_higher.py`
  - `a3614f4e…f7645b534  all_subtopics_chemistry_triple_foundation.py`
  - `edf241e7…006b83f0  all_subtopics_chemistry_triple_higher.py`
- **No commits.** One consolidated stop at the end with a single proposed commit grouping.

## Phase 1.6 status — COMPLETE 24 July 2026 (NOT committed; HEAD still 54fd89804)

| Item | Status |
|---|---|
| Part 0 — verify Phase 1.5 landed, record guard, baseline | ✅ done |
| Shared keyed-reconcile helper (`shared/heroes/keyed-render.js`) | ✅ done |
| dot-cross-stepper: keyed render + electron travel (headline) + covalent shared-pair | ✅ done |
| two-state-compare: keyed render + property-value animation + metallic layer slide | ✅ done |
| state-toggle-lab: keyed render + particle interpolation (solid→molten→dissolved) | ✅ done |
| Fix 6 remainder: explicit Reveal-comparison button + animated props + VIEWING stays | ✅ done |
| Reduced-motion: instant end-state everywhere (verified `--force-prefers-reduced-motion`) | ✅ done |
| Verify: driver node-identity + transition assertions, screenshots, determinism, freeze, keyboard, audit | ✅ done |

## What animates now, and how it was proven (headless-Chrome iframe drivers)

The frame swap is gone: every render reuses the SAME DOM nodes (keyed by a
stable id) and updates their position/size/value, so the CSS transitions
already declared on atoms/electrons/ions finally fire.

- **dot-cross transfer** (ionic-bonding): the transferring electron `etr-0`
  is the SAME node before/after the transfer step (node identity preserved),
  `transitionrun(left)` fires, it travels 215px→407px. Mid-transfer screenshot
  shows the • dot floating halfway between Na and Cl.
- **dot-cross share** (covalent-bonding): `pair-dot` identity preserved,
  travels 209→313 with smooth computed-left interpolation; the two atoms slide
  together (ring-L/ring-R/label-L transitionrun).
- **electronSea** (metallic-bonding): electron `electronSea:e-0` identity
  preserved, `transitionrun(top)`, travels 16→54 (free→pinned).
- **metalLayers** (metals-alloys): ion identity preserved, 24 `transitionrun`
  events, computed-left interpolates 26→43 (layers shear/slide under force).
- **crossfade + property values** (giant-covalent): structures crossfade
  (opacity) between diamond↔graphite; property row identity preserved, value
  animates "4"→"3"; VIEWING indicator + verdict + lock/unlock correct.
- **state-toggle** (ionic-compounds): 70 ion `transitionrun` events, ions
  interpolate between arrangements (solid→molten→dissolved reads as motion).

**Testing gotcha (recorded for next time):** under `--virtual-time-budget`,
`transitionrun` events fire NON-deterministically if you observe with a long
`setTimeout` (the compositor doesn't tick during fast-forward). Observe with a
`requestAnimationFrame` sampling loop instead — it forces frames, so both the
events AND `getComputedStyle(el).left` interpolation are reliable. Reduced-motion
drivers must NOT use an rAF loop (no frames scheduled when nothing animates → it
stalls); use `getComputedStyle(el).transitionDuration` (a single read) instead.

## Verification battery (all green)

- Node identity + transition: all 6 engine modes (above).
- Reduced motion: `--force-prefers-reduced-motion` → keyed nodes report
  `transition-duration: 0s`, `transition-property: none` on all 3 engines
  (media-query `!important` kill beats the inline transition); end position
  still set → instant end-state. dot-cross reduced-motion screenshot shows the
  electron already docked in Cl's shell (no mid-flight).
- Screenshots (scratchpad): `shot_dotcross_mid.png`, `shot_dotcross_reducedmotion_end.png`,
  `shot390_{ionic,giantcov,ioniccompounds}.png` — no page-body horizontal overflow.
- Determinism: 2 runs → 998 mrbadmus_site HTML byte-identical.
- Freeze: 4 chemistry data files byte-identical to baseline (`git diff HEAD` empty).
- Containment: 48 bonding HTML changed (script tag only), ZERO non-bonding HTML.
- Keyboard: all hero controls native `<button>`; keyed viz nodes (36/12/35) not
  in tab order; Reveal button focusable + keyboard-operable.
- Smoke: 0 JS errors across 7 loads incl. `tri` layout (MgCl₂) + Combined variant.
- Audit (`audit_content.py`): bonding 0 critical / 0 major (319 minor = frozen
  MCQ length-parity = MRB-122). Unchanged — no content data touched.

## Change containment (proposed single commit — NOT committed)

New: `shared/heroes/keyed-render.js` (+ mirror). Modified: `dot-cross-stepper.js`,
`two-state-compare.js`, `state-toggle-lab.js` (+ mirrors), `generate_site_v5.py`
(loads keyed-render.js before the 3 engines), `docs/redesign/v2_progress.md`.
Generated: 48 bonding HTML (24 root + 24 mirror = 6 engine pages × 4 variants)
gain the one `<script src="/shared/heroes/keyed-render.js">` tag. = 58 entries.

## Blocked / skipped log

- (none) — all three engines shipped; nothing narrowed or deferred.

## Notes for resume

- Bonding pages render via `make_pathway_subtopic_page` (generate_site_v5.py:3816), redesign branch at :4115 keyed on `BONDING_REDESIGN` (bonding_redesign.py).
- 50 bonding HTML files per tree (12 pages × triple×2 tiers, 11 × combined×2 — nanoparticles Triple-only — + 4 topic pages), mirrored into `mrbadmus_site/`.
- Old matching engine: `make_matching_widget` (:2963) + inline `matching_js` (:4023) — HTML5 DnD, to be retired from bonding output.
- Quiz: `.rd` pages use `make_pilot_quiz` (:3057) + `PILOT_QUIZ_JS` (:3110) inline — to extract to shared/quiz.js.
- Linear MCP may be unauthenticated in this session — if comments fail, draft them in the packet instead and log here.
