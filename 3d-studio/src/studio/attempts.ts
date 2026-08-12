// The retrieval attempt payload, and where it goes (MRB-191, Stage 6).
//
// The shape is the Retrieval Attempts Contract v1, locked at Stage 0 and
// inherited by MRB-148. It is mirrored here field for field, in the contract's
// own snake_case, deliberately: this object is a database row in waiting, and
// a client-side rename is how a contract quietly becomes two contracts.
//
// ─────────────────────────────────────────────────────────────────────────────
// NOTHING IS WRITTEN ANYWHERE TONIGHT.
//
// The table, its RLS and the real submitter are a later stage with Mide
// present. What exists here is the payload and an INJECTABLE interface to hand
// it to; the only implementation is an in-memory adapter that keeps rows in a
// list and forgets them when the tab closes. No Supabase client, no network
// call, no DDL.
// ─────────────────────────────────────────────────────────────────────────────

import type { KeyStage, Tier } from './types'

export type Pathway = 'combined' | 'triple'

/** Which surface produced the attempt. Contract §2: the field that makes the
 * shape survive growth. */
export type AttemptSource = '3d-studio' | 'page-quiz' | 'weekly-challenge'

/** Contract §2: `item_type` and `item_ref` together are the generic addressing
 * scheme, and the reason the row is not 3D-Studio-shaped. */
export type ItemType = 'hotspot' | 'question' | 'structure'

/** Who is answering. Captured at attempt time, never read from the profile at
 * query time — a student who moves from Foundation to Higher must not have
 * their history retroactively reinterpreted (contract §2). */
export interface LearnerProfile {
  /** null until sign-in is wired; the submitter fills it from the session and
   * the contract's row requires it, so a null here can never become a row. */
  userId: string | null
  pathway: Pathway
  /** null for KS3 — see PROVISIONAL below */
  tier: Tier | null
  keyStage: KeyStage
}

/**
 * PROVISIONAL — three open items on the contract (§6) need Mide's ruling, and
 * until they have one this is what the studio assumes. Every one of them is
 * the contract's own stated recommendation, implemented rather than invented:
 *
 *  1. VOCABULARY. `pathway` as combined|triple and `tier` as
 *     foundation|higher, matching what `profiles` already stores
 *     (`science_pathway` / `tier` in the Supabase schema). One vocabulary,
 *     not two. If the existing columns differ, this contract adopts theirs.
 *  2. KS3 TIER. Nullable, and null for KS3 rows, because a fake `foundation`
 *     would quietly corrupt any future KS3 tier analysis.
 *  3. CONFIDENCE. Not asked inside the identify round — it would break the
 *     rhythm of a fast retrieval mode — so `confidence` is always null from
 *     this surface. The field stays in the shape so page quizzes can use it.
 *
 * The profile below is also provisional in a second, larger sense: THERE IS NO
 * AUTH WIRED. Nothing reads a real account. These are the values an anonymous
 * visitor is treated as having so that the mechanic can run end to end, and
 * they must be replaced by the signed-in profile before a single row is
 * written.
 */
export const PROVISIONAL_ANONYMOUS_PROFILE: LearnerProfile = {
  userId: null,
  pathway: 'combined',
  tier: 'foundation',
  keyStage: 'KS4',
}

/** One graded response. Contract §2, field for field. */
export interface AttemptPayload {
  /** null until sign-in is wired; the contract's column is NOT NULL, which is
   * what stops an anonymous attempt from ever becoming a row (contract §1). */
  user_id: string | null
  source: AttemptSource
  item_type: ItemType
  item_ref: string
  spec_points: string[]
  pathway: Pathway
  tier: Tier | null
  key_stage: KeyStage
  correct: boolean
  /** null when untimed */
  latency_ms: number | null
  /** 1..5, null when not asked — always null from this surface, see above */
  confidence: number | null
  /** 1 = first ever for this item */
  attempt_no: number
  /** what the student actually gave; contract §2 calls this where misconception
   * analysis comes from later, and worthless if not captured now */
  response: string | null
  /** idempotency: unique per (user, key). Contract §2. */
  client_key: string
}

/** Where a built payload is handed. Injectable because tonight there is
 * nothing real to hand it to, and because the thing that IS real later — a
 * Supabase insert under RLS — must be swappable without the round knowing. */
export interface AttemptSubmitter {
  submit(attempt: AttemptPayload): Promise<void>
}

export interface MemoryAdapter extends AttemptSubmitter {
  /** everything submitted this session, in order */
  readonly rows: readonly AttemptPayload[]
  clear(): void
}

/**
 * The only implementation tonight. Keeps rows in a list, enforces the
 * contract's idempotency rule locally so the round is written against the real
 * constraint rather than a looser one, and writes to nothing.
 *
 * Contract §1: anonymous attempts produce NO row. That rule lives here rather
 * than in the round, because it is a property of the store: a payload with no
 * user_id is dropped, whoever built it and for whatever reason.
 */
export function createMemoryAdapter(): MemoryAdapter {
  const rows: AttemptPayload[] = []
  const keys = new Set<string>()

  return {
    rows,
    async submit(attempt: AttemptPayload) {
      // Contract §1: "Anonymous attempts. Exploration is open and the one free
      // anonymous retrieval round produces no row."
      if (!attempt.user_id) return
      // Contract §2: unique (user_id, client_key). A double-submit, a flaky
      // retry, or a student mashing the button produces one row, not three.
      const key = `${attempt.user_id}:${attempt.client_key}`
      if (keys.has(key)) return
      keys.add(key)
      rows.push(attempt)
    },
    clear() {
      rows.length = 0
      keys.clear()
    },
  }
}
