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

  let body: { assignment_id?: string; session_id?: string };
  try { body = await req.json(); } catch { return json(400, { error: "bad_request" }); }
  if (!body.assignment_id) return json(400, { error: "no_assignment" });

  const { data: a } = await svc.from("assignments")
    .select("id, class_id, school_id, set_by, kind").eq("id", body.assignment_id).maybeSingle();
  if (!a || a.kind !== "flashcards") return json(404, { error: "not_found" });

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

async function run(svc: SupabaseClient, a: { id: string; school_id: string; set_by: string | null },
                   sessionId: string | null, pupilOnly: string | null, key: string) {
  const stale = new Date(Date.now() - 5 * 60 * 1000).toISOString();
  let q = svc.from("flashcard_pupil_cards").select("id, session_id, card_id, pupil_answer")
    .eq("assignment_id", a.id).eq("answer_check", "pending")
    .or(`check_claimed_at.is.null,check_claimed_at.lt.${stale}`).limit(200);
  if (sessionId) q = q.eq("session_id", sessionId);
  if (pupilOnly) q = q.eq("pupil_id", pupilOnly);
  const { data: rows } = await q;
  if (!rows?.length) return;

  // Claim them, so two callers never pay for the same answer twice.
  const now = new Date().toISOString();
  const { data: claimed } = await svc.from("flashcard_pupil_cards").update({ check_claimed_at: now })
    .in("id", rows.map((r) => r.id)).eq("answer_check", "pending").select("id, session_id, card_id, pupil_answer");
  if (!claimed?.length) return;

  const { data: snap } = await svc.from("assignment_flashcards").select("id, question, answer")
    .in("id", [...new Set(claimed.map((r) => r.card_id))]);
  const card = new Map((snap ?? []).map((c) => [c.id, c]));

  // Per sitting, in batches.
  const bySession = new Map<string, typeof claimed>();
  for (const r of claimed) bySession.set(r.session_id, [...(bySession.get(r.session_id) ?? []), r]);
  for (const group of bySession.values()) {
    for (let i = 0; i < group.length; i += BATCH) {
      const part = group.slice(i, i + BATCH).filter((r) => card.has(r.card_id));
      if (!part.length) continue;
      try {
        const { verdicts, usage } = await checkWithModel(part.map((r) => ({
          question: card.get(r.card_id)!.question,
          model_answer: card.get(r.card_id)!.answer,
          pupil_answer: r.pupil_answer,
        })), key);
        const at = new Date().toISOString();
        for (let k = 0; k < part.length; k++) {
          if (!verdicts[k]) continue;
          await svc.from("flashcard_pupil_cards").update({ answer_check: verdicts[k], checked_at: at })
            .eq("id", part[k].id).eq("answer_check", "pending");
        }
        if (a.set_by) await logUsage(svc, "flashcard_answer_check", a.set_by, a.school_id, usage, { assignment_id: a.id });
      } catch {
        // Left claimed; the claim goes stale after five minutes and the next
        // caller picks the rows up again.
      }
    }
  }
}
