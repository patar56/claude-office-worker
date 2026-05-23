# tests/test_render_roster.py
import subprocess
import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
RENDER = PLUGIN_ROOT / "bin" / "render_roster.py"

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


def test_render_writes_roster_and_prints_it(tmp_path):
    roster = tmp_path / ".claude-office" / "roster"
    roster.mkdir(parents=True)
    (roster / "vega.md").write_text(PERSONA, encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(RENDER)], cwd=tmp_path,
        capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "Vega" in result.stdout
    written = (tmp_path / ".claude-office" / "ROSTER.md").read_text(encoding="utf-8")
    assert "Vega" in written
