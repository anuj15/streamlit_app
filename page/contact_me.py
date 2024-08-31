import re

from common_functions import mail
import streamlit as st


def email():
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    msg = st.session_state.message
    to_email = st.session_state.to_email

    if not re.match(regex, to_email):
        st.error('Please enter a valid email')
        return

    if not msg.strip():
        st.error('Message cannot be empty.')
        return

    msg = f'subject:Mail from StreamLit Portfolio App\n{msg}'
    mail(to_email, msg)
    st.success(body='Your email was sent successfully.')


TITLE = 'Contact Me'
st.write(f'<h1 style=text-align:center>{TITLE}</h1>', unsafe_allow_html=True)

with st.form(key='send_mail'):
    st.text_input(label='Your Email Address', key='to_email', placeholder='Enter your email here...')
    st.text_area(label='Your message', key='message', placeholder='Enter your message here...')
    st.form_submit_button(label='Submit', on_click=email)
