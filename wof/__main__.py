import utils

local_projects_path = "local_projects.json"
projects = utils.load_projects(local_projects_path)
choice = projects.sample()
print(choice)
