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
//   * what the cap is PAINTED IN, and how. Design's §08 cross-section treatment
//     names two values and one material property, and all three are arithmetic
//     or textual: the pair itself, the accent's absence from the tissue, the
//     measured ratio between the two, and the flat unlit material that is the
//     load-bearing half of the treatment. Check 8 deliberately does NOT match
//     the hexes — it classifies a cut face by flatness and by luminance
//     extremity, so that it keeps working through a compositing change — which
//     leaves the values themselves needing a home. This is the home.
//
// The coverage assertion is not hypothetical. The first run of check 8 found a
// real void because `capTransform` centred the quad on the world origin, and
// the generated test specimen is deliberately modelled off-centre.

import { readFileSync } from 'node:fs'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
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
import { capColour } from '../../src/renderer/mesh/cap'
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

// ── the cut face's own treatment (§08) ────────────────────────────────
//
// Design authored the cross-section treatment once the tool worked on real
// anatomy, and §08 rules three things about the cap that the geometry above
// says nothing about: which two values it is painted in, that neither of them
// is the accent, and that it is drawn FLAT.
//
// The first shipped build got the third one right by accident and the first two
// wrong on purpose — two accent values, `#A93411` wall and `#E4572E` cavity, on
// the reasoning that both were reference-declared values used as graphic fills.
// §08 overrules it: "Orange comes off the organ entirely. It marks the plane —
// the rule through the specimen, its end ticks, and the slider being dragged —
// because the plane is the interactive thing. Tissue is substance and never
// highlights itself." The two accent values also measured 1.79:1 against each
// other, which a classroom projector merges into one selected object.
//
// WHY THIS LIVES HERE AND NOT IN THE PIXEL CHECK. `3d_render_check.py` check 8
// used to find cut-face pixels by asking whether they were saturated and
// red-dominant, which was a sound classifier for an orange cap and expired with
// it. Its replacement classifies on the two properties Design named as
// load-bearing — a flat population of one exact value, sitting at a luminance
// extreme — deliberately NOT on an exact match against these hexes, so that it
// asserts the cut rather than the palette and survives a future compositing
// pass. That is the right call there and it leaves the values themselves
// unpinned, which is what this block is for.

/** Read cap.tsx as text. Source invariants that no exported value can express
 * — which MATERIAL CLASS the cap is built from, and the whole contents of a
 * module-private table — are asserted this way elsewhere in this suite too;
 * `layout.test.ts` reads studio.css for the same reason.
 *
 * Comments are stripped first, exactly as `layout.test.ts` strips CSS comments,
 * and here it is not a nicety: cap.tsx's own prose names `MeshStandardMaterial`
 * as the material this treatment REPLACED, and names both retired accent hexes.
 * Read unstripped, every assertion below would fail on correct source. The
 * naive line-comment strip is safe because cap.tsx contains no string literal
 * with a `//` in it. */
const CAP_SOURCE = readFileSync(
  resolve(dirname(fileURLToPath(import.meta.url)), '../../src/renderer/mesh/cap.tsx'),
  'utf8',
)
const CAP_CODE = CAP_SOURCE.replace(/\/\*[\s\S]*?\*\//g, '').replace(/\/\/.*$/gm, '')

/** The `CAP_COLOURS` table as the module declares it. Module-private, so it
 * cannot be imported and compared — but it can be read, which matters: a third
 * entry, or an accent restored to a depth `capColour` is never called with,
 * would be invisible to any assertion made through the function alone. */
function capTable(): string[] {
  const literal = CAP_CODE.match(/const\s+CAP_COLOURS\s*=\s*\[([^\]]*)\]/)
  if (!literal) {
    throw new Error(
      'no `const CAP_COLOURS = [...]` in cap.tsx — renamed, reshaped, or moved ' +
        'somewhere this gate cannot see it',
    )
  }
  return [...literal[1].matchAll(/#[0-9A-Fa-f]{6}/g)].map((m) => m[0])
}

/** The cap material's construction, isolated from the two stencil-only
 * materials above it — those are `MeshBasicMaterial` too, and for an unrelated
 * reason (they never write colour at all), so asserting against the whole file
 * would pass on the strength of the wrong object. */
function capMaterialSource(): string {
  const from = CAP_CODE.indexOf('const cap = new THREE.Mesh(')
  const to = CAP_CODE.indexOf('cap.renderOrder', from)
  if (from < 0 || to < 0) {
    throw new Error('cannot find the cap mesh construction in cap.tsx — it has been restructured')
  }
  return CAP_CODE.slice(from, to)
}

// ── two ways of saying "lighter" ──────────────────────────────────────
// WCAG relative luminance is linear-light and is what a contrast RATIO is
// defined on, so the 15.6:1 claim is computed with it — the same arithmetic
// `contrast.test.ts` and check 8's `_luma` use. Rec. 601 luma is the weighted
// average of the ENCODED channels, which is what a greyscale reduction actually
// does to a pixel and what gate 2 measures the hotspot states with. The
// ordering below is asserted in both, so that "extremes of the frame" is a
// property of the values and not an artefact of one weighting.

function channels(hex: string): [number, number, number] {
  const h = hex.replace('#', '')
  return [parseInt(h.slice(0, 2), 16), parseInt(h.slice(2, 4), 16), parseInt(h.slice(4, 6), 16)]
}

function wcagLuminance(hex: string): number {
  const lin = (c: number): number => {
    const s = c / 255
    return s <= 0.04045 ? s / 12.92 : ((s + 0.055) / 1.055) ** 2.4
  }
  const [r, g, b] = channels(hex)
  return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)
}

function contrastRatio(a: string, b: string): number {
  const la = wcagLuminance(a)
  const lb = wcagLuminance(b)
  const [hi, lo] = la > lb ? [la, lb] : [lb, la]
  return (hi + 0.05) / (lo + 0.05)
}

/** Rec. 601 luma — hue discarded, the greyscale a projector or a colour-blind
 * viewer is left with. */
function greyLevel(hex: string): number {
  const [r, g, b] = channels(hex)
  return (0.299 * r + 0.587 * g + 0.114 * b) / 255
}

/** The specimen's own exterior, as the repo declares it: the §08 materials
 * sheet's "Outer wall, uncut" gradient, which is `.ph-form--a` in studio.css.
 * Read rather than transcribed, so that repainting the specimen re-runs the
 * comparison instead of quietly invalidating it. */
function specimenSurface(): string[] {
  const css = readFileSync(
    resolve(dirname(fileURLToPath(import.meta.url)), '../../src/styles/studio.css'),
    'utf8',
  )
  const hexes = new Set<string>()
  for (const rule of css.matchAll(/\.ph-form--[abc]\s*\{([^}]*)\}/g)) {
    for (const hex of rule[1].matchAll(/#[0-9A-Fa-f]{6}/g)) hexes.add(hex[0].toUpperCase())
  }
  if (hexes.size === 0) throw new Error('no .ph-form--a/b/c fills in studio.css — renamed or removed')
  return [...hexes]
}

/** The two retired values, kept by name so the failure message says what the
 * regression IS rather than that a string did not match. */
const RETIRED_ACCENTS = ['#E4572E', '#A93411']

/** How far past the specimen's own surface a cap value has to sit before
 * "extreme" is doing any work. Measured in Rec. 601 luma: the wall clears the
 * lightest point of the exterior by 0.28 and the cavity sits 0.16 below its
 * darkest, so 0.10 fails long before either becomes hard to tell from tissue.
 * Check 8 measures the same property in Chrome and in linear-light luminance,
 * against the specimen's median AS RENDERED (0.50–0.58) rather than against its
 * declared fills, with a separation floor of 0.20. Neither number can be
 * derived from the other — a rendered median includes the lighting — which is
 * why the property is asserted in both places rather than once. */
const SURFACE_MARGIN = 0.1

describe('gate 10 — the cut face is material, not selection', () => {
  it('paints the cut wall and the cavity, and clamps past the end of the table', () => {
    // Outermost is cut WALL; anything nested inside it is CAVITY or lumen. A
    // cavity is an absence of material, so it takes the void end.
    expect(capColour(0)).toBe('#F0E9DC')
    expect(capColour(1)).toBe('#141109')

    // Depth is geometric (parts.ts) and a heart nests deeper than two, so the
    // table is a floor-and-ceiling, not a palette per level: everything inside
    // the wall is cavity.
    expect(capColour(2)).toBe('#141109')
    expect(capColour(7)).toBe('#141109')
    expect(capColour(99)).toBe('#141109')
    // A clamp that only held at one end would still be a bug.
    expect(capColour(-1)).toBe('#F0E9DC')
  })

  it('the accent is off the tissue — and off it in the table, not just at the depths in use', () => {
    // Written against CAP_COLOURS itself, so that restoring EITHER retired
    // value fails here even if it were parked at a depth `capColour` is not
    // currently called with.
    // Compared case-insensitively: the table is a pair of COLOURS, and a
    // re-spelling in lower case is not a regression worth failing a gate over.
    // The exact spelling `capColour` returns is pinned in the test above.
    const table = capTable().map((c) => c.toUpperCase())
    expect(table).toEqual(['#F0E9DC', '#141109'])

    for (const accent of RETIRED_ACCENTS) {
      for (const [depth, value] of [
        [0, capColour(0)],
        [1, capColour(1)],
      ] as const) {
        expect(
          value.toUpperCase(),
          `depth ${depth} is painted ${accent} — §08 takes the accent off the tissue ` +
            'entirely; orange marks the PLANE, because the plane is the interactive thing',
        ).not.toBe(accent)
      }
      expect(
        table,
        `${accent} is back in CAP_COLOURS — the two accent values measured 1.79:1 ` +
          'against each other and read as one selected object under a projector',
      ).not.toContain(accent)
    }
  })

  it('the wall and the cavity measure 15.6:1 against each other', () => {
    // Recomputed from the hexes on every run, never read back from a recorded
    // figure — the point of the pair is the measurement, so a repaint has to
    // move the number.
    //
    // §08's materials sheet annotates the cavity swatch `17:1 AGAINST WALL`.
    // The repo records the measured figure as 15.63:1 (cap.tsx, and the §08–§10
    // reconciliation in design-notes.md); recomputed here it comes out 15.62:1,
    // so the tolerance is deliberately wide enough not to pin either rounding.
    // Design's annotation is generous by about 9%. The ARGUMENT is untouched:
    // the claim is extremes of the frame rather than neighbours in a family,
    // and 15.6:1 clears every threshold that claim is used to support.
    const ratio = contrastRatio(capColour(0), capColour(1))
    expect(
      Math.abs(ratio - 15.6),
      `wall/cavity measures ${ratio.toFixed(2)}:1 — §08 chose the extremes of the frame`,
    ).toBeLessThan(0.1)
  })

  it('the cap is drawn FLAT and UNSHADED, which is the load-bearing half', () => {
    // "The cut face is flat and unshaded while the exterior keeps its gradient.
    // That alone says CUT before any colour is read, and it holds in greyscale."
    // A LIT material puts a gradient across the cap, and a gradient is precisely
    // what says "another curved surface" — the one reading the treatment exists
    // to prevent. §08 is explicit that if an implementation choice forces a
    // trade, flatness is preserved over hue.
    //
    // It is also what check 8 classifies on: a flat fill holds thousands of
    // pixels on one exact value (6.2k of ~8.8k, measured), where the busiest
    // single value on the lit surface holds 148. Light the cap and that
    // population disperses, so the pixel check stops finding a cut face at all.
    const material = capMaterialSource()
    expect(material, 'the cap material is no longer MeshBasicMaterial').toMatch(
      /new THREE\.MeshBasicMaterial\s*\(/,
    )
    // `toneMapped: false` is the second half of the same idea: the two values
    // arrive on the glass as the values Design chose, not as whatever the
    // render tier's tone curve makes of them. The cap is a diagram drawn on the
    // specimen, not a surface inside its lighting — and check 8 measures the
    // same pixels at all three tiers.
    expect(material, 'the cap is going through the tier tone curve').toMatch(
      /toneMapped:\s*false/,
    )
    expect(
      CAP_CODE,
      'a lit material is back in cap.tsx — it puts a gradient across the cut face, ' +
        'which is the one property that makes the cut read as cut',
    ).not.toMatch(/Mesh(Standard|Physical|Phong|Lambert|Toon)Material/)
  })

  it('the two values sit either side of the specimen — the extremes of the frame', () => {
    // "Not neighbours in a family: lightest thing on the stage against darkest."
    // Asserted as an ORDERING against the specimen's own declared exterior
    // rather than against a fixed mid-grey, because "the specimen's surface" is
    // the thing the cut has to be told apart from.
    const wall = capColour(0)
    const cavity = capColour(1)
    const surface = specimenSurface()

    const lightest = Math.max(...surface.map(greyLevel))
    const darkest = Math.min(...surface.map(greyLevel))

    expect(
      greyLevel(wall) - lightest,
      `the cut wall (${greyLevel(wall).toFixed(3)}) is no longer clear of the lightest ` +
        `point of the specimen's own surface (${lightest.toFixed(3)})`,
    ).toBeGreaterThan(SURFACE_MARGIN)
    expect(
      darkest - greyLevel(cavity),
      `the cavity (${greyLevel(cavity).toFixed(3)}) is no longer clear of the darkest ` +
        `point of the specimen's own surface (${darkest.toFixed(3)})`,
    ).toBeGreaterThan(SURFACE_MARGIN)

    // Every stop of the exterior gradient lands BETWEEN the two, which is what
    // "either side of a mid-tone" means when the mid-tone is a gradient rather
    // than a value.
    for (const stop of surface) {
      expect(greyLevel(stop), `${stop} is outside the wall/cavity span`).toBeLessThan(
        greyLevel(wall),
      )
      expect(greyLevel(stop), `${stop} is outside the wall/cavity span`).toBeGreaterThan(
        greyLevel(cavity),
      )
    }

    // And the same ordering in linear-light luminance, the metric check 8
    // classifies with. It holds with a far tighter margin at the dark end
    // (0.03 rather than 0.16) because linear-light compresses the shadows —
    // which is a property of the metric, not of the palette, and is exactly why
    // the margin above is stated in the metric a greyscale reduction uses.
    for (const stop of surface) {
      expect(wcagLuminance(stop)).toBeLessThan(wcagLuminance(wall))
      expect(wcagLuminance(stop)).toBeGreaterThan(wcagLuminance(cavity))
    }
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
