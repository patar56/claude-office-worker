# tests/test_sign.py
from office.sign import signature_block, sign_message
from office.persona import Persona

P = Persona(
    slug="vega", name="Vega", role="Staff Reviewer", color="#C9A227",
    emblem="◆", catchphrase="Measure twice, ship once.",
    traits=["meticulous"], on_call=False, voice="V", boundaries="B",
)


def test_signature_block_format():
    block = signature_block(P)
    assert "Co-Authored-By: Vega (Claude Office) <office+vega@users.noreply.github.com>" in block
    assert "— Vega ◆ Staff Reviewer · \"Measure twice, ship once.\"" in block


def test_sign_message_appends_once():
    out = sign_message("Fix the bug", P)
    assert out.startswith("Fix the bug")
    assert "Co-Authored-By: Vega" in out
    # signing again is idempotent
    assert sign_message(out, P) == out
