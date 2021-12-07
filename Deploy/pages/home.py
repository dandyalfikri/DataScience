import streamlit as st

def app():
    
    url = '[Dataset](https://www.kaggle.com/blastchar/telco-customer-churn)'
    st.header('Telco Customer Churn')
    st.markdown(url, unsafe_allow_html=True)
    st.write('Data ini mengenai pelanggan perusahaan Telco')
    st.caption('Tujuan Milestone ini melakukan prediksi perilaku untuk mempertahankan pelanggan. Dan melakukan pengembangan program retensi pelanggan yang terfokus')
    st.subheader('Konten dari dataset')
    st.markdown("""
- Pelanggan yang pergi dalam sebulan terakhir
- Layanan yang telah didaftarkan oleh setiap pelanggan (Telepon, saluran, internet, online security, backup online, perlindungan perangkat, dukungan teknis, straming TV dan Film.
- Informasi akun pelanggan (Sudah berapa lama menjadi pelanggan, kontrak, metode pembayaran, tagihan tanpa kertas, tagihan bulanan, dan total tagihan
- Info demografis pelanggan (Jenis kelamin, rentang usia,dan jika mereka memiliki pasangan dan tanggungan) 
    """)
    st.markdown("""
    Penjelasan per kolom:
- customerID : ID pelanggan 
- gender : Jenis kelamin pelanggan ('Male' atau 'Female')
- SeniorCitizen : apakah pelanggan tersebut sudah senior citizen (boolean)
- Partner : Apakah pelanggan tersebut sudah memiliki partner ('Yes' atau 'No)
- Dependents : Apakah pelanggan tersebut sudah memiliki tanggunan orang ('Yes' atau 'No')
- tenure : Jumlah bulan pelanggan tersebut sudah stay di perusahaan ini
- PhoneService : Apakah pelanggan tersebut memiliki phone service ('Yes' atau 'No')
- MultipleLines : Apakah pelanggan tersebut memiliki multiple lines ('Yes' atau 'No')
- InternetService : Internet service provider dari pelanggan tersebut ('DSL', 'Fiber Optic', 'No')
- OnlineSecurity : Apakah pelanggan tersebut memiliki online security ('Yes', 'No', 'No internet service')
- OnlineBackup : Apakah pelanggan tersebut memiliki online backup ('Yes', 'No', 'No internet service')
- DeviceProtection : Apakah pelanggan tersebut memiliki device protection ('Yes','No','No internet service')
- TechSupport : Apakah pelanggan tersebut memiliki tech support ('Yes', 'No', 'No Internet service')
- StreamingTV : Apakah pelanggan tersebut memiliki streaming tv ('Yes', 'No', 'No Internet service')
- StreamingMovies : Apakah pelanggan tersebut memiliki streaming film ('Yes', 'No', 'No Internet service')
- Contract : Jangka waktu kontrak pelanggan ('Month-to-month','One year','Two year')
- PaperlessBilling : Apakah pelanggan memiliki paperless billing ('Yes' atau 'No')
- PaymentMethod : Metode pembayaran pelanggan ('Electronic Check','Mailed check','Bank transfer (automatic)', 'Credit card(automatic)')
- MonthlyCharges : Jumlah yang di charge terhadap pelanggan per bulan
- TotalCharges : Jumlah total yang di charge terhadap pelanggan
- Churn : Apakah pelanggan tersebut berhenti/keluar ('Yes' atau 'No')
    """)

    