// MRB-351 — read any teacher file into STRUCTURED TEXT, or hand it on whole.
//
// Office files (pptx, docx, xlsx) are zip archives of XML and are read here,
// in order, keeping the structure a teacher's pairing depends on:
//   · pptx — slide by slide in presentation order; every text frame; tables
//            cell by cell; SPEAKER NOTES (answers often live there); runs in
//            red or another colour, and bold runs inside otherwise-plain
//            text, are MARKED, because "the answer is the red bit" is one of
//            the commonest shapes there is.
//   · docx — paragraphs and tables in document order; list numbering
//            re-created; page breaks and headings kept.
//   · xlsx — every sheet, row by row, cell by cell.
//   · csv / txt / md — as they are.
// PDFs and images are NOT read here: they go to the model whole, as a
// document or image block, which is the only way a scanned page or a
// photographed sheet can be read at all.
//
// Nothing here knows what a question is. It only makes sure the model (or
// the no-model rules in `pairs.ts`) sees the file the way a person would.

import { unzipSync, strFromU8 } from "npm:fflate@0.8.3";

export type Unit = {
  ref: string;            // "slide 7", "page 2", "sheet Waves", "table 1", "line 14"
  lines: string[];        // plain lines, markers included
  table?: string[][];     // when the unit IS a table: its cells
  notes?: string[];       // pptx speaker notes
};

export type Readable =
  | { kind: "text"; units: Unit[]; pages: number }
  | { kind: "pdf"; data: Uint8Array; pages: number }
  | { kind: "image"; data: Uint8Array; mediaType: string };

export class ReadError extends Error {
  constructor(public code: string, message?: string) { super(message ?? code); }
}

export const MAX_BYTES = 25 * 1024 * 1024;
export const MAX_PAGES = 60;

const EXT_KIND: Record<string, string> = {
  pptx: "pptx", docx: "docx", xlsx: "xlsx", csv: "csv", txt: "txt", md: "md",
  pdf: "pdf", png: "image", jpg: "image", jpeg: "image", webp: "image", heic: "heic",
};

export function extOf(name: string): string {
  const m = /\.([a-z0-9]+)$/i.exec(name || "");
  return m ? m[1].toLowerCase() : "";
}

export function readFile(name: string, bytes: Uint8Array): Readable {
  if (bytes.byteLength > MAX_BYTES) throw new ReadError("too_big");
  const kind = EXT_KIND[extOf(name)];
  if (!kind) throw new ReadError("unsupported_type");
  switch (kind) {
    case "pptx": return capPages(readPptx(bytes));
    case "docx": return readDocx(bytes);
    case "xlsx": return readXlsx(bytes);
    case "csv": {
      const table = parseCsv(decodeText(bytes));
      return { kind: "text", units: [{ ref: "sheet", lines: table.map((r) => "| " + r.join(" | ") + " |"), table }], pages: 1 };
    }
    case "txt":
    case "md": {
      const lines = decodeText(bytes).split(/\r?\n/);
      return { kind: "text", units: [{ ref: "text", lines }], pages: 1 };
    }
    case "pdf": {
      const pages = countPdfPages(bytes);
      if (pages > MAX_PAGES) throw new ReadError("too_many_pages");
      return { kind: "pdf", data: bytes, pages };
    }
    case "image": return { kind: "image", data: bytes, mediaType: sniffImage(bytes) };
    // A HEIC arrives here only if the browser could not convert it; the
    // model cannot read HEIC, so say so rather than send it.
    case "heic": throw new ReadError("heic_unconverted");
  }
  throw new ReadError("unsupported_type");
}

function capPages(r: Readable): Readable {
  if (r.kind === "text" && r.pages > MAX_PAGES) throw new ReadError("too_many_pages");
  return r;
}

export function decodeText(bytes: Uint8Array): string {
  // UTF-8 with BOM stripped; a Windows-1252 export (Excel's "CSV") falls back
  // byte-for-byte rather than filling the deck with replacement characters.
  let s = new TextDecoder("utf-8", { fatal: false }).decode(bytes);
  if (s.includes("\uFFFD")) s = new TextDecoder("windows-1252").decode(bytes);
  return s.replace(/^\uFEFF/, "");
}

// ── zip + xml helpers ──────────────────────────────────────────────────
function unzip(bytes: Uint8Array): Record<string, Uint8Array> {
  try { return unzipSync(bytes); } catch { throw new ReadError("unreadable_file"); }
}
function xmlOf(files: Record<string, Uint8Array>, path: string): string | null {
  const f = files[path];
  return f ? strFromU8(f) : null;
}
function unescapeXml(s: string): string {
  return s.replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"')
    .replace(/&apos;/g, "'").replace(/&#(\d+);/g, (_, d) => String.fromCodePoint(+d))
    .replace(/&#x([0-9a-f]+);/gi, (_, h) => String.fromCodePoint(parseInt(h, 16)))
    .replace(/&amp;/g, "&");
}
function relsOf(xml: string | null): Record<string, string> {
  const out: Record<string, string> = {};
  if (!xml) return out;
  for (const m of xml.matchAll(/<Relationship\b[^>]*>/g)) {
    const id = /\bId="([^"]+)"/.exec(m[0])?.[1];
    const t = /\bTarget="([^"]+)"/.exec(m[0])?.[1];
    if (id && t) out[id] = t;
  }
  return out;
}
function resolvePath(base: string, target: string): string {
  if (target.startsWith("/")) return target.slice(1);
  const parts = base.split("/").slice(0, -1);
  for (const seg of target.split("/")) {
    if (seg === "..") parts.pop(); else if (seg !== ".") parts.push(seg);
  }
  return parts.join("/");
}

// A colour that reads as "the answer colour": clearly red/orange/green/blue,
// not black, grey or white.
function colourName(hex: string | undefined): string | null {
  if (!hex || !/^[0-9a-f]{6}$/i.test(hex)) return null;
  const r = parseInt(hex.slice(0, 2), 16), g = parseInt(hex.slice(2, 4), 16), b = parseInt(hex.slice(4, 6), 16);
  const max = Math.max(r, g, b), min = Math.min(r, g, b);
  if (max - min < 60) return null;                 // grey, black, white
  if (r >= g && r >= b) return "red";
  if (g >= r && g >= b) return "green";
  return "blue";
}

type Run = { text: string; bold: boolean; colour: string | null };

// Join runs into one line, marking coloured runs and — only where the line
// is not bold throughout — bold runs.
function markRuns(runs: Run[]): string {
  const merged: Run[] = [];
  for (const r of runs) {
    const last = merged[merged.length - 1];
    if (last && last.bold === r.bold && last.colour === r.colour) last.text += r.text;
    else merged.push({ ...r });
  }
  const visible = merged.filter((r) => r.text.trim());
  const allBold = visible.length > 0 && visible.every((r) => r.bold);
  return merged.map((r) => {
    if (!r.text.trim()) return r.text;
    let t = r.text;
    if (r.colour) t = `[${r.colour}]${t.trim()}[/${r.colour}]` + (/\s$/.test(r.text) ? " " : "");
    else if (r.bold && !allBold) t = `**${t.trim()}**` + (/\s$/.test(r.text) ? " " : "");
    return t;
  }).join("").replace(/[ \t]+/g, " ").trim();
}

// ── pptx ───────────────────────────────────────────────────────────────
function drawingParagraphs(xml: string): string[] {
  const out: string[] = [];
  for (const p of xml.matchAll(/<a:p\b[^>]*>([\s\S]*?)<\/a:p>/g)) {
    const runs: Run[] = [];
    for (const r of p[1].matchAll(/<a:(r|fld)\b[^>]*>([\s\S]*?)<\/a:\1>|<a:br\b[^>]*\/>/g)) {
      if (r[0].startsWith("<a:br")) { runs.push({ text: " ", bold: false, colour: null }); continue; }
      const rPr = /<a:rPr\b([^>]*)(?:\/>|>([\s\S]*?)<\/a:rPr>)/.exec(r[2]);
      const bold = !!rPr && /\bb="1"/.test(rPr[1]);
      const colour = rPr?.[2] ? colourName(/<a:srgbClr val="([0-9A-Fa-f]{6})"/.exec(rPr[2])?.[1]) : null;
      const t = [...r[2].matchAll(/<a:t>([\s\S]*?)<\/a:t>|<a:t\/>/g)].map((m) => unescapeXml(m[1] ?? "")).join("");
      runs.push({ text: t, bold, colour });
    }
    const line = markRuns(runs);
    if (line) out.push(line);
  }
  return out;
}

function readPptx(bytes: Uint8Array): Readable {
  const files = unzip(bytes);
  const pres = xmlOf(files, "ppt/presentation.xml");
  if (!pres) throw new ReadError("unreadable_file");
  const rels = relsOf(xmlOf(files, "ppt/_rels/presentation.xml.rels"));
  const order = [...pres.matchAll(/<p:sldId\b[^>]*r:id="([^"]+)"/g)].map((m) => rels[m[1]]).filter(Boolean);
  const units: Unit[] = [];
  order.forEach((target, i) => {
    const path = resolvePath("ppt/presentation.xml", target);
    const xml = xmlOf(files, path);
    if (!xml) return;
    const unit: Unit = { ref: `slide ${i + 1}`, lines: [] };
    // Shapes and graphic frames in document order; a table becomes its own
    // block of `| a | b |` lines AND is kept as cells.
    const blocks = xml.matchAll(/<p:sp\b[\s\S]*?<\/p:sp>|<p:graphicFrame\b[\s\S]*?<\/p:graphicFrame>/g);
    for (const b of blocks) {
      if (b[0].startsWith("<p:graphicFrame")) {
        const rows: string[][] = [];
        for (const tr of b[0].matchAll(/<a:tr\b[^>]*>([\s\S]*?)<\/a:tr>/g)) {
          const cells = [...tr[1].matchAll(/<a:tc\b[^>]*>([\s\S]*?)<\/a:tc>/g)]
            .map((tc) => drawingParagraphs(tc[1]).join(" "));
          rows.push(cells);
        }
        if (rows.length) {
          unit.table = (unit.table ?? []).concat(rows);
          for (const r of rows) unit.lines.push("| " + r.join(" | ") + " |");
        }
      } else {
        // Slide numbers, dates and footers are furniture, not content.
        if (/<p:ph\b[^>]*type="(sldNum|dt|ftr)"/.test(b[0])) continue;
        unit.lines.push(...drawingParagraphs(b[0]));
      }
    }
    const srels = relsOf(xmlOf(files, path.replace(/slides\/(slide\d+\.xml)$/, "slides/_rels/$1.rels")));
    const notesTarget = Object.values(srels).find((t) => /notesSlide/.test(t));
    if (notesTarget) {
      const nxml = xmlOf(files, resolvePath(path, notesTarget));
      if (nxml) {
        const notes: string[] = [];
        for (const sp of nxml.matchAll(/<p:sp\b[\s\S]*?<\/p:sp>/g)) {
          if (/<p:ph\b[^>]*type="(sldImg|sldNum|hdr|ftr|dt)"/.test(sp[0])) continue;
          notes.push(...drawingParagraphs(sp[0]));
        }
        if (notes.length) unit.notes = notes;
      }
    }
    units.push(unit);
  });
  return { kind: "text", units, pages: order.length };
}

// ── docx ───────────────────────────────────────────────────────────────
function wordRuns(pXml: string): Run[] {
  const runs: Run[] = [];
  for (const r of pXml.matchAll(/<w:r\b[^>]*>([\s\S]*?)<\/w:r>/g)) {
    const rPr = /<w:rPr>([\s\S]*?)<\/w:rPr>/.exec(r[1])?.[1] ?? "";
    const bold = /<w:b\/>|<w:b w:val="(1|true|on)"\/>/.test(rPr);
    const colour = colourName(/<w:color w:val="([0-9A-Fa-f]{6})"/.exec(rPr)?.[1]) ??
      (/<w:highlight w:val="(yellow|green|cyan)"/.test(rPr) ? "highlight" : null);
    let text = "";
    for (const t of r[1].matchAll(/<w:t(?:\s[^>]*)?>([\s\S]*?)<\/w:t>|<w:tab\/>|<w:br\b[^>]*\/>/g)) {
      text += t[0].startsWith("<w:t") ? unescapeXml(t[1] ?? "") : " ";
    }
    runs.push({ text, bold, colour });
  }
  return runs;
}

function readDocx(bytes: Uint8Array): Readable {
  const files = unzip(bytes);
  const doc = xmlOf(files, "word/document.xml");
  if (!doc) throw new ReadError("unreadable_file");
  const body = /<w:body>([\s\S]*)<\/w:body>/.exec(doc)?.[1] ?? "";
  const units: Unit[] = [];
  let page = 1;
  let cur: Unit = { ref: "page 1", lines: [] };
  const counters: Record<string, number> = {};
  let tableN = 0;
  // Top-level body children in order: paragraphs and tables.
  for (const m of body.matchAll(/<w:tbl>[\s\S]*?<\/w:tbl>|<w:p\b[\s\S]*?<\/w:p>|<w:p\b[^>]*\/>/g)) {
    const x = m[0];
    if (x.startsWith("<w:tbl>")) {
      tableN++;
      const rows: string[][] = [];
      for (const tr of x.matchAll(/<w:tr\b[^>]*>([\s\S]*?)<\/w:tr>/g)) {
        rows.push([...tr[1].matchAll(/<w:tc\b[^>]*>([\s\S]*?)<\/w:tc>/g)].map((tc) =>
          [...tc[1].matchAll(/<w:p\b[\s\S]*?<\/w:p>/g)].map((p) => markRuns(wordRuns(p[0]))).filter(Boolean).join(" ")));
      }
      units.push(cur);
      units.push({ ref: `table ${tableN}`, lines: rows.map((r) => "| " + r.join(" | ") + " |"), table: rows });
      cur = { ref: `page ${page}`, lines: [] };
      continue;
    }
    const style = /<w:pStyle w:val="([^"]+)"/.exec(x)?.[1] ?? "";
    const num = /<w:numPr>[\s\S]*?<w:ilvl w:val="(\d+)"\/>[\s\S]*?<w:numId w:val="(\d+)"\/>/.exec(x);
    let line = markRuns(wordRuns(x));
    if (num && line) {
      const key = num[2] + ":" + num[1];
      counters[key] = (counters[key] ?? 0) + 1;
      line = `${counters[key]}. ${line}`;
    }
    if (/^Heading|^Title/i.test(style) && line) line = "# " + line;
    if (line) cur.lines.push(line);
    if (/<w:br w:type="page"\/>|<w:lastRenderedPageBreak\/>/.test(x)) {
      units.push(cur);
      page++;
      cur = { ref: `page ${page}`, lines: [] };
    }
  }
  units.push(cur);
  return { kind: "text", units: units.filter((u) => u.lines.length), pages: page };
}

// ── xlsx ───────────────────────────────────────────────────────────────
function colIndex(ref: string): number {
  const letters = /^[A-Z]+/.exec(ref)?.[0] ?? "A";
  let n = 0;
  for (const ch of letters) n = n * 26 + (ch.charCodeAt(0) - 64);
  return n - 1;
}

function readXlsx(bytes: Uint8Array): Readable {
  const files = unzip(bytes);
  const wb = xmlOf(files, "xl/workbook.xml");
  if (!wb) throw new ReadError("unreadable_file");
  const rels = relsOf(xmlOf(files, "xl/_rels/workbook.xml.rels"));
  const sst: string[] = [];
  const sxml = xmlOf(files, "xl/sharedStrings.xml");
  if (sxml) {
    for (const si of sxml.matchAll(/<si>([\s\S]*?)<\/si>/g)) {
      sst.push([...si[1].matchAll(/<t(?:\s[^>]*)?>([\s\S]*?)<\/t>/g)].map((t) => unescapeXml(t[1])).join(""));
    }
  }
  const units: Unit[] = [];
  for (const s of wb.matchAll(/<sheet\b[^>]*>/g)) {
    const name = unescapeXml(/\bname="([^"]*)"/.exec(s[0])?.[1] ?? "Sheet");
    const rid = /r:id="([^"]+)"/.exec(s[0])?.[1];
    const xml = rid ? xmlOf(files, resolvePath("xl/workbook.xml", rels[rid] ?? "")) : null;
    if (!xml) continue;
    const rows: string[][] = [];
    for (const row of xml.matchAll(/<row\b[^>]*>([\s\S]*?)<\/row>/g)) {
      const cells: string[] = [];
      for (const c of row[1].matchAll(/<c\b([^>]*)(?:\/>|>([\s\S]*?)<\/c>)/g)) {
        const ref = /\br="([A-Z]+\d+)"/.exec(c[1])?.[1] ?? "A1";
        const t = /\bt="(\w+)"/.exec(c[1])?.[1];
        const inner = c[2] ?? "";
        let v = "";
        if (t === "s") v = sst[+(/<v>([\s\S]*?)<\/v>/.exec(inner)?.[1] ?? -1)] ?? "";
        else if (t === "inlineStr") v = [...inner.matchAll(/<t(?:\s[^>]*)?>([\s\S]*?)<\/t>/g)].map((x) => unescapeXml(x[1])).join("");
        else v = unescapeXml(/<v>([\s\S]*?)<\/v>/.exec(inner)?.[1] ?? "");
        cells[colIndex(ref)] = v.trim();
      }
      rows.push(Array.from(cells, (x) => x ?? ""));
    }
    if (rows.some((r) => r.some(Boolean))) {
      units.push({ ref: `sheet ${name}`, lines: rows.map((r) => "| " + r.join(" | ") + " |"), table: rows });
    }
  }
  return { kind: "text", units, pages: units.length };
}

// ── csv ────────────────────────────────────────────────────────────────
export function parseCsv(text: string): string[][] {
  const delim = (text.split("\n", 1)[0].match(/;/g)?.length ?? 0) >
    (text.split("\n", 1)[0].match(/,/g)?.length ?? 0) ? ";" : (text.includes("\t") && !text.includes(",") ? "\t" : ",");
  const rows: string[][] = [];
  let row: string[] = [], cell = "", q = false;
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (q) {
      if (ch === '"' && text[i + 1] === '"') { cell += '"'; i++; }
      else if (ch === '"') q = false;
      else cell += ch;
    } else if (ch === '"' && !cell) q = true;
    else if (ch === delim) { row.push(cell.trim()); cell = ""; }
    else if (ch === "\n" || ch === "\r") {
      if (ch === "\r" && text[i + 1] === "\n") i++;
      row.push(cell.trim()); cell = "";
      if (row.some(Boolean)) rows.push(row);
      row = [];
    } else cell += ch;
  }
  row.push(cell.trim());
  if (row.some(Boolean)) rows.push(row);
  return rows;
}

// ── pdf / image ────────────────────────────────────────────────────────
function countPdfPages(bytes: Uint8Array): number {
  const s = new TextDecoder("latin1").decode(bytes);
  const n = (s.match(/\/Type\s*\/Page(?![s\w])/g) ?? []).length;
  return Math.max(1, n);
}

function sniffImage(b: Uint8Array): string {
  if (b[0] === 0x89 && b[1] === 0x50) return "image/png";
  if (b[0] === 0xff && b[1] === 0xd8) return "image/jpeg";
  if (b[0] === 0x52 && b[1] === 0x49 && b[8] === 0x57) return "image/webp";
  throw new ReadError("unsupported_type");
}

// The text the model (and the no-model rules) see.
export function render(units: Unit[]): string {
  return units.map((u) => {
    const head = `=== ${u.ref} ===`;
    const body = u.lines.join("\n");
    const notes = u.notes?.length ? `\n[speaker notes]\n${u.notes.join("\n")}` : "";
    return `${head}\n${body}${notes}`;
  }).join("\n\n");
}
