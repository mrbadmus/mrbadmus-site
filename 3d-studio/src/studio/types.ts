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
