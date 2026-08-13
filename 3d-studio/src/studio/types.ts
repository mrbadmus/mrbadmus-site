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
  /** Optional authored alternatives accepted for this structure in the
   * identify round. Written by Mide under the science gate, never computed. */
  accept?: string[]
}

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
  hotspots: HotspotRecord[]
}
