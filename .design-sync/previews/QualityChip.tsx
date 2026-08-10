// The quality chip (§01): four-bar meter + one word, bottom-right, at
// caption contrast — deliberately the quietest element on the stage.
import { QualityChip } from 'mrbadmus-3d-studio'

const stage: React.CSSProperties = {
  position: 'relative',
  width: 260,
  height: 120,
  borderRadius: 12,
  background: 'radial-gradient(90% 75% at 50% 38%, #2C261F 0%, #191510 55%, #100D0A 100%)',
}

export const AutoDetectedHigh = () => (
  <div style={stage}>
    <QualityChip setting="auto" detected="B" open={false} onToggle={() => {}} />
  </div>
)

export const AutoDetectedBalanced = () => (
  <div style={stage}>
    <QualityChip setting="auto" detected="C" open={false} onToggle={() => {}} />
  </div>
)

export const OverriddenToLite = () => (
  <div style={stage}>
    <QualityChip setting="lite" detected="A" open={false} onToggle={() => {}} />
  </div>
)
