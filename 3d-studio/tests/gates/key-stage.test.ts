// Gate 14 — the key-stage filter (MRB-193/186).
//
// The heart is offered to KS3 and to KS4, but five of its fourteen structures
// are KS4 anatomy: the coronary arteries, the three valves and the sino-atrial
// node. A Year 7 lesson on the heart does not name them. So a KS3 student must
// not see them on the stage, must not be offered them in the panel or on the
// library card, and — the one that actually costs a student something — must
// never be asked to name one in a retrieval round.
//
// ONE MECHANISM. A hotspot's own `keyStages` win where it declares them and it
// inherits the specimen's where it does not, which is exactly what `specPoints`
// already does (MRB-193). Nothing is derived: a structure is KS4-only because
// it is written down as KS4-only.
//
// ORTHOGONAL TO `tiers`, and this file asserts that too. Foundation and higher
// are not separated here at all — every KS4 student sees all fourteen. The two
// filters are over the same list and neither implies the other; conflating them
// would hide half the heart from a foundation class.
//
// The numbers below are asserted against the REAL content record, not a
// fixture. A fixture would prove the arithmetic and nothing about the heart; if
// someone edits heart.json and the counts move, this must fail.

import { describe, expect, it } from 'vitest'
import { createElement } from 'react'
import { render, waitFor } from '@testing-library/react'
import App from '../../src/App'
import {
  getSpecimen,
  resolveKeyStages,
  specimenForKeyStage,
  viewingKeyStage,
  visibleHotspots,
} from '../../src/studio/content'
import { eligibleHotspots } from '../../src/studio/retrieval'
import {
  PROVISIONAL_ANONYMOUS_PROFILE,
  type LearnerProfile,
} from '../../src/studio/attempts'
import type { CapabilityReport } from '../../src/studio/capability'
import { createPlaceholderRenderer } from '../../src/renderer/placeholder'
import type { HotspotRecord, SpecimenRecord } from '../../src/studio/types'

const heart = getSpecimen('heart')

/** The five structures authored as KS4-only in content/heart.json. */
const KS4_ONLY = [
  'heart.coronary-arteries',
  'heart.tricuspid-valve',
  'heart.bicuspid-valve',
  'heart.semilunar-valves',
  'heart.sino-atrial-node',
]

const ALL_STRUCTURES = 14
const KS3_STRUCTURES = 9

const KS3_STUDENT: LearnerProfile = {
  userId: 'ks3-student',
  pathway: 'combined',
  // A KS3 learner has no tier at all (attempts contract §6 item 2).
  tier: null,
  keyStage: 'KS3',
}

const KS4_FOUNDATION: LearnerProfile = {
  userId: 'ks4-foundation',
  pathway: 'combined',
  tier: 'foundation',
  keyStage: 'KS4',
}

const KS4_HIGHER: LearnerProfile = {
  userId: 'ks4-higher',
  pathway: 'triple',
  tier: 'higher',
  keyStage: 'KS4',
}

function find(id: string): HotspotRecord {
  const hotspot = heart.hotspots.find((h) => h.id === id)
  if (!hotspot) throw new Error(`heart.json no longer has ${id}`)
  return hotspot
}

const TIER_A: CapabilityReport = {
  tier: 'A',
  webgl2: true,
  deviceMemory: 8,
  cores: 8,
  viewport: { width: 1440, height: 900 },
  pointer: 'fine',
}

/** A tiered renderer that can exist in jsdom, so the stage genuinely draws its
 * dots rather than routing to the flat fallback. */
const viewportPlaceholder = async () => createPlaceholderRenderer('viewport')

describe('gate 14 — a hotspot inherits its specimen unless it says otherwise', () => {
  it('a hotspot with no keyStages inherits the specimen’s', () => {
    expect(heart.keyStages).toEqual(['KS3', 'KS4'])
    expect(find('heart.right-atrium').keyStages).toBeUndefined()
    expect(resolveKeyStages(heart, find('heart.right-atrium'))).toEqual(['KS3', 'KS4'])
  })

  it('a hotspot that declares its own wins', () => {
    expect(find('heart.sino-atrial-node').keyStages).toEqual(['KS4'])
    expect(resolveKeyStages(heart, find('heart.sino-atrial-node'))).toEqual(['KS4'])
  })

  it('an empty array is not a declaration — it inherits, exactly as specPoints does', () => {
    // A FIXTURE, not content: the record is never authored with an empty
    // array. Asserted because the two resolvers must not drift apart.
    const empty = { ...find('heart.septum'), keyStages: [] as never[] }
    expect(resolveKeyStages(heart, empty)).toEqual(['KS3', 'KS4'])
  })
})

describe('gate 14 — what each key stage sees on the heart', () => {
  it('the record carries fourteen structures, five of them KS4-only', () => {
    expect(heart.hotspots).toHaveLength(ALL_STRUCTURES)
    expect(
      heart.hotspots.filter((h) => Array.isArray(h.keyStages)).map((h) => h.id),
    ).toEqual(KS4_ONLY)
  })

  it('a KS3 profile sees exactly nine', () => {
    const seen = visibleHotspots(heart, viewingKeyStage(KS3_STUDENT))
    expect(seen).toHaveLength(KS3_STRUCTURES)
    for (const id of KS4_ONLY) expect(seen.map((h) => h.id)).not.toContain(id)
  })

  it('a KS4 profile sees exactly fourteen', () => {
    const seen = visibleHotspots(heart, viewingKeyStage(KS4_HIGHER))
    expect(seen).toHaveLength(ALL_STRUCTURES)
    for (const id of KS4_ONLY) expect(seen.map((h) => h.id)).toContain(id)
  })

  it('the filtered specimen keeps the record’s own order', () => {
    const ks3 = specimenForKeyStage(heart, 'KS3')
    expect(ks3.hotspots.map((h) => h.id)).toEqual([
      'heart.right-atrium',
      'heart.right-ventricle',
      'heart.left-atrium',
      'heart.left-ventricle',
      'heart.aorta',
      'heart.vena-cava',
      'heart.pulmonary-artery',
      'heart.pulmonary-vein',
      'heart.septum',
    ])
  })

  it('filtering nothing out returns the SAME record object', () => {
    // Referential stability, not tidiness: the shell memoises on this identity
    // and the renderers reload the specimen when it changes, so a fresh object
    // per render would re-fetch the GLB continuously.
    expect(specimenForKeyStage(heart, 'KS4')).toBe(heart)
    expect(specimenForKeyStage(heart, null)).toBe(heart)
    expect(specimenForKeyStage(heart, 'KS3')).not.toBe(heart)
  })
})

describe('gate 14 — a KS3 learner is never asked to name what they cannot see', () => {
  it('no KS4-only structure is eligible for a KS3 learner', () => {
    // Deliberately handed the UNFILTERED record: the round must apply the
    // filter itself, not lean on the shell having pre-filtered.
    const asked = eligibleHotspots(heart, KS3_STUDENT).map((h) => h.id)
    expect(asked).toHaveLength(KS3_STRUCTURES)
    expect(asked).not.toContain('heart.sino-atrial-node')
    for (const id of KS4_ONLY) expect(asked).not.toContain(id)
  })

  it('a KS4 learner IS asked about the sino-atrial node', () => {
    const asked = eligibleHotspots(heart, KS4_HIGHER).map((h) => h.id)
    expect(asked).toHaveLength(ALL_STRUCTURES)
    expect(asked).toContain('heart.sino-atrial-node')
  })

  it('what is asked is a subset of what is drawn, for both key stages', () => {
    for (const profile of [KS3_STUDENT, KS4_FOUNDATION, KS4_HIGHER]) {
      const drawn = specimenForKeyStage(heart, viewingKeyStage(profile))
      const drawnIds = new Set(drawn.hotspots.map((h) => h.id))
      for (const asked of eligibleHotspots(heart, profile)) {
        expect(drawnIds.has(asked.id)).toBe(true)
      }
    }
  })
})

describe('gate 14 — an anonymous visitor sees the whole specimen', () => {
  it('no account means no key stage to filter by', () => {
    expect(PROVISIONAL_ANONYMOUS_PROFILE.userId).toBeNull()
    expect(viewingKeyStage(PROVISIONAL_ANONYMOUS_PROFILE)).toBeNull()
    expect(
      specimenForKeyStage(heart, viewingKeyStage(PROVISIONAL_ANONYMOUS_PROFILE)).hotspots,
    ).toHaveLength(ALL_STRUCTURES)
  })

  it('and it is the missing account doing that, not the provisional KS4 default', () => {
    // The provisional anonymous profile happens to carry keyStage 'KS4', which
    // would show all fourteen by accident. Prove the accident is not the
    // mechanism: an anonymous visitor carrying KS3 still sees all fourteen.
    const anonymousKs3: LearnerProfile = {
      ...PROVISIONAL_ANONYMOUS_PROFILE,
      keyStage: 'KS3',
    }
    expect(viewingKeyStage(anonymousKs3)).toBeNull()
    expect(visibleHotspots(heart, viewingKeyStage(anonymousKs3))).toHaveLength(
      ALL_STRUCTURES,
    )
    expect(eligibleHotspots(heart, anonymousKs3)).toHaveLength(ALL_STRUCTURES)
  })

  it('a signed-in KS3 student is filtered where the anonymous one was not', () => {
    const signedIn: LearnerProfile = { ...KS3_STUDENT }
    const anonymous: LearnerProfile = { ...KS3_STUDENT, userId: null }
    expect(viewingKeyStage(signedIn)).toBe('KS3')
    expect(viewingKeyStage(anonymous)).toBeNull()
    expect(visibleHotspots(heart, viewingKeyStage(signedIn))).toHaveLength(
      KS3_STRUCTURES,
    )
    expect(visibleHotspots(heart, viewingKeyStage(anonymous))).toHaveLength(
      ALL_STRUCTURES,
    )
  })
})

describe('gate 14 — key stage is not tier, and does not touch it', () => {
  it('foundation and higher KS4 profiles see the same fourteen', () => {
    const foundation = specimenForKeyStage(heart, viewingKeyStage(KS4_FOUNDATION))
    const higher = specimenForKeyStage(heart, viewingKeyStage(KS4_HIGHER))
    expect(foundation.hotspots).toHaveLength(ALL_STRUCTURES)
    expect(higher.hotspots.map((h) => h.id)).toEqual(
      foundation.hotspots.map((h) => h.id),
    )
  })

  it('and are asked about the same fourteen', () => {
    expect(eligibleHotspots(heart, KS4_FOUNDATION).map((h) => h.id)).toEqual(
      eligibleHotspots(heart, KS4_HIGHER).map((h) => h.id),
    )
  })

  it('the tier filter still bites where a structure declares one tier', () => {
    // A FIXTURE. Every structure on the heart is both foundation and higher,
    // so tier separation cannot be observed there — but it must still work,
    // and must work INSIDE the key stage rather than instead of it.
    const mixed: SpecimenRecord = {
      ...heart,
      hotspots: [
        { ...find('heart.septum'), id: 'x.higher-only', tiers: ['higher'] },
        { ...find('heart.septum'), id: 'x.foundation-only', tiers: ['foundation'] },
        {
          ...find('heart.sino-atrial-node'),
          id: 'x.ks4-higher-only',
          tiers: ['higher'],
        },
      ],
    }
    expect(eligibleHotspots(mixed, KS4_HIGHER).map((h) => h.id)).toEqual([
      'x.higher-only',
      'x.ks4-higher-only',
    ])
    expect(eligibleHotspots(mixed, KS4_FOUNDATION).map((h) => h.id)).toEqual([
      'x.foundation-only',
    ])
    // KS3 has no tier, so every structure it can SEE is eligible — and the one
    // it cannot see stays out whatever its tiers say.
    expect(eligibleHotspots(mixed, KS3_STUDENT).map((h) => h.id)).toEqual([
      'x.higher-only',
      'x.foundation-only',
    ])
  })
})

describe('gate 14 — the panel, the library card and the stage report one number', () => {
  async function countsFor(profile: LearnerProfile) {
    render(
      createElement(App, {
        capability: TIER_A,
        createRenderer: viewportPlaceholder,
        profile,
      }),
    )
    // The dots are sampled on an animation frame once the renderer is ready.
    await waitFor(() =>
      expect(document.querySelectorAll('.hotspot').length).toBeGreaterThan(0),
    )
    const chip = document.querySelector('.kchip--accent')
    const meta = document.querySelector('.libcard.is-viewing .libcard__meta')
    return {
      panel: chip?.textContent ?? '',
      card: meta?.textContent ?? '',
      dots: document.querySelectorAll('.hotspot').length,
    }
  }

  it('a KS3 student is promised nine, and finds nine on the stage', async () => {
    const seen = await countsFor(KS3_STUDENT)
    expect(seen.panel).toBe('9 structures')
    expect(seen.card).toBe('Viewing · 9 structures')
    expect(seen.dots).toBe(KS3_STRUCTURES)
  })

  it('a KS4 student is promised fourteen, and finds fourteen', async () => {
    const seen = await countsFor(KS4_FOUNDATION)
    expect(seen.panel).toBe('14 structures')
    expect(seen.card).toBe('Viewing · 14 structures')
    expect(seen.dots).toBe(ALL_STRUCTURES)
  })

  it('an anonymous visitor is promised the whole shopfront', async () => {
    const seen = await countsFor(PROVISIONAL_ANONYMOUS_PROFILE)
    expect(seen.panel).toBe('14 structures')
    expect(seen.card).toBe('Viewing · 14 structures')
    expect(seen.dots).toBe(ALL_STRUCTURES)
  })
})

// ─────────────────────────────────────────────────────────────────────────────
// The lesson link (spec §11's URL map, MRB-218).
//
// `lessonUrl` now resolves to a real page — the triple-higher organisation
// lesson, because the studio's content is written at triple-higher depth and
// that is the page that matches it.
//
// It is therefore a GCSE page, and a Year 7 student sent to one is worse served
// than a Year 7 student who never sees the control. There is no KS3 circulation
// content anywhere in the scheme, so there is nothing else to point them at.
// The control is ABSENT for a KS3 viewer — not disabled, not redirected.
//
// Asserted through the real App at every layout that carries the link, because
// there are four call sites and "absent" has to mean absent at all of them.

describe('gate 14 — the lesson link is offered by key stage', () => {
  /** The layout is chosen from `window.innerWidth` by `layoutFor`, NOT from
   * the capability report's viewport — so the width has to be set on the
   * window before render or all three "layouts" are the jsdom default and this
   * asserts the desktop panel three times. (It did, on the first run: the
   * phone assertions passed against the desktop button and the sheet was never
   * mounted at all.) */
  async function lessonLinksFor(profile: LearnerProfile, width = 1440) {
    const previous = window.innerWidth
    Object.defineProperty(window, 'innerWidth', {
      value: width,
      writable: true,
      configurable: true,
    })
    const { unmount } = render(
      createElement(App, {
        capability: { ...TIER_A, viewport: { width, height: 900 } },
        createRenderer: viewportPlaceholder,
        profile,
      }),
    )
    await waitFor(() =>
      expect(document.querySelectorAll('.hotspot').length).toBeGreaterThan(0),
    )
    const links = Array.from(
      document.querySelectorAll<HTMLAnchorElement>(
        'a.btn--outline, a.lessonrow, a.lessonglyph',
      ),
    )
    const result = {
      count: links.length,
      hrefs: links.map((a) => a.getAttribute('href')),
      /** which construction rendered — the desktop/tablet button, the sheet
       * row, or the sheet foot glyph */
      marks: links.map((a) => a.className).join(' '),
      // The divider that heads the phone sheet's link must go with it.
      relatedRule: Array.from(document.querySelectorAll('.sectionrule .eyebrow')).some(
        (e) => e.textContent === 'Related lesson',
      ),
    }
    unmount()
    Object.defineProperty(window, 'innerWidth', {
      value: previous,
      writable: true,
      configurable: true,
    })
    return result
  }

  const LESSON = '/triple/higher/biology/organisation/heart-blood-vessels.html'
  // The three layouts `layoutFor` resolves, and between them all four
  // LessonLink call sites: desktop panel foot, tablet actions, phone sheet
  // body row, phone sheet foot glyph.
  const LAYOUTS = [
    ['desktop', 1440],
    ['tablet', 900],
    ['phone', 390],
  ] as const

  it('the record points at a real generated page, not a placeholder', () => {
    // validate_content.py gate 3 proves it resolves on disk; this proves the
    // app is reading the resolved value rather than a TODO string.
    expect(heart.lessonUrl).toBe(LESSON)
    expect(heart.lessonUrl.startsWith('TODO')).toBe(false)
  })

  it('the three widths really do produce three different layouts', async () => {
    // Guards the trap this harness fell into once already: if `layoutFor` ever
    // stops reading window.innerWidth, every assertion below silently becomes
    // the desktop one repeated three times.
    expect((await lessonLinksFor(KS4_HIGHER, 1440)).marks).toContain('btn--outline')
    expect((await lessonLinksFor(KS4_HIGHER, 900)).marks).toContain('btn--outline')
    expect((await lessonLinksFor(KS4_HIGHER, 390)).marks).toContain('lessonglyph')
    expect((await lessonLinksFor(KS4_HIGHER, 390)).marks).toContain('lessonrow')
  })

  for (const [layout, width] of LAYOUTS) {
    it(`a KS4 student is offered it on ${layout}`, async () => {
      const seen = await lessonLinksFor(KS4_HIGHER, width)
      expect(seen.count).toBeGreaterThan(0)
      for (const href of seen.hrefs) expect(href).toBe(LESSON)
    })

    it(`an anonymous visitor is offered it on ${layout}`, async () => {
      // The shopfront rule: no account means no key stage to filter by.
      const seen = await lessonLinksFor(PROVISIONAL_ANONYMOUS_PROFILE, width)
      expect(seen.count).toBeGreaterThan(0)
      for (const href of seen.hrefs) expect(href).toBe(LESSON)
    })

    it(`a KS3 student is offered NOTHING on ${layout} — absent, not disabled`, async () => {
      const seen = await lessonLinksFor(KS3_STUDENT, width)
      expect(seen.count, `${layout}: KS3 was offered ${seen.hrefs.join(', ')}`).toBe(0)
      // Not merely hidden by CSS or disabled: nothing pointing at the lesson
      // may be in the document at all.
      expect(document.querySelector(`a[href="${LESSON}"]`)).toBeNull()
    })
  }

  it('the phone sheet drops the "Related lesson" rule along with the link', async () => {
    // A section rule standing over nothing reads as content that failed to
    // load, which is a worse answer than the absence it is trying to express.
    const phone = 390
    expect((await lessonLinksFor(KS4_HIGHER, phone)).relatedRule).toBe(true)
    expect((await lessonLinksFor(KS3_STUDENT, phone)).relatedRule).toBe(false)
  })

  it('KS3 keeps everything else the panel offers — only the lesson goes', async () => {
    // The failure mode this guards: hiding the link by hiding the panel foot,
    // which would take Start retrieval with it and cost a KS3 student the
    // round they are entitled to.
    render(
      createElement(App, {
        capability: TIER_A,
        createRenderer: viewportPlaceholder,
        profile: KS3_STUDENT,
      }),
    )
    await waitFor(() =>
      expect(document.querySelectorAll('.hotspot').length).toBeGreaterThan(0),
    )
    const buttons = Array.from(document.querySelectorAll('button')).map((b) => b.textContent)
    expect(buttons).toContain('Start retrieval')
  })
})
