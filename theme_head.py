"""The site-wide theme hooks every generator emits (theme run, 26 Sep 2026).

ONE definition, imported by every generator and by the hand-written-page
stamper, so the pre-paint snippet is byte-identical on every page and a gate
can check for it by equality.

THEME_HEAD   — goes as early in <head> as possible (right after <meta charset>).
               Writes <html data-theme="light|dark" data-theme-pref=...> before
               first paint, so no page ever flashes the wrong theme. Light is the
               default and the fallback for anything it cannot read (Mide's
               ruling, 26 Sep 2026); a stored "dark" or "system" always wins,
               and System, once chosen, follows prefers-color-scheme.
               ⊕ Restored 9 Oct 2026. 48f2dd4d0 briefly made System the default
               for a fresh device; Mide ruled that a mistake in his brief and
               restored Light. The System-default form is now the legacy entry
               in LEGACY_THEME_HEADS, so the next build rewrites it everywhere.
THEME_SCRIPT — the shared control and persistence (shared/theme.js); `v` is the
               cache-bust stamp the caller already computes for shared assets.
THEME_SLOT   — the header slot the control mounts into.
"""

STORAGE_KEY = "mrb-theme"

THEME_HEAD = (
    "<script>(function(){var p='light';try{p=localStorage.getItem('mrb-theme')||'light'}catch(e){}"
    "if(p!=='dark'&&p!=='system')p='light';"
    "var d=p==='dark'||(p==='system'&&!!window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches),"
    "r=document.documentElement;r.setAttribute('data-theme',d?'dark':'light');"
    "r.setAttribute('data-theme-pref',p);r.style.colorScheme=d?'dark':'light'})()</script>"
)

# Every earlier byte-form of THEME_HEAD. Hand-written pages (root pages,
# parents/, consumer/, go/, org/, student/, teacher/, simulations/) carry the
# snippet literally in their <head>, so a change here would otherwise leave
# them on the old default. generate_site_v5.py runs stamp_theme_head() over
# every hand-written page on every build (next to brand.stamp_brand), and the
# round-trip writes the result back over the source, so the source always
# holds the current snippet. Append when THEME_HEAD changes; never list the
# current THEME_HEAD here (stamp_theme_head skips it if someone does).
LEGACY_THEME_HEADS = (
    # 48f2dd4d0 (9 Oct 2026) — System was the default for a fresh device.
    # Reverted the same day on Mide's ruling: Light is the default again (the
    # 26 Sep theme-run form, which is THEME_HEAD above once more).
    "<script>(function(){var p='system';try{p=localStorage.getItem('mrb-theme')||'system'}catch(e){}"
    "if(p!=='dark'&&p!=='light')p='system';"
    "var d=p==='dark'||(p==='system'&&!!window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches),"
    "r=document.documentElement;r.setAttribute('data-theme',d?'dark':'light');"
    "r.setAttribute('data-theme-pref',p);r.style.colorScheme=d?'dark':'light'})()</script>",
)


def stamp_theme_head(html: str) -> str:
    """Replace any earlier form of the pre-paint snippet with THEME_HEAD.

    Returns the page unchanged when it carries no legacy snippet.
    """
    for old in LEGACY_THEME_HEADS:
        if old != THEME_HEAD and old in html:
            html = html.replace(old, THEME_HEAD)
    return html


THEME_SLOT = '<span class="mrb-theme-slot" data-mrb-theme></span>'


def theme_script(v: str = "") -> str:
    q = f"?v={v}" if v else ""
    return f'<script src="/shared/theme.js{q}" defer></script>'
