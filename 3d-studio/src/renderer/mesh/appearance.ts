// What the OUTER SURFACE of a structure looks like (MRB-218).
//
// THE DEFECT. The acquired heart carries no authored materials at all. Its GLB
// declares exactly ONE material — a pale `#DBB8AD`, roughness 0.72 — and all
// twelve parts point at that single instance. So the specimen renders as one
// undifferentiated pale solid: not a heart with its chambers and vessels told
// apart, but a shape. Mide's words: "the heart right now looks like a model, I
// want to see it as a proper heart."
//
// THE BINDING IS THE ONE THAT ALREADY EXISTS. This does NOT invent a second
// lookup. `cutmaterial.ts` established the join for MRB-217 — a GLB part name
// slugifies to a hotspot id, the hotspot declares a value, the specimen
// supplies a default, and where neither declares the renderer falls back — and
// `hotspotForPart` below is imported from there rather than re-spelled. One
// rule, two fields.
//
// ─────────────────────────────────────────────────────────────────────────────
// WHY THE RECORD CARRIES A TOKEN AND NOT A COLOUR
//
// The content record says `blood-deoxygenated`. It does not say `#6E2029`. The
// renderer owns the mapping, exactly as `MATERIAL_COLOURS` in cap.tsx owns
// wall/cavity, and that ownership is what makes TWO PALETTES over the same five
// tokens possible: the record is byte-identical under both, and switching is a
// renderer-side swap that touches no content and no geometry.
//
//   realistic   what tissue actually looks like — the default (Mide, 15 Aug)
//   schematic   the AQA diagram convention, blue for deoxygenated
//
// The realistic palette carries a teaching point of its own: deoxygenated blood
// is DARK RED, not blue. Blue is a diagram convention, and the schematic
// palette is where that convention lives — not a fact about blood.
//
// WHY THE CHAMBERS TAKE BLOOD TOKENS RATHER THAN MUSCLE TOKENS.
// BodyParts3D models the chambers as blood-volume CASTS. That was wrong for
// wall thickness, and it makes the colouring honest: the geometry genuinely IS
// the blood, so painting it as blood is accurate rather than a convention
// imposed on tissue.
//
// This file used to predict that when a shell-modelled mesh landed, those four
// hotspots would MOVE to muscle tokens. That is not what happened (MRB-222).
// The wall arrived as a SEPARATE part — `Ventricular myocardium`, FJ2428 from
// BodyParts3D's isa tree — standing beside the casts rather than replacing
// them. So the chambers keep their blood tokens, and the reading is now
// literal rather than convenient: the cast is the blood, the myocardium is the
// muscle, and both are on the specimen at once. The record grew a sixth token;
// this mechanism did not change at all, which was the point of building it
// this way.
// ─────────────────────────────────────────────────────────────────────────────

import type { Appearance, HotspotRecord, SpecimenRecord } from '../../studio/types'
import { hotspotForPart } from './cutmaterial'

/** The six tokens, in the order the palettes are read and reported in.
 * Adding a seventh is a RULING, not a code change: every palette must cover
 * every token, and the gate asserts exactly that.
 *
 * `muscle` is the sixth (MRB-222, ruled by Mide). It could not have been
 * authored earlier: the specimen had no muscle geometry on it until the
 * ventricular myocardium was assembled from BodyParts3D's isa tree, only
 * blood-volume casts of the four chambers. */
export const APPEARANCES: readonly Appearance[] = [
  'blood-oxygenated',
  'blood-deoxygenated',
  'vessel-oxygenated',
  'vessel-deoxygenated',
  'valve',
  'muscle',
] as const

export type PaletteId = 'realistic' | 'schematic'

export interface Palette {
  id: PaletteId
  /** what this palette is FOR, in one line — read by the report, not the UI */
  intent: string
  colours: Record<Appearance, string>
  /** What geometry the record says nothing about is painted.
   *
   * Deliberately NOT one of the five. A part with no authored token must not
   * claim to be oxygenated or deoxygenated anything — an unauthored structure
   * silently painted arterial red would be the studio inventing anatomy, which
   * is the one thing it does not do. So the fallback is a neutral tissue tone
   * that makes no claim at all. */
  unauthored: string
}

/**
 * The two palettes. Both cover all six tokens; neither may have a gap.
 *
 * These are ALBEDO values handed to a lit material, not screen values. The
 * scene tone-maps (ACES Filmic, exposure 1.05), so what reaches the glass is
 * these colours under the studio's lighting rig — which is correct for a
 * surface, and is exactly why the cut face does the opposite and sets
 * `toneMapped: false`. The cap is a diagram drawn on the specimen; this is
 * substance in the room.
 */
export const PALETTES: Record<PaletteId, Palette> = {
  realistic: {
    id: 'realistic',
    intent:
      'what the tissue actually looks like — the default a student and a ' +
      'visiting teacher see on first load, and the palette in which ' +
      'deoxygenated blood is dark red rather than blue',
    colours: {
      'blood-oxygenated': '#A32B22',
      'blood-deoxygenated': '#6E2029',
      'vessel-oxygenated': '#C9907F',
      'vessel-deoxygenated': '#B08A80',
      valve: '#DCC9A8',
      muscle: '#8E4B42',
    },
    unauthored: '#9C8578',
  },
  schematic: {
    id: 'schematic',
    intent:
      'the AQA diagram convention, where blue means deoxygenated — a ' +
      'convention about diagrams, never a fact about blood',
    colours: {
      'blood-oxygenated': '#B3322C',
      'blood-deoxygenated': '#2F5C8A',
      'vessel-oxygenated': '#C4433A',
      'vessel-deoxygenated': '#3D6E9E',
      valve: '#E8DCC8',
      muscle: '#B5675A',
    },
    unauthored: '#9A9490',
  },
}

/** Realistic is the default. Ruled by Mide, 15 August: it is what he wants a
 * student and a visiting teacher to see on first load. */
export const DEFAULT_PALETTE: PaletteId = 'realistic'

export const PALETTE_IDS: readonly PaletteId[] = ['realistic', 'schematic'] as const

/**
 * How a surface takes the light — separate from its colour, and shared across
 * both palettes.
 *
 * Colour is what the palette swaps; finish is what the tissue IS. A valve is
 * matte in a realistic rendering and matte in a schematic one, because that is
 * a fact about the tissue rather than about the drawing convention. Keeping
 * finish palette-independent means a palette switch is one colour write per
 * material with no shader recompile.
 *
 * ROUGHNESS DOES THE WORK, AND THE SHEEN LOBE WAS MEASURED OUT.
 *
 * This first shipped as MeshPhysicalMaterial with three's sheen lobe — the
 * proper approximation of the soft waxy rim wet tissue has. 3d_render_check.py
 * disagreed, twice, reproducibly:
 *
 *              Tier A median   Tier B median
 *   before          100.0ms          33.4ms
 *   physical+sheen  116.6ms          50.0ms
 *   physical, no sheen             ~50.0ms   ← gating the lobe by tier fixed nothing
 *   standard        100.1ms          35.3ms   ← restored
 *
 * The cost was MeshPhysicalMaterial ITSELF, not the lobe: three compiles the
 * `physical` shader whether or not sheen is switched on. Tier-gating the sheen
 * was tried first and removed again, because it left a flag whose comment
 * claimed a saving it did not make — worse than not having it.
 *
 * Those numbers are SwiftShader on a CPU and are not evidence about a real
 * device; 3d_render_check.py says so at length. But before/after on one machine
 * is exactly what they are for, and a specular response from roughness alone
 * turned out to read as WETTER than the lobe did, not drier — the highlight is
 * tighter and the colour more saturated. So there was nothing to trade.
 */
export interface Finish {
  roughness: number
  metalness: number
}

/** Chambers and lumens: a tight highlight on a wet surface. */
const WET_TISSUE: Finish = { roughness: 0.34, metalness: 0 }

/** Vessel walls: fibrous and a little drier than the blood inside them. */
const VESSEL_WALL: Finish = { roughness: 0.46, metalness: 0 }

/** Valves are the matte exception — thin fibrous tissue, not a wet lumen. */
const VALVE_TISSUE: Finish = { roughness: 0.74, metalness: 0 }

/** Cardiac muscle: drier than the blood it encloses, wetter than a valve.
 *
 * Myocardium in a fresh dissection is damp rather than wet — it has a sheen,
 * but nothing like the standing-liquid highlight of a chamber cast. 0.52 sits
 * it a step drier than a vessel wall (0.46) and well clear of the valve's
 * matte (0.74), which keeps the wall legible as a distinct SURFACE against the
 * blood it surrounds under the cross-section, where the two meet along an edge
 * and a shared finish would let them merge. */
const MUSCLE_TISSUE: Finish = { roughness: 0.52, metalness: 0 }

/** Neutral, and flatter than anything authored — unauthored geometry should
 * not read as more confidently rendered than the structures Mide has actually
 * signed off. */
const UNAUTHORED_FINISH: Finish = { roughness: 0.62, metalness: 0 }

const FINISHES: Record<Appearance, Finish> = {
  'blood-oxygenated': WET_TISSUE,
  'blood-deoxygenated': WET_TISSUE,
  'vessel-oxygenated': VESSEL_WALL,
  'vessel-deoxygenated': VESSEL_WALL,
  valve: VALVE_TISSUE,
  muscle: MUSCLE_TISSUE,
}

/**
 * The authored appearance for a part, or null when nothing is authored for it.
 *
 * Resolution order, and it is the same three steps `resolveCutMaterial` takes:
 *
 *   1. the matching hotspot's own `appearance` — declared wins
 *   2. the specimen's `appearance` — inherited where the hotspot is silent
 *   3. null — and the caller falls back to the palette's `unauthored` tone
 *
 * A part with NO matching hotspot falls through to the specimen's default if
 * there is one, and otherwise to the fallback. Correct rather than an error: a
 * GLB may legitimately declare structural geometry the record has no hotspot
 * for, and the studio has nothing to say about it.
 */
export function resolveAppearance(
  partName: string,
  specimen: Pick<SpecimenRecord, 'id' | 'hotspots'> & { appearance?: Appearance },
  hotspotsById?: ReadonlyMap<string, HotspotRecord>,
): Appearance | null {
  const hotspot = hotspotForPart(partName, specimen, hotspotsById)
  return hotspot?.appearance ?? specimen.appearance ?? null
}

/** What to paint a surface, under a given palette. Null — nothing authored —
 * takes the palette's neutral tone, never one of the six tokens. */
export function surfaceColour(appearance: Appearance | null, palette: PaletteId): string {
  const table = PALETTES[palette]
  return appearance ? table.colours[appearance] : table.unauthored
}

/** How that surface takes the light. Palette-independent, by design. */
export function surfaceFinish(appearance: Appearance | null): Finish {
  return appearance ? FINISHES[appearance] : UNAUTHORED_FINISH
}
