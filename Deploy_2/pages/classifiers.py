import streamlit as st
import plotly.express as px
import pandas as pd

def app():
    clf_val = {
        'Random Forest':0.988,
        'Logistic Regression':0.991,
        'K-Nearest Neighbor': 0.974,
        'XGBoost': 0.989
    }
    clf_cv = {
        'Random Forest':0.986,
        'Logistic Regression':0.992,
        'K-Nearest Neighbor': 0.973,
        'XGBoost': 0.989
    }
    clf_test= {
        'Random Forest':0.988,
        'Logistic Regression':0.990,
        'K-Nearest Neighbor': 0.972,
        'XGBoost': 0.991
    }

    st.header('Hasil rata-rata Cross Validation accuracy Score ')
    col1, col2, col3 = st.columns(3)
    col1.metric("XGBoost", "98.9%")
    col2.metric("Random Forest", "98.6%")
    col3.metric("K-NN", "97.3%")
    st.metric("Logistic Regression","99.2%")

    clf_cv = pd.DataFrame(clf_cv,index=['Cross Validation Score'])
    fig1 = px.bar(x=clf_cv.T['Cross Validation Score'], y=clf_cv.T.index, 
    title="Perbandingan rata-rata Cross Validation (K-Fold = 5)",labels={
        'x':'Nilai rata-rata Cross Validation',
        'y':'Nama Classifiers'
    }
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.header('Hasil Validation prediction accuracy score')
    col1, col2, col3= st.columns(3)
    col1.metric("XGBoost", "98.9%")
    col2.metric("Random Forest", "98.8%")
    col3.metric("K-NN", "97.4%")
    st.metric("Logistic Regression","99.1%")

    clf_val = pd.DataFrame(clf_val,index=['Cross Validation Score'])
    fig2 = px.bar(x=clf_val.T['Cross Validation Score'], y=clf_val.T.index, 
    title="Perbandingan rata-rata Cross Validation (K-Fold = 5)",labels={
        'x':'Nilai rata-rata Cross Validation',
        'y':'Nama Classifiers'
    }
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.header('Hasil Test prediction accuracy score')
    col1, col2,col3 = st.columns(3)
    col1.metric("Logistic Regression", "99.0%")
    col2.metric("Random Forest", "98.8%")
    col3.metric("K-NN", "97.2%")
    st.metric("XGBoost","99.1%")

    clf_test = pd.DataFrame(clf_test,index=['Cross Validation Score'])
    fig3 = px.bar(x=clf_test.T['Cross Validation Score'], y=clf_test.T.index, 
    title="Perbandingan rata-rata Cross Validation (K-Fold = 5)",labels={
        'x':'Nilai rata-rata Cross Validation',
        'y':'Nama Classifiers'
    }
    )
    st.plotly_chart(fig3, use_container_width=True)


    st.write("""
    Hasil dari classifier yang sudah saya implementasi memiliki nilai yang beragam tetapi sudah cukup goodfit
    untuk semua classifier. Tetapi, saya akan menjadikan patokan terhadap hasil prediksi testing data. Maka dari itu,
    saya akan melanjutkan proses Model Improvement menggunakan XGBoost
    """)

    

    st.header('Hasil Test XGBoost - Setelah Hyperparameter tuning')
    st.metric("Test validation score","99.1%")
    st.write("""
    Setelah saya lakukan Model improvement terhadap XGBoost (Randomized Search -> Grid Search), hasil nya
    dibawah jika di bandingkan dengan default parameter (selisih 0.05%). Maka dari itu, dalam penyelesaian
    Milestone 2 ini, Model saya akan tetap menggunakan default parameter
    """)
    



