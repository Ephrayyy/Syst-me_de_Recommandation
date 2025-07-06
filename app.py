import streamlit as st
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics.pairwise import cosine_similarity

# --------- Chargement des données ----------
@st.cache_data
def load_data():
    movies = pd.read_csv("data/movie.csv").sample(500)
    ratings = pd.read_csv("data/rating.csv").sample(500)


    # Genres
    movies['genres'] = movies['genres'].str.split('|')
    mlb = MultiLabelBinarizer()
    genre_matrix = mlb.fit_transform(movies['genres'])
    genre_df = pd.DataFrame(genre_matrix, columns=mlb.classes_, index=movies['title'])

    # Matrice utilisateur × film pour filtrage collaboratif
    df = pd.merge(ratings, movies[['movieId', 'title']], on='movieId')
    user_movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')
    
    # Similarité genres
    cosine_sim = cosine_similarity(genre_df)

    return movies, genre_df, cosine_sim, user_movie_matrix, df

movies, genre_df, cosine_sim, user_movie_matrix, ratings_full = load_data()
indices = pd.Series(range(len(genre_df)), index=genre_df.index)

# --------- Reco par genre ----------
def recommend_by_genre(title, n=5):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n+1]
    movie_indices = [i[0] for i in sim_scores]
    return genre_df.iloc[movie_indices].index.tolist()

# --------- Reco par similarité (notes) ----------
def recommend_by_similarity(title, min_ratings=50, n=5):
    if title not in user_movie_matrix:
        return ["Ce film n'a pas assez de notes."]
    target_ratings = user_movie_matrix[title]
    similar_movies = user_movie_matrix.corrwith(target_ratings).dropna()
    
    corr_df = pd.DataFrame(similar_movies, columns=['correlation'])
    corr_df['num_ratings'] = ratings_full.groupby('title')['rating'].count()
    
    filtered = corr_df[corr_df['num_ratings'] > min_ratings].sort_values('correlation', ascending=False)
    results = filtered.drop(title).head(n)
    return results.index.tolist()

# --------- Interface utilisateur ----------
st.title("🎬 Système de Recommandation de Films")

# Choix du film
selected_movie = st.selectbox("Choisissez un film :", sorted(movies['title'].unique()))

# Choix de la méthode
method = st.radio("Méthode de recommandation :", ["Par genre", "Par similarité de notes"])

if st.button("Recommander"):
    st.subheader("🎥 Films recommandés :")
    if method == "Par genre":
        recs = recommend_by_genre(selected_movie)
    else:
        recs = recommend_by_similarity(selected_movie)

    for i, movie in enumerate(recs, start=1):
        st.write(f"{i}. {movie}")
