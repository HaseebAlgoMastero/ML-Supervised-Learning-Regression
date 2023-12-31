# -*- coding: utf-8 -*-
"""Random Forest Regression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10NiWN8-thlgYR1Sh2eq4jkjYJcEQIvB7
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

dataset = pd.read_csv('Salaries.csv')

dataset.drop(['Unnamed: 8', 'Unnamed: 9','Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12'],axis = 'columns',inplace = True)

dataset.head(5)

dataset[dataset['BasePay'] == 'Not Provided']

dataset.drop([148646,148651,148652,148650], axis = 'rows',inplace = True)

x = dataset.iloc[:,2].values.reshape(-1,1)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan , strategy='mean')
imputer.fit(x)
x = imputer.transform(x)

x

y = dataset.iloc[:,-1].values

plt.scatter(x,y)

from sklearn.model_selection import train_test_split
x_train ,x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state =1)

from sklearn.preprocessing import StandardScaler
sc_x  = StandardScaler()
sc_x.fit_transform(x_train)
sc_x.transform(x_test)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 25, random_state = 1,)
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)

r2_score(y_test,y_pred)