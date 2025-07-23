import streamlit as st
import pandas as pd
import pickle
import os
import ast


def recommend(movie_title):
    movie_index = movie[movie["title"] == movie_title].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movie.iloc[i[0]].title)
    return  recommended_movies

movie_dict = pickle.load(open("movie_dict_data.pkl","rb"))
movie = pd.DataFrame(movie_dict)

similarity = pickle.load(open("similarity_data.pkl","rb"))

st.title("Get your Movie!")

selected_movie_name = st.selectbox("Select your favourite movie!",
movie['title'].values)
if selected_movie_name: 
#for code running
# if st.button("More like This"):
    reccomended = recommend(selected_movie_name)
    for i in reccomended:
      st.write(i)