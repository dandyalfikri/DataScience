import plotly.express as px
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app #change this line

# Data Preprocessing
df = pd.read_csv('supermarket_sales_cleaned.csv')

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Graph penjualan supermarket berdasarkan kota"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Visualisasi graph untuk supermarket berdasarkan kota, dan tipe customer'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='selected_city',
                    options=[
                       {'label': city, 'value': city} for city in df['City'].unique()
                    ],
                    value='Yangon',
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.RadioItems(
                    id='customer_type',options=[
                        {'label': ' Member & non Member', 'value': 0},
                        {'label': ' Member', 'value': 1},
                        {'label': ' non Member', 'value': 2}
                    ],
                    value=0,
                    labelStyle={'display': 'block'}
                ),
                className='mb-4'
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='main-graph'
                )
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='second-graph'
                )
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H4(children='Gunakan slider di bawah graph untuk memperluas/mempersempit graph',
                className="mb-4"),className='text-center')
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='third-graph'
                )
            ),
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='fourth-graph'
                )
            )
        ])
    ])
    
])


@app.callback(
    Output('main-graph', 'figure'),
    Input('selected_city', 'value'),
    Input('customer_type', 'value')
)
def plot_jp(data,mem=0): #plotting jenis produk
    data = df[df['City'] == data]
    if mem == 1:
        pl = data['Product line'][data['Customer type'] == 'Member'] #Untuk filtering member
    elif mem == 2:
        pl = data['Product line'][data['Customer type'] == 'Normal'] #Untuk filtering normal
    else:
        pl = data['Product line'] #Kombinasi antara member dan normal
    fig = px.bar(pl,x=pl.value_counts().index,y=pl.value_counts(),width=1200,height=500,
                 color=pl.unique(),title='Jumlah jenis produk terjual',
                 labels={
                     'x': 'Jenis Produk',
                     'y': 'Kuantitas',
                     'color': 'Jenis Produk'
                 })
    return fig

@app.callback(
    Output('second-graph', 'figure'),
    Input('selected_city', 'value'),
    Input('customer_type', 'value')
)
def plot_cogs(data,mem=0): #plotting cost of goods sales
    data = df[df['City'] == data]
    if mem == 1:
        cogs = data[
            data['Customer type'] == 'Member'].groupby([
            'Product line'])['cogs'].sum().sort_values(ascending=False)
    elif mem == 2:
        cogs = data[
            data['Customer type'] == 'Normal'].groupby([
            'Product line'])['cogs'].sum().sort_values(ascending=False)
    else:
        cogs = data.groupby([
            'Product line'])['cogs'].sum().sort_values(ascending=False)
    fig = px.bar(data,
                 x=np.array(cogs.index),
                 y=cogs.unique(),
                 title='Harga pokok per jenis produk',
                color=np.array(cogs.index),
                 width=1200,height=500,
                 labels={
                     'x': 'Jenis Produk',
                     'y': 'Harga Pokok Penjualan',
                     'color': 'Jenis Produk'
                 }
    )
    return fig

@app.callback(
    Output('third-graph', 'figure'),
    Input('selected_city', 'value'),
    Input('customer_type', 'value')
)
def cogs_daily(data,mem=0):
    if mem==1: 
        data = df[
            (df['City'] == data) &
            (df['Customer type'] == 'Member')
        ].groupby(["City", "Date"])['cogs'].sum().reset_index(name="Harga Pokok Penjualan")
    elif mem==2:
        data = df[
            (df['City'] == data) &
            (df['Customer type'] == 'Normal')
        ].groupby(["City", "Date"])['cogs'].sum().reset_index(name="Harga Pokok Penjualan")
    else:
        data = df[df['City'] == data
        ].groupby(["City", "Date"])['cogs'].sum().reset_index(name="Harga Pokok Penjualan")
    fig = px.bar(data,x='Date',y='Harga Pokok Penjualan', color='Harga Pokok Penjualan',
                color_continuous_scale=px.colors.sequential.Viridis,
                width=1200,height=500)
    fig.update_xaxes(rangeslider_visible=True)
    return fig

@app.callback(
    Output('fourth-graph', 'figure'),
    Input('selected_city', 'value'),
    Input('customer_type', 'value')
)
def cogs_time(data,mem=0):
    if mem == 1:
        data = df[
            (df['City'] == data) &
            (df['Customer type'] == 'Member')
        ].groupby(["City", "Hour"])['cogs'].sum().reset_index(name="Harga Pokok Penjualan")
    elif mem == 2:
        data = df[
            (df['City'] == data) &
            (df['Customer type'] == 'Normal')
        ].groupby(["City", "Hour"])['cogs'].sum().reset_index(name="Harga Pokok Penjualan")
    else:
        data = df[df['City'] == data].groupby([
            "City", "Hour"])['cogs'].sum().reset_index(name="Harga Pokok Penjualan")
    fig = px.bar(data,x='Hour',y='Harga Pokok Penjualan', color='Harga Pokok Penjualan',
                    color_continuous_scale=px.colors.sequential.Viridis,width=1200,height=500,
                    labels={
                    'Hour':'Jam'
                })
    fig.update_xaxes(rangeslider_visible=True)
    return fig
    

# remove the main things