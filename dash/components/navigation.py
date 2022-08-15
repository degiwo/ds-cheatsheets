import dash
import dash_bootstrap_components as dbc
from dash import dcc, html


def simple_links():
    return html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}",
                    href=page["relative_path"],
                )
            )
            for page in dash.page_registry.values()
        ]
    )


# NOTE: this horizontal bar can be integrated directly in the application
def horizontal_navigation():
    return html.Div(
        dbc.NavbarSimple(
            [
                dbc.NavItem(
                    dbc.NavLink(
                        page["name"],
                        href=page["path"],
                        active="exact",
                    )
                )
                for page in dash.page_registry.values()
            ],
            brand="Template application",
            color="primary",
            dark=True,
            links_left=True,
        )
    )
