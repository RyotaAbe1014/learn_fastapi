import streamlit as st
import pandas as pd
import numpy as np

# サイドバーに配置
op = st.sidebar.multiselect('選んでね', ['a', 'b', 'c'], ['a'])

# サイドバーに配置
number = st.sidebar.slider('', 0, 100)

# カラム(bootstrapみたいなやつ)
left_col, right_col = st.columns(2)
left_col.write("aaa")
right_col.write("aaa")