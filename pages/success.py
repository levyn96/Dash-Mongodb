import warnings
# Dash configuration
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from server import app

warnings.filterwarnings("ignore")
numberOfIntervals = 0
# Create success layout
layout = html.Div(children=[
    dcc.Location(id='url_login_success', refresh=True),
    html.Div(
        className="container",
        children=[
            html.Div(
                html.Div(
                    className="row",
                    children=[
                        html.Div(
                            className="ten columns",
                            children=[
                                html.Br(),
                                html.Div(['Success!!']),
                            ]
                        ),
                        # html.Div(
                        #     className="two columns",
                        #     # children=html.A(html.Button('LogOut'), href='/')
                        #     children=[
                        #         html.Br(),
                        #         html.Button(id='back-button', children='Go back', n_clicks=0)
                        #     ]
                        # ),
                        dcc.Interval(
                            id='interval-component',
                            interval=1 * 1000,  # in milliseconds
                            n_intervals=0),

                    ]
                )
            )
        ]
    )
])


# Create callbacks
# @app.callback(Output('url_login_success', 'pathname'),
#               [Input('back-button', 'n_clicks')])
# def logout_dashboard(n_clicks):
#     if n_clicks > 0:
#         return '/Projects'

@app.callback(Output('url_login_success', 'pathname'),
              [Input('interval-component', 'n_intervals')])
def logout_dashboard(n_intervals):
    if n_intervals == 2:
        return '/Projects'
