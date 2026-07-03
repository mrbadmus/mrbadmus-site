/**
 * shared/shoutouts.js — Shoutout rendering + constants
 *
 * Used by:
 *   - teacher/class-detail.html (MRB-46 Phase 2) — composes, reads, soft-deletes
 *   - student/class.html        (MRB-46 Phase 3) — read-only
 *
 * Self-contained: brings its own escapeHtml / formatRelativeTime /
 * getStudentColour so callers don't have to provide them. Larger pages
 * keep their own copies of these helpers for other rendering — the
 * duplication cost (a few tiny functions) is preferable to a contract
 * where every caller has to inject helpers correctly.
 *
 * Page contract (load AFTER /shared/config.js, in any order vs guards/data):
 *   <script src="/shared/shoutouts.js"></script>
 *
 * Public API:
 *   MrBadmusShoutouts.SHOUTOUT_TEMPLATES
 *     The locked array of { key, emoji, label } — must match the DB
 *     class_shoutouts_template_key_chk enum exactly (six keys).
 *
 *   MrBadmusShoutouts.templateByKey(key)
 *     Returns the matching template object, or null.
 *
 *   MrBadmusShoutouts.renderShoutoutCard(shoutout, opts)
 *     shoutout = { id, template_key, message, created_at,
 *                  author_id, recipient_id,
 *                  author:    { first_name, last_name, display_name?, avatar_url } | null,
 *                  recipient: { first_name, last_name, avatar_url } | null }
 *     opts     = { showDelete: bool, currentUserId: uuid | null }
 *     Returns: HTML string for one shoutout card.
 *     The card carries data-shoutout-id (always) and data-is-own
 *     ("1"/"0") attributes so callers can wire interactions via
 *     querySelectorAll on the rendered DOM.
 *
 * The delete affordance HTML is included when both opts.showDelete is
 * true AND shoutout.author_id === opts.currentUserId. The caller is
 * responsible for wiring the click → confirm → soft-delete flow on the
 * `.shoutout-delete-btn` element (the caller knows its data layer; this
 * module stays presentation-only).
 *
 * CSS class names this module emits — caller's stylesheet must define
 * matching styles (teacher and student pages already do, sharing the
 * Phase 2 patterns):
 *   .shoutout-card, .shoutout-recipient-block, .shoutout-recipient-name,
 *   .shoutout-meta, .shoutout-body, .shoutout-template,
 *   .shoutout-template-emoji, .shoutout-message,
 *   .student-avatar (re-used from the existing roster pattern),
 *   .shoutout-delete-wrap, .shoutout-delete-btn (only emitted when
 *   showDelete + own).
 */
window.MrBadmusShoutouts = (function () {

  // ── Locked enum (mirrors the Phase 1 DB CHECK constraint) ───────
  // Order here is the display order in the compose form.
  const SHOUTOUT_TEMPLATES = [
    { key: 'top_of_class',             emoji: '🌟', label: 'Top of the class this week' },
    { key: 'brilliant_improvement',    emoji: '📈', label: 'Brilliant improvement' },
    { key: 'every_assignment_on_time', emoji: '⏰', label: 'Every assignment on time' },
    { key: 'smashed_tough_topic',      emoji: '🎯', label: 'Smashed a tough topic' },
    { key: 'bounced_back_strong',      emoji: '💪', label: 'Bounced back strong' },
    { key: 'helped_classmate',         emoji: '🤝', label: 'Helped a classmate' },
  ];

  function templateByKey(key) {
    if (!key) return null;
    for (let i = 0; i < SHOUTOUT_TEMPLATES.length; i++) {
      if (SHOUTOUT_TEMPLATES[i].key === key) return SHOUTOUT_TEMPLATES[i];
    }
    return null;
  }

  // ── Self-contained helpers ──────────────────────────────────────
  function escapeHtml(str) {
    return String(str == null ? '' : str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function formatRelativeTime(iso) {
    if (!iso) return '—';
    const then = new Date(iso).getTime();
    if (isNaN(then)) return '—';
    const sec = Math.floor((Date.now() - then) / 1000);
    if (sec < 60) return 'just now';
    const min = Math.floor(sec / 60);
    if (min < 60) return min + ' minute' + (min === 1 ? '' : 's') + ' ago';
    const hr = Math.floor(min / 60);
    if (hr < 24) return hr + ' hour' + (hr === 1 ? '' : 's') + ' ago';
    const day = Math.floor(hr / 24);
    if (day < 7) return day + ' day' + (day === 1 ? '' : 's') + ' ago';
    if (day < 30) {
      const wk = Math.floor(day / 7);
      return wk + ' week' + (wk === 1 ? '' : 's') + ' ago';
    }
    const d = new Date(iso);
    const sameYear = d.getFullYear() === new Date().getFullYear();
    return d.toLocaleDateString('en-GB', sameYear
      ? { day: 'numeric', month: 'short' }
      : { day: 'numeric', month: 'short', year: 'numeric' });
  }

  // Deterministic per-student colour. Same algorithm as the teacher/student
  // pages' inline copies, so the same student gets the same colour across
  // surfaces (roster avatar = shoutout card avatar = podium avatar).
  const AVATAR_COLOUR_VARS = [
    'var(--physics)', 'var(--chemistry)', 'var(--biology)', 'var(--science)',
  ];
  function getStudentColour(studentId) {
    const s = String(studentId || '');
    let h = 0;
    for (let i = 0; i < s.length; i++) h = (h + s.charCodeAt(i)) % AVATAR_COLOUR_VARS.length;
    return AVATAR_COLOUR_VARS[h];
  }

  // Build the recipient avatar HTML — initials+colour fallback for missing
  // avatar_url; if set, an img with onerror swap to the initials span.
  function buildAvatarHtml(recipient, recipientId) {
    const colour = getStudentColour(recipientId);
    const initial = ((recipient && recipient.first_name) || '').charAt(0).toUpperCase() || '?';
    const initialsHtml = '<span class="student-avatar" style="background:' + colour + ';">' +
      escapeHtml(initial) + '</span>';
    if (recipient && recipient.avatar_url) {
      return '<img class="student-avatar" src="' + escapeHtml(recipient.avatar_url) +
        '" alt="" referrerpolicy="no-referrer" data-fallback="' + escapeHtml(initialsHtml) +
        '" onerror="this.outerHTML=this.getAttribute(\'data-fallback\')"/>';
    }
    return initialsHtml;
  }

  // ── Public renderer ─────────────────────────────────────────────
  function renderShoutoutCard(shoutout, opts) {
    opts = opts || {};
    const showDelete = opts.showDelete === true;
    const currentUserId = opts.currentUserId || null;

    const recipient = shoutout.recipient || {};
    const author    = shoutout.author    || {};
    const recipientName = ((recipient.first_name || '') + ' ' + (recipient.last_name || '')).trim() || '—';
    // Decision F: viewers see the teacher's chosen display name ("Mr Badmus");
    // real name is only the fallback while no display name is set.
    const authorName    = (author.display_name && String(author.display_name).trim())
                       || ((author.first_name    || '') + ' ' + (author.last_name    || '')).trim() || '—';

    const avatarHtml = buildAvatarHtml(recipient, shoutout.recipient_id);

    const tpl = templateByKey(shoutout.template_key);
    let bodyHtml = '';
    if (tpl) {
      bodyHtml += '<div class="shoutout-template">' +
        '<span class="shoutout-template-emoji">' + tpl.emoji + '</span>' +
        '<span>' + escapeHtml(tpl.label) + '</span>' +
      '</div>';
    }
    if (shoutout.message) {
      bodyHtml += '<div class="shoutout-message">' + escapeHtml(shoutout.message) + '</div>';
    }

    const isOwn = !!(currentUserId && shoutout.author_id === currentUserId);
    const wireDelete = showDelete && isOwn;
    const deleteHtml = wireDelete
      ? '<div class="shoutout-delete-wrap">' +
          '<button class="shoutout-delete-btn" type="button" aria-label="Remove shoutout">×</button>' +
        '</div>'
      : '';

    return '<div class="shoutout-card" data-shoutout-id="' + escapeHtml(shoutout.id) +
        '" data-is-own="' + (isOwn ? '1' : '0') + '">' +
      '<div class="shoutout-recipient-block">' +
        avatarHtml +
        '<div>' +
          '<div class="shoutout-recipient-name">' + escapeHtml(recipientName) + '</div>' +
          '<div class="shoutout-meta">by ' + escapeHtml(authorName) + ' · ' +
            escapeHtml(formatRelativeTime(shoutout.created_at)) +
          '</div>' +
        '</div>' +
      '</div>' +
      '<div class="shoutout-body">' + bodyHtml + '</div>' +
      deleteHtml +
    '</div>';
  }

  return {
    SHOUTOUT_TEMPLATES: SHOUTOUT_TEMPLATES,
    templateByKey: templateByKey,
    renderShoutoutCard: renderShoutoutCard,
  };
})();
