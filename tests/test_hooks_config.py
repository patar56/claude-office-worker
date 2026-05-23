# tests/test_hooks_config.py
import json
from pathlib import Path

HOOKS = Path(__file__).resolve().parent.parent / "hooks" / "hooks.json"


def test_hooks_json_is_valid_and_wires_session_start():
    data = json.loads(HOOKS.read_text(encoding="utf-8"))
    assert "SessionStart" in data["hooks"]
    cmd = data["hooks"]["SessionStart"][0]["hooks"][0]["command"]
    assert "session_start.py" in cmd
    assert "${CLAUDE_PLUGIN_ROOT}" in cmd
