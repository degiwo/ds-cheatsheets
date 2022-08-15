import dash
from dash import Input, Output, dcc, html

# NOTE: with register_page Dash can integrate the file in app.py
dash.register_page(
    __name__,
    path="/",
    title="Template application - Home",
    order=0,
)


# NOTE: function need to be named layout, but can also be a variable
def layout():
    return html.Div(
        [
            html.H1("Home"),
            dcc.RadioItems(["1", "2", "3"], 1, id="input-number"),
            html.Div(id="output-number"),
        ]
    )


# NOTE: use @dash.callback instead of @app.callback
# otherwise an error occurs because app is not available during module import
@dash.callback(
    Output(component_id="output-number", component_property="children"),
    Input(component_id="input-number", component_property="value"),
)
def update_output_number(input_number):
    return f"You selected {input_number}"
