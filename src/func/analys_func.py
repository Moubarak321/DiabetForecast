import streamlit as st 

@st.cache_resource(experimental_allow_widgets=True)
def importation_of_dataset(path):
    import pandas as pd
    data = pd.read_csv(path)
    return data

# diabetics patients
def diabetics(data):
    diabetics = data[data['diabetes'] == 1]
    return diabetics

# ::::::::::::::::::        diabetics ages/bmi/glucose viz      ::::::::::::::::::
# scatterplot
def scatter(data, col):
    import seaborn as sns
    import matplotlib as plt
    # plt.figure(figsize=(10,5))
    sns.scatterplot(data[col])
    # plt.xlabels("Population")
    # plt.ylabels("Ages")
    # plt.title("Distribution des diabétiques en fonction de la variable {}".format(col))

# histplot:
def histplot(data, col):
    import seaborn as sns
    import matplotlib as plt
    # plt.figure(figsize=(10,5))
    sns.histplot(data[col], kde=True)
    # plt.ylabels("Counts")
    # plt.xlabels("Ages")
    # plt.title("Distribution des diabétiques en fonction de la variable {}".format(col))

# Densité
def densite(data, col):
    import seaborn as sns
    import matplotlib as plt
    # plt.figure(figsize=(10,5))
    sns.kdeplot(data[col])
    # plt.ylabels("Counts")
    # plt.xlabels("Ages")
    # plt.title("Distribution des diabétiques en fonction de la variable {}".format(col))

