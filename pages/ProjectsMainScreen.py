from pymongo import MongoClient
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
import pathlib
import dash_table
from server import app
# from mongo import get_projects_documents


def layout():
    client = MongoClient()
    db = client["projects_db"]  # change this to your DB name
    projects_collection = db["ProjectsCollection"]  # changes this to your collection
    print("came from mongo: {}".format(projects_collection.find()))
    exclude_col = {'_id': False}  # we are ignoring '_id' column.
    data = list(projects_collection.find({}, projection=exclude_col))  # data is in json format
    col_list = list(data[0].keys())
    print(data)
    print(col_list)
    # df = pd.DataFrame(list(projects_collection.find()))
    df = pd.DataFrame(data, columns=col_list)

    print("this is the data frame : ")
    print(df.to_string())


    '''
    layout
    '''
    return html.Div([
        dcc.Location(id='url_projects', refresh=True),

        html.Div(id='message-div'),
        html.Div(
            [
                # html.Div([
                #     html.Img(src='/assets/header.jpeg')
                #     ], style={'float': 'right'}
                # ),
                dash_table.DataTable(
                    id='datatable-interactivity',
                    columns=[
                        {"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns
                    ],
                    style_cell={'textAlign': 'left'},
                    data=df.to_dict('records'),
                    editable=True,
                    filter_action="native",
                    sort_action="native",
                    sort_mode="multi",
                    column_selectable="single",
                    row_selectable="single",
                    row_deletable=True,
                    selected_columns=[],
                    selected_rows=[],
                    page_action="native",
                    page_current=0,
                    page_size=10,
                ),
                html.Div(id='datatable-interactivity-container')

           ], className='container-width'

        ),
        html.Div(
            [
                dbc.Button("Add", id="add-project-modal"),
                dbc.Modal(
                    [
                        dbc.ModalHeader("project data"),
                        dbc.ModalBody(html.Div(
                            [
                                dbc.InputGroup(
                                    [
                                        dbc.Input(placeholder="project ID",
                                                  id="add-project-number-id"),

                                    ],
                                    className="mb-3",
                                ),
                                dbc.InputGroup(
                                    [
                                        dbc.Input(placeholder="project name",
                                                  id="add-project-name"),

                                    ],
                                    className="mb-3",
                                ),
                                dbc.InputGroup(
                                    [
                                        dbc.Input(placeholder="worker",
                                                  id='add-project-worker'),
                                    ],
                                    className="mb-3",
                                ),
                                dbc.InputGroup(
                                    [
                                        dbc.Input(placeholder="address",
                                                  id='add-project-address'),
                                    ],
                                    className="mb-3",
                                ),
                                dbc.InputGroup(
                                    [
                                        dbc.Input(placeholder="developer",
                                                  id='add-project-realestatedeveloper'),
                                    ],
                                    className="mb-3",
                                ),
                                dbc.InputGroup(
                                    [
                                        dbc.Input(placeholder="report number",
                                                  id='add-project-reportnumber'),

                                    ],
                                    className="mb-3",
                                ),
                            ]
                        )
                                       ),
                        dbc.ModalFooter(
                            [dbc.Button(
                                "Submit", id="submit-project-modal", className=
                                "ml-auto"
                            ),
                            dbc.Button(
                                "Close", id="close-project-modal", className=
                                "ml-auto"
                            ),
                            ],
                        ),
                    ],
                    id="modal-centered",
                    centered=True,
                ),
            ],style={'margin-top': '20px'},
        )
    ]
    )


@app.callback(
    Output("modal-centered", "is_open"),
    [Input("add-project-modal", "n_clicks"),
     Input("close-project-modal", "n_clicks"),
     ],
    # I was drunk writting this piece of code; the idea was submitting the new project values and adding them to mongodb
    [State("modal-centered", "is_open")]
)
def toggle_modal(add_n, close_n, is_open):
    if add_n or close_n:
        return not is_open
    return is_open

@app.callback(
    Output('message-div', 'children'),
    [Input('submit-project-modal', 'n_clicks')],
    [State('add-project-number-id', 'value'),
     State('add-project-name', 'value'),
     State('add-project-worker', 'value'),
     State('add-project-address', 'value'),
     State('add-project-realestatedeveloper', 'value'),
     State('add-project-reportnumber', 'value'),
      ]
)
def submit_new_project(submit, project_id, project_name, project_worker, project_address, real_estate_developer,
                 report_number):

    if project_id and project_name and  project_worker and project_address and real_estate_developer and report_number:
        client = MongoClient()
        db = client["Kaveret"]
        projects_collection = db["ProjectsCollection"]
        projects_collection.insert_one({"ID": project_id,
                                        "worker": project_worker,
                                        "status": "new",
                                        "name": project_name,
                                        "address": project_address,
                                        "RealEstateDeveloper": real_estate_developer,
                                        "ReportNumber": report_number,
                                        "notifications": 0
                                        })
        return "project added "
    else:
        return ""



@app.callback(
    Output('datatable-interactivity', 'style_data_conditional'),
    [Input('datatable-interactivity', 'selected_columns')]
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]


@app.callback(
    Output('url_projects', 'pathname'),
    [Input('datatable-interactivity', 'selected_row_ids'),
     Input('datatable-interactivity', 'active_cell'),
     Input('datatable-interactivity', 'derived_virtual_row_ids')])
def update_graphs(selected_row_ids, active_cell, row_ids):
    print(selected_row_ids, active_cell)
    if selected_row_ids == '[None]' or selected_row_ids == None:
        pass
    else:
        return '/project-page/{}'.format(selected_row_ids)