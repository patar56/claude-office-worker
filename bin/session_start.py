# bin/session_start.py
from __future__ import annotations

import io
import sys
from pathlib import Path

# Ensure stdout can handle Unicode on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
else:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from office.config import find_office, get_active, list_personas  # noqa: E402


def main() -> int:
    office = find_office(Path.cwd())
    if office is None:
        return 0
    active = get_active(office)
    if not active:
        return 0
    persona = next((p for p in list_personas(office) if p.slug == active), None)
    if persona is None:
        return 0
    print(
        f"You are clocked in as {persona.name} {persona.emblem} "
        f"({persona.role}). Stay in character for this session.\n\n"
        f"Voice:\n{persona.voice}\n\n"
        f"Boundaries:\n{persona.boundaries}\n\n"
        f"Sign your git commits and any PR/review text as {persona.name}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
