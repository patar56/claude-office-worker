# Claude Office Worker

Give Claude a roster of named AI coworkers. Each coworker is the Claude avatar,
tinted to their own signature color, with a name, role, voice, and catchphrase.
Clock in as one and Claude works — and signs commits — in their voice. The
roster lives in `.claude-office/` in your repo, so your whole team shares it
via git.

## Install (in a repo you work in)

```
python /path/to/claude-office-worker/bin/install.py
git add .claude-office .gitignore && git commit -m "chore: open the office"
```

This scaffolds `.claude-office/` with a default cast (Vega, Pip, Cass), writes
`ROSTER.md`, and installs a `prepare-commit-msg` git hook.

## Use

- `/roster` — meet the office.
- `/clock-in <name>` — become a coworker for this session.
- `/hire` — create a new coworker.

Commits made while clocked in are signed by that coworker automatically.

## What's next

v0.2 adds `/assign` and `/peer-review` (coworkers reviewing each other's PRs);
v0.3 adds a `/standup` digest. The long game is **Claude Block**, a block/pixel
IDE that reads the same `.claude-office/` files — which is why that format is a
stable, documented contract.
