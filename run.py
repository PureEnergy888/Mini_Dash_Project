from dash import html, dcc
from dash.dependencies import Input, Output, State
import csv

# Connect to main app.py file
from main import app

# Connect to your app pages
from pages import login, reg

# Connect the navbar to the index
from components import navbar

# define the navbar
nav = navbar.Navbar()

# Define the index page layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='page-content', children=[]),
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/login':
        return login.layout
    if pathname == '/reg':
        return reg.layout
    else:
        return "Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=True)
