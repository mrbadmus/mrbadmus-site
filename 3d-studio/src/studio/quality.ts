// Quality override — the mapping between the panel's words and render tiers.
//
// Ruling (MRB-186): Ultra→A, High→B, Balanced→C, and Lite is ALSO tier C.
// Tier D is not user-selectable: D means no WebGL at all, so offering it as a
// quality choice would be offering "turn off 3D", which is not a quality
// decision. The reference's one-bar Lite meter visually implies a step below
// Balanced; the ruling wins (flagged in the Stage 1 report). Lite stays a
// distinct labelled setting so a future mesh renderer may apply further
// reductions within tier C.

import type { RenderTier } from '../renderer/types'
import type { CapabilityTier } from './capability'

export type QualitySetting = 'auto' | 'ultra' | 'high' | 'balanced' | 'lite'

export const QUALITY_OPTIONS: ReadonlyArray<{
  setting: Exclude<QualitySetting, 'auto'>
  word: string
  bars: 1 | 2 | 3 | 4
}> = [
  { setting: 'ultra', word: 'Ultra', bars: 4 },
  { setting: 'high', word: 'High', bars: 3 },
  { setting: 'balanced', word: 'Balanced', bars: 2 },
  { setting: 'lite', word: 'Lite', bars: 1 },
]

const SETTING_TO_TIER: Record<Exclude<QualitySetting, 'auto'>, RenderTier> = {
  ultra: 'A',
  high: 'B',
  balanced: 'C',
  lite: 'C',
}

/** The render tier the renderer should be driven at. Only meaningful when the
 * capability tier is A–C; at capability D there is no mesh renderer to tune. */
export function effectiveRenderTier(
  setting: QualitySetting,
  detected: CapabilityTier,
): RenderTier {
  if (setting !== 'auto') return SETTING_TO_TIER[setting]
  return detected === 'D' ? 'C' : detected
}

/** Chip word + meter bars for the current state. On auto, the detected tier
 * speaks; on override, the chosen word does. */
export function chipDisplay(
  setting: QualitySetting,
  detected: CapabilityTier,
): { word: string; bars: 1 | 2 | 3 | 4 } {
  if (setting === 'auto') {
    const word =
      detected === 'A' ? 'Ultra' : detected === 'B' ? 'High' : 'Balanced'
    const bars = detected === 'A' ? 4 : detected === 'B' ? 3 : 2
    return { word, bars }
  }
  const option = QUALITY_OPTIONS.find((o) => o.setting === setting)!
  return { word: option.word, bars: option.bars }
}

/** The word shown beside DETECTED · in the override panel. */
export function detectedWord(detected: CapabilityTier): string {
  switch (detected) {
    case 'A':
      return 'ULTRA'
    case 'B':
      return 'HIGH'
    case 'C':
      return 'BALANCED'
    case 'D':
      return 'FLAT'
  }
}
