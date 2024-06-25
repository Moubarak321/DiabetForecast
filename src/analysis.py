
import streamlit as st
import pandas as pd
import time
import pyrebase
from src.func.analys_func import importation_of_dataset, pearson_corr, visualize_single_correlation, histplot

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

# Auth and database initialization
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

# Mapping des plages d'âge
age_mapping = {
    (18, 24): 1, (25, 29): 2, (30, 34): 3, (35, 39): 4, (40, 44): 5,
    (45, 49): 6, (50, 54): 7, (55, 59): 8, (60, 64): 9, (65, 69): 10,
    (70, 74): 11, (75, 80): 12, (80, 84): 13,
}

st.set_option('deprecation.showPyplotGlobalUse', False)

def show_protected_content():
    st.sidebar.header("Paramètres de visualisation des analogies")
    values = st.slider("Sélectionnez la tranche d'âge :", min_value=18, max_value=80, value=(18, 80))

    champs0 = st.sidebar.multiselect(
        "Voir les analogies entre les variables et le diabète",
        ["Vue d'ensemble", "IMC", "Pression artérielle(HighBP)", "Cholestérol(HighChol)", "Alcoolémie"],
        ["IMC"]
    )

    with st.sidebar.expander("**Paramètres avancés**"):
        var_secondaires = st.radio(
            "**Variables secondaires**",
            ("", "Indicateurs liés à la santé du sujet", "Indicateurs relatifs au mode de vie du sujet", "Caractéristiques sociaux")
        )

    deconnexion = st.sidebar.button("Déconnexion")
    if deconnexion:
        st.session_state.logged_in = False
        st.session_state.last_login_time = None
        st.experimental_rerun()

    path = "new_diabetes_binary.csv"
    data = importation_of_dataset(path)

    if values:
        age_category_selected = []
        for key, value in age_mapping.items():
            if values[0] <= key[0] and values[1] >= key[1]:
                age_category_selected.append(value)

        splited_data = data[data["Age"].isin(age_category_selected)]

        if "Vue d'ensemble" in champs0:
            st.subheader("**Matrice de corrélation**", divider='rainbow')
            st.info("**Analyse de corrélation entre les variables cliniques et le diabète : une exploration du coefficient de corrélation de Pearson**")
            st.write("**Visualisations**")
            st.write(pearson_corr(data))

        if "Pression artérielle(HighBP)" in champs0:
            st.subheader("**Corrélation entre le diabète et la pression artérielle (HighBP)**", divider='rainbow')
            st.write("**Visualisations**")
            st.write(visualize_single_correlation("HighBP", splited_data, "HighBP.svg"))

        if "Cholestérol(HighChol)" in champs0:
            st.subheader("**Corrélation entre le diabète et le taux de cholestérol(HighChol)**", divider='rainbow')
            st.write("**Visualisations**")
            st.write(visualize_single_correlation("HighChol", splited_data, "HighChol.svg"))

        if "IMC" in champs0:
            st.subheader("**Corrélation entre le diabète et l'indice de masse corporel(BMI)**", divider='rainbow')
            st.write("**Visualisations**")
            st.write(histplot(splited_data, "BMI", "BMI.svg"))

        if "Alcoolémie" in champs0:
            st.subheader("**Corrélation entre le diabète et la dépendance à l'alcool(HvyAlcoholConsump)**", divider='rainbow')
            st.write("**Visualisations**")
            st.write(visualize_single_correlation("HvyAlcoholConsump", splited_data, "HvyAlcoholConsump.svg"))

        if var_secondaires == "Indicateurs liés à la santé du sujet":
            st.subheader("**Indicateurs liés à la santé du sujet**", divider='rainbow')
            choix_sante_sujet = st.multiselect(
                "Selectionnez un/des paramètres",
                ["Santé mentale(MentHlth)", "Difficultés motrices(DiffWalk)", "AVC(Stroke)", "Infarctus|Maladies du coeur", "Etat de santé général"],
                ["Difficultés motrices(DiffWalk)"]
            )

            if "Difficultés motrices(DiffWalk)" in choix_sante_sujet:
                st.info("**Distribution des sujets selon leur dyspraxie motrice**")
                st.write(visualize_single_correlation("DiffWalk", splited_data, "DiffWalk.svg"))

            if "AVC(Stroke)" in choix_sante_sujet:
                st.info("**Distribution des sujets selon qu'ils aient déjà eu un avc ou pas**")
                st.write(visualize_single_correlation("Stroke", splited_data, "Stroke.svg"))

            if "Santé mentale(MentHlth)" in choix_sante_sujet:
                st.info("**Distribution des sujets selon le état de santé émotionnel(le stress, la dépression ...)**")
                st.write(visualize_single_correlation("MentHlth", splited_data, "MentHlth.svg"))

            if "Infarctus|Maladies du coeur" in choix_sante_sujet:
                st.info("**Distribution des sujets selon qu'ils aient déjà eu une maladie coronarienne (CHD) ou un infarctus du myocarde**")
                st.write(visualize_single_correlation("HeartDiseaseorAttack", splited_data, "HeartDiseaseorAttack.svg"))

            if "Etat de santé général" in choix_sante_sujet:
                st.info("**Distribution des sujets selon leur état de santé en général**")
                st.write(visualize_single_correlation("GenHlth", splited_data, "GenHlth.svg"))

        if var_secondaires == "Indicateurs relatifs au mode de vie du sujet":
            st.subheader("**Indicateurs relatifs au mode de vie du sujet**", divider='rainbow')
            choix_mode_de_vie = st.multiselect(
                "Selectionnez un/des paramètres",
                ["Activité physique(PhysActivity)", "Alimentation en légumes(Veggies)", "Alimentation en fruits(Fruits)"],
                ["Activité physique(PhysActivity)"]
            )

            if "Activité physique(PhysActivity)" in choix_mode_de_vie:
                st.info("**Distribution des sujets selon leur fréquence d'activité physique**")
                st.write(visualize_single_correlation("PhysActivity", splited_data, "PhysActivity.svg"))

            if "Alimentation en légumes(Veggies)" in choix_mode_de_vie:
                st.info("**Distribution des sujets selon leur fréquence de consommation de légumes**")
                st.write(visualize_single_correlation("Veggies", splited_data, "Veggies.svg"))

            if "Alimentation en fruits(Fruits)" in choix_mode_de_vie:
                st.info("**Distribution des sujets selon leur fréquence de consommation de fruits**")
                st.write(visualize_single_correlation("Fruits", splited_data, "Fruits.svg"))

        if var_secondaires == "Caractéristiques sociaux":
            st.subheader("**Caractéristiques sociaux**", divider='rainbow')
            choix_caracteristiques_sociaux = st.multiselect(
                "Selectionnez un/des paramètres",
                ["Age", "Sexe"],
                ["Age"]
            )

            if "Age" in choix_caracteristiques_sociaux:
                st.info("**Distribution des sujets selon leur âge**")
                st.write(visualize_single_correlation("Age", splited_data, "Age.svg"))

            if "Sexe" in choix_caracteristiques_sociaux:
                st.info("**Distribution des sujets selon leur genre**")
                st.write(visualize_single_correlation("Sex", splited_data, "Sex.svg"))


def login(email, password):       
    submit = st.sidebar.button("Connexion")
    if submit:
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.success("Connexion réussie!")
            st.session_state.logged_in = True
            st.session_state.last_login_time = time.time()
            st.experimental_rerun()
        except Exception as e:
            st.error("Erreur de connexion, veuillez vérifier vos informations")

def register(email, password):
    username = st.sidebar.text_input("Enter your username", placeholder="Nom d'utilisateur")
    submit = st.sidebar.button("Créer un compte")
    if submit:
        try:
            user = auth.create_user_with_email_and_password(email, password)
            st.success("Compte créé avec succès. Veuillez patienter un instant.")
            st.balloons()
            # signin
            user = auth.sign_in_with_email_and_password(email, password)
            db.child(user['localId']).child("Username").set(username)
            db.child(user['localId']).child("ID").set(user['localId'])
            st.session_state.logged_in = True
            st.title("Welcome "+ username)
            st.experimental_rerun()
            
            # Définir la session comme connectée
            # show_protected_content()
        except Exception as e:
            st.error("Erreur lors de la création du compte. Veuillez réessayer.")

def display_login_signup():
    login_choice = st.sidebar.selectbox("Choisissez une option", ["Connexion", "Inscription"])
    email = st.sidebar.text_input("Email",placeholder="Votre adresse mail")
    password = st.sidebar.text_input("Password",placeholder="Mot de passe", type="password")
    
    if login_choice == "Connexion":
        login(email, password)
    else:
        register(email, password)

def main():
    with open('style.css') as f:
       
       st.sidebar.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.last_login_time = None

    if not st.session_state.logged_in:
        st.info("👈Authentifiez vous pour accéder aux données")
        st.sidebar.header("Authentification")
        display_login_signup()
    else:
        show_protected_content()

if __name__ == "__main__":
    main()








# *************ancien code qui fonctionnait mais à crashé
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import time
# import pyrebase
# from src.func.analys_func import importation_of_dataset, pearson_corr,visualize_single_correlation,histplot
# #  diabetics, scatter, histplot, densite,



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
#             st.sidebar.header("Paramètres de visualisation des annalogies")
#             # viz_type = st.sidebar.selectbox("Type de visualisation", ('Variables générales', 'Paramètres'))

#             # Mapping des plages d'âge
#             age_mapping = {
#                 (18, 24): 1,
#                 (25, 29): 2,
#                 (30, 34): 3,
#                 (35, 39): 4,
#                 (40, 44): 5,
#                 (45, 49): 6,
#                 (50, 54): 7,
#                 (55, 59): 8,
#                 (60, 64): 9,
#                 (65, 69): 10,
#                 (70, 74): 11,
#                 (75, 80): 12,
#                 (80, 84): 13,
#                 # Ajoutez les autres plages d'âge...
#             }

#             # Liste des clés du mapping (valeurs du slider)
#             values = st.slider("Sélectionnez la tranche d'âge :", min_value=18, max_value=80, value=(18, 80))
#             # st.write("", values)

#             champs0 = st.sidebar.multiselect(
#                 "Voir les analogies entre les varibales et le diabète",
#                 ["Vue d'ensemble",
#                  "IMC", 
#                  "Pression artérielle(HighBP)",
#                  "Cholestérol(HighChol)", 
#                  "Alcoolémie",
               
#                  ],

#                 ["IMC"],
#             )

#             with st.sidebar.expander("**Paramètres avancés**"):
#                 var_secondaires = st.radio(
#                     "**Variables secondaires**",
#                     ("", "Indicateurs liés à la santé du sujet", 
#                         "Indicateurs relatifs au mode de vie du sujet", 
#                         "Caractéristiques sociaux",
#                         # "Matrice de corrélation"
#                     ),
#             )
           
           
           
#             deconnexion = st.sidebar.button("Déconnexion")
#             if deconnexion:
#                 st.session_state.logged_in = False
#                 st.session_state.last_login_time = None
#                 st.rerun()

#             # path = "diabetes_prediction_dataset.csv"
#             path = "new_diabetes_binary.csv"
#             data = importation_of_dataset(path)
            

#             st.set_option('deprecation.showPyplotGlobalUse', False)
           
#             if values:
#                 age_category_selected = []
#                 for key, value in age_mapping.items():
#                     if values[0] <= key[0] and values[1] >= key[1]:
#                         age_category_selected.append(value)
#                     # else :
#                     #     st.write("Selectionnez une plage valide")

#                 splited_data = data[data["Age"].isin(age_category_selected)] 
               
#                 if "Vue d'ensemble" in champs0:
#                     # st.subheader("**Corrélation entre tous les paramètres**")
#                     # st.subheader('Corrélation entre tous les paramètres', divider='rainbow')
#                     st.subheader("**Matrice de corrélation**", divider='rainbow')
#                     st.info(
#                                 "**Analyse de corrélation entre les variables cliniques et le diabète : une exploration du coefficient de corrélation de Pearson**"
#                             )
#                     # c1, c2, c3 = st.columns((2, 2, 2))

#                     with st.container():
                        
#                         st.write("**Visualisations**")
#                         st.write(pearson_corr(data))

                        
                        
#                 if "Pression artérielle(HighBP)" in champs0:
#                     st.subheader("**Corrélation entre le diabète et la pression artérielle (HighBP)**", divider='rainbow')
#                     # c1, c2, c3 = st.columns((2, 2, 2))

#                     with st.container():
                        
#                         st.write("**Visualisations**")
#                         st.write(visualize_single_correlation("HighBP",splited_data,"HighBP.svg"))
#                         # st.stop()

#                 if "Cholestérol(HighChol)" in champs0:
#                     st.subheader("**Corrélation entre le diabète et le taux de cholestérol(HighChol)**", divider='rainbow')
#                     # c1, c2, c3 = st.columns((2, 2, 2))

#                     with st.container():
                        
#                         st.write("**Visualisations**")
#                         st.write(visualize_single_correlation("HighChol",splited_data,"HighChol.svg"))
#                         # st.stop()
                
#                 if "IMC" in champs0:
#                     st.subheader("**Corrélation entre le diabète et l'indice de masse corporel(BMI)'**", divider='rainbow')
#                     # c1, c2, c3 = st.columns((2, 2, 2))

#                     with st.container():
                        
#                         st.write("**Visualisations**")
#                         st.write(histplot(splited_data,"BMI","BMI.svg"))
#                         # st.stop()
                        

#                 if "Alcoolémie" in champs0:
#                     st.subheader("**Corrélation entre le diabète et la dépendance à l'alcool(HvyAlcoholConsump)**", divider='rainbow')
#                     # c1, c2, c3 = st.columns((2, 2, 2))

#                     with st.container():
                        
#                         st.write("**Visualisations**")
#                         st.write(visualize_single_correlation("HvyAlcoholConsump",splited_data,"HvyAlcoholConsump.svg"))
#                         # st.stop()
                    
                
#                 if var_secondaires == "Indicateurs liés à la santé du sujet":
#                     st.subheader("**Indicateurs liés à la santé du sujet**", divider='rainbow')
#                     # st.markdown('**This is a string that explains something above.**')

#                     choix_sante_sujet= st.multiselect(
#                         "Selectionnez un/des paramètres",
#                         [ "Santé mentale(MentHlth)", "Difficultés motrices(DiffWalk)", "AVC(Stroke)", "Infarctus|Maladies du coeur", "Etat de santé général"],
#                         ["Difficultés motrices(DiffWalk)"],
#                     )
                    
#                     # st.subheader("**Hommes**")
#                     if "Difficultés motrices(DiffWalk)" in choix_sante_sujet:
#                         with st.container():
#                             st.info(
#                                 "**Distribution des sujets selon leur dyspraxie motrice**"
#                             )
#                             st.write(visualize_single_correlation("DiffWalk",splited_data,"DiffWalk.svg"))
#                             # st.stop()

#                     if "AVC(Stroke)" in choix_sante_sujet:
#                         with st.container():
#                             st.info(
#                                 "**Distribution des sujets selon qu'ils aient déjà eu un avc ou pas**"
#                             )
#                             st.write(visualize_single_correlation("Stroke",splited_data,"Stroke.svg"))
#                             # st.stop()

#                     if "Santé mentale(MentHlth)" in choix_sante_sujet:
#                         with st.container():
#                             st.info(
#                                 "**Distribution des sujets selon le etat de santé emotionnel(le stress, la dépression ...)**"
#                             )
#                             st.write(visualize_single_correlation("MentHlth",splited_data,"MentHlth.svg"))
#                             # st.stop()
                    
#                     if "Infarctus|Maladies du coeur" in choix_sante_sujet:
#                         with st.container():
#                             st.info(
#                                 "**Distribution des sujets selon qu'ils aient déjà eu une maladie coronarienne (CHD) ou un infarctus du myocarde**"
#                             )
#                             st.write(visualize_single_correlation("HeartDiseaseorAttack",splited_data,"HeartDiseaseorAttack.svg"))
#                             # st.stop()

#                     if "Etat de santé général" in choix_sante_sujet:
#                         with st.container():
#                             st.info(
#                                 "**Distribution des sujets selon leur état de santé en général**"
#                             )
#                             st.write(visualize_single_correlation("GenHlth",splited_data,"GenHlth.svg"))
#                             # st.stop()

#                 if var_secondaires =="Indicateurs relatifs au mode de vie du sujet":
#                     st.subheader("**Indicateurs relatifs au mode de vie du sujet**", divider='rainbow')
#                     choix_mode_de_vie= st.multiselect(
#                         "Selectionnez un/des paramètres",
#                         [ "Activité physique(PhysActivity)", "Alimentation en légumes(Veggies)", "Alimentation en fruits(Fruits)"],
#                         ["Activité physique(PhysActivity)"],
#                     )

#                     if "Activité physique(PhysActivity)" in choix_mode_de_vie:
#                         with st.container():
#                             st.info(
#                                 "**Distribution des sujets selon leur fréquence d'activité physique**"
#                             )
#                             st.write(visualize_single_correlation("PhysActivity",splited_data,"PhysActivity.svg"))
#                             # st.stop()
                    
#                     if "Alimentation en légumes(Veggies)" in choix_mode_de_vie:
#                         with st.container():
#                             st.info(
#                                 "**Distribution des sujets selon leur fréquence d'activité physique**"
#                             )
#                             st.write(visualize_single_correlation("Veggies",splited_data,"Veggies.svg"))
#                             # st.stop()
                    
#                     if "Alimentation en fruits(Fruits)" in choix_mode_de_vie:
#                         with st.container():
#                             st.info(
#                                 "**Distribution des sujets selon leur fréquence d'activité physique**"
#                             )
#                             st.write(visualize_single_correlation("Fruits",splited_data,"Fruits.svg"))
#                             # st.stop()

#                 if var_secondaires =="Caractéristiques sociaux":
#                     st.subheader("**Caractéristiques sociaux**", divider='rainbow')
#                     choix_mode_de_vie= st.multiselect(
#                         "Selectionnez un/des paramètres",
#                         [ "Age", "Sexe"],
#                         ["Age"],
#                     )

#                     if "Age" in choix_mode_de_vie:
#                         with st.container():
#                             st.info(
#                                 "**Distribution des sujets selon leur âge**"
#                             )
#                             st.write(visualize_single_correlation("Age",splited_data,"Age.svg"))
#                             # st.stop()
                    
#                     if "Sexe" in choix_mode_de_vie:
#                         with st.container():
#                             st.info(
#                                 "**Distribution des sujets selon leur genre**"
#                             )
#                             st.write(visualize_single_correlation("Sex",splited_data,"Sex.svg"))
#                             # st.stop()

              






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
#             st.empty()
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
#         st.empty()
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
#         st.rerun()
        
   











































# **************** def protected_content gpt/************
# def show_protected_content():
#     st.sidebar.header("Paramètres de visualisation des analogies")
#     values = st.slider("Sélectionnez la tranche d'âge :", min_value=18, max_value=80, value=(18, 80))

#     champs0 = st.sidebar.multiselect(
#         "Voir les analogies entre les variables et le diabète",
#         ["Vue d'ensemble", "IMC", "Pression artérielle(HighBP)", "Cholestérol(HighChol)", "Alcoolémie"],
#         ["IMC"]
#     )

#     with st.sidebar.expander("**Paramètres avancés**"):
#         var_secondaires = st.radio(
#             "**Variables secondaires**",
#             ("", "Indicateurs liés à la santé du sujet", "Indicateurs relatifs au mode de vie du sujet", "Caractéristiques sociaux")
#         )

#     deconnexion = st.sidebar.button("Déconnexion")
#     if deconnexion:
#         st.session_state.logged_in = False
#         st.session_state.last_login_time = None
#         st.experimental_rerun()

#     path = "new_diabetes_binary.csv"
#     data = importation_of_dataset(path)

#     if values:
#         age_category_selected = []
#         for key, value in age_mapping.items():
#             if values[0] <= key[0] and values[1] >= key[1]:
#                 age_category_selected.append(value)

#         splited_data = data[data["Age"].isin(age_category_selected)]

#         if "Vue d'ensemble" in champs0:
#             st.subheader("**Matrice de corrélation**", divider='rainbow')
#             st.info("**Analyse de corrélation entre les variables cliniques et le diabète : une exploration du coefficient de corrélation de Pearson**")
#             st.write("**Visualisations**")
#             st.write(pearson_corr(data))

#         if "Pression artérielle(HighBP)" in champs0:
#             st.subheader("**Corrélation entre le diabète et la pression artérielle (HighBP)**", divider='rainbow')
#             st.write("**Visualisations**")
#             st.write(visualize_single_correlation("HighBP", splited_data, "HighBP.svg"))

#         if "Cholestérol(HighChol)" in champs0:
#             st.subheader("**Corrélation entre le diabète et le taux de cholestérol(HighChol)**", divider='rainbow')
#             st.write("**Visualisations**")
#             st.write(visualize_single_correlation("HighChol", splited_data, "HighChol.svg"))

#         if "IMC" in champs0:
#             st.subheader("**Corrélation entre le diabète et l'indice de masse corporel(BMI)**", divider='rainbow')
#             st.write("**Visualisations**")
#             st.write(histplot(splited_data, "BMI", "BMI.svg"))

#         if "Alcoolémie" in champs0:
#             st.subheader("**Corrélation entre le diabète et la dépendance à l'alcool(HvyAlcoholConsump)**", divider='rainbow')
#             st.write("**Visualisations**")
#             st.write(visualize_single_correlation("HvyAlcoholConsump", splited_data, "HvyAlcoholConsump.svg"))

#         if var_secondaires == "Indicateurs liés à la santé du sujet":
#             st.subheader("**Indicateurs liés à la santé du sujet**", divider='rainbow')
#             choix_sante_sujet = st.multiselect(
#                 "Selectionnez un/des paramètres",
#                 ["Santé mentale(MentHlth)", "Difficultés motrices(DiffWalk)", "AVC(Stroke)", "Infarctus|Maladies du coeur", "Etat de santé général"],
#                 ["Difficultés motrices(DiffWalk)"]
#             )

#             for choix in choix_sante_sujet:
#                 if choix == "Difficultés motrices(DiffWalk)":
#                     st.info("**Distribution des sujets selon leur dyspraxie motrice**")
#                     st.write(visualize_single_correlation("DiffWalk", splited_data, "DiffWalk.svg"))

#                 if choix == "AVC(Stroke)":
#                     st.info("**Distribution des sujets selon qu'ils aient déjà eu un avc ou pas**")
#                     st.write(visualize_single_correlation("Stroke", splited_data, "Stroke.svg"))

#                 if choix == "Santé mentale(MentHlth)":
#                     st.info("**Distribution des sujets selon le état de santé émotionnel(le stress, la dépression ...)**")
#                     st.write(visualize_single_correlation("MentHlth", splited_data, "MentHlth.svg"))

#                 if choix == "Infarctus|Maladies du coeur":
#                     st.info("**Distribution des sujets selon qu'ils aient déjà eu une maladie coronarienne (CHD) ou un infarctus du myocarde**")
#                     st.write(visualize_single_correlation("HeartDiseaseorAttack", splited_data, "HeartDiseaseorAttack.svg"))

#                 if choix == "Etat de santé général":
#                     st.info("**Distribution des sujets selon leur état de santé en général**")
#                     st.write(visualize_single_correlation("GenHlth", splited_data, "GenHlth.svg"))

#         if var_secondaires == "Indicateurs relatifs au mode de vie du sujet":
#             st.subheader("**Indicateurs relatifs au mode de vie du sujet**", divider='rainbow')
#             choix_mode_de_vie = st.multiselect(
#                 "Selectionnez un/des paramètres",
#                 ["Activité physique(PhysActivity)", "Alimentation en légumes(Veggies)", "Alimentation en fruits(Fruits)"],
#                 ["Activité physique(PhysActivity)"]
#             )

#             for choix in choix_mode_de_vie:
#                 if choix == "Activité physique(PhysActivity)":
#                     st.info("**Distribution des sujets selon leur fréquence d'activité physique**")
#                     st.write(visualize_single_correlation("PhysActivity", splited_data, "PhysActivity.svg"))

#                 if choix == "Alimentation en légumes(Veggies)":
#                     st.info("**Distribution des sujets selon leur fréquence de consommation de légumes**")
#                     st.write(visualize_single_correlation("Veggies", splited_data, "Veggies.svg"))

#                 if choix == "Alimentation en fruits(Fruits)":
#                     st.info("**Distribution des sujets selon leur fréquence de consommation de fruits**")
#                     st.write(visualize_single_correlation("Fruits", splited_data, "Fruits.svg"))

#         if var_secondaires == "Caractéristiques sociaux":
#             st.subheader("**Caractéristiques sociaux**", divider='rainbow')
#             choix_caracteristiques_sociaux = st.multiselect(
#                 "Selectionnez un/des paramètres",
#                 ["Age", "Sexe"],
#                 ["Age"]
#             )

#             for choix in choix_caracteristiques_sociaux:
#                 if choix == "Age":
#                     st.info("**Distribution des sujets selon leur âge**")
#                     st.write(visualize_single_correlation("Age", splited_data, "Age.svg"))

#                 if choix == "Sexe":
#                     st.info("**Distribution des sujets selon leur genre**")
#                     st.write(visualize_single_correlation("Sex", splited_data, "Sex.svg"))




