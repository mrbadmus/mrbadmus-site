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

export interface ProjectionScene {
  camera: THREE.Camera
  /** the loaded specimen; everything that may occlude */
  model: THREE.Object3D
  /** container size in CSS pixels */
  width: number
  height: number
  /** bounding-sphere radius, used to scale the depth tolerance */
  radius: number
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
  const { camera, model, width, height, radius } = scene

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

  return {
    x,
    y,
    visible: inFrame && !isOccluded(anchor, _cameraPos, model, radius),
  }
}

/** True when solid geometry sits between the camera and the anchor. */
export function isOccluded(
  anchor: THREE.Vector3,
  cameraPos: THREE.Vector3,
  model: THREE.Object3D,
  radius: number,
): boolean {
  _toAnchor.copy(anchor).sub(cameraPos)
  const distance = _toAnchor.length()
  if (distance === 0) return false

  const tolerance = Math.max(radius * DEPTH_TOLERANCE, 1e-4)
  _raycaster.set(cameraPos, _toAnchor.divideScalar(distance))
  _raycaster.near = 0
  // Nothing beyond the anchor can be in front of it.
  _raycaster.far = distance - tolerance
  if (_raycaster.far <= 0) return false

  const hits = _raycaster.intersectObject(model, true)
  return hits.length > 0
}
