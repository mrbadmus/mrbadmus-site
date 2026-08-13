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
import { RULE_EDGE_ON_FLOOR, type SectionRule } from '../types'

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

/** Where to draw the accent rule that marks the plane (§08 of the
 * cross-section reference), or null when drawing one would be a lie.
 *
 * §08 takes the accent off the tissue and gives it to the plane: "It marks the
 * plane — the rule through the specimen, its end ticks, and the slider being
 * dragged — because the plane is the interactive thing." The reference draws
 * that rule as a vertical line at the boundary between the shaded exterior and
 * the cut face, which is what an edge-on plane looks like.
 *
 * A plane is only a LINE on screen when it is seen edge-on. Seen face-on it
 * covers the whole frame and has no position to mark, and the section axis is
 * Z — chosen at Stage 4 so the cut face is the thing the student is looking at
 * rather than something they must turn the specimen to find — so at the
 * default camera it is exactly face-on. Which means the reference's own
 * picture (cut face fully visible AND plane edge-on) cannot be drawn in three
 * dimensions at all; a 2D mock can hold both at once and a projection cannot.
 *
 * So the rule is drawn where it is true and not where it is not: it appears as
 * the student turns the specimen, which is the same gesture that makes the
 * plane's position legible in the first place, and it is absent head-on rather
 * than being a decoration at a made-up angle. The other three drag emphases
 * (§09: handle, hatched travel, promoted readout) are unconditional, so the
 * drag never has nothing to say.
 */
export function sectionRule(
  plane: THREE.Plane,
  box: THREE.Box3,
  camera: THREE.Camera,
  width: number,
  height: number,
): SectionRule | null {
  if (!width || !height) return null

  const centre = plane.projectPoint(
    box.getCenter(new THREE.Vector3()),
    new THREE.Vector3(),
  )

  // The normal in the camera's own frame. Its x/y span is how much of the
  // normal lies ACROSS the screen rather than into it, which is exactly how
  // edge-on the plane is.
  const nv = plane.normal.clone().transformDirection(camera.matrixWorldInverse)
  const edgeOn = Math.min(Math.hypot(nv.x, nv.y), 1)
  if (edgeOn < RULE_EDGE_ON_FLOOR) return null

  // Screen y runs down, view y runs up.
  const screenNormal = new THREE.Vector2(nv.x, -nv.y).normalize()
  // The plane's edge on screen is perpendicular to its normal on screen.
  const along = new THREE.Vector2(-screenNormal.y, screenNormal.x)

  const ndc = centre.clone().project(camera)
  const x = (ndc.x * 0.5 + 0.5) * width
  const y = (-ndc.y * 0.5 + 0.5) * height

  // How many pixels the specimen spans ALONG THE RULE, measured rather than
  // guessed: the bounding box's own half-width in that direction — its support
  // function — projected the same way the centre was.
  //
  // The bounding SPHERE's radius was the first version of this and drew a rule
  // half again too long on the heart, which is taller than it is wide: a
  // sphere is the worst case in every direction at once, and the rule only
  // needs to cross the specimen in one.
  const alongWorld = new THREE.Vector3(along.x, -along.y, 0).transformDirection(
    camera.matrixWorld,
  )
  const half = box.getSize(new THREE.Vector3()).multiplyScalar(0.5)
  const reach =
    Math.abs(half.x * alongWorld.x) +
    Math.abs(half.y * alongWorld.y) +
    Math.abs(half.z * alongWorld.z)
  const edge = centre.clone().addScaledVector(alongWorld, reach).project(camera)
  const length =
    2 * Math.hypot(((edge.x - ndc.x) * 0.5) * width, ((edge.y - ndc.y) * 0.5) * height)

  // CSS rotate() takes the element's own down-axis (0,1) to (−sin θ, cos θ).
  const angle = (Math.atan2(-along.x, along.y) * 180) / Math.PI

  return { x, y, angle, length, edgeOn }
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
