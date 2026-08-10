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
- **Known render warns:** none outstanding (BrandMark's `[RENDER_THIN]`
  cleared once its preview was authored).
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
- Six components ship the deliberate floor card (LibraryDrawer,
  LibraryFullScreen, Stage, TabletPanel, ModeToggle, ToolIcon) — the standing
  offer for incremental authoring on any later re-sync. Stage can now be
  composed via `createPlaceholderRenderer` (merged onto the global via
  `extraEntries`).
- Playwright chromium lives at `~/.cache/ms-playwright`, installed by this
  run via `.ds-sync`'s own playwright — keep the staged-scripts install and
  the browser cache in step (see base skill §4.1 on version pinning).
- Build assumed node v24 / npm 11; converter deps live in `.ds-sync/`
  (gitignored) — re-run the staging `cp -r` + `npm i` on fresh clones.
