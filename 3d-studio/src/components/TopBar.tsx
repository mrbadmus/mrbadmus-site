// Header at all three breakpoints (§01/§02/§04/§05). Brand: the reference's
// own drawing of the public-page mark for this surface — two chevrons in
// accent orange, second at 34% opacity, Bricolage wordmark. Nav entries
// beyond the studio are drawn as the reference draws them (inert, muted)
// until the product wires real destinations.

import type { StageMode } from './Stage'
import { BrandMark, MenuIcon } from './icons'

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
  const brand = (
    <a className="brand" href="/index.html">
      <BrandMark size={layout === 'phone' ? 17 : layout === 'tablet' ? 19 : 21} />
      MrBadmusAI
    </a>
  )

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
          onClick={onOpenLibrary}
        >
          <MenuIcon />
        </button>
        {phoneTitle ? (
          <span className="brand" style={{ fontSize: 15 }}>{phoneTitle}</span>
        ) : (
          brand
        )}
        <div className="topbar__end">
          <a className="signin" style={{ fontWeight: 600, fontSize: 13, color: 'var(--st-accent-text)' }} href="/auth.html">
            Sign in
          </a>
        </div>
      </header>
    )
  }

  if (layout === 'tablet') {
    return (
      <header className="topbar">
        <button type="button" className="libtrigger" onClick={onOpenLibrary}>
          <MenuIcon />
          Specimens
        </button>
        {brand}
        <div className="topbar__end">
          <ModeToggle mode={mode} onMode={onMode} />
        </div>
      </header>
    )
  }

  return (
    <header className="topbar">
      {brand}
      <nav className="topbar__nav" aria-label="Site">
        <span>Lessons</span>
        <span>Practice</span>
        <span className="is-here">3D Studio</span>
      </nav>
      <div className="topbar__end">
        <a className="signin" href="/auth.html">Sign in</a>
        <a className="cta" href="/auth.html">Create free account</a>
      </div>
    </header>
  )
}
