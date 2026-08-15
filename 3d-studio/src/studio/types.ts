// Specimen content types — mirror of content/specimen.schema.json (MRB-185).
// Naming discipline is binding: specimen and item, never the o-word.

export type KeyStage = 'KS3' | 'KS4'
export type Tier = 'foundation' | 'higher'

export interface SpecimenAssets {
  mesh: string
  fallback: string
  thumbnail: string
  licence: string
  source: string
  acquired: string
}

export interface HotspotRecord {
  id: string
  label: string
  detail: string
  position3d: [number, number, number]
  position2d: [number, number]
  tiers: Tier[]
  retrievable: boolean
  /** Optional override: where present these win, otherwise the hotspot
   * inherits the specimen's specPoints (MRB-193). */
  specPoints?: string[]
  /** Optional override: where present these win, otherwise the hotspot
   * inherits the specimen's keyStages. Same mechanism as specPoints (MRB-193). */
  keyStages?: KeyStage[]
  /** Optional authored alternatives accepted for this structure in the
   * identify round. Written by Mide under the science gate, never computed. */
  accept?: string[]
  /** Optional override: what the CUT FACE through this structure is made of
   * (MRB-217). Where present it wins; otherwise the hotspot inherits the
   * specimen's, and where neither is declared the renderer falls back to its
   * depth heuristic. Same inheritance mechanism as specPoints and keyStages,
   * and for the same reason — absence is an inherit, never a placeholder. */
  cutMaterial?: CutMaterial
}

/** What a cut face is made of.
 *
 * `capColour(depth)` decides this geometrically: outermost is wall, anything
 * nested inside it is cavity. That is right for a solid specimen and WRONG on
 * BodyParts3D geometry, which models chambers as blood-volume casts with no
 * myocardium shell around them — so the ventricles come out inverted, the cast
 * reading as wall because nothing encloses it.
 *
 * The heuristic cannot be fixed by better geometry reasoning, because the
 * information is not in the geometry: whether a solid is tissue or the space
 * tissue surrounds is a fact about anatomy. So it can be AUTHORED, per
 * structure or per specimen, and the heuristic remains for everything
 * unauthored. */
export type CutMaterial = 'wall' | 'cavity'

export interface KeyFact {
  label: string
  value: string
}

export interface SpecimenRecord {
  id: string
  renderer: 'mesh' | 'flat'
  name: string
  epithet: string
  system: string
  keyStages: KeyStage[]
  assets: SpecimenAssets
  description: string
  keyFacts: KeyFact[]
  callouts: { importance: string; didYouKnow: string }
  lessonUrl: string
  specPoints: string[]
  /** Optional specimen-wide default for the cut face's material (MRB-217).
   * Inherited by every hotspot that does not declare its own. Absent on an
   * unauthored specimen, which leaves the depth heuristic in force. */
  cutMaterial?: CutMaterial
  hotspots: HotspotRecord[]
}
