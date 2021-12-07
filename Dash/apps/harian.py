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
                html.H1("Graph penjualan supermarket berdasarkan harian"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Visualisasi graph untuk supermarket berdasarkan harian, dan jenis produk'),
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
                dcc.Checklist(
                    id='product_list',
                    options=[
                        {'label': i, 'value': i}
                        for i in df['Product line'].unique()
                    ],
                    value=df['Product line'].unique(),
                    inputStyle={"margin-right": "5px"}
    )
            )

        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='main-graph_harian'
                )
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='second-graph_harian'
                )
            )
        ])
        
    ])
    
])


@app.callback(
    Output('main-graph_harian', 'figure'),
    Input('selected_city', 'value'),
    Input('product_list', 'value')
)
def daily_qty(data,product_line=['Health and beauty', 'Food and beverages']): #pembuatan function plotting daily transaction
    data = df[df['City'] == data]
    daily = data[data['Product line'].isin(product_line)]
    daily = daily.groupby(["Product line", "Day","DoW"]).size().reset_index(name="qty")
    daily.sort_values(by='DoW', inplace=True)
    fig = px.bar(daily,x='Day', y="qty",
             width=1200,height=500,title='Jumlah jenis produk terjual',color='Product line',
             labels={
                 'qty':'Kuantitas',
                 'Day':'Hari'
             })
    return fig

@app.callback(
    Output('second-graph_harian', 'figure'),
    Input('selected_city', 'value'),
    Input('product_list', 'value')
)
def daily_cogs(data,product_line=['Health and beauty', 'Food and beverages']): #pembuatan function plotting daily transaction
    data = df[df['City'] == data]
    daily = data[data['Product line'].isin(product_line)]
    daily = daily.groupby(["Product line", "Day","DoW"])['cogs'].sum().reset_index() #membuat df baru
    daily.sort_values(by='DoW', inplace=True)#sortir berdasarkan hari
    fig = px.bar(daily,x='Day', y="cogs",
             width=1200,height=500,title='Jumlah harga pokok dari produk terjual',color='Product line',
             labels={
                 'Day' : 'Hari',
                 'cogs' : 'Harga Pokok Penjualan'
             })
    return fig
    

# remove the main things