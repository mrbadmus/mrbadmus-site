/* mrb327_safari_drive_probe.js — MRB-327 §2, second pass.
 *
 * The first pass loaded each surface. This one goes INTO the two that have a
 * second state worth measuring (the exam writing view, the report on a phone)
 * and then probes, on a real page of the estate, the specific WebKit-vs-Blink
 * seams the brief names — so a "no difference" is a measurement, not a shrug.
 *
 *   NODE_PATH=<pw>/node_modules node mrb327_safari_drive_probe.js --engine webkit
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

const FLAG_ON_JS = `(function(){var c=null;Object.defineProperty(window,'MrBadmusConfig',{configurable:true,
  get:function(){return c;}, set:function(v){ if(v&&typeof v==='object'){v.CONSUMER_SIGNUP_ENABLED=true;} c=v; }});})();`;
const qs = (p) => BASE + p + (p.includes('?') ? '&' : '?') + 'env=test&api=' + API;
const out = {};

const overflowProbe = `(function(){
  var vw = document.documentElement.clientWidth;
  var se = document.scrollingElement || document.documentElement;
  var over = [];
  var all = document.querySelectorAll('body *');
  for (var i=0;i<all.length;i++){
    var el=all[i], cs=getComputedStyle(el);
    if(cs.display==='none'||cs.visibility==='hidden'||cs.position==='fixed') continue;
    var r=el.getBoundingClientRect();
    if(r.width<1||r.height<1) continue;
    if(r.right>vw+1) over.push({tag:el.tagName.toLowerCase(), cls:String(el.className||'').slice(0,40),
      right:Math.round(r.right), w:Math.round(r.width),
      text:(el.textContent||'').replace(/\\s+/g,' ').trim().slice(0,50)});
  }
  return {overflowX: Math.round(se.scrollWidth-se.clientWidth), count: over.length, over: over.slice(0,8)};
})()`;

async function main() {
  const browser = await playwright[ENGINE].launch();
  console.log('\n══ probe ' + ENGINE + ' ' + browser.version() + ' ══');

  const ctx = await browser.newContext({ viewport: { width: 390, height: 844 } });
  await ctx.addInitScript(FLAG_ON_JS);

  // Sign the child in for real; the SDK writes the session this context needs.
  {
    const p = await ctx.newPage();
    await p.goto(qs('/go/index.html'), { waitUntil: 'networkidle' });
    await p.fill('#gl-user', STATE.child_username);
    await p.fill('#gl-pass', STATE.child_password);
    await p.click('#gl-go');
    await p.waitForURL(/consumer\/today\.html/, { timeout: 25000 });
    await p.close();
  }

  // ── 3b. exam.html: into a question, where the child actually writes ──────
  {
    const page = await ctx.newPage();
    const errs = [];
    page.on('pageerror', (e) => errs.push('PAGEERROR: ' + e.message));
    await page.goto(qs('/consumer/exam.html'), { waitUntil: 'networkidle' });
    await page.waitForTimeout(2500);

    // Whatever the page offers as a question to open — by role, not by a
    // selector guessed from the source, so this survives markup churn.
    /* Open an UNANSWERED question. The fixture family has four marked
       answers already, and a marked question opens on its mark rather than
       on a writing box — which is how the first probe run measured
       `textarea: null` and proved nothing about the surface a child types on. */
    await page.evaluate(() => {
      var t = Array.from(document.querySelectorAll('button, [role="tab"], a'))
        .find(function (e) { return /Not done yet/i.test((e.textContent || '').trim()); });
      if (t) t.click();
    });
    await page.waitForTimeout(1200);
    const opened = await page.evaluate(() => {
      var cands = Array.from(document.querySelectorAll('button, [role="button"], li[tabindex], a'))
        .filter(function (e) {
          var t = (e.textContent || '').trim();
          return t.length > 25 && /\?|\bExplain\b|\bDescribe\b|\bWhy\b|marks/i.test(t)
                 && !/YOUR MARK|\/\d/.test(t);
        });
      if (!cands.length) return null;
      cands[0].click();
      return (cands[0].textContent || '').trim().slice(0, 60);
    });
    await page.waitForTimeout(2000);
    const ta = await page.evaluate(() => {
      var t = document.querySelector('textarea');
      if (!t) return null;
      var r = t.getBoundingClientRect(), cs = getComputedStyle(t);
      return { w: Math.round(r.width), h: Math.round(r.height), right: Math.round(r.right),
               fontSize: cs.fontSize, lineHeight: cs.lineHeight, resize: cs.resize,
               appearance: cs.webkitAppearance || cs.appearance,
               borderRadius: cs.borderRadius, boxSizing: cs.boxSizing };
    });
    let typed = null;
    if (ta) {
      // A real child typing. 16px or larger is what stops iOS Safari zooming
      // the whole page on focus, so the font-size above is load-bearing.
      await page.fill('textarea', 'The chloroplast is wider than a mitochondrion so the microscope can separate it. '
        + 'The membrane is thinner again. Both are still there.');
      await page.waitForTimeout(400);
      typed = await page.evaluate(() => {
        var t = document.querySelector('textarea');
        return { len: t.value.length, scrollH: t.scrollHeight, clientH: t.clientHeight };
      });
    }
    const ov = await page.evaluate(overflowProbe);
    await page.screenshot({ path: path.join(SHOTS, '3b-exam-writing-390.png'), fullPage: true });
    out.exam_writing = { opened, textarea: ta, typed, overflow: ov, errors: errs,
                         text: (await page.evaluate(() => document.body.innerText)).replace(/\s+/g, ' ').slice(0, 600) };
    console.log('  3b exam writing → opened=' + JSON.stringify(opened) + ' ta=' + JSON.stringify(ta));
    await page.close();
  }

  // ── the WebKit seams, measured on a real page of the estate ─────────────
  {
    const page = await ctx.newPage();
    await page.goto(qs('/consumer/today.html'), { waitUntil: 'networkidle' });
    await page.waitForTimeout(1500);
    out.seams = await page.evaluate(() => {
      function sup(prop, val) { try { return CSS.supports(prop, val); } catch (e) { return 'THREW'; } }
      var root = document.querySelector('.rd') || document.body;
      var rcs = getComputedStyle(root);
      var d = new Date('2026-09-06T09:30:00Z');
      return {
        units: {
          vh: sup('height', '100vh'), dvh: sup('height', '100dvh'),
          svh: sup('height', '100svh'), lvh: sup('height', '100lvh')
        },
        // What 100vh actually RESOLVED to on this page's root, against the
        // viewport the engine reports. Equal means no dynamic-viewport gap
        // here — which is true of every desktop engine, Blink included.
        vhResolved: { minHeight: rcs.minHeight, innerHeight: window.innerHeight,
                      clientHeight: document.documentElement.clientHeight },
        css: {
          sticky: sup('position', 'sticky'),
          gap: sup('gap', '10px'), flexGap: sup('column-gap', '10px'),
          backdropFilter: sup('backdrop-filter', 'blur(4px)') || sup('-webkit-backdrop-filter', 'blur(4px)'),
          scrollBehaviorSmooth: sup('scroll-behavior', 'smooth'),
          has: sup('selector(:has(a))'),
          aspectRatio: sup('aspect-ratio', '1/1'),
          textWrapBalance: sup('text-wrap', 'balance'),
          breakInside: sup('break-inside', 'avoid'),
          pageBreakInside: sup('page-break-inside', 'avoid'),
          pageSizeDescriptor: sup('size', 'A4'),
          inset: sup('inset', '0'), gridTemplate: sup('display', 'grid'),
          overscroll: sup('overscroll-behavior', 'contain'),
          webkitOverflowScrolling: sup('-webkit-overflow-scrolling', 'touch'),
          colorMix: sup('color', 'color-mix(in srgb, red, blue)')
        },
        js: {
          scrollBehaviorInScrollTo: 'scrollBehavior' in document.documentElement.style,
          scrollIntoViewSmooth: typeof Element.prototype.scrollIntoView === 'function',
          structuredClone: typeof structuredClone === 'function',
          replaceAll: typeof ''.replaceAll === 'function',
          atFn: typeof [].at === 'function',
          lookbehind: (function () { try { new RegExp('(?<=a)b'); return true; } catch (e) { return false; } })(),
          numFormat: typeof Intl.NumberFormat === 'function',
          relTime: typeof Intl.RelativeTimeFormat === 'function',
          listFormat: typeof Intl.ListFormat === 'function',
          segmenter: typeof Intl.Segmenter === 'function'
        },
        // Intl output, string for string. Dates are all over these pages.
        intl: {
          gbLong: d.toLocaleDateString('en-GB', { day: 'numeric', month: 'long' }),
          gbFull: d.toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' }),
          gbShort: d.toLocaleDateString('en-GB'),
          time: d.toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' }),
          dtfResolved: Intl.DateTimeFormat('en-GB').resolvedOptions().timeZone,
          numGb: (1234.5).toLocaleString('en-GB'),
          isoParse: !isNaN(new Date('2026-09-06').getTime()),
          // The one that has actually broken Safari builds: a space-separated
          // timestamp, which Postgres/PostgREST emit and Safari rejects.
          pgParse: !isNaN(new Date('2026-09-12 05:00:18+00').getTime()),
          pgTParse: !isNaN(new Date('2026-09-12T05:00:18+00:00').getTime()),
          slashParse: !isNaN(new Date('2026/09/06').getTime())
        },
        inputs: (function () {
          var kinds = ['date', 'number', 'time', 'email', 'tel', 'password', 'search'];
          var res = {};
          kinds.forEach(function (k) {
            var i = document.createElement('input');
            i.type = k;
            res[k] = i.type === k;
          });
          return res;
        })(),
        /* Elements pinned to the bottom of the viewport. On iOS Safari the
           URL/toolbar sits over this band and `100vh` is taller than what is
           visible, so a bottom-fixed control is the one that gets covered. */
        fixedBottom: Array.from(document.querySelectorAll('body *')).filter(function (e) {
          var c = getComputedStyle(e);
          return (c.position === 'fixed' || c.position === 'sticky') && c.bottom !== 'auto';
        }).map(function (e) {
          var c = getComputedStyle(e), r = e.getBoundingClientRect();
          return { tag: e.tagName.toLowerCase(), id: e.id || null,
                   cls: String(e.className || '').slice(0, 30), position: c.position,
                   bottom: c.bottom, h: Math.round(r.height),
                   text: (e.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40) };
        }),
        // Every input this page's estate really uses, and its rendered size.
        realInputs: Array.from(document.querySelectorAll('input, textarea, select')).map(function (e) {
          var r = e.getBoundingClientRect(), cs = getComputedStyle(e);
          return { tag: e.tagName.toLowerCase(), type: e.type || null,
                   w: Math.round(r.width), h: Math.round(r.height), fontSize: cs.fontSize };
        })
      };
    });
    console.log('  seams           → pgParse=' + out.seams.intl.pgParse +
                ' dvh=' + out.seams.units.dvh + ' sticky=' + out.seams.css.sticky +
                ' pageSize=' + out.seams.css.pageSizeDescriptor);
    await page.close();
  }
  await ctx.close();

  // ── 1b. the report on a phone, and its print rules at a phone viewport ──
  {
    const pctx = await browser.newContext({ viewport: { width: 390, height: 844 } });
    await pctx.addInitScript(FLAG_ON_JS);
    const seedPage = await pctx.newPage();
    await seedPage.goto(BASE + '/404.html?env=test');
    await seedPage.evaluate(([k, v]) => { localStorage.clear(); localStorage.setItem(k, v); },
                            [SB_KEY, JSON.stringify(STATE.parent_session)]);
    await seedPage.close();

    const page = await pctx.newPage();
    const errs = [];
    page.on('pageerror', (e) => errs.push('PAGEERROR: ' + e.message));
    await page.goto(qs('/consumer/report.html?child=' + STATE.child + '&term=autumn-2026'),
                    { waitUntil: 'networkidle' });
    await page.waitForFunction(() => /Amara/.test(document.body.innerText), null, { timeout: 20000 }).catch(() => {});
    await page.waitForTimeout(800);
    const ov = await page.evaluate(overflowProbe);
    const sheet = await page.evaluate(() => {
      var s = document.querySelector('.rpt-sheet'); var cs = getComputedStyle(s);
      var r = s.getBoundingClientRect();
      return { w: Math.round(r.width), padding: cs.padding, fontSize: cs.fontSize,
               actionsVisible: getComputedStyle(document.querySelector('.rpt-actions')).display !== 'none' };
    });
    await page.screenshot({ path: path.join(SHOTS, '1b-report-390.png'), fullPage: true });

    // Print rules must beat the ≤820px screen breakpoint — both apply at 390.
    await page.emulateMedia({ media: 'print' });
    await page.waitForTimeout(400);
    const printAt390 = await page.evaluate(() => {
      var s = document.querySelector('.rpt-sheet'); var cs = getComputedStyle(s);
      return { width: cs.width, padding: cs.padding, boxShadow: cs.boxShadow,
               rootPadding: getComputedStyle(document.querySelector('.rpt-root')).padding,
               actionsHidden: getComputedStyle(document.querySelector('.rpt-actions')).display === 'none' };
    });
    await page.emulateMedia({ media: 'screen' });
    out.report_mobile = { overflow: ov, sheet, printAt390, errors: errs };
    console.log('  1b report 390   → overflowX=' + ov.overflowX + ' sheet.w=' + sheet.w +
                ' printPad=' + printAt390.padding + ' actionsHidden=' + printAt390.actionsHidden);
    await page.close();
    await pctx.close();
  }

  await browser.close();
  fs.writeFileSync(path.join(SCRATCH, 'safari_probe_' + ENGINE + '.json'), JSON.stringify(out, null, 1));
  console.log('  → safari_probe_' + ENGINE + '.json');
}
main().catch((e) => { console.error('FATAL', e); process.exit(1); });
