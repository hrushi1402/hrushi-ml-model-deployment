import streamlit as st
from streamlit_option_menu import option_menu

import home, trending, account, your, about

st.set_page_config(
    page_title="Pondering"
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Pondering',
                options=['Home', 'Account', 'Trending', 'Your Posts', 'about'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == "Home":
            home.app()
        elif app == "Account":
            account.app()
        elif app == "Trending":
            trending.app()
        elif app == 'Your Posts':
            your.app()
        elif app == 'about':
            about.app()

multi_app = MultiApp()
multi_app.run()
