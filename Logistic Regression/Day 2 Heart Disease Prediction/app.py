# run : streamlit run app.py 

import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open(r'saved_model\Heart_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Define a function to preprocess input data
def preprocess_input(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'cp': [cp],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg': [restecg],
        'thalach': [thalach],
        'exang': [exang],
        'oldpeak': [oldpeak],
        'slope': [slope],
        'ca': [ca],
        'thal': [thal]
    })
    
    return data

# Create a Streamlit app
def main():
    st.title('Heart Disease Prediction App')

    # Collect user inputs
    age = st.slider('Age', min_value=29, max_value=77, value=50)
    sex = st.selectbox('Sex', [0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
    cp = st.slider('Chest Pain Type (cp)', min_value=0, max_value=3, value=1)
    trestbps = st.slider('Resting Blood Pressure(trestbps)', min_value=94, max_value=200, value=120)
    chol = st.slider('Cholesterol(chol)', min_value=126, max_value=564, value=200)
    fbs = st.selectbox('Fasting Blood Sugar(fbs)', [0, 1], format_func=lambda x: 'True' if x == 1 else 'False')
    restecg = st.slider('Resting Electrocardiographic Results(restecg)', min_value=0, max_value=2, value=1)
    thalach = st.slider('Maximum Heart Rate Achieved(thalach)', min_value=71, max_value=202, value=150)
    exang = st.selectbox('Exercise Induced Angina(exang)', [0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    oldpeak = st.slider('ST Depression Induced by Exercise(oldpeak)', min_value=0.0, max_value=6.2, value=1.0)
    slope = st.slider('Slope of the Peak Exercise ST Segment(slope)', min_value=0, max_value=2, value=1)
    ca = st.slider('Number of Major Vessels Colored by Fluoroscopy(ca)', min_value=0, max_value=3, value=1)
    thal = st.slider('Thalassemia(thal)', min_value=0, max_value=3, value=1)

    # Preprocess user inputs
    input_data = preprocess_input(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)

    # Make predictions
    prediction = loaded_model.predict(input_data)

    # Display the result
    if st.button('Predict'):
        st.subheader('Prediction:')
        if prediction[0] == 1:
            st.success('High probability of heart disease.')
        else:
            st.success('Low probability of heart disease.')

# Run the Streamlit app
if __name__ == '__main__':
    main()
