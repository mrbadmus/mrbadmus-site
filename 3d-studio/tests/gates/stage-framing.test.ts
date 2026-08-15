// @vitest-environment node
// Gate 14 — the specimen is framed where a student can SEE it (MRB-216).
//
// A sibling of framing.test.ts rather than an addition to it: that file owns
// the retrieval round's turn-to-face, which is about WHERE THE CAMERA GOES.
// This one is about WHICH PART OF THE STAGE the camera frames into, which is a
// different property with a different failure.
//
// The defect: on phone the §05 sheet is drawn over the lower part of the stage
// — 55% of it at rest, all but 150px raised — while the camera framed against
// the geometric centre of the canvas. So the specimen sat half behind the
// sheet, and a retrieval target that framePosition had just turned to face the
// camera could land underneath it entirely. That is not a hard question, it is
// an unanswerable one, and it is indistinguishable from the app being broken.
//
// The assertions are made against REAL three cameras, not against the offset
// arithmetic restated — a test that recomputed the formula it is checking would
// pass on a sign error in setViewOffset's argument order, which is exactly the
// mistake available here.

import { describe, expect, it } from 'vitest'
import * as THREE from 'three'
import { FOV } from '../../src/renderer/mesh/anchors'
import {
  axisPoint,
  magnification,
  stageViewOffset,
  type ViewOffset,
} from '../../src/renderer/mesh/viewport'
import { NO_STAGE_INSETS } from '../../src/renderer/types'

/** The covered strip at each detent.
 *
 * The sheet is `height: 55%` at rest and `calc(100% - 150px)` raised, of the
 * stagewrap the stage fills — but the sheet is not all of it. On phone the tool
 * rail turns horizontal (§05) and sits on the sheet's top edge, with the hint
 * line above that, so the band the shell actually takes is their union. The
 * shell measures it; these are the same quantity, modelled, so the cases below
 * are the ones the app really produces.
 *
 * Both are exercised: sheet-only is the lower bound and was the first cut of
 * this fix, and it is kept as a case because the arithmetic must hold for any
 * covered height, not only the two the current stylesheet happens to produce. */
const RAIL_BAND = 54 + 20 // .rail is 54px; .stagehint rides ~20px above it
const REST = (h: number) => h * 0.55
const RAISED = (h: number) => h - 150
const WITH_FURNITURE = (covered: number) => covered + RAIL_BAND

const PHONE = { width: 390, height: 780 }
const TABLET = { width: 834, height: 780 }
const DESKTOP = { width: 1440, height: 900 }

/** A camera aimed at the origin the way the stage's is once a specimen has
 * been framed: orbit target at the centre, camera pulled back off it. */
function camera(width: number, height: number, offset: ViewOffset | null) {
  const cam = new THREE.PerspectiveCamera(FOV, width / height, 0.1, 100)
  cam.position.set(0, 0, 5)
  cam.lookAt(0, 0, 0)
  if (offset) {
    cam.setViewOffset(
      offset.fullWidth,
      offset.fullHeight,
      offset.offsetX,
      offset.offsetY,
      offset.width,
      offset.height,
    )
  }
  cam.updateMatrixWorld(true)
  return cam
}

/** Where a world point lands, in container pixels. */
function project(cam: THREE.Camera, v: THREE.Vector3, width: number, height: number) {
  const p = v.clone().project(cam)
  return { x: ((p.x + 1) / 2) * width, y: ((1 - p.y) / 2) * height }
}

/** The world radius `frameSpecimen` would have chosen for a specimen at this
 * distance and this canvas.
 *
 * It fits the bounding sphere into the TIGHTER of the two fields with a 1.42
 * margin — which on a portrait phone stage is the HORIZONTAL one, not the
 * vertical. Getting that wrong models a specimen far larger than the app ever
 * frames, and this test did exactly that on its first run. */
function framedRadius(distance: number, width: number, height: number): number {
  const vFov = THREE.MathUtils.degToRad(FOV)
  const hFov = 2 * Math.atan(Math.tan(vFov / 2) * Math.max(width / height, 0.2))
  const fit = Math.min(vFov, hFov)
  return (distance * Math.sin(fit / 2)) / 1.42
}

/** The vertical extent the specimen actually occupies on the glass, in
 * container pixels.
 *
 * Measured by projecting a dense sample of the sphere's SURFACE and taking the
 * outermost, rather than by projecting the two poles: under perspective the
 * silhouette of a sphere is wider than its poles, so the pole pair understates
 * it — which would make a "does it fit" assertion optimistic in exactly the
 * direction that matters. Sampling has no such lean and needs no trigonometry
 * that could repeat a mistake in the code under test. */
function extent(cam: THREE.Camera, radius: number, width: number, height: number) {
  const GOLDEN = Math.PI * (3 - Math.sqrt(5))
  let top = Infinity
  let bottom = -Infinity
  const n = 4000
  for (let i = 0; i < n; i += 1) {
    const y = 1 - (2 * i) / (n - 1)
    const r = Math.sqrt(Math.max(0, 1 - y * y))
    const theta = i * GOLDEN
    const p = project(
      cam,
      new THREE.Vector3(Math.cos(theta) * r, y, Math.sin(theta) * r).multiplyScalar(radius),
      width,
      height,
    )
    if (p.y < top) top = p.y
    if (p.y > bottom) bottom = p.y
  }
  return { top, bottom }
}

describe('gate 14 — desktop and tablet are untouched', () => {
  for (const [name, box] of [
    ['desktop', DESKTOP],
    ['tablet', TABLET],
  ] as const) {
    it(`${name} takes no view offset at all`, () => {
      expect(stageViewOffset(box.width, box.height, NO_STAGE_INSETS)).toBeNull()
    })

    it(`${name} projects a point exactly as an untouched camera does`, () => {
      // Not "approximately": with no offset the projection matrix is the one
      // that shipped, so this is an equality.
      const offset = stageViewOffset(box.width, box.height, NO_STAGE_INSETS)
      const withOffset = camera(box.width, box.height, offset)
      const plain = camera(box.width, box.height, null)
      for (const v of [
        new THREE.Vector3(0, 0, 0),
        new THREE.Vector3(0.4, -0.3, 0.2),
        new THREE.Vector3(-0.9, 0.7, -0.5),
      ]) {
        expect(project(withOffset, v, box.width, box.height)).toEqual(
          project(plain, v, box.width, box.height),
        )
      }
    })
  }

  it('a zero inset is the same as no inset', () => {
    expect(stageViewOffset(PHONE.width, PHONE.height, { bottom: 0 })).toBeNull()
  })
})

describe('gate 14 — the specimen is centred in the UNOBSCURED band', () => {
  const cases = [
    ['phone, sheet at rest', PHONE, REST(PHONE.height)],
    ['phone, sheet raised', PHONE, RAISED(PHONE.height)],
    ['phone, at rest + rail and hint', PHONE, WITH_FURNITURE(REST(PHONE.height))],
    ['phone, raised + rail and hint', PHONE, WITH_FURNITURE(RAISED(PHONE.height))],
    ['phone 360x640, at rest', { width: 360, height: 640 }, REST(640)],
    ['phone 360x640, raised', { width: 360, height: 640 }, RAISED(640)],
    ['phone 360x640, raised + furniture', { width: 360, height: 640 }, WITH_FURNITURE(RAISED(640))],
  ] as const

  for (const [name, box, covered] of cases) {
    it(`${name}: the orbit target lands at the middle of what is visible`, () => {
      const visible = box.height - covered
      const offset = stageViewOffset(box.width, box.height, { bottom: covered })
      expect(offset).not.toBeNull()

      const cam = camera(box.width, box.height, offset)
      const centre = project(cam, new THREE.Vector3(0, 0, 0), box.width, box.height)

      expect(centre.x).toBeCloseTo(box.width / 2, 6)
      expect(centre.y).toBeCloseTo(visible / 2, 6)
      // And the arithmetic helper agrees with the real camera, so the helper
      // can be trusted by the assertions below.
      const said = axisPoint(offset, box.width, box.height)
      expect(said.x).toBeCloseTo(centre.x, 6)
      expect(said.y).toBeCloseTo(centre.y, 6)
    })

    it(`${name}: the whole specimen sits ABOVE the covered strip`, () => {
      const visible = box.height - covered
      const offset = stageViewOffset(box.width, box.height, { bottom: covered })
      const cam = camera(box.width, box.height, offset)

      const radius = framedRadius(5, box.width, box.height)
      const { top, bottom } = extent(cam, radius, box.width, box.height)

      expect(top).toBeGreaterThanOrEqual(0)
      expect(bottom).toBeLessThanOrEqual(visible)
    })

    it(`${name}: without the offset it would NOT — this is the defect`, () => {
      // The assertion above is worthless unless the unfixed case fails it.
      const visible = box.height - covered
      const cam = camera(box.width, box.height, null)
      const radius = framedRadius(5, box.width, box.height)
      const { bottom } = extent(cam, radius, box.width, box.height)
      expect(bottom).toBeGreaterThan(visible)
    })
  }
})

describe('gate 14 — a detent change re-frames', () => {
  const rest = stageViewOffset(PHONE.width, PHONE.height, { bottom: REST(PHONE.height) })
  const raised = stageViewOffset(PHONE.width, PHONE.height, { bottom: RAISED(PHONE.height) })

  it('the two detents produce two different framings', () => {
    expect(rest).not.toEqual(raised)
  })

  it('the raised detent frames higher up the stage than the resting one', () => {
    const a = axisPoint(rest, PHONE.width, PHONE.height)
    const b = axisPoint(raised, PHONE.width, PHONE.height)
    expect(b.y).toBeLessThan(a.y)
  })

  it('the raised detent draws the specimen smaller, because its band is shorter', () => {
    expect(magnification(raised)).toBeLessThan(magnification(rest))
    expect(magnification(rest)).toBeLessThan(1)
    expect(magnification(null)).toBe(1)
  })

  it('the specimen fills the same share of the band at BOTH detents', () => {
    // This is the property that makes it "framed" rather than merely "moved
    // up": the fit is re-derived against the band, so the specimen is as
    // generous a use of 150px as it is of 55%.
    const share = (offset: ViewOffset | null, covered: number) => {
      const visible = PHONE.height - covered
      const cam = camera(PHONE.width, PHONE.height, offset)
      const radius = framedRadius(5, PHONE.width, PHONE.height)
      const { top, bottom } = extent(cam, radius, PHONE.width, PHONE.height)
      return (bottom - top) / visible
    }
    expect(share(rest, REST(PHONE.height))).toBeCloseTo(
      share(raised, RAISED(PHONE.height)),
      6,
    )
  })
})

describe('gate 14 — degenerate insets degrade, they do not divide by zero', () => {
  it('an inset taller than the stage still leaves a band to frame into', () => {
    const offset = stageViewOffset(PHONE.width, PHONE.height, { bottom: 10_000 })
    expect(offset).not.toBeNull()
    expect(Number.isFinite(magnification(offset))).toBe(true)
    expect(magnification(offset)).toBeGreaterThan(0)
  })

  it('a negative inset is treated as none', () => {
    expect(stageViewOffset(PHONE.width, PHONE.height, { bottom: -50 })).toBeNull()
  })

  it('a container with no size takes no offset', () => {
    expect(stageViewOffset(0, 0, { bottom: 100 })).toBeNull()
    expect(stageViewOffset(390, 0, { bottom: 100 })).toBeNull()
  })
})

describe('gate 14 — framePosition is unaffected, because nothing moved', () => {
  it('the offset changes no camera position, target or distance', () => {
    // The whole argument for doing this in the projection is that `reset` can
    // still return bit-identical values and `framePosition` can still promise
    // the camera ends a turn exactly as far from the specimen as it started.
    // Both are properties of camera.position, so: it does not move.
    const offset = stageViewOffset(PHONE.width, PHONE.height, {
      bottom: REST(PHONE.height),
    })
    const cam = camera(PHONE.width, PHONE.height, null)
    const before = cam.position.clone()
    const distanceBefore = before.distanceTo(new THREE.Vector3(0, 0, 0))

    cam.setViewOffset(
      offset!.fullWidth,
      offset!.fullHeight,
      offset!.offsetX,
      offset!.offsetY,
      offset!.width,
      offset!.height,
    )
    cam.clearViewOffset()

    expect(cam.position.equals(before)).toBe(true)
    expect(cam.position.distanceTo(new THREE.Vector3(0, 0, 0))).toBe(distanceBefore)
  })
})
