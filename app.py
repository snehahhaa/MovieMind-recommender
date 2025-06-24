import streamlit as st
import pickle
import requests
import gdown
import os

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    except:
        return None
    return None

# Load movies list
movies = pickle.load(open("movies_list.pkl", 'rb'))

# Load similarity.pkl from Google Drive if not already downloaded
if not os.path.exists("similarity.pkl"):
    url = "https://drive.google.com/uc?id=1fVQaX7NSp_BXCDQh2cBlrBtP-giTY_6b"
    gdown.download(url, "similarity.pkl", quiet=False)

similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

# Streamlit UI setup
st.set_page_config(
    page_title="MovieMind",
    page_icon="https://cdn-icons-png.flaticon.com/512/6347/6347815.png",
    layout="wide"
)

st.markdown("""
    <style>
    header, [data-testid="stHeader"], [data-testid="stDecoration"] {
        display: none !important;
    }
    .block-container {
        padding-top: 1rem !important;
    }
    .logo {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .logo img {
        width: 90px;
        height: auto;
    }
    .title {
        text-align: center;
        color: var(--text-color);
        font-size: 3em;
        margin-bottom: 10px;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        color: var(--text-color);
        font-size: 1.2em;
        margin-bottom: 40px;
    }
    .movie-title {
        color: var(--text-color);
        font-size: 0.9em;
        margin-top: 8px;
        font-weight: 500;
        text-align: center;
    }
    .stButton>button {
        background-color: #22c55e;
        color: white;
        padding: 0.5em 1em;
        border-radius: 8px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #15803d;
        transition: 0.3s;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='logo'>
        <img src='https://cdn-icons-png.flaticon.com/512/6347/6347815.png' alt='MovieMind Logo'>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>MovieMind</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Discover movies that match your cinematic taste</div>", unsafe_allow_html=True)

selected_movie = st.selectbox("Choose a movie", movies_list)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_titles = []
    recommended_posters = []
    for i in distances[1:20]:
        movie_id = movies.iloc[i[0]].id
        title = movies.iloc[i[0]].title
        poster = fetch_poster(movie_id)
        if poster:
            recommended_titles.append(title)
            recommended_posters.append(poster)
        if len(recommended_titles) == 6:
            break
    return recommended_titles, recommended_posters

if st.button("Show Recommendations"):
    titles, posters = recommend(selected_movie)
    if titles:
        cols = st.columns(len(titles))
        for i in range(len(titles)):
            with cols[i]:
                st.markdown(
                    f"<img src='{posters[i]}' style='height:240px; display:block; margin:auto; border-radius:8px;'>",
                    unsafe_allow_html=True
                )
                st.markdown(f"<div class='movie-title'>{titles[i]}</div>", unsafe_allow_html=True)
    else:
        st.error("No recommendations found. Please try another movie.")
