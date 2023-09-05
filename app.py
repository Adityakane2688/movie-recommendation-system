import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(layout="wide",
                   page_title="Movie Recommendation App")
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)
import streamlit as st
st.markdown("<h1 style='text-align: center; color: white;'>MOVIE RECOMMENDATION</h1>", unsafe_allow_html=True)
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    m_index = movies[movies['title'] == movie].index[0]
    distance = similar[m_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies_dict = pickle.load(open('model\movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

select = st.selectbox('Select A Movie',movies['title'].values)
similar = pickle.load(open('model\similar.pkl','rb'))




if st.button('Recommend'):
    names,posters = recommend(select)
    recommended_movie_names,recommended_movie_posters = recommend(select)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.subheader(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.subheader(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.subheader(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.subheader(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.subheader(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
