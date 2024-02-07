New York House Price Prediction
Overview
This project aims to predict the prices of houses in New York using various features such as the number of bedrooms, bathrooms, and property square footage. Through exploratory data analysis (EDA) and linear regression modeling, we seek to understand the factors that most influence house prices in New York and develop a predictive model to estimate house prices based on those factors.

Dataset Description
The dataset used in this project contains information about real estate listings in New York, including:

BROKERTITLE: Broker's title.
TYPE: The type of property (e.g., Condo, House, Townhouse).
PRICE: Listing price of the property.
BEDS: Number of bedrooms.
BATH: Number of bathrooms.
PROPERTYSQFT: Square footage of the property.
ADDRESS, STATE: Location details.
LATITUDE, LONGITUDE: Geographical coordinates.
Methodology
Exploratory Data Analysis (EDA)
The dataset was first examined to understand its structure and contents.
Summary statistics and distributions of key variables (PRICE, BEDS, BATH, PROPERTYSQFT) were analyzed to identify trends and outliers.
Data cleaning steps were undertaken to handle any missing or anomalous values, though no missing values were found in the selected variables for analysis.
Linear Regression Modeling
The dataset was prepared for modeling, including a logarithmic transformation of the PRICE variable to address its skewed distribution.
The data was split into training (80%) and testing (20%) sets to ensure the model's performance could be evaluated on unseen data.
A linear regression model was trained using BEDS, BATH, and PROPERTYSQFT as predictor variables.
The model's performance was evaluated using R-squared and RMSE metrics on the testing set.
Results
The linear regression model yielded an R-squared value of 0.45, indicating that approximately 45% of the variability in house prices could be explained by the model.
The RMSE value was 0.71 (on the logarithmic scale), suggesting that the model's predictions were within a factor of exp(0.71) of the actual price values.
Conclusion and Recommendations
The model provides a baseline for predicting house prices in New York but also highlights the complexity of real estate pricing, which is influenced by many factors beyond the basic features included in this analysis.
For improved accuracy, future work could explore including additional features such as property age, location specifics (e.g., neighborhood desirability), and amenities.
Advanced modeling techniques, including polynomial regression and machine learning algorithms, may offer better predictive performance.
How to Run the Project
Ensure you have Python and the necessary libraries (pandas, sklearn, numpy, matplotlib) installed.
Run the Jupyter notebook or Python script containing the EDA and linear regression analysis.
Customize the analysis and model training sections as needed to explore different features or models.
