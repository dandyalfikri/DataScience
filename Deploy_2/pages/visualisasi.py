import streamlit as st
import plotly.express as px
import pandas as pd

def app():
    @st.cache(allow_output_mutation=True)
    def fetch_data_view():
        df = pd.read_csv('Challenger_Ranked_Games.csv')
        return df


    df = fetch_data_view()
    for i in range (len(df.columns)):
        if ('First' in df.columns[i]):
            df[df.columns[i]].replace({
                0: 'Red Team First',
                1: 'Blue Team First'
            }, inplace=True)
    
    st.header('Cuplikan Data')
    st.write(df.head())
    df['blueWins'].replace({
        1:'Blue team win',
        0:'Red team win'
    },inplace=True)
    df['redWins'].replace({
        0:'Blue team win',
        1:'Red team win'
    })

    opt = st.selectbox('Visualisasi tipe data',
        ('Numerical','Categorical')
    )
    
    

    if opt == 'Numerical':
        num_col = df.select_dtypes(include='number').columns
        choices = st.multiselect('Pilih fitur (Numerical)',options=pd.DataFrame([f'{i}'for i in num_col]))

        if choices:
            for i in choices:
                fig = px.histogram(df, x=df[i], color=df['blueWins'],marginal="box",
                title=f'{i} histogram & barplot'.upper(),width=600,height=500,labels={
                    'y':'Team'
                    })
                st.plotly_chart(fig, use_container_width=True)
        
    elif opt == 'Categorical':
        cat_col = df.select_dtypes(include='object').columns
        choices_cat = st.multiselect('Pilih fitur (Categorical)',options=pd.DataFrame([f'{i}'for i in cat_col]))
        team = st.radio('Team wins',
        ('Blue team win','Red team win','Both'))
        if choices_cat:
            for i in choices_cat:
                if team == 'Blue team win':
                    data = df[df['blueWins'] == 'Blue team win']
                    data = data[i].value_counts()
                elif team == 'Red team win':
                    data = df[df['blueWins'] == 'Red team win']
                    data = data[i].value_counts()
                else:
                    data = df[i].value_counts()
                fig1 = px.pie(values=data.values, names=data.index,
                title=f'{i} Piechart'.upper(),width=600,height=500)
                st.plotly_chart(fig1, use_container_width=True)