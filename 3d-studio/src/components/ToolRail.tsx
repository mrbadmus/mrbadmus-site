// Tool rail — renders from the renderer's DECLARED tool support, never from a
// hardcoded list. A tool the renderer does not honour is absent, not greyed
// (§06: "a disabled tool is a promise the device cannot keep"). All controls
// are wired to no-ops pending Stage 2 (MRB-186 acceptance).

import type { Renderer, ToolId } from '../renderer/types'
import { ToolIcon } from './icons'

const TOOL_META: Record<ToolId, { label: string; verb: string }> = {
  rotate: { label: 'Rotate', verb: 'drag' },
  zoom: { label: 'Zoom', verb: 'scroll' },
  isolate: { label: 'Isolate', verb: 'click' },
  'cross-section': { label: 'Cross-section', verb: 'drag' },
  layers: { label: 'Layers', verb: 'click' },
  labels: { label: 'Labels', verb: 'click' },
  reset: { label: 'Reset view', verb: 'click' },
  'auto-rotate': { label: 'Auto-rotate', verb: 'toggle' },
}

/** rail order: manipulation tools, rule, reset, auto-rotate toggle */
const MAIN_ORDER: ToolId[] = ['rotate', 'zoom', 'isolate', 'cross-section', 'layers', 'labels']

export function ToolRail({
  renderer,
  activeTool,
  autoRotate,
  collapsed,
  onTool,
  onAutoRotate,
}: {
  renderer: Renderer
  activeTool: ToolId | null
  autoRotate: boolean
  /** the rail has yielded the bar to the section slider and is drawing only
   * the tool that is running (§09, phone) — the stylesheet needs to know,
   * because a one-button rail must not keep the scroll fade that says there
   * is more */
  collapsed?: boolean
  onTool: (tool: ToolId) => void
  onAutoRotate: () => void
}) {
  const supported = renderer.supportedTools
  const main = MAIN_ORDER.filter((t) => supported.includes(t))
  const hasReset = supported.includes('reset')
  const hasAuto = supported.includes('auto-rotate')

  // A stepped tool knows whether it is engaged; a pointer mode does not, and
  // the shell remembers that for it (MRB-188).
  const isActive = (tool: ToolId): boolean => {
    const stepped = renderer.toolState(tool)
    return stepped ? stepped.active : activeTool === tool
  }

  return (
    <div
      className="rail"
      data-collapsed={collapsed ? '' : undefined}
      role="toolbar"
      aria-label="Stage tools"
    >
      {main.map((tool) => (
        <RailButton
          key={tool}
          tool={tool}
          active={isActive(tool)}
          onClick={() => onTool(tool)}
        />
      ))}
      {(hasReset || hasAuto) && <div className="rail__rule" aria-hidden="true" />}
      {hasReset && (
        <RailButton tool="reset" active={false} onClick={() => onTool('reset')} />
      )}
      {hasAuto && (
        <button
          type="button"
          className={`autorot${autoRotate ? '' : ' is-off'}`}
          aria-pressed={autoRotate}
          aria-label="Auto-rotate"
          onClick={onAutoRotate}
        >
          <span className="autorot__track" aria-hidden="true" />
          <span className="autorot__word" aria-hidden="true">AUTO</span>
        </button>
      )}
    </div>
  )
}

function RailButton({
  tool,
  active,
  onClick,
}: {
  tool: ToolId
  active: boolean
  onClick: () => void
}) {
  const meta = TOOL_META[tool]
  return (
    <button
      type="button"
      className={`railbtn${active ? ' is-active' : ''}`}
      aria-label={meta.label}
      aria-pressed={active}
      onClick={onClick}
    >
      <ToolIcon tool={tool} />
      <span className="railtip" role="presentation">
        <span className="railtip__label">{meta.label}</span>
        <span className="railtip__verb">{meta.verb}</span>
      </span>
    </button>
  )
}
