import streamlit as st
import random
import requests
import json

st.sidebar.selectbox('めにゅー', ['users', 'rooms'])
st.title("ユーザーAPIテスト")

with st.form(key='users'):
    user_id: int = random.randint(0, 10)
    username: str = st.text_area('ユーザー名', max_chars=12)
    data = {
        'user_id': user_id,
        'username': username
    }
    submit_button = st.form_submit_button(label='送信')


if submit_button:
    st.write('送信データ')
    st.json(data)
    url = "http://127.0.0.1:8000/users"
    res = requests.post(url, data=json.dumps(data))
    st.json(res.json())
