// The specimen's declared parts — the geometry isolate and layers operate on
// (MRB-188, Stage 3).
//
// ─────────────────────────────────────────────────────────────────────────────
// NAMING: the studio never invents an anatomical name.
//
// A part's name is the node name the GLB declares, taken verbatim. The
// generated test specimen declares `test-shell`, `test-chamber-01` … — neutral
// by design — and those are exactly the strings the caption shows. When an
// acquired specimen declares `left-ventricle`, the same code shows that. A
// file that names nothing gets `PART 3` from its declaration index, never a
// guess. Nothing here reaches into content/*.json for a label, so no
// unauthored anatomy can leak onto the stage through this path.
// ─────────────────────────────────────────────────────────────────────────────
//
// DEPTH is derived from geometry, not from names, so it is right on a specimen
// whose nodes are named badly or not at all. Part B is inside part A when A's
// world bounding box contains B's; a part's depth is the number of parts that
// contain it. On the test specimen that yields depth 0 for the outer shell and
// depth 1 for the three chambers and the torus — which is what Stage 0's
// validator independently proves by ray parity, from different arithmetic.

import * as THREE from 'three'

export interface SpecimenPart {
  /** the node name declared in the asset, verbatim; empty when it declares none */
  name: string
  /** declaration order — the only identity a nameless node has */
  index: number
  /** nesting depth: 0 is outermost */
  depth: number
  object: THREE.Object3D
  box: THREE.Box3
}

/** Boxes are compared with a slack of this fraction of the outer box's size,
 * so a shared wall or a coincident face does not decide containment on a
 * floating-point tie. */
const CONTAINMENT_SLACK = 1e-3

/** Every drawable node the asset declares, in declaration order, with depth
 * resolved. A single-mesh GLB returns one part — which is a real answer, and
 * one the tools below read as "nothing to isolate". */
export function collectParts(model: THREE.Object3D): SpecimenPart[] {
  model.updateMatrixWorld(true)

  const found: Array<{ name: string; object: THREE.Object3D; box: THREE.Box3 }> = []
  model.traverse((node) => {
    if (!(node as THREE.Mesh).isMesh) return
    found.push({
      name: node.name || '',
      object: node,
      box: new THREE.Box3().setFromObject(node),
    })
  })

  return found.map((part, index) => ({
    name: part.name,
    index,
    depth: found.filter((other) => other !== part && contains(other.box, part.box)).length,
    object: part.object,
    box: part.box,
  }))
}

/** True when `outer` encloses `inner`. Equal boxes do not contain each other:
 * the comparison is strict once the slack is spent, so two copies of the same
 * geometry both stay at depth 0 rather than each claiming to be inside the
 * other. */
export function contains(outer: THREE.Box3, inner: THREE.Box3): boolean {
  const size = outer.getSize(new THREE.Vector3())
  const slack = Math.max(size.x, size.y, size.z) * CONTAINMENT_SLACK
  const inside =
    inner.min.x >= outer.min.x - slack &&
    inner.min.y >= outer.min.y - slack &&
    inner.min.z >= outer.min.z - slack &&
    inner.max.x <= outer.max.x + slack &&
    inner.max.y <= outer.max.y + slack &&
    inner.max.z <= outer.max.z + slack
  if (!inside) return false
  // strictly smaller in at least one axis, or it is the same box
  const innerSize = inner.getSize(new THREE.Vector3())
  return (
    innerSize.x < size.x - slack || innerSize.y < size.y - slack || innerSize.z < size.z - slack
  )
}

/** How many depth levels the specimen has. 1 means a single merged form, and
 * therefore nothing for `layers` to peel. */
export function layerCount(parts: readonly SpecimenPart[]): number {
  if (parts.length === 0) return 0
  return Math.max(...parts.map((p) => p.depth)) + 1
}

/** The caption for a part: its declared name, or its declaration index when it
 * has none. Never anatomy the studio made up. */
export function partLabel(part: SpecimenPart): string {
  return part.name || `PART ${part.index + 1}`
}

/** Which part an anchor belongs to: the smallest declared part whose bounds
 * enclose it, else the nearest part by distance to its bounds.
 *
 * Geometric, so it needs no authored binding and stays right when Stage 8
 * authors real coordinates — a point on the left-ventricle wall resolves to
 * the left-ventricle node because that is the smallest box around it. The
 * stand-in anchors all sit on the outer shell's surface, so today they all
 * resolve to the shell; that is the geometry being honest, not the resolver
 * being weak.
 */
export function partAt(
  anchor: THREE.Vector3,
  parts: readonly SpecimenPart[],
): SpecimenPart | null {
  let best: SpecimenPart | null = null
  let bestVolume = Infinity
  for (const part of parts) {
    if (!part.box.containsPoint(anchor)) continue
    const size = part.box.getSize(new THREE.Vector3())
    const volume = size.x * size.y * size.z
    if (volume < bestVolume) {
      best = part
      bestVolume = volume
    }
  }
  if (best) return best

  let nearest: SpecimenPart | null = null
  let nearestDistance = Infinity
  for (const part of parts) {
    const distance = part.box.distanceToPoint(anchor)
    if (distance < nearestDistance) {
      nearest = part
      nearestDistance = distance
    }
  }
  return nearest
}

/** True when the object and every ancestor up to (and including) the model is
 * visible. `Object3D.visible` is not inherited by lookup, and three's raycaster
 * does not consult it at all, so both the occlusion test and the tools have to
 * ask this rather than reading one flag. */
export function isShown(object: THREE.Object3D, root: THREE.Object3D): boolean {
  let node: THREE.Object3D | null = object
  while (node) {
    if (!node.visible) return false
    if (node === root) return true
    node = node.parent
  }
  // Detached from the model we were asked about: not part of what is drawn.
  return false
}

// ── the two tools' state, kept pure so vitest can drive them ────────────────

export interface PartView {
  /** index into `parts` of the single part isolate is showing, or null */
  isolated: number | null
  /** how many outer depth levels `layers` has peeled away */
  peeled: number
}

export const WHOLE_SPECIMEN: PartView = { isolated: null, peeled: 0 }

/** Isolate steps through the declared parts one at a time and then back to the
 * whole specimen, so the control always has a way home. A specimen with fewer
 * than two parts has nothing to isolate and stays whole. */
export function stepIsolate(view: PartView, parts: readonly SpecimenPart[]): PartView {
  if (parts.length < 2) return { ...view, isolated: null }
  if (view.isolated === null) return { ...view, isolated: 0 }
  const next = view.isolated + 1
  return { ...view, isolated: next >= parts.length ? null : next }
}

/** Layers peels one depth level at a time and then restores the whole form.
 * A specimen with a single depth level has nothing to peel. */
export function stepLayers(view: PartView, parts: readonly SpecimenPart[]): PartView {
  const levels = layerCount(parts)
  if (levels < 2) return { ...view, peeled: 0 }
  const next = view.peeled + 1
  return { ...view, peeled: next >= levels ? 0 : next }
}

/** Whether a part is drawn under the current view. Isolate wins outright when
 * it is engaged: a student who asked for one structure gets one structure. */
export function partVisible(
  part: SpecimenPart,
  view: PartView,
  parts: readonly SpecimenPart[],
): boolean {
  if (view.isolated !== null) return parts[view.isolated] === part
  return part.depth >= view.peeled
}

/** Apply a view to the live scene graph. */
export function applyView(
  parts: readonly SpecimenPart[],
  view: PartView,
): void {
  for (const part of parts) part.object.visible = partVisible(part, view, parts)
}
