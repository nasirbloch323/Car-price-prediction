import pandas as pd
import numpy as np
import pickle
import streamlit as st

model = pickle.load(open("3. Model/pipeline.pkl", "rb"))
df  = pickle.load(open("1. Dataset/dataset.pkl", "rb"))

st.set_page_config(page_title="Car Price Prediction", page_icon="Money.png")
st.title("Cars Price Prediction")

# input fields
# Brand 
brand = st.selectbox("Select a Brand:", np.sort(df["Make"].unique()))
brand_df = df[df["Make"]==brand]
# Model
brand_model = st.selectbox(f"Select a Model of {brand}:", np.sort(brand_df["Model"].unique()))
# Year
year = st.selectbox("Year of Purchase:", np.sort(df["Year"].unique()))
# Km's drive
# km_driven = st.selectbox("Kile-meters Driven:", df["KM's driven"].unique())
km_driven = st.number_input("Kile-meter Driven:", min_value=1, max_value=500000)
# Fuel
fuel = st.selectbox("Fuel Type:", df["Fuel"].unique())
# Car Documents
car_documents = st.selectbox("Car Documents:", df["Car documents"].unique())
# Assembly
assembly = st.selectbox("Assembly:", df["Assembly"].unique())
# Transmission
transmission = st.selectbox("Transmission:", df["Transmission"].unique())


if st.button("Predict Price"):
    # create dataframe
    predict_ = pd.DataFrame({
        "Make": [brand],
        "Model":[brand_model],
        "Year":[year],
        "KM's driven":[km_driven],
        "Fuel":[fuel],
        "Car documents":[car_documents],
        "Assembly":[assembly],
        "Transmission":[transmission],
    })


    # create new column of years range
    bins = [1999,2004,2008,2012,2016,2020,2024]
    labels = [1,2,3,4,5,6]
    predict_["Year_Range"] = pd.cut(df["Year"], bins=bins, labels=labels)

    # create new column of km driven range
    bins = [0,30000,60000,90000,120000,150000,180000,210000,224000,227000,300000,330000,360000,390000,410000,440000,470000,500000,533530]
    labels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    predict_["KM's driven_Range"] = pd.cut(df["KM's driven"], bins=bins, labels=labels)
    
    # Predict Price
    predicted_price = model.predict(predict_)

    # Displaying the predicted price
    st.subheader(f"PKR Rs./ {int(predicted_price)}")
