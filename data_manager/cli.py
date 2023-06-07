"""This module provides the RP To-Do CLI."""
# data_manager/cli.py

from typing import Optional
import os
import typer
from data_manager import *
import shutil 



app = typer.Typer()


@app.command()
def project_creator(
    name: Annotated[
        str, typer.Option(prompt="insert a name for your project: ")
    ] , 
    directory: Annotated[
        str, typer.Option(prompt="nsert the directory that will host your project: ")
    ]):

    ''' error handeling 1  '''
    try: 
        os.chdir(directory)
    except FileExistsError or FileNotFoundError:
        print("project creation failed, check that your directory exits")
        return 1
    except: 
        print("project creation failed")
        return 2
    
    '''creation of main directory of function '''
    dirpath = os.path.join(directory, name)
    os.makedirs(dirpath, exist_ok=True)

    '''creation of subdirectories for each stage'''
    dc_folder_path = os.path.join(dirpath, "1.data_collection")
    training_folder_path = os.path.join(dirpath, "2.training")
    evaluation_folder_path = os.path.join(dirpath, "3.evaluation")
    deployment_folder_path = os.path.join(dirpath, "4.deployment")
    os.makedirs(dc_folder_path, exist_ok=True)
    os.makedirs(training_folder_path, exist_ok=True)
    os.makedirs(evaluation_folder_path, exist_ok=True)
    os.makedirs(deployment_folder_path, exist_ok=True)

    '''creation of sources folders in trainnig'''
    os.chdir(dc_folder_path)
    source_number = input("How many sources does your folder have? ")
    for i in range(0, int(source_number)):
        name = input("enter source " + str(i+1) + "'s name: ")
        os.makedirs(os.path.join(os.getcwd(), name))
    

    '''creation of models folders in trainnig'''
    os.chdir(training_folder_path)
    model_number = input("How many models does your folder have? ")
    for i in range(0, int(model_number)):
        name = input("enter model " + str(i+1) + "'s name: ")
        os.makedirs(os.path.join(os.getcwd(), name))
    
    '''creation of txt file that has peoject name and directory'''
    pathfortxt = os.path.join( dirpath, "ProjectData.txt")
    f = open(pathfortxt, "w")
    f.write(directory + "  " + dirpath)

        


@app.command()
def file_mover():
    '''
    (test)
    moves file to specified project and stage.
    '''
    project_directory : str = input("enter the project directory: ")
    file_directory : str = input("enter the file directory: ")
    stage : str = input("in which stage would you like to put it? ")
    path = os.path.join(project_directory, stage.lower())
    try: 
        os.chdir(path)
    except:
        print("either project error, or stage's name is wrong")
        return 1
    try: 
        open(file_directory, "r")
    except:
        print("file does not exist")
        return 2

    if os.getcwd() != path:
        os.chdir(path)

    shutil.move(file_directory, path)
@app.command()
def file_namer():
    '''
    !!!
    names files according to convetions specified.
    '''

@app.command()
def file_puller():
    '''
    !!!
    pulls a file from project and stage specified.
    '''

@app.command()
def new_data():   
    '''
    !!!
    adds new data source folder in the data collection stage.
    '''

@app.command()
def new_model():
    '''
    !!!
    adds a new model folder in the training stage.
    '''




def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return



if __app_name__ == "__app__":
    app()