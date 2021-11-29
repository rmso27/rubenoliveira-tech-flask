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

# Read configurations (config.ini file)
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

    return data


