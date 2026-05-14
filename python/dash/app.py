import dash
import dash_bootstrap_components as dbc
from dash import Dash, html

from components.navigation import horizontal_navigation

app = Dash(
    __name__,
    use_pages=True,
    assets_folder="assets",  # NOTE: this is the default
    external_stylesheets=[dbc.themes.DARKLY],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)
app_serv = app.server  # NOTE: This and launch.json enables debugging with F5


app.layout = html.Div(
    [
        horizontal_navigation(),
        # NOTE: display the layouts in 'pages' folder
        dbc.Container(dash.page_container),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
