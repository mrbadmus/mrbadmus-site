// @vitest-environment node
// Gate 15 — the two invariants that let a specimen grow without deforming the
// page, held at their source in studio.css.
//
// Both defects this gate exists for arrived the same way: content/heart.json
// went from 2 hotspots to 14, and nothing was watching what that did to the
// layout.
//
//   A. THE PAGE GREW WITH THE HOTSPOT COUNT. At 1440x900 the body measured
//      1942px and the stage 724x1766 — the info panel's structure list is one
//      chip per hotspot, and the whole column stretched to it. `.panel` and
//      `.panel__scroll` already carried a correct internal scroll; it never
//      engaged, because `.app { min-height: 100dvh }` is a FLOOR and leaves
//      the column's height indefinite, so nothing above the panel had a
//      ceiling for it to scroll inside of. A specimen with 40 structures
//      would have made a 5000px page.
//
//   B. THE LIBRARY CAPTION TRUNCATED. `VIEWING · 14 STRUCTU…` — the count is
//      the one thing that caption exists to tell the viewer (MRB-193/186: a
//      card promising fourteen structures must not open onto nine), and the
//      count was the part cut off. It now wraps, and under the MRB-186 ruling
//      it must wrap BETWEEN WORDS ONLY — that ruling came from the panel's
//      label column rendering SYSTEM as SYSTE / M.
//
// WHAT THIS FILE CAN AND CANNOT ASSERT. Vitest runs in jsdom, which parses CSS
// but does not lay out: every box is 0x0, `getComputedStyle` returns only what
// was declared, and no text wraps because no text is measured. A height or a
// line-break assertion here would pass on the broken CSS and on the fixed CSS
// alike — a green light that means nothing. So this gate asserts the SOURCE
// invariants (what the stylesheet declares, and that the responsive overrides
// that must not change are still there), and the RENDERED behaviour — a page
// that does not scroll, a caption that is whole and unbroken — is measured in
// a real Chrome by 3d_parity.py's layer B. The two halves are named in each
// other's comments deliberately; neither is sufficient alone.

import { readFileSync } from 'node:fs'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { describe, expect, it } from 'vitest'

const here = dirname(fileURLToPath(import.meta.url))
const CSS_PATH = resolve(here, '../../src/styles/studio.css')
const css = readFileSync(CSS_PATH, 'utf8')

// ── a small stylesheet reader ─────────────────────────────────────────
// Enough CSS parsing to answer "what does THIS rule declare, in THIS media
// context" — not a general parser. Comments are stripped first so that prose
// about a property (this file has plenty) can never be read as a declaration.

const stripped = css.replace(/\/\*[\s\S]*?\*\//g, '')

interface Rule {
  selector: string
  body: string
  media: string | null
}

/** Every rule in the sheet, each tagged with the @media it sits inside. */
function parse(source: string): Rule[] {
  const rules: Rule[] = []
  let i = 0
  let media: string | null = null
  let mediaEnd = -1

  while (i < source.length) {
    const brace = source.indexOf('{', i)
    if (brace < 0) break
    // the next rule starts past the media block's close: we are outside again
    if (mediaEnd >= 0 && brace > mediaEnd) {
      media = null
      mediaEnd = -1
    }
    // close braces of preceding rules sit in the prelude; they are not selector
    const prelude = source.slice(i, brace).replace(/}/g, ' ').trim()

    // find the matching close brace
    let depth = 0
    let end = brace
    for (; end < source.length; end++) {
      if (source[end] === '{') depth++
      else if (source[end] === '}') {
        depth--
        if (depth === 0) break
      }
    }

    if (prelude.startsWith('@media')) {
      media = prelude.replace(/^@media\s*/, '').trim()
      mediaEnd = end
      i = brace + 1 // step INTO the block; its rules are read next
      continue
    }
    if (prelude.startsWith('@')) {
      // @keyframes and friends — skipped whole, their inner blocks are not rules
      i = end + 1
      continue
    }
    rules.push({ selector: prelude, body: source.slice(brace + 1, end), media })
    i = end + 1
  }
  return rules
}

const RULES = parse(stripped)

/** The declarations of one rule, failing loudly when the rule has vanished. */
function ruleOf(selector: string, media: string | null = null): Record<string, string> {
  const hits = RULES.filter((r) => r.selector === selector && r.media === media)
  if (hits.length === 0) {
    throw new Error(
      `no rule \`${selector}\`${media ? ` inside @media ${media}` : ' at top level'} ` +
        `in studio.css — renamed, moved into a media block, or deleted`,
    )
  }
  const out: Record<string, string> = {}
  for (const hit of hits) {
    for (const line of hit.body.split(';')) {
      const at = line.indexOf(':')
      if (at < 0) continue
      out[line.slice(0, at).trim()] = line.slice(at + 1).trim()
    }
  }
  return out
}

const TABLET = '(max-width: 1023px)'
const PHONE = '(max-width: 699px)'

// ── A. the desktop viewport ceiling ───────────────────────────────────

describe('gate 15A — the page is one viewport tall on desktop', () => {
  // The fix itself. `min-height` is a floor and leaves the flex column's
  // height indefinite; an `fr` grid row inside an indefinite-height container
  // resolves to its items' max-content, which is why constraining the ROW
  // does not work here — measured, `grid-template-rows: minmax(0, 1fr)` on
  // `.main` left the row at the same 1765.78px. The ceiling has to be a
  // definite height on the column itself.
  it('.app pins its height to the viewport, not just a floor', () => {
    const app = ruleOf('.app')
    expect(
      app['height'],
      '.app has no definite height — `min-height: 100dvh` alone is a floor, ' +
        'so the column grows with the panel and the page grows with it',
    ).toBe('100dvh')
    expect(app['min-height'], 'the floor is still wanted alongside the ceiling').toBe('100dvh')
    expect(app['display']).toBe('flex')
    expect(app['flex-direction']).toBe('column')
  })

  it('.main is still the flex child that takes the leftover space', () => {
    const main = ruleOf('.main')
    expect(main['flex']).toBe('1')
    // without min-height:0 the grid's content floor would defeat the ceiling
    expect(main['min-height']).toBe('0')
    expect(main['display']).toBe('grid')
  })

  it('the panel carries the internal scroll the ceiling engages', () => {
    // Built and correct before this work; it simply had no ceiling to scroll
    // inside of. If either of these regresses, the ceiling starts CLIPPING
    // the structure list instead of scrolling it — silently.
    const panel = ruleOf('.panel')
    expect(panel['overflow']).toBe('hidden')
    expect(panel['min-height']).toBe('0')
    const scroll = ruleOf('.panel__scroll')
    expect(scroll['overflow-y'], 'the panel would clip its structure list, not scroll it').toBe(
      'auto',
    )
    expect(scroll['flex']).toBe('1')
    expect(scroll['min-height']).toBe('0')
  })

  it('the ceiling is lifted below 1024, where the whole column scrolls', () => {
    // Tablet and phone deliberately scroll the document. Pinning .app there
    // would move the scroll from the document into .main — the topbar would
    // stop scrolling away — which is a design change nobody ruled on.
    expect(
      ruleOf('.app', TABLET)['height'],
      'the desktop ceiling leaks into tablet and phone: the column would ' +
        'scroll inside .main instead of with the document',
    ).toBe('auto')
  })

  it('the two responsive .main layouts are untouched', () => {
    const tablet = ruleOf('.main', TABLET)
    expect(tablet['display']).toBe('block')
    expect(tablet['overflow-y']).toBe('auto')
    const phone = ruleOf('.main', PHONE)
    expect(phone['display']).toBe('flex')
    expect(phone['flex-direction']).toBe('column')
    expect(phone['overflow']).toBe('hidden')
  })

  it('the retrieval grid is untouched at both breakpoints', () => {
    // Measured before and after: tablet retrieve rows stay 457.5 / 457.5.
    // They would NOT have: `grid-template-rows: minmax(0, 1fr)` on .main
    // turns them into 495 / 420, because row two falls into an implicit auto
    // track. A row constraint was the obvious fix and this is the second
    // reason it was the wrong one.
    expect(ruleOf('.main')['grid-template-rows']).toBeUndefined()
    expect(ruleOf('.main')['grid-auto-rows']).toBeUndefined()
    const tablet = ruleOf('.main--retrieve', TABLET)
    expect(tablet['display']).toBe('grid')
    expect(tablet['grid-template-columns']).toBe('1fr')
    const phone = ruleOf('.main--retrieve', PHONE)
    expect(phone['display']).toBe('flex')
    expect(phone['overflow-y']).toBe('auto')
  })
})

// ── B. the library caption ────────────────────────────────────────────

const BREAKING_WRAP = new Set(['break-word', 'anywhere', 'break-all'])

describe('gate 15B — the library caption wraps, never truncates, never splits a word', () => {
  it('.libcard__meta wraps instead of truncating', () => {
    const meta = ruleOf('.libcard__meta')
    expect(
      meta['white-space'],
      'nowrap here means the structure count is the part that gets cut off',
    ).toBe('normal')
    expect(
      meta['text-overflow'],
      'text-overflow only ever applied to the nowrap single line it replaced',
    ).toBeUndefined()
    expect(
      meta['overflow'],
      'overflow:hidden would silently clip an unbreakable token — the same ' +
        'failure this fix removes, just without the ellipsis to give it away',
    ).toBeUndefined()
  })

  it('.libcard__meta declares the non-breaking wrap explicitly', () => {
    // `normal`, not the `break-word` the rest of this file uses: this is a
    // label column of two short tokens, so break-word has no over-long token
    // to rescue and would only license the break MRB-186 forbids.
    const meta = ruleOf('.libcard__meta')
    expect(meta['overflow-wrap']).toBe('normal')
    expect(meta['word-break']).toBe('normal')
  })

  it('nothing it inherits from can hand it a mid-word break', () => {
    // overflow-wrap and word-break INHERIT, and several blocks in this sheet
    // set overflow-wrap: break-word. Declaring the values above closes that
    // door; this asserts nobody props it back open by putting a breaking
    // value on an ancestor and dropping the explicit declaration here.
    const ancestors = [
      '*',
      'html, body, #root',
      'body',
      '.app',
      '.main',
      '.main--explore',
      '.library',
      '.library__list',
      '.libcard',
      '.libcard__text',
      '.drawer',
      '.phonelib',
    ]
    for (const rule of RULES) {
      if (!ancestors.includes(rule.selector)) continue
      for (const prop of ['overflow-wrap', 'word-break', 'line-break']) {
        const m = rule.body.match(new RegExp(`${prop}\\s*:\\s*([a-z-]+)`))
        if (!m) continue
        expect(
          BREAKING_WRAP.has(m[1]),
          `${rule.selector} sets ${prop}: ${m[1]}, which .libcard__meta would inherit`,
        ).toBe(false)
      }
    }
  })

  it('the caption keeps the type Design drew', () => {
    // The wrap is the only thing that changed. Font, colour, tracking and the
    // 3px offset are the reference's, and the accent-text VIEWING state is an
    // allow-listed divergence the parity gate measures — not something to
    // adjust while making room for a second line.
    const meta = ruleOf('.libcard__meta')
    expect(meta['font']).toBe('400 10.5px/1 var(--st-mono)')
    expect(meta['letter-spacing']).toBe('0.06em')
    expect(meta['margin-top']).toBe('3px')
    expect(meta['color']).toBe('var(--st-faint)')
    expect(meta['text-transform']).toBe('uppercase')
  })
})
