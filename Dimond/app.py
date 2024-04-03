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
def preprocess_data(carat, cut, color, clarity, depth, table, price, x, y, z):
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
       # 'price': [price],
        'x': [x],
        'y': [y],
        'z': [z]
    })
    
    return data

# Main Streamlit app
def main():
    st.title("Diamond Price Predictor")
    
    # Input form for user to input data
    carat = st.number_input("Carat")
    cut = st.selectbox("Cut", ["Ideal", "Premium", "Very Good", "Good", "Fair"])
    color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
    clarity = st.selectbox("Clarity", ["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "I1"])
    depth = st.number_input("Depth")
    table = st.number_input("Table")
    price = st.number_input("price")
    x = st.number_input("x")
    y = st.number_input("y")
    z = st.number_input("z")
    
    # Preprocess input data
    data = preprocess_data(carat, cut, color, clarity, depth, table, price, x, y, z)
    
    # Make predictions using the model
    prediction = model.predict(data)
    
    # Display the prediction to the user
    st.subheader("Prediction")
    st.write("Predicted price:", prediction[0])

if __name__ == "__main__":
    main()
