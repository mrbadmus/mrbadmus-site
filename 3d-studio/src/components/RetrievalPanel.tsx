// §02 retrieval question panel — Stage 1 builds the STRUCTURE only. Typing
// works; Check, Skip and Reveal are no-ops pending the retrieval stage (same
// pattern as the tool rail). Free recall first: a typed answer, with Reveal
// present but demoted below the fold of the decision.

import { useState } from 'react'
import type { SpecimenRecord } from '../studio/types'

export function RetrievalPanel({
  specimen,
  targetIndex,
  roundSize,
}: {
  specimen: SpecimenRecord
  targetIndex: number
  roundSize: number
}) {
  const [answer, setAnswer] = useState('')

  return (
    <section className="rpanel" aria-label="Retrieval round">
      <div className="rpanel__head">
        <span className="rpanel__round">ROUND 1</span>
        <span className="rpanel__rule" aria-hidden="true" />
        <span className="rpanel__of">
          {targetIndex + 1} OF {roundSize}
        </span>
      </div>

      <div className="progress" aria-label="Round progress">
        {Array.from({ length: roundSize }, (_, i) => {
          if (i === targetIndex) {
            return (
              <span key={i} className="psq psq--current" aria-current="step">
                {i + 1}
              </span>
            )
          }
          return <span key={i} className="psq psq--ahead" aria-hidden="true" />
        })}
      </div>

      <div className="rpanel__ask">NAME THE HIGHLIGHTED STRUCTURE</div>
      <div className="rinput">
        <input
          type="text"
          value={answer}
          placeholder="Type your answer"
          aria-label="Your answer"
          onChange={(e) => setAnswer(e.target.value)}
        />
        {answer === '' && <span className="rinput__caret" aria-hidden="true" />}
      </div>
      <div className="rpanel__actions">
        <button type="button" className="rbtn-check">Check</button>
        <button type="button" className="rbtn-skip">Skip</button>
      </div>
      <div className="rreveal">
        <span className="rreveal__q">Can't recall it?</span>
        <button type="button" className="rreveal__link">Reveal the label</button>
      </div>

      <div className="rmissed">
        <div className="rmissed__eyebrow">MISSED SO FAR</div>
        <div className="rmissed__note">
          Missed structures come back at the end of the round.
        </div>
      </div>

      {/* the round draws only retrievable hotspots for this specimen */}
      <span hidden data-testid="round-specimen">{specimen.id}</span>
    </section>
  )
}
