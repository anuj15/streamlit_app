import streamlit as st
import pandas as pd

MY_BIO = """
Hi, I’m Anuj Gupta!\n
I graduated with a degree in Computer Engineering in 2014.\n
I'm currently work as a Software Quality Engineer at S&P Global.
"""
APP_INTRO = """
<hr>
<div style="text-align: center">Below you can find some of the apps that I have build in Python.
<hr></div>
"""

IMAGE_PATH = 'images/portfolio/'
DATA_PATH = 'data/portfolio.csv'
TITLE = 'Anuj Gupta'
st.write(f'<h1 style=text-align:center>{TITLE}</h1><hr>', unsafe_allow_html=True)

l, r = st.columns(spec=2)
with l:
    st.image(image=f'{IMAGE_PATH}/avatar.png', width=400)
with r:
    st.write(MY_BIO)

st.write(APP_INTRO, unsafe_allow_html=True)
app_data = pd.read_csv(filepath_or_buffer=DATA_PATH, sep=';').to_dict(orient='records')

l, r = st.columns(spec=2)


def show_data(d):
    st.write(f'<h3><a href="{d['url']}" target="_blank">{d["title"]}</a></h3>', unsafe_allow_html=True)
    st.write(d['description'])
    st.image(image=f'{IMAGE_PATH}{d["image"]}', width=400)


with l:
    for i in app_data[:10]:
        show_data(i)

with r:
    for i in app_data[10:]:
        show_data(i)

st.write('<hr>', unsafe_allow_html=True)
