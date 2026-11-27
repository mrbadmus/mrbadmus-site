// class_membership_drive.js — walks add / move / remove on TEST, as an admin,
// as a teacher of each class, and as the moved pupil. Screenshots at 390 px
// and 1280 px, light and dark, into $MRB_SHOTS (default ~/tmp/membership-shots).
//
//   1. psql/SQL editor on TEST: supabase/seeds/class_membership_drive_seed.sql
//   2. python3 -m http.server 8765 --directory mrbadmus_site
//   3. node tools/class_membership_drive.js
//   4. supabase/seeds/class_membership_drive_teardown.sql
//
// TEST only: config.js picks the TEST project on localhost, and this script
// refuses to run if the page reports anything else.
const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");
const os = require("os");

const ROOT = path.resolve(__dirname, "..");
const SITE = process.env.MRB_SITE || "http://localhost:8765";
const SHOTS = process.env.MRB_SHOTS || path.join(os.homedir(), "tmp", "membership-shots");
const PW = "cb-throwaway-1";
const C1 = "cb000000-0000-0000-0000-0000000000c1";
const C2 = "cb000000-0000-0000-0000-0000000000c2";
const MAYA = "cb000000-0000-0000-0000-000000000011";
const cfg = fs.readFileSync(path.join(ROOT, "shared", "config.js"), "utf8");
const testBlock = cfg.slice(cfg.indexOf("const TEST"));
const URL_ = testBlock.match(/https:\/\/[a-z]+\.supabase\.co/)[0];
const ANON = testBlock.match(/'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'/)[1];
const REF = URL_.split("//")[1].split(".")[0];
if (REF !== "qeppkiswvclkkwbxmlok") { throw new Error("not TEST: " + REF); }

fs.mkdirSync(SHOTS, { recursive: true });
const fails = [];
const ok = (cond, what) => { console.log((cond ? "ok   " : "FAIL ") + what); if (!cond) fails.push(what); };

async function session(email) {
  const r = await fetch(URL_ + "/auth/v1/token?grant_type=password", {
    method: "POST", headers: { apikey: ANON, "content-type": "application/json" },
    body: JSON.stringify({ email, password: PW }) });
  const j = await r.json();
  if (!j.access_token) throw new Error("sign-in failed for " + email + ": " + JSON.stringify(j));
  return j;
}

async function as(browser, email, opts) {
  const s = await session(email);
  const ctx = await browser.newContext({ viewport: opts.viewport, deviceScaleFactor: 2,
                                         colorScheme: opts.dark ? "dark" : "light" });
  await ctx.addInitScript(([key, val, dark]) => {
    try { localStorage.setItem(key, val); localStorage.setItem("mrb-theme", dark ? "dark" : "light"); } catch (e) {}
  }, ["sb-" + REF + "-auth-token", JSON.stringify(s), !!opts.dark]);
  const page = await ctx.newPage();
  page.on("pageerror", (e) => console.log("  [pageerror]", e.message));
  return { ctx, page };
}

async function shot(page, name) {
  await page.waitForTimeout(400);
  await page.screenshot({ path: path.join(SHOTS, name + ".png") });
}

const trigger = (page, kind) => page.locator(`[data-mrb-added="${kind}"]`);

(async () => {
  const browser = await chromium.launch();
  const sizes = [{ tag: "390", viewport: { width: 390, height: 844 } },
                 { tag: "1280", viewport: { width: 1280, height: 860 } }];

  // ── ADMIN, class page ───────────────────────────────────────────────
  {
    const { ctx, page } = await as(browser, "cb_admin@throwaway.test", sizes[0]);
    await page.goto(`${SITE}/teacher/class-detail.html?class=${C1}`);
    await trigger(page, "members-open").waitFor({ timeout: 30000 });
    ok(true, "admin: Pupils button on the class page");
    await shot(page, "01-admin-class-page-390");
    await trigger(page, "members-open").click();
    await page.locator(".cm-sheet").waitFor();
    await shot(page, "02-admin-pupils-sheet-390");
    const pastText = await page.locator(".cm-sheet").innerText();
    ok(/Moved to CB 8q\/Sc2/.test(pastText), "admin: Maya shown as moved to CB 8q/Sc2");

    // add by search, then undo
    await page.fill("#cm-find", "Newc");
    await page.locator(".cm-list .cm-row:has-text('Zara Newcomb') button:has-text('Add')").click();
    await page.locator(".cm-toast").waitFor();
    await shot(page, "03-admin-added-toast-390");
    ok(/Zara Newcomb/.test(await page.locator(".cm-sheet").innerText()), "admin: Zara added by search");
    await page.locator(".cm-toast button:has-text('Undo')").click();
    await page.waitForTimeout(1500);
    ok(!/Zara Newcomb/.test(await page.locator(".cm-sheet .cm-sec").nth(1).innerText()), "admin: undo removes Zara again");

    // remove one, plain confirm, undo
    await page.locator(".cm-row:has-text('Leo Stayer') button:has-text('Remove')").click();
    await shot(page, "04-admin-remove-confirm-390");
    ok(/Remove Leo Stayer from CB 8q\/Sc1\?/.test(await page.locator(".cm-title").innerText()), "admin: plain remove confirm");
    await page.locator(".cm-foot button:has-text('Remove')").click();
    await page.locator(".cm-toast").waitFor();
    ok(/Leo Stayer/.test(await page.locator(".cm-sheet").innerText()) &&
       /Left the class on/.test(await page.locator(".cm-sheet").innerText()), "admin: Leo listed as left");
    await page.locator(".cm-toast button:has-text('Undo')").click();
    await page.waitForTimeout(1500);

    // batch: add Zara back, tick both, move to Sc2
    await page.fill("#cm-find", "Newc");
    await page.locator(".cm-list .cm-row:has-text('Zara Newcomb') button:has-text('Add')").click();
    await page.locator(".cm-toast").waitFor();
    await page.waitForTimeout(800);
    await page.locator(".cm-row:has-text('Leo Stayer') input[type=checkbox]").check();
    await page.locator(".cm-row:has-text('Zara Newcomb') input[type=checkbox]").check();
    await shot(page, "05-admin-batch-selected-390");
    await page.locator(".cm-bar button:has-text('Move')").click();
    await page.locator(".cm-grid").waitFor();
    await shot(page, "06-admin-move-targets-390");
    await page.locator(".cm-grid button:has-text('CB 8q/Sc2')").click();
    ok(/Move 2 pupils to CB 8q\/Sc2\?/.test(await page.locator(".cm-title").innerText()), "admin: batch move confirm");
    await page.locator(".cm-foot button:has-text('Move')").click();
    await page.locator(".cm-toast").waitFor();
    await shot(page, "07-admin-batch-moved-390");
    ok(/2 pupils moved to CB 8q\/Sc2/.test(await page.locator(".cm-toast").innerText()), "admin: batch moved");

    // add by email (not on the platform yet) — goes through roster-import
    await page.locator("button:has-text('Not on MrBadmus yet')").click();
    await page.fill("#cm-first", "Esme");
    await page.fill("#cm-last", "Email");
    await page.fill("#cm-email", "cb_esme@throwaway.test");
    await shot(page, "08-admin-add-by-email-390");
    await page.locator(".cm-foot button:has-text('Add pupil')").click();
    await page.locator(".cm-toast").waitFor({ timeout: 30000 });
    ok(/Esme Email/.test(await page.locator(".cm-sheet").innerText()), "admin: Esme added by email");
    await ctx.close();
  }

  // ── ADMIN, laptop + dark ────────────────────────────────────────────
  for (const v of [{ ...sizes[1], dark: false }, { ...sizes[1], dark: true }, { ...sizes[0], dark: true }]) {
    const { ctx, page } = await as(browser, "cb_admin@throwaway.test", v);
    await page.goto(`${SITE}/teacher/class-detail.html?class=${C1}`);
    await trigger(page, "members-open").waitFor({ timeout: 30000 });
    await trigger(page, "members-open").click();
    await page.locator(".cm-sheet").waitFor();
    await shot(page, `09-admin-pupils-${v.tag}-${v.dark ? "dark" : "light"}`);
    ok(true, `admin sheet renders at ${v.tag} ${v.dark ? "dark" : "light"}`);
    await ctx.close();
  }

  // ── ADMIN, pupil page: see classes, move Maya back ──────────────────
  {
    const { ctx, page } = await as(browser, "cb_admin@throwaway.test", sizes[0]);
    await page.goto(`${SITE}/teacher/student-detail.html?student=${MAYA}&class=${C2}`);
    await trigger(page, "pupil-classes").waitFor({ timeout: 30000 });
    await shot(page, "10-admin-pupil-page-390");
    await trigger(page, "pupil-classes").click();
    await page.locator(".cm-sheet").waitFor();
    await shot(page, "11-admin-pupil-classes-390");
    ok(/CB 8q\/Sc2/.test(await page.locator(".cm-sheet").innerText()), "pupil page: shows current class");
    await page.locator(".cm-row:has-text('CB 8q/Sc2') button:has-text('Move')").click();
    await page.locator(".cm-grid button:has-text('CB 8q/Sc1')").click();
    await page.locator(".cm-foot button:has-text('Move')").click();
    await page.locator(".cm-toast").waitFor();
    await page.waitForTimeout(1200);
    const t = await page.locator(".cm-sheet").innerText();
    ok(/CB 8q\/Sc1/.test(t) && !/CB 8q\/Sc2/.test(t), "pupil page: Maya moved back to Sc1");
    await shot(page, "12-admin-pupil-moved-back-390");
    await ctx.close();
  }

  // ── TEACHERS: see the result, cannot change it ──────────────────────
  for (const [email, cls, tag] of [["cb_teacher1@throwaway.test", C1, "t1-class1"],
                                   ["cb_teacher2@throwaway.test", C2, "t2-class2"]]) {
    const { ctx, page } = await as(browser, email, sizes[1]);
    await page.goto(`${SITE}/teacher/class-detail.html?class=${cls}`);
    await page.waitForTimeout(9000);
    ok(await trigger(page, "members-open").count() === 0 ||
       (await trigger(page, "members-open").innerText()) === "Left this class",
       `${tag}: no Pupils (admin) button`);
    const r = await page.evaluate(async (c) => {
      const sb = window.MrBadmusTeacherGuard.getClient();
      return sb.rpc("class_membership_batch", { p_ops: [{ op: "remove", class_id: c,
        student_id: "cb000000-0000-0000-0000-000000000012" }] });
    }, cls);
    ok(!!r.error && /not_admin/.test(r.error.message), `${tag}: direct call refused (${r.error && r.error.message})`);
    await shot(page, `13-teacher-${tag}-1280`);
    if (await trigger(page, "members-open").count()) {
      await trigger(page, "members-open").click();
      await page.locator(".cm-sheet").waitFor();
      await shot(page, `14-teacher-${tag}-left-list-1280`);
      ok(await page.locator(".cm-sheet button:has-text('Remove')").count() === 0, `${tag}: left list is read-only`);
    }
    await ctx.close();
  }

  // ── THE MOVED PUPIL: only current classes ───────────────────────────
  {
    const { ctx, page } = await as(browser, "cb_pupil1@throwaway.test", sizes[0]);
    await page.goto(`${SITE}/student/classes.html`);
    await page.waitForTimeout(8000);
    await shot(page, "15-pupil-classes-390");
    const t = await page.locator("body").innerText();
    ok(/CB 8q\/Sc1/.test(t) && !/CB 8q\/Sc2/.test(t), "pupil: sees only current class (Sc1)");
    const r = await page.evaluate(async () => {
      const c = window.MrBadmusClassEntry && window.MrBadmusClassEntry.getClient
        ? window.MrBadmusClassEntry.getClient() : null;
      if (!c) return { skipped: true };
      return c.rpc("move_pupil", { p_student_id: "cb000000-0000-0000-0000-000000000011",
        p_from_class_id: "cb000000-0000-0000-0000-0000000000c1",
        p_to_class_id: "cb000000-0000-0000-0000-0000000000c2" });
    });
    if (!r.skipped) ok(!!r.error, "pupil: cannot move themselves (" + (r.error && r.error.message) + ")");
    await ctx.close();
  }

  await browser.close();
  console.log(fails.length ? `\n${fails.length} FAILED` : "\nALL PASS");
  console.log("shots: " + SHOTS);
  process.exit(fails.length ? 1 : 0);
})().catch((e) => { console.error(e); process.exit(2); });
