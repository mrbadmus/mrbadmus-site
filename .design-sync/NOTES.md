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
- **`[OUT_UNSAFE]` on a re-sync is usually a half-cleaned `ds-bundle/`.**
  The guard refuses a non-empty `--out` carrying neither `_ds_bundle.js`
  nor a `.ds-bundle` marker — an emptied-but-present `_screenshots/` dir
  is exactly that state. `rm -rf ds-bundle` and re-run: it is gitignored,
  fully regenerated, and holds nothing durable (authored previews live in
  `.design-sync/previews/`).
- Sync-time verification also caught a real app defect (libcard name/meta
  inline stacking) — fixed in `studio.css`, committed on `feat/3d-studio`.

## Re-sync risks

- The self-symlink above is machine state, not in git — first thing to check
  when a re-sync fails immediately.
- `tokens/` uploads are verbatim copies of `shared/tokens.css` +
  `shared/ks3.css` taken at sync time. **Re-sync after any tokens.css change
  on main** (KS4 restamps, KS3 dial changes) or Claude Design drifts from the
  live site.
- Specimen fixtures are inlined in `previews/InfoPanel.tsx`,
  `PhoneSheet.tsx`, `RetrievalPanel.tsx` and mirror the Stage 0 content
  schema — update them if the schema changes shape.
- Ten components have authored previews; the other six are unauthored. Of
  those six, only **three actually show the typographic floor card (Stage,
  TabletPanel, ToolIcon)** — LibraryDrawer, LibraryFullScreen and ModeToggle
  render real content from their `.d.ts` crash-prevention props, so the
  contact sheet marks them ✓, not `floor card`. All six remain the standing
  offer for incremental authoring on any later re-sync. Stage can be composed
  via `createPlaceholderRenderer` (merged onto the global via `extraEntries`).
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
  `README.md` still carried the pre-reconciliation ones (`--st-ink` #1A140E,
  `--st-accent-text` #A63A18) — a values-only hand-correction had reached one
  and not the other. `DesignSync(get_file)` on the specific path is the only
  reliable check. Both were repaired by the 11 Aug re-sync.
- **A grade cleared with "contract changed" is not automatically churn.**
  BrandMark and HotspotDot cleared on the 11 Aug re-sync with byte-identical
  emitted artifacts, which looks like nondeterminism but was real: the
  uploaded anchor predated commits `c158d481f` (component sources) and
  `56b49c876` (their authored previews), both 10 Aug 16:31, because the last
  upload ran earlier than the local file timestamps suggested. Check
  `git log` on the component source and `previews/<Name>.tsx` before
  suspecting the pipeline.
