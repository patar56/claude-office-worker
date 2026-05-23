# office/sign.py
from __future__ import annotations

from office.persona import Persona

_MARKER = "(Claude Office)"


def signature_block(p: Persona) -> str:
    coauthor = (
        f"Co-Authored-By: {p.name} (Claude Office) "
        f"<office+{p.slug}@users.noreply.github.com>"
    )
    emblem_line = f"— {p.name} {p.emblem} {p.role} · \"{p.catchphrase}\""
    return f"{coauthor}\n{emblem_line}"


def sign_message(msg: str, p: Persona) -> str:
    if _MARKER in msg:
        return msg
    return f"{msg.rstrip()}\n\n{signature_block(p)}\n"
