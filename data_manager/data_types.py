class project():
    
    def __init__(self, name: str , directory: str): 
        '''
        Intp. Project consists of its name and the directory. 
        
        '''
        self.name = name
        self.directory = directory

example_project = project("Speech_Recognition",
                           "/Users/cedarspace/Desktop/Soghmon_files" )


class txt_file():
    
    def __init__(self, name: str): 
        ''' 
        Intp. File is a String that contains the name 
        of the file and .txt.  
        
        '''
        self.name = (name + ".txt")

txt_file_example = txt_file("john")

'''
##Stage## 
Stage is one of: 
 - "data-collection" 
- "training"
- "evaluation" 
- "deployment"
Stage is one of four stirngs rperesenting the stage of a machine learning project
'''

