from dash import Dash, html, dash_table
import utils

local_projects_path = "local_projects.json"
projects = utils.load_projects(local_projects_path)
choice = projects.sample()

app = Dash("WoP")

app.layout = html.Div([
    html.Div(children='Local Projects'),
    dash_table.DataTable(data=projects.to_dict('records'), page_size=10),
    html.Div(children='Randomly Chosen Project'),
    dash_table.DataTable(data=choice.to_dict('records'), page_size=10)
])

if __name__ == '__main__':
    app.run_server(debug = True)

