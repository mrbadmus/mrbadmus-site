# Claude Code brief — Redesign port + content overhaul

**Companion documents (read all three before touching anything):**
1. `content_standards.md` — the content quality law. Every rule referenced below lives there.
2. `bonding_pilot_design_map.md` — archetype library + per-page map for the pilot unit.
3. `design_brief_bonding_heroes.md` — what Design is delivering and in what shape.

**Decision log (locked):**
- Hero interactives port to **vanilla JS**. No React, no runtime dependencies. Design's `.dc.html` files use a React-based canvas format (`DCLogic` classes, `{{ }}` bindings, `<sc-for>`/`<sc-if>`); treat them as a **specification of behaviour and appearance**, not as code to run. Re-implement the state machine and rendering in plain JS + DOM.
- Design's shipped tokens are canon: Space Grotesk / IBM Plex Sans / IBM Plex Mono; page `#E7E1D4`, card `#F5F1E8`, panel `#FFFDF8`, border `#E4DCCB`; burnt-orange accent family (`#E0531F` / `#C0392B` / `#B5341A`); contextual accents (endo blue `#2E7DD1`, sage `#3E6B47`). One warm palette, no per-subject colour system.
- Brand rule stands: public pages use the orange chevron + "MrBadmusAI". No octopus, no ⚗️ anywhere.

**Working constraints (non-negotiable, from standing practice):**
- Recon first. Read the generator and current page structure before editing anything.
- All shared JS/CSS as real files loaded by the generator via `os.path.abspath(__file__)` file-reads. Never embedded Python string blobs.
- Everything user-facing lands in `mrbadmus_site/`. Cloudflare serves from there.
- Commit with clear messages; pushes stay with Mide via GitHub Desktop.
- Work on a worktree; one Code session drives main at a time.
- Linear: this work should be ticketed before execution. Reactivate MRB-105 (assessment quality overhaul) with `content_standards.md` as its spec; file the port as a new ticket or under MRB-102's successor as directed. Closing comment with commit SHA first, then state change, separate calls.

---

## Phase 1 — Site-wide content audit

**Goal:** a defect table for the whole site (all 317+ pages, all tier/pathway variants) against `content_standards.md`. No fixes in this phase. Audit only.

**Method:**
1. Recon the generator's content source (the Python data structures feeding `generate_site_v5.py`). Audit **the source**, not the generated HTML, wherever possible — that's where fixes will land and it avoids generator noise.
2. Mechanical checks, scripted:
   - Test Yourself count per page per variant (rule 1). Flag: any page under 5 (severity: critical), under target 10 without a "light page" justification (severity: major).
   - FIFA blocks: worked-example count (< 3 = major), presence of interactive practice (absent = major), cross-tier value duplication — string/number-compare example values between Foundation and Higher/Triple variants of the same page; identical = fake differentiation (major).
   - Common Mistake blocks: first-sentence pattern check — does it state a mistake (student action/belief), or is it a mislabelled Key Note (major).
   - Block lineup fingerprint: hash each page's optional-block lineup; large clusters of identical lineups flagged for deliberateness review (minor, informational).
3. Judgement checks, AI-read with flags for human spot-check:
   - Distractor quality: are wrong options diagnostic (encode a misconception or classic working error) or filler?
   - Command-word usage and exam register in stems.
   - Tier integrity: does the Higher variant actually demand more, or is it the same page with a harder badge?
4. **Output:** one table (CSV or markdown in the repo), columns: page, subject, tier/pathway, block, rule, severity, one-line evidence. Sorted worst-first: Higher/Triple pages with multiple critical/major defects at the top.
5. Post the summary counts (defects by rule and severity) to the Linear ticket. Stop. **Mide reviews the table before any Phase 2 content work begins.**

## Phase 2 — Pilot port + content fix (Chemistry Bonding unit)

Runs only after Phase 1 review. Unit-by-unit thereafter; Bonding first per the pilot map.

### 2a. Foundation layer (once, shared)
1. Token stylesheet: `redesign.css` (or equivalent) as a real source file with the canonical `:root` custom-property block from Design's Part 1 output. Loaded via the generator's file-read pattern.
2. Page template: implement Design's documented skeleton (Part 2 of the Design brief) as the generator's page template, with each block a named, **optional** slot driven by per-page content data. Optional means genuinely absent from output when unused, not hidden.
3. Standard blocks wire into existing plumbing, not rebuilt: Test Yourself → existing quiz system, Ask AI → existing Anthropic tutor integration, Star Rating and Footer Nav → existing mechanisms. Matching gets a vanilla implementation (see below) since it's now a reusable archetype.

### 2b. Hero + activity components (vanilla ports)
For each component Design delivers (State Toggle Lab, Dot-and-Cross Stepper, Two-State Compare, Structure Hotspot, Zoom/Scale Explorer, plus the shared Matching and FIFA blocks):
1. Read Design's `.dc.html` for that component. Extract: the CONFIG schema, the state machine (constructor state + methods), and the rendered structure/styles.
2. Re-implement as one vanilla JS module per archetype: `heroes/<archetype>.js`, exposing an init function taking a container element + config object. All content via config; nothing hardcoded.
3. FIFA (new, per content standards §2): step-reveal worked examples (≥3, escalating) + interactive practice mode where each FIFA step is a checked input/choice with step-specific feedback. Config carries tier-differentiated example sets.
4. Match Design's visual output closely — spacing, radii, shadows, animation feel. Where Design used scroll-timeline animations (`animation-timeline: view()`), provide a graceful fallback (IntersectionObserver or static) since browser support is partial.
5. Each module gets a standalone test page in a scratch area proving two different configs render correctly, before generator integration.

### 2c. Bonding pages
1. Confirm the real page list against the generator (the pilot map's Part 3 question — merge/split as the source actually has it).
2. For each Bonding page: apply the template, instantiate heroes per the pilot map, and **fix all Phase 1 defects for that page against content standards** — question counts to target, exam-register MCQs with diagnostic distractors, FIFA sets with real tier differentiation (conversions and rearrangement at Higher), Common Mistake blocks in the three-beat format or removed if no genuine misconception exists.
3. Content drafted to spec is flagged per §7 of the standards: full-review items (Higher/Triple calculations, all FIFA sets) listed explicitly in the ticket for Mide's review; low-confidence drafts flagged regardless of category.
4. Run `python3 generate_site_v5.py`, verify green ticks, verify only genuine source edits are in the diff (shuffles are seeded; large churn means something's wrong — investigate, don't commit).
5. Commit with SHA-referenced Linear comment. Mide reviews the live-candidate pages and pushes via GitHub Desktop.

### Definition of done (pilot)
- All Bonding pages render on the new template with mapped heroes, at Design's visual quality, zero runtime dependencies.
- Zero critical/major content defects remaining on Bonding pages per a re-run of the Phase 1 checks.
- Review list for Mide posted to Linear.
- A short PORTING.md noting any places where Design's spec couldn't be matched exactly and what was done instead — so Design can iterate rather than drift.
