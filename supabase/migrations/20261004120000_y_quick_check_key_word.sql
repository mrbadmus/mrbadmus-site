-- Prompt Y (4 Oct 2026) — a one-word answer is Right only when it IS the
-- model answer's one key word.
--
-- BASE: production's flashcard_quick_check, prosrc md5
--   e7115d4ab2090efa95187e6dd6abc3d3 (read 4 Oct 2026). Carried forward byte
--   for byte except the ONE WORD block.
-- NEW:  prosrc md5 ab1d58c567c4ad5d6b7674154011fe20
-- Must match shared/flashcard-homework.js quickCheck() case for case
-- (tests/fixtures/quickcheck_cases.json, flashcard_engine_test.js).
-- One CREATE OR REPLACE; grants are kept; no DROP; no data writes.
-- Rollback: supabase/rollbacks/20261004120000_y_quick_check_key_word_rollback.sql

CREATE OR REPLACE FUNCTION public.flashcard_quick_check(p_pupil text, p_model text)
 RETURNS text
 LANGUAGE sql
 IMMUTABLE
 SET search_path TO 'public'
AS $function$
  with n as (
    select regexp_replace(lower(coalesce(p_pupil, '')), '[^a-z0-9 ]+', ' ', 'g') as pa,
           regexp_replace(lower(coalesce(p_model, '')), '[^a-z0-9 ]+', ' ', 'g') as ma
  ), t as (
    select btrim(regexp_replace(pa, '\s+', ' ', 'g')) as pa,
           btrim(regexp_replace(ma, '\s+', ' ', 'g')) as ma
      from n
  )
  select case
    when pa = '' then 'blank'
    when pa = ma then 'match'
    when pa in ('idk', 'i dont know', 'i don t know', 'dont know', 'don t know', 'dunno',
                'no idea', 'not sure', 'no clue', 'pass', 'skip', 'x', 'xx', 'xxx', 'na', 'n a',
                'unsure', 'forgot', 'i forgot', 'i dunno', 'idek', 'not a clue',
                'no answer', 'blank', 'nk', 'dk', 'dno', 'donno', 'i dno', 'hmm', 'um', 'erm')
      then 'blank'
    -- ONE WORD. A lone function word is never an answer. Any other single
    -- word is Right here only when it IS the model answer's one key word
    -- (function words and one- or two-character symbols such as J, N, kg
    -- aside): "joules" for "Joules (J)". Every other one-word answer goes to
    -- the answer check (null). Prompt Y, 4 Oct 2026: it used to be Right
    -- when it was ANY word of the model answer, so "energy" secured "The
    -- minimum amount of energy needed for particles to react".
    when pa !~ ' ' and pa in ('the', 'a', 'an', 'it', 'is', 'in', 'of', 'and', 'to', 'on', 'by')
      then 'no'
    when pa !~ ' ' and pa = (
      select string_agg(k.w, ' ' order by k.o)
        from regexp_split_to_table(ma, ' ') with ordinality as k(w, o)
       where length(k.w) > 2
         and k.w not in ('the', 'a', 'an', 'it', 'is', 'in', 'of', 'and', 'to', 'on', 'by'))
      then 'match'
    else null
  end
  from t
$function$;
