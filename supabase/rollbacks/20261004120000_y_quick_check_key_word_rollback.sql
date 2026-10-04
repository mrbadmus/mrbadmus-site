-- Rollback of 20261004120000_y_quick_check_key_word.sql — restores
-- production's flashcard_quick_check byte for byte (prosrc md5
-- e7115d4ab2090efa95187e6dd6abc3d3). One CREATE OR REPLACE; grants kept.

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
    -- ONE WORD: decided by whether that word is a word of the model answer.
    -- A lone function word is never an answer.
    when pa !~ ' ' and pa in ('the', 'a', 'an', 'it', 'is', 'in', 'of', 'and', 'to', 'on', 'by')
      then 'no'
    when pa !~ ' ' then
      case when (' ' || ma || ' ') like ('% ' || pa || ' %') then 'match' else 'no' end
    else null
  end
  from t
$function$;
