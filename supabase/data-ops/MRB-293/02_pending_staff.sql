insert into public.pending_staff (school_id, email, first_name, last_name, staff_code, profile_role, granted_by, reason)
select (select id from public.schools where code='RHS'), v.email::citext, v.first_name, v.last_name, v.staff_code, 'teacher',
       '74db2bf7-7c0d-47e6-9479-5cee3cda610e'::uuid,
       'MRB-293 Rainford science department setup, 2026-27'
from (values
  ('e.belford@rainford.org.uk','Emily','Belford','BLF'),
  ('g.bradbury@rainford.org.uk','Glen','Bradbury','BRB'),
  ('v.ellingham@rainford.org.uk','Victoria','Ellingham','ELV'),
  ('l.finnen@rainford.org.uk','Leon','Finnen','FNL'),
  ('j.heaton@rainford.org.uk','James','Heaton','HTJ'),
  ('s.harvey@rainford.org.uk','Samuel','Harvey','HRS'),
  ('s.jacks@rainford.org.uk','Siobhan','Jacks','JKS'),
  ('b.mckeown@rainford.org.uk','Benjamin','McKeown','MKB'),
  ('n.ruane@rainford.org.uk','Niamh','Ruane','RNN'),
  ('e.seary@rainford.org.uk','Emily','Seary','SRE'),
  ('r.spedding@rainford.org.uk','Richard','Spedding','SPD'),
  ('l.wilkinson@rainford.org.uk','Layla','Wilkinson','WKN')
) as v(email, first_name, last_name, staff_code)
where not exists (select 1 from public.pending_staff p where p.email = v.email::citext and p.deleted_at is null);