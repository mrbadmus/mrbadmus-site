-- MRB-265 — a student can read who teaches them.
--
-- ⊕ RULING (Mide, 19 Aug 2026): yes, students should see their teacher's name.
--
-- `class_teachers` had five read policies and not one of them described a
-- STUDENT: admin, SLT, HoD, operator, and the teacher's own row. So the class
-- page had a teacher's name to show and no way to read it, and `student-data.js`
-- reconstructed the subject from the class NAME instead — parsing `/Sc` and
-- `/Ph` out of `8r/Sc1`. That is a second derivation of a fact the table
-- already holds, and the duplication was marked in the source.
--
-- The predicate is not a new invention: it is character for character the one
-- `assignments_student_read` already uses on the same class_id, so a student
-- can see the teachers of exactly the classes whose assignments they can see.
-- Both helpers are STABLE SECURITY DEFINER and already back that policy.
--
-- ⚠️ SELECT ONLY. Nothing here lets a student write, and membership is the
-- whole discriminator: `auth_user_is_member_of_class` requires a live
-- `class_members` row (left_at IS NULL AND deleted_at IS NULL), so a student
-- who has left the class stops seeing it.
--
-- Applied via MCP `apply_migration`, which recorded version 20260819154015.
-- This filename carries that version deliberately: a mismatch would make
-- `supabase db push` re-apply the statement and fail on the duplicate policy.
--
-- PROVEN BY MUTATION on production (urklkrwevjtlfbwnipjn), as the student AY
-- (b0308282…) who is a member of 8r/Sc1 and of no other class:
--     with this policy      → 1 row for 8r/Sc1, 0 for 7h/Sc5, 1 in the table
--     with it destroyed     → 0 rows for 8r/Sc1
-- The destroying transaction was rolled back by a raised exception.

create policy class_teachers_member_read on public.class_teachers
  for select using (
    public.class_school_id(class_id) = public.auth_user_school_id()
    and public.auth_user_is_member_of_class(class_id)
  );
