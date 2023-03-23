# Import necessary libraries
import csv
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from main import app

# Define the page layout
layout = html.Div([
    html.H2('Login'),
    html.Div([
        html.Label('Username'),
        dcc.Input(
            id='username-input',
            type='text',
            placeholder='Enter your username'
        )
    ]),
    html.Div([
        html.Label('Password'),
        dcc.Input(
            id='password-input',
            type='password',
            placeholder='Enter your password'
        )
    ]),
    html.Button('Submit', id='submit-button'),
    html.Div(id='login-message'),
    dcc.Store(id='login-state', storage_type='local')
])


@app.callback(Output('login-message', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('username-input', 'value'), State('password-input', 'value'),
               State('login-state', 'data')])
def authenticate_user(n_clicks, username, password, login_state):
    if login_state:
        # If the user is already logged in, return a message and set the login state to True
        dcc.Store('login-state').data = True
        return 'You are already logged in.'
    elif n_clicks:
        # Open the CSV file and check if the entered username and password match any rows
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    # If the username and password match a row, set the login state to True
                    dcc.Store('login-state').data = True
                    return 'You have successfully logged in.'

        # If no match was found, return an error message and set the login state to False
        dcc.Store('login-state').data = False
        return 'Invalid login credentials.'

        # If the submit button has not been clicked, check the login state and return a message accordingly
    if login_state:
        return 'You are logged in.'
    else:
        return 'Please log in.'
