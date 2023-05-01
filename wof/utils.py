import yaml
import random

def load_projects(project_filename):
    
    with open(project_filename, 'r') as in_file:
        project_dict = yaml.load(in_file, Loader = yaml.loader.SafeLoader)
    return project_dict

def choose_project(project_dict: dict):
    
    projects = list(project_dict.keys())
    choice = projects[random.randint(0,len(projects)-1)]
    return choice

def add_project(project_dict, project_filename, project_name, project_type):
    
    project_dict[project_name] = project_type
    with open(project_filename, 'w') as out_file:
        yaml.dump(project_dict, out_file)
        

