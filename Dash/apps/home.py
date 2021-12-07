import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Dashboard penjualan supermarket",
                className="text-center"),
                className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='Selamat datang! Nama saya Dandy Alfikri dan dalam project milestone saya kali ini, saya akan membuat sebuah dasboard mengenai penjualan supermarket di Myanmar'),
                className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(
                html.H5(children='Ada beberapa tombol di bawah untuk melakukan navigasi kepada data set yang digunakan, gambaran visualisasi penjualan, dan Hypothesis testing'),
                className="mb-5")
        ]),

        dbc.Row([
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Dataset yang digunakan dalam dashboard ini',
                        className="text-center"),
                        dbc.Button("Supermarket Sales Dataset",
                        href="https://www.kaggle.com/aungpyaeap/supermarket-sales",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),

            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Akses Penjualan berdasarkan cabang disini',
                        className="text-center"),
                        dbc.Button("Branch sales overview",
                        href='/apps/branch',
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
        ], className="mb-5"),
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Akses visualisasi penjualan harian disini',
                        className="text-center"),
                        dbc.Button("Harian",
                        href="/apps/harian",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),

            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Akses Hypothesis testing disini',
                        className="text-center"),
                        dbc.Button("Hypothesis",
                        href='/apps/hipotesa',
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
        ], className="mb-5"),
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Akses visualisasi segmentasi penjualan  disini',
                        className="text-center"),
                        dbc.Button("Segmentasi",
                        href="/apps/piechart",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
        ], className="mb-5"),
          
            
    ])
])