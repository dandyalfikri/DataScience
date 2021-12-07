import streamlit as st
import plotly.express as px
import pandas as pd

def app():
    @st.cache(allow_output_mutation=True)
    def fetch_data_view():
        df = pd.read_csv('dataset.csv')
        return df


    df = fetch_data_view()
    
    st.header('Cuplikan Data')
    st.write(df.head())

    opt = st.selectbox('Visualisasi tipe data',
        ('Numerical','Categorical')
    )
    if opt == 'Numerical':
        num_col = df.select_dtypes(include='number').columns
        choices = st.multiselect('Pilih fitur (Numerical)',options=pd.DataFrame([f'{i}'for i in num_col]))

        if choices:
            for i in choices:
                fig = px.histogram(df, x=df[i], color=df['Churn'],marginal="box",
                title=f'{i} histogram & barplot'.upper(),width=600,height=500,labels={
                    'y':'Churn'
                    })
                st.plotly_chart(fig, use_container_width=True)
        
    elif opt == 'Categorical':
        cat_col = df.select_dtypes(include='object').drop(['customerID','Churn'],axis=1).columns
        choices_cat = st.multiselect('Pilih fitur (Categorical)',options=pd.DataFrame([f'{i}'for i in cat_col]))
        churn = st.radio('Churns',
        ('Yes','No','Both'))
        if choices_cat:
            for i in choices_cat:
                if churn == 'Yes':
                    data = df[df['Churn'] == 'Yes']
                    data = data[i].value_counts()
                elif churn == 'No':
                    data = df[df['Churn'] == 'No']
                    data = data[i].value_counts()
                else:
                    data = df[i].value_counts()
                fig1 = px.pie(values=data.values, names=data.index,
                title=f'{i} Piechart'.upper(),width=600,height=500)
                st.plotly_chart(fig1, use_container_width=True)