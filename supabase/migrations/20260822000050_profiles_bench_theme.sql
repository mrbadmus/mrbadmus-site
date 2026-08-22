-- profiles.bench_theme — the student's chosen bench theme.
--
-- MRB · 21 Aug 2026. Design's class-view amendments give the student six
-- bench themes. The choice is SERVER-SIDE on the profile, not in the browser,
-- so it follows them between the school machine and their phone — the same
-- rule assignment state already follows. The browser copy is a cache.
--
-- NULL IS A REAL VALUE AND IT MEANS HARBOUR. Design's contract is that the
-- page root carries `data-bench-theme` and that the attribute being ABSENT is
-- harbour, the default. Defaulting the column to 'harbour' would say the same
-- thing in one more place, and would then disagree with the CSS the first time
-- somebody changed the default in one of them. So the column stays NULL until
-- a student actually chooses, and "no row, no preference, no attribute" is one
-- state throughout rather than three.
--
-- The CHECK is the whole point of a named column rather than a jsonb blob:
-- six values exist, the database knows which, and a typo is rejected at the
-- write instead of rendering an unstyled bench.

alter table public.profiles
  add column if not exists bench_theme text;

alter table public.profiles
  drop constraint if exists profiles_bench_theme_check;

alter table public.profiles
  add constraint profiles_bench_theme_check
  check (bench_theme is null or bench_theme in
         ('harbour', 'clay', 'chalk', 'moss', 'damson', 'graphite'));

comment on column public.profiles.bench_theme is
  'Student''s chosen bench theme for the class view. NULL = harbour (the default). One of harbour|clay|chalk|moss|damson|graphite.';
