// MRB-351 — the two shapes that need no model at all, and the card type.
//
// A spreadsheet or table whose rows are (question, answer), and a text of
// "Q: … / A: …" lines, are already pairs: sending them to a model would
// spend money to get back what we sent, with a small chance of it being
// changed on the way. So these two shapes are paired here, exactly, and the
// file never leaves the server. Anything less clean than that — a table
// with prose round it that might be an answer key, a three-column grid, a
// half-and-half document — is NOT guessed at: it goes to the model.

import type { Unit } from "./read_file.ts";

export type Card = {
  question: string;
  answer: string;
  source_ref: string | null;
  confidence: number;     // 0..1; the review table sorts low ones to the top
  flagged: boolean;       // missing answer or low confidence
};

export type Extraction = {
  cards: Card[];
  unpaired_questions: { question: string; source_ref: string | null }[];
  unpaired_answers: { answer: string; source_ref: string | null }[];
  method: "table" | "lines" | "model";
};

const HEADER = /^(q|a|no\.?|#|questions?|answers?|keywords?|key\s*words?|terms?|words?|definitions?|meanings?|prompts?|responses?|front|back|side\s*[12])$/i;

const clean = (s: string) =>
  s.replace(/\[\/?(red|green|blue|highlight)\]/g, "").replace(/\*\*/g, "")
   .replace(/^\s*(?:\d+[.)]|[a-z][.)]|[-•*])\s+/i, "").replace(/\s+/g, " ").trim();

function visibleChars(units: Unit[]): number {
  let n = 0;
  for (const u of units) {
    for (const l of u.lines) if (!/^#/.test(l)) n += clean(l.replace(/\|/g, " ")).length;
    for (const l of u.notes ?? []) n += clean(l).length;
  }
  return n;
}

// ── tables ─────────────────────────────────────────────────────────────
// Every table row across the file with exactly two non-empty cells, header
// rows dropped. Taken only when such rows are at least three, carry at least
// 85% of all the text in the file, and no row is ragged (1 or 3+ cells) —
// a single stray row of a third shape means a teacher's layout this rule
// does not understand, and the model should look.
export function tablePairs(units: Unit[]): Extraction | null {
  const rows: { q: string; a: string; ref: string }[] = [];
  let ragged = 0, tableChars = 0;
  for (const u of units) {
    if (!u.table) continue;
    for (const r of u.table) {
      const cells = r.map(clean).filter(Boolean);
      tableChars += cells.join(" ").length;
      if (cells.length === 0) continue;
      if (cells.length !== 2) { ragged++; continue; }
      if (HEADER.test(cells[0]) && HEADER.test(cells[1])) continue;
      rows.push({ q: cells[0], a: cells[1], ref: u.ref });
    }
  }
  if (rows.length < 3 || ragged > 0) return null;
  const total = visibleChars(units);
  if (total === 0 || tableChars / total < 0.85) return null;
  return {
    method: "table",
    cards: rows.map((r) => ({
      question: r.q.slice(0, 400), answer: r.a.slice(0, 600),
      source_ref: r.ref.startsWith("sheet") ? null : r.ref, confidence: 1, flagged: false,
    })),
    unpaired_questions: [],
    unpaired_answers: [],
  };
}

// ── Q:/A: lines ───────────────────────────────────────────────────────
const QLINE = /^\s*(?:\d+[.)]\s*)?(?:q|question)\s*\d*\s*[:.)-]\s*(.+)$/i;
const ALINE = /^\s*(?:a|ans|answer)\s*\d*\s*[:.)-]\s*(.+)$/i;

export function linePairs(units: Unit[]): Extraction | null {
  if (units.some((u) => u.table)) return null;
  const out: { q: string; a: string; ref: string }[] = [];
  let pending: { q: string; ref: string } | null = null;
  let last: "q" | "a" | null = null;
  let stray = 0, used = 0;
  for (const u of units) {
    for (const raw of u.lines) {
      const line = raw.trim();
      if (!line || /^#/.test(line) || /^===/.test(line)) { last = null; continue; }
      const q = QLINE.exec(line), a = ALINE.exec(line);
      if (q) {
        if (pending) return null;                      // two questions running: not this shape
        pending = { q: clean(q[1]), ref: u.ref }; last = "q"; used += line.length;
      } else if (a) {
        if (!pending) return null;                     // an answer with no question
        out.push({ q: pending.q, a: clean(a[1]), ref: pending.ref });
        pending = null; last = "a"; used += line.length;
      } else if (last === "q" && pending) {
        pending.q += " " + clean(line); used += line.length;   // a wrapped question
      } else if (last === "a" && out.length) {
        out[out.length - 1].a += " " + clean(line); used += line.length;
      } else {
        stray += line.length;
      }
    }
  }
  if (pending || out.length < 3) return null;
  if (used / Math.max(1, used + stray) < 0.85) return null;
  return {
    method: "lines",
    cards: out.map((r) => ({
      question: r.q.slice(0, 400), answer: r.a.slice(0, 600),
      source_ref: r.ref === "text" ? null : r.ref, confidence: 1, flagged: false,
    })),
    unpaired_questions: [],
    unpaired_answers: [],
  };
}

// Normalise whatever came back (from either path) into the deck's rows:
// unpaired questions become cards with an EMPTY answer, flagged, so the
// review table shows them and "Save deck" stays disabled until they are
// answered or deleted.
export function toDeckRows(x: Extraction): Card[] {
  const rows = x.cards
    .map((c) => ({
      question: (c.question ?? "").trim().slice(0, 400),
      answer: (c.answer ?? "").trim().slice(0, 600),
      source_ref: c.source_ref ? String(c.source_ref).slice(0, 40) : null,
      confidence: Math.max(0, Math.min(1, Number.isFinite(c.confidence) ? c.confidence : 0.5)),
      flagged: false,
    }))
    .filter((c) => c.question || c.answer);
  for (const u of x.unpaired_questions ?? []) {
    const q = (u.question ?? "").trim();
    if (q) rows.push({ question: q.slice(0, 400), answer: "", source_ref: u.source_ref ?? null, confidence: 0, flagged: true });
  }
  // An answer the model could not place still belongs in front of the
  // teacher, at the top, with its question blank — never silently dropped.
  for (const u of x.unpaired_answers ?? []) {
    const a = (u.answer ?? "").trim();
    if (a) rows.push({ question: "", answer: a.slice(0, 600), source_ref: u.source_ref ?? null, confidence: 0, flagged: true });
  }
  for (const r of rows) r.flagged = !r.question || !r.answer || r.confidence < 0.6;
  return rows;
}
