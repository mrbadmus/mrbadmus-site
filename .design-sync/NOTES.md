# design-sync notes — MrBadmusAI (repo-specific gotchas)

- **Package anchor is a self-symlink.** The DS "package" is the 3D Studio app
  (`3d-studio/`, no library dist). Before any converter run:
  `ln -sfn .. 3d-studio/node_modules/mrbadmus-3d-studio`. `npm ci` (and any
  fresh clone) wipes it — recreate it first or the build dies reading
  `node_modules/mrbadmus-3d-studio/package.json`.
- **Config paths resolve through that symlink, lexically.** Package-relative
  `../` means "up from `3d-studio/node_modules/mrbadmus-3d-studio`", so
  repo-root files need `../../../` (see `tokensGlob`, `extraFonts`).
- **`css.mjs` fork** (`.design-sync/overrides/css.mjs`, declared in
  `libOverrides`): stock `copyTokens` walks one package-rooted glob; this
  repo's token files live at site root (`shared/tokens.css`, `shared/ks3.css`),
  so the fork accepts an array of package-relative paths, copied under
  sanitized names (`shared-tokens.css` etc.) to avoid basename collisions.
- **Fonts.** `.design-sync/ds-fonts.css` is the converter-facing @font-face
  manifest (relative urls it can resolve/copy). The app ships its own font
  URLs via `3d-studio/src/styles/fonts.css` — split out of the app's
  `tokens.css` during this sync so tokensGlob stays esbuild-clean. Keep the
  two in step if families change.
- **`runtimeFontPrefixes: Space Grotesk, IBM Plex`** — the KS4-legacy
  families arrive via a Google Fonts link in `generate_site_v5.py` on the
  live site and are deliberately not shipped; conventions.md tells the agent
  not to build new surfaces with them. Raised to Mide in the sync report.
- **`srcDir: src/components`** keeps `main.tsx` out of the synth entry — it
  mounts the app on import and drags app-serving CSS URLs into esbuild.
- **Preview content convention:** anatomy-shaped strings in previews use the
  frozen reference's lorem placeholder style — no invented science; real
  strings pass Mide's Stage 8 gate. UI copy is real.
- **Known render warns:** none outstanding. BrandMark's `[RENDER_THIN]`
  cleared once its preview was authored; InfoPanel's `[GRID_OVERFLOW]`
  cleared 11 Aug via `overrides.InfoPanel.cardMode: "column"` — it is a
  full-width panel and the product's grid cell was cropping both exports.
  RetrievalPanel, Stage and TabletPanel took the same `cardMode: "column"`
  remedy on 13 Aug for the same reason.
- **A media-gated component needs a `viewport` override, or its card is shot
  in the wrong layout.** `package-capture.mjs` renders each cell at the card's
  declared viewport (default **900×700**); `package-validate.mjs`'s render
  check uses a wider one. So the two can disagree, and when they do the
  **review sheet is the one telling the truth about the product card**. Stage
  is the worked example: `studio.css` has `@media (max-width: 1023px) { .stage
  { flex: none; height: 520px } }`, so at 900px the stage collapsed to **2px
  wide** and every review cell photographed as an empty dark box while the
  render check showed a perfect stage. Fix is `overrides.Stage.viewport:
  "1240x520"` — the same reason TopBar already carries `1240x480`. Before
  concluding "the capture is flaky", measure the layout chain at 900px:
  a `.stage` computing `flex: 0 0 auto` is the tell that a desktop rule did
  not apply. (Ruled out along the way, so don't re-chase: capture's frozen
  clock (`clock.setFixedTime`) and post-paint effect timing are NOT causes.)
- **`viewport` changes need a full `package-build.mjs`.** The targeted
  `preview-rebuild.mjs` refuses with `[CONFIG_STALE]` because a viewport
  change re-stamps grade keys; `cardMode` alone it accepts. Symptom of
  ignoring it: the card head still reads the old `viewport="…"` and the
  capture you just ran graded a stale card.
- **Grades do NOT track the component source — only the authored preview and
  preview-affecting config.** This is by design (§4.3) and it has bitten once:
  MRB-191 rewrote `RetrievalPanel`'s props (`targetIndex` → `round`/`revealed`/
  handlers) and the anchor still classified it `unchanged`, so nothing would
  have re-graded it. What caught it was the **render check** (`[RENDER] root
  empty`, `Cannot read properties of undefined (reading 'queue')`). On any
  re-sync that follows app-source work, treat the render check — not the
  verification partition — as the gate, and re-read every authored preview
  whose component changed shape.
- **`.d.ts` contracts are synth-mode weak.** The DS is an app, not a library,
  so there is no built `dist/` with types: the converter synthesizes the entry
  from `src/` and most components emit `<Name>Props { [key: string]: unknown }`
  — no API contract for the design agent. `cfg.dtsPropsFor` is the documented
  fix and now carries hand-written bodies for the five that had neither a
  contract nor a usage example (ModeToggle, ToolIcon, LibraryDrawer,
  LibraryFullScreen, TabletPanel). **The other twelve still emit empty props**
  and lean on the examples in their `.prompt.md`, which come from the authored
  previews. Filling those in is the next obvious win; write them as inline
  structural types (imports don't resolve in the emitted `.d.ts`).
- **`[OUT_UNSAFE]` on a re-sync is usually a half-cleaned `ds-bundle/`.**
  The guard refuses a non-empty `--out` carrying neither `_ds_bundle.js`
  nor a `.ds-bundle` marker — an emptied-but-present `_screenshots/` dir
  is exactly that state. `rm -rf ds-bundle` and re-run: it is gitignored,
  fully regenerated, and holds nothing durable (authored previews live in
  `.design-sync/previews/`).
- Sync-time verification also caught a real app defect (libcard name/meta
  inline stacking) — fixed in `studio.css`, committed on `feat/3d-studio`.

## Re-sync risks

- **Two symlinks are machine state, not in git — recreate BOTH before any
  re-sync.** Both were absent on 13 Aug (this worktree had been re-created
  since the last sync), and neither failure is self-describing:
  `ln -sfn .. 3d-studio/node_modules/mrbadmus-3d-studio` (the package anchor)
  and `ln -sfn ../.ds-sync/node_modules .design-sync/node_modules` (so the
  committed `overrides/css.mjs` fork can resolve its bare `esbuild` import).
  First thing to check when a re-sync fails immediately.
- `tokens/` uploads are verbatim copies of `shared/tokens.css` +
  `shared/ks3.css` taken at sync time. **Re-sync after any tokens.css change
  on main** (KS4 restamps, KS3 dial changes) or Claude Design drifts from the
  live site.
- Specimen fixtures are inlined in `previews/InfoPanel.tsx`,
  `PhoneSheet.tsx`, `RetrievalPanel.tsx`, `Stage.tsx`, `TabletPanel.tsx` and
  `RecordSection.tsx` and mirror the Stage 0 content schema — update them if
  the schema changes shape. `RetrievalPanel.tsx` additionally inlines a
  `RoundState` shaped as `startRound` builds one (queue/index/results/missed/
  complete), so it moves with `studio/retrieval.ts` too.
- **Every component now has an authored preview — no floor cards remain**
  (14 preview files for 17 components; `Library.tsx`, `Quality.tsx` and
  `icons.tsx` each cover more than one export). Stage is composed via
  `createPlaceholderRenderer('viewport' | 'paper')`, which reaches the bundle
  through `extraEntries` and gives the card a real renderer to mount — one
  instance per cell, because a shared one is unmounted by whichever cell
  renders last.
- **Playwright browsers live at `~/Library/Caches/ms-playwright` on macOS** —
  NOT `~/.cache/ms-playwright`, which is the Linux path this file used to
  give. Checking only the Linux path reports "nothing cached" and invites a
  needless ~200MB reinstall. Present 11 Aug: `chromium-1234`,
  `chromium_headless_shell-1234`. No `PLAYWRIGHT_BROWSERS_PATH` is set and
  there is no `chromium`/`google-chrome` on PATH (only Google Chrome.app),
  so that cache is the only thing making the render check run.
- Build assumed node v24 / npm 11; converter deps live in `.ds-sync/`
  (gitignored) — re-run the staging `cp -r` + `npm i` on fresh clones.
- **The uploaded project can sit in a mixed state matching no single commit,
  so verify per-file rather than inferring the whole project from one
  artefact.** Found 11 Aug: the token file carried the reconciled hexes while
  `README.md` still carried the pre-reconciliation values of `--st-ink` and
  `--st-accent-text` — a values-only hand-correction had reached one and not
  the other. `DesignSync(get_file)` on the specific path is the only reliable
  check. Both were repaired by the 11 Aug re-sync. (The superseded hexes are
  deliberately not quoted here: the parity gate's layer A bans them from
  `.design-sync/` outright, and a rule with a "but not in prose" exception is
  a rule that unravels. The old values live in `reference/design-notes.md`,
  which is where the divergence record belongs.)
- **A grade cleared with "contract changed" is not automatically churn.**
  BrandMark and HotspotDot cleared on the 11 Aug re-sync with byte-identical
  emitted artifacts, which looks like nondeterminism but was real: the
  uploaded anchor predated commits `c158d481f` (component sources) and
  `56b49c876` (their authored previews), both 10 Aug 16:31, because the last
  upload ran earlier than the local file timestamps suggested. Check
  `git log` on the component source and `previews/<Name>.tsx` before
  suspecting the pipeline.
