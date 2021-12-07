import streamlit as st
import pandas as pd

def app():
    
    url = '[Dataset](https://www.kaggle.com/gyejr95/league-of-legends-challenger-ranked-games2020)'
    url_lol = '[League of Legends Website](https://lol.garena.com/)'
    st.header('Prediksi League of Legends Pertandingan Ranked')
    col1,col2 = st.columns(2)
    col1.markdown(url, unsafe_allow_html=True)
    col2.markdown(url_lol, unsafe_allow_html=True)
    st.write('Data ini mengenai permainan online \' League of Legends\' Ranked match di ranking tertinggi'  )
    st.caption('Tujuan prediksi ini untuk melakukan prediksi apakah tim User akan menang berdasarkan beberapa input')
    st.subheader('Deskripsi Kolom dari dataset')
    st.markdown("""
 Dataset ini memiliki 50 jumlah kolom dengan beberapa kolom penting yaitu:
- gameDuration: Durasi game berjalan (detik)
- blueWins : Tim biru memenangkan pertandingan
- blueFirstBlood : Tim biru mendapatkan kill pertama dalam game
- blueFirstTower : Tim biru menghancurkan pertama kali dalam game
- blueFirstBaron : Tim biru membunuh objektif monster 'Baron'
- blueFirstInhibitor : Tim biru menghancurkan inhibitor pertama kali dalam game
- blueFirstDragon : Tim biru membunuh objektif monster 'Dragon'
- blueBaronKills : Jumlah monster 'Baron' yang di bunuh oleh tim biru
- blueTowerKills : Jumlah tower yang sudah di hancurkan oleh tim biru
- blueInhibitorKills : Jumlah inhibitor tower yang sudah di hancurkan oleh tim biru
- blueWardPlaced : Jumlah ward yang di pasang oleh tim biru
- blueWardKills : Jumlah ward yang sudah di hancurkan oleh tim biru
- blueKills : Jumlah kill yang tim biru dapatkan dalam game tersebut
- blueDeaths : Jumlah kematian yang tim biru dapatkan dalam game tersebut
- blueAssist : Jumlah assist yang tim biru dapatkan dalam game tersebut
- blueChampionDamageDealt : Jumlah damage yang didapatkan oleh tim biru terhadap hero musuh
- blueTotalGold : Jumlah gold yang dimiliki oleh tim biru
- blueTotalMinionKills : Jumlah creep/minion yang dibunuh oleh tim biru
- blueTotalLevel : Jumlah level yang di dapatkan dari tim biru
- blueAvgLevel : Rata-rata level yang di dapatkan dari tim biru
- blueJungleMinionKills : Jumlah creep/minion yang terbunuh dari game tersebut
- blueKillingSpree : Jumlah pembunuhan hero musuh secara beruntun
- blueTotalHeal : Total heal/penyembuhan dari tim biru
- blueObjectDamageDealt : Total damage dari tim biru terhadap tower musuh

Dan 24 fitur yang memiliki atribut 'blue' di dalamnya tapi untuk tim lawan (Red Team)
    """)

    