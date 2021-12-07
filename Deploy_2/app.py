import streamlit as st
from multipage import MultiPage
from pages import home,visualisasi,classifiers,prediction

app=MultiPage()


st.title('Milestone Phase 1 FTDS')
st.write("""
Created by Dandy Alfikri

Batch - 004 

Hacktiv8 - Full Time Data Science Student

Gunakan sidebar untuk navigasi antar halaman

""")

app.add_page('Home',home.app)
app.add_page("Visualisasi",visualisasi.app)
app.add_page('Hasil Classifiers',classifiers.app)
app.add_page('Prediksi',prediction.app)
app.run()
