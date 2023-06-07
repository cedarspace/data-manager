# tests/test_rptodo.py
import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '../data_manager')

import data_manager       


import check_output
from typer.testing import CliRunner
import cli

#cli = data_manager.cli
#import data_manager.cli

runner = CliRunner()

def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout

project_creator = cli.project_creator
check_output.check_output_1(project_creator,  )

