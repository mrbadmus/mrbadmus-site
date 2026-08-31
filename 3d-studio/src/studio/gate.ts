/* MRB-305 — the "coming soon" gate. THE WHOLE SWITCH IS THE NEXT LINE.
 *
 * Ruled by Mide, 31 Aug 2026. The studio ships to students LOOKING finished
 * and BEING dead: the heart still loads, every word on the page stays
 * readable, and nothing inside the studio responds to a mouse, a finger, a
 * keyboard or a screen reader. Two words sit over it. The site header is the
 * one thing left alive, so a student who lands here can leave again.
 *
 * ── Lifting the gate is ONE edit: `true` → `false`. ──────────────────────
 *
 * Nothing else needs touching. The attribute, the dimming, the inerting and
 * the overlay are all downstream of this constant, and every one of them
 * disappears when it is false. That is deliberate — a gate that takes a
 * rebuild to lift is a gate somebody ships past.
 *
 * ⚠️ WHAT THIS IS NOT. It is not access control and does not pretend to be.
 * The page is public, the content behind it is a heart model and some
 * anatomy labels, and anyone who opens devtools can undim it. The gate
 * exists so that a student meets a finished product or nothing — not to
 * keep a secret, because there isn't one.
 */
export const COMING_SOON = true

/** The two words, in one place, because they are the entire copy. Mide's
 *  ruling is explicit that nothing joins them: no paragraph about what is
 *  coming, no date, no "check back later". */
export const COMING_SOON_WORDS = 'COMING SOON'

/** The gate's escape hatch, and it is NOT reachable from a URL — see
 *  `3d_parity.py` and `3d_render_check.py`, its only two callers.
 *
 *  Those gates drive the BUILT studio through CDP and assert its regions,
 *  its computed styles and its interactions. Every one of those assertions
 *  is about the studio itself and none of them stops being true because the
 *  studio is gated — so the harness lifts the gate in the page it is already
 *  driving, and goes on measuring the thing it was written to measure.
 *
 *  A query parameter would have done the same job and been reachable by a
 *  student typing one, which is the whole reason this is a window flag set
 *  over the debugger instead. */
export function gateLifted(): boolean {
  return typeof window !== 'undefined' &&
    (window as unknown as { __MRB_GATE_LIFTED__?: boolean }).__MRB_GATE_LIFTED__ === true
}
