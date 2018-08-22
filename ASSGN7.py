## HOUSE PRICE PREDCTION 

#this data set predicts the house price based on number of factors like location of house,condition of house,number of bathrooms etc.
#Seaborn and Pandas provides a wide range of opportunities for visual analysis of  data.
#data is in csv(comma separated values) format

#importing the required libraries
import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd
import numpy as np
%matplotlib inline
#importing the data set
df = pd.read_csv("kc_house_data.csv")
df
# this will return the first five rows of data set
df.head()
# this is used to calculate the statstical data of the data set
df.describe()
# checking the null values in a data set
df.isnull().sum()
df.columns
## UNIVARIATE ANALYSIS:

#analysis done using one variable 
plt.hist(df["price"]) # price is less than 1000000
sn.countplot(x="bedrooms",data=df) #most houses have 3-4 bedrooms
sn.countplot(x="floors",data=df) #most houses have 1-2 floorings
sn.distplot(df["yr_built"],kde=True) # most of the houses were built in 1960-2020
sn.kdeplot(df["lat"],shade=True, color="r",bw=.001) # houses are present at
latitudinal scale of 47.5-47.7
sn.boxplot(x="price",data=df) #houses have price less than 1000000 nd this plot
has many outliers
sn.distplot(df["bedrooms"],kde=False) #most houses have 0-5 bedrooms
## BIVARIATE ANALYSIS

# analysis of two variables
#Compute pairwise correlation of columns

df.corr()
plt.scatter(df["price"],df["floors"],c="g") # houses with 1-2 floors have
pricing less than 3000000
sn.jointplot(df["price"],df["floors"],color="r") # houses with 1-2 floors have
pricing less than 3000000 along with their distribution
plt.figure(figsize=(10,8)) # The houses located at 47.0-47.2 latitude are
cheaper than the houses present between 47.4-47.8 latitude.
sn.kdeplot(df["price"],df["lat"])
sn.jointplot(df["price"],df["sqft_living15"],kind="hex", color="r") # The
houses having living area less than 4000 sqft have prices less than 1000000.
plt.figure(figsize=(10,8)) #Most of the houses built after 2000 are in good
condition.
sn.stripplot(x="condition",y="yr_built",data=df)
var=df.head(5) # houses having good condition have price less 
sn.boxplot(x="price",y="condition",data=var)
## MULTIVARIATE ANALYSIS

# analysis of more than two variables
plt.figure(figsize=(10,8)) # it describes every variable mapping with every
variable
corr=df.corr()
sn.heatmap(corr)
sn.pairplot(df) # pairwise relationshp between variables
