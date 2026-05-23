# tests/test_new_persona.py
import subprocess
import sys
from pathlib import Path

from office.persona import load_persona

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
NEW_PERSONA = PLUGIN_ROOT / "bin" / "new_persona.py"


def _office(tmp_path):
    (tmp_path / ".claude-office" / "roster").mkdir(parents=True)


def _run(args, cwd):
    return subprocess.run(
        [sys.executable, str(NEW_PERSONA), *args],
        cwd=cwd, capture_output=True, text=True,
    )


def test_creates_persona_file_and_roster(tmp_path):
    _office(tmp_path)
    result = _run([
        "--name", "Quill", "--role", "Docs Lead",
        "--emblem", "✎", "--catchphrase", "Write it down.",
        "--traits", "clear,patient",
        "--voice", "Friendly and precise.",
        "--boundaries", "Won't ship undocumented APIs.",
    ], tmp_path)
    assert result.returncode == 0, result.stderr
    persona_file = tmp_path / ".claude-office" / "roster" / "quill.md"
    assert persona_file.exists()
    p = load_persona(persona_file)
    assert p.name == "Quill"
    assert p.color.startswith("#")
    assert (tmp_path / ".claude-office" / "ROSTER.md").read_text(encoding="utf-8").find("Quill") != -1


def test_assigns_distinct_color_from_existing(tmp_path):
    _office(tmp_path)
    _run(["--name", "A", "--role", "R", "--emblem", "◆",
          "--catchphrase", "c", "--traits", "x",
          "--voice", "v", "--boundaries", "b"], tmp_path)
    _run(["--name", "B", "--role", "R", "--emblem", "◆",
          "--catchphrase", "c", "--traits", "x",
          "--voice", "v", "--boundaries", "b"], tmp_path)
    a = load_persona(tmp_path / ".claude-office" / "roster" / "a.md")
    b = load_persona(tmp_path / ".claude-office" / "roster" / "b.md")
    assert a.color != b.color
