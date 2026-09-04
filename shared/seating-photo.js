/**
 * shared/seating-photo.js — MRB-322 photo assist, browser half
 *
 * A teacher points their phone or iPad at an empty classroom; this turns that
 * photo into a STARTING layout on the canvas, which they then drag into shape.
 * It is not a measurement, it is a first draft, and the page copy says so.
 *
 * Page contract (load AFTER config.js and teacher-guard.js):
 *   <script src="/shared/seating-photo.js"></script>
 *
 * ── What this file does before the image leaves the device ───────────
 * It re-encodes the picture to a JPEG no larger than 1568px on the long edge.
 * That matters for three separate reasons:
 *
 *   1. 1568px is the size the vision model works at anyway, so anything bigger
 *      is bandwidth a teacher on school wifi pays for and the model discards.
 *   2. A modern phone photo is 4-12MB; the endpoint caps at 10MB. Re-encoding
 *      means the cap is never reached in practice rather than being a cliff a
 *      teacher falls off with no idea why.
 *   3. Re-encoding through a canvas DROPS the EXIF block, and EXIF on a phone
 *      photo carries GPS coordinates. The school's location is not something
 *      this feature needs, so it should not be something this feature sends.
 *      That is a side effect of the resize, but it is the reason the resize is
 *      not optional even for a small file.
 *
 * ⚠️ HEIC. iPhones shoot HEIC by default. Safari can decode it into an <img>
 * and therefore through this canvas; Chrome cannot, and there is no way to
 * convert it in the browser without shipping a decoder. So a HEIC on Chrome
 * fails at `img.onerror` and gets an honest sentence telling the teacher to
 * re-save as JPEG — rather than a silent failure or a 415 from the server that
 * reads like the feature is broken.
 */

window.MrBadmusSeatingPhoto = (function () {
  'use strict';

  const MAX_EDGE = 1568;
  const JPEG_QUALITY = 0.82;

  function backendUrl() {
    const cfg = window.MrBadmusConfig;
    if (!cfg || !cfg.BACKEND_URL) {
      throw new Error('[seating-photo] window.MrBadmusConfig missing');
    }
    return cfg.BACKEND_URL;
  }

  /**
   * Decode, downscale and re-encode to a JPEG Blob.
   * Rejects with code 'undecodable' when the browser cannot read the format.
   */
  function toJpeg(file) {
    return new Promise(function (resolve, reject) {
      const url = URL.createObjectURL(file);
      const img = new Image();

      img.onload = function () {
        URL.revokeObjectURL(url);
        const w = img.naturalWidth, h = img.naturalHeight;
        if (!w || !h) {
          const e = new Error('empty image');
          e.code = 'undecodable';
          return reject(e);
        }
        const scale = Math.min(1, MAX_EDGE / Math.max(w, h));
        const cw = Math.max(1, Math.round(w * scale));
        const ch = Math.max(1, Math.round(h * scale));

        const canvas = document.createElement('canvas');
        canvas.width = cw;
        canvas.height = ch;
        const ctx = canvas.getContext('2d');
        // A photographed room is mostly flat surfaces and straight edges;
        // high-quality smoothing keeps desk edges readable at this scale.
        ctx.imageSmoothingEnabled = true;
        ctx.imageSmoothingQuality = 'high';
        ctx.drawImage(img, 0, 0, cw, ch);

        canvas.toBlob(function (blob) {
          if (!blob) {
            const e = new Error('re-encode failed');
            e.code = 'undecodable';
            return reject(e);
          }
          resolve(blob);
        }, 'image/jpeg', JPEG_QUALITY);
      };

      img.onerror = function () {
        URL.revokeObjectURL(url);
        const e = new Error('browser cannot decode this image');
        e.code = 'undecodable';
        reject(e);
      };

      img.src = url;
    });
  }

  async function accessToken() {
    const guard = window.MrBadmusTeacherGuard;
    const sb = guard && guard.getClient ? guard.getClient() : null;
    if (!sb) throw new Error('[seating-photo] Supabase client unavailable');
    const { data } = await sb.auth.getSession();
    const token = data && data.session ? data.session.access_token : null;
    if (!token) {
      const e = new Error('not signed in');
      e.code = 'not_signed_in';
      throw e;
    }
    return token;
  }

  /**
   * Scan a room photo.
   *
   * Resolves to one of three shapes, and the caller must branch on all three:
   *   { ok: true,  layout, confidence }
   *   { ok: false, unconfigured: true, message }   ← no API key on the server
   *   { ok: false, message }                       ← refusal or honest failure
   *
   * It never throws for an expected outcome. A rejected promise means something
   * genuinely unexpected happened (no session, no config).
   */
  async function scan(file) {
    let blob;
    try {
      blob = await toJpeg(file);
    } catch (err) {
      if (err.code === 'undecodable') {
        return { ok: false, message:
          'This browser could not read that image. iPhone photos are often ' +
          'HEIC — save it as a JPEG and try again.' };
      }
      throw err;
    }

    const token = await accessToken();

    // The server takes 60s for the model; give the browser a little more so a
    // slow round trip surfaces as the server's honest 504 rather than as this
    // side giving up first and blaming the network.
    const controller = new AbortController();
    const timer = setTimeout(function () { controller.abort(); }, 70000);

    let res;
    try {
      res = await fetch(backendUrl() + '/api/room-scan', {
        method: 'POST',
        headers: {
          'Content-Type': 'image/jpeg',
          'Authorization': 'Bearer ' + token,
        },
        body: blob,
        signal: controller.signal,
      });
    } catch (err) {
      clearTimeout(timer);
      if (err.name === 'AbortError') {
        return { ok: false, message:
          'The scan took too long and was stopped. Try again, or build the ' +
          'room from a template instead.' };
      }
      return { ok: false, message:
        'Could not reach the scanning service. Check your connection, or ' +
        'build the room from a template instead.' };
    }
    clearTimeout(timer);

    let body = null;
    try { body = await res.json(); } catch (err) { body = null; }

    if (res.status === 503 && body && body.error === 'photo_scan_unconfigured') {
      return { ok: false, unconfigured: true,
               message: body.message || "Photo scan isn't switched on yet." };
    }

    if (!res.ok) {
      return { ok: false, message: (body && body.message) ||
        'The scan failed. You can still build the room from a template.' };
    }

    if (body && body.refusal) {
      return { ok: false, refusal: body.refusal,
               message: body.message || 'That photo could not be used.' };
    }

    if (!body || !body.layout) {
      return { ok: false, message:
        'The scan came back empty. You can still build the room from a template.' };
    }

    // Second gate. The server validated its own model output; the canvas
    // validates again here because this is the last point before untrusted
    // geometry is drawn, and the two checks are written from different sides.
    const checked = window.SeatingCanvas.validate(body.layout);
    if (!checked.ok) {
      console.warn('[seating-photo] scan rejected by canvas validation',
                   checked.errors);
      return { ok: false, message:
        'The scan came back in a shape the canvas could not read. You can ' +
        'still build the room from a template.' };
    }

    return { ok: true, layout: checked.layout,
             confidence: typeof body.confidence === 'number' ? body.confidence : null };
  }

  return { scan: scan, toJpeg: toJpeg, MAX_EDGE: MAX_EDGE };
})();
