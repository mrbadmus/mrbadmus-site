// What the cut face through a part is made of (MRB-217).
//
// THE RULING, AND WHY THE HEURISTIC IS NOT ENOUGH.
//
// `capColour(depth)` in cap.tsx decides the cut face from NESTING DEPTH:
// outermost is wall, anything nested inside it is cavity. That is correct for a
// solid specimen and needs nothing authored, which is why it shipped.
//
// It inverts on the acquired heart. BodyParts3D models the chambers as
// blood-volume CASTS — the shape of the blood, with no myocardium shell around
// it — so a ventricle is a top-level solid with nothing enclosing it, comes out
// at depth 0, and is painted as wall. The one thing on the specimen that is
// unambiguously a cavity reads as the most solid thing there.
//
// No amount of better geometry reasoning fixes that, because the information is
// not in the geometry. Whether a solid is tissue or the space tissue surrounds
// is a fact about anatomy, and the studio does not invent anatomy. So it can be
// AUTHORED — and the heuristic stays in force for everything that is not, so no
// existing specimen changes behaviour.
//
// THE BINDING ALREADY EXISTS; THIS DOES NOT INVENT A SECOND ONE.
// tools/recipes/heart.recipe.json records that a GLB part name binds to a
// hotspot id by slug — `slugify(part name)` equals the id after the specimen
// prefix — and validate_content.py and tools/derive_anchors.py both already
// resolve across that same join. So the material is authored ON THE HOTSPOT,
// which makes this the same inheritance pattern as specPoints and keyStages
// rather than a new mechanism with its own lookup table.

import type { CutMaterial, HotspotRecord, SpecimenRecord } from '../../studio/types'

/** "Right atrium" → "right-atrium".
 *
 * The one reduction that binds a GLB's part names to the record's hotspot ids.
 * Mirrored from validate_content.py's `slugify` and tools/derive_anchors.py's,
 * character for character — a THIRD spelling of this rule that disagreed with
 * the other two would bind some parts and silently not others, which is worse
 * than not binding at all. Gate 15 asserts the three agree on the heart's own
 * part names. */
export function slugify(name: string): string {
  const out: string[] = []
  for (const ch of name.trim().toLowerCase()) {
    if (/[a-z0-9]/.test(ch)) out.push(ch)
    else if (out.length && out[out.length - 1] !== '-') out.push('-')
  }
  return out.join('').replace(/^-+|-+$/g, '')
}

/** The hotspot id a part name binds to, in the record's own namespace. */
export function hotspotIdForPart(specimenId: string, partName: string): string {
  return `${specimenId}.${slugify(partName)}`
}

/**
 * The hotspot a part binds to, or null when it binds to none.
 *
 * THE one lookup. Every per-part field the record can author — `cutMaterial`
 * here, `appearance` in appearance.ts (MRB-218) — resolves through this
 * function rather than re-spelling the join, so a second field can never drift
 * into binding parts differently from the first. A nameless part is not a
 * lookup failure; it is no lookup at all, and the caller falls straight through
 * to the specimen's default.
 */
export function hotspotForPart(
  partName: string,
  specimen: Pick<SpecimenRecord, 'id' | 'hotspots'>,
  hotspotsById?: ReadonlyMap<string, HotspotRecord>,
): HotspotRecord | null {
  if (!partName) return null
  const id = hotspotIdForPart(specimen.id, partName)
  const hotspot = hotspotsById
    ? hotspotsById.get(id)
    : specimen.hotspots.find((h) => h.id === id)
  return hotspot ?? null
}

/**
 * The authored material for a part, or null when nothing is authored for it.
 *
 * Resolution order, and it is exactly the ruling's:
 *
 *   1. the matching hotspot's own `cutMaterial` — declared wins
 *   2. the specimen's `cutMaterial` — inherited where the hotspot is silent
 *   3. null — and the caller falls back to the depth heuristic
 *
 * A part with NO matching hotspot falls through to the specimen's default if
 * there is one, and otherwise to the heuristic. That is correct rather than an
 * error: a GLB may legitimately declare structural geometry the record has no
 * hotspot for, and the studio has nothing to say about it.
 */
export function resolveCutMaterial(
  partName: string,
  specimen: Pick<SpecimenRecord, 'id' | 'hotspots'> & { cutMaterial?: CutMaterial },
  hotspotsById?: ReadonlyMap<string, HotspotRecord>,
): CutMaterial | null {
  const hotspot = hotspotForPart(partName, specimen, hotspotsById)
  return hotspot?.cutMaterial ?? specimen.cutMaterial ?? null
}

/** Index the hotspots once per load, so a specimen with many parts does not
 * re-scan the list for every cap. */
export function indexHotspots(
  hotspots: readonly HotspotRecord[],
): ReadonlyMap<string, HotspotRecord> {
  return new Map(hotspots.map((h) => [h.id, h]))
}
