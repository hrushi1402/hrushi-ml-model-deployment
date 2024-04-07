import streamlit as st
import webbrowser

# Function to open portfolio website
def open_portfolio():
    webbrowser.open_new_tab("https://hrushikesh1402.dorik.io/")

# Sidebar for navigation
with st.sidebar:
    selected = st.selectbox('Model Prediction System',
                            ['Diamond price Prediction',
                             'Diabetes Prediction',
                             'Parkinsons Prediction'],
                            index=0,
                            help='Select a model for prediction')



# Horizontal Menu with custom CSS
col1, col2, col3 = st.columns(3)

if col1.button("Home", key='home_button'):
    st.write("You clicked Home")
elif col2.button("ML Models", key='ml_models_button'):
    st.write("You clicked ML Models")
    # Main content
    if selected == 'Diamond price Prediction':
        st.write("You selected Diamond price Prediction")
    elif selected == 'Diabetes Prediction':
        st.write("You selected Diabetes Prediction")
    elif selected == 'Parkinsons Prediction':
        st.write("You selected Parkinsons Prediction")



elif col3.button("Portfolio", key='portfolio_button'):
    st.write("You clicked Portfolio")
    open_portfolio()

# Apply custom CSS for button styling
st.markdown("""
    <style>
        .stButton>button {
            background-color: #ff8c00; /* Orange */
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)
