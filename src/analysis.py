import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
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
   

    values = st.slider(
    '**Selectionnez une plage d\'age pour la visualisation**',
    1, 80, (1, 80))
    st.write('', values)
    

    champs1 = st.sidebar.multiselect("Selectionnez un/des indicateurs", ['Age','IMC', 'Glucose', 'Hypertension', 'Cardio'],['Age'])

    with st.sidebar.expander("**Paramètres avancés**"):
        genre = st.radio(
        '**Distribution des diabétiques selon le genre**',
        ('','Hommes', 'Femmes', 'Similitudes'))  
    

    
    path = "diabetes_prediction_dataset.csv"
    data = importation_of_dataset(path)
    # st.write(data)

    Diabetics  = diabetics(data)
    
    mens  = Diabetics.loc[Diabetics['gender'] == 'Male']
    female  = Diabetics.loc[Diabetics['gender'] == 'Female']



    # ================ Selectionnez un/des indicateurs ================
    if values:
        splited_data = Diabetics.loc[(Diabetics['age'] >= values[0]) & (Diabetics['age'] <= values[1])]
        if "Age" in champs1 :
            st.subheader('**Distribution des diabétiques selon l\'âge**')
            c1, c2 ,c3= st.columns((2, 2,2))

            with st.container():
                with c1:
                    st.write("**Nuage de point**")
                    st.pyplot(scatter(data = splited_data, col="age"))
                with c2:
                    st.write("**Diagramme en bande**")
                    st.pyplot(histplot(data = splited_data, col="age"))
                with c3:
                    st.write("**Histogramme**")
                    st.pyplot(densite(data = splited_data, col="age"))
    
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






        # =========================== Distribution de l'homme ===========================
        if genre == 'Hommes':
            st.subheader('**Rapports de genre dans la distribution des diabétiques**')
            # st.markdown('**This is a string that explains something above.**')

            champs3 = st.multiselect("Selectionnez un/des paramètres", ['IMC','Age', 'Glucose', 'Hypertension', 'Cardio'],['IMC'])
            splited_men = mens.loc[(mens['age'] >= values[0]) & (mens['age'] <= values[1])]

            st.subheader('**Hommes**')
            if "Age" in champs3:
                with st.container():
                    st.markdown('**Distribution des hommes diabétiques selon leur age**')
                    

                    c1, c2 ,c3= st.columns((2, 2,2))
                    with c1:
                        st.write("**Nuage de point**")
                        st.pyplot(scatter(data = splited_men, col="age"))
                    with c2:
                        st.write("**Diagramme en bande**")
                        st.pyplot(histplot(data = splited_men, col="age"))
                    with c3:
                        st.write("**Histogramme**")
                        st.pyplot(densite(data = splited_men, col="age"))

            if "IMC" in champs3:
                with st.container():
                    st.markdown('**Distribution des hommes selon leur IMC**')

                    c1, c2 ,c3= st.columns((2, 2,2))
                    with c1:
                        st.write("**Nuage de point**")
                        st.pyplot(scatter(data = splited_men, col="bmi"))
                    with c2:
                        st.write("**Diagramme en bande**")
                        st.pyplot(histplot(data = splited_men, col="bmi"))
                    with c3:
                        st.write("**Histogramme**")
                        st.pyplot(densite(data = splited_men, col="bmi"))
            
            if "Glucose" in champs3:
                with st.container():
                    st.markdown('**Distribution des diabétiques leur taux de glucose**')

                    c1, c2 ,c3= st.columns((2, 2,2))
                    with c1:
                        st.write("**Nuage de point**")
                        st.pyplot(scatter(data = splited_men, col="blood_glucose_level"))
                    with c2:
                        st.write("**Diagramme en bande**")
                        st.pyplot(histplot(data = splited_men, col="blood_glucose_level"))
                    with c3:
                        st.write("**Histogramme**")
                        st.pyplot(densite(data = splited_men, col="blood_glucose_level"))

            if "Hypertension" in champs3:
                with st.container():
                    st.markdown('**Distribution des diabétiques selon qu\'ils soient hypertendus**')

                    c1, c2 ,c3= st.columns((2, 2,2))
                    with c1:
                        st.write("**Nuage de point**")
                        st.pyplot(scatter(data = splited_men, col="hypertension"))
                    with c2:
                        st.write("**Diagramme en bande**")
                        st.pyplot(histplot(data = splited_men, col="hypertension"))
                    with c3:
                        st.write("**Histogramme**")
                        st.pyplot(densite(data = splited_men, col="hypertension"))

            if "Cardio" in champs3:
                with st.container():
                    st.markdown('**Distribution des diabétiques selon leur cadio**')

                    c1, c2 ,c3= st.columns((2, 2,2))
                    with c1:
                        st.write("**Nuage de point**")
                        st.pyplot(scatter(data = splited_men, col="heart_disease"))
                    with c2:
                        st.write("**Diagramme en bande**")
                        st.pyplot(histplot(data = splited_men, col="heart_disease"))
                    with c3:
                        st.write("**Histogramme**")
                        st.pyplot(densite(data = splited_men, col="heart_disease"))


        # =========================== Distribution des femmes ===========================

        if genre == 'Femmes':
            st.subheader('**Rapports de genre dans la distribution des diabétiques**')
            champs3 = st.multiselect("Selectionnez un/des paramètres", ['Age','IMC', 'Glucose', 'Hypertension', 'Cardio'],['Age'])

            splited_female = female.loc[(female['age'] >= values[0]) & (female['age'] <= values[1])]

            st.subheader('**Femmes**')
            if "Age" in champs3:
                with st.container():
                    st.markdown('**Distribution des femmes diabétiques selon leur age**')

                    c1, c2 ,c3= st.columns((2, 2,2))
                    with c1:
                        st.write("**Nuage de point**")
                        st.pyplot(scatter(data = splited_female, col="age"))
                    with c2:
                        st.write("**Diagramme en bande**")
                        st.pyplot(histplot(data = splited_female, col="age"))
                    with c3:
                        st.write("**Histogramme**")
                        st.pyplot(densite(data = splited_female, col="age"))

            if "IMC" in champs3:
                with st.container():
                    st.markdown('**Distribution des hommes diabetiques selon leur imc**')

                    c1, c2 ,c3= st.columns((2, 2,2))
                    with c1:
                        st.write("**Nuage de point**")
                        st.pyplot(scatter(data = splited_female, col="bmi"))
                    with c2:
                        st.write("**Diagramme en bande**")
                        st.pyplot(histplot(data = splited_female, col="bmi"))
                    with c3:
                        st.write("**Histogramme**")
                        st.pyplot(densite(data = splited_female, col="bmi"))
            
            if "Glucose" in champs3:
                with st.container():
                    st.markdown('**Distribution des hommes selon leur taux de glucose**')

                    c1, c2 ,c3= st.columns((2, 2,2))
                    with c1:
                        st.write("**Nuage de point**")
                        st.pyplot(scatter(data = splited_female, col="blood_glucose_level"))
                    with c2:
                        st.write("**Diagramme en bande**")
                        st.pyplot(histplot(data = splited_female, col="blood_glucose_level"))
                    with c3:
                        st.write("**Histogramme**")
                        st.pyplot(densite(data = splited_female, col="blood_glucose_level"))

            if "Hypertension" in champs3:
                with st.container():
                    st.markdown('**Distribution des diabétiques selon qu\'ils soient hypertendus**')

                    c1, c2 ,c3= st.columns((2, 2,2))
                    with c1:
                        st.write("**Nuage de point**")
                        st.pyplot(scatter(data = splited_female, col="hypertension"))
                    with c2:
                        st.write("**Diagramme en bande**")
                        st.pyplot(histplot(data = splited_female, col="hypertension"))
                    with c3:
                        st.write("**Histogramme**")
                        st.pyplot(densite(data = splited_female, col="hypertension"))

            if "Cardio" in champs3:
                with st.container():
                    st.markdown('**Distribution des diabétiques selon qu\'ils soient hypertendus**')

                    c1, c2 ,c3= st.columns((2, 2,2))
                    with c1:
                        st.write("**Nuage de point**")
                        st.pyplot(scatter(data = splited_female, col="heart_disease"))
                    with c2:
                        st.write("**Diagramme en bande**")
                        st.pyplot(histplot(data = splited_female, col="heart_disease"))
                    with c3:
                        st.write("**Histogramme**")
                        st.pyplot(densite(data = splited_female, col="heart_disease"))







        # =========================== Similitudes ===========================


        if genre == 'Similitudes':
            st.subheader('**Rapports de genre dans la distribution des diabétiques**')
            champs3 = st.multiselect("Selectionnez un/des paramètres", ['Glucose','IMC', 'Age', 'Hypertension', 'Cardio'],['Glucose'])

            splited_female = female.loc[(female['age'] >= values[0]) & (female['age'] <= values[1])]
            splited_men = mens.loc[(mens['age'] >= values[0]) & (mens['age'] <= values[1])]


            st.subheader('**Similitudes**')
            if "Age" in champs3:
                with st.container():
                    st.markdown('**Comparaison des hommes et femmes diabétiques selon leur age**')

                    c1, c2 = st.columns((3, 3))
                    with c1:
                        st.write("**Hommes**")
                        st.pyplot(histplot(data = splited_men, col="age"))
                    with c2:
                        st.write("**Femmes**")

                        st.pyplot(histplot(data = splited_female, col="age"))
                    

            if "IMC" in champs3:
                with st.container():
                    st.markdown('**Comparaison des hommes et femmes diabétiques selon leur IMC**')

                    c1, c2 = st.columns((3, 3))
                    with c1:
                        st.write("**Hommes**")
                        st.pyplot(histplot(data = splited_men, col="bmi"))
                    with c2:
                        st.write("**Femmes**")

                        st.pyplot(histplot(data = splited_female, col="bmi"))
            
            if "Glucose" in champs3:
                with st.container():
                    st.markdown('**Comparaison des hommes et femmes diabétiques selon leur taux de glucose**')

                    c1, c2 = st.columns((3, 3))
                    with c1:
                        st.write("**Hommes**")
                        st.pyplot(histplot(data = splited_men, col="blood_glucose_level"))
                    with c2:
                        st.write("**Femmes**")

                        st.pyplot(histplot(data = splited_female, col="blood_glucose_level"))

            if "Hypertension" in champs3:
                with st.container():
                    st.markdown('**Comparaison des hommes et femmes diabétiques selon qu\'ils soient hypertendus**')

                    c1, c2 = st.columns((3, 3))
                    with c1:
                        st.write("**Hommes**")
                        st.pyplot(histplot(data = splited_men, col="hypertension"))
                    with c2:
                        st.write("**Femmes**")

                        st.pyplot(histplot(data = splited_female, col="hypertension"))

            if "Cardio" in champs3:
                with st.container():
                    st.markdown('**Comparaison des hommes et femmes diabétiques selon leur cardio**')

                    c1, c2 = st.columns((3, 3))
                    with c1:
                        st.write("**Hommes**")
                        st.pyplot(histplot(data = splited_men, col="heart_disease"))
                    with c2:
                        st.write("**Femmes**")

                        st.pyplot(histplot(data = splited_female, col="heart_disease"))               
























































































































        # if genre == 'Similitudes':

        #     champs3 = st.multiselect("Selectionnez", ['Glucose','IMC', 'Age', 'Hypertension', 'Cardio'],['Glucose'])
        #     splited_ = mens.loc[(mens['age'] >= values[0]) & (mens['age'] <= values[1])]

        #     st.subheader('**Smilitudes**')

        #     with st.container():
        #         st.subheader('***Distribution des hommes et femmes selon qu\'ils soient hypertendus***')

        #         c1, c2 ,c3= st.columns((2, 2,2))
        #         with c1:
        #             st.write("**Nuage de point**")
        #             st.pyplot(scatter(data = splited_, col="age"))
        #         with c2:
        #             st.write("**Diagramme en bande**")
        #             st.pyplot(histplot(data = splited_, col="age"))
        #         with c3:
        #             st.write("**Histogramme**")
        #             st.pyplot(densite(data = splited_, col="age"))

            
        #     with st.container():
        #         st.subheader('***Distribution des diabétiques selon qu\'ils soient hypertendus***')

        #         c1, c2 ,c3= st.columns((2, 2,2))
        #         with c1:
        #             st.write("**Nuage de point**")
        #             st.pyplot(scatter(data = splited_, col="bmi"))
        #         with c2:
        #             st.write("**Diagramme en bande**")
        #             st.pyplot(histplot(data = splited_, col="bmi"))
        #         with c3:
        #             st.write("**Histogramme**")
        #             st.pyplot(densite(data = splited_, col="bmi"))
            

        #     with st.container():
        #         st.subheader('***Distribution des diabétiques selon qu\'ils soient hypertendus***')

        #         c1, c2 ,c3= st.columns((2, 2,2))
        #         with c1:
        #             st.write("**Nuage de point**")
        #             st.pyplot(scatter(data = splited_, col="blood_glucose_level"))
        #         with c2:
        #             st.write("**Diagramme en bande**")
        #             st.pyplot(histplot(data = splited_, col="blood_glucose_level"))
        #         with c3:
        #             st.write("**Histogramme**")
        #             st.pyplot(densite(data = splited_, col="blood_glucose_level"))


        #     with st.container():
        #         st.subheader('***Distribution des diabétiques selon qu\'ils soient hypertendus***')

        #         c1, c2 ,c3= st.columns((2, 2,2))
        #         with c1:
        #             st.write("**Nuage de point**")
        #             st.pyplot(scatter(data = splited_, col="hypertension"))
        #         with c2:
        #             st.write("**Diagramme en bande**")
        #             st.pyplot(histplot(data = splited_, col="hypertension"))
        #         with c3:
        #             st.write("**Histogramme**")
        #             st.pyplot(densite(data = splited_, col="hypertension"))

            
        #     with st.container():
        #         st.subheader('***Distribution des diabétiques selon qu\'ils soient hypertendus***')

        #         c1, c2 ,c3= st.columns((2, 2,2))
        #         with c1:
        #             st.write("**Nuage de point**")
        #             st.pyplot(scatter(data = splited_, col="heart_disease"))
        #         with c2:
        #             st.write("**Diagramme en bande**")
        #             st.pyplot(histplot(data = splited_, col="heart_disease"))
        #         with c3:
        #             st.write("**Histogramme**")
        #             st.pyplot(densite(data = splited_, col="heart_disease"))




        # # else:
        #     st.write("You didn\'t select comedy.")
    