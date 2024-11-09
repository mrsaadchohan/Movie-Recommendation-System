import streamlit as st
import pickle
import pandas as pd
movies_list=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_list)
# movies_list=movies_list['title'].values
st.title('Movie Recommendation System')

similarity=pickle.load(open('similarty.pkl','rb'))
def recommend(movie_title):
    movie_index=movies[movies['title'] == movie_title].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movie=[]
    for i in distances:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie


selected_movie=st.selectbox('',movies['title'].values)
if st.button('Recommend'):
    recommendation=recommend(selected_movie)
    for i in recommendation:
        st.write(i)