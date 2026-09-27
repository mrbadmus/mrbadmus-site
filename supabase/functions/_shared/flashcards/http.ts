// MRB-351 — what both flashcard edge functions share: CORS, JSON replies,
// the caller's identity (never trusted from the body), the service client,
// and the usage log.

import { createClient, type SupabaseClient } from "jsr:@supabase/supabase-js@2";
import type { Usage } from "./model.ts";

export const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

export const json = (status: number, body: unknown) =>
  new Response(JSON.stringify(body), { status, headers: { ...CORS, "Content-Type": "application/json" } });

export function serviceClient(): SupabaseClient {
  return createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!, {
    auth: { persistSession: false },
  });
}

export type Caller = { id: string; role: string; school_id: string | null };

// The caller is whoever the bearer token says, looked up with the service
// client; the request body never names them.
export async function caller(req: Request, svc: SupabaseClient): Promise<Caller | null> {
  const token = (req.headers.get("Authorization") ?? "").replace(/^Bearer\s+/i, "");
  if (!token) return null;
  const { data, error } = await svc.auth.getUser(token);
  if (error || !data?.user) return null;
  const { data: p } = await svc.from("profiles").select("id, role, school_id").eq("id", data.user.id).maybeSingle();
  if (!p) return null;
  return { id: p.id, role: p.role ?? "student", school_id: p.school_id };
}

// The same answer `auth_user_has_scope('school_admin')` gives, read with the
// service client (which has no auth.uid() of its own): an active staff scope,
// or the M1 dual-read fallback on profiles.role.
export async function isSchoolAdmin(svc: SupabaseClient, who: Caller): Promise<boolean> {
  if (who.role === "admin") return true;
  const now = new Date().toISOString();
  const { data } = await svc.from("staff_scopes").select("profile_id")
    .eq("profile_id", who.id).eq("scope", "school_admin").is("deleted_at", null)
    .lte("started_at", now).or(`ended_at.is.null,ended_at.gt.${now}`).limit(1);
  return !!data?.length;
}

// Sonnet 5 $2/$10 and Haiku 4.5 $1/$5 per million tokens, at 0.80 GBP/USD.
// A cost ESTIMATE for the usage log, never a bill.
const PRICE: Record<string, [number, number]> = {
  "claude-sonnet-5": [2, 10],
  "claude-haiku-4-5": [1, 5],
};
export function costPence(u: Usage): number {
  const [i, o] = PRICE[u.model] ?? [0, 0];
  return Math.round(((u.input_tokens * i + u.output_tokens * o) / 1e6) * 0.8 * 100 * 10000) / 10000;
}

export async function logUsage(svc: SupabaseClient, kind: "flashcard_extract" | "flashcard_answer_check",
                               profileId: string, schoolId: string | null, u: Usage,
                               ref: { deck_id?: string; assignment_id?: string }) {
  await svc.from("ai_usage_events").insert({
    profile_id: profileId, org_id: schoolId, kind, model: u.model,
    input_tokens: u.input_tokens, output_tokens: u.output_tokens, cost_pence: costPence(u),
    deck_id: ref.deck_id ?? null, assignment_id: ref.assignment_id ?? null,
  });
}

export function background(p: Promise<unknown>) {
  // deno-lint-ignore no-explicit-any
  const rt = (globalThis as any).EdgeRuntime;
  if (rt?.waitUntil) rt.waitUntil(p); else p.catch(() => {});
}

export async function sha256Hex(bytes: Uint8Array): Promise<string> {
  const d = await crypto.subtle.digest("SHA-256", new Uint8Array(bytes));
  return [...new Uint8Array(d)].map((b) => b.toString(16).padStart(2, "0")).join("");
}
