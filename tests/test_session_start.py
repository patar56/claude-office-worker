# tests/test_session_start.py
import subprocess
import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
SESSION_START = PLUGIN_ROOT / "bin" / "session_start.py"

PERSONA = """---
name: Vega
role: Staff Reviewer
color: "#C9A227"
emblem: "◆"
catchphrase: "Measure twice, ship once."
traits: [meticulous]
on_call: true
---

## Voice
Speaks plainly and briefly.

## Boundaries
Won't rubber-stamp.
"""


def _office(tmp_path, active):
    roster = tmp_path / ".claude-office" / "roster"
    roster.mkdir(parents=True)
    (roster / "vega.md").write_text(PERSONA, encoding="utf-8")
    if active:
        (tmp_path / ".claude-office" / ".active").write_text("vega\n", encoding="utf-8")


def _run(cwd):
    return subprocess.run(
        [sys.executable, str(SESSION_START)],
        cwd=cwd, capture_output=True, text=True,
    )


def test_emits_persona_context_when_clocked_in(tmp_path):
    _office(tmp_path, active=True)
    result = _run(tmp_path)
    assert result.returncode == 0
    assert "Vega" in result.stdout
    assert "Speaks plainly and briefly." in result.stdout
    assert "Won't rubber-stamp." in result.stdout


def test_silent_when_not_clocked_in(tmp_path):
    _office(tmp_path, active=False)
    result = _run(tmp_path)
    assert result.returncode == 0
    assert result.stdout.strip() == ""


def test_silent_when_no_office(tmp_path):
    result = _run(tmp_path)
    assert result.returncode == 0
    assert result.stdout.strip() == ""
