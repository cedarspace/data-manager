
import os
import shutil

def project_creator():
    '''
    creates a new project directory.
    '''

    ''' getting the data and testing its validity'''
    name: str = input("insert a name for your project: ")
    directory: str = input("insert the directory that will host your project: ")


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
    


def move_file():
    project_directory : str = input("enter the project directory: ")
    file_directory : str = input("enter the file directory: ")
    stage : str = input("in which stage would you like to put it? ")
    path = os.path.join(project_directory, stage.lower())

    if os.getcwd() != project_directory:
        os.chdir(project_directory)

    shutil.move(file_directory, path)