// tools/mrb353_stub_model.ts — MRB-353 live proof, the deterministic stand-in
// for `checkWithModel` in supabase/functions/_shared/flashcards/model.ts.
//
// Neither TEST nor this machine has an ANTHROPIC_API_KEY, so the real Claude
// call cannot run. tools/mrb353_verdicts_live.py runs the COMMITTED
// flashcard-answer-check edge function body (index.ts, http.ts) for real,
// under Deno, against the real TEST database — and remaps ONLY the model
// call to this file with a Deno `--import-map` keyed on model.ts's absolute
// file:// URL. index.ts and http.ts are never edited.
//
// This file must export everything either of those two files imports from
// model.ts: `checkWithModel` (index.ts) and `type Usage` (http.ts). Nothing
// else from the real model.ts (EXTRACT_MODEL, extractWithModel, …) is
// imported by the answer-check function, so nothing else needs a stand-in.
//
// Verdict is decided by the pupil's answer text alone, deterministically —
// never by the question or the model answer — so the live proof can assert
// an exact verdict for an exact typed answer:
//   contains "half"   -> "partial"
//   contains "wrong"  -> "no"
//   contains "asdf"   -> "no"   (keyboard mash, fc_round3_pupil_live.py)
//   otherwise         -> "match"
//
// Every call is appended to MRB353_STUB_LOG (one JSON line per item, i.e.
// per question/pupil-answer pair), so the proof can show the model step ran
// — and, for a repeated exact answer, ran only ONCE, never a second time for
// text already stored in flashcard_answer_verdicts.

export type Usage = { model: string; input_tokens: number; output_tokens: number };
export type CheckItem = { question: string; model_answer: string; pupil_answer: string };

const LOG_PATH = Deno.env.get("MRB353_STUB_LOG");

function log(entry: Record<string, unknown>): void {
  if (!LOG_PATH) return;
  try {
    Deno.writeTextFileSync(
      LOG_PATH,
      JSON.stringify({ at: new Date().toISOString(), ...entry }) + "\n",
      { append: true, create: true },
    );
  } catch {
    // best-effort logging only; never fail the stand-in over it
  }
}

function verdictFor(answer: string): "match" | "partial" | "no" {
  const a = (answer ?? "").toLowerCase();
  if (a.includes("half")) return "partial";
  if (a.includes("wrong")) return "no";
  if (a.includes("asdf")) return "no";
  return "match";
}

export async function checkWithModel(items: CheckItem[], _apiKey: string):
    Promise<{ verdicts: (string | null)[]; usage: Usage }> {
  const verdicts = items.map((it) => {
    const v = verdictFor(it.pupil_answer);
    log({ question: it.question, model_answer: it.model_answer, pupil_answer: it.pupil_answer, verdict: v });
    return v;
  });
  return { verdicts, usage: { model: "stub", input_tokens: 0, output_tokens: 0 } };
}
