# # ==================================
#     # version finale
# # ==================================
# import numpy as np
# import streamlit as st
# import pickle
# from sklearn.ensemble import GradientBoostingClassifier
# import pandas as pd
# age = None
# BMI = None
# HighChol = None
# Sexe = None
# Highbp = None
# Fruit = None
# Genhlth = None
# MentHlth = None
# PhysHlth = None
# Smoke = None
# Diff = None

# def main():
#     global age, BMI, HighChol, Sexe, Highbp, Fruit, Genhlth, MentHlth, PhysHlth, Smoke, Diff
    

#     st.title("Évaluez votre état de santé")
#     age_mapping = {
#         "":"",
#         "18-24": 1,
#         "25-29": 2,
#         "30-34": 3,
#         "35-39": 4,
#         "40-44": 5,
#         "45-49": 6,
#         "50-54": 7,
#         "55-59": 8,
#         "60-64": 9,
#         "65-69": 10,
#         "70-74": 11,
#         "75-80": 12,
#         "80-84": 13,
#     }
#     ans = {
#         "":"",
#         "Non": 0,
#         "Oui": 1
#     }
#     genre = {
#         "":"",
#         "Homme": 1,
#         "Femme": 0
#     }
#     yes_or_no = {
#         "":"",
#         "Oui": 1,
#         "Non": 0
#     }
#     features = []

#     if "section" not in st.session_state:
#         st.session_state.section = 1
    
#     if st.session_state.section == 1:
#         st.subheader("Section 1: Informations générales")
#         with st.form("section1_form"):
#             age_ = st.selectbox("👉Entrez votre âge", list(age_mapping.keys()), index=None, placeholder="Selectionnez votre tranche d'âge",)
#             print(age_)
#             age = age_mapping[age_] if age_ else ""
#             BMI = st.number_input("👉Entrez votre indice de masse corporelle", placeholder="Entrez votre IMC", key="cgh")
#             chol = st.selectbox("Avez-vous un taux de cholestérol élevé ?", list(yes_or_no.keys()), index=None, placeholder="Sélectionnez une option")
#             HighChol = yes_or_no[chol] if chol else ""
#             if st.form_submit_button("Suivant", args="section1_next"):
#                 st.session_state.section = 2
#                 st.experimental_rerun()
#                 return


#     if st.session_state.section == 2:
#         st.subheader("Section 2: Habitudes de vie")
#         with st.form("section2_form"):
#             sexe_ = st.selectbox("👉Quel est votre genre", list(genre.keys()), index=None, key="b",placeholder="Sélectionnez une option")
#             Sexe = genre[sexe_] if sexe_ else ""
#             highbp_ = st.selectbox("👉Êtes-vous hypertendus ?", list(ans.keys()), index=None, key="skjdn",placeholder="Sélectionnez une option")
#             Highbp = ans[highbp_] if highbp_ else ""
#             fruit_ = st.selectbox("👉Consommez-vous au moins un fruit par jour ?", list(yes_or_no.keys()), index=None, key="skjv",placeholder="Sélectionnez une option")
#             Fruit = yes_or_no[fruit_] if fruit_ else ""
#             diffwalk = st.selectbox("👉Avez-vous des difficultés à marcher ou monter les escaliers ?", list(yes_or_no.keys()), index=None, key="sfkjv",placeholder="Sélectionnez une option")
#             Diff = yes_or_no[diffwalk] if diffwalk else ""
#             col1, col2 = st.columns(2)
#             print(f"2***************BMI: {BMI} ")
#             print(age_mapping["70-74"])
#             with col1:
#                 if st.form_submit_button("Retour", args="section2_back"):
#                     st.session_state.section = 1
#                     st.experimental_rerun()
                    
#                     return
                    
#             with col2:
#                 if st.form_submit_button("Suivant", args="section2_next"):
                   
#                     st.session_state.section = 3
#                     st.experimental_rerun()
                    
#                     return

#     if st.session_state.section == 3:
#         st.subheader("Section 3: État de santé")
#         with st.form("section3_form"):
#             Genhlth = st.selectbox("👉Quelle note sur 5 donneriez-vous à votre état de santé général ?", [""] + list(range(1, 6)),index=None, key="skssjv",placeholder="Sélectionnez une option")
#             PhysHlth = st.selectbox("👉Pendant combien de jours au cours des 30 derniers jours votre santé physique n'a-t-elle pas été bonne ?", [""] + list(range(1, 31)),index=None,placeholder="Sélectionnez une option", key="dddddg")
#             MentHlth = st.selectbox("👉Pensez maintenant à votre santé mentale, qui comprend le stress, la dépression et les problèmes émotionnels, pendant combien de jours au cours des 30 derniers jours votre santé mentale n'a-t-elle pas été bonne. ?", [""] + list(range(1, 31)),index=None, placeholder="Sélectionnez une option", key="eeeeeg")
#             smoke = st.selectbox("👉Avez-vous fumé au moins 100 cigarettes (05 paquets) au cours de votre vie ?", list(yes_or_no.keys()), index=None, key="h",)
#             Smoke = yes_or_no[smoke] if smoke else ""
            
#             col1, col2 = st.columns(2)
#             with col1:
#                 back =st.form_submit_button("Retour", args="section3_back")
#                 if back:
#                     st.session_state.section = 2
#                     st.experimental_rerun()
                    
#                     return
                    
#             with col2:
#                 bt = st.form_submit_button("Soumettre", args="section3_submit")
#             if bt:
#                 Highbp = int(Highbp)
#                 HighChol = int(HighChol)
#                 BMI = int(BMI)
#                 Smoke = int(Smoke)
#                 Fruit = int(Fruit)
#                 Genhlth = int(Genhlth)
#                 MentHlth = int(MentHlth)
#                 PhysHlth = int(PhysHlth)
#                 Diff = int(Diff)
#                 Sexe = int(Sexe)
#                 age = int(age)
#                 features = [Highbp,HighChol,BMI,Smoke,Fruit,Genhlth,MentHlth,PhysHlth,Diff,Sexe,age]
#                 features = np.array(features).reshape(1, -1)
#                 with open('new_GradientBoostingClassifier_boost.pkl', 'rb') as best_gradient_boost:
#                     modele_charge = pickle.load(best_gradient_boost)
#                     prediction = modele_charge.predict(features)
#                     if prediction ==1:
#                         st.error("Vous êtes susceptible d'être diabétique. Maintenez une activité sportive régulière, mangez beaucoup de fruits et legumes et surtout, consultez un spécialiste pour un examen plus approfondi ", icon="🚨")
#                     else:
#                         st.info("Vous ne présentez pas de risque d'être diabétique. Néanmoins, controlez vôtre alimentation, faites du sport et prévoyez une consultation auprès d'un spécialiste dans les jours à venir")
#                         print(features)
#                             # st.success("Vos données ont été enregistrées avec succès.")


#             # Enregistrement des informations dans un fichier CSV
#             feature_names = ["HighBP", "HighChol", "BMI", "Smoke", "Fruit", "GenHlth", "MentHlth", "PhysHlth", "DiffWalk", "Sex", "Age"]
#             df = pd.DataFrame(features, columns=feature_names)
#             # Ouverture du fichier CSV en mode append
#             with open("etat_de_sante_de_la_population.csv", mode='a', newline='') as file:
#                 df.to_csv(file, header=file.tell()==0, index=False)  # Append les données, sans écrire l'en-tête si le fichier existe déjà
# if __name__ == "__main__":
#     main()



 
#                     # Convertir la liste features en un tableau 2D
#                     # HighBP	HighChol	BMI	Smoker	Fruits	GenHlth	MentHlth	PhysHlth	DiffWalk	Sex	Age
#                     # st.write(features)







import numpy as np
import requests
import streamlit as st
import pickle
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
from test import send_prompt_to_mistral
import time
format = """
        Vous avez/ou êtes suceptibles d'être diabétique. Suivez ces conseils et n'oubliez pas de consulter un spécialiste au plus vite:
        1...
        2...
        3...
        etc
    """
format_en = """
You have/or are likely to have diabetes. Follow these tips and don't forget to consult a specialist as soon as possible:
        
        1...
        2...
        3...
        etc
    """
# Traductions en anglais et en français
content = {
    "fr": {
        "title": "Évaluez votre état de santé",
        "section1": "Section 1: Informations générales",
        "age_prompt": "👉Entrez votre âge",
        "bmi_prompt": "👉Entrez votre indice de masse corporelle",
        "chol_prompt": "Avez-vous un taux de cholestérol élevé ?",
        "suivant": "Suivant",
        "section2": "Section 2: Habitudes de vie",
        "sexe_prompt": "👉Quel est votre genre",
        "highbp_prompt": "👉Êtes-vous hypertendu ?",
        "fruit_prompt": "👉Consommez-vous au moins un fruit par jour ?",
        "diffwalk_prompt": "👉Avez-vous des difficultés à marcher ou monter les escaliers ?",
        "retour": "Retour",
        "section3": "Section 3: État de santé",
        "genhlth_prompt": "👉Quelle note sur 5 donneriez-vous à votre état de santé général ?",
        "physhlth_prompt": "👉Combien de jours votre santé physique n'a-t-elle pas été bonne ?",
        "menthlth_prompt": "👉Combien de jours votre santé mentale n'a-t-elle pas été bonne ?",
        "smoke_prompt": "👉Avez-vous fumé au moins 100 cigarettes ?",
        "soumettre": "Soumettre",
        "result_positive":send_prompt_to_mistral(f"Je suis peut-être diabétique ou en proie au diabète. prodigue moi des conseils pour améliorer mon etat de santé. utilise ce format pour répondre: {format} en français"),
        # "result_positive": "Vous êtes susceptible d'être diabétique. Consultez un spécialiste.",
        "result_negative": "Vous ne présentez pas de risque d'être diabétique."
    },
    "en": {
        "title": "Assess your health status",
        "section1": "Section 1: General Information",
        "age_prompt": "👉Enter your age",
        "bmi_prompt": "👉Enter your BMI",
        "chol_prompt": "Do you have high cholesterol?",
        "suivant": "Next",
        "section2": "Section 2: Lifestyle",
        "sexe_prompt": "👉What is your gender?",
        "highbp_prompt": "👉Do you have hypertension?",
        "fruit_prompt": "👉Do you eat at least one fruit per day?",
        "diffwalk_prompt": "👉Do you have difficulty walking or climbing stairs?",
        "retour": "Back",
        "section3": "Section 3: Health Status",
        "genhlth_prompt": "👉How would you rate your overall health on a scale of 1 to 5?",
        "physhlth_prompt": "👉How many days has your physical health been poor?",
        "menthlth_prompt": "👉How many days has your mental health been poor?",
        "smoke_prompt": "👉Have you smoked at least 100 cigarettes?",
        "soumettre": "Submit",
        "result_positive":send_prompt_to_mistral(f"Je suis peut-être diabétique ou en proie au diabète. prodigue moi des conseils pour améliorer mon etat de santé. utilise ce format pour répondre: {format}. fais-le en anglais "),

        "result_negative": "You are not at risk of diabetes."
    }
}





  
# Fonction principale
def main():
    langue = st.selectbox("Choisissez la langue / Choose Language", ("fr", "en"),key="skssjv")
    # Sélection de la langue
    selected_content = content[langue]  # Texte selon la langue sélectionnée
    
    global age, BMI, HighChol, Sexe, Highbp, Fruit, Genhlth, MentHlth, PhysHlth, Smoke, Diff

    st.title(selected_content["title"])
    

    format_en = """
    You have/or are likely to have diabetes. Follow these tips and don't forget to consult a specialist as soon as possible:
        
        1...
        2...
        3...
        etc
    """

    format = """
        Vous avez/ou êtes suceptibles d'être diabétique. Suivez ces conseils et n'oubliez pas de consulter un spécialiste au plus vite:
        1...
        2...
        3...
        etc
    """
    age_mapping = {
        "": "",
        "18-24": 1,
        "25-29": 2,
        "30-34": 3,
        "35-39": 4,
        "40-44": 5,
        "45-49": 6,
        "50-54": 7,
        "55-59": 8,
        "60-64": 9,
        "65-69": 10,
        "70-74": 11,
        "75-80": 12,
        "80-84": 13,
    }
    yes_or_no = {
        "": "",
        "Non" if langue == "fr" else "No": 0,
        "Oui" if langue == "fr" else "Yes": 1
    }
    genre = {
        "": "",
        "Homme" if langue == "fr" else "Male": 1,
        "Femme" if langue == "fr" else "Female": 0
    }

    if "section" not in st.session_state:
        st.session_state.section = 1
    
    # Section 1 : Informations générales
    if st.session_state.section == 1:
        st.subheader(selected_content["section1"])
        with st.form("section1_form"):
            age_ = st.selectbox(selected_content["age_prompt"], list(age_mapping.keys()), index=None)
            age = age_mapping[age_] if age_ else ""
            BMI = st.number_input(selected_content["bmi_prompt"], placeholder=selected_content["bmi_prompt"], key="cgh")
            chol = st.selectbox(selected_content["chol_prompt"], list(yes_or_no.keys()), index=None)
            HighChol = yes_or_no[chol] if chol else ""
            if st.form_submit_button(selected_content["suivant"]):
                st.session_state.section = 2
                st.rerun()
                return

    # Section 2 : Habitudes de vie
    if st.session_state.section == 2:
        st.subheader(selected_content["section2"])
        with st.form("section2_form"):
            sexe_ = st.selectbox(selected_content["sexe_prompt"], list(genre.keys()), index=None)
            Sexe = genre[sexe_] if sexe_ else ""
            highbp_ = st.selectbox(selected_content["highbp_prompt"], list(yes_or_no.keys()), index=None)
            Highbp = yes_or_no[highbp_] if highbp_ else ""
            fruit_ = st.selectbox(selected_content["fruit_prompt"], list(yes_or_no.keys()), index=None)
            Fruit = yes_or_no[fruit_] if fruit_ else ""
            diffwalk = st.selectbox(selected_content["diffwalk_prompt"], list(yes_or_no.keys()), index=None)
            Diff = yes_or_no[diffwalk] if diffwalk else ""
            col1, col2 = st.columns(2)
            with col1:
                if st.form_submit_button(selected_content["retour"]):
                    st.session_state.section = 1
                    st.rerun()
                    return
            with col2:
                if st.form_submit_button(selected_content["suivant"]):
                    st.session_state.section = 3
                    st.rerun()
                    return

    # Section 3 : État de santé
    if st.session_state.section == 3:
        st.subheader(selected_content["section3"])
        with st.form("section3_form"):
            Genhlth = st.selectbox(selected_content["genhlth_prompt"], [""] + list(range(1, 6)), index=None)
            PhysHlth = st.selectbox(selected_content["physhlth_prompt"], [""] + list(range(1, 31)), index=None)
            MentHlth = st.selectbox(selected_content["menthlth_prompt"], [""] + list(range(1, 31)), index=None)
            smoke = st.selectbox(selected_content["smoke_prompt"], list(yes_or_no.keys()), index=None)
            Smoke = yes_or_no[smoke] if smoke else ""
            
            col1, col2 = st.columns(2)
            with col1:
                if st.form_submit_button(selected_content["retour"]):
                    st.session_state.section = 2
                    st.rerun()
                    return
            with col2:
                bt = st.form_submit_button(selected_content["soumettre"])
            if bt:
                # Transformation des données en format numérique et prédiction
                Highbp = int(Highbp)
                HighChol = int(HighChol)
                BMI = int(BMI)
                Smoke = int(Smoke)
                Fruit = int(Fruit)
                Genhlth = int(Genhlth)
                MentHlth = int(MentHlth)
                PhysHlth = int(PhysHlth)
                Diff = int(Diff)
                Sexe = int(Sexe)
                age = int(age)
                features = [Highbp, HighChol, BMI, Smoke, Fruit, Genhlth, MentHlth, PhysHlth, Diff, Sexe, age]
                print(features)
                features = np.array(features).reshape(1, -1)
                prediction = None
                with open('new_GradientBoostingClassifier_boost.pkl', 'rb') as best_gradient_boost:
                    modele_charge = pickle.load(best_gradient_boost)
                    prediction = modele_charge.predict(features)
                    st.session_state
                    if prediction == 1:
                        with st.spinner("Chargement",):
                            time.sleep(5)
                        st.error(selected_content["result_positive"])
                        
                        # prompt = f"Je suis peut-être diabétique ou en proie au diabète. prodigue moi des conseils pour améliorer mon etat de santé. utilise ce format pour répondre: {format} dans cette Langue: {langue}."
                        # with st.spinner('Chargement des conseils...'):
                        #     # advice = send_prompt_to_mistral(prompt)
                        #     print("Advice:", advice)
                        # advice = send_prompt_to_mistral(prompt)
                        # print(send_prompt_to_mistral(prompt))
                        # st.write(advice)
                               
                        
                          
                           
                    else:
                        st.info(selected_content["result_negative"])
                        st.write("Continuez à maintenir un mode de vie sain en faisant de l'exercice régulièrement, en mangeant des fruits et légumes frais, et en consultant votre médecin régulièrement.")
            else:
                prompt = f"Je suis peut-être diabétique ou en proie au diabète. prodigue moi des conseils pour améliorer mon etat de santé. utilise ce format pour répondre: {format} dans cette Langue: {langue}."              
                advice = send_prompt_to_mistral(prompt)
                print(send_prompt_to_mistral(prompt))
                st.write(advice)

if __name__ == "__main__":
    main()
    
    
    
    
    
    

    
    
    
    
    
