// @vitest-environment node
// Gate 4 — Stage 0's content validation still passes. The validator is the
// build gate from MRB-185: presence, assets, lesson URLs, hotspot coordinate
// parity, single-name binding, naming discipline. Exit code 0 or this fails.

import { describe, expect, it } from 'vitest'
import { spawnSync } from 'node:child_process'
import { fileURLToPath } from 'node:url'

const STUDIO_DIR = fileURLToPath(new URL('../..', import.meta.url))

describe('gate 4 — Stage 0 content validation', () => {
  it('validate_content.py exits 0', () => {
    const result = spawnSync('python3', ['validate_content.py'], {
      cwd: STUDIO_DIR,
      encoding: 'utf8',
      timeout: 15000,
    })
    expect(result.error).toBeUndefined()
    expect(
      result.status,
      `validator failed:\n${result.stdout}\n${result.stderr}`,
    ).toBe(0)
    expect(result.stdout).toContain('all records valid')
  })

  // The provenance rows MRB-186 took out of the student panel did not get
  // deleted, they moved to docs/3d_studio_asset_manifest.md — and a provenance
  // document that silently falls behind the records it describes is worse than
  // no document, because it is read as current. It is generated, so staleness
  // is decidable: re-render and compare. Without this, "cannot drift" would be
  // a claim in a comment rather than a property of the repo.
  it('the asset manifest is current with the content records', () => {
    const result = spawnSync(
      'python3', ['tools/asset_manifest.py', '--check'],
      { cwd: STUDIO_DIR, encoding: 'utf8', timeout: 15000 },
    )
    expect(result.error).toBeUndefined()
    expect(
      result.status,
      `${result.stdout}\n${result.stderr}\n`
      + 'Run: python3 3d-studio/tools/asset_manifest.py',
    ).toBe(0)
  })

  // The septum's anchor, pinned. It is the one heart hotspot whose landmark
  // is a surface FURROW rather than a part of the mesh, and the number is
  // derived — tools/derive_anchors.py, under the surfaceSeam rule in
  // tools/recipes/heart.anchors.json, with the measurements that rejected two
  // earlier readings written down beside it.
  //
  // Pinned rather than re-derived here: the derivation needs numpy and takes
  // about a minute, which is not a thing to pay on every test run. The full
  // agreement check is `python3 tools/derive_anchors.py heart --check`, for
  // when a recipe or a mesh changes. This is the cheap tripwire that makes an
  // accidental change to an authored anatomy coordinate loud immediately.
  it('the septum sits on the anterior interventricular groove', async () => {
    const heart = (await import('../../content/heart.json')).default
    const at = (id: string) =>
      heart.hotspots.find((h) => h.id === id)!.position3d as number[]

    const septum = at('heart.septum')
    expect(septum).toEqual([0.16901, 0.02181, 0.23811])

    // The three properties that make it the groove rather than a chamber wall,
    // in the GLB's own axes (+x patient's left, +y superior, +z anterior).
    const rv = at('heart.right-ventricle')
    const lv = at('heart.left-ventricle')

    // ANTERIOR — this is the anterior groove, not the posterior one.
    expect(septum[2]).toBeGreaterThan(0)

    // BETWEEN THE VENTRICLES — a wall between two chambers is not out on
    // either one. The value this replaced sat at x 0.1896, past the midpoint
    // and out towards the left ventricular free wall.
    expect(septum[0]).toBeGreaterThan(rv[0])
    expect(septum[0]).toBeLessThan(lv[0])

    // NOT THE LEFT VENTRICLE'S OWN DOT. Two anchors close enough to read as
    // one is the failure the move was ruled against.
    const gap = Math.hypot(...septum.map((c, i) => c - lv[i]))
    expect(gap).toBeGreaterThan(0.1)
  })
})
