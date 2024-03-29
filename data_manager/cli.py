"""This module provides the data_manager CLI."""
# data_manager/cli.py

from typing import Optional
import os
import typer
from data_manager import *
import shutil 
__app_name__ = "data_manager"
__version__ = "0.1.0"


app = typer.Typer()


class ProjectCreatorArgs:
    ''' ProjectCreatorArgs is a class that holds some of the arguments for project_creator function 
        It only includes the ones related to sources and models. '''
    def __init__(self, sourceNumber : int = None, sourceNames : list = None , 
                 modelNumber : int  = None, modelNames: list = None):
        self.sourceNumber = sourceNumber
        self.sourceNames = sourceNames
        self.modelNumber = modelNumber 
        self.modelNames = modelNames 

class txt_file():
    
    def __init__(self, name: str): 
        ''' 
        Intp. File is a String that contains the name 
        of the file and .txt.  
        
        '''
        self.name = (name + ".txt") 


        




@app.command()
def project_creator(
    name : str = None , 
    directory : str = None,
    testargs  = None
    ):
    '''
    creates a new project directory.
    '''
    if name is not None: 
        name = name 
    else: 
        name = input("enter a name for your porject: ")
    
    if directory is not None: 
        directory = directory 
    else: 
        directory = input("enter a directory for your porject: ")

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
    name = file_namer(name)
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

   
    try: 
       os.chdir(dc_folder_path)
       os.chdir(training_folder_path)
       os.chdir(evaluation_folder_path)
       os.chdir(deployment_folder_path)
    except: 
        print("error in project creation, subdirectories not created")
        return 3
    ''' for test mode '''
    if testargs is not None:
        args = testargs
    else:
        '''creation of sources folders in trainnig'''
        source_names : list = []
        source_number : int = input("How many sources does your folder have? ")
        for i in range(0, int(source_number)):
            temp_name = input("enter source " + str(i+1) + "'s name: ")
            source_names.append(file_namer(temp_name))
        args = ProjectCreatorArgs(source_number, source_names)
    for i in range(0, int(len(args.sourceNames))):
        os.makedirs(os.path.join(dc_folder_path, args.sourceNames[i]))     

        '''creation of models folders in trainnig'''
        model_names : list = []
        model_number: int = input("How many model does your folder have? ")
        for i in range(0, int(model_number)):
             temp_name_2 = input("enter model " + str(i+1) + "'s name: ")
             model_names.append(file_namer(temp_name_2))
        args = ProjectCreatorArgs(None, None, model_number, model_names)
    for i in range(0, int(len(args.modelNames))):
         os.makedirs(os.path.join(training_folder_path, args.modelNames[i]))
    try: 
        for i in range(0, int(len(args.modelNames))):
         os.chdir(os.path.join(training_folder_path, args.modelNames[i]))
        for i in range(0, int(len(args.sourceNames))):
         os.makedirs(os.path.join(dc_folder_path, args.sourceNames[i]))
    except: 
        print("error in source or model directory creation")
        return 4

    '''creation of txt file that has peoject name and directory'''
    pathfortxt = os.path.join( dirpath, "ProjectData.txt")
    f = open(pathfortxt, "w")
    f.write(directory + "  " + dirpath)
    print(dirpath)


    '''if no error is raised, it means everything worked and returns True'''
    return True

        
def variable_initialiser(variable_name, input_message: str): 
    if variable_name is None: 
        variable_value =  input(input_message)
        return variable_value

@app.command()
def file_mover(project_directory : str = None, 
    file_directory : str = None , stage : str = None , testing : bool = None):
    '''
    moves file to specified project and stage.
    '''
    '''initialising variables '''
    project_directory = variable_initialiser(project_directory, "enter the directory of your project: ")
    file_directory = variable_initialiser(file_directory, "enter the directory of the file you want to move: ")
    stage = variable_initialiser(stage, "In which stage would you like to move it? ")


    path = os.path.join(project_directory, stage.lower())
    try: 
        os.chdir(path)
        os.chdir(file_directory)
    except:
        print(path + "might be wrong")
        print("either project error, or stage's name is wrong or file doesn't exist")
        return 1

    if os.getcwd() != path:
        os.chdir(path)

    shutil.move(file_directory, path)
    return True

special_characters = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '{', '}', '[', ']', '|', '\\', '/', ':', ';', "'", '<', '>', ',', '.', '?']
@app.command()
def file_namer(file_name : str = None):

    file_name = variable_initialiser(file_name, "enter the name of the file to check it: ") 
    '''
    names files according to convetions specified.
    '''

    ''' output: File '''
    version1 = file_name.replace(" ", "_").replace("-", "_")
    version2 = version1.lower()
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
    number(version2[0])
    print(version2)
    return version2


    

            
@app.command()
def file_puller(name : str = None , project_directory: str = None )   :
    '''
    checks in which stage the file can be found
    '''
    
    name = variable_initialiser(name, "enter the name of the file: ") 
    project_directory = variable_initialiser(project_directory, "enter the directory of the project: ") 

    def stage_maker(s):
        return os.path.join(project_directory, s)
    def which_stage(stage_name: str): 
        if name in os.listdir(stage_maker(stage_name)):
           print(stage_name)
           
    which_stage("1_data_collection")
    which_stage("2_training")
    which_stage("3_evaluation")
    which_stage("4_deployment")

@app.command()
def new_data( name : str = None  , project_directory: str = None ):   
    '''
    adds new data source folder in the data collection stage.
    '''
    name = variable_initialiser(name, "enter the name of the new source: ") 
    project_directory = variable_initialiser(project_directory, "enter the directory of the project: ") 
    try: 
        os.chdir(project_directory)
    except: 
        print("error, directory wrong")

    try: 
        os.makedirs(os.path.join(project_directory, "1_data_collection" , name))
    except: 
        print("error, file already exists")
    else: 
        name = file_namer(name)
        os.makedirs(os.path.join(project_directory, "1_data_collection" , name))

    
@app.command()
def new_model( name : str = None , project_directory: str = None):
    '''
    adds a new model folder in the training stage.
    '''
    name = variable_initialiser(name, "enter the name of the new model: ") 
    project_directory = variable_initialiser(project_directory, "enter the directory of the project: ")  
    try: 
        os.chdir(project_directory)
    except: 
        print("error, directory wrong")

    try: 
        os.makedirs(os.path.join(project_directory, "2_training" , name))
    except: 
        print("error, file already exists")
    else: 
        name = file_namer(name)
        os.makedirs(os.path.join(project_directory, "2_training" , name))

@app.command()
def follows_convention(s : str = None): 
    s = variable_initialiser(s, "enter the name of the new source: ") 
    '''checks if name follows convention '''
    if s[0] in special_characters or s[0] == " " or s.isupper:
        print("the name does not follow the conventions, it should be: ")
        file_namer(s)
        return False
    else: 
        if len(s) == 1:
            print("the name follows the conventions! ") 
            return True
        else: 
            follows_convention(s[1: ])
@app.command()
def parameters(fun = None):

    fun = variable_initialiser(fun, "enter the name of the function: ")  
    '''
    call it with command name to check its paramters
    '''
    def result(a, b): 
        if fun == a: 
            print(b)
    result("project-creator", "1. name of project , 2. directory where to save")
    result("file-mover", "1. directory of the file , 2. directory of the project, 3. Name of  one of the 4 stages where to save the new file, e.g: 1_data_collection")
    result("file-namer", "1. name of file")
    result("new-data", "1. name of new data, 2. project directory")
    result("new-model", "1. name of new model, 2. project directory")
    result("follows-convention", "1. name of file")
    result("file-puller", "1. name of new data, 2. project directory")

def name_puller(name): 
    los = list(name.split("/"))
    reverse_los = list(reversed(los))
    file_name = reverse_los[0]
    print(file_name)
    return file_name

def name_puller_without_ext(name): 
    los = list(name.split("/"))
    reverse_los = list(reversed(los))
    file_name = reverse_los[0]
    los2 = list(reversed(list(file_name.split("."))))
    file_name = los2[1]
    return file_name

def file_type_puller(file_name):
    los2 = list(reversed(list(file_name.split("."))))
    file_type = "." + los2[0]
    print(file_type)
    return file_type

@app.command()
def new_version(file_host_directory: str = None , version_number: int = None):
    file_host_directory = variable_initialiser(file_host_directory, "enter the host directory of your file: ")
    version_number = variable_initialiser(version_number, "which version is this? ")
    file_name = name_puller(file_host_directory)
    file_type = file_type_puller(file_name)
    file_name_without_ext = name_puller_without_ext(file_host_directory)
    version_add =  "_v" + str(version_number)
    print("according to the conventions, all versions of the file must be in a directory, do you ")
    directory_exists = input("Does this directory of your file already exist? (y/n) ")
    directory_exists = directory_exists.lower()
    if directory_exists == "y": 
        directory = input("enter the version directory of this file: ")
        
        shutil.move(file_host_directory, directory)
        os.chdir(directory)
        os.rename(file_name, file_name_without_ext + version_add + file_type )
        os.chdir("../")
        directory_name = file_name_without_ext + "_versions"
        os.rename(directory, directory_name)

    if directory_exists== "n":
        project = input('enter where you want to save the new version directory: ')
        path_to_verdir = os.path.join(project, file_name_without_ext + "_versions")
        os.makedirs(path_to_verdir)
        os.chdir(path_to_verdir)
        shutil.move(file_host_directory, path_to_verdir) 
        os.rename(file_name, file_name_without_ext + version_add + file_type )
    

    




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



