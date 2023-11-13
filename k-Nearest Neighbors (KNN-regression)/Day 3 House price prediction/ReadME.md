<h1 align="center">Housing Price Prediction Project 🏡💰</h1>

Welcome to the Housing Price Prediction project! This project focuses on predicting housing prices based on various features such as location, demographics, and economic factors.

## Project Scope 🌐

### Objectives:
- Develop a predictive model to estimate housing prices using K-Nearest Neighbors regression.
- Utilize feature engineering techniques to enhance model performance.
- Evaluate the model's accuracy, mean absolute error, and mean squared error.

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

This project aims to predict housing prices based on a dataset containing various attributes such as longitude, latitude, housing median age, and more. The primary focus is on utilizing K-Nearest Neighbors regression for accurate predictions.

## Dataset Overview 📊

- Dataset: Housing Price Dataset
- Attributes:
  - **Longitude:** Geographic location of the house.
  - **Latitude:** Geographic location of the house.
  - **Housing Median Age:** Median age of houses in the area.
  - **Total Rooms:** Total number of rooms in the house.
  - **Total Bedrooms:** Total number of bedrooms in the house.
  - **Population:** Population in the area.
  - **Households:** Number of households in the area.
  - **Median Income:** Median income of residents.
  - **Median House Value:** Median value of houses in the area (target variable).
  - **Ocean Proximity:** Proximity of the house to the ocean.

## Project Overview

### Libraries Used 📚
- pandas 🐼
- matplotlib 📊
- seaborn 🌈
- scikit-learn 🧠
- numpy 📊

## Exploratory Data Analysis 📈

Explore the dataset, visualize correlations, and understand the distribution of target variables.

## Data Preprocessing 🛠️

Handle missing values, drop unnecessary columns, and preprocess data for model training.

## Model Training 🤖

Train a K-Nearest Neighbors regression model using a pipeline that includes feature scaling.

## Model Evaluation 📊

- **R-squared (R2) Score:** 0.86
- **Mean Absolute Error (MAE):** 0.12
- **Mean Squared Error (MSE):** 0.03

## Feature Engineering 🧠

Explore feature engineering by introducing the log-transformed median house value.

## Saving the Model 💾

Save the trained model using pickle for future use.

## Conclusion 🏁

In conclusion, the Housing Price Prediction project successfully utilized K-Nearest Neighbors regression to estimate housing prices. The model achieved commendable performance with an R-squared score of 0.86, MAE of 0.12, and MSE of 0.03.

### Final Thoughts:
- Feature engineering, such as log-transforming the target variable, contributed to improved model accuracy.
- Continuous monitoring and updates with new housing data can further enhance the model's predictive capabilities.
- The Streamlit app provides an accessible interface for users to estimate housing prices based on their input.

This project serves as a foundational step in leveraging machine learning for housing price prediction, with opportunities for ongoing improvement and application in real-world scenarios. 🏡💰

## Questions and Concepts 🤔💡

1. **Explain the k-Nearest Neighbors algorithm and its underlying principle.**

2. **What is the significance of the 'k' parameter in KNN, and how does it impact the algorithm's performance?**

3. **Describe the distance metrics commonly used in KNN and their characteristics. How does the choice of distance metric influence the algorithm?**

4. **Explain the concept of the decision boundary in KNN. How is it determined, and what role does it play in classification?**

5. **Discuss the trade-off between a small and large value of 'k' in KNN. How does each choice affect the model's bias and variance?**

6. **How does KNN handle categorical features? Are there any specific considerations or techniques for dealing with non-numeric attributes?**

7. **What are the challenges or limitations of the KNN algorithm, and how can these challenges be mitigated?**

8. **Explain the concept of feature scaling in the context of KNN. Why is it important, and how does it impact the algorithm's performance?**

9. **Discuss strategies for selecting an optimal value for 'k' in KNN. Are there any common techniques or heuristics used for this purpose?**

10. **In what scenarios would you recommend using KNN as a machine learning algorithm? Are there specific types of datasets or problems where KNN excels or struggles?**

## Contributing
If you'd like to contribute to this project, feel free to create a pull request or open an issue.

## License
This project is licensed under the Apache License 2.0 License.