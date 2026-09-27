// MRB-351 — file in, deck rows out. The same function the edge function
// runs and the fixture tests run, so the score in CI is the score in use.

import { readFile, type Readable } from "./read_file.ts";
import { linePairs, tablePairs, toDeckRows, type Card, type Extraction } from "./pairs.ts";
import { extractWithModel, type Usage } from "./model.ts";
import { redactUnits } from "./redact.ts";

export type PipelineResult = {
  rows: Card[];
  method: Extraction["method"];
  usage: Usage | null;
  pages: number;
};

// `opts.model` lets a test swap the network call for a recorded reply.
export async function extract(
  fileName: string,
  bytes: Uint8Array,
  opts: { apiKey?: string; model?: (r: Readable, name: string) => Promise<{ result: Extraction; usage: Usage }> } = {},
): Promise<PipelineResult> {
  const r = readFile(fileName, bytes);
  if (r.kind === "text") {
    const exact = tablePairs(r.units) ?? linePairs(r.units);
    if (exact) return { rows: toDeckRows(exact), method: exact.method, usage: null, pages: r.pages };
  }
  const call = opts.model ?? ((rr: Readable, n: string) => {
    if (!opts.apiKey) throw new Error("no_api_key");
    return extractWithModel(rr, n, opts.apiKey);
  });
  // MRB-351 landing — a conservative, mechanical redaction pass runs on TEXT
  // content only, right before the one place it can reach a model. See
  // redact.ts for what it removes and why. PDFs and images pass through
  // unchanged — see the module docstring there.
  const forModel: Readable = r.kind === "text" ? { ...r, units: redactUnits(r.units) } : r;
  const { result, usage } = await call(forModel, fileName);
  return { rows: toDeckRows(result), method: "model", usage, pages: r.kind === "image" ? 1 : r.pages };
}

// A paste box is a .txt file with no name.
export function pasteBytes(text: string): Uint8Array {
  return new TextEncoder().encode(text);
}
