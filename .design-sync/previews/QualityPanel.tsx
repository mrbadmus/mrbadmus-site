// Quality override panel (§07): Auto selected until a person overrides it,
// detected tier always visible, Ultra/High/Balanced/Lite = tiers A/B/C/C.
import { QualityPanel } from 'mrbadmus-3d-studio'

// .qpanel positions absolute bottom-right of the stage; give it a stage-like
// dark box to sit in.
const stage: React.CSSProperties = {
  position: 'relative',
  width: 320,
  height: 340,
  borderRadius: 12,
  background: 'radial-gradient(90% 75% at 50% 38%, #2C261F 0%, #191510 55%, #100D0A 100%)',
}

export const AutoOnDetectedHigh = () => (
  <div style={stage}>
    <QualityPanel setting="auto" detected="B" onSelect={() => {}} />
  </div>
)

export const OverriddenToBalanced = () => (
  <div style={stage}>
    <QualityPanel setting="balanced" detected="A" onSelect={() => {}} />
  </div>
)
