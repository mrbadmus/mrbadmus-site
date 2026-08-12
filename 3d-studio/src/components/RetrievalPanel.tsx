// §02 retrieval question panel. Stage 1 built the structure; Stage 6
// (MRB-191) makes Check, Skip and Reveal do what they say.
//
// The panel decides nothing. Grading, eligibility, what comes back at the end
// of the round and what a point is worth all live in `studio/retrieval.ts`,
// because the round has to run identically behind the mesh renderer and the
// flat one — which is impossible if the rules live in a view.

import { useEffect, useRef, useState } from 'react'
import type { SpecimenRecord } from '../studio/types'
import type { RoundState } from '../studio/retrieval'
import { currentQuestion, missedSoFar, roundScore } from '../studio/retrieval'

export interface RetrievalPanelProps {
  specimen: SpecimenRecord
  round: RoundState
  /** the full round length, so the six squares §02 draws match the queue */
  roundSize: number
  /** what the student just got right, if anything — the revealed label */
  revealed: { label: string; detail: string } | null
  onCheck: (answer: string) => void
  onSkip: () => void
  onReveal: () => void
  onNext: () => void
  /** set once the round is over and the visitor has spent their free one */
  gate: 'sign-in' | null
}

export function RetrievalPanel({
  specimen,
  round,
  roundSize,
  revealed,
  onCheck,
  onSkip,
  onReveal,
  onNext,
  gate,
}: RetrievalPanelProps) {
  const [answer, setAnswer] = useState('')
  const question = currentQuestion(round)
  const inputRef = useRef<HTMLInputElement>(null)

  // A new question is a new answer. Clearing on the question's id rather than
  // on the index means a structure that comes back at the end of the round
  // also arrives with an empty box.
  const questionKey = `${round.index}:${question?.hotspot.id ?? 'done'}`
  useEffect(() => {
    setAnswer('')
  }, [questionKey])

  const labels = new Map(specimen.hotspots.map((h) => [h.id, h.label]))
  const missed = missedSoFar(round)
  const score = roundScore(round.results)
  const done = round.results.filter((r) => r.attemptNo === 1).length

  return (
    <section className="rpanel" aria-label="Retrieval round">
      <div className="rpanel__head">
        <span className="rpanel__round">ROUND 1</span>
        <span className="rpanel__rule" aria-hidden="true" />
        <span className="rpanel__of">
          {Math.min(round.index + 1, roundSize)} OF {roundSize}
        </span>
      </div>

      <div className="progress" aria-label="Round progress">
        {Array.from({ length: roundSize }, (_, i) => {
          if (i < done) {
            const result = round.results[i]
            const got = result?.outcome === 'correct'
            return (
              <span
                key={i}
                className={`psq psq--done${got ? '' : ' psq--missed'}`}
                aria-label={got ? 'named' : 'missed'}
              >
                {got ? '✓' : '·'}
              </span>
            )
          }
          if (i === done && !round.complete) {
            return (
              <span key={i} className="psq psq--current" aria-current="step">
                {i + 1}
              </span>
            )
          }
          return <span key={i} className="psq psq--ahead" aria-hidden="true" />
        })}
      </div>

      {revealed ? (
        <div className="rreveal-card" role="status">
          <div className="rreveal-card__eyebrow">NAMED</div>
          <div className="rreveal-card__title">{revealed.label}</div>
          <div className="rreveal-card__detail">{revealed.detail}</div>
          <button type="button" className="rbtn-check" onClick={onNext}>
            Next structure
          </button>
        </div>
      ) : round.complete ? (
        <div className="rreveal-card" role="status">
          <div className="rreveal-card__eyebrow">ROUND COMPLETE</div>
          <div className="rreveal-card__title">
            {score.correct} of {score.asked}
          </div>
          {/* The sign-in moment (reference §03) mounts HERE and nowhere else.
              It is deliberately not built tonight: Design fully specified that
              screen — result before ask, scrim at 55%, one concrete reason,
              the next specimen in the footer — and it is the highest-value
              moment on the page, so it gets translated rather than improvised.
              What exists is the trigger: `gate` is 'sign-in' exactly when it
              is due. See studio/access.ts. */}
          <div hidden data-testid="round-gate">{gate ?? 'none'}</div>
        </div>
      ) : (
        <>
          <div className="rpanel__ask">NAME THE HIGHLIGHTED STRUCTURE</div>
          <form
            onSubmit={(e) => {
              e.preventDefault()
              onCheck(answer)
            }}
          >
            <div className="rinput">
              <input
                ref={inputRef}
                type="text"
                value={answer}
                placeholder="Type your answer"
                aria-label="Your answer"
                autoComplete="off"
                onChange={(e) => setAnswer(e.target.value)}
              />
              {answer === '' && <span className="rinput__caret" aria-hidden="true" />}
            </div>
            <div className="rpanel__actions">
              <button type="submit" className="rbtn-check">
                Check
              </button>
              <button type="button" className="rbtn-skip" onClick={onSkip}>
                Skip
              </button>
            </div>
          </form>
          <div className="rreveal">
            <span className="rreveal__q">Can't recall it?</span>
            <button type="button" className="rreveal__link" onClick={onReveal}>
              Reveal the label
            </button>
          </div>
        </>
      )}

      <div className="rmissed">
        <div className="rmissed__eyebrow">MISSED SO FAR</div>
        {missed.length > 0 && (
          <div className="rmissed__chips">
            {missed.map((id) => (
              <span key={id} className="rmissed__chip">
                {labels.get(id)}
              </span>
            ))}
          </div>
        )}
        <div className="rmissed__note">
          Missed structures come back at the end of the round.
        </div>
      </div>

      {/* the round draws only retrievable hotspots for this specimen */}
      <span hidden data-testid="round-specimen">{specimen.id}</span>
    </section>
  )
}
