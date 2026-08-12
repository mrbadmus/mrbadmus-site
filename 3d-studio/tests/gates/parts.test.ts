// @vitest-environment node
// Gate 9 — the part graph isolate and layers stand on (MRB-188).
//
// Both tools are answers to one question the shell cannot ask for itself:
// what does this asset actually declare, and what is inside what. That is pure
// geometry plus the node names in the file, so it is asserted here rather than
// only in a browser.
//
// The properties that matter, and the ways this could quietly be a lie:
//
//   * A tool that steps but changes nothing drawn. Every step below is checked
//     by what is VISIBLE afterwards, never by the step counter alone.
//   * A name the studio invented. `partLabel` is asserted to return the
//     declared node name verbatim, and an index — never a word — when the
//     asset names nothing.
//   * Depth read from names rather than from geometry. The nesting fixture
//     below names its parts in the wrong order on purpose.
//   * Hidden geometry that still occludes. three's raycaster does not consult
//     Object3D.visible, so isolate would leave dots labelled through a form
//     that is no longer drawn.

import { describe, expect, it } from 'vitest'
import * as THREE from 'three'
import {
  applyView,
  collectParts,
  contains,
  isShown,
  layerCount,
  partAt,
  partLabel,
  partVisible,
  stepIsolate,
  stepLayers,
  WHOLE_SPECIMEN,
  type PartView,
} from '../../src/renderer/mesh/parts'
import { isOccluded } from '../../src/renderer/mesh/project'

/** A shell with three smaller forms inside it — the shape of the generated
 * test specimen, and of any specimen that passes spec §4's interior-geometry
 * purchase gate. The names are deliberately in an order that would give the
 * wrong answer if depth were read off them. */
function nestedSpecimen(): THREE.Group {
  const model = new THREE.Group()

  const inner01 = new THREE.Mesh(new THREE.SphereGeometry(0.2, 16, 12))
  inner01.position.set(0.3, 0, 0)
  inner01.name = 'a-inner-01'

  const shell = new THREE.Mesh(new THREE.SphereGeometry(1, 32, 24))
  shell.name = 'z-outer-shell'

  const inner02 = new THREE.Mesh(new THREE.SphereGeometry(0.18, 16, 12))
  inner02.position.set(-0.3, 0.1, 0)
  inner02.name = 'b-inner-02'

  const inner03 = new THREE.Mesh(new THREE.SphereGeometry(0.15, 16, 12))
  inner03.position.set(0, -0.35, 0.1)
  inner03.name = 'c-inner-03'

  model.add(inner01, shell, inner02, inner03)
  model.updateMatrixWorld(true)
  return model
}

/** One merged form, the case a decorative asset would present. */
function singleForm(): THREE.Group {
  const model = new THREE.Group()
  const only = new THREE.Mesh(new THREE.SphereGeometry(1, 32, 24))
  only.name = 'whole'
  model.add(only)
  model.updateMatrixWorld(true)
  return model
}

describe('gate 9 — what the asset declares', () => {
  it('collects one part per drawable node, in declaration order', () => {
    const parts = collectParts(nestedSpecimen())
    expect(parts.map((p) => p.name)).toEqual([
      'a-inner-01',
      'z-outer-shell',
      'b-inner-02',
      'c-inner-03',
    ])
    expect(parts.map((p) => p.index)).toEqual([0, 1, 2, 3])
  })

  it('the label is the declared name, verbatim — never anatomy the studio wrote', () => {
    const parts = collectParts(nestedSpecimen())
    for (const part of parts) expect(partLabel(part)).toBe(part.name)
  })

  it('an unnamed node is labelled by its index, not by a guess', () => {
    const model = new THREE.Group()
    const nameless = new THREE.Mesh(new THREE.SphereGeometry(1, 8, 6))
    model.add(nameless)
    model.updateMatrixWorld(true)

    const [part] = collectParts(model)
    expect(part.name).toBe('')
    expect(partLabel(part)).toBe('PART 1')
    // no letters from any language of anatomy — a numbered placeholder only
    expect(partLabel(part)).toMatch(/^PART \d+$/)
  })
})

describe('gate 9 — depth comes from geometry, not from names', () => {
  it('the enclosing form is depth 0 and everything inside it is depth 1', () => {
    const parts = collectParts(nestedSpecimen())
    const byName = new Map(parts.map((p) => [p.name, p]))
    expect(byName.get('z-outer-shell')!.depth).toBe(0)
    expect(byName.get('a-inner-01')!.depth).toBe(1)
    expect(byName.get('b-inner-02')!.depth).toBe(1)
    expect(byName.get('c-inner-03')!.depth).toBe(1)
    expect(layerCount(parts)).toBe(2)
  })

  it('nesting three deep gives three levels', () => {
    const model = new THREE.Group()
    const outer = new THREE.Mesh(new THREE.SphereGeometry(1, 16, 12))
    const middle = new THREE.Mesh(new THREE.SphereGeometry(0.6, 16, 12))
    const core = new THREE.Mesh(new THREE.SphereGeometry(0.2, 16, 12))
    model.add(outer, middle, core)
    model.updateMatrixWorld(true)

    const parts = collectParts(model)
    expect(parts.map((p) => p.depth)).toEqual([0, 1, 2])
    expect(layerCount(parts)).toBe(3)
  })

  it('two forms side by side are both outermost', () => {
    const model = new THREE.Group()
    const left = new THREE.Mesh(new THREE.SphereGeometry(0.5, 16, 12))
    left.position.set(-1, 0, 0)
    const right = new THREE.Mesh(new THREE.SphereGeometry(0.5, 16, 12))
    right.position.set(1, 0, 0)
    model.add(left, right)
    model.updateMatrixWorld(true)

    expect(collectParts(model).map((p) => p.depth)).toEqual([0, 0])
    expect(layerCount(collectParts(model))).toBe(1)
  })

  it('a box does not contain an identical box — a duplicated form is not inside itself', () => {
    const box = new THREE.Box3(new THREE.Vector3(-1, -1, -1), new THREE.Vector3(1, 1, 1))
    const same = box.clone()
    expect(contains(box, same)).toBe(false)
    expect(contains(same, box)).toBe(false)
  })
})

describe('gate 9 — isolate steps through what is declared, and shows it', () => {
  it('steps one part at a time and then returns the whole specimen', () => {
    const model = nestedSpecimen()
    const parts = collectParts(model)

    let view: PartView = WHOLE_SPECIMEN
    const shownAtEachStep: number[] = []

    for (let i = 0; i < parts.length; i += 1) {
      view = stepIsolate(view, parts)
      applyView(parts, view)
      shownAtEachStep.push(parts.filter((p) => p.object.visible).length)
      expect(view.isolated).toBe(i)
      expect(parts[i].object.visible).toBe(true)
    }
    // exactly one form drawn at every step — not a counter that moved while
    // the picture stayed the same
    expect(shownAtEachStep).toEqual([1, 1, 1, 1])

    view = stepIsolate(view, parts)
    applyView(parts, view)
    expect(view.isolated).toBeNull()
    expect(parts.every((p) => p.object.visible)).toBe(true)
  })

  it('a single-form asset has nothing to isolate and stays whole', () => {
    const parts = collectParts(singleForm())
    const view = stepIsolate(WHOLE_SPECIMEN, parts)
    expect(view.isolated).toBeNull()
    applyView(parts, view)
    expect(parts[0].object.visible).toBe(true)
  })
})

describe('gate 9 — layers peels depth, and the peel is visible', () => {
  it('peels the outer level, then restores', () => {
    const model = nestedSpecimen()
    const parts = collectParts(model)
    const shell = parts.find((p) => p.name === 'z-outer-shell')!

    let view = stepLayers(WHOLE_SPECIMEN, parts)
    applyView(parts, view)
    expect(view.peeled).toBe(1)
    expect(shell.object.visible).toBe(false)
    expect(parts.filter((p) => p.object.visible)).toHaveLength(3)

    view = stepLayers(view, parts)
    applyView(parts, view)
    expect(view.peeled).toBe(0)
    expect(parts.every((p) => p.object.visible)).toBe(true)
  })

  it('a single-level asset has nothing to peel', () => {
    const parts = collectParts(singleForm())
    const view = stepLayers(WHOLE_SPECIMEN, parts)
    expect(view.peeled).toBe(0)
    applyView(parts, view)
    expect(parts[0].object.visible).toBe(true)
  })

  it('isolate wins over a peel that is already engaged', () => {
    const parts = collectParts(nestedSpecimen())
    const peeled = stepLayers(WHOLE_SPECIMEN, parts)
    const both: PartView = { ...peeled, isolated: 1 }
    expect(partVisible(parts[1], both, parts)).toBe(true)
    expect(parts.filter((p) => partVisible(p, both, parts))).toHaveLength(1)
  })
})

describe('gate 9 — a part that is not drawn does not occlude', () => {
  const CAMERA = new THREE.Vector3(0, 0, 5)

  it('an anchor inside the shell is occluded while the shell is drawn', () => {
    const model = nestedSpecimen()
    const parts = collectParts(model)
    applyView(parts, WHOLE_SPECIMEN)
    const insideTheShell = new THREE.Vector3(0.3, 0, 0.25)
    expect(isOccluded(insideTheShell, CAMERA, model, 1)).toBe(true)
  })

  it('and is reachable once layers has peeled the shell away', () => {
    const model = nestedSpecimen()
    const parts = collectParts(model)
    applyView(parts, stepLayers(WHOLE_SPECIMEN, parts))
    const insideTheShell = new THREE.Vector3(0.3, 0, 0.25)
    // three's raycaster ignores Object3D.visible entirely, so this is only
    // true because isOccluded filters the hits itself.
    expect(isOccluded(insideTheShell, CAMERA, model, 1)).toBe(false)
  })

  it('isShown walks the whole chain, not one flag', () => {
    const model = nestedSpecimen()
    const parts = collectParts(model)
    expect(isShown(parts[0].object, model)).toBe(true)

    model.visible = false
    expect(isShown(parts[0].object, model)).toBe(false)
    model.visible = true

    const orphan = new THREE.Mesh(new THREE.SphereGeometry(0.1, 8, 6))
    expect(isShown(orphan, model)).toBe(false)
  })
})

describe('gate 9 — an anchor resolves to the structure it sits on', () => {
  it('a point inside an inner form resolves to that form, not to the shell', () => {
    const parts = collectParts(nestedSpecimen())
    const inside = partAt(new THREE.Vector3(0.3, 0, 0), parts)
    expect(inside?.name).toBe('a-inner-01')
  })

  it('a point on the outer surface resolves to the shell', () => {
    const parts = collectParts(nestedSpecimen())
    const onTheSurface = partAt(new THREE.Vector3(0, 0, 0.99), parts)
    expect(onTheSurface?.name).toBe('z-outer-shell')
  })

  it('a point outside every form resolves to the nearest, never to nothing', () => {
    const parts = collectParts(nestedSpecimen())
    const outside = partAt(new THREE.Vector3(0, 0, 40), parts)
    expect(outside?.name).toBe('z-outer-shell')
  })
})
