// Which file the renderer actually fetches.
//
// The heart GLB has not been acquired yet (spec §4 — Mide is sourcing a free
// CC-licensed one), so no specimen has a real mesh on disk. Rather than stub
// the renderer, the build points it at a generated chambered test specimen
// (`tools/make_test_specimen.py`) whose shape exercises the same code paths:
// nested shells, interior geometry, Draco compression, multiple materials.
//
// The switch lives in vite.config.ts and is decided by what is on disk:
// the moment an acquired `.glb` lands in public/assets/, __MESH_STANDIN__
// becomes null and every specimen loads its own authored asset. Nothing in
// this directory changes when that happens.

import type { SpecimenRecord } from '../../studio/types'

export function resolveMeshUrl(specimen: SpecimenRecord): string {
  return __MESH_STANDIN__ ?? specimen.assets.mesh
}

/** True while the studio is running on the generated test mesh. Surfaced on
 * the stage container so a reviewer can never mistake the test form for an
 * acquired specimen. */
export function isStandIn(): boolean {
  return __MESH_STANDIN__ !== null
}
