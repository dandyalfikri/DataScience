import streamlit as st
from multipage import MultiPage
from pages import home,prediction,bmi,kalori

st.set_page_config(
     page_title="Bon AIpetit",
     page_icon="🥗",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Report a bug': 'https://github.com/dandyalfikri', # ganti pake url github
          'Get help': 'https://github.com/AryaB29',
         'About': "# BonAIPetit : Food recognition, Recommendation, and more" # ganti pake deskripsi aplikasi
     }
 )

app=MultiPage()


st.title('Final Project FTDS')

st.write("""
#### Created by **Dandy Alfikri & Arya Bandoro**\n
##### FTDS004 - Hacktiv8 Full Time Data Science Student

*Gunakan sidebar untuk navigasi antar halaman*

""")

app.add_page('Home',home.app)
app.add_page('Prediksi Makanan',prediction.app)
app.add_page('Kalkulator BMI',bmi.app)
app.add_page('Kebutuhan Kalori',kalori.app)
app.run()
