// =====================================================================
// Edge Function: flashcard-answer-check  (MRB-351 §5)
//
// Checks what pupils WROTE (make mode) against the model answer and stores
// match | partial | no | blank on each `flashcard_pupil_cards` row. A flag
// for the teacher, never a grade the pupil sees.
//
// Called with {assignment_id, session_id?}:
//   · by the pupil's page when a sitting ends ("Finish for now", or the page
//     going away) — only that pupil's own pending answers are checked;
//   · by the teacher's progress page when it opens — every pending answer
//     of that assignment, so a pupil who closed the tab mid-sitting is
//     still checked.
// Either way the work is batched PER SITTING and runs in the background.
//
// ⚠️ NO PUPIL IDENTIFIERS REACH THE MODEL. Each request carries only
// {question, model_answer, pupil_answer}, numbered 0..n-1 inside the
// request; row ids, names, classes and sittings stay on this side and the
// verdicts are mapped back by position. Blank / one-word / "idk"-type
// answers were already decided in SQL (`flashcard_quick_check`) when they
// were written and never arrive here.
//
// Without the ANTHROPIC_API_KEY secret this does nothing and leaves the
// rows `pending`; the teacher's table counts them as pending.
//
// ⊕ SYNC MODE (MRB-351 pupil flow, docs/mrb351/PUPIL-FLOW.md §3.2) — called
// with {assignment_id, card_id, pupil_answer} by the pupil's page the moment
// they tap Check, for an answer the page's own check (a port of
// `flashcard_quick_check`) could not decide. Replies 200 {verdict} with one of
// match | partial | no | blank, or 200 {skipped:"no_key"} without the secret.
// The page waits four seconds and no longer. Pupils only, in their own class,
// after release. If the pupil's own `flashcard_pupil_cards` row for that card
// is still `pending` with the same text, the verdict is written onto it, so
// the end-of-sitting batch does not pay for the same answer twice. The same
// prompt builder, so no pupil identifier reaches the model. The batch mode
// above is untouched.
//
// ⊕ MRB-353 (1 Oct 2026) — THE VERDICT THE PUPIL SAW IS THE ONE STORED.
// The sync mode used to write its verdict onto `flashcard_pupil_cards` only,
// so a REVIEW answer's `flashcard_reviews` row stayed `pending` for ever and
// the teacher's panel said "Checking" on answers the pupil was marked on
// minutes before. Now every verdict, from either mode, goes through
// `flashcard_store_verdict(assignment, pupil, card, answer, verdict)`
// (migration 20261001190000_mrb353_flashcard_verdicts_finish.sql): it keeps
// the verdict against that EXACT answer text and copies it onto every still-
// pending review / make row with that text, and `flashcard_record` copies it
// onto a review row written later. A sync check for text this pupil already
// had checked on this card returns the stored verdict without the model.
// The batch mode now also claims and checks pending REVIEW answers, so
// nothing stays pending after a sitting. Before that migration is applied
// the RPC and the review read fail, and both modes fall back to exactly
// what they did before.
// =====================================================================

import { background, caller, CORS, isSchoolAdmin, json, logUsage, serviceClient } from "../_shared/flashcards/http.ts";
import { checkWithModel } from "../_shared/flashcards/model.ts";
import type { SupabaseClient } from "jsr:@supabase/supabase-js@2";

const BATCH = 40;

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  if (req.method !== "POST") return json(405, { error: "method_not_allowed" });
  const svc = serviceClient();
  const who = await caller(req, svc);
  if (!who) return json(401, { error: "not_signed_in" });

  let body: { assignment_id?: string; session_id?: string; card_id?: string; pupil_answer?: string };
  try { body = await req.json(); } catch { return json(400, { error: "bad_request" }); }
  if (!body.assignment_id) return json(400, { error: "no_assignment" });
  if (body.card_id !== undefined) return syncCheck(svc, who, body);

  // ⊕ Sharpen run (PUPIL-FLOW §13.6) — a deleted or not-yet-released set is
  // not checked, exactly as the sync mode refuses it below. The pupil's page
  // can still call this for a set deleted while it was open.
  const { data: a } = await svc.from("assignments")
    .select("id, class_id, school_id, set_by, kind, deleted_at, release_at")
    .eq("id", body.assignment_id).maybeSingle();
  if (!a || a.kind !== "flashcards" || a.deleted_at ||
      (a.release_at && new Date(a.release_at).getTime() > Date.now())) return json(404, { error: "not_found" });

  // Who may ask: the pupil (their own rows only) or a teacher of the class.
  let pupilOnly: string | null = null;
  if (who.role === "student") {
    pupilOnly = who.id;
  } else {
    const { data: t } = await svc.from("class_teachers").select("id").eq("class_id", a.class_id)
      .eq("teacher_id", who.id).is("ended_at", null).is("deleted_at", null).limit(1);
    const admin = who.school_id === a.school_id && await isSchoolAdmin(svc, who);
    if (!t?.length && !admin) return json(404, { error: "not_found" });
  }

  const key = Deno.env.get("ANTHROPIC_API_KEY");
  if (!key) return json(200, { skipped: "no_key" });

  background(run(svc, a, body.session_id ?? null, pupilOnly, key));
  return json(202, { queued: true });
});

type Item = { kind: "make" | "review"; id: string; session_id: string; pupil_id: string;
              card_id: string; answer: string };

// One verdict, stored where the teacher reads it. Falls back to the old
// make-row write when the MRB-353 migration is not there yet.
async function storeVerdict(svc: SupabaseClient, assignmentId: string, pupilId: string, cardId: string,
                            answer: string, verdict: string): Promise<boolean> {
  const { error } = await svc.rpc("flashcard_store_verdict", {
    p_assignment: assignmentId, p_pupil: pupilId, p_card: cardId, p_answer: answer, p_verdict: verdict,
  });
  if (!error) return true;
  await svc.from("flashcard_pupil_cards").update({ answer_check: verdict, checked_at: new Date().toISOString() })
    .eq("assignment_id", assignmentId).eq("pupil_id", pupilId).eq("card_id", cardId)
    .eq("answer_check", "pending").eq("pupil_answer", answer);
  return false;
}

// Verdicts already given for (pupil, card, exact text) on this assignment.
// Empty when the table is not there yet.
async function storedVerdicts(svc: SupabaseClient, assignmentId: string, pupilIds: string[]):
    Promise<Map<string, string>> {
  const out = new Map<string, string>();
  if (!pupilIds.length) return out;
  const { data, error } = await svc.from("flashcard_answer_verdicts").select("pupil_id, card_id, answer, verdict")
    .eq("assignment_id", assignmentId).in("pupil_id", pupilIds);
  if (error) return out;
  for (const v of data ?? []) out.set(vkey(v.pupil_id, v.card_id, v.answer), v.verdict);
  return out;
}
const vkey = (pupil: string, card: string, answer: string) => `${pupil}\u0000${card}\u0000${answer}`;

async function run(svc: SupabaseClient, a: { id: string; school_id: string; set_by: string | null },
                   sessionId: string | null, pupilOnly: string | null, key: string) {
  const stale = new Date(Date.now() - 5 * 60 * 1000).toISOString();
  const now = new Date().toISOString();
  const items: Item[] = [];

  // make-phase answers
  let q = svc.from("flashcard_pupil_cards").select("id, session_id, card_id, pupil_id, pupil_answer")
    .eq("assignment_id", a.id).eq("answer_check", "pending")
    .or(`check_claimed_at.is.null,check_claimed_at.lt.${stale}`).limit(200);
  if (sessionId) q = q.eq("session_id", sessionId);
  if (pupilOnly) q = q.eq("pupil_id", pupilOnly);
  const { data: rows } = await q;
  if (rows?.length) {
    // Claim them, so two callers never pay for the same answer twice.
    const { data: claimed } = await svc.from("flashcard_pupil_cards").update({ check_claimed_at: now })
      .in("id", rows.map((r) => r.id)).eq("answer_check", "pending")
      .select("id, session_id, card_id, pupil_id, pupil_answer");
    for (const r of claimed ?? []) {
      items.push({ kind: "make", id: r.id, session_id: r.session_id, pupil_id: r.pupil_id,
                   card_id: r.card_id, answer: r.pupil_answer });
    }
  }

  // ⊕ MRB-353: review-phase answers, claimed the same way. Before the
  // migration the column is missing and this read errors — skipped.
  let rq = svc.from("flashcard_reviews").select("id, session_id, card_id, pupil_id, answer")
    .eq("assignment_id", a.id).eq("answer_check", "pending").not("answer", "is", null)
    .or(`check_claimed_at.is.null,check_claimed_at.lt.${stale}`).limit(200);
  if (sessionId) rq = rq.eq("session_id", sessionId);
  if (pupilOnly) rq = rq.eq("pupil_id", pupilOnly);
  const { data: revRows, error: revErr } = await rq;
  if (!revErr && revRows?.length) {
    const { data: claimed } = await svc.from("flashcard_reviews").update({ check_claimed_at: now })
      .in("id", revRows.map((r) => r.id)).eq("answer_check", "pending")
      .select("id, session_id, card_id, pupil_id, answer");
    for (const r of claimed ?? []) {
      items.push({ kind: "review", id: r.id, session_id: r.session_id, pupil_id: r.pupil_id,
                   card_id: r.card_id, answer: r.answer });
    }
  }
  if (!items.length) return;

  // A verdict already given for the same text (the pupil saw it) is reused,
  // never re-asked: the stored verdict must be the one the pupil saw.
  const known = await storedVerdicts(svc, a.id, [...new Set(items.map((r) => r.pupil_id))]);
  const ask = new Map<string, Item>();          // one model item per distinct (pupil, card, text)
  for (const it of items) {
    const k = vkey(it.pupil_id, it.card_id, it.answer);
    const v = known.get(k);
    if (v) await storeVerdict(svc, a.id, it.pupil_id, it.card_id, it.answer, v);
    else if (!ask.has(k)) ask.set(k, it);
  }
  if (!ask.size) return;

  const { data: snap } = await svc.from("assignment_flashcards").select("id, question, answer")
    .in("id", [...new Set([...ask.values()].map((r) => r.card_id))]);
  const card = new Map((snap ?? []).map((c) => [c.id, c]));

  // Per sitting, in batches.
  const bySession = new Map<string, Item[]>();
  for (const r of ask.values()) bySession.set(r.session_id, [...(bySession.get(r.session_id) ?? []), r]);
  for (const group of bySession.values()) {
    for (let i = 0; i < group.length; i += BATCH) {
      const part = group.slice(i, i + BATCH).filter((r) => card.has(r.card_id));
      if (!part.length) continue;
      try {
        const { verdicts, usage } = await checkWithModel(part.map((r) => ({
          question: card.get(r.card_id)!.question,
          model_answer: card.get(r.card_id)!.answer,
          pupil_answer: r.answer,
        })), key);
        for (let k = 0; k < part.length; k++) {
          if (!verdicts[k]) continue;
          await storeVerdict(svc, a.id, part[k].pupil_id, part[k].card_id, part[k].answer, verdicts[k]!);
        }
        if (a.set_by) await logUsage(svc, "flashcard_answer_check", a.set_by, a.school_id, usage, { assignment_id: a.id });
      } catch {
        // Left claimed; the claim goes stale after five minutes and the next
        // caller picks the rows up again.
      }
    }
  }
}

// ── sync mode: one answer, now ─────────────────────────────────────────
async function syncCheck(svc: SupabaseClient, who: { id: string; role: string },
                         body: { assignment_id?: string; card_id?: string; pupil_answer?: string }) {
  const answer = typeof body.pupil_answer === "string" ? body.pupil_answer.slice(0, 500) : null;
  if (!body.card_id || answer === null) return json(400, { error: "bad_request" });
  if (who.role !== "student") return json(404, { error: "not_found" });

  const { data: a } = await svc.from("assignments")
    .select("id, class_id, school_id, set_by, kind, deleted_at, release_at")
    .eq("id", body.assignment_id).maybeSingle();
  if (!a || a.kind !== "flashcards" || a.deleted_at ||
      (a.release_at && new Date(a.release_at).getTime() > Date.now())) return json(404, { error: "not_found" });
  const { data: m } = await svc.from("class_members").select("id").eq("class_id", a.class_id)
    .eq("student_id", who.id).is("left_at", null).is("deleted_at", null).limit(1);
  if (!m?.length) return json(404, { error: "not_found" });

  const { data: card } = await svc.from("assignment_flashcards").select("id, question, answer")
    .eq("id", body.card_id).eq("assignment_id", a.id).maybeSingle();
  if (!card) return json(404, { error: "not_found" });

  // ⊕ MRB-353: this pupil already had this exact text checked on this card.
  const prior = (await storedVerdicts(svc, a.id, [who.id])).get(vkey(who.id, card.id, answer));
  if (prior) {
    await storeVerdict(svc, a.id, who.id, card.id, answer, prior);
    return json(200, { verdict: prior });
  }

  const key = Deno.env.get("ANTHROPIC_API_KEY");
  if (!key) return json(200, { skipped: "no_key" });

  let verdict: string | null = null;
  try {
    const { verdicts, usage } = await checkWithModel([{
      question: card.question, model_answer: card.answer, pupil_answer: answer,
    }], key);
    verdict = verdicts[0] ?? null;
    if (a.set_by) await logUsage(svc, "flashcard_answer_check", a.set_by, a.school_id, usage, { assignment_id: a.id });
  } catch {
    return json(200, { skipped: "model_error" });
  }
  if (!verdict) return json(200, { skipped: "no_verdict" });

  await storeVerdict(svc, a.id, who.id, card.id, answer, verdict);
  return json(200, { verdict });
}
