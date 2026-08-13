// @vitest-environment node
// Gate 12 — the retrieval round, the attempts contract, and the access model
// (MRB-191).
//
// The round is the thing that makes 3D Studio an assessment surface rather
// than a decorative toy, and almost none of it is visual: eligibility,
// grading, what comes back at the end, what shape the evidence takes, and who
// is allowed to produce any. All of that is asserted here, driven through the
// same functions the shell drives, with an injected clock and an injected id
// so every client_key in this file is reproducible.
//
// The failures this is written against, in order of how expensive they would
// be to find later:
//
//   * an anonymous attempt becoming a row. Contract §1 forbids it; there are
//     two independent locks on that door and both are asserted.
//   * a client_key that is not unique per (user, item, attempt), which is what
//     stops a double-submit becoming two pieces of evidence and two points.
//   * a reveal counted as an attempt. Giving up is not evidence.
//   * a missed structure never coming back, or coming back forever.

import { describe, expect, it } from 'vitest'
import {
  answerQuestion,
  currentQuestion,
  eligibleHotspots,
  isCorrect,
  missedSoFar,
  normaliseAnswer,
  pointsFor,
  roundScore,
  startRound,
  type RoundDeps,
  type RoundState,
} from '../../src/studio/retrieval'
import {
  createMemoryAdapter,
  PROVISIONAL_ANONYMOUS_PROFILE,
  type LearnerProfile,
} from '../../src/studio/attempts'
import {
  canStartRound,
  completeRound,
  FREE_ANONYMOUS_ROUNDS,
  FRESH_ACCESS,
  shouldPersist,
} from '../../src/studio/access'
import type { HotspotRecord, SpecimenRecord } from '../../src/studio/types'

function hotspot(
  id: string,
  label: string,
  over: Partial<HotspotRecord> = {},
): HotspotRecord {
  return {
    id,
    label,
    detail: `detail for ${label}`,
    position3d: [0, 0, 0],
    position2d: [0, 0],
    tiers: ['foundation', 'higher'],
    retrievable: true,
    ...over,
  }
}

function specimen(hotspots: HotspotRecord[]): SpecimenRecord {
  return {
    id: 'test',
    renderer: 'mesh',
    name: 'Test',
    epithet: '',
    system: '',
    // Offered at both key stages so this file's fixtures stay about what this
    // file is about. The key-stage filter is real in `eligibleHotspots`
    // (MRB-193/186) and a KS4-only fixture would silently empty every round a
    // signed-in KS3 profile started here — which is the correct behaviour, and
    // is asserted where it belongs, in tests/gates/key-stage.test.ts.
    keyStages: ['KS3', 'KS4'],
    assets: {
      mesh: '', fallback: '', thumbnail: '', licence: '', source: '', acquired: '',
    },
    description: '',
    keyFacts: [],
    callouts: { importance: '', didYouKnow: '' },
    lessonUrl: '',
    specPoints: ['KS4.B.ORG.04', 'KS3.B.BOD.02'],
    hotspots,
  }
}

/** A clock that only moves when the test moves it. */
function clock(start = 1000) {
  let t = start
  return { now: () => t, advance: (ms: number) => (t += ms) }
}

function deps(over: Partial<RoundDeps> = {}): RoundDeps {
  return {
    now: () => 1000,
    roundId: 'round-1',
    profile: PROVISIONAL_ANONYMOUS_PROFILE,
    submitter: createMemoryAdapter(),
    ...over,
  }
}

const SIGNED_IN: LearnerProfile = {
  userId: 'user-abc',
  pathway: 'triple',
  tier: 'higher',
  keyStage: 'KS4',
}

describe('gate 12 — eligibility', () => {
  it('only retrievable hotspots are asked about', () => {
    const s = specimen([
      hotspot('a', 'Alpha'),
      hotspot('b', 'Beta', { retrievable: false }),
    ])
    expect(eligibleHotspots(s, PROVISIONAL_ANONYMOUS_PROFILE).map((h) => h.id)).toEqual(['a'])
  })

  it('a tier that does not match is not asked about', () => {
    const s = specimen([
      hotspot('a', 'Alpha', { tiers: ['higher'] }),
      hotspot('b', 'Beta', { tiers: ['foundation'] }),
    ])
    const foundation = { ...PROVISIONAL_ANONYMOUS_PROFILE, tier: 'foundation' as const }
    const higher = { ...PROVISIONAL_ANONYMOUS_PROFILE, tier: 'higher' as const }
    expect(eligibleHotspots(s, foundation).map((h) => h.id)).toEqual(['b'])
    expect(eligibleHotspots(s, higher).map((h) => h.id)).toEqual(['a'])
  })

  it('a KS3 learner has no tier, and is asked about everything retrievable', () => {
    const s = specimen([
      hotspot('a', 'Alpha', { tiers: ['higher'] }),
      hotspot('b', 'Beta', { tiers: ['foundation'] }),
      hotspot('c', 'Gamma', { retrievable: false }),
    ])
    const ks3: LearnerProfile = {
      userId: null, pathway: 'combined', tier: null, keyStage: 'KS3',
    }
    expect(eligibleHotspots(s, ks3).map((h) => h.id)).toEqual(['a', 'b'])
  })
})

describe('gate 12 — grading is exact, and stays out of marking decisions', () => {
  const h = hotspot('a', 'Left ventricle')

  it('accepts the label back, however it was typed', () => {
    expect(isCorrect('Left ventricle', h)).toBe(true)
    expect(isCorrect('  left   VENTRICLE ', h)).toBe(true)
    expect(isCorrect('left ventricle.', h)).toBe(true)
  })

  it('rejects an empty answer', () => {
    expect(isCorrect('', h)).toBe(false)
    expect(isCorrect('   ', h)).toBe(false)
  })

  it('rejects a different structure', () => {
    expect(isCorrect('right ventricle', h)).toBe(false)
  })

  it('does NOT accept an abbreviation — that is a marking decision', () => {
    // Deliberately asserted. Whether "LV" is a credit-worthy answer is
    // examiner judgement and belongs to Mide, not to a normaliser.
    expect(isCorrect('LV', h)).toBe(false)
  })

  it('normalisation touches case, space and punctuation and nothing else', () => {
    expect(normaliseAnswer('  The,  Left--Ventricle!  ')).toBe('the left--ventricle')
  })
})

describe('gate 12 — authored alternatives are accepted, and only authored ones', () => {
  // A TEST FIXTURE, not content. The real alternatives are authored in the
  // content record by Mide at the science gate; nothing here derives one.
  const withAccept = hotspot('a', 'Left ventricle', {
    accept: ['Left ventricle chamber'],
  })
  const withoutAccept = hotspot('a', 'Left ventricle')

  it('an authored alternative is accepted', () => {
    expect(isCorrect('Left ventricle chamber', withAccept)).toBe(true)
  })

  it('the label is still accepted alongside it', () => {
    expect(isCorrect('Left ventricle', withAccept)).toBe(true)
  })

  it('an alternative matches under the same normalisation as the label', () => {
    expect(isCorrect('  left   VENTRICLE  chamber ', withAccept)).toBe(true)
    expect(isCorrect('left ventricle chamber.', withAccept)).toBe(true)
  })

  it('an empty answer is still wrong, alternatives or not', () => {
    expect(isCorrect('', withAccept)).toBe(false)
    expect(isCorrect('   ', withAccept)).toBe(false)
  })

  it('an alternative NOT on the list is not accepted — nothing is derived', () => {
    expect(isCorrect('LV', withAccept)).toBe(false)
    expect(isCorrect('ventricle', withAccept)).toBe(false)
  })

  it('a hotspot with no accept field grades exactly as before', () => {
    expect(isCorrect('Left ventricle', withoutAccept)).toBe(true)
    expect(isCorrect('  left   VENTRICLE ', withoutAccept)).toBe(true)
    expect(isCorrect('Left ventricle chamber', withoutAccept)).toBe(false)
    expect(isCorrect('', withoutAccept)).toBe(false)
  })
})

describe('gate 12 — the round asks, marks, and brings the missed back', () => {
  const s = specimen([hotspot('a', 'Alpha'), hotspot('b', 'Beta')])

  it('asks every eligible structure once, in record order', () => {
    const round = startRound(s, deps())
    expect(round.queue.map((q) => q.hotspot.id)).toEqual(['a', 'b'])
    expect(round.queue.every((q) => q.attemptNo === 1)).toBe(true)
    expect(round.complete).toBe(false)
  })

  it('a missed structure comes back at the END, not immediately', () => {
    const d = deps()
    let round = startRound(s, d)
    round = answerQuestion(round, s, 'wrong', 'nope', d).round
    // still the first pass — 'a' has not jumped the queue
    expect(currentQuestion(round)?.hotspot.id).toBe('b')
    round = answerQuestion(round, s, 'correct', 'Beta', d).round
    expect(round.complete).toBe(false)
    expect(currentQuestion(round)?.hotspot.id).toBe('a')
    expect(currentQuestion(round)?.attemptNo).toBe(2)
  })

  it('and comes back only once — a second miss does not loop forever', () => {
    const d = deps()
    let round: RoundState = startRound(s, d)
    round = answerQuestion(round, s, 'wrong', 'x', d).round
    round = answerQuestion(round, s, 'wrong', 'y', d).round
    round = answerQuestion(round, s, 'wrong', 'z', d).round
    round = answerQuestion(round, s, 'wrong', 'w', d).round
    expect(round.complete).toBe(true)
    expect(currentQuestion(round)).toBeNull()
  })

  it('MISSED SO FAR lists what was asked and not got, once each', () => {
    const d = deps()
    let round = startRound(s, d)
    round = answerQuestion(round, s, 'wrong', 'x', d).round
    expect(missedSoFar(round)).toEqual(['a'])
    round = answerQuestion(round, s, 'correct', 'Beta', d).round
    expect(missedSoFar(round)).toEqual(['a'])
    round = answerQuestion(round, s, 'correct', 'Alpha', d).round
    expect(missedSoFar(round)).toEqual([])
  })

  it('scores the first pass, not the retries', () => {
    const d = deps()
    let round = startRound(s, d)
    round = answerQuestion(round, s, 'wrong', 'x', d).round
    round = answerQuestion(round, s, 'correct', 'Beta', d).round
    round = answerQuestion(round, s, 'correct', 'Alpha', d).round
    expect(roundScore(round.results)).toEqual({ correct: 1, asked: 2 })
    // and a structure got on the second look earns no point
    expect(pointsFor(round.results)).toBe(1)
  })

  it('a specimen with nothing eligible produces a round that is already over', () => {
    const barren = specimen([hotspot('a', 'Alpha', { retrievable: false })])
    expect(startRound(barren, deps()).complete).toBe(true)
  })
})

describe('gate 12 — the attempt payload is the contract, field for field', () => {
  const s = specimen([hotspot('a', 'Alpha')])

  it('carries every column the contract names', () => {
    const c = clock()
    const d = deps({ now: c.now, profile: SIGNED_IN })
    const round = startRound(s, d)
    c.advance(2400)
    const { attempt } = answerQuestion(round, s, 'correct', 'Alpha', d)

    expect(attempt).toEqual({
      user_id: 'user-abc',
      source: '3d-studio',
      item_type: 'hotspot',
      item_ref: 'a',
      spec_points: ['KS4.B.ORG.04', 'KS3.B.BOD.02'],
      pathway: 'triple',
      tier: 'higher',
      key_stage: 'KS4',
      correct: true,
      latency_ms: 2400,
      confidence: null,
      attempt_no: 1,
      response: 'Alpha',
      client_key: 'round-1:a:1',
    })
  })

  it('spec_points come from the HOTSPOT where it declares its own', () => {
    const own = specimen([
      hotspot('a', 'Alpha', { specPoints: ['KS4.B.ORG.09'] }),
    ])
    const d = deps({ profile: SIGNED_IN })
    const round = startRound(own, d)
    const { attempt } = answerQuestion(round, own, 'correct', 'Alpha', d)
    expect(attempt?.spec_points).toEqual(['KS4.B.ORG.09'])
  })

  it('and fall back to the specimen where the hotspot declares none', () => {
    const d = deps({ profile: SIGNED_IN })
    const round = startRound(s, d)
    const { attempt } = answerQuestion(round, s, 'correct', 'Alpha', d)
    expect(attempt?.spec_points).toEqual(['KS4.B.ORG.04', 'KS3.B.BOD.02'])
  })

  it('confidence is always null from this surface (contract §6 item 3)', () => {
    const d = deps({ profile: SIGNED_IN })
    const round = startRound(s, d)
    expect(answerQuestion(round, s, 'wrong', 'x', d).attempt?.confidence).toBeNull()
  })

  it('a KS3 row carries a null tier, never a fake foundation (§6 item 2)', () => {
    const ks3: LearnerProfile = {
      userId: 'u', pathway: 'combined', tier: null, keyStage: 'KS3',
    }
    const d = deps({ profile: ks3 })
    const round = startRound(s, d)
    const { attempt } = answerQuestion(round, s, 'correct', 'Alpha', d)
    expect(attempt?.tier).toBeNull()
    expect(attempt?.key_stage).toBe('KS3')
  })

  it('client_key is unique per round, item and attempt number', () => {
    const two = specimen([hotspot('a', 'Alpha'), hotspot('b', 'Beta')])
    const d = deps({ profile: SIGNED_IN })
    let round = startRound(two, d)
    const keys: string[] = []
    for (let i = 0; i < 4 && !round.complete; i += 1) {
      const step = answerQuestion(round, two, 'wrong', 'x', d)
      if (step.attempt) keys.push(step.attempt.client_key)
      round = step.round
    }
    expect(new Set(keys).size).toBe(keys.length)
    expect(keys).toContain('round-1:a:1')
    expect(keys).toContain('round-1:a:2')
  })

  it('a REVEAL produces no payload — giving up is not an attempt (§1)', () => {
    const d = deps({ profile: SIGNED_IN })
    const round = startRound(s, d)
    const step = answerQuestion(round, s, 'revealed', '', d)
    expect(step.attempt).toBeNull()
    // but the round still knows not to ask again
    expect(step.round.results[0].outcome).toBe('revealed')
  })

  it('a skip is an attempt with no response', () => {
    const d = deps({ profile: SIGNED_IN })
    const round = startRound(s, d)
    const step = answerQuestion(round, s, 'skipped', '', d)
    expect(step.attempt?.correct).toBe(false)
    expect(step.attempt?.response).toBeNull()
  })
})

describe('gate 12 — nothing anonymous is ever recorded', () => {
  const s = specimen([hotspot('a', 'Alpha')])

  it('the store drops a payload with no user, whoever built it', async () => {
    const store = createMemoryAdapter()
    const d = deps({ submitter: store })
    const round = startRound(s, d)
    const { attempt } = answerQuestion(round, s, 'correct', 'Alpha', d)
    expect(attempt).not.toBeNull()
    await store.submit(attempt!)
    expect(store.rows).toHaveLength(0)
  })

  it('and the shell would not have offered it one either', () => {
    expect(shouldPersist(PROVISIONAL_ANONYMOUS_PROFILE)).toBe(false)
    expect(shouldPersist(SIGNED_IN)).toBe(true)
  })

  it('a signed-in attempt IS recorded', async () => {
    const store = createMemoryAdapter()
    const d = deps({ submitter: store, profile: SIGNED_IN })
    const round = startRound(s, d)
    const { attempt } = answerQuestion(round, s, 'correct', 'Alpha', d)
    await store.submit(attempt!)
    expect(store.rows).toHaveLength(1)
    expect(store.rows[0].item_ref).toBe('a')
  })

  it('a double-submit produces one row, not two (idempotency, §2)', async () => {
    const store = createMemoryAdapter()
    const d = deps({ submitter: store, profile: SIGNED_IN })
    const round = startRound(s, d)
    const { attempt } = answerQuestion(round, s, 'correct', 'Alpha', d)
    await store.submit(attempt!)
    await store.submit(attempt!)
    await store.submit({ ...attempt! })
    expect(store.rows).toHaveLength(1)
  })
})

describe('gate 12 — one free round, then the prompt', () => {
  it('an anonymous visitor may start exactly one', () => {
    expect(FREE_ANONYMOUS_ROUNDS).toBe(1)
    let access = FRESH_ACCESS
    expect(canStartRound(access, PROVISIONAL_ANONYMOUS_PROFILE)).toBe(true)

    const done = completeRound(access, PROVISIONAL_ANONYMOUS_PROFILE)
    access = done.access
    // the gate is due AFTER the round: the result is theirs first (§03)
    expect(done.gate).toBe('sign-in')
    expect(canStartRound(access, PROVISIONAL_ANONYMOUS_PROFILE)).toBe(false)
  })

  it('a signed-in student is never gated', () => {
    let access = FRESH_ACCESS
    for (let i = 0; i < 5; i += 1) {
      expect(canStartRound(access, SIGNED_IN)).toBe(true)
      const done = completeRound(access, SIGNED_IN)
      access = done.access
      expect(done.gate).toBeNull()
    }
  })
})
