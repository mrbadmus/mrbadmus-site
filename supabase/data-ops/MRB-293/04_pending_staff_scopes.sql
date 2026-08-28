insert into public.pending_staff_scopes (pending_staff_id, scope)
select ps.id, v.scope
from (values
  ('HTJ','school_admin'),
  ('SPD','school_admin')
) as v(staff_code, scope)
join public.pending_staff ps on ps.staff_code = v.staff_code and ps.deleted_at is null
where not exists (select 1 from public.pending_staff_scopes x
                   where x.pending_staff_id = ps.id and x.scope = v.scope
                     and coalesce(x.department,'') = '');