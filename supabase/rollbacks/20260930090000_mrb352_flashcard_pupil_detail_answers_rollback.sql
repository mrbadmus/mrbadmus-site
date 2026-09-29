-- Rollback of 20260930090000_mrb352_flashcard_pupil_detail_answers.sql.
-- Restores flashcard_pupil_detail to the body defined in
-- 20260924180100_mrb351_flashcards_functions.sql, verbatim
-- (prosrc md5 167c4c0e36f0e504c3da6bc32dd11f6b). Apply manually only.

begin;

create or replace function public.flashcard_pupil_detail(p_assignment uuid, p_pupil uuid)
returns jsonb
language plpgsql stable security definer set search_path to 'public' as $$
declare
  v_a public.assignments;
begin
  v_a := public.mrb351_teacher_gate(p_assignment);
  if not exists (select 1 from public.class_members cm
                  where cm.class_id = v_a.class_id and cm.student_id = p_pupil) then
    raise exception 'not_found' using errcode = '42501';
  end if;
  return jsonb_build_object(
    'pupil', (select jsonb_build_object('id', p.id, 'first_name', p.first_name,
                                        'last_name', p.last_name, 'display_name', p.display_name)
                from public.profiles p where p.id = p_pupil),
    'cards', coalesce((select jsonb_agg(jsonb_build_object(
        'id', af.id, 'position', af.position, 'question', af.question, 'answer', af.answer,
        'mine', pc.pupil_answer, 'check', pc.answer_check, 'written_ms', pc.written_ms,
        'secured', cs.secured, 'known', cs.known,
        'ratings', coalesce((select jsonb_agg(jsonb_build_object('rating', rv.rating, 'phase', rv.phase,
                     'at', rv.rated_at, 'think_ms', rv.think_ms, 'session_id', rv.session_id)
                     order by rv.rated_at)
                     from public.flashcard_reviews rv
                    where rv.assignment_id = p_assignment and rv.pupil_id = p_pupil
                      and rv.card_id = af.id), '[]'::jsonb)
      ) order by af.position)
      from public.assignment_flashcards af
      join public.flashcard_card_state(p_assignment, p_pupil) cs on cs.card_id = af.id
      left join public.flashcard_pupil_cards pc
        on pc.assignment_id = p_assignment and pc.pupil_id = p_pupil and pc.card_id = af.id
     where af.assignment_id = p_assignment), '[]'::jsonb),
    'sessions', coalesce((select jsonb_agg(jsonb_build_object(
        'id', s.id, 'started_at', s.started_at, 'ended_at', coalesce(s.ended_at, s.last_seen_at),
        'open', s.ended_at is null, 'active_ms', s.active_ms, 'cards_seen', s.cards_seen,
        'cards_rated', s.cards_rated, 'cards_made', s.cards_made,
        'median_think_ms', s.median_think_ms, 'rushed', s.rushed) order by s.started_at)
      from public.flashcard_sessions s
     where s.assignment_id = p_assignment and s.pupil_id = p_pupil), '[]'::jsonb)
  );
end $$;


revoke all on function public.flashcard_pupil_detail(uuid, uuid) from public, anon;
grant execute on function public.flashcard_pupil_detail(uuid, uuid) to authenticated;

commit;
