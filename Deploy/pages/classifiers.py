import streamlit as st
import plotly.express as px
import pandas as pd

def app():
    @st.cache
    def fetch_data():
        df = pd.read_csv('bank-additional-full.csv')
        return df
    clf_cv = {
        'Decision Tree':0.88975,
        'Random Forest':0.913289,
        'Logistic Regression':0.912079,
        'SVM Linear': 0.894539,
        'SVM RBF': 0.900122,
        'SVM Polynomial': 0.89578,
        'SVM Sigmoid': 0.878412,
        'K-Nearest Neighbor': 0.904947,
        'XGBoost': 0.916018
    }

    st.header('Hasil rata-rata Cross Validation Score (Training)')
    col1, col2, col3 = st.columns(3)
    col1.metric("Decision Tree", "89.0%")
    col2.metric("Random Forest", "91.3%")
    col3.metric("Logistic Regression", "91.2%")
    
    col1, col2, col3= st.columns(3)
    col1.metric("SVM Linear", "89.4%")
    col2.metric("SVM RBF", "90%")
    col3.metric("SVM Polynomial", "89.6%")
    

    col1, col2,col3 = st.columns(3)
    col1.metric("SVM Sigmoid","87.8%")
    col2.metric("XGBoost", "91.6%")
    col3.metric("KNN", "90.4%")

    clf_cv = pd.DataFrame(clf_cv,index=['Cross Validation Score'])
    fig = px.bar(x=clf_cv.T['Cross Validation Score'], y=clf_cv.T.index, 
    title="Perbandingan rata-rata Cross Validation (K-Fold = 5)",labels={
        'x':'Nilai rata-rata Cross Validation',
        'y':'Nama Classifiers'
    }
    )
    st.plotly_chart(fig, use_container_width=True)

    st.write("""
    Hasil classifier terbaik dari rata-rata akurasi dari Cross Validation (K-Fold = 5) adalah XGBoost
    Maka, saya melanjutkan ke Hyperparameter tuning dengan classifier XGBoost
    """)

    st.header('Hasil Test XGBoost - Setelah Hyperparameter tuning')

    col1,col2 = st.columns(2)
    col1.metric("Mean cross validation score","91.95%")
    col2.metric("Test validation score","91.97%")



