// Hotspot dot — every state from reference §07, which is the component source
// of truth. Identity is carried by SIZE, FILL INVERSION and the NUMERAL —
// never by hue (gate 2 renders these greyscale and asserts it). The visual
// specs live inline so they cannot drift from the state table, and so the
// gate test reads the real values.

import type { CSSProperties } from 'react'

export type HotspotState = 'closed' | 'hover' | 'open' | 'inert' | 'target'
export type HotspotSurface = 'dark' | 'paper'

interface Visual {
  size: number
  background: string
  border: string
  boxShadow: string
  color: string
  fontSize: number
}

const DARK: Record<HotspotState, Visual> = {
  closed: {
    size: 28,
    background: '#E4572E',
    border: '2.5px solid #FBF3E6',
    boxShadow: '0 0 0 3px rgba(8,6,4,0.6), 0 5px 12px rgba(0,0,0,0.55)',
    color: '#FFFDF8',
    fontSize: 12,
  },
  hover: {
    size: 32,
    background: '#E4572E',
    border: '2.5px solid #FBF3E6',
    boxShadow:
      '0 0 0 3px rgba(8,6,4,0.6), 0 0 0 9px rgba(251,243,230,0.16)',
    color: '#FFFDF8',
    fontSize: 13,
  },
  open: {
    size: 38,
    background: '#FBF3E6',
    border: '3px solid #E4572E',
    boxShadow: '0 0 0 4px rgba(8,6,4,0.55), 0 8px 20px rgba(0,0,0,0.6)',
    color: '#1A140E',
    fontSize: 14,
  },
  inert: {
    size: 13,
    background: 'transparent',
    border: '1.5px solid rgba(251,243,230,0.42)',
    boxShadow: 'none',
    color: 'transparent',
    fontSize: 0,
  },
  target: {
    size: 52,
    background: '#FBF3E6',
    border: '4px solid #E4572E',
    boxShadow: '0 0 0 5px rgba(8,6,4,0.6), 0 10px 26px rgba(0,0,0,0.65)',
    color: '#1A140E',
    fontSize: 22,
  },
}

// §06/§07 paper variants: ring flips to paper-white, halo to ink; the open
// state inverts to INK fill instead of cream. Hover/inert/target derive by
// the same inversion logic.
const PAPER: Record<HotspotState, Visual> = {
  closed: {
    size: 28,
    background: '#E4572E',
    border: '2.5px solid #FFFDF8',
    boxShadow: '0 0 0 2px #1A140E, 0 4px 10px rgba(60,40,10,0.35)',
    color: '#FFFDF8',
    fontSize: 12,
  },
  hover: {
    size: 32,
    background: '#E4572E',
    border: '2.5px solid #FFFDF8',
    boxShadow: '0 0 0 2px #1A140E, 0 0 0 8px rgba(26,20,14,0.10)',
    color: '#FFFDF8',
    fontSize: 13,
  },
  open: {
    size: 38,
    background: '#1A140E',
    border: '3px solid #E4572E',
    boxShadow: '0 6px 16px rgba(60,40,10,0.4)',
    color: '#FBF3E6',
    fontSize: 14,
  },
  inert: {
    size: 13,
    background: 'transparent',
    border: '1.5px solid rgba(26,20,14,0.42)',
    boxShadow: 'none',
    color: 'transparent',
    fontSize: 0,
  },
  target: {
    size: 52,
    background: '#1A140E',
    border: '4px solid #E4572E',
    boxShadow: '0 6px 16px rgba(60,40,10,0.4)',
    color: '#FBF3E6',
    fontSize: 22,
  },
}

export function hotspotVisual(state: HotspotState, surface: HotspotSurface): Visual {
  return (surface === 'dark' ? DARK : PAPER)[state]
}

export interface HotspotDotProps {
  state: HotspotState
  surface: HotspotSurface
  /** two-digit numeral, e.g. "01" — identity alongside size and fill */
  numeral: string
  /** container-relative position in px; omitted in gate tests */
  x?: number
  y?: number
  label?: string
  onOpen?: () => void
  onHoverChange?: (hovering: boolean) => void
}

export function HotspotDot({
  state,
  surface,
  numeral,
  x,
  y,
  label,
  onOpen,
  onHoverChange,
}: HotspotDotProps) {
  const v = hotspotVisual(state, surface)
  const style: CSSProperties = {
    width: v.size,
    height: v.size,
    background: v.background,
    border: v.border,
    boxShadow: v.boxShadow,
    color: v.color,
    fontSize: v.fontSize || undefined,
    ...(x !== undefined && y !== undefined ? { left: x, top: y } : {}),
  }

  // Inert dots are orientation furniture, not controls (§02).
  if (state === 'inert') {
    return <span className="hotspot" data-state={state} style={style} aria-hidden="true" />
  }

  const glyph = state === 'target' ? '?' : numeral

  return (
    <button
      type="button"
      className="hotspot"
      data-state={state}
      style={style}
      aria-label={label ?? `Structure ${numeral}`}
      onClick={onOpen}
      onMouseEnter={() => onHoverChange?.(true)}
      onMouseLeave={() => onHoverChange?.(false)}
      onFocus={() => onHoverChange?.(true)}
      onBlur={() => onHoverChange?.(false)}
    >
      {state === 'target' && <span className="hotspot__ping" aria-hidden="true" />}
      {glyph}
    </button>
  )
}
