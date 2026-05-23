# office/persona.py
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

_COLOR_RE = re.compile(r"^#[0-9A-Fa-f]{6}$")
_REQUIRED = ("name", "role", "color", "emblem", "catchphrase", "traits")


class PersonaError(Exception):
    pass


@dataclass
class Persona:
    slug: str
    name: str
    role: str
    color: str
    emblem: str
    catchphrase: str
    traits: list[str]
    on_call: bool
    voice: str
    boundaries: str


def slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", name.strip().lower())
    return s.strip("-")


def _section(body: str, title: str) -> str:
    pattern = rf"##\s+{re.escape(title)}\s*\n(.*?)(?=\n##\s|\Z)"
    m = re.search(pattern, body, re.DOTALL)
    return m.group(1).strip() if m else ""


def _unquote(s: str) -> str:
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


def _parse_value(value: str):
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [_unquote(v.strip()) for v in inner.split(",")]
    low = value.lower()
    if low == "true":
        return True
    if low == "false":
        return False
    return _unquote(value)


def _parse_frontmatter(fm_lines: list[str]) -> dict:
    data: dict = {}
    for raw in fm_lines:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise PersonaError(f"invalid frontmatter line: {raw!r}")
        key, _, value = line.partition(":")
        data[key.strip()] = _parse_value(value.strip())
    return data


def parse_persona(text: str, slug: str | None = None) -> Persona:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise PersonaError("persona file is missing YAML frontmatter")
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        raise PersonaError("persona frontmatter is not terminated by '---'")
    fm = _parse_frontmatter(lines[1:end])
    body = "\n".join(lines[end + 1:])
    for key in _REQUIRED:
        if key not in fm:
            raise PersonaError(f"persona is missing required field: {key}")
    color = str(fm["color"])
    if not _COLOR_RE.match(color):
        raise PersonaError(f"color must be a #RRGGBB hex string, got: {color!r}")
    traits = fm["traits"]
    if not isinstance(traits, list):
        raise PersonaError("traits must be a list")
    return Persona(
        slug=slug or slugify(str(fm["name"])),
        name=str(fm["name"]),
        role=str(fm["role"]),
        color=color,
        emblem=str(fm["emblem"]),
        catchphrase=str(fm["catchphrase"]),
        traits=[str(t) for t in traits],
        on_call=bool(fm.get("on_call", False)),
        voice=_section(body, "Voice"),
        boundaries=_section(body, "Boundaries"),
    )


def load_persona(path: Path) -> Persona:
    path = Path(path)
    return parse_persona(path.read_text(encoding="utf-8"), slug=path.stem)
