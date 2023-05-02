import wof.utils as utils


def test_load_projects(test_projects, test_projects_df):
    assert utils.load_projects(test_projects).equals(test_projects_df)


def test_add_project(
    test_projects,
    appended_test_projects_df,
    added_test_project,
):
    project_df = utils.load_projects(test_projects)

    assert utils.add_project(project_df, added_test_project).equals(
        appended_test_projects_df
    )

def test_delete_project(test_projects_df, appended_test_projects_df, added_test_project):
    assert utils.delete_project_by_name(appended_test_projects_df, added_test_project["Name"]).equals(test_projects_df)
