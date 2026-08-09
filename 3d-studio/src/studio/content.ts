// Single source of record (spec §3.2): everything about a specimen resolves
// from one content record by one id. The library, breadcrumb, stage caption
// and panel all read from here.

import type { SpecimenRecord } from './types'
import heart from '../../content/heart.json'

export const specimens: SpecimenRecord[] = [heart as SpecimenRecord]

export function getSpecimen(id: string): SpecimenRecord {
  const record = specimens.find((s) => s.id === id)
  if (!record) throw new Error(`unknown specimen id: ${id}`)
  return record
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
