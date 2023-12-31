# -*- coding: utf-8 -*-
"""Simple Linear Regression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-HRPcrChzQ0pmr02xhSs9Y2hnF23Gtkb

**`Importing Libraries`**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

#@title Importing Data
dataset = pd.read_csv('Salaries.csv')

#@title check the Head of the data set to ensure that our data set is successfully attained
dataset.head(5)

#@title check the column names
dataset.columns

#@title remove the useless commons
dataset.drop(['Unnamed: 8', 'Unnamed: 9',
       'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12'],axis = 'columns',inplace = True)

#@title again cross check
dataset.head(5)

#@title Check is there any null value our X axis data set
dataset['BasePay'].isnull().values.any()

#@title enlist the indices of the null values
dataset[dataset['BasePay'].isnull()].index.tolist()

dataset[dataset['BasePay'] == 'Not Provided']

dataset.drop([148646,148651,148652,148650], axis = 'rows',inplace = True)

"""# X axis Data pre-processing"""

x = dataset.iloc[:,2].values.reshape(-1,1)

x.shape

#@title data preprocessing
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan , strategy='mean')
imputer.fit(x)
x = imputer.transform(x)

np.where(np.isnan(x))

"""
# Our X Axis Datapoints Are Preprocessed Now"""

# ------------------------------------------Y - axis---------------------------------------------------------------

y = dataset.iloc[:,-1].values

y

np.where(np.isnan(y))

#@title Visuallizing of the results
plt.scatter(x,y)

from sklearn.model_selection import train_test_split
x_train ,x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state =1)

from sklearn.linear_model import LinearRegression
regressor  = LinearRegression()
regressor.fit(x_train,y_train)

x_pred = regressor.predict(x_train)

x_pred

y_pred = regressor.predict(x_test)

y_pred

score = r2_score(y_train,x_pred)

score

plt.scatter(x_train,y_train)
plt.plot(x_train,x_pred, color = 'red')
plt.show()

plt.scatter(x_test,y_test)
plt.plot(x_test,y_pred, color = 'red')
plt.show()