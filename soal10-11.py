import pickle
import streamlit as st
import pandas as pd
import sklearn as sk
import os
import numpy as np
import altair as alt

model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction','Profil'])
if app_mode=='Home':
    st.title('Data Mobil')

    st.header("Dataset")

    df1 = pd.read_csv('CarPrice.csv')
    st.dataframe(df1)

    st.write("Grafik Highway-mpg")
    chart_highwaympg = pd.DataFrame(df1, columns=["highwaympg"])
    st.line_chart(chart_highwaympg)

    st.write("Grafik curbweight")
    chart_curbweight = pd.DataFrame(df1, columns=["curbweight"])
    st.line_chart(chart_curbweight)

    st.write("Grafik horsepower")
    chart_horsepower = pd.DataFrame(df1, columns=["horsepower"])
    st.line_chart(chart_horsepower)


elif app_mode=='Prediction':
    st.title('Prediksi Harga Mobil')
    highwaympg = st.number_input('Highway-mpg', 0, 10000000)
    curbweight = st.number_input('Curbweight', 0, 10000000)
    horsepower = st.number_input('Horsepower', 0, 10000000)

    if st.button('Prediksi'):
        car_prediction = model.predict([[highwaympg, curbweight, horsepower]])
        
        harga_mobil_str = np.array(car_prediction)
        harga_mobil_float = float(harga_mobil_str[0])
        
        harga_mobil_formatted = "{:,.2f}".format(harga_mobil_float)
        st.markdown(f'Harga Mobil: $ {harga_mobil_formatted}')
        

elif app_mode == 'Profil':
    st.write('App realised by : Betrant Wiprazzia M')
