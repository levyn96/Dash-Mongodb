# index page
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from server import app, server
from flask_login import logout_user, current_user
from pages import success, login, login_fd, logout, ProjectsMainScreen, add_user, FullProjectPage
# Loading screen CSS
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/brPBPO.css"})
header = html.Div(
    className='header',
    children=html.Div(
        # className='container-width',
        style={'height': '100%', 'width': '100%', 'background-color': '#333333'},
        children=[
            html.Img(
                style={'margin-left': '100px', 'height': '100%', 'width': '10%'},
                src='assets/header.jpeg',
                className='logo'
            ),
            html.Div(className='links', children=[
                html.Div(id='user-name', className='link', style={'background-color': '#333333', 'color': '#F7B710'}),
                html.Div(id='logout', className='link', style={'background-color': '#333333', 'color': '#F7B710'}),
                html.Div(id='add-user', className='link',
                         style={'background-color': '#333333', 'color': '#F7B710', 'margin-right': '100px'})
            ])
        ]
    )
)

app.layout = html.Div(
    [
        header,
        html.Div([
            html.Div(
                html.Div(id='page-content', className='content'),
                className='content-container'
            ),
        ], className='container-width'),
        dcc.Location(id='url', refresh=False),
    ]
)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    try:
        split_path = pathname.split('/')
        print(split_path, ', ', len(split_path))
    except:
        split_path = ''
        pass
    if (len(split_path)) > 2:
        if split_path[1] == 'project-page' and current_user.is_authenticated:
            return FullProjectPage.layout(split_path[2])
        else:
            return login_fd.layout
    if pathname == '/':
        return login.layout
    elif pathname == '/login':
        return login.layout
    elif pathname == '/success':
        if current_user.is_authenticated:
            return success.layout
        else:
            return login_fd.layout
    elif pathname == '/Projects':
        if current_user.is_authenticated:
            return ProjectsMainScreen.layout()
        else:
            return login_fd.layout
    elif pathname == '/add-user':
        if current_user.is_authenticated:
            return add_user.layout
        else:
            return login_fd.layout
    elif pathname == '/logout':
        if current_user.is_authenticated:
            logout_user()
            return logout.layout
        else:
            return logout.layout
    else:
        return '404'


@app.callback(
    Output('user-name', 'children'),
    [Input('page-content', 'children')])
def cur_user(input1):
    if current_user.is_authenticated:
        return html.Div('Current user: ' + current_user.username)
        # 'User authenticated' return username in get_id()
    else:
        return ''


@app.callback(
    Output('logout', 'children'),
    [Input('page-content', 'children')])
def user_logout(input1):
    if current_user.is_authenticated:
        return html.A('Logout', href='/logout')
    else:
        return ''


@app.callback(
    Output('add-user', 'children'),
    [Input('page-content', 'children')])
def adding_user(input1):
    if current_user.is_authenticated:
        return html.A('Add User', href='/add-user')
    else:
        return ''


if __name__ == '__main__':
    app.run_server(host='localhost', debug=True)
