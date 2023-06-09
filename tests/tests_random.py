import os

def file_puller(name : str, project_directory: str):
    '''
    !!!
    pulls a file from project and stage specified.
    '''
    def stage_maker(s):
        return os.path.join(project_directory, s)
    def which_stage(stage_name: str): 
        if name in os.listdir(stage_maker(stage_name)):
           print(stage_name)
           
    which_stage("1_data_collection")
    which_stage("2_training")
    which_stage("3_evaluation")
    which_stage("4_deployment")



file_puller("kwakwala-google " , "/Users/cedarspace/Desktop/Soghmon_files/Data_Management/ocr-post-correction" )
name = "kwakwala-google "
project_directory = "/Users/cedarspace/Desktop/Soghmon_files/Data_Management/ocr-post-correction"
def stage_maker(s):
        return os.path.join(project_directory, s)
def which_stage(stage_name: str): 
    if name in os.listdir(stage_maker(stage_name)):
        print(stage_name)


stage_maker("2_training")
which_stage("2_training")