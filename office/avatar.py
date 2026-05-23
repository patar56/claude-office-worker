# office/avatar.py
from __future__ import annotations

# A blocky, sunburst-style nod to the Claude mark. Same shape for every
# coworker; only the tint changes. Refined and symmetrical, not busy.
AVATAR_ROWS = [
    "    ▄██▄    ",
    "▀▄▄ ████ ▄▄▀",
    "  ████████  ",
    "▄▀▀ ████ ▀▀▄",
    "    ▀██▀    ",
]


def hex_to_rgb(hex_str: str) -> tuple[int, int, int]:
    h = hex_str.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def render_avatar(color: str) -> str:
    r, g, b = hex_to_rgb(color)
    prefix = f"\x1b[38;2;{r};{g};{b}m"
    reset = "\x1b[0m"
    return "\n".join(f"{prefix}{row}{reset}" for row in AVATAR_ROWS)
