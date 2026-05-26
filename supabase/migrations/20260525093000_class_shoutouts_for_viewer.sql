-- =====================================================================
-- Migration:        20260525093000_class_shoutouts_for_viewer.sql
-- Stage:            2C — Class shoutouts (MRB-46) — Phase 3 v2 bugfix
-- Branch:           schools/mrb-46-phase-3-student-class
-- Apply target:     TEST PROJECT ONLY (qeppkiswvclkkwbxmlok)
-- DO NOT APPLY ON:  PRODUCTION (urklkrwevjtlfbwnipjn) until MRB-35
-- Linear:           MRB-46 (Phase 3 v2 — author names em-dash bug)
-- Author:           Drafted with Mide on 2026-05-25
-- =====================================================================
--
-- Adds class_shoutouts_for_viewer(p_class_id, p_limit, p_before_created_at)
-- — a SECURITY DEFINER function that returns paginated shoutouts WITH
-- joined author + recipient profile data (first_name, last_name,
-- avatar_url).
--
-- ── The bug this fixes ─────────────────────────────────────────────
-- Phase 3 v1 used a PostgREST embedded-resource query
-- (`profiles!class_shoutouts_author_id_fkey(first_name,…)`) for the
-- author + recipient join. RLS on `profiles` only allows:
--   - own row (auth.uid() = id)
--   - admin reads same-school
--   - HoD reads dept
--   - teacher reads STUDENTS in their classes
-- There is NO policy that lets students read teachers' profiles, or
-- teachers read other teachers' profiles. So when a student opened a
-- class shoutout feed (or a teacher viewed shoutouts authored by
-- another teacher), the joined profile rows returned null, and the
-- frontend rendered "by — · 1 hour ago" with an em-dash where the
-- name should have been.
--
-- ── Why not widen the profiles RLS instead? ────────────────────────
-- Widening profiles SELECT to "any same-school user" would expose
-- sensitive columns (target_grade, weaknesses, recent_results,
-- personal_note) across the whole school. Postgres RLS is whole-row;
-- column-level restrictions aren't available without a view or
-- function.
--
-- This function returns ONLY the safe display fields (first_name,
-- last_name, avatar_url) for the author and recipient of each
-- shoutout. No sensitive data leaks. The membership/teaches gate at
-- the top of the function is the security boundary.
--
-- ── Membership gate ────────────────────────────────────────────────
-- The caller must be either:
--   - an active member of the class (student viewing their own class), OR
--   - an active teacher of the class (teacher viewing their own class)
-- Non-callers get { shoutouts: [], hasMore: false }.
--
-- Mirrors the SELECT policy on class_shoutouts itself (which already
-- allows both audiences) — the function just provides the profile-
-- join capability that PostgREST's vanilla embedded resources can't,
-- without widening profiles RLS.
--
-- ── Pagination ─────────────────────────────────────────────────────
-- Cursor-based on created_at (same as the Phase 2 / Phase 3 v1
-- pagination shape). Caller passes p_before_created_at for "load more."
-- p_limit is capped at 100 defensively.
--
-- ── Return shape ───────────────────────────────────────────────────
-- Matches the existing JS-side shape exactly so the data layers and
-- renderers don't need restructuring:
--   {
--     "shoutouts": [
--       {
--         id, template_key, message, created_at,
--         author_id, recipient_id,
--         author:    { first_name, last_name, avatar_url } | null,
--         recipient: { first_name, last_name, avatar_url } | null
--       }
--     ],
--     "hasMore": boolean
--   }
--
-- Wrapped in a transaction. CREATE OR REPLACE is idempotent.
-- =====================================================================

BEGIN;

CREATE OR REPLACE FUNCTION public.class_shoutouts_for_viewer(
  p_class_id          uuid,
  p_limit             int           DEFAULT 20,
  p_before_created_at timestamptz   DEFAULT NULL
)
RETURNS jsonb
LANGUAGE plpgsql
STABLE
SECURITY DEFINER
SET search_path TO 'public'
AS $$
DECLARE
  v_limit  int;
  v_can_view boolean;
  v_rows   jsonb;
  v_count  int;
BEGIN
  v_limit := LEAST(GREATEST(COALESCE(p_limit, 20), 1), 100);

  -- Membership / teaching gate. Both audiences are legitimate; mirrors
  -- the class_shoutouts_select policy. Non-viewers get empty.
  v_can_view :=
    auth_user_is_member_of_class(p_class_id)
    OR auth_user_teaches_class(p_class_id);
  IF NOT v_can_view THEN
    RETURN jsonb_build_object('shoutouts', '[]'::jsonb, 'hasMore', false);
  END IF;

  -- Fetch the page. ORDER BY + LIMIT inside the subquery so the
  -- jsonb_agg preserves chronological-newest-first order. The
  -- caller does NOT receive a sort guarantee from jsonb_agg
  -- otherwise. The page's caller is responsible for the cursor
  -- (p_before_created_at = last loaded row's created_at).
  WITH page AS (
    SELECT
      s.id, s.template_key, s.message, s.created_at,
      s.author_id, s.recipient_id,
      jsonb_build_object(
        'first_name', author.first_name,
        'last_name',  author.last_name,
        'avatar_url', author.avatar_url
      ) AS author,
      jsonb_build_object(
        'first_name', recipient.first_name,
        'last_name',  recipient.last_name,
        'avatar_url', recipient.avatar_url
      ) AS recipient
    FROM class_shoutouts s
    LEFT JOIN profiles author    ON author.id    = s.author_id
    LEFT JOIN profiles recipient ON recipient.id = s.recipient_id
    WHERE s.class_id = p_class_id
      AND s.deleted_at IS NULL
      AND (p_before_created_at IS NULL OR s.created_at < p_before_created_at)
    ORDER BY s.created_at DESC
    LIMIT v_limit
  )
  SELECT
    COALESCE(
      jsonb_agg(
        jsonb_build_object(
          'id',           p.id,
          'template_key', p.template_key,
          'message',      p.message,
          'created_at',   p.created_at,
          'author_id',    p.author_id,
          'recipient_id', p.recipient_id,
          'author',       p.author,
          'recipient',    p.recipient
        )
        ORDER BY p.created_at DESC
      ),
      '[]'::jsonb
    ),
    COUNT(*)
  INTO v_rows, v_count
  FROM page p;

  RETURN jsonb_build_object(
    'shoutouts', v_rows,
    'hasMore',   v_count >= v_limit
  );
END;
$$;

GRANT EXECUTE ON FUNCTION public.class_shoutouts_for_viewer(uuid, int, timestamptz) TO authenticated;

COMMIT;
