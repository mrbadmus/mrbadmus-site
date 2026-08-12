/**
 * 3D Studio — Draco compressor for the synthetic test specimen (Stage 2, MRB-187).
 *
 *   node 3d-studio/tools/compress_test_specimen.mjs
 *   node 3d-studio/tools/compress_test_specimen.mjs --in a.glb --out b.glb
 *
 * tools/make_test_specimen.py writes the uncompressed intermediate. This turns
 * it into the file the renderer actually loads: genuinely Draco-compressed,
 * carrying KHR_draco_mesh_compression, so three.js DRACOLoader is exercised on
 * the real code path rather than quietly skipped. A plain re-save would look
 * fine and prove nothing.
 *
 * Both files are generated artifacts and both are gitignored — never content.
 */

import { readFileSync, statSync, mkdirSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import { NodeIO } from '@gltf-transform/core';
import { KHRDracoMeshCompression } from '@gltf-transform/extensions';
import { draco } from '@gltf-transform/functions';
import draco3d from 'draco3dgltf';

const STUDIO_DIR = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const DEFAULT_IN = resolve(STUDIO_DIR, 'tools/build/_test-specimen.raw.glb');
const DEFAULT_OUT = resolve(STUDIO_DIR, 'public/assets/_test-specimen.glb');
const SIZE_LIMIT = 3 * 1024 * 1024; // the validator's file-size gate

function arg(flag, fallback) {
  const i = process.argv.indexOf(flag);
  return i !== -1 && process.argv[i + 1] ? resolve(process.argv[i + 1]) : fallback;
}

const inPath = arg('--in', DEFAULT_IN);
const outPath = arg('--out', DEFAULT_OUT);

console.log('3D Studio — Draco compression of the test specimen\n');

let rawBytes;
try {
  rawBytes = statSync(inPath).size;
} catch {
  console.error(`  ❌ input not found: ${inPath}`);
  console.error('     Run tools/make_test_specimen.py first.');
  process.exit(1);
}

const io = new NodeIO()
  .registerExtensions([KHRDracoMeshCompression])
  .registerDependencies({
    'draco3d.encoder': await draco3d.createEncoderModule(),
    'draco3d.decoder': await draco3d.createDecoderModule(),
  });

const document = await io.read(inPath);

// Edgebreaker is the smaller of the two Draco methods for closed manifold
// meshes, which is exactly what this specimen is. Quantisation stays at the
// defaults: 14-bit positions over a 2-unit model is a ~0.00012-unit grid,
// two orders of magnitude finer than the shortest edge here, so nothing
// collapses and the mesh stays watertight through the round trip.
await document.transform(draco({ method: 'edgebreaker' }));

mkdirSync(dirname(outPath), { recursive: true });
await io.write(outPath, document);

const outBytes = statSync(outPath).size;

// Prove the claim rather than assert it: the extension name must actually be
// in the GLB's JSON chunk. A re-save with the extension merely registered but
// no compressed payload would still be a failure.
const head = readFileSync(outPath).subarray(0, Math.min(outBytes, 65536)).toString('latin1');
const declared = head.includes('KHR_draco_mesh_compression');

const ratio = rawBytes / outBytes;
console.log(`  Input:      ${inPath}`);
console.log(`              ${rawBytes.toLocaleString()} bytes`);
console.log(`  Output:     ${outPath}`);
console.log(`              ${outBytes.toLocaleString()} bytes`);
console.log(`  Ratio:      ${ratio.toFixed(2)}× smaller `
  + `(${(100 - (outBytes / rawBytes) * 100).toFixed(1)}% saved)`);
console.log(`  Size gate:  ${outBytes < SIZE_LIMIT ? '✅ under' : '❌ over'} `
  + `${SIZE_LIMIT.toLocaleString()} bytes (3 MiB)`);
console.log(`  Draco:      ${declared ? '✅' : '❌'} KHR_draco_mesh_compression `
  + `${declared ? 'present in the JSON chunk' : 'MISSING — not actually compressed'}`);

if (!declared || outBytes >= rawBytes || outBytes >= SIZE_LIMIT) {
  console.error('\n  ❌ compression did not produce a usable asset.');
  process.exit(1);
}

console.log('\n  ✅ done. Verify the round trip with:');
console.log(`     python3 validate_specimen_glb.py ${outPath}`);
