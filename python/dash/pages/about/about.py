import dash
from dash import html

# NOTE: with register_page Dash can integrate the file in app.py
dash.register_page(__name__, order=2)


# NOTE: function need to be named 'layout', but can also be a variable
def layout():
    return html.Div(
        [
            html.H1("About"),
            # NOTE: Dash can find assets automatically in the 'assets' folder
            html.Img(src=dash.get_asset_url("python.png"), height="50px"),
            html.P("This is a paragraph."),
        ]
    )
