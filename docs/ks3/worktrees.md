# KS3 worktrees — how two content lanes build at once

**Status:** law, from MRB-271 (20 Aug 2026). Read this before starting a KS3
content build in any worktree.

This document exists because two content builds running at the same time used
to be impossible in practice, and the reason was structural rather than
procedural: every new instrument registered itself inside `build_ks3.py`, so
two lanes authoring two units edited the same dict in the same file, every
time. Creating worktrees without fixing that would have bought nothing —
it would have converted "two lanes cannot work at once" into "two lanes work
at once and one of them loses a renderer at merge".

Phase 1 of MRB-271 fixed the cause. This document is the operating rule that
goes with it.

---

## 1. The lanes, and who owns which units

| Worktree | Branch | Owns |
|---|---|---|
| `mrbadmus-worktrees/content-chem` | `feat/content-chem` | Chemistry — **C1–C10** |
| `mrbadmus-worktrees/content-phys` | `feat/content-phys` | Physics — **P1–P12** |
| `mrbadmus-site` (the main checkout) | `main` | schools layer, the engine, everything not a KS3 content unit |
| `mrbadmus-worktrees/3d-studio` | `feat/3d-studio` | 3D Studio. Unchanged by this work. |

Biology (B1–B11) is complete and is nobody's active lane. A fix to a shipped
Biology unit is engine work and belongs on `main`.

### One unit has exactly one owner

**Two lanes must never author or edit the same lesson.** Worktrees do not
prevent this — they make it easier, because each lane stops seeing the other's
files.

This has already gone wrong once, on C1, and it cost real work. The units table
above is the whole rule: if you want to touch a unit your lane does not own,
that is a conversation, not a decision you make inside your worktree.

---

## 2. What is still shared after the split

The split moved 20,242 lines — 322 symbols, every unit's drawers, instruments
and registrations — out of `build_ks3.py` into `ks3_art/<unit>.py`. Adding a
unit now means **adding one new file**, because `ks3_art` discovers its modules
rather than listing them. There is no manifest to edit and so nothing to
collide on.

These files are still genuinely shared. A session that needs to change one must
**say so before starting**, so the other lane can hold off or rebase:

| File | What it is | Collision shape |
|---|---|---|
| `build_ks3.py` | the engine: page shells, block dispatch, validation, build | in-place edits, mid-file. Conflicts badly. |
| `ks3_art/kit.py` | primitives used by more than one unit | in-place. Conflicts badly. |
| `ks3_art/core.py` | registrations for kinds more than one unit authors | small; append-shaped |
| `shared/ks3.js` | all lesson interaction | see §3 |
| `shared/ks3.css` | all lesson styling | append-at-EOF; conflicts, but cleanly |
| `ks3_parity.py` | the parity gate | append-shaped, several anchors |
| `verify_ks3.py` | the build gates | append-shaped |

`ks3_art/<unit>.py` is **not** on this list, and that is the point of MRB-271.

---

## 3. `shared/ks3.js` and `shared/ks3.css` — not split, and why

Both still carry per-unit content, and both were examined in MRB-271 phase 1.

**`shared/ks3.css` is already separable and does not need to be split.** Each
unit's block is contiguous, delimited by `/* ═══ BEGIN B10 ═══ */` … `/* ═══ END
B10 ═══ */`, and appended at end of file. Two lanes appending at EOF do
conflict, but it is the one conflict shape that is safe to resolve
mechanically: take both hunks, in order, and nothing interleaves.

**`shared/ks3.js` was NOT split, deliberately.** Per-unit wiring genuinely does
live there, in two forms:

* the `wire<Instrument>` function bodies — mostly contiguous per unit, and
  cuttable;
* the dispatch lines *inside* `wireInstruments()` — `each(root.querySelectorAll(
  "[data-clblock]"), wireChainLedger)` — which is the real collision point,
  because every unit adds its lines to the same function.

Cutting the file into per-unit fragments would move the function bodies and
leave the dispatch lines exactly where they are, so it would not fix the thing
that actually collides. Fixing that properly means replacing the dispatch with
a registration call, which **changes the shipped `ks3.js` bytes**, which moves
its cache-bust stamp, which changes every KS3 page. That is a legitimate change
but it is a different unit of work with a different gate, and it could not be
done under phase 1's byte-identical gate. It is not done. Until it is:

> **Both lanes must not change `shared/ks3.js` in the same week.**

---

## 4. One session per worktree, at a time

One session works one worktree. Two sessions in one worktree share a working
tree, an output tree and a git index, and they will overwrite each other.

**`/design-sync` counts as a session.** So does a scheduled or background run.

### Never share an output tree

Every worktree builds into its own `mrbadmus_site/`. Do not point a build at
another tree's output, and do not run two builds against one output tree: six
concurrent passes over a single output tree produced transient failures and one
false report, and a gate that fails at random teaches people to ignore gates.

Since MRB-271 the generators anchor to their own directory
(`os.chdir(os.path.dirname(os.path.abspath(__file__)))` in each `__main__`), so
`python3 /elsewhere/build_ks3.py` builds *elsewhere's* tree rather than
half-building yours. Before that fix, every path in the generators was
CWD-relative, and `generate_site_v5.build_site()` opens by deleting most of what
it finds in `mrbadmus_site/` — so a build invoked across trees could delete
another worktree's output. Do not undo the anchoring.

### One thing genuinely is shared between worktrees

Headless-gate scratch space: `$KS3_GATE_TMP`, defaulting to `~/tmp/ks3-gates`.
It is outside every worktree, so all lanes use the same directory. It is safe —
Chrome profiles are stamped with their creating PID and the sweep skips live
ones — but if you want belt and braces while two lanes run gates at once, set
`KS3_GATE_TMP` to a per-worktree path.

---

## 5. Build and gate, inside a worktree

```bash
cd ~/Documents/GitHub/mrbadmus-worktrees/content-chem

python3 build_all.py          # KS4, then KS3, then student previews
python3 verify_ks3.py         # the build gates + the parity layers
./check_ks3_live.sh C3        # AFTER the push, once Cloudflare reports done
```

All three anchor to their own directory, so they act on the worktree you are
standing in whatever path you invoke them by.

`build_all.py`'s order — KS4, then KS3, then student previews — is load-bearing
and holds identically inside a worktree. `generate_site_v5.build_site()` wipes
`mrbadmus_site/` except the trees named in its `FOREIGN_OUTPUT_DIRS`
(`ks3`, `3d`), so anything else emitted before it is deleted by it.

---

## 6. How a lane merges back

1. Code commits and pushes its **own branch** — standing authority, see the
   Autonomy Contract in `CLAUDE.md`. One unit is one commit and one push.
2. Code runs the unit's gates first. **A red gate means no commit and no push.**
3. Mide merges, on github.com or in GitHub Desktop.

> **Never hand Mide git plumbing, and never ask him to run `git push` in
> Terminal.** GitHub Desktop and github.com only. If a merge needs a rebase, a
> conflict resolution or a force-push, that is Code's work on Code's branch
> before Mide ever sees it — a force-push remains a stop-and-ask.

Before merging, re-check `main`: another session has merged to `main` mid-run
before (12 Aug 2026), so check immediately before merging, not just at recon.

---

## 7. Adding a new unit — the whole procedure

1. `ks3_data/<unit>/` — the lesson records.
2. `ks3_art/<unit>.py` — **one new file**, no other module touched. Declare any
   of `ART`, `KIND_SHELL`, `KIND_FN`, `KIND_HEAD_START`, `KIND_HEAD_TOTAL`,
   `KIND_HEAD_FROM`. See `ks3_art/__init__.py` for what each is.
3. `shared/ks3.css` — append the unit's block between `BEGIN`/`END` markers.
4. `shared/ks3.js` — the wiring. Shared; announce it (§3).
5. `ks3_parity.py` — the unit's parity rows.

Steps 1 and 2 are yours alone. Steps 3–5 touch shared files.

The registry will refuse to build if you get the registration wrong. It fails
on a duplicate family name across two modules, on a family registered but never
placed, and on a placement whose family nothing registers — the three ways a
component ends up on a page that no gate is watching.
