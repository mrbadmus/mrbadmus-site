// @vitest-environment node
// Gate 11 — the two renderers are two views of ONE record (MRB-190).
//
// Spec §10 lists "fallback parity" as a gate in its own right, and §3.1 is
// explicit about why: the flat path is a second renderer, not a degraded error
// state. A student on a locked-down school machine gets the same content, the
// same hotspots and the same retrieval round as one on a gaming laptop.
//
// The failure this is written against is drift. Nothing about the two files
// forces them to agree — the mesh renderer resolves anchors by raycast against
// geometry, the flat one reads position2d off the record — so two years from
// now a specimen could easily gain a hotspot that only one of them knows
// about, and nothing on screen would say so.
//
// Both renderers' id resolution is therefore asserted here, against every
// specimen in content/, from the same source of truth.

import { describe, expect, it } from 'vitest'
import * as THREE from 'three'
import { specimens } from '../../src/studio/content'
import { frameSpecimen, resolveAnchors } from '../../src/renderer/mesh/anchors'
import { isAuthoredPoint, resolvePlatePoints } from '../../src/renderer/flat/points'
import { createFlatRenderer } from '../../src/renderer/flat'

/** Something with a near side and a far side for the anchors to land on. */
function specimenGeometry(): THREE.Object3D {
  const model = new THREE.Group()
  const shell = new THREE.Mesh(new THREE.SphereGeometry(1, 32, 24))
  shell.name = 'outer'
  const core = new THREE.Mesh(new THREE.SphereGeometry(0.3, 16, 12))
  core.name = 'inner'
  model.add(shell, core)
  model.updateMatrixWorld(true)
  return model
}

describe('gate 11 — both renderers expose the same hotspot ids', () => {
  it('there is at least one specimen to compare', () => {
    expect(specimens.length).toBeGreaterThan(0)
  })

  for (const specimen of specimens) {
    it(`${specimen.id}: mesh anchors and plate points cover the same ids`, () => {
      const model = specimenGeometry()
      const view = frameSpecimen(model)
      const meshIds = [...resolveAnchors(specimen.hotspots, model, view).keys()].sort()
      const flatIds = [...resolvePlatePoints(specimen.hotspots).keys()].sort()
      const recordIds = specimen.hotspots.map((h) => h.id).sort()

      expect(meshIds).toEqual(recordIds)
      expect(flatIds).toEqual(recordIds)
      expect(flatIds).toEqual(meshIds)
    })

    it(`${specimen.id}: every hotspot carries BOTH coordinates`, () => {
      for (const hotspot of specimen.hotspots) {
        expect(hotspot.position3d).toHaveLength(3)
        expect(hotspot.position2d).toHaveLength(2)
      }
    })

    it(`${specimen.id}: the flat renderer reads labels from the one record`, () => {
      // Not a second lookup, not a copy: the id set the flat renderer answers
      // for and the labels it captions with both come from the record the
      // shell handed it (spec §3.2, the liver/lungs/"Hepar" defect).
      const flat = createFlatRenderer()
      for (const hotspot of specimen.hotspots) {
        expect(specimen.hotspots.find((h) => h.id === hotspot.id)?.label).toBe(
          hotspot.label,
        )
      }
      expect(flat.supportedTools).not.toContain('rotate')
      expect(flat.supportedTools).not.toContain('cross-section')
      expect(flat.supportedTools).not.toContain('layers')
      expect(flat.supportedTools).not.toContain('auto-rotate')
    })
  }
})

describe('gate 11 — the flat rail is what a plate can honestly do', () => {
  const flat = createFlatRenderer()

  it('declares exactly the four tools the reference draws (§06)', () => {
    expect([...flat.supportedTools].sort()).toEqual(
      ['isolate', 'labels', 'reset', 'zoom'].sort(),
    )
  })

  it('declares no quality tiers — no renderer, no tier', () => {
    expect(flat.supportsQualityTiers).toBe(false)
  })

  it('dresses the stage as paper', () => {
    expect(flat.stage).toBe('paper')
  })
})

describe('gate 11 — an unauthored position2d is a sentinel, not a corner', () => {
  it('[0, 0] reads as unauthored', () => {
    expect(isAuthoredPoint([0, 0])).toBe(false)
  })

  it('any non-zero component reads as authored', () => {
    expect(isAuthoredPoint([0, 244])).toBe(true)
    expect(isAuthoredPoint([312, 0])).toBe(true)
  })

  it('unauthored hotspots are spread, not stacked in one place', () => {
    const points = [...resolvePlatePoints([
      hotspot('a'), hotspot('b'), hotspot('c'), hotspot('d'),
    ]).values()]
    const distinct = new Set(points.map((p) => `${p.fx.toFixed(4)},${p.fy.toFixed(4)}`))
    expect(distinct.size).toBe(4)
    // and all of them on the plate
    for (const point of points) {
      expect(point.fx).toBeGreaterThan(0)
      expect(point.fx).toBeLessThan(1)
      expect(point.fy).toBeGreaterThan(0)
      expect(point.fy).toBeLessThan(1)
    }
  })

  it('an authored coordinate wins outright', () => {
    const record = hotspot('x')
    record.position2d = [360, 280]
    const point = resolvePlatePoints([record]).get('x')!
    expect(point.fx).toBeCloseTo(0.5, 6)
    expect(point.fy).toBeCloseTo(0.5, 6)
  })
})

function hotspot(id: string) {
  return {
    id,
    label: id,
    detail: '',
    position3d: [0, 0, 0] as [number, number, number],
    position2d: [0, 0] as [number, number],
    tiers: ['foundation' as const],
    retrievable: true,
  }
}
