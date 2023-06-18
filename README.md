# data-manager
Manages data for machine learning projects
data-manager is a CLI that helps in the organization of machine learning projects. The goal is to organize models, raw data, and evaluation files directly after they are produced by writing one line of code. 



Installation

To install the library, go to: https://github.com/cedarspace/data-manager.git and download the repo. 

Go to Terminal and move to the repository by typing: 

cd /path/to/data-manager

Then;

python -m data_manager <command name> 





Getting Started

First, the library will create a directory for the project using the make-project command. In the project directory, there will be 4 directories representing 4 levels of machine learning. The levels are; 

Data Collection: involves storing the different data sets that will be used in the project.

Training: involves storing the models that the training phase produced along with the datasets which were used to train and produce the model. 

Evaluation: involves storing the results of the evaluation of the models produced during training. 

Deployment: involves storing any papers, articles, or interfaces made based on the machine learning project. 

These stages have been created based on researching stages of software projects taking into consideration the stages of any machine learning process.  You can find full details about the research with references here: 

Command References

After the creation of the project’s directory, different commands can be used to manipulate the directory. These comments are as follows;  

- project-creator

creates a new project directory.

name of project , 2. directory where to save

- file-mover:

moves file to specified project and stage. 

directory of the file , 2. directory of the project, 3. Name of  one of the 4 stages where to save the new file, e.g: 1_data_collection

- file-namer: 

names files according to protocols specified in conventions.txt file. 

name of file

- new-version

manages the versions of files according to the protocol in conventions.txt file. 

''Still under construction”

- file-puller

checks in which stage the file can be found in a specified project. 

name of the file , 2. project directory

- new-data

adds new data source folder in the data collection folder of the specified project. 

name of the file , 2. project directory

- new-model

adds new model folder in the data collection folder of the specified project.

name of new model, 2. project directory

- parameters

call it with function names above to check its paramters

<function name>  

- follows-convention

checks if name follows convention

1. name of file

Examples 

For exmaple, if I want to create a project in my ‘'projects’' directory I would type (on a mac): 

python3 -m data_manager project-creator NAME /Users/cedarspace/Desktop/Projects
How many sources does your folder have? 2
enter source 1's name: test_source_1
enter source 2's name: test_source_2
How many models does your folder have? 1
enter model 1's name: test_model_1

that should create a project of the following shape: 

├── Projects
     └── name

          └── 1. data_collection 

           └── 2. training

                 └── test_source_1

                 └── test_source_2 

          └── 3. evaluation  

                 └── test_model_1

          └── 4. deployment 



Notice that naming files has specific conventions stated in the requirements.txt file, one of these conventions is the exclusion of capital letters, which is why the name of the project is “name” and not “NAME”. To check whether the name you want to use meets the conventions you can call the follows-conventions command

python3 -m data_manager file-namer NAME

this will return 

the name does not follow the conventions, it should be: 
name

if you want to name a file according to the conventions you can call file-namer. 

All other commands work similarly. You insert the command name and then its parameters separated by space. 


For questions, you can email saughmon.boujkian@ubc.ca
