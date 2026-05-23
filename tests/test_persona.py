# tests/test_persona.py
import pytest
from office.persona import parse_persona, slugify, Persona, PersonaError

SAMPLE = """---
name: Vega
role: Staff Reviewer
color: "#C9A227"
emblem: "◆"
catchphrase: "Measure twice, ship once."
traits: [meticulous, calm, dry-witted]
on_call: false
---

## Voice
Speaks plainly and briefly.

## Boundaries
Won't rubber-stamp.
"""


def test_slugify():
    assert slugify("Vega") == "vega"
    assert slugify("QA Hawk") == "qa-hawk"


def test_parse_persona_fields():
    p = parse_persona(SAMPLE)
    assert isinstance(p, Persona)
    assert p.name == "Vega"
    assert p.slug == "vega"
    assert p.role == "Staff Reviewer"
    assert p.color == "#C9A227"
    assert p.emblem == "◆"
    assert p.catchphrase == "Measure twice, ship once."
    assert p.traits == ["meticulous", "calm", "dry-witted"]
    assert p.on_call is False


def test_parse_persona_sections():
    p = parse_persona(SAMPLE)
    assert p.voice == "Speaks plainly and briefly."
    assert p.boundaries == "Won't rubber-stamp."


def test_explicit_slug_overrides_name():
    p = parse_persona(SAMPLE, slug="vega-2")
    assert p.slug == "vega-2"


def test_missing_frontmatter_raises():
    with pytest.raises(PersonaError):
        parse_persona("no frontmatter here")


def test_bad_color_raises():
    bad = SAMPLE.replace('"#C9A227"', '"gold"')
    with pytest.raises(PersonaError):
        parse_persona(bad)
