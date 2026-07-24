/**
 * shared/username-generator.js — MrBadmusAI public usernames (MRB-138)
 * ---------------------------------------------------------------------------
 * One source of truth for:
 *   • generating friendly handles (adjective + noun + optional 2-digit number)
 *   • validating handle FORMAT
 *   • MODERATION (profanity/slurs incl. leetspeak evasion, impersonation, PII)
 *
 * SAFEGUARDING NOTE: minors use this product. The moderation here is the
 * CLIENT-side gate (fast feedback). It is deliberately mirrored by a server-side
 * gate in Postgres (see supabase/migrations/*_usernames.sql →
 * public.username_rejection_reason) — a client-only filter is trivially bypassed.
 * Keep the two lists in sync when either changes.
 *
 * Storage model: the display-cased handle (e.g. "FrostPixel42") is stored in a
 * citext column, so uniqueness is case-insensitive ("frostpixel42" == "FrostPixel42")
 * while the pretty capitalisation survives for display. `displayName` shows it as-is.
 *
 * Exposes window.MrBadmusUsername in the browser and module.exports under Node
 * (so the 500-sample audit script can require it).
 */
(function (root) {
  'use strict';

  // ── Word pools ─────────────────────────────────────────────────────────
  // Four registers deliberately mixed so no student feels branded. Nothing
  // sciencey or school-flavoured. Every word must read fine next to every noun.
  var ADJECTIVES = [
    // cool / elemental
    'frost', 'void', 'crimson', 'shadow', 'ember', 'storm', 'onyx', 'blaze',
    // aesthetic / soft
    'lunar', 'velvet', 'mint', 'pearl', 'dusk', 'coral', 'amber', 'silk',
    // nature / animal
    'falcon', 'otter', 'comet', 'fox', 'raven', 'tiger', 'wolf', 'koi',
    // playful
    'mango', 'waffle', 'pixel', 'noodle', 'bolt', 'jelly', 'turbo', 'cosmo'
  ];

  var NOUNS = [
    'pixel', 'pulse', 'rift', 'byte', 'wave', 'spark', 'drift', 'quest',
    'dash', 'echo', 'orbit', 'glide', 'flare', 'ripple', 'nova', 'prism',
    'beam', 'trail', 'loop', 'harbor', 'meadow', 'summit', 'river', 'cove'
  ];

  // ── Moderation lists (matched against the NORMALISED candidate) ─────────
  // Normalisation maps leetspeak + strips separators, so "sh1t", "s h i t",
  // "s-h-i-t" all collapse to "shit" before matching.
  //
  // Two tiers, to catch evasions WITHOUT the "Scunthorpe problem" (blocking
  // innocent words that merely contain a short rude fragment):
  //   • BANNED_SUBSTR — unambiguous strings that never appear inside ordinary
  //     words. Matched anywhere in the handle (so "xxfuckxx" is caught).
  //   • BANNED_EXACT  — short/ambiguous words matched ONLY as the whole handle,
  //     so "Essex", "Titan", "Methane", "Grape", "Uranus", "SkillWave",
  //     "SparseData", "CompassX" are all fine while a bare "ass"/"sex" is not.
  var BANNED_SUBSTR = [
    // profanity — none are substrings of common innocent words
    'fuck', 'shit', 'bitch', 'bastard', 'cunt', 'wank', 'wanker', 'bollock',
    'bugger', 'asshole', 'arsehole', 'twat', 'slut', 'whore', 'douche', 'dildo',
    'boob', 'penis', 'vagina', 'jizz', 'orgasm', 'porn', 'blowjob', 'handjob',
    'dumbass', 'jackass', 'bullshit', 'dipshit', 'shithead', 'motherfuck',
    'cocksuck', 'dickhead', 'knobhead', 'bellend', 'minge', 'tosser', 'piss',
    'sexy', 'sexual', 'cameltoe',
    // slurs / hate (kept for filtering only)
    'nigger', 'nigga', 'faggot', 'fagot', 'retard', 'spastic', 'gook', 'kike',
    'wetback', 'tranny', 'rapist', 'raping', 'molest', 'pedo', 'paedo',
    'hitler', 'nazi', 'kkk',
    // drugs
    'cocaine', 'heroin', 'ganja', 'methhead'
  ];
  // Exact-only: short/ambiguous OR substrings of wholesome, kid-relevant words
  // (peacock, dickinson, pussycat, raccoon, tycoon, pakistan, scunthorpe-avoided,
  // isis-goddess, slag=metallurgy). Blocks the standalone word, spares the host.
  var BANNED_EXACT = [
    'ass', 'arse', 'hell', 'damn', 'crap', 'hoe', 'tit', 'tits', 'nut', 'nuts',
    'pee', 'poo', 'poop', 'anal', 'anus', 'butt', 'cum', 'sex', 'fart', 'turd',
    'meth', 'crack', 'weed', 'kill', 'killer', 'rape', 'raped', 'rapes',
    'murder', 'suicide', 'xxx', 'milf', 'thot', 'std',
    'cock', 'dick', 'prick', 'pussy', 'coon', 'paki', 'pakis', 'chink', 'chinky',
    'dyke', 'isis', 'slag', 'fanny', 'knob', 'shag', 'gash'
  ];

  // Impersonation of the site / staff / a configured school. School name is
  // injected at runtime via configureSchoolName(). 'rainford' is a known school.
  // 'mod' is exact-only so it doesn't block "Model", "Module", "Modern".
  var IMPERSONATION_SUBSTR = [
    'mrbadmus', 'badmus', 'admin', 'administrator', 'moderator',
    'staff', 'teacher', 'official', 'helpdesk', 'mrbadmusai', 'rainford'
  ];
  var IMPERSONATION_EXACT = ['mod', 'support', 'system'];
  var extraBlockedNames = []; // populated by configureSchoolName()

  var MIN_LEN = 3, MAX_LEN = 20;

  // ── Normalisation (evasion-resistant) ──────────────────────────────────
  function normalizeForMatch(s) {
    return String(s == null ? '' : s)
      .toLowerCase()
      .replace(/0/g, 'o').replace(/1/g, 'i').replace(/3/g, 'e')
      .replace(/4/g, 'a').replace(/5/g, 's').replace(/7/g, 't')
      .replace(/[^a-z]/g, ''); // strip spaces, separators, remaining digits
  }

  function matchSubstr(norm, list) {
    for (var i = 0; i < list.length; i++) {
      if (list[i] && norm.indexOf(list[i]) !== -1) return list[i];
    }
    return null;
  }
  function matchExact(norm, list) {
    for (var i = 0; i < list.length; i++) {
      if (norm === list[i]) return list[i];
    }
    return null;
  }
  function containsBanned(norm) {
    return matchSubstr(norm, BANNED_SUBSTR) || matchExact(norm, BANNED_EXACT);
  }
  function containsImpersonation(norm) {
    return matchSubstr(norm, IMPERSONATION_SUBSTR.concat(extraBlockedNames)) ||
           matchExact(norm, IMPERSONATION_EXACT);
  }

  // ── FORMAT check ────────────────────────────────────────────────────────
  // Stored form: starts with a letter, then letters/digits, 3–20 chars.
  function formatReason(raw) {
    var s = String(raw == null ? '' : raw).trim();
    if (!s) return 'Please enter a username.';
    if (/\s/.test(s)) return 'No spaces — try joining the words (e.g. FrostPixel).';
    if (/[^A-Za-z0-9]/.test(s)) return 'Letters and numbers only — no symbols.';
    if (!/^[A-Za-z]/.test(s)) return 'Start with a letter.';
    if (s.length < MIN_LEN) return 'Too short — use at least ' + MIN_LEN + ' characters.';
    if (s.length > MAX_LEN) return 'Too long — keep it to ' + MAX_LEN + ' characters or fewer.';
    return null;
  }

  // ── Full moderation → plain-English reason, or null if OK ────────────────
  function rejectionReason(raw) {
    var s = String(raw == null ? '' : raw).trim();

    // PII patterns run on the RAW input (before normalisation).
    if (s.indexOf('@') !== -1) return "That looks like an email — pick a nickname instead.";
    if (/(\d[\s-]?){7,}/.test(s)) return "That looks like a phone number — pick a nickname instead.";
    // Two capitalised words with a separator read as a real full name.
    if (/^[A-Z][a-z]+[\s._-]+[A-Z][a-z]+/.test(s)) {
      return "Please use a nickname, not your real name.";
    }

    var fmt = formatReason(s);
    if (fmt) return fmt;

    var norm = normalizeForMatch(s);
    if (norm.length < 2) return 'Please choose a longer nickname.';

    if (containsBanned(norm)) return "That username isn't allowed — please pick something friendlier.";
    if (containsImpersonation(norm)) return "That name is reserved — please choose a different one.";

    return null;
  }

  function isValid(raw) { return rejectionReason(raw) === null; }

  // ── Generation ──────────────────────────────────────────────────────────
  function pick(arr) { return arr[Math.floor(Math.random() * arr.length)]; }
  function cap(w) { return w.charAt(0).toUpperCase() + w.slice(1); }

  // Returns a display-cased handle (e.g. "FrostPixel42"). Guaranteed clean:
  // never pairs a word with itself, always <= MAX_LEN, always passes moderation.
  function generate(opts) {
    opts = opts || {};
    var withNumber = opts.number == null ? (Math.random() < 0.55) : !!opts.number;
    for (var attempt = 0; attempt < 40; attempt++) {
      var adj = pick(ADJECTIVES);
      var noun = pick(NOUNS);
      if (adj === noun) continue; // e.g. pixel + pixel
      var base = cap(adj) + cap(noun);
      var handle = base;
      if (withNumber) {
        var n = 10 + Math.floor(Math.random() * 90); // 10–99
        if ((base + n).length <= MAX_LEN) handle = base + n;
      }
      if (handle.length > MAX_LEN) continue;
      if (handle.length < MIN_LEN) continue;
      if (isValid(handle)) return handle;
    }
    return 'StarPixel' + (10 + Math.floor(Math.random() * 90)); // safe fallback
  }

  function configureSchoolName(name) {
    var norm = normalizeForMatch(name);
    if (norm && norm.length >= 3 && extraBlockedNames.indexOf(norm) === -1) {
      extraBlockedNames.push(norm);
    }
  }

  var api = {
    ADJECTIVES: ADJECTIVES,
    NOUNS: NOUNS,
    BANNED_SUBSTR: BANNED_SUBSTR,
    BANNED_EXACT: BANNED_EXACT,
    IMPERSONATION_SUBSTR: IMPERSONATION_SUBSTR,
    IMPERSONATION_EXACT: IMPERSONATION_EXACT,
    MIN_LEN: MIN_LEN,
    MAX_LEN: MAX_LEN,
    generate: generate,
    normalizeForMatch: normalizeForMatch,
    formatReason: formatReason,
    rejectionReason: rejectionReason,
    isValid: isValid,
    configureSchoolName: configureSchoolName
  };

  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.MrBadmusUsername = api;
})(typeof window !== 'undefined' ? window : this);
