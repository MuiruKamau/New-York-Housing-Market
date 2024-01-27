import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('New York Housing Prices EDA')


st.markdown("""
This app performs simple EDA for New York Housing Prices
* **Python libraries:** pandas, numpy, streamlit, matplotlib, seaborn
* **Data source:** [Kaggle](https://www.kaggle.com/datasets/nelgiriyewithana/new-york-housing-market)

""")

# Load the data
df = pd.read_csv('NY-House-Dataset.csv')


# Display the data
st.subheader('NYC Property Prices')
st.write(df.head(10))

# Display the descriptive statistics
st.subheader('Descriptive Statistics')
st.write(df.describe())

#check for duplicates and drop them it should not appear on the streamlit app
duplicate = df[df.duplicated()]
df = df.drop_duplicates()

# Analyze the distribution of the PRICE
st.subheader('Distribution of Price')
plt.figure(figsize=(10,6))
sns.histplot(df['PRICE'], bins=100, kde=True)
plt.title("Distribution of Price")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.xscale('log') # using log scale due to wide range of prices
st.pyplot(plt) # Display the plot on the app

with st.expander("See explanation"):   
    st.write("""The distribution of price is right skewed.

This means that most of the houses are in the lower price range.

There are very few houses in the higher price range.

The distribution of price is not normal.

""")


# Identifying the outliers
plt.figure(figsize=(10,6))
sns.boxplot(x=df['PRICE'])
plt.title("Boxplot of House Price")
plt.xlabel("Price")
plt.xscale('log')  # using log scale due to wide range of prices
plt.ylabel("Frequency")
st.pyplot(plt)  # Display the plot on the app

with st.expander("See explanation"):   
    st.write("""The boxplot shows that there are many outliers in the price variable.

The outliers are the houses with very high prices.

The boxplot also shows that there are some houses with very low prices.

On this case the outliers will be removed from the data.

""")

# Removing the outliers
# Removing the top 1% of the data
q = df['PRICE'].quantile(0.99)
df = df[df['PRICE'] < q]

#Property size analysis
#Exploring the relationship between the price and the size of the property

st.subheader('Exploring the relationship between the price and the size of the property')

plt.figure(figsize=(10,6))
sns.scatterplot(x=df['PROPERTYSQFT'], y=df['PRICE'])
plt.title("Price vs Property Size")
plt.xlabel("Property Size")
plt.ylabel("Price")
plt.xscale('log')  # using log scale due to wide range of prices
plt.yscale('log')  # using log scale due to wide range of prices
st.pyplot(plt)  # Display the plot on the app

with st.expander("See explanation"):
    st.write("""The scatter plot shows that there is a positive correlation between the price and the size of the property.

The scatter plot also shows that there are some outliers in the data.

The outliers are the houses with very high prices and very large sizes.

The scattter plot is not linear. This means that the relationship between the price and the size of the property is not linear.

""")

#calculating the correlation between the price and the size of the property
st.subheader('Correlation between the price and the size of the property')
correlation = df['PRICE'].corr(df['PROPERTYSQFT'])
st.write(f"Correlation: {correlation}")

with st.expander("See explanation"):
    st.write("""The correlation between the price and the size of the property is 0.44.

This shows that there is a positive correlation between the price and the size of the property.

This means that as the size of the property increases, the price also increases.

The correlation is not very strong this means that the size of the property is not a very good predictor of the price

""")

st.subheader("Price based on locality")
# Plotting the top 10 localities by average price

plt.figure(figsize=(10,6))
df.groupby('LOCALITY')['PRICE'].mean().sort_values(ascending=False).head(10).plot(kind='bar')
plt.title("Top 10 Localities by Average Price")
plt.xlabel("Locality")
plt.ylabel("Average Price")
plt.yscale('log')  # using log scale due to wide range of prices
#plt.xticks(rotation=45)
st.pyplot(plt)  # Display the plot on the app

with st.expander("See explanation"):   
    st.write(""" The bar chart shows that the most expensive locality is New York County.

The bar chart also shows that the least expensive locality is the Bronx.  

""")

st.subheader("Price based on number of bedrooms")

plt.figure(figsize=(10,6))
df.groupby('BEDS')['PRICE'].mean().plot(kind='bar')
plt.title("Average Price by Number of Bedrooms")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Average Price")
plt.xticks(rotation=0) 
st.pyplot(plt)  # Display the plot on the app

with st.expander("See explanation"):   
    st.write(""" The bar chart illustrates a general upward trend in average prices with an increase in the number of bedrooms.

However, there is some fluctuation in this trend, particularly for properties with a very high number of bedrooms
    
    """)

#plotting the average price by number of bathrooms
st.subheader("Price based on number of bathrooms")

plt.figure(figsize=(10,6))
df.groupby('BATH')['PRICE'].mean().plot(kind='bar')
plt.title("Average Price by Number of Bathrooms")
plt.xlabel("Number of Bathrooms")
plt.ylabel("Average Price") 
plt.xticks(rotation=45)
st.pyplot(plt)  # Display the plot on the app

with st.expander("See explanation"):
    st.write(""" The bar chart illustrates a general upward trend in average prices with an increase in the number of bathrooms.

However, there is some fluctuation in this trend, particularly for properties with a very high number of bathrooms

""")

#Broker performance analysis
#Identifying the top 10 brokers by number of properties sold
st.subheader("Top 10 Brokers by Number of Properties Sold")

plt.figure(figsize=(10,6))
df['BROKERTITLE'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Brokers by Number of Properties Sold")
plt.xlabel("Broker")
plt.ylabel("Number of Properties Sold")
#plt.xticks(rotation=45)
st.pyplot(plt)  # Display the plot on the app

#Analyzing the performance of the top 10 brokers by average price
st.subheader("Top 10 Brokers by Average Price")

plt.figure(figsize=(10,6))
df.groupby('BROKERTITLE')['PRICE'].mean().sort_values(ascending=False).head(10).plot(kind='bar')
plt.title("Top 10 Brokers by Average Price")
plt.xlabel("Broker")
plt.ylabel("Average Price")
#plt.yscale('log')  # using log scale due to wide range of prices
st.pyplot(plt)  # Display the plot on the app

with st.expander("See explanation"):
    st.write(""" There is a noticeable variation in average prices among different brokers, suggesting that broker choice might have an influence on the pricing of properties.

Some brokers appear to specialize in higher-priced properties, which could indicate a focus on luxury or premium real estate markets.

""")





