// =====================================================================
// Edge Function: account-claim-request   (verify_jwt = true)
// Stage 3 — account reconciliation, Branch B.
//
// The signed-in (canonical, school-SSO) student enters their OLD personal
// email. We mint a single-use, time-limited token, store only its SHA-256
// hash via create_account_claim(), and email the plaintext link to the OLD
// address (proof of control). Response is deliberately generic (anti-
// enumeration): it never reveals whether an account was found.
//
// Email is sent via Resend if RESEND_API_KEY is configured; otherwise the
// request still records the claim (best-effort email). No token is ever
// returned to the browser.
// =====================================================================

import { createClient } from "jsr:@supabase/supabase-js@2";

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const json = (status: number, body: unknown) =>
  new Response(JSON.stringify(body), { status, headers: { ...CORS, "Content-Type": "application/json" } });

const ALLOWED_BASES = ["https://mrbadmus.com", "https://www.mrbadmus.com", "http://localhost:3000", "http://127.0.0.1:3000"];
const TTL_MINUTES = 30;

async function sha256Hex(input: string): Promise<string> {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(input));
  return Array.from(new Uint8Array(buf)).map((b) => b.toString(16).padStart(2, "0")).join("");
}
function randomToken(): string {
  const b = new Uint8Array(32);
  crypto.getRandomValues(b);
  return Array.from(b).map((x) => x.toString(16).padStart(2, "0")).join("");
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  if (req.method !== "POST") return json(405, { ok: false, error: "method_not_allowed" });

  const SUPABASE_URL = Deno.env.get("SUPABASE_URL")!;
  const SERVICE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
  const admin = createClient(SUPABASE_URL, SERVICE_KEY, { auth: { autoRefreshToken: false, persistSession: false } });

  const jwt = (req.headers.get("Authorization") || "").replace(/^Bearer\s+/i, "");
  if (!jwt) return json(401, { ok: false, error: "missing_token" });
  const { data: userData, error: userErr } = await admin.auth.getUser(jwt);
  if (userErr || !userData?.user) return json(401, { ok: false, error: "unauthorized" });
  const claimantId = userData.user.id;
  const claimantEmail = (userData.user.email || "").toLowerCase();

  let body: { oldEmail?: string; confirmBaseUrl?: string; env?: string };
  try {
    body = await req.json();
  } catch {
    return json(400, { ok: false, error: "invalid_json" });
  }
  const oldEmail = (body.oldEmail || "").trim().toLowerCase();
  if (!oldEmail || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(oldEmail)) {
    return json(400, { ok: false, error: "invalid_email" });
  }
  // Guard: claiming your own current email is a no-op.
  if (oldEmail === claimantEmail) {
    return json(200, { ok: true }); // generic; nothing to do
  }

  const token = randomToken();
  const tokenHash = await sha256Hex(token);

  const { data: result, error: rpcErr } = await admin.rpc("create_account_claim", {
    p_claimant_id: claimantId,
    p_old_email: oldEmail,
    p_token_hash: tokenHash,
    p_ttl_minutes: TTL_MINUTES,
  });
  if (rpcErr) return json(500, { ok: false, error: "claim_create_failed" });

  const matched = (result as { matched?: boolean })?.matched === true;

  // Send the verification email only when a matching old account exists.
  // (Anti-enumeration: the HTTP response is identical either way.)
  if (matched) {
    const origin = req.headers.get("Origin") || "";
    let base = ALLOWED_BASES.includes(body.confirmBaseUrl || "")
      ? body.confirmBaseUrl!
      : ALLOWED_BASES.includes(origin)
        ? origin
        : Deno.env.get("CLAIM_SITE_URL") || "https://mrbadmus.com";
    const envQs = body.env === "test" ? "&env=test" : "";
    const link = `${base}/student/claim-confirm.html?token=${token}${envQs}`;

    const RESEND_API_KEY = Deno.env.get("RESEND_API_KEY");
    if (RESEND_API_KEY) {
      try {
        await fetch("https://api.resend.com/emails", {
          method: "POST",
          headers: { Authorization: `Bearer ${RESEND_API_KEY}`, "Content-Type": "application/json" },
          body: JSON.stringify({
            from: "MrBadmusAI <noreply@mrbadmus.com>",
            to: [oldEmail],
            subject: "Confirm you want to move your MrBadmusAI progress",
            html: `<div style="font-family:Arial,sans-serif;max-width:480px;margin:0 auto;color:#1a1a2e">
              <h2 style="color:#4ECDC4">Move your old MrBadmusAI account</h2>
              <p>Someone signed in with a school account and asked to move the progress
              from <strong>${oldEmail}</strong> onto it.</p>
              <p>If that was you, confirm within ${TTL_MINUTES} minutes:</p>
              <p><a href="${link}" style="display:inline-block;background:#4ECDC4;color:#0F0F1A;
              text-decoration:none;font-weight:700;padding:12px 22px;border-radius:10px">Yes, move my progress</a></p>
              <p style="color:#888;font-size:13px">If this wasn't you, ignore this email — nothing will change.
              This link can only be used once and expires in ${TTL_MINUTES} minutes.</p>
            </div>`,
          }),
        });
      } catch {
        // best-effort: the claim row exists; the email can be resent later
      }
    }
  }

  return json(200, { ok: true });
});
