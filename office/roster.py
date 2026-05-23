# office/roster.py
from __future__ import annotations

from office.card import render_card_markdown
from office.persona import Persona

_HEADER = "# The Office\n\n_Meet the coworkers._\n\n---\n\n"


def render_roster_markdown(personas: list[Persona]) -> str:
    if not personas:
        return _HEADER + "_No coworkers hired yet. Run `/hire`._\n"
    cards = "\n---\n\n".join(render_card_markdown(p) for p in personas)
    return _HEADER + cards + "\n"
