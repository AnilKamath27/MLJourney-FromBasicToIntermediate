<h1 align="center">Heart Disease Prediction Project 🩺❤️</h1>

Welcome to the Heart Disease Prediction project! This project focuses on predicting heart disease based on various health attributes.

## Project Scope 🌐

### Objectives:
- Develop a predictive model to assess the likelihood of heart disease based on health-related attributes.
- Utilize logistic regression for efficient and interpretable predictions.
- Evaluate the model's performance using various metrics, including accuracy, precision, recall, and F1 score.

## Getting Started

To get started with this project, you will need to have Python and the required libraries installed. You can install the necessary packages using pip:
```
pip install -r requirements.txt
```
Clone this repository to your local machine:
```
git clone https://github.com/AnilKamath27/MLJourney-FromBasicToIntermediate.git
```
---
## Introduction 🚀

This project aims to predict the likelihood of heart disease based on health-related attributes using logistic regression.

## Dataset Overview 📊

- Dataset: Heart Disease Dataset
- Attributes:
  - **Age:** Age of the individual.
  - **Sex:** Gender of the individual (0 = Female, 1 = Male).
  - **Chest Pain Type (cp):** Type of chest pain experienced.
  - **Resting Blood Pressure (trestbps):** Resting blood pressure in mm Hg.
  - **Cholesterol (chol):** Serum cholesterol level in mg/dl.
  - **Fasting Blood Sugar (fbs):** Fasting blood sugar > 120 mg/dl (1 = True, 0 = False).
  - **Resting Electrocardiographic Results (restecg):** Resting electrocardiographic results.
  - **Maximum Heart Rate Achieved (thalach):** Maximum heart rate achieved.
  - **Exercise Induced Angina (exang):** Exercise-induced angina (1 = Yes, 0 = No).
  - **ST Depression Induced by Exercise (oldpeak):** ST depression induced by exercise.
  - **Slope of the Peak Exercise ST Segment (slope):** Slope of the peak exercise ST segment.
  - **Number of Major Vessels Colored by Fluoroscopy (ca):** Number of major vessels colored by fluoroscopy.
  - **Thalassemia (thal):** Thalassemia.

## Project Overview

### Libraries Used 📚
- pandas 🐼
- matplotlib 📊
- seaborn 🌈
- scikit-learn 🧠
- statsmodels 📈
- scipy 📊
- pickle 🥒
## Exploratory Data Analysis 📈

Explore the dataset, visualize correlations, and understand the distribution of target variables.

## Data Preprocessing 🛠️

Handle missing values, duplicates, and preprocess data for model training.

## Model Training 🤖

Train a logistic regression model using a pipeline that includes feature scaling.

## Model Evaluation 📊

- **Accuracy Score:** 0.84
- **Precision Score:** 0.87
- **Recall Score:** 0.81
- **F1 Score:** 0.84

## Feature Importance 🧠

Explore feature importance using logistic regression coefficients.

## Saving the Model 💾

Save the trained model using pickle for future use.

## Running the Streamlit App 🌐

Create an interactive Streamlit app for users to predict heart disease based on input features.

## Conclusion 🏁

In conclusion, the Heart Disease Prediction project successfully utilized logistic regression to assess the likelihood of heart disease based on various health attributes. The model achieved commendable performance with an accuracy score of 0.84, precision score of 0.87, recall score of 0.81, and an F1 score of 0.84.

### Final Thoughts:
- The logistic regression model, incorporating features such as age, gender, chest pain type, and more, proves effective in predicting heart disease.
- Continuous monitoring and updates with new health data can further enhance the model's predictive capabilities.
- Exploring additional health-related features and collaborating with medical experts may offer valuable insights for model refinement.

This project serves as a foundational step in leveraging machine learning for heart disease prediction, with opportunities for ongoing improvement and application in real-world healthcare scenarios. 🩺❤️

## Questions and Concepts 🤔💡
1. What distinguishes logistic regression from linear regression, and why is it suitable for binary classification problems? 🤔

2. Can you elaborate on the significance of logistic regression coefficients and how they contribute to the model's predictions? 📊

3. Why is the sigmoid function used in logistic regression, and how does it transform linear predictions into probabilities? 🔄

4. Briefly explain the concept of maximum likelihood estimation (MLE) and its role in training logistic regression models. 🎯

5. In logistic regression, what does the odds ratio represent, and how is it computed? 📈

6. What is the purpose of a decision boundary in logistic regression, and how does it impact the classification of data points? 🚧

7. How does multicollinearity affect logistic regression, and what methods can be employed to address this issue? 🔄

8. Discuss the potential risk of overfitting in logistic regression and how regularization techniques like L1 and L2 regularization can help prevent it. 🛡️

9. What is the ROC curve, and how is it utilized to assess the performance of a logistic regression model? 📉

10. Can you outline the key assumptions associated with logistic regression and describe the potential consequences if these assumptions are violated? 🤔
---
## Contributing
If you'd like to contribute to this project, feel free to create a pull request or open an issue.Feel free to copy and paste this content into your ReadME.md file. Make sure to customize it to fit your project specifics and add any additional information or insights you'd like to include. Good luck with your project! 🚀🤖💼

## License
This project is licensed under the Apache License 2.0 License.
