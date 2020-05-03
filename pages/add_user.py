import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import time

from server import app, User
from flask_login import login_user
from werkzeug.security import check_password_hash
from users_mgt import add_new_user

layout = html.Div(
    children=[
        html.Div(
            className="container",
            children=[
                dcc.Location(id='url_add-user', refresh=True),
                html.Div('''Please fill in the information to continue:''', id='h1'),
                html.Div(
                    # method='Post',
                    children=[
                        dcc.Input(
                            placeholder='Enter new username',
                            type='text',
                            id='new-uname-box'
                        ),
                        dcc.Input(
                            placeholder='Enter your E-mail',
                            type='text',
                            id='new-email-box'
                        ),
                        dcc.Input(
                            placeholder='Enter new password',
                            type='password',
                            id='new-pwd-box'
                        ),
                        html.Button(
                            children='Add User',
                            n_clicks=0,
                            type='submit',
                            id='sign-up-button'
                        ),
                        html.Div(children='', id='output-result')
                    ]
                ),
            ]
        )
    ]
)


@app.callback(Output('output-result', 'children'),
              [Input('sign-up-button', 'n_clicks')],
              [State('new-uname-box', 'value'),
               State('new-pwd-box', 'value'),
               State('new-email-box', 'value')])
def create_user(n_clicks, username, password, email):
    if username is not None:  # first time user gets in the page, we get in this callback and parameters are None - BAD!
        user = User.query.filter_by(username=username).first()
        if user:
            return "user exists!"
        else:
            print('username:{} '
                  'password:{} '
                  'E-mail:{} '.format(username, password, email))
            add_new_user(username, password, email)
            return "created new user!"
            pass
    else:
        return


@app.callback(Output('url_add-user', 'pathname'),
              [Input('sign-up-button', 'n_clicks')],
              [State('new-uname-box', 'value'),
               State('new-pwd-box', 'value')])
def update_output(n_clicks, input1, input2):
    if n_clicks > 0:
        user = User.query.filter_by(username=input1).first()
        if user:
            return '/add-user'
        else:
            time.sleep(1)
            return '/Projects'
