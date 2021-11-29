#######################
#   GENERAL CONFIGS
#######################

# Import modules
from flask import request, render_template
from app import app

# Import functions
from .functions import get_date, get_projects

#######################
#   ROUTES
#######################

# 'Home' route
@app.route('/')
def home():

    year = get_date()

    return render_template('public/index.html', year = year)

# 'About' route
@app.route('/about')
def about():

    year = get_date()

    return render_template('public/about.html', year = year)

# 'Projects' route
@app.route('/projects')
def projects():

    year = get_date()
    p_name, p_description, p_url, p_git = get_projects()

    return render_template('public/projects.html', year = year, names = p_name, descriptions = p_description, urls = p_url, gits = p_git)