# tests/test_roster.py
from office.roster import render_roster_markdown
from office.persona import Persona


def _persona(name, color):
    return Persona(
        slug=name.lower(), name=name, role="Role", color=color, emblem="◆",
        catchphrase="Phrase.", traits=["a"], on_call=False, voice="V", boundaries="B",
    )


def test_roster_has_header_and_each_coworker():
    personas = [_persona("Vega", "#C9A227"), _persona("Pip", "#3E7CB1")]
    md = render_roster_markdown(personas)
    assert md.startswith("# The Office")
    assert "Vega" in md
    assert "Pip" in md
    # cards are separated by a horizontal rule
    assert "\n---\n" in md


def test_roster_empty():
    md = render_roster_markdown([])
    assert md.startswith("# The Office")
