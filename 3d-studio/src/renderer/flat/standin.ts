// Which plate the flat renderer actually fetches — the exact counterpart of
// `mesh/standin.ts`, and for the exact same reason.
//
// `assets.fallback` in content/heart.json is a Stage-8 TODO: no diagram has
// been drawn. While no acquired `.svg` is on disk the build points the flat
// renderer at a generated fixture (`tools/make_test_plate.py`) that carries no
// anatomy and says so on its face. Drop a real diagram into public/assets/ and
// __PLATE_STANDIN__ becomes null on the next build. Nothing in this directory
// changes when that happens.

import type { SpecimenRecord } from '../../studio/types'

export function resolvePlateUrl(specimen: SpecimenRecord): string {
  return __PLATE_STANDIN__ ?? specimen.assets.fallback
}

/** True while the studio is running on the generated test plate. Surfaced on
 * the stage container so a reviewer can never mistake the fixture for an
 * authored diagram. */
export function isPlateStandIn(): boolean {
  return __PLATE_STANDIN__ !== null
}
