# import streamlit as st 
# from streamlit_option_menu import option_menu
# # from streamlit import option_menu
# from src import analysis , forecast
# import random



# style = """
#     <style>
#         .image-container {
#             display: flex;
#             justify-content: center;
#             align-items: center;
#         }
        
#         .image-container img {
#             max-width: 60%;
#             max-height: 50%;
#             border-radius: 10px;
#             /box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);/
#             position: relative;
#             bottom: 5em;
#         }
#     </style>
# """


# text = """
# DiabetForecast est une solution innovante conçue pour évaluer le risque de diabète de type 2 (DT2) en utilisant des techniques avancées d'intelligence artificielle (IA) et d'apprentissage automatique. Cet outil vise à surmonter les limites des méthodes traditionnelles d'évaluation des risques, telles que le Finnish Diabetes Risk Score (FINDRISC), en offrant une approche plus complète, personnalisée et adaptable.

# DiabetForecast intègre une large gamme de données, incluant des facteurs démographiques, médicaux et de mode de vie, pour développer des modèles prédictifs précis. Contrairement au FINDRISC, qui repose sur huit paramètres standard, DiabetForecast considère les interactions complexes entre divers facteurs de risque, fournissant une analyse nuancée de l'état de santé d'un individu. Ce système évalue également les appréciations subjectives de la santé et adapte ses prédictions aux caractéristiques uniques de chaque utilisateur, améliorant ainsi la précision et la pertinence de ses évaluations de risque.

# DiabetForecast comporte deux principaux composants :

# Tableau de bord d'analyse de la santé : Ce composant visualise les tendances de la santé de la population, affichant des graphiques et des métriques reflétant l'état de santé global d'une communauté. Il aide les responsables de la santé publique et les décideurs politiques à surveiller et à traiter proactivement les problèmes de santé.

# Module d'évaluation des risques : Ce module réalise une évaluation détaillée des risques pour les individus, offrant des évaluations objectives de leur état de santé général. En identifiant les personnes à haut risque, DiabetForecast permet des interventions précoces et des stratégies de prévention ciblées, visant ultimement à réduire l'incidence du DT2.

# En fournissant une interface détaillée et conviviale, DiabetForecast facilite non seulement une meilleure gestion de la santé pour les individus, mais soutient également les professionnels de la santé dans la prise de décisions éclairées. La mise en œuvre de DiabetForecast pourrait améliorer significativement la détection et la prévention du DT2, particulièrement dans des contextes divers et à faibles ressources, en faisant un outil essentiel dans la lutte mondiale contre le diabète.


# """


# st.markdown(style, unsafe_allow_html=True)

# chemin_image = "https://github.com/Moubarak321/DiabetForecast/blob/main/images/dia1.png?raw=true"
# # def get_random_img(img_names: list[str]) -> str:
# #     return random.choice(img_names)

# def accueil():
#     # st.divider()
#     # st.write(f"<div style='text-align: justify;'>{text}</div>", unsafe_allow_html=True)
#     # st.divider()
#     with st.expander("**Description du Projet DiabetForecast**"):
#         st.info(text)
#     # with st.expander("**Guide d'utilisation**"):
#     #     st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum")
#     with st.expander("**Auteurs**"):
#         st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum")
#     # with st.expander("Description du Projet DiabetForecast"):
#     #     st.write()
#     # st.image("https://static.streamlit.io/examples/dice.jpg")

# st.markdown(f'<div class="image-container"><img src="{chemin_image}" alt="Ma superbe image"></div>', unsafe_allow_html=True)


# menu = option_menu(None, ["Abstract", "Prévisions", "Analyses" ] ,
#                 icons=['house', 'lightbulb',  'bar-chart-fill'], 
#                 menu_icon="cast", default_index=0, orientation="horizontal")

# if menu == "Abstract":
#     # st.image(f"images/{get_random_img(['diabetes1', 'diabetes2', 'diabetes3', 'diabetes4'])}.jpg")
#     accueil()

# elif menu == "Prévisions":
#     forecast.main()


# elif menu == "Analyses":
#     analysis.main()







import streamlit as st 
from streamlit_option_menu import option_menu
# from streamlit import option_menu
from src import analysis , forecast
import random



style = """
    <style>
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .image-container img {
            max-width: 60%;
            max-height: 50%;
            border-radius: 10px;
            /box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);/
            position: relative;
            bottom: 5em;
        }
    </style>
"""


text = """
DiabetForecast est une solution innovante conçue pour évaluer le risque de diabète de type 2 (DT2) en utilisant des techniques avancées d'intelligence artificielle (IA) et d'apprentissage automatique. Cet outil vise à surmonter les limites des méthodes traditionnelles d'évaluation des risques, telles que le Finnish Diabetes Risk Score (FINDRISC), en offrant une approche plus complète, personnalisée et adaptable.

DiabetForecast intègre une large gamme de données, incluant des facteurs démographiques, médicaux et de mode de vie, pour développer des modèles prédictifs précis. Contrairement au FINDRISC, qui repose sur huit paramètres standard, DiabetForecast considère les interactions complexes entre divers facteurs de risque, fournissant une analyse nuancée de l'état de santé d'un individu. Ce système évalue également les appréciations subjectives de la santé et adapte ses prédictions aux caractéristiques uniques de chaque utilisateur, améliorant ainsi la précision et la pertinence de ses évaluations de risque.

DiabetForecast comporte deux principaux composants :

Tableau de bord d'analyse de la santé : Ce composant visualise les tendances de la santé de la population, affichant des graphiques et des métriques reflétant l'état de santé global d'une communauté. Il aide les responsables de la santé publique et les décideurs politiques à surveiller et à traiter proactivement les problèmes de santé.

Module d'évaluation des risques : Ce module réalise une évaluation détaillée des risques pour les individus, offrant des évaluations objectives de leur état de santé général. En identifiant les personnes à haut risque, DiabetForecast permet des interventions précoces et des stratégies de prévention ciblées, visant ultimement à réduire l'incidence du DT2.

En fournissant une interface détaillée et conviviale, DiabetForecast facilite non seulement une meilleure gestion de la santé pour les individus, mais soutient également les professionnels de la santé dans la prise de décisions éclairées. La mise en œuvre de DiabetForecast pourrait améliorer significativement la détection et la prévention du DT2, particulièrement dans des contextes divers et à faibles ressources, en faisant un outil essentiel dans la lutte mondiale contre le diabète.


"""

text_en = """
DiabetForecast is an innovative solution designed to assess the risk of type 2 diabetes (T2D) using advanced artificial intelligence (AI) and machine learning techniques. This tool aims to overcome the limitations of traditional risk assessment methods, such as the Finnish Diabetes Risk Score (FINDRISC), by offering a more comprehensive, personalized, and adaptable approach.

DiabetForecast integrates a wide range of data, including demographic, medical, and lifestyle factors, to develop precise predictive models. Unlike FINDRISC, which relies on eight standard parameters, DiabetForecast considers the complex interactions between various risk factors, providing a nuanced analysis of an individual's health status. It also evaluates subjective health perceptions and tailors its predictions to the unique characteristics of each user, thereby enhancing the accuracy and relevance of its risk assessments.

DiabetForecast has two main components:

Health Analysis Dashboard: This component visualizes health trends within the population, displaying charts and metrics that reflect the overall health status of a community. It helps public health officials and policymakers monitor and proactively address health issues.

Risk Assessment Module: This module conducts detailed risk assessments for individuals, offering objective evaluations of their general health. By identifying high-risk individuals, DiabetForecast enables early interventions and targeted prevention strategies, ultimately aiming to reduce the incidence of T2D.

By providing a detailed and user-friendly interface, DiabetForecast not only facilitates better health management for individuals but also supports healthcare professionals in making informed decisions. The implementation of DiabetForecast could significantly improve the detection and prevention of T2D, especially in diverse and resource-limited settings, making it an essential tool in the global fight against diabetes.

"""


st.markdown(style, unsafe_allow_html=True)

chemin_image = "https://github.com/Moubarak321/DiabetForecast/blob/main/images/dia1.png?raw=true"
# def get_random_img(img_names: list[str]) -> str:
#     return random.choice(img_names)
whats = "images/whatsapp.svg"
link = "images/linkedin.svg"
def accueil():
    # st.divider()
    # st.write(f"<div style='text-align: justify;'>{text}</div>", unsafe_allow_html=True)
    # st.divider()
    with st.expander("**Abstract**"):
        st.info(text_en)
    with st.expander("**Résumé**"):
        st.info(text)
    # with st.expander("**Guide d'utilisation**"):
    #     st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum")
    with st.expander("**Authors**"):
        col1, col2 = st.columns(2)
        with col1:
            st.info("Massia Moubarak BENON MONRA")
            st.warning("Data Scientist || Django Dev || AI Dev")
            cola, colb, colc = st.columns(3)
            with cola:
                st.link_button("Whatsapp", "https://wa.me/22990838919?text=Hello%20MrBull%20!!!%20Je%20voudrais...")
            with colb:
                st.link_button("LinkedIn", "www.linkedin.com/in/moubarak-benon-monra-2104221bb")
            with colc:
                st.link_button("Portfolio", "https://moubarak-benon-monra.vercel.app/")
            
        with col2:
            st.info("Yean Delphonse Yaovi ASSOGBA")
            st.warning("Data Analyst || Django Dev")
            cola, colb, colc = st.columns(3)
            with cola:
                st.link_button("Whatsapp", "https://wa.me/22990569427?text=Hello%20Jean%20!!!%20Je%20voudrais...")
            with colb:
                st.link_button("LinkedIn", "")
            with colc:
                st.link_button("Portfolio", "")
            


                
    # with st.expander("Description du Projet DiabetForecast"):
    #     st.write()
    # st.image("https://static.streamlit.io/examples/dice.jpg")

st.markdown(f'<div class="image-container"><img src="{chemin_image}" alt="Ma superbe image"></div>', unsafe_allow_html=True)


menu = option_menu(None, ["Abstract", "Prévisions", "Analyses" ] ,
                icons=['house', 'lightbulb',  'bar-chart-fill'], 
                menu_icon="cast", default_index=1, orientation="horizontal")

if menu == "Prévisions":
    # st.image(f"images/{get_random_img(['diabetes1', 'diabetes2', 'diabetes3', 'diabetes4'])}.jpg")
    # prompt = f"Je suis peut-être diabétique ou en proie au diabète. prodigue moi des conseils pour améliorer mon etat de santé. utilise ce format pour répondre: {format} ."
    
    forecast.main()
    

elif menu == "Abstract":
    # forecast.main()
    accueil()
    


elif menu == "Analyses":
    analysis.main()



