import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
import pyrebase
from src.func.analys_func import importation_of_dataset, pearson_corr,visualize_single_correlation,histplot
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
                "Voir les analogies entre les varibales et le diabète",
                ["Vue d'ensemble",
                 "IMC", 
                 "Pression artérielle(HighBP)",
                 "Cholestérol(HighChol)", 
                 "Alcoolémie",
               
                 ],

                ["IMC"],
            )

            with st.sidebar.expander("**Paramètres avancés**"):
                var_secondaires = st.radio(
                    "**Variables secondaires**",
                    ("", "Indicateurs liés à la santé du sujet", 
                        "Indicateurs relatifs au mode de vie du sujet", 
                        "Caractéristiques sociaux",
                        # "Matrice de corrélation"
                    ),
            )
           
           
           
            deconnexion = st.sidebar.button("Déconnexion")
            if deconnexion:
                st.session_state.logged_in = False
                st.session_state.last_login_time = None
                st.rerun()

            # path = "diabetes_prediction_dataset.csv"
            path = "new_diabetes_binary.csv"
            data = importation_of_dataset(path)
            

           
            if values:
                age_category_selected = []
                for key, value in age_mapping.items():
                    if values[0] <= key[0] and values[1] >= key[1]:
                        age_category_selected.append(value)
                    # else :
                    #     st.write("Selectionnez une plage valide")

                splited_data = data[data["Age"].isin(age_category_selected)] 
               
                if "Vue d'ensemble" in champs0:
                    # st.subheader("**Corrélation entre tous les paramètres**")
                    # st.subheader('Corrélation entre tous les paramètres', divider='rainbow')
                    st.subheader("**Matrice de corrélation**", divider='rainbow')
                    st.info(
                                "**Analyse de corrélation entre les variables cliniques et le diabète : une exploration du coefficient de corrélation de Pearson**"
                            )
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(pearson_corr(data))
                        st.stop()
                        
                if "Pression artérielle(HighBP)" in champs0:
                    st.subheader("**Corrélation entre le diabète et la pression artérielle (HighBP)**", divider='rainbow')
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(visualize_single_correlation("HighBP",splited_data,"HighBP.svg"))
                        st.stop()

                if "Cholestérol(HighChol)" in champs0:
                    st.subheader("**Corrélation entre le diabète et le taux de cholestérol(HighChol)**", divider='rainbow')
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(visualize_single_correlation("HighChol",splited_data,"HighChol.svg"))
                        st.stop()

                if "IMC" in champs0:
                    st.subheader("**Corrélation entre le diabète et l'indice de masse corporel(BMI)'**", divider='rainbow')
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(histplot(splited_data,"BMI","BMI.svg"))
                        st.stop()

                if "Alcoolémie" in champs0:
                    st.subheader("**Corrélation entre le diabète et la dépendance à l'alcool(HvyAlcoholConsump)**", divider='rainbow')
                    # c1, c2, c3 = st.columns((2, 2, 2))

                    with st.container():
                        
                        st.write("**Visualisations**")
                        st.pyplot(visualize_single_correlation("HvyAlcoholConsump",splited_data,"HvyAlcoholConsump.svg"))
                        st.stop()
                    
                
                if var_secondaires == "Indicateurs liés à la santé du sujet":
                    st.subheader("**Indicateurs liés à la santé du sujet**", divider='rainbow')
                    # st.markdown('**This is a string that explains something above.**')

                    choix_sante_sujet= st.multiselect(
                        "Selectionnez un/des paramètres",
                        [ "Santé mentale(MentHlth)", "Difficultés motrices(DiffWalk)", "AVC(Stroke)", "Infarctus|Maladies du coeur", "Etat de santé général"],
                        ["Difficultés motrices(DiffWalk)"],
                    )
                    
                    # st.subheader("**Hommes**")
                    if "Difficultés motrices(DiffWalk)" in choix_sante_sujet:
                        with st.container():
                            st.info(
                                "**Distribution des sujets selon leur dyspraxie motrice**"
                            )
                            st.pyplot(visualize_single_correlation("DiffWalk",splited_data,"DiffWalk.svg"))
                            st.stop()

                    if "AVC(Stroke)" in choix_sante_sujet:
                        with st.container():
                            st.info(
                                "**Distribution des sujets selon qu'ils aient déjà eu un avc ou pas**"
                            )
                            st.pyplot(visualize_single_correlation("Stroke",splited_data,"Stroke.svg"))
                            st.stop()

                    if "Santé mentale(MentHlth)" in choix_sante_sujet:
                        with st.container():
                            st.info(
                                "**Distribution des sujets selon le etat de santé emotionnel(le stress, la dépression ...)**"
                            )
                            st.pyplot(visualize_single_correlation("MentHlth",splited_data,"MentHlth.svg"))
                            st.stop()
                    
                    if "Infarctus|Maladies du coeur" in choix_sante_sujet:
                        with st.container():
                            st.info(
                                "**Distribution des sujets selon qu'ils aient déjà eu une maladie coronarienne (CHD) ou un infarctus du myocarde**"
                            )
                            st.pyplot(visualize_single_correlation("HeartDiseaseorAttack",splited_data,"HeartDiseaseorAttack.svg"))
                            st.stop()

                    if "Etat de santé général" in choix_sante_sujet:
                        with st.container():
                            st.info(
                                "**Distribution des sujets selon leur état de santé en général**"
                            )
                            st.pyplot(visualize_single_correlation("GenHlth",splited_data,"GenHlth.svg"))
                            st.stop()

                if var_secondaires =="Indicateurs relatifs au mode de vie du sujet":
                    st.subheader("**Indicateurs relatifs au mode de vie du sujet**", divider='rainbow')
                    choix_mode_de_vie= st.multiselect(
                        "Selectionnez un/des paramètres",
                        [ "Activité physique(PhysActivity)", "Alimentation en légumes(Veggies)", "Alimentation en fruits(Fruits)"],
                        ["Activité physique(PhysActivity)"],
                    )

                    if "Activité physique(PhysActivity)" in choix_mode_de_vie:
                        with st.container():
                            st.info(
                                "**Distribution des sujets selon leur fréquence d'activité physique**"
                            )
                            st.pyplot(visualize_single_correlation("PhysActivity",splited_data,"PhysActivity.svg"))
                            st.stop()
                    
                    if "Alimentation en légumes(Veggies)" in choix_mode_de_vie:
                        with st.container():
                            st.info(
                                "**Distribution des sujets selon leur fréquence d'activité physique**"
                            )
                            st.pyplot(visualize_single_correlation("Veggies",splited_data,"Veggies.svg"))
                            st.stop()
                    
                    if "Alimentation en fruits(Fruits)" in choix_mode_de_vie:
                        with st.container():
                            st.info(
                                "**Distribution des sujets selon leur fréquence d'activité physique**"
                            )
                            st.pyplot(visualize_single_correlation("Fruits",splited_data,"Fruits.svg"))
                            st.stop()

                if var_secondaires =="Caractéristiques sociaux":
                    st.subheader("**Caractéristiques sociaux**", divider='rainbow')
                    choix_mode_de_vie= st.multiselect(
                        "Selectionnez un/des paramètres",
                        [ "Age", "Sexe"],
                        ["Age"],
                    )

                    if "Age" in choix_mode_de_vie:
                        with st.container():
                            st.info(
                                "**Distribution des sujets selon leur âge**"
                            )
                            st.pyplot(visualize_single_correlation("Age",splited_data,"Age.svg"))
                            st.stop()
                    
                    if "Sexe" in choix_mode_de_vie:
                        with st.container():
                            st.info(
                                "**Distribution des sujets selon leur genre**"
                            )
                            st.pyplot(visualize_single_correlation("Sex",splited_data,"Sex.svg"))
                            st.stop()

              






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
        st.rerun()
        
   








# **************************************************************************************

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import time
# import pyrebase
# from src.func.analys_func import importation_of_dataset, pearson_corr, visualize_single_correlation, histplot

# firebaseConfig = {
#     'apiKey': "AIzaSyB6h3v8I9oTFeohknaKYAtN85sRC3_SR7o",
#     'authDomain': "diabeteforecast.firebaseapp.com",
#     'projectId': "diabeteforecast",
#     'storageBucket': "diabeteforecast.appspot.com",
#     'databaseURL': "https://diabeteforecast-default-rtdb.firebaseio.com/",
#     'messagingSenderId': "791146271892",
#     'appId': "1:791146271892:web:24b258c39a6656818c1081",
#     'measurementId': "G-0CG1BRGGNC"
# }

# firebase = pyrebase.initialize_app(firebaseConfig)
# auth = firebase.auth()
# db = firebase.database()
# storage = firebase.storage()

# st.set_option('deprecation.showPyplotGlobalUse', False)


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



# # def register(email, password):
# #     username = st.sidebar.text_input("Enter your username", value="John DOE")
# #     submit = st.sidebar.button("S'inscrire") 
# #     if submit:
# #         user = auth.create_user_with_email_and_password(email, password)
# #         st.success("Votre compte a été crée avec succès")
# #         st.balloons()
# #         # signin
# #         user = auth.sign_in_with_email_and_password(email, password)
# #         db.child(user['localId']).child("Username").set(username)
# #         db.child(user['localId']).child("ID").set(user['localId'])
# #         st.title("Welcome "+ username)
# #         # Définir la session comme connectée
# #         st.session_state.logged_in = True
# #         show_protected_content()
# #      



# def show_protected_content():
#     st.sidebar.header("Paramètres de visualisation des analogies")
#     age_mapping = {
#         (18, 24): 1,
#         (25, 29): 2,
#         (30, 34): 3,
#         (35, 39): 4,
#         (40, 44): 5,
#         (45, 49): 6,
#         (50, 54): 7,
#         (55, 59): 8,
#         (60, 64): 9,
#         (65, 69): 10,
#         (70, 74): 11,
#         (75, 80): 12,
#         (80, 84): 13,
#     }

#     values = st.slider("Sélectionnez la tranche d'âge :", min_value=18, max_value=80, value=(18, 80))

#     champs0 = st.sidebar.multiselect(
#         "Voir les analogies entre les variables et le diabète",
#         ["Vue d'ensemble", "IMC", "Pression artérielle(HighBP)", "Cholestérol(HighChol)", "Alcoolémie"],
#         ["IMC"],
#     )

#     with st.sidebar.expander("**Paramètres avancés**"):
#         var_secondaires = st.radio(
#             "**Variables secondaires**",
#             ("", "Indicateurs liés à la santé du sujet", "Indicateurs relatifs au mode de vie du sujet", "Caractéristiques sociaux"),
#         )

#     deconnexion = st.sidebar.button("Déconnexion")
#     if deconnexion:
#         st.session_state.logged_in = False
#         st.session_state.last_login_time = None
#         st.rerun()

#     path = "new_diabetes_binary.csv"
#     data = importation_of_dataset(path)

#     if values:
#         age_category_selected = [value for key, value in age_mapping.items() if values[0] <= key[0] and values[1] >= key[1]]
#         splited_data = data[data["Age"].isin(age_category_selected)]

#         if "Vue d'ensemble" in champs0:
#             st.subheader("**Matrice de corrélation**", divider='rainbow')
#             st.info("**Analyse de corrélation entre les variables cliniques et le diabète : une exploration du coefficient de corrélation de Pearson**")
#             st.pyplot(pearson_corr(data))

#         if "Pression artérielle(HighBP)" in champs0:
#             st.subheader("**Corrélation entre le diabète et la pression artérielle (HighBP)**", divider='rainbow')
#             st.pyplot(visualize_single_correlation("HighBP", splited_data, "HighBP.svg"))

#         if "Cholestérol(HighChol)" in champs0:
#             st.subheader("**Corrélation entre le diabète et le taux de cholestérol(HighChol)**", divider='rainbow')
#             st.pyplot(visualize_single_correlation("HighChol", splited_data, "HighChol.svg"))

#         if "IMC" in champs0:
#             st.subheader("**Corrélation entre le diabète et l'indice de masse corporel(BMI)'**", divider='rainbow')
#             st.pyplot(histplot(splited_data, "BMI", "BMI.svg"))

#         if "Alcoolémie" in champs0:
#             st.subheader("**Corrélation entre le diabète et la dépendance à l'alcool(HvyAlcoholConsump)**", divider='rainbow')
#             st.pyplot(visualize_single_correlation("HvyAlcoholConsump", splited_data, "HvyAlcoholConsump.svg"))

#         if var_secondaires == "Indicateurs liés à la santé du sujet":
#             st.subheader("**Indicateurs liés à la santé du sujet**", divider='rainbow')
#             choix_sante_sujet = st.multiselect(
#                 "Selectionnez un/des paramètres",
#                 ["Santé mentale(MentHlth)", "Difficultés motrices(DiffWalk)", "Difficultés physiques(PhysHlth)"],
#                 ["Santé mentale(MentHlth)"],
#             )
#             if "Santé mentale(MentHlth)" in choix_sante_sujet:
#                 st.pyplot(visualize_single_correlation("MentHlth", splited_data, "menthlth.svg"))
#             if "Difficultés motrices(DiffWalk)" in choix_sante_sujet:
#                 st.pyplot(visualize_single_correlation("DiffWalk", splited_data, "DiffWalk.svg"))
#             if "Difficultés physiques(PhysHlth)" in choix_sante_sujet:
#                 st.pyplot(visualize_single_correlation("PhysHlth", splited_data, "PhysHlth.svg"))

#         if var_secondaires == "Indicateurs relatifs au mode de vie du sujet":
#             st.subheader("**Indicateurs relatifs au mode de vie du sujet**", divider='rainbow')
#             choix_sante_sujet = st.multiselect(
#                 "Selectionnez un/des paramètres",
#                 ["Alimentation 5 fruits et légumes(Fruits)", "Activité sportive(PhysActivity)", "Consommation de fumée(Smoker)"],
#                 ["Alimentation 5 fruits et légumes(Fruits)"],
#             )
#             if "Alimentation 5 fruits et légumes(Fruits)" in choix_sante_sujet:
#                 st.pyplot(visualize_single_correlation("Fruits", splited_data, "Fruits.svg"))
#             if "Activité sportive(PhysActivity)" in choix_sante_sujet:
#                 st.pyplot(visualize_single_correlation("PhysActivity", splited_data, "PhysActivity.svg"))
#             if "Consommation de fumée(Smoker)" in choix_sante_sujet:
#                 st.pyplot(visualize_single_correlation("Smoker", splited_data, "Smoker.svg"))

#         if var_secondaires == "Caractéristiques sociaux":
#             st.subheader("**Caractéristiques sociaux**", divider='rainbow')
#             choix_sante_sujet = st.multiselect(
#                 "Selectionnez un/des paramètres",
#                 ["Revenu annuel de la famille(Income)", "Education level", "Géographie du pays (State)"],
#                 ["Revenu annuel de la famille(Income)"],
#             )
#             if "Revenu annuel de la famille(Income)" in choix_sante_sujet:
#                 st.pyplot(visualize_single_correlation("Income", splited_data, "Income.svg"))
#             if "Education level" in choix_sante_sujet:
#                 st.pyplot(visualize_single_correlation("Education", splited_data, "Education.svg"))
#             if "Géographie du pays (State)" in choix_sante_sujet:
#                 st.pyplot(visualize_single_correlation("State", splited_data, "State.svg"))

# if __name__ == "__main__":
#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False
#         st.session_state.last_login_time = None

#     if not st.session_state.logged_in:
#         st.sidebar.header("Connexion")
#         email = st.sidebar.text_input("Email")
#         password = st.sidebar.text_input("Password", type="password")
#         if st.sidebar.button("Login"):
#             try:
#                 user = auth.sign_in_with_email_and_password(email, password)
#                 st.session_state.logged_in = True
#                 st.session_state.last_login_time = time.time()
#                 st.success("Connexion réussie")
#                 st.sidebar.success("Connexion réussie")
#                 st.experimental_rerun()
#             except:
#                 st.error("Email ou mot de passe incorrect")
#     else:
#         show_protected_content()








