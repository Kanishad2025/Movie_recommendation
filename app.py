import streamlit as st
import pickle

# Page Configuration
st.set_page_config(
    page_title="Movie Recommendation System",
    layout="wide"
)

# Load Data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Custom Styling
st.markdown("""
<style>

body {
    background-color: #0E1117;
}

.main {
    background-color: #0E1117;
    color: white;
}

.title {
    text-align: center;
    font-size: 48px;
    font-weight: 700;
    color: white;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #B0B0B0;
    margin-bottom: 40px;
}

.movie-card {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    color: white;
    border: 1px solid #333333;
}

.stButton>button {
    background-color: #262730;
    color: white;
    border-radius: 8px;
    border: 1px solid #444;
    height: 3em;
    width: 100%;
    font-size: 16px;
    font-weight: 600;
}

.stSelectbox label {
    font-size: 18px;
    font-weight: 500;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<div class="title">Movie Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Content-Based Movie Recommendation using Machine Learning</div>',
    unsafe_allow_html=True
)

# Movie Selection
movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Select a Movie",
    movie_list
)

# Recommendation Function
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

# Recommendation Button
if st.button('Recommend'):

    recommendations = recommend(selected_movie)

    st.markdown("## Recommended Movies")

    cols = st.columns(5)

    for idx, col in enumerate(cols):

        with col:

            st.markdown(
                f"""
                <div class="movie-card">
                    {recommendations[idx]}
                </div>
                """,
                unsafe_allow_html=True
            )