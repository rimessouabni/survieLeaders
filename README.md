# Analyse de survie avec lifelines

Ce projet consiste en une application Streamlit qui réalise une analyse de survie à l'aide de la bibliothèque lifelines. L'application fournit plusieurs fonctionnalités pour analyser les données de survie à partir du jeu de données Leaders.csv.

## Installation

Pour exécuter cette application, vous devez d'abord installer les dépendances. Vous pouvez le faire en exécutant la commande suivante dans votre terminal :

```bash
pip install -r requirements.txt
```

Assurez-vous d'avoir Python installé sur votre système.

## Utilisation

Une fois les dépendances installées, vous pouvez lancer l'application en exécutant la commande suivante :

```bash
streamlit run lifelinesScript.py
```

Cela lancera l'application Streamlit dans votre navigateur par défaut.

## Fonctionnalités

L'application offre les fonctionnalités suivantes :

- Affichage des statistiques descriptives sur la variable 'duration'.
- Affichage d'un histogramme de la durée pour l’ensemble de la population ou par type de régime.
- Estimation de la probabilité de survie et intervalle de confiance en utilisant la fonction Kaplan-Meier. Affichage du tableau des proportions de survivants à l’instant t.
- Représentation graphique de la courbe de survie avec intervalle de confiance.
- Représentation de la courbe de Kaplan-Meier pour dictateurs et démocrates, avec possibilité de choisir d'afficher la courbe pour l'un ou l'autre groupe ou pour les deux.

## Analyse

L'utilisation de l'application peut aider à analyser les données de survie en fournissant des informations visuelles et des statistiques descriptives. Voici quelques points clés de l'analyse :

- **Histogramme de la durée** : Permet de visualiser la distribution de la durée de survie dans la population globale ou par type de régime, ce qui peut donner des indications sur les différences de survie entre les groupes.
- **Courbe de survie** : La courbe de survie Kaplan-Meier montre la probabilité de survie au fil du temps, avec un intervalle de confiance. Cela permet d'observer les tendances de survie globales et de comparer les différents groupes.
- **Courbe de Kaplan-Meier pour les dictateurs et les démocrates** : En affichant les courbes de survie pour ces deux groupes, l'utilisateur peut comparer visuellement la survie entre les dictateurs et les démocrates, ce qui peut être pertinent dans le contexte de l'analyse des données politiques.

L'application offre une interface conviviale permettant à l'utilisateur d'interagir avec les données et de tirer des conclusions significatives sur la survie en fonction de différents facteurs.

## Auteurs

Ce projet a été développé par Rim Es-souabni, Clément Frensnel et Khalil Benzinab dans le cadre de TP DSA du module Data science du M1 Miage à Polytech Lyon, promotion 2023-2024.
