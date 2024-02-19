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









# =======================================================================
    # New Version
# =======================================================================

# ::::::::::::: Relation between Diabet with major feature :::::::::::::

# def visualize_feature(feature_name, df):
#   fig, axes = plt.subplots(3,1, figsize=(6,18))

#   # Pie chart
#   df[feature_name].value_counts().plot(kind="pie", autopct='%.02f',ax=axes[0])
#   axes[0].set_title(f'Pie Chart: {feature_name}')

#   # Crosstab heatmap
#   cross_tab = pd.crosstab(df[feature_name], df['Diabetes_binary'], normalize='index')
#   sns.heatmap(cross_tab, annot=True, cmap='YlGnBu', fmt='0.2%', cbar=False, ax=axes[1])
#   axes[1].set_title(f'Cross-Tabulation: {feature_name} vs Diabetes_binary (%)')

#   # Crosstab Barplot
#   cross_tab.plot(kind="bar", ax=axes[2])
#   axes[2].set_title(f"Bar plot: {feature_name} Vs Diabetes_binary")

#   plt.tight_layout()
#   plt.show()



# def visualize_feature(feature_name, df):
#     fig, axes = plt.subplots(3,1, figsize=(6.18))

#     # Pie chart
#     df[feature_name].value_counts().plot(kind="pie", autopct='%.02f', ax=axes[0])
#     axes[0].set_title(f'Pie Chart: {feature_name}')

#     # CrossTab heatmap
#     cross_tab = pd.crosstab(df[feature_name],df['Diabetes_binary'], normalize='index')
#     sns.heatmap(cross_tab,annot=True, cmap="YlGnBu", fmt="0.2%", cbar=False, ax=axes[1])
#     axes[1].set_title(f"Cross-Tabulation:{feature_name} vs Diabetes")

#     # CrossTba Barplot
#     cross_tab.plot(kind="bar", ax=axes[2])
#     axes[2].set_title(f"Bar Plot: {feature_name} Vs Diabete")

#     plt.tight_layout()
#     plt.show()



#  correlation
# def visualize_corr(df):
#     import matplotlib.pyplot as plt

#     (df.drop('Diabetes_binary', axis=1)
#    .corrwith(df.Diabetes_binary)
#    .sort_values(ascending=False)
#    .plot(kind='bar', figsize=(10, 4), title="Diabetes_binary Correlation", alpha=0.8, zorder=3)
#    .spines[['top','right', 'left']].set_visible(False)
#    )
#     plt.grid(axis='y', linestyle='--', alpha=.5)
#     plt.xticks(rotation = 45, ha='right', size=15)