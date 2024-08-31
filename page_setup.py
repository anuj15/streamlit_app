import streamlit as st

st.set_page_config(layout='wide')

# PAGE SETUP
contact_me = st.Page(page='page/contact_me.py', title='Contact Me', icon=':material/contact_mail:')
converters = st.Page(page='page/converters.py', title='Converters', icon=':material/calculate:')
happiness_index = st.Page(page='page/happiness_index.py', title='Happiness Index', icon=':material/mood:')
movie_finder = st.Page(page='page/movie_finder.py', title='Movie Finder', icon=':material/movie:', default=True)
portfolio = st.Page(page='page/portfolio.py', title='My Portfolio', icon=':material/description:')
static_company = st.Page(page='page/static_company.py', title='Static Company', icon=':material/domain:')
to_do = st.Page(page='page/to_do.py', title='TO Do App', icon=':material/lists:')
weather = st.Page(page='page/weather.py', title='Weather Forecast', icon=':material/weather_mix:')
quiz = st.Page(page='page/quiz.py', title='Quizzes', icon=':material/quiz:')
anime_finder = st.Page(page='page/anime_finder.py', title='Anime Finder', icon=':material/movie:')

# NAVIGATION SETUP [WITHOUT SECTIONS]
# pg = st.navigation(
#     page=[portfolio, to_do, static_company, movie_finder, happiness_index, converters, weather, contact_me])

# NAVIGATION SETUP [WITH SECTIONS]
pg = st.navigation(
    {
        'Entertainment': [movie_finder, anime_finder],
        'Apps': [to_do, static_company, happiness_index, weather, quiz],
        'Info': [portfolio, contact_me],
    }
)

# SHARED ACROSS PAGES
st.sidebar.text(body='©️ by Anuj Gupta')

pg.run()
