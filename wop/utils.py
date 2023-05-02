import pandas as pd


def load_projects(project_filename):
    with open(project_filename, "r") as in_file:
        project_df = pd.read_json(in_file)
    return project_df


def save_projects(project_filename, project_df: pd.DataFrame):
    with open(project_filename, "w") as out_file:
        project_df.to_json(out_file)

