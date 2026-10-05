-- ============================================================================
-- PRODUCTION (urklkrwevjtlfbwnipjn — ends in N) — delete the junk test family
-- "Family f7678ce2".   NOT YET RUN.   Written 5 Oct 2026 for Mide + the lane.
--
-- How to run: Supabase dashboard → PRODUCTION project → SQL editor.
--   1. Run PART 1 alone. Read every row. It must list exactly:
--        1 school (kind = family), 3 profiles, 2 classes, 3 auth users, and the
--        13 other tables below with the counts in the comment beside each.
--      Anything else = stop and ask.
--   2. Run PART 2 (one transaction: DO blocks are atomic). It checks the school
--      is a family, checks every table's count BEFORE deleting, and again after.
--      Any mismatch raises an error and NOTHING is deleted.
--   3. Run PART 3. It must return zero rows.
--
-- Built from the live schema (5 Oct 2026, read-only): every foreign key that
-- points at schools / profiles / classes / academic_years / auth.users was
-- counted for these ids. Only the tables below hold rows; every other
-- referencing table is 0. No DELETE triggers exist on any of them. auth.users
-- deletion cascades to auth.identities (4 rows: 3 email + 1 google) and
-- nothing else holds rows. The subscription row has no Stripe customer, so
-- there is nothing to cancel in Stripe.
-- ============================================================================

-- PART 1 — LOOK FIRST ---------------------------------------------------------
select 'schools' t, id::text detail from schools where id='7cd25771-afc8-48ee-b081-8345ab9241c1'
union all select 'profiles', id::text||' '||coalesce(first_name,'') from profiles where id in ('f7678ce2-74b1-4aba-add4-8422e954e5b9','6b6e87b0-b013-4d63-b2a3-b2fef23cc06b','c1e90501-b07f-4f2c-b239-1573320c8daa')
union all select 'classes', id::text from classes where school_id='7cd25771-afc8-48ee-b081-8345ab9241c1'
union all select 'auth.users', id::text||' '||coalesce(email,'') from auth.users where id in ('f7678ce2-74b1-4aba-add4-8422e954e5b9','6b6e87b0-b013-4d63-b2a3-b2fef23cc06b','c1e90501-b07f-4f2c-b239-1573320c8daa')
union all select 'auth.identities', provider||' '||user_id::text from auth.identities where user_id in ('f7678ce2-74b1-4aba-add4-8422e954e5b9','6b6e87b0-b013-4d63-b2a3-b2fef23cc06b','c1e90501-b07f-4f2c-b239-1573320c8daa')
union all select 'audit_log (5)', id::text||' '||action from audit_log where school_id='7cd25771-afc8-48ee-b081-8345ab9241c1' or actor_id in ('f7678ce2-74b1-4aba-add4-8422e954e5b9','6b6e87b0-b013-4d63-b2a3-b2fef23cc06b','c1e90501-b07f-4f2c-b239-1573320c8daa')
union all select 'email_log (4)', id::text from email_log where org_id='7cd25771-afc8-48ee-b081-8345ab9241c1' or recipient_id='f7678ce2-74b1-4aba-add4-8422e954e5b9'
union all select 'parent_prefs (1)', profile_id::text from parent_prefs where profile_id='f7678ce2-74b1-4aba-add4-8422e954e5b9'
union all select 'work_generation_runs (2)', child_id::text||' '||week_start::text from work_generation_runs where child_id in ('6b6e87b0-b013-4d63-b2a3-b2fef23cc06b','c1e90501-b07f-4f2c-b239-1573320c8daa')
union all select 'child_plans (2)', child_id::text from child_plans where org_id='7cd25771-afc8-48ee-b081-8345ab9241c1'
union all select 'class_members (2)', id::text from class_members where class_id in (select id from classes where school_id='7cd25771-afc8-48ee-b081-8345ab9241c1')
union all select 'class_teachers (2)', id::text from class_teachers where class_id in (select id from classes where school_id='7cd25771-afc8-48ee-b081-8345ab9241c1')
union all select 'academic_years (1)', id::text from academic_years where school_id='7cd25771-afc8-48ee-b081-8345ab9241c1'
union all select 'staff_scopes (1)', id::text from staff_scopes where school_id='7cd25771-afc8-48ee-b081-8345ab9241c1'
union all select 'subscriptions (1)', org_id::text||' '||status from subscriptions where org_id='7cd25771-afc8-48ee-b081-8345ab9241c1';

-- PART 2 — DELETE, ALL OR NOTHING --------------------------------------------
do $$
declare
  fam  constant uuid   := '7cd25771-afc8-48ee-b081-8345ab9241c1';
  par  constant uuid   := 'f7678ce2-74b1-4aba-add4-8422e954e5b9';
  kids constant uuid[] := array['6b6e87b0-b013-4d63-b2a3-b2fef23cc06b','c1e90501-b07f-4f2c-b239-1573320c8daa']::uuid[];
  n int;
begin
  -- Guard 1: this really is the family school, with exactly these people in it.
  perform 1 from schools where id=fam and kind='family';
  if not found then raise exception 'school % is not a family school (or is gone)', fam; end if;
  select count(*) into n from profiles where school_id=fam;
  if n<>3 then raise exception 'school has % profiles, expected 3', n; end if;
  select count(*) into n from profiles where school_id=fam and id = any(array[par]||kids);
  if n<>3 then raise exception 'the 3 profiles in the school are not the 3 named ids'; end if;
  select count(*) into n from classes where school_id=fam;
  if n<>2 then raise exception 'school has % classes, expected 2', n; end if;

  -- Guard 2: nothing else refers to the family beyond what Part 1 listed.
  select count(*) into n from work_items where org_id=fam or child_id = any(kids);
  if n<>0 then raise exception 'work_items % <> 0', n; end if;
  select count(*) into n from family_messages where org_id=fam;
  if n<>0 then raise exception 'family_messages % <> 0', n; end if;
  select count(*) into n from stripe_events where org_id=fam;
  if n<>0 then raise exception 'stripe_events % <> 0', n; end if;
  select count(*) into n from subscriptions where org_id=fam and stripe_customer_id is not null;
  if n<>0 then raise exception 'subscription has a Stripe customer — cancel it in Stripe first'; end if;

  -- Deletes, children first. Each count must match Part 1 exactly.
  delete from audit_log where id in ('17ffe7fb-1ccd-49ef-b060-0a77f7667068','37b293e3-a72c-4b90-96d2-01bb365c22bb','6d0cd6b1-9632-4ebd-86e9-f944c246a040','84c9fd1c-4ca4-4350-be59-93f25a1b634e','cb80b274-9ceb-4113-a659-844473c16617');
  get diagnostics n = row_count; if n<>5 then raise exception 'audit_log % <> 5', n; end if;
  delete from email_log where id in ('93baf3e0-b18b-498e-ad0f-e5ca68dc58d8','9536b883-e8e0-4005-beb6-02577358311b','ae633cb0-9918-467d-9a9f-3be7a7dba724','deff4f83-f43a-4863-b7e8-c165bd17dddc');
  get diagnostics n = row_count; if n<>4 then raise exception 'email_log % <> 4', n; end if;
  delete from parent_prefs where profile_id=par;
  get diagnostics n = row_count; if n<>1 then raise exception 'parent_prefs % <> 1', n; end if;
  delete from work_generation_runs where child_id = any(kids) and week_start='2026-10-05'::date;
  get diagnostics n = row_count; if n<>2 then raise exception 'work_generation_runs % <> 2', n; end if;
  delete from child_plans where child_id = any(kids) and org_id=fam;
  get diagnostics n = row_count; if n<>2 then raise exception 'child_plans % <> 2', n; end if;
  delete from class_members where id in ('40693549-ad7d-4475-b11b-950d9ef5ccd7','6c7ad870-90ae-4059-b21f-a61d423419da');
  get diagnostics n = row_count; if n<>2 then raise exception 'class_members % <> 2', n; end if;
  delete from class_teachers where id in ('4d7210ee-ec99-4a11-979a-467688b380a9','aac1f057-f735-4c80-b868-1020319f85fa');
  get diagnostics n = row_count; if n<>2 then raise exception 'class_teachers % <> 2', n; end if;
  delete from classes where id in ('2531b743-30cc-4ebb-ace4-de46326e2bab','7be3d6dc-2fbe-48b7-9d1d-e8524ecda59a') and school_id=fam;
  get diagnostics n = row_count; if n<>2 then raise exception 'classes % <> 2', n; end if;
  delete from academic_years where id='3630facd-b284-4977-a6a8-7ad8a8cf2d78' and school_id=fam;
  get diagnostics n = row_count; if n<>1 then raise exception 'academic_years % <> 1', n; end if;
  delete from staff_scopes where id='18f46550-5ebf-4666-a824-32173635fca3' and school_id=fam;
  get diagnostics n = row_count; if n<>1 then raise exception 'staff_scopes % <> 1', n; end if;
  delete from subscriptions where org_id=fam;
  get diagnostics n = row_count; if n<>1 then raise exception 'subscriptions % <> 1', n; end if;
  delete from profiles where id = any(kids);          -- children first: they were created_by the parent
  get diagnostics n = row_count; if n<>2 then raise exception 'child profiles % <> 2', n; end if;
  delete from profiles where id=par;
  get diagnostics n = row_count; if n<>1 then raise exception 'parent profile % <> 1', n; end if;
  delete from schools where id=fam and kind='family';
  get diagnostics n = row_count; if n<>1 then raise exception 'schools % <> 1', n; end if;
  delete from auth.users where id = any(array[par]||kids);   -- cascades auth.identities
  get diagnostics n = row_count; if n<>3 then raise exception 'auth.users % <> 3', n; end if;

  -- Final check inside the transaction: nothing of the family is left.
  select count(*) into n from auth.identities where user_id = any(array[par]||kids);
  if n<>0 then raise exception 'identities left: %', n; end if;
  select count(*) into n from profiles where id = any(array[par]||kids) or school_id=fam;
  if n<>0 then raise exception 'profiles left: %', n; end if;
end $$;

-- PART 3 — AFTER: must return NO ROWS ----------------------------------------
select 'left' t, id::text from schools where id='7cd25771-afc8-48ee-b081-8345ab9241c1'
union all select 'left', id::text from auth.users where id in ('f7678ce2-74b1-4aba-add4-8422e954e5b9','6b6e87b0-b013-4d63-b2a3-b2fef23cc06b','c1e90501-b07f-4f2c-b239-1573320c8daa')
union all select 'left', id::text from profiles where id in ('f7678ce2-74b1-4aba-add4-8422e954e5b9','6b6e87b0-b013-4d63-b2a3-b2fef23cc06b','c1e90501-b07f-4f2c-b239-1573320c8daa')
union all select 'left', id::text from classes where school_id='7cd25771-afc8-48ee-b081-8345ab9241c1';
-- Afterwards run the Rainford health check as with every production step.
