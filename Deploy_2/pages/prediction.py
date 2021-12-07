import streamlit as st
import pandas as pd
import joblib
import time
import plotly.express as px

def app():   
    @st.cache(allow_output_mutation=True)
    def fetch_data():
        df = pd.read_csv('Challenger_Ranked_Games.csv')
        return df
    

    st.title('Input data untuk di prediksi klasifikasi')
    st.subheader('Menggunakan XGBoost (Default parameter)')
    
    df = fetch_data()
    load_model = joblib.load('xg_finalmodel.pkl')
    def user_input():
        
        for i in range (len(df.columns)):
            if ('First' in df.columns[i]):
                df[df.columns[i]].replace({
                    0: 'Red Team First',
                    1: 'Blue Team First'
                }, inplace=True)

        blueFirstBlood=st.selectbox('First Blood', df['blueFirstBlood'].unique())
        if blueFirstBlood == 'Red Team First':
            blueFirstBlood = 0
        else: blueFirstBlood = 1
        blueFirstTower=st.selectbox('First Tower', df['blueFirstTower'].unique())
        if blueFirstTower == 'Red Team First':
            blueFirstTower = 0
        else: blueFirstTower = 1
        blueFirstBaron=st.selectbox('First Baron', df['blueFirstBaron'].unique())
        if blueFirstBaron == 'Red Team First':
            blueFirstBaron = 0
        else: blueFirstBaron = 1
        blueFirstDragon=st.selectbox('First Dragon', df['blueFirstDragon'].unique())
        if blueFirstDragon == 'Red Team First':
            blueFirstDragon = 0
        else: blueFirstDragon = 1
        blueFirstInhibitor=st.selectbox('First Blood', df['blueFirstInhibitor'].unique())
        if blueFirstInhibitor == 'Red Team First':
            blueFirstInhibitor = 0
        else: blueFirstInhibitor = 1
        blueDragonKills = st.number_input('Total Dragon killed by Your team', value=0,min_value=0, max_value=4)
        blueBaronKills = st.number_input('Total Baron killed by Your team', value=0,min_value=0, max_value=10) 
        blueTowerKills = st.number_input('Total Tower killed by Your team', value=0,min_value=0, max_value=11)
        blueInhibitorKills = st.number_input('Total Inhibitor killed by Your team', value=0,min_value=0, max_value=3)
        blueKills = st.number_input('Total kills by Your team', value=0,min_value=0, max_value=999)
        blueDeath = st.number_input('Total deaths of Your team', value=0,min_value=0, max_value=999)
        blueAssist = st.number_input('Total Tower killed by Your team', value=0,min_value=0, max_value=999)
        blueChampionDamageDealt = st.number_input('Total Damage dealt to Champion by Your team', value=0,min_value=0, max_value=999999)
        blueTotalGold = st.number_input('Total gold of Your team', value=0,min_value=0, max_value=999999)
        blueTotalLevel = st.number_input('Total champion levels of Your team', value=0,min_value=0, max_value=90)
        blueJungleMinionKills = st.number_input('Total jungle minions killed by Your team', value=0,min_value=0, max_value=999)
        blueTotalHeal = st.number_input('Total heal by Your team', value=0,min_value=0, max_value=999)
        blueObjectDamageDealt = st.number_input('Total damage dealt to object by Your team', value=0,min_value=0, max_value=999)
        redDragonKills = st.number_input('Total Dragon killed by Opposite team', value=0,min_value=0, max_value=4)
        redBaronKills = st.number_input('Total Baron killed by Opposite team', value=0,min_value=0, max_value=10)
        redTowerKills = st.number_input('Total Tower killed by Opposite team', value=0,min_value=0, max_value=11)
        redInhibitorKills = st.number_input('Total Inhibitor Tower killed by Opposite team', value=0,min_value=0, max_value=3)
        redAssist = st.number_input('Total Assists by Opposite team', value=0,min_value=0, max_value=999)
        redChampionDamageDealt = st.number_input('Total Champion damage dealt by Opposite team', value=0,min_value=0, max_value=99999)
        redTotalGold = st.number_input('Total Gold of Opposite team', value=0,min_value=0, max_value=99999)
        redTotalLevel = st.number_input('Total Champion levels of Opposite team', value=0,min_value=0, max_value=90)
        redJungleMinionKills = st.number_input('Total jungle killed by Opposite team', value=0,min_value=0, max_value=999)
        redTotalHeal = st.number_input('Total Heals from Opposite team', value=0,min_value=0, max_value=99999)
        redObjectDamageDealt = st.number_input('Total Object damage dealt by Opposite team', value=0,min_value=0, max_value=999)

        
        data = {
            'blueFirstBlood': blueFirstBlood,
    'blueFirstTower': blueFirstTower,
    'blueFirstBaron': blueFirstBaron,
    'blueFirstDragon': blueFirstDragon,
    'blueFirstInhibitor': blueFirstInhibitor,
    'blueDragonKills': blueDragonKills,
    'blueBaronKills': blueBaronKills,
    'blueTowerKills': blueTowerKills,
    'blueInhibitorKills': blueInhibitorKills,
    'blueKills': blueKills,
    'blueDeath': blueDeath,
    'blueAssist': blueAssist,
    'blueChampionDamageDealt': blueChampionDamageDealt,
    'blueTotalGold': blueTotalGold,
    'blueTotalLevel': blueTotalLevel,
    'blueJungleMinionKills': blueJungleMinionKills,
    'blueTotalHeal': blueTotalHeal,
    'blueObjectDamageDealt': blueObjectDamageDealt,
    'redDragonKills': redDragonKills,
    'redBaronKills': redBaronKills,
    'redTowerKills': redTowerKills,
    'redInhibitorKills': redInhibitorKills,
    'redAssist': redAssist,
    'redChampionDamageDealt': redChampionDamageDealt,
    'redTotalGold': redTotalGold,
    'redTotalLevel': redTotalLevel,
    'redJungleMinionKills': redJungleMinionKills,
    'redTotalHeal': redTotalHeal,
    'redObjectDamageDealt': redObjectDamageDealt
        }

        features = pd.DataFrame(data, index=[0])
        return features
    input = user_input()
    time.sleep(2)
    if st.button('Predict'):
        prediction = load_model.predict(input)
        if prediction[0] == 0:
            st.header('Prediksi : Tim kamu kalah!')
        else:
            st.header('Prediksi :Tim kamu menang!')
        prob_no = (load_model.predict_proba(input)[0][0])*100
        prob_yes = (load_model.predict_proba(input)[0][1])*100
        st.write('Probability Menang :{0:.2f}%'.format(prob_yes))
        st.write('Probability Kalah :{0:.2f}%'.format(prob_no))
        prob_dict=({
            'No Probability Score':prob_no,
            'Yes Probability Score':prob_yes
        })
        prob_dict = pd.Series(prob_dict)
        
        fig = px.pie(values=prob_dict.values,names=prob_dict.index,
        title='Prediction Probability Score')
        st.plotly_chart(fig, use_container_width=True)