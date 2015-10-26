# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 15:00:12 2015

@author: fabianbaier
"""

# Importing the earthquake set
# earthquakes 2014-10-25 to 2015-10-25 
# from http://earthquake.usgs.gov/earthquakes/search/
# http://earthquake.usgs.gov/earthquakes/feed/v1.0/glossary.php

import pandas as pd
eq = pd.read_csv('data/eq.csv')

# Importing the San Francisco AP weather set
# earthquakes 2014-10-01 to 2015-10-24 
# from http://w2.weather.gov/climate/xmacis.php?wfo=mtr
# daily data for a month consolidated in one csv file

weather = pd.read_csv('data/weather.csv')

weather = pd.DataFrame(weather)

# Preparing the data
# Adding a weather column
def weather():
    for i in range(eq.time.shape[0]):
        end = eq.time[i].find('T') # We are just interested in the date not the time
        date = eq.time[i][:end] # Getting the date, like 2014-12-24
        maxtemp = weather[weather.Date == date].Max # Finding the date in the weather data set
        maxtemp = maxtemp.values[0] # Getting the max temperature value
        eq.set_value(i, 'MaxTemp', maxtemp) # Adding the max temperature to the specific day


'''
MACHINE LEARNING WITH KNN
'''    

X, y = eq['MaxTemp'].values, eq['mag'].values
X.shape
y.shape

# predict y with KNN, k=1
from sklearn.neighbors import KNeighborsClassifier  # import class
y = eq['mag'].astype(int)
knn = KNeighborsClassifier(n_neighbors=1)           # instantiate the estimator
X = X.reshape(1228,1)
y = y.reshape(1228,1)
knn.fit(X, y)                                       # fit with data

knn.predict([87])  

knn.score(X, y)

# predict y with KNN, k=2
y = eq['mag'].astype(int)
knn = KNeighborsClassifier(n_neighbors=2)           # instantiate the estimator
X = X.reshape(1228,1)
y = y.reshape(1228,1)
knn.fit(X, y)                                       # fit with data

knn.predict([87])  

knn.score(X, y)

# predict y with KNN, k=3
y = eq['mag'].astype(int)
knn = KNeighborsClassifier(n_neighbors=3)           # instantiate the estimator
X = X.reshape(1228,1)
y = y.reshape(1228,1)
knn.fit(X, y)                                       # fit with data

knn.predict([87])  

knn.score(X, y)

# predict y with KNN, k=5
y = eq['mag'].astype(int)
knn = KNeighborsClassifier(n_neighbors=5)           # instantiate the estimator
X = X.reshape(1228,1)
y = y.reshape(1228,1)
knn.fit(X, y)                                       # fit with data

knn.predict([78])  

knn.score(X, y)

# Applying this in the next draft https://github.com/sinanuozdemir/SF_DAT_17/blob/master/code/06_model_evaluation_procedures.py



eq                 
eq.head(5)          # Look at the top x observations
eq.tail()            # Bottom x observations (defaults to 5)
eq.describe()        # describe any numeric columns (unless all columns are non-numeric)
eq.index             # "the index" (aka "the labels")
eq.columns           # column names (which is "an index")
eq.shape 		    # gives us a tuple of (# rows, # cols)

eq.mag.describe()  # describe the magnitude column
eq.mag.isnull().sum() # count missing values

eq.plot(x = 'time', y = 'mag', legend = False)

eq.groupby('mag').head()

eq = eq.values

eq.time