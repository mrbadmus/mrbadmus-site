// =====================================================================
// Edge Function: flashcard-extract  (MRB-351 §2)
//
// Any file in, a DRAFT deck out. The teacher's page POSTs one of:
//   · multipart/form-data  file=<the file> [deck_id] [title] [force=1]
//   · JSON {paste: "<text>", title}                       (the paste box)
//   · JSON {deck_id, rerun: true}                         (Try extraction again)
//   · JSON {file_name, file_b64, …}                       (tests; same as multipart)
//
// It answers at once with {deck_id, job_id} — or with {cached: …} when a
// deck this teacher can see already came from the same file (sha256), so the
// page can offer "use the cards extracted before" instead of paying again —
// and does the work in the background, writing progress to
// `flashcard_extractions`, which the page polls under RLS.
//
// WHERE THIS LIVES, AND WHY NOT ON RENDER. MRB-351 §0 says extraction goes
// where the existing API calls live unless there is a concrete reason not
// to. There is one: the Render backend's repo is not part of this build, and
// TEST has no deployed backend at all (TEST's BACKEND_URL is localhost), so a
// Render route could not have been proved on TEST. This repo already owns
// edge functions (roster-import), and an edge function holds the service
// role, writes the private bucket directly, and is deployed per project.
//
// PUPIL DATA. A teacher's file is revision material; the prompt tells the
// model to ignore and never repeat any name in it (class lists on a title
// slide are common). Nothing about any pupil is ever sent.
//
// Needs the ANTHROPIC_API_KEY secret for every shape except clean tables and
// Q:/A: lines, which are paired here without a model at all.
// =====================================================================

import { background, caller, json, CORS, isSchoolAdmin, logUsage, serviceClient, sha256Hex } from "../_shared/flashcards/http.ts";
import { extOf, MAX_BYTES, ReadError } from "../_shared/flashcards/read_file.ts";
import { extract, pasteBytes } from "../_shared/flashcards/pipeline.ts";
import type { SupabaseClient } from "jsr:@supabase/supabase-js@2";

const MIME: Record<string, string> = {
  pptx: "application/vnd.openxmlformats-officedocument.presentationml.presentation",
  docx: "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
  xlsx: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
  pdf: "application/pdf", csv: "text/csv", txt: "text/plain", md: "text/markdown",
  png: "image/png", jpg: "image/jpeg", jpeg: "image/jpeg", webp: "image/webp", heic: "image/heic",
};

function titleFrom(name: string): string {
  const t = name.replace(/\.[a-z0-9]+$/i, "").replace(/[_-]+/g, " ").replace(/\s+/g, " ").trim();
  return (t || "Flashcards").slice(0, 120);
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  if (req.method !== "POST") return json(405, { error: "method_not_allowed" });

  const svc = serviceClient();
  const who = await caller(req, svc);
  if (!who) return json(401, { error: "not_signed_in" });
  if (who.role === "student" || !who.school_id) return json(403, { error: "not_staff" });

  // ── what came in ────────────────────────────────────────────────────
  let fileName = "", bytes: Uint8Array | null = null, deckId: string | null = null;
  let title = "", force = false, sourceKind: "upload" | "paste" = "upload";
  const ctype = req.headers.get("content-type") ?? "";
  try {
    if (ctype.startsWith("multipart/form-data")) {
      const form = await req.formData();
      const f = form.get("file");
      if (!(f instanceof File)) return json(400, { error: "no_file" });
      if (f.size > MAX_BYTES) return json(413, { error: "too_big" });
      fileName = f.name; bytes = new Uint8Array(await f.arrayBuffer());
      deckId = (form.get("deck_id") as string) || null;
      title = (form.get("title") as string) || "";
      force = form.get("force") === "1";
    } else {
      const body = await req.json();
      deckId = body.deck_id ?? null;
      title = body.title ?? "";
      force = !!body.force;
      if (typeof body.paste === "string") {
        if (!body.paste.trim()) return json(400, { error: "empty_paste" });
        if (body.paste.length > 200000) return json(413, { error: "too_big" });
        fileName = "pasted.txt"; bytes = pasteBytes(body.paste); sourceKind = "paste";
      } else if (typeof body.file_b64 === "string") {
        fileName = String(body.file_name ?? "file"); bytes = Uint8Array.from(atob(body.file_b64), (c) => c.charCodeAt(0));
        if (bytes.byteLength > MAX_BYTES) return json(413, { error: "too_big" });
      } else if (!body.rerun || !deckId) {
        return json(400, { error: "nothing_to_read" });
      }
    }
  } catch {
    return json(400, { error: "bad_request" });
  }

  // ── an existing deck: only its author (or the school admin) may re-run ──
  let deck: { id: string; school_id: string; created_by: string; source_file_path: string | null;
              source_file_name: string | null; title: string } | null = null;
  if (deckId) {
    const { data } = await svc.from("flashcard_decks")
      .select("id, school_id, created_by, source_file_path, source_file_name, title, deleted_at")
      .eq("id", deckId).maybeSingle();
    if (!data || data.deleted_at || data.school_id !== who.school_id) return json(404, { error: "deck_not_found" });
    if (data.created_by !== who.id && !(await isSchoolAdmin(svc, who))) return json(403, { error: "not_your_deck" });
    deck = data;
  }
  if (!bytes && deck) {
    if (!deck.source_file_path) return json(400, { error: "no_stored_file" });
    const dl = await svc.storage.from("teacher-uploads").download(deck.source_file_path);
    if (dl.error || !dl.data) return json(404, { error: "stored_file_missing" });
    bytes = new Uint8Array(await dl.data.arrayBuffer());
    fileName = deck.source_file_name ?? deck.source_file_path.split("/").pop()!;
  }
  if (!bytes) return json(400, { error: "nothing_to_read" });
  const ext = extOf(fileName);
  if (!MIME[ext]) return json(415, { error: "unsupported_type" });

  const sha = await sha256Hex(bytes);

  // ── the cache: the same file, already extracted, in a deck this teacher
  //    can see (their own, or one shared with the school) ──────────────
  if (!force && !deck && sourceKind === "upload") {
    const { data: prior } = await svc.from("flashcard_decks")
      .select("id, title, card_count, created_by, shared_with_school, status")
      .eq("school_id", who.school_id).eq("source_file_sha256", sha).is("deleted_at", null)
      .order("updated_at", { ascending: false }).limit(5);
    const hit = (prior ?? []).find((d) => d.card_count > 0 && (d.created_by === who.id || d.shared_with_school));
    if (hit) return json(200, { cached: { deck_id: hit.id, title: hit.title, card_count: hit.card_count, mine: hit.created_by === who.id } });
  }

  // ── the draft deck and the job row ──────────────────────────────────
  if (!deck) {
    const ins = await svc.from("flashcard_decks").insert({
      school_id: who.school_id, created_by: who.id, title: (title || titleFrom(fileName)).slice(0, 120),
      source_kind: sourceKind, status: "draft",
      source_file_name: sourceKind === "upload" ? fileName.slice(0, 200) : null,
    }).select("id, school_id, created_by, source_file_path, source_file_name, title").single();
    if (ins.error) return json(500, { error: "deck_create_failed" });
    deck = ins.data;
  }
  const path = sourceKind === "upload"
    ? `school/${who.school_id}/flashcards/${deck!.id}/${sha}.${ext}` : null;
  if (path && path !== deck!.source_file_path) {
    const up = await svc.storage.from("teacher-uploads").upload(path, bytes, { contentType: MIME[ext], upsert: true });
    if (up.error) return json(500, { error: "store_failed" });
    await svc.from("flashcard_decks").update({ source_file_path: path, source_file_sha256: sha,
      source_file_name: fileName.slice(0, 200) }).eq("id", deck!.id);
  }
  const job = await svc.from("flashcard_extractions").insert({
    deck_id: deck!.id, school_id: who.school_id, created_by: who.id, status: "reading", progress: 10, file_sha256: sha,
  }).select("id").single();
  if (job.error) return json(500, { error: "job_create_failed" });

  background(run(svc, who.id, who.school_id, deck!.id, job.data.id, fileName, bytes));
  return json(202, { deck_id: deck!.id, job_id: job.data.id });
});

async function run(svc: SupabaseClient, uid: string, school: string, deckId: string, jobId: string,
                   fileName: string, bytes: Uint8Array) {
  const step = (patch: Record<string, unknown>) => svc.from("flashcard_extractions").update(patch).eq("id", jobId);
  try {
    await step({ status: "asking", progress: 35 });
    const res = await extract(fileName, bytes, { apiKey: Deno.env.get("ANTHROPIC_API_KEY") ?? undefined });
    // Replace the draft's cards with what came back, in order.
    await svc.from("flashcard_cards").delete().eq("deck_id", deckId);
    if (res.rows.length) {
      const ins = await svc.from("flashcard_cards").insert(res.rows.map((r, i) => ({
        deck_id: deckId, position: i, question: r.question, answer: r.answer,
        source_ref: r.source_ref, confidence: r.confidence, flagged: r.flagged,
      })));
      if (ins.error) throw new Error("cards_write_failed");
    }
    await svc.from("flashcard_decks").update({ status: "draft" }).eq("id", deckId);
    if (res.usage) await logUsage(svc, "flashcard_extract", uid, school, res.usage, { deck_id: deckId });
    await step({
      status: "done", progress: 100, method: res.method,
      pairs_found: res.rows.filter((r) => r.question && r.answer).length,
      needs_answer: res.rows.filter((r) => !r.answer || !r.question).length,
      model: res.usage?.model ?? null, input_tokens: res.usage?.input_tokens ?? null,
      output_tokens: res.usage?.output_tokens ?? null,
    });
  } catch (e) {
    const code = e instanceof ReadError ? e.code : (e as Error)?.message?.slice(0, 60) || "failed";
    await step({ status: "failed", progress: 100, error: code });
  }
}
