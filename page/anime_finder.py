import streamlit as st
import requests
import urllib3

urllib3.disable_warnings()

KITSU_API_ENDPOINT = st.secrets['KITSU_API_ENDPOINT']


def search_anime(title):
    headers = {
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    payload = {
        'filter[text]': title
    }
    response = requests.get(url=KITSU_API_ENDPOINT, params=payload, headers=headers, verify=False).json()['data']
    response = [x for x in response if x['id'] == '1']
    return response

anime_data = search_anime('')

TITLE = 'Anime Finder'
st.write(f'<h1 style=text-align:left>{TITLE}</h1>', unsafe_allow_html=True)
st.write('<hr>', unsafe_allow_html=True)
st.text_input(label='Anime Title', placeholder='Enter complete or partial anime name', key='title')
