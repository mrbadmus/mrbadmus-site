// The identify-the-structure round (MRB-191, Stage 6).
//
// Labels are hidden, one structure is highlighted, the student names it by
// typing, and a correct identification reveals the label and the detail text.
// All of that is state and arithmetic, so all of it is here rather than in a
// component: the round runs identically behind the mesh renderer and the flat
// one, which is spec §6's requirement and impossible to honour if the rules
// live in a view.
//
// WHAT IS DELIBERATELY NOT HERE: any judgement about science. Grading compares
// what the student typed against the hotspot's own `label` and against the
// hotspot's `accept` list if it has one, normalised for case, punctuation and
// spacing, and nothing else. No "close enough".
//
// That `accept` list is AUTHORED, never computed (MRB-193). Every alternative
// on it is written down by Mide under the science gate; an alternative that is
// not written down is not accepted. Nothing here derives one — no stemming, no
// fuzzy matching, no abbreviation expansion. Whether "left ventricle" and "LV"
// are the same answer is a marking decision, and marking decisions are Mide's.

import type { HotspotRecord, SpecimenRecord } from './types'
import type { AttemptPayload, AttemptSubmitter, LearnerProfile } from './attempts'
import { viewingKeyStage, visibleHotspots } from './content'

export type QuestionOutcome = 'correct' | 'wrong' | 'skipped' | 'revealed'

export interface RoundQuestion {
  hotspot: HotspotRecord
  /** 1 = first time this structure has been asked in this round */
  attemptNo: number
}

export interface RoundResult {
  hotspotId: string
  outcome: QuestionOutcome
  response: string
  latencyMs: number | null
  attemptNo: number
}

export interface RoundState {
  /** stable id for this round; every client_key is derived from it */
  id: string
  specimenId: string
  /** the structures the round will ask about, in order */
  queue: RoundQuestion[]
  /** how far through `queue` we are */
  index: number
  results: RoundResult[]
  /** ids asked and not got, waiting to come back at the end of the round */
  missed: string[]
  /** true once the queue and its tail of missed structures are exhausted */
  complete: boolean
  /** when the current question was presented, from the injected clock */
  askedAt: number
}

/** Everything the round needs from outside itself, so it can be driven in a
 * test without a browser, a timer, or a random number. */
export interface RoundDeps {
  /** ms since some epoch; only differences are used */
  now: () => number
  /** a stable id for the round — NOT generated here, because a round that
   * invented its own would be untestable and its client_keys unreproducible */
  roundId: string
  profile: LearnerProfile
  submitter: AttemptSubmitter
}

/**
 * Eligibility. TWO filters, and they are not the same filter.
 *
 * KEY STAGE decides whether the structure exists for this student at all. A
 * hotspot's own `keyStages` win and it inherits the specimen's where it
 * declares none (MRB-193's mechanism, resolved in studio/content.ts). This is
 * applied HERE and not merely by the shell: a KS3 learner must never be asked
 * to name a structure they cannot see, and that guarantee has to hold for
 * every caller, not only for the one that happens to pre-filter today.
 *
 * It is derived through `viewingKeyStage`, the same derivation the shell uses,
 * so what is asked and what is on the stage cannot come apart. An anonymous
 * visitor filters by nothing and is asked about everything — they can see
 * everything too, so the guarantee holds.
 *
 * TIER differentiates within a key stage, spec §6: "Only hotspots with
 * `retrievable: true` and a `tiers` value matching the student's pathway are
 * eligible." Read carefully, that sentence says pathway but names `tiers`, and
 * `tiers` in the content schema holds foundation|higher. The schema is what the
 * studio can act on, so eligibility matches the TIER. A KS3 learner has no tier
 * at all (contract §6 item 2), and for them every retrievable hotspot they can
 * see is eligible — the alternative is a KS3 round that silently excludes
 * everything.
 */
export function eligibleHotspots(
  specimen: SpecimenRecord,
  profile: LearnerProfile,
): HotspotRecord[] {
  return visibleHotspots(specimen, viewingKeyStage(profile)).filter((hotspot) => {
    if (!hotspot.retrievable) return false
    if (profile.tier === null) return true
    return hotspot.tiers.includes(profile.tier)
  })
}

/**
 * A round is SPECIMEN-LENGTH: every eligible structure, asked once, with the
 * missed ones returning at the end.
 *
 * This is a real pedagogical choice and Mide may reverse it. Design drew six
 * progress squares, which implies a fixed round length; against that, spec §6
 * describes eligibility as a property of the specimen's own hotspots, and a
 * fixed six would mean either padding a small specimen with repeats or
 * truncating a large one and never asking about the rest. Specimen-length is
 * also what the parity gate already counts (one square per retrievable
 * hotspot), so the drawn round and the built one agree today. Flagged in the
 * Stage 6 report as a decision, not a detail.
 */
export function startRound(
  specimen: SpecimenRecord,
  deps: RoundDeps,
): RoundState {
  const queue = eligibleHotspots(specimen, deps.profile).map((hotspot) => ({
    hotspot,
    attemptNo: 1,
  }))
  return {
    id: deps.roundId,
    specimenId: specimen.id,
    queue,
    index: 0,
    results: [],
    missed: [],
    complete: queue.length === 0,
    askedAt: deps.now(),
  }
}

export function currentQuestion(round: RoundState): RoundQuestion | null {
  return round.queue[round.index] ?? null
}

/** Normalised for comparison: case, surrounding space, inner runs of space,
 * and the punctuation a student types without thinking. Nothing else — see the
 * header note on why there is no synonym handling here. */
export function normaliseAnswer(value: string): string {
  return value
    .toLowerCase()
    .replace(/[.,;:!?'"`()[\]{}]/g, '')
    .replace(/[‐-―]/g, '-')
    .replace(/\s+/g, ' ')
    .trim()
}

export function isCorrect(response: string, hotspot: HotspotRecord): boolean {
  const given = normaliseAnswer(response)
  if (given === '') return false
  if (given === normaliseAnswer(hotspot.label)) return true
  // The authored alternatives, compared under exactly the same normalisation
  // as the label — a hotspot with no `accept` list grades on the label alone.
  return (hotspot.accept ?? []).some((alt) => given === normaliseAnswer(alt))
}

/**
 * Points, computed and NOT persisted (MRB-191 scope). One point for naming a
 * structure at the first time of asking; a structure that comes back at the
 * end of the round because it was missed earns nothing, because the evidence
 * it produces is "needed a second look" rather than "knew it".
 *
 * PROVISIONAL. The reward layer is MRB-148's, and the attempts contract is
 * explicit (§3) that no points column belongs on the row — this is a display
 * number until that layer exists.
 */
export function pointsFor(results: readonly RoundResult[]): number {
  return results.filter((r) => r.outcome === 'correct' && r.attemptNo === 1).length
}

export function roundScore(results: readonly RoundResult[]): {
  correct: number
  asked: number
} {
  const firstPass = results.filter((r) => r.attemptNo === 1)
  return {
    correct: firstPass.filter((r) => r.outcome === 'correct').length,
    asked: firstPass.length,
  }
}

/** Hotspot-level specPoints win; a hotspot without them inherits the
 * specimen's (MRB-193). */
function resolveSpecPoints(
  specimen: SpecimenRecord,
  hotspot: HotspotRecord,
): readonly string[] {
  const own = hotspot.specPoints
  return Array.isArray(own) && own.length > 0 ? own : specimen.specPoints
}

/** Build the contract-shaped payload for one graded response. */
export function buildAttempt(
  specimen: SpecimenRecord,
  question: RoundQuestion,
  outcome: QuestionOutcome,
  response: string,
  latencyMs: number | null,
  deps: RoundDeps,
): AttemptPayload {
  return {
    user_id: deps.profile.userId,
    source: '3d-studio',
    item_type: 'hotspot',
    item_ref: question.hotspot.id,
    // Contract §2 wants the statement ids the ITEM serves, denormalised at
    // attempt time. MRB-193 closed the gap by adding an optional per-hotspot
    // specPoints: a hotspot's own list wins where it declares one, and where
    // it does not the hotspot inherits the specimen's.
    spec_points: [...resolveSpecPoints(specimen, question.hotspot)],
    pathway: deps.profile.pathway,
    tier: deps.profile.tier,
    key_stage: deps.profile.keyStage,
    correct: outcome === 'correct',
    latency_ms: latencyMs,
    // Contract §6 item 3: not asked inside the identify round.
    confidence: null,
    attempt_no: question.attemptNo,
    response: response === '' ? null : response,
    // Deterministic and unique per user: same round, same structure, same
    // attempt number can only ever be one row (contract §2 idempotency).
    client_key: `${deps.roundId}:${question.hotspot.id}:${question.attemptNo}`,
  }
}

/**
 * Grade the current question and move on.
 *
 * A REVEAL IS NOT AN ATTEMPT (contract §1: "Giving up and revealing the answer
 * is not an attempt"), so it produces no payload and is not submitted. It is
 * still recorded in the round's own results, because the round has to know not
 * to ask again.
 */
export function answerQuestion(
  round: RoundState,
  specimen: SpecimenRecord,
  outcome: QuestionOutcome,
  response: string,
  deps: RoundDeps,
): { round: RoundState; attempt: AttemptPayload | null } {
  const question = currentQuestion(round)
  if (!question || round.complete) return { round, attempt: null }

  const now = deps.now()
  const latencyMs = Math.max(0, now - round.askedAt)

  const result: RoundResult = {
    hotspotId: question.hotspot.id,
    outcome,
    response,
    latencyMs,
    attemptNo: question.attemptNo,
  }

  const attempt =
    outcome === 'revealed'
      ? null
      : buildAttempt(specimen, question, outcome, response, latencyMs, deps)

  // Missed structures come back at the END of the round, and only once: a
  // structure already on its second pass does not queue a third.
  const missedAgain =
    outcome !== 'correct' && question.attemptNo === 1
      ? [...round.missed, question.hotspot.id]
      : round.missed

  let queue = round.queue
  let index = round.index + 1
  let missed = missedAgain
  let complete = false

  if (index >= queue.length) {
    if (missed.length > 0) {
      const returning = missed
        .map((id) => specimen.hotspots.find((h) => h.id === id))
        .filter((h): h is HotspotRecord => Boolean(h))
        .map((hotspot) => ({ hotspot, attemptNo: 2 }))
      queue = [...queue, ...returning]
      missed = []
    } else {
      complete = true
      index = queue.length
    }
  }

  return {
    round: {
      ...round,
      queue,
      index,
      results: [...round.results, result],
      missed,
      complete,
      askedAt: now,
    },
    attempt,
  }
}

/** Structures asked and not got, for the MISSED SO FAR list (§02). */
export function missedSoFar(round: RoundState): string[] {
  const got = new Set(
    round.results.filter((r) => r.outcome === 'correct').map((r) => r.hotspotId),
  )
  const seen = new Set<string>()
  const out: string[] = []
  for (const result of round.results) {
    if (got.has(result.hotspotId) || seen.has(result.hotspotId)) continue
    seen.add(result.hotspotId)
    out.push(result.hotspotId)
  }
  return out
}
