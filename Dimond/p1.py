import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu", ['Diamond price Prediction',
                             'Diabetes Prediction',
                             'Parkinsons Prediction'], 
         default_index=1)
    selected


# horizontal Menu
selected2 = option_menu(None, ["Home", "ML Models", "Portfolio"], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2

# sidebar for navigation
with st.sidebar:
    selected = st.selectbox('Model Prediction System',
                            ['Diamond price Prediction',
                             'Diabetes Prediction',
                             'Parkinsons Prediction'],
                            index=0,
                            help='Select a model for prediction')
