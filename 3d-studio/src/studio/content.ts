// Single source of record (spec §3.2): everything about a specimen resolves
// from one content record by one id. The library, breadcrumb, stage caption
// and panel all read from here.

import type { HotspotRecord, KeyStage, SpecimenRecord } from './types'
import type { LearnerProfile } from './attempts'
import heart from '../../content/heart.json'

export const specimens: SpecimenRecord[] = [heart as SpecimenRecord]

export function getSpecimen(id: string): SpecimenRecord {
  const record = specimens.find((s) => s.id === id)
  if (!record) throw new Error(`unknown specimen id: ${id}`)
  return record
}

// ── the key-stage filter (MRB-193/186) ───────────────────────────────────────
//
// A specimen is offered to whole key stages; a structure on it may be narrower.
// The heart is a KS3 and a KS4 specimen, but the sino-atrial node, the valves
// and the coronary arteries are KS4 anatomy — a Year 7 lesson on the heart does
// not name them, so a Year 7 student should not see them on the stage and must
// never be asked to name one.
//
// ONE MECHANISM, not a second concept: a hotspot's own `keyStages` win where it
// declares them and it inherits the specimen's where it does not, which is
// exactly what `specPoints` already does. Nothing here is derived — a structure
// is KS4-only because it is written down as KS4-only.
//
// ORTHOGONAL TO `tiers`. Key stage decides whether a structure exists for this
// student at all; tiers differentiates within KS4 between foundation and
// higher. They are two filters over the same list and neither implies the
// other — on the heart every structure is both foundation and higher, so a KS4
// student sees all fourteen whichever tier they sit.

/** Hotspot-level keyStages win; a hotspot without them inherits the
 * specimen's. Mirrors `resolveSpecPoints` in studio/retrieval.ts. */
export function resolveKeyStages(
  specimen: SpecimenRecord,
  hotspot: HotspotRecord,
): readonly KeyStage[] {
  const own = hotspot.keyStages
  return Array.isArray(own) && own.length > 0 ? own : specimen.keyStages
}

/** The structures one viewer may see. `null` is "no filter at all" — see
 * `viewingKeyStage`. */
export function visibleHotspots(
  specimen: SpecimenRecord,
  keyStage: KeyStage | null,
): HotspotRecord[] {
  if (keyStage === null) return [...specimen.hotspots]
  return specimen.hotspots.filter((hotspot) =>
    resolveKeyStages(specimen, hotspot).includes(keyStage),
  )
}

/**
 * Whose key stage is doing the filtering, or null for nobody's.
 *
 * ANONYMOUS VISITORS SEE EVERYTHING. The studio is a public shopfront: a
 * parent, a head of department or a student who has not signed in is looking at
 * what the thing can do, and hiding half the heart from them serves nobody. A
 * key stage is a fact about an ACCOUNT, so where there is no account there is
 * no key stage to filter by — hence the null, rather than a default.
 *
 * `PROVISIONAL_ANONYMOUS_PROFILE` happens to carry keyStage 'KS4', which would
 * show the full set by accident today. This must not be what does the work: the
 * moment that provisional value changes, or an anonymous visitor is treated as
 * KS3 for any other reason, the accident becomes a truncated shopfront. The
 * null path is the mechanism.
 */
export function viewingKeyStage(profile: LearnerProfile): KeyStage | null {
  return profile.userId === null ? null : profile.keyStage
}

/**
 * The specimen as one viewer sees it — the single record every surface then
 * reads, so the stage, the panel, the sheet and the round cannot disagree
 * about what is on the heart.
 *
 * Returns THE SAME OBJECT when nothing is filtered out. That is not a
 * micro-optimisation: the shell memoises on this identity and the renderers
 * reload the specimen when it changes, so a fresh object per render would
 * re-fetch the GLB on every keystroke.
 */
export function specimenForKeyStage(
  specimen: SpecimenRecord,
  keyStage: KeyStage | null,
): SpecimenRecord {
  const visible = visibleHotspots(specimen, keyStage)
  if (visible.length === specimen.hotspots.length) return specimen
  return { ...specimen, hotspots: visible }
}

/** The v1 library set beyond the records that exist in content/ (spec §2 —
 * approved scope list; system captions from the frozen reference). These rows
 * render at coming-soon treatment and are not selectable. A specimen leaves
 * this list by gaining a real content record. */
export const comingSoon: ReadonlyArray<{ name: string; system: string }> = [
  { name: 'Lungs', system: 'Respiratory' },
  { name: 'Liver', system: 'Digestive' },
  { name: 'Small intestine', system: 'Digestive' },
  { name: 'Stomach', system: 'Digestive' },
  { name: 'Kidney', system: 'Excretory' },
  { name: 'Brain', system: 'Nervous' },
  { name: 'Eye', system: 'Nervous' },
]

export const librarySize = specimens.length + comingSoon.length
