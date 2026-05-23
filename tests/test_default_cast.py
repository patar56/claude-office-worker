# tests/test_default_cast.py
from pathlib import Path

from office.persona import load_persona

CAST_DIR = Path(__file__).resolve().parent.parent / "default-cast" / "roster"


def test_three_default_coworkers_parse():
    files = sorted(CAST_DIR.glob("*.md"))
    assert len(files) == 3
    personas = [load_persona(f) for f in files]
    slugs = {p.slug for p in personas}
    assert slugs == {"vega", "pip", "cass"}


def test_default_coworkers_have_distinct_colors():
    personas = [load_persona(f) for f in sorted(CAST_DIR.glob("*.md"))]
    colors = [p.color for p in personas]
    assert len(set(colors)) == len(colors)


def test_default_coworkers_have_voice_and_boundaries():
    for f in sorted(CAST_DIR.glob("*.md")):
        p = load_persona(f)
        assert p.voice and p.boundaries
