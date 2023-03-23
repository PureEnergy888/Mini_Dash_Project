# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc


# Define the navbar structure
def Navbar():

    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Login", href="/login")),
                dbc.NavItem(dbc.NavLink("Register", href="/reg")),
            ] ,
            brand="Mini",
            brand_href="/run",
            color="dark",
            dark=True,
        ), 
    ])

    return layout
