import streamlit as st
import pandas as pd
import pickle

import os


# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load the saved model
with open(f"{working_dir}/Diamond.pkl", "rb") as f:
    model = pickle.load(f)

# Define mappings for categorical variables
cut_n = {'Ideal':1,'Premium':2,'Very Good':3,'Good':4,'Fair':5}
color_n = {'J':7,'I':6,'H':5,'G':4,'F':3,'E':2,'D':1}
clarity_n = {'I1':8,'SI2':7,'SI1':6,'VS2':5,'VS1':4,'VVS2':3,'VVS1':2,'IF':1}

# Function to preprocess input data
def preprocess_data(carat, cut, color, clarity, depth, table, x, y, z):
    # Map categorical variables to numerical values
    cut_encoded = cut_n.get(cut, 0)  # Use 0 as default value if cut not found
    color_encoded = color_n.get(color, 0)  # Use 0 as default value if color not found
    clarity_encoded = clarity_n.get(clarity, 0)  # Use 0 as default value if clarity not found
    
    # Create DataFrame with preprocessed data
    data = pd.DataFrame({
        'carat': [carat],
        'cut': [cut_encoded],
        'color': [color_encoded],
        'clarity': [clarity_encoded],
        'depth': [depth],
        'table': [table],
        'x': [x],
        'y': [y],
        'z': [z]
    })
    
    return data



# Set page configuration
st.set_page_config(page_title="Predictor",
                   
                   page_icon="💍")

# Add CSS for background image
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://drive.google.com/file/d/1fzZKZzg5tw4CyVJZpvP4gVluZwHGMgSL/view?usp=drive_link") no-repeat center center fixed;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# sidebar for navigation
with st.sidebar:
    selected = st.selectbox('Model Prediction System',
                            ['Diamond price Prediction',
                             'Diabetes Prediction',
                             'Parkinsons Prediction'],
                            index=0,
                            help='Select a model for prediction')


if selected == 'Diamond price Prediction':

    # page title
    st.title('Diamond price Prediction using ML')
    # Creating buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        carat = st.text_input('Carat')
        color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
        table = st.number_input("Table")

    with col2:
        cut = st.selectbox("Cut", ["Ideal", "Premium", "Very Good", "Good", "Fair"])
        clarity = st.selectbox("Clarity", ["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "I1"])
        depth = st.number_input("Depth")

    with col3:
        x = st.number_input("x")
        y = st.number_input("y")
        z = st.text_input("z")


    if st.button('Predict Diamond Price'):
        # Preprocess input data
        data = preprocess_data(carat, cut, color, clarity, depth, table, x, y, z)
        
        # Convert DataFrame to 2D array
        data_array = data.values
        
        # Make predictions using the model
        prediction = model.predict(data_array)
        
        # Display the prediction to the user
        st.subheader("Prediction")
        st.write("Predicted price:", prediction[0])

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
# Footer
st.markdown('---')
st.write('Made with ❤️ by Hrushikesh Gadade')
