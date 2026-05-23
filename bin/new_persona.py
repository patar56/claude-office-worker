# bin/new_persona.py
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from office.config import (  # noqa: E402
    find_office, load_office_config, list_personas, next_color,
)
from office.persona import slugify  # noqa: E402
from office.roster import render_roster_markdown  # noqa: E402

TEMPLATE = """---
name: {name}
role: {role}
color: "{color}"
emblem: "{emblem}"
catchphrase: "{catchphrase}"
traits: [{traits}]
on_call: false
---

## Voice
{voice}

## Boundaries
{boundaries}
"""


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--role", required=True)
    parser.add_argument("--emblem", required=True)
    parser.add_argument("--catchphrase", required=True)
    parser.add_argument("--traits", required=True, help="comma-separated")
    parser.add_argument("--voice", required=True)
    parser.add_argument("--boundaries", required=True)
    parser.add_argument("--color", default=None)
    args = parser.parse_args(argv[1:])

    office = find_office(Path.cwd())
    if office is None:
        print("No .claude-office found. Install first.", file=sys.stderr)
        return 1

    cfg = load_office_config(office)
    existing = list_personas(office)
    color = args.color or next_color(cfg, [p.color for p in existing])
    traits = ", ".join(t.strip() for t in args.traits.split(",") if t.strip())
    slug = slugify(args.name)

    content = TEMPLATE.format(
        name=args.name, role=args.role, color=color, emblem=args.emblem,
        catchphrase=args.catchphrase, traits=traits,
        voice=args.voice, boundaries=args.boundaries,
    )
    (office / "roster" / f"{slug}.md").write_text(content, encoding="utf-8")

    (office / "ROSTER.md").write_text(
        render_roster_markdown(list_personas(office)), encoding="utf-8"
    )
    print(f"Hired {args.name} ({color}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
