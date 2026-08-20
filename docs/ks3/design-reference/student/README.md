# MrBadmusAI — student pages, v1

Two screens: the **class view** and the **assignment** behind its *Open the assignment* button.
Date 19 August 2026.

## Open these first

`standalone/MrBadmusAI Class View.html`
`standalone/MrBadmusAI Assignment.html`

Double-click either one. They are single self-contained files — fonts, tokens, React and every state inlined — so they work offline, on a plane, on a phone, with no server and no build step. Nothing else in this folder is needed to look at them.

### Reaching the assignment's states

The assignment opens mid-way through, six questions answered. Add a hash to the address to see any other state:

| | |
| --- | --- |
| `…Assignment.html#first` | first open, nothing answered |
| `…Assignment.html#midway` | six answered, four right |
| `…Assignment.html#returning` | coming back after leaving |
| `…Assignment.html#all` | all answered, not handed in |
| `…Assignment.html#done` | handed in — the end screen |
| `…Assignment.html#late` | opened after the due date |
| `…Assignment.html#donelate` | handed in late |
| `…Assignment.html#live` | the real thing: saves and restores as you go |

Turn your wifi off at any point to see the offline behaviour — it is driven by the real network events.

## What is in the folder

| Path | What it is |
| --- | --- |
| `standalone/` | the two self-contained files. Give these to anyone. |
| `handoff notes/` | the two READMEs. Every value, token, breakpoint, state and open question, per screen. Read these before building. |
| `source/` | the authoring sources — template plus logic class per screen — with `support.js` and the design-system bundle beside them, so they open and run from this folder as-is. |
| `source/_ds/mrbadmusai-design-system-…/` | the design system: tokens, self-hosted fonts, component bundle. Linked by relative path from each source file. |

The `- standalone source.dc.html` variants are the same designs plus a bundler thumbnail; they are what compile to the two files in `standalone/`. Edit the plain `.dc.html`, then recompile.

## The two open items

1. **The class view says eight questions; the assignment is fifteen.** The class view's docket, its bench task and its blurb all need the real count from `assignment.questionCount`. The approved v1 file has not been touched.
2. **Open the assignment is not wired.** The route is `/class/8r-sc1/assignments/:id`. The class view currently ticks task one and stays put; the assignment page's back button goes through history.

Everything else that must not ship as drawn is listed at the end of each README: authored questions and figures stand in for API content, dates are fixed strings, and 360px is verified in a desktop browser rather than on a device.
