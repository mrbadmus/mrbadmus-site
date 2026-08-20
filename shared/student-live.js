/* ═══════════════════════════════════════════════════════════════════════
   student-live.js — PLACEHOLDER. The live data source is not wired yet.

   `student/class-ported.html` and `student/assignment-ported.html` end by
   loading this file. They define `window.__MRB_MOUNT__` and do not call it,
   and they carry no data of their own — so whatever loads this is the thing
   that decides what a student sees.

   ⚠️ THIS FILE IS A STUB WRITTEN BY THE DATA-SEAM UNIT so that the production
   pages have something to point at. Replacing it is somebody else's unit: read
   the student's class, roster, work and identity from Supabase, put them on
   `window.__MRB_DATA__` under the keys the fixtures use — see
   shared/student-fixture-class.js and shared/student-fixture-assignment.js,
   which are generated and list every key the pages read — and then call
   `window.__MRB_MOUNT__()`.

   It THROWS rather than falling back to the fixture. A fallback here would
   make "the production page cannot render Design's example data" a matter of
   configuration, and it is meant to be a matter of fact.
   ═══════════════════════════════════════════════════════════════════════ */
throw new Error(
  "student-live.js: the live data source is not wired yet. This page holds " +
  "no data of its own and will not mount. Provide window.__MRB_DATA__ and " +
  "call window.__MRB_MOUNT__().");
