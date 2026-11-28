-- TEST ONLY (qeppkiswvclkkwbxmlok). Fixtures for class_membership_drive.py.
-- Every id starts cb000000-…; class_membership_drive_teardown.sql removes
-- exactly these ids and the rows that point at them. Password: cb-throwaway-1
-- School/year: Rainford High School (TEST) 2026-27.
do $seed$
declare
  sch uuid := 'd0233615-3ee7-4b1b-a8ff-c912c5196d62';
  yr  uuid := '2f560a43-73b9-422a-8fc7-ec46524a288a';
  subj uuid := (select id from public.subjects order by name limit 1);
  u record;
begin
  for u in select * from (values
    ('cb000000-0000-0000-0000-000000000001'::uuid, 'cb_admin@throwaway.test',   'Ada',   'Admin',   'teacher', null),
    ('cb000000-0000-0000-0000-000000000002'::uuid, 'cb_teacher1@throwaway.test','Tom',   'Teach',   'teacher', null),
    ('cb000000-0000-0000-0000-000000000003'::uuid, 'cb_teacher2@throwaway.test','Tara',  'Second',  'teacher', null),
    ('cb000000-0000-0000-0000-000000000011'::uuid, 'cb_pupil1@throwaway.test',  'Maya',  'Mover',   'student', 'CB0011'),
    ('cb000000-0000-0000-0000-000000000012'::uuid, 'cb_pupil2@throwaway.test',  'Leo',   'Stayer',  'student', 'CB0012'),
    ('cb000000-0000-0000-0000-000000000013'::uuid, 'cb_pupil3@throwaway.test',  'Zara',  'Newcomb', 'student', 'CB0013')
  ) as t(id, email, fn, ln, role, adm) loop
    insert into auth.users (instance_id, id, aud, role, email, encrypted_password, email_confirmed_at,
                            raw_app_meta_data, raw_user_meta_data, created_at, updated_at,
                            confirmation_token, recovery_token, email_change_token_new, email_change)
    values ('00000000-0000-0000-0000-000000000000', u.id, 'authenticated', 'authenticated', u.email,
            extensions.crypt('cb-throwaway-1', extensions.gen_salt('bf')), now(),
            '{"provider":"email","providers":["email"]}', jsonb_build_object('first_name', u.fn),
            now(), now(), '', '', '', '')
    on conflict (id) do nothing;
    insert into auth.identities (id, user_id, provider_id, provider, identity_data, created_at, updated_at, last_sign_in_at)
    values (gen_random_uuid(), u.id, u.id::text, 'email',
            jsonb_build_object('sub', u.id::text, 'email', u.email, 'email_verified', true), now(), now(), now())
    on conflict do nothing;
    insert into public.profiles (id, first_name, last_name, role, school_id, key_stage, external_student_id, tier, science_pathway)
    values (u.id, u.fn, u.ln, u.role, sch, case when u.role = 'student' then 'KS3' end, u.adm, null, null)
    on conflict (id) do update set first_name = excluded.first_name, last_name = excluded.last_name,
      role = excluded.role, school_id = excluded.school_id, key_stage = excluded.key_stage,
      external_student_id = excluded.external_student_id, deleted_at = null,
      tier = null, science_pathway = null;
  end loop;

  insert into public.staff_scopes (profile_id, scope, school_id, granted_by, reason, started_at)
  select 'cb000000-0000-0000-0000-000000000001', 'school_admin', sch, 'f3260000-0000-0000-0000-000000000002', 'class membership drive', now() - interval '1 day'
   where not exists (select 1 from public.staff_scopes where profile_id = 'cb000000-0000-0000-0000-000000000001');

  insert into public.classes (id, school_id, academic_year_id, name, key_stage, year_group)
  values ('cb000000-0000-0000-0000-0000000000c1', sch, yr, 'CB 8q/Sc1', 'KS3', 8),
         ('cb000000-0000-0000-0000-0000000000c2', sch, yr, 'CB 8q/Sc2', 'KS3', 8)
  on conflict (id) do nothing;

  insert into public.class_teachers (class_id, teacher_id, subject_id, role)
  select c, t, subj, 'subject_teacher' from (values
    ('cb000000-0000-0000-0000-0000000000c1'::uuid, 'cb000000-0000-0000-0000-000000000002'::uuid),
    ('cb000000-0000-0000-0000-0000000000c2'::uuid, 'cb000000-0000-0000-0000-000000000003'::uuid),
    ('cb000000-0000-0000-0000-0000000000c1'::uuid, 'cb000000-0000-0000-0000-000000000001'::uuid)) v(c, t)
   where not exists (select 1 from public.class_teachers x where x.class_id = v.c and x.teacher_id = v.t);

  -- Maya and Leo in class 1 since September; Zara on the platform, in no class.
  insert into public.class_members (class_id, student_id, joined_via, joined_at)
  select 'cb000000-0000-0000-0000-0000000000c1', s, 'csv_import', '2026-09-03'
    from unnest(array['cb000000-0000-0000-0000-000000000011','cb000000-0000-0000-0000-000000000012']::uuid[]) s
   where not exists (select 1 from public.class_members m where m.class_id = 'cb000000-0000-0000-0000-0000000000c1' and m.student_id = s);

  -- Two closed papers in class 1 (Oct, Nov); Maya did the first.
  insert into public.assignments (id, class_id, teacher_id, subject_id, title, topic, quiz_type, due_at, school_id,
                                  key_stage, year_group, created_at, release_at, source, auto_generated, kind)
  values ('cb000000-0000-0000-0000-0000000000a1', 'cb000000-0000-0000-0000-0000000000c1',
          'cb000000-0000-0000-0000-000000000002', subj, 'Cells', 'Cells', 'topic_quiz', '2026-10-09 17:00+01', sch, 'KS3', 8,
          '2026-10-02', '2026-10-02', 'teacher', false, 'mcq_set'),
         ('cb000000-0000-0000-0000-0000000000a2', 'cb000000-0000-0000-0000-0000000000c1',
          'cb000000-0000-0000-0000-000000000002', subj, 'Particles', 'Particles', 'topic_quiz', '2026-11-13 17:00+00', sch, 'KS3', 8,
          '2026-11-06', '2026-11-06', 'teacher', false, 'mcq_set')
  on conflict (id) do nothing;
  insert into public.assignment_submissions (assignment_id, student_id, score, max_score, status, submitted_at, completed_at, attempts)
  select 'cb000000-0000-0000-0000-0000000000a1', 'cb000000-0000-0000-0000-000000000011', 8, 10, 'complete',
         '2026-10-08 18:00+01', '2026-10-08 18:00+01', 1
   where not exists (select 1 from public.assignment_submissions where assignment_id = 'cb000000-0000-0000-0000-0000000000a1');
end
$seed$;
