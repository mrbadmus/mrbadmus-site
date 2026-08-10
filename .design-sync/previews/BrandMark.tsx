// The public-page brand for this surface, exactly as the frozen reference
// draws it: two chevrons in accent orange, the second at 34% opacity, with
// the Bricolage wordmark. Never the octopus, never the alembic.
import { BrandMark } from 'mrbadmus-3d-studio'

const wordmark: React.CSSProperties = {
  font: "600 18px/1 'Bricolage Grotesque', sans-serif",
  letterSpacing: '-0.025em',
  color: '#1A140E',
}

export const WithWordmark = () => (
  <div style={{ display: 'flex', alignItems: 'center', gap: 9, padding: '22px 26px', background: '#FBF3E6', borderRadius: 12 }}>
    <BrandMark size={21} />
    <span style={wordmark}>MrBadmusAI</span>
  </div>
)

export const OnDarkRoom = () => (
  <div style={{ display: 'flex', alignItems: 'center', gap: 9, padding: '22px 26px', background: '#15110C', borderRadius: 12 }}>
    <BrandMark size={21} />
    <span style={{ ...wordmark, color: '#FBF3E6' }}>MrBadmusAI</span>
  </div>
)

export const Sizes = () => (
  <div style={{ display: 'flex', alignItems: 'center', gap: 22, padding: '22px 26px', background: '#FBF3E6', borderRadius: 12 }}>
    <BrandMark size={21} />
    <BrandMark size={19} />
    <BrandMark size={17} />
  </div>
)
