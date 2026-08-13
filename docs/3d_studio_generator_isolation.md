# 3D Studio — Generator isolation recon (MRB-185, Stage 0)

> **STATUS: the diff in §5 landed on 13 August 2026 (MRB-194), commit
> `c48328ce5`.** §§1–5 below are the Stage 0 recon, kept as written. What
> actually shipped, and the two places it differs from what was proposed here,
> is §7 at the end. The verification plan in §6 became
> `3d_isolation_check.py`, which runs it.

**Date:** 9 August 2026
**Read:** `generate_site_v5.py` (all 5,439 lines), `build_all.py` (all 66 lines),
plus the output-writing region of `build_ks3.py` (lines 1225–1325). Every claim
below cites the actual line in the code as it stands at commit `5cd9c4330`.

**Headline answer:** a directory placed at `mrbadmus_site/3d/` today would be
**deleted** on the next `generate_site_v5.py` run. The wipe loop removes every
top-level entry of `mrbadmus_site/` that is not named in `FOREIGN_OUTPUT_DIRS`,
and that list is currently `["ks3"]` only.

---

## 1. Every path `generate_site_v5.py` deletes, and how

All deletion happens inside `build_site()` (line 5057 onward). There is no
module-level deletion. Four distinct deletion surfaces exist:

### 1a. The output-tree wipe — entry-by-entry, NOT a single rmtree

Lines 5124–5131:

```python
FOREIGN_OUTPUT_DIRS = ["ks3"]

if os.path.exists(output_dir):
    for _entry in os.listdir(output_dir):
        if _entry in FOREIGN_OUTPUT_DIRS:
            continue
        _p = os.path.join(output_dir, _entry)
        shutil.rmtree(_p) if os.path.isdir(_p) else os.remove(_p)
```

The MRB-88-era `shutil.rmtree(output_dir)` of the whole tree is **gone**. It was
replaced (per the long comment at lines 5099–5123) by this entry-by-entry loop:
each top-level file is `os.remove`d and each top-level directory is
`shutil.rmtree`d, **unless** its name is in `FOREIGN_OUTPUT_DIRS`. Skipped
directories are never moved aside — they stay in place for the whole run.

`mrbadmus_site/3d/` is not in the list → `shutil.rmtree(mrbadmus_site/3d)`.

### 1b. Replace-before-copy deletes inside the output tree

These delete a destination subtree immediately before `copytree`-ing a fresh
copy in. They act only on generator-owned paths:

| Line | Deletes | Rebuilt from |
|---|---|---|
| 5195–5196 | `mrbadmus_site/shared/<subdir>/` (e.g. `shared/fonts/`) | `shared/<subdir>/` |
| 5211–5212 | `mrbadmus_site/teacher/` | `teacher/` |
| 5224–5225 | `mrbadmus_site/student/` | `student/` |

### 1c. The copy-to-repo-root round-trip — a SECOND deletion surface, at repo root

Lines 5413–5426:

```python
for item in os.listdir(output_dir):
    s = os.path.join(output_dir, item)
    d = os.path.join(".", item)
    if item in ['.git', 'generate_site_v5.py', 'generate_site.py',
                'all_subtopics_physics.py', 'all_subtopics_chemistry.py',
                'all_subtopics_biology.py']:
        continue
    if os.path.isdir(s):
        if os.path.exists(d):
            shutil.rmtree(d)          # ← deletes the REPO-ROOT copy
        shutil.copytree(s, d)
    else:
        shutil.copy2(s, d)
```

For every top-level entry of `mrbadmus_site/` (skip list above), the matching
**repo-root** path is `rmtree`d and replaced. Note that `FOREIGN_OUTPUT_DIRS`
does **not** apply here: `ks3/` survives the wipe, so it IS in
`mrbadmus_site/`, so the round-trip rmtree's repo-root `./ks3/` and re-mirrors
it. Consequence for us: whatever ends up in `mrbadmus_site/3d/` would be
mirrored to a repo-root `./3d/` — and a repo-root `./3d/` would be deleted and
recreated every run. (The proposed diff below opts `3d` out of this mirror.)

A safety net at lines 5340–5353 aborts the build if `shared/`, `teacher/` or
`student/` contain source files missing from the output copy — it protects
those three source dirs from round-trip data loss, nothing else.

### 1d. The cache-bust rewriter — in-place HTML mutation, not deletion, but a writer

Lines 5367–5411: every `*.html` under `mrbadmus_site/` is read, has
`?v=<md5[:8]>` stamped onto `/shared/{tokens,styles,nav}.css` links, and is
rewritten if changed. The `os.walk` **prunes `FOREIGN_OUTPUT_DIRS`** at the top
level (lines 5396–5399), so skipped trees are never rewritten. This matters for
us: adding `3d` to the list also keeps this rewriter out of Vite's built HTML,
which is what makes the spec §10 "byte-identical before and after a generator
run" gate provable.

## 2. Every path `generate_site_v5.py` writes to

All inside `build_site()`, in execution order:

1. `mrbadmus_site/` directory skeleton — `combined/`, `triple/`, per
   pathway/tier/subject/topic dirs (lines 5133–5154)
2. `mrbadmus_site/shared/styles.css` and `shared/mrbadmus.v2.js` — templated
   writes (5159–5165)
3. Root hand-written pages copied in: `auth.html`, `reset-password.html`,
   `profile-setup.html`, `teacher-profile.html`, `weekly-challenge.html`,
   `leaderboard.html`, `past-papers.html`, `my-challenges.html`,
   `revision.html` (5170–5177)
4. Everything else in `shared/*` glob-copied (files and whole subdirs, 5185–5203)
5. `mrbadmus_site/teacher/` and `mrbadmus_site/student/` copytrees (5205–5229)
6. `mrbadmus_site/index.html` and `ks4.html` (5235–5243)
7. The full generated KS4 page tree: pathway → tier → subject → topic →
   subtopic pages (5246–5322)
8. Cache-bust in-place rewrites of every non-foreign `.html` (5367–5411)
9. The round-trip: every top-level output entry copied over the repo root
   (5413–5426)

For completeness, `build_ks3.py` (the other generator, run second by
`build_all.py`) writes only: `mrbadmus_site/ks3/` (rmtree + full rebuild of
that one dir, lines 1230–1233), three files into `mrbadmus_site/shared/`
(`ks3.css`, `ks3.js`, `tokens.css`, lines 1302–1308),
`docs/ks3/diagram-manifest.md` (1312–1314), and a mirror to repo-root `ks3/`
(1317–1321). It never touches anything else, so it is not a hazard to
`mrbadmus_site/3d/`.

## 3. Where `FOREIGN_OUTPUT_DIRS` actually lives, and what it protects

**Correction to the Stage 0 prompt:** the prompt describes "the existing
`FOREIGN_OUTPUT_DIRS` skip list in `build_all.py`". That is not where it is.
`build_all.py` contains **no skip list and no protection mechanic at all** — it
is a plain sequential runner (`subprocess.run` of `generate_site_v5.py` then
`build_ks3.py`, stopping on non-zero exit). Its docstring (lines 19–25)
describes the fix but explicitly says the hazard "is now fixed at source".

The skip list is defined and enforced **inside `build_site()` in
`generate_site_v5.py`** (line 5124). It is consulted in exactly two places:

1. the wipe loop (line 5128) — a listed directory is never deleted
2. the cache-bust walker (lines 5396–5399) — a listed directory's HTML is
   never rewritten

It is **not** consulted by the round-trip loop (§1c above), which has its own,
different skip list.

So: the protection is enforced by the generator itself and holds however the
generator is invoked — directly, or via `build_all.py`. Running
`generate_site_v5.py` on its own is exactly as safe (or unsafe) as running
`build_all.py`.

## 4. Would `mrbadmus_site/3d/` survive a full generator run today?

**No.** Evidence (code, not experiment — this run does not execute the
generator per the Stage 0 constraints):

- The wipe loop (lines 5126–5131) iterates `os.listdir("mrbadmus_site")` and
  `rmtree`s every directory entry not in `FOREIGN_OUTPUT_DIRS`.
- `FOREIGN_OUTPUT_DIRS = ["ks3"]` (line 5124). `"3d"` is not in it.
- Therefore `mrbadmus_site/3d/` is deleted in the first seconds of
  `build_site()`, before any page is generated. Nothing recreates it. The run
  exits 0. This is precisely the MRB-88 failure mode that deleted the KS3 tree.

## 5. Proposed mechanic — the diff, NOT applied in this run

Three hunks in `generate_site_v5.py`. Nothing else changes. The generator is
shared with live KS3/KS4 work, so this lands as its own reviewed commit.

**Hunk 1 — protect `mrbadmus_site/3d/` from the wipe and the cache-bust
rewriter** (line 5124):

```diff
-    FOREIGN_OUTPUT_DIRS = ["ks3"]
+    FOREIGN_OUTPUT_DIRS = ["ks3", "3d"]
```

One line buys both protections, because the wipe loop and the cache-bust
walker both consult this list.

**Hunk 2 — the publication copy step** (insert after the `student/` tree block,
i.e. after line 5229, before the landing pages). The `_shutil`/`_os` aliases
are already in scope from line 5169:

```diff
+    # ── 3D Studio built artifact (MRB-185) ──
+    # 3d-studio/ is a Vite app at repo root; its build output
+    # (3d-studio/dist/) is the single source of truth for mrbadmus_site/3d/.
+    # The generator's only job is publication: replace the deploy copy
+    # wholesale from dist when a build exists, and leave the deploy copy
+    # alone when it doesn't — so a machine without a fresh Vite build can
+    # never delete the deployed studio. "3d" is in FOREIGN_OUTPUT_DIRS, so
+    # the wipe and the cache-bust stamping never touch it, and it is opted
+    # out of the repo-root round-trip below. One tree, one writer.
+    _studio_dist = os.path.join("3d-studio", "dist")
+    _studio_dst = f"{output_dir}/3d"
+    if os.path.isdir(_studio_dist):
+        if _os.path.exists(_studio_dst):
+            _shutil.rmtree(_studio_dst)
+        _shutil.copytree(_studio_dist, _studio_dst)
+        print("  ✅ 3d/ (from 3d-studio/dist)")
+    else:
+        print("  ⚠️  3d-studio/dist not found — mrbadmus_site/3d/ left as-is")
```

**Hunk 3 — opt `3d` out of the repo-root round-trip** (line 5417):

```diff
-        if item in ['.git', 'generate_site_v5.py', 'generate_site.py',
+        if item in ['3d', '.git', 'generate_site_v5.py', 'generate_site.py',
                     'all_subtopics_physics.py', 'all_subtopics_chemistry.py',
                     'all_subtopics_biology.py']:
             continue
```

### Why each choice

- **`3d-studio/` at repo root is outside every generator write path** (§2
  above): the generator only writes into `mrbadmus_site/` and, via the
  round-trip, repo-root names that exist inside `mrbadmus_site/`. Nothing
  named `3d-studio` will ever exist inside `mrbadmus_site/`, so the source
  tree can never be touched. This satisfies the spec's sibling-source-dir
  requirement with zero code.
- **Replace-wholesale from `dist/`, guard on `dist/` existing.** "Never cleans
  or writes inside it" holds for the page-generation machinery — the only
  writer of `mrbadmus_site/3d/` is this one publication step, and its source
  of truth is Vite's output. When `dist/` is absent (fresh clone, no Node
  toolchain), the deployed copy is left untouched rather than deleted — the
  exact failure the MRB-88 hazard taught us to design out. When `dist/` is
  present and unchanged, `copytree` reproduces byte-identical content, which
  is the spec §10 generator-isolation gate.
- **No repo-root `./3d/` mirror** (hunk 3). The root mirrors are a historical
  pattern; Cloudflare serves from `mrbadmus_site/` only. A root `./3d/` would
  be a third copy of every multi-MB GLB in git (source in
  `3d-studio/public/assets/`, deploy copy in `mrbadmus_site/3d/`) with no
  reader. `ks3/` keeps its mirror because it already exists and other tooling
  compares against it; `3d` starts life without one.

### Interaction table after the diff

| Generator stage | Effect on `mrbadmus_site/3d/` |
|---|---|
| Wipe loop | skipped (`FOREIGN_OUTPUT_DIRS`) |
| Page generation | never touches it |
| Publication step (new) | replaced from `3d-studio/dist/` iff dist exists; otherwise untouched |
| Safety net | not consulted (checks `shared/teacher/student` only) |
| Cache-bust rewriter | pruned (`FOREIGN_OUTPUT_DIRS`) — Vite HTML never mutated |
| Round-trip | skipped (hunk 3) — no repo-root `./3d/` created or deleted |
| `build_ks3.py` | writes only `ks3/`, `shared/{ks3.css,ks3.js,tokens.css}`, docs manifest — no interaction |

## 6. Verification plan for when the diff lands (separate commit, not this run)

Spec §10's gate, made concrete:

1. Build the Vite app once → `3d-studio/dist/` exists.
2. Run `python3 build_all.py`.
3. `find mrbadmus_site/3d -type f -exec md5 {} +` → save.
4. Run `python3 build_all.py` again with no changes.
5. Same command → hashes must be identical, file-for-file.
6. Delete `3d-studio/dist/`, run again → `mrbadmus_site/3d/` must still be
   byte-identical (the leave-alone branch).

---

## 7. What actually landed (MRB-194, 13 August 2026)

The three hunks in §5 were **re-derived against the current file rather than
applied**, because the generator is shared with live KS3/KS4 work and had moved
since August. It had not moved here: every line number in §§1–3 still pointed at
the same code, and hunks 1 and 3 went in verbatim. Hunk 2 grew.

### Hunk 2 grew a staleness alarm

The publication step as proposed printed one line — `⚠️ 3d-studio/dist not
found` — and that line was the whole of its answer to a build that is not there.
MRB-194's first comment identified why that is not enough, and it is worth
restating because it is a workflow fact rather than a code fact:

> Mide's production workflow is `python3 generate_site_v5.py` in Terminal, then
> GitHub Desktop. No npm step exists anywhere in it.

A guarded publication is safe in the sense that nothing gets deleted. It is not
safe in the sense that matters: the studio ships **stale** every time the site is
regenerated without a Vite build first, and a warning line sitting among ~2,000
green ticks has not been delivered to anyone. So what shipped:

* `dist/` is compared against the newest file in `3d-studio/{src,content,public}`.
  Directory mtimes are ignored — they only move when an entry is added or
  removed, so an edit in place would not register.
* Stale, or absent, prints a `!!!!`-bordered banner rather than a line.
* **The banner is printed twice**: where it happens, and again after the
  "🎉 Done!" block, where it is the last thing on screen when the run finishes.
* Neither is fatal, and no `npm run build` runs from the generator. A Node
  failure must not be able to fail a KS3 or KS4 build. The manual pre-step is
  documented in CLAUDE.md instead, in Mide's actual workflow order — this is
  option **(c) plus (b)** from the ticket, as recommended there.
* Stale still publishes. `dist/` is the source of truth, and republishing what
  is already deployed changes nothing; the alarm is the point, not a refusal.

### Spec §9 was self-contradictory, and this is the corrected reading

§9 says the generator "copies the built artifact into `mrbadmus_site/3d/` **and
never cleans or writes inside it**". Both cannot be true. What is true, and what
is built:

> `mrbadmus_site/3d/` has exactly one writer, the publication step, and that
> writer's only source of truth is `3d-studio/dist/`. No other part of the
> generator reads, writes, cleans, stamps, or mirrors it.

The wipe skips it, the cache-bust walker prunes it, the round-trip skips it, and
the safety net never looks at it. That is the property the acceptance test
measures, and it is stronger than "never writes inside", because it also rules
out the `?v=` stamping that would otherwise have rewritten Vite's `index.html`
on every run and made byte-identity impossible to claim.

### The verification plan became a gate

§6's plan is implemented as `3d_isolation_check.py` at the repo root — six
checks, twelve assertions, including the one §6 did not have: **remove `"3d"`
from `FOREIGN_OUTPUT_DIRS` and watch the tree die.** It does, silently, exit 0,
which is the MRB-88 failure mode reproduced on demand.

Two results worth recording:

* After eight full generator runs and a `build_all.py` run, `git status` showed
  the generator edit and the new `mrbadmus_site/3d/` and **nothing else** — so
  every KS3 and KS4 file in both `mrbadmus_site/` and the repo root was
  byte-identical to `HEAD`. That is the KS3/KS4-unchanged evidence.
* The generator as it stood at `44db1c24a`, the commit immediately before the
  fix, was extracted and run against a populated `mrbadmus_site/3d/`: all 16
  files gone, exit 0, no error. The hazard was real, not theoretical.
