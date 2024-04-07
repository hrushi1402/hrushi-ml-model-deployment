import streamlit as st

# Sidebar for navigation
with st.sidebar:
    selected = st.selectbox('Model Prediction System',
                            ['Diamond price Prediction',
                             'Diabetes Prediction',
                             'Parkinsons Prediction'],
                            index=0,
                            help='Select a model for prediction')

# Main content
if selected == 'Diamond price Prediction':
    st.write("You selected Diamond price Prediction")
elif selected == 'Diabetes Prediction':
    st.write("You selected Diabetes Prediction")
elif selected == 'Parkinsons Prediction':
    st.write("You selected Parkinsons Prediction")

# Horizontal Menu
selected2 = st.radio("",
                     ["Home", "ML Models", "Portfolio"],
                     index=0)
if selected2 == "Home":
    st.write("You selected Home")
elif selected2 == "ML Models":
    st.write("You selected ML Models")
elif selected2 == "Portfolio":
    st.write("You selected Portfolio")
