// Cross-section — the clipping plane's geometry (MRB-189, Stage 4).
//
// Kept out of the scene component so it can be asserted without a browser: the
// plane, where the plane sits for a given slider position, and the two
// questions the hotspot layer asks of it. The capping itself needs a stencil
// buffer and therefore a real GL context, and is tested in
// `3d_render_check.py`.
//
// SIGN CONVENTION, once, because everything below depends on it: a THREE.Plane
// keeps geometry where `distanceToPoint(p) >= 0` and clips it away where that
// is negative. So the normal points INTO the half that survives.

import * as THREE from 'three'

export type SectionAxis = 'x' | 'y' | 'z'

export interface SectionState {
  enabled: boolean
  /** 0 → the plane sits at the near end of the axis (almost everything
   * removed); 1 → at the far end (nothing removed). */
  offset: number
}

/** The axis the cut runs along.
 *
 * Z, removing the half nearest the default camera, so the cut face is the
 * thing the student is looking at rather than something they have to turn the
 * specimen to find. Spec §4 says "a draggable plane position along a chosen
 * axis" — the axis is chosen here, at build time, and the position is the
 * student's. An axis picker was deliberately not built: it is UI the frozen
 * reference does not draw, and one legible cut beats three the class has to
 * choose between. Revisit if a specimen arrives whose teaching cut is not
 * coronal.
 */
export const SECTION_AXIS: SectionAxis = 'z'

/** Straight through the middle: the first press should show a section, not an
 * edge case at one end of the travel. */
export const SECTION_REST: SectionState = { enabled: false, offset: 0.5 }

const AXIS_NORMAL: Record<SectionAxis, THREE.Vector3> = {
  x: new THREE.Vector3(-1, 0, 0),
  y: new THREE.Vector3(0, -1, 0),
  z: new THREE.Vector3(0, 0, -1),
}

/** Where along the axis the cut sits, in world units, for a slider position.
 * A hair of margin at each end so offset 0 and 1 are "everything removed" and
 * "nothing removed" rather than degenerate exact-tangent planes. */
export function sectionConstant(
  box: THREE.Box3,
  offset: number,
  axis: SectionAxis = SECTION_AXIS,
): number {
  const min = box.min[axis]
  const max = box.max[axis]
  const margin = (max - min) * 0.02
  const low = min - margin
  const high = max + margin
  return low + THREE.MathUtils.clamp(offset, 0, 1) * (high - low)
}

/** The world-space clipping plane for a slider position. */
export function sectionPlane(
  box: THREE.Box3,
  offset: number,
  axis: SectionAxis = SECTION_AXIS,
): THREE.Plane {
  return new THREE.Plane(AXIS_NORMAL[axis].clone(), sectionConstant(box, offset, axis))
}

/** True when the point is in the half the plane has taken away.
 *
 * The hotspot layer asks this twice per anchor and for a different reason each
 * time: an anchor in the removed half is a label on material that is no longer
 * there, and a raycast hit in the removed half is geometry that is no longer
 * in front of anything. Both were wrong before the plane existed, and both
 * would be silently wrong if this returned false. */
export function isClipped(point: THREE.Vector3, plane: THREE.Plane | null): boolean {
  if (!plane) return false
  return plane.distanceToPoint(point) < 0
}

/** How wide a cap has to be to cover any cut through this specimen: the
 * bounding box's full diagonal, with headroom. The diagonal rather than the
 * sphere's diameter because the quad is square and axis-aligned to the plane,
 * so a cut across a long specimen's corner is the worst case. */
export function capSize(box: THREE.Box3): number {
  const diagonal = box.getSize(new THREE.Vector3()).length()
  return Math.max(diagonal, 1e-3) * 1.3
}

/** Position and orientation for the cap quad: sitting in the plane, centred
 * over the specimen, facing back along the normal so it is drawn towards the
 * camera side of the cut.
 *
 * Centred over the SPECIMEN, not over the world origin. A specimen modelled
 * off-centre — which the generated test one deliberately is, and which a
 * bought asset has no obligation not to be — would otherwise have part of its
 * cut face fall outside the quad and show the room through it. Found by the
 * void probe in `3d_render_check.py` check 8 on its first run, against a
 * version of this function that used `normal * -constant` and nothing else.
 */
export function capTransform(
  plane: THREE.Plane,
  box: THREE.Box3,
): { position: THREE.Vector3; quaternion: THREE.Quaternion } {
  const position = plane.projectPoint(
    box.getCenter(new THREE.Vector3()),
    new THREE.Vector3(),
  )
  const quaternion = new THREE.Quaternion().setFromUnitVectors(
    new THREE.Vector3(0, 0, 1),
    plane.normal.clone().negate(),
  )
  return { position, quaternion }
}
