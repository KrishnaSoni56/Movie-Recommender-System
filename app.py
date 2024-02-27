import streamlit as st
import pickle
movies_list = pickle.load(open('movies_list.pkl' , 'rb'))  # DataFrame
movies_list = movies_list['title'].values

st.title('Movie Recommender System')

# Creating form
# Creating SelectBox for movies_list

option = st.selectbox(
    'How would you' , movies_list
)