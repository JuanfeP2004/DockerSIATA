import pandas as pd
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State

url = "http://localhost:5000/mostrarEstacionesNivel?pass=orlios"
data = pd.read_json(url, convert_dates='True')

latA = []
lonA = []
zA = []

# App y las Contraseñas

app = dash.Dash()
usuarios = {"admin":"root", "user":"pass01"}

# Plantilla del login

form = html.Div([
    html.H1("Control de cauce en Medellin"),
    html.Br(),
    "Ingrese el usuario: ",
    dcc.Input(id="usuario", type="text"),
    "Ingrese la contraseña: ",
    dcc.Input(id="contrasenia", type="text"),
    html.Hr(),
    html.Button("Ingresar", id="ingresar", type="submit", n_clicks=0),
    html.Hr(),
    html.Div(id="login")
    ])

# Plantilla del mapa de las estaciones

for i in range(0, 100):
    zA.append(data['datos'][i]['porcentajeNivel'])
    latA.append(data['datos'][i]['coordenadas'][0]['latitud'])
    lonA.append(data['datos'][i]['coordenadas'][0]['longitud'])

fig = go.Figure(go.Densitymapbox(lat=latA, lon=lonA, z=zA, radius=20, opacity=0.9, zmin=0, zmax = 100))
fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=-75.589, mapbox_center_lat=6.2429)
fig.update_layout(margin={"r":0, "t":0, "l":0, "b":0})

mapa = html.Div([
            dcc.Graph(figure=fig)
            ])

# Zona del callback, donde se obtiene la interaccion con el formulario

@app.callback(Output("login", "children"),
    Input("ingresar", "n_clicks"),
    State("usuario", "value"),
    State("contrasenia", "value"))

# Zona del boton donde esta el codigo al actualizar

def update_output(n_clicks, usuario, contrasenia):
    if (usuario in usuarios and contrasenia == usuarios[usuario]):
        return mapa
    elif (n_clicks == 0): return None
    else: return "Usuario o contraseña incorrecto"

# Donde se corre el servidor

app.layout = form
app.run_server(host='0.0.0.0', port=80)