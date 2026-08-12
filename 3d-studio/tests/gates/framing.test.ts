// @vitest-environment node
// Gate 13 — the retrieval round frames its target before asking (MRB-191).
//
// The ruling names two properties and this file owns both, because both are
// arithmetic:
//
//   * FRAME, DON'T ZOOM IN. The camera ends the move exactly as far from the
//     specimen as it began. Filling the frame with the target would remove the
//     surrounding structure, which is the thing that makes the question
//     answerable at all.
//   * ANIMATE, DON'T CUT. The move passes through intermediate positions, all
//     of them at the same distance — a straight lerp between two points on a
//     sphere dips towards the model and reads as a lunge.
//
// The third property — that the target dot is actually on screen when the
// prompt appears — needs a camera, a raycaster and a real scene, so it is
// asserted alongside them here against synthetic geometry, and in a real
// browser in `3d_render_check.py` check 10.

import { describe, expect, it } from 'vitest'
import * as THREE from 'three'
import {
  easeInOut,
  framePosition,
  frameStep,
  needsFraming,
} from '../../src/renderer/mesh/framing'
import { projectAnchor } from '../../src/renderer/mesh/project'

const TARGET = new THREE.Vector3(0, 0, 0)
const CAMERA = new THREE.Vector3(0, 0, 5)

describe('gate 13 — frame, do not zoom in', () => {
  it('ends the move at exactly the distance it started', () => {
    for (const anchor of [
      new THREE.Vector3(0, 0, -1),
      new THREE.Vector3(1, 0, 0),
      new THREE.Vector3(-0.3, 0.9, -0.2),
    ]) {
      const to = framePosition(anchor, TARGET, CAMERA)!
      expect(to.distanceTo(TARGET)).toBeCloseTo(CAMERA.distanceTo(TARGET), 9)
    }
  })

  it('holds the distance at EVERY step of the move, not just the ends', () => {
    const anchor = new THREE.Vector3(0, 0, -1)
    const to = framePosition(anchor, TARGET, CAMERA)!
    for (let t = 0; t <= 1.0001; t += 0.1) {
      const at = frameStep(CAMERA, to, TARGET, t)
      expect(at.distanceTo(TARGET)).toBeCloseTo(5, 6)
    }
  })

  it('puts the camera on the anchor’s own side of the specimen', () => {
    const anchor = new THREE.Vector3(0, 0, -1)
    const to = framePosition(anchor, TARGET, CAMERA)!
    // same direction from the centre as the anchor
    expect(to.clone().normalize().dot(anchor.clone().normalize())).toBeCloseTo(1, 6)
  })

  it('an anchor at the orbit centre has no outward side, and is left alone', () => {
    expect(framePosition(TARGET.clone(), TARGET, CAMERA)).toBeNull()
    expect(needsFraming(TARGET.clone(), TARGET, CAMERA)).toBe(false)
  })
})

describe('gate 13 — animate, do not cut', () => {
  it('the move passes through positions that are neither end', () => {
    const anchor = new THREE.Vector3(0, 0, -1)
    const to = framePosition(anchor, TARGET, CAMERA)!
    const middle = frameStep(CAMERA, to, TARGET, 0.5)
    expect(middle.distanceTo(CAMERA)).toBeGreaterThan(0.1)
    expect(middle.distanceTo(to)).toBeGreaterThan(0.1)
  })

  it('the easing starts and ends at rest', () => {
    expect(easeInOut(0)).toBe(0)
    expect(easeInOut(1)).toBe(1)
    // slower at the ends than in the middle: a move that starts abruptly
    // reads as a cut even when it takes half a second
    expect(easeInOut(0.1)).toBeLessThan(0.1)
    expect(easeInOut(0.9)).toBeGreaterThan(0.9)
  })

  it('the move is monotonic — it never doubles back', () => {
    const anchor = new THREE.Vector3(1, 0, 0)
    const to = framePosition(anchor, TARGET, CAMERA)!
    let last = 0
    for (let t = 0; t <= 1.0001; t += 0.05) {
      const travelled = frameStep(CAMERA, to, TARGET, t).distanceTo(CAMERA)
      expect(travelled).toBeGreaterThanOrEqual(last - 1e-9)
      last = travelled
    }
  })

  it('a camera already facing the target is not moved at all', () => {
    const anchor = new THREE.Vector3(0, 0, 1)
    expect(needsFraming(anchor, TARGET, CAMERA)).toBe(false)
  })

  it('a target on the far side IS moved', () => {
    expect(needsFraming(new THREE.Vector3(0, 0, -1), TARGET, CAMERA)).toBe(true)
  })

  it('two opposed directions still produce a turn, not a jump', () => {
    // The degenerate great-circle case: no unique arc, and a naive
    // implementation returns NaN or teleports.
    const to = framePosition(new THREE.Vector3(0, 0, -1), TARGET, CAMERA)!
    const middle = frameStep(CAMERA, to, TARGET, 0.5)
    expect(Number.isFinite(middle.x)).toBe(true)
    expect(middle.distanceTo(TARGET)).toBeCloseTo(5, 6)
    expect(middle.distanceTo(CAMERA)).toBeGreaterThan(0.5)
  })
})

describe('gate 13 — after framing, the target is genuinely visible', () => {
  /** A closed form, so an anchor on the far side is really hidden. */
  function form(): THREE.Object3D {
    const model = new THREE.Group()
    model.add(new THREE.Mesh(new THREE.SphereGeometry(1, 32, 24)))
    model.updateMatrixWorld(true)
    return model
  }

  function camera(at: THREE.Vector3): THREE.PerspectiveCamera {
    const c = new THREE.PerspectiveCamera(38, 800 / 600, 0.01, 100)
    c.position.copy(at)
    c.lookAt(TARGET)
    c.updateMatrixWorld(true)
    c.updateProjectionMatrix()
    return c
  }

  it('a far-side anchor is invisible before, and visible after', () => {
    const model = form()
    const anchor = new THREE.Vector3(0, 0, -1.005)

    const before = projectAnchor(anchor, {
      camera: camera(CAMERA), model, width: 800, height: 600, radius: 1,
    })
    expect(before.visible).toBe(false)

    const to = framePosition(anchor, TARGET, CAMERA)!
    const after = projectAnchor(anchor, {
      camera: camera(to), model, width: 800, height: 600, radius: 1,
    })
    expect(after.visible).toBe(true)
    // and ON the stage, not off its edge
    expect(after.x).toBeGreaterThan(0)
    expect(after.x).toBeLessThan(800)
    expect(after.y).toBeGreaterThan(0)
    expect(after.y).toBeLessThan(600)
  })

  it('the specimen still fills a similar share of the frame — framed, not zoomed', () => {
    const anchor = new THREE.Vector3(0, 0, -1.005)
    const to = framePosition(anchor, TARGET, CAMERA)!

    // The silhouette's angular radius depends only on distance, and the
    // distance did not change.
    const beforeAngle = Math.asin(1 / CAMERA.distanceTo(TARGET))
    const afterAngle = Math.asin(1 / to.distanceTo(TARGET))
    expect(afterAngle).toBeCloseTo(beforeAngle, 9)
  })
})
