import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

# NOTE: with register_page Dash can integrate the file in app.py
dash.register_page(__name__, order=1)


# NOTE: function need to be named layout, but can also be a variable
def layout():
    return html.Div(
        [
            html.H1("Overview"),
            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Dropdown(["A", "B", "C"]),
                                width=3,
                            ),
                            dbc.Col(
                                html.Div(
                                    "Test",
                                    style={
                                        "background-color": "lightgrey",
                                        "color": "black",
                                    },
                                ),
                                width=9,
                            ),
                        ]
                    ),
                ]
            ),
        ]
    )
