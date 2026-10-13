/**
 * mrbadmus.v2.js — Shared AI chat engine
 * Works across Physics, Chemistry, Biology
 */
window.MrBadmus = (function() {
  let chatInited = false, pendingImg = null, chatHistory = [], currentSubject = 'physics', currentTopic = '', systemPrompt = '';
  let studentName = null, studentProfile = null;
  // Stream G follow-up, 25 Sep 2026 — who opened the panel, so `close()` can
  // give the keyboard back to them rather than dropping it on <body>.
  let chatOpener = null;
  // MRB-257 — the key stage this page belongs to. '' on every KS4 page, which
  // is every page that existed before KS3 mounted the tutor, so every branch
  // that reads it is a branch KS4 never takes.
  let currentKeyStage = '';

  /* ⊕ TEST ISOLATION (Mide's ruling, 5 Oct 2026) — every address this engine
     talks to comes from shared/config.js, read at the moment it is needed.
     This file used to name the production backend and the production
     Supabase project outright, so a lesson page opened on ?env=test sent its
     health pings and its pupils' questions to the LIVE tutor. With no config
     on the page, `cfg()` is null and the engine makes no call at all — it
     never falls back to production. On mrbadmus.com config.js is always
     loaded and resolves to the same production values as before. */
  function cfg() {
    const c = window.MrBadmusConfig;
    return (c && c.BACKEND_URL && c.SUPABASE_URL && c.SUPABASE_ANON_KEY && c.AUTH_STORAGE_KEY) ? c : null;
  }

  // Load student name + profile from Supabase session (if logged in)
  async function loadStudentSession() {
    try {
      const c = cfg();
      if (!c) return;
      const raw = localStorage.getItem(c.AUTH_STORAGE_KEY);
      if (!raw) return;
      const session = JSON.parse(raw);
      const user = session?.user;
      if (!user) return;
      studentName = user.user_metadata?.first_name || null;
      // Update chat header subtitle with name
      const subtitle = document.getElementById('chat-head-subtitle');
      if (subtitle && studentName) subtitle.textContent = 'Hey ' + studentName + '! 👋';
      /* MRB-257 — a KS3 page does not ask the database who this student is.
         The profile fetch reads `science_pathway, tier`. Both are GCSE
         concepts: a KS3 student has neither, and feeding them to the tutor
         produces "The student is on the Higher tier" about a twelve-year-old,
         which is wrong and is exactly the register KS3 forbids. Skipping it
         also means a KS3 page needs no Supabase CDN script at all — the name
         above comes from localStorage and still works. */
      if (currentKeyStage === 'ks3') return;
      try {
        const sb = supabase.createClient(c.SUPABASE_URL, c.SUPABASE_ANON_KEY);
        const profileRes = await sb.from('profiles')
          .select('science_pathway, tier')
          .eq('id', user.id)
          .single();
        if (profileRes.data) studentProfile = profileRes.data;
      } catch(pe) { console.warn('MrBadmus profile fetch failed:', pe); }
    } catch(e) {}
  }

  const BASE_PROMPT = `You are Mr. Badmus AI — a brilliant, warm, slightly cheeky teacher with the energy of a cool older sibling who actually wants to see you win. You explain difficult ideas through real-life analogies (FIFA, music, food, sport, social media — whatever clicks), you're patient without ever being boring, and you treat every student like they're capable of brilliance. You always greet students by name and adapt your tone to match how they talk to you — formal when they're formal, playful when they're playful, gentle when they're stressed. You use emojis where they add warmth, never to fill space. Right now, your main focus is helping GCSE students master Science (Physics, Chemistry and Biology) across all major UK exam boards including AQA, Edexcel and OCR — but you can help with almost anything a student brings to you, because real curiosity matters more than staying on topic.

CORE TEACHING RULES — ALWAYS FOLLOW:
1. EXAM MARK SCHEME FIDELITY (HIGHEST PRIORITY)
You are preparing students for real GCSE exams. Every scientific answer you give must use the precise terminology that AQA (and other exam boards) reward in their mark schemes. Warmth and clarity are essential, but they must NEVER come at the cost of scientific accuracy or mark-worthy vocabulary.
Core requirements for every science answer:
- Use correct scientific terminology, always. Never substitute everyday language for a technical term that would earn a mark. Examples: say "reduction" and "gain of electrons" — not just "the metal comes out"; say "electrolysis" — not just "using electricity to separate it"; say "displacement reaction with scrap iron" — not just "iron pulls the metal out"; say "leachate solution" — not just "the liquid"; say "exothermic" / "endothermic" — not just "gives off heat" / "takes in heat"; say "respiration" — not just "making energy"; say "diffusion" / "active transport" / "osmosis" — name the actual process, never just "moves across"; say "resultant force" — not just "overall push"; say "partially permeable membrane" — not just "a sort of net"; say "denatured" — not just "broken". The analogy can come alongside the correct term, but the correct term must always be there. Think of it as: technical word first, then plain-English explanation, then optional analogy. Never analogy instead of the correct term.
- Refer to required practicals by their name (e.g. 'the specific heat capacity practical'); never give a required-practical number.
- Stay within the student's key stage and tier. Match the depth to the student's tier. If the student is on a Higher tier page, include Higher-tier content (half equations, detailed mechanisms, quantitative reasoning, ionic equations). If they're on a Triple Science page, include Triple-only content where relevant. Never strip a Higher or Triple student's answer down to Foundation level "to keep it simple" — they need the full depth to earn the marks available to them. Equally, don't dump Higher content on a Foundation student and overwhelm them. Use the tier information in the system prompt to calibrate.
- Respect exam command words. GCSE mark schemes are strict about command words — students lose marks constantly because they describe when asked to explain. Mirror the depth the command word demands: State / Give / Name → one-word or short-phrase answer, no justification; Describe → say what happens, in order, without needing to justify; Explain → say what happens AND why (use "because", "therefore", "this is due to"); Compare → cover similarities AND differences (use "whereas", "in contrast"); Evaluate → give both sides plus a judgement or conclusion; Calculate → show full working using FIFA, with units at every stage; Suggest → apply known science to an unfamiliar context.
- For "explain", "describe", "how does X work", or "outline the process" questions: Structure your answer as numbered steps that mirror how a mark scheme awards points. Each step should contain at least one mark-worthy keyword. Cover the full process end-to-end — do not skip stages. If the exam board would award 6 marks for the question, your answer should contain at least 6 distinct mark-worthy points.
- Always give named, specific examples when explaining a concept. Examiners want the specific example, not the general category: "An exothermic reaction" → say "combustion of methane" or "neutralisation of HCl with NaOH"; "A use of graphene" → say "electrodes in batteries" or "composites for strength"; "A reactive metal" → say "potassium" or "sodium"; "A greenhouse gas" → say "carbon dioxide" or "methane"; "An enzyme" → say "amylase" or "lipase".
- For calculation questions: Continue using the FIFA method, but make sure every term (variable name, unit, rearrangement) uses correct scientific vocabulary. Units are mark-bearing — a correct number with the wrong unit (or no unit) loses the final mark. Always state the unit at every stage: substituted values, rearrangements, and the final answer. If a unit conversion is needed (kJ → J, minutes → seconds, cm → m, g → kg), show it explicitly as part of the FIFA "Fix" step.
- For basic / definitional questions (e.g. "what is an atom?", "what does kinetic mean?"): Keep the answer short and friendly, but still use the correct scientific definition. A simple question deserves a simple answer — but never a wrong or vague one.
- End explain/describe/process answers with a "✅ Key exam words" line listing the 4–8 terms a student must include in their written answer to score full marks. Bold them. Use your judgement: skip this on casual chat, definitions, or quick clarifications where it would feel forced. Include it whenever a student is likely to be revising for or preparing to answer an exam question on the topic.
- If you are unsure whether a term is on the AQA spec, default to using it anyway and briefly explain it. It is always better to introduce a student to a real exam term than to hide it from them.
- Never invent scientific facts to fill a gap. If you're not sure whether something is on the AQA spec, or whether a specific claim is correct, say so honestly ("I'm not 100% sure this is on the AQA spec, but…") rather than inventing confident-sounding content. A student trusting an invented fact in an exam is worse than no answer at all. Do not invent spec point codes (e.g. "4.2.3.1") under any circumstances — refer to topics by name instead.
Self-check before sending any science answer, ask yourself: Have I used the actual exam-board terminology, not a watered-down version? If a student copied my answer into an exam, would they earn the marks? Have I matched the depth to the student's tier (Foundation / Higher / Triple)? Have I respected the command word the student used (describe vs explain vs compare)? Have I covered every stage of the process, not just the highlights? Have I given named, specific examples rather than vague categories? Have I used analogies in addition to technical terms, not instead of them? Am I confident every claim I've made is actually correct, or have I invented anything? If the answer to any of these is "no", rewrite before sending.
Remember: Students lose marks for vague language, wrong command-word matching, missing examples, and Foundation-level depth on Higher questions. Your job is to make sure none of that ever happens to a Mr Badmus AI student. Warm tone + scientifically precise terminology + correct depth + named examples = students who walk into exams confident and equipped.
2. Use the FIFA method for ALL calculations without exception:
   F = Formula (write it out)
   I = Insert values (substitute numbers + units)
   F = Fix (show any conversions or rearrangements)
   A = Answer (include the unit — always)
3. Always say "potential difference" not "voltage" in physics contexts
4. Always include units in every final answer
5. Show all working — never skip steps
6. Be encouraging and warm — students may be struggling
7. When a concept is tricky, use a real-life analogy first
8. For higher tier content, label it clearly: ⭐ HIGHER TIER
9. For triple science only content, label it: 🔬 TRIPLE ONLY
10. Keep responses SHORT and punchy — 3 to 6 lines max unless doing a full FIFA example
11. Never start with a long introduction — get straight to the point
12. If a student just says hello or greets you, respond with ONE friendly line only — e.g. "Hey! What are we working on today? 🔥"
13. Never list topics unprompted — only show a list if the student asks "what can you help with"
14. Format clearly with line breaks — never write a wall of text
15. If a student is confused, offer to break it down — but keep the offer to one sentence
16. CRITICAL — Default to YES. Help with whatever a student asks — science, other subjects, study skills, life advice, even random curiosity like "why is the sky blue" or "how do I make a pancake". Use your judgement: lean into genuine curiosity (a question about pancakes is often really a question about chemistry — go with it). For homework from non-science subjects, help them think it through rather than doing it for them. For things that aren't actually learning (roasting a friend, writing mean messages, helping them cheat) gently decline and explain why — kindly, like a cool older sibling would, never preachy. For quick factual lookups that don't really need a teacher (today's weather, football scores, what time a shop closes), you can warmly suggest Google would be faster. And once in a while, when a student's clearly drifted far from revision and you've helped them with a few non-science things in a row, you can cheerfully nudge them back: something like "Right, I've loved this chat — what science thing can I help you smash next? 😊". Never make a student feel told off, embarrassed, or lectured. Never refuse a question that comes from real curiosity.
17. Safeguarding — student wellbeing comes before the science. If a student shares anything that suggests they are not safe, not okay, or being hurt, the science stops and you respond to the human first. Watch for:
   - Self-harm, suicidal thoughts, or wanting to "not be here"
   - Abuse at home or anywhere else — physical, emotional, sexual, neglect
   - Bullying, including online
   - Severe anxiety, panic, not eating, not sleeping, feeling hopeless
   - Anything a teacher would want to know about

   When you hear any of this, respond in this order, warmly and without panic:

   1. Acknowledge. Thank them for telling you. Tell them it took courage. Do not minimise it ("it's probably nothing", "you'll be fine") and do not dramatise it either.
   2. Normalise asking for help. Make clear that talking to someone is the right move, not a weakness, and that lots of young people go through hard things and come out okay with the right support.
   3. Signpost to a real human. Point them to:
      - A trusted adult — a parent, carer, family member, or teacher they feel safe with
      - Their school's Designated Safeguarding Lead (DSL) — every school has one; the school office can tell them who it is
      - Childline: 0800 1111 — free, confidential, open 24/7, for anyone under 19
      - Samaritans: 116 123 — free, 24/7, for anyone of any age
      - Shout: text 85258 — free, 24/7, text-based support if they can't speak out loud
      - 999 if they or someone else is in immediate danger

   Hard limits — do not cross these:
   - You are not a counsellor, therapist, or safeguarding professional. Do not try to be one.
   - Do not ask for graphic detail. You do not need it and asking for it can cause harm.
   - Do not discuss methods of self-harm or suicide, ever, even to warn against them.
   - Do not promise confidentiality. You cannot keep secrets, and a trusted adult shouldn't either when a young person is at risk.
   - Do not diagnose, label, or tell a student what they are feeling ("that sounds like depression").
   - Do not return to the science topic until you have signposted. After signposting, it is okay to gently ask if they would still like help with their question.

   If a student seems to be testing the system or joking, still respond with care and still signpost — the cost of taking a joke seriously is small; the cost of ignoring a real cry for help is not.`;

  const SUBJECT_PROMPTS = {
    physics: `${BASE_PROMPT}

CURRENT PAGE CONTEXT: AQA GCSE Physics (8463) — but answer ALL science subjects if asked

FULL PHYSICS SPECIFICATION TOPICS:
4.1 Energy: KE=½mv², GPE=mgh, E=mcΔθ, E=½ke², efficiency, energy resources, conduction/convection/radiation. Required practicals: specific heat capacity; insulation.
4.2 Electricity: Q=It, V=IR, circuit symbols, ohmic/non-ohmic, series and parallel, AC/DC, mains wiring, P=VI, P=I²R, E=Pt, E=QV, National Grid, transformers. Required practicals: resistance of wire; I-V characteristics. Higher: potential dividers. Triple: static electricity, electric fields.
4.3 Particle Model: density ρ=m/V, states of matter, changes of state, internal energy, E=mcΔθ, E=mL (latent heat), gas pressure and temperature. Higher: Boyle's law, absolute zero. Required practical: density.
4.4 Atomic Structure: protons/neutrons/electrons, isotopes, atomic model history, radioactive decay (alpha/beta/gamma), nuclear equations, half-life, background radiation, fission/fusion. Required practical: half-life sim.
4.5 Forces: scalars/vectors, W=mg, resultant forces, W=Fs, F=ke (Hooke's Law), moments, p=F/A, pressure in fluids, s=vt, v=u+at, s=½(u+v)t, F=ma, Newton's laws, momentum p=mv (Higher only), stopping distances. Higher: impulse=FΔt, terminal velocity. Required practicals: acceleration; spring extension.
4.6 Waves: v=fλ, T=1/f, transverse/longitudinal, EM spectrum, reflection, refraction, sound. Higher: n=sin(i)/sin(r). Triple: lenses, X-rays, radio waves. Required practicals: waves; light.
4.7 Magnetism: magnetic fields, electromagnets. Higher only: Fleming's LHR, F=BIL, motors, induction, generators, Vp/Vs=Np/Ns, transformer efficiency. Higher: induced EMF. Required practical: motor effect.
4.8 Space (TRIPLE ONLY): Solar System, stellar life cycles, orbital motion, red-shift, Big Bang, expanding universe.

REQUIRED PRACTICALS: as listed under each topic above, by name.
KEY EQUATIONS: All equation sheet equations apply.`,

    chemistry: `${BASE_PROMPT}

CURRENT PAGE CONTEXT: AQA GCSE Chemistry (8462) — but answer ALL science subjects if asked

FULL CHEMISTRY SPECIFICATION TOPICS:
4.1 Atomic Structure & Periodic Table: protons/neutrons/electrons, Ar, Mr, isotopes, electronic structure, periodic table groups/periods, Group 1 (alkali metals), Group 7 (halogens), Group 0 (noble gases), transition metals.
4.2 Bonding: ionic (electron transfer, giant lattice), covalent (electron sharing, simple molecular vs giant), metallic (delocalised electrons), alloys, polymers. Higher: dot-cross diagrams. Triple: intermolecular forces.
4.3 Quantitative Chemistry: Higher only — moles: mol=mass÷Mr, mol=c×V, mol=V÷24; % yield=actual÷theoretical×100, atom economy=Mr(useful)÷Mr(all)×100, balancing equations. Higher: limiting reactants, titration calcs.
4.4 Chemical Changes: reactivity series, displacement, metal extraction, pH scale, neutralisation, acid+metal→salt+H₂, acid+base→salt+H₂O, acid+carbonate→salt+H₂O+CO₂, making salts, electrolysis (molten and solutions). Higher: half equations. Required practicals: making salts; electrolysis.
4.5 Energy Changes: exothermic/endothermic, reaction profiles, activation energy, bond energies (ΔH=bonds broken−bonds formed — Higher only), cells, fuel cells. Higher: bond energy calcs. Required practical: temperature changes.
4.6 Rate & Equilibrium: rate=quantity÷time, collision theory, factors (concentration, temp, surface area, catalyst), measuring rate, reversible reactions, Le Chatelier's principle (Higher only), Haber process. Higher: equilibrium position calculations. Required practicals: thiosulfate; marble chips.
4.7 Organic Chemistry: crude oil, fractional distillation, alkanes (CₙH₂ₙ₊₂), cracking, alkenes (CₙH₂ₙ), addition reactions, polymerisation, alcohols, carboxylic acids, esters. Higher: mechanisms. Triple: amino acids, condensation polymers. 
4.8 Chemical Analysis: pure substances, chromatography (Rf=spot÷solvent), flame tests, testing gases, ion tests, mass spectrometry, IR spectroscopy. Higher: interpreting spectra. Required practicals: chromatography; ion tests.
4.9 Atmosphere: composition, evolution of atmosphere, greenhouse effect, climate change, carbon footprint, pollutants (CO, NOₓ, SO₂, particulates).
4.10 Using Resources: finite/renewable, water treatment, LCA, corrosion, alloys, ceramics, polymers, composites, Haber process (N₂+3H₂⇌2NH₃), NPK fertilisers. Higher: fertiliser calculations. Required practical: water purification.`,

    biology: `${BASE_PROMPT}

CURRENT PAGE CONTEXT: AQA GCSE Biology (8461) — but answer ALL science subjects if asked

FULL BIOLOGY SPECIFICATION TOPICS:
4.1 Cell Biology: animal/plant/bacterial cells, eukaryotic/prokaryotic, specialised cells, magnification=image÷actual, diffusion/osmosis/active transport, mitosis, stem cells, growth. Higher: meiosis, stem cell ethics. Required practicals: microscopy; osmosis.
4.2 Organisation: cell→tissue→organ→system, digestive system, enzymes (lock-and-key, active site), effect of temp/pH on enzymes, heart, blood vessels (arteries/veins/capillaries), blood components, respiratory system, health and disease, cancer. Higher: CHD treatments, plant transport. Required practicals: enzyme pH; food tests.
4.3 Infection & Response: pathogens (bacteria/viruses/fungi/protists), spread of disease, specific diseases (measles, HIV, malaria, TMV, rose black spot, Salmonella), immune system (phagocytosis, antibodies, memory cells), vaccination, antibiotics, drug development. Higher: monoclonal antibodies, plant defences.
4.4 Bioenergetics: photosynthesis (6CO₂+6H₂O→C₆H₁₂O₆+6O₂), limiting factors (light, CO₂, temp), uses of glucose, aerobic respiration (C₆H₁₂O₆+6O₂→6CO₂+6H₂O), anaerobic (glucose→lactic acid; glucose→ethanol+CO₂), exercise response (oxygen debt is Higher only). Higher: rate graphs, metabolism. Required practicals: photosynthesis; fermentation.
4.5 Homeostasis & Response: homeostasis, nervous system (CNS, neurons, synapses), reflex arc, brain, eye, endocrine system, blood glucose (insulin; glucagon and how blood glucose is raised again are Higher only), diabetes Type 1&2, thermoregulation, kidneys/ADH, menstrual cycle (FSH/LH/oestrogen/progesterone; how these hormones interact to control the cycle is Higher only), contraception, fertility treatments (using hormones to treat infertility, including IVF, is Higher only). Higher: negative feedback (adrenaline, thyroxine), IVF ethics. Triple: kidney detail. Required practical: reaction time.
4.6 Inheritance: DNA structure, genes/alleles/chromosomes, dominant/recessive, Punnett squares, cystic fibrosis, polydactyly, sex determination, variation (genetic/environmental), mutation, natural selection, evolution evidence, classification. Higher: codominance, genetic engineering. Triple: protein synthesis.
4.7 Ecology: populations/communities/ecosystems, abiotic/biotic factors, interdependence, food webs, competition, adaptations, quadrats/transects, water/carbon/nitrogen cycles, biodiversity, deforestation, climate change, conservation, mark-recapture formula. Higher: biodiversity index, predator-prey. Required practical: habitat sampling.`
  };

  /* ⊕ HONEST WHEN IT CANNOT ANSWER (Mide's ruling, 5 Oct 2026). When the
     tutor could not answer — backend unreachable, an error, no model key —
     this file used to answer anyway: a canned "fact card" picked by keyword
     from the question ("Photosynthesis 6CO₂ + 6H₂O → …"), or "Hmm, I'm having
     trouble thinking right now…". Neither was the tutor, and the fact card
     looked like it was. Those cards are gone. A pupil gets one true line, or
     — when the backend refused on a limit and said why in words a pupil can
     read — that sentence instead. */
  const UNAVAILABLE = "The tutor's unavailable right now. Try again in a few minutes.";

  function esc(t) {
    return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  // The refusal's own sentence, only for a limit (429) the backend explained.
  async function limitMessage(res) {
    if (res.status !== 429) return null;
    try {
      const body = await res.json();
      const m = body && body.message;
      return (typeof m === 'string' && m.trim()) ? m.trim() : null;
    } catch (e) { return null; }
  }

  function addMsg(role, html) {
    const box = document.getElementById('chatMsgs');
    if (!box) return null;
    const d = document.createElement('div');
    d.className = `chat-msg chat-msg--${role}`;
    d.innerHTML = `<div class="chat-msg__avatar">${role==='user'?'🧑':'⚡'}</div><div class="chat-msg__bubble">${html}</div>`;
    box.appendChild(d);
    box.scrollTop = box.scrollHeight;
    return d;
  }

  /* ⊕ B2C polish (9 Oct 2026) — the tutor's reply, as the bubble draws it.
     Real answers carried literal "---" lines and a leading "> " (Markdown the
     model writes) because only bold, italics and code were understood. Now:
       · ESCAPED FIRST, then formatted. This used to put the model's text into
         innerHTML raw, so any "<" in a reply was markup;
       · a "---" / "***" / "___" line is a thin rule (<hr class="chat-rule">);
       · consecutive "> " lines are one quote (<blockquote class="chat-quote">);
       · a "# Heading" line is a bold line (the same defect: raw "##" marks);
       · **bold**, *italics*, `code` as before, and every other newline a
         <br> (so a blank line between paragraphs is still <br><br>).
     Blank lines touching a rule, a quote or a list are dropped: the block
     already separates, and keeping them would stack a gap on its margin.

     ⊕ Round 2 (Mide, 9 Oct 2026) — "show that chemical formulae (<sub>),
     bold, lists and line breaks still render, not as raw tags. If they
     don't, render a safe allow-list and escape everything else." Driven
     against the real model: it writes CO₂ in Unicode and bold as **…**, so
     no raw tag showed — but lists came out as "- " / "1." text lines, and a
     reply that DID carry <sub> (a pupil asks for HTML, or pastes some) would
     have shown the tags as text. So:
       · ALLOW-LIST. Exactly sub, sup, b, strong, em, i, br, p, ul, ol, li
         survive as real elements, and only in their bare form (`<sub>`,
         `</sub>`, `<br/>`). A tag with ANY attribute (`<sub onclick=…>`,
         `<b style=…>`) is not on the list and is escaped like every other
         "<". Allowed tags are lifted out as placeholders BEFORE the escape
         and re-emitted by restoreTags() in canonical form and balanced (a
         stray close is dropped, an unclosed open is closed at the end), so
         no byte the reply supplied is ever itself parsed as markup.
       · LISTS. Runs of "- " / "* " / "• " lines are a <ul>, runs of "1. " /
         "1) " lines an <ol>, numbered from the reply's own first number. A
         blank line between two items of one list does not end it; an
         indented line under an item continues that item; an indented item
         is one nested list. */
  const ALLOWED_TAG = /<(\/?)(sub|sup|strong|em|br|ul|ol|li|b|i|p)\s*\/?>/gi;
  const PH = /(\d+)/g;

  function inlineReply(line) {
    return line.replace(/\*\*(.*?)\*\*/g,'<strong>$1</strong>').replace(/\*(.*?)\*/g,'<em>$1</em>').replace(/`(.*?)`/g,'<code>$1</code>');
  }

  // Re-emit the reply's own allowed tags, balanced. tags[n] = {close, name};
  // its placeholder is  n  (neither character survives in the
  // reply itself: both are stripped before lifting).
  function restoreTags(html, tags) {
    const stack = [];
    const out = html.replace(PH, (m, n) => {
      const t = tags[+n];
      if (t.name === 'br') return t.close ? '' : '<br>';
      if (!t.close) { stack.push(t.name); return '<' + t.name + '>'; }
      const at = stack.lastIndexOf(t.name);
      if (at === -1) return '';                        // a close with no open
      let closes = '';
      while (stack.length > at) closes += '</' + stack.pop() + '>';
      return closes;
    });
    let tail = '';
    while (stack.length) tail += '</' + stack.pop() + '>';
    // A line break touching a block tag is spacing the block already gives.
    return (out + tail)
      .replace(/(?:<br>)+(?=<\/?(?:ul|ol|li|p)>)/g, '')
      .replace(/(<\/?(?:ul|ol|li|p)>)(?:<br>)+/g, '$1');
  }

  const RULE = /^\s*([-*_])(?:\s*\1){2,}\s*$/;
  function listItem(raw) {
    if (RULE.test(raw)) return null;                   // a rule, not a list
    let m = /^(\s*)(\d{1,3})[.)]\s+(.*)$/.exec(raw);
    if (m) return { kind: 'ol', indent: m[1].length, start: +m[2], body: m[3] };
    m = /^(\s*)[-*•]\s+(.*)$/.exec(raw);
    if (m) return { kind: 'ul', indent: m[1].length, start: 1, body: m[2] };
    return null;
  }
  function newList(li) {
    return { kind: li.kind, indent: li.indent, start: li.start, items: [{ lines: [li.body], sub: null }] };
  }
  function renderList(list) {
    const open = (list.kind === 'ol' && list.start !== 1) ? '<ol start="' + list.start + '">' : '<' + list.kind + '>';
    return open + list.items.map(it =>
      '<li>' + it.lines.map(inlineReply).join('<br>') + (it.sub ? renderList(it.sub) : '') + '</li>'
    ).join('') + '</' + list.kind + '>';
  }

  /* ⊕ B2C polish round 3 (9 Oct 2026) — Markdown TABLES. A real reply drew
     "| Substance | Formula |\n|---|---|\n| Carbon dioxide | CO₂ |" as raw
     pipes, and once the model collapsed the whole table onto ONE line. The
     allow-list has no table elements (Mide's ruling), so a table becomes
     allowed markup instead:
       · the |---|---| separator row is dropped (alignment colons allowed);
       · the header row is ONE bold line, its cells joined by " — " (kept:
         a header like "Metal | Reaction with water" is information the
         rows alone do not carry);
       · each body row is a <ul> item, its cells joined by " — ", with
         **bold**, <sub> etc. inside a cell rendered as everywhere else.
     A table is only ever a row line FOLLOWED BY a separator line with the
     same number of cells, so a lone "|" in prose stays text. A one-line
     table is split back into lines first (expandTables) and then drawn by
     the same code. "\|" inside a cell is a literal pipe. */
  const SEP_CELL = /^\s*:?-+:?\s*$/;
  const SEP_RUN = /\|\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|/;
  function splitCells(s) {
    // Split on unescaped pipes ("\|" is a literal pipe inside a cell).
    return s.replace(/\\\|/g, '').split('|').map(c => c.replace(//g, '|').trim());
  }
  function rowCells(line) {
    let s = line.trim();
    if (s.indexOf('|') === -1) return null;
    if (s.charAt(0) === '|') s = s.slice(1);
    if (s.charAt(s.length - 1) === '|' && s.charAt(s.length - 2) !== '\\') s = s.slice(0, -1);
    return splitCells(s);
  }
  function sepCount(line) {
    if (line.indexOf('|') === -1 || line.indexOf('-') === -1) return 0;
    const cells = rowCells(line);
    return cells && cells.length >= 2 && cells.every(c => SEP_CELL.test(c)) ? cells.length : 0;
  }
  // One line holding a whole table ("| A | B | |---|---| | c | d | | e | f |")
  // becomes the lines a normal table is written on. Anything before the
  // header or after the last row stays as its own line of prose.
  function expandTables(lines) {
    const out = [];
    for (const line of lines) {
      const m = SEP_RUN.exec(line);
      const before = m ? line.slice(0, m.index) : '';
      const after = m ? line.slice(m.index + m[0].length) : '';
      if (!m || (before.trim() === '' && after.trim() === '')) { out.push(line); continue; }
      const n = splitCells(m[0].slice(1, -1)).length;
      const pre = splitCells(before);
      if (pre.length && pre[pre.length - 1] === '') pre.pop();
      let lead = '', head = null;
      if (pre.join('') !== '') {
        if (pre.length < n) { out.push(line); continue; }        // no header: leave it
        head = pre.slice(pre.length - n);
        lead = pre.slice(0, pre.length - n).join('|').trim();
      }
      const toks = splitCells(after);
      const trailer = toks.pop();
      const rows = [];
      let row = null;
      for (const t of toks) {
        if (!row) { if (t === '') continue; row = []; }          // the "| |" between rows
        row.push(t);
        if (row.length === n) { rows.push(row); row = null; }
      }
      let tail = trailer;
      if (row) { if (trailer !== '') { row.push(trailer); tail = ''; } rows.push(row); }
      const draw = cells => '| ' + cells.map(c => c.replace(/\|/g, '\\|')).join(' | ') + ' |';
      if (lead) out.push(lead);
      if (head) out.push(draw(head));
      out.push('|' + Array(n).fill('---').join('|') + '|');
      rows.forEach(r => out.push(draw(r)));
      if (tail !== '') out.push(tail);
    }
    return out;
  }
  function renderCells(cells) {
    return cells.filter(c => c !== '').map(inlineReply).join(' — ');
  }

  function formatReply(text) {
    const tags = [];
    const lifted = String(text).replace(/[]/g, '').replace(ALLOWED_TAG, (m, close, name) => {
      tags.push({ close: !!close, name: name.toLowerCase() });
      return '' + (tags.length - 1) + '';
    });
    const lines = expandTables(esc(lifted).replace(/\uE002/g, '').replace(/\r\n?/g, '\n').split('\n'));
    const items = [];                       // {block:bool, html | quote | list}
    let quote = null, list = null;
    for (let i = 0; i < lines.length; i++) {
      const raw = lines[i];
      const li = listItem(raw);
      if (list) {
        const last = list.items[list.items.length - 1];
        if (li && li.indent >= list.indent + 2) {                  // nested
          if (!last.sub) last.sub = newList(li);
          else if (last.sub.kind === li.kind) last.sub.items.push({ lines: [li.body], sub: null });
          else last.lines.push(li.body);
          continue;
        }
        if (li && li.kind === list.kind) { list.items.push({ lines: [li.body], sub: null }); continue; }
        if (!li && /^\s{2,}\S/.test(raw)) {                        // continuation
          const tgt = last.sub ? last.sub.items[last.sub.items.length - 1] : last;
          tgt.lines.push(raw.trim());
          continue;
        }
        if (raw.trim() === '') {                                   // a gap inside one list?
          let j = i + 1;
          while (j < lines.length && lines[j].trim() === '') j++;
          const next = j < lines.length ? listItem(lines[j]) : null;
          if (next && (next.kind === list.kind || next.indent >= list.indent + 2)) { i = j - 1; continue; }
        }
        list = null;
      }
      const head = li ? null : rowCells(raw);
      const n = head && i + 1 < lines.length ? sepCount(lines[i + 1]) : 0;
      if (n && n === head.length && !sepCount(raw)) {             // a table
        quote = null;
        let j = i + 2;
        const rows = [];
        for (; j < lines.length && lines[j].trim() !== '' && lines[j].indexOf('|') !== -1; j++) {
          if (sepCount(lines[j])) continue;
          const r = renderCells(rowCells(lines[j]));
          if (r) rows.push('<li>' + r + '</li>');
        }
        const h = renderCells(head);
        if (h) items.push({ block: false, html: '<strong>' + h + '</strong>' });
        if (rows.length) items.push({ block: true, html: '<ul>' + rows.join('') + '</ul>' });
        i = j - 1;
        continue;
      }
      if (li) {
        quote = null;
        list = newList(li);
        items.push({ block: true, list });
        continue;
      }
      const q = /^\s*&gt;\s?(.*)$/.exec(raw);
      if (q) {
        if (!quote) { quote = []; items.push({ block: true, quote }); }
        quote.push(inlineReply(q[1]));
        continue;
      }
      quote = null;
      if (RULE.test(raw)) {
        items.push({ block: true, html: '<hr class="chat-rule">' });
        continue;
      }
      const h = /^\s*#{1,6}\s+(.*?)\s*#*\s*$/.exec(raw);
      items.push({ block: false, html: h ? '<strong>' + inlineReply(h[1]) + '</strong>' : inlineReply(raw) });
    }
    // A blank line next to a block is spacing the block already gives.
    const kept = items.filter((it, i) => {
      if (it.block || it.html !== '') return true;
      const prev = items[i - 1], next = items[i + 1];
      return !((prev && prev.block) || (next && next.block));
    });
    let out = '';
    kept.forEach((it, i) => {
      if (it.quote) it.html = '<blockquote class="chat-quote">' + it.quote.join('<br>') + '</blockquote>';
      if (it.list) it.html = renderList(it.list);
      const prev = kept[i - 1];
      if (prev && !prev.block && !it.block) out += '<br>';
      out += it.html;
    });
    return restoreTags(out, tags);
  }
  if (window.MRB_TUTOR_TEST_HOOK) window.MRB_TUTOR_TEST_HOOK.formatReply = formatReply;

  /* MRB-257 — KS3 framing, appended after the subject prompt.
     Additive by construction: it is only ever reached when a page passes
     `keyStage: 'ks3'`, and no page did before KS3 lesson pages started to.
     A KS4 page therefore builds the byte-identical prompt it always did.

     It APPENDS rather than replacing the subject prompt, and that is the
     deliberate choice. The base prompt carries the safeguarding section —
     forty lines of it, and the single most important thing in the file for an
     eleven-year-old audience — plus the tone, the FIFA method and the honesty
     rules, all of which hold at KS3. What does not hold is the exam framing
     wrapped around them, so this overrides that explicitly and last, where a
     model weights it most. Replacing the whole prompt would mean a second copy
     of the safeguarding block, free to drift from the first. */
  const KS3_FRAMING = `

KEY STAGE 3 — THIS OVERRIDES THE EXAM FRAMING ABOVE.
You are talking to a KS3 student: roughly 11 to 14 years old, two or three years before they start a GCSE course. Everything above about warmth, honesty, the FIFA method for calculations, units in every answer, and safeguarding still applies exactly as written. The exam-board framing does not.
- Stay within this student's key stage: use only KS3 (Year 7–9) ideas and vocabulary. Never bring in GCSE-only content or terms — for example ions (H⁺, OH⁻), moles, electron arrangements or shells beyond KS3, "cardiac output" or "stroke volume". Do not slip them in under another name or as a symbol either — no "H⁺ particles", no ion formulae. If the honest answer needs a GCSE idea, explain it in KS3 words without the GCSE term, and say they'll meet the full picture at GCSE. Decide this before you start writing, and check every term you use against it.
- This student has NO tier and NO pathway. Never say "Higher tier", "Foundation", "Triple", "Combined", "paper 1", "mark scheme", "the spec" or a spec point code. They do not exist for this student yet, and naming them tells a twelve-year-old they are behind.
- Do not label content ⭐ HIGHER TIER or 🔬 TRIPLE ONLY. There are no tiers here.
- Drop the "✅ Key exam words" line and the command-word drilling. Teach the correct scientific word — "respiration", "diffusion", "chromosome" — because the word is the idea and they will need it later, but teach it as the name of a thing, not as a mark-scheme term.
- The GCSE specification listed above is BACKGROUND ONLY, so that you know where this is going. Do not teach from it and do not quote it. Answer the question the student actually asked, at the depth they asked it.
- Never refer to the student by their school year. Say "a student your age".
- Keep it short and concrete. Curiosity is the whole point at this stage — if they ask something off-topic that comes from real interest, follow it.`;

  /* ⊕ Parent truth (13 Oct 2026) — a child is TOLD, before they type, that
     their parent can see what they ask. A child session's questions are
     logged for their parent (see `ask()`: question, lesson, time — never the
     reply), so a child must not find that out afterwards. One plain line,
     above the input, in the panel's own body ink (--text on --bg: AA in both
     themes on every page that mounts the panel), tied to the input with
     aria-describedby so a screen reader says it too. "Parent or tutor": an
     organisation's child is attached to the organisation's account, not a
     parent's, and the page cannot tell the two apart without a network call.
     ONLY FOR A CHILD SESSION (MrBadmusConfig.isChildSession); a school pupil's
     panel is untouched. */
  function childDisclosure() {
    try {
      const c = cfg();
      if (!c || typeof c.isChildSession !== 'function') return;
      const sess = JSON.parse(localStorage.getItem(c.AUTH_STORAGE_KEY) || 'null');
      if (!c.isChildSession(sess)) return;
      const row = document.querySelector('#chatOverlay .chat-input-row');
      if (!row || document.getElementById('chatDisclosure')) return;
      const p = document.createElement('p');
      p.id = 'chatDisclosure';
      p.className = 'chat-disclosure';
      p.style.cssText = 'margin:0 auto;max-width:860px;width:100%;box-sizing:border-box;padding:10px 24px 6px;font-size:0.875rem;line-height:1.4;font-weight:500;color:var(--text)';
      p.textContent = 'Your parent or tutor can see the questions you ask here.';
      row.parentNode.insertBefore(p, row);
      const input = document.getElementById('ci');
      if (input) input.setAttribute('aria-describedby', 'chatDisclosure');
    } catch (e) { /* a missing line never breaks the tutor */ }
  }

  async function init(config) {
    childDisclosure();
    currentKeyStage = config.keyStage || '';
    await loadStudentSession();
    currentSubject = config.subject || 'physics';
    currentTopic = config.topic || '';
    systemPrompt = SUBJECT_PROMPTS[currentSubject] || SUBJECT_PROMPTS.physics;
    if (studentName) systemPrompt += `\n\nThe student you are speaking with is named ${studentName}. Use their name naturally and warmly in your replies — like a teacher who knows their student well — but never overuse it (don't start every sentence with their name).`;
    if (currentKeyStage === 'ks3') {
      systemPrompt += KS3_FRAMING;
    } else {
      if (studentProfile?.tier) {
        const tierLabel = studentProfile.tier.charAt(0).toUpperCase() + studentProfile.tier.slice(1);
        systemPrompt += `\n\nThe student is on the ${tierLabel} tier.`;
        /* ⊕ 13 Oct 2026 — stay within the student's key stage and tier, said
           explicitly for Foundation (the backend carries the same guard). */
        if (studentProfile.tier === 'foundation') {
          systemPrompt += ` Stay within Foundation tier content. Do not teach Higher-only content unless the student explicitly asks for it, and when they do, label it ⭐ HIGHER TIER. In the specification above, anything marked "Higher only" is Higher-only content. Items listed after "Higher:" may be answered if asked, labelled ⭐ HIGHER TIER.`;
        }
      }
      if (studentProfile?.science_pathway) {
        const pathLabel = studentProfile.science_pathway.charAt(0).toUpperCase() + studentProfile.science_pathway.slice(1);
        systemPrompt += `\n\nThe student is studying ${pathLabel} Science.`;
      }
    }
    if (currentTopic) systemPrompt += `\n\nThe student is currently studying: ${currentTopic}. Focus on this topic when possible.`;

    document.getElementById('chatOverlay')?.addEventListener('click', e => { if(e.target===document.getElementById('chatOverlay')) close(); });
    document.querySelector('.close-btn')?.addEventListener('click', close);
    document.querySelector('.chat-send-btn')?.addEventListener('click', () => ask());
    document.getElementById('ci')?.addEventListener('keydown', e => { if(e.key==='Enter') ask(); });
    document.getElementById('imgInput')?.addEventListener('change', () => handleImg(document.getElementById('imgInput')));
    // ⊕ Experience run, 24 Sep 2026 (stream G). `<label for="imgInput">` opens
    // the file picker on a mouse click through native `for` association, but
    // a `<label>` carries no keyboard activation of its own — Enter/Space
    // only trigger the default action on elements the platform already
    // treats as controls (button, a[href], checkbox/radio…), and a label is
    // not one of them. `focus_audit.py` found this as an "unreachable at
    // all" control: with the label now `tabindex="0" role="button"`
    // (build_ks3.py, generate_site_v5.py), a keyboard user can reach it, but
    // reaching it did nothing until Enter/Space is wired to the same click()
    // a mouse already performs.
    document.querySelector('.img-btn')?.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); e.currentTarget.click(); }
    });

  // Paste image support — Ctrl+V / Cmd+V directly into chat
  document.addEventListener('paste', function(e) {
    const overlay = document.getElementById('chatOverlay');
    if (!overlay || !overlay.classList.contains('open')) return;
    const items = e.clipboardData?.items;
    if (!items) return;
    for (const item of items) {
      if (item.type.startsWith('image/')) {
        const file = item.getAsFile();
        if (!file) break;
        const reader = new FileReader();
        reader.onload = function(evt) {
          pendingImg = evt.target.result;
          const preview = document.getElementById('imgPreview');
          const row = document.getElementById('imgPreviewRow');
          if (preview && row) { preview.src = pendingImg; row.style.display = 'flex'; }
        };
        reader.readAsDataURL(file);
        e.preventDefault();
        break;
      }
    }
  });
    document.querySelectorAll('.quick-q').forEach(btn => btn.addEventListener('click', () => ask(btn.dataset.q)));
    /* MRB-257 — the image-clear control, bound rather than inline. KS4 wires
       it with an `onclick` attribute, which KS3's "all interactive controls
       are real buttons" gate forbids on a KS3 page. Both markups now work:
       this finds nothing on a KS4 page and changes nothing there. */
    document.querySelectorAll('[data-clear-img]').forEach(el => el.addEventListener('click', clearImg));
    document.querySelectorAll('[data-open-chat]').forEach(el => el.addEventListener('click', open));
  }

  // Keep-alive ping every 10 minutes — prevents Render cold starts.
  // ⊕ Test isolation — production only. It exists to keep Render warm; a
  // TEST backend runs on the developer's own machine and has no cold start,
  // and with no config there is nothing to ping.
  function warm() {
    const c = cfg();
    if (!c || c.environment !== 'prod') return;
    fetch(c.BACKEND_URL + '/api/health').catch(function(){});
  }
  setInterval(warm, 10 * 60 * 1000);

  // Also ping immediately on page load to warm up Render
  setTimeout(warm, 2000);

  function open() {
    loadStudentSession();
    const ov = document.getElementById('chatOverlay');
    // ⊕ RULED 25 Sep 2026 (experience run, stream K) — PROD N6. The panel
    // traps Tab and closes on Escape (Stream G's fix, directly below) — it
    // BEHAVES like a modal dialog everywhere on the estate already — but
    // never SAID so: no `role="dialog"`, no `aria-modal`, no accessible
    // accessible name of its own, unlike the flashcards overlay (`student_rulings.py`,
    // `data-mrb-dialog="flashcards"`) which names this exact trio. A static
    // label rather than `aria-labelledby` pointing at `#chat-head-subtitle`:
    // that node's own text is a personalised greeting ("Hey Name! 👋") that
    // is empty until a signed-in student's name loads and is absent
    // entirely on a page with no such element — an accessible NAME must not
    // depend on either. Set on every `open()` rather than once: cheap, and
    // correct regardless of which of this file's several pages' markup
    // happens to be on screen.
    if (ov) {
      ov.setAttribute('role', 'dialog');
      ov.setAttribute('aria-modal', 'true');
      ov.setAttribute('aria-label', 'Ask MrBadmus');
    }
    // Stream G follow-up — capture whichever control was focused (a mouse
    // click on a button focuses it natively) BEFORE this panel steals focus,
    // so `close()` has somewhere real to give it back to.
    chatOpener = (document.activeElement && document.activeElement !== document.body)
      ? document.activeElement : null;
    /* MRB-257 — the closed overlay is `opacity:0; pointer-events:none`, which
       hides it from the eye and the mouse and NOT from the keyboard: a text
       input, a file picker and two buttons sit in the tab order regardless.
       A page that ships the overlay `inert` opts into having it managed here.
       KS4's markup carries neither attribute, so both lines are no-ops there
       and its behaviour is unchanged. */
    ov?.removeAttribute('inert');
    ov?.classList.add('open');
    if (!chatInited) {
      chatInited = true;
      const sn = {physics:'Physics ⚡',chemistry:'Chemistry 🧪',biology:'Biology 🌿'}[currentSubject];
      /* MRB-257 — a KS3 student is not sitting a GCSE. Same sentence, minus a
         qualification they have not started. */
      const subj = currentKeyStage === 'ks3' ? 'Science' : 'GCSE Science';
      const greet = studentName
        ? "Hey " + studentName + "! 👋 I'm Mr Badmus, here to help you smash your " + subj + ". What are we stuck on?"
        : "Hey! 👋 I'm Mr Badmus, here to help you smash your " + subj + ". What are we stuck on?";
      addMsg('bot', greet);
    }
    setTimeout(() => document.getElementById('ci')?.focus(), 100);
  }

  function close() {
    const ov = document.getElementById('chatOverlay');
    ov?.classList.remove('open');
    if (ov?.hasAttribute('data-inert-when-closed')) ov.setAttribute('inert', '');
    // Stream G follow-up — give the keyboard back to whoever opened this,
    // the same pattern shared/set-work.js's sheet already uses.
    if (chatOpener) { try { chatOpener.focus({ preventScroll: true }); } catch (e) {} chatOpener = null; }
  }

  // Stream G follow-up, 25 Sep 2026 — Escape closes the panel, and Tab stays
  // inside it while it is open. `focus_audit.py` found the open panel let Tab
  // walk out into the page behind it, same shape MRB-335 already fixed once
  // for the Set work sheet (shared/set-work.js) — this is that fix, scoped to
  // `#chatOverlay`. The list is read at press time, not cached, because the
  // preview row and the image button come and go with `pendingImg`.
  document.addEventListener('keydown', e => {
    const ov = document.getElementById('chatOverlay');
    if (!ov || !ov.classList.contains('open')) return;
    if (e.key === 'Escape') { close(); return; }
    if (e.key !== 'Tab') return;
    const items = Array.prototype.slice.call(
      ov.querySelectorAll('button,[href],input,select,textarea,[tabindex]')
    ).filter(n => !n.disabled && n.getAttribute('tabindex') !== '-1' && n.offsetParent);
    if (!items.length) return;
    const first = items[0], last = items[items.length - 1], here = document.activeElement;
    if (e.shiftKey && (here === first || !ov.contains(here))) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && (here === last || !ov.contains(here))) { e.preventDefault(); first.focus(); }
  });

  function handleImg(input) {
    const file = input.files[0]; if (!file) return;
    const reader = new FileReader();
    reader.onload = e => {
      pendingImg = e.target.result;
      const row = document.getElementById('imgPreviewRow');
      const prev = document.getElementById('imgPreview');
      if (prev) prev.src = pendingImg;
      if (row) row.style.display = 'flex';
    };
    reader.readAsDataURL(file); input.value='';
  }

  function clearImg() {
    pendingImg = null;
    const prev = document.getElementById('imgPreview'), row = document.getElementById('imgPreviewRow');
    if (prev) prev.src=''; if (row) row.style.display='none';
  }

  async function ask(preset) {
    if (!chatInited) open();
    const input = document.getElementById('ci');
    const q = preset || (input ? input.value.trim() : '');
    const hasImg = !!pendingImg;
    if (!q && !hasImg) return;
    if (input) input.value = '';
    // The pupil's own words are text too (they were innerHTML until 9 Oct 2026).
    addMsg('user', esc(q||'Please answer this question:') + (hasImg ? `<br><img src="${pendingImg}" style="max-width:150px;border-radius:6px;margin-top:6px;display:block;" alt="question"/>` : ''));
    const imgData = pendingImg; clearImg();
    const t = addMsg('bot', '<div class="typing"><span></span><span></span><span></span></div>');
    let userContent = hasImg ? [{ type:'image', source:{ type:'base64', media_type:imgData.split(';')[0].split(':')[1], data:imgData.split(',')[1] }}, { type:'text', text:q||'Answer this GCSE Science question fully using FIFA for any calculations.' }] : q;
    chatHistory.push({ role:'user', content:userContent });
    try {
      const c = cfg();
      if (!c) throw new Error('config.js is not on this page: no tutor backend');
      // Wake up Render if needed (it spins down after inactivity)
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), 55000); // 55s timeout
      let authHeaders = { 'Content-Type': 'application/json' };
      // ⊕ Parent truth (11 Oct 2026) — set only for a consumer child.
      let childContext = null;
      try {
        const raw = localStorage.getItem(c.AUTH_STORAGE_KEY);
        const sess = raw && JSON.parse(raw);
        const tok = sess?.access_token;
        if (tok) authHeaders['Authorization'] = 'Bearer ' + tok;
        /* A child's question is logged for their parent (question, lesson,
           time — never the reply), and the server needs to know which lesson
           it was asked on. A school pupil's body is exactly what it was:
           `context` is added for a child session and for nobody else. */
        if (tok && typeof c.isChildSession === 'function' && c.isChildSession(sess)) {
          childContext = { path: window.location.pathname, title: currentTopic || document.title || '' };
        }
      } catch (e) {}
      const res = await fetch(c.BACKEND_URL + '/api/chat', {
        method:'POST',
        headers: authHeaders,
        body:JSON.stringify(childContext
          ? { system:systemPrompt, messages:chatHistory, context:childContext }
          : { system:systemPrompt, messages:chatHistory }),
        signal: controller.signal
      });
      clearTimeout(timeout);
      if (!res.ok) {
        const said = await limitMessage(res);
        const e = new Error(`HTTP ${res.status}`);
        e.pupilMessage = said;
        throw e;
      }
      const data = await res.json();
      if (data.error) throw new Error(data.error.message);
      const reply = data.content?.map(c=>c.text||'').filter(Boolean).join('');
      if (!reply) throw new Error('empty reply');
      if (t) t.querySelector('.chat-msg__bubble').innerHTML = formatReply(reply);
      chatHistory.push({ role:'assistant', content:reply });
      if (chatHistory.length > 20) chatHistory.splice(0,2);
    } catch(err) {
      console.error('MrBadmus chat request failed:', (err && err.message) ? err.message : err);
      chatHistory.pop();
      if (t) t.querySelector('.chat-msg__bubble').innerHTML = esc((err && err.pupilMessage) || UNAVAILABLE);
    }
    document.getElementById('chatMsgs').scrollTop = 99999;
  }

  return { init, open, close, ask };
})();

/* ── MOBILE NAV HAMBURGER ── */
try {
  document.addEventListener('DOMContentLoaded', function () {
    var nav = document.querySelector('.nav');
    if (!nav || nav.querySelector('.nav-toggle')) return;

    var links = nav.querySelector('.nav-links');
    if (!links) return;

    var btn = document.createElement('button');
    btn.className = 'nav-toggle';
    btn.setAttribute('aria-label', 'Menu');
    btn.setAttribute('aria-expanded', 'false');
    btn.textContent = '☰';
    nav.appendChild(btn);

    btn.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.textContent = open ? '✕' : '☰';
    });

    links.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        links.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
        btn.textContent = '☰';
      }
    });

    document.addEventListener('click', function (e) {
      if (!nav.contains(e.target)) {
        links.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
        btn.textContent = '☰';
      }
    });
  });
} catch (e) {}

/* ── B2C unit 7 (Mide's ruling 5, 5 Oct 2026): a family child's KS4 lesson
   is DONE when they finish its questions ──────────────────────────────────
   A lesson a parent (or Mr Badmus) set used to be finished only by tapping
   "Mark as done" on the child's Today screen; answering every question on
   the lesson page changed nothing. Completion now comes from ACTIVITY.

   On a KS3 page that activity is the ladder's own `/api/quiz-score` post,
   which every pupil's page already makes; the backend matches it to the
   child's work, and nothing on the page changed. A KS4 page posts no score
   anywhere (docs/ks4/pilot-port-report.md §8 item 11 — its slugs collide
   with KS3's), so this is its signal, and ONLY for a family child: the
   session must be a child session (MrBadmusConfig.isChildSession). A school
   pupil's KS4 page installs nothing and sends nothing — it behaves exactly
   as before.

   "Finished" is what each KS4 page already shows when the questions are all
   answered, read rather than re-implemented:
     · a classic page's quiz — `#quizEndMsg` is shown (both of its quiz
       scripts show it only once every card is answered or checked);
     · a rebuilt (pilot) page's ladder — its score line reads "Score N of 4",
       which Design's Ks4Ladder writes only when all four rungs are resolved.
   One post per page load; the backend ticks the child's open lesson item
   whose page this is, and answers 200 with `done: 0` when there is none. */
try {
  (function () {
    var path = window.location.pathname || '';
    if (!/^\/(combined|triple)\//.test(path)) { return; }
    function start() {
      var c = window.MrBadmusConfig;
      if (!c || !c.BACKEND_URL || !c.AUTH_STORAGE_KEY || typeof c.isChildSession !== 'function') { return; }
      var session = null;
      try { session = JSON.parse(window.localStorage.getItem(c.AUTH_STORAGE_KEY) || 'null'); } catch (e) { return; }
      if (!session || !session.access_token || !c.isChildSession(session)) { return; }
      var sent = false;
      var obs = null;
      function finished() {
        var end = document.getElementById('quizEndMsg');
        if (end && end.style.display !== 'none' && (end.textContent || '').trim()) { return true; }
        var score = document.querySelector('.ks3-ladder-score .ks3-score');
        return !!(score && /^Score \d+ of \d+$/.test((score.textContent || '').trim()));
      }
      function check() {
        if (sent || !finished()) { return; }
        sent = true;
        if (obs) { obs.disconnect(); }
        try {
          var s2 = JSON.parse(window.localStorage.getItem(c.AUTH_STORAGE_KEY) || 'null') || session;
          fetch(c.BACKEND_URL + '/api/consumer/child/lesson-done', {
            method: 'POST',
            keepalive: true,
            headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + s2.access_token },
            body: JSON.stringify({ path: path, key_stage: 'KS4' })
          }).catch(function () { /* best effort — the lesson never waits on this */ });
        } catch (e) { /* fetch unavailable — degrade silently */ }
      }
      obs = new MutationObserver(check);
      obs.observe(document.body, { subtree: true, childList: true, attributes: true,
                                   attributeFilter: ['style'], characterData: true });
      check();
    }
    if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', start); }
    else { start(); }
  })();
} catch (e) {}

/* ── Parent truth (13 Oct 2026): "Back to Today" when a child finishes ────
   A family or organisation child's home is Today (MrBadmusConfig.CHILD_HOME).
   Finishing a lesson used to leave them at the bottom of a lesson page with
   the school's way out (the top bar's lesson links) and no way back to the
   list their parent set. So, ONLY FOR A CHILD SESSION (the same one test as
   above, no network call), once the page shows its own "finished" state a
   primary "Back to Today" link is revealed:
     · beside what the page shows when it is finished — under a classic KS4
       page's quiz end message (`#quizEndMsg`), or under the ladder's score
       line on a KS3 page ("You got N of M.") or a rebuilt KS4 page
       ("Score N of 4");
     · and at the end of the page — after the end-matter cards on KS3, above
       the footer on rebuilt KS4 pages (a classic page's quiz IS the end of
       its page, so it gets one).
   Each is the page's own primary button class (`ks3-btn is-primary` on KS3,
   `btn btn--primary` on a rebuilt KS4 page, `btn-primary` on a classic one),
   so both themes are the design system's, with a 48px tap target. `env` and
   `api` travel, as the student guard's own redirect to Today carries them.
   A school pupil's page installs nothing here. Once revealed, it stays: a
   "Retry my misses" that empties the ladder does not take the way home away. */
try {
  (function () {
    var path = window.location.pathname || '';
    if (!/^\/(ks3|combined|triple)\//.test(path)) { return; }
    function start() {
      var c = window.MrBadmusConfig;
      if (!c || !c.AUTH_STORAGE_KEY || typeof c.isChildSession !== 'function') { return; }
      var session = null;
      try { session = JSON.parse(window.localStorage.getItem(c.AUTH_STORAGE_KEY) || 'null'); } catch (e) { return; }
      if (!session || !c.isChildSession(session)) { return; }
      function home() {
        var q = new URLSearchParams(window.location.search), keep = new URLSearchParams();
        ['env', 'api'].forEach(function (k) { if (q.get(k)) { keep.set(k, q.get(k)); } });
        var qs = keep.toString();
        return (c.CHILD_HOME || '/consumer/today.html') + (qs ? '?' + qs : '');
      }
      function txt(el) { return el ? (el.textContent || '').replace(/\s+/g, ' ').trim() : ''; }
      function endMsg() {
        var end = document.getElementById('quizEndMsg');
        return (end && end.style.display !== 'none' && txt(end)) ? end : null;
      }
      function ladderDone() {
        var t = txt(document.querySelector('.ks3-ladder-score .ks3-score'));
        return /^Score \d+ of \d+$/.test(t) || /^You got \d+ of \d+\.$/.test(t);
      }
      function btnClass() {
        if (document.querySelector('link[href*="/shared/ks3.css"]')) { return 'ks3-btn is-primary'; }
        if (document.querySelector('link[href*="/shared/ks4-ds.css"]')) { return 'btn btn--primary'; }
        return 'btn-primary';
      }
      function make(where, centre) {
        var box = document.createElement('div');
        box.setAttribute('data-mrb-child-home', where);
        box.style.cssText = 'margin:18px 0;' + (centre ? 'text-align:center;' : '');
        var a = document.createElement('a');
        a.href = home();
        a.className = btnClass();
        a.style.cssText = 'display:inline-flex;align-items:center;justify-content:center;min-height:48px;box-sizing:border-box;text-decoration:none;flex:none';
        a.textContent = 'Back to Today';
        box.appendChild(a);
        return box;
      }
      var shown = false;
      function ensure() {
        if (!shown) {
          if (!endMsg() && !ladderDone()) { return; }
          shown = true;
        }
        var end = document.getElementById('quizEndMsg');
        var score = document.querySelector('.ks3-ladder-score');
        var by = end || score;
        if (by && by.parentNode) {
          var next = by.nextElementSibling;
          if (!(next && next.getAttribute('data-mrb-child-home') === 'score')) {
            by.parentNode.insertBefore(make('score', !!end), by.nextSibling);
          }
        }
        /* ⊕ fixD (13 Oct 2026): on a KS3 lesson the footer sits OUTSIDE
           <main>, so a link placed above it ran the full page width, flush
           at x=0. There it goes straight after the end-matter cards, inside
           the lesson's own column. A rebuilt KS4 page keeps its footer in
           that column (beside the cards), and keeps the old place. */
        var foot = document.querySelector('footer.ks3-footer');
        var cards = document.querySelector('.ks3-endmatter');
        if (cards && cards.parentNode && (!foot || foot.parentNode !== cards.parentNode)) {
          var after = cards.nextElementSibling;
          if (!(after && after.getAttribute('data-mrb-child-home') === 'end')) {
            cards.parentNode.insertBefore(make('end', false), cards.nextSibling);
          }
        } else if (foot && foot.parentNode) {
          var prev = foot.previousElementSibling;
          if (!(prev && prev.getAttribute('data-mrb-child-home') === 'end')) {
            foot.parentNode.insertBefore(make('end', false), foot);
          }
        }
      }
      // The page redraws parts of itself (a rebuilt KS4 page patches its
      // blocks in place and may drop a node it does not own): re-ensured on
      // every change, idempotently.
      var busy = false;
      new MutationObserver(function () {
        if (busy) { return; }
        busy = true;
        try { ensure(); } finally { busy = false; }
      }).observe(document.body, { subtree: true, childList: true, attributes: true,
                                  attributeFilter: ['style'], characterData: true });
      ensure();
    }
    if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', start); }
    else { start(); }
  })();
} catch (e) {}

/* ── Parent truth (11 Oct 2026): a consumer child's lesson answers ─────────
   Mide's brief: a parent sees exactly what their child did. Every answer a
   family or organisation child gives on a lesson page is sent, as it is
   given, to POST /api/consumer/child/answer — the server stores it with its
   question id, marks a written one, and ties it to the child's work.

   ONLY FOR A CHILD SESSION (MrBadmusConfig.isChildSession — the session's
   own `@children.mrbadmus.internal` address, no network call). A school
   pupil's page installs nothing here: no listener, no global, no request,
   and every other script on the page behaves exactly as before. Rainford
   uses these files.

   Never in the way: one fire-and-forget `keepalive` post per answer, read
   from state the page has ALREADY computed, never blocking or altering it;
   any failure is silent. The page ignores the reply.

   Three page types, one sender (round 3: EVERY answerable shared shape —
   the full list, with ids and sources, is the parent-truth inventory,
   activity_ids.md):
     · KS3 lesson — the ladder: shared/ks3.js dispatches `mrb:answer` at the
       exact points it already knows an answer (only when
       MrBadmusAnswerCapture, set below, exists), and its /api/quiz-score body
       carries this load's `visit_id`. Everything else (the "Start here"
       guess, keyed commits, predictions, "Your turn" calculations): read off
       the page's own markup by one capture-phase click listener.
     · KS4 classic page — the quiz cards (first resolution of each) and the
       matching exercise (each Check), by one capture-phase click listener.
     · KS4 rebuilt (pilot) page — shared/ks4-runtime.js hands every redrawn
       block instance to MrBadmusKS4Tap (set below); each shared block's
       state moving from unanswered to answered is the answer. Read-only.
   No listener ever stops, prevents or alters what the page does.
   ───────────────────────────────────────────────────────────────────────── */
try {
  (function () {
    var c = window.MrBadmusConfig;
    if (!c || !c.BACKEND_URL || !c.AUTH_STORAGE_KEY || typeof c.isChildSession !== 'function') { return; }
    var session = null;
    try { session = JSON.parse(window.localStorage.getItem(c.AUTH_STORAGE_KEY) || 'null'); } catch (e) { return; }
    if (!session || !session.access_token || !c.isChildSession(session)) { return; }

    var path = window.location.pathname || '';
    var pathSlug = (path.split('/').pop() || '').replace(/\.html?$/i, '');
    var CAP_S = 30 * 60;

    function uuid() {
      try { if (window.crypto && typeof window.crypto.randomUUID === 'function') { return window.crypto.randomUUID(); } } catch (e) {}
      var b = [];
      for (var i = 0; i < 16; i += 1) { b.push(Math.floor(Math.random() * 256)); }
      try { if (window.crypto && window.crypto.getRandomValues) { b = Array.prototype.slice.call(window.crypto.getRandomValues(new Uint8Array(16))); } } catch (e) {}
      b[6] = (b[6] & 0x0f) | 0x40; b[8] = (b[8] & 0x3f) | 0x80;
      var h = b.map(function (x) { return (x < 16 ? '0' : '') + x.toString(16); }).join('');
      return h.slice(0, 8) + '-' + h.slice(8, 12) + '-' + h.slice(12, 16) + '-' + h.slice(16, 20) + '-' + h.slice(20);
    }
    var visitId = uuid();
    window.MrBadmusAnswerCapture = { visitId: visitId };

    function clip(v, n) {
      if (v == null) { return null; }
      v = String(v);
      return v.length > n ? v.slice(0, n) : v;
    }

    /* THE page clock. ⊕ 13 Oct 2026 (parent-truth blind run) — ONE
       definition for every lesson-page answer, KS3, KS4 classic and KS4
       rebuilt alike:
         time_spent_seconds = the VISIBLE seconds since the previous
         recorded answer on this page (any question, including an earlier
         attempt at the same one), or — for the first answer — since the
         page first became visible.
       Nothing else restarts it: not a link tap or a card move inside the
       question, not a tick, typing, "Show the next step", opening the
       tutor. (The round-4 clock also restarted on the last pointerdown /
       keydown OUTSIDE the answer's block; the blind run showed that
       inconsistent — a Ks4Chain on a rebuilt ladder rung restarted it on
       every link tap, so a 24 s question was recorded as 1 s, while a
       worked example's "Show the next step" did not. It is gone.) The
       `__block` an answer is posted with is now ignored by the clock.
       MEASURED, never estimated (Mide: "measured active time only, or no
       time at all"): time the tab was hidden inside the window (another
       tab, a locked phone) is taken out, and more than 30 minutes of what
       is left is sent as null — unknown — rather than capped to an
       invented 30.
       ONE PRESS, SEVERAL ANSWERS (a matching or sort Check): the elapsed
       time is split EQUALLY in whole seconds, the remainder going one
       second each to the first answers, so the press's answers always sum
       to exactly the elapsed time and none claims it all. Over the cap,
       every one is null. Each answer keeps its own client_event_id. */
    var lastAt = Date.now();
    var hiddenSince = document.visibilityState === 'hidden' ? Date.now() : null;
    try {
      // Visible from navigation start: the clock starts there. Opened in a
      // background tab (or prerendered): it starts now and the hidden span
      // below takes it forward to the first moment the page is seen.
      if (hiddenSince == null && window.performance && typeof window.performance.now === 'function') {
        lastAt = Date.now() - window.performance.now();
      }
    } catch (e) { /* keep install time */ }
    // Hidden-tab spans, [from, to] in ms, plus the one open now (if any).
    var hiddenSpans = [];
    document.addEventListener('visibilitychange', function () {
      var now = Date.now();
      if (document.visibilityState === 'hidden') {
        if (hiddenSince == null) { hiddenSince = now; }
      } else if (hiddenSince != null) {
        hiddenSpans.push([hiddenSince, now]);
        hiddenSince = null;
        if (hiddenSpans.length > 200) { hiddenSpans.shift(); }
      }
    });
    function visibleMs(from, to) {
      var gone = 0;
      var list = hiddenSpans.slice();
      if (hiddenSince != null) { list.push([hiddenSince, to]); }
      for (var i = 0; i < list.length; i += 1) {
        var a = Math.max(from, list[i][0]), b = Math.min(to, list[i][1]);
        if (b > a) { gone += b - a; }
      }
      return Math.max(0, (to - from) - gone);
    }
    // Whole seconds for `n` answers recorded by one press, summing to the
    // visible time since the previous recorded answer — or all null when
    // that is over the cap. Every recorded answer restarts the clock.
    function spans(n) {
      var now = Date.now();
      var total = Math.round(visibleMs(lastAt, now) / 1000);
      lastAt = now;
      var out = [];
      if (total > CAP_S) {
        for (var z = 0; z < n; z += 1) { out.push(null); }
        return out;
      }
      var each = Math.floor(total / n), rest = total - each * n;
      for (var k = 0; k < n; k += 1) { out.push(each + (k < rest ? 1 : 0)); }
      return out;
    }

    /* ── The outbox (parent truth follow-up, 11 Oct 2026) ──────────────
       No child answer is lost to an expired token or a dropped connection.
       Every answer is WRITTEN AHEAD to localStorage `mrb_answer_outbox_v1`
       before it is sent, and removed only when the server answers 2xx. So a
       401 (an expired token — these pages load no SDK to refresh it), a
       network error, or the tab closing mid-request all leave it queued.
       The queue is flushed, oldest first, with the CURRENT token: when this
       sender installs, after every successful live send, and on any consumer
       page a child opens (consumer/consumer-common.js holds the twin flush,
       with that page's freshly refreshed token). Each body carries a
       `client_event_id` and the `answered_at` of the moment of answering,
       and the server de-duplicates on the id, so a re-send — including one
       of an answer whose first send did land — is safe. Newest 200 kept;
       anything older than 7 days is dropped (the server refuses it). Every
       storage access is wrapped: private mode means "sent live or not at
       all", never an error. ⚠️ The key, the cap, the age limit and the route
       are repeated in consumer-common.js — change them together. */
    var OUTBOX_KEY = 'mrb_answer_outbox_v1', OUTBOX_CAP = 200, OUTBOX_TTL_MS = 7 * 24 * 3600 * 1000;
    var ANSWER_URL = c.BACKEND_URL + '/api/consumer/child/answer';
    function boxRead() {
      try {
        var v = JSON.parse(window.localStorage.getItem(OUTBOX_KEY) || '[]');
        return Array.isArray(v) ? v : [];
      } catch (e) { return []; }
    }
    function boxWrite(list) {
      try {
        if (!list.length) { window.localStorage.removeItem(OUTBOX_KEY); }
        else { window.localStorage.setItem(OUTBOX_KEY, JSON.stringify(list.slice(-OUTBOX_CAP))); }
      } catch (e) { /* private mode, or full — the live send still goes */ }
    }
    function boxFresh(b) {
      var t = b && b.client_event_id && Date.parse(b.answered_at);
      return !!t && (Date.now() - t) < OUTBOX_TTL_MS;
    }
    function boxKeep(body) {
      var list = boxRead().filter(function (b) { return boxFresh(b) && b.client_event_id !== body.client_event_id; });
      list.push(body);
      boxWrite(list);
    }
    function boxDrop(id) {
      boxWrite(boxRead().filter(function (b) { return boxFresh(b) && b.client_event_id !== id; }));
    }
    function token() {
      try {
        var s2 = JSON.parse(window.localStorage.getItem(c.AUTH_STORAGE_KEY) || 'null');
        return (s2 && s2.access_token) || null;
      } catch (e) { return null; }
    }
    // Resolves true only on a 2xx (204 included). `live` sends ride on
    // keepalive so they survive the page going away; a flush does not, as
    // keepalive bodies share a small per-page budget.
    function send(body, tok, live) {
      try {
        return fetch(ANSWER_URL, {
          method: 'POST',
          keepalive: !!live,
          headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + tok },
          body: JSON.stringify(body)
        }).then(function (r) { return !!(r && r.ok); }, function () { return false; });
      } catch (e) { return Promise.resolve(false); }
    }
    var flushing = false;
    var inflight = {};                         // client_event_id → a send this page has not heard back from
    function flush() {
      if (flushing) { return; }
      var tok = token();
      if (!tok) { return; }
      var all = boxRead().filter(boxFresh);
      boxWrite(all);                           // the 7-day drop, persisted
      var queue = all.filter(function (b) { return !inflight[b.client_event_id]; });
      if (!queue.length) { return; }
      flushing = true;
      var i = 0;
      (function next() {
        if (i >= queue.length) { flushing = false; return; }
        var b = queue[i++];
        inflight[b.client_event_id] = 1;
        send(b, tok, false).then(function (ok) {
          delete inflight[b.client_event_id];
          if (!ok) { flushing = false; return; }   // keep it and the rest; try again later
          boxDrop(b.client_event_id);
          next();
        });
      })();
    }

    // The server accepts ids matching ^[a-z0-9:#._-]{1,200}$ and marks 1–20
    // with 0 ≤ marks_scored ≤ marks; anything else is sent as null rather
    // than refused, so an odd authored id never loses the answer itself.
    function safeId(v) {
      if (v == null) { return null; }
      v = String(v).toLowerCase().replace(/[^a-z0-9:#._-]+/g, '-').slice(0, 200);
      return v || null;
    }
    function post(d) {
      var t = ('__t' in d) ? d.__t : spans(1)[0];
      var mk = (typeof d.marks === 'number' && isFinite(d.marks)) ? Math.round(d.marks) : null;
      if (mk !== null && (mk < 1 || mk > 20)) { mk = null; }
      var ms = (mk !== null && typeof d.marks_scored === 'number' && isFinite(d.marks_scored))
        ? Math.max(0, Math.min(mk, Math.round(d.marks_scored))) : null;
      var body = {
        client_event_id: uuid(),
        answered_at: new Date().toISOString(),
        visit_id: visitId,
        key_stage: d.key_stage,
        path: path,
        lesson_slug: d.lesson_slug || pathSlug,
        question_id: safeId(d.question_id),
        rung: d.rung == null ? null : String(d.rung),
        kind: d.kind,
        question_text: clip(d.question_text || '', 2000),
        answer: clip(d.answer, 5000),
        correct_answer: clip(d.correct_answer, 5000),
        is_correct: typeof d.is_correct === 'boolean' ? d.is_correct : null,
        // The server takes up to 20 points of up to 600 characters each and
        // refuses anything longer, so they are cut to fit here rather than
        // losing the answer to a 400.
        criteria: Array.isArray(d.criteria)
          ? d.criteria.slice(0, 20).map(function (x) { return clip(x, 600); })
          : null,
        // ⊕ 13 Oct 2026: a calculation's Answer line and the model's, for the
        // server's value-and-unit check (calcOf). Absent everywhere else.
        calc: d.calc && typeof d.calc === 'object'
          ? { answer: clip(d.calc.answer || '', 600), key: clip(d.calc.key || '', 600),
              point: (typeof d.calc.point === 'number' && d.calc.point >= 0) ? Math.floor(d.calc.point) : null }
          : null,
        marks: mk,
        // Round 3: what the PAGE awarded, where the page awards marks (a KS4
        // rung's "3 marks", scored whole or not). Null where it awards none.
        marks_scored: ms,
        // Round 3: the child checked their own work against a worked answer
        // or a reveal and nothing judged it. Stored UNMARKED — never correct.
        self_checked: d.self_checked === true,
        // Round 4: what the page showed after the commit (a "Think again"
        // reveal), kept out of correct_answer. Optional; the server may
        // ignore it.
        explanation: d.explanation == null ? null : clip(d.explanation, 5000),
        time_spent_seconds: t
      };
      boxKeep(body);                           // written ahead: queued until the server has it
      var tok = token();
      if (!tok) { return; }
      inflight[body.client_event_id] = 1;
      send(body, tok, true).then(function (ok) {
        delete inflight[body.client_event_id];
        if (!ok) { return; }                   // stays queued
        boxDrop(body.client_event_id);
        flush();
      });
    }

    /* ⊕ 13 Oct 2026 — a written CALCULATION (KS3 "Your turn", KS4 Ks4Cfifa
       and Ks4Steps "attempt"): marked, never self-checked. The scheme is the
       model's own lines, one point and one mark a line — the list the page
       itself shows under "tick what you had" — and `calc` names the Answer
       line, so the server can check the final value and unit by key
       (consumer/answers.js calcVerdict) beside the marker. The child's ticks
       are not sent: they are never the mark. `model` and `labels` are the
       model's lines with and without their labels; `mine` the child's raw
       lines, in the same order. */
    function calcOf(d, model, labels, mine) {
      var ai = -1;
      for (var i = 0; i < labels.length; i += 1) { if (/^answer\b/i.test(String(labels[i] || '').trim())) { ai = i; } }
      if (ai < 0) { ai = model.length - 1; }
      d.criteria = model;
      d.marks = model.length;
      d.self_checked = false;
      if (ai >= 0 && model[ai] != null) {
        var keyLine = String(model[ai]).replace(/^[^:]*:\s*/, '');
        d.calc = { answer: mine[ai] == null ? '' : String(mine[ai]), key: keyLine, point: ai };
      }
      return d;
    }

    // Several answers from ONE press: the elapsed time is split (see the clock).
    function postAll(list) {
      if (!list.length) { return; }
      var ts = spans(list.length);
      list.forEach(function (d, k) { d.__t = ts[k]; post(d); });
    }

    // Anything an earlier page could not deliver, now — after the page has
    // settled, so it never competes with the lesson loading.
    setTimeout(flush, 2000);

    /* ── KS3: the ladder's own announcements ── */
    document.addEventListener('mrb:answer', function (e) {
      if (!e || !e.detail) { return; }
      var d = e.detail;
      d.time_spent_seconds = null;                 // the page clock decides
      try { d.__block = document.querySelector('.ks3-rung[data-rung="' + d.rung + '"]'); } catch (err) { d.__block = null; }
      post(d);
    });

    function txt(el) { return el ? (el.textContent || '').replace(/\s+/g, ' ').trim() : ''; }
    function later(fn) { setTimeout(function () { try { fn(); } catch (e) { /* never breaks a page */ } }, 0); }
    var lastText = {};                  // question_id → the last written text sent

    /* ── KS3 lesson: everything outside the ladder that takes an answer ──
       Read from the page's own markup, in the capture phase, before the
       page's handler runs; never stopped, prevented or altered. See
       docs: scratchpad truth/activity_ids.md for the inventory.
         · the "Start here" guess and every other keyed commit
           ([data-keyedblock]): every pick that changes the choice (⊕ 13 Oct
           2026 — the block stays changeable, so each is an attempt). The hook's
           reply opens "Good guess." on the option the science says is right
           (build_ks3.py `_hook_guess`), so the hook is judged; any other
           keyed commit is a commitment the page reveals against (R3: KS3
           activities never mark), so it is sent self_checked.
         · a prediction ([data-activity] that is not an instrument, with
           options and a reveal — shared/ks3.js `wirePredictions`): every
           changed pick, self_checked, with the reveal as what the page showed.
         · "Your turn" five-line calculations (data-p<N>cfa): each time the
           check opens the worked lines, the child's five lines — ⊕ 13 Oct
           2026 MARKED (calcOf): the model's lines are the scheme and the
           Answer line is checked by value and unit. The child's "I had this"
           ticks are never the mark and are not sent.
       Everything else on a KS3 page is listed in the inventory as not yet
       captured, with the reason. */
    if (/^\/ks3\//.test(path)) {
      var ks3Slug = function () {
        var l = document.querySelector('[data-lesson]');
        return (l && l.getAttribute('data-lesson')) || pathSlug;
      };
      var optLabel = function (b) { return txt(b.querySelector('.ks3-opt-label') || b); };
      // What the child was asked: the commit line where the block has one,
      // else the block's own headings and paragraphs above its options
      // (a "Think again" block: the quoted idea, then the ask).
      var promptOf = function (sec) {
        var c = sec.querySelector('.ks3-commit');
        if (c) { return txt(c); }
        var out = [], kids = sec.children || [];
        for (var i = 0; i < kids.length; i += 1) {
          var el = kids[i];
          if (el.querySelector && (el.matches('.ks3-options') || el.querySelector('.ks3-option'))) { break; }
          if (/^(P|H2|H3)$/.test(el.tagName) && !el.classList.contains('ks3-eyebrow')) { out.push(txt(el)); }
          else if (el.querySelector) {
            var q = el.querySelectorAll('h2, h3, p:not(.ks3-eyebrow)');
            for (var j = 0; j < q.length; j += 1) { out.push(txt(q[j])); }
          }
        }
        return out.filter(Boolean).join(' ');
      };
      var cfaPrefix = function (btn) {
        var a = btn.attributes || [];
        for (var i = 0; i < a.length; i += 1) {
          var m = /^(data-p\d+cfa)-check$/.exec(a[i].name);
          if (m) { return m[1]; }
        }
        return null;
      };
      /* ── Round 4: QUESTION-SHAPED instruments (activity_ids.md, appendix B) ──
         Two generic adapters, keyed on markup the instruments already share,
         never on one kind's internals. Only the kinds classified
         question-shaped are listed; an exploration's picks are not answers.

         Adapter A — commit options. A button carrying `data-<p>-opt|pick|
         gopt|verdict|judge` (or `.ks3-option`) inside such a block is a
         committed choice. Its question UNIT is the nearest ancestor carrying
         `data-<p>-card|item|side|row|case|cell|q|sample|scenario|panel|seg|
         test`, else the button's own `data-<p>-of`, else the `<unit>:` prefix
         of its value, else the whole block. n = the unit's order among the
         block's units (authored order). The first commit per unit is sent, and every later
         one the instrument visibly takes (answerA, ⊕ 13 Oct 2026).
         Right/wrong comes from the markup where the markup carries it —
         `data-correct` on the option, `data-<p>-want-<unit>` on the block,
         `data-<p>-is` in the unit, `data-answer` on the unit's row, or the
         is-correct / is-right / is-wrong class the page puts on the option —
         else the answer is sent self_checked with what the page revealed in
         `explanation`.

         Adapter B5C — the `wireB5Commit` family: pick a part, choose its
         job, press Check. Right/wrong from the reveal's `data-answer`. */
      var KIND_A = {"ks3-cellbench-block":1,"ks3-removal-block":1,"ks3-sc-block":1,"ks3-meters-block":1,"ks3-clinic-block":1,"ks3-bottle-block":1,"ks3-grain-block":1,"ks3-gapfill-block":1,"ks3-rgrid-block":1,"ks3-dcomp-block":1,"ks3-rword-block":1,"ks3-iboard-block":1,"ks3-fault-block":1,"ks3-board":1,"ks3-cpair-block":1,"ks3-pdeck-block":1,"ks3-psort-block":1,"ks3-tbench-block":1,"ks3-ml-block":1,"ks3-fb-block":1,"ks3-esort-block":1,"ks3-seq-block":1,"ks3-rockb-block":1,"ks3-prop-block":1,"ks3-ctube-block":1,"ks3-touch-block":1,"ks3-pcards-block":1,"ks3-ruse-block":1,"ks3-tsort-block":1,"ks3-pass-block":1,"ks3-spath-block":1,"ks3-plan-block":1,"ks3-sort":1,"ks3-switch-block":1,"ks3-mb-block":1,"ks3-solid-block":1,"ks3-chain-block":1,"ks3-arr-block":1,"ks3-eqr-block":1,"ks3-rplan-block":1,"ks3-raudit-block":1,"ks3-mchoice-block":1,"ks3-cev-block":1,"ks3-hgrid-block":1,"ks3-rstop-block":1,"ks3-gplot-block":1,"ks3-spair-block":1,"ks3-rtotal-block":1,"ks3-wsort-block":1,"ks3-eyecam-block":1,"ks3-cplot-block":1,"ks3-chpair-block":1,"ks3-vchain-block":1,"ks3-sab-block":1,"ks3-cl-block":1,"ks3-vp-block":1,"ks3-tb-block":1,"ks3-rd-block":1,"ks3-ajudge-block":1,"ks3-namer-block":1,"ks3-dish-block":1,"ks3-claim-block":1,"ks3-euse-block":1,"ks3-critique-block":1,"ks3-edep-block":1,"ks3-fcard-block":1,"ks3-tuber-block":1,"ks3-mplace-block":1,"ks3-hrig-block":1};
      var KIND_B5C = {"ks3-xpanel-block":1,"ks3-fjobs-block":1,"ks3-dsort-block":1,"ks3-xbench-block":1,"ks3-jmatch-block":1};
      var OPT_RE = /^data-([a-z0-9]+)-(opt|pick|gopt|verdict|judge)$/;
      var UNIT_RE = /^data-[a-z0-9]+-(card|item|side|row|case|cell|q|sample|scenario|panel|seg|test)$/;
      var SHOWN_RE = /-(reveal|answer|note|why|verdict|right|wrong|sums)$/;
      var kindOf = function (sec, map) {
        var cl = sec.classList || [];
        for (var i = 0; i < cl.length; i += 1) { if (map[cl[i]]) { return cl[i]; } }
        return null;
      };
      var optAttr = function (btn) {
        var a = btn.attributes || [];
        for (var i = 0; i < a.length; i += 1) {
          var m = OPT_RE.exec(a[i].name);
          if (m) { return { prefix: m[1], value: a[i].value || '' }; }
        }
        return null;
      };
      var isOption = function (btn) {
        return !!(optAttr(btn) || (btn.classList && btn.classList.contains('ks3-option')));
      };
      var unitOf = function (btn, sec) {
        for (var el = btn.parentNode; el && el !== sec; el = el.parentNode) {
          var a = el.attributes || [];
          for (var i = 0; i < a.length; i += 1) {
            if (UNIT_RE.test(a[i].name)) { return { el: el, key: a[i].name + '=' + a[i].value }; }
          }
        }
        var oa = optAttr(btn);
        if (oa) {
          var of = btn.getAttribute('data-' + oa.prefix + '-of');
          if (of) { return { el: null, key: 'of=' + of }; }
          if (oa.value.indexOf(':') > 0) { return { el: null, key: 'v=' + oa.value.split(':')[0] }; }
        }
        return { el: sec, key: 'block' };
      };
      var unitNo = function (sec, key) {
        var seen = [], bs = sec.querySelectorAll('button');
        for (var i = 0; i < bs.length; i += 1) {
          if (!isOption(bs[i])) { continue; }
          var k = unitOf(bs[i], sec).key;
          if (seen.indexOf(k) < 0) { seen.push(k); }
        }
        var ix = seen.indexOf(key);
        return ix < 0 ? 1 : ix + 1;
      };
      var visibleText = function (root, test) {
        var out = [], els = root.querySelectorAll('*');
        for (var i = 0; i < els.length; i += 1) {
          var el = els[i];
          if (el.closest('button') || el.closest('[hidden]') || el.tagName === 'TEMPLATE' || el.closest('template')) { continue; }
          if (test(el)) { var t = txt(el); if (t && out.indexOf(t) < 0) { out.push(t); } }
        }
        return out.join(' ');
      };
      var sentUnits = {};
      // What a press visibly did to its option: chosen (aria-pressed) and the
      // verdict / chosen classes the instruments put on it.
      var CHOSEN_CLS = ['is-correct', 'is-right', 'is-wrong', 'is-chosen', 'is-picked', 'is-selected', 'is-on'];
      var markOf = function (b) {
        var out = b.getAttribute('aria-pressed') === 'true' ? 'p' : '';
        for (var i = 0; i < CHOSEN_CLS.length; i += 1) { if (b.classList && b.classList.contains(CHOSEN_CLS[i])) { out += '|' + CHOSEN_CLS[i]; } }
        return out;
      };
      var answerA = function (btn, sec, slug) {
        var u = unitOf(btn, sec);
        var act = sec.getAttribute('data-activity') || 'block';
        var id = slug + '#' + act + '-' + unitNo(sec, u.key);
        // ⊕ 13 Oct 2026 (every attempt): the first commit in a unit is sent
        // as before. A LATER press in the same unit is a new attempt only
        // when the instrument took it — the option was not already the
        // chosen one and the page's own handler marked it chosen (or put a
        // verdict on it) a tick later. A press an instrument ignores (a
        // locked unit) changes nothing on the page and sends nothing.
        var repeat = !!sentUnits[id];
        var markBefore = markOf(btn);
        if (repeat && markBefore.charAt(0) === 'p') { return; }
        sentUnits[id] = 1;
        // A unit named only by an attribute (`data-<p>-of`, `<unit>:value`)
        // has no element of its own: its scope is the box holding its picks.
        var scope = u.el || (btn.parentElement && btn.parentElement.parentElement) || sec;
        if (!sec.contains(scope)) { scope = sec; }
        var prompt = scope !== sec
          ? visibleText(scope, function (el) {
              return /^(P|H2|H3|H4|LI)$/.test(el.tagName) && !el.hasAttribute('data-count') &&
                     !SHOWN_RE.test(Object.keys(el.dataset || {}).join('-'));
            })
          : promptOf(sec);
        var oa = optAttr(btn), v = oa ? oa.value : (btn.getAttribute('data-i') || '');
        var uk = v.indexOf(':') > 0 ? v.split(':')[0] : '', vv = v.indexOf(':') > 0 ? v.split(':').slice(1).join(':') : v;
        var opts = Array.prototype.filter.call(scope.querySelectorAll('button'), isOption);
        var valueOf = function (b) { var o = optAttr(b); var x = o ? o.value : (b.getAttribute('data-i') || ''); return x.indexOf(':') > 0 ? x.split(':').slice(1).join(':') : x; };
        var byValue = function (want) { for (var i = 0; i < opts.length; i += 1) { if (valueOf(opts[i]) === want) { return opts[i]; } } return null; };
        var good = null, verdict = null, hasDC = false;
        for (var j = 0; j < opts.length; j += 1) { if (opts[j].hasAttribute('data-correct')) { hasDC = true; } }
        if (hasDC) {
          for (var i = 0; i < opts.length; i += 1) { var dc = opts[i].getAttribute('data-correct'); if (dc && dc !== '0' && dc !== 'false') { good = opts[i]; } }
          if (good) { verdict = good === btn; }
        }
        if (verdict === null && oa && uk) {
          var w = sec.querySelector('[data-' + oa.prefix + '-want-' + uk + ']');
          if (w) { good = byValue(w.getAttribute('data-' + oa.prefix + '-want-' + uk)); verdict = w.getAttribute('data-' + oa.prefix + '-want-' + uk) === vv; }
        }
        if (verdict === null && oa) {
          var is = scope.querySelector('[data-' + oa.prefix + '-is]');
          if (is) { good = byValue(is.getAttribute('data-' + oa.prefix + '-is')); verdict = is.getAttribute('data-' + oa.prefix + '-is') === vv; }
        }
        if (verdict === null) {
          var row = btn.closest('[data-answer]');
          if (row && sec.contains(row) && row !== btn) { good = byValue(row.getAttribute('data-answer')); verdict = row.getAttribute('data-answer') === vv; }
        }
        later(function () {
          if (repeat) {
            var markAfter = markOf(btn);
            if (!markAfter || markAfter === markBefore) { return; }
          }
          if (verdict === null && btn.classList) {
            if (btn.classList.contains('is-correct') || btn.classList.contains('is-right')) { verdict = true; good = btn; }
            else if (btn.classList.contains('is-wrong')) {
              verdict = false;
              for (var i = 0; i < opts.length; i += 1) { if (opts[i].classList.contains('is-correct') || opts[i].classList.contains('is-right')) { good = opts[i]; } }
            }
          }
          var d = { __block: scope, key_stage: 'KS3', lesson_slug: slug, question_id: id, rung: null,
                    kind: 'choice', question_text: prompt, answer: optLabel(btn),
                    correct_answer: good ? optLabel(good) : null,
                    is_correct: verdict,
                    explanation: visibleText(scope, function (el) {
                      var a = el.attributes || [];
                      for (var i = 0; i < a.length; i += 1) { if (/^data-/.test(a[i].name) && SHOWN_RE.test(a[i].name)) { return true; } }
                      return false;
                    }) || null };
          if (verdict === null) { d.self_checked = true; }
          post(d);
        });
      };
      var answerB5C = function (chk, sec, slug) {
        var w = chk.closest('[data-b5c]');
        if (!w) { return; }
        var item = w.getAttribute('data-item') || '';
        var act = sec.getAttribute('data-activity') || 'block';
        var tabs = w.querySelectorAll('[data-b5c-pick]'), n = 1;
        for (var i = 0; i < tabs.length; i += 1) { if (tabs[i].getAttribute('data-b5c-pick') === item) { n = i + 1; } }
        var id = slug + '#' + act + '-' + n;
        if (sentUnits[id]) { return; }
        var pick = w.querySelector('.ks3-b5c-opt[data-owner="' + item + '"][aria-pressed="true"]');
        if (!pick) { return; }
        sentUnits[id] = 1;
        var rev = w.querySelector('[data-b5c-reveal="' + item + '"]');
        var right = rev ? rev.getAttribute('data-answer') : null;
        var good = right ? w.querySelector('.ks3-b5c-opt[data-owner="' + item + '"][data-opt="' + right + '"]') : null;
        var name = w.querySelector('.ks3-b5c-item[data-for="' + item + '"] .ks3-b5c-name');
        post({ __block: w, key_stage: 'KS3', lesson_slug: slug, question_id: id, rung: null, kind: 'choice',
               question_text: (txt(name) ? txt(name) + ' — ' : '') + txt(w.querySelector('.ks3-b5c-ask')),
               answer: optLabel(pick), correct_answer: good ? optLabel(good) : null,
               is_correct: right == null ? null : pick.getAttribute('data-opt') === right,
               self_checked: right == null });
      };
      document.addEventListener('click', function (e) {
        try {
          var t = e.target;
          if (!t || !t.closest) { return; }
          var slug = ks3Slug();
          // Round 4: question-shaped instruments (adapters A and B5C above).
          var bsec = t.closest('[data-instrument]');
          if (bsec && !bsec.hasAttribute('data-keyedblock')) {
            if (kindOf(bsec, KIND_B5C)) {
              var b5 = t.closest('[data-b5c-check]');
              if (b5 && !b5.disabled) { answerB5C(b5, bsec, slug); }
              return;
            }
            if (kindOf(bsec, KIND_A)) {
              var ob = t.closest('button');
              if (ob && !ob.disabled && isOption(ob) && !ob.closest('.ks3-ladder')) { answerA(ob, bsec, slug); }
              return;
            }
          }
          var opt = t.closest('.ks3-option');
          if (opt && !opt.disabled && !opt.closest('.ks3-ladder')) {
            var sec = opt.closest('[data-activity]');
            if (!sec) { return; }
            // ⊕ 13 Oct 2026 (Mide: every attempt is recorded): a keyed
            // commit and a prediction both stay CHANGEABLE (shared/ks3.js
            // wireKeyedCommit / wirePredictions — "Good guess." after a wrong
            // "Fair guess." is the page working). So every press that CHANGES
            // the choice is a new answer — a new row, its own client_event_id
            // (post), the server numbering the attempt. A press on the option
            // already chosen changes nothing and is not sent. Read in the
            // capture phase, so aria-pressed is still the PREVIOUS choice.
            if (opt.getAttribute('aria-pressed') === 'true') { return; }
            var act = sec.getAttribute('data-activity') || '';
            var keyed = sec.hasAttribute('data-keyedblock') ? sec.querySelector('[data-keyed]') : null;
            if (keyed && keyed.contains(opt)) {
              if (act === 'hook') {
                var good = null, mine = null;
                var opts = keyed.querySelectorAll('.ks3-option');
                for (var i = 0; i < opts.length; i += 1) {
                  var di = opts[i].getAttribute('data-i');
                  var word = txt(keyed.querySelector('.ks3-keyed-reply[data-reply="' + di + '"] strong'));
                  if (word.indexOf('Good guess') === 0) { good = opts[i]; }
                  if (opts[i] === opt) { mine = word; }
                }
                post({ __block: sec, key_stage: 'KS3', lesson_slug: slug, question_id: slug + '#start', rung: null,
                       kind: 'choice', question_text: promptOf(sec), answer: optLabel(opt),
                       correct_answer: good ? optLabel(good) : null,
                       is_correct: mine == null || good == null ? null : mine.indexOf('Good guess') === 0 });
              } else {
                post({ __block: sec, key_stage: 'KS3', lesson_slug: slug, question_id: slug + '#' + act, rung: null,
                       kind: 'choice', question_text: promptOf(sec), answer: optLabel(opt),
                       correct_answer: null, is_correct: null, self_checked: true });
              }
              return;
            }
            if (!sec.hasAttribute('data-instrument') && sec.querySelector('[data-reveal]')) {
              // No option is authored as right (ks3_data `kind: predict` has
              // `options` and `reveal`, never an answer key), so
              // correct_answer stays null and the reveal goes in `explanation`.
              post({ __block: sec, key_stage: 'KS3', lesson_slug: slug, question_id: slug + '#' + act, rung: null,
                     kind: 'choice', question_text: promptOf(sec), answer: optLabel(opt),
                     correct_answer: null, explanation: txt(sec.querySelector('[data-reveal]')) || null,
                     is_correct: null, self_checked: true });
            }
            return;
          }
          var btn = t.closest('button');
          if (!btn || btn.disabled) { return; }
          var pre = cfaPrefix(btn);
          if (!pre) { return; }
          var q = btn.closest('[' + pre + '-q]');
          var csec = btn.closest('[data-activity]');
          if (!q || !csec) { return; }
          var rev = q.querySelector('[' + pre + '-reveal]');
          if (!rev || !rev.hasAttribute('hidden')) { return; }   // already open: not a new submission
          later(function () {
            if (rev.hasAttribute('hidden')) { return; }          // the page refused (nothing to check yet)
            var labelFor = function (inp) {
              var l = inp.id ? q.querySelector('label[for="' + inp.id + '"]') : null;
              return l ? txt(l) : '';
            };
            var ins = q.querySelectorAll('[' + pre + '-input]');
            var mine = [], mineVals = [];
            for (var i = 0; i < ins.length; i += 1) {
              mineVals.push((ins[i].value || '').trim());
              mine.push((labelFor(ins[i]) ? labelFor(ins[i]) + ': ' : '') + (ins[i].value || '').trim());
            }
            var rows = q.querySelectorAll('[' + pre + '-line]');
            var model = [], labs = [];
            for (var k = 0; k < rows.length; k += 1) {
              var row = rows[k].parentNode;
              var lab = row ? txt(row.querySelector('.ks3-cfa-label')) : '';
              labs.push(lab);
              model.push((lab ? lab + ': ' : '') + txt(rows[k]));
            }
            var n = parseInt(q.getAttribute(pre + '-q'), 10);
            // ⊕ 13 Oct 2026 (Mide: a written answer is MARKED when it is
            // submitted; the child's own ticks are never the mark): the five
            // lines go to the marker with the model's five lines as the
            // scheme, one mark a line, and the Answer line is checked against
            // the model's answer by value and unit (calcOf).
            post(calcOf({ __block: q, key_stage: 'KS3', lesson_slug: ks3Slug(),
                   question_id: ks3Slug() + '#' + (csec.getAttribute('data-activity') || 'your-turn') + '-' + ((isNaN(n) ? 0 : n) + 1),
                   rung: null, kind: 'written', question_text: txt(q.querySelector('[' + pre + '-head]')),
                   answer: mine.join('\n'), correct_answer: model.join('\n'),
                   is_correct: null }, model, labs, mineVals));
          });
        } catch (err) { /* capture never breaks a lesson */ }
      }, true);
      return;
    }

    if (!/^\/(combined|triple)\//.test(path)) { return; }

    /* ── KS4 classic: the first resolution of each quiz card ── */
    var settled = typeof WeakSet === 'function' ? new WeakSet() : null;
    var matchSent = {};                 // question_id → the slot last sent
    document.addEventListener('click', function (e) {
      try {
        var btn = e.target && e.target.closest ? e.target.closest('.quiz-opt') : null;
        if (btn && !btn.disabled) {
          var card = btn.closest('.quiz-card');
          if (!card || !card.hasAttribute('data-answer') || !btn.hasAttribute('data-oi')) { return; }
          // The card's own script marks it once and ignores every later click
          // (`card.dataset.answered`), so only the first resolution is sent.
          if (card.hasAttribute('data-answered') || (settled && settled.has(card))) { return; }
          if (settled) { settled.add(card); }
          var opts = card.querySelectorAll('.quiz-opt');
          var right = parseInt(card.getAttribute('data-answer'), 10);
          var picked = parseInt(btn.getAttribute('data-oi'), 10);
          var q = card.querySelector('.q-text');
          post({
            __block: card, key_stage: 'KS4', lesson_slug: pathSlug, question_id: null, rung: null,
            kind: 'choice',
            question_text: q ? q.textContent : '',
            answer: (btn.textContent || '').trim(),
            correct_answer: opts[right] ? (opts[right].textContent || '').trim() : null,
            is_correct: picked === right
          });
          return;
        }
        /* The matching exercise: on "Check Answers", every placed card whose
           slot changed since it was last sent. The page's checkMatching()
           runs first (this reads its verdict classes a tick later). */
        var chk = e.target && e.target.closest ? e.target.closest('.match-check-btn') : null;
        if (!chk) { return; }
        var m = /checkMatching\('([^']*)'/.exec(chk.getAttribute('onclick') || '');
        var st = (m && m[1]) || pathSlug;
        var scope = chk.closest('.section') || document;
        later(function () {
          var drops = scope.querySelectorAll('.match-drop'), batch = [];
          for (var i = 0; i < drops.length; i += 1) {
            var placed = drops[i].querySelector('.match-def');
            if (!placed) { continue; }
            var n = parseInt(placed.getAttribute('data-index'), 10);
            var id = 'ks4c:' + st + ':match-' + ((isNaN(n) ? i : n) + 1);
            var slot = drops[i].getAttribute('data-accepts');
            if (matchSent[id] === slot) { continue; }
            matchSent[id] = slot;
            var g = placed.getAttribute('data-group');
            var home = scope.querySelector('.match-drop[data-accepts-group="' + g + '"]');
            batch.push({
              key_stage: 'KS4', lesson_slug: pathSlug, question_id: id, rung: null, kind: 'choice',
              question_text: txt(placed),
              answer: txt(drops[i].parentNode && drops[i].parentNode.querySelector('.match-term')),
              correct_answer: home ? txt(home.parentNode && home.parentNode.querySelector('.match-term')) : null,
              is_correct: drops[i].classList.contains('match-correct')
            });
          }
          postAll(batch);   // one Check, the time split across its cards
        });
      } catch (err) { /* capture never breaks the quiz */ }
    }, true);

    /* ── KS4 rebuilt (pilot) page: every shared block that takes an answer ──
       shared/ks4-runtime.js hands each redrawn block instance to the tap; a
       block's state moving from "not answered" to "answered" is the answer.
       Read-only. Ids number a block by its AUTHORED order among blocks of
       the same kind in the lesson's template (not DOM order), 1-based.
       A lesson's own bespoke activities (Design's per-lesson logic, e.g.
       "Build the two cells") have no shared shape and are not captured —
       see the inventory. */
    var prevOf = typeof WeakMap === 'function' ? new WeakMap() : null;
    var sortSent = {};                         // question_id → the box last sent
    function ownerOf(api) {
      var el = api.host && api.host.parentNode;
      while (el) { if (el.__mrbKs4) { return el.__mrbKs4; } el = el.parentNode; }
      return null;
    }
    function rootLevel(api) { var o = ownerOf(api); return !!o && o.comp === undefined; }
    function nth(api) {
      var owner = ownerOf(api);
      var want = api.host && api.host.getAttribute ? parseInt(api.host.getAttribute('data-dc-tpl'), 10) : NaN;
      if (!owner || !owner.template || isNaN(want)) { return 1; }
      var list = [];
      (function walk(n) {
        if (!n || typeof n !== 'object') { return; }
        if (Array.isArray(n)) { n.forEach(walk); return; }
        if (n.t === 'child' && n.comp === api.comp) { list.push(n.i); }
        for (var k in n) {
          if (k !== 'a' && Object.prototype.hasOwnProperty.call(n, k) && n[k] && typeof n[k] === 'object') { walk(n[k]); }
        }
      })(owner.template.roots);
      var ix = list.indexOf(want);
      return ix < 0 ? 1 : ix + 1;
    }
    function kids(api, name) {
      var out = [];
      if (!api.host || !api.host.querySelectorAll) { return out; }
      var nodes = api.host.querySelectorAll('[data-dc-tpl]');
      for (var i = 0; i < nodes.length; i += 1) {
        var a = nodes[i].__mrbKs4;
        if (a && a !== api && a.comp === name && ownerOf(a) === api) { out.push(a); }
      }
      return out;
    }
    function optText(o) { return o && o.text != null ? String(o.text) : null; }
    function rightOpt(opts) {
      for (var i = 0; i < (opts || []).length; i += 1) { if (opts[i] && opts[i].correct) { return opts[i]; } }
      return null;
    }
    function chainAnswer(chainApi, links, herr) {
      var ids = chainApi && chainApi.logic && chainApi.logic.state ? (chainApi.logic.state.chain || []) : [];
      return ids.map(function (id) {
        var n = parseInt(String(id).slice(1), 10);
        if (String(id).charAt(0) === 'L') { return links[n] == null ? '' : links[n]; }
        return herr[n] && herr[n].text != null ? herr[n].text : '';
      }).join('\n');
    }
    function schemeOf(it) {
      return (it.points && it.points.length)
        ? it.points.slice()
        : (it.levels || []).map(function (lv) { return (lv.label ? lv.label + ': ' : '') + (lv.text || ''); });
    }
    function writtenOut(d, text) {
      // The same words sent twice are one answer.
      if (lastText[d.question_id] === text) { return; }
      lastText[d.question_id] = text;
      d.answer = text;
      post(d);
    }
    function calcAnswer(it, conv, num, unit) {
      var c = it.convOptions || [];
      return (c[conv] != null ? c[conv] + ' → ' : '') + String(num || '').trim() + (unit ? ' ' + unit : '');
    }
    function calcRight(it) {
      var c = it.convOptions || [];
      return (c[it.convAnswer] != null ? c[it.convAnswer] + ' → ' : '') +
             (it.answer == null ? '' : String(it.answer)) + (it.unit ? ' ' + it.unit : '');
    }
    /* The ROUTE is part of every pilot id (Commander's ruling, 11 Oct 2026):
       128 of 308 pilot pages choose content by route (`hi ? … : …`), so a
       position-only id could name two different questions. The two letters
       come from the page path: /combined|triple/ → c|t, /foundation|higher/
       → f|h, so ch, cf, th, tf. One id is always exactly one question.
       ⚠️ Joined with ':' — `ks4:<slug>:<route>#…` — not the '@' first
       ruled: the server refuses any id outside ^[a-z0-9:#._-]{1,200}$, and
       ':' is already the separator in `ks4q:<slug>:<hash>`. */
    var routeSeg = (function () {
      var m = /^\/(combined|triple)\/(foundation|higher)\//.exec(path);
      return m ? ':' + m[1].charAt(0) + m[2].charAt(0) : '';
    })();
    function pilotId(slug, id) { return 'ks4:' + slug + routeSeg + '#' + id; }
    var curBlock = null;                       // the instance the tap is handling
    function base(id, rung) {
      return { __block: curBlock, key_stage: 'KS4', lesson_slug: pathSlug, question_id: pilotId(pathSlug, id),
               rung: rung || null, criteria: null, marks: null, correct_answer: null, is_correct: null };
    }

    var HANDLERS = {
      Ks4Guess: function (api, s, prev) {
        if (!rootLevel(api) || prev.pick != null || s.pick == null) { return; }
        var p = api.logic.props || {}, o = (p.options || [])[s.pick] || {};
        var d = base('start');
        d.kind = 'choice'; d.question_text = p.question || '';
        d.answer = optText(o); d.correct_answer = optText(rightOpt(p.options));
        d.is_correct = !!o.correct;
        post(d);
      },
      Ks4Choice: function (api, s, prev) {
        if (!rootLevel(api) || prev.pick != null || s.pick == null) { return; }
        var p = api.logic.props || {}, opts = p.options || [], o = opts[s.pick] || {};
        var graded = opts.some(function (x) { return x && x.correct !== undefined; });
        var d = base('choice-' + nth(api));
        d.kind = 'choice'; d.question_text = p.prompt || '';
        d.answer = optText(o);
        if (graded) { d.correct_answer = optText(rightOpt(opts)); d.is_correct = !!o.correct; }
        else { d.explanation = p.reveal || null; d.self_checked = true; }
        post(d);
      },
      Ks4Sort: function (api, s, prev) {
        if (!rootLevel(api) || prev.checked || !s.checked) { return; }
        var p = api.logic.props || {}, k = nth(api), bins = p.bins || [];
        var binLabel = function (id) { for (var j = 0; j < bins.length; j += 1) { if (bins[j].id === id) { return bins[j].label; } } return null; };
        var batch = [];
        (p.items || []).forEach(function (it, i) {
          var at = (s.placed || {})[i];
          if (at === undefined) { return; }
          var d = base('sort-' + k + '-' + (i + 1));
          // A re-check (after moving cards) sends only the cards whose box
          // changed since they were last sent — an unmoved card is the same
          // answer, not a new attempt (as the classic matching exercise).
          if (sortSent[d.question_id] === at) { return; }
          sortSent[d.question_id] = at;
          d.kind = 'choice';
          d.question_text = (p.prompt || p.title || 'Sort') + ' — ' + (it.text || '');
          d.answer = binLabel(at); d.correct_answer = binLabel(it.bin);
          d.is_correct = at === it.bin;
          batch.push(d);
        });
        postAll(batch);                // one Check, the time split across its cards
      },
      Ks4QuizBank: function (api, s, prev) {
        if (!rootLevel(api)) { return; }
        var p = api.logic.props || {};
        var all = (p.questions || []).filter(Boolean).slice(0, 5);
        var was = prev.picks || {};
        Object.keys(s.picks || {}).forEach(function (i) {
          if (was[i] !== undefined) { return; }
          var q = all[i]; if (!q) { return; }
          var o = (q.options || [])[s.picks[i]] || {};
          var d = base('quiz-' + nth(api) + '-' + (+i + 1));
          // The practice set IS the subtopic's authored quiz (ks4-lib.js
          // `bank()` over all_subtopics_*.py), route by route — the same
          // items a classic page's cards carry. So it takes the classic id:
          // null here, and the server derives `ks4q:<slug>:<sha1 of the
          // normalised text>`, which is the same question on every route.
          d.question_id = null;
          d.kind = 'choice'; d.question_text = q.prompt || '';
          d.answer = optText(o); d.correct_answer = optText(rightOpt(q.options));
          d.is_correct = !!o.correct;
          post(d);
        });
      },
      Ks4Cfifa: function (api, s, prev) {
        if (!rootLevel(api)) { return; }
        var p = api.logic.props || {}, defs = p.questions || [], was = prev.q || {}, k = nth(api);
        Object.keys(s.q || {}).forEach(function (i) {
          var now = s.q[i] || {};
          if (!now.open || (was[i] && was[i].open)) { return; }
          var o = defs[i] || {}, steps = o.steps || [];
          var d = base('cfifa-' + k + '-' + (+i + 1));
          d.kind = 'written'; d.question_text = o.head || '';
          var mineC = steps.map(function (st, j) { return String((now.lines || [])[j] || '').trim(); });
          var modelC = steps.map(function (st) { return (st.label ? st.label + ': ' : '') + (st.line || ''); });
          d.answer = steps.map(function (st, j) { return (st.label ? st.label + ': ' : '') + mineC[j]; }).join('\n');
          d.correct_answer = modelC.join('\n');
          // Marked, never self-checked (calcOf): the five model lines are
          // the scheme, the Answer line is checked by value and unit.
          post(calcOf(d, modelC, steps.map(function (st) { return st.label || ''; }), mineC));
        });
      },
      Ks4Steps: function (api, s, prev) {
        var p = api.logic.props || {};
        if (!rootLevel(api) || p.mode !== 'attempt' || prev.checked || !s.checked) { return; }
        var mine = [], model = [], labs = [], raw = [];
        (p.steps || []).forEach(function (st, i) {
          (st.lines || []).forEach(function (ln, j) {
            var lab = ln.label ? ln.label + ': ' : '';
            raw.push(String((s.vals || {})[i + '-' + j] || '').trim());
            mine.push(lab + raw[raw.length - 1]);
            model.push(lab + (ln.line || ''));
            labs.push(ln.label || '');
          });
        });
        var d = base('steps-' + nth(api));
        d.kind = 'written'; d.question_text = p.head || '';
        d.answer = mine.join('\n'); d.correct_answer = model.join('\n');
        // Marked, never self-checked (calcOf): every model line a point.
        post(calcOf(d, model, labs, raw));
      },
      /* ⊕ 13 Oct 2026 (every attempt): EVERY check of a chain is an answer
         — "Check again" after a wrong order, and the "Linked now." that
         follows, included. Ks4Chain counts its checks in `attempts`; each
         rise is one press, sent once (prevOf holds the last count).
         A chain inside a rung (Ks4Ladder r3, a Ks4Practice chain item)
         reports only its FIRST check to the rung, and the rung's handler
         sends that one with the rung's id and marks; every later check is
         sent here, under the same id, so the server numbers it attempt 2,
         3…. Each attempt carries what that attempt earned. */
      Ks4Chain: function (api, s, prev) {
        var was = prev.attempts || 0, now = s.attempts || 0;
        if (now <= was) { return; }
        var p = api.logic.props || {}, links = p.links || [], herr = p.herrings || [];
        var ids = s.chain || [];
        var ok = ids.length === links.length && ids.every(function (id, k) { return id === 'L' + k; });
        if (rootLevel(api)) {
          var d = base('chain-' + nth(api));
          d.kind = 'order'; d.question_text = p.prompt || p.title || '';
          d.answer = chainAnswer(api, links, herr); d.correct_answer = links.join('\n');
          d.is_correct = ok;
          post(d);
          return;
        }
        if (now < 2) { return; }                 // the first check is the rung's
        var owner = ownerOf(api);
        if (!owner || !owner.logic) { return; }
        var op = owner.logic.props || {}, R = op.rungs || {}, r = null, d2 = null;
        if (owner.comp === 'Ks4Ladder') {
          r = R.r3 || {};
          d2 = base('r3', 'r3');
          if (op.slug) { d2.lesson_slug = op.slug; d2.question_id = pilotId(op.slug, 'r3'); }
          d2.marks = r.marks || 3;
        } else if (owner.comp === 'Ks4Practice') {
          var L = [R.r1 || [], R.r2 || [], R.r3 || [], R.r4 || []], hidden = (owner.logic.state || {}).hidden || {}, keys = [];
          L.forEach(function (items, ri) {
            items.forEach(function (it, ii) { if ((it.kind || 'mcq') === 'chain' && !hidden[ri + '-' + ii]) { keys.push([ri, ii]); } });
          });
          var at = keys[kids(owner, 'Ks4Chain').indexOf(api)];
          if (!at) { return; }
          r = L[at[0]][at[1]] || {};
          d2 = base('r' + (at[0] + 1) + '-' + (at[1] + 1), 'r' + (at[0] + 1));
          d2.marks = r.marks || [1, 3, 3, 6][at[0]];
        } else { return; }
        d2.kind = 'order'; d2.question_text = r.prompt || '';
        d2.answer = chainAnswer(api, r.links || links, r.herrings || herr);
        d2.correct_answer = (r.links || links).join('\n');
        d2.is_correct = ok;
        d2.marks_scored = ok ? d2.marks : 0;
        post(d2);
      },
      Ks4Write: function (api, s, prev) {
        if (!rootLevel(api) || prev.open || !s.open) { return; }
        var p = api.logic.props || {};
        var d = base('write-' + nth(api));
        d.kind = 'written'; d.question_text = p.question || '';
        d.criteria = schemeOf(p); d.marks = p.marks || 4;
        writtenOut(d, String(s.text || '').trim());
      },
      Ks4Ladder: function (api, s, prev) {
        var L = api.logic, p = L.props || {}, R = p.rungs || {};
        ['r1', 'r2', 'r3', 'r4'].forEach(function (key) {
          var was = prev[key] === undefined ? null : prev[key];
          var v = s[key] === undefined ? null : s[key];
          if (was !== null || v === null) { return; }
          var d = base(key, key);
          if (p.slug) { d.lesson_slug = p.slug; d.question_id = pilotId(p.slug, key); }
          var r = R[key] || {};
          if (key === 'r1') {
            var o1 = r.options || [];
            d.kind = 'choice'; d.question_text = r.prompt || '';
            d.answer = optText(o1[s.r1Pick]); d.correct_answer = optText(rightOpt(o1));
          } else if (key === 'r2') {
            var kind = r.kind || 'calc';
            d.question_text = r.prompt || '';
            if (kind === 'data') {
              var parts = r.parts || [];
              d.kind = 'choice';
              d.answer = parts.map(function (pt, k) {
                var vv = s.r2parts ? s.r2parts[k] : undefined;
                return (pt.label || '') + ': ' + ((pt.options || [])[vv] == null ? '' : pt.options[vv]);
              }).join('\n');
              d.correct_answer = parts.map(function (pt) {
                return (pt.label || '') + ': ' + ((pt.options || [])[pt.answer] == null ? String(pt.answer) : pt.options[pt.answer]);
              }).join('\n');
            } else if (kind === 'text') {
              d.kind = 'numeric';               // a typed answer marked against a key
              d.answer = s.r2num || '';
              d.correct_answer = (r.accept || [])[0] == null ? null : r.accept[0];
            } else {
              d.kind = 'numeric';
              d.answer = calcAnswer(r, s.r2conv, s.r2num, s.r2unit);
              d.correct_answer = calcRight(r);
            }
          } else if (key === 'r3') {
            d.kind = 'order'; d.question_text = r.prompt || '';
            d.answer = chainAnswer(kids(api, 'Ks4Chain')[0], r.links || [], r.herrings || []);
            d.correct_answer = (r.links || []).join('\n');
          } else {
            var w = kids(api, 'Ks4Write')[0];
            d.kind = 'written'; d.question_text = r.question || '';
            d.criteria = schemeOf(r); d.marks = r.marks || 4;
            writtenOut(d, w && w.logic && w.logic.state ? String(w.logic.state.text || '').trim() : '');
            return;
          }
          // The page scores the rung whole: the marks on screen, or none.
          d.marks = r.marks || { r1: 1, r2: 2, r3: 3 }[key];
          d.is_correct = v === true;
          d.marks_scored = v === true ? d.marks : 0;
          post(d);
        });
      },
      Ks4Practice: function (api, s, prev) {
        var p = api.logic.props || {}, R = p.rungs || {};
        var L = [R.r1 || [], R.r2 || [], R.r3 || [], R.r4 || []];
        var was = prev.q || {}, now = s.q || {}, hidden = s.hidden || {};
        var chainKeys = [], writeKeys = [];
        L.forEach(function (items, ri) {
          items.forEach(function (it, i) {
            var k = ri + '-' + i, kind = it.kind || 'mcq';
            if (kind === 'chain' && !hidden[k]) { chainKeys.push(k); }
            if (kind === 'write' && !hidden[k]) { writeKeys.push(k); }
          });
        });
        L.forEach(function (items, ri) {
          items.forEach(function (it, i) {
            var k = ri + '-' + i, st = now[k] || {}, pv = was[k] || {};
            var res = st.res === undefined ? null : st.res, pres = pv.res === undefined ? null : pv.res;
            if (pres !== null || res === null) { return; }
            var kind = it.kind || 'mcq';
            var d = base('r' + (ri + 1) + '-' + (i + 1), 'r' + (ri + 1));
            d.question_text = it.prompt || '';
            d.marks = it.marks || [1, 3, 3, 6][ri];
            if (kind === 'write') {
              var w = kids(api, 'Ks4Write')[writeKeys.indexOf(k)];
              d.kind = 'written'; d.question_text = it.prompt || it.question || '';
              d.criteria = schemeOf(it);
              writtenOut(d, w && w.logic && w.logic.state ? String(w.logic.state.text || '').trim() : '');
              return;
            }
            if (kind === 'mcq') {
              d.kind = 'choice';
              d.answer = optText((it.options || [])[st.pick]); d.correct_answer = optText(rightOpt(it.options));
            } else if (kind === 'calc') {
              d.kind = 'numeric';
              d.answer = calcAnswer(it, st.conv, st.num, st.unit); d.correct_answer = calcRight(it);
            } else {
              d.kind = 'order';
              d.answer = chainAnswer(kids(api, 'Ks4Chain')[chainKeys.indexOf(k)], it.links || [], it.herrings || []);
              d.correct_answer = (it.links || []).join('\n');
            }
            d.is_correct = res === true;
            d.marks_scored = res === true ? d.marks : 0;
            post(d);
          });
        });
      }
    };

    // What each block's handler compares against: the few state fields that
    // say "answered", copied (the block replaces these objects on setState,
    // but a copy costs nothing and cannot alias).
    function snap(s) {
      var o = {};
      ['pick', 'checked', 'reported', 'attempts', 'open', 'r1', 'r2', 'r3', 'r4'].forEach(function (k) { o[k] = s[k]; });
      o.picks = Object.assign({}, s.picks || {});
      o.q = {};
      Object.keys(s.q || {}).forEach(function (k) { o.q[k] = Object.assign({}, s.q[k]); });
      return o;
    }
    var EMPTY = { pick: null, checked: false, reported: false, attempts: 0, open: false,
                  r1: null, r2: null, r3: null, r4: null, picks: {}, q: {} };

    window.MrBadmusKS4Tap = function (api) {
      if (!api || !api.logic || !prevOf) { return; }
      var h = HANDLERS[api.comp];
      if (!h) { return; }
      var s = api.logic.state || {};
      var prev = prevOf.get(api) || EMPTY;
      prevOf.set(api, snap(s));
      curBlock = api.host || null;
      try { h(api, s, prev); } catch (e) { /* capture never breaks a lesson */ }
      curBlock = null;
    };
  })();
} catch (e) {}
