import wop.utils as utils


def test_load_projects(test_projects, test_projects_df):
    assert utils.load_projects(test_projects).equals(test_projects_df)


