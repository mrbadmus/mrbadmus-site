# ADR: Revision Materials Library — storage & data model

## Status

Accepted — 16 May 2026 (Mide). Spec frozen for the MRB-62 build. Further
changes go to a v2 ticket under MRB-60.

## Context

MRB-60 introduces a public-facing revision-materials library. Pattern B
access model: metadata visible to everyone (marketing surface), file bytes
gated to logged-in users via signed URLs. Decisions needed on storage
backend and the database shape that holds material metadata.

## Decisions

### 1. Storage backend — Supabase Storage, PRIVATE bucket

- Bucket name: `revision-materials`
- Bucket policy: private. No anon access to objects.
- Downloads served via short-lived signed URLs generated from an
  authenticated session.

Rationale: already on Supabase Pro (no new vendor/cost); native auth
tie-in keeps the Pattern B gating clean; security model decided up front
rather than retrofitted.

The Storage bucket itself is created in MRB-63, NOT in this ticket.

### 2. Intentional divergence from MRB-27 (inline images)

Inline images may use a different storage approach (small, public,
perf-sensitive — CDN/repo defensible). Divergence is deliberate.

### 3. Data model — `revision_materials` table

| Column            | Type                              | Notes |
|---|---|---|
| `id`              | uuid pk                           | |
| `title`           | text not null                     | |
| `description`    | text                              | nullable |
| `subject`         | text not null                     | check: biology \| chemistry \| physics |
| `pathway`         | text not null                     | check: combined \| triple |
| `tier`            | text not null                     | check: foundation \| higher |
| `paper`           | text not null                     | check: paper_1 \| paper_2 (stored, not derived) |
| `topic`           | text not null                     | canonical AQA slug — see taxonomy below |
| `material_type`   | text not null                     | check: notes \| worksheet \| mark_scheme \| pack \| other |
| `file_path`       | text not null                     | Supabase Storage object key (private bucket) |
| `file_size_bytes` | bigint                            | nullable — MUST stay nullable to avoid coupling this ticket to MRB-63 |
| `school_id`       | uuid                              | nullable; NULL = all schools (v1 RLS unused) |
| `created_at`      | timestamptz not null default now() | |
| `deleted_at`      | timestamptz                       | soft delete |

No `subtopic` column. Topic-level only (~7 buckets per subject per paper).
Subtopic granularity explicitly deferred.

### 4. Pathway column name — `pathway` (not `science_pathway`)

Schools-layer convention: person rows use `science_pathway` (profiles,
classes); content rows use `pathway` (weekly_challenges, weekly_scores,
scheme_of_work_entries, scheme_of_work_overrides). `revision_materials`
is a content row, so it uses `pathway`.

### 5. File path / naming convention

`file_path` stores the Supabase Storage object key (not a URL). Proposed
key structure (locked when MRB-63 builds the bucket, not in this ticket):

`{pathway}/{tier}/{subject}/{paper}/{topic}/{material_type}/{uuid}-{slug}.{ext}`

Example: `combined/foundation/biology/paper_1/cell-biology/notes/8e1a-eukaryotes-summary.pdf`

The `{uuid}` prefix prevents same-title collisions.

### 6. RLS policy

- SELECT: public (anon + authenticated). Soft-deleted rows hidden by
  `USING (deleted_at IS NULL)`.
- INSERT / UPDATE / DELETE: no policies → no client writes. Service role
  bypasses RLS for legitimate admin operations.
- `school_id` nullable and NOT used in v1 RLS. Per-school scoping is a
  future v2 decision.

### 7. RLS reminder — bucket vs. table

`revision_materials` table SELECT is public (metadata = marketing
surface), but the Storage bucket holding the file bytes is PRIVATE. File
access is gated separately from metadata. That separation IS Pattern B.

## Canonical AQA topic taxonomy

Source of truth: `SITE_DATA` in `generate_site_v5.py`. Mirrored here so
the separate Claude chat authoring revision content can file documents
against the same labels (prevents MRB-67 reconciliation drift). If
`SITE_DATA` ever changes, update this table AND the
`revision_materials_topic_check` constraint in lock-step.

### Biology (AQA 8461 / Combined 8464)

| Paper   | Topic slug          | Topic name                            | Spec |
|---|---|---|---|
| paper_1 | cell-biology        | Cell Biology                          | 4.1  |
| paper_1 | organisation        | Organisation                          | 4.2  |
| paper_1 | infection-response  | Infection and Response                | 4.3  |
| paper_1 | bioenergetics       | Bioenergetics                         | 4.4  |
| paper_2 | homeostasis         | Homeostasis and Response              | 4.5  |
| paper_2 | inheritance         | Inheritance, Variation and Evolution  | 4.6  |
| paper_2 | ecology             | Ecology                               | 4.7  |

### Chemistry (AQA 8462 / Combined 8464)

| Paper   | Topic slug         | Topic name                                  | Spec |
|---|---|---|---|
| paper_1 | atomic-structure   | Atomic Structure and the Periodic Table     | 4.1  |
| paper_1 | bonding            | Bonding, Structure and Properties of Matter | 4.2  |
| paper_1 | quantitative       | Quantitative Chemistry                      | 4.3  |
| paper_1 | chemical-changes   | Chemical Changes                            | 4.4  |
| paper_1 | energy-changes     | Energy Changes                              | 4.5  |
| paper_2 | rates-equilibrium  | Rate and Extent of Chemical Change          | 4.6  |
| paper_2 | organic            | Organic Chemistry                           | 4.7  |
| paper_2 | analysis           | Chemical Analysis                           | 4.8  |
| paper_2 | atmosphere         | Chemistry of the Atmosphere                 | 4.9  |
| paper_2 | resources          | Using Resources                             | 4.10 |

### Physics (AQA 8463 / Combined 8464)

| Paper   | Topic slug      | Topic name                       | Spec | Pathways          |
|---|---|---|---|---|
| paper_1 | energy          | Energy                           | 4.1  | Combined + Triple |
| paper_1 | electricity     | Electricity                      | 4.2  | Combined + Triple |
| paper_1 | particle-model  | Particle Model of Matter         | 4.3  | Combined + Triple |
| paper_1 | atomic-structure| Atomic Structure                 | 4.4  | Combined + Triple |
| paper_2 | forces          | Forces                           | 4.5  | Combined + Triple |
| paper_2 | waves           | Waves                            | 4.6  | Combined + Triple |
| paper_2 | magnetism       | Magnetism and Electromagnetism   | 4.7  | Combined + Triple |
| paper_2 | space           | Space Physics                    | 4.8  | **Triple only**   |

The migration enforces "physics + topic=space ⇒ pathway ≠ combined" via a
dedicated CHECK constraint. This prevents content-gating violations —
Combined students must never see Space Physics.

## Out of scope for MRB-62

- The Storage bucket itself (MRB-63)
- Upload tooling / admin UI
- Signed-URL download flow
- Public list page
- School-scoped RLS (deferred to a future v2 ticket)
