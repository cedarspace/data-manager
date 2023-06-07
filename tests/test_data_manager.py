# tests/test_rptodo.py
import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '../data_manager')
import data_manager
from data_manager import  __app_name__ 
from data_manager import __version__


import check_output
from typer.testing import CliRunner
from data_manager import cli

runner = CliRunner()

def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout

from data_manager import project_creator
project_creator()