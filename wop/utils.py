import pandas as pd


def load_projects(project_filename):
    with open(project_filename, "r") as in_file:
        project_df = pd.read_json(in_file)
    return project_df


def save_projects(project_filename, project_df: pd.DataFrame):
    with open(project_filename, "w") as out_file:
        project_df.to_json(out_file)


def add_project(project_df: pd.DataFrame, project_as_dict):
    project_df.loc[len(project_df)] = project_as_dict
    return project_df


def delete_project_by_name(project_df: pd.DataFrame, project_name):
    project_df = project_df[project_df["Name"] != project_name]
    return project_df
