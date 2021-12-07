import streamlit as st
import pandas as pd
import joblib
import time
import plotly.express as px

def app():
    
    @st.cache
    def fetch_data():
        df = pd.read_csv('bank-additional-full-cleaned.csv')
        return df
    
    

    st.title('Input data untuk di prediksi klasifikasi')
    st.subheader('Menggunakan XGBoost (Tuned parameter)')
    
    df = fetch_data()
    load_model = joblib.load('final_model.pkl')
    def user_input():
        month_dict = {
            1:'Januari',2:'Februari',3:'Maret',4:'April',5:'Mei',6:'Juni',7:'Juli',8:'Agustus',
            9:'September',10:'Oktober',11:'November',12:'Desember'
        }
        month_dict = pd.Series(month_dict)

        day_dict = {
            1:'Senin',2:'Selasa',3:'Rabu',4:'Kamis',5:'Jumat',6:'Sabtu',7:'Minggu'
        }
        day_dict = pd.Series(day_dict)

        edu_dict = {
            1:'unknown',2:'basic.4y',3:'basic.6y',4:'basic.9y',5:'high.school',
            6:'university.degree',7:'professional.course'
            }
        edu_dict = pd.Series(edu_dict)

        age=st.number_input('Umur', value=0, min_value=0, max_value=99)
        job= st.selectbox('Pekerjaan', df['job'].unique())
        marital = st.selectbox('Status', df['marital'].unique())
        education = st.selectbox('Edukasi Terakhir', df['education'].unique())
        education = edu_dict[edu_dict == education].index
        default = st.selectbox('Default', df['default'].unique())
        housing = st.selectbox('KPR', df['housing'].unique())
        loan = st.selectbox('Loan', df['loan'].unique())
        contact = st.selectbox('Kontak', df['contact'].unique())
        month = st.selectbox('Bulan', month_dict.values)
        month = month_dict[month_dict == month].index[0]
        day_of_week = st.selectbox('Hari', day_dict.values)
        day_of_week = day_dict[day_dict == day_of_week].index[0]
        duration = st.number_input('Durasi kontak terakhir', value=0,min_value=0)
        campaign = st.number_input('Jumlah Kontak selama kampanye', value=0,min_value=0)
        pdays = st.number_input('Jumlah hari terakhir dihubungi', value=0,min_value=-1, max_value=99)
        st.write('Jika belum pernah di hubungi sebelumnya, input -1')
        previous = st.number_input('Jumlah hubungan terakhir', value=0,min_value=0, max_value=99)
        poutcome = st.selectbox('Hasil kampanye terakhir', df['poutcome'].unique())
        emp_var_rate = st.number_input('Employment Variation Rate', value=df['emp.var.rate'].mean())
        cons_price_idx = st.number_input('Indeks Harga Konsumen', value=df['cons.price.idx'].mean())
        cons_conf_idx = st.number_input('Indeks Keyakinan Konsumen', value=df['cons.conf.idx'].mean())
        euribor3m = st.number_input('Euro Interbank Offered Rate', value=df['euribor3m'].mean())
        nr_employed = st.number_input('Number of employees', value=df['nr.employed'].mean())

        data = {
            'age':age, 'job':job, 'marital':marital,
             'education':education,
              'default':default,
             'housing':housing, 'loan':loan, 'contact':contact, 'month':month,
              'day_of_week':day_of_week, 'duration':duration, 'campaign':campaign,
               'pdays':pdays,'previous':previous, 'poutcome':poutcome,
                'emp.var.rate':emp_var_rate, 'cons.price.idx':cons_price_idx,
                'cons.conf.idx':cons_conf_idx, 'euribor3m':euribor3m, 'nr.employed':nr_employed
        }

        features = pd.DataFrame(data, index=[0])
        return features
    input = user_input()
    time.sleep(2)
    if st.button('Predict'):
        prediction = load_model.predict(input)

        if prediction[0] == 0:
            st.header('Prediksi : Tidak berlangganan untuk deposit')
        else:
            st.header('Prediksi : Akan berlangganan deposit')
        prob_no = (load_model.predict_proba(input)[0][0])*100
        prob_yes = (load_model.predict_proba(input)[0][1])*100
        st.write('Probability Berlangganan :{0:.2f}%'.format(prob_yes))
        st.write('Probability Tidak Berlangganan :{0:.2f}%'.format(prob_no))
        prob_dict=({
            'No Probability Score':prob_no,
            'Yes Probability Score':prob_yes
        })
        prob_dict = pd.Series(prob_dict)
        
        fig = px.pie(values=prob_dict.values,names=prob_dict.index,
        title='Prediction Probability Score')
        st.plotly_chart(fig, use_container_width=True)