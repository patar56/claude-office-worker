# tests/test_sign_commit.py
import subprocess
import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
SIGN_COMMIT = PLUGIN_ROOT / "bin" / "sign_commit.py"

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


def _office(tmp_path, active=True):
    office = tmp_path / ".claude-office" / "roster"
    office.mkdir(parents=True)
    (office / "vega.md").write_text(PERSONA, encoding="utf-8")
    if active:
        (tmp_path / ".claude-office" / ".active").write_text("vega\n", encoding="utf-8")


def _run(msg_file):
    return subprocess.run(
        [sys.executable, str(SIGN_COMMIT), str(msg_file)],
        cwd=msg_file.parent, capture_output=True, text=True,
    )


def test_signs_when_clocked_in(tmp_path):
    _office(tmp_path, active=True)
    msg = tmp_path / "COMMIT_EDITMSG"
    msg.write_text("Fix the bug\n", encoding="utf-8")
    result = _run(msg)
    assert result.returncode == 0, result.stderr
    text = msg.read_text(encoding="utf-8")
    assert "Co-Authored-By: Vega" in text


def test_noop_when_not_clocked_in(tmp_path):
    _office(tmp_path, active=False)
    msg = tmp_path / "COMMIT_EDITMSG"
    msg.write_text("Fix the bug\n", encoding="utf-8")
    result = _run(msg)
    assert result.returncode == 0
    assert msg.read_text(encoding="utf-8") == "Fix the bug\n"


def test_noop_when_no_office(tmp_path):
    msg = tmp_path / "COMMIT_EDITMSG"
    msg.write_text("Fix the bug\n", encoding="utf-8")
    result = _run(msg)
    assert result.returncode == 0
    assert msg.read_text(encoding="utf-8") == "Fix the bug\n"
