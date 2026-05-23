# tests/test_avatar.py
from office.avatar import AVATAR_ROWS, hex_to_rgb, render_avatar


def test_hex_to_rgb():
    assert hex_to_rgb("#C9A227") == (201, 162, 39)
    assert hex_to_rgb("#000000") == (0, 0, 0)
    assert hex_to_rgb("#ffffff") == (255, 255, 255)


def test_render_avatar_has_truecolor_prefix_and_reset():
    out = render_avatar("#C9A227")
    assert "\x1b[38;2;201;162;39m" in out
    assert "\x1b[0m" in out


def test_render_avatar_preserves_all_rows():
    out = render_avatar("#C9A227")
    assert out.count("\n") == len(AVATAR_ROWS) - 1
