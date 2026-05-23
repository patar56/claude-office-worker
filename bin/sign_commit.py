# bin/sign_commit.py
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from office.config import find_office, get_active, list_personas  # noqa: E402
from office.sign import sign_message  # noqa: E402


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        return 0  # nothing to sign
    msg_path = Path(argv[1])
    office = find_office(Path.cwd())
    if office is None:
        return 0
    active = get_active(office)
    if not active:
        return 0
    persona = next((p for p in list_personas(office) if p.slug == active), None)
    if persona is None:
        return 0
    original = msg_path.read_text(encoding="utf-8")
    msg_path.write_text(sign_message(original, persona), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
