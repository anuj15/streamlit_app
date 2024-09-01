import streamlit as st

st.set_page_config(layout='wide')

# PAGE SETUP
movie_finder = st.Page(page='page/movie_finder.py', title='Movie Finder', icon=':material/movie:', default=True)
anime_finder = st.Page(page='page/anime_finder.py', title='Anime Finder', icon=':material/movie:')

to_do = st.Page(page='page/to_do.py', title='TO Do App', icon=':material/lists:')
static_company = st.Page(page='page/static_company.py', title='Static Company', icon=':material/domain:')
happiness_index = st.Page(page='page/happiness_index.py', title='Happiness Index', icon=':material/mood:')
weather = st.Page(page='page/weather.py', title='Weather Forecast', icon=':material/weather_mix:')
quiz = st.Page(page='page/quiz.py', title='Quizzes', icon=':material/quiz:')

portfolio = st.Page(page='page/portfolio.py', title='My Portfolio', icon=':material/description:')
contact_me = st.Page(page='page/contact_me.py', title='Contact Me', icon=':material/contact_mail:')

# NAVIGATION SETUP [WITHOUT SECTIONS]
# pg = st.navigation(
#     page=[portfolio, to_do, static_company, movie_finder, happiness_index, weather, contact_me]
#     )

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
