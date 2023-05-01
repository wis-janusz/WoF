import wof.utils as utils

def test_load_projects(test_projects, test_projects_dict):
    assert utils.load_projects(test_projects) == test_projects_dict

def test_choose_projects(test_projects, test_projects_dict):
    project_dict = utils.load_projects(test_projects)
    assert utils.choose_project(project_dict) in test_projects_dict.keys()

def test_add_project(test_projects, appended_test_projects, appended_test_projects_dict, added_test_project):
    project_dict = utils.load_projects(test_projects)
    utils.add_project(project_dict, appended_test_projects,added_test_project[0], added_test_project[1])
    assert utils.load_projects(appended_test_projects) == appended_test_projects_dict
