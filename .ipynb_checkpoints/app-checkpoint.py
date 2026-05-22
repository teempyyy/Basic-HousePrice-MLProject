import streamlit as st
import joblib
import numpy as np

model = joblib.load(r"C:\Users\USER\OneDrive\Documents\Machine Learning\house_price_project\model\house_model.pk1")

st.title("House Price Prediction App")

overall_qual = st.slider("Overall Quality", 1, 10, 5)
gr_liv_area = st.number_input("Living Area (sqft)", 500, 5000, 1500)
garage_cars = st.slider("Garage Cars", 0, 4, 1)
total_bsmt = st.number_input("Basement Area", 0, 3000, 800)
bath = st.slider("Bathrooms", 1, 4, 2)
year_built = st.slider("Year Built", 1900, 2024, 2000)

if st.button("Predict Price"):
    input_data = np.array([[overall_qual, gr_liv_area, garage_cars,
                            total_bsmt, bath, year_built]])

    prediction = model.predict(input_data)

    st.success(f"Predicted House Price: ${int(prediction[0]):,}")