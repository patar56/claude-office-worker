# tests/test_skill.py
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent / "skills" / "persona-engine" / "SKILL.md"


def test_skill_has_frontmatter_name_and_description():
    text = SKILL.read_text(encoding="utf-8")
    assert text.startswith("---")
    assert "name:" in text
    assert "description:" in text


def test_skill_mentions_embodiment_and_signing():
    text = SKILL.read_text(encoding="utf-8").lower()
    assert "clock" in text
    assert "voice" in text
    assert "sign" in text
