import pandas as pd
import streamlit as st
import plotly.express as px

FILE = 'data/happiness.csv'
TITLE = 'Happiness Index'
raw_data = pd.read_csv(filepath_or_buffer=FILE)
columns = raw_data.columns
columns = [x.title().replace('_', ' ') for x in columns]
st.write(f'<h1 style=text-align:center>{TITLE}</h1><hr>', unsafe_allow_html=True)
st.subheader(body='In Search of Happiness', anchor=False)
st.selectbox(label='Select X-Axis', options=columns, key='x')
st.selectbox(label='Select Y-Axis', options=columns, key='y')

def get_data():
    x_data = st.session_state.x.lower().replace(' ', '_')
    xx = raw_data[x_data]
    y_data = st.session_state.y.lower().replace(' ', '_')
    yy = raw_data[y_data]
    return xx, yy

x_, y_ = get_data()

figure = px.scatter(x=x_, y=y_, labels={'x': st.session_state.x, 'y': st.session_state.y})
st.plotly_chart(figure)
