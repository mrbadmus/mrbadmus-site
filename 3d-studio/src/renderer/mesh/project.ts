// World anchor → container pixels, with honest occlusion.
//
// Stage 1's placeholder always reported visible: true, because it had no
// geometry to hide anything behind. This is where the contract's promise —
// "false when the hotspot is on the far side of the model" — becomes real.
//
// The test is a raycast, not a normal-facing dot product: a dot product only
// knows which way the surface under the anchor points, so it would keep
// showing an anchor that a nearer chamber wall or a fold of the outer shell
// has moved in front of. The raycast asks the only question that matters —
// is there geometry between the camera and this point.

import * as THREE from 'three'
import type { ScreenPoint } from '../types'
import { isShown } from './parts'
import { isClipped } from './section'

export interface ProjectionScene {
  camera: THREE.Camera
  /** the loaded specimen; everything that may occlude */
  model: THREE.Object3D
  /** container size in CSS pixels */
  width: number
  height: number
  /** bounding-sphere radius, used to scale the depth tolerance */
  radius: number
  /** the cross-section's clipping plane, when one is engaged (MRB-189).
   * Geometry the plane has taken away is not in front of anything. */
  clip?: THREE.Plane | null
}

/** How much nearer than the anchor a hit must be before it counts as
 * occluding, as a fraction of the specimen's radius. Anchors sit just off the
 * surface, so the surface they sit on must not read as occluding them. */
const DEPTH_TOLERANCE = 0.02

/** How far outside the frame an anchor may drift before it is called
 * invisible. The stage clips at its own edge; a little slack keeps dots from
 * flickering out exactly on the boundary. */
const NDC_LIMIT = 1.08

const _cameraPos = new THREE.Vector3()
const _toAnchor = new THREE.Vector3()
const _ndc = new THREE.Vector3()
const _view = new THREE.Vector3()
const _raycaster = new THREE.Raycaster()

export function projectAnchor(anchor: THREE.Vector3, scene: ProjectionScene): ScreenPoint {
  const { camera, model, width, height, radius, clip } = scene

  camera.updateMatrixWorld()
  camera.getWorldPosition(_cameraPos)

  // Behind the camera: project() would fold it back into frame at a mirrored
  // position, which is worse than saying nothing.
  _view.copy(anchor).applyMatrix4(camera.matrixWorldInverse)
  const behind = _view.z >= 0

  _ndc.copy(anchor).project(camera)
  const x = (_ndc.x * 0.5 + 0.5) * width
  const y = (-_ndc.y * 0.5 + 0.5) * height

  const inFrame =
    !behind &&
    Math.abs(_ndc.x) <= NDC_LIMIT &&
    Math.abs(_ndc.y) <= NDC_LIMIT &&
    _ndc.z <= 1

  const along = raysight(anchor, _cameraPos, model, radius, clip)

  return {
    x,
    y,
    visible: inFrame && !along.occluded,
    onCut: inFrame && !along.occluded && along.throughCut,
  }
}

/** What the ray from the camera to the anchor met on the way.
 *
 * `occluded` is the original question: does solid geometry sit in front.
 *
 * `throughCut` is the other one, and it comes free from the same raycast
 * (MRB-189, §08). If the ray passed through geometry the plane took away, then
 * the cap — which is drawn exactly where the stencil says the plane removed
 * material in front of what survived — covers this pixel. So the dot is not on
 * the specimen's shaded exterior at all; it is on the cut face, which is a
 * LIGHT ground (`#F0E9DC`) inside a dark stage. Design's ruling is that such a
 * dot flips to the §07 paper variant, dark outline and all, and this is the
 * only honest way to know: the shell cannot see canvas pixels, and the
 * anchor's distance to the plane would be a guess about geometry rather than a
 * measurement of what is in front of it.
 */
export function raysight(
  anchor: THREE.Vector3,
  cameraPos: THREE.Vector3,
  model: THREE.Object3D,
  radius: number,
  clip: THREE.Plane | null = null,
): { occluded: boolean; throughCut: boolean } {
  _toAnchor.copy(anchor).sub(cameraPos)
  const distance = _toAnchor.length()
  if (distance === 0) return { occluded: false, throughCut: false }

  const tolerance = Math.max(radius * DEPTH_TOLERANCE, 1e-4)
  _raycaster.set(cameraPos, _toAnchor.divideScalar(distance))
  _raycaster.near = 0
  // Nothing beyond the anchor can be in front of it.
  _raycaster.far = distance - tolerance
  if (_raycaster.far <= 0) return { occluded: false, throughCut: false }

  // three's raycaster does not consult Object3D.visible — it tests layers and
  // nothing else — so a part that isolate or layers has switched off would
  // keep occluding the dots behind it, and a structure the student asked to
  // see alone would be labelled through a form that is no longer drawn
  // (MRB-188).
  // Two things a raycast against the raw scene graph gets wrong once the tools
  // exist. three's raycaster does not consult Object3D.visible — it tests
  // layers and nothing else — so a part isolate or layers switched off would
  // keep occluding the dots behind it (MRB-188). And it knows nothing about
  // clipping planes, so the half of the specimen the cross-section has taken
  // away would keep occluding what the cut just exposed (MRB-189).
  const hits = _raycaster.intersectObject(model, true)
  let occluded = false
  let throughCut = false
  for (const hit of hits) {
    if (!isShown(hit.object, model)) continue
    if (isClipped(hit.point, clip)) throughCut = true
    else occluded = true
  }
  return { occluded, throughCut }
}

/** True when solid geometry sits between the camera and the anchor. Kept as
 * its own name because that is the question `occlusion.test.ts` asks and the
 * one the contract's `visible` is defined by. */
export function isOccluded(
  anchor: THREE.Vector3,
  cameraPos: THREE.Vector3,
  model: THREE.Object3D,
  radius: number,
  clip: THREE.Plane | null = null,
): boolean {
  return raysight(anchor, cameraPos, model, radius, clip).occluded
}
