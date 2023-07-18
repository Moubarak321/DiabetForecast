import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
from src.func.analys_func import importation_of_dataset, diabetics, scatter, histplot, densite

# Age 
# Genre
# BMI
# Glucose
# Cholesterol
st.set_option('deprecation.showPyplotGlobalUse', False)
def data_viz():
    st.sidebar.header("Paramètres de visualisation de données")
    # viz_type = st.sidebar.selectbox("Type de visualisation", ('Variables générales', 'Paramètres'))
   
    champs1 = st.sidebar.multiselect("Selectionnez un/des indicateurs", ['Age','IMC', 'Glucose', 'Hypertension', 'Cardio'],['Age'])
    with st.sidebar.expander("**Paramètres avancés**"):
        genre = st.radio(
        "Distribution des diabétiques selon le genre",
        ('Hommes', 'Femmes', 'Similitudes'))

    if genre == 'Comedy':
        st.write('You selected comedy.')
    else:
        st.write("You didn\'t select comedy.")
        
    path = "diabetes_prediction_dataset.csv"
    data = importation_of_dataset(path)
    st.write(data)

    Diabetics  = diabetics(data)
    # st.write(Diabetics)
    
    # c3 = st.columns((4))  

    if "Age" in champs1 :
        st.subheader('**Distribution des diabétiques selon l\'âge**')
        c1, c2 ,c3= st.columns((2, 2,2))

        with st.container():
            with c1:
                st.write("**Nuage de point**")
                st.pyplot(scatter(data = Diabetics, col="age"))
            with c2:
                st.write("**Diagramme en bande**")
                st.pyplot(histplot(data = Diabetics, col="age"))
            with c3:
                st.write("**Histogramme**")
                st.pyplot(densite(data = Diabetics, col="age"))
    
    if "IMC" in champs1 :
        st.subheader('**Distribution des diabétiques selon l\'indice de masse corporelle.**')
        c1, c2 ,c3= st.columns((2, 2,2))

        with st.container():
            with c1:
                st.write("**Nuage de point**")
                st.pyplot(scatter(data = Diabetics, col="bmi"))
            with c2:
                st.write("**Diagramme en bande**")
                st.pyplot(histplot(data = Diabetics, col="bmi"))
            with c3:
                st.write("**Histogramme**")
                st.pyplot(densite(data = Diabetics, col="bmi"))

    

    if "Glucose" in champs1 :
        st.subheader('**Distribution des diabétiques selon leur taux de glucose**')
        c1, c2 ,c3= st.columns((2, 2,2))

        with st.container():
            with c1:
                st.write("**Nuage de point**")
                st.pyplot(scatter(data = Diabetics, col="blood_glucose_level"))
            with c2:
                st.write("**Diagramme en bande**")
                st.pyplot(histplot(data = Diabetics, col="blood_glucose_level"))
            with c3:
                st.write("**Histogramme**")
                st.pyplot(densite(data = Diabetics, col="blood_glucose_level"))

    
    if "Hypertension" in champs1 :
        st.subheader('**Distribution des diabétiques selon qu\'ils soient hypertendus**')
        c1, c2 ,c3= st.columns((2, 2,2))

        with st.container():
            with c1:
                st.write("**Nuage de point**")
                st.pyplot(scatter(data = Diabetics, col="hypertension"))
            with c2:
                st.write("**Diagramme en bande**")
                st.pyplot(histplot(data = Diabetics, col="hypertension"))
            with c3:
                st.write("**Histogramme**")
                st.pyplot(densite(data = Diabetics, col="hypertension"))

    if "Cardio" in champs1 :
        st.subheader('**Distribution des diabétiques qu\'ils soient atteints de maladies cardiaques**')
        c1, c2 ,c3= st.columns((2, 2,2))

        with st.container():
            with c1:
                st.write("**Nuage de point**")
                st.pyplot(scatter(data = Diabetics, col="heart_disease"))
            with c2:
                st.write("**Diagramme en bande**")
                st.pyplot(histplot(data = Diabetics, col="heart_disease"))
            with c3:
                st.write("**Histogramme**")
                st.pyplot(densite(data = Diabetics, col="heart_disease"))

    