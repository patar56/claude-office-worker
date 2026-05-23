# tests/test_config.py
import json
from pathlib import Path

import pytest

from office.config import (
    OFFICE_DIRNAME, DEFAULT_PALETTE, find_office, load_office_config,
    save_office_config, list_personas, get_active, set_active, next_color,
)

PERSONA = """---
name: Vega
role: Staff Reviewer
color: "#C9A227"
emblem: "◆"
catchphrase: "Measure twice, ship once."
traits: [meticulous]
on_call: false
---

## Voice
Plainly.

## Boundaries
None.
"""


@pytest.fixture
def office(tmp_path):
    d = tmp_path / OFFICE_DIRNAME
    (d / "roster").mkdir(parents=True)
    (d / "roster" / "vega.md").write_text(PERSONA, encoding="utf-8")
    save_office_config(d, {"palette": DEFAULT_PALETTE})
    return d


def test_find_office_walks_up(office, tmp_path):
    nested = tmp_path / "a" / "b"
    nested.mkdir(parents=True)
    assert find_office(nested) == office


def test_find_office_none(tmp_path):
    assert find_office(tmp_path / "nope") is None


def test_load_and_save_config(office):
    cfg = load_office_config(office)
    assert cfg["palette"] == DEFAULT_PALETTE


def test_list_personas(office):
    people = list_personas(office)
    assert [p.slug for p in people] == ["vega"]


def test_active_roundtrip(office):
    assert get_active(office) is None
    set_active(office, "vega")
    assert get_active(office) == "vega"


def test_next_color_skips_used():
    cfg = {"palette": ["#111111", "#222222", "#333333"]}
    assert next_color(cfg, used=["#111111"]) == "#222222"
    assert next_color(cfg, used=["#111111", "#222222", "#333333"]) == "#111111"
