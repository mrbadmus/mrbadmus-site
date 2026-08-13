// The eight tool glyphs the rail draws (§06). Each is a stroked SVG on
// `currentColor`, so the surface — not the icon — decides the colour: the
// dark room inherits the room's text token, the paper stage the ink.
// UI copy (the tool names) is real.
import { ToolIcon } from 'mrbadmus-3d-studio'

const TOOLS = [
  'rotate',
  'zoom',
  'isolate',
  'cross-section',
  'layers',
  'labels',
  'reset',
  'auto-rotate',
] as const

const row: React.CSSProperties = {
  display: 'flex',
  gap: 18,
  flexWrap: 'wrap',
  alignItems: 'flex-start',
  padding: 20,
  borderRadius: 14,
}

const cell: React.CSSProperties = {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  gap: 8,
  width: 76,
  font: "400 10.5px/1 var(--st-mono)",
  letterSpacing: '0.06em',
  textTransform: 'uppercase',
}

export const OnDarkRoom = () => (
  <div style={{ ...row, background: 'var(--st-room)', color: 'var(--st-room-text)' }}>
    {TOOLS.map((tool) => (
      <span key={tool} style={cell}>
        <ToolIcon tool={tool} />
        {tool}
      </span>
    ))}
  </div>
)

export const OnPaper = () => (
  <div style={{ ...row, background: 'var(--st-paper)', color: 'var(--st-ink)' }}>
    {TOOLS.map((tool) => (
      <span key={tool} style={cell}>
        <ToolIcon tool={tool} />
        {tool}
      </span>
    ))}
  </div>
)

// size is the one knob — the rail draws 20, the phone sheet's controls smaller
export const Sizes = () => (
  <div style={{ ...row, background: 'var(--st-room)', color: 'var(--st-room-text)', alignItems: 'center' }}>
    {[16, 20, 28, 40].map((size) => (
      <span key={size} style={{ ...cell, width: 60 }}>
        <ToolIcon tool="rotate" size={size} />
        {size}px
      </span>
    ))}
  </div>
)
