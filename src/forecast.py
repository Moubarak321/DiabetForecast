import streamlit as st

def main():
    st.title("Évaluez votre état de santé")
    features = []
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
    ans={
        "":"",

        "Non":0,
         "Oui":1}
    genre={"":"","Homme":1, "Femme":0}
    yes_or_no={"":"","Oui":1,"Non":0}
    


    col1, col2 = st.columns(2)
    with col1:
        age = st.selectbox("Entrez votre âge", age_mapping, )
        age=age_mapping[age]
        BMI = int(st.number_input("Entrez votre indice de masse corporelle",key="c"))
        chol = st.selectbox("Avez-vous un taux de cholesterol élevé ?", yes_or_no)
        HighChol = yes_or_no[chol]

    veggie = st.selectbox("Consommez-vous des légumes quotidiennement ?", yes_or_no)
    Veggie = yes_or_no[veggie]

    with col2:
        sexe = st.selectbox("Quel est votre genre",genre,key="b",)
        Sexe = genre[sexe]

        highbp = st.selectbox("Ëtes-vous hypertendus ?", ans,key="skjdn")
        Highbp=ans[highbp]

        fruit = st.selectbox("Consommez-vous au moins un fruit pas jour ?", yes_or_no, key="skjv")
        Fruit = yes_or_no[fruit]

    Genhlth = st.selectbox("Quelle note sur 5 donneriez-vous à votre état de santé général ?", [1,2,3,4,5], key="skssjv")
    PhysHlth = st.selectbox("Pendant combien de jours au cours des 30 derniers jours votre santé physique n'a-t-elle pas été bonne ?",[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30] ,placeholder="Âge", key="dddddg")
    MentHlth =st.selectbox("Pensez maintenant à votre santé mentale, qui comprend le stress, la dépression et les problèmes émotionnels, pendant combien de jours au cours des 30 derniers jours votre santé mentale n'a-t-elle pas été bonne. ?",[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30], placeholder="Âge", key="eeeeeg")    
    smoke = st.selectbox("Avez-vous fumé au moins 100 cigarettes (05 paquets) au cours de votre vie ?",yes_or_no,key="h")
    Smoke = yes_or_no[smoke]
    
    features.append(Highbp)
    features.append(HighChol)
    features.append(BMI)
    features.append(Smoke)
    features.append(Fruit)
    features.append(Veggie)
    features.append(Genhlth)
    features.append(MentHlth)
    features.append(PhysHlth)
    features.append(Sexe)
    features.append(age)
    print("Features: ", features)
    
        
    