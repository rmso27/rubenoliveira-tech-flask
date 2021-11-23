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

    data = open(list_of_projects + 'projects.json', 'r', encoding='utf-8')

    for project in range(len(data)):
        print(['projects'][project]['name'])

    return 0


