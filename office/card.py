# office/card.py
from __future__ import annotations

from office.avatar import AVATAR_ROWS
from office.persona import Persona


def render_card_markdown(p: Persona) -> str:
    avatar = "\n".join("    " + row for row in AVATAR_ROWS)
    traits = ", ".join(p.traits)
    return (
        f"### {p.emblem} {p.name} — {p.role}\n\n"
        f"{avatar}\n\n"
        f"`{p.color}` · {traits}\n\n"
        f"> _\"{p.catchphrase}\"_\n"
    )
