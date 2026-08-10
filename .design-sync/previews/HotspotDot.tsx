// Hotspot states from the frozen reference §07 — identity by size, fill
// inversion and numeral, never hue. Anatomy-shaped strings follow the design
// pipeline's rule: placeholder only, no invented science (Stage 8 gates it).
import { HotspotDot } from 'mrbadmus-3d-studio'

const dark: React.CSSProperties = {
  position: 'relative',
  width: 150,
  height: 110,
  borderRadius: 11,
  background: 'radial-gradient(90% 90% at 50% 40%, #2C261F, #131009)',
}
const paper: React.CSSProperties = {
  position: 'relative',
  width: 150,
  height: 110,
  borderRadius: 11,
  background: '#FFFDF8',
  border: '1px solid #E0D2B9',
}

export const Closed = () => (
  <div style={dark}>
    <HotspotDot state="closed" surface="dark" numeral="01" x={75} y={55} label="Structure 01" />
  </div>
)

export const Hover = () => (
  <div style={dark}>
    <HotspotDot state="hover" surface="dark" numeral="01" x={75} y={55} label="Structure 01" />
  </div>
)

export const Open = () => (
  <div style={dark}>
    <HotspotDot state="open" surface="dark" numeral="03" x={75} y={55} label="Structure 03" />
  </div>
)

export const InertDuringRetrieval = () => (
  <div style={dark}>
    <HotspotDot state="inert" surface="dark" numeral="02" x={75} y={55} />
  </div>
)

export const RetrievalTarget = () => (
  <div style={dark}>
    <HotspotDot state="target" surface="dark" numeral="04" x={75} y={55} label="Highlighted structure" />
  </div>
)

export const PaperClosed = () => (
  <div style={paper}>
    <HotspotDot state="closed" surface="paper" numeral="01" x={75} y={55} label="Structure 01" />
  </div>
)

export const PaperOpen = () => (
  <div style={paper}>
    <HotspotDot state="open" surface="paper" numeral="01" x={75} y={55} label="Structure 01" />
  </div>
)
