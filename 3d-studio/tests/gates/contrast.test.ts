// Gate 6 — WCAG contrast, computed from the token file on every run.
//
// Three of Design's caption-tier values were darkened in the MRB-186
// reconciliation because they failed 4.5:1 on the cream ground. Nothing
// stopped the next value regressing the same way — this gate does. It parses
// src/styles/tokens.css, computes the WCAG relative-luminance ratio for every
// foreground/background pair the shell actually uses (the pair table below is
// read off studio.css usage, with the px size each pair carries), and fails
// when text below 24px sits under 4.5:1 or ANY text sits under 3.0:1.
//
// Ratios are NEVER hardcoded — a token edit changes the numbers on the next
// run. Some pairs carry a `licence`: a reference-authored value that measures
// between 3.0 and 4.5 at body size, tolerated with a written reason because
// repainting it is a Design/Mide ruling, not an engineering fix (the same
// standing the caption tier had before Finding 1 ruled on it). A licence is
// not a pass list: the licensed pair still holds the 3.0 floor, and its
// `measured` value pins the authoring-time ratio so silent degradation fails
// too. Hotspot ring/halo contrast is the no-hue-only gate's territory (§07);
// this gate covers the type.

import { readFileSync } from 'node:fs'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { describe, expect, it } from 'vitest'

const here = dirname(fileURLToPath(import.meta.url))
const tokensCss = readFileSync(resolve(here, '../../src/styles/tokens.css'), 'utf8')

// ── token parsing ─────────────────────────────────────────────

const TOKENS: Record<string, string> = {}
for (const m of tokensCss.matchAll(/(--st-[a-z0-9-]+)\s*:\s*(#[0-9A-Fa-f]{6})\s*;/g)) {
  TOKENS[m[1]] = m[2]
}

/** Resolve a token name to its hex, failing loudly on a rename. */
function t(name: string): string {
  const hex = TOKENS[name]
  if (!hex) throw new Error(`token ${name} not found in tokens.css — renamed or removed?`)
  return hex
}

// ── WCAG maths ────────────────────────────────────────────────

function rgb(hex: string): [number, number, number] {
  const h = hex.replace('#', '')
  return [parseInt(h.slice(0, 2), 16), parseInt(h.slice(2, 4), 16), parseInt(h.slice(4, 6), 16)]
}

function lin(c: number): number {
  const s = c / 255
  return s <= 0.04045 ? s / 12.92 : ((s + 0.055) / 1.055) ** 2.4
}

function luminance(hex: string): number {
  const [r, g, b] = rgb(hex)
  return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)
}

function contrast(a: string, b: string): number {
  const la = luminance(a)
  const lb = luminance(b)
  const [hi, lo] = la > lb ? [la, lb] : [lb, la]
  return (hi + 0.05) / (lo + 0.05)
}

/** Composite `rgba(fg, alpha)` over an opaque ground — the rail, chip and
 * callout grounds are translucent ink over the stage gradient. */
function over(fgHex: string, alpha: number, bgHex: string): string {
  const f = rgb(fgHex)
  const b = rgb(bgHex)
  const mix = f.map((c, i) => Math.round(alpha * c + (1 - alpha) * b[i]))
  return '#' + mix.map((c) => c.toString(16).padStart(2, '0')).join('')
}

// grounds studio.css builds outside the token file
const STAGE_DARKEST = '#100D0A' // viewport gradient outer stop — the ground under hint/chip/callout
const RAIL_GROUND = over('#16120E', 0.9, '#191510') // rgba(22,18,14,.9) over gradient mid
const CHIP_GROUND = over('#16120E', 0.86, STAGE_DARKEST)
const CALLOUT_GROUND = over('#100D0A', 0.95, '#191510')
const SEG_DARK = '#241E17' // retrieve-mode toggle trough (studio.css literal)
const AUTOROT_BG = '#241E18'
const DARK_INK_TEXT = '#4A4136' // studio.css literal: didyouknow body, flatchip word, paper-rail icons
const QROW_WORD = '#C4B8A7' // studio.css literal: unselected quality rows, rail icons
const PLACEHOLDER = '#6B6055' // studio.css literal: retrieval input placeholder

interface Pair {
  name: string
  fg: string
  bg: string
  px: number
  /** identifying/state-bearing mark rather than text — 3.0 bar (KS3 R1) */
  mark?: boolean
  /** reference-authored value between 3.0 and 4.5 at body size: tolerated
   * with a reason, still floored at 3.0, pinned by `measured`. */
  licence?: string
  /** authoring-time ratio for licensed pairs; dropping >0.05 below it fails */
  measured?: number
}

const BTN_LICENCE =
  'reference-authored button tier: cream/paper text on the accent fill ' +
  '(3.62:1). Every accent-filled control in the frozen reference uses it. ' +
  'Repainting the button tier is a Design/Mide ruling — reported in the ' +
  'MRB-186 Stage 1b run, alongside the tinted-ground caption pairs below.'

const PAIRS: Pair[] = [
  // ── cream world: page chrome ──
  { name: 'nav links — muted on ground (15px)', fg: t('--st-muted'), bg: t('--st-ground'), px: 15 },
  { name: 'sign in — muted on ground (15px)', fg: t('--st-muted'), bg: t('--st-ground'), px: 15 },
  { name: 'active nav item — ink on ground (15px)', fg: t('--st-ink'), bg: t('--st-ground'), px: 15 },
  { name: 'CTA — paper on accent (14px)', fg: t('--st-paper'), bg: t('--st-accent'), px: 14, licence: BTN_LICENCE, measured: 3.62 },
  { name: 'crumb — caption on crumb strip (12px)', fg: t('--st-caption'), bg: t('--st-crumb-bg'), px: 12, licence: 'reference-authored: the crumb strip tint costs the reconciled caption 0.22 of ratio (4.29:1). Darkening caption further changes a ruled value — Design/Mide call.', measured: 4.29 },
  { name: 'MODE eyebrow — faint on crumb strip (10.5px)', fg: t('--st-faint'), bg: t('--st-crumb-bg'), px: 10.5, licence: 'reference-authored, same tinted-strip cost as the crumb (4.28:1).', measured: 4.28 },
  { name: 'mode toggle unselected — caption on trough (13.5px)', fg: t('--st-caption'), bg: t('--st-seg-bg'), px: 13.5, licence: 'reference-authored: the darker seg trough takes the reconciled caption to 3.71:1. The selected state carries the meaning (ink on paper, 16:1); the unselected label is the quiet half of a two-state control. Repaint is a Design/Mide call.', measured: 3.71 },
  { name: 'mode toggle selected — ink on paper chip (13.5px)', fg: t('--st-ink'), bg: t('--st-paper'), px: 13.5 },

  // ── cream world: library ──
  { name: 'LIBRARY eyebrow — caption on ground (10.5px)', fg: t('--st-caption'), bg: t('--st-ground'), px: 10.5 },
  { name: 'library count — ghost on ground (11px)', fg: t('--st-ghost'), bg: t('--st-ground'), px: 11 },
  { name: 'libcard name — ink on ground (14.5px)', fg: t('--st-ink'), bg: t('--st-ground'), px: 14.5 },
  { name: 'libcard meta — faint on ground (10.5px)', fg: t('--st-faint'), bg: t('--st-ground'), px: 10.5 },
  { name: 'viewing meta — accent on paper card (10.5px)', fg: t('--st-accent'), bg: t('--st-paper'), px: 10.5, licence: 'reference-authored: VIEWING is drawn in the accent itself (3.62:1). The state is also carried by the card border and fill (no-hue rule), the word is reinforcement. Repaint is a Design/Mide call.', measured: 3.62 },

  // ── stage furniture ──
  { name: 'stage hint — room-hint on viewport ground (11.5px)', fg: t('--st-room-hint'), bg: STAGE_DARKEST, px: 11.5 },
  { name: 'stage hint — faint on paper stage (11.5px)', fg: t('--st-faint'), bg: t('--st-paper'), px: 11.5 },
  { name: 'chip word — room-text on chip ground (10.5px)', fg: t('--st-room-text'), bg: CHIP_GROUND, px: 10.5 },
  { name: 'rail icons — on rail ground (mark)', fg: QROW_WORD, bg: RAIL_GROUND, px: 20, mark: true },
  { name: 'paper rail icons — on paper (mark)', fg: DARK_INK_TEXT, bg: t('--st-paper'), px: 20, mark: true },
  { name: 'AUTO word — room-muted on autorot well (7.5px)', fg: t('--st-room-muted'), bg: AUTOROT_BG, px: 7.5, licence: 'reference-authored (4.39:1): the 7.5px AUTO caption under the toggle; the toggle itself carries the state. Repaint is a Design/Mide call.', measured: 4.39 },
  { name: 'railtip label — ink on cream pop (12.5px)', fg: t('--st-ink'), bg: t('--st-cream'), px: 12.5 },
  { name: 'railtip verb — caption on cream pop (10px)', fg: t('--st-caption'), bg: t('--st-cream'), px: 10 },
  { name: 'FLAT DIAGRAM word — on note tint (10.5px)', fg: DARK_INK_TEXT, bg: t('--st-note-bg'), px: 10.5 },
  { name: 'accent chevron — on ground (mark)', fg: t('--st-accent'), bg: t('--st-ground'), px: 21, mark: true },
  { name: 'accent chevron — on room (mark)', fg: t('--st-accent'), bg: t('--st-room'), px: 21, mark: true },

  // ── info panel ──
  { name: 'kchip — caption on paper (10.5px)', fg: t('--st-caption'), bg: t('--st-paper'), px: 10.5 },
  { name: 'kchip accent — accent-text on chip tint (10.5px)', fg: t('--st-accent-text'), bg: t('--st-chip-tint'), px: 10.5 },
  { name: 'panel name — ink on paper (36px)', fg: t('--st-ink'), bg: t('--st-paper'), px: 36 },
  { name: 'epithet — caption on paper (16px)', fg: t('--st-caption'), bg: t('--st-paper'), px: 16 },
  { name: 'description — body on paper (16.5px)', fg: t('--st-body'), bg: t('--st-paper'), px: 16.5 },
  { name: 'section count — ghost on paper (10.5px)', fg: t('--st-ghost'), bg: t('--st-paper'), px: 10.5 },
  { name: 'structure label — muted on paper (13.5px)', fg: t('--st-muted'), bg: t('--st-paper'), px: 13.5 },
  { name: 'structure numeral — caption on number well (10px)', fg: t('--st-caption'), bg: t('--st-num-well'), px: 10, licence: 'reference-authored: the number-well tint takes caption to 4.09:1 at 10px. The numeral repeats the adjacent 5.6:1 label — orientation, not sole carrier. Repaint is a Design/Mide call.', measured: 4.09 },
  { name: 'open structure numeral — paper on accent (10px)', fg: t('--st-paper'), bg: t('--st-accent'), px: 10, licence: BTN_LICENCE, measured: 3.62 },
  { name: 'open structure label — ink on chip tint (13.5px)', fg: t('--st-ink'), bg: t('--st-chip-tint'), px: 13.5 },
  { name: 'fact label — caption on paper (11.5px)', fg: t('--st-caption'), bg: t('--st-paper'), px: 11.5 },
  { name: 'fact value — ink on paper (14.5px)', fg: t('--st-ink'), bg: t('--st-paper'), px: 14.5 },
  { name: 'WHY IT MATTERS eyebrow — ember on ink (10px)', fg: t('--st-ember'), bg: t('--st-ink'), px: 10 },
  { name: 'why-it-matters body — room-note on ink (13.5px)', fg: t('--st-room-note'), bg: t('--st-ink'), px: 13.5 },
  { name: 'DID YOU KNOW eyebrow — caption on note tint (10px)', fg: t('--st-caption'), bg: t('--st-note-bg'), px: 10, licence: 'reference-authored: the note tint takes caption to 4.17:1 at 10px. Repaint is a Design/Mide call.', measured: 4.17 },
  { name: 'did-you-know body — on note tint (13.5px)', fg: DARK_INK_TEXT, bg: t('--st-note-bg'), px: 13.5 },
  { name: 'outline button — ink on paper (14.5px)', fg: t('--st-ink'), bg: t('--st-paper'), px: 14.5 },
  { name: 'primary button — paper on accent (14.5px)', fg: t('--st-paper'), bg: t('--st-accent'), px: 14.5, licence: BTN_LICENCE, measured: 3.62 },

  // ── phone / drawer chrome ──
  { name: 'phone sign in — accent-text on ground (13px)', fg: t('--st-accent-text'), bg: t('--st-ground'), px: 13 },
  { name: 'library note — muted on ground (13.5px)', fg: t('--st-muted'), bg: t('--st-ground'), px: 13.5 },
  { name: 'library CTA — accent-text on ground (13.5px)', fg: t('--st-accent-text'), bg: t('--st-ground'), px: 13.5 },
  { name: 'lesson row meta — faint on paper (10.5px)', fg: t('--st-faint'), bg: t('--st-paper'), px: 10.5 },

  // ── dark room ──
  { name: 'brand — cream on room (18px)', fg: t('--st-cream'), bg: t('--st-room'), px: 18 },
  { name: 'end round — room-text on room (14px)', fg: t('--st-room-text'), bg: t('--st-room'), px: 14 },
  { name: 'MODE eyebrow — room-faint on room (10.5px)', fg: t('--st-room-faint'), bg: t('--st-room'), px: 10.5, licence: 'reference-authored dim tier of the dark room (4.00:1 on room). Repaint is a Design/Mide call.', measured: 4.0 },
  { name: 'retrieve toggle unselected — room-muted on trough (13.5px)', fg: t('--st-room-muted'), bg: SEG_DARK, px: 13.5, licence: 'reference-authored (4.39:1 on the dark trough): the quiet half of the two-state control, as on cream. Repaint is a Design/Mide call.', measured: 4.39 },
  { name: 'retrieve toggle selected — paper on accent (13.5px)', fg: t('--st-paper'), bg: t('--st-accent'), px: 13.5, licence: BTN_LICENCE, measured: 3.62 },
  { name: 'ROUND eyebrow — room-muted on panel (10.5px)', fg: t('--st-room-muted'), bg: t('--st-room-panel'), px: 10.5, licence: 'reference-authored (4.64:1) — above 4.5 today; licence documents the tier if the panel ever lightens.', measured: 4.64 },
  { name: 'round count — cream on panel (10.5px)', fg: t('--st-cream'), bg: t('--st-room-panel'), px: 10.5 },
  { name: 'current square numeral — cream on raise (13px)', fg: t('--st-cream'), bg: t('--st-room-raise'), px: 13 },
  { name: 'NAME THE STRUCTURE — ember on panel (11px)', fg: t('--st-ember'), bg: t('--st-room-panel'), px: 11 },
  { name: 'answer text — cream on input well (21px)', fg: t('--st-cream'), bg: t('--st-room-well'), px: 21 },
  { name: 'answer placeholder — on input well (21px)', fg: PLACEHOLDER, bg: t('--st-room-well'), px: 21, licence: 'reference-authored placeholder (3.12:1): deliberately ghosted prompt text, replaced by 17:1 cream the moment the student types. Repaint is a Design/Mide call.', measured: 3.12 },
  { name: 'check button — paper on accent (15px)', fg: t('--st-paper'), bg: t('--st-accent'), px: 15, licence: BTN_LICENCE, measured: 3.62 },
  { name: 'skip button — room-text on panel (15px)', fg: t('--st-room-text'), bg: t('--st-room-panel'), px: 15 },
  { name: "can't recall — room-muted on panel (13.5px)", fg: t('--st-room-muted'), bg: t('--st-room-panel'), px: 13.5, licence: 'reference-authored (4.64:1) — above 4.5 today; documents the tier.', measured: 4.64 },
  { name: 'reveal link — ember on panel (13.5px)', fg: t('--st-ember'), bg: t('--st-room-panel'), px: 13.5 },
  { name: 'MISSED SO FAR — room-muted on panel (10.5px)', fg: t('--st-room-muted'), bg: t('--st-room-panel'), px: 10.5, licence: 'reference-authored (4.64:1) — above 4.5 today; documents the tier.', measured: 4.64 },
  { name: 'missed note — room-faint on panel (13px)', fg: t('--st-room-faint'), bg: t('--st-room-panel'), px: 13, licence: 'reference-authored dim tier (3.72:1): a footnote under the fold of the decision. Repaint is a Design/Mide call.', measured: 3.72 },
  { name: 'DETECTED caption — room-faint on room (9.5px)', fg: t('--st-room-faint'), bg: t('--st-room'), px: 9.5, licence: 'the quality panel keeps DETECTED dimmer than its title (reference hierarchy). Was --st-muted at 2.87:1 — a light-world token on the dark panel, under the 3.0 floor — refit to the dark-room role tier (4.00:1) in this run.', measured: 4.0 },
  { name: 'RENDER QUALITY — room-muted on room (10px)', fg: t('--st-room-muted'), bg: t('--st-room'), px: 10 },
  { name: 'quality row word — on room (13.5px)', fg: QROW_WORD, bg: t('--st-room'), px: 13.5 },
  { name: 'selected row word — cream on raise (13.5px)', fg: t('--st-cream'), bg: t('--st-room-raise'), px: 13.5 },

  // ── callout ──
  { name: 'STRUCTURE eyebrow — ember-strong on callout (10.5px)', fg: t('--st-ember-strong'), bg: CALLOUT_GROUND, px: 10.5 },
  { name: 'callout title — cream on callout (18px)', fg: t('--st-cream'), bg: CALLOUT_GROUND, px: 18 },
  { name: 'callout detail — room-body on callout (13px)', fg: t('--st-room-body'), bg: CALLOUT_GROUND, px: 13 },
  { name: 'callout foot — room-faint on callout (11px)', fg: t('--st-room-faint'), bg: CALLOUT_GROUND, px: 11, licence: 'reference-authored dim tier (4.13:1): ISOLATE · HIDE LABEL secondary actions. Repaint is a Design/Mide call.', measured: 4.13 },
  { name: 'paper callout body — room-note on ink (13px)', fg: t('--st-room-note'), bg: t('--st-ink'), px: 13 },
]

// ── the gate ──────────────────────────────────────────────────

function requirementFor(p: Pair): number {
  if (p.mark) return 3.0 // identifying mark, not text (KS3 R1)
  if (p.px >= 24) return 3.0 // WCAG large text
  return p.licence ? 3.0 : 4.5
}

describe('gate 6 — contrast, recomputed from tokens.css (no hardcoded ratios)', () => {
  it('parsed a real token file', () => {
    expect(Object.keys(TOKENS).length).toBeGreaterThan(30)
    expect(TOKENS['--st-ground']).toBeTruthy()
  })

  for (const p of PAIRS) {
    it(p.name, () => {
      const ratio = contrast(p.fg, p.bg)
      const need = requirementFor(p)
      expect(
        ratio,
        `${p.name}: ${p.fg} on ${p.bg} measures ${ratio.toFixed(2)}:1, needs ${need.toFixed(1)}:1` +
          (p.licence ? ` (licensed: ${p.licence})` : ''),
      ).toBeGreaterThanOrEqual(need - 0.005)

      // A licence is a tolerance for today's value, not a 3.0-wide door: the
      // pair may not silently degrade below its authoring-time ratio.
      if (p.licence) {
        expect(
          ratio,
          `${p.name}: licensed at ${p.measured}:1 but now measures ${ratio.toFixed(2)}:1 — ` +
            'the licensed value has degraded; re-rule it, do not let it slide',
        ).toBeGreaterThanOrEqual((p.measured ?? need) - 0.05)
      }
    })
  }

  it('every licence carries a reason and a pinned measurement', () => {
    for (const p of PAIRS.filter((x) => x.licence)) {
      expect(p.licence!.length, p.name).toBeGreaterThan(20)
      expect(p.measured, `${p.name} has a licence but no pinned measurement`).toBeTypeOf('number')
    }
  })

  it('the three MRB-186 darkened values clear 4.5 on both light grounds', () => {
    for (const name of ['--st-caption', '--st-faint', '--st-ghost']) {
      for (const ground of ['--st-ground', '--st-paper']) {
        expect(
          contrast(t(name), t(ground)),
          `${name} on ${ground} — the Finding 1 darkening has regressed`,
        ).toBeGreaterThanOrEqual(4.5 - 0.005)
      }
    }
  })
})
