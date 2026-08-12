// Framing and hotspot anchors — the geometry the shell's dots hang off.
//
// Two jobs, both pure enough to test without a browser:
//
//   1. frameSpecimen — the authored default view. Reset must return here
//      EXACTLY (MRB-187 acceptance), so it is computed once from the model's
//      bounds and then never recomputed.
//
//   2. resolveAnchors — a world-space point per hotspot id. Content authors
//      real `position3d` values at Stage 8; until then every hotspot in
//      heart.json is [0, 0, 0], which as a literal anchor would sit at the
//      model's origin — inside the mesh, and therefore permanently occluded
//      once occlusion is honest. So an all-zero position is read as "not yet
//      authored" and a stand-in anchor is derived instead: spread across the
//      hemisphere the default camera faces, then snapped onto the mesh
//      surface by raycast. All of them are visible at the default view (which
//      is what the frozen reference draws and what the parity gate counts),
//      and rotating the specimen genuinely hides the ones that turn away.

import * as THREE from 'three'
import type { HotspotRecord } from '../../studio/types'

export interface DefaultView {
  position: THREE.Vector3
  target: THREE.Vector3
  /** bounding-sphere radius of the specimen, in world units */
  radius: number
}

/** Vertical field of view the stage camera is built with. */
export const FOV = 38

/** Where the camera sits relative to the specimen at the default view:
 * slightly right of centre and a little above, matching the frozen
 * reference's three-quarter presentation of the form. */
const DEFAULT_AZIMUTH = THREE.MathUtils.degToRad(22)
const DEFAULT_ELEVATION = THREE.MathUtils.degToRad(14)
/** Headroom around the bounding sphere so the specimen never touches the
 * stage edge — the rail and the quality chip both overhang the stage. */
const FRAMING_MARGIN = 1.42

/** The authored default view for a loaded model. Deterministic: the same
 * model always frames identically, which is what makes reset exact. */
export function frameSpecimen(object: THREE.Object3D, aspect = 16 / 9): DefaultView {
  const box = new THREE.Box3().setFromObject(object)
  const sphere = box.getBoundingSphere(new THREE.Sphere())
  const radius = sphere.radius > 0 ? sphere.radius : 1

  // Fit the sphere in the tighter of the two axes: on a portrait-ish stage
  // the horizontal field is the binding one.
  const vFov = THREE.MathUtils.degToRad(FOV)
  const hFov = 2 * Math.atan(Math.tan(vFov / 2) * Math.max(aspect, 0.2))
  const fit = Math.min(vFov, hFov)
  const distance = (radius / Math.sin(fit / 2)) * FRAMING_MARGIN

  const target = sphere.center.clone()
  const position = target
    .clone()
    .add(
      new THREE.Vector3(
        Math.sin(DEFAULT_AZIMUTH) * Math.cos(DEFAULT_ELEVATION),
        Math.sin(DEFAULT_ELEVATION),
        Math.cos(DEFAULT_AZIMUTH) * Math.cos(DEFAULT_ELEVATION),
      ).multiplyScalar(distance),
    )

  return { position, target, radius }
}

/** An all-zero position3d is the unauthored sentinel (see the file header),
 * not a genuine anchor at the model's origin. */
export function isAuthoredPosition(p: readonly number[]): boolean {
  return p.length === 3 && p.some((v) => v !== 0)
}

/** Golden-angle spread over the hemisphere the camera faces. Deterministic in
 * the hotspot's index, so a given specimen always gets the same stand-ins. */
const GOLDEN_ANGLE = Math.PI * (3 - Math.sqrt(5))
const MIN_OFF_AXIS = THREE.MathUtils.degToRad(18)
const MAX_OFF_AXIS = THREE.MathUtils.degToRad(52)

export function standInDirection(index: number, count: number, view: DefaultView): THREE.Vector3 {
  const toCamera = view.position.clone().sub(view.target).normalize()
  // An up vector that is never parallel to toCamera.
  const seed = Math.abs(toCamera.y) > 0.9 ? new THREE.Vector3(0, 0, 1) : new THREE.Vector3(0, 1, 0)
  const right = new THREE.Vector3().crossVectors(seed, toCamera).normalize()
  const up = new THREE.Vector3().crossVectors(toCamera, right).normalize()

  const spread = count > 1 ? index / (count - 1) : 0
  const theta = MIN_OFF_AXIS + spread * (MAX_OFF_AXIS - MIN_OFF_AXIS)
  const phi = index * GOLDEN_ANGLE

  return toCamera
    .clone()
    .multiplyScalar(Math.cos(theta))
    .addScaledVector(right, Math.sin(theta) * Math.cos(phi))
    .addScaledVector(up, Math.sin(theta) * Math.sin(phi))
    .normalize()
}

/** Push a surface anchor this far out along the surface normal so the
 * occlusion test does not read the surface it sits on as the thing occluding
 * it. A fraction of the specimen's own size, so it scales with the model. */
const SURFACE_LIFT = 0.006

/** World-space anchor per hotspot id. Authored coordinates win; unauthored
 * ones get a stand-in on the mesh surface. */
export function resolveAnchors(
  hotspots: readonly HotspotRecord[],
  model: THREE.Object3D,
  view: DefaultView,
): Map<string, THREE.Vector3> {
  const anchors = new Map<string, THREE.Vector3>()
  const raycaster = new THREE.Raycaster()
  model.updateMatrixWorld(true)

  hotspots.forEach((hotspot, index) => {
    if (isAuthoredPosition(hotspot.position3d)) {
      const local = new THREE.Vector3().fromArray(hotspot.position3d)
      anchors.set(hotspot.id, local.applyMatrix4(model.matrixWorld))
      return
    }

    const direction = standInDirection(index, hotspots.length, view)
    const origin = view.target.clone().addScaledVector(direction, view.radius * 4)
    raycaster.set(origin, direction.clone().negate())
    const hit = raycaster.intersectObject(model, true)[0]

    if (hit) {
      const normal = hit.face
        ? hit.face.normal.clone().transformDirection(hit.object.matrixWorld)
        : direction.clone()
      anchors.set(
        hotspot.id,
        hit.point.clone().addScaledVector(normal, view.radius * SURFACE_LIFT),
      )
    } else {
      // No geometry along that ray (a very concave model). Sit on the
      // bounding sphere instead — still outside the form, still deterministic.
      anchors.set(hotspot.id, view.target.clone().addScaledVector(direction, view.radius))
    }
  })

  return anchors
}
