
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import sklearn 
import pickle

st.title('Real Time order prediction')
from PIL import Image
image = Image.open('crmb.png')
st.image(image, caption='crmb')




st.title('The app uses the real inputs to predict the quantity of cookies in each location')


# Add a heading for input features
st.subheader('Enter  Features for Predictions')



 # Rwquest for input fatures, but replod with some default values
location= st.number_input('location', 7)

st.write(' The location is :', location)

product= st.number_input('product_id', 1.0)

st.write('The product id is:', product)

price= st.number_input('unit_price', 1.0)

st.write('The price is :', price)


day= st.number_input('day', 1.0)

st.write('The day is', day)


year= st.number_input('year', 1.0)

st.write('The year is', year)


month= st.number_input('month', 1.0)


st.write('The month is', month)

hour= st.number_input('hour', 1.0)


st.write('The hour is', hour)




# Load  the model from disk


if st.button("Predict"):
    
    pickle_in = open('finalized_model.pkl', 'rb')
    model = pickle.load(pickle_in)
    predict=model.predict([[location,product,price,day,year,month,hour]])
     

    st.text(f"""
     The predicted items  is :  {predict[0]} 
    """)    # Get the input features
    # run predictions









