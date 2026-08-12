// Turning the specimen to face a hotspot (MRB-191, Stage 6).
//
// Pure geometry, so the two properties the ruling actually names can be
// asserted without a browser:
//
//   * FRAME, DON'T ZOOM IN — the camera ends the move exactly as far from the
//     specimen as it started. The surrounding structure is what makes the
//     question answerable.
//   * the anchor ends up FACING the camera, which is what makes the pulsing
//     52px marker be on screen when the prompt appears.
//
// The animation itself — easing the camera from where it is to where this says
// it should be — lives in the renderer, because it needs a frame loop.

import * as THREE from 'three'

/** How long the turn takes. Long enough to read as a turn rather than a jump,
 * short enough not to be waited on. The controls damp at 0.075, so this is in
 * the same register as a released drag. */
export const FRAME_DURATION_MS = 620

/** Ease in and out: a move that starts and stops abruptly reads as a cut even
 * when it takes half a second. */
export function easeInOut(t: number): number {
  const x = THREE.MathUtils.clamp(t, 0, 1)
  return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2
}

/**
 * Where the camera should end up so that `anchor` faces it.
 *
 * The direction is the anchor's own outward direction from the point the
 * camera orbits, which for a surface anchor is the direction its material
 * faces. The DISTANCE is copied from where the camera already is, so the move
 * is a rotation about the target and nothing else.
 *
 * Returns null when there is no meaningful direction — an anchor sitting
 * exactly on the orbit target has no outward side, and turning to face it
 * would mean picking one arbitrarily.
 */
export function framePosition(
  anchor: THREE.Vector3,
  target: THREE.Vector3,
  camera: THREE.Vector3,
): THREE.Vector3 | null {
  const outward = anchor.clone().sub(target)
  if (outward.lengthSq() < 1e-12) return null

  const distance = camera.distanceTo(target)
  if (distance < 1e-9) return null

  return target.clone().addScaledVector(outward.normalize(), distance)
}

/**
 * Is this anchor already facing the camera closely enough to leave alone?
 *
 * The ruling is explicit that framing happens when a question is presented,
 * not continuously, and a move of two degrees is a twitch rather than a turn.
 * Answered as the angle between where the camera is and where it would go.
 */
export function needsFraming(
  anchor: THREE.Vector3,
  target: THREE.Vector3,
  camera: THREE.Vector3,
  toleranceDegrees = 24,
): boolean {
  const wanted = framePosition(anchor, target, camera)
  if (!wanted) return false
  const from = camera.clone().sub(target).normalize()
  const to = wanted.clone().sub(target).normalize()
  const angle = Math.acos(THREE.MathUtils.clamp(from.dot(to), -1, 1))
  return THREE.MathUtils.radToDeg(angle) > toleranceDegrees
}

/** One step of the move, as an absolute camera position.
 *
 * Interpolated on the SPHERE rather than through it: a straight line between
 * two points at the same distance passes closer to the specimen, so a linear
 * lerp would dip towards the model mid-turn and read as a lunge.
 */
export function frameStep(
  from: THREE.Vector3,
  to: THREE.Vector3,
  target: THREE.Vector3,
  t: number,
): THREE.Vector3 {
  const a = from.clone().sub(target)
  const b = to.clone().sub(target)
  const radius = a.length()
  const eased = easeInOut(t)

  const fromDir = a.clone().normalize()
  const toDir = b.clone().normalize()
  const dot = THREE.MathUtils.clamp(fromDir.dot(toDir), -1, 1)
  const angle = Math.acos(dot)

  if (angle < 1e-6) return to.clone()

  // Great-circle interpolation. The degenerate case — exactly opposite
  // directions — has no unique arc, so any perpendicular axis will do and the
  // move is still a turn rather than a jump.
  let axis = new THREE.Vector3().crossVectors(fromDir, toDir)
  if (axis.lengthSq() < 1e-12) {
    const seed =
      Math.abs(fromDir.y) > 0.9 ? new THREE.Vector3(1, 0, 0) : new THREE.Vector3(0, 1, 0)
    axis = new THREE.Vector3().crossVectors(fromDir, seed)
  }
  axis.normalize()

  const rotated = fromDir
    .clone()
    .applyAxisAngle(axis, angle * eased)
    .multiplyScalar(radius)
  return target.clone().add(rotated)
}
