# tests/test_rptodo.py
import os
import check_output



def project_creator(
    name : str , 
    directory : str
    ):
    '''
    creates a new project directory.
    '''
    try: 
        isinstance(name, str)
    except: 
        str(name)
    try: 
        #isinstance(directory, str)
        print("name must be string")
    except: 
        str(directory)

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
    try: 
        os.chdir(dirpath)
    except: 
        print("project creation failed")
        return 2
    else: 
        return 0


check_output.check_output_2(project_creator, "spider", "Desktop/Soghomon_files", 2 )
check_output.check_output_2(project_creator, "spider", "/Users/cedarspace/Desktop/Soghmon_files", 0)
check_output.check_output_2(project_creator, 1, "/Users/cedarspace/Desktop/Soghmon_files", 0)


