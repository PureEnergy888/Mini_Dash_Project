# Import necessary libraries
from main import app
import csv
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

layout = html.Div([
    html.H2('Registration'),
    html.Div([
        html.Label('Username'),
        dcc.Input(
            id='username-input',
            type='text',
            placeholder='Enter a username'
        )
    ]),
    html.Div([
        html.Label('Password'),
        dcc.Input(
            id='password-input',
            type='password',
            placeholder='Enter a password'
        )
    ]),
    html.Div([
        html.Label('email'),
        dcc.Input(
            id='email-input',
            type='email',
            placeholder='Enter your email'
        )
    ]),
    html.Div([
        html.Label('firstname'),
        dcc.Input(
            id='first-input',
            type='text',
            placeholder='Enter your first name'
        )
    ]),
    html.Button('Register', id='register-button'),
    html.Div(id='registration-message')
])


@app.callback(Output('registration-message', 'children'),
              [Input('register-button', 'n_clicks')],
              [State('username-input', 'value'), State('password-input', 'value')])
def register_user(n_clicks, username, password):
    if n_clicks:
        # Open the CSV file and append the new username and password
        with open('users.csv', mode='a') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])

        return f'User {username} has been registered.'
