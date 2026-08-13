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

**Why it matters so much:** the other common formats — `.blend`, `.fbx`, `.dae`,
`.stl`, `.ply` — are not web formats. Converting them needs Blender, a free 3D
modelling program that is *not installed on this Mac*. If you download a
`.blend` you have added a 1 GB install and an untested conversion step to your
afternoon. If you download the `.glb` of the same model, none of that happens.
See [If your file is not a GLB](#if-your-file-is-not-a-glb) at the bottom if you
are already stuck with one.

**`.obj` is the exception — it is not a problem.** `.obj` (its full name is
Wavefront OBJ) is a plain text file listing corner points and the flat triangles
joining them up — which is all a 3D shape really is, as Step 4 explains. Because
it is plain text, the tool reads it itself, in Python, with nothing to install.
Point
the same command at a `.obj` and it runs. That matters more than it sounds,
because the anatomical sources worth using publish `.obj` and nothing else — and
they publish it in pieces, which is what
[When the model arrives in pieces](#when-the-model-arrives-in-pieces) is about.

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
  size         7,840,208 → 196,736 bytes
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

## When the model arrives in pieces

Everything above assumes one download is one model. The best anatomical sources
do not work that way, and it is worth understanding why before it surprises you.

They do not publish "a heart". They publish a few thousand small meshes — a mesh
being one shape built from triangles — one per anatomical piece, each saved as
its own `.obj` file under a code like `FJ2424`. A heart, in that world, is a
**named selection** of those pieces.

**That is a good thing, not a complication.** It is precisely what the studio
needs. The isolate and layers tools can only offer a student the parts that exist
as separately named pieces inside the file (Step 6). A single downloaded heart is
usually one lump of geometry, or a handful of pieces named `Object_1`; a source
that ships one mesh per structure lets you name every part yourself, in the words
the class will read. You are not working around the format — you are getting the
thing the format makes possible.

The list of which pieces make which structure is written down in an **assembly
recipe**: a small text file that says "the part called *Right atrium* is made of
these source files". The tool reads the recipe, gathers the files, and builds the
specimen from them.

### The command

```
python3 3d-studio/tools/prepare_specimen.py 3d-studio/tools/recipes/heart.recipe.json --obj-dir ~/Downloads/partof_BP3D_4.0_obj_99
```

- **the recipe file** goes where the model file usually goes. The tool recognises
  a `.json` as a recipe rather than a model.
- **`--obj-dir`** is the folder you unzipped the source meshes into. The recipe
  names files, not paths; this says where to find them.
- **no `--name` needed.** The recipe names the specimen itself (`"name":
  "heart"`), so the output lands at `3d-studio/public/assets/heart.glb`.

Everything after that point is identical to Step 3 onwards: same pipeline, same
report, same purchase gates, same two checks that are yours. `--out` works the
same way if you want to try one somewhere temporary.

### What a recipe looks like

`3d-studio/tools/recipes/heart.recipe.json` is the worked example. Stripped to
its bones:

```json
{
  "recipe": "specimen-assembly/v1",
  "name": "heart",
  "transform": { "axes": "LPS-to-glTF", "recentre": "bounds", "scaleTo": 1.0 },
  "parts": [
    { "name": "Right atrium",   "files": ["FJ2424", "FJ2439"] },
    { "name": "Bicuspid valve", "files": ["FJ2420", "FJ2432"] }
  ]
}
```

- **`name`** — the specimen's short id, which decides the output filename and
  should match the `id` in `3d-studio/content/heart.json`.
- **`parts`** — one entry per structure a student can isolate. The `name` is
  shown to the class word for word, so write it the way you would say it.
- **`files`** — the source meshes that make that part. The `.obj` on the end is
  optional; `FJ2424` and `FJ2424.obj` mean the same thing.
- **several files in one part is normal.** The source ships the right atrium's
  wall and its cavity as two meshes; the recipe is where you say they are one
  structure.
- **`transform`** — three pieces of housekeeping, applied to every part together
  so the specimen stays assembled. `axes` re-orients the model from the
  convention medical imaging uses (x towards the patient's left, y towards their
  back, z towards their head) into the one 3D browsers use (y is up), which gives
  the ordinary front-on view — the patient's left on your right, exactly as in a
  textbook plate or a dissection photograph. `recentre: bounds` moves the
  specimen so it sits around the middle of the scene, because the source
  coordinates place the heart about 1.2 metres up a whole body. `scaleTo: 1.0`
  makes its longest edge one unit, so every specimen arrives at a comparable
  size.

The real file also carries a `source` block recording where the meshes came from
(Step 5's job, done once for the whole specimen rather than by hand afterwards),
and long `note` and `sources` entries explaining each choice. Those extra keys
are ignored by the tool and are there for the next person to read.

### Two rules that keep a recipe honest

- **Every file named must exist.** A missing source stops the run. It would
  otherwise produce a specimen with a structure quietly absent from it, and
  nothing further down the line could tell that from a structure the source never
  had.
- **Each source file belongs to exactly one part.** In the real heart source the
  tricuspid leaflets are claimed by *right atrium* and *right ventricle* at once,
  because both descriptions are anatomically true. The recipe assigns each file
  to the single most specific structure that claims it, so no triangle appears
  in the model twice and the watertight gate keeps meaning something.

### The parts and the content file must agree

The part names in the recipe and the hotspots in
`3d-studio/content/heart.json` are two halves of the same thing, and
`3d-studio/validate_content.py` holds them to it. A part called `Right atrium`
binds to the hotspot `heart.right-atrium` — the name lowercased with spaces
turned into hyphens.

- A part **no hotspot claims** is a failure. A student could isolate it and the
  panel would have nothing to say about it.
- A hotspot **with no part** is allowed and listed, not failed, as *anchored by
  coordinate alone*. Some structures genuinely have no mesh of their own — see
  [Where the numbered dots go](#where-the-numbered-dots-go).

> **This path has been run exactly once**, on the heart, and there are no
> automated tests covering it yet. It worked, and the specimen it produced passed
> the gates — but one run is one run. Read the part list in the report against
> the recipe the first few times rather than assuming it.

---

## Where the heart came from

The heart is the first real specimen, so it is worth recording in full — both as
the answer to "what are we hosting?" and as the pattern for the next one.

**Source:** BodyParts3D, published by the **Database Center for Life Science** in
Japan — an anatomical model of the whole human body, broken into one mesh per
named structure. The release used is BP3D 4.0, the "partof" tree, at 99%
reduction (their own pre-simplified set, which is small enough to work with).
Downloaded as `partof_BP3D_4.0_obj_99.zip` from
<https://dbarchive.biosciencedbc.jp/en/bodyparts3d/desc.html>. The recipe records
the archive's `sha256` — a long fingerprint calculated from the file's contents,
so anyone can confirm they have the same bytes we did.

**Licence: CC BY-SA 2.1 Japan.** Two obligations, and both are already recorded:

- **Attribution** — the credit line travels with the model. The exact wording
  is `BodyParts3D, (c) The Database Center for Life Science licensed under CC
  Attribution-Share Alike 2.1 Japan`.
- **Share-alike** — this is the one worth being clear about, because it attaches
  to *our* file, not just theirs. The mesh we derived from their meshes carries
  the same licence onward: anyone we hand `heart.glb` to receives it under CC
  BY-SA too. In practice, for a free revision site, that costs nothing — a school
  may copy it, reuse it and adapt it, and inherits the same terms when it does.
  What it rules out is ever making that mesh proprietary, putting it behind a
  paywall, or licensing it to someone on different terms. It is not ours to close.

**One honest discrepancy, recorded rather than tidied away.** Each downloaded
release-4.0 `.obj` file states CC BY-SA 2.1 Japan in a comment in its own header.
The upstream README at the same URL now states CC BY 4.0 International, which is
the looser of the two. We recorded the files' own statement — the more
restrictive one — so attribution and share-alike are honoured whichever turns out
to be authoritative. The note explaining this lives in the recipe's `source`
block, next to the licence itself.

All of it is written into `3d-studio/content/heart.json` under `assets.licence`,
`assets.source` and `assets.acquired`, exactly as Step 5 describes, and flows
from there into the provenance manifest
(`docs/3d_studio_asset_manifest.md`).

---

## Where the numbered dots go

Every hotspot — the numbered dot a student taps to name a structure — has a
`position3d` in the content file: three numbers giving a point in space on the
model.

**Do not type those by hand.** They are not authored content, they are a fact
about the mesh, and the mesh changes whenever a specimen is rebuilt. Fourteen
numbers guessed by eye against a spinning model are fourteen numbers nobody can
check, and they rot silently the next time the model is regenerated.
`3d-studio/tools/derive_anchors.py` reads the finished model and works each one
out, and it can be re-run whenever the model is rebuilt.

**The rule, in one sentence:** the dot sits on the outside of the specimen at the
point nearest the structure it names — so a structure buried inside, like a
valve, gets its dot on the wall directly over it.

Not the middle of the structure, which is the obvious first guess. The studio
genuinely tests whether a dot is hidden behind geometry before drawing it, so a
dot placed in the middle of a chamber sits under the heart wall from every angle
and never appears. On the outer surface, over its structure, it points at the
right place from outside *and* the structure is what the cross-section exposes
underneath it.

### The two commands

```
python3 3d-studio/tools/derive_anchors.py heart
python3 3d-studio/tools/derive_anchors.py heart --write
```

The first is report-only: it prints what it would do and changes nothing. The
second writes the results into `3d-studio/content/heart.json`.

`--write` touches `position3d` and nothing else. It never edits a label, a
detail sentence, an accepted answer or a spec point — those are yours, under the
science gate.

The report lists each hotspot with its derived coordinate, how far the surface
was from the structure's centre, and that distance as a percentage of the
model's radius. A structure whose nearest way out is a long way off is one to
look at by eye. It also flags mesh parts that no hotspot claims, and hotspots it
could not place.

It needs two Python add-ons, `numpy` and `DracoPy` — the same two the purchase
gates use, both already installed on this Mac.

### The two structures with no mesh

Twelve of the heart's fourteen hotspots take their dot from their own like-named
part. Two cannot, because BodyParts3D does not model them as separately
selectable geometry:

- **the septum** — the wall between the two ventricles. The source's `wall of
  right ventricle` and `free wall of right ventricle` resolve to identical sets
  of meshes, so there is no septal shape to select.
- **the sino-atrial node** — no conducting tissue is modelled anywhere in the
  dataset.

Their dots come from written-down anatomical rules in
`3d-studio/tools/recipes/heart.anchors.json`. Each rule names the parts that
locate the structure and says in plain words why — the septum from the midpoint
between the two ventricles, the sino-atrial node from the right atrium, shifted
up and slightly forward into its wall. They are written down and reviewable
precisely because they are anatomy rather than measurement.

> **Those two dots are a judgement, not a measurement.** Every other dot is
> derived from the shape of the structure it names; these two are derived from a
> rule someone wrote about where the structure ought to be. They are the two to
> check by eye, and they are yours to accept or move.

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

### `❌ could not read … into a GLB`

The `.obj` file, or the recipe, could not be turned into a model at all. The line
immediately above says which — usually a file the recipe names that is not in the
`--obj-dir` folder, or a `.json` that is not a `specimen-assembly/v1` recipe. The
purchase gates are not run, because there is nothing fit to gate. Fix the path or
the recipe and run it again.

### `❌ .fbx files need Blender`

See the next section.

### `❌ file not found` / `❌ .zip is not a 3D model format`

A typo in the path, or the download is still a zip archive. Unzip it first and
point at the `.glb` inside.

---

## If your file is not a GLB

`.blend`, `.fbx`, `.dae`, `.stl` and `.ply` are not web formats. Converting them
into GLB needs **Blender**, the free 3D modelling program, and **Blender is not
installed on this Mac**. When the tool meets one of these formats and cannot find
Blender, it stops and says so rather than half-running and leaving you with
something that looks converted.

`.obj` used to be on that list and no longer is: it converts here, in Python,
with nothing installed. If you have a `.obj`, just run the command — and if you
have a folder full of them, read
[When the model arrives in pieces](#when-the-model-arrives-in-pieces) instead of
this section.

For the formats that do still need Blender, there are two ways forward. The
first is much faster:

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

One entry point, and the files behind it:

| File | Role |
|---|---|
| `3d-studio/tools/prepare_specimen.py` | The command you run. Works out the format, converts `.obj` and recipes itself, converts the Blender formats if Blender is present, runs the pipeline, then runs the purchase gates on the result. |
| `3d-studio/tools/obj_glb.py` | Reads `.obj` — one file, or every file a recipe names — and writes the multi-part model the rest of the pipeline expects. Python only, nothing to install. Called for you; it has its own small command line if you ever want it directly. |
| `3d-studio/tools/recipes/<name>.recipe.json` | The assembly recipe: which named parts a specimen has, which source files make each one, and where the source came from. |
| `3d-studio/tools/recipes/<name>.anchors.json` | Anchor rules for the structures that have no mesh part of their own. Read by `derive_anchors.py`; optional, and absent for a specimen that needs none. |
| `3d-studio/tools/specimen_pipeline.mjs` | Does the 3D work. Never run directly. |
| `3d-studio/validate_specimen_glb.py` | The purchase gates. The only thing that gets to say pass or fail. |
| `3d-studio/tools/derive_anchors.py` | A separate command, run after the specimen exists: derives each hotspot's `position3d` from the finished model. |

The pipeline, in order: read the `.obj` files into a model if that is what
arrived → remove duplicated data → merge identical points → reduce triangles
(only if over 60,000, by an amount calculated from the actual count) → shrink
surface images to 1024 pixels max, keeping their proportions → compress → write →
**re-open the written file and check every part name is still there**.

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
| 6 | a `.obj` file or an assembly recipe could not be read into a model |

### The same command through npm

If you are already inside `3d-studio/`, this is equivalent:

```
npm run prepare-specimen -- ~/Downloads/heart.glb --name heart
```

The bare `--` is npm's way of saying "everything after this belongs to the
script, not to npm".

---

## Known limits, stated plainly

- **The Blender conversion path has never run.** That is `.blend`, `.fbx`,
  `.dae`, `.stl` and `.ply` — `.obj` no longer goes anywhere near it. There is no
  Blender on this machine. The code is written to Blender's documented
  command-line interface and reviewed, but reviewed is not tested. Treat its
  first real run as something to check, not to trust.
- **The `.obj` path has been run exactly once.** One specimen — the heart — has
  been through it, and there are no automated tests over it yet. It worked and
  the result passed the gates, but a single run on a single source is thin
  evidence. Check the part list in the report against what you expected, rather
  than assuming it.
- **Two heart structures have no mesh of their own.** The septum and the
  sino-atrial node: BodyParts3D models neither as separately addressable
  geometry, so neither can be isolated, and their dots are placed from a
  written-down anatomical rule rather than from geometry. That rule is reviewable
  (`3d-studio/tools/recipes/heart.anchors.json`) but it is still a judgement, and
  it is the one part of the dot placement worth checking by eye.
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
