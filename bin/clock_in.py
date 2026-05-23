# bin/clock_in.py
from __future__ import annotations

import io
import sys
from pathlib import Path

# Ensure stdout can handle Unicode (block characters in the avatar) on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
else:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from office.avatar import render_avatar  # noqa: E402
from office.config import find_office, list_personas, set_active  # noqa: E402
from office.persona import slugify  # noqa: E402


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: clock_in.py <name-or-slug>", file=sys.stderr)
        return 2
    query = slugify(argv[1])
    office = find_office(Path.cwd())
    if office is None:
        print("No .claude-office found. Run /hire or install first.", file=sys.stderr)
        return 1
    personas = list_personas(office)
    persona = next((p for p in personas if p.slug == query), None)
    if persona is None:
        names = ", ".join(p.slug for p in personas) or "(none)"
        print(f"No coworker named {argv[1]!r}. Roster: {names}", file=sys.stderr)
        return 1
    set_active(office, persona.slug)
    print(render_avatar(persona.color))
    print(f"\n{persona.name} {persona.emblem} {persona.role} has clocked in.")
    print(f"\"{persona.catchphrase}\"")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
