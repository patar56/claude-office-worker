---
description: Hire a new Claude Office coworker (interactive)
---

# Hire a coworker

Help the user create a new office coworker. Gather these one at a time, keeping
it quick and warm:

1. **Name** (a short first name).
2. **Role** (e.g. "Backend Lead", "Docs Wrangler").
3. **Three or four personality traits** (e.g. blunt, witty, careful).
4. **A one-line catchphrase / sign-off.**
5. **An emblem** — a single character (e.g. ◆ ✦ ✕ ✎ ★). Suggest one that fits.
6. **Voice** — 2–3 sentences on how they talk and write.
7. **Boundaries** — 1–2 sentences on what they won't do.

Color is assigned automatically from the office palette unless the user asks for
a specific one.

When you have the details, create the coworker by running:

```
python "${CLAUDE_PLUGIN_ROOT}/bin/new_persona.py" \
  --name "<name>" --role "<role>" --emblem "<emblem>" \
  --catchphrase "<catchphrase>" --traits "<t1,t2,t3>" \
  --voice "<voice>" --boundaries "<boundaries>"
```

Then show the user the new entry from `.claude-office/ROSTER.md` and suggest they
`git add .claude-office && git commit` so the team gets the new hire.
