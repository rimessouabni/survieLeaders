import streamlit as st
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.datasets import load_dd
from lifelines.utils import survival_table_from_events

# Charger les données
data = load_dd()

# Titre de l'application
st.title('Analyse de survie avec lifelines')

# Affichage des statistiques descriptives
st.subheader("Statistiques descriptives sur la variable 'duration':")
st.write(data['duration'].describe())

# Affichage de l'histogramme de la durée pour l'ensemble de la population ou par type de régime
st.subheader('Histogramme de la durée')
option = st.radio("Afficher l'histogramme pour :", ('Ensemble de la population', 'Par type de régime'))
if option == 'Ensemble de la population':
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(data['duration'], bins=20, color='skyblue', edgecolor='black')
    ax.set_xlabel('Durée')
    ax.set_ylabel('Nombre de cas')
    ax.set_title('Histogramme de la durée pour l’ensemble de la population')
    st.pyplot(fig)
else:
    regimes = data['regime'].unique()
    selected_regime = st.selectbox('Sélectionnez un régime :', regimes)
    subset = data[data['regime'] == selected_regime]
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(subset['duration'], bins=30, color='skyblue', edgecolor='black')
    ax.set_xlabel('Durée')
    ax.set_ylabel('Fréquence')
    ax.set_title(f'Histogramme de la durée pour le régime "{selected_regime}"')
    st.pyplot(fig)

# Estimation de la probabilité de survie et intervalle de confiance avec KaplanMeier
st.subheader('Estimation de la probabilité de survie')
kmf = KaplanMeierFitter()
kmf.fit(data['duration'], event_observed=data['observed'])
st.write("Tableau des proportions de survivants:")
st.write(survival_table_from_events(kmf.event_observed, kmf.durations).head())

# Affichage de la courbe de survie avec intervalle de confiance
st.subheader('Courbe de survie avec intervalle de confiance')
fig, ax = plt.subplots(figsize=(10, 6))
kmf.plot_survival_function(ax=ax, ci_show=True)
ax.set_xlabel('Durée')
ax.set_ylabel('Probabilité de survie')
st.pyplot(fig)

# Courbe de Kaplan-Meier pour dictateurs et démocrates
st.subheader('Courbe de Kaplan-Meier')
group_option = st.radio("Afficher la courbe pour :", ('Dictateurs', 'Démocrates', 'Les deux groupes'))
fig, ax = plt.subplots(figsize=(10, 6))
kmf_dictators = KaplanMeierFitter()
kmf_dictators.fit(data[data['democracy'] == 'Non-democracy']['duration'], event_observed=None, label='Dictateurs')
kmf_democrats = KaplanMeierFitter()
kmf_democrats.fit(data[data['democracy'] == 'Democracy']['duration'], event_observed=None, label='Démocrates')
if group_option == 'Dictateurs':
    kmf_dictators.plot(ax=ax)
elif group_option == 'Démocrates':
    kmf_democrats.plot(ax=ax)
else:
    kmf_dictators.plot(ax=ax)
    kmf_democrats.plot(ax=ax)
ax.set_xlabel('Durée')
ax.set_ylabel('Probabilité de survie')
ax.legend()
st.pyplot(fig)