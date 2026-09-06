/* mrb327_safari_drive.js — MRB-327 §2, the Safari lane.
 *
 *   node mrb327_safari_drive.js --engine webkit
 *   node mrb327_safari_drive.js --engine chromium
 *
 * safaridriver cannot be enabled without an admin password and a GUI toggle,
 * so the equivalent that proves the same property is Playwright's WebKit —
 * the engine Safari renders with. That catches CSS and JS engine differences.
 * It does NOT catch Safari-the-application (its print dialogue, its PDF
 * export, iOS viewport chrome); those are named in the report as unproven.
 *
 * Run from the scratchpad/pw directory so `require('playwright')` resolves.
 */
const fs = require('fs');
const path = require('path');
const playwright = require('playwright');

const SCRATCH = '/private/tmp/claude-501/-Users-midebadmus-Documents-GitHub-mrbadmus-worktrees-b2c-launch/06d799b1-12f9-481b-9871-424a2321715f/scratchpad';
const STATE = JSON.parse(fs.readFileSync(path.join(SCRATCH, 'safari_fixtures.json'), 'utf8'));
const BASE = 'http://localhost:8171';
const API = 'http://localhost:3100';
const SB_KEY = 'sb-qeppkiswvclkkwbxmlok-auth-token';

const argv = process.argv.slice(2);
const ENGINE = (argv[argv.indexOf('--engine') + 1]) || 'webkit';
const SHOTS = path.join(SCRATCH, 'shots', 'safari', ENGINE);
fs.mkdirSync(SHOTS, { recursive: true });

/* Survives shared/config.js overwriting window.MrBadmusConfig — same setter
 * admin_ui_drive.py uses (FLAG_ON_JS). */
const FLAG_ON_JS = `(function(){var c=null;Object.defineProperty(window,'MrBadmusConfig',{configurable:true,
  get:function(){return c;}, set:function(v){ if(v&&typeof v==='object'){v.CONSUMER_SIGNUP_ENABLED=true;} c=v; }});})();`;

const qs = (p) => BASE + p + (p.includes('?') ? '&' : '?') + 'env=test&api=' + API;

let CHILD_CTX = null;
const results = {};
function record(key, value) { results[key] = value; }

/* ── the in-page measurement. Deliberately engine-neutral: it asks the DOM
 *    questions whose answers are facts about layout, not about the browser. */
const MEASURE = `(function () {
  var vw = document.documentElement.clientWidth;
  var se = document.scrollingElement || document.documentElement;

  // Anything sticking out to the right of the viewport, ignoring things that
  // are deliberately off-canvas (a hidden rail, an aria-live sink).
  var over = [];
  var all = document.querySelectorAll('body *');
  for (var i = 0; i < all.length; i++) {
    var el = all[i];
    var cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || cs.position === 'fixed') continue;
    var r = el.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) continue;
    if (r.right > vw + 1) {
      over.push({
        tag: el.tagName.toLowerCase(),
        id: el.id || null,
        cls: (el.className && el.className.baseVal !== undefined ? el.className.baseVal : el.className) || null,
        right: Math.round(r.right), width: Math.round(r.width),
        text: (el.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 60)
      });
    }
  }
  // Only the outermost offenders — a wide parent makes every child look wide.
  var outer = over.filter(function (o, ix) {
    return !over.some(function (p, px) { return px !== ix && p.right >= o.right && p.width > o.width; });
  }).slice(0, 12);

  function probe(sel) {
    var el = document.querySelector(sel);
    if (!el) return null;
    var r = el.getBoundingClientRect();
    return { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
  }

  var text = (document.body.innerText || '').replace(/\\s+/g, ' ').trim();

  return {
    viewport: { w: vw, h: document.documentElement.clientHeight },
    scrollWidth: Math.round(se.scrollWidth),
    scrollHeight: Math.round(se.scrollHeight),
    overflowX: Math.round(se.scrollWidth - se.clientWidth),
    overflowing: outer,
    textLen: text.length,
    text: text.slice(0, 4000),
    probes: {
      main: probe('main') || probe('#c-main') || probe('#su-main'),
      h1: probe('h1'),
      sheet: probe('.rpt-sheet'),
      timer: probe('#uc-timer'),
      rail: probe('.su-rail')
    }
  };
})()`;

async function measure(page) {
  const m = await page.evaluate(MEASURE);
  /* A child surface that has silently become the login page measures
     perfectly and means nothing. Every child-surface record carries this. */
  m.bouncedToLogin = /Who’s this\?/.test(m.text) || /\/go\//.test(page.url());
  return m;
}

function newErrs(page) {
  const errs = [];
  page.on('console', (m) => { if (m.type() === 'error') errs.push(m.text()); });
  page.on('pageerror', (e) => errs.push('PAGEERROR: ' + String(e && e.message || e)));
  return errs;
}
const cleanErrs = (e) => e.filter((x) =>
  !/favicon\.ico/.test(x) && !/Failed to load resource.*(40\d|409|423|429)/.test(x));

async function seed(ctx, session) {
  const p = await ctx.newPage();
  await p.goto(BASE + '/404.html?env=test');
  await p.evaluate(([k, v]) => { localStorage.clear(); localStorage.setItem(k, v); },
                   [SB_KEY, JSON.stringify(session)]);
  await p.close();
}

async function main() {
  const browser = await playwright[ENGINE].launch();
  console.log('\n══ ' + ENGINE + ' ' + browser.version() + ' ══');

  // ───────────────────────────────────────────────────── 6. child login
  {
    const ctx = await browser.newContext({ viewport: { width: 390, height: 844 } });
    await ctx.addInitScript(FLAG_ON_JS);
    const page = await ctx.newPage();
    const errs = newErrs(page);
    await page.goto(qs('/go/index.html'), { waitUntil: 'networkidle' });
    await page.waitForSelector('#gl-form', { timeout: 15000 });
    const before = await measure(page);
    await page.screenshot({ path: path.join(SHOTS, '6-go-login-390.png'), fullPage: true });

    await page.fill('#gl-user', STATE.child_username);
    await page.fill('#gl-pass', STATE.child_password);
    // The Show/Hide control — a type swap, which is where WebKit has historically
    // dropped the value or the caret.
    await page.click('#gl-show');
    const shownType = await page.getAttribute('#gl-pass', 'type');
    const shownVal = await page.inputValue('#gl-pass');
    await page.click('#gl-show');

    await page.click('#gl-go');
    let landed = null;
    try {
      await page.waitForURL(/consumer\/today\.html/, { timeout: 25000 });
      landed = page.url();
    } catch (e) { landed = 'DID NOT NAVIGATE: ' + page.url(); }
    await page.waitForTimeout(1500);
    await page.screenshot({ path: path.join(SHOTS, '6-go-after-login.png') });

    record('6_go_login', {
      before, landed,
      showToggle: { type: shownType, valueKept: shownVal === STATE.child_password },
      errors: cleanErrs(errs)
    });
    console.log('  6 go/login      →', landed);
    await page.close();
    CHILD_CTX = ctx;   // the SDK wrote a REAL child session into this context
  }

  // ─────────────────────────────────── 2/3/4. child surfaces at 390px
  {
    /* Reuse the context the child actually signed in on. Writing the
       /child/login response into localStorage by hand does NOT work: that
       response is {access_token, refresh_token}, not a Supabase session
       object, and the SDK deletes what it cannot parse — which is exactly
       how the first run of this drive silently measured the login page six
       times instead of the six surfaces. */
    const ctx = CHILD_CTX;

    // 2 — Today
    {
      const page = await ctx.newPage();
      const errs = newErrs(page);
      await page.goto(qs('/consumer/today.html'), { waitUntil: 'networkidle' });
      await page.waitForFunction(() => /Amara/.test(document.body.innerText), null, { timeout: 20000 })
        .catch(() => {});
      await page.waitForTimeout(1200);
      const m = await measure(page);
      await page.screenshot({ path: path.join(SHOTS, '2-today-390.png'), fullPage: true });
      // The date string on this page comes from toLocaleDateString — Intl is a
      // real engine seam, so capture the exact string both engines produced.
      const dates = await page.evaluate(() =>
        (document.body.innerText.match(/\b\d{1,2}\s+\w+|\w+day\b|\b\w+ \d{1,2}\b/g) || []).slice(0, 8));
      record('2_today', { ...m, dates, errors: cleanErrs(errs) });
      console.log('  2 today         → overflowX=' + m.overflowX + ' errs=' + cleanErrs(errs).length);
      await page.close();
    }

    // 3 — Exam questions
    {
      const page = await ctx.newPage();
      const errs = newErrs(page);
      await page.goto(qs('/consumer/exam.html'), { waitUntil: 'networkidle' });
      await page.waitForTimeout(2500);
      const m = await measure(page);
      await page.screenshot({ path: path.join(SHOTS, '3-exam-390.png'), fullPage: true });
      // The textarea a child writes into is the thing that must not overflow.
      const ta = await page.evaluate(() => {
        var t = document.querySelector('textarea');
        if (!t) return null;
        var r = t.getBoundingClientRect(), cs = getComputedStyle(t);
        return { w: Math.round(r.width), right: Math.round(r.right),
                 fontSize: cs.fontSize, resize: cs.resize,
                 appearance: cs.webkitAppearance || cs.appearance };
      });
      record('3_exam', { ...m, textarea: ta, errors: cleanErrs(errs) });
      console.log('  3 exam          → overflowX=' + m.overflowX + ' errs=' + cleanErrs(errs).length);
      await page.close();
    }

    // 4 — Unit check, including the timer
    {
      const page = await ctx.newPage();
      const errs = newErrs(page);
      await page.goto(qs('/consumer/unit-check.html?unit=B1'), { waitUntil: 'networkidle' });
      await page.waitForSelector('#uc-start', { timeout: 20000 }).catch(() => {});
      const intro = await measure(page);
      await page.screenshot({ path: path.join(SHOTS, '4-unitcheck-intro-390.png'), fullPage: true });

      let timer = { started: false };
      if (await page.$('#uc-start')) {
        await page.click('#uc-start');
        await page.waitForFunction(
          () => { var t = document.getElementById('uc-timer'); return t && !t.hidden; },
          null, { timeout: 20000 }).catch(() => {});
        const t1 = await page.textContent('#uc-clock').catch(() => null);
        await page.waitForTimeout(5000);
        const t2 = await page.textContent('#uc-clock').catch(() => null);
        const toS = (s) => { const m2 = /(\d+):(\d+)/.exec(s || ''); return m2 ? (+m2[1] * 60 + +m2[2]) : null; };
        timer = { started: true, t1, t2, delta: (toS(t1) != null && toS(t2) != null) ? toS(t1) - toS(t2) : null };
      }
      const inCheck = await measure(page);
      await page.screenshot({ path: path.join(SHOTS, '4-unitcheck-question-390.png'), fullPage: true });
      record('4_unit_check', { intro, inCheck, timer, errors: cleanErrs(errs) });
      console.log('  4 unit-check    → overflowX=' + inCheck.overflowX + ' timer ' +
                  JSON.stringify(timer.t1) + '→' + JSON.stringify(timer.t2) +
                  ' (Δ' + timer.delta + 's) errs=' + cleanErrs(errs).length);
      await page.close();
    }
    await ctx.close();
  }

  // ───────────────────────────────────────────── 5. checkout-return polling
  {
    const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 } });
    await ctx.addInitScript(FLAG_ON_JS);
    await seed(ctx, STATE.parent_session);
    const page = await ctx.newPage();
    const errs = newErrs(page);

    // Count the polls for real, off the network, not off a promise we control.
    const polls = [];
    page.on('request', (r) => {
      if (/\/api\/consumer\/family(\?|$)/.test(r.url())) polls.push(Date.now());
    });

    // Ask the harness to put the subscription back to `none` — the real
    // pre-webhook state, which is what makes this page poll at all.
    fs.writeFileSync(path.join(SCRATCH, 'poll_mode_' + ENGINE), '1');
    for (let i = 0; i < 60 && !fs.existsSync(path.join(SCRATCH, 'poll_ready_' + ENGINE)); i++) {
      await page.waitForTimeout(500);
    }

    await page.goto(qs('/consumer/checkout-return.html'), { waitUntil: 'commit' });
    await page.waitForTimeout(9000);
    const pollingShot = await measure(page);
    await page.screenshot({ path: path.join(SHOTS, '5-checkout-polling.png'), fullPage: true });
    const intervals = polls.slice(1).map((t, i) => t - polls[i]);

    record('5_checkout_polling', {
      pollCount: polls.length, intervals,
      waitingText: pollingShot.text.slice(0, 300),
      spinnerAnimating: await page.evaluate(() => {
        var d = document.querySelector('#su-main div[style*="pb-spin"]');
        if (!d) return null;
        var cs = getComputedStyle(d);
        return { name: cs.animationName, dur: cs.animationDuration, state: cs.animationPlayState };
      }),
      rail: pollingShot.probes.rail,
      errors: cleanErrs(errs)
    });
    console.log('  5 checkout poll → ' + polls.length + ' polls, gaps ' + JSON.stringify(intervals));

    // Now let the harness settle it; the page must STOP polling and draw.
    fs.writeFileSync(path.join(SCRATCH, 'settle_now_' + ENGINE), '1');
    const t0 = Date.now();
    let settled = false;
    while (Date.now() - t0 < 40000) {
      const txt = await page.evaluate(() => document.body.innerText);
      if (/first week is ready|Go to my dashboard/.test(txt)) { settled = true; break; }
      await page.waitForTimeout(500);
    }
    const nAtSettle = polls.length;
    await page.waitForTimeout(8000);   // did it keep polling after arriving?
    const m = await measure(page);
    await page.screenshot({ path: path.join(SHOTS, '5-checkout-settled.png'), fullPage: true });
    record('5_checkout_settled', {
      settled, pollsAtSettle: nAtSettle, pollsAfter: polls.length - nAtSettle,
      terminated: polls.length === nAtSettle,
      msToSettle: Date.now() - t0, ...m, errors: cleanErrs(errs)
    });
    console.log('  5 checkout end  → settled=' + settled + ' polls stopped=' +
                (polls.length === nAtSettle) + ' overflowX=' + m.overflowX);
    await ctx.close();
  }

  // ────────────────────────────────────────────── 1. termly report + print
  {
    const ctx = await browser.newContext({ viewport: { width: 1280, height: 1000 } });
    await ctx.addInitScript(FLAG_ON_JS);
    await seed(ctx, STATE.parent_session);
    const page = await ctx.newPage();
    const errs = newErrs(page);
    await page.goto(qs('/consumer/report.html?child=' + STATE.child + '&term=autumn-2026'),
                    { waitUntil: 'networkidle' });
    await page.waitForFunction(() => /Amara/.test(document.body.innerText), null, { timeout: 20000 })
      .catch(() => {});
    await page.waitForTimeout(1000);

    const screen = await measure(page);
    await page.screenshot({ path: path.join(SHOTS, '1-report-screen.png'), fullPage: true });

    // ── print media. WebKit in Playwright cannot make a PDF, so the A4 page
    //    box is emulated: 210mm × 297mm at 96dpi = 794 × 1123 CSS px.
    await page.setViewportSize({ width: 794, height: 1123 });
    await page.emulateMedia({ media: 'print' });
    await page.waitForTimeout(600);

    const print = await page.evaluate(() => {
      var PAGE_H = 1123, PAGE_W = 794;
      var se = document.scrollingElement || document.documentElement;
      var sheet = document.querySelector('.rpt-sheet');
      var sr = sheet ? sheet.getBoundingClientRect() : null;
      var cs = sheet ? getComputedStyle(sheet) : null;

      var actions = document.querySelector('.rpt-actions');
      var actionsHidden = !actions || getComputedStyle(actions).display === 'none';

      // Anything wider than the page box, and anything a fold would cut through
      // that asked not to be cut.
      var tooWide = [], split = [];
      var els = document.querySelectorAll('.rpt-sheet *');
      for (var i = 0; i < els.length; i++) {
        var el = els[i], c = getComputedStyle(el);
        if (c.display === 'none' || c.visibility === 'hidden') continue;
        var r = el.getBoundingClientRect();
        if (r.width < 1 || r.height < 1) continue;
        if (r.right > PAGE_W + 1) {
          tooWide.push({ tag: el.tagName.toLowerCase(), cls: String(el.className || ''),
                         right: Math.round(r.right), w: Math.round(r.width),
                         text: (el.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 50) });
        }
        var top = r.top + se.scrollTop, bot = top + r.height;
        var pTop = Math.floor(top / PAGE_H), pBot = Math.floor((bot - 1) / PAGE_H);
        if (pTop !== pBot) {
          var avoid = /avoid/.test(c.breakInside || '') || /avoid/.test(c.pageBreakInside || '');
          if (avoid || el.classList.contains('rpt-keep')) {
            split.push({ tag: el.tagName.toLowerCase(), cls: String(el.className || ''),
                         breakInside: c.breakInside, pageBreakInside: c.pageBreakInside,
                         topPage: pTop + 1, botPage: pBot + 1, h: Math.round(r.height),
                         text: (el.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 50) });
          }
        }
      }
      // Section headings that would land in the last 60px of a page — an
      // orphaned heading is the classic print defect.
      var orphan = [];
      var hs = document.querySelectorAll('.rpt-h2');
      for (var j = 0; j < hs.length; j++) {
        var hr = hs[j].getBoundingClientRect();
        var ht = hr.top + se.scrollTop;
        var off = ht % PAGE_H;
        if (off > PAGE_H - 90) {
          orphan.push({ text: hs[j].textContent.trim().slice(0, 40),
                        page: Math.floor(ht / PAGE_H) + 1, fromBottom: Math.round(PAGE_H - off) });
        }
      }

      return {
        docHeight: Math.round(se.scrollHeight),
        pages: Math.ceil(se.scrollHeight / PAGE_H),
        lastPageFill: Math.round(se.scrollHeight % PAGE_H),
        sheet: sr ? { x: Math.round(sr.x), w: Math.round(sr.width), h: Math.round(sr.height) } : null,
        sheetPadding: cs ? cs.padding : null,
        sheetWidthRule: cs ? cs.width : null,
        rootBg: getComputedStyle(document.querySelector('.rpt-root')).backgroundColor,
        actionsHidden, tooWide, split, orphan,
        overflowX: Math.round(se.scrollWidth - se.clientWidth),
        headingCount: hs.length,
        // Does the engine even understand the modern property?
        breakSupport: {
          breakInside: CSS.supports('break-inside', 'avoid'),
          pageBreakInside: CSS.supports('page-break-inside', 'avoid'),
          pageSize: CSS.supports('size', 'A4')
        }
      };
    });

    // One screenshot per emulated A4 page.
    const pageCount = Math.min(print.pages, 6);
    for (let i = 0; i < pageCount; i++) {
      await page.evaluate((y) => window.scrollTo(0, y), i * 1123);
      await page.waitForTimeout(200);
      await page.screenshot({ path: path.join(SHOTS, '1-report-print-p' + (i + 1) + '.png') });
    }
    await page.emulateMedia({ media: 'screen' });
    record('1_report', { screen, print, errors: cleanErrs(errs) });
    console.log('  1 report        → print pages=' + print.pages + ' sheet.w=' +
                (print.sheet && print.sheet.w) + ' tooWide=' + print.tooWide.length +
                ' split=' + print.split.length + ' orphan=' + print.orphan.length +
                ' actionsHidden=' + print.actionsHidden);
    await ctx.close();
  }

  await browser.close();
  results._engine = ENGINE;
  results._version = null;
  fs.writeFileSync(path.join(SCRATCH, 'safari_' + ENGINE + '.json'), JSON.stringify(results, null, 1));
  console.log('  → ' + path.join(SCRATCH, 'safari_' + ENGINE + '.json'));
}

main().catch((e) => { console.error('FATAL', e); process.exit(1); });
