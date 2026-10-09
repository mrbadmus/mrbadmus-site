"""The site-wide theme hooks every generator emits (theme run, 26 Sep 2026).

ONE definition, imported by every generator and by the hand-written-page
stamper, so the pre-paint snippet is byte-identical on every page and a gate
can check for it by equality.

THEME_HEAD   — goes as early in <head> as possible (right after <meta charset>).
               Writes <html data-theme="light|dark" data-theme-pref=...> before
               first paint, so no page ever flashes the wrong theme. With no
               stored choice (a fresh device) the preference is SYSTEM, which
               follows the device's prefers-color-scheme; a stored explicit
               "light" or "dark" always wins. Anything unreadable is System too.
               ⊕ B2C polish (9 Oct 2026): this used to default to Light, so a
               fresh phone in dark mode opened every page in Light with the
               Light option selected (blind journey run). See LEGACY_THEME_HEADS.
THEME_SCRIPT — the shared control and persistence (shared/theme.js); `v` is the
               cache-bust stamp the caller already computes for shared assets.
THEME_SLOT   — the header slot the control mounts into.
"""

STORAGE_KEY = "mrb-theme"

THEME_HEAD = (
    "<script>(function(){var p='system';try{p=localStorage.getItem('mrb-theme')||'system'}catch(e){}"
    "if(p!=='dark'&&p!=='light')p='system';"
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
# holds the current snippet. Append — never edit — when THEME_HEAD changes.
LEGACY_THEME_HEADS = (
    # Theme run, 26 Sep 2026 — Light was the default for a fresh device.
    "<script>(function(){var p='light';try{p=localStorage.getItem('mrb-theme')||'light'}catch(e){}"
    "if(p!=='dark'&&p!=='system')p='light';"
    "var d=p==='dark'||(p==='system'&&!!window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches),"
    "r=document.documentElement;r.setAttribute('data-theme',d?'dark':'light');"
    "r.setAttribute('data-theme-pref',p);r.style.colorScheme=d?'dark':'light'})()</script>",
)


def stamp_theme_head(html: str) -> str:
    """Replace any earlier form of the pre-paint snippet with THEME_HEAD.

    Returns the page unchanged when it carries no legacy snippet.
    """
    for old in LEGACY_THEME_HEADS:
        if old in html:
            html = html.replace(old, THEME_HEAD)
    return html


THEME_SLOT = '<span class="mrb-theme-slot" data-mrb-theme></span>'


def theme_script(v: str = "") -> str:
    q = f"?v={v}" if v else ""
    return f'<script src="/shared/theme.js{q}" defer></script>'
