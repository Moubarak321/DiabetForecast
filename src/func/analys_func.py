# import streamlit as st 
# # @st.cache_resource(experimental_allow_widgets=True)
# @st.cache_data
# def importation_of_dataset(path):
#     import pandas as pd
#     import streamlit as st 
#     import time
    
#     data = pd.read_csv(path)
#     with st.spinner('Chargement des données...'):
#         time.sleep(5)
#     # st.success("Données chargées avec succès")
#     return data

# #     plt.show()
# def visualize_single_correlation(feature_name, df, img_name):
#     import seaborn as sns
#     import matplotlib.pyplot as plt
#     import pandas as pd
#     import streamlit as st
#     import time
    
#     fig, axes = plt.subplots(2, 2, figsize=(15, 12))

#     # KDE Plot
#     sns.kdeplot(data=df, x=feature_name, hue="Diabetes_binary", multiple='stack', ax=axes[0, 0])
#     axes[0, 0].set_title(f'KDE Plot: {feature_name} vs Diabetes_binary',fontsize=20)

#     # Crosstab Barplot
#     cross_tab = pd.crosstab(df[feature_name], df['Diabetes_binary'], normalize='index')
#     cross_tab.plot(kind="bar", ax=axes[0, 1])
#     axes[0, 1].set_title(f"Bar plot: {feature_name} Vs Diabetes_binary",fontsize=20)
    
#     # Crosstab heatmap
#     sns.heatmap(cross_tab, annot=True, cmap='YlGnBu', fmt='0.2%', cbar=False, ax=axes[1, 0])
#     axes[1, 0].set_title(f'Cross-Tabulation: {feature_name} vs Diabetes_binary (%)',fontsize=20)

#     # Supprimez la sous-trace inutilisée
#     fig.delaxes(axes[1, 1])

#     plt.tight_layout()
#     plt.savefig(f"src/viz_img/{img_name}")
#     with st.spinner('Traitement...'):
#         time.sleep(5)
#     # st.success('Vos données sont prêtes!')
#     plt.show()







# #  correlation
# def visualize_corr(df):
#     import seaborn as sns
#     import matplotlib.pyplot as plt  # Import correctement pyplot de matplotlib
#     import streamlit as st
#     import time
#     # %config InlineBackend.figure_formats = 'svg'
#     # Calculez les corrélations et tracez le graphique
#     corr = df.drop('Diabetes_binary', axis=1).corrwith(df.Diabetes_binary).sort_values(ascending=False)
#     fig, ax = plt.subplots(figsize=(10, 4))
#     corr.plot(kind='bar', ax=ax, title="Diabetes_binary Correlation", alpha=0.8)
    
#     # Masquez les bords indésirables
#     ax.spines[['top', 'right', 'left']].set_visible(False)
    
#     # Ajoutez la grille à l'axe y
#     ax.yaxis.grid(True, linestyle='--', alpha=.5)
    
#     # Réglez les étiquettes x
#     plt.xticks(rotation=45, ha='right', size=15)
#     # plt.savefig('correlation_plot.png')
#     with st.spinner('Traitement...'):
#         time.sleep(5)
#     plt.show()  # Affichez le graphique



# def histplot(df,feature, img_name):
#     import seaborn as sns
#     import matplotlib.pyplot as plt 
#     import streamlit as st 
#     import time
#     plt.figure(figsize = (10,6))
#     sns.kdeplot(df , x= df[feature],hue=df["Diabetes_binary"] ,multiple='stack' )
#     # sns.scatterplot(df[feature])
#     plt.tight_layout()

#     plt.savefig(f"src/viz_img/{img_name}")
#     with st.spinner('Traitement...'):
#         time.sleep(5)
#     plt.show()



# def pearson_corr(df):
#     import pandas as pd
#     import seaborn as  sns 
#     import matplotlib.pyplot as plt 
#     pearson_corr = df.drop("Diabetes_binary", axis =1).corrwith(df["Diabetes_binary"]).abs()
#     sort_pearson_corr = pearson_corr.sort_values(ascending=False)
#     sort_pearson_corr_df = pd.DataFrame({"Column": sort_pearson_corr.index, "Correlation":sort_pearson_corr.values})
#     # Tri à partir de values >0.05
#     sort_pearson_corr_df = sort_pearson_corr_df[sort_pearson_corr_df.Correlation > 0.05]

#     plt.figure(figsize=(6,6))
#     sns.barplot(x="Correlation", y="Column", data=sort_pearson_corr_df, palette='viridis')

#     plt.xlabel("indice de corrélation")
#     plt.ylabel("Indicateurs cliniques")
#     plt.title("Matrice de corrélation entre les indicateurs cliniques du diabète")

#     plt.tight_layout()
#     plt.show







# ***************************************gpt***************************************************

# import streamlit as st 
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import time

# @st.cache_data
# def importation_of_dataset(path):
#     data = pd.read_csv(path)
#     with st.spinner('Chargement des données...'):
#         time.sleep(5)
#     return data

# def visualize_single_correlation(feature_name, df, img_name):
#     fig, axes = plt.subplots(2, 2, figsize=(15, 12))

#     # KDE Plot
#     sns.kdeplot(data=df, x=feature_name, hue="Diabetes_binary", multiple='stack', ax=axes[0, 0])
#     axes[0, 0].set_title(f'KDE Plot: {feature_name} vs Diabetes_binary', fontsize=20)

#     # Crosstab Barplot
#     cross_tab = pd.crosstab(df[feature_name], df['Diabetes_binary'], normalize='index')
#     cross_tab.plot(kind="bar", ax=axes[0, 1])
#     axes[0, 1].set_title(f"Bar plot: {feature_name} Vs Diabetes_binary", fontsize=20)
    
#     # Crosstab heatmap
#     sns.heatmap(cross_tab, annot=True, cmap='YlGnBu', fmt='0.2%', cbar=False, ax=axes[1, 0])
#     axes[1, 0].set_title(f'Cross-Tabulation: {feature_name} vs Diabetes_binary (%)', fontsize=20)

#     # Supprimez la sous-trace inutilisée
#     fig.delaxes(axes[1, 1])

#     plt.tight_layout()
#     plt.savefig(f"src/viz_img/{img_name}")
#     with st.spinner('Traitement...'):
#         time.sleep(5)
#     return fig

# def visualize_corr(df):
#     corr = df.drop('Diabetes_binary', axis=1).corrwith(df.Diabetes_binary).sort_values(ascending=False)
#     fig, ax = plt.subplots(figsize=(10, 4))
#     corr.plot(kind='bar', ax=ax, title="Diabetes_binary Correlation", alpha=0.8)
    
#     ax.spines[['top', 'right', 'left']].set_visible(False)
#     ax.yaxis.grid(True, linestyle='--', alpha=.5)
#     plt.xticks(rotation=45, ha='right', size=15)
#     with st.spinner('Traitement...'):
#         time.sleep(5)
#     return fig

# def histplot(df, feature, img_name):
#     fig = plt.figure(figsize=(10, 6))
#     sns.kdeplot(df, x=df[feature], hue=df["Diabetes_binary"], multiple='stack')
#     plt.tight_layout()
#     plt.savefig(f"src/viz_img/{img_name}")
#     with st.spinner('Traitement...'):
#         time.sleep(5)
#     return fig

# def pearson_corr(df):
#     pearson_corr = df.drop("Diabetes_binary", axis=1).corrwith(df["Diabetes_binary"]).abs()
#     sort_pearson_corr = pearson_corr.sort_values(ascending=False)
#     sort_pearson_corr_df = pd.DataFrame({"Column": sort_pearson_corr.index, "Correlation": sort_pearson_corr.values})
#     sort_pearson_corr_df = sort_pearson_corr_df[sort_pearson_corr_df.Correlation > 0.05]

#     fig = plt.figure(figsize=(6, 6))
#     sns.barplot(x="Correlation", y="Column", data=sort_pearson_corr_df, palette='viridis')

#     plt.xlabel("indice de corrélation")
#     plt.ylabel("Indicateurs cliniques")
#     plt.title("Matrice de corrélation entre les indicateurs cliniques du diabète")
#     plt.tight_layout()
#     return fig








# *****************************gpt jean*******************************

import streamlit as st
@st.cache_data
def importation_of_dataset(path):
    import pandas as pd
    import time
    
    data = pd.read_csv(path)
    with st.spinner('Chargement des données...'):
        time.sleep(5)
    return data

def visualize_single_correlation(feature_name, df, img_name):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd
    import time
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))

    sns.kdeplot(data=df, x=feature_name, hue="Diabetes_binary", multiple='stack', ax=axes[0, 0])
    axes[0, 0].set_title(f'KDE Plot: {feature_name} vs Diabetes_binary', fontsize=20)

    cross_tab = pd.crosstab(df[feature_name], df['Diabetes_binary'], normalize='index')
    cross_tab.plot(kind="bar", ax=axes[0, 1])
    axes[0, 1].set_title(f"Bar plot: {feature_name} Vs Diabetes_binary", fontsize=20)
    
    sns.heatmap(cross_tab, annot=True, cmap='YlGnBu', fmt='0.2%', cbar=False, ax=axes[1, 0])
    axes[1, 0].set_title(f'Cross-Tabulation: {feature_name} vs Diabetes_binary (%)', fontsize=20)

    fig.delaxes(axes[1, 1])

    plt.tight_layout()
    plt.savefig(f"src/viz_img/{img_name}")
    with st.spinner('Traitement...'):
        time.sleep(5)
    
    st.pyplot(fig)

def visualize_corr(df):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import time

    corr = df.drop('Diabetes_binary', axis=1).corrwith(df.Diabetes_binary).sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 4))
    corr.plot(kind='bar', ax=ax, title="Diabetes_binary Correlation", alpha=0.8)
    
    ax.spines[['top', 'right', 'left']].set_visible(False)
    ax.yaxis.grid(True, linestyle='--', alpha=.5)
    plt.xticks(rotation=45, ha='right', size=15)
    
    with st.spinner('Traitement...'):
        time.sleep(5)
    st.pyplot(fig)

def histplot(df, feature, img_name):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import time
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=df, x=feature, hue="Diabetes_binary", multiple='stack')
    plt.tight_layout()
    plt.savefig(f"src/viz_img/{img_name}")
    with st.spinner('Traitement...'):
        time.sleep(5)
    st.pyplot(plt.gcf())

def pearson_corr(df):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    pearson_corr = df.drop("Diabetes_binary", axis=1).corrwith(df["Diabetes_binary"]).abs()
    sort_pearson_corr = pearson_corr.sort_values(ascending=False)
    sort_pearson_corr_df = pd.DataFrame({"Column": sort_pearson_corr.index, "Correlation": sort_pearson_corr.values})
    sort_pearson_corr_df = sort_pearson_corr_df[sort_pearson_corr_df.Correlation > 0.05]

    plt.figure(figsize=(6, 6))
    sns.barplot(x="Correlation", y="Column", data=sort_pearson_corr_df, palette='viridis')

    plt.xlabel("indice de corrélation")
    plt.ylabel("Indicateurs cliniques")
    plt.title("Matrice de corrélation entre les indicateurs cliniques du diabète")

    plt.tight_layout()
    st.pyplot(plt.gcf())
