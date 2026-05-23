# tests/test_commands.py
from pathlib import Path

CMD = Path(__file__).resolve().parent.parent / "commands"
BIN = Path(__file__).resolve().parent.parent / "bin"


def test_all_commands_exist():
    assert (CMD / "hire.md").exists()
    assert (CMD / "clock-in.md").exists()
    assert (CMD / "roster.md").exists()


def test_commands_only_reference_real_scripts():
    referenced = {"hire.md": "new_persona.py",
                  "clock-in.md": "clock_in.py",
                  "roster.md": "render_roster.py"}
    for cmd_file, script in referenced.items():
        text = (CMD / cmd_file).read_text(encoding="utf-8")
        assert script in text
        assert (BIN / script).exists()
