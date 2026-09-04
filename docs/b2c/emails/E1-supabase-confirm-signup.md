# E1 — "Confirm signup" (paste into Supabase)

Design's E1, from `docs/b2c/design/drop1/B2C consumer front door design/Emails.dc.html`.

**This one email is NOT a backend template and never will be.** Every other
consumer email is rendered by `consumer/email.js` and sent through Resend. E1
is sent by **GoTrue**, before a profile exists, before `/api/consumer/family/ensure`
has ever been called, and with a confirmation link only GoTrue can mint. So it
lives in the Supabase dashboard and nowhere else, and this file is the copy of
record for it.

**Where it goes:** Supabase dashboard → *Authentication* → *Emails* →
**Confirm signup** (both the TEST project `qeppkiswvclkkwbxmlok` and, at
launch, production `urklkrwevjtlfbwnipjn`).

The one template variable available and used is `{{ .ConfirmationURL }}`.

---

## The copy

| field | text |
|---|---|
| **Subject** | `Confirm your email to finish setting up` |
| **Preview text** | `One tap, then your first week is set tonight.` |
| **Heading** | `One tap and you're in.` |
| **Lede** | `Confirm this is your address and the account is yours. The link works for 24 hours.` |
| **CTA** | `Confirm my email` → `{{ .ConfirmationURL }}` |
| **Note under the CTA** | `If you didn't sign up, ignore this and nothing happens.` |
| **Signoff** | `Mide Badmus` |
| **Footer** | `Mr Badmus Education Ltd, England. You are getting this because you have a MrBadmus account for your family.` |
| **Unsubscribe line** | `This one is required — there is nothing to unsubscribe from.` |

### ⊕ One deviation from Design, and why

Design's preview line reads *"One tap, then Amara's first week is set
tonight."* At E1 there is **no child**: the parent has typed an email address
and a password and nothing else, and the add-a-child step is three screens
away. Supabase's confirm-signup template has access to `{{ .ConfirmationURL }}`,
`{{ .Email }}`, `{{ .SiteURL }}` and `{{ .Token }}` — no name of any kind. So
the preview is the same sentence with the child's name taken out. Nothing else
changed.

The footer's second line also differs from every other email: the rest carry
an "Email settings / unsubscribe" link, and Design marks E1's as
*"nothing — this one is required"*. A confirmation email is not marketing and
has no unsubscribe, so it says so instead of linking to a preferences page the
recipient cannot reach yet (they have no session).

---

## Paste this into "Message body" (HTML)

```html
<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Confirm your email to finish setting up</title></head>
<body style="margin:0;padding:0;background:#F4EFE6;">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;">One tap, then your first week is set tonight.</div>
<table role="presentation" cellpadding="0" cellspacing="0" style="width:100%;background:#F4EFE6;">
<tr><td align="center" style="padding:28px 12px;">
<table role="presentation" cellpadding="0" cellspacing="0" style="width:100%;max-width:560px;background:#FFFFFF;border-radius:10px;overflow:hidden;">
  <tr><td style="padding:22px 28px 0;">
    <span style="font-family:'IBM Plex Sans','Space Grotesk',Helvetica,Arial,sans-serif;font-size:19px;font-weight:700;letter-spacing:-0.01em;color:#E4572E;">MrBadmus</span>
  </td></tr>
  <tr><td style="padding:16px 28px 8px;font-family:'IBM Plex Sans',Helvetica,Arial,sans-serif;">
    <h1 style="margin:0 0 16px;font-size:22px;line-height:1.25;color:#2A2622;font-weight:700;">One tap and you&#39;re in.</h1>
    <p style="margin:0 0 14px;font-size:15px;line-height:1.6;color:#2A2622;">Confirm this is your address and the account is yours. The link works for 24 hours.</p>
    <p style="margin:22px 0;"><a href="{{ .ConfirmationURL }}" style="display:inline-block;padding:12px 22px;background:#E4572E;color:#FFFFFF;text-decoration:none;border-radius:6px;font-size:15px;font-weight:600;">Confirm my email</a></p>
    <p style="margin:0 0 14px;font-size:15px;line-height:1.6;color:#2A2622;">If you didn&#39;t sign up, ignore this and nothing happens.</p>
    <p style="margin:18px 0 0;font-size:15px;line-height:1.6;color:#2A2622;">Mide Badmus</p>
  </td></tr>
  <tr><td style="padding:8px 28px 26px;font-family:'IBM Plex Sans',Helvetica,Arial,sans-serif;">
    <hr style="border:0;border-top:1px solid #EDE6DA;margin:8px 0 14px;">
    <p style="margin:0 0 5px;font-size:12px;line-height:1.5;color:#6B6259;">Mr Badmus Education Ltd, England. You are getting this because you have a MrBadmus account for your family.</p>
    <p style="margin:0 0 5px;font-size:12px;line-height:1.5;color:#6B6259;">This one is required — there is nothing to unsubscribe from.</p>
  </td></tr>
</table>
</td></tr></table>
</body></html>
```

The markup above is the output of `consumer/email.js`'s own `render()`, so E1
sits in an inbox looking identical to E2–E8: same 560px card, same cream
ground, same `#E4572E` wordmark, same `#2A2622` ink. Do not restyle it by hand
— if the house style moves, re-render this one from `render()` rather than
patching the HTML here.

## Two settings to check while you are in there

- **Subject** field: `Confirm your email to finish setting up` (Supabase keeps
  the subject in its own box, separate from the body above).
- **Site URL / Redirect URLs** must include the verify landing
  `https://mrbadmus.com/consumer/verify.html`, or the link in this email
  confirms the address and then drops the parent somewhere that is not the
  next step.

⚠️ **The wordmark is `MrBadmus`.** Not the two-letter suffix, here or in any
other email. This is the first thing a stranger ever sees of the product and
the consumer brand is the teacher's name.
