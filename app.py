
from calendar import month
import streamlit as st
import pandas as pd
import pickle
import numpy as np
import plotly.express as px
import sklearn 

st.title('Quantity chip')
from PIL import Image
image = Image.open('chip.png')
st.image(image, caption='chip')




st.title('The app uses the real inputs to predict the quantity store_id')



# Add a heading for input features
st.subheader('Enter  Features for Predictions')

 # Rwquest for input fatures, but replod with some default values
product= st.number_input('product_id', 1.0)

st.write(' The product id is :', product)

location= st.number_input('location_id', 1.0)

st.write('The location_id is:', location)

price= st.number_input('unit_price', 1.0)

st.write('The price is :', price)


year= st.number_input('year', 1.0)


st.write('The year is', year)


month= st.number_input('month', 1.0)


st.write('The month is', month)


day= st.number_input('day', 1.0)

st.write('The day is', day)


hour= st.number_input('hour', 1.0)


st.write('The hour is', hour)




# Load  the model from disk


if st.button("Predict"):
    pickle_in = open('model2.pkl', 'rb')
    model = pickle.load(pickle_in)
    predict=model.predict([[product,location,price,year,month,day,hour]])
  

    st.text(f"""
     The predicted items  is :  {predict[0]} 
    """)    # Get the input features
    # run predictions







