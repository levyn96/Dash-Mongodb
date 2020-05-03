import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from server import app


def layout(project_id):
     return html.Div(
        children=[
            html.Div(
                className="container",
                children=[
                    dcc.Location(id='url_add-user', refresh=True),
                    html.Div('''you made it!''', id='h1'),
                    html.Div("page {}".format(project_id))
                ]
            )
        ]
    )

