# office/card.py
from __future__ import annotations

from office.avatar import AVATAR_ROWS
from office.persona import Persona


def render_card_markdown(p: Persona) -> str:
    avatar = "\n".join("    " + row for row in AVATAR_ROWS)
    meta = f"`{p.color}`"
    if p.traits:
        meta += " · " + ", ".join(p.traits)
    card = (
        f"### {p.emblem} {p.name} — {p.role}\n\n"
        f"{avatar}\n\n"
        f"{meta}\n"
    )
    if p.catchphrase:
        card += f"\n> _\"{p.catchphrase}\"_\n"
    return card
