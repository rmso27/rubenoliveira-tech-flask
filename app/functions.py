#######################
#   GENERAL CONFIGS
#######################

# Import modules
import datetime

#######################
#   FUNCTIONS
#######################

# Function to get_date (year) used on template footer
def get_date():

    current_date = datetime.datetime.now()
    current_year = current_date.year

    return current_year
