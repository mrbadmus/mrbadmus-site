-- ROLLBACK for mrb318_classes_consumer_kind. Apply by hand only.
-- ⚠️ Group classes (consumer_kind = 'group') become indistinguishable from a
-- pupil's own class once the column is gone, and the readers that exclude
-- 'group' (GET /family, classOf(), consumerPracticeFor) would then see two
-- classes per pupil. Soft-delete the group classes first, then drop.
update public.classes set deleted_at = now() where consumer_kind = 'group' and deleted_at is null;
alter table public.classes drop column if exists consumer_kind;
