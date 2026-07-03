// =====================================================================
// Edge Function: roster-import
// Stage 3 — CSV bulk import reconciliation engine (the spine).
//
// The frontend (teacher/import.html) parses + maps the CSV client-side with
// papaparse and POSTs a normalised plan here. This function:
//   1. authenticates the caller and confirms they are staff of a school;
//   2. reconciles IDEMPOTENTLY with the service role (bypasses RLS):
//        - find-or-create classes in the school's current academic year
//        - find-or-create student auth users (Admin API) + profiles
//        - attach class_members non-destructively (never deletes links)
//        - update changed profile fields (e.g. add surname)
//   3. supports dryRun: computes the exact plan WITHOUT writing anything;
//   4. writes ONE audit_log row per real import (who/when/counts/file hash).
//
// Re-running the same file is safe: 0 created, 0 attached, no duplicates,
// nothing destroyed. profiles.id is a hard FK to auth.users.id, so new
// students are pre-provisioned as confirmed auth users here (no email sent);
// on first school SSO login their verified email links automatically.
//
// KEY-STAGE RULE: the class a student is imported into governs their stage.
// The class's year_group (when supplied) is authoritative for its key_stage:
// Years 7–9 → KS3, 10–11 → KS4, 12–13 → KS5. We set profiles.key_stage to
// the class's key_stage and only set tier/science_pathway when that
// key_stage is 'KS4' (the profiles_tier_only_ks4 CHECK constraint). This
// keeps the write constraint-safe and idempotent — a single gated upsert is
// the only profile write path.
// =====================================================================

import { createClient } from "jsr:@supabase/supabase-js@2";

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

const json = (status: number, body: unknown) =>
  new Response(JSON.stringify(body), {
    status,
    headers: { ...CORS, "Content-Type": "application/json" },
  });

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

type StudentRow = {
  rowIndex?: number;
  email?: string;
  firstName?: string;
  lastName?: string;
  className?: string;
  tierOverride?: string | null;
  pathwayOverride?: string | null;
  externalStudentId?: string | null; // external MIS id (e.g. Synergy Admission Number) — store-only
};
type ClassSpec = {
  name: string;
  keyStage?: string;
  yearGroup?: number;
  tier?: string | null;
  pathway?: string | null;
  teacherId?: string | null;
  subjectId?: string | null;
};

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  if (req.method !== "POST") return json(405, { ok: false, error: "method_not_allowed" });

  const SUPABASE_URL = Deno.env.get("SUPABASE_URL")!;
  const SERVICE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
  const admin = createClient(SUPABASE_URL, SERVICE_KEY, {
    auth: { autoRefreshToken: false, persistSession: false },
  });

  // ── 1. Authenticate the caller (teacher JWT in Authorization header) ──
  const jwt = (req.headers.get("Authorization") || "").replace(/^Bearer\s+/i, "");
  if (!jwt) return json(401, { ok: false, error: "missing_token" });
  const { data: userData, error: userErr } = await admin.auth.getUser(jwt);
  if (userErr || !userData?.user) return json(401, { ok: false, error: "unauthorized" });
  const callerId = userData.user.id;

  const { data: caller } = await admin
    .from("profiles")
    .select("id, role, school_id")
    .eq("id", callerId)
    .single();
  if (!caller || !["teacher", "hod", "admin"].includes(caller.role) || !caller.school_id) {
    return json(403, { ok: false, error: "not_staff_of_school" });
  }
  const schoolId = caller.school_id as string;

  // ── 2. Parse + validate the payload ──
  let body: {
    dryRun?: boolean;
    source?: { fileName?: string; fileHash?: string; rowCount?: number };
    academicYearName?: string | null;
    classes?: ClassSpec[];
    students?: StudentRow[];
  };
  try {
    body = await req.json();
  } catch {
    return json(400, { ok: false, error: "invalid_json" });
  }
  const dryRun = body.dryRun !== false; // default to SAFE (dry-run) unless explicitly false
  const classes = Array.isArray(body.classes) ? body.classes : [];
  const students = Array.isArray(body.students) ? body.students : [];
  if (classes.length === 0) return json(400, { ok: false, error: "no_classes" });

  // ── 3. Resolve the school's current academic year ──
  let yearQ = admin
    .from("academic_years")
    .select("id, name")
    .eq("school_id", schoolId)
    .is("deleted_at", null);
  yearQ = body.academicYearName
    ? yearQ.eq("name", body.academicYearName)
    : yearQ.eq("is_current", true);
  const { data: year } = await yearQ.maybeSingle();
  if (!year) return json(400, { ok: false, error: "no_academic_year" });
  const yearId = year.id as string;

  const counts = {
    classesCreated: 0,
    classesFound: 0,
    studentsCreated: 0,
    profilesUpdated: 0,
    studentsAttached: 0,
    studentsAlreadyAttached: 0,
    studentsSkipped: 0,
  };
  const issues: Array<{ rowIndex?: number; email?: string; reason: string; detail?: string }> = [];

  // ── 4. find-or-create classes → name→id map ──
  const classMap = new Map<string, string | null>(); // null = would-create in dry-run
  const classSpecByName = new Map<string, ClassSpec>();
  const classKeyStageByName = new Map<string, string>();
  for (const c of classes) {
    if (!c?.name) continue;
    classSpecByName.set(c.name, c);
    // year_group is authoritative for the key stage when supplied (7–9 →
    // KS3, 10–11 → KS4, 12–13 → KS5); a client-sent keyStage that disagrees
    // is ignored so a class can never be, say, Year 7 + KS4.
    const yg = Number.isInteger(c.yearGroup) && c.yearGroup! >= 7 && c.yearGroup! <= 13
      ? (c.yearGroup as number)
      : null;
    const clientKeyStage = c.keyStage && ["KS3", "KS4", "KS5"].includes(c.keyStage) ? c.keyStage : null;
    const keyStage = yg !== null
      ? (yg <= 9 ? "KS3" : yg <= 11 ? "KS4" : "KS5")
      : (clientKeyStage ?? "KS4");
    classKeyStageByName.set(c.name, keyStage);
    // tier/pathway only valid at KS4 (DB CHECK constraint)
    const tier = keyStage === "KS4" ? (c.tier ?? null) : null;
    const pathway = keyStage === "KS4" ? (c.pathway ?? null) : null;
    const yearGroup = yg ?? (keyStage === "KS4" ? 10 : keyStage === "KS3" ? 7 : 12);

    const { data: existing } = await admin
      .from("classes")
      .select("id")
      .eq("school_id", schoolId)
      .eq("academic_year_id", yearId)
      .eq("name", c.name)
      .is("deleted_at", null)
      .maybeSingle();

    if (existing) {
      classMap.set(c.name, existing.id);
      counts.classesFound++;
    } else {
      counts.classesCreated++;
      if (dryRun) {
        classMap.set(c.name, null);
      } else {
        const { data: created, error: cErr } = await admin
          .from("classes")
          .insert({
            school_id: schoolId,
            academic_year_id: yearId,
            name: c.name,
            key_stage: keyStage,
            year_group: yearGroup,
            tier,
            science_pathway: pathway,
          })
          .select("id")
          .single();
        if (cErr || !created) {
          issues.push({ reason: "class_create_failed", detail: `${c.name}: ${cErr?.message}` });
          classMap.set(c.name, null);
          continue;
        }
        classMap.set(c.name, created.id);
        // optional: attach the named teacher to the class (idempotent)
        if (c.teacherId && c.subjectId) {
          const { data: ct } = await admin
            .from("class_teachers")
            .select("id")
            .eq("class_id", created.id)
            .eq("teacher_id", c.teacherId)
            .eq("subject_id", c.subjectId)
            .eq("role", "subject_teacher")
            .is("ended_at", null)
            .is("deleted_at", null)
            .maybeSingle();
          if (!ct) {
            await admin.from("class_teachers").insert({
              class_id: created.id,
              teacher_id: c.teacherId,
              subject_id: c.subjectId,
              role: "subject_teacher",
            });
          }
        }
      }
    }
  }

  // ── 5. process students (dedupe by email; flag messy rows) ──
  const seenEmail = new Set<string>();
  const seenExternalId = new Set<string>(); // in-file duplicate detection for the external MIS id
  for (const s of students) {
    const rawEmail = (s.email || "").trim();
    const email = rawEmail.toLowerCase();
    if (!email) {
      counts.studentsSkipped++;
      issues.push({ rowIndex: s.rowIndex, email: rawEmail, reason: "missing_email" });
      continue;
    }
    if (!EMAIL_RE.test(email)) {
      counts.studentsSkipped++;
      issues.push({ rowIndex: s.rowIndex, email: rawEmail, reason: "invalid_email" });
      continue;
    }
    if (seenEmail.has(email)) {
      counts.studentsSkipped++;
      issues.push({ rowIndex: s.rowIndex, email, reason: "duplicate_in_file" });
      continue;
    }
    seenEmail.add(email);

    const className = s.className || "";
    if (!classMap.has(className)) {
      counts.studentsSkipped++;
      issues.push({ rowIndex: s.rowIndex, email, reason: "unknown_class", detail: className });
      continue;
    }
    const classId = classMap.get(className); // may be null in dry-run

    // The class governs the student's key_stage; tier/pathway only apply at KS4.
    const classKeyStage = classKeyStageByName.get(className) || "KS4";
    const spec = classSpecByName.get(className);
    const effTier = (s.tierOverride ?? spec?.tier ?? null) || null;
    const effPathway = (s.pathwayOverride ?? spec?.pathway ?? null) || null;
    const desiredTier = classKeyStage === "KS4" ? effTier : null;
    const desiredPathway = classKeyStage === "KS4" ? effPathway : null;

    // resolve existing auth user by email
    const { data: existingId } = await admin.rpc("user_id_for_email", { p_email: email });
    let studentId: string | null = (existingId as string) || null;
    const preExisting = !!studentId;

    let existingProfile:
      | { role: string; first_name: string | null; last_name: string | null; tier: string | null; science_pathway: string | null; school_id: string | null; key_stage: string | null; external_student_id: string | null }
      | null = null;
    if (preExisting) {
      const { data: p } = await admin
        .from("profiles")
        .select("role, first_name, last_name, tier, science_pathway, school_id, key_stage, external_student_id")
        .eq("id", studentId)
        .maybeSingle();
      existingProfile = p as typeof existingProfile;
      // never downgrade or hijack a staff account via a student roster
      if (existingProfile && ["teacher", "hod", "admin"].includes(existingProfile.role)) {
        counts.studentsSkipped++;
        issues.push({ rowIndex: s.rowIndex, email, reason: "email_belongs_to_staff" });
        continue;
      }
    }

    // external MIS id (store-only — never used to match identity). Trim;
    // treat '' as null. Flag in-file duplicates but DON'T fail the row: drop
    // the dup id to null so the partial unique index can't reject the write —
    // the student is still imported (matched by email), just without the id.
    const rawExternalId = (s.externalStudentId || "").trim();
    let externalStudentId: string | null = rawExternalId || null;
    if (externalStudentId) {
      if (seenExternalId.has(externalStudentId)) {
        issues.push({ rowIndex: s.rowIndex, email, reason: "duplicate_external_id", detail: externalStudentId });
        externalStudentId = null;
      } else {
        seenExternalId.add(externalStudentId);
      }
    }

    // desired profile state — class-governed key_stage, KS4-gated tier/pathway
    const desired = {
      first_name: s.firstName ?? existingProfile?.first_name ?? null,
      last_name: s.lastName ?? existingProfile?.last_name ?? null,
      school_id: schoolId,
      key_stage: classKeyStage,
      tier: desiredTier,
      science_pathway: desiredPathway,
      // store-only; preserve a previously-stored id when this file omits it
      external_student_id: externalStudentId ?? existingProfile?.external_student_id ?? null,
    };

    if (preExisting) {
      // count a profile update only when something actually differs
      const changed =
        (existingProfile?.first_name ?? null) !== desired.first_name ||
        (existingProfile?.last_name ?? null) !== desired.last_name ||
        (existingProfile?.school_id ?? null) !== desired.school_id ||
        (existingProfile?.key_stage ?? null) !== desired.key_stage ||
        (existingProfile?.tier ?? null) !== desired.tier ||
        (existingProfile?.science_pathway ?? null) !== desired.science_pathway ||
        (existingProfile?.external_student_id ?? null) !== desired.external_student_id;
      if (changed) {
        counts.profilesUpdated++;
        if (
          (existingProfile?.first_name ?? null) &&
          desired.first_name &&
          existingProfile?.first_name !== desired.first_name
        ) {
          issues.push({
            rowIndex: s.rowIndex,
            email,
            reason: "name_updated",
            detail: `first_name "${existingProfile?.first_name}" → "${desired.first_name}"`,
          });
        }
      }
    } else {
      counts.studentsCreated++;
    }

    // ── single, idempotent, constraint-safe write path (real run only) ──
    if (!dryRun) {
      if (!studentId) {
        // brand-new student → pre-provision a confirmed auth user (no email sent)
        const { data: created, error: cErr } = await admin.auth.admin.createUser({
          email,
          email_confirm: true,
          user_metadata: { first_name: desired.first_name },
        });
        if (cErr || !created?.user) {
          const { data: retryId } = await admin.rpc("user_id_for_email", { p_email: email });
          if (!retryId) {
            counts.studentsCreated = Math.max(0, counts.studentsCreated - 1);
            counts.studentsSkipped++;
            issues.push({ rowIndex: s.rowIndex, email, reason: "auth_create_failed", detail: cErr?.message });
            continue;
          }
          studentId = retryId as string;
        } else {
          studentId = created.user.id;
        }
      }
      const { error: upErr } = await admin
        .from("profiles")
        .upsert({ id: studentId, role: "student", ...desired }, { onConflict: "id" });
      if (upErr) {
        if (preExisting) counts.profilesUpdated = Math.max(0, counts.profilesUpdated - 1);
        else counts.studentsCreated = Math.max(0, counts.studentsCreated - 1);
        counts.studentsSkipped++;
        issues.push({ rowIndex: s.rowIndex, email, reason: "profile_write_failed", detail: upErr.message });
        continue;
      }
    }

    // ── attach class_members non-destructively (idempotent) ──
    if (dryRun || !classId || !studentId) {
      // dry-run (or class would-be-created): treat as a fresh attach
      counts.studentsAttached++;
      continue;
    }
    const { data: member } = await admin
      .from("class_members")
      .select("id")
      .eq("class_id", classId)
      .eq("student_id", studentId)
      .is("left_at", null)
      .is("deleted_at", null)
      .maybeSingle();
    if (member) {
      counts.studentsAlreadyAttached++;
    } else {
      const { error: mErr } = await admin.from("class_members").insert({
        class_id: classId,
        student_id: studentId,
        joined_via: "csv_import",
      });
      if (mErr) {
        counts.studentsAlreadyAttached++; // unique-violation race → already attached
      } else {
        counts.studentsAttached++;
      }
    }
  }

  // ── 6. audit (real runs only) ──
  let auditId: string | null = null;
  if (!dryRun) {
    const { data: aid } = await admin.rpc("write_audit_event", {
      p_action: "csv_import",
      p_target_table: "class_members",
      p_target_id: null,
      p_payload: {
        source: body.source ?? null,
        academic_year: year.name,
        classes: classes.map((c) => c.name),
        counts,
        issue_count: issues.length,
      },
      p_actor_id: callerId,
      p_school_id: schoolId,
    });
    auditId = (aid as string) ?? null;
  }

  return json(200, { ok: true, dryRun, counts, issues, auditId });
});
