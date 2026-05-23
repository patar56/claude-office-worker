# tests/test_clock_in.py
import subprocess
import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
CLOCK_IN = PLUGIN_ROOT / "bin" / "clock_in.py"

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
Plain.

## Boundaries
None.
"""


def _office(tmp_path):
    roster = tmp_path / ".claude-office" / "roster"
    roster.mkdir(parents=True)
    (roster / "vega.md").write_text(PERSONA, encoding="utf-8")


def _run(name, cwd):
    return subprocess.run(
        [sys.executable, str(CLOCK_IN), name],
        cwd=cwd, capture_output=True, text=True,
    )


def test_clock_in_sets_active_and_greets(tmp_path):
    _office(tmp_path)
    result = _run("vega", tmp_path)
    assert result.returncode == 0, result.stderr
    assert (tmp_path / ".claude-office" / ".active").read_text(encoding="utf-8").strip() == "vega"
    assert "Vega" in result.stdout
    # ANSI color present in the greeting
    assert "\x1b[38;2;201;162;39m" in result.stdout


def test_clock_in_unknown_name_errors(tmp_path):
    _office(tmp_path)
    result = _run("nobody", tmp_path)
    assert result.returncode != 0
    assert "nobody" in (result.stdout + result.stderr)


def test_clock_in_no_office_errors(tmp_path):
    result = _run("vega", tmp_path)
    assert result.returncode != 0
