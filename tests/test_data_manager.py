# tests/test_rptodo.py
import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/Users/cedarspace/Desktop/Soghmon_files/DataManager_library/datamanager_project/data_manager')

import data_manager       


import check_output
from typer.testing import CliRunner

cli = data_manager.cli
import data_manager.cli

runner = CliRunner()

def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout

project_creator = data_manager.cli.project_creator
check_output.check_output_1(project_creator,  )

