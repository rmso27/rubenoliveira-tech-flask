#######################
#   GENERAL CONFIGS
#######################

# Import modules
import datetime
import configparser
import json

# Set variables
config = configparser.ConfigParser()
config.read('configs/config.ini')

# Read configurations
list_of_projects = config['data']['DATA_PROJECTS']

#######################
#   FUNCTIONS
#######################

# Function to get_date (year) used on template footer
def get_date():

    current_date = datetime.datetime.now()
    current_year = current_date.year

    return current_year

# Function to get_projects
def get_projects():

    with open(list_of_projects + 'projects.json', encoding='utf-8') as loaded_data:
        data = json.loads(loaded_data.read())

    project_name = []
    project_description = []
    project_url = []
    project_git = []

    for project in range(len(data['projects'])):
        project_name += [data['projects'][project]['name']]
        project_description += [data['projects'][project]['description']]
        project_url = [data['projects'][project]['url']]
        project_git = [data['projects'][project]['git']]

    return project_name, project_description, project_url, project_git


