# tests/test_install.py
import subprocess
import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
INSTALL = PLUGIN_ROOT / "bin" / "install.py"


def _git(args, cwd):
    subprocess.run(["git", *args], cwd=cwd, check=True,
                   capture_output=True, text=True)


def _run_install(target):
    return subprocess.run(
        [sys.executable, str(INSTALL), str(target)],
        capture_output=True, text=True,
    )


def test_install_scaffolds_office(tmp_path):
    _git(["init"], tmp_path)
    result = _run_install(tmp_path)
    assert result.returncode == 0, result.stderr
    office = tmp_path / ".claude-office"
    assert (office / "office.json").exists()
    assert (office / "ROSTER.md").exists()
    assert sorted(p.name for p in (office / "roster").glob("*.md")) == [
        "cass.md", "pip.md", "vega.md",
    ]


def test_install_installs_git_hook(tmp_path):
    _git(["init"], tmp_path)
    _run_install(tmp_path)
    hook = tmp_path / ".git" / "hooks" / "prepare-commit-msg"
    assert hook.exists()
    assert "sign_commit.py" in hook.read_text(encoding="utf-8")


def test_install_gitignores_active(tmp_path):
    _git(["init"], tmp_path)
    _run_install(tmp_path)
    gitignore = (tmp_path / ".gitignore").read_text(encoding="utf-8")
    assert ".claude-office/.active" in gitignore
