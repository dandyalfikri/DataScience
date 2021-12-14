from os import name
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image,ImageOps
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle5 as pickle

def app():
    st.title("Food Image Classification")
    food_list = ['Macarons',
    'French Toast',
    'Beef Carpaccio',
    'Hot and Sour Soup',
    'Seaweed Salad',
    'Pulled Pork Sandwich',
    'Lobster Roll Sandwich',
    'Carrot Cake',
    'Red Velvet Cake',
    'Grilled Cheese Sandwich',
    'Spring Rolls',
    'Omelette',
    'Fried Calamari',
    'Caprese Salad',
    'Ramen',
    'Grilled Salmon',
    'Hamburger',
    'Miso Soup',
    'Bread Pudding',
    'Crab Cakes',
    'Cheese Cake',
    'Cup Cakes',
    'Waffles',
    'Fish and Chips',
    'Macaroni and Cheese',
    'Chocolate Mousse',
    'Chicken Curry',
    'Caesar Salad',
    'Nachos',
    'Frozen Yogurt',
    'Ice Cream',
    'Club Sandwich',
    'Strawberry Shortcake',
    'Steak',
    'Garlic Bread',
    'Chicken Wings',
    'Greek Salad',
    'Chocolate Cake',
    'Samosa',
    'Sushi',
    'Beef Tartare',
    'Apple Pie',
    'Pizza',
    'French Onion Soup',
    'Hot Dog',
    'Chicken Quesadilla',
    'Pancakes',
    'Fried Rice',
    'Cheese Plate',
    'Onion Rings',
    'French Fries']
    @st.cache(allow_output_mutation=True)
    def load_model():
        model = tf.keras.models.load_model('0003')
        return model
    model = load_model()
    

    @st.cache(allow_output_mutation=True)
    def teachable_machine_classification(img):
        size = (299,299)
        gambar = ImageOps.fit(img, size)
        gambar = image.img_to_array(gambar)
        gambar = np.expand_dims(img, axis=0)
        gambar = gambar/255
        
        pred = model.predict(gambar)
        index = np.argmax(pred)
        food_list.sort()
        pred_value = food_list[index]
        return  pred_value
    @st.cache(allow_output_mutation=True)
    def load_df():
        df = pd.read_csv('recipes_bersih.csv')
        return df
    df = load_df()
    def load_df2():
        df2 = pd.read_csv('Data_Cakep.csv')
        return df2
    df2 = load_df2()
    def getRecipe(name):
        if len(df[df['Name'] == name]) == 0:
            st.write('## Name : *{}*'.format(name))
            st.write('Belum ada resep untuk makanan tersebut...')
        else:
            recipes = df[df['Name'] == name]
            recipes2 = df2[df2['Name'] == name]
            for i in range (len(recipes)):
                recipe = recipes.iloc[i]
                recipe2 = recipes2.iloc[i]
                st.write('---')
                st.write('## Name : *{}*'.format(name))
                st.write("### Nutrition Information :", recipes2[['Calories','FatContent','SugarContent']] )
                st.write('---')
                st.write("### **Description :**")
                st.write(recipe2['Description'])
                st.write('---')
                st.write('### **Ingredients :**')
                st.write(recipe['RecipeIngredientParts'])
                st.write('---')
                st.write("### **Instruction**")
                st.write(recipe['RecipeInstructions'])
                st.write('---')
                st.write("### **This Is Our Recomendation Based On Your Preferences**")
                indices_cos_path = r'pages/indices_cos.pkl'
                with open(indices_cos_path, "rb") as fh:
                    indices_cos = pickle.load(fh)
                cos_sim = np.load(r'pages/cos_sim.npy')       
                def recommendations(name, cos_sim = cos_sim):
                
                    recommended_hotel = []
                    if len(df[df['Name'] == name]) != 0:

                        idx = indices_cos[indices_cos == name].index[0]

                        score_series = pd.Series(cos_sim[idx]).sort_values(ascending = False)

                        top_10_indexes = list(score_series.iloc[1:11].index)
                    
                        for i in top_10_indexes:
                            recommended_hotel.append(list(df.Name)[i])
                        
                    return recommended_hotel
                a = pd.DataFrame(recommendations(name))
                a.columns=['Recommendations']
                st.write(a)
        


    st.header("Input gambar makanan:")
    uploaded_file = st.file_uploader("Pilih gambar...", type="jpg")
    if uploaded_file is not None:
        gambar = Image.open(uploaded_file)
        st.image(gambar, caption='Uploaded file', width=300)
        # st.write("")
        # st.write("Classifying...")
        label = teachable_machine_classification(gambar)
        # st.write(label)
        getRecipe(label)
        #recommendations(label)
        # if len(df[df['Name'] == name]) != 0:
        #     a = pd.DataFrame(recommendations(label))
        #     a.columns=['Recommendations']
        #     st.write(a)
