# office/sign.py
from __future__ import annotations

from office.persona import Persona

_MARKER = "(Claude Office)"


def signature_block(p: Persona) -> str:
    coauthor = (
        f"Co-Authored-By: {p.name} (Claude Office) "
        f"<office+{p.slug}@users.noreply.github.com>"
    )
    emblem_line = f"— {p.name} {p.emblem} {p.role}"
    if p.catchphrase:
        emblem_line += f" · \"{p.catchphrase}\""
    return f"{coauthor}\n{emblem_line}"


def sign_message(msg: str, p: Persona) -> str:
    if _MARKER in msg:
        return msg
    block = signature_block(p)
    lines = msg.split("\n")
    idx = next((i for i, ln in enumerate(lines) if ln.startswith("#")), None)
    if idx is None:
        return f"{msg.rstrip()}\n\n{block}\n"
    head = "\n".join(lines[:idx]).rstrip()
    tail = "\n".join(lines[idx:])
    return f"{head}\n\n{block}\n\n{tail}"
