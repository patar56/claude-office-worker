# office/persona.py
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

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


def parse_persona(text: str, slug: str | None = None) -> Persona:
    if not text.lstrip().startswith("---"):
        raise PersonaError("persona file is missing YAML frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise PersonaError("persona frontmatter is not terminated by '---'")
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        raise PersonaError(f"invalid YAML frontmatter: {exc}") from exc
    for key in _REQUIRED:
        if key not in fm:
            raise PersonaError(f"persona is missing required field: {key}")
    color = str(fm["color"])
    if not _COLOR_RE.match(color):
        raise PersonaError(f"color must be a #RRGGBB hex string, got: {color!r}")
    traits = fm["traits"]
    if not isinstance(traits, list):
        raise PersonaError("traits must be a list")
    body = parts[2]
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
