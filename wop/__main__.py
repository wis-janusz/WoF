from dash import Dash, html, dash_table, dcc, callback, Input, Output, State
import plotly.express as px
import pandas as pd
import utils


app = Dash("WoP")


local_projects_path = "local_projects.json"
in_projects = utils.load_projects(local_projects_path)
choice = in_projects.sample()


app.layout = html.Div([
    html.Div(children='Local Projects'),
    html.Hr(),
    dash_table.DataTable(in_projects.to_dict('records'), [{"name": i, "id":i} for i in in_projects.columns], editable=True, id = "projects-table", persistence=True, persisted_props=["data"]),
    html.Button('Add new project', id ='add-button'),
    html.Button('Save changes', id = 'save-button'),
    html.Hr(),
    dcc.RadioItems(options=["Type","Completed"], value="Type", id="histogram-data-buttons"),
    dcc.Graph(figure={}, id="histogram-graph"),
    html.Div(children='Randomly Chosen Project'),
    dash_table.DataTable(data=choice.to_dict('records'), page_size=10),

    dcc.Store(id='stored-table'),

    html.Div(id='hidden-div', style={'display':'none'})
])


# @callback(
#         Output(component_id="stored-table", component_property="data"),
#         Input(component_id="projects-table", component_property="data")
# )
# def store_table(projects_table):
#     return projects_table

@callback(
    Output(component_id='projects-table', component_property='data'),
    Input(component_id='add-button', component_property='n_clicks'),
    State(component_id='projects-table', component_property='data'),
    State(component_id='projects-table', component_property='columns')
)
def add_project(n_clicks, rows, columns):
    if n_clicks:
        rows.append({c['id']:'' for c in columns})
    return rows

@callback(
    Output(component_id='hidden-div', component_property='children'),
    State(component_id='projects-table', component_property='data'),
    Input(component_id='save-button', component_property='n_clicks'),
)
def save_table(projects_table, n_clicks):
    if n_clicks:
        projects_df = pd.DataFrame(projects_table)
        utils.save_projects(local_projects_path, projects_df)


@callback(
    Output(component_id="histogram-graph", component_property="figure"),
    Input(component_id="projects-table", component_property="data"),
    Input(component_id="histogram-data-buttons", component_property="value")
)
def update_graph(projects_table, displayed_column):
    fig = px.histogram(projects_table, x=displayed_column)
    return fig


if __name__ == '__main__':
    app.run_server(debug = True)

