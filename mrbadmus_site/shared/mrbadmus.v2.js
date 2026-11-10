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

  /* ⊕ Saved work follow-up (16 Oct 2026) — A CURRENT TOKEN FOR A FAMILY
     CHILD. A child who sat on a lesson for more than an hour, or whose
     phone slept, held an expired access token: every answer then queued
     behind a 401, the tutor refused, and the page restored nothing. These
     pages (KS3, rebuilt KS4) load no Supabase SDK, and
     consumer/consumer-common.js — which has the same fix as `api()` — is
     not on them, so this is the small local twin. Only the child-only
     paths below call it; a school pupil's page never does.
       · token(c): the session's access token — through the SDK's
         getSession() (which refreshes) when the page has the SDK, otherwise
         the stored one, refreshed first when it expires within a minute;
       · refresh(c): one refresh, for a 401 from our backend.
     A refresh without the SDK is GoTrue's own refresh-token grant, written
     back to the same localStorage key in the same shape, and only while
     that key still holds the SAME person (a different account's session is
     never swapped in). One refresh at a time per page. A refused refresh
     returns null: the caller keeps its answer queued, as before. */
  const childAuth = (function () {
    let client = null, pending = null;
    function stored(c) {
      try { return JSON.parse(localStorage.getItem(c.AUTH_STORAGE_KEY) || 'null'); } catch (e) { return null; }
    }
    function uid(s) { return s && s.user && s.user.id ? s.user.id : null; }
    function sdk(c) {
      if (!client && window.supabase && typeof window.supabase.createClient === 'function') {
        try { client = window.supabase.createClient(c.SUPABASE_URL, c.SUPABASE_ANON_KEY); } catch (e) { client = null; }
      }
      return client;
    }
    /* One refresh, under the SAME lock shared/config.js's timed child-token
       refresher takes ('lock:' + AUTH_STORAGE_KEY, exclusive), so the two
       never spend one refresh token at once. Inside the lock storage is read
       again: if someone else has already refreshed (same person, a token not
       expiring within a minute — and, for a 401, not the token that failed),
       that token is used with no request. Otherwise the stored refresh token
       is spent, and the result is written only if storage still holds that
       refresh token. Without navigator.locks, the same steps run unlocked. */
    function grant(c, s, force) {
      if (pending) return pending;
      const failed = s.access_token;
      const work = () => {
        const cur = stored(c);
        if (!cur || uid(cur) !== uid(s) || !cur.refresh_token) return null;
        const fresh = cur.access_token && cur.expires_at && cur.expires_at * 1000 > Date.now() + 60000;
        if (fresh && (!force || cur.access_token !== failed)) return cur.access_token;
        const spent = cur.refresh_token;
        return fetch(c.SUPABASE_URL + '/auth/v1/token?grant_type=refresh_token', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'apikey': c.SUPABASE_ANON_KEY },
          body: JSON.stringify({ refresh_token: spent })
        }).then(r => (r.ok ? r.json() : null)).then(n => {
          if (!n || !n.access_token || uid(n) !== uid(cur)) return null;
          const next = Object.assign({}, cur, n);
          if (!n.expires_at) next.expires_at = Math.floor(Date.now() / 1000) + (Number(n.expires_in) || 3600);
          const now = stored(c);
          if (now && uid(now) === uid(cur) && now.refresh_token === spent) {
            try { localStorage.setItem(c.AUTH_STORAGE_KEY, JSON.stringify(next)); } catch (e) {}
          }
          return next.access_token;
        }, () => null);
      };
      const locks = navigator.locks && typeof navigator.locks.request === 'function' ? navigator.locks : null;
      pending = Promise.resolve(locks ? locks.request('lock:' + c.AUTH_STORAGE_KEY, { mode: 'exclusive' }, work) : work())
        .catch(() => null);
      pending.then(() => { pending = null; }, () => { pending = null; });
      return pending;
    }
    async function viaSdk(cl, s, fn) {
      try {
        const r = await cl.auth[fn]();
        const ns = r && r.data && r.data.session;
        return ns && ns.access_token && uid(ns) === uid(s) ? ns.access_token : null;
      } catch (e) { return null; }
    }
    async function token(c) {
      const s = stored(c);
      if (!s || !s.access_token) return null;
      const cl = sdk(c);
      if (cl) return (await viaSdk(cl, s, 'getSession')) || s.access_token;
      if (!s.refresh_token || !s.expires_at || s.expires_at * 1000 > Date.now() + 60000) return s.access_token;
      return (await grant(c, s)) || s.access_token;
    }
    async function refresh(c) {
      const s = stored(c);
      if (!s || !s.refresh_token || !uid(s)) return null;
      const cl = sdk(c);
      return cl ? viaSdk(cl, s, 'refreshSession') : grant(c, s, true);
    }
    return { token, refresh };
  })();

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
- Respect exam command words. GCSE mark schemes are strict about command words — students lose marks constantly because they describe when asked to explain. Mirror the depth the command word demands: State / Give / Name → one-word or short-phrase answer, no justification; Describe → say what happens, in order, without needing to justify; Explain → say what happens AND why (use "because", "therefore", "this is due to"); Compare → cover similarities AND differences (use "whereas", "in contrast"); Evaluate → give both sides plus a judgement or conclusion; Calculate → show full working using CFIFA, with units at every stage; Suggest → apply known science to an unfamiliar context.
- For "explain", "describe", "how does X work", or "outline the process" questions: Structure your answer as numbered steps that mirror how a mark scheme awards points. Each step should contain at least one mark-worthy keyword. Cover the full process end-to-end — do not skip stages. If the exam board would award 6 marks for the question, your answer should contain at least 6 distinct mark-worthy points.
- Always give named, specific examples when explaining a concept. Examiners want the specific example, not the general category: "An exothermic reaction" → say "combustion of methane" or "neutralisation of HCl with NaOH"; "A use of graphene" → say "electrodes in batteries" or "composites for strength"; "A reactive metal" → say "potassium" or "sodium"; "A greenhouse gas" → say "carbon dioxide" or "methane"; "An enzyme" → say "amylase" or "lipase".
- For calculation questions: Continue using the CFIFA method, but make sure every term (variable name, unit, rearrangement) uses correct scientific vocabulary. Units are mark-bearing — a correct number with the wrong unit (or no unit) loses the final mark. Always state the unit at every stage: substituted values, rearrangements, and the final answer. If a unit conversion is needed (kJ → J, minutes → seconds, cm → m, g → kg), show it explicitly as the CFIFA "Convert" step, before the formula.
- For basic / definitional questions (e.g. "what is an atom?", "what does kinetic mean?"): Keep the answer short and friendly, but still use the correct scientific definition. A simple question deserves a simple answer — but never a wrong or vague one.
- End explain/describe/process answers with a "✅ Key exam words" line listing the 4–8 terms a student must include in their written answer to score full marks. Bold them. Use your judgement: skip this on casual chat, definitions, or quick clarifications where it would feel forced. Include it whenever a student is likely to be revising for or preparing to answer an exam question on the topic.
- If you are unsure whether a term is on the AQA spec, default to using it anyway and briefly explain it. It is always better to introduce a student to a real exam term than to hide it from them.
- Never invent scientific facts to fill a gap. If you're not sure whether something is on the AQA spec, or whether a specific claim is correct, say so honestly ("I'm not 100% sure this is on the AQA spec, but…") rather than inventing confident-sounding content. A student trusting an invented fact in an exam is worse than no answer at all. Do not invent spec point codes (e.g. "4.2.3.1") under any circumstances — refer to topics by name instead.
Self-check before sending any science answer, ask yourself: Have I used the actual exam-board terminology, not a watered-down version? If a student copied my answer into an exam, would they earn the marks? Have I matched the depth to the student's tier (Foundation / Higher / Triple)? Have I respected the command word the student used (describe vs explain vs compare)? Have I covered every stage of the process, not just the highlights? Have I given named, specific examples rather than vague categories? Have I used analogies in addition to technical terms, not instead of them? Am I confident every claim I've made is actually correct, or have I invented anything? If the answer to any of these is "no", rewrite before sending.
Remember: Students lose marks for vague language, wrong command-word matching, missing examples, and Foundation-level depth on Higher questions. Your job is to make sure none of that ever happens to a Mr Badmus AI student. Warm tone + scientifically precise terminology + correct depth + named examples = students who walk into exams confident and equipped.
2. Use the CFIFA method for ALL calculations without exception:
   C = Convert (put every value into the unit the equation needs first, e.g. kJ → J, minutes → seconds, cm → m, g → kg — say so if nothing needs converting)
   F = Formula (write it out)
   I = Insert values (substitute numbers + units)
   F = Fine-tune (rearrange, then round to sensible significant figures)
   A = Answer (include the unit — always)
3. Always say "potential difference" not "voltage" in physics contexts
4. Always include units in every final answer
5. Show all working — never skip steps
6. Be encouraging and warm — students may be struggling
7. When a concept is tricky, use a real-life analogy first
8. For higher tier content, label it clearly: ⭐ HIGHER TIER
9. For triple science only content, label it: 🔬 TRIPLE ONLY
10. Keep responses SHORT and punchy — 3 to 6 lines max unless doing a full CFIFA example
11. Never start with a long introduction — get straight to the point
12. If a student just says hello or greets you, respond with ONE friendly line only — e.g. "Hey! What are we working on today? 🔥"
13. Never list topics unprompted — only show a list if the student asks "what can you help with"
14. Format clearly with line breaks — never write a wall of text. Write maths in plain text and Unicode (×, ÷, ², ₂, 10⁴, ΔE = m × c × Δθ, ½mv²), never LaTeX commands or $ signs around maths — the chat cannot draw LaTeX
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

  // `before` (⊕ saved work, 16 Oct 2026): put the message ahead of that node
  // instead of at the end. Only a family child's restored conversation passes
  // it; every other call is exactly as before.
  function addMsg(role, html, before) {
    const box = document.getElementById('chatMsgs');
    if (!box) return null;
    const d = document.createElement('div');
    d.className = `chat-msg chat-msg--${role}`;
    d.innerHTML = `<div class="chat-msg__avatar">${role==='user'?'🧑':'⚡'}</div><div class="chat-msg__bubble">${html}</div>`;
    if (before && before.parentNode === box) box.insertBefore(d, before);
    else box.appendChild(d);
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

  /* ⊕ Tutor maths (25 Oct 2026) — the model writes LaTeX: \frac{a}{b},
     3 \times 10^{8}, $E = mc\Delta\theta$, x_{2}. The bubble showed every
     backslash and brace raw. texToText() turns it into plain text before
     formatReply does anything else:
       · MATH SPANS. \( … \) and \[ … \] always; $ … $ and $$ … $$ only when
         the body holds a backslash command, a ^ or a _ — so "£5 and $3" and
         "$3 and $5" are prose and stay exactly as written.
       · OUTSIDE A SPAN only the unambiguous pieces are touched: a KNOWN
         command (\times, \frac{…}{…}, \Delta …), ^{…} / _{…}, and ^ or _
         followed by digits right after a letter, digit or bracket
         (10^4, H_2O). snake_case, ^_^ and "___" rules are left alone.
       · Powers and subscripts become Unicode (10⁴, x₂, 2+ → ²⁺) where every
         character has one, else a bare <sup>/<sub>. Those are the only tags
         this pass writes; it runs BEFORE the allow-list lift, so they are
         lifted like a reply's own and every other byte is still escaped.
     No lookbehind in any regex here: one SyntaxError in an old Safari and
     the whole tutor is gone. */
  const TEX_OPS = { times: '×', div: '÷', cdot: '·', pm: '±', mp: '∓', leq: '≤', le: '≤', geq: '≥', ge: '≥',
    neq: '≠', ne: '≠', approx: '≈', propto: '∝', equiv: '≡', rightarrow: '→', to: '→', longrightarrow: '→',
    Rightarrow: '⇒', leftarrow: '←', leftrightarrow: '↔', rightleftharpoons: '⇌', rightleftarrows: '⇌' };
  const TEX_SYMS = { Delta: 'Δ', delta: 'δ', alpha: 'α', beta: 'β', gamma: 'γ', Gamma: 'Γ', lambda: 'λ', mu: 'μ',
    pi: 'π', rho: 'ρ', sigma: 'σ', Sigma: 'Σ', theta: 'θ', Theta: 'Θ', omega: 'ω', Omega: 'Ω', eta: 'η',
    epsilon: 'ε', varepsilon: 'ε', phi: 'φ', varphi: 'φ', Phi: 'Φ', tau: 'τ', nu: 'ν', kappa: 'κ', chi: 'χ',
    psi: 'ψ', circ: '°', degree: '°', infty: '∞', partial: '∂', prime: '′', ldots: '…', dots: '…', cdots: '⋯',
    angle: '∠', hbar: 'ħ', ell: 'ℓ', sin: 'sin', cos: 'cos', tan: 'tan', log: 'log', ln: 'ln', exp: 'exp' };
  const TEX_FRAC = { frac: 1, dfrac: 1, tfrac: 1, cfrac: 1 };
  const TEX_WRAP = { text: 1, textrm: 1, mbox: 1, textbf: 1, textit: 1, mathrm: 0, mathbf: 0, mathit: 0,
    mathsf: 0, operatorname: 0, boxed: 0 };               // 1 = literal text, 0 = more maths inside
  const TEX_DROP = { left: 1, right: 1, displaystyle: 1, textstyle: 1, limits: 1, big: 1, Big: 1,
    bigl: 1, bigr: 1, Bigl: 1, Bigr: 1, quad: 2, qquad: 2 };     // 2 = a space
  const TEX_HALF = { '1/2': '½', '1/3': '⅓', '2/3': '⅔', '1/4': '¼', '3/4': '¾' };
  const SUP_MAP = { 0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹',
    '+': '⁺', '-': '⁻', '−': '⁻', '=': '⁼', '(': '⁽', ')': '⁾', n: 'ⁿ', i: 'ⁱ' };
  const SUB_MAP = { 0: '₀', 1: '₁', 2: '₂', 3: '₃', 4: '₄', 5: '₅', 6: '₆', 7: '₇', 8: '₈', 9: '₉',
    '+': '₊', '-': '₋', '−': '₋', '=': '₌', '(': '₍', ')': '₎' };
  const isLetter = c => !!c && /[A-Za-z]/.test(c);

  function texScript(body, up) {
    const s = body.trim();
    if (!s) return '';
    if (up && (s === '°' || s === '′')) return s;          // ^{\circ}, ^{\prime}
    const map = up ? SUP_MAP : SUB_MAP;
    if ([...s].every(c => map[c])) return [...s].map(c => map[c]).join('');
    return up ? '<sup>' + s + '</sup>' : '<sub>' + s + '</sub>';
  }
  // One argument at s[i]: {balanced group}, a \command, or one character.
  function texArg(s, i) {
    while (s[i] === ' ') i++;
    if (i >= s.length) return ['', i];
    if (s[i] === '{') {
      let depth = 0;
      for (let j = i; j < s.length; j++) {
        if (s[j] === '\\') { j++; continue; }
        if (s[j] === '{') depth++;
        else if (s[j] === '}' && --depth === 0) return [s.slice(i + 1, j), j + 1];
      }
      return [s.slice(i + 1), s.length];                 // never closed: the rest
    }
    if (s[i] === '\\') {
      let j = i + 1;
      if (isLetter(s[j])) { while (isLetter(s[j])) j++; } else j++;
      return [s.slice(i, j), j];
    }
    return [s[i], i + 1];
  }
  // a/b needs brackets round a sum on either side, and round any denominator
  // that is more than one quantity: Q/(mΔθ), never Q/mΔθ.
  function texCompound(x, under) {
    if (/^\(.*\)$/.test(x)) return x;
    const one = /^(\d+(\.\d+)?|[A-Za-zΑ-Ωα-ω][₀-₉⁰-⁹⁻]*)$/.test(x);
    return /[\s+\-−×÷·/=±]/.test(x) || (under && !one) ? '(' + x + ')' : x;
  }
  // Where the command whose name ends at j stops (its arguments included).
  function texEnd(s, name, j) {
    if (TEX_FRAC[name]) return texArg(s, texArg(s, j)[1])[1];
    if (name === 'sqrt') {
      let k = j;
      while (s[k] === ' ') k++;
      if (s[k] === '[') { const c = s.indexOf(']', k); if (c !== -1) k = c + 1; }
      return texArg(s, k)[1];
    }
    if (name === 'ce' || name in TEX_WRAP) return texArg(s, j)[1];
    if ((name === 'left' || name === 'right') && s[j] === '.') return j + 1;
    return j;
  }
  const texKnown = name => !!(TEX_FRAC[name] || name === 'sqrt' || name === 'ce' || name in TEX_WRAP ||
    name in TEX_DROP || name in TEX_OPS || name in TEX_SYMS);

  // The body of a maths span: everything is LaTeX.
  function texMath(s) {
    let out = '';
    let i = 0;
    while (i < s.length) {
      const c = s[i];
      if (c === '\\') {
        if (!isLetter(s[i + 1])) {
          const n = s[i + 1];
          if (n !== undefined) out += ',;: \\'.indexOf(n) !== -1 ? ' ' : n === '!' ? '' : n;
          i += 2;
          continue;
        }
        let j = i + 1;
        while (isLetter(s[j])) j++;
        const name = s.slice(i + 1, j);
        if (TEX_FRAC[name]) {
          const a = texArg(s, j), b = texArg(s, a[1]);
          const A = texMath(a[0]), B = texMath(b[0]);
          out += TEX_HALF[A + '/' + B] || texCompound(A, false) + '/' + texCompound(B, true);
          i = b[1];
        } else if (name === 'sqrt') {
          let k = j, idx = '';
          while (s[k] === ' ') k++;
          if (s[k] === '[') { const e = s.indexOf(']', k); if (e !== -1) { idx = s.slice(k + 1, e).trim(); k = e + 1; } }
          const a = texArg(s, k), A = texMath(a[0]);
          out += (idx === '3' ? '∛' : idx === '4' ? '∜' : (idx ? texScript(idx, true) : '') + '√') +
            (A.length > 1 ? '(' + A + ')' : A);
          i = a[1];
        } else if (name === 'ce') {                          // mhchem: \ce{H2SO4}
          const a = texArg(s, j);
          out += texMath(a[0].replace(/->/g, '\\rightarrow ').replace(/<=>/g, '\\rightleftharpoons ')
            .replace(/([A-Za-z)\]])(\d+)/g, '$1_{$2}'));
          i = a[1];
        } else if (name in TEX_WRAP) {
          const a = texArg(s, j);
          out += TEX_WRAP[name] ? a[0].replace(/\\([%$&#_{}])/g, '$1') : texMath(a[0]);
          i = a[1];
        } else if (name in TEX_DROP) {
          if (TEX_DROP[name] === 2) out += ' ';
          i = texEnd(s, name, j);
        } else if (name in TEX_OPS) {
          out += ' ' + TEX_OPS[name] + ' ';
          i = j;
        } else {
          out += name in TEX_SYMS ? TEX_SYMS[name] : name;   // unknown: its name, no backslash
          if (s[j] === ' ' && isLetter(s[j + 1])) j++;       // TeX eats the space: \Delta T → ΔT
          i = j;
        }
        continue;
      }
      if (c === '^' || c === '_') {
        let j = i + 1;
        while (s[j] === ' ') j++;
        const run = s[j] !== '{' ? /^[-−+]?\d+/.exec(s.slice(j)) : null;
        const a = run ? [run[0], j + run[0].length] : texArg(s, j);
        out += texScript(texMath(a[0]), c === '^');
        i = a[1];
        continue;
      }
      if (c === '{' || c === '}') { i++; continue; }
      out += c === '~' || c === '&' ? ' ' : c;
      i++;
    }
    return out.replace(/\s+/g, ' ').replace(/\( /g, '(').replace(/ \)/g, ')').trim();
  }

  // Prose: only a known command, ^{…}/_{…}, or ^/_ + digits after a letter,
  // digit or bracket. Everything else is left byte for byte.
  function texProse(t) {
    if (!/[\\^_]/.test(t)) return t;
    let out = '';
    let i = 0;
    while (i < t.length) {
      const c = t[i];
      const prev = out.slice(-1);
      if (c === '\\') {
        const n = t[i + 1];
        if (n === ',' || n === ';') { out += ' '; i += 2; continue; }
        if (n === '!') { i += 2; continue; }
        if (n === '$') { out += '$'; i += 2; continue; }
        let j = i + 1;
        while (isLetter(t[j])) j++;
        const name = t.slice(i + 1, j);
        if (!name || !texKnown(name)) { out += c; i++; continue; }
        const end = texEnd(t, name, j);
        const piece = texMath(t.slice(i, end));
        i = end;
        if (name in TEX_OPS) {
          const line = out.slice(out.lastIndexOf('\n') + 1);
          if (line.trim()) out = out.replace(/[ \t]+$/, '') + ' ';
          while (t[i] === ' ' || t[i] === '\t') i++;
          out += piece + (i < t.length && !/[\s.,;:!?)\]]/.test(t[i]) ? ' ' : '');
        } else {
          out += piece;
          if (name in TEX_SYMS && t[i] === ' ' && isLetter(t[i + 1])) i++;
        }
        continue;
      }
      if (c === '^' || c === '_') {
        const n = t[i + 1];
        if ((n === '{' || (c === '^' && n === '\\' && isLetter(t[i + 2]))) && prev && prev.trim()) {
          const a = texArg(t, i + 1);
          out += texScript(texMath(a[0]), c === '^');
          i = a[1];
          continue;
        }
        const run = (c === '^' ? /^[-−+]?\d+/ : /^\d+(?!_)/).exec(t.slice(i + 1));
        if (run && (c === '^' ? /[A-Za-z0-9)\]]/ : /[A-Za-z)\]]/).test(prev)) {
          out += texScript(run[0], c === '^');
          i += 1 + run[0].length;
          continue;
        }
      }
      out += c;
      i++;
    }
    return out;
  }

  function texToText(str) {
    const s = String(str);
    if (!/[\\^_$]/.test(s)) return s;
    let out = '', last = 0, i = 0;
    while (i < s.length) {
      const c = s[i];
      let from = -1, close = '', dollar = false;
      if (c === '\\' && (s[i + 1] === '(' || s[i + 1] === '[')) { from = i + 2; close = s[i + 1] === '(' ? '\\)' : '\\]'; }
      else if (c === '\\') { i += 2; continue; }                       // \$ is a dollar sign
      else if (c === '$' && s[i + 1] === '$') { from = i + 2; close = '$$'; dollar = true; }
      else if (c === '$') { from = i + 1; close = '$'; dollar = true; }
      if (from !== -1) {
        let end = -1;
        if (close === '$') {
          for (let j = from; j < s.length && s[j] !== '\n'; j++) {
            if (s[j] === '\\') { j++; continue; }
            if (s[j] === '$') { end = j; break; }
          }
        } else end = s.indexOf(close, from);
        if (end > from) {
          const body = s.slice(from, end);
          const ok = !dollar || (/[\\^_]/.test(body) &&
            (close !== '$' || (body[0] !== ' ' && body[body.length - 1] !== ' ' && !/\d/.test(s[end + 1] || ''))));
          if (ok) {
            out += texProse(s.slice(last, i)) + texMath(body);
            i = last = end + close.length;
            continue;
          }
        }
      }
      i++;
    }
    return out + texProse(s.slice(last));
  }

  function formatReply(text) {
    const tags = [];
    const lifted = texToText(String(text).replace(/[]/g, '')).replace(ALLOWED_TAG, (m, close, name) => {
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
  if (window.MRB_TUTOR_TEST_HOOK) {
    window.MRB_TUTOR_TEST_HOOK.formatReply = formatReply;
    window.MRB_TUTOR_TEST_HOOK.texToText = texToText;
  }

  /* MRB-257 — KS3 framing, appended after the subject prompt.
     Additive by construction: it is only ever reached when a page passes
     `keyStage: 'ks3'`, and no page did before KS3 lesson pages started to.
     A KS4 page therefore builds the byte-identical prompt it always did.

     It APPENDS rather than replacing the subject prompt, and that is the
     deliberate choice. The base prompt carries the safeguarding section —
     forty lines of it, and the single most important thing in the file for an
     eleven-year-old audience — plus the tone, the CFIFA method and the honesty
     rules, all of which hold at KS3. What does not hold is the exam framing
     wrapped around them, so this overrides that explicitly and last, where a
     model weights it most. Replacing the whole prompt would mean a second copy
     of the safeguarding block, free to drift from the first. */
  const KS3_FRAMING = `

KEY STAGE 3 — THIS OVERRIDES THE EXAM FRAMING ABOVE.
You are talking to a KS3 student: roughly 11 to 14 years old, two or three years before they start a GCSE course. Everything above about warmth, honesty, the CFIFA method for calculations, units in every answer, and safeguarding still applies exactly as written. The exam-board framing does not.
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
      drawSavedTalk();                       // a family child's earlier conversation, if any
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
    let userContent = hasImg ? [{ type:'image', source:{ type:'base64', media_type:imgData.split(';')[0].split(':')[1], data:imgData.split(',')[1] }}, { type:'text', text:q||PHOTO_ONLY }] : q;
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
      /* ⊕ A child's token is a CURRENT one (childAuth), and a 401 is
         refreshed and asked once more — a child back from a long pause is
         answered, and their question is logged. A school pupil's request is
         exactly as before: the stored token, one request. */
      if (childContext) {
        const fresh = await childAuth.token(c);
        if (fresh) authHeaders['Authorization'] = 'Bearer ' + fresh;
      }
      const chatOnce = () => fetch(c.BACKEND_URL + '/api/chat', {
        method:'POST',
        headers: authHeaders,
        body:JSON.stringify(childContext
          ? { system:systemPrompt, messages:chatHistory, context:childContext }
          : { system:systemPrompt, messages:chatHistory }),
        signal: controller.signal
      });
      let res = await chatOnce();
      if (res.status === 401 && childContext) {
        const again = await childAuth.refresh(c);
        if (again) { authHeaders['Authorization'] = 'Bearer ' + again; res = await chatOnce(); }
      }
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

  /* ⊕ Saved work (Mide, 16 Oct 2026): "the full tutor conversation for that
     lesson" comes back on load — on any device, after signing out and in.
     ONLY FOR A FAMILY OR ORGANISATION CHILD: the one caller is the saved-work
     loader at the end of this file, which installs itself for a child
     session (MrBadmusConfig.isChildSession) and for nobody else, so a school
     pupil's panel never reaches this.

     `rows` are the child's own exchanges on this lesson, oldest first, from
     GET /api/consumer/child/saved: {question, has_image, reply, answered,
     asked_at}. Each answered one is drawn exactly as it was live — the
     question escaped (esc), the reply through formatReply — and seeds
     chatHistory, so a follow-up question carries the conversation. An
     exchange the tutor never answered is left out, as it was left out of
     chatHistory live. The picture itself is not kept anywhere, so a photo
     question says so in words.

     Drawn after the greeting when the panel first opens (open() adds the
     greeting); if the panel is already open, slotted in after the greeting,
     ahead of anything asked on this visit. */
  const PHOTO_ONLY = 'Answer this GCSE Science question fully using CFIFA for any calculations.';
  // Saved before 25 Oct 2026 (FIFA → CFIFA): a stored photo question still reads as one.
  const PHOTO_ONLY_FIFA = 'Answer this GCSE Science question fully using FIFA for any calculations.';
  let savedTalk = null;
  function drawSavedTalk() {
    const rows = savedTalk;
    savedTalk = null;
    if (!rows || !rows.length) return;
    const box = document.getElementById('chatMsgs');
    if (!box) return;
    const anchor = box.children[1] || null;       // after the greeting
    rows.forEach(r => {
      const q = r.has_image && (r.question === PHOTO_ONLY || r.question === PHOTO_ONLY_FIFA) ? '' : String(r.question || '');
      addMsg('user', esc(q || 'Please answer this question:') +
        (r.has_image ? '<br><em>(You sent a photo with this question.)</em>' : ''), anchor);
      addMsg('bot', formatReply(r.reply), anchor);
    });
    box.scrollTop = box.scrollHeight;
  }
  function restoreTalk(rows) {
    const done = (rows || []).filter(r => r && r.answered && typeof r.reply === 'string' && r.reply !== '' && typeof r.question === 'string');
    if (!done.length) return;
    const past = [];
    done.forEach(r => {
      past.push({ role:'user', content:r.question });
      past.push({ role:'assistant', content:r.reply });
    });
    chatHistory = past.concat(chatHistory);
    while (chatHistory.length > 20) chatHistory.splice(0, 2);
    savedTalk = done;
    if (chatInited) drawSavedTalk();
  }

  /* ⊕ 8 Nov 2026 — formatReply and the built prompt, for "Ask the tutor" on a
     practice question (shared/ask-tutor.js), which has no chat panel of its own. */
  return { init, open, close, ask, restoreTalk, childAuth, formatReply, systemPrompt: () => systemPrompt };
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
      /* ⊕ Saved work (16 Oct 2026): a page that comes back FINISHED because
         its answers were restored from the server was finished on an earlier
         visit — that visit already sent this. So nothing is checked while
         the saved work is being put back, and a page that is finished the
         moment it has been put back is latched as sent. Only a page the
         child finishes now sends. */
      // Read when asked: on a deferred page this runs before the loader at
      // the end of this file has installed MrBadmusSaved.
      function restoring() {
        var sv = window.MrBadmusSaved;
        return !!(sv && sv.state !== 'done');
      }
      document.addEventListener('mrb:saved-applied', function () {
        if (sent) { return; }
        if (finished()) { sent = true; if (obs) { obs.disconnect(); } }
        else { check(); }
      });
      function check() {
        if (restoring()) { return; }
        if (sent || !finished()) { return; }
        sent = true;
        if (obs) { obs.disconnect(); }
        /* ⊕ Saved work follow-up (16 Oct 2026): a lost "done" breaks the
           child's streak, so the token is a CURRENT one (MrBadmus.childAuth
           refreshes an expired one) and a 401 is refreshed once and sent
           once more. */
        try {
          var s2 = JSON.parse(window.localStorage.getItem(c.AUTH_STORAGE_KEY) || 'null') || session;
          var auth = window.MrBadmus && window.MrBadmus.childAuth;
          var done = function (tok) {
            return fetch(c.BACKEND_URL + '/api/consumer/child/lesson-done', {
              method: 'POST',
              keepalive: true,
              headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + tok },
              body: JSON.stringify({ path: path, key_stage: 'KS4' })
            });
          };
          Promise.resolve(auth ? auth.token(c) : s2.access_token)
            .then(function (tok) { return done(tok || s2.access_token); })
            .then(function (r) {
              if (r && r.status === 401 && auth) {
                return auth.refresh(c).then(function (t2) { return t2 ? done(t2) : r; });
              }
              return r;
            })
            .catch(function () { /* best effort — the lesson never waits on this */ });
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
    // ⊕ 8 Nov 2026: a practice page loads this file for its tutor only.
    if (/^\/student\//.test(path)) { return; }
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
    /* ⊕ Saved work (16 Oct 2026) — `replay` and `mute`, for the saved-work
       loader at the end of this file. When a child comes back to a lesson,
       their answers are put back by the page's OWN controls (or, on the
       rebuilt KS4 pages, the block's own state), and every capture path below
       sees that as an answer being given. While `mute` is held, nothing is
       sent: a restored answer is never a second ledger row. The capture's
       memory of what it has already sent (sentUnits, lastText, matchSent…)
       still moves, exactly as if the child had just done it, so the NEXT real
       answer is judged against the restored one. Each page type below
       registers one `replay` function; each is handed the child's saved rows
       for this lesson, oldest first. */
    var muted = 0;
    var replay = [];
    window.MrBadmusAnswerCapture = {
      visitId: visitId,
      replay: replay,
      mute: function (on) { muted = Math.max(0, muted + (on ? 1 : -1)); }
    };

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
    /* ⊕ Saved work follow-up (16 Oct 2026): the token is a CURRENT one
       (MrBadmus.childAuth — refreshed when it has expired), and a 401 is
       refreshed once and sent once more, so an answer given after a long
       pause is saved now rather than queued behind an expired token. */
    var auth = window.MrBadmus && window.MrBadmus.childAuth;
    function token() {
      if (auth) { return auth.token(c); }
      try {
        var s2 = JSON.parse(window.localStorage.getItem(c.AUTH_STORAGE_KEY) || 'null');
        return Promise.resolve((s2 && s2.access_token) || null);
      } catch (e) { return Promise.resolve(null); }
    }
    // Resolves true only on a 2xx (204 included). `live` sends ride on
    // keepalive so they survive the page going away; a flush does not, as
    // keepalive bodies share a small per-page budget.
    function send(body, tok, live, retried) {
      try {
        return fetch(ANSWER_URL, {
          method: 'POST',
          keepalive: !!live,
          headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + tok },
          body: JSON.stringify(body)
        }).then(function (r) {
          if (r && r.status === 401 && !retried && auth) {
            return auth.refresh(c).then(function (t2) { return t2 ? send(body, t2, live, true) : false; });
          }
          return !!(r && r.ok);
        }, function () { return false; });
      } catch (e) { return Promise.resolve(false); }
    }
    var flushing = false;
    var inflight = {};                         // client_event_id → a send this page has not heard back from
    function flush() {
      if (flushing) { return; }
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
        token().then(function (tok) { return tok ? send(b, tok, false) : false; }).then(function (ok) {
          delete inflight[b.client_event_id];
          if (!ok) { flushing = false; return; }   // keep it and the rest; try again later
          boxDrop(b.client_event_id);
          next();
        });
      })();
    }

    /* ⊕ Saved work follow-up (16 Oct 2026) — THE CHILD'S OWN TICKS.
       "I had this" lines (KS3 and KS4 "Your turn", Ks4Steps) and a written
       answer's criteria (a KS3 written rung, Ks4Write) are the child's
       self-marking. They were kept only on the page, so 5 of 5 ticked on
       one device came back 0 of 5 on another. Each change is sent (after a
       short pause, so a run of taps is one request) to
       POST /api/consumer/child/self-ticks, which keeps them on that
       answer's own ledger row — never a mark, never a new row. A 404 means
       the answer itself has not reached the ledger yet (a written answer is
       marked first): tried again, waiting longer each time, for ~2 minutes. While `mute` is held (a restore) nothing
       is sent, and the restored ticks are remembered as already saved. */
    var tickTimers = {}, tickLast = {}, tickWant = {};
    /* ⊕ 9 Nov 2026: unsubmitted typing, kept on this device only, per child and
       question, cleared when the answer is sent. It never reaches the server and
       never comes back on another device. A family child's session only: this whole
       capture installs for nobody else. */
    var draftChild = (session.user && session.user.id) || 'child', draftTimers = {}, draftWaiting = {};
    /* ⊕ 9 Nov 2026: a timer that starts again on reload makes an answer look quick.
       A draft keeps how long the child had been at it, and the answer it becomes is
       sent with that time added. A draft from before this (no time kept) gives null,
       never a low figure. */
    var draftCarry = {};
    function draftKey(q) { return 'mrb_draft_v1:' + draftChild + ':' + q; }
    function draftWrite(q) {
      var w = draftWaiting[q];
      delete draftWaiting[q];
      if (w === undefined) { return; }
      try { window.localStorage.setItem(draftKey(q), w); } catch (e) { /* storage refused */ }
    }
    function draftPut(q, v) {
      var had = Object.prototype.hasOwnProperty.call(draftCarry, q) ? draftCarry[q] : 0;
      var ms = had === null ? null : had + visibleMs(lastAt, Date.now());
      draftWaiting[q] = JSON.stringify({ __d: 1, v: v, ms: ms });
      clearTimeout(draftTimers[q]);
      draftTimers[q] = setTimeout(function () { draftWrite(q); }, 300);
    }
    function draftRaw(q) { try { return JSON.parse(draftWaiting[q] || window.localStorage.getItem(draftKey(q)) || 'null'); } catch (e) { return null; } }
    function draftGet(q) { var r = draftRaw(q); return r && r.__d ? r.v : r; }
    // The draft is going back on screen: its time goes with it.
    function draftTake(q) {
      var r = draftRaw(q);
      if (r === null) { return null; }
      draftCarry[q] = r.__d && typeof r.ms === 'number' ? r.ms : null;
      return r.__d ? r.v : r;
    }
    function draftDrop(q) { clearTimeout(draftTimers[q]); delete draftWaiting[q]; try { window.localStorage.removeItem(draftKey(q)); } catch (e) { /* storage refused */ } }
    function draftsFlush() { Object.keys(draftWaiting).forEach(function (q) { clearTimeout(draftTimers[q]); draftWrite(q); }); }
    window.addEventListener('pagehide', draftsFlush);
    document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'hidden') { draftsFlush(); } });
    var rootCarry;                       // a lesson's own picks, restored: see rootDraftBack
    // What this answer owes its draft, if it came from one.
    function carried(d, t) {
      var c, has = false, q = d.question_id;
      if (q != null && Object.prototype.hasOwnProperty.call(draftCarry, q)) { c = draftCarry[q]; has = true; delete draftCarry[q]; }
      var b = d.__block, sent = String(d.answer == null ? '' : d.answer);
      if (b && b.id === 'ks4-mount' && rootCarry !== undefined) { c = rootCarry; has = true; rootCarry = undefined; }
      var owner = b && b.closest ? b.closest('[data-activity]') : null;
      if (owner && owner.__mrbPickKey) {
        draftDrop(owner.__mrbPickKey);
        if (Object.prototype.hasOwnProperty.call(owner, '__mrbPickCarry')) { c = owner.__mrbPickCarry; has = true; delete owner.__mrbPickCarry; }
      }
      if (b && b.querySelectorAll) {
        Array.prototype.forEach.call(b.querySelectorAll('input, textarea, select'), function (el) {
          var val = el.tagName === 'SELECT' ? (el.options[el.selectedIndex] ? (el.options[el.selectedIndex].textContent || '').trim() : '') : String(el.value || '').trim();
          var went = !!val && sent.indexOf(val) >= 0;
          if (el.__mrbDraftKey && (went || el.disabled)) { draftDrop(el.__mrbDraftKey); }
          if (went && Object.prototype.hasOwnProperty.call(el, '__mrbCarry')) {
            c = has && (c === null || c === undefined) ? null : el.__mrbCarry; has = true; delete el.__mrbCarry;
          }
        });
      }
      if (!has) { return t; }
      if (t == null || c == null) { return null; }
      var total = t + Math.round(c / 1000);
      return total > CAP_S ? null : total;
    }
    // A saved row's own ticks: the server's 100 + level is not one of them.
    function ownTicks(r) { return r && Array.isArray(r.self_ticks) ? r.self_ticks.filter(function (n) { return n < 100; }) : null; }
    function tickKeep(qid, list, level) {
      try {
        var box = JSON.parse(window.localStorage.getItem('mrb_ticks_outbox_v1') || '{}');
        if (list) { box[qid] = { ticks: list, at: Date.now() }; if (typeof level === 'number') { box[qid].level = level; } } else { delete box[qid]; }
        if (Object.keys(box).length) { window.localStorage.setItem('mrb_ticks_outbox_v1', JSON.stringify(box)); }
        else { window.localStorage.removeItem('mrb_ticks_outbox_v1'); }
      } catch (e) { /* storage refused: the in-page retry still runs */ }
    }
    /* ⊕ 9 Nov 2026: `level` (a value, 0–9) is the level a child picked, read from
       the label they pressed. A rung's correct_answer is its indicative points, so
       the server cannot read a pick from a position in `ticks`. It keeps the value
       inside self_ticks as 100 + level: every reader here uses ownTicks(). */
    function sendTicks(qid, list, tries, level) {
      qid = safeId(qid);
      if (!qid) { return; }
      list = (list || []).filter(function (n) { return n >= 1 && n <= 20; });
      var lvl = typeof level === 'number' && level >= 0 && level <= 9 ? level : null;
      var key = list.join(',') + '|' + (lvl === null ? '' : lvl);
      if (muted) { tickLast[qid] = key; tickWant[qid] = key; return; }
      if (tries && tickWant[qid] !== key) { return; }        // a newer set has been asked for
      tickWant[qid] = key;
      if (!tries && tickLast[qid] === key) { return; }
      if (!tries) { tickKeep(qid, null); }                 // this set supersedes any waiting one
      clearTimeout(tickTimers[qid]);
      tickTimers[qid] = setTimeout(function () {
        var go = function (tok) {
          return fetch(c.BACKEND_URL + '/api/consumer/child/self-ticks', {
            method: 'POST', keepalive: true,
            headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + tok },
            body: JSON.stringify(lvl === null ? { question_id: qid, ticks: list } : { question_id: qid, ticks: list, level: lvl })
          });
        };
        token().then(function (tok) { return tok ? go(tok) : null; })
          .then(function (r) {
            if (r && r.status === 401 && auth) { return auth.refresh(c).then(function (t2) { return t2 ? go(t2) : r; }); }
            return r;
          })
          .then(function (r) {
            if (r && (r.ok || r.status === 204)) { tickLast[qid] = key; tickKeep(qid, null); return; }
            /* ⊕ 9 Nov 2026: a 429 waits what it says and sends the same set again.
               A tick set replaces the last one on the row, so a repeat cannot double
               it. Whatever is left is kept for shared/account.js to send after a reload. */
            if (r && r.status === 429) {
              tickKeep(qid, list, lvl);
              return r.json().then(function (d) { return d && d.retry_after_s; }, function () { return null; }).then(function (s) {
                if ((tries || 0) < 8) { setTimeout(function () { sendTicks(qid, list, (tries || 0) + 1, lvl); }, Math.max(Number(s) > 0 ? Number(s) * 1000 : 30000, 1000)); }
              });
            }
            tickKeep(qid, list, lvl);
            // A written answer is marked BEFORE its row lands (up to half a
            // minute), so the wait grows: 3 s, 6 s, … eight tries, ~2 min.
            if (r && r.status === 404 && (tries || 0) < 8) {
              setTimeout(function () { sendTicks(qid, list, (tries || 0) + 1, lvl); }, 3000 * ((tries || 0) + 1));
            }
          }, function () { tickKeep(qid, list, lvl); });
      }, tries ? 0 : 700);
    }
    window.MrBadmusAnswerCapture.ticks = sendTicks;
    window.MrBadmusAnswerCapture.afterReplay = [];
    window.MrBadmusAnswerCapture.beforeReplay = [];

    // The server accepts ids matching ^[a-z0-9:#._-]{1,200}$ and marks 1–20
    // with 0 ≤ marks_scored ≤ marks; anything else is sent as null rather
    // than refused, so an odd authored id never loses the answer itself.
    function safeId(v) {
      if (v == null) { return null; }
      v = String(v).toLowerCase().replace(/[^a-z0-9:#._-]+/g, '-').slice(0, 200);
      return v || null;
    }
    var rungSent = {};                         // question id → when a row naming its rung last went
    function post(d) {
      if (muted) { return; }                   // a restored answer, already in the ledger
      if (d.rung != null && d.question_id) { rungSent[d.question_id] = Date.now(); }
      var t = carried(d, ('__t' in d) ? d.__t : spans(1)[0]);
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
      inflight[body.client_event_id] = 1;
      token().then(function (tok) { return tok ? send(body, tok, true) : false; }).then(function (ok) {
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
      if (!list.length || muted) { return; }
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
    // fix 2 (display-only): a KS4 classic option whose label was shortened keeps its stored text on data-full.
    function sentOpt(b) { return b.hasAttribute('data-full') ? (b.getAttribute('data-full') || '').trim() : (b.textContent || '').trim(); }
    function later(fn) { setTimeout(function () { try { fn(); } catch (e) { /* never breaks a page */ } }, 0); }
    /* Saved-work helpers (16 Oct 2026). `same` compares two pieces of text as
       the ledger stored them (whitespace runs collapsed); `quizKey` is the
       server's normaliseQuizText (consumer/answers.js) — the text a KS4 quiz
       card's id is hashed from — so a card is matched to its saved row by the
       very text the id came from. `byId` groups the child's rows per question,
       oldest first; the last of a group is the latest attempt. */
    function same(a, b) {
      return String(a == null ? '' : a).replace(/\s+/g, ' ').trim() === String(b == null ? '' : b).replace(/\s+/g, ' ').trim();
    }
    function quizKey(t) {
      var x = String(t == null ? '' : t);
      try { x = x.normalize('NFKC'); } catch (e) { /* old browser */ }
      return x.replace(/^\s*\d+[.)]\s+/, '').replace(/\s+/g, ' ').trim().toLowerCase();
    }
    /* The best whole round on any earlier day: for each of those days, the latest
       answer to every question so far, scored as the lesson scores it (a rung counts
       when all its questions are right), and only once every question has one. */
    function bestBefore(rungs, hidden, ids) {
      var today = new Date().toDateString(), days = {};
      var at = function (ri, n) { return ids[pilotId(pathSlug, 'r' + (ri + 1) + '-' + (n + 1))] || []; };
      var right = function (r, list, it, ri) {
        if ((it.kind || 'mcq') === 'chain') { r = list[scoredAt(list)]; }
        if (typeof r.is_correct === 'boolean') { return r.is_correct; }
        var mk = it.marks || [1, 3, 3, 6][ri];
        return typeof r.marks_scored === 'number' && r.marks_scored >= Math.ceil(mk / 2);
      };
      rungs.forEach(function (items, ri) {
        items.forEach(function (it, n) {
          at(ri, n).forEach(function (r) {
            var d = r.answered_at ? new Date(r.answered_at) : null;
            if (d && d.toDateString() !== today) { days[d.toDateString()] = d.getTime(); }
          });
        });
      });
      var best = null;
      Object.keys(days).forEach(function (day) {
        var end = new Date(day).getTime() + 864e5, score = 0, whole = true;
        rungs.forEach(function (items, ri) {
          var all = items.length > 0;
          items.forEach(function (it, n) {
            var list = at(ri, n).filter(function (r) { return r.answered_at && new Date(r.answered_at).getTime() < end; });
            if (!list.length) { whole = false; all = false; return; }
            if (!right(list[list.length - 1], list, it, ri)) { all = false; }
          });
          if (!items.length) { whole = false; }
          if (all) { score += 1; }
        });
        if (whole && (best === null || score > best)) { best = score; }
      });
      return best;
    }
    if (window.KS4 && typeof window.KS4.load === 'function' && typeof window.KS4.save === 'function') {
      var ks4Load = window.KS4.load, ks4Save = window.KS4.save;
      window.KS4.load = function (key, fb) { return /^ks4-best-/.test(String(key)) ? fb : ks4Load(key, fb); };
      window.KS4.save = function (key, v) { if (!/^ks4-best-/.test(String(key))) { ks4Save(key, v); } };
    }
    function byId(rows) {
      var out = {};
      (rows || []).forEach(function (r) {
        if (!r || !r.question_id) { return; }
        (out[r.question_id] = out[r.question_id] || []).push(r);
      });
      return out;
    }
    function lastOf(list) { return list && list.length ? list[list.length - 1] : null; }
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
           activities never mark), so it is sent unmarked.
         · a prediction ([data-activity] that is not an instrument, with
           options and a reveal — shared/ks3.js `wirePredictions`): every
           changed pick, unmarked, with the reveal as what the page showed.
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
      var optLabel = function (b) { return b.hasAttribute && b.hasAttribute('data-full') ? txt({ textContent: b.getAttribute('data-full') }) : txt(b.querySelector('.ks3-opt-label') || b); }; // fix 2: a shortened label still sends its stored text (data-full)
      // What the child was asked: the commit line where the block has one,
      // else the block's own headings and paragraphs above its options
      // (a "Think again" block: the quoted idea, then the ask).
      // ⊕ 14 Oct 2026: only what is ON SCREEN is the question. Text in a
      // hidden reveal (an answer not yet shown) and a progress counter
      // ("0 of 5 ruled on", `data-count`) never were, and are left out.
      var onScreen = function (el) {
        return !el.closest('[hidden]') && !el.hasAttribute('data-count') &&
               !!(el.getClientRects && el.getClientRects().length);
      };
      var promptOf = function (sec) {
        var c = sec.querySelector('.ks3-commit');
        if (c) { return txt(c); }
        var out = [], kids = sec.children || [];
        for (var i = 0; i < kids.length; i += 1) {
          var el = kids[i];
          if (el.querySelector && (el.matches('.ks3-options') || el.querySelector('.ks3-option'))) { break; }
          if (/^(P|H2|H3)$/.test(el.tagName) && !el.classList.contains('ks3-eyebrow')) { if (onScreen(el)) { out.push(txt(el)); } }
          else if (el.querySelector) {
            var q = el.querySelectorAll('h2, h3, p:not(.ks3-eyebrow)');
            for (var j = 0; j < q.length; j += 1) { if (onScreen(q[j])) { out.push(txt(q[j])); } }
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
         else the answer is sent unmarked with what the page revealed in
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
      /* ⊕ 9 Nov 2026: a blind run found five rulings stored under one id, shown as
         "1 of 5". UNIT_RE only knows the unit words most kinds use. These kinds
         call their unit something else, so it is named here (a selector), which
         tools/kp_ks3_units.py reads too. TAB_NOT_OPTION: a `.ks3-option` that only
         chooses what is on screen, never an answer. REVEAL_KEY: kinds whose reveal
         opens with the right option in the lesson's own words ("Flawed — …"). */
      var UNIT_BY_KIND = {"ks3-rplan-block":"[data-rplan-step]","ks3-gplot-block":"[data-gplot-read]","ks3-mb-block":".ks3-mb-step","ks3-board":".ks3-board-panel","ks3-removal-block":".ks3-removal-panel","ks3-sab-block":".ks3-sab-panel","ks3-switch-block":".ks3-switch-panel","ks3-seq-block":"[data-seq-step]"};
      var TAB_NOT_OPTION = {"ks3-sc-block":".ks3-sc-tab","ks3-ml-block":"[data-ml-amount]","ks3-tb-block":"[data-tb-food]","ks3-cl-block":"[data-cl-chain]"};
      var REVEAL_KEY = {"ks3-rplan-block":1,"ks3-esort-block":1,"ks3-tsort-block":1,"ks3-bottle-block":1,"ks3-gapfill-block":1,"ks3-pdeck-block":1,"ks3-pcards-block":1,"ks3-ruse-block":1,"ks3-prop-block":1,"ks3-psort-block":1,"ks3-ajudge-block":1};
      var isOption = function (btn) {
        if (!(optAttr(btn) || (btn.classList && btn.classList.contains('ks3-option')))) { return false; }
        var s0 = btn.closest && btn.closest('[data-instrument]'), k0 = s0 && kindOf(s0, TAB_NOT_OPTION);
        return !(k0 && btn.matches(TAB_NOT_OPTION[k0]));
      };
      // The option the unit's reveal names first, exactly one or none.
      var revealKey = function (scope, opts) {
        var rev = scope.querySelector('[data-reveal]');
        if (!rev) {
          var els = scope.querySelectorAll('*');
          for (var q = 0; q < els.length && !rev; q += 1) {
            var at = els[q].attributes || [];
            for (var w = 0; w < at.length; w += 1) { if (/^data-[a-z0-9]+-reveal$/.test(at[w].name)) { rev = els[q]; break; } }
          }
        }
        if (!rev) { return null; }
        var first = rev.firstElementChild || rev;
        var lead = txt(first).split(/ — |\. |: /)[0].toLowerCase().replace(/[.\s]+$/, '');
        if (!lead) { return null; }
        var whole = function (hay, nee) { return (' ' + hay.replace(/[^a-z0-9.%-]+/g, ' ') + ' ').indexOf(' ' + nee.replace(/[^a-z0-9.%-]+/g, ' ').trim() + ' ') >= 0; };
        var hits = opts.filter(function (o) {
          var l = optLabel(o).toLowerCase().replace(/[.\s]+$/, '');
          return l && (whole(lead, l) || whole(l, lead));
        });
        return hits.length === 1 ? hits[0] : null;
      };
      var unitOf = function (btn, sec) {
        var named = kindOf(sec, UNIT_BY_KIND);
        if (named) {
          var ue = btn.closest(UNIT_BY_KIND[named]);
          if (ue && sec.contains(ue)) {
            return { el: ue, key: 'named=' + Array.prototype.indexOf.call(sec.querySelectorAll(UNIT_BY_KIND[named]), ue) };
          }
        }
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
        /* ⊕ 14 Oct 2026 — the question AS SHOWN: the block's own ask (its
           heading, "Acid, alkali or neutral? Commit on all eight.") and then
           the unit's words ("Lemon juice kitchen"). A card alone lost the
           ask. A block-wide unit (no unit element: a step of a method, a
           scenario tab) reads the nearest box around the pressed option that
           has words of its own, never the whole block — the whole block
           carried every other step and, before onScreen, their hidden
           verdicts. Only visible lines; never an option's own label. Ids are
           untouched: they never came from this text. */
        var lineTest = function (el) {
          return /^(P|H2|H3|H4|LI)$/.test(el.tagName) && onScreen(el) && !el.querySelector('button') &&
                 !SHOWN_RE.test(Object.keys(el.dataset || {}).join('-'));
        };
        var near = scope;
        if (scope === sec) {
          near = sec;
          for (var up = btn.parentElement; up && up !== sec; up = up.parentElement) {
            if (visibleText(up, lineTest)) { near = up; break; }
          }
        }
        var ask = '', hs = sec.querySelectorAll('h2, h3');
        for (var hi = 0; hi < hs.length; hi += 1) {
          if (!near.contains(hs[hi]) && onScreen(hs[hi]) && !hs[hi].closest('button')) { ask = txt(hs[hi]); break; }
        }
        var body = near === sec && sec.querySelector('.ks3-commit') ? promptOf(sec) : visibleText(near, lineTest);
        var prompt = ask && body.indexOf(ask) < 0 ? (body ? ask + ' — ' + body : ask) : body;
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
          if (verdict === null && kindOf(sec, REVEAL_KEY)) {
            var rk = revealKey(scope, opts);
            if (rk) { good = rk; verdict = rk === btn; }
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
               is_correct: right == null ? null : pick.getAttribute('data-opt') === right });
      };
      /* ── ⊕ 25 Oct 2026 (Mide's item 1): the rest of the KS3 instruments ──
         266 instrument blocks were handled by nothing above. Each kind was
         read in its shared/ks3.js wire function (tools/ks3_instrument_
         shapes.json): 158 have nothing to answer — reading-only panels and
         explorations (sliders, tabs, run buttons) — and are left alone. The
         108 that take an answer are named here, by kind, in four shapes:
           u — a choice taken at once: `opt` the commit control, its unit the
               nearest `unit` ancestor, or the pressed `tab` (the unit is the
               tab on screen), or the whole block. `commit` (optional) is a
               separate button that sends the pressed `opt`.
           c — several parts committed together by `check`: each `part`'s
               pressed choice is one answer (or, `whole`, one answer for all).
           t — typed or selected inputs committed by `check`: one written
               answer, self-checked (nothing on these pages marks them).
           o — an order built by pressing steps (`step`), committed when the
               last one is placed.
           l — a live puzzle with no Check (⊕ 8 Nov 2026): `read` says what a
               press left, `back` puts it back.
         Ids are the adapter-A scheme, `<slug>#<activity>-<n>`. `right` reads
         the page's OWN verdict a tick after the page has handled the press
         (an attribute, a class, a revealed word) and returns {ok, good}; a
         kind whose page never judges is sent self-checked, with the text the
         press revealed as `explanation`. Restore presses the same controls
         again, then the Check. */
      /* <ks3-specs> */
      var gateOpt = function (b) {
        var a = b.attributes || [];
        for (var i = 0; i < a.length; i += 1) { if (/^data-[a-z0-9]+-gopt$/.test(a[i].name)) { return true; } }
        return !!(b.closest && b.closest('[data-benchgate]') && b.classList.contains('ks3-option'));
      };
      var G = function () { return { t: 'u', opt: gateOpt, count: true }; };
      var attr = function (el, n) { return el ? el.getAttribute(n) : null; };
      var shownIn = function (root, sel) {
        var out = null;
        Array.prototype.forEach.call(root.querySelectorAll(sel), function (el) { if (!out && !el.closest('[hidden]') && el.getClientRects().length) { out = el; } });
        return out;
      };
      var byWord = function (word, opts) {
        var w = String(word || '').replace(/[.\s]+$/, '').trim().toLowerCase();
        for (var i = 0; i < opts.length; i += 1) { if (optLabel(opts[i]).replace(/[.\s]+$/, '').trim().toLowerCase() === w) { return opts[i]; } }
        return null;
      };
      var gridCells = function (p) {
        var cell = '[data-' + p + '-cell]', pred = '[data-' + p + '-opt]';
        return { t: 'l', press: cell,
          pre: function (sec) { var on = sec.querySelector(pred + '[aria-pressed="true"]'); return on || null; },
          read: function (sec, b, on) {
            var key = attr(b, 'data-' + p + '-cell'), all = sec.querySelectorAll(cell);
            var n = Array.prototype.indexOf.call(all, b) + 1;
            var verdict = sec.querySelector('[data-' + p + '-out="' + key + '"] .ks3-' + p + '-verdict');
            // Only where the page words it as a plain yes or no ("A reaction." / "No reaction.").
            var said = txt(verdict), no = /^no reaction/i.test(said), yes = /^a reaction/i.test(said);
            var ok = on && (yes || no) ? (attr(on, 'data-' + p + '-opt') === (yes ? 'yes' : 'no')) : null;
            return { n: n, answer: on ? optLabel(on) : 'Opened without predicting', ok: ok, ask: txt(sec.querySelector('[data-' + p + '-out="' + key + '"] .ks3-' + p + '-title')) };
          },
          back: function (sec, n, r) {
            var c = sec.querySelectorAll(cell)[n - 1];
            if (!c) { return; }
            Array.prototype.forEach.call(sec.querySelectorAll(pred), function (o) { if (same(optLabel(o), r.answer)) { o.click(); } });
            c.click();
          } };
      };
      var KS3_SPECS = {
        // Commit-before-explore gates (a prediction; nothing judges it).
        'ks3-abench-block': G(), 'ks3-alt-block': G(), 'ks3-bal-block': G(), 'ks3-bill-block': G(), 'ks3-btally-block': G(),
        'ks3-calor-block': G(), 'ks3-clamp-block': G(), 'ks3-cloop-block': G(), 'ks3-counter-block': G(), 'ks3-cundt-block': G(),
        'ks3-cut-block': G(), 'ks3-dipc-block': G(), 'ks3-dlane-block': G(), 'ks3-dprobe-block': G(), 'ks3-echo-block': G(),
        'ks3-fall-block': G(), 'ks3-fgauge-block': G(), 'ks3-fgrid-block': G(), 'ks3-ftank-block': G(), 'ks3-grun-block': G(),
        'ks3-hb-block': G(), 'ks3-joint-block': G(), 'ks3-junc-block': G(), 'ks3-lever-block': G(), 'ks3-lgate-block': G(),
        'ks3-lrace-block': G(), 'ks3-lrange-block': G(), 'ks3-mcoil-block': G(), 'ks3-mrange-block': G(), 'ks3-mtbench-block': G(),
        'ks3-muscle-block': G(), 'ks3-parr-block': G(), 'ks3-pbench-block': G(), 'ks3-pinh-block': G(), 'ks3-plever-block': G(),
        'ks3-prism-block': G(), 'ks3-rbench-block': G(), 'ks3-rblock-block': G(), 'ks3-rframe-block': G(), 'ks3-rsurf-block': G(),
        'ks3-rtank-block': G(), 'ks3-sbench-block': G(), 'ks3-scope-block': G(), 'ks3-slane-block': G(), 'ks3-slink-block': G(),
        'ks3-solen-block': G(), 'ks3-span-block': G(), 'ks3-spbench-block': G(), 'ks3-splot-block': G(), 'ks3-tgap-block': G(),
        'ks3-tpair-block': G(), 'ks3-vtap-block': G(), 'ks3-walk-block': G(), 'ks3-xfer-block': G(), 'ks3-sand-block-shell': G(),
        // Predictions with their own controls (one per block; re-asked runs are new attempts).
        'ks3-bbench-block': { t: 'u', opt: '[data-bbench-predict] .ks3-option', commit: '[data-bbench-run]' },
        'ks3-burner-block': { t: 'u', opt: '[data-burner-predict] .ks3-option' },
        'ks3-cryst-block': { t: 'u', opt: '[data-cryst-gate-opts] .ks3-option', commit: '[data-cryst-run]' },
        'ks3-trough-block': { t: 'u', opt: '[data-trough-opt]' },
        'ks3-still-block': { t: 'u', opt: '[data-still-predict] .ks3-option', unit: '[data-still-predict]' },
        'ks3-tempb-block': { t: 'u', opt: '[data-tempb-predict]', unit: '[data-tempb-card]' },
        // The bench must have run before a verdict counts: the page forgets one made before it.
        'ks3-mpb-block': { t: 'u', opt: '[data-mpb-verdict-btn]', first: '[data-mpb-run]' },
        // Choices the page judges, read from its markup.
        'ks3-gap-block': { t: 'u', opt: '[data-gap] .ks3-option',
          right: function (b, u, sec) {
            var want = attr(sec.querySelector('[data-gap]'), 'data-empty-choice');
            if (want == null) { return null; }
            return { ok: attr(b, 'data-i') === want, good: sec.querySelector('[data-gap] .ks3-option[data-i="' + want + '"]') };
          } },
        'ks3-chroma-block': { t: 'u', opt: '[data-chroma-pen]',
          right: function (b, u, sec) {
            var cfg = null;
            try { cfg = JSON.parse(attr(sec.querySelector('[data-chroma]'), 'data-cfg') || 'null'); } catch (e) { cfg = null; }
            if (!cfg || cfg.match == null) { return null; }
            return { ok: attr(b, 'data-chroma-pen') === String(cfg.match), good: sec.querySelector('[data-chroma-pen="' + cfg.match + '"]') };
          } },
        'ks3-rsort-block': { t: 'u', opt: '[data-rsort-btn]', unit: '[data-rsort-item]',
          right: function (b, u) {
            var rn = attr(u, 'data-renew');
            if (rn == null) { return null; }
            var want = rn === '1' ? 'renew' : 'finite';
            return { ok: attr(b, 'data-rsort-btn') === want, good: u.querySelector('[data-rsort-btn="' + want + '"]') };
          } },
        'ks3-predict-block': { t: 'u', opt: '.ks3-predict-btn', unit: '.ks3-predict',
          right: function (b, u) {
            var a = attr(u, 'data-answer');
            return a == null ? null : { ok: attr(b, 'data-i') === a, good: u.querySelector('.ks3-predict-btn[data-i="' + a + '"]') };
          } },
        'ks3-pwsort-block': { t: 'u', opt: '[data-pwsort-btn]', unit: '[data-pwsort-item]',
          right: function (b, u) {
            var p = attr(u, 'data-ispower');
            if (p == null) { return null; }
            var want = p === '1' ? 'power' : 'energy';
            return { ok: attr(b, 'data-pwsort-btn') === want, good: u.querySelector('[data-pwsort-btn="' + want + '"]') };
          } },
        'ks3-sortcards-block': { t: 'u', opt: '.ks3-sortcards-opt', unit: '.ks3-sortcards-card',
          right: function (b, u) {
            var a = attr(u, 'data-answer');
            return a == null ? null : { ok: attr(b, 'data-choice') === a, good: u.querySelector('.ks3-sortcards-opt[data-choice="' + a + '"]') };
          } },
        'ks3-ebench-block': { t: 'u', opt: '.ks3-ebench-btn', unit: '.ks3-ebench-case',
          right: function (b, u) {
            var a = attr(u, 'data-ok');
            return a == null ? null : { ok: attr(b, 'data-call') === a, good: u.querySelector('.ks3-ebench-btn[data-call="' + a + '"]') };
          } },
        'ks3-jobsort-block': { t: 'u', opt: '.ks3-jobsort-opt', unit: '.ks3-jobsort-item',
          right: function (b, u) {
            var w = u.querySelector('.ks3-jobsort-answer');
            var good = w ? byWord(txt(w), u.querySelectorAll('.ks3-jobsort-opt')) : null;
            return good ? { ok: good === b, good: good } : null;
          } },
        'ks3-vcards-block': { t: 'u', opt: '.ks3-vcard-opt', unit: '.ks3-vcard',
          right: function (b, u) {
            var w = u.querySelector('.ks3-vcard-answer');
            var good = w ? byWord(txt(w), u.querySelectorAll('.ks3-vcard-opt')) : null;
            return good ? { ok: good === b, good: good } : null;
          } },
        'ks3-budget-block': { t: 'u', opt: '.ks3-verdict-btn', unit: '.ks3-sample' },
        'ks3-amgrid-block': { t: 'u', opt: '[data-amgrid-predict]', tab: '[data-amgrid-cell]' },
        'ks3-catb-block': { t: 'u', opt: '[data-catb-predict]', tab: '[data-catb-tab]' },
        'ks3-phbench-block': { t: 'u', opt: '[data-phbench-guess]', tab: '[data-phbench-tab]' },
        'ks3-fsort-block': { t: 'u', opt: '.ks3-fsort-label', tab: '[data-fsort-tab]',
          right: function (b, u, sec, tab) {
            var d = tab && sec.querySelector('[data-fsort-data="' + attr(tab, 'data-fsort-tab') + '"]');
            var a = attr(d, 'data-answer');
            return a == null ? null : { ok: attr(b, 'data-fsort-label') === a, good: sec.querySelector('.ks3-fsort-label[data-fsort-label="' + a + '"]') };
          } },
        'ks3-xroute-block': { t: 'u', opt: '[data-xroute-method]', tab: '[data-xroute-ore]',
          right: function (b, u, sec, tab) {
            var out = tab && sec.querySelector('[data-xroute-out="' + attr(tab, 'data-xroute-ore') + ':' + attr(b, 'data-xroute-method') + '"]');
            var w = attr(out, 'data-works');
            if (w == null) { return null; }
            var fits = sec.querySelector('[data-xroute-out^="' + attr(tab, 'data-xroute-ore') + ':"][data-works="1"]');
            return { ok: w === '1', good: fits ? sec.querySelector('[data-xroute-method="' + attr(fits, 'data-xroute-out').split(':')[1] + '"]') : null };
          } },
        'ks3-specb-block': { t: 'u', opt: '[data-specb-mat]', tab: '[data-specb-jbtn]',
          right: function (b, u, sec, tab) {
            var job = tab && tab.closest('[data-specb-job]');
            var out = job && sec.querySelector('[data-specb-out="' + attr(job, 'data-specb-job') + ':' + attr(b, 'data-specb-mat') + '"]');
            var f = attr(out, 'data-fit');
            if (f == null) { return null; }
            var fits = sec.querySelector('[data-specb-out^="' + attr(job, 'data-specb-job') + ':"][data-fit="1"]');
            return { ok: f === '1', good: fits ? sec.querySelector('[data-specb-mat="' + attr(fits, 'data-specb-out').split(':')[1] + '"]') : null };
          } },
        'ks3-ccheck-block': { t: 'u', opt: '.ks3-ccheck-fault', tab: '[data-pick]', commit: '[data-ccheck-open]',
          right: function (b, u, sec, tab) {
            var v = tab && sec.querySelector('.ks3-ccheck-verdict[data-verdict="' + attr(tab, 'data-pick') + '"]');
            var a = attr(v, 'data-answer');
            return a == null ? null : { ok: attr(b, 'data-fault') === a, good: sec.querySelector('.ks3-ccheck-fault[data-fault="' + a + '"]') };
          } },
        // Several parts, one Check.
        'ks3-gas-block': { t: 'c', check: '[data-gas-open]', part: '.ks3-gas-row', opt: '.ks3-gas-choice',
          right: function (p) { var v = attr(p, 'data-verdict'); return v === 'right' ? true : v === 'wrong' ? false : null; },
          key: function (p) { return optLabel(p.querySelector('.ks3-gas-choice[data-choice="' + attr(p, 'data-change') + '"]')); } },
        'ks3-plate-block': { t: 'c', check: '[data-plate-open]', part: '.ks3-plate-row', opt: '.ks3-plate-band',
          right: function (p) { var v = attr(p, 'data-state'); return v === 'hit' ? true : v === 'miss' ? false : null; },
          key: function (p) { return optLabel(p.querySelector('.ks3-plate-band[data-band="' + attr(p, 'data-answer') + '"]')); } },
        'ks3-hard': { t: 'c', check: '[data-hard-reveal]', part: '.ks3-hardrow', opt: '.ks3-rung-chip',
          right: function (p) { var v = attr(p, 'data-right'); return v === '1' ? true : v === '0' ? false : null; },
          key: function (p) { return attr(p, 'data-answer'); } },
        'ks3-settles': { t: 'c', check: '[data-settle-reveal]', part: '.ks3-feature', opt: '.ks3-settle-choice', scope: '.ks3-case-panel',
          right: function (p, c) { var s = attr(p, 'data-settles'); return s == null || !c ? null : (attr(c, 'data-pick') === 'yes') === (s === '1'); },
          key: function (p) { return optLabel(p.querySelector('.ks3-settle-choice[data-pick="' + (attr(p, 'data-settles') === '1' ? 'yes' : 'no') + '"]')); } },
        'ks3-pairs': { t: 'c', check: '[data-pair-reveal]', part: '.ks3-pairrow', opt: '.ks3-pair-chip',
          right: function (p, c) {
            var w = p.querySelector('.ks3-pairrow-word');
            var good = w ? byWord(txt(w), p.querySelectorAll('.ks3-pair-chip')) : null;
            return good && c ? good === c : null;
          },
          key: function (p) { var w = p.querySelector('.ks3-pairrow-word'); var good = w ? byWord(txt(w), p.querySelectorAll('.ks3-pair-chip')) : null; return good ? optLabel(good) : null; } },
        'ks3-critique': { t: 'c', check: '[data-steps-reveal]', part: '.ks3-step', opt: '.ks3-step-btn', toggle: true,
          right: function (p, c) { var f = attr(p, 'data-fault'); return f == null ? null : !!c === (f === '1'); },
          key: function (p) { return attr(p, 'data-fault') === '1' ? 'Flagged' : 'Not flagged'; } },
        'ks3-saudit-block': { t: 'c', whole: true, check: '[data-saudit-check]', part: '.ks3-saudit-chip', opt: '.ks3-saudit-chip', toggle: true, tab: '[data-saudit-sc]',
          right: function (p, c, sec) { var v = shownIn(sec, '[data-saudit-vlabel]'); return v ? /balanced/i.test(txt(v)) && !/not/i.test(txt(v)) : null; },
          key: function (p, c, sec) {
            var sc = attr(sec.querySelector('[data-saudit-sc][aria-pressed="true"]'), 'data-saudit-sc');
            return sc ? Array.prototype.map.call(sec.querySelectorAll('.ks3-saudit-chip[data-saudit-want-' + sc + ']'), optLabel).join('\n') : null;
          } },
        'ks3-eqb-block': { t: 'c', whole: true, check: '[data-eqb-check]', part: '[data-eqb-row]', opt: '[data-eqb-place]', tab: '[data-eqb-tab]',
          right: function (p, c, sec) {
            var br = shownIn(sec, '[data-eqb-branch]');
            return br ? attr(br, 'data-eqb-branch') === 'perfect' : null;
          },
          key: function (p, c, sec) {
            var cfg = JSON.parse(attr(sec.querySelector('[data-eqb]'), 'data-eqb-cfg') || '{}');
            var tab = attr(sec.querySelector('[data-eqb-tab][aria-pressed="true"]'), 'data-eqb-tab');
            var one = (cfg.cases || []).filter(function (x) { return x.id === tab; })[0] || (cfg.cases || [])[0];
            return one ? 'Reactants: ' + (one.reactants || []).join(', ') + '\nProducts: ' + (one.products || []).join(', ') : null;
          } },
        'ks3-fit-block': { t: 'c', whole: true, check: '[data-fit-run]', part: '.ks3-fit-part', opt: '.ks3-fit-part', toggle: true, tab: '.ks3-fit-tab',
          right: function (p, c, sec) { var b = sec.querySelector('[data-fit-badge]'); var s = attr(b, 'data-state'); return s ? s === 'works' : null; },
          key: function (p, c, sec) {
            var spec = JSON.parse(attr(sec.querySelector('[data-fit-spec]'), 'data-fit-spec') || '{}'), on = attr(sec.querySelector('.ks3-fit-tab[aria-pressed="true"]'), 'data-fit');
            var one = (spec.specimens || []).filter(function (x) { return x.id === on; })[0];
            if (!one) { return null; }
            return Array.prototype.filter.call(sec.querySelectorAll('.ks3-fit-part'), function (b) {
              return Array.prototype.some.call(b.attributes, function (a) { return /^data-/.test(a.name) && one.needs.indexOf(a.value) >= 0; });
            }).map(optLabel).join('\n') || null;
          } },
        'ks3-jwalk-block': { t: 'c', whole: true, check: '[data-jwalk-send]', part: '[data-jwalk-seg]', opt: '[data-jwalk-mode]',
          right: function (p, c, sec) {
            var tg = attr(sec.querySelector('[data-jwalk]'), 'data-target');
            if (!tg) { return null; }
            var mine = Array.prototype.map.call(sec.querySelectorAll('[data-jwalk-seg]'), function (s) { return attr(s.querySelector('[data-jwalk-mode][aria-pressed="true"]'), 'data-jwalk-mode') || ''; });
            return mine.join('|') === tg;
          },
          key: function (p, c, sec) {
            var tg = String(attr(sec.querySelector('[data-jwalk]'), 'data-target') || '').split('|');
            return Array.prototype.map.call(sec.querySelectorAll('[data-jwalk-seg]'), function (s, i) {
              return (partWords(s) ? partWords(s) + ': ' : '') + optLabel(s.querySelector('[data-jwalk-mode="' + tg[i] + '"]'));
            }).join('\n');
          } },
        // Typed or selected, then shown: one written answer, self-checked.
        'ks3-construct-block': { t: 't', check: '[data-construct-check]', inputs: '[data-fifa-input]' },
        'ks3-lstep-block': { t: 't', check: '[data-lstep-open]', inputs: '[data-lstep-ans], [data-lstep-unit]', opt: '.ks3-lstep-opt' },
        'ks3-pick-block': { t: 't', check: '[data-pick-open]', inputs: '[data-pick-ans], [data-pick-unit]', opt: '.ks3-pick-opt' },
        'ks3-rwrite-block': { t: 't', check: '[data-rwrite-show]', inputs: '[data-rwrite-field]' },
        // ⊕ 8 Nov 2026 — a live puzzle, no Check: the page judges on every press.
        // `read` is what the press left (null: nothing to send yet), `back` puts it back.
        'ks3-dh-block': { t: 'l', press: '.ks3-dh-opt',
          read: function (sec) {
            var lines = [], mine = {};
            Array.prototype.forEach.call(sec.querySelectorAll('.ks3-dh-dial'), function (d) {
              var on = d.querySelector('.ks3-dh-opt[aria-pressed="true"]');
              if (!on) { return; }
              mine[attr(on, 'data-dh-dial')] = attr(on, 'data-dh-opt');
              lines.push(txt(d.querySelector('.ks3-dh-dialname')) + ': ' + optLabel(on));
            });
            var want = null;
            try { want = JSON.parse(attr(sec.querySelector('[data-dh]'), 'data-target') || 'null'); } catch (e) { want = null; }
            var ok = null;
            if (want) { ok = Object.keys(want).every(function (k) { return mine[k] === want[k]; }); }
            var good = null;
            if (want && ok === false) {
              good = Array.prototype.map.call(sec.querySelectorAll('.ks3-dh-dial'), function (d) {
                var o = Array.prototype.filter.call(d.querySelectorAll('.ks3-dh-opt'), function (b) { return want[attr(b, 'data-dh-dial')] === attr(b, 'data-dh-opt'); })[0];
                return txt(d.querySelector('.ks3-dh-dialname')) + ': ' + (o ? optLabel(o) : '');
              }).join('\n');
            }
            return { n: 1, answer: lines.join('\n'), ok: ok, good: good };
          },
          back: function (sec, n, r) {
            String(r.answer == null ? '' : r.answer).split('\n').forEach(function (ln) {
              var ix = ln.lastIndexOf(': '), name = ln.slice(0, ix), label = ln.slice(ix + 2);
              Array.prototype.forEach.call(sec.querySelectorAll('.ks3-dh-dial'), function (d) {
                if (ix < 0 || !same(txt(d.querySelector('.ks3-dh-dialname')), name)) { return; }
                Array.prototype.forEach.call(d.querySelectorAll('.ks3-dh-opt'), function (o) {
                  if (same(optLabel(o), label) && o.getAttribute('aria-pressed') !== 'true') { o.click(); }
                });
              });
            });
          } },
        // Sent when an equation balances (each press on the way is not an answer):
        // right when it is the page's own target, a whole multiple left unjudged,
        // as the page says "balanced" and gives it no tick.
        'ks3-cbal-block': { t: 'l', press: '[data-cbal-for]',
          read: function (sec, b) {
            var eq = b.closest('[data-cbal-eq]');
            var panel = eq && eq.querySelector('[data-cbal-balanced]');
            if (!panel || panel.hidden) { return null; }
            var id = attr(eq, 'data-cbal-eq'), tick = sec.querySelector('[data-cbal-tick="' + id + '"]');
            var eqs = Array.prototype.slice.call(sec.querySelectorAll('[data-cbal-eq]'));
            var tab = sec.querySelector('[data-cbal-tab="' + id + '"]');
            var cs = Array.prototype.map.call(eq.querySelectorAll('[data-cbal-coeff]'), function (c) { return txt(c); });
            var multiple = eq.querySelector('[data-cbal-note="multiple"]');
            return { n: eqs.indexOf(eq) + 1, answer: cs.join(', '),
                     ask: tab && tab.firstChild ? String(tab.firstChild.nodeValue || '').trim() : '',
                     ok: multiple && !multiple.hidden ? null : !!(tick && !tick.hidden) };
          },
          back: function (sec, n, r) {
            var eq = sec.querySelectorAll('[data-cbal-eq]')[n - 1];
            if (!eq) { return; }
            var tab = sec.querySelector('[data-cbal-tab="' + attr(eq, 'data-cbal-eq') + '"]');
            if (tab && tab.getAttribute('aria-pressed') !== 'true') { tab.click(); }
            String(r.answer == null ? '' : r.answer).split(', ').forEach(function (v, i) {
              var el = eq.querySelector('[data-cbal-coeff="' + i + '"]'), want = parseInt(v, 10);
              if (!el || isNaN(want)) { return; }
              for (var guard = 0; guard < 12 && parseInt(txt(el), 10) !== want; guard += 1) {
                var up = parseInt(txt(el), 10) < want;
                var btn = eq.querySelector('[data-cbal-for="' + i + '"][data-cbal-delta="' + (up ? '1' : '-1') + '"]');
                if (!btn || btn.getAttribute('aria-disabled') === 'true') { return; }
                btn.click();
              }
            });
          } },
        // ⊕ 9 Nov 2026: separately judged items that shared one id.
        'ks3-rd-block': { t: 'u', opt: '[data-rd-route]', tab: '[data-rd-case]', commit: '[data-rd-run]',
          right: function (b, u, sec, tab) {
            var cs = null;
            try { cs = JSON.parse(attr(sec.querySelector('[data-rd]'), 'data-cases') || 'null'); } catch (e) { cs = null; }
            var c = (cs || []).filter(function (x) { return tab && x.id === attr(tab, 'data-rd-case'); })[0];
            return c ? { ok: attr(b, 'data-rd-route') === c.answer, good: sec.querySelector('[data-rd-route="' + c.answer + '"]') } : null;
          } },
        'ks3-rgrid-block': { t: 'u', opt: '[data-rgrid-opt]', tab: '[data-rgrid-cell]',
          right: function (b, u, sec, tab) {
            var o = attr(tab, 'data-rgrid-outcome');
            if (o == null) { return null; }
            var want = o === 'reacts' ? 'yes' : 'no';
            return { ok: attr(b, 'data-rgrid-opt') === want, good: sec.querySelector('[data-rgrid-opt="' + want + '"]') };
          } },
        'ks3-tbench-block': { t: 'u', opt: '[data-predict] .ks3-option', dims: ['.ks3-tbench-tab[data-food]', '.ks3-tbench-tab[data-test]'],
          right: function (b, u, sec) { return shownIn(sec, '[data-verdict="hit"]') ? { ok: true, good: b } : shownIn(sec, '[data-verdict="miss"]') ? { ok: false, good: null } : null; } },
        'ks3-switch-block': { t: 'u', opt: '.ks3-switch-predict .ks3-option', unit: '.ks3-switch-panel', unitTab: '.ks3-switch-tab', commit: '[data-switch]' },
        'ks3-mb-block': { t: 'c', whole: true, check: '[data-mb-run]', part: '.ks3-mb-step', opt: '.ks3-mb-opt' },
        'ks3-sc-block': { t: 'u', opt: '.ks3-sc-verdict', tab: '.ks3-sc-tab', commit: '[data-sc-check]',
          right: function (b, u, sec, tab) {
            var panel = tab && sec.querySelector('[data-sc-panel="' + attr(tab, 'data-sc-case') + '"]');
            var a = attr(panel, 'data-sc-answer');
            return a == null ? null : { ok: attr(b, 'data-sc-verdict') === a, good: panel.querySelector('.ks3-sc-verdict[data-sc-verdict="' + a + '"]') };
          } },
        'ks3-vp-block': { t: 'u', opt: '[data-vp-pred]', unit: '[data-vp-charpanel]', unitTab: '[data-vp-char]', commit: '[data-vp-plot]',
          right: function (b, u) {
            var el = u.querySelector('[data-vp-type]') || (u.hasAttribute('data-vp-type') ? u : null), want = attr(el, 'data-vp-type');
            return want == null ? null : { ok: attr(b, 'data-vp-pred') === want, good: u.querySelector('[data-vp-pred="' + want + '"]') };
          } },
        'ks3-chain-block': { t: 'u', opt: '[data-chain-slot] .ks3-option', unit: '[data-chain-slot]',
          right: function (b, u, sec) {
            var ideal = attr(sec.querySelector('[data-chain]'), 'data-chain-ideal'), slot = attr(u, 'data-chain-slot'), m = new RegExp('(?:^|,)' + slot + ':(\\d+)').exec(ideal || '');
            return m ? { ok: attr(b, 'data-i') === m[1], good: u.querySelector('.ks3-option[data-i="' + m[1] + '"]') } : null;
          } },
        'ks3-fault-block': { t: 'u', opt: '[data-fault] .ks3-option', tab: '.ks3-fault-tab', commit: '[data-fault-open]',
          right: function (b, u, sec, tab) {
            var rv = tab && sec.querySelector('.ks3-fault-reveal[data-factor="' + attr(tab, 'data-factor') + '"]');
            var a = attr(rv, 'data-answer');
            return a == null ? null : { ok: attr(b, 'data-part') === a, good: sec.querySelector('.ks3-option[data-part="' + a + '"]') };
          } },
        // ⊕ 9 Nov 2026: the chips stay changeable until the reveal, so that is the answer.
        // The question under the reveal is a press of its own (`also`), with the ids it always had.
        'ks3-sort': { t: 'c', check: '[data-sort-reveal]', part: '.ks3-sortrow', opt: '.ks3-sort-chip',
          right: function (p, c) {
            var w = p.querySelector('.ks3-sort-answer');
            var good = w ? byWord(txt(w), p.querySelectorAll('.ks3-sort-chip')) : null;
            return good && c ? good === c : null;
          },
          key: function (p) { var w = p.querySelector('.ks3-sort-answer'); var good = w ? byWord(txt(w), p.querySelectorAll('.ks3-sort-chip')) : null; return good ? optLabel(good) : null; },
          also: { t: 'u', opt: '[data-selfcheck] .ks3-option', unit: '.ks3-sortrow, [data-selfcheck]' } },
        // A cell of a grid opens its own outcome; the prediction pressed before it belongs to that cell.
        'ks3-hgrid-block': gridCells('hgrid'),
        'ks3-raudit-block': gridCells('raud'),
        // The rig the child built, each time they ran it. Nothing judges a rig.
        'ks3-rigb-block': { t: 'l', press: '[data-rigb-run]',
          read: function (sec) {
            var lines = [];
            Array.prototype.forEach.call(sec.querySelectorAll('.ks3-rigb-dial'), function (d) {
              var on = d.querySelector('[data-rigb-for][aria-pressed="true"]');
              if (on) { lines.push(txt(d.querySelector('.ks3-rigb-diallabel')) + ': ' + optLabel(on)); }
            });
            return { n: 1, answer: lines.join('\n'), ok: null, again: true };
          },
          back: function (sec, n, r) {
            String(r.answer == null ? '' : r.answer).split('\n').forEach(function (ln) {
              var ix = ln.lastIndexOf(': '), name = ln.slice(0, ix), label = ln.slice(ix + 2);
              Array.prototype.forEach.call(sec.querySelectorAll('.ks3-rigb-dial'), function (d) {
                if (ix < 0 || !same(txt(d.querySelector('.ks3-rigb-diallabel')), name)) { return; }
                Array.prototype.forEach.call(d.querySelectorAll('[data-rigb-for]'), function (o) {
                  if (same(optLabel(o), label) && o.getAttribute('aria-pressed') !== 'true') { o.click(); }
                });
              });
            });
            var run = sec.querySelector('[data-rigb-run]');
            if (run) { run.click(); }
          } },
        // An order built step by step.
        'ks3-grain-block': { t: 'o', step: '[data-grain-pick]', clear: '[data-grain-reset]', badge: '[data-grain-badge]',
          key: function (sec) {
            return Array.prototype.slice.call(sec.querySelectorAll('[data-grain-pick]')).sort(function (a, b) { return parseInt(attr(a, 'data-grain-rank'), 10) - parseInt(attr(b, 'data-grain-rank'), 10); })
              .map(function (b) { return optLabel(b).replace(/^\d+\s*/, ''); }).join('\n');
          },
          done: function (sec) { return shownIn(sec, '[data-grain-verdict]'); },
          right: function (sec) { return shownIn(sec, '[data-grain-verdict="right"]') ? true : shownIn(sec, '[data-grain-verdict="wrong"]') ? false : null; } },
        'ks3-morder-block': { t: 'o', step: '[data-morder-step]', clear: '[data-morder-clear]',
          done: function (sec) { return shownIn(sec, '[data-morder-answer]'); },
          key: function (sec) { return txt(shownIn(sec, '[data-morder-answer]')) || null; },
          right: function (sec) { return shownIn(sec, '[data-morder-verdict="right"]') ? true : shownIn(sec, '[data-morder-verdict="wrong"]') ? false : null; } }
      };
      /* </ks3-specs> */
      window.MrBadmusAnswerCapture.ks3Specs = KS3_SPECS;   // read by activity_save_drive.py --sweep
      var specOf = function (sec) { var k = kindOf(sec, KS3_SPECS); return k ? KS3_SPECS[k] : null; };
      var matches = function (el, sel) { return typeof sel === 'function' ? sel(el) : !!(el.matches && el.matches(sel)); };
      var allIn = function (root, sel) {
        return Array.prototype.filter.call(root.querySelectorAll(typeof sel === 'function' ? 'button' : sel), function (b) { return matches(b, sel); });
      };
      var pressedTab = function (sec, sp) {
        var tabs = sec.querySelectorAll(sp.tab), on = null, n = 0;
        for (var i = 0; i < tabs.length; i += 1) { if (tabs[i].getAttribute('aria-pressed') === 'true' || tabs[i].getAttribute('aria-selected') === 'true') { on = tabs[i]; n = i + 1; } }
        return { el: on, n: n };
      };
      // The words on screen in a box (no buttons), for "what the press revealed".
      var linesOf = function (root) {
        var out = [];
        Array.prototype.forEach.call(root.querySelectorAll('p, li, h3, h4, strong, dd, td'), function (el) {
          if (el.closest('button') || !onScreen(el)) { return; }
          var t2 = txt(el);
          if (t2 && out.indexOf(t2) < 0) { out.push(t2); }
        });
        return out;
      };
      var askOf = function (sec, unitEl, btn) {
        var head = '', hs = sec.querySelectorAll('h2, h3');
        for (var i = 0; i < hs.length; i += 1) { if (onScreen(hs[i]) && !hs[i].closest('button')) { head = txt(hs[i]); break; } }
        var commit = null, cs = sec.querySelectorAll('.ks3-commit');
        for (var j = 0; j < cs.length; j += 1) { if (onScreen(cs[j]) && cs[j].compareDocumentPosition(btn) & 4) { commit = cs[j]; } }
        var own = unitEl ? linesOf(unitEl).filter(function (l) { return l !== head; }).slice(0, 2).join(' ') : '';
        var parts = [head, commit ? txt(commit) : '', own].filter(Boolean);
        return parts.filter(function (x, k) { return parts.indexOf(x) === k; }).join(' — ');
      };
      var specSent = {};                       // question_id → the answer last sent
      // Two sets of tabs choose one unit between them (a food and a test).
      var dimN = function (sec, sp) {
        var n = 0, mult = 1;
        sp.dims.slice().reverse().forEach(function (sel) {
          var tabs = sec.querySelectorAll(sel), on = 0;
          for (var i = 0; i < tabs.length; i += 1) { if (tabs[i].getAttribute('aria-pressed') === 'true') { on = i; } }
          n += on * mult; mult *= tabs.length;
        });
        return n + 1;
      };
      /* ⊕ 9 Nov 2026 (F9): a commit-first bench saves its one commitment, and its
         "3 of 3 states seen" came back "1 of 3". Which controls moved that count are
         the child's own, not an answer: they are kept with the self-ticks on the
         commitment's row, as the position of each control, and pressed again. */
      var countSeen = {};
      var isRecord = function (b) { return Array.prototype.some.call(b.attributes || [], function (a) { return /^data-[a-z0-9]+-record$/.test(a.name); }); };
      var countTrack = function (sp, sec, t, slug) {
        if (!sp.count) { return; }
        var b = t.closest('button'), cnt = sec.querySelector('[data-count]');
        if (!b || !cnt || !sec.contains(b) || matches(b, sp.opt)) { return; }
        // ⊕ 10 Nov 2026: a Record press makes a reading from wherever the bench is set, so
        // pressing it again on return would record the bench as it is now, not as it was.
        if (isRecord(b)) { return; }
        var id = slug + '#' + (sec.getAttribute('data-activity') || 'block') + '-1';
        var pos = Array.prototype.indexOf.call(sec.querySelectorAll('button'), b) + 1;
        if (pos < 1 || pos > 20) { return; }
        var was = txt(cnt);
        var look = function () {
          if (txt(cnt) === was || (countSeen[id] || []).indexOf(pos) >= 0) { return; }
          countSeen[id] = (countSeen[id] || []).concat([pos]);
          sendTicks(id, countSeen[id]);
        };
        later(look);
        setTimeout(function () { try { look(); } catch (e) { /* never breaks a page */ } }, 1500);
      };
      var specU = function (sp, t, sec, slug) {
        var act = sec.getAttribute('data-activity') || 'block';
        var btn = null, viaCommit = false;
        if (sp.commit) {
          var cb = t.closest(sp.commit);
          if (cb && sec.contains(cb)) { viaCommit = true; btn = cb; }
        }
        if (!btn) {
          for (var el = t; el && el !== sec; el = el.parentNode) { if (el.tagName === 'BUTTON' && matches(el, sp.opt)) { btn = el; break; } }
        }
        if (!btn || btn.disabled) { return; }
        if (sp.commit && !viaCommit) { return; }          // the option alone is not the answer: its Check is
        var unitEl = null, n = 1, tab = null;
        if (sp.dims) { n = dimN(sec, sp); }
        else if (sp.tab) { var pt = pressedTab(sec, sp); tab = pt.el; n = pt.n || 1; }
        else if (sp.unit) {
          unitEl = btn.closest(sp.unit) || (viaCommit ? shownIn(sec, sp.unit) : null);
          if (!unitEl || !sec.contains(unitEl)) { return; }
          n = Array.prototype.indexOf.call(sec.querySelectorAll(sp.unit), unitEl) + 1;
        }
        var opt = viaCommit ? (function () {
          var on = allIn(unitEl || sec, sp.opt).filter(function (o) { return o.getAttribute('aria-pressed') === 'true'; });
          return on[on.length - 1] || null;
        })() : btn;
        if (!opt) { return; }
        if (!viaCommit && opt.getAttribute('aria-pressed') === 'true') { return; }   // already the choice: nothing new
        var id = slug + '#' + act + '-' + n;
        var scope = unitEl || sec;
        var before = linesOf(scope), ask = askOf(sec, unitEl, opt);
        later(function () {
          // The page took it: the option is now the pressed one (or a judged
          // control with no pressed state at all changed what is shown).
          var pressed = opt.getAttribute('aria-pressed');
          var after = linesOf(scope);
          if (pressed === 'false' && !viaCommit) { return; }
          if (pressed == null && after.join('\n') === before.join('\n')) { return; }
          var shown = after.filter(function (l) { return before.indexOf(l) < 0; }).join(' ');
          var v = sp.right ? sp.right(opt, unitEl, sec, tab) : null;
          var d = { __block: scope, key_stage: 'KS3', lesson_slug: slug, question_id: id, rung: null, kind: 'choice',
                    question_text: ask, answer: optLabel(opt), explanation: shown || null };
          if (v && typeof v.ok === 'boolean') {
            d.is_correct = v.ok;
            d.correct_answer = v.good ? optLabel(v.good) : (v.ok ? optLabel(opt) : null);
          } else { d.is_correct = null; d.correct_answer = null; }
          specSent[id] = d.answer;
          post(d);
        });
      };
      // A part's own words, without its buttons' labels.
      var partWords = function (el) {
        var out = [];
        (function walk(n) {
          for (var c = n.firstChild; c; c = c.nextSibling) {
            if (c.nodeType === 3) { out.push(c.nodeValue); }
            else if (c.nodeType === 1 && c.tagName !== 'BUTTON' && !c.hasAttribute('hidden') && c.tagName.toLowerCase() !== 'svg') { walk(c); }
          }
        })(el);
        return out.join(' ').replace(/\s+/g, ' ').trim();
      };
      var partChoice = function (sp, part) {
        if (sp.toggle) { var tb = part.matches(sp.opt) ? part : part.querySelector(sp.opt); return tb && tb.getAttribute('aria-pressed') === 'true' ? tb : null; }
        var on = Array.prototype.filter.call(part.querySelectorAll(sp.opt), function (o) { return o.getAttribute('aria-pressed') === 'true'; });
        return on[on.length - 1] || null;
      };
      // The answer the page holds, asked for only when the child's was wrong.
      var specKey = function (sp, p, c, sec, ok) {
        if (ok !== false || !sp.key) { return null; }
        try { return sp.key(p, c, sec) || null; } catch (e) { return null; }
      };
      var specC = function (sp, t, sec, slug) {
        var chk = t.closest(sp.check);
        if (!chk || !sec.contains(chk) || chk.disabled) { return; }
        var act = sec.getAttribute('data-activity') || 'block';
        var box = (sp.scope && chk.closest(sp.scope)) || sec;
        var tn = 0;
        if (sp.tab) { tn = pressedTab(sec, sp).n; }
        var allParts = Array.prototype.slice.call(sec.querySelectorAll(sp.part));
        var parts = Array.prototype.filter.call(box.querySelectorAll(sp.part), function (p) { return !sp.tab || onScreen(p) || p.closest('[hidden]') === null; });
        var picked = parts.map(function (p) {
          var c = partChoice(sp, p);
          var label = sp.toggle ? (c ? optLabel(sp.opt && p.matches(sp.opt) ? p : c) : null) : (c ? optLabel(c) : null);
          return { p: p, c: c, n: allParts.indexOf(p) + 1, label: label, words: linesOf(p).join(' ') || optLabel(p) };
        });
        var ask = askOf(sec, null, chk);
        later(function () {
          if (sp.whole) {
            var chosen = picked.filter(function (x) { return x.c; });
            var answer = chosen.map(function (x) { return sp.toggle ? x.label : (partWords(x.p) ? partWords(x.p) + ': ' : '') + x.label; }).join('\n');
            var id = slug + '#' + act + '-' + (tn || 1);
            var ok = sp.right ? sp.right(null, null, sec) : null;
            var d = { __block: sec, key_stage: 'KS3', lesson_slug: slug, question_id: id, rung: null, kind: 'choice', question_text: ask,
                      answer: answer, correct_answer: specKey(sp, null, null, sec, ok), is_correct: typeof ok === 'boolean' ? ok : null };
            post(d);
            return;
          }
          var batch = [];
          picked.forEach(function (x) {
            if (!sp.toggle && !x.c) { return; }
            var id = slug + '#' + act + '-' + x.n;
            var label = sp.toggle ? (x.c ? 'Flagged' : 'Not flagged') : x.label;
            if (specSent[id] === label) { return; }               // unchanged since it was last sent
            specSent[id] = label;
            var ok = sp.right ? sp.right(x.p, x.c, sec) : null;
            var d = { __block: sec, key_stage: 'KS3', lesson_slug: slug, question_id: id, rung: null, kind: 'choice',
                      question_text: ask + (x.words ? ' — ' + x.words : ''), answer: label, correct_answer: specKey(sp, x.p, x.c, sec, ok),
                      is_correct: typeof ok === 'boolean' ? ok : null };
            batch.push(d);
          });
          postAll(batch);
        });
      };
      var specT = function (sp, t, sec, slug) {
        var chk = t.closest(sp.check);
        if (!chk || !sec.contains(chk) || chk.disabled) { return; }
        var act = sec.getAttribute('data-activity') || 'block';
        var lines = [];
        if (sp.opt) {
          Array.prototype.forEach.call(sec.querySelectorAll(sp.opt), function (o) { if (o.getAttribute('aria-pressed') === 'true') { lines.push(optLabel(o)); } });
        }
        // ⊕ 10 Nov 2026: one box and nothing else is the child's words alone; the box's
        // label goes in only where it tells several boxes apart.
        var tIns = sec.querySelectorAll(sp.inputs), alone = tIns.length === 1 && !sp.opt;
        Array.prototype.forEach.call(tIns, function (inp) {
          var l = inp.id ? sec.querySelector('label[for="' + inp.id + '"]') : null;
          var v = inp.tagName === 'SELECT' ? (inp.options[inp.selectedIndex] ? txt(inp.options[inp.selectedIndex]) : '') : String(inp.value || '').trim();
          lines.push((l && !alone ? txt(l) + ': ' : '') + v);
        });
        var ask = askOf(sec, null, chk), before = linesOf(sec);
        later(function () {
          var after = linesOf(sec);
          if (after.join('\n') === before.join('\n') && !chk.disabled) { return; }   // the page refused (not ready)
          post({ __block: sec, key_stage: 'KS3', lesson_slug: slug, question_id: slug + '#' + act + '-1', rung: null, kind: 'written',
                 question_text: ask, answer: lines.join('\n'), correct_answer: null, is_correct: null,
                 explanation: after.filter(function (l) { return before.indexOf(l) < 0; }).join(' ') || null });
        });
      };
      var specO = function (sp, t, sec, slug) {
        var st = t.closest(sp.step);
        if (!st || !sec.contains(st) || st.disabled) { return; }
        var act = sec.getAttribute('data-activity') || 'block', ask = askOf(sec, null, st);
        later(function () {
          if (!sp.done(sec)) { return; }
          var steps = Array.prototype.slice.call(sec.querySelectorAll(sp.step));
          var badge = function (s) { var b = s.querySelector(sp.badge || '[data-morder-badge]'); var n = parseInt(b ? txt(b) : '', 10); return isNaN(n) ? 99 : n; };
          steps.sort(function (a, b) { return badge(a) - badge(b); });
          var ok = sp.right(sec);
          var d = { __block: sec, key_stage: 'KS3', lesson_slug: slug, question_id: slug + '#' + act + '-1', rung: null, kind: 'order',
                    question_text: ask, answer: steps.map(function (s) { return optLabel(s).replace(/^\d+\s*/, ''); }).join('\n'),
                    correct_answer: sp.key ? sp.key(sec) : null, is_correct: typeof ok === 'boolean' ? ok : null };
          post(d);
        });
      };
      var specL = function (sp, t, sec, slug) {
        var b = t.closest(sp.press);
        if (!b || !sec.contains(b) || b.disabled || b.getAttribute('aria-disabled') === 'true' || b.getAttribute('aria-pressed') === 'true') { return; }
        var act = sec.getAttribute('data-activity') || 'block', ask = askOf(sec, null, b);
        var pre = sp.pre ? sp.pre(sec, b) : null;
        later(function () {
          var v = sp.read(sec, b, pre);
          if (!v) { return; }
          var id = slug + '#' + act + '-' + v.n;
          if (specSent[id] === v.answer && !v.again) { return; }
          specSent[id] = v.answer;
          var d = { __block: sec, key_stage: 'KS3', lesson_slug: slug, question_id: id, rung: null, kind: 'choice',
                    question_text: ask + (v.ask ? ' — ' + v.ask : ''), answer: v.answer, correct_answer: v.good || null,
                    is_correct: typeof v.ok === 'boolean' ? v.ok : null };
          post(d);
        });
      };
      var specCapture = function (sp, t, sec, slug) {
        if (sp.also) { specCapture(sp.also, t, sec, slug); }
        if (sp.t === 'u') { specU(sp, t, sec, slug); }
        else if (sp.t === 'c') { specC(sp, t, sec, slug); }
        else if (sp.t === 't') { specT(sp, t, sec, slug); }
        else if (sp.t === 'o') { specO(sp, t, sec, slug); }
        else if (sp.t === 'l') { specL(sp, t, sec, slug); }
      };
      document.addEventListener('click', function (e) {
        try {
          var t = e.target;
          if (!t || !t.closest) { return; }
          var slug = ks3Slug();
          // Round 4: question-shaped instruments (adapters A and B5C above).
          var bsec = t.closest('[data-instrument]');
          if (bsec && !bsec.hasAttribute('data-keyedblock')) {
            var sp0 = specOf(bsec);
            if (sp0) { countTrack(sp0, bsec, t, slug); specCapture(sp0, t, bsec, slug); return; }
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
                       correct_answer: null, is_correct: null });
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
                     is_correct: null });
            } else if (!sec.hasAttribute('data-instrument')) {
              // ⊕ 25 Oct 2026 (commitNoReveal): a "commit first" choice with
              // nothing revealed on the block itself (a practical's first
              // question). Every changed pick, self-checked.
              post({ __block: sec, key_stage: 'KS3', lesson_slug: slug, question_id: slug + '#' + act, rung: null,
                     kind: 'choice', question_text: promptOf(sec), answer: optLabel(opt),
                     correct_answer: null, is_correct: null });
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
            draftDrop(cfaId(q, pre, csec));
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

      /* ⊕ 9 Nov 2026: "Your turn" lines typed and not yet checked (draftPut). */
      var cfaInput = function (el) {
        var a = el.attributes || [];
        for (var i = 0; i < a.length; i += 1) { var m = /^(data-p\d+cfa)-input$/.exec(a[i].name); if (m) { return m[1]; } }
        return null;
      };
      var cfaId = function (q, pre, csec) {
        var n = parseInt(q.getAttribute(pre + '-q'), 10);
        return ks3Slug() + '#' + (csec.getAttribute('data-activity') || 'your-turn') + '-' + ((isNaN(n) ? 0 : n) + 1);
      };
      document.addEventListener('input', function (e) {
        var t = e.target, pre = t && t.getAttribute ? cfaInput(t) : null;
        if (!pre) { return; }
        var q = t.closest('[' + pre + '-q]'), csec = t.closest('[data-activity]');
        if (!q || !csec) { return; }
        var vals = Array.prototype.map.call(q.querySelectorAll('[' + pre + '-input]'), function (i) { return i.value || ''; });
        if (vals.some(function (v) { return v.trim(); })) { draftPut(cfaId(q, pre, csec), vals); } else { draftDrop(cfaId(q, pre, csec)); }
      }, true);
      window.MrBadmusAnswerCapture.afterReplay.push(function () {
        var seen = [];
        Array.prototype.forEach.call(document.querySelectorAll('input, textarea, select'), function (el) {
          var pre = cfaInput(el), q = pre && el.closest('[' + pre + '-q]'), csec = q && el.closest('[data-activity]');
          if (!csec || seen.indexOf(q) >= 0) { return; }
          seen.push(q);
          var rev = q.querySelector('[' + pre + '-reveal]'), id = cfaId(q, pre, csec);
          if (rev && !rev.hasAttribute('hidden')) { draftDrop(id); return; }
          var vals = draftGet(id), ins = q.querySelectorAll('[' + pre + '-input]');
          if (!Array.isArray(vals) || Array.prototype.some.call(ins, function (i) { return (i.value || '').trim(); })) { return; }
          draftTake(id);
          Array.prototype.forEach.call(ins, function (i, k) {
            i.value = vals[k] == null ? '' : vals[k];
            try { i.dispatchEvent(new Event('input', { bubbles: true })); } catch (e) { /* old browser */ }
          });
        });
      });
      /* ⊕ 10 Nov 2026: the question the child was on, on this device. Restoring answers
         presses Check on every question, so the tab is put back last of all. */
      var cfaTabOf = function (el) {
        var a = el.attributes || [];
        for (var i = 0; i < a.length; i += 1) { var m = /^(data-p\d+cfa)-tab$/.exec(a[i].name); if (m) { return m[1]; } }
        return null;
      };
      document.addEventListener('click', function (e) {
        if (muted) { return; }
        var tb = e.target && e.target.closest ? e.target.closest('button') : null, pre = tb && cfaTabOf(tb), csec = pre && tb.closest('[data-activity]');
        if (csec) { draftPut(ks3Slug() + '#' + csec.getAttribute('data-activity') + '~tab', tb.getAttribute(pre + '-tab')); }
      }, true);
      window.MrBadmusAnswerCapture.afterReplay.push(function () {
        Array.prototype.forEach.call(document.querySelectorAll('[data-activity]'), function (csec) {
          var tabs = Array.prototype.filter.call(csec.querySelectorAll('button'), function (b) { return !!cfaTabOf(b); });
          if (!tabs.length) { return; }
          var pre = cfaTabOf(tabs[0]), want = draftGet(ks3Slug() + '#' + csec.getAttribute('data-activity') + '~tab');
          var tab = tabs.filter(function (b) { return b.getAttribute(pre + '-tab') === String(want == null ? tabs[0].getAttribute(pre + '-tab') : want); })[0];
          if (tab && tab.getAttribute('aria-pressed') !== 'true') { tab.click(); }
        });
      });

      /* ⊕ 9 Nov 2026: every other field in a KS3 activity that nothing has sent yet:
         typed text, a number, a slider, a dropdown. Same rule as above: on this
         device, for this child, cleared once the value has gone in an answer. A field
         only takes its draft if it still holds what it held when the child began, so
         a saved answer always beats it. The ladder keeps its own text (shared/ks3.js). */
      var FIELD = 'input:not([type=checkbox]):not([type=radio]):not([type=file]):not([type=hidden]):not([type=button]):not([type=submit]), textarea, select';
      var fieldKey = function (el) {
        if (!el || !el.matches || !el.matches(FIELD) || cfaInput(el) || el.closest('.ks3-ladder')) { return null; }
        var fsec = el.closest('[data-activity]');
        if (!fsec) { return null; }
        return ks3Slug() + '#' + fsec.getAttribute('data-activity') + '~' + (el.id || Array.prototype.indexOf.call(fsec.querySelectorAll(FIELD), el));
      };
      var fieldTap = function (e) {
        if (muted) { return; }
        var el = e.target, k = fieldKey(el);
        if (!k) { return; }
        if (!Object.prototype.hasOwnProperty.call(el, '__mrbBase')) { el.__mrbBase = el.tagName === 'SELECT' ? (el.options[0] ? el.options[0].value : '') : el.defaultValue; }
        el.__mrbDraftKey = k;
        if (el.value === el.__mrbBase) { draftDrop(k); } else { draftPut(k, { val: el.value, base: el.__mrbBase }); }
      };
      document.addEventListener('input', fieldTap, true);
      document.addEventListener('change', fieldTap, true);
      window.MrBadmusAnswerCapture.afterReplay.push(function () {
        Array.prototype.forEach.call(document.querySelectorAll('[data-activity]'), function (fsec) {
          Array.prototype.forEach.call(fsec.querySelectorAll(FIELD), function (el) {
            var k = fieldKey(el);
            if (!k) { return; }
            var raw = draftGet(k);
            el.__mrbBase = el.value;
            if (!raw || typeof raw !== 'object') { return; }
            if (benchHeld && el.type === 'range') { draftDrop(k); return; }   // the saved calculation set this bench
            if (el.disabled || el.value !== raw.base) { draftDrop(k); return; }
            el.__mrbBase = raw.base;
            el.value = raw.val;
            if (el.value !== raw.val) { el.value = raw.base; draftDrop(k); return; }   // the page no longer offers it
            draftTake(k);
            el.__mrbDraftKey = k;
            el.__mrbCarry = draftCarry[k];
            delete draftCarry[k];
            try { el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })); } catch (e) { /* old browser */ }
          });
        });
        // A ladder rung's text the page itself put back: the time since load is not how long it took.
        Array.prototype.forEach.call(document.querySelectorAll('.ks3-ladder [data-answer]'), function (el) {
          if ((el.value || '').trim()) { el.__mrbCarry = null; }
        });
      });

      /* ⊕ 9 Nov 2026: picks on a block with its own Check or Run, not yet committed. Not
         an answer, so nothing is sent; pressed again on return, on this device, after the
         saved rows have gone back, and forgotten once an answer from the block is sent. */
      var pickLogged = function (lsec) {
        var sp = specOf(lsec);
        if (sp && (sp.commit || sp.t === 'c')) { return sp.commit || sp.check; }
        return kindOf(lsec, KIND_B5C) ? '[data-b5c-check]' : null;
      };
      var pickKey = function (lsec) { return ks3Slug() + '#' + lsec.getAttribute('data-activity') + '~picks'; };
      document.addEventListener('click', function (e) {
        if (muted) { return; }
        var b = e.target && e.target.closest ? e.target.closest('button') : null;
        var lsec = b && !b.disabled ? b.closest('[data-activity]') : null;
        var commit = lsec && !lsec.closest('.ks3-ladder') ? pickLogged(lsec) : null;
        if (!commit || b.closest(commit)) { return; }
        var list = draftGet(pickKey(lsec));
        lsec.__mrbPickKey = pickKey(lsec);
        draftPut(pickKey(lsec), (Array.isArray(list) ? list : []).concat([Array.prototype.indexOf.call(lsec.querySelectorAll('button'), b)]));
      }, true);
      window.MrBadmusAnswerCapture.afterReplay.push(function () {
        Array.prototype.forEach.call(document.querySelectorAll('[data-activity]'), function (lsec) {
          if (!pickLogged(lsec)) { return; }
          var key = pickKey(lsec), list = draftGet(key);
          if (!Array.isArray(list) || !list.length) { return; }
          lsec.__mrbPickKey = key;
          draftTake(key);
          lsec.__mrbPickCarry = draftCarry[key];
          delete draftCarry[key];
          list.forEach(function (at) {
            var b = lsec.querySelectorAll('button')[at];
            if (b && !b.disabled) { b.click(); }
          });
        });
      });

      /* ⊕ 9 Nov 2026: a "3 of 6 opened" count on a block that takes no answer. It is
         not work to mark, so it is kept on this device, and comes back by pressing the
         same controls again. <ks3-count-local> is checked against the pages by
         activity_save_drive --units. */
      var COUNT_LOCAL = /* <ks3-count-local> */ /\bks3-(ab|ahist|amix|ba|bb|becomes|bell|cd|clock|cross|cy|dial|elay|erun|fm|fold|gcmp|ghouse|gut|jobsw|ledger|lt|mloop|nr|od|parrow|pb|pc|qb|route|rr|rs|scale|shell|srig|ss|stock|tpl|zb)-block\b/ /* </ks3-count-local> */;
      var countKey = function (lsec) { return ks3Slug() + '#' + lsec.getAttribute('data-activity') + '~count'; };
      document.addEventListener('click', function (e) {
        if (muted) { return; }
        var b = e.target && e.target.closest ? e.target.closest('button') : null;
        var lsec = b && b.closest('[data-activity]');
        if (!lsec || !COUNT_LOCAL.test(lsec.className)) { return; }
        var cnt = lsec.querySelector('[data-count]');
        if (!cnt) { return; }
        var was = cnt.textContent, at = Array.prototype.indexOf.call(lsec.querySelectorAll('button'), b);
        setTimeout(function () {
          if (cnt.textContent === was) { return; }
          var list = draftGet(countKey(lsec));
          draftPut(countKey(lsec), (Array.isArray(list) ? list : []).concat([at]));
        }, 0);
      }, true);
      window.MrBadmusAnswerCapture.afterReplay.push(function () {
        Array.prototype.forEach.call(document.querySelectorAll('[data-activity]'), function (lsec) {
          if (!COUNT_LOCAL.test(lsec.className) || !lsec.querySelector('[data-count]')) { return; }
          var list = draftGet(countKey(lsec));
          if (!Array.isArray(list)) { return; }
          list.forEach(function (at) {
            var b = lsec.querySelectorAll('button')[at];
            if (b && !b.disabled) { b.click(); }
          });
        });
      });

      /* ── Saved work follow-up: "Your turn" ticks ("I had this") ──
         Read a tick after the page has flipped it; the whole set of ticked
         lines for that question goes to sendTicks (above). */
      document.addEventListener('click', function (e) {
        var tb = e.target && e.target.closest ? e.target.closest('.ks3-cfa-tick') : null;
        if (!tb) { return; }
        later(function () {
          var pre = null, a = tb.attributes || [];
          for (var i = 0; i < a.length && !pre; i += 1) { var m = /^(data-p\d+cfa)-tick$/.exec(a[i].name); if (m) { pre = m[1]; } }
          var q = pre ? tb.closest('[' + pre + '-q]') : null;
          var csec = tb.closest('[data-activity]');
          if (!q || !csec) { return; }
          var n = parseInt(q.getAttribute(pre + '-q'), 10);
          var list = [];
          Array.prototype.forEach.call(q.querySelectorAll('[' + pre + '-tick]'), function (x) {
            if (x.getAttribute('aria-pressed') === 'true') { list.push(parseInt(x.getAttribute(pre + '-tick'), 10) + 1); }
          });
          sendTicks(ks3Slug() + '#' + (csec.getAttribute('data-activity') || 'your-turn') + '-' + ((isNaN(n) ? 0 : n) + 1), list);
        });
      }, false);

      /* ── Saved work, KS3: everything OUTSIDE the ladder ──
         (The ladder puts its own rungs back — shared/ks3.js wireLadder.)
         Each saved answer is given again, oldest first, through the page's
         own control: the same option pressed, the same "Your turn" lines
         typed and checked. So the page ends in exactly the state the child
         left it in — a changed guess shows the latest guess, an instrument
         shows every unit committed — and every lock, reveal, rail stop and
         progress count is the page's own doing. `mute` is held by the loader
         throughout, so none of it is sent again. Ids are read the way the
         capture above WRITES them (slug#start, slug#<activity>,
         slug#<activity>-<n>). */
      /* ⊕ 10 Nov 2026: a run recorded in a bench's results table (the calorimeter). Each
         is a row of its own, numbered as the table numbers it, with the table's own cells;
         nothing judges a run. On return the same run is made again through the page:
         the food, the mass, a full burn, Record. The page's figures depend only on the
         food and the mass, so the table comes back as it was. A run recorded part-way
         through a burn comes back as a full burn of the mass that had gone. */
      var RECORDS = {
        'ks3-calor-block': { rec: '[data-calor-record]', rows: '[data-calor-rows] tr',
          /* Only a run the slider can hold exactly is made again: a part-way burn
             (0.07 g on a slider that starts at 0.1) would come back as other numbers. */
          can: function (sec, cells) {
            var food = Array.prototype.filter.call(sec.querySelectorAll('[data-calor-food]'), function (b) { return same(txt(b), cells[0]); })[0];
            var slider = sec.querySelector('[data-calor-mass]'), mass = parseFloat(String(cells[1] || ''));
            if (!food || !slider || isNaN(mass)) { return false; }
            var lo = parseFloat(slider.min), hi = parseFloat(slider.max), st = parseFloat(slider.step) || 0;
            if (mass < lo - 1e-9 || mass > hi + 1e-9) { return false; }
            return !st || Math.abs((mass - lo) / st - Math.round((mass - lo) / st)) < 1e-6;
          },
          put: function (sec, cells, done) {
            var food = Array.prototype.filter.call(sec.querySelectorAll('[data-calor-food]'), function (b) { return same(txt(b), cells[0]); })[0];
            var slider = sec.querySelector('[data-calor-mass]'), burn = sec.querySelector('[data-calor-burn]');
            var mass = parseFloat(String(cells[1] || ''));
            if (!food || !slider || !burn || isNaN(mass)) { done(); return; }
            food.click();
            slider.value = String(mass);
            try { slider.dispatchEvent(new Event('input', { bubbles: true })); } catch (e) { /* old browser */ }
            burn.click();
            var t0 = Date.now();
            (function wait() {
              if (burn.disabled || Date.now() - t0 > 8000) {
                var rec = sec.querySelector('[data-calor-record]');
                if (rec && !rec.disabled) { rec.click(); }
                done();
                return;
              }
              setTimeout(wait, 60);
            })();
          } }
      };
      document.addEventListener('click', function (e) {
        var b = e.target && e.target.closest ? e.target.closest('button') : null;
        var rsec = b && !b.disabled ? b.closest('[data-instrument]') : null;
        var spec = rsec ? RECORDS[kindOf(rsec, RECORDS)] : null;
        if (!spec || !b.matches(spec.rec)) { return; }
        var before = rsec.querySelectorAll(spec.rows).length, slug = ks3Slug(), act = rsec.getAttribute('data-activity') || 'block';
        later(function () {
          var trs = rsec.querySelectorAll(spec.rows);
          if (trs.length <= before) { return; }
          var tr = trs[trs.length - 1], cells = Array.prototype.map.call(tr.children, txt);
          var heads = Array.prototype.map.call(rsec.querySelectorAll('thead th'), txt);
          post({ __block: rsec, key_stage: 'KS3', lesson_slug: slug, question_id: slug + '#' + act + '-run-' + cells[0], rung: null, kind: 'numeric',
                 question_text: (txt(rsec.querySelector('h2')) || act) + ' — ' + (heads[0] || 'Run') + ' ' + cells[0] + ': ' + heads.slice(1).join(', '),
                 answer: cells.slice(1).join(' · '), correct_answer: null, is_correct: null });
        });
      }, true);
      replay.push(function (rows) {
        var todo = [];
        Array.prototype.forEach.call(document.querySelectorAll('[data-instrument]'), function (rsec) {
          var spec = RECORDS[kindOf(rsec, RECORDS)];
          if (!spec) { return; }
          var pre = ks3Slug() + '#' + (rsec.getAttribute('data-activity') || 'block') + '-run-', mine = {};
          (rows || []).forEach(function (r) { if (String(r.question_id || '').indexOf(pre) === 0) { mine[r.question_id] = r; } });
          var runs = Object.keys(mine).sort(function (a, b) { return parseInt(a.slice(pre.length), 10) - parseInt(b.slice(pre.length), 10); }).map(function (q) {
            return { sec: rsec, spec: spec, cells: String(mine[q].answer || '').split(' · ') };
          });
          // All or none: a table missing one run would renumber the rest.
          if (runs.every(function (r) { return !spec.can || spec.can(r.sec, r.cells); })) { todo = todo.concat(runs); }
        });
        if (!todo.length) { return; }
        // Runs take the page's own time to burn: the answers they make are held back throughout.
        var cap = window.MrBadmusAnswerCapture;
        cap.mute(true);
        setTimeout(function next() {
          var one = todo.shift();
          if (!one) { cap.mute(false); return; }
          try { one.spec.put(one.sec, one.cells, function () { setTimeout(next, 30); }); } catch (e) { setTimeout(next, 30); }
        }, 0);
      });

      /* ⊕ 10 Nov 2026: a "Your turn" that reads its numbers live off a bench on the page
         ("Your spanner: 40 N at 0.05 m") would otherwise be marked against wherever the
         bench happens to sit now. Before its lines go back, the bench is set to what the
         saved question says: a button showing that value is pressed, or a slider that
         makes the question read it is moved. Nothing else on the bench is touched, and
         the bench's own unsent slider drafts then stand down (benchHeld). */
      var benchHeld = false;
      var benchTo = function (csec, head, want) {
        var tpl = head && head.getAttribute('data-template');
        if (!tpl || !want || txt(head) === want) { return; }
        var keys = [];
        var re = new RegExp('^' + tpl.replace(/[.*+?^$()|[\]\\]/g, '\\$&').replace(/\{(\w+)\}/g, function (all, k) { keys.push(k); return '(.+?)'; }) + '$');
        var m = re.exec(want);
        if (!m) { return; }
        var root = csec.closest('.ks3-lesson') || document, used = [];
        var blocks = Array.prototype.filter.call(root.querySelectorAll('[data-instrument]'), function (b) { return b !== csec; });
        keys.forEach(function (k, i) {
          var val = m[i + 1];
          if (head.textContent.indexOf(val) >= 0 && txt(head) === want) { return; }
          var hit = null;
          blocks.forEach(function (b) {
            Array.prototype.forEach.call(b.querySelectorAll('button[aria-pressed]'), function (btn) { if (!hit && txt(btn) === val) { hit = btn; } });
          });
          if (hit) { if (hit.getAttribute('aria-pressed') !== 'true') { hit.click(); } return; }
          var n = parseFloat(String(val).replace('\u2212', '-'));
          if (isNaN(n)) { return; }
          blocks.forEach(function (b) {
            Array.prototype.forEach.call(b.querySelectorAll('input[type="range"]'), function (rg) {
              if (hit || used.indexOf(rg) >= 0 || n < parseFloat(rg.min) || n > parseFloat(rg.max)) { return; }
              var old = rg.value;
              rg.value = String(n);
              try { rg.dispatchEvent(new Event('input', { bubbles: true })); rg.dispatchEvent(new Event('change', { bubbles: true })); } catch (e) { /* old browser */ }
              var parts = re.exec(txt(head));
              if (parts && parts[i + 1] === val) { hit = rg; used.push(rg); return; }
              rg.value = old;
              try { rg.dispatchEvent(new Event('input', { bubbles: true })); rg.dispatchEvent(new Event('change', { bubbles: true })); } catch (e) { /* old browser */ }
            });
          });
        });
        benchHeld = true;
      };
      /* Saved work for the <ks3-specs> kinds: the same controls pressed
         again, in the unit (or on the tab) the id numbers, then the Check. */
      var specPend = [];
      var slug0 = function (sec) { return ks3Slug() + '#' + (sec.getAttribute('data-activity') || 'block'); };
      var specBack = function (sp, sec, n, r) {
        var click = function (b) { if (b && !b.disabled) { b.click(); } };
        var press = function (list, label) {
          for (var i = 0; i < list.length; i += 1) {
            if (same(optLabel(list[i]), label)) { if (list[i].getAttribute('aria-pressed') !== 'true') { click(list[i]); } return list[i]; }
          }
          return null;
        };
        if (sp.t === 'l') { sp.back(sec, n, r); return; }
        var lines = String(r.answer == null ? '' : r.answer).split('\n');
        if (sp.dims) {
          var left = n - 1, sizes = sp.dims.map(function (sel) { return sec.querySelectorAll(sel).length; });
          sp.dims.forEach(function (sel, di) {
            var below = 1;
            for (var dj = di + 1; dj < sizes.length; dj += 1) { below *= sizes[dj]; }
            var want = Math.floor(left / below); left -= want * below;
            var tb = sec.querySelectorAll(sel)[want];
            if (tb && tb.getAttribute('aria-pressed') !== 'true') { click(tb); }
          });
        }
        if (sp.tab) {
          var tabs = sec.querySelectorAll(sp.tab);
          if (tabs[n - 1] && tabs[n - 1].getAttribute('aria-pressed') !== 'true') { click(tabs[n - 1]); }
        }
        if (sp.t === 'u') {
          var scope = sp.unit ? sec.querySelectorAll(sp.unit)[n - 1] : sec;
          if (!scope) { return; }
          if (sp.first) { click(sec.querySelector(sp.first)); }
          if (sp.unitTab) { click(sec.querySelectorAll(sp.unitTab)[n - 1]); }
          var hit = press(allIn(scope, sp.opt), r.answer);
          if (hit && sp.commit) { click(scope.querySelector(sp.commit) || sec.querySelector(sp.commit)); }
          if (hit && sp.after) { var af = scope.querySelector(sp.after); if (af) { click(af); } }
          if (hit && sp.count && ownTicks(r)) {
            var bs0 = sec.querySelectorAll('button'), kept = [];
            ownTicks(r).forEach(function (pos) {
              if (bs0[pos - 1] && !isRecord(bs0[pos - 1])) { click(bs0[pos - 1]); kept.push(pos); }
            });
            countSeen[slug0(sec) + '-1'] = kept;
          }
          return;
        }
        if (sp.t === 'c') {
          if (sp.whole) {
            var parts = Array.prototype.filter.call(sec.querySelectorAll(sp.part), function (p) { return p.closest('[hidden]') === null; });
            if (sp.toggle) {
              var j = 0;
              parts.forEach(function (p) {
                var tb = p.matches(sp.opt) ? p : p.querySelector(sp.opt);
                if (!tb) { return; }
                var want = j < lines.length && same(optLabel(tb), lines[j]);
                if (want) { j += 1; }
                if ((tb.getAttribute('aria-pressed') === 'true') !== want) { click(tb); }
              });
            } else {
              lines.forEach(function (ln) {
                var ix = ln.lastIndexOf(': '), words = ix >= 0 ? ln.slice(0, ix) : '', label = ix >= 0 ? ln.slice(ix + 2) : ln;
                for (var k = 0; k < parts.length; k += 1) {
                  if (!words || same(partWords(parts[k]), words)) { if (press(parts[k].querySelectorAll(sp.opt), label)) { return; } }
                }
              });
            }
            click(sec.querySelector(sp.check));
            return;
          }
          var part = sec.querySelectorAll(sp.part)[n - 1];
          if (!part) { if (sp.also) { specBack(sp.also, sec, n, r); } return; }
          if (sp.toggle) {
            var tb2 = part.matches(sp.opt) ? part : part.querySelector(sp.opt);
            if (tb2 && (tb2.getAttribute('aria-pressed') === 'true') !== (r.answer === 'Flagged')) { click(tb2); }
          } else { press(part.querySelectorAll(sp.opt), r.answer); }
          var box = (sp.scope && part.closest(sp.scope)) || sec, chk = box.querySelector(sp.check);
          if (chk && specPend.indexOf(chk) < 0) { specPend.push(chk); }
          return;
        }
        if (sp.t === 't') {
          var optLabels = sp.opt ? Array.prototype.map.call(sec.querySelectorAll(sp.opt), function (o) { return optLabel(o); }) : [];
          var rest = [];
          lines.forEach(function (ln) {
            if (sp.opt && optLabels.some(function (l) { return same(l, ln); })) { press(sec.querySelectorAll(sp.opt), ln); }
            else { rest.push(ln); }
          });
          var ins = sec.querySelectorAll(sp.inputs);
          if (ins.length === 1 && !sp.opt) { rest = [rest.join('\n')]; }
          Array.prototype.forEach.call(ins, function (inp, k) {
            var l = inp.id ? sec.querySelector('label[for="' + inp.id + '"]') : null, v = rest[k] == null ? '' : rest[k];
            var lt = l ? txt(l) + ': ' : '';
            if (lt && v.indexOf(lt) === 0) { v = v.slice(lt.length); }
            if (inp.tagName === 'SELECT') {
              for (var q = 0; q < inp.options.length; q += 1) { if (same(txt(inp.options[q]), v)) { inp.selectedIndex = q; } }
            } else { inp.value = v; }
            try { inp.dispatchEvent(new Event('input', { bubbles: true })); inp.dispatchEvent(new Event('change', { bubbles: true })); } catch (e) { /* old browser */ }
          });
          click(sec.querySelector(sp.check));
          return;
        }
        if (sp.t === 'o') {
          var steps = Array.prototype.slice.call(sec.querySelectorAll(sp.step));
          if (steps.some(function (s2) { return s2.disabled; })) { click(sec.querySelector(sp.clear)); }
          lines.forEach(function (ln) {
            for (var k = 0; k < steps.length; k += 1) {
              if (!steps[k].disabled && same(optLabel(steps[k]).replace(/^\d+\s*/, ''), ln)) { click(steps[k]); return; }
            }
          });
        }
      };
      replay.push(function (rows) {
        var slug = ks3Slug();
        var acts = {};
        Array.prototype.forEach.call(document.querySelectorAll('[data-activity]'), function (el) {
          var a = el.getAttribute('data-activity');
          if (a && !acts[a] && !el.closest('.ks3-ladder')) { acts[a] = el; }
        });
        var pressOpt = function (list, label) {
          for (var i = 0; i < list.length; i += 1) {
            if (same(optLabel(list[i]), label)) {
              if (list[i].getAttribute('aria-pressed') !== 'true' && !list[i].disabled) { list[i].click(); }
              return;
            }
          }
        };
        var one = function (key, r) {
          if (key === 'start') {
            var hook = acts.hook;
            var kd = hook && hook.hasAttribute('data-keyedblock') ? hook.querySelector('[data-keyed]') : null;
            if (kd) { pressOpt(kd.querySelectorAll('.ks3-option'), r.answer); }
            return;
          }
          var sec = acts[key];
          if (sec && !(sec.hasAttribute('data-instrument') && !sec.hasAttribute('data-keyedblock'))) {
            var keyed = sec.hasAttribute('data-keyedblock') ? sec.querySelector('[data-keyed]') : null;
            pressOpt((keyed || sec).querySelectorAll('.ks3-option'), r.answer);
            return;
          }
          var m = /^(.+)-(\d+)$/.exec(key);
          if (!m || !acts[m[1]]) { return; }
          sec = acts[m[1]];
          var n = parseInt(m[2], 10);
          var spr = specOf(sec);
          if (spr) { specBack(spr, sec, n, r); return; }
          if (r.answer_kind === 'written') {
            // "Your turn": the five lines, typed back, then checked.
            var pre = null, bs = sec.querySelectorAll('button');
            for (var i = 0; i < bs.length && !pre; i += 1) { pre = cfaPrefix(bs[i]); }
            if (!pre) { return; }
            var q = sec.querySelector('[' + pre + '-q="' + (n - 1) + '"]');
            if (!q) { return; }
            var rev = q.querySelector('[' + pre + '-reveal]');
            // The child's own "I had this" ticks, as they were saved (an
            // older row without them leaves the ticks as the page has them).
            var putTicks = function () {
              var own3 = ownTicks(r);
              if (!own3) { return; }
              Array.prototype.forEach.call(q.querySelectorAll('[' + pre + '-tick]'), function (tb) {
                var want = own3.indexOf(parseInt(tb.getAttribute(pre + '-tick'), 10) + 1) >= 0;
                if ((tb.getAttribute('aria-pressed') === 'true') !== want && !tb.disabled) { tb.click(); }
              });
            };
            if (rev && !rev.hasAttribute('hidden')) { putTicks(); return; }       // already open
            benchTo(sec, q.querySelector('[' + pre + '-head]'), String(r.question_text || ''));
            var lines = String(r.answer || '').split('\n');
            var ins = q.querySelectorAll('[' + pre + '-input]');
            for (var k = 0; k < ins.length; k += 1) {
              var lab = ins[k].id ? q.querySelector('label[for="' + ins[k].id + '"]') : null;
              var line = lines[k] == null ? '' : lines[k];
              var lt = lab ? txt(lab) : '';
              if (lt && line.indexOf(lt + ': ') === 0) { line = line.slice(lt.length + 2); }
              ins[k].value = line;
              try { ins[k].dispatchEvent(new Event('input', { bubbles: true })); } catch (e) { /* old browser */ }
            }
            var chk = q.querySelector('[' + pre + '-check]');
            if (chk && !chk.disabled) { chk.click(); }
            putTicks();
            return;
          }
          if (kindOf(sec, KIND_B5C)) {
            var w = sec.querySelector('[data-b5c]') || sec;
            var tabs = w.querySelectorAll('[data-b5c-pick]');
            var item = tabs[n - 1] ? tabs[n - 1].getAttribute('data-b5c-pick') : null;
            if (!item) { return; }
            if (tabs[n - 1].getAttribute('aria-pressed') !== 'true') { tabs[n - 1].click(); }
            pressOpt(w.querySelectorAll('.ks3-b5c-opt[data-owner="' + item + '"]'), r.answer);
            var c5 = w.querySelector('[data-b5c-check]');
            if (c5 && !c5.disabled) { c5.click(); }
            return;
          }
          if (kindOf(sec, KIND_A)) {
            var keys = [], opts = [], all = sec.querySelectorAll('button');
            for (var j = 0; j < all.length; j += 1) {
              if (!isOption(all[j]) || all[j].closest('.ks3-ladder')) { continue; }
              var uk = unitOf(all[j], sec).key;
              if (keys.indexOf(uk) < 0) { keys.push(uk); }
              if (keys.indexOf(uk) === n - 1) { opts.push(all[j]); }
            }
            pressOpt(opts, r.answer);
          }
        };
        (rows || []).forEach(function (r) {
          var id = String(r.question_id || '');
          if (id.indexOf(slug + '#') !== 0 || /#(recall|apply|explain|produce)$/.test(id)) { return; }
          try { one(id.slice(slug.length + 1), r); } catch (e) { /* one block never stops the rest */ }
        });
        // The Checks of the part-by-part blocks, once all their parts are back.
        specPend.splice(0).forEach(function (c) { try { if (c && !c.disabled) { c.click(); } } catch (e) { /* never breaks a page */ } });
      });
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
            answer: sentOpt(btn),
            correct_answer: opts[right] ? sentOpt(opts[right]) : null,
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

    /* ── Saved work, KS4 classic: the quiz cards ──
       A card's saved row is found by the card's own question text (its id is
       hashed from exactly that), and the option the child chose is pressed
       again: the card's script marks it, shows the feedback and moves the
       progress line, as it did live. Only the FIRST resolution was ever sent
       and the card locks after it, so the first row is the one. (The matching
       exercise is drag-placed and is not put back.) */
    replay.push(function (rows) {
      var first = {};
      (rows || []).forEach(function (r) {
        if (!r || !/^ks4q:/.test(String(r.question_id || '')) || r.answer_kind !== 'choice') { return; }
        var k = quizKey(r.question_text);
        if (!(k in first)) { first[k] = r; }
      });
      Array.prototype.forEach.call(document.querySelectorAll('.quiz-card'), function (card) {
        if (card.hasAttribute('data-answered')) { return; }
        var r = first[quizKey(txt(card.querySelector('.q-text')))];
        if (!r) { return; }
        var opts = card.querySelectorAll('.quiz-opt');
        for (var i = 0; i < opts.length; i += 1) {
          if (same(sentOpt(opts[i]), r.answer)) { if (!opts[i].disabled) { opts[i].click(); } return; }
        }
      });
      /* The matching exercise: each card's LATEST checked place
         (`ks4c:<st>:match-<n>`, the term of the row it sat in) is put back
         the way the page's own drop handler places a card, then the page's
         own "Check Answers" marks them. Rows exist only for a checked
         exercise, so a restored one is a checked one. */
      var ids = byId(rows);
      Array.prototype.forEach.call(document.querySelectorAll('.match-check-btn'), function (chk) {
        var m = /checkMatching\('([^']*)'/.exec(chk.getAttribute('onclick') || '');
        var st = (m && m[1]) || pathSlug;
        var scope = chk.closest('.section') || document;
        var moved = false;
        Array.prototype.forEach.call(scope.querySelectorAll('.match-def'), function (def) {
          var n = parseInt(def.getAttribute('data-index'), 10);
          var r = lastOf(ids['ks4c:' + st + ':match-' + ((isNaN(n) ? 0 : n) + 1)]);
          if (!r || (def.parentNode && def.parentNode.classList && def.parentNode.classList.contains('match-drop'))) { return; }
          var drops = scope.querySelectorAll('.match-drop');
          for (var i = 0; i < drops.length; i += 1) {
            var term = drops[i].parentNode && drops[i].parentNode.querySelector('.match-term');
            if (drops[i].querySelector('.match-def') || !same(txt(term), r.answer)) { continue; }
            drops[i].innerHTML = '';
            drops[i].appendChild(def);
            drops[i].classList.add('has-item');
            drops[i].classList.remove('match-correct', 'match-wrong');
            moved = true;
            return;
          }
        });
        if (moved) { chk.click(); }
      });
    });

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
    /* ⊕ 14 Oct 2026: the question AS SHOWN. A block's template may print
       words of its own around a prop on the same line — Ks4Guess prints
       "If you had to guess, " + `question` — and the ledger must hold the
       line the child read, not the prop alone. This finds the template
       element whose text is built from `expr`, reads that element's text
       from THIS instance's DOM (never a nested block's), and falls back to
       the template's literal words around `value` when the DOM is not
       there. Only for blocks whose id does not hash the text: a classic
       practice set's id is derived from its text and keeps the prop. */
    // Template node kinds that are not an element of their own (ks4-runtime.js).
    var NOT_EL = { '#': 1, 'if': 1, 'for': 1, 'import': 1, 'child': 1, 'helmet': 1, 'sc-helmet': 1 };
    function shownLine(api, expr, value) {
      var at = null, parts = null;
      (function walk(n, el) {
        if (at !== null || !n || typeof n !== 'object') { return; }
        if (Array.isArray(n)) { n.forEach(function (x) { walk(x, el); }); return; }
        if (n.t === '#' && n.v && Array.isArray(n.v.parts)) {
          var hit = n.v.parts.filter(function (x) { return x && typeof x === 'object'; });
          if (hit.length === 1 && hit[0].e === expr) { at = el; parts = n.v.parts; return; }
        }
        if (n.t === 'child') { return; }        // another block's words are not this one's
        for (var k in n) {
          if (k !== 'a' && Object.prototype.hasOwnProperty.call(n, k) && n[k] && typeof n[k] === 'object') {
            walk(n[k], (n.t && !NOT_EL[n.t] && n.i !== undefined) ? n.i : el);
          }
        }
      })(api.template && api.template.roots, null);
      if (at !== null && api.host && api.host.querySelectorAll) {
        var els = api.host.querySelectorAll('[data-dc-tpl="' + at + '"]');
        for (var i = 0; i < els.length; i += 1) {
          var up = els[i].parentNode;
          while (up && !up.__mrbKs4) { up = up.parentNode; }
          if (up === api.host) { var t = txt(els[i]); if (t) { return t; } }
        }
      }
      if (!parts || value == null || value === '') { return value || ''; }
      return parts.map(function (x) { return typeof x === 'string' ? x : String(value); }).join('').replace(/\s+/g, ' ').trim();
    }
    // fix 2 (display-only): a KS4 lesson option's `full` is the stored text; `text` is the label shown.
    function optText(o) { return o && o.full != null ? String(o.full) : (o && o.text != null ? String(o.text) : null); }
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

    /* ⊕ 25 Oct 2026: how many practice-set questions THIS block offers. The
       batch blocks cap their set at five (`slice(0, 5)` in their own render);
       the pilot block offers every question, four at a time behind "Show 4
       more" — so a fixed five lost the pilot's sixth to eighth answers. The
       block's own progress line ("N of M answered") says M. */
    function quizLimit(api) {
      var all = ((api.logic.props || {}).questions || []).filter(Boolean).length;
      try {
        var m = /\bof (\d+) answered/.exec(String((api.logic.renderVals() || {}).progress || ''));
        if (m) { return Math.min(all, parseInt(m[1], 10)); }
      } catch (e) { /* fall back to the block's whole set */ }
      return all;
    }
    var HANDLERS = {
      Ks4Guess: function (api, s, prev) {
        if (!rootLevel(api) || prev.pick != null || s.pick == null) { return; }
        var p = api.logic.props || {}, o = (p.options || [])[s.pick] || {};
        var d = base('start');
        // The line on screen is "If you had to guess, " + `question`: the
        // lead is the template's, not the prop's (shownLine).
        d.kind = 'choice'; d.question_text = shownLine(api, 'question', p.question || '');
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
        else { d.explanation = p.reveal || null; }
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
        var all = (p.questions || []).filter(Boolean).slice(0, quizLimit(api));
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
          d2 = base('r3');                      // no rung: see scoredRow
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
          d2 = base('r' + (at[0] + 1) + '-' + (at[1] + 1));
          d2.marks = r.marks || [1, 3, 3, 6][at[0]];
        } else { return; }
        d2.kind = 'order'; d2.question_text = r.prompt || '';
        d2.answer = chainAnswer(api, r.links || links, r.herrings || herr);
        d2.correct_answer = (r.links || links).join('\n');
        d2.is_correct = ok;
        d2.marks_scored = ok ? d2.marks : 0;
        /* ⊕ 10 Nov 2026: after "Retry my misses" the rung is dealt again, so its next check
           is the rung's own and goes with the rung (its handler sends it). Only a check the
           rung did not take is sent here, unscored. The rung's handler runs a moment later. */
        if (muted) { return; }                   // a restored chain: already in the ledger
        var qid2 = d2.question_id, at2 = Date.now();
        setTimeout(function () {
          if (rungSent[qid2] && rungSent[qid2] >= at2 - 60) { return; }   // this check went with the rung
          post(d2);
        }, 120);
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

    /* ── Saved work follow-up (16 Oct 2026): the child's own ticks on a
       rebuilt page — a Ks4Write's marking points (on its own, or as a
       ladder's rung 4 / a practice set's written item), a "Your turn"
       (Ks4Cfifa) question's "I had this" lines, a Ks4Steps attempt's lines.
       Ids are the ones the answer itself was posted with. */
    function boolList(arr) {
      var out = [];
      (arr || []).forEach(function (v, i) { if (v) { out.push(i + 1); } });
      return out;
    }
    function writeQid(api) {
      if (rootLevel(api)) { return pilotId(pathSlug, 'write-' + nth(api)); }
      var owner = ownerOf(api);
      if (!owner || !owner.logic) { return null; }
      var op = owner.logic.props || {};
      if (owner.comp === 'Ks4Ladder') { return pilotId(op.slug || pathSlug, 'r4'); }
      if (owner.comp === 'Ks4Practice') {
        var R = op.rungs || {}, L = [R.r1 || [], R.r2 || [], R.r3 || [], R.r4 || []];
        var hidden = (owner.logic.state || {}).hidden || {}, keys = [];
        L.forEach(function (items, ri) {
          items.forEach(function (it, ii) { if ((it.kind || 'mcq') === 'write' && !hidden[ri + '-' + ii]) { keys.push([ri, ii]); } });
        });
        var at = keys[kids(owner, 'Ks4Write').indexOf(api)];
        return at ? pilotId(pathSlug, 'r' + (at[0] + 1) + '-' + (at[1] + 1)) : null;
      }
      return null;
    }
    function stepsTicks(p, ticks) {
      var out = [], at = 0;
      (p.steps || []).forEach(function (stp, si) {
        (stp.lines || []).forEach(function (ln, j) { at += 1; if ((ticks || {})[si + '-' + j]) { out.push(at); } });
      });
      return out;
    }
    /* ⊕ 25 Oct 2026 (Mide's item 1): a Ks4Write marked by LEVELS — the child
       picks the level their own answer reaches (standalone, a ladder's rung 4,
       a practice write item). The pick is their self-marking, like the
       ticks on a points-marked write, and is kept the same way: `self_ticks`
       on that answer's own row, holding the ONE level picked, counted from 1
       in the order the page lists the levels (top level first). It never
       touches the mark. Before this, the pick lived only on the page. */
    var levelSent = {};
    function levelTicks(api) {
      var st = api.logic.state || {}, lvs = (api.logic.props || {}).levels || [];
      if (!st.open) { return; }
      var qid = writeQid(api);
      if (!qid) { return; }
      /* ⊕ 9 Nov 2026 (F4): the "Indicative content" ticks beside the levels, in the
         same `self_ticks`, counted on past the levels so the two can never be read
         for each other: [2, 6] on four levels is "the second level, and point 2". */
      var list = typeof st.level === 'number' ? [st.level + 1] : [];
      boolList(st.ticks).forEach(function (n) { list.push(n + lvs.length); });
      if (!list.length && !levelSent[qid]) { return; }
      levelSent[qid] = 1;
      var lb = typeof st.level === 'number' ? String((lvs[st.level] || {}).label || '') : '';
      var lm = /level\s*(\d)/i.exec(lb);
      sendTicks(qid, list, 0, lm ? parseInt(lm[1], 10) : (/no relevant content/i.test(lb) ? 0 : undefined));
    }
    function tickTap(api) {
      var st = api.logic.state || {}, p = api.logic.props || {};
      if (api.comp === 'Ks4Write') {
        if (p.levels && p.levels.length) { levelTicks(api); return; }
        if (!st.open) { return; }
        var qid = writeQid(api);
        if (qid) { sendTicks(qid, boolList(st.ticks)); }
      } else if (api.comp === 'Ks4Cfifa' && rootLevel(api)) {
        var k = nth(api);
        Object.keys(st.q || {}).forEach(function (i) {
          var q = st.q[i];
          if (q && q.open) { sendTicks(pilotId(pathSlug, 'cfifa-' + k + '-' + (+i + 1)), boolList(q.ticks)); }
        });
      } else if (api.comp === 'Ks4Steps' && rootLevel(api) && p.mode === 'attempt' && st.checked) {
        sendTicks(pilotId(pathSlug, 'steps-' + nth(api)), stepsTicks(p, st.ticks));
      }
    }

    /* <ks4-root-acts> — the lesson's OWN activities on a rebuilt KS4 page.
       Pure analysis of a lesson's root instance (its logic, its compiled
       template, its render values). It never changes the lesson: every
       probe runs the lesson's own handlers against a COPY of its state with
       setState, forceUpdate and the timers stood in for, synchronously, and
       puts everything back before returning. Shared, byte for byte, with
       tools/activity_save_coverage.py (which evaluates this text in Node), so
       the coverage report and the page classify a group the same way. */
    var KS4RootActs = (function () {
      function noopFn() { return 0; }
      function look(expr, scope) {
        var c = scope, ps = String(expr).split('.');
        for (var i = 0; i < ps.length; i += 1) { if (c == null) { return undefined; } c = c[ps[i]]; }
        return c;
      }
      function clone(v) { try { return v === undefined ? undefined : JSON.parse(JSON.stringify(v)); } catch (e) { return null; } }
      function isArr(v) { return Object.prototype.toString.call(v) === '[object Array]'; }
      function isObj(v) { return v !== null && typeof v === 'object' && !isArr(v); }
      function prim(v) { return v === null || v === undefined || typeof v === 'number' || typeof v === 'string' || typeof v === 'boolean'; }
      // A root option group: a top-level `sc-for` (never inside a shared
      // block) whose item holds a control with an onClick. A nested group
      // (a for of items, each with a for of options) is one group per item.
      function groupsOf(template) {
        var out = [];
        function firstOn(n) {
          var hit = null;
          (function w(x) {
            if (hit || !x || typeof x !== 'object') { return; }
            if (isArr(x)) { x.forEach(w); return; }
            if (x.t === 'child') { return; }
            if (x.on) { hit = x; return; }
            (x.c || []).forEach(w);
          })(n);
          return hit;
        }
        function innerFor(n) {
          var hit = null;
          (function w(x) {
            if (hit || !x || typeof x !== 'object') { return; }
            if (isArr(x)) { x.forEach(w); return; }
            if (x.t === 'child') { return; }
            if (x.t === 'for') { if (firstOn(x.c)) { hit = x; } return; }
            (x.c || []).forEach(w);
          })(n);
          return hit;
        }
        function labelOf(n, as) {
          var hit = null;
          (function w(x) {
            if (hit || !x || typeof x !== 'object') { return; }
            if (isArr(x)) { x.forEach(w); return; }
            if (x.t === 'child') { return; }
            if (x.t === '#' && x.v && x.v.parts) {
              for (var i = 0; i < x.v.parts.length; i += 1) {
                var p = x.v.parts[i];
                if (p && p.e && p.e.indexOf(as + '.') === 0) { hit = p.e.slice(as.length + 1); return; }
              }
            }
            (x.c || []).forEach(w);
          })(n);
          return hit;
        }
        (function walk(n) {
          if (!n || typeof n !== 'object') { return; }
          if (isArr(n)) { n.forEach(walk); return; }
          if (n.t === 'child') { return; }
          if (n.t === 'for') {
            var b = firstOn(n.c);
            if (b) {
              var inner = innerFor(n.c), g;
              if (inner && inner.e.indexOf(n.as + '.') === 0) {
                var ib = firstOn(inner.c);
                g = { e: n.e, as: n.as, inner: inner.e.slice(n.as.length + 1), ias: inner.as, on: ib.on, tpl: ib.i, label: labelOf(inner.c, inner.as) };
              } else {
                g = { e: n.e, as: n.as, inner: null, ias: n.as, on: b.on, tpl: b.i, label: labelOf(n.c, n.as) };
              }
              g.field = g.on.indexOf(g.ias + '.') === 0 ? g.on.slice(g.ias.length + 1) : null;
              out.push(g);
              return;
            }
          }
          (n.c || []).forEach(walk);
        })(template && template.roots);
        return out;
      }
      // The options of a group at the lesson's current render values, flat,
      // in DOM order: [{oi, k, item}] (oi null for a flat group).
      function itemsOf(g, vals) {
        var top = look(g.e, vals), out = [];
        if (!isArr(top)) { return out; }
        top.forEach(function (it, oi) {
          if (g.inner) {
            var list = look(g.inner, it);
            if (isArr(list)) { list.forEach(function (x, k) { out.push({ oi: oi, k: k, item: x }); }); }
          } else { out.push({ oi: null, k: oi, item: it }); }
        });
        return out;
      }
      function labelText(g, item) {
        var v = g.label ? look(g.label, item) : null;
        if (v == null && item) { v = item.label != null ? item.label : (item.text != null ? item.text : (item.name != null ? item.name : item.aria)); }
        return v == null ? null : String(v).replace(/\s+/g, ' ').trim();
      }
      // Run fn with the lesson's state set to `state` (a copy), setState
      // recording instead of drawing, and no timer able to start. Returns
      // the merged patch the handler asked for (null when it threw).
      function withStubs(L, state, fn) {
        var w = typeof window !== 'undefined' ? window : {};
        var keep = { st: L.state, ss: Object.prototype.hasOwnProperty.call(L, 'setState') ? L.setState : undefined,
                     fu: Object.prototype.hasOwnProperty.call(L, 'forceUpdate') ? L.forceUpdate : undefined,
                     to: w.setTimeout, si: w.setInterval, ra: w.requestAnimationFrame };
        L.state = state;
        w.setTimeout = noopFn; w.setInterval = noopFn; w.requestAnimationFrame = noopFn;
        L.forceUpdate = function () {};
        try { return fn(); } finally {
          L.state = keep.st;
          if (keep.ss === undefined) { delete L.setState; } else { L.setState = keep.ss; }
          if (keep.fu === undefined) { delete L.forceUpdate; } else { L.forceUpdate = keep.fu; }
          w.setTimeout = keep.to; w.setInterval = keep.si; w.requestAnimationFrame = keep.ra;
        }
      }
      function valsAt(L, state) {
        return withStubs(L, clone(state) || {}, function () { L.setState = function () {}; return L.renderVals() || {}; });
      }
      function patchOf(L, state, getFn) {
        var work = clone(state) || {};
        return withStubs(L, work, function () {
          var patch = {}, any = false;
          L.setState = function (u, cb) {
            var nx = typeof u === 'function' ? u(clone(work), L.props) : u;
            if (nx && typeof nx === 'object') {
              for (var k in nx) { if (Object.prototype.hasOwnProperty.call(nx, k)) { patch[k] = clone(nx[k]); work[k] = clone(nx[k]); any = true; } }
            }
            // On a restore, what the lesson does when an animation ends happens too.
            if (L.__mrbFast && typeof cb === 'function') { cb(); }
          };
          try {
            var fn = getFn(L.renderVals() || {});
            if (typeof fn !== 'function') { return null; }
            fn.call(null, { target: { value: '' }, preventDefault: function () {}, stopPropagation: function () {} });
          } catch (e) { return null; }
          return any ? patch : {};
        });
      }
      // The leaf writes a patch makes against `state`: [{path, before, after,
      // append?}]. A top-level list that grows by one is an append (a "seen"
      // list); anything deeper is followed to its leaves (four levels).
      function writes(patch, state) {
        var out = [];
        function leaves(a, b, path, d) {
          if (JSON.stringify(a) === JSON.stringify(b)) { return; }
          if (d === 1 && isArr(a) && isArr(b) && a.length === b.length + 1 && JSON.stringify(a.slice(0, b.length)) === JSON.stringify(b)) {
            out.push({ path: path, before: b, after: a, append: a[a.length - 1] }); return;
          }
          if (d === 1 && isArr(a) && b == null) { out.push({ path: path, before: b, after: a, append: a.length === 1 ? a[0] : undefined }); return; }
          if (d >= 4 || prim(a) || !(isObj(b) || isArr(b) || b == null)) { out.push({ path: path, before: b, after: a }); return; }
          var keys = {};
          Object.keys(a || {}).forEach(function (x) { keys[x] = 1; });
          Object.keys(b || {}).forEach(function (x) { keys[x] = 1; });
          Object.keys(keys).forEach(function (k) { leaves(a ? a[k] : undefined, b ? b[k] : undefined, path.concat([k]), d + 1); });
        }
        Object.keys(patch || {}).forEach(function (k) { leaves(patch[k], state ? state[k] : undefined, [k], 1); });
        return out;
      }
      function pathKey(p) { return p.join('\u0001'); }
      function at(state, p) { var v = state; for (var i = 0; i < p.length; i += 1) { if (v == null) { return undefined; } v = v[p[i]]; } return v; }
      function msgLike(w) {
        var last = String(w.path[w.path.length - 1]);
        if (/^(wrong|miss|missed|err|error)$/i.test(last) && w.after != null && w.after !== false) { return true; }
        return typeof w.after === 'string' && w.after.trim().length > 0 && (/msg|wrong|err|note|why|hint/i.test(last) || w.after.trim().split(/\s+/).length >= 3);
      }
      function alerts(v) {
        var n = 0, seen = [];
        (function w(x, d) {
          if (d > 9 || x == null) { return; }
          if (typeof x === 'string') { var m = x.match(/ks3-alert/g); if (m) { n += m.length; } return; }
          if (typeof x !== 'object' || x.__mrbFig) { return; }
          if (seen.indexOf(x) >= 0) { return; }
          seen.push(x);
          for (var k in x) { if (Object.prototype.hasOwnProperty.call(x, k)) { w(x[k], d + 1); } }
        })(v, 0);
        return n;
      }
      function apply(state, patch) {
        var s = clone(state) || {};
        Object.keys(patch || {}).forEach(function (k) { s[k] = clone(patch[k]); });
        return s;
      }
      function probe(L, g, state, oi) {
        var flat = itemsOf(g, valsAt(L, state)).filter(function (x) { return x.oi === oi; });
        return flat.map(function (x) {
          var p = g.field ? patchOf(L, state, function (v) {
            var f = itemsOf(g, v).filter(function (y) { return y.oi === oi && y.k === x.k; })[0];
            return f ? look(g.field, f.item) : null;
          }) : null;
          return { k: x.k, label: labelText(g, x.item), patch: p, item: x.item, ws: p ? writes(p, state) : [] };
        });
      }
      /* Classify ONE group (one outer item of a nested group) at `state`:
           {kind:'pick', slot:[path], options:[{k,label,patch,value}], right:[k…]|null, graded}
           {kind:'gate', slot:[key], step:<before>, options…, right:[k…]}
           {kind:'multi', slot:[key], check:k, options…}
           {kind:'explore', why:'…'}   {kind:'none'}
         `init` is the lesson's state as it was first drawn: a slot whose
         first value was a number or a string is a selector (a tab, a dial),
         never an answer. */
      function classify(L, g, state, init, oi) {
        var vals = valsAt(L, state);
        var flat = itemsOf(g, vals).filter(function (x) { return x.oi === oi; });
        if (!flat.length) { return { kind: 'none', why: 'no options' }; }
        var opts = probe(L, g, state, oi);
        var live = opts.filter(function (o) { return o.ws.length; });
        if (!live.length) { return { kind: 'none', why: 'no option changes the lesson here' }; }
        if (opts.some(function (o) { return o.item && typeof o.item.correct === 'boolean'; })) {
          var cslot = commonSlot(live);
          if (cslot) { return finish({ kind: 'pick', slot: cslot, options: opts, right: opts.filter(function (o) { return o.item && o.item.correct === true; }).map(function (o) { return o.k; }), graded: true }, state, init); }
        }
        // A multi-select with its own Check: toggles add/remove an index in
        // one array, and one option (the Check) sets a flag true.
        var togg = live.filter(function (o) { return o.ws.length && o.ws.every(function (w) { return isArr(w.after) || typeof w.after === 'boolean'; }) && o.ws.some(function (w) { return isArr(w.after); }); });
        var chk = live.filter(function (o) { return o.ws.every(function (w) { return typeof w.after === 'boolean'; }) && o.ws.some(function (w) { return w.after === true; }); });
        if (togg.length >= 2 && chk.length === 1 && togg.indexOf(chk[0]) < 0) {
          var mk = togg[0].ws.filter(function (w) { return isArr(w.after); })[0].path[0];
          if (togg.every(function (o) { return o.ws.some(function (w) { return w.path[0] === mk; }); })) {
            return { kind: 'multi', slot: [mk], check: chk[0].k, options: opts };
          }
        }
        // A gate: one option moves the lesson on (a number goes up), the
        // others say why not (a message).
        var msgs = live.filter(function (o) { return o.ws.some(msgLike); });
        if (msgs.length && msgs.length < live.length) {
          var go = live.filter(function (o) { return msgs.indexOf(o) < 0; });
          var adv = null;
          go.forEach(function (o) {
            // A stepper's key may start unset (`s[key] || 0` in the lesson): that is step 0.
            o.ws.forEach(function (w) { if (w.path.length === 1 && typeof w.after === 'number' && (typeof w.before === 'number' || w.before == null) && w.after > (w.before || 0)) { adv = adv || w.path[0]; } });
          });
          if (adv) { return { kind: 'gate', slot: [adv], step: state[adv] || 0, options: opts, right: go.map(function (o) { return o.k; }), graded: true }; }
          var gslot = commonSlot(go);
          if (gslot) { return finish({ kind: 'pick', slot: gslot, options: opts, right: go.map(function (o) { return o.k; }), graded: true, msg: true }, state, init); }
        }
        // Explorations: a card or tab that only records it was seen.
        if (live.every(function (o) { return o.ws.every(function (w) { return w.append !== undefined || (isArr(w.after) && !prim(w.before)) || (w.path.length === 1 && isArr(w.after)); }); })) {
          return { kind: 'explore', why: 'opens a card or marks it seen' };
        }
        var slot = commonSlot(live);
        if (!slot) { return { kind: 'explore', why: 'no single place the choice is kept' }; }
        // A list of choices (tap several), not one answer: after one pick, the
        // next pick lands in the NEXT place of the same list.
        if (slot.length > 1 && /^\d+$/.test(String(slot[slot.length - 1])) && live.length > 1 && live[0].patch) {
          var after1 = probe(L, g, apply(state, live[0].patch), oi).filter(function (o) { return o.k === live[1].k; })[0];
          var w1 = after1 && after1.ws.filter(function (w) { return pathKey(w.path.slice(0, -1)) === pathKey(slot.slice(0, -1)); })[0];
          if (w1 && pathKey(w1.path) !== pathKey(slot)) { return { kind: 'explore', why: 'a list of picks (choose several)' }; }
        }
        // A tab that also lists what has been seen: the slot plus list writes only.
        if (live.every(function (o) { return o.ws.every(function (w) { return pathKey(w.path) === pathKey(slot) || isArr(w.after); }); }) &&
            live.some(function (o) { return o.ws.length > 1; })) {
          return { kind: 'explore', why: 'a tab that records which ones were seen' };
        }
        var r = finish({ kind: 'pick', slot: slot, options: opts, right: null, graded: false }, state, init);
        if (r.kind === 'pick') { okFlag(L, g, r, state, oi); }
        return r;
      }
      // The lesson's own verdict flag: a true/false the choice sets, true for
      // the right option(s) only (`bqOk` in the batch lessons' pick()). Asked
      // again with the flag cleared when an earlier right answer holds it.
      function okFlag(L, g, r, state, oi) {
        function flags(os) {
          var f = {};
          os.forEach(function (o) {
            o.ws.forEach(function (w) { if (typeof w.after === 'boolean') { var pk = pathKey(w.path); (f[pk] = f[pk] || {})[o.k] = w.after; } });
          });
          return f;
        }
        function pickRight(f, os) {
          for (var B in f) {
            if (!Object.prototype.hasOwnProperty.call(f, B)) { continue; }
            var yes = os.filter(function (o) { return f[B][o.k] === true; });
            if (yes.length && yes.length < os.length) { return yes.map(function (o) { return o.k; }); }
          }
          return null;
        }
        var live = r.options.filter(function (o) { return o.ws.length; });
        var f = flags(live), got = pickRight(f, live);
        if (!got) {
          var st2 = clone(state) || {}, any = false;
          for (var B in f) {
            if (!Object.prototype.hasOwnProperty.call(f, B)) { continue; }
            var bp = B.split('\u0001'), par = st2;
            for (var q = 0; q < bp.length - 1 && par; q += 1) { par = par[bp[q]]; }
            if (par && par[bp[bp.length - 1]] === true) { par[bp[bp.length - 1]] = false; any = true; }
          }
          if (any) {
            var again = probe(L, g, st2, oi).filter(function (o) { return o.ws.length; });
            got = pickRight(flags(again), again);
          }
        }
        if (got) { r.right = got; r.graded = true; r.byFlag = true; }
      }
      // The one leaf every live option writes, each a different value.
      function commonSlot(live) {
        if (!live.length) { return null; }
        var cand = live[0].ws.map(function (w) { return w.path; });
        for (var i = 0; i < cand.length; i += 1) {
          var key = pathKey(cand[i]), vals2 = [], ok = true;
          for (var j = 0; j < live.length && ok; j += 1) {
            var hit = live[j].ws.filter(function (w) { return pathKey(w.path) === key; })[0];
            if (!hit || !prim(hit.after) || hit.after === null || typeof hit.after === 'boolean') { ok = false; break; }
            vals2.push(JSON.stringify(hit.after));
          }
          if (ok && (live.length < 2 || vals2.filter(function (v, x) { return vals2.indexOf(v) === x; }).length === vals2.length)) { return cand[i]; }
        }
        return null;
      }
      function finish(r, state, init) {
        r.options.forEach(function (o) { var w = o.ws.filter(function (x) { return pathKey(x.path) === pathKey(r.slot); })[0]; o.value = w ? w.after : undefined; });
        var first = at(init, r.slot);
        if (r.slot.length === 1 && (typeof first === 'number' || typeof first === 'string')) {
          return { kind: 'explore', why: 'a selector: it starts on an option already chosen' };
        }
        return r;
      }
      // Every piece of text a render shows (styles and figures left out).
      function texts(v) {
        var out = {}, seen = [];
        (function w(x, d, k) {
          if (d > 9 || x == null) { return; }
          if (typeof x === 'string') { if (!/style|svg|fig|href|src|class/i.test(k || '')) { out[x.replace(/\s+/g, ' ').trim()] = 1; } return; }
          if (typeof x !== 'object' || x.__mrbFig || seen.indexOf(x) >= 0) { return; }
          seen.push(x);
          for (var key in x) { if (Object.prototype.hasOwnProperty.call(x, key)) { w(x[key], d + 1, key); } }
        })(v, 0, '');
        return out;
      }
      var YES = /^(yes|right|correct|exactly|that'?s (it|right)|well done|spot on)\b/i;
      var TALLY = /(\d+) of (\d+) (right|correct|matched)/i;
      /* Right/wrong for a pick the lesson's code does not flag, from what the
         lesson DRAWS after each option, compared across the options:
           · words — the line that appears opens "Yes." for some options only;
           · a tally — "N of M right" goes up for some options only;
           · style — an alert-styled verdict for some options only.
         None of these differ: the lesson does not judge the choice. Then a
         choice that changes no words at all is part of a form another button
         commits (not an answer on its own); a prediction is kept, unjudged
         (self-checked); anything else is an exploration. */
      function judge(L, g, r, state) {
        if (r.kind !== 'pick' || r.graded) { return r; }
        var base = texts(valsAt(L, state));
        var per = r.options.map(function (o) {
          if (!o.patch) { return null; }
          var v = valsAt(L, apply(state, o.patch)), t = texts(v), added = [];
          for (var k in t) { if (!base[k]) { added.push(k); } }
          var m = null;
          for (var k2 in t) { var mm = TALLY.exec(k2); if (mm) { m = Math.max(m === null ? -1 : m, Number(mm[1])); } }
          // The last right answer of a tally often stops counting and says "All five right".
          if (m === null) { for (var k3 in t) { if (/^all\b.{0,30}\b(right|correct)\b/i.test(k3)) { m = Infinity; } } }
          return { added: added, yes: added.some(function (x) { return YES.test(x); }), tally: m, alerts: alerts(v) };
        });
        var real = per.filter(Boolean);
        if (real.length < 2) { return r; }
        function choose(test) { return r.options.filter(function (o, i) { return per[i] && test(per[i]); }).map(function (o) { return o.k; }); }
        var yes = choose(function (p) { return p.yes; });
        if (yes.length && yes.length < real.length) { r.right = yes; r.graded = true; r.byWords = true; return r; }
        var tl = real.map(function (p) { return p.tally; }).filter(function (n) { return n !== null; });
        if (tl.length === real.length && Math.max.apply(null, tl) !== Math.min.apply(null, tl)) {
          var top = Math.max.apply(null, tl);
          r.right = choose(function (p) { return p.tally === top; }); r.graded = true; r.byTally = true; return r;
        }
        var al = real.map(function (p) { return p.alerts; });
        var lo = Math.min.apply(null, al);
        if (lo !== Math.max.apply(null, al)) { r.right = choose(function (p) { return p.alerts === lo; }); r.graded = true; r.byAlert = true; return r; }
        if (/pred|guess|estim|^est$|bet|vote/i.test(String(r.slot[0]))) { r.prediction = true; return r; }
        if (real.every(function (p) { return !p.added.length; })) { return { kind: 'explore', why: 'part of a form another button commits' }; }
        return { kind: 'explore', why: 'shows a result for any choice; nothing is judged' };
      }
      function analyse(L, g, state, init, oi) { return judge(L, g, classify(L, g, state, init, oi), state); }
      // The ledger id of an answer in a slot: the state key, and for a map
      // or list the entry (a number counted from 1). Lower case, server
      // shape (^[a-z0-9:#._-]{1,200}$).
      function slotId(r, oi) {
        var s = r.kind === 'gate' ? [r.slot[0], typeof r.step === 'number' ? r.step : 0] : r.slot;
        var parts = [s[0]];
        for (var i = 1; i < s.length; i += 1) { parts.push(/^\d+$/.test(String(s[i])) ? String(Number(s[i]) + 1) : String(s[i])); }
        return parts.join('-').toLowerCase().replace(/[^a-z0-9:#._-]+/g, '-');
      }
      return { groupsOf: groupsOf, itemsOf: itemsOf, classify: classify, judge: judge, analyse: analyse, probe: probe, slotId: slotId,
               valsAt: valsAt, patchOf: patchOf, writes: writes, labelText: labelText, apply: apply, clone: clone, at: at, look: look };
    })();
    /* </ks4-root-acts> */

    /* ── Saved work follow-up: a lesson's OWN one-off activities ──
       Some rebuilt lessons ask questions in their own code rather than in a
       shared block (eukaryotes-prokaryotes' cell builder, "Which cell has
       it?", and its three "how many fit" estimates). Their answers live in
       the lesson's root state, and nothing recorded them. The mechanism is
       general; each lesson is named here by what its own render already
       shows, so nothing in Design's lesson code (examiner-frozen) changes:
         pick  — the state map {item index → option index} the buttons fill;
         step  — the state field naming the item on screen;
         opts  — the render value listing the options ({label});
         title — the render value naming the item; lead — the ask;
         right — true when the render shows the CHOSEN option is right.
       The right answer is found by asking the lesson's own render which
       option it would call right. Each choice is one ledger row,
       `ks4:<slug>:<route>#<id>-<n>`, kind choice, right/wrong. */
    var ROOT_SPECS = {
      'eukaryotes-prokaryotes': [
        { id: 'builder', pick: 'bPick', step: 'bk', opts: 'bOpts', title: 'bTitle',
          lead: function () { return 'Which cell has it?'; },
          right: function (v) { return /as you said\.$/.test(String(v.bWord || '')); } },
        { id: 'estimate', pick: 'fPick', step: 'fk', opts: 'fOpts', title: 'fTitle',
          lead: function (v) { return 'Estimate · ' + (v.fName || ''); },
          right: function (v) { return v.fWord === 'Yes.'; } }
      ]
    };
    var rootPrev = {};
    function valsAt(L, patch) {
      var keep = L.state;
      L.state = Object.assign({}, keep, patch);
      try { return L.renderVals() || {}; } finally { L.state = keep; }
    }
    function labelsOf(v, sp) { return (v[sp.opts] || []).map(function (o) { return o && o.label != null ? String(o.label) : ''; }); }
    function rootTap(api) {
      var specs = ROOT_SPECS[pathSlug];
      if (!specs) { return; }
      var L = api.logic, st = L.state || {};
      specs.forEach(function (sp) {
        var cur = st[sp.pick] || {}, was = rootPrev[sp.pick] || {};
        rootPrev[sp.pick] = Object.assign({}, cur);
        Object.keys(cur).forEach(function (k) {
          if (was[k] === cur[k]) { return; }
          var at = {}; at[sp.step] = +k;
          var v = valsAt(L, at), labels = labelsOf(v, sp), good = null;
          for (var i = 0; i < labels.length && good === null; i += 1) {
            var tryPatch = {}; tryPatch[sp.step] = +k; tryPatch[sp.pick] = Object.assign({}, cur); tryPatch[sp.pick][k] = i;
            if (sp.right(valsAt(L, tryPatch))) { good = i; }
          }
          var d = base(sp.id + '-' + (+k + 1));
          d.__block = api.host;
          d.kind = 'choice';
          d.question_text = sp.lead(v) + ' — ' + (v[sp.title] || '');
          d.answer = labels[cur[k]] == null ? null : labels[cur[k]];
          d.correct_answer = good === null ? null : labels[good];
          d.is_correct = good === null ? null : cur[k] === good;
          post(d);
        });
      });
    }

    /* ── ⊕ 8 Nov 2026 (Mide: every answer a family child gives anywhere saves
       and restores): the lesson activities KS4RootActs cannot see. ──
       That classifier reads ROOT OPTION GROUPS only. It never sees a typed or
       selected answer, a form whose options a separate button commits, a list
       of picks, or a builder of steppers. Each of these was read in its
       lesson, and the lesson is named here by what it does, the way ROOT_SPECS
       names one above. `covers` is the handlers and groups a form answers for:
       tools/activity_save_coverage.py reads it, so a new lesson with a typed
       answer shows up there as NOT saved until it is named here or in
       tools/ks4_root_explorations.json.

       A form:
         fire(s, was, x)  the rows the move from state `was` to `s` commits:
                          {e: entry (or null), a: the answer as text, ok: true,
                           false, or null when the lesson does not judge it,
                           q: the question, kind}.
         back(r, e, st, x)  the saved row put back: returns a state patch, or
                          presses the lesson's own handlers through `x`.
       Everything is read at the lesson's commit (its Check, its reveal, its
       run finishing), never per keystroke. A typed answer the lesson judges
       goes as `numeric`, because the server sends `written` to the marker and
       discards the page's verdict. Read only until restore: `x.press` runs the
       lesson's handler on a COPY of its state and applies what it asked for,
       `x.fast` does the same on the lesson's own reduced-motion path so a run
       lands at its end without animating. */
    /* <ks4-root-forms> */
    var lastRootPress = null;                  // the words on the root control last pressed
    var ROOT_FORMS = (function () {
      /* ⊕ 9 Nov 2026: the right answer, as the lesson itself decides it. Each option's own
         handler is run on a copy of the state the child answered from, and the option
         the lesson's verdict calls right is the one named. Read only, never drawn, and
         run only when the child's answer was wrong. */
      function rightBy(x, from, list, test) {
        var A = KS4RootActs, items = list(A.valsAt(x.L, A.clone(from))) || [];
        for (var i = 0; i < items.length; i += 1) {
          try {
            var p = A.patchOf(x.L, A.clone(from), (function (n) { return function (t) { return ((list(t) || [])[n] || {}).onClick; }; })(i));
            if (!p) { continue; }
            var at = A.apply(A.clone(from), p);
            if (test(A.valsAt(x.L, at), at)) { return items[i].label != null ? items[i].label : items[i].text; }
          } catch (e) { /* the next option */ }
        }
        return null;
      }
      // Small whole numbers per slot, the few a balancing question can need; never long on a phone.
      function findCounts(n, max, test, show) {
        var cand = [], t0 = Date.now(), i;
        for (i = 0; i < n; i += 1) { cand.push(1); }
        while (Date.now() - t0 < 250) {
          if (test(cand)) { return show ? show(cand) : cand.join(', '); }
          for (i = n - 1; i >= 0; i -= 1) { if (cand[i] < max) { cand[i] += 1; break; } cand[i] = 1; }
          if (i < 0) { return null; }
        }
        return null;
      }
      function partRight(x, s, k, r, part, names) {
        var hit = null;
        Object.keys(names).forEach(function (key) {
          if (hit !== null) { return; }
          var at = {}, one = {}; one[part] = key; at[k] = Object.assign({}, r, one);
          if (!/alert/.test(String(x.vals({ cur: k, rec: Object.assign({}, s.rec, at) }).verdictStyle || ''))) { hit = names[key]; }
        });
        return hit;
      }
      function put(o, k, v) { var c = Object.assign({}, o || {}); c[k] = v; return c; }
      function find(list, text, key) {
        for (var i = 0; i < (list || []).length; i += 1) { if (list[i] && same(list[i][key || 'label'], text)) { return i; } }
        return -1;
      }
      function rose(s, w, k) { return !!s[k] && !w[k]; }
      function after(text) { var t = String(text == null ? '' : text); var i = t.lastIndexOf(': '); return i < 0 ? t : t.slice(i + 2); }
      // One pick per step, committed when the lesson marks that step done.
      function stepPick(o) {
        return { id: o.id || o.pick, covers: o.covers,
          fire: function (s, w, x) {
            var out = [];
            Object.keys(s[o.done] || {}).forEach(function (k) {
              if (!s[o.done][k] || (w[o.done] || {})[k] || (s[o.pick] || {})[k] === undefined) { return; }
              var at = {}; at[o.step] = +k;
              var v = x.vals(at), it = (v[o.opts] || [])[s[o.pick][k]], good = null;
              (v[o.opts] || []).forEach(function (cand, i) {
                if (good !== null) { return; }
                var tr = Object.assign({}, at), pk = {}; pk[k] = i;
                tr[o.pick] = Object.assign({}, s[o.pick], pk);
                if (o.yes.test(String(x.vals(tr)[o.word] || ''))) { good = cand.label; }
              });
              out.push({ e: +k + 1, a: it ? it.label : null, ok: o.yes.test(String(v[o.word] || '')), q: String(v[o.ask] || ''), good: good });
            });
            return out;
          },
          back: function (r, e, st, x) {
            var k = +e - 1, at = {}; at[o.step] = k;
            var i = find(x.vals(at)[o.opts], r.answer);
            if (i < 0) { return null; }
            var p = {}; p[o.step] = k; p[o.pick] = put(st[o.pick], k, i);
            x.set(p);
            if (o.run) { x.fast(o.run); }
            var d = {}; d[o.done] = put(x.L.state[o.done], k, true);
            return Object.assign(d, o.also || {});
          } };
      }
      /* ⊕ 9 Nov 2026: picks a separate press commits ("Close the switch", Reveal, Check).
         A pick the child can still change is not an answer, so nothing goes until the
         press, and then one row per question with the verdict the page draws. `qs`: the
         render's questions, each with `opts`; or `opts` alone for one question per step.
         `at(k)`, or `step`, puts that step on screen. */
      function commitPicks(o) {
        var atOf = function (k, x) { if (o.at) { return o.at(k, x); } var a = {}; a[o.step] = +k; return a; };
        var withPick = function (s, k, j, i) {
          var m = Object.assign({}, s[o.map] || {}), out = {};
          if (j === null) { m[k] = i; }
          else if (o.slots) { m[k] = Object.assign({}, m[k] || {}); m[k][o.slots[j]] = i; }
          else { m[k] = (m[k] || []).slice(); m[k][j] = i; }
          out[o.map] = m;
          return out;
        };
        var styleOf = function (v, j) {
          if (o.style) { return v[o.style]; }
          var w = (v[o.verdicts] || [])[j === null ? 0 : j];
          return w ? w.style : null;
        };
        var listOf = function (v) { return o.qs ? (v[o.qs] || []) : (v[o.opts] && v[o.opts].length ? [{ opts: v[o.opts] }] : []); };
        var lab = function (x) { return x ? (x.label != null ? x.label : x.text) : null; };
        return { id: o.id, covers: o.covers,
          fire: function (s, w, x) {
            var out = [];
            Object.keys(s[o.done] || {}).forEach(function (k) {
              if (!s[o.done][k] || (w[o.done] || {})[k]) { return; }
              var at = atOf(k, x), v = x.vals(at);
              listOf(v).forEach(function (q, j) {
                var on = (q.opts || []).filter(function (c) { return c.pressed; })[0];
                if (!on) { return; }
                var jj = o.qs ? j : null, st = styleOf(v, jj), good = null;
                (q.opts || []).forEach(function (c, i) {
                  if (good !== null) { return; }
                  var tr = Object.assign({}, at, withPick(s, k, jj, i));
                  if (styleOf(x.vals(tr), jj) && !/ks3-alert/.test(String(styleOf(x.vals(tr), jj)))) { good = lab(c); }
                });
                var key = /^\d+$/.test(k) ? +k + 1 : k;
                out.push({ e: o.qs ? key + '-' + (o.slots ? o.slots[j] : j + 1) : key, a: lab(on), ok: st ? !/ks3-alert/.test(String(st)) : null, good: good, q: String(q.prompt || (o.ask ? v[o.ask] : '') || '') });
              });
            });
            return out;
          },
          back: function (r, e, st, x) {
            var parts = String(e).split('-'), slotKey = o.qs ? parts.pop() : null, kk = parts.join('-');
            var k = /^\d+$/.test(kk) ? String(+kk - 1) : kk;
            var j = o.qs ? (o.slots ? o.slots.indexOf(slotKey) : +slotKey - 1) : null;
            x.set(atOf(k, x));
            var q = listOf(x.vals())[o.qs ? j : 0], i = q ? findLab(q.opts, r.answer) : -1;
            if (i < 0) { return null; }
            x.set(withPick(x.L.state, k, j, i));
            x.fast(o.press);
            return null;
          } };
      }
      function findLab(list, text) {
        for (var i = 0; i < (list || []).length; i += 1) { if (list[i] && same(list[i].label != null ? list[i].label : list[i].text, text)) { return i; } }
        return -1;
      }
      // A typed value and the flag its Check raises.
      function typed(o) {
        return { id: o.id || o.key, covers: o.covers,
          fire: function (s, w, x) {
            if (!rose(s, w, o.flag)) { return null; }
            return [{ e: null, a: s[o.key], ok: o.yes.test(String(x.vals()[o.word] || '')), good: o.good ? function () { return o.good(s, x); } : null, q: o.q, kind: 'numeric' }];
          },
          back: function (r, e, st, x) {
            if (o.before) { o.before(x); }
            var p = {}; p[o.key] = String(r.answer == null ? '' : r.answer); p[o.flag] = true;
            return p;
          } };
      }
      // A reading the child took on a bench: own[key] = seconds, null = over the limit.
      function readings(o) {
        return { id: 'own', covers: [],
          fire: function (s, w) {
            var out = [];
            Object.keys(s.own || {}).forEach(function (k) {
              if ((w.own || {})[k] === s.own[k] && Object.prototype.hasOwnProperty.call(w.own || {}, k)) { return; }
              out.push({ e: k, a: s.own[k] === null ? 'Over 600 s' : s.own[k] + ' s', ok: null, q: o.q(k), kind: 'numeric' });
            });
            return out;
          },
          back: function (r, e, st) {
            var n = /^Over/.test(String(r.answer)) ? null : parseInt(r.answer, 10);
            return o.put(e, n, st);
          } };
      }
      // The option the lesson answers "Yes" to, asked of its own render.
      function optionWhere(x, list, key, word) {
        var out = null;
        (list || []).forEach(function (o) {
          if (out !== null || o.value === '' || o.value == null) { return; }
          var at = {}; at[key] = o.value;
          if (/^Yes/.test(String(x.vals(at)[word] || ''))) { out = o.label; }
        });
        return out;
      }
      var labelOfPressed = function (list) { var on = (list || []).filter(function (o) { return o && o.pressed; }); return on.length ? on[on.length - 1].label : null; };
      return {
        'decomposition': [
          readings({ q: function (k) { return 'Your time for the pink to go at ' + k + ' °C'; },
            put: function (e, n, st) { var p = { own: put(st.own, e, n), run: put(st.run, e, true) }; if (String(st.temp) === String(e)) { p.simT = n === null ? 600 : n; } return p; } }),
          typed({ key: 'rate', flag: 'rateChecked', word: 'rateWord', yes: /^Correct/, q: 'Work out the rate at 40 °C, in s⁻¹', covers: ['onRate'],
            // From the child's own reading, as the lesson works it, and only if the lesson then agrees.
            good: function (s, x) { var n = (s.own || {})[40]; if (typeof n !== 'number') { return null; } var v = (1 / n).toFixed(4); return x.vals({ rate: v, rateChecked: true }).rateWord === 'Correct.' ? v : null; } })
        ],
        'enzymes': [
          readings({ q: function (k) { return 'Your time for the starch to go at pH ' + k; },
            put: function (e, n, st) {
              var end = n ? n / 30 : 0, total = end ? Math.min(20, end + 2) : 20;
              var p = { own: put(st.own, e, n), runs: put(st.runs, e, { end: end, total: total }) };
              if (String(st.ph) === String(e)) { p.shown = total; }
              return p;
            } }),
          { id: 'anom', covers: ['onAnom'],
            fire: function (s, w, x) {
              if (s.anom === w.anom || s.anom === '') { return null; }
              var v = x.vals(), i = (v.anomOpts || []).map(function (o) { return String(o.value); }).indexOf(String(s.anom));
              return [{ e: null, a: i >= 0 ? v.anomOpts[i].label : s.anom, ok: /^Yes/.test(String(v.anomWord || '')), q: 'Which result is the anomaly?', good: optionWhere(x, v.anomOpts, 'anom', 'anomWord') }];
            },
            back: function (r, e, st, x) {
              var o = x.vals().anomOpts || [], i = find(o, r.answer);
              if (i < 0) { return null; }
              x.afterDraw(function () { var el = document.getElementById('enz-anom'); if (el) { el.value = o[i].value; } });
              return { anom: o[i].value };
            } },
          typed({ key: 'mean', flag: 'meanChecked', word: 'meanWord', yes: /^Correct/, q: 'Work out the mean time at pH 6', covers: ['onMean'],
            good: function (s, x) { var n = (s.own || {})[6]; if (typeof n !== 'number') { return null; } var v = String((n + 90) / 2), t = x.vals({ mean: v, meanChecked: true }); return t.meanWord === 'Correct.' ? String(t.meanText || '').split(' s.')[0] + ' s' : null; } })
        ],
        'states-of-matter': (function () {
          var lab = function (x) { if (!x.vals().labDone) { x.fast('onRun'); } };
          return [
            { id: 'anom', covers: ['onAnom'],
              fire: function (s, w, x) {
                if (s.anom === w.anom || s.anom === '') { return null; }
                var v = x.vals(), i = (v.timeOpts || []).map(function (o) { return String(o.value); }).indexOf(String(s.anom));
                return [{ e: null, a: i >= 0 ? v.timeOpts[i].label : s.anom, ok: /^Yes/.test(String(v.anomWord || '')), q: 'Which reading is the anomaly?', good: optionWhere(x, v.timeOpts, 'anom', 'anomWord') }];
              },
              back: function (r, e, st, x) {
                lab(x);
                var o = x.vals().timeOpts || [], i = find(o, r.answer);
                if (i < 0) { return null; }
                x.afterDraw(function () { var el = document.getElementById('anom'); if (el) { el.value = o[i].value; } });
                return { anom: o[i].value };
              } },
            typed({ key: 'mp', flag: 'mpChecked', word: 'mpWord', yes: /^That agrees/, q: 'What is the melting point, in °C?', covers: ['onMp'], before: lab,
              good: function (s, x) { for (var c = 0; c <= 400; c += 1) { var t = x.vals({ mp: String(c), mpChecked: true }); if (/^That agrees/.test(String(t.mpWord || ''))) { var m = /about (\d+)/.exec(String(t.mpText || '')); return m ? m[1] + ' °C' : null; } } return null; } })
          ];
        })(),
        'conservation-of-mass': [
          { words: 'Choose the state symbol for each substance in the equation', id: 'w3', covers: ['w3Rows'],
            fire: function (s, w, x) {
              if (!rose(s, w, 'w3Checked')) { return null; }
              var out = [];
              (x.vals().w3Rows || []).forEach(function (row, i) {
                var on = labelOfPressed(row.options);
                var good = (row.options || []).filter(function (o) { return /--ks3-accent-text/.test(String(o.style || '')); })[0];
                if (on) { out.push({ e: i + 1, a: on, ok: !row.hasWhy, q: String(row.group || ''), good: good ? good.label : (row.hasWhy ? null : on) }); }
              });
              return out;
            },
            back: function (r, e, st, x) {
              var k = +e - 1, row = (x.vals().w3Rows || [])[k], i = row ? find(row.options, r.answer) : -1;
              if (i >= 0) { x.press(function (v) { return v.w3Rows[k].options[i].onClick; }); }
              x.press('onW3Check');
              return null;
            } }
        ],
        'ionic-compounds': [
          { id: 'lenspick', covers: ['lensOpts'],
            fire: function (s, w) {
              if (s.lensPick === w.lensPick || s.lensPick === null) { return null; }
              return [{ e: null, a: String(s.lensPick), ok: s.lensPick === 6, good: '6', q: 'In a real salt crystal, how many chloride ions sit right next to one sodium ion?' }];
            },
            back: function (r) { return { lensPick: parseInt(r.answer, 10) }; } },
          { id: 'dxval', covers: ['onDx'],
            fire: function (s, w, x) {
              if (!rose(s, w, 'dxChecked')) { return null; }
              var v = x.vals(), tab = (v.dxTabs || [])[s.dx];
              // The formula the lesson accepts, in the lesson's own table (its `DX`).
              var acc = null;
              Array.prototype.forEach.call(document.scripts, function (sc) {
                if (acc !== null || String(sc.textContent).indexOf('const DX = [') < 0) { return; }
                var found = String(sc.textContent).slice(sc.textContent.indexOf('const DX = [')).split('];')[0].match(/accept: \['([^']*)'/g) || [];
                var one = found[s.dx];
                acc = one ? one.replace(/^accept: \['|'$/g, '') : '';
              });
              return [{ e: s.dx + 1, a: s.dxVal[s.dx], ok: /^That matches/.test(String(v.dxWord || '')), kind: 'numeric', good: acc || null,
                        q: 'Write the formula' + (tab ? ' — ' + String(tab.label).replace(/ · done$/, '') : '') }];
            },
            back: function (r, e, st, x) {
              var k = +e - 1, a = (st.dxVal || []).slice(); a[k] = String(r.answer == null ? '' : r.answer);
              x.set({ dx: k, dxVal: a });
              x.press('onDxCheck');
              return null;
            } }
        ],
        'ionic-bonding': [
          { id: 'wa', covers: ['wOptions'],
            fire: function (s, w, x) {
              var out = [];
              (s.wa || []).forEach(function (list, wi) {
                var old = (w.wa || [])[wi] || [];
                for (var j = old.length; j < list.length; j += 1) {
                  var was = Object.assign({}, w, { w: wi }); var wj = (w.wa || []).map(function (a) { return a.slice(); }); wj[wi] = list.slice(0, j); was.wa = wj;
                  var v = KS4RootActs.valsAt(x.L, was), o = (v.wOptions || [])[list[j]];
                  // The lesson's own line for this step: its log says "Yes." or "Not this."
                  var log = (x.vals({ w: wi }).wLog || [])[j];
                  out.push({ e: (wi + 1) + '-' + (j + 1), a: o ? o.label : null, ok: !!log && log.word === 'Yes.', good: (function (from, step) { return function () { return rightBy(x, from, function (t) { return t.wOptions; }, function (t) { return ((t.wLog || [])[step] || {}).word === 'Yes.'; }); }; })(was, j), q: String(v.wPrompt || '') });
                }
              });
              return out;
            },
            back: function (r, e, st, x) {
              var wi = parseInt(e, 10) - 1;
              x.set({ w: wi });
              var i = find(x.vals().wOptions, r.answer);
              if (i >= 0) { x.press(function (v) { return v.wOptions[i].onClick; }); }
              return null;
            } },
          { id: 'draw', covers: ['onMq', 'onXq'],
            fire: function (s, w, x) {
              if (!rose(s, w, 'dChecked')) { return null; }
              var v = x.vals();
              return [{ e: s.dp + 1, a: 'Electrons moved: ' + s.moved + '\n' + v.dMetalLabel + ': ' + s.mq + '\n' + v.dNonLabel + ': ' + s.xq,
                        ok: (v.dLines || []).every(function (l) { return /right\.$/.test(String(l.word)); }), good: function () { for (var n = 1; n <= 3; n += 1) { var t = x.vals({ moved: n, mq: String(n), xq: String(-n), dChecked: true }); if ((t.dLines || []).every(function (l) { return /right\.$/.test(String(l.word)); })) { return 'Electrons moved: ' + n + '\n' + t.dMetalLabel + ': ' + n + '\n' + t.dNonLabel + ': ' + (-n); } } return null; }, q: 'Draw the transfer and give each ion its charge' }];
            },
            back: function (r, e, st, x) {
              var l = String(r.answer || '').split('\n');
              x.set({ dp: +e - 1, moved: parseInt(after(l[0]), 10) || 0, mq: after(l[1]), xq: after(l[2]) });
              x.press('onDCheck');
              return null;
            } },
          { id: 'formula', covers: ['onAddM', 'onAddX'],
            fire: function (s, w, x) {
              var v = x.vals();
              if (!/^Formula:/.test(String(v.fDone || '')) || !(s.fm || s.fx) || (w.f === s.f && w.fm === s.fm && w.fx === s.fx)) { return null; }
              return [{ e: s.f + 1, a: String(v.fTally || (s.fm + ', ' + s.fx)).replace(/\s+/g, ' '), ok: true, q: String(v.fTitle || '') }];
            },
            back: function (r, e) {
              var k = +e - 1, n = String(r.answer || '').match(/\d+(?= ×)/g) || [], dn = [];
              for (var i = 0; i < k; i += 1) { dn.push(i); }
              return { f: k, fm: parseInt(n[0], 10) || 0, fx: parseInt(n[1], 10) || 0, fDone: dn };
            } }
        ],
        'carbon-cycle': [
          { id: 'labels', covers: ['r.onChange'], sent: {},
            fire: function (s, w, x) {
              if (!rose(s, w, 'lChecked')) { return null; }
              var sent = this.sent, out = [];
              (x.vals().lRows || []).forEach(function (row) {
                if (!row.value || sent[row.letter] === row.value) { return; }
                sent[row.letter] = row.value;
                out.push({ e: row.letter, a: row.value, ok: !row.hasWhy, good: function () { var el = document.getElementById(row.id), hit = null; Array.prototype.forEach.call(el ? el.options : [], function (o) { if (hit !== null || !o.value) { return; } var at = {}; at[row.letter] = o.value; var t = x.vals({ labels: Object.assign({}, s.labels, at), lChecked: true }); if ((t.lRows || []).some(function (y) { return y.letter === row.letter && !y.hasWhy; })) { hit = o.value; } }); return hit; }, q: String(row.aria || '') });
              });
              return out;
            },
            back: function (r, e, st, x) {
              x.set({ labels: put(st.labels, String(e).toUpperCase(), String(r.answer == null ? '' : r.answer)) });
              x.press('onLCheck');
              return null;
            } }
        ],
        'relative-formula-mass': [
          { id: 'pan', covers: ['panOpts', 'onPanL', 'onPanR'],
            fire: function (s, w, x) {
              var out = [];
              Object.keys(s.pd || {}).forEach(function (k) {
                if (!s.pd[k] || (w.pd || {})[k]) { return; }
                var v = x.vals({ pi: +k }), o = (v.panOpts || [])[s.pp[k]], pv = s.pv[k] || {};
                out.push({ e: +k + 1, a: 'Prediction: ' + (o ? o.label : '') + '\nReactants: ' + pv.l + '\nProducts: ' + pv.r,
                           ok: /^Both totals right/.test(String(v.panVerdict || '')), good: function () { var f = /level: (\S+) and (\S+?)\./.exec(String((v.panFig || {}).alt || '')); return f ? 'Reactants: ' + f[1] + '\nProducts: ' + f[2] : null; }, q: 'Predict, then total each side', kind: 'numeric' });
              });
              return out;
            },
            back: function (r, e, st, x) {
              var k = +e - 1, l = String(r.answer || '').split('\n');
              var i = find(x.vals({ pi: k }).panOpts, after(l[0]));
              if (i < 0) { return null; }
              return { pi: k, pp: put(st.pp, k, i), pv: put(st.pv, k, { l: after(l[1]), r: after(l[2]) }), pd: put(st.pd, k, true) };
            } }
        ],
        'specific-latent-heat': [
          stepPick({ pick: 'picks', done: 'done', step: 'stage', opts: 'stageOpts', word: 'verdictWord', yes: /^Yes/, ask: 'ledgerTitle', also: { prog: 1 }, covers: ['stageOpts'] }),
          { id: 'ans', covers: ['logSteps'],
            fire: function (s, w, x) {
              var out = [], v = x.vals();
              Object.keys(s.ans || {}).forEach(function (k) {
                if ((w.ans || {})[k] === s.ans[k]) { return; }
                var q = (v.logSteps || [])[k], o = q && q.opts[s.ans[k]];
                out.push({ e: +k + 1, a: o ? o.label : null, ok: !!q && q.fbWord === 'Yes.', good: function () { return rightBy(x, w, function (t) { return (t.logSteps || [])[k] ? t.logSteps[k].opts : []; }, function (t) { return ((t.logSteps || [])[k] || {}).fbWord === 'Yes.'; }); }, q: q ? String(q.prompt || '') : '' });
              });
              return out;
            },
            back: function (r, e, st, x) {
              var k = +e - 1;
              x.set({ logDone: true, logP: 1 });
              var q = (x.vals().logSteps || [])[k], j = q ? find(q.opts, r.answer) : -1;
              if (j >= 0) { x.press(function (v) { return v.logSteps[k].opts[j].onClick; }); }
              return null;
            } },
          { id: 'ltext', covers: ['onLText', 'lUnits'],
            fire: function (s, w, x) {
              if (s.lCode === null || (s.lTries === w.lTries && s.lCode === w.lCode)) { return null; }
              var u = (x.vals().lUnits || [])[s.lUnit];
              return [{ e: null, a: s.lText + '\n' + (u ? u.label : ''), ok: s.lCode === 'ok', good: function () { return String(x.vals({ lCode: 'ok' }).lFbText || '').replace(/^Yes\.\s*/, '') || null; }, q: 'Calculate the specific latent heat, with its unit', kind: 'numeric' }];
            },
            back: function (r, e, st, x) {
              var l = String(r.answer || '').split('\n');
              x.set({ logDone: true, logP: 1, lText: l[0] });
              var i = find(x.vals().lUnits, l[1]);
              if (i >= 0) { x.set({ lUnit: i }); }
              x.press('onLCheck');
              return null;
            } }
        ],
        'temperature-changes-shc': [
          { id: 'order', covers: ['raceCards', 'raceSlots'],
            fire: function (s, w, x) {
              if (!rose(s, w, 'raceDone')) { return null; }
              var v = x.vals(), c = v.raceCards || [];
              return [{ e: null, a: (s.order || []).map(function (i) { return c[i] ? c[i].text : ''; }).join('\n'), ok: v.raceVerdictWord === 'Right order.', good: function () { return String(v.raceVerdictWord || '').replace(/^The order is /, '').replace(/\.$/, '') || null; }, q: 'Put the four samples in the order they reach the temperature', kind: 'order' }];
            },
            back: function (r, e, st, x) {
              var c = x.vals().raceCards || [], o = String(r.answer || '').split('\n').map(function (t) { return find(c, t, 'text'); });
              return o.indexOf(-1) >= 0 ? null : { order: o, raceDone: true, raceP: 1 };
            } },
          { id: 'offpick', covers: ['offOpts'],
            fire: function (s, w, x) {
              if (s.offPick === w.offPick || s.offPick === null) { return null; }
              var o = (x.vals().offOpts || [])[s.offPick];
              return [{ e: null, a: o ? o.label : null, ok: s.offPick === 1, good: function () { return ((x.vals().offOpts || [])[1] || {}).label || null; }, q: 'The heater has switched off. Which temperature do you record as the final one?' }];
            },
            back: function (r, e, st, x) {
              if (x.L.state.phase === 'ready') { x.fast('onRun'); }
              var i = find(x.vals().offOpts, r.answer);
              if (i >= 0) { x.fast(function (v) { return v.offOpts[i].onClick; }); }
              return null;
            } },
          { id: 'ctext', covers: ['onCText'],
            fire: function (s, w, x) {
              if (s.cCode === null || (s.cTries === w.cTries && s.cCode === w.cCode)) { return null; }
              return [{ e: null, a: s.cText, ok: s.cCode === 'ok', good: function () { return String(x.vals({ cCode: 'ok' }).cFbText || '') || null; }, q: 'Calculate the specific heat capacity', kind: 'numeric' }];
            },
            back: function (r, e, st, x) {
              x.set({ cText: String(r.answer == null ? '' : r.answer) });
              x.press('onCCheck');
              return null;
            } }
        ],
        'properties-small-molecules': [
          { id: 'gate', covers: ['gateOpts'],
            fire: function (s, w, x) {
              if (s.gate === w.gate || s.gate === null) { return null; }
              var v = x.vals(), o = (v.gateOpts || [])[s.gate];
              return [{ e: null, a: o ? o.label : null, ok: v.gateWord === 'Yes.', good: function () { return rightBy(x, w, function (t) { return t.gateOpts; }, function (t) { return t.gateWord === 'Yes.'; }); }, q: 'What separates when it melts or boils?' }];
            },
            back: function (r, e, st, x) {
              var i = find(x.vals().gateOpts, r.answer);
              if (i >= 0) { x.press(function (v) { return v.gateOpts[i].onClick; }); }
              return null;
            } },
          { id: 'rank', covers: ['rankPool', 'rankSlots'],
            fire: function (s, w, x) {
              if (!rose(s, w, 'rankChecked')) { return null; }
              var v = x.vals();
              return [{ e: null, a: (v.rankSlots || []).map(function (o) { return o.label; }).join('\n'), ok: s.rankOk === true, good: function () { var t = x.vals({ order: [1, 2, 3, 4], rankChecked: true }); return t.rankWord === 'In order.' ? (t.rankSlots || []).map(function (o) { return o.label; }).join('\n') : null; }, q: 'Tap them in order from the lowest boiling point to the highest.', kind: 'order' }];
            },
            back: function (r, e, st, x) {
              x.set({ order: [], rankChecked: false });
              String(r.answer || '').split('\n').forEach(function (t) {
                var i = find(x.vals().rankPool, t);
                if (i >= 0) { x.press(function (v) { return v.rankPool[i].onClick; }); }
              });
              x.press('onRankCheck');
              return null;
            } }
        ],
        'thermal-conductivity': [
          { id: 'tries', covers: ['changes', 'predictions'],
            fire: function (s, w, x) {
              if (!(s.tries > w.tries) || !s.pred || w.pend === null) { return null; }
              return [{ e: s.tries + '-' + (w.pend + 1), a: s.pred.pick, ok: s.pred.pick === s.pred.result, good: function () { return s.pred.result; }, q: 'Change from ' + s.pred.from + ' to ' + s.pred.to + '. The house will cool:' }];
            },
            back: function (r, e, st, x) {
              var n = parseInt(String(e).split('-')[1], 10) - 1;
              x.press(function (v) { return v.changes[n].onClick; });
              var i = find(x.vals().predictions, r.answer);
              if (i >= 0) { x.press(function (v) { return v.predictions[i].onClick; }); }
              return null;
            } }
        ],
        'blood': [
          { id: 'cell', covers: ['choices', 'targets'],
            fire: function (s, w, x) {
              var said = lastRootPress && lastRootPress.text, moved = s.stage !== w.stage && w.sel === s.sel;
              if (!moved && (s.wrong === null || s.wrong === w.wrong)) { return null; }
              return [{ e: (s.sel + 1) + '-' + w.stage, a: said, ok: moved, good: function () { return rightBy(x, w, function (t) { return t.choices; }, function (t, at) { return at.stage !== w.stage; }); }, q: w.stage === 'name' ? 'Name this cell' : 'What is its job?' }];
            },
            back: function (r, e, st, x) {
              x.set({ sel: parseInt(e, 10) - 1 });
              var i = find(x.vals().choices, r.answer, 'text');
              if (i >= 0) { x.press(function (v) { return v.choices[i].onClick; }); }
              return null;
            } }
        ],
        'types-of-em-waves': [
          commitPicks({ words: 'Compare two electromagnetic waves: wavelength, frequency and speed in a vacuum', id: 'preds', map: 'preds', done: 'shown', step: 'pair', press: 'onSend', qs: 'pairQs', verdicts: 'verdicts', covers: ['pairQs'] }),
          { id: 'placed', covers: ['tray', 'slots'],
            fire: function (s, w, x) {
              if (!rose(s, w, 'p1')) { return null; }
              var v = x.vals();
              return [{ e: null, a: (s.placed || []).join('\n'), ok: !(v.p1Notes || []).length, good: function () { var ids = s.placed || [], truth = ids.map(function (nope, k) { for (var n = 0; n < ids.length; n += 1) { var arr = ids.slice(); arr[k] = ids[n]; if (((x.vals({ placed: arr, p1: true }).slots || [])[k] || {}).isOk) { return ids[n]; } } return null; }); return truth.indexOf(null) >= 0 ? null : truth.join('\n'); }, q: 'Tap the seven groups in order, longest wavelength first.', kind: 'order' }];
            },
            back: function (r, e, st, x) {
              var ids = String(r.answer || '').split('\n');
              x.set({ placed: ids });
              x.press('onP1');
              return null;
            } }
        ],
        // ⊕ 8 Nov 2026: the child's own runs, and the concordant titres they chose.
        'titrations': [
          { id: 'gate', covers: ['gateOpts'],
            fire: function (s, w, x) {
              if (s.gate === w.gate || s.gate === null) { return null; }
              var o = (x.vals().gateOpts || [])[s.gate];
              return [{ e: null, a: o ? o.label : null, ok: null, q: 'The rough run goes in 1 cm³ or more at a time. Compared with the careful runs, its titre will be…' }];
            },
            back: function (r, e, st, x) {
              var i = find(x.vals().gateOpts, r.answer);
              if (i >= 0) { x.press(function (v) { return v.gateOpts[i].onClick; }); }
              return null;
            } },
          { id: 'rows', covers: [],
            fire: function (s, w, x) {
              if ((s.rows || []).length <= (w.rows || []).length) { return null; }
              var n = s.rows.length - 1, b = (x.vals().rowBtns || [])[n], row = s.rows[n];
              return [{ e: row.run + 1, a: b ? b.label + ': ' + b.sum : String(row.titre), ok: null, q: 'Record the final reading', kind: 'numeric' }];
            },
            back: function (r, e, st, x) {
              var run = +e - 1, m = /= ([\d.]+) cm/.exec(String(r.answer || ''));
              if (!m) { return null; }
              var t = Math.round(parseFloat(m[1]) * 100);
              x.set({ rows: (st.rows || []).filter(function (y) { return y.run !== run; }), run: run, added: t, shown: t, live: true, pick: null });
              x.press('onRecord');
              return null;
            } },
          { id: 'concord', covers: ['rowBtns'],
            fire: function (s, w, x) {
              if (!s.pick || w.pick) { return null; }
              var on = (x.vals().rowBtns || []).filter(function (b) { return b.pressed; }).map(function (b) { return b.label; });
              // The lesson's own judge, asked which selection it would accept.
              var good = null, rows = s.rows || [], bs = x.vals().rowBtns || [];
              if (typeof x.L.judge === 'function' && rows.length && rows.length <= 12) {
                for (var m = 1; m < (1 << rows.length) && good === null; m += 1) {
                  var sel = {};
                  rows.forEach(function (y, i) { if (m & (1 << i)) { sel[i] = true; } });
                  try { if (x.L.judge(rows, sel).ok) { good = bs.filter(function (b, i) { return sel[i]; }).map(function (b) { return b.label; }).join('\n'); } } catch (e) { good = null; }
                }
              }
              // No selection of these runs passes ("Not concordant yet"): the lesson's answer is what it said.
              if (good === null && !s.pick.ok) { good = [s.pick.word, s.pick.note].filter(Boolean).join(' '); }
              if (good === null && s.pick.ok) { good = on.join('\n'); }
              return [{ e: null, a: on.join('\n'), ok: s.pick.ok === true, q: 'Choose the concordant titres', good: good }];
            },
            back: function (r, e, st, x) {
              x.set({ sel: {}, pick: null });
              String(r.answer || '').split('\n').forEach(function (t) {
                var i = find(x.vals().rowBtns, t);
                if (i >= 0) { x.press(function (v) { return v.rowBtns[i].onClick; }); }
              });
              x.press('onPickCheck');
              return null;
            } }
        ],
        'energy-resources': [
          { id: 'placed', covers: ['zones'],
            fire: function (s, w, x) {
              if (s.tried === null || s.tried === w.tried || s.card !== w.card) { return null; }
              return [{ e: s.card + 1, a: lastRootPress && lastRootPress.text, ok: !!s.flip, good: function () { return rightBy(x, w, function (t) { return t.zones; }, function (t, at) { return at.flip === true; }); }, q: 'Place the card on the grid' }];
            },
            back: function (r, e, st, x) {
              x.set({ card: +e - 1, tried: null, flip: false });
              var i = find(x.vals().zones, r.answer);
              if (i >= 0) { x.press(function (v) { return v.zones[i].onClick; }); }
              return null;
            } }
        ],
        'factors-affecting-food-security': [
          { id: 'picks', covers: ['threatBtns'],
            fire: function (s, w, x) {
              var k = s.hi, was = (w.picks || [])[k];
              if ((s.picks || [])[k] === undefined || (s.picks || [])[k] === null || (s.picks || [])[k] === was) { return null; }
              var said = lastRootPress && lastRootPress.text, v = x.vals();
              return [{ e: k + 1, a: said, ok: /^Yes/.test(String(v.headReply || '')), good: function () { return rightBy(x, w, function (t) { return t.threatBtns; }, function (t) { return /^Yes/.test(String(t.headReply || '')); }); }, q: 'File the headline under the threat it shows' }];
            },
            back: function (r, e, st, x) {
              x.set({ hi: +e - 1 });
              var i = find(x.vals().threatBtns, r.answer);
              if (i >= 0) { x.press(function (v) { return v.threatBtns[i].onClick; }); }
              return null;
            } }
        ],
        'principles-of-organisation': [
          { id: 'picks', covers: ['levelBtns'],
            fire: function (s, w, x) {
              var k = s.ei, a = (s.picks || [])[k];
              if (a === undefined || a === null || a === (w.picks || [])[k]) { return null; }
              return [{ e: k + 1, a: lastRootPress && lastRootPress.text, ok: /^Yes\./.test(String(x.vals().exReply || '')), good: function () { return rightBy(x, w, function (t) { return t.levelBtns; }, function (t) { return /^Yes\./.test(String(t.exReply || '')); }); }, q: 'Which level of organisation is it?' }];
            },
            back: function (r, e, st, x) {
              x.set({ ei: +e - 1 });
              var i = find(x.vals().levelBtns, r.answer);
              if (i >= 0) { x.press(function (v) { return v.levelBtns[i].onClick; }); }
              return null;
            } }
        ],
        'extraction-of-metals': [
          { id: 'pick', covers: ['methods'],
            fire: function (s, w, x) {
              if (s.pick === null || s.pick === w.pick) { return null; }
              var v = x.vals();
              return [{ e: s.metal + 1, a: lastRootPress && lastRootPress.text, ok: !/^Check where/.test(String(v.chooseNote || '')), good: function () { return rightBy(x, w, function (t) { return t.methods; }, function (t) { return !/^Check where/.test(String(t.chooseNote || '')); }); }, q: String(v.chooseQ || '') }];
            },
            back: function (r, e, st, x) {
              x.set({ metal: +e - 1, pick: null });
              var i = find(x.vals().methods, r.answer);
              if (i >= 0) { x.press(function (v) { return v.methods[i].onClick; }); }
              return null;
            } }
        ],
        'viral-diseases': [
          { id: 'clue', covers: ['clueBtns'],
            fire: function (s, w, x) {
              if (s.pick === null || s.pick === w.pick) { return null; }
              var v = x.vals();
              return [{ e: s.ci + 1, a: lastRootPress && lastRootPress.text, ok: /^Yes/.test(String(v.clueNote || '')), good: function () { return rightBy(x, w, function (t) { return t.clueBtns; }, function (t) { return /^Yes/.test(String(t.clueNote || '')); }); }, q: 'Which disease? ' + String(v.clueCount || '') }];
            },
            back: function (r, e, st, x) {
              x.set({ ci: +e - 1, pick: null });
              var i = find(x.vals().clueBtns, r.answer);
              if (i >= 0) { x.press(function (v) { return v.clueBtns[i].onClick; }); }
              return null;
            } }
        ],
        'meiosis': [
          { id: 'gate', covers: ['stepBtns'],
            fire: function (s, w, x) {
              var said = lastRootPress && lastRootPress.text;
              if (!said || /^(Next step|Start again)$/.test(said)) { return null; }
              var wrong = s.gateMsg && s.gateMsg !== w.gateMsg, right = s.step > w.step;
              if (!wrong && !right) { return null; }
              return [{ e: w.step + 1, a: said, ok: !!right, good: function () { return rightBy(x, w, function (t) { return t.stepBtns; }, function (t, at) { return at.step > w.step; }); }, q: 'Predict what happens next' }];
            },
            back: function (r, e, st, x) {
              x.set({ step: +e - 1, gateMsg: '' });
              var i = find(x.vals().stepBtns, r.answer);
              if (i >= 0) { x.press(function (v) { return v.stepBtns[i].onClick; }); }
              return null;
            } }
        ],
        'microscopy': [
          { id: 'gate', covers: ['gateOpts'],
            fire: function (s, w, x) {
              var out = [], v = x.vals(), said = lastRootPress && lastRootPress.text;
              (s.gate || []).forEach(function (g, i) {
                if (g === null || g === (w.gate || [])[i]) { return; }
                out.push({ e: i + 1, a: said, ok: v.gateWord === 'Yes.', good: function () { return rightBy(x, w, function (t) { return t.gateOpts; }, function (t) { return t.gateWord === 'Yes.'; }); }, q: String(x.vals({ pending: i }).gatePrompt || '') });
              });
              return out;
            },
            back: function (r, e, st, x) {
              var k = +e - 1;
              x.set({ pending: k });
              var i = find(x.vals().gateOpts, r.answer);
              if (i >= 0) { x.press(function (v) { return v.gateOpts[i].onClick; }); } else { x.set({ pending: null }); }
              return null;
            } }
        ],
        'sound-waves-hearing': [
          commitPicks({ words: 'What do the air particles and the ear drum do when a sound passes?', id: 'ppred', map: 'pPred', done: 'pShown', step: 'pStage', press: 'onPReveal', opts: 'pOpts', verdicts: 'pVerdicts', ask: 'pPrompt', covers: ['pOpts'] }),
          { id: 'tpred', covers: ['pTones'],
            fire: function (s, w, x) {
              var out = [];
              Object.keys(s.pShown || {}).forEach(function (k) {
                if (!s.pShown[k] || (w.pShown || {})[k]) { return; }
                var v = x.vals({ pStage: +k });
                (v.pTones || []).forEach(function (t, i) {
                  var on = (t.opts || []).filter(function (o) { return o.pressed; })[0];
                  if (on) { out.push({ e: k + '-' + (i + 1), a: on.label, ok: null, q: 'Can you hear a tone of ' + t.label + '?' }); }
                });
              });
              return out;
            },
            back: function (r, e, st, x) {
              var n = String(e).split('-'), i = +n[1] - 1;
              x.set({ pStage: +n[0] });
              var t = (x.vals().pTones || [])[i], j = t ? find(t.opts, r.answer) : -1;
              if (j >= 0) { x.press(function (v) { return v.pTones[i].opts[j].onClick; }); }
              x.press('onPReveal');
              return null;
            } }
        ],
        'polymers': [
          { id: 'appick', covers: ['apOpts'],
            fire: function (s, w, x) {
              if (s.apPick === w.apPick || s.apPick === null) { return null; }
              var v = x.vals(), o = (v.apOpts || [])[s.apPick];
              return [{ e: null, a: o ? o.label : null, ok: /as you said/.test(String(v.apWord || '')), good: function () { return rightBy(x, w, function (t) { return t.apOpts; }, function (t) { return /as you said/.test(String(t.apWord || '')); }); }, q: 'Eight ethene molecules (48 atoms) join into one chain. How many atoms are lost?' }];
            },
            back: function (r, e, st, x) {
              var i = find(x.vals().apOpts, r.answer);
              if (i >= 0) { x.press(function (v) { return v.apOpts[i].onClick; }); }
              return null;
            } }
        ],
        'chemical-bonds': [
          { id: 'pair', covers: ['cells', 'predictButtons'],
            fire: function (s, w, x) {
              if (s.pred === null || s.pred === w.pred) { return null; }
              var v = x.vals(), on = (v.cells || []).filter(function (c) { return c.pressed; }).map(function (c) { return c.sym; });
              return [{ e: on.join('-'), a: lastRootPress && lastRootPress.text, ok: !/alert/.test(String(v.verdictStyle || '')), good: function () { return rightBy(x, w, function (t) { return t.predictButtons; }, function (t) { return !/alert/.test(String(t.verdictStyle || '')); }); }, q: 'What kind of bond forms between ' + on.join(' and ') + '?' }];
            },
            back: function (r, e, st, x) {
              x.press('onNewPair');
              String(e).split('-').forEach(function (sym) {
                var cs = x.vals().cells || [], i = -1;
                cs.forEach(function (c, n) { if (String(c.sym).toLowerCase() === sym) { i = n; } });
                if (i >= 0) { x.press(function (v) { return v.cells[i].onClick; }); }
              });
              var p = find(x.vals().predictButtons, r.answer);
              if (p >= 0) { x.fast(function (v) { return v.predictButtons[p].onClick; }); }
              return null;
            } }
        ],
        /* ⊕ 9 Nov 2026: readings taken on the bench. Each is a row of its own, numbered
           across the whole session, with the meters' figures; Clear is a row too, so
           the list comes back the same on any device. Nothing judges a reading. */
        /* ⊕ 10 Nov 2026: "You predicted gentler. It is the other way." is the lesson's verdict
           on the prediction: sent with it, and the option it calls right. Lithium's single
           "Drop it in" is not a prediction and sends nothing. */
        'group-1': [
          { words: 'Predict how vigorously each alkali metal reacts with water', id: 'preds', covers: ['predBtns'],
            fire: function (s, w, x) {
              var out = [];
              (s.shown || []).forEach(function (on, i) {
                if (!on || (w.shown || [])[i] || i === 0) { return; }
                var v = x.vals({ at: i }), from = Object.assign(KS4RootActs.clone(w), { at: i });
                var said = s.preds[i] === 'more' ? 'More vigorously' : (s.preds[i] === 'less' ? 'More gently' : null);
                (KS4RootActs.valsAt(x.L, from).predBtns || []).forEach(function (b) {
                  var p = KS4RootActs.patchOf(x.L, KS4RootActs.clone(from), function (t) { return (t.predBtns || []).filter(function (c) { return c.label === b.label; })[0].onClick; });
                  if (p && p.preds && p.preds[i] === s.preds[i]) { said = b.label; }
                });
                out.push({ e: i + 1, a: said, ok: !/other way/i.test(String(v.waterNote || '')), good: function () { return rightBy(x, from, function (t) { return t.predBtns; }, function (t) { return !/other way/i.test(String(t.waterNote || '')); }); },
                           q: 'Before it goes in, predict: ' + String(((v.metals || [])[i] || {}).label || '') + ' reacts…' });
              });
              return out;
            },
            back: function (r, e, st, x) {
              var i = +e - 1;
              if (!(i > 0)) { return null; }
              var sh = (x.L.state.shown || []).slice();
              for (var k = 0; k < i; k += 1) { sh[k] = true; }
              x.set({ shown: sh, at: i });
              var j = find(x.vals().predBtns, r.answer);
              if (j >= 0) { x.fast(function (v) { return v.predBtns[j].onClick; }); }
              return null;
            } }
        ],
        'resistors': [(function () {
          var lists = {}, taken = {};
          var word = function (x, k) { var c = (x.vals({ comp: k }).simTitle || ''); return c.split(' \u00b7 ')[0] || k; };
          return { words: 'Readings of potential difference and current for a component', id: 'data', covers: [],
            fire: function (s, w, x) {
              var out = [];
              Object.keys(s.data || {}).forEach(function (k) {
                var now = s.data[k] || [], was = (w.data || {})[k] || [];
                if (now.length < was.length) {
                  out.push({ e: k + '-cleared', a: 'Cleared ' + was.length + (was.length === 1 ? ' reading' : ' readings'), ok: null, q: word(x, k) + ': readings cleared', kind: 'numeric' });
                }
                // ⊕ 10 Nov 2026: the figures the meters showed the child, as the page printed them.
                var mv = x.vals({ comp: k });
                now.slice(was.length).forEach(function (p) {
                  taken[k] = (taken[k] || 0) + 1;
                  var shown = (mv.vText && mv.iText) ? mv.vText + ', ' + mv.iText : p.v + ' V, ' + Number(p.i).toPrecision(4) + ' A';
                  out.push({ e: k + '-' + taken[k], a: shown, ok: null, q: word(x, k) + ': reading ' + taken[k], kind: 'numeric' });
                });
              });
              return out;
            },
            back: function (r, e) {
              var m = /^([a-z]+)-(\d+|cleared)$/.exec(e || '');
              if (!m) { return null; }
              if (m[2] === 'cleared') { lists[m[1]] = []; } else {
                var a = /^([-\u2212]?[\d.]+(?:e[-+]?\d+)?) V, ([-\u2212]?[\d.]+(?:e[-+]?\d+)?) (m?A)$/i.exec(String(r.answer || ''));
                if (!a) { return null; }
                var num = function (t) { return Number(String(t).replace('\u2212', '-')); };
                lists[m[1]] = (lists[m[1]] || []).concat([{ v: num(a[1]), i: num(a[2]) / (a[3] === 'mA' ? 1000 : 1) }]);
                taken[m[1]] = Math.max(taken[m[1]] || 0, Number(m[2]));
              }
              var patch = { data: Object.assign({ resistor: [], lamp: [], diode: [] }, lists), comp: m[1] };
              return patch;
            } };
        })()],
        'series-parallel-circuits': [commitPicks({ words: 'What happens to the ammeter and voltmeter readings when the circuit changes?', id: 'preds', map: 'preds', done: 'revealed', step: 'step', press: 'onReveal', qs: 'qs', verdicts: 'verdicts', covers: ['qs'] })],
        'chromosomes-mitosis': [commitPicks({ words: 'Predict each stage of the cell cycle and mitosis before running the model', id: 'preds', map: 'preds', done: 'revealed', step: 'st', press: 'onCyRun', qs: 'cyQs', verdicts: 'cyVerdicts', covers: ['cyQs'] })],
        'lenses': [commitPicks({ words: 'Predict the image a lens forms for this object distance', id: 'preds', map: 'preds', done: 'shown', press: 'onDraw', qs: 'bQs', verdicts: 'bVerdicts', slots: ['t', 's', 'w'], covers: ['bQs'],
          at: function (k, x) {
            var lens = String(k).slice(0, 2), s0 = {}; s0[k] = true;
            for (var pos = 0; pos < 12; pos += 1) {
              // Only this key shown, so an earlier position's verdicts are never read for this one.
              var v = x.vals({ lens: lens, pos: pos, shown: s0 });
              if ((v.bVerdicts || []).length) { return { lens: lens, pos: pos }; }
            }
            return { lens: lens };
          } })],
        'waves-detection-exploration': [
          commitPicks({ words: 'What do seismometer records of P-waves and S-waves show about the structure of the Earth?', id: 'qpred', map: 'qPred', done: 'qShown', step: 'qStage', press: 'onQReveal', opts: 'qOpts', style: 'qVerdictStyle', ask: 'qPrompt', covers: ['qOpts'] }),
          commitPicks({ words: 'Ultrasound echoes from boundaries: how many come back to the probe?', id: 'upred', map: 'uPred', done: 'uShown', step: 'uStage', press: 'onUReveal', opts: 'uOpts', style: 'uVerdictStyle', ask: 'uPrompt', covers: ['uOpts'] })
        ],
        'changes-in-energy': [stepPick({ pick: 'picks', done: 'revealed', step: 'round', opts: 'roundOpts', word: 'verdictWord', yes: /as you said/, ask: 'roundAsk', also: { anim: 1 }, covers: ['roundOpts'] })],
        'power': [stepPick({ pick: 'picks', done: 'revealed', step: 'round', opts: 'roundOpts', word: 'verdictWord', yes: /^Yes/, ask: 'roundAsk', covers: ['roundOpts'] })],
        'internal-energy': [stepPick({ pick: 'picks', done: 'done', step: 'stage', opts: 'stageOpts', word: 'verdictWord', yes: /^Yes/, ask: 'stageTitle', also: { prog: 1 }, covers: ['stageOpts'] })],
        'particle-motion-pressure': (function () {
          // covers: ['p3Opts', 'p4Opts']
          var one = function (n) {
            var pk = n + 'Pick', dn = n + 'Done', op = n + 'Opts', run = 'on' + n.toUpperCase() + 'Run';
            return { id: n, covers: [op],
              fire: function (s, w, x) {
                if (!rose(s, w, dn)) { return null; }
                var v = x.vals(), o = (v[op] || [])[s[pk]];
                return [{ e: null, a: o ? o.label : null, ok: /^Yes/.test(String(v[n + 'VerdictWord'] || '')), good: function () { var list = v[op] || [], hit = null; list.forEach(function (o2, i) { var at = {}; at[pk] = i; at[dn] = true; if (hit === null && /^Yes/.test(String(x.vals(at)[n + 'VerdictWord'] || ''))) { hit = o2.label; } }); return hit; }, q: 'Commit, then run the piston' }];
              },
              back: function (r, e, st, x) {
                var i = find(x.vals()[op], r.answer);
                if (i < 0) { return null; }
                var p = {}; p[pk] = i; x.set(p);
                x.fast(run);
                var d = {}; d[dn] = true;
                return d;
              } };
          };
          return [stepPick({ id: 'bpick', pick: 'bPick', done: 'bDone', step: 'b', opts: 'bOpts', word: 'bVerdictWord', yes: /^Yes/, ask: 'bAsk', run: 'onBRun', covers: ['bOpts'] }), one('p3'), one('p4')];
        })(),
        'greenhouse-gases': [
          { id: 'rep', covers: ['repQs'], sent: {},
            fire: function (s, w, x) {
              if (!rose(s, w, 'repChecked')) { return null; }
              var sent = this.sent, out = [];
              (x.vals().repQs || []).forEach(function (q, i) {
                var a = labelOfPressed(q.options);
                if (a == null || sent[i] === a) { return; }
                sent[i] = a;
                out.push({ e: i + 1, a: a, ok: !q.hasWhy, good: function () { return rightBy(x, w, function (t) { return ((t.repQs || [])[i] || {}).options || []; }, function (t, at) { return !((x.vals(Object.assign({}, at, { repChecked: true })).repQs || [])[i] || {}).hasWhy; }); }, q: q.label });
              });
              return out;
            },
            back: function (r, e, st, x) {
              var k = +e - 1, q = (x.vals().repQs || [])[k], i = q ? find(q.options, r.answer) : -1;
              if (i < 0) { return null; }
              x.press(function (v) { return v.repQs[k].options[i].onClick; });
              x.press('onRepCheck');
              return null;
            } }
        ],
        'metal-hydroxides': (function () {
          var P1 = { blue: 'Blue precipitate', green: 'Green precipitate', brown: 'Brown precipitate', white: 'White precipitate', none: 'No precipitate' };
          var P2 = { dissolves: 'It dissolves', stays: 'It stays' };
          var pressAsk = function (x, label) {
            var i = find(x.vals().askOptions, label);
            if (i >= 0) { x.fast(function (v) { return v.askOptions[i].onClick; }); }
            return i >= 0;
          };
          var rec = function (x, k, o) { var r = {}; r[k] = Object.assign({}, x.L.state.rec[k] || {}, o); x.set({ rec: Object.assign({}, x.L.state.rec, r) }); };
          return [
            { id: 'rec', covers: ['askOptions'],
              fire: function (s, w, x) {
                var out = [];
                Object.keys(s.rec || {}).forEach(function (k) {
                  var r = s.rec[k] || {}, was = (w.rec || {})[k] || {}, v = x.vals({ cur: k });
                  var good = !/alert/.test(String(v.verdictStyle || ''));
                  if (r.s1 === 'done' && was.s1 !== 'done' && r.p1) { out.push({ e: k + '-p1', a: P1[r.p1], ok: good, good: function () { return partRight(x, s, k, r, 'p1', P1); }, q: String(v.askPrompt || 'A few drops of sodium hydroxide go in. What forms?') }); }
                  if (r.s2 === 'done' && was.s2 !== 'done' && r.p2) { out.push({ e: k + '-p2', a: P2[r.p2], ok: good, good: function () { return partRight(x, s, k, r, 'p2', P2); }, q: 'Now add sodium hydroxide until it is in excess. What happens to the precipitate?' }); }
                  if (r.last && r.last !== was.last) {
                    out.push({ e: k + '-id', a: labelOfPressed(v.askOptions), ok: r.idOk === true, good: function () { return rightBy(x, Object.assign({}, w, { cur: k }), function (t) { return t.askOptions; }, function (t, at) { return ((at.rec || {})[k] || {}).idOk === true; }); }, q: String(v.askPrompt || ('Which metal ion is in tube ' + k + '?')) });
                  }
                });
                return out;
              },
              back: function (r, e, st, x) {
                var ix = String(e).lastIndexOf('-'), low = String(e).slice(0, ix), kind = String(e).slice(ix + 1);
                // The id lower-cased the tube's letter; the state's own key is found again.
                var k = low;
                ['W', 'X', 'Y', 'Z'].forEach(function (t) { if (t.toLowerCase() === low) { k = t; } });
                x.set({ cur: k });
                if (kind === 'id') {
                  rec(x, k, { s1: 'done' });
                  if (pressAsk(x, r.answer) && r.is_correct === true && !(x.L.state.rec[k] || {}).idOk) {
                    rec(x, k, { s2: 'done' });
                    pressAsk(x, r.answer);
                  }
                } else { pressAsk(x, r.answer); }
                return null;
              } },
            { id: 'forge', covers: ['forgeItems'],
              fire: function (s, w, x) {
                var out = [], v = x.vals();
                (v.forgeItems || []).forEach(function (f, n) {
                  var key = String(((f.parts || [])[0] || {}).id || '').replace(/^mh-|-\d+$/g, '');
                  var st = (s.forge || {})[key], was = (w.forge || {})[key];
                  if (!st || !st.checked || (was && was.checked)) { return; }
                  out.push({ e: n + 1, a: f.parts.map(function (p) { return p.label + ': ' + labelOfPressed(p.options); }).join('\n'), ok: st.ok === true, good: function () { var at = {}; at[key] = { picks: st.picks || {}, checked: true, ok: true }; return ((x.vals({ forge: Object.assign({}, s.forge, at) }).forgeItems || [])[n] || {}).note || null; }, q: String(f.head || '') });
                });
                return out;
              },
              back: function (r, e, st, x) {
                var n = +e - 1, lines = String(r.answer || '').split('\n');
                lines.forEach(function (ln, pi) {
                  var f = (x.vals().forgeItems || [])[n], p = f && f.parts[pi], i = p ? find(p.options, after(ln)) : -1;
                  if (i >= 0) { x.press(function (v) { return v.forgeItems[n].parts[pi].options[i].onClick; }); }
                });
                x.press(function (v) { return (v.forgeItems[n] || {}).onCheck; });
                return null;
              } },
            { id: 'ion', covers: ['ionParts'],
              fire: function (s, w, x) {
                if (!(s.ion || {}).checked || (w.ion || {}).checked) { return null; }
                var v = x.vals();
                return [{ e: null, a: (v.ionParts || []).map(function (p) { return p.label + ': ' + labelOfPressed(p.options); }).join('\n'), ok: s.ion.ok === true, good: function () { return x.vals({ ion: { picks: s.ion.picks || {}, checked: true, ok: true } }).ionNote || null; }, q: 'Build the ionic equation' }];
              },
              back: function (r, e, st, x) {
                String(r.answer || '').split('\n').forEach(function (ln, pi) {
                  var p = (x.vals().ionParts || [])[pi], i = p ? find(p.options, after(ln)) : -1;
                  if (i >= 0) { x.press(function (v) { return v.ionParts[pi].options[i].onClick; }); }
                });
                x.press('onIonCheck');
                return null;
              } }
          ];
        })(),
        'atmospheric-pollutants': [
          { id: 'products', covers: ['products'],
            fire: function (s, w, x) {
              if (!rose(s, w, 'checked')) { return null; }
              var v = x.vals(), a = (v.products || []).filter(function (p) { return p.pressed; }).map(function (p) { return p.label; });
              return [{ e: s.ci + 1, a: a.join('\n'), ok: v.verdictWord === 'Exactly right.', good: function () { return (x.vals({ picks: {}, checked: true }).products || []).filter(function (p) { return p.mark === 'missed'; }).map(function (p) { return p.label; }).join('\n') || null; }, q: 'Which products form? ' + String(v.caseText || '') }];
            },
            back: function (r, e, st, x) {
              x.set({ ci: +e - 1, picks: {}, checked: false });
              String(r.answer || '').split('\n').forEach(function (t) {
                var i = find(x.vals().products, t);
                if (i >= 0) { x.press(function (v) { return v.products[i].onClick; }); }
              });
              x.press('onCheck');
              return null;
            } }
        ],
        'atoms-elements-compounds': [
          { id: 'bv', covers: ['balTerms'],
            fire: function (s, w, x) {
              var out = [];
              Object.keys(s.bv || {}).forEach(function (k) {
                if ((w.bv || {})[k] === s.bv[k] && JSON.stringify((w.bc || {})[k]) === JSON.stringify((s.bc || {})[k])) { return; }
                var c = (s.bc || {})[k], v = x.vals({ bi: +k });
                if (!c) { c = (v.balTerms || []).filter(function (t) { return t.isSpecies; }).map(function () { return 1; }); }
                out.push({ e: +k + 1, a: c.join(', '), ok: s.bv[k] === 'ok' ? true : (s.bv[k] === 'no' ? false : null), good: function () { return s.bv[k] === 'no' ? findCounts(c.length, 5, function (cand) { var at = {}; at[k] = cand; var p = KS4RootActs.patchOf(x.L, Object.assign(KS4RootActs.clone(s), { bi: +k, bc: Object.assign({}, s.bc, at), bv: {} }), function (t) { return t.onBalCheck; }); return !!p && !!p.bv && p.bv[k] === 'ok'; }) : null; }, q: 'Balance the equation: ' + (v.balTerms || []).map(function (t) { return t.isSign ? t.sign : t.formula; }).join(' ') });
              });
              return out;
            },
            back: function (r, e, st, x) {
              var k = +e - 1, c = String(r.answer || '').split(', ').map(function (n) { return parseInt(n, 10); });
              x.set({ bi: k, bc: put(st.bc, k, c) });
              x.press('onBalCheck');
              return null;
            } }
        ],
        'carbonates-halides-sulfates': [
          { id: 'spec', covers: ['specItems'],
            fire: function (s, w, x) {
              var out = [], v = x.vals();
              (v.specItems || []).forEach(function (it, i) {
                var st = (s.spec || {})[i], was = (w.spec || {})[i];
                if (!st || !st.checked || (was && was.checked)) { return; }
                out.push({ e: i + 1, a: (it.chips || []).filter(function (c) { return c.pressed; }).map(function (c) { return c.label; }).join('\n'), ok: st.ok === true, good: function () { var chips = it.chips || [], n2 = chips.length; for (var bits = 0; bits < (1 << n2); bits += 1) { var marks = {}; chips.forEach(function (c, z) { if (bits & (1 << z)) { marks[z] = true; } }); var at = {}; at[i] = { marks: marks, checked: false, ok: false }; var p = KS4RootActs.patchOf(x.L, Object.assign(KS4RootActs.clone(s), { spec: Object.assign({}, s.spec, at) }), function (t) { return (t.specItems || [])[i].onCheck; }); if (p && p.spec && p.spec[i] && p.spec[i].ok) { return chips.filter(function (c, z) { return bits & (1 << z); }).map(function (c) { return c.label; }).join('\n'); } } return null; }, q: 'Mark the spectator ions: ' + String(it.full || '') });
              });
              return out;
            },
            back: function (r, e, st, x) {
              var n = +e - 1, want = String(r.answer || '').split('\n');
              var item = function () { return (x.vals().specItems || [])[n]; };
              if (!item()) { return null; }
              item().chips.forEach(function (c, k) {
                if (!!c.pressed !== want.some(function (t) { return same(t, c.label); })) { x.press(function (v) { return v.specItems[n].chips[k].onClick; }); }
              });
              x.press(function (v) { return v.specItems[n].onCheck; });
              return null;
            } }
        ],
        'covalent-bonding': [
          { id: 'orders', covers: ['bBonds'],
            fire: function (s, w, x) {
              if (!rose(s, w, 'bChecked')) { return null; }
              var v = x.vals();
              return [{ e: s.m + 1, a: (v.bBonds || []).map(function (b) { return b.label + ': ' + b.value; }).join('\n'), ok: v.bWord === 'Every shell is full.', good: function () { var mk = null, n3 = (v.bBonds || []).length, zero = String(((v.bBonds || [])[0] || {}).value); Object.keys(s.orders || {}).forEach(function (key) { var at = {}; at[key] = (v.bBonds || []).map(function () { return 3; }); if (mk === null && String(((x.vals({ orders: at }).bBonds || [])[0] || {}).value) !== String(((x.vals({ orders: {} }).bBonds || [])[0] || {}).value)) { mk = key; } }); if (mk === null || !n3 || !zero) { return null; } return findCounts(n3, 3, function (cand) { var at = {}; at[mk] = cand; return x.vals({ orders: at, bChecked: true }).bWord === 'Every shell is full.'; }, function (cand) { var at = {}; at[mk] = cand; return (x.vals({ orders: at, bChecked: true }).bBonds || []).map(function (b) { return b.label + ': ' + b.value; }).join('\n'); }); }, q: 'Choose how many pairs each bond shares.' }];
            },
            back: function (r, e, st, x) {
              x.set({ m: +e - 1 });
              String(r.answer || '').split('\n').forEach(function (ln, i) {
                var want = parseInt(after(ln), 10);
                var cur = function () { return parseInt(((x.vals().bBonds || [])[i] || {}).value, 10); };
                for (var g = 0; g < 4 && cur() < want; g += 1) { x.press(function (v) { return v.bBonds[i].onMore; }); }
              });
              x.press('onBCheck');
              return null;
            } }
        ],
        'metals-non-metals': [
          { id: 'verdict', covers: ['verdicts'],
            fire: function (s, w, x) {
              var out = [];
              (s.verdict || []).forEach(function (val, i) {
                if (val === null || val === (w.verdict || [])[i]) { return; }
                var v = x.vals({ samp: i });
                out.push({ e: i + 1, a: val ? 'Metal' : 'Non-metal', ok: !/^L/.test(String(v.verdictNote || '')), good: function () { return val ? 'Non-metal' : 'Metal'; }, q: 'This sample is a metal or a non-metal? ' + String(v.sampleLook || '') });
              });
              return out;
            },
            back: function (r, e, st) {
              var a = (st.verdict || []).slice(); a[+e - 1] = r.answer === 'Metal';
              return { verdict: a, samp: +e - 1 };
            } }
        ],
        'reactivity-series': [
          { id: 'pred', covers: ['predicts'],
            fire: function (s, w, x) {
              if (s.pred === null || s.pred === w.pred) { return null; }
              var v = x.vals(), st = (v.strips || [])[s.strip], so = (v.sols || [])[s.sol];
              return [{ e: (s.strip + 1) + '-' + (s.sol + 1), a: s.pred ? 'Reacts' : 'No reaction', ok: /^Right/.test(String(v.swapNote || '')), good: function () { return s.pred ? 'No reaction' : 'Reacts'; }, q: 'Will it react? ' + (st ? st.label : '') + ' in ' + (so ? so.label : '') }];
            },
            back: function (r, e, st) {
              var n = String(e).split('-');
              return { strip: +n[0] - 1, sol: +n[1] - 1, pred: r.answer === 'Reacts', swaps: (st.swaps || 0) + 1 };
            } }
        ],
        'red-shift-big-bang': [
          { id: 'order', covers: ['links'],
            fire: function (s, w, x) {
              var said = lastRootPress && lastRootPress.text, grew = (s.order || []).length > (w.order || []).length;
              if (!grew && (s.wrongTap === null || s.wrongTap === w.wrongTap)) { return null; }
              return [{ e: (w.order || []).length + 1, a: said, ok: grew, good: function () { return rightBy(x, w, function (t) { return t.links; }, function (t, at) { return (at.order || []).length > (w.order || []).length; }); }, q: 'Tap the four links in order.', kind: 'choice' }];
            },
            back: function (r, e, st, x) {
              var L = x.vals().links || [], i = -1;
              L.forEach(function (l, n) { if (i < 0 && String(r.answer || '').indexOf(String(l.text)) >= 0) { i = n; } });
              if (i >= 0) { x.press(function (v) { return v.links[i].onClick; }); }
              return null;
            } }
        ],
        'stellar-evolution': [
          { id: 'step', covers: ['nextBtns'],
            fire: function (s, w, x) {
              var m = s.mass, a = (s.step || {})[m], b = (w.step || {})[m];
              if (!(a > b) || m !== w.mass) { return null; }
              return [{ e: m + '-' + a, a: lastRootPress && lastRootPress.text, ok: s.last === 'ok', good: function () { return rightBy(x, w, function (t) { return t.nextBtns; }, function (t, at) { return at.last === 'ok'; }); }, q: 'What comes next?' }];
            },
            back: function (r, e, st, x) {
              x.set({ mass: String(e).split('-')[0] });
              var i = find(x.vals().nextBtns, r.answer);
              if (i >= 0) { x.press(function (v) { return v.nextBtns[i].onClick; }); }
              return null;
            } }
        ],
        'structure-of-atom': [
          { id: 'built', covers: ['counters'],
            fire: function (s, w) {
              if (!rose(s, w, 'built')) { return null; }
              return [{ e: null, a: 'Protons ' + s.p + ', Neutrons ' + s.n + ', Electrons ' + s.e, ok: true, q: 'Make a neutral atom with 6 protons.' }];
            },
            back: function (r) {
              var n = String(r.answer || '').match(/\d+/g) || [];
              return n.length === 3 ? { p: +n[0], n: +n[1], e: +n[2], built: true } : null;
            } }
        ],
        'cell-specialisation': [
          { id: 'compared', covers: ['featBtns'],
            fire: function (s, w, x) {
              var out = [];
              Object.keys(s.compared || {}).forEach(function (k) {
                if (!s.compared[k] || (w.compared || {})[k]) { return; }
                var v = x.vals();
                out.push({ e: s.job + 1, a: (v.featBtns || []).filter(function (f) { return f.pressed; }).map(function (f) { return f.label; }).join('\n'), ok: null, q: String(v.compareLead || 'Which features does this cell have?') });
              });
              return out;
            },
            back: function (r, e, st, x) {
              x.set({ job: +e - 1 });
              String(r.answer || '').split('\n').forEach(function (t) {
                var i = find(x.vals().featBtns, t);
                if (i >= 0) { x.press(function (v) { return v.featBtns[i].onClick; }); }
              });
              x.press('onCompare');
              return null;
            } }
        ]
      };
    })();
    /* </ks4-root-forms> */
    var formPrev = null;
    // The form a row's id belongs to (the longest stem that fits), or null.
    function formOf(rest) {
      var f = null;
      (ROOT_FORMS[pathSlug] || []).forEach(function (c) { if ((rest === c.id || rest.indexOf(c.id + '-') === 0) && (!f || c.id.length > f.id.length)) { f = c; } });
      return f;
    }
    function formX(L) {
      var A = KS4RootActs;
      var x = {
        L: L,
        vals: function (at) { return A.valsAt(L, Object.assign(A.clone(L.state) || {}, at || {})); },
        set: function (p) { L.setState(p); },
        // After the lesson's next draw: a <select> drawn new takes its value only once its options exist.
        afterDraw: function (fn) { var h = document.getElementById('ks4-mount'), api = h && h.__mrbKs4; if (api && api.schedule) { api.schedule(fn); } },
        press: function (get) {
          var p = A.patchOf(L, L.state, typeof get === 'string' ? function (v) { return v[get]; } : get);
          if (p && Object.keys(p).length) { L.setState(p); }
          return p;
        },
        fast: function (get) {
          var had = Object.prototype.hasOwnProperty.call(L, 'reduced'), keep = L.reduced;
          L.reduced = typeof keep === 'function' ? function () { return true; } : true;
          L.__mrbFast = true;
          try { return x.press(get); } finally { L.__mrbFast = false; if (had) { L.reduced = keep; } else { delete L.reduced; } }
        }
      };
      return x;
    }
    /* ⊕ 9 Nov 2026: a pick or a typed value in a lesson's own activity that has not
       been committed. Not an answer, so it never reaches the server; it comes back on
       this device, per child, wherever the saved answers left that slot untouched.
       The keys are the lesson's own state: activity_save_drive --commits checks them. */
    /* <ks4-root-drafts> */
    var ROOT_DRAFT = {
      'decomposition': ['rate'], 'enzymes': ['mean'], 'states-of-matter': ['mp'], 'ionic-compounds': ['dxVal'],
      'ionic-bonding': ['moved', 'mq', 'xq', 'fm', 'fx'], 'carbon-cycle': ['labels'], 'relative-formula-mass': ['pp', 'pv'],
      'specific-latent-heat': ['picks', 'lText', 'lUnit'], 'temperature-changes-shc': ['cText', 'order'],
      'changes-in-energy': ['picks'], 'power': ['picks'], 'internal-energy': ['picks'],
      'particle-motion-pressure': ['bPick', 'p3Pick', 'p4Pick'], 'greenhouse-gases': ['rep'], 'metal-hydroxides': ['forge', 'ion'],
      'atmospheric-pollutants': ['picks'], 'atoms-elements-compounds': ['bc'], 'carbonates-halides-sulfates': ['spec'], 'covalent-bonding': ['orders'],
      'cell-specialisation': ['picks'], 'properties-small-molecules': ['order'], 'types-of-em-waves': ['placed', 'preds'],
      'series-parallel-circuits': ['preds'], 'chromosomes-mitosis': ['preds'], 'lenses': ['preds'],
      'sound-waves-hearing': ['pPred', 'tPred'], 'waves-detection-exploration': ['qPred', 'uPred'], 'conservation-of-mass': ['w3']
    };
    /* </ks4-root-drafts> */
    var rootBase = null;
    function rootDraftKey() { return pathSlug + '~own'; }
    function rootDraftTap(api) {
      var keys = ROOT_DRAFT[pathSlug];
      if (!keys || muted || !rootBase) { return; }
      var st = api.logic.state, vals = {}, any = false;
      keys.forEach(function (k) {
        if (JSON.stringify(st[k]) !== JSON.stringify(rootBase[k])) { vals[k] = st[k]; any = true; }
      });
      if (any) { draftPut(rootDraftKey(), vals); } else { draftDrop(rootDraftKey()); }
    }
    function draftMerge(cur, dv, base) {
      if (JSON.stringify(cur) === JSON.stringify(base)) { return dv; }
      if (cur && dv && typeof cur === 'object' && typeof dv === 'object') {
        var out = Array.isArray(cur) ? cur.slice() : Object.assign({}, cur);
        Object.keys(dv).forEach(function (k) { out[k] = draftMerge(cur[k], dv[k], base ? base[k] : undefined); });
        return out;
      }
      return cur;
    }
    window.MrBadmusAnswerCapture.beforeReplay.push(function () {
      var host = document.getElementById('ks4-mount'), api = host && host.__mrbKs4;
      if (ROOT_DRAFT[pathSlug] && api && api.logic) { rootBase = KS4RootActs.clone(api.logic.state); }
    });
    window.MrBadmusAnswerCapture.afterReplay.push(function () {
      var host = document.getElementById('ks4-mount'), api = host && host.__mrbKs4;
      if (!rootBase || !api || !api.logic) { return; }
      var vals = draftGet(rootDraftKey());
      if (!vals || typeof vals !== 'object') { return; }
      var patch = {}, any = false, st = api.logic.state;
      Object.keys(vals).forEach(function (k) {
        var m = draftMerge(st[k], vals[k], rootBase[k]);
        if (JSON.stringify(m) !== JSON.stringify(st[k])) { patch[k] = m; any = true; }
      });
      if (!any) { return; }
      draftTake(rootDraftKey());
      rootCarry = draftCarry[rootDraftKey()];
      delete draftCarry[rootDraftKey()];
      if (rootCarry === undefined) { rootCarry = null; }
      api.logic.setState(patch);
    });
    function formTap(api) {
      var forms = ROOT_FORMS[pathSlug];
      if (!forms) { return; }
      var L = api.logic, s = KS4RootActs.clone(L.state), w = formPrev;
      formPrev = s;
      if (!w) { return; }
      var x = formX(L);
      forms.forEach(function (f) {
        var rows = null;
        try { rows = f.fire(s, w, x); } catch (e) { return; }
        (rows || []).forEach(function (r) {
          if (r.a == null || r.a === '') { return; }
          var d = base(f.id + (r.e == null ? '' : '-' + String(r.e).toLowerCase().replace(/[^a-z0-9._-]+/g, '-')));
          d.__block = api.host; d.kind = r.kind || 'choice'; d.question_text = r.q || ''; d.answer = String(r.a);
          if (typeof r.ok === 'boolean') { d.is_correct = r.ok; }
          // Worked out only for a wrong answer: it runs the lesson's handlers on copies.
          var good = r.good;
          if (typeof good === 'function') { try { good = r.ok === false ? good() : null; } catch (e) { good = null; } }
          if (good != null) { d.correct_answer = String(good); }
          post(d);
        });
      });
    }

    /* ── ⊕ 25 Oct 2026 (Mide's item 1): EVERY lesson's own activities ──
       ROOT_SPECS above names one lesson by hand. This does the same for every
       rebuilt lesson, from the lesson's own code: a press on a ROOT control
       (one of the lesson's own option groups, never a shared block's) is
       analysed by KS4RootActs against the state the lesson had a moment
       before, and if it is an answer — one place in the state, a different
       value per option, empty to start with — it is sent like any other:
       `ks4:<slug>:<route>#<state key>[-<entry>]`, the option's own label, and
       right/wrong where the lesson itself decides it (its flag, its "Yes.",
       its tally, its alert-styled verdict). A prediction nothing judges is
       sent self-checked. Explorations (tabs, cards, selectors) send nothing.
       Read only: the probe runs the lesson's handlers on a COPY of its state
       and never draws; the real press goes ahead exactly as before. The
       groups ROOT_SPECS already names are left to it, so its ids stand. */
    var ROOT_SPEC_OPTS = {};
    (ROOT_SPECS[pathSlug] || []).forEach(function (sp) { ROOT_SPEC_OPTS[sp.opts] = 1; });
    (ROOT_FORMS[pathSlug] || []).forEach(function (f) { (f.covers || []).forEach(function (c) { ROOT_SPEC_OPTS[c] = 1; }); });
    var rootActs = null;
    function rootActsOf() {
      if (rootActs) { return rootActs; }
      var host = document.getElementById('ks4-mount');
      var api = host && host.__mrbKs4;
      if (!api || !api.logic || !api.template || api.comp !== undefined) { return null; }
      rootActs = {
        api: api,
        // The state as the lesson first drew it: a slot that started on a
        // value is a selector, never an answer.
        init: KS4RootActs.clone(api.logic.state),
        groups: KS4RootActs.groupsOf(api.template).filter(function (g) { return !ROOT_SPEC_OPTS[g.e]; })
      };
      return rootActs;
    }
    try { rootActsOf(); } catch (e) { /* the page has no rebuilt lesson */ }
    function rootOwned(el, host) {
      for (var up = el.parentNode; up; up = up.parentNode) { if (up.__mrbKs4) { return up === host; } }
      return false;
    }
    // Words of an element that are not inside one of its buttons.
    function ownWords(el) {
      var out = [];
      (function walk(n) {
        for (var c = n.firstChild; c; c = c.nextSibling) {
          if (c.nodeType === 3) { out.push(c.nodeValue); }
          else if (c.nodeType === 1 && c.tagName !== 'BUTTON' && !c.hasAttribute('hidden') && c.tagName !== 'svg' && c.tagName !== 'SVG') { walk(c); }
        }
      })(el);
      return out.join(' ').replace(/\s+/g, ' ').trim();
    }
    /* The question AS SHOWN, read before the press: the section's heading
       above the control, the last line above it (its "commit" line where it
       has one), and the item's own words where the options sit in a row of
       their own. */
    function rootAsk(btn, host) {
      var sec = btn.closest('section') || host;
      if (!host.contains(sec)) { sec = host; }
      var seen = function (el) { return !el.closest('[hidden]') && !!(el.getClientRects && el.getClientRects().length); };
      var above = function (el) { return !!(el.compareDocumentPosition(btn) & 4) && !el.contains(btn); };
      var head = '', line = '', near = '';
      Array.prototype.forEach.call(sec.querySelectorAll('h2, h3'), function (h) { if (seen(h) && above(h) && !h.closest('button')) { head = txt(h); } });
      Array.prototype.forEach.call(sec.querySelectorAll('p'), function (p) {
        if (seen(p) && above(p) && !p.closest('button') && !p.querySelector('button') && !/eyebrow/.test(p.className || '')) { line = txt(p); }
      });
      for (var up = btn.parentElement; up && up !== sec && up !== host; up = up.parentElement) {
        var w = ownWords(up);
        if (w) { near = w.length > 300 ? w.slice(0, 300) : w; break; }
      }
      var parts = [];
      [head, line, near].forEach(function (x) {
        if (x && !parts.some(function (y) { return y.indexOf(x) >= 0 || x.indexOf(y) >= 0; })) { parts.push(x); }
      });
      return parts.join(' — ');
    }
    /* ⊕ 9 Nov 2026 (a blind run: "Self-checked" beside a page that had said "goes up,
       not stays the same"). `self_checked` means the child compared their own work with
       a shown answer. A commitment nothing judges goes unmarked. A commitment the page
       judges a moment later is judged here: the lesson's own render is asked what it
       would draw, for each option, and its verdict style says which are right. `show`
       opens that on a COPY of the state; `read` is the verdict for this slot. */
    var ROOT_JUDGE = {
      'red-shift-big-bang': { pred: { show: function (s) { s.gal = 2; }, read: function (v) { return { style: v.specNoteStyle }; } } }
    };
    function rootJudged(r, pre) {
      var cfg = (ROOT_JUDGE[pathSlug] || {})[String(r.slot && r.slot[0])], R = rootActsOf();
      if (!cfg || !R || r.kind !== 'pick') { return null; }
      var A = KS4RootActs, L = R.api.logic, right = [], label = null, seen = false;
      r.options.forEach(function (o) {
        if (!o.patch) { return; }
        var st = A.apply(pre, o.patch);
        cfg.show(st, r.slot);
        var w = cfg.read(A.valsAt(L, st), r.slot);
        if (!w || !w.style) { return; }
        seen = true;
        if (!/ks3-alert/.test(w.style)) { right.push(o.k); if (label === null) { label = o.label; } }
      });
      return seen && right.length ? { right: right, label: label } : null;
    }
    function rootAnswer(R, g, pre, me, ask, hit) {
      var A = KS4RootActs, L = R.api.logic;
      var r = A.analyse(L, g, pre, R.init, me.oi);
      /* ⊕ 9 Nov 2026: a blind run lost the fifth of five answers. Analysed with four
         already right, the fifth's words stopped looking like a tally, so it read as an
         exploration and was never sent. A group that takes answers from a clean start
         keeps taking them: never drop an answer on how the words happen to read now. */
      if (r.kind !== 'pick' && r.kind !== 'gate' && r.kind !== 'multi') {
        var r0 = A.analyse(L, g, R.init, R.init, me.oi);
        if (r0.kind !== 'pick' && r0.kind !== 'gate' && r0.kind !== 'multi') { return; }
        r = A.classify(L, g, pre, R.init, me.oi);
        if (r.kind !== 'pick' && r.kind !== 'gate' && r.kind !== 'multi') { return; }
        if (r0.graded && r0.right && r.kind === r0.kind) { r.right = r0.right; r.graded = true; }
      }
      var o = null;
      r.options.forEach(function (x) { if (x.k === me.k) { o = x; } });
      if (!o || !o.ws || !o.ws.length) { return; }          // this press changes nothing: not a new answer
      // The lesson took it: its state now holds what this option writes.
      var took = o.ws.every(function (w) { return JSON.stringify(A.at(L.state, w.path)) === JSON.stringify(w.after); });
      if (!took) { return; }
      if (r.kind === 'multi' && me.k !== r.check) { return; }  // a toggle: the Check is the answer
      // One button is a control ("Drop it in"), not a choice between anything.
      if (r.kind === 'pick' && r.options.filter(function (x) { return x.ws && x.ws.length; }).length < 2) { return; }
      var labelOf = function (k) { var l = null; r.options.forEach(function (x) { if (x.k === k) { l = x.label; } }); return l; };
      var d = base(A.slotId(r, me.oi));
      d.__block = hit; d.kind = 'choice'; d.question_text = ask;
      if (r.kind === 'multi') {
        var sel = A.at(pre, r.slot);
        d.answer = (Array.isArray(sel) ? sel : []).map(labelOf).filter(Boolean).join('\n');
        // The lesson's own flag, asked with every earlier "ok" cleared.
        var st2 = A.clone(pre) || {};
        Object.keys(st2).forEach(function (k) { if (st2[k] === true && /ok$/i.test(k)) { st2[k] = false; } });
        var chk = A.probe(L, g, st2, me.oi).filter(function (x) { return x.k === r.check; })[0];
        var okw = chk && chk.ws.filter(function (w) { return typeof w.after === 'boolean' && /ok$/i.test(String(w.path[w.path.length - 1])); })[0];
        if (okw) { d.is_correct = okw.after; }
      } else {
        d.answer = o.label;
        if (r.graded && r.right && r.right.length) {
          d.correct_answer = labelOf(r.right[0]);
          d.is_correct = r.right.indexOf(me.k) >= 0;
        } else {
          var jr = rootJudged(r, pre);
          if (jr) { d.is_correct = jr.right.indexOf(me.k) >= 0; d.correct_answer = jr.label; }
        }
      }
      post(d);
    }
    document.addEventListener('click', function rootActClick(e) {
      try {
        var R = rootActsOf();
        if (!R) { return; }
        var host = R.api.host, t = e.target;
        if (!t || !t.closest || !host.contains(t)) { return; }
        var hit = null;
        for (var el = t; el && el !== host; el = el.parentNode) {
          if (el.__mrbKs4) { return; }                     // inside a shared block: its own capture
          if (!hit && el.__mrbClickBound) { hit = el; }
        }
        if (hit) { lastRootPress = { text: txt(hit) }; }
        if (!R.groups.length) { return; }
        if (!hit || hit.disabled || hit.getAttribute('aria-disabled') === 'true') { return; }
        var tpl = parseInt(hit.getAttribute('data-dc-tpl'), 10), g = null;
        R.groups.forEach(function (x) { if (x.tpl === tpl) { g = x; } });
        if (!g) { return; }
        var A = KS4RootActs, L = R.api.logic, pre = A.clone(L.state);
        var flat = A.itemsOf(g, A.valsAt(L, pre));
        var mine = Array.prototype.filter.call(host.querySelectorAll('[data-dc-tpl="' + tpl + '"]'), function (x) { return rootOwned(x, host); });
        var me = null;
        if (mine.length === flat.length) { me = flat[mine.indexOf(hit)] || null; }
        else {
          var said = txt(hit);
          var by = flat.filter(function (f) { var l = A.labelText(g, f.item); return l && said.indexOf(l) >= 0; });
          if (by.length === 1) { me = by[0]; }
        }
        if (!me) { return; }
        var ask = rootAsk(hit, host);
        // After the lesson has handled the press (and drawn), off the click.
        setTimeout(function () { try { rootAnswer(R, g, pre, me, ask, hit); } catch (err) { /* never breaks a lesson */ } }, 30);
      } catch (err) { /* capture never breaks a lesson */ }
    }, true);

    /* ⊕ 9 Nov 2026: a written answer and a five-line calculation typed and not yet
       opened (draftPut). A Ks4Write anywhere; a calculation at the lesson's own level. */
    function draftsOf(api) {
      var st = api.logic.state || {}, out = [];
      if (api.comp === 'Ks4Write') {
        var q = writeQid(api);
        if (q) { out.push({ id: q, done: !!st.open, val: st.text, empty: !String(st.text || '').trim(), put: function (v) { api.logic.setState({ text: String(v) }); } }); }
      } else if (api.comp === 'Ks4Cfifa' && rootLevel(api)) {
        var k = nth(api);
        ((api.logic.props || {}).questions || []).forEach(function (o, i) {
          var cur = (st.q || {})[i] || { lines: [], ticks: [], open: false };
          out.push({ id: pilotId(pathSlug, 'cfifa-' + k + '-' + (i + 1)), done: !!cur.open, val: cur.lines, empty: !(cur.lines || []).some(function (l) { return String(l || '').trim(); }),
            put: function (v) { var nq = Object.assign({}, api.logic.state.q || {}); nq[i] = Object.assign({ ticks: [], open: false }, nq[i] || {}, { lines: v }); api.logic.setState({ q: nq }); } });
        });
      } else if (api.comp === 'Ks4Steps' && rootLevel(api) && (api.logic.props || {}).mode === 'attempt') {
        var vs = st.vals || {};
        out.push({ id: pilotId(pathSlug, 'steps-' + nth(api)), done: !!st.checked, val: vs, empty: !Object.keys(vs).some(function (x) { return String(vs[x] || '').trim(); }), put: function (v) { api.logic.setState({ vals: v }); } });
      }
      return out;
    }
    function draftTap(api) {
      draftsOf(api).forEach(function (d) {
        if (d.done || d.empty) { draftDrop(d.id); } else { draftPut(d.id, d.val); }
      });
    }
    window.MrBadmusAnswerCapture.afterReplay.push(function () {
      var seen = [];
      Array.prototype.forEach.call(document.querySelectorAll('[data-dc-tpl]'), function (el) {
        var api = el.__mrbKs4;
        if (!api || !api.logic || api.comp === undefined || seen.indexOf(api) >= 0) { return; }
        seen.push(api);
        draftsOf(api).forEach(function (d) {
          if (d.done) { draftDrop(d.id); return; }
          var v = d.empty ? draftGet(d.id) : null;
          if (v) { draftTake(d.id); d.put(v); }
        });
      });
    });

    window.MrBadmusKS4Tap = function (api) {
      if (!api || !api.logic || !prevOf) { return; }
      if (api.comp !== undefined) { try { draftTap(api); } catch (e) { /* never breaks a lesson */ } }
      // ⊕ Saved work follow-up: the lesson's own one-off activities (the
      // page's root instance) and the child's own ticks.
      if (api.comp === undefined) {
        try { rootTap(api); } catch (e) { /* never breaks a lesson */ }
        try { formTap(api); } catch (e) { /* never breaks a lesson */ }
        try { rootDraftTap(api); } catch (e) { /* never breaks a lesson */ }
        return;
      }
      try { tickTap(api); } catch (e) { /* never breaks a lesson */ }
      var h = HANDLERS[api.comp];
      if (!h) { return; }
      var s = api.logic.state || {};
      var prev = prevOf.get(api) || EMPTY;
      prevOf.set(api, snap(s));
      curBlock = api.host || null;
      try { h(api, s, prev); } catch (e) { /* capture never breaks a lesson */ }
      curBlock = null;
    };

    /* ── Saved work, KS4 rebuilt (pilot) page: each block's own state ──
       Every shared block that takes an answer is handed back the state its
       saved answers describe, through the block's own setState — the same
       call its buttons make — so the block draws itself exactly as it was:
       the option picked and its verdict, the five lines typed, the chain in
       its order, the writing with its mark scheme open. Ids are matched the
       way the tap above WRITES them (pilotId, nth, the ladder's own slug); a
       practice-set question by its text (the server hashed its id from it).
       A block the child has already answered on this visit is left alone.
       The tap then sees these states arrive; `mute` (held by the loader until
       the redraw has run) stops any of them being sent again.

       Self-marking on a fresh device: a written answer's ticks are the
       points the server's marking credited (points_hit, 1-based, against the
       same list the page shows) — the child's own ticks were never sent. */
    function idxOf(opts, text) {
      for (var i = 0; i < (opts || []).length; i += 1) { if (opts[i] && same(opts[i].full != null ? opts[i].full : opts[i].text, text)) { return i; } }
      return -1;
    }
    function calcBack(it, answer) {
      var c = it.convOptions || [], a = String(answer == null ? '' : answer), conv = null, best = -1;
      for (var i = 0; i < c.length; i += 1) {
        var lead = String(c[i]) + ' \u2192 ';
        if (a.indexOf(lead) === 0 && lead.length > best) { conv = i; best = lead.length; }
      }
      var rest = conv === null ? a : a.slice(best);
      var unit = '';
      (it.units || []).forEach(function (u) {
        u = String(u);
        if (u && (rest === u || rest.slice(-(u.length + 1)) === ' ' + u) && u.length > unit.length) { unit = u; }
      });
      return { conv: conv, num: (unit ? rest.slice(0, rest.length - unit.length) : rest).trim(), unit: unit };
    }
    function chainBack(links, herr, answer) {
      var used = {}, out = [];
      String(answer == null ? '' : answer).split('\n').forEach(function (line) {
        var i;
        for (i = 0; i < (links || []).length; i += 1) { if (!used['L' + i] && same(links[i], line)) { used['L' + i] = 1; out.push('L' + i); return; } }
        for (i = 0; i < (herr || []).length; i += 1) { if (!used['H' + i] && herr[i] && same(herr[i].text, line)) { used['H' + i] = 1; out.push('H' + i); return; } }
      });
      return out;
    }
    /* ⊕ Saved work follow-up (16 Oct 2026): the ticks are the child's OWN
       (`self_ticks`, 1-based, saved by sendTicks). The marker's credit
       (points_hit) is never shown as the child's ticks — that showed marking
       point 1 unticked on a rung the child had ticked 6 of 6 and awarded
       themselves 4 of 4 (the marker had credited points 2–6). */
    function ticksBack(r, n) {
      var t = [];
      if (!r || !n || !ownTicks(r)) { return t; }
      ownTicks(r).forEach(function (h) { if (h >= 1 && h <= n) { t[h - 1] = true; } });
      return t;
    }
    // A Ks4Write put back; returns the marks its own tally now shows. An
    // older row with no saved ticks falls back to the marker's score.
    function writeBack(w, r, points, marks, notify) {
      if (!w || !w.logic || !r) { return null; }
      var ws = w.logic.state || {};
      if (ws.open || String(ws.text || '').trim()) { return null; }
      // ⊕ 25 Oct 2026: a level-marked write gets its level back (levelTicks);
      // the tally is then the top of that level, as it was on the page.
      var lvs = (w.logic.props || {}).levels || [];
      if (lvs.length) {
        var own = ownTicks(r) || [], lv = null, tkl = [];
        own.forEach(function (h) {
          if (h >= 1 && h <= lvs.length) { lv = h - 1; }
          else if (h > lvs.length && h - lvs.length <= ((w.logic.props || {}).points || []).length) { tkl[h - lvs.length - 1] = true; }
        });
        w.logic.setState({ text: String(r.answer || ''), open: true, level: lv, ticks: tkl, reported: true });
        var awl = lv !== null ? Math.min(marks, (lvs[lv] && lvs[lv].max) || 0) : (r.marks_scored == null ? 0 : r.marks_scored);
        var wpl = w.logic.props || {};
        if (notify && lv !== null && typeof wpl.onMark === 'function') { wpl.onMark({ awarded: awl, marks: marks, set: true }); }
        return awl;
      }
      var ticks = ticksBack(r, (points || []).length);
      var n = ticks.filter(Boolean).length;
      w.logic.setState({ text: String(r.answer || ''), open: true, ticks: ticks, reported: true });
      var aw = (points || []).length && ownTicks(r) ? Math.min(marks, n) : (r.marks_scored == null ? 0 : r.marks_scored);
      // A Write on its own tells the lesson it was marked, as it does live.
      var wp = w.logic.props || {};
      if (notify && (points || []).length && typeof wp.onMark === 'function') { wp.onMark({ awarded: aw, marks: marks, set: true }); }
      return aw;
    }
    // A block's own "done" signal to its lesson, as the block sends it live,
    // so the lesson's progress (its rail, "N of 5 done") counts it.
    function tell(fn) { if (typeof fn === 'function') { try { fn.apply(null, Array.prototype.slice.call(arguments, 1)); } catch (e) { /* never breaks a lesson */ } } }
    /* ⊕ 9 Nov 2026: the page's own rule is that a rung scores the FIRST check of a
       chain since it was last dealt ("The rung scores your first attempt"), and "Retry
       my misses" deals it again. The rung's handler sends that check with the rung
       named; a later "Check again" is sent with none. So the row that scored is the
       last one naming its rung. (An older "Check again" did name it, and reads as a
       retry.) Reading the first row gave 3 of 4 where the page had said 4 of 4. */
    function scoredAt(rs) {
      for (var i = (rs || []).length - 1; i >= 0; i -= 1) { if (rs[i] && rs[i].rung) { return i; } }
      return 0;
    }
    function chainSet(ch, rs, links, herr) {
      if (!ch || !ch.logic || !rs || !rs.length || (ch.logic.state || {}).attempts) { return; }
      ch.logic.setState({ chain: chainBack(links, herr, lastOf(rs).answer), checked: true, attempts: rs.length - scoredAt(rs), reported: true });
    }
    replay.push(function (rows) {
      var ids = byId(rows);
      var quiz = {};
      (rows || []).forEach(function (r) {
        if (r && /^ks4q:/.test(String(r.question_id || ''))) { quiz[quizKey(r.question_text)] = r; }   // the last wins
      });
      var seen = [];
      Array.prototype.forEach.call(document.querySelectorAll('[data-dc-tpl]'), function (el) {
        var api = el.__mrbKs4;
        if (!api || !api.logic || seen.indexOf(api) >= 0) { return; }
        seen.push(api);
        try { putBack(api); } catch (e) { /* one block never stops the rest */ }
      });
      try { rootBack(); } catch (e) { /* the lesson's own activities never stop the rest */ }
      try { rootActsBack(); } catch (e) { /* the lesson's own activities never stop the rest */ }
      try { formsBack(); } catch (e) { /* the lesson's own activities never stop the rest */ }
      /* ⊕ 8 Nov 2026: the forms, typed answers and builders (ROOT_FORMS), each
         row oldest first, so a changed answer ends on the latest. */
      function formsBack() {
        var forms = ROOT_FORMS[pathSlug];
        var host = document.getElementById('ks4-mount');
        var api = host && host.__mrbKs4;
        if (!forms || !api || !api.logic) { return; }
        var L = api.logic, x = formX(L), prefix = pilotId(pathSlug, '');
        // The same reduced path as rootActsBack: a restored step lands finished, never mid-animation.
        var had = Object.prototype.hasOwnProperty.call(L, 'reduced'), keep = L.reduced;
        L.reduced = typeof keep === 'function' ? function () { return true; } : true;
        L.__mrbFast = true;
        try {
          (rows || []).forEach(function (r) {
            var id = String((r && r.question_id) || '');
            if (id.indexOf(prefix) !== 0) { return; }
            var rest = id.slice(prefix.length), f = formOf(rest);
            if (!f) { return; }
            try {
              var p = f.back(r, rest === f.id ? null : rest.slice(f.id.length + 1), L.state, x);
              if (p) { L.setState(p); }
            } catch (e) { /* one answer never stops the rest */ }
          });
        } finally {
          L.__mrbFast = false;
          if (had) { L.reduced = keep; } else { delete L.reduced; }
        }
      }
      /* ⊕ 25 Oct 2026: every other lesson's own activities (rootActClick).
         Each saved row, oldest first, is matched to the group whose answer
         slot it names — on the lesson's state as it is now, else with the
         step the id numbers (a "structure 4 of 7" style stepper) — and the
         option with the saved label is applied through the lesson's own
         handler, run against a copy of its state: exactly the change the
         press made, flags and tallies included. The step the child last
         answered on is put back on screen. */
      /* ⊕ 9 Nov 2026: a blind run's step 2 came back blank and answerable. Restoring
         step 1 ran its handler as if the child had just pressed it, which starts an
         animation, and a lesson refuses the next answer while one runs. So a restore
         takes the lesson's own reduced-motion path: every step lands finished. */
      function rootActsBack() {
        var R = rootActsOf();
        if (!R || !R.groups.length) { return; }
        var L0 = R.api.logic, had = Object.prototype.hasOwnProperty.call(L0, 'reduced'), keep = L0.reduced;
        L0.reduced = typeof keep === 'function' ? function () { return true; } : true;
        L0.__mrbFast = true;
        try { rootActsPut(R); } finally {
          L0.__mrbFast = false;
          if (had) { L0.reduced = keep; } else { delete L0.reduced; }
        }
      }
      function rootActsPut(R) {
        var A = KS4RootActs, L = R.api.logic, prefix = pilotId(pathSlug, '');
        var mine = (rows || []).filter(function (r) { return r && r.answer_kind === 'choice' && String(r.question_id || '').indexOf(prefix) === 0 && !formOf(String(r.question_id).slice(prefix.length)); });
        if (!mine.length) { return; }
        var keyOf = function (k) { return String(k).toLowerCase().replace(/[^a-z0-9:#._-]+/g, '-'); };
        // The state keys each group's options write, learnt once.
        var keys = R.groups.map(function (g) {
          var out = {}, st = A.clone(L.state), vals = A.valsAt(L, st);
          var ois = g.inner ? A.itemsOf(g, vals).map(function (x) { return x.oi; }) : [null];
          ois.filter(function (v, i) { return ois.indexOf(v) === i; }).forEach(function (oi) {
            A.probe(L, g, st, oi).forEach(function (o) { (o.ws || []).forEach(function (w) { out[keyOf(w.path[0])] = 1; }); });
          });
          return out;
        });
        var scal = Object.keys(L.state || {}).filter(function (k) { return typeof L.state[k] === 'number' && k !== 'active'; });
        var lastStep = null;
        mine.forEach(function (row) {
          var rest = String(row.question_id).slice(prefix.length);
          var nums = (rest.match(/\d+/g) || []).map(Number);
          var found = null;
          var tryAt = function (state, ctxKey) {
            for (var gi = 0; gi < R.groups.length && !found; gi += 1) {
              var g = R.groups[gi], kk = keys[gi], hit = false;
              for (var k in kk) { if (Object.prototype.hasOwnProperty.call(kk, k) && rest.indexOf(k) === 0) { hit = true; } }
              if (!hit && Object.keys(kk).length) { continue; }
              var ois = g.inner ? A.itemsOf(g, A.valsAt(L, state)).map(function (x) { return x.oi; }) : [null];
              ois = ois.filter(function (v, i) { return ois.indexOf(v) === i; });
              for (var j = 0; j < ois.length && !found; j += 1) {
                var r = A.classify(L, g, state, R.init, ois[j]);
                if ((r.kind === 'pick' || r.kind === 'gate' || r.kind === 'multi') && A.slotId(r, ois[j]) === rest) {
                  found = { g: g, oi: ois[j], r: r, state: state, ctx: ctxKey };
                }
              }
            }
            return !!found;
          };
          if (!tryAt(A.clone(L.state), null)) {
            for (var si = 0; si < scal.length && !found; si += 1) {
              for (var ni = 0; ni < nums.length && !found; ni += 1) {
                var st = A.clone(L.state);
                if (st[scal[si]] === nums[ni] - 1) { continue; }
                st[scal[si]] = nums[ni] - 1;
                tryAt(st, scal[si]);
              }
            }
          }
          if (!found) { return; }
          var r = found.r, patch = null;
          if (r.kind === 'multi') {
            if (found.r.slot.length !== 1) { return; }
            var want = String(row.answer || '').split('\n');
            var sel = r.options.filter(function (o) { return o.k !== r.check && want.some(function (w) { return same(w, o.label); }); }).map(function (o) { return o.k; });
            var p1 = {}; p1[r.slot[0]] = sel;
            var chk = A.probe(L, found.g, A.apply(found.state, p1), found.oi).filter(function (o) { return o.k === r.check; })[0];
            patch = Object.assign(p1, (chk && chk.patch) || {});
          } else {
            var o = r.options.filter(function (x) { return same(x.label, row.answer); })[0];
            if (!o || !o.patch || !o.ws.length) { return; }
            patch = o.patch;
          }
          L.setState(patch);
          if (found.ctx && !Object.prototype.hasOwnProperty.call(patch, found.ctx)) { lastStep = { k: found.ctx, v: found.state[found.ctx] }; }
        });
        if (lastStep) { var back = {}; back[lastStep.k] = lastStep.v; L.setState(back); }
      }
      /* The lesson's own one-off activities (ROOT_SPECS): each saved choice
         back in the lesson's root state, and the item on screen moved to
         where the child would naturally carry on — the first item after the
         last one they answered, or the last item when all are answered. */
      function rootBack() {
        var specs = ROOT_SPECS[pathSlug];
        var host = document.getElementById('ks4-mount');
        var api = host && host.__mrbKs4;
        if (!specs || !api || !api.logic) { return; }
        var L = api.logic, patch = {}, has = false;
        specs.forEach(function (sp) {
          var map = Object.assign({}, (L.state || {})[sp.pick] || {}), last = -1, total = 0;
          for (var j = 0; j < 60; j += 1) {
            var at = {}; at[sp.step] = j;
            var v;
            try { v = valsAt(L, at); } catch (e) { break; }
            if (!v || v[sp.title] == null) { break; }
            total = j + 1;
            var r = lastOf(ids[pilotId(pathSlug, sp.id + '-' + (j + 1))]);
            if (!r || map[j] !== undefined) { continue; }
            var i = labelsOf(v, sp).map(function (l) { return same(l, r.answer); }).indexOf(true);
            if (i >= 0) { map[j] = i; last = Math.max(last, j); }
          }
          if (last < 0) { return; }
          patch[sp.pick] = map;
          patch[sp.step] = last < total - 1 ? last + 1 : last;
          rootPrev[sp.pick] = Object.assign({}, map);
          has = true;
        });
        if (has) { L.setState(patch); }
      }
      function rowsOf(id) { return ids[pilotId(pathSlug, id)] || null; }
      function putBack(api) {
        var L = api.logic, p = L.props || {}, st = L.state || {}, r, rs, i;
        switch (api.comp) {
          case 'Ks4Guess':
            if (!rootLevel(api) || st.pick != null || !(r = lastOf(rowsOf('start')))) { return; }
            i = idxOf((p.options || []).slice(0, 2), r.answer);
            if (i >= 0) { L.setState({ pick: i }); tell(p.onCommit, i, !!((p.options || [])[i] || {}).correct); }
            return;
          case 'Ks4Choice':
            if (!rootLevel(api) || st.pick != null || !(r = lastOf(rowsOf('choice-' + nth(api))))) { return; }
            i = idxOf(p.options, r.answer);
            if (i >= 0) { L.setState({ pick: i }); tell(p.onCommit, i, (p.options || [])[i]); }
            return;
          case 'Ks4QuizBank': {
            if (!rootLevel(api)) { return; }
            var picks = Object.assign({}, st.picks || {}), any = false, top = -1;
            (p.questions || []).filter(Boolean).slice(0, quizLimit(api)).forEach(function (q, k) {
              var qr = quiz[quizKey(q.prompt)];
              if (!qr || picks[k] !== undefined) { return; }
              var j = idxOf(q.options, qr.answer);
              if (j >= 0) { picks[k] = j; any = true; top = Math.max(top, k); }
            });
            // ⊕ 25 Oct 2026 (item 5): a question answered beyond the ones the
            // block shows at first (the pilot's "Show 4 more") stays OPEN, not
            // folded away behind the button.
            var qp = { picks: picks };
            if (typeof st.shown === 'number' && top + 1 > st.shown) { qp.shown = top + 1; }
            if (any) { L.setState(qp); }
            return;
          }
          case 'Ks4Write':
            if (!rootLevel(api)) { return; }
            writeBack(api, lastOf(rowsOf('write-' + nth(api))), p.levels && p.levels.length ? [] : p.points, p.marks || 4, true);
            return;
          case 'Ks4Chain':
            if (!rootLevel(api) || st.attempts) { return; }
            rs = rowsOf('chain-' + nth(api));
            chainSet(api, rs, p.links || [], p.herrings || []);
            if (rs && rs.length) { tell(p.onDone, { correct: rs[0].is_correct === true }); }
            return;
          case 'Ks4Sort': {
            if (!rootLevel(api) || st.checked || Object.keys(st.placed || {}).length) { return; }
            var k4 = nth(api), bins = p.bins || [], placed = {}, got = false;
            (p.items || []).forEach(function (it, n) {
              var sr = lastOf(rowsOf('sort-' + k4 + '-' + (n + 1)));
              if (!sr) { return; }
              for (var b = 0; b < bins.length; b += 1) { if (same(bins[b].label, sr.answer)) { placed[n] = bins[b].id; got = true; return; } }
            });
            if (got) {
              L.setState({ placed: placed, checked: true, reported: true });
              var allRight = (p.items || []).every(function (it, n) { return placed[n] !== undefined && placed[n] === it.bin; });
              tell(p.onDone, { correct: allRight });
            }
            return;
          }
          case 'Ks4Cfifa': {
            if (!rootLevel(api)) { return; }
            var kc = nth(api), qs = Object.assign({}, st.q || {}), gotC = false;
            (p.questions || []).forEach(function (o, n) {
              var cr = lastOf(rowsOf('cfifa-' + kc + '-' + (n + 1)));
              if (!cr || (qs[n] && qs[n].open)) { return; }
              var lines = String(cr.answer || '').split('\n');
              qs[n] = { lines: (o.steps || []).map(function (stp, j) {
                var line = lines[j] == null ? '' : lines[j], lead = stp.label ? stp.label + ': ' : '';
                return lead && line.indexOf(lead) === 0 ? line.slice(lead.length) : line;
              }), ticks: ticksBack(cr, (o.steps || []).length), open: true };
              gotC = true;
            });
            if (gotC) {
              /* ⊕ 25 Oct 2026 (item 5): "Your turn" reopens on the question the
                 child was on — the first one they have not checked yet, else
                 the one they checked last — never always on Question 1. */
              var nQ = (p.questions || []).length, firstOpen = -1, cfAt = '', lastQ = 0;
              for (var qn = 0; qn < nQ; qn += 1) {
                if (!(qs[qn] && qs[qn].open) && firstOpen < 0) { firstOpen = qn; }
                var lr = lastOf(rowsOf('cfifa-' + kc + '-' + (qn + 1)));
                if (lr && String(lr.answered_at || '') >= cfAt) { cfAt = String(lr.answered_at || ''); lastQ = qn; }
              }
              L.setState({ q: qs, qEx: firstOpen >= 0 ? firstOpen : lastQ });
              var open = (p.questions || []).filter(function (o, n) { return qs[n] && qs[n].open; }).length;
              tell(p.onOpen, open, (p.questions || []).length);
            }
            return;
          }
          case 'Ks4Steps': {
            if (!rootLevel(api) || p.mode !== 'attempt' || st.checked || !(r = lastOf(rowsOf('steps-' + nth(api))))) { return; }
            var sl = String(r.answer || '').split('\n'), vals = {}, at = 0;
            (p.steps || []).forEach(function (stp, si) {
              (stp.lines || []).forEach(function (ln, j) {
                var line = sl[at] == null ? '' : sl[at], lead = ln.label ? ln.label + ': ' : '';
                at += 1;
                vals[si + '-' + j] = lead && line.indexOf(lead) === 0 ? line.slice(lead.length) : line;
              });
            });
            var tk = {}, own = ownTicks(r) || [], n1 = 0;
            (p.steps || []).forEach(function (stp, si) {
              (stp.lines || []).forEach(function (ln, j) { n1 += 1; if (own.indexOf(n1) >= 0) { tk[si + '-' + j] = true; } });
            });
            L.setState({ vals: vals, ticks: tk, checked: true });
            tell(p.onDone);
            return;
          }
          case 'Ks4Ladder': {
            var R = p.rungs || {}, slug = p.slug || pathSlug, patch = {}, has = false;
            var lid = function (key) { return ids[pilotId(slug, key)] || null; };
            if (st.r1 == null && (r = lastOf(lid('r1')))) {
              i = idxOf((R.r1 || {}).options, r.answer);
              if (i >= 0) { patch.r1 = !!((R.r1.options[i] || {}).correct); patch.r1Pick = i; has = true; }
            }
            if (st.r2 == null && (r = lastOf(lid('r2')))) {
              var r2 = R.r2 || {}, kind = r2.kind || 'calc';
              if (kind === 'calc') {
                var cb = calcBack(r2, r.answer);
                patch.r2conv = cb.conv; patch.r2num = cb.num; patch.r2unit = cb.unit;
              } else if (kind === 'text') {
                patch.r2num = String(r.answer || '');
              } else {
                var parts = {}, pl = String(r.answer || '').split('\n');
                (r2.parts || []).forEach(function (pt, n) {
                  var line = pl[n] == null ? '' : pl[n], lead = (pt.label || '') + ': ';
                  if (line.indexOf(lead) === 0) { line = line.slice(lead.length); }
                  var o = (pt.options || []).map(String).indexOf(line);
                  if (o >= 0) { parts[n] = String(o); }
                });
                patch.r2parts = parts;
              }
              patch.r2 = r.is_correct === true; has = true;
            }
            rs = lid('r3');
            if (st.r3 == null && rs && rs.length) {
              patch.r3 = rs[scoredAt(rs)].is_correct === true; has = true;
              chainSet(kids(api, 'Ks4Chain')[0], rs, (R.r3 || {}).links || [], (R.r3 || {}).herrings || []);
            }
            if (st.r4 == null && (r = lastOf(lid('r4')))) {
              var r4 = R.r4 || {}, mk4 = r4.marks || 4;
              var aw = writeBack(kids(api, 'Ks4Write')[0], r, r4.levels && r4.levels.length ? [] : r4.points, mk4);
              if (aw != null) { patch.r4 = aw >= Math.ceil(mk4 / 2); patch.r4a = aw; has = true; }
            }
            if (has) { L.setState(patch); }
            return;
          }
          case 'Ks4Practice': {
            var RP = p.rungs || {}, LP = [RP.r1 || [], RP.r2 || [], RP.r3 || [], RP.r4 || []];
            var q = Object.assign({}, st.q || {}), hid = st.hidden || {}, chainKeys = [], writeKeys = [], gotP = false;
            LP.forEach(function (items, ri) {
              items.forEach(function (it, n) {
                var kk = ri + '-' + n, kd = it.kind || 'mcq';
                if (kd === 'chain' && !hid[kk]) { chainKeys.push(kk); }
                if (kd === 'write' && !hid[kk]) { writeKeys.push(kk); }
              });
            });
            LP.forEach(function (items, ri) {
              items.forEach(function (it, n) {
                var kk = ri + '-' + n, kd = it.kind || 'mcq', cur = q[kk] || {};
                if (cur.res != null) { return; }
                var prs = ids[pilotId(pathSlug, 'r' + (ri + 1) + '-' + (n + 1))];
                var pr = lastOf(prs);
                if (!pr) { return; }
                var base = { res: null, pick: null, conv: null, num: '', unit: '' };
                if (kd === 'mcq') {
                  var j = idxOf(it.options, pr.answer);
                  if (j < 0) { return; }
                  q[kk] = Object.assign(base, cur, { res: !!(it.options[j] || {}).correct, pick: j });
                } else if (kd === 'calc') {
                  var cbp = calcBack(it, pr.answer);
                  q[kk] = Object.assign(base, cur, { res: pr.is_correct === true, conv: cbp.conv, num: cbp.num, unit: cbp.unit });
                } else if (kd === 'chain') {
                  q[kk] = Object.assign(base, cur, { res: prs[scoredAt(prs)].is_correct === true });
                  chainSet(kids(api, 'Ks4Chain')[chainKeys.indexOf(kk)], prs, it.links || [], it.herrings || []);
                } else {
                  var mkw = it.marks || [1, 3, 3, 6][ri];
                  var awp = writeBack(kids(api, 'Ks4Write')[writeKeys.indexOf(kk)], pr, it.levels && it.levels.length ? [] : it.points, mkw);
                  if (awp == null) { return; }
                  q[kk] = Object.assign(base, cur, { res: awp >= Math.ceil(mkw / 2), awarded: awp });
                }
                gotP = true;
              });
            });
            if (gotP) { L.setState({ q: q }); }
            // ⊕ 9 Nov 2026: "Best before today" comes from the saved rows, so every device
            // reads the same and today's own answers are never "before today".
            L.setState({ best: bestBefore(LP, hid, ids) });
            return;
          }
          default:
            return;
        }
      }
    });
  })();
} catch (e) {}

/* ── Saved work (Mide, 16 Oct 2026): a child's lesson comes back as they
   left it ──────────────────────────────────────────────────────────────
   "Pages don't restore saved work. When a child returns to a lesson … only
   written answers reappear (from the device). Multiple-choice answers and the
   tutor conversation are gone, though both are on the server. On load, every
   page restores from the server: every answer the child gave, right/wrong
   and marks, where they got to, and the full tutor conversation for that
   lesson. It must work on a different device and after signing out and back
   in."

   ONLY FOR A CHILD SESSION (MrBadmusConfig.isChildSession — the session's
   own `@children.mrbadmus.internal` address, no network call), on a lesson
   page. Mide's brief is the ruling that a family or organisation child's
   lesson is put back on load; for every school pupil the MRB-291 /
   architecture §4.8.1 rule ("nothing ticked on load") stands, and this
   installs nothing — no request, no global, no listener.

   One read: GET /api/consumer/child/saved?path=<this page>, the child's own
   answers for this lesson (every attempt, oldest first) and their tutor
   exchanges on it. Then, once the page has wired itself:
     · the KS3 ladder puts its rungs back (shared/ks3.js, via `when`);
     · every other answerable block is replayed through the page's own
       controls or state (the `replay` functions the answer capture above
       registers), with the capture MUTED — nothing restored is ever sent
       again, so the ledger gets no duplicate rows;
     · the tutor panel gets the conversation (MrBadmus.restoreTalk).
   The scroll position and focus are put back afterwards: restoring never
   moves the page. If the read fails (offline, an expired token), nothing is
   replayed and the page keeps what it already shows from the device — the
   KS3 written rungs' own localStorage copy is the offline fallback.
   `state` is 'loading' until all of this has happened, then 'done', and
   `mrb:saved-applied` is dispatched on document (the KS4 "lesson done" signal
   waits for it, so a lesson finished on an EARLIER visit is not re-sent). */
try {
  (function () {
    var path = window.location.pathname || '';
    if (!/^\/(ks3|combined|triple)\//.test(path)) { return; }
    var c = window.MrBadmusConfig;
    if (!c || !c.BACKEND_URL || !c.AUTH_STORAGE_KEY || typeof c.isChildSession !== 'function') { return; }
    var session = null;
    try { session = JSON.parse(window.localStorage.getItem(c.AUTH_STORAGE_KEY) || 'null'); } catch (e) { return; }
    if (!session || !session.access_token || !c.isChildSession(session)) { return; }

    var waiting = [];
    var saved = window.MrBadmusSaved = {
      state: 'loading',
      data: null,                 // {answers, tutor} once read; null if the read failed
      // fn(data) once the saved work is in (data null when it could not be
      // read). Called at once when it already is.
      when: function (fn) {
        if (typeof fn !== 'function') { return; }
        if (saved.state === 'done' || saved.state === 'applying') { try { fn(saved.data); } catch (e) {} return; }
        waiting.push(fn);
      }
    };

    var read = new Promise(function (resolve) {
      var done = false;
      var finish = function (v) { if (!done) { done = true; resolve(v); } };
      setTimeout(function () { finish(null); }, 12000);          // never hold the page longer
      // A CURRENT token (MrBadmus.childAuth refreshes an expired one), and a
      // 401 is refreshed once and asked once more.
      var auth = window.MrBadmus && window.MrBadmus.childAuth;
      var ask = function (tok) {
        return fetch(c.BACKEND_URL + '/api/consumer/child/saved?path=' + encodeURIComponent(path), {
          headers: { 'Authorization': 'Bearer ' + tok, 'Accept': 'application/json' },
          cache: 'no-store'
        });
      };
      try {
        Promise.resolve(auth ? auth.token(c) : session.access_token)
          .then(function (tok) { return ask(tok || session.access_token); })
          .then(function (r) {
            if (r.status === 401 && auth) {
              return auth.refresh(c).then(function (t2) { return t2 ? ask(t2) : r; });
            }
            return r;
          })
          .then(function (r) { return r.ok ? r.json() : null; })
          .then(function (b) {
            finish(b && b.ok && Array.isArray(b.answers) ? { answers: b.answers, tutor: Array.isArray(b.tutor) ? b.tutor : [] } : null);
          }, function () { finish(null); });
      } catch (e) { finish(null); }
    });
    /* The page has wired itself once DOMContentLoaded's own listeners have run.
       ⊕ 8 Nov 2026: two races, both lost whenever the read beat the page. This
       file is `defer`, so it runs with readyState ALREADY 'interactive' but
       BEFORE the deferred scripts after it — a KS3 page's ks3.js wires its
       buttons as it executes — so only DOMContentLoaded (or `load`, if this
       file was ever added late) says they have all run; replaying sooner
       pressed buttons nothing was listening to. And a rebuilt KS4 lesson
       mounts with `libReady: false` and no blocks: its timer flips the flag
       some 40ms later and the NEXT draw creates them. schedule() runs its
       callback straight after that draw. Until then there is nothing to put
       an answer back into. */
    var wired = new Promise(function (resolve) {
      var fired = false;
      var go = function () { if (!fired) { fired = true; setTimeout(resolve, 0); } };
      if (document.readyState === 'complete') { go(); return; }
      document.addEventListener('DOMContentLoaded', go);
      window.addEventListener('load', go);
    }).then(function () {
      return new Promise(function (resolve) {
        var host = document.getElementById('ks4-mount');
        var api = host && host.__mrbKs4;
        var st = api && api.logic && api.logic.state;
        if (!st || !('libReady' in st) || typeof api.schedule !== 'function') { resolve(); return; }
        var t0 = Date.now();
        (function wait() {
          if (st.libReady === true) { api.schedule(resolve); return; }
          if (Date.now() - t0 > 8000) { resolve(); return; }     // never hold the page longer
          setTimeout(wait, 30);
        })();
      });
    });

    Promise.all([read, wired]).then(function (v) {
      var data = v[0];
      saved.data = data;
      saved.state = 'applying';
      var cap = window.MrBadmusAnswerCapture;
      var x = window.scrollX, y = window.scrollY, had = document.activeElement;
      if (cap && cap.mute) { cap.mute(true); }
      try {
        waiting.splice(0).forEach(function (fn) { try { fn(data); } catch (e) {} });
        if (cap && cap.beforeReplay) { cap.beforeReplay.forEach(function (fn) { try { fn(); } catch (e) {} }); }
        if (data && data.answers.length && cap && cap.replay) {
          cap.replay.forEach(function (fn) { try { fn(data.answers); } catch (e) {} });
        }
        // Last, and even when the read failed: only what the saved rows did not fill.
        if (cap && cap.afterReplay) { cap.afterReplay.forEach(function (fn) { try { fn(); } catch (e) {} }); }
        if (data && data.tutor.length && window.MrBadmus && typeof window.MrBadmus.restoreTalk === 'function') {
          window.MrBadmus.restoreTalk(data.tutor);
        }
      } catch (e) { /* restoring never breaks a lesson */ }
      // The rebuilt KS4 blocks redraw on the next frame and the KS3 capture
      // reads its verdicts a tick later: the mute is held past both.
      var raf = window.requestAnimationFrame || function (f) { return setTimeout(f, 16); };
      raf(function () {
        raf(function () {
          setTimeout(function () {
            if (cap && cap.mute) { cap.mute(false); }
            try {
              if (had && had !== document.activeElement && typeof had.focus === 'function' && had !== document.body) { had.focus({ preventScroll: true }); }
              else if (document.activeElement && document.activeElement !== had && document.activeElement.blur) { document.activeElement.blur(); }
            } catch (e) {}
            window.scrollTo(x, y);
            saved.state = 'done';
            try { document.dispatchEvent(new CustomEvent('mrb:saved-applied')); } catch (e) {}
          }, 60);
        });
      });
    });
  })();
} catch (e) {}
