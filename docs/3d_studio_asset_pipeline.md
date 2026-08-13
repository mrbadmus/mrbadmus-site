# 3D Studio — turning a downloaded model into a studio specimen

This is the route from "I found a heart model online" to "the studio is showing
it". It is written for you, Mide, not for a developer: every technical word is
defined the first time it appears, and every step is a command you can copy.

There is one command to remember. Everything else on this page is either
context for it or what to do when it says no.

```
python3 3d-studio/tools/prepare_specimen.py ~/Downloads/heart.glb --name heart
```

Run it from the top of the repo folder (the one containing `index.html` and
`3d-studio/`).

---

## Step 1 — download the model in the right format

**Download it as GLB.** This is the single most important choice on the page,
and it takes one click at download time.

GLB is the 3D file format web browsers understand natively. It is one file that
holds everything — the shape, the colours, the surface images — so there is
nothing to lose track of. Its full name is "glTF binary"; you will see `.glb` on
the end of the filename. Some sites write it as "glTF (.glb)" in the menu.

On **Sketchfab**, the download button offers several formats. Pick the glTF one
and take the `.glb`. Most other model sites offer the same.

**Why it matters so much:** the other common formats — `.blend`, `.fbx`, `.obj`
— are not web formats. Converting them needs Blender, a free 3D modelling
program that is *not installed on this Mac*. If you download a `.blend` you have
added a 1 GB install and an untested conversion step to your afternoon. If you
download the `.glb` of the same model, none of that happens. See
[If your file is not a GLB](#if-your-file-is-not-a-glb) at the bottom if you are
already stuck with one.

While you are on the download page, **copy the licence and the page URL into a
note.** You need both in Step 5, and they are much harder to find again later.

---

## Step 2 — put the file somewhere you can point at

Anywhere is fine — `~/Downloads` is fine. The command takes the path to the
file you downloaded; it does not need the file moved first. The tool writes its
own output into the right place inside the project.

Leave the original download where it is and do not delete it. If a step goes
wrong, you want the untouched original to start again from.

---

## Step 3 — run the command

```
python3 3d-studio/tools/prepare_specimen.py ~/Downloads/heart.glb --name heart
```

- **`~/Downloads/heart.glb`** — the file you downloaded.
- **`--name heart`** — the specimen's short id. It decides the output filename
  (`heart.glb`) and should match the `id` in the specimen's content file
  (`3d-studio/content/heart.json`).

By default the finished file is written to
`3d-studio/public/assets/heart.glb`, which is where the studio looks for it.

**Trying one out without committing to it.** Add `--out` and a path somewhere
temporary, and nothing in the project is touched:

```
python3 3d-studio/tools/prepare_specimen.py ~/Downloads/candidate.glb \
  --name heart --out /tmp/candidate-check.glb
```

That is the right form to use while you are still comparing models. Once the
file lands in `3d-studio/public/assets/`, the studio stops using the generated
stand-in shape and starts using your model on the next build — which is what
you want when you have chosen, and not before.

The whole run takes a second or two for a typical model.

---

## Step 4 — read what comes back

The command prints three blocks, in this order.

### BEFORE — what you actually downloaded

```
  BEFORE
    File:       /Users/mide/Downloads/heart.glb
                7,840,208 bytes (7.48 MiB)
    Triangles:  270,400 (gate: under 60,000)
    Textures:   1
                body — 4096×4096 image/png, 233,653 bytes  ⚠️ over the limit
    Parts:      2 mesh-bearing node(s)
                outer-wall  135,200 tris
                inner-part  135,200 tris
```

- **Triangles** — 3D shapes are built from flat triangles. More triangles means
  more detail and a slower load. The studio's limit is 60,000.
- **Textures** — the images painted onto the surface. `4096×4096` means a 4096
  pixel square image, which is four times wider than the studio allows.
- **Parts** — the named pieces the model is built from. **Read this list
  carefully.** It is the single most important thing on the screen, and Step 6
  explains why.

### WORK — what it did about it

```
  WORK
    dedup + weld:      270,400 triangles
    simplify:          ratio 0.203, error 0.001 — 270,400 → 55,000 triangles
    textureCompress:   1 texture(s) over 1024² resized
    draco:             edgebreaker
```

In plain terms: it removed duplicated data, reduced the triangle count until it
fit the budget while changing the shape as little as it could, shrank the
surface images to 1024 pixels square, and compressed the result. Steps it does
not need are skipped and say so — a model already under budget is not
simplified at all.

### AFTER and CHECKS — what you have now

```
  AFTER
    File:       .../3d-studio/public/assets/heart.glb
                7,840,208 bytes (7.48 MiB) → 196,736 bytes (0.19 MiB)  (39.85× smaller)
    Triangles:  270,400 → 55,000
    Parts:      2 — the names Stage 3 isolates on:
                outer-wall  27,500 tris
                inner-part  27,500 tris

  CHECKS
    Part names: ✅ preserved (2 in, 2 out)
    Draco:      ✅ KHR_draco_mesh_compression present in the JSON chunk
    Triangles:  ✅ under 60,000
    File size:  ✅ under 3,145,728 (3 MiB)
```

Then the purchase gates run automatically on the file that was just written,
and print their own verdict.

---

## Step 5 — what a pass looks like

```
Mechanical gates: 5 pass, 0 fail, 0 unverified. Interior geometry: HUMAN CHECK REQUIRED.

────────────────────────────────────────────────────────────────────────────
Summary

  wrote        .../3d-studio/public/assets/heart.glb
  triangles    270,400 → 55,000
  parts        outer-wall, inner-part
  part names   preserved
  gates        every mechanical gate passed
```

Five green ticks and `every mechanical gate passed` means the file is the right
size, the right shape-complexity, properly compressed, its images are within
budget, and it is a closed, solid surface with no holes.

**It does not mean the model is good enough to teach with.** Two things are
still yours to decide, and the tool says so every time:

1. **The cross-section check** (Step 6) — is the inside really modelled?
2. **The science** — is it anatomically right at the fidelity a GCSE student
   needs, and does it match the conventions of an AQA diagram? Nothing
   automated will ever answer that. It is your examiner's eye, and it is the
   last gate.

**Then record where it came from.** Open the specimen's content file —
`3d-studio/content/heart.json` — and fill in three fields inside `assets`:

```json
"licence":  "CC Attribution 4.0",
"source":   "https://sketchfab.com/3d-models/…  by <creator name>",
"acquired": "2026-08-13"
```

This is not admin for its own sake. Those three values are what answers "what
are we hosting, from whom, under what terms?" when a school's business manager
or data protection officer asks — and they flow straight into the generated
provenance manifest (`docs/3d_studio_asset_manifest.md`), which is where that
question gets answered for the whole collection at once. A licence you did not
write down at download time is a licence you will spend an hour hunting for
later, or an asset you have to drop.

If the licence requires credit (most free models do), the creator's name goes in
`source` exactly as they wrote it.

---

## Step 6 — the two checks the computer cannot do for you

### The part names

Look at the `Parts:` list. Those names are what the studio's *isolate* and
*layers* tools work on — the controls that let a student pull one structure out
of the model and look at it alone. The studio never invents a name; it shows the
name inside the file, exactly as the modeller typed it.

So:

- `outer-wall`, `left-ventricle`, `aorta` — good. Real parts, usefully named.
- `Object_1`, `Object_2`, `mesh_0` — the model is in pieces but the pieces are
  not named. Usable, but every label a student sees would have to be authored
  elsewhere and matched up by hand.
- **One part only** — the whole heart is a single lump of geometry. It will load
  and it will look fine, and the isolate and layers tools will have nothing to
  do. The tool prints a note when it sees this. It is a good reason to go back
  and find a different model.

### The cross-section

The validator prints this at the end of every run, and it is not a formality:

> **HONEST LIMIT**: this script can show that surfaces exist inside the outer
> shell; it CANNOT confirm they are anatomically meaningful chambers, valves and
> lumens rather than junk geometry.

A heart that is hollow, or one with a couple of stray flat planes rattling
around inside it, produces the same encouraging signals as a properly modelled
one. The only way to know is to look:

1. Open the finished `.glb` at <https://gltf-viewer.donmccurdy.com> (drag the
   file onto the page — it stays on your machine, nothing is uploaded).
2. Cut through it with a clipping plane — a slider that hides everything in
   front of an invisible flat surface, so you see the model in section, like a
   dissection.
3. Check that the structures a student must be able to name are *modelled* —
   the four chambers, the valves, the openings of the vessels — and not just
   painted onto the inside of a hollow shell.

If the inside is empty, the model is wrong for this studio no matter how good
the outside looks. Cross-section is the whole point of the thing.

---

## What a failure looks like, and what to do

The command stops with a message and a non-zero exit code. Each failure has one
sensible response.

### `❌ Watertight manifold FAIL`

The surface has holes, or faces that meet in ways a solid object's cannot. It
matters because the cross-section tool cuts the model open and caps the cut — a
model with holes produces a cut that looks broken.

- If the **triangle count barely changed** during the run, the holes were in the
  model when you downloaded it. Find a different model; this is not something to
  patch.
- If the model was **simplified hard** (say 250,000 triangles down to 55,000),
  the reduction may have caused it. Look for a lower-detail version of the same
  model — many sites offer one — or a different model. Squeezing harder will not
  help.

### `⚠️ still over budget` / `❌ Triangle count FAIL` / `❌ File size FAIL`

The model is too heavy to bring inside the limits without wrecking it. The
answer is a lighter source, not a harder squeeze: look for a "low poly" or
"game-ready" version, which means the same subject built from far fewer
triangles.

### `❌ PART NAMES DID NOT SURVIVE THE ROUND TRIP`

A bug guard, not something you caused. It means the conversion merged the
model's named pieces together, which would silently break the isolate and layers
tools while leaving a file that looks perfect in a viewer. The tool refuses to
call that a success. Nothing is written that you should use — report it.

### `❌ .fbx files need Blender`

See the next section.

### `❌ file not found` / `❌ .zip is not a 3D model format`

A typo in the path, or the download is still a zip archive. Unzip it first and
point at the `.glb` inside.

---

## If your file is not a GLB

`.blend`, `.fbx`, `.obj`, `.dae`, `.stl` and `.ply` are not web formats.
Converting them into GLB needs **Blender**, the free 3D modelling program, and
**Blender is not installed on this Mac**. When the tool meets one of these
formats and cannot find Blender, it stops and says so rather than half-running
and leaving you with something that looks converted.

Two ways forward. The first is much faster:

**1. Re-download the model as GLB.** Go back to the model's page and take the
glTF/`.glb` download instead. Nothing to install, and the conversion step
disappears. This is almost always the right answer.

**2. Install Blender** — free, about 1 GB, from <https://www.blender.org/download/>.
Drag it to Applications and open it once so macOS clears its security prompt.
The tool then finds it automatically on the next run and converts the file
itself, with no change to the command you type.

> **Be careful with option 2 the first time.** The conversion code is written
> and ready, but it has never actually run, because there was no Blender on this
> machine to run it against. The first time you use it, check the `Parts:` list
> against the model you downloaded before trusting anything else in the report.
> The tool prints this warning itself when it takes that path.
>
> With Blender installed you can also sidestep the code entirely: open the file
> in Blender, then **File ▸ Export ▸ glTF 2.0**, set Format to **glTF Binary
> (.glb)**, and run this tool on the exported file. That is the well-trodden
> path, and it is what to fall back on if the automatic conversion misbehaves.

---

## Reference — what the tool actually does

Two files, one entry point:

| File | Role |
|---|---|
| `3d-studio/tools/prepare_specimen.py` | The command you run. Works out the format, converts non-glTF files if Blender is present, runs the pipeline, then runs the purchase gates on the result. |
| `3d-studio/tools/specimen_pipeline.mjs` | Does the 3D work. Never run directly. |
| `3d-studio/validate_specimen_glb.py` | The purchase gates. The only thing that gets to say pass or fail. |

The pipeline, in order: remove duplicated data → merge identical points →
reduce triangles (only if over 60,000, by an amount calculated from the actual
count) → shrink surface images to 1024 pixels max, keeping their proportions →
compress → write → **re-open the written file and check every part name is still
there**.

It deliberately never merges or flattens the model's parts, because that would
destroy the named pieces the isolate and layers tools depend on while producing
a file that loads and renders perfectly. That is the failure mode worth guarding
against, so it is guarded twice: those operations are not used, and the output is
re-read and checked anyway.

**One verdict, from one place.** The pipeline reports what it did; the validator
decides pass or fail. The pipeline never overrules it and never claims a gate
passed.

### Exit codes, if you are scripting it

| Code | Meaning |
|---|---|
| 0 | written, and every mechanical gate passed |
| 1 | a gate failed |
| 2 | a gate could not be verified, or bad usage / missing file |
| 3 | the format needs Blender and Blender is not installed |
| 4 | Blender ran and the conversion failed |
| 5 | the pipeline failed (part names lost, compression missing, unreadable file) |

### The same command through npm

If you are already inside `3d-studio/`, this is equivalent:

```
npm run prepare-specimen -- ~/Downloads/heart.glb --name heart
```

The bare `--` is npm's way of saying "everything after this belongs to the
script, not to npm".

---

## Known limits, stated plainly

- **The Blender conversion path has never run.** There is no Blender on this
  machine. The code is written to Blender's documented command-line interface
  and reviewed, but reviewed is not tested. Treat its first real run as
  something to check, not to trust.
- **Reducing triangles is lossy.** It changes the shape slightly, by design. On
  a clean, closed model this is safe — a five-fold reduction of the studio's
  test specimen stayed perfectly watertight. On a model that arrives with messy
  geometry, a hard reduction can turn small existing flaws into holes. The
  watertight gate catches it; the fix is a better source model.
- **Surface images are re-encoded.** When any image is over 1024 pixels, all of
  the model's images are re-saved. Photographic (JPEG) images lose a small
  amount of quality in that step. This is invisible in practice at the size the
  studio draws them.
- **Nothing here judges anatomy.** Not the pipeline, not the gates. That is
  yours, and it is the last word.
