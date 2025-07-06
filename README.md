
# 🎬 Movie Recommender App

Cette application Streamlit propose deux types de recommandations de films à partir du dataset MovieLens :

- 🔁 **Filtrage collaboratif** : basé sur les notes des utilisateurs
- 🧩 **Filtrage par contenu** : basé sur les genres des films

---

## 🚀 Fonctionnalités

- Choisissez un film depuis une liste déroulante
- Sélectionnez la méthode de recommandation :
  - **Par similarité de notes** (collaboratif)
  - **Par similarité de genres** (contenu)
- Obtenez les 5 films les plus similaires recommandés

---

## 📁 Structure du projet

```
movie_recommender/
├── app.py                # Application Streamlit principale
├── requirements.txt      # Dépendances à installer
├── data/
│   ├── movie.csv         # Fichier avec titres et genres
│   ├── rating.csv        # Notes des utilisateurs
```

---

## ⚙️ Installation

### 1. Cloner le repo et entrer dans le dossier

```bash
git clone https://github.com/tonprofil/movie_recommender.git
cd movie_recommender
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## ▶️ Lancer l'application

```bash
streamlit run app.py
```

L'application s’ouvrira automatiquement dans votre navigateur à l’adresse :  
`http://localhost:8501`

---

## 📦 Données utilisées

Les fichiers `movie.csv` et `rating.csv` proviennent du dataset [MovieLens](https://grouplens.org/datasets/movielens/).
https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset
https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews

---

## ✅ À venir (améliorations possibles)

- Recommandation par tags (`genome_scores.csv`)
- Système hybride (collaboratif + contenu)
- Ajout des affiches de films via TMDb API
- Déploiement en ligne (Vercel, Streamlit Cloud…)

---

## 👨‍💻 Auteur

Projet développé par moi (Ephraïm KOSSONOU) dans le cadre d’un apprentissage pratique des systèmes de recommandation.
