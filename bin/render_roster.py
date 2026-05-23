# bin/render_roster.py
from __future__ import annotations

import io
import sys
from pathlib import Path

# Ensure stdout can handle Unicode (block characters in avatar rows) on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
else:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from office.config import find_office, list_personas  # noqa: E402
from office.roster import render_roster_markdown  # noqa: E402


def main() -> int:
    office = find_office(Path.cwd())
    if office is None:
        print("No .claude-office found.", file=sys.stderr)
        return 1
    md = render_roster_markdown(list_personas(office))
    (office / "ROSTER.md").write_text(md, encoding="utf-8")
    print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
