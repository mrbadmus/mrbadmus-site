"""The site-wide theme hooks every generator emits (theme run, 26 Sep 2026).

ONE definition, imported by every generator and by the hand-written-page
stamper, so the pre-paint snippet is byte-identical on every page and a gate
can check for it by equality.

THEME_HEAD   — goes as early in <head> as possible (right after <meta charset>).
               Writes <html data-theme="light|dark" data-theme-pref=...> before
               first paint, so no page ever flashes the wrong theme. Light is the
               default and the fallback for anything it cannot read.
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

THEME_SLOT = '<span class="mrb-theme-slot" data-mrb-theme></span>'


def theme_script(v: str = "") -> str:
    q = f"?v={v}" if v else ""
    return f'<script src="/shared/theme.js{q}" defer></script>'
