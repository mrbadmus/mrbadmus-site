-- MRB-321 Night 4 — the parent's acceptance of the terms, stamped once and never moved.
--
-- The signup account step now carries "I agree to the terms and privacy policy" and
-- will not proceed without it. That tick has to leave a trace, because the only thing
-- that makes it worth asking for is being able to say WHEN it was given.
--
-- Nullable on purpose, and no backfill. Every existing row stays NULL, which is the
-- honest answer: those parents signed up before the checkbox existed and we did not
-- ask them. A DEFAULT now() here would have written a lie onto every row in the table.
--
-- The write path is service-role only (POST /api/consumer/family/ensure and
-- PATCH /api/consumer/parent, both with `terms_accepted: true`), and both refuse to
-- overwrite a non-NULL value — an earlier acceptance is the one that counts.
alter table public.profiles
  add column if not exists terms_accepted_at timestamptz;

comment on column public.profiles.terms_accepted_at is
  'MRB-321: when this account holder ticked "I agree to the terms and privacy policy" at signup. NULL = never asked (pre-MRB-321 rows) or never given. Stamped once by the backend; never overwritten.';
