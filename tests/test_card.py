# tests/test_card.py
from office.card import render_card_markdown
from office.persona import Persona

P = Persona(
    slug="vega", name="Vega", role="Staff Reviewer", color="#C9A227",
    emblem="◆", catchphrase="Measure twice, ship once.",
    traits=["meticulous", "calm"], on_call=False,
    voice="Speaks plainly.", boundaries="Won't rubber-stamp.",
)


def test_card_contains_identity():
    md = render_card_markdown(P)
    assert "Vega" in md
    assert "Staff Reviewer" in md
    assert "#C9A227" in md
    assert "◆" in md
    assert "Measure twice, ship once." in md
    assert "meticulous, calm" in md


def test_card_avatar_is_indented_code_block():
    md = render_card_markdown(P)
    # avatar rows are indented 4 spaces so they render as a code block
    assert "\n    " in md
