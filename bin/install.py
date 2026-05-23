# bin/install.py
from __future__ import annotations

import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from office.config import (  # noqa: E402
    OFFICE_DIRNAME, DEFAULT_PALETTE, save_office_config, list_personas,
)
from office.roster import render_roster_markdown  # noqa: E402

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CAST = PLUGIN_ROOT / "default-cast" / "roster"
SIGN_COMMIT = PLUGIN_ROOT / "bin" / "sign_commit.py"

HOOK_TEMPLATE = """#!/bin/sh
# Installed by claude-office-worker. Signs commits as the active coworker.
"{python}" "{sign_commit}" "$1"
"""


def _ensure_gitignore(target: Path) -> None:
    gi = target / ".gitignore"
    line = ".claude-office/.active"
    existing = gi.read_text(encoding="utf-8") if gi.exists() else ""
    if line not in existing:
        with gi.open("a", encoding="utf-8") as fh:
            if existing and not existing.endswith("\n"):
                fh.write("\n")
            fh.write(line + "\n")


def _install_hook(target: Path) -> None:
    hooks_dir = target / ".git" / "hooks"
    if not hooks_dir.is_dir():
        return  # not a git repo (yet); skip silently
    hook = hooks_dir / "prepare-commit-msg"
    hook.write_text(
        HOOK_TEMPLATE.format(python=sys.executable, sign_commit=SIGN_COMMIT),
        encoding="utf-8",
    )
    hook.chmod(0o755)


def main(argv: list[str]) -> int:
    target = Path(argv[1]).resolve() if len(argv) > 1 else Path.cwd()
    office = target / OFFICE_DIRNAME
    roster = office / "roster"
    roster.mkdir(parents=True, exist_ok=True)

    for src in sorted(DEFAULT_CAST.glob("*.md")):
        dst = roster / src.name
        if not dst.exists():
            shutil.copyfile(src, dst)

    save_office_config(office, {"palette": list(DEFAULT_PALETTE)})
    (office / "ROSTER.md").write_text(
        render_roster_markdown(list_personas(office)), encoding="utf-8"
    )
    _ensure_gitignore(target)
    _install_hook(target)
    print(f"Office installed at {office}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
