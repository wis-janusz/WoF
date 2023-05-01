import utils

path = 'projects.yml'

projects = utils.load_projects(path)

utils = utils.choose_project(projects)

print(utils + ' (' + projects[utils] + ')')
