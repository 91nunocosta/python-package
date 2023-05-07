"""Test the command line interface for template_pyproject."""
from typer.testing import CliRunner

from template_pyproject.cli import app

runner = CliRunner()


def test_app() -> None:
    """Test the command line interface for template_pyproject"""
    result = runner.invoke(app, ["10"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "55"
