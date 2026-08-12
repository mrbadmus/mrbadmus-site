// Who may take a retrieval round, and when the sign-in moment is due
// (MRB-191, Stage 6).
//
// Spec §6: exploration is fully open and needs no account; an anonymous
// visitor gets ONE free retrieval round, so the mechanic proves itself before
// any wall; the prompt comes after that; scoring persists only for signed-in
// users.
//
// ─────────────────────────────────────────────────────────────────────────────
// STRUCTURED, NOT WIRED.
//
// This module decides WHEN the sign-in moment is due. It does not render it
// and it does not call an auth flow. §03 of the frozen reference fully
// specifies that screen — result before ask, scrim at 55%, one concrete
// reason, the next specimen in the footer — and it is the highest-value moment
// on the page. It is deliberately not improvised here; the shell reaches
// `gate === 'sign-in'` and stops, which is the trigger built and the screen
// left, exactly as the run was scoped.
//
// Nothing in this file touches storage. An anonymous round is counted in
// memory for the life of the tab, which is what "one free attempt" means when
// nothing about the visitor is recorded (contract §1: anonymous attempts
// produce no row, and nothing personal is captured pre-sign-in).
// ─────────────────────────────────────────────────────────────────────────────

import type { LearnerProfile } from './attempts'

/** How many rounds an anonymous visitor may complete before the prompt.
 *
 * ONE, and one ROUND rather than one question: §03 shows the moment carrying a
 * score, per-structure marks and a time, which is a completed round's result,
 * and MRB-191 is explicit that a hard wall on first click "reads as bait and
 * wastes the best conversion moment on the page". */
export const FREE_ANONYMOUS_ROUNDS = 1

export interface AccessState {
  /** rounds this visitor has finished without an account, this tab */
  anonymousRoundsDone: number
}

export const FRESH_ACCESS: AccessState = { anonymousRoundsDone: 0 }

export function isSignedIn(profile: LearnerProfile): boolean {
  return profile.userId !== null
}

/** May this person start another round? */
export function canStartRound(
  access: AccessState,
  profile: LearnerProfile,
): boolean {
  if (isSignedIn(profile)) return true
  return access.anonymousRoundsDone < FREE_ANONYMOUS_ROUNDS
}

/** Record a completed round and say whether the sign-in moment is now due.
 *
 * Due AFTER the round, never before it: the result is theirs first (§03,
 * "RESULT BEFORE ASK"). */
export function completeRound(
  access: AccessState,
  profile: LearnerProfile,
): { access: AccessState; gate: 'sign-in' | null } {
  if (isSignedIn(profile)) return { access, gate: null }
  const next = { anonymousRoundsDone: access.anonymousRoundsDone + 1 }
  return {
    access: next,
    gate: next.anonymousRoundsDone >= FREE_ANONYMOUS_ROUNDS ? 'sign-in' : null,
  }
}

/** Whether a completed round's attempts are worth submitting at all.
 *
 * Spec §6: "Scoring persists only for signed-in users." The submitter drops
 * anonymous payloads too (contract §1), so this is the second of two locks on
 * the same door — deliberately, because the two are in different files and
 * either one going wrong alone must not produce a row. */
export function shouldPersist(profile: LearnerProfile): boolean {
  return isSignedIn(profile)
}
