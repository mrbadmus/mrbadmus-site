/* ═══════════════════════════════════════════════════════════════════════
   parents/public.js — the shared furniture of the public front door.
   MRB-317 Night 3.

   Four content pages (home, how it works, home education, pricing) carry
   the SAME nav and the SAME footer. Design drew them four times, because a
   `.dc.html` file is a single standalone page and has nowhere to put a
   shared component. Transcribing them four times would be transcribing the
   company's registered entity four times, and the trading name, and the
   five hrefs — and then editing three of the four when one changes.

   So they are written once, here, and each page asks for its own.

   ── EVERY LINK GOES THROUGH `MrBadmusConsumer.href()` ───────────────────
   which carries `?env=` and `?api=` across the hop. A tester on TEST who
   clicks "Pricing" must land on TEST; a developer pointed at port 3107 must
   not have the next page talk to 3000. The public pages are the FIRST hop
   of a signup, so losing the parameters here loses them for the whole flow.

   ── AND EVERY PRICE COMES FROM `MrBadmusConsumer.pricing()` ─────────────
   There is no price constant in this file or in any page that includes it.
   See the note above `pricing()` in consumer-common.js.
   ═══════════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  var C = window.MrBadmusConsumer;
  var esc = C.escapeHtml;

  /* Design sets her BrandMark at size 26 on every public surface; the
     shared constant is drawn at 20 for the consumer nav. Re-stamping the
     two attributes keeps ONE drawing on the estate — the alternative is a
     second copy of the chevron path that can drift from the first, which is
     precisely the brand drift CLAUDE.md warns about. If the constant is
     ever redrawn without those attributes, the replace is a no-op and the
     mark renders at its own size rather than not at all. */
  function brand(size) {
    var px = String(size || 26);
    return C.BRANDMARK.replace('width="20" height="20"',
                               'width="' + px + '" height="' + px + '"');
  }

  var PAGES = {
    home:    { href: '/parents/index.html',          label: 'Home' },
    how:     { href: '/parents/how-it-works.html',   label: 'How it works' },
    homeEd:  { href: '/parents/home-education.html', label: 'Home education' },
    pricing: { href: '/parents/pricing.html',        label: 'Pricing' },
    signIn:  { href: '/parents/sign-in.html',        label: 'Sign in' },
    signUp:  { href: '/consumer/signup.html',        label: 'Start free' }
  };

  function url(key) { return esc(C.href(PAGES[key].href)); }

  /* The company behind the product, written once.

     ⊕ DEVIATION FROM DESIGN, and a deliberate one. Her footer reads
     "Mr Badmus Education Ltd · England". The trading entity is 3rd Eye Ltd
     trading as MrBadmus, so the footer says that instead — a footer is the
     one line on a public site that has to be legally true, and a company
     name nobody is registered under is not a styling choice. Flagged for
     Mide in the run report rather than changed silently. */
  var ENTITY = '3rd Eye Ltd, trading as MrBadmus · England';

  /* ── nav ───────────────────────────────────────────────────────────────
     `current` is 'home' | 'how' | 'homeEd' | 'pricing' | null. The current
     section gets Design's 2px accent underline; the home page marks none,
     exactly as her Public Home does.

     The three section links live inside `.pb-nav-links`, which public.css
     hides below 900px. The brand, "Sign in" and "Start free" are outside
     it and never collapse. */
  function nav(current) {
    function link(key) {
      var on = current === key;
      return '<a href="' + url(key) + '" style="color:var(--ks3-ink)' +
        (on ? ';border-bottom:2px solid var(--ks3-accent)' : '') + '">' +
        esc(PAGES[key].label) + '</a>';
    }
    return '<header class="pb-wrap" style="display:flex;align-items:center;gap:14px;' +
      'padding:18px 20px;border-bottom:2px solid var(--ks3-ink);position:sticky;top:0;' +
      'background:var(--ks3-ground);z-index:5">' +
      '<a href="' + url('home') + '" style="display:flex;align-items:center;gap:10px;color:var(--ks3-ink)">' +
        brand(26) +
        '<span style="font-family:var(--ks3-font-display);font-weight:800;font-size:22px;' +
        'letter-spacing:-.02em">MrBadmus</span>' +
      '</a>' +
      '<nav class="pb-nav-links" style="margin-left:24px;gap:22px;font-weight:600;font-size:16px">' +
        link('how') + link('homeEd') + link('pricing') +
      '</nav>' +
      '<span style="flex:1"></span>' +
      '<a href="' + url('signIn') + '" style="font-weight:700;font-size:16px;color:var(--ks3-ink)">Sign in</a>' +
      '<a href="' + url('signUp') + '" style="display:flex;align-items:center;min-height:44px;' +
      'padding:0 18px;border:2px solid var(--ks3-ink);border-radius:var(--ks3-r-control);' +
      'background:var(--ks3-ink);color:var(--ks3-on-dark);font-weight:700;font-size:16px">Start free</a>' +
      '</header>';
  }

  /* ── footer ─────────────────────────────────────────────────────────── */
  function footer() {
    function link(key) {
      return '<a href="' + url(key) + '">' + esc(PAGES[key].label) + '</a>';
    }
    return '<footer style="border-top:2px solid var(--ks3-ink);background:var(--ks3-card)">' +
      '<div class="pb-wrap" style="max-width:1160px;margin:0 auto;padding:28px 20px;' +
      'display:flex;flex-wrap:wrap;gap:16px 28px;align-items:center;font-size:15px;' +
      'color:var(--ks3-ink-muted)">' +
      '<span style="font-family:var(--ks3-font-display);font-weight:800;font-size:18px;' +
      'letter-spacing:-.02em;color:var(--ks3-ink)">MrBadmus</span>' +
      link('how') + link('homeEd') + link('pricing') + link('signIn') +
      '<span style="margin-left:auto">' + esc(ENTITY) + '</span>' +
      '</div></footer>';
  }

  /* ── money ─────────────────────────────────────────────────────────────
     Design's own formatter, reproduced: a whole number of pounds prints
     without decimals (£79), anything else with both (£9.99). Integer pence
     in, so £5.99 × 3 is never 17.970000000000002.

     `PENDING` is what a price is before `pricing()` answers. It is a single
     neutral character on purpose: "£9.99" would be a guess rendered as a
     fact, and "£0.00" would be a lie in the direction that costs us money. */
  var PENDING = '…';

  function money(pence) {
    if (pence == null || !isFinite(Number(pence))) { return PENDING; }
    var n = Math.round(Number(pence));
    var pounds = Math.floor(n / 100), rem = n % 100;
    if (rem === 0) { return '£' + pounds; }
    return '£' + pounds + '.' + (rem < 10 ? '0' : '') + rem;
  }

  /* ── the tick, the cross, the arrows ───────────────────────────────────
     Inline SVG, never a typed character: the shipped font subsets do not
     carry ✓ ✗ → and a page that types one renders a blank box on a phone.
     Design's exact paths. */
  function mark(path, extraStyle) {
    return '<svg class="ks3-mark" viewBox="0 0 24 24" aria-hidden="true"' +
      (extraStyle ? ' style="' + extraStyle + '"' : '') + '><path d="' + path + '"/></svg>';
  }
  var PATH = {
    tick:  'M5 12.5l4.5 4.5L19 7',
    right: 'M5 12h14M13 6l6 6-6 6',
    down:  'M6 9l6 6 6-6',
    back:  'M15 5l-7 7 7 7',
    plus:  'M12 5v14M5 12h14',
    minus: 'M5 12h14'
  };

  /* ── the accordion (How It Works) ──────────────────────────────────────
     One panel open at a time; clicking the open one closes it. Design's
     state is `{ open: 0 }` — the first question starts open — and her
     chevron rotates 180° when it is.

     Rendered rather than toggled with a class because the collapsed answer
     must not be in the DOM at all: an `<sc-if>` in her file means absent,
     and a screen reader that can reach a "hidden" answer reads the whole
     FAQ as one paragraph. */
  function accordion(el, faqs, state) {
    state = state || { open: 0 };

    function render() {
      el.innerHTML = faqs.map(function (f, i) {
        var open = state.open === i;
        return '<div style="padding:18px 0;border-top:1px solid var(--ks3-dark-rule)">' +
          '<button type="button" data-faq="' + i + '" aria-expanded="' + (open ? 'true' : 'false') + '" ' +
          'style="display:flex;justify-content:space-between;align-items:center;gap:16px;width:100%;' +
          'padding:0;border:0;background:none;text-align:left;font-weight:700;font-size:19px;' +
          'color:var(--ks3-on-dark);cursor:pointer">' + esc(f.q) +
          mark(PATH.down, 'width:18px;height:18px;flex:0 0 auto;transform:' +
               (open ? 'rotate(180deg)' : 'none') + ';transition:transform .15s') +
          '</button>' +
          (open ? '<p style="margin:12px 0 0;font-size:17px;color:var(--ks3-on-dark-body);' +
                  'max-width:60em">' + esc(f.a) + '</p>' : '') +
          '</div>';
      }).join('');
    }

    el.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-faq]');
      if (!btn) { return; }
      var i = Number(btn.getAttribute('data-faq'));
      state.open = state.open === i ? -1 : i;
      render();
    });

    render();
  }

  /* ── a plain (always-open) FAQ list — Pricing and Home Education ─────── */
  function faqList(el, faqs) {
    el.innerHTML = faqs.map(function (f) {
      return '<div style="padding:18px 0;border-bottom:1px solid var(--ks3-rule)">' +
        '<p style="margin:0;font-weight:700;font-size:19px">' + esc(f.q) + '</p>' +
        '<p style="margin:8px 0 0;font-size:17px;color:var(--ks3-ink-body);max-width:60em">' +
        esc(f.a) + '</p></div>';
    }).join('');
  }

  /* ── year tabs (Home Education's scheme-of-work browser) ───────────────
     Design's exact treatment: the selected year is ink-filled with a 2px
     ink border, the others are transparent with a transparent border so
     nothing shifts by two pixels when the selection moves. */
  function yearTabs(years, selected) {
    return years.map(function (n) {
      var on = n === selected;
      return '<button type="button" data-year="' + n + '" aria-pressed="' + (on ? 'true' : 'false') + '" ' +
        'style="flex:1;min-height:38px;border:2px solid ' + (on ? 'var(--ks3-ink)' : 'transparent') +
        ';border-radius:10px;background:' + (on ? 'var(--ks3-ink)' : 'transparent') +
        ';color:' + (on ? 'var(--ks3-on-dark)' : 'var(--ks3-ink)') +
        ';font-weight:700;font-size:15px;cursor:pointer">Y' + n + '</button>';
    }).join('');
  }

  /* The subject dot, Design's map. 'All three' takes the neutral band
     colour because a bridging unit belongs to no single science. */
  var SUBJECT_DOT = {
    Biology: 'var(--ks3-biology)',
    Chemistry: 'var(--ks3-chemistry)',
    Physics: 'var(--ks3-physics)',
    'All three': 'var(--ks3-band)'
  };

  /* Mount nav + footer on a page that has the two hosts. Every page calls
     this from inside `boot()`, so nothing is drawn on the off path. */
  function chrome(current) {
    var n = document.getElementById('pb-nav');
    var f = document.getElementById('pb-footer');
    if (n) { n.outerHTML = nav(current); }
    if (f) { f.outerHTML = footer(); }
  }

  window.MrBadmusPublic = {
    PAGES: PAGES,
    PENDING: PENDING,
    PATH: PATH,
    SUBJECT_DOT: SUBJECT_DOT,
    brand: brand,
    url: url,
    nav: nav,
    footer: footer,
    chrome: chrome,
    money: money,
    mark: mark,
    accordion: accordion,
    faqList: faqList,
    yearTabs: yearTabs
  };
})();
