// Capability detection — feature probe ONLY, never user-agent parsing.
// Probed once on load; the user can override the result from the quality
// panel because probes are imperfect and a student who sees a stutter should
// be able to drop a tier themselves.

export type CapabilityTier = 'A' | 'B' | 'C' | 'D'

export interface CapabilityReport {
  tier: CapabilityTier
  webgl2: boolean
  /** GiB as reported by navigator.deviceMemory; null where unsupported */
  deviceMemory: number | null
  /** logical cores; null where unsupported */
  cores: number | null
  viewport: { width: number; height: number }
  pointer: 'fine' | 'coarse'
}

function probeWebGL2(): boolean {
  try {
    const canvas = document.createElement('canvas')
    return canvas.getContext('webgl2') !== null
  } catch {
    return false
  }
}

export function detectCapability(): CapabilityReport {
  const webgl2 = probeWebGL2()
  const nav = navigator as Navigator & { deviceMemory?: number }
  const deviceMemory = typeof nav.deviceMemory === 'number' ? nav.deviceMemory : null
  const cores =
    typeof navigator.hardwareConcurrency === 'number'
      ? navigator.hardwareConcurrency
      : null
  const viewport = { width: window.innerWidth, height: window.innerHeight }
  const pointer =
    typeof window.matchMedia === 'function' &&
    window.matchMedia('(pointer: coarse)').matches
      ? ('coarse' as const)
      : ('fine' as const)

  // Tier D is the floor: no WebGL2 means the flat renderer, full stop.
  if (!webgl2) {
    return { tier: 'D', webgl2, deviceMemory, cores, viewport, pointer }
  }

  // Scored probe. Unreported signals count as mid-range rather than weak, so
  // browsers that hide deviceMemory (Safari, Firefox) are not unfairly demoted.
  const memory = deviceMemory ?? 4
  const cpu = cores ?? 4
  const smallViewport = Math.min(viewport.width, viewport.height) < 500

  let tier: CapabilityTier
  if (memory >= 8 && cpu >= 8 && pointer === 'fine' && !smallViewport) {
    tier = 'A'
  } else if (memory >= 4 && cpu >= 4 && !smallViewport) {
    tier = 'B'
  } else {
    tier = 'C'
  }
  return { tier, webgl2, deviceMemory, cores, viewport, pointer }
}
