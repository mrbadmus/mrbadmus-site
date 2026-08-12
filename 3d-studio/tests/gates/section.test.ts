// @vitest-environment node
// Gate 10 — the cross-section's geometry (MRB-189).
//
// The capped cut needs a stencil buffer and therefore a real GL context, so
// whether the cap is DRAWN is settled in `3d_render_check.py` check 8, in
// Chrome, by looking at pixels. What is settled here is everything about the
// cut that is arithmetic:
//
//   * where the plane sits for a slider position, and that the ends of the
//     travel mean "everything" and "nothing";
//   * that the cap quad COVERS the cut. The pixel check cannot own this one:
//     shrinking the quad to a quarter of its size still leaves a large, plainly
//     visible cut face, and the uncovered part of the cut shows the inside of
//     the far wall rather than the backdrop, so no pixel count separates the
//     two cleanly. Coverage is a property of two functions and eight box
//     corners, so it is asserted as one.
//   * that the hotspot layer's two questions get the right answers: an anchor
//     in the removed half is gone, and geometry in the removed half stops
//     occluding what the cut just exposed.
//
// The coverage assertion is not hypothetical. The first run of check 8 found a
// real void because `capTransform` centred the quad on the world origin, and
// the generated test specimen is deliberately modelled off-centre.

import { describe, expect, it } from 'vitest'
import * as THREE from 'three'
import {
  capSize,
  capTransform,
  isClipped,
  sectionConstant,
  sectionPlane,
  SECTION_AXIS,
  SECTION_REST,
} from '../../src/renderer/mesh/section'
import { isOccluded } from '../../src/renderer/mesh/project'

/** Deliberately off-centre and not cubic, like the generated test specimen. */
function offCentreBox(): THREE.Box3 {
  return new THREE.Box3(
    new THREE.Vector3(1.4, -0.9, -2.2),
    new THREE.Vector3(3.1, 2.6, 0.4),
  )
}

describe('gate 10 — where the plane sits', () => {
  const box = offCentreBox()

  it('the middle of the travel is the middle of the specimen', () => {
    const middle = sectionConstant(box, 0.5)
    const centre = (box.min[SECTION_AXIS] + box.max[SECTION_AXIS]) / 2
    expect(middle).toBeCloseTo(centre, 6)
  })

  it('one end removes everything and the other removes nothing', () => {
    const plane0 = sectionPlane(box, 0)
    const plane1 = sectionPlane(box, 1)
    const corners = boxCorners(box)
    expect(corners.every((c) => isClipped(c, plane0))).toBe(true)
    expect(corners.some((c) => isClipped(c, plane1))).toBe(false)
  })

  it('the travel is monotonic — dragging one way only ever removes more', () => {
    const constants = [0, 0.25, 0.5, 0.75, 1].map((o) => sectionConstant(box, o))
    for (let i = 1; i < constants.length; i += 1) {
      expect(constants[i]).toBeGreaterThan(constants[i - 1])
    }
  })

  it('a slider value outside 0–1 is clamped, not extrapolated', () => {
    expect(sectionConstant(box, -3)).toBe(sectionConstant(box, 0))
    expect(sectionConstant(box, 9)).toBe(sectionConstant(box, 1))
  })

  it('the cut is off by default — pressing the tool is what engages it', () => {
    expect(SECTION_REST.enabled).toBe(false)
  })
})

describe('gate 10 — the cap covers the cut', () => {
  /** Every corner of the specimen, projected onto the cut plane, must land
   * inside the cap quad. That is what "the cut is capped" means before any
   * pixel is drawn: if a corner falls outside, part of the cut face has no cap
   * over it and the room shows through. */
  function coverage(box: THREE.Box3, offset: number): number {
    const plane = sectionPlane(box, offset)
    const { position, quaternion } = capTransform(plane, box)
    const half = capSize(box) / 2
    const inverse = quaternion.clone().invert()

    let worst = 0
    for (const corner of boxCorners(box)) {
      const local = plane
        .projectPoint(corner, new THREE.Vector3())
        .sub(position)
        .applyQuaternion(inverse)
      worst = Math.max(worst, Math.abs(local.x) / half, Math.abs(local.y) / half)
    }
    return worst
  }

  it('covers an off-centre specimen at every position along the travel', () => {
    const box = offCentreBox()
    for (const offset of [0, 0.15, 0.35, 0.5, 0.65, 0.85, 1]) {
      expect(coverage(box, offset)).toBeLessThanOrEqual(1)
    }
  })

  it('covers a specimen modelled a long way from the origin', () => {
    const far = new THREE.Box3(
      new THREE.Vector3(40, 12, -8),
      new THREE.Vector3(46, 20, -1),
    )
    expect(coverage(far, 0.5)).toBeLessThanOrEqual(1)
  })

  it('covers a long thin specimen cut across its diagonal', () => {
    const thin = new THREE.Box3(
      new THREE.Vector3(-9, -0.4, -0.4),
      new THREE.Vector3(9, 0.4, 0.4),
    )
    expect(coverage(thin, 0.5)).toBeLessThanOrEqual(1)
  })

  it('the quad sits IN the plane, not merely near it', () => {
    const box = offCentreBox()
    const plane = sectionPlane(box, 0.4)
    const { position } = capTransform(plane, box)
    expect(Math.abs(plane.distanceToPoint(position))).toBeLessThan(1e-6)
  })
})

describe('gate 10 — what the cut does to the hotspot layer', () => {
  const CAMERA = new THREE.Vector3(0, 0, 6)

  /** A closed shell with a smaller closed form inside it. */
  function shellAndCore(): THREE.Object3D {
    const model = new THREE.Group()
    const shell = new THREE.Mesh(new THREE.SphereGeometry(1, 32, 24))
    const core = new THREE.Mesh(new THREE.SphereGeometry(0.3, 16, 12))
    model.add(shell, core)
    model.updateMatrixWorld(true)
    return model
  }

  it('an anchor in the removed half is clipped; one in the kept half is not', () => {
    const box = new THREE.Box3(new THREE.Vector3(-1, -1, -1), new THREE.Vector3(1, 1, 1))
    const plane = sectionPlane(box, 0.5)
    expect(isClipped(new THREE.Vector3(0, 0, 0.8), plane)).toBe(true)
    expect(isClipped(new THREE.Vector3(0, 0, -0.8), plane)).toBe(false)
  })

  it('with no plane, nothing is clipped', () => {
    expect(isClipped(new THREE.Vector3(0, 0, 99), null)).toBe(false)
  })

  it('the interior is occluded before the cut, and reachable after it', () => {
    const model = shellAndCore()
    const box = new THREE.Box3().setFromObject(model)
    const onTheCore = new THREE.Vector3(0, 0, 0.31)

    expect(isOccluded(onTheCore, CAMERA, model, 1, null)).toBe(true)

    // This is what "interior structures become reachable when the plane
    // exposes them" means, expressed as something that can be asserted: the
    // near wall is no longer between the camera and the core.
    const plane = sectionPlane(box, 0.5)
    expect(isOccluded(onTheCore, CAMERA, model, 1, plane)).toBe(false)
  })

  it('a cut that has not reached the near wall exposes nothing', () => {
    const model = shellAndCore()
    const box = new THREE.Box3().setFromObject(model)
    const onTheCore = new THREE.Vector3(0, 0, 0.31)
    // The plane is beyond the specimen: nothing is removed, so nothing is
    // exposed. A clip test that ignored the plane's POSITION would pass the
    // assertion above and fail this one.
    const plane = sectionPlane(box, 1)
    expect(isOccluded(onTheCore, CAMERA, model, 1, plane)).toBe(true)
  })
})

function boxCorners(box: THREE.Box3): THREE.Vector3[] {
  const out: THREE.Vector3[] = []
  for (const x of [box.min.x, box.max.x]) {
    for (const y of [box.min.y, box.max.y]) {
      for (const z of [box.min.z, box.max.z]) out.push(new THREE.Vector3(x, y, z))
    }
  }
  return out
}
