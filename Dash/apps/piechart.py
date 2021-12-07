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
                html.H1("Visualisasi segment penjualan supermarket"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Visualisasi untuk supermarket berdasarkan segmen customer, penjualan, dan cara transaksi'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='selected_option',
                    options=[
                       {'label':'Gender', 'value': 'Gender'},
                       {'label':'Customer type', 'value':'Customer type'},
                       {'label':'Payment', 'value':'Payment'},
                       {'label':'City', 'value':'City'}
                    ],
                    value='Gender',
                ),
                className="mb-4"
            )
        ]) ,
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='main_pie'
                )
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='second_bar'
                )
            )
        ])
        
    ])
    
])


@app.callback(
    Output('main_pie', 'figure'),
    Input('selected_option', 'value'),
)
def pie(kategori):
    fig = px.pie(df, values=df[kategori].value_counts(),
                 names = df[kategori].unique(), title=kategori)
    return fig

@app.callback(
    Output('second_bar', 'figure'),
    Input('selected_option', 'value'),
)
def bar(kategori):
    new_df = df[kategori].value_counts()
    fig = px.bar(x=np.array(new_df.index), y=new_df,
             width=1200,height=500,title=kategori,
                labels={
                     'x': kategori,
                     'y': 'Kuantitas',
                 })
    return fig
    

# remove the main things