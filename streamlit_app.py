import streamlit as st 
from streamlit_option_menu import option_menu
from src import analysis 
import random





text = """
L'autosuffisance énergétique demeure un enjeu de taille pour chaque nation.

Notre projet consiste en une prévision instantanée de la consommation énergétique afin d'optimiser les réseaux de distribution et les adopter les meilleurs stratégies de stockage.
                                                                    
Les modèles de ce projet ont été construits sur les données de la ville de Tétouan au Maroc et apposés à trois villes de cotonou dont Calavi, Ganhi et Akpakpa. Les données de consommation sont données en KW pour ces trois zones.



"""


# def get_random_img(img_names: list[str]) -> str:
#     return random.choice(img_names)

def accueil():
    # st.divider()
    # st.write(f"<div style='text-align: justify;'>{text}</div>", unsafe_allow_html=True)
    # st.divider()
    with st.expander("**Description du Projet DiabetForecast**"):
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum")
    with st.expander("**Guide d'utilisation**"):
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum")
    with st.expander("**Auteurs**"):
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum")
    # with st.expander("Description du Projet DiabetForecast"):
    #     st.write()
    # st.image("https://static.streamlit.io/examples/dice.jpg")

menu = option_menu(None, ["Accueil", "Analyses", "Prévisions" ] ,
                icons=['house', 'bar-chart-fill',  'gear'], 
                menu_icon="cast", default_index=0, orientation="horizontal")

if menu == "Accueil":
    # st.image(f"images/{get_random_img(['diabetes1', 'diabetes2', 'diabetes3', 'diabetes4'])}.jpg")
    accueil()


elif menu == "Analyses":
    analysis.data_viz()


