// The tool rail renders from the renderer's DECLARED tool support — the
// viewport renderer honours seven tools, the paper renderer four (absent,
// not greyed: §06 "a disabled tool is a promise the device cannot keep").
import { ToolRail, createPlaceholderRenderer } from 'mrbadmus-3d-studio'

const viewportStage: React.CSSProperties = {
  position: 'relative',
  width: 220,
  height: 420,
  borderRadius: 12,
  background: 'radial-gradient(90% 75% at 50% 38%, #2C261F 0%, #191510 55%, #100D0A 100%)',
}
const paperStage: React.CSSProperties = {
  position: 'relative',
  width: 220,
  height: 420,
  borderRadius: 12,
  background: '#FFFDF8',
  border: '1px solid #D9C9AC',
}

const viewport = createPlaceholderRenderer('viewport')
const paper = createPlaceholderRenderer('paper')

export const ViewportSevenTools = () => (
  <div style={viewportStage} className="stage stage--viewport">
    <ToolRail
      renderer={viewport}
      activeTool="rotate"
      autoRotate={false}
      onTool={() => {}}
      onAutoRotate={() => {}}
    />
  </div>
)

export const PaperFourTools = () => (
  <div style={paperStage} className="stage stage--paper">
    <ToolRail
      renderer={paper}
      activeTool={null}
      autoRotate={false}
      onTool={() => {}}
      onAutoRotate={() => {}}
    />
  </div>
)
