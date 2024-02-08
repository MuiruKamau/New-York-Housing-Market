# New York Housing Market Regression Analysis

## Overview
This project focuses on predicting the prices of houses in New York using various characteristics, including the number of bedrooms, bathrooms, and the square footage of the property. By conducting exploratory data analysis (EDA) and applying linear regression modeling, we aim to uncover the key factors influencing house prices in New York. Our goal is to develop a predictive model capable of estimating house prices based on these determinants.

## Dataset Description
The dataset for this project comprises information about real estate listings in New York, featuring the following attributes:

- **BROKERTITLE**: The title of the broker.
- **TYPE**: The type of property (e.g., Condo, House, Townhouse).
- **PRICE**: The listing price of the property.
- **BEDS**: The number of bedrooms.
- **BATH**: The number of bathrooms.
- **PROPERTYSQFT**: The property's square footage.
- **ADDRESS, STATE**: Details of the location.
- **LATITUDE, LONGITUDE**: The geographical coordinates.

## Methodology

### Exploratory Data Analysis (EDA)
Initially, the dataset was scrutinized to grasp its structure and contents thoroughly. We analyzed summary statistics and distributions for crucial variables such as PRICE, BEDS, BATH, and PROPERTYSQFT, identifying trends and outliers. Data cleaning was performed to address any missing or anomalous values, although no missing values were discovered in the variables selected for analysis.

### Linear Regression Modeling
Preparations for modeling included a logarithmic transformation of the PRICE variable to correct its skewed distribution. The dataset was divided into training (80%) and testing (20%) sets to evaluate the model's performance on unseen data. A linear regression model was then developed using BEDS, BATH, and PROPERTYSQFT as predictors. We assessed the model's accuracy using the R-squared and RMSE (Root Mean Square Error) metrics on the test set.

## Results
The linear regression model achieved an R-squared value of 0.45, indicating that about 45% of the variability in house prices can be explained by the model. The RMSE, calculated on the logarithmic scale, was 0.71, which implies that the model's predictions were within a factor of exp(0.71) of the actual price values.

## Conclusion and Recommendations
The developed model serves as a foundational tool for predicting house prices in New York, illustrating the complex nature of real estate pricing influenced by numerous factors beyond the basic features analyzed here. For enhanced precision, subsequent research could incorporate additional variables, such as property age, specific location attributes (e.g., neighborhood desirability), and amenities. Advanced modeling approaches, including polynomial regression and machine learning algorithms, might provide superior predictive capability.

## How to Run the Project
- Ensure Python and the required libraries (pandas, sklearn, numpy, matplotlib) are installed.
- Execute the Jupyter notebook or Python script that contains the EDA and linear regression analysis.
- Modify the analysis and model training sections as necessary to investigate different features or models.
