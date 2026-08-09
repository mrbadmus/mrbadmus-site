// Quality chip + override panel (§01 + §07). The chip is the whole
// affordance: four-bar meter and one word, at caption contrast — the quietest
// element on the stage. No toast, no banner, no first-run tour. Auto stays
// selected until a person overrides it, and the detected tier stays visible
// so the override is a choice against something known.

import type { CapabilityTier } from '../studio/capability'
import type { QualitySetting } from '../studio/quality'
import { chipDisplay, detectedWord, QUALITY_OPTIONS } from '../studio/quality'

function Meter({ bars, panel }: { bars: 1 | 2 | 3 | 4; panel?: boolean }) {
  return (
    <span className={`meter${panel ? ' meter--panel' : ''}`} aria-hidden="true">
      {[1, 2, 3, 4].map((n) => (
        <i key={n} className={n <= bars ? '' : 'is-dim'} />
      ))}
    </span>
  )
}

export function QualityChip({
  setting,
  detected,
  open,
  onToggle,
}: {
  setting: QualitySetting
  detected: CapabilityTier
  open: boolean
  onToggle: () => void
}) {
  const { word, bars } = chipDisplay(setting, detected)
  return (
    <button
      type="button"
      className="chip"
      aria-label={`Render quality: ${word}. Open quality options`}
      aria-expanded={open}
      onClick={onToggle}
    >
      <Meter bars={bars} />
      <span className="chip__word">{word}</span>
    </button>
  )
}

export function QualityPanel({
  setting,
  detected,
  onSelect,
}: {
  setting: QualitySetting
  detected: CapabilityTier
  onSelect: (s: QualitySetting) => void
}) {
  return (
    <div className="qpanel" role="menu" aria-label="Render quality">
      <div className="qpanel__head">
        <span className="qpanel__title">RENDER QUALITY</span>
        <span className="qpanel__detected">DETECTED · {detectedWord(detected)}</span>
      </div>
      <button
        type="button"
        role="menuitemradio"
        aria-checked={setting === 'auto'}
        className={`qrow${setting === 'auto' ? ' is-on' : ''}`}
        onClick={() => onSelect('auto')}
      >
        <span className="qrow__box" aria-hidden="true" />
        <span className="qrow__word">Auto</span>
        <span className="qrow__note">RECOMMENDED</span>
      </button>
      <div className="qpanel__rule" aria-hidden="true" />
      {QUALITY_OPTIONS.map((option) => (
        <button
          key={option.setting}
          type="button"
          role="menuitemradio"
          aria-checked={setting === option.setting}
          className={`qrow${setting === option.setting ? ' is-on' : ''}`}
          onClick={() => onSelect(option.setting)}
        >
          <span className="qrow__box" aria-hidden="true" />
          <span className="qrow__word">{option.word}</span>
          <span className="qrow__meter">
            <Meter bars={option.bars} panel />
          </span>
        </button>
      ))}
    </div>
  )
}
