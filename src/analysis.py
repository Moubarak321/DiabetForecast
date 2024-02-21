import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
import pyrebase
from src.func.analys_func import importation_of_dataset, visualize_corr,visualize_single_correlation,histplot
#  diabetics, scatter, histplot, densite,



firebaseConfig = {
  'apiKey': "AIzaSyB6h3v8I9oTFeohknaKYAtN85sRC3_SR7o",
  'authDomain': "diabeteforecast.firebaseapp.com",
  'projectId': "diabeteforecast",
  'storageBucket': "diabeteforecast.appspot.com",
  'databaseURL': "https://diabeteforecast-default-rtdb.firebaseio.com/",
  'messagingSenderId': "791146271892",
  'appId': "1:791146271892:web:24b258c39a6656818c1081",
  'measurementId': "G-0CG1BRGGNC"
}



# auth
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# database
db = firebase.database()
storage = firebase.storage()

# Age 
# Genre
# BMI
# Glucose
# Cholesterol
st.set_option('deprecation.showPyplotGlobalUse', False)



def show_protected_content():
            st.sidebar.header("Paramètres de visualisation des annalogies")
            # viz_type = st.sidebar.selectbox("Type de visualisation", ('Variables générales', 'Paramètres'))

            # Mapping des plages d'âge
            age_mapping = {
                (18, 24): 1,
                (25, 29): 2,
                (30, 34): 3,
                (35, 39): 4,
                (40, 44): 5,
                (45, 49): 6,
                (50, 54): 7,
                (55, 59): 8,
                (60, 64): 9,
                (65, 69): 10,
                (70, 74): 11,
                (75, 80): 12,
                (80, 84): 13,
                # Ajoutez les autres plages d'âge...
            }

            # Liste des clés du mapping (valeurs du slider)
            values = st.slider("Sélectionnez la tranche d'âge :", min_value=18, max_value=80, value=(18, 80))
            # st.write("", values)

            champs0 = st.sidebar.multiselect(
                "Variables générales",
                ["Vue d'ensemble",
                 "IMC", 
                 "Pression artérielle(HighBP)",
                 "Cholestérol(HighChol)", 
                 "Propension à la cigarette",
                 "Alcoolémie",
                #  "Activité physique",
                #  "Alimentation en fruits", 
                #  "Alimentation en légumes",
                #  "AVC",
                #  "Infactus",
                #  "Fréquence de consultation", 
                # #  "Etat de santé",
                # #  "Santé mentale", 
                #  "Age",
                #  "Sexe",
                 ],

                ["Vue d'ensemble"],
            )

            with st.sidebar.expander("**Paramètres avancés**"):
                var_secondaires = st.radio(
                    "**Variables secondaires**",
                    ("", "Indicateurs liés à la santé du sujet", 
                        "Indicateurs relatifs au mode de vie du sujet", 
                        "Indicateurs relatifs aux soins de santé",
                        "Caractéristiques sociaux"
                    ),
            )
            # champs1 = st.sidebar.multiselect(
            #     "Indicateurs liés à la santé du sujet",
            #     [
            #     "Test","zaazazazaz","Vue d'ensemble"
            #      ],

            #     ["Vue d'ensemble"],
            # )

            # champs2 = st.sidebar.multiselect(
            #     "Indicateurs relatifs aux soins de santé",
            #     [
            #                     "Test","zaazazazaz","Vue d'ensemble"

            #      ],

            #     ["Vue d'ensemble"],
            # )

            # champs3 = st.sidebar.multiselect(
            #     "Indicateurs relatifs au mode de vie du sujet",
            #     [
            #                     "Test","zaazazazaz","Vue d'ensemble"

            #      ],

            #     ["Vue d'ensemble"],
            # )
            # champs4 = st.sidebar.multiselect(
            #     "Caractéristiques sociaux",
            #     [
            #                     "Test","zaazazazaz","Vue d'ensemble"

            #      ],

            #     ["Vue d'ensemble"],
            # )


           
           
            deconnexion = st.sidebar.button("Déconnexion")
            if deconnexion:
                st.session_state.logged_in = False
                st.session_state.last_login_time = None
                st.rerun()

            # path = "diabetes_prediction_dataset.csv"
            path = "new_diabetes_binary.csv"
            data = importation_of_dataset(path)
            

            # ================ Selectionnez un/des indicateurs ================
            # if values:
            #     splited_data = data.loc[
            #         (data["Age"] >= values[0]) & (data["Age"] <= values[1])
            #     ]
            if values:
                age_category_selected = []
                for key, value in age_mapping.items():
                    if values[0] <= key[0] and values[1] >= key[1]:
                        age_category_selected.append(value)
                    # else :
                    #     st.write("Selectionnez une plage valide")

                splited_data = data[data["Age"].isin(age_category_selected)] 
               
                if "Vue d'ensemble" in champs0:
                    st.subheader("**Corrélation entre tous les paramètres**")
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(visualize_corr(splited_data))
                        
                if "Pression artérielle(HighBP)" in champs0:
                    st.subheader("**Corrélation entre le diabète et la pression artérielle (HighBP)**")
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(visualize_single_correlation("HighBP",splited_data,"HighBP.svg"))

                if "Cholestérol(HighChol)" in champs0:
                    st.subheader("**Corrélation entre le diabète et le taux de cholestérol(HighChol)**")
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(visualize_single_correlation("HighChol",splited_data,"HighChol.svg"))

                if "IMC" in champs0:
                    st.subheader("**Corrélation entre le diabète et l'indice de masse corporel(BMI)'**")
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(histplot(splited_data,"BMI","BMI.svg"))

                if "Alcoolémie" in champs0:
                    st.subheader("**Corrélation entre le diabète et la dépendance à l'alcool(HvyAlcoholConsump)**")
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(visualize_single_correlation("HvyAlcoholConsump",splited_data,"HvyAlcoholConsump.svg"))
                    
                if "Activité physique" in champs0:
                    st.subheader("**Corrélation entre le diabète et la fréquence d'activité physique(PhysActivity)**")
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(visualize_single_correlation("PhysActivity",splited_data,"PhysActivity.svg"))

                if "Alimentation en fruits" in champs0:
                    st.subheader("**Corrélation entre le diabète et la fréquence de consommation de fruits(Fruits)**")
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(visualize_single_correlation("Fruits",splited_data,"Fruits.svg"))
                                  
                if "Alimentation en légumes" in champs0:
                    st.subheader("**Corrélation entre le diabète et la fréquence de consommation de légumes(Veggies)**")
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(visualize_single_correlation("Veggies",splited_data,"Veggies.svg"))
              
                if "AVC" in champs0:
                    st.subheader("**Corrélation entre le diabète et la fréquence d'accidents cardio-vasculaires(Stroke)**")
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(visualize_single_correlation("Stroke",splited_data,"Stroke.svg"))

                if "Infactus" in champs0:
                    st.subheader("**Corrélation entre le diabète et la fréquence d'infarctus(HeartDiseaseorAttack)**")
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(visualize_single_correlation("HeartDiseaseorAttack",splited_data,"HeartDiseaseorAttack.svg"))
               
                if "Fréquence de consultation" in champs0:
                    st.subheader("**Corrélation entre le diabète et la Fréquence de consultation médicale(NoDocbcCost)**")
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(visualize_single_correlation("NoDocbcCost",splited_data,"NoDocbcCost.svg"))
              
                if "Age" in champs0:
                    st.subheader("**Corrélation entre le diabète et l'age'**")
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(visualize_single_correlation("Age",splited_data,"Age.svg"))
                          
                if "Sexe" in champs0:
                    st.subheader("**Corrélation entre le diabète et le sexe du sujet**")
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(visualize_single_correlation("Sex",splited_data,"Sex.svg"))

                

                # ==============================================================
                # debut var secondaire
                # ==============================================================
                
                if var_secondaires == "Indicateurs liés à la santé du sujet":
                    st.subheader("**Indicateurs liés à la santé du sujet**")
                    # st.markdown('**This is a string that explains something above.**')

                    choix_sante_sujet= st.multiselect(
                        "Selectionnez un/des paramètres",
                        [ "Santé mentale(MentHlth)", "Difficultés motrices(DiffWalk)", "AVC(Stroke)", "Infarctus|Maladies du coeur", "Etat de santé général"],
                        ["Difficultés motrices(DiffWalk)"],
                    )
                    
                    # st.subheader("**Hommes**")
                    if "Difficultés motrices(DiffWalk)" in choix_sante_sujet:
                        with st.container():
                            st.markdown(
                                "**Distribution des sujets selon leur dyspraxie motrice**"
                            )
                            st.pyplot(visualize_single_correlation("DiffWalk",splited_data,"DiffWalk.svg"))

                    if "AVC(Stroke)" in choix_sante_sujet:
                        with st.container():
                            st.markdown(
                                "**Distribution des sujets selon qu'ils aient déjà eu un avc ou pas**"
                            )
                            st.pyplot(visualize_single_correlation("Stroke",splited_data,"Stroke.svg"))

                    if "Santé mentale(MentHlth)" in choix_sante_sujet:
                        with st.container():
                            st.markdown(
                                "**Distribution des sujets selon le etat de santé emotionnel(le stress, la dépression ...)**"
                            )
                            st.pyplot(visualize_single_correlation("MentHlth",splited_data,"MentHlth.svg"))
                    
                    if "Infarctus|Maladies du coeur" in choix_sante_sujet:
                        with st.container():
                            st.markdown(
                                "**Distribution des sujets selon qu'ils aient déjà eu une maladie coronarienne (CHD) ou un infarctus du myocarde**"
                            )
                            st.pyplot(visualize_single_correlation("HeartDiseaseorAttack",splited_data,"HeartDiseaseorAttack.svg"))

                    if "Etat de santé général" in choix_sante_sujet:
                        with st.container():
                            st.markdown(
                                "**Distribution des sujets selon leur état de santé en général**"
                            )
                            st.pyplot(visualize_single_correlation("GenHlth",splited_data,"GenHlth.svg"))

               






def login(email, password):
    submit = st.sidebar.button("Connexion") 
    if submit:
        # signin
        user = auth.sign_in_with_email_and_password(email, password)
        usernamedata =db.child(user['localId']).child("Username").get()
        if usernamedata:
            username = usernamedata.val()

            print(username)
            st.title("Welcome " + username)
            # Définir la session comme connectée
            st.session_state.logged_in = True
            show_protected_content()
            st.rerun()



def register(email, password):
    username = st.sidebar.text_input("Enter your username", value="John DOE")
    submit = st.sidebar.button("S'inscrire") 
    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        st.success("Votre compte a été crée avec succès")
        st.balloons()
        # signin
        user = auth.sign_in_with_email_and_password(email, password)
        db.child(user['localId']).child("Username").set(username)
        db.child(user['localId']).child("ID").set(user['localId'])
        st.title("Welcome "+ username)
        # Définir la session comme connectée
        st.session_state.logged_in = True
        show_protected_content()
        st.rerun()

def data_viz():
    with open('style.css') as f:
       
        st.sidebar.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    # st.sidebar.markdown(f'<div class="image-container"><img src="https://github.com/Moubarak321/DiabetForecast/blob/main/images/dia1.png?raw=true" alt="Ma superbe image"></div>', unsafe_allow_html=True)
       
        # Vérifier si l'utilisateur est connecté avant d'afficher le formulaire de connexion
    if not ("logged_in" in st.session_state and st.session_state.logged_in):
        # Afficher le formulaire de connexion
        st.info("👈Authentifiez vous pour accéder aux données")
        menu = st.sidebar.selectbox("Authentifiez-vous", ["Connexion", "Inscription"])
        email = st.sidebar.text_input("Your email adress", placeholder="Email")
        password = st.sidebar.text_input("Your password",placeholder="Mot de passe",type="password")
        
        if menu == "Inscription":
            register(email, password)

        elif menu == "Connexion":
            login(email, password)

    # Vérifier si l'utilisateur est connecté avant d'afficher le contenu protégé
    if "logged_in" in st.session_state and st.session_state.logged_in:
        st.empty()
        show_protected_content()
   




























































































































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
    

# Vérifiez si l'utilisateur est connecté



























































































































# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import time
# import pyrebase
# from src.func.analys_func import importation_of_dataset, diabetics, scatter, histplot, densite




# firebaseConfig = {
#   'apiKey': "AIzaSyB6h3v8I9oTFeohknaKYAtN85sRC3_SR7o",
#   'authDomain': "diabeteforecast.firebaseapp.com",
#   'projectId': "diabeteforecast",
#   'storageBucket': "diabeteforecast.appspot.com",
#   'databaseURL': "https://diabeteforecast-default-rtdb.firebaseio.com/",
#   'messagingSenderId': "791146271892",
#   'appId': "1:791146271892:web:24b258c39a6656818c1081",
#   'measurementId': "G-0CG1BRGGNC"
# }



# # auth
# firebase = pyrebase.initialize_app(firebaseConfig)
# auth = firebase.auth()

# # database
# db = firebase.database()
# storage = firebase.storage()

# # Age 
# # Genre
# # BMI
# # Glucose
# # Cholesterol
# st.set_option('deprecation.showPyplotGlobalUse', False)



# def show_protected_content():
#         st.sidebar.header("Paramètres de visualisation de données")
#         # viz_type = st.sidebar.selectbox("Type de visualisation", ('Variables générales', 'Paramètres'))

#         values = st.slider(
#             "**Selectionnez une plage d'age pour la visualisation**", 1, 80, (1, 80)
#         )
#         st.write("", values)

#         champs0 = st.sidebar.multiselect(
#             "Voir les analogies",
#             ["Vue d'ensemble","Age" ,"IMC", "Glucose", "Hypertension", "Cardio"],
#             ["Vue d'ensemble"],
#         )

#         champs1 = st.sidebar.multiselect(
#             "Selectionnez un/des indicateurs",
#             ["Age", "IMC", "Glucose", "Hypertension", "Cardio"],
#             ["Age"],
#         )

#         with st.sidebar.expander("**Paramètres avancés**"):
#             genre = st.radio(
#                 "**Distribution des diabétiques selon le genre**",
#                 ("", "Hommes", "Femmes", "Similitudes"),
#             )
        
#         deconnexion = st.sidebar.button("Déconnexion")
#         if deconnexion:
#             st.session_state.logged_in = False
#             st.session_state.last_login_time = None
#             st.rerun()

#         # path = "diabetes_prediction_dataset.csv"
#         path = "new_diabetes_binary.csv"
#         data = importation_of_dataset(path)
#         # st.write(data)

#         Diabetics = diabetics(data)

#         mens = Diabetics.loc[Diabetics["gender"] == "Male"]
#         female = Diabetics.loc[Diabetics["gender"] == "Female"]

#         # ================ Selectionnez un/des indicateurs ================
#         if values:
#             splited_data = Diabetics.loc[
#                 (Diabetics["age"] >= values[0]) & (Diabetics["age"] <= values[1])
#             ]
#             if "Age" in champs1:
#                 st.subheader("**Distribution des diabétiques selon l'âge**")
#                 c1, c2, c3 = st.columns((2, 2, 2))

#                 with st.container():
#                     with c1:
#                         st.write("**Nuage de point**")
#                         st.pyplot(scatter(data=splited_data, col="age"))
#                     with c2:
#                         st.write("**Diagramme en bande**")
#                         st.pyplot(histplot(data=splited_data, col="age"))
#                     with c3:
#                         st.write("**Histogramme**")
#                         st.pyplot(densite(data=splited_data, col="age"))

#             if "IMC" in champs1:
#                 st.subheader(
#                     "**Distribution des diabétiques selon l'indice de masse corporelle.**"
#                 )
#                 c1, c2, c3 = st.columns((2, 2, 2))

#                 with st.container():
#                     with c1:
#                         st.write("**Nuage de point**")
#                         st.pyplot(scatter(data=Diabetics, col="bmi"))
#                     with c2:
#                         st.write("**Diagramme en bande**")
#                         st.pyplot(histplot(data=Diabetics, col="bmi"))
#                     with c3:
#                         st.write("**Histogramme**")
#                         st.pyplot(densite(data=Diabetics, col="bmi"))

#             if "Glucose" in champs1:
#                 st.subheader("**Distribution des diabétiques selon leur taux de glucose**")
#                 c1, c2, c3 = st.columns((2, 2, 2))

#                 with st.container():
#                     with c1:
#                         st.write("**Nuage de point**")
#                         st.pyplot(scatter(data=Diabetics, col="blood_glucose_level"))
#                     with c2:
#                         st.write("**Diagramme en bande**")
#                         st.pyplot(histplot(data=Diabetics, col="blood_glucose_level"))
#                     with c3:
#                         st.write("**Histogramme**")
#                         st.pyplot(densite(data=Diabetics, col="blood_glucose_level"))

#             if "Hypertension" in champs1:
#                 st.subheader(
#                     "**Distribution des diabétiques selon qu'ils soient hypertendus**"
#                 )
#                 c1, c2, c3 = st.columns((2, 2, 2))

#                 with st.container():
#                     with c1:
#                         st.write("**Nuage de point**")
#                         st.pyplot(scatter(data=Diabetics, col="hypertension"))
#                     with c2:
#                         st.write("**Diagramme en bande**")
#                         st.pyplot(histplot(data=Diabetics, col="hypertension"))
#                     with c3:
#                         st.write("**Histogramme**")
#                         st.pyplot(densite(data=Diabetics, col="hypertension"))

#             if "Cardio" in champs1:
#                 st.subheader(
#                     "**Distribution des diabétiques qu'ils soient atteints de maladies cardiaques**"
#                 )
#                 c1, c2, c3 = st.columns((2, 2, 2))

#                 with st.container():
#                     with c1:
#                         st.write("**Nuage de point**")
#                         st.pyplot(scatter(data=Diabetics, col="heart_disease"))
#                     with c2:
#                         st.write("**Diagramme en bande**")
#                         st.pyplot(histplot(data=Diabetics, col="heart_disease"))
#                     with c3:
#                         st.write("**Histogramme**")
#                         st.pyplot(densite(data=Diabetics, col="heart_disease"))

#             # =========================== Distribution de l'homme ===========================

#             if genre == "Hommes":
#                 st.subheader("**Rapports de genre dans la distribution des diabétiques**")
#                 # st.markdown('**This is a string that explains something above.**')

#                 champs3 = st.multiselect(
#                     "Selectionnez un/des paramètres",
#                     ["IMC", "Age", "Glucose", "Hypertension", "Cardio"],
#                     ["IMC"],
#                 )
#                 splited_men = mens.loc[
#                     (mens["age"] >= values[0]) & (mens["age"] <= values[1])
#                 ]

#                 st.subheader("**Hommes**")
#                 if "Age" in champs3:
#                     with st.container():
#                         st.markdown(
#                             "**Distribution des hommes diabétiques selon leur age**"
#                         )

#                         c1, c2, c3 = st.columns((2, 2, 2))
#                         with c1:
#                             st.write("**Nuage de point**")
#                             st.pyplot(scatter(data=splited_men, col="age"))
#                         with c2:
#                             st.write("**Diagramme en bande**")
#                             st.pyplot(histplot(data=splited_men, col="age"))
#                         with c3:
#                             st.write("**Histogramme**")
#                             st.pyplot(densite(data=splited_men, col="age"))

#                 if "IMC" in champs3:
#                     with st.container():
#                         st.markdown("**Distribution des hommes selon leur IMC**")

#                         c1, c2, c3 = st.columns((2, 2, 2))
#                         with c1:
#                             st.write("**Nuage de point**")
#                             st.pyplot(scatter(data=splited_men, col="bmi"))
#                         with c2:
#                             st.write("**Diagramme en bande**")
#                             st.pyplot(histplot(data=splited_men, col="bmi"))
#                         with c3:
#                             st.write("**Histogramme**")
#                             st.pyplot(densite(data=splited_men, col="bmi"))

#                 if "Glucose" in champs3:
#                     with st.container():
#                         st.markdown("**Distribution des diabétiques leur taux de glucose**")

#                         c1, c2, c3 = st.columns((2, 2, 2))
#                         with c1:
#                             st.write("**Nuage de point**")
#                             st.pyplot(scatter(data=splited_men, col="blood_glucose_level"))
#                         with c2:
#                             st.write("**Diagramme en bande**")
#                             st.pyplot(histplot(data=splited_men, col="blood_glucose_level"))
#                         with c3:
#                             st.write("**Histogramme**")
#                             st.pyplot(densite(data=splited_men, col="blood_glucose_level"))

#                 if "Hypertension" in champs3:
#                     with st.container():
#                         st.markdown(
#                             "**Distribution des diabétiques selon qu'ils soient hypertendus**"
#                         )

#                         c1, c2, c3 = st.columns((2, 2, 2))
#                         with c1:
#                             st.write("**Nuage de point**")
#                             st.pyplot(scatter(data=splited_men, col="hypertension"))
#                         with c2:
#                             st.write("**Diagramme en bande**")
#                             st.pyplot(histplot(data=splited_men, col="hypertension"))
#                         with c3:
#                             st.write("**Histogramme**")
#                             st.pyplot(densite(data=splited_men, col="hypertension"))

#                 if "Cardio" in champs3:
#                     with st.container():
#                         st.markdown("**Distribution des diabétiques selon leur cadio**")

#                         c1, c2, c3 = st.columns((2, 2, 2))
#                         with c1:
#                             st.write("**Nuage de point**")
#                             st.pyplot(scatter(data=splited_men, col="heart_disease"))
#                         with c2:
#                             st.write("**Diagramme en bande**")
#                             st.pyplot(histplot(data=splited_men, col="heart_disease"))
#                         with c3:
#                             st.write("**Histogramme**")
#                             st.pyplot(densite(data=splited_men, col="heart_disease"))

#             # =========================== Distribution des femmes ===========================

#             if genre == "Femmes":
#                 st.subheader("**Rapports de genre dans la distribution des diabétiques**")
#                 champs3 = st.multiselect(
#                     "Selectionnez un/des paramètres",
#                     ["Age", "IMC", "Glucose", "Hypertension", "Cardio"],
#                     ["Age"],
#                 )

#                 splited_female = female.loc[
#                     (female["age"] >= values[0]) & (female["age"] <= values[1])
#                 ]

#                 st.subheader("**Femmes**")
#                 if "Age" in champs3:
#                     with st.container():
#                         st.markdown(
#                             "**Distribution des femmes diabétiques selon leur age**"
#                         )

#                         c1, c2, c3 = st.columns((2, 2, 2))
#                         with c1:
#                             st.write("**Nuage de point**")
#                             st.pyplot(scatter(data=splited_female, col="age"))
#                         with c2:
#                             st.write("**Diagramme en bande**")
#                             st.pyplot(histplot(data=splited_female, col="age"))
#                         with c3:
#                             st.write("**Histogramme**")
#                             st.pyplot(densite(data=splited_female, col="age"))

#                 if "IMC" in champs3:
#                     with st.container():
#                         st.markdown(
#                             "**Distribution des hommes diabetiques selon leur imc**"
#                         )

#                         c1, c2, c3 = st.columns((2, 2, 2))
#                         with c1:
#                             st.write("**Nuage de point**")
#                             st.pyplot(scatter(data=splited_female, col="bmi"))
#                         with c2:
#                             st.write("**Diagramme en bande**")
#                             st.pyplot(histplot(data=splited_female, col="bmi"))
#                         with c3:
#                             st.write("**Histogramme**")
#                             st.pyplot(densite(data=splited_female, col="bmi"))

#                 if "Glucose" in champs3:
#                     with st.container():
#                         st.markdown(
#                             "**Distribution des hommes selon leur taux de glucose**"
#                         )

#                         c1, c2, c3 = st.columns((2, 2, 2))
#                         with c1:
#                             st.write("**Nuage de point**")
#                             st.pyplot(
#                                 scatter(data=splited_female, col="blood_glucose_level")
#                             )
#                         with c2:
#                             st.write("**Diagramme en bande**")
#                             st.pyplot(
#                                 histplot(data=splited_female, col="blood_glucose_level")
#                             )
#                         with c3:
#                             st.write("**Histogramme**")
#                             st.pyplot(
#                                 densite(data=splited_female, col="blood_glucose_level")
#                             )

#                 if "Hypertension" in champs3:
#                     with st.container():
#                         st.markdown(
#                             "**Distribution des diabétiques selon qu'ils soient hypertendus**"
#                         )

#                         c1, c2, c3 = st.columns((2, 2, 2))
#                         with c1:
#                             st.write("**Nuage de point**")
#                             st.pyplot(scatter(data=splited_female, col="hypertension"))
#                         with c2:
#                             st.write("**Diagramme en bande**")
#                             st.pyplot(histplot(data=splited_female, col="hypertension"))
#                         with c3:
#                             st.write("**Histogramme**")
#                             st.pyplot(densite(data=splited_female, col="hypertension"))

#                 if "Cardio" in champs3:
#                     with st.container():
#                         st.markdown(
#                             "**Distribution des diabétiques selon qu'ils soient hypertendus**"
#                         )

#                         c1, c2, c3 = st.columns((2, 2, 2))
#                         with c1:
#                             st.write("**Nuage de point**")
#                             st.pyplot(scatter(data=splited_female, col="heart_disease"))
#                         with c2:
#                             st.write("**Diagramme en bande**")
#                             st.pyplot(histplot(data=splited_female, col="heart_disease"))
#                         with c3:
#                             st.write("**Histogramme**")
#                             st.pyplot(densite(data=splited_female, col="heart_disease"))

#             # =========================== Similitudes ===========================

#             if genre == "Similitudes":
#                 st.subheader("**Rapports de genre dans la distribution des diabétiques**")
#                 champs3 = st.multiselect(
#                     "Selectionnez un/des paramètres",
#                     ["Glucose", "IMC", "Age", "Hypertension", "Cardio"],
#                     ["Glucose"],
#                 )

#                 splited_female = female.loc[
#                     (female["age"] >= values[0]) & (female["age"] <= values[1])
#                 ]
#                 splited_men = mens.loc[
#                     (mens["age"] >= values[0]) & (mens["age"] <= values[1])
#                 ]

#                 st.subheader("**Similitudes**")
#                 if "Age" in champs3:
#                     with st.container():
#                         st.markdown(
#                             "**Comparaison des hommes et femmes diabétiques selon leur age**"
#                         )

#                         c1, c2 = st.columns((3, 3))
#                         with c1:
#                             st.write("**Hommes**")
#                             st.pyplot(histplot(data=splited_men, col="age"))
#                         with c2:
#                             st.write("**Femmes**")

#                             st.pyplot(histplot(data=splited_female, col="age"))

#                 if "IMC" in champs3:
#                     with st.container():
#                         st.markdown(
#                             "**Comparaison des hommes et femmes diabétiques selon leur IMC**"
#                         )

#                         c1, c2 = st.columns((3, 3))
#                         with c1:
#                             st.write("**Hommes**")
#                             st.pyplot(histplot(data=splited_men, col="bmi"))
#                         with c2:
#                             st.write("**Femmes**")

#                             st.pyplot(histplot(data=splited_female, col="bmi"))

#                 if "Glucose" in champs3:
#                     with st.container():
#                         st.markdown(
#                             "**Comparaison des hommes et femmes diabétiques selon leur taux de glucose**"
#                         )

#                         c1, c2 = st.columns((3, 3))
#                         with c1:
#                             st.write("**Hommes**")
#                             st.pyplot(histplot(data=splited_men, col="blood_glucose_level"))
#                         with c2:
#                             st.write("**Femmes**")

#                             st.pyplot(
#                                 histplot(data=splited_female, col="blood_glucose_level")
#                             )

#                 if "Hypertension" in champs3:
#                     with st.container():
#                         st.markdown(
#                             "**Comparaison des hommes et femmes diabétiques selon qu'ils soient hypertendus**"
#                         )

#                         c1, c2 = st.columns((3, 3))
#                         with c1:
#                             st.write("**Hommes**")
#                             st.pyplot(histplot(data=splited_men, col="hypertension"))
#                         with c2:
#                             st.write("**Femmes**")

#                             st.pyplot(histplot(data=splited_female, col="hypertension"))

#                 if "Cardio" in champs3:
#                     with st.container():
#                         st.markdown(
#                             "**Comparaison des hommes et femmes diabétiques selon leur cardio**"
#                         )

#                         c1, c2 = st.columns((3, 3))
#                         with c1:
#                             st.write("**Hommes**")
#                             st.pyplot(histplot(data=splited_men, col="heart_disease"))
#                         with c2:
#                             st.write("**Femmes**")

#                             st.pyplot(histplot(data=splited_female, col="heart_disease"))


# def login(email, password):
#     submit = st.sidebar.button("Connexion") 
#     if submit:
#         # signin
#         user = auth.sign_in_with_email_and_password(email, password)
#         usernamedata =db.child(user['localId']).child("Username").get()
#         if usernamedata:
#             username = usernamedata.val()

#             print(username)
#             st.title("Welcome " + username)
#             # Définir la session comme connectée
#             st.session_state.logged_in = True
#             show_protected_content()
#             st.rerun()



# def register(email, password):
#     username = st.sidebar.text_input("Enter your username", value="John DOE")
#     submit = st.sidebar.button("S'inscrire") 
#     if submit:
#         user = auth.create_user_with_email_and_password(email, password)
#         st.success("Votre compte a été crée avec succès")
#         st.balloons()
#         # signin
#         user = auth.sign_in_with_email_and_password(email, password)
#         db.child(user['localId']).child("Username").set(username)
#         db.child(user['localId']).child("ID").set(user['localId'])
#         st.title("Welcome "+ username)
#         # Définir la session comme connectée
#         st.session_state.logged_in = True
#         show_protected_content()
#         st.rerun()

# def data_viz():
#     with open('style.css') as f:
       
#         st.sidebar.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
#     # st.sidebar.markdown(f'<div class="image-container"><img src="https://github.com/Moubarak321/DiabetForecast/blob/main/images/dia1.png?raw=true" alt="Ma superbe image"></div>', unsafe_allow_html=True)
       
#         # Vérifier si l'utilisateur est connecté avant d'afficher le formulaire de connexion
#     if not ("logged_in" in st.session_state and st.session_state.logged_in):
#         # Afficher le formulaire de connexion
#         st.info("👈Authentifiez vous pour accéder aux données")
#         menu = st.sidebar.selectbox("Authentifiez-vous", ["Connexion", "Inscription"])
#         email = st.sidebar.text_input("Your email adress", placeholder="Email")
#         password = st.sidebar.text_input("Your password",placeholder="Mot de passe",type="password")
        
#         if menu == "Inscription":
#             register(email, password)

#         elif menu == "Connexion":
#             login(email, password)

#     # Vérifier si l'utilisateur est connecté avant d'afficher le contenu protégé
#     if "logged_in" in st.session_state and st.session_state.logged_in:
#         st.empty()
#         show_protected_content()
   


