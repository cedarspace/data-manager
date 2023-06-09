"""This module provides the RP To-Do CLI."""
# data_manager/cli.py

from typing import Optional
import os
import typer
from data_manager import *
import shutil 
import data_types


app = typer.Typer()


@app.command()
def project_creator(
    name : str , 
    directory : str
    ):
    '''
    creates a new project directory.
    '''

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
def file_mover(project_directory : str, 
    file_directory : str, stage : str ):
    '''
    (test)
    moves file to specified project and stage.
    '''
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
def file_namer( file_name : str ):
    '''
    !!!
    names files according to convetions specified.
    '''
    ''' output: File '''
    version1 = file_name.replace(" ", "_")
    version2 = version1.lower()
    special_characters = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', '/', ':', ';', "'", '<', '>', ',', '.', '?']
    list_of_letters = []
    for i in version2: 
       list_of_letters.append(i)
    
    for i in list_of_letters:
        for ii in special_characters:
             if i == ii:
                version2 = version2.replace( i, "")
    
    def number(n : str):
      ''' ouput: str'''
      if n.isdigit():
        print("your file begins with a number, make sure to use the version function if this is a different verison of an existing file. Numbers are only kept if there is iteration in the directory")
        keep : str = input('Do you want to keep the number (y/n)? ' )
        if keep == "y":
            version3 = version2
            return data_types.txt_file(version3) 
        if keep == "n":
            version3 = version2[1:]
            return data_types.txt_file(version3) 
        else: 
            print('please enter y or n')
            number(n)
    number(version2[0])





    

            
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



