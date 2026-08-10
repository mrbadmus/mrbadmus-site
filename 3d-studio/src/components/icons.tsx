// Inline SVG glyphs, paths lifted from the frozen reference. Everything that
// looks like a character (arrow, tick, cross) is DRAWN, never typed — the
// self-hosted latin subsets do not carry U+2192/U+2713/U+2715 (see tokens.css).

import type { ToolId } from '../renderer/types'

export function BrandMark({ size = 21 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 22 22" aria-hidden="true">
      <path
        d="M3.5 3.5 L11 11 L3.5 18.5"
        stroke="#E4572E"
        strokeWidth="3.4"
        fill="none"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
      <path
        d="M12 3.5 L19.5 11 L12 18.5"
        stroke="#E4572E"
        strokeOpacity="0.34"
        strokeWidth="3.4"
        fill="none"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  )
}

export function MenuIcon({ color = 'var(--st-ink)' }: { color?: string }) {
  return (
    <svg width="16" height="16" viewBox="0 0 16 16" style={{ color }} aria-hidden="true">
      <path d="M2.5 4h11M2.5 8h11M2.5 12h11" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" />
    </svg>
  )
}

export function CloseIcon({ color = 'var(--st-ink)' }: { color?: string }) {
  return (
    <svg width="14" height="14" viewBox="0 0 16 16" style={{ color }} aria-hidden="true">
      <path d="M4 4l8 8M12 4l-8 8" stroke="currentColor" strokeWidth="1.9" strokeLinecap="round" />
    </svg>
  )
}

export function ArrowIcon({ color = 'currentColor', size = 16 }: { color?: string; size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 16 16" aria-hidden="true">
      <path
        d="M2.5 8h10M8.5 3.5 13 8l-4.5 4.5"
        stroke={color}
        strokeWidth="1.8"
        fill="none"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  )
}

export function BookIcon() {
  return (
    <svg width="19" height="19" viewBox="0 0 20 20" fill="none" stroke="currentColor" style={{ color: 'var(--st-ink)' }} strokeWidth="1.7" strokeLinejoin="round" aria-hidden="true">
      <path d="M3 4.2h5.2a2 2 0 0 1 1.8 1.1 2 2 0 0 1 1.8-1.1H17v11h-5.2a2 2 0 0 0-1.8 1 2 2 0 0 0-1.8-1H3Z" />
    </svg>
  )
}

/** Tool icons, 20×20, stroke = currentColor so the rail recolours them. */
export function ToolIcon({ tool, size = 20 }: { tool: ToolId; size?: number }) {
  const common = {
    width: size,
    height: size,
    viewBox: '0 0 20 20',
    fill: 'none',
    stroke: 'currentColor',
    strokeWidth: 1.7,
    'aria-hidden': true as const,
  }
  switch (tool) {
    case 'rotate':
      return (
        <svg {...common} strokeLinecap="round">
          <path d="M16.5 10a6.5 6.5 0 1 1-2.1-4.8" />
          <path d="M16.8 2.6v3.9h-3.9" />
        </svg>
      )
    case 'zoom':
      return (
        <svg {...common} strokeLinecap="round">
          <circle cx="8.5" cy="8.5" r="5.4" />
          <path d="M12.6 12.6 17 17M6.4 8.5h4.2M8.5 6.4v4.2" />
        </svg>
      )
    case 'isolate':
      return (
        <svg {...common}>
          <rect x="2.6" y="2.6" width="14.8" height="14.8" rx="2.4" strokeDasharray="3 2.6" />
          <rect x="7.2" y="7.2" width="5.6" height="5.6" rx="1.2" fill="currentColor" stroke="none" />
        </svg>
      )
    case 'cross-section':
      return (
        <svg {...common}>
          <path d="M2.6 17.4 17.4 2.6 17.4 17.4Z" fill="currentColor" fillOpacity="0.35" stroke="none" />
          <rect x="2.6" y="2.6" width="14.8" height="14.8" rx="2.4" />
        </svg>
      )
    case 'layers':
      return (
        <svg {...common} strokeLinejoin="round">
          <path d="M10 2.4 17.6 6.6 10 10.8 2.4 6.6Z" />
          <path d="M2.4 11 10 15.2 17.6 11" />
        </svg>
      )
    case 'labels':
      return (
        <svg {...common}>
          <rect x="2.4" y="5.4" width="15.2" height="9.2" rx="2" />
          <path d="M5.8 10h4.4" strokeLinecap="round" />
          <circle cx="13.6" cy="10" r="1.5" fill="currentColor" stroke="none" />
        </svg>
      )
    case 'reset':
      return (
        <svg {...common}>
          <circle cx="10" cy="10" r="6.2" />
          <circle cx="10" cy="10" r="1.6" fill="currentColor" stroke="none" />
          <path d="M10 1.6v2.6M10 15.8v2.6M1.6 10h2.6M15.8 10h2.6" strokeLinecap="round" />
        </svg>
      )
    case 'auto-rotate':
      // drawn as the AUTO toggle in the rail, not as an icon; placeholder glyph
      return (
        <svg {...common} strokeLinecap="round">
          <path d="M16.5 10a6.5 6.5 0 1 1-2.1-4.8" />
          <path d="M16.8 2.6v3.9h-3.9" />
        </svg>
      )
  }
}
