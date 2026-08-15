/**
 * 3D Studio — glTF conversion worker for an acquired specimen.
 *
 *   node 3d-studio/tools/specimen_pipeline.mjs --in downloaded.glb --out public/assets/heart.glb
 *   node 3d-studio/tools/specimen_pipeline.mjs --in a.gltf --out b.glb --name heart --report r.json
 *
 * Not the entry point. `tools/prepare_specimen.py` drives this and then chains
 * the purchase-gate validator behind it, so one command runs a downloaded file
 * all the way to a verdict. This file does the glTF work in between.
 *
 * What it does, and why in this order
 * -----------------------------------
 * A model bought or downloaded for the web is almost never inside the studio's
 * budget: 300k triangles and 4096² textures are ordinary on Sketchfab. The
 * budget is not a preference — validate_specimen_glb.py gates on it, because a
 * phone on a school network has to load this. So:
 *
 *   dedup()            drop duplicated meshes/materials/textures the exporter left
 *   weld()             merge bitwise-identical vertices; simplification needs it
 *   simplify()         meshoptimizer, ONLY when over the 60,000-triangle gate,
 *                      at a ratio computed from the actual count, escalating the
 *                      error budget only as far as it has to — and skipping any
 *                      part the recipe marks `preserve` (see --preserve below)
 *   textureCompress()  resize to 1024² max, aspect preserved, downsize only
 *   draco()            edgebreaker, the same setting the test specimen uses
 *
 * PART NAMES ARE LOAD-BEARING — the reason flatten() and join() are absent
 * -----------------------------------------------------------------------
 * src/renderer/mesh/parts.ts takes a part's name from the node name the GLB
 * declares, verbatim, and Stage 3's isolate and layers tools are built on that
 * list. join() would merge nodes and flatten() would collapse the hierarchy;
 * either one produces a file that loads, renders, looks correct in a viewer,
 * and has silently destroyed every tool built on the parts. Neither is called
 * here, and after writing, the output is RE-READ and its part names compared
 * against the input's. A mismatch fails the run loudly rather than shipping a
 * pretty asset with nothing to isolate.
 *
 * Who decides pass/fail
 * ---------------------
 * Not this file. validate_specimen_glb.py is the authority on the six purchase
 * gates and prepare_specimen.py always runs it on the output. This worker exits
 * non-zero only when the artifact is unfit to be gated at all — part names
 * lost, Draco absent, nothing written. Budget overshoot is reported loudly here
 * and FAILED by the validator, so there is exactly one verdict, from one place.
 */

import { readFileSync, statSync, mkdirSync, writeFileSync } from 'node:fs';
import { basename, dirname, resolve } from 'node:path';

import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import { PropertyType } from '@gltf-transform/core';
import {
  dedup, draco, prune, simplifyPrimitive, textureCompress, weld,
} from '@gltf-transform/functions';
import { MeshoptDecoder, MeshoptEncoder, MeshoptSimplifier } from 'meshoptimizer';
import draco3d from 'draco3dgltf';
import sharp from 'sharp';

// Mirrors validate_specimen_glb.py exactly. If those move, these move with them.
const TRIANGLE_LIMIT = 60_000;
const TEXTURE_LIMIT = 1024;
const SIZE_LIMIT = 3 * 1024 * 1024;

// Aim under the gate, not at it: simplification lands approximately, and a file
// that clears by four triangles today fails on the next re-export.
const TRIANGLE_TARGET = 55_000;

// Error budget, as a fraction of mesh radius, climbing only as far as needed.
// The first rung is imperceptible; the last is visible on close inspection and
// is a last resort before admitting the source is too heavy to use.
const ERROR_LADDER = [0.001, 0.005, 0.02, 0.05];

// ── CLI ──────────────────────────────────────────────────────────────────────

function arg(flag, fallback = null) {
  const i = process.argv.indexOf(flag);
  return i !== -1 && process.argv[i + 1] ? process.argv[i + 1] : fallback;
}

const inArg = arg('--in');
const outArg = arg('--out');
const specimenName = arg('--name', null);
const reportPath = arg('--report', null);

// Parts the recipe forbids the simplifier from touching, by node/mesh name.
//
// MRB-222 is the case that forced this. The heart's ventricular myocardium
// carries the one measurement the specimen exists to show — a left free wall of
// 9.4mm against a right of 3.5mm — on a median edge length of 1.62mm. That is
// about two triangles across the thin wall, so a uniform decimation eats the
// RIGHT ventricle first and destroys the teaching point while leaving a mesh
// that still looks like a heart. No error budget expresses "spend the error
// anywhere but here"; only excluding the part does.
//
// Preservation is never free. The ratio below is computed against the budget
// that REMAINS once the preserved parts have taken their share, so protecting
// one structure visibly costs the others — which is the honest trade and is
// printed as such.
let preserveNames;
try {
  preserveNames = new Set(JSON.parse(arg('--preserve', '[]')));
} catch {
  console.error('  ❌ --preserve must be a JSON array of part names');
  process.exit(64);
}

if (!inArg || !outArg) {
  console.error('usage: node tools/specimen_pipeline.mjs --in <src.glb|src.gltf> '
    + '--out <dst.glb> [--name <specimen-id>] [--report <report.json>]');
  process.exit(64);
}

const inPath = resolve(inArg);
const outPath = resolve(outArg);

if (inPath === outPath) {
  console.error(`  ❌ input and output are the same file: ${inPath}`);
  console.error('     Write somewhere else — the source is the only copy of the original.');
  process.exit(1);
}

// Underscore-prefixed assets are the generated fixtures (_test-specimen.glb,
// _test-plate.svg). Other gates are built on their exact bytes, and vite.config
// treats a non-underscore .glb as "acquired". Refuse to write over either
// convention by accident.
if (basename(outPath).startsWith('_')) {
  console.error(`  ❌ refusing to write ${basename(outPath)}`);
  console.error('     Underscore-prefixed files are generated test fixtures that other');
  console.error('     gates depend on. Pass --name <specimen-id> or --out <path>.');
  process.exit(1);
}

// ── survey helpers ───────────────────────────────────────────────────────────

/** Triangles in one primitive, counted the way validate_specimen_glb.py counts
 * them: indexed count over draw mode, and points/lines contribute none. */
function primitiveTriangles(prim) {
  const mode = prim.getMode();
  const indices = prim.getIndices();
  const n = indices ? indices.getCount() : prim.getAttribute('POSITION').getCount();
  if (mode === 4) return n / 3;                    // TRIANGLES
  if (mode === 5 || mode === 6) return Math.max(n - 2, 0); // STRIP / FAN
  return 0;
}

function countTriangles(document) {
  let total = 0;
  for (const mesh of document.getRoot().listMeshes()) {
    for (const prim of mesh.listPrimitives()) total += primitiveTriangles(prim);
  }
  return Math.round(total);
}

/** The parts the renderer will see.
 *
 * three's GLTFLoader names the Object3D it builds after the glTF NODE, and
 * collectParts() in src/renderer/mesh/parts.ts pushes one part per mesh-bearing
 * object. So the set that matters is: the name of every node that carries a
 * mesh, in declaration order. A node whose name is empty is recorded as such —
 * the renderer captions it `PART n` — and it still has to survive the round
 * trip, so it is compared like any other entry. */
function surveyParts(document) {
  const root = document.getRoot();
  const scenes = root.listScenes();
  const seen = new Set();
  const parts = [];

  const visit = (node) => {
    if (seen.has(node)) return;
    seen.add(node);
    const mesh = node.getMesh();
    if (mesh) {
      parts.push({
        node: node.getName() || '',
        mesh: mesh.getName() || '',
        triangles: Math.round(
          mesh.listPrimitives().reduce((n, p) => n + primitiveTriangles(p), 0)),
      });
    }
    for (const child of node.listChildren()) visit(child);
  };

  for (const scene of scenes) for (const node of scene.listChildren()) visit(node);
  // Nodes outside every scene are not loaded by three, but a source file that
  // parks geometry there is worth seeing in the report rather than silently
  // dropping, so they are surveyed last and marked.
  for (const node of root.listNodes()) {
    if (seen.has(node) || !node.getMesh()) continue;
    const mark = parts.length;
    visit(node);
    for (let i = mark; i < parts.length; i++) parts[i].orphan = true;
  }
  return parts;
}

function surveyTextures(document) {
  return document.getRoot().listTextures().map((texture, i) => {
    const size = texture.getSize();
    const image = texture.getImage();
    return {
      index: i,
      name: texture.getName() || `(unnamed ${i})`,
      mimeType: texture.getMimeType() || 'unknown',
      width: size ? size[0] : null,
      height: size ? size[1] : null,
      bytes: image ? image.byteLength : 0,
    };
  });
}

function describeTexture(t) {
  const dims = t.width === null ? 'size unreadable' : `${t.width}×${t.height}`;
  const over = t.width !== null && (t.width > TEXTURE_LIMIT || t.height > TEXTURE_LIMIT);
  return `${t.name} — ${dims} ${t.mimeType}, ${t.bytes.toLocaleString()} bytes`
    + (over ? '  ⚠️ over the limit' : '');
}

function partKey(part) {
  return part.node === '' ? '(unnamed node)' : part.node;
}

function bytes(n) {
  return `${n.toLocaleString()} bytes (${(n / (1024 * 1024)).toFixed(2)} MiB)`;
}

// ── run ──────────────────────────────────────────────────────────────────────

console.log('3D Studio — specimen conversion pipeline'
  + (specimenName ? ` — ${specimenName}` : '') + '\n');

let bytesBefore;
try {
  bytesBefore = statSync(inPath).size;
} catch {
  console.error(`  ❌ input not found: ${inPath}`);
  process.exit(1);
}

await MeshoptDecoder.ready;
await MeshoptEncoder.ready;
await MeshoptSimplifier.ready;

// Every extension is registered for READING, because a downloaded asset may
// arrive already Draco- or meshopt-compressed, carrying KHR_materials_* it does
// not need. Registering them means the file opens instead of throwing.
const io = new NodeIO()
  .registerExtensions(ALL_EXTENSIONS)
  .registerDependencies({
    'draco3d.decoder': await draco3d.createDecoderModule(),
    'draco3d.encoder': await draco3d.createEncoderModule(),
    'meshopt.decoder': MeshoptDecoder,
    'meshopt.encoder': MeshoptEncoder,
  });

let document;
try {
  document = await io.read(inPath);
} catch (error) {
  console.error(`  ❌ could not read ${inPath}`);
  console.error(`     ${error.message}`);
  process.exit(1);
}

// ── before ───────────────────────────────────────────────────────────────────

const trianglesBefore = countTriangles(document);
const texturesBefore = surveyTextures(document);
const partsBefore = surveyParts(document);

console.log('  BEFORE');
console.log(`    File:       ${inPath}`);
console.log(`                ${bytes(bytesBefore)}`
  + (inPath.toLowerCase().endsWith('.gltf')
    ? ' — .gltf, external buffers and images not counted' : ''));
console.log(`    Triangles:  ${trianglesBefore.toLocaleString()} `
  + `(gate: under ${TRIANGLE_LIMIT.toLocaleString()})`);
console.log(`    Textures:   ${texturesBefore.length}`);
for (const t of texturesBefore) console.log(`                ${describeTexture(t)}`);
console.log(`    Parts:      ${partsBefore.length} mesh-bearing node(s)`);
for (const p of partsBefore) {
  console.log(`                ${partKey(p)}`
    + (p.mesh && p.mesh !== p.node ? `  [mesh: ${p.mesh}]` : '')
    + `  ${p.triangles.toLocaleString()} tris`
    + (p.orphan ? '  ⚠️ outside every scene — three will not load it' : ''));
}
if (partsBefore.length === 0) {
  console.error('\n  ❌ the source declares no mesh-bearing nodes — nothing to convert.');
  process.exit(1);
}
if (partsBefore.length === 1) {
  console.log('\n    NOTE: one part only. The file will load and render, but Stage 3\'s');
  console.log('          isolate and layers tools have nothing to work with. A specimen');
  console.log('          modelled as separate named parts is worth going back for.');
}

// ── work ─────────────────────────────────────────────────────────────────────

console.log('\n  WORK');

await document.transform(dedup(), weld());
console.log(`    dedup + weld:      ${countTriangles(document).toLocaleString()} triangles`);

const simplifyPasses = [];
let triangles = countTriangles(document);

const meshTriangles = (mesh) => mesh.listPrimitives()
  .reduce((n, p) => n + primitiveTriangles(p), 0);

// ── topology, as the WATERTIGHT GATE sees it ─────────────────────────────────
//
// validate_specimen_glb.py welds vertices by POSITION at a tolerance of the
// mesh extent × 1e-6 before counting edges. Counting raw indices instead
// reports every duplicated seam vertex as a boundary edge, which is a fact
// about the file rather than a hole in the surface — so this mirrors the gate's
// rule rather than inventing a second one. If the gate's tolerance moves, this
// moves with it.
const WELD_REL = 1e-6;

/** (boundary, over-shared, misoriented) for one primitive. All zero = the
 * closed orientable manifold the watertight gate demands. */
function weldedDefects(prim) {
  const indices = prim.getIndices();
  if (!indices || prim.getMode() !== 4) return { boundary: 0, over: 0, mis: 0 };
  const position = prim.getAttribute('POSITION');
  const count = position.getCount();

  const xyz = new Float64Array(count * 3);
  const lo = [Infinity, Infinity, Infinity];
  const hi = [-Infinity, -Infinity, -Infinity];
  const scratch = [0, 0, 0];
  for (let i = 0; i < count; i++) {
    position.getElement(i, scratch);
    for (let k = 0; k < 3; k++) {
      xyz[i * 3 + k] = scratch[k];
      if (scratch[k] < lo[k]) lo[k] = scratch[k];
      if (scratch[k] > hi[k]) hi[k] = scratch[k];
    }
  }
  const extent = Math.max(hi[0] - lo[0], hi[1] - lo[1], hi[2] - lo[2]);
  const tol = Math.max(extent, 1e-12) * WELD_REL;

  const seen = new Map();
  const remap = new Int32Array(count);
  for (let i = 0; i < count; i++) {
    const key = `${Math.round(xyz[i * 3] / tol)},${Math.round(xyz[i * 3 + 1] / tol)},`
      + `${Math.round(xyz[i * 3 + 2] / tol)}`;
    let id = seen.get(key);
    if (id === undefined) { id = seen.size; seen.set(key, id); }
    remap[i] = id;
  }

  const undirected = new Map();
  const directed = new Map();
  const n = indices.getCount();
  for (let i = 0; i < n; i += 3) {
    const a = remap[indices.getScalar(i)];
    const b = remap[indices.getScalar(i + 1)];
    const c = remap[indices.getScalar(i + 2)];
    if (a === b || b === c || a === c) continue;            // degenerate
    const tri = [a, b, c];
    for (let e = 0; e < 3; e++) {
      const u = tri[e];
      const v = tri[(e + 1) % 3];
      const key = u < v ? `${u},${v}` : `${v},${u}`;
      undirected.set(key, (undirected.get(key) || 0) + 1);
      const dir = `${u},${v}`;
      directed.set(dir, (directed.get(dir) || 0) + 1);
    }
  }
  let boundary = 0;
  let over = 0;
  let mis = 0;
  for (const v of undirected.values()) { if (v === 1) boundary++; else if (v > 2) over++; }
  for (const v of directed.values()) if (v > 1) mis++;
  return { boundary, over, mis };
}

const isManifold = (d) => d.boundary === 0 && d.over === 0 && d.mis === 0;
const describeDefects = (d) => `b${d.boundary}/o${d.over}/m${d.mis}`;

/** Enough of a primitive to put it back exactly as it was.
 *
 * simplifyPrimitive replaces a primitive's accessors rather than editing them,
 * so keeping references to the old ones is not safe — they may be detached by
 * the time a retry needs them. The raw arrays are. */
function snapshotPrim(prim) {
  const indices = prim.getIndices();
  const semantics = prim.listSemantics();
  return {
    indices: indices ? indices.getArray().slice() : null,
    indicesType: indices ? indices.getComponentType() : null,
    attributes: semantics.map((semantic) => {
      const accessor = prim.getAttribute(semantic);
      return {
        semantic,
        array: accessor.getArray().slice(),
        type: accessor.getType(),
        componentType: accessor.getComponentType(),
        normalized: accessor.getNormalized(),
      };
    }),
  };
}

function restorePrim(doc, prim, snap) {
  for (const saved of snap.attributes) {
    prim.setAttribute(saved.semantic, doc.createAccessor()
      .setArray(saved.array)
      .setType(saved.type)
      .setNormalized(saved.normalized));
  }
  if (snap.indices) {
    prim.setIndices(doc.createAccessor().setArray(snap.indices));
  }
}

/** The meshes split by whether the recipe protects them.
 *
 * Matched on MESH name. obj_glb.py writes the mesh, the node and the recipe's
 * part name as the same string, and a name in --preserve that matches nothing
 * is reported rather than ignored: a typo there would silently un-protect the
 * one part the flag exists to protect. */
const preserved = [];
const simplifiable = [];
for (const mesh of document.getRoot().listMeshes()) {
  (preserveNames.has(mesh.getName()) ? preserved : simplifiable).push(mesh);
}
const unmatched = [...preserveNames].filter(
  (name) => !preserved.some((m) => m.getName() === name));
if (unmatched.length) {
  console.error(`\n  ❌ --preserve names ${unmatched.length} part(s) that do not `
    + `exist in the model: ${unmatched.join(', ')}`);
  console.error('     The recipe and the GLB disagree about what this specimen is');
  console.error('     made of. Refusing to simplify on a guess.');
  process.exit(1);
}

const preservedTriangles = Math.round(
  preserved.reduce((n, m) => n + meshTriangles(m), 0));
if (preserved.length) {
  console.log(`    preserved:         ${preserved.length} part(s), `
    + `${preservedTriangles.toLocaleString()} triangles never simplified — `
    + `${preserved.map((m) => m.getName()).join(', ')}`);
}

/** One simplification pass over the SIMPLIFIABLE meshes only.
 *
 * The ratio is computed from the current count of what may actually be cut,
 * against the budget left after preservation — an asset 5× over budget and one
 * 5% over need very different cuts, and a preserved part changes the sum. This
 * mirrors gltf-transform's own simplify() transform (weld first, then
 * simplifyPrimitive per primitive, then drop anything simplified away to
 * nothing); it is scoped rather than reimplemented. simplifyPrimitive is
 * exported but marked @hidden, so it is pinned by package-lock.json and worth
 * re-checking on any gltf-transform upgrade. */
// How far a part is allowed to climb back up when the requested cut breaks its
// topology, and the point past which backing off further is pointless.
const BACKOFF_STEPS = [1.5, 2.25, 3.5, 5.0];
const BACKOFF_CEILING = 0.95;

async function simplifyPass(error, lockBorder) {
  const before = Math.round(simplifiable.reduce((n, m) => n + meshTriangles(m), 0));
  const budget = TRIANGLE_TARGET - preservedTriangles;
  const ratio = Math.max(0.01, Math.min(0.99, budget / before));
  await document.transform(weld({ overwrite: false }));

  for (const mesh of simplifiable) {
    for (const prim of mesh.listPrimitives()) {
      if (prim.getMode() !== 4) continue;               // TRIANGLES only

      // A part that was ALREADY non-manifold is not this pass's problem, and
      // holding simplification hostage to a defect the source shipped with
      // would be the wrong trade. Only a part the simplifier BREAKS is backed
      // off, so the check can never make an existing failure worse.
      const wasManifold = isManifold(weldedDefects(prim));
      const snapshot = wasManifold ? snapshotPrim(prim) : null;

      simplifyPrimitive(prim, {
        simplifier: MeshoptSimplifier, ratio, error, lockBorder,
      });
      if (!wasManifold) continue;

      let defects = weldedDefects(prim);
      if (isManifold(defects)) continue;

      // THE BACKOFF. The simplifier tore this part; ask for less of it until it
      // holds. Thin branching tubes are what provoke this — the heart's 54
      // coronary segments pinch shut somewhere below ratio 0.40 while the
      // atrial walls are still clean at 0.15 — so the tolerable cut is a
      // property of the PART, not a number anyone can pick in advance. The
      // alternative is shipping a specimen the watertight gate then fails,
      // having spent the whole pipeline getting there.
      let healed = false;
      for (const step of BACKOFF_STEPS) {
        const retry = Math.min(BACKOFF_CEILING, ratio * step);
        restorePrim(document, prim, snapshot);
        simplifyPrimitive(prim, {
          simplifier: MeshoptSimplifier, ratio: retry, error, lockBorder,
        });
        defects = weldedDefects(prim);
        if (isManifold(defects)) {
          console.log(`    simplify:          ${mesh.getName()} tore at ratio `
            + `${ratio.toFixed(3)} — backed off to ${retry.toFixed(3)}, `
            + `${primitiveTriangles(prim).toLocaleString()} triangles, topology intact`);
          healed = true;
          break;
        }
        if (retry >= BACKOFF_CEILING) break;
      }
      if (!healed) {
        restorePrim(document, prim, snapshot);
        console.log(`    simplify:          ⚠️  ${mesh.getName()} could not be `
          + `simplified without tearing (${describeDefects(defects)}) — left at `
          + `${primitiveTriangles(prim).toLocaleString()} triangles, uncut`);
      }
    }
  }

  const after = countTriangles(document);
  simplifyPasses.push({ ratio, error, lockBorder, from: triangles, to: after });
  console.log(`    simplify:          ratio ${ratio.toFixed(3)}, error ${error}`
    + `${lockBorder ? '' : ', borders UNLOCKED'} — `
    + `${triangles.toLocaleString()} → ${after.toLocaleString()} triangles`);
  if (after >= triangles) {
    console.log('                       no further reduction at this error budget');
  }
  triangles = after;
}

if (preservedTriangles >= TRIANGLE_LIMIT) {
  // No amount of cutting elsewhere can help: the protected geometry alone is
  // over the gate. Say so plainly rather than grinding through the ladder.
  console.error(`\n  ❌ the preserved parts alone are `
    + `${preservedTriangles.toLocaleString()} triangles, at or over the `
    + `${TRIANGLE_LIMIT.toLocaleString()} gate.`);
  console.error('     Nothing the simplifier is allowed to touch can bring this');
  console.error('     specimen inside budget. Either the preservation or the gate');
  console.error('     has to change, and that is a ruling, not a build setting.');
  process.exit(1);
}

if (triangles < TRIANGLE_LIMIT) {
  console.log(`    simplify:          skipped — already under `
    + `${TRIANGLE_LIMIT.toLocaleString()}`);
} else {
  // lockBorder matters more here than the docs suggest. A UV seam splits
  // vertices that share a position, so the simplifier sees a topological
  // border down the seam; collapsing it moves the two sides apart and opens a
  // crack, which the watertight gate then FAILS. Measured on a 270k synthetic:
  // 327 boundary edges with borders free, 0 with them locked. Locked is the
  // default here for that reason.
  for (const error of ERROR_LADDER) {
    if (triangles < TRIANGLE_LIMIT) break;
    await simplifyPass(error, true);
  }
  if (triangles >= TRIANGLE_LIMIT) {
    // Locked borders can pin a mesh above budget. Unlocking is the last thing
    // to try and the first thing to suspect afterwards, so it says so.
    console.log('                       still over budget with borders locked — '
      + 'unlocking as a last resort');
    await simplifyPass(ERROR_LADDER[ERROR_LADDER.length - 1], false);
    console.log('                       ⚠️  cracks along seams are now possible; '
      + 'the watertight gate below is the check that matters');
  }
}

// Sweep up accessors nothing points at any more.
//
// The backoff above restores a primitive by building fresh accessors from the
// snapshot; the retry that follows immediately replaces them, leaving the
// originals owned by the document but referenced by nothing. NodeIO serialises
// every accessor the root owns, and an orphan is not part of any primitive so
// Draco never touches it — it lands in the buffer at full size, uncompressed.
// Measured on the heart: two backoffs left 12 orphans and took the written file
// from 203 KB to 796 KB, for 4% more triangles. Scoped to accessors so this
// cannot quietly remove a material, a node or a mesh.
await document.transform(prune({
  propertyTypes: [PropertyType.ACCESSOR],
  keepAttributes: true,
}));
console.log('    prune:             unreferenced accessors dropped');

const oversizeTextures = texturesBefore.filter(
  (t) => t.width !== null && (t.width > TEXTURE_LIMIT || t.height > TEXTURE_LIMIT));
if (oversizeTextures.length > 0) {
  // resize is fitWithin(): aspect ratio preserved, and a texture already inside
  // the limit comes back untouched. Run only when something is actually over,
  // so textures that are already fine are not re-encoded for nothing.
  await document.transform(
    textureCompress({ encoder: sharp, resize: [TEXTURE_LIMIT, TEXTURE_LIMIT] }));
  console.log(`    textureCompress:   ${oversizeTextures.length} texture(s) over `
    + `${TEXTURE_LIMIT}² resized`);
} else {
  console.log(`    textureCompress:   skipped — every texture already within `
    + `${TEXTURE_LIMIT}²`);
}

// Same setting as the test specimen (tools/compress_test_specimen.mjs):
// edgebreaker is the smaller method for closed manifold meshes, and closed
// manifold is what the watertight gate requires anyway.
await document.transform(draco({ method: 'edgebreaker' }));
console.log('    draco:             edgebreaker');

mkdirSync(dirname(outPath), { recursive: true });
await io.write(outPath, document);
const bytesAfter = statSync(outPath).size;

// ── verify ───────────────────────────────────────────────────────────────────

// Prove the claims against the written file rather than against the in-memory
// document, in the same spirit as compress_test_specimen.mjs: what ships is
// what is checked.
const head = readFileSync(outPath)
  .subarray(0, Math.min(bytesAfter, 65536)).toString('latin1');
const dracoDeclared = head.includes('KHR_draco_mesh_compression');

const reread = await io.read(outPath);
const partsAfter = surveyParts(reread);
const trianglesAfter = countTriangles(reread);
const texturesAfter = surveyTextures(reread);

const namesBefore = partsBefore.map(partKey).sort();
const namesAfter = partsAfter.map(partKey).sort();
const namesPreserved = namesBefore.length === namesAfter.length
  && namesBefore.every((name, i) => name === namesAfter[i]);

console.log('\n  AFTER');
console.log(`    File:       ${outPath}`);
console.log(`                ${bytes(bytesBefore)} → ${bytes(bytesAfter)}`
  + (bytesAfter < bytesBefore
    ? `  (${(bytesBefore / bytesAfter).toFixed(2)}× smaller)` : ''));
console.log(`    Triangles:  ${trianglesBefore.toLocaleString()} → `
  + `${trianglesAfter.toLocaleString()}`);
console.log(`    Textures:   ${texturesAfter.length}`);
for (const t of texturesAfter) console.log(`                ${describeTexture(t)}`);
console.log(`    Parts:      ${partsAfter.length} — the names Stage 3 isolates on:`);
for (const p of partsAfter) {
  console.log(`                ${partKey(p)}  ${p.triangles.toLocaleString()} tris`);
}

console.log('\n  CHECKS');
console.log(`    Part names: ${namesPreserved ? '✅ preserved' : '❌ CHANGED'} `
  + `(${namesBefore.length} in, ${namesAfter.length} out)`);
console.log(`    Draco:      ${dracoDeclared ? '✅' : '❌'} `
  + `KHR_draco_mesh_compression ${dracoDeclared
    ? 'present in the JSON chunk' : 'MISSING — not actually compressed'}`);
console.log(`    Triangles:  ${trianglesAfter < TRIANGLE_LIMIT ? '✅ under' : '⚠️  OVER'} `
  + `${TRIANGLE_LIMIT.toLocaleString()}`);
console.log(`    File size:  ${bytesAfter < SIZE_LIMIT ? '✅ under' : '⚠️  OVER'} `
  + `${SIZE_LIMIT.toLocaleString()} (3 MiB)`);

if (reportPath) {
  writeFileSync(resolve(reportPath), JSON.stringify({
    specimen: specimenName,
    input: inPath,
    output: outPath,
    bytesBefore,
    bytesAfter,
    trianglesBefore,
    trianglesAfter,
    preservedParts: preserved.map((m) => m.getName()),
    preservedTriangles,
    simplifyPasses,
    texturesBefore,
    texturesAfter,
    parts: partsAfter.map(partKey),
    namesPreserved,
    dracoDeclared,
  }, null, 2) + '\n');
}

if (!namesPreserved) {
  const lost = namesBefore.filter((n) => !namesAfter.includes(n));
  const gained = namesAfter.filter((n) => !namesBefore.includes(n));
  console.error('\n  ❌ PART NAMES DID NOT SURVIVE THE ROUND TRIP.');
  if (lost.length) console.error(`     lost:   ${lost.join(', ')}`);
  if (gained.length) console.error(`     gained: ${gained.join(', ')}`);
  console.error('     Stage 3\'s isolate and layers tools read these names from the');
  console.error('     GLB. The written file is not usable as a specimen — do not ship');
  console.error('     it, and do not update the content record to point at it.');
  process.exit(1);
}

if (!dracoDeclared) {
  console.error('\n  ❌ the output is not Draco-compressed — purchase gate 4 cannot pass.');
  process.exit(1);
}

const overBudget = trianglesAfter >= TRIANGLE_LIMIT || bytesAfter >= SIZE_LIMIT;
if (overBudget) {
  console.log('\n  ⚠️  Written, but still over budget. The validator below will FAIL it,');
  console.log('     and that failure is real: this source is too heavy for the studio');
  console.log('     as it stands. Look for a lighter version of the model, or one whose');
  console.log('     textures do the work its geometry is currently doing.');
} else {
  console.log('\n  ✅ conversion complete. Purchase gates are the validator\'s call.');
}

process.exit(0);
