import streamlit as st
import plotly.express as px
import pandas as pd

def app():
    @st.cache
    def fetch_data_view():
        df_view = pd.read_csv('bank-additional-full.csv',sep=';')
        return df_view
    
    @st.cache
    def fetch_data():
        df = pd.read_csv('bank-additional-full-cleaned.csv')
        return df

    df_view = fetch_data_view()
    st.header('Cuplikan Data')
    st.write(df_view.head())
    df_view.rename(columns={'y':'Subscribed'},inplace=True)
    df = fetch_data()
    opt = st.selectbox('Visualisasi tipe data',
        ('Numerical','Categorical')
    )
    col1, col2 = st.columns(2)
    
    

    if opt == 'Numerical':
        num_col = df_view.select_dtypes(include='number').columns
        choices = st.multiselect('Pilih fitur (Numerical)',options=pd.DataFrame([f'{i}'for i in num_col]))

        if choices:
            for i in choices:
                fig = px.histogram(df_view, x=df_view[i], color=df_view['Subscribed'],marginal="box",
                title=f'{i} histogram & barplot'.upper(),width=600,height=500,labels={
                    'y':'Subscribed?'
                    })
                st.plotly_chart(fig, use_container_width=True)
        
    elif opt == 'Categorical':
        cat_col = df_view.select_dtypes(include='object').columns
        choices_cat = st.multiselect('Pilih fitur (Categorical)',options=pd.DataFrame([f'{i}'for i in cat_col]))
        subs = st.radio('Subscription options',
        ('Subscribed','Not Subscribed','Both'))
        st.write(subs)
        if choices_cat:
            for i in choices_cat:
                if subs == 'Subscribed':
                    data = df_view[df_view['Subscribed'] == 'yes']
                    data = data[i].value_counts()
                elif subs == 'Not Subscribed':
                    data = df_view[df_view['Subscribed'] == 'no']
                    data = data[i].value_counts()
                else:
                    data = df_view[i].value_counts()
                fig1 = px.pie(values=data.values, names=data.index,
                title=f'{i} Piechart'.upper(),width=600,height=500)
                st.plotly_chart(fig1, use_container_width=True)