import streamlit as st
import random
import requests
import json

page = st.sidebar.selectbox('めにゅー', ['users', 'rooms'])

if page == 'users':
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

elif page == 'rooms':
    st.title("会議室APIテスト")
    with st.form(key='room'):
        room_id: int = random.randint(0, 10)
        room_name: str = st.text_area('会議室名', max_chars=12)
        capacity: int = st.number_input('定員', step=1)

        data = {
            'room_id': room_id,
            'room_name': room_name,
            'capacity': capacity
        }
        submit_button = st.form_submit_button(label='送信')

    if submit_button:
        st.write('送信データ')
        st.json(data)
        url = "http://127.0.0.1:8000/rooms"
        res = requests.post(url, data=json.dumps(data))
        st.json(res.json())
