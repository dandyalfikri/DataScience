import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats


df = pd.read_csv('supermarket_sales - Sheet1.csv')
df_cleaned = pd.read_csv('supermarket_sales_cleaned.csv')
plot = df.groupby('Customer type')['cogs'].sum()
fig1=px.bar(x = plot.index, y=plot, color=np.array(plot.index), height=400,width=500,
       labels={
                     'x': 'Customer type',
                     'y': 'Pengeluaran dana',
                 })

fig2=px.box(df,x='Customer type',y='cogs', height=400,width=500,labels={'cogs':'Pengeluaran dana'})

member = df[df['Customer type'] == 'Member'].groupby('Date').sum()
normal = df[df['Customer type'] == 'Normal'].groupby('Date').sum()
t,p=stats.ttest_ind(member['cogs'],normal['cogs'])
np.random.seed(42)
pop=np.random.normal(member['cogs'].mean(), member['cogs'].std(), 100000)
ci = stats.norm.interval(0.95, pop.mean(), pop.std())
fig3 = px.histogram(pop,width=1000,height=400,labels={
                     'variable': 'Distribution'}
                  )
fig3.add_vline(pop.mean(), line_color='yellow', line_dash='dash', line_width=2,annotation_text='Mean')
fig3.add_vline(ci[0], line_color='green', line_dash='dash', line_width=2)
fig3.add_vline(ci[1], line_color='green', line_dash='dash', line_width=2,annotation_text='CI')
fig3.add_vline(pop.mean()+t*pop.std(), line_color='black', line_dash='dash', line_width=2,annotation_text='P-val')
fig3.add_vline(pop.mean()-t*pop.std(), line_color='black', line_dash='dash', line_width=2)
fig3.update_yaxes(title='y', visible=False, showticklabels=False)
fig3.update_xaxes(title='x', visible=False, showticklabels=False)
fig3.update_layout(showlegend=False)


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Hypothesis Testing",
                className="text-center"),
                className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='Berdasarkan data yang di dapatkan dari dataset penjualan supermarket, Ada perbedaan antara tipe customer \'Member\' dan \'Normal\'(Non Member) berdasarkan harga pokok penjualan (Cost of goods sold).'),
                className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(
                html.H6(children='Dalam hypothesis testing ini, Saya ingin melihat apakah ada perbedaan yang signifikan antara Member dan Normal(Non-member) dalam harga pokok penjualan menggunakan two-tailed independent two sample test'),
                className="mb-5")
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(figure=fig1)
            ),
            dbc.Col(
                dcc.Graph(figure=fig2)
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Dapat dilihat dari boxplot, ada beberapa outlier yang akan saya drop, agar tidak memberikan distorsi kepada data ini')
            ),
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Dalam hypothesis testing ini, Critical Value yang di tetapkan adalah 0.05(5%)')
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='H₀ : μ Harga pokok penjualan Member = μ Harga pokok penjualan Normal (non-Member)')
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='H₀ : μ Harga pokok penjualan Member ≠ μ Harga pokok penjualan Normal (non-Member)')
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(figure=fig3)
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H2(children='Kesimpulan untuk Developer',
                className="text-center"),
                className="mb-5 mt-5"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='Dari hasil hypothesis testing ini, saya mendapatkan t-stat senilai 0.65 dan p-value senilai 0.52. Nilai dari p-value tersebut melebihi dari nilai critical value yang sudah di tetapkan. Maka, dapat di konklusikan bahwa Null-Hypothesis (H0) gagal di tolak dikarenakan kurangnya bukti untuk menolak nya',
                className="text-center")
            )
        ]),dbc.Row([
            dbc.Col(
                html.H2(children='Kesimpulan untuk Shop Executives',
                className="text-center"),
                className="mb-5 mt-5"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='Kesimpulan yang dapat ditarik adalah, tidak ada-nya perbedaan yang signifikan antara member dan normal (non-member). Menurut saya, harus di perbanyak benefit yang diberikan kepada Member agar dapat menjadi loyal customer dalam toko dari dataset ini. Apabila tidak ada perbedaan yang signifikan antara keduanya, customer akan jauh lebih memilih untuk menjadi normal customer saja (asumsi menjadi member harus memberikan data / effort tambahan)',
                className="text-center"),
                className="mb-4"
            )
        ])

        
    ])
])