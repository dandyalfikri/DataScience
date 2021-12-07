import streamlit as st
import pandas as pd
import time
import plotly.express as px
import tensorflow as tf

def app():   
    @st.cache(allow_output_mutation=True)
    def fetch_data():
        df = pd.read_csv('dataset.csv')
        return df
    

    st.title('Input data untuk di prediksi klasifikasi')
    st.subheader('Menggunakan Neural Network FunctionalAPI')
    
    df = fetch_data()
    load_model = tf.keras.models.load_model('final_complete_model/')
    def user_input():

        SeniorCitizen=st.selectbox('Senior Citizen', df['SeniorCitizen'].unique())

        Partner=st.selectbox('Partner', df['Partner'].unique())

        Dependents=st.selectbox('Dependents', df['Dependents'].unique())

        PhoneService=st.selectbox('PhoneService', df['PhoneService'].unique())

        MultipleLines=st.selectbox('MultipleLines', df['MultipleLines'].unique())

        InternetService=st.selectbox('InternetService', df['InternetService'].unique())

        OnlineSecurity=st.selectbox('OnlineSecurity', df['OnlineSecurity'].unique())

        OnlineBackup=st.selectbox('OnlineBackup', df['OnlineBackup'].unique())

        DeviceProtection=st.selectbox('DeviceProtection', df['DeviceProtection'].unique())

        TechSupport=st.selectbox('TechSupport', df['TechSupport'].unique())

        StreamingTV=st.selectbox('StreamingTV', df['StreamingTV'].unique())

        StreamingMovies=st.selectbox('StreamingMovies', df['StreamingMovies'].unique())

        Contract=st.selectbox('Contract', df['Contract'].unique())

        PaperlessBilling=st.selectbox('PaperlessBilling', df['PaperlessBilling'].unique())

        PaymentMethod=st.selectbox('PaymentMethod', df['PaymentMethod'].unique())

        MonthlyCharges = st.number_input('Monthyly Charges', value=0,min_value=0, max_value=9999)

        tenure = st.number_input('tenure', value=0,min_value=0, max_value=9999)

        TotalCharges = st.number_input('Total Charges', value=0,min_value=0, max_value=9999) 
        
        
        data = {
            'SeniorCitizen':SeniorCitizen,
            'Partner':Partner,
            'Dependents':Dependents,
            'tenure':tenure,
            'PhoneService':PhoneService,
            'MultipleLines':MultipleLines,
            'InternetService':InternetService,
            'OnlineSecurity':OnlineSecurity,
            'OnlineBackup':OnlineBackup,
            'DeviceProtection':DeviceProtection,
            'TechSupport':TechSupport,
            'StreamingTV':StreamingTV,
            'StreamingMovies':StreamingMovies,
            'Contract':Contract,
            'PaperlessBilling':PaperlessBilling,
            'PaymentMethod': PaymentMethod,
            'MonthlyCharges':MonthlyCharges,
            'TotalCharges':TotalCharges
        }

        
        return data
    input = user_input()
    input_dict = {name: tf.convert_to_tensor([value]) for name, value in input.items()}
    time.sleep(2)
    if st.button('Predict'):
        prediction = load_model.predict(input_dict)
        if prediction[0][0] < 0.5:
            st.header('Prediksi : Tidak berhenti berlangganan (Churn = No)')

        else:
            st.header('Prediksi : Berhenti berlangganan (Churn = Yes)')
        st.write(prediction[0][0])