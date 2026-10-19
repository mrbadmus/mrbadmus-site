# Loose ends run — 17–19 Oct 2026

Seven small fixes left over from the KS4 port, front door and Catch-up reports.
Opus led and audited; Sonnet built. Each fix was its own build, gate round and
push. No GATE-OVERRIDE on any push. No production writes.

## What shipped

| # | Fix | Commit on main | What a pupil sees |
|---|---|---|---|
| 1 | Opener shuffle | `7a68c3c34` | The two "If you had to guess" options swap order at random on each visit, KS4 and KS3 |
| 2 | Giveaway reasons stripped | `e76786948` | Practice options show "0.5 g", not "0.5 g — confusing moles with grams"; the reason moves to the feedback |
| 3 | Arctic fox | — | No change (ruled correct) |
| 4 | Back-link | `4f0ea00ba` | Reactivity series → "Oxidation and reduction" in Connects to |
| 5 | 3D Studio check | `b2af6f849` | Nothing visible; `3d_parity` green for the first time since August |
| 6 | Head-of-department rollup | branch `feat/hod-rollup-visibility-migration` | Nothing yet — parked SQL, proven on TEST |
| 7 | KS4 tidy list | `5e430525f` | Figure text ≥11px on phones; off-spec words replaced |

### 1. Opener shuffle
- KS4: ruling R20 in `ks4_rulings.py` patches the compiled `Ks4Guess` block (all
  eight delivered copies are byte-identical, Design's files untouched). KS3:
  `shuffleGuess()` in `shared/ks3.js`, wired from `build_ks3.py`'s `data-shuffle`.
- Order is picked once per page load; the right option's reply always follows it.
- The right option was **not** always first, as the report claimed: about 12 of
  43 Code openers, 102 of 119 Design openers and 84 of 185 KS3 openers had it
  first. Each page still used the same order every visit.
- Gates: `ks4_parity` R18 now compares the two options as an unordered pair. A new
  slow gate, `guess_shuffle_drive`, proves both orders occur and that replies follow
  their option.

### 2. Giveaway reasons
- One display rule in `option_labels.py`: the label is the text before the first
  " — ". Three renderers apply it: KS4 topic pages (`generate_site_v5.py`), the KS3
  ladder (`build_ks3.py`) and KS4 lesson pages (`ks4-lib.js` `item()`, ruling R21).
- **Display-only.** The page still SENDS the full stored option text (a `data-full`
  attribute, or the option's `full` field). That keeps the parent-product answer keys
  matching with no backend or database change. The sent payloads were captured
  before, after (local) and after (live), and are identical.
- 889 questions, 2,301 labels, 726 pages. The full list is in
  `docs/ks4/LOOSE-ENDS-DISTRACTOR-SWEEP.md`.
- 34 questions are left as authored, because the tail is the answer (e.g. "myopia —
  concave lenses" against "myopia — convex lenses").
- New fast gate `option_labels`.

### 4. Back-link
- Ruling `LE17-F4-RS-BACK` adds one Connects entry. Batch 5 was re-frozen; only
  reactivity-series' hash moved.
- **Deviation:** extraction-of-metals was NOT given the link. Its Next card already
  points at oxidation-reduction, so a Connects entry would repeat the same link
  directly underneath (no-redundant-text rule).

### 5. 3D Studio check
- The studio already matched Design; the gate was wrong on all three rows. Watched
  failing first on unmodified main:
  - `--st-ok-room` is Mide's ruled student green (MRB-270), never painted by the
    studio. Now in `ADOPTED`.
  - Two `1.5px` borders read as `1px`. Chrome 155 floors used border widths to whole
    CSS px at any device scale, so measuring at DPR 2 doesn't help. Rows with a
    fractional expectation now read the authored width from the stylesheet and
    compare it exactly. A mutation test (setting it to 1px) fails as it should.
- `studio_build.py`: `3d_parity` and `3d_render_check` build the studio themselves
  instead of skipping, and fail if Node or the build fails.
- `3d_isolation` keeps its `needs=3d-studio/dist` skip. It is a fast gate that runs
  `build_all`, so making it unskippable added 20–35 minutes to every worktree push.

### 6. Head-of-department rollup
- **Cause:** `teacher_class_rollup_v2` (SECURITY DEFINER) read every
  `flashcard_sessions` row, but `flashcard_sessions_select` hides them from a head of
  department.
- **Fix:** the `flashcard_activity` step now carries the same visibility test as the
  RLS policy. The catch-up line `recipient_ids IS NULL` is kept.
- **TEST:** before, 1329 values compared with 1 mismatch (HOD view of one pupil's
  "last active"). After, 1329 compared with 0 mismatches across all three readers.
  Triangulated as head of department, class teacher and pupil: each sees exactly what
  RLS lets them read.
- Old prosrc md5 `2d776cb1…` (TEST = production); new `250f89ed…`.
- **For the platform chat:** apply sheet `supabase/HOD-ROLLUP-APPLY.md` on the branch,
  with a pre-check, post-checks and rollback.

### 7. KS4 tidy list
- **Words:** 18 rulings `LE17-F7-*` (batches 7, 8, 10). ATP → energy; catabolic →
  breaking down; base pairs → genome wording except on Triple Higher; beta and alpha
  cells → the pancreas; autoimmune → spec wording; keystone, niche and aposematism
  glosses removed.
  - Eight option changes are display-only (R22), so the sent answer key is unchanged.
    A key refresh is parked for the platform chat.
  - Kept as examiner-OK or not on the list: latent heat, "about 90%", DNA bases,
    anabolism, parasites.
  - Batches 7, 8 and 10 re-frozen; only the edited lessons moved.
- **Figure text:** before, 702 of 903 figures had text under 11px at 390px (worst
  5.3px). After, 0.
  - **How:** on phones only, a figure whose smallest label would fall under 11px gets
    a min-width that brings it to 11px, and scrolls sideways in its frame with a fade
    at the edge. Nothing moves, so labels stay beside their lines. Desktop is
    unchanged.
  - New slow gate `ks4_figure_text`. `ks4_parity` R23 lets a section grow only by its
    own scrolling figures' extra height.
- **Menstrual-cycle graph:** it already labelled its lines directly; the labels were
  5–7.5px. They are now 11px, and the graph scrolls about one screen.

## Parked

- **Production SQL for fix 6:** branch `feat/hod-rollup-visibility-migration` and
  `supabase/HOD-ROLLUP-APPLY.md`, for the platform chat.
- **Answer-key refresh for the 8 display-only option texts (fix 7):** for the
  platform chat, if the keys should carry the new wording. Until then pages show the
  new wording and send the old.
- **36 figures needing more than two columns of phone scroll:** the worst are
  strong-weak-acids, stellar-evolution and structure-of-atom. They want a phone
  redraw; listed in `docs/ks4/LOOSE-ENDS-FIGURES.md`.
- **26 colon-tail questions** (`'100 mol: 2.7 kg = …'`): the same giveaway, but
  outside the " — " rule. Listed in §8 of the sweep doc.
- **290 unscored KS3 activity options:** not changed by ruling; §7 of the sweep doc.
- **Default backend checkout:** `../mrbadmus---backend` is 131 commits behind and
  can't fetch over HTTPS. Every push used a fresh SSH worktree instead.
