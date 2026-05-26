-- =====================================================================
-- Migration:        0009_class_shoutouts.sql
-- Stage:            2C — Class shoutouts (MRB-46) — Phase 1 (schema only)
-- Branch:           schools/mrb-46-shoutouts-schema
-- Apply target:     TEST PROJECT ONLY (qeppkiswvclkkwbxmlok)
-- DO NOT APPLY ON:  PRODUCTION (urklkrwevjtlfbwnipjn) until MRB-35
--                   (Stage 2C bundle merge) — held branch, see CLAUDE.md
-- Linear:           MRB-46 (Phase 1 — schema + RLS)
-- Author:           Drafted with Mide on 2026-05-24
-- =====================================================================
--
-- Creates the `class_shoutouts` table: short, teacher-authored notes of
-- recognition for students in a class. A shoutout carries at least one
-- of:
--   - template_key — one of six locked keys, resolved to display copy
--     on the frontend
--   - message      — free text ≤ 500 characters
-- Both may be set; at least one must be (table CHECK).
--
-- RLS model:
--   SELECT — teachers of the class OR active members (students) of the
--            class; soft-deleted rows hidden from everyone.
--   INSERT — only the teachers of THIS class; author must be the caller
--            themselves; recipient must be an active member of THIS
--            class; school-scoped (defence-in-depth).
--   UPDATE — author only AND must still teach the class. Used for soft
--            delete (set deleted_at) + any future edit-own flow.
--   DELETE — no policy. Hard deletes are blocked by default. Soft
--            delete only.
--
-- All four helper functions used here were created in 0001_schools_
-- layer. Argument name in helpers is `p_class_id` — we pass positionally.
--
-- Additive only — no DROPs, no UPDATEs to existing data, no changes to
-- existing tables. Wrapped in a single transaction.
-- =====================================================================

BEGIN;

-- SECTION 1 — TABLE
-- =====================================================================

CREATE TABLE public.class_shoutouts (
  id              uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
  class_id        uuid        NOT NULL REFERENCES public.classes(id)   ON DELETE RESTRICT,
  author_id       uuid        NOT NULL REFERENCES public.profiles(id)  ON DELETE RESTRICT,
  recipient_id    uuid        NOT NULL REFERENCES public.profiles(id)  ON DELETE RESTRICT,
  template_key    text        NULL,
  message         text        NULL,
  created_at      timestamptz NOT NULL DEFAULT now(),
  updated_at      timestamptz NOT NULL DEFAULT now(),
  deleted_at      timestamptz NULL,

  -- At least one of template or custom message must be present.
  CONSTRAINT class_shoutouts_content_chk
    CHECK (template_key IS NOT NULL OR message IS NOT NULL),

  -- Locked enum of six template keys (frontend resolves to display
  -- copy). Adding a 7th = one migration to relax this CHECK + frontend
  -- update.
  CONSTRAINT class_shoutouts_template_key_chk
    CHECK (template_key IS NULL OR template_key IN (
      'top_of_class',
      'brilliant_improvement',
      'every_assignment_on_time',
      'smashed_tough_topic',
      'bounced_back_strong',
      'helped_classmate'
    )),

  -- Custom message length cap.
  CONSTRAINT class_shoutouts_message_length_chk
    CHECK (message IS NULL OR char_length(message) <= 500)
);


-- SECTION 2 — INDEXES
-- =====================================================================
-- Two read paths Phase 2/3 will use:
--   1. "10A's class feed, newest first"   → (class_id, created_at DESC)
--   2. "Hannah's shoutouts, newest first" → (recipient_id, created_at DESC)
-- Both partial (exclude soft-deleted) since the SELECT policy hides
-- those rows anyway.
-- FK columns get their default B-tree indexes via REFERENCES.

CREATE INDEX class_shoutouts_class_created_idx
  ON public.class_shoutouts (class_id, created_at DESC)
  WHERE deleted_at IS NULL;

CREATE INDEX class_shoutouts_recipient_created_idx
  ON public.class_shoutouts (recipient_id, created_at DESC)
  WHERE deleted_at IS NULL;


-- SECTION 3 — RLS ENABLE + POLICIES
-- =====================================================================

ALTER TABLE public.class_shoutouts ENABLE ROW LEVEL SECURITY;

-- SELECT: teachers of the class OR active members of the class.
-- Soft-deleted rows are hidden from everyone.
CREATE POLICY class_shoutouts_select
  ON public.class_shoutouts FOR SELECT
  USING (
    deleted_at IS NULL
    AND (
      auth_user_teaches_class(class_id)
      OR auth_user_is_member_of_class(class_id)
    )
  );

-- INSERT: only teachers of THIS class; the author must be the caller
-- themselves (symmetry with UPDATE — no "on behalf of" attribution);
-- recipient must be an ACTIVE member of THIS class; the class must
-- belong to the caller's school (defence-in-depth — `auth_user_
-- teaches_class` already implies same school, but this guards against
-- future helper regressions).
--
-- "Active member" = `left_at IS NULL AND deleted_at IS NULL`, matching
-- the semantics of `auth_user_is_member_of_class`.
CREATE POLICY class_shoutouts_insert
  ON public.class_shoutouts FOR INSERT
  WITH CHECK (
    auth_user_teaches_class(class_id)
    AND class_school_id(class_id) = auth_user_school_id()
    AND author_id = auth.uid()
    AND recipient_id IN (
      SELECT cm.student_id
      FROM public.class_members cm
      WHERE cm.class_id = class_shoutouts.class_id
        AND cm.left_at IS NULL
        AND cm.deleted_at IS NULL
    )
  );

-- UPDATE: author only AND must still teach the class. WITH CHECK
-- mirrors USING so the author can't reassign the row to another
-- author/class on update.
CREATE POLICY class_shoutouts_update
  ON public.class_shoutouts FOR UPDATE
  USING (
    author_id = auth.uid()
    AND auth_user_teaches_class(class_id)
  )
  WITH CHECK (
    author_id = auth.uid()
    AND auth_user_teaches_class(class_id)
  );

-- DELETE: no policy. RLS denies by default. Soft delete is performed
-- by UPDATE setting deleted_at.

COMMIT;
