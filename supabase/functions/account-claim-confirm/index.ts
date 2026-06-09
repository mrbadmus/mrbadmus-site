// =====================================================================
// Edge Function: account-claim-confirm   (verify_jwt = false)
// Stage 3 — account reconciliation, Branch B.
//
// Reached when the student clicks the verification link in their OLD email
// (student/claim-confirm.html?token=...). No session is required — the
// single-use token IS the proof of control. We hash the plaintext token and
// hand it to confirm_account_claim_and_reparent(), which idempotently
// reparents the old profile onto the canonical account, soft-deletes the
// old profile, consumes the claim, and writes an audit_log entry.
// =====================================================================

import { createClient } from "jsr:@supabase/supabase-js@2";

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const json = (status: number, body: unknown) =>
  new Response(JSON.stringify(body), { status, headers: { ...CORS, "Content-Type": "application/json" } });

async function sha256Hex(input: string): Promise<string> {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(input));
  return Array.from(new Uint8Array(buf)).map((b) => b.toString(16).padStart(2, "0")).join("");
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  if (req.method !== "POST") return json(405, { ok: false, error: "method_not_allowed" });

  const SUPABASE_URL = Deno.env.get("SUPABASE_URL")!;
  const SERVICE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
  const admin = createClient(SUPABASE_URL, SERVICE_KEY, { auth: { autoRefreshToken: false, persistSession: false } });

  let body: { token?: string };
  try {
    body = await req.json();
  } catch {
    return json(400, { ok: false, error: "invalid_json" });
  }
  const token = (body.token || "").trim();
  if (!token || token.length < 32) return json(400, { ok: false, error: "invalid_token" });

  const tokenHash = await sha256Hex(token);
  const { data: result, error } = await admin.rpc("confirm_account_claim_and_reparent", {
    p_token_hash: tokenHash,
  });
  if (error) return json(500, { ok: false, error: "confirm_failed" });

  // result already shaped as { ok, reason?, counts?, already_consumed? }
  return json(200, result);
});
