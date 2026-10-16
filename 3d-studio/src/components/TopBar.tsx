// ⊕ Front door (12 Oct 2026) — THE STUDIO WEARS THE ONE PUBLIC BAR'S RIGHT-HAND
// END. The inert "Lessons / Practice" nav, "Sign in" and "Create free account"
// are gone: the bar's end is now the site's single home button ("Sign in", or
// "My class" / "My classes" / "My dashboard" / "Today" for a signed-in person)
// and the hamburger, and BOTH ARE DRAWN BY shared/nav.js — this component only
// renders the two empty hooks it binds to (`#nav-auth-area`, `.nav-burger`),
// so there is one drawer implementation on the whole site and the studio has
// no copy of it. nav.js refills the slot if a layout change remounts the
// header. No theme control: the studio is a light-only surface and does not
// honour html[data-theme], so a theme button here would do nothing.
//
// Header at all three breakpoints (§01/§02/§04/§05). Brand: ⊕ one-mark ruling
// (Mide, 13 Sep 2026) — the ONE site lockup, taken at run time from
// /shared/brand/brand.js (written by brand.py; loaded by index.html together
// with brand.css), never redrawn here. The reference's own drawing (two
// chevrons, halves mirrored, Bricolage 600 "MrBadmusAI") is retired. Nav entries
// beyond the studio are drawn as the reference draws them (inert, muted)
// until the product wires real destinations.

import type { StageMode } from './Stage'
import { SpecimensIcon } from './icons'

declare global {
  interface Window {
    MrBadmusBrand?: { NAME: string; MARK: string; lockup: (href?: string, onDark?: boolean) => string }
  }
}

/** The one lockup. `onDark`: the retrieval room's bar is dark whatever the
 *  page does, so the wordmark goes cream there. Without brand.js (a unit test
 *  in jsdom, or the script failing to load) it degrades to the wordmark
 *  alone — never to a second drawing of the mark. */
function Brand({ onDark }: { onDark: boolean }) {
  const lib = typeof window !== 'undefined' ? window.MrBadmusBrand : undefined
  if (!lib) {
    return (
      <a className={'mrb-brand' + (onDark ? ' mrb-brand--on-dark' : '')} href="/index.html" aria-label="MrBadmus home">
        <span className="mrb-brand__word">MrBadmus</span>
      </a>
    )
  }
  return <span className="brand-slot" dangerouslySetInnerHTML={{ __html: lib.lockup('/index.html', onDark) }} />
}

/** The shared public bar's end (shared/nav.js paints into and binds these). */
function PublicEnd() {
  return (
    <>
      <span id="nav-auth-area" />
      <button
        className="nav-burger"
        type="button"
        aria-label="Open menu"
        aria-expanded="false"
        aria-controls="nav-drawer"
      >
        <span />
        <span />
        <span />
      </button>
    </>
  )
}

export function ModeToggle({
  mode,
  onMode,
}: {
  mode: StageMode
  onMode: (m: StageMode) => void
}) {
  return (
    <div className="modewrap">
      <span className="eyebrow">Mode</span>
      <div className="modeseg" role="group" aria-label="Mode">
        <button
          type="button"
          className={mode === 'explore' ? 'is-on' : ''}
          aria-pressed={mode === 'explore'}
          onClick={() => onMode('explore')}
        >
          Explore
        </button>
        <button
          type="button"
          className={mode === 'retrieve' ? 'is-on' : ''}
          aria-pressed={mode === 'retrieve'}
          onClick={() => onMode('retrieve')}
        >
          Retrieve
        </button>
      </div>
    </div>
  )
}

export function TopBar({
  layout,
  mode,
  onMode,
  onOpenLibrary,
  phoneTitle,
}: {
  layout: 'desktop' | 'tablet' | 'phone'
  mode: StageMode
  onMode: (m: StageMode) => void
  onOpenLibrary: () => void
  /** phone: specimen name replaces the brand once the sheet is raised (§05) */
  phoneTitle?: string | null
}) {
  const brand = <Brand onDark={mode === 'retrieve'} />

  if (mode === 'retrieve') {
    return (
      <header className="topbar">
        {brand}
        <div className="topbar__end">
          <ModeToggle mode={mode} onMode={onMode} />
          <button type="button" className="endround" onClick={() => onMode('explore')}>
            End round
          </button>
        </div>
      </header>
    )
  }

  if (layout === 'phone') {
    return (
      <header className="topbar">
        <button
          type="button"
          className="libtrigger libtrigger--square"
          aria-label="Open specimen library"
          title="Specimens"
          onClick={onOpenLibrary}
        >
          <SpecimensIcon />
        </button>
        {phoneTitle ? (
          <span className="brand" style={{ fontSize: 15 }}>{phoneTitle}</span>
        ) : (
          brand
        )}
        <div className="topbar__end">
          <PublicEnd />
        </div>
      </header>
    )
  }

  if (layout === 'tablet') {
    return (
      <header className="topbar">
        <button type="button" className="libtrigger" onClick={onOpenLibrary}>
          <SpecimensIcon />
          Specimens
        </button>
        {brand}
        <div className="topbar__end">
          <ModeToggle mode={mode} onMode={onMode} />
          <PublicEnd />
        </div>
      </header>
    )
  }

  return (
    <header className="topbar">
      {brand}
      <div className="topbar__end">
        <PublicEnd />
      </div>
    </header>
  )
}
