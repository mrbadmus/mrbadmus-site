// @vitest-environment node
// Gate 8 — the geometry the hotspot layer stands on (MRB-187).
//
// Occlusion, framing and anchor resolution are the mesh renderer's only
// answers to a question the shell asks constantly ("where is this hotspot,
// and can it be seen"), and they are pure geometry: no WebGL, no canvas, no
// browser needed. So they are asserted here, deterministically, rather than
// only in `3d_render_check.py` where a real browser has to be started.
//
// The property that matters most: Stage 1's placeholder always answered
// visible: true. A renderer that quietly kept doing so would pass every other
// gate in this suite.

import { describe, expect, it } from 'vitest'
import * as THREE from 'three'
import { frameSpecimen, resolveAnchors, standInDirection } from '../../src/renderer/mesh/anchors'
import { isOccluded, projectAnchor } from '../../src/renderer/mesh/project'
import type { HotspotRecord } from '../../src/studio/types'

const WIDTH = 800
const HEIGHT = 600

/** A closed sphere of radius 1 at the origin — enough geometry to have a near
 * side and a far side, which is the whole question. */
function sphere(radius = 1): THREE.Mesh {
  const mesh = new THREE.Mesh(new THREE.SphereGeometry(radius, 32, 24))
  mesh.updateMatrixWorld(true)
  return mesh
}

function cameraAt(position: THREE.Vector3, target = new THREE.Vector3()): THREE.PerspectiveCamera {
  const camera = new THREE.PerspectiveCamera(38, WIDTH / HEIGHT, 0.01, 100)
  camera.position.copy(position)
  camera.lookAt(target)
  camera.updateMatrixWorld(true)
  camera.updateProjectionMatrix()
  return camera
}

function hotspot(id: string, position3d: [number, number, number]): HotspotRecord {
  return {
    id,
    label: id,
    detail: '',
    position3d,
    position2d: [0, 0],
    tiers: ['foundation'],
    retrievable: true,
  }
}

describe('gate 8 — occlusion is honest', () => {
  const model = sphere()
  const camera = cameraAt(new THREE.Vector3(0, 0, 5))
  const scene = { camera, model, width: WIDTH, height: HEIGHT, radius: 1 }

  it('an anchor on the near surface is visible', () => {
    const near = projectAnchor(new THREE.Vector3(0, 0, 1.005), scene)
    expect(near.visible).toBe(true)
  })

  it('the same anchor on the far surface is NOT visible', () => {
    const far = projectAnchor(new THREE.Vector3(0, 0, -1.005), scene)
    expect(far.visible).toBe(false)
    // It still reports where it would be: the shell decides what to do with
    // an invisible dot, the renderer only answers the question.
    expect(far.x).toBeGreaterThan(0)
    expect(far.y).toBeGreaterThan(0)
  })

  it('turning the camera around swaps which one is visible', () => {
    const behind = {
      ...scene,
      camera: cameraAt(new THREE.Vector3(0, 0, -5)),
    }
    expect(projectAnchor(new THREE.Vector3(0, 0, -1.005), behind).visible).toBe(true)
    expect(projectAnchor(new THREE.Vector3(0, 0, 1.005), behind).visible).toBe(false)
  })

  it('an anchor behind the camera is not visible, and is not folded back into frame', () => {
    const point = projectAnchor(new THREE.Vector3(0, 0, 7), scene)
    expect(point.visible).toBe(false)
  })

  it('an anchor outside the frame is not visible', () => {
    const point = projectAnchor(new THREE.Vector3(40, 0, 0), scene)
    expect(point.visible).toBe(false)
  })

  it('projects to container pixels, origin top-left', () => {
    const centre = projectAnchor(new THREE.Vector3(0, 0, 1.005), scene)
    expect(centre.x).toBeCloseTo(WIDTH / 2, 3)
    expect(centre.y).toBeCloseTo(HEIGHT / 2, 3)

    // +Y in world is up, which is DOWN the page: y must decrease.
    const above = projectAnchor(new THREE.Vector3(0, 0.5, 1.005), scene)
    expect(above.y).toBeLessThan(centre.y)
    const right = projectAnchor(new THREE.Vector3(0.5, 0, 1.005), scene)
    expect(right.x).toBeGreaterThan(centre.x)
  })

  it('a hollow model does not occlude through its own opening', () => {
    // Two nested shells: an anchor on the INNER shell's near face is hidden by
    // the outer one. This is the case a normal-facing dot product gets wrong —
    // the inner surface faces the camera, and is still not visible.
    const outer = sphere(2)
    const inner = sphere(1)
    const group = new THREE.Group()
    group.add(outer, inner)
    group.updateMatrixWorld(true)
    const nested = { camera: cameraAt(new THREE.Vector3(0, 0, 8)), model: group, width: WIDTH, height: HEIGHT, radius: 2 }
    expect(projectAnchor(new THREE.Vector3(0, 0, 1.005), nested).visible).toBe(false)
    expect(projectAnchor(new THREE.Vector3(0, 0, 2.01), nested).visible).toBe(true)
  })

  it('isOccluded tolerates the surface an anchor sits on', () => {
    // Exactly on the surface, not lifted: the surface must not read as
    // occluding the anchor it carries.
    expect(isOccluded(new THREE.Vector3(0, 0, 1), new THREE.Vector3(0, 0, 5), model, 1)).toBe(false)
  })
})

describe('gate 8 — framing and anchors', () => {
  it('frames the whole specimen, wherever it sits', () => {
    // Deliberately off-centre, like the test specimen.
    const model = sphere(1.5)
    model.position.set(3, -2, 1)
    model.updateMatrixWorld(true)

    const view = frameSpecimen(model, WIDTH / HEIGHT)
    const camera = cameraAt(view.position, view.target)
    const scene = { camera, model, width: WIDTH, height: HEIGHT, radius: view.radius }

    // Every corner of the bounding box lands inside the frame.
    const box = new THREE.Box3().setFromObject(model)
    for (const x of [box.min.x, box.max.x]) {
      for (const y of [box.min.y, box.max.y]) {
        for (const z of [box.min.z, box.max.z]) {
          const point = projectAnchor(new THREE.Vector3(x, y, z), scene)
          expect(point.x).toBeGreaterThanOrEqual(0)
          expect(point.x).toBeLessThanOrEqual(WIDTH)
          expect(point.y).toBeGreaterThanOrEqual(0)
          expect(point.y).toBeLessThanOrEqual(HEIGHT)
        }
      }
    }
  })

  it('framing is deterministic — which is what makes reset exact', () => {
    const model = sphere(1.5)
    model.position.set(3, -2, 1)
    model.updateMatrixWorld(true)
    const a = frameSpecimen(model, WIDTH / HEIGHT)
    const b = frameSpecimen(model, WIDTH / HEIGHT)
    expect(a.position.toArray()).toEqual(b.position.toArray())
    expect(a.target.toArray()).toEqual(b.target.toArray())
    expect(a.radius).toBe(b.radius)
  })

  it('authored coordinates are used as authored', () => {
    const model = sphere()
    const view = frameSpecimen(model, WIDTH / HEIGHT)
    const anchors = resolveAnchors([hotspot('a', [0.2, -0.3, 0.9])], model, view)
    expect(anchors.get('a')!.toArray()).toEqual([0.2, -0.3, 0.9])
  })

  it('unauthored [0,0,0] hotspots become distinct, visible surface anchors', () => {
    // Every position3d in content is still [0, 0, 0] (Stage 8 authors them).
    // Taken literally they would all sit at the model's centre — inside the
    // mesh, and so occluded forever once occlusion is honest.
    const model = sphere()
    const view = frameSpecimen(model, WIDTH / HEIGHT)
    const hotspots = [hotspot('a', [0, 0, 0]), hotspot('b', [0, 0, 0]), hotspot('c', [0, 0, 0])]
    const anchors = resolveAnchors(hotspots, model, view)

    const camera = cameraAt(view.position, view.target)
    const scene = { camera, model, width: WIDTH, height: HEIGHT, radius: view.radius }

    const points = hotspots.map((h) => {
      const anchor = anchors.get(h.id)!
      expect(anchor.length()).toBeGreaterThan(0.9) // on the surface, not at the centre
      return projectAnchor(anchor, scene)
    })

    // All visible at the authored default view — which is the view the frozen
    // reference draws and the parity gate counts dots in.
    expect(points.every((p) => p.visible)).toBe(true)
    // And distinct, not stacked on each other.
    const keys = new Set(points.map((p) => `${Math.round(p.x)},${Math.round(p.y)}`))
    expect(keys.size).toBe(3)
  })

  it('stand-in anchors sit on the hemisphere the camera faces', () => {
    const model = sphere()
    const view = frameSpecimen(model, WIDTH / HEIGHT)
    const toCamera = view.position.clone().sub(view.target).normalize()
    for (let i = 0; i < 6; i += 1) {
      const direction = standInDirection(i, 6, view)
      expect(direction.dot(toCamera)).toBeGreaterThan(0.5) // within ~60° of the view axis
    }
  })

  it('the same specimen always gets the same stand-ins', () => {
    const model = sphere()
    const view = frameSpecimen(model, WIDTH / HEIGHT)
    const hotspots = [hotspot('a', [0, 0, 0]), hotspot('b', [0, 0, 0])]
    const first = resolveAnchors(hotspots, model, view)
    const second = resolveAnchors(hotspots, model, view)
    for (const id of ['a', 'b']) {
      expect(first.get(id)!.toArray()).toEqual(second.get(id)!.toArray())
    }
  })
})
