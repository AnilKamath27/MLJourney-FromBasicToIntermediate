<h1 align="center">Sales Prediction Project 📈💰</h1>

## 🌐 Project Scope
The Sales Prediction Project is a data science and machine learning endeavor aimed at helping businesses forecast their future sales. Accurate sales prediction is crucial for optimizing marketing strategies, allocating resources, and maximizing revenue. In this project, we leverage various machine learning techniques to predict sales based on advertising spending across different mediums.

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
## 📊 Attributes

- 📺 **TV**: This feature represents the advertising budget spent on TV advertisements. It's the amount of money allocated to running television commercials for promoting a product or service. TV advertising can reach a wide and diverse audience.

- 📻 **Radio**: The "Radio" feature represents the advertising budget spent on radio advertisements. It refers to the amount of money allocated to air radio ads, which are typically more targeted than TV ads. Radio advertising can be effective for reaching specific demographics or local audiences.

- 📰 **Newspaper**: This feature corresponds to the advertising budget spent on newspaper advertisements. It represents the amount of money allocated to print ads in newspapers. Newspaper advertising is a traditional medium for reaching a broad audience, especially in local markets.

Now, let's look at the 🎯 target variable:

- 📈 **Sales**: "Sales" is the target variable in your dataset. It represents the actual sales achieved as a result of the advertising efforts. This is the outcome you want to predict based on the advertising budgets allocated to TV, radio, and newspaper.

## Project Overview

### Libraries Used 📚
- pandas 🐼
- matplotlib 📊
- seaborn 🌈
- scikit-learn 🧠
- statsmodels 📈
- scipy 📊
- pickle 🥒

### Data Exploration 🕵️‍♀️
- Loaded the dataset from "data\Advertising.csv"
- Removed unnecessary columns
- Checked for missing values and duplicates
- Explored dataset statistics and visualized relationships using pair plots and heatmaps

### Model Building 🛠️
- Implemented linear regression model
- Split data into training and testing sets
- Scaled features for better model performance

### Model Evaluation 📊
- Evaluated the model using metrics:
  - R-squared (R2)
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)

### Visualizations 📈
- Visualized predictions against actual values
- Examined the distribution of residuals
- Generated a probability plot of residuals

### Saving the Model 📁
- Saved the trained linear regression model using pickle

## Project Steps

1. **Data Exploration and Preprocessing 📝🔍**
   - Explored and visualized data relationships.
   - Checked for missing values and duplicates.
   - Conducted feature scaling and selection.

2. **Model Building and Evaluation 🧮🔍**
   - Implemented a Linear Regression model.
   - Split data into training and testing sets.
   - Evaluated the model using R-squared, MAE, and MSE.

3. **Visualizations 📊📈**
   - Created visualizations of predictions, residuals, and probability plots.

4. **Saving the Model 📁**
   - Utilized pickle to save the trained Linear Regression model.

## Model Evaluation 📊

- **R-squared (R2):** 86%
- **Mean Absolute Error (MAE):** 1.49
- **Mean Squared Error (MSE):** 3.73

## Conclusion 🏁

In conclusion, the Linear Regression model demonstrates a robust predictive capability, as indicated by the high R-squared value of 86%. The mean absolute error (MAE) and mean squared error (MSE) metrics further validate the model's accuracy in predicting sales based on advertising budgets.

### Final Thoughts:
- Continuous model updates with new data are recommended for improved accuracy.
- Exploring additional features or refining existing ones could enhance predictive power.
- Engaging domain experts can provide deeper insights for further model optimization.

## Questions and Concepts 🤔💡

1. **What is Linear Regression, and how does it work in the context of machine learning?** 🤖📉
2. **Can you explain the difference between Simple Linear Regression and Multiple Linear Regression?** 📊📈
3. **How do you measure the performance of a Linear Regression model?** 📏📐
4. **What is the role of the cost function in Linear Regression, and can you name a specific cost function used in this context?** 💰🎯
5. **Explain the concept of feature scaling and why it's important in Linear Regression.** 📈🔄
6. **How does Linear Regression handle multicollinearity, and why is it important to address this issue?** 🔄📊
7. **What are some common assumptions that Linear Regression makes about the data?** 🤔📊
8. **What is the purpose of the coefficients in a Linear Regression model, and how are they determined during training?** 📈🔍
9. **Can you discuss the limitations of Linear Regression as a machine learning algorithm?** 🛑📉
10. **How would you interpret the results of a Linear Regression model to a non-technical audience, such as stakeholders or clients?** 📊👥

---
## Contributing
If you'd like to contribute to this project, feel free to create a pull request or open an issue.Feel free to copy and paste this content into your ReadME.md file. Make sure to customize it to fit your project specifics and add any additional information or insights you'd like to include. Good luck with your project! 🚀🤖💼

## License
This project is licensed under the Apache License 2.0 License.
