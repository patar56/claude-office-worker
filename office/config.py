# office/config.py
from __future__ import annotations

import json
from pathlib import Path

from office.persona import Persona, load_persona

OFFICE_DIRNAME = ".claude-office"
_CONFIG_NAME = "office.json"
_ACTIVE_NAME = ".active"  # local, gitignored: who YOU are clocked in as

# A curated, refined multi-color palette (gold, slate-blue, rose, sage,
# violet, amber). One color per coworker.
DEFAULT_PALETTE = [
    "#C9A227", "#3E7CB1", "#B5485D", "#5B8C5A", "#8E6FB6", "#C7743B",
]


def find_office(start) -> Path | None:
    p = Path(start).resolve()
    for d in (p, *p.parents):
        cand = d / OFFICE_DIRNAME
        if cand.is_dir():
            return cand
    return None


def load_office_config(office_dir) -> dict:
    path = Path(office_dir) / _CONFIG_NAME
    if not path.exists():
        return {"palette": list(DEFAULT_PALETTE)}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"palette": list(DEFAULT_PALETTE)}


def save_office_config(office_dir, cfg: dict) -> None:
    path = Path(office_dir) / _CONFIG_NAME
    path.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")


def list_personas(office_dir) -> list[Persona]:
    roster = Path(office_dir) / "roster"
    if not roster.is_dir():
        return []
    return [load_persona(p) for p in sorted(roster.glob("*.md"))]


def get_active(office_dir) -> str | None:
    path = Path(office_dir) / _ACTIVE_NAME
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8").strip() or None


def set_active(office_dir, slug: str) -> None:
    (Path(office_dir) / _ACTIVE_NAME).write_text(slug + "\n", encoding="utf-8")


def next_color(cfg: dict, used: list[str]) -> str:
    palette = cfg.get("palette") or list(DEFAULT_PALETTE)
    for color in palette:
        if color not in used:
            return color
    return palette[len(used) % len(palette)]
