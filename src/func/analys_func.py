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
    plt.close(fig)
    st.stop()
    
    

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
    plt.close(fig)
    

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
    plt.close()
    
    
    

def pearson_corr(df):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import plotly.express as px

    
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
    plt.close()
    
    



# ******************************************************plotly*****************************************************
# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# import time

# @st.cache_data
# def importation_of_dataset(path):
#     data = pd.read_csv(path)
#     with st.spinner('Chargement des données...'):
#         time.sleep(5)
#     return data

# def visualize_single_correlation(feature_name, df, img_name):
#     fig = make_subplots(rows=2, cols=2, subplot_titles=(f"KDE Plot: {feature_name} vs Diabetes_binary",
#                                                         f"Bar plot: {feature_name} Vs Diabetes_binary",
#                                                         f"Cross-Tabulation: {feature_name} vs Diabetes_binary (%)"))

#     kde_fig = px.histogram(df, x=feature_name, color='Diabetes_binary', nbins=50, histnorm='density', title=f"KDE Plot: {feature_name} vs Diabetes_binary")
#     bar_fig = px.bar(pd.crosstab(df[feature_name], df['Diabetes_binary'], normalize='index').reset_index(), x=feature_name, y=[0, 1], barmode='group', title=f"Bar plot: {feature_name} Vs Diabetes_binary")
#     cross_tab = pd.crosstab(df[feature_name], df['Diabetes_binary'], normalize='index')
#     heatmap_fig = px.imshow(cross_tab, text_auto=True, aspect="auto", title=f"Cross-Tabulation: {feature_name} vs Diabetes_binary (%)")

#     for trace in kde_fig.data:
#         fig.add_trace(trace, row=1, col=1)
#     for trace in bar_fig.data:
#         fig.add_trace(trace, row=1, col=2)
#     for trace in heatmap_fig.data:
#         fig.add_trace(trace, row=2, col=1)

#     fig.update_layout(height=800, width=1000, title_text=f"Visualisation de la corrélation pour {feature_name}")

#     with st.spinner('Traitement...'):
#         time.sleep(5)
#     st.plotly_chart(fig)

# def visualize_corr(df):
#     corr = df.drop('Diabetes_binary', axis=1).corrwith(df.Diabetes_binary).sort_values(ascending=False)
#     corr_df = corr.reset_index().rename(columns={0: 'Correlation', 'index': 'Feature'})
#     fig = px.bar(corr_df, x='Feature', y='Correlation', title="Diabetes_binary Correlation", labels={'Correlation': 'Correlation', 'Feature': 'Feature'})

#     fig.update_layout(xaxis=dict(tickangle=45))

#     with st.spinner('Traitement...'):
#         time.sleep(5)
#     st.plotly_chart(fig)

# def histplot(df, feature):
#     fig = px.histogram(df, x=feature, color='Diabetes_binary', nbins=50, histnorm='density', title=f"Histogramme: {feature} vs Diabetes_binary")

#     with st.spinner('Traitement...'):
#         time.sleep(5)
#     st.plotly_chart(fig, theme="streamlit")

# def pearson_corr(df):
#     pearson_corr = df.drop("Diabetes_binary", axis=1).corrwith(df["Diabetes_binary"]).abs()
#     sort_pearson_corr = pearson_corr.sort_values(ascending=False)
#     sort_pearson_corr_df = pd.DataFrame({"Column": sort_pearson_corr.index, "Correlation": sort_pearson_corr.values})
#     sort_pearson_corr_df = sort_pearson_corr_df[sort_pearson_corr_df.Correlation > 0.05]

#     fig = px.bar(sort_pearson_corr_df, x="Correlation", y="Column", orientation='h', title="Matrice de corrélation entre les indicateurs cliniques du diabète", color="Correlation", color_continuous_scale='viridis')

    
#     st.plotly_chart(fig, theme="streamlit")
    