# =======================================================================
    # version officielle
# =======================================================================
import numpy as np
import streamlit as st
import pickle
from sklearn.ensemble import GradientBoostingClassifier

age = None
BMI = None
HighChol = None
Sexe = None
Highbp = None
Fruit = None
Genhlth = None
MentHlth = None
PhysHlth = None
Smoke = None
Diff = None

def main():
    global age, BMI, HighChol, Sexe, Highbp, Fruit, Genhlth, MentHlth, PhysHlth, Smoke, Diff

    st.title("Évaluez votre état de santé")
    age_mapping = {
        "":"",
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
    ans = {
        "":"",
        "Non": 0,
        "Oui": 1
    }
    genre = {
        "":"",
        "Homme": 1,
        "Femme": 0
    }
    yes_or_no = {
        "":"",
        "Oui": 1,
        "Non": 0
    }
    features = []

    if "section" not in st.session_state:
        st.session_state.section = 1

    if st.session_state.section == 1:
        st.subheader("Section 1: Informations générales")
        with st.form("section1_form"):
            age_ = st.selectbox("👉Entrez votre âge", list(age_mapping.keys()), index=None, placeholder="Selectionnez votre tranche d'âge",)
            print(age_)
            age = age_mapping[age_] if age_ else ""
            BMI = st.number_input("👉Entrez votre indice de masse corporelle", placeholder="Entrez votre IMC", key="cgh")
            chol = st.selectbox("Avez-vous un taux de cholestérol élevé ?", list(yes_or_no.keys()), index=None, placeholder="Sélectionnez une option")
            HighChol = yes_or_no[chol] if chol else ""
            if st.form_submit_button("Suivant", args="section1_next"):
               
               
                features.append(age)
                features.append(BMI)
                features.append(HighChol)
                st.session_state.section = 2
            print(f"***************age: {age} ")
            print(age_mapping["70-74"])

    elif st.session_state.section == 2:
        st.subheader("Section 2: Habitudes de vie")
        with st.form("section2_form"):
            # veggie = st.selectbox("👉Consommez-vous des légumes quotidiennement ?", list(yes_or_no.keys()), index=None ,placeholder="Sélectionnez une option",)
            # Veggie = yes_or_no[veggie] if veggie else ""
            sexe_ = st.selectbox("👉Quel est votre genre", list(genre.keys()), index=None, key="b",placeholder="Sélectionnez une option")
            Sexe = genre[sexe_] if sexe_ else ""
            highbp_ = st.selectbox("👉Êtes-vous hypertendus ?", list(ans.keys()), index=None, key="skjdn",placeholder="Sélectionnez une option")
            Highbp = ans[highbp_] if highbp_ else ""
            fruit_ = st.selectbox("👉Consommez-vous au moins un fruit par jour ?", list(yes_or_no.keys()), index=None, key="skjv",placeholder="Sélectionnez une option")
            Fruit = yes_or_no[fruit_] if fruit_ else ""
            diffwalk = st.selectbox("👉Avez-vous des difficultés à marcher ou monter les escaliers ?", list(yes_or_no.keys()), index=None, key="sfkjv",placeholder="Sélectionnez une option")
            Diff = yes_or_no[diffwalk] if diffwalk else ""
            col1, col2 = st.columns(2)
            print(f"2***************BMI: {BMI} ")
            print(age_mapping["70-74"])
            with col1:
                if st.form_submit_button("Retour", args="section2_back"):
                
                    st.session_state.section = 1
                    
            with col2:
                if st.form_submit_button("Suivant", args="section2_next"):
                    # features.append(Veggie)
                    features.append(Sexe)
                    features.append(Highbp)
                    features.append(Fruit)
                    features.append(Diff)
                    st.session_state.section = 3
                

    elif st.session_state.section == 3:
        st.subheader("Section 3: État de santé")
        with st.form("section3_form"):
            Genhlth = st.selectbox("👉Quelle note sur 5 donneriez-vous à votre état de santé général ?", [""] + list(range(1, 6)),index=None, key="skssjv",placeholder="Sélectionnez une option")
            PhysHlth = st.selectbox("👉Pendant combien de jours au cours des 30 derniers jours votre santé physique n'a-t-elle pas été bonne ?", [""] + list(range(1, 31)),index=None,placeholder="Sélectionnez une option", key="dddddg")
            MentHlth = st.selectbox("👉Pensez maintenant à votre santé mentale, qui comprend le stress, la dépression et les problèmes émotionnels, pendant combien de jours au cours des 30 derniers jours votre santé mentale n'a-t-elle pas été bonne. ?", [""] + list(range(1, 31)),index=None, placeholder="Sélectionnez une option", key="eeeeeg")
            smoke = st.selectbox("👉Avez-vous fumé au moins 100 cigarettes (05 paquets) au cours de votre vie ?", list(yes_or_no.keys()), index=None, key="h",)
            Smoke = yes_or_no[smoke] if smoke else ""
            
            col1, col2 = st.columns(2)
            with col1:
                back =st.form_submit_button("Retour", args="section3_back")
                if back:
                    st.session_state.section = 2
                    
            with col2:
                if st.form_submit_button("Soumettre", args="section3_submit"):
                    features.append(Highbp)
                    features.append(HighChol)
                    features.append(BMI)
                    features.append(Smoke)
                    features.append(Fruit)
                    features.append(Genhlth)
                    features.append(MentHlth)
                    features.append(PhysHlth)
                    features.append(Diff)
                    features.append(Sexe)
                    features.append(age)
                    # Convertir la liste features en un tableau 2D
                    # HighBP	HighChol	BMI	Smoker	Fruits	GenHlth	MentHlth	PhysHlth	DiffWalk	Sex	Age
                    st.write(features)

                    features = np.array(features).reshape(1, -1)
                    with open('new_GradientBoostingClassifier_boost.pkl', 'rb') as best_gradient_boost:
                        modele_charge = pickle.load(best_gradient_boost)
                        prediction = modele_charge.predict(features)
                        if prediction ==1:
                            st.write("Vous êtes diabétique")
                        else:
                            st.write("Vous ne présentez pas de risque")
                        print(features)
                    st.success("Vos données ont été enregistrées avec succès.")

if __name__ == "__main__":
    main()





# ==================================
    # autre chat gpt optimisé
# ==================================
# import numpy as np
# import streamlit as st
# import pickle

# def main():
#     st.title("Évaluez votre état de santé")
#     features = []
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

#     section = st.session_state.get("section", 1)

#     if section == 1:
#         st.subheader("Section 1: Informations générales")
#         with st.form("section1_form"):
#             age = st.selectbox("👉Entrez votre âge", list(age_mapping.keys()), index=None, placeholder="Selectionnez votre tranche d'âge",)
#             age = age_mapping[age] if age else ""
#             BMI = int(st.number_input("👉Entrez votre indice de masse corporelle", placeholder="Entrez votre IMC", key="c"))
#             chol = st.selectbox("Avez-vous un taux de cholestérol élevé ?", list(yes_or_no.keys()), index=None, placeholder="Sélectionnez une option")
#             HighChol = yes_or_no[chol] if chol else ""
#             if st.form_submit_button("Suivant"):
#                 features.extend([age, BMI, HighChol])
#                 st.session_state.section = 2

#     elif section == 2:
#         st.subheader("Section 2: Habitudes de vie")
#         with st.form("section2_form"):
#             sexe = st.selectbox("👉Quel est votre genre", list(genre.keys()), index=None, key="b",placeholder="Sélectionnez une option")
#             Sexe = genre[sexe] if sexe else ""
#             highbp = st.selectbox("👉Êtes-vous hypertendus ?", list(ans.keys()), index=None, key="skjdn",placeholder="Sélectionnez une option")
#             Highbp = ans[highbp] if highbp else ""
#             fruit = st.selectbox("👉Consommez-vous au moins un fruit par jour ?", list(yes_or_no.keys()), index=None, key="skjv",placeholder="Sélectionnez une option")
#             Fruit = yes_or_no[fruit] if fruit else ""
#             diffwalk = st.selectbox("👉Avez-vous des difficultés à marcher ou monter les escaliers ?", list(yes_or_no.keys()), index=None, key="sfkjv",placeholder="Sélectionnez une option")
#             Diff = yes_or_no[diffwalk] if fruit else ""
#             if st.form_submit_button("Retour"):
#                 st.session_state.section = 1
#             if st.form_submit_button("Suivant"):
#                 features.extend([Sexe, Highbp, Fruit, Diff])
#                 st.session_state.section = 3

#     elif section == 3:
#         st.subheader("Section 3: État de santé")
#         with st.form("section3_form"):
#             Genhlth = st.selectbox("👉Quelle note sur 5 donneriez-vous à votre état de santé général ?", [""] + list(range(1, 6)),index=None, key="skssjv",placeholder="Sélectionnez une option")
#             PhysHlth = st.selectbox("👉Pendant combien de jours au cours des 30 derniers jours votre santé physique n'a-t-elle pas été bonne ?", [""] + list(range(1, 31)),index=None,placeholder="Sélectionnez une option", key="dddddg")
#             MentHlth = st.selectbox("👉Pensez maintenant à votre santé mentale, qui comprend le stress, la dépression et les problèmes émotionnels, pendant combien de jours au cours des 30 derniers jours votre santé mentale n'a-t-elle pas été bonne. ?", [""] + list(range(1, 31)),index=None, placeholder="Sélectionnez une option", key="eeeeeg")
#             smoke = st.selectbox("👉Avez-vous fumé au moins 100 cigarettes (05 paquets) au cours de votre vie ?", list(yes_or_no.keys()), index=None, key="h",)
#             Smoke = yes_or_no[smoke] if smoke else ""
            
#             if st.form_submit_button("Retour"):
#                 st.session_state.section = 2
#             if st.form_submit_button("Soumettre"):
#                 features.extend([Genhlth, MentHlth, PhysHlth, Smoke])
#                 features = np.array(features).reshape(1, -1)
#                 with open('best_gradient_boost.pkl', 'rb') as best_gradient_boost:
#                     modele_charge = pickle.load(best_gradient_boost)
#                     prediction = modele_charge.predict(features)
#                     if prediction ==1:
#                         st.write("Vous êtes diabétique")
#                     else:
#                         st.write("Vous ne présentez pas de risque")
#                     print(features)
#                 st.success("Vos données ont été enregistrées avec succès.")

# if __name__ == "__main__":
#     main()



# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************
# ********************************************************************************************************************************














# ==========================================================================================================
        # debut Fonctionne
# ==========================================================================================================

# import numpy as np
# import streamlit as st
# import pickle

# def main():
#     st.title("Évaluez votre état de santé")
#     features = []
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

#     col1, col2 = st.columns(2)
#     with col1:
# #         option = st.selectbox(
# #    "How would you like to be contacted?",
# #    list(age_mapping.keys()), index=0,
# #    placeholder="Select contact method...",
# # )
#         age = st.selectbox("👉Entrez votre âge", list(age_mapping.keys()), index=None,placeholder="Selectionnez votre tranche d'âge",)
#         age = age_mapping[age] if age else ""
#         BMI = int(st.number_input("👉Entrez votre indice de masse corporelle", placeholder="Entrez votre IMC", key="c"))
#         chol = st.selectbox("Avez-vous un taux de cholestérol élevé ?", list(yes_or_no.keys()), index=None,placeholder="Sélectionnez une option")
#         HighChol = yes_or_no[chol] if chol else ""

#     veggie = st.selectbox("👉Consommez-vous des légumes quotidiennement ?", list(yes_or_no.keys()), index=None ,placeholder="Sélectionnez une option",)
#     Veggie = yes_or_no[veggie] if veggie else ""

#     with col2:
#         sexe = st.selectbox("👉Quel est votre genre", list(genre.keys()), index=None, key="b",placeholder="Sélectionnez une option")
#         Sexe = genre[sexe] if sexe else ""

#         highbp = st.selectbox("👉Ëtes-vous hypertendus ?", list(ans.keys()), index=None, key="skjdn",placeholder="Sélectionnez une option")
#         Highbp = ans[highbp] if highbp else ""

#         fruit = st.selectbox("👉Consommez-vous au moins un fruit par jour ?", list(yes_or_no.keys()), index=None, key="skjv",placeholder="Sélectionnez une option")
#         Fruit = yes_or_no[fruit] if fruit else ""

#     Genhlth = st.selectbox("👉Quelle note sur 5 donneriez-vous à votre état de santé général ?", [""] + list(range(1, 6)),index=None, key="skssjv",placeholder="Sélectionnez une option")
#     PhysHlth = st.selectbox("👉Pendant combien de jours au cours des 30 derniers jours votre santé physique n'a-t-elle pas été bonne ?", [""] + list(range(1, 31)),index=None,placeholder="Sélectionnez une option", key="dddddg")
#     MentHlth = st.selectbox("👉Pensez maintenant à votre santé mentale, qui comprend le stress, la dépression et les problèmes émotionnels, pendant combien de jours au cours des 30 derniers jours votre santé mentale n'a-t-elle pas été bonne. ?", [""] + list(range(1, 31)),index=None, placeholder="Sélectionnez une option", key="eeeeeg")

#     smoke = st.selectbox("👉Avez-vous fumé au moins 100 cigarettes (05 paquets) au cours de votre vie ?", list(yes_or_no.keys()), index=None, key="h",)
#     Smoke = yes_or_no[smoke] if smoke else ""

#     if st.button("Soumettre"):
#         if "" not in [age, BMI, HighChol, Veggie, Sexe, Highbp, Fruit, Genhlth, MentHlth, PhysHlth, Smoke]:
#             features.append(Highbp)
#             features.append(HighChol)
#             features.append(BMI)
#             features.append(Smoke)
#             features.append(Fruit)
#             features.append(Veggie)
#             features.append(Genhlth)
#             features.append(MentHlth)
#             features.append(PhysHlth)
#             features.append(Sexe)
#             features.append(age)
#             st.write(features)
#             # Convertir la liste features en un tableau 2D
#             features = np.array(features).reshape(1, -1)
#             with open('modele_regression_logistique.pkl', 'rb') as modele_regression_logistique:
#                 modele_charge = pickle.load(modele_regression_logistique)
#                 prediction = modele_charge.predict(features)
#             if prediction ==1:
#                 st.write("Vous êtes diabétique")
#             else:
#                 st.write("Vous ne présentez pas de risque")
                
#         else:
#             st.error("Veuillez remplir tous les champs obligatoires.")


# HighBP	HighChol	BMI	Smoker	Fruits	GenHlth	MentHlth	PhysHlth	DiffWalk	Sex	Age


# ==========================================================================================================
        # Fin Fonctionne
# ==========================================================================================================





































# import numpy as np
# import pickle
# import streamlit as st
# from streamlit import session_state
# import extra_streamlit_components as stx

# ans = {
#     "": "",
#     "Non": 0,
#     "Oui": 1
# }
# yes_or_no = {
#     "": "",
#     "Oui": 1,
#     "Non": 0
# }
# genre = {
#     "": "",
#     "Homme": 1,
#     "Femme": 0
# }

# def section_1():
#     st.title("Évaluation de l'état de santé - Section 1")
#     features = []
#     age_mapping = {
#         "": "",
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

#     col1, col2 = st.columns(2)
#     with col1:
#         age = st.selectbox("👉Entrez votre âge", list(age_mapping.keys()), index=None, placeholder="Selectionnez votre tranche d'âge")
#         age = age_mapping[age] if age else ""
#         BMI = int(st.number_input("👉Entrez votre indice de masse corporelle", placeholder="Entrez votre IMC", key="c"))
#         chol = st.selectbox("Avez-vous un taux de cholestérol élevé ?", list(yes_or_no.keys()), index=None, placeholder="Sélectionnez une option")
#         HighChol = yes_or_no[chol] if chol else ""

#     veggie = st.selectbox("👉Consommez-vous des légumes quotidiennement ?", list(yes_or_no.keys()), index=None , placeholder="Sélectionnez une option")
#     Veggie = yes_or_no[veggie] if veggie else ""
    
#     if st.button("Suivant"):
#         if "" not in [age, BMI, HighChol, Veggie]:
#             st.session_state.current_page = "2"
#         else:
#             st.error("Veuillez remplir tous les champs obligatoires.")
#         return


# def section_2():
#     st.title("Évaluation de l'état de santé - Section 2")
#     features = []
    
#     with st.form("my_form"):
#         col1, col2 = st.columns(2)
#         with col1:
#             sexe = st.selectbox("👉Quel est votre genre", list(genre.keys()), index=None, key="b", placeholder="Sélectionnez une option")
#             Sexe = genre[sexe] if sexe else ""

#             highbp = st.selectbox("👉Êtes-vous hypertendus ?", list(ans.keys()), index=None, key="skjdn", placeholder="Sélectionnez une option")
#             Highbp = ans[highbp] if highbp else ""

#         with col2:
#             fruit = st.selectbox("👉Consommez-vous au moins un fruit par jour ?", list(yes_or_no.keys()), index=None, key="skjv", placeholder="Sélectionnez une option")
#             Fruit = yes_or_no[fruit] if fruit else ""
            
#     if st.form_submit_button("Suivant"):
#         st.session_state.current_page = "3"

# def section_3():
#     st.title("Évaluation de l'état de santé - Section 3")
#     features = []
    
#     Genhlth = st.selectbox("👉Quelle note sur 5 donneriez-vous à votre état de santé général ?", [""] + list(range(1, 6)), index=None, key="skssjv", placeholder="Sélectionnez une option")
#     PhysHlth = st.selectbox("👉Pendant combien de jours au cours des 30 derniers jours votre santé physique n'a-t-elle pas été bonne ?", [""] + list(range(1, 31)), index=None, placeholder="Sélectionnez une option", key="dddddg")
#     MentHlth = st.selectbox("👉Pensez maintenant à votre santé mentale, qui comprend le stress, la dépression et les problèmes émotionnels, pendant combien de jours au cours des 30 derniers jours votre santé mentale n'a-t-elle pas été bonne. ?", [""] + list(range(1, 31)), index=None, placeholder="Sélectionnez une option", key="eeeeeg")

#     smoke = st.selectbox("👉Avez-vous fumé au moins 100 cigarettes (05 paquets) au cours de votre vie ?", list(yes_or_no.keys()), index=None, key="h")
#     Smoke = yes_or_no[smoke] if smoke else ""

#     if st.button("Soumettre"):
#         if "" not in [Genhlth, MentHlth, PhysHlth, Smoke]:
#             features.append("Highbp")
#             features.append("HighChol")
#             features.append("BMI")
#             features.append("Smoke")
#             features.append("Fruit")
#             features.append("Veggie")
#             features.append(Genhlth)
#             features.append(MentHlth)
#             features.append(PhysHlth)
#             features.append("Sexe")
#             features.append("age")
#             # Convertir la liste features en un tableau 2D
#             features = np.array(features).reshape(1, -1)
#             with open('modele_regression_logistique.pkl', 'rb') as modele_regression_logistique:
#                 modele_charge = pickle.load(modele_regression_logistique)
#                 prediction = modele_charge.predict(features)
#             if prediction == 1:
#                 st.write("Vous êtes diabétique")
#             else:
#                 st.write("Vous ne présentez pas de risque")
                
#         else:
#             st.error("Veuillez remplir tous les champs obligatoires.")

# def main():
#     if "current_page" not in st.session_state:
#         st.session_state.current_page = "1"

#     chosen_id = stx.tab_bar(data=[
#         stx.TabBarItemData(id="1", title="Section 1", description="First section of the form"),
#         stx.TabBarItemData(id="2", title="Section 2", description="Second section of the form"),
#         stx.TabBarItemData(id="3", title="Section 3", description="Third section of the form"),
#     ], default="1")

#     if chosen_id == "1" and st.session_state.current_page == "1":      
#         section_1()
        
#     elif chosen_id == "2" and st.session_state.current_page == "2":
#         section_2()
        
#     elif chosen_id == "3" and st.session_state.current_page == "3":
#         section_3()



















# Marche
# import numpy as np
# import streamlit as st
# import pickle





# age = None
# BMI = None
# HighChol = None
# Veggie = None
# Sexe = None
# Highbp = None
# Fruit = None
# Genhlth = None
# MentHlth = None
# PhysHlth = None
# Smoke = None

# def main():
#     global age, BMI, HighChol, Veggie, Sexe, Highbp, Fruit, Genhlth, MentHlth, PhysHlth, Smoke

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
#         st.session_state["section"] = 1

#     if st.session_state["section"] == 1:
#         st.subheader("Section 1: Informations générales")
#         with st.form("section1_form"):
#             age = st.selectbox("👉Entrez votre âge", list(age_mapping.keys()), index=None,placeholder="Selectionnez votre tranche d'âge",)
#             age = age_mapping[age] if age else ""
#             BMI = int(st.number_input("👉Entrez votre indice de masse corporelle", placeholder="Entrez votre IMC", key="c"))
#             chol = st.selectbox("Avez-vous un taux de cholestérol élevé ?", list(yes_or_no.keys()), index=None,placeholder="Sélectionnez une option")
#             HighChol = yes_or_no[chol] if chol else ""
#             if st.form_submit_button("Suivant"):
#                 features.append(age)
#                 features.append(BMI)
#                 features.append(HighChol)
#                 print(features,"*****")                
#                 st.session_state["section"] = 2

#     elif st.session_state["section"] == 2:
#         st.subheader("Section 2: Habitudes de vie")
#         with st.form("section2_form"):
#             veggie = st.selectbox("👉Consommez-vous des légumes quotidiennement ?", list(yes_or_no.keys()), index=None ,placeholder="Sélectionnez une option",)
#             Veggie = yes_or_no[veggie] if veggie else ""
#             sexe = st.selectbox("👉Quel est votre genre", list(genre.keys()), index=None, key="b",placeholder="Sélectionnez une option")
#             Sexe = genre[sexe] if sexe else ""
#             highbp = st.selectbox("👉Ëtes-vous hypertendus ?", list(ans.keys()), index=None, key="skjdn",placeholder="Sélectionnez une option")
#             Highbp = ans[highbp] if highbp else ""
#             fruit = st.selectbox("👉Consommez-vous au moins un fruit par jour ?", list(yes_or_no.keys()), index=None, key="skjv",placeholder="Sélectionnez une option")
#             Fruit = yes_or_no[fruit] if fruit else ""
#             if st.form_submit_button("Suivant"):
#                 features.append(Veggie)
#                 features.append(Sexe)
#                 features.append(Highbp)
#                 features.append(Fruit)
#                 print(features,"*****")
#                 st.session_state["section"] = 3
#             if st.form_submit_button("cancel"):
#                 st.session_state["section"] = 1

#     elif st.session_state["section"] == 3:
#         st.subheader("Section 3: État de santé")
#         with st.form("section3_form"):
#             Genhlth = st.selectbox("👉Quelle note sur 5 donneriez-vous à votre état de santé général ?", [""] + list(range(1, 6)),index=None, key="skssjv",placeholder="Sélectionnez une option")
#             PhysHlth = st.selectbox("👉Pendant combien de jours au cours des 30 derniers jours votre santé physique n'a-t-elle pas été bonne ?", [""] + list(range(1, 31)),index=None,placeholder="Sélectionnez une option", key="dddddg")
#             MentHlth = st.selectbox("👉Pensez maintenant à votre santé mentale, qui comprend le stress, la dépression et les problèmes émotionnels, pendant combien de jours au cours des 30 derniers jours votre santé mentale n'a-t-elle pas été bonne. ?", [""] + list(range(1, 31)),index=None, placeholder="Sélectionnez une option", key="eeeeeg")
#             smoke = st.selectbox("👉Avez-vous fumé au moins 100 cigarettes (05 paquets) au cours de votre vie ?", list(yes_or_no.keys()), index=None, key="h",)
#             Smoke = yes_or_no[smoke] if smoke else ""
#             if st.form_submit_button("Soumettre"):
#                 features.append(Highbp)
#                 features.append(HighChol)
#                 features.append(BMI)
#                 features.append(Smoke)
#                 features.append(Fruit)
#                 features.append(Veggie)
#                 features.append(Genhlth)
#                 features.append(MentHlth)
#                 features.append(PhysHlth)
#                 features.append(Sexe)
#                 features.append(age)
                
                
#                 st.write(features)
#                 st.success("Vos données ont été enregistrées avec succès.")
#         if st.button("Retour"):
#             st.session_state["section"] = 2




































# import numpy as np
# import streamlit as st
# import pickle

# age = None
# BMI = None
# HighChol = None
# Veggie = None
# Sexe = None
# Highbp = None
# Fruit = None
# Genhlth = None
# MentHlth = None
# PhysHlth = None
# Smoke = None

# def main():
#     global age, BMI, HighChol, Veggie, Sexe, Highbp, Fruit, Genhlth, MentHlth, PhysHlth, Smoke

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
#         st.session_state["section"] = 1

#     if st.session_state["section"] == 1:
#         st.subheader("Section 1: Informations générales")
#         with st.form("section1_form"):
#             age = st.selectbox("👉Entrez votre âge", list(age_mapping.keys()), index=None,placeholder="Selectionnez votre tranche d'âge",)
#             age = age_mapping[age] if age else ""
#             BMI = int(st.number_input("👉Entrez votre indice de masse corporelle", placeholder="Entrez votre IMC", key="c"))
#             chol = st.selectbox("Avez-vous un taux de cholestérol élevé ?", list(yes_or_no.keys()), index=None,placeholder="Sélectionnez une option")
#             HighChol = yes_or_no[chol] if chol else ""
#             if st.form_submit_button("Suivant"):
#                 features.append(age)
#                 features.append(BMI)
#                 features.append(HighChol)
#                 st.session_state["section"] = 2

#     elif st.session_state["section"] == 2:
#         st.subheader("Section 2: Habitudes de vie")
#         with st.form("section2_form"):
#             veggie = st.selectbox("👉Consommez-vous des légumes quotidiennement ?", list(yes_or_no.keys()), index=None ,placeholder="Sélectionnez une option",)
#             Veggie = yes_or_no[veggie] if veggie else ""
#             sexe = st.selectbox("👉Quel est votre genre", list(genre.keys()), index=None, key="b",placeholder="Sélectionnez une option")
#             Sexe = genre[sexe] if sexe else ""
#             highbp = st.selectbox("👉Ëtes-vous hypertendus ?", list(ans.keys()), index=None, key="skjdn",placeholder="Sélectionnez une option")
#             Highbp = ans[highbp] if highbp else ""
#             fruit = st.selectbox("👉Consommez-vous au moins un fruit par jour ?", list(yes_or_no.keys()), index=None, key="skjv",placeholder="Sélectionnez une option")
#             Fruit = yes_or_no[fruit] if fruit else ""
#             if st.form_submit_button("Suivant"):
#                 features.append(Veggie)
#                 features.append(Sexe)
#                 features.append(Highbp)
#                 features.append(Fruit)
#                 st.session_state["section"] = 3
#             if st.form_submit_button("Cancel"):
#                 st.session_state["section"] = 1

#     elif st.session_state["section"] == 3:
#         st.subheader("Section 3: État de santé")
#         with st.form("section3_form"):
#             Genhlth = st.selectbox("👉Quelle note sur 5 donneriez-vous à votre état de santé général ?", [""] + list(range(1, 6)),index=None, key="skssjv",placeholder="Sélectionnez une option")
#             PhysHlth = st.selectbox("👉Pendant combien de jours au cours des 30 derniers jours votre santé physique n'a-t-elle pas été bonne ?", [""] + list(range(1, 31)),index=None,placeholder="Sélectionnez une option", key="dddddg")
#             MentHlth = st.selectbox("👉Pensez maintenant à votre santé mentale, qui comprend le stress, la dépression et les problèmes émotionnels, pendant combien de jours au cours des 30 derniers jours votre santé mentale n'a-t-elle pas été bonne. ?", [""] + list(range(1, 31)),index=None, placeholder="Sélectionnez une option", key="eeeeeg")
#             smoke = st.selectbox("👉Avez-vous fumé au moins 100 cigarettes (05 paquets) au cours de votre vie ?", list(yes_or_no.keys()), index=None, key="h",)
#             Smoke = yes_or_no[smoke] if smoke else ""
#             if st.form_submit_button("Soumettre"):
#                 features.append(Highbp)
#                 features.append(HighChol)
#                 features.append(BMI)
#                 features.append(Smoke)
#                 features.append(Fruit)
#                 features.append(Veggie)
#                 features.append(Genhlth)
#                 features.append(MentHlth)
#                 features.append(PhysHlth)
#                 features.append(Sexe)
#                 features.append(age)
#                 print(features)
#                 st.success("Vos données ont été enregistrées avec succès.")
#             if st.form_submit_button("Cancel"):
#                 st.session_state["section"] = 2

# if __name__ == "__main__":
#     main()





































# import numpy as np
# import streamlit as st
# import pickle

# age = None
# BMI = None
# HighChol = None
# Veggie = None
# Sexe = None
# Highbp = None
# Fruit = None
# Genhlth = None
# MentHlth = None
# PhysHlth = None
# Smoke = None

# def main():
#     global age, BMI, HighChol, Veggie, Sexe, Highbp, Fruit, Genhlth, MentHlth, PhysHlth, Smoke

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
#             age = st.selectbox("👉Entrez votre âge", list(age_mapping.keys()), index=None,placeholder="Selectionnez votre tranche d'âge",)
#             age = age_mapping[age] if age else ""
#             BMI = int(st.number_input("👉Entrez votre indice de masse corporelle", placeholder="Entrez votre IMC", key="c"))
#             chol = st.selectbox("Avez-vous un taux de cholestérol élevé ?", list(yes_or_no.keys()), index=None,placeholder="Sélectionnez une option")
#             HighChol = yes_or_no[chol] if chol else ""
#             if st.form_submit_button("Suivant",args="section1_next"):
#                 features.append(age)
#                 features.append(BMI)
#                 features.append(HighChol)
#             st.session_state.section = 2

#     elif st.session_state.section == 2:
#         st.subheader("Section 2: Habitudes de vie")
#         with st.form("section2_form"):
#             veggie = st.selectbox("👉Consommez-vous des légumes quotidiennement ?", list(yes_or_no.keys()), index=None ,placeholder="Sélectionnez une option",)
#             Veggie = yes_or_no[veggie] if veggie else ""
#             sexe = st.selectbox("👉Quel est votre genre", list(genre.keys()), index=None, key="b",placeholder="Sélectionnez une option")
#             Sexe = genre[sexe] if sexe else ""
#             highbp = st.selectbox("👉Ëtes-vous hypertendus ?", list(ans.keys()), index=None, key="skjdn",placeholder="Sélectionnez une option")
#             Highbp = ans[highbp] if highbp else ""
#             fruit = st.selectbox("👉Consommez-vous au moins un fruit par jour ?", list(yes_or_no.keys()), index=None, key="skjv",placeholder="Sélectionnez une option")
#             Fruit = yes_or_no[fruit] if fruit else ""
#             if st.form_submit_button("Suivant", args="section2_next"):
#                 features.append(Veggie)
#                 features.append(Sexe)
#                 features.append(Highbp)
#                 features.append(Fruit)
#             st.session_state.section = 3
#             if st.form_submit_button("Retour", args="section2_back"):
#                 st.session_state.section -=1
#                 # Réinitialiser les variables globales
#                 age = BMI = HighChol = Veggie = Sexe = Highbp = Fruit = None

#     elif st.session_state.section == 3:
#         st.subheader("Section 3: État de santé")
#         with st.form("section3_form"):
#             Genhlth = st.selectbox("👉Quelle note sur 5 donneriez-vous à votre état de santé général ?", [""] + list(range(1, 6)),index=None, key="skssjv",placeholder="Sélectionnez une option")
#             PhysHlth = st.selectbox("👉Pendant combien de jours au cours des 30 derniers jours votre santé physique n'a-t-elle pas été bonne ?", [""] + list(range(1, 31)),index=None,placeholder="Sélectionnez une option", key="dddddg")
#             MentHlth = st.selectbox("👉Pensez maintenant à votre santé mentale, qui comprend le stress, la dépression et les problèmes émotionnels, pendant combien de jours au cours des 30 derniers jours votre santé mentale n'a-t-elle pas été bonne. ?", [""] + list(range(1, 31)),index=None, placeholder="Sélectionnez une option", key="eeeeeg")
#             smoke = st.selectbox("👉Avez-vous fumé au moins 100 cigarettes (05 paquets) au cours de votre vie ?", list(yes_or_no.keys()), index=None, key="h",)
#             Smoke = yes_or_no[smoke] if smoke else ""
#             if st.form_submit_button("Soumettre", args="section3_submit"):
#                 features.append(Highbp)
#                 features.append(HighChol)
#                 features.append(BMI)
#                 features.append(Smoke)
#                 features.append(Fruit)
#                 features.append(Veggie)
#                 features.append(Genhlth)
#                 features.append(MentHlth)
#                 features.append(PhysHlth)
#                 features.append(Sexe)
#                 features.append(age)
#                 print(features)
#                 st.success("Vos données ont été enregistrées avec succès.")
#             elif st.form_submit_button("Retour", args="section3_back"):
#                 st.session_state.section -= 1
#                 # Réinitialiser les variables globales
#                 Genhlth = MentHlth = PhysHlth = Smoke = None

# if __name__ == "__main__":
#     main()