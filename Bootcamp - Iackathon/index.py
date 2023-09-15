import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import os

app = dash.Dash(__name__)
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

Path_images = "assets/logos"

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



app.layout = html.Div([
    header,
    aside,
    html.Div(id="body_page",className="content")
])
if __name__ == '__main__':
    app.run_server(debug=True)
