"""Test the command line interface for prototype-python-library"""
from typer.testing import CliRunner

from prototype_python_library.cli import app

runner = CliRunner()


def test_app() -> None:
    """Test the command line interface for prototype-python-library"""
    result = runner.invoke(app, ["10"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "55"
