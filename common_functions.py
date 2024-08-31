from smtplib import SMTP

import requests
import streamlit as st
import urllib3

urllib3.disable_warnings()
OWM_API_KEY = st.secrets['OWM_API_KEY']
OWM_ENDPOINT = st.secrets['OWM_ENDPOINT']
SMTP_HOST = st.secrets['SMTP_HOST']
SMTP_PORT = st.secrets['SMTP_PORT']
FROM_ = st.secrets['GMAIL_USERNAME']
PASSWORD = st.secrets['GMAIL_PASSWORD']
OPEN_TRIVIA_ENDPOINT = st.secrets['OPEN_TRIVIA_ENDPOINT']
TODO_FILE = 'data/to_do.txt'


def mail(to_, msg):
    with SMTP(host=SMTP_HOST, port=SMTP_PORT) as conn:
        conn.starttls()
        conn.login(user=FROM_, password=PASSWORD)
        conn.sendmail(from_addr=FROM_, to_addrs=to_, msg=msg)


def read_file():
    with open(file=TODO_FILE) as f:
        return f.readlines()


def write_file(data):
    with open(file=TODO_FILE, mode='w') as f:
        f.writelines(data)


def get_weather_data(city):
    params = {
        'q': city,
        'appid': OWM_API_KEY,
    }
    response = requests.get(url=OWM_ENDPOINT, params=params, verify=False)
    response.raise_for_status()
    return response.json()['list']


def get_quiz_data(category, difficulty, q_type):
    try:
        url = OPEN_TRIVIA_ENDPOINT
        payload = {
            'amount': '10',
            'category': category,
            'difficulty': difficulty,
            'type': q_type,
        }
        quiz_data = requests.get(url=url, params=payload, verify=False).json()['results']
        questions = []
        answers = []
        options = []
        if quiz_data:
            for i in quiz_data:
                questions.append(i['question'])
                answers.append(i['correct_answer'])
                options.append(i['incorrect_answers'])
            for ans, opt in zip(answers, options):
                opt.append(ans)
            return questions, answers, options
        else:
            return None
    except KeyError:
        return
