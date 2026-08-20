-- MRB-269 phase 4c / MRB-265 — the class view's teacher chip.
--
-- ⚠️ APPLIED VIA MCP `apply_migration`; this file's timestamp is the version it
-- recorded (20260820001231) so `supabase db push` will not re-run it.
--
-- Measured on production before writing it, as the student b0308282 in 8r/Sc1:
--   class_teachers row for own class ...... 1  (visible — 20260819154015)
--   subjects.name via subject_id .......... 1  (visible)
--   profiles row for the teacher .......... 0  (NOT visible)
-- So a student can already tell that their class has a teacher and what
-- subject it is; what they cannot reach is the teacher's NAME. That single
-- missing join is the whole reason this needs SECURITY DEFINER.
--
-- Built on the class_shoutouts_for_viewer precedent, deliberately:
--   * plpgsql, STABLE SECURITY DEFINER, search_path pinned to public
--   * membership-gated — a member OR a teacher of the class
--   * returns an EMPTY payload rather than raising when not permitted, so a
--     caller renders its empty state instead of handling an error
--   * jsonb envelope with a named key, so the shape can grow without breaking
--
-- Returns DISPLAY NAME AND SUBJECT ONLY. No teacher_id, no email, no profile
-- row. A student surface has no use for an identifier it cannot act on, and a
-- SECURITY DEFINER function is exactly where that restraint has to be applied.
--
-- Proven on production four ways:
--   member student ....... {"teachers":[{"subject":"Science","display_name":"Mr Badmus"}]}
--   non-member student ... {"teachers":[]}
--   teacher of class ..... {"teachers":[{"subject":"Science","display_name":"Mr Badmus"}]}
--   anonymous ............ {"teachers":[]}

CREATE OR REPLACE FUNCTION public.class_teachers_for_viewer(p_class_id uuid)
RETURNS jsonb
LANGUAGE plpgsql
STABLE SECURITY DEFINER
SET search_path TO 'public'
AS $function$
DECLARE
  v_can_view boolean;
  v_rows     jsonb;
BEGIN
  v_can_view := auth_user_is_member_of_class(p_class_id)
             OR auth_user_teaches_class(p_class_id);

  IF NOT v_can_view THEN
    RETURN jsonb_build_object('teachers', '[]'::jsonb);
  END IF;

  SELECT COALESCE(
           jsonb_agg(
             jsonb_build_object('display_name', t.display_name,
                                'subject',      t.subject)
             ORDER BY t.subject NULLS LAST, t.display_name),
           '[]'::jsonb)
    INTO v_rows
  FROM (
    SELECT
      COALESCE(
        NULLIF(btrim(p.display_name), ''),
        NULLIF(btrim(COALESCE(p.first_name, '') || ' ' ||
                     COALESCE(p.last_name, '')), ''),
        'Teacher')                        AS display_name,
      s.name                              AS subject
    FROM class_teachers ct
    LEFT JOIN profiles p ON p.id = ct.teacher_id
    LEFT JOIN subjects s ON s.id = ct.subject_id
    WHERE ct.class_id  = p_class_id
      AND ct.ended_at  IS NULL
      AND ct.deleted_at IS NULL
  ) t;

  RETURN jsonb_build_object('teachers', v_rows);
END;
$function$;
