import streamlit as st
import pandas as pd

content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna 
aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
EMP_DATA = 'data/emp_info.csv'
IMAGE_PATH = 'images/company/'

emp_data = pd.read_csv(EMP_DATA).to_dict(orient='records')
TITLE = 'Company Profile'
st.write(f'<h1 style=text-align:center>{TITLE}</h1><hr>', unsafe_allow_html=True)
st.write(content)
st.subheader(body='Meet the Team', anchor=False)
l, m, r = st.columns(spec=3, gap='small', vertical_alignment='center')


def show_data(info):
    name = info['first name'].title() + ' ' + info['last name'].title()
    pic = IMAGE_PATH + info['image']
    st.subheader(body=name, anchor=False)
    st.write(info['role'])
    st.image(pic)
    st.write('<hr>', unsafe_allow_html=True)


with l:
    for i in emp_data[:4]:
        show_data(i)

with m:
    for i in emp_data[4:8]:
        show_data(i)

with r:
    for i in emp_data[8:]:
        show_data(i)
