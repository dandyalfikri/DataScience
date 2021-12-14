import streamlit as st
def app():
    st.write("Metode Yang Kami Gunakan Adalah BMR dengan Metode Harris-Bennedict, Silahkan Masukan Data Anda")
    gender_user = st.selectbox("Masukan Gender Anda",['Pria','Wanita'])
    st.write("Gender Anda :", gender_user)
    usia_user = st.number_input('Masukan Umur Anda',0,150)
    st.write("Usia Anda :",usia_user)
    berat_user = st.slider("Silahkan Masukan Berat Badan Anda",0,200)
    st.write ("Berat Anda :",berat_user)
    tinggi_user = st.slider("Silahkan Masukan Tinggi Badan Anda",0,300)
    st.write("Tinggi Anda :",tinggi_user)
    if(st.button('Calculate')):
        if(usia_user != 0 and berat_user !=0 and tinggi_user !=0):
            if gender_user == "Pria":
                BMR1 = 88.362+(13.397*berat_user)+(4.799*tinggi_user)-(5.677*usia_user)
                st.write("Kebutuhan BMR Anda :", BMR1,"Kalori")
            if gender_user == "Wanita":
                BMR2 = 447.593 +(9.247*berat_user)+(3.098*tinggi_user) - (4.330*usia_user)
                st.write("Kebutuhan BMR Anda :",BMR2,"Kalori")