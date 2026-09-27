// MRB-351 — how a fixture's extraction is scored against expected.json.
//
// A produced card RECOVERS an expected pair when both sides carry the
// expected content: every expected token (bar a little slack for long
// sides) appears in the produced side, and the produced side is not so much
// longer that it could be swallowing a neighbour. A keyword card may come
// back as "Conductor" or as "What is a conductor?" — both recover it. A
// questions-only pair is recovered by a card with that question and an EMPTY
// answer: an invented answer is a failure, not a bonus.
//
// Each produced card can recover at most one expected pair.

export type Expected = {
  shape: string;
  pairs: { q: string; a: string | null }[];
  answers_missing: boolean;
  forbidden: string[];
};
export type Produced = { question: string; answer: string };

const STOP = new Set(["the", "a", "an", "of", "is", "are", "what", "which", "to", "in", "and", "it", "its", "by", "for", "on", "as", "at", "be", "does", "do", "how", "that"]);

export function tokens(s: string): string[] {
  return (s || "").toLowerCase()
    .replace(/[×÷=+→]/g, " ").replace(/_{2,}/g, " ")
    .replace(/[^a-z0-9 ]+/g, " ").split(/\s+/).filter((t) => t && !STOP.has(t));
}

function covers(expected: string, produced: string): boolean {
  const e = tokens(expected), p = tokens(produced);
  if (e.length === 0) return p.length === 0;
  const ps = new Set(p);
  const hit = e.filter((t) => ps.has(t)).length;
  const need = e.length <= 3 ? e.length : Math.ceil(e.length * 0.8);
  return hit >= need && p.length <= e.length * 3 + 6;
}

export function scoreFixture(exp: Expected, got: Produced[]) {
  const used = new Set<number>();
  let recovered = 0;
  const misses: string[] = [];
  for (const pair of exp.pairs) {
    const i = got.findIndex((g, k) => !used.has(k) && covers(pair.q, g.question) &&
      (pair.a === null ? !g.answer.trim() : covers(pair.a, g.answer)));
    if (i >= 0) { used.add(i); recovered++; } else misses.push(pair.q);
  }
  const text = got.map((g) => g.question + " " + g.answer).join(" ").toLowerCase();
  const leaked = exp.forbidden.filter((n) => text.includes(n.toLowerCase()) ||
    text.includes(n.split(" ")[1]?.toLowerCase() ?? "\u0000"));
  return { expected: exp.pairs.length, recovered, extra: got.length - used.size, misses, leaked };
}
