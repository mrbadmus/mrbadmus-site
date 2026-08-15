// The capped cut surface (MRB-189, Stage 4).
//
// A clipping plane on its own opens the specimen into a hollow shell: you see
// through the cut, out of the far side, and into the room. Teaching-wise that
// is worse than no cut at all — a heart's wall thickness is half the point. So
// the cut is capped, and the cap is drawn with the stencil buffer rather than
// with cutaway geometry, because a stencil cap costs nothing per specimen and
// works on any mesh that passes spec §4's watertight gate.
//
// HOW IT WORKS, since stencil capping reads as magic otherwise:
//
//   1. Every clipped part is drawn a second time, colour-write off, into the
//      stencil buffer only: back faces increment the count, front faces
//      decrement it, both clipped by the same plane.
//   2. Where the plane has taken the front face away and left the back face,
//      the count comes out non-zero — which is exactly the set of pixels
//      looking into that part's solid material.
//   3. A quad sitting in the plane is then drawn wherever the count is not
//      zero. That is the cap. It clears the stencil behind it, so the next
//      part starts from a clean count.
//
// This is why spec §4 makes watertightness a purchase gate rather than a
// preference. A mesh with a hole in it has back faces the count never
// balances, and the cap tears.
//
// The plane object is created once by the renderer and MUTATED as the slider
// moves — the materials hold a reference to it, so the cut follows the drag
// without a single material recompile. `version` is how a React effect hears
// about a change that happened inside an object it already has.

import { useEffect, useLayoutEffect, useMemo } from 'react'
import * as THREE from 'three'
import { useThree } from '@react-three/fiber'
import { capSize, capTransform } from './section'
import type { SpecimenPart } from './parts'
import type { CutMaterial } from '../../studio/types'

// The cut face's colours, one per structural depth (§08 of
// `reference/crosssection-v1.html`, the cross-section reference Design authored
// once the tool worked on real anatomy).
//
// One colour for the whole cut is geometrically correct and pedagogically
// useless: a plane through the middle of a solid specimen produces a face that
// fills the silhouette, and if the wall and the chambers inside it are painted
// the same the section reads as a single mass. So the cap is drawn per part and
// coloured by the part's nesting depth — outermost is cut WALL, anything nested
// inside it is CAVITY or lumen. Depth is geometric (see `parts.ts`), so this
// needs nothing authored and no invented palette.
//
// THE ACCENT CAME OFF THE TISSUE. This shipped first as two accent values
// (`#A93411` wall, `#E4572E` cavity) — the reasoning being that both are
// reference-declared values used as graphic fills with no text on them. Design
// overruled it in §08: orange marks the PLANE — the rule through the specimen,
// its end ticks, and the slider while being dragged — because the plane is the
// interactive thing, and tissue is substance that never highlights itself. The
// as-built pair also measured 1.79:1 against each other, close enough in
// lightness that a classroom projector merges them and the whole cut reads as
// one selected object rather than as material.
//
// The two values that replace them are the extremes of the frame rather than
// neighbours in a family: the lightest thing on the stage against the darkest,
// 15.62:1 apart. A cavity is an absence of material, so it takes the void end.
// (§08's materials sheet annotates the pair as 17:1, which is generous by about
// 9%; the argument is unaffected and the allow-list carries the difference.)
const CAP_COLOURS = ['#F0E9DC', '#141109'] as const

export function capColour(depth: number): string {
  return CAP_COLOURS[Math.min(Math.max(depth, 0), CAP_COLOURS.length - 1)]
}

/** The same two values, addressed by what they MEAN rather than by how deep the
 * geometry happens to be (MRB-217). Depth was only ever a proxy for this, and
 * on cast geometry it is a bad one — see `cutmaterial.ts`. */
const MATERIAL_COLOURS: Record<CutMaterial, string> = {
  wall: CAP_COLOURS[0],
  cavity: CAP_COLOURS[1],
}

/** What to paint a part's cut face. Authored material wins; where none is
 * authored the depth heuristic decides, exactly as before. */
export function cutFaceColour(material: CutMaterial | null, depth: number): string {
  return material ? MATERIAL_COLOURS[material] : capColour(depth)
}

/** Coplanar cap quads z-fight. Each depth is nudged this fraction of the
 * specimen's size towards the camera side of the cut, so an inner cut face is
 * drawn in front of the wall it sits inside rather than fighting it. */
const DEPTH_LIFT = 0.0012

export interface CapProps {
  model: THREE.Object3D
  /** stable instance, mutated as the cut is dragged */
  plane: THREE.Plane
  box: THREE.Box3
  /** the parts the asset declares — one cap each */
  parts: readonly SpecimenPart[]
  /** bumped whenever the plane moved or the drawn part set changed */
  version: number
  /** which of the specimen's meshes are on the stage right now, so a part
   * isolate or layers has taken away does not leave its cut face behind */
  isDrawn: (object: THREE.Object3D) => boolean
  /** the AUTHORED material for a part, or null where the record says nothing
   * and the depth heuristic should decide (MRB-217) */
  materialFor: (part: SpecimenPart) => CutMaterial | null
}

interface CapUnit {
  source: THREE.Object3D
  depth: number
  stencil: THREE.Mesh[]
  cap: THREE.Mesh
}

/** Two stencil-only draws per part, plus the quad that fills the result. */
export function SectionCap({
  model,
  plane,
  box,
  parts,
  version,
  isDrawn,
  materialFor,
}: CapProps) {
  const gl = useThree((s) => s.gl)

  // Local clipping has to be on for material-level clippingPlanes to do
  // anything at all; it is off by default.
  useEffect(() => {
    const was = gl.localClippingEnabled
    gl.localClippingEnabled = true
    return () => {
      gl.localClippingEnabled = was
    }
  }, [gl])

  const { group, units } = useMemo(() => {
    const group = new THREE.Group()
    group.matrixAutoUpdate = false

    const size = capSize(box)
    const units: CapUnit[] = []

    // Outermost first, so an inner cut face is drawn over the wall around it.
    const ordered = [...parts].sort((a, b) => a.depth - b.depth)

    model.updateMatrixWorld(true)
    ordered.forEach((part, order) => {
      const source = part.object as THREE.Mesh
      if (!source.isMesh || !source.geometry) return

      const base = new THREE.MeshBasicMaterial()
      base.depthWrite = false
      base.depthTest = false
      base.colorWrite = false
      base.stencilWrite = true
      base.stencilFunc = THREE.AlwaysStencilFunc

      const back = base.clone()
      back.side = THREE.BackSide
      back.clippingPlanes = [plane]
      back.stencilFail = THREE.IncrementWrapStencilOp
      back.stencilZFail = THREE.IncrementWrapStencilOp
      back.stencilZPass = THREE.IncrementWrapStencilOp

      const front = base.clone()
      front.side = THREE.FrontSide
      front.clippingPlanes = [plane]
      front.stencilFail = THREE.DecrementWrapStencilOp
      front.stencilZFail = THREE.DecrementWrapStencilOp
      front.stencilZPass = THREE.DecrementWrapStencilOp
      base.dispose()

      const stencil = [back, front].map((material) => {
        const mesh = new THREE.Mesh(source.geometry, material)
        mesh.renderOrder = 2 * order + 1
        // The stencil twins live OUTSIDE the model: collectParts, the texture
        // budget and disposeTree all walk the model and would otherwise count
        // them as specimen geometry. So they carry the source's world matrix
        // themselves rather than inheriting it.
        mesh.matrixAutoUpdate = false
        mesh.matrix.copy(source.matrixWorld)
        return mesh
      })

      // FLAT AND UNSHADED, and this is the load-bearing half of the treatment.
      // The exterior keeps its gradient; the cut face takes none, so the cut
      // reads as cut before any colour is interpreted and it holds in
      // greyscale. A lit material (this was MeshStandardMaterial) puts a
      // gradient across the cap that says "another curved surface". Basic
      // rather than Standard for the flatness, `toneMapped: false` so the two
      // values arrive on the glass as the values Design chose rather than as
      // whatever the tier's tone curve makes of them — the cap is a diagram
      // drawn on the specimen, not a surface in its lighting.
      const cap = new THREE.Mesh(
        new THREE.PlaneGeometry(size, size),
        new THREE.MeshBasicMaterial({
          color: cutFaceColour(materialFor(part), part.depth),
          toneMapped: false,
          side: THREE.DoubleSide,
          stencilWrite: true,
          stencilRef: 0,
          stencilFunc: THREE.NotEqualStencilFunc,
          stencilFail: THREE.ReplaceStencilOp,
          stencilZFail: THREE.ReplaceStencilOp,
          stencilZPass: THREE.ReplaceStencilOp,
        }),
      )
      cap.renderOrder = 2 * order + 2
      cap.matrixAutoUpdate = false
      // Leaving the count behind would cap the NEXT part against this part's
      // silhouette.
      cap.onAfterRender = (renderer) => renderer.clearStencil()

      group.add(...stencil, cap)
      units.push({ source, depth: part.depth, stencil, cap })
    })

    return { group, units }
  }, [model, plane, box, parts, materialFor])

  // Give everything back: eight specimens are coming, and a studio a teacher
  // leaves open all lesson must not accumulate stencil twins.
  useEffect(
    () => () => {
      for (const unit of units) {
        for (const mesh of unit.stencil) (mesh.material as THREE.Material).dispose()
        unit.cap.geometry.dispose()
        ;(unit.cap.material as THREE.Material).dispose()
      }
    },
    [units],
  )

  // Follow the plane as the slider moves, and follow the parts as isolate and
  // layers change which of them are on the stage. A layout effect, so the cap
  // is in place on the same frame the cut is.
  useLayoutEffect(() => {
    const { position, quaternion } = capTransform(plane, box)
    const lift = capSize(box) * DEPTH_LIFT

    for (const unit of units) {
      unit.cap.quaternion.copy(quaternion)
      unit.cap.position
        .copy(position)
        .addScaledVector(plane.normal, -lift * (unit.depth + 1))
      unit.cap.updateMatrix()
      unit.cap.updateMatrixWorld(true)

      const on = isDrawn(unit.source)
      unit.cap.visible = on
      for (const mesh of unit.stencil) mesh.visible = on
    }
    // `version` is the dependency that matters: `plane` is mutated in place,
    // so its identity never changes and React would otherwise never re-run.
  }, [units, plane, box, isDrawn, version])

  return <primitive object={group} />
}

/** Put the plane on (or take it off) the specimen's own materials. Separate
 * from the cap because the clip has to happen whether or not the cap does —
 * MRB-189's tier fallback is an uncapped clip, never no clip. */
export function useClippedMaterials(
  model: THREE.Object3D | null,
  plane: THREE.Plane | null,
): void {
  useEffect(() => {
    if (!model) return
    const touched: THREE.Material[] = []
    model.traverse((node) => {
      const mesh = node as THREE.Mesh
      if (!mesh.isMesh) return
      const materials = Array.isArray(mesh.material) ? mesh.material : [mesh.material]
      for (const material of materials) {
        if (!material) continue
        material.clippingPlanes = plane ? [plane] : null
        material.clipShadows = true
        // Without this the far wall's inside face is back-face culled and the
        // cut reads as a hole even before the cap is considered.
        material.side = plane ? THREE.DoubleSide : THREE.FrontSide
        material.needsUpdate = true
        touched.push(material)
      }
    })
    return () => {
      for (const material of touched) {
        material.clippingPlanes = null
        material.side = THREE.FrontSide
        material.needsUpdate = true
      }
    }
  }, [model, plane])
}
