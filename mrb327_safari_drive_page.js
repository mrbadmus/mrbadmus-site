/* mrb327_safari_drive_page.js — MRB-327 §2, the two things the first two
 * passes could only half-answer.
 *
 * 1. Does the engine's CSS parser actually ACCEPT `@page { size: A4; margin: 0 }`?
 *    `CSS.supports('size','A4')` is not the test — `size` is a @page DESCRIPTOR,
 *    not a property, so CSS.supports is entitled to say no either way. This
 *    reads the parsed CSSOM instead: if the engine kept the rule and kept the
 *    descriptors, it understood them.
 * 2. today.html's chat composer is `position:fixed; bottom:0`. On a phone that
 *    is the band iOS Safari's toolbar sits over. Open it and measure it.
 */
const fs = require('fs'), path = require('path'), playwright = require('playwright');
const SCRATCH = '/private/tmp/claude-501/-Users-midebadmus-Documents-GitHub-mrbadmus-worktrees-b2c-launch/06d799b1-12f9-481b-9871-424a2321715f/scratchpad';
const STATE = JSON.parse(fs.readFileSync(path.join(SCRATCH, 'safari_fixtures.json'), 'utf8'));
const BASE = 'http://localhost:8171', API = 'http://localhost:3100';
const ENGINE = process.argv[process.argv.indexOf('--engine') + 1] || 'webkit';
const SHOTS = path.join(SCRATCH, 'shots', 'safari', ENGINE);
fs.mkdirSync(SHOTS, { recursive: true });
const FLAG_ON_JS = `(function(){var c=null;Object.defineProperty(window,'MrBadmusConfig',{configurable:true,
  get:function(){return c;}, set:function(v){ if(v&&typeof v==='object'){v.CONSUMER_SIGNUP_ENABLED=true;} c=v; }});})();`;
const qs = (p) => BASE + p + (p.includes('?') ? '&' : '?') + 'env=test&api=' + API;

(async () => {
  const browser = await playwright[ENGINE].launch();
  const out = { engine: ENGINE, version: browser.version() };
  console.log('\n══ page/composer ' + ENGINE + ' ' + browser.version() + ' ══');
  const ctx = await browser.newContext({ viewport: { width: 390, height: 844 } });
  await ctx.addInitScript(FLAG_ON_JS);

  // ── 1. @page, read out of the parsed CSSOM ───────────────────────────────
  {
    const page = await ctx.newPage();
    await page.goto(BASE + '/404.html?env=test');
    out.atPage = await page.evaluate(() => {
      var st = document.createElement('style');
      st.textContent = '@page { size: A4; margin: 0; } @page :first { margin-top: 0; } .x { color: red; }';
      document.head.appendChild(st);
      var sheet = st.sheet;
      var rules = Array.from(sheet.cssRules).map(function (r) {
        return { type: r.constructor.name, text: r.cssText };
      });
      var pageRule = Array.from(sheet.cssRules).find(function (r) { return /^@page/.test(r.cssText); });
      var descriptors = null;
      if (pageRule && pageRule.style) {
        descriptors = {};
        for (var i = 0; i < pageRule.style.length; i++) {
          descriptors[pageRule.style[i]] = pageRule.style.getPropertyValue(pageRule.style[i]);
        }
        descriptors._size = pageRule.style.getPropertyValue('size');
        descriptors._margin = pageRule.style.getPropertyValue('margin');
      }
      return {
        ruleCount: sheet.cssRules.length, rules: rules,
        pageRuleKept: !!pageRule, descriptors: descriptors,
        cssSupportsSize: CSS.supports('size', 'A4'),
        cssSupportsPageMargin: CSS.supports('margin', '0')
      };
    });
    console.log('  @page kept=' + out.atPage.pageRuleKept +
                ' descriptors=' + JSON.stringify(out.atPage.descriptors));
    console.log('  rules: ' + out.atPage.rules.map((r) => r.text).join(' | '));
    await page.close();
  }

  // ── 2. the bottom-fixed chat composer on today.html ──────────────────────
  {
    const p = await ctx.newPage();
    await p.goto(qs('/go/index.html'), { waitUntil: 'networkidle' });
    await p.fill('#gl-user', STATE.child_username);
    await p.fill('#gl-pass', STATE.child_password);
    await p.click('#gl-go');
    await p.waitForURL(/consumer\/today\.html/, { timeout: 25000 });
    await p.waitForTimeout(2000);

    // Whatever opens the chat, found by its words rather than a guessed id.
    const openedBy = await p.evaluate(() => {
      var b = Array.from(document.querySelectorAll('button, [role="button"], a'))
        .find(function (e) { return /ask|chat|message|mr badmus/i.test((e.textContent || '').trim()); });
      if (!b) return null;
      b.click();
      return (b.textContent || '').trim().slice(0, 40);
    });
    await p.waitForTimeout(1500);
    const composer = await p.evaluate(() => {
      var el = document.querySelector('.td-composer');
      var inputs = Array.from(document.querySelectorAll('input, textarea')).map(function (e) {
        var r = e.getBoundingClientRect(), cs = getComputedStyle(e);
        return { tag: e.tagName.toLowerCase(), type: e.type || null,
                 w: Math.round(r.width), h: Math.round(r.height),
                 top: Math.round(r.top), bottom: Math.round(r.bottom),
                 fontSize: cs.fontSize,
                 /* < 16px is what makes iOS Safari zoom the whole page when
                    the field is focused. It is the one number on this element
                    that a desktop engine can still tell you the truth about. */
                 iosWouldZoom: parseFloat(cs.fontSize) < 16 };
      });
      if (!el) return { present: false, inputs: inputs };
      var r = el.getBoundingClientRect(), cs = getComputedStyle(el);
      return { present: true, position: cs.position, bottom: cs.bottom,
               x: Math.round(r.x), y: Math.round(r.y),
               w: Math.round(r.width), h: Math.round(r.height),
               viewportH: window.innerHeight,
               belowFold: r.bottom > window.innerHeight + 1,
               inputs: inputs };
    });
    await p.screenshot({ path: path.join(SHOTS, '2b-today-composer-390.png') });
    out.composer = { openedBy, ...composer };
    console.log('  composer openedBy=' + JSON.stringify(openedBy) + ' → ' + JSON.stringify(composer));
    await p.close();
  }

  await ctx.close(); await browser.close();
  fs.writeFileSync(path.join(SCRATCH, 'safari_page_' + ENGINE + '.json'), JSON.stringify(out, null, 1));
})().catch((e) => { console.error('FATAL', e); process.exit(1); });
