import streamlit as st
import pandas as pd
import numpy as np

if st.button('click me'):
    st.write('クリックされました！')


st.checkbox('やあ')

op = st.multiselect('選んでね', ['a', 'b', 'c'], ['a'])

number = st.slider('', 0, 100)
