// Putting the authored appearance onto the geometry (MRB-218).
//
// `appearance.ts` decides WHAT a surface is and what colour that makes it under
// a given palette. This file is the only place that talks to Three.js about it.
//
// WHY THE GLB'S OWN MATERIAL CANNOT SIMPLY BE TINTED.
// heart.glb declares exactly one material and all twelve parts reference that
// single instance, so writing a colour onto it would repaint the whole specimen
// at once — the atria, the aorta and the valves would stay indistinguishable,
// which is the defect rather than the fix. Each part therefore gets a material
// of its OWN, built here, and the shared original is dropped.
//
// WHAT THIS MUST NOT TOUCH: THE CUT FACE.
// The cap's flat unshaded `#F0E9DC` / `#141109` pair (cap.tsx §08, measured
// 15.62:1) is what says "cut", and flatness is the load-bearing half of that
// treatment. The cap draws its own meshes into its own group, OUTSIDE the
// model — `SectionCap` builds them from the source geometry with materials it
// owns — so nothing here reaches them. This work colours the outer surface
// only, and if lighting ever bled onto the cap, the cap wins.

import * as THREE from 'three'
import {
  DEFAULT_PALETTE,
  surfaceColour,
  surfaceFinish,
  type PaletteId,
} from './appearance'
import type { Appearance } from '../../studio/types'
import type { SpecimenPart } from './parts'

interface Painted {
  mesh: THREE.Mesh
  appearance: Appearance | null
  material: THREE.MeshPhysicalMaterial
}

/**
 * The coat of materials the renderer lays over a loaded specimen.
 *
 * Owns them for the specimen's lifetime: built once at load, recoloured in
 * place on a palette switch, given back on release. A palette swap writes one
 * colour uniform per material and triggers no shader recompile, because finish
 * is palette-independent by design — which is what makes the switch cost
 * "nothing but a material update".
 */
export class SpecimenSurface {
  private painted: Painted[] = []
  private palette: PaletteId = DEFAULT_PALETTE

  /** Build one material per part and hang it on the geometry.
   *
   * Called from `adopt()`, BEFORE the model is handed to React — so by the time
   * `useClippedMaterials` runs its effect and puts the clipping plane on the
   * specimen's materials, the materials it finds are these ones. */
  paint(
    parts: readonly SpecimenPart[],
    appearanceFor: (part: SpecimenPart) => Appearance | null,
    palette: PaletteId = this.palette,
  ): void {
    this.dispose()
    this.palette = palette

    // The originals are shared between parts, so they are collected in a set
    // and released once. They never reached the GPU — every one of them is
    // replaced before the first frame is drawn — so this is returning a plain
    // JS object, not a texture upload.
    const originals = new Set<THREE.Material>()

    for (const part of parts) {
      const mesh = part.object as THREE.Mesh
      if (!mesh.isMesh) continue

      for (const material of Array.isArray(mesh.material) ? mesh.material : [mesh.material]) {
        if (material) originals.add(material)
      }

      const appearance = appearanceFor(part)
      const finish = surfaceFinish(appearance)
      const material = new THREE.MeshPhysicalMaterial({
        color: new THREE.Color(surfaceColour(appearance, palette)),
        roughness: finish.roughness,
        metalness: finish.metalness,
        sheen: finish.sheen,
        sheenRoughness: finish.sheenRoughness,
        sheenColor: new THREE.Color(finish.sheenColour),
        // Large smooth areas of a dark saturated red band badly on an 8-bit
        // display; dithering costs nothing and is the difference between
        // "tissue" and "gradient artefact" on the deoxygenated chambers.
        dithering: true,
      })
      material.name = `${part.name || `part ${part.index + 1}`} · ${appearance ?? 'unauthored'}`

      mesh.material = material
      this.painted.push({ mesh, appearance, material })
    }

    for (const material of originals) material.dispose()
  }

  /**
   * Swap the palette. Colour only: the finish does not move, so no material is
   * rebuilt, no shader is recompiled, and — critically — the clipping planes
   * `useClippedMaterials` has already attached stay attached. A palette switch
   * during an open cross-section does not disturb the cut.
   */
  setPalette(palette: PaletteId): void {
    this.palette = palette
    for (const { appearance, material } of this.painted) {
      material.color.set(surfaceColour(appearance, palette))
    }
  }

  /** Which palette is in force. */
  activePalette(): PaletteId {
    return this.palette
  }

  /** What each part was actually painted, for the browser-driven gates and for
   * anyone asking the renderer to account for itself. */
  report(): ReadonlyArray<{ name: string; appearance: Appearance | null; colour: string }> {
    return this.painted.map(({ mesh, appearance, material }) => ({
      name: mesh.name,
      appearance,
      colour: `#${material.color.getHexString().toUpperCase()}`,
    }))
  }

  /** Give the materials back. Eight specimens are coming, and a studio a
   * teacher leaves open all lesson must not accumulate them. */
  dispose(): void {
    for (const { material } of this.painted) material.dispose()
    this.painted = []
  }
}
