# streamlit run streamlit_app.py to run

import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
from sklearn.preprocessing import StandardScaler

with open(r'saved_model\Sales_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

df = pd.read_csv('data/Advertising.csv')
df.drop(columns=['Unnamed: 0'], axis=1, inplace=True)

def predict_sales(tv, radio, newspaper):
    input_data = pd.DataFrame({'TV': [tv], 'Radio': [radio], 'Newspaper': [newspaper]})
    ss = StandardScaler()
    ss.fit(df[['TV', 'Radio', 'Newspaper']])
    input_data_scaled = ss.transform(input_data)
    prediction = model.predict(input_data_scaled)
    return prediction[0]

st.title('Sales Prediction App 📈💰')

st.write("This app predicts sales based on advertising budgets for TV, Radio, and Newspaper.")

tv_budget = st.slider('TV Advertising Budget', 0, 300, 150)
radio_budget = st.slider('Radio Advertising Budget', 0, 50, 25)
newspaper_budget = st.slider('Newspaper Advertising Budget', 0, 100, 50)

if st.button('Predict'):
    predicted_sales = predict_sales(tv_budget, radio_budget, newspaper_budget)
    st.write(f'Predicted Sales: ${predicted_sales:.2f}')

st.header('Interactive Bar Chart 📊')

advertising_budgets = [tv_budget, radio_budget, newspaper_budget]
fig_advertising_budgets = px.bar(
    x=['TV', 'Radio', 'Newspaper'], y=advertising_budgets,
    labels={'y': 'Budget Amount'},
    title='Advertising Budgets')

st.plotly_chart(fig_advertising_budgets)