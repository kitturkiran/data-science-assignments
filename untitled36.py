# -*- coding: utf-8 -*-
"""Untitled36.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12u8oOuCBD5-S-kkMXCVoUJ3e-bAPi-c3
"""


import streamlit as st
import pickle
import pandas as pd
import requests

st.title('books Recommender System')



def recommend(books):


  
  distances, indices = model.kneighbors(matrix.loc[books].values.reshape(1, -1), n_neighbors =10)

  for i in range(0, len(distances.flatten())):
    if i > 0:
        return(matrix.index[indices.flatten()[i]]) 


matrix= pickle.load(open('books.pkl','rb'))

model= pickle.load(open('model.pkl','rb'))

books_list = matrix['Book-Title'].values
selected_movie = st.selectbox(
    'Select a books from drop down',
    books_list)

st.write('You selected:', selected_movie)


if st.button('Show Recommend book'):
    recommended_movie_names = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movie_names[0])
        

    with col2:
        st.text(recommended_movie_names[1])
      

    with col3:
        st.text(recommended_movie_names[2])
      

    with col4:
        st.text(recommended_movie_names[3])
       

    with col5:
        st.text(recommended_movie_names[4])

