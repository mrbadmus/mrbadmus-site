/**
 * mrbadmus.js — Shared AI chat engine
 * Works across Physics, Chemistry, Biology
 */
window.MrBadmus = (function() {
  let chatInited = false, pendingImg = null, chatHistory = [], currentSubject = 'physics', currentTopic = '', systemPrompt = '';

  const BASE_PROMPT = `You are Mr. Badmus AI — an expert AQA GCSE Science teacher covering Physics, Chemistry and Biology (AQA 8463 / 8462 / 8461). You are warm, encouraging, and deeply knowledgeable.

CORE TEACHING RULES — ALWAYS FOLLOW:
1. Use the FIFA method for ALL calculations without exception:
   F = Formula (write it out)
   I = Insert values (substitute numbers + units)
   F = Fix (show any conversions or rearrangements)
   A = Answer (include the unit — always)
2. Always say "potential difference" not "voltage" in physics contexts
3. Always include units in every final answer
4. Show all working — never skip steps
5. Be encouraging and warm — students may be struggling
6. When a concept is tricky, use a real-life analogy first
7. Always state the AQA spec point if relevant (e.g. "AQA 4.2.1.3")
8. For higher tier content, label it clearly: ⭐ HIGHER TIER
9. For triple science only content, label it: 🔬 TRIPLE ONLY
10. Keep responses SHORT and punchy — 3 to 6 lines max unless doing a full FIFA example
11. Never start with a long introduction — get straight to the point
12. If a student just says hello or greets you, respond with ONE friendly line only — e.g. "Hey! What are we working on today? 🔥"
13. Never list topics unprompted — only show a list if the student asks "what can you help with"
14. Format clearly with line breaks — never write a wall of text
15. If a student is confused, offer to break it down — but keep the offer to one sentence
16. CRITICAL — You are a FULL GCSE Science tutor covering ALL THREE sciences. You MUST answer questions about Biology, Chemistry AND Physics regardless of which subject page the student is on. NEVER say "I'm only the Physics tutor" or refuse to answer Chemistry or Biology questions. If a student on a Physics page asks about photosynthesis, answer it fully. Always help with any AQA GCSE Science topic.`;

  const SUBJECT_PROMPTS = {
    physics: `${BASE_PROMPT}

CURRENT PAGE CONTEXT: AQA GCSE Physics (8463) — but answer ALL science subjects if asked

FULL PHYSICS SPECIFICATION TOPICS:
4.1 Energy: KE=½mv², GPE=mgh, E=mcΔθ, E=½ke², efficiency, energy resources, conduction/convection/radiation. RP1 specific heat capacity, RP2 insulation.
4.2 Electricity: Q=It, V=IR, circuit symbols, ohmic/non-ohmic, series and parallel, AC/DC, mains wiring, P=VI, P=I²R, E=Pt, E=QV, National Grid, transformers. RP3 resistance of wire, RP4 I-V characteristics. Higher: potential dividers. Triple: static electricity, electric fields.
4.3 Particle Model: density ρ=m/V, states of matter, changes of state, internal energy, E=mcΔθ, E=mL (latent heat), gas pressure and temperature. Higher: Boyle's law, absolute zero. RP5 density.
4.4 Atomic Structure: protons/neutrons/electrons, isotopes, atomic model history, radioactive decay (alpha/beta/gamma), nuclear equations, half-life, background radiation, fission/fusion. RP6 half-life sim.
4.5 Forces: scalars/vectors, W=mg, resultant forces, W=Fs, F=ke (Hooke's Law), moments, p=F/A, pressure in fluids, s=vt, v=u+at, s=½(u+v)t, F=ma, Newton's laws, momentum p=mv, stopping distances. Higher: impulse=FΔt, terminal velocity. RP7 acceleration, RP8 spring extension.
4.6 Waves: v=fλ, T=1/f, transverse/longitudinal, EM spectrum, reflection, refraction, sound. Higher: n=sin(i)/sin(r). Triple: lenses, X-rays, radio waves. RP9 waves, RP10 light.
4.7 Magnetism: magnetic fields, electromagnets, Fleming's LHR, F=BIL, motors, induction, generators, Vp/Vs=Np/Ns, transformer efficiency. Higher: induced EMF. RP11 motor effect.
4.8 Space (TRIPLE ONLY): Solar System, stellar life cycles, orbital motion, red-shift, Big Bang, expanding universe.

REQUIRED PRACTICALS: RP1-RP11 as listed above.
KEY EQUATIONS: All equation sheet equations apply.`,

    chemistry: `${BASE_PROMPT}

CURRENT PAGE CONTEXT: AQA GCSE Chemistry (8462) — but answer ALL science subjects if asked

FULL CHEMISTRY SPECIFICATION TOPICS:
4.1 Atomic Structure & Periodic Table: protons/neutrons/electrons, Ar, Mr, isotopes, electronic structure, periodic table groups/periods, Group 1 (alkali metals), Group 7 (halogens), Group 0 (noble gases), transition metals.
4.2 Bonding: ionic (electron transfer, giant lattice), covalent (electron sharing, simple molecular vs giant), metallic (delocalised electrons), alloys, polymers. Higher: dot-cross diagrams. Triple: intermolecular forces.
4.3 Quantitative Chemistry: mol=mass÷Mr, mol=c×V, mol=V÷24, % yield=actual÷theoretical×100, atom economy=Mr(useful)÷Mr(all)×100, balancing equations. Higher: limiting reactants, titration calcs.
4.4 Chemical Changes: reactivity series, displacement, metal extraction, pH scale, neutralisation, acid+metal→salt+H₂, acid+base→salt+H₂O, acid+carbonate→salt+H₂O+CO₂, making salts, electrolysis (molten and solutions). Higher: half equations. RP1 making salts, RP2 electrolysis.
4.5 Energy Changes: exothermic/endothermic, reaction profiles, activation energy, bond energies (ΔH=bonds broken−bonds formed), cells, fuel cells. Higher: bond energy calcs. RP3 temperature changes.
4.6 Rate & Equilibrium: rate=quantity÷time, collision theory, factors (concentration, temp, surface area, catalyst), measuring rate, reversible reactions, Le Chatelier's principle, Haber process. Higher: equilibrium position calculations. RP4 thiosulfate, RP5 marble chips.
4.7 Organic Chemistry: crude oil, fractional distillation, alkanes (CₙH₂ₙ₊₂), cracking, alkenes (CₙH₂ₙ), addition reactions, polymerisation, alcohols, carboxylic acids, esters. Higher: mechanisms. Triple: amino acids, condensation polymers. 
4.8 Chemical Analysis: pure substances, chromatography (Rf=spot÷solvent), flame tests, testing gases, ion tests, mass spectrometry, IR spectroscopy. Higher: interpreting spectra. RP6 chromatography, RP7 ion tests.
4.9 Atmosphere: composition, evolution of atmosphere, greenhouse effect, climate change, carbon footprint, pollutants (CO, NOₓ, SO₂, particulates).
4.10 Using Resources: finite/renewable, water treatment, LCA, corrosion, alloys, ceramics, polymers, composites, Haber process (N₂+3H₂⇌2NH₃), NPK fertilisers. Higher: fertiliser calculations. RP8 water purification.`,

    biology: `${BASE_PROMPT}

CURRENT PAGE CONTEXT: AQA GCSE Biology (8461) — but answer ALL science subjects if asked

FULL BIOLOGY SPECIFICATION TOPICS:
4.1 Cell Biology: animal/plant/bacterial cells, eukaryotic/prokaryotic, specialised cells, magnification=image÷actual, diffusion/osmosis/active transport, mitosis, stem cells, growth. Higher: meiosis, stem cell ethics. RP1 microscopy, RP2 osmosis.
4.2 Organisation: cell→tissue→organ→system, digestive system, enzymes (lock-and-key, active site), effect of temp/pH on enzymes, heart, blood vessels (arteries/veins/capillaries), blood components, respiratory system, health and disease, cancer. Higher: CHD treatments, plant transport. RP3 enzyme pH, RP4 food tests.
4.3 Infection & Response: pathogens (bacteria/viruses/fungi/protists), spread of disease, specific diseases (measles, HIV, malaria, TMV, rose black spot, Salmonella), immune system (phagocytosis, antibodies, memory cells), vaccination, antibiotics, drug development. Higher: monoclonal antibodies, plant defences.
4.4 Bioenergetics: photosynthesis (6CO₂+6H₂O→C₆H₁₂O₆+6O₂), limiting factors (light, CO₂, temp), uses of glucose, aerobic respiration (C₆H₁₂O₆+6O₂→6CO₂+6H₂O), anaerobic (glucose→lactic acid; glucose→ethanol+CO₂), exercise response. Higher: rate graphs, metabolism. RP5 photosynthesis, RP6 fermentation.
4.5 Homeostasis & Response: homeostasis, nervous system (CNS, neurons, synapses), reflex arc, brain, eye, endocrine system, blood glucose (insulin/glucagon), diabetes Type 1&2, thermoregulation, kidneys/ADH, menstrual cycle (FSH/LH/oestrogen/progesterone), contraception, fertility treatments. Higher: negative feedback, IVF ethics. Triple: kidney detail. RP7 reaction time.
4.6 Inheritance: DNA structure, genes/alleles/chromosomes, dominant/recessive, Punnett squares, cystic fibrosis, polydactyly, sex determination, variation (genetic/environmental), mutation, natural selection, evolution evidence, classification. Higher: codominance, genetic engineering. Triple: protein synthesis.
4.7 Ecology: populations/communities/ecosystems, abiotic/biotic factors, interdependence, food webs, competition, adaptations, quadrats/transects, water/carbon/nitrogen cycles, biodiversity, deforestation, climate change, conservation, mark-recapture formula. Higher: biodiversity index, predator-prey. RP8 habitat sampling.`
  };

  const FALLBACKS = {
    physics: [
      { k: ['potential difference','pd','voltage'], r: '<strong>Potential Difference (p.d.) — AQA 4.2.1.3</strong><br><br>P.d. is the energy transferred per unit charge. It\'s the "push" that drives current around the circuit.<br><br><strong>FIFA Example</strong> (find p.d. across 4Ω with 3A):<br>F — V = I × R<br>I — V = 3 × 4<br>F — No conversion needed<br>A — V = <strong>12 V</strong><br><br>Measured with a voltmeter connected <strong>in parallel</strong>.' },
      { k: ['ohm','v=ir','resistance','calculate'], r: '<strong>Ohm\'s Law — V = IR (AQA 4.2.1.3)</strong><br><br>FIFA Example (find current, V=12V, R=4Ω):<br>F — I = V ÷ R<br>I — I = 12 ÷ 4<br>F — No conversion<br>A — I = <strong>3 A</strong>' },
      { k: ['series'], r: '<strong>Series Circuit (AQA 4.2.2)</strong><br>• Current: same everywhere<br>• P.D.: splits between components<br>• Resistance: R_total = R₁ + R₂ + ...' },
      { k: ['parallel'], r: '<strong>Parallel Circuit (AQA 4.2.2)</strong><br>• P.D.: same across every branch<br>• Current: splits — I = I₁ + I₂<br>• Resistance: less than smallest branch' },
    ],
    chemistry: [
      { k: ['mole','mol','mr','mass'], r: '<strong>Moles (AQA Chem)</strong><br>mol = mass ÷ Mr<br><br>FIFA (2 mol CO₂, Mr=44):<br>F — mass = mol × Mr<br>I — mass = 2 × 44<br>F — None<br>A — mass = <strong>88 g</strong>' },
      { k: ['atom','proton','electron','neutron'], r: '<strong>Atomic Structure</strong><br>• Protons: +1, in nucleus<br>• Neutrons: 0, in nucleus<br>• Electrons: −1, in shells<br>Atomic number = protons. Mass number = protons + neutrons.' },
    ],
    biology: [
      { k: ['cell','nucleus','mitochondria'], r: '<strong>Cell Types</strong><br>Animal: nucleus, cytoplasm, membrane, mitochondria, ribosomes<br>Plant: all above + cell wall, chloroplasts, vacuole<br>Bacterial: cell wall, membrane, cytoplasm, ribosomes, plasmid, DNA loop (no nucleus)' },
      { k: ['photosynthesis'], r: '<strong>Photosynthesis</strong><br>6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂<br>Limiting factors: light intensity, CO₂, temperature' },
    ]
  };

  function getFallback(q, subject) {
    const lq = q.toLowerCase();
    const items = FALLBACKS[subject] || FALLBACKS.physics;
    for (const item of items) {
      if (item.k.some(k => lq.includes(k))) return item.r;
    }
    return `Great question! 😊 Ask me about a specific topic and I\'ll help. For unlimited live AI answers, the teacher can add the API key in server settings.`;
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

  function formatReply(text) {
    return text.replace(/\*\*(.*?)\*\*/g,'<strong>$1</strong>').replace(/\*(.*?)\*/g,'<em>$1</em>').replace(/`(.*?)`/g,'<code>$1</code>').replace(/\n\n/g,'<br><br>').replace(/\n/g,'<br>');
  }

  const VOICE_ADDENDUM = `

VOICE MODE — YOU ARE SPEAKING OUT LOUD, NOT WRITING:
- Reply in 2 to 3 SHORT spoken sentences MAXIMUM. Never more.
- NO bullet points, NO numbered lists, NO asterisks, NO markdown, NO emojis.
- NO headers, NO bold, NO dashes used as lists.
- Write like you are talking directly to the student face to face.
- Use natural spoken language: say "for example" not "e.g.", say "which means" not an arrow symbol.
- For calculations, talk through steps verbally: "First write the formula, then substitute the values..."
- End with ONE short follow-up question to keep the conversation going.
- Keep it warm, punchy and human. You are a teacher talking, not writing a textbook.`;

  let _voiceSystemPrompt = '';

  function init(config) {
    currentSubject = config.subject || 'physics';
    currentTopic = config.topic || '';
    systemPrompt = SUBJECT_PROMPTS[currentSubject] || SUBJECT_PROMPTS.physics;
    if (currentTopic) systemPrompt += `\n\nThe student is currently studying: ${currentTopic}. Focus on this topic when possible.`;
    _voiceSystemPrompt = systemPrompt + VOICE_ADDENDUM;

    document.getElementById('chatOverlay')?.addEventListener('click', e => { if(e.target===document.getElementById('chatOverlay')) close(); });
    document.querySelector('.close-btn')?.addEventListener('click', close);
    document.querySelector('.chat-send-btn')?.addEventListener('click', () => ask());
    document.getElementById('ci')?.addEventListener('keydown', e => { if(e.key==='Enter') ask(); });
    document.getElementById('imgInput')?.addEventListener('change', () => handleImg(document.getElementById('imgInput')));
    document.querySelectorAll('.quick-q').forEach(btn => btn.addEventListener('click', () => ask(btn.dataset.q)));
    document.querySelectorAll('[data-open-chat]').forEach(el => el.addEventListener('click', open));
  }

  function open() {
    document.getElementById('chatOverlay')?.classList.add('open');
    if (!chatInited) {
      chatInited = true;
      const sn = {physics:'Physics ⚡',chemistry:'Chemistry 🧪',biology:'Biology 🌿'}[currentSubject];
      addMsg('bot', `Hey! 👋 I\'m Mr Badmus — here to help you smash your GCSE Science. What are we stuck on?`);
    }
    setTimeout(() => document.getElementById('ci')?.focus(), 100);
  }

  function close() { document.getElementById('chatOverlay')?.classList.remove('open'); }

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
    addMsg('user', (q||'Please answer this question:') + (hasImg ? `<br><img src="${pendingImg}" style="max-width:100%;border-radius:6px;margin-top:6px;display:block;" alt="question"/>` : ''));
    const imgData = pendingImg; clearImg();
    const t = addMsg('bot', '<div class="typing"><span></span><span></span><span></span></div>');
    let userContent = hasImg ? [{ type:'image', source:{ type:'base64', media_type:imgData.split(';')[0].split(':')[1], data:imgData.split(',')[1] }}, { type:'text', text:q||'Answer this GCSE Science question fully using FIFA for any calculations.' }] : q;
    chatHistory.push({ role:'user', content:userContent });
    try {
      const res = await fetch('/api/chat', { method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({ system:(window._mrBadmusVoiceMode ? _voiceSystemPrompt : systemPrompt), messages:chatHistory }) });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      if (data.error) throw new Error(data.error.message);
      const reply = data.content?.map(c=>c.text||'').filter(Boolean).join('') || 'Sorry, no response.';
      if (t) t.querySelector('.chat-msg__bubble').innerHTML = formatReply(reply);
      chatHistory.push({ role:'assistant', content:reply });
      if (chatHistory.length > 20) chatHistory.splice(0,2);
    } catch(err) {
      chatHistory.pop();
      if (t) t.querySelector('.chat-msg__bubble').innerHTML = hasImg ? '⚠️ Image analysis needs a live connection. Type your question instead!' : getFallback(q, currentSubject);
    }
    document.getElementById('chatMsgs').scrollTop = 99999;
  }

  return { init, open, close, ask };
})();


// ══════════════════════════════════════════════════════
//  MR BADMUS VOICE MODE
//  Student speaks → AI replies → Mr Badmus speaks back
// ══════════════════════════════════════════════════════

(function() {
  var MB = window.MrBadmus;

  var _ttsEnabled  = false;
  var _voiceMode   = false;
  var _recognition = null;
  var _isSpeaking  = false;
  var _isThinking  = false;
  var _isListening = false;

  function _orb()        { return document.getElementById('voiceOrb'); }
  function _label()      { return document.getElementById('voiceStateLabel'); }
  function _transcript() { return document.getElementById('voiceTranscript'); }
  function _banner()     { return document.getElementById('voiceBanner'); }
  function _msgs()       { return document.getElementById('chatMsgs'); }
  function _subtitle()   { return document.getElementById('chatSubtitle'); }

  function _setOrbState(state, emoji, labelText) {
    var orb = _orb(); var lbl = _label();
    if (!orb) return;
    orb.className = 'voice-orb voice-orb--' + state;
    orb.textContent = emoji;
    orb.onclick = (state === 'idle') ? function(){ MB.startListening(); } : null;
    if (lbl) lbl.textContent = labelText;
  }

  function _speak(text, onEnd) {
    if (!window.speechSynthesis) { if (onEnd) onEnd(); return; }
    window.speechSynthesis.cancel();
    var clean = text
      .replace(/\*\*(.*?)\*\*/g, '$1')
      .replace(/\*(.*?)\*/g, '$1')
      .replace(/`([^`]*)`/g, '$1')
      .replace(/#{1,6} /g, '')
      .replace(/^[-*+] /gm, '')
      .replace(/e\.g\./gi, 'for example')
      .replace(/i\.e\./gi, 'that is')
      .replace(/\n+/g, ' ')
      .replace(/  +/g, ' ')
      .trim()
      .substring(0, 1000);
    var utt = new SpeechSynthesisUtterance(clean);
    utt.rate = 0.92; utt.pitch = 1.0; utt.lang = 'en-GB';
    function _trySpeak() {
      var voices = window.speechSynthesis.getVoices();
      var v = voices.find(function(v){ return v.name === 'Daniel'; })
           || voices.find(function(v){ return v.lang === 'en-GB'; })
           || voices.find(function(v){ return v.lang.startsWith('en'); });
      if (v) utt.voice = v;
      utt.onend  = function() { _isSpeaking = false; if (onEnd) onEnd(); };
      utt.onerror = function() { _isSpeaking = false; if (onEnd) onEnd(); };
      _isSpeaking = true;
      window.speechSynthesis.speak(utt);
    }
    if (window.speechSynthesis.getVoices().length === 0) {
      window.speechSynthesis.onvoiceschanged = _trySpeak;
    } else { _trySpeak(); }
  }

  MB.toggleTTS = function() {
    _ttsEnabled = !_ttsEnabled;
    var btn = document.getElementById('ttsToggle');
    if (btn) {
      btn.textContent = _ttsEnabled ? '🔊 ON' : '🔊 TTS';
      btn.style.background  = _ttsEnabled ? 'rgba(78,205,196,0.3)' : 'rgba(255,255,255,0.1)';
      btn.style.borderColor = _ttsEnabled ? '#4ECDC4' : 'rgba(255,255,255,0.2)';
    }
    if (!_ttsEnabled && window.speechSynthesis) window.speechSynthesis.cancel();
  };

  MB.enterVoiceMode = function() {
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
      alert('Voice mode needs Chrome or Edge. Safari on iPhone also works.');
      return;
    }
    _voiceMode = true; _ttsEnabled = true; window._mrBadmusVoiceMode = true;
    var banner = _banner(); var msgs = _msgs();
    if (banner) banner.style.display = 'flex';
    if (msgs)   msgs.style.display   = 'none';
    var sub = _subtitle(); if (sub) sub.textContent = '🎤 Voice mode';
    var ttsBtn = document.getElementById('ttsToggle');
    if (ttsBtn) { ttsBtn.textContent = '🔊 ON'; ttsBtn.style.background = 'rgba(78,205,196,0.3)'; ttsBtn.style.borderColor = '#4ECDC4'; }
    _setOrbState('idle', '🎤', 'Tap to speak');
    if (!window._voiceWelcomeDone) {
      window._voiceWelcomeDone = true;
      _setOrbState('speaking', '🔊', 'Mr Badmus is speaking...');
      _speak('Voice mode is on. Tap the mic and ask me anything.', function() {
        _setOrbState('idle', '🎤', 'Tap to speak');
      });
    }
  };

  MB.exitVoiceMode = function() {
    _voiceMode = false; window._mrBadmusVoiceMode = false;
    if (_recognition) { try { _recognition.stop(); } catch(e){} }
    if (window.speechSynthesis) window.speechSynthesis.cancel();
    _isSpeaking = false; _isListening = false;
    var banner = _banner(); var msgs = _msgs();
    if (banner) banner.style.display = 'none';
    if (msgs)   msgs.style.display   = '';
    var sub = _subtitle(); if (sub) sub.textContent = 'GCSE Science Tutor';
  };

  MB.startListening = function() {
    if (_isListening || _isThinking || _isSpeaking) return;
    var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SR) { alert('Voice not supported in this browser.'); return; }
    _recognition = new SR();
    _recognition.lang = 'en-GB';
    _recognition.interimResults = true;
    _recognition.onstart = function() {
      _isListening = true;
      _setOrbState('listening', '🔴', 'Listening...');
      var tr = _transcript(); if (tr) tr.textContent = '';
    };
    _recognition.onresult = function(e) {
      var interim = '', final_t = '';
      for (var i = e.resultIndex; i < e.results.length; i++) {
        if (e.results[i].isFinal) final_t += e.results[i][0].transcript;
        else interim += e.results[i][0].transcript;
      }
      var tr = _transcript(); if (tr) tr.textContent = final_t || interim;
    };
    _recognition.onerror = function(e) {
      _isListening = false;
      _setOrbState('idle', '🎤', e.error === 'no-speech' ? 'Tap to speak' : 'Error: ' + e.error);
    };
    _recognition.onend = function() {
      _isListening = false;
      var tr = _transcript();
      var text = tr ? tr.textContent.trim() : '';
      if (!text || !_voiceMode) { if (_voiceMode) _setOrbState('idle', '🎤', 'Tap to speak'); return; }
      _setOrbState('thinking', '💭', 'Mr Badmus is thinking...');
      _isThinking = true;
      if (tr) tr.textContent = '“' + text + '”';
      var p = MB.ask(text);
      if (!p || typeof p.then !== 'function') p = Promise.resolve();
      p.then(function() {
        _isThinking = false;
        setTimeout(function() {
          var bubbles = document.querySelectorAll('.chat-msg--bot .chat-msg__bubble');
          var reply = bubbles.length ? bubbles[bubbles.length - 1].innerText : '';
          if (reply) {
            _setOrbState('speaking', '🔊', 'Mr Badmus is speaking...');
            _speak(reply, function() { setTimeout(function() { _setOrbState('idle', '🎤', 'Tap to speak'); }, 400); });
          } else {
            _setOrbState('idle', '🎤', 'Tap to speak');
          }
        }, 300);
      }).catch(function() {
        _isThinking = false; _setOrbState('idle', '🎤', 'Something went wrong — tap to retry');
      });
    };
    _recognition.start();
  };

  document.addEventListener('DOMContentLoaded', function() {
    var orb = _orb();
    if (!orb) return;
    orb.addEventListener('click', function() {
      if (_isListening) { if (_recognition) _recognition.stop(); }
      else if (_isSpeaking) { if (window.speechSynthesis) window.speechSynthesis.cancel(); _isSpeaking = false; setTimeout(function(){ if (_voiceMode) MB.startListening(); }, 200); }
      else if (!_isThinking) { MB.startListening(); }
    });
  });

  var _origAsk = MB.ask;
  MB.ask = function(preset) {
    var p = _origAsk(preset);
    if (!p || typeof p.then !== 'function') return Promise.resolve();
    if (_ttsEnabled && !_voiceMode) {
      p.then(function() {
        setTimeout(function() {
          var bubbles = document.querySelectorAll('.chat-msg--bot .chat-msg__bubble');
          if (bubbles.length) _speak(bubbles[bubbles.length - 1].innerText, null);
        }, 150);
      });
    }
    return p;
  };

  MB.toggleVoice = MB.enterVoiceMode;

})();
