import streamlit as st
from PIL import Image
def app():
    image = Image.open('bmi-classification.jpeg')
    st.image(image,caption='Klasifikasi Berdasarkan BMI')
    input_berat = st.slider("Masukan Berat Badan Anda",0,200)
    input_tinggi = st.slider("Masukan Tinggi Badan Anda",0,300)
    if(st.button('Calculate')):
        if(input_berat != 0 and input_tinggi != 0):
            BMI = input_berat / (input_tinggi/100)**2
            st.write("Berat Anda :", input_berat)
            st.write("Tinggi Anda :", input_tinggi)
            st.write("BMI Anda :", BMI)
            if BMI <= 18.4:
                st.write("Anda Kekurangan Berat Badan")
                st.write("Silahkan Akses Fitur Kami Untuk Mengetahui kebutuhan Kalori Anda")
            elif BMI <= 24.9:
                st.write("BMI Anda Ideal")
            elif BMI <= 29.9:
                st.write("Anda Memiliki Berat Over Weight")
                st.write("Silahkan Akses Fitur Kami Untuk Mengetahui kebutuhan Kalori Anda")
            elif BMI <= 34.9:
                st.write("Anda Mengalami Over Weight Yang Parah")
                st.write("Silahkan Akses Fitur Kami Untuk Mengetahui kebutuhan Kalori Anda")
            elif BMI <= 39.9:
                st.write("Anda Mengalami Obesitas")
                st.write("Silahkan Akses Fitur Kami Untuk Mengetahui kebutuhan Kalori Anda")
            else:
                st.write("Anda Mengalami Obesitas Yang Cukup Parah")
                st.write("Silahkan Akses Fitur Kami Untuk Mengetahui kebutuhan Kalori Anda")