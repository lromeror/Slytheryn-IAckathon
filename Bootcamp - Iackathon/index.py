import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import os

import pandas as pd
import numpy as np

app = dash.Dash(__name__)
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

Path_images = "assets/logos"
#planning = pd.read_csv("../planning2015-2023_M.csv")
#tender = pd.read_csv("../tender2015-2023.csv")
#releases  = pd.read_csv("../releases2015-2023.csv")
#contracts  = pd.read_csv("../contracts2015-2023.csv")

header = dbc.Row(
            [
                dbc.Col(html.Img(src="assets/logos/logo1.png", height="41px",className="col1_1")),
                dbc.Col(html.H5("Contrataciones Abiertas Ecuador - DashBoard"),style={"font-size":"2vw"},className="col1_1 texto-bonito"),
                dbc.Col(html.Img(src="assets/logos/ecuador.png", height="70px",className="col1_1")),
            ],
            align='center',
            justify='space-between',    
            style={'justifyContent':'space-around'},
            className="Header g-0"
)
aside = html.Div([
    dbc.Button([
        html.Div([html.Img(src=os.path.join(Path_images,"aside1.png"),height="30px")], className="menu-icon"),
        html.Div("INFO", className="menu-text"),
    ], id="home", className="menu-item"),
    dbc.Button([
        html.Div([html.Img(src=os.path.join(Path_images,"aside1.png"),height="30px")], className="menu-icon"),
        html.Div("AGREGAR2", className="menu-text"),
    ], id="search", className="menu-item"),
    dbc.Button([
        html.Div([html.Img(src=os.path.join(Path_images,"aside1.png"),height="30px")], className="menu-icon"),
        html.Div("AGREGAR", className="menu-text"),
    ], id="settings", className="menu-item"),
], id="aside", className="aside-closed")


#Info = dbc.Container([
#    dbc.Row([
#        dbc.Col([
#            dcc.Dropdown(
#                id='OCID',
#                options=sorted(contracts.NOMBRE.unique().tolist()),style={'margin-bottom': '30px'},
#                value=sorted(contracts.NOMBRE.unique().tolist())[1]
#            )
#        ]),
#        dbc.Col([])
#    ]),])
app.layout = html.Div([
    header,
    aside,
    html.Div(id="body_page",className="content")
])
if __name__ == '__main__':
    app.run_server(debug=True)
