import streamlit as st
import plotly.express as px
from common_functions import get_weather_data

TITLE = 'Weather Forecast'
IMAGES = 'images/weather/'
st.write(f'<h1 style=text-align:center>{TITLE}</h1><hr>', unsafe_allow_html=True)
st.text_input(label='Place', key='input', help='Enter city name to get the forecast')
st.slider(label='Forecast Days', min_value=1, max_value=5, key='slider',
          help='Select for how many days you want to see the forecast')
st.selectbox(label='Select data to view', options=['Temperature', 'Weather'], key='selection')
place = st.session_state.input
days = st.session_state.slider
view = st.session_state.selection
if place:
    st.subheader(f'{view} for next {days} day(s) in {place.title()}', anchor=False)
    try:
        data = get_weather_data(place)
        data = data[8 * days]
        if view == 'Temperature':
            temp = [x['main']['temp'] / 10 for x in data]
            dates = [x['dt_txt'] for x in data]
            figure = px.line(x=dates, y=temp, labels={'x': 'Date', 'y': 'Temperature (c)'}, title='Temperature vs Date')
            st.plotly_chart(figure_or_data=figure)
            st.balloons()
        else:
            sky_conditions = [x['weather'][0]['main'] for x in data]
            paths = []
            for condition in sky_conditions:
                paths.append(f'{IMAGES}{condition.lower()}.png')
            st.image(image=paths, width=90)
            st.balloons()
    except KeyError:
        st.write('This place does not exist')
